# AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors

**arXiv**: 2308.10848 | **發表**: 2023-08-21 | **PDF**: 2023-08-21-agentverse-multi-agent-collaboration-emergent-behaviors-2308-10848.pdf

## 核心貢獻

提出可動態調整 agent 組成的多 agent 框架，涵蓋兩個主軸：（1）**任務求解（task-solving）**：動態組建 agent 團隊解決問題；（2）**模擬（simulation）**：模擬社會行為（如 The Sims 式互動）。框架在協作過程中研究正向（合作湧現）與負向（社會惰化、共識陷阱）兩種湧現行為。

## 方法 / 架構

- **四階段 pipeline**：Recruitment（招募適合的 agent 組成）-> Collaborative Decision-Making（集體決策）-> Independent Action Execution（分工執行）-> Evaluation and Evolution（評估並調整 agent 組成）
- **動態組成（Dynamic Composition）**：根據任務複雜度與進展，在執行中新增/移除 agent，實現 "greater-than-sum" 效果
- **正負湧現管理**：識別 groupthink（群體思維）、free-riding（搭便車）等負向行為並干預
- 支援 simulation 模式：多 agent 擁有獨立記憶 + 個性，模擬社交互動

## 關鍵發現與數據

- Multi-agent 組在複雜推理任務（text games、code generation、logical reasoning）上穩定超越單 agent
- 發現 agent 數量並非越多越好：存在最優 team size，過多 agent 引入 coordination overhead
- 負向湧現可被結構化 prompt 干預緩解（具體設計見 §4.3）
- Task-solving 和 simulation 雙框架複用同一 agent 架構，驗證通用性

## 對 agent-team 設計的啟示

1. **team composition 是一等公民**：不應固定 agent 角色，任務導向的動態招募比靜態分工更適合不確定性高的任務
2. **監控負向湧現是 orchestrator 職責**：groupthink / free-riding 不會自我消除，需外部干預機制（類 R10 checkpoint）
3. **simulation 與 task-solving 共用 agent 架構**：說明 memory + persona + interaction 模組是可複用原語

## 原文關鍵引用（≤150字）

> "We propose AgentVerse, a multi-agent framework that can collaboratively and dynamically adjust its composition as a greater-than-the-sum-of-its-parts system... AgentVerse framework can effectively deploy multi-agent groups that outperform a single agent. We also discuss emergent social behaviors among individual agents within a group during collaborative task accomplishment and discuss strategies to leverage positive ones and mitigate negative ones."
