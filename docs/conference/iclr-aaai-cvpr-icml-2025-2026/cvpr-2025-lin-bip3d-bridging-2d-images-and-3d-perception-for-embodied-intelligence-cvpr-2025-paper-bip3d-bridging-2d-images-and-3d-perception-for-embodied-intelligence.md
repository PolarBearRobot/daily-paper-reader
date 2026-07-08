---
title: "BIP3D: Bridging 2D Images and 3D Perception for Embodied Intelligence"
title_zh: BIP3D：桥接二维图像与三维感知赋能具身智能
authors: "Lin, Xuewu, Lin, Tianwei, Huang, Lichao, Xie, Hongyu, Su, Zhizhong"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_BIP3D_Bridging_2D_Images_and_3D_Perception_for_Embodied_Intelligence_CVPR_2025_paper.pdf"
tags: ["query:model"]
score: 9.0
evidence: 利用二维基础模型和空间增强模块为具身智能提供三维感知
tldr: 针对具身智能中传统点云方法存在稀疏、噪声等问题，提出以图像为中心的BIP3D模型，利用预训练二维视觉基础模型提升语义理解，并加入空间增强模块强化空间感知，为具身代理提供更鲁棒的三维环境理解能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 858, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1760, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1783, \"height\": 553, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1793, \"height\": 472, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 868, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1818, \"height\": 363, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1783, \"height\": 470, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1755, \"height\": 380, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1739, \"height\": 685, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1650, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-bip3d-bridging-2d-images-and-3d-perception-for-embodied-intelligence-cvpr-2025-paper/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1544, \"height\": 233, \"label\": \"Table\"}]"
motivation: 传统三维感知依赖稀疏、噪声点云，限制了具身代理的环境理解性能。
method: BIP3D以图像为中心，融合预训练二维基础模型和空间增强模块，提升三维感知的语义与空间理解。
result: 实验表明BIP3D在多种三维感知任务上优于基于点云的方法。
conclusion: BIP3D为具身智能提供了一种有效的三维感知方案，加速了从二维到三维的桥接。
---

## Abstract
In embodied intelligence systems, a key component is 3D perception algorithm, which enables agents to understand their surrounding environments. Previous algorithms primarily rely on point cloud, which, despite offering precise geometric information, still constrain perception performance due to inherent sparsity, noise, and data scarcity. In this work, we introduce a novel image-centric 3D perception model, BIP3D, which leverages expressive image features with explicit 3D position encoding to overcome the limitations of point-centric methods. Specifically, we leverage pre-trained 2D vision foundation models to enhance semantic understanding, and introduce a spatial enhancer module to improve spatial understanding. Together, these modules enable BIP3D to achieve multi-view, multi-modal feature fusion and end-to-end 3D perception. In our experiments, BIP3D outperforms current state-of-the-art results on the EmbodiedScan benchmark, achieving improvements of 5.69% in the 3D detection task and 15.25% in the 3D visual grounding task. Code has been released at https://github.com/HorizonRobotics/BIP3D.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **研究动机**：具身智能系统中的三维感知模块对于理解环境至关重要。传统方法主要依赖点云（point cloud），尽管点云能提供精确的几何信息，但其固有的稀疏性、噪声以及数据采集与标注成本高的问题，限制了感知性能的上限。
- **核心问题**：如何克服点云方法的局限，有效利用海量图像数据中蕴含的丰富语义信息，来提升三维环境下的物体检测与视觉定位（visual grounding）性能。
- **整体含义**：提出了一种以图像为中心的（image‑centric）三维感知范式——**BIP3D**，它通过桥接二维基础模型与三维空间编码，为具身代理提供更鲁棒、语义更丰富的环境理解能力，并显著降低对高质量点云的依赖。

### 2. 论文提出的方法论

