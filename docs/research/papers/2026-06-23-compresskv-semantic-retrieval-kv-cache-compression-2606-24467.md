---
url: "https://arxiv.org/abs/2606.24467"
title: "CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference"
archived_date: 2026-06-24
arxiv_id: 2606.24467
authors: ["Xiaolin Lin", "Jingcun Wang", "Olga Kondrateva", "Yiyu Shi", "Bing Li", "Grace Li Zhang"]
domains: [cs.AI]
html: "https://arxiv.org/html/2606.24467v1"
pdf_path: pdfs/2606.24467.pdf
published_date: 2026-06-23
---

# CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference

**Authors**: Xiaolin Lin, Jingcun Wang, Olga Kondrateva, Yiyu Shi, Bing Li, Grace Li Zhang
**Published**: June 23, 2026
**Source**: https://arxiv.org/abs/2606.24467 · [HTML](https://arxiv.org/html/2606.24467v1)
**arXiv ID**: 2606.24467
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2606.24467.pdf](https://arxiv.org/abs/2606.24467) (14 pp, full text archived)

---

## Abstract (quoted)

> Long-context large language model (LLM) inference is increasingly constrained by the memory footprint and decoding cost of key-value (KV) caches, limiting sustainable deployment on resource-constrained hardware. Existing KV cache eviction methods typically apply heuristic token scoring over all heads in GQA-based LLMs. These methods ignore the different functionalities of attention heads, leading to the eviction of critical tokens and thus degrading the performance of LLMs. To address this issue, we propose CompressKV, a resource-efficient KV-cache compression framework for GQA-based LLMs. Instead of aggregating attention scores from all heads, CompressKV identifies Semantic Retrieval Heads (SRHs) that capture both the initial and final tokens of a prompt and semantically important mid-context evidence, and uses them to select tokens whose KV pairs should be retained. Furthermore, CompressKV allocates cache budgets across layers according to offline estimates of layer-wise eviction error. Experiments on LongBench and Needle-in-a-Haystack show that CompressKV consistently outperforms existing KV-cache eviction methods across memory budgets. Notably, it preserves over 97% of full-cache performance using only 3% of the KV cache on LongBench question-answering tasks and achieves 90% accuracy with just 0.7% KV storage on Needle-in-a-Haystack. These results demonstrate an improved resource–performance trade-off for long-context LLM inference.

---

## 結構化摘要

### 核心貢獻

- 提出 CompressKV，針對 GQA-based LLM 的 KV cache 壓縮框架，核心機制是識別 Semantic Retrieval Heads（SRHs）
- SRHs 能捕捉 prompt 的首尾 token 與語義重要的中段 evidence，用以決定哪些 KV pair 應保留，取代對所有 attention heads 平均聚合的啟發式做法
- 採用 layer-wise 離線估算 eviction error，跨層非均勻分配 cache budget，避免一刀切的均等壓縮

### 關鍵結果

- LongBench QA 任務：僅用 3% KV cache，保留超過 97% 全快取效能
- Needle-in-a-Haystack：僅用 0.7% KV storage，仍達 90% 準確率
- 在多種 memory budget 下一致優於現有 KV cache eviction 方法

### 限制

- 論文未設獨立 Limitations 章節
- SRHs 識別方式為 offline 估算，推理時若 prompt 分布偏移（out-of-distribution），layer budget 分配可能次優
- 實驗集中於 LongBench 與 Needle-in-a-Haystack，對話、程式碼等其他長 context 場景的泛化能力未充分驗證
- 結果針對 GQA-based LLM，對 MHA 或 MLA 架構的適用性未說明

---

## Workspace 關聯（評估，非既成結論）

- **context-management / token budget**：CompressKV 的 3% KV cache 保留 97% 效能，直接對應 context-management.md 的 NLAH 原則（Right context > more context）；SRH 選擇語義重要 token 的機制，本質上與「只放 HEAD/TAIL 最重要資訊」的 context 放置策略同構。
- **KV cache 與 prefix caching 的邊界**：Workspace 已有 `2026-01-19-prefix-cache-to-fusion-rag-cache-2601-12904.md` 與 `2026-05-28-cacheprobe-auditing-prompt-cache-isolation-2605-30613.md`；CompressKV 聚焦 decode 階段 KV eviction（非 prefill prefix reuse），與 prompt caching 層次不同，可互補而非重疊。⚠️ 落地需確認目標推理框架（vLLM/SGLang）是否支援 GQA head-level KV 過濾介面。
- **unverified_success 閘門**：論文以 LLM benchmark 分數自報效能，符合 core.md 的 unverified_success 警示——直接採信前應在目標 serving stack 親跑 healthcheck，而非僅引用論文數字。
- **RAG / retrieval 相關論文群**：SRHs 識別「語義重要 mid-context evidence」的邏輯與 RAG 的 chunk relevance scoring 高度相似；可對照 `2024-05-23-hipporag-neurobiological-memory-2405-14831.md` 探討記憶檢索與 attention head 分工的關係。⚠️ 跨論文整合屬 off-rails 推斷，需人工判斷。
