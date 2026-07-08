---
title: "Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes"
title_zh: 跨视角观察：基准测试机器人场景中视觉-语言模型的空间推理能力
authors: "ZhiYuan Feng, Zhaolu Kang, Qijie Wang, Zhiying Du, Jiongrui Yan, Shi Shubin, Chengbo Yuan, Huizhi Liang, Yu Deng, Qixiu Li, Rushuai Yang, Ruichuan An, Leqi Zheng, Weijie Wang, Shawn Chen, Sicheng Xu, Yaobo Liang, Jiaolong Yang, Baining Guo"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=jXDZJAfRZB"
tags: ["query:model"]
score: 7.0
evidence: 评估多视图空间推理的基准，针对机器人场景中的VLM，对VLA模型至关重要
tldr: 当前VLM评估多限于单视角，而机器人平台普遍采用多摄像头，VLA模型需要多视图空间推理能力。为此，引入MV-RoboBench基准，专门评估VLM在机器人场景中整合多视图信息进行空间推理的能力。该基准填补了VLA模型评估中的关键空白，为提升具身AI的空间理解提供了标准化测试平台。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 多摄像头机器人设置日益普遍，但VLM的多视图空间推理能力尚未得到系统评估。
method: 构建MV-RoboBench基准，设计多视图空间推理任务，评测VLM在机器人场景中的表现。
result: 揭示了现有VLM在多视图整合中的局限性，为未来VLA模型提供改进方向。
conclusion: MV-RoboBench推动了机器人空间推理评估，凸显了多视图能力对VLA模型的重要性。
---

## Abstract
Vision-language models (VLMs) are essential to Embodied AI, enabling robots to perceive, reason, and act in complex environments. They also serve as the foundation for the recent Vision-Language-Action (VLA) models. Yet most evaluations of VLMs focus on single-view settings, leaving their ability to integrate multi-view information underexplored. At the same time, multi-camera setups are increasingly standard in robotic platforms, as they provide complementary perspectives to mitigate occlusion and depth ambiguity. Whether VLMs can effectively leverage such multi-view inputs for robotic reasoning therefore remains an open question. To bridge this gap, we introduce \textbf{MV-RoboBench}, a benchmark specifically designed to evaluate the multi-view spatial reasoning capabilities of VLMs in robotic manipulation. MV-RoboBench consists of 1.7k manually curated QA items across eight subtasks, divided into two primary categories: spatial understanding and robotic execution. We evaluate a diverse set of existing VLMs, including both open-source and closed-source models, along with enhanced versions incorporating Chain-of-Thought (CoT)-inspired techniques. The results show that state-of-the-art models remain far below human performance, underscoring the substantial challenges VLMs face in multi-view robotic perception. Additionally, our analysis uncovers two key findings: (i) spatial intelligence and robotic task execution are positively correlated in multi-view robotic scenarios; and (ii) strong performance on existing general-purpose single-view spatial understanding benchmarks does not reliably translate to success in the robotic spatial tasks assessed by our benchmark. We release MV-RoboBench as an open resource to foster progress in spatially grounded VLMs and VLAs, providing not only data but also a standardized evaluation protocol for multi-view embodied reasoning.

---

## 论文详细总结（自动生成）

# 跨视角观察：基准测试机器人场景中视觉-语言模型的空间推理能力

## 1. 论文的核心问题与整体含义

- **核心问题**：现有的视觉-语言模型（VLMs）评测主要集中在**单视角**场景，而现代机器人平台普遍采用**多摄像头**配置，以克服遮挡和深度歧义。但 VLMs 能否有效整合**多视图**信息进行空间推理和操作决策，这一能力尚未被系统评估。
- **研究动机**：VLMs 是具身智能与最近视觉-语言-行动（VLA）模型的基础，其多视图空间推理能力直接关系到机器人在真实环境中的感知与执行。因此，**填补多视图机器人空间推理评测的空白**，对于推动 VLAs 的实用化至关重要。
- **整体含义**：该工作通过构建专门的基准，揭示了现有 VLMs 在多视图机器人场景中的**显著短板**，并提出了一个标准化的评估体系，旨在引导未来模型向真正的多视图具身理解发展。

## 2. 论文提出的方法论

