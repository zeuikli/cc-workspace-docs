# best-practices/INDEX.md

> Type: wiki:synthesis
> Harness-Layer: L4-knowledge
> **Type:** wiki:compiled — 46 docs covering hooks, agents, skills, permissions, MCP, sandbox, dynamic workflows, Opus 5, Fable 5, Sonnet 5, Managed Agents, Artifacts, W25–W31 features  
> **Updated**: 2026-08-04（新增 44–49：Opus 5、模型選型、Claude 5 context engineering、verification loops、W28–W31、MCP 2026-07-28）  
> **Query pattern**: BRAIN.md → 本表（序號 / 主題）→ `<NN>-<topic>.md`

本目錄收錄從官方文件與社群來源抓取的 Claude/Claude Code 最佳實踐，涵蓋 Agent、Skill、Rules、Hooks 四個面向。

---

## 檔案清單

| 檔案 | 主題 | 重點內容 |
|------|------|---------|
| [01-official-hooks-memory-settings.md](./01-official-hooks-memory-settings.md) | 官方 Hooks / Memory / Settings | Hook 三層架構、4 種 Handler 類型、Exit Code 規約、CLAUDE.md 載入順序、Settings 層級 |
| [02-community-claudemd-agent-skill.md](./02-community-claudemd-agent-skill.md) | 社群 CLAUDE.md / Agent / Skill | CLAUDE.md 設計原則、Command→Agent→Skill 架構、Skill 設計模式、Context 管理 |
| [03-hooks-patterns.md](./03-hooks-patterns.md) | Hooks 實戰設計模式 | 25 種 Hook 事件、13 個完整 shell script 範例、完整 settings.json 範本、最佳實踐 checklist |
| [04-subagent-mcp-skill.md](./04-subagent-mcp-skill.md) | Sub-Agent / MCP / Skill 進階 | 委派策略、Model 分層（Haiku/Sonnet/Opus）、Advisor 模式、MCP 整合、Tasks 原語 |
| [05-claude-prompting-best-practices.md](./05-claude-prompting-best-practices.md) | 官方 Prompt Engineering 完整指南 | Opus 4.7 行為調整、Effort 等級、XML 標籤結構、平行工具呼叫、Agentic 系統、遷移指引（2026-05-01）|
| [06-agent-skills-best-practices.md](./06-agent-skills-best-practices.md) | 官方 Agent Skills 撰寫最佳實踐 | 簡潔原則、自由度校準、Progressive Disclosure、Checklist Pattern、Plan-Validate-Execute、Claude A/B 迭代法（2026-05-01）|
| [07-advisor-tool-best-practices.md](./07-advisor-tool-best-practices.md) | 官方 Advisor Tool 完整技術指南 | Executor+Advisor 架構、模型相容性、Timing 指引、官方 System Prompt 範本、Advisor 端 Prompt Caching、成本控制（2026-05-01）|
| [08-prompt-caching.md](./08-prompt-caching.md) | 官方 Prompt Caching 完整技術指南 | 自動/明確兩種實作、最小 token 閾值、失效條件、Pre-warming、跨場景策略、Cache hit = 0.1× 費率（2026-05-01）|
| [09-secure-deployment.md](./09-secure-deployment.md) | AI Agent 安全部署完整指南 | 威脅模型、Sandbox/Docker/gVisor/VM 隔離比較、Proxy Pattern 憑證管理、Filesystem 設定、敏感檔案清單（2026-05-01）|
| [10-agent-skills-enterprise.md](./10-agent-skills-enterprise.md) | Agent Skills 企業治理指南 | 風險層級評估表、8 步安全 Checklist、評估維度、生命週期管理、Recall 限制（最多 8 Skills/request）、版本策略（2026-05-01）|
| [11-routines.md](./11-routines.md) | Routines 排程自動化完整指南 | Scheduled / API trigger / GitHub Webhook 三種觸發模式、Routine 建立流程、使用限額（Pro 5/日、Max 15/日、Team 25/日）（2026-05-01）|
| [12-permissions.md](./12-permissions.md) | 細粒度 Permission 設定完整指南 | Permission 系統架構、wildcard 語法、allow/block/prompt 三種模式、工具特定規則、Managed Settings 組織 policy（2026-05-01）|
| [13-sandbox.md](./13-sandbox.md) | Sandboxing OS 層隔離技術詳解 | Sandbox 原理、Filesystem/Network 隔離、OS 層技術、設定選項、安全限制、最佳實踐（補充 09-secure-deployment.md）（2026-05-01）|
| [14-mcp.md](./14-mcp.md) | MCP 整合完整指南 | HTTP/SSE/stdio 三種 transport 安裝、Scope 優先序、OAuth 完整設定（DCR / pre-configured / headersHelper）、Tool Search 設定、Managed MCP 組織管控兩種模式（2026-05-01）|
| [15-boris-cherny-tips.md](./15-boris-cherny-tips.md) | Boris Cherny Claude Code Tips 主題整合 | 7 個 tip 集合（2026-01 至 2026-04，約 60 個技巧）：Session 管理、多 Agent 平行化、權限安全、生產力工具、Git/PR 工作流、模型 Effort（2026-05-01）|
| [16-thariq-tips.md](./16-thariq-tips.md) | Thariq Claude Code Tips — Skill 設計與 Session 管理 | T1-T9 Skill 設計原則、9 種 Skill 類型、Skill 治理、Session 管理深度指南、工程哲學（Unhobbling / Delete-and-Rebuild）（2026-05-01）|
| [17-best-practices-overview.md](./17-best-practices-overview.md) | Claude Code 最佳實踐官方總綱 | 驗證工作流、探索→規劃→實作四階段、Context 管理、平行化與自動化、常見失敗模式（2026-05-01）|
| [18-how-claude-code-works.md](./18-how-claude-code-works.md) | How Claude Code Works — Agentic Loop / Tools / Context | Agentic Loop 三階段、五類 Built-in Tools、Session 管理、Checkpoint、Permission Modes（2026-05-01）|
| [19-features-overview.md](./19-features-overview.md) | Extend Claude Code 功能總覽與選擇指南 | CLAUDE.md vs Skills vs MCP vs Subagents vs Agent Teams vs Hooks vs Plugins 完整比較表（2026-05-01）|
| [20-common-workflows.md](./20-common-workflows.md) | Common Workflows 逐步實戰指南 | Codebase 探索、Bug Fix、Refactoring、Tests、PR、Plan Mode、Session 管理、Git Worktrees、平行化（2026-05-01）|
| [21-memory-claudemd.md](./21-memory-claudemd.md) | CLAUDE.md 與 Auto Memory 完整指南 | CLAUDE.md 多層級設定、路徑範圍規則（path-scoped rules）、Auto Memory 機制、除錯方式（2026-05-01）|
| [22-code-review.md](./22-code-review.md) | Code Review 多代理 PR 自動審查完整指南 | multi-agent 審查流程、severity 等級、`@claude review` 指令、`REVIEW.md` 設計、定價 $15-25/review（2026-05-01）|
| [24-plugins.md](./24-plugins.md) | Claude Code Plugin 系統完整指南 | Plugin vs Standalone 決策表、plugin.json manifest schema、全組件類型（skills/agents/hooks/MCP/LSP/monitors）、Marketplace 提交、Standalone 遷移、.zip/URL 載入（W19）、plugin details（W20）（2026-05-28）|
| [25-bcherny-config-github.md](./25-bcherny-config-github.md) | Boris Cherny 實際 GitHub 設定完整解析 | CLAUDE.md 自更新哲學、7 slash commands（/grill、/techdebt、/worktree 等）、6 specialized agents（code-simplifier、staff-reviewer、oncall-guide 等）、settings.json PostToolUse 格式化 hook、/loop 4 個真實配方（2026-05-01）|
| [28-thariq-prompt-caching-lessons.md](./28-thariq-prompt-caching-lessons.md) | Prompt Caching 核心教訓（Thariq Shihipar）| 分層快取結構（靜態→動態）、用 messages 代替 system prompt 更新、mid-session 禁止切換模型、工具 stub + defer_loading、Compact 保留前綴、Cache Hit Rate 監控（2026-05-16）|
| [29-onboarding-large-codebase.md](./29-onboarding-large-codebase.md) | Claude Code Onboarding 與大型 Codebase 最佳實踐 | 三層 Context 架構（context repo + Skills + MCP）、Agentic Search vs RAG、五元件 Harness（CLAUDE.md/Hooks/Skills/Plugins/MCP）、每 3-6 個月審閱設定、組織 DRI 所有權、/team-onboarding（2026-05-28）|
| [30-new-tools-commands.md](./30-new-tools-commands.md) | 新工具與 Slash Commands（2026 W13–W20）| Computer Use（Desktop/CLI）、Terminal UI（Flicker-free/Custom themes/Vim mode）、Session Recap、PR URL resume、/insights、/powerup、/terminal-setup、/feedback 跨 session（2026-05-28）|
| [31-html-output-strategy.md](./31-html-output-strategy.md) | HTML 作為主要輸出格式（HTML-First Strategy）| 五大場景（規格/Code Review/設計/報告/客製編輯器）、Markdown vs HTML 比較、快速開始範例 Prompt（2026-05-20）|
| [32-dynamic-workflows.md](./32-dynamic-workflows.md) | Dynamic Workflows 完整指南 | 六大 Workflow 模式（Fan-out/Adversarial/Tournament 等）、技術能力（模型選擇/隔離/續接）、Bun Zig→Rust 案例、方案可用性（W22，2026-05-28/06-02）|
| [33-skills-nine-categories.md](./33-skills-nine-categories.md) | Skills 九大類別與 Analytics Agent 設計指南 | Anthropic 內部九類 Skill、design 核心原則、Analytics Stack 四層架構、skills 準確率 21%→95%（2026-06-03）|
| [34-w21-w22-features.md](./34-w21-w22-features.md) | Claude Code W21–W22 新功能（v2.1.143–v2.1.157）| Auto mode on Pro、/code-review 指令、claude agents --json、Opus 4.8 新預設、Dynamic Workflows、Security Guidance Plugin、Fast Mode 定價（2026-05-18–29）|
| [35-ai-native-engineering.md](./35-ai-native-engineering.md) | AI 原生工程組織管理指南 | JIT Planning、Code Review 重新定義、三大指標（Onboarding/PR cycle time/Claude-assisted commits）、消滅過時流程（2026-06-03）|
| [36-claude-fable-5.md](./36-claude-fable-5.md) | Claude Fable 5 與 Mythos 5 完整指南 | Model ID / 規格 / 定價、訂閱方案免費期（6/9–6/22）、安全分類器路由、Prompt 差異（稽核/Subagent/記憶）、與 Opus 4.8 選型對照（2026-06-09）|
| [37-managed-agents-schedule-vaults.md](./37-managed-agents-schedule-vaults.md) | Managed Agents 排程部署與 Vault 金鑰管理 | Scheduled Deployments（cron 觸發）、Vaults with Env Vars（網路邊界替換 API Key）、post-session lifecycle hook（2026-06-09）|
| [38-steering-claude-code.md](./38-steering-claude-code.md) | 自訂 Claude Code 行為的七種機制 | CLAUDE.md / Rules / Skills / Subagents / Hooks / Output Styles / System Prompt Appending 選擇框架（2026-06-18）|
| [39-artifacts.md](./39-artifacts.md) | Claude Code Artifacts — 工作 Session 轉互動網頁 | 自動更新頁面、版本歷史、存取控制、PR walkthrough / 事故調查 / 安全稽核使用場景（2026-06-18，Team/Enterprise Beta）|
| [40-w25-features.md](./40-w25-features.md) | Claude Code W25 新功能（v2.1.178–v2.1.183）| Agent Teams 簡化（Implicit Teams）、`Tool(param:value)` permission 語法、Nested Skills 目錄、Auto mode 破壞性指令攔截、`/config key=value`、Subagent 5 層深度上限、`attribution.sessionUrl`（2026-06-15–19）|
| [41-claude-sonnet-5.md](./41-claude-sonnet-5.md) | Claude Sonnet 5 完整指南 | 新預設模型、1M context window、促銷定價 $2/$10（至 2026-08-31）、Agentic 能力躍進、與 Opus 4.8/Fable 5 選型對照（2026-06-30）|
| [42-w26-27-features.md](./42-w26-27-features.md) | Claude Code W26–W27 新功能（v2.1.185–v2.1.201）| 預設 permission mode 改為 Manual、Subagent 預設背景執行 + 自動 commit/push/開 draft PR、Claude in Chrome GA、Org 層級預設模型、`sandbox.credentials`、Streaming idle watchdog、`CLAUDE_CODE_MAX_RETRIES` 上限反覆調整（2026-06-20–07-03）|
| [43-claude-in-chrome.md](./43-claude-in-chrome.md) | Claude in Chrome — 瀏覽器操作正式 GA | Ask-before-acting 權限模型、16 項擴充功能權限、Team/Enterprise allowlist/blocklist、Prompt Injection 安全注意事項、與 Computer Use（Desktop/CLI）比較（2026-07-01 GA）|
| [44-claude-opus-5.md](./44-claude-opus-5.md) | Claude Opus 5 完整指南 | `claude-opus-5`、1M context、$5/$25（與 Opus 4.8 同價）、low/medium/high effort、Frontier-Bench 為 4.8 的 2 倍、CursorBench 與 Fable 5 差 < 0.5%、Claude Max 新預設（2026-07-24）|
| [45-model-selection-guide.md](./45-model-selection-guide.md) | Claude 模型選型官方指南 | 從最強模型起步再往下調、四 class 定位、effort 改變 per-task 經濟性、Advisor（Sonnet+Fable = 90% 效能 / 63% 成本）、自建 eval > benchmark（2026-07-24）|
| [46-context-engineering-claude5.md](./46-context-engineering-claude5.md) | Claude 5 世代 Context Engineering 新規則 | system prompt 刪 80%+ 無退化、六條 Then→Now（judgment/tool design/progressive disclosure/去重/auto-memory/rich references）、Context Assembly 四層；workspace canonical = `.claude/refs/context-engineering-claude5.md`（2026-07-24）|
| [47-verification-loops-skills.md](./47-verification-loops-skills.md) | 用 Skill 建構驗證迴圈 | 驗證迴圈定義、內建 `/verify` 與 Code Review、Skill 寫法、四種部署形態（standalone/embedded/chained/PR-wide）、專案特定確定性規則即素材（2026-07-22）|
| [48-w28-w31-features.md](./48-w28-w31-features.md) | Claude Code W28–W31 新功能（v2.1.202–221）| Opus 5 上線、subagent 上限與巢狀關閉、`/fork` 改語義 + `/subtask`、`/verify`/`/code-review`/`/deep-research` 不再自動觸發、單段 `dir/**` allow 語義變更、sandbox credential mask、大量權限繞過修正（2026-07-05–08-03）|
| [49-mcp-2026-07-28.md](./49-mcp-2026-07-28.md) | MCP 2026-07-28 規格更新 | Stateless core（serverless/edge 可部署）、Extensions 版本化（MCP Apps / Tasks）、OAuth 2.0 + OIDC 對齊、企業 IdP 佈建、950+ servers、connector dashboard（2026-07-28）|

