---
title: "OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints"
title_zh: OmniManip：通过物体为中心交互原语实现通用机器人操作
authors: "Pan, Mingjie, Zhang, Jiyao, Wu, Tianshu, Zhao, Yinghao, Gao, Wenlong, Dong, Hao"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Pan_OmniManip_Towards_General_Robotic_Manipulation_via_Object-Centric_Interaction_Primitives_as_CVPR_2025_paper.pdf"
tags: ["query:model"]
score: 7.0
evidence: 面向VLA操作中精细3D空间推理的物体中心化表示
tldr: OmniManip 针对 VLM 缺乏细粒度 3D 空间理解而难以精准操作的问题，提出一种物体中心化表示，通过在物体规范空间定义空间约束，将 VLM 的高层推理与低层操作衔接，避免昂贵的数据采集和微调，提升了机器人操作的泛化性和精度。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1777, \"height\": 718, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1795, \"height\": 1217, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 869, \"height\": 602, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 861, \"height\": 587, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 853, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 854, \"height\": 537, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 847, \"height\": 476, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 854, \"height\": 492, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 871, \"height\": 817, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1737, \"height\": 819, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 804, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-pan-omnimanip-towards-general-robotic-manipulation-via-object-centric-interaction-primitives-as-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 835, \"height\": 246, \"label\": \"Table\"}]"
motivation: VLM 缺乏精细 3D 空间理解，VLA 微调成本高泛化差。
method: 提出物体中心化表示，在物体规范空间定义交互原语作为空间约束。
result: 实现了无需微调的高精度操作泛化。
conclusion: 物体中心化表示有效衔接推理与操作，提升通用性。
---

## Abstract
The development of general robotic systems capable of manipulating in unstructured environments is a significant challenge. While Vision-Language Models(VLM) excel in high-level commonsense reasoning, they lack the fine-grained 3D spatial understanding required for precise manipulation tasks. Fine-tuning VLM on robotic datasets to create Vision-Language-Action Models(VLA) is a potential solution, but it is hindered by high data collection costs and generalization issues. To address these challenges, we propose a novel object-centric representation that bridges the gap between VLM's high-level reasoning and the low-level precision required for manipulation. Our key insight is that an object's canonical space, defined by its functional affordances, provides a structured and semantically meaningful way to describe interaction primitives, such as points and directions. These primitives act as a bridge, translating VLM's commonsense reasoning into actionable 3D spatial constraints. In this context, we introduce a dual closed-loop, open-vocabulary robotic manipulation system: one loop for high-level planning through primitive resampling, interaction rendering and VLM checking, and another for low-level execution via 6D pose tracking. This design ensures robust, real-time control without requiring VLM fine-tuning. Extensive experiments demonstrate strong zero-shot generalization across diverse robotic manipulation tasks, highlighting the potential of this approach for automating large-scale data generation.

---

## 论文详细总结（自动生成）

好的，这是根据您提供的论文内容生成的结构化中文总结。

### 1. 论文的核心问题与整体含义
*   **研究动机**：开发能够在非结构化环境中进行操作的通用机器人系统是一个重大挑战。当前，视觉-语言模型（VLM）虽然在高层常识推理方面表现出色，但缺乏精确操作任务所需的细粒度3D空间理解能力。
*   **现有方案局限**：一种潜在的解决方案是将VLM在机器人数据集上微调成视觉-语言-动作模型（VLA），但这面临数据采集成本高昂和泛化能力差的问题。
*   **整体含义**：论文提出一个核心观点，即一个物体的**规范空间**（由其功能可供性定义）能够以一种结构化且语义明确的方式来描述交互原语（如点和方向）。这些原语作为桥梁，将VLM的常识推理转化为可操作的3D空间约束，从而在不进行VLM微调的情况下，实现鲁棒的、实时的通用机器人操作。

### 2. 论文提出的方法论
*   **核心思想**：提出一种新颖的、以物体为中心的中间表示。该表示在物体的规范空间内定义**交互原语**（交互点 `p` 和交互方向 `v`），并将其作为**空间约束**来指导低层操作。
*   **关键技术细节**：
    *   **任务分解**：给定指令，VLM会先从场景中筛选出任务相关物体，并将复杂任务分解为多个阶段（如抓起茶壶、倒入杯中）。每个阶段定义了主动物体、被动物体和原子动作。
    *   **交互原语提取**：
        *   **交互点**：利用视觉提示机制（如SCAFFOLD），在2D图像上定位可见/可触摸的点。对于不可见或不可触摸的点（如中心开口），则利用规范空间的多视图推理来推断。
        *   **交互方向**：将物体的主轴作为候选交互方向。先用VLM为每个主轴生成语义描述，再用大语言模型（LLM）评估其与任务的相关性并打分，从而得到有序的候选方向。
    *   **空间约束定义**：通过距离约束（`D(Oa, Op) = di`）和角度约束（`Θ(Oa, Op) = θi`）来定义主动与被动物体交互原语之间的几何关系。
    *   **双闭环系统**：
        *   **规划闭环**：引入**重采样、渲染、检查（RRC）**的自纠正机制。系统会根据当前空间约束渲染交互图像，由VLM检查是否正确。若需优化，则进行细化重采样，从而有效缓解VLM的幻觉问题。
        *   **执行闭环**：将任务执行形式化为一个优化问题（公式2），目标是最小化包含约束损失、碰撞损失和路径损失的损失函数，以求解末端执行器的最优姿态。在实时执行中，利用现成的6D物体姿态跟踪算法，持续更新物体位姿，实现鲁棒的闭环控制。

