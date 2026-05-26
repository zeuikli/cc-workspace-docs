---
task_id: task-01-simple-qa
description: 查詢 workspace auto-load 規則的關鍵數字與檔案
expected_behavior: |
  回答需包含：
  1. auto-load 上限：12,000 bytes
  2. 計入 auto-load 的檔案清單（CLAUDE.md + 4 個規則檔）
  3. 驗證指令：wc -c .claude/rules/*.md CLAUDE.md | tail -1
  不應包含臆測或錯誤數字。
source: core.md rule + harness design
metrics:
  reasoning_tokens: 100–500
  completion_rate: pass/fail
  output_quality: 0–10
target_models:
  - haiku-4-5
  - sonnet-4-6
  - opus-4-7
---

## 任務說明

請回答以下問題（不需要執行任何 Bash 命令，純粹依據 workspace 規則回答）：

1. 這個 workspace 的 auto-load 總 byte 上限是多少？
2. 哪些檔案計入 auto-load 上限？請列出完整清單。
3. 如何用一行 shell 指令驗證當前 auto-load 使用量？
4. 目前 auto-load 剩餘空間大約是多少 bytes？（需要執行指令才能回答則跳過）
