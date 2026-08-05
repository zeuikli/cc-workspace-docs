---
title: "Fusion 架構 Phase 1 落地驗證（GLM-5.2 協作）"
date: 2026-07-09
status: done
method: "逐項驗證 4 個優化項是否在 Claude Code 現有功能下可落地；每項附檔案:行號佐證"
parent-report: research/reports/2026-07-09-fusion-architecture-design-plan.md
scope: "§2.3 Claude Code Phase 1 — Sidekick via Sub-agent（現有能力,零修改）"
type: architecture-validation
validator: GLM-5.2
---

# Fusion 架構 Phase 1 落地驗證

> 本報告驗證 `2026-07-09-fusion-architecture-design-plan.md` §2.3 Phase 1（「現有能力,零修改」）的四個優化項是否在 Claude Code 現有功能下可落地。
> 驗證者: GLM-5.2（ceiling 檔,開源）。今天: 2026-07-09。

## 驗證對象（報告 §2.3 原文）

Phase 1 主張: workspace 現有 `multi-mode-skill` + `multi-mode-agent` 已近似 Sidekick 模式,只需「改使用模式」不改架構。四個優化項:

1. 主對話預設委派機械任務給 cost 檔 sidekick,只在「規劃/歧義/審查」時親做
2. sidekick 回報只含結論 + 檔案:行號（delegation-protocol.md §4 既有規則）
3. 主對話的 cache 前綴保持穩定（context-management.md Static First 既有規則）
4. 用 `claude-progress.json` checkpoint 模擬 sidekick 持久性

## 驗證方法（5 項查證）

| # | 查證項 | 檔案 | 結論 |
|---|--------|------|------|
| 1 | agent 是否支援 model override + mode 注入 | `.claude/agents/multi-mode-agent.md` | ✅ 支援 |
| 2 | router 是否支援「預設委派」邏輯 | `.claude/skills/multi-mode-skill/SKILL.md` | ✅ 支援 |
| 3 | §4 回報合約是否已落地 | `.claude/refs/delegation-protocol.md` | ✅ 已落地 |
| 4 | Static First 規則是否存在 | `.claude/rules/context-management.md` | ✅ 存在 |
| 5 | checkpoint 機制是否已有實作 | `schemas/progress.schema.json` + `.claude/hooks/session-init.sh` + `.claude/skills/multi-mode-skill/SKILL.md` §4 | ✅ 已實作 |

---

## 逐項驗證

### 優化項 1: 主對話預設委派機械任務給 cost 檔 sidekick,只在「規劃/歧義/審查」時親做

**判定: ✅ 可落地** — 既有功能/規則已支撐,無需修改。

**佐證（檔案:行號）**:

- `.claude/agents/multi-mode-agent.md:8`（frontmatter）: `model: sonnet` 為預設,但 **parent 於 spawn 時依任務分類綁定 model + 注入 tier 指令** — 明確支援 model override。
- `.claude/agents/multi-mode-agent.md:13-15`（不變式）: 「你的 model 由 parent 在 spawn 時綁定,不可自切」「parent 會在 task description 注入 `[mode: cost|quality|ceiling|frontier]`」— mode 注入機制落地。
- `.claude/skills/multi-mode-skill/SKILL.md:§1`（router 核心表）: 「0–1 位置數 → tier cost → model haiku → inline/spawn 1 worker」— 機械任務自動路由到 cost 檔,正是 sidekick 的角色定位。
- `.claude/skills/multi-mode-skill/SKILL.md:§2`（委派門檻）: 「任一成立 → spawn multi-mode-agent（注入 `[mode: ...]` + 對應 `model` override）」+ spawn 範例 `Agent(subagent_type="multi-mode-agent", model="opus", prompt="[mode: ceiling] ...")` — spawn 時綁定 cost 檔 model（haiku）即可作 sidekick。
- `.claude/refs/delegation-protocol.md:§1`（指揮官不下場）: 「預設委派、例外親做」+ 「T0 親做例外: 0–1 檔且 ≤3 次工具呼叫;對話/裁決/確認 gate」— 「只在規劃/歧義/審查時親做」已有量化門檻。
- `.claude/refs/delegation-protocol.md:§1 T1 一律委派`: 「讀取 >3 檔或預期輸出 >100 行、掃 repo、批次改檔、跑驗證迭代——主對話只進結論」— 機械任務委派規則已落地。

