---
title: "R1-R12 Token 效率可執行計劃書（compact re-encode）"
date: 2026-06-04
status: 待核准（本 session 零修改）
baseline_bytes: 18455
cap_bytes: 19000
companion: 2026-06-04-r1r12-token-efficiency-deep-research.md
headroom_bytes: 545
primary_lever: compact re-encode（非 delete-rationale）
target_after: ~17900-18100
type: execution-plan
---

# R1-R12 Token 效率可執行計劃書

> **狀態**：待核准。本 session **零修改**（使用者指令「產出研究報告和可執行計劃書」；R1-R12 調整為下一 gated session）。
> **主力槓桿**：**compact re-encode**（verbose 散文 → 緊湊結構，語義 + 枚舉 + 驗證指令 verbatim 保留）。**禁 delete-rationale**（官方 O4：motivation 助遵守）。
> **下限（取代誤讀的 MAST κ）**：CDCT 語義不可模糊 + 枚舉/驗證指令 verbatim + 不增 constraint 數 + 保留 motivation。
> **走 Harness Loop**：OBSERVE→IDENTIFY→PROPOSE→TEST→APPLY→RECORD；APPLY 前 gate 使用者。

---

## 前置（OBSERVE）

```bash
git branch --show-current   # feature branch
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1   # 18455
bash scripts/healthcheck.sh | tail -3   # 基線 FAIL
grep -c "^## §R" .claude/rules/core.md   # 11
```

---

## 危險表 GATE（每個候選必過此 4 檢，任一觸發 ❌ → 移出 APPLY）

| 檢查 | 通過條件 |
|------|---------|
| G1 語義保留 | re-encode 後行為語義字面可一一對應原文，不進 CDCT ~27 字模糊區 |
| G2 枚舉 verbatim | 不可逆動作清單（DELETE/TRUNCATE/DROP/...）、量化數字、驗證指令逐字不動 |
| G3 不增 constraint | 條文數不變（11+R6）；不拆條 |
| G4 motivation 保留 | 「每條防止哪個失敗模式」的 why 保留（可緊湊表達，不刪意義）|

---

## 行動項清單（逐項 re-encode 候選）

> 每項：位置 → 操作 → before/after 示意 → 估算 → G1-G4 自檢 → 驗證。

### D1 — §R1 Ask-rate 校準散文緊湊化（re-encode，~80-120 B）

**現況**（散文，含「官方實測此 nudge −12pp 無 over-reach」史料數字）：
> **Ask-rate 校準（Opus 4.8）**：小決策（命名 / 格式 / 預設值 / 等價方案擇一）→ 自決並一句註明，不問；scope 變更 / 破壞性動作 → 仍先問。顯露假設保留，僅對「等價瑣碎選擇」免問（4.8 預設過度提問，官方實測此 nudge −12pp 無 over-reach）。

**操作**：散文 → 緊湊（自決清單條列；保留「scope/破壞性必問」+ motivation「4.8 預設過度提問」；−12pp 史料數字可移研究報告引用，**但這是 motivation 證據，保留較安全** → G4 傾向保留，僅壓措辭）。

**G1-G4**：G1 ✅（語義對應）/ G2 ✅（無枚舉動）/ G3 ✅ / G4 ⚠️ 保留 motivation。
**估算**：~80 B（保守，因 G4 限制）。
**驗證**：`grep -c "scope 變更\|破壞性動作" core.md` 不變；自決語義人工核對。

### D2 — §R3 P0 安全例外流程緊湊化（re-encode，~60-100 B）

**現況**：P0 例外含 `git stash → hotfix/p0-* 分支 → 最小 patch → PR → 回報` 流程 + grep 細節散文。

**操作**：流程箭頭鏈保留（已緊湊）；grep 命令 verbatim 保留（G2）；周邊散文措辭壓縮。
**G1-G4**：G2 ✅ grep 字面不動 / G4 P0 觸發條件保留。
**估算**：~60 B。
**驗證**：`grep -c "git stash\|hotfix/p0\|--exclude-dir" core.md` 不變。

### D3 — §R2 / §R12 散文措辭緊湊化（re-encode，~80-120 B）

**現況**：§R2 Simplicity「資深工程師會說太複雜嗎」自我檢驗散文；§R12 PGE「語氣可調資訊不省」+ 截斷標示散文。

**操作**：保留 Rule of 3 數字（G2）、截斷標示格式（G2）、安全例外清單（G2）；壓縮連接散文。
**估算**：~80 B。
**驗證**：`grep -c "Rule of 3\|CONTEXT BOUNDARY\|≥3 呼叫點" core.md` 不變。

### D4 — 長期記憶回路操作散文緊湊化（re-encode，~60-100 B）

**現況**（616 B）：含 MEMORY 更新格式 + 自我改進觸發 + GOTCHAS 同步散文。

**操作**：格式範本 verbatim 保留（G2）；操作步驟散文壓縮。
**估算**：~70 B。
**驗證**：`grep -c "Session YYYY-MM-DD\|GOTCHAS" core.md` 不變。

### D5 — 跨檔殘餘重複去除（去重 TYPE C，~50-100 B）

**現況**：context-management.md compact hint ↔ CLAUDE.md compact 觸發描述可能殘餘重複（#449 C3 已去 byte 門檻重複，此為另一處）。