- **核心思想**：设计一个**系统化的基准测试**（MV-RoboBench），通过一系列多视图问答对，量化 VLMs 在机器人操作中的空间推理能力。
- **关键技术细节**：
    - **数据构建**：手工策划 1.7k 个高质量的问答项，覆盖 **8 个子任务**，并归入两大类别：**空间理解**（如物体的相对位置、朝向）与**机器人执行**（如抓取规划、碰撞检测）。
    - **评测模式**：提供多幅不同视角的 RGB 图像作为输入，要求模型回答相关问题，检验其对跨视图几何关系的整合能力。
    - **基线增强**：除直接评测现有模型外，还引入了受 **思维链（Chain-of-Thought, CoT）** 启发的推理增强技术，以探索显式推理对多视图理解的帮助。
- **评估对象**：涵盖**开源与闭源**的一系列 VLMs，以反映领域前沿的真实水平。

## 3. 实验设计

- **数据集与场景**：
    - 使用自建的 **MV-RoboBench** 基准，包含 `1.7k` 个手工标注的多视图问答对。
    - 场景聚焦于**机器人操作**任务，包含遮挡、深度模糊等典型视觉挑战，通过多摄像头视角提供互补信息。
- **对比方法**：
    - **多类 VLMs**：评估了当前主流的开源模型和闭源（商业）模型。
    - **增强版本**：对比上述模型在加入 CoT 式推理策略前后的性能变化。
    - **人类表现**：以人类在该基准上的得分为**上限参考**。
- **衡量指标**：推测以各子任务和总体上的准确率（或类似指标）作为空间推理能力的量化标准。

## 4. 资源与算力

- 论文摘要与提供的元数据中**未明确说明**所使用的 GPU 型号、数量及训练时长等计算资源消耗。由于该工作主要贡献是**基准构建与评测**，而非训练大规模模型，其推理过程的算力需求相对较小或未予重点报告。

## 5. 实验数量与充分性

- **实验组数量**：
    - 根据摘要，至少进行了 **两大组对比**：①多类现有 VLMs 的直接测评；②加入 CoT 增强后的效果评估。同时包含与 **人类基准** 的横向比较。
    - 考虑到 8 个子任务，实际结果可能按任务逐一报告，实验矩阵较为丰富，但具体消融实验的种类无法从摘要中获知。
- **充分性与客观性**：
    - **数据来源**：手工标注的 1.7k 样本确保了质量与针对性，但样本规模相对于大规模多视图变化来说属于中等。
    - **模型覆盖**：同时纳入开源与闭源模型，提升了结论的**普适性与公平性**。
    - **任务多样性**：两大类别 8 个子任务的设计，从感知到执行层面形成梯度，能较**全面地**暴露模型弱点，实验设计较为充分。

## 6. 论文的主要结论与发现

- **模型与人类差距显著**：当前最先进的 VLMs 在 MV-RoboBench 上的表现**远低于人类水平**，多视图机器人空间推理仍是巨大挑战。
- **正相关关系**：在多视图机器人场景中，模型的**空间智能与其机器人任务执行能力呈正相关**，验证了空间推理对具身操作的基础作用。
- **跨基准迁移有限**：在通用单视图空间理解基准上表现强劲的模型，**并不能可靠地迁移**到机器人多视图空间任务中，说明现有的单视图评测无法替代专门的多视图具身评测。
- **标准化需求迫切**：该基准暴露了当前 VLA 模型在多视图整合上的关键缺陷，并提供了推进研究的标准化测试平台。

## 7. 优点

- **填补领域空白**：首次系统性地针对多视图机器人空间推理建立评测基准，抓住了 VLAs 实际部署的痛点。
- **任务设计扎实**：手工精心标注的 1.7k 问答对，且细分为空间理解与执行两大类，**贴近真实机器人需求**。
- **评估体系完整**：横跨开源/闭源模型、引入 CoT 增强、与人类水平对标，形成**多层次的诊断框架**。
- **资源开源**：承诺开放基准与标准化评估协议，为社区提供**可复现、可跟踪**的研究工具，具有长期价值。

## 8. 不足与局限

- **规模局限**：数据量（1.7k）和任务数量（8 个）可能无法覆盖长尾机器人操作场景，模型的**泛化性评估仍有限**。
- **场景特异性**：基准完全围绕机器人操作，虽具针对性，但对其他具身平台（如自动驾驶、无人机）的多视图推理覆盖不足。
- **模态限制**：目前仅使用 RGB 图像，未纳入深度、触觉等机器人常用感知模态，与真实机器人系统的**多模态输入仍有距离**。
- **静态评测**：问答形式的静态评测可能无法完全反映动态交互中模型的空间推理需求，例如持续的动作序列决策。
- **算力报告缺失**：未提及推理所需的资源开销，可能影响计算受限场景下的应用评估。

（完）
