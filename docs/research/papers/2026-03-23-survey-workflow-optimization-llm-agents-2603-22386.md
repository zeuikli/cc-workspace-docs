---
url: "https://arxiv.org/abs/2603.22386"
title: "From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2603.22386
authors: ["Ling Yue", "Kushal Raj Bhandari", "Ching-Yun Ko", "Dhaval Patel", "Shuxin Lin", "Nianjun Zhou", "Jianxi Gao", "Pin-Yu Chen", "Shaowu Pan"]
domains: [cs.AI]
html: "https://arxiv.org/html/2603.22386v1"
pdf_path: pdfs/2603.22386.pdf
published_date: 2026-03-23
---

# From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents

**Authors**: Ling Yue, Kushal Raj Bhandari, Ching-Yun Ko, Dhaval Patel, Shuxin Lin, Nianjun Zhou, Jianxi Gao, Pin-Yu Chen, Shaowu Pan
**Published**: March 23, 2026
**Source**: https://arxiv.org/abs/2603.22386 · [HTML](https://arxiv.org/html/2603.22386v1)
**arXiv ID**: 2603.22386
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2603.22386.pdf](https://arxiv.org/abs/2603.22386) (31 pp, full text archived)

---

## Abstract (quoted)

> Large language model (LLM)-based systems are becoming increasingly popular for solving tasks by constructing executable workflows that interleave LLM calls, information retrieval, tool use, code execution, memory updates, and verification. This survey reviews recent methods for designing and optimizing such workflows, which we treat as agentic computation graphs (ACGs). We organize the literature based on when workflow structure is determined, where structure refers to which components or agents are present, how they depend on each other, and how information flows between them. This lens distinguishes static methods, which fix a reusable workflow scaffold before deployment, from dynamic methods, which select, generate, or revise the workflow for a particular run before or during execution. We further organize prior work along three dimensions: when structure is determined, what part of the workflow is optimized, and which evaluation signals guide optimization (e.g., task metrics, verifier signals, preferences, or trace-derived feedback). We also distinguish reusable workflow templates, run-specific realized graphs, and execution traces, separating reusable design choices from the structures actually deployed in a given run and from realized runtime behavior. Finally, we outline a structure-aware evaluation perspective that complements downstream task metrics with graph-level properties, execution cost, robustness, and structural variation across inputs. Our goal is to provide a clear vocabulary, a unified framework for positioning new methods, a more comparable view of existing body of literature, and a more reproducible evaluation standard for future work in workflow optimizations for LLM agents.

---

## 結構化摘要

### 核心貢獻
- 提出 **agentic computation graphs (ACGs)** 統一抽象：把 LLM 工作流（LLM calls、retrieval、tool use、code execution、memory updates、verification 的交織）視為可優化的計算圖。
- 核心分類軸 = **「workflow structure 何時被決定」**：區分 **static methods**（部署前固定可重用 scaffold）vs **dynamic methods**（執行前或執行中為單次 run 選擇/生成/修訂 workflow）。對應標題 "Static Templates → Dynamic Runtime Graphs"。
- 三維 taxonomy：(1) **when** structure 被決定；(2) **what part** of the workflow 被優化；(3) **which evaluation signals** 引導優化（task metrics / verifier signals / preferences / trace-derived feedback）。
- 三層結構分離：**reusable workflow templates**（可重用設計選擇）／ **run-specific realized graphs**（單次 run 實際部署結構）／ **execution traces**（實際 runtime 行為）。
- 提出 **structure-aware evaluation** 視角：在 downstream task metrics 之外，補上 graph-level properties、execution cost、robustness、跨 input 的結構變異。

### 關鍵結果
（survey 性質，無單一量化 benchmark；以涵蓋範圍與框架維度為主）
- **涵蓋範圍**：LLM agent workflow 的設計與優化方法綜述，31 頁。
- **分類維度**：static/dynamic（時間軸）× 優化標的（what）× 評估訊號（signal）× 三層結構抽象（template / realized graph / trace）。
- **主要發現/主張**：現有文獻缺乏共通詞彙與可比框架；以「structure 何時/何處被決定」為 lens 可統一定位新舊方法，並提出更可重現的 evaluation 標準。

### 限制
- 文件未列明確 limitation 章節（abstract 未自述弱點）。判斷的弱點：
  - survey 快照性質，LLM agent 領域迭代極快，taxonomy 易隨新方法過時。
  - ACG 抽象偏概念框架，abstract 未承諾統一 empirical benchmark 或可執行的 evaluation harness，可比性主張仍待社群採用驗證。
  - 「structure-aware evaluation」為提出的視角而非標準化工具，落地需後續工作。

---

## Workspace 關聯（評估，非既成結論）

- **dynamic workflow 紀律直接對映**：本 survey 的 static→dynamic 軸與 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的 dynamic workflow 三失敗模式（agentic laziness / self-preferential bias / goal drift）同源；ACG 的「run-specific realized graph vs trace」分離，呼應 workspace 對 fan-out 拓撲與 verdict 機械重驗的要求。⚠️ 落地門檻：survey 為概念框架，無現成可套用的圖優化實作。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **structure-aware evaluation ↔ The Loop TEST 階段**：論文主張在 task metric 外補 execution cost / robustness / graph-level properties，與 core.md `unverified_success` 閘門（確定性 gate 不經 sub-agent 中介）方向一致；可作為設計 healthcheck 評估維度的參考。⚠️ 需自行轉譯為可機械驗證條件。
- **三層結構抽象 ↔ 委派契約**：template / realized graph / trace 的分離，類比 Handoff Contract（綁定 mode/model）與實際 sub-agent 執行軌跡；對「parent 綁定、child 不自切」的拓撲規則提供理論詞彙。⚠️ 屬概念啟發，非可導入的工具或檔案。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **適合作為 research 背景文獻**，非可立即落地的工程資產；可在後續設計 multi-agent coordinator pattern 時引用其 taxonomy 詞彙。
