# HTML 作為主要輸出格式（HTML-First Strategy）

> 來源：[Using Claude Code: The unreasonable effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html)  
> 作者：Thariq Shihipar（Anthropic）  
> 整理日期：2026-06-05  
> 原文日期：2026-05-20

---

## 核心主張

HTML 優於 Markdown 的原因：資訊密度、視覺清晰度、可分享性、互動能力、資料導入效率。Thariq 已幾乎完全放棄 Markdown，轉向「HTML maximalist」工作流。

---

## 為何 HTML 優於 Markdown

| 面向 | Markdown 限制 | HTML 優勢 |
|------|-------------|---------|
| 資訊密度 | 平面文字 + 有限表格 | 表格、SVG、CSS、可摺疊區塊、空間布局 |
| 視覺清晰度 | 超過 100 行難以閱讀 | Tabs、分層、響應式設計 |
| 分享 | 需要附件 | 單一 URL，同事真的會看 |
| 互動 | 靜態 | Slider、旋鈕、自訂編輯器，可匯出回 prompt |
| 資料導入 | N/A | File system、MCP（Slack/Linear）、瀏覽器、git history |

---

## 五大使用場景與 Prompt 範例

### 1. 規格與探索（Specs & Exploration）

視覺化多個解法，讓選擇更容易：

```text
Generate 6 distinctly different approaches to [problem]...
lay them out as a single HTML file in a grid
```

### 2. Code Review

直觀理解 PR 變更：

```text
Create an HTML artifact reviewing this PR... focus on streaming/backpressure logic.
Render actual diff with inline margin annotations
```

### 3. 設計與原型

測試 animation 並互動調參：

```text
Create a HTML file with several sliders controlling animation parameters...
try different options on this animation, give me a copy button
```

### 4. 報告與研究

資料視覺化合成：

```text
Produce a single HTML explainer page: diagram of token-bucket flow,
key code snippets annotated, key numbers
```

### 5. 客製編輯器

打造任務專屬介面：

```text
Make draggable cards across Now/Next/Later/Cut columns...
Add a copy as Markdown button
```

---

## 快速開始

不需要預設模板，直接 prompt：

```text
> make an HTML file
> create an HTML artifact showing [your content]
```

**避免的常見錯誤：**
- 過度設計（不需要預設模板）
- 過早把 pattern 變成 Skill（先有機地實驗）
- 擔心 token 用量（1M context window 讓這不再是問題）

---

## 實作建議

- HTML 作為**持久參考工件**：可跨 session 再次載入做為 context
- 互動 HTML 允許用戶調整設計並將修改後的參數匯回 prompt
- 優先用 HTML 做 code review 的 artifact，比文字摘要更清晰
- 增加使用者持續參與 AI 生成工作的可能性（而非被動消費輸出）

---

## 關鍵洞察

> "HTML outperforms Markdown as an output format because it enables richer information density, improved visual clarity, easier sharing, interactive capabilities, and better context ingestion."

這是 Claude Code 特有優勢：可讀取 file system、MCP connector、web browser、git history，是在 claude.ai 或 Claude Design 介面操作所沒有的能力。
