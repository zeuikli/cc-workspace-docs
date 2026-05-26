# Keep Rate: The Production Quality Metric for AI Agents — @Anthropic

**來源**：https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
**作者**：Anthropic Engineering
**發布日期**：2026-05-08（近似）
**收錄日期**：2026-05-10
**類型**：Anthropic 官方 Engineering Blog + 社群討論
**分類**：eval / harness-design

---

## 核心概念

> "Keep rate measures what fraction of AI agent-generated changes remain in the codebase after a fixed time interval. Unlike pass@1, it captures user acceptance over time — the ultimate signal of whether the harness produces useful output."

---

## 研究摘要

**TL;DR**：Anthropic 提出 **Keep Rate** 作為 AI agent 的生產品質指標。與 lab metric（pass@1、benchmark score）不同，Keep Rate 衡量「使用者實際保留了多少 AI 生成的改動」。Harness 品質最終由 keep rate 反映，而非 LLM 的 task completion 聲稱。

### Keep Rate 的定義

```
Keep Rate (t) = |preserved_changes| / |total_ai_changes| at time t

t = 1 week：短期接受率（用戶未立即 revert）
t = 1 month：中期接受率（改動在 review 後存活）
t = 3 months：長期接受率（改動在生產環境存活）
```

### 三種 Eval 的對比

| Metric | 測量什麼 | 局限性 |
|--------|---------|------|
| pass@1 | Lab task completion | 不代表 production usefulness |
| Benchmark score | Domain capability | 任務分佈 ≠ 實際工作分佈 |
| **Keep Rate** | 用戶真實接受度 | 需要時間（無法即時）|

### 應用意涵

Keep rate 作為 harness feedback loop 的最終評估：
1. Low keep rate → harness 生成的改動不符合用戶意圖
2. High keep rate at day 1, low at day 30 → 短期表面 OK，長期品質差
3. 漸進 keep rate 曲線（t=1d, 1w, 1m, 3m）= harness 品質的時間序列

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| 相關性 | 9/10 | Anthropic 官方 eval 框架，直接影響 harness 評估方式 |
| 可行動性 | 8/10 | Keep rate 可在 git log 中追蹤（改動存活天數）|
| 新穎性 | 9/10 | 從 lab metric 到 production metric 的典範轉移 |
| **總評** | **8.7/10** | — |

---

## 與 cc-workspace 的連結

- 支持 PGE 原則中「Evaluator 用外部工具而非 LLM 自評」的方向
- Keep rate 可加入 `harness-evaluation-metrics-2026.md` 的 metric 清單
- 建議：在 session retros 中追蹤「我接受了 AI 多少比例的改動？」作為近似 keep rate

**Anthropic 對齊**：外部工具評估 > LLM 自評（Rajasekaran 2026 同一立場）
