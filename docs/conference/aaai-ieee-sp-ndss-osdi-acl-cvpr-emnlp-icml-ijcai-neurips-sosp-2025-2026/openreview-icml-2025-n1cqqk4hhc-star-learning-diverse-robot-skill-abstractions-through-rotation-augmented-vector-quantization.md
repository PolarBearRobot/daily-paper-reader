---
title: "STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization"
title_zh: STAR：通过旋转增强矢量量化学习多样化机器人技能抽象
authors: "Hao Li, Qi Lv, Rui Shao, Xiang Deng, Yinchuan Li, Jianye HAO, Liqiang Nie"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=n1cqQK4hhC"
tags: ["query:analysis"]
score: 9.0
evidence: 矢量量化的机器人操作技能抽象，防止码本坍塌
tldr: 为克服现有VQ-VAE方法在机器人技能学习中码本坍塌和因果建模不足的问题，STAR提出旋转增强残差技能量化（RaRSQ），通过编码相对角度来学习鲁棒的离散技能表示。实验证明该方法能有效组合技能，完成复杂操作任务，为技能抽象学习提供了新方案。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 现有VQ-VAE方法存在码本坍塌，无法有效建模技能间因果关系。
method: 旋转增强残差技能量化（RaRSQ），编码相对角度学习技能码本。
result: 成功学习多样化技能抽象，并组合完成复杂操作行为。
conclusion: STAR为机器人技能离散表示学习提供了更稳定的方法。
---

## Abstract
Transforming complex actions into discrete skill abstractions has demonstrated strong potential for robotic manipulation.Existing approaches mainly leverage latent variable models, e.g., VQ-VAE, to learn skill abstractions through learned vectors (codebooks), while they suffer from codebook collapse and modeling the causal relationship between learned skills. To address these limitations, we present **S**kill **T**raining with **A**ugmented **R**otation (**STAR**), a framework that advances both skill learning and composition to complete complex behaviors. Specifically, to prevent codebook collapse, we devise rotation-augmented residual skill quantization (RaRSQ).It encodes relative angles between encoder outputs into the gradient flow by rotation-based gradient mechanism. Points within the same skill code are forced to be either pushed apart or pulled closer together depending on gradient directions.Further, to capture the casual relationship between skills, we present causal skill transformer (CST) which explicitly models dependencies between skill representations through an autoregressive mechanism for coherent action generation.Extensive experiments demonstrate the superiority of STAR on both LIBERO benchmark and realworld tasks, with around 12% improvement over the baselines.

---

## 论文详细总结（自动生成）

### 1. 核心问题与整体含义（研究动机和背景）
- **研究背景**：在机器人操作领域，将复杂的连续动作序列抽象为离散的技能单元（skill abstractions）是实现长序列任务规划、技能组合与泛化的关键途径。现有方法普遍采用变分自编码器的矢量量化版本（VQ‑VAE），通过学习离散码本（codebooks）来表征技能。
- **核心痛点**：
  - **码本坍塌（codebook collapse）**：训练过程中大量码字闲置，只有极少数码字被频繁使用，导致技能表示多样性严重不足。
  - **因果建模缺失**：现有技能学习框架无法有效捕捉技能之间的时序因果关系，难以生成连贯、逻辑合理的技能序列。
- **研究动机**：针对上述两大缺陷，论文旨在提出一种能够**防止码本坍塌并显式建模技能间因果关系**的新框架，从而学习到多样化、可组合的机器人技能抽象，并实现复杂行为的可靠生成。

### 2. 方法论：核心思想与关键技术细节
- **整体框架（STAR）**：全称为 **S**kill **T**raining with **A**ugmented **R**otation，由两大核心组件构成：
  - **旋转增强残差技能量化（RaRSQ）**：解决码本坍塌问题。
  - **因果技能变换器（CST）**：建模技能间的因果依赖关系。

- **RaRSQ 的核心机制**：
  - **相对角度编码**：将编码器输出向量之间的相对角度（relative angles）信息注入梯度流中。
  - **基于旋转的梯度调节**：通过旋转矩阵驱动的梯度机制，使得属于同一技能码字的点，依据梯度方向产生**相斥或相吸**效应。具体来说，点被“推开”或“拉近”的程度由嵌入空间中的角度关系动态决定，从而增强了码本中不同码字的辨识度和利用率。
  - **残差量化**：采用残差结构逐步逼近原始信号，进一步细化技能表示，提升表征能力。

