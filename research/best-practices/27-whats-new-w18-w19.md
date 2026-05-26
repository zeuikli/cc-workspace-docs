# Claude Code What's New — 週版本要點彙整（2026-W18 至 W19）

> 來源：https://code.claude.com/docs/en/whats-new/2026-w18  
>       https://code.claude.com/docs/en/whats-new/2026-w19  
> 收錄日期：2026-05-10  
> 涵蓋：2026-04-27 至 2026-05-08，版本 v2.1.120 → v2.1.136，2 週 / 6 個主要功能

---

## 快速索引

| 週別 | 版本 | 主要功能 |
|------|------|---------|
| W18（Apr 27–May 1）| v2.1.120–126 | Windows 無需 Git Bash、claude project purge、PR URL 恢復 Session、瀏覽器外 OAuth 登入 |
| W19（May 4–8）| v2.1.128–136 | Plugin .zip/URL 載入、Ctrl+R 跨專案歷史搜尋、worktree.baseRef、auto mode hard deny、Hooks 看到 effort level |

---

## Week 18 · April 27 – May 1（v2.1.120–v2.1.126）

### Windows 無需 Git Bash

Git for Windows 不再必要。當 Bash 不存在時，Claude Code 改用 PowerShell 作為 shell 工具。PowerShell 7 無論透過 Microsoft Store、MSI（不帶 PATH）或 `.NET` global tool 安裝，均能自動偵測。

---

### `claude auth login`：無瀏覽器回調登入（v2.1.126）

WSL2、SSH Session、Container 等無法 localhost 回調的環境，現在可以直接在 terminal 貼入 OAuth code 完成登入：

```bash
claude auth login
# 瀏覽器開啟後，將頁面上的 code 貼入 terminal
```

同版本修復了慢速網路/Proxy 的登入逾時，以及 IPv6-only devcontainer 的相容性問題。

---

### `claude project purge`（v2.1.126）

清除指定專案的所有 Claude Code 本地狀態：transcript、task、file history、config entry。

```bash
# 預覽將被刪除的內容（不實際執行）
claude project purge --dry-run

# 清除當前專案（會確認提示）
claude project purge

# 跳過確認直接執行
claude project purge -y

# 清除所有專案
claude project purge --all
```

---

### PR URL 恢復 Session（v2.1.122）

用 `gh pr create` 建立的 PR 會自動與建立它的 session 連結。之後可以貼入 PR URL 回到該 session：

```text
> /resume
```

在 picker 中貼入 PR URL（輸入第一個字元進入搜尋模式）→ 列表自動過濾到對應 session → Enter 恢復。

支援 GitHub、GitHub Enterprise、GitLab、Bitbucket 的 PR/MR URL。

也可直接用 CLI 指定：

```bash
claude --from-pr 1234
```

---

### Other Wins（W18）

| 功能 | 說明 |
|------|------|
| MCP `alwaysLoad: true` | MCP server 可設定此選項，跳過 tool-search deferral，所有工具常態可用 |
| `claude plugin prune` | 移除孤立的自動安裝 plugin 依賴；`plugin uninstall --prune` 一次清除 |
| `/skills` 搜尋框 | 輸入文字即時過濾，長清單不用滾動 |
| `PostToolUse` 任意工具輸出替換 | 透過 `hookSpecificOutput.updatedToolOutput`，可替換任何工具輸出（不限 MCP）|
| `claude ultrareview`（CLI 子命令）| 非互動式 `/ultrareview`，可在 CI/scripts 中使用；`--json` 輸出原始結果；成功 exit 0，失敗 exit 1 |
| `/terminal-setup` | 啟用 iTerm2 clipboard access，讓 `/copy` 在 tmux 中也能運作 |
| Vertex AI mTLS | 支援 X.509 certificate-based Workload Identity Federation |

---

## Week 19 · May 4–8（v2.1.128–v2.1.136）

### Plugin 從 .zip 與 URL 載入

`--plugin-dir` 現在接受 `.zip` 壓縮檔，新增 `--plugin-url` 從 URL 下載 plugin 壓縮包用於當前 session：

```bash
# 從 URL 直接載入 plugin（適合試用或內部 artifact store）
claude --plugin-url https://example.com/my-plugin.zip

# 從本地 zip 載入
claude --plugin-dir ./my-plugin.zip
```

---

### Ctrl+R 跨專案歷史搜尋（v2.1.129）

`Ctrl+R` reverse-search 改為預設搜尋所有專案的歷史，`Ctrl+S` 切換縮小到當前專案/session：

```text
Ctrl+R          → 搜尋全部專案歷史
（搜尋中）Ctrl+S → 縮小到當前專案
```

---

### Other Wins（W19）

| 功能 | 說明 |
|------|------|
| `worktree.baseRef` | 設定新 worktree 的分支基準：`fresh`（遠端預設分支，default）或 `head`（本地 HEAD）；`fresh` 確保未推送的 commit 不會進入新 worktree |
| `settings.autoMode.hard_deny` | Auto mode 中無條件封鎖指定操作，不受 allow 例外影響 |
| Hooks 看到 effort level | Hook 輸入 JSON 新增 `effort.level` 欄位；Bash tool 可讀取 `$CLAUDE_EFFORT` 環境變數 |
| `CLAUDE_CODE_SESSION_ID` | 現在傳遞到 Bash tool 子程序環境，與 hooks 接收的 `session_id` 一致 |
| Sub-agent cache 優化 | Sub-agent 進度摘要命中 prompt cache，`cache_creation` token 成本降低約 3× |
| `--channels` console auth | Channels 現在支援 API key（console）認證，不限 OAuth |
| MCP `parentSettingsBehavior` | admin key 讓管理員將 SDK `managedSettings` 納入 policy merge |
| `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` | 關閉全螢幕 alternate-screen 渲染，回到 terminal 原生 scrollback |

---

## 對 Workspace 的影響

| 功能 | 建議動作 |
|------|---------|
| `claude project purge` | 可加入 housekeeping routine，定期清理舊專案 state |
| PR URL resume | 在 core.md 補充：建立 PR 後可用 `--from-pr` 快速恢復 session |
| `PostToolUse` 任意輸出替換 | auto-sync.md 中的 PostToolUse hook 可升級支援非 MCP 工具輸出替換 |
| `worktree.baseRef` | 若使用 worktree 隔離策略，可在 settings.json 設定 `worktree.baseRef: "fresh"` |
| `autoMode.hard_deny` | 若有絕對禁止的命令，可在 settings.json 設定 hard deny rules |
| Hooks effort level | Hook scripts 可根據 `$CLAUDE_EFFORT` 調整行為（如 xhigh 時做額外驗證）|
| Sub-agent cache 優化 | 無需額外設定，自動生效；預期可見 cache_creation token 下降 |
