---
task_id: task-04-doc-summary
description: 閱讀 prompt-caching-rules.md 並產出結構化摘要
expected_behavior: |
  摘要需包含：
  1. Cache 運作的核心原則（Static First 順序）
  2. Cache 失效的條件（至少 3 個）
  3. 模型差異的 cache 最低 token 門檻（Sonnet/Haiku/Opus 各別數字）
  4. Compact 與 cache 的關係
  格式：要點清單，≤200 字
source: prompt-caching-rules.md documentation task
metrics:
  reasoning_tokens: 300–1000
  completion_rate: pass/fail
  output_quality: 0–10
target_models:
  - haiku-4-5
  - sonnet-4-6
  - opus-4-7
---

## 任務說明

請閱讀 `.claude/refs/prompt-caching-rules.md`，然後產出一份結構化摘要：

**要求**：
- 格式：要點清單（Markdown bullet points）
- 長度：≤200 字
- 必須涵蓋：
  1. Cache prefix 的靜態→動態順序
  2. 哪些操作會讓 cache 失效（至少列出 3 個）
  3. 各模型的最低 token 門檻（Sonnet 4.6/4.5、Haiku 4.5、Opus）
  4. Compact 時如何避免 cache 失效（1 句）