- **核心思想**：将预训练的二维视觉‑语言基础模型（GroundingDINO）作为特征提取和交互的主干，并将其扩展至三维。整个网络以多视角图像特征为核心表示，而不是以点云体素为中心。
- **系统架构**：BIP3D 接受多视角图像、文本指令以及可选的深度图作为输入，输出文本所指定目标的三维边界框。网络包含六个主要模块：文本编码器、图像编码器、深度编码器、特征增强器、空间增强器以及具有多视角融合能力的 Transformer 解码器。
- **关键技术细节**：
  - **特征增强器（Feature Enhancer）**：针对多视角输入导致特征向量数量巨大的问题，仅使用最大步长的特征图与文本特征进行双向交叉注意力，其他尺度的图像特征通过视角内多跨度可变形注意力间接获取文本信息。
  - **空间增强器（Spatial Enhancer）**：
    - 显式建模相机投影模型 \(C\) 和 \(C^{-1}\)，在视锥体内均匀采样三维点，并经线性层生成点位置嵌入 \(PPE\)。
    - 利用图像特征和深度特征联合预测离散深度分布 \(DT\)，从而将点嵌入加权聚合为依赖图像内容的图像位置嵌入 \(IPE\)。
    - 将原始图像特征、深度特征与 \(IPE\) 融合，得到增强的图像特征 \(I'\)。
  - **多视角融合解码器**：
    - 每个查询（query）维护一个九自由度三维框 \(B\)，在其内部采样三维关键点（包括可学习偏移和固定先验点）。
    - 将三维关键点投影到各视角特征图上，通过可变形注意力采样特征 \(F\)。
    - 查询特征、三维框与相机参数共同预测权重 \(W\)，并对无效采样点显式置零，最终加权聚合多视角特征以更新查询。
  - **相机内参标准化（CIS）**：通过将输入图像变换到统一的虚拟相机坐标系，缓解模型对相机内参的泛化能力不足问题。
  - **训练损失**：采用一对一匹配损失，包括基于对比损失的分类损失 \(L_{cls}\)、中心点回归的 L2 损失 \(L_{center}\)，以及基于简化 Wasserstein 距离的九自由度框回归损失 \(L_{box}\)（避免方向歧义）。
- **算法流程**：图像→相机建模与位置编码→深度分布加权融合→文本‑图像特征增强→多视角三维可变形聚合→三维边界框预测。

### 3. 实验设计

- **数据集与基准**：主要在 **EmbodiedScan** 基准上进行评估。该基准整合了 **ScanNet、3RScan、Matterport3D** 三个室内 RGB‑D 数据集，包含 4 633 个高质量扫描，训练/验证/测试划分分别为 3 113/817/703 个扫描。评测指标为基于三维 IoU 阈值为 0.25 的平均精度（AP₃D@0.25）。
- **对比方法**：
  - **三维检测任务**：与点模型 VoteNet、纯 RGB 模型 ImVoxelNet、稀疏体素模型 FCAF3D 以及多模态融合模型 EmbodiedScan‑D 进行对比。
  - **三维视觉定位任务**：与 EmbodiedScan 基线、SAG3D、DenseG 等单阶段或两阶段方法对比。
- **评估维度**：除总体指标外，还从类别泛化性（头部/常见/尾部）、目标体积（小/中/大）、场景与传感器泛化性（不同子集）以及定位任务的难度与视角依赖性等角度进行细分评测。

### 4. 资源与算力

- **硬件配置**：所有模型均使用 **8 块 NVIDIA 4090 GPU（24 GB 显存）** 进行训练。
- **训练时长**：论文未明确给出每个模型的具体训练时长（如 epoch 数或 wall clock time），仅提及使用 AdamW 优化器，训练过程中随机采样 18 张图像作为输入，测试时使用 50 张关键帧。
- **模型参数量**：BIP3D 总参数量约 **166.84 MB**，其中二维编码器 28.29 MB，三维编码器仅 0.09 MB，远低于点云中心模型 EmbodiedScan‑G 的 219.76 MB（其三维编码器占 87.31 MB），体现了图像中心设计的轻量化优势。

### 5. 实验数量与充分性

- **主要实验**：
  - 三维检测任务：在整体验证集上提供详细的子类别与子体积性能对比（6 种方法）。
  - 三维视觉定位任务：验证集与测试集结果对比（含模型集成）。
- **消融研究与分析实验**：
  - 二维预训练权重对点中心模型与图像中心模型的影响对比（4 组配置）。
  - 相机内参标准化（CIS）在不同训练/评估子集组合下的作用（12 组对比，覆盖 RGB 与 RGB‑D 模式）。
  - 边界框回归损失函数对比（4 种损失：CCD、L1、PCD、WD）。
  - 训练时文本描述数量对视觉定位性能的影响（3 种策略）。
- **充分性与公平性**：实验设计较为系统，覆盖了从预训练、输入模态、损失函数、训练策略到泛化能力的多维度分析。对比方法均为同期或近期代表性工作，评估标准一致，且采用了公开、广泛使用的 EmbodiedScan 基准，整体实验具备较好的充分性与客观公平性。

### 6. 论文的主要结论与发现

- **以图像为中心的架构有效**：通过将二维视觉基础模型与显式三维位置编码结合，BIP3D 在三维检测和定位任务上均大幅超越现有基于点云的方法。
- **性能显著提升**：在 EmbodiedScan 验证集上，三维检测 AP 比 EmbodiedScan 基线提升 **5.69%**；三维视觉定位 AP 提升 **15.25%**。在测试集上，模型整合后超越挑战赛冠军 DenseG **2.49%**。
- **泛化能力强**：得益于二维基础模型的强大语义，BIP3D 在尾部类别和小目标上展现出显著优势，验证了图像密集特征对细节感知的益处。
- **标准化与损失函数设计关键**：相机内参标准化和基于 Wasserstein 距离的框回归损失对稳定训练和提升精度有重要作用。

### 7. 优点

- **创新范式**：明确提出图像中心的三维感知架构，将大量参数转移到二维编码器，极大降低了三维编码器的参数量，有效利用了大规图像预训练权重。
- **灵活的多模态融合**：支持 RGB、RGB‑D 以及纯文本输入，既能做开集检测也能做指代表达定位，并可通过随机描述训练策略提升定位鲁棒性。
- **精细的空间建模**：通过可学习的深度分布加权与三维关键点采样，实现了动态、内容感知的空间增强和多视角融合，优于传统固定编码方式。
- **全面的实验验证**：在主流大基准上进行多任务、多细粒度评测，消融实验扎实，为后续图像中心三维感知的研究提供了有价值的分析指导。

### 8. 不足与局限

- **动态场景尚未涉及**：当前模型主要面向静态室内扫描场景，未在动态环境或时序信息融合的检测‑跟踪任务上进行验证。
- **下游任务有限**：仅实现了三维检测与视觉定位，对于实例分割、占用栅格、抓取姿态估计等更细粒度的三维感知任务尚未扩展。
- **对深度输入的依赖性**：虽然 RGB‑only 模式下已超过现有方法，但引入深度图仍带来显著增益（特别是小目标）。在极端弱纹理或大基线情况下，纯 RGB 的性能可能受限。
- **训练与推理效率未充分分析**：论文未提供推理速度（FPS）或训练时间的具体数字，且单次需处理 50 张静态图像，在实时具身系统中可能存在效率瓶颈。
- **相机内参泛化的局限性**：当训练集相机参数多样性不足时，即使采用标准化，跨传感器泛化仍可能受到场景和类别分布差异的影响（文中在 3RScan→MP3D 等迁移实验中有所体现）。
- **实验覆盖**：消融与对比均基于 EmbodiedScan，缺少在更广泛室外或自动驾驶数据集（如 nuScenes、Waymo）上的验证，结论的普适性有待进一步检验。

（完）
