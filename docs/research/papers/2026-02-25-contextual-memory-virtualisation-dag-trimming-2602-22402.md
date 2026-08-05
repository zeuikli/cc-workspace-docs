---
url: "https://arxiv.org/abs/2602.22402"
title: "Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2602.22402
authors: ["Cosmo Santoni"]
domains: [cs.SE]
html: "https://arxiv.org/html/2602.22402v1"
pdf_path: pdfs/2602.22402.pdf
published_date: 2026-02-25
---

# Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents

**Authors**: Cosmo Santoni
**Published**: February 25, 2026
**Source**: https://arxiv.org/abs/2602.22402 · [HTML](https://arxiv.org/html/2602.22402v1)
**arXiv ID**: 2602.22402
**Categories**: cs.SE
**PDF**: [research/papers/pdfs/2602.22402.pdf](https://arxiv.org/abs/2602.22402) (11 pp, full text archived)

---

## Abstract (quoted)

> As large language models engage in extended reasoning tasks, they accumulate significant state -- architectural mappings, trade-off decisions, codebase conventions -- within the context window. This understanding is lost when sessions reach context limits and undergo lossy compaction. We propose Contextual Memory Virtualisation (CMV), a system that treats accumulated LLM understanding as version-controlled state. Borrowing from operating system virtual memory, CMV models session history as a Directed Acyclic Graph (DAG) with formally defined snapshot, branch, and trim primitives that enable context reuse across independent parallel sessions. We introduce a three-pass structurally lossless trimming algorithm that preserves every user message and assistant response verbatim while reducing token counts by a mean of 20% and up to 86% for sessions with significant overhead by stripping mechanical bloat such as raw tool outputs, base64 images, and metadata. A single-user case-study evaluation across 76 real-world coding sessions demonstrates that trimming remains economically viable under prompt caching, with the strongest gains in mixed tool-use sessions, which average 39% reduction and reach break-even within 10 turns. A reference implementation is available at https://github.com/CosmoNaught/claude-code-cmv.

---

## 結構化摘要

### 核心貢獻
- 提出 CMV（Contextual Memory Virtualisation）：將累積的 LLM 理解視為「版本控制狀態」，借用 OS virtual memory，將 session 歷史建模為 DAG，並定義 snapshot / branch / trim primitive，支援跨獨立平行 session 的 context reuse。
- 提出 three-pass structurally lossless trimming 演算法：逐字保留每則 user message 與 assistant response，僅剝除 raw tool output、base64 image、metadata 等 mechanical bloat。

### 關鍵結果
- token 平均減少 20%，高 overhead session 最高減少 86%。
- 76 個真實 coding session 的單使用者 case study：prompt caching 下 trimming 仍具經濟性；mixed tool-use session 平均減少 39%，10 turn 內達 break-even。

### 限制
- 文件自述為「single-user case-study」（76 session）；判斷弱點：單一使用者、樣本侷限，泛化性待補；trim 雖 structurally lossless 但剝除 tool output 可能損及後續推理可追溯性。

---

## Workspace 關聯（評估，非既成結論）

- 高度貼合本庫 context-management：DAG snapshot/branch/trim ≈ /rewind + worktree 平行 session；「逐字保留 user/assistant、只剝 mechanical bloat」正是 compact「delta hint 非全量 rewrite」「file path/error string 原文勿改寫」的精神。
- 「prompt caching 下仍經濟、10 turn break-even」直接呼應 context-management 的 Cache 健康指標（cache_read/input_tokens >0.7）。
- 參考實作為 `claude-code-cmv`（Claude Code 生態）→ 與本 workspace 工具鏈天然相容；⚠️ 落地門檻：本庫目前以 markdown handoff + hook 維護狀態，導入 DAG 化 session 管理屬可評估但未驗證的擴充。
