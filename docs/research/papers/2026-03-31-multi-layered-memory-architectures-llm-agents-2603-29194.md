---
url: "https://arxiv.org/abs/2603.29194"
title: "Multi-Layered Memory Architectures for LLM Agents: An Experimental Evaluation of Long-Term Context Retention"
archived_date: 2026-06-24
arxiv_id: 2603.29194
authors: ["Sunil Tiwari", "Payal Fofadiya"]
domains: [cs.CV]
html: "https://arxiv.org/html/2603.29194v1"
pdf_path: pdfs/2603.29194.pdf
published_date: 2026-03-31
---

# Multi-Layered Memory Architectures for LLM Agents: An Experimental Evaluation of Long-Term Context Retention

**Authors**: Sunil Tiwari, Payal Fofadiya
**Published**: March 31, 2026
**Source**: https://arxiv.org/abs/2603.29194 · [HTML](https://arxiv.org/html/2603.29194v1)
**arXiv ID**: 2603.29194
**Categories**: cs.CV
**PDF**: [research/papers/pdfs/2603.29194.pdf](https://arxiv.org/abs/2603.29194) (8 pp, full text archived)

---

## Abstract (quoted)

> Long-horizon dialogue systems suffer from semantic drift and unstable memory retention across extended sessions. This paper presents a Multi-Layer Memory Framework that decomposes dialogue history into working, episodic, and semantic layers with adaptive retrieval gating and retention regularization. The architecture controls cross-session drift while maintaining bounded context growth and computational efficiency. Experiments on LOCOMO, LOCCO, and LoCoMo show improved performance, achieving 46.85 Success Rate, 0.618 overall F1 with 0.594 multi-hop F1, and 56.90% six-period retention while reducing false memory rate to 5.1% and context usage to 58.40%. Results confirm enhanced long-term retention and reasoning stability under constrained context budgets.

---

## 結構化摘要

### 核心貢獻
- 提出 Multi-Layer Memory Framework：將對話歷史拆為 working / episodic / semantic 三層，搭配 adaptive retrieval gating 與 retention regularization。
- 在控制 cross-session drift 的同時維持 bounded context growth 與計算效率。

### 關鍵結果
- 於 LOCOMO / LOCCO / LoCoMo：Success Rate 46.85、overall F1 0.618、multi-hop F1 0.594、six-period retention 56.90%。
- false memory rate 降至 5.1%，context usage 降至 58.40%。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：2 作者短篇（8 頁），benchmark 名稱（LOCOMO/LOCCO/LoCoMo）疑有重複，需正文確認；retention 56.90% 仍偏低。

---

## Workspace 關聯（評估，非既成結論）

- 「bounded context growth + context usage 降至 58.40%」直接對應 context-management 的 token budget 與 compact 觸發閾值。
- working/episodic/semantic 三層對應本批 LightMem 的 STM/MTM/LTM；可作為理解本庫 MEMORY（語意層）vs handoff/progress（情節層）vs 即時對話（working）的概念框架。
- 「false memory rate 5.1%」呼應 core.md TEST「Fail Loud」與 RECORD——記憶系統須可觀測退化（false memory 即一種退化訊號）。
