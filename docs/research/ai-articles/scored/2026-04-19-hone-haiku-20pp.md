# Using GEPA to Hone Claude Haiku on GitHub Bug Fixes (+20%)

**來源**：https://tim.waldin.net/blog/2026-04-19-hone-haiku-20pp  
**作者**：Timothy Waldin  
**日期**：2026-04-19  
**收錄日期**：2026-04-20

---

## 文章摘要

Claude Haiku 4.5 用 14 個字的 seed prompt 可解決 65% 的真實 GitHub bug。作者用 GEPA（來自 dspy 的 prompt 演化優化器）跑 7 小時、20 個 bug-fix 訓練挑戰，優化後的 prompt 讓同一個模型在 **9 個未見過的 bug 上達到 85% 解決率**，純靠 prompt prose 提升 20 個百分點。

### 系統架構（三個現成工具組合）

| 元件 | 用途 |
|------|------|
| **GEPA** | Prompt 優化器（pareto 式 mutation + selection，來自 dspy） |
| **harness** | Python 函式庫，把 6 個 AI coding CLI（Claude Code、Codex、opencode、Gemini、Cursor、Aider）封裝成統一 API |
| **agentelo** | Leaderboard / 挑戰評分器，評分公式：`tests_fixed / tests_broken_before` |
| **hone** | ~300 行協調器，串起以上三者 |

### 訓練結果

20 個來自 5 個 repo（click/marshmallow/qs/jinja/koa）的真實 PR：

| iter | candidate | full valset (20) | delta |
|------|-----------|-----------------|-------|
| 0 | seed（14 words）| 0.5476 | — |
| 1 | candidate 1（6-step v1）| 0.8583 | +0.3107 |
| 2 | candidate 2（6-step v2）| 0.9176 | +0.3700 |
| 3 | candidate 3（tied）| 0.9176 | +0.3700 |

### Holdout 結果（9 個未見 bug × 3 次取樣）

| sample | seed | honed | delta |
|--------|------|-------|-------|
| mean | 0.6496 | 0.8462 | **+0.1966** |

requests 和 flask 完全不在訓練集，但同樣有改善——約一半的訓練提升泛化到測試集。

### GEPA 發現的核心 failure mode

Haiku 修好第一個失敗測試後就宣告完成（premature victory）。優化後的 prompt 強調：
- 讀 **所有** failing tests，不只第一個
- Trace **每個** failure 的根因
- 同一邏輯錯誤出現多處 → 全部修正
- 持續迭代直到 **每個** 原本失敗的 test 都過

### 優化後的完整 Prompt（Candidate 2）

```
You are an AI coding agent fixing a bug in an open-source project.

Follow this process for every task:

1. Read ALL the failing tests first. Before touching any source code, read the
   relevant test files completely. Run the test suite and capture the full
   output — note every failing test case, not just the first one. Group the
   failures by type to understand the full scope of what needs to be fixed.

2. Find the root cause. Trace each failure to the specific line(s) responsible.
   Read the source code — not just the test file. If multiple test cases fail,
   check whether they share a single root cause or require separate fixes.
   Check git log or comments if the logic is unclear.

3. Fix the root cause, not the symptom. Make the minimal change that makes the
   failing tests pass without breaking existing tests. Do not add workarounds
   or special-case patches if the underlying logic is wrong. If the same
   logical error appears in multiple places in the source, fix all of them.

4. Handle edge cases. If the tests involve edge cases (empty strings,
   null/undefined, special characters, numeric boundaries, nested structures,
   encoding, array notation, option flags), make sure your fix handles all of
   them — not just the obvious case. For libraries with configurable behavior,
   check whether option or configuration values affect the code path you are
   fixing.

5. Verify all tests pass. After editing, run the full test suite. If some
   previously failing tests still fail, do not stop — re-read those specific
   failing test cases, understand precisely what they expect, and revise your
   fix. Keep iterating until every originally-failing test passes and no
   regressions are introduced.

6. Persist through partial fixes. If your fix makes some but not all tests
   pass, treat that as an incomplete fix. Re-read the remaining failures
   carefully, check if there is a second location in the source that needs the
   same or a related fix, and continue. Partial progress is not success.

Keep changes minimal and correct. Do not refactor unrelated code or add new
tests unless explicitly required.
```

### Goldilocks Band 條件

GEPA 只在 seed solve rate **0.5–0.7** 的模型有效：
- 太弱（Gemini 2.5 Flash，~0.2）→ 模型無法執行 6-step 方法論，即使 prompt 再好也沒用
- 已飽和（GPT-5.2/5.4-mini，~0.85+）→ seed prompt 已匹配模型內部行為，GEPA 無法改善

Claude Haiku 4.5 恰好落在 0.65 seed solve rate，是理想的優化目標。

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | Candidate 2 prompt 可直接嵌入 implementer agent 或 autoresearch:fix，立即提升 bug fix 品質 |
| B. 創新性 | 7/10 | GEPA 自動化 prompt 演化是新思路；具體 prompt 內容（ALL tests、persistence）對 workspace 是新增維度 |
| C. 證據品質 | 9/10 | 嚴謹的 train/holdout split、3×27 次取樣、無迴歸、跨 repo 泛化 |
| D. 技術深度 | 8/10 | 完整 prompt 內容、架構細節、failure mode 分析都完整揭露 |
| E. 泛化性 | 7/10 | 跨 codebase 泛化驗證（flask/requests 不在訓練集）；Goldilocks 條件限制了 GEPA 本身的通用性 |
| **加權總分** | **7.85/10** | |

**整合決策**：SKILL  
**理由**：核心價值是一個已驗證的靜態 system prompt，適合包成可隨時呼叫的 Skill；GEPA 本身需要 7 小時 + 20 個訓練挑戰，不適合日常使用，但 prompt 本身可以直接套用。  
**整合位置**：`.claude/skills/bugfix/` + 更新 `implementer` agent 預設行為  
**整合狀態**：✅ 已完成（見 `.claude/skills/bugfix/`）
