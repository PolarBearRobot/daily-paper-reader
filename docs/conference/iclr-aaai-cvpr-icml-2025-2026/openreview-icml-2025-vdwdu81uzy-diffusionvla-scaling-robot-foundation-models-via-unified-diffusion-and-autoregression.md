---
title: "DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression"
title_zh: DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型
authors: "Junjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Jinming Li, Zhongyi Zhou, Xiaoyu Liu, Chaomin Shen, Yaxin Peng, Feifei Feng"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=VdwdU81Uzy"
tags: ["query:model"]
score: 10.0
evidence: 融合自回归推理与扩散策略以扩展机器人基础模型
tldr: 针对现有VLA模型缺乏精确动作生成或推理能力的问题，提出DiffusionVLA框架，融合预训练VLM的自回归推理与扩散策略，通过推理注入模块将推理短语嵌入策略学习，实现了可扩展、兼具推理与精准动作生成的机器人基础模型，在多种任务上展现了优越性能。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 自回归VLA模型缺乏精确鲁棒的动作生成，而扩散策略缺乏推理能力。
method: 以自回归推理引导扩散动作策略，通过推理注入模块将推理短语嵌入策略学习过程。
result: 框架简单灵活高效，能够从噪声数据中鲁棒推理，实现精准动作生成。
conclusion: 提出了可扩展的通用机器人基础模型新范式，兼具推理与动作生成能力。
---

## Abstract
In this paper, we present DiffusionVLA, a novel framework that integrates autoregressive reasoning with diffusion policies to address the limitations of existing methods: while autoregressive Vision-Language-Action (VLA) models lack precise and robust action generation, diffusion-based policies inherently lack reasoning capabilities. Central to our approach is autoregressive reasoning — a task decomposition and explanation process enabled by a pre-trained VLM — to guide diffusion-based action policies. To tightly couple reasoning with action generation, we introduce a reasoning injection module that directly embeds self-generated reasoning phrases into the policy learning process. The framework is simple, flexible, and efficient, enabling seamless deployment across diverse robotic platforms.

We conduct extensive experiments using multiple real robots to validate the effectiveness of DiVLA. Our tests include a challenging factory sorting task, where DiVLA successfully categorizes objects, including those not seen during training. The reasoning injection module enhances interpretability, enabling explicit failure diagnosis by visualizing the model’s decision process. Additionally, we test DiVLA on a zero-shot bin-picking task, achieving \textbf{63.7\% accuracy on 102 previously unseen objects}. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiVLA can follow novel instructions and retain conversational ability. Notably, DiVLA is data-efficient and fast at inference; our smallest DiVLA-2B runs 82Hz on a single A6000 GPU. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

---

## 论文详细总结（自动生成）

# DiffusionVLA 论文总结

## 1. 核心问题与整体含义（研究动机和背景）

- 当前机器人基础模型面临双方面挑战：
  - 自回归视觉-语言-动作（VLA）模型虽然具备推理能力，但动作生成不够精准与鲁棒。
  - 基于扩散策略（diffusion policies）的方法能生成精细动作，却缺乏推理与任务分解能力。
- 研究目标是构建一个兼具自主推理与精准动作生成的通用框架，以扩展机器人基础模型的规模与适用性。
- 整体含义：提出“以推理引导动作”的新范式，使机器人能够理解任务、解释决策并灵活执行，提升泛化性和可解释性。

## 2. 论文提出的方法论

### 核心思想
- 将预训练视觉语言模型（VLM）的自回归推理能力与扩散动作策略相结合。
- 自回归推理负责任务分解和自然语言解释，扩散策略负责高精度动作生成。
- 引入“推理注入模块”（reasoning injection module），将模型自生成的推理短语直接嵌入策略学习过程，实现推理与动作的紧密耦合。

### 关键技术细节
- **框架组成**：
  - 预训练VLM作为推理骨干，输出文本推理（对任务的理解、步骤规划等）。
  - 扩散去噪网络作为动作生成器，输入观测和推理嵌入，输出动作序列。
- **推理注入模块**：
  - 将VLM生成的推理短语（token级别或句子级别）编码为稠密向量。
  - 该向量被注入扩散去噪过程的每一层（可能是通过交叉注意力或特征拼接），使动作生成直接受推理内容指导。
