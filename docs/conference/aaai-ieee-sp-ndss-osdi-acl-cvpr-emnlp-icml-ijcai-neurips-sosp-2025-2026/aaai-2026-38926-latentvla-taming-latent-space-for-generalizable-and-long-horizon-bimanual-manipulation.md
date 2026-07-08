---
title: "LatentVLA: Taming Latent Space for Generalizable and Long-Horizon Bimanual Manipulation"
title_zh: LatentVLA：驯服潜在空间以实现可泛化的长程双手操作
authors: Junming Wang
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38926/42888"
tags: ["query:analysis"]
score: 10.0
evidence: 潜在动作空间错配导致时间混淆和控制失败；LatentVLA学习连续的物理一致潜在空间
tldr: 针对逆动力学模型中潜在动作空间与物理世界脱节导致的时序混淆和规划失败，LatentVLA学习一个连续的、能捕捉动作方向和幅度的潜在空间。该表示与物理现实对齐，有效解决了视觉相似状态下的动作歧义问题，并在双手机器人上实现了长程、可泛化的操作，为具身智能的表示学习提供了重要参考。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38926/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 877, \"height\": 417, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38926/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1107, \"height\": 601, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38926/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1839, \"height\": 1123, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38926/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1848, \"height\": 651, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38926/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 661, \"height\": 417, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38926/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 884, \"height\": 565, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38926/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 384, \"height\": 459, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38926/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 344, \"height\": 451, \"label\": \"Table\"}]"
motivation: 现有模型潜在动作空间与物理脱节，导致时序混淆和规划不可行。
method: 学习连续的、方向与幅度感知的潜在动作空间，对齐物理现实。
result: 解决了时间混淆问题，实现了稳健的双手长程操作规划。
conclusion: LatentVLA表明物理一致的潜在空间对泛化和规划至关重要。
---

## Abstract
Current paradigms for robotic imitation learning face a stark trade-off between the motion fidelity of diffusion models and the data scalability of inverse dynamics models. The latter, while scalable, often learns a latent action space disconnected from physical reality. This flaw leads to critical failures: temporal entanglement, where the model cannot distinguish between visually similar states requiring distinct actions, e.g., a gripper approaching versus receding from an object. This ambiguity, compounded by discretization artifacts and sensitivity to task-irrelevant dynamics, renders robust planning infeasible. We introduce LatentVLA, a vision-language-action framework designed to overcome these limitations by learning a continuous and spatiotemporally grounded latent action representation. Its progressive three-stage architecture first employs a Temporal-Attentive Latent Action Model (TA-LAM) to resolve ambiguities using language-guided attention and explicit temporal encoding. Subsequently, a Latent Action Diffusion Transformer (LADT) performs planning via diffusion directly within this continuous latent space, preserving motion fidelity without tokenization. Finally, an expert policy head translates these latent plans into precise robot actions. Experiments show LatentVLA sets a new state-of-the-art across a suite of real-world bimanual tasks, outperforming prior methods and demonstrating superior zero-shot generalization and few-shot efficiency.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **研究动机**：当前机器人模仿学习存在两个主流范式：扩散模型（高运动保真度但需大量标注数据）与逆动力学模型（利用无标注视频实现数据可扩展性，但学习到的潜在动作空间往往脱离物理现实）。
- **核心矛盾**：逆动力学模型产生的潜在动作会遭遇**时间混淆（temporal entanglement）**——无法区分视觉相似但动作语义不同的状态（如夹爪接近 vs. 远离物体）。此外，**离散化伪影**和**对任务无关动态的敏感性**进一步破坏规划可靠性。
- **整体目标**：构建一个连续、时空锚定的潜在动作表示，同时解决运动保真度与数据可扩展性之间的权衡，并克服上述固有缺陷。

### 2. 论文提出的方法论

#### 核心思想
- 将**表示学习与规划解耦**：第一阶段从异构数据（标注与非标注）学习一个稳健的连续潜在动作空间；第二阶段在该连续空间内进行扩散规划，避免离散化伪影；第三阶段通过专家策略头将潜在计划转化为物理动作。
- 采用**语言引导的注意力与显式时间编码**实现时空情境化，消除任务无关动态和感知歧义。

#### 关键技术细节与流程

**阶段一：时间注意潜在动作模型 (TA-LAM)**
- **注意力驱动的逆动力学模型 (IDM)**：
  - 利用冻结的 SigLIP 模型计算语言指令与多视角图像的注意力掩码，生成任务聚焦的视觉特征。
  - 引入**绝对时间编码** \(\gamma(t)\) 提供任务进度信号，配合正弦相对位置编码 PE(k) 来建模短时动态。
  - Transformer 编码器处理上下文序列，输出单步潜在动作 \(Z_t\) (维度 512)。
- **潜在前向动力学模型 (FDM)**：用 \(Z_t\) 和隐藏状态预测下一帧视觉观测 \(\hat{O}_{t+1}\)，构成无监督重建损失。
- **动作解码器**：轻量 MLP 将 \(Z_t\) 映射为双臂动作 \(\hat{a}_t \in \mathbb{R}^{14}\)，仅用标注机器人数据监督。
- **联合损失**：\(\mathcal{L}_{\text{TA-LAM}} = \mathcal{L}_{\text{recon}} + \lambda_{\text{act}} \mathcal{L}_{\text{action}}\)，重建损失应用于所有序列（包括人类视频），动作损失仅应用于标注子集。

