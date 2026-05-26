# Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers

**ArXiv**: 2603.07670 | **Date**: 2026-03-08 | **Author**: Pengfei Du | **Category**: cs.AI

## 摘要

全面綜述 LLM 自主 agent 中記憶系統的設計、實作與評估方法，涵蓋 2022 至 2026 年初的研究。核心觀點：「單一 context window 遠不足以捕捉長期互動中發生的一切」，記憶是將無狀態文字生成器轉變為真正自適應系統的關鍵。

## 核心貢獻

### 形式框架：Write–Manage–Read 循環

論文引入將 agent 記憶概念化為「write–manage–read 循環」的形式框架，整合感知與行動系統。

### 三維分類法

記憶系統依三個維度分類：
- **時間範疇**（Temporal scope）：短期 vs 長期
- **表示基底**（Representational substrate）：向量、圖、語言、代碼
- **控制策略**（Control policy）：靜態、動態、學習型

### 五大機制族群

| 機制 | 描述 |
|------|------|
| Context-resident compression | 在有限 token 窗口內壓縮資訊 |
| Retrieval-augmented stores | 外部知識庫選擇性召回 |
| Reflective self-improvement | 從過去經驗中學習改進 |
| Hierarchical virtual context | 結構化階層組織資訊 |
| Policy-learned management | AI 驅動的記憶保留/丟棄決策 |

## 主要發現

- **評估轉向**：從靜態回憶基準轉向多 session 測試（交織記憶與決策）
- **4 個基準分析**：揭示現有系統的持續差距
- **5 個應用領域**：個人助理、代碼 agent、開放世界遊戲、科學推理、多 agent 協作
- **5 大開放挑戰**：持續鞏固、因果接地檢索、可信反思、學習遺忘、多模態具身記憶

## 工程實踐考量

涵蓋：write-path filtering、衝突解決、延遲約束、隱私治理。

## 與現有研究的關係

| 對比論文 | 差異 |
|---------|------|
| `2024-04-21-survey-memory-mechanism-llm-agents` | 本文聚焦機制族群分類，前者聚焦評估標準碎片化 |
| `2025-04-22-human-memory-to-ai-memory-survey` | 本文覆蓋更寬廣，前者從人類記憶視角切入 |

## 分類

**Memory Architecture** — 2026 年最全面的記憶機制綜述，write–manage–read 形式框架為設計新系統提供基礎。
