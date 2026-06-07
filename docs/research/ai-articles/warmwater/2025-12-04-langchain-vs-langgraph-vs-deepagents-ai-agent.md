---
url: "https://warmwater.dev/blog/langchain-vs-langgraph-vs-deepagents-ai-agent"
title: "LangChain vs LangGraph vs DeepAgents：該選哪個 AI Agent 框架？"
date: 2025-12-04
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design  
#  LangChain vs LangGraph vs DeepAgents：該選哪個 AI Agent 框架？完整場景對比指南 
  2025-12-04 · — views      

> **系列文章**：本文是 LangChain 生態系統深度解析系列，幫助你選擇最適合的 Agent 框架


如果你曾經遇過：


> 「LangChain、LangGraph、DeepAgents 都是 LangChain 的產品，到底有什麼差別？」
> 「我該用哪一個框架來建構 AI Agent？」
> 「這三個工具的使用場景和時機是什麼？」


那這篇文章就是為你準備的！我們要深入比較 LangChain 生態系統的三大核心框架，幫助你做出正確的技術選型。

---


## 什麼是 LangChain？


【Context】
LangChain 是 LangChain 生態系統中的基礎函式庫，作為第一個也是最廣泛採用的框架，用於建構基於 LLM 的應用程式。


【Core Knowledge】
LangChain 是一個 Python/JavaScript 函式庫，專為建構 Large Language Models (LLMs) 應用程式而設計。它提供：


- **Modular Components**：預建的組件，如 prompts、chains 和 tools

- **Simple Abstraction**：針對常見 LLM 操作的高階 API

- **Quick Prototyping**：快速開發 LLM 應用程式

- **Integration Ecosystem**：超過 700 種外部服務整合


【Use Cases】
LangChain 最適合用於：


- 具有基本問答功能的簡單聊天機器人

- RAG (Retrieval-Augmented Generation) pipeline

- Prompt engineering 和模板管理

- 快速概念驗證和 MVP

- 無需複雜狀態管理的線性工作流程


【Why Use LangChain】


**優點**：


- 學習門檻低，容易上手

- 豐富的文件和社群支援

- 廣泛的整合函式庫

- 非常適合 LLM 開發初學者


**限制**：


- 對 agent 決策流程的控制有限

- 難以實作複雜的多步驟工作流程

- 當 chains 變得複雜時難以除錯

- 不適合需要狀態管理的生產級應用


【When NOT to Use】
以下情況應避免使用 LangChain：


- 需要跨多個步驟的複雜狀態管理

- 需要精確控制 agent 執行流程

- 需要進階除錯和可觀測性

- 需要循環或條件式工作流程模式


---


## 什麼是 LangGraph？


【Context】
LangGraph 是一個建構在 LangChain 之上的進階框架，專門設計用於建構具有複雜工作流程的狀態化、多角色應用程式。


【Core Knowledge】
LangGraph 是一個基於 graph 的編排框架，將 agent 工作流程視為有向圖。主要特性包括：


- **Graph-Based Architecture**：將工作流程定義為 nodes (函數) 和 edges (轉換)

- **State Management**：內建狀態持久化和 checkpointing

- **Cyclic Workflows**：支援循環、條件和 human-in-the-loop 模式

- **Fine-Grained Control**：精確控制 agent 執行流程


【How It Works】
LangGraph 將 agent 工作流程表示為狀態機：

```
State → Node (Action) → Edge (Transition) → Next State

```


工作流程結構範例：


- **Nodes**：Tools、LLM 呼叫、人工介入點

- **Edges**：條件路由、循環、錯誤處理

- **State**：跨整個工作流程的持久化記憶體


【Use Cases】
LangGraph 擅長處理：


- 具有複雜互動的多 agent 系統

- 需要 human-in-the-loop 審批的工作流程

- 狀態化應用程式（客服機器人、專案管理）

- 需要精確執行控制的應用程式

- 需要 checkpointing 的長時間運行流程


【Why Use LangGraph】


**優點**：


- 完全控制 agent 決策流程

- 內建狀態持久化和恢復

- 支援複雜模式（循環、條件、分支）

- 具有圖形視覺化的優秀除錯能力

- 具備強大錯誤處理的生產就緒


**限制**：


- 學習曲線比 LangChain 陡峭

- 需要理解 graph 概念

- 簡單任務的程式碼較冗長

- 對於基本線性工作流程來說過於複雜


【Tradeoff】
複雜度 vs 控制力：


- LangChain：簡單但控制有限

- LangGraph：複雜但完全控制


根據你的工作流程複雜度需求來選擇。


【Related】
State Machines, Workflow Orchestration, Agent Frameworks, LangChain Middleware

