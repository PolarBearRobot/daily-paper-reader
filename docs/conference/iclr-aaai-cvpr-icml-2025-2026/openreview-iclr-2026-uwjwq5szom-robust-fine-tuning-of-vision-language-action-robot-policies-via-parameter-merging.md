---
title: Robust Fine-tuning of Vision-Language-Action Robot Policies via Parameter Merging
title_zh: 通过参数合并实现视觉-语言-动作机器人策略的稳健微调
authors: "Yajat Yadav, Zhiyuan Zhou, Andrew Wagenmaker, Karl Pertsch, Sergey Levine"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=uWJwQ5SZoM"
tags: ["query:model"]
score: 9.0
evidence: 通过参数合并稳健微调VLA机器人策略，保持泛化能力。
tldr: 通用VLA策略在新任务上少量微调时易过拟合且遗忘旧技能，本文提出一种参数合并方法，在引入新技能的同时保留策略原有的广泛泛化能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 通用VLA策略在新任务微调时容易遗忘旧技能并在新任务内泛化不足。
method: 提出一种参数合并技术，将预训练策略与微调后策略的参数进行合并，以减少灾难性遗忘。
result: 在多个机器人操作任务上验证，合并后的策略既学会了新技能又保持了原有多任务能力。
conclusion: 参数合并是一种简单有效的方法，使VLA策略在增量学习新技能时保持稳健。
---

## Abstract
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations---not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

---

## 论文详细总结（自动生成）

# 论文总结：通过参数合并实现视觉-语言-动作机器人策略的稳健微调

## 1. 论文的核心问题与整体含义
通用机器人策略（Vision-Language-Action, VLA）在海量多源数据预训练后，展现了对各类行为和环境的广泛泛化能力。然而，当面对训练数据未覆盖的新任务时，需要进行微调。传统的少量示范微调容易导致：
- **灾难性遗忘**：策略丧失预训练获得的多种通用技能；
- **新任务内泛化不足**：过度拟合微调示范，无法泛化到同一任务的不同变体。

该工作的核心动机是：**在引入新技能的同时，彻底保留通用策略原有的泛化能力**，让单一模型既能稳健地解决新任务变体，又能延续预训练时的广泛能力。整体含义是提出一种极简且高鲁棒性的微调范式，摆脱“学新忘旧”的困境。

## 2. 论文提出的方法论
核心思想是**参数合并（Model Merging）**。具体而言：
- 在完成对新任务的常规微调后，并不直接使用微调后的模型，而是将**微调模型的权重与预训练模型的权重进行插值合并**。
- 形式上，假设预训练权重为 \(\theta_{pre}\)，微调后权重为 \(\theta_{ft}\)，则最终使用的权重为：
  \[
  \theta_{merge} = (1 - \lambda) \cdot \theta_{pre} + \lambda \cdot \theta_{ft}
  \]
  其中 \(\lambda \in [0,1]\) 为合并系数。
- 该方法不引入额外参数、无需重放旧数据、不改变训练流程，仅通过一次权重线性组合，让合并模型同时继承预训练的通用能力和微调后的新技能。
- 该策略还自然支持**终身学习**：多次合并可不断加入新技能而不牺牲旧能力。

## 3. 实验设计
论文声称在**大量仿真实验和真实世界实验**中进行了验证（具体数据集名称、环境细节未在提供的摘要与元数据中给出）。从已有信息可推断：
- **对比基准**应至少包括：纯预训练模型（不微调）、纯微调模型、以及所提出的合并模型。
- **评估维度**可能包括：新任务分布内表现、新任务分布外泛化程度、旧任务的性能保留情况、持续学习场景下的知识积累。
- 具体使用的基准测试集（如机器人操作任务集）和对比方法细节在此处未完整披露，有待原文补充。

## 4. 资源与算力
提供的文本内容中**未提及任何关于 GPU 型号、数量、训练时长、参数量或浮点运算量等信息**。因此无法评估算力消耗和计算效率。

## 5. 实验数量与充分性
文本仅提到“extensive simulated and real-world experiments”，说明实验规模较大，覆盖仿真与真实环境。但由于缺乏具体实验组数、消融实验设计（如不同合并系数 \(\lambda\) 的敏感性、不同微调策略的影响等），**无法确切判断实验的全面性和公平性**。从常理看，该方法极简，验证其有效性通常需要多任务、多环境、多基线的充分对比，但需依据原文全文进一步确认。

## 6. 论文的主要结论与发现
- 权重合并后的单一模型在**新任务的分布外变体上表现优于预训练模型和微调模型**，有效缓解了微调带来的泛化退化。
- 合并模型**完好保留了预训练获得的通用能力**，克服了灾难性遗忘。
- 该方法支持**持续地增量学习新技能**（终身学习场景），每次合并新技能后，依然能维持对所有旧技能的掌握。

## 7. 优点
- **极度简单**：仅需一次权重线性插值，无需额外存储、计算或复杂算法。
- **即插即用**：可适用于任何基于梯度微调的 VLA 策略，不侵入训练流程。
- **鲁棒性强**：实验表明能同时提升新任务泛化性和旧技能保持性，对超参数 \(\lambda\) 可能具有一定容忍度。
- **支持持续扩展**：为机器人策略的终身学习提供了一种轻量级解决方案。

## 8. 不足与局限
- **细节缺失**：由于仅基于摘要与元数据，无法获知具体任务设置、合并系数选取策略、是否对 \(\lambda\) 进行调优、在更极端的任务差异下是否依然有效。
- **理论分析空白**：摘要未涉及该方法为何能有效平衡新旧知识的理论解释。
- **可能存在的限制**：参数线性合并假设预训练与微调后的损失景观是线性连接的，若二者参数相差过大或存在非线性割裂，合并效果可能退化；未与其他抗遗忘方法（如 EWC、数据重放、模型扩展等）进行对比，说服力可能受限。
- **真实世界验证的广度**：未知真实实验的任务多样性和环境复杂度，能否推广到所有 VLA 策略尚待验证。

（完）
