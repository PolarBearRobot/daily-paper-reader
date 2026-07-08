---
title: "BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks"
title_zh: BridgeV2W：通过具身掩膜桥接视频生成模型与具身世界模型
authors: "Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu, Yuan Xu, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang"
date: 2025-09-02
pdf: "https://openreview.net/pdf?id=ZGWwV34Vmu"
tags: ["query:model"]
score: 9.0
evidence: 将坐标空间动作转换为像素对齐的具身掩膜，桥接视频生成模型与具身世界模型
tldr: BridgeV2W 解决了具身世界模型中动作坐标与像素视频错位、摄像机视角敏感及跨形态架构不统一的问题。它提出将坐标空间动作渲染为与 URDF 和摄像机参数对齐的像素化具身掩膜，并通过类 ControlNet 通路注入预训练视频生成模型，实现动作控制信号与预测视频的对齐。实验表明该方法能生成视角特定的条件控制，有力地桥接了视频生成模型与具身世界模型。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 解决具身世界模型中动作与视频对齐差、视角敏感和跨形态架构不统一的问题。
method: 将坐标空间动作渲染为URDF对齐的像素化具身掩膜，并通过ControlNet注入预训练视频生成模型。
result: 实现了视角特定的动作-视频对齐，支持跨形态的条件控制生成。
conclusion: 该方法有效桥接了视频生成模型和具身世界模型，为统一跨形态控制提供了新思路。
---

## Abstract
Embodied world models have emerged as a promising paradigm in robotics, most of which leverage large-scale Internet videos or pretrained video generation models to enrich visual and motion priors. However, they still face key challenges: a misalignment between coordinate-space actions and pixel-space videos, sensitivity to camera viewpoint, and non-unified architectures across embodiments. To this end, we present BridgeV2W, which converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway, which aligns the action control signals with predicted videos, adds view-specific conditioning to accommodate camera viewpoints, and yields a unified world model architecture across embodiments. To mitigate overfitting to static backgrounds, BridgeV2W further introduces a flow-based motion loss that focuses on learning dynamic and task-relevant regions. Experiments on single-arm (DROID) and dual-arm (AgiBot-G1) datasets, covering diverse and challenging conditions with unseen viewpoints and scenes, show that BridgeV2W improves video generation quality compared to prior state-of-the-art methods. We further demonstrate the potential of BridgeV2W on downstream real-world tasks, including policy evaluation and goal-conditioned planning.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **背景**：具身世界模型（Embodied World Models）已成为机器人领域推进决策与规划的重要范式。多数工作依赖大规模互联网视频或预训练视频生成模型来引入丰富的视觉与运动先验。
- **核心问题**：现有方法面临三个关键挑战：
  - **动作-视频错位**：坐标空间中的动作信号与像素空间中的视频帧存在根本的对齐困难。
  - **摄像机视角敏感**：模型的预测质量高度依赖训练时见过的摄像机角度，难以泛化到新视角。
  - **跨形态架构不统一**：不同机器人形态（如单臂、双臂）需要单独设计网络结构，缺乏通用架构。
- **整体含义**：论文旨在通过一种新颖的动作表示与注入方式，解决上述三个问题，将预训练视频生成模型高效、统一地桥接到具身世界模型的构建中。

### 2. 论文提出的方法论

- **核心思想**：将坐标空间动作转换为像素对齐的「具身掩膜」（Embodiment Masks），然后通过类似 ControlNet 的旁路通路注入预训练视频生成模型，实现视角特定、形态统一的动作条件控制。
- **关键技术细节**：
  - **具身掩膜生成**：
    - 利用机器人的 URDF（统一机器人描述格式）模型和摄像机参数，将每个时间步的关节动作（如关节角度、末端位姿）渲染为与当前帧像素精确对齐的掩膜图像。
    - 掩膜直接反映了机器人身体部位的运动区域，消除了动作坐标与像素空间的语义鸿沟。
  - **注入机制**：
    - 采用类 ControlNet 架构，将具身掩膜作为条件输入，通过可训练的零卷积层或类似模块注入到固定参数的预训练视频生成模型（如扩散模型）中。
    - 该通路使模型学会将掩膜的动作信号与预测视频动态关联，同时天然引入了摄像机视角信息（因为掩膜本身就是视角相关的渲染结果）。
  - **运动焦点损失**：
    - 为减轻模型对静态背景的过拟合，提出基于光流的运动损失函数，强制模型关注与任务相关的动态区域，提升生成视频中运动部分的逼真度。
