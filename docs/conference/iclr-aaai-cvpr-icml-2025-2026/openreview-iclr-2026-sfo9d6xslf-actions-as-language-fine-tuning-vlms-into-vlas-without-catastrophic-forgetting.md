---
title: "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting"
title_zh: 动作即语言：无灾难性遗忘地将视觉语言模型微调为视觉语言动作模型
authors: "Asher James Hancock, Xindi Wu, Lihan Zha, Olga Russakovsky, Anirudha Majumdar"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=sFO9d6XSlf"
tags: ["query:model"]
score: 9.0
evidence: 将视觉语言模型微调为机器人控制用的视觉语言动作模型，避免灾难性遗忘
tldr: 针对将视觉语言模型（VLM）微调为用于机器人控制的视觉语言动作模型（VLA）时出现的灾难性遗忘问题，提出VLM2VLA方法，通过将动作表示为语言来对齐预训练与微调的数据分布，从而保留VLM的基础推理与多模态理解能力，提升在新场景中的泛化性能。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 微调VLM为VLA时，学习动作输出会削弱VLM的推理能力，导致泛化性能下降。
method: 提出VLM2VLA，在数据层面将底层动作表示为语言，消除分布不匹配，实现无遗忘的微调。
result: 实验验证该方法能有效保持VLM的语义理解和指令遵循能力，同时提高策略的泛化性能。
conclusion: VLM2VLA为训练通用机器人策略提供了新范式，避免灾难性遗忘。
---

## Abstract
Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：将预训练的视觉语言模型（VLM）通过机器人遥操作数据微调为视觉语言动作模型（VLA），是训练通用机器人策略的一条充满前景的路线。然而，这一过程面临一个根本性的权衡：学习输出底层动作往往会削弱 VLM 原本具备的基础推理与多模态理解能力，导致模型在新场景中的泛化、指令遵循以及语义理解能力下降。
- **核心问题**：这种能力衰退的本质是灾难性遗忘。论文指出，遗忘的根源在于 VLM 的大规模互联网预训练语料与机器人微调数据之间存在严重的分布不匹配。机器人动作通常以连续数值向量的形式呈现，与 VLM 习惯处理的自然语言文本差异巨大，从而破坏了预训练阶段习得的表征。
- **整体含义**：该论文试图从根本上解决这一分布不匹配问题，使得在微调 VLM 为 VLA 时，既能获得产生动作的能力，又能完整保留 VLM 的通用世界知识与推理能力，从而在不牺牲泛化性的前提下推进通用机器人策略的学习。

## 2. 论文提出的方法论

- **核心思想**：将低层动作转换为自然语言表示，从数据层面直接消除预训练与微调之间的模态与分布差异，进而允许仅使用轻量级参数微调（LoRA）来训练 VLA，避免对 VLM 主干的剧烈改动，从而防止灾难性遗忘。
- **方法名称**：VLM2VLA
- **关键技术细节**：
  - **动作的语言化表示**：将原本为连续向量（如关节角度、末端执行器位姿）的低层动作映射或转换为自然语言令牌。例如，“向前移动 5 厘米，左转 10 度”用自然语言描述。这样，动作序列就变成了类似文本生成的预测任务，与 VLM 预训练时处理文本的形式完全对齐。
  - **参数高效微调**：由于输入输出都统一到语言空间，可以直接使用 Low‑Rank Adaptation (LoRA) 对 VLM 进行微调。LoRA 仅在原模型的权重矩阵旁插入低秩分解矩阵进行学习，原 VLM 的绝大部分参数保持冻结，从而最大限度地保留预训练知识。
  - **训练流程**：VLM 以语言描述的观测（如图像 tokens + 文本指令）作为输入，以语言描述的动作作为输出，通过标准的自回归语言建模目标进行微调。整个过程不需要额外的互联网规模数据的联合训练，也不需要改动网络结构。

## 3. 实验设计

- **评估维度与基准**：
  - **VQA 研究**：通过广泛的视觉问答测试，系统评估微调后模型在基础语义推理、常识理解和多模态理解上的保持程度。
  - **真实世界机器人实验**：设计超过 800 次真实机器人操作实验，重点考察模型在新任务上的零样本泛化能力，包括需要开放世界语义推理和遵循多语言指令的任务。
