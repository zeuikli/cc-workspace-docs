---
url: "https://arxiv.org/abs/2604.08075"
title: "Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving"
archived_date: 2026-06-24
arxiv_id: 2604.08075
authors: ["Xunzhuo Liu", "Bowei He", "Xue Liu", "Andy Luo", "Haichen Zhang", "Huamin Chen"]
domains: [cs.CL, "token budget"]
html: "https://arxiv.org/html/2604.08075v1"
pdf_path: pdfs/2604.08075.pdf
published_date: 2026-04-09
---

# Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving

**Authors**: Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
**Published**: April 09, 2026
**Source**: https://arxiv.org/abs/2604.08075 · [HTML](https://arxiv.org/html/2604.08075v1)
**arXiv ID**: 2604.08075
**Categories**: cs.CL, token budget
**PDF**: [research/papers/pdfs/2604.08075.pdf](https://arxiv.org/abs/2604.08075) (15 pp, full text archived)

---

## Abstract (quoted)

> Production vLLM fleets typically provision each instance for the worst-case context length, leading to substantial KV-cache over-allocation and under-utilized concurrency. In practice, 80-95% of requests are short, yet are served under configurations optimized for long contexts, wasting 4-8× throughput capacity and triggering reliability issues such as OOM crashes, preemption, and request rejections. We identify a common root cause for these inefficiencies: configuration-traffic mismatch. We propose dual-pool token-budget routing, a lightweight dispatch mechanism that partitions a homogeneous fleet into two specialized pools: a high-throughput short-context pool and a high-capacity long-context pool. Each request is routed based on its estimated total token budget, computed using a per-category bytes-to-token ratio that is learned online via exponential moving average from usage.prompt_tokens feedback, eliminating the need for a tokenizer. We also develop a simple analytical model that predicts fleet-level cost savings from workload characteristics and measured throughput differences, enabling practitioners to estimate benefits prior to deployment. Evaluations on real-world traces from the Azure LLM Inference Dataset and LMSYS-Chat-1M, serving Llama-3-70B on A100 GPUs, show that our approach reduces GPU-hours by 31-42%, corresponding to $2.86M annual savings at fleet scale, while lowering preemption rates by 5.4× and improving P99 TTFT by 6%. A case study with Qwen3-235B-A22B on AMD MI300X at 10,000 req/s projects $15.4M in annual savings. The method incurs only O(1) dispatch overhead, adapts automatically to heterogeneous workloads, and composes seamlessly with existing optimizations such as PagedAttention, continuous batching, and prefill-decode disaggregation.

---

## 結構化摘要

### 核心貢獻

- 識別 production LLM fleet 的根本問題：**configuration-traffic mismatch**——80–95% 請求為短 context，卻在針對長 context 最佳化的實例上執行，造成 4–8× throughput 浪費與 OOM/preemption 可靠性問題。
- 提出 **dual-pool token-budget routing**：將同質 fleet 分成 short-context 高吞吐池與 long-context 高容量池，依每請求估算的 token budget 做 O(1) dispatch。
- Token budget 估算採 **per-category bytes-to-token ratio**，透過 exponential moving average 從 `usage.prompt_tokens` 在線學習，完全不需 tokenizer，適合生產部署。
- 附帶 **分析模型**：根據 workload 特性與 throughput 差異預測 fleet 級省本，讓工程師部署前即可評估收益。

### 關鍵結果

- Llama-3-70B on A100（Azure LLM Inference Dataset & LMSYS-Chat-1M traces）：GPU-hours 減少 **31–42%**，換算年省 **$2.86M**。
- Preemption rate 降低 **5.4×**；P99 TTFT 改善 **6%**。
- Qwen3-235B-A22B on AMD MI300X（10,000 req/s）案例研究：年省預測 **$15.4M**。
- 與 PagedAttention、continuous batching、prefill-decode disaggregation 等現有優化無縫組合，無競態。

### 限制

- 文件未列獨立 limitation 章節。判斷弱點：
  - **Pool 數量固定為 2**：workload 若呈多峰分布（短、中、長混合），雙池切割可能不夠精細。
  - **bytes-to-token ratio 線上學習收斂期**：冷啟動或 workload 突變初期，估算誤差可能導致路由偏差。
  - **評估模型受限**：僅驗證 Llama-3-70B 與 Qwen3-235B；對 MoE 以外架構或多模態輸入的泛化性未驗證。

---

## Workspace 關聯（評估，非既成結論）

- **Token budget / context-management**：論文的核心機制是依 token budget 做 routing，直接對應 `context-management.md` 中「Token Budget（軟性參考，防 loop 失控）」與「per-task ~4,000 / per-session ~30,000 tokens」監控概念——fleet 側的 budget-aware dispatch 與 agent 側的 budget 管理屬同一問題族。
- **「判斷 vs 決定」跨切紀律**：論文的 routing 邏輯（bytes-to-token ratio → pool 選擇）是純確定性計算，符合 `core.md` 跨切紀律「確定性代碼做決定（路由/重試）；LLM 做判斷」的設計原則，可作為 workspace subagent routing 設計的參照案例。
- **Subagent fan-out 與 pool 分工**：dual-pool 架構（short-context 高吞吐池 vs long-context 高容量池）概念上類似 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的 model selection 按任務規模路由（0–1 檔 Haiku / 10+ 檔 Sonnet/Opus），提供 infrastructure 層驗證。
- ⚠️ 落地門檻：本論文針對 vLLM production fleet，workspace 目前無自建 inference fleet；概念可借鑒，但具體 pool 參數與 workload trace 分析不可直接套用。

