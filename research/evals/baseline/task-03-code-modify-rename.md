---
task_id: task-03-code-modify-rename
description: 讀取腳本，將指定變數名稱重新命名並輸出修改版本
expected_behavior: |
  1. 正確讀取 .claude/hooks/audit-log.sh
  2. 找到並重命名指定變數（不改變邏輯）
  3. 輸出修改後的完整腳本
  4. 所有出現位置均正確替換，不遺漏
source: surgical edit discipline (R3)
metrics:
  reasoning_tokens: 200–600
  completion_rate: pass/fail
  output_quality: 0–10
target_models:
  - haiku-4-5
  - sonnet-4-6
  - opus-4-7
---

## 任務說明

請執行以下步驟：

1. 讀取 `.claude/hooks/audit-log.sh`
2. 找到腳本中所有的 `LOG_FILE` 變數（包含賦值和使用）
3. 將 `LOG_FILE` 重新命名為 `AUDIT_LOG_PATH`（所有出現位置）
4. 輸出修改後的完整腳本（不要寫入任何檔案，僅輸出到對話）
5. 說明總共替換了幾處

**注意**：不需要執行或寫入任何檔案。
