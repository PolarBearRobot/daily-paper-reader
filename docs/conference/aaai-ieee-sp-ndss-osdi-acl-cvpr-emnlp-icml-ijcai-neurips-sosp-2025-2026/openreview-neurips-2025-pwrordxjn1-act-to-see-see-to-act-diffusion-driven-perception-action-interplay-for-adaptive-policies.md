---
title: "Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies"
title_zh: 为看而做，为做而看：扩散驱动的感知-动作交互自适应策略
authors: "Jing Wang, Weiting Peng, Jing Tang, Zeyu Gong, Xihua Wang, Bo Tao, Li cheng"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=PWRORdXJN1"
tags: ["query:analysis"]
score: 8.0
evidence: 统一表示学习显式建模感知与动作的动态交互。
tldr: 针对模仿学习中感知与动作解耦忽略因果互惠性的问题，DP-AG提出动作引导扩散策略，通过变分推断编码观测并利用动作引导随机微分方程演化潜在状态，显式建模感知-动作双向交互学习，在真实机器人操作任务中展现了更高的适应性和鲁棒性，为学习更有效的动作表征提供了新路径。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有模仿学习解耦感知与动作，忽略了人类自适应行为中感知与执行的因果互惠性。
method: 提出DP-AG，利用变分推断和动作引导SDE在潜在空间中建模感知-动作动态交互。
result: 在真实机器人操作任务中，DP-AG展示了更强的自适应能力和鲁棒性。
conclusion: 显式建模感知-动作双向交互能显著提升策略的学习效率和泛化性能。
---

## Abstract
Existing imitation learning methods decouple perception and action, which overlooks the causal reciprocity between sensory representations and action execution that humans naturally leverage for adaptive behaviors. To bridge this gap, we introduce Action-Guided Diffusion Policy (DP-AG), a unified representation learning that explicitly models a dynamic interplay between perception and action through probabilistic latent dynamics. DP-AG encodes latent observations into a Gaussian posterior via variational inference and evolves them using an action-guided SDE, where the Vector–Jacobian Product (VJP) of the diffusion policy's noise predictions serves as a structured stochastic force driving latent updates. To promote bidirectional learning between perception and action, we introduce a cycle-consistent contrastive loss that organizes the gradient flow of the noise predictor into a coherent perception–action loop, enforcing mutually consistent transitions in both latent updates and action refinements. Theoretically, we derive a variational lower bound for the action-guided SDE, and prove that the contrastive objective enhances continuity in both latent and action trajectories. Empirically, DP-AG significantly outperforms state-of-the-art methods across simulation benchmarks and real-world UR5 manipulation tasks. As a result, our DP-AG offers a promising step toward bridging biological adaptability and artificial policy learning. Code is available on our project website: https://jingwang18.github.io/dp-ag.github.io/.

---

## 论文详细总结（自动生成）

# 论文总结：《Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies》（行动以视，视以行动：扩散驱动的感知-动作交互自适应策略）

## 1. 论文的核心问题与整体含义

- **研究动机与背景**  
  现有的模仿学习方法通常将**感知（observation）与动作（action）解耦**处理，忽略了人类在自适应行为中天然利用的**感官表征与动作执行之间的因果互惠性**。  
  人类在操作过程中会主动调整感知以适应动作需求，同时根据感知反馈精调动作，这种“看为了做、做为了看”的双向交互是形成灵活策略的关键，但当前策略学习却缺失了对这一动态过程的显式建模。

- **整体含义**  
  论文旨在填补这一空白，提出**动作引导扩散策略（Action-Guided Diffusion Policy, DP-AG）**，通过统一的表示学习框架，将感知与动作的**动态交互**显式地嵌入到概率潜在动力学中，从而提升策略的自适应性和鲁棒性，为连接生物适应性与人工策略学习迈出重要一步。

## 2. 论文提出的方法论

- **核心思想**  
  DP-AG 将观测编码为潜在变量，并在潜在空间中用**动作引导的随机微分方程（SDE）** 推演潜在状态的演化，使得动作信息能够反向塑造感知过程，同时感知演化也能正向指导动作的精细化。引入**循环一致性对比损失**来强化感知与动作之间的相互一致性。

- **关键技术细节**
  - **变分推断编码观测**：将原始观测（如图像）通过编码器得到潜在观测的高斯后验分布（均值和方差）。
  - **动作引导 SDE**：潜在状态按照一个 SDE 进行演化，其中的漂移项或扩散项由**扩散策略的噪声预测的向量-雅可比乘积（Vector-Jacobian Product, VJP）** 构成，作为结构化的随机力，驱动潜在状态的更新。这使得动作预测梯度能够直接影响潜在空间的动态。
  - **循环一致性对比损失**：在训练时，强迫潜在状态更新与动作细化形成一致环路——组织噪声预测器的梯度流，使其在潜在轨迹和动作轨迹上产生**相互一致的变换**，从而加强感知与动作的双向耦合。
  - **理论支撑**：论文推导了动作引导 SDE 的**变分下界**，并证明了对比目标能够增强潜在轨迹和动作轨迹的**连续性**。

