---
title: "ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning"
title_zh: ReinboT：用强化学习增强机器人视觉-语言操作
authors: "Hongyin Zhang, Zifeng Zhuang, Han Zhao, Pengxiang Ding, Hongchao Lu, Donglin Wang"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=Mzz4BhdIFb"
tags: ["query:model"]
score: 8.0
evidence: 将离线强化学习集成到VLA中，从混合质量数据中生成鲁棒动作
tldr: VLA模型受限于训练数据质量不均。本文提出ReinboT，将离线RL最大化累积奖励的原则融入端到端VLA，通过预测密集回报感知数据质量分布。实验显示该方法能从混合质量数据中学习更鲁棒的策略，提升了多任务操作的成功率与泛化性。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 训练数据质量不均限制了VLA模型的性能。
method: 将离线RL集成到VLA中，利用密集回报预测捕获操作任务数据质量分布。
result: 在混合质量数据下生成更鲁棒的决策动作，提升操作成功率。
conclusion: ReinboT为VLA模型提供了一种从多样数据中学习稳健操作的强化学习解决方案。
---

## Abstract
Vision-Language-Action (VLA) models have shown great potential in general robotic decision-making tasks via imitation learning. However, the variable quality of training data often constrains the performance of these models. On the other hand, offline Reinforcement Learning (RL) excels at learning robust policy models from mixed-quality data. In this paper, we introduce Reinforced robot GPT (ReinboT), a novel end-to-end VLA model that integrates the RL principle of maximizing cumulative reward. ReinboT achieves a deeper understanding of the data quality distribution by predicting dense returns that capture the nuances of manipulation tasks. The dense return prediction capability enables the robot to generate more robust decision-making actions, oriented towards maximizing future benefits. Extensive experiments show that ReinboT achieves state-of-the-art performance on the CALVIN mixed-quality dataset and exhibits superior few-shot learning and out-of-distribution generalization capabilities in real-world tasks.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：视觉-语言-动作（VLA）模型在机器人操作任务中主要依赖模仿学习，但训练数据质量参差不齐（例如人类遥操作数据混杂次优轨迹），极大限制了模型的性能与鲁棒性。
- **研究动机**：离线强化学习（offline RL）天然适合从混合质量数据中学习最大化累积奖励的策略，而现有端到端 VLA 模型尚未系统性地融入这一机制。本文旨在将离线 RL 的奖励最大化原则集成进 VLA 框架，使模型能感知数据质量分布并输出面向长期收益的鲁棒动作。
- **整体含义**：提出 **ReinboT（Reinforced robot GPT）**，通过预测密集回报（dense return）来理解操作任务的细粒度质量，使机器人能在质量不均的数据上习得更稳固的决策习惯。

### 2. 论文提出的方法论
- **核心思想**：在 VLA 模型中嵌入离线 RL 的目标——最大化累积奖励，而不显式进行动作值函数估计或策略梯度；通过引入密集回报预测任务，让模型理解每条轨迹、每个状态-动作对的未来期望回报，从而在动作生成时内隐地偏向高回报区域。
- **关键技术细节**（根据摘要推断）：
  - **架构设计**：将 Transformer 基的 VLA 模型（类似 GPT 风格）扩展为同时输出动作与预测的密集回报（return-to-go）。输入为视觉 token、语言指令和过往状态-动作序列；输出为下一步动作及对应的累计回报预测。
  - **训练目标**：除传统的动作预测损失外，增加一个回报预测的回归损失（如均方误差），该回报标签可来自预定义的奖励函数或事后重标记（hindsight relabeling）。为了让模型从不同质量数据中区分高低回报行为，回报预测头起到了隐式“数据质量分类器”的作用。
  - **推理阶段**：模型根据当前视觉-语言输入和历史，先预测执行某个动作可能带来的未来回报，再基于该预测选择/输出动作；或直接在动作 token 序列中利用回报信号进行条件生成。具体公式未在摘要中给出，但可概括为：
    - 给定状态 \(s_t\)、指令 \(l\)、历史 \(h_{t-1}\)，模型输出动作分布 \(p(a_t | s_t, l, h_{t-1})\) 和回报预测 \(\hat{R}_t\)。
    - 训练损失：\(\mathcal{L} = \mathcal{L}_{action} + \lambda \mathcal{L}_{return}\)，其中 \(\mathcal{L}_{return} = MSE(\hat{R}_t, R_t)\)。
