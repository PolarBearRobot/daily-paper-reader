---
title: "HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision–Language–Action Policies"
title_zh: HiMoE-VLA：面向通用视觉-语言-动作策略的分层混合专家架构
authors: "Zhiying Du, Bei Liu, Yaobo Liang, Yichao Shen, Haidong Cao, Xiangyu Zheng, ZhiYuan Feng, Zuxuan Wu, Jiaolong Yang, Yu-Gang Jiang"
date: 2025-09-13
pdf: "https://openreview.net/pdf?id=TX3oGD99CJ"
tags: ["query:model"]
score: 9.0
evidence: 分层混合专家处理异构机器人数据，训练通用VLA策略。
tldr: 机器人数据在形态、动作空间等方面高度异构，导致通用VLA训练困难。本文提出HiMoE-VLA，通过分层混合专家架构显式处理数据异构性，支持大规模多源机器人数据上的通用策略学习。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 异构机器人数据集的融合训练因缺乏对多样性的显式设计而性能下降。
method: 设计分层混合专家（MoE）结构，在不同粒度上对异构因素进行建模和组合。
result: 在多个机器人数据集上，HiMoE-VLA提升了跨形态和任务的迁移性能。
conclusion: HiMoE-VLA为利用大规模异构机器人数据训练通用VLA提供了有效途径。
---

## Abstract
The development of foundation models for embodied intelligence critically depends on access to large-scale, high-quality robot demonstration data. Recent approaches have sought to address this challenge by training on large collections of heterogeneous robotic datasets. However, unlike vision or language data, robotic demonstrations exhibit substantial heterogeneity across embodiments and action spaces as well as other prominent variations such as senor configurations and action control frequencies. The lack of explicit designs for handling such heterogeneity causes existing methods to struggle with integrating diverse factors, thereby limiting their generalization and leading to degraded performance when transferred to new settings. In this paper, we present HiMoE-VLA, a novel vision–language–action (VLA) framework tailored to effectively handle diverse robotic data with heterogeneity. Specifically, we introduce a Hierarchical Mixture-of-Experts (HiMoE) architecture for the action module which adaptively handles multiple sources of heterogeneity across layers and gradually abstracts them into shared knowledge representations.
Through extensive experimentation with simulation benchmarks and real-world robotic platforms, HiMoE-VLA demonstrates a consistent performance boost over existing VLA baselines, achieving higher accuracy and robust generalization across diverse robots and action spaces.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究动机**：构建具身智能基础模型需要大规模、高质量的机器人演示数据。近期工作尝试聚合多个异构机器人数据集进行统一训练，但面临巨大挑战。
- **核心问题**：与视觉或语言数据不同，机器人数据在多个层面存在显著异质性，包括：
  - 机器人形态（不同硬件平台）
  - 动作空间（连续/离散、不同自由度）
  - 传感器配置
  - 动作控制频率等。
- **整体含义**：现有的通用视觉-语言-动作（VLA）策略**缺乏显式处理上述异质性的设计**，导致多源数据融合困难，模型泛化受限，在迁移到新环境时性能下降。本文旨在填补这一空白，让通用策略能有效利用异构数据。

### 2. 论文提出的方法论
- **核心思想**：提出**分层混合专家架构（HiMoE）**，专门针对 VLA 模型的动作模块进行重构，**在不同层级的粒度上显式建模并处理多种异质性来源**，最终将其逐步抽象为共享的知识表示。
- **关键技术细节**：
  - **分层 MoE 结构**：在动作输出模块中堆叠多个混合专家层，每层包含多个并行专家网络。
  - **自适应门控**：每层使用一个门控网络，根据输入特征自适应地激活最相关的专家组合，从而针对不同形态、动作空间等选择合适的处理路径。
  - **渐进式抽象**：底层专家负责捕获**细粒度、形态相关的异构模式**（如特定传感器的特征）；上层专家则将这些模式**融合、抽象为与具体平台无关的通用动作表示**，进而预测动作。
  - **整体框架**：HiMoE-VLA 在标准的视觉-语言骨干网络之上，插接分层 MoE 动作头，实现对多源异构动作空间的统一建模。
