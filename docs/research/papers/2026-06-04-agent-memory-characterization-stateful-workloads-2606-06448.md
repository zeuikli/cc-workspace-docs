---
url: "https://arxiv.org/abs/2606.06448"
title: "Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads"
archived_date: 2026-06-24
arxiv_id: 2606.06448
authors: ["Yasmine Omri", "Ziyu Gan", "Zachary Broveak", "Robin Geens", "Zexue He", "Alex Pentland", "Marian Verhelst", "Tsachy Weissman", "Thierry Tambe"]
domains: [cs.AI]
html: "https://arxiv.org/html/2606.06448v1"
pdf_path: pdfs/2606.06448.pdf
published_date: 2026-06-04
---

# Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

**Authors**: Yasmine Omri, Ziyu Gan, Zachary Broveak, Robin Geens, Zexue He, Alex Pentland, Marian Verhelst, Tsachy Weissman, Thierry Tambe
**Published**: June 04, 2026
**Source**: https://arxiv.org/abs/2606.06448 · [HTML](https://arxiv.org/html/2606.06448v1)
**arXiv ID**: 2606.06448
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2606.06448.pdf](https://arxiv.org/abs/2606.06448) (12 pp, full text archived)

---

## Abstract (quoted)

> LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characterization of agent memory. First, we introduce a system-oriented taxonomy classifying agent memory systems along four axes. Second, we build a phase-aware profiling harness attributing cost to construction, retrieval, and generation. Third, we characterize ten representative systems across two benchmark suites, uncovering how design choices shift cost across the write and read paths. Finally, we derive 10 system recommendations covering construction scheduling, capability floors, amortization via query volume, freshness-latency tradeoffs, and fleet-scale management.

---

## 結構化摘要

### 核心貢獻
- 首個 agent memory 的「系統層」特性刻畫（systems characterization），補足過往只談檢索精度的空白。
- 提出沿四軸分類的 system-oriented taxonomy；建構 phase-aware profiling harness，將成本歸因到 construction / retrieval / generation 三階段。
- 對 10 個代表系統、2 個 benchmark suite 做剖析，揭示設計選擇如何在 write/read path 間移轉成本。

### 關鍵結果
- 導出 10 條系統建議：construction scheduling、capability floor、以 query volume 攤銷成本、freshness-latency 取捨、fleet-scale 管理。
- 發現設計決策顯著改變 write path（建構/抽取）與 read path（檢索）的成本分佈（質性發現為主，abstract 未列單一量化主數字）。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：僅 10 系統 / 2 benchmark，泛化到更大 fleet 待驗證；建議偏經驗法則，缺正式成本模型。

---

## Workspace 關聯（評估，非既成結論）

- 「phase-aware 成本歸因（construction/retrieval/generation）」直接對應 context-management 的 token budget 與 prompt caching：寫入成本一次、讀取成本多次 → 與「以 query volume 攤銷」一致。
- 「capability floor」呼應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的「能力下限」與 model-selection-grid——記憶寫入/抽取需最低模型能力，否則 garbage in。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- ⚠️ 落地門檻：本庫無自動化 memory fleet；其 freshness-latency 取捨可作為設計 MEMORY/handoff 快取策略時的概念參考，非可直接套用的工具。
