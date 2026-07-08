---
title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
title_zh: 双流扩散用于世界模型增强的视觉-语言-动作模型
authors: "John Won, Kyungmin Lee, Huiwon Jang, Dongyoung Kim, Jinwoo Shin"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=mK1SdO7j3t"
tags: ["query:model"]
score: 10.0
evidence: 世界模型增强的VLA，双流扩散处理模态冲突
tldr: 现有VLA融入世界模型时面临模态冲突，难以同时预测观测与动作。DUST提出双流扩散Transformer，为观测和动作保持独立流并实现跨模态知识共享，结合独立噪声扰动和解耦训练技巧。实验显示，该方法显著增强了世界模型增强VLA的性能，在多样化任务上取得更优效果。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 世界模型增强VLA中动作与观测的模态差异导致预测困难。
method: 提出双流扩散架构，独立处理模态并通过跨模态融合增强。
result: 在操作任务上联合预测与动作生成性能优于以往方法。
conclusion: 双流扩散有效解决模态冲突，提升世界模型增强VLA能力。
---

## Abstract
Recently, augmenting vision-language-action models (VLAs) with world-models has shown promise in robotic policy learning. However, it remains challenging to jointly predict next-state observations and action sequences because of the inherent difference between the two modalities. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework that handles the modality conflict and enhances the performance of VLAs across diverse tasks. Specifically, we propose a multimodal diffusion transformer architecture that explicitly maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, we propose training techniques such as independent noise perturbations for each modality and a decoupled flow matching loss, which enables the model to learn the joint distribution in a bidirectional manner while avoiding the need for a unified latent space. Furthermore, based on the decoupled training framework, we introduce a sampling method where we sample action and vision tokens asynchronously at different rates, which shows improvement through inference-time scaling. Through experiments on simulated benchmarks such as RoboCasa and GR-1, DUST achieves up to 6\% gains over standard VLA baselines and world-modeling methods, with our inference-time scaling approach providing an additional 2-5\% gain on success rate. On real-world tasks with the Franka Research 3, DUST outperforms baselines in success rate by 10\%, confirming its effectiveness beyond simulation. Lastly, we demonstrate the effectiveness of DUST in large-scale pretraining with action-free videos from BridgeV2, where DUST leads to significant gain when transferred to the RoboCasa benchmark.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：近年来，将世界模型（world models）集成到视觉‑语言‑动作模型（VLA）中，已成为提升机器人策略学习的有效途径。世界模型能够预测环境未来的观测状态，从而辅助 VLA 进行规划与决策。
- **核心问题**：联合预测下一时刻的观测（图像）与动作序列时，由于两种模态（高维视觉信号 vs. 低维控制指令）存在本质上不同的分布特性，传统单一模型难以同时良好处理，造成“模态冲突”，限制世界模型增强 VLA 的性能。
- **整体含义**：本文提出 DUST（DUal‑STream diffusion）框架，通过专门的双流扩散结构来消解模态冲突，从而在不牺牲预测质量的前提下，增强 VLA 在多种任务中的表现，并支持从无动作视频中大规模预训练。

## 2. 论文提出的方法论

- **核心思想**：为观测和动作分别维护独立的隐式空间与处理通道，同时通过跨模态交互实现知识共享，避免强行将两种模态压缩到统一隐空间所带来的干扰。
- **关键技术细节**：
    - **双流扩散 Transformer 架构**：显式分为观测流和动作流，各流使用独立的扩散过程，但在 Transformer 层间插入跨注意力或融合模块，使视觉特征与动作特征能够互相增强。
    - **独立噪声扰动**：在扩散前向加噪过程中，对观测和动作分别施加独立的噪声水平与调度，使得模型能够分别适应两者不同的不确定性结构。
    - **解耦的流匹配损失（Decoupled Flow Matching Loss）**：训练时，采用双向匹配目标进行解耦，不强制构建统一的联合隐空间，而是让模型分别学习边缘分布和条件分布，最终仍能拟合真实的联合分布。
    - **异步采样方法**：推理时，利用训练的解耦框架，以不同的步长或速率分别对动作和视觉 token 进行扩散采样（例如动作流可以更早地完成重构），实现推理时的计算扩展（inference‑time scaling），进一步提升了成功率。
- **形式化表述（文字说明）**：给定历史观测‑动作序列，模型对下一时刻的观测 \(o_{t+1}\) 和动作 \(a_{t+1}\) 建立双流扩散过程：\(q(o_{t+1},a_{t+1} | \text{context})\) 被分解为经过独立流处理后由跨模态注意力融合的条件生成。训练利用解耦流匹配，优化目标为最小化各流上真实数据路径与模型预测路径之间的 Wasserstein 距离的期望，同时保证跨模态一致性。

