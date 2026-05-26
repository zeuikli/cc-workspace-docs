---
title: Claude Code Plugin 系統完整指南
source: "https://code.claude.com/docs/en/plugins"
type: best-practices
---

# Claude Code Plugin 系統完整指南

> 來源：https://code.claude.com/docs/en/plugins  
> 補充來源：https://code.claude.com/docs/en/plugins-reference  
> 收錄日期：2026-05-01  
> 涵蓋：Plugin vs Standalone 比較、Manifest 結構、全部 Plugin 組件類型、Quickstart、Marketplace 分發、遷移策略

---

## 一、Plugin vs Standalone 設定

Claude Code 支援兩種擴展方式：

| 面向 | **Standalone**（`.claude/` 目錄）| **Plugin**（含 `.claude-plugin/plugin.json`）|
|------|------|------|
| Skill 名稱 | `/hello` | `/plugin-name:hello`（有命名空間）|
| 適用場景 | 個人工作流、單一專案客製化、快速實驗 | 跨專案共享、團隊分發、marketplace 發佈 |
| 版本控制 | 手動管理 | 內建版本策略 |
| 跨專案安裝 | 手動複製 | `/plugin install` |

**決策建議**：先用 standalone 快速迭代 → 準備分享時轉換為 plugin。

---

## 二、Plugin 目錄結構

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        ← 唯一放在 .claude-plugin/ 內的檔案
├── skills/
│   └── my-skill/
│       └── SKILL.md
├── commands/              ← 舊格式（平面 markdown 檔案），新 plugin 用 skills/
├── agents/
│   └── my-agent.md
├── hooks/
│   └── hooks.json
├── .mcp.json              ← MCP server 設定
├── .lsp.json              ← LSP server 設定
├── monitors/
│   └── monitors.json
├── bin/
│   └── my-tool            ← 可執行檔，自動加入 Bash PATH
└── settings.json          ← Plugin 啟用時套用的預設設定
```

**常見錯誤**：`skills/`、`agents/`、`hooks/` **不可放在 `.claude-plugin/` 內**，只有 `plugin.json` 放在裡面。

---

## 三、Manifest（plugin.json）

```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "homepage": "https://example.com",
  "repository": "https://github.com/user/repo",
  "license": "MIT"
}
```

| 欄位 | 說明 |
|------|------|
| `name` | 唯一識別符 + skill 命名空間前綴（`/name:skill`）|
| `description` | Plugin manager 中顯示的說明 |
| `version` | 選填。設定後用戶只在 bump 版本時收到更新；未設定時以 git commit SHA 為版本 |
| `author` | 選填，用於署名 |

---

## 四、Quickstart — 建立第一個 Plugin

```bash
# 1. 建立目錄
mkdir my-first-plugin
mkdir my-first-plugin/.claude-plugin

# 2. 建立 manifest
cat > my-first-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-first-plugin",
  "description": "A greeting plugin",
  "version": "1.0.0"
}
EOF

# 3. 建立 skill
mkdir -p my-first-plugin/skills/hello
cat > my-first-plugin/skills/hello/SKILL.md << 'EOF'
---
description: Greet the user with a friendly message
disable-model-invocation: true
---

Greet the user warmly and ask how you can help them today.
EOF

# 4. 測試（--plugin-dir 旗標）
claude --plugin-dir ./my-first-plugin
```

在 session 中執行：

```text
> /my-first-plugin:hello
```

多個 plugin 同時載入：

```bash
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two
```

**`$ARGUMENTS` 用法**（接受 skill 後的文字）：

```markdown
---
description: Greet the user with a personalized message
---

Greet the user named "$ARGUMENTS" warmly.
```

```text
> /my-first-plugin:hello Alex
```

---

## 五、Plugin 組件詳解

### 5.1 Skills（`skills/`）

每個 skill 是 `skills/<name>/SKILL.md` 的資料夾，Claude 依 context 自動選用。

```yaml
---
description: Reviews code for best practices. Use when reviewing code or checking PRs.
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage
```

安裝 plugin 後 `/reload-plugins` 載入新 Skill。詳見 `skill-authoring.md`（本 workspace 已收錄）。

### 5.2 Agents（`agents/`）

自訂 agent 定義（system prompt、model、工具限制）。

### 5.3 Hooks（`hooks/hooks.json`）

Hook 設定放在 `hooks/hooks.json`，格式與 `settings.json` 的 `hooks` key 相同：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{"type": "command", "command": "jq -r '.tool_input.file_path' | xargs npm run lint:fix"}]
      }
    ]
  }
}
```

### 5.4 MCP Servers（`.mcp.json`）

Plugin 專屬 MCP server 設定。

