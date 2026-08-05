---
title: "Sonnet-5 Fresh-Context Adversarial Review of Fusion Architecture Design"
date: 2026-07-09
status: done
ground-truth-read: [".claude/refs/delegation-protocol.md (§1, §4, §6)", ".claude/rules/context-management.md (Static First, mid-session prohibition)", ".claude/refs/model-profiles.md (§0, §1, §2.3, §2.4, §3, §6)", ".claude/skills/multi-mode-skill/SKILL.md (§0, §1, §2, §4)", "AGENTS.md (§2, §4, §6b)", "research/archive/the-loop-harness-v3/HARNESS-CORE-v3.md (v3 鐵律, §6)", ".claude/agents/multi-mode-agent.md (frontmatter, 不變式, Mode 紀律表)"]
mechanical-verification: {'protocol-draft-bytes': 1077, 'protocol-draft-model-name-hits': 0, 'phase2-config-docs-mentions': 32, 'token-sim-math-spotcheck': 'pass'}
parent-artifacts: [research/reports/2026-07-09-fusion-architecture-design-plan.md, research/reports/2026-07-09-fusion-glm-architecture-validation.md, research/reports/2026-07-09-fusion-glm-factory-phase2-config.md, research/reports/2026-07-09-fusion-kimi-token-simulation.md, research/reports/2026-07-09-fusion-kimi-agents-md-protocol-draft.md]
reviewer: "Sonnet-5 (ceiling tier, fresh context, adversarial mode)"
type: cross-review
---

# Sonnet-5 Fresh-Context Adversarial Review of Fusion Architecture Design

## Reviewer Context
- Model: Sonnet-5 (ceiling tier, fresh context)
- Mode: Adversarial — assume wrong until proven correct
- Scope: Full Fusion architecture design + 4 sub-reports + 7 ground-truth workspace files
- Method: Read every artifact fresh, verify every load-bearing claim against workspace SSoT, spot-check arithmetic mechanically.

---

## Part A: Architectural Soundness

### A1. Three-layer architecture is well-defined but has a naming/numbering inconsistency

The design plan §2.2 presents **four** boxes labelled L0–L3 (Fusion Router, Main Agent, Sidekick Agent, Compaction Gate), yet the section title and §2 references call it a "三層架構" (three-layer). The Compaction Gate is described as L3 but is not a persistent agent layer — it is a *transition trigger* embedded in the other layers. This is a presentation defect, not a soundness defect, but in a ceiling-tier design doc the L-numbering ambiguity will cause downstream implementers to misplace the gate (is it a layer or a hook?). **Recommend: rename to "3 layers + 1 cross-cutting gate" and drop the L3 label, or renumber consistently.**

### A2. Boundaries between layers are mostly clear, with one leakage

- L0 (Router) → L1 (Main): clear — Router classifies, Main executes/plans. ✅
- L1 (Main) → L2 (Sidekick): clear — Main delegates, Sidekick reports conclusions only. ✅ Aligned with delegation-protocol.md §4.
- L2 (Sidekick) → L3 (Compaction Gate): **leakage**. The Compaction Gate is drawn as a sibling of Sidekick but its trigger condition ("compaction 觸發 → 評估是否升降級") is a *Main session* event, not a Sidekick event. In the Claude Code path, sidekick is a one-shot sub-agent spawn (per GLM validation §優化項 4) and has **no compaction of its own that matters to routing** — the sidekick's context dies when the spawn ends. So the "compaction-time switching" lever only applies to the **Main agent's** compaction, which in the Claude Code path is governed by context-management.md's mid-session prohibition (see Part B). The architecture diagram implies the gate watches both contexts; in reality on Claude Code it watches only Main, and on Factory it can patch the session. The diagram should annotate which context the gate binds to per harness.

### A3. Missing feedback loop: Sidekick failure → Main upgrade path is described, but Sidekick success → Main downgrade is not a real feedback loop

§2.5 Protocol says "機械模式確認 → 降級" and "連續失敗 → 升級". The upgrade side is concrete (delegation-protocol.md §5 + §6 verification chain). The **downgrade side is hand-waved**: "高檔位解出模式寫成規則,降 cost 批次套用" requires a human-or-Main step to *extract the pattern into a rule* before downgrading. There is no automated mechanism for "sidekick confirmed mechanical → downgrade Main's next-task tier". This is a decision the Router (L0) must make, but the Router in the Claude Code path is the static-position-count classifier from multi-mode-skill §1, which does **not** receive sidekick success as an input. So the "dynamic routing" claim is true for Factory (Session API PATCH can react) but **not for Claude Code Phase 1**, where routing remains static-position-count with post-failure escalation only. The design plan §1.2 honestly lists this as a gap ("workspace 無執行中動態升降級"), but §2.5 Protocol draft then presents the downgrade as a general rule without scoping it to Factory-only. **Recommend: annotate the Protocol's downgrade row as "Factory path only; Claude Code = post-task escalation".**

