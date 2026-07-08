---
title: Lifelong Language-Conditioned Robotic Manipulation Learning
title_zh: 终身语言条件机器人操作学习
authors: "Xudong Wang, Zebin Han, Zhiyu Liu, Gan Li, Jiahua Dong, Baichen Liu, Lianqing Liu, Zhi Han"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38930/42892"
tags: ["query:analysis"]
score: 4.0
evidence: 基于SVD的技能语义子空间，用于终身技能表示学习
tldr: 针对语言条件机器人技能持续学习中的灾难性遗忘问题，SkillsCrafter通过对技能指令进行奇异值分解获得公共语义子空间投影矩阵，记录技能本质语义，并结合技能适配实现新旧知识的共享与保留。该方法在动态场景下持续学习多个操作技能，减轻了遗忘，为终身机器人学习提供了有效策略。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38930/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1823, \"height\": 640, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38930/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1749, \"height\": 431, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38930/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1818, \"height\": 672, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38930/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 869, \"height\": 544, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38930/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 877, \"height\": 435, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38930/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1845, \"height\": 549, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38930/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1836, \"height\": 552, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38930/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 874, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38930/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 869, \"height\": 249, \"label\": \"Table\"}]"
motivation: 传统方法学习新技能时遗忘旧技能，难以适应动态场景。
method: SVD分解技能指令得公共语义子空间，结合技能适配和知识投影。
result: 在多个操作技能上持续学习，有效减少了灾难性遗忘。
conclusion: SkillsCrafter为机器人终身学习提供了语义空间保留方法。
---

## Abstract
Traditional language-conditioned manipulation agent adaptation to new manipulation skills leads to catastrophic forgetting of old skills, limiting dynamic scene practical deployment. In this paper, we propose SkillsCrafter, a novel robotic manipulation framework designed to continually learn multiple skills while reducing catastrophic forgetting of old skills. Specifically, we propose a Manipulation Skills Adaptation to retain the old skills knowledge while inheriting the shared knowledge between new and old skills to facilitate learning of new skills. Meanwhile, we perform the singular value decomposition on the diverse skill instructions to obtain common skill semantic subspace projection matrices, thereby recording the essential semantic space of skills. To achieve forget-less and generalization manipulation, we propose a Skills Specialization Aggregation to compute inter-skills similarity in skill semantic subspaces, achieving aggregation of the previously learned skill knowledge for any new or unknown skill. Extensive simulator and real-world experiments demonstrate the effectiveness and superiority of our SkillsCrafter.

---

## 论文详细总结（自动生成）

好的，作为资深学术论文分析助手，我将使用中文、以Markdown形式，对给定的论文《Lifelong Language-Conditioned Robotic Manipulation Learning》进行结构化、深入且客观的总结。

### 1. 核心问题与研究动机
*   **核心问题**：论文聚焦于**语言条件机器人操作（LCRM）** 领域的**灾难性遗忘（Catastrophic Forgetting）** 问题。现有的操作智能体在序列化学习新技能时，会急剧遗忘先前掌握的旧技能，这严重阻碍了机器人在动态、真实环境中的长期部署。
*   **研究目标**：旨在提出一种**终身语言条件机器人操作（Lifelong Language-Conditioned Robotic Manipulation, LLCRM）** 框架，使机器人能够持续学习并积累多项操作技能，同时**最大限度地减轻对旧技能的遗忘**，并能泛化到未知技能。

### 2. 方法论：SkillsCrafter框架
该工作提出了名为 **SkillsCrafter** 的创新框架，其核心思想是显式地利用不同技能间的**共享知识**和**特异性知识**，并通过技能语义子空间来关联和聚合参数。框架主要包含两个核心组件和一项推理机制：

*   **核心观察**：通过预实验，作者得出三个关键观察：（1）技能的参数子空间和语义子空间存在相似的关联性；（2）不同技能所需的学习子空间分布在Transformer的不同层；（3）LoRA（低秩适应）的矩阵A倾向于学习技能间的共享知识，而矩阵B倾向于学习技能特有的知识。

*   **操作技能适配（Manipulation Skills Adaptation, MSkA）**：
    *   **技能共享知识**：为利用共享知识促进新技能学习，当学习第t个新技能时，矩阵`At`的初始化不再是随机的，而是**通过继承**先前所有技能的矩阵A的加权聚合值`At*`。聚合权重由技能语义相似度计算得到。
    *   **技能特有知识**：为巩固特异知识，对矩阵`Bt`施加**正交性约束**，强制其与先前技能的矩阵B正交，避免干扰已学知识，并引入L2正则化防止退化为零矩阵。
    *   **动态稀疏加载**：针对不同技能对网络层依赖不同的观察，引入**Gumbel-Softmax门控机制**，动态决定是否在每一层注入LoRA适配器，实现稀疏化学习，避免过拟合或欠拟合。
    *   **损失函数**：总损失`Lt`由标准的自回归动作生成损失和正交约束项`Rt`（以及稀疏正则项`Ls`）共同构成。

*   **技能特化聚合（Skills Specialization Aggregation, SkSA）**：
    *   **语义子空间构建**：对于一项技能，首先使用CLIP文本编码器获取其多种指令的嵌入`Xt`，然后通过**奇异值分解（SVD）** `Xt = UΣVᵀ`提取右奇异向量矩阵的前`rs`行，构成该技能的**共同语义子空间投影矩阵**`ψt`，并保存下来。
    *   **知识聚合**：当面对一项新技能或未知技能`Sq`时，将其指令嵌入`E(Iq)`投影到所有已保存的语义子空间`ψ`上，通过余弦相似度计算其与每个旧技能的语义相似度`Sm`。最后，将相似度指数化后归一化，作为聚合权重`Ω`，用于加权融合所有旧技能的LoRA适配器参数，得到面向当前技能的自定义参数`ΔWq`。

