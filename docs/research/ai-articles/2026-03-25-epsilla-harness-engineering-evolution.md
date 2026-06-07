---
url: "https://www.epsilla.com/blogs/harness-engineering-evolution-prompt-context-autonomous-agents"
title: "The Third Evolution: Why Harness Engineering Replaced Prompting in 2026"
author: "Isabella (Epsilla)"
archived: 2026-05-27
domain: epsilla.com
published: 2026-03-25
tags: [harness-engineering, prompt-engineering, context-engineering, autonomous-agents, llm-agents, enterprise-ai]
word_count: "約 1,200 字"
---

# The Third Evolution: Why Harness Engineering Replaced Prompting in 2026

> **來源**：[epsilla.com](https://www.epsilla.com/blogs/harness-engineering-evolution-prompt-context-autonomous-agents)
> **作者**：Isabella（Epsilla）
> **發布日期**：2026-03-25
> **收錄日期**：2026-05-27

---

## Overview

本文記錄 AI 工程實踐的演進歷程，論證業界已從優化單一 prompt 轉移到為自主 agents 建構完整的運作環境。核心論點：「Agents 不難；難的是 Harness。」

## 三代演進歷程

### 第一代：Prompt Engineering（2022–2024）

專注於製作最佳化的單一指令，技術包括 few-shot learning 和 chain-of-thought prompting。工程師的核心工作是「找到正確的詞語」。

### 第二代：Context Engineering（2025）

認識到模型需要動態建構的 context window，包含相關文件、對話歷史和工具定義。重點從「如何說」轉移到「給什麼資訊」。

### 第三代：Harness Engineering（2026）

系統層面的架構設計，涵蓋 agents 的完整工作流程、約束條件、回饋迴路和生命週期管理。重點從「說什麼」轉移到「建立什麼環境」。

## 關鍵效能數據

**最重要的實驗結果**：使用**相同模型、相同資料、相同 prompt**，一個團隊透過僅修改 runtime 環境，將程式設計 benchmark 成功率從 **42% 提升至 78%**。

唯一的變數是包裹模型的 shell——即 harness 本身。

此外，Anthropic 展示了在管理環境中採用結構化迭代方法，儘管成本更高，卻能產生更優異的結果。

## Harness 核心概念

Mitchell Hashimoto 的定義：「工程化解決方案，防止 agent 錯誤重複發生。」

關鍵洞見：「Agents 不難；Harness 才難。」

## 真實案例驗證

### OpenAI Codex 團隊

五個月內在 1,500 個 pull requests 中生成約**一百萬行**生產程式碼，零人工撰寫程式碼。

核心 harness 原則：
1. **Repository is truth**：repository 是 agent 唯一的事實來源，不假設外部知識
2. **Agent-readable code**：程式碼必須對 agent 可讀（不只對人類），需有清晰一致的結構和詳細 comment
3. **Linter-enforced constraints**：架構約束由 linter 強制執行，而非依賴 prompt——建立一個讓違反規則成為不可能的系統
4. **Incremental autonomy**：逐步擴大自主權範圍

### Stripe Minions

「Minions」機群每週合併超過 **1,300 個 pull requests**，採用「Blueprint」編排系統，分離確定性節點與 agentic 節點，並有嚴格的兩次失敗升級規則。

## Anthropic 的評估者模型

Anthropic 識別的關鍵限制：**模型無法可靠地自我評估其工作**。

解決方案：實作受 GAN 架構啟發的獨立 Generator 和 Evaluator agents，評估者使用 Playwright 等工具進行端對端測試。

## 約束的悖論

限制解決方案空間看似矛盾，實際上能提升生產力：
- 防止探索無效路徑
- 強迫更快收斂至正確解

## Epsilla 的 Semantic Graph 解決方案

Epsilla 提出企業級 harness 基礎設施，提供：

| 功能 | 說明 |
|------|------|
| **結構性約束** | 防止幻覺（hallucination） |
| **持久記憶** | 編碼回饋迴路 |
| **可擴展的非同步互動** | 支援 Agent-as-a-Service (AaaS) 部署 |

## 核心結論

Harness engineering 解決了前兩代範式無法處理的根本問題：「AI 模型無法可靠評估自身工作」。答案不是更好的 prompt，而是更好的環境設計。

---

*相關 Epsilla 文章：*
- *[Harness Engineering: Why the Focus is Shifting from Models to Agent Control Systems](https://www.epsilla.com/blogs/2026-03-12-harness-engineering)*
- *[The GAN-Style Agent Loop: Deconstructing Anthropic's Harness Architecture](https://www.epsilla.com/blogs/anthropic-harness-engineering-multi-agent-gan-architecture)*
