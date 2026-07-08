---
title: "Vidar: Embodied Video Diffusion Model for Generalist Manipulation"
title_zh: Vidar：用于通用操作策略的具身视频扩散模型
authors: "Yao Feng, Hengkai Tan, Xinyi Mao, Chendong Xiang, Guodong Liu, Shuhe Huang, Hang Su, Jun Zhu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=CFuNu8dK4s"
tags: ["query:model"]
score: 9.0
evidence: 利用互联网规模预训练和多机器人数据，通过具身视频扩散模型实现通用操作
tldr: 针对通用操作策略难以跨本体泛化的问题，提出Vidar，将互联网规模预训练的视频扩散模型作为通用先验，利用75万条多本体真实机器人轨迹进行具身预训练，并设计统一观测空间，结合掩码逆动力学模型适配，实现对新本体的高效泛化。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有操作策略需大量同质演示，且端到端管线难以应对背景和视角变化。
method: Vidar以视频扩散模型为先验，联合掩码逆动力学模型适配，并在统一观测空间下进行多本体预训练。
result: 实验证明Vidar在新机器人和新任务上表现出色的泛化能力。
conclusion: Vidar展示了利用大规模视频生成模型与多源机器人数据构建通用操作策略的潜力。
---

## Abstract
Scaling general-purpose manipulation to new robot embodiments remains challenging: each platform typically needs large, homogeneous demonstrations, and end-to-end pixel-to-action pipelines may degenerate under background and viewpoint shifts. Based on previous advances in video-based robot control, we present Vidar, consisting of an embodied video diffusion model as the generalizable prior and a masked inverse dynamics model (MIDM) as the adapter. We leverage a video diffusion model pre-trained at Internet scale, and further continuously pre-train it for the embodied domain using 750K multi-view trajectories collected from three real-world robot platforms. For this embodied pre-training, we introduce a unified observation space that jointly encodes robot, camera, task, and scene contexts. The MIDM module learns action-relevant pixel masks without dense labels, grounding the prior into the target embodiment’s action space while suppressing distractors. With only ∼20 minutes of human demonstrations on an unseen robot (∼1% of typical data), Vidar outperforms state-of-the-art baselines and generalizes to unseen tasks, backgrounds, and camera layouts. Our results suggest a scalable recipe for “one prior, many embodiments”: strong, inexpensive video priors together with minimal on-robot alignment.

---

## 论文详细总结（自动生成）

# Vidar：用于通用操作策略的具身视频扩散模型 论文总结

## 1. 核心问题与整体含义（研究动机与背景）
- **核心问题**：将通用操作策略扩展到新的机器人本体（embodiment）上仍面临重大挑战。传统方法通常需要为每个机器人平台收集大规模、同质化的演示数据，且端到端的像素到动作管线容易因背景和视角变化而性能退化。
- **整体含义**：该论文旨在利用互联网规模预训练的视频扩散模型所蕴含的丰富视觉先验，结合少量多源真实机器人数据，构建一个能够高效适应新本体、新任务和新环境的通用操作策略。

## 2. 方法论
- **核心思想**：以视频扩散模型作为可泛化的通用先验，再通过一个轻量级的适配模块将其落地到特定机器人的动作空间上。
- **关键技术细节**：
  - **具身视频扩散模型**：使用已在互联网规模数据上预训练的视频扩散模型，并进一步在多机器人轨迹数据上进行连续预训练，使其适应具身场景。
  - **掩码逆动力学模型（MIDM）**：作为适配器，通过无密集标注的方式学习与动作相关的像素掩码，从而将通用先验锚定到目标本体的动作空间，并抑制背景等干扰因素。
  - **统一观测空间**：为了多本体预训练，设计了能够联合编码机器人本体、相机、任务和场景上下文的统一表示，使得模型能处理来自不同平台的异构数据（共75万条多视角真实机器人轨迹）。
- **算法流程**：视频扩散模型依据历史观测生成未来视频预测；MIDM则从这些预测中提取与动作相关的区域，进而映射为具体机器人的控制指令。适配到新机器人仅需约20分钟的人类演示（约占典型数据的1%）。

## 3. 实验设计
- **数据集与场景**：
  - 具身预训练使用了从3个真实机器人平台收集的75万条多视角轨迹。
  - 对新机器人适配时，仅需~20分钟的人类演示数据。
  - 评估场景涉及未见过的新任务、新背景和新相机布局。
- **基准对比**：论文表示（根据元数据），Vidar 在泛化到新机器人和新任务方面，优于现有最先进的基线方法（具体基线名称未在元数据中列出，但可推测包括端到端像素到动作策略等方法）。

## 4. 资源与算力
- 元数据及提供的片段中**未明确提及**具体的算力配置（如GPU型号、数量、训练时长等）。考虑到涉及互联网规模视频扩散模型的预训练和75万条多机器人轨迹的连续预训练，可以推测算力需求较大，但缺乏具体数字。

## 5. 实验数量与充分性
- **实验维度**：从元数据描述推测，实验覆盖了多本体预训练、新机器人泛化、新任务泛化、背景/视角变化鲁棒性等。
- **消融实验**：未明确说明，但一般此类工作会包含对MIDM模块、预训练数据规模、适配数据量等的消融分析。
- **充分性与公平性**：由于是会议拒稿论文（ICLR-2026-Rejected-Public），评审分数为9.0，但最终被拒，可能表明实验部分在某些方面被认为不够全面（如对比基线的全面性、真实世界实验规模等），或存在其他不足。仅凭元数据无法判断实验是否完全客观公平。

## 6. 主要结论与发现
- Vidar 成功展示了将大规模视频生成模型与多源机器人数据结合，以构建通用操作策略的潜力。
- 通过“一个先验，多个本体”的范式，仅需在新机器人上采集极少量演示（约20分钟），即可实现优异的泛化能力，超越现有前沿基线。
- 该方法表明：强大的、可廉价获取的视频先验，辅以极小的在机器人上的对齐成本，是一条可扩展的技术路线。

## 7. 优点（亮点）
- **利用互联网先验**：巧妙将大规模预训练视频生成模型的知识迁移至机器人操作任务，大幅降低对新机器人数据的依赖。
- **高效适配**：仅需极少目标机器人数据（约1%典型数据量）即可完成部署，显著提升了扩展性。
- **统一观测空间设计**：允许混合不同机器人平台的数据进行预训练，增强了泛化基础。
- **掩码逆动力学模型**：无监督地关注动作相关的视觉区域，提供了一种可解释且高效的适配机制。

## 8. 不足与局限
- **实验细节未知**：由于缺乏全文，具体实验设置、对比基线、消融实验的深度与广度均无法评估。
- **真实环境限制**：论文被ICLR-2026拒稿（尽管获得9分），暗示可能存在方法或实验上的局限，例如可能仅在某些受控设置下验证，或对新本体的泛化尚未达到真正的“零样本”水平。
- **应用风险**：依赖大规模预训练视频模型可能存在数据偏差问题；视频预测模型的计算开销在资源受限的实际部署中可能是瓶颈。
- **元数据信息有限**：无法判断其在安全性、实时性等机器人关键指标上的表现。

（完）
