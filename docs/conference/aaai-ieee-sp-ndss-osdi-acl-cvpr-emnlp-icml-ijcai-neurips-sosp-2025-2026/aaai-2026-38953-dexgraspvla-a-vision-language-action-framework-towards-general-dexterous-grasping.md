---
title: "DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping"
title_zh: DexGraspVLA：面向通用灵巧抓取的视觉-语言-动作框架
authors: "Yifan Zhong, Xuchuan Huang, Ruochong Li, Ceyao Zhang, Zhang Chen, Tianrui Guan, Fanlian Zeng, Ka Nam Lui, Yuyao Ye, Yitao Liang, Yaodong Yang, Yuanpei Chen"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38953/42915"
tags: ["query:model"]
score: 9.0
evidence: 用于灵巧抓取的分层VLA框架，具有域不变表示
tldr: 针对灵巧抓取的泛化难题，提出分层VLA框架DexGraspVLA，高层使用预训练视觉语言模型规划，低层采用扩散策略执行。其泛化关键在于将多样化的语言和视觉输入迭代转换为域不变表征。实验表明该方法能有效提升跨场景和物体的抓取鲁棒性，为通用机器人操作提供了新的范式。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38953/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 784, \"height\": 779, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38953/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1364, \"height\": 1028, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38953/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 700, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38953/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 849, \"height\": 598, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38953/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 843, \"height\": 369, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38953/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 481, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38953/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 569, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38953/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 915, \"height\": 369, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38953/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 605, \"height\": 258, \"label\": \"Table\"}]"
motivation: 现有灵巧抓取方法场景受限，泛化能力不足，需要通用框架。
method: 分层架构：高层VLM规划，低层扩散策略控制，迭代生成域不变表示。
result: 该方法在多种物体和场景下实现了鲁棒泛化的灵巧抓取。
conclusion: DexGraspVLA为通用灵巧操作提供了可扩展的VLA解决方案。
---

## Abstract
Dexterous grasping remains a fundamental yet challenging problem in robotics. A general-purpose robot must be capable of grasping diverse objects in arbitrary scenarios. However, existing research typically relies on restrictive assumptions, such as single-object settings or limited environments, showing constrained generalization. We present DexGraspVLA, a hierarchical framework for robust generalization in language-guided general dexterous grasping and beyond. It utilizes a pre-trained Vision-Language model as the high-level planner and learns a diffusion-based low-level Action controller. The key insight to achieve generalization lies in iteratively transforming diverse language and visual inputs into domain-invariant representations via foundation models, where imitation learning can be effectively applied due to the alleviation of domain shift. Notably, our method achieves a 90+% dexterous grasping success rate under thousands of challenging unseen cluttered scenes. Empirical analysis confirms the consistency of internal model behavior across environmental variations, validating our design. DexGraspVLA also, for the first time, simultaneously demonstrates free-form long-horizon prompt execution, robustness to adversarial objects and human disturbance, and failure recovery. Extended application to nonprehensile grasping further proves its generality.

---

## 论文详细总结（自动生成）

好的，作为一名资深学术论文分析助手，我将以 Markdown 格式对该论文进行结构化、深入、客观的总结。

### 1. 论文的核心问题与整体含义

*   **核心问题**： 灵巧抓取（Dexterous Grasping）是机器人领域的基础性挑战。现有方法要么依赖于单物体、受限环境的简化假设，缺乏泛化能力；要么是开环的两阶段（检测-规划）方法，对环境变化和扰动鲁棒性差；端到端的模仿学习方法虽然能实现闭环控制，但其核心瓶颈在于难以超越训练数据的分布，无法泛化到多样的未知场景。
*   **整体含义/动机**： 旨在开发一个通用的、语言引导的灵巧抓取框架，使其能够在数千种未见过的杂乱场景中可靠工作。论文的核心洞察在于，通过基础模型（Foundation Models）将多样化的视觉、语言输入迭代地转换为**域不变表征（Domain-Invariant Representations）**，从而缓解模仿学习中的域偏移（Domain Shift）问题，实现鲁棒的泛化。