---

## 核心要點速查

### CLAUDE.md
- 長度 ≤ 200 行（最佳 60 行），只寫會改變 Claude 行為的內容
- 大型規則用 `.claude/rules/*.md` + `@import` 拆分，支援惰性載入
- Path-scoped rules 用 frontmatter 的 `paths:` 欄位

### Hooks
- 三層架構：Event → Matcher Group → Handler
- Exit code：0=成功、1=警告繼續、2=阻斷
- PreToolUse 防守，PostToolUse 自動化
- 非阻斷操作加 `"async": true`
- Conditional hooks：`if` 欄位條件式觸發（W13，v2.1.83+）
- Hooks 可讀取 effort level：`effort.level`（JSON）/ `$CLAUDE_EFFORT`（env，W19）
- `PostToolUse` 任意工具輸出替換：`hookSpecificOutput.updatedToolOutput`（W18）
- `args: string[]` exec form：直接 spawn，不經 shell，路徑不需加引號（W20）
- `continueOnBlock`（PostToolUse）：阻斷後將原因回傳 Claude 並繼續 turn（W20）
- `terminalSequence`：hook 輸出中設定視窗標題 / 桌面通知 / 響鈴（W20）

### Skill
- SKILL.md ≤ 500 行（超過用 Progressive Disclosure 拆子檔）
- description 要有觸發條件 + 排除條件（Do NOT use for）
- Known Gotchas section：每次踩坑後補充

