# HarnessCard — cc-workspace

> Standard disclosure per P01 §6.2 (He et al. 2026-04-23). Full template: `research/papers/2026-04-23-harness-engineering-language-agents-car.md:268`
> Generated: 2026-05-08 | Updated: 2026-05-25 | Scope: personal SRE/Cloud Architect workspace

<!-- harness-audit 2026-05-25: PostToolUseFailure + Notification hooks added (hooks 13→15); healthcheck.sh import yaml → re-based parse (PASS 100/WARN 3/FAIL 0); token 3,412→3,542 tok (+130: Scratchpad + child-output rules); score 13.0/14; 5 items from v2.1.147-149 alignment -->
<!-- harness-audit 2026-05-23b: P0 harness-engineering.md 遷移至 skill（tier: on-demand 為非官方欄位，Claude Code 不識別；改用 /harness-meta skill 按需載入）；P1 移除 [FF]/[FB] 40 個標記（~40 tok）；measure.sh 修正（paths: frontmatter 偵測）；token 3,467 → 3,412 tok（-55 tok，CAR hard cap 4,500，餘裕 1,088 tok 24%）；PASS 94 / WARN 2 / FAIL 0 -->
<!-- harness-audit 2026-05-23: opus-pilot 二次評估 + harness-meta 全量審查；新增 latent-audit.sh / context-budget.sh / research-hub:gh-profile / review-hub:debug 增強 / session-stop.sh Memory 閾值；token 3,467 tok（workspace 目標 3,500 ✅；CAR hard cap 4,500，餘裕 1,033 tok 23%）；score 13.0/14；auto-load 不變 -->
<!-- harness-audit 2026-05-19: harness-engineering.md frontmatter fix; skills 40→17; token 3,423→3,583→3,467 tok (大道至簡 pass); score 13.0/14 -->

---

## Base Model

- **Primary**: claude-sonnet-4-6 (settings.json:model default, 2026-05-13 起；quality-first baseline)
- **Advisor / deep-review**: claude-opus-4-7 (via `advisor()` and `reviewer` agent)
- **Cost-first opt-in**: claude-haiku-4-5 (via `/haiku-pilot` at session start; sub-agents researcher/architecture-explorer 仍可獨立宣告 haiku)
- **Decoding**: alwaysThinkingEnabled=false; stream watchdog 600s; API timeout 900s
- **Fine-tuning**: none; behavior governed by rules + hooks (see Control Artifacts)

## Control Artifacts

- **Auto-loaded rules (4)**: core.md, subagent-strategy.md, context-management.md, output-discipline.md（**3,298 tok** ✅；Known Gotchas + dispatch table + surgical table + Rule 5 examples 已移至 on-demand refs/；harness-engineering.md 已遷移至 `.claude/skills/harness-meta/` skill，按需載入）
- **AGENTS.md**: cross-tool root manifest; agent roster with Do/Don't, delegation rules, safety boundaries, Known Limitations
- **Tool schemas**: 14 agents (`.claude/agents/*.md`) each declare `tools:` frontmatter; 18 skills each declare `allowed-tools:` frontmatter
- **Safety policy**: block-dangerous.sh allow-list v2 (deny-by-default for Bash); protect-sensitive-files.sh; audit-permission.sh (PermissionRequest hook); prod 二次確認 (core.md §prod 紅線)
- **Sandbox disclosure**: allow-list 層（⚠️ 有意識技術債）；無 OCI/gVisor container isolation。個人 workspace cost/benefit 評估後 DEFERRED。
- **Architecture rules**: subagent-strategy.md（trigger conditions）; refs/subagent-dispatch.md（dispatch table + Advisor matrix）; model-selection-grid.md escalation ladder

## Runtime Policies

