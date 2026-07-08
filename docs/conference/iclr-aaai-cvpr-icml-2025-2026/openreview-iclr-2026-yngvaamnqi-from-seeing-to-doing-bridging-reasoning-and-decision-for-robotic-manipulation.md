---
title: "From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation"
title_zh: 从看到做：桥接机器人操作中的推理与决策
authors: "Yifu Yuan, Haiqin Cui, Yibin Chen, Zibin Dong, Fei Ni, Longxin Kou, Jinyi Liu, Pengyi Li, YAN ZHENG, Jianye HAO"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=yngvAamNQi"
tags: ["query:model"]
score: 9.0
evidence: 具有空间推理能力的VLA模型，实现机器人零样本操作
tldr: FSD 针对 VLA 模型在未知场景中零样本性能不足的问题，提出通过层次化数据构建和自一致性机制生成空间关系推理的中间表示，为机器人操作提供精细指导。实验证明该方法显著提升了未知任务上的泛化能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 当前VLA模型由于数据稀缺和异构，零样本性能不足。
method: 提出层次化数据构建流水线和自一致性机制，生成空间关系推理作为中间表示。
result: 在未知场景和任务上实现了鲁棒的零样本操作性能。
conclusion: 通过空间推理桥接感知和行动，可有效提升机器人泛化能力。
---

## Abstract
Achieving generalization in robotic manipulation remains a critical challenge, particularly for unseen scenarios and novel tasks. Current Vision-Language-Action (VLA) models, while building on top of general Vision-Language Models (VLMs), still fall short of achieving robust zero-shot performance due to the scarcity and heterogeneity prevalent in embodied datasets. To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained guidance for robotic manipulation. Our approach combines a hierarchical data construction pipeline for training with a self-consistency mechanism that aligns spatial coordinates with visual signals. Through extensive experiments, we comprehensively validated FSD’s capabilities in both “seeing” and “doing”, achieving outstanding performance across 8 benchmarks for general spatial reasoning and embodied reference abilities, as well as on our proposed more challenging benchmark VABench. We also verified zero-shot capabilities in robot manipulation, demonstrating significant performance improvements over baseline methods in both SimplerEnv and real robot settings. Experimental results show that FSD achieves 40.6% success rate in SimplerEnv and 72% success rate across 8 real-world tasks, outperforming the strongest baseline by 30%.

---

## 论文详细总结（自动生成）

# 论文总结：《From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation》

## 1. 论文的核心问题与整体含义
- **核心问题**：当前视觉-语言-动作模型（VLA）在面对未知场景和新任务时，零样本泛化能力不足，难以实现鲁棒的机器人操作。
- **原因分析**：具身数据稀缺且异构，导致模型无法从有限的训练样本中习得通用的操作策略。
- **整体含义**：提出将空间关系推理作为感知与动作之间的中间桥梁，使机器人不仅“看见”场景，还能理解物体间的空间关系，从而更好地“执行”操作，显著提升零样本泛化性能。

## 2. 论文提出的方法论
- **核心思想**：让VLA模型在输出动作前先生成关于物体空间关系的中间推理表示，为操作提供精细化的空间指导。
- **关键技术细节**：
  - **层次化数据构建流水线**：自动化生成带有空间关系标注的训练数据，可能涵盖多粒度（物体、部件、场景）关系。
  - **自一致性机制**：将空间坐标与视觉信号对齐，确保推理结果与实际观测一致，可能采用循环验证或跨模态对比。
  - **FSD模型架构**：基于通用视觉-语言模型，新增空间推理头或解码器，输出关系三元组（如 `(A, 在, B 上方)`）后再映射为动作。
- **算法流程（推断）**：
  1. 输入：RGB图像 + 任务指令。
  2. VLM编码视觉与文本特征。
  3. 空间推理模块生成中间表示（物体定位 + 空间关系图）。
  4. 自一致性模块核对坐标与图像，纠正错误推理。
  5. 动作头根据推理结果和原始视觉特征输出末端执行器位姿或轨迹。

## 3. 实验设计
- **数据集/场景**：
  - **通用空间推理与具身指称基准**：8个公开基准，可能包含 CLEVR、VSR、RefCOCO、GQA 等变体，以及具身指称理解任务。
  - **VABench**：自行提出的更具挑战性的基准，侧重未知场景的视觉-动作对齐评估。
  - **仿真操作**：SimplerEnv（桌面级或厨房类仿真环境）。
  - **真实机器人**：8个真实世界操作任务，涉及日常物品抓取、放置、堆叠等。
- **对比方法**：未详细列出，但提及“strongest baseline”，可能包括 RT-2、Octo、OpenVLA 等主流VLA模型。

## 4. 资源与算力
- 摘要和元数据中**未明确提及**GPU型号、数量及训练时长。由于模型基于VLM，推测需多卡A100/H100进行预训练或微调，但缺乏原文确证。

## 5. 实验数量与充分性
- **实验组数**：至少涉及 8 个通用基准 + 1个自建基准 + 2 类物理实验（仿真与真实），合计约 11 组独立实验，加上消融研究（如自一致性机制的有效性）则更多。
- **充分性评价**：
  - **横向覆盖广**：涵盖视觉推理、指称理解、仿真操作、真实操作等多维度。
  - **纵向对比深**：与最强基线比较，并验证零样本能力。
  - **客观性**：使用公开基准和自建挑战基准，评价指标明确（成功率），相对公平。
  - 潜在不足：未说明对照组是否完全复现原始设置，可能存在数据分布差异。

## 6. 论文的主要结论与发现
- FSD通过引入空间推理中间表示，大幅提升了未知场景下的零样本操作成功率。
- SimplerEnv仿真中成功率达40.6%，真实世界8项任务综合成功率达72%，较最强基线提升30个百分点。
- 空间推理能力在“看见”与“执行”两端均带来增益，证明了感知-推理-决策桥接的有效性。

## 7. 优点
- **问题洞察深刻**：抓住VLA模型缺少中间推理机制的痛点。
- **方法简洁有效**：用层次化数据与自一致性机制增强空间推理，不依赖巨量异构数据。
- **实验设计全面**：自建高难度基准，同时进行仿真与真实机器人验证，零样本设置更加贴近实际部署。
- **性能提升显著**：在多个维度取得大幅超越基线的结果。

## 8. 不足与局限
- **资源信息缺失**：未提供训练成本，可复现性受限。
- **任务多样性有限**：真实世界仅8项任务，环境变化（光照、背景、物体类别）的鲁棒性未充分测试。
- **推理范围**：空间关系可能仅限于静态场景，动态交互或遮挡情况下的推理能力未知。
- **自建的VABench细节不明**：摘要未展示其构造方式和难度分布，可能带来评估偏差。
- **基线方法对比粒度**：仅提“最强基线”，未列出全部对比模型，削弱横向比较的完整性。

（完）
