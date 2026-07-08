---
title: "D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI"
title_zh: D2E：利用桌面数据扩展视觉-动作预训练以迁移至具身AI
authors: "Suhwan Choi, Jaeyoon Jung, Haebin Seong, Minchan Kim, Minyeong Kim, Yongjun Cho, Yoonshik Kim, Park Yu Been, Youngjae Yu, Yunsung Lee"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=TRwQND3xpt"
tags: ["query:data"]
score: 7.0
evidence: 利用可扩展的桌面数据收集为具身AI预训练
tldr: 针对具身AI中物理交互数据采集成本高昂的问题，提出D2E框架，利用桌面环境（如游戏）获取大规模具身交互数据，进行视觉-动作预训练，然后迁移到真实机器人任务上，验证了桌面数据作为预训练基质的有效性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 具身AI受限于物理轨迹采集的高成本，缺乏大规模交互数据。
method: D2E框架利用桌面环境收集可扩展的视觉-动作数据，进行预训练并迁移至机器人任务。
result: 实验表明基于桌面数据预训练的模型在机器人任务上表现良好，证明了该范式的可行性。
conclusion: D2E为具身AI提供了可扩展的预训练数据来源，显著降低了数据获取门槛。
---

## Abstract
Large language models leverage internet-scale text data, yet embodied AI remains constrained by the prohibitive costs of physical trajectory collection.
Desktop environments---particularly gaming---offer a compelling alternative: they provide rich sensorimotor interactions at scale while maintaining the structured observation-action coupling essential for embodied learning.
We present D2E (Desktop to Embodied AI), a framework that demonstrates desktop interactions can serve as an effective pretraining substrate for robotics embodied AI tasks.
Unlike prior work that remained domain-specific (e.g., VPT for Minecraft) or kept data proprietary (e.g., SIMA), D2E establishes a complete pipeline from scalable desktop data collection to verified transfer in embodied domains.
Our framework comprises three components: (1) the OWA Toolkit that unifies diverse desktop interactions into a standardized format with 152× compression, (2) the Generalist-IDM that achieves strong zero-shot generalization across unseen games through timestamp-based event prediction, enabling internet-scale pseudo-labeling, and (3) VAPT that transfers desktop-pretrained representations to physical manipulation and navigation.
Using 1.3K+ hours of data (259 hours of human demonstrations and 1K+ hours of pseudo-labeled gameplay), our 1B-parameter model achieves 96.6\% success on LIBERO manipulation and 83.3\% on CANVAS navigation, matching or surpassing models up to 7$\times$ larger, such as $\pi_0$ (3.3B) and OpenVLA (7B).
These results demonstrate that sensorimotor primitives learned from digital interactions transfer effectively to real-world physical tasks, establishing desktop pretraining as a practical paradigm for embodied AI.
All resources are publicly available at https://worv-ai.github.io/d2e.

---

## 论文详细总结（自动生成）

# D2E 论文深度解析

## 1. 核心问题与研究动机
- **问题背景**：具身人工智能受制于真实物理轨迹采集的高昂成本，难以像大语言模型那样利用互联网规模的数据进行预训练。
- **核心矛盾**：具身模型迫切需要大规模、高质量、**观测-动作**紧密耦合的交互数据，而物理世界的采集效率与代价严重制约了模型的发展。
- **整体含义**：提出**用桌面环境（尤其是游戏）作为具身预训练的替代数据源**，这些环境天然具备丰富的感官运动交互，且数据采集具有近乎无限的可扩展性。D2E 旨在证明：从数字交互中学到的**感知运动基元**能够有效迁移到真实世界的物理操作与导航任务中，从而大幅降低具身AI的数据门槛。

## 2. 方法论
D2E 构建了一套从桌面数据采集、大规模伪标签生成到机器人端迁移的完整流水线，包含三个核心组件：

- **OWA Toolkit**  
  - 统一多种桌面交互（如不同游戏）为标准化的观察-动作格式。  
  - 实现 **152 倍数据压缩**，极大降低存储与传输负担，使大规模数据汇聚成为可能。

- **Generalist-IDM（通用逆动力学模型）**  
  - 以基于时间戳的事件预测为主要学习目标，**不依赖特定游戏的奖励或标签**。  
  - 获得强大的**零样本泛化**能力：能在从未见过的游戏中准确预测动作，为海量无标签游戏视频生成伪标签。  
  - 实现了**互联网规模的伪标注**，将 1K+ 小时的纯游戏玩法自动转化为带动作监督的训练数据。

