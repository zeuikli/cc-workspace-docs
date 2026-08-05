---
url: "https://arxiv.org/abs/2604.03143"
title: "TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing"
archived_date: 2026-06-24
arxiv_id: 2604.03143
authors: ["Zhuohang Bian", "Feiyang Wu", "Chengrui Zhang", "Hangcheng Dong", "Yun Liang", "Youwei Zhuo"]
domains: [cs.DC, "KV cache"]
html: "https://arxiv.org/html/2604.03143v1"
pdf_path: pdfs/2604.03143.pdf
published_date: 2026-04-03
---

# TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing

**Authors**: Zhuohang Bian, Feiyang Wu, Chengrui Zhang, Hangcheng Dong, Yun Liang, Youwei Zhuo
**Published**: April 03, 2026
**Source**: https://arxiv.org/abs/2604.03143 · [HTML](https://arxiv.org/html/2604.03143v1)
**arXiv ID**: 2604.03143
**Categories**: cs.DC, KV cache
**PDF**: [research/papers/pdfs/2604.03143.pdf](https://arxiv.org/abs/2604.03143) (14 pp, full text archived)

---

## Abstract (quoted)

> Multi-agent LLM applications organize execution in synchronized rounds where a central scheduler gathers outputs from all agents and redistributes the combined context. This All-Gather communication pattern creates massive KV Cache redundancy, because every agent's prompt contains the same shared output blocks, yet existing reuse methods fail to exploit it efficiently. We present TokenDance, a system that scales the number of concurrent agents by exploiting the All-Gather pattern for collective KV Cache sharing. TokenDance's KV Collector performs KV Cache reuse over the full round in one collective step, so the cost of reusing a shared block is paid once regardless of agent count. Its Diff-Aware Storage encodes sibling caches as block-sparse diffs against a single master copy, achieving 11-17x compression on representative workloads. Evaluation on GenerativeAgents and AgentSociety shows that TokenDance supports up to 2.7x more concurrent agents than vLLM with prefix caching under SLO requirement, reduces per-agent KV Cache storage by up to 17.5x, and achieves up to 1.9x prefill speedup over per-request position-independent caching.

---

## 結構化摘要

### 核心貢獻

- **TokenDance 系統**：針對 multi-agent LLM serving 設計，利用 All-Gather 通訊模式中固有的 KV Cache 冗餘，透過集體共享大幅降低記憶體用量。
- **KV Collector**：以單次集體步驟完成一個 round 內全部 agent 的 KV Cache 複用，共享 block 的成本只付一次，與 agent 數量無關（O(1) 而非 O(N)）。
- **Diff-Aware Storage**：將 sibling cache 編碼為相對 master copy 的 block-sparse diff，而非儲存完整副本，對代表性 workload 達到 11–17x 壓縮比。
- 明確針對 synchronized round 架構（central scheduler → All-Gather → redistribute）而設計，填補現有 prefix caching 無法有效利用此模式的空缺。

### 關鍵結果

- **並發 agent 容量**：比 vLLM with prefix caching 支援多達 **2.7x** 的並發 agent 數（在同等 SLO 限制下）。
- **KV Cache 儲存量**：每 agent 降低最高 **17.5x**。
- **Prefill 加速**：相較 per-request position-independent caching 達 **1.9x** prefill speedup。
- Benchmark：GenerativeAgents 與 AgentSociety 兩個代表性多 agent 模擬 workload。

### 限制

- 設計假設 synchronized round（All-Gather 模式）；非同步或異質 agent 拓撲（如 fan-out DAG、event-driven）能否直接受益未在論文中討論。
- Diff-Aware Storage 壓縮率依賴 sibling cache 相似度；若 agent 的 prompt 分歧度高，壓縮收益可能下降——論文未量化分歧閾值。
- 評估侷限於 GenerativeAgents / AgentSociety，尚未涵蓋非模擬類多 agent 任務（如 coding agent、tool-use agent）。

---

## Workspace 關聯（評估，非既成結論）

- **`core.md §PROPOSE 委派`（原 subagent-strategy.md）（fan-out / All-Gather 等價）**：`core.md §PROPOSE 委派` 的 fan-out 模式（parent → N child → 結果聚回 parent）在結構上對應 TokenDance 所描述的 All-Gather 通訊輪。TokenDance 的 KV Collector 概念暗示：若 workspace 的 fan-out agent 共用大量 system prompt/context，在 inference 層做集體 KV 共享可顯著降低成本，是 subagent fan-out 的基礎設施層優化方向。
- **context-management（NLAH / prompt caching / token budget）**：`context-management.md` 強調 prompt caching 的 cache_read/input_tokens 比率健康度。TokenDance 的 Diff-Aware Storage 是 prefix caching 的進化版，針對多 agent 共享 context block 場景補足了 per-request prefix cache 的盲點；可作為評估現有 prompt caching 效率瓶頸的理論參照。
- **unverified_success 閘門（core.md TEST）**：本論文評估基於 GenerativeAgents / AgentSociety 模擬 workload；若欲將 TokenDance 概念應用於 workspace 的 agentic 系統，須以真實 workload 重新驗證壓縮率，不可直接援引論文數字作為 verified 結果（⚠️ simulation workload ≠ production workload）。
- **⚠️ 落地門檻**：TokenDance 為 LLM serving infra 層方案（修改 vLLM scheduler + KV storage），workspace 現行 subagent 運行於 Claude API 層，無法直接控制 KV Cache 分配；此論文的實用性目前偏向**架構設計參照**而非可直接部署的工具。
