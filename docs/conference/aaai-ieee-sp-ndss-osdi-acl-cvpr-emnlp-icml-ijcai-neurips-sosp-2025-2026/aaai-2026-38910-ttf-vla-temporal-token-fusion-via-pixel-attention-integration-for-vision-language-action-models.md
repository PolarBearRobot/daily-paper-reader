---
title: "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models"
title_zh: "TTF-VLA: 面向视觉-语言-动作模型的时间令牌融合通过像素注意力集成"
authors: "Chenghao Liu, Jiachen Zhang, Chengxuan Li, Zhimu Zhou, Shixin Wu, Songfang Huang, Huiling Duan"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38910/42872"
tags: ["query:analysis"]
score: 9.0
evidence: 提出时间令牌融合，集成历史与当前视觉表示，提升机器人操作中VLA模型的推理质量
tldr: 针对VLA模型逐帧处理视觉输入丢失时序信息的问题，TTF-VLA提出一种无需训练的时间令牌融合方法。通过灰度像素差分析和注意力语义评估双重检测，选择性融合历史与当前视觉令牌，增强VLA模型对视觉噪声的鲁棒性和动作生成的一致性。实验在机器人操作任务上验证了该方法能有效提升VLA的推理性能。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38910/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1619, \"height\": 913, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38910/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 845, \"height\": 820, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38910/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1797, \"height\": 558, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38910/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 878, \"height\": 252, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38910/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 873, \"height\": 871, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38910/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1430, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38910/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 809, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38910/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1748, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38910/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 860, \"height\": 248, \"label\": \"Table\"}]"
motivation: VLA模型独立处理每帧图像，丢弃了机器人操作中的时序信息，易受噪声影响。
method: 提出训练自由的时间令牌融合，结合像素差异与注意力语义检测，选择性融合历史视觉令牌。
result: 在操纵任务中提升了VLA模型的推理质量和鲁棒性。
conclusion: TTF-VLA为VLA模型的时序信息利用提供了一种高效、实用的方案。
---

## Abstract
Vision-Language-Action (VLA) models process visual inputs independently at each timestep, discarding valuable temporal information inherent in robotic manipulation tasks. This frame-by-frame processing makes models vulnerable to visual noise while ignoring the substantial coherence between consecutive frames in manipulation sequences. We propose Temporal Token Fusion (TTF), a training-free approach that intelligently integrates historical and current visual representations to enhance VLA inference quality. Our method employs dual-dimension detection combining efficient grayscale pixel difference analysis with attention-based semantic relevance assessment, enabling selective temporal token fusion through hard fusion strategies and keyframe anchoring to prevent error accumulation. Comprehensive experiments across LIBERO, SimplerEnv, and real robot tasks demonstrate consistent improvements: 4.0 percentage points average on LIBERO (72.4% vs 68.4% baseline), cross-environment validation on SimplerEnv (4.8% relative improvement), and 8.7% relative improvement on real robot tasks. Our approach proves model-agnostic, working across OpenVLA and VLA-Cache architectures. Notably, TTF reveals that selective Query matrix reuse in attention mechanisms enhances rather than compromises performance, suggesting promising directions for direct KQV matrix reuse strategies that achieve computational acceleration while improving task success rates.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义  
- **核心痛点**：当前的视觉‑语言‑动作（VLA）模型在机器人操作中**逐帧独立处理视觉输入**，完全丢弃了连续帧之间的时空连贯性。  
- **带来的后果**：  
  - 模型对光照波动、运动模糊、传感器噪声等视觉噪声高度敏感。  
  - 重复计算大量冗余视觉令牌，浪费计算资源并忽视“背景稳定、变化集中在局部”的固有特性。  
- **整体目标**：提出一种**无需重新训练**的时间令牌融合方法，智能地整合历史帧与当前帧的视觉表达，在不牺牲变化敏感度的前提下，增强 VLA 推理的鲁棒性和成功率。

## 2. 方法论  
本方法的核心是 **Temporal Token Fusion (TTF)**，一个即插即用的推理增强框架。关键技术细节如下：

- **问题形式化**  
  输入序列为 `{I_t, L_t} → A_t`，目标是通过融合函数 `F` 生成融合后的令牌 `T̃_t = F(T_t, T_{t-1}, I_t, I_{t-1}, L_t)`。

- **硬融合策略**  
  为每个图像块 `i` 做一个二值决策：  
  - 重要块（`m_fusion_i = 1`） → 使用**当前帧令牌** `t_i_t`；  
  - 非重要块（`m_fusion_i = 0`） → 重用**历史帧令牌** `t_i_{t-1}`。  
  该决策由双维度检测的**逻辑或**确定：`m_fusion_i = m_pixel_i ∨ m_attention_i`。

- **双维度检测**  
  1. **灰度像素差分检测**（低层空间动态）：  
     将 RGB 转灰度，计算相邻帧在该块区域内的平均绝对亮度差，超过阈值 `τ_pixel` 的块视为重要块。该方法复杂度为 **O(1)**，且对物体移动和阴影变化敏感。  
  2. **注意力语义相关性检测**（高层语义重要性）：  
     利用上一时刻的 Transformer 注意力权重（文本‑到‑视觉 或 动作‑到‑视觉），计算每个视觉块的平均注意力得分，然后通过 `Top‑K` 选取高相关度块作为重要块。这种做法避免了推理时的额外计算。

