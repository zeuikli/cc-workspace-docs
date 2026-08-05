---
url: "https://arxiv.org/abs/2601.07190"
title: "Active Context Compression: Autonomous Memory Management in LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2601.0719
authors: ["Nikhil Verma"]
domains: [cs.AI]
html: "https://arxiv.org/html/2601.07190v1"
pdf_path: pdfs/2601.07190.pdf
published_date: 2026-01-12
---

# Active Context Compression: Autonomous Memory Management in LLM Agents

**Authors**: Nikhil Verma
**Published**: January 12, 2026
**Source**: https://arxiv.org/abs/2601.07190 · [HTML](https://arxiv.org/html/2601.07190v1)
**arXiv ID**: 2601.07190
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2601.07190.pdf](https://arxiv.org/abs/2601.07190) (4 pp, full text archived)

---

## Abstract (quoted)

> Large Language Model (LLM) agents struggle with long-horizon software engineering tasks due to 'Context Bloat.' As interaction history grows, computational costs explode, latency increases, and reasoning capabilities degrade due to distraction by irrelevant past errors. Existing solutions often rely on passive, external summarization mechanisms that the agent cannot control. This paper proposes Focus, an agent-centric architecture inspired by the biological exploration strategies of Physarum polycephalum (slime mold). The Focus Agent autonomously decides when to consolidate key learnings into a persistent 'Knowledge' block and actively withdraws (prunes) the raw interaction history. Using an optimized scaffold matching industry best practices (persistent bash + string-replacement editor), we evaluated Focus on N=5 context-intensive instances from SWE-bench Lite using Claude Haiku 4.5. With aggressive prompting that encourages frequent compression, Focus achieves 22.7% token reduction (14.9M -> 11.5M tokens) while maintaining identical accuracy (3/5 = 60% for both agents). Focus performed 6.0 autonomous compressions per task on average, with token savings up to 57% on individual instances. We demonstrate that capable models can autonomously self-regulate their context when given appropriate tools and prompting, opening pathways for cost-aware agentic systems without sacrificing task performance.

---

## 結構化摘要

### 核心貢獻
- 提出 Focus：agent-centric 架構，受黏菌（Physarum polycephalum）探索策略啟發。Agent 自主決定何時把關鍵學習整合進持久的 'Knowledge' block，並主動 prune（撤回）raw interaction history。
- 對比過往「被動、外部、agent 無法控制」的摘要機制，強調自主可控的 context 自我調節。

### 關鍵結果
- 於 SWE-bench Lite N=5 context-intensive 實例、用 Claude Haiku 4.5 評估：token 減少 22.7%（14.9M→11.5M），準確率不變（兩 agent 皆 3/5 = 60%）。
- 平均每任務 6.0 次自主壓縮，單一實例 token 節省最高 57%。

### 限制
- 文件自述 N=5（極小樣本，4 頁短文）；判斷弱點：統計效力弱、單一 backbone（Haiku 4.5）、aggressive prompting 下的壓縮品質未做退化分析。

---

## Workspace 關聯（評估，非既成結論）

- 高度貼合本 workspace：以 Claude Haiku 4.5 + persistent bash + string-replacement editor 為 scaffold，幾乎是 `pilot`（tier=cost，原 `haiku-pilot`） + 本庫 Bash/Edit 工具鏈的鏡像。
- 「agent 自主決定何時 consolidate 並 prune raw history」對應 context-management 的主動 compact（30–35% 主動觸發）與 core.md RECORD checkpoint——把學習寫入 Knowledge block ≈ 更新 MEMORY/LESSONS。
- ⚠️ 落地門檻：N=5 樣本不足以背書；「aggressive 壓縮」與本庫「delta hint 防 context collapse」存在張力——自主 prune 須有 unverified_success 閘門防止刪掉 load-bearing 脈絡。
