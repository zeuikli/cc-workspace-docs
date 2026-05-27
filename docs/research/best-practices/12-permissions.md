---
title: "細粒度 Permission 設定完整指南"
source: "https://code.claude.com/docs/en/permissions"
type: best-practices
---

# 細粒度 Permission 設定完整指南

> 來源：https://code.claude.com/docs/en/permissions
> 收錄日期：2026-05-01
> 涵蓋：Permission 系統架構、wildcard 語法、allow/block/prompt 三種模式、工具特定規則、Managed Settings 組織 policy

---

## Permission 系統架構

Claude Code 使用分層 permission 系統平衡能力與安全：

| 工具類型 | 範例 | 需要核准？ | "Yes, don't ask again" 行為 |
|---------|------|-----------|----------------------------|
| Read-only | File reads, Grep | 否 | N/A |
| Bash 指令 | Shell execution | 是 | 永久（per project directory + command）|
| File modification | Edit/write files | 是 | 到 session 結束為止 |

**規則評估順序**：`deny → ask → allow`，**第一個匹配的規則勝出**。deny 規則永遠優先。

---

## Permission 模式

透過 `settings.json` 的 `defaultMode` 設定：

| 模式 | 說明 |
|------|------|
| `default` | 標準模式：每個工具首次使用時提示 |
| `acceptEdits` | 自動接受 file edits 和常見 filesystem 指令（`mkdir`, `touch`, `mv`, `cp`）|
| `plan` | Plan Mode：Claude 只能分析，不能修改檔案或執行指令 |
| `auto` | 自動核准工具呼叫，含背景安全檢查（Research Preview）|
| `dontAsk` | 自動拒絕工具，除非透過 `/permissions` 或 `allow` 規則預先核准 |
| `bypassPermissions` | 跳過所有 permission prompt（`rm -rf /` 類操作仍會提示）|

> **`bypassPermissions` 警告**：跳過所有 prompt，包含對 `.git`、`.claude`、`.vscode`、`.idea`、`.husky` 的寫入。僅限隔離環境（container/VM）使用。

**禁用特定模式**（適用於 Managed Settings）：
- `permissions.disableBypassPermissionsMode: "disable"` — 防止 bypass 模式
- `permissions.disableAutoMode: "disable"` — 防止 auto 模式

---

## Permission 規則語法

格式：`Tool` 或 `Tool(specifier)`

### 匹配工具的所有用途

| 規則 | 效果 |
|------|------|
| `Bash` | 匹配所有 Bash 指令 |
| `WebFetch` | 匹配所有 web fetch 請求 |
| `Read` | 匹配所有 file reads |

`Bash(*)` 等同於 `Bash`。

### Wildcard 模式