### 5.5 LSP Servers（`.lsp.json`）

提供 code intelligence（主要對已有官方 LSP plugin 的語言不需要自建）：

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

用戶安裝此 plugin 後需自行安裝 language server binary。

### 5.6 Background Monitors（`monitors/monitors.json`）

Plugin 啟用後自動啟動的背景監控進程：

```json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]
```

每行 stdout 以 notification 形式注入 Claude 對話。W16 更新：可在 manifest 頂層加 `monitors` key，並支援 skill invoke 時觸發。

### 5.7 bin/ — PATH 可執行檔

放在 `bin/` 的可執行檔在 plugin 啟用時自動加入 Bash tool 的 PATH。

### 5.8 settings.json — Plugin 預設設定

Plugin 啟用時套用的預設設定（目前支援 `agent` 和 `subagentStatusLine`）：

```json
{
  "agent": "security-reviewer"
}
```

此設定讓 plugin 的 `agents/security-reviewer.md` 成為 main thread agent（改變 Claude Code 的預設行為）。

---

## 六、開發工作流

### 本地測試

```bash
# 使用 --plugin-dir 載入（不需安裝）
claude --plugin-dir ./my-plugin

# 同名本地 plugin 優先於已安裝的 marketplace 版本
# 修改後不需重啟，用：
> /reload-plugins
```

### Debug checklist

1. 確認 `skills/`、`agents/`、`hooks/` 在 **plugin root**（不是 `.claude-plugin/` 內）
2. 各組件分開測試
3. 參見官方 `Debugging and development tools` 文件取得 CLI 診斷指令

---

## 七、發佈與分發（Marketplace）

### 準備步驟

1. 加入 `README.md`（安裝 + 使用說明）
2. 決定版本策略：設定明確 `version` 或依賴 git commit SHA
3. 使用 plugin marketplace 分發

### 提交到官方 Marketplace

- Claude.ai：`claude.ai/settings/plugins/submit`
- Console：`platform.claude.com/plugins/submit`

上架後可在你的 CLI 中提示用戶安裝（`Plugin Hints` 功能）。

### Plugin Tag 指令（v2.1.117+）

```bash
claude plugin tag    # 建立 release git tag，含 version validation
```

### 私有團隊 Marketplace

在私有 repo host marketplace，讓 plugin 只在組織內分發（詳見 `plugin-marketplaces` 文件）。

---

## 八、從 Standalone 遷移到 Plugin

```bash
# 1. 建立 plugin 結構
mkdir -p my-plugin/.claude-plugin
# 建立 plugin.json（見上面範例）

# 2. 複製現有設定
cp -r .claude/commands my-plugin/
cp -r .claude/agents my-plugin/
cp -r .claude/skills my-plugin/

# 3. 遷移 hooks（從 settings.json 的 hooks key）
mkdir my-plugin/hooks
# 建立 my-plugin/hooks/hooks.json

# 4. 測試
claude --plugin-dir ./my-plugin
```

| Standalone | Plugin |
|-----------|-------|
| `.claude/commands/` 中的檔案 | `plugin-name/commands/` |
| `settings.json` 中的 hooks | `hooks/hooks.json` |
| 只在當前專案可用 | `/plugin install` 跨專案安裝 |
| 手動複製分享 | Marketplace 一鍵安裝 |

遷移後可從 `.claude/` 移除原始檔案（本地 plugin 優先於 marketplace 版本）。

---

## 九、Plugin 與本 Workspace 的關係

本 workspace 目前使用 **standalone** 模式（`.claude/skills/`、`.claude/agents/`）。Plugin 模式適合：

- 將現有 skills（如 `deep-review`、`harness-eval`、`score-article`）打包為可分享的 plugin
- 為 `bin/` 目錄封裝 helper scripts（現有 `scripts/` 可遷移）
- 透過 `monitors/` 實作自動化背景監控

**遷移優先序**：`/deep-review` skill → 最具分享價值，適合率先打包。

---

## Known Gotchas

- `skills/`、`agents/`、`hooks/` 必須放在 **plugin root**，不是 `.claude-plugin/` 內（最常見錯誤）
- Skill 命名空間：`/plugin-name:skill-name`，不支援無前綴的短名稱
- `settings.json` 目前只有 `agent` 和 `subagentStatusLine` 兩個 key 有效，其他靜默忽略
- Version 欄位未設定時，每次 git commit 都算新版本（用戶每次 git pull 都觸發更新）
- `--plugin-dir` 無法覆蓋 managed settings 強制啟用的 marketplace plugin
- LSP plugin 安裝後用戶仍需自行安裝 language server binary（plugin 不含 binary 本身）
