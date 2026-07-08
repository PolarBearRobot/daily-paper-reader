---
title: "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model"
title_zh: X-VLA：基于软提示 Transformer 的可扩展跨本体视觉-语言-动作模型
authors: "Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Tai Wang, Ya-Qin Zhang, Jingjing Liu, Xianyuan Zhan"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=kt51kZH4aG"
tags: ["query:model"]
score: 9.0
evidence: 通过软提示方法从异构机器人数据训练可扩展的跨本体 VLA
tldr: X-VLA 针对大规模异构跨本体机器人数据难以有效利用的问题，提出软提示方法，为每个数据源引入独立的可学习嵌入，以极少参数量实现具身自适应，基于流匹配架构的 VLA 模型能够高效融合多样数据，提升泛化性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 跨本体异构数据训练 VLA 困难。
method: 引入软提示，为不同数据源学习具身特定嵌入，结合流匹配架构。
result: 在多种机器人平台实现高效训练和泛化。
conclusion: 软提示是一种高效利用异构数据实现跨本体 VLA 的方法。
---

## Abstract
Successful generalist Vision-Language-Action (VLA) models that rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets. To facilitate and leverage the heterogeneity in rich, diverse robotic data sources, we propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. These embeddings serve as embodiment-specific prompts, which in unity empower VLA models with effective exploitation of varying cross-embodiment features. Our new X-VLA, a neat flow-matching-based VLA architecture, relies exclusively on soft-prompted standard Transformer encoders with an enhanced encoding pipeline, enjoying both scalability and simplicity. Evaluated across 6 simulation environments as well as 3 real-world robotics platforms, our 0.9B instantiation-X-VLA-0.9B simultaneously achieves state-of-the-art performance over a sweep of benchmark suites, demonstrating superior results on a wide axes of capabilities, from flexible dexterity to quick adaptation across embodiments, environments, and tasks.

---

## 论文详细总结（自动生成）

由于提供的论文 PDF 内容无法直接提取（仅显示验证页面），以下总结完全依据论文元数据中的 **摘要**、**动机、方法、结果和结论** 等字段进行推导，并对部分细节进行合理推断。若需更详尽的技术细节，需阅读原文。

---

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：当前通用视觉-语言-动作（VLA）模型需要在大规模、跨本体（cross-embodiment）、异构的机器人数据集上进行训练，但直接融合来自不同机器人平台、不同数据分布的数据极为困难。异构性（不同的传感器配置、运动空间、任务粒度等）会导致模型难以统一学习，泛化性受限。
- **整体含义**：提出一种轻量级的**软提示（Soft Prompt）**方法，以极少的额外参数解决跨本体数据异构的挑战，使得同一个 VLA 模型能够高效利用多种来源的机器人数据，实现可扩展的跨本体学习，从而提升从灵巧操作到快速环境适应的综合能力。

## 2. 方法论：核心思想与关键技术细节

- **核心思想**：
  - 将提示学习（prompt learning）的概念引入跨本体机器人学习，为**每一个不同的数据源**（如不同的机器人平台、不同的数据集）学习一组独立的、可训练的嵌入向量，称为“软提示”（soft prompt）。这些嵌入作为**具身特定（embodiment-specific）的提示**，向统一的 Transformer 模型注入数据源的身份信息与特征偏差，从而模型能自适应不同本体的差异。
  - 模型架构基于**流匹配（flow matching）**，整个 VLA 完全依靠标准 Transformer 编码器构建，保持简洁性和可扩展性。

- **关键技术细节**（基于文字描述）：
  - **软提示注入**：对于每个数据样本，将其所属数据源对应的可学习嵌入拼接到输入序列（如视觉 token 和语言 token）之前，或与序列中的特殊标记相加，使得 Transformer 在自注意力过程中能够感知到具身特异性。每个数据源仅增加极少量的参数（嵌入向量的参数量）。
  - **增强编码管线**：论文提到“enhanced encoding pipeline”，可能是在视觉-语言输入上做了特殊处理，例如多模态对齐、多尺度特征融合等，从而更好地支持软提示的作用。
  - **流匹配架构**：动作生成部分采用流匹配（Flow Matching）来建模连续动作分布，替代传统的扩散模型或离散化动作头。这提供了更稳定的训练和有概率保证的生成。
  - **训练方式**：将多个异构数据集混合训练，每个批次根据数据源选择对应的软提示嵌入，其余 Transformer 参数完全共享。这种设计使得模型能够从丰富的多源数据中学习通用的视觉-语言-动作映射，同时通过软提示保留并利用领域特性，实现**具身自适应**。

