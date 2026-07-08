---
title: "RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems"
title_zh: RoboMemory：面向物理具身系统的类脑多记忆智能体框架
authors: "Mingcong Lei, Honghao Cai, Zezhou Cui, Liangchen Tan, Junkun Hong, Gehan Hu, Shuangyu Zhu, Yimou Wu, Shaohan Jiang, Ge Wang, Yuyuan Yang, Junyuan Tan, Zhenglin Wan, Zhen Li, Shuguang Cui, Yiming Zhao, Yatong Han"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=ey2w57KZTe"
tags: ["query:model"]
score: 10.0
evidence: 类脑多记忆框架，集成空间/时间/情景/语义记忆用于长程规划
tldr: "具身智能体面临部分可观测、空间推理弱和记忆集成延迟等挑战。RoboMemory提出类脑多记忆框架，统一空间、时间、情景和语义记忆，并采用动态空间知识图谱保证记忆更新一致性。在EmbodiedBench上，该方法使基于Qwen2.5-VL-72B-Ins的智能体平均成功率提升25%，证明了多记忆机制对物理交互环境学习的重要性。"
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 具身智能体在真实环境中面临多记忆集成和长程规划的困难。
method: 提出并行化多记忆架构，结合动态空间知识图谱与闭环规划器。
result: 在EmbodiedBench上显著提升任务成功率，验证多记忆的有效性。
conclusion: 多记忆框架能有效提升具身智能体的长期交互学习能力。
---

## Abstract
Embodied agents face persistent challenges in real-world environments, including partial observability, limited spatial reasoning, and high-latency multi-memory integration. We present RoboMemory, a brain-inspired framework that unifies Spatial, Temporal, Episodic, and Semantic memory under a parallelized architecture for efficient long-horizon planning and interactive environmental learning. A dynamic spatial knowledge graph (KG) ensures scalable and consistent memory updates, while a closed-loop planner with a critic module supports adaptive decision-making in dynamic settings. Experiments on EmbodiedBench show that RoboMemory, built on Qwen2.5-VL-72B-Ins, improves average success rates by 25% over its baseline and exceeds the closed-source state-of-the-art (SOTA) Gemini-1.5-Pro by 3%. Real-world trials further confirm its capacity for cumulative learning, with performance improving across repeated tasks. These results highlight RoboMemory as a scalable foundation for memory-augmented embodied intelligence, bridging the gap between cognitive neuroscience and robotic autonomy.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **研究动机**：具身智能体在真实物理环境中长期面临三大难题：环境部分可观测、空间推理能力薄弱、多种记忆机制（空间、时间、情景、语义）的集成延迟高且难以协同。
- **整体含义**：本文提出类脑架构“RoboMemory”，将多种记忆统一在并行化框架下，旨在弥合认知神经科学与机器人自主性之间的鸿沟，提升交互式环境学习与长程规划能力。

### 2. 论文提出的方法论

- **核心思想**：模拟人脑多记忆系统的协作方式，将空间记忆、时间记忆、情景记忆和语义记忆并行化集成，实现高效的长时序决策与持续环境学习。
- **关键技术细节**：
  - **多记忆并行架构**：四种记忆模块同时运行，通过统一接口交互，避免串行延迟。
  - **动态空间知识图谱（KG）**：以知识图谱的形式维护环境的空间关系与物体状态，支持可扩展、一致性的记忆更新。
  - **闭环规划器 + Critic 模块**：规划器根据当前记忆生成动作，Critic 模块实时评估动作合理性并反馈，形成自适应闭环决策。
- **算法流程**（文字概括）：
  1. 智能体通过视觉等感知输入提取特征，更新四种记忆。
  2. 动态 KG 融合空间与语义信息，保证记忆间的一致性。
  3. 闭环规划器基于融合后的记忆生成候选动作序列。
  4. Critic 模块对候选序列评分，选出最优动作执行，并将结果反馈回记忆系统。

### 3. 实验设计

- **数据集/场景**：主要使用 **EmbodiedBench**（具身智能标准测试平台），并在真实世界环境中进行重复任务验证。
- **基准对比**：
  - **基线方法**：直接使用 **Qwen2.5-VL-72B-Ins** 的智能体。
  - **竞品方法**：闭源 SOTA 模型 **Gemini-1.5-Pro**。
- **评估指标**：任务成功率（平均成功率提升百分比）。

### 4. 资源与算力

- 文中（根据现有信息）**未明确说明**具体使用的 GPU 型号、数量、训练时长或推理算力开销。
- 已知基础模型为 **Qwen2.5-VL-72B-Ins**，意味着推理阶段需要较大显存，但论文未披露更多算力细节。

### 5. 实验数量与充分性

- **实验组数**：摘要仅给出整体提升结果（比自身基线高 25%，比 Gemini-1.5-Pro 高 3%），以及真实世界累积学习表现。从常见投稿模式推测，应包含不同任务类型、不同记忆组合的消融实验，但具体数量未在元数据中体现。
- **充分性与客观性**：
  - 在与基线、外部闭源模型的对比上，结果呈现直接且具有可比性。
  - 但缺乏详细的消融分析（如去除某一记忆模块的影响）和统计显著性检验的说明，可能导致论证不够充分。
  - 整体实验设计框架（基准 + 真实场景）较合理，但细节缺失削弱了可复现性与说服力。

### 6. 论文的主要结论与发现

- 多记忆并行架构能显著提升具身智能体的任务成功率，RoboMemory 在 EmbodiedBench 上超越自基线 25%，并略优于 Gemini-1.5-Pro。
- 动态空间知识图谱有效保证了记忆更新的一致性和可扩展性。
- 真实世界试验表明，框架具备累积学习能力——随着任务重复，性能持续提升。
- 该成果证明认知神经科学的多记忆模型可以成为提升机器人自主性的可扩展基础。

### 7. 优点

- **生物学启发设计**：将人脑记忆系统（空间/时间/情景/语义）工程化，想法新颖且具解释性。
- **多记忆一致性**：通过动态 KG 统一维护，避免了多源记忆冲突的常见问题。
- **强基线比较**：同时对比自基线与闭源 SOTA，性能有明确提升。
- **真实验证**：不仅有仿真基准，还做了物理世界实验，验证了方法的泛化和持续学习能力。

### 8. 不足与局限

- **算力和效率未知**：未给推理延迟、资源消耗等实用指标，72B VL 模型可能部署成本极高。
- **实验细节缺失**：从已有信息看，消融实验、失败案例分析、长期遗忘效应等未提及，可信度受限。
- **任务限制**：仅在 EmbodiedBench 的部分任务上验证，未知在其他具身环境（如 Habitat、AI2-THOR）上的迁移能力。
- **多记忆协同上限**：未讨论记忆模块间可能存在的干扰或冗余，以及并行架构的扩展瓶颈。
- **环境假设**：真实世界试验可能受控场景较简单，复杂动态物理交互下的鲁棒性未充分证明。

（完）
