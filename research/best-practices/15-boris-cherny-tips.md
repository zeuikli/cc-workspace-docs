# Boris Cherny Claude Code Tips — 主題分類整合

> 來源：shanraisshan/claude-code-best-practice · Boris Cherny (@bcherny, Claude Code 創始人)
> 收錄日期：2026-05-16（初次：2026-05-01）
> 涵蓋：2026-01 至 2026-05 共 7+ 個 tip 集合（約 65 個技巧）
> 原始來源：
> - 2026-01-03: 13 tips (個人設定)
> - 2026-02-01: 10 tips (Claude Code 團隊最佳實踐)
> - 2026-02-12: 12 tips (客製化功能)
> - 2026-03-10: 2 tips (Code Review + Test Time Compute)
> - 2026-03-25: 2 tips (Squash Merge + PR 大小)
> - 2026-03-30: 15 tips (隱藏與未被充分利用的功能)
> - 2026-04-16: 6 tips (Opus 4.7 使用技巧)
> - 2026-05（W20 v2.1.137–143）: /goal、Agent View、Fast Mode 變更、Plugin 依賴管理

---

## 一、Session 管理

### /branch — Fork 現有 Session

從現有 session 建立分支，探索不同方案而不污染原線：

```bash
# 方法 1：在 session 內執行
/branch

# 方法 2：從 CLI 啟動
claude --resume <session-id> --fork-session
```

`/branch` 會建立分支對話，使用 `claude -r <original-session-id>` 回到原始線。

### /btw — 非阻塞側邊提問

在 agent 執行任務中途插入問題，不中斷當前任務進度。Agent 完成目前工作後才回應：

```
/btw how do I spell dachshund?
> dachshund — German for "badger dog" (dachs + badger, hund + dog).
↑/↓ to scroll · Space, Enter, or Escape to dismiss
```

Boris 每天大量使用，解決快速側邊查詢而不打斷主任務。

### /focus — 專注模式

隱藏所有中間工具呼叫與輸出，只顯示最終結果。當你已充分信任模型時適合使用：

```
/focus   ← toggle on/off
```

Boris 現在大多只看最終結果，不需要逐步監看中間過程。

### /loop — 本地定期重複執行

在本機 terminal session 中定期呼叫 slash command。Boris 的實際使用範例：

```bash
/loop 5m /babysit        # 自動處理 code review、rebase、推 PR 到 production
/loop 30m /slack-feedback  # 每 30 分鐘自動針對 Slack 回饋開 PR
/loop /post-merge-sweeper  # 補處理錯過的 code review 意見
/loop 1h /pr-pruner        # 關閉過時的 PR
```

### /batch — 大規模平行 Fan-out

`/batch` 訪談你的需求後，讓 Claude fan-out 工作給盡可能多的 worktree agent（幾十、幾百甚至上千個）：

```
/batch migrate all Python 2 modules to Python 3
```

適合大型程式碼遷移和其他可平行化的工作。每個 worktree agent 在獨立的 codebase 副本上工作。

### Rewind — 走錯路徑時的正確做法

錯誤做法：「那個沒用，試 X」（失敗嘗試仍留在 context 污染後續）

正確做法：**Rewind**（Esc + Esc）到失敗前，用新學到的資訊重新 prompt。

「Summarize from here」功能可建立 handoff message，記錄嘗試過什麼、為什麼失敗，讓重新開始的 session 不走相同錯誤路徑。

### Side Chat — 從主對話分岔出副線

快捷鍵：`⌘+;`（macOS）/ `Ctrl+;`（Windows/Linux）

Side chat 會讀入主對話 context，但不會回寫到主線，適合探索性問題而不污染主任務方向。

### --bare 旗標 — 加速 SDK 啟動最多 10x

預設 `claude -p` 會搜尋本地 CLAUDE.md、settings、MCP。非互動用途明確指定所需設定可大幅加速：

```bash
claude -p "summarize this codebase" \
    --output-format=stream-json \
    --verbose \
    --bare
```

### Recaps — 快速定位長時間 Session

長時間 session 回來時，Claude 自動顯示摘要：

```
* Cogitated for 6m 27s
* recap: Fixing the post-submit transcript shift bug. Styling-flash shipped as PR #29869.
         Next: need screen recording of remaining horizontal rewrap.
         (disable recaps in /config)
```

在 `/config` 中可關閉。

### Teleport + Remote Control — 跨設備繼續 Session

