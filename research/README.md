# Research

> **Type:** wiki:index — compiled knowledge hub for SRE / Cloud Architect  
> LLMs: read this index to understand what's in `research/` before exploring subdirectories.

---

## Agent Quick Navigation

| Looking for... | Go to | Type |
|---------------|-------|------|
| Career experience / past decisions | `career-wiki/INDEX.md` → `zeuik-senior-architect` agent | wiki:compiled |
| Agent harness evaluation | `agent-harness/HARNESS-CARD.md` | eval |
| Latest AI news (7-day dashboard) | `ai-news/README.md` | wiki:auto |
| Claude Code official guidance | `claude-blog/README.md` | wiki:compiled |
| Academic papers | `papers/README.md` | raw:indexed |
| Per-model eval results | `evals/INDEX.md` | eval |
| Deep research reports | `reports/README.md` | wiki:generated |
| Claude Code best practices | `best-practices/INDEX.md` | wiki:compiled |
| Tweet / article archive | `tweets/README.md` | raw:indexed |

---

## Directory Map

| Sub-directory | Type | Size | Description |
|--------------|------|------|-------------|
| `career-wiki/` | wiki:compiled | 36 pages | Zeuik 8-segment career knowledge (Karpathy LLM Wiki pattern) |
| `agent-harness/` | wiki:compiled | 7 docs | CAR 14-component framework; HARNESS-CARD; RATCHET |
| `evals/` | eval | baseline + runs | Per-model eval suite (Haiku/Sonnet/Opus baselines) |
| `claude-blog/` | wiki:compiled | ~76 articles | claude.com/blog archive 2025-11→2026-05 |
| `ai-news/` | wiki:auto | 26 sources | Newsletter 90-day rolling archive (daily auto-ingest) |
| `ai-articles/` | raw:indexed | 59 articles | Karpathy×Mnilax scored; 48 in `scored/` |
| `best-practices/` | wiki:compiled | 29 docs | Official + community Claude Code best practices |
| `papers/` | raw:indexed | 86+ papers | Academic LLM/agent papers 2022–2026 |
| `reports/` | wiki:generated | 23 reports | autoresearch / overnight-research deep reports |
| `tweets/` | raw:indexed | 157+ | Twitter/X research archive |
| `videos/` | raw:indexed | 5 transcripts | YouTube research video transcripts |
| `substack-thestevekoh/` | raw:indexed | 177 articles | Steve Koh 繁中 Substack archive |
| `prompts/` | schema | 3 files | Research task prompt templates |
| `templates/` | schema | 3 files | ai-news / overnight-research / tweets templates |
| `RESEARCH-INDEX.md` | index | — | Full research index |
| `archive-index.md` | index | — | Archive summary; 30-day retention policy |

---

## Query Patterns

```
"Zeuik 在 KKStream 怎麼做 FinOps？"
  → zeuik-senior-architect agent → career-wiki/pages/finops-*.md

"最新的 LLM agent 論文有哪些？"
  → papers/README.md → browse by topic

"今天的 AI 新聞"
  → ai-news/README.md (7-day dashboard)

"Harness 目前評分多少？"
  → agent-harness/HARNESS-CARD.md

"最近有哪些深度研究報告？"
  → reports/README.md → sort by date
```
