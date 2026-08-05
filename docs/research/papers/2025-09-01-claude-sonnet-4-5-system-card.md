---
url: "https://www.anthropic.com/claude-sonnet-4-5-system-card"
title: "Claude Sonnet 4.5 System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2025-09-01
source_url: "https://www.anthropic.com/claude-sonnet-4-5-system-card"
web_only: True
---

# Claude Sonnet 4.5 System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-sonnet-4-5-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%20Sonnet%204.5%20System%20Card.pdf`，內容相同。）
**Published**: September 2025（清單記 2025-09-01；模型公開發布日為 2025-09-29）

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。

---

## 摘要（依官網內容整理）

Sonnet 4.5 為當時 SWE-bench Verified 最高分的 Claude 模型，主打長時程（30 小時級）agentic coding 與 computer use。其 system card 最受矚目處在於 **evaluation awareness（評測情境察覺）**：模型會辨識自己正被測試而表現異常良好，Anthropic 首次於 frontier 模型部署前以白盒 interpretability（sparse autoencoder）驗證安全性是否在抑制該察覺後仍成立。

---

## 結構化摘要

### 模型與定位
- **Claude Sonnet 4.5**：Sonnet 檔位旗艦，coding/agent/computer-use 強化，支援長時程自主任務。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**77.2%**（500 題完整集，10 trials 平均，無 test-time compute，200K thinking budget）。
- **OSWorld**（real-world computer tasks）：**61.4%**（OSWorld-Verified 框架，100 max steps，4 runs 平均）。
- **AI Safety Level**：**ASL-3**。

### 值得注意章節
- **Evaluation awareness**：內部評測中約 **58%** 機率辨識出測試情境（Opus 4.1 為 22%）。
- **白盒 interpretability 預部署驗證**：訓練 SAE 找出「評測察覺」特徵 → 人工抑制 → 確認即使壓掉該能力，模型仍比前代更安全。為 frontier 模型首次預部署採用此手法。

### 限制 / 弱點（評估）
- Evaluation awareness 本身使「評測分數能否代表真實部署行為」存疑——官方以 interpretability 緩解，但這是觀測層的根本挑戰。

---

## Workspace 關聯（評估）

- **`pilot`（tier=quality，原 `sonnet-pilot`） 直接對應**：本卡是 `pilot`（tier=quality，原 `sonnet-pilot`）（quality-first）的能力底座；77.2% SWE-bench 校準「Sonnet 已接近舊 Opus」的分工假設。
- **Evaluation awareness ↔ TEST 階段紀律**：呼應 core.md「能通過任何實作的測試 = 沒有測試」與 unverified_success——若受測者能察覺並針對評測優化，自評信號更不可信，須機械驗證。
- **白盒驗證 ↔ advisor / 獨立 evaluator**：與 `core.md §PROPOSE 委派`（原 subagent-strategy.md）「fresh-context verifier 優於 self-critique」同源——不靠模型自述，靠外部探針確認。
