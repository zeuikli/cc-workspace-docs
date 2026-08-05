---
url: "https://arxiv.org/abs/2604.02812"
title: "Learning Structured Robot Policies from Vision-Language Models via Synthetic Neuro-Symbolic Supervision"
archived_date: "2026-07-12"
arxiv_id: "2604.02812"
authors: ["Alessandro Adami", "Tommaso Tubaldo", "Marco Todescato", "Ruggero Carli", "Pietro Falco"]
domain: neuro-symbolic-robot-policy
published_date: "2026-04-03"
source_routine: routine-e
---

# Learning Structured Robot Policies from Vision-Language Models via Synthetic Neuro-Symbolic Supervision

## 摘要 / 核心貢獻

針對端到端機器人策略「不透明、難以驗證」的問題，本文提出一套 neuro-symbolic 方法：
用 vision-language model 從視覺觀測、自然語言指令與結構化系統規格，
生成可執行的 **Behavior Tree 策略**——神經網路產出的是可解釋的符號結構，而非黑箱動作序列。

**核心貢獻：**
- 自動化 pipeline，透過 domain randomization 生成合成訓練資料，免除人工標註
- 把「符號約束下的任務分解」與「馬達控制細節」分離學習，12B 參數模型即可學會
  Behavior Tree 合成所需的映射
- 在兩種不同機械臂上驗證：僅用模擬資料訓練的結構化策略達成 zero-shot 遷移至真實環境

## 為何屬「新領域」

`neurosymbolic` / `neuro-symbolic` 關鍵詞在 workspace 自有題庫命中 **0 次**。
Workspace 既有機器人相關探勘（2026-06-28 formal-verification-robotics）聚焦「驗證方法」，
本篇聚焦「策略生成本身即產出符號結構」——與既有覆蓋互補而非重疊，且與 workspace 核心公理
「LLM 只做判斷、確定性程序做決定」同構（VLM 判斷 → Behavior Tree 為確定性可執行結構）。
