---
url: "https://martinfowler.com/articles/harness-engineering.html"
date: 2026-04-02
authors: Birgitta Böckeler
source: Martin Fowler Blog (by Birgitta Böckeler, Thoughtworks)
tags: [harness-design, feedforward, feedback, control-theory, coding-agents]
---

# Harness Engineering for Coding Agents (Martin Fowler)

**原始來源**：https://martinfowler.com/articles/harness-engineering.html  
**作者**：Birgitta Böckeler（Thoughtworks）  
**發表平台**：Martin Fowler Blog  
**歸檔日期**：2026-05-10

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | Feedforward/Feedback 分類可直接映射到 hooks + rules |
| B. 創新性 | 7/10 | 控制論框架應用於 harness 設計，教學價值高 |
| C. 證據品質 | 7/10 | Thoughtworks 實務來源，非嚴格實驗 |
| D. 技術深度 | 7/10 | 清晰模式，實作細節留給讀者 |
| E. 泛化性 | 9/10 | 適用任何 coding agent 系統 |
| **加權總分** | **7.7/10** | 8×0.3 + 7×0.2 + 7×0.2 + 7×0.15 + 9×0.15 = 7.70 |

**整合決策**：RULE — feedforward/feedback 分類法整合進 `harness-design.md`  
**整合位置**：`.claude/refs/harness-design.md` §元件分類  
**整合狀態**：待實作

---

## TL;DR

Coding agent harness 的控制論框架：**Feedforward controls**（引導 agent，如 architecture docs、structural tests）vs **Feedback controls**（感知 agent 輸出，如 linters with LLM-readable messages）。三層監管：maintainability harness、architecture fitness harness、behavior harness（最不成熟）。強調 computational（確定性）vs inferential（AI 語意）控制的分工。

---

## 核心主張

### 1. Feedforward vs Feedback 分類

**Feedforward Controls（引導）**：
- Architecture Decision Records（ADRs）作為 agent 的設計約束
- Structural tests（例：「所有 API handler 必須有對應 error handler」）
- CLAUDE.md 中的 coding conventions

**Feedback Controls（感知與修正）**：
- Linters with LLM-readable error messages（不是給人看的 error，是給 AI 可理解的描述）
- Unit test failure reports 格式優化
- PostToolUse hooks 的輸出格式化

> "The quality of feedback depends on whether the AI can parse and act on it. A linter error that says 'line too long' is worse than one that explains 'this line exceeds PEP-8 limits, making it harder to review in diff views.'"

### 2. 三層 Harness 監管成熟度

| 層次 | 成熟度 | 範例 |
|------|------|------|
| **Maintainability** | ✅ 成熟 | lint、format、test coverage |
| **Architecture Fitness** | ⚠️ 中等 | dependency checks、circular import detection |
| **Behavior** | ❌ 最不成熟 | functional correctness、business logic validation |

Behavior harness 最難，因為需要語意理解，不能只靠 deterministic 工具。

### 3. Computational vs Inferential 控制

| 類型 | 定義 | 範例 |
|------|------|------|
| **Computational** | 確定性規則 | 「import 必須在檔案頂部」|
| **Inferential** | AI 語意判斷 | 「這個函式是否符合設計意圖？」|

建議：能用 Computational 就不用 Inferential（成本、可靠性優先）。

---

## 對 cc-workspace 的映射

| 論文概念 | cc-workspace 對應 |
|---------|----------------|
| Feedforward controls | CLAUDE.md rules + `.claude/rules/*.md` |
| Feedback controls | PostToolUse hooks（`pre-commit-review.sh`）|
| Maintainability harness | `healthcheck.sh` + `/deep-review` |
| Architecture fitness | 目前缺乏 dependency graph checks |
| Behavior harness | `/deep-review` LLM 審查（inferential）|
| LLM-readable linter messages | ⚠️ 現有 lint 輸出未針對 LLM 優化 |

**Gap**：Lint 輸出未針對 LLM 優化（Computational feedback 效率不足）

---

## 行動建議

1. 在 `pre-commit-review.sh` 中格式化 lint 輸出，加入「為什麼這是問題」的上下文
2. 評估 Architecture Fitness harness：建立 dependency check（例：`scripts/check-deps.sh`）
3. 在 CLAUDE.md 明確標記哪些規則是 Feedforward（靜態引導）vs Feedback（事後修正）
