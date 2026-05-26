# 工作流程與核心技巧

整合自 Anthropic 官方最佳實踐、Boris Cherny（Claude Code 創始人）65+ 實戰技巧，以及社群驗證的工作模式。

## Explore → Plan → Implement → Commit 四階段

用 Plan Mode 分離探索與執行，是最高槓桿的單一習慣改變。

| 階段 | 說明 | 指令 |
|------|------|------|
| **Explore** | 進入 Plan Mode，Claude 僅讀取不修改 | `Shift+Tab` 兩次 |
| **Plan** | 請 Claude 建立詳細實作計畫 | `Ctrl+G` 在編輯器中調整計畫 |
| **Implement** | 切回 Normal Mode，依計畫執行 | `Shift+Tab` 切回 |
| **Commit** | 讓 Claude 撰寫 commit message 並開 PR | `"commit with a descriptive message and open a PR"` |

**何時跳過 Plan Mode**：任務範圍清楚且改動小（改 typo、加 log、改名稱）時直接執行。

**Plan Mode 最有價值的場景**：方法不確定、改動影響多個檔案、不熟悉被修改的程式碼。

## 給 Claude 驗證機制（最高槓桿單一動作）

包含測試、截圖、預期輸出，讓 Claude 能自我驗證。

| 策略 | 差 | 好 |
|------|----|----|
| 提供驗證標準 | "implement a function that validates email addresses" | "write a validateEmail function. example test cases: user@example.com → true, invalid → false. run the tests after implementing" |
| 視覺驗證 UI 變更 | "make the dashboard look better" | "[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them" |
| 解決根因 | "the build is failing" | "the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error" |

## Context 提供技巧

| 方式 | 說明 |
|------|------|
| `@filepath` | 在 prompt 中引用檔案（Claude 先讀再回應）|
| 貼圖 | 直接 copy/paste 或拖放截圖 |
| 貼 URL | 文件、API reference（加入 `/permissions` 白名單）|
| Pipe | `cat error.log \| claude` |
| 自行抓取 | 讓 Claude 透過 bash、MCP 工具讀取 |

---

## Boris Cherny 65+ 實戰技巧（七大類）

### 一、Session 管理

**`/branch`** — Fork 現有 Session，探索不同方案而不污染原線：

```bash
/branch
# 或從 CLI
claude --resume <session-id> --fork-session
```

**`/btw`** — 非阻塞側邊提問。在 agent 執行任務中途插入問題，不中斷當前進度，agent 完成目前工作後才回應：

```
/btw how do I spell dachshund?
> dachshund — German for "badger dog"
```

**`/focus`** — 隱藏所有中間工具呼叫與輸出，只顯示最終結果（toggle on/off）。

**`/loop`** — 本地定期重複執行 slash command：

```bash
/loop 5m /babysit          # 自動處理 code review、rebase、推 PR
/loop 30m /slack-feedback  # 每 30 分鐘針對 Slack 回饋開 PR
/loop 1h /pr-pruner        # 關閉過時的 PR
```

**Rewind**（`Esc + Esc`）— 走錯路徑時，回到失敗前再用新資訊重新 prompt，而非繼續在被污染的 context 中掙扎。

**Side Chat**（`⌘+;` / `Ctrl+;`）— 讀入主對話 context 但不回寫，適合探索性問題。

**`--bare` 旗標** — 跳過搜尋本地 CLAUDE.md/settings/MCP，加速 SDK 啟動最多 10×：

```bash
claude -p "summarize this codebase" --output-format=stream-json --bare
```

### 二、Multi-Agent 與平行化

**`/batch`** — Fan-out 大規模平行工作給數十至上百個 worktree agent：

```
/batch migrate all Python 2 modules to Python 3
```

**Git Worktrees** — 平行處理多個獨立任務的正確架構（不用 tmux 多視窗）：

```bash
git worktree add ../feature-a -b feature-a
git worktree add ../bugfix-b -b bugfix-b
# 各自在獨立目錄啟動 claude
```

**Subagent 委派門檻**：

- 需要讀取 ≥10 個檔案 → 委派 Explore agent
- 需要 >20 個工具呼叫 → 委派 Sub-agent
- 研究型任務 → 委派 Sub-agent（保護主 context）

