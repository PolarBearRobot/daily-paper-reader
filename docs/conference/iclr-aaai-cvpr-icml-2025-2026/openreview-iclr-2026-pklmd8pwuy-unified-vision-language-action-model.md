---
title: Unified Vision-Language-Action Model
title_zh: 统一视觉-语言-动作模型
authors: "Yuqi Wang, Xinghang Li, Wenxuan Wang, Junbo Zhang, Yingyan Li, Yuntao Chen, Xinlong Wang, Zhaoxiang Zhang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=PklMD8PwUy"
tags: ["query:model"]
score: 9.0
evidence: 集成了自回归视觉-语言-动作及世界模型的统一 VLA 模型
tldr: UniVLA 提出一个统一的原生多模态 VLA 模型，将视觉、语言、动作信号作为离散 token 序列自回归建模，并融入世界模型提供生成式视觉监督，从而提升视觉理解与操作能力，支持灵活的多任务学习。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有 VLA 忽略视觉观测的时序因果结构。
method: 自回归 token 序列建模，结合世界模型提供生成监督。
result: 增强视觉理解，提升操作性能。
conclusion: 统一多模态 token 化与世界模型有助于进阶 VLA。
---

## Abstract
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation.
However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This tokenized formulation naturally supports flexible multimodal task learning, particularly from large-scale video data, and further demonstrates that generative vision supervision can significantly enhance visual understanding. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning—especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, substantially outperforming prior methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing π₀-FAST's 85.5%. We further demonstrate its broad applicability through experiments on real-world ALOHA manipulation tasks and autonomous driving scenarios.

---

## 论文详细总结（自动生成）

# 论文总结：UniVLA – 统一视觉-语言-动作模型

## 1. 论文的核心问题与整体含义

- **研究背景**：视觉-语言-动作模型（VLA）在机器人操作领域展现出巨大潜力。现有方法多依赖视觉-语言模型（VLM）的通用理解能力来生成动作信号，但往往忽略视觉观测中蕴含的丰富时间序列和因果结构。
- **核心问题**：如何更充分地利用视觉观测的时序因果信息，并将其与语言指令、动作信号在统一框架下建模，从而提升机器人的操作能力，尤其是长程任务的效果。
- **整体含义**：UniVLA提出一种原生的多模态统一模型架构，将视觉、语言、动作统一为离散token序列进行自回归建模，并融入世界模型提供生成式视觉监督，增强模型对动态变化的理解，为VLA模型的设计提供了新的范式。

## 2. 论文提出的方法论

### 2.1 核心思想
- **统一多模态token化**：将视觉、语言、动作信号均转换为离散token序列，在统一的序列建模框架下进行自回归生成。
- **世界模型融入**：在后训练阶段引入世界模型，从视频数据中捕捉因果动态，利用生成式视觉监督（预测未来帧）来加强视觉理解，并以此为下游策略学习提供更好的迁移能力。

### 2.2 关键技术细节
- **离散token序列建模**：视觉输入（图像或视频帧）通过离散化模块编码为视觉token；语言指令同样转换为语言token；动作信号则离散化为动作token。这些token拼接为单一序列，由Transformer架构以自回归方式逐token预测。
- **多任务学习**：该token化形式天然支持灵活的多模态任务学习，尤其可大规模利用视频数据进行训练。
- **世界模型后训练**：利用视频预测目标（生成下一帧的视觉token）来训练模型理解环境动态，这一监督信号有效提升了模型对视觉场景的因果推理能力，从而增强策略学习。
- **下游策略迁移**：经过世界模型增强的UniVLA ，再针对具体操作任务进行策略微调，特别是在长程任务上表现出显著改善。

