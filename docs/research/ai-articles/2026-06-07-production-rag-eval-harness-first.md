---
title: "Claude Code Production RAG Case Study: 11天、68% AI鍵入率、Eval Harness First"
author: "futureproofing.dev"
date: 2026-06-07
source: "https://www.futureproofing.dev/blog/claude-code-production-rag-case-study"
tags: [claude-code, rag, eval-harness, production, case-study, langchain, pinecone, hipaa]
topic: "11 天 production RAG，eval harness first，68% keystrokes AI，拒絕 AI 建議的具體場景"
---

# Production RAG Case Study: 11 天、Eval Harness First 紀律

一位工程師使用 Claude Code Max（20x tier）在 11 個日曆天（約 70 工時）完成一套生產級 RAG 醫療系統，47 個 PR、87% eval 通過率（目標 80%）。

## 技術堆疊

Next.js + LangChain + Pinecone + OpenAI embeddings（text-embedding-3-large）+ Claude Sonnet 4.6

## Eval Harness First 策略

**最關鍵決策**：在寫任何 pipeline 代碼之前，先建立評估框架。

- Days 1–2：建立含 50 個精選測試案例（臨床情境 + 評分邏輯）的 eval harness
- AI 輔助率：71%（配置和樣板代碼密集階段）
- 工程師可要求「再給我 10 個類似測試案例但帶 X 變體」並在數秒內收到可用 diff

此紀律的價值：integration tests 在後期捕捉到了 Unicode regex 失敗和 JSON parsing edge case——這些問題若未被攔截會進入生產環境。

## 11 天時間軸與 AI 輔助率

| 天數 | 工作內容 | PRs | AI 輔助率 |
|------|---------|-----|----------|
| Days 1–2 | Eval harness 搭建 | 1–7 | 71% |
| Days 3–5 | Embedding + chunking 優化 | 8–22 | 64% |
| Days 6–8 | Retrieval ranker + citation + HIPAA logging | 23–35 | 58% |
| Days 9–10 | End-to-end eval + 失敗分析 | 36–43 | 81% |
| Day 11 | Production deploy（feature flag） | 44–47 | 65% |

加權平均 AI 輔助率：**68% 的鍵入**。PR velocity 較工程師的個人基線提升 **2.3x**。

## Embedding 演進過程

- OpenAI ada-002：eval 62%
- text-embedding-3-large + 固定 chunk：71%
- text-embedding-3-large + 250-token chunks + section-aware splitting：**84%**

## 三次拒絕 AI 建議的具體場景

**第一次拒絕（Days 3–5）**：AI 建議固定大小 chunking。工程師以領域知識判斷臨床指南必須遵循自然章節邊界——固定 chunk 會破壞語意完整性。

**第二次拒絕（Days 6–8）**：AI 建議使用 LangChain 內建 citation module。工程師自行撰寫 60 行的 citation tracker，原因：LangChain 抽象層過重，且未保留 line-level span 數據（HIPAA 合規所需）。

**第三次拒絕（Day 11）**：AI 建議 10% 使用者 rollout。工程師選擇先給 5 位內部醫師顧問，24 小時內發現 PHI scrubbing edge case。

約 **20% 的 AI 建議被拒絕**，尤其是領域知識與標準 pattern 衝突、解法過度抽象、或 eval 通過但隱藏微妙 bug 時。

## 核心教訓

> "68% of keystrokes had AI involvement. The engineer's judgment determined ~95% of architectural calls. Those are different things."

Days 1–2 僅 API 費用就消耗約 $320（20x tier），但這是在大量生成測試 fixtures 的高密度使用階段。

## Key Insights
- Eval harness first 是唯一讓「AI 輔助」安全的方式——沒有 eval，快速生成的代碼無法判斷是否正確
- AI 輔助率在「機械性調試」（81%）遠高於「架構決策」（58%）——這個分佈是健康的
- 拒絕 AI 建議的場景有共同特徵：過度抽象、缺失領域知識、eval 通過但業務邏輯錯誤
- HIPAA 合規場景中自行實作優於使用第三方抽象層（line-level span 追蹤是關鍵）

## Code Examples / Commands

```python
# Embedding 最終配置
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=25,
    separators=["\n## ", "\n### ", "\n\n", "\n"]  # section-aware
)

# 自製 citation tracker（60 行，非 LangChain 內建）
class CitationTracker:
    def track(self, chunk_id: str, span_start: int, span_end: int, text: str):
        # 保留 line-level span for HIPAA audit trail
        ...
```

```bash
# Eval 執行
python eval_harness.py --test-suite clinical_scenarios_50.json
# Final: 87/100 passed (target: 80)
```
