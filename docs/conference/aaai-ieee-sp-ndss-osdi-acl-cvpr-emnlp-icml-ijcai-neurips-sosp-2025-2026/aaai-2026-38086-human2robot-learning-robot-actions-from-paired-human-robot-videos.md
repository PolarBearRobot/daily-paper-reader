---
title: "Human2Robot: Learning Robot Actions from Paired Human-Robot Videos"
title_zh: Human2Robot：从配对的人机视频中学习机器人动作
authors: "Sicheng Xie, Haidong Cao, Zejia Weng, Zhen Xing, Haoran Chen, Shiwei Shen, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38086/42048"
tags: ["query:data"]
score: 10.0
evidence: "通过条件视频生成实现细粒度人-机器人对齐，在精确同步的H&R数据集上学习机器人动作"
tldr: "Human2Robot突破粗粒度对齐限制，将精细的人-机器人对齐视为条件视频生成问题，并构建了精确同步的第三人称数据集H&R。该方法能捕捉逐帧动力学，使机器人从人类演示中学习复杂操作并泛化到新任务。这项工作为人机技能迁移提供了新范式。"
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 746, \"height\": 1079}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 872, \"height\": 260}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1796, \"height\": 1033}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1830, \"height\": 609}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1830, \"height\": 327}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38086/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1105, \"height\": 343}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38086/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 704, \"height\": 328}]"
motivation: 现有人-机器人视频对齐粗糙，仅学习全局特征，忽略细粒度帧级动力学。
method: "提出条件视频生成范式实现精细对齐，并构建同步的H&R数据集。"
result: 在复杂操作和新任务上表现出更好的泛化能力，捕获了细粒度动作。
conclusion: 精细对齐和同步数据集实现了更高效的人机技能迁移。
---

## Abstract
Distilling knowledge from human demonstrations is a promising way for robots to learn and act. Existing methods, which often rely on coarsely-aligned video pairs, are typically constrained to learning global or task-level features. As a result, they tend to neglect the fine-grained frame-level dynamics required for complex manipulation and generalization to novel tasks. We posit that this limitation stems from a vicious circle of inadequate datasets and the methods they inspire. To break this cycle, we propose a paradigm shift that treats fine-grained human-robot alignment as a conditional video generation problem. To this end, we first introduce H&R, a novel third-person dataset containing 2,600 episodes of precisely synchronized human and robot motions, collected using a VR teleoperation system. We then present Human2Robot, a framework designed to leverage this data. Human2Robot employs a Video Prediction Model to learn a rich and implicit representation of robot dynamics by generating robot videos from human input, which in turn guides a decoupled action decoder. Our real-world experiments demonstrate that this approach not only achieves high performance on seen tasks but also exhibits significant one-shot generalization to novel positions, objects, instances, and even new task categories.

---

## 论文详细总结（自动生成）

# 论文详细总结：Human2Robot: Learning Robot Actions from Paired Human-Robot Videos

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：当前机器人从人类演示中学习的方法大多依赖**粗粒度对齐**的人机视频对，仅能提取全局或任务级特征，忽视了复杂操作与泛化所必需的**细粒度帧级动力学**。
- **恶性循环**：数据集缺乏精细标注 → 方法只能学习粗糙对齐 → 方法的发展反过来抑制了精细数据集的构建，导致模型无法真正理解“如何做”而只知“做什么”。
- **整体含义**：本文提出**范式转变**——将精细的人机对齐视为**条件视频生成问题**，通过生成视频迫使模型内化机器人运动动力学，从而打破上述循环，实现从简单任务到全新任务的**一次式泛化**。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：利用**视频预测模型（VPM）**从人类视频直接生成对应的机器人视频，学习隐含的细粒度时空对应，然后利用生成模型的中间特征指导动作解码，实现**解耦的两阶段训练**。
- **H&R数据集构建**：借助VR遥操作系统，通过三点匹配建立人手与机械臂的**统一坐标系**，采集了2600个片段，保证人手与机械臂在第三人称视角下**精确同步**，覆盖4种基本任务和6种长时序任务。
- **第一阶段：视频预测模型 (VPM)**
  - **行为提取器 (Behavior Extractor)**：以卷积网络从人类视频（单帧或片段）提取运动和位置线索。
  - **空间UNet (S‑UNet)**：初始化自Stable Diffusion，提取机器人首帧特征，含有自注意力和与CLIP嵌入的交叉注意力。
  - **时空UNet (ST‑UNet)**：每个块包含空间层（同S‑UNet）+时间层，接收行为提取器特征和噪声潜变量，并融合S‑UNet特征，预测未来机器人帧。
  - **训练策略**：先训练图像生成（预测单帧），再冻结VAE编解码器和CLIP，训练时间层以生成30帧视频。损失为噪声预测MSE \( L_G = \mathbb{E}_{z_{ts},c,\epsilon,ts}\|\epsilon - \epsilon_\theta(z_{ts},c,ts)\|_2^2 \)，其中\(c\)为人类视频和机器人首帧。
- **第二阶段：动作解码**
  - **冻结VPM作为视觉编码器**：对输入人类视频加固定强度噪声（一步正向过程），执行**单步去噪**，取第一个上采样层的输出作为动作先验特征 \(F_{\text{VPM}}\)。
  - **视频聚合（Video Former）**：使用可学习查询Token通过空间－时间注意力将\(F_{\text{VPM}}\)聚合成固定长度的特征 \(F_{\text{VF}}\)。
  - **扩散策略 (Diffusion Policy)**：以\(F_{\text{VF}}\)为条件，通过交叉注意力注入扩散Transformer块，从噪声动作中重建原始动作，损失为 \(L_A = \mathbb{E}_{a_k,F_{\text{VF}},\epsilon,k}\|\epsilon - \epsilon_\phi(a_k,F_{\text{VF}},k)\|_2^2\)。
