---
title: Thariq Claude Code Tips — Skill 設計、Session 管理與 Prompt Caching
source: shanraisshan/claude-code-best-practice · Thariq
type: best-practices
---

# Thariq Claude Code Tips — Skill 設計、Session 管理與 Prompt Caching

> 來源：shanraisshan/claude-code-best-practice · Thariq (@trq212, Anthropic Claude Code 核心團隊)
> 收錄日期：2026-05-16（初次：2026-05-01）
> 涵蓋：
> - 2026-03-17: Skill 設計深度指南（9 種類型 + T1-T9 設計原則）
> - 2026-04-16: Session 管理與 1M Context 指南
> - 2026-04-30: Prompt Caching 核心教訓（官方 blog 文章）

---

## 一、Skill 設計原則（T1-T9）

### 前言

Skills 的常見誤解是「只是 markdown 檔案」，但最有趣的部分是它們是**資料夾**，可以包含 scripts、assets、data 等 — agent 可以探索和操作的東西。Anthropic 內部有數百個 skills 在活躍使用中。

### T1: 不要陳述顯而易見的事

Claude Code 對你的 codebase 知道很多，Claude 對程式設計也知道很多，包括許多預設意見。如果你的 skill 主要是關於知識，聚焦在**推動 Claude 超出正常思維方式的資訊**。

範例：frontend-design skill 是透過與用戶迭代改善 Claude 的設計品味而建立的 — 避免 Inter 字體和紫色漸層等經典 AI 生成設計模式。

### T2: 建立 Gotchas 區段

Skill 中信號密度最高的內容是 Gotchas 區段。這些區段應該從 Claude 使用你的 skill 時遇到的常見失敗點中累積。隨時間更新 skill 來捕捉這些 gotchas。

### T3: 使用檔案系統與 Progressive Disclosure

Skill 是資料夾，不只是 markdown 檔案。把整個檔案系統視為 context engineering 和 progressive disclosure 的形式：

- 告訴 Claude 你的 skill 中有哪些檔案，它會在適當時機讀取它們
- 最簡單的形式：指向其他 markdown 檔案（例如把詳細函式簽名和使用範例拆到 `references/api.md`）
- 可以有 references、scripts、examples 等資料夾

```
skills/my-skill/
  SKILL.md            ← 核心指引和 TOC
  references/api.md   ← 詳細 API 文件
  scripts/helper.sh   ← 可執行腳本
  examples/           ← 使用範例
```

### T4: 避免 Railroading Claude

Claude 通常會嘗試遵循你的指示，因為 skills 非常可重用，要小心過於具體：

- 給 Claude 它需要的資訊，但給它**適應情況的靈活性**
- 不要開出逐步的詳細指示，**給目標和限制**
- 過度具體的 skill 在邊界情況會失敗

### T5: 思考 Setup

有些 skill 需要用戶的 context 才能運作。好的模式是在 skill 目錄中儲存 `config.json`：

- 如果 config 未設定，agent 可以詢問用戶資訊
- 可以指示 Claude 使用 AskUserQuestion tool 進行結構化、多選問題

```json
// skills/my-skill/config.json
{
  "target_service": "",
  "environment": "staging"
}
```

### T6: Description 欄位是寫給模型的

Claude Code 啟動 session 時，會建立所有可用 skill 及其 description 的列表。這個列表是 Claude 掃描「有沒有適合這個請求的 skill？」的依據。

**description 欄位不是摘要 — 它是觸發條件的描述。為模型寫它。**

```yaml
description: |
  Use when deploying to production. Triggers on: "deploy", "push to prod",
  "release to live". Do NOT use for: staging deploys, local testing.
```

### T7: Memory 與資料儲存

有些 skill 可以透過儲存資料來包含記憶：

- 簡單：append-only text log 或 JSON 檔案
- 複雜：SQLite 資料庫

**重要**：skill 目錄中的資料在升級 skill 時可能被刪除。使用 `${CLAUDE_PLUGIN_DATA}` 作為穩定的每個 plugin 資料儲存資料夾。

