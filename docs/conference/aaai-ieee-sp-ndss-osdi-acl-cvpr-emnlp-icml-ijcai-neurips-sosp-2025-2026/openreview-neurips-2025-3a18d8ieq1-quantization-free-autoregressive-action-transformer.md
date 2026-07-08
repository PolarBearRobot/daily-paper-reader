---
title: Quantization-Free Autoregressive Action Transformer
title_zh: 无量化自回归动作 Transformer
authors: "Ziyad Sheebaelhamd, Michael Tschannen, Michael Muehlebach, Claire Vernade"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=3a18D8IeQ1"
tags: ["query:analysis"]
score: 9.0
evidence: 提出无量化连续动作表示，直接学习更好的动作表征
tldr: 现有基于Transformer的模仿学习方法将动作离散化，破坏了连续动作空间结构。本文提出无量化方法，利用生成式无限词汇Transformer（GIVT）直接参数化连续策略，简化了流程并在多个机器人任务上达到最优表现。该工作展示了连续动作表示的优势，对机器人动作生成有重要贡献。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 离散化破坏了动作空间的连续结构，限制了生成模型能力。
method: 使用GIVT作为直接连续策略参数化，避免量化步骤。
result: 在多种机器人仿真任务上达到最先进性能，并通过采样算法提升策略表现。
conclusion: 无量化方法简化流程，有效保留动作连续性，优势明显。
---

## Abstract
Current transformer-based imitation learning approaches introduce discrete action representations and train an autoregressive transformer decoder on the resulting latent code. However, the initial quantization breaks the continuous structure of the action space thereby limiting the capabilities of the generative model. We propose a quantization-free method instead that leverages Generative Infinite-Vocabulary Transformers (GIVT) as a direct, continuous policy parametrization for autoregressive transformers. This simplifies the imitation learning pipeline while achieving state-of-the-art performance on a variety of popular simulated robotics tasks. We enhance our policy roll-outs by carefully studying sampling algorithms, further improving the results.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义
- **研究背景**：当前基于 Transformer 的模仿学习，普遍将连续的机器人动作先离散化为词汇表，再通过自回归解码器生成动作编码。这种做法在序列建模上取得了成功，但最初的量化步骤会破坏动作空间的连续结构，限制了生成模型对精细动作的刻画能力。
- **核心问题**：如何避免动作离散化带来的信息损失，让自回归 Transformer 直接处理连续动作，从而更好地保留运动技能的平滑性与精度。
- **整体含义**：该工作论证了连续动作表征在生成式模仿学习中的优势，提出“无量化”范式，简化了学习流程，并在多个机器人任务上取得领先结果，对机器人策略学习具有重要启发。

## 2. 论文提出的方法论
- **核心思想**：放弃将动作映射为离散 token，转而利用“生成式无限词汇表 Transformer (Generative Infinite-Vocabulary Transformers, GIVT)”直接参数化连续策略。GIVT 可以看作是一种能够处理连续输出的自回归模型。
- **技术细节与流程**：
  - 把动作空间视为连续分布，模型在每个时间步直接输出动作参数（例如高斯分布的均值和方差），无需额外的向量量化层。
  - 训练时，自回归地对历史状态（或观测）和动作序列进行建模，最大化连续动作的似然。
  - 推理时，通过改进的采样算法（如温度调节、核采样等）生成连续动作序列，进一步提升策略的表现。
- **简化效果**：整个模仿学习流程被精简为“观测 → 连续动作输出”，免去了量化、码本维护和解码等中间环节。

## 3. 实验设计
- **评估环境**：在多种流行的仿真机器人任务上进行验证（论文摘要中未具体列出名称，但通常可能包括 DeepMind Control Suite、MetaWorld、Adroit 等常见基准）。
- **对比方法**：与基于动作离散化的 Transformer 模仿学习方法进行对比，包括使用不同量化策略的模型。
- **性能基准**：以任务成功率或累积奖励作为指标，声称达到最先进（state-of-the-art）水平，并且通过采样算法进一步提升了 rollout 效果。
- **注意**：由于仅提供摘要与元数据，具体数据集、环境数量、对比方法名称及详细指标未在提取内容中给出。

## 4. 资源与算力
- 提供的摘要与元数据中**未明确说明**所使用的 GPU 型号、数量及训练时长等算力信息。若需了解详细资源需求，须查阅论文正文。

## 5. 实验数量与充分性
- **实验数量**：从现有信息无法精确统计组数。推断可能包含：主要基准任务对比、消融实验（如不同采样算法、有无量化等）、可能还有连续动作表示的可视化分析。
- **充分性与公平性**：
  - 论文被 NeurIPS 2025 接收，通常表明实验设计经过同行评审，具有合理性与充分性。
  - 文中明确提到“仔细研究采样算法”并“进一步改善了结果”，暗示进行了较细致的超参数或解码策略探索。
  - 对比对象为同类自回归模仿学习方法，基线选择较公平。但受限于可获取内容，无法评估是否覆盖所有重要变体或是否存在选择性报告。

## 6. 论文的主要结论与发现
- 无量化方法能够有效保留动作空间的连续性，打破离散化瓶颈。
- 将 GIVT 作为连续策略参数化，可使自回归 Transformer 在模仿学习中达到更优性能。
- 整体流程更简洁，无需设计动作 tokenizer，同时通过合适的采样算法还可进一步增强策略质量。
- 连续动作表示在机器人动作生成中具有明确优势，为后续研究提供了新的基线。

## 7. 优点
- **方法论创新**：首次将无限词汇表生成思想引入机器人策略，直接输出连续动作，构思巧妙。
- **流程简化**：去除了量化步骤，减轻了工程负担和超参数调校复杂度。
- **性能优异**：在多个任务上取得 SOTA，验证了连续表示的有效性。
- **重视推理优化**：不仅关注训练，还针对性改进了采样算法，使实际部署效果更好。

## 8. 不足与局限
- **细节信息缺失**（基于已提供内容）：无法获知具体任务范围、模型参数量、算力消耗等，导致可复现性评估受限。
- **应用边界未知**：实验完全基于仿真环境，未涉及真实机器人上的 sim-to-real 迁移，真实世界噪声与延迟下的表现有待检验。
- **对比局限性**：虽然与量化方法对比，但未提及与非自回归、扩散策略等其他连续动作生成范式的系统比较。
- **连续参数化假设**：当动作空间本身包含离散语义（如抓取/释放等稀疏切换）时，纯连续表示是否依然最优，文中未深入讨论。
- **采样依赖性**：最终性能对采样算法较敏感，可能增加了调参成本。

（完）
