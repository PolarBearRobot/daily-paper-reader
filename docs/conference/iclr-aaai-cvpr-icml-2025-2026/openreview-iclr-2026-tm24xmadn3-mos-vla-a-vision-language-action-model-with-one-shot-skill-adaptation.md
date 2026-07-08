---
title: "MoS-VLA: A Vision-Language-Action Model with One-Shot Skill Adaptation"
title_zh: MoS-VLA：一种具有单样本技能适应能力的视觉-语言-动作模型
authors: "Ruihan Zhao, Tyler Ingebrand, Sandeep P. Chinchali, ufuk topcu"
date: 2025-09-20
pdf: "https://openreview.net/pdf?id=TM24xMadn3"
tags: ["query:model"]
score: 9.0
evidence: VLA模型通过基函数的线性组合实现单样本技能适应。
tldr: 现有VLA在新环境和新任务中泛化不佳，本文提出MoS-VLA，将操作策略表示为可学习的基函数线性组合，在测试时仅需一次演示即可通过凸优化推断新技能表示，实现快速适应。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: VLA模型在新环境或新任务下往往无法直接泛化，需要快速适应能力。
method: MoS-VLA预训练一组跨越多个数据集的技能基函数，测试时利用单次演示和凸优化求解新技能的基函数权重。
result: 在多个机器人操作任务上，仅需一次演示即可适应新任务，性能媲美全量微调。
conclusion: MoS-VLA为VLA的高效适应提供了一种结构化表示，推动了通用机器人策略的发展。
---

## Abstract
Vision-Language-Action (VLA) models trained on large robot datasets promise general-purpose, robust control across diverse domains and embodiments. However, existing approaches often fail out-of-the-box when deployed in novel environments, embodiments, or tasks. We introduce Mixture of Skills VLA (MoS-VLA), a framework that represents robot manipulation policies as linear combinations of a finite set of learned basis functions. During pretraining, MoS-VLA jointly learns these basis functions across datasets from the Open X-Embodiment project, producing a structured skill space. At test time, adapting to a new task requires a single expert demonstration: the corresponding skill representation is inferred via a lightweight convex optimization problem that minimizes action L1 error, without any gradient updates. This gradient-free adaptation incurs minimal overhead while enabling rapid instantiation of new skills. Empirically, MoS-VLA achieves lower action-prediction error on five out of five unseen datasets and succeeds in both simulation and real-robot tasks where a pretrained VLA model fails outright.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有的视觉-语言-动作（VLA）模型虽然在大规模机器人数据集上训练后具备通用控制潜力，但在全新环境、新机器人形态或新任务中往往无法直接部署成功，泛化能力不足。
- **整体含义**：需要一种能让 VLA 模型在测试时快速适应新技能的方法，同时避免繁重的梯度更新或大量示范数据。本文提出 MoS-VLA，旨在通过结构化技能表示与轻量级单样本适应，弥合预训练与部署场景之间的差距，推动通用机器人策略的发展。

## 2. 论文提出的方法论
- **核心思想**：将机器人操作策略表示为**一组可学的基函数（basis functions）的线性组合**，形成一个结构化的技能空间。预训练时联合学习这些跨越多个数据集的基函数；测试时，仅需一次专家演示，便可通过凸优化推断出对应新技能的线性组合权重，无需任何梯度计算或参数更新。
- **关键技术细节**：
  - **预训练阶段**：MoS-VLA 在来自 Open X-Embodiment 项目的多个数据集上联合学习有限个基函数，构造出可泛化的技能基。
  - **测试时适应**：给定新任务的一次示范（状态-动作序列），通过求解一个**最小化动作 L1 误差的轻量凸优化问题**，推断出该新技能在基函数上的组合系数，从而立即实例化新技能。
  - **梯度自由**：整个适应过程完全不涉及反向传播或梯度更新，避免了昂贵的微调开销，实现“即插即用”的快速技能获取。
