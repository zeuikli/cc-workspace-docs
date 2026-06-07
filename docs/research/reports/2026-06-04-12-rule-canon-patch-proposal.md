---
title: "12-Rule Canon — Auto-load Patch Proposal (APPLY-gated)"
date: 2026-06-04
status: PROPOSAL — APPLY requires a gated session
branch: feature/karpathy-mnilax-universalization
constraint: "§R1–§R12 conduct articles are NOT touched. Proposal only. Auto-load budget 18,455/19,000 (margin 545 B)."
research: 2026-06-04-karpathy-mnilax-12-rule-universalization-research.md
ruleset: 2026-06-04-12-rule-universal-ruleset.md
type: proposal
---

# 12-Rule Canon — Auto-load Patch Proposal

> **Scope guard.** This is a **proposal**, not an applied change. The §R1–§R12 behavioral articles in `core.md` are **not** modified by any item here. APPLY is a separate gated session (per workspace rule: auto-load changes near the 19,000-byte cap are gated). Current: **18,455/19,000, margin 545 B**.

## Method

Research surfaced 3 candidate gaps. Each was checked against existing auto-load text **before** proposing (R8: read before write; R2: don't build what exists). Result: **1 APPLY-candidate, 1 ref-only, 1 NO-OP (already covered).**

---

## P1 — R6 universalization note (APPLY-candidate)

**Gap:** `context-management.md:20-21` hardcodes `Per-task 4,000 / Per-session 30,000 tokens` with no signal that these are *this workspace's calibrated values*, not universal constants. The universalization research found R6 is the single biggest "portability trap" — anyone copying the canon to another harness/model would inherit the wrong numbers as if they were law.

**Proposed diff (context-management.md, after line 21):**
```diff
   - Per-task budget: **4,000 tokens**（單一工作上限）
   - Per-session budget: **30,000 tokens**（整個 session 上限）
+  - **數字為本 workspace 校準值，非普世常數**：跨 harness/模型移植時，原則（設明確預算 + breach 必 surface）不變，數字依模型與成本自訂。
```

**Byte cost:** ~150 B (CJK). Margin after: 545 − 150 ≈ **395 B** (within budget).

**Why auto-load and not ref-only:** R6 is auto-load; the trap is *at the point the numbers are read*. A →See pointer wouldn't fire when someone copies the literal numbers. This is a 1-line inline note, not new knowledge.

**Falsifiable prediction:**
- After APPLY: `wc -c` total ≤ 18,955 (still < 19,000).
- §R count unchanged = 12 (`grep -c '§R[0-9]' core.md` unchanged).
- R6 budget numbers (4000/30000) **unchanged** — only a note added.
- `bash scripts/healthcheck.sh` FAIL=0.
- **Verify:** `grep -n "非普世常數" .claude/rules/context-management.md` returns 1 line; `wc -c CLAUDE.md .claude/rules/*.md | tail -1`.

---

## P2 — methodology credibility note (ref-only, NOT auto-load)

**Gap:** `.claude/refs/karpathy-mnilax-best-solution.md` lineage cites "41%→3% mistake rate" and "76%→52% compliance past 14 rules" without flagging these are **single-author self-reported, non-peer-reviewed, non-reproducible** numbers. This is exactly the misattribution failure mode MEMORY already records (SELF-ROUTE 65%/39% wrong-sourced; enterprise-failure stat downgraded to LOW). Leaving it unflagged invites the same error on re-cite.

**Proposed change (ref file §規則演化 Lineage, NOT auto-load — zero byte impact on cap):**
```diff
-           50 tasks × 30 codebases × 6 weeks；41%→3% mistake rate
+           50 tasks × 30 codebases × 6 weeks；41%→3% mistake rate
+           [信度 MEDIUM：作者自報實驗，無公開資料集 / 非同儕審查，引用須標「作者自報」]
```

**Byte cost:** 0 on auto-load cap (on-demand ref). Safe to APPLY without gating the cap — but bundle with P1 for one atomic commit.

**Falsifiable prediction:** `grep -n "作者自報" .claude/refs/karpathy-mnilax-best-solution.md` returns ≥1; auto-load `wc -c` total unchanged (ref not in cap).

---

## P3 — R12 "information withholding" (NO-OP — already covered)

**Original hypothesis:** MAST's "Information withholding" failure mode (not sharing partial-failure info) is a gap in R12.

**Check result (R8 before proposing):** `core.md:69` already states:
> 略過步驟／跳過驗證**必須明示**，不得以「完成」「成功」掩蓋靜默跳過。**語氣可調，資訊不省。**

"資訊不省" (information not omitted) + "不得掩蓋靜默跳過" **already covers** MAST information-withholding. **No change needed.** Proposing one would violate R2 (building what exists). Recorded as NO-OP for honesty.

---

## Summary

| Item | Verdict | Auto-load byte Δ | APPLY gate |
|---|---|---|---|
| P1 R6 universalization note | APPLY-candidate | +~150 B → 395 B margin | gated session |
| P2 methodology credibility note | APPLY-candidate (ref) | 0 (on-demand) | bundle w/ P1 |
| P3 R12 info-withholding | **NO-OP (covered)** | 0 | — |

**Net if both APPLY:** auto-load 18,455 → ~18,605, margin 545 → ~395. §R1–§R12 articles **untouched**. R6 numbers **unchanged**. No conduct change — both items are *meta-notes* (one says "these numbers are local," one says "this stat is self-reported").

**Recommendation:** APPLY P1+P2 together in a gated session if the user approves; both are honesty/portability guards, not behavior changes. P3 confirmed NO-OP.
