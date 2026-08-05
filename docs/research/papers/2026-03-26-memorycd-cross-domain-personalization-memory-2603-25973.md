---
url: "https://arxiv.org/abs/2603.25973"
title: "MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization"
archived_date: 2026-06-24
arxiv_id: 2603.25973
authors: ["Weizhi Zhang", "Xiaokai Wei", "Wei-Chieh Huang", "Zheng Hui", "Chen Wang", "Michelle Gong", "Philip S. Yu"]
domains: [cs.CL]
html: "https://arxiv.org/html/2603.25973v1"
pdf_path: pdfs/2603.25973.pdf
published_date: 2026-03-26
---

# MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization

**Authors**: Weizhi Zhang, Xiaokai Wei, Wei-Chieh Huang, Zheng Hui, Chen Wang, Michelle Gong, Philip S. Yu
**Published**: March 26, 2026
**Source**: https://arxiv.org/abs/2603.25973 · [HTML](https://arxiv.org/html/2603.25973v1)
**arXiv ID**: 2603.25973
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2603.25973.pdf](https://arxiv.org/abs/2603.25973) (22 pp, full text archived)

---

## Abstract (quoted)

> Recent advancements in Large Language Models (LLMs) have expanded context windows to million-token scales, yet benchmarks for evaluating memory remain limited to short-session synthetic dialogues. We introduce MemoryCD, the first large-scale, user-centric, cross-domain memory benchmark derived from lifelong real-world behaviors in the Amazon Review dataset. Unlike existing memory datasets that rely on scripted personas to generate synthetic user data, MemoryCD tracks authentic user interactions across years and multiple domains. We construct a multi-faceted long-context memory evaluation pipeline of 14 state-of-the-art LLM base models with 6 memory method baselines on 4 distinct personalization tasks over 12 diverse domains to evaluate an agent's ability to simulate real user behaviors in both single and cross-domain settings. Our analysis reveals that existing memory methods are far from user satisfaction in various domains, offering the first testbed for cross-domain life-long personalization evaluation.

---

## 結構化摘要

### 核心貢獻
- 提出 MemoryCD：首個大規模、user-centric、cross-domain 記憶 benchmark，源自 Amazon Review 的真實終身行為（非腳本化 persona 合成資料）。
- 追蹤跨年、跨多領域的真實使用者互動，補足「現有 benchmark 僅短 session 合成對話」的缺口。

### 關鍵結果
- 評估管線涵蓋 14 個 SOTA base model + 6 個 memory method baseline、4 種 personalization 任務、12 個領域，覆蓋 single 與 cross-domain 設定。
- 分析顯示現有記憶方法在各領域「far from user satisfaction」——cross-domain 終身個人化仍是開放難題。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：以 Amazon Review 行為近似「記憶」，與對話式記憶的對齊度待商榷；隱私/資料偏差未在 abstract 討論。

---

## Workspace 關聯（評估，非既成結論）

- cross-domain personalization 對應 2606.09483 的 cross-domain schema induction——兩篇共同指出「跨域抽象」是當前記憶系統最弱環節。
- 「真實資料 vs 腳本 persona」呼應 core.md TEST「測試要能在業務邏輯改變時失敗」——合成 benchmark 易過擬合，真實分布才暴露缺陷。
- ⚠️ 落地門檻：屬電商個人化評測，與本庫工程記憶（決策/LESSONS）域外；價值在「真實長期行為才是記憶系統試金石」的方法論啟示。
