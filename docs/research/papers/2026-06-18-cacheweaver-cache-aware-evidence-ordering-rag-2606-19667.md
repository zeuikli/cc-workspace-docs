---
url: "https://arxiv.org/abs/2606.19667"
title: "CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference"
archived_date: 2026-06-24
arxiv_id: 2606.19667
authors: ["Kaizhen Tan", "Rong Gu", "Mingyuan Li"]
domains: [cs.CL, "prompt caching"]
html: "https://arxiv.org/html/2606.19667v1"
pdf_path: pdfs/2606.19667.pdf
published_date: 2026-06-18
---

# CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference

**Authors**: Kaizhen Tan, Rong Gu, Mingyuan Li
**Published**: June 18, 2026
**Source**: https://arxiv.org/abs/2606.19667 · [HTML](https://arxiv.org/html/2606.19667v1)
**arXiv ID**: 2606.19667
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2606.19667.pdf](https://arxiv.org/abs/2606.19667) (9 pp, full text archived)

---

## Abstract (quoted)

> Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. Prefix caching in serving engines such as vLLM reduces this cost only when requests share the same token prefix. In grounded generation, however, adjacent queries may retrieve overlapping evidence in different orders, so set overlap does not become reusable prefix overlap. We present CacheWeaver, a lightweight prompt-layer method for cache-aware evidence ordering. The method keeps a prefix tree over recently served evidence sequences and uses a greedy walk to place the most reusable prefix first, while leaving the serving engine and retrieved evidence set unchanged. Across three vLLM configurations, the method lowers median time-to-first-token (TTFT) by about 20-33 percent relative to retrieval-order prefix caching, without hurting answer quality in our QA tests. The greedy policy reaches 97.5 percent of the median TTFT gain from oracle ordering, indicating that most reusable prefix locality can be recovered by a simple scheduling layer between retrieval and inference.

---

## 結構化摘要

### 核心貢獻

- 提出 **CacheWeaver**：在 retrieval 與 inference 之間插入輕量 prompt-layer scheduling，重新排列 evidence 順序以最大化 prefix cache 命中率。
- 維護 **prefix tree**（前綴樹）追蹤近期已服務的 evidence 序列，以 greedy walk 選出最長可重用前綴優先放置，不修改 serving engine（vLLM）或 retrieved evidence set。
- 目標指標：**TTFT（time-to-first-token）**，即 prefill 延遲；在不影響答題品質的前提下降低推論成本。

### 關鍵結果

- 跨三種 vLLM 配置，median TTFT 相較 retrieval-order prefix caching 降低約 **20–33%**。
- Greedy policy 達到 oracle ordering 可得 median TTFT 增益的 **97.5%**，顯示簡單排程即可回收絕大多數 prefix locality。
- QA 品質測試中未觀測到答題品質下降。

### 限制

- 論文未設獨立 limitation 章節；可判斷的弱點：
  - Prefix tree 效益依賴相鄰請求間 evidence 重疊率高，低重疊場景（如高多樣性查詢流）增益有限。
  - 評估僅在 vLLM 上進行，跨 serving engine（TGI、TensorRT-LLM 等）泛化性未驗證。
  - 僅報告 median TTFT，尾延遲（P95/P99）與 throughput 影響未充分討論。

---

## Workspace 關聯（評估，非既成結論）

- **直接呼應 `context-management.md` §Prompt Caching 核心原則**：本庫規則要求「CLAUDE.md 內容 = 最穩定快取前綴，永遠放最前」，CacheWeaver 的 prefix tree greedy walk 是同一直覺的系統化實現——在 RAG 場景動態決定哪段 context 應擺在 HEAD 以最大化 cache 復用。
- **對應 NLAH 原則（Right context > more context）**：CacheWeaver 不增減 evidence，只調整排列順序；這與「context 放 HEAD 或 TAIL，中間放動態狀態」的 NLAH 精神一致，說明 ordering 本身即是 context 管理的一個維度。
- **對 subagent fan-out 場景的潛在啟示**：多個 sub-agent 並行查詢共用知識庫時，若 LLM serving 層有 prefix cache，統一 evidence 排序策略可降低跨請求的 cache 碎片化；⚠️ 本庫目前無對應機制，屬未落地概念。
- **⚠️ 域外注意**：CacheWeaver 針對 vLLM serving engine 的 KV cache；Claude API（Anthropic 管理）的 prompt caching 實作細節不公開，本方法能否直接移植需進一步確認。

