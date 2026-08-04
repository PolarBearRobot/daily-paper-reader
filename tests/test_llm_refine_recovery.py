import importlib.util
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch


def _load_module(module_name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


class LlmRefineRecoveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = pathlib.Path(__file__).resolve().parents[1]
        src_dir = root / "src"
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        cls.mod = _load_module("llm_refine_mod_recovery", src_dir / "4.llm_refine_papers.py")

    def relevant_result(self, paper_id="p-1", score=8):
        return {
            "id": paper_id,
            "matched_requirement_index": 1,
            "evidence_en": "relevant method",
            "evidence_cn": "相关方法",
            "tldr_en": "This paper is relevant because it studies a method that matches the requested research direction and provides useful technical evidence.",
            "tldr_cn": "这篇论文围绕用户关注的研究方向展开，提出了与需求高度相关的方法框架。它不仅说明了核心问题和技术路线，也给出了可用于判断相关性的实验或理论依据。整体上，该论文可以作为后续精读和方法比较的重要候选，并帮助用户快速判断是否值得继续阅读原文，同时为相近主题的论文筛选提供稳定参考。",
            "title_zh": "中文标题",
            "motivation_cn": "论文动机直接对应用户检索需求，关注当前方法在目标任务中仍然存在的关键不足。",
            "method_cn": "论文方法围绕需求中的技术核心展开，给出了较明确的建模思路、算法流程或实现策略。",
            "result_cn": "论文结果显示该方法在相关任务或实验设置中取得了有效提升，具备进一步参考价值。",
            "conclusion_cn": "论文结论表明该方向具有继续探索价值，并能为用户关注的问题提供可复用思路。",
            "score": score,
        }

    def test_recover_filter_results_retries_for_missing_ids(self):
        docs = [
            {"id": "p-1", "content": "doc1"},
            {"id": "p-2", "content": "doc2"},
        ]
        calls = []

        def runner(batch_docs, attempt, retry_note):
            calls.append((tuple(item["id"] for item in batch_docs), attempt, retry_note))
            if attempt == 1:
                return [
                    self.relevant_result("p-1"),
                ]
            return [
                self.relevant_result("p-1"),
                self.relevant_result("p-2", score=7),
            ]

        out = self.mod.recover_filter_results(docs, runner, max_attempts=2, debug_tag="batch_test")
        self.assertEqual([item["id"] for item in out], ["p-1", "p-2"])
        self.assertEqual(len(calls), 2)
        self.assertIn("p-1, p-2", calls[1][2])
        self.assertIn("missing ids=p-2", calls[1][2])

    def test_recover_filter_results_split_batch_after_retry_exhausted(self):
        docs = [
            {"id": "p-1", "content": "doc1"},
            {"id": "p-2", "content": "doc2"},
        ]
        calls = []

        def runner(batch_docs, attempt, retry_note):
            doc_ids = tuple(item["id"] for item in batch_docs)
            calls.append((doc_ids, attempt))
            if len(batch_docs) == 1:
                return [
                    self.relevant_result(batch_docs[0]["id"], score=6)
                ]
            return [
                self.relevant_result("p-1", score=6),
            ]

        out = self.mod.recover_filter_results(docs, runner, max_attempts=1, debug_tag="split_test")
        self.assertEqual([item["id"] for item in out], ["p-1", "p-2"])
        self.assertIn((("p-1",), 1), calls)
        self.assertIn((("p-2",), 1), calls)

    def test_recover_filter_results_splits_immediately_on_truncated_output(self):
        docs = [
            {"id": "p-1", "content": "doc1"},
            {"id": "p-2", "content": "doc2"},
        ]
        calls = []

        def runner(batch_docs, attempt, retry_note):
            doc_ids = tuple(item["id"] for item in batch_docs)
            calls.append((doc_ids, attempt))
            if len(batch_docs) > 1:
                raise self.mod.FilterOutputTruncatedError("unexpected finish_reason: length")
            return [
                self.relevant_result(batch_docs[0]["id"], score=6)
            ]

        out = self.mod.recover_filter_results(docs, runner, max_attempts=3, debug_tag="length_test")

        self.assertEqual([item["id"] for item in out], ["p-1", "p-2"])
        self.assertEqual(calls.count((("p-1", "p-2"), 1)), 1)
        self.assertNotIn((("p-1", "p-2"), 2), calls)
        self.assertIn((("p-1",), 1), calls)
        self.assertIn((("p-2",), 1), calls)

    def test_recover_filter_results_accepts_short_best_effort_fields(self):
        docs = [
            {"id": "p-1", "content": "doc1"},
        ]
        calls = []

        def runner(batch_docs, attempt, retry_note):
            calls.append((tuple(item["id"] for item in batch_docs), attempt, retry_note))
            return [
                {
                    **self.relevant_result("p-1", score=8),
                    "tldr_cn": "相关，但摘要信息有限。",
                    "motivation_cn": "信息有限。",
                    "method_cn": "信息有限。",
                    "result_cn": "信息有限。",
                    "conclusion_cn": "信息有限。",
                }
            ]

        out = self.mod.recover_filter_results(docs, runner, max_attempts=3, debug_tag="short_test")

        self.assertEqual(out[0]["id"], "p-1")
        self.assertEqual(out[0]["tldr_cn"], "相关，但摘要信息有限。")
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][1], 1)
        self.assertEqual(calls[0][2], "")

    def test_recover_filter_results_does_not_retry_balance_error(self):
        docs = [{"id": "p-1", "content": "doc1"}]
        calls = []
        response = MagicMock()
        response.status_code = 402
        response.json.return_value = {"error": {"message": "Insufficient Balance"}}
        error = Exception("402 Client Error: Payment Required")
        error.response = response

        def runner(batch_docs, attempt, retry_note):
            calls.append((batch_docs, attempt, retry_note))
            raise error

        with self.assertRaises(Exception) as ctx:
            self.mod.recover_filter_results(docs, runner, max_attempts=3, debug_tag="billing")

        self.assertIs(ctx.exception, error)
        self.assertEqual(len(calls), 1)

    def test_process_file_saves_unrefined_fallback_on_balance_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = pathlib.Path(tmpdir) / "input.json"
            output_path = pathlib.Path(tmpdir) / "output.json"
            payload = {
                "papers": [{"id": "p-1", "title": "Paper", "abstract": "Abstract"}],
                "queries": [
                    {
                        "paper_tag": "query:test",
                        "ranked": [{"paper_id": "p-1", "star_rating": 5}],
                    }
                ],
                "llm_ranked": [{"paper_id": "stale"}],
            }
            input_path.write_text(json.dumps(payload), encoding="utf-8")

            response = MagicMock()
            response.status_code = 402
            response.json.return_value = {"error": {"message": "Insufficient Balance"}}
            error = Exception("402 Client Error: Payment Required")
            error.response = response

            with patch.dict(os.environ, {"DEEPSEEK_API_KEY": "depleted-key"}, clear=False), patch.object(
                self.mod,
                "build_user_requirements",
                return_value=[{"id": "req-1", "query": "test", "tag": "query:test"}],
            ), patch.object(self.mod, "_filter_batch", side_effect=error) as mock_filter:
                self.mod.process_file(
                    input_path=str(input_path),
                    output_path=str(output_path),
                    config_path=None,
                    min_star=4,
                    batch_size=10,
                    max_chars=850,
                    filter_model="deepseek-v4-flash",
                    max_output_tokens=1024,
                    filter_concurrency=1,
                )

            saved = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertNotIn("llm_ranked", saved)
            self.assertNotIn("llm_ranked_at", saved)
            self.assertEqual(saved["papers"], payload["papers"])
            self.assertEqual(mock_filter.call_count, 1)

    def test_process_file_stops_missing_doc_recovery_on_balance_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = pathlib.Path(tmpdir) / "input.json"
            output_path = pathlib.Path(tmpdir) / "output.json"
            payload = {
                "papers": [
                    {"id": "p-1", "title": "Paper 1", "abstract": "A"},
                    {"id": "p-2", "title": "Paper 2", "abstract": "B"},
                ],
                "queries": [
                    {
                        "paper_tag": "query:test",
                        "ranked": [
                            {"paper_id": "p-1", "star_rating": 5},
                            {"paper_id": "p-2", "star_rating": 5},
                        ],
                    }
                ],
            }
            input_path.write_text(json.dumps(payload), encoding="utf-8")

            response = MagicMock()
            response.status_code = 402
            response.json.return_value = {"error": {"message": "Insufficient Balance"}}
            billing_error = Exception("402 Client Error: Payment Required")
            billing_error.response = response
            recovery_calls = []

            def recovery_runner(_docs, _attempt, _retry_note):
                recovery_calls.append(1)
                raise billing_error

            with patch.dict(os.environ, {"DEEPSEEK_API_KEY": "depleted-key"}, clear=False), patch.object(
                self.mod,
                "build_user_requirements",
                return_value=[{"id": "req-1", "query": "test", "tag": "query:test"}],
            ), patch.object(
                self.mod,
                "_filter_batch",
                side_effect=RuntimeError("temporary batch failure"),
            ), patch.object(
                self.mod,
                "_make_filter_runner",
                return_value=recovery_runner,
            ):
                self.mod.process_file(
                    input_path=str(input_path),
                    output_path=str(output_path),
                    config_path=None,
                    min_star=4,
                    batch_size=10,
                    max_chars=850,
                    filter_model="deepseek-v4-flash",
                    max_output_tokens=1024,
                    filter_concurrency=1,
                )

            saved = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertNotIn("llm_ranked", saved)
            self.assertEqual(len(recovery_calls), 1)

    def test_call_filter_repeats_user_prompt_with_separator(self):
        captured = {}
        test_case = self

        class FakeClient:
            model = "gemini-3-flash-preview-nothinking"

            def chat_structured(self, messages, schema_name, schema, strict, allow_json_object_fallback):
                captured["messages"] = messages
                captured["schema_name"] = schema_name
                captured["schema"] = schema
                captured["strict"] = strict
                captured["allow_json_object_fallback"] = allow_json_object_fallback
                return {
                    "content": (
                        '{"results":[{"id":"p-1","matched_requirement_index":1,'
                        '"evidence_en":"ok","evidence_cn":"相关","tldr_en":"ok","tldr_cn":"相关","score":8}]}'
                    ),
                    "parsed": {
                        "results": [test_case.relevant_result("p-1")]
                    },
                    "parse_error": None,
                    "refusal": "",
                    "finish_reason": "stop",
                }

        out = self.mod.call_filter(
            client=FakeClient(),
            all_requirements=[
                {
                    "id": "req-1",
                    "query": "symbolic regression methods",
                    "tag": "query:sr",
                    "kind": "direct",
                    "description_en": "Find papers relevant to symbolic regression methods",
                }
            ],
            docs=[{"id": "p-1", "content": "Title: A\nAbstract: B"}],
            debug_dir="",
            debug_tag="prompt_test",
        )

        self.assertEqual(out[0]["id"], "p-1")
        self.assertEqual(out[0]["title_zh"], "中文标题")
        self.assertIn("论文方法围绕需求", out[0]["method_cn"])
        user_content = captured["messages"][1]["content"]
        self.assertEqual(captured["schema_name"], "rerank_batch")
        self.assertTrue(captured["strict"])
        self.assertTrue(captured["allow_json_object_fallback"])
        self.assertIn("Let me repeat that:", user_content)
        self.assertEqual(user_content.count("User requirements list:"), 2)
        self.assertEqual(user_content.count("Papers:"), 2)
        self.assertIn("method_cn", user_content)
        self.assertIn("title_zh", user_content)
        self.assertIn("150-220 Chinese characters", user_content)
        self.assertIn("30-70 Chinese characters", user_content)
        self.assertIn("length targets are guidance", user_content)
        self.assertIn("same style as a paper-page TLDR abstract", user_content)
        self.assertNotIn("<= 60 Chinese characters", user_content)
        self.assertTrue(user_content.rstrip().endswith("Output must be strict JSON only, no markdown, no fences, no extra text."))


if __name__ == "__main__":
    unittest.main()