### 2.3 算法流程（文字描述）
1. **数据预处理**：视觉、语言、动作数据分别离散化为token序列。
2. **预训练/联合训练**：模型以自回归方式在混合数据（可能包括纯视频、图文、机器人数据）上训练，预测下一个token。
3. **世界模型后训练**：在视频数据上强化模型预测未来视觉token的能力。
4. **策略微调**：在机器人操作数据集上微调，模型根据当前观测（视觉+语言）自回归生成动作token序列。

## 3. 实验设计

- **仿真Benchmark数据集**：
  - CALVIN（基于语言引导的长程操作任务）
  - LIBERO（多任务、长时间操作基准）
  - Simplenv-Bridge（另一模拟环境，常用于操作策略评估）
- **真实世界实验**：
  - ALOHA双臂操作任务（高精度、真实环境操作）
  - 自动驾驶场景（验证模型泛化能力）
- **对比方法**：文中提到了与 π₀-FAST 对比，在LIBERO基准上 UniVLA 平均成功率达95.5%，显著超过 π₀-FAST 的85.5%。可能还包括其他SOTA VLA方法（摘要未详细列出）。
- **评估指标**：平均任务成功率（主要指标）。

## 4. 资源与算力

- **文中未明确说明**：从摘要和元数据中未找到GPU型号、数量、训练时长等具体算力信息。完整论文可能包含实验设置章节，但根据提供内容无法得知。

## 5. 实验数量与充分性

- **实验维度**：从描述看，至少包含：
  - 3个模拟基准上的主实验（CALVIN, LIBERO, Simplenv-Bridge）
  - 至少1组真实世界ALOHA实验
  - 自动驾驶验证实验
  - 可能包括消融实验（如世界模型的效果、不同token化方式等），摘要未展开细节。
- **充分性与公平性**：
  - 覆盖多种环境（模拟到真实、操作到驾驶），具有一定广度。
  - 设定新的SOTA并与现有强基线（π₀-FAST）比较，体现公平性。
  - 由于看不到完整论文，无法判断统计显著性、误差线、超参搜索等细节，但表面上看实验设计合理、客观。

## 6. 论文的主要结论与发现

- **统一模型有效**：将视觉、语言、动作统一为离散token序列并进行自回归建模，能够有效利用视觉时序信息，提升多模态任务性能。
- **世界模型增强视觉理解**：通过世界模型提供的生成式视觉监督，模型更好地捕捉环境因果动态，显著加强了视觉表征，尤其有益于长程任务。
- **性能领先**：在多个仿真基准（尤其是LIBERO）上显著超越此前最优模型，并成功泛化到真实世界操作和自动驾驶任务。

## 7. 优点

- **方法创新**：首次在VLA中将视觉、语言、动作统一为离散token流，并原生集成了世界模型，提供了简洁而强大的框架。
- **对视觉时序的利用**：弥补了现有VLA忽略时序因果结构的缺陷，使模型能够预测未来帧并从中学习动态规律。
- **灵活的多任务学习**：离散token序列结构天然支持多种类型数据混合训练，便于扩展至大规模视频预训练。
- **实验结果强劲**：在多个基准上达到SOTA，且展现了从仿真到真实、从操作到驾驶的广泛迁移能力。

## 8. 不足与局限

- **算力需求不明**：未提供算力信息，难以评估实际训练成本。
- **数据集选择局限**：实验集中在特定的仿真和真实平台（CALVIN, LIBERO, ALOHA），在其他更具多样性的真实环境中的泛化性未验证。
- **真实世界实验规模**：真实世界评估（ALOHA、自动驾驶）可能任务数量和尝试次数有限，结论的统计可靠性待进一步验证。
- **方法的内在局限**：离散token化可能引入量化误差，对精细运动控制的影响未讨论；世界模型预测的视觉 token可能在复杂动态中不够准确。
- **缺少消融实验细节**：摘要未展示世界模型剔除、不同token化粒度等关键消融结果，无法判断各组件贡献度。
- **潜在偏差**：预训练数据分布若偏向仿真或特定场景，可能导致机器人策略在实际部署时出现偏差。

（完）
