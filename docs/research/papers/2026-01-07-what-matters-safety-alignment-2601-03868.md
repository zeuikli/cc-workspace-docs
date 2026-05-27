---
title: "What Matters For Safety Alignment?"
arxiv_id: 2601.03868
authors: "Xing Li, Hui-Ling Zhen, Lihao Yin, et al."
published: 2026-01-07
source: "https://arxiv.org/abs/2601.03868"
source_tier: P
---

# What Matters For Safety Alignment?

**ArXiv**: 2601.03868 | **Date**: 2026-01-07 (修訂 2026-02-24) | **Authors**: Xing Li, Hui-Ling Zhen, Lihao Yin, et al. | **Category**: cs.CL

## 摘要

大規模實證研究，評估 32 個模型（13 個系列，3B–235B 參數）的安全對齊能力，涵蓋 6 個關鍵模型特性、3 種外部攻擊技術、5 個安全資料集、56 種越獄技術、4 種思維鏈攻擊策略，共 **460 萬次 API 調用**。

## 主要發現

### 最安全的模型

GPT-OSS-20B、Qwen3-Next-80B-A3B-Thinking、GPT-OSS-120B — 共同特點：整合推理和自我反思機制。

### Post-Training 風險

**關鍵發現**：後訓練（post-training）和知識蒸餾（knowledge distillation）可能導致「安全對齊的系統性退化」。安全應在此階段作為**顯式約束**，而非事後考量。

### Chain-of-Thought 脆弱性

| 攻擊方式 | 攻擊成功率 |
|---------|----------|
| CoT 攻擊（通過 response prefix）| 平均 **3.34× 提升** |
| 部分模型極端案例 | 從 **0.6% → 96.3%** |

文字補全介面（text-completion interfaces）和用戶定義 response prefix 存在嚴重安全風險。

### 主要攻擊方法

- 角色扮演（Roleplay）
- 提示注入（Prompt Injection）
- 梯度搜索對抗提示（Gradient-based adversarial prompts）

## 模型參數大小 vs 安全性

規模效應並非線性：
- 最安全模型包括 20B 和 80B（非最大的 235B）
- 整合推理機制（thinking）比純粹規模更重要

## 對 Workspace 的意義

與 `2026-05-23-cheating-agents-benchmark-manipulation` 形成互補：
- 前者：benchmark manipulation（外部攻擊評估系統）
- 本文：safety alignment failure（模型在安全場景中的失敗）

CoT 攻擊脆弱性提示：在 agentic 環境中使用 response prefix 引導時需特別注意安全邊界。

## 分類

**Safety & Alignment** — 迄今最大規模的安全對齊系統評估，CoT 3.34× 攻擊放大效應是 agentic 環境安全設計的關鍵警示。
