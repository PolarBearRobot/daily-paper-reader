---
title: "MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training"
title_zh: MimicDreamer：对齐人机演示以实现可扩展 VLA 训练
authors: "Haoyun Li, Ivan Zhang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Zhiqin Yang, Zhentao Zhang, Boyuan Wang, Chaojun Ni, Wenkang Qin, Xinze Chen, Yun Ye, Guan Huang, Zhenbo Song, Xingang Wang"
date: 2025-09-03
pdf: "https://openreview.net/pdf?id=xCAum9gOkj"
tags: ["query:data"]
score: 10.0
evidence: 通过视觉、视角和动作对齐将人类演示转化为机器人可用监督的框架
tldr: MimicDreamer 解决人类演示视频与机器人执行视频之间的域差异问题，通过联合对齐视觉外观、相机视角和动作动态，将低成本的人类演示转换为包含机器人姿态轨迹的监督数据，实现可扩展的 VLA 训练。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 机器人数据昂贵，人类视频存在域差异。
method: 联合对齐视觉、视角和动作，生成机器人可执行轨迹。
result: 实现从人类演示到机器人监督的转换，扩展 VLA 训练数据。
conclusion: 有效弥合人机域差异，为 VLA 提供廉价大规模训练方案。
---

## Abstract
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

---

## 论文详细总结（自动生成）

# MimicDreamer: 对齐人机演示以实现可扩展 VLA 训练

## 1. 核心问题与研究动机
- **核心问题**：视觉‑语言‑动作（VLA）模型的强泛化能力依赖于多样化训练数据，但机器人具身交互数据的采集成本极高。虽然人类演示视频可低成本、规模化地采集，并能有效训练 VLA，却存在明显的**人机域差异**。
- **域差异表现**：
  - 相机视角不稳定（手持拍摄抖动）
  - 人手与机器人手臂的视觉外观差异
  - 运动动力学差异（人手轨迹 vs. 机器人关节指令）
- **研究目标**：将快速、低成本的人类演示转化为机器人可用的监督信号，直接支撑策略训练，从而**桥接上述域鸿沟**。

## 2. 方法论：核心思想与关键技术
MimicDreamer 通过**联合对齐视觉外观、相机视角与动作动态**三大维度，将人类演示视频转换成包含机器人位姿轨迹的监督数据。

### 2.1 视觉对齐：H2R Aligner
- 基于视频扩散模型，将人手操作视频中的运动迁移生成高保真机器人演示视频。
- 消除人手与机器臂的外观差异，输出视觉上一致的机器人视角视频。

### 2.2 视角稳定化：EgoStabilizer
- 利用单应性变换规范化第一人称（egocentric）视频，消除相机抖动。
- 对变换造成的遮挡和畸变进行修复（inpainting），确保画面完整稳定。

### 2.3 动作对齐：人手轨迹到机器人指令的映射
- 将人手运动轨迹映射到机器人操作空间坐标系。
- 使用**带约束的逆运动学求解器**生成可行、低抖动、高精度位姿跟踪的关节指令。

> 整体流程：原始人类 Egocentric 视频 → 视角稳定 → 视觉迁移为机器人视频 → 动作映射为机器人轨迹 → 用于 VLA 训练。

## 3. 实验设计
由于仅提供论文摘要，具体实验细节未能完全获取，现基于已有信息总结：
- **评估任务**：6 个代表性的机器人操作任务（具体任务名称未列出）。
- **训练数据**：
  - 纯合成数据：由 MimicDreamer 从人类视频生成的人机对齐视频。
  - 纯真实机器人数据。
  - 人类合成数据与真实机器人数据的组合。
- **评估方法**：真实机器人上的**少样本执行（few‑shot execution）**，对比平均成功率。
- **对比方法**：摘要中未列出具体基线方法名称，但实验包含“仅用真实机器人数据训练”的模型作为基线。

## 4. 资源与算力
- 论文摘要与元数据中**未提供**任何关于 GPU 型号、数量、训练时长等算力相关的信息。因此无法总结计算资源消耗。

## 5. 实验数量与充分性
- **实验组数**：至少包含以下几类对比：
  - 仅用 MimicDreamer 合成数据训练 vs. 仅用真实数据训练
  - 合成数据 + 真实数据扩展训练的效果
- **消融实验**：摘要未提及针对各对齐模块（视觉、视角、动作）的消融分析，但从方法论完整性推测可能包含。
- **充分性评价**：仅从摘要看，实验展示了在 6 个任务上平均成功率提升 14.7%，且实现纯合成数据的少样本真实操控，具备初步说服力。但缺少与现有域适应/仿真迁移方法的对比、更详细的消融分析及跨具身实验，整体不能断定实验完全充分，需阅读全文确认。

## 6. 主要结论与发现
- MimicDreamer 成功将廉价的人类演示视频转化为机器人可直接使用的监督数据，弥合人机域差异。
- 仅使用合成的人类‑机器人对齐视频训练 VLA 模型，即可在真实机器人上实现少样本执行。
- 在真实机器人数据基础上扩展人类转换数据，相较于纯真实数据训练，在 6 个任务上平均成功率提升 **14.7%**，证实了该方法的可扩展性和有效性。

## 7. 优点
- **三维度联合对齐**：同时解决视觉、视角和动作三个层次的域差异，设计系统而新颖。
- **成本低廉、可扩展**：将人类视频这一廉价的“野生”数据源转化为高质量机器人监督，显著降低数据采集门槛。
- **实用性强**：产出直接为机器人可执行的关节轨迹，端到端支撑 VLA 策略训练，而非仅提供辅助信号。
- **验证全面**：在真实机器人上检验少样本操控能力和数据扩展收益，而非仅做仿真环境测试。

## 8. 不足与局限
- **实验细节不透明**：缺少对比方法、具体任务清单、消融研究及量化指标的标准差，难以评估结果稳健性。
- **泛化边界未知**：仅测试 6 个操作任务，未见对复杂灵巧操作、不同机器人形态或环境泛化的讨论。
- **逆运动学依赖**：动作对齐需给定机器人运动学模型，部署到新机器人时需要重新适配求解器，灵活性受限。
- **潜在的性能上限**：视觉生成质量和稳定化效果必然存在误差，这些误差对下游策略的影响未在摘要中分析。
- **算力成本未披露**：视频扩散模型的训练和推理开销不明，影响对实际落地可行性的判断。

（完）