### 三、Permission 與安全設定

**Auto mode** — 獨立 classifier 模型審查指令，只 block 有風險的操作（`Shift+Tab` 循環切換）。

**Permission allowlists** — 允許特定安全工具避免中斷：

```json
{
  "permissions": {
    "allow": ["Bash(npm run *)", "Bash(git commit *)", "Read(**)"],
    "deny": ["Bash(rm -rf *)", "Read(.env*)"],
    "ask": ["Bash(git push *)"]
  }
}
```

**Sandboxing** — OS 層隔離，限制 filesystem 和 network 存取範圍，啟用後 Bash 指令無需 prompt。

### 四、生產力技巧

**給 Claude 使用 CLI 工具的能力**：

```
Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.
```

Claude 善於學習不熟悉的 CLI 工具（`gh`、`aws`、`sentry-cli` 等）。

**讓 Claude 從特定位置找答案**：

```
look through ExecutionFactory's git history and summarize how its api came to be
```

**參照現有 pattern**：

```
look at how existing widgets are implemented on the home page.
HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget.
```

**Recaps** — 長時間 session 回來時，Claude 自動顯示摘要（在 `/config` 中可關閉）。

**Teleport** — 跨設備繼續 Session：

```bash
claude --teleport    # 將 cloud session 拉到本地 terminal
/teleport            # 同上
```

### 五、Git 與 PR 工作流

**讓 Claude 管理整個 PR 生命週期**：

```
commit with a descriptive message and open a PR
```

**Deep Review** — Commit 前讓 Claude 做代碼審查：

```
/deep-review   # 或設定為 hook 自動觸發
```

**Squash Merge 策略** — 保持 git log 整潔，讓每個功能只有一個 commit。

**PR 大小控制** — 每個 PR 控制在 400 行以內（Boris 的建議），大功能拆成多個小 PR。

### 六、Model 與 Effort 設定

| 模型 | 適用場景 |
|------|---------|
| Haiku 4.5 | 簡單查詢、格式化、低延遲任務 |
| Sonnet 4.6 | 標準開發任務（日常首選）|
| Opus 4.7 | 複雜架構設計、長程推理 |

**Effort 等級**（在 `settings.json` 設定）：

| Effort | 適用 |
|--------|------|
| `xhigh` | Opus 4.7 的多數 coding / agentic 任務（推薦預設）|
| `high` | 多數智力敏感任務的最低建議值 |
| `medium` | 降低 token，犧牲一定智力 |
| `low` | 短、範圍小、延遲敏感的任務 |

**Fast Mode**（`/fast`）— 使用 Opus 但更快的輸出（不降級到小模型）。

### 七、W20+ 新功能

**`/goal`** — 設定 session 目標，Claude 在每次回應後追蹤完成度。

**Agent View** — 視覺化 sub-agent 的狀態與進度。

**Plugin 依賴管理** — Plugin 更新時自動重新安裝 MCP server 依賴。

---

## CLAUDE.md 應該放什麼

| 應放 ✅ | 不應放 ❌ |
|--------|---------|
| Claude 猜不到的 bash 指令 | Claude 讀程式碼就能知道的事 |
| 與預設不同的 code style 規則 | 標準語言慣例 |
| 測試指令與偏好的 test runner | 詳細 API 文件（改放連結）|
| Branch 命名、PR 慣例 | 頻繁變更的資訊 |
| 專案特定架構決策 | 詳細教學 |
| 開發環境特殊性（必要的 env var）| 逐檔描述 codebase |
| 常見陷阱與非直覺行為 | 「寫乾淨程式碼」等不言而喻的事 |

**關鍵原則**：每行問自己「移除這行 Claude 會犯錯嗎？」不會就刪。CLAUDE.md 過長 = Claude 忽略實際指令。

---

## 延伸閱讀

- [官方最佳實踐](https://code.claude.com/docs/en/best-practices)
- [Common Workflows](https://code.claude.com/docs/en/common-workflows)
- [Hooks 設計模式](/resources/best-practices/hooks)
- [Permission 設定](/resources/best-practices/permissions)