### Sub-Agent
- 預期工具呼叫 > 20 次 → 必須委派
- 判斷心智模型：只需結論 → subagent；需反覆檢視 → 主對話
- 強模型（Opus/Fable）需要明確的平行指示

### MCP
- 工具數量建議 3–6 個 MCP servers
- Hooks 是確定性，Prompts 只是建議
- `alwaysLoad: true`：MCP server 跳過 tool-search deferral，所有工具常態可用（W18）

### Plugins
- Plugin vs Standalone：先用 standalone 快速迭代 → 準備跨專案分享/Marketplace 時轉 Plugin
- `plugin.json` 是唯一放在 `.claude-plugin/` 的檔案；`skills/`、`agents/`、`hooks/` 放根目錄
- 安裝：`/plugin install <url>` 或 `--plugin-url <url.zip>`（W19 起支援 URL/zip 直接載入）
- `claude plugin prune`：清除孤立 plugin 依賴

### 新 Skills（官方，2026 Q1+）
- `/simplify`：PR 完成後對已變更程式碼做 review for reuse/quality/efficiency，提交精煉後改善
- `/batch <task>`：一次性 fan-out 平行遷移（僅適合各目標互相獨立的任務）
- `/insights`：讀取過去一月 message history，輸出專案摘要、使用模式分析、改善建議
- `/ultraplan`：雲端規劃模式，web UI 編輯後可 teleport 回 terminal 執行
- `/ultrareview`：多 agent fleet 深度 code review；`claude ultrareview` 可在 CI 非互動執行

