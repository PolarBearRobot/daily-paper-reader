---
title: "NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation"
title_zh: NoTVLA：通过稀疏化动作轨迹实现可泛化的机器人操作
authors: "Zheng Huang, Mingyu Liu, Xiaoyi Lin, Muzhi Zhu, Canyu Zhao, Zongze Du, Xiaoman Li, Yiduo Jia, Hao Zhong, Hao Chen, Chunhua Shen"
date: 2025-09-01
pdf: "https://openreview.net/pdf?id=GtyMclqDqY"
tags: ["query:model"]
score: 8.0
evidence: NoTVLA通过预测稀疏航点而非密集轨迹来缓解VLA的灾难性遗忘。
tldr: 将VLM微调为VLA时因密集动作轨迹与预训练目标冲突导致灾难性遗忘，本文提出NoTVLA，将动作生成转变为预测稀疏语义三维航点，从而缓解遗忘并保留VLM的推理能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: VLM微调为VLA时，生成密集动作轨迹会与预训练目标冲突，导致灾难性遗忘。
method: NoTVLA框架将动作生成重构为预测稀疏且有语义的三维航点序列。
result: 在多个实验中，NoTVLA在保持VLM推理能力的同时提升了操作泛化性。
conclusion: NoTVLA提供了一种缓解VLA灾难性遗忘的有效方案，有助于构建更通用的机器人模型。
---

## Abstract
A common method for creating Vision-Language-Action (VLA) models involves fine-tuning pre-trained Vision-Language Models (VLMs) for robotic control. However, this adaptation process often leads to \textbf{catastrophic forgetting}, where the VLM's original powerful reasoning capabilities are degraded. We identify that this issue stems from a fundamental task conflict: fine-tuning on dense, continuous action trajectories is misaligned with the VLM's pre-training objectives. To tackle this, we propose the \textbf{Narrowing of Trajectory VLA (NoTVLA)} framework, which mitigates catastrophic forgetting by reframing the action generation task. Instead of dense trajectories, NoTVLA learns to predict sparse, semantically meaningful trajectory 3D points leading to keyframes.
This approach aligns the fine-tuning task more closely with the VLM's inherent strengths, preserving its reasoning abilities. A key innovation of NoTVLA lies in its trajectory planning strategy, which uses temporal compression and spatial pruning for the robot end-effector's path. In multi-task evaluations, NoTVLA achieves superior performance and generalization compared to baselines like $\pi_0$, while using over an order of magnitude less compute and not necessarily need wrist-mounted camera.
This design ensures that NoTVLA’s operational accuracy closely approximates that of single-task expert models. Crucially, by mitigating catastrophic forgetting, it preserves the model’s inherent language capabilities, enabling \textbf{zero-shot generalization} in specific scenarios, supporting unified model deployment \textbf{across multiple robot platforms}, and fostering generalization even when \textbf{perceiving tasks from novel perspectives}.

---

## 论文详细总结（自动生成）

您提供的论文 PDF 提取文本不包含实际论文正文，仅显示 OpenReview 的验证页面提示，无法获取论文内容。因此，无法基于此生成结构化总结。请提供完整的论文文字内容后再试。

（完）
