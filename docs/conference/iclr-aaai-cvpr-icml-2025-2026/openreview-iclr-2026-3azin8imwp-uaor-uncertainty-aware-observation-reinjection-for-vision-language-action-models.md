---
title: "UAOR: Uncertainty-aware Observation Reinjection for Vision-Language-Action Models"
title_zh: UAOR：面向视觉-语言-行动模型的不确定性感知观测重注入
authors: "Jiabing Yang, Yixiang Chen, Yuan Xu, Peiyan Li, Xiangnan Wu, Zichen Wen, Bowen Fang, Tao Yu, Zhengbo Zhang, Yingda Li, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang"
date: 2025-09-03
pdf: "https://openreview.net/pdf?id=3azIn8ImwP"
tags: ["query:model"]
score: 8.0
evidence: 通过不确定性感知的记忆重注入，在无需重训练的情况下为VLA整合观测信息。
tldr: 现有VLA方法通过额外观测和模块提升性能但需大量数据与训练，本文提出UAOR，将VLM中的FFN视为键值记忆，在推理时利用不确定性引导的重注入机制融合深度等观测信息，实现无训练的精度提升。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 为VLA增加辅助观测信息往往需要重新采集数据并重新训练，缺乏灵活性。
method: UAOR利用FFN的记忆特性，根据不确定性选择性将观测信息重新注入模型，无需额外训练。
result: 在多个VLA基准上，UAOR无需重训练即提升了任务成功率。
conclusion: UAOR为VLA提供了一种轻量、即插即用的观测融合方法，增强了模型的感知能力。
---

## Abstract
Vision–Language–Action (VLA) models leverage pretrained Vision–Language Models (VLMs) as backbones to map images and instructions to actions, demonstrating remarkable potential for generalizable robotic manipulation. To improve performance, many methods have been proposed to incorporate additional observation cues (e.g., depth maps, point clouds) and auxiliary modules (e.g., object detectors, encoders), enabling more precise and reliable task execution. Although effective, these approaches often require extensive data collection and additional training or fine-tuning, limiting their flexibility and scalability. Inspired by the finding that Feed-Forward Network (FFN) in language models can act as "key-value memory'', we propose **U**ncertainty-**a**ware **O**bservation **R**einjection (**UAOR**), an effective training-free and plug-and-play module for VLA models. Specially, when the current language model layer exhibits high uncertainty, measured by **Action Entropy**, it reinjects the observation information into the next layer's Feed-Forward Network (FFN) in a blending manner. This mechanism helps VLA models look more clearly on the observation during inference, enabling more confident and faithful action generation. Comprehensive simulation and real-world experiments show that our method consistently improves the performance of heterogeneous VLA models across various tasks and embodiments while incurring minimal computational overhead. Notably,  **UAOR** eliminates the need for extra observation cuse or modules, making it a versatile and practical plug-in for existing VLA pipelines.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**  
  视觉‑语言‑行动（VLA）模型以预训练视觉‑语言模型（VLM）为骨干，将图像和指令映射为机器人动作，展现出在通用操作任务中的强大潜力。为提升性能，许多方法引入额外的观测线索（如深度图、点云）或辅助模块（如目标检测器、专用编码器），以增强精细操作和任务可靠性。

- **核心问题**  
  传统方法通常需要**重新采集大规模数据**并对模型进行**再训练或微调**，这严重限制了系统的灵活性与可扩展性。当需要融入新的观测信息时，必须重复这一昂贵过程，难以做到“即插即用”。

- **整体含义**  
  本文提出 **UAOR**（Uncertainty-aware Observation Reinjection），利用 VLM 中前馈网络（FFN）的“键值记忆”特性，在**无需额外训练**的情况下，根据模型在推理时的不确定性，动态将观测信息重新注入模型，从而提升动作预测的准确性和置信度，同时保持极低的计算开销。这为 VLA 模型提供了一种灵活、通用的观测融合方案。

## 2. 论文提出的方法论

- **核心思想**  
  将大语言模型中的 FFN 视为一种可读写的“键值记忆”，在推理时，当模型对当前语言层的预测表现出高不确定性时，**选择性**地将额外的观测信息（无论来自何种传感器）重新注入到下一层 FFN 中，以此迫使模型“更清楚地看到”当前观测，生成更确信的动作。

