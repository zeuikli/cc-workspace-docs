---
url: "https://arxiv.org/abs/2604.01707"
title: "Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework"
archived_date: 2026-06-24
arxiv_id: 2604.01707
authors: ["Yanchen Wu", "Tenghui Lin", "Yingli Zhou", "Fangyuan Zhang", "Qintian Guo", "Xun Zhou", "Sibo Wang", "Xilin Liu", "Yuchi Ma", "Yixiang Fang"]
domains: [cs.CL]
html: "https://arxiv.org/html/2604.01707v1"
pdf_path: pdfs/2604.01707.pdf
published_date: 2026-04-01
---

# Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework

**Authors**: Yanchen Wu, Tenghui Lin, Yingli Zhou, Fangyuan Zhang, Qintian Guo, Xun Zhou, Sibo Wang, Xilin Liu, Yuchi Ma, Yixiang Fang
**Published**: April 01, 2026
**Source**: https://arxiv.org/abs/2604.01707 · [HTML](https://arxiv.org/html/2604.01707v1)
**arXiv ID**: 2604.01707
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2604.01707.pdf](https://arxiv.org/abs/2604.01707) (20 pp, full text archived)

---

## Abstract (quoted)

> Memory emerges as the core module in the large language model (LLM)-based agents for long-horizon complex tasks (e.g., multi-turn dialogue, game playing, scientific discovery), where memory can enable knowledge accumulation, iterative reasoning and self-evolution. A number of memory methods have been proposed in the literature. However, these methods have not been systematically and comprehensively compared under the same experimental settings. In this paper, we first summarize a unified framework that incorporates all the existing agent memory methods from a high-level perspective. We then extensively compare representative agent memory methods on two well-known benchmarks and examine the effectiveness of all methods, providing a thorough analysis of those methods. As a byproduct of our experimental analysis, we also design a new memory method by exploiting modules in the existing methods, which outperforms the state-of-the-art methods. Finally, based on these findings, we offer promising future research opportunities. We believe that a deeper understanding of the behavior of existing methods can provide valuable new insights for future research.

---

## 結構化摘要

### 核心貢獻
- 提出一個高層次 unified framework，將既有 agent memory 方法統合納入同一視角。
- 在相同實驗設定下，對代表性方法於兩個知名 benchmark 做系統性、全面比較（補足過往「設定不一致無法公平比較」的缺口）。
- 作為分析副產物，藉組合既有方法的模組設計出一個新記憶方法，超越 SOTA。

### 關鍵結果
- 統一設定下的對照揭示各方法有效性差異；組合式新方法 outperform state-of-the-art（abstract 未列具體數字）。
- 提出未來研究方向清單。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：survey + 實驗綜合論文，新方法的增益幅度未在 abstract 量化；僅兩 benchmark，外部效度待補。

---

## Workspace 關聯（評估，非既成結論）

- 「同設定下公平比較」呼應 core.md TEST 的 unverified_success 閘門與 `core.md §PROPOSE 委派`（原 subagent-strategy.md）「verdict 非證據，須機械重驗」——記憶方法宣稱的增益須在受控設定下重驗。
- unified framework 的「模組化拆解」對應本批多篇（LightMem/HyMem）共同的 retrieval/write/consolidate 分層，可作為比較記憶設計時的共同詞彙。
- ⚠️ 落地門檻：屬學術 benchmark 對照研究，與本庫 markdown 記憶層無直接映射；價值在提供「記憶方法分類」的概念地圖。
