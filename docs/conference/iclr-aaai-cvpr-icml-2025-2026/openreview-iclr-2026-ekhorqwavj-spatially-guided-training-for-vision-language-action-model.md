---
title: Spatially Guided Training for Vision-Language-Action Model
title_zh: 空间引导训练的视觉语言动作模型
authors: "Jinhui Ye, Fangjing Wang, Ning Gao, Junqiu Yu, Zhu Yangkun, Bin Wang, Jinyu Zhang, Weiyang Jin, Yanwei Fu, Feng Zheng, Yilun Chen, Jiangmiao Pang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=eKhOrQWAVJ"
tags: ["query:model"]
score: 8.0
evidence: 空间引导训练的VLA模型，利用网络规模和机器人数据
tldr: SP-VLA 解决了大视觉语言模型在具身任务中将指令转化为低层动作的难题，通过空间基础预训练和空间引导动作后训练，将对齐的空间先验注入 VLA 框架。实验显示其在多个机器人操控任务上优于现有方法。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: VLMs在具身任务中难以将指令转换为低层动作。
method: 两步训练：空间基础预训练注入可移植先验，空间引导后训练产生更丰富先验以指导动作。
result: 在多个机器人操控基准上取得领先性能。
conclusion: 空间先验是连接语言指令和机器人控制的桥梁，可有效提升VLA模型。
---

## Abstract
Large vision–language models (VLMs) excel at multimodal understanding but fall short when extended to embodied tasks, where instructions must be transformed into low-level motor actions. We introduce SP-VLA, a dual-system **V**ision–**L**anguage–**A**ction framework that leverages **S**patial **P**riors as a bridge between linguistic instructions and embodiment-specific control. 
introduce SP-VLA aligns action learning with spatial priors through two stages: (i) spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory prediction from both web-scale and robot-specific data, and (ii) spatially guided action post-training, which encourages the model to produce richer spatial priors to guide action generation via spatial prompting.
This design preserves spatial grounding during policy learning and promotes consistent optimization across spatial and action objectives. Empirically, introduce SP-VLA achieves substantial improvements over vanilla VLA, with performance increasing from $66.1{\rightarrow}84.6$ on Google Robot and from $54.7{\rightarrow}73.2$ on WidowX, establishing new state-of-the-art results on SimplerEnv. It also demonstrates stronger generalization to unseen objects and paraphrased instructions, as well as robustness to long-horizon perturbations in real-world settings. These results highlight scalable spatially guided training as a promising direction for robust, generalizable robot learning. We will release code, data, and model checkpoints to support future research.
See more visualization results at the anonymous page: https://sp-vla-anonymous.vercel.app

---

## 论文详细总结（自动生成）

# SP-VLA：空间引导训练的视觉语言动作模型 论文总结

## 1. 核心问题与整体含义
- **研究动机**：大型视觉语言模型（VLMs）在多模态理解任务上表现卓越，但在具身智能（机器人操控）场景中面临严重适应困难，核心瓶颈在于将抽象的语义指令转化为连续、精确的低层电机动作。  
- **整体含义**：本文提出 SP-VLA（**S**patially Guided **V**ision–**L**anguage–**A**ction），将“空间先验”（spatial priors）作为连接语言理解和机器人控制的桥梁，注入空间感知能力以大幅提升 VLA 模型的动作预测和泛化性能。

## 2. 方法论
- **核心思想**：在 VLA 框架中显式建模并利用空间信息（点、包围框、运动轨迹等），通过两阶段训练将对齐的空间先验有机融合到策略学习过程中，使得动作生成受到丰富空间线索的引导。  
- **关键技术细节**：
  - **空间基础预训练（Spatial Grounding Pre-training）**：利用网络规模数据和机器人专属数据，让 VLM 学习可迁移的空间预测能力（点、框、轨迹预测），为后续动作学习植入稳定空间基础。  
  - **空间引导动作后训练（Spatially Guided Action Post-training）**：在策略微调阶段，通过空间提示（spatial prompting）鼓励模型生成更丰富的空间先验，并以此指导动作生成，确保空间目标与动作目标的一致性优化。  
- **算法流程**（文字说明）：两步训练范式：  
  1. 第一阶段：在大规模多源数据上训练 VLM 执行空间定位任务（如指向目标位置、绘制移动路径），获得通用的空间基础；  
  2. 第二阶段：在机器人操控数据上，以空间先验作为中间表征，与动作预测联合优化，使用空间提示引导动作学习，保持空间定位能力不遗忘。

## 3. 实验设计
- **数据集/场景**：
  - **Google Robot** 和 **WidowX** 两个机器人平台的数据（对应不同形态与任务）。  
  - **SimplerEnv** 基准（可能为仿真环境）用于主要性能评测。  
  - 还测试了对未见物体（unseen objects）和改写指令（paraphrased instructions）的泛化能力，以及长时序扰动下的真实世界鲁棒性。  
- **对比方法**：与 vanilla VLA（标准视觉语言动作模型）直接对比，性能从 66.1→84.6（Google Robot）和 54.7→73.2（WidowX）大幅提升；在 SimplerEnv 上取得 state-of-the-art 结果。  
- **benchmark 指标**：主要为任务成功率（success rate），并关注泛化性和鲁棒性。

## 4. 资源与算力
- 摘要及所提供元数据中**未明确说明**使用的 GPU 型号、数量或训练时长。这一点在论文全文中可能有具体说明，但从当前提取的内容中无法获取。

## 5. 实验数量与充分性
- **实验组数**（根据摘要推断）：
  - 两个主要机器人平台（Google Robot, WidowX）上的性能对比实验；  
  - SimplerEnv 上的主流方法对比；  
  - 消融实验（虽未详述，但“空间基础预训练+空间引导后训练”两阶段设计很可能包含消融分析）；  
  - 泛化测试（未见物体、改写指令）和鲁棒性测试（长时序扰动）。  
- **充分性与公平性**：多平台、多任务、多维度评估（性能、泛化、鲁棒），对比基线明确，结果提升显著，实验设计较为完备。但细节需看全文才能判断消融是否全面、对比方法是否覆盖最新 SOTA。

## 6. 主要结论与发现
- 空间先验可作为连接语言指令和低层控制的强效桥梁，显著提升 VLA 模型的操控能力。  
- 提出的两阶段训练（空间预训练 + 空间引导动作微调）能保持空间定位能力，在多个标准平台取得领先性能，并展现出更强的泛化与鲁棒性。  
- 该方向为可扩展、可泛化的机器人学习提供了有前景的技术路线。

## 7. 优点
- **方法创新性**：首次系统性地将空间先验融入 VLA 训练，用双阶段设计解耦空间理解与动作生成，解决 VLM 在具身任务中的适应难题。  
- **实验亮点**：多平台、大规模性能跃升，同时验证了泛化和真实世界鲁棒性，实验结果扎实。  
- **开源承诺**：作者宣布将开源代码、数据和模型，有助于社区复现与后续研究。

## 8. 不足与局限
- **算力与成本信息缺失**：未提供训练所需资源细节，难以评估方法的计算开销和部署可行性。  
- **细节待补充**：方法中空间先验的具体形式、空间提示机制、训练数据集规模与配比等关键实现信息在摘要中未展开，需查阅全文。  
- **潜在偏差风险**：实验场景有限（仅两类机器人平台），复杂交互任务、动态环境、多Agent场景下的表现未知；预训练数据来源与分布未说明，可能影响通用性。  
- **应用限制**：依赖大规模多源数据做空间预训练，对数据获取与标注仍有较高要求，可能限制其在某些特定领域的快速迁移。

（完）
