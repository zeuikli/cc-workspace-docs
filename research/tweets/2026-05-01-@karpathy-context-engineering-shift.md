# Context Engineering: Filling the window with just the right information — @karpathy

**來源**：https://x.com/karpathy/status/1937902205765607626
**作者**：Andrej Karpathy（@karpathy）
**發布日期**：2026-05-01（近似）
**收錄日期**：2026-05-10
**類型**：推文（+ 後續討論）
**分類**：context-engineering

---

## 核心推文

> "I suggest to use the term 'context engineering' over 'prompt engineering'. It is more accurate to the actual challenge:
>
> — filling the context window with just the right information for the next step
> — it's not just about wording a single prompt
> — it's about system design: memory, tool outputs, search results, instructions, etc.
>
> Prompt engineering = write a better sentence. Context engineering = system architecture."

---

## 研究摘要

**TL;DR**：Karpathy 正式確立「context engineering」術語，將關注點從「提示措辭」移向「系統設計」——memory、tool outputs、search results、instructions 的架構配置。

### 核心論點

1. **Prompt Engineering 的侷限性**：prompt 只是一句話，context engineering 是系統架構決策
2. **Context Window as Resource**：填充的「不是更多資訊」，而是「下一步恰好所需的資訊」
3. **Harness 與 Context 的連結**：harness 決定了哪些資訊進入 context → harness IS context engineering

### 關鍵引用

> "The delicate science of filling the context window with just the right information for the next step." — @karpathy

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| 相關性 | 10/10 | 直接定義 cc-workspace 的核心實踐框架 |
| 可行動性 | 9/10 | 重新框架了所有 harness 設計決策 |
| 新穎性 | 8/10 | 術語統一有重大影響，論點本身不全新 |
| **總評** | **9/10** | — |

---

## 與 cc-workspace 的連結

- `context-management.md` §理論錨點直接引用此推文（已收錄）
- 支持 CLAUDE.md 的三層載入策略（auto → on-demand → manual = context engineering）
- 強化 harness-design.md 的設計哲學：harness 工程 = context 工程

**已在 workspace 中引用**：`research/tweets/2025-06-25-@karpathy-607626.md`（原始推文版本，此為 2026-05 後續討論擴散版）
