---
title: "AI Code Review Gets Better When Models Debate"
author: "Li Liu"
date: 2026-02-26
source: "https://milvus.io/blog/ai-code-review-gets-better-when-models-debate-claude-vs-gemini-vs-codex-vs-qwen-vs-minimax.md"
tags: [claude-code, code-review, multi-model, adversarial-debate, bug-detection, Milvus]
topic: orchestration
---

# AI Code Review Gets Better When Models Debate

Li Liu 對 15 個含已知 production bug 的 Milvus PR，測試單模型 vs. 五模型對抗辯論的 bug 偵測率。單模型最佳（Claude Opus）偵測 53%，五模型辯論達到 80%。實驗工具 Magpie 與 AI-CodeReview-Arena 已開源。

## 實驗設計

**對象**：15 個 Milvus（開源向量資料庫）的真實 PR，均含已知 production bugs

**五個模型**：Claude、Gemini、Codex、Qwen、MiniMax

**兩種模式**：
- **Raw mode**：只給 PR diff
- **R1 mode**：透過 Magpie 預先提供背景 context

**Bug 難度分類**：
- **L1**：只看 diff 即可發現（所有模型 100%）
- **L2**：需理解周邊程式碼（10 個案例）
- **L3**：需系統級推理（5 個案例）

## 單模型表現（L2+L3 合計）

| 模型 | Raw mode | R1 mode |
|------|----------|---------|
| **Claude** | **53%（第一）** | 47% ↓ |
| Qwen | 33% | 40% ↑ |
| Codex | 33% | 27% ↓ |
| MiniMax | 27% | 33% ↑ |
| Gemini | 13%（最後）| 33% ↑ |

Claude 在 raw mode 主導：L3（系統級）bugs 完美偵測率，Gemini 需要 context 才能顯著改善。

## 五模型辯論機制

五輪對抗辯論：
- **Round 1**：各自獨立審查
- **Rounds 2-5**：審查對方發現並更新立場
- 所有主張**必須引用具體程式碼行**作為證據

## 辯論結果

| 指標 | 單模型最佳（Claude） | 五模型辯論 |
|------|---------------------|-----------|
| L2 bug 偵測 | 3/10（30%） | 7/10（70%） |
| L3 bug 偵測 | 5/5（100%） | 5/5（100%） |
| **整體覆蓋** | **53%** | **80%** |

辯論模式將日常 L2 bug 偵測率加倍，代表最常見的實際問題類型。

## 兩模型組合（實務推薦）

**Claude + Gemini** 最強：達到五模型天花板的 91%

| 組合 | 覆蓋率 |
|------|--------|
| Claude + Gemini | 10/15（67%） |
| Claude + Qwen | 9/15（60%） |
| Claude + Codex | 8/15（53%） |
| Claude + MiniMax | 8/15（53%） |

Claude 擅長深度邏輯，Gemini 補足 concurrency 與相容性問題，兩者弱點最小重疊。

## Bug 類型分析

| 類別 | Claude | Gemini | Qwen | Codex | MiniMax |
|------|--------|--------|------|-------|---------|
| Validation gaps | 3/4 | 2/4 | 3/4 | 1/4 | 1/4 |
| Data structure lifecycle | 3/4 | 1/4 | 1/4 | 1/4 | 3/4 |
| Concurrency races | 0/2 | 1/2 | 0/2 | 0/2 | 0/2 |
| Compatibility | 0/2 | 1/2 | 1/2 | 1/2 | 0/2 |
| Deep logic | 1/3 | 0/3 | 1/3 | 1/3 | 1/3 |

有 4 個 bug 所有模型都未偵測到——這些涉及「開發者腦中的假設」而非可偵測的程式碼 pattern。

## Claude 的獨特特質

Claude「公開承認遺漏」（acknowledges misses openly）——在辯論中最具協作性，被對等評分同列第一（與 Qwen 並列 8.6/10）。

## Key Insights
- 15 個 Milvus PR 含已知 bug，五模型五輪對抗辯論：單模型最佳（Claude Opus）53%，五模型辯論達 80%
- Claude+Gemini 組合達到五模型天花板的 91%（10/15）；日常 L2 bugs 從 3/10 提升至 7/10
- Claude「公開承認遺漏」——獨特協作特質；最難的系統級 bugs 在辯論中達 100%（單模型 0/15）

## Code Examples / Commands

```bash
# Magpie — 辯論協調工具（已開源）
# AI-CodeReview-Arena — 完整評估 pipeline
# https://github.com/milvus-io/ai-code-review-arena

# 基本辯論啟動（概念示意）
magpie debate \
  --pr-url https://github.com/milvus-io/milvus/pull/12345 \
  --models claude,gemini,codex,qwen,minimax \
  --rounds 5 \
  --require-citations
```
