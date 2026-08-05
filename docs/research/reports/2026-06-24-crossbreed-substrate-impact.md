---
title: "跨模型 Harness 激盪 loop-2：融合規則對 substrate（hooks/agents/commands/skills）落地衝擊 + R3 不上調 cap 落地實證 + 2 HIGH_VALUE open-q 落地設計"
date: 2026-06-24
status: draft-for-decision
branch: feature/chatgpt55-harness-crossbreed
related: 2026-06-23-crossmodel-harness-crossbreed.md
tags: [harness-engineering, substrate-impact, inline-mirror-sync, byte-cap, autoload-evolution, r3-task-contract]
type: research-report
workflow: "crossbreed-substrate-impact (7 agents, 455K tokens, 600s, fable-free)"
---

# loop-2：融合規則 substrate 落地衝擊與可行性實證

> **一句話結論**：第一輪驗證 codex-rewrite 的 CLAUDE.md+rules，loop-2 補齊使用者要求的 **hooks/agents/commands/skills 層** —— 融合規則落地會觸及 **3 個 inline-mirror sync 點 + 9 個 agent/skill dependents + 5 個 hook 風險閘**；**R3 Task-Contract 經主對話親算可在不上調 cap 下落地（18,995/19,000，5B 飽和）**；2 個 HIGH_VALUE open-q 皆可落 off-auto-load（0 byte），model-switching=READY（須修 confidence-floor 衝突）、memory-write-gate=NEEDS_PLUMBING。

## 0. loop-2 定位

第一輪交付比較報告 + 融合草案 + Session Insight，但只覆蓋使用者要求的 **CLAUDE.md + rules**。codex-rewrite **無 hooks/agents/commands/skills 對照版** → 使用者要求的「包含 hooks/agents/commands/skills」= **分析融合規則對現有 substrate 的落地衝擊**，非比對兩家 substrate 改寫。

本輪（dynamic workflow，fable-free 避開已知不可用）：substrate scan → 3 並行深化（衝擊矩陣 / R3 落地實證 / open-q 設計）+ 各帶 opus 對抗稽核。**仍不動 auto-load**（使用者選深化研究）。所有關鍵數字 + 壓縮候選 + sync 點主對話親 grep 重驗。

## 1. inline-mirror sync 點（3 個，全主對話親驗存在）

融合規則落地最大的隱性衝擊 = **silent fork**：auto-load 內容被 sub-agent/skill 內聯鏡像，改了 canonical 卻沒同步鏡像 → 兩處漂移。

| sync 點 | 鏡像什麼 | R3 觸發條件 | 親驗 |
|------|------|------|------|
| `.claude/agents/multi-mode-agent.md:31-40` | core.md The Loop 六階段（:33 自帶 sync 指令「core.md 條文變更時須同步本檔」）+ :21-28 四 pilot Mode 紀律表 | R3 落 subagent-strategy（非 core.md Loop）→ **此鏡像不需同步**；但若 R3 滲入 core.md IDENTIFY/APPLY 則需 | ✓ :31-40 存在 |
| `.claude/agents/multi-mode-agent.md:49` | Return schema：`{mode, model, 成功條件達標?, 驗證輸出前5/後5行, open questions, 升級建議}` | **R3 建立 canonical Return schema → 此鏡像必須同步**（3 處欄位名對齊）否則 parent 期待 R3 schema 而 child 吐 legacy schema | ✓ :49 親驗 |
| `.claude/skills/multi-mode-skill/SKILL.md:78` | 委派門檻（≥10 檔/>20 工具/≥3 子任務）+ 自帶 sync 指令「門檻 canonical 定義 = rules/subagent-strategy.md，改動時同步本段」 | R3 加 spawn 時 Task-Contract 欄位 → :82-84 spawn template 須同步 | ✓ :78 親驗（grep 模式初判失誤，實際存在） |

**關鍵修正（opus audit）**：multi-mode-agent.md:49 sync **是必須的**，理由不是「prompt-lifecycle.md:9 命令」（它只管 core.md Loop 鏡像），而是「**R3 自身建立 canonical Return schema，:49 成為其鏡像**」。誤把「prompt-lifecycle 沒提到 = 不需 sync」會讓未來編輯者跳過必要同步。

## 2. substrate dependents（R3 衝擊範圍）

### agents（5 個 handoff dependents）
- `multi-mode-agent.md:49` — 輸出 typed handoff，R3 加 Goal/Done-when/Allowed-paths（**主同步點**）
- `self-escalate.md` — JSON schema `escalate_to`，R3 Allowed-paths 可能需引用
- `implementer.md` / `haiku-implementer.md` / `reviewer.md` — 共用 child-契約 boilerplate（「child 只回結果不加確認句；不 self-retry」= R3 要形式化的隱式 handoff shape）

