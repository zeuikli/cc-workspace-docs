---
url: "https://arxiv.org/abs/2602.16873"
title: "AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence"
archived_date: 2026-06-24
arxiv_id: 2602.16873
authors: ["Geunbin Yu"]
domains: [cs.MA]
html: "https://arxiv.org/html/2602.16873v1"
pdf_path: pdfs/2602.16873.pdf
published_date: 2026-02-18
---

# AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence

**Authors**: Geunbin Yu
**Published**: February 18, 2026
**Source**: https://arxiv.org/abs/2602.16873 · [HTML](https://arxiv.org/html/2602.16873v1)
**arXiv ID**: 2602.16873
**Categories**: cs.MA
**PDF**: [research/papers/pdfs/2602.16873.pdf](https://arxiv.org/abs/2602.16873) (21 pp, full text archived)

---

## Abstract (quoted)

> As large language models from diverse providers converge toward comparable benchmark performance, the traditional paradigm of selecting a single best model per task yields diminishing returns. We argue that orchestration topology -- the structural composition of how multiple agents are coordinated, parallelized, and synthesized -- now dominates system-level performance over individual model capability. We present AdaptOrch, a formal framework for task-adaptive multi-agent orchestration that dynamically selects among four canonical topologies (parallel, sequential, hierarchical, and hybrid) based on task dependency graphs and empirically derived domain characteristics. Our framework introduces three key contributions: (1) a Performance Convergence Scaling Law, formalizing conditions under which orchestration selection outweighs model selection; (2) a Topology Routing Algorithm that maps task decomposition DAGs to optimal orchestration patterns in O(|V| + |E|) time; and (3) an Adaptive Synthesis Protocol with provable termination guarantees and heuristic consistency scoring for parallel agent outputs. We validate AdaptOrch across coding (SWE-bench), reasoning (GPQA), and retrieval-augmented generation tasks, demonstrating that topology-aware orchestration achieves 12-23% improvement over static single-topology baselines, even when using identical underlying models. Our results establish orchestration design as a first-class optimization target independent of model scaling.

---

## 結構化摘要

### 核心貢獻
- 提出 **AdaptOrch**：task-adaptive multi-agent orchestration 形式化框架，依 task dependency graph 與經驗推導的 domain 特徵，在四種 canonical topology（parallel / sequential / hierarchical / hybrid）間動態選路。
- **Performance Convergence Scaling Law**：形式化「當各家 LLM benchmark 表現收斂時，orchestration 選擇的邊際效益超過 model 選擇」的成立條件。
- **Topology Routing Algorithm**：將 task decomposition DAG 映射到最佳 orchestration pattern，複雜度 O(|V| + |E|)（對節點數 + 邊數線性）。
- **Adaptive Synthesis Protocol**：對 parallel agent 輸出做合成，具 provable termination guarantee 與 heuristic consistency scoring。
- 核心論點：orchestration design 應視為獨立於 model scaling 的 first-class 最佳化目標。

### 關鍵結果
- 跨 coding（SWE-bench）、reasoning（GPQA）、RAG 三類任務驗證。
- topology-aware orchestration 相較 static single-topology baseline 取得 **12–23% 提升**，且在使用相同底層 model 時仍成立（提升來自拓撲而非模型能力）。
- Routing 演算法線性時間 O(|V| + |E|)；Synthesis Protocol 具 termination 保證。

### 限制
文件未列明確 limitation 章節（僅依 abstract 判讀）。基於 abstract 的弱點推測：
- consistency scoring 為 **heuristic**，非保證最佳，跨 domain 穩健性存疑。
- 12–23% 區間跨度大，未見各 benchmark 個別拆解與變異數，泛化性待原文確認。
- 單一作者、未提供 baseline 對手實作細節與成本/延遲開銷（orchestration 本身有 coordination overhead）。
- 「收斂」前提依賴特定時點的 model 對等假設，模型代際更替時是否仍成立未明。

---

## Workspace 關聯（評估，非既成結論）

- 與本 workspace `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的 **Fan-out（上限 4）** 與 **Hierarchical 拓撲** 概念直接對應；AdaptOrch 的四 topology 分類可作為「何時 parallel vs sequential vs hierarchical」的決策依據參考。⚠️ 落地門檻：本框架需 task DAG 顯式分解，現行委派多靠啟發式判斷，導入需先建立 dependency graph 抽取步驟。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **Adaptive Synthesis Protocol（parallel 輸出合成 + consistency scoring）** 對應 The Loop 的 `unverified_success` 閘門與「多 agent 輸出矛盾明列交主對話」紀律；可借其 consistency scoring 思路強化 child 輸出仲裁。⚠️ 但論文用 heuristic scoring，本 workspace 要求機械驗證（grep/test），不可直接以 heuristic 取代確定性 gate。
- **Performance Convergence Scaling Law** 與 pilot 模式的 model 選擇（haiku/sonnet/opus/fable）形成張力：論文主張模型收斂後拓撲 > 模型，可作為「effort 先於 model」原則的外部佐證。⚠️ 仍須以本地 eval 驗證，不可照搬論文 12–23% 數字。
- Topology Routing 的 O(|V|+|E|) 路由屬「確定性 decide」範疇（路由由代碼決定，非 LLM 自決），符合本 workspace「判斷 vs 決定」分工；概念上可對接 `multi-mode` 自動路由設計。
