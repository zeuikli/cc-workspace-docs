---
url: "https://x.com/ArtificialAnlys/status/2065328920514515037"
title: "DeepSWE replaces SWE-Bench Pro: Claude Code + Fable 5 leads at 77"
author: "Artificial Analysis"
archived: 2026-06-18
category: anthropic-news
handle: "@ArtificialAnlys"
published: 2026-06-12
score: 7.0
stats: 1943❤ · 185 retweets
tags: [deepswe, benchmark, claude-code, fable5, harness-quality, evaluation]
type: tweet-thread
---

# DeepSWE replaces SWE-Bench Pro: Claude Code + Fable 5 leads at 77 — @ArtificialAnlys

**來源**：https://x.com/ArtificialAnlys/status/2065328920514515037
**類別**：anthropic-news
**統計**：1943❤ · 185 retweets

---

## 全文

We've updated the Artificial Analysis Coding Agent Index, replacing SWE-Bench Pro with Datacurve's DeepSWE benchmark - the swap lifts Codex with GPT-5.5 (xhigh) above Claude Code with Opus 4.8 (max), while the newly released Claude Fable 5 (max) in Claude Code debuts at the top

DeepSWE, built by @datacurve, writes its tasks from scratch rather than adapting them from public GitHub issues or pull requests, so no model has seen the solutions during training. That matters because SWE-Bench Pro, the benchmark it replaces in our Coding Agent Index, had grown gameable, with some models recovering the fix from the repository's commit history instead of solving the task.

The swap reorders the index: Codex with GPT-5.5 (xhigh) rises from 65 to 76, overtaking Claude Code with Opus 4.8 (max) at 73. Claude Code with Fable 5 (max), which enters directly on the refreshed index, leads at 77. SWE-Bench Pro had been flattering some combinations and penalizing others.

More below.

---

## 評分

| 維度 | 分數 | 說明 |
|------|------|------|
| A. Workspace 可行動性 (30%) | 7/10 | 直接影響 Claude Code 模型選型（Fable 5=77>Opus 4.8=73），harness quality 成獨立決策維度 |
| B. 創新性 (20%) | 8/10 | 引入 harness quality 作為評測第一變數，打破「模型能力=系統能力」的錯誤假設 |
| C. 證據品質 (20%) | 6/10 | 具體分數（77/76/73）、SWE-Bench Pro gameable 的技術解釋，推文上限 6 |
| D. 技術深度 (15%) | 7/10 | 解釋 DeepSWE 為何不可 game（任務從零生成）、why harness quality matters |
| E. 泛化性 (15%) | 7/10 | 評測方法論的普遍影響：「系統評測」vs「模型評測」的認知轉移 |
| **加權總分** | **7.0/10** | 7×0.3+8×0.2+6×0.2+7×0.15+7×0.15 |

**整合決策**：Rule（model-selection-grid 更新，待人工審核）
**理由**：DeepSWE 分數（Fable 5=77, Opus 4.8=73）應更新 .claude/refs/model-selection-grid.md，已在 EVOLUTION-QUEUE 中建立提案
