---
title: "MVP: Memory-enhanced Vision-Language-Action Policy with Feedback Learning"
title_zh: MVP：记忆增强的视觉-语言-动作策略与反馈学习
authors: "Chubin Zhang, Yansong Tang, Wenkai Guo, Guanxing Lu, Yi Su, Haoji Zhang, Xiuwei Xu, Linqing Zhao, Ziwei Wang, Jiwen Lu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Yz2DnYBJXd"
tags: ["query:model"]
score: 9.0
evidence: 增强记忆的VLA策略，利用情景记忆处理非马尔可夫任务和反馈学习
tldr: 现有VLA通常基于马尔可夫假设，无法利用历史信息处理长任务和从反馈中学习。MVP提出非马尔可夫VLA模型，将历史动作和视觉观测编码为紧凑情景记忆，并设计训练策略防止忽略记忆。实验表明，该方法在时序扩展任务上表现更佳，显著增强VLA的长程决策能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: VLA模型缺乏对历史信息的利用，限制了长程任务表现。
method: 引入情景记忆，将历史动作和视觉编码为紧凑表示，结合反馈学习。
result: 在长时间任务上展现出更好的规划和适应能力。
conclusion: 记忆机制可有效扩展VLA框架，使其处理非马尔可夫任务。
---

## Abstract
Recent advances in Vision-Language-Action (VLA) models have enabled robots to perform a wide range of manipulation tasks conditioned on language instructions, offering strong generalization across tasks, objects, and environments. However, most existing VLAs operate under a Markov assumption, limiting their ability to handle temporally extended tasks and learn from feedback. To address these limitations, we propose MVP, a non-Markovian VLA model that leverages episodic memory composed of historical actions and visual observations. To mitigate the computational cost of storing high-dimensional histories, we introduce a compact memory representation inspired by video understanding techniques. Additionally, to prevent the model from disregarding historical inputs during training, we design a novel feedback learning strategy based on SO(3) trajectory perturbation. This approach encourages the model to associate actions with their environmental consequences through observation-action-observation sequences. Experimental results on both simulated and real-world benchmarks demonstrate that MVP outperforms existing models, particularly on tasks that require temporal reasoning and history-dependent decision-making. Our findings highlight the importance of memory and feedback in advancing the capabilities of general-purpose robotic manipulation systems.

---

## 论文详细总结（自动生成）

# MVP：记忆增强的视觉-语言-动作策略与反馈学习 论文总结

**说明**：由于提供的 PDF 提取文本仅为 OpenReview 的验证页面，未能获取论文全文。以下总结主要依据元数据中的摘要、结论字段及论文标题信息，力求在有限材料下呈现客观、结构化的分析。

## 1. 论文的核心问题与整体含义
- **背景与动机**：当前的视觉-语言-动作（VLA）模型已能令机器人根据语言指令完成多种操作任务，并在任务、物体、环境上展现出强泛化性。
- **核心问题**：绝大多数现有 VLA 模型基于**马尔可夫假设**（仅依赖当前状态决策），这严重限制了它们处理**时间延展型任务**（temporally extended tasks）和**从反馈中学习**的能力。机器人无法利用历史信息进行长程推理，也难以将动作与环境后果真正关联起来。
- **整体含义**：这项研究旨在打破 VLA 的马尔可夫局限，赋予模型**非马尔可夫决策能力**，使机器人能像人类一样借助记忆和反馈在复杂任务中持续改进，向通用机器人操作迈出关键一步。

## 2. 论文提出的方法论
- **核心思想**：提出 **MVP**，一种**非马尔可夫 VLA 模型**，通过引入**情景记忆**（episodic memory）并配合专门的反馈学习策略，让模型在决策时能利用历史动作和视觉观测。
- **关键技术细节**：
  - **紧凑情景记忆**：直接将高维历史（图像、动作序列）存储成本极高。受视频理解技术启发，MVP 将历史动作和视觉观测编码为一个压缩的记忆表示，在保留关键时序信息的同时大幅降低计算开销。
  - **基于 SO(3) 轨迹扰动的反馈学习**：为防止模型在训练中忽视历史输入（即退化回仅依赖当前观测的马尔可夫策略），设计了新颖的反馈学习策略。通过对末端执行器的 **SO(3) 轨迹施加扰动**，迫使模型必须通过“观测-动作-观测”序列来推断动作与环境后果之间的因果联系，从而学会真正利用记忆。