## 3. 实验设计

- **模拟基准与环境**：
    - **RoboCasa**：大规模机器人操作模拟平台，涵盖丰富的家居操作任务。
    - **GR‑1**：另一个机器人学习基准（文中指与 GR‑1 相关的模拟任务）。
- **对比方法**：标准 VLA 基线（如不含世界模型的策略）、已有的世界模型增强方法（如将观测和动作统一建模的单流扩散或自回归方案）。
- **真实机器人实验**：使用 Franka Research 3 机械臂，在真实世界操作任务上验证，与基线比较成功率。
- **大规模预训练与迁移**：利用 BridgeV2 数据集中的无动作视频进行大规模预训练，然后将学习到的世界模型部分迁移到 RoboCasa 模拟任务上，评估迁移增益。

## 4. 资源与算力

- **文中提及情况**：根据提供的摘要与元数据，**未明确说明** GPU 型号、数量、训练时长等具体算力信息。该信息可能存在于论文正文中，但此处给出的内容未包含。从采用扩散 Transformer 与大规模预训练（BridgeV2）推断，所需的计算资源应当较高，但无法给出确切数字。

## 5. 实验数量与充分性

- **实验组数大致估计**：
    - 两组模拟基准（RoboCasa、GR‑1）上的对比实验。
    - 不同推理时采样策略的消融（异步 vs. 同步，不同速率）。
    - 真实机器人操作任务验证。
    - 大规模预训练后的迁移实验。
- **充分性与公平性**：实验覆盖了仿真、真实环境以及迁移学习，与标准 VLA 基线及同类世界模型方法进行直接比较，且通过消融验证了异步采样等的贡献。所属实验设计较为系统，对比公平，能够支撑其“双流扩散有效缓解模态冲突”的核心主张。但摘要未提供具体任务数量和种子数，因此更细致的充分性评判需查阅全文。

## 6. 论文的主要结论与发现

- 在模拟基准上，DUST 较标准 VLA 和单流世界模型方法成功率最高提升约 **6%**。
- 所提出的**推理时缩放（异步采样）**，可在不额外训练的情况下，再带来 **2‑5%** 的成功率增益。
- 在 Franka 真实机器人任务上，DUST 的成功率高出基线 **10%**，证实了仿真到真实的有效迁移。
- 利用 BridgeV2 的无动作视频进行预训练，DUST 在迁移至 RoboCasa 时仍能获得显著提升，表明方法具备从纯观测数据中学习世界模型并增强策略的能力。
- 总体结论：通过双流扩散显式分离和控制模态差异，是一种简单且高效的世界模型增强 VLA 范式，有望成为未来综合感知‑规划‑控制系统的基石。

## 7. 优点

- **创新性强的问题定义**：明确指出并形式化世界模型增强 VLA 中的“模态冲突”，并给出有针对性的解决方案。
- **简洁而有效的架构设计**：双流分离、独立噪声、解耦损失，避免了强行融合带来的性能退化，工程实现上相对清晰。
- **推理时扩展的优势**：异步采样利用了解耦训练的特性，能够在不增加模型参数的情况下实现类似“思考时间”的增益，适合资源受限或实时调整的场合。
- **多元验证**：涵盖仿真环境、真实机器人操作以及大规模无动作视频预训练，展示了方法的通用性和鲁棒性。
- **模块化设计**：双流架构易于与原 VLA 系统集成，也方便单独预训练世界模型部分。

## 8. 不足与局限

- **算力需求可能较高**：采用扩散 Transformer 以及双流并行处理，在训练和推理时可能比单流方法需要更多计算资源，但论文摘要未量化这一代价。
- **实验细节不透明**：从提供的文本中，无法看到具体的成功率和方差、任务数量、数据集规模等量化指标，对结论的稳健性判断受限。
- **真实世界任务范围**：仅在 Franka Research 3 上进行验证，任务复杂度和环境多样性可能有限，泛化到更嘈杂或动态变化的实际场景尚待证明。
- **对预训练数据的依赖**：虽然展示了无动作视频预训练的增益，但如果视频数据的分布与下游任务差异过大，迁移效果可能衰减，且方法对数据质量的敏感性未深入讨论。
- **异步采样的超参数敏感性**：推断采样步长和调度器需要针对不同任务调节，可能增加部署时的调优负担。

（完）
