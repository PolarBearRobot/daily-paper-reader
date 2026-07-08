---
title: "VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation"
title_zh: VITA-VLA：通过行动专家蒸馏高效教导视觉-语言模型行动
authors: "Shaoqi Dong, Chaoyou Fu, Haihan Gao, YiFan Zhang, Chi Yan, Chu Wu, Xiaoyu Liu, Yunhang Shen, Jing Huo, Deqiang Jiang, Haoyu Cao, Yang Gao, Xing Sun, Ran He, Caifeng Shan"
date: 2025-09-05
pdf: "https://openreview.net/pdf?id=dIqJaNbHmP"
tags: ["query:model"]
score: 9.0
evidence: 通过行动专家蒸馏高效训练视觉-语言-动作模型，用于机器人操作
tldr: 针对端到端训练VLA模型成本高的问题，提出VITA-VLA框架，从预训练小动作模型蒸馏知识，仅添加行动令牌和状态编码器即赋予VLM行动能力。实验表明该方法能以更低数据和计算成本实现有竞争力的泛化和鲁棒性，为高效构建VLA提供了新路径。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: VLA端到端训练需要大量数据和计算，成本高昂。
method: 提出蒸馏框架，保留VLM结构，仅添加行动令牌和状态编码器，从预训练小动作模型迁移行动知识。
result: 以较低数据量和计算量实现与端到端训练相当的泛化性能。
conclusion: 蒸馏是高效训练VLA的有效途径，降低了机器人学习大模型的门槛。
---

## Abstract
Vision-Language Action (VLA) models significantly advance robotic manipulation by leveraging the strong perception capabilities of pretrained vision-language models (VLMs). By integrating action modules into these pretrained models, VLA methods exhibit improved generalization and robustness. However, training them end-to-end is costly, as modeling action distributions typically requires massive datasets and heavy computation. In this work, we propose a simple yet effective distillation-based framework that equips VLMs with action-execution capability by transferring knowledge from pretrained small action models. Our architecture retains the original VLM structure, adding only an action token and a state encoder to incorporate physical inputs, as illustrated in Figure 1. To distill action knowledge, we adopt a two-stage training strategy. First, we perform lightweight alignment by mapping VLM hidden states into the action space of the small action model, enabling effective reuse of its pretrained action decoder and avoiding expensive end-to-end pretraining. This also facilitates better transfer of action modeling capabilities to the VLM. Second, we selectively fine-tune the language model, state encoder, and action modules, enabling the system to integrate multimodal inputs with precise action generation. Specifically, the action token provides the VLM with a direct handle for predicting future actions, while the state encoder allows the model to incorporate robot dynamics not captured by vision alone (see Figure 2). This design yields substantial efficiency gains over training large VLA models from scratch. Compared with previous state-of-the-art methods, our method achieves 97.3\% average success rate on LIBERO (11.8\% improvement), 93.5\% on LIBERO-LONG (24.5\% improvement), 92.5\% first task success rate on CALVIN ABC-D (4.1\% improvement). In real-world experiments across five manipulation tasks, our method consistently outperforms the teacher model Seer, achieving 82.0\% average success rate (17\% improvement). These results demonstrate that action distillation effectively enables VLMs to generate precise, executable actions while substantially reducing training costs.

---

## 论文详细总结（自动生成）

# VITA-VLA：通过行动专家蒸馏高效教导视觉-语言模型行动

## 1. 论文的核心问题与整体含义
- **研究动机**：视觉‑语言‑行动（VLA）模型通过将预训练视觉‑语言模型（VLM）与行动模块结合，显著提升了机器人操作的泛化性和鲁棒性。然而，端到端训练VLA模型需要海量数据和巨大算力，成本高昂，限制了其广泛应用。
- **整体含义**：作者提出一种基于蒸馏的高效训练框架，从预训练的小型行动模型中迁移知识，使VLM快速获得行动执行能力，在保持竞争性性能的同时大幅降低训练数据和计算开销，为低成本构建VLA系统提供了新路径。

## 2. 方法论
- **核心思想**：**VITA‑VLA** 保留原有VLM结构，仅额外引入一个行动令牌（action token）和一个状态编码器（state encoder），将物理输入（如机器人状态）融入模型。行动知识通过两阶段训练从预训练的“教师”小行动模型蒸馏而来。
- **关键技术细节**：
  - **第一阶段（轻量对齐）**：将VLM的隐状态映射到小行动模型的行动空间，使VLM能直接复用教师模型预训练的行动解码器，避免昂贵的端到端预训练，并促进行动建模能力迁移。
  - **第二阶段（选择性微调）**：只对语言模型、状态编码器和行动相关模块进行微调，让系统融合多模态输入并生成精确动作。行动令牌为VLM提供预测未来动作的直接“句柄”，状态编码器则引入视觉无法捕获的机器人本体状态。