- **区别于现有工作**：直接将离线 RL 的核心信号（return）整合进端到端的 VLA 训练，而非两阶段（先训 RL 再迁移）或显式 RL 策略优化。

### 3. 实验设计
- **主要数据集与场景**：
  - **CALVIN** 长序列操作数据集，包含多种任务和混合质量（人类演示与次优数据）的轨迹。
  - **真实世界任务**：评估少样本学习和分布外泛化能力，具体任务未详细说明，但涉及不同物体、场景变化。
- **Benchmark 与对比方法**：
  - 基线与对比方法包括其他 VLA 模型（如 RT-1、RT-2 等，需推断），以及可能的标准模仿学习、决策变换器（Decision Transformer）等离线 RL 方法。摘要称在 CALVIN 混合质量数据上达到 SOTA。
- **评估指标**：多任务操作成功率、少样本学习成功率和分布外泛化成功率。

### 4. 资源与算力
- **算力信息**：从提供的摘要和元数据中 **未明确说明** 所使用的 GPU 型号、数量、训练时长或总计算量。论文可能只在正文中才提及（如 A100、训练小时等），但此处无详细数据，故需指出这一点。

### 5. 实验数量与充分性
- **实验数量**：推断至少包括以下组别：
  - CALVIN 上的主实验（与多种基线对比）；
  - 真实世界少样本学习实验；
  - 真实世界分布外泛化实验；
  - 可能包含消融实验（如移除回报预测头、对比不同回报标签构造方式等），以验证各模块贡献。
- **充分性与公平性**：
  - 实验覆盖了标准仿真基准和真实场景，且强调混合质量数据，贴近实际应用，具有一定的充分性。
  - 但摘要未提供统计显著性、可重复性细节或错误条，无法判断统计稳健性。对比基线若只与模仿学习方法相比，可能缺少与主流离线 RL 方法（如 IQL、CQL）作为动作预测模块的对比，有局限。

### 6. 论文的主要结论与发现
- ReinboT 通过密集回报预测，能有效捕获操作任务的数据质量分布。
- 在混合质量数据上，该方法相比传统模仿学习型 VLA 生成了更稳健的动作，提高了多任务操作成功率。
- 模型展现出优越的少样本学习能力与分布外泛化性能，证明 RL 信号有助于策略应对陌生场景。
- 端到端集成 RL 原理的 VLA 框架是可行且高效的，为缓解演示数据质量敏感问题提供了新思路。

### 7. 优点
- **新颖的融合方式**：首次将离线 RL 的核心要素（累积回报预测）直接植入端到端 VLA 训练，避免了复杂的 RL 优化流程。
- **数据质量自适应**：通过预测密集回报，模型能隐式地偏重高质量片段，对数据质量分布更鲁棒。
- **实操友好**：推理时不需在线 RL 交互或价值函数迭代，仅靠模型前向过程即可输出动作，适合真实机器人部署。
- **实验场景覆盖**：既有标准化仿真基准 CALVIN，也有真实世界的少样本和泛化实验，验证了方法的实用性。

### 8. 不足与局限
- **方法论细节缺失**：基于摘要无法评判模型的具体架构、回报标签构造方式、训练稳定性等关键细节，可能影响复现。
- **对比实验可能不足**：摘要未提及与强离线 RL 方法（如 Diffusion Policy + Q-learning）的直接比较，不清楚改进来源是 VLA 结构还是 RL 信号。
- **奖励函数依赖**：方法需要定义合理的奖励函数来生成回报标签，然而在真实机器人操作中密集奖励的获取本身就是挑战，可能需人工设计或自动 relabeling，这一点未在摘要中讨论。
- **扩展性未知**：在大规模真实机器人数据（如 Open X-Embodiment）上的效果未提及，能否跨异构平台保持鲁棒性有待验证。
- **算力与效率未说明**：无法评估训练成本、推理时延是否适合实时操作。

（完）
