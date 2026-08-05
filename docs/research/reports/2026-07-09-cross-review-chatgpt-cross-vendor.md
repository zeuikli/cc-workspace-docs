---
title: "ChatGPT-5.5 Cross-Vendor Independent Review of Fusion Architecture"
date: 2026-07-09
status: done
method: "Independent fresh-context review from a non-Anthropic, non-Cognition reasoning baseline. Mechanical checks executed before prose findings."
parent-artifacts: [research/reports/2026-07-09-fusion-architecture-design-plan.md, research/reports/2026-07-09-fusion-glm-architecture-validation.md, research/reports/2026-07-09-fusion-glm-factory-phase2-config.md, research/reports/2026-07-09-fusion-kimi-token-simulation.md, research/reports/2026-07-09-fusion-kimi-agents-md-protocol-draft.md]
reviewer: "ChatGPT-5.5 (frontier tier, cross-vendor, fresh-context)"
scope: Full Fusion architecture design + 4 sub-reports + source material
type: cross-vendor-adversarial-review
---

# ChatGPT-5.5 Cross-Vendor Independent Review of Fusion Architecture

## Reviewer Context

- **Model**: ChatGPT-5.5 (frontier tier, cross-vendor)
- **Mode**: Independent, fresh context — no shared ecosystem bias with Claude Code / Anthropic / Cognition
- **Scope**: Full Fusion architecture design plan + 4 sub-reports + AGENTS.md + delegation-protocol.md
- **Stance**: Adversarial-by-default (per workspace `subagent-strategy.md` "對抗立場預設"); verdict ≠ evidence
- **What I am NOT**: I am not reviewing to validate the design. I am reviewing to find what same-ecosystem reviewers (Claude, GLM, Kimi — all of whom share the Anthropic-adjacent or open-source-Fusion framing) would systematically miss.

---

## A. Vendor Neutrality Audit

### A1. The "Claude Code path vs Factory path" framing is a false dichotomy

The design plan §2.3-§2.4 presents exactly two implementation paths: Claude Code (Phase 1-2) and Factory Droid (Phase 1-3). A genuinely vendor-neutral design would acknowledge at least three additional paths that this framing excludes:

1. **Direct API path** (no harness at all): A pure-API user could implement the Sidekick pattern with two parallel API clients maintaining independent cached prefixes — no Claude Code, no Factory Droid. The design's §2.5 "AGENTS.md Fusion Protocol" claims to be "harness-neutral" but then immediately grounds all concrete steps in either Claude Code sub-agent spawn or Factory Session API PATCH. A pure-API user reading this design gets an abstract protocol and zero executable steps.
2. **Alternative harness path** (Cursor, Codex, Aider, Continue): The AGENTS.md §1 "Portability note (MHF)" itself admits "switching to Codex/Cursor = rebuild enforcement layer." The Fusion design silently inherits this limitation — its "harness-neutral" claim is only as portable as the two harnesses it explicitly targets.
3. **Orchestration-layer path** (LangGraph, DSPy, custom router): The "Fusion Router (L0)" in §2.2 is described as a "lightweight classifier" but its implementation is left entirely unspecified. A vendor-neutral design would at minimum name the abstraction boundary (is the router a model call? a rule engine? a hook?).

**Verdict on neutrality**: The design is "bi-harness-neutral" (Claude Code + Factory), not vendor-neutral. It is Anthropic-flavored throughout — every concrete pricing figure, every cache threshold, every model ID comes from `model-profiles.md` which is 100% Anthropic (the file itself notes "4 檔位全 Anthropic = 監管單點失效"). A reviewer from OpenAI, Mistral, or a self-hosted shop would not recognize this as their architecture.

### A2. The Factory Session API PATCH capability is partially verified, not fully

The GLM Phase 2 config report (D6 verification) is the strongest part of the submission — it actually catches that `providerLock` is **not** a settable CLI switch and that `providerLockTimestamp`'s semantics are undocumented. This is exactly the kind of assumption-challenging a cross-vendor reviewer expects, and GLM-5.2 performed it well.

However, two API-behavior assumptions remain unchallenged that a non-Anthropic vendor would press harder on:

1. **"compaction 本就觸發 cache 失效,因此順便換模型成為零額外 cache 懲罰"** (design §1.1, §2.2 L3). This is the **load-bearing assumption** of the entire Fusion architecture — the claim that model switching at compaction time is "free." But this is asserted as a direct port of Cognition's Devin Fusion claim. Factory's `compactionModel` API field lets you *set* a different compaction model; it does **not** guarantee that switching the *main session model* mid-session (via PATCH `model`) preserves cache across the compaction boundary. The design conflates "compaction invalidates cache anyway" (true) with "switching model at compaction is zero-penalty" (only true if the new model's cache prefix is compatible with the surviving post-compaction context). A non-Anthropic vendor would ask: *does Factory's post-compaction context survive a model switch intact, or does the new model re-process the compacted summary from scratch?* The design does not answer this.

2. **`compactionThresholdCheckEnabled: true` as the "detect compaction trigger" precondition** (Phase 3). The design assumes setting this flag gives you a reliable signal to PATCH the model. But the flag's name suggests it *checks* the threshold, not that it *emits an event* you can hook. If it's a check (poll), you need a polling loop; if it's an event, you need a webhook. The Phase 3 pseudo-code ("1. 偵測 compaction 觸發 → 2. PATCH session") skips the detection mechanism entirely.

### A3. The "Claude Code path" sub-agent spawn ≠ Devin Fusion sidekick

A subtle but critical conflation: Devin Fusion's sidekick maintains **persistent cached context** across many task delegations. The design's Claude Code Phase 1 uses **one-shot sub-agent spawn** (each spawn = fresh context). The GLM validation report correctly flags this (optimization item 4: ⚠️ needs modification) and the design plan §2.3 admits "不是真正的 cache 持久化." So the architecture's own documentation acknowledges that **the Claude Code path does not actually implement Fusion** — it implements a degraded approximation. The -35.2% savings figure is computed assuming Phase 2/Factory persistent sidekick (token simulation §5 limitation 4), not the Phase 1 reality. This is a bait-and-switch risk: the headline number describes Phase 2+, but the "zero-code-change" claim describes Phase 1.

---

## B. Open-Source Model Reliability

### B1. GLM-5.2 and Kimi K2.7 as sidekicks — reliability assumptions are untested

The design proposes GLM-5.2 (ceiling-tier open-source) and Kimi K2.7 (quality-tier open-source) as sidekick candidates (§4.1). The supporting evidence is benchmark-adjacent: GLM-5.2 "SWE-bench Pro 62.1% 接近 Opus" and Kimi "1000 tok/s + code 特化." But:

1. **No workspace-internal eval exists for either model as a sidekick.** The `model-profiles.md` §1 explicitly labels non-Claude models as "未知=當最高處理" (unknown = treat as highest tier). The design proposes routing *mechanical* tasks to these models, but "mechanical" tasks (grep, batch edit, test execution) are exactly where a subtly-wrong model does the most silent damage — a wrong grep pattern misses a security-relevant file, and nobody notices until production.
2. **The design's own §3.3 mechanism 5 ("跨模型互查: GPT-5.5 複查 Fable 5 仍能抓到遺漏")** is cited as evidence that cross-model review catches errors. But this is a *review* scenario (verdict on completed work), not a *execution* scenario (sidekick producing the work). The evidence does not transfer. A sidekick that produces subtly wrong mechanical output is not the same as a reviewer that misses a subtle error in someone else's work.

### B2. "eval-hack risk" is named but has no concrete mitigation

Design §6 risk 4 names "開源模型 eval-hack 風險未知" and §3.3 mechanism 3 says "檔位越高驗證越嚴." But:

- **No definition of "eval-hack" in this context.** Does it mean the model has been trained on the benchmark (contamination)? Does it mean the model produces output that *looks* correct to a weak verifier but isn't? The design uses the term as if it's self-evident.
- **No concrete detection mechanism.** "檔位越高驗證越嚴" is a *policy*, not a *mechanism*. What is the mechanical check that distinguishes "sidekick output is correct" from "sidekick output passes a weak gate"? The delegation-protocol.md §6 says "cost 產出 → parent 逐項覆核" — but "逐項覆核" (item-by-item review) by the main agent is itself a cost (see §D2 below) and is only as good as the main agent's attention budget.
- **The token simulation's quality column says "維持/提升" for tasks 3 and 5** (where sidekick does mechanical work). This is an assertion, not a measured result. No task in the simulation has been actually run with a GLM/Kimi sidekick and verified.

### B3. "Sidekick failure → immediate upgrade, no retry" is insufficient for partial failures

Delegation-protocol.md §6 and the design's Layer 4 say "Sidekick 失敗 1 次即升級（cost → quality）,不重試." This handles **crash failures** (syntax error, tool exception, empty output) but is silent on **partial failures**:

- **Correct syntax, wrong logic**: A sidekick produces a grep that runs successfully but uses a pattern that misses 3 of 10 relevant files. No exception is thrown. The "failure" signal never fires. The main agent's "機械重驗" must independently re-run the grep with a *different* pattern to detect this — but the design does not specify that the verification uses an *orthogonal* method, just that it "機械重驗."
- **Correct output, wrong scope**: A sidekick edits the right function but in the wrong file (e.g., a similarly-named file in a different module). The diff looks valid. The main agent's review must know which file was *intended* — but if the main agent delegated because it didn't want to read the files, it may not catch the scope error.
- **Plausible hallucination**: An open-source sidekick summarizing a research paper could hallucinate a citation that looks real. The design's §3.3 "Source-Verify gate" is mentioned for task 3 but not mechanically specified — it's a named gate, not a defined check.

The "no retry" rule optimizes for the failure mode where retrying wastes tokens. It does not address the failure mode where *there is no failure signal at all.* For open-source sidekicks with unknown reliability profiles, the partial-failure gap is the dominant risk.

---

## C. Devin Fusion Source Dependency

### C1. Single-source dependency on Cognition's blog — confirmed

The entire architecture derives from one Cognition blog post (2026-06-29). Mechanical verification:

- The scored article (`research/ai-articles/scored/2026-07-02-cognition-devin-fusion-sidekick-routing.md`) itself rates evidence quality **6/10** with the note "廠商自報 benchmark，非第三方驗證" (vendor self-reported, not third-party verified).
- WebSearch for independent verification returns **only Cognition's own channels** (cognition.com, @cognition on X, Jeff Wang's post, Reddit reposts of the blog, digg.com summary, codenewsletter.ai summary). **Zero independent third-party reproductions** of the 35% / 41% / 88% figures exist as of 2026-07-09.
- The zenml.io LLMops database entry is a *description* of Cognition's approach, not an independent benchmark.