**落地姿勢**: 主對話遇到機械任務 → spawn `multi-mode-agent` with `model="haiku"`, `prompt="[mode: cost] <task>"`。這是 §1 表的 cost 行 + §2 spawn 範例的直接組合,零修改。

---

### 優化項 2: sidekick 回報只含結論 + 檔案:行號（delegation-protocol.md §4 既有規則）

**判定: ✅ 可落地** — 既有功能/規則已支撐,無需修改。

**佐證（檔案:行號）**:

- `.claude/refs/delegation-protocol.md:§4 回報合約`:
  - 「只回**結論 + 檔案:行號**;禁貼大段原文進 parent context」
  - 「長產物（>30 行）→ 存檔（scratchpad 或指定路徑）,回傳路徑 + ≤10 行摘要」
  - 「輸出只含結果:不加確認句、不加開場白;要求 JSON 就回純 JSON」
- `.claude/agents/multi-mode-agent.md:輸出契約`（檔尾）: 「回報 parent 用結構化摘要（非原始 dump）: `{mode, model, 達標?, 驗證前5/後5行, open_questions, 升級建議}`」— sidekick（multi-mode-agent）的回報 schema 已對齊 §4 合約,且明文「不加確認句」「不 self-retry」。
- `.claude/skills/multi-mode-skill/SKILL.md:§4`（Context 不爆）: 「主對話只收**摘要**」— 與 §4 合約同向,router 端也要求摘要回報。

**落地姿勢**: sidekick（multi-mode-agent）的輸出契約已內建結論 + 檔案:行號 + 摘要格式,parent 不需額外指示。零修改。

---

### 優化項 3: 主對話的 cache 前綴保持穩定（context-management.md Static First 既有規則）

**判定: ✅ 可落地** — 既有功能/規則已支撐,無需修改。

**佐證（檔案:行號）**:

- `.claude/rules/context-management.md:Prompt Caching（Static First）`:
  - 「CLAUDE.md = 最穩定快取前綴,永遠放最前、session 內不動」
  - 「**Mid-session 禁止**切換模型/增刪 tool/改 CLAUDE.md（破快取）;能力升級需求 → sub-agent 檔位 override（載體 `multi-mode-agent`）或新 session,不切主對話模型」
- `.claude/skills/multi-mode-skill/SKILL.md:§0 不變式`: 「model 在 spawn 時綁定,主對話 mid-session 不切 model（破 prompt cache,見 context-management.md）。要換檔位 → 用 sub-agent `model` override 或新 session」— router 明文遵守 Static First。
- `.claude/skills/multi-mode-skill/SKILL.md:§4`（NLAH）: 「原始目標放 HEAD,最新工具輸出放 TAIL,動態狀態放中間」— cache 前綴穩定性 + 動態內容放置規則並存。
- `.claude/agents/multi-mode-agent.md:isolation: worktree`（frontmatter）: sidekick 在獨立 worktree 執行,context 與主對話隔離 → sidekick 的 context 變動不污染主對話 cache 前綴。

**落地姿勢**: Phase 1 的 sidekick 是 sub-agent spawn（新 context）,主對話模型/工具/CLAUDE.md 全程不動 → cache 前綴天然穩定。這正是 context-management.md「能力升級 → sub-agent 檔位 override」的設計意圖。零修改。

---

### 優化項 4: 用 `claude-progress.json` checkpoint 模擬 sidekick 持久性

