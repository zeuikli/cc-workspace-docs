---
url: "https://arxiv.org/abs/2607.01641"
title: "When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents"
archived_date: 2026-07-18
arxiv_id: 2607.01641
authors: ["Xinyi Hou", "Shenao Wang", "Yanjie Zhao", "Haoyu Wang"]
pdf_path: pdfs/2607.01641.pdf
published_date: 2026-07-02
---

# When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents

**Authors**: Xinyi Hou, Shenao Wang, Yanjie Zhao, Haoyu Wang
**Published**: July 2026
**Source**: https://arxiv.org/abs/2607.01641
**arXiv ID**: 2607.01641
**Categories**: Software Engineering (cs.SE)
**PDF**: [research/papers/pdfs/2607.01641.pdf](https://arxiv.org/abs/2607.01641)

---

## Abstract

The researchers identify a failure class called Infinite Agentic Loops (IALs) that occurs when LLM agents repeatedly execute model calls, tools, workflow transitions, or agent handoffs when the feedback path is not effectively bounded. These failures can cause cost exhaustion, model denial of service, context growth, and repeated external side effects. To address this problem, the team developed IAL-Scan, a static analysis tool that abstracts heterogeneous agent code into a framework independent Agent IR and constructs an Agentic Loop Dependence Graph to identify feedback paths. Evaluation across 6,549 repositories revealed 68 confirmed IAL failures across 47 projects, achieving 91.9% precision in their detection methodology.

---

## Core Thesis

- 定義 Infinite Agentic Loop (IAL)：agent 邏輯、框架語意、runtime 觀測、終止機制交互作用下，feedback path 未被有效界定，導致 model call/工具/workflow transition/agent handoff 無限重複執行。
- 後果具體化：cost exhaustion（費用爆炸）、model denial-of-service、context 無限增長、重複的外部副作用（如重複寫入/呼叫外部 API）。
- 提出 IAL-Scan 靜態分析工具：把異質 agent 程式碼抽象成框架無關的 Agent IR，建構 Agentic Loop Dependence Graph (ALDG) 找出 feedback path，檢查是否能無界重複觸達高成本或狀態增長操作。
- 實測 6,549 個 repository，確認 47 個專案中 68 個 IAL 失效案例，偵測精確率 91.9%。
- **Workspace 關聯**：與 core.md TEST 章「unverified_success 閘門」及 `core.md §PROPOSE 委派`（原 subagent-strategy.md）「fan-out child 不 self-retry」規則直接相關——IAL 是本 workspace 一貫防範的「agent 不知道何時該停」失效模式的正式化與可機械偵測版本；IAL-Scan 的 Agent IR + dependence graph 方法論可作為未來稽核 `/autoresearch` 或 `fusion-sidekick` 自管迴圈是否有界終止的靜態檢查參考。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
