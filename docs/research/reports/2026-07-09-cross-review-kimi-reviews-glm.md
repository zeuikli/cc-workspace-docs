---
title: "Kimi-2.7 Cross-Review of GLM-5.2 Fusion Outputs"
date: 2026-07-09
status: done
method: "Adversarial mechanical re-verification: read source files, run grep/cat commands, fetch Factory docs via HTTP, count checklist items, cross-check line citations"
principle: 驗證不自驗 — producer (GLM-5.2) cannot validate own output; reviewer (Kimi-2.7) must mechanically re-verify every claim
reviewed-outputs: ["research/reports/2026-07-09-fusion-glm-architecture-validation.md (GLM-A)", "research/reports/2026-07-09-fusion-glm-factory-phase2-config.md (GLM-B)"]
reviewer: "Kimi-K2.7 (quality tier, fresh context)"
source-design-plan: research/reports/2026-07-09-fusion-architecture-design-plan.md
type: cross-model-adversarial-review
---

# Kimi-2.7 Cross-Review of GLM-5.2 Outputs

> Reviewer: Kimi K2.7 Code (quality tier, fresh context, did NOT author either reviewed file).
> Reviewed: GLM-5.2's architecture validation (GLM-A) and Factory Phase 2 config (GLM-B).
> Stance: adversarial — assume errors exist until proven otherwise. Every mechanical claim re-run by reviewer.

---

## File 1: Architecture Validation

**Path**: `research/reports/2026-07-09-fusion-glm-architecture-validation.md`
**Scope claimed**: Verify design plan §2.3 Phase 1 ("現有能力,零修改") optimization items.

### Mechanical Verification Results

