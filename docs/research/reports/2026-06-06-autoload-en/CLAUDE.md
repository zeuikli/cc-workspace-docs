# CLAUDE.md
> Traditional Chinese preferred · English supported · Tasks unrelated to this workspace → `/clear`.
> Sub-agents do not inherit this file; parent instructs sub-agent "Read AGENTS.md first".
> This file ≤ 200 lines (Mnilax: compliance drops sharply beyond this). Auto-load five-source byte threshold (three-tier soft limit, canonical unit: byte) — see core.md §Framework Integrity.

## The Loop (Behavioral Contract — Six-Phase Meta-Loop)

> Each phase answers "which failure mode does this prevent?". Reference basis: Karpathy R1–R4 + Mnilax R5–R12 (original 12 rules reorganized into six phases). Mandatory clauses = `core.md`; checklist + paper grounding = `refs/karpathy-mnilax-best-solution.md`. Improvement/audit tasks follow these six phases, each mechanically verifiable (bash/test); gate before destructive APPLY.

| Phase | Discipline | Prevents |
|-------|-----------|----------|
| **OBSERVE** | Read before acting + on-rails/off-rails classification | Editing without reading |
| **IDENTIFY** | Surface assumptions + verifiable success criteria (incl. four-dimension quality) | Silent assumptions / weak criteria |
| **PROPOSE** | Minimal + surgical (AI four-defect self-check) | Over-engineering / peripheral pollution |
| **APPLY** | Convention-first + destructive gate (derivable = noise) | silent fork |
| **TEST** | Tests verify intent + Fail Loud/PGE/unverified_success | Fake tests / silent failure |
| **RECORD** | Checkpoint + reflection into store (self-evolution) | Running on broken state |
| **Cross-cutting** | Judgment vs. decision / surface contradictions / Token budget | LLM making deterministic decisions / mixing contradictions / loop runaway |

## Always-loaded Rules (Auto-load)

- @.claude/rules/core.md — The Loop six-phase mandatory clauses · cross-cutting discipline · Git workflow · production red lines
- @.claude/rules/context-management.md — Token budget · Compact · Prompt Caching
- @.claude/rules/output-discipline.md — No preamble · filler words banned · concise output (cross-cuts all phases)
- @.claude/rules/subagent-strategy.md — Delegation decision · Fan-out · Advisor mode

> `.claude/rules/security-hygiene.md` is path-scoped on-demand (triggered when editing .env / credentials files).

## Modes & Effort

> **Modes**: Default Sonnet 4.6; `/haiku-pilot` (cost) `/sonnet-pilot` (quality) `/opus-pilot` (architecture/security).
> **Effort (Opus 4.8)**: `/effort low`(quick)·`high`(daily)·`xhigh`(agentic/review)·`max`(hardest)·`/fast`(refactor)·`ultracode`(=xhigh+dynamic workflow). Matrix+pricing in `refs/pilot-shared-preflights.md` §E.
