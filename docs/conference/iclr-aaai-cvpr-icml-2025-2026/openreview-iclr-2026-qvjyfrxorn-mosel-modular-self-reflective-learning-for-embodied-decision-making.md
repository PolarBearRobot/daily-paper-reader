---
title: "MoSEL: Modular Self-Reflective Learning for Embodied Decision-Making"
title_zh: MoSEL：面向具身决策的模块化自反思学习
authors: "Jr-Jen Chen, Yu-Chiang Frank Wang, Yilun Du"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=QVjyFrXOrn"
tags: ["query:model"]
score: 7.0
evidence: 面向长程机器人决策的模块化自反思学习
tldr: MoSEL 为让机器人自主执行复杂长程任务，提出模块化自反思学习框架，利用层次规划与多模态基础模型（如 LVLM、视频扩散等）分解任务，并通过自反思学习循环从执行经验中改进，无需人类监督即可提升决策能力。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 机器人难以自主完成长程任务。
method: 结合层次规划与多模态基础模型，引入自反思学习。
result: 实现无监督自改进的长程任务执行。
conclusion: 自反思学习为机器人长程自主决策开辟新范式。
---

## Abstract
Enabling robots to autonomously perform complex, long-horizon tasks remains challenging due to the need for hierarchical reasoning and dynamic adaptability. Humans overcome this by interacting with environment and learning from their own experience, which is infeasible for existing robots without human supervision. To enable similar capabilities in robotic agents, we introduce MoSEL, an modular self-reflective learning framework for robotic decision making. MoSEL combines hierarchical planning with multimodal foundation models, including LVLMs, video diffusion, and inverse dynamics models. These components work together to break down complex tasks, generate executable visual plans, and perform actions. We further introduce a modular self-reflective learning framework that autonomously identifies failures and iteratively refines policies with minimal human intervention. Evaluations on LIBERO-LONG and RoboTwin benchmarks demonstrate that MoSEL outperforms existing methods, achieving over $33\%$ and $46\%$ average performance improvements, respectively. Our results underscore the effectiveness of autonomous self-improvement and accurate failure identification in advancing robust robotic manipulation.

---

## 论文详细总结（自动生成）

基于提供的论文摘要及元数据，以下是对《MoSEL: Modular Self-Reflective Learning for Embodied Decision-Making》的结构化总结。

### 1. 论文的核心问题与整体含义
- **核心问题**：让机器人自主执行复杂、长时间跨度的任务（long-horizon tasks）仍面临巨大挑战，主要是因为这类任务需要**层次化推理**与**动态适应能力**。
- **研究动机**：人类能够通过与环境的交互并从自身经验中学习来克服此类挑战，而现有机器人系统通常无法在缺乏人类监督的情况下实现这种自我改进。因此，如何赋予机器人智能体类似的自主学习和纠错能力，是具身决策领域的关键空白。
- **整体含义**：本文旨在通过提出一种模块化自反思学习框架，使机器人能够像人类一样从执行失败中自主识别问题并迭代优化策略，从而在无需人工干预的情况下，逐步提升处理长程复杂操作任务的能力。

### 2. 论文提出的方法论
- **核心思想**：构建一个名为MoSEL的**模块化自反思学习**框架，将层次化规划与多模态基础模型相结合，并引入一个自反思循环，使机器人能够自主识别失败并改进其决策。
- **关键技术细节**：
  - **模块化架构**：框架由多个功能模块协同工作，包括大型视觉语言模型（LVLMs）、视频扩散模型（video diffusion）和逆动力学模型（inverse dynamics models）。
  - **任务分解与执行流程**：首先，框架利用层次化规划将复杂的长程任务**分解**为可执行的子目标；接着，通过视频扩散等模型生成可执行的**视觉计划**；最后，根据计划执行具体**动作**。
  - **自反思学习机制**：框架的核心创新点在于引入了一个**模块化自反思学习循环**。该循环能够在机器人执行任务后，**自主识别失败案例**，并依据识别出的错误类型，**迭代地优化和调整其决策策略**。这一过程最小化了人类的介入，实现了从经验中自主进化。

### 3. 实验设计
- **评估基准**：论文在两个具身决策基准上进行了评估。
  - **LIBERO-LONG**：用于测试长时间跨度任务执行能力。
  - **RoboTwin**：另一个机器人操作任务基准。
- **对比方法**：文中声称MoSEL**优于现有方法**，在LIBERO-LONG和RoboTwin上分别取得了超过33%和46%的平均性能提升。但摘要未列出具体的对比基线方法名称。
- **实验重点**：评估目标是验证自主自改进能力与精确失败识别在推进鲁棒机器人操作上的有效性。

### 4. 资源与算力
- 提供的文本（摘要及元数据）中**未明确提及**所使用的具体计算资源，包括GPU型号、数量或训练时长。关于模型训练与推理的算力开销细节缺失。

### 5. 实验数量与充分性
- **实验规模**：摘要明确指出在两个主要的具身决策基准（LIBERO-LONG和RoboTwin）上进行了评估，并报告了平均性能提升数据。这暗示至少包含与基准方法对比的主实验。
- **充分性与客观性**：
  - **有限的信息能判断充分性**：由于仅提供了摘要，无法得知是否包含消融实验（如验证各模块贡献、自反思迭代的作用等）、在不同任务维度的细分实验、鲁棒性测试或定性分析。从摘要来看，实验覆盖了两个公认的基准，但其内部实验的全面性（如对比方法的数量、随机种子下的重复实验等）无法证实。
  - **客观性**：采用了公开基准进行对比，并给予量化提升指标，在形式上是客观的。但缺少具体对比对象和实验配置细节，使得结果的公平性难以仅凭摘要评判。

### 6. 论文的主要结论与发现
- MoSEL框架能够有效地将多模态基础模型与自反思学习相结合，解决长程机器人操作问题。
- 所提出的**自主自改进**和**精确失败识别**能力是提升机器人操作鲁棒性的关键因素。
- 该方法在两个挑战性基准上**显著优于现有方法**，验证了其有效性和先进性。
- 研究结果强调了自反思学习范式为机器人自主进行长程决策开辟了新路径。

### 7. 优点
- **创新性整合**：巧妙地将层次化规划、多种前沿基础模型（LVLM、视频扩散、逆动力学）与独特的自反思学习机制融合到一个统一的决策框架中。
- **解决关键痛点**：直面了具身智能中高度依赖人类监督进行错误修正的难题，提出的自主反思与迭代改进思路显著降低了人工介入需求。
- **性能显著**：在权威基准测试上取得了大幅度的性能领先（超33%和46%），证明了方法的实用潜力。
- **模块化设计**：模块化结构可能使得各组件能够独立升级或替换，具有较好的灵活性和可扩展性。

### 8. 不足与局限
- **实验细节严重缺失**：基于当前文本，无法获知对比的具体方法、是否进行了消融研究、任务类型分布、成功率计算方式等，这为全面评估方法的有效性和边界带来了困难。
- **计算资源未提及**：多模态基础模型（特别是视频扩散模型）的推理与微调通常计算开销巨大，算力成本的缺失限制了对其实际应用可行性的判断。
- **自反思的局限未知**：自反思学习仅在执行失败时触发，其发现问题能力的边界、对根本原因分析的粒度、以及迭代优化的收敛性保障等，均在提供的信息中未得到探讨。
- **跨场景泛化性存疑**：尽管在两个基准上表现良好，但仅限于特定的操作任务。从摘要无法得知该方法在更开放、非结构化的环境或完全不同的任务形态下的迁移能力。

（完）
