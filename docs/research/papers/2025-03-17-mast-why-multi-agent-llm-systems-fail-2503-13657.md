---
url: "https://arxiv.org/abs/2503.13657"
title: "Why Do Multi-Agent LLM Systems Fail?"
archived_date: 2026-06-09
arxiv_id: 2503.13657
authors: ["Mert Cemri", "Melissa Z. Pan", "Shuyi Yang", "Lakshya A. Agrawal", "Bhavya Chopra", "Rishabh Tiwari", "Kurt Keutzer", "Aditya Parameswaran", "Dan Klein", "Kannan Ramchandran", "Matei Zaharia", "Joseph E. Gonzalez", "Ion Stoica"]
domains: [cs.AI, cs.MA, cs.CL]
pdf_path: pdfs/2503.13657.pdf
published_date: 2025-03-17
tags: [multi-agent, failure-taxonomy, mast, benchmark, reliability, llm]
venue: "NeurIPS 2025 Datasets & Benchmarks"
---

# Why Do Multi-Agent LLM Systems Fail?

**arXiv**: 2503.13657 | **發表**: 2025-03-17 | **PDF**: 2025-03-17-mast-why-multi-agent-llm-systems-fail-2503-13657.pdf

## 核心貢獻

UC Berkeley 等提出 **MAST（Multi-Agent System Failure Taxonomy）**：首個實驗性多 agent 失敗模式分類框架。分析 7 個主流 MAS 框架（AutoGen、CrewAI、LangGraph 等）× 200+ 任務，人工標注 150 條 traces，歸納 14 個失敗模式，inter-annotator agreement κ = 0.88。NeurIPS 2025 Datasets & Benchmarks Track。

## 方法 / 架構

- **MAST-Data**：1,600+ 標注 traces，跨 7 個框架 × 多模型（GPT-4、Claude 3、Qwen2.5、CodeLlama）× 三類任務（coding、math、general agent）
- **14 種失敗模式**，分三大類：
  - **(i) Specification Issues**：任務規格不清、工具描述錯誤、角色定義歧義
  - **(ii) Inter-Agent Misalignment**：agent 間目標不一致、資訊傳遞失真、責任歸屬不明
  - **(iii) Task Verification**：無法判斷任務完成狀態、幻覺式自我報告完成
- **LLM-as-Judge pipeline**：可自動標注新 traces，驗證與人工標注高度一致
- **Improvement Headroom 分析**：每個失敗模式標注潛在提升空間，作為設計優先順序依據

## 關鍵發現與數據

- 7 個框架在 benchmark 上的提升相對單 agent **常常很小甚至為負**，揭示 MAS 效能增益被誇大
- Task Verification 是最難自動修復的類別：agent 無法可靠判斷自己是否完成任務
- Inter-Agent Misalignment 在 hierarchical 架構中特別顯著（coordinator 與 worker 目標漂移）
- 跨框架、跨模型、跨任務類型，失敗分佈高度一致，表明問題是結構性而非模型特定

## 對 agent-team 設計的啟示

1. **Specification 品質是 MAS 天花板**：工具描述、角色定義、任務分解的歧義度直接決定失敗率，在設計階段解決比 agent 數量更重要
2. **需要外部 verification oracle**：agent 自我報告「完成」不可信（對應 R4 完成條件必須可機械驗證）
3. **inter-agent misalignment 在 hierarchical 架構是系統性風險**：coordinator 指令需要 structured handoff + confirmation，不能依賴 agent 自行解讀

## 原文關鍵引用（≤150字）

> "Despite growing enthusiasm, performance gains on popular benchmarks often remain minimal compared with single-agent frameworks... We develop MAST, the first empirically grounded taxonomy for understanding MAS failures. MAST was developed through rigorous analysis of 150 traces, guided closely by expert human annotators and validated by high inter-annotator agreement (κ = 0.88). We identify 14 unique failure modes organized into 3 overarching categories: specification issues, inter-agent misalignment, and task verification."
