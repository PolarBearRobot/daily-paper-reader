---
title: Universal Actions for Enhanced Embodied Foundation Models
title_zh: 通用动作增强的具身基础模型
authors: "Zheng, Jinliang, Li, Jianxiong, Liu, Dongxiu, Zheng, Yinan, Wang, Zhihao, Ou, Zhonghong, Liu, Yu, Liu, Jingjing, Zhang, Ya-Qin, Zhan, Xianyuan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zheng_Universal_Actions_for_Enhanced_Embodied_Foundation_Models_CVPR_2025_paper.pdf"
tags: ["query:model"]
score: 10.0
evidence: 通用动作空间捕捉不同机器人间的通用行为，实现异构跨本体数据训练
tldr: 针对不同机器人因本体和控制界面差异导致动作空间异构，阻碍跨本体数据训练具身基础模型的问题，提出UniAct框架，学习通用动作空间捕捉跨机器人的通用行为。实验表明该方法能有效利用异构的众包具身数据集，显著提升具身基础模型的性能和跨本体泛化能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 755, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1691, \"height\": 951, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1714, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1694, \"height\": 536, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 874, \"height\": 273, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1745, \"height\": 366, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1703, \"height\": 618, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1712, \"height\": 539, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 874, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zheng-universal-actions-for-enhanced-embodied-foundation-models-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 871, \"height\": 257, \"label\": \"Table\"}]"
motivation: 跨机器人动作空间异构阻碍大规模、多样化数据训练具身基础模型。
method: 提出UniAct，在通用动作空间中学习捕捉不同机器人通用行为的表示，统一异构动作。
result: 能有效利用多种机器人数据集训练，模型泛化能力大幅提升。
conclusion: 通用动作空间为训练具身基础模型提供了可扩展的框架，解决了跨本体数据协同的关键挑战。
---

## Abstract
Training on diverse, internet-scale data is a key factor in the success of recent large foundation models. Yet, using the same recipe for building embodied agents has faced noticeable difficulties. Despite the availability of many crowd-sourced embodied datasets, their action spaces often exhibit significant heterogeneity due to distinct physical embodiment and control interfaces for different robots, causing substantial challenges in developing embodied foundation models using cross-embodiment data. In this paper, we introduce UniAct, a new embodied foundation modeling framework operating in the Universal Action Space. Our learned universal actions capture the generic behaviors across diverse robots by exploiting their shared structural features, and enable enhanced cross-domain data utilization and cross-embodiment generalizations by eliminating the notorious heterogeneity. Moreover, the universal actions can be efficiently translated back to heterogeneous actionable commands by simply adding embodiment-specific details, from which fast adaptation to new robots becomes simple and straightforward. Our 0.5B instantiation of UniAct outperforms 14X larger SOTA embodied foundation models in extensive evaluations on various real-world and simulation robots, showcasing exceptional cross-embodiment control and adaptation capability, highlighting the crucial benefit of adopting universal actions.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- 当前大型基础模型在自然语言处理和计算机视觉等领域取得成功的关键在于使用互联网规模的多样化数据进行训练。
- 然而，将同样的方法应用于具身智能体时面临巨大挑战，主要原因是不同机器人的物理本体（如自由度、构型）和控制接口（如末端执行器位置、速度、关节扭矩等）差异巨大，导致动作空间存在显著异构性。
- 这种异构性使得不同来源的具身数据分布在原本物理空间中几乎不相交的流形上，难以有效整合和共享，严重阻碍了通用具身基础模型的发展。
- 现有方法要么粗暴地将不同动作空间视为等价并进行相同离散化或归一化处理，导致动作编码冲突；要么简单聚合所有动作空间，未能挖掘不同机器人动作之间的内在共性。
- 因此，本文的核心问题是：如何从大规模异构的具身数据中提取出通用的行为表征，以消除动作空间异构性，实现跨本体数据的有效利用和模型泛化。

### 2. 论文提出的方法论

