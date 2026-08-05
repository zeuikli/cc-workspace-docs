# Lecture 07：Skills 設計與 Progressive Disclosure

## 學習目標

完成本課後，你將能夠：

- 說明 Skill 在七種行為調整機制中的位置，以及何時該選 Skill 而非 CLAUDE.md / Hook / Subagent
- 用 Anthropic 內部的九大類別為自己的 Skill 分類，避免寫出「重述 Claude 預設行為」的空 Skill
- 依任務脆弱度校準指令自由度（高／中／低）
- 用 Progressive Disclosure 把超過 500 行的 Skill 拆成不會炸 context 的結構
- 用 Claude A / Claude B 方法迭代 Skill，並以評估先行取代憑感覺調整

## 核心概念

### Skill 在機制光譜上的位置

官方把「自訂 Claude Code 行為」歸納為七種機制。選擇的第一個問題不是「怎麼寫 Skill」，而是「這件事該用哪個機制」：

| 要改變的東西 | 機制 |
|-------------|------|
| Claude **知道**什麼（永久） | CLAUDE.md |
| Claude 知道什麼（路徑條件式） | `.claude/rules/`（path-scoped rules）|
| Claude **會做**什麼（可重用流程、參考資料） | **Skills** |
| Claude 在**哪個 context** 做 | Subagents |
| Claude **呼叫**什麼外部工具 | MCP |
| 生命週期事件**一定**要發生的事 | Hooks |
| Claude 回應**長什麼樣** | Output Styles / System Prompt Appending |

最容易搞混的是 Skill 與 Hook。差別在確定性：

> CLAUDE.md 或 Skill 裡的「絕不編輯 `.env`」是**請求**，不是保證。`PreToolUse` hook 封鎖編輯才是**強制執行**。如果規則必須每次都成立，做成 hook 而非 prompt 指令。

以及 Skill 與 Subagent：Skill 是「內容」（跨 context 共享的指令與知識），Subagent 是「容器」（獨立 context 的 worker）。兩者可以組合——subagent 可用 `skills:` 欄位預載特定 Skill，Skill 也可用 `context: fork` 在隔離 context 中執行。

### Context 成本對照

選機制時真正該算的帳是 context 成本：

| 機制 | 載入時機 | 載入什麼 | Context 成本 |
|------|---------|---------|------------|
| CLAUDE.md | Session start | 完整內容 | 每個 request 都付 |
| **Skills** | Session start + 使用時 | 描述在 start，全文在觸發時 | 低（只有描述常駐）|
| MCP servers | Session start | Tool names；schema 按需 | 低（直到工具被用）|
| Subagents | Spawn 時 | 獨立新 context | 與主 session 隔離 |
| Hooks | 事件觸發時 | 不載入任何東西 | 零（除非 hook 回傳輸出）|

設 `disable-model-invocation: true` 可讓 Skill 完全對 Claude 隱藏、直到你手動 `/name` 呼叫——context 成本歸零。

### 九大 Skill 類別（Anthropic 內部分類）

用這張表檢查你想寫的東西「算不算一個 Skill」。落不進任何一類，通常代表它該是 CLAUDE.md 的一行、或根本不需要存在：

| # | 類別 | 範例 |
|---|------|------|
| 1 | Library & API Reference | 內部 SDK 用法、第三方 API 怪癖與 edge case |
| 2 | Product Verification | 功能測試、UI 驗收流程 |
| 3 | Data Fetching & Analysis | DB 查詢、指標取得 |
| 4 | Business Process Automation | 日報生成、審批流 |
| 5 | Code Scaffolding & Templates | 新服務初始化、endpoint 生成 |
| 6 | Code Quality & Review | 風格檢查、PR review |
| 7 | CI/CD & Deployment | 自動部署、rollback |
| 8 | Runbooks | 事件處理 SOP、on-call 指南 |
| 9 | Infrastructure Operations | 資源清理、健康檢查 |

### 最重要的一句話

> "A skill that restates what Claude would do by default adds context without adding value."

**預設假設是「Claude 已經非常聰明」**，Skill 只補 Claude 沒有的脈絡。三個常見錯誤：

- 重述 Claude 預設就會做的事（無效 context）
- 過度指定指令，限制 Claude 的靈活性
- 只寫一份 markdown——Skill 是完整資料夾（腳本、模板、資源、執行紀錄）

