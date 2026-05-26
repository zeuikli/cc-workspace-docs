# 社群 Claude Code CLAUDE.md / Agent / Skill 最佳實踐

> 來源：shanraisshan/claude-code-best-practice、code.claude.com/docs/en/best-practices、hesreallyhim/awesome-claude-code（2026-04-25）

---

## CLAUDE.md 設計原則

### 核心規則

- **長度限制**：保持在 200 行以下；60 行最佳（太長會被忽視）
- **聚焦內容**：只寫會讓 Claude **改變行為**的內容

**✅ 應該包含：**
- CLI 無法猜測的 Bash 指令
- 與預設不同的代碼風格
- 測試指令與驗證方式
- 架構決策、模組邊界

**❌ 不應包含：**
- Claude 能從代碼推斷的內容
- 標準語言慣例（PEP8 等）
- 詳細 API 文檔（改放 REFERENCE.md）
- 顯而易見的實踐

### CLAUDE.md 結構範本

```markdown
# Code Style
- Use ES modules (import/export), not CommonJS
- Prefer functional patterns over class-based

# Workflow
- Run single tests for performance, not whole suite
- Typecheck after code changes: npm run typecheck

# Build & Test
npm run build        # Production build
npm run test         # Run test suite
npm run test:watch   # Watch mode for TDD

# Architecture
- API routes in src/routes/
- Business logic in src/services/ (NOT in routes)
- Database access only through src/repositories/
```

### 撰寫原則

- 定期修剪：問自己「移除這行會讓 Claude 出錯嗎？」不會就刪
- Treat CLAUDE.md like code：遇到問題時審查，定期測試改動是否產生行為變化
- 用 `<important>` 標籤強調關鍵規則

---

## Agent 設計模式

### Command → Agent → Skill 架構

```
/weather                 ← Command（使用者觸發）
    ↓
WeatherAgent             ← Agent（隔離 context、協調邏輯）
    ├─ CurrentWeatherSkill
    └─ ForecastSkill
```

- **Commands**：簡單使用者觸發的提示範本（`.claude/commands/`）
- **Agents**：隔離 context 中的專門執行者，有自訂工具和記憶
- **Skills**：可組合的知識，支援漸進式揭露（progressive disclosure）

### Agent 設定結構

```yaml
---
name: security-reviewer
description: |
  Reviews code for security vulnerabilities.
  Do NOT use for: general code review, formatting, style issues.
tools: Read, Grep, Glob, Bash
model: opus
effort: xhigh
permissionMode: auto
maxTurns: 20
---

You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure dependencies

Provide specific line references for each finding.
```

### 何時使用 Subagents

**需要 subagent 的信號：**
- 讀取 10+ 個檔案（結果只需要結論）
- 產生大量中間輸出（tool noise 不需留在主線）
- 可拆成 3+ 個獨立子任務
- 需要隔離工具存取（如 review agent 不應有 Write 權限）

**Subagent vs 直接執行的心智模型：**
> "Will I need this tool output again, or just the conclusion?"
- 只需要結論 → 委派 subagent
- 需要反覆檢視中間產物 → 主對話自己做

### 工具作用域原則

```yaml
researcher:    allowed-tools: Read, Grep, Glob        # 只讀
implementer:   allowed-tools: Read, Write, Edit, Bash  # 可寫可執行
reviewer:      allowed-tools: Read, Grep, Glob         # 只讀（不給 Write）
```

### 編排策略

**Writer/Reviewer 模式：**
- Session A：實作功能
- Session B：獨立 context 審查（無偏見）

**Test/Code 對稱：**
- Session A：寫測試
- Session B：寫代碼通過測試

---

## Skill 設計模式

### 檔案結構

```
.claude/skills/api-conventions/
├── SKILL.md           ← 核心規則（≤500 行）
├── REFERENCE.md       ← 完整 API 參考
├── FORMS.md           ← 範本定義
└── scripts/
    └── validate.sh    ← 可執行驗證腳本
```

### SKILL.md 描述設計

