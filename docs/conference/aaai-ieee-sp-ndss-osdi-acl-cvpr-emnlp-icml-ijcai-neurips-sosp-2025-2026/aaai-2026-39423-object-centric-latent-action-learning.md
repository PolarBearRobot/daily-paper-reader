---
title: Object-Centric Latent Action Learning
title_zh: 对象中心潜在动作学习
authors: "Albina Klepach, Alexander Nikulin, Ilya Zisman, Denis Tarasov, Alexander Derevyagin, Andrei Polubarov, Nikita Lyubaykin, Igor Kiselev, Vladislav Kurenkov"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39423/43384"
tags: ["query:data"]
score: 9.0
evidence: 从无标签互联网视频中通过对象中心解耦推断潜在动作
tldr: 利用互联网视频学习潜在动作时，视觉干扰严重影响性能。本文提出对象中心潜在行动学习框架，通过自监督对象中心预训练将动作与背景动态分离，从而获得鲁棒的代理动作标签。实验表明该框架在干扰环境下显著优于像素级方法，为大规模无监督视频数据用于机器人模仿学习开辟了途径。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39423/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 865, \"height\": 401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39423/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1469, \"height\": 628, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39423/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 709, \"height\": 707, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39423/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1451, \"height\": 724, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39423/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1876, \"height\": 1056, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39423/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1839, \"height\": 819, \"label\": \"Table\"}]"
motivation: 互联网视频中视觉干扰阻碍了潜在动作推断用于模仿学习。
method: 基于自监督对象中心预训练解耦动作与背景，提取鲁棒代理动作。
result: 在存在干扰的视频中显著提升了模仿学习的性能。
conclusion: 对象中心表示能有效过滤干扰，提升从视频中学习潜在动作的可靠性。
---

## Abstract
Leveraging vast amounts of unlabeled internet video data for embodied AI is currently bottlenecked by the lack of action labels and the presence of action-correlated visual distractors. Although recent latent action policy optimization (LAPO) has shown promise in inferring proxy action labels from visual observations, its performance degrades significantly when distractors are present. To address this limitation, we propose a novel object-centric latent action learning framework that centers on objects rather than pixels. We leverage self-supervised object-centric pretraining to disentangle the movement of the agent and distracting background dynamics. This allows LAPO to focus on task-relevant interactions, resulting in more robust proxy-action labels, enabling better imitation learning and efficient adaptation of the agent with just a few action-labeled trajectories. We evaluated our method in eight visually complex tasks across the Distracting Control Suite (DCS) and Distracting MetaWorld (DMW). Our results show that object-centric pretraining mitigates the negative effects of distractors by 50%, as measured by downstream task performance: average return (DCS) and success rate (DMW).

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心挑战**：大量互联网视频可用来训练具身 AI 智能体，但这类数据普遍缺少动作标签，并且经常存在与动作发生虚假关联的视觉干扰（如动态背景、相机晃动、颜色变化）。
- **现有方法短板**：以往的 Latent Action 方法（如 LAPO）虽然能在纯净视频中从观测序列推断出代理动作，但一旦出现视觉干扰，性能会急剧下降，因为模型容易过拟合到非因果的干扰模式上。
- **论文目标**：提出 **对象中心潜在动作学习**（Object-Centric Latent Action Learning）框架，不再直接从原始像素学习，而是通过自监督对象中心表示将智能体运动与背景干扰解耦，从而在强干扰下获得更可靠的潜在动作，提升模仿学习效果。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程
整体流程分为四个阶段：对象中心预训练 → 动作相关槽自动选择 → 潜在动作建模 → 行为克隆与微调。

- **对象中心预训练**：
  - 采用 VideoSAUR 模型，将视频帧序列分解为固定数量 $K$ 的对象槽（slot）$\mathbf{s}^{(k)}_{t}$，每个槽编码某个实体或区域的特征。
  - VideoSAUR 使用基于 Transformer 的解码器及注意力 mask，可将每个槽投影回图像空间，得到可解释的对象掩码 $\mathbf{m}^{(k)}_{t}$。
  - 为保持一致性，使用固定槽初始化，使得同一槽索引在不同片段中对应类似的语义对象。

- **槽选择（Slot Selection）**：
  - 利用少量带标签轨迹，对每个槽的表示做 PCA 降维，再训练一个**线性动作探针**（Linear Action Probe）回归真实动作，以均方误差（MSE）作为该槽与动作相关性的衡量指标（MSE 越低，相关性越高）。
  - 自动选择最相关的一个或几个槽，构成任务相关槽集合 $\mathcal{K}^\star$，参与后续建模。

- **潜在动作建模**（基于 LAPO 框架）：
  - **LAPO-slots**：在潜在空间操作。逆动态模型 $f^s_{\text{IDM}}(z_t|\mathbf{s}_t,\mathbf{s}_{t+1})$ 从相邻槽嵌入推断潜在动作 $z_t$；前向动态模型 $f^s_{\text{FDM}}(\hat{\mathbf{s}}_{t+1}|\mathbf{s}_t,z_t)$ 基于当前槽和 $z_t$ 预测下一时刻槽嵌入。训练目标为最小化重构误差 $\|\hat{\mathbf{s}}_{t+1} - \mathbf{s}_{t+1}\|^2$。
  - **LAPO-masks**：在像素空间操作。利用选中槽的掩码 $\mathbf{m}^{(k)}_t$ 对原始帧过滤，仅保留任务相关区域，然后训练前向动态模型对该过滤图像进行预测，重构目标为下一帧过滤图像。

