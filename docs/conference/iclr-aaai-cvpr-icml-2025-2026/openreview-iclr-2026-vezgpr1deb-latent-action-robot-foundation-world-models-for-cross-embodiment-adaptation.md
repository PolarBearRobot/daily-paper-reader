---
title: Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation
title_zh: 跨本体自适应的潜在动作机器人基础世界模型
authors: "Huang Huang, Sriram Yenamandra, Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan, Tsung-Yen Yang, Akshara Rai, Michael Rabbat, Li Fei-Fei, Jiajun Wu, Tingfan Wu, Franziska Meier"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=vEZgPr1deb"
tags: ["query:model"]
score: 9.0
evidence: 用于跨本体机器人世界模型的统一潜在动作空间
tldr: 针对不同机器人本体动作空间差异导致世界模型难以跨本体泛化的问题，提出LAC-WM，学习一个统一的潜在动作空间，使得世界模型能在不同本体间共享知识，实验表明其在未见本体上的适应性能优于基于显式动作标签的模型。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 机器人本体和动作空间的多样性阻碍了世界模型的跨本体泛化。
method: 提出LAC-WM，在统一的潜在动作空间中操作，实现跨本体的知识共享与适应。
result: 与基于显式标签的基线模型相比，LAC-WM在适应未见本体时性能更优。
conclusion: 统一潜在动作空间是构建可跨本体泛化的机器人基础世界模型的有效途径。
---

## Abstract
Robot action-conditioned video generation models, also known as robot world models, hold great potential for enhancing robotic planning and decision-making. However, the diversity of robot embodiments and action spaces makes it challenging to build models that generalize across different embodiments. We introduce a robot foundation world model, LAC-WM, which operates within a learned unified latent action space shared across diverse embodiments. We explore how this unified action space improves the world model’s performance when adapted to previously unseen robot embodiments. Specifically, we compare LAC-WM to a baseline model EAC-WM conditioned on explicit motion labels. Our results show that conditioning on explicit labels creates disjoint action spaces across embodiments, limiting downstream task performance when adapting to new robots. We evaluate both models on a dexterous manipulation task. The latent action-conditioned model LAC-WM achieves up to a 46.7% improvement in performance over EAC-WM. Crucially, the unified latent action space allows LAC-WM’s downstream performance to scale positively with the number of embodiments used during pretraining. In contrast, the disjoint action space in EAC-WM leads to decreased performance as the number of pretraining embodiments increases. These results highlights the importance of a unified action space for efficient cross-embodiment learning, addressing a key challenge in robotics.

---

## 论文详细总结（自动生成）

# 论文总结：《Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation》

## 1. 核心问题与整体含义
- **核心问题**：机器人世界模型（即动作条件的视频生成模型）虽对规划决策有巨大潜力，但由于不同机器人本体（如夹爪、灵巧手）在动作空间的维度和语义上差异巨大，现有模型难以在不同本体之间泛化。
- **研究动机**：多样化的本体与动作空间导致模型无法共享知识，每对一种新本体都需要重新训练或微调，限制了基础世界模型的规模化应用。
- **整体含义**：该论文致力于解决机器人基础世界模型在跨本体自适应时的“动作空间碎片化”瓶颈，希望通过学习统一潜在动作空间实现知识迁移，使模型在多本体预训练后对未见本体有更优的适应能力。

## 2. 方法论
- **核心思想**：构建一个潜动作空间机器人基础世界模型（**LAC-WM**），将不同本体的原始动作映射到一个共享的、连续的、低维的潜在动作空间中，再以此空间为条件进行视频生成。这样不同本体的动作在潜空间中具备可比性和可迁移性。
- **关键技术细节**：
  - 学习一个本体无关的**统一潜在动作空间**，可能通过编码器将各本体特异的动作标签或关节角度映射到该空间。
  - 世界模型以历史观测与潜在动作为输入，预测未来视频帧。在预训练阶段利用多个本体数据联合训练，使潜动作空间捕捉到形形色色运动模式的共通结构。
  - 对比基线：**EAC-WM**，即基于显式动作标签（explicit motion labels）的世界模型。显式标签导致不同本体的动作空间在表示层面完全互斥、不连续，阻碍跨本体适应。
