---
title: "IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments"
title_zh: IAAO：3D环境中铰接物体的交互式可供性学习
authors: "Zhang, Can, Lee, Gim Hee"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_IAAO_Interactive_Affordance_Learning_for_Articulated_Objects_in_3D_Environments_CVPR_2025_paper.pdf"
tags: ["query:model"]
score: 4.0
evidence: 交互式可供性学习，用于3D环境中的物体理解
tldr: IAAO 提出通过交互构建显式3D模型以理解铰接物体，利用基础模型估计交互可供性，但并非面向机器人控制的具身基础模型，仅提供感知模块。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 902, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1793, \"height\": 701, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 848, \"height\": 459, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 828, \"height\": 214, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 828, \"height\": 215, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1535, \"height\": 501, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1814, \"height\": 1338, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1809, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-iaao-interactive-affordance-learning-for-articulated-objects-in-3d-environments-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 860, \"height\": 207, \"label\": \"Table\"}]"
motivation: 传统方法依赖特定任务网络和可动部件假设，缺乏通用交互理解。
method: 使用3D高斯泼溅分层建模，通过蒸馏掩膜和视一致标签估计交互可供性和部件运动。
result: 实现了铰接物体的全局变换和局部运动估计。
conclusion: 为具身智能体提供了3D物体交互理解的基础，但与机器人控制模型仍有距离。
---

## Abstract
This work presents IAAO, a novel framework that builds an explicit 3D model for intelligent agents to gain understanding of articulated objects in their environment through interaction. Unlike prior methods that rely on task-specific networks and assumptions about movable parts, our IAAO leverages large foundation models to estimate interactive affordances and part articulations in three stages. We first build hierarchical features and label fields for each object state using 3D Gaussian Splatting (3DGS) by distilling mask features and view-consistent labels from multi-view images. We then perform object- and part-level queries on the 3D Gaussian primitives to identify static and articulated elements, estimating global transformations and local articulation parameters along with affordances. Finally, scenes from different states are merged and refined based on the estimated transformations, enabling robust affordance-based interaction and manipulation of objects. Experimental results demonstrate the effectiveness of our method.

---

## 论文详细总结（自动生成）

### 1. 论文核心问题与整体含义
- **研究背景**：智能体要在真实三维环境中与铰接物体交互，不仅需要识别物体，还必须理解物体各部分的具体物理交互方式（即“可供性”，如门把手、开关）。传统方法依赖特定任务的网络和对可动部件的强假设，难以泛化到新物体类别与复杂场景。
- **核心问题**：如何让智能体在没有类别限制、未知部件数量、存在遮挡与视角变化的条件下，从多视图图像中重建物体的几何、语义、部件分割，并估计铰接运动参数（全局场景对齐与各部件局部关节运动），同时支持基于语言/点/掩码提示的可供性查询。
- **整体含义**：IAAO 提出了一种利用大型基础模型（CLIP、SAM、DINOv2）与显式 3D 高斯泼溅（3DGS）相结合的框架，通过“交互式感知”实现铰接物体的自动理解与操控，填补了以往方法在泛化性、细粒度可供性定位和复杂场景处理上的空白。

### 2. 方法论核心思想与技术细节
- **整体流程**：分三阶段——语义场景重建、可供性与运动预测、场景状态融合。
- **语义场景重建（3.1 节）**
  - 对每个关节状态的多视图图像，用 3DGS 重建场景，并通过蒸馏 SAM 产生的类别无关掩码来构建视一致标签场。
  - 设计**层次特征场**：从 CLIP 提取实例级和部件级特征，从 DINOv2 提取密集特征，通过低维潜特征场和小型 MLP 解码器压缩并嵌入 3D 高斯点，避免直接存储高维特征带来的计算与内存开销。
  - 基于 SAM 掩码构建图，聚类生成 3D 一致的实例提案，并用跨视图交叉熵损失增强标签一致性。
  - 利用掩码特征跨状态关联相同语义区域，形成全局 3D 掩码对应。
