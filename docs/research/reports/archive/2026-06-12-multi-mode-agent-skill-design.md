---
title: "Multi-Mode Agent + Skill 設計：四模式內聯 · 自動 model 路由 · 破-4 fan-out · /loop 排程"
date: 2026-06-12
status: applied
branch: claude/multi-mode-agent-design-5psvdg
method: 3-way researcher fan-out（pilot skills / agent schema / fan-out+context+report 慣例）→ The Loop 六階段設計
scope: .claude/agents/multi-mode-agent.md · .claude/skills/multi-mode-skill/SKILL.md · .claude/skills/RESOLVER.md
type: design
---

## TL;DR

需求是「可 `/loop` 週期觸發、每 fire 跑 The Loop、自動選最省 model、fan-out 不受 4 限制」的自主執行單元。
交付 = **一對配對產物**，非單一 agent 或單一 skill：

- **`multi-mode-skill`**（主對話 router/orchestrator）：分類任務 → 選 model/effort/mode → inline 或 spawn worker；寬任務走 dynamic workflow 破 4；內建 `/loop` 接線。
- **`multi-mode-agent`**（sub-agent worker）：四模式（fable/opus/sonnet/haiku）紀律 **內聯**，解決「SKILL 不能在 sub-agent 執行」。

**誠實邊界**：本遠端 web 環境**無 `CronCreate`/`ScheduleWakeup` 排程原語**（ToolSearch 三次查無），無法在此武裝週期計時器。排程須於本機 CL/桌面 app 觸發；報告交代接線與停止方式，未偽造排程。

## 需求 → 解法對照

| # | 需求 | 解法 | 落地位置 |
|---|------|------|---------|
| 1 | agent 要有 4 pilot SKILL 能力（因 SKILL 無法在 sub-agent 用） | 四模式核心 gate **內聯**到 agent body（mode 紀律表）；不引用 Skill 工具（實證：15 個既有 agent 無一在 tools 列 Skill） | `multi-mode-agent.md` Mode 紀律表 |
| 2 | 每 session 用最有效率 model，200K/1M 不爆 context、不衰退 | model **spawn 時綁定**（router 依檔案數選）；NLAH + 委派重讀 + compaction 觸發 + `claude-progress.json` checkpoint | `multi-mode-skill.md` §1 §4 |
| 3 | fan-out sub-agent 不受最多並行限制 | 寬任務走 **dynamic workflow**（runtime ≤16並行/≤1000總量，與「主對話手動 4」不同層級）；multi-mode-agent 為 worker 單元 | `multi-mode-skill.md` §3 + agent Fan-out 段 |
| 4 | 參考現有準則 | 全程接地 CLAUDE.md + 4 auto-load rules + prompt-lifecycle；frontmatter/慣例比對既有 agent/skill | 全程 |
| 5 | 補不完備處 | 見下「補充缺口」 | — |
| 6 | 研究後出報告 | 本檔 | — |

## 核心架構決策（Decision-Log）

1. **Pair 而非單體**
   - Choice：skill(router) + agent(worker) 配對。
   - Rejected：① 單 agent — 無法在主對話做 skill 路由、sub-agent 無法自切 model；② 單 skill — sub-agent 無 Skill 工具（正是需求 1 的痛點）。
   - Reason：路由/排程是主對話職責，紀律執行是 worker 職責，職責分離。

2. **model 綁定於 spawn，mode 只切紀律**
   - sub-agent 無法 mid-run 換 model（且 mid-session 切 model 破 prompt cache，context-management.md 禁止）。
   - 故「多模式」拆兩軸：**model = spawn 時由 router 綁定**（最佳成本）；**mode（cost/quality/ceiling/frontier）= agent body 切換的紀律強度**。router 負責 model↔mode 最佳配對。

3. **Fan-out 破 4 = 換層級非提高上限**
   - subagent-strategy.md:16 明載「4 上限僅限主對話手動委派；dynamic workflow runtime ≤16/≤1000」。兩者不同層級不衝突。
   - 故破 4 = 寬任務改走 dynamic workflow（`agent()/parallel()/pipeline()`，每 worker 可指定 model + worktree），非去改 4 這個數字。

## 四模式內聯紀律（需求 1 細節）

各 pilot 的「無法從 repo 推導的行為契約」被提煉進 agent，capability-agnostic：

