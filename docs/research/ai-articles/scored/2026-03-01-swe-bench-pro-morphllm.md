---
title: "SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%"
date: 2026-03-01
type: article
---

> Source: https://www.morphllm.com/swe-bench-pro
> Fetched: 2026-05-08

# SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%

Live SWE-Bench Pro rankings with SEAL scores, agent systems, and Verified. The best model scores 46% on Pro but 81% on Verified, because Verified is contaminated. Full leaderboard and analysis.

March 1, 2026 · 2 min read

## Overview

Claude Opus 4.5 achieves markedly different results across benchmarks: "80.9% on SWE-Bench Verified and 45.9% on SWE-Bench Pro." The explanation reveals critical differences in dataset construction and contamination resistance.

## SEAL Leaderboard: SWE-Bench Pro (Standardized Scaffolding)

Scale AI's standardized evaluation uses "identical tooling with a 250-turn limit" to isolate raw model capability. The top-ranked model achieves 45.9%, with the next tier separated by roughly 5 percentage points but statistically indistinguishable due to overlapping confidence intervals.

| Rank | Model | Score | CI |
|------|-------|-------|-----|
| 1 | Claude Opus 4.5 | 45.9% | ±3.60 |
| 2 | Claude Sonnet 4.5 | 43.6% | ±3.60 |
| 3 | Gemini 3 Pro | 43.3% | ±3.60 |

The benchmark spans "1,865 Tasks across 41 repositories" in multiple languages.

## Agent Systems Leaderboard

Custom scaffolding substantially impacts performance. "Three different agent systems ran the same model (Opus 4.5), and their scores ranged from 50.2% to 55.4%." This variance demonstrates that "the scaffolding gap is the most underappreciated finding in this data."

## WarpGrep Impact

Morph's internal benchmarks indicate that incorporating WarpGrep v2 as a search subagent adds approximately 2 percentage points to model performance while reducing costs and latency.

## SWE-Bench Verified Leaderboard (2026)

The older benchmark consists of "500 Python-only tasks from the original SWE-Bench." However, "OpenAI has stopped reporting Verified scores" after discovering that "every frontier model tested could reproduce verbatim gold patches or problem statement specifics."

| Rank | Model | Score |
|------|-------|-------|
| 1 | Claude Opus 4.5 | 80.9% |
| 2 | Claude Opus 4.6 | 80.8% |
| 3 | MiniMax M2.5 | 80.2% |

## SWE-Bench Variants Comparison

| Variant | Tasks | Languages | Top Score | Status |
|---------|-------|-----------|-----------|--------|
| Original (Full) | 2,294 | Python | ~65% | Active |
| Lite | 300 | Python | ~55% | Active |
| Verified | 500 | Python | 80.9% | Contaminated |
| Pro | 1,865 | Py, Go, TS, JS | ~59% | Active (recommended) |

## Pro vs Verified: Key Differences

| Dimension | Verified | Pro |
|-----------|----------|-----|
| Tasks | 500 | 1,865 |
| Repositories | 12 (Python) | 41 (Multi-language) |
| Avg lines changed | 11 | 107.4 |
| Avg files changed | ~1 | 4.1 |
| Contamination resistance | Low | High |

The complexity gap is substantial: "161 of SWE-Bench Verified's 500 tasks require only 1-2 lines of change. Every SWE-Bench Pro task requires at least 10 lines."

## How SWE-Bench Pro Works

The benchmark contains three subsets:

**Public Set (731 tasks):** Tasks from GPL-licensed repositories on HuggingFace

**Commercial Set (276 tasks):** Tasks from proprietary startup codebases, providing contamination resistance

**Held-Out Set (858 tasks):** Reserved for overfitting detection

Each task undergoes three-stage human augmentation including "problem statement creation," "requirements definition," and "interface specification."

## Why Scores Are Lower Than Verified

Four compounding factors explain the dramatic performance drop:

**Multi-File Modifications:** Tasks require "coordinating changes across an average of 4.1 files" rather than single-file edits.

**Longer Time Horizons:** These represent "tasks that would take a professional engineer hours to days."

**Codebase Complexity:** Production systems feature "complex build systems, cross-cutting concerns, and domain-specific conventions."

**Contamination Resistance:** GPL and proprietary licensing prevent models from relying on training data memorization.

