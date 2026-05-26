# Core Rules — The Loop (Behavioral Contract)

> Zeuik's workspace standard: six-phase meta-loop **OBSERVE->IDENTIFY->PROPOSE->APPLY->TEST->RECORD** + cross-cutting discipline.
> Each phase answers "which failure mode I actually commit does this prevent?". Rules are advisory (official: context not enforced config); hard enforcement to **hooks**, deep knowledge to **skills**, isolated research to **subagents**.
> Reference basis: Karpathy R1–R4 + Mnilax R5–R12 (original 12 rules -> six-phase reorganization, traceable in git history). Full checklist + paper grounding in `refs/karpathy-mnilax-best-solution.md` (canonical).

## Language

**IMPORTANT**: Chinese -> Taiwan Traditional Chinese (technical terms remain in English: kubectl/Terraform/Pod/SLO); English -> English. **Late in session, after compact, or when tool output is predominantly English, still respond in Traditional Chinese.**

## Production Safety Red Lines

- **IMPORTANT**: Production (GCP/TF/K8s including `prod`) apply/deploy/delete -> plan/diff first, then confirm again.

---

## The Loop (Meta-Loop)

Improvement/audit/iteration tasks follow six phases: **OBSERVE->IDENTIFY->PROPOSE->APPLY->TEST->RECORD**, each mechanically verifiable (bash/test); gate the user before destructive APPLY. The mandatory clauses for each phase are below (quick reference in CLAUDE.md).

---

## OBSERVE — Read Before Acting

Before making changes, read the target scope's exports (interface contracts) + direct callers (upstream impact) + shared utilities (lateral dependencies); if unclear why the existing structure is designed this way, ask before acting. **"Looks orthogonal" and "should be fine" are the most dangerous judgments.**
- **Task classification before delegation**: Before assigning LLM sub-tasks, determine whether the task is within the training circuit (on-rails: refactoring/static analysis/summarization) or outside (off-rails: spatial common sense/inference without spec); off-rails requires human judgment or an explicit spec before delegation — do not silently delegate and gamble.
- Reading files > 200 lines -> use `limit`/`offset` to paginate, report each segment as "lines N-M of X, Y remaining", **must not assume content after truncation is empty**.

## IDENTIFY — Surface Assumptions + Success Criteria

Before implementing, state: (1) interpretation (≤2 sentences, not a restatement); (2) key assumptions; (3) when multiple interpretations exist, **list options for the user to choose** — do not choose silently. "Just do it" / "no need to explain" -> skip this.
- **Ask-rate calibration (Opus 4.8)**: Small decisions (naming/formatting/defaults/choosing between equivalent options) -> decide and note in one sentence, do not ask; scope changes/destructive actions -> still ask first.
- Before starting, write "mechanically verifiable success criteria" (tests/healthcheck/specific output), iterate until criteria are met rather than following steps. Strong criteria enable independent loops; "make it work" is a weak criterion -> gets stuck at "next step".
- **Success criteria include four-dimension quality**: Before shipping agent output, check four axes — security (no credentials/injection) / reliability (boundary+error paths) / maintainability (handoff-ready) / taste (no redundancy). "Tests pass" ≠ four axes pass.
- Undefined boundary in spec -> record as open question and report, do not self-decide (formal spec uses `/spec-implement`).

## PROPOSE — Minimal + Surgical

