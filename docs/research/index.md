# research/INDEX.md

> **Type:** wiki:index — SRE / Cloud Architect 知識中樞（compiled + raw + generated）  
> **Updated**: 2026-06-07 | **Sub-directories**: 14+  
> **Query pattern**: BRAIN.md → 本表（Looking for…）→ 子目錄 index.md → 具體文件

---

## Agent 快速導覽

| 查詢目標 | 前往 | 類型 |
|---------|------|------|
| Agent harness 評估 | [agent-harness/index.md](agent-harness/index.md) | wiki:compiled |
| 最新 AI 新聞（7 日儀表板）| [archive-index.md](archive-index.md) | wiki:auto |
| Claude Code 官方指引 | [claude-blog/index.md](claude-blog/index.md) | wiki:compiled |
| 學術論文 | [papers/index.md](papers/index.md) | raw:indexed |
| 深度研究報告 | [reports/index.md](reports/index.md) | wiki:generated |
| Claude Code 最佳實踐 | [best-practices/index.md](best-practices/index.md) | wiki:compiled |
| 推文 / 文章歸檔 | [tweets/index.md](tweets/index.md) | raw:indexed |

---

## 目錄地圖

| 子目錄 | 類型 | 規模 | 說明 |
|-------|------|------|------|
| [agent-harness/](agent-harness/) | wiki:compiled | 16 docs | CAR 14-component 框架；HARNESS-CARD；RATCHET |
| [claude-blog/](claude-blog/) | wiki:compiled | ~91 篇 | claude.com/blog 歸檔 2024–2026 |
| [best-practices/](best-practices/) | wiki:compiled | 32 docs | 官方 + 社群 Claude Code 最佳實踐 |
| [papers/](papers/) | raw:indexed | 183 papers | 學術 LLM/agent 論文 2022–2026（PDF + MD）|
| [reports/](reports/) | wiki:generated | 47 active + 39 archived | autoresearch / overnight-research 深度報告 |
| [tweets/](tweets/) | raw:indexed | 186 files | Twitter/X 研究歸檔 |
| [videos/](videos/) | raw:indexed | 7 transcripts | Podcast / YouTube 研究摘要 |
| [medium/](medium/) | raw:indexed | 1 article | Medium 文章歸檔 |
| [prompts/](prompts/) | schema | 9 files | 研究任務 prompt 模板 |
| [templates/](templates/) | schema | 3 files | ai-news / overnight-research / tweets 模板 |

---

## Query Patterns

```
"最新的 LLM agent 論文有哪些？"
  → papers/index.md → browse by topic

"今天的 AI 新聞"
  → archive-index.md（7-day dashboard）

"Harness 目前評分多少？"
  → agent-harness/index.md → HARNESS-CARD.md

"最近有哪些深度研究報告？"
  → reports/index.md → sort by date

"Claude Code 官方如何建議處理 context？"
  → claude-blog/index.md → claude-code/ 類別
```
