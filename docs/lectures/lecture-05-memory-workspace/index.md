# Lecture 05：記憶系統與工作區設計

## 學習目標

完成本課後，你將能夠：

- 設計跨 session 的狀態持久化機制（MEMORY.md）
- 正確設定 Git Worktrees 實現多工作區並行
- 選擇合適的 Sub-agent 委派策略和 Model 分層方案
- 配置和使用 Skills 與 MCP Server 延伸 Claude Code 能力

## 核心概念

### Auto Memory（MEMORY.md）機制

Auto Memory 是 Claude Code 自動維護的記憶系統，讓 Claude 能夠跨 session 記住它學到的東西。

**工作原理**：
- Claude 在 session 中發現有用的 patterns、指令、debug insights
- 自動寫入 `MEMORY.md`（位於每個 working tree 的根目錄）
- 每次新 session 開始時，自動載入 MEMORY.md 的前 200 行（或 25KB）

**MEMORY.md 和 CLAUDE.md 的協作**：

| 特性 | MEMORY.md（Auto Memory）| CLAUDE.md |
|------|------------------------|-----------|
| **誰維護** | Claude 自動寫入 | 你手動維護 |
| **優先序** | 較低（CLAUDE.md 覆蓋它）| 較高 |
| **內容** | Build 指令、debug insights、已發現的 patterns | 架構規則、禁止事項、完成定義 |
| **適合** | Claude 自行積累的學習成果 | 人類主動定義的規則 |

**重要**：CLAUDE.md 的內容會覆蓋 Auto Memory 的學習。如果你想強制某個行為，在 CLAUDE.md 中明確定義，不要依賴 Auto Memory。

### 跨 Session 狀態管理

Anthropic 在《Effective harnesses for long-running agents》中推薦的三層狀態架構：

**1. CLAUDE.md（靜態規則層）**
- 專案的永久約定：技術棧、架構規則、禁止事項
- 不受 session 影響

**2. claude-progress.md（任務進度層）**
- 當前任務的進度追蹤
- 每個 session 開始時讀取，結束時更新
- 包含：已完成的 spec items、遇到的問題、下一步計畫

**3. feature_list.json（功能驗收層）**
- 功能的驗收標準和狀態
- 每個功能 item 的完成狀態

```json
{
  "features": [
    {
      "id": "user-auth",
      "description": "使用者 OAuth 2.0 認證",
      "status": "done",
      "completion_evidence": "pytest tests/test_auth.py passes"
    },
    {
      "id": "search-api",
      "description": "GET /api/search endpoint",
      "status": "in_progress",
      "completion_evidence": "GET /api/search?q=test returns 200 with results"
    }
  ]
}
```

**跨 session 的 Initializer Agent 流程**（來自 Anthropic 推薦）：

```
New Session 開始
  │
  ▼
Initializer Agent
  ├─ 讀取 CLAUDE.md（專案規則）
  ├─ 讀取 claude-progress.md（上次進度）
  ├─ 讀取 feature_list.json（待完成項目）
  └─ 輸出：「我上次做到哪了，接下來要做什麼」
  │
  ▼
Coding Agent
  ├─ 從 Initializer 的輸出接手
  ├─ 逐項完成 feature_list 中的 item
  └─ 每完成一項更新 feature_list.json 和 claude-progress.md
  │
  ▼
Session 結束
  └─ 確認 claude-progress.md 已更新（含下一步計畫）
```

### Git Worktrees：多工作區並行

Git Worktrees 讓你可以在同一個 repo 中並行開多個工作目錄，每個都有獨立的 branch 和 Claude session：

```bash
# 建立新的 worktree（feature branch）
git worktree add ../myproject-feature1 feature/add-search
git worktree add ../myproject-feature2 feature/user-profile

# 在各自的目錄中開啟獨立 Claude session
cd ../myproject-feature1 && claude
cd ../myproject-feature2 && claude

# 查看所有 worktrees
git worktree list

# 清理已合併的 worktree
git worktree remove ../myproject-feature1
```

**使用 Worktrees 的好處**：
1. 並行處理多個功能，互不干擾
2. 每個 worktree 有獨立的 session 歷史
3. CLAUDE.md 從根目錄繼承，但各 worktree 可有自己的 CLAUDE.local.md
4. Sub-agent 可以在不同 worktree 中並行工作

### Sub-agent 委派策略

