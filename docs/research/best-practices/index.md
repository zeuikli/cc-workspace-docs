---
title: "Claude Code 最佳實踐研究索引"
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
| [01-official-hooks-memory-settings](./01-official-hooks-memory-settings) | 官方 Hooks / Memory / Settings | Hook 三層架構、4 種 Handler 類型、Exit Code 規約、CLAUDE.md 載入順序、Settings 層級 |
| [02-community-claudemd-agent-skill](./02-community-claudemd-agent-skill) | 社群 CLAUDE.md / Agent / Skill | CLAUDE.md 設計原則、Command→Agent→Skill 架構、Skill 設計模式、Context 管理 |
| [03-hooks-patterns](./03-hooks-patterns) | Hooks 實戰設計模式 | 25 種 Hook 事件、13 個完整 shell script 範例、完整 settings.json 範本、最佳實踐 checklist |
| [04-subagent-mcp-skill](./04-subagent-mcp-skill) | Sub-Agent / MCP / Skill 進階 | 委派策略、Model 分層（Haiku/Sonnet/Opus）、Advisor 模式、MCP 整合、Tasks 原語 |
| [05-claude-prompting-best-practices](./05-claude-prompting-best-practices) | 官方 Prompt Engineering 完整指南 | Opus 4.7 行為調整、Effort 等級、XML 標籤結構、平行工具呼叫、Agentic 系統、遷移指引 |
| [06-agent-skills-best-practices](./06-agent-skills-best-practices) | 官方 Agent Skills 撰寫最佳實踐 | 簡潔原則、自由度校準、Progressive Disclosure、Checklist Pattern、Plan-Validate-Execute |
| [07-advisor-tool-best-practices](./07-advisor-tool-best-practices) | 官方 Advisor Tool 完整技術指南 | Executor+Advisor 架構、模型相容性、Timing 指引、官方 System Prompt 範本 |
| [08-prompt-caching](./08-prompt-caching) | 官方 Prompt Caching 完整技術指南 | 自動/明確兩種實作、最小 token 閾值、失效條件、Pre-warming、跨場景策略 |
| [09-secure-deployment](./09-secure-deployment) | AI Agent 安全部署完整指南 | 威脅模型、Sandbox/Docker/gVisor/VM 隔離比較、Proxy Pattern 憑證管理 |
| [10-agent-skills-enterprise](./10-agent-skills-enterprise) | Agent Skills 企業治理指南 | 風險層級評估表、8 步安全 Checklist、評估維度、生命週期管理 |
| [11-routines](./11-routines) | Routines 排程自動化完整指南 | Scheduled / API trigger / GitHub Webhook 三種觸發模式、Routine 建立流程 |
| [12-permissions](./12-permissions) | 細粒度 Permission 設定完整指南 | Permission 系統架構、wildcard 語法、allow/block/prompt 三種模式 |
| [13-sandbox](./13-sandbox) | Sandboxing OS 層隔離技術詳解 | Sandbox 原理、Filesystem/Network 隔離、OS 層技術、設定選項 |
| [14-mcp](./14-mcp) | MCP 整合完整指南 | HTTP/SSE/stdio 三種 transport 安裝、Scope 優先序、OAuth 完整設定 |
| [15-boris-cherny-tips](./15-boris-cherny-tips) | Boris Cherny Claude Code Tips 主題整合 | 7 個 tip 集合（2026-01 至 2026-04，約 60 個技巧） |
| [16-thariq-tips](./16-thariq-tips) | Thariq Claude Code Tips — Skill 設計與 Session 管理 | T1-T9 Skill 設計原則、9 種 Skill 類型、Session 管理深度指南 |
| [17-best-practices-overview](./17-best-practices-overview) | Claude Code 最佳實踐官方總綱 | 驗證工作流、探索→規劃→實作四階段、Context 管理、平行化與自動化 |
| [18-how-claude-code-works](./18-how-claude-code-works) | How Claude Code Works — Agentic Loop / Tools / Context | Agentic Loop 三階段、五類 Built-in Tools、Session 管理 |
| [19-features-overview](./19-features-overview) | Extend Claude Code 功能總覽與選擇指南 | CLAUDE.md vs Skills vs MCP vs Subagents vs Agent Teams vs Hooks vs Plugins 比較表 |
| [20-common-workflows](./20-common-workflows) | Common Workflows 逐步實戰指南 | Codebase 探索、Bug Fix、Refactoring、Tests、PR、Plan Mode、Session 管理 |
| [21-memory-claudemd](./21-memory-claudemd) | CLAUDE.md 與 Auto Memory 完整指南 | CLAUDE.md 多層級設定、路徑範圍規則、Auto Memory 機制 |
| [22-code-review](./22-code-review) | Code Review 多代理 PR 自動審查完整指南 | multi-agent 審查流程、severity 等級、`@claude review` 指令 |
| [23-whats-new-w13-w17](./23-whats-new-w13-w17) | Claude Code What's New 週版本彙整（W13-W17）| v2.1.83→v2.1.119，24 個主要功能 |
| [24-plugins](./24-plugins) | Claude Code Plugin 系統完整指南 | Plugin vs Standalone 決策表、plugin.json manifest schema |
| [25-bcherny-config-github](./25-bcherny-config-github) | Boris Cherny 實際 GitHub 設定完整解析 | CLAUDE.md 自更新哲學、7 slash commands、6 specialized agents |
| [26-new-features-2026-q1](./26-new-features-2026-q1) | Claude Code 新功能彙整 2026 Q1 | /simplify+/batch 官方新 Skills、/insights、Spec-Based Development 模式 |
| [27-whats-new-w18-w19](./27-whats-new-w18-w19) | Claude Code What's New 週版本彙整（W18-W19）| v2.1.120→v2.1.136，6 個主要功能 |
| [28-thariq-prompt-caching-lessons](./28-thariq-prompt-caching-lessons) | Prompt Caching 核心教訓（Thariq Shihipar）| 分層快取結構、mid-session 禁止切換模型 |
| [29-onboarding-large-codebase](./29-onboarding-large-codebase) | Claude Code Onboarding 與大型 Codebase 最佳實踐 | 三層 Context 架構、Agentic Search vs RAG、五元件 Harness |

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
- `alwaysLoad: true`：MCP server 跳過 tool-search deferral（W18）

### Plugins
- Plugin vs Standalone：先用 standalone 快速迭代 → 準備跨專案分享時轉 Plugin
- `plugin.json` 是唯一放在 `.claude-plugin/` 的檔案
- 安裝：`/plugin install <url>` 或 `--plugin-url <url.zip>`（W19+）

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
