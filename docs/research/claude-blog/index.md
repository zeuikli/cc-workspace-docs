# claude-blog/INDEX.md

> Type: raw:corpus
> Harness-Layer: L4-knowledge
> **Type:** raw:blog — Anthropic 官方 blog / docs 外部歸檔（LLM 只讀不改）；153 條目 / 去重後約 138 篇  
> **涵蓋期間**：2025-11-13 ~ 2026-07-28  
> **Updated**: 2026-08-05  
> **Query pattern**: BRAIN.md → 本表（Category）→ `<category>/index.md` → 具體文章

---

## 子目錄索引

| 目錄 | 條目數 | 涵蓋期間 | 主題 | 索引 |
|------|------|---------|------|------|
| [claude-code/](claude-code/) | 45 | 2026-01-29 ~ 2026-07-24 | Claude Code 功能 · 工作流 · API · Dynamic Workflows · 驗證迴圈 | [index.md](claude-code/index.md) |
| [agents/](agents/) | 25 | 2025-11-13 ~ 2026-07-24 | Agent 設計 · Sub-agents · Orchestration · Context Engineering | [index.md](agents/index.md) |
| [announcements/](announcements/) | 38 | 2026-02-17 ~ 2026-07-28 | 模型發布 · 功能公告 · 版本說明 · MCP 規格 | [index.md](announcements/index.md) |
| [enterprise-ai/](enterprise-ai/) | 45 | 2025-11-17 ~ 2026-07-24 | 企業 AI · 安全 · 合規 · 部署 · Zero Trust · 前線案例 | [index.md](enterprise-ai/index.md) |
| [docs/](docs/) | 3 (synthesis) | — | 官方 docs 合成 · Codebase summary · Timeline | [index.md](docs/index.md) |

> 部分文章同時收錄於多個分類（如 `the-new-rules-of-context-engineering-...` 在 claude-code 與 agents），故條目數合計 153 大於去重後篇數。

## 延伸文件

| 檔案 | 說明 |
|------|------|
| [REPORT.md](REPORT.md) | 收錄統計、核心主題分析、Top 8 推薦閱讀、收錄狀態追蹤 |
| [docs/synthesis.md](docs/synthesis.md) | 跨文件合成：主題一～六（至 2026-04）+ 主題七～九（2026 下半年三個轉向）|
| [docs/timeline.md](docs/timeline.md) | 發布時間軸（2025-11-13 ~ 2026-07-28）|
| [docs/codebase-summary.md](docs/codebase-summary.md) | Codebase 整體摘要 |

## 近期重點條目（2026-06 ~ 2026-07）

| 日期 | 分類 | 文章 |
|------|------|------|
| 2026-07-28 | announcements | [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) |
| 2026-07-24 | announcements | [Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) |
| 2026-07-24 | claude-code · agents | [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) |
| 2026-07-24 | 三分類 | [Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) |
| 2026-07-22 | claude-code | [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) |
| 2026-07-21 | 三分類 | [How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) |
| 2026-07-17 | enterprise-ai | [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai) |
| 2026-07-16 | claude-code · enterprise-ai | [How Anthropic runs large-scale code migrations with Claude Code](https://claude.com/blog/ai-code-migration) |
| 2026-07-07 | claude-code | [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) |
| 2026-06-30 | announcements | [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) |
| 2026-06-30 | claude-code | [Getting started with loops](https://claude.com/blog/getting-started-with-loops) |
| 2026-06-24 | enterprise-ai | [Building effective human-agent teams](https://claude.com/blog/building-effective-human-agent-teams) |
| 2026-06-18 | claude-code | [Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) |
| 2026-06-18 | announcements | [Claude Code now supports artifacts](https://claude.com/blog/artifacts-in-claude-code) |

## Typed Edges

| Edge | From | To |
|------|------|----|
| `references` | `research/best-practices/INDEX.md` | `claude-blog/` (官方 blog → best-practice 篩選) |
| `cited-by` | `research/ai-articles/scored/` | `claude-blog/` (多篇 scored 文章引用官方 blog) |
| `cited-by` | `docs/lectures/` | `claude-blog/` (課程講義的官方一手來源) |
