---
title: "Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation"
title_zh: 指令增强的长时域规划：在具身移动操作中嵌入接地机制
authors: "Fangyuan Wang, Shipeng Lyu, Peng Zhou, Anqing Duan, Guodong Guo, David Navarro-Alarcon"
date: 2025-04-11
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/33610/35765"
tags: ["query:model"]
score: 8.0
evidence: 面向具身移动操作的长时域规划，结合接地机制以定量理解环境
tldr: 针对人形机器人在真实环境中进行长时域移动操作规划的挑战，现有LLM规划器缺乏环境定量理解。IALP系统将接地机制嵌入LLM规划中，使机器人能定量判断物体可操作性，实现指令增强的长时域规划。实验验证了该方法在复杂移动操作任务中的有效性，提升了机器人对物理世界的真实感知能力。
source: AAAI-2025-Accepted
selection_source: conference_retrieval
motivation: 现有LLM规划器依赖文本描述，无法定量评估环境中的物体可操作性。
method: 提出IALP系统，在LLM规划中嵌入接地机制，实现定量环境理解与指令增强规划。
result: IALP使机器人成功执行长时域移动操作，定量判断提高了任务成功率。
conclusion: IALP为具身智能体提供了与环境接地的高级规划，缩小了语言与物理世界的鸿沟。
---

## Abstract
Enabling humanoid robots to perform long-horizon mobile manipulation planning in real-world environments based on embodied perception and comprehension abilities has been a longstanding challenge. With the recent rise of large language models (LLMs), there has been a notable increase in the development of LLM-based planners. These approaches either utilize human-provided textual representations of the real world or heavily depend on prompt engineering to extract such representations, lacking the capability to quantitatively understand the environment, such as determining the feasibility of manipulating objects. To address these limitations, we present the Instruction-Augmented Long-Horizon Planning (IALP) system, a novel framework that employs LLMs to generate feasible and optimal actions based on real-time sensor feedback, including grounded knowledge of the environment, in a closed-loop interaction. Distinct from prior works, our approach augments user instructions into PDDL problems by leveraging both the abstract reasoning capabilities of LLMs and grounding mechanisms. By conducting various real-world long-horizon tasks, each consisting of seven distinct manipulatory skills, our results demonstrate that the IALP system can efficiently solve these tasks with an average success rate exceeding 80%. Our proposed method can operate as a high-level planner, equipping robots with substantial autonomy in unstructured environments through the utilization of multi-modal sensor inputs.

---

## 论文详细总结（自动生成）

# 论文总结：Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：人形机器人在真实世界中执行长时域移动操作规划时，如何从具身感知中获取并利用环境的接地知识，从而生成可行且最优的动作序列。
- **研究背景**：现有基于大语言模型（LLM）的规划器大多依赖人工提供的文本环境描述或通过提示工程提取2D图像中的信息，缺乏对环境的**定量理解**（例如物体抓取可行性、三维空间中的可达性），导致在非结构化真实环境中自主性不足。
- **整体含义**：提出一种将**接地机制**嵌入LLM规划闭环的方法，让人工指令增强为含有真实世界定量约束的规划问题，使机器人能够可靠地完成包含导航与操作的长序列任务。

## 2. 方法论（核心思想与技术细节）
- **核心框架**：指令增强长时域规划系统 IALP，结合LLM的抽象推理能力和接地机制的定量感知，将用户指令转化为**PDDL问题**，并以闭环方式生成和选择动作。
- **关键技术流程**：
  1. **指令增强**：利用LLM从自然语言指令中提取任务相关对象，并结合相机获得的2D/3D数据，通过两类谓词构建当前状态和目标的PDDL描述。
     - **可提示谓词**（Promptable）：如 `on`、`holding`、`opened`，由LLM直接判断。
     - **接地机制谓词**（Grounding Mechanism-based）：如 `find`（路径是否存在）、`at`（到达位置）、`graspable`（抓取位姿可行性）、`reachable`（末端可达性），通过Voxel Map、LangSAM、GraspNet、可达性地图等定量计算。
  2. **可行性判断**：每次规划时评估动作的物理可行性（导航路径存在、目标检测成功、抓取位姿和放置空间合理、机器人可达），若条件不满足则直接避免无效动作。
  3. **最优性选择**：LLM规划器在给定PDDL域和问题后生成 K 个候选动作，计算每个动作的**token对数概率**作为最优性得分，选得分最高者执行，实现语言模型视角下的最优规划。
  4. **闭环交互**：每执行一个动作后重新观测状态，重建PDDL问题再规划，形成“感知-规划-执行-反馈”闭环。