- **核心思想**：构建一个**通用动作空间（Universal Action Space）**，将不同机器人的异构控制信号抽象为共享的离散原子行为（universal actions），这些原子行为不受具体本体和控制接口的约束，从而在统一空间中实现跨机器人的行为共享与泛化。
- **关键技术细节**：
  - **离散码本表示**：通用动作空间建模为一个向量量化码本 \( \mathbf{U} \in \mathbb{R}^{N \times D} \)，包含 \( N \) 个 \( D \) 维向量，每个向量代表一种通用的原子行为（如“向前移动”）。
  - **通用动作提取器**：利用一个共享的视觉语言模型（VLM，如LLaVA-OneVision-0.5B）作为提取器，根据观测 \( o \) 和任务目标 \( g \)（如语言指令）输出选择每个通用动作的概率 \( p(u|o, g) \)。通过Gumbel-Softmax重参数化技巧进行可微分选择，得到当前步的通用动作 \( \mathbf{u}^* \)：
    \[
    w_i = \frac{\exp((\log p(\mathbf{u}_i|o, g) + \epsilon_i)/\tau)}{\sum_k \exp((\log p(\mathbf{u}_k|o, g) + \epsilon_k)/\tau)}, \quad \mathbf{u}^* = \sum_i w_i \mathbf{u}_i
    \]
    其中 \( \epsilon_i \) 为Gumbel噪声，\( \tau \) 为温度系数，训练初期设置较高以探索，后期衰减。
  - **异构解码器**：为每种机器人本体设计轻量级解码头 \( h_k \)，以通用动作 \( \mathbf{u}^* \) 和观测 \( o \) 为输入，输出该本体特定的控制命令 \( \hat{a}^{(k)} \)。解码头通常为简单的MLP网络，这样强迫大部分学习集中在通用动作提取上，保证泛化能力。
  - **训练目标**：在 \( K \) 个异构数据集上联合优化码本、提取器和各解码头，最小化行为克隆损失（如交叉熵或MSE）：
    \[
    \min_{\mathbf{U}, \theta} \sum_{k=1}^K \mathbb{E}_{\tau_i \in \mathcal{D}_k, a_i \in \tau_i} \mathcal{L}_k(\hat{a}^{(k)}, a_i)
    \]
- **快速适应新机器人**：冻结已学好的通用动作空间和提取器，仅需为新机器人训练新的轻量解码头（MLP），即可快速适配新的控制接口，所需参数量极少（例如仅4M/500M）。

### 3. 实验设计

- **数据集/场景**：
  - 训练数据来自多个开源机器人数据集：Open-X Embodiment、LIBERO、DROID，共包含来自28种不同本体的约100万条演示数据，保留了原始的动作异构性（未进行统一化清洗）。
  - 评估场景包括：真实世界的WidowX机器人（覆盖视觉泛化、运动泛化、物理泛化、语义泛化和语言基础等19个任务）、仿真中的Franka机器人（LIBERO基准，含130个任务）、全新的AIRBOT真实机器人（快速适应实验），以及双手机器人（Bimanual AIRBOT）任务。
- **对比方法**：
  - Octo（0.1B参数，基于Transformer的通用策略）
  - CrossFormer（0.1B，跨本体策略）
  - OpenVLA（7B，基于自回归离散动作的VLA模型）
  - LAPA（7B，通过视频帧间变化构建隐动作的VLM，需额外微调生成真动作）
  - 在快速适应实验中与Octo和OpenVLA对比微调效率和最终性能。
- **下游任务与评估指标**：
  - 真实WidowX机器人：每个任务10次试验，报告平均成功率。
  - LIBERO仿真基准：五个测试套件（Spatial, Object, Goal, Long, 90），共计130个任务，每个任务20次试验，报告平均成功率。
  - 快速适应实验：AIRBOT机器人，四种控制接口（相对/绝对末端位置，相对/绝对关节位置），简单与困难两种任务设置。

### 4. 资源与算力

- **计算资源**：训练使用64块A100 GPU，借助DeepSpeed框架进行分布式训练。
- **训练时长**：总训练时间约10天，处理约100万条演示数据。
- 文中明确给出了GPU型号、数量和训练持续时间，算力消耗较为庞大，但符合基础模型训练规模。

### 5. 实验数量与充分性

