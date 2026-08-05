---
url: "https://arxiv.org/abs/2602.19320"
title: "Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations"
archived_date: 2026-06-24
arxiv_id: 2602.1932
authors: ["Dongming Jiang", "Yi Li", "Songtao Wei", "Jinxin Yang", "Ayushi Kishore", "Alysa Zhao", "Dingyi Kang", "Xu Hu", "Feng Chen", "Qiannan Li", "Bingzhe Li"]
domains: [cs.CL]
html: "https://arxiv.org/html/2602.19320v1"
pdf_path: pdfs/2602.19320.pdf
published_date: 2026-02-22
---

# Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations

**Authors**: Dongming Jiang, Yi Li, Songtao Wei, Jinxin Yang, Ayushi Kishore, Alysa Zhao, Dingyi Kang, Xu Hu, Feng Chen, Qiannan Li, Bingzhe Li
**Published**: February 22, 2026
**Source**: https://arxiv.org/abs/2602.19320 · [HTML](https://arxiv.org/html/2602.19320v1)
**arXiv ID**: 2602.19320
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2602.19320.pdf](https://arxiv.org/abs/2602.19320) (19 pp, full text archived)

---

## Abstract (quoted)

> Agentic memory systems enable large language model (LLM) agents to maintain state across long interactions, supporting long-horizon reasoning and personalization beyond fixed context windows. Despite rapid architectural development, the empirical foundations of these systems remain fragile: existing benchmarks are often underscaled, evaluation metrics are misaligned with semantic utility, performance varies significantly across backbone models, and system-level costs are frequently overlooked. This survey presents a structured analysis of agentic memory from both architectural and system perspectives. We first introduce a concise taxonomy of MAG systems based on four memory structures. Then, we analyze key pain points limiting current systems, including benchmark saturation effects, metric validity and judge sensitivity, backbone-dependent accuracy, and the latency and throughput overhead introduced by memory maintenance. By connecting the memory structure to empirical limitations, this survey clarifies why current agentic memory systems often underperform their theoretical promise and outlines directions for more reliable evaluation and scalable system design.

---

## 結構化摘要

### 核心貢獻
- 從架構與系統雙視角對 agentic memory 做結構化分析（survey）。
- 提出基於四種記憶結構的 MAG 系統 concise taxonomy。
- 系統性點名當前痛點：benchmark saturation、metric validity 與 judge sensitivity、backbone-dependent accuracy、記憶維護的 latency/throughput 開銷。

### 關鍵結果
- 指出實證基礎脆弱：benchmark 規模不足、metric 與語意效用錯配、效能高度依賴 backbone 模型、系統成本常被忽略。
- 將「記憶結構 ↔ 實證限制」連結，解釋為何現有系統表現低於理論承諾，並列出更可靠評估與可擴展設計的方向。

### 限制
- survey 性質，無新方法/新實驗主結果；判斷弱點：taxonomy 的四結構劃分主觀，痛點分析依賴既有文獻品質。

---

## Workspace 關聯（評估，非既成結論）

- 「metric validity 與 judge sensitivity」「benchmark saturation」直接對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 dynamic workflow 三失敗模式與 core.md「LLM-judge verdict 非證據」——記憶評測同樣需防 self-preferential bias。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- 「backbone-dependent accuracy」呼應 model-selection-grid／subagent「能力下限」：記憶系統效能隨 backbone 變動 → 換模型世代須重評（呼應 Framework Integrity「規則=decaying cache」）。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- ⚠️ 落地門檻：屬綜述地圖，無可直接套用工具；價值在提供「評估記憶方法時的反幻覺檢查清單」。
