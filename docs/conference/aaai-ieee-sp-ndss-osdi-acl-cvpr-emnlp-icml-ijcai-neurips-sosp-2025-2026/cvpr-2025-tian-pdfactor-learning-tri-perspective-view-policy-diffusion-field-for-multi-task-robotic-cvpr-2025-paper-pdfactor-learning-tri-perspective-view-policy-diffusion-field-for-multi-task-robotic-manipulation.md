---
title: "PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation"
title_zh: PDFactor：学习三视角策略扩散场以实现多任务机器人操作
authors: "Tian, Jingyi, Wang, Le, Zhou, Sanping, Wang, Sen, Li, Jiayi, Sun, Haowen, Tang, Wei"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf"
tags: ["query:analysis"]
score: 7.0
evidence: 利用混合三平面表示建模6-DoF动作分布，生成潜在扩散场。
tldr: 针对机器人操作中动作分布建模的精度与效率权衡难题，PDFactor提出三视角策略扩散场，将点云分解为正交特征平面，通过三视角变换器生成密集立方特征作为潜在扩散场，表示任意位置6-DoF动作概率分布，在多任务操作中实现高精度与高效率的兼顾，为动作表征学习提供了结构化新方法。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 833, \"height\": 540, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1764, \"height\": 585, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1809, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 784, \"height\": 461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1777, \"height\": 452, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 774, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 774, \"height\": 251, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1806, \"height\": 938, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1800, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-tian-pdfactor-learning-tri-perspective-view-policy-diffusion-field-for-multi-task-robotic-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 863, \"height\": 327, \"label\": \"Table\"}]"
motivation: 现有方法在动作分布建模中难以兼顾精度与效率。
method: 提出PDFactor，采用正交三平面特征和变换器生成密集潜在扩散场。
result: 在多个操作任务上，PDFactor在准确率和效率方面优于基线方法。
conclusion: 三平面表示能有效结构化高维动作空间，提升扩散策略性能。
---

## Abstract
Robotic manipulation based on visual observations and natural language instructions is a long-standing challenge in robotics. Yet prevailing approaches model action distribution by adopting explicit or implicit representations, which often struggle to achieve a trade-off between accuracy and efficiency. In response, we propose PDFactor, a novel framework that models action distribution with a hybrid triplane representation. In particular, PDFactor decomposes 3D point cloud into three orthogonal feature planes and leverages a tri-perspective view transformer to produce dense cubic features as a latent diffusion field aligned with observation space representing 6-DoF action probability distribution at an arbitrary location. We employ a small denoising network conceptually as both a parameterized loss function measuring the quality of the learned latent features and an action gradient decoder to sample actions from the latent diffusion field during inference. This design enables our PDFactor to benefit from spatial awareness of explicit representation and arbitrary resolution of implicit representation, rendering it with manipulation accuracy, inference efficiency, and model scalability. Experiments demonstrate that PDFactor outperforms state-of-the-art approaches across a diverse range of manipulation tasks in RLBench simulation. Moreover, PDFactor can effectively learn multi-task policies from a limited number of human demonstrations, achieving promising accuracy in a variety of real-world manipulation tasks.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义
- **核心问题**：在基于视觉观察和自然语言指令的机器人操作中，如何**高效且精确地建模末端执行器的 6-DoF 动作分布**。现有方法要么采用显式表示（如体素、点云），精度较高但计算与内存开销大；要么采用隐式表示（如神经场），效率与分辨率灵活但常牺牲部分结构精度，难以在**精度与效率间取得平衡**。
- **整体含义**：论文提出 **PDFactor**，将动作分布建模为一个**混合三平面 (triplane) 表示的潜在扩散场**，旨在结合显式表示的空间感知优势与隐式表示的任意分辨率与可扩展性，实现多任务操作策略的高性能与高效率，为结构化、高维动作表征学习提供新范式。

## 2. 方法论
- **核心思想**：将 3D 场景点云分解为三个正交的特征平面，通过三视角变换器生成稠密的**立方特征体 (cubic features)**，将其作为**潜在扩散场**，该场能够编码观测空间中任意空间位置的 6-DoF 动作概率分布。去噪网络同时承担参数化损失函数和推理时的动作梯度解码器角色。
- **关键技术细节**：
  - **三平面分解**：输入点云被映射到三个互相正交的 2D 特征平面 (XY, YZ, XZ)，每个平面捕捉不同视角的空间信息。
  - **三视角变换器**：融合三个平面的特征并通过注意力机制建模全局上下文，输出一个稠密的 3D 立方特征图，形成**与观测空间对齐的潜在扩散场**。
  - **动作扩散场**：该特征场可在连续三维坐标上插值查询，其对应的隐特征用于参数化目标位置和姿态的扩散去噪过程，代表 6-DoF 动作概率分布。
  - **小型去噪网络**：不仅用于扩散训练时的 score matching，还充当一种**参数化的度量函数**评估隐特征的表示质量；推理时，它作为解码器从扩散场中采样高质量动作。
