---
title: "From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors"
title_zh: 从空间到行动：将视觉-语言-动作模型建立在空间基础先验上
authors: "Zhengshen Zhang, Hao Li, Yalun Dai, Zhengbang Zhu, Lei Zhou, Chenchen Liu, Dong Wang, Francis E. H. Tay, Sijin Chen, Ziwei Liu, Yuxiao Liu, Xinghang Li, Pan Zhou"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=fzmittHfq3"
tags: ["query:model"]
score: 9.0
evidence: 将空间基础模型的丰富3D空间令牌注入VLA动作头，增强空间基础
tldr: 针对VLA模型因基于2D编码器导致空间推理不足的问题，提出FALCON框架，将空间基础模型提取的丰富3D几何先验注入动作头，设计一种Embodied Spatial Model可选择融合深度、姿态或仅用RGB，在不重新训练VLM的情况下增强空间理解。实验表明该方法能显著提升VLA在3D环境中的泛化性和适应性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: VLA基于2D编码器，存在空间推理鸿沟，限制了在3D环境中的泛化能力。
method: 提出FALCON，将空间基础模型的3D令牌注入VLA动作头，Embodied Spatial Model可融合深度/姿态增强几何先验。
result: 通过强几何先验显著提升了VLA的泛化性，尤其在未见环境中的表现。
conclusion: 注入空间基础先验是弥补VLA空间推理缺口的有效途径，增强了具身模型的3D理解。
---

## Abstract
Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability. Recent 3D integration techniques for VLAs either require specialized sensors and transfer poorly across modalities, or inject weak cues that lack geometry and degrade vision-language alignment. In this work, we introduce **FALCON (From Spatial to Action)**, a novel paradigm that injects rich 3D spatial tokens into the action head. FALCON leverages spatial foundation models to deliver strong geometric priors from RGB alone, and includes an *Embodied Spatial Model* that can optionally fuse depth, or pose for higher fidelity when available, without retraining or architectural changes. To preserve language reasoning, spatial tokens are consumed by a *Spatial-Enhanced Action Head* rather than being concatenated into the vision-language backbone. These designs enable FALCON to address limitations in spatial representation, modality transferability, and alignment. In comprehensive evaluations across three simulation benchmarks and eleven real-world tasks, our proposed FALCON achieves state-of-the-art performance, consistently surpasses competitive baselines, and remains robust under clutter, spatial-prompt conditioning, and variations in object scale and height. Project page: https://falcon-vla.github.io/

---

## 论文详细总结（自动生成）

好的，请查收按要求生成的结构化中文论文总结。

### 1. 论文的核心问题与整体含义
本论文聚焦于**视觉-语言-动作（VLA）模型在三维真实世界中执行动作时存在的空间推理鸿沟**。目前主流的 VLA 模型虽然作用于三维环境，但其视觉骨干通常基于二维编码器，导致模型缺乏对三维空间结构和几何关系的深层理解。这一根本性不足限制了 VLA 模型在陌生场景下的泛化能力与环境适应性。

论文指出，已有的三维集成技术要么依赖专用传感器且跨模态迁移性差，要么仅注入微弱且缺乏几何信息的空间线索，这甚至会损害视觉-语言对齐。因此，本文的核心目标是**为 VLA 模型注入强健的三维空间基础先验，以弥合从二维感知到三维行动的鸿沟**，同时保持语言推理能力不受影响。

### 2. 方法论
论文提出了一个名为 **FALCON（From Spatial to Action）** 的新范式，其核心思想是**将空间基础模型提取的丰富三维几何先验注入到 VLA 的动作预测头中，而非其视觉-语言骨干网**。该方法的关键技术细节包括：

*   **空间令牌的来源：空间基础模型**  
    FALCON 利用预训练的空间基础模型，仅通过 RGB 图像即可提取出携带强几何信息的 3D 空间令牌，无需深度传感器。

*   **可选的具身空间模型**  
    设计了一个“具身空间模型”，该模型具备高度灵活性：在只有 RGB 输入时工作，当深度或姿态等传感器信息可用时，能够选择性地将这些模态融合进来，以进一步提升空间先验的保真度。此过程**无需重新训练视觉-语言模型或改变其网络架构**，实现了即插即用与跨模态的兼容性。