**Implication**: The -35.2% headline is a number derived from a design *inspired by* a vendor's *self-reported* number, simulated on a *different* workspace's *estimated* task distribution. It is three levels of inference removed from any independently measured result. The design plan §6 risk 2 acknowledges "43% 為廠商自報" for Factory Router but does **not** apply the same caveat to the Devin Fusion 35-41% figures that anchor the entire architecture's value proposition.

### C2. The 88% "fully automated merged PRs" figure is Devin-specific, not reproducible

The 88% figure measures *Devin's* merged PRs under *Devin's* Fusion routing on *Devin's* task distribution. The token simulation §3.2 shows this workspace's estimated task distribution is: 40% single-file-small-change (0% savings), 25% cross-module refactor (-36% cost increase), 20% deep research (+37%), 5% security review (-18%), 10% large migration (+53%). The cost-weighted average of **-35.2%** is **entirely driven by the 10% large-migration task type** (which contributes -29.7% of the -35.2% total). Remove large migrations from the workload, and Fusion is a net **cost increase** (+2.8% frequency-weighted, per the simulation's own §3.2).

**This is the single most important finding a cross-vendor reviewer can surface**: The -35.2% savings is not a property of the Fusion architecture. It is a property of a workload that happens to contain a high proportion of mechanically-amenable large migrations. A workspace without large migrations (most SRE/ops workspaces, most product codebases) would see Fusion *increase* costs. The design presents -35.2% as if it generalizes; it does not.

### C3. The FrontierCode 57.6 vs 57.0 quality claim is within noise

The design cites "FrontierCode 分數維持 frontier-level（57.6 vs 純 Fable 5 的 57.0）" as evidence that quality is maintained. A 0.6-point difference on a benchmark with unknown variance is **not evidence of maintained quality** — it is consistent with noise. A cross-vendor reviewer would require either (a) the benchmark's reported variance / confidence interval, or (b) multiple runs. The design provides neither. The claim "維持 frontier-level" is reasonable but the specific 57.6-vs-57.0 framing overstates the precision of the evidence.

---

## D. Cost Model Reality Check

### D1. The -35.2% math is mechanically correct but built on fragile assumptions

**Mechanical verification of the cost arithmetic** (executed via Python):

| Task | Reported existing | Calculated existing | Reported fusion | Calculated fusion | Reported savings | Calculated savings |
|------|------------------|--------------------|-----------------|-------------------|-----------------|-------------------|
| 3 (deep research) | $0.4613 | $0.4613 ✅ | $0.2925 | $0.2925 ✅ | 37% | 36.6% (rounds to 37%) ✅ |
| 5 (large migration) | $1.536 | $1.5360 ✅ | $0.729 | $0.7290 ✅ | 53% | 52.5% (rounds to 53%) ✅ |

The arithmetic is internally consistent. The pricing baseline (Haiku $1/$5, Sonnet $3/$15, Opus $5/$25, Fable $10/$50) matches `model-profiles.md` §0/§2.3. The 1.35x ceiling tokenizer factor is documented in §2.3. **The math checks out.** The problem is not the math; it is the inputs:

1. **Token estimates are "量級近似" (order-of-magnitude approximations)** — the simulation's own §5 limitation 1 admits this. No `count_tokens` was run. CJK inflation (1.3-2.3x per §2.5) is not applied despite the workspace operating in 繁體中文. This means the input token estimates are likely **understated by 30-130%** for this workspace's actual language mix, which would shift the cost-weighted savings figure.
2. **Task frequency weights are "粗估" (rough estimates)** — §3.2 and §5 limitation 3 admit the 40/25/20/5/10 weights are subjective. The -35.2% figure is acutely sensitive to the large-migration weight: at 10% weight it's -35.2%; at 5% weight it would be ~-17%; at 0% it's +2.8%. The design does not run `evolution/cost-log.jsonl` to get real weights, despite the file existing.
3. **The cost-weighted vs frequency-weighted gap is buried**: §3.4 shows frequency-weighted = +2.8% (cost *increase*) vs cost-weighted = -35.2% (savings). The headline uses cost-weighted. A vendor-neutral reviewer would headline **both** numbers and explain that the choice of weighting is a judgment call, not a settled fact.

### D2. The cost of verification is not included in the savings figure

The design says "sidekick output must be mechanically re-verified by main agent" (§3.3 mechanism 1, delegation-protocol.md §6). This verification has a cost:

- delegation-protocol.md §6: "cost 產出 → parent 逐項覆核" (item-by-item review).
- For task 5 (large migration, 16 PRs), the main agent (ceiling, $5/$25) must review 16 PRs of sidekick (cost) output. The simulation's Fusion cost for task 5 ($0.729) **already includes** main agent review tokens (main_out 3,000 for "編排決策"), but this is characterized as orchestration, not as the full item-by-item verification of 16 PRs of mechanical edits. If the main agent must read 16 PRs × ~50 lines × 8 tokens/line = 6,400 input tokens of diffs *at ceiling pricing* to verify them, that's 6,400 × 1.35 × $5/1M = $0.043 — small for task 5 but proportionally large for the smaller tasks where it's omitted.
- For task 3 (deep research), the main agent must "機械重驗引用來源" (mechanically re-verify citation sources). Re-verifying 5 WebSearch citations means 5 additional searches + 5 reads, which is not in the Fusion cost column. This is an **omitted verification cost**.

**Net effect**: The -35.2% is an *upper bound* on savings, not a net figure. A more honest accounting would subtract verification overhead, which would compress the savings on the high-saving tasks (3, 5) and deepen the cost increase on the negative-saving tasks (2, 4).

### D3. The +36% cost for cross-module refactor is a real architectural overhead, not a tradeoff

Task 2 (cross-module refactor, 6-9 files) shows Fusion costs **+36%** more than the existing architecture. The simulation attributes this to "ceiling 升級 + sidekick overhead." A cross-vendor reading: **Fusion adds overhead for exactly the task type that is most representative of day-to-day engineering work** (cross-module interface changes). The design frames this as "品質換成本" (quality for cost), but:

- The quality benefit ("ceiling 規劃 + §6 機械重驗") is asserted, not measured (see §B2).
- The existing architecture already routes 6-9 file tasks to quality tier (Sonnet 5), which the workspace's own model-profiles.md §2.3 notes is the "標準工作馬" (standard workhorse) — i.e., already a reasonable quality level.
- Upgrading the main agent to ceiling (Opus 4.8, $5/$25, with 1.35x tokenizer penalty) for a task that Sonnet 5 handles well is **over-engineering the planning layer**. The design's §3.2 Layer 1 says "標準任務 → quality 檔," but the Fusion architecture violates its own routing rule by defaulting the main agent to ceiling for all non-T0 tasks.

**This is an architectural self-contradiction**: the Fusion design's main-agent-is-always-ceiling default conflicts with the workspace's existing "依位置數路由" (route by file count) principle, which deliberately uses quality tier for 2-9 file tasks. Fusion doesn't preserve the existing routing intelligence; it replaces it with a cruder "main = ceiling, sidekick = cost" binary.

### D4. Router overhead and orchestration tax are not modeled

The "Fusion Router (L0)" classifier is described but its cost is never included in any simulation. If the router is a model call (even a cheap one), it runs on every task. If it's a rule engine, it has maintenance cost. The -35.2% assumes the router is free. Additionally, the simulation §5 limitation 5 admits "未計 session overhead" (session init / auto-load / hook execution / handoff parsing), noting "實際節省會被 overhead 侵蝕, 尤其任務 1." This overhead is documented to be **76.2k tokens for cost tier, 73.9k for quality** (cited as "O9") — which is larger than the entire input token budget for tasks 1 and 2. For task 1 (single-file change), the overhead alone dwarfs the task cost, making the 0% savings figure misleading (it should be negative when overhead is included).

---

## E. Missing Perspectives

### E1. Pure-API user perspective: design is not relevant to them

A pure-API user (no Claude Code, no Factory) gets from this design:
- An abstract 4-layer architecture diagram (§2.2) they could in principle implement.
- An AGENTS.md Protocol draft (1077 bytes) that is too abstract to guide implementation (see §F2).
- Zero concrete API patterns for implementing the Sidekick pattern with two parallel cached clients.

The design is relevant to them only as *inspiration*. For execution, they would need to design their own router, their own cache-prefix management, their own compaction trigger detection — none of which the design specifies at the API level. **The design's "harness-neutral" claim does not survive contact with a pure-API reader.**

### E2. Multi-tenant scenarios: design is single-user/single-session oriented

Every simulation assumes a single user, single session, single main agent. There is no discussion of:
- **Concurrent sessions sharing a sidekick pool** (could a sidekick serve multiple main agents? the design implies 1:1).
- **Tenant isolation** (if multiple users' sidekicks run on shared infrastructure, does the cached context bleed?).
- **Cost attribution** (Factory's `childInclusiveTokenUsageBySessionId` is per-session, but a multi-tenant deployment would need per-tenant aggregation — not discussed).
- **Rate limits** (open-source sidekicks via BYOK may have provider rate limits that constrain parallelism; the 16-PR parallel migration in task 5 assumes no rate-limit binding).

For a workspace owner this is fine (single-user). For anyone considering this as a *general* architecture, it's a gap.

### E3. Latency: entirely unaddressed

The design optimizes for cost and claims quality is maintained. It says nothing about latency. But:

- **Model switching has latency**: a PATCH to switch models mid-session, plus the new model's cold-start (cache miss on the new model's prefix), adds wall-clock time. The design claims "零 cache 懲罰" for compaction-time switches, but cache *miss* ≠ zero latency — the new model still has to process the compacted context.
- **Sidekick round-trip latency**: spawning a sub-agent (Claude Code) or PATCHing a session (Factory) + sidekick execution + report-back adds a round-trip the existing architecture (main agent does it inline) does not have. For task 1 (single-file change), the sidekick round-trip latency would likely exceed the inline execution time, which is why the design correctly excludes T0 tasks from sidekick routing — but this latency reasoning is never stated, only the cost reasoning.
- **Parallel sidekick latency for task 5**: 16 PRs in parallel assumes the sidekick infrastructure can actually run 16 concurrent executions. If it can't (rate limits, concurrency caps), the 53% savings figure is unreachable.

A cross-vendor reviewer from a latency-sensitive domain (real-time, on-call SRE) would find this design unusable without a latency model.

### E4. Observability: no debugging path for wrong routing decisions

The design specifies *when* to route (compaction trigger, consecutive failures, mechanical-mode-confirmed) but not *how to know a routing decision was wrong.* Concretely:

- **No routing log**: There is no specified artifact recording "task X was routed to sidekick at time T because signal S." Without this, a wrong routing decision (e.g., routing a subtly-complex task to a cost sidekick that produces plausible-but-wrong output) is undetectable after the fact.
- **No rollback path**: If a sidekick produces wrong output and the main agent's "機械重驗" catches it, the design says "升級不重試." But what about the *cost already spent* on the wrong sidekick attempt? Is it logged? Attributed? The `evolution/cost-log.jsonl` exists but the design never references it for Fusion routing audit.
- **No A/B framework**: The -35.2% is a simulation, not a measurement. The design does not propose how to *measure* actual savings once deployed (e.g., run Fusion vs non-Fusion on identical tasks and compare). Without this, the architecture cannot be empirically validated — it can only be *believed.*

The workspace's own `subagent-strategy.md` says "verdict 非證據: 採信前機械重驗." The design applies this to sidekick *output* but not to its own *routing claims.* That's a consistency gap a same-vendor reviewer (who shares the "trust the architecture" prior) would miss.

---

## F. Implementation Pragmatism

### F1. Phase 1 "zero-code-change" claim is mostly accurate but oversells one item

The GLM validation report is the authoritative check here, and it found: 3/4 optimization items are genuinely zero-modification (✅), 1/4 (checkpoint-based sidekick persistence) needs modification (⚠️). This is a strong, honest validation. The design plan's §2.3 claim "現有能力,零修改" is **3/4 accurate**. The GLM report correctly downgrades item 4 and correctly flags the ephemeral-environment failure mode (checkpoint is gitignored, so cloud/fresh-clone environments lose sidekick state).

**One gap in the GLM validation**: it does not challenge whether "預設委派" (preset delegation) in optimization item 1 is actually enforceable. The GLM report's own "non-blocking caveat 3" notes "預設委派是行為紀律非強制 gate" (it's behavioral discipline, not an enforced gate) and that there's no PreToolUse hook forcing delegation. This means Phase 1's headline benefit (route mechanical tasks to sidekick) depends entirely on the main agent *choosing* to delegate — which, in practice, agents frequently don't (the "agentic laziness" / "self-preferential bias" failure modes documented in the workspace's own `subagent-strategy.md`). Phase 1 is zero-code-change but also zero-enforcement. A cross-vendor reviewer would flag this as "zero-code-change and zero-guarantee."

