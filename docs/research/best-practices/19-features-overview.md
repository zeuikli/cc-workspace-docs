---
title: "Extend Claude Code — 功能總覽與選擇指南"
source: "https://code.claude.com/docs/en/features-overview"
type: best-practices
---

# Extend Claude Code — 功能總覽與選擇指南

> 來源：https://code.claude.com/docs/en/features-overview
> 收錄日期：2026-05-01
> 涵蓋：CLAUDE.md vs Skills vs MCP vs Subagents vs Agent Teams vs Hooks vs Plugins 完整比較

---

## 功能全覽

Extensions 插入 agentic loop 的不同位置：

| 功能 | 作用 | 載入時機 |
|------|------|---------|
| **CLAUDE.md** | 每次 session 自動載入的持久 context | Session 開始 |
| **Skills** | 可重用的知識和可呼叫的 workflows | 按需（描述在 session start 載入，內容在使用時載入） |
| **MCP** | 連接外部服務和工具 | Session 開始（tool names）；schema 按需 |
| **Subagents** | 在隔離 context 中執行，回傳摘要 | 被 spawn 時 |
| **Agent teams** | 協調多個獨立 session，共享 tasks 和點對點通訊 | 各 session 獨立 |
| **Hooks** | 在 lifecycle events 執行腳本、HTTP 請求、prompt、或 subagent | 觸發事件時 |
| **Plugins/Marketplaces** | 打包分發上述功能的單元 | 安裝後按各功能規則 |

Skills 是最靈活的 extension。可用 `/deploy` 呼叫，也可讓 Claude 在相關情境自動載入。可在當前對話或隔離 context（via subagents）中執行。

---

## 何時加入各功能（觸發點判斷表）