### A4. "Compaction-time switching = zero cache penalty" claim — partially holds, with a critical caveat

The core Devin Fusion insight (compaction already invalidates cache, so switching model then is "free") is **sound in principle**. But the design over-extends it in two ways:

1. **Compaction does not *fully* invalidate cache.** Anthropic prompt caching has a 5-minute TTL and a minimum block size (Haiku/Opus = 4,096 tokens, Sonnet 4.6/frontier = 2,048 per model-profiles.md §2.4). A compaction rewrites the *middle* of context but the **stable prefix** (CLAUDE.md/AGENTS.md/system prompt) is designed to *survive* compaction — that is the entire point of "Static First" in context-management.md. If the prefix survives compaction and remains cacheable, then switching the *main* model at compaction time **does** invalidate the prefix cache (different model = different cache namespace). So "zero cache penalty" is only true for the *compactionModel* swap (the compaction output model), **not** for swapping the main session model at compaction time. The design conflates the two: §2.2 L3 says "compaction 觸發 → 評估是否升級/降級模型" (main model swap), but the cache-zero claim only rigorously applies to the compactionModel field. **This is a load-bearing conflation.** For the Factory path, swapping the main model via Session API PATCH at compaction time *does* cost the prefix cache of the new model (first-read full price) — it is "free" only relative to swapping at a non-compaction moment, not absolutely free.

2. **Claude Code path cannot do main-model swap at all** (see Part B), so on Claude Code the only compaction-time lever is the compactionModel, which Claude Code does not expose as configurable (it uses the current model per context-management.md). The "zero cache penalty" benefit is therefore **Factory-only**, but §2.2 presents it as a general architectural property.

**Verdict on A4:** The claim is *directionally correct but over-stated*. Precise statement: "swapping compactionModel at compaction time = zero extra cache penalty; swapping the main session model at compaction time = one-time prefix re-cache cost on the new model, which is still cheaper than swapping mid-turn." The design should state this precisely.

---

## Part B: Claude Code vs Factory Droid Path Divergence

### B1. "Claude Code cannot do mid-session model switching" — ACCURATE, verified

context-management.md (Prompt Caching / Static First) states verbatim: "**Mid-session 禁止**切換模型/增刪 tool/改 CLAUDE.md（破快取）；能力升級需求 → sub-agent 檔位 override（載體 `multi-mode-agent`）或新 session,不切主對話模型。" multi-mode-skill §0 不變式 repeats: "model 在 spawn 時綁定,主對話 mid-session 不切 model". multi-mode-agent.md frontmatter `isolation: worktree` + 不變式 "你的 model 由 parent 在 spawn 時綁定,不可自切" confirms sub-agents also cannot mid-run switch.

**The design's claim is correct and well-grounded.** The Claude Code path correctly routes around this via sub-agent spawn (new context) rather than main-session switching. ✅

### B2. Factory Session API PATCH capability — correctly described, with one undocumented field flagged

The phase2-config sub-report (GLM-B) is admirably honest: it explicitly flags that `providerLock` is **not** a documented CLI switch (步驟 3 "重要修正"), that `providerLockTimestamp` exists in the API but its *semantics are undocumented*, and that the exact `model` ID strings for Factory Router and Haiku 4.5 are not in the docs and must be read from the picker. This is exactly the "trust but verify" discipline the workspace demands. ✅

However, the main design plan §1.3 presents `providerLock` as "✅ Session 層級" (a supported feature) without the caveat that GLM-B later discovered. **There is an internal contradiction between the main plan (claims providerLock is a supported session-level feature) and the sub-report (finds it is not a settable CLI switch, only an undocumented API timestamp field).** The main plan should be updated to reflect GLM-B's finding, or the sub-report's "⚠️ 需確認" should propagate up.

### B3. Hidden assumptions about Factory API behavior

Three hidden assumptions that might not hold:

