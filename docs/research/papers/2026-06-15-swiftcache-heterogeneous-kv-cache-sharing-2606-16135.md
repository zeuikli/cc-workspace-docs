---
url: "https://arxiv.org/abs/2606.16135"
title: "SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing"
archived_date: 2026-06-24
arxiv_id: 2606.16135
authors: ["Jianmin Hu", "Minxian Xu", "Sa Wang", "Chong Ma", "Min Shen", "Kejiang Ye", "Lin Qu", "Chengzhong Xu"]
domains: [cs.DC, "KV cache"]
html: "https://arxiv.org/html/2606.16135v1"
pdf_path: pdfs/2606.16135.pdf
published_date: 2026-06-15
---

# SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing

**Authors**: Jianmin Hu, Minxian Xu, Sa Wang, Chong Ma, Min Shen, Kejiang Ye, Lin Qu, Chengzhong Xu
**Published**: June 15, 2026
**Source**: https://arxiv.org/abs/2606.16135 · [HTML](https://arxiv.org/html/2606.16135v1)
**arXiv ID**: 2606.16135
**Categories**: cs.DC
**PDF**: [research/papers/pdfs/2606.16135.pdf](https://arxiv.org/abs/2606.16135) (15 pp, full text archived)

---

## Abstract (quoted)

> Multi-turn conversation is a fundamental scenario in LLM applications, widely used in chatbots and AI agents. As the conversation evolves, historical tokens accumulate continuously. Existing systems cache their key-value (KV) pairs to avoid redundant computation. However, limited GPU memory (HBM) capacity often forces these KV caches to be offloaded to CPU memory or SSD, making KV cache reloads increasingly costly in terms of latency as the context grows. Meanwhile, the constrained HBM capacity also limits the maximum inference length, thereby restricting the number of turns that can be supported in a conversation. To address these two challenges, we propose SwiftCache, a collaborative inference system that enables heterogeneous models to share underutilized GPU memory and NVLink bandwidth within a server. Specifically, models with low KV cache demand donate idle GPU memory to store the prefix cache of high-demand models, allowing cross-model KV cache sharing over NVLink and avoiding slow PCIe transfers. SwiftCache further reduces memory pressure by keeping only the KV cache of the currently active layer in local GPU memory, thereby enabling longer-context inference. Our experiments on real-world workloads show that SwiftCache reduces P99 time-to-first-token (TTFT) by up to 69% and extends maximum context length by up to 3.98x compared to vLLM and SGLang, with minimal interference to co-located models.

---

## 結構化摘要

### 核心貢獻

- **異構 KV cache 共享**：提出 SwiftCache 協作推論系統，讓同一伺服器內 KV cache 需求低的模型，將閒置 GPU HBM 捐出給高需求模型，透過 NVLink 跨模型共享 prefix cache，繞過速度慢的 PCIe 傳輸。
- **逐層 active KV cache**：任意時刻只在本地 GPU 記憶體保留「當前 active layer」的 KV cache，大幅降低 HBM 壓力，支援更長 context 推論。
- **Multi-turn 場景優化**：針對 chatbot / AI agent 多輪對話中 historical token 持續累積導致的延遲與長度限制，提出端到端系統解法。

### 關鍵結果

- P99 TTFT（time-to-first-token）最高降低 **69%**（對比 vLLM 與 SGLang）。
- 最大支援 context 長度延伸最高 **3.98×**。
- 對同節點 co-located 模型的推論干擾最小。

### 限制

- 論文聚焦單一伺服器內 NVLink 拓撲，跨節點（multi-node）場景未覆蓋。
- 異構模型共存的排程策略複雜度在動態負載下的穩健性未深入評估。
- 實驗基準僅對比 vLLM 與 SGLang，未涵蓋其他 KV offloading 方案（如 InfiniGen、MagicPIG）。

---

## Workspace 關聯（評估，非既成結論）

- **context-management / NLAH 原則**：SwiftCache 的 prefix cache 共享機制，與 `context-management.md` 中「Right context > more context」的 NLAH 原則在理念上呼應——都在解決 context 累積導致的記憶體/token 壓力；但 SwiftCache 是硬體層方案，workspace 的 prompt caching 是 API 層，域不同，⚠️ 不可直接類比為實作參考。
- **`core.md §PROPOSE 委派`（原 subagent-strategy.md） / KV cache 與 fan-out**：多輪 AI agent 對話中 KV cache 累積問題，對應 `core.md §PROPOSE 委派` 委派決策中「讀取 ≥10 檔 → context rot」的場景；SwiftCache 的跨模型 cache 共享概念，可作為思考 multi-agent 工作流中 context 隔離與共享的理論背景，⚠️ 但 workspace 無對應基礎設施層可直接採用。
- **unverified_success 閘門**：論文以 P99 TTFT 等可量化指標作為驗證依據，符合 `core.md` TEST 階段「展示確定性輸出才升 verified」的精神，可作為 LLM serving 系統評估指標的參考案例。
- **The Loop OBSERVE 階段**：SwiftCache 針對 GPU HBM 容量限制做精準的問題定義（OBSERVE），再提出最小干預解（NVLink sharing），與 core.md PROPOSE「外科刀原則」結構相符，是論文寫作與系統設計方法論的良好示範，⚠️ 僅概念映射，非工具整合。
