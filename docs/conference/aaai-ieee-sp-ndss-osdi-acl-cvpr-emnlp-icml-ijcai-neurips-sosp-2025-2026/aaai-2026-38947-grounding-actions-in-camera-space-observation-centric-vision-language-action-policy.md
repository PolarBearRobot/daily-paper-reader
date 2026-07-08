---
title: "Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy"
title_zh: 将动作锚定于相机空间：以观测为中心的视觉语言动作策略
authors: "Tianyi Zhang, Haonan Duan, Haoran Hao, Yu Qiao, Jifeng Dai, Zhi Hou"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38947/42909"
tags: ["query:analysis"]
score: 9.0
evidence: 通过将动作锚定在相机空间，解决观测与动作空间的差异。
tldr: 针对VLA模型由于观测和动作空间不一致导致泛化困难的问题，OC-VLA提出以观测为中心的框架，利用相机外参将末端执行器位姿从机器人基坐标系变换到相机坐标系，统一预测目标，在多视角任务中显著提升了零样本泛化性能，为对齐隐状态表示与动作控制提供了直接解决方案。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38947/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 858, \"height\": 506, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38947/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1808, \"height\": 571, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38947/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 810, \"height\": 1187, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38947/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 855, \"height\": 643, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38947/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 855, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38947/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 854, \"height\": 1062, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38947/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1441, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38947/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1778, \"height\": 855, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38947/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1829, \"height\": 265, \"label\": \"Table\"}]"
motivation: VLA模型观测空间与动作空间不一致，导致空间泛化能力差。
method: 提出OC-VLA，将动作预测锚定在相机坐标系，利用外参标定变换。
result: 在多样相机视角测试中，OC-VLA展现了卓越的跨视角泛化性能。
conclusion: 统一观测与动作空间是提升VLA空间泛化性的关键。
---

## Abstract
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera’s extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **核心问题**：现有视觉语言动作（VLA）模型通常在机器人基坐标系下预测末端执行器位姿，但视觉观测却来自相机坐标系，导致观测空间与动作空间不匹配。这种不一致性在相机视角变化时尤为突出，严重影响模型的跨视角泛化能力。
- **研究动机**：机器人训练数据通常采集自不同相机视角，但模型却需学习从二维观测推断三维空间动作，这本质上是一个“病态”问题。尤其在相机位姿多样的大规模预训练中，同一动作在不同视角下的观测共享同一个基坐标系监督信号，会引入学习冲突，阻碍泛化。
- **整体含义**：提出以观测为中心的 VLA 框架（OC-VLA），直接将动作预测锚定在相机观测空间，从根源上对齐感知与动作，从而提升模型对相机视角变化的鲁棒性和泛化性能。

### 2. 方法论：核心思想与关键技术细节

- **核心思想**：解耦末端执行器动作与机器人基坐标系的耦合关系，改用相机坐标系下的动作表示作为预测目标，使得模型预测的输出与视觉观测在同一空间。
- **关键公式与流程**：
    1. **动作转换**：利用标定外参矩阵 \( T \in \mathbb{R}^{4\times4} \)（世界到相机），将世界坐标系下的末端执行器位姿 \( P^{\text{world}} \) 转换为相机坐标系下的位姿 \( P^{\text{cam}} = T P^{\text{world}} \)。
    2. **动作定义**：给定相邻时刻的相机系位姿，计算相机系下的相对动作 \( A^{\text{cam}} = P^{\text{cam}}_2 (P^{\text{cam}}_1)^{-1} \)，或等价地 \( A^{\text{cam}} = T A^{\text{world}} T^{-1} \)。
    3. **预测与执行**：模型直接预测 7 维动作 \(\langle x,y,z,roll,pitch,yaw,gripper\rangle\)（在相机系下），推理时再利用标定矩阵将相机系动作转换回机器人系进行控制。
- **即插即用**：无需修改模型结构，仅改变监督信号的坐标表达，与现有 VLA 架构完全兼容。
- **优化视角分析**：从观测空间的 UV 坐标到相机系坐标的映射只依赖一致的内参，而到机器人基坐标系的映射则需变化的外参，因此相机系预测任务更一致、更易学习。

### 3. 实验设计

