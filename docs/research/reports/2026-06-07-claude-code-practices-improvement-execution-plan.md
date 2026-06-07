---
title: "Claude Code 社群實踐 — Workspace 改善與執行計劃書"
author: "Opus 4.8 (draft) → Sonnet 4.6 (revision)"
date: 2026-06-07
status: 部分執行（2026-06-07，見 §15 執行狀態）
branch: feature/claudecode-improvement-plan
sources: ["2026-06-07-claude-code-community-practices-report.md (32 篇社群實踐, PR", "2026-06-07-claude-code-deep-practices-v2.md (盲點補足 v2, PR", 2026-06-07-session-insights.md, 2026-06-07-session-insights-v2.md]
type: execution-plan
---

# Claude Code 社群實踐 — Workspace 改善與執行計劃書

> **使用方式**：本計劃書已完整查驗原始來源 + 比對 workspace 現況 + 驗證官方 schema。每項標註「現況」「證據可信度」「建議動作」「驗收條件」「風險」。你逐項核准後執行；破壞性 / schema 未定項目已標 GATE。
> **重要校準**：報告原始的 P0/P1/P2 是「社群通用排序」，非「你的 workspace 排序」。本計劃書依**實測現況**重排優先序——多個原 P-tag 在你這裡已是 no-op 或不適用，已降級；真正缺口已升級。
> **撰寫流程**：Opus 4.8 起草 → Sonnet 4.6 修訂（符合你指定的雙模型流程）。

---

## 0. 執行摘要 — 重排後的真實優先序

| 重排 | 項目 | 原 tag | 現況一句話 | 動作類型 |
|------|------|--------|-----------|---------|
| **🔴 先驗證** | autoCompactAt 設定 | P0 | **schema 無此 key**；真實機制是 env var `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`（未文件化+有 bug）→ 預設走人為紀律 | A1 紀律 / A2 試 env var |
| **🟢 真缺口** | STATUS.md / 跨 session handoff | P1 | 你**沒有** STATUS.md，但已有 `schemas/progress.schema.json` 未啟用 | 採用既有 schema |
| **🟢 真缺口** | Session length 紀律 | P1 | 無「每 N 任務強制 /clear」觸發 | 加軟性紀律 |
| **🟢 真缺口** | Skill description 更新 | P2 | 27 skills，已有 UserPromptSubmit hook，可增強 | 增強既有 |
| **🟡 部分成立** | Centralized kill-switch / 3-tier | P1 | 你是 `bypassPermissions` + 已有 `block-dangerous.sh` 分層 | 評估 + 補強 |
| **🟡 部分成立** | Hook Narrowness Principle | P1 | `block-dangerous.sh` 是 376 行 monolith（違反原則）| 評估重構 |
| **⚪ 近 no-op** | Hook exit code 稽核 | P1 | **僅 1 個 exit 1**，在 PostCompact/Stop，非阻斷、正確 | 確認即可 |
| **⚪ 近 no-op** | MEMORY.md 200 行 cap | P2 | **87/200 行**，遠未觸頂 | 加自動 gate（預防）|
| **🔵 條件式** | .claude/tasks/ JSON persistence | P2 | 已有 progress.schema.json，與 STATUS.md 重疊 | 合併到 handoff |
| **🔵 條件式** | eval harness first | P2 | 已有 eval-designer skill + healthcheck | 流程紀律化 |
| **🔵 條件式** | AST graph navigation | P2 | workspace 非 code-heavy（研究型）| 不適用，存檔 |

<!-- SONNET-FLAG: §0 表「Centralized kill-switch」標 🟡 是預設姿態；§5-E1 與 §12.1 條件式升級至 P0（若有 clone 外部 repo 習慣）。條件未成立時不矛盾，成立時應對照 §5 重評優先序。 -->

**一句話結論**：你標的 11 項中，**3 項是真缺口值得做**（STATUS.md handoff、session 紀律、skill description），**2 項近 no-op**（exit code、MEMORY cap——確認比修改重要），**1 項報告建議直接無效**（autoCompactAt schema 不存在），**其餘為條件式 / 不適用**。

---

## 1. 🔴 autoCompactAt 設定（原 P0）— 報告 key 不存在；真實機制是 env var（有 bug 警告）

> **深度研究後更新（2026-06-07）**：原判「報告建議無效」成立，但補上**真實替代機制**。Claude Code **確實有 built-in auto-compaction**，且**確實有一個可調閾值的機制**——只是不是報告寫的那個 key，而是一個**官方未文件化、且有 reliability bug** 的 env var。以下分三層：機制真相 → 真實 key → 落地建議。

