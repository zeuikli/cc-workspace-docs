---
url: "https://www.anthropic.com/claude-opus-4-5-system-card"
title: "Claude Opus 4.5 System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2025-11-01
source_url: "https://www.anthropic.com/claude-opus-4-5-system-card"
web_only: True
---

# Claude Opus 4.5 System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-opus-4-5-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%20Opus%204.5%20System%20Card.pdf`，內容相同。）
**Published**: November 2025（清單記 2025-11-01；模型公開發布日為 2025-11-24）

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。

---

## 摘要（依官網內容整理）

Opus 4.5 為當時「全球最佳 coding / agents / computer use 模型」，並伴隨大幅降價（Opus 系列由 $15/$75 降至 $5/$25）。effort level 調控的 token 效率為核心賣點。

---

## 結構化摘要

### 模型與定位
- **Claude Opus 4.5**：4.5 世代旗艦；coding/agent/computer-use SOTA，超越同期 GPT-5.1、Gemini 3 Pro（依官方陳述）。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**80.9%**。
- **Effort 效率**：medium effort 即可追平 Sonnet 4.5 最佳 SWE-bench 分數，且少用 **76%** output tokens；最高 effort 超越 Sonnet 4.5 達 **4.3pp**，且少用 **48%** tokens。
- **Pricing**：**$5 / 1M input、$25 / 1M output**（較前代 Opus 大幅下降）。
- **AI Safety Level**：**ASL-3**；官方稱已大致達到「straightforward ASL-4 rule-out」基準閾值（即接近但以基準任務排除 ASL-4）。

### 值得注意章節
- effort-first 的量化證據：同分數下 effort 調控可省下 48–76% output tokens——直接的成本/品質帕累托。

---

## Workspace 關聯（評估）

- **effort-first 鐵證**：CLAUDE.md「Effort 先於 model；high 為甜蜜點，xhigh 留給溢出任務」在此卡有量化背書——同分數省 76% tokens 正是「先調 effort」的價值。
- **`pilot`（tier=ceiling，原 `opus-pilot`） ceiling 更新**：80.9% SWE-bench 與大幅降價，使 Opus 檔位的成本門檻下降，`pilot`（tier=ceiling，原 `opus-pilot`）的使用時機可放寬。
- **model-selection-grid 校準**：Opus 4.5 medium ≈ Sonnet 4.5 best，提示「跨檔位等效點」——選 model 前先確認 effort 是否已足。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
