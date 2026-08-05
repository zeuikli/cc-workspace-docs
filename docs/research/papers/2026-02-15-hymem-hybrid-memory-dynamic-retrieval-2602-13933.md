---
url: "https://arxiv.org/abs/2602.13933"
title: "HyMem: Hybrid Memory Architecture with Dynamic Retrieval Scheduling"
archived_date: 2026-06-24
arxiv_id: 2602.13933
authors: ["Xiaochen Zhao", "Kaikai Wang", "Xiaowen Zhang", "Chen Yao", "Aili Wang"]
domains: [cs.AI]
html: "https://arxiv.org/html/2602.13933v1"
pdf_path: pdfs/2602.13933.pdf
published_date: 2026-02-15
---

# HyMem: Hybrid Memory Architecture with Dynamic Retrieval Scheduling

**Authors**: Xiaochen Zhao, Kaikai Wang, Xiaowen Zhang, Chen Yao, Aili Wang
**Published**: February 15, 2026
**Source**: https://arxiv.org/abs/2602.13933 · [HTML](https://arxiv.org/html/2602.13933v1)
**arXiv ID**: 2602.13933
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2602.13933.pdf](https://arxiv.org/abs/2602.13933) (18 pp, full text archived)

---

## Abstract (quoted)

> Large language model (LLM) agents demonstrate strong performance in short-text contexts but often underperform in extended dialogues due to inefficient memory management. Existing approaches face a fundamental trade-off between efficiency and effectiveness: memory compression risks losing critical details required for complex reasoning, while retaining raw text introduces unnecessary computational overhead for simple queries. The crux lies in the limitations of monolithic memory representations and static retrieval mechanisms, which fail to emulate the flexible and proactive memory scheduling capabilities observed in humans, thus struggling to adapt to diverse problem scenarios. Inspired by the principle of cognitive economy, we propose HyMem, a hybrid memory architecture that enables dynamic on-demand scheduling through multi-granular memory representations. HyMem adopts a dual-granular storage scheme paired with a dynamic two-tier retrieval system: a lightweight module constructs summary-level context for efficient response generation, while an LLM-based deep module is selectively activated only for complex queries, augmented by a reflection mechanism for iterative reasoning refinement. Experiments show that HyMem achieves strong performance on both the LOCOMO and LongMemEval benchmarks, outperforming full-context while reducing computational cost by 92.6%, establishing a state-of-the-art balance between efficiency and performance in long-term memory management.

---

## 結構化摘要

### 核心貢獻
- 提出 HyMem：受 cognitive economy 啟發的 hybrid memory 架構，透過 multi-granular 記憶表徵實現 dynamic on-demand scheduling。
- dual-granular storage + dynamic two-tier retrieval：lightweight 模組建構 summary-level context 供高效生成；LLM-based deep 模組僅在 complex query 時選擇性啟動，並以 reflection 機制做 iterative reasoning refinement。

### 關鍵結果
- 於 LOCOMO 與 LongMemEval 表現強勁，outperform full-context 同時降低計算成本 92.6%。
- 在效率與效能間建立 SOTA 平衡。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：deep 模組「何時啟動」的 gating 準確度未在 abstract 量化，誤判將損及複雜查詢；92.6% 成本下降為相對 full-context，基準偏寬鬆。

---

## Workspace 關聯（評估，非既成結論）

- 「lightweight 模組常駐 + deep 模組僅 complex query 啟動」精準對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的委派決策與 multi-mode：簡單任務走 Haiku/inline，複雜才升 Sonnet/Opus，是 effort-first 紀律的記憶層映射。
- 「降低計算成本 92.6% 而不犧牲效能」呼應 context-management token budget 與 `pilot`（tier=cost，原 `haiku-pilot`） 成本紀律。
- two-tier retrieval（粗→深）+ reflection 對應 core.md「判斷 vs 決定」分層與 RECORD 反思迴圈；⚠️ gating 誤判風險對應「unverified_success 閘門」——deep 模組未啟動時不得假設淺層結果完整。