### 自由度校準：窄橋 vs 開闊平原

指令的自由度應該由**任務的脆弱度**決定，不是由你想寫多細決定：

| 類型 | 什麼時候用 | 格式 |
|------|-----------|------|
| **高自由度** | 多種做法都有效、需依情境判斷 | 純文字指令 + persona |
| **中自由度** | 有偏好模式但可調整 | Pseudocode + 參數化腳本 |
| **低自由度** | 操作脆弱、順序關鍵 | 精確腳本，明確禁止修改命令 |

比喻：**窄橋兩側有懸崖**（DB migration、破壞性操作）→ 低自由度，逐步精確；**開闊平原無障礙**（code review、分析）→ 高自由度，給方向即可。

### Description 是選擇引擎，不是說明文件

Claude 從上百個 Skill 中挑一個的唯一依據就是 description。它必須包含**做什麼 + 何時用 + 何時不用**，並且永遠用第三人稱：

```yaml
# 差
description: "API convention checker for REST endpoints"

# 好
description: |
  REST API 設計慣例審查。
  Make sure to use this skill whenever designing or reviewing REST endpoints.
  Do NOT use for: gRPC、GraphQL、SDK 設計、前端元件
```

**字元預算**：description 上限 1,024 字元；Claude Code 對 description + when_to_use 合計的截斷限制約 1,536 字元。

**命名慣例**：優先動名詞（gerund）形式——`processing-pdfs`、`analyzing-spreadsheets`；可接受 `pdf-processing`；避免 `helper`、`utils`、`documents` 這種零資訊的名字。名稱 ≤64 字元、小寫英數與連字號、不得含 `anthropic` / `claude`。

### Progressive Disclosure：把 SKILL.md 當成目錄

| SKILL.md 長度 | 策略 |
|---------------|------|
| < 300 行 | 保持單檔，持續補 Gotchas 與 Examples |
| 300–500 行 | 開始識別可拆出的 Reference |
| **> 500 行** | **必須拆**：SKILL.md 只留 TOC + 核心流程 |

```
pdf/
├── SKILL.md              # 入口，≤500 行，觸發時載入
├── FORMS.md              # 表單填寫指南（需要時才讀）
├── reference.md          # API 參考（需要時才讀）
└── scripts/
    ├── analyze_form.py   # 執行，不載入內容
    └── validate.py
```

三個關鍵限制：

1. **避免深層參考鏈**。Claude 遇到多層 reference 可能只用 `head -100` 預覽而非完整讀取。`SKILL.md → advanced.md（直接有資訊）` 可以；`SKILL.md → advanced.md → details.md → 實際資訊` 不行。
2. **超過 100 行的 reference 檔案頂部加 TOC**，確保部分讀取時仍看得到完整範圍。
3. **腳本只有輸出進 context**，內容不進——把重複邏輯放進 `scripts/` 是最省 context 的做法。

### 規則要寫原因，不要寫命令

```
❌ MUST use constructor injection. NEVER use field injection.

✅ Use constructor injection. Field injection breaks testability
   because we cannot mock the field without Spring context.
```

這一條與 Claude 5 世代的 context engineering 方向一致（見 [Lecture 03](/lectures/lecture-03-context-engineering/)）：**judgment over rules**。給模型判斷依據，比給它一條它無法評估邊界的禁令有效。

### 量化效果：Skills 值多少

Anthropic 自家 analytics agent 的實測：

| 配置 | 準確率 |
|------|--------|
| 無 Skills | ≤21% |
| 有 Skills | ≥95% |
| 再加 adversarial review sub-agent | +6%（代價：+32% 延遲）|

這是 21% → 95% 的差距，而且模型沒換。這是 Harness 工程投報率的又一個直接證據。

### 評估先行，不要憑感覺迭代

**先建評估，再寫文件**——確保你解決的是真實問題而非預想問題：

1. 識別 gap（無 Skill 時 Claude 的實際失敗點）
2. 建 3 個測試場景
3. 建立 baseline（沒有 Skill 時的表現）
4. 寫**最少**的文件通過測試
5. 迭代

### Claude A / Claude B 開發法

- **Claude A**：協助設計與精煉 Skill（有完整對話脈絡）
- **Claude B**：全新 session + 該 Skill，執行真實任務（測試效果）

