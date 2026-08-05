---
url: "https://arxiv.org/abs/2605.24786"
title: "CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM"
archived_date: 2026-06-24
arxiv_id: 2605.24786
authors: ["Yubo Li", "Yidi Miao"]
domains: [cs.LG]
html: "https://arxiv.org/html/2605.24786v1"
pdf_path: pdfs/2605.24786.pdf
published_date: 2026-05-24
---

# CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM

**Authors**: Yubo Li, Yidi Miao
**Published**: May 24, 2026
**Source**: https://arxiv.org/abs/2605.24786 · [HTML](https://arxiv.org/html/2605.24786v1)
**arXiv ID**: 2605.24786
**Categories**: cs.LG
**PDF**: [research/papers/pdfs/2605.24786.pdf](https://arxiv.org/abs/2605.24786) (20 pp, full text archived)

---

## Abstract (quoted)

> Long-horizon LLM inference turns the key--value (KV) cache into the dominant GPU memory consumer and makes per-token attention increasingly expensive. Many common eviction policies use static recency windows or historical attention, leaving unused a signal computed on every decoding step: the model's current uncertainty. We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident. Within each budget, tokens are ranked by a composite of accumulated attention mass and recency, while a protected recent window preserves local coherence. We combine the policy with blockwise online-softmax attention, mixed FP16/INT8 storage, and a pyramidal per-layer budget variant. Across four model families and generated lengths up to 4K, CONF-KV stays near the footprint of a fixed 512-token sliding window while remaining within 1.5--2.1 perplexity points of full KV. On Needle-in-a-Haystack up to 32K tokens, CONF-KV reaches 91.4% retrieval accuracy versus 53.8% for sliding windows and 80.6% for H2O; on 75 VisualWebArena tasks it retains 95.3% of full-KV success at 2.8 times lower peak memory.

---

## 結構化摘要

### 核心貢獻

- **Confidence-aware 動態 budget**：將 next-token distribution 轉為純量 confidence score，模型不確定時保留更多 KV cache context；高信心時積極 evict，實現自適應 per-step budget 調控。
- **複合 token ranking**：每個 budget 內以 accumulated attention mass + recency 複合分數排名，並設 protected recent window 維持局部 coherence，避免近端 context 被誤刪。
- **Mixed-precision 儲存 + 金字塔 layer budget**：結合 FP16/INT8 混合精度儲存與 blockwise online-softmax attention；pyramidal per-layer budget variant 針對不同 layer 深度分配不同 budget。
- **端到端效能**：在 Needle-in-a-Haystack（32K tokens）達 91.4% retrieval accuracy，顯著優於 sliding window（53.8%）與 H2O（80.6%）；VisualWebArena 以 2.8× 較低 peak memory 保留 95.3% full-KV success rate。

### 關鍵結果

- 四個 model families、生成長度至 4K：KV footprint 接近固定 512-token sliding window，perplexity 僅差 1.5–2.1 points vs full KV。
- Needle-in-a-Haystack（32K）：CONF-KV 91.4% vs sliding window 53.8% vs H2O 80.6%。
- VisualWebArena（75 tasks）：peak memory 降低 2.8×，仍保留 95.3% full-KV success。

### 限制

- 論文未列明確 limitation 章節。推斷弱點：
  - Confidence score 計算依賴 next-token logit distribution，對採用 sparse softmax 或特殊 head 的模型需額外適配。
  - 評估 context 長度至 32K；更長序列（128K+）的 confidence score 穩定性未驗證。
  - Mixed-precision INT8 quantization 在特定任務（精確數值推理）可能累積誤差，論文未作細分分析。

---

## Workspace 關聯（評估，非既成結論）

- **context-management / NLAH 原則直接呼應**：CONF-KV 的核心思想「不確定時保留更多 context、信心高時剪枝」與 core.md 的「Right context > more context」及 context-management.md 的 token budget 軟性控制在概念層高度對齊；CONF-KV 提供了一個可機械驗證的 confidence 信號，而非靜態規則。
- **「判斷 vs 決定」跨切紀律**：論文的 confidence score 扮演「LLM 判斷」的量化代理（scalar signal），再由確定性的 budget allocation 邏輯做「決定」（evict / retain），與 core.md 判斷 vs 決定分離原則結構吻合；⚠️ 落地門檻：實際整合需能取得 token-level logit，API-only 環境無法直接套用。
- **subagent token budget 優化潛力**：長 agentic session（core.md context-management §compact 觸發）的 KV 壓力與 CONF-KV 解決的問題同域；若推理引擎層可整合此 eviction policy，有機會延後 compact 觸發點；⚠️ 目前 Claude API 不暴露 KV 控制介面，屬研究啟發而非直接可用。
- **unverified_success 閘門類比**：CONF-KV 的 protected recent window 設計（保護最近 tokens 不被 evict）在概念上類似 core.md 的「unverified_success 閘門」——即使信心高也不貿然丟棄最新狀態，防止局部 coherence 崩壞；此設計原則可遷移至 agent workflow 的 checkpoint 保護策略。