### T8: 儲存 Scripts 與生成程式碼

給 Claude 最強大的工具之一是**程式碼本身**。提供 scripts 和 libraries 讓 Claude 把 turns 花在組合和決策上，而不是重建 boilerplate：

- Claude 可以即時生成 scripts 來組合這些功能進行更進階的分析
- Scripts 提供確定性的操作，降低 Claude 犯錯的機率

### T9: 按需 Hooks（On Demand Hooks）

Skills 可以包含只在 skill 被呼叫時啟動、持續到 session 結束的 hooks。適合不想一直執行但有時極有用的 opinionated hooks：

- `/careful` — 透過 PreToolUse matcher 阻擋 `rm -rf`、`DROP TABLE`、force-push、`kubectl delete`
- `/freeze` — 阻擋任何不在特定目錄的 Edit/Write

---

## 二、9 種 Skill 類型

Anthropic 團隊整理所有 skills 後，發現它們聚集成 9 個類別。最好的 skills 清楚屬於其中一類；令人困惑的往往橫跨多類。

### 類型 1: Library & API Reference（函式庫 API 參考）

解釋如何正確使用函式庫、CLI 或 SDK 的 skills：
- 適合內部函式庫或 Claude 有時有困難的常用函式庫
- 通常包含參考程式碼片段資料夾和要避免的 gotchas 列表

**範例**：`billing-lib`、`internal-platform-cli`、`frontend-design`

### 類型 2: Product Verification（產品驗證）

描述如何測試或驗證程式碼正確性的 skills：
- 通常配合 Playwright、tmux 等外部工具
- 驗證 skills 對確保 Claude 輸出正確極有價值
- **值得讓工程師花一週時間把驗證 skills 做到優秀**

**範例**：`signup-flow-driver`、`checkout-verifier`、`tmux-cli-driver`

### 類型 3: Data Fetching & Analysis（資料抓取與分析）

連接到你的資料和監控 stack 的 skills：
- 可能包含帶 credentials 的資料抓取 libraries、特定 dashboard ID
- 以及常見工作流程或資料取得方式的說明

**範例**：`funnel-query`、`cohort-compare`、`grafana`

### 類型 4: Business Process & Team Automation（業務流程與團隊自動化）

將重複工作流程自動化為單一命令的 skills：
- 通常是相對簡單的指示，但可能對其他 skills 或 MCP 有更複雜的依賴
- 在 log 檔案中儲存先前結果可幫助模型保持一致性並反思先前執行

**範例**：`standup-post`、`create-<ticket-system>-ticket`、`weekly-recap`

### 類型 5: Code Scaffolding & Templates（程式碼 Scaffolding 與模板）

為 codebase 中特定功能生成框架 boilerplate 的 skills：
- 可以與可組合的 scripts 結合
- 在 scaffolding 有自然語言需求（純程式碼無法完全涵蓋）時特別有用

**範例**：`new-<framework>-workflow`、`new-migration`、`create-app`

### 類型 6: Code Quality & Review（程式碼品質與審查）

在你的組織中強制執行程式碼品質並幫助 review 程式碼的 skills：
- 可以包含確定性 scripts 或工具以獲得最大穩健性
- 可以作為 hooks 的一部分或在 GitHub Action 中自動執行

**範例**：`adversarial-review`、`code-style`、`testing-practices`

### 類型 7: CI/CD & Deployment（CI/CD 與部署）

幫助你在 codebase 中 fetch、push 和部署程式碼的 skills：
- 這些 skills 可能引用其他 skills 來收集資料

**範例**：`babysit-pr`、`deploy-<service>`、`cherry-pick-prod`

### 類型 8: Runbooks（運行手冊）

接受症狀（如 Slack thread、alert 或錯誤特徵），走過多工具調查，並產出結構化報告的 skills：

**範例**：`<service>-debugging`、`oncall-runner`、`log-correlator`

