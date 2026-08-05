# Claude Blog Analysis Docs

claude-blog 分析文件，從 153 個收錄條目（去重後約 138 篇 claude.com/blog 與 anthropic.com 文章，2025-11-13 ~ 2026-07-28）提煉。

| 檔案 | 說明 | 涵蓋範圍 |
|------|------|---------|
| [`synthesis.md`](./synthesis.md) | 主題精粹（跨類別洞察整合）| 主題一～六至 2026-04-22；主題七～九增補至 2026-07-28 |
| [`timeline.md`](./timeline.md) | 發布時間軸 | 2025-11-13 ~ 2026-07-28（列出重點條目）|
| [`codebase-summary.md`](./codebase-summary.md) | 代碼庫與結構摘要 | — |

## 2026 下半年的三條主線

讀 `synthesis.md` 前先掌握這三點，其餘內容都掛在它們底下：

1. **從「堆規則」轉向「信任判斷」** — Claude 5 世代刪 system prompt 80%+ 無退化；衝突指令會消耗推理預算。
2. **驗證的觸發權從模型收回 harness** — 官方推廣驗證 Skill，同時關掉 `/verify`、`/code-review`、`/deep-research` 的自動觸發。
3. **扇出從「越多越好」轉向「有界治理」** — subagent 上限、預設不巢狀、預算硬止血、背景 session 收尾語義明確化。

索引：[claude-blog 總索引](../) · 統計：[REPORT.md](../REPORT)

*最後更新：2026-08-05*