Bash 規則支援 `*` glob pattern，可出現在指令任何位置：

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git commit *)",
      "Bash(git * main)",
      "Bash(* --version)",
      "Bash(* --help *)"
    ],
    "deny": [
      "Bash(git push *)"
    ]
  }
}
```

**重要細節**：
- `Bash(ls *)` 匹配 `ls -la` 但**不匹配** `lsof`（空格前有 word boundary）
- `Bash(ls*)` 匹配 `ls -la` 和 `lsof`（無 word boundary）
- `:*` 後綴等同 trailing wildcard：`Bash(ls:*)` 和 `Bash(ls *)` 等效
- 單個 `*` 跨越多個 argument：`Bash(git *)` 匹配 `git log --oneline --all`

---

## 各工具的 Permission 規則

### Bash 規則詳解

#### 複合指令（Compound Commands）

Claude Code 能識別 shell operator，`Bash(safe-cmd *)` **不會**授權 `safe-cmd && other-cmd`。

識別的 separator：`&&`, `||`, `;`, `|`, `|&`, `&`, newlines。規則必須對每個 sub-command 獨立匹配。

批准複合指令時，Claude Code 為每個需核准的 sub-command 分別儲存規則（而非整條複合指令規則），最多 5 條規則。

#### Process Wrappers 自動剝離

以下 wrapper 在匹配前自動剝離，讓 `Bash(npm test *)` 也能匹配 `timeout 30 npm test`：

`timeout`, `time`, `nice`, `nohup`, `stdbuf`, bare `xargs`（無 flag 時）

**不剝離**：`direnv exec`, `devbox run`, `mise exec`, `npx`, `docker exec`（這些執行 argument 時應寫含 wrapper 的完整規則）。

`watch`, `setsid`, `ionice`, `flock` 永遠需要 prompt，**無法**用前綴規則自動核准。

`find -exec/-delete` 也永遠 prompt，`Bash(find *)` 不涵蓋這些形式。

#### 內建唯讀指令（免 prompt）

Claude Code 內建白名單，以下指令永遠免 prompt：

`ls`, `cat`, `head`, `tail`, `grep`, `find`, `wc`, `diff`, `stat`, `du`, `cd`，以及 git 的唯讀形式。

> 此白名單不可設定；如需強制 prompt，加 `ask` 或 `deny` 規則。

#### URL 過濾警告

`Bash(curl http://github.com/ *)` 等 URL 過濾**脆弱且不可靠**，容易被繞過：

```
# 以下變化均不會匹配：
curl -X GET http://github.com/...      # option 在 URL 前
curl https://github.com/...            # 不同 protocol
curl -L http://bit.ly/xyz              # redirect 到 github
```

**替代方案**：
- 用 `deny` 封鎖 `curl`/`wget`，改用 `WebFetch(domain:github.com)` 管控
- 用 `PreToolUse hook` 驗證 URL

### PowerShell 規則

語法與 Bash 相同，常見 alias 自動正規化：`PowerShell(Get-ChildItem *)` 也匹配 `gci`, `ls`, `dir`。匹配大小寫不敏感。

### Read 與 Edit 規則

**Edit 規則**適用所有修改檔案的內建工具；**Read 規則**對讀取類工具（Grep/Glob）做 best-effort 應用。

> **重要**：Read/Edit deny 規則只影響 Claude 的內建 file tools，**不影響** Bash subprocess（`cat .env` 不受 `Read(./.env)` deny 規則限制）。如需 OS 層強制，啟用 sandbox。

#### 路徑前綴規則（gitignore 規格）

| 前綴 | 意義 | 範例 | 解析結果 |
|------|------|------|---------|
| `//path` | 絕對路徑（從 filesystem root）| `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**` |
| `~/path` | 從 home directory | `Read(~/Documents/*.pdf)` | `/Users/alice/Documents/*.pdf` |
| `/path` | 相對於 project root | `Edit(/src/**/*.ts)` | `<project root>/src/**/*.ts` |
| `path` 或 `./path` | 相對於當前目錄 | `Read(*.env)` | `<cwd>/*.env` |

> **警告**：`/Users/alice/file` **不是**絕對路徑，是相對於 project root。絕對路徑用 `//Users/alice/file`。

Windows 路徑轉為 POSIX 後匹配：`C:\Users\alice` → `/c/Users/alice`。

#### Glob pattern 說明

- `*`：匹配單一目錄內的檔案
- `**`：遞迴跨目錄匹配
- 允許整個工具（無括號）：`Read`、`Edit`、`Write`

#### Symlink 處理

- **Allow 規則**：symlink 本身和目標**都必須**匹配才放行，只匹配一個則 fallback 到提示
- **Deny 規則**：symlink 或目標任一匹配就封鎖

### WebFetch 規則

```
WebFetch(domain:example.com)   # 匹配對 example.com 的所有請求
```

### MCP 規則

```
mcp__puppeteer                       # 匹配 puppeteer server 的所有工具
mcp__puppeteer__*                    # 等同上方（wildcard 語法）
mcp__puppeteer__puppeteer_navigate   # 只匹配特定工具
```

### Agent（Subagent）規則

```
Agent(Explore)             # 匹配 Explore subagent
Agent(Plan)                # 匹配 Plan subagent
Agent(my-custom-agent)     # 匹配自訂 subagent
```

停用 Explore agent 範例：

```json
{
  "permissions": {
    "deny": ["Agent(Explore)"]
  }
}
```

---

## 用 Hooks 擴充 Permission

`PreToolUse hook` 在 permission prompt 前執行，輸出可以：deny 工具呼叫、強制 prompt、或跳過 prompt。

**關鍵行為**：
- Hook 決策**不 bypass** permission 規則
- Hook 返回 `allow` 仍受 deny/ask 規則約束（deny 規則仍封鎖，ask 規則仍提示）
- Hook exit code 2 封鎖工具，即使 allow 規則存在也阻斷

> 應用場景：在 `allow` 列表加 `Bash`，再用 hook 封鎖特定危險指令。參考[封鎖保護檔案編輯](https://code.claude.com/docs/en/hooks-guide#block-edits-to-protected-files)。

---

## Working Directories

Claude 預設存取啟動所在目錄的檔案，可擴充：

| 方式 | 命令 |
|------|------|
| 啟動時指定 | `--add-dir <path>` |
| Session 中指定 | `/add-dir` |
| 永久設定 | `additionalDirectories` in settings |

**注意**：`--add-dir` 擴充的是**檔案存取範圍**，不是完整設定 root。以下設定**會**從 `--add-dir` 目錄載入：

| 設定類型 | 從 `--add-dir` 載入 |
|---------|-------------------|
| Skills（`.claude/skills/`）| 是（live reload）|
| Plugin settings | 只有 `enabledPlugins` 和 `extraKnownMarketplaces` |
| CLAUDE.md、rules、CLAUDE.local.md | 只在 `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` 時 |

其他設定（subagents、hooks 等）只從 cwd、`~/.claude/`、Managed Settings 載入。

---

## Permission 與 Sandbox 的互補關係

| 層次 | 範圍 | 工具 |
|------|------|------|
| **Permissions** | 控制 Claude Code 可使用哪些工具、存取哪些檔案或域名 | Bash、Read、Edit、WebFetch、MCP 等所有工具 |
| **Sandboxing** | OS 層強制限制 Bash 工具的 filesystem 和 network 存取 | 只限 Bash 指令及其子程序 |

啟用 sandbox 且 `autoAllowBashIfSandboxed: true`（預設值）時，sandbox 內的 Bash 無需 prompt。但 explicit deny 規則仍生效，`rm`/`rmdir` 指向根目錄等高危路徑仍會提示。

---

## Managed Settings（組織 Policy）

管理員可部署無法被 user/project settings 覆蓋的 managed settings。透過 MDM/OS-level policies、managed settings 檔案、或 server-managed settings 配發。

### 只能在 Managed Settings 使用的設定

| 設定 | 說明 |
|------|------|
| `allowedChannelPlugins` | Channel plugin allowlist |
| `allowManagedHooksOnly` | `true` 時只載入 managed hooks，封鎖其他所有 hook |
| `allowManagedMcpServersOnly` | `true` 時只允許 managed settings 的 MCP server |
| `allowManagedPermissionRulesOnly` | `true` 時禁止 user/project settings 定義 allow/ask/deny 規則 |
| `blockedMarketplaces` | Marketplace 黑名單 |
| `channelsEnabled` | 允許 Team/Enterprise 使用 Channels |
| `forceRemoteSettingsRefresh` | `true` 時 CLI 啟動前強制取得最新 remote managed settings |
| `sandbox.filesystem.allowManagedReadPathsOnly` | 只允許 managed 的 `allowRead` 路徑 |
| `sandbox.network.allowManagedDomainsOnly` | 只允許 managed 的 allowedDomains，非白名單自動封鎖 |
| `strictKnownMarketplaces` | 控制用戶可安裝的 plugin marketplace 來源 |
| `wslInheritsWindowsSettings` | WSL 繼承 Windows 的 managed settings |

---

## Settings 優先序

1. **Managed settings**（最高，無法被任何層覆蓋）
2. Command line arguments（臨時 session override）
3. Local project settings（`.claude/settings.local.json`）
4. Shared project settings（`.claude/settings.json`）
5. **User settings**（`~/.claude/settings.json`，最低）

> 工具在任一層被 deny，其他層都無法 allow。例如 managed deny 不能被 `--allowedTools` 覆蓋。

---

## 範例設定

官方提供多種部署情境的 starter settings：[github.com/anthropics/claude-code/tree/main/examples/settings](https://github.com/anthropics/claude-code/tree/main/examples/settings)

---

## 延伸閱讀

- [Settings](https://code.claude.com/docs/en/settings) — 完整設定參考（含 permission settings 表格）
- [Configure auto mode](https://code.claude.com/docs/en/auto-mode-config) — 設定 auto mode classifier
- [Sandboxing](https://code.claude.com/docs/en/sandboxing) — OS 層 filesystem/network 隔離
- [Hooks](https://code.claude.com/docs/en/hooks-guide) — 自動化工作流程與擴充 permission 評估
- [Security](https://code.claude.com/docs/en/security) — 安全最佳實踐
