---
task_id: task-02-code-modify-hook
description: 讀取 hook 腳本並輸出加入說明 comment 後的修改版本
expected_behavior: |
  1. 正確讀取 .claude/hooks/session-init.sh
  2. 在腳本開頭加入 1-2 行說明 comment（說明此 hook 的觸發時機與作用）
  3. 輸出修改後的完整腳本內容（不需寫入檔案，僅輸出）
  4. comment 符合 bash 語法（# 開頭），不破壞原有功能
source: workspace hook design
metrics:
  reasoning_tokens: 200–800
  completion_rate: pass/fail
  output_quality: 0–10
target_models:
  - haiku-4-5
  - sonnet-4-6
  - opus-4-7
---

## 任務說明

請執行以下步驟：

1. 讀取 `.claude/hooks/session-init.sh` 的內容
2. 理解此 hook 的用途（從程式碼推斷）
3. 在腳本最頂端（shebang 行之後）加入 1-2 行 comment，說明：
   - 此 hook 的觸發時機（何時執行）
   - 此 hook 的主要作用
4. 將修改後的完整腳本內容輸出（不要寫入任何檔案，僅輸出到對話）

**注意**：不需要執行或寫入任何檔案。
