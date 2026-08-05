---
title: "deep-practices-v2 執行計劃書 — 六主題盤點 + 排程"
date: 2026-06-07
branch: feature/deep-practices-v2-plan
companion_report: research/reports/2026-06-07-claude-code-community-practices-report.md
source_report: research/reports/2026-06-07-claude-code-deep-practices-v2.md
type: execution-plan
---

# deep-practices-v2 執行計劃書

> 針對使用者圈選的六個主題（iSkill 設計、§8.1 LobeHub L1-L4、§6.2 五層成本優化、§9 P0/P1/P2），盤點 workspace 現況後排程。
> **核心結論（前置）**：六主題對應的 13 項報告行動中，**多數已滿足或屬幻覺建議**——真正新增且無設計衝突的小項僅 2 個。本計劃以「誠實 gap」為主軸，不把 13 項當待辦逐條鋪（符合 workspace 反湊數紀律）。

---

## 第一節：盤點結論總覽

### 1.1 三類判定（套用對稱懷疑）

對報告建議套用 workspace 既有紀律：不只剔除**幻覺 key**（技術上不存在），也剔除**撞既有設計的有效建議**（技術上有效，但與 workspace 刻意設計衝突 → 屬 tradeoff 非 fix，需 AskUserQuestion 不自動執行）。

| 判定類別 | 數量 | 處置 |
|---------|------|------|
| ✅ 已滿足 | 5 | 不動，僅記錄佐證 |
| 🟡 部分（有真實小 gap） | 4 | 評估後執行 |
| 🔴 未做（真 gap） | 2 | quick-win 可即執行 |
| ⚫ 報告建議無效（幻覺 key） | 1 | 剔除 |
| ⚠️ tradeoff（撞既有設計，非 fix） | 1 | AskUserQuestion 待決 |

### 1.2 主對話親驗修正子代理 verdict（unverified_success 閘門）

| 項目 | 子代理 verdict | 親驗結果 | 修正 |
|------|---------------|---------|------|
| P0-1 `memory-sync.sh:44 exit 1` | 「誤用，應改 exit 0」 | remote-mismatch 中止路徑，exit 1=sync 失敗但不阻斷 session（exit 2 才 block，見 `branch-isolation-guard.sh:14` 註解） | **語義正確，已滿足**（子代理誤判） |
| P0-4 subagent model env | 「未設定，建議加」 | env 確無 `CLAUDE_CODE_SUBAGENT_MODEL`（已驗 settings.json）| verdict 屬實，但釘定會破壞檔數路由 → 改列 ⚠️ tradeoff |
| skill body 字數 | 「25/27 超標」 | 抽驗 opus-pilot=2986 / diagram-gen=298 / spec-implement=331 屬實 | 數字屬實，但**詮釋錯**：pilot/hub skill 多命令本不適用 450 上限 |

---

## 第二節：六主題逐項盤點

### 主題 1 — iSkill 設計（community 報告主題 I）

**基準**：description 雙段（Use when + Do NOT）、body 250-450 words、banlist、name ≤64。

**現況**（27 skills）：
- ✅ name ≤64：27/27（最長 19 chars）
- ✅ description 雙段格式：27/27 字面具備
- 🟡 description 偏短：實測 17–71 words，無一達 150 words「pushy 門檻」
- ⚠️ body「超標」25/27：**此為 tradeoff 非 fix**——opus-pilot(2986)/sre(1513)/research-hub(1531) 是多命令 pilot/hub skill，450 words 上限只適用單一指令 skill（diagram-gen 298 ✓ / spec-implement 331 ✓ 證明單指令 skill 本就達標）。盲目壓縮會砍真實操作內容，違反「不破壞 working」+「不為湊數反推」。

**正確行動**：不做 batch 壓縮。改用 `skill-evolution:audit` 對逐 skill 跑四缺陷自檢（bloated/copy-paste/brittle/awkward），由 audit 判定哪些是真冗餘、哪些是必要操作內容。→ 列 P1。

### 主題 2 — §8.1 LobeHub L1-L4 演化梯度

**基準**：L1 手動 / L2 agent 輔助人工確認 / L3 agent 主導人類關鍵判斷 / L4 agent 自主優化。

**workspace 定位 ≈ L2–L3（非從零起步）**：
- `autoload-evolution` skill：閉環掃描→提案→eval gate→human-gated 整合→記錄；≤1 rule/cycle + ≤50 行 diff + eval 回歸 ≥5pp 自動 revert。→ 具備 L3 的「agent 主導 + 人類保留關鍵判斷」+ 退化可觀測。
- `skill-evolution` skill：scan/apply/audit 對照最佳實踐自我改進。
- **缺 L4 要件**：tracing-first（per-step Execution Snapshot）+ error pattern 自動 bucket 化。

**行動**：明確認定 workspace 已在 L2–L3，不需「從 L1 起步」。L4 的 tracing instrumentation 屬重型投資，列 P2 觀察項（非承諾執行）。

