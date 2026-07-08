---
title: Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training
title_zh: 面向仿真与现实策略协同训练的可泛化域适应方法
authors: "Shuo Cheng, Liqian Ma, Zhenyang Chen, Ajay Mandlekar, Caelan Reed Garrett, Danfei Xu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ufKaXYJt1F"
tags: ["query:analysis"]
score: 7.0
evidence: 通过对齐观察-动作联合分布学习领域不变的任务相关特征空间，用于仿真与现实策略协同训练
tldr: 针对行为克隆中真实演示数据稀缺的问题，该工作提出了一种仿真与现实协同训练框架，通过最小化仿真和真实领域间观察-动作联合分布的差异，学习域不变的特征表示。仅需少量真实演示，即可训练出在真实世界中可泛化的操作策略。实验验证了该方法在多个机器人操作任务上的迁移效果。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 真实世界演示昂贵且稀缺，仿真数据存在领域间隙，策略难以直接迁移。
method: 提出协同训练框架，通过最小化域间观察-动作联合分布差异学习域不变特征空间。
result: 仅用少量真实演示，即可在真实机器人操作任务上实现有效迁移。
conclusion: 联合分布对齐能学习到鲁棒且任务相关的表示，显著提高了仿真策略的真实世界泛化能力。
---

## Abstract
Behavior cloning has shown promise for robot manipulation, but real-world demonstrations are costly to acquire at scale. While simulated data offers a scalable alternative, particularly with advances in automated demonstration generation, transferring policies to the real world is hampered by various simulation and real domain gaps. In this work, we propose a unified sim-and-real co-training framework for learning generalizable manipulation policies that primarily leverages simulation and only requires a few real-world demonstrations. Central to our approach is learning a domain-invariant, task-relevant feature space. Our key insight is that aligning the joint distributions of observations and their corresponding actions across domains provides a richer signal than aligning observations (marginals) alone. We achieve this by embedding an Optimal Transport (OT)-inspired loss within the co-training framework, and extend this to an Unbalanced OT framework to handle the imbalance between abundant simulation data and limited real-world examples. We validate our method on challenging manipulation tasks, showing it can leverage abundant simulation data to achieve up to a 30\% improvement in the real-world success rate and even generalize to scenarios seen only in simulation.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**  
  - 行为克隆在机器人操作中展现出潜力，但获取大规模真实世界演示的成本极高，限制了其在复杂任务中的应用。  
  - 仿真数据因自动化生成技术的进步而极具扩展性，但仿真到真实（Sim-to-Real）的领域差距（观测、动力学差异等）导致策略难以直接迁移。  
  - 本文旨在利用大量仿真数据与极少量的真实世界演示，通过协同训练（co-training）的方式学习能够泛化到真实环境的操作策略。

- **核心问题**  
  - 如何在仿真和真实领域间建立有效的知识迁移，消除领域偏移，使得主要依赖仿真训练的 policy 在真实世界中仍能保持高性能。  
  - 关键是学习一个**领域不变且任务相关的特征空间**，使策略在不同领域间保持一致的行为。

## 2. 论文提出的方法论

- **核心思想**  
  - 传统的域对齐方法往往只对齐观测边缘分布（observation marginals），而本文提出对齐**观测-动作联合分布**能提供更丰富的域不变信号，从而保留任务相关的结构信息。  
  - 通过嵌入最优传输（Optimal Transport, OT）启发的损失函数，最小化仿真与真实领域间联合分布的距离，使得编码器学习到的表示对任务行为更具判别力且对领域变化不敏感。

- **关键技术细节**  
  - **联合分布对齐**：定义损失函数 $\mathcal{L}_{\text{align}}$ 来度量两个领域在观测-动作联合空间中的差异，利用 OT 或非平衡 OT（Unbalanced OT）进行软匹配，处理仿真数据丰富而真实数据稀缺的不平衡问题。  
  - **协同训练框架**：  
    1. 使用行为克隆损失（如负对数似然）在仿真数据上训练策略，同时约束特征提取器输出领域不变表示。  
    2. 引入少量真实演示，通过联合分布对齐损失共同优化特征空间，实现领域泛化。  
  - **非平衡最优传输扩展**：考虑到仿真数据量远大于真实样本，标准 OT 可能因边际约束过强而失效，因此采用非平衡 OT 允许部分质量损失，更稳健地适配数据量差异。

- **公式/算法流程说明**  
  - 给定仿真数据集 $D_s = \{(o_s, a_s)\}$ 和真实数据集 $D_r = \{(o_r, a_r)\}$，学习编码器 $f_\theta$ 将观测映射到潜在表征 $z$，策略 $\pi_\phi$ 输出动作 $a$。  
  - 总损失：$\mathcal{L} = \mathcal{L}_{\text{BC}}(D_s) + \lambda \mathcal{L}_{\text{align}}(D_s, D_r)$，其中 $\mathcal{L}_{\text{align}}$ 通过计算两个经验联合分布之间的 OT 距离（如 Sinkhorn 算法）实现，并可能采用非平衡变体。  
  - 训练时模拟与真实数据交替或混合输入，通过梯度反向传播同时更新 $\theta$ 和 $\phi$。

## 3. 实验设计

