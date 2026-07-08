---
title: "MoTVLA: A Vision-Language-Action Model with Unified Fast-Slow Reasoning"
title_zh: "MoTVLA: 一种统一快慢推理的视觉-语言-动作模型"
authors: "Wenhui Huang, Changhe Chen, Han Qi, Chen Lv, Yilun Du, Heng Yang"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=bjApyTEoRf"
tags: ["query:model"]
score: 8.0
evidence: 具有快慢推理的视觉-语言-动作模型，实现高效可控的机器人控制
tldr: 现有VLA模型面临语言可操控性与推理延迟的权衡：不生成推理则操控性弱，生成推理则延迟高。MoTVLA提出基于混合专家Transformer的VLA模型，统一快速-慢速推理与行为策略学习，保留预训练VLM的通用智能用于感知和规划，同时引入领域专家模块提升操作效率。实验表明，该模型在保持低延迟的同时增强了语言操控能力，实现了机器人操作的开世界泛化。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: VLA模型需要在推理速度与语言可操控性之间取得平衡。
method: 混合专家Transformer架构，融合快慢推理与策略学习。
result: MoTVLA在低延迟下实现语言操控，成功泛化到新场景。
conclusion: MoTVLA为高效、可操控的通用机器人VLA模型提供了有效架构。
---

## Abstract
Integrating visual-language instructions into visuomotor policies is gaining momentum in robot learning for enhancing open-world generalization. Despite promising advances, existing approaches face two challenges: limited language steerability when no generated reasoning is used as a condition, or significant inference latency when reasoning is incorporated. In this work, we introduce MoTVLA, a mixture-of-transformers (MoT)–based vision–language–action (VLA) model that integrates fast–slow unified reasoning with behavior policy learning. MoTVLA preserves the general intelligence of pre-trained VLMs (serving as the generalist) for tasks such as perception, scene understanding, and semantic planning, while incorporating a domain expert, a second transformer that shares knowledge with the pretrained VLM, to generate fast domain-specific reasoning (e.g., robot motion decomposition), thereby improving policy execution efficiency. By conditioning the action expert on decomposed motion instructions, MoTVLA can learn diverse behaviors and substantially improve language steerability. Extensive evaluations across natural language processing benchmarks, robotic simulation environments, and real-world experiments confirm the superiority of MoTVLA in both language reasoning and manipulation task performance. We refer to https://motvla.github.io/MoTVLA-website/ for the demonstration videos and corresponding descriptions.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前视觉-语言-动作（VLA）模型在机器人操控中存在一个两难挑战：如果直接使用视觉-语言指令驱动策略，模型的语言可操控性（language steerability）较弱；而如果引入显式推理（生成中间语言计划），则会带来显著的推理延迟，影响实时性能。
- **整体含义**：论文致力于在保持低推理延迟的前提下，大幅提升机器人对语言指令的响应能力和行为多样性，使通用机器人策略既能理解复杂场景，又能高效执行精细动作。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法或流程

- **核心思想**：提出一种基于混合专家 Transformer（Mixture-of-Transformers, MoT）的 VLA 模型 —— MoTVLA，将“快–慢统一推理”与行为策略学习融合在一起。
- **架构组成**：
  - **通用专家（generalist）**：保持预训练视觉语言模型（VLM）的通用智能，负责感知、场景理解和语义规划（慢推理）。
  - **领域专家（domain expert）**：另一个 Transformer，与预训练 VLM 共享知识，专门生成快速的领域特定推理（如机器人运动分解），从而提升策略执行效率。
- **工作流程**：
  - 通用专家对视觉输入和语言指令进行深度理解，形成高层语义计划。
  - 领域专家将高层计划快速转化为机器人可执行的细粒度运动指令（分解动作）。
  - 动作专家（action expert）以这些分解后的运动指令为条件，学习多样化的行为策略，实现更强的语言可操控性。
- **关键特点**：两个 Transformer 协同工作，既保留了 VLM 的泛化能力，又通过领域专家获得低延迟的动作生成能力，避免了传统方法中因生成完整推理过程而导致的延迟。

## 3. 实验设计：数据集/场景、benchmark、对比方法

- **评估维度**：
  - 自然语言处理基准测试（NLP benchmarks）：评估语言推理能力。
  - 机器人仿真环境：测试操作任务表现。
  - 真实世界实验（real-world experiments）：验证开世界泛化。
- **对比方法**（摘要未全部列出，可合理推断）：
  - 可能包含仅使用视觉–语言条件但不生成推理的策略模型（作为低操控性基线）。
  - 包含生成完整推理过程的 VLA 模型（作为高延迟基线）。
  - 其他主流 VLA 或基于 VLM 的策略学习方法。
- **结果**：MoTVLA 在语言推理和操作任务上均表现出优越性，且在低延迟下实现了有效的语言操控。

## 4. 资源与算力

- 论文摘要及提供的元数据中 **未明确提及** 所使用的 GPU 型号、数量、训练时长等算力资源信息。
- 由于仅获取到摘要和元数据，全文详细资源信息可能存在于正文，但当前材料中无法确认。

## 5. 实验数量与充分性

- **实验组数**：摘要指出进行了“广泛评估”，涵盖 NLP 基准、仿真环境、真实世界实验等三个大类，但具体子实验数量（如不同仿真任务数量、消融研究等）未在摘要中详述。
- **充分性与公平性**：
  - 多维度评估（语言、仿真、真实）增强了结论的可靠性。
  - 对比了关键瓶颈（有/无推理、不同架构），问题设定明确，体现了客观比较意图。
  - 因缺少全文，无法判断消融实验的全面性或是否存在潜在偏差，但摘要呈现的方案设计具备合理性。

## 6. 论文的主要结论与发现

- MoTVLA 成功实现了在统一框架内将快–慢推理与行为策略学习相结合。
- 通过引入领域专家快速生成运动分解指令，模型在保持低延迟的同时显著增强了语言可操控性。
- MoTVLA 在语言推理和机器人操控任务上均优于现有方法，并能泛化到真实世界新场景。
- 该架构为开发高效、可操控的通用机器人 VLA 模型提供了有效路径。

## 7. 优点：方法或实验设计上的亮点

- **架构创新**：MoT 设计自然解耦了通用感知与领域高效推理，保留 VLM 能力的同时降低了延迟。
- **问题针对性**：直接瞄准 VLA 中语言可控性与延迟的矛盾，提出了清晰的双专家协同方案。
- **评估全面**：涵盖从语言到仿真再到真实世界的多层次验证，增强了说服力。
- **可解释性**：中间的快推理（运动分解）可作为可解释的动作规划，提升了模型的透明度。

## 8. 不足与局限

- **文本信息有限**：当前仅依据摘要和元数据进行分析，无法获得完整方法论细节（如领域专家的训练方式、损失函数、数据构成）和全面的实验设置。
- **量化结果缺失**：摘要未给出具体性能指标（如成功率、延迟毫秒数），难以评估提升幅度。
- **可能局限**（基于一般推断）：
  - 领域专家的推理范围可能局限于已知的运动分解模式，对全新操作类型泛化能力待考。
  - 双 Transformer 架构可能增加参数量和部署复杂度，对边缘设备的适配性未说明。
  - 真实世界实验的规模和场景多样性未提及，可能存在场景覆盖不足的偏差风险。

（完）