- **算法流程（文字说明）**：输入包括视觉和机器人状态 → 状态编码器生成状态嵌入 → VLM结合状态嵌入与行动令牌预测下一动作的隐表示 → 该隐表示通过蒸馏损失与教师模型的行动空间对齐，最终由教师解码器输出可执行动作。

## 3. 实验设计
- **数据集与场景**：
  - **LIBERO**：标准机器人操作基准，评估单任务成功率。
  - **LIBERO‑LONG**：长期任务基准，评估多步任务完成能力。
  - **CALVIN ABC‑D**：聚焦 ABC→D 的泛化任务，考察首任务成功率。
  - **真实世界实验**：5项操纵任务，验证 sim‑to‑real 转移。
- **对比方法**：与先前最先进（SOTA）方法对比，同时明确与教师模型 **Seer** 对比，展示蒸馏之后学生模型超过教师。
- **评价指标**：平均成功率和首任务成功率。

## 4. 资源与算力
- 论文摘要与提供的元数据中**未明确说明**所使用的GPU型号、数量或训练时长。仅强调方法相比端到端训练“显著提升效率”（efficiency gains），但未给出具体算力指标。这可能意味着正文中有更详细的算力对比，但本总结依据的信息不足以提取相关数据。

## 5. 实验数量与充分性
- **实验组概览**：
  - 至少包含4个独立的测试场景（LIBERO、LIBERO‑LONG、CALVIN、真实世界）。
  - 每个场景下与SOTA及教师模型Seer对比，并给出绝对和相对提升。
  - 摘要未提及消融实验，但元数据中“method”的描述暗示有两阶段训练设计，可能正文有对蒸馏策略、模块保留的消融分析。
- **充分性与公平性**：
  - 多数据集、多任务的覆盖较为全面，且有真实世界验证，增强了结论的可信度。
  - 对比基准包括教师模型与先前SOTA，基线选择合理，但对比方法的具体名称未在摘要列出，无法完全确认是否覆盖了同期最强工作。
  - 从现有描述看，实验设计较为客观、公平，蒸馏成本显著低于端到端训练的目标通过成功率提升间接体现。

## 6. 主要结论与发现
- **性能提升**：VITA‑VLA在LIBERO上平均成功率达97.3%（较基线提升11.8%），LIBERO‑LONG达93.5%（提升24.5%），CALVIN ABC‑D首任务成功率92.5%（提升4.1%），真实世界任务82.0%（提升17%）。
- **效率优势**：通过蒸馏，从预训练小模型获取行动能力，显著减少了训练数据和计算成本，且学生模型可超越教师模型。
- **有效性验证**：显示行动蒸馏是一种高效教导VLM生成精确、可执行动作的可行方案，为机器人学习大模型的低成本构建提供了实证支撑。

## 7. 优点
- **结构精简**：仅增加少量模块（行动令牌、状态编码器），不破坏原有VLM架构，实现轻量化扩展。
- **训练高效**：两阶段蒸馏策略复用现成的行动头，避免了从头预训练VLA所需的庞大数据和算力。
- **性能优异**：在多个基准上大幅超越SOTA，并优于教师模型，说明蒸馏过程能有效继承并提升行动能力。
- **实验扎实**：涵盖模拟长周期任务、泛化任务和真实机器人操作，验证了方法的鲁棒性和实用性。

## 8. 不足与局限
- **细节缺失**：由于仅基于摘要和元数据，缺乏对方法局限性的直接陈述。可能的局限包括：
  - 对教师模型的依赖：方法依赖于一个预训练良好的小型行动模型，若教师性能差则蒸馏效果可能受限。
  - 微调阶段可能仍然需要一定规模的数据，虽然降低了整体成本，但未给出数据量的具体比较。
  - 复杂操作的泛化边界：真实世界只测试了5个任务，更加多样和动态环境下的能力尚不明确。
  - 未讨论对VLM原有能力（如图像理解、对话）的灾难性遗忘问题。
- **实验覆盖的说明不足**：摘要中未列出所有对比的SOTA方法，其选取是否最全面可能存在偏差风险；未提及失败案例或鲁棒性边界。
- **算力透明度低**：未说明训练所用GPU资源，对读者复现的成本估计不够友好。

（完）
