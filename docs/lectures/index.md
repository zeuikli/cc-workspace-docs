# 課程講義

本課程涵蓋 Claude Code 與 Agent Harness 的核心概念，從基礎原理到組織治理，共十二堂。

內容以 Anthropic 官方文件與 [claude.com/blog 歸檔](/research/claude-blog/)（153 個條目，2025-11 ~ 2026-07）為一手來源，每堂課末列出對應的官方原文連結。

## Part 1：基礎（Lecture 01–03）

### [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/)

Agent = Model + Body + Harness 三層等式、Agentic Loop 三階段、Agent 失敗五層級歸因診斷、導入成效的量化錨點。

**關鍵概念**：Harness first、先修 Harness 再換模型、刪鷹架與強化閘門同時發生

---

### [Lecture 02：CLAUDE.md 與規則設計](/lectures/lecture-02-claude-md/)

CLAUDE.md 四層作用域、Ratchet 原則、觸發點判斷表（何時該加 CLAUDE.md / Skill / MCP / Hook / Plugin）、Context Assembly 四層。

**關鍵概念**：請求 ≠ 保證、規則不是零成本、每 3–6 個月審閱

---

### [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/)

Context Rot 量化數據、Sub-agent 作為 Context Firewall、Claude 5 世代六條新規則、Prompt Caching 的五個禁令。

**關鍵概念**：system prompt −80% 無退化、可刪的是鷹架不是閘門、cache hit rate 是健康指標

---

## Part 2：架構（Lecture 04–06）

### [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/)

Planner / Generator / Evaluator 三層分離、25 種 Hooks 事件、Exit Code 規約、Harness 複雜度隨模型能力調整。

**關鍵概念**：Generator 不能自評、獨立 verifier 讓 false positive 減半

---

### [Lecture 05：Memory 與 Workspace 管理](/lectures/lecture-05-memory-workspace/)

跨 session 三層狀態架構、Git Worktrees、Sub-agent 委派與工具作用域、Model 分層與 Advisor 模式。

**關鍵概念**：In-context vs External memory、`/fork` 語義已改、不要 mid-session 換模型

---

### [Lecture 06：安全沙箱與 Proxy](/lectures/lecture-06-security/)

Native Sandboxing、Filesystem + Network 雙重隔離、細粒度 Permission、CISO 四個評估問題、六類 agentic 漏洞。

**關鍵概念**：環境層優先於模型層、外部輸入是資料不是指令、憑證在網路邊界才替換

---

## Part 3：擴展（Lecture 07–09）

### [Lecture 07：Skills 設計與 Progressive Disclosure](/lectures/lecture-07-skills/)

七種行為調整機制的選擇、九大 Skill 類別、自由度校準、Progressive Disclosure、Claude A/B 迭代法。

**關鍵概念**：Description 是選擇引擎、窄橋 vs 開闊平原、準確率 21% → 95%

---

### [Lecture 08：Sub-agents、Agent Teams 與 Dynamic Workflows](/lectures/lecture-08-subagents-workflows/)

三個協作層級、委派的硬門檻、五種協調模式、六種 workflow 模式、W28–W31 扇出治理變更。

**關鍵概念**：工具呼叫 > 20 次必須委派、預設不再巢狀 spawn、背景 session 會自動 commit/push

---

### [Lecture 09：模型選型與 Effort 經濟學](/lectures/lecture-09-model-selection/)

四個 class 定位、現役模型規格與定價、effort 等級、Advisor 策略、自建 eval。

**關鍵概念**：class × effort 二維框架、每 token 價格 ≠ 每任務價格、Advisor 90% 效能 / 63% 成本

---

## Part 4：工程化（Lecture 10–12）

### [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/)

驗證迴圈四種部署形態、Oracle 先驗、裝完成的六種捷徑、Code Review 與 REVIEW.md。

**關鍵概念**：觸發權在 harness 不在模型、獨立 verifier false positive −50%、測試檔被改即紅旗

---

### [Lecture 11：MCP 整合與外部系統](/lectures/lecture-11-mcp/)

三種 transport 與 scope、intent-grouped 工具設計、Tool Search、OAuth 與 managed MCP、MCP 2026-07-28 規格。

**關鍵概念**：Tool Search 降 85%+ token、3–6 個 server 上限、stateless core

---

### [Lecture 12：Plugins、自動化與組織治理](/lectures/lecture-12-governance/)

Plugin 打包、Routines 三種觸發器、Vaults、大型 codebase 三層 context 架構、AI 原生工程組織三指標。

**關鍵概念**：Agentic Search 不是 RAG、每 3–6 個月審閱、風險可見且有界

---

## 學習路徑

| 路徑 | 內容 | 預估時間 |
|------|------|---------|
| **入門** | Lecture 01 → 02 → 03 → [Project 01](/projects/project-01-init-workspace/) | 4 小時 |
| **架構** | Lecture 04 → 05 → 06 → [Project 02](/projects/project-02-harness-design/) | 5 小時 |
| **擴展** | Lecture 07 → 08 → 09 | 4 小時 |
| **工程化** | Lecture 10 → 11 → 12 | 4 小時 |

**按角色的建議切入點**：

- **個人開發者**：01 → 02 → 03 → 07 → 10（先讓單人工作流可靠）
- **技術主管 / 平台團隊**：01 → 04 → 09 → 12（先看架構與成本治理）
- **SRE / 安全**：01 → 06 → 10 → 12（先看邊界與稽核）

## 延伸資源

- [實作專案](/projects/) — 兩個動手練習
- [資源庫](/resources/) — 最佳實踐與研究摘要精選
- [研究資料庫](/research/) — 論文、深度報告、官方 blog 歸檔全文
