---
title: Embodied Navigation Foundation Model
title_zh: 具身导航基础模型
authors: "Jiazhao Zhang, Anqi Li, Yunpeng Qi, Minghan Li, Jiahang Liu, Shaoan Wang, Haoran Liu, Gengze Zhou, Yuze Wu, Xingxing LI, Yuxin Fan, Wenjun Li, Zhibo Chen, Fei Gao, Qi Wu, Zhizheng Zhang, He Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=kkBOIsrCXh"
tags: ["query:model"]
score: 9.0
evidence: 跨本体、跨任务的导航基础模型，训练自八百万样本
tldr: 现有导航模型大多局限于特定任务和本体。NavFoM提出跨本体、跨任务的导航基础模型，在涵盖四足、无人机、轮式等多种机器人的八百万样本上训练。实验表明，该模型在视觉语言导航、目标搜索等多项任务上展现了强泛化能力，为搭建通用移动机器人基础模型提供了可行路径。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有导航模型普遍受限于特定任务设定和本体架构。
method: 提出跨本体、跨任务基础模型架构，在大规模异构样本上统一训练。
result: 在多种导航任务上展示出强泛化能力，超越领域专用模型。
conclusion: 大规模基础模型是实现通用移动机器人智能的有效途径。
---

## Abstract
Navigation is a fundamental capability in embodied AI, representing the intelligence required to perceive and interact within physical environments. To achieve such intelligence, recent advanced works leverage Vision-Language Models (VLMs), which demonstrate strong generalizability and possess a well-suited formulation for navigation. However, these approaches remain largely confined to narrow task settings and embodiment-specific architectures. In this work, we introduce a cross-embodiment and cross-task Navigation Foundation Model (NavFoM), trained on eight million navigation samples that encompass quadrupeds, drones, wheeled robots, and vehicles, and spanning diverse tasks such as vision-and-language navigation, object searching, target tracking, and autonomous driving. NavFoM employs a unified architecture that processes multimodal navigation inputs from varying camera configurations and navigation horizons. To accommodate diverse camera setups and temporal horizons, NavFoM incorporates identifier tokens that embed camera view information of embodiments and the temporal context of tasks.  Furthermore, to meet the demands of real-world deployment, NavFoM controls all observation tokens using a dynamically adjusted sampling strategy under a limited token length budget. Extensive evaluations on seven public benchmarks demonstrate that our model achieves state-of-the-art or highly competitive performance across different navigation tasks and embodiments without requiring task-specific fine-tuning. Additional real-world experiments further confirm the strong generalizability and practical applicability of our approach.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- 具身导航是具身智能的基本能力，需要感知物理环境并与之交互。
- 现有先进方法利用视觉-语言模型（VLM）来提升导航的泛化性，但其构造大多仍被限制在狭窄的任务设定和特定本体的架构中。
- 核心问题：**如何构建一个跨越不同机器人形态（四足、无人机、轮式等）和多样化导航任务（视觉语言导航、目标搜索、目标跟踪、自动驾驶等）的统一导航基础模型**。
- 整体含义：通过在海量、异构的导航数据上训练一个通用模型，实现跨本体、跨任务的强泛化能力，为通用移动机器人智能提供可行路径。

### 2. 论文提出的方法论：核心思想、关键技术细节、算法或流程
- **核心思想**：提出导航基础模型 NavFoM（Navigation Foundation Model），使用**统一架构**处理来自不同相机配置和导航时间跨度的多模态导航输入。
- **统一架构设计**：
  - 模型能接纳多种模态输入，例如视觉、语言指令等。
  - 为处理不同本体上的多样化相机视角和任务所需的时序范围，引入**标识符令牌（identifier tokens）**，嵌入各本体的相机视角信息以及任务的时间上下文。
- **动态调整采样策略**：
  - 为满足真实世界部署需求，在有限的令牌长度预算（token length budget）下，对所有观测令牌进行动态调整的采样控制，确保高效推理。
- 训练数据：使用了包含**四足机器人、无人机、轮式机器人、车辆**等多种本体的**八百万导航样本**，覆盖视觉语言导航、目标搜索、目标跟踪、自动驾驶等多种任务。

### 3. 实验设计：数据集/场景、benchmark、对比方法
- **评估基准**：在**七个公开基准**上进行测试，涵盖不同导航任务和本体设定。
- **任务类型**：包括视觉语言导航（VLN）、目标搜索、目标跟踪、自动驾驶等。
- **对比方法**：与各领域当前最先进的专用模型进行对比，未列出具体名称但强调无需任务特定微调即取得最优或极具竞争力的性能。
- **现实世界实验**：除基准测试外，还进行了额外的真实环境实验，以验证模型的强泛化性和实际适用性。

### 4. 资源与算力
- 文中未提供明确的算力细节（如 GPU 型号、数量、训练时长等）。提到训练数据规模为“八百万导航样本”，但未披露训练该模型所需的计算资源。

### 5. 实验数量与充分性
- **实验规模**：评估覆盖了七个公开基准，并补充了真实世界实验，总体实验组数较多。
- **实验充分性**：
  - 多任务、多本体的综合评估显示了模型在多种场景下的效能。
  - 论文宣称无需任务特定的微调，因此零样本或统一模型直接评测的方式强化了结论的客观性和公平性。
- **消融实验**：摘要未明确提及消融实验，但提及“dynamic adjusted sampling strategy under a limited token length budget”表明可能对令牌预算或采样策略进行过分析；具体情况需查看全文。

### 6. 论文的主要结论与发现
- NavFoM 在跨任务、跨本体的导航任务上取得了最先进或高度竞争力的性能，且不需要进行任何任务特定的微调。
- 大规模基础模型是实现通用移动机器人智能的一条有效途径。
- 模型具备良好的泛化能力，能够从仿真基准迁移到真实世界部署。

### 7. 优点：方法或实验设计上的亮点
- **跨本体泛化**：首次在如此多样化的机器人形态（腿足、飞行、轮式、车辆）上实现统一的导航模型。
- **跨任务统一**：覆盖了从目标搜索、语言导航到自动驾驶等多种任务，避免了为每个任务设计专门模型的复杂性。
- **即插即用的泛化性**：在七个基准上未进行微调即获得强竞争力，展示出强大的零样本迁移能力。
- **工程实用性**：引入动态令牌采样以适应有限计算预算，考虑了真实部署的资源限制。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等
- 论文摘要未明确提及模型的具体网络结构细节和正则化方式，方法论的高层描述可能掩盖了实现上的复杂性。
- 未提供算力开销信息，无法判断其训练成本是否在可承受范围内。
- 虽然宣称跨任务、跨本体，但未见其在某些极端或未见过环境中的测试，偏差风险未知。
- 实验全部在七个特定公开基准上进行，可能存在基准过拟合的风险，尤其是当这些基准被广泛使用时。
- 真实世界实验的规模和多样性未说明，推广到任意非结构化环境的能力仍有待验证。

（完）