### 主題 3 — §6.2 五層成本優化

| 層 | 狀態 | 證據 |
|---|------|------|
| 1 Token Budgets + autoCompactAt | ⚫ 無效 | `autoCompactAt`/`tokenBudget` 幻覺 key（Lesson 2026-06-07-C）；settings.json 已驗無此 key |
| 2 Prompt Caching | ✅ 完整 | context-management.md：Static-first + cache_hit_rate>0.7 + byte cap tokenizer 免疫 |
| 3 Scope-limited Sessions | ✅ 完整 | context-management.md：per-task 4K / per-session 30K budget + PreCompact hook |
| 4 Model Routing | ✅ 完整 | haiku/sonnet/opus-pilot 三 skill + subagent-strategy 檔數路由表 |
| 5 Scoped Context References | ✅ 完整 | 下沉原則 + path-scoped on-demand + NLAH |

**真實 gap**：0（層 1 無效、層 2–5 已完整）。`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` env 雖為真實機制但 MEMORY 標「has bug」→ 不建議設定。

### 主題 4–6 — §9 P0/P1/P2 行動（13 項）

| 項 | 狀態 | 證據 / 行動 |
|---|------|------------|
| P0-1 Hook exit code 稽核 | ✅ 已滿足 | 親驗：exit 2 阻斷用對（block-dangerous/pre-compact/pre-commit-review）；memory-sync exit 1 語義正確 |
| P0-2 autoCompactAt+thinkingTokenLimit | ⚫ 無效 | 幻覺 key |
| P0-3 釘定 Claude Code 版本 | 🔴 未做 | 當前 2.1.168，無 onboarding 最低版本標注 → **quick-win** |
| P0-4 Subagent 模型驗證 | ⚠️ tradeoff | env 確無 `CLAUDE_CODE_SUBAGENT_MODEL`；但釘定破壞「0–1檔 Haiku / 2–9 Sonnet」檔數路由 → AskUserQuestion |
| P1-1 Hook Narrowness 重構 | 🟡 部分 | block-dangerous 有 13-case fixture pair；其他 hook 缺 fixture。jq 替換屬工具偏好非強制 |
| P1-2 Skill 激活率提升 | ✅ 已滿足 | `user-prompt-submit.sh` 已注入 skill routing（Twitter/YT/GH/實作關鍵字） |
| P1-3 Effort Routing | ✅ 已滿足 | CLAUDE.md:32 effort 矩陣完整，/effort high 為 daily 預設 |
| P1-4 CLAUDE.md 精確度 | ✅ 已滿足 | 32 行 ≪ 200 上限 |
| P1-5 STATUS.md handoff | ✅ 已滿足 | `schemas/progress.schema.json` + core.md 長期記憶回路要求建 claude-progress.json |
| P2-1 Multi-Agent TDD 試點 | 🔴 未做 | 無 tdd 三件組 agent；現有 test-writer/test-engineer 部分覆蓋 → 季度級 |
| P2-2 Agent Teams 評估 | 🔴 未做 | 無 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` flag → **低成本試跑可即評估** |
| P2-3 Self-Evolving 試點 | 🟡 部分 | autoload/skill-evolution 已達 L2–L3（見主題 2）；缺 tracing bucket |
| P2-4 Spec-Driven 三文件 | 🟡 部分 | `spec-implement` skill 已存在；無 product/tech/structure.md 範本目錄 |

---

## 第三節：執行排程

### 即可執行（quick-win，無設計衝突）

| # | 行動 | 規模 | 驗證條件 |
|---|------|------|---------|
| Q1 | **P0-3 版本釘定**：README 或 onboarding 標注最低 Claude Code 版本（≥2.1.116 = 所有已知 CVE 修補；當前 2.1.168）| ≤10 行 | grep README 含版本要求 |
| Q2 | **P2-2 Agent Teams 試評**：settings.json env 加 flag 試跑一個 3-5 子系統平行任務，記錄 wall-clock vs token，寫入報告（非永久啟用）| 試跑 1 次 | 產出評估記錄 |

### 已決（AskUserQuestion 2026-06-07）

| # | 決策 | 結果 |
|---|------|------|
| D1 | **P0-4 subagent model pin** | **不釘定，維持檔數路由**。靜默降級風險靠 subagent-strategy.md 文字規範 + 主對話親驗 verdict 控制（現況）。符合 workspace 成本紀律。 |
| Q2 | **Agent Teams 試評** | **本次執行**（見下方執行記錄） |

### 季度級（P1/P2，列入待辦非本次執行）

| # | 行動 | 前置 |
|---|------|------|
| S1 | **iSkill audit**：跑 `skill-evolution:audit` 對 27 skill 逐個四缺陷自檢（**非 batch 壓縮**）| — |
| S2 | **P1-1 hook fixture 擴充**：為 block-dangerous 以外的 hook 補 fixture pair | — |
| S3 | **P2-4 spec 三文件範本**：建 docs/spec/ product/tech/structure.md 範本或在 spec-implement 加範本指引 | — |
| S4 | **P2-1 Multi-Agent TDD 試點**：選中型 feature 跑 tdd 三件組，量化 regression rate | 需建 3 agent |
| S5 | **P2-3 / 主題2 L4 tracing**（觀察項，非承諾）：tracing-first Execution Snapshot + error pattern bucket | 重型投資，評估 ROI 後再定 |

---

## 第三節之二：Q2 Agent Teams 評估記錄（2026-06-07 執行）

### 對稱懷疑驗證：flag 真偽

`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` **是真實 flag**（官方文件 `code.claude.com/docs/en/agent-teams` 確認，非幻覺 key）。需 Claude Code ≥2.1.32（當前 2.1.168 ✓）。

### 誠實邊界：為何「本次試跑」無法在當前 session 完成

官方文件關鍵事實：
- Agent Teams 是**互動式 CLI session 級編排**：lead session 在使用者確認後 spawn teammates，透過 tmux/in-process pane + 共享 task list（`~/.claude/tasks/`）+ mailbox 協調。
- **「No nested teams：teammates cannot spawn their own teams or teammates. Only the lead can manage the team.」**
- 當前 runtime 是被 spawn 的 agent，**無法在此 session 內程式化啟動 Agent Team**。真正啟用須使用者在終端：① settings.json 加 flag → ② 重啟 CLI → ③ 自然語言要求建 team。

→ 不假裝跑了（unverified_success 紀律）。評估改為「啟用指南 + workspace 適配性 + 對照決策」。

### Subagents（現況）vs Agent Teams 決策表

| 維度 | Subagents（workspace 現用） | Agent Teams |
|------|---------------------------|-------------|
| 通訊 | 只回報 parent，child 間不通訊（subagent-strategy 鐵律） | teammates 直接互相 message + 共享 task list |
| Context | 各自 context，結果摘要回 parent | 各自獨立 context，不回 parent |
| token 成本 | 較低（摘要回主對話） | 顯著較高（每 teammate 獨立 instance，線性增長） |
| 協調 | 主 agent 手動管理（fan-out ≤4） | 自協調 + 依賴自動解析 |
| 最適 | 聚焦任務、只要結果（**workspace 多數研究/審查場景**） | 需互相挑戰/辯論的複雜任務（競爭假設除錯、跨層協調） |

### workspace 適配性結論

- workspace 既有 4-agent fan-out（parallel researcher）已覆蓋「平行研究/審查只要結果」場景，**token 成本更低**，符合成本紀律。
- Agent Teams 的獨特價值在「teammates 互相辯論挑戰」（如競爭假設除錯）——這是 fan-out 做不到的（child 間不通訊）。
- **建議**：保留 subagent fan-out 為預設；Agent Teams 留給「需對抗式辯論」的特定任務，由使用者在獨立 CLI session 手動啟用。**不在 settings.json 永久啟用 flag**（避免每 session 多餘協調開銷 + experimental 已知限制：無 session resumption / task status lag）。

### 使用者啟用指南（下次試跑用）

```jsonc
// ~/.claude/settings.json（非 workspace settings，避免影響團隊）
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```
重啟 CLI 後，對 lead 說：「建一個 agent team，3 個 teammate 從不同角度調查 X，讓他們互相辯論挑戰對方理論」。試跑後記錄 wall-clock vs token vs 單 session 對照。

**已知限制（官方）**：無 `/resume` 復原 in-process teammates、task status 可能 lag、shutdown 慢、一次一隊、split pane 需 tmux/iTerm2（VS Code 整合終端不支援）。

---

## 第四節：被剔除/不執行清單（誠實記錄）

| 報告建議 | 不執行原因 |
|---------|-----------|
| P0-2 autoCompactAt + thinkingTokenLimit | 幻覺 key，官方 schema 不存在（Lesson 2026-06-07-C） |
| §6.2 層1 tokenBudget settings | 同上 |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` 設定 | 真實 env 但 MEMORY 標「has bug」 |
| skill body batch 壓縮到 450 words | pilot/hub 多命令 skill 不適用單指令上限；屬 tradeoff 非 fix |
| P0-1 memory-sync exit 1 改 exit 0 | 子代理誤判；exit 1 為 sync 失敗不阻斷 session 之正確語義 |

---

## 附錄：盤點方法

- 3 個並行 researcher 子代理盤點（skill 設計 / 成本 settings / P0-P1-P2 逐項）
- 主對話親驗關鍵 verdict（P0-1 exit code、P0-4 env、skill 字數抽驗）→ 修正 2 個子代理誤判
- advisor 諮詢 → 對稱懷疑原則（剔除幻覺 key + tradeoff 建議）、LobeHub L 定位、誠實 gap 主軸