- **算法流程（文字说明）**：
  1. 将观测到的 3D 点云编码为三个正交特征平面。
  2. 三视角变换器处理平面特征，输出与场景对齐的密集潜特征场。
  3. 在训练阶段，对潜特征场中采样的点附加噪声，使用小型去噪网络预测噪声，联合优化平面编码器和变换器，使得潜特征空间能良好支持扩散过程。
  4. 推理阶段，给定任务指令和观测，生成潜扩散场，在期望的位置查询特征，通过多步去噪得到末端执行器的 6-DoF 目标位姿。

## 3. 实验设计
- **数据集 / 场景**：
  - 模拟环境：**RLBench**——经典的机器人操作基准，包含多个需要视觉和语言指令的任务。
  - 真实世界：多任务机器人操作场景，使用**少量人类示教数据**进行策略学习。
- **对比方法**：与现有的最先进 (SOTA) 方法进行比较，大致覆盖以下几类（文中应有具体方法名，此处根据摘要推断）：
  - 基于显式表征的动作生成方法（如体素化策略）。
  - 基于隐式表征的扩散策略（如 3D 扩散策略、NeRF-based 策略）。
  - 端到端的行为克隆或强化学习基线。
- **评估指标**：任务成功率、动作精度（如平移/旋转误差）、推理效率（耗时、计算量）。

## 4. 资源与算力
- 提供的摘要及元数据中**未明确说明**训练所使用的 GPU 型号、数量、训练时长等算力细节。原文图表缺失，无法获取相关信息。通常在会议正文中会给出，但基于目前给定的内容只能声明信息不足。

## 5. 实验数量与充分性
- 根据现有信息，实验总体较为丰富，至少包括：
  - **RLBench 多任务性能对比实验**（与多个基线方法的全面比较）。
  - **真实世界多任务迁移实验**，验证仿真到现实的泛化能力和样本效率。
  - 可能包含**消融实验**（例如分析三平面表示的有效性、变换器设计、扩散场分辨率的影响等）。
- **充分性与公平性**：从摘要和结论推断，对比了 SOTA 方法，有仿真和真实场景验证，若补充消融实验则实验链条较完整，评估维度覆盖精度、效率等，整体较为客观公平。但因无法获取实验表格详情，无法量化肯定。

## 6. 论文的主要结论与发现
- **三平面混合表示**能有效结构化高维动作空间，在扩散策略框架下显著提升建模效率和精度。
- PDFactor 在 RLBench 多个操作任务上**准确率与效率均超越**现有最优方法。
- 该方法具备良好的**样本效率**，仅用少量人类示教即可在真实环境中取得有前景的成功率。
- 潜在扩散场的设计允许在**任意空间位置**采样动作，兼得显式表征的空间一致性与隐式表征的连续分辨能力，模型亦具可扩展性。

## 7. 优点
- **方法层面**：
  - 创新性地将三平面表示引入机器人动作扩散策略，**兼顾空间感知与连续表示**，平衡精度与效率。
  - 去噪网络的双重作用（损失函数 + 动作解码器）设计精妙，简化训练并提升隐特征质量。
  - 点云到潜扩散场的端到端学习，避免手工设计动作先验。
- **实验层面**：
  - 仿真与真实环境双重验证，增强了方法的实践说服力。
  - 涵盖多任务、有限示教场景，体现较强的泛化性和实用性。

## 8. 不足与局限
- **未明确说明的局限**（基于摘要推断）：
  - **点云依赖**：输入依赖于 3D 点云的质量和密度，传感器噪声或遮挡可能影响表示。
  - **真实世界实验规模**：虽验证了有效性，但真实任务数量和多样性可能有限，从少量示教学习对复杂灵巧操作仍具挑战。
  - **推理速度**：扩散过程虽声称高效，但多步去噪仍可能比单步前馈方法慢，且未与纯确定性策略的推理延迟对比（摘要未给出具体数值），在需要高频控制的场景可能受限。
  - **多任务扩展上限**：三平面表示在大规模任务类别上的可扩展性未深入探讨，特征解耦能力有待检验。
- **实验覆盖风险**：若消融设计不全面或对比基线版本较旧，可能夸大优势，但摘要无法判断。
- **应用限制**：主要针对抓取和操作，未覆盖移动操作或动态环境。

（完）
