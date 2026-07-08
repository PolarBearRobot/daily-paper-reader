---
title: Learning Diffusion Policy from Primitive Skills for Robot Manipulation
title_zh: 从基本技能学习扩散策略用于机器人操作
authors: "Zhihao Gu, Ming Yang, Difan Zou, Dong Xu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38889/42851"
tags: ["query:analysis"]
score: 9.0
evidence: 技能条件的扩散策略学习可解释的技能表示，减少机器人操作中的动作生成错位
tldr: 针对传统扩散策略依赖全局指令导致动作生成错位的问题，SDP方法将操作分解为八种可复用的基本技能，利用视觉语言模型提取离散技能表示，并以此条件化扩散策略进行动作规划。实验表明，该方法能生成更精确、可解释的动作序列，显著减少了动作错位。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38889/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 845, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38889/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 806, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38889/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1444, \"height\": 703, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38889/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1566, \"height\": 462, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38889/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1668, \"height\": 340, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38889/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1358, \"height\": 717, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38889/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 866, \"height\": 405, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38889/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 773, \"height\": 546, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38889/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 844, \"height\": 210, \"label\": \"Table\"}]"
motivation: 现有扩散策略的全局指令与短期控制信号间存在错位，导致动作生成不准确。
method: 提出技能条件扩散策略SDP，抽象八种可复用基本技能，并用VLM提取离散表示以条件化动作规划。
result: 在机器人操作任务上减少动作错位，提高了动作生成准确性和可解释性。
conclusion: SDP通过引入技能表示学习，为机器人动作生成提供了更直观有效的接口。
---

## Abstract
Diffusion policies have recently shown great promise for generating actions in robotic manipulation. However, existing approaches often rely on global instructions to produce short-term control signals, which can result in misalignment in action generation. We conjecture that the primitive skills, referred to as fine-grained, short-horizon manipulations, such as "move up" and "open the gripper", provide a more intuitive and effective interface for robot learning. To bridge this gap, we propose SDP, a skill-conditioned diffusion policy that integrates interpretable skill learning with conditional action planning. SDP abstracts eight reusable primitive skills across tasks and employs a vision-language model to extract discrete representations from visual observations and language instructions. Based on the representations, a lightweight router network is designed to assign a desired primitive skill for each state, which helps construct a single-skill policy to generate skill-aligned actions. By decomposing complex tasks into a sequence of primitive skills and selecting a single-skill policy, the proposed SDP ensures skill-consistent behavior across diverse tasks.
Extensive experiments on two challenging simulation benchmarks and real-world robot deployments demonstrate that SDP consistently outperforms state-of-the-art methods, providing a new paradigm for skill-based robot learning with diffusion policies.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：现有扩散策略（如 Language-conditioned DP）通常直接将高层的任务指令（如“把柠檬捡起放到黄色盘子里”）映射到短时动作序列。这种全局指令与具体控制信号之间**粒度不匹配**，导致动作生成出现错位（Misalignment）、模糊或不可靠。
- **整体含义**：作者提出用**可解释的“基本技能”（Primitive Skills）**（如“向上移动”、“闭合夹爪”）作为中间接口，将复杂任务分解为可重用的短时操作单元，从而为扩散策略提供更精确、更直观的条件信号，提升动作生成的准确性、一致性和跨任务泛化能力。

### 2. 论文提出的方法论
核心理念：构建**技能条件的扩散策略（SDP）**，将任务执行抽象为“先分配技能，再按技能生成动作”的过程。

- **技能抽象与提示构建**
  - 从不同任务中归纳出 **8 种可复用的基本技能**：`roll`、`yaw`、`open gripper`、`move up`、`translate`、`close gripper`、`move down`、`rotate`。
  - 设计统一的文本模板：“the robot arm is going to {skill}.”，并利用**组合式提示集成（Compositional Prompt Ensemble, CPE）** 为每种技能生成提示文本，通过冻结的 CLIP 文本编码器和 MLP 得到技能嵌入 $p \in \mathbb{R}^{8 \times C_{\text{img}}}$。

- **技能分配模块**
  - **视觉语言表示**：用共享图像编码器提取静态和手腕相机观测的特征，结合经 tokenizer 处理的高层指令，送入 Transformer 得到多模态表示 $z_{vl}$。
  - **轻量路由器网络**：对 $z_{vl}$ 沿 token 维取平均后，经 MLP、Softmax 和 Top-1 操作，为每个状态输出当前最适合的基本技能索引。最终选取的嵌入 $z$ 将用于条件化后续的扩散策略。

- **技能条件扩散策略**
  - **先验注入**：通过改进的 AdaLN 注入时间步和本体感知信息；视觉语言 tokens 则通过 Cross-Attention 逐层注入。
  - **技能相关的前馈网络**：在扩散策略的每个 Transformer 块中，额外引入一个低秩风格（LoRA-like）的 FFN 层，其参数 $W_z^1, W_z^2$ 由技能嵌入 $z$ 通过 MLP 生成。最终 FFN 输出为`技能相关 FFN(x) + 原始 FFN(x)`，从而显式建立技能与动作预测之间的依赖。
  - **训练目标**：评分匹配损失 $L_{SM}$ 加上正交损失 $L_{Orth}$（促使不同技能嵌入之间余弦相似度降低），总损失 $L = L_{SM} + \gamma L_{Orth}$。

