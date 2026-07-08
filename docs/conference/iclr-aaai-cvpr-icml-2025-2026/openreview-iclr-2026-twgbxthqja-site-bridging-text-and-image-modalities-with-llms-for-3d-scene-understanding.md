---
title: "SITE: BRIDGING TEXT AND IMAGE MODALITIES WITH LLMS FOR 3D SCENE UNDERSTANDING"
title_zh: SITE：用LLM桥接文本与图像模态实现3D场景理解
authors: "Haoyuan Li, Rui Liu, Hehe Fan, Yi Yang"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=TWgBXtHQJA"
tags: ["query:model"]
score: 7.0
evidence: 利用LLMs结合文本和图像编码器实现具身智能体的3D场景理解
tldr: 该工作针对具身智能体理解复杂3D场景的挑战，提出SITE框架，通过Scene2Text模块提取实例级关系，将多视图观测转换为BEV图像，并融合1D文本和2D图像编码器到LLM中，实现一致的3D理解。实验表明该方法能有效解析场景并推理空间关系，为具身智能体的3D空间理解提供了可扩展的路径。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有LLM因缺乏足够3D配对数据难以进行可扩展的3D场景理解，限制具身智能体能力。
method: 设计Scene2Text提取实例关系，将多视图转为BEV图像解释空间关系，并融合1D/2D编码器进行LLM微调。
result: 方法在结构化场景解析和3D理解上表现出色，能有效整合空间信息。
conclusion: SITE为具身智能体提供了一种仅用2D图像和文本即可实现3D场景理解的通用框架，减少了对3D数据的依赖。
---

## Abstract
It is a fundamental challenge for embodied agents to understand and interact with complex 3D scenes. Large language models (LLMs) have demonstrated strong capabilities in text and 2D image understanding. However, existing LLMs with 3D encoders suffer from insufficient paired 3D data for scalable training. In this work, we propose Single-Image and 
Text Encoders (SITE), a general framework using a 1D text encoder and a 2D image encoder for structured scene parsing and 3D scene understanding. Specifically, we i) design Scene2Text module to extract instance-level relations, ii) transform multi-view observations into BEV images for interpreting spatial relations, and iii) fuse such 1D and 2D encoders into LLM fine-tuning for consistent 3D understanding. In addition, we introduce InPlan3D, a long-sequence planning benchmark to further evaluate the embodied reasoning ability. Extensive experiments demonstrate the effectiveness and efficiency of SITE on multiple 3D scene understanding datasets and InPlan3D with less token cost. Code and dataset will be publicly released.

---

## 论文详细总结（自动生成）

# SITE：用LLM桥接文本与图像模态实现3D场景理解 总结

## 1. 核心问题与整体含义
- 具身智能体（embodied agents）理解和交互复杂3D场景是一项根本性挑战。
- 大语言模型（LLMs）已在文本与2D图像理解上展现强大能力，但现有的LLM结合3D编码器的工作受限于配对3D数据不足，无法进行可扩展的训练。
- 本研究提出 SITE（Single-Image and Text Encoders）框架，仅利用1D文本编码器和2D图像编码器，实现结构化场景解析与3D场景理解，从而降低对3D标签数据的依赖。

## 2. 方法论
- **核心思想**：将多视角2D观测转换为鸟瞰图（BEV）图像，并用自然语言描述实例间关系，通过融合文本与图像编码器对LLM进行微调，使模型能推理3D空间关系。
- **关键技术细节**：
  - **Scene2Text 模块**：设计用于提取实例级语义关系，生成结构化的文本描述。
  - **BEV图像转换**：将多个视角的2D观测投影为BEV图像，以直观表达空间布局与位置关系。
  - **融合与微调**：将1D文本编码器（处理场景文本）和2D图像编码器（处理BEV图像）的输出对齐并注入LLM，通过微调实现一致的多模态3D理解。
  - **推理能力基准**：引入 InPlan3D，一个长序列规划基准，用于评估模型在具身推理方面的能力。
- 公式或算法流程未在摘要中详述，整体为模块化流水线：多视图输入 → Scene2Text（文本分支）+ BEV图像生成（图像分支）→ 编码器提取特征 → 融合 → LLM → 3D理解与规划输出。

## 3. 实验设计
- **数据集与场景**：在多个3D场景理解数据集上进行评估（具体数据集名称未在摘要中列出）。
- **Benchmark**：除现有3D场景理解任务外，专门引入 InPlan3D 长序列规划基准，用于衡量具身推理能力。
- **对比方法**：与当前结合3D编码器的LLM方法进行对比（未给出具体方法名称），强调在 token 成本更低的前提下取得更好或可比的性能。

## 4. 资源与算力
- 论文摘要及所提供信息中 **未明确说明** 使用的GPU型号、数量及训练时长。
- 仅提及代码与数据集将开源，未提及计算资源细节。

## 5. 实验数量与充分性
- 提及进行了“广泛实验”（extensive experiments），涵盖多个3D场景理解数据集以及新增的InPlan3D基准，暗示实验维度多样。
- 实验设计包括对比实验、消融研究（通过Scene2Text、BEV转换等模块的引入可推测），并强调了token效率，属于典型的验证范式。
- 由于未见到论文正文，无法判断具体实验组数、统计显著性检验等细节，但摘要传递的信息体现出较充分的验证框架。

## 6. 主要结论与发现
- SITE能有效地对复杂3D场景进行结构化解析，并实现空间关系推理。
- 通过仅使用2D图像和文本编码器，模型可绕过3D数据稀缺的障碍，且Token消耗更低，效率提升。
- 所提框架为具身智能体的3D场景理解提供了一种可扩展的通用路径。

## 7. 优点
- **数据高效**：无需昂贵的3D点云或深度标注，仅依赖2D图像和文本，降低了数据门槛。
- **多模态融合简洁有效**：将1D文本关系描述与2D BEV图像统一到LLM，使空间推理更直观，同时保留语言模型的推理能力。
- **任务定制度高**：设计了专门的场景文本生成模块（Scene2Text）和具身规划基准（InPlan3D），使方法针对性增强。
- **计算经济**：声称在Token成本上更有优势。

## 8. 不足与局限
- 摘要未提及任何局限性，根据方法可推断：
  - **依赖多视图与相机位姿**：BEV转换需要精确的多视图几何，可能受实际传感器噪声影响。
  - **文本描述能力边界**：Scene2Text模块的实例关系提取可能存在漏检或误判，影响最终理解。
  - **动态环境未覆盖**：文中强调3D场景理解，但未提及动态变化下的鲁棒性。
  - **实验细节隐蔽**：没有提供对比方法列表、数据集规模、量化指标及消融分析的数值，无法客观判断其宣称效果的可靠性。
- 若后续正文无详细讨论，则透明性存在局限。

---
（完）
