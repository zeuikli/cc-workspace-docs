---
url: "https://arxiv.org/abs/2605.05657"
title: "Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation"
archived_date: 2026-07-26
arxiv_id: 2605.05657
authors: ["Abhijit Talluri", "Pujith Anne", "Bhagavan Choudary Pendiyala", "Raghavendra Chilukuri"]
domains: [cs.AI, cs.MA]
html: "https://arxiv.org/html/2605.05657v1"
pdf_path: pdfs/2605.05657.pdf
published_date: 2026-05-07
---

# Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation

**Authors**: Abhijit Talluri, Pujith Anne, Bhagavan Choudary Pendiyala, Raghavendra Chilukuri
**Published**: May 7, 2026
**Source**: https://arxiv.org/abs/2605.05657 · [HTML](https://arxiv.org/html/2605.05657v1)
**arXiv ID**: 2605.05657
**Categories**: cs.AI; cs.MA
**PDF**: [research/papers/pdfs/2605.05657.pdf](https://arxiv.org/abs/2605.05657)

---

## Abstract (quoted)

> Multi-agent LLM systems for code generation face a fundamental routing problem: the optimal orchestration topology depends on the structural complexity of the code under modification, yet existing systems select topologies without consulting the codebase. We present Retrieval-Guided Adaptive Orchestration (RGAO), an architecture that closes this loop by extracting a structural complexity vector from a hierarchical code index before selecting the orchestration topology. RGAO operates within Code-Agent, a multi-agent framework whose sub-agents are governed by formal contracts with six-dimensional budget vectors. Our headline contribution is the composition of two previously separate lines of work -- complexity-conditioned LLM routing and formal resource algebras -- yielding a property neither admits alone: provable budget conservation under retrieval-conditioned dynamic topology selection.

---

## 結構化摘要

### 核心貢獻

- **RGAO 路由器**：從分層代碼索引抽取 5 維複雜度向量 **c = (d_dep, n_f, n_s, h_t, ρ_x)**（最大依賴深度、文件數、符號計數、樹遍歷深度、跨模塊耦合比），全部訊號 <1ms 內從樹元資料讀出；依確定性閾值路由到 4 種拓撲：FastPath / SubAgent / MultiAgent / DeepResearch
- **六維預算代數** B = (B_iter, B_calls, B_tok, B_sec, B_retry, B_handoff) ∈ ℕ⁶；**Theorem 1** 保證父 agent 預算 ≥ 所有子 agent 預算之和（⊕ 運算），靜態檢查於 O(|V|+|E|) 時間內完成、在任何 LLM 呼叫之前執行
- 三路檢索融合：LATTICE（EMA 校準 α=0.6）+ KohakuRAG（多查詢重述）+ BM25，以倒數排名融合（RRF）合併；七信號評分函數（TF-IDF、語言先驗、符號類型、上下文鄰近、依賴中心度、內容長度、PageRank）
- 核心論點：**「組合本身才是貢獻」**——retrieval-conditioned routing 與 formal budget algebra 單獨皆無法達成可證明的 budget conservation，唯有二者組合才行

### 關鍵結果

- 250 標籤樣本（3 標註者，Fleiss' κ=0.78）：誤路由率 **30.1% → 8.2%**（[95% CI 6.1–10.9]，相對改善 73%；配對 McNemar χ²=43.6, p<10⁻⁶）
- 微基準（中值±MAD，n=20 輪）：路由決策 0.11ms、樹索引構建（200 檔案）11.1ms、契約工廠例示化 1.10μs、預算追蹤開銷 0.65μs
- 5 條複合管道 100% 完成率，平均約 6,000 tokens/管道（含干預恢復）；兩次故障注入（timeout、可重試錯誤）皆成功恢復
- SWE-bench 子集（10 題）pass@1 40%；相較無約束單體 agent（50–120K tokens）省 **8–20 倍** token
- 七信號消融：移除 TF-IDF 信號傷害最大（−0.022 nDCG，+2.8pp 誤路由）

### 限制

- Theorem 1 前提三假設：確定性工具成本（隨機成本下降級為期望保證，需 Azuma-Hoeffding 尾界）、有界檢索深度、有限行動空間
- 路由閾值為 hand-tuned（列於附錄 D）；250 樣本不足以訓練學習式分類器
- 5 維複雜度向量刻意輕量，遺漏圈複雜度、測試覆蓋密度、語言特定慣例（如 C++ 模板深度）等已知信號；陌生 repo 或樹坐標器語法外的語言下性能衰退
- 評估數字來自代理測試套件（非真實 SWE-bench）；作者自陳 SWE-bench Verified 有 contamination suspect 疑慮；完整 SWE-bench Pro 執行延至後續（估需約 220 GPU 小時、$3,400 API 成本）

---

## Workspace 關聯（評估，非既成結論）

- Theorem 1「父預算 ≥ 子預算總和」的形式化，直接對應 `core.md §PROPOSE 委派`（原 `graph.md §G4`） handoff「tier/effort parent 綁定，child 不自切」——本論文把這條 advisory 規則寫成可機械驗證的不等式，示範了 `[E]`/未標二分（原 `[E*]`，v5.1 廢除三分類） advisory 規則升級為機械驗證的具體路徑。⚠️ 落地前提是要有可觀測的 token/call 計量層，本 repo 目前無此基礎設施。
- 「靜態檢查先於任何 LLM 呼叫」與 `core.md`「判斷 vs 決定」公理一致：拓撲路由用確定性閾值而非 LLM 判斷。⚠️ 論文承認閾值手調、未學習化——與本 workspace pilot 檔位路由現況（同為手寫規則）處境相同，並非已驗證的優越解法。
