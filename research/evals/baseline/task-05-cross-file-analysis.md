---
task_id: task-05-cross-file-analysis
description: 分析 CLAUDE.md 與 4 個 rules 檔案之間的引用與依賴關係
expected_behavior: |
  分析需包含：
  1. CLAUDE.md 中 @-引用的所有 rules 檔案清單（精確路徑）
  2. 各 rules 檔案的功能定位（1 句）
  3. 各 rules 檔案的 byte 大小（執行 wc -c 取得）
  4. 識別哪個檔案佔 auto-load 比重最大（附百分比）
  5. 識別 security-hygiene.md 的特殊地位（path-scoped，非常駐）
source: harness architecture analysis (task-05)
metrics:
  reasoning_tokens: 500–1500
  completion_rate: pass/fail
  output_quality: 0–10
target_models:
  - haiku-4-5
  - sonnet-4-6
  - opus-4-7
---

## 任務說明

請執行跨檔分析：

1. 讀取 `CLAUDE.md`，列出所有 `@.claude/rules/*.md` 引用（精確路徑）
2. 讀取每個被引用的 rules 檔案，用 1 句話描述其功能定位
3. 執行 `wc -c CLAUDE.md .claude/rules/core.md .claude/rules/context-management.md .claude/rules/output-discipline.md .claude/rules/subagent-strategy.md` 取得各檔 byte 大小
4. 計算每個檔案佔 auto-load 總量的百分比（以 11,313 bytes 為基準）
5. 說明 `security-hygiene.md` 與其他 rules 檔的差異