1. **`compactionModel` swap preserves session continuity.** The design assumes PATCHing `compactionModel` mid-session is safe and the session resumes cleanly. The docs (D6) confirm the field exists and PATCH returns 200 with the setting, but there is **no documented guarantee that changing compactionModel mid-session doesn't trigger an immediate re-compaction or reset compaction state**. This needs empirical verification before relying on it.

2. **`compactionThresholdCheckEnabled: true` exposes a compaction-trigger signal to the caller.** Phase 3 (§2.4) says "偵測 compaction 觸發 (compactionThresholdCheckEnabled: true)" — but this flag *enables threshold checking*, it does not *emit an event the caller can hook*. The design assumes a polling/event model for "detect compaction triggered → PATCH model" that is not documented. The actual mechanism (webhook? polling GET session? CLI hook?) is unspecified. **This is the single biggest unstated assumption in the Factory Phase 3 design.**

3. **Factory Router is treated as a settable `model` value.** GLM-B correctly flags the ID string is undocumented, but the deeper assumption is that Router can be *combined* with a separately-configured `compactionModel`. If Router is itself doing per-task model routing, layering a fixed compactionModel on top may interact (does Router override compactionModel per-task? unknown). The design does not address this interaction.

---

## Part C: Token Savings Claims

### C1. -35.2% cost-weighted savings — math verified, but the weighting is the weak point

I mechanically spot-checked the arithmetic (Python recompute):

| Task | Reported existing | Recomputed existing | Reported fusion | Recomputed fusion | Reported % | Recomputed % |
|------|------------------|--------------------|----------------|------------------|-----------|--------------|
| 3 (deep research) | $0.4613 | $0.4612 | $0.2925 | $0.2925 | 37% | 36.6% |
| 5 (large migration) | $1.536 | $1.536 | $0.729 | $0.729 | 53% | 52.5% |
| **Aggregate** | $2.477 | $2.4772 | $1.605 | $1.6046 | -35.2% | -35.2% |

**Arithmetic is correct** (rounding-only differences). ✅

**But the -35.2% headline is fragile because it is dominated by a single task type:**

| Task | Share of existing total cost |
|------|------------------------------|
| 5 (large migration) | 56.0% |
| 3 (deep research) | 21.6% |
| 4 (security review) | 17.3% |
| 2 (cross-module refactor) | 4.6% |
| 1 (single-file) | 0.5% |

Task 5 alone contributes -29.7pp of the -35.2% (i.e., **84% of the headline savings come from one task type** that the simulation itself flags as "量級不同,僅供架構對比" and based on a Twitter-sourced, unconfirmed $1,146 figure). If Task 5's frequency or cost share is even half of the assumed 56%, the aggregate drops to ~-20%. The frequency-weighted view (+2.8%) tells the opposite story. **The truth is task-structure-dependent, and the design plan headline leans on the cost-weighted number while burying the frequency-weighted number.** A ceiling-tier doc should lead with *both* and state the dependency explicitly.

### C2. Sidekick overhead accounting — partially accounted, two gaps

The simulation *does* account for spawn cost (sidekick input/output tokens are line-itemed) and context transfer (sub-agent 交辦 prompt ~1,500 tokens is in §1.3). Good. Two gaps:

1. **Verification overhead is not costed.** delegation-protocol.md §6 requires "sidekick 產出由 main 機械重驗" — the Main agent re-reads/re-greps the sidekick's output. This verification cost (Main agent input tokens to re-read the diff/files) is **not in any task's Fusion column**. For Task 5 (16 PRs), Main reviewing each PR's 50-line diff = 16 × (read diff + grep verify) is non-trivial and would erode the 53%. The simulation mentions "ceiling 審查每個 PR（已含）" in the 品質影響 note but the Main input token line (40,000) does not visibly include 16 × diff-read. **Under-costed by likely 10-20k Main input tokens for Task 5.**

2. **Session overhead (O9) is explicitly excluded** (§5 limitation 5 acknowledges this). model-profiles.md §5 O9: cost 檔位 fixed overhead 76.2k tokens > quality 73.9k. For Task 1 (single-file, $0.0117), the real cost is dominated by overhead, so the "0% difference" is correct in *delta* but misleading in *absolute* terms — both architectures pay ~$0.05-0.10 of fixed overhead the simulation omits. Not a savings error, but the per-task absolute numbers are lower bounds.

### C3. +36% cost increase for cross-module refactor (Task 2) — acceptable as a design choice, but the framing is a design flaw