### F2. The AGENTS.md Protocol draft (1077 bytes) is too abstract to guide implementation

Mechanical verification: the draft is 1077 bytes, contains zero model names (grep confirmed: 0 matches). It passes the byte threshold and the L1 zero-model-name rule. But as an *implementation guide*:

- **It describes roles and signals, not mechanisms.** "compaction 觸發 → 評估升降級 model" — *how* do you evaluate? *What* is the decision function? The draft defers all of this to "深究 → research/reports/.../fusion-architecture-design-plan.md §2.5," which itself defers to the Phase 1-3 implementation paths. A reader of the AGENTS.md draft alone cannot implement Fusion.
- **It has no failure handling.** The "切換時機" table has "連續失敗 → 升級 sidekick 檔位" but no definition of "連續" (how many? 1? 3?), no definition of "失敗" (crash? wrong output? timeout?), and no path for when the upgrade *also* fails.
- **It is a pointer, not a protocol.** A protocol should be sufficient for two independent implementers to produce compatible behavior. This draft is not — it's a summary that requires reading the full design plan to act on.

**Verdict**: The draft is a well-formed *summary* for AGENTS.md's byte-constrained context, but calling it a "Protocol" overstates its implementability. It would be more accurately titled "Fusion Protocol Summary" or "Fusion Roles & Signals (see design plan for protocol)."

