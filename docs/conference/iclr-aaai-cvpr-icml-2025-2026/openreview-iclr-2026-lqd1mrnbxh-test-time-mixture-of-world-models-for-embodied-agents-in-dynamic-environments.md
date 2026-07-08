---
title: Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments
title_zh: 动态环境中具身智能体的测试时混合世界模型
authors: "Jinwoo Jang, Minjong Yoo, Sihyung Yoon, Honguk Woo"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=LQD1MrnbxH"
tags: ["query:model"]
score: 7.0
evidence: "测试时混合世界模型，通过在线更新路由适应动态环境,用于具身智能体"
tldr: 针对语言模型基具身智能体在动态环境中适应性不足的问题，提出测试时混合世界模型（TMoW），通过在线更新专家路由函数，实现跨未见域的自适应推理与决策，提升了模型在动态场景下的灵活性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 语言模型基具身智能体在动态环境中适应性有限，构建准确灵活的世界模型至关重要。
method: 将混合专家范式扩展到具身智能体，提出TMoW框架，在测试时动态更新路由函数以选择合适的世界模型。
result: 实验表明TMoW能够有效适应未见动态域，提升推理与决策性能。
conclusion: TMoW为具身智能体提供了一种测试时自适应机制，与世界动作模型的概念相关。
---

## Abstract
Language model (LM)-based embodied agents are increasingly deployed in real-world settings. Yet, their adaptability remains limited in dynamic environments, where constructing accurate and flexible world models is crucial for effective reasoning and decision-making. To address this challenge, we extend the Mixture-of-Experts (MoE) paradigm to embodied agents. While conventional MoE architectures modularize knowledge into expert components with pre-trained routing, they remain rigid once deployed, making them less effective for adapting to unseen domains in dynamic environments. We therefore propose Test-time Mixture of World Models (TMoW), a framework that enhances adaptability to unseen and evolving domains. TMoW updates its routing function over world models at test time, unlike conventional MoE where the function remains fixed, enabling agents to recombine existing models and integrate new ones for continual adaptation. It achieves this through (i) multi-granular prototype-based routing, which adapts mixtures across object- to scene-level similarities, (ii) test-time refinement that aligns unseen domain features with prototypes during inference, and (iii) distilled mixture-based augmentation, which efficiently constructs new models from few-shot data and existing prototypes. We evaluate TMoW on VirtualHome, ALFWorld, and RLBench benchmarks, demonstrating strong performance in both zero-shot adaptation and few-shot expansion scenarios, and showing that it enables embodied agents to operate effectively in dynamic environments.

---

## 论文详细总结（自动生成）

# 论文总结：《测试时混合世界模型：动态环境中具身智能体的自适应决策》

## 1. 论文的核心问题与整体含义

- **核心问题**：基于语言模型的具身智能体在真实动态环境中适应性有限。传统世界模型构建方式一旦部署便固化，难以应对未知的、不断变化的场景，制约了推理与决策的效果。
- **研究动机**：现实世界动态性强，智能体需要在部署后持续适应新环境，而现有的混合专家（MoE）架构中的路由函数在训练后保持不变，无法在线更新，导致模型僵化。
- **整体含义**：提出“测试时混合世界模型”（TMoW），让具身智能体在测试阶段动态更新世界模型的路由函数，从而实现对新领域的自适应，提升在未见动态环境中的灵活性和泛化能力。

## 2. 论文提出的方法论

- **核心思想**：将混合专家范式扩展至具身智能体的世界模型，并在测试时引入动态路由更新机制，打破传统MoE路由固定的限制。
- **关键技术与流程**（基于摘要推测）：
  - **多粒度原型路由**：基于物体级到场景级的多粒度相似度，自适应地混合不同专家世界模型，实现更细粒度的知识组合。
  - **测试时精炼**：在推理过程中，将未见域的特征与已有原型对齐，动态调整路由权重，使模型能快速适应分布变化。
  - **蒸馏式混合增强**：利用少量新样本和已有原型高效构建新的世界模型，支持快速扩展能力。
- **与现有MoE的区别**：路由函数在测试时持续优化，而非一次性预训练后固定。

## 3. 实验设计

- **测试环境/数据集**：
  - VirtualHome（家庭环境）
  - ALFWorld（具身文本游戏）
  - RLBench（机器人操作任务）
- **评估场景**：
  - **零样本自适应**：模型在未见域中的直接推理和决策能力。
  - **少样本扩展**：提供少量新域数据后模型性能提升。
- **对比方法**：未在摘要中指明，推测可能包括传统MoE、固定路由的世界模型、无自适应机制的基线等。

## 4. 资源与算力

- 摘要中**未提及**GPU型号、数量、训练时长等算力信息。需查阅全文方可获得具体资源开销。

## 5. 实验数量与充分性

- **实验组数预估**：三个不同特征的基准（VirtualHome、ALFWorld、RLBench），涵盖室内、文本、机器人操作场景，每个基准可能包含多个子任务或域迁移。结合零样本和少样本两种设定，以及消融实验（如移除测试时精炼或蒸馏增强），可能包含**10–20组有效对比实验**。
- **充分性**：覆盖多样化具身场景，场景类型差异大，有利于验证方法的泛化性。存在零样本和少样本两种扩展设定，对自适应能力的考察相对全面。
- **客观性与公平性**：若对比基线统一使用相同预训练世界模型并遵循一致的评估协议，则较为公平。但摘要未描述细节，可能存在基线选择偏差。

## 6. 主要结论与发现

- TMoW使具身智能体在未见动态域中表现出色，有效提升推理与决策性能。
- 测试时路由更新能够利用已有世界模型组合与新模型快速构建，实现持续自适应。
- 该方法与世界动作模型的概念相关联，为具身智能体的在线自适应提供了一种新范式。

## 7. 优点

- **创新性强**：首次将测试时路由更新引入混合世界模型，解决了传统MoE在部署后固定不变的痛点。
- **多粒度设计**：从物体到场景级的原型匹配，使知识组合更灵活。
- **实用价值高**：支持零样本和少样本两种现实部署场景，且可与新的世界模型无缝集成，具有良好的扩展性。
- **评估多样**：在三个差异显著的具身基准上验证，结果更具说服力。

## 8. 不足与局限

- **细节缺失**：仅靠摘要无法判断路由更新的计算复杂度、延迟，以及蒸馏增强的具体实现稳定性。
- **实验覆盖风险**：未提及仿真到现实（Sim2Real）的迁移实验，所有评估均在模拟器内，真实机器人场景的适用性待验证。
- **对比方法不明确**：缺少与最新自适应技术（如在线元学习、持续学习等方法）的直接比较，可能无法完全体现优势。
- **潜在偏差**：原型路由假设新域特征可被现有原型覆盖，当域差异极大时可能失效。
- **算力未知**：测试时更新可能引入额外推理开销，实际部署的实时性需进一步讨论。

（完）
