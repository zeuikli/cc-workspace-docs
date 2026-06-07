# 課程講義

本課程涵蓋 Claude Code 與 Agent Harness 核心概念，從基礎原理到進階架構，共六堂。

## 課程清單

### [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/)

Agent = Model + Body + Harness 三層等式、Agentic Loop 三階段、Agent 失敗五層級歸因診斷。

**關鍵概念**：Harness first、先修 Harness 再換模型

---

### [Lecture 02：CLAUDE.md 與規則設計](/lectures/lecture-02-claude-md/)

CLAUDE.md 結構設計、12-Rule Canon、規則層級與 override 邏輯。

**關鍵概念**：Rules vs Preferences、Rule ratchet、CLAUDE.md 五段落框架

---

### [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/)

Context window 管理、Prompt caching、Token 優化策略、CJK token 倍率。

**關鍵概念**：Context Engineering vs Prompt Engineering、KV cache 命中率

---

### [Lecture 04：Harness 架構設計](/lectures/lecture-04-harness-architecture/)

Planner / Generator / Evaluator 三層架構、CAR 14-component 框架、Harness 健康度評估。

**關鍵概念**：CAR scorecard、HARNESS-CARD、Model-Harness-Fit

---

### [Lecture 05：Memory 與 Workspace 管理](/lectures/lecture-05-memory-workspace/)

跨 session 記憶系統、MEMORY.md 設計、Hermes 模式、Workspace canon。

**關鍵概念**：In-context vs External memory、記憶四類型、Ratchet 原則

---

### [Lecture 06：安全與 Hooks](/lectures/lecture-06-security/)

Permission model、Hooks 實戰腳本、危險指令攔截、Zero Trust 設計原則。

**關鍵概念**：Hooks 四事件、allowlist / blocklist、pre-commit 攔截

## 學習路徑

1. **入門**：Lecture 01 → 02 → Project 01
2. **進階**：Lecture 03 → 04 → Project 02
3. **完整**：依序完成 01–06 + 兩個 Projects
