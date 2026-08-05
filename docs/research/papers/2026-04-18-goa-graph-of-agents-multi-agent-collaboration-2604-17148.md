---
url: "https://arxiv.org/abs/2604.17148"
title: "Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration"
archived_date: 2026-07-26
arxiv_id: 2604.17148
authors: ["Sukwon Yun", "Jie Peng", "Pingzhi Li", "Wendong Fan", "Jie Chen", "James Zou", "Guohao Li", "Tianlong Chen"]
domains: [cs.AI]
pdf_path: pdfs/2604.17148.pdf
published_date: 2026-04-18
---

# Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration

**Authors**: Sukwon Yun, Jie Peng, Pingzhi Li, Wendong Fan, Jie Chen, James Zou, Guohao Li, Tianlong Chen
**Published**: April 18, 2026
**Source**: https://arxiv.org/abs/2604.17148
**arXiv ID**: 2604.17148
**Categories**: cs.AI
**Code**: https://github.com/UNITES-Lab/GoA
**PDF**: [research/papers/pdfs/2604.17148.pdf](https://arxiv.org/abs/2604.17148)

> **Gotcha**：本論文 arXiv 無 HTML 全文版本（`/html/2604.17148v1` 回 404，僅提供 PDF 與 TeX 原始碼），故無 `html` frontmatter 欄位；結構化摘要改由 PDF 全文（pymupdf4llm 擷取）交叉核對 WebFetch 摘要後撰寫。

---

## Abstract (quoted)

> With an ever-growing zoo of LLMs and benchmarks, the need to orchestrate multiple models for improved task performance has never been more pressing. While frameworks like Mixture-of-Agents (MoA) attempt to coordinate LLMs, they often fall short in terms of (1) selecting relevant agents, (2) facilitating effective intra-agent communication, and (3) integrating responses efficiently. In this work, we propose Graph-of-Agents (GoA), a new graph-based framework for modeling multi-agent LLM communication. Our approach begins with node sampling, selecting only the most relevant agents by leveraging model cards that summarize each model's domain, task specialization, and other characteristics. Next, we construct edges between the selected agents by evaluating their responses against one another to determine relevance ordering. Directed message passing is then performed from highly relevant agents to less relevant ones to enhance their responses, followed by reverse message passing to refine the original responses of the more relevant agents. Finally, the updated responses are aggregated via graph-based pooling (e.g., max or mean pooling) to produce a single, unified answer. We evaluate GoA on diverse multi-domain benchmarks (MMLU, MMLU-Pro, GPQA) and domain-specific benchmarks (MATH, HumanEval, MedMCQA), with an agent pool of 6 LLMs spanning multiple domains. Surprisingly, GoA achieves superior performance using only 3 selected agents, outperforming recent multi-agent LLM baselines that utilize all 6 agents simultaneously. By adopting a graph structure, GoA offers both scalability and effectiveness through structured message passing-positioning it as a strong candidate for navigating the challenges of the ever-growing LLM zoo.

---

## 結構化摘要

### 核心貢獻

- **Node sampling**：用 model card（domain / task specialization）做 Top-k 篩選相關 agent，過濾無關領域模型以防止 agent explosion
- **Edge construction**：讓被選 agent 互評彼此回應以決定 relevance ordering，建構 query-specific graph（而非固定拓撲）
- **雙向 directed message passing**：先由高相關度 agent 流向低相關度 agent（enhance 對方回應），再反向流回（refine 原始高相關度 agent 的回應）
- **Graph pooling**（max / mean）聚合最終答案；程式碼開源 https://github.com/UNITES-Lab/GoA

### 關鍵結果

- 6-LLM agent pool（7–8B 參數，涵蓋 General/Code/Math/Biomedical/Finance/Legal），Top-k=3；在 MMLU / MMLU-Pro / GPQA（多領域）與 MATH / HumanEval / MedMCQA（領域專用）上評測
- **僅用 3 個 agent 即超越使用全部 6 個 agent 的 baseline**（Debate / Self-Consistency / Refine / ReConcile / MoA / Self-MoA）：GoA-Max 平均最高，MMLU 79.18、MMLU-Pro 54.78、MedMCQA 60.04；GoA-Mean 在 GPQA 40.54、MATH 73.12、HumanEval 84.98 最佳
- 效率（MMLU-Pro）：相較 MoA 減少 LLM 呼叫數、token 用量與延遲，同時準確度更高
- gpt-4o 規模擴展測試：GoA（3 agent）優於 DyLAN（8 個專門 agent）
- 消融：反轉 message-passing 方向造成最大性能下降（MMLU-Pro −2.60、GPQA −5.05）；top-k=2 限制多樣性、k=5 略降；邊閾值 τ=0.05 為最佳平衡點（過稀疏 τ=0.1/0.2 有害）

### 限制

- 論文未設獨立 Limitations 章節，Conclusion 僅重申貢獻，未討論失效模式
- 判斷弱點：top-k / τ 為手調超參數且敏感度高（消融顯示選擇顯著影響效果），跨任務自動調參未驗證
- 主力評測集中在 7–8B 開源模型 pool，僅一項 gpt-4o scaling-up 測試涵蓋專有模型，跨模型規模/家族的穩健性證據有限
- Graph pooling 聚合策略（max/mean）相對簡單，對高衝突回應的處理未深入探討

---

## Workspace 關聯（評估，非既成結論）

- 「用 model card 做 node sampling 過濾無關 agent」與 `core.md §PROPOSE 委派`（原 `graph.md §G3`）「fan-out 有上限」「brief 不清時越大越虧」同源：GoA 實證顯示 3 個相關 agent 勝過 6 個全量 agent，是「多不如準」的量化佐證。
- Bidirectional message passing（先高→低相關度 enhance、再低→高相關度 refine 回饋）補強 `core.md §PROPOSE 委派`（原 `graph.md §G2`）「verify 靠視角互斥取勝」——提供一個可具體實作的雙向修正範式。⚠️ 論文的 agent 是同質 LLM pool 互評，非本 workspace 現行 parent↔child 單向委派拓撲，能否直接遷移未驗證。
