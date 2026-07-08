---
title: "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver"
title_zh: ReconVLA：作为有效机器人感知器的重建式视觉-语言-动作模型
authors: "Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan, Yuxin Huang, Feilong Tang, Donglin Wang, Haoang Li"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38921/42883"
tags: ["query:analysis"]
score: 10.0
evidence: 诊断并纠正VLA模型中的视觉注意力错配
tldr: 通过经验分析发现现有VLA模型视觉注意力分散，导致无法关注正确目标物体。本文提出ReconVLA，利用扩散Transformer重建凝视区域，以隐式方式引导模型学习细粒度表征并正确分配视觉注意力，从而提升机器人操作精度，为VLA模型的诊断和表征改进提供了可解释性方法。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38921/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 870, \"height\": 569, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38921/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 870, \"height\": 286, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38921/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1569, \"height\": 812, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38921/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1832, \"height\": 503, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38921/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 812, \"height\": 505, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38921/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1741, \"height\": 377, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38921/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 850, \"height\": 293, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38921/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1240, \"height\": 277, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38921/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1760, \"height\": 554, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38921/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1778, \"height\": 342, \"label\": \"Table\"}]"
motivation: 现有VLA模型视觉注意力分散，无法准确定位操作目标。
method: 提出隐式定位范式，通过扩散Transformer重建目标物体凝视区域来引导注意力。
result: 在机器人操作基准上，ReconVLA显著提高了任务成功率和视觉注意力准确性。
conclusion: 重建式模态可有效改善VLA模型的视觉表征和对动作的注意力对齐。
---

## Abstract
Recent advances in Vision-Language-Action (VLA) models have enabled robotic agents to integrate multimodal understanding with action execution. However, our empirical analysis reveals that current VLAs struggle to allocate visual attention to target regions.
Instead, visual attention is always dispersed. To guide the visual attention grounding on the correct target, we propose ReconVLA, a reconstructive VLA model with an implicit grounding paradigm.  Conditioned on the model's visual outputs, a diffusion transformer aims to reconstruct the gaze region of the image, which corresponds to the target manipulated objects. This process prompts the VLA model to learn fine-grained representations and accurately allocate visual attention, thus effectively leveraging task-specific visual information and conducting precise manipulation. Moreover, we curate a large-scale pretraining dataset comprising over 100k trajectories and 2 million data samples from open-source robotic datasets, further boosting the model’s generalization in visual reconstruction. Extensive experiments in simulation and the real world demonstrate the superiority of our implicit grounding method, showcasing its capabilities of precise manipulation and generalization.

---

## 论文详细总结（自动生成）

好的，作为一名资深学术论文分析助手，我将以 Markdown 形式，对所提供的论文《ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver》进行结构化、深入、客观的总结。

### 1. 论文的核心问题与整体含义

*   **核心问题**：当前的视觉-语言-动作（VLA）模型在为机器人执行操作任务时，面临一个关键痛点：**视觉注意力分散**。经验分析表明，VLA 模型在生成动作时，其视觉注意力往往无法精确地聚焦于指令所指的目标物体，而是分散在整个场景的无关区域。这导致机器人容易抓取或操作错误的对象，尤其在存在干扰物的杂乱环境或长周期任务中表现不佳。
*   **整体含义**：该问题本质上源于 VLA 模型缺乏对目标区域进行细粒度感知和精确定位的内在机制。为了解决这个问题，论文受到人类视觉系统中“凝视”（Gaze）行为的启发，提出了一种名为 **ReconVLA** 的全新框架。核心思想是通过一个辅助的**隐式视觉重建任务**来作为一种“软监督”，强制 VLA 模型学习目标区域的精细特征，从而从根本上引导其视觉注意力，最终实现更精准的机器人操控。这项工作旨在提升 VLA 模型作为机器人“感知器”的有效性。

### 2. 论文提出的方法论

