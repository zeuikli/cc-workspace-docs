---
url: "https://arxiv.org/abs/2606.05711"
title: "Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems"
archived_date: 2026-07-17
arxiv_id: 2606.05711
authors: ["Yingzhuo Liu"]
domains: [cs.CL]
html: "https://arxiv.org/html/2606.05711v1"
pdf_path: pdfs/2606.05711.pdf
published_date: 2026-06-04
---

# Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems

**Authors**: Yingzhuo Liu
**Published**: June 4, 2026
**Source**: https://arxiv.org/abs/2606.05711 · [HTML](https://arxiv.org/html/2606.05711v1)
**arXiv ID**: 2606.05711
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2606.05711.pdf](https://arxiv.org/abs/2606.05711)

---

## Abstract (quoted)

> Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought.

---

## 結構化摘要

### 核心貢獻

- Latent communication（agent 間直接交換 embedding/hidden state/KV-cache，繞過 text 生成瓶頸）文獻的統一框架
- 三正交軸分類：WHAT（交換什麼連續表徵）× WHICH（sender-receiver 對齊方式）× HOW（接收端融合方式）
- 系統化歸類 2024–2026 間 18 個代表方法，萃取 5 大設計模式

### 關鍵結果

- 綜述性論文；開放挑戰包含跨架構對齊、latent channel 安全性、edge 部署壓縮、與 latent CoT 的關係

### 限制

- latent 通道犧牲可解讀性與可稽核性——peer 無法「read, verify, and respond」
- 多數方法需白盒模型與共同架構，API-based agent 系統不可用

---

## Workspace 關聯（評估，非既成結論）

- 對 workspace 是「反面邊界」參考：core.md 的驗證閘門與展示紀律依賴通訊內容人類可稽核，latent channel 安全性被本篇列為 open challenge，正好說明 workspace 選擇 NL 通訊 + 機械失真閘（`.claude/skills/output-compress`）而非 latent 壓縮的取捨依據。
- 「discretization 不可逆資訊損失」提醒：文字層壓縮的 fidelity 上限存在，whitelist 不變式是在此上限內守住決策相關資訊。