Task 2 goes from $0.0984 (quality親做) to $0.1341 (ceiling main + cost sidekick) = +36%. The simulation justifies this as "品質換成本" (ceiling planning + adversarial review improves quality). **This is a legitimate design choice, but it is *not token savings* — it is a quality upgrade priced as a cost increase.** The problem is the *architecture name*: "Token 節省策略" (Token Saving Strategy) implies savings across the board. A design that increases cost on 25% of tasks (by frequency) / 4.6% (by cost) while saving on 30% is really a **quality-cost reallocation**, not a savings strategy. The frequency-weighted +2.8% makes this visible. **Recommend: reframe §3 from "Token 節省策略" to "Token 重分配 + 節省策略" and explicitly mark Tasks 2 & 4 as quality-investment zones where cost increase is intentional and accepted.** Currently the design quietly absorbs the increase under a savings headline.

---

## Part D: Workspace Alignment

### D1. §5.2 claim: "Mid-session 禁止切換模型 — Claude Code 路徑用 sub-agent spawn 不切主對話" — CONSISTENT ✅

Verified against context-management.md ("能力升級需求 → sub-agent 檔位 override") and multi-mode-skill §0 ("要換檔位 → 用 sub-agent `model` override 或新 session"). The Claude Code path is genuinely compliant. The claim is accurate.

### D2. §5.2 claim: "Factory 路徑用 compaction 時切換（API 原生支援）" — CONSISTENT but with the cache caveat from A4

Factory Session API PATCH of `compactionModel` is documented (D6). ✅ But the §5.2 table frames this as simply "API 原生支援" without noting that swapping the *main* model (not just compactionModel) at compaction time still costs prefix cache (see A4). The claim is *literally* consistent (the API does support it) but *rhetorically* overclaims the cache-zero benefit.

### D3. §5.2 claim: "L1 零模型名 — AGENTS.md Fusion Protocol 不含模型名" — VERIFIED ✅ (with a structural caveat)

Mechanical verification: the protocol draft (kimi-agents-md-protocol-draft.md) is **1077 bytes** (≤1200 ✅) and contains **0** matches for `opus|sonnet|haiku|fable|glm|kimi|gpt|claude|anthropic|openai` (✅). The draft uses tier words (cost/ceiling) and "cost 檔" only. **Compliant with HARNESS-CORE-v3 v3 鐵律** ("L1 不出現模型名").

**Structural caveat:** The draft is labelled "§7. Fusion Protocol" but the *live* AGENTS.md currently ends at §6b (verified: no §7, no "Fusion Protocol" string in the live file). So the draft is a **proposal not yet merged**. The design plan §2.5 and §5.2 present it as if it were a workspace rule ("在 AGENTS.md 新增"), which is correct intent but the §5.2 table row "本設計如何遵守" implies the Protocol is already enforcing — it is not yet enforced. **Recommend: §5.2 should say "（草案,待 merge）" for the L1 row.**

### D4. §5.2 claim: "指揮官不下場 — Main Agent 預設委派,例外親做" — CONSISTENT ✅

Matches delegation-protocol.md §1 verbatim ("預設委派、例外親做"). The Fusion Main Agent role is a direct mapping of the existing 指揮官 concept. ✅

### D5. §5.2 claim: "驗證不自驗 — Sidekick 產出由 Main Agent 機械重驗" — CONSISTENT ✅

Matches delegation-protocol.md §6 ("產出者不得驗收自己的產出"). The T2 異模型互審鏈 (cost→quality→ceiling→frontier) is preserved in §3.3 機制 1-2. ✅

### D6. §5.2 claim: "確定性 gate 永遠 main 親跑 — Fusion 不改變 gate 執行者" — CONSISTENT ✅

delegation-protocol.md §1 T0: "一次性的確定性檢查（單發 grep/test/healthcheck——這類 gate **必須**親跑,不經 subagent 中介）". The design preserves this (Task 1 single-file = T0 exception, main親做). ✅

### D7. AGENTS.md §4 prohibitions — no violation detected

Checked the 5 prohibitions: (1) no `git add -A` guidance in design — ✅; (2) the design does not instruct auto-fixing out-of-scope bugs — ✅ (it defers to delegation-protocol); (3) no prod changes proposed without confirmation — ✅; (4) the design does not skip `/deep-review` — ✅; (5) no emojis in the design files (verified by reading) — ✅. **No §4 violations.**

---

## Part E: Risk Assessment Completeness

