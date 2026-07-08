---
title: "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models"
title_zh: CoT-VLA：面向视觉-语言-动作模型的视觉链式思维推理
authors: "Zhao, Qingqing, Lu, Yao, Kim, Moo Jin, Fu, Zipeng, Zhang, Zhuoyang, Wu, Yecheng, Li, Zhaoshuo, Ma, Qianli, Han, Song, Finn, Chelsea, Handa, Ankur, Lin, Tsung-Yi, Wetzstein, Gordon, Liu, Ming-Yu, Xiang, Donglai"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"
tags: ["query:model"]
score: 9.0
evidence: 将视觉链式思维推理融入VLA，用于复杂操作任务。
tldr: 现有VLA缺乏中间推理步骤，难以完成长程操作任务。本文提出CoT-VLA，通过自回归预测未来图像帧作为视觉目标，再生成动作序列，从而在VLA中实现显式的视觉推理，提升复杂任务的规划能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 850, \"height\": 999, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1798, \"height\": 556, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 655, \"height\": 592, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1811, \"height\": 424, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1746, \"height\": 1196, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 866, \"height\": 632, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1565, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 875, \"height\": 507, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 852, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhao-cot-vla-visual-chain-of-thought-reasoning-for-vision-language-action-models-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 845, \"height\": 195, \"label\": \"Table\"}]"
motivation: 当前VLA模型直接映射输入到输出，缺少中间推理，难以处理复杂操作。
method: 在VLA中加入视觉链式推理模块，先预测未来视觉目标帧，再据此生成动作。
result: 在需要多步规划的操作任务中，CoT-VLA显著提升了成功率和泛化性。
conclusion: 视觉链式推理为VLA提供了有效的规划能力，是迈向通用机器人操作的重要一步。
---

## Abstract
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Videos are available at: https://cot-vla.github.io/.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：当前的视觉‑语言‑动作模型（VLA）大多采用从感知直接映射到动作的端到端方式，缺乏显式的中间推理步骤，导致模型在面对需要多步规划、长程时间关联的复杂操作任务时表现不足。
- **整体含义**：本文提出将“视觉链式思维（Visual Chain‑of‑Thought）”引入 VLA 框架，在产生动作序列之前先自回归地预测未来的视觉子目标图像，从而让模型拥有“先思考再行动”的能力。这种设计不仅增强了模型对复杂操作的规划和推理能力，还可以利用大量不含动作标注的视频数据来提升视觉推理的泛化性，为通用机器人操作提供了新的思路。

### 2. 论文提出的方法论
- **核心思想**：视觉链式思维推理（Visual CoT Reasoning）在 VLA 中体现为两步生成过程：
  1. 根据当前观测和语言指令，自回归地生成一张未来时刻的子目标图像（subgoal image），作为中间推理状态。
  2. 以当前观测和生成的子目标图像为条件，一次性预测一短序列动作以实现该子目标。
- **底座模型**：基于统一多模态基础模型 VILA‑U（7B 参数），它能够理解并生成图像与文本标记，使用残差量化（RQ‑VAE）将图像编码为离散视觉 token。
- **关键技术细节**：
  - **混合注意力机制（Hybrid Attention）**：对视觉和文本 token 的预测采用因果注意力（causal attention）以保持自回归生成顺序；对动作 token 的预测则采用全注意力（full attention），允许所有动作维度相互交互，一次性预测整个动作序列。
  - **动作分块（Action Chunking）**：预测长度为 $m$ 的动作序列，而非单一动作，减少推理频率并提升动作连贯性。论文中 $m=10$。
  - **损失函数**：
    - 视觉 token 预测：在残差量化的深度 transformer 上，对每个位置的残差 token 序列使用负对数似然损失，$\mathcal{L}_{\text{visual}} = -\sum_{j}\sum_{d=1}^{D} \log P_\delta(k_j^d | k_j^{<d})$。
    - 动作 token 预测：交叉熵损失，$\mathcal{L}_{\text{action}} = -\sum_{i=1}^{m} \log P_\theta(a_{t}...a_{t+m} | l, s_t, s_{t+n})$。
    - 总损失：$\mathcal{L} = \mathcal{L}_{\text{action}} + \mathcal{L}_{\text{visual}}$。
- **训练流程**：
  - **预训练阶段**：同时使用来自 Open X‑Embodiment 的机器人演示数据（含动作标注）以及无动作视频数据（EPIC‑KITCHENS、Something‑Something V2）训练子目标生成能力；动作预测仅在机器人数据上训练。
  - **下游适应阶段**：在目标机器人平台上，用少量任务演示微调整个模型（冻结视觉塔）。