| # | Claim | Expected | Actual | Pass? |
|---|-------|----------|--------|-------|
| 1 | Checks every Phase 1 optimization item from design plan §2.3 | Cover all items in §2.3 "優化項" list | Design plan §2.3 lists **3 numbered items** under "優化項（不改架構,改使用模式）": (1) 預設委派 cost sidekick, (2) 回報結論+檔案:行號, (3) cache 前綴穩定. GLM validated **4 items** — added `claude-progress.json` checkpoint as item 4. | ⚠️ PARTIAL — see Issue F1-1 |
| 2 | Each item has ✅/⚠️/❌ status | Status marker per item | Item 1: ✅, Item 2: ✅, Item 3: ✅, Item 4: ⚠️. All 4 have explicit status. | ✅ PASS |
| 3 | Each item has file:line evidence | Specific file path + line/section | All 4 items cite specific files (multi-mode-agent.md, multi-mode-skill/SKILL.md, delegation-protocol.md, context-management.md, schemas/progress.schema.json, session-init.sh, handoff/). | ✅ PASS (with precision caveats — see Issue F1-2) |
| 4 | `multi-mode-agent.md` exists with model override + mode injection | File exists, supports model binding | File exists at `.claude/agents/multi-mode-agent.md` (5993 bytes). Frontmatter line 5: `model: sonnet`. Line 14: "你的 model 由 parent 在 spawn 時綁定,不可自切". Line 15: "parent 會在 task description 注入 `[mode: cost\|quality\|ceiling\|frontier]`". | ✅ PASS — capability confirmed |
| 5 | `multi-mode-skill/SKILL.md` exists with router §1 table | File exists, 0–1 locations → cost/haiku | File exists (10923 bytes). §1 table line 29: "\| 0–1 \| cost \| haiku \| low \| inline \| 主對話 inline 或 spawn 1 worker \|". | ✅ PASS — capability confirmed |
| 6 | delegation-protocol.md §4 回報合約 exists | §4 with 結論+檔案:行號 rule | §4 at line 33 ("## 4. 回報合約（child 端）"). Line 35: "只回**結論 + 檔案:行號**;禁貼大段原文". Line 36: "長產物（>30 行）→ 存檔...回傳路徑 + ≤10 行摘要". | ✅ PASS — rule confirmed |
| 7 | context-management.md Static First rule exists | Static First + mid-session禁止切換 | Line 3: "## Prompt Caching（Static First）". Line 5: "CLAUDE.md = 最穩定快取前綴...**Mid-session 禁止**切換模型/增刪 tool/改 CLAUDE.md（破快取）". | ✅ PASS — rule confirmed |
| 8 | checkpoint infrastructure exists (schema + hooks + skill) | progress.schema.json + session-init.sh + SKILL §4/§5 | `schemas/progress.schema.json` (3756 bytes, full schema with task_id/steps[]/current_step/next_action/sessions[]/reminders[]). `session-init.sh` line 359: `PROGRESS_JSON="$WORKSPACE_DIR/claude-progress.json"` + line 427: `if [ -f "$PROGRESS_JSON" ]`. SKILL.md line 101: "每輪寫 `claude-progress.json`". Line 112: "OBSERVE 讀 `claude-progress.json`". | ✅ PASS — infrastructure confirmed |
| 9 | `claude-progress.json` is gitignored (GLM's caveat) | .gitignore contains the file | `.gitignore` line 51: `claude-progress.json`. | ✅ PASS — caveat accurate |
| 10 | handoff/GOTCHAS.md G4 ephemeral failure case exists | G4 documents gitignored+ephemeral loss | GOTCHAS.md G4 (line ~30): "下一 session（雲端 fresh clone）依 MEMORY「見 claude-progress.json round2」找佇列 → 檔案不存在（gitignored + ephemeral 容器）". | ✅ PASS — caveat accurate |
| 11 | GLM claimed to run `grep -q 'multi-mode-agent' .claude/agents/` | If claimed, command should pass | GLM did NOT claim to run this command (grep for "grep -q" / "驗證命令" in validation report = 0 matches). GLM used file:line evidence instead. | ✅ N/A — GLM did not make this claim |
| 12 | Design plan §4.2 verification command works | `grep -q 'multi-mode-agent' .claude/agents/` should pass | Command FAILS (exit 2: "Is a directory"). Correct version `grep -rq` passes (exit 0). This is a **design plan flaw**, not GLM's. GLM wisely avoided relying on it. | ✅ N/A for GLM (design plan issue, flagged separately) |

### Quality Assessment

**Strengths**:
- GLM used **file:line evidence** rather than blanket assertions — methodologically sound.
- GLM correctly identified the `claude-progress.json` checkpoint's **semantic misalignment** (designed for cross-session main-task resume, not sidekick cross-spawn state) and **ephemeral environment failure** (gitignored + cloud fresh-clone loss, backed by GOTCHAS G4). This is genuinely adversarial self-critique — GLM did not rubber-stamp its own design.
- The ⚠️ verdict on item 4 is well-reasoned: checkpoint infrastructure exists, but using it for sidekick persistence requires prompt-layer or 1-line agent rule adjustment. The "為何不是 ❌" justification is logical (infrastructure complete, only usage pattern needs tweak).
- Non-blocking caveats section is honest about gaps: ephemeral failure, Phase 2 being the real blocker, no PreToolUse hard gate for "預設委派".

**Weaknesses**:
- **Line citation precision**: GLM cited `multi-mode-agent.md:8` for `model: sonnet`, but `model: sonnet` is on **line 5** (line 8 is the frontmatter closing `---`). GLM cited `:13-15` for the invariants, but `## 不變式（先讀）` is line 12 and the invariant bullets are lines 14-17. The substance is correct (the content exists in the frontmatter/section), but the line numbers are imprecise by 2-3 lines. This does not invalidate the verdicts but reduces evidence auditability.
- **Scope drift**: GLM treated the `claude-progress.json` checkpoint (which the design plan places under Phase 2 "現狀替代方案") as a 4th Phase 1 optimization item. See Issue F1-1.

### Issues Found

**Issue F1-1 (scope classification — minor)**: The design plan §2.3 lists **only 3 numbered optimization items** under "優化項（不改架構,改使用模式）". The `claude-progress.json` checkpoint appears under the **Phase 2** paragraph ("現狀替代方案: 用 claude-progress.json checkpoint 模擬持久性"). GLM reclassified it as Phase 1 item 4. This is defensible (it is a "現狀替代方案" usable now, hence Phase 1-adjacent), and GLM's ⚠️ verdict is appropriately cautious, but strictly the design plan did not enumerate it as a Phase 1 "優化項". **Impact**: low — GLM was transparent and the verdict is correct; only the scope label is debatable.

**Issue F1-2 (line citation precision — minor)**: As noted, `multi-mode-agent.md:8` should be `:5` for `model: sonnet`; `:13-15` should be `:12-17` for the invariants section. The cited content exists and supports the verdict, but a reviewer mechanically checking `sed -n '8p'` would find `---` not `model: sonnet`. **Impact**: low — substance correct, line numbers off by 2-3.

**Issue F1-3 (adversarial challenge — borderline ✅ on item 1)**: Item 1 ("預設委派") is marked ✅ (zero modification). GLM's own "非阻擋性 caveat #3" admits "預設委派" is **behavioral discipline with no PreToolUse hard gate** — it relies on the main conversation *choosing* to delegate per delegation-protocol.md §1. One could argue this should be ⚠️ (needs modification = a hook) rather than ✅ (zero modification), because without enforcement the "default delegation" can drift (the exact problem the harness's hook-escalation pattern exists to solve, per AGENTS.md §5). GLM's defense (capability exists, enforcement is a separate Phase 2+ concern) is reasonable but the ✅ is **borderline lenient on itself**. **Impact**: medium — this is the kind of self-lenient marking the cross-review is meant to catch. Recommend downgrading to ✅-with-caveat or ⚠️-light.

