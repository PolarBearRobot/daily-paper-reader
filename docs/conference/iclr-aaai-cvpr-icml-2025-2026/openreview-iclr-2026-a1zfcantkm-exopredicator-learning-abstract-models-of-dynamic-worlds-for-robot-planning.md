---
title: "ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning"
title_zh: ExoPredicator：学习动态世界的抽象模型用于机器人规划
authors: "Yichao Liang, Thanh Dat Nguyen, Cambridge Yang, Tianyang Li, Joshua B. Tenenbaum, Carl Edward Rasmussen, Adrian Weller, Zenna Tavares, Tom Silver, Kevin Ellis"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=a1zfcaNTkM"
tags: ["query:model"]
score: 8.0
evidence: 抽象世界模型，联合学习内生与外生因果过程用于机器人规划
tldr: 长程规划中常忽略世界外生过程。ExoPredicator提出联合学习符号状态表示和内生/外生因果过程的抽象世界模型，通过变分贝叶斯推理和LLM提议进行高效规划。在五个模拟桌面环境实验中，所学模型能快速规划并泛化到物体更多、更复杂的任务，为世界模型赋予外生建模能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有世界模型只考虑主体动作，忽略环境中的外生动态过程。
method: 联合学习符号状态及内生/外生因果过程，利用变分贝叶斯与LLM。
result: 在模拟环境中实现快速规划，并泛化到更复杂的未见任务。
conclusion: 纳入外生过程的世界模型能显著提升机器人长程规划能力。
---

## Abstract
Long-horizon embodied planning is challenging because the world does not only change through an agent's actions: exogenous processes (e.g., water heating, dominoes cascading) unfold concurrently with the agent's actions. We propose a framework for abstract world models that jointly learns (i) symbolic state representations and (ii) causal processes for both endogenous actions and exogenous mechanisms. Each causal process models the time course of a stochastic cause-effect relation. We learn these world models from limited data via variational Bayesian inference combined with LLM proposals. Across five simulated tabletop robotics environments, the learned models enable fast planning that generalizes to held-out tasks with more objects and more complex goals, outperforming a range of baselines.

---

## 论文详细总结（自动生成）

基于提供的论文元数据（标题、摘要、作者、结论等），对该论文进行如下结构化总结。注意，由于未获得完整 PDF 内容，部分细节如算力资源、具体实验组数等无法从元数据中提取，将在相应位置注明。

---

## 1. 核心问题与研究动机

- **核心问题**：长程具身规划（long-horizon embodied planning）通常只考虑智能体自身动作对环境的影响，而忽略了环境中**外生过程**（exogenous processes）——即与智能体动作并行的动态变化，例如水加热、多米诺骨牌连锁倾倒等。
- **研究动机**：真实世界中，许多因果过程不受智能体控制，却深刻影响任务成败。现有世界模型（world models）仅建模智能体动作的效应，导致在包含外生动态的场景中规划失效或低效。因此，需要一种能**同时学习内生与外生因果过程**的抽象世界模型，以提升长程规划的准确性和泛化能力。

---

## 2. 方法论

### 2.1 核心思想
- 提出 **ExoPredicator** 框架，**联合学习**：
  - (i) 符号化的状态表示（symbolic state representations）；
  - (ii) 内生动作（endogenous actions）与外生机制（exogenous mechanisms）的因果过程。
- 每个因果过程建模**一个随机因果关系的时程**（time course of a stochastic cause-effect relation）。

### 2.2 关键技术细节
- **模型学习**：从有限数据中学习世界模型，采用**变分贝叶斯推理（variational Bayesian inference）**。
- **先验/提议**：融合**大语言模型（LLM）的提议**（proposals）来辅助推理或生成合理的因果结构/状态抽象。
- **规划**：基于学到的抽象世界模型进行快速规划，支持在具有更多对象和更复杂目标的场景下运行。

