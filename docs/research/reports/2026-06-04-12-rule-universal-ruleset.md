---
title: "The 12-Rule Canon for AI Coding Agents — Universal Edition"
date: 2026-06-04
status: complete
derived_from: ["Karpathy R1–R4 (CLAUDE.md) + Mnilax R5–R12 (thread)", ".claude/refs/karpathy-mnilax-best-solution.md (AB4.0, workspace-coupled baseline)"]
evidence: "2026-06-04-karpathy-mnilax-12-rule-universalization-research.md (8 papers, grep-verified)"
generalization: stack-agnostic + harness-agnostic
license_note: Adapt freely. Tune the numbers (R6 budgets) to your model and cost structure.
type: ruleset
---

# The 12-Rule Canon for AI Coding Agents — Universal Edition

> **What this is.** A portable discipline ruleset for *any* AI coding agent (Claude Code, Cursor, Copilot, Aider, Devin, a custom agent, or a human reviewing AI output) on *any* stack. Derived from Karpathy's R1–R4 + Mnilax's R5–R12, grounded in agent-failure research, stripped of any single tool's mechanisms.
>
> **How to read each rule.** Every rule is one triad:
> **① Failure it prevents -> ② Mechanism any team can adopt -> ③ Mechanically-checkable verification.**
> The third column is the point: a rule you cannot mechanically check is a vibe, not a rule.
>
> **Why exactly 12.** The original author observed compliance dropping from 76% to 52% past ~14 rules (self-reported). Keep your active ruleset ≤ 12. Adding a 13th means merging or cutting one.
>
> **Evidence labels.** Inline tags mean:
> - **(Parallel: …)** = an *analogous* failure mode observed in agent research. It does **not** prove the rule — it shows the same root-cause failure appearing in autonomous/multi-agent architectures. The rule prevents the assistant-discipline version of that failure.
> - **(Empirical: …)** = a *directly measured* result from a cited paper (grep-verified against primary text).
> - **R1–R3 grounding is thinner than R4–R12**: the papers study agent *architectures*, not single-assistant diff hygiene — so R2/R3 lean on analogy, R4–R12 on direct measurement.

---

## R1 — Think Before Coding

| | |
|---|---|
| **① Prevents** | Acting on a silent assumption; hiding confusion instead of surfacing it. *(Parallel: MAST "Fail to ask for clarification" — acting on unclear/incomplete data -> incorrect actions. arXiv:2503.13657)* |
| **② Mechanism** | Before writing code, state in ≤2 sentences: your interpretation (not a restatement of the request) + key assumptions. If multiple interpretations exist, **present them and let the human choose** — don't pick silently. Calibrate ask-rate: trivial equivalent choices (naming, formatting, default values) -> decide and note it in one line; **scope changes or irreversible actions -> always ask.** |
| **③ Verify** | Before the first edit, the transcript contains an explicit interpretation + assumptions line. For any destructive keyword (`DELETE` / `DROP` / `TRUNCATE` / prod deploy / key rotation / `rm -rf` / `--force` push / infra destroy), a confirmation summary was shown and acknowledged **even if the human said "just do it."** |

**Irreversible-action exception:** the destructive keywords above always require a summary + wait, regardless of "just do it." This is the one place "Think Before" is non-negotiable.

---

## R2 — Simplicity First