- **主要实验组数**（粗略统计）：
  1. 真实WidowX机器人上的5种泛化维度×19个任务，共190次评估rollout。
  2. 仿真LIBERO基准5个套件×130个任务，每个任务20次试验，共2600次评估rollout。
  3. AIRBOT快速适应实验：4种控制接口×2种任务难度（easy & hard），共8组对比。
  4. 双手机器人ACT解码头快速适应实验（4个任务）。
  5. 通用动作空间分析实验：手动检查256个码本行为一致性（约40%表现完全一致），并通过人工控制机器人执行通用动作序列验证可解释性。
  6. 通用动作利用率统计：计算不同机器人、不同任务间码本使用分布的JS散度。
- **评估充分性与公平性**：
  - 实验覆盖了真实世界和仿真、单臂与双臂、已知与未知机器人、多种控制接口，规模较大。
  - 对比方法包含了不同规模（0.1B、0.5B、7B）的SOTA模型，且对于基线模型在LIBERO上进行了公平微调（使用相同数据量、任务和图像质量），快速适应实验中基线模型也根据官方要求调至收敛。
  - 消融实验（如轻量解码头的作用）可通过与全参数微调的对比间接体现，但文中未单独设置系统性消融研究，主要依赖与大型模型的性能对比证明有效性。
  - 总体而言，实验数量充分，对比客观，覆盖维度较广，能够支撑核心论点。

### 6. 论文的主要结论与发现

- 在通用动作空间中学习跨机器人原子行为，能够有效消除动作异构性，使模型可以从多个异构数据源中提取共享技能，显著提升具身基础模型的跨本体泛化能力。
- 仅0.5B参数的UniAct在多数真实和仿真任务上超越了14倍大小的OpenVLA（7B），甚至在视觉、运动和物理泛化任务上大幅领先，展示了通用动作的高效性。
- 学习到的通用动作具有语义一致性：相同通用动作解码到不同机器人上表现出相似的高级行为（如“推”“抓”），且码本利用率主要由任务类型而非机器人本体决定。
- 快速适应新机器人时，仅需训练少量参数（0.8%）的解码头即可达到甚至超越需要全参数或大比例参数微调的基线方法，表明通用动作提取器已捕获了本体无关的行为知识。
- 通用动作提取器可作为一种“动作标记化器”，支持在离散通用动作空间中进行规划，为未来更大规模的具身基础模型提供了构建基础。

### 7. 优点

- **新颖的视角**：首次提出通过向量量化码本学习与本体无关的通用动作空间，从任务进展角度提取共享原子行为，而非简单聚合动作空间或仅依赖视觉变化。
- **有效的异构融合**：利用信息瓶颈原理，强制VLM在统一码本中寻找跨机器人的共性行为，避免了手工设计统一动作空间的繁琐。
- **轻量化适配**：通过冻结主干、仅训练轻量MLP解码头，实现了对新机器人的快速、低成本部署，参数量显著低于其他方法。
- **实验扎实全面**：评估覆盖多平台、多任务、多泛化维度，并与多个SOTA模型对比，且在大规模异构真实数据上进行了训练，验证了方法的实用性和可扩展性。
- **解释性分析**：通过手动检查通用动作的解码行为和使用分布，证明了所学空间确实捕捉到了有意义的通用技能。

### 8. 不足与局限

- **模型规模有限**：当前使用0.5B参数的VLM，可能限制了复杂语义理解和长程推理能力的上限，而大型模型（如OpenVLA 7B）在语义泛化任务上仍具有优势。未来需要扩展模型规模。
- **本体覆盖面**：主要实验集中在单臂操作机器人，对于双手机器人、移动机器人、自动驾驶等更广泛的具身形态仅进行了初步的双臂实验，仍需进一步验证其通用性。
- **训练对预训练VLM的依赖**：通用动作提取器基于现成的VLM，其效果可能受限于预训练模型的质量。若换用其他VLM，通用动作的语义质量需重新评估。
- **码本大小固定**：码本维度（\( N=256, D=128 \)）是预先设定的超参数，可能无法完美涵盖所有原子行为粒度，且如何自动确定最优码本大小未讨论。
- **可能的安全与可靠性**：直接通过选择通用动作ID控制机器人（“playing with it”）可能存在风险，需考虑安全约束。
- **数据偏差**：训练数据仍主要来自常见的机器人数据集（如Bridge、LIBERO），可能包含特定的场景偏见，由数据驱动得到的通用动作是否对所有新环境都适用有待考察。

（完）
