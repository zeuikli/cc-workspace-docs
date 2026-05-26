# Harness 評估指標化：基準與測量框架（2025-2026）

> 建立日期：2026-05-08
> 研究方法：autoresearch + web search
> 關聯論文：`../papers/2026-04-23-harness-engineering-language-agents-car.md`

---

## 核心命題

Harness 改進通常**優於模型升級**，但業界缺乏標準化的 harness 評估指標。
本文彙整當前最重要的基準和評估框架。

---

## 1. 關鍵數據：Harness > 模型升級

**來源：** https://www.mindstudio.ai/blog/agent-harnesses-beat-model-upgrades-5-benchmarks

### Endor Labs 功能性基準

> 數據來源：MindStudio 文章引用 Endor Labs 基準測試（2026）
> ⚠️ "GPT-5.5" 為 Endor Labs 報告中使用的命名（非 OpenAI 官方型號名稱），可能是內部測試版本或報告筆誤；實際性能對應已知公開模型。

| 模型（per Endor Labs）| Harness 環境 | 功能性評分 |
|----------------------|-------------|-----------|
| GPT-5.5 [secondary] | OpenAI Codex | 61.5% |
| GPT-5.5 [secondary] | **Cursor** | **87.2%** |
| Claude Opus 4.7 | Native Claude Code | 87.2% |
| Claude Opus 4.7 | Cursor | 91.1% |

**GPT-5.5 跨 harness 差異：+25.7 pp（零模型改動）**

→ 對低能力模型，harness 選擇的影響**遠大於模型版本**。

### 歷史佐證：TerminalBench-1 LangChain 案例

換 harness 後 LangChain 從排名 #30 → #5（同一模型）

---

## 2. Terminal-Bench（tbench.ai）

**來源：** https://arxiv.org/abs/2601.11868  |  https://www.tbench.ai/

### 設計

- 評估 LLM-based agents 在命令列界面（CLI）的能力
- 任務：複雜、真實場景的終端機操作
- 評估方式：binary pass/fail，aggregate = pass rate

### TerminalBench-2 當前排行榜

基準提供公開競爭環境；任何人可提交 harness 測試。

---

## 3. Meta-Harness（End-to-End 自動優化）

**來源：** https://yoonholee.com/meta-harness/

### 設計理念

Meta-Harness 是「Harness 的 Harness」——用 LLM（Claude Code）閱讀每個任務的執行 trace，**自動診斷失敗模式並提出修正**。

優化對象：
- System prompts
- Tool definitions
- Completion-checking logic
- Context management

### 量化結果

| 任務域 | 基準 | Meta-Harness | 提升 |
|--------|------|--------------|------|
| Text Classification（ACE）| 40.9% | 48.6% | +7.7 pp |
| Text Classification（LawBench）| 29.0% | 45.0% | **+16 pp** |
| Text Classification（Symptom2Disease）| 77.8% | 86.8% | +9 pp |
| Math Reasoning（IMO-level）| 34.1% | 38.8% | +4.7 pp avg |
| Agentic Coding（TerminalBench-2, Opus 4.6）| 74.7% | 76.4% | +1.7 pp |
| Agentic Coding（TerminalBench-2, Haiku 4.5）| 35.5% | **37.6%** | +2.1 pp (#1 overall) |

### 效率對比

| 指標 | Meta-Harness vs ACE |
|------|---------------------|
| Context tokens | 4x 更少 |
| Evaluations 次數 | 10x 更少 |

---

## 4. SkillsBench（Harness 效果隔離評估）

**來源：** https://arxiv.org/pdf/2602.12670

### 設計

評估商業 harness 和基於 Terminal-Bench 的模型無關 harness，
**分離模型效果和 harness 效果**。

→ 填補了「harness 貢獻 vs 模型貢獻」量化分解的空白。

---

## 5. HAL（Holistic Agent Leaderboard）

**來源：** https://github.com/princeton-pli/hal-harness

Princeton PLI 主導的集中式、可重現的代理評估排行榜。
提供跨 benchmark 的標準化比較框架。

---

## 6. HarnessCard（提案標準，CAR 論文）

**來源：** `../papers/2026-04-23-harness-engineering-language-agents-car.md`

### 狀態：仍為提案

CAR 論文（Control/Agency/Runtime）提出 HarnessCard 作為標準化的 harness 文件格式，
類似 ModelCard 的概念，但**尚未被工業界廣泛採用**。

### HarnessCard 應包含的維度

1. Control 層：任務分解方式、循環控制邏輯
2. Agency 層：工具存取範圍、委派深度
3. Runtime 層：context 管理策略、狀態持久化機制

---

## 7. 評估框架選擇矩陣

| 需求 | 推薦基準/框架 |
|------|-------------|
| 測量 harness 絕對性能 | TerminalBench-2 |
| 自動優化現有 harness | Meta-Harness |
| 分離模型 vs harness 貢獻 | SkillsBench |
| 跨任務域統一評估 | HAL |
| 標準化 harness 文件 | HarnessCard（提案中）|

---

## 8. 待補充空白

- [ ] 中文/非英文任務的 harness 評估數據
- [ ] 長時間運行（> 24h）的 harness 穩定性指標
- [ ] 安全性 / 權限模型的 harness 評估維度
- [ ] HarnessCard 標準的工業採用進展（2026 Q2 後）

---

## 引用來源

- [Agent Harnesses Beat Model Upgrades (MindStudio)](https://www.mindstudio.ai/blog/agent-harnesses-beat-model-upgrades-5-benchmarks)
- [Terminal-Bench (arxiv 2601.11868)](https://arxiv.org/abs/2601.11868)
- [TerminalBench-2 Leaderboard](https://llm-stats.com/benchmarks/terminal-bench)
- [Meta-Harness](https://yoonholee.com/meta-harness/)
- [SkillsBench (arxiv 2602.12670)](https://arxiv.org/pdf/2602.12670)
- [HAL Harness (Princeton)](https://github.com/princeton-pli/hal-harness)
- [TerminalBench-2 (Emergent Mind)](https://www.emergentmind.com/topics/terminalbench-2)
