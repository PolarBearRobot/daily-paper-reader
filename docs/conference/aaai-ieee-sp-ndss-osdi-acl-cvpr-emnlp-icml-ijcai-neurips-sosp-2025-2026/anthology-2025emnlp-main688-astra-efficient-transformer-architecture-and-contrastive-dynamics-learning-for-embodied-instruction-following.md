---
title: "Astra: Efficient Transformer Architecture and Contrastive Dynamics Learning for Embodied Instruction Following"
title_zh: Astra：面向体具体指令跟随的高效Transformer结构与对比动力学学习
authors: "Yueen Ma, Dafeng Chi, Shiguang Wu, Yuecheng Liu, Yuzheng Zhuang, Irwin King"
date: 2025-11-01
pdf: "https://aclanthology.org/2025.emnlp-main.688.pdf"
tags: ["query:model"]
score: 7.0
evidence: 为VLA动作预测设计轨迹注意力与对比动力学学习的Transformer架构。
tldr: 针对现有视觉语言动作模型因果注意力在处理多模态交错序列时次优的问题，Astra提出新型Transformer架构，采用轨迹注意力和可学习动作查询，并引入对比动力学学习目标，在模仿学习任务中高效预测动作并增强环境动态理解，在体具体指令跟随基准上达到先进水平，展现了高效VLA模型设计的价值。
source: EMNLP-2025-Main
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 694, \"height\": 327, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1575, \"height\": 610, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1484, \"height\": 722, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1654, \"height\": 362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1615, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1646, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 811, \"height\": 809, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 590, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1553, \"height\": 707, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 720, \"height\": 440, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 718, \"height\": 211, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 803, \"height\": 1075, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 799, \"height\": 492, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 803, \"height\": 566, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 793, \"height\": 518, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 795, \"height\": 517, \"label\": \"Figure\"}, {\"url\": \"assets/figures/emnlp-2025-main/anthology-2025.emnlp-main.688/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 779, \"height\": 1235, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1477, \"height\": 427, \"label\": \"Table\"}, {\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1465, \"height\": 667, \"label\": \"Table\"}, {\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1664, \"height\": 328, \"label\": \"Table\"}, {\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1480, \"height\": 380, \"label\": \"Table\"}, {\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 811, \"height\": 1408, \"label\": \"Table\"}, {\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1645, \"height\": 328, \"label\": \"Table\"}, {\"url\": \"assets/tables/emnlp-2025-main/anthology-2025.emnlp-main.688/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 723, \"height\": 278, \"label\": \"Table\"}]"
motivation: 现有VLA模型因果注意力在处理多模态交错序列时表现次优。
method: 提出Astra，结合轨迹注意力、可学习动作查询和对比动力学目标。
result: 在体具体指令跟随基准上，Astra达到先进水平，效率与精度俱佳。
conclusion: 专门设计的Transformer注意力机制和辅助目标能有效提升VLA模型性能。
---

## Abstract
Vision-language-action models have gained significant attention for their ability to model multimodal sequences in embodied instruction following tasks. However, most existing models rely on causal attention, which we find suboptimal for processing sequences composed of interleaved segments from different modalities. In this paper, we introduce Astra, a novel Transformer architecture featuring trajectory attention and learnable action queries, designed to efficiently process segmented multimodal trajectories and predict actions for imitation learning. Furthermore, we propose a contrastive dynamics learning objective to enhance the model’s understanding of environment dynamics and multimodal alignment, complementing the primary behavior cloning objective. Through extensive experiments on three large-scale robot manipulation benchmarks, Astra demonstrates substantial performance improvements over previous models.

---

## 论文详细总结（自动生成）

## 1. 论文核心问题与整体含义

*  **研究背景**：视觉‑语言‑动作（VLA）模型在具身指令跟随（Embodied Instruction Following）任务中日益重要，其核心是对多模态序列进行建模以预测机器人动作。
*  **核心问题**：现有VLA模型普遍采用**因果注意力（causal attention）**机制，而论文发现该机制在交错呈现不同模态片段的序列上存在次优表现，未能充分利用模态间的时间与语义结构。
*  **整体含义**：论文致力于重新设计Transformer架构，以更高效的方式处理分段式多模态轨迹，并引入辅助目标增强模型对环境动态的理解，最终在多个机器人操控基准上取得显著性能提升。

## 2. 方法论

### 2.1 核心思想
*   从序列建模的角度出发，专门针对多模态交错轨迹设计注意力模式与查询机制，而非直接沿用标准因果注意力。
*   同时引入对比动力学学习作为辅助目标，推动模型更好地捕捉环境状态转移和跨模态对齐。