### Session 管理（新功能）
- PR URL 恢復：`/resume` 中貼入 PR URL → 自動過濾到建立該 PR 的 session（W18，v2.1.122+）
- CLI 恢復：`claude --from-pr <number>` 直接指定 PR 號
- `claude project purge`：清除專案所有本地狀態；`--dry-run` 預覽、`--all` 清除全部（W18）
- `worktree.baseRef`：`fresh`（遠端預設，default）或 `head`（本地 HEAD）（W19）
- **Agent View**：`claude agents` 開啟所有 session 的統一儀表板（W20，research preview）
- **`/goal`**：設定完成條件，Claude 持續執行直到條件成立（W20，v2.1.139）
- **Background sessions**：出現在 `/resume`（標記 `bg`），`Ctrl+T` 固定後保持存活（W21）
- **`claude agents --json`**：以 JSON 列出活躍 session，適合 status bar 腳本（W21）
- **`!` 前綴背景 job**：`claude agents` 中 `!cmd` 執行可 attach/detach 的背景工作（W22）

### W25 新功能（v2.1.178–183，2026-06-15 起）
- **Agent Teams 簡化**：移除 `TeamCreate`/`TeamDelete`，每個 session 自動有隱含 team；設 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 啟用
- **`Tool(param:value)` permission 語法**：deny/ask 規則支援工具輸入參數精細控制，如 `Agent(model:opus)` 阻止 Opus-level subagent spawn
- **Nested `.claude/skills/`**：子目錄 skills 現在可被載入，名稱衝突以 `<dir>:<name>` 格式顯示
- **Auto mode 破壞性指令攔截**：`git reset --hard`、`git clean -fd`、`git commit --amend`（非本 session 建立的 commit）、`terraform/pulumi/cdk destroy` 在未明確要求時一律封鎖
- **`/config key=value`**：runtime 直接設定，無需編輯 settings.json；`/config --help` 列出所有 shorthand
- **Subagent 5 層深度上限**：修正嵌套無限制 bug，防止 OOM 和成本失控
- **`attribution.sessionUrl`**：設定可從 commit/PR 省略 claude.ai session URL
- **Prompt cache 修復**：自訂 `ANTHROPIC_BASE_URL` / Foundry 環境現在能正確利用 cache（v2.1.181）
- **Artifacts**：session 轉互動網頁，自動更新，Team/Enterprise Beta（詳見 39-artifacts.md）