### 1.1 機制真相（官方確認）
- **Built-in auto-compaction 存在**：context 接近上限時自動摘要舊內容並續跑。
- **預設觸發點**：「可用 input tokens − 13,000」的固定 buffer（非乾淨百分比）。200K 模型約落在 **83–95% 使用率**才觸發。來源：[anthropics/claude-code#12004](https://github.com/anthropics/claude-code/issues/12004)（原始碼確認 `nx1 = 13000`）。
- **不可由 `settings.json` 設定**：schema 無 `autoCompactAt` / `tokenBudget` / `autoCompact` / `autoCompactThreshold` / `sessionLimit` / `warningThreshold`。三個要求加此 key 的 feature request（[#28728](https://github.com/anthropics/claude-code/issues/28728) / [#41818](https://github.com/anthropics/claude-code/issues/41818) / [#25679](https://github.com/anthropics/claude-code/issues/25679)）**全部 closed as not planned**。

### 1.2 報告 key 為何無效（已 WebFetch 官方 schema 確認）
- community-practices [來源宣稱, Branch8]：`autoCompactAt: 60%`（flat）；deep-practices-v2 [個人宣稱, @zodchiii]：`tokenBudget.autoCompactAt: 0.6`（nested）。**兩者互相矛盾**。
- 官方 schema（`https://www.schemastore.org/claude-code-settings.json`，即你 settings.json `$schema` 宣告者）：`autoCompactAt` / `tokenBudget` / `sessionLimit` / `dailyLimit` / `warningThreshold` / `thinkingTokenLimit` → **全部 DOES NOT EXIST**。
- **myth 來源**（深研發現）：社群 guide / LLM 生成的 config 片段，很可能**把上述 feature request 提案的 key 名當成已實作的 key 抄出來**（#28728 提案 `autoCompactThreshold: 0.85`、#41818 提案 `compactAtPercent: 66`）。無任何證據 `autoCompactAt` 曾在任何版本真實存在。

### 1.3 真實可調閾值的機制（唯一一條路，但有 bug 警告）
- **`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`**（shell env var，非 settings.json）：把 auto-compact 觸發設為百分比（1–100）。
  - 原始碼確認存在（[#12004](https://github.com/anthropics/claude-code/issues/12004)）；只能**調低**不能調高（Math.min clamp，[#31806](https://github.com/anthropics/claude-code/issues/31806)）→ 設 60 在 clamp 下**有效方向**。
  - **官方未文件化**（[#20244](https://github.com/anthropics/claude-code/issues/20244)）。
  - **⚠️ reliability bug**：v2.1.79（[#36381](https://github.com/anthropics/claude-code/issues/36381)）、v2.1.90（[#42394](https://github.com/anthropics/claude-code/issues/42394)）回報**被忽略**；放進 `settings.json` 的 `env` block **靜默無效**（[#63186](https://github.com/anthropics/claude-code/issues/63186)）→ 必須放 shell rc。
  - **你的版本 v2.1.168 是否生效：UNVERIFIED**（須實測，見驗收）。
  - **你的 session 現況**：`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` = unset（已查）。
- **`claude config set -g autoCompactEnabled false`**（寫入 `~/.claude.json`，非 settings.json）：全域關閉 auto-compact。**reliability 有爭議**（[#38483](https://github.com/anthropics/claude-code/issues/38483) 回報被忽略，closed not planned）。

### 1.4 建議動作（決策樹）
- **A1（推薦預設）— 人為紀律 + 既有 hooks，不依賴 env var**：
  - 你 `context-management.md` 已有「行為信號 > 數字閾值」compact 紀律（70% 一般 / 30–35% 長 agentic）+ `/compact <hint>` + PreCompact hook（`pre-compact.sh`）。**這層已運作且不受上述 bug 影響**——是最可靠的「60% 意圖」實現方式（人主動在 60% 下 `/compact`）。
  - 零變更、零 schema 風險、零 env-var bug 暴露。
- **A2（想要自動觸發，願承擔 UNVERIFIED 風險）— 試 env var**：
  ```bash
  # 加進 ~/.zshrc（不是 settings.json，後者靜默無效）；重啟 session 才生效
  export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60
  ```
  - **必須實測驗證**（見驗收）；若 v2.1.168 仍有 #42394 的 bug 則無效，退回 A1。
- **A3（成本控制，與閾值無關）— schema-confirmed**：
  - `model`（schema 存在）：選成本較低 model 結構性降成本。
  - `autoMemoryEnabled: true`（你**已開**）：offload 記憶到 MEMORY.md，間接減 context 壓力。
  - `cleanupPeriodDays`（schema 存在）：控 transcript 保留天數（與 compact 閾值**無關**，別誤用為成本上限）。
  - 成本監控用 `ccusage` / `/usage`，非 config 硬上限。
- **A4（不做）**：不寫 `autoCompactAt` 進 settings.json（schema 無效，validator 標紅或靜默忽略）。

### 驗收條件
- A1：`python3 -m json.tool .claude/settings.json` 通過，未引入 schema 無效 key。
- A2（若採）：export 後**重啟 session**，跑長對話觀察 compaction 是否在 **<70% context** 觸發（觸發 = 生效；到 83%+ 才觸發 = 仍 bug，退 A1）。`echo $CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` 應回 `60`。

### 風險
- **A1 零風險**（純人為紀律 + 既有機制）。
- **A2 中風險**：env var UNVERIFIED on v2.1.168，可能靜默無效（假安全感）；故列為「願承擔風險才試」，預設走 A1。

### 來源
官方：[Hooks](https://code.claude.com/docs/en/hooks) · [Settings](https://code.claude.com/docs/en/settings) · [SchemaStore](https://www.schemastore.org/claude-code-settings.json)。Issues：#12004（13K buffer）· #20244（env 未文件化）· #31806（只能調低）· #36381 / #42394（被忽略 bug）· #63186（settings.json env block 無效）· #38483（autoCompactEnabled 被忽略）· #28728 / #41818 / #25679（feature request 全 not planned）。

---

## 2. 🟢 STATUS.md / 跨 session handoff（原 P1）— 真缺口，但用既有 schema

### 現況
- `ls STATUS.md` → **不存在**。
- 但 `schemas/progress.schema.json` **已存在**（Justin Young 2025 pattern，session-stop.sh 會 auto-update `updated_at`），且 SessionStart hook 已偵測「無 claude-progress.json」並提示建立。
- → 這不是「設計新 handoff 格式」，而是「**啟用既有但未使用的 schema**」。

### 證據與可信度
- community-practices [來源宣稱, Eva Khmelinskaya]：CLAUDE.md 在 90+ 分鐘 session 後被 compact 丟失 → STATUS.md 修復。格式：`{task, phase, last_checkpoint, next_action, blockers}`（lines 151–174）。
- deep-practices-v2 [失敗案例類型學]：同一「instruction dilution」現象（line 104）。
- **比對**：`progress.schema.json` 已含 `next_action`（"prevents premature completion"）、`sessions`、`current_step`、`status` — **覆蓋報告建議的 STATUS.md 欄位且更完整**。報告的 STATUS.md 是 progress.schema 的子集。

### 建議動作
- **B1（推薦）**：採用 `progress.schema.json` 取代另造 STATUS.md。長任務（overnight / 跨 session）開工時建 `claude-progress.json`（SessionStart hook 已會提示）。
- **B2**：在 `core.md`「長期記憶回路」段加 1 行：「跨 session / overnight 任務開工 → 建 `claude-progress.json`（schema: `schemas/progress.schema.json`）」。**注意 auto-load byte 預算**（現 18,726 / cap 19,000，餘 274）——這 1 行約 +120 B，可容；若超則放 `refs/` 加指針。
- **B3（不做）**：不另造 STATUS.md（與 progress.json 重複 = 維護債）。

### 驗收條件
- `python3 -c "import json,jsonschema; ..."` 或簡易 `python3 -m json.tool claude-progress.json` 對一個樣本檔通過。
- session-stop.sh 對該檔的 `updated_at` auto-update 實測生效（建檔後跑一次 session 結束驗證）。

### 風險
- **低**。僅新增使用慣例 + ≤1 行 auto-load。byte 預算需先量測。

---

## 3. 🟢 Session length 紀律（原 P1）— 真缺口，加軟性觸發

### 現況
- `context-management.md` 已有 compact 觸發（行為信號 + 70%/30% 閾值），但**無「每 N 任務 /clear」計數觸發**。
- core.md 有「每重要步驟 checkpoint」，但 checkpoint ≠ session 邊界紀律。

### 證據與可信度
- community-practices [來源宣稱, Jamie Cole 30 天回顧]：47 任務 25% 放棄率（12/47）；「每 5 任務 1 regression」；"One task, one session"（lines 329–345）。
- deep-practices-v2 [個人宣稱, Sean Moran ★★★☆☆]：2026 範式轉移「long session > frequent /clear」（lines 26–37）——**與 Jamie Cole 方向相反**。
- **矛盾標記**：Jamie Cole 主張短 session / 勤 /clear；Sean Moran 主張 long session 已從「脆弱」變「資產」。兩者皆 [個人宣稱]，無學術背書。**不可同時採信**（core.md 浮現矛盾紀律）。
- 「30–60 min session」門檻：兩份報告 researcher 均確認**非 Jamie Cole 建議**，而是 Eva Khmelinskaya 對 overnight agent 的 session cap（context-dependent）。

### 建議動作
- **C1（推薦，折衷）**：不採二元立場。加**軟性自評觸發**而非硬性 /clear：「連續完成 5 個獨立任務後，主動自評 context drift（一句 checkpoint：是否出現迷失/重複/規則遺忘）→ 決定 compact 或 continue」。對應 Jamie Cole 的數據點，但保留 Sean Moran 的 long-session 彈性。
- **C2**：寫入 `context-management.md`「Compact 觸發」段，作為「行為信號」的具體化（第 5 任務 = 一個主動檢查點）。約 +100 B。
- **C3（不做）**：不設「硬性每 5 任務強制 /clear」——與你 long-session 研究工作流衝突，且 Sean Moran 反證。

### 驗收條件
- 規則寫入後，下次連續任務 session 實測出現第 5 任務自評 checkpoint。
- auto-load byte 量測 ≤ cap。

### 風險
- **低**。軟性紀律，不改 harness 機制。矛盾已明示（C2 寫入時加 `TODO(conflict): chose soft-5-task-check over hard /clear (Jamie Cole) per Sean Moran long-session evidence; revisit at 2026-Q3` 在 `context-management.md` Compact 觸發段）。

---

## 4. 🟢 Skill description 更新（原 P2）— 增強既有

### 現況
- 27 skills，多數已有 `Do NOT use for:`（抽查 RESOLVER 與本 session 注入的 skill list 確認大部分已遵循該 pattern）。
- 已有 UserPromptSubmit hook（`user-prompt-submit.sh`）注入 skill 提醒。

### 證據與可信度
- deep-practices-v2 [個人宣稱, source-7]：自然觸發 ~20% → UserPromptSubmit hook 注入 → ~84%（lines 315–338）。**注意**：researcher 確認「Alex Opalic」此名 **不在 deep-v2 檔內**（source-7 未具名）；community-practices 也**無此 20%/84% 數字**。→ 數字來源單一、未具名、[個人宣稱]。
- community-practices [來源宣稱, AgentStack/Mayur Panchal]：banlist > stylelist；description 要「pushy」；格式 `Use when... Do NOT use for: A, B`（lines 393–412）。

### 建議動作
- **D1（推薦）**：`grep -L "Do NOT use for\|Do not use" .claude/skills/*/SKILL.md` → 對回傳的 skill 逐一補齊該欄位。低成本、低風險。
- **D2（可選）**：你的 UserPromptSubmit hook 已注入提醒，但**未實作 MANDATORY SKILL ACTIVATION 評估邏輯**（source-7 的 84% 來自此）。可評估是否值得——但 84% 數字單一未具名，**先小規模驗證**（觀察現有 hook 的觸發率）再決定是否加邏輯。
- **D3（不做）**：不照搬 source-7 的 TS hook（`user-prompt-skill-eval.ts`）——你已有 bash hook，雙軌會衝突。

### 驗收條件
- `grep -L "Do NOT use for\|Do not use" .claude/skills/*/SKILL.md` 回傳空（或剩餘清單已逐一確認豁免）。

### 風險
- **低**（D1）。D2 涉 hook 改動 → 走 Hook Narrowness（見 §6）+ fixture 測試。

---

## 5. 🟡 Centralized kill-switch / 3-tier hooks（原 P1）— 部分成立，重要安全

### 現況（這裡有真實安全暴露）
- `.claude/settings.json` → `"defaultMode": "bypassPermissions"`。
- 已有分層 deny（`rm -rf /`、`curl|bash`、`chmod 777`）+ `block-dangerous.sh`（3 個 exit 2 阻斷點）+ `branch-isolation-guard.sh` + `protect-sensitive-files.sh`。
- → 有「單層 hooks」雛形，但**無 centralized kill-switch**，且 `bypassPermissions` 是高暴露姿態。

### 證據與可信度
- deep-practices-v2 [安全研究機構, Check Point Research ★★★★★]：
  - **CVE-2025-59536 (CVSS 8.7)**：惡意 repo → `.claude/settings.json` 的 hooks 在 **trust dialog 出現前**執行 → RCE（lines 591–593）。
  - **CVE-2026-21852 (CVSS 5.3)**：`.claude/settings.json` 覆寫 `ANTHROPIC_BASE_URL` → API key 在 trust dialog 前被攔截（lines 594–597）。
  - 第三項是「50 subcommand 上限 bypass」，**非** researcher A 誤記的「CVE-2025-54794」（已查驗澄清）。
- [學術, arXiv 2604.14228 ★★★★★]：CLAUDE.md = user context（~70% 機率遵從），hooks = 100% 確定性；安全規則放 CLAUDE.md 是設計錯誤（lines 58–63）。
- **直接關聯你的姿態**：你的 `bypassPermissions` 正是 CVE-2025-59536 描述的暴露面——clone 惡意 repo 時其 `.claude/settings.json` hooks 可在你 trust 前執行。

### 建議動作
- **E1（推薦，先評估）**：稽核你 clone 外部 repo 的習慣——是否曾在未審查 `.claude/settings.json` 下開 session？若是，**這是 P0 級安全項**（升級）。檢查：你的 workspace 是否只在自己的 trusted repo 開 session（是 → 暴露低）。
- **E2**：考慮 `bypassPermissions` → 至少對「clone 的外部 repo」改用 `default`/`acceptEdits` 模式（per-project settings）。你自己的 cc-workspace 可維持 bypass（trusted）。
- **E3（kill-switch）**：3-tier 是給「組織管理多開發者」的；你是單人 workspace → centralized remote kill-switch **過度工程**。替代：把安全關鍵規則確認都在 hooks（已大致如此）而非 CLAUDE.md（符合 arXiv 發現）。
- **E4**：稽核 `.claude/settings.json` 的 hooks 是否全指向 repo 內受信任腳本（`grep command .claude/settings.json` → 全部 `$CLAUDE_PROJECT_DIR/.claude/hooks/*` = 安全）。

### 驗收條件
- 列出所有 hook command 來源，確認 0 個指向外部 / 非 repo 腳本。
- 決策記錄：bypassPermissions 維持 or 收緊（附理由）。

### 風險
- **E2 中風險**（改 permission mode 影響日常流暢度）→ 需你決定 trade-off。E4 零風險（只讀稽核）。

---

## 6. 🟡 Hook Narrowness Principle（原 P1）— 部分成立，評估重構

### 現況
- `block-dangerous.sh` = **376 行 monolith**（34 個 exit 0 + 3 個 exit 2），單檔處理多規則 → **違反 Narrowness Principle**。
- 其他 hooks 多數單一職責（branch-isolation / protect-sensitive / memory-sync 各管一事）。

### 證據與可信度
- community-practices [來源宣稱, Jangwook Kim]：一 hook 一規則；anti-pattern = if/elif merge 10 規則，單一 regex error 汙染全部（lines 69–88）。
- deep-practices-v2 [設計原則, hooks-security-gates-narrowness]：① 一 hook 一規則 ↔ 一 fixture pair；② safe/dangerous payload 在 Claude Code 外測試；③ `jq` 結構化解析 > regex（lines 289–296）。

### 建議動作
- **F1（推薦，評估而非立即拆）**：`block-dangerous.sh` 376 行雖違反原則，但**已運作且有 3 層設計**（line 18 註解：allowlist → 不在清單 exit 2）。拆分 = 大改動、有回歸風險。先評估「拆分收益 vs 風險」：單人 workspace、該檔穩定 → **可暫不拆**，但**必須補 fixture 測試**（最高價值動作）。
- **F2（推薦，高價值低風險）**：為 `block-dangerous.sh` 建 fixture pair 測試（safe payload 應 exit 0 / dangerous payload 應 exit 2），放 `tests/hooks/`。這直接實現 Narrowness 原則 ②，且**不動現有邏輯**。
- **F3（可選）**：新增 hook 時遵循「一 hook 一規則」+ `jq` 解析（原則 ①③），但**不回頭重構** block-dangerous（Rule of proportionality）。

### 驗收條件
- `tests/hooks/test-block-dangerous.sh` 存在，涵蓋 ≥3 safe + ≥3 dangerous fixture，全綠。
- 測試能在 block 邏輯被改壞時失敗（驗意圖，非驗實作）。

### 風險
- **F2 低風險**（純加測試）。F1 拆分若做 = 中高風險，故建議暫緩。

---

## 7. ⚪ Hook exit code 稽核（原 P1）— 近 no-op，確認即可

### 現況（已實測）
- `grep -rn "exit 1" .claude/hooks/` → **僅 1 個**：`memory-sync.sh:44`。
- 該 `exit 1` 在 **PostCompact / Stop** 事件（remote URL mismatch → abort sync）。
- exit code 直方圖：所有阻斷意圖都正確用 `exit 2`（block-dangerous ×3、pre-commit-review ×3、protect-sensitive ×2、branch-isolation ×1、session-init ×8、pre-compact ×2、sdd-cache-pre ×1）。

### 證據與可信度
- 兩份報告 [官方語義]：exit 1 = 非阻斷（Unix convention）；exit 2 = Claude Code 阻斷信號。
- **比對你的 hooks**：唯一的 exit 1 在 PostCompact/Stop——這兩個事件 exit 2 的語義是「阻止 stop / 無阻斷效果」，故此處 `exit 1`（中止 sync 流程、非阻斷 harness）**語義正確、非誤用**。

### 建議動作
- **G1（推薦）**：確認 `memory-sync.sh:44` 的 `exit 1` 為「有意的非阻斷中止」（已確認：remote mismatch 時放棄 sync，不該阻斷 session）→ **保持不變**，加 1 行註解標明「# exit 1: non-blocking abort (PostCompact/Stop event, intentional)」避免未來誤改。
- **G2（不做）**：報告建議的「全面 exit 1 → exit 2 稽核」在你這裡已完成且通過——**不需要批次修改**。

### 驗收條件
- `memory-sync.sh:44` 加註解（1 行）；其餘 hooks 無變更。

### 風險
- **零**（1 行註解）。

---

## 8. ⚪ MEMORY.md 200 行 cap（原 P2）— 近 no-op，加預防 gate

### 現況（已實測）
- `wc -l MEMORY.md` → **87 行 / 200**（43% 使用率，遠未觸頂）。
- 已有 `memory-compactor` skill + agent（>200 行時委派）。

### 證據與可信度
- community-practices [來源宣稱, Ian Paterson]：always-loaded ≤200 行；「501 行導致 60% lessons 不可見」（lines 241–248）。
- deep-practices-v2 [官方引述, Boris Cherny ★★★★☆]：CLAUDE.md 最佳 <200 行 / <5,000 tokens（lines 283–286）。**注意**：此 cap 報告中指 **CLAUDE.md**，非 MEMORY.md；MEMORY.md 的 200 行 cap 來自 Ian Paterson 的 always-loaded layer。

### 建議動作
- **H1（推薦）**：你的 MEMORY.md cap 200 已寫進 `core.md`（「總行 >200 → 委派 memory-compactor」），機制**已存在**。87 行 → 無需動作。
- **H2（可選預防）**：在 session-stop.sh 加軟性提醒：`wc -l MEMORY.md` >180 行時輸出警示（提前於 200 觸發）。約 +5 行 bash。但**現狀 87 行，優先序低**。
- **H3（澄清）**：你的 CLAUDE.md ≤200 行規則（不同於 MEMORY.md）已守（現況見 `wc -l CLAUDE.md`；core.md §Framework Integrity 管理）。

### 驗收條件
- 無需立即動作。若做 H2：人為觸發 >180 行測試輸出警示。

### 風險
- **零 ~ 極低**。

---

## 9. 🔵 .claude/tasks/ JSON persistence（原 P2）— 合併到 §2 handoff

### 現況
- `ls .claude/tasks/` → 不存在。但 `schemas/progress.schema.json` 已覆蓋「跨 session 任務持久化」需求。

### 證據與可信度
- community-practices [來源宣稱, Alex Opalic]：`{task_id, status, spec, last_commit, blockers}`（line 339）。
- deep-practices-v2 [來源宣稱, Ralph Loop]：`tasks.json` 作持久記憶；**注意**：researcher 確認 deep-v2 **未指定 `.claude/tasks/` 具體路徑**，用泛稱 `tasks.json`。

### 建議動作
- **I1（推薦）**：**不另建 `.claude/tasks/`**。與 §2 的 `claude-progress.json` 合併——後者 schema 已含 `steps[]`（含 id/title/status/notes）、`current_step`、`next_action`，**完全覆蓋** Alex Opalic 的 `{task_id, status, spec, last_commit, blockers}`。
- **I2（不做）**：避免 STATUS.md + .claude/tasks/ + claude-progress.json 三套並存（維護債 + 規則矛盾）。

### 驗收條件
- 同 §2（採用 progress.schema.json 即同時滿足本項）。

### 風險
- **零**（合併，不新增）。

---

## 10. 🔵 eval harness first（原 P2）— 流程紀律化

### 現況
- 已有 `eval-designer` skill（4 條件：auto-calculable / hard-to-hack / target-relevant / sensitive）+ `scripts/healthcheck.sh` + core.md TEST 階段「測試驗意圖」紀律。
- → 「eval-first」精神**已存在於 harness 哲學**，但無「先建 eval 再寫 feature」的強制流程。

### 證據與可信度
- community-practices [來源宣稱, RAG 11 天案例]：Day 1-2 先建 50 fixtures；87% pass / 20% rejection；read-only reviewer 防 auto-accept（lines 465–487）。
- deep-practices-v2 [業界領袖, Addy Osmani]：@reviewer 只讀 teammate（lines 207–212）；[學術, source-8（未具名）]：LLM 生成 AGENTS.md 無益、降 ~3% 成功率、增 20% 成本（lines 227–229）。<!-- SONNET-FLAG: source-8 匿名；數字 [個人宣稱/學術 — 無 arXiv 可驗] — 採信前建議查原始來源 -->

### 建議動作
- **J1（推薦）**：你的 workspace 是**研究型**（非 feature-heavy code repo），「eval-first 50 fixtures」對研究報告不直接適用。對**有實作的任務**（hooks/scripts）→ 套用既有 `eval-designer` + §6 的 fixture 測試已覆蓋。
- **J2（採納 read-only reviewer 精神）**：你已有 `/deep-review`、`review-hub`、`code-reviewer` agent（Read/Grep/Glob only = 天然 read-only）→ **已符合**。確認 reviewer agent 無 write 工具即可。
- **J3（採納 AGENTS.md 警示）**：core.md 已有「只寫無法從 repo 推導的行為契約」——與「LLM 生成 AGENTS.md 無益」一致。無需動作。

### 驗收條件
- 確認 `code-reviewer` / `review-hub` agent 工具集無 Edit/Write（grep agent 定義）。

### 風險
- **零**（多為確認既有）。

---

## 11. 🔵 AST graph navigation（原 P2）— 不適用，存檔

### 現況
- workspace 是研究 / harness 配置型，**非 >50K loc 的 code-heavy repo**。

### 證據與可信度
- 兩份報告 [來源宣稱, Graphify / mcplens]：>50K loc → RAG MCP（70-85% token 減）/ AST graph（宣稱 71x）。deep-v2 researcher 確認**未給明確 loc 門檻**；community 給 >50K loc。
- 數字 [個人宣稱]，無學術背書，且「71x」是 navigation overhead 對比非總 token。

### 建議動作
- **K1（不做，存檔）**：你的 codebase 規模未達 RAG/AST 收益點。**列入未來研究**：若 workspace 演化成大型 code repo（或你接手大型專案），再評估。
- **K2（研究延伸）**：可做的是「對你常 grep 的大檔（如 block-dangerous.sh 376 行、session-init.sh）建索引」——但收益小，優先序最低。

### 驗收條件
- N/A（決策為「暫不採用」）。

---

## 12. 額外發現（報告外，本次查驗浮現）

1. **🔴 bypassPermissions × CVE-2025-59536 直接命中**（見 §5）：你的 default `bypassPermissions` 正是 Check Point 揭露的暴露面。若你會 clone 外部 repo，這應**升級為 P0 安全評估**。
2. **本地 main 落後 origin/main 2 commits**：本 session 來源檔（PR #492/#493）在 origin 但不在本地 working tree（已從 origin 讀取）。建議任務結束後 `git pull` 同步本地 main。
3. **schema 落差風險普遍化**：autoCompactAt 不存在揭示一個系統性風險——**社群 blog 的 config 建議常引用非官方 / 已棄用 / 版本特定的 key**。建議：未來採納任何 `settings.json` 建議前，一律先對 `https://www.schemastore.org/claude-code-settings.json` 驗 key 存在性。可寫成 `harness-meta` skill 的一個 check。
4. **report 內部數字矛盾未被原報告標記**：Jamie Cole（短 session）vs Sean Moran（long session）方向相反但同列「最佳實踐」；兩 researcher 對 Branch8 同一數字給不同可信度標（[來源宣稱] vs [企業自述]/[個人宣稱]）。→ 採信前需 source 分級，已在各節標註。

---

## 13. 建議執行順序（你核准後）

| 批次 | 項目 | 預估 | 風險 | 阻斷? |
|------|------|------|------|------|
| **批次 0（先驗證）** | §1-A1 採人為紀律（零變更）或 §1-A2 試 `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=60`（須重啟+實測）；§5-E4 hook 來源稽核；§12.1 bypassPermissions 暴露評估 | 30 min | 零（A1）/ 中（A2 UNVERIFIED） | A2 須實測通過才採 |
| **批次 1（真缺口，低風險）** | §2 採用 progress.schema；§3 session 紀律 1 行；§4-D1 skill description 補齊；§7 exit 1 註解 | 1-2 hr | 低 | auto-load byte 量測 GATE |
| **批次 2（測試強化）** | §6-F2 block-dangerous fixture 測試；§10-J2 確認 reviewer read-only | 2-3 hr | 低 | — |
| **批次 3（評估後決定）** | §5-E2 permission mode 收緊（需你決策）；§8-H2 MEMORY 預防警示 | 視決策 | 中 | 你的 trade-off 決定 |
| **不做 / 存檔** | §1 報告原 P0 案、§9 .claude/tasks、§11 AST、§5-E3 kill-switch、§6-F1 拆分 | — | — | — |

**auto-load byte GATE**：批次 1 涉 §2/§3 寫入 auto-load（現 18,726 / cap 19,000，餘 274 B）。執行前 `wc -c CLAUDE.md .claude/rules/*.md` 量測；若 §2+§3 合計 >274 B → 下沉到 `refs/` + auto-load 只留指針（符合 core.md §Framework Integrity「不為塞 byte 反推湊」）。

---

## 14. 驗收總表（healthcheck 友善）

每批次完成後跑 `bash scripts/healthcheck.sh`，且：
- [ ] §1：`python3 -m json.tool .claude/settings.json` 通過，未引入 schema-invalid key
- [ ] §2：`claude-progress.json` 樣本通過 schema 驗證
- [ ] §3：auto-load byte ≤ 19,000（`wc -c`）
- [ ] §4：`grep -L "Do NOT use for" .claude/skills/*/SKILL.md` 已逐一確認
- [ ] §5：hook command 來源 100% 指向 repo 內腳本
- [ ] §6：`tests/hooks/test-block-dangerous.sh` 全綠且能驗意圖
- [ ] §7：`memory-sync.sh:44` 加註解
- [ ] §10：reviewer agent 工具集無 Edit/Write

---

## 15. 執行狀態（2026-06-07，使用者核准後）

使用者經 AskUserQuestion 拍板：§1=A1 人為紀律｜§5=只稽核不改 mode｜批次 1 採 §2/§4/§7｜其餘採 §6/§10/§12.3/§8｜§3 跳過。**執行時「先讀後動」發現多項已滿足或與既有決策衝突**，誠實記錄如下。

### ✅ 已執行（commit 本 branch）
| 項目 | 動作 | 驗證 |
|------|------|------|
| **§6** | `tests/hooks/test-block-dangerous.sh`（safe→exit0 / dangerous→exit2） | **13/13 pass + mutation test 確認能 fail loud**（中和 block → `rm -rf /etc` 漏放，測試會抓到） |
| **§12.3** | `harness-meta/scripts/schema-verify.sh` + SKILL.md Diagnose 步驟加指針 | 真 settings PASS(8 key)；注入 `autoCompactAt`→FAIL。**副發現**：`advisorModel` 也不在 schemastore（schema 落後），已加 `known_real` 豁免 |

### ⚪ 已滿足，無需動作（執行時 grep 確認）
| 項目 | 現況 |
|------|------|
| **§4 skill description** | `grep -L "Do NOT use for"` → **空**。27 skills 全部已有，**無一缺漏** → 無需補齊 |
| **§5-E4 hook 來源稽核** | 所有 hook command → **0 個外部來源**，全指向 `$CLAUDE_PROJECT_DIR/.claude/hooks/` → 安全 |
| **§10 reviewer read-only** | `reviewer` / `quick-code-reviewer` / `security-reviewer` 工具集 = **`Read, Grep, Glob`**（無 Edit/Write）→ 已天然 read-only |

### 衝突項 → 已交使用者裁決（2026-06-07，不 silent fork）
| 項目 | 衝突 | 使用者裁決 |
|------|------|-----------|
| **§8 MEMORY >180 行警示** | **直接違反 ADR 2026-05-31**（`docs/reference/auto-memory-hybrid.md`）：該 ADR **刻意移除** session-stop.sh L300-311 的 MEMORY 大小監控（repo MEMORY.md 已凍結為歷史 log；真實 auto-memory 為 machine-local + 官方優雅降級）。 | **DROP** ✅——遵守 ADR，不加警示。當前狀態即正確，無需動作。 |
| **§2 core.md 加指針（B2）** | 同 ADR **延後項 #1**：core.md 長期記憶回路段須走 `autoload-evolution`（≤1 規則/cycle + eval gate），**非 freehand 改 auto-load**，且該段標記待重構對齊兩層模型。基礎設施 `session-stop.sh:184-224` auto-update + `session-init.sh:404-445` 讀取**已完整接線** ✓ | **走 autoload-evolution 正規加** → 不在本 PR；另起 `/autoload-evolution` 閉環（≤1 規則/cycle + eval 回歸 gate）把指針正規加進 core.md。**列為後續待辦**。 |

### §7（使用者核准）→ 未執行，狀態明示（不 silent drop）
- **§7 exit 1 註解 = NOT DONE**。使用者批次 1 核准了「§7 exit 1 註解」，但執行時「先讀後動」發現：`memory-sync.sh` 已是 no-op（line 17 `exit 0`，ADR 2026-05-31 停用自動 commit），故 :44 的 `exit 1` 是 **dead code（永不執行）**。原計劃「加註解標非阻斷」語義不精確（會誤導為「會執行」）。
- **決定**：**不加註解**——對永不執行的死碼加「防誤改」註解價值近零；正確處置是隨 §2 走 autoload-evolution 重構記憶層時一併清理 memory-sync 死碼。**已在收尾向使用者明示此項未做 + 理由**（非靜默跳過）。

### 已修正（self-correction，advisor 攔下）
- **`schema-verify.sh` 的 `advisorModel` 豁免註解**：原寫 `實證` 但**從未驗證 harness 實讀此 key**（advisor 工具可用 ≠ 此 key 被讀）→ 已改標 `假設未驗證`（守 unverified_success 閘門，不掛假 verified-label）。
- **§3** 使用者跳過（long-session 偏好），存檔。

*草稿 by Opus 4.8 | 修訂 by Sonnet 4.6 | 執行 by Opus 4.8 | 2026-06-07*
