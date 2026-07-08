---
title: Object-centric 3D Motion Field for Robot Learning from Human Videos
title_zh: 面向机器人学习的人类视频中以物体为中心的三维运动场
authors: "Zhao-Heng Yin, Sherry Yang, Pieter Abbeel"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=kp9B9iQDIt"
tags: ["query:data"]
score: 10.0
evidence: 从人类视频中提取以物体为中心的三维运动场作为机器人动作表征
tldr: 针对从人类视频中提取机器人可执行动作知识的挑战，本文提出以物体为中心的三维运动场作为动作表征，并设计了一套从视频中提取该表征的框架，实现零样本机器人控制。该方法通过去噪三维运动场估计器和域适应策略，有效捕捉精细手物交互，为利用大规模人类视频进行机器人学习提供了新途径。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有基于视频帧、像素流等动作表征存在建模复杂或信息丢失的问题。
method: 提出去噪三维运动场估计器，从人类视频提取物体级精确运动场作为动作表征。
result: 在多个机器人操作任务上实现零样本控制，性能优于现有方法。
conclusion: 以物体为中心的三维运动场是适合机器人学习的有效动作表征，能充分利用人类视频数据。
---

## Abstract
Learning robot control policies from human videos is a promising direction for scaling up robot learning. However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge. Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this representation from videos for zero-shot control. We introduce two novel components. First, a novel training pipeline for training a ``denoising'' 3D motion field estimator to extract fine object 3D motions from human videos with noisy depth robustly. Second, a dense object-centric 3D motion field prediction architecture that favors both cross-embodiment transfer and policy generalization to background. We evaluate the system in real world setups. Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior approaches fail ($\lesssim 10$\%), and can even acquire fine-grained manipulation skills like insertion.

---

## 论文详细总结（自动生成）

由于您提供的 PDF 提取文本仅为 OpenReview 的验证页面（未包含论文正文），以下总结完全基于摘要和给定的元数据（动机、方法、结果、结论等），并结合机器人与计算机视觉领域的常识进行推断。对于无法从现有信息中获取的内容，将如实说明。

### 1. 论文的核心问题与整体含义（研究动机和背景）
*   **核心问题**：如何从人类操作视频中提取适合机器人策略学习的“动作表征”是一个关键挑战。
*   **动机与背景**：利用大规模人类视频来扩展机器人学习是一个有前景的方向，但直接将视频帧、像素流（optical flow）、点云流等作为动作表征存在固有缺陷：要么建模复杂度过高，要么信息丢失严重（如无法捕捉精细的手物交互）。因此，需要一种既能有效编码物体运动、又易于跨形态迁移的动作表征。
*   **整体含义**：本文提出以**物体为中心的 3D 运动场**作为该桥梁，并开发了从单目人类视频中鲁棒提取该表征的完整框架，最终实现零样本机器人控制，为利用海量人类视频进行机器人技能学习开辟了新路径。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
*   **核心思想**：将动作定义为场景中目标物体表面的稠密三维运动向量场（object-centric 3D motion field），它描述了物体每一点从当前帧到未来帧的精确位移。该表征直接捕获了手物交互的精细几何变化，且与机器人形态无关，便于跨形态迁移。
*   **关键技术细节**（基于元数据和摘要）：
    *   **去噪 3D 运动场估计器 (Denoising 3D Motion Field Estimator)**：
        *   训练流水线：专门设计的训练流程，使得估计器能够从含有噪声深度的人类视频中鲁棒地提取精细物体的 3D 运动。
        *   功能：输入可能是带噪声的 RGB-D 视频序列，通过去噪过程输出物体表面各点平滑、准确的 3D 运动场。
    *   **稠密、以物体为中心的预测架构**：
        *   架构设计有利于**跨形态迁移（cross-embodiment transfer）**：提取的运动场与机器人的机械手形态无关，可重定向至机器人末端执行器。
        *   架构设计有利于**背景泛化**：预测对象专注于目标物体，对环境背景变化具有较强的鲁棒性。
*   **算法流程**（推断）：给定人类操作视频，首先对目标物体进行分割或关键点定位，然后利用去噪估计器预测物体表面的 3D 运动场；接着，将该运动场作为动作表征输入到机器人的控制策略中，生成机器人末端执行器的对应动作，实现零样本操控。