**Issue F1-4 (Phase 1 feature-dependency check — clean)**: No Phase 1 claim depends on a non-existent Claude Code feature. Items 1-3 rely on existing rules/files (confirmed mechanically). Item 4 relies on existing checkpoint infra (confirmed). The only feature-dependent claim (Phase 2 persistent sidekick with cached context) is correctly deferred to "需 Claude Code 新功能" and not claimed as Phase 1. ✅ No phantom-feature dependency.

### Verdict (File 1)

**PASS-WITH-CAVEATS**

- All 4 validated items have correct substance — the cited files/rules/capabilities exist and were mechanically confirmed.
- GLM was genuinely adversarial on item 4 (⚠️ with detailed reasoning + ephemeral failure caveat), which is the correct self-critical posture.
- Two minor issues: (a) item 4 is a Phase 2 workaround reclassified as Phase 1 (scope label debatable, verdict correct); (b) line citations are imprecise by 2-3 lines (substance correct).
- One borderline issue: item 1's ✅ is arguably lenient given the no-hard-gate admission — recommend noting it as ✅-with-caveat rather than clean ✅.
- No phantom Claude Code feature dependencies detected.

---

## File 2: Factory Phase 2 Config

**Path**: `research/reports/2026-07-09-fusion-glm-factory-phase2-config.md`
**Scope claimed**: Concrete step-by-step Factory Droid Phase 2 configuration (Factory Router + compactionModel + providerLock).

### Mechanical Verification Results