- **VAPT（视觉-动作预训练与迁移）**  
  - 将上述桌面预训练得到的表征（1B 参数模型）迁移到真实机器人任务上。  
  - 验证了两种关键具身能力：**物体操纵**（LIBERO benchmark）与**视觉导航**（CANVAS benchmark）。

整条管线可概括为：**桌面原始交互 → 统一压缩 → 伪标签扩增 → 通用表征预训练 → 机器人策略微调**。

## 3. 实验设计
- **数据集构成**  
  - 总计 **1,300+ 小时**的桌面交互数据：  
    - 259 小时的人工采集演示数据。  
    - 1,000+ 小时经 Generalist-IDM 伪标注的游戏数据。  
- **下游任务基准**  
  - **LIBERO**：标准化物体操纵任务套件，评估细粒度操作能力。  
  - **CANVAS**：视觉导航任务，评估空间移动与目标驱动的能力。  
- **对比方法**  
  - `π0`（3.3B 参数）  
  - `OpenVLA`（7B 参数）  
  两者均为大规模具身预训练模型，参数量远大于 D2E 的 1B 模型。

## 4. 资源与算力
- 论文摘要及所提供材料**未明确提及所用的 GPU 型号、数量及具体训练时长**。  
- 仅披露模型规模为 1B 参数，并使用了 1.3K+ 小时数据。可以合理推断所需算力可观，但详细资源清单需查阅正文或附录。

## 5. 实验数量与充分性
- **受益于有限的披露信息**，我们可以确认的实验组包括：  
  - 在 LIBERO 操纵基准上的成功率评估。  
  - 在 CANVAS 导航基准上的成功率评估。  
  - 与至少两个大规模 baseline 模型（π0、OpenVLA）的性能对比。  
- **充分性与公平性分析**：  
  - 两个典型的具身任务（操纵、导航）有助于验证迁移的通用性，但未提及更多复杂环境（如移动操作、人机交互）。  
  - 对比的模型参数量均为我方模型的 **3.3~7 倍**，双方采用不同的预训练数据源，比较具有科学意义，但细节未知（如微调数据量、评测协议）。  
  - 未呈现消融实验（如不同预训练数据量、各组件贡献等）的细节，因此目前仅能依据公开摘要判断实验覆盖度中等，尚待完整论文补充验证。

## 6. 主要结论与发现
1. **桌面交互数据是有效的具身预训练基质**：仅使用数字世界的感官运动经验，即可成功迁移到物理操作与导航中。  
2. **参数效率超群**：1B 参数的 D2E 模型在 LIBERO 操纵任务上达到 **96.6%** 的成功率，在 CANVAS 导航任务上达到 **83.3%** 的成功率，匹配或超越了参数多 3~7 倍的大模型。  
3. **伪标签扩展是可行路径**：通用逆动力学模型能够在零样本条件下为海量游戏视频生成有效的动作监督，大幅放大预训练数据规模。  
4. **范式成立**：桌面预训练可作为低成本、可扩展的具身AI发展范式，为后续研究提供了开放资源和基线。

## 7. 优点
- **思路新颖且实用**：巧妙地将游戏数据引入具身预训练，直击物理数据稀缺的痛点，并证明了迁移的可行性。  
- **完整的系统实现**：从数据采集、压缩、自动标注到策略迁移的端到端框架，为社区提供了可直接复用的基础设施。  
- **性能强悍且资源高效**：以小搏大，1B 模型在多个具身基准上超越或持平数倍参数专有模型，展示了桌面预训练的高效性。  
- **资源全面开源**：所有资源公开，有助于推动开放科学和后续研究。

## 8. 不足与局限
- **评估场景仍较有限**：目前仅覆盖桌面操纵（LIBERO）和视觉导航（CANVAS），未在更多样化、更复杂的真实机器人任务（如全身操控、动态交互、长程作业）上验证。  
- **模拟到现实的跨域偏差未充分探讨**：桌面游戏与真实物理在动力学、视觉纹理、动作延迟等方面仍有显著差异，论文摘要未说明缩小该偏差的具体技术或分析。  
- **伪标签质量依赖**：千余小时的伪标签数据由通用逆动力学模型生成，其噪声和错误可能影响最终性能，缺乏对标签质量及其影响的详细分析。  
- **算力与可复现性细节缺失**：未提供训练所用具体硬件、能耗或训练时长，难以精确评估资源需求和复现成本。  
- **任务类型局限**：桌面交互多为离散或简单的连续动作，能否泛化到连续、高频的真实机器人控制（如力控）仍待验证。

（完）
