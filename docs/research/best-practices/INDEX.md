---
title: Claude Code 最佳實踐研究索引
type: index
---

# Claude Code 最佳實踐研究索引

> **Type:** wiki:compiled — 29 docs covering hooks, agents, skills, permissions, MCP, sandbox  
> 收集日期：2026-04-25（最後更新：2026-05-10）

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
| [23-whats-new-w13-w17.md](./23-whats-new-w13-w17.md) | Claude Code What's New 週版本彙整（W13-W17）| v2.1.83→v2.1.119，24 個主要功能：Auto mode、Computer use、Conditional hooks、Ultraplan、Opus 4.7 xhigh、Routines Web UI、/ultrareview（2026-05-01）|
| [24-plugins.md](./24-plugins.md) | Claude Code Plugin 系統完整指南 | Plugin vs Standalone 決策表、plugin.json manifest schema、全組件類型（skills/agents/hooks/MCP/LSP/monitors）、Marketplace 提交、Standalone 遷移（2026-05-01）|
| [25-bcherny-config-github.md](./25-bcherny-config-github.md) | Boris Cherny 實際 GitHub 設定完整解析 | CLAUDE.md 自更新哲學、7 slash commands（/grill、/techdebt、/worktree 等）、6 specialized agents（code-simplifier、staff-reviewer、oncall-guide 等）、settings.json PostToolUse 格式化 hook、/loop 4 個真實配方（2026-05-01）|
| [26-new-features-2026-q1.md](./26-new-features-2026-q1.md) | Claude Code 新功能彙整 2026 Q1 | /simplify+/batch 官方新 Skills（PR shepherd + 平行遷移）、/insights 工作流自我診斷指令、Spec-Based Development 模式（AskUserQuestionTool 訪問流程）、Claude Code = 通用 Agent 哲學（Anthropic 內部確認）（2026-05-01）|
| [27-whats-new-w18-w19.md](./27-whats-new-w18-w19.md) | Claude Code What's New 週版本彙整（W18-W19）| v2.1.120→v2.1.136，6 個主要功能：Windows 無需 Git Bash、claude project purge、PR URL 恢復 Session、Plugin .zip/URL 載入、Ctrl+R 跨專案歷史搜尋、autoMode.hard_deny、Hooks effort level（2026-05-10）|
| [28-thariq-prompt-caching-lessons.md](./28-thariq-prompt-caching-lessons.md) | Prompt Caching 核心教訓（Thariq Shihipar）| 分層快取結構（靜態→動態）、用 messages 代替 system prompt 更新、mid-session 禁止切換模型、工具 stub + defer_loading、Compact 保留前綴、Cache Hit Rate 監控（2026-05-16）|
| [29-onboarding-large-codebase.md](./29-onboarding-large-codebase.md) | Claude Code Onboarding 與大型 Codebase 最佳實踐 | 三層 Context 架構（context repo + Skills + MCP）、Agentic Search vs RAG、五元件 Harness（CLAUDE.md/Hooks/Skills/Plugins/MCP）、每 3-6 個月審閱設定、組織 DRI 所有權（2026-05-16）|

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

### Skill
- SKILL.md ≤ 500 行（超過用 Progressive Disclosure 拆子檔）
- description 要有觸發條件 + 排除條件（Do NOT use for）
- Known Gotchas section：每次踩坑後補充

### Sub-Agent
- 預期工具呼叫 > 20 次 → 必須委派
- 判斷心智模型：只需結論 → subagent；需反覆檢視 → 主對話
- Opus 4.7 需要明確的平行指示

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