*   **空间增强的动作头**  
    为了保护语言推理链路的完整性，提取出的 3D 空间令牌并非与视觉-语言序列拼接后送入 Transformer 主干，而是专门由一个“空间增强动作头”进行消费。该动作头负责将空间几何信息与 VLM 输出的高层语义信息融合，最终生成更精准的动作指令。

### 3. 实验设计
论文进行了全面且跨领域的评估，具体设计如下：

*   **仿真基准**：在三类不同的仿真环境中进行了测试（摘要未列出具体数据集名称，但强调了“三个仿真基准”）。
*   **真实世界任务**：在十一个真实世界的机器人操作任务上进行了验证，以检验方法的实际部署能力。
*   **对比方法**：文中提及与具有竞争力的基线方法进行了对比，并一致性地取得了领先（state-of-the-art）的性能。
*   **鲁棒性测试**：评估了在杂乱环境、受空间提示词约束的条件、以及物体尺度和高度变化等复杂情况下的鲁棒性。

### 4. 资源与算力
**论文摘要及提供的元数据中，未明确说明所使用的 GPU 型号、数量以及具体的训练时长。** 要获得这些详细计算资源需求，需查阅论文原文或附录。

### 5. 实验数量与充分性
*   **实验规模**：从摘要来看，实验覆盖了**三个仿真基准**和**十一个真实世界任务**，总计至少十四组核心实验，此外还包含了不同条件下的鲁棒性测试。这一规模足以证明方法的有效性和跨场景的泛化能力。
*   **实验充分性与公平性**：由于缺少全文，无法精准确认是否包含详尽的消融研究（例如对各模块作用的独立分析）。但对比多个基线并达到最佳性能，体现了其客观对比。从元数据给出的“通过强几何先验显著提升了泛化性”等结论来看，实验设计应具备充分的说服力。需要指出，对实验公平性的绝对判断需以阅读完整论文中关于基线复现和超参设定的细节为基础。

### 6. 论文的主要结论与发现
*   FALCON 通过注入从空间基础模型导出的强几何先验，**有效弥补了 VLA 模型由于依赖 2D 编码器而导致的 3D 空间推理缺口**。
*   该方法在不重新训练视觉-语言骨干的前提下，极大增强了具身模型的 3D 空间理解能力，在多个仿真和真实环境中都取得了最先进的性能。
*   模型在未见环境中的**泛化能力和对各类干扰（杂波、物体尺度变化等）的鲁棒性均得到显著提升**。
*   将空间先验与动作头而非语言模块结合的策略，是保持视觉-语言对齐和语言推理能力的关键。

### 7. 优点
*   **架构非侵入性**：空间令牌仅作用于动作头，无需修改或微调原始 VLM，保护了预训练的对齐能力和语言推理能力，即插即用。
*   **模态灵活性与简洁性**：核心工作仅依赖 RGB 即可注入强 3D 先验，同时允许可选地融合深度或姿态信息以提升精度，不强制特殊传感器，跨平台迁移性好。
*   **性能提升显著**：在仿真和真实世界等多个基准上一致超越基线，并展现出优秀的鲁棒性。
*   **直击痛点**：明确并针对性地解决了当前 VLA 模型普遍存在的 2D 感知与 3D 行动之间的本源矛盾，思路清晰且有深度。

### 8. 不足与局限
*   **依赖空间基础模型**：方法的性能上限受限于所选用的空间基础模型的先验质量、泛化性和推理速度。如果基础模型在特定场景（如高度动态、透明物体）下失效，FALCON 的性能将受影响。
*   **实验细节未知**：由于目前仅基于摘要和元信息分析，无法评估其在仿真任务的具体难度、与最近 SOTA 方法的对比细节、以及是否在极度长序列、接触密集型任务上接受了考验。算力开销也未知。
*   **潜在的应用限制**：在极端资源受限的机器人平台（如微型无人机）上，额外运行空间基础模型可能会引入无法承受的延迟或计算功耗，实时性有待详查。
*   **评估偏差风险**：论文于 2026 年被 ICLR 接收，其真实世界任务可能局限于特定的实验室环境或物体套件，向完全开放、非结构化环境的泛化能力仍需进一步验证。

（完）
