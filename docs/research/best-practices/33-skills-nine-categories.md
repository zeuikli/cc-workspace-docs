# Skills 九大類別與 Analytics Agent 設計指南

> 來源：  
> - [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)（2026-06-03）  
> - [How Anthropic enables self-service data analytics with Claude](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)（2026-06-03）  
> 整理日期：2026-06-05

---

## 九大 Skill 類別（Anthropic 內部分類）

| # | 類別 | 說明 | 範例 |
|---|------|------|------|
| 1 | **Library & API Reference** | 內部/外部函式庫文件，含 edge case 和 gotchas | 內部 SDK 使用、第三方 API 怪癖 |
| 2 | **Product Verification** | 測試與驗證流程，可量化品質影響 | 功能測試、UI 驗收 |
| 3 | **Data Fetching & Analysis** | 連接資料與監控基礎架構 | DB 查詢、指標取得 |
| 4 | **Business Process Automation** | 重複工作流自動化為單一指令 | 日報生成、審批流 |
| 5 | **Code Scaffolding & Templates** | 框架樣板 + 自然語言需求 | 新服務初始化、API endpoint 生成 |
| 6 | **Code Quality & Review** | 品質強制與 code review 輔助 | 風格檢查、PR review |
| 7 | **CI/CD & Deployment** | 程式碼管理與部署協調 | 自動部署、rollback |
| 8 | **Runbooks** | 多工具調查工作流 → 結構化報告 | 事件處理 SOP、on-call 指南 |
| 9 | **Infrastructure Operations** | 日常維護與操作程序 | 資源清理、健康檢查 |

---

## Skill 設計核心原則

### 避免的常見錯誤

> "A skill that restates what Claude would do by default adds context without adding value."

- **不要**重述 Claude 預設就會做的事
- **不要**過度指定指令（限制 Claude 靈活性）
- **不要**只做 markdown 文件（Skill 是完整資料夾：腳本、模板、資源）

### 必做的事

- 從實際失敗點累積「Gotchas」section
- 用 progressive disclosure（巢狀子檔案）逐步揭露 context
- description 針對模型決策，不是人類閱讀

### 進階功能

- **On-demand hooks**：依情況觸發工具（PreToolUse 守護破壞性操作）
- **Assets 資料夾**：輸出生成用的模板
- **Persistent storage**：`${CLAUDE_PLUGIN_DATA}` 跨 session 記憶
- **Execution logs**：讓 agent 參考之前的工作記錄

---

## Skill 資料夾結構

```
my-skill/
├── SKILL.md         # 主指令（含 description、Gotchas、Trigger conditions）
├── config.json      # 使用者特定 context 設定
├── assets/          # 輸出模板
├── scripts/         # 可重複使用腳本（組合 > 樣板重建）
└── logs/            # 執行歷史（透過 ${CLAUDE_PLUGIN_DATA}）
```

---

## Analytics Agent 特殊設計模式

Analytics agent 與 coding agent 有根本差異：有「唯一正確答案」，失敗模式不同。

### 三大失敗模式

| 失敗模式 | 說明 | 解法 |
|---------|------|------|
| 概念模糊 | "active users" → 多個候選欄位 | Semantic layer 消除歧義 |
| 資料過期 | Schema、定義持續變動 | 元資料視為產品維護 |
| 檢索失敗 | 正確資料存在但找不到 | Skills 提升可發現性 |

### 準確率對比

| 配置 | 準確率 |
|------|------|
| 無 Skills | ≤21% |
| 有 Skills | ≥95% |
| 加入 adversarial review sub-agent | +6%（但 +32% 延遲） |

### 四層 Analytics Stack

1. **Data Foundations** — Canonical datasets、強制標準、colocated artifacts、metadata-as-product
2. **Sources of Truth** — Semantic layer、lineage graphs、query corpora、business context
3. **Skills** — 領域知識 skill + unbook（程序 skill）配對
4. **Validation** — 離線 eval、ablation study、線上監控、adversarial review

### Skills 配對模式

```
知識 Skill（Knowledge Router）
  → 薄層，路由到正確 unbook
  → 記錄：概念、grain、exclusions、gotchas、模式

程序 Skill（Unbook）
  → 詳細步驟，含 SQL 範例和錯誤處理
  → 與 transformation code 共置（data PR 自動同步）
```

### CI 整合

~90% 的 data PR 現在包含 skill 修改；CI flag 會在模型修改但未更新文件時報警。

---

## 發布與擴散

**內部實踐：**
- 直接 commit 至 `./.claude/skills/`
- 內部 plugin marketplace 跨團隊共享
- Sandbox 資料夾有機採用 → 達到一定使用量後升級為官方

**使用量追蹤：**
透過 `PreToolUse` hook 記錄 skill 呼叫次數，識別高人氣和低使用率 skill。
