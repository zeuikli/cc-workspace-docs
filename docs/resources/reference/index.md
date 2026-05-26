# 延伸閱讀與參考資料

篩選標準：只收錄能**直接解釋 Harness 機制**的文章。Harness 在這裡指模型外部的運行系統，包括 agent loop、工具執行、沙箱、狀態、上下文、驗證、終止條件、控制平面和觀測反饋。不收錄泛泛的 prompt engineering 或 agent 框架介紹。

## 核心三篇（必讀）

| 文章 | 日期 | 核心貢獻 |
|------|------|---------|
| [OpenAI: Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) | 2026-02-11 | agent-first 倉庫、repo-local context、custom lint、結構性 guardrail |
| [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 2025-11-26 | initializer agent、coding agent、feature list、progress log、跨上下文窗口交接 |
| [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) | 2026-03-24 | planner / generator / evaluator 三角色、context reset、harness 簡化和組件過期 |

## Harness 工程實踐

| 文章 | 核心貢獻 |
|------|---------|
| [LangChain: Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) | 只改 harness（system prompt、tools、middleware、tracing、self-verification），讓 coding agent 從 Top 30 進到 Top 5 |
| [Thoughtworks / Martin Fowler: Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | 把 harness 拆成 feedforward guides 和 feedback sensors；deterministic vs inferential controls |
| [HumanLayer: Skill Issue — Harness Engineering for Coding Agents](https://humanlayer.dev/articles/harness-engineering-for-coding-agents/) | CLAUDE.md + hooks 的具體實踐；Ratchet 原則 |
| [Cursor: Continually improving our agent harness](https://cursor.com/blog/continually-improving-agent-harness) | 把 harness 當成持續迭代的產品系統；離線評估 + 線上指標 |

## Context 管理

| 文章 | 核心貢獻 |
|------|---------|
| [LangChain: Context Management for Deep Agents](https://www.langchain.com/blog/context-management-for-deepagents) | filesystem offloading、tool-call truncation、summarization、targeted evals |
| [Chroma: Context Rot Research](https://www.trychroma.com/blog/context-rot) | 18 個模型的量化衰退數據；NIAH benchmark；1M context window 的虛假安全感 |

## Agent Loop 機制

| 文章 | 核心貢獻 |
|------|---------|
| [OpenAI: Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/) | Codex runtime harness 的核心循環、工具調用、上下文增長和終止狀態 |
| [Simon Willison: Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) | Agentic loop 設計原則；測試套件是 loop 基礎 |

## 評估與驗證

| 文章 | 核心貢獻 |
|------|---------|
| [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 評估 agent 時評的是 model + harness；evaluation harness 與 agent harness 的區別 |
| [Eugene Yan: LLM Patterns](https://eugeneyan.com/writing/llm-patterns/) | Evals pattern 是生產系統的基石 |

## 企業級 Harness

| 文章 | 核心貢獻 |
|------|---------|
| [Stripe: Minions — one-shot end-to-end coding agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) | devbox 隔離、custom agent harness、blueprints 狀態機、規則檔案、MCP tool curation、安全控制 |
| [Anthropic: Building a C compiler with parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler) | 並行 agent 團隊、任務鎖、git 同步、容器隔離 |
| [Anthropic: April 23 Postmortem](https://www.anthropic.com/engineering/april-23-postmortem) | reasoning effort、context pruning、system prompt 都屬於 harness 變更，且需要回歸治理 |

## Agent 架構理論

| 論文 | 核心貢獻 |
|------|---------|
| [Lilian Weng: LLM-powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) | ReAct、Memory 架構、工具使用的全面介紹 |
| [CoALA: Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) | 認知架構分類框架 |

## CLAUDE.md 與 Karpathy 規則

Andrej Karpathy 的 CLAUDE.md（Skills file）對 AI 輔助開發的影響深遠，以下是核心文章：

| 文章 | 核心貢獻 |
|------|---------|
| [Agentpedia: Karpathy's CLAUDE.md Skills File — The Complete Guide](https://agentpedia.io/karpathy-skills-file-complete-guide) | 完整分析 Karpathy 的四條核心規則 |
| [Andrej Karpathy: LLM Wiki — A Knowledge Management Pattern](https://gist.github.com/karpathy/2c4ece47fbd90eb066b8e0d756f7cd00) | LLM wiki 的 knowledge management 模式 |

**Karpathy 的四條核心原則**：
1. **不讓 AI 刪程式碼**：除非有明確理由，否則刪除是破壞性的
2. **測試要跑起來**：能執行的測試才是真正的驗證
3. **不改無關的東西**：範圍控制是 agent 最容易失控的地方
4. **對話後更新規則**：把發現的知識沉澱到 CLAUDE.md

## Ratchet 原則的來源

Mitchell Hashimoto 原話：

> 「Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.」

Addy Osmani 的延伸（[AI-assisted coding: building better LLM habits](https://addyosmani.com/blog/ai-assisted-coding/)）：

> 「Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong.」

這是貫穿本課程的核心工程哲學：Harness 不是預先設計的，而是從失敗中沉澱出來的。

## Claude Code 官方文件索引

| 主題 | URL |
|------|-----|
| 快速開始 | https://code.claude.com/docs |
| Memory（CLAUDE.md + Auto Memory）| https://code.claude.com/docs/en/memory |
| Hooks | https://code.claude.com/docs/en/hooks |
| Sandboxing | https://code.claude.com/docs/en/sandboxing |
| Permissions | https://code.claude.com/docs/en/permissions |
| Sub-Agents | https://code.claude.com/docs/en/sub-agents |
| MCP | https://code.claude.com/docs/en/mcp |
| Skills | https://code.claude.com/docs/en/skills |
| How Claude Code Works | https://code.claude.com/docs/en/how-claude-code-works |
| Common Workflows | https://code.claude.com/docs/en/common-workflows |