- **Memory**: autoMemoryEnabled=true (Auto Memory across sessions); memory-archive.sh (PreCompact hook: archives oldest sessions to Memory-archive-YYYY-MM.md when Memory.md exceeds limit)
- **Context strategy**: compact 三層觸發 — 行為信號 > 數字閾值(70%) > 定時器(每300-400K tokens); context-management.md auto-loaded
- **Retry policy**: git push retry 4× exponential (2s/4s/8s/16s); tool errors reported, not swallowed
- **Budget**: BASH_DEFAULT_TIMEOUT=300s, BASH_MAX_TIMEOUT=600s; auto-load token CAR hard cap 4,500（`scripts/measure.sh` enforced，現況 **3,298 tok** ✅，CAR 餘裕 1,202 tok 26.7%）; per-task 4k / per-session 30k（context-management.md）
- **Checkpoint**: claude-progress.json per long-horizon task; session-init.sh / session-stop.sh lifecycle hooks

## Action Substrate

- **Shell**: Bash with allow-list (block-dangerous.sh); permitted prefixes: git, ls, wc, find, cat, echo, curl -s, python3, bash scripts/healthcheck.sh
- **Filesystem**: Read/Write/Edit/Grep/Glob (unrestricted within project)
- **Agent spawn**: Agent tool (fan-out sub-agents); 14 specialist agents; 18 skills
- **Web**: WebFetch, WebSearch (available in researcher/general-purpose agents)
- **MCP**: GitHub MCP (zeuikli/cc-workspace scope); 3712d42e drive MCP
- **Error handling**: PreToolUse hooks block before execution; PostToolUse audit-log.sh; healthcheck.sh 12-section PASS/WARN/FAIL

## Execution Topology

- **Pattern**: Single parent session + fan-out sub-agents (≥3 independent tasks or ≥10 files triggers delegation); 15 hooks 完整覆蓋
- **Planner-Executor**: plan-mode-expert (planning) → implementer/haiku-implementer (execution)
- **Evaluator**: /deep-review skill (commit-time) + healthcheck.sh; reviewer agent (Opus) for architecture
- **PGE enforcement**: Generator ≠ Evaluator (core.md §PGE 原則); pre-commit-review.sh hook enforces
- **No Message Bus**: multi-agent coordination via parent orchestrator only (A3 deferred; SCORING 5.45/10)

## Feedback Mechanisms

- **Success signal**: healthcheck.sh PASS; /deep-review approval; git push success
- **Failure signal**: hook exit codes (block-dangerous returns non-zero); test failures shown in full (core.md)
- **Observability**: audit-log.sh (PostToolUse Bash) + failure-log.sh (PostToolUseFailure) + notification-log.sh (Notification); harness-audit 14-component CAR scorecard; PASS 101 / WARN 2 / FAIL 0 (2026-05-25)
- **Error interpretation**: pre-commit-review.sh pre-commit gate; self-correcting loop in harness-eval (max 2 re-scans)

## Governance Structures

- **Human oversight**: prod 環境 apply/deploy/delete → MUST show plan/diff + explicit confirmation (core.md §prod 紅線)
- **Escalation triggers**: same problem ≥3 failures → Sonnet; architecture/security keyword → Opus/advisor()
- **Audit trail**: audit-log.sh logs all Bash commands; pre-commit-review.sh reviews staged changes
- **Commit hygiene**: `git add <specific files>` only; commit message + session URL required (hook enforced)

## Observability and Evaluation

- **Primary metric**: harness-audit 14-component CAR scorecard (✅/⚠️/❌); current score **13.0/14 = 92.9%** (🟢 Production-ready, 2026-05-25); auto-load budget **3,298 tok** ✅ (4 files + CLAUDE.md；CAR hard cap 4,500，餘裕 1,202 tok 26.7%)
- **Benchmark**: healthcheck.sh 12 validation sections (PASS/WARN/FAIL)
- **Scoring gate**: SCORING.md 5-dim gate (A×0.3+B×0.2+C×0.2+D×0.15+E×0.15 > 6.0) for Ratchet promotion
- **Failure categories**: context rot (compact trigger), false positive Ratchet (source-verify gate), prod safety violation (hook block), non-determinism (Known Gotchas log)
- **Eval protocol**: harness-audit skill（5 階段 Diagnose→Ratchet-Log）; Source-Verify Gate required before Ratchet promotion; RATCHET.md tracks known failures

---

*Source: CLAUDE.md + AGENTS.md + .claude/settings.json + .claude/rules/ | Full CAR framework: P01 §2*