```bash
claude --teleport    # 將 cloud session 拉到本地 terminal
/teleport            # 同上

/remote-control      # 讓手機/網頁控制本地 session
```

Boris 在 `/config` 中啟用「Enable Remote Control for all sessions」。

---

## 二、多 Agent 平行化

### 同時跑 5 個 Claude（Terminal）

在 terminal 開 5 個標籤分頁，各跑一個 Claude 並編號 1–5，用系統通知知道哪個需要輸入。

### claude.ai/code 再跑 5-10 個（雲端）

在 `claude.ai/code` 同時跑 5–10 個 Claude，搭配本機 Claude 使用。手動在 Chrome 啟動 session，在本地和網頁之間來回傳遞。

### Git Worktrees — 平行工作的核心工具

Claude Code 深度支援 git worktrees，是在同一 repo 做大量平行工作的關鍵：

```bash
claude -w           # 在 worktree 中啟動新 session
```

或在 Claude Desktop 勾選「worktree」checkbox。Boris 同時跑幾十個 Claude，全靠 worktrees。

```bash
# 常見工作流程：開 3-5 個 worktree，各自運行獨立 Claude session
git worktree add ../feature-a feature-a
git worktree add ../feature-b feature-b
```

### 多個 Context Window — Test Time Compute

多個獨立 context window 的結果比單一 context window 更好。這是 subagents 有效的原因：同一個模型，讓不同 agent 找另一個 agent 的 bug，就像讓同事 review 你的程式碼一樣有效。

### Subagents — 自動化常見工作流程

在請求中加入「use subagents」來分配額外運算資源：

- `code-simplifier`：Claude 完成工作後自動簡化程式碼
- `verify-app`：端對端測試 Claude Code 輸出
- `code-review agent`：PR 開啟時 dispatch 一組 agent 進行深度審查

Subagents 放在 `.claude/agents/`。

### Code Review — Agent 團隊 PR 審查

PR 開啟時，Claude dispatch 一組 agent 進行深度 review，Boris 的 code output 每工程師提升 200%，review 曾是瓶頸，現在 Code Review 功能處理。常常抓到 Boris 自己不會發現的真實 bug。

---

## 三、權限與安全

### 不要用 --dangerously-skip-permissions

不要使用 `--dangerously-skip-permissions`。改用 `/permissions` 預先允許你知道安全的 bash 指令，避免不必要的權限提示。大多數設定 check in 到 `.claude/settings.json` 與團隊共享。

### Wildcard 權限語法

`/permissions` 支援完整 wildcard 語法：

```
Bash(bun run *)       # 允許所有 bun run 指令
Edit(/docs/**)        # 只允許編輯 docs 目錄
```

### Auto Mode — 智慧型權限路由（Opus 4.7）

Auto mode 將權限提示路由給模型分類器判斷：
- 安全 → 自動批准
- 有風險 → 暫停詢問

`Shift+Tab` 切換：`Ask permissions` → `Plan mode` → `Auto mode`

這讓你能同時跑更多 Claude，安全的操作自動通過，不需守候。

### /fewer-permission-prompts Skill

掃描 session history 找出反覆提示但安全的 bash/MCP 命令，推薦加入 allowlist。不使用 auto mode 時用這個調整權限設定。

### /sandbox — 開源沙盒運行環境

在機器上跑沙盒，支援檔案和網路隔離：

```
/sandbox   ← 啟用
```

提升安全性同時減少權限提示。

### Hooks 路由權限提示

使用 `PermissionRequest` hook 將權限請求路由到 WhatsApp 等外部工具供你批准/拒絕：

```json
"PermissionRequest": [
  { "hooks": [{ "type": "command", "command": "your-approval-script.sh" }] }
]
```

---

## 四、生產力工具

### Plan Mode — 每個複雜任務的起點

`Shift+Tab`（兩次）進入 Plan mode。如果目標是寫 PR，在 Plan mode 來回確認計畫，再切換到 auto-accept edits mode，Claude 通常能一次完成。好的計畫至關重要。

整個 Claude Code 團隊也用同樣做法：有些成員用一個 Claude 寫計畫，另一個從 staff engineer 視角審查計畫。

### Auto Mode — 無需守候的長時間任務

適合深度研究、重構、建構複雜功能、迭代到效能基準達標等長時間任務。以前需要守候或用危險的 skip-permissions，現在 auto mode 是更安全的替代。

### MCP — 讓 Claude 使用你的所有工具

Claude 可以用你的所有工具：
- 搜尋和發文到 Slack（Slack MCP server）
- 執行 BigQuery 查詢（`bq` CLI）
- 抓取 Sentry 錯誤日誌