---


## 什麼是 DeepAgents？


20260406更新: 補上我參考了DeepAgents架構設計的簡易Harness Engineering應用([https://github.com/jason8745/llm-kaggle-agent](https://github.com/jason8745/llm-kaggle-agent))


【Context】
DeepAgents 是 LangChain 生態系統的最新成員，隨著 LangChain 1.0 達到里程碑而發布。它專注於自主的、具備推理能力的 agents。


【Core Knowledge】
DeepAgents 是一個用於建構進階 AI agents 的框架，能夠：


- **Autonomous Reasoning**：獨立做出複雜決策

- **Deep Planning**：將複雜目標分解為可執行步驟

- **Self-Reflection**：評估和改進自己的輸出

- **Tool Orchestration**：智能選擇和串聯多個工具


【Core Capabilities】
DeepAgents 引入了：


- **ReAct Pattern**：在迭代循環中進行推理 + 行動

- **Planning Agents**：具有目標分解的多步驟規劃

- **Memory Management**：長期和短期記憶系統

- **Self-Correction**：自主檢測和修正錯誤的能力


【Use Cases】
DeepAgents 設計用於：


- 複雜的研究和分析任務

- 自主問題解決場景

- 需要深度推理鏈的應用

- 多領域知識整合

- 具有高度不確定性和模糊性的任務


【Why Use DeepAgents】


**優點**：


- 三個框架中最自主的

- 最佳的推理和規劃能力

- 適合尖端 AI 應用

- 專為複雜、開放式任務設計


**限制**：


- 最新框架，文件仍在演進中

- 運算成本較高（更多 LLM 呼叫）

- 行為可預測性低於腳本化工作流程

- 需要仔細的 prompt engineering

- 對於明確定義的任務可能過於複雜


【When to Use】
在以下情況使用 DeepAgents：


- 任務需要多步驟推理

- 問題複雜且開放式

- 需要自主決策

- 有人工監督可用

- 成本不是主要限制


【Related】
ReAct Pattern, Autonomous Agents, Planning Systems, LangGraph

---


## 三大框架核心差異對比


【Context】
理解 LangChain、LangGraph 和 DeepAgents 之間的關鍵差異，對於做出正確的框架選擇至關重要。


【Core Comparison】


維度LangChainLangGraphDeepAgents**核心定位**基礎構建模塊工作流程編排自主推理引擎**複雜度**簡單中等複雜**控制力**有限精確自主**狀態管理**弱強大內建**學習曲線**平緩中等陡峭**適用階段**原型開發生產環境前沿研究


【Architecture Pattern】


**LangChain**：Chain-based（線性）

```
Input → Chain1 → Chain2 → Chain3 → Output

```


**LangGraph**：Graph-based（彈性）

```
     ┌→ Node2 →┐
Input → Node1 → Node3 → Output
     └→ Node4 →┘

```


**DeepAgents**：Autonomous（推理）

```
Input → [Plan] → [Act] → [Observe] → [Reflect] → Output
              ↑                                      ↓
              └──────────── Loop ────────────────────┘

```


【Decision Framework】
根據專案需求選擇：


- **簡單任務、快速 MVP** → LangChain

- **複雜工作流程、生產環境** → LangGraph

- **需要自主推理** → DeepAgents


【Related】
Framework Selection, Architecture Patterns, AI Agent Design

---


## 使用場景決策樹


【Context】
此決策樹幫助你快速識別哪個框架最適合你的使用案例。


【Decision Flow】

```
你的 AI 應用需求是？

├─ 需要複雜的推理和自主決策？
│  └─ 是 → DeepAgents
│     └─ 例如：研究助手、複雜問題解決、多領域知識整合
│
├─ 需要精確控制執行流程？
│  ├─ 需要循環、條件分支、狀態持久化？
│  │  └─ 是 → LangGraph
│  │     └─ 例如：多步驟工作流、人工審批、客服系統
│  │
│  └─ 只需要簡單的線性流程？
│     └─ 是 → LangChain
│        └─ 例如：簡單問答、RAG、快速原型
│
└─ 不確定？從 LangChain 開始
   └─ 需求複雜化後再遷移到 LangGraph 或 DeepAgents

```


【Key Scenarios】


**Scenario 1: 客服聊天機器人**


- 簡單 FAQ → **LangChain**

- 需要工單追蹤和狀態管理 → **LangGraph**

- 需要理解複雜問題並自主解決 → **DeepAgents**


**Scenario 2: 文檔分析助手**


- 基本 RAG 查詢 → **LangChain**

- 多步驟分析工作流 → **LangGraph**

- 深度研究和知識整合 → **DeepAgents**


**Scenario 3: 數據分析 Agent**


- 固定查詢和報表 → **LangChain**

- 複雜多步驟分析流程 → **LangGraph**

- 探索性分析和洞察發現 → **DeepAgents**


【Migration Path】
從小處開始，逐步擴展：


- **原型階段**：從 LangChain 開始

- **生產階段**：將複雜部分遷移到 LangGraph

- **進階階段**：為自主功能加入 DeepAgents


【Related】
Use Case Analysis, Framework Selection, Migration Strategy

---


## 技術架構深度比較


【Context】
了解技術架構差異有助於你在擴展性和維護性方面做出明智的決策。


【LangChain Architecture】


**Core Components**:


- **Chains**: Sequential processing pipelines

- **Prompts**: Template management system

- **Tools**: External service integrations

- **Memory**: Simple conversation history


**Execution Model**: Synchronous, linear
**State Management**: Minimal (in-memory only)
**Error Handling**: Basic try-catch patterns


【LangGraph Architecture】


**Core Components**:


- **StateGraph**: Stateful workflow orchestration

- **Nodes**: Executable functions with state access

- **Edges**: Transition logic and routing

- **Checkpointer**: State persistence layer


**Execution Model**: Asynchronous, graph-based
**State Management**: Advanced (persistent, recoverable)
**Error Handling**: Built-in retry, fallback, and error nodes


【DeepAgents Architecture】


**Core Components**:


- **Planner**: Goal decomposition and task planning

- **Executor**: Tool selection and execution

- **Memory**: Long-term and short-term memory systems

- **Reflector**: Self-evaluation and correction


**Execution Model**: Autonomous, reasoning-driven
**State Management**: Hierarchical (task-level and session-level)
**Error Handling**: Self-correction and adaptive planning


【Performance Comparison】


MetricLangChainLangGraphDeepAgents**Latency**低 (1x)中 (1.5x)高 (3-5x)**LLM Calls**少中等多**Memory Usage**低中高**Scalability**水平擴展水平+垂直垂直為主


【Cost Implications】


- LangChain: Lowest cost (fewer LLM calls)

- LangGraph: Moderate cost (state management overhead)

- DeepAgents: Highest cost (multiple reasoning iterations)


【Related】
Architecture Design, Performance Optimization, Cost Management

---


## 實際應用建議


【Context】
針對在實際專案中實作各框架的實務建議。


【Best Practices】


**使用 LangChain 時**:


- 用於 MVP 和快速原型開發

- 保持 chains 簡單且層次淺（≤ 3 步驟）

- 盡可能使用預建的 chains

- 監控複雜度是否超出框架能力


**使用 LangGraph 時**:


- 提前仔細設計 state schema

- 為長時間運行的流程使用 checkpointing

- 實作完善的錯誤處理機制

- 視覺化 graphs 以便除錯和文件化

- 結合 LangChain 組件提高效率


**使用 DeepAgents 時**:


- 提供清晰的目標和成功標準

- 為關鍵決策實作人工監督

- 預算較高的 LLM 成本

- 用於自主性能增加價值的任務

- 從簡單的 agents 開始，再進行複雜推理


【Migration Strategy】


**從 LangChain 遷移到 LangGraph**:

```
Step 1: 識別需要狀態管理的組件
Step 2: 將 chains 轉換為 nodes
Step 3: 定義 state schema
Step 4: 為轉換添加 edges
Step 5: 實作 checkpointing

```


**從 LangGraph 遷移到 DeepAgents**:

```
Step 1: 識別推理需求
Step 2: 定義規劃目標
Step 3: 配置記憶系統
Step 4: 實作自我反思循環
Step 5: 添加人工監督

```


【Common Pitfalls】


**避免**:


- 為簡單線性任務使用 LangGraph（過度設計）

- 為複雜狀態化工作流使用 LangChain（能力不足）

- 使用 DeepAgents 而沒有成本預算

- 混合使用框架而沒有清楚的邊界


**應該做**:


- 從簡單開始，根據需要增加複雜度

- 為每個組件使用正確的工具

- 持續監控成本和效能

- 記錄你的框架選擇和理由


【Related】
Implementation Strategy, Best Practices, Migration Patterns

---


## 生態系統整合建議


【Context】
這三個框架可以在單一應用程式中一起使用，充分發揮各自的優勢。


【Hybrid Architecture Patterns】


**Pattern 1: LangChain + LangGraph**

```
使用場景：混合複雜度的生產應用

架構：
- LangChain: 簡單的 RAG 查詢和工具包裝
- LangGraph: 複雜的多步驟工作流和狀態管理

好處：
- 簡單部分開發更快
- 複雜工作流完全控制
- 最佳的成本效益平衡

```


**Pattern 2: LangGraph + DeepAgents**

```
使用場景：有監督的自主系統

架構：
- LangGraph: 整體工作流編排
- DeepAgents: Graph 中的自主推理節點

好處：
- 有監督的自主性
- 兼顧控制與推理能力
- 需要時可退回到腳本化流程

```


**Pattern 3: All Three Combined**

```
使用場景：企業級 AI 平台

架構：
- LangChain: 基本整合和簡單 chains
- LangGraph: 工作流編排和狀態管理
- DeepAgents: 特定節點的自主推理

好處：
- 最大靈活性
- 每個組件都最佳化
- 可擴展且易維護

```


【Integration Guidelines】


- **Clear Boundaries**：明確定義各框架負責的部分

- **State Sharing**：使用 LangGraph 的 state 作為唯一真實來源

- **Error Handling**：實作跨框架一致的錯誤處理

- **Monitoring**：使用統一的可觀測性工具 (LangSmith)

- **Testing**：獨立測試每個組件以及整合點


【Real-World Example】


客服平台：


- **LangChain**：FAQ 檢索、知識庫搜尋

- **LangGraph**：工單流程、升級邏輯、人工轉接

- **DeepAgents**：複雜問題診斷和解決


【Related】
System Architecture, Integration Patterns, Hybrid Systems

---


## 總結與下一步


【Context】
關於如何開始使用 LangChain 生態系統的最終建議。


【Key Takeaways】


**Framework Summary**:


- **LangChain**: 快速原型、簡單任務、入門首選

- **LangGraph**: 複雜工作流、生產環境、狀態管理

- **DeepAgents**: 自主推理、開放任務、前沿應用


**Decision Criteria**:


- **Complexity** → 任務複雜度決定框架

- **Control** → 控制需求影響選擇

- **Cost** → 預算限制考量因素

- **Timeline** → 開發時間權衡取捨


**Learning Path**:

```
Week 1-2: 掌握 LangChain 基礎
Week 3-4: 學習 LangGraph 處理複雜工作流
Week 5+: 探索 DeepAgents 進階使用案例

```


【Action Items】


**Immediate Next Steps**:


- 使用檢查清單評估你的專案需求

- 從 LangChain 開始學習和原型開發

- 當複雜度增加時遷移到 LangGraph

- 為研究專案實驗 DeepAgents


**Long-term Strategy**:


- 建立所有三個框架的專業知識

- 為生產環境設計混合架構

- 持續關注生態系統發展

- 貢獻開源社群


【Resources】


Official Documentation:


- [LangChain Docs](https://docs.langchain.com/oss/python/langchain/overview)

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)

- [DeepAgents Docs](https://docs.langchain.com/oss/python/deepagents/overview)


【Final Thoughts】


選擇框架不是非黑即白的決策，而是根據具體需求、團隊能力、專案階段做出的權衡。


記住：


- **從簡單開始**：LangChain 入門

- **按需升級**：複雜度增加時遷移到 LangGraph

- **探索創新**：前沿需求嘗試 DeepAgents

- **混合使用**：發揮各框架優勢


AI Agent 開發是一個快速演進的領域，保持學習和實驗的心態最為重要！


【Related】
Getting Started, Learning Resources, Community Engagement

---


## Tags


`#LangChain` `#LangGraph` `#DeepAgents` `#AI Agent` `#框架比較` `#技術選型` `#工作流程編排` `#自主推理` `#Python` `#架構設計`

## 延伸閱讀


- [用 LangChain + LangGraph 實作 Harness Engineering：從 deepagents 學到的設計模式](/blog/langchain-langgraph-harness-engineering-deepagents) — 框架比較後的實作版：LangChain + LangGraph 落地 Harness 五個維度的 POC

- [打開原始碼才發現：三個 Agent 框架，三種截然不同的設計哲學](/blog/agent-20260423) — 更深入的框架原始碼分析：deepagents、openclaw、hermes-agent 的設計哲學對比

- [從一個任務出發：怎麼疊加一個夠用的 Agent 系統](/blog/agent-20260501) — 框架選好之後：如何從零開始疊加一個實際能用的 Agent 系統
     [ System Design ](/blog?tag=System%20Design)[ Tutorial ](/blog?tag=Tutorial)  
### 
相關文章

[Implement用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄2026-05-28](/blog/kube-arena)[Tutorial第一個 Claude Skill：用 skill-creator 打包可重用工作流程2026-05-25](/blog/create-your-own-claude-skill)[System DesignMCP、CLI、還是直呼 API？先看工具長什麼樣2026-05-23](/blog/mcp-cli-api-integration)