- **算法流程**（文字描述）：给定当前观测和语言指令，模型首先从历史中提取紧凑记忆，结合记忆与当前观测进行动作预测；在训练时，额外生成带有扰动的轨迹片段，要求模型根据扰动前后的观测变化来修正决策，强化记忆的利用。

## 3. 实验设计
- **测试场景与数据集**：论文同时在**仿真基准**和**真实世界基准**上验证 MVP。摘要中未列出具体数据集/场景名称，仅提及“simulated and real-world benchmarks”。
- **对比方法**：与现有模型进行对比（existing models），重点考察在需要时间推理和历史依赖决策的任务上的表现。由于缺少全文，无法列出具体对比的基线模型列表，但可推断包括了主流的马尔可夫型 VLA 模型。

## 4. 资源与算力
- **算力信息缺失**：提供的元数据和摘要中**未明确提及**训练所用的 GPU 型号、数量、训练时长或任何算力开销细节。故无法在此总结相关资源消耗。

## 5. 实验数量与充分性
- **实验体量推断**：根据摘要“experimental results on both simulated and real-world benchmarks”以及方法中包含的多种设计（记忆模块、反馈学习），可以合理推测论文至少包含以下类别实验：
  - 仿真环境上的主实验对比；
  - 真实机器人上的策略迁移验证；
  - 可能有的消融实验（如移除记忆、移除反馈学习等）。
- **充分性与公平性评价**：从有限信息看，同时验证仿真与真机、并明确设计防止记忆被忽视的机制，表明作者对评估的严谨性有所考虑。但由于无法看到具体实验表格、指标和误差线，客观评价其充分性受限。需要结合全文才能确认实验是否覆盖了足够多的任务类型、消融是否彻底，以及对比基线是否公平。

## 6. 论文的主要结论与发现
- **性能优势**：MVP 在仿真和真实世界任务中均**优于现有模型**，尤其在需要时序推理和历史依存决策的任务上优势明显。
- **机制有效性**：记忆机制和反馈学习策略切实提升了 VLA 模型的长程规划与适应能力，证明了**记忆**和**反馈**对推动通用机器人操作系统发展至关重要。
- **框架扩展性**：记忆增强的思路可有效扩展 VLA 框架，使其能够处理更广泛的非马尔可夫任务。

## 7. 优点
- **问题定义清晰**：直指当前 VLA 的马尔可夫假设痛点，动机切中实际机器人应用中的长程决策难题。
- **方法设计有针对性**：
  - 紧凑记忆表示兼顾了信息保存与计算效率；
  - 基于 SO(3) 扰动的反馈学习策略巧妙的解决了“模型忽视记忆”的训练退化问题，强迫模型建立因果联系。
- **实验验证维度丰富**：同步覆盖仿真与真实环境，关注时序依赖性任务，使结论更具说服力。
- **非马尔可夫框架**：为 VLA 模型突破当前能力边界提供了一种可复用的范式。

## 8. 不足与局限
- **信息获取局限**：因仅获得元数据，以下分析带有推测性质，完整评价需依赖全文。
- **可能的方法局限**：
  - 紧凑记忆的压缩倍率和信息损失情况未知，当历史序列极长时可能存在信息瓶颈。
  - SO(3) 轨迹扰动对任务类型有一定限制，可能更适用于操作类任务，在纯导航或非刚体控制场景中适用性待考。
- **实验覆盖风险**：摘要中未说明仿真环境的具体规模和多样性，真实世界实验的任务数量、物体多样性以及试错次数均不明确，可能存在小样本真实任务偏差。
- **算力与复现成本**：未有算力报告，难以评估训练成本及其对实际复现的门槛。

（完）
