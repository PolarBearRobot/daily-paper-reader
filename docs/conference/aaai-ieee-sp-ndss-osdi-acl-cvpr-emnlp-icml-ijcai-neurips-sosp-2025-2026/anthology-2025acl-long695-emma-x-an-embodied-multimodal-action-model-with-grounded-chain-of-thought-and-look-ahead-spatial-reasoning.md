---
title: "Emma-X: An Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning"
title_zh: 具有接地链式思维与前瞻空间推理的具身多模态动作模型
authors: "Qi Sun, Pengfei Hong, Tej Deep Pala, Vernon Toh, U-Xuan Tan, Deepanway Ghosal, Soujanya Poria"
date: 2025-07-01
pdf: "https://aclanthology.org/2025.acl-long.695.pdf"
tags: ["query:model"]
score: 9.0
evidence: 提出具有空间推理与规划的VLA模型
tldr: 现有VLA模型在长程空间推理与接地任务规划中面临挑战。本文提出EMMA-X，通过引入基于链式思维的推理与前瞻空间推理增强VLA模型，并构建层次化具身数据集。实验表明该方法提升了多环境下的长程操作能力，为通用机器人动作生成提供了更有效的时空推理机制。
source: ACL-2025-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2025-long/anthology-2025.acl-long.695/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 795, \"height\": 802, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2025-long/anthology-2025.acl-long.695/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1639, \"height\": 628, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2025-long/anthology-2025.acl-long.695/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 803, \"height\": 963, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2025-long/anthology-2025.acl-long.695/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 774, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2025-long/anthology-2025.acl-long.695/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1632, \"height\": 615, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1636, \"height\": 623, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 793, \"height\": 307, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1662, \"height\": 764, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1654, \"height\": 632, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1550, \"height\": 974, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1474, \"height\": 1379, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2025-long/anthology-2025.acl-long.695/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1468, \"height\": 828, \"label\": \"Table\"}]"
motivation: 传统VLA模型缺乏长程空间推理与接地规划能力。
method: 引入链式思维推理与前瞻空间推理，构建层次化具身数据集。
result: 在多环境长程操作任务中提升了策略泛化性与空间推理性能。
conclusion: EMMA-X显著增强了VLA模型的推理与规划能力，缩小了从感知到动作的差距。
---

## Abstract
Traditional reinforcement learning-based robotic control methods are often task-specific and fail to generalize across diverse environments or unseen objects and instructions. Visual Language Models (VLMs) demonstrate strong scene understanding and planning capabilities but lack the ability to generate actionable policies tailored to specific robotic embodiments. To address this, Visual-Language-Action (VLA) models have emerged, yet they face challenges in long-horizon spatial reasoning and grounded task planning. In this work, we propose the Embodied Multimodal Action Model with Grounded Chain of Thought and Look-ahead Spatial Reasoning, EMMA-X. EMMA-X leverages our constructed hierarchical embodiment dataset based on BridgeV2, containing 60,000 robot manipulation trajectories auto-annotated with grounded task reasoning and spatial guidance. Additionally, we introduce a trajectory segmentation strategy based on gripper states and motion trajectories, which can help mitigate hallucination in grounding subtask reasoning generation. Experimental results demonstrate that EMMA-X achieves superior performance over competitive baselines, particularly in real-world robotic tasks requiring spatial reasoning.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：传统强化学习（RL）方法高度任务特定，难以泛化到新环境、新物体或新指令。视觉语言模型（VLM）虽具备强大的场景理解与任务规划能力，却无法直接产出适配特定机器人本体的可执行动作策略。
- **现有方法的不足**：视觉‑语言‑动作（VLA）模型（如OpenVLA）在一定程度上弥补了上述差距，但在处理需要长时程空间推理和接地任务规划的场景时仍力不从心。以ECoT为代表的已有工作尝试引入思维链推理，但其推理过程仅依赖文本描述，缺乏视觉场景信息的充分接地，容易出现幻觉，且缺少对末端执行器未来空间状态的预测。
- **本文动机与整体含义**：为了让VLA模型不仅能理解当前场景，还能像人类一样“预测未来状态并规划空间路径”，论文提出具身多模态动作模型EMMA‑X。它通过引入**接地链式思维（Grounded CoT）**与**前瞻空间推理**，显著增强了模型在复杂、长期任务中的泛化与空间推理能力。