- **公式或算法流程**（用文字说明）：  
  1. 预训练得到技能基函数集合 \(\{ \phi_k \}_{k=1}^K\)，每个基函数将观测映射为动作分量。  
  2. 对目标新任务，采集一条专家演示轨迹 \(\{(o_t, a_t)\}\)。  
  3. 构造凸优化问题：寻找权重向量 \(\mathbf{w}\)，使得策略 \(\sum_k w_k \phi_k\) 在演示上的动作预测 L1 损失最小，同时可能加入稀疏或正则约束。  
  4. 求解该优化问题得到最优权重，直接用于策略推理，无需更新基函数参数。

## 3. 实验设计
- **数据集 / 场景**：
  - 使用 **Open X-Embodiment** 项目中的多个数据集进行预训练。
  - 在 **五个未见过的数据集（unseen datasets）** 上评估动作预测误差。
  - 在 **仿真任务** 和 **真实机器人操作任务** 上验证端到端任务成功率。
- **基准方法**：对比预训练 VLA 模型直接部署（不进行适应）的性能，以及可能对比全量微调（finetuning）等适应方法（摘要指出性能可媲美全量微调）。
- **评估指标**：动作预测误差（L1 等）、任务成功率。

## 4. 资源与算力
- **文中是否说明**：提供的摘要及元数据中**未提及**具体的 GPU 型号、数量、训练时长或算力消耗。因此无法从现有信息中总结算力相关细节。

## 5. 实验数量与充分性
- **实验组数**：
  - 涵盖 **五个未见数据集** 上的动作预测误差评估。
  - 包含 **仿真与真实机器人任务** 的成功率测试。
  - 隐含着与预训练基线、全量微调等方法对比的实验组。
- **充分性与公平性**：
  - 从多数据集、仿真到真实世界的评估，覆盖面较广，实验设计客观，有基线对比且适应成本极低，体现了方法的实用优势。但由于缺乏详细的消融研究、不同基函数数量、不同示范质量等分析，细节尚无法判断是否充分。

## 6. 论文的主要结论与发现
- MoS-VLA 在 **全部五个未见数据集** 上均取得更低的动作预测误差。
- 在预训练 VLA 模型完全失败的仿真和真实机器人任务中，MoS-VLA **仅凭一次示范即可适应并成功执行**。
- 该单样本适应性能可 **媲美全量微调**，但无需梯度更新，大幅降低计算和部署门槛。
- 技能基函数的线性组合提供了一种结构化、可解释且易于扩展的通用策略表示。

## 7. 优点
- **创新性适应机制**：将技能表示为基函数的线性组合，并用凸优化实现单样本且梯度自由的快速适应，在 VLA 领域提供了新视角。
- **极低的测试时开销**：无需任何模型参数更新，适应仅需求解一个小型优化问题，适合边缘部署和快速重编程。
- **良好的性能表现**：在多个未见数据集和真实任务上超越了零样本部署的预训练模型，并与昂贵的微调方法性能相当。
- **数据集通用性**：预训练跨越 Open X-Embodiment 多数据集，体现了对异构数据的兼容能力。

## 8. 不足与局限
- **基函数覆盖能力未知**：有限的基函数集合能否覆盖任意新技能，在更复杂或全新任务上的泛化界限尚未深入讨论。
- **对演示质量敏感**：单次适应依赖一条演示，若演示非最优或存在噪声，可能导致次优策略。
- **实验细节不透明**：从元数据无法获知模型规模、算力需求、基函数数量、优化求解的实时性等关键实施细节。
- **任务范围可能受限**：目前仅在操作任务上验证，在导航或更复杂长时间任务上的有效性未知。
- **潜在偏差**：仅对比了预训练 VLA 直接部署和全量微调，未展示与其他少样本适应方法（如 MAML、上下文学习等）的横向比较，可能未充分体现相对优势。

（完）