- **关键技术细节**
  - **不确定性度量**：使用“动作熵”（Action Entropy）来衡量当前语言模型层的不确定性。熵越高，说明模型对下一步动作的分歧越大，越需要外部观测的促进。
  - **观测重注入机制**：当不确定性超过某个阈值时，将观测信息（原始或由额外模块提供的特征）以**混合（blending）方式**写入目标层的 FFN 键值记忆中，实现无训练的信息融合。
  - **即插即用设计**：UAOR 不依赖特定的额外观测线索或辅助模块，也不改变原始 VLA 模型的结构，可作为独立模块嵌入现有推理流程。

- **总体流程**  
  1. 给定输入图像和指令，VLA 模型逐层计算特征。  
  2. 在某一语言层，通过动作熵评估当前状态的不确定性。  
  3. 若不确定性较高，则将预处理的观测信息注入下一层 FFN 的键值记忆中（与其他记忆混合）。  
  4. 模型继续前向计算，直至生成最终动作。  

## 3. 实验设计

- **实验场景与基准**  
  论文进行了 **仿真实验** 和 **真实世界实验**，覆盖了**多种任务和不同具身形态**（如单臂/双臂操作、移动抓取等）。具体的公开基准名称在摘要中未列出，但描述指出在多个 VLA 基准上评估了任务成功率。

- **对比方法**  
  摘要未明确列出对比方法，但从背景可知，主要对比的是**无额外观测融合的原始 VLA 模型**，可能还包含其他需要重训练的观测融合方法（如添加传感器编码器并进行微调的方案）。

- **实验目的**  
  验证 UAOR 在**不重新训练**的前提下，能否一致提升异构 VLA 模型的性能，以及计算开销是否可控。

## 4. 资源与算力

摘要和提供的元数据中**未明确说明**所使用的 GPU 型号、数量、训练/推理时长等算力细节。由于 UAOR 宣称是“无训练”方法，其算力需求主要体现在推理阶段的额外计算（如观测编码和 FFN 注入），文中仅提到“最小计算开销”（minimal computational overhead），但未给出具体数值。

## 5. 实验数量与充分性

- **实验数量**  
  摘要提到“全面的仿真和真实世界实验”，并声称在“多种任务和具身形态”上对“异构 VLA 模型”进行了评估。初步可推断至少包含若干仿真任务和若干真实机器人任务，数量可能较为充分。但未给出具体的实验组数或消融实验的统计。

- **充分性与公平性评价**  
  - **客观性**：采用公开 VLA 模型和基准任务，对比时仅添加 UAOR 模块，排除了额外训练的影响，比较公平。  
  - **充分性风险**：由于摘要仅提供高度概括，无法判断是否覆盖了足够多的任务类型、噪声条件和失败案例。消融实验（如不同注入方式、不同不确定性阈值的影响）是否存在也未可知。若正文中无详细消融和鲁棒性分析，则实验可能不够深入。

## 6. 论文的主要结论与发现

- UAOR 可以有效**利用 FFN 的记忆特性**，在不改变 VLA 模型权重的情况下，通过不确定性感知的观测重注入机制提升动作预测质量。  
- 经仿真和真实世界验证，该方法能**一致地提高不同 VLA 模型**在各类任务中的成功率，且计算开销极低。  
- UAOR 消除了对额外观测模块或重新训练的需求，成为一种**通用、实用的即插即用插件**，适合直接部署到现有 VLA 管线中。

## 7. 优点

- **无训练、即插即用**：完全免除数据收集和再训练成本，极大提升部署灵活性。  
- **机理新颖**：将 FFN 视为键值记忆，利用不确定性引导的注入方式融合多模态信息，提供了新的视角。  
- **通用性强**：不依赖特定的观测源，可适配深度图、点云等多种额外信息，也兼容不同的 VLA 骨干。  
- **计算轻量**：仅需在推理时执行少量额外计算，适合真实机器人实时应用。

## 8. 不足与局限

- **实验覆盖的细节缺失**：摘要未提供具体的任务列表、对比方法名称、成功率数值和统计检验，难以评估其性能增益的实际幅度和显著性。  
- **依赖不确定性度量的有效性**：若动作熵不能准确反映真正需要重注入的时刻（如环境噪声导致熵升高），可能引入误导信息，反而降低性能。鲁棒性尚需验证。  
- **FFN 记忆假设的普适性**：重注入效果可能依赖于特定 VLM 架构的 FFN 设计，对某些非 Transformer 结构或不同变体未必适用。  
- **安全性问题未讨论**：在不确定性度量失效时，盲目注入观测是否会导致灾难性动作？文中未提及失效保护机制。  
- **可解释性不足**：注入时机和方式对最终动作的影响缺乏定量分析，可能带来不可预期的行为。

（完）
