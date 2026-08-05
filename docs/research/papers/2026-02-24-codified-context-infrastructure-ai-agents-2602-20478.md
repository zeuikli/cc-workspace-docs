---
url: "https://arxiv.org/abs/2602.20478"
title: "Codified Context: Infrastructure for AI Agents in a Complex Codebase"
arxiv_id: 2602.20478
collected_at: 2026-08-03
collected_by: routine-d
domain: Context Engineering
pdf_path: pdfs/2602.20478.pdf
year: 2026
---

# Codified Context: Infrastructure for AI Agents in a Complex Codebase

## 摘要 / 核心貢獻

LLM-based 程式協作助理難以跨 session 維持記憶，經常遺失專案慣例並重複犯錯。本文針對一個
10.8 萬行的大型 C# 分散式系統，提出三段式基礎設施框架：(1) 「hot-memory constitution」
收錄慣例與檢索協定，(2) 十九個專職 domain-expert agent，(3) 「cold-memory knowledge base」
內含三十四份可依需求調閱的規格文件。論文分析 283 次開發 session 的指標，並以四個案例研究
展示 codified context 如何在各自獨立的工作 session 間維持一致性、避免失誤重演。該框架已
開源並附文件。

## 與 Harness 的關聯

本文的 hot-memory constitution / cold-memory knowledge base 二分，與本 workspace
CLAUDE.md（穩定前綴、auto-load）+ `.claude/refs/`（按需讀取）的 progressive disclosure
架構高度同構，等於是「codified context」設計在另一個大型 codebase 上的獨立驗證；其
283-session 實測數據為本庫「結構性下沉優先於壓縮」的設計選擇提供外部佐證。
