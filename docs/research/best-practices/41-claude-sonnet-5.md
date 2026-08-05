# Claude Sonnet 5 完整指南

> 來源：[Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)（2026-06-30）
> 來源：Claude Code changelog v2.1.197（2026-06-30）
> 整理日期：2026-07-06

---

## 模型定位

**Claude Sonnet 5** 於 2026-06-30（Claude Code v2.1.197）發布，取代 Sonnet 4.6 成為 Claude Code **預設模型**。定位為「Agentic 能力大幅躍進」的平衡檔位——縮小與 Opus 4.8 的效能差距，同時維持遠低於 Opus/Fable 的成本。

---

## 技術規格

| 規格 | 值 |
|------|-----|
| Model ID | `claude-sonnet-5` |
| Context window | **1M token**（原生，changelog 公告文字）|
| 輸入定價（促銷，至 2026-08-31）| $2 / MTok |
| 輸出定價（促銷，至 2026-08-31）| $10 / MTok |
| 輸入定價（促銷結束後，2026-09-01 起）| $3 / MTok |
| 輸出定價（促銷結束後）| $15 / MTok |
| 發布日期 | 2026-06-30 |

**可用方案**：Free / Pro 預設模型；Max / Team / Enterprise 可選用；Claude API、Claude Platform、Claude Code 均可存取。

---

## 能力與行為差異（對照 Sonnet 4.6）

- Agentic 表現顯著提升：規劃、工具使用（browser/terminal）、自主連續執行的品質接近以往需要更大模型才能達到的水準
- 推理、工具呼叫、coding、知識工作任務全面優於 Sonnet 4.6
- 幻覺率與 sycophancy 降低
- 抵抗 prompt injection、拒絕惡意請求的能力提升
- **安全**：cyber safeguards 預設啟用；cybersecurity 能力明顯弱於 Opus 系列（設計上的限制，非 bug）

---

## Claude Code 整合細節（v2.1.197 起）

- 取代 Sonnet 4.6 成為 CLI 預設模型（`/model` 不指定時的 fallback）
- Subagent alias `sonnet` 解析至 `claude-sonnet-5`
- 與同批（v2.1.198）「Subagent 預設背景執行」「Explore agent 繼承主 session 模型（上限 opus）」等變更同時生效，兩者常一併觸發舊 workflow 假設失效，升級後建議重新檢視 pin 設定與 subagent 檔位對照表

---

## 模型選擇建議

| 情境 | 推薦模型 |
|------|---------|
| 一般日常工作馬（預設） | **Sonnet 5** |
| 深推理 / 跨模組架構決策 | Opus 4.8 |
| 稀缺頂配、需使用者顯式授權 | Fable 5 |
| 預算敏感 batch 處理 | Sonnet 5 / Haiku 4.5 |
| Cybersecurity 主題 | Opus 4.8（Sonnet 5 該能力刻意弱化）|

---

## 促銷定價注意事項

- 2026-06-30 ~ 08-31：$2/$10（促銷）
- 2026-09-01 起：$3/$15（標準價，仍低於 Sonnet 4.6 同期水準）
- 促銷到期前若有大量批次任務，可提前排程於促銷窗口內完成以降低成本

---

## 延伸閱讀

- `36-claude-fable-5.md` — Fable 5 / Mythos 5，稀缺頂配對照
- `42-w26-27-features.md` — 同批（v2.1.196–198）Claude in Chrome GA、Subagent 背景預設、Org default models 等變更
- `.claude/refs/model-profiles.md` — 本 workspace 檔位對應 SSoT（quality 檔位已 pin `claude-sonnet-5`）
