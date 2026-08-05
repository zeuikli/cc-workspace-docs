---
url: "https://arxiv.org/abs/2606.22741"
title: "GRADE: Graph Representation of LLM Agent Dependency and Execution"
archived_date: 2026-07-18
arxiv_id: 2606.22741
authors: ["Yue Zhao"]
pdf_path: pdfs/2606.22741.pdf
published_date: 2026-06-22
---

# GRADE: Graph Representation of LLM Agent Dependency and Execution

**Authors**: Yue Zhao
**Published**: June 2026
**Source**: https://arxiv.org/abs/2606.22741
**arXiv ID**: 2606.22741
**Categories**: Computer Science > Machine Learning (cs.LG)
**PDF**: [research/papers/pdfs/2606.22741.pdf](https://arxiv.org/abs/2606.22741)

---

## Abstract

The paper addresses whether a single graph structure can represent all varieties of LLM agent executions. Traditional traces document execution order but omit dependency information. GRADE introduces a dual-layer graph model featuring execution edges (recording step sequence) and dependency edges (capturing what each step relied upon). These dependencies are graded based on visibility—whether known, observed, declared, or inferred. Evaluation across six LLM agent datasets spanning tool use, coding, and web interaction demonstrates that the dependency layer identifies failures better than execution complexity alone. Under cross-corpus testing, the dependency layer maintains performance on unseen categories while simpler metrics fail. Additionally, the execution layer can pinpoint which step caused failure in multi-agent runs. The research includes analysis of why standard graph neural networks underperform with the dependency layer compared to feature-based alternatives, offering broader applications for optimization and debugging.

---

## Core Thesis

- 傳統執行軌跡（trace）只記錄步驟順序，遺失「這一步依賴了什麼」的資訊；GRADE 提出雙層圖模型：execution edge（步驟序列）+ dependency edge（依賴關係，並依可見度分級為 known/observed/declared/inferred）。
- 六個涵蓋工具使用、程式碼、網頁互動的 agent 資料集上驗證：dependency 層比單純執行複雜度更能定位失敗；跨語料測試中，dependency 層在未見過的任務類別上仍保持效能，而較簡單指標則失效。
- execution 層可在多代理執行中精確定位是哪一步造成失敗；文中並分析標準圖神經網路為何在 dependency 層表現不如特徵導向替代方案。
- **Workspace 關聯**：與 core.md RECORD 章「失敗歸因到層」精神一致——GRADE 提供把「執行順序」與「依賴關係」分離建模的具體資料結構，可作為未來設計 fan-out/多 sub-agent 失敗歸因（"是哪個 child 的輸出污染了 parent 決策"）的技術參考。