### 2.3 算法流程（文字描述）
1. 从交互轨迹数据中抽取状态-动作-外生事件的序列。
2. 利用变分贝叶斯推断，同时推断符号状态空间划分以及内生/外生因果过程的参数。
3. LLM 提供关于状态抽象或因果依赖关系的先验建议，压缩推断搜索空间。
4. 在线规划阶段，使用学到的因果过程预测环境演化，进行模型预测控制（MPC）或搜索式规划。

（注：具体公式与算法伪代码在元数据中未给出，仅为逻辑推断。）

---

## 3. 实验设计

### 3.1 环境与场景
- **五个模拟桌面机器人环境**（simulated tabletop robotics environments），具体名称未在元数据中列出。
- 每个环境均包含外生动态（如物体加热、连锁反应等）。

### 3.2 评估基准（Benchmark）
- 规划任务分为**训练时见过的设置**和**留出任务（held-out tasks）**。
- 留出任务包含**更多物体**和**更复杂的目标**，用于测试泛化能力。
- 对比指标推测为规划成功率、规划步数或效率（元数据未明确给出，仅提及“outperforming”）。

### 3.3 对比方法
- 与**一系列基线方法**对比（a range of baselines），但基线名称在元数据中未列出。
- 推测可能包括：仅建模内生动作的符号规划器、端到端学习的世界模型（如Dreamer系列）、基于LLM直接规划的方法等。

---

## 4. 资源与算力

- 元数据中**未提供**任何关于 GPU 型号、数量、训练时长或算力消耗的信息。
- 因此，无法评估该方法的计算资源需求及实际部署成本。

---

## 5. 实验数量与充分性

- 明确提到 **5个模拟环境**，并包含**留出任务（更复杂的目标和更多物体）**，显示至少进行了环境类型和泛化难度的交叉评估。
- 由于缺少完整论文，无法确定是否包含消融实验（如去除外生建模、去除LLM提议等），但从“jointly learns”和“combined with LLM proposals”的贡献点推测，作者很可能进行了对应消融。
- 对比“一系列基线”，说明实验对比维度较全面。
- **充分性初步判断**：基于摘要信息，实验设计覆盖多环境、泛化能力比较，具备基本说服力；但缺乏细节，无法判断统计显著性、重复次数等。

---

## 6. 主要结论与发现

- 联合学习符号状态表示与内生/外生因果过程的抽象世界模型，能**显著提升机器人长程规划能力**。
- 从有限数据中学到的模型可以实现**快速规划**，并且**泛化到拥有更多物体和更复杂目标的未见任务**上。
- 该方法**全面优于**对比基线，验证了对外生过程建模的重要性。

---

## 7. 优点与亮点

- **问题新颖性**：首次将外生动态过程显式集成到可学习的抽象世界模型中，切合真实机器人规划的痛点。
- **方法融合**：将**结构化因果建模**与**变分推理**、**LLM先验**结合，兼具符号可解释性和统计效率。
- **泛化能力**：不仅在训练场景有效，还能推广到更复杂的、未见过的任务配置，显示模型的抽象性和鲁棒性。
- **数据效率**：强调从“有限数据”学习，符合机器人领域数据稀缺的现实。

---

## 8. 不足与局限

- **信息缺失严重**：由于仅有摘要和元数据，无法评估以下关键点：
  - 实验的具体环境细节、任务定义、评价指标；
  - 基线的类型和实现水平，是否公平对比；
  - 消融实验是否存在及其结论；
  - 计算开销是否可接受；
  - 外生过程的覆盖种类是否多样；
  - 对感知噪声、动作执行误差的鲁棒性。
- **应用限制**：目前仅在**模拟桌面环境**中验证，真实世界的传感器噪声、非确定性外生事件（如人为干扰）可能带来挑战。
- **LLM依赖**：利用LLM提议可能引入外部知识，但也可能限制场景到LLM已知范畴，且增加运行时成本。
- **可扩展性未知**：符号状态表示在面对高维感知时可能需要额外学习模块（如视觉编码器），文中未提及其结合方式。

---

（完）
