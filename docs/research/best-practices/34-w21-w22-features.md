# Claude Code W21–W22 新功能（2026-05-18 ~ 2026-05-29）

> 來源：官方 What's New  
> 版本：v2.1.143 → v2.1.157  
> 整理日期：2026-06-05

---

## Week 21（v2.1.143–v2.1.149）｜2026-05-18–22

### 主功能：Auto Mode on Pro Plan

Auto mode 現在支援 Pro 方案，同時支援 Sonnet 4.6（原僅 Opus）。以背景安全檢查取代權限提示：

- 常規操作自動執行，無需中斷
- 破壞性或可疑操作被阻止並浮現告知

```bash
claude update          # 更新至最新版
# Shift+Tab 切換模式，auto mode 在帳號符合條件後出現
```

### 其他功能

| 功能 | 說明 |
|------|------|
| `/usage` 細分 | 顯示 skill、subagent、plugin、MCP server 各自消耗的方案配額 |
| `extra-usage` → `usage-credits` | 重命名，`/extra-usage` 舊名仍有效 |
| `/code-review` 指令 | 報告正確性 bug，支援 effort 等級（`/code-review high`）；`--comment` 發布行內 GitHub PR 評論 |
| Background sessions | 背景 session 出現在 `/resume`（標記 `bg`），`Ctrl+T` 固定後保持存活 |
| `claude agents --json` | 以 JSON 列出活躍 session，適合 status bar、session picker 腳本 |
| PowerShell 預設啟用 | Windows on Bedrock/Vertex/Foundry 預設啟用；`CLAUDE_CODE_USE_POWERSHELL_TOOL=0` 關閉 |
| Plugin 依賴管理 | `disable` 拒絕有依賴的 plugin；`enable` 強制啟用遞移依賴 |
| Plugin marketplace | 顯示預計 context 成本；安裝前列出 commands/agents/skills/hooks/MCP/LSP |
| `worktree.bgIsolation: "none"` | 背景 session 直接編輯工作目錄，不需 `EnterWorktree`（worktree 不實際的 repo 適用） |
| GFM checkboxes | Markdown 輸出渲染 GFM task list checkbox；`/diff` detail 支援鍵盤滾動 |
| Status line | JSON 輸入增加 GitHub repo 和 PR 資訊（自動偵測） |
| Enterprise：`allowAllClaudeAiMcps` | managed setting 同時載入 claude.ai cloud MCP connector 和 managed-mcp.json |

---

## Week 22（v2.1.150–v2.1.157）｜2026-05-25–29

### 主功能 1：Claude Opus 4.8

新預設模型（Max、Team Premium、Enterprise PAYG、Anthropic API），需 v2.1.154+：

```text
> /model claude-opus-4-8
```

- 預設 high effort；`/effort xhigh` 用於最難任務
- Fast mode on Opus 4.8：$10/$50 per MTok（2× 標準費率，約 2.5× 速度）
- Opus 4.7/4.6 fast mode 維持 $30/$150；Opus 4.6 fast mode 已 deprecated

### 主功能 2：Dynamic Workflows（Research Preview）

詳見 `32-dynamic-workflows.md`。管理指令：

```text
> /workflows
```

### 主功能 3：Security Guidance Plugin

自動審查 Claude 的程式碼變更以發現漏洞，並在同一 session 修復：

- **快速模式**：每次 edit 後執行 pattern check
- **模型模式**：每個 turn 結尾做 model review
- **深度模式**：commit 或 push 時執行 agentic review

```text
> /plugin install security-guidance@claude-plugins-official
> /reload-plugins
```

自訂規則：`.claude/claude-security-guidance.md`

### 主功能 4：Fast Mode on Opus 4.8

```text
> /fast
```

Opus 4.6 fast mode 已 deprecated。

### 其他功能

| 功能 | 說明 |
|------|------|
| `!` 前綴 shell 指令 | `claude agents` 中前綴 `!` 執行背景 job，可 attach/detach；`claude --bg --exec 'pytest -x'` |
| `.claude/skills` 自動載入 | 無需 marketplace，直接載入；`claude plugin init <name>` 初始化新 plugin |
| `/reload-skills` | 重新掃描 skill 目錄，不需重啟；`SessionStart` hook 可回傳 `reloadSkills: true` |
| `disallowed-tools` | Skill/command frontmatter 可移除特定工具 |
| `MessageDisplay` hook | 轉換或隱藏 assistant 訊息顯示文字 |
| `--fallback-model` | 主模型找不到時自動切換 fallback，不失敗整個 session |
| `defaultEnabled: false` | Plugin 安裝後預設不啟動，需手動 enable |
| Vim mode：`/` 反向歷史搜尋 | NORMAL mode 下 `/` 開啟反向歷史搜尋（Bash/Zsh vi-mode 對應） |
| 串流工具執行 | 所有情境（含 telemetry 停用、Bedrock/Vertex/Foundry）皆啟用 |
| `←←` agents view | 在 Bedrock/Vertex/Foundry 和 telemetry 停用時也可用 |
| Claude in Chrome | `/chrome` → "Select browser…" 選擇多個已連接瀏覽器 |
| MCP `mcp list` / `mcp get` | 顯示未批准的 `.mcp.json` server 為 pending，不再自動批准 |

---

## 重點速查

```text
# W21 關鍵指令
/code-review [low|medium|high|max]
/code-review high --comment          # 發布 PR 行內評論
/usage                               # 查看各來源使用量細分
claude agents --json                 # JSON session 列表

# W22 關鍵指令
/model claude-opus-4-8
/effort xhigh
/fast
/workflows
/plugin install security-guidance@claude-plugins-official
/reload-skills
```