流程：先在沒有 Skill 的情況下完成一次任務，注意你**自然提供了哪些脈絡**；請 Claude A 把這些脈絡打包成 Skill；請 Claude A 刪掉「Claude 本來就知道」的部分；用 Claude B 測；帶著 B 的行為觀察回到 A 迭代。

觀察 Claude 如何導航 Skill 時要注意四個訊號：

| 觀察到 | 意義 |
|--------|------|
| 意外的探索路徑 | 結構不直覺 |
| 遺漏某個 reference 連結 | 連結不夠明顯 |
| 反覆讀同一個檔案 | 該內容應移進主 SKILL.md |
| 某個檔案從未被讀取 | 可能不必要 |

## 程式碼範例

### 一個完整的 SKILL.md 骨架

```markdown
---
name: reviewing-migrations
description: |
  審查資料庫 migration 的安全性與可回滾性。
  Make sure to use this skill whenever a migration file under db/migrations/ is
  created or modified, or when the user mentions schema changes.
  Do NOT use for: 一般 SQL 查詢優化、ORM model 定義、seed data。
allowed-tools: Read, Grep, Glob, Bash
disable-model-invocation: false
user-invocable: true
---

# Migration 審查

## 適用前提

當前分支：`!git branch --show-current`
變更的 migration：`!git diff --name-only main -- db/migrations/`

## 檢查流程（低自由度：逐項執行，不要跳步）

複製此 checklist 並逐步勾選：

- [ ] Step 1：確認每個 migration 都有可執行的 `down`
- [ ] Step 2：`python scripts/check_backfill.py <file>` 檢查 drop column 是否有 backfill
- [ ] Step 3：確認索引建立使用 `CONCURRENTLY`（PostgreSQL）
- [ ] Step 4：確認新欄位為 nullable 或有 default（向後相容）
- [ ] Step 5：驗證失敗 → 修正 → 回到 Step 2 重跑，通過才繼續

## Rules

- Drop column 必須先有一版只停止寫入、不刪欄位的 migration。
  原因：rollback 時舊版程式碼仍會讀該欄位，直接 drop 無法回滾。
- 索引建立不加 `CONCURRENTLY` 會鎖表。
  原因：2026-03 一次 500 萬列的表建索引造成 4 分鐘寫入阻塞。

## Known Gotchas

- alembic 的 `op.alter_column` 在 PostgreSQL 上對 type 變更會重寫整張表——大表要改用
  「新增欄位 + backfill + 切換 + 刪舊欄位」四步法。
- 詳細的四步法見 [FOUR-STEP.md](FOUR-STEP.md)。
```

### Shell 動態注入（保持確定性）

```markdown
當前 git branch：`!git branch --show-current`
最後一次 commit：`!git log --oneline -1`
```

`` !`command` `` 在 Skill 觸發時由 harness 執行，結果插入 prompt——**不是** Claude 執行，所以結果是確定的。

### Plan-Validate-Execute Pattern（批量／高風險操作）

```
1. Claude 分析任務 → 產出 changes.json 計畫檔（無副作用）
2. 驗證腳本檢查計畫（無副作用）
3. 計畫通過才執行
```

驗證腳本的錯誤訊息要具體到可以直接修：

```
✅ "Field 'signature_date' not found. Available fields: customer_name, order_total, signature_date_signed"
❌ "Invalid field"
```

### 腳本：解決問題，不要推回給 Claude

```python
# 好：明確處理錯誤
def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, "w") as f:
            f.write("")
        return ""

# 差：失敗就讓 Claude 想辦法
def process_file(path):
    return open(path).read()
```

以及避免魔法數字——Skill 腳本會被 Claude 讀，數字沒有理由等於 Claude 不知道能不能改：

```python
REQUEST_TIMEOUT = 30  # HTTP requests typically complete within 30 seconds
MAX_RETRIES = 3       # Three retries balances reliability vs speed
```

### 評估場景檔

```json
{
  "skills": ["reviewing-migrations"],
  "query": "Review the migration in db/migrations/0042_drop_legacy_email.py",
  "files": ["db/migrations/0042_drop_legacy_email.py"],
  "expected_behavior": [
    "Flags the DROP COLUMN as unsafe because no backfill or two-phase plan exists",
    "Points to the specific line number of the drop statement",
    "Proposes the four-step add/backfill/switch/drop sequence"
  ]
}
```

### MCP 工具在 Skill 中的引用格式