*   **核心思想：隐式定位范式（Implicit Grounding）**
    *   与传统的显式定位方法（如输入裁剪后的图像或输出边界框）不同，ReconVLA 不直接或间接地处理目标的位置信息。其核心思想是让模型通过**重建“凝视区域”（被操作的目标区域）**来驱动自身内部表征向目标聚焦，这个过程如同人类眼睛自动聚焦于感兴趣的区域。
*   **关键技术细节与流程**:
    1.  **基础架构**：ReconVLA 基于一个预训练的视觉-语言模型（VLM），如 LLaVA-7b，该模型包含一个视觉编码器、一个大型语言模型（LLM）和一个分词器。
    2.  **双任务训练目标**：
        *   **动作预测任务 (Action Part)**：模型接收多视角图像 `I` 和文本指令 `S`，以自回归方式生成离散的动作令牌序列 `a`，并由动作解码器映射为可执行的动作 `A`。损失函数 `L_action` 为标准的交叉熵损失。
        *   **视觉重建任务 (Reconstruction Part)**：这是论文的核心创新。模型被引导输出一系列“重建令牌”（Reconstructive Tokens）`hR`。这些令牌作为条件，输入到一个**轻量级的扩散 Transformer 去噪器（Denoiser）**中。
    3.  **重建过程**：
        *   **目标**：目标是重建输入图像中对应于被操作物体的“凝视区域” `I'`。
        *   **潜空间重建**：为避免像素级别的冗余，一个预训练并冻结的连续 VAE 视觉分词器 `F` 将凝视区域图像 `I'` 编码为场景令牌 `z0`。随后，向 `z0` 添加噪声得到 `zt`。
        *   **去噪网络**：扩散去噪器 `D` 以 VLA 模型输出的重建令牌 `hR` 为条件，预测并去除 `zt` 上的噪声，力图恢复出原始的 `z0`。损失函数 `L_visual` 为预测噪声与真实噪声之间的均方误差（MSE）。
    4.  **大规模预训练**：
        *   **数据集构建**：为了增强模型的泛化能力，作者整合了 BridgeData V2、LIBERO 和 CALVIN 等开源机器人数据集，利用微调后的 Grounding DINO 模型自动提取每张图像中的目标操作区域，构建了一个包含超过 10 万条轨迹和 200 万个样本的配对预训练数据集。
        *   **预训练**：在预训练阶段，模型同时优化动作损失和重建损失，让 VLM 习得基础的视觉重建和定位能力。随后，再在特定任务上微调，将对齐视觉-语言理解和重建能力与操控能力。

### 3. 实验设计

*   **实验环境与基准**：
    *   **模拟环境**：主要在 **CALVIN** 基准上进行评估。该基准基于 PyBullet 模拟器，包含一个 Franka Panda 机械臂和 34 项语言条件操作任务，分布在使用 A、B、C、D 四个不同纹理环境的场景中。它专门用于测试模型的长期规划能力。
    *   **评估指标**：使用 CALVIN 提供的标准指标，即从 1/5 到 5/5 的连续子任务成功率及 5 次连续任务的平均完成长度。
*   **主要对比方法**：
    *   **不同视觉定位范式**：在同一基线 VLA 模型上实现了**显式定位（EG, 将检测到的目标物体裁剪并作为额外输入）**和**思维链定位（CG, 预测边界框坐标作为动作前序输出）**，以验证所提隐式定位方法（IG）的优越性。
    *   **生成式方法**：UniPi, SuSIE, CLOVER, GR-1, Vidman, GEVRM 等通过预测未来图像或视频进行规划的方法。
    *   **大型 VLA 模型**：RoboFlamingo, OpenVLA, VLAS, UniVLA 等。
    *   **真实世界测评**：对比了 **OpenVLA** 和 **PD-VLA**。

### 4. 资源与算力

*   论文中**未明确说明**所使用的 GPU 型号、数量、批处理大小或具体的训练时长等硬件算力信息。

### 5. 实验数量与充分性

