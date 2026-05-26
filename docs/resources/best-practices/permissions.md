# Permission 細粒度設定

Claude Code 使用分層 permission 系統平衡能力與安全。理解這個系統是設計有效 harness 的基礎。

## 系統架構

| 工具類型 | 範例 | 需要核准？ | "Yes, don't ask again" 行為 |
|---------|------|-----------|----------------------------|
| Read-only | File reads, Grep | 否 | N/A |
| Bash 指令 | Shell execution | 是 | 永久（per project directory + command）|
| File modification | Edit/write files | 是 | 到 session 結束為止 |

**規則評估順序**：`deny → ask → allow`，第一個匹配的規則勝出。deny 規則永遠優先。

---

## 五種 Permission 模式

透過 `settings.json` 的 `defaultMode` 設定：

| 模式 | 說明 |
|------|------|
| `default` | 標準模式：每個工具首次使用時提示 |
| `acceptEdits` | 自動接受 file edits 和常見 filesystem 指令（`mkdir`, `touch`, `mv`, `cp`）|
| `plan` | Plan Mode：Claude 只能分析，不能修改檔案或執行指令 |
| `auto` | 自動核准工具呼叫，含背景安全檢查（Research Preview）|
| `dontAsk` | 自動拒絕工具，除非透過 `/permissions` 或 `allow` 規則預先核准 |
| `bypassPermissions` | 跳過所有 permission prompt（僅限隔離環境）|

> **`bypassPermissions` 警告**：跳過所有 prompt，包含對 `.git`、`.claude`、`.vscode`、`.idea`、`.husky` 的寫入。僅限 container/VM 隔離環境使用。

---

## 規則語法

格式：`Tool` 或 `Tool(specifier)`

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

## Bash 規則詳解

### 複合指令（Compound Commands）

Claude Code 能識別 shell operator，`Bash(safe-cmd *)` **不會**授權 `safe-cmd && other-cmd`。

識別的 separator：`&&`、`||`、`;`、`|`、`|&`、`&`、newlines。規則必須對每個 sub-command 獨立匹配。

### Process Wrappers 自動剝離

以下 wrapper 在匹配前自動剝離，讓 `Bash(npm test *)` 也能匹配 `timeout 30 npm test`：

`timeout`、`time`、`nice`、`nohup`、`stdbuf`、bare `xargs`（無 flag 時）

**不剝離**：`direnv exec`、`devbox run`、`mise exec`、`npx`、`docker exec`（需寫含 wrapper 的完整規則）。

`watch`、`setsid`、`ionice`、`flock` 永遠需要 prompt，**無法**用前綴規則自動核准。

`find -exec/-delete` 也永遠 prompt，`Bash(find *)` 不涵蓋這些形式。

### 內建唯讀指令（免 prompt）

Claude Code 內建白名單，以下指令永遠免 prompt：

`ls`、`cat`、`head`、`tail`、`grep`、`find`、`wc`、`diff`、`stat`、`du`、`cd`，以及 git 的唯讀形式。

> 此白名單不可設定；如需強制 prompt，加 `ask` 或 `deny` 規則。

### URL 過濾警告

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

---

## Read 與 Edit 規則

### 路徑前綴規則（gitignore 規格）

| 前綴 | 意義 | 範例 | 解析結果 |
|------|------|------|---------|
| `//path` | 絕對路徑（從 filesystem root）| `Read(//Users/alice/secrets/**)` | `/Users/alice/secrets/**` |
| `~/path` | 從 home directory | `Read(~/Documents/*.pdf)` | `/Users/alice/Documents/*.pdf` |
| `/path` | 相對於 project root | `Edit(/src/**/*.ts)` | `<project root>/src/**/*.ts` |
| `path` 或 `./path` | 相對於當前目錄 | `Read(*.env)` | `<cwd>/*.env` |

> **警告**：`/Users/alice/file` **不是**絕對路徑，是相對於 project root。絕對路徑用 `//Users/alice/file`。

### Glob pattern

- `*`：匹配單一目錄內的檔案
- `**`：遞迴跨目錄匹配

### Symlink 處理

- **Allow 規則**：symlink 本身和目標**都必須**匹配才放行，只匹配一個則 fallback 到提示
- **Deny 規則**：symlink 或目標任一匹配就封鎖

> **重要**：Read/Edit deny 規則只影響 Claude 的內建 file tools，**不影響** Bash subprocess（`cat .env` 不受 `Read(./.env)` deny 規則限制）。如需 OS 層強制，啟用 sandbox。

---

## 各工具規則

### WebFetch 規則

```json
"WebFetch(domain:example.com)"   // 匹配對 example.com 的所有請求
```

### MCP 規則

```json
"mcp__puppeteer"                       // 匹配 puppeteer server 的所有工具
"mcp__puppeteer__puppeteer_navigate"   // 只匹配特定工具
```

### Subagent 規則

```json
{
  "permissions": {
    "deny": ["Agent(Explore)"]          // 停用 Explore agent
  }
}
```

---

## Permission 與 Sandbox 的互補關係

| 層次 | 範圍 | 工具 |
|------|------|------|
| **Permissions** | 控制 Claude Code 可使用哪些工具、存取哪些檔案或域名 | Bash、Read、Edit、WebFetch、MCP 等所有工具 |
| **Sandboxing** | OS 層強制限制 Bash 工具的 filesystem 和 network 存取 | 只限 Bash 指令及其子程序 |

啟用 sandbox 且 `autoAllowBashIfSandboxed: true`（預設值）時，sandbox 內的 Bash 無需 prompt。但 explicit deny 規則仍生效，`rm`/`rmdir` 指向根目錄等高危路徑仍會提示。

---

## Managed Settings（組織 Policy）

管理員可部署無法被 user/project settings 覆蓋的 managed settings：

| 設定 | 說明 |
|------|------|
| `allowManagedHooksOnly` | `true` 時只載入 managed hooks，封鎖其他所有 hook |
| `allowManagedMcpServersOnly` | `true` 時只允許 managed settings 的 MCP server |
| `allowManagedPermissionRulesOnly` | `true` 時禁止 user/project settings 定義 allow/ask/deny 規則 |
| `sandbox.network.allowManagedDomainsOnly` | 只允許 managed 的 allowedDomains，非白名單自動封鎖 |

### Settings 優先序

1. **Managed settings**（最高，無法被任何層覆蓋）
2. Command line arguments（臨時 session override）
3. Local project settings（`.claude/settings.local.json`）
4. Shared project settings（`.claude/settings.json`）
5. **User settings**（`~/.claude/settings.json`，最低）

> 工具在任一層被 deny，其他層都無法 allow。

---

## 延伸閱讀

- [官方 Permissions 文件](https://code.claude.com/docs/en/permissions)
- [Sandboxing 文件](https://code.claude.com/docs/en/sandboxing)
- [Hooks 設計模式](/resources/best-practices/hooks)
- [Lecture 06：安全沙箱與 Proxy](/lectures/lecture-06-security/)
