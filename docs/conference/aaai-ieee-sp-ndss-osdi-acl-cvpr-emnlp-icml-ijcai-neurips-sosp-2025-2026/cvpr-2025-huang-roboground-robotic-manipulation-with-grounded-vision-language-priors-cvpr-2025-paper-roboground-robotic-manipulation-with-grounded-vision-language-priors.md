---
title: "RoboGround: Robotic Manipulation with Grounded Vision-Language Priors"
title_zh: RoboGround：基于视觉-语言先验的机器人操作
authors: "Huang, Haifeng, Chen, Xinyi, Chen, Yilun, Li, Hao, Han, Xiaoshen, Wang, Zehan, Wang, Tai, Pang, Jiangmiao, Zhao, Zhou"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf"
tags: ["query:analysis"]
score: 5.0
evidence: 探索将接地掩码作为生成机器人动作的有效中间表示
tldr: 本文探索将视觉-语言模型生成的接地掩码作为机器人操作策略的中间表示，以提供空间引导并利用大规模预训练知识。该接地感知策略提升了在物体操作任务上的泛化性，展示了一种利用视觉语言先验改进动作生成的路径，对动作中高级表示的学习具有启发意义。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 817, \"height\": 986, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1710, \"height\": 957, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1709, \"height\": 684, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 867, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1807, \"height\": 326, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 871, \"height\": 324, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 872, \"height\": 293, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 870, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-roboground-robotic-manipulation-with-grounded-vision-language-priors-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 699, \"height\": 222, \"label\": \"Table\"}]"
motivation: 机器人操作策略需要高效中间表示来提升泛化性。
method: 利用预训练视觉-语言模型的接地掩码作为中间表示引导策略。
result: 接地感知策略在物体操作任务上展现出良好泛化能力。
conclusion: 接地掩码是一种简单有效的中间表示，可显著提高策略泛化性。
---

## Abstract
Recent advancements in robotic manipulation have highlighted the potential of intermediate representations for improving policy generalization. In this work, we explore grounding masks as an effective intermediate representation, balancing two key advantages: (1) effective spatial guidance that specifies target objects and placement areas while also conveying information about object shape and size, and (2) broad generalization potential driven by large-scale vision-language models pretrained on diverse grounding datasets. We introduce \method, a grounding-aware robotic manipulation policy that leverages grounding masks as an intermediate representation to guide policy networks in object manipulation tasks. To further explore and enhance generalization, we propose an automated pipeline for generating large-scale, simulated data with a diverse set of objects and instructions. Extensive experiments show the value of our dataset and the effectiveness of grounding masks as intermediate guidance, significantly enhancing the generalization abilities of robot policies.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义
- **研究动机**：机器人操作策略的泛化能力严重受限。现有方法要么依赖大量机器人数据微调（成本高），要么使用太粗糙的语言指令（缺乏空间精度），或采用点流、目标图像等细粒度但资源密集的表示。论文探索了 **接地掩码（grounding masks）** 作为中间表示，平衡两种优势：
  - 有效的空间引导：既指定目标物体和放置区域，又传递形状与尺寸信息。
  - 广阔的泛化潜力：可利用大规模预训练的视觉‑语言模型，便于适应新物体、新场景。
- **核心问题**：如何设计一个以接地掩码为桥梁的机器人策略，使其能从高层面语言指令中提取精准空间信息，并极大地提升操作策略的泛化能力。

## 2. 论文提出的方法论
- **整体框架**：ROBOGROUND 由两大部分构成：
  - **Grounded Vision‑Language Model（VLM）**：基于 GLaMM，接收图像观测与语言指令，输出目标物体和放置区域的像素级二值掩码。
  - **Grounded Policy Network**：接收历史图像、机器人状态和语言指令（连同 VLM 生成的掩码），预测未来的机械臂和夹爪动作。
- **关键技术细节**：
  - **VLM 模块**：
    - 用 CLIP 编码图像，投影后与文本指令一起送入大语言模型（LLM）生成文本输出。
    - 引入 `<SEG>` 令牌，从 LLM 最后一层嵌入中提取与接地相关的特征，通过 SAM 编码器‑解码器结构生成分割掩码：
      \[
      M = D\left(f_s\left(F_{seg}\right), E\left(x_v\right)\right)
      \]
    - 针对操控任务，模型被提示分别输出目标物体掩码 \(M_o\) 和放置区域掩码 \(M_p\)。
  - **策略网络（基于 GR‑1）**：
    - 输入图像与对应掩码 \(M_o\)、\(M_p\) 做通道拼接后，通过线性层回投至 3 通道，再经 ViTMAE 编码得到视觉特征 \(Z_v\)。
    - **Grounded Perceiver**：在标准 Perceiver 的基础上，新增两组可学习的查询令牌 \(Q_o\)（目标物体）和 \(Q_p\)（放置区域）。每次注意层中，根据掩码对补丁特征进行注意力引导（通过 mask fill 操作），保留关键空间信息，最终输出 3 倍于原始查询令牌长度的视觉表征。
    - 历史 \(N\) 步视觉、文本和状态令牌与可学习的动作令牌 `<ACT>` 拼接，经 Transformer 解码器预测下一步动作。