- **算法流程概括**：视觉-语言输入 → 骨干网络提取共享特征 → 输入分层 MoE 动作模块 → 各层级门控根据特征动态选择专家 → 低层输出异构特征，高层输出通用表示 → 最终动作预测。文中未提供具体公式，但核心是门控网络输出的专家权重与对应专家输出的加权组合。

### 3. 实验设计
- **数据集与场景**：摘要提及在**模拟基准测试（simulation benchmarks）** 和 **真实机器人平台（real-world robotic platforms）** 上进行验证。具体数据集名称（如 CALVIN、Open X-Embodiment 等）在给定文本中未明确列出。
- **Benchmark 任务**：应涵盖多机器人形态、多任务的操作与移动等泛化能力测试。
- **对比方法**：与**现有的 VLA 基线方法（existing VLA baselines）** 进行对比，以验证性能提升。基线具体名称未提供，但通常可能包括 RT 系列、OpenVLA 等通用策略。

### 4. 资源与算力
- **明确说明**：**未在提供的文本中提及**。摘要与元数据均未给出所用 GPU 型号、数量、训练时长或单次实验算力消耗等具体信息。

### 5. 实验数量与充分性
- **大致实验量**：根据描述，进行了 **“广泛的实验（extensive experimentation）”**，应包括：
  - 多种模拟基准的测试；
  - 真实机器人的迁移与评估；
  - 可能包含消融实验（如验证分层设计、专家数量等的作用）。
- **充分性评价**：由于缺乏具体的实验指标、表格和对比数据，仅从文字推断，实验覆盖了模拟到现实（Sim-to-Real）的关键环节，并包含了与基线的对比，结构较为完整。但**具体实验组数、统计显著性、误差棒等细节均不可知**。
- **客观与公平性**：声称与现有基线对比，且架构改动集中在特定模块（动作模块），理论上可进行公平的消融对比，但受限于信息细节，无法最终评判。

### 6. 论文的主要结论与发现
- **性能提升**：HiMoE-VLA 在多个异构机器人数据集上，相比现有 VLA 基线，取得了**持续且一致的性能提升**。
- **泛化能力**：在跨不同机器人形态和动作空间的任务上，HiMoE-VLA 展现出**更高的准确率和鲁棒的泛化性**。
- **架构有效性**：分层混合专家结构是一种有效途径，能够**显式处理数据中的多源异质性**，并将其转化为可共享的知识，从而实现通用策略训练。
- **最终启示**：该工作为后续利用大规模、异构的机器人数据来训练更通用的具身智能策略提供了重要的技术思路和实证支持。

### 7. 优点
- **问题切入精准**：直接针对大规模机器人数据融合中最核心的异质性瓶颈，而非绕开问题。
- **方法设计优雅**：分层 MoE 架构提供了一种自然、灵活的方式来解耦和级联处理不同粒度的异质因素，从“异构专用”渐进至“通用共享”，思路清晰。
- **实验验证全面**：同时包含模拟基准和真实机器人实验，增强了方法的实用性和可信度，符合具身智能研究的要求。
- **可拓展性强**：该架构可方便地通过增加新的专家网络来适配更多种类的机器人和数据，具备良好的增长潜力。

### 8. 不足与局限
- **关键实验细节缺失**：基于所提供文本，无法获知具体的测试基准、基线方法名称及详细性能数值，完整性和可复现性受影响。
- **覆盖范围待验证**：虽提及真实机器人，但未说明部署的机器人类型及任务的复杂性，在极端动态环境或精细操作中的表现未知。
- **潜在效率问题**：混合专家结构通常会增加模型参数和推理成本，文中未讨论由此带来的计算开销与效率折损。
- **依赖与风险**：框架建立在预训练的视觉-语言模型之上，其性能上限受骨干网络制约；门控网络的路由策略可能在大规模异构数据下引入负载不均衡或专家坍塌等 MoE 常见风险，但摘要未给出分析。

（完）