```yaml
---
name: api-conventions
description: |
  REST API 設計慣例。使用 kebab-case URL paths、camelCase JSON 屬性、
  分頁清單端點、版本化 API。
  
  Make sure to use this skill whenever designing REST API endpoints.
  
  Do NOT use for: 非 REST API（gRPC/GraphQL）、SDK 設計、前端元件
allowed-tools: Read, Glob
---
```

**描述寫作要點：**
- 作為觸發條件（「何時應該觸發我？」），而非摘要
- 加 "Make sure to use this skill whenever..." 主動提示（模型傾向 undertrigger）
- 必有排除條件（Do NOT use for）

### Skill 核心內容結構

```markdown
## 規則（Rules）
- Use kebab-case for URL paths (/api/v1/user-profiles)
- Use camelCase for JSON properties

## Known Gotchas（踩坑紀錄）
- Pagination tokens are base64-encoded, never raw offsets
- Nested resources: /users/{id}/posts/{id}，不是 /users/{user_id}/...

## Examples
Input:  "Design endpoint for listing user preferences"
Output: "GET /api/v1/user-profiles/{id}/preferences?page=1&limit=20"
```

### Skill 長度控制

| 長度 | 策略 |
|------|------|
| < 300 行 | 保持單檔，補充 Gotchas 和 Examples |
| 300–500 行 | 接近上限，識別可拆出的 Reference |
| **> 500 行** | **Progressive Disclosure**：SKILL.md 只做 TOC |

### 關鍵設計原則

| 設計面向 | 做法 | 原因 |
|---------|------|------|
| **Known Gotchas** | 每次踩坑後立即補充 | 最有價值的 Skill 內容 |
| **可組合性** | 包含腳本庫 | 讓 Claude 組合，不重建樣板 |
| **指令自由度** | 分析類高自由度、DB 遷移低自由度 | 安全操作需精確腳本 |
| **解釋原因** | MUST/NEVER 附上理由 | 理由成為邊界情況判斷標準 |

---

## Context 管理最佳實踐

### Context 壓縮決策表

| 狀態 | 動作 | 原因 |
|------|------|------|
| 同一任務、context 仍相關 | Continue | 不重建 context |
| Claude 走錯路徑 | `/rewind`（雙按 Esc）| 保留讀取結果、丟棄失敗嘗試 |
| 任務未完但充滿雜訊 | `/compact <hint>` | 低成本、Claude 決定保留什麼 |
| 開始全新任務 | `/clear` | 零 context rot |
| 下一步產生大量輸出 | Subagent | 中間產物留在 child context |

### Compact Hint 範本

```
/compact 保留：當前實作進度、已確認的設計決策、待辦清單。
         丟棄：探索過但放棄的方法、冗長工具輸出、重複錯誤訊息。
         下一步：繼續實作 <feature>，從 <file:line> 開始。
```

### Context Rot 閾值

約 300–400k tokens 開始影響輸出品質：
- 複雜 agentic 任務：30–35% 主動 compact
- 一般任務：70% 提醒

---

## 常見失敗模式與修復

| 失敗模式 | 修復 |
|---------|------|
| **廚房水槽會話**（一個 session 做太多事）| `/clear` 分離無關任務 |
| **重複糾正**（Claude 一直走錯路）| 2 次失敗後 `/clear` + 寫更好的初始提示 |
| **CLAUDE.md 過度設定** | 無情修剪；規則已遵循就刪 |
| **信任但未驗證** | 提供測試/腳本驗證邊界情況 |
| **無限探索** | 給範圍限制或用 subagents |

---

## 驗證優先（Goal-Driven）

```
❌ 模糊：「實作一個驗證 email 的函式」

✅ 目標驅動：「寫 validateEmail 函式。
   測試用例：
     user@example.com → true
     invalid → false
     user@.com → false
   實作後跑測試並通過」
```

---

## 平行化與自動化

### 非互動模式

```bash
# 一次性查詢
claude -p "Explain this project"

# 結構化輸出
claude -p "List all API endpoints" --output-format json

# 批量遷移
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue" --allowedTools "Edit,Bash"
done
```

---

## 參考來源

- https://github.com/shanraisshan/claude-code-best-practice
- https://code.claude.com/docs/en/best-practices
- https://github.com/hesreallyhim/awesome-claude-code
- https://github.com/ChrisWiles/claude-code-showcase