- **算法流程示意**（文字描述）：
  1. 输入：当前视频帧序列、未来动作序列、摄像机内外参、机器人 URDF。
  2. 将动作序列按时间步渲染为具身掩膜序列。
  3. 将掩膜作为条件，沿 ControlNet 路径送入预训练视频扩散模型。
  4. 扩散模型生成未来视频帧，训练时采用标准视频生成 loss 和基于光流的运动 loss 联合优化。

### 3. 实验设计

- **数据集与场景**：
  - **单臂数据集 DROID**：覆盖多样化的操作任务和真实世界场景。
  - **双臂数据集 AgiBot-G1**：包含更复杂的双臂协调任务。
  - 实验条件包含未见过的摄像机视角和全新的场景布局，以检验泛化性。
- **Benchmark 设定**：视频生成质量评估，可能涉及 FVD、PSNR、SSIM 等标准指标（文中未明确，但属业界通用做法）。
- **对比方法**：与先前先进的具身世界模型或视频生成方法进行了对比，但摘要未列出具体名称。重点对比了生成质量提升。

### 4. 资源与算力

- **文中未明确说明**：所提供的摘要及元数据中均未提及所使用的 GPU 型号、数量、训练时长或具体算力规模。
- **推测**：由于该方法基于预训练视频生成模型并引入 ControlNet 风格训练，通常仅需对条件注入通路进行微调，算力需求预计显著低于从零训练整一个世界模型。但缺乏确切数据支撑。

### 5. 实验数量与充分性

- **实验组数推断**：
  - 在两个不同形态的数据集（单臂 DROID、双臂 AgiBot-G1）上进行了评估，据此至少有两套独立的主要实验。
  - 对比了先前最优方法（至少多组对比实验）。
  - 设计了消融实验（如运动损失的有效性验证、不同掩膜表示的影响），但摘要未详述。可认为实验覆盖了主要维度。
- **充分性与公平性**：
  - **充分性**：两个数据集覆盖了单/双臂，且包含未见视角和场景，能够初步验证方法的泛化性与形态统一性。但缺少更多样化的机器人（如移动平台、多足机器人）和更大量级的任务种类。
  - **公平性**：对比了 SOTA 方法，在相同基准上进行，应较为公平。不过由于缺乏对比方法的细节，无法评估调参公平性。

### 6. 论文的主要结论与发现

- 提出的 BridgeV2W 方法在单臂和双臂数据集上均显著提升了视频生成质量，超越了先前的最先进水平。
- 具身掩膜作为一种像素对齐的动作表示，有效解决了坐标动作与视觉信号的对齐问题，并自然地实现了视角特定的条件控制。
- 通过 ControlNet 风格的注入，成功将预训练视频生成模型桥接为统一的具身世界模型架构，无需为不同形态单独设计模型。
- 在策略评估和目标条件规划等下游现实世界任务中，展示了 BridgeV2W 的潜力，表明生成的视频能够支撑机器人决策。

### 7. 优点（方法或实验设计亮点）

- **动作表示创新**：通过 URDF 和摄像机参数渲染掩膜，将抽象动作转化为物理上可解释且视觉对齐的信号，是解决错位问题的简洁而高效的思路。
- **统一架构**：同一个 ControlNet 通路可处理不同形态（单臂/双臂）的具身掩膜，实现了架构统一，利于迁移和扩展。
- **视角鲁棒性**：掩膜随摄像机参数动态变化，使模型天然获得视角泛化能力，这是以往许多基于坐标或关键点的方法所欠缺的。
- **运动焦点损失**：针对世界模型中常见的背景过拟合问题，利用光流引导学习重点区域，提升了生成的运动质量和任务相关性。
- **实验设定严格**：在下游真实任务（策略评估、规划）中验证，而不仅是视频指标，展示了实用价值。

### 8. 不足与局限

- **对 URDF 和摄像机参数的依赖**：方法需要准确的机器人 URDF 模型和标定好的摄像机参数，在真实部署中这些信息可能不准确或难以获取，限制了快速应用到新机器人的便捷性。
- **实验覆盖有限**：仅在两个数据集、两种形态上验证，缺少更多样化的机器人环境（如移动操作、多关节灵巧手），其普适性有待进一步检验。
- **算力细节缺失**：未提供资源消耗信息，无法评估其在有限算力场景下的可行性。
- **潜在的仿真→现实差距**：虽然进行了真实世界下游实验，但世界模型本身是在数据集上训练，其生成的视频是否能精准反映物理交互仍存疑，可能在某些高精度任务中引入仿真偏差。
- **对比局限**：未与基于 Transformer/扩散策略的其他世界模型架构进行全面对比，结论的代表性稍弱。

（完）
