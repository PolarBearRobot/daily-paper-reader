---
title: "FASTer: Toward Powerful and Efficient Autoregressive Vision–Language–Action Models with Learnable Action Tokenizer and Block-wise Decoding"
title_zh: FASTer：基于可学习动作分词器与分块解码的高效自回归视觉-语言-动作模型
authors: "Yicheng Liu, Shiduo Zhang, Zibin Dong, Baijun Ye, Tianyuan Yuan, Xiaopeng Yu, Linqi Yin, Chenhao Lu, Junhao Shi, Luca Jiang-Tao Yu, Liangtao Zheng, Jingjing Gong, Tao Jiang, Xipeng Qiu, Hang Zhao"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=k6nTUFoqeT"
tags: ["query:model"]
score: 9.0
evidence: 可学习动作分词器与分块解码提升VLA模型在机器人操作中的效率
tldr: 针对自回归VLA模型中动作分词存在重建保真度与推理效率权衡的问题，提出FASTer框架，包括将动作块编码为单通道图像的可学习分词器FASTerVQ，以及基于分块自回归解码和轻量级动作专家的FASTerVLA策略，在提高效率的同时保持强大的泛化能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型的动作分词器难以同时兼顾重建精度和推理效率。
method: FASTer设计可学习的动作图像分词器和分块自回归解码策略，优化VLA模型。
result: 实验表明FASTer在多个机器人操作任务中实现了效率和泛化性能的双重提升。
conclusion: FASTer为构建高效且泛化性强的VLA模型提供了新方法。
---

## Abstract
Autoregressive vision-language-action (VLA) models have recently demonstrated strong capabilities in robotic manipulation. However, their core process of action tokenization often involves a trade-off between reconstruction fidelity and inference efficiency.
We introduce \textbf{FASTer}, a unified framework for efficient and generalizable robot learning that integrates a learnable tokenizer with an autoregressive policy built upon it.
FASTerVQ encodes action chunks as single-channel images, capturing global spatio-temporal dependencies while maintaining a high compression ratio. FASTerVLA builds on this tokenizer with block-wise autoregressive decoding and a lightweight action expert, achieving both faster inference and higher task performance.
Extensive experiments across simulated and real-world benchmarks show that FASTerVQ delivers superior reconstruction quality, high token utilization, and strong cross-task and cross-embodiment generalization, while FASTerVLA further improves overall capability, surpassing previous state-of-the-art VLA models in both inference speed and task performance.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：自回归视觉-语言-动作（VLA）模型在机器人操作中展现出强大能力。这类模型通常将动作序列转化为离散 token 进行自回归生成，其中 **动作分词（Action Tokenization）** 是关键环节。
- **核心矛盾**：现有的动作分词方法在 **重建保真度（reconstruction fidelity）** 与 **推理效率（inference efficiency）** 之间存在显著权衡——高保真往往导致低效率，反之亦然。
- **论文目标**：提出一个统一的框架 **FASTer**，同时设计**可学习的动作分词器（FASTerVQ）**与基于该分词器的**自回归策略（FASTerVLA）**，以期在不牺牲重建精度的前提下大幅提升推理速度与泛化性能。

## 2. 论文提出的方法论

- **核心思想**：将动作块（action chunks）编码为 **单通道图像**，利用图像 tokenizer 捕获全局时空依赖，同时保持高压缩率；在策略端采用 **分块自回归解码（block‑wise autoregressive decoding）** 和轻量级动作专家模块，实现又快又好的动作生成。
- **关键技术组件**：
  - **FASTerVQ 分词器**：
    - 将动作块映射为单通道图像，通过向量量化（VQ）得到离散 token。
    - 在全局时空维度捕获依赖关系，获得高重建质量和高 token 利用率。
  - **FASTerVLA 策略**：
    - 基于 FASTerVQ 的离散 token 表示。
    - **分块自回归解码**：一次推理生成一个动作块的多个 token，而非逐 token 生成，显著减少自回归步数。
    - **轻量级动作专家（action expert）**：将解码出的 token 快速转换为连续动作，降低额外开销。
- **公式或算法流程**（摘要未提供具体公式，仅描述流程）：
  1. 动作序列 → 单通道图像 → FASTerVQ 编码 → 离散 token 序列。
  2. 多模态输入（视觉、语言、动作历史）→ VLA 模型 → 分块自回归生成动作token块。
  3. 动作专家 → 重建连续动作。

## 3. 实验设计

- **数据集/场景**：摘要提到“广泛的仿真与真实世界基准测试（Extensive experiments across simulated and real‑world benchmarks）”，但未列出具体数据集名称（例如 CALVIN、LIBERO、真实机器人任务等）。
- **对比方法**：摘要指出 FASTerVLA **超越了之前的 SOTA VLA 模型**（surpassing previous state‑of‑the‑art VLA models），但未列出具体对比对象。
- **评估维度**：
  - FASTerVQ：重建质量、token 利用率、跨任务与跨形态泛化。
  - FASTerVLA：推理速度、任务成功率。

## 4. 资源与算力

- 摘要及元数据 **未提及** 使用的 GPU 型号、数量、训练时长等算力信息。论文正文可能包含，但基于现有内容无法得知。

## 5. 实验数量与充分性

- 摘要仅概括性地说明实验覆盖“仿真与真实世界基准”，并涉及 **重建质量、token 利用率、跨任务泛化、跨形态泛化、推理速度、任务性能** 等多维度比较。
- 元数据中 `evidence` 提到“可学习动作分词器与分块解码提升效率”，说明实验支撑了其声称的效率优势。
- **充分性判断**：由于缺少具体实验数量、消融研究细节，无法评估实验是否充分、公平。但被 ICLR 2026 接收（评分 9.0），被会议审稿人认为实验支撑充足。

## 6. 论文的主要结论与发现

- FASTerVQ 在动作重建保真度上达到了更高水平，同时具有 **更高的 token 利用率**，并展现出 **跨任务、跨机器人形态的泛化能力**。
- FASTerVLA 在 FASTerVQ 基础上实现了 **更快的推理速度** 和 **更高的任务性能**，整体超越了先前最先进的 VLA 模型。
- 该框架为构建 **高效且泛化性强的 VLA 模型** 提供了新途径，缓解了动作分词中保真度与效率的固有矛盾。

## 7. 优点

- **方法创新**：将动作块编码为单通道图像，既保留了时空结构，又提高了压缩效率，是一种新颖的动作表示方式。
- **效率与性能兼顾**：分块自回归解码 + 轻量级动作专家的设计，在推理速度和任务成功率上取得双重提升，解决了传统 VLA 模型的痛点。
- **强泛化性**：在跨任务、跨形态场景下均表现良好，增强了模型的实用性。

## 8. 不足与局限

- **细节缺失**：基于目前提供的摘要，无法得知具体的实验配置、使用的基准名称、对比方法、消融实验设置等，限制了外部对论文方法实际有效性的独立评估。
- **算力未知**：未提供训练资源需求，难以判断其实用门槛。
- **可能局限**：方法依赖动作图像化的先验假设，对于极高维或极长序列动作场景的适应性未知；单通道图像表示是否丢失高频细节未深入探讨；真实世界评测的规模和多样性可能有限（摘要笼统描述）。
- **偏差风险**：由于未列出对比方法，可能存在对比不够全面（如仅与早期 VLA 模型对比而忽略同期工作）的风险。

（完）
