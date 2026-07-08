---
title: "D²PPO: Diffusion Policy Policy Optimization with Dispersive Loss"
title_zh: D²PPO：使用分散损失的扩散策略策略优化
authors: "Guowei Zou, Weibing Li, Hejun Wu, Yukun Qian, Yuhang Wang, Haitao Wang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38959/42921"
tags: ["query:analysis"]
score: 9.0
evidence: 通过分散损失正则化学习判别性表征，解决扩散策略中的表征坍缩问题
tldr: D²PPO针对扩散策略在机器人操作中的表征坍缩问题，提出分散损失正则化方法，将批次内所有隐藏表征视为负样本对，迫使网络学习相似观察的判别性表征。实验表明，该方法能有效提升复杂操作任务对细微差异的敏感性，改善动作预测的性能。此工作为提高扩散策略表征质量提供了有效途径。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38959/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 867, \"height\": 890, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38959/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1819, \"height\": 752, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38959/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1826, \"height\": 891, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38959/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 790, \"height\": 378, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38959/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1831, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38959/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1792, \"height\": 847, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38959/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 689, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38959/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1705, \"height\": 496, \"label\": \"Table\"}]"
motivation: 扩散策略存在表征坍缩，相似观察被映射到无法区分的特征，阻碍复杂操作。
method: 提出D²PPO，引入分散损失，将批次内隐藏表征作为负样本对，强制学习判别性表征。
result: 学习到的表征更具判别性，提升了对细微操作变化的敏感度和动作预测准确性。
conclusion: D²PPO有效解决了扩散策略的表征坍缩，为机器人操作学习提供了更好的表征。
---

## Abstract
Diffusion policies excel at robotic manipulation by naturally modeling multimodal action distributions in high-dimensional spaces. Nevertheless, diffusion policies suffer from diffusion representation collapse: semantically similar observations are mapped to indistinguishable features, ultimately impairing their ability to handle subtle but critical variations required for complex robotic manipulation. To address this problem, we propose D²PPO (Diffusion Policy Policy Optimization with Dispersive Loss). D²PPO introduces dispersive loss regularization that combats representation collapse by treating all hidden representations within each batch as negative pairs. D²PPO compels the network to learn discriminative representations of similar observations, thereby enabling the policy to identify subtle yet crucial differences necessary for precise manipulation. In evaluation, we find that early-layer regularization benefits simple tasks, while late-layer regularization sharply enhances performance on complex manipulation tasks. On RoboMimic benchmarks, D²PPO achieves an average improvement of 22.7% in pre-training and 26.1% after fine-tuning, setting new SOTA results. In comparison with SOTA, the results of real-world experiments on a Franka Emika Panda robot show the excitingly high success rate of our method. The superiority of our method is especially evident in complex tasks.

---

## 论文详细总结（自动生成）

好的，以下是根据您提供的论文内容生成的结构化中文总结。

### 1. 论文的核心问题与整体含义
- **研究所针对的问题**：论文指出，尽管扩散策略（Diffusion Policy）在机器人操作中表现出色，但它们会遭遇**“扩散表征坍缩（Diffusion Representation Collapse）”**的问题。具体表现为，模型会将语义上相似但需要不同动作的观察映射到难以区分的特征，导致在需要处理细微差异的复杂任务中（如精确抓取）表现不佳或失败。
- **研究的动机与意义**：为了解决上述关键瓶颈，本文旨在提升扩散策略的特征辨识能力。通过引入一种新的表征正则化技术，迫使模型学习到更有辨别力的特征，从而能够区分相似观测中的关键性差异，最终提升在复杂操作任务上的成功率。这项工作的核心是架起了表征学习与扩散策略之间的桥梁，以提高机器人的精细操作能力。

### 2. 论文提出的方法论
- **核心思想**：提出一个名为 **D²PPO (Diffusion Policy Policy Optimization with Dispersive Loss)** 的两阶段训练框架。其核心创新是引入一种 **“分散损失（Dispersive Loss）”** 正则化项，在预训练时将其与标准扩散损失结合，以防止表征坍缩。这种分散损失被描述为一种**“无正样本对的对比学习损失”**，它通过将同一批次内的所有隐藏表征都视为“负样本对”，强制它们在隐空间中均匀分散开来。
- **关键技术细节**：
  - **两阶段训练范式**：
    1.  **第一阶段（预训练）**：在模仿学习的基础上，使用带有分散损失的扩散模型进行预训练，目标是学习到更具辨别力的视觉-动作表征。
    2.  **第二阶段（微调）**：将预训练好的策略作为初始模型，使用策略梯度算法（PPO）进行在线强化学习微调，以最大化任务成功率。
- **算法流程与公式**：
  - **预训练总目标**：`L_pre-train = L_diff + λ * L_disp`，其中 `L_diff` 是标准的扩散去噪损失，`L_disp` 是提出的分散损失，`λ` 是平衡系数。
  - **分散损失（L_disp）**的定义：源自于对标准对比学习损失（InfoNCE）的改造，即**直接去除正样本对齐项，仅保留样本间的分散项**。目标是最大化批次内所有样本对之间的距离。`L_disp = log(E[exp(-D(z_i, z_j) / τ)])`。
  - **三种变体**：论文基于距离计算方式的不同，探索了三种分散损失的变体：
    1.  **InfoNCE-L2**：基于L2欧几里得距离。
    2.  **InfoNCE-Cosine**：基于余弦距离。
    3.  **Hinge损失**：基于合页损失，显式地强制样本对之间保持一个最小距离间隔。
  - **微调目标**：使用重要性采样，仅在部分去噪时间步上计算策略梯度进行更新，以提高效率。梯度计算方式为：对选定的去噪步 `k`，计算 `∇θ log p(a_{t}^{k-1} | a_t^k, s_t)` 并乘以优势估计 `A_t^(k)`。

