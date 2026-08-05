---
url: "https://arxiv.org/abs/2606.23961"
title: "Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets"
archived_date: 2026-06-24
arxiv_id: 2606.23961
authors: ["Duc Duong", "Hoang Anh Duy Le", "Jianwen Xie", "Anshumali Shrivastava", "Zhaozhuo Xu"]
domains: [cs.LG, "KV cache"]
html: "https://arxiv.org/html/2606.23961v1"
pdf_path: pdfs/2606.23961.pdf
published_date: 2026-06-22
---

# Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets

**Authors**: Duc Duong, Hoang Anh Duy Le, Jianwen Xie, Anshumali Shrivastava, Zhaozhuo Xu
**Published**: June 22, 2026
**Source**: https://arxiv.org/abs/2606.23961 · [HTML](https://arxiv.org/html/2606.23961v1)
**arXiv ID**: 2606.23961
**Categories**: cs.LG, KV cache
**PDF**: [research/papers/pdfs/2606.23961.pdf](https://arxiv.org/abs/2606.23961) (21 pp, full text archived)

---

## Abstract (quoted)

> Long-context and agentic LLM workloads push the KV cache past any fixed memory budget, forcing the inference stack to permanently evict tokens at every step of a continuous-inference stream. Existing methods all share the same template, a per-step direct-attention score followed by deterministic top-K selection, which converts a single below-cutoff step into an irreversible verdict and permanently erases any subtly important token that direct attention cannot single out from noise. To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-K. Theoretically, we show that Nexus Sampling dominates deterministic top-K in long-run survival of subtly important tokens. Empirically, at 80% KV cache eviction, Nexus Sampling matches dense attention within 1% on LongBench while outperforming top-K baselines on retrieval-heavy tasks, with up to 10x smaller per-sequence cache memory.

---

## 結構化摘要

### 核心貢獻

- 提出 **Nexus Sampling**：training-free 的 streaming KV cache eviction 方法，解決現有 deterministic top-K 方案的「單步失分即永久刪除」缺陷。
- 引入 **Nexus scoring**：對 direct attention 做 iterative walk，挖掘 bridge token（連結性強但單步 attention 不突出的 token）。
- 以 **weighted reservoir sampling** 取代 deterministic top-K：token 以 inclusion probability 保留，避免單一低分步導致不可逆淘汰。
- 理論上證明 Nexus Sampling 在長期 token survival 上支配（dominates）deterministic top-K。

### 關鍵結果

- 80% KV cache eviction 條件下，LongBench 上與 dense attention 差距 **<1%**。
- retrieval-heavy tasks 上超越 top-K baselines。
- per-sequence cache memory 可縮小 **最高 10×**。

### 限制

- 論文未設獨立 Limitations 章節。
- Nexus scoring 為 iterative walk，相較 direct attention 有額外計算開銷，論文未詳述延遲數字。
- 評測以 LongBench 為主，針對超長 context（>1M token）或多模態場景的泛化能力尚未驗證。
- 目前為 inference-only 方法，與訓練期 context compression 技術的協同效果未探討。

---

## Workspace 關聯（評估，非既成結論）

- **context-management.md — NLAH 原則與 token budget**：Nexus Sampling 的核心問題（固定 memory budget 下如何選擇保留哪些 token）直接對應 NLAH 原則中「Right context > more context」的設計思路；bridge token 概念可類比於「高價值 context 放 HEAD/TAIL」的人工選擇策略。
- **core.md — 不可逆決策閘門（APPLY gate）**：論文批評 deterministic top-K 將「單步低分」轉為「不可逆淘汰」，與 The Loop 中「破壞性動作需二次確認、避免不可逆操作」的設計哲學對應；weighted sampling 引入的隨機性可視為一種 reversibility buffer。
- **`core.md §PROPOSE 委派`（原 subagent-strategy.md） — fan-out 與長 agentic workload**：論文明確針對 agentic LLM workload 的 streaming KV cache 問題，與 workspace 中多 sub-agent 並行、長時任務的 context 管理需求高度相關；⚠️ 實際落地需推理框架（vLLM/SGLang 等）支援 custom eviction policy，workspace 目前無此基礎設施。
- **unverified_success 閘門**：論文的 empirical 結果均以 LongBench benchmark 為準，對應 TEST 階段「展示真實輸出而非口頭聲稱」；⚠️ 將此方法引入 production inference pipeline 前，需在實際 workload 上做獨立驗證，不得以 benchmark 數字直接視為 verified。
