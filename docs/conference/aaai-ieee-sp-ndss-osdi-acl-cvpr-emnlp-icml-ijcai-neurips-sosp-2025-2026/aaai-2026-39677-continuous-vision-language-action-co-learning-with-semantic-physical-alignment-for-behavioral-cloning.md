---
title: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
title_zh: 面向行为克隆的连续视觉-语言-动作协同学习与语义-物理对齐
authors: "Xiuxiu Qi, Yu Yang, Jiannong Cao, Luyao Bai, Chongshan Fan, Chengtai Cao, Hongpeng Wang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39677/43638"
tags: ["query:analysis"]
score: 9.0
evidence: 解决语义-物理对齐错配问题，改善视觉-语言-动作协同学习及行为克隆
tldr: CCoL针对行为克隆中因物理不连续和语义-物理错配导致的复合误差问题，提出连续视觉-语言-动作协同学习框架，实现语义与物理表征的持续对齐。实验表明该方法显著减少了动作克隆中的不准确性，提升了机器人操作执行的流畅性。这项工作为弥合表征与动作之间的鸿沟提供了有效方案。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1724, \"height\": 739}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 860, \"height\": 461}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 864, \"height\": 383}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 592, \"height\": 312}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 591, \"height\": 173}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 844, \"height\": 365}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 862, \"height\": 444}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 870, \"height\": 486}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 862, \"height\": 373}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 880, \"height\": 409}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1779, \"height\": 499}]"
motivation: 现有行为克隆方法存在物理不连续和语义-物理错配，导致动作执行不准。
method: 提出CCoL框架，连续进行视觉-语言-动作协同学习与语义-物理对齐。
result: 对齐后的策略减少了复合误差，提升了动作克隆的准确性和连续性。
conclusion: CCoL通过表征对齐有效改进了行为克隆的性能。
---