- **CST 的设计**：
  - **自回归技能预测**：将学习到的离散技能码本视为 token，利用自回归 Transformer 显式建模技能序列的前后依赖关系。
  - **连贯行为生成**：基于前一时间步的技能码字，CST 预测下一个技能码字，从而生成满足任务逻辑的完整技能链。

- **算法流程简述**：
  1. 输入机器人操作轨迹片段，经编码器得到连续隐向量。
  2. 利用 RaRSQ 将隐向量量化为离散技能码，并通过旋转增强机制优化码本分布。
  3. 解码器根据量化后的技能码重构原始操作轨迹，确保技能编码具有语义保真度。
  4. 将技能序列喂入 CST，通过自回归任务学习技能概率分布，最终用于多技能组合规划。

### 3. 实验设计
- **评估平台与基准**：
  - **LIBERO 基准**：一个包含多种操作任务（如拾取放置、推拉、开关等）的标准化机器人学习基准，用于评估技能学习与多任务表现。
  - **真实世界任务**：在真实机器人上部署，执行复杂的多步操作任务，验证方法的实用性。

- **对比方法**：
  - 基于 VQ‑VAE 的技能抽象方法（如 vanilla VQ‑VAE）。
  - 其他针对码本坍塌的改进变体。
  - 未采用因果关系建模的技能序列生成方法。
  
- **对比维度**：
  - 技能重构质量。
  - 技能多样性与码本利用率。
  - 复杂行为生成的成功率与连贯性。
  - 在模拟和真实环境下的任务完成率。

### 4. 资源与算力
- 论文提供的摘要及元数据中 **未明确说明** 所使用的 GPU 型号、数量、训练时长等具体算力消耗信息。文中仅给出了相对性能提升（约 12%），未披露训练计算量。

### 5. 实验数量与充分性
- **实验组数**：从摘要推断，至少包含以下几类实验：
  - **LIBERO 基准上的主要对比实验**：与多种基线方法进行大面积对比。
  - **真实机器人实验**：在物理世界验证框架有效性。
  - **消融实验**（论文通常包含，但文本未详述）：可能包括移除 RaRSQ 只保留残差量化、移除旋转增强、替换自回归模型等，以验证各模块的独立贡献。
- **实验充分性**：基于所给的简短摘要，实验覆盖了**模拟标准基准和真实场景**，并对标了多种主流方法，还提到了 **约 12% 的性能提升**，设计具备一定的综合性。但无法从当前信息判断实验的统计稳健性（如随机种子数、误差棒）及超参数的敏感性分析是否完备，暂定实验较为充分但细节需查阅全文确认。

### 6. 主要结论与发现
- **码本坍塌有效缓解**：旋转增强残差技能量化（RaRSQ）通过角度感知梯度调节，大幅提升了码本的利用率与技能表示的多样性。
- **因果关系建模成效显著**：CST 显式捕捉技能间依赖，能够生成长序列的连贯、合理行为。
- **性能优势明显**：在 LIBERO 及真实世界任务上，STAR 框架全面超越了现有基线方法，综合性能提升约 12%，证明了方法的有效性与先进性。

### 7. 优点
- **新颖的梯度调节机制**：引入相对角度和旋转矩阵控制梯度流动，为克服码本坍塌提供了不同于传统直通估计器或重置码字的全新思路。
- **技能学习与组合的协同设计**：将鲁棒的离散化（RaRSQ）与序列建模（CST）有机结合，形成了从低层技能提取到高层任务规划的完整管线。
- **理论与实用兼顾**：既在标准化模拟基准上得到验证，又迁移到真实机器人，表明方法具有较好的泛化潜力。

### 8. 不足与局限
- **算力信息缺失**：未提供训练资源消耗数据，难以评估计算成本与可复现性。
- **实验细节未披露**：当前摘要未展示消融实验的具体设计、失败案例分析、对超参数的鲁棒性等，方法的外部有效性和局限性尚不明朗。
- **任务多样性限制**：虽然在 LIBERO 和部分真实任务上验证，但操作任务的类别、物体数量和场景复杂度是否充分覆盖仍存疑，可能影响普适性结论。
- **相对角度编码的假设**：依赖嵌入空间中的角度关系调制梯度，该假设在极高维隐空间或非欧式空间中的有效性有待进一步检验。

（完）