**判定: ⚠️ 需修改** — checkpoint 機制本身已實作且可用,但**現有實作是為「跨 session 長任務 resume」設計,並非為「sidekick 跨 spawn 狀態恢復」設計**;要模擬 sidekick 持久性需小幅調整使用模式（非架構修改）。

**佐證（檔案:行號）**:

**已落地部分（checkpoint 基礎設施完備）**:

- `schemas/progress.schema.json`: 完整 schema 已定義 — `task_id` / `title` / `status` / `steps[]`（含 id/title/status/notes）/ `current_step` / `next_action` / `sessions[]` / `reminders[]`。可承載 sidekick 的 goal + 已完成 + 下一步。
- `.claude/hooks/session-init.sh`: 多處 `PROGRESS_JSON="$WORKSPACE_DIR/claude-progress.json"` + `if [ -f "$PROGRESS_JSON" ]; then python3 ...` — session 啟動時自動讀取 checkpoint。
- `.claude/skills/multi-mode-skill/SKILL.md:§4 防衰退`: 「每輪寫 `claude-progress.json`（goal + 成功條件 + 已完成 + 下一步）;不依賴 compact 後記憶」— router 已內建 checkpoint 寫入。
- `.claude/skills/multi-mode-skill/SKILL.md:§5 /loop`: 「OBSERVE 讀 `claude-progress.json`（無 → 視為首輪,建立 goal + 成功條件）」— 跨 fire 狀態恢復已實作。
- `.claude/skills/handoff/SKILL.md`: 整個 skill 處理 `claude-progress.json` 建立/更新,交接流程完備。

**需修改部分（用於 sidekick 持久性,非現有用途）**:

1. **語義不對齊**: 現有 schema 的 `steps[]` / `current_step` / `next_action` 是為「主對話跨 session 長任務」設計的單一任務狀態。Fusion 報告 §2.3 的 sidekick 持久性需求是「sidekick 每次 spawn 時讀取 checkpoint 恢復狀態」,即 **sidekick 自身的執行狀態跨多次 spawn 保持**。兩者粒度不同:
   - 現有: 一個主任務的進度（主對話視角）
   - Fusion 需求: 一個 sidekick agent 的累積 context（sidekick 視角,可能服務多個主任務）

2. **gitignored + ephemeral 限制（重要 caveat）**:
   - `.gitignore:claude-progress.json` — 檔案不進 git。
   - `.claude/skills/handoff/SKILL.md` 鐵律: 「`claude-progress.json` 是 **gitignored + 遠端容器 ephemeral 會消失** → 交接內容必須在 `memory/MEMORY.md`（Git 追蹤）**自足**」
   - `.claude/skills/handoff/GOTCHAS.md` G4: 「下一 session（雲端 fresh clone）依 MEMORY『見 claude-progress.json round2』找佇列 → 檔案不存在（gitignored + ephemeral 容器）」— 已有實證失敗案例。
   - 含義: 在雲端 / fresh clone 環境,checkpoint 會消失 → sidekick 持久性模擬在這些環境**失效**。本機 CLI 環境則可用。

3. **sidekick 讀取入口缺失**: 現有 `session-init.sh` 是 session 啟動時讀,但 sidekick 是 sub-agent spawn（非 session 啟動）。`multi-mode-agent.md` 的「The Loop 六階段」OBSERVE 步驟是「改動前讀目標 exports + 直接 caller + 共用 utility」,**未明文讀 `claude-progress.json`**。sidekick 要用 checkpoint 恢復狀態,需在 spawn prompt 中顯式指示「先讀 `claude-progress.json` 的 `<sidekick-task-id>` 段」,或在 multi-mode-agent.md OBSERVE 加一行。

**具體修改建議（小幅,不改架構）**:

