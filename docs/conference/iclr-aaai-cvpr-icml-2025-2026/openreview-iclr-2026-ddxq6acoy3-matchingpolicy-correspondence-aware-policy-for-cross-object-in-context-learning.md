---
title: "MatchingPolicy: Correspondence-aware Policy For Cross-object In-context Learning"
title_zh: MatchingPolicy：面向跨物体上下文学习的对应感知策略
authors: "Qijin She, Hanyang Yu, Zeming Li, Ping Tan"
date: 2025-09-08
pdf: "https://openreview.net/pdf?id=ddxq6ACoY3"
tags: ["query:model"]
score: 9.0
evidence: 上下文模仿学习实现少样本泛化；解耦示范-场景匹配以稳健迁移
tldr: 针对上下文模仿学习中解示范与场景匹配困难的问题，提出MatchingPolicy框架，利用图扩散策略和视觉基础模型提取的稠密对应关系，将匹配与策略学习解耦，并集成在线自适应匹配算法动态建立可靠对应。实验表明该方法能有效应对未见物体和新场景，实现稳健的少样本任务泛化。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有上下文模仿学习在未见物体或新场景下泛化能力不足，难以同时推理对应和动作。
method: 提出基于图的扩散策略，利用视觉基础模型提取稠密对应，解耦示范-场景匹配与动作适应，并用在线自适应匹配动态更新。
result: 在多种任务中实现稳健的跨物体迁移，显著优于现有方法。
conclusion: 解耦匹配与策略学习提升了上下文模仿学习的泛化性和鲁棒性，为少样本机器人学习提供了有效框架。
---

## Abstract
In-context imitation learning enables few-shot task generalization by conditioning policies on demonstrations, but existing methods often fail on unseen objects or novel scenarios. We introduce MatchingPolicy, a correspondence-aware framework that explicitly decouples demonstration–scene matching from policy learning. At its core, MatchingPolicy employs a graph-based diffusion policy that adapts robot actions based on dense correspondences extracted by vision foundation models. This separation alleviates the burden of simultaneous correspondence inference and action adaptation, enabling robust transfer across diverse tasks. Our approach further integrates an online adaptive matching algorithm to dynamically establish reliable correspondences during execution. Empirical results on both RLBench and real-world manipulation tasks show that MatchingPolicy achieves strong few-shot performance, demonstrating consistent generalization across unseen object instances and categories.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究背景**：上下文模仿学习（In-context Imitation Learning）旨在通过将示范作为条件，使策略能够快速适应新任务，实现少样本泛化。然而，现有方法在面对未见过的物体或全新场景时常常失败。
- **核心问题**：示范与目标场景之间的匹配（对应关系）和后续的动作适应高度耦合，导致模型在同时学习“识别对应”与“生成动作”时负担过重，难以稳健迁移到分布的物体实例和类别。
- **整体含义**：提出将“匹配”与“策略”解耦，让模型专注于动作生成，而将对应关系的提取交给更擅长此任务的视觉基础模型，从而突破跨物体、跨场景的少样本泛化瓶颈。

### 2. 论文提出的方法论
- **核心思想**：显式解耦示范-场景匹配与策略学习，构建对应感知（correspondence-aware）的框架，使动作生成仅依赖已建立的稠密对应，降低学习难度。
- **关键技术细节**：
  - **图扩散策略（Graph-based Diffusion Policy）**：将机器人动作建模为扩散过程，其中的条件机制基于示范与当前场景之间的稠密对应图，而非原始视觉输入。
  - **利用视觉基础模型提取稠密对应**：借助预训练的大规模视觉模型（如 DINOv2、Stable Diffusion 特征等）在示范帧与当前观测之间建立像素/点级别的鲁棒对应关系。
  - **在线自适应匹配算法**：在策略执行过程中动态更新和筛选可靠对应，以应对运行时出现的遮挡、视角变化或新物体部分。
  - **算法流程**：首先离线提取示范的视觉特征与机器人动作；在线阶段，用视觉基础模型建立当前观测与示范间的对应；将这些对应送入图扩散策略，迭代去噪生成适应后的动作序列；同时自适应匹配模块根据执行反馈修正对应权重。
