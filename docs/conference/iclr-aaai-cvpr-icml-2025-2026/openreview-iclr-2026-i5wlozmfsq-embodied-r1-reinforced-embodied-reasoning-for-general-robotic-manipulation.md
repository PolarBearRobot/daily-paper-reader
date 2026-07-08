---
title: "Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation"
title_zh: Embodied-R1：面向通用机器人操作的强化具身推理
authors: "Yifu Yuan, Haiqin Cui, Yaoting Huang, Yibin Chen, Fei Ni, Zibin Dong, Pengyi Li, YAN ZHENG, Hongyao Tang, Jianye HAO"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=i5wlozMFsQ"
tags: ["query:model"]
score: 8.0
evidence: 具身无关的指向表示实现跨本体泛化的 VLM 操作
tldr: Embodied-R1 针对具身 AI 中“看见-执行”鸿沟，提出“指向”作为统一的本体无关中间表示，定义四种核心指向能力，构建大规模数据集并用两阶段强化微调训练 VLM，实现跨本体泛化的推理与操作。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 数据匮乏和本体异构导致泛化困难。
method: 引入指向中间表示，构建数据集，强化微调 VLM。
result: 跨本体零样本泛化，桥接高层理解与低层动作。
conclusion: 指向表示有效解决本体异构，推动通用机器人操作。
---

## Abstract
Generalization in embodied AI is hindered by the "seeing-to-doing gap", stemming from data scarcity and embodiment heterogeneity. To address this, we pioneer "pointing" as a unified, embodiment-agnostic intermediate representation, defining four core embodied pointing abilities that bridge high-level vision-language comprehension with low-level action primitives. We introduce Embodied-R1, a 3B Vision-Language Model (VLM) specifically designed for embodied reasoning and pointing. We use a wide range of embodied and general visual reasoning datasets as sources to construct a large-scale dataset, Embodied-Points-200K, which supports key embodied pointing capabilities. Then we train Embodied-R1 using a two-stage Reinforced Fine-tuning (RFT) curriculum with specialized multi-task reward design. Embodied-R1 achieves state-of-the-art performance on 11 embodied spatial and pointing benchmarks. Critically, it demonstrates robust zero-shot generalization by achieving a 56.2% success rate in the SIMPLEREnv and 87.5% across 8 real-world XArm tasks without any task-specific fine-tuning, representing a 62% improvement over strong baselines. Furthermore, the model exhibits high robustness against diverse visual disturbances. Our work shows that a pointing-centric representation, combined with an RFT training paradigm, offers an effective and generalizable pathway to closing the perception-action gap in robotics.

---

## 论文详细总结（自动生成）

# 论文总结：Embodied-R1 — 面向通用机器人操作的强化具身推理

## 1. 核心问题与整体含义
- **核心挑战**：具身人工智能面临“看见—执行”鸿沟（seeing-doing gap），即高层视觉语言理解与低层动作执行之间存在巨大断裂。
- **产生根源**：
  - 真实环境交互数据匮乏；
  - 机器人本体（机械臂、夹爪、底座等）异构性严重，导致泛化困难。
- **整体含义**：通过统一的、本体无关的中间表示来桥接理解与动作，从而推动通用机器人操作。

## 2. 方法论
### 核心思想
- **“指向”（Pointing）作为本体无关的中间表示**：将高层视觉语言理解映射为 2D 图像平面上的指向坐标或区域，再让低层控制器根据指向执行操作，从而解除对具体本体的依赖。
- **四种核心具身指向能力**：定义并强化四类关键指向技能（如直接指向目标、指向物体部位、沿路径指向等），覆盖操作所需的空间推理。

### 技术细节与流程
- **模型**：基于 3B 参数的视觉语言模型（VLM）Embodied-R1。
- **数据构建**：
  - 汇集多种具身数据集与通用视觉推理数据源；
  - 构造大规模数据集 **Embodied-Points-200K**，支持四种核心指向能力。
- **训练范式**：
  - 采用**两阶段强化微调（RFT）课程**，包含专门设计的**多任务奖励函数**。
  - 第一阶段：初步对齐视觉语言理解与指向输出；
  - 第二阶段：通过强化学习进一步精调，使指向预测与任务成功奖励对齐。

## 3. 实验设计
- **评测基准**：
  - 11 个具身空间推理与指向基准（具体名称未在给定内容中列出）；
  - 模拟环境 **SIMPLEREnv**，测试零样本泛化成功率；
  - **8 个真实世界 XArm 机械臂任务**，不进行任何任务微调，验证跨现实泛化。
- **对比方法**：与多个强基线方法进行比较（基线名称未提及），且所给摘要称其性能提升高达 62%。
- **鲁棒性测试**：在多种视觉干扰下评估模型的稳定性。

## 4. 资源与算力
- 论文提供的内容中**未明确说明**使用的 GPU 型号、数量及训练时长，仅提及模型规模为 3B 参数。因此无法总结算力消耗。

## 5. 实验数量与充分性
- **实验组合**：
  - 在 11 个空间/指向基准上进行了全面评测；
  - 在仿真环境和真实世界场景下完成了零样本泛化实验；
  - 进行了视觉干扰鲁棒性测试；
  - （根据常见范式推测可能包含消融实验，但给定内容未提及）。
- **充分性与客观性**：
  - 多基准、仿真-真实双重验证体现了较好的实验广度；
  - 对比强基线并报告提升幅度，具有一定客观性；
  - 但由于未披露具体基线名称、消融实验细节和统计显著性，部分结论的公平性尚无法完整评判。

## 6. 主要结论与发现
- 以**指向为核心**的表示能够有效解决机器人本体异构问题，实现跨本体的零样本迁移。
- 两阶段 **RFT 课程**与多任务奖励设计，使小型 VLM 在多种具身推理任务上达到最优性能。
- **关键结果**：
  - 在 SIMPLEREnv 中零样本成功率 **56.2%**；
  - 在 8 个真实 XArm 任务中成功率 **87.5%**，相较强基线提升 62%；
- 模型对多种视觉干扰表现出**高鲁棒性**，证明指向表示的优势。

## 7. 优点
- **方法亮点**：
  - 创新性地引入“指向”作为**统一的、本体无关的中间表示**，解耦感知与动作。
  - 两阶段强化微调**贴合具身决策需求**，将预训练对齐与任务奖励直接结合起来。
  - 仅使用 3B 规模的 VLM 便取得强泛化能力，效率较高。
- **实验亮点**：
  - 覆盖仿真与真实机器人，零样本评估严格，贴近实际应用。
  - 多基准评价和视觉干扰测试凸显模型鲁棒性。

## 8. 不足与局限
- **信息缺失**：论文正文未提供，多数细节未知：
  - 具体基准名称、强基线方法的对比细节无法得知；
  - 消融实验（如 RFT 两阶段的作用、指向能力数量贡献）未被提及；
  - 算力资源未报告，难以评估训练成本。
- **应用局限**：
  - 模型为 3B 规模，在极度复杂的长序列操作中可能仍力不从心；
  - 真实世界实验仅采用 XArm 单一平台，跨更多本体的泛化证据有限；
  - “指向”表示可能无法处理所有形式的操作（如高维力控、灵巧手操作），其通用性尚待验证。
- **偏差风险**：数据集构建来源和筛选标准未知，可能存在场景偏差；真实世界任务仅8种，任务多样性可能不足。

（完）