### 3. 实验设计
- **评估环境与数据集**：
  - **LIBERO 模拟基准**：四个任务套件（Spatial, Object, Goal, Long），每套件 10 个任务，每个任务 50 条演示，全面考察空间关系、物体交互、目标理解与长程能力。
  - **Bridge‑V2 真实机器人平台**：使用 WidowX 机械臂，基于 45k 语言标注轨迹，测试四个泛化维度（视觉鲁棒性、运动泛化、语义泛化、指令基础）。
  - **Franka‑Tabletop 真实机器人平台**：使用 Franka Emika Panda 7‑DoF 机械臂，单指令与多指令任务共 6 个，演示数据 10~150 条，评估少样本自适应能力。
- **对比方法**：
  - **Diffusion Policy**：从头训练的行为克隆方法，含动作分块与本体感知。
  - **Octo**：基于 OpenX 的通用策略模型，无 VLM 初始化。
  - **OpenVLA**：开源 VLA 模型，基于 VLM 微调。
  - **SUSIE**：两阶段方法，先用图像编辑扩散生成目标，再训练目标条件策略（仅 Bridge‑V2）。
- **评价指标**：任务成功率（含标准差/标准误差），多次试验取均值。

### 4. 资源与算力
- 论文中未明确说明训练所使用的 GPU 型号、数量以及具体训练时长。
- 模型基座为 7B 参数的 VILA‑U，预训练涉及 OpenX 大规模数据集及额外视频数据，可推测需要较高的计算资源，但缺少可量化的细节。

### 5. 实验数量与充分性
- **主要实验组数**：
  - LIBERO：4 个套件 × 500 次试验 × 3 随机种子。
  - Bridge‑V2：4 个泛化任务 × 10 次试验。
  - Franka‑Tabletop：6 个任务，多次试验统计成功率。
  - 消融研究：在 LIBERO‑Spatial 和 LIBERO‑Goal 上比较 VLA 基础版、+动作分块、+混合注意力、完整 CoT‑VLA 共 4 种配置。
  - 预训练消融：在 Franka‑Tabletop 上，对比直接微调 VILA‑U 与经过预训练的 CoT‑VLA。
  - 视觉推理质量分析：2 个新组合长程任务，对比生成子目标与真实子目标下的成功率。
- **充分性与公平性**：实验覆盖模拟与真实世界、多类任务、多种基线，消融实验系统性地验证了各个模块贡献，评估过程遵循标准协议（如使用相同预处理、多次试验），整体设计较为全面且公平。

### 6. 论文的主要结论与发现
- 视觉链式思维推理能够显著提升 VLA 在复杂操作任务上的表现：在 LIBERO 上平均成功率高达 81.13%，超越最强基线 6% 以上；在 Franka‑Tabletop 真实场景超越 OpenVLA 平均达 17%；在 Bridge‑V2 上也展现了竞争力的泛化能力。
- 动作分块与混合注意力均对性能有正面贡献，且视觉 CoT 为最大的性能推动力。
- 利用无动作视频数据进行预训练可有效增强视觉推理能力，从而提高下游任务成功率（相对提升 46.7%）。
- 更好的子目标生成质量可直接转化为更高的任务成功率，表明视觉推理是提升动作执行能力的关键瓶颈之一。

### 7. 优点
- **创新性强**：首次将子目标图像作为显式视觉 CoT 推理步骤融入 VLA 框架，以可解释、自然的方式赋予模型规划能力。
- **模块设计合理**：混合注意力兼顾生成与预测的特性，动作分块减少推理频次，整体架构由统一多模态模型支撑，端到端可训练。
- **数据效率高**：通过视觉推理过程，能够利用大量无动作标注的视频丰富视觉先验，缓解机器人数据稀缺问题。
- **实验扎实**：覆盖模拟与真实环境、多类机器人平台和任务，消融实验完整，对比公平，结论可信度高。

### 8. 不足与局限
- **推理速度慢**：每次推理需先生成 256 个图像 token，导致平均 7 倍于直接动作生成的延迟，虽通过动作分块缓解，但仍为部署瓶颈。
- **视觉生成质量受限**：自回归图像生成在画质和准确性上弱于扩散模型，可能影响子目标质量，进而限制最终任务性能。
- **动作分块的连续性缺陷**：跨分块的边界可能出现动作跳跃，且执行过程中缺乏高频反馈修正。
- **新任务泛化有限**：在完全未见的、需要长程组合的任务上，子目标生成能力仍显不足，模型的计算约束限制了更大规模视频预训练带来的泛化增益。
- **资源描述不透明**：未提供详细的算力需求，不利于复现和成本评估。

（完）
