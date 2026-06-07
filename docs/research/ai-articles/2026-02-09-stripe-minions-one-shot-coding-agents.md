---
url: "https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents"
title: "Minions: Stripe's one-shot, end-to-end coding agents"
author: "Alistair Gray (Stripe Engineering)"
archived: 2026-05-27
domain: stripe.dev
published: 2026-02-09
tags: [coding-agents, agent-harness, developer-productivity, stripe, ci-cd, multi-agent]
word_count: 約 900 字
---

# Minions: Stripe's one-shot, end-to-end coding agents

> **來源**：[stripe.dev](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
> **作者**：Alistair Gray（Stripe Engineering）
> **發布日期**：2026-02-09
> **收錄日期**：2026-05-27

---

## Overview

Stripe 開發了 Minions——完全無人值守的 coding agents，每週負責處理超過 **1,000 個合併的 pull requests**，無需人類貢獻任何程式碼。Minions 代表從探索性 AI 編碼轉向企業級生產自動化的重大轉變。

## 核心能力

Minions 從任務發起到 pull request 建立，全程端對端運作。工程師可透過以下方式觸發：

- Slack
- CLI
- Web 介面
- 整合的內部應用

整個工作流程「中間不需要任何互動」——從請求到通過 CI 的 PR，完全自動。

## 為何需要自行開發

Stripe 的工程環境具有獨特挑戰：

- **程式碼規模**：數億行程式碼，主要為 Ruby（含 Sorbet 型別系統）及大量私有函式庫
- **模型不熟悉度**：標準 LLM 對 Stripe 的私有函式庫知識不足
- **品質標準極高**：程式碼每年處理超過 **1 兆美元**的支付量，容錯率極低

通用 LLM agents 難以應對需要複雜心智模型的大型成熟程式碼庫。Stripe 的解決方案是將 Minions 緊密整合至現有的開發者生產力基礎設施，而非改造外部工具。

## 技術架構

### 核心元件

| 元件 | 說明 |
|------|------|
| **Devbox 隔離環境** | 10 秒啟動，預載程式碼與服務 |
| **自訂 Orchestration** | 基於 Block 的 Goose agent framework |
| **MCP 整合** | 透過 "Toolshed" 整合 400+ 內部工具的函式呼叫 |
| **條件式規則應用** | 根據子目錄套用不同的 agent 規則 |
| **多層回饋系統** | 本地 linting（5 秒）+ 選擇性 CI 測試 + 自動測試修復 |

### 品質保證策略

Minions 強制執行「shift left」回饋原則：

1. 本地 linting 在 CI 前執行，5 秒內完成
2. 完整測試週期限制在**最多兩次**，平衡速度與完成品質
3. 失敗的執行提供後續手動迭代的起點，而非完全失敗

## 用戶體驗

工程師透過 Slack thread 與 Minions 互動，可存取包含連結文件的完整上下文。Web UI 在整個執行過程中顯示 agent 的決策與動作，讓工程師保持可見性與控制感。

## 行業意義

本文將無人值守的 coding agents 定位為從實驗性到必要基礎設施的演進，Minions 是企業規模生產就緒實作的典範案例。

---

*延伸閱讀：[Minions: Stripe's one-shot, end-to-end coding agents—Part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2)*
