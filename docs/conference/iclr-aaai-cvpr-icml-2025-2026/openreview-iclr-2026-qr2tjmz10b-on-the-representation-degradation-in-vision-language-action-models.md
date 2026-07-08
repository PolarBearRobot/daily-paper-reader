---
title: On the Representation Degradation in Vision-Language-Action Models
title_zh: 视觉-语言-动作模型中的表征退化研究
authors: "Zhilong Zhang, Xiong-Hui Chen, Yidi Wang, Yihao Sun, Wenyu Luo, Haoxiang Ren, Haoxin Lin, Yang Yu"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=qR2TjMZ10B"
tags: ["query:model"]
score: 9.0
evidence: 分析VLA表征退化问题并提出SWOL对齐深层与中层可泛化表征
tldr: VLA模型中深层表征常出现泛化退化，影响动作生成。本文通过逐层表征分析揭示该现象，提出SWOL方法，将退化的深层特征与未来观测推导的中层可泛化表征对齐，施加时间连续性约束。实验证明该方法能有效缓解退化，提升VLA模型的泛化能力，无需改动模型结构。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: VLA模型深层负责动作生成的表征泛化能力下降。
method: 提出SWOL，将深层特征与基于未来观测的外推中层表征对齐。
result: 减轻了表征退化，在多个任务上提升了策略的泛化性能。
conclusion: 表征对齐是提升VLA模型泛化性的高效手段。
---

## Abstract
Vision-Language-Action (VLA) models have become a promising paradigm for robotic decision-making, yet their application remains limited by generalization bottlenecks. In this paper, we conduct a layer-wise representation analysis and uncover a previously overlooked phenomenon of representation degradation: deeper layers tasked with action generation exhibit diminished generalization to both semantic information and environmental dynamics. To mitigate this issue, we introduce hidden Space WOrld modeLing (SWOL), a lightweight but efficient approach that aligns degraded deep-layer features with more generalizable mid-layer representations extrapolated from future observations. SWOL enforces temporally consistent, action-grounded representations without modifying model architecture or inference procedures. Extensive experiments in simulation and real-world settings demonstrate that SWOL alleviates representation degradation, leading to improved policy effectiveness and stronger generalization across modalities of vision, language, and dynamics.

---

## 论文详细总结（自动生成）

# 论文总结：视觉-语言-动作模型中的表征退化研究

## 1. 论文的核心问题与整体含义
- **研究背景**：视觉-语言-动作（VLA）模型已成为机器人决策领域的重要范式，但其实际应用仍受限于泛化瓶颈。
- **核心问题**：论文发现 VLA 模型深层（靠近输出端）负责动作生成的表征，其泛化能力出现明显退化，即对语义信息和环境动态的泛化性下降，这一现象之前被忽视。
- **整体含义**：该研究旨在揭示 VLA 模型的表征退化现象，并提出一种轻量方法缓解该问题，从而提升模型在视觉、语言和动态环境下的泛化能力，具有很强的理论与实践价值。

## 2. 方法论
- **核心思想**：通过表征分析定位退化现象，将退化严重的深层特征与更具泛化性的中层表征进行对齐，而非直接修改原始模型结构或推理流程。
- **关键技术细节**：
  - 进行逐层表征分析，发现深层特征泛化性明显低于中层特征。
  - 提出 **SWOL（hidden Space WOrld modeLing）** 方法：
    - 利用未来观测信息，从中层表征中推导或外推出更具泛化性的中间表示。
    - 将退化的深层特征与这些外推得到的中层可泛化表征进行对齐。
    - 在训练中施加时间一致性约束，以确保表征在动作层面保持时序稳定和因果一致。
- **公式/算法流程**：虽然摘要未给出具体公式，其总体流程可概括为：
  1. 获取当前观测下模型各层特征；
  2. 利用未来观测信息在中层构建一个“世界模型”式的泛化表征；
  3. 在训练时对齐深层特征与该中层外推表征，并施加时间一致性损失；
  4. 推理时不改变模型结构，仅通过训练获得的更好泛化性直接提升动作生成质量。

## 3. 实验设计
- **数据集/场景**：论文在模拟环境与真实世界场景中均开展了实验（摘要提到“Extensive experiments in simulation and real-world settings”），但未列出具体数据集名称或任务。
- **Benchmark**：未在摘要中指明特定基准；从泛化评估角度，可能涉及视觉泛化、语言指令泛化和动态环境泛化等多个维度。
- **对比方法**：由于缺乏完整论文，无法确定具体对比的基线模型；推测应包含原始 VLA 模型及其他表征对齐或泛化提升方法。

## 4. 资源与算力
- **文中提及情况**：摘要未提供任何关于 GPU 型号、数量、训练时长等算力资源信息。该部分需等待全文披露。

## 5. 实验数量与充分性
- **实验数量**：从摘要表述可推测至少包含：
  - 模拟环境与真实环境两大类实验；
  - 可能包含多组消融实验以验证 SWOL 不同组分的作用；
  - 跨模态（视觉、语言、动态）泛化测试。
- **充分性与公平性**：摘要强调实验“广泛”，但未给出具体统计量或对比条目。从方法论设计看，SWOL 不改变模型架构，对比原始模型相对公平。然而，缺少具体实验细节使得难以充分评判其充分性与客观性。

## 6. 论文的主要结论与发现
- 首次揭示 VLA 模型中深层表征的泛化退化现象。
- 提出 SWOL 方法，通过将退化的深层特征与基于未来观测推导的中层可泛化表征对齐，成功缓解了表征退化。
- SWOL 在多种任务上提升了策略的有效性和泛化性能，且无需改动模型结构，具有即插即用的优越性。

## 7. 优点
- **问题新颖**：发现并定义 VLA 表征退化这一先前被忽视的关键现象，具有启发意义。
- **方法轻量高效**：SWOL 仅通过表征对齐和时间约束训练，不修改架构、不增加推理负担，易于集成到现有 VLA 流程中。
- **实验全面**：涵盖模拟与真实环境，兼顾多模态泛化，增强了结论的可靠性。
- **表征对齐思路清晰**：利用未来观测外推中层表征来指导深层学习，提供了新的视角。

## 8. 不足与局限
- **信息缺失**：摘要未透露具体实验细节（如数据集、基准、对比方法），无法全面评估实验严谨性；算力资源也未说明。
- **深层退化成因未深究**：只揭示现象并缓解，未深入分析退化产生的原因，未来或可结合可解释性研究。
- **外推限制**：利用未来观测推导中层表征可能依赖环境的可预测性，在高度随机或非平稳环境中效果待验证。
- **扩展性**：仅针对 VLA 模型，在其他类型序列决策模型中的适用性尚未探讨。

（完）
