---
layout: home

hero:
  name: "Zeuik's Claude Code Docs"
  text: "Claude Code Harness 工程課程"
  tagline: 從 CLAUDE.md 設計到驗證迴圈與組織治理，掌握讓 AI Agent 真正可靠的工程方法。十二堂課，四個實作專案，全部接地於官方一手來源。
  actions:
    - theme: brand
      text: 開始學習 ->
      link: /lectures/
    - theme: alt
      text: 實作專案
      link: /projects/
    - theme: alt
      text: 研究資料庫
      link: /research/
    - theme: alt
      text: GitHub ↗
      link: https://github.com/zeuikli/cc-workspace-docs

features:
  - icon: 🧠
    title: Harness 工程理論
    details: 深入理解 Agent = Model + Body + Harness 等式。量化數據證明：同一個模型，不同 Harness 造成 7–23pp 的效能差距。
  - icon: 📄
    title: CLAUDE.md 與規則設計
    details: 四層作用域、Ratchet 原則、觸發點判斷表。以及 2026 年的新變數——規則不是零成本，衝突指令會消耗模型的推理預算。
  - icon: 🔄
    title: Context Engineering
    details: Context Rot 的量化機制（18 個模型全部隨 context 增長下降），Claude 5 世代六條新規則，以及五個會炸掉 prompt cache 的操作。
  - icon: 🏗️
    title: 三層 Harness 架構
    details: Planner / Generator / Evaluator 分離設計。為什麼 Generator 不能自評？25 種 Hooks 事件如何構建防禦層？
  - icon: 🧩
    title: Skills 與 Sub-agents
    details: 九大 Skill 類別、自由度校準、Progressive Disclosure；委派的硬門檻、五種協調模式、六種 Dynamic Workflow 模式。
  - icon: ⚖️
    title: 模型選型與 Effort
    details: class × effort 的二維框架。為什麼「每 token 價格」不等於「每任務價格」？Advisor 策略如何取得 90% 效能而只付 63% 成本？
  - icon: ✅
    title: 驗證迴圈
    details: 獨立 verifier 讓 false positive 減半。Oracle 先驗、裝完成的六種捷徑、REVIEW.md 收斂——驗證的觸發權在 harness，不在模型。
  - icon: 🔒
    title: 安全與治理
    details: 環境層優先於模型層。Filesystem + Network 雙重隔離、六類 agentic 漏洞、CISO 四問、Vault 憑證邊界替換。
---

## 關於本課程

本課程源自 **Zeuik 的私有 cc-workspace**，整理了 SRE / Cloud Architect 視角下對 Claude Code Workspace 的深度研究。

課程以 **Harness Engineering** 為主軸，從理論到實作，幫助你把 Claude Code 這類 AI Agent 從「不可靠」變成「生產可用」。每一堂課都標註官方一手來源，可以追溯回 Anthropic 的原始文件與工程部落格。

**內容規模**：

- **12 堂課程講義** — 基礎 → 架構 → 擴展 → 工程化
- **4 個實作專案** — 建立 workspace → 設計 harness → 驗證資產化 → 推廣成基礎建設
- **研究資料庫** — 315 篇論文歸檔、深度研究報告、49 篇最佳實踐、[153 個官方 blog 條目](/research/claude-blog/)（2025-11 ~ 2026-07）

## 適合誰閱讀

- 想讓 Claude Code / Codex 在真實專案中可靠工作的工程師
- 對 LLM Agent 架構設計感興趣的開發者
- 需要為團隊建立 AI 開發規範與護欄的技術主管
- 關心 agentic 系統安全邊界的 SRE 與資安工程師

## 學習路徑

| 階段 | 內容 | 產出 | 預估時間 |
|------|------|------|---------|
| **基礎** | Lecture 01–03：Harness 等式、CLAUDE.md、Context Engineering | 可跨 session 記憶的 workspace | 4 小時 |
| **架構** | Lecture 04–06：三層架構、Memory / Worktree、安全沙箱 | 有獨立驗證與安全邊界的 harness | 5 小時 |
| **擴展** | Lecture 07–09：Skills、Sub-agents / Workflows、模型選型 | 可重用的 Skill 與成本策略 | 4 小時 |
| **工程化** | Lecture 10–12：驗證迴圈、MCP、Plugins 與治理 | 團隊可安裝的 plugin 與自動化 | 4 小時 |

按角色的建議切入點見[課程總覽](/lectures/)。

## 2026 年的三個轉向

如果你以前讀過類似的內容，這三件事在 2026 下半年**反轉**了，值得先知道：

1. **從「堆規則」轉向「信任判斷」** — Anthropic 為 Claude 5 世代刪掉 Claude Code system prompt 的 **80% 以上**，coding evals 無可量測退化。多加一條保險條文不是零成本。
2. **驗證的觸發權從模型收回 harness** — `/verify`、`/code-review`、`/deep-research` 都改為手動呼叫。任何假設「模型會自己 review」的流程都已失效。
3. **扇出從「越多越好」轉向「有界治理」** — subagent 上限、預設不巢狀 spawn、預算真正止血、背景 session 收尾語義明確化。

完整論述見 [claude-blog 跨主題合成](/research/claude-blog/docs/synthesis)。

## 關鍵參考資料

> 本課程的理論基礎來自以下一手來源：

**Harness 工程**

- [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [OpenAI: Harness engineering — leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- [LangChain: Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)

**Claude 5 世代**

- [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)（2026-07-24）
- [Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)（2026-07-24）
- [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)（2026-07-22）
- [Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)（2026-06-18）

**安全與治理**

- [Anthropic: How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude)
- [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)（2026-07-17）
- [Zero Trust for AI agents](https://claude.com/blog/zero-trust-for-ai-agents)（2026-05-27）

**Context Rot**

- [Chroma: Context Rot Research](https://www.trychroma.com/research/context-rot)

---

> 內容同步自 [私有 cc-workspace](https://github.com/zeuikli/cc-workspace)，已排除個人職涯記錄（career-wiki）與敏感設定。
> 研究資料庫收錄截止：2026-07-28 · 最後更新：2026-08-05
