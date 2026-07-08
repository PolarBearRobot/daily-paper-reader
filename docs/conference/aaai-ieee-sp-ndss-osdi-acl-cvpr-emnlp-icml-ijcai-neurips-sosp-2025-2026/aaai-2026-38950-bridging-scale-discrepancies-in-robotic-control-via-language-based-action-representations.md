---
title: Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations
title_zh: 通过基于语言的动作表示弥合机器人控制中的尺度差异
authors: "Yuchi Zhang, Churui Sun, Shiqi Liang, Diyuan Liu, Chao Ji, Weinan Zhang, Ting Liu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38950/42912"
tags: ["query:analysis"]
score: 9.0
evidence: 基于语言的动作表示归一化尺度差异，实现鲁棒操作
tldr: 针对跨机器人平台和任务中动作数据数值尺度差异导致的分布偏移问题，提出一种基于语义的动作语言表示，忽略数值尺度而强调方向相似性。该表示归一化了动作命令，使得预训练知识能够有效迁移，在多种操作任务上展示了鲁棒的泛化能力，为机器人动作标准化表示提供了新方案。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38950/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1844, \"height\": 476, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38950/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1391, \"height\": 725, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38950/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 873, \"height\": 732, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 864, \"height\": 409, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 817, \"height\": 383, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 864, \"height\": 380, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 787, \"height\": 384, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 768, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 765, \"height\": 434, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38950/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 856, \"height\": 472, \"label\": \"Table\"}]"
motivation: 不同机器人动作数值尺度差异大，阻碍预训练知识迁移。
method: 提出语言化的动作表示，忽略数值尺度，强调方向相似性。
result: 实现了跨平台和任务的鲁棒操作，泛化性能显著提升。
conclusion: 语义动作表示有效解决了尺度偏移问题，促进了机器人学习。
---

## Abstract
Recent end-to-end robotic manipulation research increasingly adopts architectures inspired by large language models to enable robust manipulation. However, a critical challenge arises from severe distribution shifts between robotic action data, primarily due to substantial numerical variations in action commands across diverse robotic platforms and tasks, hindering the effective transfer of pretrained knowledge. To address this limitation, we propose a semantically grounded linguistic representation to normalize actions for efficient pretraining. Unlike conventional discretized action representations that are sensitive to numerical scales, the motion representation specifically disregards numeric scale effects, emphasizing directionality instead. This abstraction mitigates distribution shifts, yielding a more generalizable pretraining representation. Moreover, using the motion representation narrows the feature distance between action tokens and standard vocabulary tokens, mitigating modality gaps. Multi-task experiments on two benchmarks demonstrate that the proposed method significantly improves generalization performance and transferability in robotic manipulation tasks.

---

## 论文详细总结（自动生成）

好的，以下是对这篇论文的结构化总结。

### 1. 论文的核心问题与整体含义
- **核心问题**：在端到端机器人操作中，不同机器人平台和任务采集的动作数据存在严重的**数值尺度分布偏移**（如执行器位移范围、采样频率差异），这导致在通用数据集上预训练的知识难以有效迁移到下游任务，极大限制了模型泛化能力。
- **整体含义**：提出一种**基于语义的动作语言化表示**（称为 motion），将数值型的动作命令转化为忽略具体数值尺度、只强调方向性的粗糙语言描述，以此作为预训练的归一化中间目标。这种方法弥合了跨数据集的分布鸿沟，使得模型能够学习到更通用、可迁移的运动模式，最终提升多任务操作的成功率和鲁棒性。

### 2. 论文提出的方法论
#### 2.1 核心思想
- 利用**规则映射**将连续动作空间转换为粗粒度、固定结构的自然语言描述，作为预训练阶段的监督信号，以屏蔽底层数值差异，提取通用的运动方向特征。
- 采用**两阶段训练**：先在海量数据上学习从视觉和指令到运动语言的映射，再在下游数据上同时预测运动语言和精细动作，实现知识迁移。

#### 2.2 关键技术细节
- **动作分词器**：将7维动作（ΔX, ΔY, ΔZ, Δroll, Δpitch, Δyaw, 夹爪状态）归一化到256个bins，映射为模型词表中新增的256个特殊 token。
- **运动生成**：
  - **表示形式**：固定句式的语言描述，如 `move [forward/backward] [left/right] [up/down]`，`tilt [up/down]`，`rotate [clockwise/counterclockwise]`，`[open/close] gripper`，无运动则为 `stop`。
  - **自适应阈值**：引入速度校正补偿高速运动下的抖动，公式为：
    \[
    T_i(t) = T_i^{\text{base}} + \beta \cdot \frac{1}{\tau} \sum_{s=t-\tau}^{t} |\hat{\Delta}_i(s)|
    \]
  - **分层时间窗口**：设计快、中、慢三种分辨率的运动检测器，分别关注快速突变、持续运动和缓慢同向变化，三者取逻辑或生成最终运动标记，有效抑制错误分割。
