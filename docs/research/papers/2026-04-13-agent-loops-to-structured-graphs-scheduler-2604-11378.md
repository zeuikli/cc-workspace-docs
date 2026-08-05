---
url: "https://arxiv.org/abs/2604.11378"
title: "From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution"
archived_date: 2026-06-24
arxiv_id: 2604.11378
authors: ["Hu Wei"]
domains: [cs.AI]
html: "https://arxiv.org/html/2604.11378v1"
pdf_path: pdfs/2604.11378.pdf
published_date: 2026-04-13
---

# From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution

**Authors**: Hu Wei
**Published**: April 13, 2026
**Source**: https://arxiv.org/abs/2604.11378 · [HTML](https://arxiv.org/html/2604.11378v1)
**arXiv ID**: 2604.11378
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2604.11378.pdf](https://arxiv.org/abs/2604.11378) (50 pp, full text archived)

---

## Abstract (quoted)

> The dominant paradigm for building LLM based agents is the Agent Loop, an iterative cycle where a single language model decides what to do next by reading an ever growing context window. This paradigm has three structural weaknesses: implicit dependencies between steps, unbounded recovery loops, and mutable execution history that complicates debugging. We characterize the Agent Loop as a single ready unit scheduler: at any moment, at most one executable unit is active, and the choice of which unit to activate comes from opaque LLM inference rather than an inspectable policy. This perspective places Agent Loops and graph based execution engines on a single semantic continuum. We propose SGH, Structured Graph Harness, which lifts control flow from implicit context into an explicit static DAG. SGH makes three commitments: execution plans are immutable within a plan version, planning execution and recovery are separated into three layers, and recovery follows a strict escalation protocol. These choices trade some expressiveness for controllability, verifiability, and implementability. Our contributions are fourfold: a scheduler unified framework that applies classical scheduling theory to LLM agent execution and identifies challenges introduced by non deterministic LLM nodes; a trade off analysis of controllability, expressiveness, and implementability across 70 surveyed systems; a formal specification including a node state machine with termination and soundness guarantees; and an attributable experimental framework with a seven group design for future validation. This is a position paper and design proposal. We provide a theoretical framework, design analysis, and experimental protocol, not a production implementation or empirical results.

---

## 結構化摘要

### 核心貢獻
- 提出 **scheduler-unified framework**：把 classical scheduling theory 套到 LLM agent 執行，並指出 non-deterministic LLM node 帶來的新挑戰。
- 將 **Agent Loop** 重新刻畫為 *single ready-unit scheduler*——任一時刻至多一個 executable unit 為 active，且「下一步選誰」由 opaque LLM inference 而非可檢視的 policy 決定；由此把 Agent Loop 與 graph-based execution engine 放在同一 semantic continuum 上。
- 提出 **SGH (Structured Graph Harness)**：把 control flow 從 implicit context 提升為 explicit static DAG，三項 commitment——plan 在版本內 immutable、planning / execution / recovery 三層分離、recovery 走 strict escalation protocol。
- 給出 **formal specification**：含 node state machine，附 termination 與 soundness guarantee。
- 設計 **attributable experimental framework**：seven-group design，供後續 validation。

### 關鍵結果
- 屬 position paper / design proposal，**無 empirical results**（作者明示）。
- 量化面僅有：橫跨 **70 個 surveyed systems** 的 controllability / expressiveness / implementability trade-off 分析。
- 方法層發現：明確指出 Agent Loop 三大結構弱點——implicit dependencies between steps、unbounded recovery loops、mutable execution history（debug 困難）；SGH 以 expressiveness 換取 controllability / verifiability / implementability。

### 限制
- 作者自述：**This is a position paper and design proposal**，提供 theoretical framework / design analysis / experimental protocol，**非 production implementation、亦無 empirical results**。
- 判斷弱點：seven-group experimental design 僅為 protocol，未跑；SGH 的 static DAG 假設可能不適合高度 open-ended、需動態重規劃的任務（immutable plan 與真實 agent 探索性需求之間的張力未經實證檢驗）；single-author position paper，trade-off 結論依賴 survey 詮釋而非對照實驗。

---

## Workspace 關聯（評估，非既成結論）

- 本論文把 Agent Loop 形式化為「single ready-unit scheduler + opaque policy」，與本 workspace 的 **The Loop**（OBSERVE→…→RECORD 六階段）形成對照：The Loop 已把「下一步選誰」用可機械驗證的成功條件外顯化，正是 SGH 主張的「lift control flow into inspectable policy」方向。⚠️ 落地門檻：本 repo 的階段是 advisory prompt 規則，非 static DAG runtime，無 termination/soundness guarantee。
- SGH 的 *planning / execution / recovery 三層分離* 對應 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的 parent↔child 拓撲與 `error-handling.md` 的控制語義；可作為「dynamic workflow 三失敗模式（laziness / self-preferential bias / goal drift）」的理論補強。⚠️ 論文無實作，無法直接驗證能否抑制 goal drift。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- *strict escalation protocol* 概念與 `self-escalate` agent（≥3 次同問失敗 → escalate 非 retry）同源，可借其 node state machine 形式化現有升級鏈。⚠️ 需自行把 prompt 級規則映射到狀態機，非現成模組。
- *immutable plan version* 與本 workspace 「commit 原子性 / 不可逆 gate」哲學一致；但 ⚠️ 對 off-rails 探索性任務，immutable DAG 可能與 IDENTIFY 階段的 open-question 動態調整衝突，採用前須評估任務是否真為 static-planable。