- **行为克隆与微调**：
  - 使用推断出的潜在动作 $z_t$ 作为伪标签，训练行为克隆（BC）策略 $\tilde{\pi}(z_t|o_t)$。
  - 最后用极少量的真实动作标注数据（≤ 2.5% 数据集）对该策略进行微调，使其适配真实动作空间。

## 3. 实验设计：数据集 / 场景、基准和方法对比
- **数据集与环境**：
  - **Distracting Control Suite (DCS)**：基于 DMControl，增加三种视觉干扰（动态背景视频、颜色偏移、相机扰动），设置两个难度等级：仅动态背景（DCS），以及全部干扰叠加（DCS‑hard）。任务：cheetah-run、walker-run、hopper-hop、humanoid-walk。
  - **Distracting MetaWorld (DMW)**：在 MetaWorld 基础上加入动态背景干扰。任务：hammer、bin-picking、basketball、soccer。
- **评估指标**：
  - DCS 任务：归一化回合回报（Normalized Return），以使用全部真动作训练的 BC 策略得分为 1.0。
  - DMW 任务：归一化成功率（Normalized Success Rate），同样以全监督 BC 为 1.0。
- **对比方法**：
  - **LAPO**（原始方法，在带干扰数据上训练，作为基线）。
  - **LAPO-clean**（在纯净无干扰数据上训练，作为性能上界）。
  - **LAPO-slots**（本文方法，基于对象槽潜在空间建模）。
  - **LAPO-masks**（本文方法，基于对象掩码像素建模）。
- **实验设置**：所有模型使用相同数据集，BC 代理在不同数量的真实标签轨迹下微调（4‑512 条），多个随机种子取平均。

## 4. 资源与算力
论文中未明确说明使用的 GPU 型号、数量、具体训练时间或总计算资源消耗。这部分信息在提供的文本中缺失。

## 5. 实验数量与充分性：实验是否充分、客观、公平
- **实验数量较丰富**：
  - 两个主要基准环境（DCS、DCS‑hard、DMW）共 8 个任务。
  - 每种方法在不同微调数据量（4 ~ 128 / 256 ~ 512 条轨迹）下评估，对应图 1 和图 4 的多组实验。
  - 针对槽数量 $K$ 的鲁棒性研究（$K$ 从 2 到 15）和槽选择机制的分析（线性探针相关性、不同槽组合对下游性能的影响）。
  - 对方法变体（slots vs. masks）和不同干扰程度的敏感性测试。
- **公平性**：
  - 所有对比方法使用相同的专家数据集和相同的评估流程；上限 LAPO‑clean 给出了纯净性能参考。
  - 报告多随机种子平均值，增强统计可靠性。
- **潜在不足**：
  - 未在更多复杂环境（如真实机器人视频、多物体变化场景）上测试，泛化证据有限。
  - 消融内容较集中，对关键设计（如固定初始化、PCA 步骤）的独立消融未特别细述，但整体实验比较系统。

## 6. 论文的主要结论与发现
- 对象中心表示可大幅缓解视觉干扰对潜在动作学习的影响：LAPO-slots 和 LAPO-masks 在所有任务中均优于基准 LAPO，平均将性能差距（相比纯净上限）缩小约 50%，在 humanoid-walk 等复杂任务上甚至超过 100%。
- 提出的线性动作探针能自动筛选与控制相关的槽，且探针得分与下游 BC 性能强相关，可降低对手工标注的依赖。
- 方法对槽数量 $K$ 具有很好的鲁棒性：在 DMW 任务中，$K$ 从 2 到 15 均取得优于基准的性能。
- 在叠加多种干扰（DCS‑hard）时，基于槽嵌入的 LAPO-slots 仍保持稳健增益，而基于视觉掩码的 LAPO-masks 增益有所下降，推测与 VideoSAUR 使用的稳健语义编码器有关。
- VideoSAUR 在有干扰时倾向于将功能上耦合的物体合并为同一个槽，这种“功能性分解”在实际数据有限时反而有利于下游学习。

## 7. 优点：方法或实验设计上的亮点
- **对象中心与潜在动作学习的融合**：首次将对象中心解耦思想引入 LAPO 框架，为在干扰视频上学习动作提供了新的强归纳偏置。
- **自动槽选择机制**：无需人工指定哪个物体是智能体，通过线性探针实现端到端的自动选择，实用性强。
- **两个模态的模型设计**：提供潜在空间和像素空间两种实现，兼顾稳健性和可解释性。
- **在连续控制和高维干扰下的全面验证**：覆盖两类环境、多种难度、多种任务，证明了方法的通用性和增益。
- **对槽数量不敏感**：降低了调参难度，适合真实世界中物体数量未知的场景。

## 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等
- **依赖 OCL 模型性能**：方法高度依赖于 VideoSAUR 的分解质量，当视频中物体过少或多样性不足时，会出现槽合并或坍缩现象；对严重遮挡、多视角的鲁棒性未探讨。
- **固定槽数量假设**：当前方法需要预先设定 $K$，尽管实验结果对此不敏感，但理论上仍是一个限制，未能适应物体数量变化的场景。
- **缺乏真实世界数据验证**：所有实验均在仿真环境（DCS、DMW）中进行；真实互联网视频的动态复杂性和相机运动可能超出当前 OCL 模型的能力。
- **未涉及动作多样性评估**：评价集中于模仿学习性能，没有对推断出的潜在动作本身的语义质量、解耦程度做深入分析。
- **对额外干扰类型研究有限**：尽管测试了 DCS‑hard，但主要结论仍以动态背景为主导，相机和颜色变化单独的影响未作细致区分。
- **监督信号的使用**：槽选择阶段依赖少量真实动作标签来训练探针，虽然用量很少，但在完全无标签的场景下需另寻他法。

（完）
