---
title: "Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization"
title_zh: Tactile-VLA：释放视觉-语言-动作模型的物理知识以实现触觉泛化
authors: "Jialei Huang, Shuo Wang, Fanqi Lin, Yihang Hu, Chuan Wen, Yang Gao"
date: 2025-09-10
pdf: "https://openreview.net/pdf?id=uhB3pbJpRm"
tags: ["query:model"]
score: 9.0
evidence: 融合触觉传感的视觉-语言-动作模型，用于接触密集型物理交互
tldr: 针对VLA模型缺乏精细物理接触引导的问题，提出Tactile-VLA，将触觉传感与视觉、语言、动作深度融合，通过混合位置-力控制器和推理模块将模型意图转化为精确物理动作。实验表明该框架能有效处理需要力控的接触密集型任务，拓展了VLA到真实物理交互的能力。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有VLA模型在接触密集型任务中缺乏细粒度力控，难以实现精确物理交互。
method: 提出深度融合视觉、语言、动作和触觉的框架，结合混合位置-力控制器和推理模块。
result: 在需要力控的任务中展现出优于纯视觉/语言VLA的泛化能力。
conclusion: 触觉感知的整合显著增强了VLA在真实世界物理操作中的适用性。
---

## Abstract
Vision-Language-Action (VLA) models have shown remarkable achievements, driven by the rich implicit knowledge of their vision-language components. However, achieving generalist robotic agents demands precise grounding into physical interactions, especially in contact-rich scenarios where fine-grained force control is essential. We advance VLAs' implicit knowledge beyond identifying what to do, towards guiding how to physically interact with real world. This paper introduces Tactile-VLA, a novel framework that deeply fuses vision, language, action, and tactile sensing. This framework incorporates a hybrid position-force controller to translate the model's intentions into precise physical actions and a reasoning module that allows the robot to adapt its strategy based on tactile feedback. Experiments demonstrate Tactile-VLA's effectiveness and generalizability in three key aspects: (1) enabling tactile-aware instruction following, (2) utilizing tactile-relevant commonsense, and (3) facilitating adaptive tactile-involved reasoning. A key finding is that the VLM's prior knowledge already contains semantic understanding of physical interaction; by connecting it to the robot's tactile sensors with only a few demonstrations, we can activate this prior knowledge to achieve zero-shot generalization in contact-rich tasks.

---

## 论文详细总结（自动生成）

# 论文详细总结：Tactile-VLA：释放视觉-语言-动作模型的物理知识以实现触觉泛化

## 1. 核心问题与研究动机
- **核心问题**：当前视觉-语言-动作（VLA）模型虽然能利用丰富的视觉-语言先验知识，但在接触密集型（contact-rich）机器人任务中缺乏精细的力觉引导，难以应对真实世界的物理交互。简单地说，VLA模型知道“做什么”，却不知道“如何以正确的力去接触和操作”。
- **研究动机**：赋予通用机器人智能体一种能力，使其不仅能理解视觉场景和语言指令，还能将内在的物理常识转化为具体的力控动作，从而在需要精细接触的任务中实现泛化。

## 2. 方法论
- **核心思想**：将触觉传感（tactile sensing）深度融合到VLA框架中，通过一个混合位置-力控制器和一个触觉推理模块，将模型的语义意图精准地落地为物理动作。
- **关键技术细节**：
    - **深度融合框架**：模型同时处理视觉、语言、动作和触觉信息。
    - **混合位置-力控制器**：将VLA模型输出的高层意图（如抓取、插入）翻译成精确的末端执行器位置和接触力指令，实现力位混合控制。
    - **触觉推理模块**：机器人可根据触觉反馈（如压力分布、滑觉）在线调整操作策略，体现自适应能力。
    - **少量演示激活先验**：论文提出一个关键发现——VLM（视觉-语言模型）的预训练知识中已经包含物理交互的语义理解，只需通过少量触觉演示（a few demonstrations），就能激活这些先验知识，实现接触密集型任务的零样本泛化（zero-shot generalization）。

## 3. 实验设计
- **场景与任务**：文中未详列具体数据集或benchmark名称，但从摘要可知实验任务为接触密集型操作，需展示触觉感知相关的能力。包含三个关键评估维度：
    1. 触觉感知的指令跟随（tactile-aware instruction following）
    2. 利用触觉相关的常识（tactile-relevant commonsense）
    3. 自适应触觉参与推理（adaptive tactile-involved reasoning）
- **对比方法**：摘要未列出所有对比基线，但暗示与纯视觉或纯语言的VLA模型进行对比，可能还包括不同传感模态组合的消融。具体基线需参考原文。

## 4. 资源与算力
- **文中未提及**：所提供的摘要中未包含任何关于GPU型号、数量、训练时长或推理算力的信息。此类细节通常在论文正文的“实验设置”或“实现细节”部分出现。由于只提供了摘要，无法给出答案。

## 5. 实验数量与充分性
- **实验组数推测**：从摘要的三个评估维度来看，很可能包含多个子任务或多个难度等级的测试。此外，激活VLM先验的实验设计（少量演示+零样本泛化）暗示了跨任务泛化测试。
- **充分性与客观性**：
    - 评估维度覆盖了指令跟随、常识运用和自适应推理，较为全面。
    - 对比纯视觉/语言VLA，体现了触觉融合的增益。
    - 是否包含详细的消融（如不同传感器配置、推理模块的有无、力控制参数等），摘要未说明，因此无法判断实验的完备性和统计显著性。总体上看，实验方向合理，但缺乏具体定量结果支持。

## 6. 主要结论与发现
- **有效性**：Tactile-VLA 在触觉感知的指令跟随、常识运用和自适应推理方面均优于纯视觉/语言VLA，证明了触觉融合的有效性。
- **关键发现**：VLM的预训练知识包含物理交互的语义理解，通过连接真实触觉传感器并用少量演示激活，即可实现接触密集型任务的零样本泛化。这揭示了VLA模型隐含的物理常识可以被显式地提取和落地。

## 7. 优点
- **创新性**：首次将触觉传感与VLA模型深度融合，并提出“先验知识激活”的新视角，将VLA的常识转化为物理动作。
- **方法实用**：混合位置-力控制器和触觉推理模块的设计，解决了高层语义到低层控制的关键瓶颈。
- **零样本泛化**：仅需少量演示就能在新触觉任务上表现出色，降低了数据获取成本，显示出很强的迁移潜力。
- **多模态整合**：视觉、语言、触觉共同参与动作生成与在线调整，更贴近人类的操作模式。

## 8. 不足与局限
- **实验细节缺失**：仅凭摘要无法获知具体的任务集、成功率定量指标、对比基线的详细信息以及统计检验。
- **触觉传感器依赖**：触觉传感器种类繁多，框架是否在不同触觉传感器上通用尚不明确。
- **任务范围限制**：目前只在接触密集型任务上验证，在其他非接触或大范围移动任务上的表现未知。
- **算力与数据需求不明**：训练所需的计算资源和演示数据量未披露，实际部署成本待评估。
- **真实世界干扰**：摘要未提及对传感器噪声、物体物理属性变化（如刚度、摩擦）的鲁棒性测试。

（完）
