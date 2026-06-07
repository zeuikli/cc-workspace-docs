# 執行計劃書 — Zeuik Workspace 準則重構（The Loop）

> **配對報告**：`2026-06-06-zeuik-workspace-canon.md`
> **分支**：`feature/workspace-canon-rewrite`
> **使用者授權**：core.md 改 The Loop 六階段語意 header + §R 編號退役為 inline tag + 同步改 healthcheck gate（2026-06-06 AskUserQuestion 選項 1）。
> **完成條件（機械驗證）**：① 5 檔重寫 ② 新 gate green + mutation-test 證明能抓回歸 ③ healthcheck 全綠 ④ byte ≤19,000 ⑤ coverage checklist 100% 對應 ⑥ commit+pr+merge。

---

## 0. 硬約束（merge 後 GHA 會驗 — 不可違反）

| 約束 | 來源 | 驗證命令 |
|------|------|---------|
| byte ≤ 19,000 | measure.sh L83 | `wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md` |
| 六階段 header 存活（新 gate）| measure.sh 改寫後 | `grep -cE '^## (OBSERVE\|IDENTIFY\|PROPOSE\|APPLY\|TEST\|RECORD)' core.md` = 6 |
| §R inline tag 非 stub | measure.sh 改寫後 | gate awk 檢查 |
| §R6 successor 在 context-management | measure.sh L96 改寫 | `grep -c '§R6\|TEST·Token' context-management.md` ≥1 |
| canonical wc -c 指令存活 | measure.sh L121 | grep |
| refs/README ↔ refs/*.md 一致 | healthcheck §15 | 若新增 ref 必登錄 |
| baseline 已 green | 改動前實測 | gate exit=0 ✅（已驗）|

---

## 1. byte 預算分配（總 ≤18,597，不增；理想下沉後回收）

| 檔 | 現況 byte | 目標上限 | 策略 |
|----|----------|---------|------|
| CLAUDE.md | 2,585 | ≤2,900 | The Loop 速查表取代 12-Rule 表（同等密度）|
| core.md | 9,065 | ≤9,065 | 六階段重組；論文證據下沉 best-solution ref；新內容（三洞見壓縮句）抵銷退役編號省的字 |
| context-management.md | 2,007 | ≤2,100 | §R6→TEST·Token 段；加 HTML comment 一行 |
| output-discipline.md | 1,490 | ≤1,490 | 幾乎不動（橫切層）|
| subagent-strategy.md | 3,450 | ≤3,450 | on-rails/off-rails 一句；其餘不動 |
| **總計** | **18,597** | **≤18,597** | 每檔寫完即 wc -c |

→ 新內容靠「退役 12-Rule 編號表頭 + 論文細節下沉 ref」回收的 byte 容納，淨 ≤0。

---

## 2. 逐檔改動規格

### 2.1 CLAUDE.md
- **12-Rule Canon 表** → **The Loop 六階段速查表**（每階段：階段名 + 一句紀律 + inline §R tag + 防止的失敗）。
- 保留：語言鐵律、Harness Loop 段（升為主敘事）、常駐規則 @import、模式/Effort、暫存。
- Effort 段加一句：「ROI 遞減（xhigh vs high 僅差 2 分/4× 成本，作者自報 LOW）→ 預設 high」。
- 不動：5 源 byte 門檻、sub-agent 不繼承本檔。

### 2.2 core.md（核心重寫）
主結構六階段語意 header，每階段下紀律條 + 行尾 inline `〔§Rn〕`：
```
## 語言 / ## 生產環境安全紅線（不動，置頂）
## The Loop（六階段元迴圈說明）
## OBSERVE — 先讀後動〔§R8〕   ← + on-rails/off-rails
## IDENTIFY — 顯露假設〔§R1〕 + 成功條件〔§R4〕  ← + 四維品質
## PROPOSE — 極簡〔§R2〕 + 外科刀〔§R3〕  ← + AI 四大缺陷
## APPLY — 規範優先〔§R11〕 + 不可逆 gate〔§R1〕  ← + 可推導=噪音
## TEST — 測試驗意圖〔§R9〕 + Fail Loud/PGE〔§R12〕  ← + working≠good + unverified_success
## RECORD — Checkpoint〔§R10〕 + 反思入庫（自我演化）
## 跨切紀律 — 判斷vs決定〔§R5〕 / 浮現矛盾〔§R7〕
## Framework Integrity（含 canonical wc -c 指令 — gate 斷言點，不動措辭）
## 暫存 / 長任務 / 長期記憶 / Git 工作流程（不動）
```
- **coverage 全帶入**：A1-A7 安全紅線、B1-B10 血淚、C1-C17 行為、D1-D13 機制 → 各埋對應階段。
- 論文證據細節 → 不重複（指 best-solution ref）。

### 2.3 context-management.md
- §R6 段改 header `## TEST·Token Budget〔§R6〕`（保 gate 斷言點 b：grep `§R6` ≥1）。
- 加一行：HTML comment 零 token 維護筆記（官方新機制）。
- 其餘（caching/compact/NLAH）不動。

### 2.4 output-discipline.md
- 橫切層，幾乎不動。標註「橫切所有 The Loop 階段」。

### 2.5 subagent-strategy.md
- 委派決策段加 on-rails/off-rails 一句（off-rails 強制人工/加 spec）。
- 其餘不動（verdict 非證據鐵律保留）。

---

## 3. healthcheck gate 改寫（measure.sh L94-121）

### 3.1 改動
- L95 `RB_CORE=$(grep -c "^## §R" core.md)` 比 `=11` → 改 `PHASE_CT=$(grep -cE '^## (OBSERVE|IDENTIFY|PROPOSE|APPLY|TEST|RECORD)' core.md)` 比 `=6`。
- L96 `RB_R6` 比 `§R6` in context-management → **保留**（inline tag `〔§R6〕` 仍在 context-management）。
- L108 awk split `^## §R[0-9]` → 改 split `^## (OBSERVE|IDENTIFY|PROPOSE|APPLY|TEST|RECORD|跨切)`；body 非 stub 檢查不變。
- L121 canonical wc -c 指令檢查 → 不動（core.md 保留該指令）。
- 同步改錯誤訊息字串。

### 3.2 mutation test（advisor 強制 — 證明 gate 能抓回歸）
```
# 1. 新結構下 gate 應 green
bash scripts/measure.sh --gate; echo "exit=$?"   # 期望 0
# 2. 故意刪一個 phase body → 應 red
（暫時掏空 ## TEST body）
bash scripts/measure.sh --gate; echo "exit=$?"   # 期望 1
# 3. 故意刪一個 phase header → 應 red
bash scripts/measure.sh --gate; echo "exit=$?"   # 期望 1
# 4. 還原
```

---

## 4. 多輪自檢清單（merge 前，advisor「自行多輪檢驗」）

| 輪 | 檢查 | 命令 | 通過條件 |
|----|------|------|---------|
| 1 | byte cap | `wc -c` 5 檔 | ≤19,000 |
| 2 | 六階段 header | `grep -cE '^## (OBSERVE\|...)'` | =6 |
| 3 | §R inline tag 存活 | `grep -oE '〔§R[0-9]+〕' core.md \| sort -u \| wc -l` | ≥11（R1-R12 除 R6）|
| 4 | §R6 in context-mgmt | `grep -c '§R6' context-management.md` | ≥1 |
| 5 | coverage checklist | 逐項對 successor | A/B/C/D/E/F/G/H 全 ✅ 或標 🔵 |
| 6 | gate green + mutation | §3.2 | exit 0 / 1 / 1 |
| 7 | healthcheck 全綠 | `bash scripts/healthcheck.sh` | FAIL=0 |
| 8 | refs 一致性 | healthcheck §15 | pass |
| 9 | 繁中無 silent fork | 人工掃 | 對使用者回應全繁中 |

---

## 5. commit + pr + merge（自主執行）

1. `git branch --show-current` 確認 = feature/workspace-canon-rewrite
2. `git add` 指定檔（5 主檔 + measure.sh + 2 報告）—— 不用 -A
3. commit 清晰 message
4. `git push -u origin`（失敗重試 2/4/8/16s）
5. `gh pr create`
6. merge 前最後跑一次 healthcheck（merge 不可逆）
7. squash merge + 確認 main GHA green

---

## 6. 回滾計劃

- gate 改壞 → `git revert` measure.sh commit（gate 與規則同 PR，revert gate 不影響規則內容）。
- 規則 eval 回歸 → 走 /autoload-evolution；≥5pp 回歸則整 PR revert。
- §R inline tag 漏 → grep `core §R` 找斷指針補 tag。