- **数据集**：
    - **预训练**：使用 Droid 数据集（1417 个不同第三方相机视角），该数据集包含外参标定，可支撑相机系动作转换。
    - **仿真评估**：ManiSkill2 中选取 5 个代表性任务（PickCube、StackCube、PickSingleYCB、PickClutterYCB、PickSingleEGAD），随机生成 30 万个相机视角，产生超 4 万条轨迹，按 19:1 划分训练/验证，为闭集评估每条任务采样 100 条轨迹。
    - **真机评估**：基于 Franka Emika Panda 机器人，配备 3 个 Realsense D435i 相机，收集 15 个长时序任务（含抓取、堆叠、倾倒等）的示范数据，每任务 10 条，进行 10-shot 微调；另设 8 任务数据集并引入轻微相机扰动。
- **对比方法**：
    - OpenVLA-OFT、π0 等现有 VLA 方法，采用官方训练协议微调。
    - 相同结构下以机器人基坐标系动作预测作为基线（Robot Base），与相机系预测（Camera Base，即 OC-VLA）对比。
    - 针对连续动作空间（扩散策略）和离散动作空间分别进行实验。
- **评估设置**：
    - 固定相机视角、轻微相机扰动、零样本新相机视角三种设定，评估跨视角泛化。

### 4. 资源与算力

- **GPU 配置**：8 块 NVIDIA A100 GPU（每块 256 样本），全局 batch size 2048。
- **训练轮数/步数**：仿真实验从零训练 30,000 步；真机微调 20,000 步（batch size 512）。
- **优化器与学习率**：AdamW，causal Transformer 和 Q-Former 学习率 1e-4，DINOv2 学习率 1e-5。
- **其他细节**：连续扩散模型采用 DDPM 训练 100 步，推理采用 DDIM 10 步；离散模型量化至离散 bins 并计算交叉熵损失。

### 5. 实验数量与充分性

- **实验组数**：
    - 仿真：连续/离散两种动作空间 × 两种坐标表示，共 4 组主要配置，在 5 个任务上报告成功率，涵盖大量相机视角的泛化测试。
    - 真机：固定视角 15 任务、扰动视角 8 任务、零样本新视角 15 任务，与三个基线对比，共 6 组评估设置。
    - 合计约 10 组以上主要对比实验。
- **充分性与公平性**：
    - 同时涵盖仿真和真实场景，任务多样。
    - 基线包括同期热门 VLA 模型（OpenVLA、π0），且自身消融采用相同架构仅改变监督坐标。
    - 评估指标统一为成功率，闭环执行，可以反映实际操纵性能。
    - 在真机实验中严格控制训练数据量（10 demonstrations），确保对比公平。
- **潜在局限**：缺少对更大图像扰动、动态环境、多模态输入的扩展实验；未讨论标定精度影响。

### 6. 主要结论与发现

- 在仿真实验中，无论离散还是连续动作空间，相机系动作预测均显著提升任务成功率，离散空间提升约 14%。
- 在真机 10-shot 设定下，OC-VLA 比机器人基坐标基线成功率提升约 10%，并超越 OpenVLA-OFT 和 π0。
- 在零样本新视角下，OC-VLA 性能下降 14%，远小于 OpenVLA-OFT 的 20% 下降，跨视角泛化优势显著。
- 轻微相机扰动时，OC-VLA 同样表现出更强的鲁棒性。
- 总体而言，以观测为中心的动作表示能统一感知与动作空间，减轻相机视角变化带来的学习混淆，提升数据效率和泛化性。

### 7. 优点

- **概念简洁，实现轻量**：仅改变动作坐标表达，无需修改模型结构，即插即用。
- **理论扎实**：从观测空间到动作空间的一致性角度分析学习难度，给出清晰的数学解释。
- **实验全面**：覆盖仿真与真实平台，多种任务、多种动作空间，多种视角泛化设置，与多个强基线对比。
- **数据效率高**：在 10-shot 微调下即可获得显著提升，有助于实际应用。
- **公开资源**：提供代码和扩展版论文，可复现。

### 8. 不足与局限

- **依赖外参标定**：方法要求已知相机外参，标定误差或动态变化的相机位姿可能影响性能，论文未对此进行敏感性分析。
- **视角变化依赖**：虽提升了跨视角泛化，但在极端视角偏移或遮挡下仍存在失败可能，未分析失效场景。
- **预训练数据受限**：仅使用 Droid 数据集（第三方视角），尚未在更大规模、更异构的数据集上验证。
- **动作空间限制**：当前只适用于末端执行器位姿控制，未涉及关节空间或双手协调任务。
- **评估受限**：真机任务数量（15 类）和每类试次（10 次）仍较少，统计稳定性有限。

（完）