### W26–W27 新功能（v2.1.185–201，2026-06-20 起，詳見 42-w26-27-features.md）
- **⚠️ 預設 permission mode 改為 "Manual"**（v2.1.200）：CLI/VS Code/JetBrains 一致；自動化腳本/CI 需明確指定 `--permission-mode`
- **Claude Sonnet 5 發布**（v2.1.197）：新預設模型，1M context，促銷價 $2/$10（至 2026-08-31），詳見 41-claude-sonnet-5.md
- **Claude in Chrome 正式 GA**（v2.1.198）：詳見 43-claude-in-chrome.md
- **Subagent 預設背景執行 + 完成後自動 commit/push/開 draft PR**（v2.1.198）：稽核時機需提前到 PR review 階段
- **`sandbox.credentials`**（v2.1.187）：封鎖 sandboxed 指令讀取憑證檔案/secret 環境變數
- **`autoMode.classifyAllShell`**（v2.1.193）：auto mode 分類器擴及所有 Bash/PowerShell 指令
- **`claude_code.assistant_response` OTel 事件**（v2.1.193）：⚠️ 未設 `OTEL_LOG_ASSISTANT_RESPONSES` 時跟隨 `OTEL_LOG_USER_PROMPTS`，已記錄 prompt 的部署升級後會一併記錄 response
- **`/rewind` 支援跨越 `/clear` 恢復**（v2.1.191）
- **`CLAUDE_CODE_MAX_RETRIES` 上限**：v2.1.186 訂為 15，v2.1.199 對非容量類 transient error 解除上限並提高至 300
- **`/dataviz` skill**、**Org 層級預設模型**（v2.1.196）、移除 `/agents` wizard（v2.1.198）