- **算法流程（概括）**  
  1. 编码观测为潜在分布 \(q(z_t | o_t)\)。  
  2. 从分布中采样潜在变量，与当前动作预测结合，通过 SDE 推演下一时刻的潜在变量 \(z_{t+1}\)，其中 SDE 项利用动作噪声预测的 VJP。  
  3. 利用潜在变量解码或直接预测精炼后的动作。  
  4. 训练时额外施加循环一致性对比损失，约束感知更新与动作更新形成闭环。

## 3. 实验设计

- **使用的数据集 / 场景**  
  - **仿真基准**（Simulation benchmarks）：论文未列出具体名称，但从“simulation benchmarks”推测，可能包含了常见的机器人操作仿真任务（如 Robomimic、Meta-World 等）。  
  - **真实机器人操作任务**：基于 **UR5** 机械臂的真实世界操作任务（如抓取、放置等）。

- **Benchmark 与对比方法**  
  - 对标的是当前最先进的模仿学习方法（state-of-the-art imitation learning methods），文中未列出具体方法名称，但从摘要可知 DP-AG 在所有对比实验中均取得显著提升。
  - 对比基线可能包括：行为克隆（BC）、隐式行为克隆（如扩散策略 Diffusion Policy）、Transformer 策略等，但确切的对比方法需参考原文。

## 4. 资源与算力

- **论文提供的文本中未明确说明算力资源。**  
  摘要和元数据均未提及所用 GPU 型号、数量、训练时长等信息。从方法本身看，扩散策略和变分推断通常需要较大的计算资源，真实机器人实验也隐含了一定的训练成本，但具体细节缺失。

## 5. 实验数量与充分性

- **实验数量**  
  基于摘要信息，论文至少包含**仿真基准实验**和**真实 UR5 操作任务**两大类，每一类下很可能包含多个子任务（如不同技能或环境扰动）。此外，可能还设计了**消融实验**（如验证循环一致性损失、动作引导 SDE 模块的有效性）。  
- **充分性与客观性**  
  - **充分性**：同时覆盖仿真和真实环境，能够展示方法的泛化能力。若有消融研究，则可进一步验证各个组件的贡献，结构上较为完整。  
  - **客观性与公平性**：摘要宣称“显著优于最先进方法”，表明对比时使用了相同的任务设置和评价指标，实验设计应具公平性。由于缺乏详细数据，无法判断是否存在偏差风险，但以 NeurIPS 录用论文的水准，通常实验较为规范。

## 6. 论文的主要结论与发现

- **显式建模感知-动作双向交互能够显著提升策略的学习效率和泛化性能。**  
- DP-AG 在仿真基准和真实机器人操作任务中均**表现出更强的自适应能力和鲁棒性**。  
- 理论上前述的变分下界和轨迹连续性证明了方法的合理性。  
- 这项工作**为学习更有效的动作表征提供了新路径**，并朝着融合生物适应性与人工策略学习的目标迈进一步。

## 7. 优点（方法或实验设计亮点）

- **新颖的统一表示框架**：首次将感知与动作的双向动态耦合建模为动作引导的随机微分方程，超越了传统的单向解耦思路。  
- **巧妙的梯度回传机制**：通过 VJP 将动作噪声预测的梯度信息注入潜在状态演化，实现了动作→感知的反馈。  
- **双向一致性约束**：循环一致性对比损失确保了感知更新与动作精细化的协调，增强了整体表征的连贯性。  
- **理论与实证结合**：既有变分下界推导做支撑，又在仿真和真实机器人上进行了验证，说服力较强。  
- **开源可复现**：提供了项目网站与代码，促进社区复现与改进。

## 8. 不足与局限

- **计算开销可能较高**：扩散模型本身推理步骤多，加上变分推断和 SDE 模拟，可能导致实时性受限，难以直接应用于高频控制场景。  
- **实验细节未公开**：从摘要无法得知仿真的具体任务、对比方法的名称及消融实验结果，难以评估其具体优势幅度和适用范围。  
- **泛化边界未知**：在 UR5 上完成的任务种类、环境扰动程度等均未说明，泛化到全新场景或更复杂操作（如长序列、多步骤）的能力有待进一步验证。  
- **对感知编码器依赖较强**：方法依赖于编码器给出的潜在后验质量，若观测包含噪声或遮挡，可能影响 SDE 的动力演化。论文未讨论这一鲁棒性问题。  
- **对比的全面性可能不足**：未知是否对比了其他引入双向交互的模仿学习方法，或仅与主流方法对比，存在选择性对比的偏差风险。

（完）