- **训练过程**：
  - 联合微调：保持VLM的语言能力，同时训练扩散策略以顺从推理信号。
  - 数据来源：与具体任务相关的机器人演示数据，同时利用VLM预训练时的世界知识。

### 流程简述
1. 输入：当前观测（图像等）与任务指令。
2. 自回归阶段：VLM生成结构化推理文本。
3. 注入阶段：将推理文本编码后融入扩散模型。
4. 扩散阶段：基于融合特征迭代去噪，输出动作序列。

## 3. 实验设计

### 数据集与场景
- 多个真实机器人平台上的测试，具体场景包括：
  - 工厂分拣任务（factory sorting）：对有训练未见的物体进行分类。
  - 零样本料箱抓取（zero-shot bin-picking）：使用102种未见过的物体，测试泛化能力。
  - 视觉扰动测试：添加干扰物、更换背景，验证鲁棒性。
  - 新指令跟随与对话能力保留测试。
- Benchmark：没有明确提到公开基准，主要使用自行设计的真实世界任务，关注成功率、准确率、推理速度等。

### 对比方法
- 文中摘要未详细列出对比方法名称，但可推断：
  - 自回归VLA模型（如RT-2等）作为基准，对比动作精度。
  - 扩散策略类方法（如Diffusion Policy）作为基准，对比推理能力。
- 强调与纯自回归和纯扩散的分离对比，突出融合的优势。

## 4. 资源与算力

- 提到最小规模模型DiffusionVLA-2B可在单个A6000 GPU上达到82Hz推理速度。
- 训练阶段的算力（GPU型号、数量、训练时长）在摘要中未明确说明，需要查阅论文正文。
- 模型规模从2B参数扩展到72B，表明训练需大量算力，但具体资源未公开。

## 5. 实验数量与充分性

- 实验组包含：
  - 复杂分拣任务（含未见过物体） ×1
  - 零样本抓取（102种未见物体）测试 ×1
  - 视觉鲁棒性测试（干扰物、新背景） ×2+
  - 新指令跟随和对话能力定性测试 ×1
  - 模型规模缩放实验（2B→72B） ×1
  - 消融研究（推理注入模块的有效性，可能还有不同规模对比）虽未明说，但常见于此类论文。
- 整体上看，实验覆盖了泛化性、鲁棒性、可解释性、速度、可扩展性等多个维度，且基于真实机器人，具有较强的现实说服力。对比与消融若详实则更充分，但摘要未列细节。

## 6. 主要结论与发现

- 通过自回归推理引导扩散策略，DiffusionVLA实现了更精准的动作生成与任务级推理的统一。
- 框架简单灵活，可跨多种机器人平台部署，且数据高效、推理速度快。
- 推理注入模块增强了可解释性：可通过可视化决策过程进行失败诊断。
- 零样本任务（未见物体抓取）达到63.7%准确率，展示了强泛化能力。
- 模型规模扩大带来泛化性能的持续提升，表明该范式具有良好的可扩展性。

## 7. 优点（方法或实验设计的亮点）

- **架构融合创新**：首次将自回归推理与扩散动作紧密结合，弥补两类方法各自短板。
- **可解释性强**：通过自然语言推理输出，使机器人决策透明，便于调试。
- **可扩展性**：验证了从2B到72B参数规模下性能的提升，展现基础模型潜力。
- **真实世界验证**：在多个真实机器人任务和未见物体上测试，减少仿真-现实差距。
- **高效率**：最小模型推理速度达82Hz，适合实时控制。
- **鲁棒性**：对视觉变化、新背景、新指令均有良好适应能力。

## 8. 不足与局限（包括实验覆盖、偏差风险、应用限制等）

- **内容不完整**：当前仅基于摘要分析，缺少具体方法细节、对比实验中的数值结果、训练资源等，难以深入评估。实际PDF由于验证页面无法获取完整内容。
- **零样本精度仍有提升空间**：63.7%准确率对于工业应用可能不足，且未报告其他基线在同一任务上的表现。
- **任务类型相对简单**：主要涉及抓取和分拣，缺乏长序列、接触密集或精密操作任务。
- **跨机器人部署的具体成本未说明**：虽声称易部署，但未给出适配新本体的工作量或数据需求。
- **数据集和评测基准缺乏统一性**：未使用公共benchmark，可能降低与其他工作的可比性。
- **推理注入可能增加计算负担**：虽然推理速度高，但未对比纯扩散策略在相同硬件上的延迟。

（完）
