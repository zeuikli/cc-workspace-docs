# Harness Ratchet Log

> 「每當 agent 犯一個錯誤，花時間工程化一個解決方案，使其永遠不再犯同樣的錯誤。」
> — Mitchell Hashimoto

每一行都應可追蹤到一次具體失敗。新增條目時：先記錄 → 再決定 Ratchet 層級 → 再實作。

---

## 欄位說明

| 欄位 | 說明 |
|------|------|
| 日期 | YYYY-MM-DD |
| 錯誤描述 | 具體失敗場景（不是抽象規則） |
| Ratchet 層級 | `hook`（code 層）/ `rule`（CLAUDE.md）/ `skill`（Known Gotchas）|
| 實作動作 | 做了什麼 |
| 驗證方式 | 如何確認問題不再發生 |
| 狀態 | ✅ 已實作 / ⏳ 待實作 / 📋 觀察中 |

---

## Ratchet 記錄

| 日期 | 錯誤描述 | Ratchet 層級 | 實作動作 | 驗證方式 | 狀態 |
|------|---------|------------|---------|---------|------|
| 2026-05-25 | README.md 有 4 個死連結（FRAMEWORK.md / REFERENCE.md / ANTHROPIC-ALIGNMENT.md 歸檔後未更新；eval-2026-05-15.md 從未存在）→ dead link checker 偵測到 | rule | 移除三個歸檔連結，替換為 KNOWLEDGE-MAP.md + SURVEY.md；eval-2026-05-15 → eval-2026-05-25；修正 "52 skills" → "18 skills" 誤值 | `python3 dead-link-check` → ✅ No dead links in key docs | ✅ |
| 2026-05-25 | healthcheck.sh Memory.md 閾值（200 行）與 core.md 規則（>150 → memory-compactor）不一致，150-200 行 gray zone 中規則說要委派但 healthcheck 說 OK | hook | healthcheck.sh 閾值 200 → 150，對齊 core.md | `bash scripts/healthcheck.sh` → Memory.md 191 行正確 WARN ✅；PASS 100 / WARN 3 / FAIL 0 | ✅ |
| 2026-05-25 | 18 個 skills 全部缺少 `review-by` frontmatter，無排程複查機制（harness-meta:add-skill 規範要求 90 天到期日）| skill（GOTCHAS） | 批次補全 `review-by: 2026-08-23`（+90d）；harness-meta 已有故跳過 | `head -8` 各 SKILL.md 確認 review-by 存在；healthcheck PASS 100 ✅ | ✅ |
| 2026-04-30 | pre-commit 門檻過高（50 files），日常小改動（1-7 files）繞過強制 /deep-review，self-evaluation bias 無攔截 | hook | `pre-commit-review.sh` FILE_THRESHOLD: 50→5，LINE_THRESHOLD: 500→100 | 下次 git commit 小改動時確認 exit 2 觸發 | ✅ |
| 2026-04-30 | 跨 session 長任務重入時，agent 需手動讀 Tasks.md 才能定位，容易方向漂移或 premature completion | hook | `session-init.sh` 加入 ACTIVE_TASK.md 自動讀取 + git log 最近 5 次 commit | 下次 session 啟動時確認輸出包含 `[Harness]` 區塊 | ✅ |
| 2026-04-30 | sandbox 缺失：bash 在 host 直接執行，deny-list 是 allow-by-default；`rm -rf` workspace 路徑未涵蓋在 block-dangerous 規則內 | hook | `block-dangerous.sh` 加入 workspace 路徑保護、`git clean -fd/fx`、`find . -delete` | 嘗試執行 `rm -rf ~/cc-workspace` 確認被阻斷 | ✅ |
| 2026-04-30 | MCP tool 覆蓋範圍對 project level 不透明；GitHub MCP 在 system level 配置，無法從 settings.json 稽核 | rule | `research/agent-harness/FRAMEWORK.md` 加入 MCP 說明；建立本 RATCHET.md 記錄觀察中狀態 | 每季 harness-eval 時重新確認 MCP 使用頻率 | 📋 |
| 2026-04-30 | 無量化基線，harness 改動有效與否只靠主觀感受，無 before/after 對比能力 | skill | 建立 `research/agent-harness/BENCHMARK.md`（5-task benchmark 設計） | 首次跑完 benchmark 並記錄 baseline 數據 | ✅ |
| 2026-04-30 | block-dangerous.sh 為 deny-list 策略，未知 pattern 可繞過 | hook | `block-dangerous.sh` 改為 allow-list：只放行明確安全 command prefix，其他全 block | 測試 `git status`(exit 0) + `mytool`(exit 2) + `bash -c`(exit 2) | ✅ |
| 2026-05-18 | HMF Full Run 3 top-3 缺口：D4 skill desc > 400 chars（3 skills） / D3 allow-list 24 entries 偏寬 / D1 claude-progress.json missing | 📋 | 觀察中 | 下次 eval 追蹤改善進度（可視條件調整優先序） | 📋 |
| 2026-05-19 | `harness-engineering.md` 缺 `tier: on-demand` frontmatter → measure.sh 將其計入 auto-load，顯示 5,617 tok（誤報）；實際 auto-load 為 3,583 tok | skill（GOTCHAS） | 加入 `---\ntier: on-demand\n---` frontmatter；measure.sh 依此 flag 跳過 on-demand 檔案 | measure.sh 輸出 `(on-demand, skipped)`；token 3,583 tok（後經大道至簡降至 3,467 tok ✅）| ✅ |
| 2026-05-19 | measure.sh IMPORTANT 計數 section 使用獨立 `grep -rn "IMPORTANT" CLAUDE.md .claude/rules/*.md`，未套用 on-demand filter → 計數 6（含 harness-engineering.md 的 3 個），誤判為注意力稀釋 | skill（GOTCHAS） | 將 IMPORTANT count section 改為 file-iteration loop，套用相同 `tier: on-demand` 跳過邏輯 | measure.sh 顯示 `IMPORTANT 出現次數: 2` ✅ | ✅ |
| 2026-05-19 | healthcheck.sh 在 0 個 on-demand ref 路徑時發出 WARN（「未發現 on-demand 觸發路徑」），但 CLAUDE.md 移除載入策略節後本就無 ref 路徑，0 refs = 無待驗證項目，非異常 | hook | 將 WARN 改為 PASS：`pass "on-demand 觸發路徑：無引用需驗證"` | healthcheck.sh 顯示 PASS 94 / WARN 2 / FAIL 0 ✅（WARN 2 為 MCP system level，預期行為）| ✅ |
| 2026-05-19 | auto-load token 3,583 tok 超 soft cap 3,500（+83 tok）；根因：core.md R1 補 open questions +84 tok，且 CLAUDE.md/rules 有 TYPE C/D 可安全移除的背景說明 | rule | FRAMEWORK-FIRST 大道至簡 pass：移除 TYPE C/D 內容（CLAUDE.md 載入策略節 + harness-engineering.md 待補強清單等）→ 3,583 → 3,467 tok | measure.sh 合計 ≈3,467 tok ✅（< 3,500 soft cap）| ✅ |
| 2026-05-25 | `healthcheck.sh` 使用 `import yaml`（pyyaml 非標準庫），在缺少 pyyaml 的環境下全部 FAIL（32 items）；eval-2026-05-20 記錄 PASS 94 的環境有 pyyaml，但新環境不保證 | hook | 將 `import yaml` + `yaml.safe_load()` 改為純 `re`-based frontmatter 解析（`re.match(r'^(\w[\w-]*)\s*:\s*(.*)', line)`），消除外部依賴 | `bash scripts/healthcheck.sh` 顯示 PASS 100 / WARN 3 / FAIL 0 ✅ | ✅ |
| 2026-05-25 | `PostToolUseFailure` 和 `Notification` 是 Claude Code 官方 hook 事件（upstream v2.1.77 確認），但 settings.json 缺少這兩個事件覆蓋 — 工具失敗無法記錄，通知事件無可觀測性 | hook | 新增 `failure-log.sh`（PostToolUseFailure → command-log.jsonl event_type: tool_failure）+ `notification-log.sh`（Notification → session-stats.log）；settings.json 新增對應 hook 區塊 | `python3 -c "import json; d=json.load(open('.claude/settings.json')); print(list(d['hooks'].keys()))"` 顯示含 PostToolUseFailure + Notification ✅ | ✅ |
| 2026-05-25 | AUDIT-2026-05-01 P1 記錄 `auto-push.sh` 繞過 healthcheck gate；本次驗證 `auto-push.sh` 不存在、settings.json Stop hook 僅有 session-stop.sh + memory-sync.sh，finding 為歷史遺留無法重現 | rule | 標記為 CLOSED：finding 失效（腳本已刪除）；`memory-sync.sh` 有互斥鎖 + 僅 commit Memory.md，無 healthcheck 繞道風險 | `ls .claude/hooks/auto-push.sh` → 不存在；`grep auto-push .claude/` → no references ✅ | ✅ |
| 2026-05-25 | `pre-compact.sh` 無 exit 2 阻斷模式：大量未提交變更（>100 行）時 compact 無保護，進行中架構決策可能被覆蓋；此 G3 gap 自 cross-validation-report（2026-05-15）起記錄 10 天仍未修 | hook | `pre-compact.sh` 加入 `git diff HEAD --numstat` 計算未提交行數，>100 行則 `exit 2` 阻斷 + 寫 compact-events.log | `grep "exit 2" .claude/hooks/pre-compact.sh` → 命中；實際 workspace 11,435 行未提交，觸發阻斷 ✅（commit eba4a785）| ✅ |
| 2026-05-25 | 建立新檔前未查重：任務要求建立 `harness-model-fit.json` 與 `RATCHET.md`，直接 Write 新建，未先 `find` 確認，導致在 `.claude/` 建立兩個重複且劣化版本（正本分別在根目錄與 `research/agent-harness/`，含真實 audit history；副本 eval scores 為假設值）| rule | 刪除兩個副本（commit 59557228、36c712fe）；防範規則：建立新檔前 YOU MUST `find . -name "<filename>"` 確認不存在，已存在則更新正本 | `find . -name "harness-model-fit.json" \| wc -l` → 1；`find . -name "RATCHET.md" \| wc -l` → 1 ✅ | ✅ |
| 2026-05-25 | `research/reports/` 積累 15 個已落地或過期報告（最早至 2026-05-12），無定期清理機制；README 與實際檔案長期失同步（列了 33 份報告但已刪/過期者混入）| skill（routine） | 手動盤點刪除 15 個（已落地 8、過期重複 3、中間產物 2、無關 2）；README 重構為 4 主題區；建立 monthly-reports-cleanup remote routine（trig_015q9m1NVU2UdsjEKq6Y1YX9，每月 1 日 09:00 台北）| `ls research/reports/*.md \| wc -l` → 19 ✅；routine 首次執行：2026-06-01 ✅ | ✅ |
| 2026-05-25 | auto-load 4 個規則檔案內部排序未依 NLAH 優化：IMPORTANT 行為規則不一定在各檔頂端；context-management.md 和 output-discipline.md 在系統提示的相對 MIDDLE 位置，若檔案內部重要規則也不在頂端，衰減效應疊加。Token 餘裕 7%（4,180/4,500），後續新增空間有限 | rule | **✅ NLAH-Rule-Ordering Audit**（2026-05-26）：4 檔各做 TYPE A 前置重排（廣義：含 IMPORTANT/YOU MUST/禁止/不得/必須）。HEAD/TAIL/MIDDLE 分配：core.md HEAD=驗證與品質(6 hits) TAIL=Git工作流程(2 hits) MIDDLE=9節；context-management.md HEAD=Prompt Caching(禁止) TAIL=監控 MIDDLE=Compact hint；output-discipline.md 已最優無需修改；subagent-strategy.md HEAD=Agent Input Security(YOU MUST) TAIL=Background Agent規範(不得) MIDDLE=6節。criterion #3 按 Step1 廣義 TYPE A 解讀（literal IMPORTANT/YOU MUST 在 context-management.md/output-discipline.md 為 0，N/A）；frontmatter 驗證 N/A（各檔無 frontmatter）。K×M ✅ (IMPORTANT\|YOU MUST counts: 4/0/0/1 → 4/0/0/1; sections: 11/3/3/8 → 11/3/3/8)；auto-load 3,292 tok ✅（目標 ≤ 3,800）；IMPORTANT 出現 3 次 ✅；`bash scripts/measure.sh` PASS ✅ | routine `trig_NLAH_audit`（待建）| ✅ |
| 2026-05-25 | 研究報告 Re-check 節記錄的新發現（Background Agents 規範、Routines 第四原語、NLAH -95% token 原則、`/goal` R4 工具化）未同步進 auto-load rules；G3 cross-validation gap 持續 10 天也未被追蹤觸發修復動作 | rule | 更新 `subagent-strategy.md`（Background Agents 前景/背景決策表 + Routines 四原語表）、`core.md`（`/goal` R4 工具化）、`context-management.md`（NLAH 原則）| `grep -n "Routines\|Background Agent\|NLAH\|/goal" .claude/rules/*.md` → 各有命中 ✅（commit 30c5d432）| ✅ |
| 2026-05-25 | `healthcheck.sh` agents/*.md 迴圈把 `agents/README.md`（索引檔）當 agent 定義掃描 → 缺 YAML frontmatter → FAIL 1；同類問題 measure.sh 已正確跳過 rules/README.md，但 healthcheck.sh 未同步此邏輯 | hook | `healthcheck.sh` agents 迴圈加 `[[ "$(basename "$md")" == "README.md" ]] && continue`（同 measure.sh 做法）| `bash scripts/healthcheck.sh` → PASS 101 / WARN 2 / FAIL 0 ✅ | ✅ |

---

## Ratchet 升格決策樹

```
發現錯誤
  │
  ├─ 錯誤頻率 > 1次/週？
  │    ├─ 是 → hook（code 層，直接砍掉分布中的該行為）
  │    └─ 否 ↓
  │
  ├─ 錯誤與特定 skill 相關？
  │    ├─ 是 → skill Known Gotchas
  │    └─ 否 ↓
  │
  └─ 一般性錯誤
       └─ CLAUDE.md rule
            └─ 觀察 2 週仍反覆 → 升格到 hook
```

---

## Known Gotchas（跨 skill 彙整）

從各 skill Known Gotchas 提取的高頻跨域問題：

| 來源 Skill | 問題 | 影響 |
|-----------|------|------|
| harness-eval | `.claude/settings.json` hooks 可能被 global settings 覆蓋 | 以為 hook 有效但實際被覆蓋 |
| harness-eval | Auto Memory 在 `~/.claude/projects/`，非 repo 內 | bash path 需正確 |
| harness-eval | MCP tool descriptions 佔 context，越多 server context rot 越快 | 不要過度安裝 MCP |
| context-management | Compact 在 context rot 最嚴重時觸發，模型最不聰明 | 主動 `/compact` 優於自動 compact |
| subagent-strategy | 「Sub-agent spawn 能力」≠「實際使用 sub-agent」 | 需看 CLAUDE.md 委派規則 |

---

---

## harness-audit 2026-05-14 — Gap 結案紀錄

### G2 — Global Stop Hook 重疊（2026-05-14 關閉：false positive）

**原始診斷**：`~/.claude/settings.json` 與 `.claude/settings.json` 各有 1 個 Stop hook → 懷疑重複觸發。

**實際查驗結果**：
- Global Stop：`stop-hook-git-check.sh` — 檢查未提交變更 / 未推送 commit（harness 基礎設施）
- Project Stop：`session-stop.sh`（session stats）+ `memory-sync.sh`（MEMORY.md sync）

兩者職責完全不同，均需執行。Claude Code 多 scope hooks 採並列執行（concatenate），非覆蓋。

**結論**：G2 為 audit 框架誤報，無需任何修正。HARNESS-CARD.md 中「2 Stop hooks」記錄應更新為說明其互補關係。

---

## 下次 harness-eval 應確認的項目

- [ ] pre-commit 門檻調整後，實際觸發率是否提升
- [ ] session-init 的 ACTIVE_TASK.md 輸出是否清楚（不超過 30 行）
- [ ] block-dangerous.sh 新規則是否有誤傷正常操作
- [ ] MCP 使用頻率初步稽核（check command-log.txt）
- [x] BENCHMARK.md 首次 baseline 記錄（87.5%）、Ratchet 後重評估（93.75%）
- [x] G1 token budget 修正（4562→3508 tok，-23%）
- [x] G2 false positive 關閉（global + project Stop hooks 互補）
- [ ] G3 IMPORTANT 數量 5→3 後，實際行為是否維持（下次 eval 確認）

---

## Ratchet #R2026-05-14c — Memory Clean + Harness Audit

**執行日期**：2026-05-14
**模式**：full + ratchet
**觸發原因**：memory 目錄整理後 + 用戶要求全 workspace 文件同步

### Before

| 指標 | 數值 |
|------|------|
| CAR Score | 13.0/14（HARNESS-CARD 舊記錄）|
| auto-load tokens | 3,501 |
| PASS/WARN/FAIL | 118/3/0 |

### 發現

| ID | 類型 | 描述 |
|----|------|------|
| R2026-05-14c-1 | ❌ 斷連結 | MEMORY.md:33 保留已刪除的 harness_audit_2026-05-13.md 連結（memory 整理時引入）|
| R2026-05-14c-2 | ⚠️ 數據過時 | HARNESS-CARD.md "42 skills" → 應為 13；score 13.0/14 → 應為 13.5/14 |
| R2026-05-14c-3 | 📋 觀察中 | R3 token budget：3,501 = 3,500 + 1 tok（borderline；measure.sh 持續監控）|

### 修正（已執行）

1. `memory/MEMORY.md:33`：移除斷連結，改為純文字說明
2. `research/agent-harness/HARNESS-CARD.md`：skills 42→13；score 13.0→13.5/14；補 audit 日期 comment

### After

| 指標 | 數值 |
|------|------|
| CAR Score | **13.5/14 = 96.4%** 🟢 |
| auto-load tokens | 3,501（⚠️ borderline，持續觀察）|
| PASS/WARN/FAIL | **92/2/0**（-26 PASS = research/* 目錄刪除後檔案減少，預期）|

### 升格判定

- R2026-05-14c-1：✅ 升格（斷連結已修復，source-verify 可確認）
- R2026-05-14c-2：✅ 升格（數據更新，有 before/after 量化）
- R2026-05-14c-3：📋 觀察中（無量化改善，不升格）

---

## R2026-05-23 — P0 `tier: on-demand` 非官方欄位導致意外自動載入

### 失敗場景

`harness-engineering.md` 使用 `tier: on-demand` frontmatter 標記，開發者假設此欄位可阻止自動載入。但 Claude Code 只識別官方 `paths:` frontmatter；`tier` 為自定義欄位，完全被忽略。結果：harness-engineering.md（~1,400-1,700 tok）每次 session 無條件自動載入，實際 auto-load 合計超出 CAR hard cap 4,500 tok（前次 measure.sh 未偵測到此問題，因為 measure.sh 本身也用 `tier: on-demand` 作為跳過條件）。

**官方文件原文**：*"Rules without a paths field are loaded unconditionally and apply to all files."*

### Before

| 指標 | 數值 |
|------|------|
| auto-load tokens | ~4,144-5,183 tok（含 harness-engineering.md）|
| measure.sh 顯示 | ~3,467 tok（因 measure.sh 的跳過邏輯同樣依賴 `tier: on-demand`，誤以為已排除）|
| harness-engineering.md 載入狀態 | ❌ 每次 session 自動載入（應為按需）|

### 修正（已執行 2026-05-23）

1. **P0**：將 `.claude/rules/harness-engineering.md` 遷移至 `.claude/skills/harness-meta/references/harness-engineering-REFERENCE.md`，並刪除原 rules 檔案。官方機制：skill 只在明確 invoke 或 Claude 判斷相關時載入。
2. **P1**：移除 4 個 auto-load rules 檔案中的 `[FF]`/`[FB]` 標記（40 個，~40 tok）。
3. **measure.sh 修正**：將跳過邏輯從 `grep -q '^tier: on-demand'` 改為 `awk` 偵測 YAML frontmatter 中的 `paths:` 欄位（符合官方規範）。
4. **core.md 更新**：`Framework Integrity` 的導航引用從 `harness-engineering.md` 更新為 `/harness-meta`（TYPE D 導航行）。

### After

| 指標 | 數值 |
|------|------|
| auto-load tokens | **3,412 tok** ✅（CAR hard cap 4,500，餘裕 24%）|
| measure.sh 顯示 | 3,412 tok（現在準確反映實際 auto-load）|
| harness-engineering.md 載入狀態 | ✅ 按需載入（via `/harness-meta` skill）|
| healthcheck | PASS 94 / WARN 2 / FAIL 0 |

### 升格判定

- R2026-05-23-1（tier: on-demand 誤用）：✅ 升格（P0 已遷移至 skill；measure.sh 已修正；有 before/after 量化）
- R2026-05-23-2（measure.sh 跳過邏輯錯誤）：✅ 升格（已修正為 paths: frontmatter 偵測）