Slack MCP 設定 check in 到 `.mcp.json` 與團隊共享。

### Output Styles — 調整 Claude 的輸出風格

```
/config  → 設定 output style
```

- **Explanatory**：熟悉新 codebase 時，Claude 解釋框架和程式碼模式
- **Learning**：Claude 引導你自己做程式碼改動
- **Custom**：建立自訂輸出風格調整 Claude 的語氣

### Voice Input — 語音編程

Boris 大部分程式碼是用說話而非打字完成的：

```
/voice  ← CLI 啟用後按住空白鍵說話
```

Desktop 按語音按鈕；iOS 啟用系統聽寫。語音輸入產生比打字更詳細的 prompt。

### Chrome Extension — 前端開發必備

讓 Claude 控制瀏覽器，就像給 Claude 一個瀏覽器讓它迭代直到結果好看：

> 「就像叫人建網站但不讓他用瀏覽器——結果通常不好看」

Boris 每次做前端工作都用 Chrome extension，比其他同類 MCP 更可靠。

### PostToolUse Hook — 自動格式化

```json
"PostToolUse": [
  {
    "matcher": "Write|Edit",
    "hooks": [
      { "type": "command", "command": "bun run format || true" }
    ]
  }
]
```

Claude 生成的程式碼通常格式良好，hook 處理最後 10%，避免 CI 後期格式錯誤。

### CLAUDE.md 持續精煉

每次 Claude 出錯後：
1. 立即加到 `CLAUDE.md`（「Claude 不要再犯這個錯誤」）
2. 結尾加：「Update your CLAUDE.md so you don't make that mistake again.」
3. 部分工程師維護任務特定筆記目錄，在 CLAUDE.md 中引用

整個 repo 共用一個 `CLAUDE.md`，check in 到 git，全團隊每週多次貢獻。

### Slash Commands — 每日工作流程自動化

為每個每天重複多次的「inner loop」工作流建立 slash command。Claude 也可以使用這些 commands。Commands check in 到 git，放在 `.claude/commands/`。

範例：`/commit-push-pr` — 一次 commit、push 並開 PR。

### Status Line — 即時工作狀態顯示

自訂 status line 顯示在 composer 下方，顯示模型、目錄、剩餘 context、費用等：

```
/statusline  ← 讓 Claude 根據你的 .bashrc/.zshrc 生成
```

每個團隊成員可以有不同的 statusline。

### --add-dir — 跨 Repo 工作

跨多個 repository 工作時，從一個 repo 啟動 Claude 後用 `--add-dir` 加入其他 repo：

```bash
claude --add-dir /path/to/other-repo
# 或在 session 內：
/add-dir /path/to/other-repo
```

也可在 `settings.json` 加入 `"additionalDirectories"` 永久設定。

### --agent 旗標 — 自訂系統 Prompt 與工具

```bash
claude --agent=<your-agent-name>
```

Custom agents 放在 `.claude/agents/`，可有限制的工具集、自訂描述和指定模型。適合建立唯讀 agent、專業 review agent 或領域特定工具。

---

## 五、Git / PR 工作流程

### Squash Merge — 保持乾淨的 Git 歷史

Boris 在 2026-03-24 一天完成 141 個 squash PR（266 個 contributions）。

Squash merge 把分支所有 commit 壓縮成目標分支的單一 commit：
- 保持線性歷史，方便 feature rollback
- 簡化 `git bisect` 操作
- 在高速 AI 驅動開發中（一天 141 PR），中間的「fix lint」等 commit 是不必要的雜訊

### PR 大小 — 保持小而聚焦

Boris 的 141 個 PR 的大小分佈（共 45,032 行）：

| 指標 | 行數（加+刪）|
|------|------------|
| p50 | 118 |
| p90 | 498 |
| p99 | 2,978 |
| min | 2 |
| max | 10,459 |

中位數 118 行，即使一天 141 個 PR 也保持專注可管理。偶爾的大 PR（重構、程式碼生成）是例外。較小的 PR 減少衝突可能性、提升 review 效率、配合 squash merge 方便回滾。

### @claude on PRs — 更新 CLAUDE.md

Code review 時在同事 PR 上 tag `@claude`，讓 Claude 自動更新 CLAUDE.md 作為 PR 的一部分。使用 Claude Code GitHub action。Boris 稱為「Compounding Engineering」。

---

## 六、模型與 Effort

### Opus 4.7 Effort 等級