## Abstract
Language-Conditioned Manipulation (LCM) facilitates human-robot interaction via Behavioral Cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (i.e., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL’s generalization under unseen and noisy object states.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
*   **核心问题**：语言驱动的机器人操作（LCM）在利用行为克隆（BC）学习控制策略时，面临着严重的**复合误差（Compounding Errors）**问题。这种误差源于顺序决策过程中的错误累积，导致策略在长时域任务中失效。
*   **现有局限**：当前解决复合误差的方法（如数据增强、表达性表征学习、时间抽象）存在两个关键缺陷：
    *   **物理不连续性（Physical Discontinuities）**：时间抽象等离散动作建模方法会破坏动作轨迹的平滑性，导致急动或运动学上不可行的过渡。
    *   **语义-物理错位（Semantic-Physical Misalignment）**：静态的多模态融合方法无法在任务执行过程中动态地将高层语义目标（如“将杯子放在架子上”）与底层物理动作精确对齐，导致错误的动作克隆。
*   **研究动机**：为了抑制复合误差，需要一种既能保证动作序列时间上连续、物理上可行，又能在每一步实现细粒度语义-物理对齐的新框架。

### 2. 论文提出的方法论
论文提出了一个名为 **CCoL（Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment）** 的框架，其核心思想是**连续协同学习**与**逐步的语义物理对齐**。

*   **核心组件一：多模态连续协同学习（MCC）**
    *   **目标**：解决动作序列的物理不连续问题，确保轨迹平滑。
    *   **关键技术**：采用**神经常微分方程（Neural ODEs）** 来建模机器人本体感受数据（关节位置等）在隐空间中的连续动态演化。它学习一个微分函数 $f(z(t), t; \psi)$，并通过常微分方程求解器（`odeint`）计算出连续且平滑的隐状态轨迹 $Z_t$，替代了离散的、可能不连贯的编码特征。
    *   **模态融合**：将视觉（ViT特征）、语言（RoBERTa特征）和由MCC产生的连续本体感受特征投影到一个共享的嵌入空间，实现协同学习。

*   **核心组件二：跨模态语义-物理对齐（CSA）**
    *   **目标**：解决语义-物理错位问题，实现细粒度的语义锚定。
    *   **关键技术**：设计了一个**双向交叉注意力机制**。该机制在每一步计算文本嵌入（如动词“按压”、名词“按钮”）与联合的视觉-本体感受特征 $X_t$ 之间的注意力分数。
    *   **对齐过程**：公式为 $F_t(\tilde{l}_t, X_t) = \text{softmax}(...)$，它动态地将语言学符号（如名词）锚定到视觉区域，并将动作指令（如动词）与本体感受状态关联起来，从而生成包含丰富上下文信息的融合特征 $\tilde{F}_t$。为了保持时间连贯性，该机制还引入了位置编码。

*   **动作生成与优化**
    *   **解码器**：一个目标条件解码器，基于融合特征 $\tilde{F}_t$ 预测未来 $k$ 个时间步的动作序列 $a'_{t:t+k}$。
    *   **混合损失函数**：总损失 $\mathcal{L} = \mathcal{L}_{\text{BC}} + \mathcal{E}_{\text{disc}}$。
        *   $\mathcal{L}_{\text{BC}}$ 结合了**重建损失**（使预测动作接近专家动作）和**KL散度损失**（源自条件变分自编码器CVAE框架，用于正则化隐空间）。
        *   $\mathcal{E}_{\text{disc}}$ 是一个**不连续性惩罚项**，直接约束隐状态的变化速率 $dz(t)/dt$ 与NeuralODE预测的速率 $f(z(t), t; \psi)$ 保持一致，从而增强轨迹的平滑性。

### 3. 实验设计
*   **数据集/场景**：
    *   **Aloha MuJoCo**：用于评估双臂协作任务（方块转移、双臂插入），包含脚本和人类两种演示模式。
    *   **RLBench**：用于多场景评估，包含开灯、烤肉、接电话、开瓶等任务。
    *   **Franka Kitchen**：用于评估长时域任务表现，包含单任务（如转旋钮）和多任务组合（如开门+开微波炉）。
    *   **真实世界**：在一台7自由度Franka Emika Panda机器人上，设计了提笔、滑方块、堆方块三个任务，以测试在未见过的或带噪声状态下的泛化能力。

*   **对比方法（Benchmark）**：
    *   **时序建模类**：BCCNN, RT-1, VINN, BeT。
    *   **动作分块/路径点抽象类**：ACT, AWE。
    *   **扩散模型类**：DP, DIC, HDP, 3DDiff。
    *   **表示增强策略类**：R3M, Voltron, MPI。

*   **评估指标**：任务成功率（%）。

### 4. 资源与算力
论文提到了模型训练的算力开销：
*   **GPU型号**：1块 NVIDIA RTX 4090 GPU。
*   **训练时长**：训练时长为 **5.3小时**。
*   **推理速度**：单次动作序列推理时间约为 **0.015秒**（对应策略频率约67Hz），满足实时性要求。

### 5. 实验数量与充分性
实验设计**非常充分和全面**，通过多维度对比验证了方法的有效性。
*   **多场景对比实验**：在3个主流仿真基准（Aloha MuJoCo, RLBench, Franka Kitchen）和1个真实机器人平台上，与超过10种的现有最佳方法（SOTA）进行了横向对比，覆盖了不同任务类型（双臂、多步、长时序）。
*   **消融实验**：系统地移除了CCoL的关键组件，包括：MCC模块、CSA模块、不连续性惩罚项 $\mathcal{E}_{\text{disc}}$、CSA中的注意力机制（替换为平均池化）、本体感受编码器中的注意力机制（替换为TCN）。这清晰地证明了每个模块的贡献。
*   **超参数与定性分析**：探讨了NeuralODE求解器的时间步长对性能的影响，并对轨迹平滑度进行了定量分析（速度和加速度标准差）。还通过注意力归因图进行了定性分析，可视化了语义锚定的过程。
*   **公平性**：在不同仿真环境中，实验设置与对比方法（如AWE, 3DDiff, MPI）保持一致，确保了比较的公平性。

### 6. 论文的主要结论与发现
*   CCoL框架通过**连续协同学习**和**逐步语义-物理对齐**，有效地减轻了行为克隆中的复合误差。
*   该方法在**多个仿真和真实世界任务**中均取得了SOTA性能，尤其在需要精细连续动作和长时域规划的任务上优势明显（相对提升最高达19.2%）。
*   MCC模块是实现**平滑且物理可行轨迹**的关键，而CSA模块则通过动态注意力机制确保了**语义指令与动作的精准对应**，两者协同作用显著优于单一模块。

### 7. 优点
*   **方法创新性强**：首次将Neural ODE用于行为克隆中的连续动作序列建模，以解决物理不连续性问题，并结合交叉注意力实现了细粒度的、动态的语义-物理对齐。
*   **问题剖析深刻**：准确指出了现有方法中“物理不连续”和“语义-物理错位”这两个关键但又常被忽视的问题，并提供了针对性的、协同的解决方案。
*   **实验设计翔实**：实验覆盖面广，跨越多个仿真和真实环境，与众多SOTA基线对比；消融研究彻底，并辅以定性与定量分析，结论高度可信。

### 8. 不足与局限
*   **任务场景相对固定**：实验任务主要为结构化环境下的刚性物体操作，其对非结构化环境、可变形物体或动态复杂交互的泛化能力尚待验证。
*   **对演示数据质量的依赖**：作为BC方法，其性能上限受限于专家演示数据的质量，在噪声非常大或次优的演示数据下的鲁棒性文中虽有涉及（人类演示），但讨论不够深入。
*   **尚未与基础模型整合**：论文在结论中提及未来工作将探索与大语言模型和基础模型的结合，目前的方法是一个独立的、轻量级的框架，在处理开放式世界指令方面可能能力有限。

（完）