- **算法流程简述**（基于摘要推测）：
  1. 对每个机器人本体，通过本体专属的动作编码器将原始动作嵌入到共享潜空间。
  2. 将潜动作与观测历史一起喂入视频预测模型（如 Transformer 或扩散模型）。
  3. 多本体联合训练后，当适配到新本体时，仅需学习一个轻量级映射到已有潜空间，即可重用预训练世界模型，实现高效适应。

## 3. 实验设计
- **数据集/场景**：在**灵巧操作任务**（dexterous manipulation）上进行评估。未详细说明使用的具体数据集名称，但从“多种本体”和“灵巧手”可推知涉及不同形态的机械手及抓取/操作场景。
- **Benchmark 与对比方法**：
  - 主要对比基线：**EAC-WM**（显式动作条件世界模型）。
  - 评估指标：下游任务性能，隐指视频预测质量或基于世界模型的策略成功率。
- **实验条件**：对比在不同数量的预训练本体下，两种模型适应到**未见本体**时的性能变化，考察跨本体泛化能力。

## 4. 资源与算力
- 文中**未明确说明**所用的 GPU 型号、数量及训练时长。从论文分析仅能推断需要多卡进行大规模多本体世界模型预训练，但具体资源消耗无法获知。这是信息缺失之处。

## 5. 实验数量与充分性
- **实验组数推测**：
  - 至少包含预训练本体数量变化的系列实验（如 1 个、2 个、多个直至上限）。
  - 主要结果对比：LAC-WM vs. EAC-WM 在未见本体上的性能，以及在增大预训练本体时的性能趋势。
  - 可能包含消融实验分析潜在动作空间的特性，但摘要未提及具体消融项。
- **充分性与公平性**：
  - 仅在一个任务类型（灵巧操作）上进行验证，场景覆盖有限；未见导航、移动操作等更广泛的本体差异场景。
  - 对比方法单一（仅 EAC-WM），缺少与其他跨本体迁移方法（如元学习、域随机化）的横向比较。
  - 但核心实验——预训练本体规模对适应性能的影响——能够有效揭示统一动作空间的优势，实验设置较为直接，客观且公平地暴露了两类动作表示的本质差别。

## 6. 主要结论与发现
- **性能提升**：LAC-WM 相比 EAC-WM 在适应未见机器人本体时性能提升最高达 **46.7%**。
- **规模化效应**：统一潜在动作空间使得 LAC-WM 的下游任务性能随预训练所用本体数量增加而**正向增长**；而显式标签的 EAC-WM 因动作空间割裂，预训练本体越多性能反而下降。
- **核心启示**：构建可跨本体泛化的机器人基础世界模型，关键在于学习一个**统一的、本体无关的动作表示空间**，这为机器人基础模型的进一步发展指明了方向。

## 7. 优点（亮点）
- **问题定位精准**：抓住了机器人世界模型跨本体迁移中的根本矛盾——动作空间异构。
- **方案简洁有效**：通过学习共享潜在动作空间，使原本互不相关的动作表征变得连续、可迁移，且易于拓展到新本体。
- **规模化验证**：不仅仅是单点性能提升，还证明了方法具备“见多识广”的扩展优势，这对基础模型的哲学至关重要。
- **与显式标签的对比鲜明**：通过 EAC-WM 的退化现象，有力地反衬出统一动作空间的必要性，论证逻辑清晰。

## 8. 不足与局限
- **任务场景单一**：仅在灵巧操作任务上验证，对于移动机器人、双臂协调、人形等多类本体及控制模式的普适性尚不清楚。
- **对比基线有限**：只和基于显式标签的世界模型比较，未涉及其他迁移学习或跨本体动作映射方法（如共享运动原语、Transformer 统一 token 化等）。
- **缺乏资源报告**：未公开所需算力，不利于评估方法实际的可复现性与成本。
- **潜在假设限制**：统一潜空间假设不同本体动作之间存在可共享的流形，这可能对动作语义差异极大的本体（如轮式移动与飞行）失灵，结论的外推性需谨慎。
- **未见实物实验**：从摘要看，很可能仅限仿真或离线的视频预测评估，缺乏真实机器人上的闭环操纵验证，实际部署中的泛化效果未知。

（完）