`Shift+Tab` 切換 effort，或透過 `/model` 設定。五個等級：`low` · `medium` · `high` · `xhigh` · `max`

- **低 effort** — 更快的回應和更低的 token 用量
- **高 effort** — 最強的智力和能力

Boris 個人偏好：高 effort 做所有事。Opus 4.7 使用 adaptive thinking（非固定 thinking budget），模型自行決定每步思考深度。

### Test Time Compute — 丟越多 Token 結果越好

大致上，對程式碼問題投入越多 tokens，結果越好。使用獨立 context window 效果更好——這是 subagents 有效的原因，也是一個 agent 可以找到另一個 agent 製造的 bug 的原因。

### 給 Claude 驗證自己工作的方式（最重要的事）

Boris 的 prompt 現在長這樣：`Claude do blah blah /go`，其中 `/go` 是一個 skill：

1. 用 bash、browser 或 computer use 端對端測試自己
2. 執行 `/simplify`
3. 開 PR

根據任務不同，驗證方式不同：
- **後端**：跑 server/service 端對端測試
- **前端**：用 Chrome extension 讓 Claude 控制瀏覽器
- **桌面應用**：用 Computer Use

給 Claude 這個驗證回饋迴圈，最終結果品質會提升 2–3 倍。

---

## 已知重要設定

- `settings.json` 中的 `"agent"` 欄位：設定主對話的預設 agent
- `"additionalDirectories"`：永久加入額外目錄
- `"env"` 欄位：取代 wrapper scripts 設定環境變數（有 84 個環境變數可設定）
- 37 個設定選項，支援 codebase 級、子目錄級、個人、企業政策四個層級

---

## 七、W20 新功能補充（v2.1.137–v2.1.143，May 9–15, 2026）

> 完整 Changelog 詳見 `27-whats-new-w18-w19.md`（W20 版本待另建 best-practices 文件）

### /goal — 持續執行到完成

新指令 `/goal` 讓你設定完成條件，Claude 工作到達標為止：

```
/goal 所有 type error 都修復，CI 通過
```

執行期間顯示即時 overlay，達到條件後自動停止。比寫長 prompt 更能確保驗收條件被遵守。
- **適用**：已知成功標準的自動化任務（測試通過、無 lint 錯誤）
- **禁止**：開放式任務（/goal 需要可判斷的完成條件）

### Agent View — 統一管理多個 Session

```bash
claude agents     # 進入 Agent View dashboard
← （左箭頭）     # 從任意 session 進入 Agent View
```

顯示所有活躍/歷史 session 的狀態、待輸入需求、最後回應。
- 內嵌互動：可直接在 Agent View 回應 pending 決策，不需進入個別 session
- 背景操作：`/bg` 將當前 session 移到背景；`claude --bg [task]` 直接後台啟動
- `claude agents --cwd <path>`：只顯示特定目錄的 sessions（v2.1.141+）

### Fast Mode 變更：Opus 4.7 預設（v2.1.142）

Fast Mode（`Shift+Tab` 切換）現在預設使用 **Opus 4.7**（原為 Opus 4.6）。

若需回到 4.6：設定 `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`

### worktree.bgIsolation 設定（v2.1.143）

```json
// settings.json
"worktree": {
  "bgIsolation": "none"  // 背景 session 直接編輯 working copy（不建新 worktree）
}
```

預設行為：背景 session 自動建立新 worktree（隔離）。改為 `"none"` 讓背景 session 直接在原工作目錄操作。

### Plugin 依賴管理（v2.1.143）

`claude plugin disable` 現在會拒絕停用被其他已啟用 plugin 依賴的 plugin。先停用依賴者，再停用被依賴的 plugin。

`/plugin` marketplace pane 新增每個 plugin 的預計 context cost 顯示。

### Rewind 新選項：Summarize up to here（v2.1.141）

Rewind menu 新增「Summarize up to here」，在當前點壓縮之前的 context，比 `/compact` 更細緻的控制（選擇壓縮到哪個時間點）。

### Hooks 新功能（v2.1.141）

`terminalSequence` 欄位：允許 hook 在不控制 terminal 的情況下發送桌面通知：

```json
"PostToolUse": [{
  "hooks": [{
    "type": "command",
    "command": "your-script.sh",
    "terminalSequence": "\033]9;通知訊息\007"
  }]
}]
```

`continueOnBlock`（PostToolUse）：Block 後將拒絕原因回傳給 Claude，讓 Claude 自行決策下一步（而非直接終止）。
