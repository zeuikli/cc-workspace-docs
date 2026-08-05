# Claude Opus 5 完整指南

> 來源：[Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)（2026-07-24）
> 來源：Claude Code changelog v2.1.219（`claude-opus-5`，1M context window）
> 整理日期：2026-08-04

---

## 模型定位

**Claude Opus 5** 於 2026-07-24 發布，是 Claude 5 世代不到兩個月內的第四個模型（Fable 5 → Mythos 5 → Sonnet 5 → Opus 5）。定位是「多數任務逼近 Fable 5、價格只有一半」的日常主力：接手 Opus 4.8 的價位帶與角色，成為 **Claude Max 的預設模型**、**Claude Pro 可用的最強模型**。

---

## 技術規格

| 規格 | 值 |
|------|-----|
| Model ID | `claude-opus-5` |
| Context window | **1M token**（changelog v2.1.219）|
| 輸入定價 | $5 / MTok（與 Opus 4.8 同價）|
| 輸出定價 | $25 / MTok（與 Opus 4.8 同價）|
| Fast mode | 約 2.5× 速度、2× 價格（$10 / $50）|
| Effort 等級 | low / medium / high 可調，換取速度與成本 |
| 發布日期 | 2026-07-24 |

**可用範圍**：Claude API、Claude Code、Claude Cowork、Claude Platform、claude.ai；AWS Bedrock / Google Cloud Vertex / Microsoft Foundry 同步供應。

---

## Benchmark（官方公布）

| Benchmark | 結果 |
|-----------|------|
| Frontier-Bench v0.1 | 超越所有競品，為 Opus 4.8 的 **2 倍** |
| CursorBench 3.2 | 與 Fable 5 差距 **< 0.5%**，成本為其一半 |
| ARC-AGI 3 | 次佳模型的 **3 倍** |
| OSWorld 2.0 | 優於 Fable 5，成本為其 **1/3** |

能力面重點：驗證與迭代解題能力增強（更常自查自糾）、agentic 推理與自我修正提升、視覺輸出品質提升、科學研究任務（有機化學、蛋白質分析）明顯改善。

**安全**：官方稱其為近期模型中欺騙性行為比率最低者；攻擊性 cyber 能力仍低於 Mythos 5。

---

## 對本 workspace 的影響

- **檔位對照**：`ceiling` 檔位原 pin `claude-opus-4-8`，Opus 5 同價但全面更強 → 應評估換 pin（校準值 SSoT = `.claude/refs/model-profiles.md`，本檔不決定數字）。
- **1M context**：Opus 系列首次與 Sonnet 5 / Fable 5 同為 1M；先前以「Opus context 較小」為前提的 context 預算假設需重驗。
- **Effort 可調**：`low/medium/high` 讓「高檔位模型 + 低 effort」成為可行的成本策略——依 45-model-selection-guide.md，高檔位低 effort 有時在 per-task 經濟性上優於低檔位模型。
- **Prompt cache**：換模型會斷前綴快取，遵守 `context-management.md` 五禁令②（不 mid-session 換模型）。

---

## 與同代模型選型對照

| 情境 | 推薦模型 |
|------|---------|
| 日常主力、深推理、agentic 長跑 | **Opus 5** |
| 最難的 1% 問題、需最強能力且授權明確 | Fable 5（$10/$50）|
| 高頻 sub-agent、批次、成本敏感 | Sonnet 5 |
| 極低成本 / 高頻分類 | Haiku 4.5 |
| 受邀限定、無安全分類器 | Mythos 5 |

---

## 延伸閱讀

- `45-model-selection-guide.md` — 官方選型框架（class × effort × 單位經濟）
- `41-claude-sonnet-5.md` — Sonnet 5（日常工作馬）
- `36-claude-fable-5.md` — Fable 5 / Mythos 5
- `48-w28-w31-features.md` — v2.1.219 等同批 Claude Code 變更