### W28–W31 新功能（v2.1.202–221，2026-07-05 起，詳見 48-w28-w31-features.md）
- **Claude Opus 5 上線**（v2.1.219）：`claude-opus-5`，1M context，詳見 44-claude-opus-5.md
- **⚠️ 單段 `dir/**` allow 規則語義變更**（v2.1.214）：`Edit(src/**)` 與 hook `if:` 現在只匹配 `<cwd>/dir`，任意深度需寫 `**/dir/**`；`deny`/`ask` 維持任意深度
- **Subagent 扇出上限**：每 session 200（`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`）、同時 20（`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`）、**預設不再巢狀 spawn**（v2.1.212/217）
- **Task 工具 `mode` 參數廢除**（v2.1.212）：subagent 繼承 parent permission mode
- **`/fork` 改為建立獨立背景 session（自有 worktree）**，原 in-session subagent 改名 **`/subtask`**（v2.1.212/213）
- **驗證與研究不再自動觸發**：`/verify`、`/code-review`（v2.1.215）、`/deep-research`（v2.1.218）改為手動呼叫
- **背景 session 收尾語義**（v2.1.213）：commit + push，只在需要時開 draft PR，遵守 CLAUDE.md git 指示，結束一定回報工作落點
- **權限繞過密集修正**（v2.1.213/214/216）：zsh `[[ ]]` 隱藏命令、fd 重導向 fail closed、> 10,000 字元命令一律提示、`docker` daemon 重導向旗標需授權
- **沙箱**：`sandbox.credentials` 新增 `mode: "mask"`（Linux/WSL，v2.1.213）、`sandbox.network.strictAllowlist`（v2.1.219）、`sandbox.filesystem.disabled`（v2.1.216）
- **`claude-api` skill 新增 `prompt-audit`**（v2.1.213）：稽核為舊世代寫的 prompt / tool description
- **WebSearch 每 session 上限 200**、**MCP 呼叫 > 2 分鐘自動轉背景**（v2.1.212）
- **`--max-budget-usd` 現在會中止執行中的背景 agent**（v2.1.217）