| | |
|---|---|
| **① Prevents** | Over-engineering: speculative features, single-use abstractions, error handling for impossible cases. *(Parallel: MAST — failures "stem from system design issues, not just LLM limitations"; adding complexity doesn't fix structural problems. arXiv:2503.13657)* |
| **② Mechanism** | Write the minimum code that solves the stated problem. No feature beyond what was asked. **Rule of 3:** extract a helper only at the 3rd call site. Self-test: "Would a senior engineer call this overcomplicated?" If yes, rewrite smaller. If you wrote 200 lines and it could be 50, rewrite it. |
| **③ Verify** | Diff contains no abstraction with <3 call sites, no config/flag that wasn't requested, no error branch for an input that cannot occur. Line count is justifiable to a senior reviewer. |

**Security exception (always a shared function, exempt from Rule-of-3):** crypto primitives, key operations, input validation, authentication. Never inline nonce/IV generation per-algorithm (-> IV-reuse vulnerability).

---

## R3 — Surgical Changes

| | |
|---|---|
| **① Prevents** | Tangential refactoring, reformatting, renaming — noise that buries the real change. Wide-blast-radius edits also raise cascade risk. *(Parallel (thin — architecture-level, not diff-hygiene): SWE-agent "Cascading Failed Edits" = 23.4% of failures, the largest category; this grounds the cascade-risk half of R3 and overlaps R8. Scope-discipline itself is not directly measured in these papers. arXiv:2405.15793)* |
| **② Mechanism** | Touch only what the task requires. Don't "improve" adjacent code/comments/formatting. Match existing style even if you'd do it differently. Clean up only **your own** orphans (imports/vars your change made unused) — leave pre-existing dead code (mention it, don't delete). |
| **③ Verify** | **Every changed line traces directly to the request.** Soft bounds: bug fix ≤ 50 lines, feature ≤ 300, single file ≤ 500. Unrelated bug found mid-task -> logged & reported, **not** auto-fixed (keeps commits atomic). |

**P0 security exception (fix on sight):** hardcoded credentials, SQLi, path traversal, auth bypass. Isolate the fix on its own branch — don't bury a security patch inside a feature commit. Credential scans must exclude test/fixture/example/docs dirs to avoid drowning real leaks in fake data.

---

## R4 — Goal-Driven Execution

| | |
|---|---|
| **① Prevents** | Walking steps toward a weak goal ("make it work") and stalling on the next step instead of converging on a verifiable outcome. *(Parallel: SWE-agent "fast success, slow failure" — resolved tasks median 12 steps/$1.21; unresolved 21 steps/$2.52, "increasing budget unlikely to improve.")* |
| **② Mechanism** | Transform the task into an observable success condition **before** starting, then loop to it: "add validation" -> "write tests for invalid inputs, then make them pass"; "fix the bug" -> "write a test that reproduces it, then make it pass." For multi-step work, state a brief plan with a per-step check. |
| **③ Verify** | Success condition is **mechanically checkable** (a command exits 0 / a test passes / a specific output appears) — never "looks correct." The verification command actually ran and its output is shown. *(Empirical payoff: Reflexion loop-until-`outcome.success` -> 91% pass@1 vs one-shot GPT-4 80% on HumanEval. arXiv:2303.11366. Confucius makes verification a mandatory pipeline stage: "if tests fail, the agent enters a debugging sub-loop." arXiv:2512.10398)* |

---

## R5 — Use the Model for Judgment, Code for Decisions

| | |
|---|---|
| **① Prevents** | Using the LLM where deterministic code belongs — routing, retries, status-code handling, math, transforms. Non-deterministic answers to deterministic questions. |
| **② Mechanism** | **LLM (latent/judgment):** classification, drafting, summarization, extraction from unstructured text. **Code (deterministic):** routing, retries, HTTP status handling, arithmetic, format transforms. If a status code already answers the question, plain code answers the question. |
| **③ Verify** | No control-flow decision (route/retry/branch on a known signal) is delegated to a model call. *(Empirical: Dynamic Cheatsheet — once the model judged "use a Python solver" and let deterministic code compute, Game of 24 went 10%->99%; equation-balancing ~50%->98–100% while LLM-only "baselines stagnated around 50%." arXiv:2504.07952)* |

---

## R6 — Token Budgets Are Not Advisory

| | |
|---|---|
| **① Prevents** | Loops running until context is exhausted; quality degrading silently as context "collapses." *(Parallel: ACE "context collapse" — "iterative rewriting erodes details… sharp performance declines"; DC "context ballooning." arXiv:2510.04618 / 2504.07952)* |
| **② Mechanism** | Set an explicit **per-task** and **per-session** token/cost budget for your model and price point. When approaching it, **summarize and start fresh** rather than pushing through. **Surfacing the breach > silently overrunning.** When you do compact, use incremental/delta summaries that preserve goal + key results — don't full-rewrite (that *causes* collapse). |
| **③ Verify** | A budget number exists and is checked. On breach, the agent compacts or restarts and **says so** — it doesn't quietly continue. *(Empirical: Confucius — disabling semantic context management cost −6.6pp Resolve@1; persistent notes saved ~11k tokens & 3 turns/task. arXiv:2512.10398)* |

> **Universalization note:** budget *numbers* are model- and cost-specific — set your own. The *principle* (explicit budgets + surface the breach) is universal. Don't ship someone else's specific token figures as if they were constants.

---

## R7 — Surface Conflicts, Don't Average Them

| | |
|---|---|
| **① Prevents** | Blending two contradictory codebase patterns into "average" code that satisfies neither and is the worst of both. *(Parallel: MAST "Inter-Agent Misalignment" class — goal/instruction divergence resolved silently; coordinators need "structured handoff + confirmation, not self-interpretation." arXiv:2503.13657)* |
| **② Mechanism** | When two existing patterns contradict, **pick one** — by priority: ADR/CONTRIBUTING > most recent commits > test coverage. Explain why, and flag the other for cleanup. Never blend. |
| **③ Verify** | The chosen pattern is consistent (not a hybrid), and a `TODO(conflict): chose A over B; reason …; remove B before <milestone>` marker exists. |

---

## R8 — Read Before You Write

| | |
|---|---|
| **① Prevents** | Adding code without understanding the interface contract or upstream impact. "Looks orthogonal to me" is the most dangerous phrase in any codebase. |
| **② Mechanism** | Before editing a file, read: its exports (interface contract) + the immediate caller (upstream impact) + obvious shared utilities (lateral deps). If you don't understand *why* existing code is structured a certain way, ask before adding to it. |
| **③ Verify** | The transcript shows the relevant exports/callers were read **before** the edit. *(Empirical: SWE-agent's successful trajectories open with find/read/reproduce (turns 1–4) then zoom-in dir->file->line; skipping it is costly — recovery rate collapses 90.5%->57.2% after the first failed edit. arXiv:2405.15793. Confucius enforces a Retrieval+Localization phase before Implementation. arXiv:2512.10398)* |

---

## R9 — Tests Verify Intent, Not Just Behavior

| | |
|---|---|
| **① Prevents** | Tests that pass any implementation regardless of correctness. `expect(getUserName()).toBe('John')` is worthless if the function returns a hardcoded ID. |
| **② Mechanism** | Every test encodes **why** the behavior matters, not just **what** it does. Mock external boundaries, not the business core. The test: if you can't write a test that would **fail when the business logic changes**, the function is wrong. |
| **③ Verify** | Flip a line of business logic -> at least one test fails. *(Empirical: Reflexion explicitly distinguishes "explicit test cases" from "LLM self-evaluation" as evaluators — the 91% result used the former. arXiv:2303.11366. SWE-bench-Pro required human-vetted test suites as ground truth — test *quality*, not presence, is what verifies intent. arXiv:2509.16941. SWE-agent's reproduction-first `(create, edit, python)` = write the failing case before the fix. arXiv:2405.15793)* |

---

## R10 — Checkpoint After Every Significant Step

| | |
|---|---|
| **① Prevents** | Continuing from a state you can't describe; repeating already-done work. *(Parallel: MAST "Loss of conversation history" (context truncation -> revert to stale state) + "Step repetition." arXiv:2503.13657)* |
| **② Mechanism** | After each step in a multi-step task, emit one line: **what was done / what's verified / what's left.** If you lose track, **stop and restate** — don't continue from an undescribable state. |
| **③ Verify** | A checkpoint line exists per major step and accurately reflects current state. *(Empirical: Confucius's "Architect" checkpoint preserves task spec + decisions + file paths + recent N messages; persistent notes save ~11k tokens, 3 turns/task and +1.4pp Resolve@1 by not re-discovering or repeating failed approaches. arXiv:2512.10398)* |

---

## R11 — Match the Codebase's Conventions, Even If You Disagree

| | |
|---|---|
| **① Prevents** | Silently forking convention (snake_case->camelCase, classes->hooks) on taste. Re-deriving what already exists. *(Parallel: DC — "repeatedly re-discovering… the same solutions and mistakes" is the cost of ignoring accumulated conventions; reusing the existing solution took Game of 24 10%->99%. arXiv:2504.07952)* |
| **② Mechanism** | Inside the codebase, **conformance > taste.** snake_case if it's snake_case; class-based if it's class-based. Disagreement is a separate conversation. Treat existing conventions as an **evolving playbook** — the authoritative starting point, not a blank slate. *(ACE "evolving playbooks." arXiv:2510.04618)* |
| **③ Verify** | New code matches surrounding style/naming/structure. If a convention is genuinely harmful (e.g., SQL string concatenation), it's surfaced as a flagged issue — **not silently forked**. |

---

## R12 — Fail Loud

| | |
|---|---|
| **① Prevents** | Silent failure masquerading as success. "Migration completed" when 30 records were skipped. "Tests pass" when some were skipped. "Feature works" when the asked-for edge case was never checked. *(Parallel: MAST's entire "Task Verification" class — the hardest to auto-fix — incl. "Premature termination," "No/incomplete verification" ("allowing errors to propagate undetected"), plus "Information withholding." arXiv:2503.13657)* |
| **② Mechanism** | If you can't be sure something worked, **say so explicitly.** Default to surfacing uncertainty, not hiding it. Skipped steps and partial failures must be stated — tone can soften, **information cannot be omitted.** Report the count of what was skipped/failed, with a pointer to the log. |
| **③ Verify** | Before declaring done: the verification command ran and **its output is shown** (not a verbal "tests pass"). Any skip/partial-failure is named with a number. Truncated reads/searches are flagged, not silently assumed empty. |

---

## Appendix A — Compounding Engineering (the meta-rule)

> Not one of the 12. A wrapper that keeps the 12 alive.

**Every mistake is an opportunity to update the ruleset so it never recurs.**

- **Mechanism:** after a mistake, ask "will this recur?" -> if yes, add a guard (a hook/lint if mechanizable; otherwise a written rule). Record only **verified** constraints — never speculative "expected behavior" (that pollutes the ruleset).
- **Verify:** the same failure mode does not recur in the next session.
- *Empirical: ReasoningBank — agents that "fail to learn from accumulated history… discard insights and repeat past errors"; distilling lessons from successes AND failures is a "new scaling dimension." arXiv:2509.25140. ACE's "Reflector" extracts "what worked, what failed, and why." arXiv:2510.04618. A survey of 100+ papers calls memory "indispensable for self-evolving capability." arXiv:2404.13501.*
- **Guard against the cliff:** when active rules exceed ~14, compliance drops (self-reported 76%->52%). Merge or cut before adding.

---

## Appendix B — How to adopt this in a non-Claude harness

| Concept here | Cursor / Copilot / Aider / custom agent |
|---|---|
| Surface interpretation before coding (R1) | Put R1 in your system prompt / `.cursorrules` / agent preamble |
| Independent reviewer pass (R4/R9/R12) | A second model (or human) reviews the full transcript before merge |
| Summarize & restart on budget breach (R6) | Your harness's context-compaction or a fresh thread; set token caps in the runner |
| Verification command (R4/R12) | Wire your test/lint/build command as a required gate (CI or pre-commit) |
| Checkpoint line (R10) | Have the agent write a running notes file; reload it next session |
| Update-on-mistake (Appendix A) | A `LESSONS.md` / `GOTCHAS.md` the agent reads at session start |

**The rules are the contract; the mechanisms are interchangeable.** Any harness that lets you (1) inject a system prompt, (2) run a verification command, and (3) persist notes across sessions can implement all 12.

---

## Appendix C — One-line cheat sheet

1. **Think** before coding — surface assumptions, ask on ambiguity.
2. **Simplest** code that works — no speculation.
3. **Surgical** edits — every line traces to the request.
4. **Goal-driven** — define a checkable success condition, loop to it.
5. **Judgment** to the model, **decisions** to code.
6. **Budgets** are hard — surface the breach, don't overrun.
7. **Surface** conflicts — pick one, never average.
8. **Read** before you write.
9. **Tests** verify intent — must fail when logic changes.
10. **Checkpoint** — describe state every step.
11. **Conform** to conventions — disagree elsewhere.
12. **Fail loud** — uncertainty surfaced, not hidden.
