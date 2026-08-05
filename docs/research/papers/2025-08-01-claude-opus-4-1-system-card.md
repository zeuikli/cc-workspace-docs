---
url: "https://www.anthropic.com/claude-opus-4-1-system-card"
title: "Claude Opus 4.1 System Card (Addendum)"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2025-08-01
source_url: "https://www.anthropic.com/claude-opus-4-1-system-card"
web_only: True
---

# Claude Opus 4.1 System Card (Addendum)

**Source**: Anthropic 官方 system card addendum（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-opus-4-1-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%204.1%20System%20Card.pdf`，內容相同。）
**Published**: August 1, 2025（公開報導多記為 2025-08-05 發布）

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。

---

## 摘要（依官網內容整理）

Opus 4.1 為 Opus 4 的增量升級（addendum 形式 system card），主打 coding 重構（refactoring）、深度研究與 agentic search 的細節追蹤，並提升安全/拒答可靠度。安全檔位延續 Opus 4。

---

## 結構化摘要

### 模型與定位
- **Claude Opus 4.1**：Opus 4 的小幅迭代旗艦，非全新世代。
- 重點：refactoring、in-depth research、detail tracking、agentic search。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**74.5%**（由 Opus 4 的 72.5% 提升，+2pp）。
- **Harmless response rate（無害回應率）**：**98.76%**（由 Opus 4 的 97.27% 提升）。
- **AI Safety Level**：延續 **ASL-3**（與 Opus 4 同檔）。

### 值得注意章節
- 以 addendum 形式發布——僅記錄相對 Opus 4 的差異，未重做完整評測套件。
- 安全側主要為拒答可靠度的漸進改善，未公開新增重大紅線行為。

---

## Workspace 關聯（評估）

- **小數點升級（4 → 4.1）的遷移紀律**：對應 context-management.md「mid-session 禁切模型」——升級於新 session 進行；prompt scaffolding 多半可沿用（與後續 4.7 那種破壞性 tokenizer/API 變更不同）。
- **harmless rate ↑ ↔ TEST 階段**：拒答可靠度提升不等於對齊已解，core.md「測試通過 ≠ 四軸通過」仍成立。
- **`pilot`（tier=ceiling，原 `opus-pilot`） 基線**：Opus 4.1 是 Opus 系列早期 ceiling 參照點之一。
