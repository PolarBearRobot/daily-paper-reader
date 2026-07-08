---
title: "XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations"
title_zh: XR-1：通过学习统一视觉-运动表征迈向通用视觉-语言-动作模型
authors: "Shichao Fan, Kun Wu, Zhengping Che, Xinhua Wang, Di Wu, Fei Liao, Ning Liu, Yixue Zhang, Zhen Zhao, Zhiyuan Xu, Meng Li, Qingjie Liu, Shanghang Zhang, Min Wan, Jian Tang"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=XJclc9Eabd"
tags: ["query:model"]
score: 10.0
evidence: 学习统一视觉-运动表征的VLA模型，处理异构数据与人类演示
tldr: 现有VLA模型难以从高维观测生成精确动作，且无法有效利用异构数据中的多模态知识。为此，XR-1提出学习统一的视觉-运动表征，同时处理机器人动作和视频动态，以弥合不同本体和人类演示间的领域差异。实验表明，该方法能显著提升低层动作精度和跨数据源的策略学习，增强了VLA模型的通用性和实用性。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有VLA模型面临精确动作生成和异构数据域差异两大挑战。
method: 提出统一视觉-运动表征学习框架，融合多模态知识以引导策略学习。
result: 在真实机器人实验上，改善了低层动作精度和跨任务泛化能力。
conclusion: 统一VLA表征能有效利用异构演示数据，提升机器人操作通用性。
---