### 類型 9: Infrastructure Operations（基礎設施操作）

執行例行維護和操作程序的 skills — 部分涉及受益於 guardrails 的破壞性操作：

**範例**：`<resource>-orphans`、`dependency-management`、`cost-investigation`

---

## 三、Skill 分發與治理

### 兩種分發方式

1. **Check in 到 repo**（放在 `.claude/skills/` 下）— 適合在少數 repo 工作的小型團隊
2. **建立 plugin** 並有 Claude Code Plugin marketplace — 規模化時的選擇

每個 check in 的 skill 都會讓模型的 context 增加一點。規模化時，內部 plugin marketplace 讓你分發 skills 並讓團隊決定安裝哪些。

### Marketplace 管理

沒有集中的團隊決定哪些 skills 進入 marketplace。做法：
1. 上傳到 GitHub 的 sandbox 資料夾
2. 在 Slack 或論壇推廣
3. 一旦 skill 獲得足夠關注（由 skill 擁有者決定），提 PR 移入 marketplace
4. 在發布前進行策展，避免冗餘 skills

### Skill 組合

Skills 可以互相依賴。直接在 skill 中按名稱引用其他 skills，模型會在安裝時呼叫它們：

```markdown
此 skill 依賴 `file-upload` skill 來上傳結果。
請確保已安裝 `file-upload` skill。
```

### 量測 Skills

使用 `PreToolUse` hook 記錄 skill 使用狀況：
- 找出受歡迎的 skills
- 發現觸發率低於預期的 skills

---

## 四、Session 管理（1M Context 時代）

### Context Rot 原理

「Context window 是模型在生成下一個回應時能『看到』的一切。」包含：system prompts、對話歷史、tool calls、檔案讀取。

**Context rot**：隨著 context 增長，模型效能下降，因為注意力分散在更多 tokens 上。1M context 模型通常在約 300-400k tokens 開始出現，但依任務類型而異。

### 每個 Turn 都是分支點

Claude 完成一個 turn 後，有幾個選擇：

| 情況 | 使用 | 原因 |
|------|------|------|
| 同一任務、context 仍相關 | **Continue** | 所有內容仍 load-bearing，不要白花錢重建 |
| 走錯路徑 | **Rewind**（Esc Esc）| 保留讀取，丟掉失敗，用所學重新 prompt |
| 中途 session 膨脹 | **/compact \&lt;hint\>** | 低 effort；Claude 決定相關性 |
| 開始新任務 | **/clear** | 零 rot；完全控制帶入的 context |
| 下一步會產生大量中間輸出 | **Subagent** | 中間雜訊留在 child context |

### 何時開新 Session

「當你開始新任務，你也應該開新 session。」

灰色地帶：相關任務需要部分但非全部 context，例如為剛實作的功能寫文件。

### Rewind 優於口頭修正

不要在失敗嘗試後口頭說「那個沒用，試 X」（失敗嘗試仍留在 context 污染後續）。

Rewind 移除失敗並用學到的資訊重新 prompt。「Summarize from here」功能建立 handoff messages，記錄嘗試過什麼和為什麼失敗。

### Compact vs 清空重開

| | `/compact` | `/clear` + 手寫摘要 |
|---|------------|---------------------|
| 誰寫摘要 | Claude 自動 | 你自己 |
| 損失 | lossy（可能漏關鍵）| 零 rot |
| 成本 | 低（自動）| 高（人工寫摘要）|
| 控制度 | 可用 hint 引導 | 完全自控 |

**Bad compact 的成因**：autocompact 在 context rot 最嚴重時觸發 — 模型此時最不聰明，可能丟掉關鍵細節。

### Subagents — Context 管理的形式

「Subagents 是 context 管理的一種形式，在你提前知道一塊工作會產生大量不需要再用的中間輸出時很有用。」

Subagents 有自己的新鮮 context windows，只把最終報告回傳給 parent context。

**Mental test**：「我需要這個工具輸出本身，還是只需要結論？」
- 只需要結論 → 委派 subagent
- 需要反覆檢視中間產物 → 主對話自己做

