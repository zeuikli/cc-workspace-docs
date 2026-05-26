---
url: "https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files"
title: A Good AGENTS.md Is a Model Upgrade. A Bad One Is Worse Than No Docs at All
date: 2026-05-02
type: article
---

# A Good AGENTS.md Is a Model Upgrade. A Bad One Is Worse Than No Docs at All

**來源**：https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files  
**作者**：Augment Code（官方部落格）  
**發佈日期**：2026 年（確切日期未標示）  
**收錄日期**：2026-05-02  
**類型**：原廠研究報告（vendor content，含 internal eval 數據）

---

## 文章背景

Augment Code 是一家專注於讓 AI 更理解大型企業 codebase 的 AI coding assistant 公司。本文為其系統性 eval 研究，測量 `AGENTS.md`（或 `CLAUDE.md` 等等效文件）對 code generation 品質的影響，並量化哪些文件模式有效、哪些有害。

---

## 核心發現

### 結論一：文件品質 ≈ 模型升級效果

- 最佳 `AGENTS.md` 帶來的性能提升，**相當於跨越一個 Claude 模型等級**（如 Haiku → Sonnet）。
- 最差 `AGENTS.md` 比完全沒有文件還糟，最差情況讓 completeness **下降 30%**。

### 結論二：7 個有效文件模式

| 模式 | 效果 | 說明 |
|------|------|------|
| **Progressive Disclosure** | 10–15% 提升 | 主文件 100–150 行，細節用 reference 文件 |
| **Procedural Workflows** | 遺漏檔案 40%→10%，correctness +25%，completeness +20% | 六步驟部署流程範例 |
| **Decision Tables** | best practices +25% | 結構化決策矩陣（如 React Query vs Zustand 選擇標準）|
| **Production Code Examples** | 程式碼重用 +20%，pattern 一致性提升 | 真實 codebase 的 3–10 行片段 |
| **Domain-Specific Rules** | 有效，但規則過多效果遞減 | 語言或組織特定限制，需具體可執行 |
| **Prohibition + Solution** | 防止探索失敗 | "Don't" 必須搭配對應的 "Do"，否則觸發驗證循環 |
| **Modular Architecture** | 優於 repo-root 一份大文件 | 模組層級文件優先 |

### 結論三：2 個主要失敗模式

**1. Overexploration Trap（過度探索陷阱）**
- 過長的架構概述 → agent 載入 80K+ 無關 token
- 30+ 條 "don't" 規則但無替代方案 → 觸發驗證循環
- 結果：執行時間加倍，completeness 下降 20%

**2. Incompatible New Patterns（舊文件誤導新架構）**
- 文件描述現有做法，但任務是新架構設計時會誤導 agent
- 解法是 specification-driven development，而非更多文件

---

## 文件可發現性（Discovery Rate）

| 位置 | 發現率 |
|------|--------|
| `AGENTS.md`（repo root） | 100% |
| 被明確 reference 的文件 | 90%+ |
| 工作目錄的 `README.md` | 80%+ |
| 子目錄 `README` | ~40% |
| `_docs/` 等孤立資料夾 | <10% |

> Agent 的文件發現機制：約 50% 透過 grep 和語意搜尋，不只依靠明確 reference。

---

## 各目標對應的最佳模式

| 目標 | 推薦模式 |
|------|---------|
| 程式碼重用 | Production code examples |
| Best practices | Decision tables |
| Feature completeness | Procedural workflows |
| Gotcha handling | Paired "don't/do" statements |
| Context 效率 | Progressive disclosure |

---

## 遷移建議

- 現有 `README.md` 可複用，但需激進刪減
- 品質高且最新的文件從模組層級 `AGENTS.md` reference
- 每份文件 reference 上限：10–15 個
- 審視周圍文件環境：龐大 spec 文件（500K+ 字元）會污染精心寫的 `AGENTS.md`

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 直接量化本 workspace CLAUDE.md 設計原則（Progressive Disclosure、Prohibition+Solution 等），多項已實作，可立即用來稽核現有 rules |
| B. 創新性 | 7/10 | 「壞文件比沒文件還糟 -30%」、「overexploration trap」是新量化洞見；其餘模式與既有最佳實踐重疊 |
| C. 證據品質 | 7/10 | 有具體 eval 數字，但為自家 internal eval，未外部驗證；vendor content 偏差存在 |
| D. 技術深度 | 8/10 | 有具體失敗模式、discovery rate 表、metric-specific 優化表——可操作性高 |
| E. 泛化性 | 9/10 | 直接適用於所有 `CLAUDE.md` / `AGENTS.md` 設計場景，跨工具通用 |
| **加權總分** | **8.0/10** | 9×0.3 + 7×0.2 + 7×0.2 + 8×0.15 + 9×0.15 = 2.7 + 1.4 + 1.4 + 1.2 + 1.35 = **8.05 ≈ 8.0** |

**整合決策**：Rule（強化既有規則）  
**整合位置**：`.claude/rules/skill-authoring.md` — 以 Overexploration Trap 和 Prohibition+Solution 模式補充 §4「規則寫法」和 §2「SKILL.md 長度控制」  
**整合狀態**：待實作