## 2. 论文提出的方法论

### 2.1 核心思想
以OpenVLA为基础，通过向训练数据中注入层次化的接地推理信息，使模型在预测动作之前先完成：
- **子任务分解与接地推理**（结合视觉输入，给出当前子任务及其理由）；
- **前瞻空间推理**（预测下一子任务段起始时的2D夹爪位置，以及从当前位形到该位置的3D运动计划）。

### 2.2 关键技术细节

- **轨迹分割策略**
  - 同时利用**末端执行器运动轨迹**与**夹爪开闭状态**进行分割。
  - 定义加权距离度量：  
    `d(i, j) = ∥pᵢ − pⱼ∥₂ + λ∥rᵢ − rⱼ∥₂ + β|tᵢ − tⱼ|`  
    其中`p`为3D位置，`r`为3D朝向，`t`为时间戳，λ=1、β=0.03。
  - 采用HDBSCAN算法对轨迹聚类；同时，当相邻数据点的夹爪状态发生改变（`gsᵢ ≠ gs₊₁`）时，立即产生新的分割点。最终每段内机器人执行语义相近的动作。
  - 输出段序列：`Σι = {σ₁, σ₂, …, σₙ}`。

- **层次化具身数据生成**（基于BridgeV2的6万条轨迹）
  - **接地任务推理**：将每一段的图像序列、任务描述送入Gemini（gemini‑1.5‑pro‑latest），生成该段对应的**子任务标签**与**场景理由**。视觉输入的加入有效缓解了纯文本推理的幻觉问题。
  - **前瞻2D夹爪位置**：使用OWLv2 + SAM检测每一段第一个状态中的夹爪2D位置，作为当前段训练时的目标预测值（即“下一段起始位置”）。
  - **前瞻3D运动计划**：计算当前状态与段末状态之间的3D位移，并转换为规范化的自然语言模板（如“向前移动22步，向右移动32步，向下移动142步”）。
  - 最终每个轨迹的数据形式为：`{ (sₜ, T), (mₜ, gₜ, GRₜ, aₜ) }ₜ₌₁ᵀ`。

- **模型架构与训练**
  - 基座模型：**OpenVLA**（7B参数的VLA模型，基于Prismatic VLM，在Open X‑Embodiment数据集上预训练）。
  - 输入：任务指令、当前观测图像、实时检测到的2D夹爪位置（推理时由SAM提供）。
  - 输出：**先**生成子任务、场景描述、未来2D夹爪位置、3D运动计划，**再**生成7维动作（x,y,z速度；roll,pitch,yaw；夹爪开闭）。
  - 训练方式：将连续动作离散化为token，以自回归方式微调（next‑token prediction，交叉熵损失），batch size=64，训练9个epoch至收敛。

## 3. 实验设计

- **机器人平台与场景**：6自由度WidowX机器人臂，单视角第三摄像头，真实世界环境。任务涵盖四类：
  - **空间关系**（如“将胡萝卜的上半部分放入锅”）
  - **分布外物体（OOD Object）**（如“将香蕉放入锅”）
  - **分布外指令（OOD Instruction）**（如“拿起任一种蔬菜”）
  - **域内任务**（如“打开微波炉”）
- **评价指标**：成功率（`Succ`）与半成功率（`h_Succ`，按难度分0.5分），每类任务进行10次回放。
- **对比基线**：
  - **OpenVLA**：原始预训练模型。
  - **OpenVLA w/ FT**：在BridgeV2上使用相同设置直接微调的OpenVLA。
  - **ECoT**：由Zawalski等人提出的、基于OpenVLA微调并加入文本CoT推理的VLA模型。
