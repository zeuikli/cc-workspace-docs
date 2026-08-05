# Claude Code W26–W27 新功能（v2.1.185–v2.1.201）

> **Source:** https://code.claude.com/docs/en/changelog
> **Date Range:** 2026-06-20 ~ 2026-07-03
> **Versions:** v2.1.185 / v2.1.186 / v2.1.187 / v2.1.190 / v2.1.191 / v2.1.193 / v2.1.195 / v2.1.196 / v2.1.197 / v2.1.198 / v2.1.199 / v2.1.200 / v2.1.201

> Claude Sonnet 5 本身另立 `41-claude-sonnet-5.md` 專篇；本檔僅記錄該版本（v2.1.197）在 Claude Code 內的整合細節。

---

## v2.1.185（2026-06-20，trivial）

串流中斷提示文字與觸發時機調整：「Waiting for API response · will retry in …」（原「No response from API · Retrying in …」），觸發門檻從 10 秒延長為 **20 秒**無回應。

---

## v2.1.186（2026-06-22，feature-dense）

### CLI MCP 登入/登出

```bash
claude mcp login <name>
claude mcp logout <name>
```

不需開 `/mcp` 選單即可完成 MCP 認證；`--no-browser` 支援 SSH 場景的 stdin redirect 流程。

### 其他新增
- `/workflows` agent detail view 支援狀態篩選（按 `f`）
- `/plugin` Installed tab 新增「Skills」區塊
- `teammateMode: "iterm2"` 設定（缺少 `it2` CLI 會警告）

### 行為變更（需注意）

**`!` bash 指令現在會觸發 Claude 自動回應輸出**（原本只是把輸出放進 context，不主動回應）。要恢復舊行為：

```json
// settings.json
{
  "respondToBashCommands": false
}
```

### `CLAUDE_CODE_MAX_RETRIES` 上限變更

本版將 `CLAUDE_CODE_MAX_RETRIES` 上限訂為 **15**（無人值守 session 改用 `CLAUDE_CODE_RETRY_WATCHDOG`）。**此上限已在 v2.1.199 針對非容量類 transient error 再次放寬**，見下方。

### 安全性修復

- `Agent(type)` deny 規則 / `Agent(x,y)` allowed-types 未被強制執行的 bug（**安全相關**）

### 其他修復
- 睡眠恢復後串流「Content block not found」/ JSON parse 錯誤
- Subagent transcript 捲動殘影、背景任務預覽顯示原始工具名稱
- Chrome tab-group 隔離、背景 recap 訊息重複
- 主 turn 結束後背景 agent 仍在跑時 Esc/Ctrl+C 失去回應
- Permission prompt 選項編號錯位、`~~刪除線~~` 字面 tilde 未渲染
- `--tools` flag-gate race condition（冷啟動）
- Agent teams `--effort` 繼承問題（tmux/pane teammates）
- Workflow `agent({schema})` 無限迴圈（現在 5 次嘗試後中止）

### 改善
- `claude mcp get`/`remove` 拼字建議、MEMORY.md compaction 提醒
- Skill frontmatter key 大小寫容錯（`display-name`/`default-enabled`/`fallback`/`metadata.*` 接受 kebab/snake/camelCase）
- `SKILL.md` YAML 格式錯誤時改為載入 body（空 metadata），不再靜默失敗

---

## v2.1.187（2026-06-23，feature-dense + security）

### `sandbox.credentials` 設定

新增設定，封鎖 sandboxed 指令讀取憑證檔案 / secret 環境變數。

### 其他新增
- Org 層級 model 限制反映在 model picker、`--model`、`/model`、`ANTHROPIC_MODEL`（顯示「restricted by your organization's settings」）
- Fullscreen 下 select menu（permission prompt / `/model` / `/config`）支援滑鼠點擊

### 修復
- `--resume` 在 `-p` 執行未產生 model turn 時報「No conversation found」
- `--json-schema` / workflow `agent({schema})` 無限重呼叫 bug
- Remote MCP tool call 無限期 hang——現在 **5 分鐘後自動 abort**，可用 `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` 覆寫
- Remote session 啟動延遲 +2.7s 迴歸
- 貼上韓文/CJK 亂碼
- `/update` 於 Remote Control 下卡住
- 背景任務永久卡在「working」狀態
- Subagent 深度追蹤（resume/fork 場景）、殘留 agent worktree 註冊

### 改善
- `/install-github-app`：GitHub App 安裝改為選用，可跳過 workflow/secret 步驟
- `/btw` 方向鍵導覽、`/plugin` 顯示未使用的 plugin

---

