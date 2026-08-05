---
title: "GLM-5.2 Cross-Review of Kimi-2.7 Outputs"
date: 2026-07-09
status: completed
inputs: [research/reports/2026-07-09-fusion-kimi-token-simulation.md, research/reports/2026-07-09-fusion-kimi-agents-md-protocol-draft.md, ".claude/refs/model-profiles.md (§0, §2.3, §2.4 pricing matrix)", ".claude/refs/delegation-protocol.md (§1, §3, §4, §6)", "AGENTS.md (section style reference)"]
reviewee: Kimi-K2.7-Code
reviewer: GLM-5.2 (Droid Core)
type: cross-model-review
---

# GLM-5.2 Cross-Review of Kimi-2.7 Outputs

> Adversarial cross-model validation per "驗證不自驗" principle. All mechanical checks re-run independently. No claim from Kimi's reports trusted without verification.

---

## File 1: Token Savings Simulation

**Path**: `research/reports/2026-07-09-fusion-kimi-token-simulation.md`

### Mechanical Verification Results

| # | Claim | Expected | Actual | Pass? |
|---|-------|----------|--------|-------|
| 1 | Covers 5 task types | single-file fix, cross-module refactor, deep research, security audit, large migration | All 5 present (§2 Task 1-5) | PASS |
| 2 | Each task has current vs Fusion comparison with numbers | Per-task cost table with USD figures | All 5 tasks have 4+ row comparison tables with USD | PASS |
| 3 | Pricing from model-profiles.md §2.3 | cost $1/$5, quality $3/$15, ceiling $5/$25, frontier $10/$50 | Report §1.1 table matches exactly; cross-referenced | PASS |
| 4 | Task 1 cost: $0.0117 (current) = $0.0117 (Fusion) | 10500×$1/1M + 240×$5/1M = $0.0105+$0.0012 = $0.0117 | $0.0117 = $0.0117, savings 0% | PASS |
| 5 | Task 2 current cost: $0.0984 | 28000×$3/1M + 960×$15/1M = $0.084+$0.0144 | $0.0984 | PASS |
| 6 | Task 2 Fusion cost: $0.1341 | main: 15000×1.35×$5/1M + 400×$25/1M; side: 18000×$1/1M + 960×$5/1M = $0.1013+$0.010+$0.018+$0.0048 | $0.1341 | PASS |
| 7 | Task 2 savings: -36% | ($0.0984-$0.1341)/$0.0984 = -36.2% | -36.2% ≈ -36% | PASS |
| 8 | Task 3 current cost: $0.4613 | main: 45000×1.35×$5/1M + 1800×$25/1M; sub: 30000×$3/1M + 1500×$15/1M = $0.3038+$0.045+$0.09+$0.0225 | $0.4613 | PASS |
| 9 | Task 3 Fusion cost: $0.2925 | main: 30000×1.35×$5/1M + 1800×$25/1M; side: 35000×$1/1M + 2000×$5/1M = $0.2025+$0.045+$0.035+$0.010 | $0.2925 | PASS |
| 10 | Task 3 savings: 37% | ($0.4613-$0.2925)/$0.4613 = 36.6% | 36.6% ≈ 37% (rounded) | PASS |
| 11 | Task 4 current cost: $0.3698 | main: 50000×$3/1M + 2400×$15/1M; sub: 25000×1.35×$5/1M + 600×$25/1M = $0.15+$0.036+$0.1688+$0.015 | $0.3698 | PASS |
| 12 | Task 4 Fusion cost: $0.4373 | main+side+adv: $0.1485+$0.06+$0.04+$0.005+$0.1688+$0.015 | $0.4373 | PASS |
| 13 | Task 4 savings: -18% | ($0.3698-$0.4373)/$0.3698 = -18.3% | -18.3% ≈ -18% | PASS |
| 14 | Task 5 current cost: $1.536 | main: 60000×1.35×$5/1M + 3000×$25/1M; 16×sub: 20000×$3/1M + 400×$15/1M = $0.405+$0.075+$0.96+$0.096 | $1.536 | PASS |
| 15 | Task 5 Fusion cost: $0.729 | main: 40000×1.35×$5/1M + 3000×$25/1M; 16×side: 22000×$1/1M + 400×$5/1M = $0.27+$0.075+$0.352+$0.032 | $0.729 | PASS |
| 16 | Task 5 savings: 53% | ($1.536-$0.729)/$1.536 = 52.5% | 52.5% ≈ 53% (rounded) | PASS |
| 17 | §3.2 frequency-weighted: +2.8% | 40%×0 + 25%×(-36) + 20%×37 + 5%×(-18) + 10%×53 = 0-9+7.4-0.9+5.3 | +2.8% | PASS |
| 18 | §3.2 weights sum to 100% | 40+25+20+5+10 = 100 | 100% | PASS |
| 19 | §3.3 total current cost: $2.477 | Sum of 5 current costs = 0.0117+0.0984+0.4613+0.3698+1.536 | $2.4772 ≈ $2.477 | PASS |
| 20 | §3.3 total Fusion cost: $1.605 | Sum of 5 Fusion costs = 0.0117+0.1341+0.2925+0.4373+0.729 | $1.6046 ≈ $1.605 | PASS |
| 21 | §3.3 cost-weighted: -35.2% | ($2.4772-$1.6046)/$2.4772 = 35.2% savings | 35.2% | PASS |
| 22 | §3.3 Task 1 cost share: 0.5% | 0.0117/2.4772 = 0.47% | 0.5% (rounded) | PASS |
| 23 | §3.3 Task 2 cost share: 4.6% | 0.0984/2.4772 = 3.97% | 4.0% (report says 4.6%) | **FAIL** |
| 24 | §3.3 Task 3 cost share: 21.6% | 0.4613/2.4772 = 18.6% | 18.6% (report says 21.6%) | **FAIL** |
| 25 | §3.3 Task 4 cost share: 17.3% | 0.3698/2.4772 = 14.9% | 14.9% (report says 17.3%) | **FAIL** |
| 26 | §3.3 Task 5 cost share: 56.0% | 1.536/2.4772 = 62.0% | 62.0% (report says 56.0%) | **FAIL** |
| 27 | §3.3 weighted contributions sum to -35.2% | Sum of claimed contributions: 0+1.7-7.3+1.2-29.7 | -34.1% (report claims -35.2%) | **FAIL** |
| 28 | Acknowledges quality tradeoffs | Not just savings, also quality impact | §2 each task has "品質影響" row; §4 dedicated quality section; tasks 2/4 explicitly note cost increase for quality | PASS |
| 29 | §5 limitations section | Should acknowledge uncertainties | 6 limitations listed (token estimation, Vercel source confidence, weight estimates, sidekick persistence assumption, session overhead, quality not monetized) | PASS |

