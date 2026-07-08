---
title: "Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance"
title_zh: 先对齐再引导：通过统一潜空间指导适配视觉-语言-动作模型
authors: "Yang Zhang, Chenwei Wang, ouyang lu, Yuan Zhao, Yunfei Ge, Zhenglong Sun, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=T3i7Ifeatk"
tags: ["query:model"]
score: 9.0
evidence: 统一潜空间对齐实现跨本体数据高效的VLA模型适配
tldr: 针对VLA模型在跨本体或任务变化时需大量数据微调的问题，提出Align-Then-stEer框架，通过变分自编码器构建统一潜空间对齐动作分布，再通过潜引导实现高效适配，大幅降低了适配数据需求，推动了通用机器人模型的跨本体迁移。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: VLA模型预训练后适配下游任务时，本体或任务差异导致动作分布错配，需要大量数据和计算。
method: 提出ATE框架，第一阶段用VAE对齐不同动作空间到统一潜空间；第二阶段通过潜引导微调策略。
result: 数据高效地将VLA模型适配到新任务和本体，性能接近或超越完全微调。
conclusion: ATE为VLA模型的跨本体迁移提供了即插即用的高效适配方案。
---

## Abstract
Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce Align-Then-stEer (ATE), a novel, data-efficient, and plug-and-play adaptation framework. ATE first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to 9.8% in simulation and achieves a striking 32% success rate gain in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying  VLA models to new robotic platforms and tasks. Our code is released at \url{https://github.com/TeleHuman/Align-Then-Steer}.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **核心问题**：视觉 – 语言 – 动作（VLA）模型在通用机器人操作中潜力巨大，但适配下游任务时存在瓶颈——当机器人本体（embodiment）或任务与预训练数据不同时，动作分布产生严重错配，导致需要大量数据和计算才能有效微调。
- **整体含义**：旨在提出一种数据高效、即插即用的 VLA 模型适配框架，降低从预训练模型迁移到新本体、新任务时的数据与算力开销，提升通用机器人的实际部署效率。

## 2. 方法论

- **核心思想**：采用“先对齐、再引导”的两阶段策略。
- **第一阶段：动作空间对齐（Align）**
  - 使用变分自编码器（VAE）将不同本体的动作空间映射到一个统一潜空间。
  - 通过**反向 KL 散度**约束，将适配动作嵌入到预训练动作潜分布的模态（mode）中，实现动作分布的对齐。
- **第二阶段：潜空间引导微调（Steer）**
  - 在微调基于扩散或流模型的 VLA 时，引入**潜空间引导机制**。
  - 该机制将模型的输出分布“推向”目标域（即新任务/新本体的动作分布），从而实现高效适配。
- **关键特性**：整个框架具有**即插即用**的特点，不改变原有 VLA 模型结构，仅需少量适配数据。

## 3. 实验设计

- **场景与基准**：
  - **仿真环境**：跨本体和跨任务的机器人操作任务。
  - **真实世界**：跨本体设置下的真实机器人操作任务。
  - 评估指标为**多任务成功率**。
- **对比方法**：主要与代表性 VLA 模型的**直接完全微调**进行对比。

## 4. 资源与算力

- **论文元数据中未明确说明**使用的 GPU 型号、数量、训练时长等算力开销细节。仅从摘要判断，该方法强调数据高效，但计算资源消耗未披露。

## 5. 实验数量与充分性

- 从元数据可推断的实验量级：
  - 包含**仿真**与**真实世界**两大类实验。
  - 仿真中涉及多任务，汇报了“平均多任务成功率提升**9.8%**”，真实世界中跨本体设置下成功率提升**32%**。
  - 论文描述为“大量实验”，但未提供具体实验组数、消融实验细节或不同数据量下的性能曲线。
- **充分性与客观性评价**：
  - 与直接微调的对比结果清晰，且跨度较大（仿真 + 真实），初步说明方法有效。
  - 然而，由于缺少与其他参数高效适配方法（如 Adapter、LoRA 等）的对比、消融实验的详细披露，难以全面评估方法的相对优势与稳定边界。总体而言，信息有限，但已呈现的对比实验具备基本客观性。

## 6. 主要结论与发现

- ATE 框架能**数据高效地**将预训练 VLA 模型适配到新任务和跨本体场景，性能上**接近甚至超越完全微调**。
- 在仿真跨本体、多任务操作中，成功率平均提升最高达 9.8%；在真实世界跨本体任务中取得 32% 的显著增益。
- ATE 为通用机器人模型提供了一种**通用、轻量级的适配方案**，有效推动了 VLA 模型的实际部署。

## 7. 优点

- **数据效率高**：显著降低了适配所需的数据量，缓解动作分布错配问题。
- **即插即用**：无需修改 VLA 模型内部架构，可作为通用适配层快速应用于不同模型。
- **两阶段设计合理**：先对齐潜空间、再引导生成过程，从分布层面解决跨本体适配的核心矛盾。
- **实验验证真实**：覆盖仿真与真实机器人，对直接微调基线展现出大幅提升，真实世界效果突出。

## 8. 不足与局限

- **对比方法单一**：仅与完全微调对比，缺乏与当前主流的参数高效微调方法（如 LORA、Adapter、Prompt Tuning）的直接比较，难以全面确立其优势。
- **信息不全**：未提供实验所需的具体数据量、计算开销、模型规模与训练细节，复现性和资源评估受限。
- **泛化性未知**：仅在部分 VLA 模型和特定本体上测试，缺少对更极端本体差异、多样化任务类型的广义验证。
- **潜空间构建成本**：需要为不同目标域训练 VAE 进行对齐，虽然数据量少，但每次适配仍需额外的前置训练阶段。
- **评估维度单一**：仅汇报成功率，缺少如响应延迟、干预率、行为平滑度等机器人操作中重要的细粒度指标。

（完）