## v2.1.190 / v2.1.191（2026-06-24）

### `/rewind` 支援跨越 `/clear` 恢復

**`/rewind` 現在可以恢復到 `/clear` 執行之前的對話**——先前 `/clear` 是不可逆的邊界，此版打通後可救回誤 `/clear` 的 session。

### 效能

- **串流時 CPU 使用量降低約 37%**（100ms 文字更新合併批次處理）
- 長 session 記憶體成長速度降低（終端輸出快取優化）

### 修復
- 串流時捲動跳動
- 背景 agent 在 stop 後「復活」的 bug（現已**永久修復**）
- `/voice` 組織政策提示訊息
- Windows Terminal 下 `/login` URL 截斷
- Ghostty ssh/tmux 下 Cmd+click
- `claude agents` 誤把內建 slash command 當成 prompt 文字送出
- 圖片路徑洩漏（改用 `[Image #N]` placeholder）
- 逗號分隔的 hook matcher（如 `"Bash,PowerShell"`）完全不觸發的 bug
- `/permissions` Recently-denied 核可狀態未持久化
- Managed settings `forceRemoteSettingsRefresh`（MDM/檔案政策）+ `Cache-Control: no-cache`

### 改善
- Sandbox 網路權限對話記住當次 session 已核可的 host
- MCP capability discovery（`tools/list`/`prompts/list`/`resources/list`）針對 transient error 重試
- MCP OAuth 重試 + headless 貼 URL 流程

---

## v2.1.193（2026-06-25，feature-dense）

### `autoMode.classifyAllShell`

新設定：讓 auto mode 分類器處理**所有** Bash/PowerShell 指令，不再只針對「任意程式碼執行」樣式的指令做分類。

### OpenTelemetry 新事件：`claude_code.assistant_response`

新增記錄模型回應文字的 OTel log event。

⚠️ **需注意的行為變更**：
- 預設 **redacted**，需 `OTEL_LOG_ASSISTANT_RESPONSES=1` 才會記錄
- 若未設定，**跟隨 `OTEL_LOG_USER_PROMPTS` 的值**——已在記錄 user prompts 的部署，升級後會**開始一併記錄 assistant response 內容**
- 想維持「只記 prompt、不記 response」需明確設 `OTEL_LOG_ASSISTANT_RESPONSES=0`

### 其他新增
- Bash mode（`!`）即時檔案路徑自動完成
- MCP server 需要認證時的啟動提示，導向 `/mcp`
- 閒置背景 shell 指令的自動記憶體壓力回收，停用旗標 `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`

### 修復
- 登入後 `/model` UI 顯示過期資訊
- Backgrounding 誤報「N background tasks would be abandoned」而取消
- 自動更新後 pinned agent 重新詢問
- 幽靈「general-purpose (resumed)」subagent、agent panel 隱藏 sibling 的問題

---

## v2.1.195（2026-06-26，minor）

- 新增 **`CLAUDE_CODE_DISABLE_MOUSE_CLICKS`** 環境變數——停用 fullscreen 模式下滑鼠點擊/拖曳/hover，但保留滾輪
- 修復 hook matcher 對含連字號 identifier（如 `code-reviewer`、`mcp__brave-search`）誤判為子字串匹配的 bug——現改**精確匹配**；要匹配某 hyphenated MCP server 底下所有工具需寫 `mcp__brave-search__.*`
- 修復語音聽寫問題（macOS 靜音錄音、無空格語言如日文/中文/泰文自動送出失敗）
- 修復僅由專案 `.claude/settings.json` 啟用的外部 plugin 未要求安裝同意的問題
- 修復 `/plugin` 在 `plugin.json` name 與 marketplace entry name 不同時的 Enable/Disable 行為

---

## v2.1.196（2026-06-29，feature + security）

### Org 層級預設模型

管理員可在 org console 設定組織預設模型；使用者未自選時 `/model` 顯示「Org default」（或「Role default」）。

### 安全修復

`claude mcp list`/`get` **不再自動 spawn** 由 untrusted workspace 中已提交的 `.claude/settings.json` 自我核准的 `.mcp.json` server——改顯示 `⏸ Pending approval`。

### 其他新增
- 啟動時顯示可讀的預設 session 名稱
- 聊天中的檔案附件可點擊（Cmd/Ctrl-click 在 Finder/Explorer 中顯示）

### 串流閒置監控預設開啟

**Streaming idle watchdog 現在對所有 provider 預設開啟**：串流 **5 分鐘**無任何事件即 abort/retry；停用旗標 `CLAUDE_ENABLE_STREAM_WATCHDOG=0`。

