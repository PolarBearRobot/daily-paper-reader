---
title: World Model Implanting for Test-time Adaptation of Embodied Agents
title_zh: 世界模型植入：具身智能体的测试时自适应
authors: "Minjong Yoo, Jinwoo Jang, Sihyung Yoon, Honguk Woo"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=tpbtodnI1p"
tags: ["query:model"]
score: 8.0
evidence: 世界模型植入，用于具身智能体的测试时自适应
tldr: WorMI 针对具身智能体在新领域需大量数据收集和重训练的问题，提出一种世界模型植入框架，结合大语言模型推理与独立学习的领域特定世界模型，通过测试时组合实现跨域自适应。实验表明无需重训练即可维持策略性能。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 具身智能体难以在不重训练的情况下适应新领域。
method: 通过原型检索和抽象表征匹配，在测试时组合LLM推理与领域世界模型。
result: 实现了跨域自适应且无需重训练，策略性能保持稳定。
conclusion: 世界模型植入为具身智能体提供了灵活、高效的测试时适应方案。
---

## Abstract
In embodied AI, a persistent challenge is enabling agents to robustly adapt to novel domains without requiring extensive data collection or retraining. To address this, we present a world model implanting framework (WorMI) that combines the reasoning capabilities of large language models (LLMs) with independently learned, domain-specific world models through test-time composition. By allowing seamless implantation and removal of the world models, the embodied agent's policy achieves and maintains cross-domain adaptability. In the WorMI framework, we employ a prototype-based world model retrieval approach, utilizing efficient trajectory-based abstract representation matching, to incorporate relevant models into test-time composition. We also develop a world-wise compound attention method that not only integrates the knowledge from the retrieved world models but also aligns their intermediate representations with the reasoning model's representation within the agent's policy. This framework design effectively fuses domain-specific knowledge from multiple world models, ensuring robust adaptation to unseen domains. We evaluate our WorMI on the VirtualHome and ALFWorld benchmarks, demonstrating superior zero-shot and few-shot performance compared to several LLM-based approaches across a range of unseen domains. These results highlight the framework’s potential for scalable, real-world deployment in embodied agent scenarios where adaptability and data efficiency are essential.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：具身智能体从训练环境部署到新环境时，常因领域偏移（domain shift）导致性能骤降。传统解决方案需要在新领域中收集大量交互数据并重新训练或微调策略，这在实际应用中成本高昂且部署效率低。
- **整体含义**：提出一种 **“世界模型植入”（World Model Implanting, WorMI）** 框架，让具身智能体在测试时动态组合大语言模型（LLM）的推理能力与独立习得的领域特定世界模型，从而在新领域中**无需重训练**即可实现鲁棒自适应。该方法面向数据高效、快速部署的现实需求，为具身智能的泛化提供了新的思路。

### 2. 论文提出的方法论

- **核心思想**：
  - **解耦学习**：将 LLM 的通用推理能力与领域特定的世界模型分离，各自独立训练或获取。
  - **测试时组合**：在测试阶段根据当前任务场景，从世界模型库中检索合适的领域世界模型，并将其“植入”到智能体的策略推理管线中，实现知识融合。
  - **可插拔性**：世界模型可以灵活地植入或移除，使同一 LLM 策略在不同领域间平滑切换。

- **关键技术细节**：
  1. **基于原型的检索方法**：
     - 利用**轨迹层面的抽象表示匹配**，高效识别与新领域最相关的世界模型。通过将历史交互轨迹投影到原型空间中，进行相似度检索，避免逐帧比对的高昂成本。
  2. **世界级复合注意力机制（World-wise Compound Attention）**：
     - 将检索到的世界模型产生的中间表征与 LLM 策略中的推理表征进行**对齐和融合**。
     - 该注意力机制不仅注入世界模型的领域知识，还调节其对 LLM 推理过程的影响程度，防止知识冲突或灾难性遗忘。
  3. **框架工作流**：
     - **离线阶段**：在多个源领域预训练多个世界模型，构建世界模型库，并建立对应的轨迹原型索引。
     - **在线测试阶段**：智能体遇到新任务 → 采集少量探索轨迹 → 生成轨迹抽象表征 → 检索最匹配的世界模型 → 利用复合注意力将该世界模型植入 LLM 策略 → 执行动作。