### E1. Unaddressed risk #1: Verification cost death-spiral for high-volume sidekick tasks

The design requires Main to mechanically re-verify sidekick output (§6). For Task 5 (16 PRs), if Main must re-read + re-grep each PR, the verification overhead scales with sidekick volume. At sufficient scale, **the verifier (Main, ceiling-priced) becomes the bottleneck and cost driver**, potentially inverting the savings. The design treats verification as a fixed-quality gate but does not model its scaling. This is a real architectural risk: the cheaper the sidekick, the more output it produces, the more Main must verify — a perverse incentive. **Mitigation not in §6: stratified verification (sample-audit N% of PRs, full-verify only on anomaly) per delegation-protocol §6 ("ceiling 產出 → 機械 gate + 關鍵判斷抽問") — but the design applies "機械重驗" uniformly without stratification.**

### E2. Unaddressed risk #2: Prompt-cache namespace fragmentation across multi-model sessions

The design assumes cache is a single shared resource. In reality, each model has its own cache namespace. In the Factory path with Router (per-task routing) + compactionModel (Haiku) + sidekick (cost), a single session may touch 3-4 different models' caches. The *aggregate* cache hit rate may be lower than a single-model session because each model's prefix is built independently. The design's "zero cache penalty" framing hides that **multi-model sessions may have lower overall cache efficiency than mono-model sessions**, even if each *switch* is free. This is not in §6.

### E3. Unaddressed risk #3: Checkpoint persistence in ephemeral/cloud environments (partially in GLM validation, not in main §6)

GLM validation §優化項 4 non-blocking caveat 1 documents that `claude-progress.json` is gitignored + ephemeral in cloud containers (handoff GOTCHAS G4 real failure case), so the checkpoint-based sidekick persistence simulation **fails in cloud/fresh-clone environments**. This is a real, documented limitation — but it lives only in the GLM sub-report, **not in the main design plan §6 risks**. The main plan §6 risk 1 mentions "Phase 2 persistent sidekick 需新功能" but does **not** mention that even the Phase 1 checkpoint simulation is environment-fragile. **Recommend: promote GLM's ephemeral caveat to main §6.**

### E4. "Eval-hack risk for open-source models" — addressed in §3.3 but inadequately scoped

§3.3 機制 3 says "檔位越高驗證越嚴（frontier = +對抗稽核）" and §6 risk 4 says "開源模型 eval-hack 風險未知". model-profiles.md §1 rates non-Claude models as "未知=當最高處理" (treat unknown as highest risk) and §6 (non-Claude接入程序) says first calibration requires 5-10 representative tasks *including eval-hack trap tasks* in the actual non-Claude environment — status **BLOCKED-EXTERNAL** (cannot run in Claude Code session). **The design's Phase 2 Factory BYOK path (sidekick = GLM-5.2 or Haiku) implicitly assumes open-source sidekick capability is adequate, but the workspace SSoT says open-source model calibration is BLOCKED and unverified.** The design should explicitly gate the GLM/Kimi sidekick path on completing the §6 non-Claude calibration procedure, not assume it. Currently §4.1 assigns GLM-5.2 as "ceiling 檔,開源" with "SWE-bench Pro 62.1% 接近 Opus" — but model-profiles.md §0 notes GLM-5.2 is "**目前不在 workspace 使用**;其 Z.ai API 走中國伺服器有 GDPR/合規風險,企業任務勿用 API 模式". **The design uses GLM-5.2 as a reviewer/simulator without addressing the documented GDPR/compliance risk for enterprise tasks.** This is a compliance gap, not just an eval-hack gap.

### E5. Model availability/deprecation risk — NOT addressed

§6 lists 5 risks; none cover model deprecation. Yet model-profiles.md §0 documents a **real precedent**: "Fable 曾 72h 無預警下架實證,含 Bedrock". The entire Fusion design assumes GLM-5.2, Kimi K2.7, Haiku 4.5, Opus 4.8, Fable 5 are stably available. If any sidekick model (especially open-source GLM/Kimi with no SLA) is deprecated or becomes unavailable, the architecture's cost model breaks. The design should add: "**Model-deprecation contingency**: sidekick tier must have ≥2 qualified candidates; if a sidekick model is discontinued, fallback to next cost-tier Claude model (per model-profiles §0 single-vendor risk note).**"

### E6. Unaddressed risk #4: Router black-box + verification loop cost

