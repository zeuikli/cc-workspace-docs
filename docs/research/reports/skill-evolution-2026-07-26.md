# Skill Evolution Report — autoload-evolution

**Date**: 2026-07-26  
**Target**: `.claude/skills/autoload-evolution/SKILL.md`  
**Reason flagged**: quality_score=4.0 < 7.0, usage=58, refinement_count=0  

---

## Quality Assessment (7-Dimension Rubric)

| Dimension | Score | Finding |
|-----------|-------|---------|
| Trigger clarity | 3/5 | Sub-commands listed in frontmatter; body has no "when to use / when to skip" quick-ref |
| Tool declaration | 5/5 | `allowed-tools: Read, Grep, Glob, Bash, Edit, Write` — complete |
| Guard/Verify mechanical | 3/5 | 4a-prune guard has bash but missing explicit exit-code contract; not idempotent in spec |
| Fallback paths | 2/5 | Phase 6c rollback exists; no fallback when healthcheck.sh unavailable or eval baseline missing |
| Line count | 4/5 | 294 lines — within ≤350 limit |
| Version/Date | 4/5 | version: 1.0.0 + review-by: 2026-08-29 |
| Gotcha records | 4/5 | 7 in-text gotchas covering key failure modes |

**Total: 25/35 → Tier B**  
**Gap dimensions**: Trigger clarity (3), Guard/Verify (3), Fallback (2)

---

## Proposed Improvements

### Gap 1: Trigger Clarity
**Problem**: No "When to use / When to skip" section in body — users must parse frontmatter description to understand routing.

**Proposed addition** (after intro paragraph, before 子命令 table):

```markdown
## 何時使用 / 何時跳過

**使用**：收到 `/autoload-evolution` 或子命令；RATCHET.md 新增 ≥2 個同類 pattern；healthcheck FAIL > 0 且未有對應規則；byte 超過 canvas 目標需壓縮。

**跳過**：單行手動修改（直接 `Edit`）、SKILL 品質問題（→ `skill-evolution`）、無外部訊號的主觀優化（違反 ≥2 軸訊號要求）。
```

### Gap 2: Fallback Paths
**Problem**: If `healthcheck.sh` is unavailable (CI/sub-agent context) or eval baseline file is missing, there is no defined fallback — the flow has no exit path other than failure.

**Proposed addition** (to intro block):

```markdown
**Fallback**：healthcheck.sh 不可用 → 僅跑 4a byte 預檢 + 4a-prune，標 WARN 繼續；eval baseline 完全缺失 → 語意變更禁止執行（停止並報告），純排版/byte 變更可標 WARN 繼續但仍跑 4a+4a-prune。
```

Also add to Phase 1 comment block:
```bash
# Fallback: scripts/healthcheck.sh 不存在 → echo "WARN: healthcheck unavailable" → 記 WARN，繼續 Phase 1b–1f
```

And to Phase 4c baseline read:
```bash
# Fallback: baseline 檔不存在 → 語意變更禁止執行（停止報告）；純排版/byte → 標 WARN 可繼續
```

### Gap 3: Guard Exit-Code Contract
**Problem**: The 4a-prune guard uses `echo` + comment `# → 停下` but never specifies `exit 1`. Without an explicit exit code, the guard is advisory, not mechanical. The claim of "idempotent bash gate" is not met.

**Proposed change** in 4a-prune bash block — add after the anchor-found branch:
```bash
exit 1   # → 停下，等使用者確認「確實要移除這些 anchor」；未 ACK 不得進 Phase 5
```
And in the else branch:
```bash
exit 0
```

Also add guard doc comment above the block:
```markdown
> **Exit-code 契約**：anchor 命中 → exit 1（需使用者 ACK）；無命中 → exit 0（自動通過）。
```

And new Gotcha entry:
```
- **4a-prune exit-code 契約**：anchor 命中必須 exit 1 停下等 ACK；不得 echo 警告後繼續（fail-open 只針對 hook，不針對互動式 flow）
```

---

## Version Bump

`version: 1.0.0` → `version: 1.1.0`

---

## Status

**Write permission denied** during this evolution run — SKILL.md was not modified.  
This report documents the quality assessment and proposed diff for manual application or a subsequent run with write permissions.

**Proposed METADATA.json updates** (to apply when SKILL.md write succeeds):
- `refinement_count`: 0 → 1  
- `last_reviewed`: "2026-07-26"  
- `evolution_stage`: "stable" (already stable, no change)

---

## Diff Summary (lines changed if applied)

- +9 lines added (When to use section + fallback block + exit-code doc + 1 gotcha)
- ~4 lines modified (4a-prune bash block: add exit 0/exit 1; baseline fallback comment)
- Net: +~13 lines → new total ~307 lines (within ≤350 limit)