### 3. 实验设计
- **数据集/场景**：
  - 仿真实验：使用 **RoboMimic** 基准测试中的四个任务，按复杂度从低到高排列为：**Lift（举起）**、**Can（罐子）**、**Square（方形块）**、**Transport（运输）**。
  - 真实世界实验：在 **Franka Emika Panda** 机器人上进行了实际部署验证。
- **对比方法**：
  - 表2中，D²PPO与众多强基线方法进行了对比，包括 **LSTM-GMM, IBC, BET, DiffusionPolicy-C/T, DPPO, MTIL** 等。D²PPO在微调后的平均成功率上达到了最高的0.94，取得了最优（SOTA）结果。
  - 预训练阶段主要采用 **DPPO** 作为基线进行对比。
  - 在微调阶段，基线方法包括DPPO和基于高斯分布的策略。
- **消融研究**：对比了三种分散损失变体，并研究了将其应用于网络的不同层（早期、中期、晚期）的影响，以及不同损失系数 `λ` 的效果。

### 4. 资源与算力
- 论文提供的文本中，**未明确提及**进行实验所使用的具体GPU型号、数量或训练总时长等算力资源相关信息。

### 5. 实验数量与充分性
- **实验数量**：实验设计较为全面，覆盖了多个层次的验证：
  1.  **预训练实验**：在4个任务上评估了多种（至少5种）分散损失配置（3种变体 × 不同层位置）的性能。
  2.  **微调实验**：在4个任务上，将最佳预训练模型与多个基线方法（表2中的9种方法）进行了对比。
  3.  **消融实验**：详细研究了关键超参数 `λ` 对任务性能的非单调影响。
  4.  **真机实验**：在真实机器人上对4个任务进行了各100次试验的验证。
- **实验充分性与公平性**：
  - **充分性**：实验从仿真到真实世界，从预训练到微调，并包含了对方法内部机制（层位置、损失函数变体）的深入消融分析，整体来看非常充分。
  - **客观与公平性**：对比的基线方法广泛且包括了当时的先进方法。实验结果表明，D²PPO不仅在简单任务上表现良好，其优势更是在复杂任务上尤为突出，这有力地支撑了其“解决复杂任务表征坍缩”的核心论点。实验设定是客观和公平的。

### 6. 论文的主要结论与发现
- **分散损失有效缓解表征坍缩**：通过在预训练阶段引入分散损失，D²PPO能学习到更具辨别力的特征，显著改善了模型对相似但关键性差异的识别能力，从而解决了表征坍缩问题。
- **任务复杂度与正则化层位置相关**：简单任务受益于在网络**早期层**应用正则化，而复杂任务则从**晚期层**的正则化中获得显著提升。分散损失的有效性与任务复杂度呈强正相关（R²=0.92）。
- **性能达到最优**：D²PPO在 RoboMimic 基准上取得了SOTA性能。相比于基线方法，预训练阶段平均提升**22.7%**，微调后平均提升**26.1%**，最终平均成功率达到**94%**。
- **真实世界有效性**：在Franka机器人上的实机实验证实了D²PPO的实用性，尤其在Transport此类高难度任务上实现了巨大突破（DPPO: 45% vs. D²PPO: 70%）。

### 7. 优点
- **方法创新与简洁性**：提出的“无正样本对”分散损失概念新颖，直接针对扩散策略的表征坍缩问题，且实现上是一个即插即用的损失项，无需额外网络、数据或预训练阶段。
- **深刻的洞察力**：系统性地揭示了“表征坍缩”是扩散策略在复杂任务中失败的原因，并发现正则化网络层位置与任务复杂度之间的关联，为后续研究提供了有价值的指导。
- **实验验证充分扎实**：实验设计环环相扣，从问题分析到方法提出，再到仿真和真机验证，逻辑清晰，论据充分，尤其是在困难任务上的大幅性能提升极具说服力。
- **理论与实践的桥梁**：成功将表征学习领域的先进思想应用于机器人策略学习范畴，解决了实际应用中的具体难题。

### 8. 不足与局限
- **任务范围有限**：实验主要集中在RoboMimic的桌面级操作任务，未来研究可探索该方法在导航、灵巧手操作等其他机器人领域的泛化能力。
- **超参数敏感性**：消融实验显示，超参数 `λ` 对性能影响显著，值过大或过小都可能导致性能下降，实际应用时可能需要为不同任务进行精心的超参数调优。
- **两阶段训练成本**：虽然不在第一阶段引入额外模型，但“预训练+微调”的两阶段范式相比于端到端方法，整体训练流程可能更为耗时和复杂。
- **真机部署的适应性**：从仿真到真机迁移的有效性已验证，但论文未深入探讨在动态变化、非结构化真实环境中的鲁棒性和长期运行稳定性。

（完）
