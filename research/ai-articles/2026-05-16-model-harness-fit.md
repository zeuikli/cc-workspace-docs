---
title: "Model-Harness Fit"
url: https://nicolasbustamante.com/blog/model-harness-fit
domain: nicolasbustamante.com
author: Nicolas Bustamante
published: 未知
archived: 2026-05-16
tags: [model-harness, agent, claude-code, codex, copilot, post-training]
word_count: 約 620 字
---

# Model-Harness Fit

> **來源**：[nicolasbustamante.com](https://nicolasbustamante.com/blog/model-harness-fit)  
> **作者**：Nicolas Bustamante  
> **發布日期**：未知  
> **收錄日期**：2026-05-16  
> **字數**：約 620 字

---

## Overview

Nicolas Bustamante 的文章探討為何在不同 agent harness（協作框架）之間切換模型，即使使用相同的模型權重，性能也會下降。核心論點：**模型是針對特定 harness 進行 post-training 的，因此配對（model + harness）才是正確的分析單位，而非模型本身。**

## Core Argument

Bustamante 論證「模型是針對 harness 而非僅針對 API 進行 post-training」。Tool 名稱、input schemas、引用慣例、system prompt 結構都是「baked into post training 的 byte-level 慣例」。將模型從其原生 harness 抽出，所損失的性能「不重寫任何一側就無法找回」。

## Evidence from Terminal-Bench 2.0

排行榜揭示顯著差距：Claude Opus 4.6 搭配 ForgeCode 達到 79.8%，但搭配 Capy 只有 75.3%——**相同模型、不同 harness，差距 4.5 個百分點**。Cursor 研究團隊回報「僅改變 harness，就從 Top 30 躍升至 Top 5」。

## Three Harness Architectures Compared

**Codex CLI**：使用帶有結構化記憶提取的 typed 非同步 submission/event queue，透過嚴格 JSON schema 與 `<oai-mem-citation>` 標籤實現 decay signals。

**Claude Code**：直接對話迴圈，使用 `Read`/`Edit`/`Write` 工具進行同步 file-based 記憶寫入，並透過 `<system-reminder>` 注入。

**GitHub Copilot CLI**：透過 JSON RPC subprocess 執行 supervisor protocol，搭配 server-side 記憶後端與 `store_memory` 工具。

## Divergent Tool Surfaces

每個 harness 提供不同的 tool vocabulary：Codex 提供帶有 Lark grammar 的 `apply_patch`；Claude Code 使用帶有 `old_string`/`new_string` 替換的 `Edit`；Copilot CLI 依照當前模型路由兩者。**相同的概念操作有「不同的 shape」**，要求在一個 surface 上訓練的模型在切換時必須脫離其本能集合外運作。

## The Memory Layer Problem

引用機制存在根本差異：Codex 的 `<oai-mem-citation>` blocks 在 SQLite 中遞增 `usage_count` 以驅動 decay 邏輯；Claude Code 的模型透過帶有 age-in-days 標注的 `<system-reminder>` wrappers 讀取記憶；Copilot CLI 委派給遠端伺服器。跨 harness 執行會導致記憶系統「靜默失敗或執行降級版本」。

## System Prompt Structure

Copilot CLI 文件化了十個明確的 system prompt section IDs（`identity`、`tone`、`tool_efficiency` 等）。每個區塊帶有特定的 authority weight——`safety` 區塊比 `guidelines` 更硬性。在不同 prompt 排序下訓練的模型，對指令優先序的處理方式不同。

## Key Insight: The Matched Pair

正如 LangChain 的 Trivedy 所言：「Agent = Model + Harness。如果你不是模型，你就是 harness。」Cursor 的 Stefan Heule 描述這份工作是「執念地堆疊小優化」，因為「step change 很罕見，收益只在匹配的 pair 內複合累積」。

## Practical Implications

- **平台建構者**：以統一產品出貨 model-harness pairs，而非模組化元件
- **模型實驗室**：harness 代表產品策略與競爭護城河，而非單純基礎設施
- **使用者**：mid-conversation 切換模型會同時破壞對話歷史分佈、cache 結構與 tool surfaces
- **關鍵不穩定性**：隨著模型成熟，harness 元件會變得 load-bearing 或過時——Rajasekaran 的工作顯示，Sonnet 4.5 所需的 context-reset 機制對 Opus 4.6 已不必要

## Strategic Convergence

Anthropic 出貨 Claude Code 作為 canonical Claude harness；OpenAI 出貨 Codex CLI 作為 canonical Codex harness；GitHub 出貨帶有明確 per-model routing 的 Copilot CLI 應對多模型場景。每個都代表對 model-harness coupling 管理的一個連貫但不同的答案。
