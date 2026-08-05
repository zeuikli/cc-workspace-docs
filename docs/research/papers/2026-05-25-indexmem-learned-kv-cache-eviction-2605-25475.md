---
url: "https://arxiv.org/abs/2605.25475"
title: "IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference"
archived_date: 2026-06-24
arxiv_id: 2605.25475
authors: ["Xintong Yang", "Hao Gu", "Binxing Xu", "Lujun Li", "Bei Liu", "Jiacheng Liu", "Qiyuan Zhu", "Sirui Han", "Yike Guo"]
domains: [cs.CL, "KV cache"]
html: "https://arxiv.org/html/2605.25475v1"
pdf_path: pdfs/2605.25475.pdf
published_date: 2026-05-25
---

# IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference

**Authors**: Xintong Yang, Hao Gu, Binxing Xu, Lujun Li, Bei Liu, Jiacheng Liu, Qiyuan Zhu, Sirui Han, Yike Guo
**Published**: May 25, 2026
**Source**: https://arxiv.org/abs/2605.25475 · [HTML](https://arxiv.org/html/2605.25475v1)
**arXiv ID**: 2605.25475
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2605.25475.pdf](https://arxiv.org/abs/2605.25475) (18 pp, full text archived)

---

## Abstract (quoted)

> Large Language Models (LLMs) are increasingly expected to operate over long contexts, yet standard softmax attention incurs a KV cache that grows linearly with sequence length, quickly becoming the bottleneck for long context inference. A practical remedy is to evict less important KV entries; however, existing eviction policies are largely heuristic and struggle to capture the rich, input-dependent distribution of token importance. In this work, we introduce a learnable indexer that predicts KV importance, enabling more accurate retention of critical tokens. Meanwhile, naively evicting tokens permanently discards their information, leading to irreversible forgetting and degraded retrieval over long ranges. To address this, we propose a lightweight latent memory module that compresses evicted tokens into a compact, online-updated state and provides residual readouts to compensate for the attention contributions lost through KV eviction. Collectively, our method enables accurate long-context inference under a bounded KV budget, delivering consistent improvements on RULER (4K/16K) across Qwen, Mistral, and Llama models (up to 25 points under aggressive eviction), markedly more stable Needle-in-a-Haystack retrieval, and superior LongBench scores and compression curves compared to existing eviction policies.

---

## 結構化摘要

### 核心貢獻

- **Learned KV eviction**：以可學習的 indexer 預測每個 token 的 KV 重要性，取代現有啟發式 eviction policy（如 attention score threshold），使留存決策隨輸入分佈動態調整。
- **Latent memory module**：被 evict 的 KV 不直接丟棄，而是壓縮進一個 lightweight、online-updated 的 latent state；attention 計算時提供 residual readout，補償 eviction 造成的注意力損失，緩解不可逆遺忘問題。
- **Bounded KV budget 推論**：整體架構在記憶體上限固定的條件下，讓 long-context LLM 保持穩定推理品質，適用於 Qwen、Mistral、Llama 等主流架構。

### 關鍵結果

- RULER benchmark（4K/16K context）：在 aggressive eviction 設定下，相較 baseline eviction policy 提升最多 **25 points**。
- Needle-in-a-Haystack 檢索任務：穩定性顯著優於現有 eviction 方法（量化數字未明列，論文以曲線呈現）。
- LongBench：compression curve（KV budget vs. 性能）全程優於對比方案。

### 限制

- Learned indexer 需要額外訓練（fine-tuning 或 plug-in 訓練），對已部署模型的整合成本未詳述。
- Latent memory 的 online update 機制在極長序列（>100K tokens）下的延遲與記憶體開銷未量化。
- 實驗限於 decoder-only 架構（Qwen/Mistral/Llama），encoder-decoder 或 MoE 模型適用性未驗證。

---

## Workspace 關聯（評估，非既成結論）

- **context-management.md 的 NLAH 原則**：本論文的 KV eviction + latent memory 機制與 "Right context > more context" 理念高度對應——保留 critical tokens、壓縮低重要性 token，是 inference 層的 NLAH 實踐；⚠️ 兩者作用層不同（模型推理 vs. prompt 工程），不可直接互換。
- **memory-compactor 概念**：latent memory module 的「壓縮被捨棄資訊為 compact state」思路，與 workspace 的 memory compactor（跨 session 壓縮 context）在設計意圖上相似；⚠️ 落地門檻高，workspace memory 為 text-level 操作，此論文為 embedding-level，實作路徑不同。
- **unverified_success 閘門**：論文以 RULER/LongBench 等 benchmark 驗證，但 benchmark 覆蓋的 task 分佈不等於生產推理場景；引用結果前應視為 `unverified_success`，需在目標模型與 context 長度下親自重跑確認。
- **token budget 管理**：研究結論可作為設計「何時/如何截斷長 context」策略的理論依據，與 context-management.md 的 token budget 軟性門檻互為參照；⚠️ 直接套用需對應模型支援 IndexMem 的 learned indexer。
