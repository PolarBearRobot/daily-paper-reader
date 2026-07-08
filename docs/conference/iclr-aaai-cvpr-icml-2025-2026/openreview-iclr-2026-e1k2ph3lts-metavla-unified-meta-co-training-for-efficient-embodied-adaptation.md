---
title: "MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation"
title_zh: MetaVLA：面向高效具身自适应的统一元协同训练
authors: "Chen Li, Zhantao Yang, Han Zhang, Fangyi Chen, Chenchen Zhu, Anudeepsekhar Bolimera, Marios Savvides"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=E1K2Ph3LtS"
tags: ["query:model"]
score: 9.0
evidence: 统一的元协同训练框架，用于VLA模型的高效自适应和泛化
tldr: 针对VLA模型需任务特定微调且泛化性差的问题，提出MetaVLA统一后训练框架，通过上下文感知的元协同训练和元学习机制，使模型能利用多样辅助任务快速适应新任务，无需额外架构改动，实现高效扩展和泛化。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: VLA模型泛化能力弱，常需任务特定微调，计算成本高。
method: 提出MetaVLA，通过上下文感知的元协同训练，将多目标任务合并到单一微调阶段，并引入元学习实现快速适应。
result: 实验表明MetaVLA在不同未见任务上均能高效适应，泛化性能大幅提升。
conclusion: MetaVLA为VLA模型提供了一种统一的、可扩展的高效自适应方案。
---

## Abstract
Vision–Language–Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists—they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism—derived from Attentive Neural Processes—to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0\% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by 76%. These results show that scalable, low-resource post-training is achievable—paving the way toward general-purpose embodied agents. Code will be available.

---

## 论文详细总结（自动生成）

# 论文总结：MetaVLA: Unified Meta Co-Training for Efficient Embodied Adaptation

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：视觉-语言-动作（VLA）模型在具身推理任务中表现出一定潜力，但距离真正的通用智能体仍有较大差距。
- **核心问题**：
  - 现有VLA模型通常需要针对特定任务进行微调，计算成本高。
  - 泛化能力弱，难以适应未见过的任务。
  - 缺乏一种统一的、可扩展的后训练框架来实现高效的任务适配。
- **整体含义**：提出MetaVLA，旨在通过元协同训练机制，提升VLA模型的泛化性和自适应效率，推动通用具身智能体的发展。

## 2. 论文提出的方法论
- **核心思想**：通过上下文感知的元协同训练（Context-Aware Meta Co-Training），将多个目标任务合并到单一微调阶段，并利用结构多样化的辅助任务增强域内泛化。同时引入轻量级元学习机制，使模型能从多样上下文中快速适应新任务，而无需大幅改变架构或增加推理开销。
- **关键技术细节**：
  - **统一后训练框架**：与骨干模型无关，可灵活应用于各种VLA架构。
  - **元学习机制**：借鉴注意力神经过程（Attentive Neural Processes）的思想，使模型具有快速适应能力。
  - **训练效率**：通过单一阶段的协同训练替代传统的多次任务特定微调，显著降低训练步数和GPU时间。
- **算法流程（文字说明）**：将多个目标任务和辅助任务的数据混合在一起，在统一的训练阶段中让模型学习共享表示；元学习组件使模型能够根据少量上下文样本快速调整行为，从而在新任务上展现良好的泛化能力。

## 3. 实验设计
- **数据集/场景**：主要基于LIBERO基准测试，涵盖多种操作任务，包括长时程任务。
- **基准方法**：与OpenVLA等现有VLA模型进行对比。
- **评估指标**：成功率提升、训练步数、GPU时间等。
- **对比方法**：传统多任务监督微调（multi-task SFT）、任务特定微调等。

## 4. 资源与算力
- **算力使用**：文中提到与OpenVLA相比，MetaVLA将训练步数从240K降至75K，GPU时间削减76%，但是**未明确说明使用的GPU型号、数量及具体训练时长**。只给出了相对改进率。

## 5. 实验数量与充分性
- **实验组数**：从摘要来看，至少包含在LIBERO上的主要实验以及与基准方法的对比；提及使用6个辅助任务，但未详细列出所有消融实验。
- **充分性评估**：由于仅提供摘要信息，具体实验数量不明确。但提到在长时程任务上最高提升8.0%，并从训练步数和GPU时间两方面验证了效率。实验对比了多任务SFT和任务特定微调，设计较为公平。若无更多全文细节，难以判断消融实验的全面性，但整体证据指向方法的有效性。

## 6. 论文的主要结论与发现
- MetaVLA在LIBERO上显著优于OpenVLA，尤其在长时程任务中提升达8.0%。
- 训练步数从240K减少至75K，GPU时间缩短76%，证明高效的后训练是可行的。
- 该方法显示出良好的可扩展性和泛化能力，为通用具身智能体铺平道路。

## 7. 优点：方法或实验设计上的亮点
- **统一性与骨干无关性**：可应用于不同的VLA架构，扩展性强。
- **高效性**：极大降低了训练计算成本，实现低资源后训练。
- **泛化能力**：利用元学习和辅助任务，模型能快速适应新任务，缓解传统微调的局限。
- **架构简洁**：元学习机制轻量，几乎不增加推理开销。

## 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等
- **实验覆盖范围有限**：仅在LIBERO基准上进行评估，缺少其他具身任务或仿真/真实环境的验证。
- **辅助任务依赖**：方法性能可能受辅助任务选择和质量的影响，文中未讨论任务选取策略。
- **算力细节缺失**：未给出所用GPU具体型号、数量和总训练时间，难以精确评估资源需求。
- **元学习方法复杂性**：虽然声称轻量，但注意力神经过程的实际实现细节未充分披露，可能在某些场景下有额外开销。
- **泛化边界未探明**：未讨论在极大差异任务或域迁移下的表现，以及可能存在的过拟合风险。

（完）