### skills（4 個 Task-Contract dependents）
- `autoresearch/SKILL.md` — 已有 Goal/Scope/Metric/Direction/Verify（**最接近 R3 的既有類比**，R3 欄位名應對齊或顯式標差異）
- `multi-mode-skill/SKILL.md:82-84` — spawn template 用非正式 task-contract（「成功條件：<可機械驗證>」）→ R3 形式化後須更新 template 吐具名欄位
- `overnight-research/SKILL.md` — Step 0 `/goal` 區塊（TOPIC/REPORT_PATH/MIN_CHARS）= 非正式 Task-Contract
- `handoff/SKILL.md` — claude-progress.json（steps[]/next_action）= 跨 session 持久化 Task-Contract，與 R3 Goal/Done-when 直接重疊

### hooks（5 個風險閘 = R5 5-tier 落地點）
- `block-dangerous.sh`（PreToolUse Bash）— rm -rf / push --force / kubectl delete / curl|sh / SQL DROP/TRUNCATE = **R5 tier 3-5 destructive 主執行點**
- `protect-sensitive-files.sh`（PreToolUse Edit|Write）— .env/.pem/.key/credentials = R5 credential tier
- `pre-commit-review.sh`（PreToolUse git-commit）— healthcheck FAIL=0 + >5 檔/>200 行 gate = R5 tier-2（可逆但有後果）
- `settings.json permissions.ask` — push --force / github push = R5 tier 4-5 人工確認
- `settings.json permissions.deny` — rm -rf /* / curl|bash / chmod 777 = 在 hook 之前硬擋

**結論（R5 落地）**：R5 的 5-tier 不需新增 prose 重列 destructive（會撞既有 4 列 → core.md:70 矛盾陷阱）；正解 = **5-tier 概念 map 到既有 hook 層**（tier 3-5 → block-dangerous + deny；tier 1-2 → pre-commit-review），escalation ladder 為唯一淨新增概念，path-scoped 0 auto-load。

## 3. R3 落地可行性實證（不上調 cap，主對話親算）

| 項目 | agent 報告 | 主對話親驗 | 結論 |
|------|------|------|------|
| R3 byte_cost | 522 | 521（含 header，±1 trailing-newline） | ✓ |
| 壓縮候選 L16 | −45 | grep -c=1 存在 | ✓ |
| 壓縮候選 L17 | −47 | grep -c=1 存在 | ✓ |
| 壓縮候選 L30 | −82 | grep -c=1 存在 | ✓ |
| 壓縮候選 L38 | −65 | grep -c=1 存在 | ✓ |
| 壓縮總計 | 238 | 親驗全存在 | ✓ |
| 淨增 | 283 | **18,713 + 282 = 18,995/19,000** | ✓ |
| **headroom_after** | （bare true）| **5B（飽和）** | ⚠️ |
| feasible_without_cap_raise | true | **TRUE 但飽和** | ✓ |

**關鍵發現**：4 個壓縮候選**全部 grep 驗證存在且 byte 精確（±1B）**，無 Lesson 2026-06-23-D 的「~0B 謊言」。R3 確實可在不上調 cap 下落地——**但落地後 5B headroom = 飽和**（觸發 MEMORY「19,000 近滿監控」待辦），本 cycle 物理上不可再落其他規則（core.md:80 ≤1/cycle 本就強制，5B 餘裕讓它物理成真）。

### R3 最終文字（繁中，ChatGPT 5.5 authored，credit）
```
## 任務契約（Handoff Contract）
委派任務必含欄位（child 回傳同格式）：Goal（1 窄結果）·Non-goals（不碰）·
Allowed-paths（讀寫白名單）·Context（檔/錯/假設/diff）·Done-when（確定性條件）·
Return：{mode, model, 達標?, 驗證前5/後5行, open_questions, 升級建議}·
[mode: haiku|sonnet|opus|fable]（parent 決，child 不自切）·語言：繁中。
Child 未收此格式 → 不得開工，回報 parent 補齊。巢狀委派需顯式授權。
```

### 必要 sync（落地時一併做，否則 silent fork）
`multi-mode-agent.md:49` 三處欄位名對齊 R3 Return schema：
- `成功條件達標?` → `達標?`
- `驗證輸出前5/後5行` → `驗證前5/後5行`
- `open questions` → `open_questions`

## 4. 2 個 HIGH_VALUE open-q 落地設計（皆 0 auto-load byte）

### 4.1 model-switching-as-control — **READY（須修 1 衝突）**
- **落點**：`self-escalate.md`（escalate_to 觸發表 + verifier-score threshold 列）+ `multi-mode-skill SKILL.md §5/§1`（router 依 next_action==escalate 在下次 spawn re-bind model；§1 Fable→Opus fallback threshold-explicit）。**非 hook**（escalation 需 LLM judge 的 confidence，非確定性 shell gate）。
- **失敗背書**：CLAUDE.md:22「Fable cyber/bio silent fallback → Opus」（silent = 無門檻記錄的不受控切換）+ 本 session Fable 不可用事件。
- **opus audit 修正（必做）**：
  - ❌ 設計誤稱「confidence 由 exit-code 衍生 = 確定性」→ 實際 self-escalate confidence 是 **LLM judgement**（:24-31），exit-code 衍生的是 `converged` 非 `confidence`。控制 = 對 LLM 判定的 scalar 做確定性比較，移除 line-17/exit-code 歸因。
  - ❌ 新增 `confidence<0.70 → escalate` 與既有三帶（≥0.85 可靠 / 0.7-0.85 需確認 / <0.7 not converged）**語意衝突**——會讓每個 `converged=false`（最常見非終態）都觸發 model re-bind，燒掉便宜模型的迭代預算。**正解**：`confidence<floor AND failure-count≥2`（複用既有 ≥3 觸發降為 ≥2），或保持 task-class 驅動、刪 raw-confidence 列。
- **byte**：self-escalate +~120B、SKILL §5/§1 +~150B，皆 off auto-load。

### 4.2 memory-write-gate — **NEEDS_PLUMBING**
- **落點**：`memory-compactor.md`（Conflict Gate :44-50 → Write-Integrity Gate，對 Lesson consolidate/promote 做 anchor 驗證）+ `sync-memory.py`（新 Lesson 行做 non-blocking anchor-presence warning，fail-open）。**非新 hook**（複用既有 memory-sync.sh → sync-memory.py 路徑）。
- **設計**：memory-compactor 已守 DELETE 方向（Post-Prune self-verify :75-98 斷言 Lesson-count + 待辦存活，引 faulty-memory 2605-12978）；**gap = INVERSE 方向**——無物 gate 一條 faulty Lesson 寫入。
- **失敗背書**：Lesson 2026-06-04-D（agent 寫的 record ≠ validated 決定）+ 2026-06-14-C（grep-confirmed-absent ≠ failure-validated）+ Fable Ex3 自欺寫入 memory + faulty-memory 論文非單調效用。
- **opus audit 修正**：設計誤稱 sync-memory.py 用 `pull --rebase`，實際 :222 是 `pull --no-rebase`（刻意讓 merge=union driver 處理並發 append）→ warning 區塊須對齊既有 fail-open 機制。
- **byte**：memory-compactor +~200B、sync-memory.py +~15 行 Python，皆 off auto-load。

### verification-stringency-scales-with-capability — **ACADEMIC_DEFER**（第一輪已判，本輪不變）
無「強模型需更少驗證反被燒」的真實失敗錨點。

## 5. 落地 checklist（供 /autoload-evolution，使用者裁決後）

**Cycle 1（R3，唯一本 cycle 可落，因 5B 飽和）**：
1. 壓 subagent-strategy.md L16/L17/L30/L38（−238B，親驗存在）
2. 加 R3 任務契約區塊（+521B）
3. **sync** multi-mode-agent.md:49 三欄位名（必做，否則 silent fork）
4. 檢查 multi-mode-skill SKILL.md:82-84 spawn template 是否需吐具名欄位
5. eval 回歸 ≥5pp 驗證；healthcheck FAIL=0；byte 確認 18,995/19,000
6. **記錄飽和**：MEMORY「19,000 近滿監控」更新為 5B

**off-cycle（0 auto-load，不佔 R3 cycle）**：
- model-switching-as-control（self-escalate + SKILL，修 confidence-floor 衝突）
- memory-write-gate（memory-compactor + sync-memory.py，NEEDS_PLUMBING）

## 6. 殘留風險與下一步
- **未套用**：仍守先報告後裁決，本輪零 .claude/ 編輯。套用走 /autoload-evolution gated loop。
- **5B 飽和**：R3 落地後 auto-load 幾乎滿——任何後續 auto-load 增補前必先壓更多空間。R1/R2 即使壓縮也無空間共存，必走 refs 化。
- **驗證狀態**：3 inline-mirror + 4 壓縮候選 + R3 落地 byte 主對話親 grep/親算 exit=0；opus 對抗稽核（fable 缺位代行）修正 model-switching 2 個實質設計錯 + sync rationale 誤導。
- **教訓**：主對話親驗壓縮候選時，第 3 個 inline-mirror（multi-mode-skill:78）因 grep 模式含反引號未對上、初判「agent 幻覺」，再驗才確認存在——**親驗也可能因 grep 模式錯誤而冤枉 agent，grep 失配時換模式重試再下結論**（見 session insight）。
