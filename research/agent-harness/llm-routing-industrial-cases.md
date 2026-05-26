# LLM 路由演算法：工業案例與量化數據

> 建立日期：2026-05-08
> 研究方法：autoresearch + web search（基於 AgentOpt 論文延伸）
> 關聯論文：`../papers/2026-04-07-agentopt-client-side-optimization.md`

---

## 核心命題

AgentOpt（arxiv 2604.06296）證明「弱規劃器 + 強求解器」優於單一強模型（31.71% → 74.27%）。
本文追蹤**工業界如何實作此概念**，以及除 UCB-E 外的路由演算法實際部署情況。

---

## 1. RouteLLM（LMSYS, ICLR 2025）

**來源：** https://arxiv.org/abs/2406.18665

### 核心設計

以偏好數據（Chatbot Arena）訓練的**輕量路由器**，對每個 query 判斷是否需要強模型（GPT-4）或可用弱模型（Mixtral 8x7B）。

### 量化結果（三個數字的分母不同，需區分）

| 路由器類型 | 達成 GPT-4 95% 性能所需 GPT-4 呼叫比例 | 相較隨機基準成本節省 |
|-----------|-------------------------------------|------------------|
| Matrix Factorization（Arena 數據）| 26% | ~48% |
| Matrix Factorization（+LLM judge 增強）| **14%** | **75%** |
| Causal LLM（MMLU，augmented）| 54% | 14% |

> ⚠️ 數字說明（防混淆）：
> - **14% GPT-4 呼叫**：衡量路由器將多少 query 送至強模型（越低越好）
> - **75% cheaper than random baseline**：以「所有 query 隨機分配」作分母
> - **「85% cost reduction」**（部分部落格引用）：以「所有 query 送 GPT-4」作分母；這是二手來源的綜合數字，原始論文表述為「over 85%」on MT Bench
> - 三者描述同一個路由器，但起點不同，**不可互換引用**

**相較商業路由器（Chatbot Arena 商業方案）：** 相同性能，**便宜 40%+**

### 遷移學習特性

路由器在**強/弱模型改變時仍維持性能**，無需重新訓練。
→ 意涵：訓練一次可跨模型版本使用。

---

## 2. Martian（商業路由器，2023–2026）

**來源：** https://techcrunch.com/2023/11/15/martians-tool-automatically-switches-between-llms-to-reduce-costs/

### 概況

- 首個商業 LLM 路由器（2023 年 11 月公開）
- 資金：$9M（NEA、General Catalyst、CVP、Prosus Ventures）
- 2024 年 9 月：Accenture 投資並採用（企業級部署）
- 客戶規模：300+ 公司（Amazon 到 Zapier）

### 技術特點

Query-by-query 動態模型選擇；**專利申請中**的路由技術
2025 年新增：AI 模型合規功能（Model Compliance Layer）

### 限制

公開量化數字稀少，商業定價不透明。

---

## 3. RouterBench（Martian 研究，ICLR 2024）

**來源：** https://github.com/withmartian/routerbench

多 LLM 路由系統標準化評估基準，由 Martian 維護。
→ 對比 RouteLLM 偏學術，RouterBench 偏工業標準化。

---

## 4. RouterArena（開放評估平台）

**來源：** https://arxiv.org/html/2510.00202v1

類 Chatbot Arena 設計，專門比較不同 LLM 路由器的端到端性能。

---

## 5. 工業界主流路由模式（2025-2026）

### 5.1 Requesty（企業 LLM 路由）
- 側重：上線時間、成本效率、模型選擇
- 模式：Intelligent routing + fallback chains

### 5.2 OpenRouter
- 統一 API，自動根據可用性和延遲路由
- 功能：provider 切換、fallback、速率限制管理

### 5.3 總結矩陣

| 路由器 | 類型 | 強項 | 已知弱點 |
|--------|------|------|---------|
| RouteLLM | 開源 | 學術驗證、可遷移 | 需要偏好訓練數據 |
| Martian | 商業 | 企業合規、scale | 成本不透明 |
| RouterArena | 評估平台 | 標準化比較 | 不是路由工具本身 |
| OpenRouter | API 層 | 高可用性 | 不做 query 層路由 |

---

## 6. AgentOpt 限制與批評

### 何時 Strong Planner > Weak Planner

基於 2025-2026 文獻，以下場景弱規劃器失效：

| 場景 | 原因 |
|------|------|
| 順序推理任務 | 計劃錯誤無法被求解器修正 |
| 需要全局一致性的複雜邏輯 | 弱規劃器缺乏跨步驟視野 |
| 極短 query（<50 tokens）| 分派開銷超過效益 |
| Domain-specific 高精度任務 | 弱模型在 domain 外泛化差 |

### 多代理研究的平行發現（DeepMind 2025）

- 4 agents 以上出現「coordination tax」（性能增益飽和）
- **45% 規則**：當 single-agent baseline < 45% 時多代理最有效
- 當 single-agent > 80%：增加代理**引入噪音而非價值**

---

## 知識空白（待後續研究）

- [ ] RouterBench 具體評分方法與標準化程度
- [ ] RouteLLM 在非英文任務上的路由準確率
- [ ] Martian 路由的具體算法機制（專利保護）
- [ ] Query 複雜度如何量化（現有方法：embedding similarity、token length、few-shot performance）

---

## 引用來源

- [RouteLLM Paper (arxiv 2406.18665)](https://arxiv.org/abs/2406.18665)
- [RouteLLM LMSYS Blog](https://www.lmsys.org/blog/2024-07-01-routellm/)
- [Martian TechCrunch](https://techcrunch.com/2023/11/15/martians-tool-automatically-switches-between-llms-to-reduce-costs/)
- [Accenture × Martian](https://newsroom.accenture.com/news/2024/accenture-invests-in-martian-to-bring-dynamic-routing-of-large-language-queries-and-more-effective-ai-systems-to-clients)
- [RouterArena](https://arxiv.org/html/2510.00202v1)
- [RouterBench GitHub](https://github.com/withmartian/routerbench)
- [Intelligent LLM Routing 85% cost](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)
