---
url: "https://arxiv.org/abs/2410.02506"
title: "Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems"
archived_date: 2026-07-17
arxiv_id: 2410.02506
authors: ["Guibin Zhang", "Yanwei Yue", "Zhixun Li", "Sukwon Yun", "Guancheng Wan", "Kun Wang", "Dawei Cheng", "Jeffrey Xu Yu", "Tianlong Chen"]
domains: [cs.MA, cs.LG]
html: "https://arxiv.org/html/2410.02506v1"
pdf_path: pdfs/2410.02506.pdf
published_date: 2024-10-03
---

# Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)

**Authors**: Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, Guancheng Wan, Kun Wang, Dawei Cheng, Jeffrey Xu Yu, Tianlong Chen
**Published**: October 3, 2024
**Source**: https://arxiv.org/abs/2410.02506 · [HTML](https://arxiv.org/html/2410.02506v1)
**arXiv ID**: 2410.02506
**Categories**: cs.MA, cs.LG
**PDF**: [research/papers/pdfs/2410.02506.pdf](https://arxiv.org/abs/2410.02506)

---

## Abstract (quoted)

> Recent advancements in large language model (LLM)-powered agents have shown that collective intelligence can significantly outperform individual capabilities, largely attributed to the meticulously designed inter-agent communication topologies. Though impressive in performance, existing multi-agent pipelines inherently introduce substantial token overhead, as well as increased economic costs, which pose challenges for their large-scale deployments. In response to this challenge, we propose an economical, simple, and robust multi-agent communication framework, termed AgentPrune, which can seamlessly integrate into mainstream multi-agent systems and prunes redundant or even malicious communication messages. Technically, AgentPrune is the first to identify and formally define the communication redundancy issue present in current LLM-based multi-agent pipelines, and efficiently performs one-shot pruning on the spatial-temporal message-passing graph, yielding a token-economic and high-performing communication topology.

---

## 結構化摘要

### 核心貢獻

- 首次形式化定義 LLM multi-agent pipeline 的 communication redundancy 問題
- AgentPrune：在 spatial-temporal message-passing graph 上做 one-shot pruning，剪除冗餘甚至惡意訊息，可無縫整合主流 MAS（AutoGen、GPTSwarm 等）

### 關鍵結果

- 產出 token 經濟且高效能的通訊拓樸；abstract 未含具體節省百分比（正文有，未在此引用）

### 限制

- one-shot pruning 對動態變化的任務分布適應性未知
- 「惡意訊息剪除」的安全宣稱需獨立驗證，非本文核心 benchmark

---

## Workspace 關聯（評估，非既成結論）

- 對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 benefit-gated 委派與「child 輸出只含結果」紀律：AgentPrune 證明 agent 間通訊大量冗餘，支持 workspace「bulk 產出不回灌主 context」的既有設計。
- 剪枝以圖結構確定性操作執行、非 LLM 逐訊息自評，契合 output-compress 的機械閘思路——可評估把「訊息級白名單」推廣到 parent↔child Return 欄位裁剪。