- **公式/算法流程（文字说明）**：
  - 前向过程：给定多模态输入（图像 \(I\)、语言指令 \(L\)）、数据源标识 \(k\)，取对应的软提示嵌入 \(p_k\)。将 \(p_k\) 与视觉 token、文本 token 拼接后送入标准 Transformer 编码器得到隐藏状态。对隐藏状态进行解码，利用流匹配方式从简单分布（如高斯）逐步转变为目标动作轨迹。
  - 损失函数：可能是流匹配中常用的连续归一化流损失或条件流匹配损失，驱动模型预测一条将噪声映射为真实动作的矢量场。

## 3. 实验设计：数据集/场景、基准与对比方法

- **评估环境与平台**：
  - **6 个模拟环境**：具体名称未在元数据中列出，推测可能包含常见的仿真基准如 Meta-World、LIBERO、CALVIN 等，涵盖不同机械臂、灵巧手和操作任务。
  - **3 个真实世界机器人平台**：涉及不同形态的真实机器人（如单臂、双臂、移动底盘等），验证从模拟到现实或跨本体的迁移。
- **基准**：论文使用了一系列基准套件（“a sweep of benchmark suites”），应包含多任务操作成功率、泛化性（新场景、新任务、新本体）等指标。
- **对比方法**：未在摘要中说明，但作为 VLA 模型，典型对比对象可能包括直接微调的 RT-2、Octo、OpenVLA 等通用策略，以及不使用软提示的基线（全量微调或简单拼接本体 ID）。还可能对比了基于扩散的 VLA 模型。

## 4. 资源与算力

- **算力说明**：提供的摘要和元数据**均未提及**具体的 GPU 型号、数量、训练时长或总 FLOPs。文中提到一个 **0.9B 参数**的实例 `X-VLA-0.9B`，表明该规模的模型是主要测评对象，算力消耗大致在数十张 A100 GPU·天的量级，但该信息为推测，原文未提供。

## 5. 实验数量与充分性评估

- **推测的实验量**：
  - 需在 6 个模拟环境 + 3 个真实平台的多个任务上进行全面对比，至少会报告每个环境下的成功率、泛化性评分。
  - 消融实验很可能包括：有无软提示、提示嵌入维度选择、不同数据源混合策略、流匹配与扩散/离散动作头的对比等。
- **充分性**：
  - 摘要声称同时达到最优（SoTA），并覆盖从灵活灵巧操作到跨本体快速适应的“广泛能力轴”，表明实验进行得相当系统。
  - 由于论文被 ICLR 2026 接收且评分 9.0，可以认为审稿人对实验的全面性、公平性（如统一超参、公平的基线实现）持认可态度。
  - 但无法从现有信息中确定具体消融组数和对比方法数量，存在信息缺失。

## 6. 主要结论与发现

- 软提示方法能够以极少的额外参数，有效地让 Transformer 架构处理大规模、跨本体异构数据。
- 基于纯软提示 Transformer 和流匹配的 X-VLA 架构兼具可扩展性和简洁性，无需复杂的设计即可在多平台、多任务上达到最优表现。
- 模型展现了优异的**具身自适应**能力：面对不同的本体、环境和任务时，能快速泛化，证明了软提示是高效利用异质机器人数据的可行路径。

## 7. 优点（方法或实验设计上的亮点）

- **极轻量的跨本体适应**：为每个数据源仅添加一组嵌入向量，避免了为不同平台设计独立模块或微调全部参数的巨大开销。
- **架构的简洁与可扩展性**：完全基于标准 Transformer 和流匹配，脱离对特殊网络结构的强依赖，易于随着数据和参数规模扩大。
- **实验覆盖面广**：同时评价了仿真和真实世界，涉及多种机器人平台和广泛能力维度，对方法的鲁棒性提供了有力佐证。
- **理论与工程结合**：将 NLP 中成熟的提示学习与机器人动作生成（流匹配）结合，是一种古老思想在新领域的巧妙应用。

## 8. 不足与局限（包括实验覆盖、偏差风险、应用限制等）

- **信息不完整**：因原文未提供细节，无法判断软提示是否仅对数据源标识敏感，是否会在新数据源上需要重新学习提示；流匹配的推理速度是否满足高频控制需求。
- **可能的数据源定义模糊**：如何定义“数据源”是一个关键问题，如果数据源过多，维护大量嵌入可能仍会引入复杂度，论文可能未讨论其上限。
- **真实世界实验规模未知**：虽然涵盖3个平台，但每个平台的测试场景数目、任务多样性可能有限，零样本跨本体迁移的性能到底如何仍有待验证。
- **与更强基线的对比缺失**：摘要未列出比较对象，如果未与参数规模接近的最新 VLA（如某些百亿参数模型）在同等数据上对比，SoTA 声明可能存疑。
- **算力细节缺失**：无法评估其效率优势是否真正显著，对于资源受限的研究者复现造成障碍。

（完）
