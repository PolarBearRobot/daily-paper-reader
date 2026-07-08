---
title: "dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought"
title_zh: dVLA：带多模态思维链的扩散视觉-语言-动作模型
authors: "Junjie Wen, Minjie Zhu, Jiaming Liu, Zhiyuan Liu, Yicun Yang, Linfeng Zhang, Shanghang Zhang, Yichen Zhu, Yi Xu"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=2rxgospB5s"
tags: ["query:model"]
score: 9.0
evidence: 扩散 VLA 模型配合多模态思维链进行跨模态推理与泛化
tldr: dVLA 提出一种扩散视觉-语言-动作模型，通过统一扩散目标联合优化视觉推理、语言理解和机器人动作，并融入多模态思维链，增强跨模态推理泛化能力，同时集成加速技术降低延迟。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有 VLA 缺乏跨模态深层推理，泛化有限。
method: 结合扩散模型与多模态思维链，统一优化视觉、语言、动作。
result: 实现对新指令和新物体的强泛化，响应快速。
conclusion: 扩散框架与思维链结合有效提升 VLA 跨模态推理与实用化。
---

## Abstract
Vision-language-action (VLA) models have emerged as the next-generation framework in robotics, integrating visual perception, language reasoning, and robotic control into unified systems. In this paper, we present \textbf{dVLA}, a diffusion vision-language-action model with multimodal chain-of-thought. The dVLA optimizes visual reasoning, language comprehension, and robotic actions simultaneously through a unified diffusion-based objective. By harmonizing these modalities into a single cohesive framework, dVLA facilitates more effective cross-modal reasoning, enabling the model to generalize to novel instructions and objects. To ensure practical viability, we also integrate model acceleration methods that substantially decrease robot response times. Extensive evaluations in both simulation and the real world confirm that dVLA significantly outperforms current discrete and continuous VLA models, highlighting the potential of diffusion language model (DLM) based frameworks for robotics.

---

## 论文详细总结（自动生成）

由于所提供的论文内容仅包含标题、摘要和元数据，缺少完整的实验章节、方法论细节和算力信息，以下总结将基于现有内容进行，同时明确指出缺失的信息。

---

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有的视觉‑语言‑动作（VLA）模型在跨模态深层推理上存在不足，导致面对新指令和新物体时泛化能力有限。
- **研究动机**：VLA 正成为机器人领域的下一代框架，需要能同时处理视觉感知、语言推理和动作控制，但多数模型难以真正实现多模态的协同推理。
- **整体含义**：论文提出将扩散模型与多模态思维链（Chain‑of‑Thought）相结合，构建一个统一优化的 VLA 系统，以增强跨模态推理和实际部署时的响应效率。

## 2. 论文提出的方法论
- **核心思想**：将视觉推理、语言理解和机器人动作的训练统一到一个扩散目标（diffusion‑based objective）中，形成端到端可优化的“扩散 VLA”（dVLA）框架。
- **关键技术细节**：
  - 采用**多模态思维链**：模型在推理过程中显式地进行跨模态的逐步推理，使视觉和语言信息能够相互引导，从而提升对复杂指令的理解。
  - 统一扩散优化：视觉特征、语言表示和动作序列被纳入同一个扩散过程，同时去噪生成，强化模态间的一致性。
  - 集成**模型加速技术**：通过加速方法减少机器人响应延迟，提高实际应用的可行性。
- **公式或算法流程**：摘要中未给出具体公式或流程细节，只概括性地描述了联合扩散优化与思维链的结合。

## 3. 实验设计
- **实验场景**：既包含**仿真环境**，也有**真实世界机器人**的评估。
- **基准对比**：与“当前离散和连续的 VLA 模型”进行了比较，但未列出具体的方法名称。
- **评估维度**：衡量对新指令和新物体的泛化能力，以及响应时间。
- **数据相关信息**：摘要未提数据集名称或规模；元数据仅以“ICLR‑2026‑Rejected‑Public”表明来源，未提供实验细节。

## 4. 资源与算力
- **文中未明确说明**所使用的 GPU 型号、数量或训练时长。仅提到“集成模型加速方法以大幅降低机器人响应时间”，未给出具体的算力配置。

## 5. 实验数量与充分性
- **实验组数未知**：由于只提供了摘要，无法判断到底进行了多少组实验（如不同场景、不同消融实验等）。
- **充分性评价受限**：摘要宣称“仿真和真实世界广泛评估”，但缺少定量结果、统计检验和消融分析，无法从现有信息判定实验是否充分或公平。

## 6. 论文的主要结论与发现
- dVLA 在仿真和真实世界任务中均显著超越现有的离散和连续 VLA 模型。
- 基于扩散语言模型（Diffusion Language Model）的框架在机器人领域展现出了巨大潜力。
- 多模态思维链与统一扩散优化的结合，有效提升了跨模态推理和对新指令、新物体的泛化能力。
- 模型加速技术的引入保障了实际应用中的低延迟响应。

## 7. 优点
- **方法论亮点**：
  - 创造性地将扩散模型与多模态思维链融合，实现了视觉、语言、动作在统一扩散框架下的联合建模。
  - 强调跨模态推理的显式建模，有望解决过往 VLA 模型“黑箱”推断的局限。
- **实用导向**：不仅关注准确率，还通过加速技术考虑实际部署的实时性要求。

## 8. 不足与局限
- **信息不完整**：无法获取详细的实验数据、对比方法列表、消融实验设计以及算力需求，因此难以评估该方法的绝对优势、复现难度和泛化范围。
- **可能存在的局限**（基于摘要推断）：
  - 真实世界评估的范围和任务类型未明确，可能偏向特定场景。
  - 扩散模型通常存在采样步数多、计算开销较大的问题，文中虽提到加速，但未说明加速技术细节及对性能的折中影响。
  - 多模态思维链的具体实现方式、所需标注成本等均未披露，可能存在偏差风险。
- **发表状态**：元数据显示该文为 ICLR 2026 的投稿（被拒），可能表明审稿人对实验验证或原创性存在顾虑，但此处不构成对质量的直接判断。

（完）
