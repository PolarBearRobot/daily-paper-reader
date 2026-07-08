---
title: "VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding"
title_zh: VLAC：基于成对进展理解的通用动作-评价模型
authors: "Qi Zhang, Shaopeng Zhai, Shengzhe Zhang, Litao Liu, TianyiZhang, Fuxian Huang, Zhang HaoranECNU, Ming Zhou, Jiangmiao Pang"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=PmYX0XiQQ0"
tags: ["query:model"]
score: 9.0
evidence: 融合人类和机器人数据进行动作-评价学习，并理解任务进展
tldr: VLAC 针对机器人在动态环境中缺乏可靠任务进展反馈的问题，提出通用视觉语言动作-评价模型，统一行动生成与任务进度理解，并通过成对进展预测整合人类与机器人数据。实验表明该模型能有效提升长程任务中的适应能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 机器人缺乏可靠的任务进展反馈，难以适应开放动态环境。
method: 提出成对进展理解方法，统一行动生成与进度预测于自回归架构中。
result: 在长程任务中实现了有效的适应和进度感知。
conclusion: 整合人类和机器人数据并引入进展理解可显著提升通用操控能力。
---

## Abstract
Recent advances in Vision-Language-Action (VLA) models have significantly improved robotic perception and manipulation capabilities. However, robots deployed in real-world settings still struggle to adapt in dynamic, open-ended environments due to a lack of reliable task progress feedback and improvement mechanisms. To address these challenges, we propose a generalist Vision Language Action-Critic model, VLAC, which can integrate both human and robot data, and unify action generation and task progress understanding within a single autoregressive architecture. Specifically, we propose a scalable and generalizable pair-wise progress understanding approach to predict the task progress delta between any two images in one visual trajectory, and generate the action based on the first image. The model is trained on large-scale, multi-source human data without action annotations and robot data with action information, while also incorporating general vision-language data yielding world knowledge understanding. Furthermore, we deploy reinforcement learning where VLAC can autonomously evaluate task progress to feedback intrinsic rewards. We evaluated our model's progress understanding across eight datasets and show that it not only generalizes to new tasks and environments but also discriminates success from failure trajectories, e.g., on RoboFAC dataset, it reaches VOC-F1 0.89 for successful versus 0.44 for failed trajectories, providing dependable dense reward signals. Then, we evaluated action generation and real-world reinforcement learning performance on diverse real-world robotic manipulation tasks. Experimental results indicate strong disturbance robustness in VLAC’s action generation, while integrating pairwise progress prediction allows real-world RL to improve success from roughly 30\% to 90\% within 200 episodes.

---

## 论文详细总结（自动生成）

# 论文详细总结：VLAC: A Generalist Action-Critic Model via Pair-wise Progress Understanding

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：机器人在真实动态、开放式环境中部署时，缺乏可靠的任务进展反馈与自我改进机制，导致难以自适应和纠正错误。现有的视觉-语言-动作（VLA）模型虽能提升感知与操控能力，但无法给出任务完成度的细粒度评价，限制了其在长程任务中的鲁棒性。
- **整体含义**：本文提出一个通用视觉语言动作-评价模型（VLAC），将动作生成与任务进度理解统一到单个自回归架构中。通过“成对进展理解”预测任意两帧图像之间的任务进度差，模型不仅能生成动作，还能充当“评价器”，提供内在奖励信号，进而支持强化学习，使机器人从失败中自主学习恢复。

## 2. 论文提出的方法论

- **核心思想**：将动作生成和任务进度理解融合在一个自回归 transformer 中，通过在一段视觉轨迹中任意抽取两个图像对，预测它们之间的任务进度差（progress delta），并基于第一张图像生成动作。这样模型既能“行动”又能“评价”当前状态与目标状态的差距。
- **关键技术细节**：
  - **成对进度预测**：给定同一任务轨迹中的两张图像（观测），模型输出它们之间的进度差异（连续值或离散进度变化）。该方法规模可扩展，无需额外标注，可利用人类视频数据（不含动作标签）提供进度监督。
  - **统一架构**：自回归模型同时输出动作 token 和进度差 token，共享视觉-语言 backbone，实现多任务学习。
  - **多源数据整合**：训练数据包含三类：  
    1. 无动作标注的大规模人类视频数据（提供进度线索）；  
    2. 带有动作信息的机器人数据；  
    3. 通用视觉-语言数据，赋予模型世界知识。
  - **强化学习部署**：将训练好的 VLAC 作为评价器（critic），在真实环境 RL 中自主评估任务进展，提供稠密的内在奖励，支持模型自我进化。
