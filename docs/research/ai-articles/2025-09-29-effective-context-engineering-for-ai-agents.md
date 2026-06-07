---
url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
title: "Effective context engineering for AI agents"
author: "Anthropic Applied AI Team"
archived: 2026-05-27
domain: anthropic.com
published: 2025-09-29
tags: [anthropic, context-engineering, prompt-engineering, llm-agents, long-horizon-tasks]
word_count: "約 1,400 字"
---

# Effective context engineering for AI agents

> **來源**：[anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
> **作者**：Prithvi Rajasekaran、Ethan Dixon、Carly Ryan、Jeremy Hadfield（Anthropic Applied AI）；貢獻者：Rafi Ayub、Hannah Moran、Cal Rueb、Connor Jennings
> **發布日期**：2025-09-29
> **收錄日期**：2026-05-27

---

## Overview

Context engineering 是 prompt engineering 的自然演進：從「找對詞彙和句式」轉向「什麼樣的 token 配置最能引導模型產生期望行為」。Anthropic 定義 context engineering 為「在 LLM inference 期間策劃並維護最佳 token 集合的策略」。核心原則：**將 context 視為有限資源，邊際報酬遞減**，目標是找到能最大化期望結果的最小高信號 token 集合。

---

## Context Engineering vs. Prompt Engineering

| 面向 | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| 焦點 | 單一 prompt 的用詞優化 | 整個 agent 互動中的 token 配置 |
| 範疇 | 單次推論 | 多輪 session、跨 context window |
| 核心問題 | 「說什麼？」 | 「放什麼資訊、放在哪裡？」 |

---

## Context Rot 與 Attention Budget

隨著 context window 擴大，模型準確度會退化（**context rot**）。根源在 transformer 架構：模型需要處理所有 token 間 n² 的成對關係，context 越長，attention 越稀薄。結論：注入更多資訊不等於更好的結果。

---

## 有效 Context 的主要組成

### 1. System Prompts

- 要具體（足以引導行為）又靈活（足以讓模型應對多種情境）
- 避免過於脆弱的 if-else 邏輯，也避免模糊的通用指示
- 找到能讓模型建立穩健啟發式規則的平衡點

### 2. Tools

- 工具集應**最小化、無重疊、意圖明確**
- 設計良好的工具回傳 token 高效的資訊，同時鼓勵 agent 採取高效行為
- 避免功能模糊或重疊的工具，防止 agent 決策歧義

### 3. Examples（Few-shot Prompting）

- 「Examples 是值千言的圖片」——示範期望行為比描述更有效
- 精選一組**多樣、典型**的範例，優於試圖枚舉所有邊緣案例
- 避免過度窮舉：邊緣案例清單反而稀釋注意力

### 4. Message History

- 視為動態狀態，需要主動管理而非被動累積
- 隨著對話延伸，應定期壓縮或精煉歷史記錄

---

## Runtime Context 策略

### Just-in-Time Retrieval

- Agent 維護輕量級 identifier，而非預先載入所有資料
- 執行任務時透過工具動態取得所需資訊
- 效仿人類認知模式：需要時才查閱，不是全部記住

### Hybrid Approaches

- 結合預先取得（速度）與自主探索能力（靈活性）
- 根據任務特性在執行效率與 runtime 成本間取得平衡

---

## 長期任務（Long-Horizon Tasks）技術

### 1. Compaction（壓縮）

- 摘要並壓縮對話歷史
- 保留關鍵決策，丟棄冗餘輸出
- 讓 agent 在接近 context 上限時仍能繼續有效工作

### 2. Structured Note-Taking（結構化筆記）

- Agent 維護外部記憶文件（如 `progress.txt`、`notes.md`）
- 實現跨 context reset 的持久記憶
- 新 session 開始時先讀筆記，快速重建工作狀態

### 3. Sub-Agent Architectures（子 agent 架構）

- 專業化 agent 各自處理範疇聚焦的任務，擁有乾淨的 context
- 將精煉後的摘要回傳主 agent
- 避免單一 agent context 過度膨脹

---

## 核心指導原則

> **找到能最大化期望結果的最小高信號 token 集合。**

- 每個加入 context 的 token 都有成本（attention 消耗）
- 過多 context 稀釋關鍵資訊，降低模型表現
- 「緊湊但資訊豐富」優於「全面但冗長」
- 與人類認知的類比：過多資訊導致認知過載，少而精的資訊促進清晰判斷