- **可供性与运动预测（3.2 节）**
  - **可供性预测**：将任务描述用 CLIP 文本编码器编码，计算其与 3D 高斯特征场中各掩码嵌入的相似度，超过阈值即定位可交互部件。同时利用标签场直接输出部件级可供性掩码。
  - **运动恢复**：
    - 通过正/负语言查询实现对象级筛选，再部件级查询定位铰接部件。
    - **全局变换**：使用 GeoTransformer 对高不透明度高斯点进行粗配准，初始化全局尺度、旋转、平移（\( \xi_t^g \)）。
    - **局部关节参数**：定义每个可动部件从状态 \( t \) 到 \( t' \) 的旋转/平移 \( \xi_t^o \)，并利用一致性损失（RGB、掩码特征、标签）和基于 DINOv2 特征相似度的点-像素匹配损失（\( L_{\text{match}} \)）联合优化。
    - 总损失：\( L = \lambda_{\text{cons}}(L_{\text{rgb}} + L_{\text{mask}} + L_{\text{label}}) + \lambda_{\text{match}} L_{\text{match}} \)
- **场景状态融合（3.3 节）**：根据估计的变换合并两个状态的 3DGS 模型，填补遮挡区域，支持平滑交互。

### 3. 实验设计
- **数据集**
  - **PARIS 两部件物体数据集**：10 个合成物体（PartNet-Mobility）+ 2 个真实物体（MultiScan 扫描），每个物体有静态与可动两部分，在两个关节状态下采集 100 个随机视点的 RGB、深度、掩码。
  - **合成多部件物体数据集**：两个场景，每个物体含一个静态基座与多个可动部件，同样 100 视点 RGB、深度、掩码。
  - **OmniSim 室内场景数据集**：用 OmniGibson 生成，包含可调铰接关节的室内环境，提供 RGB-D、交互掩码与真实状态。
- **对比基准**
  - Ditto、PARIS、PARIS*（含深度监督）、PARIS-m*（多部件扩展）、CSG-reg（TSDF+实体几何+配准）、3Dseg-reg（点云分割+配准）、DigitalTwinArt（两阶段隐式重建）。
- **评价指标**
  - 关节估计：旋转轴角度误差（Axis Ang）、轴位置误差（Axis Pos）、部件运动误差（旋转毛度或平移欧氏距离，Part Motion）。
  - 重建质量：Chamfer-L1 距离（CD-w整体，CD-s静态部分，CD-m可动部分）。

### 4. 资源与算力
- 论文**未明确提及**详细的 GPU 型号、数量或总训练时长。文中仅描述了使用 3DGS 优化和高斯点匹配，但未给出训练硬件配置或推理耗时等算力指标。

### 5. 实验数量与充分性
- **实验组别**：约 3 组主实验（两部件数据集、多部件数据集、室内场景数据集），以及 1 组消融实验（移除匹配损失、掩码约束、RGB 损失、标签场）。
- **实验覆盖**：合成物体、真实物体、单部件可动、多部件可动、室内复杂场景均有评估；对比了 7 种以上基线方法；定量与定性结果（网格重建、关节可视化、运动插值快照）并重。
- **充分性与公平性**：实验设计较全面，消融验证了各模块贡献。评估时，IAAO 利用语义特征自动对应部件，而非像其它方法遍历所有配对找最小 CD，这一差异可能影响比较的完全公平性，但论文在 3.1 节中明确了评估流程，整体较为客观。

### 6. 主要结论与发现
- IAAO 在铰接物体的形状重建、部件分割和关节参数估计上均达到或超过现有最优方法，尤其在未知类别和复杂部件上表现出强泛化能力。
- 消融实验表明，基于跨状态 2D-3D 特征匹配的损失（\( L_{\text{match}} \)）对精确运动恢复至关重要；掩码级特征约束和标签场显著改善了分割与重建质量。
- 框架支持物体级和部件级的多种交互提示，可处理不限数量的可动部件，且兼具全局场景对齐与局部运动重建。

### 7. 优点
- **零样本泛化**：借助 CLIP、SAM、DINOv2 等基础模型，无需针对特定类别预训练，对新物体类别和场景适应性强。
- **显式 3DGS 表示**：比隐式 NeRF 渲染更高效，可直接在 3D 高斯原语上进行查询和交互，无需昂贵的多尺度渲染。
- **层次语义感知**：实例级和部件级特征场支持粗粒度物体定位和细粒度可供性检测。
- **全局-局部运动解耦**：同时估计静态背景的刚性对齐和多个铰接部件的独立关节参数，更贴近真实场景。
- **多模态交互**：支持语言、点、掩码等多种提示方式，增强实用性。

### 8. 不足与局限
- **依赖已知相机姿态**：虽然提及“未知相机姿态”是挑战，但方法仍基于 SfM 提供初始点云和姿态，未实现全自动的未知姿态处理。
- **真实数据覆盖有限**：真实世界评估仅 2 个物体和模拟室内场景，缺乏大规模真实室内环境的验证，泛化到极复杂、严重遮挡的真实场景性能待考。
- **可能受掩码质量影响**：采用 SAM 生成掩码，其不稳定的分割层次和视间不一致性可能引入噪声，需额外聚类与标签场监督来缓解。
- **未讨论效率与延迟**：缺少训练/推理时间及显存占用报告，难以评估实际部署时的实时性。
- **仅考虑两状态观测**：运动重建要求场景在两个不同关节状态下被完整拍摄，当可动部件多于一个且需要多步交互时，可能需要多次采集。

（完）