- **对比方法**（根据摘要可合理推断）：
  - 应与直接微调 VLM 输出连续动作的传统 VLA 范式（无语言化动作）进行对比，以暴露灾难性遗忘现象；
  - 可能与使用全参数微调或以其他方式缓解遗忘的基线方法进行比较（如多任务学习、数据重放等），但摘要未具体列出。
- **任务场景**：涵盖需要语义理解的开放世界任务，以及多语言指令遵循任务，体现对预训练能力的保留。

## 4. 资源与算力

- 论文提供的摘要及元数据中**未明确说明**所使用的 GPU 型号、数量、训练时长等算力细节。仅从“使用 LoRA 进行微调”可推断训练开销应远低于全参数微调或从零训练大型 VLM，但具体数字需查阅正文。

## 5. 实验数量与充分性

- **实验规模**：
  - 定性评估部分：进行了“广泛的”视觉问答研究，暗示覆盖多类型、多数据集的 VQA 测评。
  - 机器人实验：明确提及超过 800 次真实世界实验，样本量较大。
- **实验充分性**：
  - 从摘要看，实验设计兼顾了基础能力保持（VQA）和下游策略泛化（机器人零样本任务），维度较为全面。
  - 未给出具体的消融实验细节（如对比有无动作语言化的效果、不同表示粒度的语言映射等），但推断正文中应包含相关分析。
  - 总体看，实验数量可观，且使用了真实机器人平台而非仅有仿真，增强了结论的说服力。对比公平性取决于是否在相同数据和评估设定下比较各方法，摘要尚未透露细节。

## 6. 论文的主要结论与发现

- VLM2VLA 通过将动作表示为语言，能够有效对齐预训练与微调数据的分布，从而几乎完全避免微调过程中的灾难性遗忘。
- 该方法使得仅用 LoRA 训练的 VLA 模型可以完整保留原始 VLM 的语义理解、常识推理和指令遵循能力。
- 在真实机器人实验中，由此训练的 VLA 表现出对新任务的强零样本泛化能力，包括那些需要开放世界语义推理和处理多语言指令的任务，这些任务传统微调方法往往难以胜任。
- 整体表明，在数据层面统一表示是训练通用机器人策略的一条可行且高效的路径，且无需昂贵的联合预训练。

## 7. 优点

- **方法简洁且本质**：从数据分布匹配这一根本原因切入，而非仅在算法层面打补丁，思想清晰，解释性强。
- **保留基础能力出色**：通过动作语言化和只用 LoRA，几乎不牺牲 VLM 的原有能力，这在实际部署中很有价值，因为机器人需要同时理解复杂环境并执行动作。
- **训练高效**：无需全参数微调或混合大规模预训练数据，LoRA 使训练成本和存储开销大幅降低，也更容易复现和扩展。
- **泛化能力强**：在零样本语义推理和多语言指令遵循等具有挑战性的场景下展现优越性能，验证了保留通用知识对机器人泛化的重要性。
- **实验扎实**：结合了系统评估（VQA）和大量真实机器人实验（>800 次），覆盖分析型与应用型指标。

## 8. 不足与局限

- **动作表示的表达力限制**：将连续、高精度的动作压缩为自然语言可能丢失细粒度控制信息，对于需要高频、高精度控制的任务（如灵巧操作、动态运动），语言表示可能不够精确或效率低下。
- **语言映射的工程依赖性**：需要设计自然语言动作的描述模板或映射函数，这可能引入人为偏差，且在不同机器人平台或动作空间之间的迁移性未知。
- **仅展示零样本泛化**：虽然零样本泛化是重点，但未提及经过少量适配样本后模型能否进一步提升，缺少对样本效率的讨论。
- **算力信息缺失**：摘要未提供训练所需算力和时间，无法评估实际资源门槛，尽管 LoRA 通常轻量，但基座 VLM 的前向传播和对齐过程仍可能有耗时。
- **对比不全面**：摘要未明确说明与哪些最新的 VLA 基线（如 RT‑1、RT‑2、Octo 等）进行系统对比，无法判断在标准 VLA 基准上的绝对性能水平。
- **安全性考虑缺失**：将动作转为语言并由生成模型产生，可能引入不可控的幻觉风险，论文未讨论此类安全局限。

（完）
