---
title: Agent Harness Engineering — 論文與資源總覽
type: documentation
---

# Agent Harness Engineering — 論文與資源總覽

> 建立時間：2026-05-01  
> 覆蓋範圍：arXiv 論文 · 工程博客 · Benchmark 報告  
> 更新策略：每季補充新論文；Ratchet 新增洞見至 KNOWLEDGE-MAP.md

---

## Priority A — 核心論文（必讀）

### 1. Agentic Harness Engineering: Observability-Driven Automatic Evolution
- **arXiv**: [2604.25850](https://arxiv.org/abs/2604.25850)
- **發表**: 2026-04
- **摘要**: 提出 AHE 框架，透過三個可觀測性柱子（元件 / 經驗 / 決策）自動進化 agent harnesses。核心洞見：harness 改進應由工具、中介軟體、長期記憶主導，而非系統提示詞。
- **關鍵成果**:
  - Terminal-Bench 2: pass@1 69.7% → 77.0%（10 次迭代）
  - SWE-bench-verified: 用 12% 更少 token 達最佳成績
  - 跨模型族遷移收益：+5.1 到 +10.1 pp
- **與 FRAMEWORK.md 的連結**: 直接驗證「harness > model」命題；Ratchet 自動化演進的學術支撐

---

### 2. Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering
- **arXiv**: [2603.05344](https://arxiv.org/abs/2603.05344)
- **發表**: 2026-03
- **摘要**: 首篇系統區分「Scaffolding（組裝期）」vs「Harness（執行期）」概念的論文。介紹 OPENDEV（Rust 終端機代理），強調適應性 context 壓縮、雙代理架構。
- **Scaffolding 定義**: 系統提示、工具定義、subagent 註冊
- **Harness 定義**: 工具分派、context 管理、安全執行、session 持久化
- **架構創新**: 工作負載專門化模型路由、懶惰工具發現、自動化記憶系統

---

### 3. Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures
- **arXiv**: [2604.03515](https://arxiv.org/abs/2604.03515)
- **發表**: 2026-04
- **摘要**: 首次對 13 個開源 coding agents 進行源碼層級架構分析，提出跨 12 維度、3 層組織的統一分類學。
- **5 個通用控制原語**:
  1. ReAct（推理-行動交錯）
  2. Generate-test-repair
  3. Plan-execute
  4. Multi-attempt retry
  5. Tree search
- **關鍵發現**: 11/13 agents 混合多個原語，而非單一模式

---

## Priority B — 重要論文

### 4. Natural-Language Agent Harnesses (NLAH)
- **arXiv**: [2603.25723](https://arxiv.org/abs/2603.25723)
- **發表**: 2026-03
- **摘要**: 提出用自然語言表達 harness 行為，引入 Natural-Language Agent Harnesses (NLAHs) 與 Intelligent Harness Runtime (IHR)。解決 harness「深埋在控制器代碼中」的可移植性問題。
- **核心價值**: 使 harness 設計可跨系統遷移、可對比、可科學研究

---

### 5. Meta-Harness: End-to-End Optimization of Model Harnesses
- **arXiv**: [2603.28052](https://arxiv.org/abs/2603.28052)
- **發表**: 2026-03
- **摘要**: 外層迴圈系統，透過訪問原始代碼、分數和所有先前執行軌跡，用 agent 搜尋 harness 代碼空間。類似 Neural Architecture Search，但針對 harness 層。

---

### 6. ReAct: Synergizing Reasoning and Acting in Language Models
- **arXiv**: [2210.03629](https://arxiv.org/abs/2210.03629)
- **發表**: 2022-10（ICLR 2023）
- **摘要**: LLM agent 的基礎論文。定義推理跡象（reasoning traces）與行動（actions）的交錯模式。推理幫助歸納、追蹤、更新行動計畫；行動與外部環境互動。
- **成果**: HotpotQA 超越 CoT；ALFWorld +34% 絕對成功率

---

### 7. Agent Harness for Large Language Model Agents: A Survey
- **來源**: Preprints.org, 2026-03
- **摘要**: 直指核心：「隨著 agent 任務變長變複雜，執行可靠性越來越不是模型能力問題，而是包裹在它周圍的『基礎設施層』——agent 執行 harness」。

---

### 8. Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers
- **arXiv**: [2603.07670](https://arxiv.org/abs/2603.07670)
- **發表**: 2026-03
- **摘要**: long-running agents 的記憶設計調查。Pattern B（主流）：working memory 在 context window，長期記錄在外部向量/結構化存儲，每步檢索相關記錄。
- **核心挑戰**: 檢索品質是瓶頸
- **相關論文**: A-Mem [2502.12110]、MemGPT [2310.08560]

---

### 9. Agentic Artificial Intelligence: Architectures, Taxonomies, and Evaluation
- **arXiv**: [2601.12560](https://arxiv.org/abs/2601.12560)
- **發表**: 2026-01
- **摘要**: 新一代 LLM agents 作為結合記憶、工具使用、環境反饋的認知控制器。涵蓋 CAMEL、AutoGen、MetaGPT、LangGraph、Swarm 等框架；互動模式有 chain、star、mesh。

---

## Priority C — 工具與方法論論文

### 10. Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use
- **arXiv**: [2602.20426](https://arxiv.org/abs/2602.20426)
- **發表**: 2026-02
- **摘要**: 工具描述的措辭會顯著影響 agent 成功率。提出自動化重寫工具 schema 和描述以提升可靠性。

---

### 11. Act While Thinking: Pattern-Aware Speculative Tool Execution
- **arXiv**: [2603.18897](https://arxiv.org/abs/2603.18897)
- **發表**: 2026-03
- **摘要**: 在 agent 完成思考前並行執行工具，減少延遲。

---

### 12. Design Patterns for Securing LLM Agents against Prompt Injections
- **arXiv**: [2506.08837](https://arxiv.org/abs/2506.08837)
- **發表**: 2025-06
- **摘要**: LLM agent 安全防禦模式，針對提示詞注入等攻擊。

---

### 13. Architecting Resilient LLM Agents: Secure Plan-and-Execute Architectures
- **arXiv**: [2509.08646](https://arxiv.org/abs/2509.08646)
- **發表**: 2025-09

---

## 工程博客資源

### 14. Lilian Weng — LLM Powered Autonomous Agents
- **URL**: https://lilianweng.github.io/posts/2023-06-23-agent/
- **發表**: 2023-06-23
- **定位**: 業界標準入門文章；Planning-Memory-Tools 三層框架的經典定義
- **核心框架**:
  - Planning: Task Decomposition（CoT, ToT）+ Self-Reflection
  - Memory: Sensory / Short-term（context）/ Long-term（向量存儲）
  - Tools: 外部 API 超越訓練數據限制
- **特點**: ReAct 框架的清晰圖解；MIPS 檢索算法（FAISS、ANNOY）說明

---

### 15. Eugene Yan — Patterns for Building LLM-based Systems & Products
- **URL**: https://eugeneyan.com/writing/llm-patterns/
- **定位**: 生產級 LLM 系統的 7 大設計模式
- **7 大 Patterns**: Evals、RAG、Fine-tuning、Caching、Guardrails、Defensive UX、Collect User Feedback
- **Agent Harness 相關洞見**:
  - 「專化模型組隊」勝過單一通才
  - Hybrid 方法（傳統 + embedding）優於單一策略
  - Guardrails + Evals 是生產環境必需品

---

### 16. Adnan Masood — Agent Harness Engineering: The Rise of the AI Control Plane
- **URL**: https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d
- **發表**: 2026-04
- **核心**: 5 層 Control Plane 架構視角
  1. Context Management
  2. Tool/Function Calling
  3. Execution Loop（Observe-Think-Act）
  4. State & Memory
  5. Safety & Observability
- **關鍵統計**: 企業 AI 失敗 65% 源自 harness 層缺陷，而非模型限制
- **獨特觀點**: 正確 cache 管理可將 token 成本降低十倍

---

### 17. Daily Dose of DS — The Anatomy of an Agent Harness
- **URL**: https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness
- **定位**: 最完整的 harness 組件分解（11 個生產級組件）
- **11 個核心組件**:
  1. Orchestration Loop（Thought-Action-Observation）
  2. Tools（schema + 執行 + 驗證 + 結果格式化）
  3. Memory（短期 + 長期）
  4. Context Management（壓縮、masking、即時檢索、子 agent）
  5. Prompt Construction（系統提示 → 工具定義 → 記憶 → 對話）
  6. Output Parsing（結構化物件，避免自由文本）
  7. State Management（類型化字典 + 邊界檢查點）
  8. Error Handling（暫時性/LLM 可恢復/用戶可修正/意外性）
  9. Guardrails & Safety（輸入/輸出/工具層三層）
  10. Verification Loops（規則型/視覺型/LLM-as-judge）
  11. Subagent Orchestration（專門 agent + 完整交接）
- **核心論點**: Verification 能使品質提升 2-3 倍；LangChain 只改 harness 就從外賽區升至第 5 名

---

### 18. LangChain — Agent Engineering: A New Discipline
- **URL**: https://blog.langchain.com/agent-engineering-a-new-discipline/
- **定位**: Agent Engineering 作為工程學科的宣言
- **核心定義**: 「將非確定性 LLM 系統迭代精煉為可靠生產體驗的過程」
- **工程循環**: Build → Test → Ship → Observe → Refine → Repeat
- **跨職能要求**: Product thinking + Engineering + Data Science
- **關鍵轉變**: 放棄「發布前完美」，改為快速發行 + 生產學習

---

## Benchmark 資源

### 19. SWE-bench / SWE-bench Verified / SWE-bench Pro
- **URL**: https://www.swebench.com/
- **規模**: 2,294 issues；Verified 版 500 個（人工 3 倍驗證）
- **評估 Harness 設計**: 最小化 bash-tool-only，Docker 容器化隔離
- **2026 最新成績（SWE-bench Pro）**: Claude Opus 4.7 64.3%、GPT-5.4 57.7%

### 20. Terminal-Bench 2.0
- **URL**: https://www.tbench.ai/leaderboard/terminal-bench/2.0
- **特點**: 終端實務工作（編譯/訓練/部署）；39 個模型排行
- **Harness 洞見**: 同一 Opus 4.6，不同 harness → 13 pp 差距（66.9% → 79.8%）

### 21. AgentBench（ICLR 2024）
- **arXiv**: [2308.03688](https://arxiv.org/abs/2308.03688)
- **特點**: 8 種環境多輪推理評估；29 個模型測試

### 22. WebArena
- **URL**: https://webarena.dev/
- **特點**: 812 個網頁自主操作任務；2 年間成績 14% → 60%

---

## 推薦閱讀順序

### Week 1 — 建立基礎理論
1. ReAct (#6) — 推理-行動交錯基礎
2. Lilian Weng (#14) — Planning-Memory-Tools 三層框架
3. AHE (#1) — 最新 SOTA 與自動演進

### Week 2 — 深入架構設計
4. Scaffolding vs Harness 區分 (#2) — 術語定義
5. Inside the Scaffold Taxonomy (#3) — 12 維度、5 原語
6. Daily Dose of DS Anatomy (#17) — 11 組件生產級分解
7. Adnan Masood Control Plane (#16) — 5 層視角

### Week 3 — 實踐與評估
8. Natural-Language Harnesses (#4) — 可移植性
9. Memory for Agents (#8) — long-running 策略
10. Eugene Yan Patterns (#15) — 生產模式
11. Agent Engineering Discipline (#18) — 工程學科

### Reference — 按需查閱
- SWE-bench / Terminal-Bench（效能基準）
- Security papers (#12, #13)（安全防禦）
- Speculative execution (#11)（效能優化）

---

## 2026-05 最新 Harness 論文

### 23. Continual Harness
- **arXiv**: [2605.09998](https://arxiv.org/abs/2605.09998)
- **發表**: 2026-05-11
- **摘要**: Online adaptation for self-improving foundation agents; runtime harness modification without retraining.

### 24. Harness Engineering as Categorical Architecture
- **arXiv**: [2605.12239](https://arxiv.org/abs/2605.12239)
- **發表**: 2026-05-12
- **摘要**: Category theory framework for harness composition; functorial mappings between tool schemas.

### 25. Meta-Harness (Finn et al.)
- **arXiv**: [2603.28052](https://arxiv.org/abs/2603.28052)
- **發表**: 2026-05-12
- **摘要**: End-to-end optimization of model harnesses; Chelsea Finn / Stanford group; joint optimization of harness+model (supersedes #5 entry dated 2026-03).

### 26. AI Harness Engineering: Runtime Substrate
- **arXiv**: [2605.13357](https://arxiv.org/abs/2605.13357)
- **發表**: 2026-05-13
- **摘要**: Runtime substrate for foundation-model software agents; Zhong & Zhu; execution layer taxonomy.

### 27. Effective Harness Engineering for Algorithm Discovery
- **arXiv**: [2605.15221](https://arxiv.org/abs/2605.15221)
- **發表**: 2026-05-15
- **摘要**: Vesper framework for coding agent harness design; empirical on algorithm discovery benchmarks.

### 28. Code as Agent Harness
- **arXiv**: [2605.18747](https://arxiv.org/abs/2605.18747)
- **發表**: 2026-05-18
- **摘要**: Using code structure itself as the harness; Ning et al.; tool schema compilation from code.

### 29. Adapting the Interface, Not the Model
- **arXiv**: [2605.22166](https://arxiv.org/abs/2605.22166)
- **發表**: 2026-05-21
- **摘要**: Runtime harness adaptation for deterministic LLM agents; Xu et al.; interface-level vs weight-level adaptation.

### 30. Cheating Agents: Benchmark Manipulation
- **發表**: 2026-05-23 (DebugML)
- **摘要**: Widespread benchmark manipulation in LLM agent evaluations; implications for harness benchmark validity.

### 31. Coordination Architectural Layer
- **arXiv**: [2605.03310](https://arxiv.org/abs/2605.03310)
- **發表**: 2026-05-05
- **摘要**: Multi-agent coordination as a distinct architectural layer.

### 32. HeavySkill
- **arXiv**: [2605.02396](https://arxiv.org/abs/2605.02396)
- **發表**: 2026-05-04
- **摘要**: Heavy thinking inner skill; extended reasoning within harness skill invocations.