- **关键帧机制**  
  每隔 `K` 步强制将所有块标记为重要（即使用当前令牌），防止长期误差累积。公式为 `IsKeyframe(t) = (t mod K == 0) ∨ (T_{t-1} = ∅)`。

- **算法流程概览**  
  非关键帧时：提取当前令牌后，对每个块依次计算像素掩码、注意力掩码，通过逻辑或得到融合掩码，最后按掩码拼接当前令牌和历史令牌。整体增加的计算开销不超过 2%。

## 3. 实验设计  
- **数据集与场景**  
  - **LIBERO**：四个任务套件 —— Object、Spatial、Goal、Long。每套件 10 个任务，每任务 20 次评估（共 800 集）。  
  - **SimplerEnv**：跨平台验证，三个任务：移动靠近、抓可乐罐、抽屉操作（多种方向），共 756 集。  
  - **真实机器人**： Franka Research 3 执行三个任务：抓取放置大蒜、多物体顺序操作（胡椒和玉米）、关闭抽屉。每任务收集 80 次示教（Gello遥操作），评估时各 20 集。

- **基准与对比方法**  
  - 基础模型：**OpenVLA‑7B**（微调检查点用于 LIBERO，未微调基础模型用于 SimplerEnv，真实任务微调）和 **VLA‑Cache**（利用其 KV 缓存机制的版本）。  
  - 对比：基线 vs **基线+TTF**；消融实验额外对比“仅像素 TTF”“仅注意力 TTF”。

## 4. 资源与算力  
- 论文**未明确说明**训练或推理所使用的 GPU 型号、显存容量、单次训练时长等资源细节。  
- 仅提到真实机器人任务微调 OpenVLA‑7B 时，训练 **20,000 步**、批量大小为 **8**，推理频率 5 Hz，**未披露所需计算硬件**。

## 5. 实验数量与充分性  
- **主要实验**：  
  - LIBERO 4 组任务 × 2 种架构（OpenVLA、VLA‑Cache），共 8 组主结果。  
  - SimplerEnv 3 组任务（1 种模型）。  
  - 真实机器人 3 组任务。  
- **消融实验**：  
  - 分析维度消融（像素 only、注意力 only、双维度）在 LIBERO 全部四个套件上完成。  
  - 关键帧间隔 `K` 的系统分析（K=2~200，共 14 种配置），展示成功率与融合率的变化。  
- **充分性与公平性**：  
  对比基线均来自公开检查点或官方实现，参数设置一致（跨平台未调参），任务覆盖长程、空间推理、抓取等多种维度。消融与超参分析完整，成功验证了方法各组件的必要性，整体实验量充足且公平。

## 6. 主要结论与发现  
- **一致提升**：TTF 在 LIBERO 上平均提升 **4.0 个百分点**（72.4% vs 68.4%），SimplerEnv 相对提升 4.8%，真实机器人相对提升 8.7%，且适用于 OpenVLA 和 VLA‑Cache 两种架构。  
- **时序融合有效性**：双维度检测（像素+注意力）能精确区分需更新的块和可复用的块，既保持了任务关键变化的敏感性，又通过对稳定背景的时间重用增强了抗噪声能力。  
- **Query 重用的意外收益**：在 VLA‑Cache+TTF 中，Token 融合间接实现了 Query 矩阵的部分复用，实验证明这种做法不仅没有损害性能，反而**同时提高了成功率和计算效率**，揭示了直接复用 KQV 矩阵的“免费午餐”潜力。  
- **高效性与鲁棒性**：推理开销极小（<2%），对超参数不敏感（关键帧 K=3 附近性能稳定），适用于长程与噪声环境。

## 7. 优点  
- **无需训练**：即插即用，不会引入额外的模型微调成本。  
- **计算友好**：像素差分检测复杂度为 O(1)，注意力复用上一帧权重，整体推理几乎不增加延迟。  
- **双维度互补**：低层像素变化与高层语义注意力协同作用，覆盖了从细粒度运动到任务语义的多种变化模式。  
- **实用性强**：在仿真基准、跨环境验证和真实机器人上均得到验证，对视觉噪声的容忍度高，具备从模拟到现实的部署潜力。  
- **启发性发现**：Query 矩阵复用的正面效果为未来研究同时追求速度与精度的注意力优化指明了方向。

## 8. 不足与局限  
- **缺少与其他时序融合方法的对比**：仅与自身基线和基于 KV 缓存的 VLA‑Cache 比较，未涉及视频时序建模中的常见方法（如光流引导、3D 注意力等），在 VLA 任务上的相对优势边界不够清晰。  
- **真实机器人实验规模小**：仅有三个任务，每任务20次评估，结论的统计显著性未被验证，且缺少对长期部署稳定性的测试。  
- **对剧烈场景突变的鲁棒性未知**：像素差分阈值固定，若环境光照或背景发生全局大幅变化，可能误判大量块为重要，降低融合效益。  
- **任务适配参数**：VLA‑Cache 中使用了任务相关的融合率调整（30%~50%），实际部署时可能需要一定调参。  
- **计算资源细节未公开**，无法评估训练阶段的碳排放或资源需求。  

（完）