### 2. 论文提出的方法论

*   **核心思想**： 构建分层式视觉-语言-动作（VLA）框架 **DexGraspVLA**，将基础模型的泛化能力与模仿学习的动作建模能力相结合。其关键是在多个层级上将时变、多样的感官输入转化为稳定、域不变的表征，然后在此之上应用模仿学习。
*   **框架结构与关键技术细节**：
    *   **高层规划器（High-Level Planner）**：
        *   采用一个预训练的视觉语言模型（如 Qwen-VL）。
        *   **功能**： 接收自由形式的用户提示（如“清理桌面”），进行任务推理和分解，并动态规划抓取流程。
        *   **域不变转换**： 将灵活多变的语言指令 `l` 转换为一个一致、通用的任务示能（Affordance）信号——目标物体的**边界框** `(x1, y1, x2, y2)`。这一步缓解了语言输入的域偏移。
    *   **低层控制器（Low-Level Controller）**：
        *   **掩码生成与追踪**： 接收高层规划器提供的边界框，利用预训练视觉基础模型 **SAM** (Segment Anything Model) 生成目标物体的初始二进制掩码 `m0`，并使用 **Cutie** 模型进行实时追踪，获得时刻 `t` 的掩码 `mt`。
        *   **域不变视觉特征提取**： 认识到原始像素易受环境影响，使用冻结的预训练视觉基础模型 **DINOv2** 作为特征提取器 `ϕ`，从原始的第一视角和第三视角图像中提取鲁棒、语义一致的视觉特征 `zh_t` 和 `zw_t`。这一步缓解了视觉输入的域偏移。
        *   **特征融合**： 将掩码 `mt` 投影到图像特征空间并与图像特征 `zh_t` 拼接，同时通过 MLPs 融合机器人本体感受 `st`，形成最终的观察特征序列 `˜z_obs_t`。
        *   **动作生成**： 采用基于 **扩散策略** 的 **DiT** (Diffusion Transformer) 模型作为动作头。该模型以 `˜z_obs_t` 为条件，通过学习从噪声中重建动作序列来生成未来H步的动作块 `At`。
    *   **工作流程**： 规划器持续监控控制器执行，根据新场景提出新指令，直至整个任务完成。控制器以滚动时域控制的方式运行。

### 3. 实验设计

*   **数据集/场景**：
    *   **训练数据**： 在一个固定的环境中，使用36个家庭常见物体，手动收集了 **2,094** 条成功的杂乱场景抓取演示。
    *   **测试环境**： **零样本（Zero-Shot）** 设定，即测试环境与训练环境完全不同，以严格评估泛化性。测试使用了 **360个新物体**、**6种未见背景**和 **3种未见光照条件**。
*   **基准（Benchmark）**： 设定了多种任务进行对比和评估。
    *   **大规模泛化评估**： 对数千个未见物体、背景、光照的组合进行抓取测试。
    *   **基线对比**： 在一个子集上，与当前最佳的端到端 VLA 模型进行比较，包括 **π0** (含全参/ LoRA微调)、**RDT-1b**、**OpenVLA** (含LoRA/ OFT微调)。
    *   **消融实验**： 在单物体抓取任务上，与自身模型的删减版（ **DINOv2-train**：DINOv2 参与训练；**ViT-small**：用小训练ViT替代DINOv2）进行对比。
    *   **长时域任务评估**： 在需多步推理和执行的杂乱场景中测试框架执行“清理桌面”等复杂指令的能力。
    *   **扩展应用**： 将框架直接应用于“非抓握式抓取”任务并评估其泛化性。
*   **评估指标**： 核心指标是**成功率**，定义为将物体抓离桌面10厘米并保持20秒的比例。