#### 何時使用 Sub-agent

**需要委派的信號**：
- 側邊任務會淹沒主對話（搜尋結果、日誌、大量檔案讀取）
- 需要隔離工具存取（reviewer 不應有 Write 權限）
- 需要專業化系統提示（DB migration subagent 包含 SQL 知識）
- 成本控制：快速、便宜的任務路由到 Haiku

**判斷心智模型**：
> "Will I need this tool output again, or just the conclusion?"
- 只需要結論 → 委派 subagent（中間產物留在 child context）
- 需要反覆檢視中間產物 → 主對話自己做

#### 工具作用域原則

```yaml
researcher:    allowed-tools: Read, Grep, Glob          # 只讀
implementer:   allowed-tools: Read, Write, Edit, Bash    # 可寫可執行
reviewer:      allowed-tools: Read, Grep, Glob           # 只讀（不給 Write/Bash）
test-writer:   allowed-tools: Read, Grep, Glob, Write    # 可寫測試，不執行
```

#### Model 分層策略

| Model | 任務類型 | 適用場景 |
|-------|---------|---------|
| **Haiku 4.5** | 搜尋、探索、重複性工作 | Subagent 預設；成本/速度優先 |
| **Sonnet 4.6** | 實作、測試、日常編碼 | 主線執行者；品質與成本平衡 |
| **Opus 4.7** | 架構設計、複雜審查、疑難雜症 | Advisor 模式；按需諮詢 |

**Advisor 模式（Boris Cherny / Anthropic 推薦）**：
- Sonnet 主執行：驅動任務、讀寫檔案、呼叫工具、逐步推進
- Opus 幕後顧問：僅在關鍵時刻提供策略建議（回應 400-700 token）

**諮詢 Opus 的時機**：架構層級的設計決策、邊界案例判斷、複雜邏輯的程式碼審查。

**不需諮詢 Opus**：簡單搜尋、格式化、已知模式的重複性工作、執行測試與 lint。

### Skills：封裝可重用的 Agent 行為

Skills 是可重用的自然語言 instructions，封裝了特定任務的 step-by-step 流程：

```bash
# 建立 skill（在 .claude/skills/ 目錄）
mkdir -p .claude/skills

# 使用 skill
/skill-name args
```

典型的 skill 結構：

```markdown
<!-- .claude/skills/run-tests.md -->
# Run Tests Skill

你被呼叫來執行測試套件並分析結果。

## 步驟

1. 執行 `pytest tests/ -v --tb=short`
2. 如果有失敗，分析錯誤訊息
3. 對每個失敗的測試，說明：
   - 失敗原因
   - 是否需要修改測試本身或業務邏輯
4. 回傳結構化的測試報告
```

### MCP Server：連接外部服務

MCP（Model Context Protocol）讓 Claude Code 透過標準化協定連接外部工具和服務：

```bash
# 新增 MCP server（透過 claude mcp add）
claude mcp add github

# 查看已設定的 MCP servers
/mcp

# 在 .claude/settings.json 中設定
```

設定範例：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

## 程式碼範例

### claude-progress.md 模板

```markdown
# Claude Progress Log

## 當前 Sprint
**目標**：實作用戶偏好設定 API（/api/v2/users/preferences）

## 完成狀態
- [x] 設計 API schema（GET + PUT /api/v2/users/preferences）
- [x] 建立 database migration（alembic revision）
- [ ] 實作 GET endpoint
- [ ] 實作 PUT endpoint
- [ ] 撰寫單元測試
- [ ] 整合測試

## 遇到的問題
- PostgreSQL 的 JSONB 欄位在 SQLAlchemy 2.0 的寫入語法：
  ```python
  # 正確：
  await session.execute(update(User).where(User.id == user_id).values(preferences=new_prefs))
  # 錯誤（1.x 語法）：
  user.preferences = new_prefs
  ```

## 下一步（下次 session 從這裡開始）
1. 實作 GET /api/v2/users/preferences（handlers/user_preferences.py）
2. 驗證：`pytest tests/api/test_user_preferences.py -v`

## 最後更新
2026-05-26 by Claude (session abc123)
```

### Worktree 並行工作腳本

