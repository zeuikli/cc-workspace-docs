---
title: "Research"
type: index
---

# Research

> **Type:** wiki:index — compiled knowledge hub for SRE / Cloud Architect  
> LLMs: read this index to understand what's in `research/` before exploring subdirectories.

---

## Agent Quick Navigation

| Looking for... | Go to | Type |
|---------------|-------|------|
| Agent harness evaluation | [agent-harness/](./agent-harness/) | wiki:compiled |
| Latest AI news | [ai-news/](./ai-news/) | wiki:auto |
| Claude Code official guidance | [claude-blog/](./claude-blog/) | wiki:compiled |
| Academic papers | [papers/](./papers/) | raw:indexed |
| Deep research reports | [reports/](./reports/) | wiki:generated |
| Claude Code best practices | [best-practices/](./best-practices/) | wiki:compiled |
| Tweet / article archive | [tweets/](./tweets/) | raw:indexed |
| AI community articles | [ai-articles/](./ai-articles/) | raw:indexed |
| Research videos | [videos/](./videos/) | raw:indexed |

---

## Directory Map

| Sub-directory | Type | Size | Description |
|--------------|------|------|-------------|
| [`agent-harness/`](./agent-harness/) | wiki:compiled | 67 docs | CAR 14-component framework; SURVEY; KNOWLEDGE-MAP; RATCHET |
| [`claude-blog/`](./claude-blog/) | wiki:compiled | 9 articles | claude.com/blog archive 2025-11→2026-05 |
| [`ai-news/`](./ai-news/) | wiki:auto | 529 files | Newsletter 90-day rolling archive (daily auto-ingest) |
| [`ai-articles/`](./ai-articles/) | raw:indexed | 123 articles | Karpathy×Mnilax scored; community AI engineering articles |
| [`best-practices/`](./best-practices/) | wiki:compiled | 27 docs | Official + community Claude Code best practices |
| [`papers/`](./papers/) | raw:indexed | 96 papers | Academic LLM/agent papers 2022–2026 |
| [`reports/`](./reports/) | wiki:generated | 18 reports | autoresearch / overnight-research deep reports |
| [`tweets/`](./tweets/) | raw:indexed | 158+ | Twitter/X research archive |
| [`videos/`](./videos/) | raw:indexed | 6 transcripts | YouTube research video transcripts |
| [`prompts/`](./prompts/) | schema | 9 files | Research task prompt templates |
| [`templates/`](./templates/) | schema | 4 files | ai-news / overnight-research / tweets templates |
| [`RESEARCH-INDEX.md`](./RESEARCH-INDEX) | index | — | Full research index |
| [`archive-index.md`](./archive-index) | index | — | Archive summary; 30-day retention policy |

---

## Query Patterns

```
"最新的 LLM agent 論文有哪些？"
  → papers/index.md → browse by topic

"今天的 AI 新聞"
  → ai-news/index.md (rolling archive)

"Harness 架構研究"
  → agent-harness/index.md

"最近有哪些深度研究報告？"
  → reports/index.md → sort by date

"Claude Code 最佳實踐"
  → best-practices/index.md
```