*   **技能指定性推理（Skills Specified Inference, SkSI）**：在推理阶段，直接加载由SkSA为当前技能聚合出的适配器`ΔWq`，使基础模型能够利用累积的知识完成已知或未知任务。

### 3. 实验设计
*   **数据集/场景**：构建了一个全面的**终身机器人操作基准**，包含：
    *   **模拟器技能**：基于**RLBench**仿真器的12项常见操作技能（如开抽屉、推积木、存钱等）。
    *   **真实世界技能**：基于**UR-5机械臂**和RGB摄像头的6项真实操作技能（如扫入畚斗、烤肉取下、精密装配等）。
    *   前16个技能用于持续学习与测试，最后2个未训练的技能用于评估**开世界泛化能力**。
*   **对比方法（Benchmark）**：与当前主流的、基于LoRA的持续学习方法进行了全面比较，包括：
    *   **基础方法**：Sequence Fine-Tuning (Seq-FT).
    *   **正则化方法**：LwF-LoRA, EWC-LoRA.
    *   **专家混合/路由方法**：Dense MoLE, Sparse MoLE, MoLA, HydraLoRA, BranchLoRA.
    *   **正交约束方法**：O-LoRA (配合SkSA), SD-LoRA (配合SkSA).
*   **基础模型**：所有方法统一使用LLARVA作为主干网络。
*   **评估指标**：
    *   **平均成功率（ASR）**：每项技能进行25个回合（episodes）测试，计算成功率的百分比。
    *   **遗忘率（FR）**：衡量学习新技能后，旧技能成功率下降的程度。

### 4. 资源与算力
*   论文明确提到，所有方法的训练和测试均在 **8块 NVIDIA RTX 6000 Ada Generation GPU** 上进行。
*   使用的软件环境为 **PyTorch 2.1.2 with cu121**。
*   文中未明确提及总的训练时长。

### 5. 实验数量与充分性
*   **实验数量**：实验设计较为充分，包含：
    *   **1组主要对比实验**：在18项技能序列上，与8种基线方法进行全面对比。
    *   **1组预研实验（Preliminary Study）**：为验证方法论背后的三个核心观察，设计了三个探究性实验。
    *   **2组消融实验**：分别验证了技能共享/特异知识模块（GGM, INA, SOT）和技能知识聚合策略（IM, VM, Avg, TOP）的有效性。
*   **公平性与客观性**：
    *   **公平**：所有对比方法均基于相同的骨干网络（LLARVA）、优化器和学习率等设定，确保了比较的公平性。
    *   **客观**：定量结果以表格形式清晰列出，同时提供了可视化示例，结论有数据支撑。
    *   **充分**：实验覆盖了模拟和真实环境，评估指标同时兼顾了性能（ASR）和抗遗忘能力（FR），消融研究也有效论证了各模块的贡献，整体实验体系较为完整。

### 6. 主要结论与发现
*   **性能优越**：提出的SkillsCrafter在终身技能学习任务上，相较于所有对比方法，取得了**最高的平均成功率（ASR: 52.0%）** 和**最低的遗忘率（FR: 16.0%）**，证明了其在持续学习和抗遗忘方面的显著优势。
*   **泛化能力强**：在未训练的未知技能（S17, S18）上，SkillsCrafter同样展现了最高的成功率，表明其技能知识聚合机制能够有效泛化。
*   **模块有效性**：消融实验证实，动态门控加载（GGM）、共享知识继承（INA）和正交约束（SOT）等设计对性能提升起到了关键作用。基于SVD的指令匹配（IM）是更优的知识聚合方式。

### 7. 优点
*   **问题新颖**：首次明确定义并系统研究了**终身语言条件机器人操作（LLCRM）** 这一实际问题，并提供了相应的基准。
*   **观察深入**：通过预研究揭示了技能参数与语义子空间的关联、LoRA矩阵A和B的自然分工等关键洞察，为方法设计提供了理论依据。
*   **设计精巧**：巧妙地将**SVD技术**应用于提取语义子空间，并以此作为桥梁来衡量技能相似性、聚合参数知识，实现了从语义空间到参数空间的知识复用，构思巧妙。
*   **双重验证**：论文不仅在仿真环境（RLBench）中进行了评估，还在真实机器人平台上验证了方法的有效性，增强了其实际应用的说服力。

### 8. 不足与局限
*   **绝对成功率有待提升**：尽管相对优势明显，但其52.0%的平均成功率仍然不算高，表明在复杂的操作任务上大学网络可能还不够成熟，离实际自动化还有距离。
*   **语义空间的局限性**：技能相似度的计算完全依赖CLIP文本编码器，这可能忽略了对视觉、物理动态等非语言信息至关重要的技能的关联性。
*   **遗忘问题仍存在**：16.0%的遗忘率表明灾难性遗忘并未被完全解决，特别是对于较早学习的技能（如S1-S3），遗忘仍较为明显。
*   **开销与扩展性**：SVD的计算和所有旧适配器知识的存储与聚合，可能使其计算和内存开销随着技能数量的增加而线性增长，文章未讨论该框架在超大规模技能库下的扩展效率。

（完）