Failure analysis identifies three dominant breakdown modes: "semantic understanding failures (35.9% of Opus 4.1 failures), context overflow (35.6% of Sonnet 4 failures), and tool-use inefficiency (42% of smaller model failures)."

## Frequently Asked Questions

**What is SWE-Bench Pro?**

"A software engineering benchmark by Scale AI that evaluates AI coding agents on 1,865 long-horizon tasks from 41 real repositories across Python, Go, TypeScript, and JavaScript."

**What is Claude Opus 4.5's SWE-Bench Pro score?**

On standardized evaluation, "45.9% on the SEAL leaderboard with standardized scaffolding, the highest of any model."

**How does SWE-Bench Pro differ from SWE-Bench Verified?**

Pro offers substantially larger scope with multi-language support and inherent contamination resistance, while Verified's smaller, Python-only dataset has experienced confirmed training data overlap with frontier models.

---

## 繁體中文全文摘要

### 核心命題：46% 為何比 81% 更有意義

Claude Opus 4.5 在兩個 benchmark 上的成績差異揭示了 dataset 構建和污染抵抗力的關鍵差異：

| Benchmark | 成績 | 狀態 |
|-----------|------|------|
| SWE-bench Verified | **80.9%** | ⚠️ 已污染（不可靠）|
| SWE-bench Pro | **45.9%** | ✅ 抗污染（可信）|

OpenAI 已停止報告 Verified 分數，因為「所有測試的前沿模型都能重現逐字金標補丁或問題陳述細節」。

### SEAL Leaderboard：標準化腳手架評分

Scale AI 使用「相同工具和 250 步限制」隔離原始模型能力：

| 排名 | 模型 | 分數 | 信賴區間 |
|------|------|------|---------|
| 1 | Claude Opus 4.5 | 45.9% | ±3.60 |
| 2 | Claude Sonnet 4.5 | 43.6% | ±3.60 |
| 3 | Gemini 3 Pro | 43.3% | ±3.60 |

Top 3 間的差距在統計上無法區分（信賴區間重疊）。

### Scaffolding Gap（腳手架差距）是最被低估的發現

**同一模型（Opus 4.5）在不同 Agent systems 中的成績：50.2% 到 55.4%**（差距 5.2pp）。

這個差異說明：**scaffolding（harness）設計對效能的影響，與模型能力本身一樣重要**。

### Pro vs Verified 的關鍵差異

| 維度 | Verified | Pro |
|------|----------|-----|
| 任務數 | 500 | 1,865 |
| Repo 數 | 12（Python only）| 41（多語言）|
| 平均修改行數 | 11 行 | **107.4 行** |
| 平均修改檔案數 | ~1 | **4.1** |
| 污染抵抗力 | 低 | 高 |

Verified 有 161/500 個任務只需要 1-2 行變更；SWE-bench Pro 的每個任務都至少需要 10 行。

### 為何分數比 Verified 低：四個因素

1. **多檔案修改**：平均需要協調 4.1 個檔案的變更（非單檔編輯）
2. **更長時間跨度**：代表專業工程師需要數小時到數天的任務
3. **代碼庫複雜度**：生產系統有複雜的構建系統、跨切面問題、領域特定慣例
4. **污染抵抗**：GPL 和專有授權防止模型依賴訓練資料記憶

### 三種主要失敗模式

- **語義理解失敗**：35.9%（Opus 4.1 失敗案例）
- **Context overflow**：35.6%（Sonnet 4 失敗案例）
- **工具使用效率低**：42%（較小模型失敗案例）

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 6/10 | Benchmark 選擇建議對模型選型有參考價值；不直接改變 workspace 流程 |
| B. 創新性 | 7/10 | Scaffolding gap（同模型 50.2%→55.4%）是重要且被低估的發現 |
| C. 證據品質 | 9/10 | 詳細 benchmark 數據、污染分析、3 類失敗模式比例均有量化支撐 |
| D. 技術深度 | 7/10 | Pro vs Verified 對比詳細；三子集設計說明清楚 |
| E. 泛化性 | 7/10 | Benchmark 理解和 scaffolding 重要性適用任何 agent 評估場景 |
| **加權總分** | **7.1/10** | 6×0.3+7×0.2+9×0.2+7×0.15+7×0.15 = 1.8+1.4+1.8+1.05+1.05 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/model-selection-grid.md`（benchmark 選擇指南補充）  
**整合狀態**：待實作