| # | Check | Expected | Actual | Pass? |
|---|-------|----------|--------|-------|
| 1 | `grep -c 'docs.factory.ai'` ≥ 3 | ≥ 3 Factory doc URL citations | **32** occurrences of `docs.factory.ai` | ✅ PASS (32 ≥ 3, ~10x margin) |
| 2 | URL format: `https://docs.factory.ai/...` | Valid Factory doc URL format | 9 unique `docs.factory.ai` URLs + 1 `factory.ai/news/factory-router` URL. All follow correct format. | ✅ PASS |
| 3 | URL reality check — fetch 3 random Factory doc URLs | URLs resolve to real Factory documentation | Fetched 4 URLs via HTTP (update-a-session, settings, mixed-models, factory-router). All returned **HTTP 200** with real Factory documentation content. | ✅ PASS — URLs are real, live Factory docs |
| 4 | Each config step has a specific CLI/API command (not just prose) | Concrete command per step | Step 1: `/model` selector + settings.json edit. Step 2a: `/settings` → "Context and compaction" → `compactionModelMode` + settings.json edit. Step 2b: full cURL PATCH command (copy-pasteable, with headers + JSON body). Step 3: `/model` verification + cURL PATCH for `providerLockTimestamp`. | ✅ PASS — all steps have executable commands |
| 5 | `compactionModel` API field is real | Field exists in Session API PATCH | **CONFIRMED via fetched docs**: Session API PATCH body includes `"compactionModel": "current-model"` (default) + `"compactionThresholdCheckEnabled": true`. GLM's claim exactly matches the official API schema. | ✅ PASS |
| 6 | `compactionModelMode` CLI setting is real | Field exists in settings.json | **CONFIRMED via fetched docs**: Settings doc "Context and compaction" table lists `compactionModelMode` \| string \| `same`, `<modelId>` \| `same` \| "Which model performs compaction: `same` uses the current session model, or specify a model ID." GLM's D5 citation is exact. | ✅ PASS |
| 7 | `providerLock` correction is accurate (no CLI toggle; auto-enforced by Mixed Models rules) | providerLock is NOT a user-settable CLI setting; compatibility is auto-enforced | **CONFIRMED via fetched docs**: Settings doc full settings table has **NO `providerLock` field**. Mixed Models doc states "violations will be prevented by the CLI" and lists 3 compatibility rules (OpenAI↔OpenAI; Anthropic reasoning on↔Anthropic; Anthropic reasoning off↔non-OpenAI). GLM's correction is **accurate and well-reasoned** — the original design plan §2.4 ("設定 `providerLock: anthropic`") referenced a non-existent toggle, and GLM caught this. | ✅ PASS — key claim verified, GLM self-corrected the design plan |
| 8 | `providerLockTimestamp` API field exists (semantics undocumented) | Field exists, meaning unclear | **CONFIRMED**: Session API PATCH body includes `"providerLockTimestamp": "<string>"`. The docs show it as a string field but do NOT document its semantic meaning. GLM's ⚠️ "語意需向 Factory 確認" is accurate. | ✅ PASS |
| 9 | Factory Router "43% aggregate savings" claim | Matches official doc | **CONFIRMED via fetched factory-router doc**: "aggregate cost is 43% lower. The median session costs 81% less, and 61% of sessions are at least 80% cheaper." GLM cited all three figures accurately. | ✅ PASS |
| 10 | Factory Router "GA, no setup required" claim | Matches official doc | **CONFIRMED**: "Factory Router is generally available in the Factory CLI and App model selector, with no setup required." + "Factory Router can be enabled/disabled like any other model today." | ✅ PASS |
| 11 | Mixed Models compatibility rules summary accurate | Matches official doc | **CONFIRMED**: Official doc states "OpenAI models can only pair with other OpenAI models" (encrypted reasoning), "Anthropic models with reasoning enabled can only pair with other Anthropic models", "Anthropic models with reasoning off can pair with non-OpenAI models". GLM's D2 summary is a faithful paraphrase. | ✅ PASS |
| 12 | "19-item checklist" count | Should be 19 if claimed | Report does **NOT claim "19 items"** anywhere (grep for "19" = 0 matches in checklist context). Actual count: **25 checkbox items** (A1-A6=6, B1-B6=6, C1-C5=5, D1-D5=5, E1-E3=3; total=25). | ⚠️ MISMATCH — see Issue F2-1 |
| 13 | Each checklist item is actionable (has a command or verification) | Concrete action per item | All 25 items reference specific commands (`/model`, `/settings`, `cat ~/.factory/settings.json \| grep`, cURL PATCH) or verification steps. | ✅ PASS |

### Quality Assessment

**Strengths**:
- **Every Factory doc URL is real and live** (HTTP 200 verified on 4 fetched). This is the strongest aspect — GLM did not fabricate documentation references.
- **`providerLock` correction is the standout**: GLM caught that the original design plan §2.4's "設定 `providerLock: anthropic`" references a **non-existent CLI toggle**, and correctly reframed it as "遵守 Mixed Models 相容性規則" (auto-enforced by CLI). This is exactly the adversarial self-correction the "驗證不自驗" principle demands. The reviewer independently confirmed via fetched docs that (a) no `providerLock` setting exists in the settings table, and (b) the Mixed Models compatibility rules are auto-enforced ("violations will be prevented by the CLI").
- **Honest ⚠️ flags on unverified specifics**: GLM flagged 5 items as "⚠️ 需確認" — Factory Router exact model ID string, Haiku 4.5 exact model ID, `providerLock` CLI toggle (possibly non-existent), `providerLockTimestamp` semantics, 43% vendor-reported savings. Each ⚠️ is justified by the actual doc gap.
- **Copy-pasteable cURL commands**: Step 2b and Step 3 provide full cURL PATCH commands with headers, URL, and JSON body — executable as-is (after filling `<SESSION_ID>` and `<FACTORY_API_KEY>`).
- **Cost impact + verification method per step**: Each step includes both "驗證方式" (how to confirm it worked) and "成本影響" (quantified savings). This exceeds the "具體 CLI/API 指令" acceptance criterion.

