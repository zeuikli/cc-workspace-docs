# Claude Code Sub-Agent、MCP Server 與 Skill 最佳實踐

> 來源：官方 Sub-Agents 文件、MCP 文件、社群實踐（2026-04-25）

---

## Sub-Agent 委派策略

### 何時使用 Sub-Agent

**需要委派的信號：**
- 側邊任務會淹沒主對話（搜尋結果、日誌、大量檔案）
- 需要隔離工具存取（reviewer 不應有 Write 權限）
- 需要專業化系統提示（DB migration subagent 包含 SQL 知識）
- 成本控制：快速、便宜的任務路由到 Haiku

**判斷心智模型：**
> "Will I need this tool output again, or just the conclusion?"
- 只需要結論 → 委派 subagent（中間產物留在 child context）
- 需要反覆檢視中間產物 → 主對話自己做

### Sub-Agent vs Agent Teams vs 直接執行

| 情境 | 選擇 | 理由 |
|------|------|------|
| 獨立子任務、結論即可 | Sub-Agent | Context 隔離，中間產物不污染主線 |
| 需要中途通訊或共享狀態 | Agent Teams | 同儕通訊 + 共享 task list |
| 需要反覆檢視中間產物 | 直接執行 | 保留完整 context |
| 預期工具呼叫 > 20 次 | 必須委派 Sub-Agent | 防止 context rot |

### 工具作用域原則

```yaml
researcher:    allowed-tools: Read, Grep, Glob        # read-heavy，只讀
implementer:   allowed-tools: Read, Write, Edit, Bash  # 可寫可執行
reviewer:      allowed-tools: Read, Grep, Glob         # 只讀（不給 Write/Bash）
test-writer:   allowed-tools: Read, Grep, Glob, Write  # 可寫測試，不執行
```

---

## Agent Model 分層

| Model | 任務類型 | 適用場景 |
|-------|---------|---------|
| **Haiku 4.5** | 搜尋、探索、重複性工作 | Subagent 預設；成本/速度優先 |
| **Sonnet 4.6** | 實作、測試、日常編碼 | 主線執行者；品質與成本平衡 |
| **Opus 4.7** | 架構設計、複雜審查、疑難雜症 | Advisor 模式；按需諮詢（xhigh effort）|

### Advisor 模式（核心策略）

- **Sonnet 主執行**：驅動任務、讀寫檔案、呼叫工具、逐步推進
- **Opus 幕後顧問**：僅在關鍵時刻提供策略建議（回應 400–700 token）

**諮詢 Opus 的時機：**
- 架構層級的設計決策或跨模組重構
- 邊界案例判斷與不確定的技術選型
- 複雜邏輯的程式碼審查與安全性審計
- 長 session 的 recovery（如 compact 後接手）

**不需諮詢 Opus：**
- 簡單搜尋、格式化
- 已知模式的重複性工作
- 執行測試與 lint

---

## MCP Server 最佳實踐

### 基本設定

```bash
# 新增 MCP server
claude mcp add <server-name>

# 查看已設定的 MCP servers
/mcp
```

### 設計原則

1. **權限最小化**：MCP servers 以系統權限執行，嚴格審查社群擴充來源
2. **工具數量限制**：常見 3–6 個 MCP servers；太多稀釋模型工具選擇品質
3. **Hooks 用於強制執行**：
   - Prompts 是建議（模型可選擇忽略）
   - Hooks 是確定性（保證每次執行）

### MCP + Hooks 整合範例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp_tool",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/audit-mcp-call.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Skill 設計規範

### SKILL.md 基本架構

```yaml
---
name: my-skill
description: |
  何時使用（正向觸發，可以 pushy）。
  Make sure to use this skill whenever X.
  
  Do NOT use for: Y, Z（排除條件必寫）
allowed-tools: Read, Grep        # 預先批准的工具
disable-model-invocation: false  # 是否允許 Claude 自主呼叫
user-invocable: true             # 是否可用 /skill-name 觸發
context: fork                    # 在 subagent 中執行（隔離 context）
---

# 核心說明

## Rules
[規則列表，附說明原因]

## Known Gotchas
[踩坑紀錄，每次實際運行後補充]

## Examples
Input: [輸入範例]
Output: [預期輸出]
```

### Description 設計原則

**Description 是選擇引擎**，不是說明文件：

