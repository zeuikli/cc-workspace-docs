---
url: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/
date: 2026-05-06
source: Simon Willison's Weblog
authors: Simon Willison
tags: [vibe-coding, code-review, agentic-engineering, productivity, review-culture]
---

# Vibe Coding and Agentic Engineering Are Getting Closer Than I'd Like

**原始來源**：https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/  
**作者**：Simon Willison  
**歸檔日期**：2026-05-10

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | Code review 文化轉向建議可行動 |
| B. 創新性 | 6/10 | 觀察性文章，非新方法論 |
| C. 證據品質 | 5/10 | 個人觀察為主，無實驗數據 |
| D. 技術深度 | 5/10 | 概念層次，無實作細節 |
| E. 泛化性 | 8/10 | 跨團隊適用 |
| **加權總分** | **6.35/10** | 7×0.3 + 6×0.2 + 5×0.2 + 5×0.15 + 8×0.15 = 6.35 |

**整合決策**：存入 scored（分數 > 6）；不直接整合規則（觀察性，非處方性）  
**整合位置**：作為 code review culture shift 的參考文獻  
**整合狀態**：已歸檔，不整合

---

## TL;DR

「Vibe coding」（不看 AI 輸出直接接受）和「agentic engineering」（負責任的 agent 驅動開發）之間的界線正在模糊。生產力提升（200→2,000 行/天）讓傳統 code review 不實際，迫使評估標準移至設計決策和真實世界驗證，而非工件審查。

---

## 核心觀察

### 1. 生產力 vs 可審計性的張力

```
生產力提升：200 行/天 → 2,000 行/天（10x）
Code review 速度：沒有提升（人還是那個人）
結果：review backlog 爆炸 → review 品質下降 → 實質上是 vibe coding
```

### 2. 評估上移（Upstream Evaluation）

解決方案不是「更快 review 程式碼」，而是「評估的上移」：
- **設計評估**：在 implementation 前評估架構決策
- **真實驗證**：部署後看行為，而非靠 code review 推斷行為
- **Harness 評估**：評估 harness 約束是否足夠，而非 review 每行 code

### 3. 對 harness 的啟示

> "If you can't review AI-generated code line by line, you need a harness strong enough to prevent bad code from reaching production."

Vibe coding 的興起是「我們需要更強 harness」的另一個論點。

---

## 對 cc-workspace 的映射

| 觀察 | cc-workspace 對應 |
|-----|----------------|
| 評估上移 | `plan-mode-expert` 設計前評估 |
| 真實驗證 > code review | `healthcheck.sh` + 整合測試 |
| Harness 約束替代 review | PreToolUse hooks + permission model |

**關聯**：Datadog Harness-First 文章（2026-03-09）提供了此觀察的系統化解決方案。

---

## 與 Karpathy 的連結

Karpathy「context engineering」（2025-06）+ Willison「評估上移」（2026-05）→ 共同方向：  
**品質保證的重心從「輸出審查」移向「輸入工程（context + harness）」**。