- **公式化目标**：最大化动作序列同时满足指令（最优性得分）且物理可执行（可行性得分）的联合概率。可行性得分确保奖励均为1，任一动作失败即整条序列失败。

## 3. 实验设计
- **实验场景**：真实室内环境（单个房间），使用Tiago++移动机器人（轮式底座、双臂7自由度、头部RGB-D相机）。
- **任务**：5个长时域任务，每个包含7种不同操作技能：
  - Place box（拾取纸箱放置到另一桌子）
  - Take jacket（从衣架取蓝夹克送至门口）
  - Take pillbox（从抽屉取药盒）
  - Insert book（从黑桌取书插入书架）
  - Lift bucket（提起蓝桶放到白桌）
- **对比基线**：
  - IALP 完整系统
  - IALP 无可行性反馈（移除接地谓词）
  - IALP 无最优选择（不按token概率选动作）
- **评估指标**：成功率（生成可执行动作的比例）、各阶段耗时、失败类型分析。

## 4. 资源与算力
- 文中未提及训练过程，方法主要基于预训练基础模型和传统算法，**无明确GPU算力（型号、数量、训练时长）说明**。
- 高层规划使用 **GPT‑4o** API。
- 硬件方面使用三台计算机：一台用于机器人ROS控制，其余用于感知反馈计算。

## 5. 实验数量与充分性
- **实验规模**：
  - 每个任务进行20次真实世界试验（共100次）。
  - 消融实验为每个任务随机生成20组观测（谓词随机设为True/False），评估规划器能否生成正确动作。
  - 记录了单次成功执行的导航、操作和规划时间。
- **充分性**：
  - 涵盖多种技能组合，在真实硬件上验证闭环性能，并开展系统的消融研究，实验设计较为合理。
  - 但场景仅限单一室内环境，机器人初始状态固定，任务种类有限，泛化性探索不够充分。

## 6. 主要结论与发现
- IALP 在所有长时域任务中成功率超过 **80%**。
- 接地机制（可行性反馈）的移除会导致成功率大幅下降，表明定量理解环境对生成可行动作至关重要。
- 最优选择机制在可行性被保障的前提下能进一步提升成功率。
- 失败主要来源于规划错误、可提示谓词误判和接地机制谓词输出错误（如抓取位姿不准），其中接地机制错误在真实硬件实验中占比不容忽视。

## 7. 优点
- **定量接地**：首次将多源接地谓词形式化地融入PDDL问题，使LLM规划器能直接利用三维空间和物理约束。
- **训练零代价**：完全基于预训练模型和经典算法（如A*、GraspNet、可达性分析），无需额外训练。
- **闭环自适应**：每步重新感知和规划，可应对实际执行中的不确定性和部分失败。
- **模块化可扩展**：谓词库和技能库均设计为可扩展，便于添加新能力。

## 8. 不足与局限
- **场景单一**：仅在室内单个房间测试，未验证动态或杂乱环境下的鲁棒性。
- **依赖预定义技能**：技能库需手动设计，限制了对开放指令的泛化。
- **接地机制不够鲁棒**：仍存在抓取检测、可达性判断等模块的失败，影响总体可靠性。
- **时间效率**：长序列任务耗时较长（单次成功执行需几分钟），未进行实时性优化。
- **对比不充分**：仅与自身消融版本比较，缺少与其它最新训练自由或基于LLM的移动操作规划器的直接对比。

（完）
