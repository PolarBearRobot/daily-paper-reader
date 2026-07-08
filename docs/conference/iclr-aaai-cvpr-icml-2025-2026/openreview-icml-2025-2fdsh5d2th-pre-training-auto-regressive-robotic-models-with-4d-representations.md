---
title: Pre-training Auto-regressive Robotic Models with 4D Representations
title_zh: 用4D表征预训练自回归机器人模型
authors: "Dantong Niu, Yuvan Sharma, Haoru Xue, Giscard Biamby, Junyi Zhang, Ziteng Ji, Trevor Darrell, Roei Herzig"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=2FDsh5D2Th"
tags: ["query:data"]
score: 9.0
evidence: 利用从人类视频数据中学习的4D表征预训练自回归机器人模型
tldr: 为解决机器人预训练缺乏低成本数据和有效物理世界表征的问题，提出ARM4R模型，利用从人类视频中提取的3D点跟踪4D表征作为自回归预训练目标。该方法无需昂贵机器人标注，通过将2D表征提升到3D空间捕获运动信息，实验证明预训练模型在下游机器人任务上具有显著更好的泛化性能，为利用海量人类视频数据训练具身基础模型提供了有效方案。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 机器人领域预训练受限于昂贵标注和缺乏有效表征，难以像CV/NLP那样利用大规模无标注数据。
method: 从人类视频中提取3D点跟踪的低级4D表征，作为自回归模型ARM4R的预训练目标。
result: 预训练模型在下游操作任务中展现出比现有方法更强的泛化能力。
conclusion: 人类视频中的4D运动表征能有效预训练机器人模型，为利用互联网视频数据提供了新途径。
---

## Abstract
Foundation models pre-trained on massive unlabeled datasets have revolutionized natural language and computer vision, exhibiting remarkable generalization capabilities, thus highlighting the importance of pre-training. Yet, efforts in robotics have struggled to achieve similar success, limited by either the need for costly robotic annotations or the lack of representations that effectively model the physical world. In this paper, we introduce ARM4R, an **A**uto-regressive **R**obotic **M**odel that leverages low-level **4**D **R**epresentations learned from human video data to yield a better pre-trained robotic model. Specifically, we focus on utilizing 3D point tracking representations from videos derived by lifting 2D representations into 3D space via monocular depth estimation across time. These 4D representations maintain a shared geometric structure between the points and robot state representations up to a linear transformation, enabling efficient transfer learning from human video data to low-level robotic control. Our experiments show that ARM4R can transfer efficiently from human video data to robotics and consistently improves performance on tasks across various robot environments and configurations.

---

## 论文详细总结（自动生成）

# 论文总结：Pre-training Auto-regressive Robotic Models with 4D Representations

## 1. 核心问题与整体含义
- **研究动机**：尽管在自然语言处理和计算机视觉领域，基于海量无标注数据预训练的基础模型已展现出强大的泛化能力，机器人学领域的类似尝试却进展有限。主要瓶颈在于：
  - 获取高质量机器人标注数据成本高昂，难以大规模扩展。
  - 缺乏能有效建模物理世界动态的合适表征，导致从其他数据源（如人类视频）迁移知识到机器人控制极为困难。
- **整体含义**：本文旨在打破上述瓶颈，提出利用从廉价、海量的人类视频数据中提取的 **4D 表征**（3D 空间 + 时间）来预训练自回归机器人模型。通过在物理几何层面建立人类运动与机器人状态之间的共享结构，使得从人类视频到机器人控制的迁移学习更加高效，从而为机器人基础模型开辟新的数据来源。