- **選項 A（最小改動,推薦）**: 在主對話 spawn sidekick 的 prompt 中加一句:「先 Read `claude-progress.json` 的 `steps[].notes` 中 `<本 sidekick 的 task_id>` 相關段落恢復狀態,完成後 Write 更新該段」。這是 prompt 層調整,不改任何檔案。
- **選項 B（agent 層內化）**: 在 `.claude/agents/multi-mode-agent.md` 的 OBSERVE 步驟加一行:「若 parent prompt 標記 `[resume: <task_id>]` → 先 Read `claude-progress.json` 找對應 step 恢復狀態」。改 1 行,讓 sidekick 具備 checkpoint resume 能力。
- **選項 C（schema 層）**: 在 `schemas/progress.schema.json` 加一個 `sidekick_state` 可選欄位,專門存 sidekick 的累積 context。改 schema,但向後相容（optional）。

**為何不是 ❌**: checkpoint 基礎設施（schema + hooks + skill）已完備,語義不對齊是使用模式問題,可透過 prompt 指示或 1 行 agent 規則調整解決,非依賴未確認的 Claude Code 功能。報告 §2.3 自己也標明這是「現狀替代方案」「不是真正的 cache 持久化,但可減少重複 context 建構的 token 開銷」— 定位為模擬,非真正持久化,與本判定的 ⚠️ 一致。

---

## 統計

| 優化項 | 判定 | 依賴 | 是否需修改 |
|--------|------|------|-----------|
| 1. 預設委派 cost 檔 sidekick | ✅ 可落地 | multi-mode-agent model override + mode 注入; router §1 表; delegation-protocol §1 | 否 |
| 2. sidekick 回報結論 + 檔案:行號 | ✅ 可落地 | delegation-protocol §4; multi-mode-agent 輸出契約 | 否 |
| 3. 主對話 cache 前綴穩定 | ✅ 可落地 | context-management.md Static First; router §0 不變式; agent worktree isolation | 否 |
| 4. claude-progress.json 模擬持久性 | ⚠️ 需修改 | checkpoint 基礎設施已完備,但語義/入口/ephemeral 限制需小調整 | 是（prompt 層或 1 行 agent 規則） |

**合計: ✅×3 · ⚠️×1 · ❌×0**

## 阻擋性問題

**無阻擋性問題**。Phase 1 的 4 個優化項均可在 Claude Code 現有功能下落地:
- 3 項零修改直接可用（既有規則/功能完全覆蓋）
- 1 項（checkpoint 持久性）需小幅使用模式調整,但基礎設施已完備,不依賴任何未確認的 Claude Code 功能

**非阻擋性 caveat（需後續注意）**:

1. **ephemeral 環境失效**: 優化項 4 的 checkpoint 模擬在雲端 / fresh clone 環境會因 `claude-progress.json` gitignored 而失效（已有 handoff GOTCHAS G4 實證）。本機 CLI 環境可用。若 Fusion 架構要在雲端穩定運行,sidekick 狀態需改存 git-tracked 路徑（如 `memory/MEMORY.md` 或獨立的 git-tracked sidekick state 檔）。
2. **Phase 2 才是真阻塞**: 報告 §2.3 Phase 2（persistent sidekick with cached context）需 Claude Code 新功能,目前只能用 checkpoint 模擬。這是報告自己已標明的限制,非 Phase 1 問題。
3. **「預設委派」是行為紀律非強制 gate**: 優化項 1 的「預設委派」依賴主對話遵守 delegation-protocol §1,目前是 auto-load 規則 + SKILL 路由建議,**無 PreToolUse 硬 gate 強制**。若要確保主對話不「偷做」機械任務,需評估是否加 hook（但這超出 Phase 1「零修改」範圍,屬 Phase 2+ 議題）。

## 結論

報告 §2.3 Phase 1「現有能力,零修改」的定位**基本準確**: 3/4 優化項確實零修改可用,1/4 需小幅使用模式調整（非架構修改）。Phase 1 可作為 Fusion 架構的渐进落地起點,無阻塞。報告對 Phase 2 限制的預告（persistent sidekick 需新功能）也與本驗證一致 — checkpoint 模擬是合理的過渡方案,但不是長期答案。