| Mode (model) | 內聯的關鍵 gate |
|--------------|----------------|
| cost (haiku) | 量化 escalation gate（≤9檔/≤300LoC stay；≥10檔/跨模組/test/≥3失敗 escalate）；>30LoC 止於 explain；citation anchor 分級 |
| quality (sonnet) | Forced self-review（>30LoC 自審 diff；auth/payment/user-data 安全自審）；line-level source-verify `:LineN`；Decision-Log |
| ceiling (opus) | Reverse-advisor 自我 peer-review；CAR 標籤；Reasoning Sandwich（Plan→Implement→Verify）；Decision-Log ≥3 外化 |
| frontier (fable) | Anti-hack 雙重驗證（自產 verdict 非證據，親跑 grep/test）；worktree `git diff` 落地檢查；evaluator 防弱化斷言；trace-first |

升級鏈：cost→quality→ceiling→frontier；frontier 失敗 ≥3 = ill-posed，停並重述（無升級路）。

## Model 路由表（需求 2，依 model-selection-grid）

| 獨立位置數 / 信號 | model | effort | mode |
|------|-------|--------|------|
| 0–1 | haiku | low | cost |
| 2–5 | sonnet | medium–high | quality |
| 6–9 | sonnet | high | quality |
| 10+ / 跨模組 | sonnet→opus | xhigh | ceiling |
| 架構/安全設計關鍵字 | opus | xhigh | ceiling |
| 最難架構+長程 agentic / opus 不收斂 | claude-fable-5 | high | frontier |

定價錨點（per 1M in/out，2026-05-30 雙源）：Haiku $1/$5 · Sonnet $3/$15 · Opus $5/$25 · Fable $10/$50（effective ≈2.6× Opus）。Opus 僅 1.67× Sonnet → ceiling 任務不必恐懼成本。

## Context 不爆 / 不衰退（需求 2）

- **可靠工作區**：1M 名義 context 實際可靠僅 64–128K（lost-in-the-middle U 型偏差）→ 主對話只收 worker 摘要，重讀全委派。
- **NLAH**：goal 放 HEAD、最新工具輸出放 TAIL。
- **Compaction**：行為信號（迷失問句）> 數字（一般 70%、長 agentic 30–35%）；compact 必用相同 system prompt+tools（否則 cache 失效）。
- **防衰退關鍵**：`claude-progress.json` 外存 goal+成功條件+進度，每 `/loop` fire 重讀（fresh context 不依賴記憶）。

## /loop ⊗ The Loop 接線（需求核心）

本機 CLI：`/loop 30m multi-mode <task>`。每 fire 全新 context，故 prompt 自包含：
OBSERVE 讀 progress → router 選 model/mode → inline/spawn worker 跑六階段 → 主對話親跑確定性 gate 升 verified → RECORD 更新 progress；委派 `self-escalate` 判收斂，`converged && confidence≥0.85` → 建議 `CronDelete <job-id>` 停 loop。recurring task 7 天自動過期。

## 補充缺口（需求 5）

設計過程發現並補上的不完備處：

1. **缺 sub-agent 可攜的紀律載體** — 既有 4 pilot 全是 SKILL，沒有任何 sub-agent 能在委派狀態套用其紀律。multi-mode-agent 填此空缺。
2. **缺自動 model router** — model-selection-grid 是「人讀的決策表」，無自動執行體。multi-mode-skill §1 將其轉成可執行路由。
3. **缺破-4 fan-out 的明確姿勢** — 規則散在 subagent-strategy:16 + harness-meta GOTCHAS，無單一入口。本設計集中為 §3。
4. **`refs/` 路徑漂移**（回報，未修）：subagent-strategy.md 引用 `refs/error-handling.md`、core.md 引用 `refs/harness-loop.md`，實際在 `.claude/refs/`。屬任務外，記錄不順手改（commit 原子性）。

## 驗證（TEST）

```
$ bash scripts/healthcheck.sh | tail -4
======================================
 統計結果：PASS: 128  WARN: 2  FAIL: 0
======================================
健康檢查完成，有 2 個警告項目。
```

- FAIL: 0（修復了「RESOLVER.md 未登錄 multi-mode-skill」一項）。
- 2 WARN 為既有（MCP servers 空），與本變更無關。
- frontmatter 比對：agent 用 `name/description/tools/model/permissionMode/isolation`（match implementer）；skill 用 `name/description/version/roster-trigger/roster-domain/allowed-tools/review-by`（match haiku-pilot）。

## 限制與後續

- **排程不可用於本環境**：CronCreate/ScheduleWakeup 僅本機/桌面；遠端 web 退化單輪。已誠實標注，未偽造。
- **dynamic workflow 可用性未驗**：為 Opus 4.8 runtime 功能，依 plan/mode（Max/Team/Enterprise 預設；Pro 需 /config）。採信 worker verdict 前主對話須機械 grep 重驗。
- 後續可選：寫 eval（eval-designer）量化「router 選對 model 的命中率」作為回歸閘門。
