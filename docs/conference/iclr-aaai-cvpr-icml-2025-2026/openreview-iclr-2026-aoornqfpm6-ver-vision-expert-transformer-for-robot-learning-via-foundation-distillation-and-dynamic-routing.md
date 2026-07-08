---
title: "VER: Vision Expert Transformer for Robot Learning via Foundation Distillation and Dynamic Routing"
title_zh: VER：通过基础模型蒸馏与动态路由实现机器人学习的视觉专家Transformer
authors: "Yixiao Wang, Mingxiao Huo, Zhixuan Liang, Yushi Du, Lingfeng Sun, Haotian Lin, Jinghuan Shang, Chensheng Peng, Mohit Bansal, Mingyu Ding, Masayoshi Tomizuka"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=aoorNQFpM6"
tags: ["query:model"]
score: 9.0
evidence: 将多个视觉基础模型蒸馏为机器人视觉专家，动态选择任务相关表示。
tldr: 单个视觉基础模型难以覆盖所有机器人任务，本文提出VER，将多个视觉基础模型蒸馏成一个专家库，并通过可训练的路由网络为下游任务动态组合专家特征，实现高效且灵活的视觉表征学习。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 单一视觉基础模型在不同机器人任务上表现不一，缺乏通用性。
method: VER预训练蒸馏多个视觉基础模型形成专家库，微调时仅训练少量参数的路由网络动态选择专家。
result: 在多种机器人操纵任务上，VER提升了任务性能且参数高效。
conclusion: VER为机器人学习提供了一种可扩展的视觉表征框架，有效融合多源视觉知识。
---

## Abstract
Pretrained vision foundation models (VFMs) advance robotic learning via rich visual representations, yet individual VFMs typically excel only in specific domains, limiting generality across tasks. Distilling multiple VFMs into a unified representation can mitigate this limitation but often yields inflexible task-specific feature selection and requires costly full retraining to incorporate robot-domain knowledge.
We propose VER, a Vision Expert transformer for Robot learning. During pretraining, VER distills multiple VFMs into a vision expert library. We then fine-tune only a lightweight routing network (fewer than 0.4% of parameters) to dynamically select task-relevant experts from the pretrained library for downstream robot tasks. We further introduce Patchwise Expert Routing with Curriculum Top-K Annealing to improve both flexibility and precision of dynamic expert selection. Moreover, VER supports parameter-efficient finetuning for scalable expert utilization and robot-domain knowledge integration. Across 17 diverse robotic tasks and multiple policy heads, VER achieves state-of-the-art performance. We find that VER reduces large-norm outliers in task-irrelevant regions (e.g., background) and concentrates on task-critical regions. More visualizations and codes are available in https://yixiaowang7.github.io/ver_page/.

---

## 论文详细总结（自动生成）

# VER 论文详细总结

## 1. 核心问题与整体含义
- **研究动机**：预训练的视觉基础模型（Vision Foundation Models, VFMs）在机器人学习中提供了丰富的视觉表示，但单一模型往往仅在特定领域表现突出，无法在所有任务上保持通用性。
- **现有方法局限**：将多个 VFM 蒸馏为一个统一表示是常见思路，但通常会产生僵化的任务特化特征选择，且需要高昂的完整再训练来整合机器人领域知识。
- **整体含义**：论文旨在解决多 VFM 知识融合中的通用性与灵活性矛盾，提出一种可扩展的框架，使机器人能够动态、高效地利用多种视觉专家知识，提升下游操作任务的性能。

## 2. 方法论
- **核心思想**：构建一个视觉专家 Transformer（VER），在预训练阶段将多个 VFM 蒸馏成一个**视觉专家库**；在下游任务微调时，仅训练一个轻量级**路由网络**（参数量少于 0.4%），动态选择任务相关的专家，从而避免对整个模型进行昂贵的重训练。
- **关键技术细节**：
  - **专家库构建**：预训练时，VER 从多个 VFM 中蒸馏知识，形成一组可组合的视觉专家表示。
  - **动态路由**：提出 **Patchwise Expert Routing with Curriculum Top-K Annealing**，在图像块级别进行专家选择，并通过课程式的 Top-K 退火策略逐步减少激活的专家数量，提升选择灵活性和精度。
  - **参数高效微调**：仅训练路由网络，专家库参数冻结，实现高效的专家利用和机器人领域知识整合。
- **流程简述**：
  1. 预训练：多 VFM 知识蒸馏 → 专家库。
  2. 下游适配：冻结专家库 → 训练路由网络 → 动态选择专家 → 输入策略头执行任务。

## 3. 实验设计
- **数据集 / 场景**：17 种不同的机器人操控任务（详情未在摘要中展开，但从结果看覆盖多个策略头和任务类型）。
- **Benchmark 与对比方法**：
  - 对比其他基于视觉基础模型的表示学习方法，可能包括单一 VFM、现有蒸馏方法等（摘要未列出具体名称，仅提到“多个 baseline”）。
  - 通过多种策略头（policy heads）评估 VER 的通用性。
- **评估指标**：任务性能（可能包含成功率等，摘要中未详述），并分析了特征可视化中的离群值抑制和任务关键区域聚焦。

## 4. 资源与算力
- 摘要及元数据中**未明确提及** GPU 型号、数量、训练时长等具体算力信息。
- 仅提到“仅训练路由网络（少于 0.4% 参数）”，暗示微调阶段计算开销极低，但预训练阶段的资源需求未披露。

## 5. 实验数量与充分性
- **实验数量**：覆盖 17 个机器人任务，采用多种策略头，并与多个基线对比，同时进行了可视化分析（如离群值分布）。若包含消融研究（如路由策略、专家数量等），实验规模合理。
- **充分性与客观性**：
  - 任务多样性较好，可评估跨任务泛化性。
  - 与多种方法对比，具备一定的公平性。
  - 但摘要未提及消融实验的具体设置、重复次数、统计显著性检验，无法完全判断实验严谨性。整体给读者的印象是实验较为充实。

## 6. 主要结论与发现
- VER 在 17 个机器人任务上取得了最先进的性能。
- 通过动态路由，VER 能够抑制与任务无关区域（如背景）的大范数离群点，并将注意力集中于任务关键区域。
- 仅训练极少参数的路由网络，即可高效利用多源视觉知识，实现可扩展的机器人视觉表示。

## 7. 优点
- **参数高效性**：微调参数量仅占 0.4% 以下，极大降低下游部署成本。
- **动态灵活选择**：Patchwise 路由与退火策略在细粒度层级实现了灵活的专家组合，避免僵化的特征选择。
- **多源蒸馏理念**：将“专家库”概念引入机器人学习，有效融合异构 VFM 知识，提升跨任务通用性。
- **可解释性分析**：通过离群值抑制等可视化，直观展示了模型如何聚焦于关键区域。

## 8. 不足与局限
- **算力信息缺失**：预训练阶段的训练成本未知，可能涉及较大规模的计算资源，限制更广泛复现。
- **任务类型局限**：虽然覆盖 17 个任务，但可能仅限模拟操控环境，真实机器人部署效果未验证。
- **专家库上限**：性能受限于所选 VFM 的上限，若某个任务无合适的 VFM 知识可蒸馏，可能难以弥补。
- **路由训练数据依赖**：动态路由依赖下游少量数据，若任务样本极少时路由可能不够准确。
- **对比方法不详**：摘要未列出具体对比模型，无法判断 SOTA 声明的相对优势与公平性细节。

（完）
