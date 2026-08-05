---
url: "https://arxiv.org/abs/2606.06302"
title: "Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving"
archived_date: 2026-06-24
arxiv_id: 2606.06302
authors: ["Hyungmin Kim", "Minsoo Kim", "Hongseok Kim", "Jungwook Choi"]
domains: [cs.LG]
html: "https://arxiv.org/html/2606.06302v1"
pdf_path: pdfs/2606.06302.pdf
published_date: 2026-06-04
---

# Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving

**Authors**: Hyungmin Kim, Minsoo Kim, Hongseok Kim, Jungwook Choi
**Published**: June 04, 2026
**Source**: https://arxiv.org/abs/2606.06302 · [HTML](https://arxiv.org/html/2606.06302v1)
**arXiv ID**: 2606.06302
**Categories**: cs.LG
**PDF**: [research/papers/pdfs/2606.06302.pdf](https://arxiv.org/abs/2606.06302) (15 pp, full text archived)

---

## Abstract (quoted)

> Multi-turn LLM serving accumulates dialogue history whose Key-Value (KV) cache grows with every turn and every user, quickly exceeding the model weights themselves and making memory -- not compute -- the binding constraint on throughput. Non-uniform KV compression, which allocates heterogeneous budgets across attention heads, preserves accuracy far better than uniform schemes, yet remains impractical: modern serving stacks assume identical KV lengths across heads, so heterogeneity traps freed memory as page fragmentation, spends up to 25% of prefill time reclaiming scattered pages, and skews GPU workloads that inflate decode latency by up to 1.7× or burn 15--20% of each decode step on re-planning. We observe that this heterogeneity need not be discovered at runtime: head-wise retention follows a two-level structural regularity -- an input-invariant head ranking with narrowly bounded per-head ratios -- that can be calibrated offline from as few as 50 samples. Building on this insight, we present Tangram, a serving framework that statically resolves what prior systems handle dynamically: Budget Reservation fixes each head's post-compression footprint at scheduling time, eliminating page reclamation; Ragged Paging clusters similar-budget heads into independent page tables, turning fragmentation into reclaimable memory; and Ahead-of-Time Load Balancing precomputes balanced GPU partitions with zero runtime planning. Implemented on vLLM, Tangram serves as a drop-in substrate for existing non-uniform compression methods, matching their accuracy while improving end-to-end throughput by up to 2.6× over the full-KV baseline.

---

## 結構化摘要

### 核心貢獻

- **問題定義**：Multi-turn LLM serving 中，KV cache 隨對話輪次累積，記憶體（而非算力）成為 throughput 瓶頸；non-uniform KV compression 雖精度更優，但現有 serving stack 無法有效支援異質 head budget。
- **靜態化洞察**：Head-wise retention 具備「兩層結構規律性」——head ranking 對輸入不變、per-head ratio 範圍窄——可從 50 個樣本 offline 校準，無需 runtime 動態計算。
- **Budget Reservation**：在 scheduling 階段靜態確定每個 head 壓縮後的記憶體佔用，消除 page reclamation 開銷。
- **Ragged Paging**：將相近 budget 的 head 歸入獨立 page table，將 fragmentation 轉為可回收記憶體。
- **Ahead-of-Time Load Balancing**：預計算 GPU partition 分配，decode 步驟零 re-planning 成本。

### 關鍵結果

- 相比 full-KV baseline，end-to-end throughput 提升最高 **2.6×**。
- 消除了 prefill 階段高達 **25%** 的 page reclamation 時間。
- 解決 decode latency 膨脹問題（舊方案可達 **1.7×** 延遲，每步燒 **15–20%** 在 re-planning）。
- 實作於 vLLM，可作為現有 non-uniform compression 方法的 drop-in substrate，精度不降。

### 限制

- 論文自述 offline 校準仰賴代表性 calibration data（50 samples），若 serving workload 分布偏移，靜態 budget 可能次優。
- ⚠️ Ragged Paging 與 Budget Reservation 的系統整合複雜度未深入討論；對非 vLLM serving stack 的移植成本不明。
- 評估聚焦 throughput 指標，未見對 tail latency（p99）的系統性報告。

---

## Workspace 關聯（評估，非既成結論）

- **Context-management / token budget 類比**：Tangram 的「靜態 budget reservation」與 `context-management.md` 中 NLAH 原則（Right context > more context）及 token budget 管理在設計哲學上相通——兩者皆強調預先規劃資源分配，避免 runtime 動態重分配的不可預測性。
- **判斷 vs 決定（跨切紀律）**：論文的核心洞察是將 head ranking（判斷層，offline LLM 分析）與 page table 分配（決定層，確定性演算法）明確分離，對應 `core.md` 「LLM 只做判斷，確定性代碼做決定」原則的工程實踐案例。
- **unverified_success 閘門**：offline calibration 產出的靜態 budget 若未經 runtime 實測驗證即直接部署，構成典型 `unverified_success` 情境；Tangram 的設計隱含需要 workload distribution 穩定作為前提假設，⚠️ 實際部署前須驗證 calibration set 代表性。
- **Multi-turn serving → multi-session memory 延伸**：KV cache 跨 turn 累積的問題結構，與 workspace 中跨 session 記憶管理（`memory/MEMORY.md`、memory-compactor）在「歷史 context 如何有效壓縮保留」這一抽象層面具可類比性，⚠️ 但 LLM inference serving 與 agent session 管理屬不同工程域，直接套用須謹慎。