*   **实验数量**：论文进行了相当数量的实验来支撑其论点，具体包括：
    *   **1 组范式对比实验**（表 1），以证明隐式定位优于其他方法。
    *   **1 组消融实验**（表 2），分析了“重建模块”、“凝视区域”和“预训练”三个关键组件的作用。
    *   **2 组大规模模拟环境性能对比**（表 3，表 4），与 10 余种当前最优方法在 `ABC->D` 和 `ABCD->D` 两种数据划分下进行比较。
    *   **1 组真实世界多任务实验**（图 6），在 4 个代表性任务和 2 个未见任务上与 2 个基线模型比较。
    *   此外还包括**可视注意力图**的定性分析（图 4）和针对特定精确操作任务（如叠方块）的深入分析。
*   **实验充分性与客观性**：
    *   **充分性**：实验设计相对全面，覆盖了从方法验证、组件消融到大模型横向对比和真实世界迁移的完整链条。尤其是在 CALVIN 基准上的 `ABC->D`（测试环境泛化）和 `ABCD->D`（测试全面性能）两种设置，充分考验了模型的泛化能力和长期任务规划能力。
    *   **客观公平性**：范式对比实验均在相同基线模型上进行，公平性较高。与 SOTA 方法的对比引用了各论文报告的公开结果，且遵循了 CALVIN 基准的 500 次 rollout 评估标准，具有可比性。然而，CALVIN 模拟环境本身存在领域差距（domain gap），真实世界实验的评测任务和样本数量（每任务20次）相对有限，其结论的普遍性有待更多真实场景验证。

### 6. 论文的主要结论与发现

*   **隐式定位有效且最优**：通过重建凝视区域来引导视觉注意力的隐式范式，在性能上显著优于输入裁剪图像的“显式定位”和输出边界框的“思维链定位”方法。
*   **注意力机制得到根本性改善**：可视化结果表明，ReconVLA 的注意力图能够从分散状态转变为高度集中于目标物体（凝视区域），从而带来更准确的行为决策。
*   **精准操控能力提升显著**：注意力机制的改善直接转化为卓越的操作精度，尤其在“叠方块”这类对精度要求极高的长周期任务中，成功率相比基线大幅提升。
*   **大规模预训练至关重要**：消融实验证明，在百万级机器人数据上进行视觉重建预训练，对于增强模型面向新场景和未见物体的泛化能力起到了关键作用。

### 7. 优点

*   **思想新颖且直观**：将人类视觉的“凝视”机制引入 VLA 模型的训练中，通过重建任务隐式地提升注意力分配，思路巧妙且具有生物学启发性。
*   **方法简洁高效**：相较于需要额外输入或输出的显式定位方法，ReconVLA 的隐式定位策略不增加推理时的输入复杂度，也不改变模型原始的输出格式，实现了一种优雅的、端到端的训练方案。
*   **内在机制解析清晰**：通过注意力图的可视化分析，清晰地展示了观察到的现象（注意力分散）和解决方法（注意力聚焦）之间的因果关系，增强了方法的可解释性。
*   **性能提升显著且全面**：无论是在模拟环境还是真实世界，相比多种类型的基线模型，ReconVLA 都展现了强大的性能优越性和泛化潜力。

### 8. 不足与局限

*   **算力开销未披露**：训练一个包含扩散去噪模块的 VLA 模型，并在百万级数据上进行预训练，其所需算力成本、具体配置和训练时长等关键信息缺失，不利于其他研究者复现或评估其资源需求。
*   **对视觉分词器的依赖**：目标物体的“凝视区域”在预训练阶段依赖于 Grounding DINO 模型，这意味着模型的“凝视”能力上界受限于该预训练目标检测器的性能。
*   **真实世界实验规模有限**：尽管展示了真实世界结果，但实验仅涉及单个双臂机器人、4 个类型的任务和有限的试次，评估的全面性有待加强。未见任务的实验如果仅仅更换了颜色或极为相似形状的物体，对“泛化”能力的证明强度可能稍弱。
*   **任务复杂度仍有提升空间**：实验任务主要集中在小范围桌面上的拾取、放置、堆叠等操作。未来可探索在更复杂、更动态的环境中检验该方法的鲁棒性。

（完）
