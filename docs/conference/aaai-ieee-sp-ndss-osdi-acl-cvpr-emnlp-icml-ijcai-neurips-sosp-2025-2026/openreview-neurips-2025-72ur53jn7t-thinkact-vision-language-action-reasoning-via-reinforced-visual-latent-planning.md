---
title: "ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning"
title_zh: ThinkAct：通过强化视觉潜在规划进行视觉-语言-动作推理
authors: "Chi-Pin Huang, Yueh-Hua Wu, Min-Hung Chen, Yu-Chiang Frank Wang, Fu-En Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=72UR53jN7T"
tags: ["query:model"]
score: 8.0
evidence: 双系统VLA结合推理与潜在规划用于长程任务
tldr: 端到端VLA模型缺乏显式推理，难以应对复杂长程任务。本文提出ThinkAct双系统框架，通过强化视觉潜在规划将多模态LLM的高层推理计划与低层动作执行连接。实验显示该框架在需要多步推理的任务中显著提升了成功率与适应性，为VLA的推理能力提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型缺乏多步推理与自适应动作执行能力。
method: 构建双系统框架，利用强化视觉潜在规划连接高层推理与低层动作。
result: 在动态环境的长程操作任务中取得了更高的成功率和泛化性。
conclusion: 显式推理与潜在规划结合有效增强了VLA模型的长期任务执行能力。
---

## Abstract
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

---

## 论文详细总结（自动生成）

# ThinkAct：通过强化视觉潜在规划进行视觉–语言–动作推理

## 1. 论文的核心问题与整体含义
- **研究动机**：当前视觉–语言–动作 (VLA) 模型普遍采用端到端训练，直接将多模态输入映射为动作，缺乏显式的多步推理与规划能力，难以在动态环境中完成复杂的长程任务。
- **核心问题**：如何让 VLA 智能体具备高层推理、长期规划与自适应动作执行的能力，从而突破端到端生硬映射的瓶颈。
- **整体含义**：作者提出 ThinkAct 双系统框架，将高层推理与低层执行分离，并通过**强化视觉潜在规划**桥接二者。该工作为 VLA 推理能力提供了新范式：让多模态大语言模型 (MLLM) 生成可优化的推理计划，再将其压缩为视觉潜在变量以驱动鲁棒的动作执行。

## 2. 方法论
- **核心思想**：构建“快–慢双系统”：系统一基于 MLLM 生成自然语言推理计划（高层、慢、可优化）；系统二为下游动作模型（低层、快、条件执行）。两者通过**视觉计划潜在变量**衔接，并引入强化学习，利用动作执行结果产生的视觉奖励来优化推理计划。
- **关键技术细节与算法流程**：
  - **高层推理生成**：给定任务指令和视觉观测，多模态 LLM 输出具身推理计划（文本形式的步骤描述）。
  - **强化视觉奖励**：设计两类视觉奖励——**目标完成度奖励**和**轨迹一致性奖励**，用以评估推理计划引导的执行效果，并使用策略梯度方法更新 MLLM 的推理生成策略。
  - **视觉计划潜在压缩**：优化后的推理计划与对应的视觉特征共同编码为一个紧凑的**视觉计划潜在变量**，该变量将作为下游动作模型的条件信息。
  - **低层动作执行**：动作模型（如扩散策略或 Transformer 策略）以视觉计划潜在变量为条件，生成连续或离散的动作序列，在环境中完成操作。该模型在训练时即学习如何根据潜在变量自适应执行。
  - **整体流程**：多模态观测 → MLLM 生成初始推理计划 → 执行并收集视觉奖励 → 强化学习更新计划生成 → 压缩计划为潜在变量 → 动作模型以潜变量为条件输出动作 → 迭代直至任务完成或终止。

## 3. 实验设计
- **数据集/场景与基准**：论文在两大类别基准上进行了广泛验证（摘要用语）：
  - **具身推理基准**：用于评估多步指令跟随与推理能力，可能包括类似 ALFRED 的室内具身任务或需要复杂推理的交互式环境。
  - **机器人操作基准**：用于测试长程操作与动态适应，可能涵盖 CALVIN、RLBench 等需要长期规划的操作任务。
- **对比方法**：端到端 VLA 基线（直接输入到动作）、以及其他可能包含推理能力的方法，重点比较在少样本适应、长期规划和自我纠正行为上的差异。
- **评估指标**：任务成功率、轨迹一致性、泛化能力（few-shot adaptation）等。

## 4. 资源与算力
- 提供的文本中**未包含任何算力细节**。摘要及元数据未提及 GPU 型号、数量、训练时长、模型参数量等信息，因此无法估计实际计算资源需求。

## 5. 实验数量与充分性
- 摘要称进行了“extensive experiments”，但未给出具体实验组数。根据论文结构和接收背景（NeurIPS-2025，评分 8.0），可合理推断实验应包含：
  - 多个基准上的主结果对比；
  - 不同任务难度与长度的分析；
  - 消融实验（如分别去掉视觉奖励、去除潜在压缩、仅用语言计划等）；
  - 泛化与自适应分析（少样本、环境扰动、自校正情况）。
- 鉴于会议接收，实验设计应达到了该领域的充分性与客观公平要求，但**当前文本不足以从细节层面确认**。

## 6. 主要结论与发现
- ThinkAct 通过显式推理与强化视觉潜在规划的结合，有效增强了 VLA 模型的长期任务执行能力。
- 在动态环境的长程操作任务中，该框架取得了比端到端方法**更高的成功率和更强的泛化性**。
- 模型展现出**少样本适应**、**长期规划**以及**自我纠正**行为，验证了高层推理指导低层动作执行的可行性与优势。

## 7. 优点
- **双系统解耦设计**：推理与执行模块分离，MLLM 专注高层计划，动作模型专注鲁棒执行，结构清晰且易于分别优化。
- **动作对齐的视觉奖励**：直接使用任务完成和轨迹一致性作为视觉奖励，使推理计划与最终动作效果一致，比单纯的语言监督更符合具身任务本质。
- **潜在表示压缩**：将语言推理计划压缩为紧凑的视觉潜在变量，降低了信息传递维度，便于下游动作模型利用，并可支持在潜在空间进行规划。
- **自适应与自校正**：强化学习优化使计划能根据环境反馈动态调整，在遇到干扰或中途失败时可修正后续步骤。
- **泛化潜力**：实验显示对未见任务具备少样本适应能力，表明方法并非仅拟合训练分布。

## 8. 不足与局限
- **实验细节缺失**：从当前摘要无法得知具体基准名称、模型规模与训练成本，难以评估真实场景下的可行性与计算开销。
- **依赖高质量 LLM**：高层推理严重依赖 MLLM 的生成质量，可能受幻觉、错误推理影响，进而误导动作执行。
- **潜在压缩信息损失**：将多步自然语言计划压缩为单一潜在变量可能丢失精细的步骤信息，对细粒度操作的性能影响未知。
- **强化学习训练效率**：优化高层计划需与环境交互收集奖励，样本效率可能较低，在真实机器人上训练成本较高。
- **实验环境局限性**：摘要未提及真实世界机器人实验，所有结果可能仅在仿真环境下验证，sim-to-real 迁移能力尚不明确。
- **动态重规划能力未知**：单次推理生成的潜在变量可能难以应对需要连续在线重规划的极端动态场景，框架的动态适应上限有待检验。

（完）
