---
title: "Claude Code Memory System: MEMORY.md, Topic Files, and Automated Maintenance"
author: "Ian L. Paterson"
date: "2026-02-22"
source: "https://ianlpaterson.com/blog/claude-code-memory-architecture/"
tags: "[claude-code, memory, MEMORY.md, cron, automation, persistence, cross-session]"
topic: memory
---

# Claude Code Memory System: MEMORY.md, Topic Files, and Automated Maintenance

Ian L. Paterson 在管理 34 個跨 corporate strategy、AI infrastructure、content 的專案時建立了一套四層記憶架構，搭配五個自主 cron job 維護，跨 session 零重複解釋，月費 ~US$8。

## 四層記憶架構

**Layer 1 — Always Loaded（每次 session 自動載入）**
- `MEMORY.md`：嚴格 200 行上限，含日期戳記的 lessons
- Global `CLAUDE.md`：人格設定 + session 生命週期規則

**Layer 2 — Daily Logs（每日日誌）**
- 路徑：`~/llm-data/daily-log/`，每天一個檔案
- 記錄：完成工作、決策、未結事項、學到的 lessons

**Layer 3 — Project State（專案狀態）**
- 每個 project 的 `CLAUDE.md`，含 Status section
- 追蹤：工作狀態、阻塞項、近期操作記錄（append-only log）

**Layer 4 — On Demand（按需載入）**
- 10 個 domain-specific topic files（via `/project` 指令）
- 22 個 shared context files（穩定文件）
- 6 個 navigation indexes（project/script/resource 映射）

## 五個自主 Cron Jobs

| Script | 排程 | 功能 |
|--------|------|------|
| `rotate-memory-lessons.sh` | 每週日 | 將超過 200 行上限的 lessons 歸檔 |
| `check-memory-rules.sh` | 每週日 | 驗證 8 條設計規則 |
| `rotate-state-entries.sh` | 每週日 | 歸檔超過 2 週的 project state entries |
| `check-consistency.sh` | 每日 | diff indexes 與實際 filesystem |
| `heartbeat.sh` | 每 6 小時 | 將逾期事項寫入 daily log |

## 核心指令

```
/project [name]  — 載入 project context（~4 秒），顯示狀態與相關 topic files
/flush           — 單一寫入觸發，捕捉狀態至 daily logs + project CLAUDE.md + MEMORY.md
```

## 8 條設計規則

1. 每個檔案都能透過 index/mapping 找到
2. 每條 lesson 都有 `[YYYY-MM-DD]` 日期戳記
3. 寫入目標有固定 schema
4. Cron jobs 有預算上限並帶失敗告警
5. 所有 indexes 有過期偵測器
6. 每個事實只存在一個位置（single source of truth）
7. 檔案大小符合其載入機制
8. 不重建 Claude Code 已有的原生功能

## 驗證指標（22 天，34 個專案）

| 指標 | 數值 |
|------|------|
| 跨 session 零重複解釋次數 | 0 次 |
| 累積 lessons | 130+ 條 |
| 自我審計發現的問題 | 13 個結構性問題 |
| 月費（rotation/compliance） | ~US$8 |
| 總檔案數 | 50 個（全純 markdown + scripts） |

**關鍵失敗案例**：一個 501 行的 MEMORY.md（設計 200 行上限）導致 60% 的 lessons 不可見，無法進入 context window——直到 cron job 觸發歸檔才恢復。

## 基礎設施

- US$6/月 DigitalOcean VPS
- SyncThing 跨機器同步（免費）
- Local LLM：Qwen3.6-27B + Dell Precision T5820 + RTX 3090 Ti
- **不用 RAG**：對小型 corpus，filesystem retrieval 在正確性與相關性上優於 vector RAG

## Key Insights
- 四層記憶架構：always-loaded（MEMORY.md 200 行上限 + CLAUDE.md）、daily logs、project state（每專案 append-only log）、on-demand（10 topic files + 22 shared context + 6 navigation indexes）
- 五個 cron jobs 自主維護：rotate-memory-lessons.sh（週）、check-memory-rules.sh（週）、rotate-state-entries.sh（週）、check-consistency.sh（日）、heartbeat.sh（6hr）— 月費 ~US$8
- 關鍵驗證：34 個專案/22 天；130+ 條壓縮 lessons；13 個結構性問題自我偵測；501 行 MEMORY.md 導致 60% lessons 不可見

## Code Examples / Commands

```bash
# heartbeat.sh（每 6 小時執行）
#!/bin/bash
OVERDUE=$(find ~/llm-data/tasks/ -name "*.md" -mtime +7 2>/dev/null)
if [ -n "$OVERDUE" ]; then
  DATE=$(date +%Y-%m-%d)
  echo "## Overdue items flagged at $DATE" >> ~/llm-data/daily-log/$DATE.md
  echo "$OVERDUE" >> ~/llm-data/daily-log/$DATE.md
fi
```

```bash
# check-consistency.sh（每日執行）
#!/bin/bash
# diff navigation indexes 與實際 filesystem
find ~/llm-data/projects/ -name "*.md" | sort > /tmp/actual-files.txt
cat ~/llm-data/indexes/project-index.md | grep -oP '(?<=\[).+(?=\])' | sort > /tmp/indexed-files.txt
diff /tmp/actual-files.txt /tmp/indexed-files.txt
```
