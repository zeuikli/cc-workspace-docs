---
url: "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
title: "Effective harnesses for long-running agents"
author: "Justin Young (Anthropic)"
archived: 2026-05-27
domain: anthropic.com
published: 2025-11-26
tags: [anthropic, harness-engineering, long-running-agents, context-windows, llm-agents]
word_count: 約 1,200 字
---

# Effective harnesses for long-running agents

> **來源**：[anthropic.com](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
> **作者**：Justin Young（Anthropic）；貢獻者：David Hershey、Prithvi Rajasakeran、Jeremy Hadfield、Naia Bouscal、Michael Tingley、Jesse Mu、Jake Eaton、Marius Buleandara、Maggie Vo、Pedram Navid、Nadine Yasser、Alex Notov
> **發布日期**：2025-11-26
> **收錄日期**：2026-05-27

---

## Overview

隨著 AI agent 能力提升，開發者越來越常要求 agent 執行跨越數小時乃至數天的複雜任務，但讓 agent 在多個 context window 之間維持一致進度仍是未解難題。Anthropic 開發了一個雙 agent 架構（初始化 agent + 編碼 agent），搭配 `claude-progress.txt` 與 git history，讓 agent 在每次全新 context window 開始時能快速掌握工作狀態。關鍵洞察：**讓 agent 能快速理解工作狀態**，而非試圖延伸記憶跨越 context 邊界。

---

## 核心問題

每個新 session 都從零記憶開始，讓複雜任務的進行極為低效。文章以「輪班工程師」比喻：「每位新工程師到崗時對之前發生的事一無所知。」

---

## 解決方案：雙 Agent 架構

### 1. Initializer Agent（初始化 agent，只執行一次）

- 建立 `init.sh`：環境標準化設定腳本
- 生成 `claude-progress.txt`：session 連續性的核心文件
- 建立初始 git repository

### 2. Coding Agent（後續每個 session 使用）

- 每次只做**一個 feature 的增量進度**
- 保持程式碼整潔，方便下一個 session 接手
- 每次變更後必須 git commit 並寫下進度摘要

---

## 環境管理策略

### Feature List 框架

使用結構化 JSON 文件，記錄超過 200 個 feature 及其狀態，每個 feature 包含詳細測試步驟，標記為「passing」或「failing」——防止 agent 過早宣稱任務完成。

選用 JSON 而非 Markdown 的原因：「相比 Markdown 文件，模型較不容易不當地修改或覆蓋 JSON 文件。」

### 增量進度方法論

- 一次只處理一個 feature
- 每次變更後強制 git commit
- 撰寫清楚的進度摘要供下個 session 閱讀

### 全面測試

Claude 使用 Puppeteer 自動化工具進行 browser-based end-to-end 測試，找出純程式碼分析無法發現的 bug。若不使用自動化測試工具，Claude「會無法識別 feature 在端對端層面是否正常運作」；加入適當測試基礎設施後，「效能顯著提升」。

---

## Session 啟動流程（Getting Up to Speed）

每個 session 開始時的標準化初始化序列：

1. 確認工作目錄
2. 查閱 git history 與 progress 文件
3. 檢視 feature 需求清單
4. 啟動開發伺服器
5. 執行基本功能測試
6. 開始新的 feature 工作

---

## 常見失敗模式與解法

| 問題 | 解法 |
|------|------|
| 過早宣告專案完成 | 完整 feature list 防止誤判 |
| 進度未文件化 | Git history + progress notes 追蹤所有變更 |
| Feature 過早標記完成 | 完成前強制自我驗證 |
| 環境設定混亂 | `init.sh` 標準化設定 |

---

## 未來方向

文章提出兩個開放研究問題：

1. **多 agent 專業化**是否優於單一 agent？（例如：專屬測試 agent、QA agent、清理 agent）
2. 這些發現是否能**從 web 開發推廣**到科學研究、金融建模等其他領域？

---

## 實作資源

完整程式碼範例與實作指引可在 Claude Quickstarts GitHub repository 的 autonomous coding 專案中取得。