§6 risk 2 flags Router as black-box (43% vendor-reported). Good. But the *verification* of Router's decisions (per §5.1 "供應商工具也需信任但驗證") has a cost the design does not model: if Main must audit Router's per-task routing choices, that is additional Main overhead. The design assumes Router is trusted-enough to not audit per-task, which *contradicts* §5.1's own principle. Either Router is trusted (drop the §5.1 caveat) or it is audited (add the audit cost). The design holds both positions simultaneously.

---

## Part F: Feasibility

### F1. Phase 1 "zero code changes" — VERIFIED as accurate (with the checkpoint caveat)

GLM validation independently verified 3/4 Phase 1 optimizations are zero-modification (✅×3) and 1/4 (checkpoint persistence) needs a small prompt-layer or 1-line agent-rule tweak (⚠️). I re-verified the load-bearing claims:

- multi-mode-agent.md frontmatter confirms `model: sonnet` default + parent override at spawn. ✅
- multi-mode-skill §1 confirms 0-1 位置 → cost → haiku → inline/spawn. ✅
- delegation-protocol §4 confirms 回報合約 (conclusion + file:line). ✅
- context-management.md Static First confirms cache prefix stability. ✅

**The "zero code changes" claim for 3/4 items is accurate.** The 1/4 (checkpoint) is honestly flagged by GLM as ⚠️, not oversold. **Phase 1 is feasible as described.** ✅

### F2. Checkpoint-based persistence simulation — realistic but explicitly a simulation, not persistent cache

The design plan §2.3 itself states: "這不是真正的 cache 持久化,但可減少重複 context 建構的 token 開銷." GLM validation independently confirms the checkpoint infrastructure (schema + hooks + skill) exists but flags (a) semantic misalignment (checkpoint is for main-task resume, not sidekick cumulative context), (b) ephemeral/cloud failure (GOTCHAS G4), (c) missing sidekick read entry point. **The design is honest that this is a simulation. The feasibility concern is whether the *token savings* claimed in the simulation (which assumes "Phase 2/Factory 已落地" per token-sim §5 limitation 4) actually materialize in Phase 1 with one-shot spawns.** They do not fully — Phase 1 sidekick is one-shot, so the "sidekick 持久 context" savings in Tasks 3/5 are Phase 2/Factory savings, not Phase 1. The simulation acknowledges this (limitation 4) but the main plan's Phase 1 framing does not clearly separate "Phase 1 feasible" from "Phase 1 savings". **Recommend: state that Phase 1 delivers the architecture, not the headline savings; savings require Phase 2/Factory.**

### F3. Factory Phase 2 — feasible with the undocumented-field caveats from B2

GLM-B produced a concrete step-by-step guide with 8 doc URLs (32 `docs.factory.ai` mentions, ≥3 ✅). The configuration is feasible *if* the three undocumented assumptions in B3 hold (compactionModel mid-session safety, compaction-trigger signal mechanism, Router+compactionModel interaction). **Feasible contingent on empirical verification of B3 assumptions.** Not a hand-wave, but not yet verified.

### F4. Factory Phase 3 (API mid-session Fusion) — feasible in API mechanics, unproven in trigger mechanism

The PATCH mechanics are documented. The "detect compaction triggered → PATCH" loop (§2.4 Phase 3) is the unproven part (B3 assumption 2). Without a documented webhook/event/polling contract for compaction-trigger, Phase 3 is **design-complete but integration-unproven**. This is acceptable for a "proposed" architecture but should not be presented as "現有能力" — Phase 3 requires *building* the trigger-detection integration, which is code, not configuration.

---

## Mechanical Verification Results