```yaml
# ❌ 只說明是什麼
description: "API convention checker for REST endpoints"

# ✅ 說明何時用、何時不用
description: |
  REST API 設計慣例審查。
  Make sure to use this skill whenever designing or reviewing REST endpoints.
  Do NOT use for: gRPC、GraphQL、SDK 設計、前端元件
```

**字元預算**：description + when_to_use 合計 ≤ 1,536 字元（Claude Code 截斷限制）

### 長度控制策略

| SKILL.md 長度 | 策略 |
|---------------|------|
| < 300 行 | 保持單檔，補充 Gotchas 和 Examples |
| 300–500 行 | 識別可拆的 Reference |
| **> 500 行** | **Progressive Disclosure**：SKILL.md 只做 TOC + 核心流程 |

**Progressive Disclosure 結構：**

```
skills/my-skill/
├── SKILL.md          ← TOC + 核心流程（≤ 500 行）
├── REFERENCE.md      ← 完整 API / 設定參考
├── FORMS.md          ← 表單/模板定義
└── scripts/          ← 可執行腳本（只有輸出進 context）
```

### 規則寫法：說明原因而非命令

```
❌ MUST use constructor injection. NEVER use field injection.

✅ Use constructor injection. Field injection breaks testability
   because we cannot mock the field without Spring context.
```

### 自由度分層

| 任務類型 | 指令自由度 | 寫法 |
|---------|----------|------|
| Code review、分析 | 高 | 文字說明 + persona |
| Deploy、CI 流程 | 中 | Pseudocode + 參數化腳本 |
| **DB 遷移、破壞性操作** | **低** | **精確腳本，禁止修改命令** |

### Shell 動態注入

```markdown
當前 git branch：`!git branch --show-current`
最後 commit：`!git log --oneline -1`
```

`` !`command` `` 在 Skill 觸發時執行，結果插入 prompt（非 Claude 執行，保持確定性）。

---

## Tasks 原語（跨 Session 協作）

Tasks 是磁碟持久化的任務追蹤，不同於內存 Todos：

| | Todos | Tasks |
|---|-------|-------|
| 儲存位置 | Session 記憶體 | `~/.claude/tasks`（磁碟）|
| 跨 session | ❌ | ✅ |
| Subagent 協作 | ❌ | ✅ 多個 subagent 同時更新 |
| 依賴關係 | ❌ | ✅ Task 可以有 dependencies |
| 跨 session 廣播 | ❌ | ✅ 即時同步 |

**使用時機：**
- 跨越多個 session 的長任務
- 多個 subagent 需要協調的複雜工作
- Coordinator 追蹤多個 Worker 進度

---

## 平行化最佳實踐

### 單一訊息啟動多個 Subagent

```
# 正確：同一訊息平行啟動
請同時啟動三個 subagent：
1. researcher：分析 src/auth/ 的認證流程
2. test-writer：為 auth module 補測試
3. doc-writer：更新 auth 相關 README

# 錯誤：序列啟動（浪費時間）
先啟動 researcher，等它完成再啟動 test-writer...
```

### Opus 4.7 需要明確的平行指示

Opus 4.7 預設較少自動開 subagent，需在 prompt 中明確指示：

```
Do not spawn a subagent for work you can complete directly in a single response
(e.g., refactoring a function you can already see).
Spawn multiple subagents in the same turn when fanning out across items
or reading multiple files.
```

---

## 核心認知

1. **Subagents 是隔離機制**，不是簡單的委派——目標是保持主對話 context 乾淨
2. **Hooks ≠ Prompts**：Hooks 強制執行，Prompts 只是建議
3. **Skills 是 lazy-load**：description 始終載入，full content 僅在觸發時載入
4. **Advisor 模式勝於直接使用 Opus**：讓 Sonnet 主執行，Opus 只在架構層諮詢
5. **預期工具呼叫 > 20 次 → 必須委派 Sub-Agent**

---

## 參考來源

- https://code.claude.com/docs/en/sub-agents（官方 Sub-Agents 文件）
- https://code.claude.com/docs/en/skills（官方 Skill 文件）
- https://code.claude.com/docs/en/mcp（官方 MCP 文件）
- https://www.anthropic.com/engineering/claude-code-best-practices
- https://alexop.dev/posts/understanding-claude-code-full-stack/
- https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/
- https://platform.claude.com/docs/en/agent-sdk/subagents
