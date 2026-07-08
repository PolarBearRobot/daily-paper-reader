---
title: "VISOR: VIsual Spatial Object Reasoning for Language-driven Object Navigation"
title_zh: VISOR：面向语言驱动物体导航的视觉空间对象推理
authors: "Francesco Taioli, Shiping Yang, Sonia Raychaudhuri, Marco Cristani, Unnat Jain, Angel X Chang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=HhBxIQ0CA2"
tags: ["query:model"]
score: 7.0
evidence: 紧凑的3B参数VLA智能体，进行视觉空间推理以实现语言驱动的物体导航
tldr: 针对语言驱动物体导航中泛化性和可解释性不足的问题，提出VISOR，一个3B参数的视觉-语言-动作模型，通过类人空间推理实现高效导航，平衡了性能与计算成本，为导航领域的通用模型提供了参考。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有方法要么泛化性差，要么计算成本高且难以将推理整合回导航策略。
method: 设计紧凑的3B参数VLA模型，执行类人具身推理，直接输出导航动作。
result: 在物体导航任务中实现了高性能和动作级可解释性。
conclusion: 展示了VLA模型在具身导航中的潜力，但主要限于导航任务。
---

## Abstract
Language-driven object navigation requires agents to interpret natural language descriptions of target objects, which combine intrinsic and extrinsic attributes for instance recognition and commonsense navigation. Existing methods either (i) use end-to-end trained models with vision–language embeddings, which struggle to generalize beyond training data and lack action-level explainability, or (ii) rely on modular zero-shot pipelines with large language models (LLMs) and open-set object detectors, which suffer from error propagation, high computational cost, and difficulty integrating their reasoning back into the navigation policy.
To this end, we propose a compact 3B-parameter Vision–Language–Action (VLA) agent that performs human-like embodied reasoning for both object recognition and action selection, removing the need for stitched multi-model pipelines. Instead of raw embedding matching, our agent employs explicit image-grounded reasoning to directly answer "Is this the target object?" and "Why should I take this action?" The reasoning process unfolds in three stages: "think", "think summary", and "action", yielding improved explainability, stronger generalization, and more efficient navigation. Code and dataset available upon acceptance.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：语言驱动的物体导航（Language-driven Object Navigation）要求智能体理解目标物体的自然语言描述（同时包含内在属性与外在属性），并基于常识进行导航。现有方法存在两类困境：
  - 端到端模型（使用视觉-语言嵌入）泛化能力弱，缺乏动作层面的可解释性；
  - 基于大语言模型和开放集检测器的模块化零样本流水线存在错误传播、计算成本高以及难以将推理过程重新融入导航策略的问题。
- **整体含义**：该论文提出一种兼顾泛化性、可解释性与计算效率的紧凑型视觉-语言-动作（VLA）模型，旨在以类人具身推理的方式一步到位完成物体识别与动作选择，不再需要拼接多个模型。

### 2. 论文提出的方法论
- **核心思想**：用一个 3B 参数的紧凑 Vision–Language–Action（VLA）智能体，执行显式的、图像锚定的推理，直接回答“这是目标物体吗？”以及“为什么采取这个动作？”，避免 raw embedding matching。
- **推理流程**：推理过程展开为三个阶段：
  - **Think**（思考）：对外部视觉输入与语言指令进行初步分析；
  - **Think Summary**（思考总结）：提炼关键推理信息；
  - **Action**（动作）：输出最终的导航动作。
- **技术特点**：模型直接生成导航动作，整个推理过程透明、可解释，消除了多模型串联带来的误差累积和计算冗余。

### 3. 实验设计
- **任务与场景**：针对语言驱动的物体导航任务（具体数据集或模拟环境未在提供文本中明确，摘要及元数据中仅提及“language-driven object navigation”，可能为常用 benchmark，如 Habitat ObjectNav 或 RoboTHOR 等，但无直接说明）。
- **对比方法**：根据摘要，对比的思路涵盖两类方法：
  - 端到端训练、依赖视觉-语言嵌入的方法；
  - 基于大语言模型和开放集目标检测的模块化 zero-shot 流水线。
- **具体数据集/benchmark 名称未在提供材料中列出。**

### 4. 资源与算力
- **论文中未明确提及 GPU 型号、数量、训练时长等算力信息**。元数据仅指出模型参数量为 3B，暗示该模型相对轻量，平衡了性能与计算成本，但具体算力开销需要查阅原文。

### 5. 实验数量与充分性
- 提供材料中未列出具体实验组数、消融实验或不同数据集的细节。从摘要推断，实验应至少包含：
  - 与两种主流范式（端到端、模块化 LLM）的对比；
  - 在物体导航任务上的总体性能评测。
- 由于缺乏具体统计量和实验设置，无法评价实验的充分性与客观公平性。元数据中“证据”提到“紧凑的3B参数VLA智能体……实现高效导航”，提示实验可能展示了性能-效率的折衷优势。

### 6. 论文的主要结论与发现
- VLA 模型在物体导航任务中能够实现高性能与动作级的可解释性；
- 紧凑的 3B 参数设计证明了在具身导航中平衡性能与计算成本的可行性；
- 该工作展示了 VLA 模型在具身导航领域的潜力，但主要是限定在导航任务。

### 7. 优点
- **方法简洁**：用一个紧凑模型替代复杂的多模型流水线，降低错误传播风险；
- **推理可解释**：通过分阶段思考-总结-动作流程，提供类人推理过程，增强可解释性；
- **性能与效率平衡**：3B 参数的规模相对较小，兼顾泛化性和计算成本；
- **一体化输出**：直接产生导航动作，避免推理结果难以嵌入导航策略的问题。

### 8. 不足与局限
- **任务局限**：论文结论明确指出主要限于导航任务，通用性尚待验证；
- **实验细节缺失**：由于提供材料不完整，无法评估实验的全面性、数据集多样性以及是否在多个 benchmark 上验证（如不同房间布局、不同物体类别等）；
- **消融与鲁棒性未知**：材料未提及对视觉空间推理各阶段的消融研究，或对噪声、对抗样本等的鲁棒性分析；
- **外部比较可能不足**：仅提及与两类方法的对比，但没有给出具体模型名称或最新的强基线，难以判断性能的真实领先程度；
- **探索范围有限**：未提及现实世界机器人实验或 sim-to-real 迁移的表现。

（完）
