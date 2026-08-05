---
url: "https://www.anthropic.com/claude-mythos-preview-system-card"
title: "Claude Mythos Preview System Card"
archived_date: 2026-06-24
authors: [Anthropic]
domains: [system-card]
published_date: 2026-04-07
source_url: "https://www.anthropic.com/claude-mythos-preview-system-card"
web_only: True
---

# Claude Mythos Preview System Card

**Source**: Anthropic 官方 system card（web-only，無 arXiv PDF）— https://www.anthropic.com/claude-mythos-preview-system-card
（原始 URL 307 重導向至官方 PDF `www-cdn.anthropic.com/.../Claude%20Mythos%20Preview%20System%20Card.pdf`，內容相同。）
**Published**: April 7, 2026

> 依官方公開資訊整理；數字以可交叉驗證者為主，不確定處保守描述。

---

## 摘要（依官網內容整理）

Mythos Preview 是 Anthropic 當時最強 frontier 模型，但因 **網路安全能力過強**而**未做一般商用釋出**——改作為有限夥伴的防禦性 cybersecurity 計畫使用。官方強調限制存取的決策由 cyber 能力驅動，而非 RSP 硬性要求。是首份「無一般商用 GA」即公開的 system card。

---

## 結構化摘要

### 模型與定位
- **Claude Mythos Preview**：最強 frontier 模型；非 GA，限定夥伴防禦性 cyber 用途。

### 關鍵能力 / 安全評估數字（依官方公開資訊整理）
- **SWE-bench Verified**：**93.9%**。
- **SWE-bench Pro**：**77.8%**。
- **Terminal-Bench 2.0**：**82.0%**。
- **USAMO 2026**：**97.6%**。
- **Cybench**：飽和（**100%** pass rate）。
- **CyberGym**：**0.83**（由前代 0.67 提升）。
- **自製 Firefox 147 zero-day exploitation benchmark**：**84%** 成功率。
- **AI Safety Level**：公開文件未明定正式檔位；二手分析提及實務上以 ASL-3 或更高（部分提及 ASL-4 條件供夥伴存取），**正式 tier 官方留白**——保守標註，不臆斷。

### 值得注意章節
- **不釋出決策**：cyber 能力（尤其 zero-day exploitation 達 84%）使官方選擇不 GA，改走防禦夥伴計畫——能力治理優先於商業化的明確案例。

---

## Workspace 關聯（評估）

- **cyber 域路由紀律**：CLAUDE.md 註明「Fable 對 cyber/bio prompt silent fallback → Opus，該域直接指定 Opus」——Mythos 級 cyber 能力正是此類治理的源頭；本庫對 cyber/bio 任務應顯式指定模型、不賭路由。
- **ceiling 但不可用**：Mythos Preview 是 `pilot`（tier=frontier，原 `fable-pilot`）/`pilot`（tier=ceiling，原 `opus-pilot`） 之上的「理論天花板」參照，但非可調用模型——model-selection 時不納入可選清單。
- **能力治理 ↔ 生產紅線**：與 core.md「不可逆/高風險動作須 gate」同精神——能力越強，部署越須前置防護。⚠️ 域外：本庫無 cyber offensive 任務，此卡為背景認知而非操作依據。