### 3. 实验设计
*   **数据集与场景**：实验在真实世界的12项操作任务上进行，包括6项刚性物体操作（如倒茶、插花）和6项关节物体操作（如开关抽屉、按按钮），覆盖了多种物体和交互类型。
*   **基准对比方法**：选择了三个具有代表性的基线方法进行对比：
    *   **VoxPoser**：使用LLM和VLM生成3D价值图以合成轨迹。
    *   **CoPa**：引入物体部件的空间约束，结合VLM实现开放词汇操作。
    *   **ReKep**：利用关系关键点约束和分层优化，从自然语言指令生成实时动作。
*   **评估指标**：对每个任务进行10次独立试验，每次试验后重新配置物体布局，以成功操作次数计算成功率。

### 4. 资源与算力
*   论文正文中**未明确提及**所使用的GPU型号、数量或训练时长等具体的算力资源信息。方法主要依赖调用预训练模型（如GPT-4o、Omni6DPose）和算法优化，而非大规模模型训练。

### 5. 实验数量与充分性
*   **实验组数**：实验设计较为系统和充分，主要包括：
    *   **主实验**：在12个任务上进行定量对比，共计480次试验（4种方法 × 12任务 × 10次）。
    *   **消融实验**：通过禁用规划闭环的方式，验证了闭环规划模块对性能的提升（成功率下降超15%）。
    *   **稳定性与一致性分析**：通过对比试验（见表2、图5、图6），量化并定性分析了方法在不同视角下的表现一致性以及交互原语提取的鲁棒性，与ReKep、CoPa进行了对比。
    *   **效率分析**：通过对比论文的采样策略与SO(3)均匀采样的迭代次数和成功率，验证了其采样效率。
*   **充分性与公平性**：实验覆盖了多种任务类型，对比了当代最先进且思路相近的方法，并进行了关键的消融和属性分析，实验设计客观、公平，能够有力支撑其结论。

### 6. 论文的主要结论与发现
*   **强大的零样本泛化能力**：提出的OmniManip系统在无需任何特定任务训练的情况下，在12项开放词汇操作任务中均表现出色，总成功率远超基线方法。
*   **闭环系统至关重要**：所提出的**规划与执行双闭环**设计是系统鲁棒性的关键。规划闭环有效减少了大模型幻觉导致的失败，执行闭环则能应对象对物体位移、抓取偏差等动态不确定性。
*   **表示方法的优越性**：以**物体规范空间为中心的交互原语**作为一种中间表示，比基于表面关键点（如ReKep）或部件分割（如CoPa）的方法更稳定、视角一致性更强、采样效率更高，能更好地桥接VLM推理与底层3D几何。

### 7. 优点
*   **无需微调**：完全避开了VLA微调带来的高昂数据成本和特定机器人表征的泛化性限制。
*   **视角不变性**：由于交互原语定义在物体的规范空间中，其提取具有近似视角不变性，这相对于依赖表面关键点的基线方法是一个显著优势。
*   **完整的闭环设计**：首次在规划和执行两个层面实现闭环控制，显著提升了整个操作流程的鲁棒性和成功率。
*   **高效的采样策略**：利用物体的功能主轴作为先验进行交互方向采样，比在SO(3)空间均匀采样效率更高，效果更好。

### 8. 不足与局限
*   **对象限制**：该方法无法处理可变形物体，因为其核心依赖基于6D姿态的刚性表示。
*   **依赖外部模型质量**：系统性能严重依赖单视图3D生成（AIGC）的网格质量，尽管该领域已有进展，但仍是潜在瓶颈。
*   **计算效率问题**：框架需要多次调用VLM和LLM（如RRC循环），即使采用并行处理，也带来了显著的计算挑战和延迟。
*   **原子动作有限**：预定义的6种原子动作是基本的操作基元，本身不含3D空间推理能力，其成功执行完全依赖OmniManip框架，但在处理超出这6种动作的复杂任务时可能受限。

（完）