- **训练与推理**：
  - VLM 在自动生成的指令‑跟随数据上微调，结合交叉熵（文本）和 DICE+BCE（分割）损失。
  - 策略网络通过 Smooth‑L1（手臂动作）和 BCE（夹爪）损失联合训练。
  - 推理时，仅在episode开始阶段调用一次 VLM 生成掩码，后续所有步均复用该掩码。

## 3. 实验设计
- **数据集与场景**：
  - 基于 RoboCasa 仿真环境，利用其自动化场景生成能力，构建了一个包含 24K 演示和 **112K 条多样化指令**的新数据集，指令涵盖**外观、空间关系、常识**三类推理。
  - 场景复杂度通过从 176 个类别、3526 个物体中采样干扰物显著提高。
  - 原始 RoboCasa 数据归为“Easy”（简单）任务，用于训练基础技能（开门/关门、按按钮、转杠杆、拧旋钮）。
- **对比基准**：
  - ACT：基于变压器的条件 VAE，无语言输入。
  - BC‑Transformer：经典行为克隆，语言通过 CLIP+FiLM 注入。
  - GR‑1：GPT 风格策略，复现时未使用大规模预训练。
- **评估指标**：
  - Pick‑and‑place：接触率 / 成功率（a / b%）。
  - 其他技能：成功率。
- **测试场景**：
  - 标准测试：Easy、Appearance、Spatial、Common‑sense 四种指令类型。
  - 零样本泛化：未见实例（同类新物体）与未见类别（全新物体类别），每种生成 400 个测试样本。

## 4. 资源与算力
- **训练硬件**：文中提及消融实验使用**8 块 NVIDIA 4090 GPU**，全量数据训练需“数天”完成，未给出更精确的显存、批次大小或完整训练时长。
- **推理速度**：掩码生成可多视图并行处理，每个episode仅需一次 VLM 前向传播。

## 5. 实验数量与充分性
- **主要实验**：
  - 表 1：在 7 种任务（4 种捡放 + 3 种基本技能）上与三个基准方法对比，展示掩码的显著提升。
  - 表 2：两档零样本泛化（实例级 / 类别级），有无掩码的对照，证明掩码在陌生环境下带来约 100% 的相对提升。
- **消融研究**：
  - 训练数据组成（原始 vs. 新数据 + 掩码）→ 表 3。
  - 掩码融入方式（通道拼接 vs. Grounded Perceiver）→ 表 4。
  - 接地表示形式（点、包围盒、掩码，低维 vs. 图像通道）→ 表 5。
  - VLM 微调策略（零样本、仅仿真数据、仿真+原始 VLM 数据）→ 表 6。
- **充分性与公平性**：实验设置统一历史长度、图像视图和尺寸；所有方法在相同数据上训练；消融实验覆盖了关键设计要素，对比公平且结论可靠。

## 6. 论文的主要结论与发现
- 接地掩码作为中间表示，**极大地增强了策略对复杂指令和陌生场景的泛化能力**，在多种挑战性任务中表现一致且大幅超越无掩码方法。
- Grounded Perceiver 能更有效地利用掩码信息，优于简单的通道拼接。
- 提出的数据生成 pipeline 能自动产生大量多样化指令和复杂场景，为评估泛化能力提供了严格基准。
- 微调 VLM 时混合仿真数据与原始接地数据，可以保持模型原有知识并提升指令跟随能力。

## 7. 优点
- **表示新颖且高效**：掩码兼具细粒度空间信息和用大规模预训练基础模型的可迁移性，开销适中。
- **系统设计完整**：从数据生成、VLM 微调、到策略网络融合，形成闭环。
- **泛化验证扎实**：覆盖外观、空间、常识推理以及零样本实例/类别泛化，实验结论可信。
- **Grounded Perceiver**：通过注意力引导机制有效保留关键区域信息，方法简单但效果显著。

## 8. 不足与局限
- **仅在仿真环境验证**：未在真实机器人上测试，迁移性未知。
- **任务类型单一**：主要针对单步 pick‑and‑place，对长序列或动态变化目标（掩码仅初始生成）的场景可能不适用。
- **VLM 性能依赖**：掩码质量直接影响策略，需要在仿真数据上微调，可能损害原有通用接地能力。
- **成功率与接触率存在差距**：模型成功抓取率仍然有限，作者也指出可引入外部抓取预测网络改善。
- **计算资源需求较高**：全量训练需多卡数天，VLM 微调也会增加额外负担。

（完）
