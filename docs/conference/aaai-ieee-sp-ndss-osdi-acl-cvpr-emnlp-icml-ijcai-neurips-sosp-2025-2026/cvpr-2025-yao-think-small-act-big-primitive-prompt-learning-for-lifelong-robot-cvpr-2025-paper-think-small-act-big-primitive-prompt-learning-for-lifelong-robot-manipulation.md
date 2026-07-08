---
title: "Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation"
title_zh: 见微知著：面向终身机器人操作的基元提示学习
authors: "Yao, Yuanqi, Liu, Siao, Song, Haoming, Qu, Delin, Chen, Qizhi, Ding, Yan, Zhao, Bin, Wang, Zhigang, Li, Xuelong, Wang, Dong"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yao_Think_Small_Act_Big_Primitive_Prompt_Learning_for_Lifelong_Robot_CVPR_2025_paper.pdf"
tags: ["query:analysis"]
score: 9.0
evidence: 学习可重用的基元提示作为机器人操作技能的动作表示
tldr: 针对通用机器人持续技能获取中难以利用共享基元的挑战，提出基元提示学习（PPL）框架，通过多技能预训练学习运动感知提示来捕获跨技能的语义和运动基元，再组合基元学习新技能。该方法实现了终身机器人操作，有效避免了灾难性遗忘，为基元化表示学习提供了新思路。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 777, \"height\": 827, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1674, \"height\": 621, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1709, \"height\": 815, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1703, \"height\": 572, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1767, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1761, \"height\": 502, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 845, \"height\": 369, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 870, \"height\": 203, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 863, \"height\": 494, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1443, \"height\": 394, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 865, \"height\": 441, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yao-think-small-act-big-primitive-prompt-learning-for-lifelong-robot-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 874, \"height\": 176, \"label\": \"Table\"}]"
motivation: 现有方法无法利用技能间的共享基元，导致持续学习低效。
method: 两阶段学习：预训练运动感知提示捕获基元，再组合提示学新技能。
result: 在终身学习中有效组合基元，保持了旧技能并快速获取新技能。
conclusion: PPL展示了基元提示作为可重用动作表示的优越性。
---

## Abstract
Learning a generalist robot that can effectively leverage prior knowledge for continuous skill acquisition remains significantly challenging. Despite the success of experience replay and parameter-efficient methods in maintaining knowledge across skills, naively applying these methods causes a failure to leverage the shared primitives between skills. To tackle these issues, we propose Primitive Prompt Learning (PPL), to achieve lifelong robot manipulation via reusable and extensible primitives. Within our two stage learning scheme, we first learn a set of primitive prompts to model primitives through multi-skills pre-training stage, where motion-aware prompts are learned to capture semantic and motion shared primitives across different skills. Secondly, when acquiring new skills in lifelong span, new prompts are concatenated and optimized with frozen pretrained prompts, boosting the learning via knowledge transfer from old skills to new ones. For evaluation, we construct a large-scale skill dataset and conduct extensive experiments in both simulation and real-world tasks, demonstrating PPL's superior performance over state-of-the-art methods.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：通用机器人进行终身学习时，如何有效利用已有技能中的共享“基元”（primitives）来加速新技能的获取，同时避免灾难性遗忘。现有方法（如经验回放、参数高效适配）往往忽略技能之间底层的运动模式共性，导致知识迁移低效。
- **整体含义**：作者认为技能在语义层面虽可能不同，但在运动基元层面存在大量可复用的模式（如“抓香蕉”和“放罐子”共享精确夹取类的运动模式）。因此，通过显式提取并复用这些“基元提示”（primitive prompts），可以更高效地实现终身操控学习。

### 2. 论文提出的方法论
核心思路是两阶段框架 **Primitive Prompt Learning (PPL)**：
- **第一阶段：多技能预训练（学习基元提示）**
  - 基于扩散Transformer策略，在注意力层的键（Key）和值（Value）前插入可学习的提示向量 ${p_K, p_V}$。
  - 设计**运动感知提示（Motion-Aware Prompting, MAP）**查询机制：利用视觉光流（RAFT提取）捕获跨技能共享的低层运动模式，结合CLIP文本嵌入保留任务语义，通过加权求和生成最终的提示向量 $P = \sum_m \alpha_m P_m$。权重 $\alpha$ 由查询向量与提示成分键的余弦相似度计算得出。
  - 该阶段让模型自动学习一组可复用的基元提示，这些提示隐式编码了不同技能间共享的语义和运动基础单元。
