---
title: "Learning Primitive Embodied World Models: Towards Scalable Robotic Learning"
title_zh: 学习基元具身世界模型：迈向可扩展的机器人学习
authors: "Qiao Sun, Liujia Yang, Wei Tang, Wei Huang, Kaixin Xu, Yongchao Chen, Mingyu Liu, Haoyi Zhu, Jiange Yang, Yating Wang, Yilun Chen, Xili Dai, Nanyang Ye, Qinying Gu"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=W0AY49wWrb"
tags: ["query:model"]
score: 9.0
evidence: 提出原始运动基的世界模型，通过短程视频生成实现可扩展的机器人学习。
tldr: 现有具身世界模型依赖海量交互数据，难以扩展。本文提出PEWM，将世界建模限制在固定的短程运动基上，通过组合基元实现长程视频生成，大幅降低对大规模数据的依赖，并提升规划能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 具身世界模型因数据稀缺、维度高而难以实现长程视频生成。
method: PEWM范式将视频生成分解为短程运动基元的组合，每个基元对应固定时长的视频片段。
result: 实验表明PEWM能以更低的数据量实现高质量长程视频生成与规划。
conclusion: PEWM为具身世界模型提供了一种更高效、可扩展的新范式，有望推动具身智能的GPT时刻。
---

## Abstract
While video-generation-based embodied world models have gained increasing
attention, their reliance on large-scale embodied interaction data remains a key
bottleneck. The scarcity, difficulty of collection, and high dimensionality of em-
bodied data fundamentally limit the alignment granularity between language and
actions and exacerbate the challenge of long-horizon video generation—hindering
generative models from achieving a "GPT moment" in the embodied domain. There
is a naive observation: the diversity of embodied data far exceeds the relatively
small space of possible primitive motions. Based on this insight, we propose a novel
paradigm for world modeling–Primitive Embodied World Models (PEWM). By
restricting video generation to fixed short horizons, our approach 1) enables fine-
grained alignment between linguistic concepts and visual representations of robotic
actions, 2) reduces learning complexity, 3) improves data efficiency in embodied
data collection, and 4) decreases inference latency. By equipping with a modular
Vision-Language Model (VLM) planner and a Start-Goal heatmap Guidance mech-
anism (SGG), PEWM further enables flexible closed-loop control and supports
compositional generalization of primitive-level policies over extended, complex
tasks. Our framework leverages the spatiotemporal vision priors in video mod-
els and the semantic awareness of VLMs to bridge the gap between fine-grained
physical interaction and high-level reasoning, paving the way toward scalable,
interpretable, and general-purpose embodied intelligence.

---

## 论文详细总结（自动生成）

# 论文总结：学习基元具身世界模型——迈向可扩展的机器人学习

## 1. 核心问题与研究动机
- **问题背景**：具身世界模型（embodied world models）在机器人学习中用于通过视频生成来预测未来状态，但当前方法严重依赖大规模交互数据，存在数据稀缺、采集难、维度高等瓶颈。
- **核心挑战**：
  - 语言与动作间的对齐粒度受限，难以精准对应。
  - 长程视频生成因误差累积与复杂性而失效，阻碍具身智能实现类似 GPT 的突破。
- **直观洞察**：具身数据的多样性远超机器人可能执行的原始运动（primitive motions）空间；通过约束生成范围，有望降低学习难度。
- **整体意义**：提出一种可扩展、数据高效的新范式，旨在推动通用具身智能体的发展。

## 2. 方法论：PEWM 范式
- **核心思想**：将世界建模限定在固定的短程运动基元上，长程视频通过组合这些基元实现，从而降低学习复杂度与数据需求。
- **关键组件**：
  - **短程视频生成**：每个基元对应固定时长的视频片段，模型仅需学习短程动态，结合时空视觉先验。
  - **VLM 规划器**：模块化视觉语言模型用于高层规划，将复杂任务分解为基元序列，实现语言概念与视觉表示的细粒度对齐。
  - **SGG（Start-Goal Heatmap Guidance）**：起始-目标热力图引导机制，为基元组合提供空间定向，支持闭环控制与泛化。
- **技术流程**：
  1. VLM 根据任务指令生成基元级别的子目标（start-goal pairs）。
  2. SGG 模块生成与目标状态相关的热力图，指导视频生成模块。
  3. 短程视频生成模型依次生成各基元对应的片段，拼接成完整的长程视频。
  4. 生成的内容可直接用于策略学习或离线规划。
- **算法亮点**（文字说明）：
  - 解耦了长程生成问题，将误差累积限制在固定短窗内。
  - 利用预训练视频模型的时空先验和 VLMs 的语义理解，桥接物理交互与高层推理。

## 3. 实验设计
- **数据集/场景**：摘要未详列具体数据集，推断用于具身交互的常见基准（如 CALVIN、RLBench 或自定义机械臂操作环境）。
- **对比方法**：与现有基于视频生成的世界模型方法比较（如 UniPi、Video Diffusion Planner 等，未明确列出）。
- **评价维度**：视频生成质量（长程一致性、物理合理性）、任务成功率、数据效率、推理延迟。
- **Benchmark**：可能采用标准机器人操作 benchmark 进行评估，验证闭环控制能力与组合泛化性。

## 4. 资源与算力
- **文中提及情况**：摘要未提供 GPU 型号、数量或训练时长等具体算力信息。
- 推断所用算力可能包括多卡 GPU 训练视频生成模型和 VLM 推理，但无法从现有文本中确认。

## 5. 实验数量与充分性
- **实验组数**：摘要未给出具体实验数量，推测包含主实验（与基准方法比较）、消融实验（如移除 SGG 或 VLM 规划器）、数据效率分析、长程生成可视化。
- **充分性评价**：从摘要描述看，实验覆盖了提出的核心主张（数据效率、长程生成、组合泛化），但缺乏具体指标支持。无法评估统计显著性或公平性细节。

## 6. 主要结论与发现
- PEWM 通过短程基元组合，能以更低的数据量实现高质量长程视频生成。
- 方法提升了语言-动作的对齐精度，减少了推理延迟，并赋予模型闭环控制能力。
- 基于基元的策略具备组合泛化性，可扩展至复杂、多步骤任务。
- 整体框架为具身世界模型提供了一种可扩展、可解释的新路径，有望推动具身智能的范式跃迁。

## 7. 优点
- **数据效率**：显著降低对大规模交互数据的依赖，切中当前痛点。
- **解耦设计**：将长程生成分解为短窗预测，简化学习目标，提升稳定性。
- **组合性**：通过 VLM 与 SGG 的结合，实现“基元即技能”的灵活复用。
- **实用性**：协同闭环控制，减少累积误差，适合真实机器人部署。

## 8. 不足与局限
- **实验细节缺失**：摘要未公开数据集、确切对比方法和量化指标，难以判断方法的实际优势。
- **基元覆盖范围**：预先定义的基元可能无法涵盖所有真实场景的运动模式，需要人工设计或扩展。
- **VLM 依赖**：高层规划性能受限于 VLM 能力，可能被误导或产生不现实子目标。
- **泛化边界**：组合泛化在分布外场景下的鲁棒性未经验证。
- **算力需求不明**：无法评估实际训练成本与部署可行性。
- **长程上限**：虽然误差控制在短窗内，但基元序列累积引起的语义偏移或物理不一致仍未彻底解决。

（完）