- **消融实验**：为验证各组件贡献，还训练了以下变体（在6项代表性任务上评估）：
  - 移除HDBSCAN分割（仅靠夹爪开断分割）
  - 移除未来夹爪位置预测（`w/o gₜ`）
  - 移除3D运动计划（`w/o mₜ`）
  - 移除接地CoT推理（`w/o GRₜ`）
  - 直接微调OpenVLA（`w/ FT`）

## 4. 资源与算力

- 论文**未明确披露**所使用GPU的具体型号、数量以及训练总时长。
- 唯一提及的计算相关信息是：采用较小的批处理大小（batch size=64）以适应硬件条件，并在BridgeV2增强数据集上对7B参数的OpenVLA微调9个epoch。由于缺少详细的算力说明，无法评估其训练开销与可复现性。

## 5. 实验数量与充分性

- **主实验**：12项真实机器人任务，3种方法对比，每个任务10次重复，产生足够样本。
- **消融与分析实验**：在6项子集任务上比较了5种变体，清晰验证了分割、前瞻位置、运动计划、接地推理等关键设计的必要性。
- **定性分析**：展示了成功与失败案例，佐证推理内容与实际行为的一致性。
- **公平性**：所有模型在相同的硬件、灯光、背景与指令下测试，基线中包含了直接微调OpenVLA的对比，排除了“微调本身即带来提升”的干扰。任务设置涵盖了域内、物体泛化、空间理解、指令泛化等多个维度。整体实验设计和数量较为充分，能够支撑论文结论。

## 6. 论文的主要结论与发现

- EMMA‑X在成功率上较OpenVLA提升**24.17%**，半成功率提升**26.25%**；较ECoT有更加显著的领先。
- 在**空间关系**任务中，EMMA‑X的h_Succ率高出OpenVLA 35%，高出ECoT 29%，充分证实了前瞻空间推理的有效性。
- 消融实验表明：**接地CoT推理**贡献最大（移除后性能下降43‑55%），其次是**前瞻夹爪位置**和**运动计划**；基于HDBSCAN的运动轨迹分割对空间推理至关重要（移除后空间推理指标骤降50%）。
- 直接微调OpenVLA会导致性能退化（过拟合），说明BridgeV2已在其预训练中覆盖，单纯微调无法带来增益。
- 定性分析显示，接地且前瞻的推理能够引导机器人执行正确的子任务，但物体识别错误（如将热狗误认为菠萝）仍会导致失败。

## 7. 优点

- **创新性强**：首次将接地视觉CoT与前瞻2D/3D空间推理同时引入VLA训练，填补了现有模型在长程空间规划上的短板。
- **数据集构建巧妙**：提出的轨迹分割方法（融合运动与夹爪状态）有效降低了Gemini在生成子任务推理时的幻觉，且大幅提升了推理的准确性。
- **实验验证扎实**：在真实机器人上测试了12项泛化任务，并通过详尽的消融实验证明了每个模块的独立贡献。
- **开源友好**：作者承诺公开代码、模型与数据集，利于后续研究复现与拓展。
- **与基座模型无缝结合**：以OpenVLA为底座微调，方法可以兼容未来更强的基础VLM。

## 8. 不足与局限

- **推理延迟**：模型生成长达10倍于OpenVLA的token，导致控制延迟明显，限制了其在高速动态场景中的应用。论文仅提出了“预测整段动作”的缓解思路，未实现。
- **物体检测依赖**：推理时需用SAM实时检测夹爪2D位置，当夹爪被遮挡或超出画面时会出现检测失败，影响可靠性。
- **泛化边界有限**：实验平台为单一WidowX臂，且仅在BridgeV2和小规模真实任务上验证，尚未展示在更多样化的机器人本体或大规模OXE子集上的能力。
- **基线比较范围较窄**：未与Octo、RT‑2‑X、LLaRA等更具代表性的最新VLA方法对比；ECoT作为主要的CoT基线，其表现较差可能受限于其原始的标注质量，但不排除其他CoT方法能取得更好效果。
- **标注偏差风险**：层次化推理数据由Gemini自动生成，虽通过视觉输入降低了幻觉，但仍可能携带预训练模型的内在偏差，在特殊场景下可能输出不合理的推理。

（完）
