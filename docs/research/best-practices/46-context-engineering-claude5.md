# Claude 5 世代的 Context Engineering 新規則

> 來源：[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)（2026-07-24）
> 整理日期：2026-08-04
> **canonical 落點**：本 workspace 的完整校準與剪枝判準在 `.claude/refs/context-engineering-claude5.md`（L2 SSoT）。本檔只保留官方原文重點，供 corpus 追溯，**不重複該檔的 workspace 對應表**。

---

## 官方實證錨點

Anthropic 為 Claude Opus 5 / Fable 5 **刪掉了 Claude Code system prompt 的 80% 以上**，在其 coding evals 上**無可量測退化**。

根因：舊 prompt 對模型 over-constrain，且指令彼此打架——同一次請求裡同時出現「leave documentation as appropriate」與「DO NOT add comments」。新世代模型會花推理預算去調解衝突訊息，所以「多加一條保險條文」不是零成本。

---

## 六條 Then → Now

| # | 規則 | 內容 |
|---|------|------|
| 1 | Judgment over rules | 用「寫得像周遭程式碼」取代硬性條數禁令，讓模型判斷 |
| 2 | Tool design over examples | 與其給使用範例（會限縮探索），不如把參數設計得有表達力、enumeration 清楚（`status: pending/in_progress/completed`）|
| 3 | Progressive disclosure over upfront info | 驗證與 code review 指導從 system prompt 移出，改成 Claude 需要時才呼叫的 Skill；部分工具改 **deferred loading**（先 `ToolSearch` 取 schema 才可呼叫）|
| 4 | Simplified descriptions over repetition | 同一指令不要在 system prompt 與 tool description 重覆；指令的正確歸宿是 tool description |
| 5 | Auto-memory over manual saving | 新世代自動保留相關記憶，不必事事用 `#` 熱鍵手寫進 CLAUDE.md |
| 6 | Rich references over simple specs | 除了 markdown 規格，也吃 HTML artifact / test suite / code sample / rubric |

---

## Context Assembly 四層

| 層 | 承載 |
|----|------|
| System prompt | 產品脈絡與核心目的（平台持有）|
| CLAUDE.md | 輕量 repo 描述 + critical gotchas |
| Skills | 編碼團隊意見的輕量指南 |
| References | code sample / spec / mockup / test suite |

工具：`/doctor` 可對現有 context 提出 rightsize 建議（v2.1.206 起會主動提案 `CLAUDE.md` 精簡）。

---

## 重要邊界（本 workspace 立場）

**驗證閘門不在「可刪的鷹架」之列。** 能力提升不得換取更少驗證（`core.md` 能力悖論）。可刪的是為補償模型弱點而堆的程序性鷹架，不是 `[E]` 閘門與不可逆操作確認。

---

## 延伸閱讀

- `.claude/refs/context-engineering-claude5.md` — L2 校準 + 剪枝判準（workspace canonical）
- `47-verification-loops-skills.md` — 被移出 system prompt 的驗證指導長什麼樣
- `21-memory-claudemd.md` · `38-steering-claude-code.md` — CLAUDE.md 與行為調整機制
