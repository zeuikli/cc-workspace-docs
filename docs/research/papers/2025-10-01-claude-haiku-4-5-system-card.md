---
url: "https://www.anthropic.com/claude-haiku-4-5-system-card"
title: "Claude Haiku 4.5 System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2025-10-01
source_url: "https://www.anthropic.com/claude-haiku-4-5-system-card"
web_only: True
---

# Claude Haiku 4.5 System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-haiku-4-5-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%20Haiku%204.5%20System%20Card.pdf`，內容相同。）
**Published**: October 2025（清單記 2025-10-01；模型公開發布日為 2025-10-15）

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。

---

## 摘要（依官網內容整理）

Haiku 4.5 為成本/速度導向的小型旗艦，但 coding 能力已逼近前代中大型模型，定位為 multi-agent fan-out 與高吞吐場景的經濟選擇。安全檔位較低（ASL-2）。

---

## 結構化摘要

### 模型與定位
- **Claude Haiku 4.5**：最快、最便宜的 4.5 世代檔位；主打高並行、低延遲、multi-agent。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**73.3%**（500 題完整集，50 trials 平均，無 test-time compute，128K thinking budget，bash + 字串替換編輯雙工具 scaffold）。
- **AI Safety Level**：**ASL-2 Standard**（低於同期 Sonnet 4.5 / Opus 4.1 的 ASL-3）。
- **Pricing**：約 **$1 / 1M input、$5 / 1M output**；prompt caching 最高省 90%、batch 省 50%。

### 值得注意章節
- 後續官方溯及性陳述指出：自 Haiku 4.5 起的每個 Claude 模型在勒索評測上皆 **0%**——即 Haiku 4.5 是「代理失準勒索行為清零」的世代起點。

---

## Workspace 關聯（評估）

- **`pilot`（tier=cost，原 `haiku-pilot`） 核心參照**：本卡是 `pilot`（tier=cost，原 `haiku-pilot`）（cost-first）的能力底座；73.3% SWE-bench 證明「便宜檔位仍可做實質 coding」，支持「先調 effort 再換 model」的 effort-first 原則。
- **multi-agent fan-out 經濟性 ↔ `core.md §PROPOSE 委派`（原 subagent-strategy.md）**：Haiku 低成本使「fan-out 上限 4 / dynamic workflow ≤16」的並行委派在預算上可行——平行 sub-agent 用 Haiku 跑研究/靜態分析很划算。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **ASL-2 ↔ 能力下限**：`core.md §PROPOSE 委派`（原 subagent-strategy.md）「能力下限」提醒——低檔位適合 on-rails 任務（重構/摘要），off-rails 仍須升級。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