### 4. 资源与算力

*   **论文未明确提及**： 文中没有说明训练该框架所使用的GPU型号、数量及具体训练时长等算力信息。

### 5. 实验数量与充分性

*   **实验数量丰富**： 论文进行了相当大规模的实验，包括：
    *   一项包含 **1，287** 个未见场景组合的大规模泛化测试。
    *   一项与 **5个主流基线模型** 在多个测试维度上的对比实验。
    *   两项针对 **2个消融变体** 的实验。
    *   一项有 **96个场景** 的长时域任务评估。
    *   一项包含 **144次测试** 的非抓握式抓取扩展实验。
*   **评估充分且客观公正**：
    *   **充分性**： 覆盖了从对比、消融到大规模泛化、复杂任务和领域外应用的多层次评估，十分全面。
    *   **客观性**： 所有测试均在“零样本”环境下进行，确保了评估的严格性。与基线的对比是在相同的数据集和任务上进行，保证了公平性。内部行为分析（可视化特征、注意力图）进一步为方法的有效性提供了机理层面的证据，而非仅依赖最终性能。

### 6. 论文的主要结论与发现

*   **卓越的泛化性能**： DexGraspVLA 在包含 1，287 个未见场景（物体、背景、光照组合）的零样本杂乱场景抓取测试中，达到了 **90.8%** 的聚合成功率，远超现有基线方法。
*   **设计有效性验证**： 消融实验证明，对“域不变表征”进行模仿学习是成功泛化的关键，其单物体抓取成功率（98.6%）显著优于从原始输入直接学习的变体（高出48%以上）。
*   **内部行为一致性**： 可视化和经验分析证实，尽管输入图像因环境变化而差异巨大，但模型内部的 DINOv2 特征、物体掩码及扩散模型的注意力图都保持高度一致，始终聚焦于目标任务，从而揭示了其鲁棒性的内在机理。
*   **通用性证明**： 框架首次同时展示了处理长时域自由提示、对抗性物体、人为干扰下的鲁棒恢复，并能直接扩展到如非抓握式抓取等新操作任务，证明了其作为通用框架的潜力。

### 7. 优点

*   **结合优势，解决核心矛盾**： 巧妙地通过分层设计，将基础模型的泛化知识与模仿学习的鲁棒闭环动作生成能力结合起来，直接解决了模仿学习的泛化瓶颈。
*   **“域不变表征”的深刻洞察**： 提出并实践了“迭代转换到域不变空间”这一清晰且有效的设计原则，其效果得到了充分的实验验证和可视化分析，具有很强的启发性。
*   **全面的实证评估**： 实验设计严谨、规模庞大（上千个零样本测试场景），覆盖了从定量对比到定性分析的完整链条，结论极具说服力。
*   **高通用性和鲁棒性**： 框架展现了对新任务（非抓握式抓取）的良好扩展性，并展示了面对干扰和复杂指令时的强大鲁棒性，更贴近真实应用需求。

### 8. 不足与局限

*   **算力与效率未明**： 论文未提供模型训练的计算资源需求、训练时长和推理速度的具体数据，这为评估其实时性和部署成本带来了不确定性。
*   **任务功能局限**： 虽然名为通用框架，但所展示的能力仅限于“抓取”这一动作，尚未扩展到功能性的目标导向操作（如拧开瓶盖、使用工具等）。
*   **感知模态不完整**： 系统完全依赖视觉，缺乏触觉反馈。对于需要精细力控的抓取任务，这可能是一个根本性缺陷。
*   **高层规划器能力依赖**： 整个系统的性能上限受限于所采用的预训练 VLM 的能力，VLM 在复杂场景下的推理错误会直接导致任务失败。
*   **数据依赖**： 尽管所需的演示数据量相对少，但仍需要为每个新技能（如非抓握式抓取）收集专门的专家演示，未能实现零样本的策略迁移。

（完）
