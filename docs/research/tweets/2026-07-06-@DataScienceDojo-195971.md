---
url: "https://x.com/DataScienceDojo/status/2074202317491195971"
title: "Fable 5 is expensive if you use it wrong"
author: "Data Science Dojo"
archived: 2026-07-12
handle: "@DataScienceDojo"
published: 2026-07-06
stats: 25 likes · 5 retweets · 77 bookmarks · 44428 views
tags: [model-routing, orchestrator-worker, cost-optimization, subagent-config, fable5]
type: twitter-article
---

# Fable 5 is expensive if you use it wrong — @DataScienceDojo

**來源**：https://x.com/DataScienceDojo/status/2074202317491195971
**作者**：Data Science Dojo（@DataScienceDojo）
**發布日期**：2026-07-06
**收錄日期**：2026-07-12
**類型**：Twitter Article
**統計**：25 likes · 5 retweets · 77 bookmarks · 44428 views

---

## 全文

Fable 5 costs $10/$50 per million tokens. That's 2x Opus 4.8 and up to 5x Sonnet 5.
Run an entire coding session through it, planning, boilerplate, tests, formatting, all of it, and you're paying frontier rates for work a cheaper model would've handled identically.
Most people using Fable 5 in Claude Code right now are burning budget on tasks that never needed frontier-level judgment in the first place.
The fix isn't using Fable 5 less. It's using it smarter.
Set Fable 5 up as an orchestrator instead of a single-model worker. It plans, decomposes the task, and decides what actually needs deep reasoning.
Then it delegates:
- Hard reasoning, architecture, debugging → a subagent pinned to Opus
- Mechanical work, boilerplate, formatting → a subagent pinned to Sonnet
Fable spends its (expensive) tokens only where the judgment call matters. Everything routine gets handled at a fraction of the cost, without you babysitting which model should touch which task.
The setup takes about 10 minutes. Two subagent configs, one CLAUDE.md file, done. No third-party tools, Anthropic models only.
We wrote up the full step-by-step, including the exact subagent configs, the model frontmatter fields you need to get right.
Full guide here: https://datasciencedojo.com/blog/claude-code-fable-5-orchestrator-workflow/

---

## 研究摘要

**TL;DR**：把 Fable 5 當 orchestrator 而非全程 worker，硬推理丟 Opus subagent、機械工作丟 Sonnet subagent，省下 frontier 價差。

### 核心論點

- Fable 5 定價 $10/$50 每百萬 tokens，是 Opus 4.8 的 2 倍、Sonnet 5 的最高 5 倍；若整段 coding session（規劃、樣板、測試、格式化）全用 Fable 跑，等於用 frontier 價格做不需要 frontier 判斷力的工作。
- 解法不是少用 Fable，而是重新分工：Fable 5 只負責規劃、拆解任務、判斷哪裡需要深度推理，實際執行委派給釘住特定模型的 subagent——硬推理/架構/除錯給 Opus，機械性工作（樣板、格式化）給 Sonnet。
- 宣稱設置只需約 10 分鐘：兩個 subagent 設定檔 + 一份 CLAUDE.md，純 Anthropic 模型組合，不需第三方工具。
- 完整步驟（含 subagent 設定與 model frontmatter 欄位）收在外部部落格連結，推文本身只給概念與定價數字。

### 關鍵數據 / 工具

- 定價：Fable 5 $10/$50（input/output 每百萬 tokens），Opus 4.8 約其一半，Sonnet 5 最低到 1/5。
- 外部連結：`datasciencedojo.com/blog/claude-code-fable-5-orchestrator-workflow/`（完整 subagent 設定範例，本次未抓取）。

### 批判性觀察

- 「orchestrator 用高檔位判斷、實作下沉低檔 worker」的分工模式與本 workspace `subagent-strategy.md`「檔位經濟：主對話檔位高於任務→執行下沉低檔 worker」、`multi-mode-agent`/`pilot` skill 現有設計完全一致，屬既有實踐的重述，未帶來新資訊。
- 全文沒有任何實測數字佐證「省下多少成本」或「品質是否維持」，只給定價比例（2x/5x）與「10 分鐘設置」的口頭宣稱，核心細節（subagent 設定/CLAUDE.md 內容）都在外部連結而非推文本身，證據品質薄弱。
- 內容本質是引流到部落格文章的摘要貼文，推文本身資訊密度低（僅 12 blocks、1312 字），可行動性受限於是否額外抓取該外部連結。

---

## 評分

| 維度 | 分數 | 說明 |
|------|------|------|
| A. Workspace 可行動性 (30%) | 6/10 | 分工模式已與 workspace 現有 pilot/multi-mode-agent 一致，屬驗證而非新增 |
| B. 創新性 (20%) | 3/10 | orchestrator 分工按任務難度路由模型已是常見既有模式 |
| C. 證據品質 (20%) | 3/10 | 僅定價倍數與口頭宣稱，無實測成本/品質數字，細節在外部連結 |
| D. 技術深度 (15%) | 3/10 | 推文本身無具體 subagent 設定或程式碼，僅概念層描述 |
| E. 泛化性 (15%) | 7/10 | 任何 Claude Code 多檔位使用者皆可套用，純 Anthropic 生態 |
| **加權總分** | **4.5/10** | A×0.3+B×0.2+C×0.2+D×0.15+E×0.15 |

**整合決策**：Skip
**理由**：核心分工模式與本 workspace 既有 pilot/subagent-strategy 設計重疊，未帶來新資訊；核心細節在外部連結，推文本身證據與技術深度不足。
