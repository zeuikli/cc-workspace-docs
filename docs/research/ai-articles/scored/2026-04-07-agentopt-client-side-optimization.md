---
url: "https://arxiv.org/abs/2604.06296"
title: "AgentOpt v0.1: Client-Side Optimization for LLM-Based Agents"
date: 2026-04-07
type: article
---

# AgentOpt v0.1: Client-Side Optimization for LLM-Based Agents

**原始來源**：https://arxiv.org/abs/2604.06296  
**作者**：Wenyue Hua 等 7 位  
**發表日期**：2026-04-07（v1），2026-04-15（v2）  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 核心命題

在多步驟 Agent pipeline 中，**模型組合的選擇比個別模型能力更重要**。強模型不一定是每個角色的最佳選擇；錯誤的組合可能同時浪費成本又損害品質。

**框架定位**：Client-side 優化 — 在不修改 Agent 程式碼的情況下，透過攔截 httpx 傳輸層（patching `httpx.Client.send()`），系統性地找到最佳模型組合。

### 標題結論：最強模型當 Planner 反而最差

在 HotpotQA（多跳問答）測試：

| 組合 | 準確率 |
|------|-------|
| Claude Opus 4.6（規劃者 + 求解者） | **31.71%** |
| Ministral 3 8B（規劃者）+ Claude Opus 4.6（求解者） | **74.27%** |

**原因**：Claude Opus 4.6 作為規劃者時，傾向「自己全部做完」，**繞過下游求解者**——讓強模型餓死了 pipeline。

**推論**：
- 強 ≠ 在每個角色最佳
- 懂得委派的弱規劃者 > 什麼都做的強規劃者
- 與 cc-workspace 的「parent 協調 + sub-agent 執行」架構一致

### 成本差距量化

> 「在相同準確率下，最佳與最差模型組合的成本差距達 **13× 到 32×**。」

這代表：在相同品質下，選擇正確的模型組合可以節省 93-97% 的成本。

### 搜索算法（10 種，v2）

| 算法 | 類型 |
|------|------|
| **UCB-E（v2 最佳）** | Bandit（+ Low-Rank Factorization 變體）|
| **Arm Elimination（v1 最佳）** | Bandit（逐步淘汰 UCB 低於領先者的組合）|
| Epsilon-LUCB | Bandit |
| Threshold Successive Elimination | Bandit |
| Bayesian Optimization | BO |
| Hill Climbing | 局部搜索 |
| LM Proposal | LM 驅動（用 LLM 建議候選組合）|
| Brute-force | 基準（評估所有組合）|
| Random search | 基準 |

**結果**：UCB-E 在相近準確率下，比 brute-force 減少 **62-76%** 的評估預算（v2）。

### 四個 Benchmark

| Benchmark | 領域 |
|-----------|------|
| HotpotQA | 多跳問答 |
| GPQA Diamond | 研究所程度科學問答 |
| MathQA | 數學推理 |
| BFCL v3 | 函式呼叫（工具使用）|

### 與 LLM Routing 的差異

| LLM Routing | AgentOpt（Pipeline 優化）|
|-------------|------------------------|
| 每個 query 的決策 | Pipeline 層級優化 |
| 單次 LLM 呼叫 | 多階段 pipeline，**各階段賦值相互耦合** |
| 無耦合 | 下游依賴上游輸出品質 |

### 對 Workspace 的直接映射

AgentOpt 的 pipeline 角色對應到 cc-workspace：

| AgentOpt 角色 | Workspace 映射 |
|--------------|---------------|
| Planner | Parent Claude Code session（協調者）|
| Solver/Executor | sub-agent（`haiku-implementer`、`implementer`）|
| Critic/Reviewer | `reviewer`、`security-reviewer`、`/deep-review`|

**關鍵洞見**：AgentOpt 實驗發現「弱規劃者 + 強求解者」優於「強規劃者獨大」，正是 cc-workspace 的 haiku-pilot 設計哲學的實驗驗證。

### 對 Workspace 的啟示

1. **量化驗證 haiku-first 策略**：13-32× 成本差距表示正確的小模型放置節省大量成本，且不損品質
2. **「Opus 做規劃者反而最差」是反直覺警告**：強模型作為 orchestrator 時，可能反而降低 sub-agent 使用率
3. **A/B 測試模型組合**：對重複性任務類型，應建立 eval set 測試 Haiku/Sonnet/Opus 組合，用 Arm Elimination / UCB-E 找最佳組合
4. **效果測量先於假設**：最佳組合往往違反直覺，必須實測而非假設

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 直接驗證 Haiku-first 架構；13-32× 成本差距是給 subagent-strategy.md 的實證基礎 |
| B. 創新性 | 9/10 | 「強模型當 planner 反而最差」是反直覺的重要發現；pipeline-level 優化框架本身是新穎貢獻 |
| C. 證據品質 | 9/10 | 四個 benchmark，10 種算法比較，具體數字（31.71% vs 74.27%，13-32× 成本差距）均可重現 |
| D. 技術深度 | 8/10 | Bandit 算法理論、httpx 攔截機制、Pareto frontier 輸出均有具體實作說明 |
| E. 泛化性 | 8/10 | 四個不同領域的 benchmark 驗證，框架設計為模型無關 |
| **加權總分** | **8.70/10** | 9×0.3 + 9×0.2 + 9×0.2 + 8×0.15 + 8×0.15 = 2.7+1.8+1.8+1.2+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/rules/subagent-strategy.md` 和 `.claude/refs/model-selection-grid.md`  
**整合狀態**：待實作（`.claude/skills/prompt-token-optimization/` 已引用 13-32× 數字）

**TODO**：
- 在 subagent-strategy.md 加入 AgentOpt 的實驗結論作為「為什麼 parent 應保持輕量」的量化理由
- 在 model-selection-grid.md 加入「強模型當 orchestrator 的反直覺風險」的警告
- 考慮設計一個小型 A/B 測試框架，讓常見任務類型的模型選擇可以用數據驗證
