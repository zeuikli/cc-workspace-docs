---
url: "https://arxiv.org/abs/2604.05400"
title: "HYVE: Hybrid Views for LLM Context Engineering over Machine Data"
archived_date: 2026-06-24
arxiv_id: 2604.054
authors: ["Jian Tan", "Fan Bu", "Yuqing Gao", "Dev Khanolkar", "Jason Mackay", "Boris Sobolev", "Lei Jin", "Li Zhang"]
domains: [cs.AI, "context engineering"]
html: "https://arxiv.org/html/2604.05400v1"
pdf_path: pdfs/2604.05400.pdf
published_date: 2026-04-07
---

# HYVE: Hybrid Views for LLM Context Engineering over Machine Data

**Authors**: Jian Tan, Fan Bu, Yuqing Gao, Dev Khanolkar, Jason Mackay, Boris Sobolev, Lei Jin, Li Zhang
**Published**: April 07, 2026
**Source**: https://arxiv.org/abs/2604.05400 · [HTML](https://arxiv.org/html/2604.05400v1)
**arXiv ID**: 2604.05400
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2604.05400.pdf](https://arxiv.org/abs/2604.05400) (22 pp, full text archived)

---

## Abstract (quoted)

> Machine data is central to observability and diagnosis in modern computing systems, appearing in logs, metrics, telemetry traces, and configuration snapshots. When provided to large language models (LLMs), this data typically arrives as a mixture of natural language and structured payloads such as JSON or Python/AST literals. Yet LLMs remain brittle on such inputs, particularly when they are long, deeply nested, and dominated by repetitive structure.
>
> We present HYVE (HYbrid ViEw), a framework for LLM context engineering for inputs containing large machine-data payloads, inspired by database management principles. HYVE surrounds model invocation with coordinated preprocessing and postprocessing, centered on a request-scoped datastore augmented with schema information. During preprocessing, HYVE detects repetitive structure in raw inputs, materializes it in the datastore, transforms it into hybrid columnar and row-oriented views, and selectively exposes only the most relevant representation to the LLM. During postprocessing, HYVE either returns the model output directly, queries the datastore to recover omitted information, or performs a bounded additional LLM call for SQL-augmented semantic synthesis.
>
> We evaluate HYVE on diverse real-world workloads spanning knowledge QA, chart generation, anomaly detection, and multi-step network troubleshooting. Across these benchmarks, HYVE reduces token usage by 50-90% while maintaining or improving output quality. On structured generation tasks, it improves chart-generation accuracy by up to 132% and reduces latency by up to 83%. Overall, HYVE offers a practical approximation to an effectively unbounded context window for prompts dominated by large machine-data payloads.

---

## 結構化摘要

### 核心貢獻

- **HYVE framework**：針對含大型 machine data（logs、metrics、telemetry traces、JSON/AST）的 LLM 輸入，設計 preprocessing + postprocessing 協調層，靈感來自 database management 原則。
- **Request-scoped datastore**：以 schema 增強的暫存資料庫為核心，在 model invocation 外圍進行結構偵測與物化，而非直接塞入 context window。
- **Hybrid columnar/row-oriented views**：自動偵測重複結構，轉換為混合欄位導向與行導向的 view，僅向 LLM 暴露最相關的表示形式，大幅壓縮 token 用量。
- **SQL-augmented semantic synthesis**：postprocessing 階段可直接查詢 datastore 補回省略資訊，或進行有界的額外 LLM call 做語意合成，避免資訊遺失。

### 關鍵結果

- Token 用量降低 **50–90%**，跨 knowledge QA、chart generation、anomaly detection、multi-step network troubleshooting 四類真實工作負載皆維持或提升輸出品質。
- Structured generation（chart generation）準確率提升最高 **132%**，延遲降低最高 **83%**。
- 整體效果：對以 machine data 為主的 prompt，實現近似「無界 context window」的實用近似。

### 限制

- 論文聚焦 machine data（結構化/半結構化），對純自然語言 prompt 的適用性未評估。
- Request-scoped datastore 引入額外系統複雜度（schema 偵測、SQL 層），對低延遲要求場景的 overhead 未量化。
- SQL-augmented postprocessing 需額外 LLM call，在 worst-case path 下可能抵消部分延遲增益。
- 評估集為公司內部真實工作負載，外部可重現性受限。

---

## Workspace 關聯（評估，非既成結論）

- **NLAH 原則直接對應**：HYVE 的「只暴露最相關表示給 LLM」與 `context-management.md` 的 NLAH 原則（Right context > more context）高度一致，為該原則提供系統性工程實作的參考案例。
- **The Loop OBSERVE 階段的 context 預算管理**：HYVE 的 preprocessing datastore 可類比 The Loop 中 OBSERVE 前的「讀取最小必要範圍」紀律；token 50–90% 降幅為 token budget 軟性門檻（per-task ~4,000 tokens）在 machine data 場景的量化佐證。
- **unverified_success 閘門的工具層類比**：HYVE 的 postprocessing「query datastore to recover omitted information」階段，與 core.md `unverified_success` 閘門概念相似——model output 不直接信任，需機械查驗補回省略資訊後才確認結果。⚠️ 落地門檻：workspace 目前無 machine data ingestion pipeline，需額外基礎設施才能直接採用。
- **Subagent context rot 緩解**：fan-out 委派中各 sub-agent 收到的 context 若含大量結構化工具輸出（JSON logs），HYVE 式 view 壓縮可緩解 context rot 問題；⚠️ 目前 workspace 無此層，屬概念層連結。