| # | Check | Expected | Actual | Pass? |
|---|-------|----------|--------|-------|
| 1 | `wc -c` protocol draft ≤ 1200 bytes | ≤1200 | 1077 | ✅ Pass |
| 2 | `grep -ciE 'opus\|sonnet\|haiku\|fable\|glm\|kimi\|gpt\|claude\|anthropic\|openai'` protocol draft = 0 | 0 | 0 | ✅ Pass |
| 3 | `grep -c 'docs.factory.ai'` phase2-config ≥ 3 | ≥3 | 32 | ✅ Pass |
| 4 | Token sim Task 3 math (existing $0.4613, fusion $0.2925, 37%) | match | $0.4612 / $0.2925 / 36.6% | ✅ Pass (rounding) |
| 5 | Token sim Task 5 math (existing $1.536, fusion $0.729, 53%) | match | $1.536 / $0.729 / 52.5% | ✅ Pass (rounding) |
| 6 | Token sim aggregate (-35.2%) | match | -35.2% | ✅ Pass |
| 7 | context-management.md mid-session prohibition exists | present | present (verbatim) | ✅ Pass |
| 8 | multi-mode-skill §0 "mid-session 不切 model" invariant | present | present (verbatim) | ✅ Pass |
| 9 | delegation-protocol §6 "驗證不自驗" exists | present | present (verbatim) | ✅ Pass |
| 10 | HARNESS-CORE-v3 L1 zero-model-name rule | present | present ("L1 不出現模型名") | ✅ Pass |
| 11 | Live AGENTS.md has §7 Fusion Protocol merged | absent (proposal) | absent (no §7 in live file) | ⚠️ N/A — draft not merged |
| 12 | model-profiles §0 GLM-5.2 GDPR/compliance caveat | present | present ("Z.ai API 走中國伺服器有 GDPR/合規風險,企業任務勿用") | ✅ Pass (caveat exists; design did not cite it) |

---

## Critical Issues (must fix before implementation)

1. **Cache-zero claim is over-stated and conflates compactionModel swap with main-model swap (A4).** The "零額外 cache 懲罰" claim rigorously holds *only* for the compactionModel field. Swapping the main session model at compaction time still costs a one-time prefix re-cache on the new model. §2.2 L3 and §2.5 Protocol must state this precisely and scope the cache-zero benefit to the compactionModel lever only. This is load-bearing because the entire "compaction-time switching = free" narrative drives the Factory Phase 3 design.

2. **Internal contradiction on `providerLock` (B2).** Main plan §1.3 lists `providerLock` as "✅ Session 層級" (supported feature); GLM-B sub-report finds it is *not* a settable CLI switch and `providerLockTimestamp` semantics are undocumented. The main plan must be corrected to match GLM-B's verified finding, or implementers will attempt to set a non-existent switch.

3. **Factory Phase 3 trigger-detection mechanism is unspecified (B3 assumption 2).** "偵測 compaction 觸發 → PATCH model" assumes an event/polling contract that no Factory document describes. Phase 3 must either (a) specify the actual detection mechanism (webhook? polling GET? CLI hook?) with doc citation, or (b) be downgraded from "現有能力,配置層" to "需整合開發". As written, Phase 3 is integration-unproven.

4. **Headline -35.2% savings is single-task-dominated and task-structure-fragile (C1).** 84% of the headline comes from Task 5 (large migration, 56% cost share), which is itself based on an unconfirmed Twitter-sourced figure. The design must lead with *both* frequency-weighted (+2.8%) and cost-weighted (-35.2%) views and state explicitly that savings are realized only on mechanical-proportion-heavy tasks. Leading with -35.2% alone is misleading for a ceiling-tier doc.

5. **GLM-5.2 / Kimi K2.7 used as reviewers/simulators without addressing documented GDPR/compliance risk (E4).** model-profiles.md §0 explicitly warns "Z.ai API 走中國伺服器有 GDPR/合規風險,企業任務勿用 API 模式" for GLM-5.2, and §6 marks non-Claude calibration as BLOCKED-EXTERNAL. The design assigns GLM-5.2 as ceiling-tier reviewer and Kimi as simulator without gating on the §6 calibration procedure or citing the compliance caveat. For an owner whose domains include ISO 27017 and enterprise GCP, this is a compliance gap that must be resolved before any BYOK sidekick deployment.

---

## Minor Issues (should fix)

1. **Layer numbering inconsistency (A1):** §2.2 title says "三層" but diagram shows 4 boxes L0-L3. Rename to "3 layers + 1 cross-cutting gate" or renumber.

2. **Compaction Gate binding context unclear in diagram (A2):** Annotate which context (Main vs Sidekick) the gate watches per harness; on Claude Code it watches Main only.

3. **Downgrade feedback loop scoped to Factory-only (A3):** §2.5 Protocol downgrade row should note "Factory path only; Claude Code = post-task escalation" since Claude Code's router is static-position-count.

4. **Verification overhead not costed in token sim (C2):** Main's mechanical re-verification of sidekick output (§6 requirement) is not in any Fusion column. Add ~10-20k Main input tokens for Task 5.

5. **"Token 節省策略" framing hides quality-investment cost increases (C3):** Tasks 2 & 4 cost *more* under Fusion by design (quality upgrade). Reframe §3 as "Token 重分配 + 節省策略" and explicitly mark Tasks 2 & 4 as accepted quality-investment zones.