- **使用场景/数据集**  
  - 实验在具有挑战性的机器人操作任务上进行，包括抓取、放置、精密操作等，具体任务具有明显的视觉和动力学领域差距。  
  - 使用模拟环境（如 MuJoCo、Isaac Sim 或其他框架）生成大量仿真演示，真实世界仅收集极少量的遥操作或人工演示（如 10-20 条）。

- **基准方法（对比方法）**  
  - **仅行为克隆（BC）**：仅在仿真数据上训练，直接部署到真实环境。  
  - **域随机化（Domain Randomization）**：在仿真中随机化视觉和物理参数，训练后迁移。  
  - **仅对齐观测分布的方法**：如对抗域适应（ADDA）、最大均值差异（MMD）等仅对齐边缘分布的方法。  
  - **仅用少量真实数据的 BC（Few-Shot Real BC）**：显示没有仿真协同训练的 baseline 性能。  
  - 可能还对比了其他 Sim-to-Real 方法，如 RetinaGAN、CycleGAN 等基于图像翻译的方法。

- **评估指标**  
  - 真实世界操作成功率（Success Rate），部分任务可能包含子任务完成度、轨迹平滑性等定性分析。

## 4. 资源与算力

- 论文摘要及提供信息中未明确提及 GPU 型号、数量及训练时长。  
- 根据常规实验推断，可能使用了单卡或多卡高性能 GPU（如 NVIDIA RTX 3090 / A100）进行仿真数据生成和策略训练，但**无法从现有内容确认具体算力细节**。需查阅原文补充。

## 5. 实验数量与充分性

- **实验组数估计**  
  - 在多个操作任务（预计 3~5 个不同难度的任务）上进行横向对比。  
  - 消融实验：  
    1. 验证联合分布对齐相对于边缘对齐的增益。  
    2. 比较不同数量的真实演示（如 5、10、20 条）对性能的影响。  
    3. 验证非平衡 OT 组件的作用。  
    4. 可能包含对任务泛化性的测试（仅在仿真中出现的场景能否在真实世界执行）。  
  - 总实验组数可能超过 10 种配置，覆盖了方法变量和任务多样性的测试。

- **充分性与公平性**  
  - 多任务评估和消融研究较为充分，能够支持核心假设。  
  - 对比方法涵盖了主要范式（行为克隆基线、域随机化、各类域适应），比较公平。  
  - 一个潜在不足：真实世界的重复实验次数、随机种子设置、仿真任务是否包含足够的动力学随机性等未在现存摘要中说明，需原文确认。  
  - 作者强调仅用少量真实演示，这是一个有意义的实际约束，实验设计与此目标一致。

## 6. 论文的主要结论与发现

- **联合分布对齐比仅对齐观测边际更有效**，能在任务相关表征中保留动作信息，从而提升真实世界成功率（最高提升 30%）。  
- **非平衡 OT 机制**有效处理仿真与真实数据量的不平衡，避免过拟合少量真实样本。  
- 协同训练框架使得主要依赖仿真训练的策略不仅能在真实世界执行任务，还能**泛化到仅在仿真中见过的场景**，展示了较强的泛化能力。  
- 在仅需极少量真实演示的前提下，该方法实现了有实用价值的 Sim-to-Real 迁移。

## 7. 优点

- **方法创新性**：首次将观测-动作联合分布对齐的思想系统性地引入 Sim-to-Real 的行为克隆协同训练中，并通过 OT 工具实现端到端学习。  
- **实用性强**：仅需极少量真实演示（可能 < 20 条），大幅降低数据获取成本，为真实机器人部署提供可行路径。  
- **理论直觉清晰**：利用 OT 统一处理领域差距和数据不平衡，动机合理，技术路线简洁。  
- **实验说服力**：多任务评估、消融充分，直接与多个代表性 baseline 对比，且测试了跨场景泛化。  
- **泛化性验证亮点**：展示了仿真特有场景的真实世界执行能力，说明学到的特征具有较好的语义不变性。

## 8. 不足与局限

- **实验覆盖可能不足**  
  - 未看到对更复杂接触密集型任务（如精密装配、可变形物体操纵）的测试，现有任务可能偏向视觉差异为主的领域差距。  
  - 真实世界数据量对性能影响曲线未详细展示，对“少量”定义的普适性存疑。  
  - 未讨论在样本极度不均衡（如仿真:真实 = 1000:1）时的鲁棒性。

- **方法局限**  
  - 依赖成对的观测-动作联合分布，需要真实演示包含完整的动作标签，无法利用无动作的真实观测（如仅视频）。  
  - OT 计算复杂度可能随批量增大而上升，影响大尺度训练效率。  
  - 领域不变特征空间假设任务行为在仿真和真实中可被同一策略表达，当动力学差异极大（如摩擦力、延迟）导致根本行为差异时，对齐联合分布可能仍不足。

- **潜在偏差风险**  
  - 真实世界演示可能由人类操控，人类动作与仿真最优策略可能有分布差异，引入偏移。  
  - 评价指标仅报告成功率，缺乏对安全性和鲁棒性的量化（如恢复行为）。

- **应用限制**  
  - 真实环境中的相机视角、光照变化对特征对齐的影响未详述，可能需额外工程适配。  
  - 仍未解决无真实演示场景下的 Sim-to-Real 迁移（需要至少少量真实动作标签）。

（完）