- **KNN推理增强**：在推理阶段，若无人为提供演示，利用DINOv2和CLIP特征从训练集中检索最相似的机器人首帧，将其对应的人类视频作为条件输入，实现无演示执行。

## 3. 实验设计：数据集/场景，benchmark，对比方法
- **数据集**：自建**H&R数据集**（2600个片段的第三人称同步人机视频）作为训练与评估基准。任务涵盖推拉、拾放、旋转、组合等基本操作和长时序任务。
- **测试维度**：
  - **Seen Tasks**：基本推拉、拾放、旋转。
  - **泛化任务**：外观变化（不同颜色/材质）、位置偏移、新实例（乒乓球、香蕉）、背景干扰、**任务组合**（拉盘后拾块）、**全新任务**（书写字母“H”“R”，训练时仅用无意义乱画数据）。
- **对比方法**：
  - **Diffusion Policy**：语言条件的扩散策略。
  - **XSkill**：自监督人体视频条件策略。
  - **Video Prediction Policy (VPP)**：语言条件+视频预测预训练。
  - **Action Decoder w. Human**：直接用人类视频（ResNet18编码）条件解码动作。
  - **HUMAN2ROBOT w/o Pretrain**：无视频生成预训练。
  - **HUMAN2ROBOT w. KNN**：本文带KNN的完整模型。
- **评估指标**：成功率（每任务20次试验）。

## 4. 资源与算力
- **第一阶段（视频预测模型）**：使用 **4块NVIDIA A100 GPU**，训练耗时 **3天**，在2600个预训练视频上进行。
- **第二阶段（动作解码，基本任务）**：使用 **8块NVIDIA A100 GPU**，训练约 **6小时**。
- **书写任务专项训练**：同样使用 **8块A100 GPU**，训练约 **6小时**，仅使用无意义的乱画数据。

## 5. 实验数量与充分性
- **实验组数**：
  - 多任务成功对比（表1左，4类任务×6种方法）。
  - 泛化能力对比（表1右，6种泛化类型×3种方法）。
  - 消融实验：验证**VPM有效性**（Action Decoder w. Human）、**视频预训练有效性**（w/o Pretrain）。
  - KNN方法效果。
  - 定性可视化（单步去噪与完全去噪结果，图5）。
- **充分性与公平性**：
  - 覆盖从已知任务到强泛化的多维评估，且对比了基于视频预测、自监督、语言条件等不同流派的方法，较为全面。
  - 使用相同的成功次数指标和20次重复实验，公平性基本得到保证，但所有方法均在自建数据集上训练，可能存在**数据集依赖偏差**，但H&R是为精细对齐专门构建，是本文核心贡献之一。

## 6. 论文的主要结论与发现
- **HUMAN2ROBOT在已知任务上达到最高成功率**（平均95%），远超基线（DP 28%，XSkill 53%，VPP 80%）。
- **强大的泛化能力**：在外观变化（100%）、位置偏移（80%）、实例泛化（70%）、背景干扰（80%）、任务组合（50%）和**全新书写任务**（70%）上，只有HUMAN2ROBOT能成功完成任务，而其他基线基本失效。
- **预训练和VPM架构是成功的关键**：未预训练版本几乎不能完成任务，直接用人类视频解码动作的成功率仅23%，证明视频生成过程学习到的人机对齐动力学是不可或缺的运动先验。

## 7. 优点：方法或实验设计上的亮点
- **精准同步的数据集**：H&R是首个精确帧对齐的人-机器人手－臂视频数据集，为细粒度学习提供了宝贵的基础。
- **创新的范式**：将人机对齐转化为生成问题，一举两得获取运动动力学表征。
- **高效的动作先验提取**：仅需单步去噪即可得到富含运动信息的特征，既快速又能屏蔽无关的像素细节，推理效率优于全扩散过程。
- **突出的泛化设计**：证明了从简单的拾放乱画数据可以泛化到书写特定字符等全新任务，体现了“学会如何做”而非“模仿做什么”的核心思想。
- **KNN增强实用性**：对已知任务无需实时人类演示即可执行，提升了系统的部署灵活性。

## 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等
- **任务受限于拾放类**：因遥操作系统的灵巧性限制，无法收集需精密操作的刚体交互数据（如拧螺丝），导致方法仅验证在抓取－放置任务上。
- **环境与动态相对简单**：真实世界测试场景的背景、光照、干扰物变化有限，与真实家庭的非结构化环境仍有一定差距。
- **KNN方法的扩展性**：依赖训练集特征库，当任务数量激增时检索效率和匹配精度可能下降。
- **书写泛化范围窄**：仅测试了两个字母，且训练数据为无规律乱画，能否泛化到更复杂的轨迹（如数字、符号）仍需验证。
- **计算资源需求较高**：虽然推理时单步去噪较快，但第一阶段训练仍需数天和多个A100，普适性受算力约束。
- **对新颖任务的长期稳定性未评估**：组合任务和新任务的成功率（50％‑70%）仍有提升空间，且未报告失败模式分析。

（完）
