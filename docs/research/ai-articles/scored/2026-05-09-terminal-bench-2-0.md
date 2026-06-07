---
url: "https://arxiv.org/html/2601.11868v1"
date: 2026-05-09
source: Terminal-Bench 2.0 / Laude Institute
tags: [benchmark, harness-impact-measurement, leaderboard, model-harness-pairs, evaluation-methodology]
---

# Terminal-Bench 2.0: Benchmarking Agents on Hard, Realistic Tasks

**原始來源**：https://arxiv.org/html/2601.11868v1  
**歸檔日期**：2026-05-09

---

## TL;DR

Terminal-Bench 2.0 是首個大規模 agent benchmark 以「harness + model pair」而非「model only」方式排名。關鍵發現：同一模型在不同 harness（ForgeCode vs Capy）上相差 4.5 個百分點；Stanford IRIS Lab 的自動 harness 演化系統推動同模型達成 76.4%。**Harness 對分數的影響力大於模型世代升級**。

---

## 核心主張

1. **Harness 優於模型作為性能動力**
   - Codex CLI with GPT-5.2 = 62.9%  
   - Claude Opus 4.5 with Terminus 2 = 57.8%  
   - 同一模型配不同 harness 可造成 4.5 百分點差異（> 模型升級的典型增幅）

2. **第三方 Harness 主導排行**
   - ForgeCode（第三方 harness）在 Terminal-Bench 2.0 top 6 佔 3 席
   - 暗示 harness 設計技巧超越模型提供商之專家度
   - Proprietary models 在 top 13 佔絕大多數（開源 Kimi K2 = 35.7%，遠低於 frontier）

3. **評估方法論：Outcome 而非 Process**
   - Tests verify final container state properties；不評估模型的中間命令
   - 32,155 total trials across 6 agent types × 16 frontier models
   - ~3 reviewer-hours per task quality control

4. **飽和信號與 Benchmark 有效期**
   - 結論：「Frontier models resolve less than 65% of tasks」
   - Authors 預警：「potential saturation within one year」→ 需持續發布新難度任務集

---

## 直接意涵

### cc-workspace 可行動性

1. **排行榜設計需納入 harness-model pair 維度**
   - 若 cc-workspace 建立內部 benchmark（如 SWE-bench 自訂子集），排序應展示 (Haiku+current-harness), (Sonnet+current-harness), (Opus+current-harness)
   - 單純比較「Opus vs Sonnet」得分忽略了 harness 的貢獻
   - 推薦在 `.claude/refs/quality.md` 的 benchmark 章節記錄

2. **Harness Iteration 的 ROI > 模型升級**
   - 若當前 benchmark 分數相對較低，先嘗試 harness 改進而非等 Opus 4.8
   - Terminal-Bench 的證據強度：科學評估、多獨立評分員、開源任務集

3. **Benchmark 衰減週期追蹤**
   - Terminal-Bench 預警「飽和於一年內」
   - cc-workspace 若引入自訂 benchmark，應標記「建立日期」+ 「預期衰減日期」
   - 避免在已飽和的 benchmark 上過度投入優化

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | 量化 harness impact，支持優化決策；但無 actionable optimization playbook |
| B. 創新性 | 7/10 | Harness-pair ranking 是新角度；evaluation 方法論本身非突破 |
| C. 證據品質 | 9/10 | 大規模評估（32K trials）、多獨立評分員、開源任務集、可複現 |
| D. 技術深度 | 7/10 | 評估方法清晰；未深入分析為何某 harness 超越其他（機制黑盒） |
| E. 泛化性 | 8/10 | 原則適用所有 terminal/shell agent 工作；結論「harness matter」 universally 有效 |
| **加權總分** | **7.6/10** | 7×0.3 + 7×0.2 + 9×0.2 + 7×0.15 + 8×0.15 = 2.1+1.4+1.8+1.05+1.2 = 7.55 |

**整合決策**：Reference（納入 `.claude/refs/quality.md` 的 benchmark evaluation 小節）

---

## 引用關聯

- 推文 @nicbstme 2026-05-04：Terminal-Bench 2.0 引用（Opus 4.6 ForgeCode 79.8% vs Capy 75.3%）  
- LangChain harness engineering：同模型不同 harness 達成 52.8%→66.5%  
- Cursor blog：Terminal-Bench rank improvement through harness-only changes  