### F3. The Factory Phase 2 config's 32 doc URLs: information density, not padding — but with a quality concern

Mechanical verification: 32 `docs.factory.ai` URLs, 36 total URLs. This is high density but not padding — each URL is cited in context next to the configuration step it supports. The GLM report's structure (step → doc URL → verification → cost impact) is genuinely useful as a runbook.

**However**, the quality concern a cross-vendor reviewer raises: **every URL is Factory's own documentation**. There are zero independent sources validating Factory Router's 43% claim, zero independent analyses of Mixed Models compatibility behavior, zero third-party tests of the Session API PATCH semantics. The config guide is a faithful *translation of Factory's docs into step-by-step instructions*, but it inherits all of Factory's self-reporting bias. The guide's own risk table flags "43% 成本節省 ⚠️ 廠商自報,需獨立驗證" — good — but then the cost impact sections quote the 43% / 81% figures as if established. A cross-vendor reviewer would keep the numbers but consistently label them "vendor-reported" in every occurrence, not just the risk table.

---

## Mechanical Verification Results

| # | Check | Expected | Actual | Pass? |
|---|-------|----------|--------|-------|
| 1 | AGENTS.md Protocol draft has zero model names | 0 matches | `grep -ciE 'opus\|sonnet\|haiku\|fable\|glm\|kimi\|gpt\|claude\|anthropic\|openai\|deepseek'` = **0** | ✅ PASS |
| 2 | AGENTS.md Protocol draft ≤ 1200 bytes | ≤ 1200 | `wc -c` = **1077** | ✅ PASS |
| 3 | Token simulation Task 3 cost math (existing $0.4613) | $0.4613 | Python calc = **$0.4613** | ✅ PASS |
| 4 | Token simulation Task 3 cost math (fusion $0.2925, 37%) | $0.2925, 37% | Python calc = **$0.2925, 36.6%** (rounds to 37%) | ✅ PASS |
| 5 | Token simulation Task 5 cost math (existing $1.536) | $1.536 | Python calc = **$1.5360** | ✅ PASS |
| 6 | Token simulation Task 5 cost math (fusion $0.729, 53%) | $0.729, 53% | Python calc = **$0.7290, 52.5%** (rounds to 53%) | ✅ PASS |
| 7 | Pricing baseline matches model-profiles.md §0/§2.3 | Haiku $1/$5, Sonnet $3/$15, Opus $5/$25, Fable $10/$50 | model-profiles.md lines 113-117 confirm exact match | ✅ PASS |
| 8 | 1.35x ceiling tokenizer factor documented | documented in §2.3 | model-profiles.md line 120 confirms "ceiling 檔位 tokenizer 較舊版多耗 ~35% token" | ✅ PASS |
| 9 | Factory Phase 2 config has ≥3 `docs.factory.ai` URLs (GLM-B acceptance §4.5) | ≥ 3 | `grep -c` = **32** | ✅ PASS (far exceeds) |
| 10 | Design §5.2 "Mid-session 禁止切換模型" rule check | context-management.md enforces ban | context-management.md line 3: "Mid-session 禁止切換模型" ✅; **BUT** design's Factory Phase 3 PATCH switches mid-session — relies on Factory API being an exception to the Claude Code rule. The design claims this is "API 原生支援" but the workspace rule is harness-agnostic in phrasing. | ⚠️ PARTIAL — the Claude Code path complies; the Factory path relies on an implicit "API layer is exempt" reading not explicit in the rule |
| 11 | Design §5.2 "L1 零模型名" rule check (HARNESS-CORE-v3 §6) | AGENTS.md Fusion Protocol has zero model names | Check #1 confirms 0 matches in the draft | ✅ PASS |
| 12 | Design §5.2 "指揮官不下場" rule check | delegation-protocol.md §1 enforces | delegation-protocol.md §1 confirms "預設委派、例外親做" ✅; **BUT** subagent-strategy.md line 9 supersedes this with "預設最簡拓撲；委派須具名效益（非舊「預設委派、例外親做」）" — the design cites the **older, superseded** phrasing | ❌ FAIL — design relies on superseded delegation rule; current rule requires named benefit, not preset delegation |
| 13 | Design §5.2 "驗證不自驗" rule check | delegation-protocol.md §6 enforces | delegation-protocol.md §6 confirms "產出者不得驗收自己的產出" | ✅ PASS |
| 14 | Devin Fusion 35% / 41% / 88% figures independently verified | ≥1 independent source | WebSearch returns **only Cognition channels + reposts**; scored article rates evidence 6/10 "廠商自報" | ❌ FAIL — no independent verification exists |
| 15 | Devin Fusion 57.6 vs 57.0 quality claim has variance/confidence data | reported or cited | Not present in design or scored article | ❌ FAIL — 0.6-point delta presented without noise floor |