```markdown
Use the BigQuery:bigquery_schema tool to retrieve table schemas.
Use the GitHub:create_issue tool to create issues.
```

格式是 `ServerName:tool_name`——不加前綴 Claude 可能找不到工具。

## 常見問題與注意事項

**Q：Skill 和 CLAUDE.md 的界線到底在哪？**

A：用觸發點判斷。「Claude 同一個慣例犯錯兩次」→ CLAUDE.md；「你第三次把同樣的 playbook 貼進對話」→ Skill。前者是常駐規則，後者是按需流程。CLAUDE.md 控制在 200 行以內，長出來的參考資料就該搬進 Skill。

**Q：Skill 太多會不會反而拖慢選擇？**

A：會。企業治理指南提到 Recall 上限是**每個 request 最多召回 8 個 Skill**。Skill 數量成長後，description 的區辨力（尤其是排除條件 `Do NOT use for:`）比 Skill 本身的內容更決定成敗。

**Q：Nested skills 目錄可以用嗎？**

A：可以，v2.1.178 起 `.claude/skills/backend/postgres/` 這種子目錄會被載入，名稱衝突時以 `<dir>:<name>` 格式顯示。

**Q：怎麼知道哪些 Skill 沒人用？**

A：用 `PreToolUse` hook 記錄 skill 呼叫次數。Anthropic 內部就是這樣識別高人氣與低使用率 Skill 的。`/usage` 也會顯示 skill / subagent / plugin / MCP server 各自消耗的配額。

**Q：Skill 該跨模型測試嗎？**

A：該。同一份 Skill 對 Haiku 可能指引不足、對 Opus 可能過度解釋。至少在你實際會用的兩個檔位上各跑一次評估場景。

**Q：時效性資訊怎麼寫？**

A：不要寫「如果是 2026 年 8 月前，用舊 API」這種句子——它一定會過時而且沒人會回來刪。正確做法是把舊做法收進 `<details>` 折疊區塊，正文只留現行做法。

## 本課小結

- **先選機制再寫內容**：規則必須每次成立 → Hook；常駐事實 → CLAUDE.md；可重用流程與參考資料 → Skill；需要隔離 context → Subagent。
- **Skill 的價值來自「Claude 沒有的脈絡」**。重述預設行為的 Skill 只增加 context、不增加價值。
- **自由度由脆弱度決定**：窄橋（DB migration）給精確腳本，開闊平原（code review）給方向即可。
- **Description 是選擇引擎**：做什麼 + 何時用 + **何時不用**，第三人稱，≤1,024 字元。
- **超過 500 行必須 Progressive Disclosure**，且參考鏈只能一層深。
- **量化效果**：analytics agent 準確率 21% → 95%，模型沒換。
- **評估先行 + Claude A/B 迭代**，取代憑感覺調整。

## 延伸閱讀

- [Lecture 02：CLAUDE.md 設計](/lectures/lecture-02-claude-md/) — Skill 與 CLAUDE.md 的分工
- [Lecture 08：Sub-agents、Agent Teams 與 Dynamic Workflows](/lectures/lecture-08-subagents-workflows/) — Skill 與 Subagent 的組合
- [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/) — 把驗證編碼成 Skill
**官方一手來源**

- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)（2026-06-03）— 九大類別、21%→95% 數據
- [Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)（2026-06-18）— 七種機制選擇框架
- [Agent Skills Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — 自由度校準、Progressive Disclosure、Claude A/B 迭代
- [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude)（2026-01-29）
- [Improving skill-creator: Test, measure, and refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)（2026-03-03）— 評估先行
- [Skills explained: How Skills compares to prompts, Projects, MCP, and subagents](https://claude.com/blog/skills-explained)（2025-11-13）
- [How Anthropic enables self-service data analytics with Claude](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)（2026-06-03）— Analytics agent 四層架構
- [Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent)（2026-04-10）— 工具設計哲學與 Progressive Disclosure

**站內研究歸檔**

- [Skills 九大類別與 Analytics Agent 設計](/research/best-practices/33-skills-nine-categories)
- [官方 Agent Skills 撰寫最佳實踐](/research/best-practices/06-agent-skills-best-practices)
- [自訂 Claude Code 行為的七種機制](/research/best-practices/38-steering-claude-code)
- [Agent Skills 企業治理指南](/research/best-practices/10-agent-skills-enterprise)
