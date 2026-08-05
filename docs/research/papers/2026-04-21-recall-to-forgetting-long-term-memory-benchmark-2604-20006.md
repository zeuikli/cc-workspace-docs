---
url: "https://arxiv.org/abs/2604.20006"
title: "From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents"
archived_date: 2026-06-24
arxiv_id: 2604.20006
authors: ["Md Nayem Uddin", "Kumar Shubham", "Eduardo Blanco", "Chitta Baral", "Gengyu Wang"]
domains: [cs.CL]
html: "https://arxiv.org/html/2604.20006v1"
pdf_path: pdfs/2604.20006.pdf
published_date: 2026-04-21
---

# From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents

**Authors**: Md Nayem Uddin, Kumar Shubham, Eduardo Blanco, Chitta Baral, Gengyu Wang
**Published**: April 21, 2026
**Source**: https://arxiv.org/abs/2604.20006 · [HTML](https://arxiv.org/html/2604.20006v1)
**arXiv ID**: 2604.20006
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2604.20006.pdf](https://arxiv.org/abs/2604.20006) (28 pp, full text archived)

---

## Abstract (quoted)

> Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change. However, existing benchmarks predominantly frame long-term memory evaluation as fact retrieval from past conversations, providing limited insight into agents' ability to consolidate memory over time or handle frequent knowledge updates. We introduce Memora, a long-term memory benchmark spanning weeks to months long user conversations. The benchmark evaluates three memory-grounded tasks: remembering, reasoning, and recommending. To ensure data quality, we employ automated memory-grounding checks and human evaluation. We further introduce Forgetting-Aware Memory Accuracy (FAMA), a metric that penalizes reliance on obsolete or invalidated memory when evaluating long-term memory. Evaluations of four LLMs and six memory agents reveal frequent reuse of invalid memories and failures to reconcile evolving memories. Memory agents offer marginal improvements, exposing shortcomings in long-term memory for personalized agents.

---

## 結構化摘要

### 核心貢獻
- 提出 Memora：跨「數週到數月」對話的長期記憶 benchmark，評測三類 memory-grounded 任務——remembering、reasoning、recommending。
- 提出 FAMA（Forgetting-Aware Memory Accuracy）指標：對「依賴過時/已失效記憶」加以懲罰，超越單純 fact retrieval 的評估框架。
- 以 automated memory-grounding check + 人工評估保證資料品質。

### 關鍵結果
- 評測 4 個 LLM + 6 個 memory agent：普遍發現「重複使用無效記憶」與「無法調和演變中的記憶」。
- memory agent 僅帶來邊際改善，暴露 personalized agent 長期記憶的根本缺陷。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：benchmark 規模/語言覆蓋未在 abstract 量化；FAMA 對「obsolete」的界定依賴標註，可能引入主觀性。

---

## Workspace 關聯（評估，非既成結論）

- FAMA「懲罰沿用失效記憶」直接對應 core.md RECORD 與本庫 MEMORY/LESSONS 的核心風險：compact 後沿用過時決策 → context collapse；呼應 context-management「compact 後自檢③ 最近工具結果未失真」。
- 「無法調和演變中的記憶」對應 2606.09483 的 belief revision／supersedes chain——本批論文共同指向「記憶需可失效、可覆寫」。
- ⚠️ 落地門檻：本庫無自動 forgetting 機制；可作為設計 memory-compactor 整合 gate 時「過時資訊偵測」的評估視角，非現成指標實作。