### Quality Assessment

**Strengths:**
1. All 30 per-task cost calculations (5 tasks × ~6 line items each) are arithmetically correct. Every USD figure reproduces exactly when re-computed from the stated token counts and pricing.
2. Pricing faithfully cross-references model-profiles.md §0/§2.3. The ceiling tokenizer 1.35x factor is correctly applied to input tokens for ceiling models.
3. Honest about tradeoffs: Tasks 2 and 4 explicitly show Fusion costs MORE (negative savings), with quality justification. This is not a one-sided "savings" pitch.
4. The frequency-weighted +2.8% vs cost-weighted -35.2% duality is intellectually honest, showing the result depends entirely on weighting method.
5. §5 limitations are substantive, not boilerplate. The sidekick persistence assumption (limitation 4) and session overhead erosion (limitation 5) are real concerns.
6. The -35.2% headline is mathematically correct via direct computation: (total_current - total_fusion) / total_current = 35.2%.

**Weaknesses:**
1. The §3.3 cost-share decomposition table is internally inconsistent (see Issues #1-#3 below). The headline -35.2% is correct, but the per-task breakdown that supposedly produces it does NOT sum to -35.2%. The shares and contributions appear to be computed from different numbers than the §2 per-task costs.
2. The ceiling tokenizer 1.35x factor is applied ONLY to input tokens, not output tokens. model-profiles.md §2.3 states the tokenizer "較舊版多耗 ~35% token" which is a token-count effect, not a price effect, and should affect both input and output. This systematically understates ceiling model costs in both architectures (though it affects the comparison less since both current and Fusion use ceiling).
3. The quality tokenizer +30% (Sonnet 5 vs Sonnet 4.6) is acknowledged in §5 but not applied. The report states "cost/quality 模型不加乘" as an assumption. This is defensible if the baseline IS Sonnet 5 (comparing to itself), but the ceiling 1.35x factor IS applied, creating an asymmetry. If both are tokenizer-adjusted vs a common baseline, or neither is, the comparison would be cleaner.

### Issues Found

**Issue #1 (MEDIUM): §3.3 cost shares are wrong.**
The reported cost shares (4.6%, 21.6%, 17.3%, 56.0%) do not match the actual shares computed from the §2 per-task costs (4.0%, 18.6%, 14.9%, 62.0%). Task 5 is particularly off: report says 56.0%, actual is 62.0%. The shares appear to be computed from different (unknown) cost figures, not from the §2 table values.

**Issue #2 (MEDIUM): §3.3 weighted contributions don't sum to headline.**
The claimed per-task contributions (0%, +1.7%, -7.3%, +1.2%, -29.7%) sum to -34.1%, not -35.2% as claimed. The -35.2% headline is only correct via direct total computation ($2.477-$1.605)/$2.477. The decomposition table is inconsistent with its own headline number. This suggests the contributions were computed using the wrong cost shares (Issue #1), and the headline was computed separately and correctly.

**Issue #3 (LOW): Tokenizer factor applied asymmetrically.**
The 1.35x ceiling tokenizer factor is applied to input tokens only, not output. For ceiling-heavy tasks (3, 4, 5), this understates both current and Fusion costs. The net effect on savings percentage is small since both architectures use ceiling, but it is a methodological inconsistency. If the tokenizer affects token count, it affects both directions.

**Issue #4 (LOW): Weights are subjective and unvalidated.**
The frequency weights (40/25/20/5/10) are described as "粗估" (rough estimates) based on workspace report distribution. §5 limitation 3 acknowledges this. This is transparent but means the +2.8% frequency-weighted figure has wide error bars. The cost-weighted -35.2% is more robust but dominated by a single task type (large migration at 62% of cost).

**Issue #5 (LOW): Task 5 dominates cost-weighted result.**
Task 5 (large migration) accounts for 62.0% of total current cost and 45.4% of Fusion cost. The -35.2% headline is almost entirely driven by this single task type's 53% savings. If large migrations are rare (10% frequency per §3.2), the cost-weighted figure overweights a rare event. This is acknowledged in §3.4 but could mislead a casual reader who only sees "-35.2%".

**Issue #6 (INFO): Vercel TS7 case confidence.**
The $1,146 Vercel cost figure is from a Twitter source with "確認度中" (medium confidence). The report correctly states it does not depend on this number for its calculations (§5 limitation 2), only using the structural pattern (16 PR + codemod). This is handled correctly.

### Verdict: **PASS-WITH-CAVEATS**

The core arithmetic (all 30+ per-task cost calculations, both headline weighted averages) is correct. The -35.2% cost-weighted figure is mathematically verifiable via direct computation. However, the §3.3 decomposition table has internal consistency errors (wrong cost shares, contributions don't sum to headline) that must be fixed before this table can be trusted as a breakdown. The tokenizer asymmetry and weight subjectivity are acknowledged limitations, not errors. **Recommendation: fix §3.3 cost shares and contributions to match §2 per-task costs, or remove the decomposition and present only the direct total computation.**

---

## File 2: AGENTS.md Fusion Protocol Draft

**Path**: `research/reports/2026-07-09-fusion-kimi-agents-md-protocol-draft.md`

### Mechanical Verification Results

| # | Check | Expected | Actual | Pass? |
|---|-------|----------|--------|-------|
| 1 | File size ≤1200 bytes | ≤1200 | 1077 bytes | PASS |
| 2 | Zero model names (opus/sonnet/haiku/fable/glm/kimi/gpt/claude/anthropic/openai/deepseek/minimax) | 0 matches | 0 matches | PASS |
| 3 | Zero pricing numbers (X%, X$, X tok) | 0 matches | 0 matches | PASS |
| 4 | Section header format aligns with AGENTS.md | `## §N. Title` format | `## §7. Fusion Protocol（跨 harness 通用）` matches `## §N. Title` pattern | PASS |
| 5 | Uses tier words (cost/quality/ceiling/frontier) not model names | Tier words only | Uses "cost sidekick", "升降級檔位"; no model names | PASS |
| 6 | Harness-neutral (no Claude Code/Factory/Devin specific terms) | 0 matches for claude code/factory/devin/.claude/settings.json/skill/hook | 0 matches | PASS |
| 7 | Table format consistent with AGENTS.md | Pipe-delimited tables with header separators | 3 tables using `|---|` format, matching AGENTS.md style | PASS |
| 8 | Contains "深究 →" cross-reference pattern | Links to detail file | `**深究** → research/reports/2026-07-09-fusion-architecture-design-plan.md §2.5` | PASS |
| 9 | Uses "檔位" terminology consistent with AGENTS.md | AGENTS.md §2/§3 use 檔位詞 | File uses "檔位", "cost" consistent with parent | PASS |
| 10 | Number-free (broader check for any digits) | Minimal/zero numbers in body | Only numbers found: "§7" (section number) and "2026-07-09" (date in ref path) | PASS (section numbers and date in cross-ref are structural, not pricing) |

### Quality Assessment

**Strengths:**
1. All three mechanical constraints (≤1200 bytes, zero model names, zero pricing numbers) pass cleanly.
2. Format closely matches AGENTS.md section style: `## §N. Title` header, pipe-delimited tables, blockquote summary, `深究 →` cross-reference footer. This is the correct pattern for an AGENTS.md section.
3. Genuinely harness-neutral: uses abstract terms (主 agent, sidekick, compaction, context, cache) without referencing Claude Code, Factory, Devin, or any specific tool. The term "sub-agent spawn" is slightly CC-flavored but is also used in delegation-protocol.md as a generic concept.
4. Concise: 1077 bytes is well within the 1200-byte cap, leaving room for future edits.
5. The "切換時機" (switch timing) table is actionable and decision-oriented, matching AGENTS.md's TLDR style.

**Weaknesses:**
1. The term "sub-agent spawn" (lines 15-17) is mildly Claude Code-flavored. While "sub-agent" is generic, "spawn" is CC terminology. A truly harness-neutral term would be "dispatch" or "delegate". Minor.
2. The "Cache 紀律" section references "AGENTS.md + system prompt" as the stable prefix. This is correct for the workspace but assumes a system-prompt-based harness. Not a violation, but slightly less universal than it could be.
3. The section number §7 assumes it appends after §6b. This is logical but should be confirmed against the current AGENTS.md structure (which ends at §6b). No conflict detected.

### Issues Found

**Issue #1 (LOW): "spawn" terminology slightly CC-specific.**
Lines 15-17 use "sub-agent spawn" and "spawn 新 context". While "sub-agent" is generic, "spawn" is Claude Code's term for creating sub-agents. For maximum harness-neutrality, consider "dispatch" or "delegate". This does not violate the zero-model-name or harness-neutral checks mechanically, but is a style note.

**Issue #2 (INFO): Section numbering assumes append position.**
The draft is numbered §7, implying it follows §6b. This is correct for the current AGENTS.md structure but should be verified at merge time. No issue with the draft itself.

**Issue #3 (INFO): No explicit "驗證不自驗" mention.**
The draft covers Main/Sidekick roles and cache discipline but does not explicitly mention the "驗證不自驗" (producer cannot validate own output) principle, which is a core delegation-protocol.md §6 rule. This may be intentional (the principle lives in delegation-protocol.md, not AGENTS.md L1), but the Fusion protocol's "Main Agent 監控 sidekick" role implies it without stating it.

### Verdict: **PASS**

All three hard mechanical constraints pass (byte count, zero model names, zero pricing numbers). Format aligns with AGENTS.md section style. Content is harness-neutral. The "spawn" terminology is a minor style note, not a failure. This draft is ready for merge into AGENTS.md as §7, pending the minor terminology consideration.

---

## Overall Assessment

### Summary of Findings

| File | Verdict | Critical Issues | Minor Issues |
|------|---------|----------------|-------------|
| Token Simulation | PASS-WITH-CAVEATS | §3.3 cost shares wrong (4 tasks); contributions don't sum to headline | Tokenizer asymmetry (input only); weights subjective; Task 5 dominates |
| AGENTS.md Protocol Draft | PASS | None | "spawn" term slightly CC-flavored |

**Key finding**: The token simulation's headline -35.2% figure is mathematically correct (verified via direct total computation), and all 30+ per-task cost calculations reproduce exactly. However, the §3.3 decomposition table that breaks down the -35.2% into per-task contributions is internally inconsistent: the cost shares are wrong for 4 of 5 tasks, and the per-task contributions sum to -34.1% instead of -35.2%. This is a presentation/table error, not a calculation error in the underlying costs. The headline number can be trusted; the breakdown table cannot.

**File 2 (AGENTS.md draft) is clean**: all mechanical constraints pass, format is correct, content is harness-neutral. Ready for merge.

### Recommendations for Revision

1. **Token Simulation §3.3 (MUST FIX)**: Recompute cost shares from actual §2 per-task costs. Correct shares: Task 1=0.5%, Task 2=4.0%, Task 3=18.6%, Task 4=14.9%, Task 5=62.0%. Recompute weighted contributions from these shares. The contributions will then sum to -35.2% correctly. Alternatively, remove the decomposition table and present only the direct total: "($2.477 - $1.605) / $2.477 = -35.2%".

2. **Token Simulation §1.1 (SHOULD FIX)**: Either apply the 1.35x tokenizer factor to both input AND output for ceiling models, or explicitly state why output is excluded (e.g., "output token counts are already measured post-tokenizer in the estimate"). Document the asymmetry.

3. **Token Simulation §3.2 (CONSIDER)**: Add a sensitivity analysis on the frequency weights. If Task 5 frequency changes from 10% to 5%, the frequency-weighted result drops from +2.8% to +0.2%. The result is fragile to weight assumptions.

4. **AGENTS.md Draft (OPTIONAL)**: Consider replacing "spawn" with "dispatch" in lines 15-17 for maximum harness-neutrality. This is a style preference, not a requirement.

---

*Cross-review completed 2026-07-09 · GLM-5.2 Droid Core · All mechanical checks re-run independently via Python arithmetic verification and grep/wc*