### 2.2 关键技术细节

*   **轨迹注意力（Trajectory Attention）**  
    替代传统的因果注意力，使模型能够对分段的多模态轨迹进行更有效的上下文聚合，更自然地处理“观察‑指令‑动作”交替出现的序贯结构。

*   **可学习动作查询（Learnable Action Queries）**  
    在Transformer解码阶段使用一组可学习的动作查询向量，专门用于预测动作序列，避免完全依赖逐步自回归生成所带来的累积误差或冗余计算。

*   **对比动力学学习目标（Contrastive Dynamics Learning）**  
    在行为克隆（Behavior Cloning）主目标之外，引入一个对比学习辅助目标。该目标通过对比正负状态转移样本，鼓励模型学习环境动态变化（状态‑动作‑下一状态的关系），并加强多模态表示的对齐。

*   **算法流程概览**  
    1. 输入经分段后的多模态序列（视觉特征、语言指令、历史动作等）。  
    2. 经轨迹注意力编码器整合跨时间与跨模态信息。  
    3. 可学习动作查询与编码表示交互，生成动作预测。  
    4. 同时计算行为克隆损失和对比动力学损失，联合优化。

## 3. 实验设计

*   **数据集/场景**：在三个大规模机器人操控基准（robot manipulation benchmarks）上评估。元数据中未列出具体名称，推断可能涉及常见的具身指令跟随基准（如ALFRED、Mutex或类似多任务环境）。
*   **对比方法**：与先前表现较强的VLA模型进行对比（具体名称未在元数据中给出）。对比维度主要包括成功率、效率与多模态理解能力。
*   **评价指标**：大概率采用任务成功率、动作预测准确度等模仿学习的常规指标。

## 4. 资源与算力

*   提供的元数据与摘要中**未明确说明**所使用的GPU型号、数量、训练时长等算力细节。  
*   仅在结论中提到Astra兼顾“效率与精度”，暗示相比同类模型可能具有更高的参数或计算效率，但缺乏具体量化信息。

## 5. 实验数量与充分性

*   **实验组数概览**：从元数据中的图表数量（17张图、7张表）可推断进行了大量实验，至少涵盖：
    *   三个主流基准（3组主实验）；
    *   消融实验以验证轨迹注意力、学习动作查询和对比动力学目标各自的效果；
    *   定性分析或可视化（注意力图、表示分布等）。
*   **充分性与公平性**：多基准、多角度的对比与消融设计使得实验较为充分；对比方法采用先前先进模型，指标统一，大体公平。但未看到关于超参调优、随机种子影响的详细说明，这部分信息可能在全文中有所交代。

## 6. 主要结论与发现

*   **架构有效性**：专门为多模态交错序列设计的轨迹注意力和可学习动作查询，在行为克隆中显著优于标准因果注意力。
*   **辅助目标增益**：对比动力学学习目标能有效增强模型对环境动态的理解和跨模态对齐，进一步提升操纵成功率。
*   **综合领先**：Astra 在三个基准上均达到当时先进水平，同时保持了较高的效率，证明了专用Transformer设计和自监督辅助任务在VLA模型中的价值。

## 7. 优点

*   **问题洞察深刻**：从序列结构角度指出因果注意力的不适配，并针对性设计注意力模式，思考角度新颖。
*   **结构创新实用**：轨迹注意力与可学习动作查询的组合，既改善建模能力又可能降低解码计算量，兼顾效果与效率。
*   **辅助目标设计合理**：对比动力学学习直接强化环境动态理解，与主任务形成互补，提升整体泛化性。
*   **实验扎实**：覆盖多个大规模基准，配有丰富消融和可视化，论据较为完整。

## 8. 不足与局限

*   **基准范围未知**：摘要未列出具体基准名称，难以判断场景的多样性和复杂程度（如是否包含真实机器人数据或仅仿真环境）。
*   **算力与训练细节缺失**：未给出资源消耗说明，读者无法评估其实际部署成本和可复现性。
*   **语言指令复杂度**：具身指令跟随任务中对复杂自由形式语言的理解能力是否仍有瓶颈，缺少详细分析。
*   **泛化边界不明**：未提及模型在未见过的任务、物体或环境中的迁移表现，存在分布外鲁棒性的风险。
*   **实验公平性细节**：未说明对比方法是否都使用相同预训练权重或同等规模，可能影响比较的绝对公平性。

（完）