### 其他修復
- 喚醒背景任務時誤刪對話並重跑原始 prompt（transcript probe 誤判）
- Rate-limit 警告閃爍/重複計數、重複 recap 行（StructuredOutput schema 被拒）
- PowerShell 下 `git diff`/`git grep`/`egrep`/`fgrep` 誤報 exit-1 失敗
- `claude agents` panel（focus 卡住、subagent type 遺失、狀態顯示錯誤）
- `claude agents --dangerously-skip-permissions` fallback bug
- MCP OAuth `scopes_supported` 導致 GitLab self-hosted `invalid_scope` 錯誤
- Bedrock 下 `/context` 顯示 0 tokens
- `/deep-research` 誤報 verifier 失敗
- Plugin 依賴版本鎖定、語音聽寫吞掉空格

### 改善
- 背景 session 可靠性（撐過 stop/restart/update，含 Windows shell handoff）
- 背景 agent 在 daemon 重啟後自動恢復
- **`/code-review` workflow 將五個清理型 finder 合併為一個，token 減少約 25%**
- Remote Control 在 `ANTHROPIC_BASE_URL` 指向非 Anthropic host 時自動停用（比照既有 `CLAUDE_CODE_USE_BEDROCK`/`_VERTEX`/`_FOUNDRY` 行為）
- 從前景 session 開啟 agents view 現在只需按一次 `←`（原本要兩次）

---

## v2.1.197（2026-06-30，MAJOR — 新模型）

> **Claude Sonnet 5 發布**，成為 Claude Code 預設模型，原生 **1M-token context window**，促銷定價 **$2/$10 per Mtok**（至 2026-08-31）。詳見專篇 `41-claude-sonnet-5.md`。

---

## v2.1.198（2026-07-01，MAJOR — 多項重大功能）

### Subagent 預設背景執行

Subagent（含 sub-sub-agent）**現在預設在背景執行**（先前為漸進式 rollout，本版全面預設開啟）。

### Claude in Chrome 正式 GA

瀏覽器操作能力（Computer Use 的瀏覽器變體）正式脫離 beta。

### 背景 agent 通知

`claude agents` 新增背景 agent 通知，觸發 `Notification` hook，事件類型 `agent_needs_input` / `agent_completed`。

### `/dataviz` skill

新增官方 skill，提供圖表/dashboard 設計指引 + 可執行的色票驗證工具。

### Gateway：新增 AWS 上游 provider

新增 **Claude Platform on AWS**（`anthropicAws`）作為 gateway 上游 provider；model-not-found 回應現在會推進 failover chain。

### 背景 agent 自動 commit + push + 開 draft PR

`claude agents` 產生的背景 agent 完成 worktree 內的程式碼工作後，**自動 commit、push、開 draft PR**，不再停下來詢問。

### Explore agent 繼承主 session 模型

內建 Explore agent 現在繼承主 session 的模型（上限 opus），不再固定跑 haiku。

### Subagent / context compaction 繼承 extended thinking 設定

### 移除 `/agents` wizard

改為直接請 Claude 建立/管理 subagent，或直接編輯 `.claude/agents/`。

### 修復
- 短暫網路中斷（ECONNRESET）串流中途自動重試
- 重複 sandboxed 網路 host access 觸發過多背景分類器請求
- Web/desktop/VS Code 任務面板背景任務卡「Running」
- Agent teams：teammate 因 API error 死亡時正確回報「failed」；發訊息可喚醒卡住的 teammate
- `/diff` panel 分支切換未刷新
- Fullscreen 下 Markdown 表格溢出
- Claude Platform on AWS/Mantle session 因 STS 過期而 dead-end——`awsAuthRefresh` 現在自動執行
- macOS Local Network entitlements 修復「no route to host」
- `/desktop` 離開 worktree 後「Cannot determine working directory」
- 背景 agent macOS 上每約 52 秒「Reconnecting…」閃爍
- `claude attach <id>` 中按 `←` 誤退出到 shell
- `claude --bg` + `--print`/`-p` 衝突現在提前拒絕
- Workflow progress view 遺失最早的 agent
- `.claude/rules/` 條件式規則透過 symlink 路徑不載入
- `/branch` 預設 fork 名稱改從第一則真實 prompt 取得（原本用 compaction summary）

### 其他
- Focus mode：一個 turn 內的 subagent 出現在活動摘要中，通知折疊為單一計數
- Syntax highlighting 升級至 highlight.js 11
- **安全相關**：subagent 將 launcher 訊息視為任務指示，**永不**視為 user approval

---

## v2.1.199（2026-07-02，feature + reliability）

