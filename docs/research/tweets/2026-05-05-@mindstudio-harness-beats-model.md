---
title: "Harness Beats Model Upgrades: 5 Benchmark Analysis — @MindStudio"
author: "MindStudio Engineering"
date: 2026-05-05
source: "https://www.mindstudio.ai/blog/agent-harnesses-beat-model-upgrades-5-benchmarks"
type: tweet
---

# Harness Beats Model Upgrades: 5 Benchmark Analysis — @MindStudio

**來源**：https://www.mindstudio.ai/blog/agent-harnesses-beat-model-upgrades-5-benchmarks
**作者**：MindStudio Engineering
**發布日期**：2026-05-05（近似）
**收錄日期**：2026-05-10
**類型**：Blog 研究 + 社群傳播推文
**分類**：eval / harness-design

---

## 核心數據

> "GPT-5.5 in native Codex harness: 61.5% SWE-Bench verified. Same model in Cursor harness: 87.2%. That's a 25.7pp swing from harness alone."

---

## 研究摘要

**TL;DR**：5 個 benchmark 的分析證明 harness 工程現在超越模型升級對結果的貢獻。相同模型（GPT-5.5）在不同 harness 中的性能差距達 25.7 pp — 超過一個模型世代的提升。

### 5 Benchmark 結果

| Benchmark | 模型 | Harness A | Harness B | 差距 |
|-----------|------|-----------|-----------|------|
| SWE-Bench | GPT-5.5 | Codex 61.5% | Cursor 87.2% | +25.7 pp |
| Terminal-Bench 2 | Claude Sonnet | Base 64.2% | AHE-evolved 77.0% | +12.8 pp |
| HotpotQA | Claude Opus | Solo 31.7% | 3-agent 74.3% | +42.6 pp |
| MATH | Haiku 4.5 | No scaffold 52.1% | CoT+tools 78.4% | +26.3 pp |
| WebArena | GPT-5 | Default 42.8% | Optimized 61.7% | +18.9 pp |

### 關鍵結論

1. **Harness 影響 > 模型升級影響**：25.7 pp 差距超過 GPT-4 → GPT-5 的提升（~20 pp）
2. **最小 harness 提升**：即使最保守的 harness 優化也帶來 12+ pp 提升
3. **飽和閾值**：在已有強 harness 的基準上（AHE-evolved），模型升級仍有 8-15 pp 效果

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| 相關性 | 9/10 | 直接量化 harness engineering 的 ROI vs 模型升級 |
| 可行動性 | 9/10 | 明確指向「先優化 harness 再考慮升級模型」 |
| 新穎性 | 8/10 | 量化比較首次跨 5 benchmarks 系統呈現 |
| **總評** | **8.7/10** | — |

---

## 對 cc-workspace 的意涵

1. **Model selection 決策**：先問「harness 有沒有優化？」再問「要升級到哪個模型？」
2. **ROI 計算**：harness 改善的 ROI > 模型升級的 ROI（25.7 pp vs ~20 pp，且 harness 成本低）
3. **Subagent 策略驗證**：HotpotQA 的 74.3% vs 31.7% 直接驗證 PGE 多代理設計的價值

**相關**：`subagent-strategy.md` §45% 規則（single-agent baseline < 45% 時多代理效果最大）
