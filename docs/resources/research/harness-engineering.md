# Harness Engineering 研究全景

整合 16 篇核心論文、工程博客資源與 Benchmark 數據，建立 Agent Harness Engineering 的知識基礎。

## Priority A — 核心論文（必讀）

### 1. AHE: Observability-Driven Automatic Evolution

- **arXiv**: [2604.25850](https://arxiv.org/abs/2604.25850)
- **發表**: 2026-04
- **核心洞見**: 提出 AHE 框架，透過三個可觀測性柱子（元件 / 經驗 / 決策）自動進化 agent harnesses。**Harness 改進應由工具、中介軟體、長期記憶主導，而非系統提示詞。**
- **關鍵成果**:
  - Terminal-Bench 2: pass@1 **69.7% → 77.0%**（10 次自動迭代）
  - SWE-bench-verified: 用 **12% 更少 token** 達最佳成績
  - 跨模型族遷移收益：**+5.1 到 +10.1 pp**
- **意義**: 直接驗證「harness > model」命題；Ratchet 自動化演進的學術支撐

---

### 2. Building AI Coding Agents for the Terminal

- **arXiv**: [2603.05344](https://arxiv.org/abs/2603.05344)
- **發表**: 2026-03
- **核心洞見**: 首篇系統區分「Scaffolding（組裝期）」vs「Harness（執行期）」概念的論文。
  - **Scaffolding 定義**: 系統提示、工具定義、subagent 註冊
  - **Harness 定義**: 工具分派、context 管理、安全執行、session 持久化
- **架構創新**: 工作負載專門化模型路由、懶惰工具發現、自動化記憶系統

---

### 3. Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures

- **arXiv**: [2604.03515](https://arxiv.org/abs/2604.03515)
- **發表**: 2026-04
- **核心洞見**: 首次對 **13 個開源 coding agents** 進行源碼層級架構分析，提出跨 12 維度、3 層組織的統一分類學。
- **5 個通用控制原語**:
  1. ReAct（推理-行動交錯）
  2. Generate-test-repair
  3. Plan-execute
  4. Multi-attempt retry
  5. Tree search
- **關鍵發現**: 11/13 agents 混合多個原語，而非單一模式

---

### 4. NLAH: Natural-Language Agent Harnesses

- **arXiv**: [2603.25723](https://arxiv.org/abs/2603.25723)
- **發表**: 2026-03
- **核心洞見**: 提出用自然語言表達 harness 行為，引入 Natural-Language Agent Harnesses (NLAHs) 與 Intelligent Harness Runtime (IHR)。解決 harness「深埋在控制器代碼中」的可移植性問題。
- **核心價值**: 使 harness 設計可跨系統遷移、可對比、可科學研究

---

### 5. Meta-Harness: End-to-End Optimization

- **arXiv**: [2603.28052](https://arxiv.org/abs/2603.28052)
- **發表**: 2026-03（Stanford/Chelsea Finn）
- **核心洞見**: 外層迴圈系統，透過訪問原始代碼、分數和所有先前執行軌跡，用 agent 搜尋 harness 代碼空間。類似 Neural Architecture Search，但針對 harness 層。
- **關鍵成果**: 聯合優化 harness + 模型的收益 **15-22%**

---

## Priority B — 重要論文

### 6. ReAct: Synergizing Reasoning and Acting

- **arXiv**: [2210.03629](https://arxiv.org/abs/2210.03629)（ICLR 2023）
- **核心**: LLM agent 的基礎論文。定義推理跡象（reasoning traces）與行動（actions）的交錯模式。
- **成果**: HotpotQA 超越 CoT；ALFWorld +34% 絕對成功率

### 7. Agent Harness Survey

- **來源**: Preprints.org, 2026-03
- **核心引述**: 「隨著 agent 任務變長變複雜，執行可靠性越來越不是模型能力問題，而是包裹在它周圍的『基礎設施層』——agent 執行 harness」

### 8. Memory for Autonomous LLM Agents

- **arXiv**: [2603.07670](https://arxiv.org/abs/2603.07670)
- **核心**: long-running agents 的記憶設計調查。Pattern B（主流）：working memory 在 context window，長期記錄在外部向量/結構化存儲，每步檢索相關記錄。
- **核心挑戰**: 檢索品質是瓶頸

### 9. Agentic AI: Architectures, Taxonomies, and Evaluation

- **arXiv**: [2601.12560](https://arxiv.org/abs/2601.12560)
- **核心**: 新一代 LLM agents 作為結合記憶、工具使用、環境反饋的認知控制器。涵蓋 CAMEL、AutoGen、MetaGPT、LangGraph、Swarm 等框架。

---

## Priority C — 工具與方法論論文

| 論文 | arXiv | 核心貢獻 |
|------|-------|---------|
| Learning to Rewrite Tool Descriptions | 2602.20426 | 工具描述的措辭顯著影響 agent 成功率；提出自動化重寫工具 schema |
| Act While Thinking | 2603.18897 | 在 agent 完成思考前並行執行工具，減少延遲 |
| Design Patterns for Securing LLM Agents | 2506.08837 | LLM agent 安全防禦模式，針對提示詞注入等攻擊 |
| Architecting Resilient LLM Agents | 2509.08646 | 安全的 Plan-and-Execute 架構設計 |

---

## 工程博客資源

### Lilian Weng — LLM Powered Autonomous Agents

- **URL**: [lilianweng.github.io](https://lilianweng.github.io/posts/2023-06-23-agent/)
- **定位**: 業界標準入門文章；Planning-Memory-Tools 三層框架的經典定義
- **核心框架**:
  - Planning: Task Decomposition（CoT, ToT）+ Self-Reflection
  - Memory: Sensory / Short-term（context）/ Long-term（向量存儲）
  - Tools: 外部 API 超越訓練數據限制

### Eugene Yan — Patterns for Building LLM-based Systems

- **URL**: [eugeneyan.com](https://eugeneyan.com/writing/llm-patterns/)
- **7 大 Patterns**: Evals、RAG、Fine-tuning、Caching、Guardrails、Defensive UX、Collect User Feedback
- **Agent Harness 洞見**: 「專化模型組隊」勝過單一通才；Guardrails + Evals 是生產環境必需品

### Adnan Masood — Agent Harness Engineering: The Rise of the AI Control Plane

- **URL**: [Medium](https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d)
- **核心**: 5 層 Control Plane 架構視角（Context → Tool/Function → Execution Loop → State & Memory → Safety & Observability）
- **關鍵統計**: 企業 AI 失敗 **65% 源自 harness 層缺陷**，而非模型限制
- **獨特觀點**: 正確 cache 管理可將 token 成本降低十倍

### Daily Dose of DS — The Anatomy of an Agent Harness

- **定位**: 最完整的 harness 組件分解（11 個生產級組件）
- **11 個核心組件**: Orchestration Loop、Tools、Memory、Context Management、Prompt Construction、Output Parsing、State Management、Error Handling、Guardrails & Safety、Verification Loops、Subagent Orchestration
- **核心論點**: Verification 能使品質提升 2-3 倍

### LangChain — Agent Engineering: A New Discipline

- **核心定義**: 「將非確定性 LLM 系統迭代精煉為可靠生產體驗的過程」
- **工程循環**: Build → Test → Ship → Observe → Refine → Repeat
- **關鍵轉變**: 放棄「發布前完美」，改為快速發行 + 生產學習

---

## Benchmark 資源

### Terminal-Bench 2.0

- **URL**: [tbench.ai](https://www.tbench.ai/leaderboard/terminal-bench/2.0)
- **Harness 影響量化**: 同 Opus 4.6，不同 Harness：**66.9% → 79.8%**（13pp 差距）
- **意義**: 第一個直接量化 harness 影響的 benchmark

### SWE-bench / SWE-bench Verified / SWE-bench Pro

- **URL**: [swebench.com](https://www.swebench.com/)
- **規模**: 2,294 issues；Verified 版 500 個（人工 3 倍驗證）
- **2026 最新成績（SWE-bench Pro）**: Claude Opus 4.7 64.3%、GPT-5.4 57.7%

---

## 跨源共識點

| 共識 | 量化依據 | 核心論文 |
|------|---------|---------|
| Harness 影響 > Model 大小 | Vesper 論文：harness 結構佔 40% 性能差距，model 大小只佔 30% | 2605.15221 |
| Context 管理是最高槓桿 | Stanford Meta-Harness：59.6% → 76.4%（16.8pp）| 2603.28052 |
| Verification 使品質提升 2-3× | Daily Dose DS；LangChain 從 Top 30 → Top 5 | NLAH 論文 |
| Harness 可不重訓練自動演化 | Continual Harness：運行時在線 RL 循環 | 2605.09998 |
| 工具設計是 schema 語言工程 | Tool Rewriting 論文：措辭顯著影響成功率 | 2602.20426 |

---

## 延伸閱讀

- [跨源知識地圖](/resources/research/knowledge-map/)
- [延伸閱讀與參考資料](/resources/reference/)
- [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/)
