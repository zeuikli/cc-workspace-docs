---
url: "https://arxiv.org/abs/2605.06365"
title: "From Agent Loops to Deterministic Graphs: Execution Lineage for Reproducible AI-Native Work"
archived_date: 2026-07-18
arxiv_id: 2605.06365
authors: ["Josh Rosen", "Seth Rosen"]
pdf_path: pdfs/2605.06365.pdf
published_date: 2026-05-07
---

# From Agent Loops to Deterministic Graphs: Execution Lineage for Reproducible AI-Native Work

**Authors**: Josh Rosen, Seth Rosen
**Published**: May 2026
**Source**: https://arxiv.org/abs/2605.06365
**arXiv ID**: 2605.06365
**Categories**: Artificial Intelligence (cs.AI); Multiagent Systems (cs.MA); Software Engineering (cs.SE)
**PDF**: [research/papers/pdfs/2605.06365.pdf](https://arxiv.org/abs/2605.06365)

---

## Abstract

Large language model systems are increasingly deployed as agentic workflows that interleave reasoning, tool use, memory, and iterative refinement. These systems are effective at producing answers, but they often rely on implicit conversational state, making it difficult to preserve stable work products, isolate irrelevant updates, or propagate changes through intermediate artifacts. The authors introduce execution lineage: an execution model representing AI-native work as a directed acyclic graph of artifact-producing computations with explicit dependencies, stable intermediate boundaries, and identity-based replay. Their goal is enhancing maintainability of evolving AI-generated work rather than improving single-pass generation. Comparing execution-lineage replay against loop-centric baselines on policy-memo update tasks, the DAG approach preserved final outputs precisely while preventing unrelated context contamination. In intermediate-artifact edits, only DAG replay achieved perfect upstream preservation, downstream propagation, and cross-artifact consistency. The research demonstrates that final output quality and maintained-state quality represent distinct objectives, with execution lineage providing superior guarantees about what changes, what remains constant, and how work evolves across revisions.

---

## Core Thesis

- 指出主流「agent loop」（隱式對話狀態不斷疊代）的結構性弱點：難以保留穩定工作產物、難以隔離無關更新、難以把變更正確傳播到中間產物。
- 提出 execution lineage：把 AI-native 工作表示成有向無環圖（DAG），節點是產出 artifact 的計算，具備顯式依賴、穩定的中間邊界、以身分（identity）為基礎的重放（replay）能力。
- 目標不是改善單次生成品質，而是改善「持續演化中的 AI 產物」的可維護性——這是與「最終輸出品質」不同的獨立目標。
- 在政策備忘錄更新任務上，DAG replay 相較 loop-centric baseline 精確保留最終輸出、避免無關 context 污染；中間產物編輯場景下，只有 DAG replay 做到上游保留、下游傳播、跨產物一致性三者兼顧。
- **Workspace 關聯**：與本庫已收錄的 agent-loops-to-graphs-2604-11378（scheduler-theoretic DAG 框架）主題呼應但切入點不同——本文聚焦「可維護性/可重放性」而非「終止保證」，對 Implementation Notes / handoff 交接文件的「哪些狀態該保持不變、哪些該隨修訂演化」設計提供概念工具。