### Skill 疊加呼叫支援多個前綴 skill

`/skill-a /skill-b do XYZ` 現在載入**所有前綴 skill（最多 5 個）**，不再只載入第一個。

### 其他新增
- SSL 憑證錯誤（TLS-inspecting proxy、缺 `NODE_EXTRA_CA_CERTS`、過期憑證）現在立即失敗並給修復提示，不再浪費重試次數

### 可靠性修復
- 串流過程中 mid-stream overloaded/server error 現在保留部分輸出 + 顯示未完成提示
- Subagent 因 rate-limit/server error 中斷時**回傳部分工作給 parent**，不再靜默失敗
- Subagent 把 API 錯誤（如額度用盡）誤報為「成功」的 bug——現在正確回報為錯誤
- Linux 背景 agent daemon 在非乾淨關閉後每約 50 秒自我終止迴圈
- macOS SSH 冷啟動失敗（"Could not switch to audit session" — v2.1.196 的迴歸）
- `claude stop` 被競速的背景 agent respawn 靜默復原
- 背景任務進度指示器在長指令執行中卡住
- 低記憶體機器顯示通用錯誤而非記憶體提示
- Remote session 在 agent view 中 Working/Idle 狀態閃爍
- 閒置 subagent 從 agent panel 消失（現折疊為可展開摘要列）
- 查看 subagent 時按 `/model`/`/fast` 誤開 lead 的 picker
- `SessionStart`/`Setup`/`SubagentStart` hook 在 exit code 2 時隱藏 stderr
- `SendMessage` 在 agent 名稱重複使用時誤路由

### `CLAUDE_CODE_RETRY_WATCHDOG` 重試上限放寬

**非容量類 transient error 的預設重試次數提高到 300**，並解除 `CLAUDE_CODE_MAX_RETRIES` 原本的 **15 上限**（v2.1.186 訂下的上限）。

### 其他改善
- 訂閱用戶的 transient 429 rate-limit 現在自動重試 + backoff
- `claude agents` 中 PR 連結顯示為簡潔的 `#N`

---

## v2.1.200（2026-07-03，行為變更 + 大量修復）

### 預設 permission mode 改為 "Manual"

CLI、`--help`、VS Code、JetBrains 的**預設 permission mode 從先前預設改為 "Manual"**；`--permission-mode manual` 與 `"defaultMode": "manual"` 與既有 `default` 同時接受。

**影響**：升級後首次啟動若未明確設定 permission mode，行為會更保守（更多工具呼叫需人工核可）——習慣舊預設值的自動化腳本/CI 需明確指定 permission mode。

### `AskUserQuestion` 不再自動繼續

`AskUserQuestion` 對話框現在**預設不再自動繼續**；需透過 `/config` 選擇加入 idle timeout。

### 大量可靠性修復（背景 agent / daemon）
- `.claude.json` 中 `disabledMcpServers`/`enabledMcpServers` 非陣列時啟動崩潰
- 背景 session 在睡眠/喚醒後或重開 stalled session 時靜默中途停止
- 背景 session 在 Esc 取消的 stall respawn 後重跑該 turn
- 背景 agent crash 後從未重啟 + stale `daemon.lock` PID 重用問題
- 背景 agent daemon handover 強化（透過內嵌 build timestamp 判斷新舊）
- 背景 agent roster 損毀問題（孤兒清理、欄位保留、socket auth token 剝離）

### 其他修復
- Subagent 在任何文字輸出前被 rate limit 截斷，現在乾淨失敗而非回傳空結果
- 背景 agent 輸出的控制位元組洩漏到終端
- `claude agents --plugin-dir <dir>` flag 順序 bug
- 專案範圍 plugin 無法從 git worktree 載入
- `/mcp` server 列表畫面朗讀器 focus 追蹤
- 語音聽寫在無聲錄音時誤報「Voice connection failed」
- tmux 3.4+ 下渲染閃爍（透過同步終端輸出修復）
- 朗讀器輸出改善（隱藏裝飾性字符、transcript 標籤、表格朗讀）
- 安裝腳本現在會解釋安裝過程中的 OOM-kill

---

## v2.1.201（2026-07-03，minor/internal）

Claude Sonnet 5 session 不再使用對話中段的 system role 承載 harness 提醒。

---

## 功能對照索引