6. **§5.2 L1 row implies Protocol is enforced; it is a draft (D3):** Add "（草案,待 merge）" to the §5.2 L1 zero-model-name row.

7. **Checkpoint ephemeral failure not in main §6 (E3):** Promote GLM validation's cloud/ephemeral caveat (GOTCHAS G4) to main design plan §6 risks.

8. **Model-deprecation contingency missing (E5):** Add a §6 risk for sidekick model deprecation (Fable 72h precedent documented in model-profiles §0); require ≥2 qualified sidekick candidates per tier.

9. **Router black-box + verification contradiction (E6):** §5.1 says "供應商工具也需信任但驗證" but the design does not model Router-decision audit cost. Either trust Router (drop caveat) or add audit cost.

10. **Phase 1 framing conflates "feasible" with "delivers savings" (F2):** Phase 1 delivers the architecture; headline savings require Phase 2/Factory (token-sim §5 limitation 4). State this separation explicitly.

11. **Protocol draft uses "§7" label but live AGENTS.md ends at §6b:** When merging, verify §7 is the correct next section number and does not collide with future §6c/§7 additions.

---

## Strengths (what the design gets right)

1. **Honest sub-report discipline.** GLM-B explicitly flags 3 undocumented/unsupported Factory fields (providerLock, model ID strings, providerLockTimestamp semantics) rather than papering over them — exactly the "trust but verify" behavior the workspace demands. This is ceiling-tier integrity.

2. **Phase 1 "zero code changes" claim is verified accurate for 3/4 items.** GLM validation independently confirmed each optimization against file:line evidence, and the ⚠️ on item 4 is honestly flagged, not oversold.

3. **Protocol draft is mechanically L1-compliant.** 1077 bytes, 0 model names, uses tier words only — passes the HARNESS-CORE-v3 v3 鐵律. The draft is a clean, mergeable artifact.

4. **Token simulation arithmetic is correct.** All spot-checked figures (Tasks 3, 5, aggregate) recompute to the reported values (rounding-only differences). No fabricated numbers.

5. **Claude Code vs Factory path divergence is correctly identified and routed around.** The Claude Code mid-session prohibition (context-management.md) is accurately cited, and the sub-agent spawn workaround is genuinely compliant, not a workaround-in-name-only.

6. **§5.2 workspace-alignment table is largely accurate.** 5 of 5 checked rules (mid-session, 指揮官不下場, 驗證不自驗, L1 零模型名, 確定性 gate) are correctly mapped to existing workspace rules with correct compliance behavior. No §4 prohibitions violated.

7. **Three-phase progressive rollout is sound.** Each phase is independently verifiable, Phase 1 requires no code, and the design does not attempt a big-bang rebuild. This matches the workspace's "漸進落地" preference.

8. **Sidekick/sub-agent report contract (§4) is correctly inherited from delegation-protocol §4** — conclusion + file:line, no raw dump. This preserves parent context hygiene.

9. **Compaction model = cost tier is a genuinely high-leverage, low-risk optimization** (compaction is summarization, not reasoning; downgrading it has no quality loss). This is the design's strongest concrete saving lever and is correctly identified.

10. **Quality safeguards (§3.3) are correctly inherited** — verification-not-self-verify, adversarial review, eval-hack defense, cross-model cross-check. The design does not sacrifice quality gates for savings.

---

## Final Verdict

**SHIP-WITH-CAVEATS**

**Rationale:** The architecture is structurally sound, the Phase 1 feasibility claim is verified accurate (3/4 zero-modification, 1/4 honestly flagged), the protocol draft is mechanically L1-compliant, and the token arithmetic is correct. However, five critical issues must be resolved before implementation: the cache-zero claim is over-stated and conflates compactionModel swap with main-model swap; the main plan contradicts its own sub-report on `providerLock`; Factory Phase 3's compaction-trigger detection mechanism is unspecified and unproven; the headline -35.2% savings is single-task-dominated and task-structure-fragile (84% from one unconfirmed-source task); and GLM-5.2/Kimi are used without addressing the documented GDPR/compliance risk and BLOCKED-EXTERNAL calibration status. None of these are fatal — all are fixable with precise rewording, doc verification, and a compliance gate — but shipping as-is would propagate an over-claimed cache benefit, an internal contradiction, an unproven integration step, a misleading savings headline, and a compliance gap. Fix the 5 critical issues, then ship.