**Weaknesses**:
- **Checklist count mismatch**: The report's checklist has 25 items, not 19 (though the report never claims 19 — the parent task's "19-item" framing was an assumption). See Issue F2-1.
- **Factory Router model ID string unknown**: GLM flags this as ⚠️ but the practical impact is that "路徑 B" (direct settings.json edit) cannot be scripted without first reading the ID from `/model`. GLM correctly recommends "路徑 A" (interactive selector) as primary. This is a real gap in Factory's documentation, not GLM's fault, but it means the "可複製貼上執行" claim is slightly weakened for step 1 path B.
- **Haiku 4.5 model ID unknown**: Same issue — `compactionModelMode` and `compactionModel` both need a concrete model ID string, but the exact Haiku 4.5 ID (e.g., `claude-haiku-4-5-*`) is not in the cited docs. GLM flags this ⚠️ and points to `/model` selector + Available Models page. The cURL/API commands are templated with `<haiku-4.5-model-id>` placeholder, which is honest but not fully copy-pasteable.

### Issues Found

**Issue F2-1 (checklist count — minor, parent-task framing)**: The parent task asked "Is the 19-item checklist actually 19 items?" The report does **not claim 19 items** anywhere. The actual checklist has **25 items** (6+6+5+5+3). The "19" expectation appears to originate from the parent agent's assumption, not from GLM's report. **Impact**: none on GLM's report quality — the checklist is comprehensive (arguably more thorough than a 19-item version would be). Flagging only because the parent task explicitly asked to count.

**Issue F2-2 (model ID placeholders — real but documented gap)**: Steps 1B, 2a, 2b all require a concrete model ID string (Factory Router ID, Haiku 4.5 ID) that the cited Factory docs do not explicitly list. GLM handles this honestly with ⚠️ flags and `<placeholder>` syntax + redirects to `/model` selector / Available Models page. This is a **Factory documentation gap**, not a GLM error, but it means the "可複製貼上執行的 step-by-step" acceptance criterion is only fully met for the interactive (路徑 A) paths and the API structure (the cURL commands are copy-pasteable but need ID substitution). **Impact**: low-medium — honest handling, but a follow-up step "read model IDs from `/model` and record them" should be step 0.

