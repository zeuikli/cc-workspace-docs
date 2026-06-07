---
url: "https://warmwater.dev/blog/claude-skills-agent"
title: "Claude Skills 完全解析：Agent 時代的能力模組化設計"
date: 2025-12-31
category: Skill
source: warmwater.dev
---

# Claude Skills 完全解析：Agent 時代的能力模組化設計

問題的起點：為什麼 Agent 需要 Skills？
--------------------------

【Context】 當你想讓 Claude 幫你執行重複性任務——格式化文件、審核合約、建立 Excel 公式——最直覺的做法是把所有指令塞進 prompt。但當你有幾十個甚至上百個這樣的任務時，Context Window 就爆炸了。

【Core Problem】

傳統做法的困境：

```
Task 1 指令（500 tokens）
Task 2 指令（800 tokens）
Task 3 指令（600 tokens）
...
Task 50 指令（???）

結果：Context 爆炸 💥
```

你不可能同時把所有任務的完整指令都放進 prompt。

【Core Insight】

Anthropic 的解法是：

> 不要一次載入所有能力，讓 Agent 按需取用

這就是 Claude Skills 的設計理念。

## 什麼是 Claude Skills？

【Context】 Claude Skills 是 Anthropic 推出的能力模組化機制，本質上是「可重用的工作能力包」。

【Definition】

一句話定義：

> Skills 是教 Claude 如何執行特定任務的模組，包含指令、腳本、範本，且按需載入

【Structure】

一個 Skill 的基本結構：

```
my-skill/
├── SKILL.md          ← 核心指引 + YAML metadata
├── scripts/          ← 可執行腳本
├── templates/        ← 範本檔案
└── resources/        ← 相關資源
```

【Key Difference】

Skills vs 傳統 Prompt：

| 面向 | 傳統 Prompt | Claude Skills |
|------|-------------|---------------|
| 載入方式 | 全部塞進 context | 按需載入 |
| 可重用性 | 每次重寫 | 模組化分享 |
| 複雜任務 | Context 爆炸 | 漸進式揭露 |
| 包含內容 | 純文字 | 指令 + 腳本 + 範本 |

## 漸進式揭露：Skills 的核心設計

【Context】 Skills 最精妙的設計在於「漸進式揭露」（Progressive Disclosure）——不是一次載入所有內容，而是分層逐步展開。

【How It Works】

```
Step 1: 只載入 metadata
        ↓
        「你有這項技能：格式化 Excel」
        ↓
Step 2: Agent 判斷需要時
        ↓
        載入 SKILL.md 完整內容
        ↓
Step 3: 需要更多細節時
        ↓
        載入 scripts / templates
```

【Why This Matters】

這個設計解決了根本問題：

```
傳統做法：
├─ 50 個任務 × 500 tokens = 25,000 tokens
└─ Context 爆炸

Skills 做法：
├─ 50 個 metadata × 50 tokens = 2,500 tokens
├─ 實際使用 2 個 Skill × 500 tokens = 1,000 tokens
└─ 總計：3,500 tokens ✅
```

你可以同時掛載幾百個 Skills，但只有真正用到的才會進入 context。

## Skills vs MCP Server：什麼時候用哪個？

【Context】 很多人會問：Skills 和 MCP Server 有什麼不同？它們是互補的，不是替代關係。

【Core Difference】

| 面向 | Claude Skills | MCP Server |
|------|---------------|-----------|
| 本質 | 工作流程模組 | 外部工具橋接 |
| 目的 | 教 Claude 怎麼做 | 讓 Claude 能呼叫外部系統 |
| 執行位置 | Claude 內部 | 外部服務 |
| 典型場景 | SOP 自動化、格式規範 | API 呼叫、資料庫查詢 |
| 複雜度 | 較低 | 較高（需維護 server） |

【Simple Analogy】

```
Skills = 教你「如何做」（知識與流程）
MCP = 給你「工具」（外部能力）
```

【How They Work Together】

實際工作流程可能是這樣：

```
User: 幫我查詢客戶資料並格式化成報告

Claude 判斷：
├─ 需要「報告格式化」Skill → 載入格式規範
├─ 需要呼叫 CRM API → 透過 MCP Server
└─ 結合兩者完成任務
```

Skills 負責「怎麼做」，MCP 負責「用什麼工具」。

## 實際應用場景

【Context】 Skills 最適合需要重複執行、有明確規範的任務。

【Use Cases】

**1. 文件格式化**

*   根據公司品牌指南格式化文件
*   統一程式碼風格
*   產出固定格式的報告

**2. SOP 自動化**

*   合約審核流程
*   PR Review 檢查清單
*   客戶 onboarding 步驟

**3. 專業領域知識**

*   特定框架的最佳實踐
*   內部工具的使用方式
*   領域專有的術語和規範

【When to Use Skills】

✅ 適合：

*   重複性任務
*   有明確規範的流程
*   需要團隊共享的知識

❌ 不適合：

*   一次性任務
*   需要即時外部資料
*   高度動態的情境

## 總結：Skills 的設計哲學

【Core Insight】

Skills 代表了一種思維轉變：

```
傳統思維：把所有指令塞給 AI
Skills 思維：讓 AI 按需學習能力
```

這不只是技術優化，更是對「AI 如何獲取能力」的重新設計。

【Key Takeaways】

1.  Skills 是「可重用的能力模組」，不是單次 prompt
2.  漸進式揭露解決了 Context 爆炸問題
3.  Skills 教「怎麼做」，MCP 提供「用什麼工具」
4.  兩者互補，不是替代

【Final Thought】

> Skills 讓 Agent 從「被動接收指令」變成「主動調用能力」

這是 Agent 架構演進的重要一步。

---

**官方資源**：

*   [Anthropic Skills Repository](https://github.com/anthropics/skills)
*   [Equipping Agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

**相關資源**：

*   [Awesome Copilot](https://github.com/github/awesome-copilot)
*   [MCP Protocol 規範](https://modelcontextprotocol.io/)

---

**Tags**: `#ClaudeCode` `#Skills` `#MCPServer` `#Agent` `#ContextManagement` `#Anthropic` `#AIArchitecture`

**延伸閱讀**

*   [Claude Code：從 claw-code 的分析看一個 Coding Agent 的設計關心](/blog/claude-code-claw-code-coding-agent) — 深入版：Skills 在 Claude Code 整體架構（Hooks/Skills/MCP 三層）的設計位置
*   [Harness Engineering — AI 工程師的第三個維度](/blog/harness-engineering-ai) — Skills 是 Harness 的「能力注入」機制：理解它在整體 AI 基礎設施的角色
*   [Plan Mode 之後：你的 AI Agent 還缺什麼](/blog/superpowers-plan-mode-ai-agent) — Skills 的實際應用：Superpowers 如何用 Skill 懶載入覆蓋 coding lifecycle