---

## Critical Blind Spots (things same-vendor reviewers would miss)

1. **The -35.2% savings is a workload artifact, not an architecture property.** Same-ecosystem reviewers (who share the "Fusion is good" prior) would accept the headline. A cross-vendor reviewer sees that 84% of the savings (-29.7% of -35.2%) comes from one task type (large migration) that is 10% of the workload by frequency. Remove it and Fusion is a net cost increase. The architecture's value is contingent on a specific workload shape, not on the architecture itself.

2. **The "compaction-time model switch is zero cache penalty" assumption is inherited from Cognition, not verified for Factory.** Same-vendor reviewers trust the Devin Fusion mechanism transfers to Factory's API. A cross-vendor reviewer asks: does Factory's post-compaction context survive a model switch intact, or does the new model reprocess the compacted summary from scratch? The design assumes the former; the API docs (D6) describe the field, not the cache behavior.

3. **The design relies on the superseded delegation rule.** The workspace's `subagent-strategy.md` (current) says "預設最簡拓撲；委派須具名效益" — delegation requires a *named benefit*, not preset delegation. The design plan and GLM validation both cite `delegation-protocol.md` §1's older "預設委派、例外親做." A same-vendor reviewer reading delegation-protocol.md would not notice the conflict because they share the document's framing. A cross-vendor reviewer grepping both files finds the contradiction (mechanical check #12).