**Issue F2-3 (assumed Factory features that may not exist — clean)**: The reviewer checked each Factory feature GLM's config depends on:
- Factory Router (GA): ✅ confirmed real (fetched doc + news blog).
- `compactionModelMode` setting: ✅ confirmed in settings table.
- `compactionModel` + `compactionThresholdCheckEnabled` API fields: ✅ confirmed in Session API schema.
- `providerLockTimestamp` API field: ✅ exists (semantics undocumented, GLM flagged).
- Mixed Models compatibility auto-enforcement: ✅ confirmed ("violations will be prevented by the CLI").
- `providerLock` CLI toggle: ✅ correctly identified as **non-existent** (GLM's correction).
- No phantom Factory features detected. The only "需確認" items are exact model ID strings (which exist but aren't string-documented) and `providerLockTimestamp` semantics (field exists, meaning unclear).

**Issue F2-4 (43% savings is vendor-reported — GLM flagged)**: GLM correctly notes (報告 §6 風險 2) that the 43% Router savings is "廠商自報,Router 路由决策為黑箱,需獨立驗證". The fetched factory-router doc confirms it is Factory's own claim ("In production, measured as billed usage compared with the same workload priced at top-tier model rates"). GLM's "信任但驗證" posture is correct. ✅ Not an issue — GLM handled it right.

### Verdict (File 2)

**PASS**

- All Factory documentation URLs are real and live (HTTP 200 verified on 4 fetched).
- Every key technical claim (`compactionModel`, `compactionModelMode`, `compactionThresholdCheckEnabled`, `providerLockTimestamp`, Mixed Models compatibility rules, Factory Router GA + 43% savings) was **mechanically confirmed against the official fetched docs**.
- The `providerLock` correction is accurate and is the report's strongest contribution — GLM self-corrected a non-existent toggle in the original design plan, and the reviewer independently confirmed no `providerLock` CLI setting exists.
- Each configuration step has a specific CLI/API command (interactive selector, settings.json edit, or copy-pasteable cURL PATCH).
- Honest ⚠️ flags on all genuinely unverified specifics (model ID strings, `providerLockTimestamp` semantics, vendor-reported savings).
- Checklist has 25 items (report does not claim 19; parent task's "19" was an assumption).
- Minor gap: model ID placeholders mean some commands need ID substitution before execution — but GLM transparently flags this and provides the ID-discovery path (`/model` selector).

---

## Overall Assessment

### Summary of Findings

| File | Verdict | Key Strength | Key Issue |
|------|---------|-------------|-----------|
| File 1 (Architecture Validation) | **PASS-WITH-CAVEATS** | Genuinely adversarial on item 4 (⚠️ + ephemeral failure caveat); no phantom Claude Code feature dependencies | Item 1's ✅ borderline lenient (no hard gate for "預設委派"); line citations imprecise by 2-3 lines; item 4 scope label (Phase 2 workaround reclassified as Phase 1) |
| File 2 (Factory Phase 2 Config) | **PASS** | All URLs real (HTTP 200 verified); `providerLock` correction is accurate self-correction of a design-plan error; every technical claim confirmed against fetched official docs | Model ID placeholders need substitution; checklist is 25 not 19 (report never claims 19) |

**Cross-model validation principle (驗證不自驗)**: UPHELD. GLM-5.2 did not rubber-stamp its own design. The clearest evidence:
1. File 1 item 4: GLM marked ⚠️ (not ✅) on a checkpoint mechanism its own design plan proposed, with detailed reasoning about semantic misalignment and ephemeral failure.
2. File 2 Step 3: GLM caught that the design plan §2.4's `providerLock: anthropic` references a **non-existent CLI toggle** and corrected it to "Mixed Models compatibility rules auto-enforced by CLI" — verified accurate by this reviewer against fetched Factory docs.

**Adversarial check — was GLM too lenient on itself?**: One borderline case found — File 1 item 1 ("預設委派") marked ✅ despite GLM's own admission that it has no PreToolUse hard gate (behavioral discipline only). This is arguably ✅-with-caveat or ⚠️-light rather than clean ✅. All other ✅ marks were mechanically confirmed to be accurate.

### Recommendations for Revision

1. **File 1, Item 1**: Downgrade from clean ✅ to "✅ (with caveat: no PreToolUse hard gate — behavioral discipline only; enforcement is Phase 2+ concern)". This makes GLM's own caveat #3 explicit in the verdict row, not just the footer.

2. **File 1, line citations**: Correct `multi-mode-agent.md:8` → `:5` (for `model: sonnet`) and `:13-15` → `:12-17` (for invariants section). Precision matters for mechanical auditability — a reviewer running `sed -n '8p'` currently finds `---` not the cited content.

3. **File 1, Item 4 scope**: Add a note that this item originates from the design plan's Phase 2 "現狀替代方案" paragraph (not the Phase 1 "優化項" numbered list), and GLM reclassified it as Phase 1-adjacent because it is usable now. This preempts a reviewer accusing scope drift.

4. **File 2, Step 0 (add)**: Insert a "Step 0: Discover model IDs" before Step 1 — run `/model`, record the exact Factory Router model ID string and Haiku 4.5 model ID string. This makes all subsequent commands fully copy-pasteable without placeholder substitution.

5. **File 2, checklist**: No change needed (25 items is fine), but if a specific count is desired, add a header note "（共 25 項）" for clarity.

6. **Both files**: No phantom-feature dependencies detected. No fabricated evidence detected. The reports are trustworthy post-revision.

### Reviewer Confidence

High. All mechanical checks were re-run by the reviewer (grep counts, file existence, line-number audits, HTTP fetches of 4 Factory doc URLs, .gitignore verification, schema/hook/skill existence). The two verdicts are based on independently reproduced evidence, not on trusting GLM's claims.

---

*End of cross-review. Reviewer: Kimi K2.7 Code (quality tier). All mechanical verifications executed 2026-07-09 in fresh context.*