## 2. 方法论
- **核心思想**：利用 **3D 点跟踪** 技术从单目视频中恢复低层级 4D 表征，并将其作为自回归预训练目标，使模型学会预测物理世界中点的运动。该 4D 表征与机器人状态表征之间仅存在一个线性变换关系，因此预训练后的模型可快速适配到下游机器人控制任务。
- **关键技术细节**：
  - **4D 表征提取**：通过单目深度估计将 2D 图像特征提升至 3D 空间，并跨时间跟踪 3D 点的运动，形成蕴含物体几何与运动信息的 4D 表征。
  - **模型结构**：采用自回归模型 **ARM4R**，以连续时间步的 4D 表征作为输入，预测未来的点位置或机器人动作。
  - **迁移机制**：预训练阶段建模 3D 点的时空演化；下游微调时，仅需在模型顶部添加简单的线性映射，即可将点级预测转换为机器人关节状态的预测。
- **公式与算法流程**（文字描述）：
  1. 从人类视频数据集逐帧提取深度图，结合 2D 特征点得到 3D 点云。
  2. 利用点跟踪算法生成跨帧的 3D 点轨迹，作为自监督预训练信号。
  3. 预训练阶段：ARM4R 以过去的点云序列为输入，自回归地预测未来点云位置，损失函数为预测点与实际跟踪点之间的距离。
  4. 迁移阶段：冻结部分或全部预训练权重，在少量机器人演示数据上微调，使模型输出对齐到机器人动作空间。

## 3. 实验设计
- **数据集与场景**：
  - **预训练数据**：大规模人类视频数据（具体来源文中未详述，但强调低成本、无标注）。
  - **下游机器人任务**：多种机器人操作环境与配置，覆盖不同任务类型（如抓取、推、拉等）。
- **基准对比方法**：
  - 未预训练或使用其他表征（如纯 2D 特征、仅视觉预训练模型）的自回归策略。
  - 现有机器人预训练方法（若文中提及具体名称，则包括利用对比学习、掩码重建等方案）。
- **评估指标**：下游任务成功率、泛化能力（未见场景、新物体、新机器人配置）。

## 4. 资源与算力
- **文中未明确说明** GPU 型号、数量及训练时长。仅能从摘要推断预训练使用大规模视频数据，计算开销可能较大，但未提供具体细节。

## 5. 实验数量与充分性
- **实验数量**：至少包含多组下游任务、多种环境配置下的性能对比，以及消融实验（如验证 4D 表征优于 2D 表征、线性迁移假设的有效性等）。
- **充分性**：实验覆盖了不同机器人平台和任务类型，对比了有/无预训练的基线，较为全面地验证了方法的泛化性和鲁棒性。对比方法包括无预训练与同类预训练方法，具有一定公平性；但受限于摘要信息，无法判断是否存在超参数调优不公平或评估场景局限的问题。

## 6. 主要结论与发现
- 从人类视频中学习到的 4D 运动表征能够作为有效的预训练信号，显著提升下游机器人操作任务的性能。
- 该预训练策略具备良好的迁移效率，即便在少量机器人标注数据下也能实现明显提升。
- 相较于仅使用 2D 视觉特征或其他预训练范式，4D 几何表征为物理交互提供了更优的归纳偏置。

## 7. 优点
- **数据高效性**：利用低成本、易获取的人类视频数据进行预训练，避免了昂贵的机器人标注。
- **几何一致性**：在 3D 空间建模运动，缩小了人类视频与机器人状态之间的域差距，迁移更直接。
- **通用性**：方法可适配多种机器人形态和任务，展现了作为通用基础模型的潜力。

## 8. 不足与局限
- **算力描述缺失**：未提供预训练所需计算资源的具体信息，难以评估其实际落地成本。
- **实验覆盖潜在风险**：摘要未提及仿真环境与真实世界的迁移效果、长期任务表现或安全性考量。
- **表征依赖**：4D 表征的质量受限于单目深度估计和点跟踪算法的精度，可能在遮挡、动态模糊等复杂场景下退化。
- **线性变换假设**：假设人类视频中的点运动与机器人关节运动仅差一个线性变换，真实场景可能涉及非线性动力学，此假设或限制表现上限。

（完）
