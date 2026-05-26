# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

**arXiv**: 2308.08155 | **發表**: 2023-08-16 | **PDF**: 2023-08-16-autogen-multi-agent-conversation-framework-2308-08155.pdf

## 核心貢獻

Microsoft Research 提出通用 multi-agent 對話框架，允許開發者以自然語言 + 程式碼定義 agent 互動行為。核心抽象：**conversable agent**（可被任何組合的 LLM / 工具 / 人類輸入驅動）+ **conversation pattern**（靈活配置通訊拓撲）。目標：把「multi-agent 協作」降為可程式化的基礎設施，而非任務特定實現。

## 方法 / 架構

- **ConversableAgent**：統一介面，每個 agent 可配置 LLM backend、tool calling、human-in-loop，三者任意組合
- **GroupChat**：N agent 輪流發言的廣播模式，搭配 GroupChatManager 控制發言順序
- **兩人對話（Two-Agent Chat）**：最小單元，UserProxy + AssistantAgent；UserProxy 可轉發人類輸入或自動執行工具
- **Nested Chat**：一個 agent 可以在內部啟動另一個子對話（遞迴委派）
- 支援 termination condition、code execution sandbox、custom reply function

## 關鍵發現與數據

- 展示 6 個應用場景：math（GSM8K）、coding、Q&A、operations research、online decision-making、entertainment
- 在 math 任務中，AutoGen multi-agent 方案優於 GPT-4 單 agent baseline（具體見全文表格）
- 透過 human-in-loop 混合模式（automatic + manual）在敏感 coding 任務中保持安全性
- 框架在 43 頁論文附錄中展示 30+ 頁實際案例，強調通用性

## 對 agent-team 設計的啟示

1. **Conversable agent 是最小可組合單元**：不要為每個任務重新設計 agent；用同一介面 + 不同配置組合
2. **GroupChat 適合廣播式決策，Two-Agent 適合有序 pipeline**：通訊拓撲決定協作語義，設計時先選拓撲
3. **Nested Chat 實現遞迴委派**：orchestrator 可以是 agent，worker 也可以在內部是 orchestrator，天然支援 hierarchical

## 原文關鍵引用（≤150字）

> "AutoGen enables diverse LLM-based applications using multi-agent conversations. It provides a multi-agent conversation framework as a high-level abstraction. With this framework, one can build LLM applications by composing multiple agents that can converse with each other to accomplish tasks... Agents in AutoGen can operate in various modes that employ combinations of LLMs, human inputs, and tools."