---

## 五、工程哲學

### Unhobbling — 移除不必要的限制

傳統軟體工具是為人類設計的，為人類建立了很多 guardrails 和限制。當 AI agent 使用這些工具時，這些限制可能反而成為障礙。

設計供 agent 使用的 skills/tools 時，問：「這個限制是為了保護人類免於錯誤，還是為了保護系統？」保護系統的限制通常 agent 不需要；保護人類決策完整性的限制可能需要保留或以新方式實現。

### Delete-and-Rebuild（重建優於修補）

當你的 Claude 設定開始感覺像是在修補修補的修補時，考慮從頭重建：
- Skills 從一個 SKILL.md 和單一 gotcha 開始
- 隨著 Claude 碰到新邊界情況而逐漸改善
- 不要害怕刪掉已過時的 skills 並重建更清晰的版本

「我們大多數的 skills 從幾行和一個 gotcha 開始，因為人們不斷加入 Claude 碰到的新邊界情況而變得更好。」

### Seeing like an Agent（以 Agent 的視角看問題）

設計 skills 時，想象 Claude 在看到這個 skill 時的視角：
- 它會在什麼情況下觸發這個 skill？（description 欄位的重要性）
- 它需要什麼資訊才能成功？（避免過度詳細或過度簡略）
- 什麼情況會讓它失敗？（Gotchas 區段的來源）

Anthropic 的 frontend-design skill 就是這個哲學的體現：不是列出所有設計規則，而是聚焦在 Claude 最常犯的、最需要被糾正的特定錯誤上。

---

---

## 三、Prompt Caching 心法（2026-04-30 官方 Blog）

> 來源：https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything  
> 完整分析見：`research/best-practices/28-thariq-prompt-caching-lessons.md`

### 核心立場

Claude Code 團隊將 **Cache Hit Rate 視為關鍵指標，下降時觸發 incident**。不是優化項，是生產系統基本健康指標。

### 分層結構（靜態 → 動態）

```
1. System prompt + Tools       ← 最穩定，全域快取
2. 專案特定檔案 / CLAUDE.md   ← 跨 session 快取
3. Session context             ← 僅當次 session
4. 對話訊息（最新輪次）        ← 每次請求不同
```

越靠前越穩定，快取效益越高。

### 五個禁止事項

| 禁止 | 原因 | 正確做法 |
|------|------|---------|
| 動態更新 system prompt | 前綴失效 | 用 `<system-reminder>` 注入動態資訊 |
| Mid-session 切換模型 | 快取模型專屬 | 用 Subagent 處理需不同模型的任務 |
| 對話中增刪工具 | 前綴失效 | stub + `defer_loading: true` |
| Compact 時改 system prompt | 後續快取失效 | Compact 保留完全相同的 system prompt + tools |
| 忽略 cache hit rate | 沉默降解 | 加入 observability dashboard |

### 關鍵引言

> 「Cache rules everything. We treat it like uptime. When it drops, we have an incident.」
> — Thariq Shihipar, Claude Code MTS

---

## 附錄：Thariq 在 Workspace Rules 中的引用

以下是已整合到本 workspace 規則中的 Thariq 觀點，供對照：

- **Context rot 閾值**（300-400k tokens）→ `.claude/rules/context-management.md`
- **Subagent mental test**（conclusion vs. tool output）→ `.claude/rules/subagent-strategy.md`
- **Prompt caching 架構規則**（static first, dynamic last）→ `.claude/rules/context-management.md`
- **1M context + compact 策略**（壓縮層級決策表）→ `.claude/rules/context-management.md`
- **Session branching point**（每個 turn 的六個選擇）→ `.claude/rules/session-management.md`
- **Forked Subagent / context 繼承**（v2.1.117）→ `.claude/rules/subagent-advanced.md`
- **Prompt caching 五禁止事項**（2026-04-30）→ `28-thariq-prompt-caching-lessons.md`