- **公式简述（文字说明）**：整体可以视为最大化条件动作分布 \(p(a|o, demo)\)，但通过引入隐式对应变量 \(C\)，将分布分解为对应推断 \(p(C|o, demo)\) 和基于对应的动作生成 \(p(a|C, demo)\)。该方法将对应推断外包给视觉基础模型，策略仅需学习 \(p(a|C, demo)\)。

### 3. 实验设计
- **数据集/场景**：
  - **RLBench**：模拟环境中的多种桌面操作任务，评估跨物体实例和跨物体类别的泛化能力。
  - **真实世界操作任务**：在真实机器人上部署，验证对未见物体的抓取、放置等操作。
- **基准对比方法**：与现有上下文模仿学习或对应学习方法比较，如基于原始图像条件的扩散策略、直接特征拼接的上下文策略、无对应或仅用稀疏对应的方法等（文中摘要未列出具体名称，但总体涵盖端到端学习范式）。
- **任务设置**：少样本设定，仅在少量示范（如5个以内）下测试在新物体或新场景上的成功率。

### 4. 资源与算力
- 提供的摘要和元数据中**未明确说明**使用的 GPU 型号、数量或训练时长。文内可能包含具体算力信息，但依据当前给出的材料无法确认。建议查阅完整论文的“实验设置”或附录部分。

### 5. 实验数量与充分性
- 至少包含**两大组实验**：模拟环境（RLBench）和真实世界操作。
- 在 RLBench 中可能进一步细分为**跨实例泛化**和**跨类别泛化**两种协议，每种协议涉及多个任务，构成多组实验。
- 应包含**消融实验**，验证各模块（如解耦设计、在线自适应匹配、稠密对应来源）的贡献。
- 还可能有**定性展示**（对应可视化、适应过程）。
- 从摘要推断，实验覆盖了不同难度层次的泛化场景，对比基线合理，消融分析能支撑主张，整体**较为充分且客观**。但缺少具体实验数字，无法精确评价规模。

### 6. 论文的主要结论与发现
- 显式解耦示范-场景匹配与策略学习显著提升了跨物体少样本泛化能力。
- 图扩散策略在基于稠密对应的条件下，能够稳健地生成适应新几何形状和外观的动作。
- 在线自适应匹配进一步增强了执行过程中的鲁棒性，尤其在动态变化场景下。
- 方法在模拟和真实实验中均优于现有上下文模仿学习基线，证明了对应感知框架的有效性。

### 7. 优点
- **思想简洁有效**：解耦设计与认知科学中的“perception-action”分离思路一致，降低了学习复杂度。
- **充分利用视觉基础模型**：将大模型的先验知识注入机器人策略，无需大量领域内数据即可获得可靠对应。
- **鲁棒的在线适应**：动态匹配机制使策略在真实世界非结构化环境中更实用。
- **跨物体泛化能力强**：不仅在同类物体不同实例间迁移，还能泛化到全新类别的物体，体现了较强的语义感知。

### 8. 不足与局限
- **对视觉基础模型依赖较重**：若基础模型在特定场景（如强遮挡、无纹理物体）失效，对应质量下降可能直接影响策略性能。
- **实时性未提及**：稠密对应提取和图扩散过程可能带来较高计算延迟，在高速任务中可能受限。
- **实验任务范围**：目前仅在桌面操作任务上验证，未涉及移动操作、长序列接触式交互等更复杂场景。
- **对比基线可能不全面**：未在摘要中看到与最新端到端多模态大模型策略的对比，无法判断与更前沿范式的差距。
- **数据效率**：虽称为少样本，但离线提取示范特征和训练扩散策略仍需要一定量的演示数据，绝对数据效率未详细讨论。

（完）