## Abstract
Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models.  However, existing VLA models still face two fundamental challenges: (\textit{i}) producing precise low-level actions from high-dimensional observations, (\textit{ii}) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present \textbf{XR-1}, a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments.
At its core, XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion.  UVMC addresses these challenges by (\textit{i}) serving as an intermediate representation between the observations and actions, and  (\textit{ii}) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a \emph{three-stage training paradigm}: (\textit{i}) self-supervised UVMC learning, (\textit{ii}) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (\textit{iii}) task-specific post-training.  We validate XR-1 through extensive real-world experiments with more than 12,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $\pi_0$ and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at \href{https://xr-1-vla.github.io/}{https://xr-1-vla.github.io/}.

---

## 论文详细总结（自动生成）

# XR-1：通过学习统一视觉-运动表征迈向通用视觉-语言-动作模型

## 1. 论文的核心问题与整体含义
现有视觉-语言-动作（VLA）模型在利用大规模异构机器人数据集时面临两个根本挑战：
- **动作精度不足**：如何从高维视觉观测中生成精确的低层动作（如末端执行器位置、关节角等）。
- **域差异难以弥合**：不同机器人本体（如单臂、双臂、移动操作等）以及人类演示与机器人数据之间存在显著的动态域鸿沟。现有方法常孤立地从视觉动态或动作序列中提取隐变量来引导策略，未能充分整合异构数据源中互补的多模态知识。

因此，本文提出**XR-1**，一种可扩展的通用VLA框架，其核心是学习一个统一的离散表征——“统一视觉-运动码”（UVMC），以同时编码视觉动态与机器人运动，从而作为观测与动作之间的中间表征，对齐来自不同机器人本体和人类演示的动态信息，提升策略的多任务、多本体泛化能力。

## 2. 论文提出的方法论
XR-1的核心思路是通过一个**双分支VQ-VAE**学习离散的**统一视觉-运动码（UVMC）**，并采用**三阶段训练范式**：

### 2.1 统一视觉-运动码（UVMC）学习
- **双分支结构**：分别对视觉序列（视频帧）和机器人运动序列（动作轨线）进行编码，共享同一个码本（codebook），强制将两种模态映射到相同的离散隐空间。
- **训练目标**：通过自监督重建损失和码本更新损失，使UVMC既能保留视觉场景的动态变化，又能捕捉精细的动作控制信息。
- **作用**：
  - 作为观测与动作之间的**中间表征**，降低策略从高维观测到连续动作的映射难度。
  - **对齐多模态动态信息**：将不同本体和人类演示的视觉-运动映射统一表示，从而提取互补知识。

### 2.2 三阶段训练范式
1. **阶段一：自监督UVMC学习**
   - 仅使用原始视觉序列和机器人运动序列，训练VQ-VAE，获得可同时重构视觉和运动的离散码本。
2. **阶段二：UVMC引导的预训练**
   - 在大规模跨本体机器人数据集上，以语言指令为条件，训练一个Transformer策略网络预测UVMC码字，再由解码器生成目标动作。
   - 预训练阶段利用UVMC作为桥梁，让模型接触多种异构数据，吸收广泛的操控知识。
3. **阶段三：任务特定的后训练**
   - 在目标机器人平台和具体任务上，对预训练模型进行微调，使其适应特定本体和新的交互场景。

## 3. 实验设计
- **数据集/场景**：未详细罗列所用公开数据集名称，但提及在大规模、跨本体（涵盖不同机器人形态）和人类演示的混合数据上进行预训练。真实世界实验覆盖6种不同的机器人本体和120多种操控任务。
- **评估基准**：主要通过与最新的VLA模型基线进行比较，包括**π₀**、**GR00T-N1.5**。评估维度包括任务成功率、对新物体、背景变化、干扰物和光照变化的泛化能力。
- **对比方法**：上述两个强基线模型，以及其他可能的隐式策略方法（文中摘要指出“现有方法常编码隐变量”，XR-1试图超越这些方法）。
- **真实世界 rollout 数量**：超过12,000次实际机器人执行，表明评估规模大。

## 4. 资源与算力
提供的摘要和元数据中**未明确说明**所使用的GPU型号、数量或训练时长。需要查阅完整论文以获取具体计算资源信息。

## 5. 实验数量与充分性
- **实验组数**：涉及6种机器人本体、120多种任务、12,000+个rollout，真实世界实验规模较大。
- **消融实验**：虽未在摘要中详述，但通常会包含对UVMC码本尺寸、双分支设计、预训练数据组合等的消融，以验证各组件贡献。
- **充分性与公平性**：
  - 对比了当前最先进的基线，并覆盖多种泛化设定（新物体、光照等），具备较好客观性。
  - 大量真实世界实验增加了结果的可靠性。
  - 潜在不足：文中未提及与仅用机器人数据、仅用人类数据、或传统多任务学习方法的消融对比细节，需原文进一步确认。

## 6. 论文的主要结论与发现
- **统一视觉-运动表征有效提升策略精度**：UVMC作为中间表征，显著改善了高维观测到精确动作的映射，提高了底层控制精度。
- **可跨异构数据迁移**：通过UVMC对齐不同本体和人类演示的动态，XR-1能够利用规模更大、形态更丰富的预训练数据，增强在真实机器人上的泛化性能。
- **三阶段训练是可行的规模化路径**：从自监督表征学习到大规模预训练再到任务微调，使VLA模型更具通用性和实用性。
- **性能超越现有基线**：在实验中一贯优于π₀和GR00T-N1.5，展示了更强的鲁棒性和泛化能力。

## 7. 优点
- **新颖的表征学习方法**：首次在VLA领域明确采用双分支VQ-VAE学习统一视觉-运动码，将异构动态信息对齐到同一离散空间。
- **良好的通用性与可扩展性**：框架可以包容多种机器人数据源和人类视频，为跨本体、跨任务学习提供了新思路。
- **大规模真实世界验证**：在6种形态、120+任务和1.2万次执行中验证，实验说服力强。
- **三阶段训练范式清晰**：结构化的训练流程易于复现和迁移到新平台。

## 8. 不足与局限
- **算力消耗不明确**：缺少GPU资源、训练时长等关键信息，难以评估实际部署成本。
- **码本离散化可能丢失精细信息**：离散表征虽然有助于对齐，但在需要超高精度力控或高速动态任务中可能引入量化误差，文中未深入分析此局限。
- **实验覆盖可能仍有限**：
  - 未提及移动操作、灵巧手等更复杂本体的表现。
  - 未与基于扩散策略或端到端模仿学习的最新方法（如Diffusion Policy）进行对比。
- **三阶段训练的复杂性**：多阶段训练流程增加了超参数调优和工程实现难度，迁移到新机器人时可能需要重训UVMC模块。
- **对数据覆盖的依赖**：UVMC的表征质量高度依赖大规模多源预训练数据，若新机器人形态与预训练分布差异极大，可能需补充数据。

（完）