4. **Open-source sidekick partial-failure modes are unaddressed.** Same-vendor reviewers (especially GLM and Kimi, who are themselves the proposed sidekicks) have a structural incentive not to foreground their own failure modes. The "no retry on failure" rule handles crashes but is silent on correct-syntax-wrong-logic and plausible-hallucination — the two failure modes most likely from open-source models on mechanical tasks.

5. **Latency and observability are entirely absent.** Same-vendor reviewers focused on cost and quality would not notice the missing dimensions because the design's framing makes them invisible. A cross-vendor reviewer from a latency-sensitive or ops-debugging background immediately asks "how do I know a routing decision was wrong?" and finds no answer.

6. **The verification cost is omitted from the savings figure.** Same-vendor reviewers accept "main agent re-verifies" as a quality mechanism without costing it. A cross-vendor reviewer sees that item-by-item verification by a ceiling-tier main agent is itself a significant cost that, if included, would compress the -35.2% figure.

7. **The FrontierCode 57.6-vs-57.0 delta is presented as meaningful without a noise floor.** Same-vendor reviewers familiar with the benchmark would implicitly know the variance but not flag its absence. A cross-vendor reviewer treats any sub-1-point delta on an undocumented-variance benchmark as noise, not evidence.

---

## Recommendations

**Prioritized by impact on the decision to adopt:**

1. **Reframe the headline savings as workload-conditional, not universal.** Replace "-35.2%" with "−35.2% cost-weighted (−2.8% frequency-weighted) on estimated workspace distribution; savings are driven by large-migration tasks and are negative for cross-module refactor and security review." Do not ship the -35.2% figure without the +2.8% frequency-weighted figure alongside it. **This is the single most important correction.**

