# claude-blog/INDEX.md

> **Type:** raw:blog — Anthropic 官方 blog / docs 外部歸檔（LLM 只讀不改）；~91 篇  
> **Updated**: 2026-06-05  
> **Query pattern**: BRAIN.md → 本表（Category）→ `<category>/index.md` → 具體文章

---

## 子目錄索引

| 目錄 | 篇數 | 主題 | 索引 |
|------|------|------|------|
| [claude-code/](claude-code/) | ~26 | Claude Code 功能 · 工作流 · API · Dynamic Workflows | [index.md](claude-code/index.md) |
| [agents/](agents/) | ~19 | Agent 設計 · Sub-agents · Orchestration | [index.md](agents/index.md) |
| [announcements/](announcements/) | ~23 | 模型發布 · 功能公告 · 版本說明 | [index.md](announcements/index.md) |
| [enterprise-ai/](enterprise-ai/) | ~24 | 企業 AI · 安全 · 合規 · 部署 · Zero Trust | [index.md](enterprise-ai/index.md) |
| [docs/](docs/) | 3 (synthesis) | 官方 docs 合成 · Codebase summary · Timeline | — |

## 延伸文件

| 檔案 | 說明 |
|------|------|
| [REPORT.md](REPORT.md) | Best-practices 研究報告（含各分類評分）|
| [docs/synthesis.md](docs/synthesis.md) | 官方 docs 跨文件合成摘要 |
| [docs/timeline.md](docs/timeline.md) | 功能發布時間線 |
| [docs/codebase-summary.md](docs/codebase-summary.md) | Codebase 整體摘要 |

## Typed Edges

| Edge | From | To |
|------|------|----|
| `references` | `research/best-practices/INDEX.md` | `claude-blog/` (官方 blog → best-practice 篩選) |
| `cited-by` | `research/ai-articles/scored/` | `claude-blog/` (多篇 scored 文章引用官方 blog) |
