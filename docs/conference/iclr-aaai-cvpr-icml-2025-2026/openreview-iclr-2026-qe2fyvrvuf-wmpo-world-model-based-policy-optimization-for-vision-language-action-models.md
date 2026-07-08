---
title: "WMPO: World Model-based Policy Optimization for Vision-Language-Action Models"
title_zh: "WMPO: 基于世界模型的视觉-语言-动作模型策略优化"
authors: "Fangqi Zhu, YAN Zhengyang, Zicong Hong, Quanxin Shou, Xiao Ma, Song Guo"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=qE2FyvRvuF"
tags: ["query:model"]
score: 9.0
evidence: 基于世界模型的策略优化用于VLA模型，实现无需真实机器人交互的强化学习
tldr: VLA模型依赖专家演示，无法从失败中学习与自我纠正；强化学习虽能自我改进，但真实机器人采样成本高。WMPO提出基于世界模型的策略优化框架，利用与VLA特征对齐的像素级世界模型在想象中进行在线策略强化学习，无需真实环境交互。实验表明，该方法使VLA策略更具鲁棒性，能通过想象数据自我改进，显著提升了操作成功率。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: VLA模型受限于演示学习，缺乏从失败中自愈的能力。
method: 构建与VLA特征对齐的像素世界模型，在想象轨迹上执行在线RL。
result: WMPO使VLA策略通过想象实现自我纠正，鲁棒性大幅提升。
conclusion: WMPO桥接了VLA模型与强化学习，为通用机器人操作提供了更鲁棒的学习范式。
---

## Abstract
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. 
Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots.
We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment.
In contrast to widely used latent world models, 
WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images.
Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods.
Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

---

## 论文详细总结（自动生成）

# WMPO: 基于世界模型的视觉-语言-动作模型策略优化 论文总结

## 1. 论文的核心问题与整体含义
- **研究背景**：视觉-语言-动作（VLA）模型在通用机器人操作中展现强大潜力，但其性能高度依赖专家演示数据，难以从自身错误中学习并实现自我纠正。
- **核心问题**：强化学习具备自我改进能力，但直接在真实机器人上交互采样成本极高、样本效率低，导致RL难以规模化应用。
- **整体含义**：提出一种无需真实环境交互的在线策略强化学习框架，利用像素级世界模型在“想象”中优化VLA策略，从而桥接演示学习与自我改进之间的鸿沟。

## 2. 论文提出的方法论
- **核心思想**：构建一个与VLA预训练视觉特征对齐的像素级世界模型，用该世界模型生成高保真想象轨迹，并在其上执行在线策略梯度优化（尤其是GRPO），使VLA策略能够脱离真实机器人实现鲁棒自纠。
- **关键技术细节**：
  - **像素级世界模型**：区别于广泛使用的隐空间世界模型，WMPO直接预测像素，更利于将想象轨迹与利用网络规模图像预训练的VLA特征对齐，保证视觉-语言-动作模态的一致性。
  - **在线策略强化学习（On-policy RL）**：采用GRPO（Group Relative Policy Optimization）等在线策略算法，从世界模型生成的想象轨迹中采样学习，相比离线RL方法具有更优的性能上限。
  - **无需真实交互**：整个策略改进过程完全在世界模型的想象空间内进行，避免真实机器人采样，大幅降低样本复杂度。
- **算法流程**（文字描述）：
  1. 基于VLA模型的视觉编码器，训练像素级世界模型，使其能够接收动作指令并预测下一帧RGB图像。
  2. 由当前VLA策略在世界模型中采样生成想象轨迹。
  3. 在想象数据上应用在线策略GRPO进行策略更新。
  4. 更新后的策略可重新生成想象轨迹，形成自我改进循环。

## 3. 实验设计
- **数据集/场景**：论文在仿真环境与真实机器人设定下均进行了验证（具体数据集名称在摘要中未列出，元数据提及“通用机器人操作”）。
- **Benchmark与对比方法**：
  - 与广泛使用的离线RL方法对比。
  - 可能对比传统隐空间世界模型、纯演示学习等（具体方法名称未提供）。
- **评估目标**：操作成功率、样本效率、自我纠正行为涌现、鲁棒泛化与持续学习能力。

## 4. 资源与算力
- 所提供的摘要与元数据中**未明确提及**所使用的GPU型号、数量、训练时长等算力细节。文中仅强调通过想象世界模型避免了真实机器人采样，从而“大幅提升样本效率”，但未量化物理计算开销。

## 5. 实验数量与充分性
- 摘要称进行了“extensive experiments”（大量实验），涵盖仿真与真实机器人场景，但未给出具体实验组数、消融研究项目。
- 根据元数据中的result字段（“使VLA策略通过想象实现自我纠正，鲁棒性大幅提升”）及tldr信息，可推断实验验证了方法核心贡献：样本效率提升、性能增强、自我纠正行为涌现、泛化与终身学习。这些多角度的验证表明实验设计**相对充分**，但具体对比数量和消融充分性因信息不足无法精确评估。
- 公平性：作为ICLR 2026录用论文（score 9.0），其对比基准与方法选择应具有同行评审保障的客观性和公平性。

## 6. 论文的主要结论与发现
- WMPO成功使VLA策略**在不接触真实环境的情况下实现自我纠正**，显著提升操作成功率。
- 方法在样本效率、整体性能、泛化能力和持续学习能力上都展现优势。
- 想象世界中的在线策略优化为通用机器人操作提供了一条更为鲁棒、安全且可规模化的学习路径。

## 7. 优点
- **无需真实交互**：从根本上解决了真实机器人RL的样本复杂度和安全问题，极大降低实验成本。
- **像素级对齐**：世界模型直接预测像素，与VLA的预训练视觉特征天然对齐，保真度高，便于利用大规模预训练知识。
- **在线策略RL优势**：采用GRPO等在线算法取代常用的离线方法，获得更强的性能提升。
- **涌现行为**：能够催生自我纠正等高级智能行为，验证了方法的内在有效性。
- **支持终身学习**：框架具备持续进化的潜力。

## 8. 不足与局限
- **算力细节缺失**：摘要未披露训练世界模型和在线RL所需的实际GPU算力与时间，无法评估计算开销与实用性边界。
- **实验量化信息有限**：仅凭摘要无法知晓具体实验规模、对比方法的公平性细节，以及在不同难度任务上的表现差异。
- **世界模型泛化风险**：像素级世界模型虽高保真，但其预测误差可能累积，在长序列想象中潜在导致策略优化偏差，文中未提及误差控制机制。
- **真实环境迁移**：虽然展示真实机器人实验，但想象到现实的迁移效果（sim-to-real gap的具体处理）在摘要中未被充分讨论。

（完）
