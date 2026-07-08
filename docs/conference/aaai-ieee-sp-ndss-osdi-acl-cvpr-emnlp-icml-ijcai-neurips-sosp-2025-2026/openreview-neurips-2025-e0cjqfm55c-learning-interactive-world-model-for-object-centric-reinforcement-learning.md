---
title: Learning Interactive World Model for Object-Centric Reinforcement Learning
title_zh: 学习交互式世界模型以实现对象中心强化学习
authors: "Fan Feng, Phillip Lippe, Sara Magliacane"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=E0cjqfM55C"
tags: ["query:model"]
score: 6.0
evidence: 学习结构化对象与交互表示的世界模型，提升策略学习。
tldr: 针对对象中心强化学习中交互建模不足的问题，FIOC-WM提出分解式交互对象中心世界模型，从像素中学习对象中心潜在变量和交互结构，显式建模动态，在多种环境中显著提升了策略学习的样本效率和泛化能力，为构建具有更好因果理解的体具体世界模型提供了参考。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有对象中心RL方法仅按个体对象分解状态，忽略交互。
method: 提出FIOC-WM，从像素中学习对象中心潜在变量和交互结构。
result: 在多种环境中，策略的样本效率和泛化能力显著提高。
conclusion: 显式建模对象交互能提升世界模型的表示质量和策略性能。
---

## Abstract
Agents that understand objects and their interactions can learn policies that are more robust and transferable. However, most object-centric RL methods factor state by individual objects while leaving interactions implicit. We introduce the Factored Interactive Object-Centric World Model (FIOC-WM), a unified framework that learns structured representations of both objects and their interactions within a world model. FIOC-WM captures environment dynamics with disentangled and modular representations of object interactions, improving sample efficiency and generalization for policy learning. Concretely, FIOC-WM first learns object-centric latents and an interaction structure directly from pixels, leveraging pre-trained vision encoders. The learned world model then decomposes tasks into composable interaction primitives, and a hierarchical policy is trained on top: a high level selects the type and order of interactions, while a low level executes them. On simulated robotic and embodied-AI benchmarks, FIOC-WM improves policy-learning sample efficiency and generalization over world-model baselines, indicating that explicit, modular interaction learning is crucial for robust control.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究动机**：现有面向对象中心的强化学习（Object-Centric RL）方法大多仅按个体对象分解状态表示，将对象之间的交互视为隐式、未建模的部分，导致学习到的策略鲁棒性和迁移性不足。
- **核心问题**：如何在世界模型中显式地学习对象及其交互的结构化表示，以提升策略学习的样本效率和泛化能力。
- **整体含义**：提出一种能够同时捕获对象与交互结构的分解式世界模型，通过显式、模块化的交互建模，让智能体更好地理解环境动态，从而实现更稳健的控制。

### 2. 论文提出的方法论
- **核心思想**：构建分解式交互对象中心世界模型（Factored Interactive Object-Centric World Model, FIOC-WM），将环境动态分解为可组合的交互基元，使世界模型能够显式地对对象之间的关系进行建模。
- **关键技术细节**：
  - **对象中心潜在变量学习**：直接从像素中学习对象中心潜在表示，并借助预训练视觉编码器提取特征。
  - **交互结构学习**：同时学习对象间的交互结构，以解耦和模块化的方式表示对象交互。
  - **分层策略训练**：在习得的世界模型之上构建分层策略——高层策略选择交互的类型和顺序，低层策略负责执行具体的交互动作。
- **算法流程**（文字说明）：
  1. 从原始像素输入中，利用预训练视觉编码器获得特征；
  2. 学习对象中心潜在变量以及它们之间的交互结构；
  3. 以模块化、可组合的方式对环境动态建模；
  4. 基于此世界模型，训练分层策略：高层决策交互序列，低层执行具体控制指令。

### 3. 实验设计
- **数据集/场景**：模拟机器人操作和具身AI基准环境（simulated robotic and embodied-AI benchmarks），具体名称在摘要中未进一步列出。
- **基准对比方法**：与基于世界模型的基线方法（world-model baselines）进行比较，评估样本效率和泛化能力。
- **评估指标**：策略学习的样本效率、泛化性能。

### 4. 资源与算力
- 所提供的文本中**未明确说明**使用的 GPU 型号、数量、训练时长等算力信息。

### 5. 实验数量与充分性
- 文本未详细列出实验组数，但提及在多种模拟机器人和具身AI基准上进行了评估，并进行了与基线的对比实验。摘要强调FIOC-WM在样本效率和泛化能力上超越基线，暗示包含多个环境下的对比，但消融实验的具体情况并未展开。
- 从现有信息来看，实验结果显示了相对于世界模型基线的优势，但无法判断实验是否绝对充分、全面，需查阅正文才能确认是否有更多维度（如不同难度、对象数量、干扰因素等）的评估。

### 6. 论文的主要结论与发现
- 显式的、模块化的交互学习对于鲁棒控制至关重要；
- FIOC-WM 通过分解对象与交互的表示，显著提升了策略学习的样本效率和泛化能力；
- 所学习到的世界模型能自然地分解任务为可组合的交互基元，分层策略能有效利用这一结构。

### 7. 优点
- **方法论亮点**：首次将对象交互结构直接融入到世界模型的潜变量学习中，实现了对象与交互的联合解耦表示；
- **分层策略设计**：高层交互选择与低层执行的分离，增强了复杂任务的组合泛化能力；
- **使用预训练视觉编码器**：减少从零学习视觉特征的负担，提高样本效率。

### 8. 不足与局限
- 摘要未提及实验的规模、环境多样性以及是否测试真实世界场景，可能局限于仿真环境；
- 缺少与其他类型对象中心RL方法的直接比较（仅提及世界模型基线）；
- 没有提供消融实验或模块有效性验证的信息，方法各部分贡献尚不明确；
- 算力需求与可复现性细节缺失，难以评估实际应用门槛；
- 交互结构的自动学习是否总是准确、对复杂动态场景的扩展性仍有待验证。

（完）
