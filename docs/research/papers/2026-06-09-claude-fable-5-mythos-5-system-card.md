---
url: "https://www.anthropic.com/claude-fable-5-mythos-5-system-card"
title: "Claude Fable 5 & Claude Mythos 5 System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2026-06-09
source_url: "https://www.anthropic.com/claude-fable-5-mythos-5-system-card"
web_only: True
---

# Claude Fable 5 & Claude Mythos 5 System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-fable-5-mythos-5-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%20Fable%205%20&%20Claude%20Mythos%205%20System%20Card.pdf`，內容相同。）
**Published**: June 9, 2026

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。官方 system card 約 319 頁。

---

## 摘要（依官網內容整理）

Fable 5 與 Mythos 5 為同一底層模型的雙版本：**Fable 5** 是「Mythos-class」但做成可一般使用的最強 GA 模型；**Mythos 5** 為同模型解除部分安全限制版，僅透過 Project Glasswing 提供給經審核的 cyberdefender，不對公眾開放。Fable 5 主打多日自主任務、persistent memory、強視覺（從原始截圖通關 Pokémon FireRed）。

---

## 結構化摘要

### 模型與定位
- **Claude Fable 5**：最強 GA 模型，Mythos-class 安全化版本。
- **Claude Mythos 5**：同底層、解除部分 safeguard，限 Project Glasswing 防禦夥伴。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**95.5%**。
- **SWE-bench Pro**：**80.3%**（任何受測模型最高，領先 Opus 4.8 的 69.2%）。
- **能力亮點**：多日自主任務、persistent memory、視覺從截圖通關 Pokémon FireRed。
- **AI Safety Level**：**ASL-3**；化生分級 **CB-1**（具非新穎化生武器資訊能力，但未跨 CB-2 新穎武器門檻）。
- **安全分類器**：對 cyber/bio/chem/model-distillation 請求跑保守分類器；約 **1/20** prompt 會被保守過濾「靜默降級」至舊版 Opus 4.8。

### 值得注意章節
- **雙版本治理模型**：同一強模型，GA 版（Fable）與受限版（Mythos）並行——能力與安全解耦的部署範式。
- **靜默降級機制**：保守 filter 將約 5% prompt 降級到 Opus 4.8——是「安全優先於一致體驗」的明確 trade-off。

---

## Workspace 關聯（評估）

- **`pilot`（tier=frontier，原 `fable-pilot`） 直接對應**：本卡是 `pilot`（tier=frontier，原 `fable-pilot`）（Mythos-class 全能模式）的官方底座——95.5% SWE-bench / 80.3% SWE-bench Pro 是其「最強稽核/優化/架構」定位的能力證據。
- **靜默降級 ↔ cyber/bio 路由紀律**：CLAUDE.md「Fable 對 cyber/bio silent fallback → Opus，該域直接指定 Opus」——本卡的 1/20 降級至 Opus 4.8 正是此機制；故 cyber/bio 任務應顯式指定 Opus 避免賭路由。
- **persistent memory ↔ memory-compactor / 長期記憶回路**：多日自主 + persistent memory 呼應 core.md「長期記憶回路（Compounding Engineering）」與 MEMORY.md 設計。
- **CB-1 / ASL-3 ↔ 安全例外鐵律**：core.md「加密原語/輸入驗證永遠獨立函式」等安全紅線不因模型更強而放寬。