- **两阶段训练**：
  - **预训练**：输入为系统提示、用户指令和视频帧，模型仅预测运动 token；格式类似 VLM 微调。
  - **微调**：在预训练基础上，增加预测精细动作 token，运动 token 作为上下文辅助，类似课程学习先易后难。

### 3. 实验设计
- **数据集与基准**：
  - **预训练**：从 Open X-Embodiment 选取7个子集（约12,000条轨迹），生成运动数据。
  - **微调与评估**：
    - **LIBERO基准**：包含130+个语言条件操作任务，评测 **Spatial, Object, Goal, Long** 四个子套件的成功率。
    - **SimplerEnv基准**：基于 Bridge V2 数据集的仿真环境，评测 **Place spoon on towel, Place carrot on plate, Stack green on yellow block, Place eggplant in basket** 四个任务。
- **对比方法**：Diffusion Policy, ScaleDP, Octo, OpenVLA, RT-1-x, ECoT。此外，还进行从头训练与预训练、有无运动 token、有无运动生成优化的消融对比。

### 4. 资源与算力
- 论文明确指出所有实验在 **A100-80G** GPU 上运行。
- 预训练 batch size 为 2048，微调为 512，学习率 \(2\times10^{-5}\)。
- **未提及**具体使用的 GPU 数量以及各阶段完整训练时长，仅注明详细计算效率分析可参考附录 C（本摘录未包含）。

### 5. 实验数量与充分性
- 实验覆盖较为全面：
  - 三种模型尺寸（0.5B, 1.5B, 3B）× 两种训练范式（从头训练 vs. 预训练后微调）× 两个下游基准 × 若干变体（有无运动、有无优化）。
  - 与6个主流基线方法进行比较。
  - 对运动生成的质量改善进行了单独消融（原始固定阈值窗口 vs. 优化方法 vs. 无运动）。
  - 通过 PCA 和置信椭圆可视化了有无运动预训练对动作 token 与语言 token 特征距离的影响。
- 总体实验量较大，对比公平，消融设计合理，能够有效支撑论文主张。但仅在两个仿真基准上评估，且 SimplerEnv 中存在所有模型全部失败的极端任务。

### 6. 论文的主要结论与发现
- 基于语言的运动表示能有效**弥合不同机器人平台的数值尺度差异**，预训练知识迁移效果显著优于直接使用原始动作 token。
- 所提的自适应阈值和分层窗口机制**显著提升了运动生成的准确性与鲁棒性**（人工标注准确率从57.62%提升至86.37%）。
- 引入运动预测目标可以**缩小动作 token 与语言 token 的特征空间距离**，缓解模态差异，使训练更高效、表征更聚集。
- 在 LIBERO 和 SimplerEnv 上，该方法以较小的模型规模和预训练数据取得有竞争力的结果，其中 3B 模型在 LIBERO 上平均成功率达到 78.1%。

### 7. 优点
- **思维创新**：巧妙利用粗粒度语言描述作为「中间归一化层」，将分布偏移严重的数值信号转化为语义信号，简单且可解释性强。
- **无需昂贵标注**：运动生成完全基于规则自动完成，不依赖人工校正或外部语言模型，成本低、易扩展。
- **训练高效**：课程式两阶段训练符合直觉，在小模型上即可获得明显提升，算力需求相对较低。
- **实验扎实**：多尺度消融、可视化分析和多基准对比完整，充分论证了方法的有效性。

### 8. 不足与局限
- **规则依赖**：运动生成依赖于手工设计的阈值和窗口，可能需要针对新型机器人进行人工调整，泛化到未见动作模式的灵活性受限。
- **精细操作能力有限**：在需要极高精度的堆叠任务上表现不佳（SimplerEnv stack block 成功率为 0），且模型性能在模拟仿真与真实数据之间存在差距。
- **预训练数据规模较小**：仅使用了 OXE 的7个子集，未探索更大规模数据下的 scaling 效果。
- **未在真实机器人验证**：所有评估均在仿真环境中完成，缺少真实世界的部署测试。
- **模型规模上限低**：最大模型仅 3B 参数，与当前 7B 甚至更大参数量的 VLA 模型相比，绝对上限可能受限。

（完）
