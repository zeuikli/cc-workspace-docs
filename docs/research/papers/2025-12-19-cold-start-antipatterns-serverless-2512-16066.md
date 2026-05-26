---
url: "https://arxiv.org/abs/2512.16066"
title: "Cold-Start Anti-Patterns and Refactorings in Serverless Systems: An Empirical Study"
date: 2025-12-18
arxiv: 2512.16066
authors: "Syed Salauddin Mohammad Tariq, Foyzul Hassan, Amiangshu Bosu, Probir Roy (University of Michigan–Dearborn, Wayne State)"
pdf: 2025-12-19-cold-start-antipatterns-serverless-2512-16066.pdf
relevance: 間接但概念強相關 — 把 cold-start 當 developer-visible 設計問題（非黑盒），直接對應 hook spawn 反模式
topic: cold-start anti-patterns / developer-visible design problem
venue: "IEEE SANER 2026 (accepted, preprint)"
---

# Cold-Start Anti-Patterns and Refactorings in Serverless Systems

## 核心論點
與多數視 cold-start 為黑盒最佳化的前作不同，本文把 cold start 當作 **developer-visible design problem**（開發者可見的設計問題）。從 **81 個 adjudicated issue reports**（跨開源 serverless 專案）推導初始化反模式的分類學（taxonomy），涵蓋 design / packaging / runtime 三層。

## 商業動機（關鍵引用）
- **Amazon：每多 100ms 延遲 -> 損失 1% 銷售**
- **Google：回應時間增至 500ms -> 搜尋流量降 20%**
- 冷啟動延遲源自跨多抽象層（import graphs -> packaging -> runtime -> environment）

## 反模式分類（developer-visible，performance 而非 correctness 缺陷）
1. **Redundant library imports**（冗餘 library 匯入）
2. **Deferred one-time initialization**（一次性初始化未前置/未快取）
3. **Unnecessary packaging of large dependencies**（大型相依不必要打包）

## 工具與成果
- **SCABench**：可重現 benchmark
- **InitScope**：輕量分析框架，連結「what code is *loaded*」與「what is *executed*」
- InitScope 定位準確度 **提升 40%**，診斷工作量 **減少 64%**（vs prior tools）

## 對 cc-workspace 的遷移啟示（直接對應）
- **Redundant imports** -> 18 個 hook scripts 中，每次工具呼叫都 spawn 的 hook（block-dangerous.sh 53ms/call）= 重複 init 成本
- **Deferred one-time init** -> session-init.sh 592ms（含 git fetch）應快取 / 前置 / async
- **InitScope「loaded vs executed」** -> auto-load 16,927 bytes 中有多少在每個 session 真正被引用？= 本研究 gap-map 同精神
- 核心遷移：**冷啟動是可被靜態分析與重構的設計問題**，不是不可控的固定成本
