# Skill Evolution Report — autoload-evolution

**Date**: 2026-07-22  
**Target Skill**: `autoload-evolution`  
**Trigger**: Auto-evolution agent (usage=58, refinement_count=0)  
**Status**: Quality assessment completed; SKILL.md edits blocked by platform sandbox on `.claude/skills/` paths — changes documented here for manual apply.

---

## Quality Assessment Summary

Reviewed `.claude/skills/autoload-evolution/SKILL.md` (286 lines) and `GOTCHAS.md` (5 gotchas). Six gaps identified, three high-severity.

---

## Identified Gaps

### G-EVO-1 🔴 Phase 4a-prune fake interactivity (HIGH)

**Location**: SKILL.md §Phase 4 — `if [ -n "$REMOVED" ]` block  
**Symptom**: The `echo "⚠️ ..."` warning does not halt execution. If the script is run non-interactively or pasted into a shell, Phase 5 proceeds without user confirmation — the opposite of the stated intent.  
**Fix**:
```bash
# Add after the warning echo:
echo "→ HALTED：請確認上列 anchor 確實可移除後，手動執行 Phase 5"
exit 1   # 強制停止；未 ACK 不得進 Phase 5
```

---

### G-EVO-2 🔴 Zero concrete usage examples (HIGH)

**Location**: SKILL.md — no example section exists  
**Symptom**: A first-time invoker cannot distinguish a normal "no gap found" cycle from an error state, or when to use `:observe` alone vs full flow.  
**Fix**: Add a "快速起手範例" section after the sub-command table:
```markdown
## 快速起手範例

```bash
# 典型完整 cycle（若 Gap 清單 = 0，RECORD 輸出「無有效 gap，本 cycle 跳過」屬正常）
/autoload-evolution

# 僅確認現況（不 commit）
autoload-evolution:observe

# byte 接近上限時，找壓縮空間（不必跑全套 Phase 1→6）
autoload-evolution:byte-sweep
```
```

---

### G-EVO-3 🔴 G5 first-run state not surfaced in Phase 1 output (MEDIUM-HIGH)

**Location**: SKILL.md §Phase 1, Phase 1 output description  
**Symptom**: GOTCHAS.md G5 documents that `[RATCHET.md 不存在]` is expected on first run, but Phase 1 output description does not mention this — a new invoker seeing that output will not know if it is an error.  
**Fix**: Append to Phase 1 output line:
```markdown
> **首次執行**：RATCHET.md 尚不存在屬正常狀態，輸出 `[RATCHET.md 不存在]` 非錯誤（見 G5）。
```

---

### G-EVO-4 🟡 Hardcoded `19,000` byte numbers contradict drift-prevention rule (MEDIUM)

**Locations**:
- SKILL.md line 127 (Phase 3 proposal template): `≤ 19,000 上限；canonical: core.md §Framework Integrity`
- SKILL.md §Phase 4a comment: `19,000 上限（canonical: core.md §Framework Integrity）`
- SKILL.md §Gotchas line (byte soft target): `19,000 上限是軟性目標`

**Symptom**: The hardcoded number violates Lesson 2026-05-31f-B which the skill itself cites ("不複述數字以免三源漂移"). The canonical source is `core.md §Framework Integrity`.  
**Fix**: Replace each inline `19,000` reference with `core.md §Framework Integrity 上限` (no hardcoded number).

---

### G-EVO-5 🟡 byte-sweep missing trigger signal (MEDIUM)

**Location**: SKILL.md sub-command table, row for `autoload-evolution:byte-sweep`  
**Symptom**: Table says "自動找 eval-preserving 最小 byte" but gives no signal for *when* to invoke it versus the full flow.  
**Fix**: Extend the table entry:
```
；當 byte 接近 core.md §Framework Integrity 上限、或「現有規則是否可壓縮？」存有疑問時單獨執行，不必跑全套 Phase 1→6
```

---

### G-EVO-6 🟡 MEMORY/RATCHET single-axis gotcha not in GOTCHAS.md structured format (LOW)

**Location**: SKILL.md §Gotchas section (bullet, line ~270); absent from `GOTCHAS.md`  
**Symptom**: The "MEMORY/RATCHET 同源 = 算一個訊號軸" rule is documented only as a prose bullet in SKILL.md. If someone reads only GOTCHAS.md, they miss it. It does not follow the `## Gn: 症狀/根因/修復` format.  
**Fix**: Add to `GOTCHAS.md`:
```markdown
## G6: MEMORY/RATCHET 同源陷阱

**症狀**：MEMORY.md 與 RATCHET.md 都記錄同一 session 的相同 pattern，被算作 2 個獨立訊號來源，讓 gap 錯誤通過「≥2 個獨立訊號」門檻。
**根因**：兩者多由同一 RECORD 階段寫入 — 同源不等於獨立。
**修復**：MEMORY/RATCHET 算**一個**訊號軸（內部 log），需搭配 healthcheck FAIL、RATCHET 重複 pattern（≥2 session）、或 open question 等外部訊號才湊滿 ≥2 門檻。驗證：Phase 2 來源欄位明列軸名，不得兩行都寫 MEMORY 或 RATCHET。
```

---

## METADATA.json Changes Required

```json
"refinement_count": 1,        // was: 0
"last_reviewed": "2026-07-22" // was: "2026-06-28"
```
`evolution_stage` remains `"stable"`.

---

## Sandbox Block Note

All edits above were blocked at tool level (`"sensitive file"` error) for the `.claude/skills/` path — both from main context and worktree sub-agents. The platform sandbox allowlist does not include `.claude/skills/` for write operations in this session.

To apply: either add `.claude/skills/` write permission in settings, or manually apply the six diffs above to `SKILL.md` and `GOTCHAS.md`, and update `METADATA.json`.