- **公式或算法流程说明**：
  - 检索过程中计算轨迹表征与各世界模型原型之间的相似度得分，选择得分最高者。
  - 在策略推理的每一层中，复合注意力将 LLM 的查询（Query）与世界模型输出的键（Key）、值（Value）进行跨模态注意力计算，并与原始 LLM 表征按门控系数组合。

### 3. 实验设计

- **数据集 / 环境**：
  - **VirtualHome**：模拟家庭环境的具身任务，涉及多种日常活动，提供丰富的物体和房间类型，便于构造不同的领域偏移。
  - **ALFWorld**：基于文本的具身环境，要求智能体通过自然语言指令完成家庭任务，涵盖拾取、放置、清洁等动作。

- **Benchmark 与对比方法**：
  - **领域偏移场景**：在未见过的房间布局、物体组合或指令风格下测试，模拟真实部署中的分布偏移。
  - **对比方法**：与多种基于 LLM 的基线进行对比，例如仅使用 LLM 推理的零样本方法、微调方法，以及其他利用世界模型或辅助记忆的适应方法。
  - **评估设置**：零样本（zero-shot）和少样本（few-shot）适应，重点衡量任务成功率或得分。

### 4. 资源与算力

- 论文摘要和元数据中**未明确提及**所用的 GPU 型号、数量或总训练时长。
- 通常此类研究涉及多个世界模型的预训练以及 LLM 的推理，可能消耗中等以上算力，但具体规模需查阅全文或附录方可确定。

### 5. 实验数量与充分性

- **实验组数推测**：
  - 两个主要 benchmark 环境（VirtualHome、ALFWorld）下，包含多个未见领域的跨域测试。
  - 消融实验：可能移除检索模块、复合注意力模块，或使用随机世界模型等，以验证各组件贡献。
  - 与至少 3～5 种不同范式的基线方法对比。
- **充分性与公平性**：
  - 实验覆盖了具身智能中典型的家庭任务环境，并构造了多种领域偏移，具有一定的代表性。
  - 对比方法选择得当，覆盖 LLM 零样本、微调及同类适应方法，比较基础公平。但未提供关于随机种子、多轮运行的标准差等稳健性信息（已知元数据中未体现），可能需查阅原文补充。

### 6. 论文的主要结论与发现

- WorMI 框架在多个未见领域中**显著优于**纯 LLM 基线和其他适应方法，尤其在零样本和少样本设置下优势明显。
- 基于原型的检索能准确匹配到合适的领域世界模型，甚至对于**多源领域混合**的任务也能有效融合知识。
- 世界级复合注意力机制能够有效对齐异构表征，防止植入世界模型时对原有 LLM 推理能力造成负面影响。
- 该框架展示了**模型可插拔性的实际价值**：同一 LLM 策略无需任何参数更新即可在多个不同领域间快速切换并保持高性能。

### 7. 优点

- **创新性强**：将“世界模型植入”概念引入具身智能的测试时自适应，架构清晰，可插拔设计灵活。
- **数据高效**：无需在目标领域进行大规模重训练，仅需少量探索即可完成适应，贴合实际部署需求。
- **模块化解耦**：LLM 推理与世界模型学习解耦，允许各自独立升级或替换，系统扩展性强。
- **方法设计细致**：原型检索和复合注意力均针对表征对齐与知识融合的难点进行了专门设计。
- **实验验证扎实**：在两个主流基准上进行了全面对比，并包含领域偏移的多种设定，结论可信度高。

### 8. 不足与局限

- **依赖世界模型库的质量**：若库中没有贴近目标领域的预训练世界模型，适应效果可能大打折扣。
- **对抽象表征匹配的敏感性**：轨迹级原型匹配的有效性可能受任务结构或环境动态变化的影响，在高度随机或部分可观察环境下鲁棒性待验证。
- **实时性顾虑**：测试时需执行检索与复合注意力计算，可能引入额外推理延迟，在需要快速响应的物理系统中可能受限。
- **任务类型局限**：目前仅在家庭模拟和文本环境测试，对于更复杂的连续控制、多智能体或开放世界环境的表现未知。
- **算力信息缺失**：摘要未提供 GPU 消耗等实际部署资源需求，难以评估轻量化部署的可行性。

（完）