| 觸發情況 | 加入什麼 |
|---------|---------|
| Claude 同一慣例或指令犯兩次錯 | 加入 [CLAUDE.md](/research/best-practices/21-memory-claudemd) |
| 你一直輸入同樣的 prompt 開始某個任務 | 存成可呼叫的 [skill](https://code.claude.com/docs/en/skills) |
| 你第三次把同樣的 playbook 或多步流程貼進對話 | 捕捉為 [skill](https://code.claude.com/docs/en/skills) |
| 你一直要複製 Claude 看不到的 tab 資料 | 把該系統連接為 [MCP server](https://code.claude.com/docs/en/mcp) |
| 某個側邊任務把你的對話淹沒在你不會再看的輸出 | 用 [subagent](https://code.claude.com/docs/en/sub-agents) 路由 |
| 你希望某件事每次都自動發生，不需要詢問 | 寫 [hook](https://code.claude.com/docs/en/hooks-guide) |
| 第二個 repo 需要相同的設定 | 打包成 [plugin](https://code.claude.com/docs/en/plugins) |

同樣的觸發點告訴你何時更新已有的功能。重複的錯誤或 code review 評論 = CLAUDE.md 的更新（不是臨時修正）。你一直手動調整的 workflow = 需要再次修改的 skill。

---

## 功能比較詳解

### CLAUDE.md vs Skill

| 面向 | CLAUDE.md | Skill |
|------|-----------|-------|
| **載入時機** | 每次 session 自動 | 按需 |
| **可引入檔案** | 是，用 `@path` | 是，用 `@path` |
| **可觸發 workflows** | 否 | 是，用 `/<name>` |
| **最適合** | "Always do X" 規則 | 參考資料、可呼叫 workflows |

**經驗法則**：CLAUDE.md 控制在 200 行以內。成長太快時，把參考資料移到 skills 或拆進 `.claude/rules/` 檔案。

### Skill vs Subagent

| 面向 | Skill | Subagent |
|------|-------|---------|
| **本質** | 可重用的指令、知識、workflows | 有自己 context 的隔離 worker |
| **核心優勢** | 跨 contexts 分享內容 | Context 隔離；工作在獨立空間完成，只有摘要回傳 |
| **最適合** | 參考資料、可呼叫 workflows | 讀取大量檔案、平行工作、專門 workers |

**兩者可結合**：subagent 可以預載特定 skills（`skills:` 欄位）；skill 可以用 `context: fork` 在隔離 context 中執行。

### CLAUDE.md vs Rules vs Skills（三層區分）

| 面向 | CLAUDE.md | `.claude/rules/` | Skill |
|------|-----------|-----------------|-------|
| **載入時機** | 每次 session | 每次 session，或開啟符合路徑的檔案時 | 按需 |
| **範圍** | 整個專案 | 可限縮到特定路徑 | 任務特定 |
| **最適合** | 核心慣例和 build 指令 | 語言或目錄特定的指南 | 參考資料、重複 workflows |

### Subagent vs Agent Team

| 面向 | Subagent | Agent Team |
|------|---------|------------|
| **Context** | 自己的 context window；結果回傳給呼叫者 | 自己的 context window；完全獨立 |
| **通訊** | 只向主 agent 回報結果 | 成員之間直接互傳訊息 |
| **協調** | 主 agent 管理所有工作 | 共享 task list，自我協調 |
| **最適合** | 只需要結果的聚焦任務 | 需要討論和協作的複雜工作 |
| **Token 成本** | 較低（結果摘要回主 context） | 較高（每個成員都是獨立 Claude instance） |

**轉換時機**：如果你在跑平行 subagents 但遭遇 context limits，或 subagents 需要互相通訊 → Agent teams 是自然的下一步。

> Agent teams 為實驗性功能，預設關閉。

### MCP vs Skill

| 面向 | MCP | Skill |
|------|-----|-------|
| **本質** | 連接外部服務的協定 | 知識、workflows、參考資料 |
| **提供** | Tools 和資料存取 | 知識、workflows、參考資料 |
| **範例** | Slack 整合、資料庫查詢、瀏覽器控制 | Code review checklist、deploy workflow、API style guide |

**搭配使用**：MCP 提供能力，Skill 提供如何有效使用的知識。例：MCP server 連接資料庫，Skill 教 Claude 你的資料模型和常用 query patterns。

### Hook vs Skill

| 面向 | Hook | Skill |
|------|------|-------|
| **執行內容** | shell 指令、HTTP 請求、LLM prompt、或 subagent | Claude 讀取並遵循的指令 |
| **觸發** | Lifecycle events（如 PostToolUse、SessionStart） | 你輸入 `/<name>`，或 Claude 判斷與你的任務相關 |
| **確定性** | 事件觸發時一定執行 | Claude 詮釋指令；結果可能有差異 |
| **Context 成本** | 零（除非 hook 回傳輸出） | 描述每次 session 載入；內容在使用時載入 |
| **最適合** | Lint 後編輯、封鎖不安全指令、logging、通知 | 需要推理的 workflows、參考資料、多步驟任務 |

**重要**：CLAUDE.md 或 Skill 中的「絕不編輯 `.env`」是請求，不是保證。`PreToolUse` hook 封鎖編輯才是強制執行。**如果規則必須每次都成立，做成 hook 而非 prompt 指令。**

**Hook 輸出進入 context**：`PostToolUse` hook 跑 linter → 結果以文字回傳給 Claude 讀取；`/fix-lint` skill 告訴 Claude 如何解決。

---

## 功能分層（多層級設定）

功能可在多個層級定義：user-wide、per-project、via plugins、managed policies。

- **CLAUDE.md files**：累加性，所有層級的內容同時進入 context
- **Skills 和 Subagents**：名稱覆蓋（managed > user > project for skills）；Plugin skills 用命名空間避免衝突
- **MCP servers**：local > project > user
- **Hooks**：合併，所有 hooks 都會在對應事件觸發

---

## 功能組合 Patterns

| Pattern | 如何運作 | 範例 |
|---------|---------|------|
| **Skill + MCP** | MCP 提供連接；Skill 教 Claude 如何有效使用 | MCP 連資料庫，Skill 記錄 schema 和 query patterns |
| **Skill + Subagent** | Skill 派出 subagents 平行工作 | `/audit` skill 啟動 security、performance、style 三個 subagents |
| **CLAUDE.md + Skills** | CLAUDE.md 放常駐規則；Skills 放按需參考資料 | CLAUDE.md 說「遵循我們的 API 慣例」，Skill 包含完整 API style guide |
| **Hook + MCP** | Hook 透過 MCP 觸發外部操作 | 編輯後 hook 透過 Slack MCP 發送通知 |

---

## Context 成本對照表

| 功能 | 載入時機 | 載入什麼 | Context 成本 |
|------|---------|---------|------------|
| **CLAUDE.md** | Session start | 完整內容 | 每個 request |
| **Skills** | Session start + 使用時 | 描述在 start，完整內容在使用時 | 低（描述每個 request）* |
| **MCP servers** | Session start | Tool names；完整 schema 按需 | 低（直到 tool 被使用） |
| **Subagents** | 被 spawn 時 | 獨立的新 context + 指定的 skills | 與主 session 隔離 |
| **Hooks** | 觸發時 | 不載入任何東西（外部執行） | 零（除非 hook 回傳輸出） |

*設定 `disable-model-invocation: true` 可讓 skill 完全對 Claude 隱藏，直到你手動呼叫 → context 成本歸零。

### 各功能載入時序

1. **Session start**：CLAUDE.md 全部內容 + MCP tool names + Skill 描述
2. **Skill 被呼叫/相關時**：Skill 完整內容載入
3. **MCP tool 被使用時**：該 tool 的完整 schema 載入
4. **Subagent spawn 時**：隔離的新 context（包含：system prompt、指定 skills 完整內容、CLAUDE.md、git status）

---

## 相關文件

| 功能 | 文件 |
|------|------|
| CLAUDE.md | [本站 Memory 指南](/research/best-practices/21-memory-claudemd) |
| Skills | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| Subagents | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) |
| Agent teams | [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) |
| MCP | [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) |
| Hooks | [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) |
| Plugins | [code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins) |
| Plugin Marketplaces | [code.claude.com/docs/en/plugin-marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) |
