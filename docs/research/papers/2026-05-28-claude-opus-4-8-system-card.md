---
url: "https://www.anthropic.com/claude-opus-4-8-system-card"
title: "Claude Opus 4.8 System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2026-05-28
source_url: "https://www.anthropic.com/claude-opus-4-8-system-card"
web_only: True
---

# Claude Opus 4.8 System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-opus-4-8-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%20Opus%204.8%20System%20Card.pdf`，內容相同。）
**Published**: May 28, 2026

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。本卡為當前 workspace 主力模型（claude-opus-4-8）的官方文件。

---

## 摘要（依官網內容整理）

Opus 4.8 為 Opus 4.7 的增量旗艦升級，核心敘事不在 coding 跳分，而在 **honesty / alignment**：更積極標記程式缺陷、降低 misalignment incidence，並引入更便宜的 fast mode。安全檔位延續 ASL-3。

---

## 結構化摘要

### 模型與定位
- **Claude Opus 4.8**（API: claude-opus-4-8）：最新 GA 旗艦；coding 小幅進步，主打誠實度與對齊。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**88.6%**（由 4.7 的 87.6% 提升，+1pp）。
- **SWE-bench Pro**：**69.2%**（領先同期 GPT-5.5 58.6%、Gemini 3.1 Pro 54.2%）。
- **Honesty / 缺陷標記**：較 Opus 4.7 約 **4× 更不易**讓 code flaw 漏標而不警示。
- **Misalignment incidence**：**~1.9**（4.7 為 ~2.5；官方稱「與 Mythos Preview 大致打平」）。
- **Pricing**：**$5 / 1M input、$25 / 1M output**（同 4.7）；fast mode 約 2.5× 速度、$10/$50，較 4.7 fast mode 便宜約 3×。
- **AI Safety Level**：**ASL-3**（同 4.7）。

### 值得注意章節
- 誠實度為發布主軸而非 benchmark 跳分——「working ≠ honest」的對齊側深化。
- misalignment incidence 已逼近受限的 Mythos Preview，顯示對齊投資的邊際成果。

---

## Workspace 關聯（評估）

- **ceiling 檔位的世代參照之一**：本卡是 `pilot`（tier=ceiling，原 `opus-pilot`）在 Opus 4.8 世代的能力底座。⚠️ 原文寫「即當前 session 的 claude-opus-4-8」——該敘述已於 2026-08-02 失效（harness 已換代，`HARNESS_MODEL_VERSION` 見 session-init 輸出）。**「當前 session 模型」這類隨 session 變動的事實不應寫入 corpus**（`context-management.md` §Prompt Caching 禁令①：動態事實不寫穩定前綴）；模型檔位對照請一律以 `refs/model-profiles.md` 為 SSoT。
- **誠實度 ↔ unverified_success / anti-hack**：core.md「subagent 自報成功須親驗」「anti-hack 雙重驗證」——4.8 更積極標記缺陷，但 4x 改善仍非 100%，機械驗證閘門不可撤。
- **fast mode 便宜化 ↔ effort-first / finops**：fast mode 降價使「速度 vs 成本」trade-off 在 Opus 檔位更有彈性，呼應 effort-first 與成本紀律。
- **misalignment ~1.9 ↔ The Loop RECORD**：對齊非歸零，core.md「assisted-success ≠ autonomous-success」的人工介入歸因仍須保留。
