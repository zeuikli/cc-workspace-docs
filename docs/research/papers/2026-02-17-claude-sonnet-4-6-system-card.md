---
url: "https://www.anthropic.com/claude-sonnet-4-6-system-card"
title: "Claude Sonnet 4.6 System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2026-02-17
source_url: "https://www.anthropic.com/claude-sonnet-4-6-system-card"
web_only: True
---

# Claude Sonnet 4.6 System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-sonnet-4-6-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf`，內容相同。）
**Published**: February 17, 2026

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。

---

## 摘要（依官網內容整理）

Sonnet 4.6 為高性價比 frontier 模型，coding 表現逼近同期 Opus 4.6（差距約 1.2pp），維持 Sonnet 一貫的 $3/$15 定價。安全檔位 ASL-3，並延續勒索評測 0% 的世代記錄。

---

## 結構化摘要

### 模型與定位
- **Claude Sonnet 4.6**：Sonnet 檔位升級，定位「best-value frontier」——近 Opus 品質、Sonnet 價格。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**79.6%**（10 trials 平均；距同期 Opus 4.6 的 80.8% 僅 1.2pp）。
- **SWE-bench Multilingual**：**75.9%**。
- **OSWorld-Verified**：**72.5%**（Opus 4.6 為 72.7%）。
- **Terminal-Bench 2.0**：**59.1%**。
- **Pricing**：**$3 / 1M input、$15 / 1M output**（維持 Sonnet 定價）。
- **AI Safety Level**：**ASL-3**。

### 值得注意章節
- 「near-Opus at Sonnet price」的 coding 收斂——Sonnet 與 Opus 在主流 coding/agent 評測上差距持續縮小。

---

## Workspace 關聯（評估）

- **`pilot`（tier=quality，原 `sonnet-pilot`） 強化**：79.6% vs Opus 4.6 80.8% 差 1.2pp——`pilot`（tier=quality，原 `sonnet-pilot`）「接近 Opus 品質」的定位在此世代幾乎成立；多數 coding 任務可優先 Sonnet 省成本。
- **model-selection-grid 重新校準**：Sonnet/Opus 差距收斂使「10+ 檔才上 Opus」的門檻更穩固——Opus 留給真正需要 ceiling 的架構/跨模組任務。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **ASL-3 + 勒索 0%**：對齊側延續穩定，sub-agent 委派的安全假設不變。