- **公式/算法流程（文字说明）**：
  1. 从一条任务执行轨迹中采样一对图像 `(I_i, I_j)`，并计算真实进度差 `Δp`。
  2. 模型输入 `(I_i, I_j)`，自回归地生成进度预测 token（可量化）和基于 `I_i` 的动作 token。
  3. 损失函数同时优化动作预测（行为克隆）和进度预测（回归或分类）。
  4. RL 阶段：冻结 VLAC 作为 critic，每步给出当前图像与目标图像间的进度预测，转化为内在奖励，策略网络依据此奖励更新。

## 3. 实验设计

- **数据集/场景**：
  - 进度理解评估：在 **8 个数据集**上测试进度理解泛化能力，其中包括 **RoboFAC** 数据集。
  - 动作生成与 RL 评估：在**多种真实世界机器人操控任务**中测试（具体任务未在摘要中列出，应包含长程操作任务）。
- **Benchmark 与对比方法**：
  - 进度理解：在 RoboFAC 上报告了成功轨迹与失败轨迹的 VOC-F1 分数，成功轨迹达到 0.89，失败轨迹为 0.44，以此证明模型能区分任务进展。
  - 动作生成：测试在扰动环境下的鲁棒性，并与 baseline（未提及具体名称）对比。
  - 真实 RL：对比有/无成对进度预测内在奖励的强化学习，从约 30% 成功率提升至 90%（200 episodes）。
- **主要评估指标**：VOC-F1（用于进度预测），任务成功率，扰动鲁棒性。

## 4. 资源与算力

- 摘要及元数据中**未明确说明**使用的 GPU 型号、数量或训练时长。通常此类大规模 VLA 模型训练可能涉及多卡并行，但无确切信息。因此，无法量化算力需求，这是一个缺失点。

## 5. 实验数量与充分性

- **实验数量**：
  - 进度理解的评价覆盖 **8 个数据集**；
  - 动作生成在真实世界多个任务上测试；
  - 消融实验**未在摘要中提及**，但标题提到“成对进展理解”是关键设计，大概率有消融研究（如对比不同进度预测方式、数据混合比例等）；
  - 真实 RL 实验展示了从 30% 到 90% 的显著提升曲线，表明进行了多回合训练测试。
- **充分性与客观性**：
  - 实验维度较广：从静态进度评估到在线 RL 都进行了验证；利用人类和机器人多源数据增强泛化性；同时测试了成功与失败轨迹的区分能力，说明评价信号的可靠性。
  - 客观性：对比了基线（尽管未指名），并在标准数据集上报告数值；RL 设置基于真实机器人，排除了纯仿真的偏差。
  - 不足之处：摘要未提及与专有模型（如 RT-2, Octo 等）的直接比较，也未透露消融细节，实验数量虽已陈述但缺乏详细统计。

## 6. 论文的主要结论与发现

- 通过成对进展预测，VLAC 能够统一动作生成与进度理解，整合人类和机器人数据后，模型在未见过的任务和环境上展现出强大的泛化能力。
- 模型可以有效区分成功与失败轨迹，提供的密集奖励信号在真实 RL 中极具价值，使长程操作任务的成功率从约 30% 大幅提升至 90%，仅需 200 个回合。
- 动作生成部分具有显著抗干扰鲁棒性，证明进展感知有助于模型在动态环境中稳定执行。

## 7. 优点（方法或实验设计亮点）

- **统一框架**：将 Actor 和 Critic 凝练为一个模型，减少额外的评价网络设计，实现端到端的进度感知。
- **数据高效利用**：巧妙利用无动作标签的人类视频来训练进度预测，跨数据源迁移能力强。
- **可扩展的成对比较方法**：任意两张图像的进度差预测范式，免去了对完整顺序标注的依赖，易于扩展。
- **真实 RL 验证**：不仅停留在仿真，直接将模型部署到真实机器人上执行 RL，证明其提供的奖励信号的实际价值，大大提升了任务成功率和样本效率。

## 8. 不足与局限（包括实验覆盖、偏差风险、应用限制等）

- **实验覆盖与对比**：
  - 摘要中未明确列出对比的 SOTA 方法（如 RT 系列、Octo 等），难以量化其相对优势。
  - 真实机器人任务的多样性、复杂度和数量未详述，可能局限于特定场景。
- **偏差风险**：
  - 人类视频数据可能包含领域偏差，若人类操作方式与机器人动作空间差异过大，进度学习可能不准确。
  - 内在奖励的塑造可能存在过估计风险，需进一步分析奖励分布的稳定性。
- **应用限制**：
  - 模型需要成对图像输入，在线部署时可能增加推理延迟；RL 阶段虽冻结 VLAC，但整体系统仍较庞大。
  - 进度定义为可量化的差值，对于高度非线性或需要序列理解的任务，简单差值可能不足以描述进展。
  - 未提及计算资源和训练时间，实际落地成本未知。

（完）
