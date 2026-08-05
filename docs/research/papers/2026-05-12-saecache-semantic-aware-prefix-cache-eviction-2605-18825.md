---
url: "https://arxiv.org/abs/2605.18825"
title: "Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches"
archived_date: 2026-06-24
arxiv_id: 2605.18825
authors: ["Shaoke Fang", "Ziang Li", "Wenfei Wu", "Jiatong Ji", "Qingsong Liu", "Ruizhi Pu"]
domains: [cs.LG, "prompt caching"]
html: "https://arxiv.org/html/2605.18825v1"
pdf_path: pdfs/2605.18825.pdf
published_date: 2026-05-12
---

# Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches

**Authors**: Shaoke Fang, Ziang Li, Wenfei Wu, Jiatong Ji, Qingsong Liu, Ruizhi Pu
**Published**: May 12, 2026
**Source**: https://arxiv.org/abs/2605.18825 · [HTML](https://arxiv.org/html/2605.18825v1)
**arXiv ID**: 2605.18825
**Categories**: cs.LG, prompt caching
**PDF**: [research/papers/pdfs/2605.18825.pdf](https://arxiv.org/abs/2605.18825) (31 pp, full text archived)

---

## Abstract (quoted)

> Prefix caching is a key optimization in Large Language Model (LLM) serving, reusing attention Key-Value (KV) states across requests with shared prompt prefixes to reduce expensive prefill computation. However, its benefit depends critically on the eviction policy as GPU memory is scarce, and existing policies such as LRU largely treat cached blocks uniformly. This view ignores a fundamental property of LLM prompts: not all tokens are equally worth caching. We show that different token types within a prompt, including system prompts, user queries, tool outputs, model responses, and chain-of-thought reasoning, exhibit up to 756x variation in reuse rates, yet no existing eviction policy exploits this signal. In this paper, we present SAECache (Semantic-Adaptive Eviction for prefix caches), a semantic-adaptive prefix cache eviction policy that addresses this gap through three innovations: (1) a multi-queue architecture that routes KV blocks to task-specific queues with tailored priority metrics, capturing both session reuse in multi-turn requests and structural reuse in templated single-turn requests; (2) a semantic-aware token weighting mechanism that learns the reuse value of different token types online through eviction feedback; (3) a fully adaptive online learning schema for all parameter updates, including log-normal timing parameters, position decay power, queue weights, and meta-parameters, which eliminates manual tuning and enables automatic adaptation to deployment-specific workload characteristics. Through extensive evaluation across heterogeneous workloads, we demonstrate that SAECache achieves 1.4x-2.7x TTFT improvement over production-style baselines, while fixed-parameter alternatives can degrade by up to 2.7x under workload mismatch -- a failure mode our adaptive approach avoids entirely.

---

## 結構化摘要

### 核心貢獻

- **Reuse rate 差異揭露**：實證不同 token 類型（system prompt、user query、tool output、model response、chain-of-thought）的 KV block reuse rate 相差最高 756x，打破 LRU 等均等對待的假設。
- **SAECache 三層設計**：(1) multi-queue 架構依 token 類型路由 KV block，同時捕捉 multi-turn session reuse 與 single-turn structural reuse；(2) semantic-aware token weighting，透過 eviction feedback 線上學習各 token 類型的 reuse value；(3) 全參數 fully adaptive online learning（含 log-normal timing、position decay power、queue weights、meta-parameters），消除人工調參。
- **部署自適應**：所有參數線上更新，可自動適應 workload 分布漂移，不需重新調參。

### 關鍵結果

- 相較 production-style baselines，SAECache 達到 **1.4x–2.7x TTFT（Time To First Token）改善**。
- 固定參數替代方案在 workload mismatch 下最多降退 **2.7x**，而 SAECache 全適應設計完全迴避此失敗模式。
- 評估橫跨 heterogeneous workloads（multi-turn、templated single-turn 等多種場景）。

### 限制

- 論文自述限制未在 abstract 中明列；推測弱點：
  - Online learning 的收斂速度與 cold-start 行為在 workload 急劇變化時可能存在延遲。
  - multi-queue 架構的 overhead（記憶體管理、queue routing）在小規模部署下的 cost-benefit 需實驗驗證。
  - 評估場景以 LLM serving infrastructure 為主，edge 或 consumer 設備上的適用性未討論。

---

## Workspace 關聯（評估，非既成結論）

- **context-management.md — Prompt Caching 核心原則**：SAECache 的核心發現（system prompt reuse rate 遠高於 user query）直接支持 workspace 規則「CLAUDE.md 內容 = 最穩定快取前綴，永遠放最前」——本論文提供了這一設計決策的實證基礎，並量化了不同 token 類型的 reuse value 差異（最高 756x）。
- **NLAH 原則（Right context > more context）**：SAECache 的 semantic-aware weighting 與 NLAH 精神一致——並非所有 context 等價，高 reuse value 的 token（穩定 system prompt）應優先保留，低 reuse 的動態 user query 可優先 evict。
- **跨切紀律「判斷 vs 決定」**：SAECache 的 online learning schema 示範了一種在 LLM serving 層做「決定」（哪個 block evict）而非讓 LLM 做「判斷」的架構分離——與 workspace 核心紀律的精神對應；⚠️ 直接移植到 prompt 組裝層需額外橋接。
- **`core.md §PROPOSE 委派`（原 subagent-strategy.md） — Fan-out token budget**：SAECache 的 multi-queue 設計（依 token 角色分流）啟發 multi-agent 工作流中按 token 類型（system context vs tool output vs model response）差異化管理 context 配額的可能；⚠️ 目前 workspace 無對應實作，屬概念延伸。