**阶段二：潜在动作扩散 Transformer (LADT)**
- 在冻结的 TA-LAM 产生的连续潜在空间内直接进行长程规划。
- 条件：历史观测、先前潜在动作、本体感受和语言指令。
- 训练目标：预测未来 16 步的潜在动作序列，使用标准去噪分数匹配损失。
- 设计选择：连续空间避免 VQ‑VAE 的量化误差，模型动作的细微变化，生成平滑序列。

**阶段三：真实世界微调**
- 冻结 TA-LAM（IDM + 动作解码器），仅微调 LADT 规划器。
- 最小化解码动作与专家动作的均方差，保持表示泛化能力的同时高效适应。

### 3. 实验设计

**数据集与场景**
- **预训练数据** \(D_{\text{pretrain}}\)：来自 52 个来源的超过 250 万条序列，包含未标注人类视频、多平台带标注机器人轨迹（RDT-1B 语料库）、仿真数据以及自采的 AgiBot World Beta 和 LatentVLA‑Dexterous 数据集（约 50 万序列）。
- **微调数据** \(D_{\text{finetune}}\)：1600 小时的双臂任务演示，涵盖 8 个特定任务。
- **评估场景**：
  - **真实世界**：8 项具有挑战性的双臂操作（如折叠布料、折叠毛巾等），并设置分布外（OOD）探测（光照变化、新物体、动态干扰）。
  - **仿真基准**：RoboTwin 1.0（双臂协调）、SIMPLER（长程操作）、CALVIN（ABC→D 组合泛化）。

**对比方法**
- 真实世界：重新训练的 RDT‑1B 和 LAPA。
- 仿真：DP、DP3、Octo、OpenVLA、RT‑2、Moto、RoboFlamingo、GR‑1 等，均在同一数据条件下公平比较。

### 4. 资源与算力

- **预训练（阶段一、二）**：在 112 块 NVIDIA A100‑80G GPU 集群上进行，耗时约一个月。
- **微调（阶段三）**：针对 8 个任务共 100,000 次迭代；少样本实验仅需单块 A100 GPU、不到一小时微调即可适应新物体。

### 5. 实验数量与充分性

- **主要实验组**：
  - 真实世界 8 项任务的成功率对比（图 4）。
  - 3 个仿真基准的完整结果（表 1a、1b、1c）。
  - 零样本泛化能力测试（光照、背景、新物体）。
  - 数据缩放实验：在相同原始 RDT‑1B 数据集上从头训练，以及用新增 1600 小时数据微调基线。
  - 少样本适应实验（20 个演示，折叠长毛巾）。
  - 消融实验（表 2）：5 种变体（替换为 VQ‑VAE + 自回归、移除绝对时间编码、仅视频训练、移除语言注意力、移除潜在历史条件）以及两种基线。
- **充分性与公平性**：所有基线均在同一完整数据集上重新训练；消融实验清晰量化每个组件的贡献；覆盖域内、分布外、零样本和少样本场景；实验规模较大且设计系统，结论可靠。

### 6. 主要结论与发现

- **性能领先**：在真实世界 8 项任务中平均成功率达 63.8%，分别比 RDT‑1B 和 LAPA 高 12.8% 和 48.5%；在三个仿真基准上均建立新 SOTA。
- **泛化能力突出**：在多种干扰条件下（光照、背景变化）仍保持 56% 成功率，连续潜在空间使其在面对感知扰动时表现出“优雅退化”。
- **少样本高效**：仅 20 个演示微调即可在新物体上达到 61% 成功率，超 RDT‑1B 27%。
- **架构有效性**：消融表明连续扩散规划（而非离散表示）和绝对时间编码是性能的关键支柱；语言注意力与联合训练（视频+机器人数据）对物理落地至关重要。

### 7. 优点

- **创新性设计**：首次在双臂操作领域系统性地将语言引导的空间注意、显式绝对时间编码和连续潜在扩散规划集成到同一框架。
- **表示与规划解耦**：既利用未标注数据提升可扩展性，又通过连续潜在空间保持动作精细度，解决离散方法的“伪影”问题。
- **扎实的实验验证**：真实机器人、多仿真基准、详尽的消融和泛化测试，证据链完整。
- **高效微调策略**：冻结表示层仅更新规划器，极大降低目标平台适应成本。

### 8. 不足与局限

- **遮挡与反射敏感**：论文明确指出对完全物体遮挡和高反光表面造成的视觉歧义敏感，可能影响潜在动作推断。
- **未探讨复杂接触任务**：实验任务以抓取和折叠为主，未涉及高动态接触或力控密集型任务。
- **单一双臂平台**：所有真实实验仅在一类双臂机器人上进行，泛化至不同构型（如移动操作）还需验证。
- **大规模数据依赖**：预训练仍依赖百万级序列和海量 GPU 资源，训练成本较高。
- **绝对时间编码的假设**：依赖任务进度的时间戳，可能不适用于非结构化或无限长任务。

（完）