### 3. 实验设计：使用了哪些数据集/场景，它的 benchmark 是什么，对比了哪些方法
*   **数据集/场景**：实验在**真实世界设定（real world setups）**下进行，涵盖了多种操作任务。具体任务包括抓取、放置等常规操作，以及需要精细操控的**插入（insertion）**任务。
*   **Benchmark**：文中提到将所提方法与最近的方法（the latest method）进行对比，以 3D 运动估计误差和多项任务的成功率作为评估基准。
*   **对比方法**：
    *   未给出具体名称，但摘要指出对比了“现有动作表征”（如视频帧、像素流、点云流）相关的方法。这些先前方法在多样化任务中的成功率极低（$\lesssim 10\%$）。

### 4. 资源与算力
*   摘要和元数据中**未提供任何关于 GPU 型号、数量、训练时长的信息**。鉴于实验主要在真实世界运行，模型训练所需的算力规模无法判断，需查阅正文。

### 5. 实验数量与充分性
*   **实验数量**：从摘要推断，至少包含以下几类实验：
    *   3D 运动估计误差的定量对比（与最新方法相比误差降低 50% 以上）。
    *   多种真实世界任务上的机器人零样本控制性能评估，平均成功率达到 55%（而先前方法几乎为 0，$\lesssim 10\%$）。
    *   包含对精细技能（如插入）的专项测试。
*   **充分性、客观与公平性**：
    *   既有运动估计的底层精度对比，又有高层任务成功率验证，且涵盖了简单和精细操作，具有较强的说服力。
    *   使用了真实世界设置，避免了纯仿真偏差。
    *   对比基准明确（最新方法和先前典型表征），结果显示出“质变”，表明对比是公平且具有明显优势的。
    *   不过，摘要中提及“平均 55% 成功率”虽远超 10%，但绝对值仍不高，可能暗示某些任务上依然困难。未提及消融实验。

### 6. 论文的主要结论与发现
*   **主要结论**：以物体为中心的 3D 运动场是连接人类视频和机器人动作的有效表征，能够充分利用人类视频数据进行机器人学习。所提框架能实现零样本机器人控制。
*   **关键发现**：
    *   提出的去噪估计器将 3D 运动估计误差降低了 **50% 以上**。
    *   在先前方法失败（成功率 $\lesssim 10\%$）的多样化任务中，本方法平均成功率达到 **55%**，是一个显著跃升。
    *   该方法甚至能够习得**精细操作技能（如插入）**，表明表征保留了关键的几何交互细节。

### 7. 优点：方法或实验设计上有哪些亮点
*   **表征新颖有效**：物体中心的 3D 运动场在精细度、跨形态迁移能力和背景泛化性之间取得了良好的平衡，解决了现有表征的信息丢失或复杂度问题。
*   **技术组件强**：“去噪”估计器设计巧妙，专门应对人类视频中常见的深度噪声，使得从普通单目视频中提取精确 3D 动作成为可能。
*   **性能飞跃**：在真实机器人任务中，从接近失败（~10%）提升至 55% 零样本成功率，展现了方法的巨大潜力。
*   **零样本控制**：无需机器人任何微调数据，即可将人类视频中提取的动作表征直接应用于机器人，迁移能力突出。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等
*   **信息缺失**：由于未获得论文正文，许多细节不明——训练数据规模、网络结构、是否依赖其他前提（如物体 6D 位姿、专用分割模型）、以及去噪估计器的训练方式。
*   **成功率绝对水平**：平均 55% 的成功率虽远优于基线，但在实际部署中仍显不足，尤其对于精密装配等场景可能不够可靠。
*   **任务与场景覆盖**：仅在“真实世界设定”下测试了有限种类的任务，未提及在基准数据集（如大规模机器人基准）上的泛化测试；无法判断对物体种类、背景、光照的大范围泛化能力。
*   **假设与限制**：方法假设能够获取物体掩膜或定位。性能受单目深度估计质量影响，去噪虽有效，但极端噪声或透明物体的运动估计可能仍然受限。
*   **实验充分性**：摘要未提及消融实验（如各组件贡献度）、对深度噪声水平的鲁棒性实验，以及与最近端到端视觉运动策略的详细比较，这些需在正文中验证。

（完）