**操作**：先 `grep` 確認重複實際存在再去重（不臆測）；canonical 留 context-management.md，CLAUDE.md 指針化。
**估算**：~50 B（待 grep 確認）。
**驗證**：去重後語義單一來源；指針存活。

### D6 — MAST κ=0.88 誤讀修正（**非精簡，是糾錯**）

**現況**：core.md / MEMORY 多處把 κ=0.88 當「spec-quality」。
**操作**：core.md 內若有引用 → 修正措辭（κ 是 inter-annotator agreement）；MEMORY 待修 flag（下一 session）。
**注意**：這**不為省 byte**，是 Fail-Loud 糾錯（研究發現 1）。可能**略增** byte（修正更精確）——可接受。
**驗證**：`grep -rn "κ=0.88\|spec.*品質" core.md` 措辭正確。

---

## 回收總計

| 項 | 操作 | 淨回收 |
|----|------|-------:|
| D1 | §R1 Ask-rate re-encode | ~80 B |
| D2 | §R3 P0 流程 re-encode | ~60 B |
| D3 | §R2/§R12 措辭 re-encode | ~80 B |
| D4 | 長期記憶回路 re-encode | ~70 B |
| D5 | 跨檔去重 | ~50 B |
| **小計（保守）** | | **~340 B** |
| D6 | κ 糾錯（非精簡）| ±0（可能略增）|

**保守批 ~340 B**：18,455 → ~18,115，餘裕 545 → **~885**。
（**刻意低於 #449 的 500B**——本輪禁刪 rationale，只 re-encode。少省 byte 換不傷遵守，符合使用者「遵守優先」。）

---

## TEST（APPLY 後必跑，展示前 5 / 後 5 行）

```bash
# 1. byte 回收
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1   # < 18455

# 2. R1-R12 條文數不變（G3）
grep -c "^## §R" .claude/rules/core.md   # == 11

# 3. 枚舉/驗證指令 verbatim 存活（G2，最關鍵）
grep -c "DELETE\|TRUNCATE\|DROP\|terraform destroy\|kubectl delete\|git push --force" core.md   # 不變
grep -c "healthcheck.sh\|wc -c\|--exclude-dir\|hotfix/p0\|Rule of 3\|CONTEXT BOUNDARY" core.md   # 不變

# 4. motivation 保留（G4）— 逐條人工核對「防止哪個失敗模式」未刪
grep -c "防止\|防範\|→ IV reuse\|過度提問" core.md   # 不減

# 5. healthcheck 回歸
bash scripts/healthcheck.sh | tail -5   # FAIL == 基線

# 6. measure.sh
bash scripts/measure.sh 2>/dev/null | grep -i byte
```

---

## Falsifiable Prediction（含遵守度不降驗證）

**改動**：core.md §R1/R2/R3/R12 + 長期記憶回路散文 compact re-encode；跨檔去重；κ 糾錯。**語義 + 枚舉 + 驗證指令 + motivation 全 verbatim/保留**。

**預測**：
1. byte **< 18,455**（保守 ~18,115，餘裕 ≥ 340）；
2. **條文數 == 11**（G3 不增 constraint）；
3. **枚舉/驗證指令 grep 命中全不變**（G2，最強不變量）；
4. **motivation（防止X）grep 不減**（G4）；
5. R1-R12 行為語義**逐條人工可對應原文**（無進 CDCT ~27 字模糊區）；
6. `healthcheck FAIL == 基線`；
7. κ=0.88 措辭修正為 inter-annotator（不再寫 spec-quality）。

**遵守度 eval（證據接地，非自評）**：
- 結構化不變量（G2/G3/G4 grep）= 確定性 proxy（prompt-lifecycle.md 定義的 eval 條件）；
- behavioral eval（task-07/08）需 out-of-band per-model 跑（#439 已知邊界）→ **本批不在 inline 範圍**，列為後續；
- 論文接地：P1 (2604.07192 δ<0.01) 證 re-encode 不傷 CSR = 預測 CSR 不降的一手依據。

**REFUTED 處置**：任一不變量失守 → `git revert`（autoload-evolution：eval 回歸 ≥5pp 即 revert）。

---

## RECORD（APPLY 後）

- 執行報告 → `research/reports/`（逐項 + 前後 byte + TEST 前5/後5行）。
- MEMORY：① 記回收後餘裕；② **修正 κ=0.88 誤讀**（散佈多處）；③ 補 Lesson（前一輪框架被新證據翻轉的教訓）。
- commit：`git commit -- <精確 pathspec>`；commit 前緊鄰 `git branch --show-current`。

---

## 不做什麼（範圍界線，§R3）

- ❌ **不刪 rationale/motivation**（官方 O4 反對；本輪核心修正）
- ❌ 不碰枚舉清單（不可逆動作）、量化數字、驗證指令 verbatim
- ❌ 不增 / 不拆 constraint（MOSAIC/Constraint Decay）
- ❌ 不壓條文到語義模糊（CDCT U-curve）
- ❌ 不用自動壓縮工具（LLMLingua 類，不適用規則檔）
- ❌ 不 mid-session 改（破 cache）——獨立 commit、session 結束後
- ❌ 不把回收餘裕立即回填新規則
