---
title: "STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization"
title_zh: STAR：通过旋转增强向量量化学习多样化机器人技能抽象
authors: "Hao Li, Qi Lv, Rui Shao, Xiang Deng, Yinchuan Li, Jianye HAO, Liqiang Nie"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=n1cqQK4hhC"
tags: ["query:model"]
score: 8.0
evidence: 通过旋转增强向量量化学习多样化机器人技能抽象，用于组合复杂行为
tldr: 针对现有VQ-VAE方法在机器人技能学习中易出现码本坍缩和无法建模技能因果关系的缺陷，提出STAR框架，通过旋转增强残差技能量化（RaRSQ）将编码器输出相对角度编码进梯度，防止坍缩，并学习多样化离散技能抽象。实验展示该框架能有效组合技能完成复杂操作任务。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 现有方法用VQ-VAE学习技能抽象时面临码本坍缩和缺乏技能间因果建模的问题。
method: 设计旋转增强残差技能量化（RaRSQ），利用相对角度信息防止码本坍缩，并学习技能组合完成复杂行为。
result: 方法能学习多样化技能并成功组合执行复杂操作，优于现有技能抽象方法。
conclusion: STAR为机器人操作提出了稳定的技能抽象学习框架，显著提升了复杂任务的完成能力。
---

## Abstract
Transforming complex actions into discrete skill abstractions has demonstrated strong potential for robotic manipulation.Existing approaches mainly leverage latent variable models, e.g., VQ-VAE, to learn skill abstractions through learned vectors (codebooks), while they suffer from codebook collapse and modeling the causal relationship between learned skills. To address these limitations, we present **S**kill **T**raining with **A**ugmented **R**otation (**STAR**), a framework that advances both skill learning and composition to complete complex behaviors. Specifically, to prevent codebook collapse, we devise rotation-augmented residual skill quantization (RaRSQ).It encodes relative angles between encoder outputs into the gradient flow by rotation-based gradient mechanism. Points within the same skill code are forced to be either pushed apart or pulled closer together depending on gradient directions.Further, to capture the casual relationship between skills, we present causal skill transformer (CST) which explicitly models dependencies between skill representations through an autoregressive mechanism for coherent action generation.Extensive experiments demonstrate the superiority of STAR on both LIBERO benchmark and realworld tasks, with around 12% improvement over the baselines.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **研究背景**：在机器人操作中，将复杂动作转化为离散的技能抽象已被证明具有潜力。这类抽象通过将连续的动作数据压缩为离散编码，使机器人能像使用基本动作单元一样组合执行复杂任务。
- **现有方法局限**：目前主流方法主要基于潜变量模型（如 VQ-VAE），通过训练得到的向量码本实现技能抽象。但这些方法存在两个关键缺陷：
  - **码本坍缩**：学习过程中大部分码本向量未被充分利用，导致技能多样性丧失。
  - **技能因果关系缺失**：无法有效建模已学习技能之间的时序依赖和因果链，难以组合出连贯的复杂行为。
- **整体含义**：本文提出的 **STAR** 框架旨在同时解决码本坍缩和技能因果建模问题，从而稳定学习多样化的机器人技能抽象，并实现高效的行为组合。

### 2. 论文提出的方法论

STAR 框架包含两个核心技术组件：

- **旋转增强残差技能量化（RaRSQ）**：
  - **核心思想**：利用编码器输出之间的相对角度来构建梯度流，不同技能码内的点依据梯度方向被推远或拉近，从而在训练中动态维护码本的多样性。
  - **技术细节**：该方法对经典 VQ-VAE 中的向量量化模块进行改造，以旋转增强的方式将相对角度信息编码进入梯度计算。具体而言，对于编码器输出向量与码本向量的差异，引入基于角度的梯度调制机制，迫使向量在嵌入空间中保持合适距离，有效防止码本坍缩。
  - 公式描述（文字）：给定编码器输出 $z_e$ 和码本向量 $e_k$，传统 VQ 仅以最近邻方式选择码字并传递直通梯度；RaRSQ 则在此过程中注入相对角度 $\Delta\theta$ 的梯度项，使不同技能码对应的点群在更新时沿有利方向移动。

- **因果技能变换器（CST）**：
  - **核心思想**：显式建模技能表示之间的依赖关系。
  - **实现方式**：采用自回归机制（如因果注意力），在生成动作序列时，每个技能 token 仅能关注其之前的技能，从而构建时间上的因果关系。该设计让组合技能执行更连贯，符合机器人操作中动作顺序的逻辑约束。

- **整体流程**：编码器将观测和动作序列映射为连续嵌入，经 RaRSQ 量化为离散技能码，再由 CST 依据因果顺序解码生成最终动作序列或机器人轨迹。

### 3. 实验设计

- **数据集/场景**：
  - **LIBERO 基准**：一个用于机器人操作的多任务基准测试，包含丰富场景。
  - **真实世界任务**：在真实机器人上验证，具体任务细节未在摘要中展开。
- **对比方法**：与现有技能抽象方法进行对比（摘要未列出具体名称，但提及“优于基线方法约 12%”）。
- **评测指标**：方法论层面关注技能多样性与组合成功度；实际任务中应包含任务完成率等常见度量。

### 4. 资源与算力

- 论文摘要及可用元数据中 **未提及** GPU 型号、数量、训练时长等计算资源信息。若需详细算力说明，需查阅论文正文。

### 5. 实验数量与充分性

- 从摘要描述推断，实验至少包含：
  - LIBERO 基准上的多组对比实验；
  - 真实世界任务验证；
  - 约 12% 的提升来源于对比实验的平均统计；
  - 通常此类工作会包含消融实验（验证 RaRSQ 和 CST 各自贡献），但摘要未直接列出。
- **充分性分析**：用标准基准和真机结合的方式，实验设计较为全面。与基线的系统对比和大幅性能提升表明实验具有一定说服力，但摘要中未给出具体重复次数、统计检验等细节，公平性需查看完整论文确认。

### 6. 论文的主要结论与发现

- STAR 框架能有效解决码本坍缩问题，学习到多样化的离散技能抽象。
- 通过 CST 对技能间因果关系的建模，技能组合生成的动作更加连贯，复杂操作任务的成功率显著提高。
- 在 LIBERO 和真实世界任务中，STAR 比现有技能抽象方法均有约 12% 的性能提升，证明了其优势。

### 7. 优点

- **方法创新**：
  - RaRSQ 将旋转增强与向量量化巧妙结合，利用相对角度控制码本分布，为克服码本坍缩提供了新思路。
  - CST 将因果关系显式融入技能序列建模，使动作生成更符合任务逻辑。
- **实验全面**：覆盖模拟与真实环境，性能提升显著且一致。
- **可组合性**：学习到的技能抽象支持灵活组合，为复杂任务提供模块化解决方案。

### 8. 不足与局限

- **方法论细节缺失**：摘要未清晰解释旋转增强梯度机制的具体形式与理论保证。
- **真实世界任务描述不足**：未提供真实任务的复杂度、成功率具体数值，难以评估其实际部署效果。
- **实验对比范围**：摘要仅提及“现有技能抽象方法”，未列出具体基线（如 TAPOS、SPiRL 等），无法判断对比的充分性。
- **通用性边界**：在 LIBERO 和有限真实任务上有效，迁移到更复杂操作环境或非操作类技能时的适用性未知。
- **计算成本未说明**：缺少计算资源分析，难以评估方法在实际系统部署中的开销。

（完）
