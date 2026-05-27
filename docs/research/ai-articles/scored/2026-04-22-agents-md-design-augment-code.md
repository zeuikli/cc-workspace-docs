---
url: "https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files"
title: "A Good AGENTS.md is a Model Upgrade"
date: 2026-04-22
type: article
---

# A Good AGENTS.md is a Model Upgrade

**作者**: Slava Zhenylenko, Member of Technical Staff at Augment Code  
**發布日期**: 2026-04-22（更新：2026-04-23）  
**來源**: https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files

## 評分（5 維度）

| 維度 | 得分 | 說明 |
|------|------|------|
| 原創性 | 8/10 | Augment Code 內部 eval 的數據驅動分析，指出 AGENTS.md 品質對 agent 表現的劇烈影響 |
| 實用性 | 9/10 | 7 種有效模式 + 失敗模式，直接對應 CLAUDE.md 設計理念 |
| 深度 | 8/10 | 有具體數字（25% 提升、30% 下降），但大多停留在高層觀點 |
| 清晰度 | 9/10 | 結構清晰，從問題、方案、反模式、應用都涵蓋 |
| 相關性 | 9/10 | 核心於 agents.md 設計，高度契合 workspace 架構實踐 |
| **平均** | **8.6/10** | **強烈推薦收錄** |

---

## 核心洞見

### 文件品質 = 模型升級

良寫的 AGENTS.md 相當於把模型從 Haiku 升級到 Opus；  
劣質的 AGENTS.md 比完全沒有文件還糟（效能 -30%）。

**含義**: Context 與流程設計的重要性 **超越模型選擇**。

### 七種有效模式

1. **漸進式揭示** (Progressive Disclosure)
   - 主文件 100-150 行，聚焦核心規則
   - 細節拆成參考文件（需時才讀）
   - 效果：全指標 +10-15%

2. **程序化工作流** (Procedural Workflows)
   - Step-by-step 任務描述
   - 6 步部署流程例：正確性 +25%，完成度 +20%

3. **決策表** (Decision Tables)
   - 預先解決架構選擇（React Query vs Zustand）
   - 約定俗成遵守度 +25%

4. **生產程式碼例** (Production Code Examples)
   - 3-10 行真實片段
   - 程式碼重用率 +20%

5. **領域特定規則** (Domain-Specific Rules)
   - 語言、組織特殊約定
   - 須具體且可執行

6. **禁止配對解決方案** (Pair Prohibitions with Solutions)
   - 不只說「不要 X」，要說「改用 Y」
   - 避免 agent 過度謹慎

7. **模組化文件** (Modular Documentation)
   - 中規模模組（100 核心檔）用焦點文件勝過龐大倉庫級文件

### 三大失敗模式

1. **過度探索陷阱** (Overexploration)
   - 原因：架構說明過多或 30+ 條警告規則
   - 後果：Agent 載入不必要 context，完成度 -25%

2. **模式不匹配** (Mismatched Patterns)
   - 過時的架構決策導向錯誤實作

3. **文件發現率差異**
   ```
   AGENTS.md: 100%
   參考文件: 90%+
   DIR README.md: 80%
   嵌套文件: 40%
   孤立 _docs/: <10%
   ```

---

## Workspace 應用

**直接對應 CLAUDE.md 現有設計**：

| AGENTS.md 實踐 | CLAUDE.md 對應 |
|---------------|--------------|
| 漸進式揭示 | 常駐層 (@auto) + 按需層 (@skill) + 手動層 (Read) |
| 決策表 | `.claude/rules/` 各檔案的決策樹 |
| 生產例 | `playbooks/` 中的 SRE runbooks |
| 程序化工作流 | `/deep-review` Skill 的執行檢查表 |
| 禁止配對解決 | `core.md` §「外科刀式修改」對應的正確做法 |

**洞見**: AGENTS.md 質量不是「有最好」的附加，而是 **負責任的 context engineering 必備**。

---

## 引申思考

### 跨領域應用

不只 coding agent：客服、營運、財務、法務 Agent 都需要等效的「工作說明書」。

> AGENTS.md 代表的本質：把資深同仁腦海裡的「做事默契」，轉化成 AI 可理解、可執行、可驗證的操作系統。

### 組織能力升級

- **一階段**: 買最強模型
- **二階段**: 升級 Agent 的工作環境設計
- **未來**: 企業差距不來自模型選擇，而來自誰更會設計「人與 Agent 共同工作的系統」

---

## 評論

Augment Code 的研究打破「模型 ≥ 一切」的直觀。核心發現是 **context 結構化與流程清晰度**對 agent 表現的舉足輕重。

特別有價值的：
- **數據化證據** — 不只概念，有 +25% / -30% 的具體數字
- **失敗模式詳列** — 指出「看似努力的 over-exploration」陷阱
- **文件發現率差異** — 說明為何 AGENTS.md 必須在根目錄且高度焦點

**主要限制**：
- 研究基於 Augment Code 自身 codebase（vendor content 色彩），不是跨組織普遍 eval
- 「好文件」的定義仍高度依賴專案類型（bug fix vs feature 的最優文件完全不同）

**對 workspace 的啟發**：CLAUDE.md 既有的三層載入、決策表、生產例模式已符合 Augment Code 研究的 7 種模式，印證架構設計方向。
