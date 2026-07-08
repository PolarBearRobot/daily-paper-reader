---
title: "FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens"
title_zh: FreqPolicy：具有连续令牌的频率自回归视觉运动策略
authors: "Yiming Zhong, Yumeng Liu, Chuyang Xiao, Zemin Yang, Youzhuo Wang, Yufei Zhu, Ye Shi, Yujing Sun, Xinge Zhu, Yuexin Ma"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=N3UNXzWRRG"
tags: ["query:analysis"]
score: 9.0
evidence: 提出在频域中表示动作以捕获结构化运动模式
tldr: 机器人操作中现有视觉运动策略在动作表示上存在局限性。本文提出FreqPolicy，在频域中表示动作，低频捕获全局运动模式，高频编码局部细节，并且采用连续令牌的频率自回归架构。实验表明该方法能更准确地建模动作结构，提升了操作任务的精度和效率，为动作表示学习提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有方法受限于动作表示和网络架构，无法有效捕获运动结构化本质。
method: 提出在频域中表示动作，并采用频率自回归策略生成连续令牌。
result: 通过频域表示，策略能更好地建模运动模式，生成精确动作。
conclusion: FreqPolicy提供了一种新的动作表示范式，显著改善机器人操作策略的表现。
---

## Abstract
Learning effective visuomotor policies for robotic manipulation is challenging, as it requires generating precise actions while maintaining computational efficiency. Existing methods remain unsatisfactory due to inherent limitations in the essential action representation and the basic network architectures. We observe that representing actions in the frequency domain captures the structured nature of motion more effectively: low-frequency components reflect global movement patterns, while high-frequency components encode fine local details. Additionally, robotic manipulation tasks of varying complexity demand different levels of modeling precision across these frequency bands. Motivated by this, we propose a novel paradigm for visuomotor policy learning that progressively models hierarchical frequency components. To further enhance precision, we introduce continuous latent representations that maintain smoothness and continuity in the action space. Extensive experiments across diverse 2D and 3D robotic manipulation benchmarks demonstrate that our approach outperforms existing methods in both accuracy and efficiency, showcasing the potential of a frequency-domain autoregressive framework with continuous tokens for generalized robotic manipulation.Code is available at https://github.com/4DVLab/Freqpolicy

---

## 论文详细总结（自动生成）

基于所提供的论文摘要与元数据，以下是对《FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens》的结构化深入总结。

## 1. 论文的核心问题与整体含义
- **研究动机**：机器人操作需要同时满足动作精度与计算效率。现有视觉运动策略在动作表示和网络架构上存在固有局限，难以有效捕获运动的结构化本质。
- **核心观察**：频域中的动作表示能更自然地解构运动模式——低频分量反映全局运动趋势，高频分量编码局部精细细节。不同复杂度的操作任务对各频段的建模精度要求不同。
- **整体含义**：通过将动作建模从时域转向频域，并采用频率自回归的方式逐频段生成连续令牌，为机器人操作提供了一种更高效、更精确的策略学习新范式。

## 2. 论文提出的方法论
- **核心思想**：在频域中表示动作序列，利用频率分量的层次化特性，渐进式地建模从粗到细的运动模式。同时引入连续潜在表示，以保持动作空间的平滑性和连续性。
- **关键技术细节**：
  - **频域动作表示**：对动作序列进行时频变换（如离散余弦变换），将动作分解为不同频率的系数。低频系数控制主要运动趋势，高频系数负责微调位姿。
  - **频率自回归架构**：策略网络按从低频到高频的顺序逐步生成每个频率分量的连续令牌。在生成当前频率令牌时，网络可条件化于已生成的低频令牌及视觉观测，实现由整体到局部的层次化动作生成。
  - **连续令牌设计**：不同于将动作离散化为码本索引，直接使用连续向量作为令牌，避免离散化带来的精度损失，并保证生成动作的光滑性。
- **算法流程概览**：输入视觉观测 → 提取特征 → 依次自回归预测每个频率分量的连续值 → 将所有频率分量合并，通过逆变换得到时域动作序列。

## 3. 实验设计
- **测试场景**：论文在多种2D和3D机器人操作基准（benchmarks）上进行了实验，覆盖不同复杂度与动作空间的任务。具体基准名称在摘要中未列出，但从“diverse 2D and 3D robotic manipulation benchmarks”可推断为仿真环境中的标准操作任务集。
- **对比方法**：与现有的视觉运动策略方法进行了比较，旨在验证准确性和效率优势。具体基线方法参见原文。
- **评估指标**：主要关注动作生成的精度与整体任务执行效率。

## 4. 资源与算力
- 论文摘要及提供的元数据中**未明确说明**所使用的GPU型号、数量、训练时长或其他算力细节。该信息需查阅完整原文才能获取。

## 5. 实验数量与充分性
- **实验规模**：摘要强调进行了“广泛实验（extensive experiments）”，覆盖多样的2D和3D基准，并证实方法在精度和效率上均超越现有方法。通常此类研究可能包含多个标准任务集上的主实验、与多种基线的对比以及消融实验（如验证频域表示的有效性、连续令牌的优势、频率自回归顺序的影响等），但具体实验组数未在提供材料中列出。
- **充分性与公平性**：基于文中“outperforms existing methods”的表述及被顶会接收的背景，可推断实验设计具备一定的全面性和客观性。但读者仍需通过原文确认任务选择是否偏见、基线是否被公平调优。

## 6. 论文的主要结论与发现
- 在频域中表示动作能更有效地捕捉运动的结构化模式，使策略生成更精确的动作。
- 频率自回归连续令牌架构能够按频率层次逐步生成动作，复杂任务中兼顾全局规划与局部细节。
- 所提方法在2D和3D机器人操作任务上取得了比现有方法更优的精度和效率，展示了频率域自回归框架在通用机器人操作中的潜力。

## 7. 优点
- **新颖的动作表示**：将频域分析引入视觉运动策略，从结构化角度解决动作建模问题，范式独特。
- **层次化生成**：频率自回归策略与运动行为的层次特性天然契合，有利于模型可解释性和可控性。
- **连续令牌**：避免离散化带来的精度与平滑性损失，更适合精细操作。
- **实验广泛性**：在多种2D和3D任务上验证，且开源代码，增强了可复现性与实用性。

## 8. 不足与局限
- **应用场景边界**：目前实验基于仿真基准，文中未提真实机器人平台上的验证，sim-to-real泛化性能尚不明确。
- **信息缺失导致的局限**：
  - 未提供算力与训练开销，难以评估方法对计算资源的增益或负担。
  - 具体数据集、基线名称及消融实验细节未在摘要中披露，阻碍对实验充分性的精准判断。
- **可能的内在限制**：频域变换与频率分量的划分可能引入额外超参数；对非周期性或非平稳动作的频域假设存在一定局限；连续令牌自回归的生成效率在长序列任务中可能成为瓶颈。
- **对比公平性风险**：无法确认基线方法是否都经过同等程度的调优。

（完）