- **第二阶段：终身技能获取（组合与扩展提示）**
  - 冻结预训练阶段学到的基元提示。
  - 遇到新技能时，新增可训练的终身提示向量$P'$（以及对应的键$K'$和注意力向量$A'$），与冻结的旧提示拼接后共同参与加权求和。
  - 仅优化新提示对应的参数，权重计算仍涉及所有历史提示，从而实现从旧技能到新技能的知识迁移，且无需访问旧数据。

**算法流程简化表示**：
1. 初始化基元提示 $p$。
2. 对每个训练技能：计算光流 → MAP生成查询 → 前缀提示插入Transformer → 计算扩散损失并更新提示和模型参数。
3. 对每个新技能：初始化新提示组件 → 与冻结旧提示拼接 → 计算注意力权重 → 生成新提示 → 仅优化新参数 → 将新提示加入提示集合。

### 3. 实验设计
- **数据集与场景**：
  - **仿真大规模技能数据集**：基于MimicGen和LIBERO构建，包含多种操作技能（如抓、放、开关抽屉等），每个技能含约1K条人类演示，初始状态分布广泛。
  - **真实世界**：使用Franka Panda机械臂，4个预训练技能+4个终身技能，涵盖抓、放、推等动作，物体随机放置以测试泛化性。每个技能200条演示，每任务独立评估15次。
- **基准与对比方法**：
  - 传统序列学习方法（Sequential Fine-tuning）。
  - 经验回放（ER）。
  - 基于适配器的方法：LoRA（任务特定低秩适配）、MOE（混合专家策略）等。
- **评估指标**：前向迁移权重（FWT，新任务最高成功率）和后向迁移权重（BWT，学新任务后旧任务性能平均提升量）。

### 4. 资源与算力
- 论文**未明确说明**所使用的GPU型号、数量或具体训练时长。仅从方法涉及扩散Transformer、光流计算等推断，训练应需要中高端GPU支持，但缺少量化信息。

### 5. 实验数量与充分性
- **实验组数**：
  - 仿真多技能预训练：LIBERO-GOAL上4项任务的对比（Diff-T、MOE vs. PPL）。
  - 仿真终身学习：MimicGen上7个序列任务的FWT/BWT对比（Sequential、ER、LoRA vs. PPL）。
  - 真实世界多技能预训练与终身学习：各4-5项任务。
  - 消融实验：运动感知提示的有效性（文本查询 vs. 文本+光流查询）、基元提示数量的影响、基元提示机制本身的作用（有无预训练提示、有无使用预训练提示）。
  - 鲁棒性分析：在模拟动态光照变化（暖→冷→暗）下测试性能。
- **充分性与公平性**：实验覆盖了仿真和现实、多种主流对比方法、多项消融和鲁棒性测试，任务多样，评估指标明确且多次独立运行。对比公平（均基于同数据集和演示），结果呈现标准差，能较好验证方法的有效性。

### 6. 论文的主要结论与发现
- PPL通过运动感知提示建模可复用基元，在预训练阶段即捕捉跨技能的共享运动-语义表示。
- 在终身学习阶段，仅扩展少量新提示即可实现高效知识迁移，无需回放旧数据，性能显著优于现有序列学习、经验回放和LoRA方法。
- 运动感知查询（结合光流与语义）比纯文本查询更能发现语义不同但运动相似技能间的共享基元，从而提升知识复用。
- 提示数量需适中，过多引入噪声，过少则难以覆盖所有基元。
- 面对剧烈光照变化时，仅依赖光流的提示鲁棒性下降，纯文本查询反而更稳定。

### 7. 优点
- **新颖的基元提示范式**：将技能分解为可学习提示，实现模块化和可扩展的终身学习。
- **运动感知设计**：融合光流与文本语义，使模型能从运动角度挖掘跨技能共性，突破纯粹语义限制。
- **参数高效**：增式学习时仅需为新技能增加少量参数，不与旧数据交互，适合现实部署。
- **实验完整**：兼具仿真与真实世界、大规模技能数据集、多项对比和消融，结论可信度高。

### 8. 不足与局限
- **光流依赖的脆弱性**：实验表明在极端光照变化下性能下降，纯文本查询更鲁棒，暗示光流特征对环境敏感，实用性受限于复杂视觉条件。
- **实时性考量不足**：光流提取（RAFT）和扩散策略推理可能增加计算开销，论文未讨论部署的实时性能。
- **提示数量需手动调节**：基元提示数量需根据技能集大小调整，缺乏自动确定机制。
- **真实世界技能数量有限**：真实实验仅覆盖8个技能，更大规模技能库下的可扩展性未充分验证。
- **缺乏与更先进终身学习方法的对比**：未比较一些注重结构剪枝或动态扩展的新方法。

（完）