| 功能 | 版本 | 日期 |
|------|------|------|
| 串流中斷提示延長至 20s | v2.1.185 | 2026-06-20 |
| `claude mcp login`/`logout` CLI 認證 | v2.1.186 | 2026-06-22 |
| `!` bash 自動回應行為變更（`respondToBashCommands`）| v2.1.186 | 2026-06-22 |
| `CLAUDE_CODE_MAX_RETRIES` 上限訂為 15 | v2.1.186 | 2026-06-22 |
| `sandbox.credentials` 設定 | v2.1.187 | 2026-06-23 |
| Org 層級 model 限制反映於 model picker | v2.1.187 | 2026-06-23 |
| MCP tool call 5 分鐘逾時（`CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT`）| v2.1.187 | 2026-06-23 |
| `/rewind` 支援跨越 `/clear` 恢復 | v2.1.191 | 2026-06-24 |
| 串流 CPU 使用量降低 ~37% | v2.1.191 | 2026-06-24 |
| `autoMode.classifyAllShell` | v2.1.193 | 2026-06-25 |
| `claude_code.assistant_response` OTel 事件 | v2.1.193 | 2026-06-25 |
| `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP` | v2.1.193 | 2026-06-25 |
| `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` | v2.1.195 | 2026-06-26 |
| Hook matcher 連字號精確匹配修復 | v2.1.195 | 2026-06-26 |
| Org 層級預設模型 | v2.1.196 | 2026-06-29 |
| `.mcp.json` 自我核准安全修復 | v2.1.196 | 2026-06-29 |
| Streaming idle watchdog 預設開啟（5 分鐘）| v2.1.196 | 2026-06-29 |
| `/code-review` finder 合併，token -25% | v2.1.196 | 2026-06-29 |
| **Claude Sonnet 5 發布**（1M context，$2/$10 促銷）| v2.1.197 | 2026-06-30 |
| Subagent 預設背景執行 | v2.1.198 | 2026-07-01 |
| Claude in Chrome GA | v2.1.198 | 2026-07-01 |
| `/dataviz` skill | v2.1.198 | 2026-07-01 |
| Claude Platform on AWS gateway provider | v2.1.198 | 2026-07-01 |
| 背景 agent 自動 commit+push+draft PR | v2.1.198 | 2026-07-01 |
| 移除 `/agents` wizard | v2.1.198 | 2026-07-01 |
| Skill 疊加呼叫支援最多 5 個前綴 skill | v2.1.199 | 2026-07-02 |
| Subagent 部分結果回傳（rate-limit 中斷）| v2.1.199 | 2026-07-02 |
| `CLAUDE_CODE_RETRY_WATCHDOG` 上限放寬至 300（解除 15 上限）| v2.1.199 | 2026-07-02 |
| 預設 permission mode 改為 "Manual" | v2.1.200 | 2026-07-03 |
| `AskUserQuestion` 不再自動繼續 | v2.1.200 | 2026-07-03 |
| Sonnet 5 移除 mid-conversation system role 提醒 | v2.1.201 | 2026-07-03 |

---

## 需要立即檢視的變更（升級後行動項）

1. **Permission mode 預設改為 Manual**（v2.1.200）——CI/自動化腳本若依賴舊預設值，需明確指定 `--permission-mode` 或 `"defaultMode"`。
2. **`!` bash 自動回應**（v2.1.186）——若 workflow 依賴「純輸出、不觸發回應」的舊行為，需設 `"respondToBashCommands": false`。
3. **`OTEL_LOG_ASSISTANT_RESPONSES` 跟隨 `OTEL_LOG_USER_PROMPTS`**（v2.1.193）——已在記錄 prompt 的 OTel 部署，升級後會**開始一併記錄 response 內容**，涉合規/隱私需明確設 `=0` 關閉。
4. **Subagent 預設背景執行 + 自動 commit/push/開 draft PR**（v2.1.198）——委派拓樸與 sub-agent 產出「回主 context 前先審查」的既有假設需重新核對（本 workspace `subagent-strategy.md` 的「產出者不驗收自己的產出」原則仍適用，但背景 agent 現在會**先開 PR 才被看到**，稽核時機需提前到 PR review）。
5. **`Agent(type)` deny 規則此前未強制執行**（v2.1.186 修復前）——已設定該類 deny rule 的環境應確認修復生效（升級到 v2.1.186+）。

---

## 延伸閱讀

- [41-claude-sonnet-5.md](./41-claude-sonnet-5.md) — Claude Sonnet 5 模型專篇
- [12-permissions.md](./12-permissions.md) — Permission 系統架構（v2.1.200 預設值變更的背景知識）
- [40-w25-features.md](./40-w25-features.md) — 前一批（W25）功能
- [32-dynamic-workflows.md](./32-dynamic-workflows.md) — Dynamic Workflows（`agent({schema})` 相關修復見本檔）
