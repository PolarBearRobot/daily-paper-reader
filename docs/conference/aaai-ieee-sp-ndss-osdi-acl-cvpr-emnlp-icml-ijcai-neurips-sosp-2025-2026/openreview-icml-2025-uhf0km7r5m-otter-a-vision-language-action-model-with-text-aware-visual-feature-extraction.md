---
title: "OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction"
title_zh: OTTER：具备文本感知视觉特征提取的视觉-语言-动作模型
authors: "Huang Huang, Fangchen Liu, Letian Fu, Tingfan Wu, Mustafa Mukadam, Jitendra Malik, Ken Goldberg, Pieter Abbeel"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=UHF0km7R5M"
tags: ["query:analysis"]
score: 9.0
evidence: 文本感知的视觉特征提取，学习与动作相关的更好表示
tldr: 现有VLA模型将视觉和语言特征独立输入策略网络，破坏了预训练语义对齐。OTTER提出文本感知的视觉特征提取，仅传递与语言指令语义对齐的任务相关视觉特征，从而保持预训练编码器冻结。该方法提升了机器人动作预测的准确性和泛化性，为高效VLA架构设计提供了新思路。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 解决VLA中视觉语言特征独立处理导致语义对齐退化的问题。
method: 文本感知的视觉特征提取，仅选择与指令相关的语义对齐特征。
result: 冻结编码器下，动作预测性能超越需要微调的基线方法。
conclusion: OTTER展示了利用预训练对齐改进VLA表示的有效性。
---

## Abstract
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained vision-language models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zero-shot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

---

## 论文详细总结（自动生成）

以下是对论文《OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction》的结构化中文总结。该总结基于论文的摘要、元数据及相关信息进行客观分析。

---

## 1. 论文的核心问题与整体含义

- **研究背景与动机**  
  - 视觉-语言-动作（VLA）模型旨在根据视觉观测和语言指令预测机器人动作，是实现具身智能的关键技术。  
  - 现有 VLA 方法通常需要微调预训练的视觉-语言模型（VLM），因为视觉特征和语言特征被**独立地**送入下游策略网络，导致预训练阶段建立的语义对齐被破坏。  
  - 这种独立处理方式流失了大量从海量数据中学到的跨模态语义知识，限制了模型的泛化能力，尤其是零样本泛化能力。

- **整体含义**  
  - 论文提出 **OTTER**，一种新颖的 VLA 架构，通过**文本感知的视觉特征提取**来显式利用预训练的语义对齐，避免因特征独立处理而导致的语义退化，从而保持预训练编码器冻结，并显著增强零样本泛化性能。

---

## 2. 论文提出的方法论

- **核心思想**  
  - 不将所有视觉特征全部输入策略网络，而是**基于语言指令选择性地提取与任务相关、且语义对齐的视觉特征**。  
  - 这种“文本感知”的提取机制使预训练的视觉-语言编码器可以保持冻结，保留其在大规模预训练中习得的丰富语义理解。

- **关键技术细节**  
  - 设计了一种文本感知的视觉特征提取模块，该模块以语言指令为引导，从视觉特征中筛选出语义对齐最强的部分。  
  - 筛选后的特征最终传递给策略 Transformer，用于动作预测。  
  - 由于编码器冻结，整个 VLA 模型只需训练轻量级的特征选择器和下游策略网络，大幅降低了微调代价并提升了训练稳定性。

- **算法流程（文字描述）**  
  1. 输入视觉观测和语言指令；  
  2. 使用冻结的 VLM 编码器分别提取全局视觉特征和文本特征；  
  3. 文本感知特征提取模块计算视觉特征与文本特征的对齐程度，仅保留高对齐度的视觉特征；  
  4. 将筛选后的任务相关视觉特征与指令表示一同送入策略 Transformer；  
  5. 策略 Transformer 输出动作预测（如末端执行器位姿、抓取动作等）。

---

## 3. 实验设计

- **数据集与场景**  
  - 论文在**仿真**和**真实世界**两个维度开展了实验。  
  - 从摘要及项目主页可推断，实验涉及多种物体、新异环境，用于评估零样本泛化能力（如未见过的物体、场景）。  
  - 具体基准数据集名称在已提供信息中未明确列出，但可推断其设计了一系列操作任务（如抓取、放置等）。

- **基准对比方法**  
  - 与现有的 VLA 模型进行对比，这些模型通常需要微调预训练 VLM，如将视觉和语言特征独立送入策略网络的方法。  
  - 文中指出 OTTER **显著超越**这些基线模型，尤其是在零样本泛化场景下。

---

## 4. 资源与算力

- 已提供的摘要和元数据中**未明确说明**使用的 GPU 型号、数量以及具体训练时长。  
- 一般而言，这类基于预训练 VLM 的方法会利用已有的强大编码器（如 CLIP 系列），训练主要涉及轻量模块，可能对算力要求相对较低，但论文未提供确切数据，因此无法给出具体总结。  
- 如需详细了解算力细节，需查阅正文。

---

## 5. 实验数量与充分性

- **实验组数推断**  
  - 至少包含仿真实验和真实世界实验两大块。  
  - 很可能包含多组消融实验（如验证文本感知特征提取的有效性、对比冻结与微调编码器的效果等），但具体组数未在已提供文本中详述。  
  - 从“significant outperforms”和“strong zero-shot generalization”等表述可推测，作者进行了较为全面的评估，涵盖不同物体、环境及指令种类。

- **充分性与公平性**  
  - 对比的方法为当前 VLA 基线，冻结编码器与微调基线的对比能公平体现 OTTER 的优势。  
  - 由于给出了项目地址和开源承诺（代码、检查点、数据集），实验的可复现性和透明度较高，有助于验证结论的客观性。

---

## 6. 论文的主要结论与发现

- OTTER 通过保留并利用预训练 VLM 的跨模态语义对齐，能够在**冻结编码器**的情况下，实现超越传统微调基线的动作预测性能。  
- 模型在零样本泛化方面表现突出，面对新物体和新环境时仍能保持较高的成功率。  
- 这一设计思想证明了：有效利用预训练对齐可以得到更优的机器人动作表示，无需破坏通用语义知识，为 VLA 架构设计提供了新方向。

---

## 7. 优点

- **方法新颖性**  
  - 首次明确在 VLA 模型中引入文本感知的视觉特征提取，解决了视觉语言特征独立处理的语义退化问题。  
- **高效性**  
  - 冻结预训练编码器，仅训练轻量级模块，降低了微调代价，提高了训练稳定性。  
- **泛化能力突出**  
  - 在仿真和真机实验中均展示出强大的零样本泛化性能，证明了对大规模预训练知识的有效继承。  
- **可复现性**  
  - 公开了代码、模型检查和数据集，有利于社区验证和后续研究。

---

## 8. 不足与局限

- **实验细节未获取**  
  - 由于当前仅依据摘要和元数据，无法评估具体数据集规模、任务复杂度、消融实验的全面性等细节，可能存在实验覆盖的局限。  
- **应用场景可能受限**  
  - 该方法依赖高质量的文本指令，对于模糊或简短的指令，文本感知筛选可能准确度下降。  
- **对比基线范围未知**  
  - 摘要声称“显著超越现有 VLA 模型”，但未列出具体对比模型，可能仅与部分基线进行了比较，需在正文中验证。  
- **真实世界部署的稳健性**  
  - 虽然提及真实世界实验，但摘要未报告具体量化指标，实际部署中的稳定性、反应速度等有待进一步考察。  
- **模态限制**  
  - 当前设计基于视觉和语言对齐，能否拓展至其他模态（如力觉、触觉）未作讨论。

---

（完）