### Dynamic Workflows（W22 新）
- 啟動：直接請求 "create a workflow that..."，或 `/effort ultracode`
- 管理：`/workflows` 查看執行中 workflows
- 六種模式：Classify-and-act / Fan-out-and-synthesize / Adversarial verification / Generate-and-filter / Tournament / Loop until done
- 用於：大型遷移、全 codebase audit、需要並行驗證的複雜任務
- 方案：Max、Team Premium、Enterprise PAYG、API（Research Preview）

### 新指令（W21–W22）
- `/code-review [low|medium|high|max]`：報告正確性 bug；`--comment` 發布 GitHub PR 行內評論（W21）
- `/usage`：顯示 skill/subagent/plugin/MCP server 各自消耗的配額（W21）
- `/reload-skills`：重新掃描 skill 目錄，不需重啟（W22）
- `/workflows`：管理動態 workflows（W22）

### 模型（最新，截至 2026-08-04）

| Model | ID | 輸入 | 輸出 | 備註 |
|-------|-----|------|------|------|
| **Claude Fable 5** | `claude-fable-5` | $10/MTok | $50/MTok | 最強公開模型；1M ctx；128k 輸出；2026-06-09 GA |
| **Claude Mythos 5** | `claude-mythos-5` | $10/MTok | $50/MTok | Project Glasswing 受邀限定；無安全分類器 |
| **Claude Opus 5** | `claude-opus-5` | $5/MTok | $25/MTok | **2026-07-24 發布**；1M ctx；low/medium/high effort；Claude Max 預設、Pro 最強；多數任務逼近 Fable 5 而價格減半；詳見 44-claude-opus-5.md |
| **Claude Opus 4.8** | `claude-opus-4-8` | $5/MTok | $25/MTok | 前代深推理檔位；Fable 5 安全路由的備援模型；已被 Opus 5 取代 |
| **Claude Sonnet 5** | `claude-sonnet-5` | $2/MTok（促銷至 08-31，之後 $3）| $10/MTok（促銷，之後 $15）| CLI 預設模型（v2.1.197，2026-06-30）；1M ctx；取代 Sonnet 4.6；詳見 41-claude-sonnet-5.md |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251001` | $0.25/MTok | $1.25/MTok | 速度/成本最優 |

- Sonnet 4.6 已被 Sonnet 5 取代為預設模型（仍可手動選用）
- **Opus 5 fast mode**：約 2.5× 速度、2× 價格（$10/$50）
- **選型框架**：從一般可用的最強模型起步再依延遲/成本往下調；class × effort 決定 per-task 經濟性 → 45-model-selection-guide.md

- **Fable 5 訂閱方案**：Pro/Max/Team/Enterprise 免費用至 2026-06-22；2026-06-23 起需 Usage Credits（API 費率）
- **Fable 5 安全分類器**：cyber / bio-chem / distillation 請求自動路由至 Opus 4.8（< 5% sessions）；Fable 5 prompt cache 與 Opus 4.8 不相容
- **Fast mode on Opus 4.8**：$10/$50 per MTok（標準費率 2×，速度 2.5×）；Fable 5 standard 同價，勿混淆
- Opus 4.6 fast mode 已 deprecated

### Security Guidance Plugin（W22 新）
- 安裝：`/plugin install security-guidance@claude-plugins-official`
- 三層掃描：edit 後快速 pattern check → turn 結尾 model review → commit/push 時 agentic review
- 自訂規則：`.claude/claude-security-guidance.md`

---

## 關鍵來源

| 類型 | URL |
|------|-----|
| 官方 Hooks 指南 | https://code.claude.com/docs/en/hooks-guide |
| 官方 Memory 文件 | https://code.claude.com/docs/en/memory |
| 官方 Settings 文件 | https://code.claude.com/docs/en/settings |
| 官方 Sub-Agents | https://code.claude.com/docs/en/sub-agents |
| 官方 Skills | https://code.claude.com/docs/en/skills |
| 官方最佳實踐 | https://code.claude.com/docs/en/best-practices |
| 社群最佳實踐 | https://github.com/shanraisshan/claude-code-best-practice |
| Awesome Claude Code | https://github.com/hesreallyhim/awesome-claude-code |
| Hooks 實戰 | https://github.com/disler/claude-code-hooks-mastery |
| Anthropic Engineering | https://www.anthropic.com/engineering/claude-code-best-practices |