```bash
#!/bin/bash
# scripts/start-parallel-work.sh
# 建立兩個並行工作環境

REPO_ROOT=$(git rev-parse --show-toplevel)
PARENT_DIR=$(dirname "$REPO_ROOT")

# Feature 1
git worktree add "$PARENT_DIR/work-feature1" -b feature/search-api
echo "Created worktree for search-api feature"

# Feature 2
git worktree add "$PARENT_DIR/work-feature2" -b feature/user-profile
echo "Created worktree for user-profile feature"

echo ""
echo "Start working:"
echo "  cd $PARENT_DIR/work-feature1 && claude"
echo "  cd $PARENT_DIR/work-feature2 && claude"
```

### Sub-agent 呼叫模式

```
# 在主 Claude session 中，委派搜尋任務給 sub-agent
Task: 在 src/ 目錄中搜尋所有使用了舊版 SQLAlchemy 1.x session 語法的位置。
具體來說，找所有使用 Session() 或 db.session 而不是 async_session 或 get_db() 的地方。
只需要返回：檔案路徑、行號、問題描述的清單。不要修改任何檔案。
```

```
# 主 agent 收到清單後，自己決定如何處理
# sub-agent 的搜尋過程（讀取的大量檔案）不污染主 agent 的 context
```

### 路徑規則 frontmatter 格式

```markdown
---
paths:
  - "src/api/**/*.ts"
  - "src/handlers/**/*.ts"
---

# API Layer Rules

- 所有 API handlers 必須驗證輸入（使用 Zod schema）
- 使用標準錯誤格式（`{ error: string, code: string }`）
- 包含 OpenAPI 文件注釋
```

## 常見問題與注意事項

**Q：MEMORY.md 存在哪裡？**

A：存在每個 working tree 的根目錄（`./MEMORY.md`）。如果使用 Git Worktrees，每個 worktree 有獨立的 MEMORY.md，不共用。

**Q：如何查看 Auto Memory 的內容？**

A：直接讀取 `./MEMORY.md` 或用 `/memory` 指令查看。

```bash
# 清空 Auto Memory
/memory clear

# 查看 memory
cat MEMORY.md
```

**Q：Claude Code session 存在哪裡？**

A：存在 `~/.claude/projects/` 的 JSONL 檔案中。

```bash
# 繼續最近的 session
claude --continue

# 選擇最近的 sessions
claude --resume

# Fork 一個 session（不影響原始 session）
claude --continue --fork-session
```

**Q：MCP Server 和 Skills 有什麼區別？**

A：
- **MCP Server**：外部服務的連接器（GitHub、資料庫、Slack 等）。Claude 透過 MCP 呼叫外部 API。
- **Skills**：封裝 agent 行為的 instruction set。Skills 是「怎麼做某件事的步驟」，不是連接外部服務。

**Q：Sub-agent 的 context 和主 agent 完全隔離嗎？**

A：是的。Sub-agent 在獨立的 session 中執行，它讀取的所有檔案、呼叫的所有工具的中間輸出，都留在 sub-agent 的 context 中，不會流回主 agent。主 agent 只看到 sub-agent 返回的最終結論。

## 本課小結

- **Auto Memory（MEMORY.md）**：Claude 自動維護，跨 session 記憶 patterns 和 insights。CLAUDE.md 規則優先級更高。
- **三層狀態架構**：CLAUDE.md（靜態規則）+ claude-progress.md（任務進度）+ feature_list.json（驗收標準）。
- **Git Worktrees**：同一個 repo 的多個並行工作環境。每個 worktree 有獨立 session 和 MEMORY.md。
- **Sub-agent 委派**：中間產物不污染主 context。只傳結論，不傳過程。工具作用域原則（reviewer 只讀）。
- **Model 分層**：Haiku（探索）→ Sonnet（實作）→ Opus（架構決策）。Advisor 模式讓 Opus 按需諮詢。
- **Skills + MCP**：Skills 封裝行為，MCP 連接外部服務。兩者都是 Claude Code 能力延伸的方式。

## 延伸閱讀

- [Lecture 02：CLAUDE.md 設計](/lectures/lecture-02-claude-md/) — CLAUDE.md 的詳細設定
- [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/) — Sub-agent 作為 Context Firewall
- [Project 01：從零建立你的第一個 Workspace](/projects/project-01-init-workspace/) — 動手建立 MEMORY.md 和 claude-progress.md
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [官方文件：Claude Code Sub-Agents](https://code.claude.com/docs/en/sub-agents)