2. **Run `evolution/cost-log.jsonl` to get real task distribution weights before quoting any aggregate savings.** The simulation admits the weights are "粗估." The file exists. A 1-hour analysis would replace speculation with measurement and either confirm or invalidate the -35.2% figure for this workspace's actual workload.

3. **Resolve the delegation-rule conflict before implementation.** The design cites the superseded "預設委派、例外親做" (delegation-protocol.md §1). The current rule is "預設最簡拓撲；委派須具名效益" (subagent-strategy.md line 9). Either (a) update delegation-protocol.md to match, or (b) re-anchor the Fusion design to the current rule (each Fusion delegation must name its benefit: context isolation / parallelism / adversarial review / low-risk mechanical volume / noise reduction). Option (b) is more work but more correct.

4. **Specify the partial-failure detection mechanism for open-source sidekicks.** "No retry on failure" is insufficient. Add: (a) orthogonal verification method (main agent re-runs grep with a *different* pattern, not the same one), (b) scope-verification step (main agent confirms the sidekick operated on the intended file(s) before accepting output), (c) citation-existence check for research sidekicks (grep the cited URL, do not trust the sidekick's claim it exists).

5. **Add a latency model, even a rough one.** At minimum: estimate the sidekick round-trip cost (spawn/PATCH + execution + report-back) in wall-clock seconds and compare to inline execution. Explicitly exclude Fusion from latency-sensitive task types (on-call incident response, real-time debugging). The design currently says nothing; saying "Fusion is not recommended for latency-bound tasks" is better than silence.

6. **Add a routing log and an A/B measurement plan.** Without `evolution/cost-log.jsonl` entries recording routing decisions + outcomes, the architecture cannot be empirically validated. Specify: (a) log every Fusion routing decision (task, signal, route chosen, model, cost, outcome), (b) run a 2-week Fusion-vs-non-Fusion A/B on identical task types, (c) report measured savings, not simulated savings. This converts the architecture from "believed" to "verified," per the workspace's own "verdict ≠ evidence" principle.

7. **Verify the compaction-time model-switch cache behavior empirically on Factory before relying on it.** The "zero cache penalty" claim is the load-bearing assumption. Run one test: a Factory session that PATCHes the model at compaction, and measure whether the post-compaction context is reprocessed from scratch or served from the new model's cache. If reprocessed, the -35.2% figure needs a cache-miss penalty correction.

8. **Cost the verification overhead and include it in the savings figure.** For each task type, add the main agent's verification token cost (reading sidekick output at ceiling pricing) to the Fusion cost column. This will reduce the task 3/5 savings and deepen the task 2/4 cost increases, producing a more honest net figure.

9. **Downgrade the "harness-neutral" claim to "bi-harness (Claude Code + Factory)."** The design does not address pure-API, alternative-harness, or orchestration-layer paths. Calling it "universal" or "harness-neutral" overstates portability. The AGENTS.md §1 portability note already admits "switching to Codex/Cursor = rebuild enforcement layer" — the Fusion design should inherit this caveat explicitly.

10. **Rename the AGENTS.md draft from "Fusion Protocol" to "Fusion Protocol Summary" or add a one-line implementability caveat.** As written, it is a pointer to the design plan, not a self-sufficient protocol. A reader who implements only what the draft says will produce an incomplete Fusion.

---

## Final Verdict

**SHIP-WITH-CAVEATS**

**Rationale**: The architecture is internally coherent, the cost math is mechanically correct, the Phase 1 zero-code-change claim is 3/4 validated honestly by the GLM report, and the Factory Phase 2 config is a genuinely useful runbook. However, the headline -35.2% savings is a workload artifact (driven by one task type representing 10% of frequency) that is presented as if it generalizes; the load-bearing "zero cache penalty at compaction" assumption is inherited from Cognition's self-reported blog and not verified for Factory's API; the design relies on a superseded delegation rule; and latency, observability, verification cost, and open-source partial-failure modes are unaddressed. These are fixable with measurement and reframing, not architectural redesign — hence SHIP-WITH-CAVEATS rather than NEEDS-REVISION. The caveats are significant enough that adopting the architecture *as currently described* without running the recommended measurements (real task weights, compaction cache test, A/B validation) would mean shipping a simulation as if it were a result.

**Confidence level**: **Medium-high** on the findings (mechanical checks passed; rule conflict verified by grep; source-dependency verified by web search; cost math verified by Python). **Medium** on the verdict — the gap between SHIP-WITH-CAVEATS and NEEDS-REVISION depends on whether the workspace owner treats "run the measurements first" as a caveat (ship-with-caveats) or a blocker (needs-revision). I lean ship-with-caveats because the architecture is directionally sound and the fixes are additive (measurement, reframing), not structural. Confidence would rise to High if recommendation #2 (real task weights from cost-log.jsonl) and #7 (compaction cache test) were executed and confirmed the assumptions.