- **推理流程**：给定观测和指令 → VLM+路由器选出当前状态的基本技能 → 技能嵌入参数化 FFN → 条件扩散策略去噪生成技能对齐的动作序列。

### 3. 实验设计
- **模拟基准**
  - **CALVIN**：包含四个场景（A-D），34 种任务，约24k条语言标注演示。评估设定：`ABCD → D` 和更难的 `ABC → D`（零样本泛化到未见环境）。测试集为 1000 条由 5 个连续子任务构成的指令链，指标为每条链上连续完成任务的个数及平均完成长度。
  - **LIBERO**：涵盖四个套件（Spatial、Object、Goal、Long），每个套件 10 个任务，各含 50 条人类遥操作演示。指标为任务成功率。

- **真实世界实验**
  - 自建 9 项任务，使用 6-DoF Lebai 机器人臂，每任务收集 30 条轨迹。评估多任务学习（空间感知、工具使用、语义理解）和视觉泛化（未见物体、背景干扰）。每项任务测评 20 次，报告平均成功率。

- **对比方法**
  - 扩散/行为策略类：DiffPolicy (CNN)、MoDE、MDT。
  - 通用视觉语言动作模型：Octo、OpenVLA、UniVLA、RoboFlamingo、GR-1。
  - 针对 LIBERO 的方法：MaIL、UniActions。
  - 部分基线基于官方代码复现（如 MoDE）。

### 4. 资源与算力
- 训练硬件：模拟任务使用 **4 块 A100 GPU** 微调 40 个 epoch，优化器为 AdamW，学习率 $10^{-4}$，batch size 64。
- 推理成本：SDP 模型参数量 **1017M**，FLOPS **74.5G**，推理时间 **45.1 ms**（仅比 MoDE 多约 14.6 ms），略高于其他扩散策略，但性能提升显著。
- 预训练：基于 OpenX 数据集预训练，未说明预训练具体算力。

### 5. 实验数量与充分性
- **实验组数充分**：
  - **主实验**：2 个 CALVIN 设定 + 4 个 LIBERO 套件 + 9 个真实世界任务，与 10 余种基线对比。
  - **消融实验**：在 CALVIN 和 LIBERO-Long 上验证关键组件（Cross-Attention、先验注入、技能抽象、CPE）和技能条件化策略（加法、拼接、FiLM、本文的 FFN 参数化）。
  - **可视化分析**：展示不同时间步的技能分配和对应的观测，验证技能的可解释性。
  - **复杂度分析**：对比参数量、计算量和推理时间。
- **客观与公平性**：
  - 基线包含多种架构（CNN、Transformer、VLM），均采用标准评测协议，部分基线使用官方代码或论文报告结果。
  - 所有模拟实验基于 3 个种子取平均，报告标准差或平均值。
  - 真实世界实验统一条件，对照组同时微调。

### 6. 论文的主要结论与发现
- SDP 在 CALVIN `ABC → D` 上完成 5 连串任务的成功率**76.9%**，平均完成长度 **4.49**，远超先前最优方法（MoDE 的 62.4%，UniVLA 的 56.5%）。
- 在 LIBERO-Long 上成功率达到 **93.8%**，远超其他通用策略（UniVLA 87.5%），并在四项套件上全部超越 SOTA。
- 真实世界任务中，SDP 在多任务学习和视觉泛化（尤其是未见物体和抗干扰）上均表现出明显优势。
- 可视化显示，模型能自主将高层指令分解为有意义的基本技能序列，并正确执行对应动作，验证了方法的**可解释性和有效性**。

### 7. 优点
- **创新性强**：首次将可解释的基本技能与扩散策略深度结合，通过技能条件化 FFN 层直接指导动作生成，解决了指令 - 动作粒度错位问题。
- **技能设计可复用且显式**：8 种技能具有明确物理含义，可由人类理解，且跨任务共享，无需隐式潜码或额外标注。
- **性能提升显著且一致**：无论在短时复杂任务还是长序列泛化任务上，均远超同类方法，消融实验证实每个组件的正向贡献。
- **训练高效性**：使用 LoRA 式的技能相关 FFN 参数化，在不显著增加推理成本的前提下，实现了更强的条件化能力。
- **可解释性强**：路由器输出的技能分配与观测高度一致，方便开发者理解和调试机器人行为。

### 8. 不足与局限
- **技能集合固定**：仅抽象了 8 种基本技能，可能**无法覆盖所有精细操作**（如推、按、拧等），对需要更高操作粒度的任务泛化能力有限。
- **真实世界评估规模较小**：仅 9 个自定任务、单一机器人平台，**视觉泛化仅测试了苹果和香蕉**等少数物体，对剧烈的形状变化（如香蕉）性能下降，说明对未见物体形状的泛化仍存在挑战。
- **依赖 VLM 预训练质量**：视觉语言表示来自外部模型，其偏误或局限性可能影响路由器技能分配（尤其在新场景下）。
- **计算与内存开销略增**：SDP 参数量（1017M）和推理时间均略高于 MoDE 等基线，对部署在资源受限的边缘设备可能存在瓶颈。
- **无显式长期规划**：技能路由器仅为当前状态分配技能，不保证全局序列的最优性，可能仍依赖扩散策略完成长时依赖的协调。

（完）
