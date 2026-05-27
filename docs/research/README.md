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
| Agent harness evaluation | `agent-harness/README.md` | wiki:compiled |
| Latest AI news (7-day dashboard) | `ai-news/README.md` | wiki:auto |
| Claude Code official guidance | `claude-blog/README.md` | wiki:compiled |
| Academic papers | `papers/README.md` | raw:indexed |
| Deep research reports | `reports/README.md` | wiki:generated |
| Claude Code best practices | `best-practices/INDEX.md` | wiki:compiled |
| Tweet / article archive | `tweets/README.md` | raw:indexed |

---

## Directory Map

| Sub-directory | Type | Size | Description |
|--------------|------|------|-------------|
| `agent-harness/` | wiki:compiled | 6 docs | CAR framework; RESEARCH; SURVEY; KNOWLEDGE-MAP |
| `claude-blog/` | wiki:compiled | ~76 articles | claude.com/blog archive 2025-11→2026-05 |
| `ai-news/` | wiki:auto | 66 digests | Newsletter 90-day rolling archive (daily auto-ingest) |
| `ai-articles/` | raw:indexed | 59 articles | Karpathy×Mnilax scored; 48 in `scored/` |
| `best-practices/` | wiki:compiled | 29 docs | Official + community Claude Code best practices |
| `papers/` | raw:indexed | 86+ papers | Academic LLM/agent papers 2022–2026 |
| `reports/` | wiki:generated | 18 reports | autoresearch / overnight-research deep reports |
| `tweets/` | raw:indexed | 160 | Twitter/X research archive |
| `videos/` | raw:indexed | 6 transcripts | YouTube research video transcripts |
| `prompts/` | schema | 3 files | Research task prompt templates |
| `templates/` | schema | 3 files | ai-news / overnight-research / tweets templates |
| `RESEARCH-INDEX.md` | index | — | Full research index |
| `archive-index.md` | index | — | Archive summary; 30-day retention policy |

---

## Query Patterns

```
"最新的 LLM agent 論文有哪些？"
  → papers/README.md → browse by topic

"今天的 AI 新聞"
  → ai-news/README.md (7-day dashboard)

"Agent harness 研究資源"
  → agent-harness/README.md → RESEARCH.md / SURVEY.md

"最近有哪些深度研究報告？"
  → reports/README.md → sort by date
```
