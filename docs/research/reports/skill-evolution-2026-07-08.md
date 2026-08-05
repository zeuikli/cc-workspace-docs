# Skill Evolution Report — autoload-evolution
**Date**: 2026-07-08  
**Target**: `.claude/skills/autoload-evolution/`  
**Triggered by**: auto-evolution agent (refinement_count=0, usage=41)

---

## Quality Assessment (7-Dimension Rubric)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Trigger 清晰度 | 5/5 | Description 明確列所有觸發詞（`/autoload-evolution`, `autoload-evolution:observe/propose/apply/audit`）及反例（手動單行修改 → Edit；SKILL 品質改進 → skill-evolution） |
| 工具宣告完整性 | 5/5 | `allowed-tools: Read, Grep, Glob, Bash, Edit, Write` — 覆蓋所有 Phase 用到的工具 |
| Guard/Verify 可機械驗證 | 4/5 | Phase 4a/4b 有 idempotent bash 指令；Phase 4c eval 委派步驟清晰；**扣 1 分**：baseline 缺失時無明確 fallback 路徑（見 Gap #1） |
| Fallback 路徑 | 4/5 | Phase 6c rollback 有具體指令；**扣 1 分**：Phase 4c baseline 缺失的 fallback 未列出，執行者易卡住 |
| 行數合規 | 5/5 | 281 行 ≤ 350 行門檻 |
| 版本/日期 | 5/5 | `version: 1.0.0` + `review-by: 2026-08-29` |
| Gotcha 記錄 | 5/5 | GOTCHAS.md 有 G1–G5 共 5 條，格式完整（症狀/根因/修復）；SKILL.md 底部也有摘要 |

**加總：33 / 35 → Tier A（優秀）**

---

## Gap 識別

### Gap #1（優先度 P1）：Phase 4c Baseline 缺失 Fallback 路徑不明確

**問題**：Phase 4c 末尾僅一句「baseline 缺失不再是有效跳過理由」，但未給出執行者的具體行動路徑。usage=41 中，遇到 baseline 不存在時執行者不知道下一步是什麼（停 Apply？靜態審查？）。

**訊號來源**：
1. G1（GOTCHAS.md）：「PGE 自評陷阱 — baseline 不存在時直接 SKIP 而非降為 WARN」
2. 使用頻率 41 次但 refinement_count=0，代表此缺口從未被修補

**提案**：在 Phase 4c 末尾新增「Baseline 缺失 Fallback」5 步驟路徑：
```
1. 停止 Apply，不以 baseline 不存在作為 SKIP 理由
2. bash scripts/healthcheck.sh 取得 F0
3. 委派 reviewer agent 靜態 PGE 審查（不同 model，輸出 APPROVE/WARN/REJECT）
4. WARN → 繼續並在 RATCHET 標注「PGE-static-only」；REJECT → Phase 6c rollback
5. Apply 後建立新 baseline commit 入庫
```

**falsifiable_prediction**：Phase 4c 的執行者在 baseline 缺失時不再靜默 SKIP，healthcheck pass-rate 不變（純 fallback 路徑新增，不影響 eval 語意）。

**diff 估計**：+8 行，byte 增量 ~400 bytes（軟性目標範圍內）。

---

### Gap #2（優先度 P2）：CLAUDE_PROJECT_DIR 缺失時無 fallback

**問題**：Phase 1 和 Phase 5 的命令使用 `cd "$CLAUDE_PROJECT_DIR"`，但若此環境變數未設置，bash 指令會靜默 cd 到根目錄，導致所有路徑操作在錯誤位置執行。

**訊號來源**：
1. SKILL.md Phase 5 有 `2026-07-03 Phase 3.4` 的 comment 說明 cwd 問題
2. RATCHET 已知這是歷史問題

**提案**：在 Phase 1 bash 區塊頂部加一行驗證：
```bash
[ -n "$CLAUDE_PROJECT_DIR" ] || { echo "ERROR: CLAUDE_PROJECT_DIR not set; run from repo root or set env var"; exit 1; }
```

**diff 估計**：+2 行。

---

## 建議變更（已被 Write 工具權限阻擋，記錄於此）

由於 `.claude/skills/autoload-evolution/SKILL.md` 寫入權限未授予，本 cycle 未能直接應用改進。完整改進內容如下：

**SKILL.md 版本提升**：`1.0.0` → `1.1.0`

**Phase 4c 新增段落**（於最後一行 `> 規則檔語意變更...` 之後）：

```markdown
**Baseline 缺失 Fallback（語意變更時）**：若 `research/evals/INDEX.md` 或 `baseline-*-scored.md` 不存在：
1. **停止 Apply**，不以「baseline 不存在」作為 SKIP 理由。
2. 先執行 `bash scripts/healthcheck.sh` 取得基線健康快照（記 FAIL 計數 F0）。
3. 委派 reviewer agent 對本次提案做靜態 PGE 審查（不同 model，輸出 APPROVE / WARN / REJECT + 理由）。
4. WARN → 可繼續並在 RATCHET 標注「PGE-static-only」；REJECT → 走 Phase 6c rollback。
5. Apply 後立刻建立新 baseline（若有 `scripts/run-evals.sh`）：commit 入庫供下次 cycle 使用。
```

**Gotchas 區塊更新**（`baseline 已建立` 條目）：
```
- **baseline 已建立**（2026-05-30, 51e02d4）：規則語意變更必跑全套 4c；baseline 缺失不再是跳過理由，見 Phase 4c Fallback
```

---

## METADATA.json 擬更新

```json
{
  "refinement_count": 1,
  "last_reviewed": "2026-07-08",
  "evolution_stage": "stable"
}
```

（evolution_stage 已為 stable，維持不變；quality_score 由 skill-curator 設定，不更動）

---

## 結論

`autoload-evolution` 整體品質 **Tier A（33/35）**，主要弱點是 Phase 4c baseline 缺失時的 fallback 路徑不夠具體。建議在下次有寫入權限的 session 中應用上述 Gap #1 改進。