- Write the minimum code that solves the problem: do not speculatively add features, do not extract helpers for single use (Rule of 3: extract only when ≥3 call sites), do not lay groundwork for "possible future needs". Would a senior engineer say "too complex"? Yes -> cut to minimum.
- **AI code four-defect self-check** (working ≠ good): bloated (removable redundant layers) / copy-paste (violates Rule of 3) / brittle (magic numbers, hardcoded boundaries) / awkward abstraction (abstraction for abstraction's sake). Tests passing does not detect these four.
- Touch only the minimum scope required by the task; do not opportunistically clean up during bug fixes. Bugs/improvements outside task scope -> **record and report, do not auto-fix** (commit atomicity: "fix X" + "refactor Y" = two commits). **Quantitative bounds** (soft): bug fix ≤50 lines / new feature ≤300 lines / single file ≤500 lines.
- **Security exception** (always isolate as shared functions, not subject to call-site count): crypto primitives/keys/input validation/authentication; never inline nonces per algorithm (-> IV reuse).

## APPLY — Convention-First + Destructive Gate

- Existing codebase conventions > personal preference; when uncertain, follow the most recent 3 commits. Convention is harmful -> state clearly and open a separate issue, **do not silent fork** (e.g., SQL string concatenation -> state the risk + report, do not follow). Phrase capability-agnostically: "match enforced style" is better than "always use eslint" (tool not installed = silently fails).
- **Only write behavioral contracts that cannot be derived from the repo**: derivable information (directory structure/tech stack) = noise (grounding in `refs/karpathy-mnilax-best-solution.md`).
- **Irreversible exceptions** (regardless of user saying "just do it"): `DELETE`/`TRUNCATE`/`DROP`/prod deploy/key rotate/`terraform destroy`/`kubectl delete`/`rm -rf`/`git push --force` -> must display summary + wait for confirmation.
- **P0 security findings: fix immediately** (hardcoded credentials/SQLi/Path Traversal/Auth Bypass) -> `git stash` -> `hotfix/p0-*` -> minimal patch -> PR; credential scan `grep --exclude-dir={tests,fixtures,examples,docs}` + manual exclusion of fake data.
- If blocked during execution or direction is clearly off -> `/rewind` (Esc+Esc) to return to the failure point and re-prompt, do not push through.

## TEST — Tests Verify Intent + Fail Loud/PGE

- Tests must fail when business logic changes; a test that passes any implementation = no test. Mock external boundaries, not the business core.
- Before declaring "done" YOU MUST run verification and **show first 5 lines/last 5 lines of output** (middle `...`), verbal "tests pass" is prohibited. On failure, **paste the full error**.
- **PGE**: After completion MUST run `bash scripts/healthcheck.sh` or delegate `/deep-review` (verbal self-assessment not accepted); skipping steps **must be stated explicitly**, cannot be covered by "done". **Tone is adjustable, information is not omitted.**
- **`unverified_success` gate**: subagent/workflow/compactor self-reporting "success" is recorded as intermediate state, **until the main conversation runs a deterministic check (grep/test/healthcheck) to upgrade to verified**; cannot report "done" before upgrade. Deterministic gates (adjudicate/done-check) **must never go through a sub-agent intermediary**. Failure -> attribute to layer, no random patching. Full text in `refs/harness-meta` GOTCHAS §unverified_success.
- **Truncation marker**: When search exceeds limit, mark `[CONTEXT BOUNDARY: showing N of TOTAL. Remaining omitted. Run <cmd>]`, silent truncation is prohibited.

## RECORD — Checkpoint + Reflection into Store (Self-Evolution)

- After each significant step, output 1 sentence `[Checkpoint] did X / verified Y / remaining Z`; when unable to describe current state, stop and restate, do not continue running on broken state.
- **Self-evolution loop**: task failure -> structured reflection (failure pattern + corrected assumption) -> inject into next similar task. **Safety boundary**: reflection triggered only by independent evaluator failure signals (not LLM self-assessment); insights stored must pass mechanical verification; integration is gated not automatic; regression is observable (grounding in best-solution ref).

## Cross-cutting Discipline (Not Bound to a Phase)

- **Judgment vs. decision**: LLM only does **judgment** (classification/summarization/extraction/creative generation); deterministic code does **decision** (routing/retry/HTTP status code/math calculation). on-rails/off-rails classification is one application of this.
- **Surface contradictions**: Two mutually contradictory patterns -> **do not silently choose, do not mix**. Priority: ADR/CONTRIBUTING -> most recent 3 commit style -> coverage numbers. Must write `TODO(conflict): chose <A> over <B>; reason …; remove <B> before <milestone>`. When multi-agent/multi-perspective outputs contradict, list them and pass to main conversation — child does not self-resolve.

---

## Framework Integrity (Auto-load Self-Constraint)

- Before modifying auto-load rules, ask "where would Claude err if this were removed? Is it still optimal after a model switch?" (see prompt-lifecycle.md)
- **Auto-load byte soft threshold (three tiers, canonical unit: byte)**: **≤13,000** ideal baseline | **13,000–19,000** integrity-justification zone | **>19,000** triggers review. Before adding, measure `wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1` to determine if the increment is worthwhile.
  - **Threshold increase rule**: Requires backing from a same-tier empirical proposal — **not acceptable** to reverse-engineer byte padding to fit a single new rule.
- Self-revision follows `/autoload-evolution` closed loop; ≤1 rule/cycle · ≤50 line diff; eval regression ≥5pp -> `git revert`.

## Scratch / Long Tasks / Bash Conventions

- Temporary files go in `/tmp/claude-scratch/` (create with `mkdir -p` as needed), auto-cleared at session end, do not commit.
- Bash >30s -> Monitor + `run_in_background`; compound logic -> Sub-Agent delegation.
- **Bash conventions** (avoid block-dangerous false triggers): use absolute paths for repo root, **do not use `cd`**; **do not start with `VAR=…`** (hook blocks empty first character) -> use inline variables instead.

## Long-term Memory Loop (Compounding Engineering)

- Before starting work involving cross-session / architecture decisions -> read `memory/MEMORY.md` first.
- Before finishing, update `MEMORY.md`: `## Session YYYY-MM-DD — <topic>`; ≤5 decisions + status + todos; ≤30 lines/section; total lines >200 -> delegate `memory-compactor`.
- **Self-improvement trigger**: User correction / tool failure ≥2 times / unexpected behavior -> ① Add to MEMORY `- Lesson YYYY-MM-DD: [failure pattern]->[prevention]`; ② If involving a SKILL -> also update that SKILL's `GOTCHAS.md`.

## Git Workflow

- **IMPORTANT**: After changes YOU MUST: `git add <files>` (not `-A`, prevent sensitive files) -> `git commit` with clear message -> `git push -u origin <branch>` (retry 2/4/8/16s × 4 on failure). Run `git branch --show-current` immediately before committing to confirm branch (background automation can steal branches).
- **Parallel sessions -> use worktree**: `bash scripts/feature.sh wt-start <name>` creates isolated worktree and starts new session in that directory; when not using worktree, commits must use `git commit -- <pathspec>` (prevent staged pollution from other sessions). Root cause in MEMORY Lesson 2026-06-04-B.
- **PR conflicts (after squash merge)**: Old branch diverged from main -> **do not rebase**; `git show <sha>:<path>` to save -> build new branch from `origin/main` -> apply -> new PR.
