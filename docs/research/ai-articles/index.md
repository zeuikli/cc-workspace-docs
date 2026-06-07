# ai-articles/INDEX.md

> **Type:** raw:indexed — 48 scored articles；Karpathy×Mnilax 評分框架  
> **Updated**: 2026-06-02  
> **Query pattern**: BRAIN.md → 本表（Topic / 整合狀態）→ `scored/<date>-<slug>.md`

---

## 整合狀態快查

| 符號 | 說明 |
|------|------|
| ✅ | 已整合到指定 skill/rule/ref |
| 📋 | 分數 > 6，待整合 |
| 🔵 | 已 scored，整合狀態未確認 |
| 🗂 | low-score（< 6 分）或重複 |

---

## 特殊文件（scored/ 目錄內的索引性質文件）

| 檔案 | 說明 |
|------|------|
| [AGENTS-MD-RESEARCH-INDEX.md](scored/AGENTS-MD-RESEARCH-INDEX.md) | AGENTS.md 主題文章去重決策記錄（4 篇比較 + 保留決策）|
| [2026-03-01-swe-bench-pro-morphllm.md](scored/2026-03-01-swe-bench-pro-morphllm.md) | SWE-bench Pro（morphllm 分析）|

---

## Topic 索引

| Topic | 代表文章 | 數量 |
|-------|---------|------|
| [Harness Engineering](#harness-engineering) | NLAH · Datadog · anatomy-of-harness | 22 |
| [AGENTS.md / Skill Design](#agentsmd--skill-design) | addyosmani · augmentcode · skill-authoring | 7 |
| [Claude Code / Anthropic](#claude-code--anthropic) | boris-verification · claude-code-best-practices · postmortem | 8 |
| [Multi-agent / AgentFlow](#multi-agent--agentflow) | agentflow · langchain-deep-agents | 3 |
| [Model / Optimization](#model--optimization) | hone-haiku-20pp · agentopt · v4a-diff | 5 |
| [MCP / Tools](#mcp--tools) | github-mcp-lazy-loading · adnan-ai-control-plane | 2 |
| [Best Practices](#best-practices) | simonwillison · martinfowler-feedforward | 3 |

---

## Harness Engineering

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2025-12-11 | [confucius-code-agent](scored/2025-12-11-confucius-code-agent.md) | — | 🔵 |
| 2026-02-01 | [agent-harness-2026-philschmid](scored/2026-02-01-agent-harness-2026-philschmid.md) | — | 🔵 |
| 2026-02-11 | [openai-harness-engineering-codex](scored/2026-02-11-openai-harness-engineering-codex.md) | — | 🔵 |
| 2026-02-20 | [harness-engineering-interpretations-zenn-kenimo](scored/2026-02-20-harness-engineering-interpretations-zenn-kenimo.md) | — | 🔵 |
| 2026-02-20 | [harness-engineering-overview-smartscope](scored/2026-02-20-harness-engineering-overview-smartscope.md) | — | 🔵 |
| 2026-03-01 | [claude-code-harness-runtime-architecture](scored/2026-03-01-claude-code-harness-runtime-architecture-pasqualepillitteri.md) | — | 🔵 |
| 2026-03-01 | [harness-engineering-best-practices-nyosegawa](scored/2026-03-01-harness-engineering-best-practices-2026-nyosegawa.md) | — | 🔵 |
| 2026-03-09 | [datadog-harness-first-verification-loop](scored/2026-03-09-datadog-harness-first-verification-loop.md) | — | ✅ harness-meta |
| 2026-03-26 | [natural-language-agent-harnesses-nlah](scored/2026-03-26-natural-language-agent-harnesses-nlah.md) | — | ✅ harness-meta |
| 2026-03-30 | [meta-harness-optimization](scored/2026-03-30-meta-harness-optimization.md) | — | 🔵 |
| 2026-04-01 | [anatomy-of-agent-harness](scored/2026-04-01-anatomy-of-agent-harness.md) | — | 🔵 |
| 2026-04-01 | [agentic-harness-engineering-decodingai](scored/2026-04-01-agentic-harness-engineering-decodingai.md) | — | 🔵 |
| 2026-04-01 | [ai-coding-harness-agents-2026-jock](scored/2026-04-01-ai-coding-harness-agents-2026-jock.md) | — | 🔵 |
| 2026-04-01 | [start-harness-engineering-caddi](scored/2026-04-01-start-harness-engineering-caddi.md) | — | 🔵 |
| 2026-04-02 | [martinfowler-harness-engineering-feedforward-feedback](scored/2026-04-02-martinfowler-harness-engineering-feedforward-feedback.md) | — | 🔵 |
| 2026-04-02 | [harness-engineering-ai-warmwater](scored/2026-04-02-harness-engineering-ai-warmwater.md) | 7.25 | 📋 → harness-meta checklist |
| 2026-04-07 | [agent-harness-survey](scored/2026-04-07-agent-harness-survey.md) | — | 🔵 |
| 2026-04-15 | [claude-code-harness-engineering-zenn-sasadango](scored/2026-04-15-claude-code-harness-engineering-zenn-sasadango.md) | — | 🔵 |
| 2026-04-23 | [harness-engineering-car-framework](scored/2026-04-23-harness-engineering-car-framework.md) | — | 🔵 |
| 2026-05-09 | [anthropic-harness-design-long-running-apps](scored/2026-05-09-anthropic-harness-design-long-running-apps.md) | — | 🔵 |
| 2026-05-09 | [cursor-continually-improving-agent-harness](scored/2026-05-09-cursor-continually-improving-agent-harness.md) | — | 🔵 |
| 2026-05-09 | [langchain-deep-agents-harness-engineering](scored/2026-05-09-langchain-deep-agents-harness-engineering.md) | — | 🔵 |

---

## AGENTS.md / Skill Design

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2026-02-23 | [addyosmani-agents-md](scored/2026-02-23-addyosmani-agents-md.md) | — | 🔵 |
| 2026-04-20 | [skill-authoring-patterns](scored/2026-04-20-skill-authoring-patterns.md) | — | ✅ skill-authoring.md |
| 2026-04-22 | [agents-md-design-augment-code](scored/2026-04-22-agents-md-design-augment-code.md) | — | 🔵 |
| 2026-04-29 | [agents-md-haiku-opus-taiwan](scored/2026-04-29-agents-md-haiku-opus-taiwan.md) | — | 🔵 |
| 2026-05-02 | [augmentcode-how-to-write-good-agents-md](scored/2026-05-02-augmentcode-how-to-write-good-agents-md.md) | — | 🔵 |
| 2026-05-02 | [cobus-greyling-auto-agentic-harness](scored/2026-05-02-cobus-greyling-auto-agentic-harness.md) | — | 🔵 |
| 2026-05-10 | [perplexity-agent-skills](scored/2026-05-10-designing-refining-and-maintaining-agent-skills-at-perplexity.md) | — | 🔵 |

---

## Claude Code / Anthropic

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2026-04-20 | [claude-opus47-system-prompt](scored/2026-04-20-claude-opus47-system-prompt.md) | — | ✅ anthropic-insights.md |
| 2026-04-24 | [cat-wu-ai-pm-anthropic](scored/2026-04-24-cat-wu-ai-pm-anthropic.md) | — | 🔵 |
| 2026-05-06 | [simonwillison-vibe-coding-agentic-engineering](scored/2026-05-06-simonwillison-vibe-coding-agentic-engineering.md) | — | 🔵 |
| 2026-05-09 | [anthropic-april-23-postmortem-claude-code-quality](scored/2026-05-09-anthropic-april-23-postmortem-claude-code-quality.md) | — | 🔵 |
| 2026-05-09 | [terminal-bench-2-0](scored/2026-05-09-terminal-bench-2-0.md) | — | 🔵 |
| 2026-05-09 | [arbiter-system-prompt-interference](scored/2026-05-09-arbiter-system-prompt-interference.md) | — | 🔵 |
| 2026-05-12 | [boris-cherny-verification-loops](scored/2026-05-12-boris-cherny-verification-loops.md) | — | ✅ harness-meta |
| 2026-05-12 | [claude-code-best-practices](scored/2026-05-12-claude-code-best-practices.md) | — | 🔵 |

---

## Multi-agent / AgentFlow

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2026-04-22 | [agentflow-multi-agent-harnesses](scored/2026-04-22-agentflow-multi-agent-harnesses.md) | — | 🔵 |
| 2026-04-23 | [adnan-masood-ai-control-plane](scored/2026-04-23-adnan-masood-ai-control-plane.md) | — | 🔵 |
| 2026-05-09 | [langchain-deep-agents-harness-engineering](scored/2026-05-09-langchain-deep-agents-harness-engineering.md) | — | 🔵（上方 Harness 區已列）|

---

## Model / Optimization

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2026-02-28 | [codex-vs-claude-code-morphllm](scored/2026-02-28-codex-vs-claude-code-morphllm.md) | — | 🔵 |
| 2026-03-01 | [agent-engineering-morphllm](scored/2026-03-01-agent-engineering-morphllm.md) | — | 🔵 |
| 2026-04-07 | [agentopt-client-side-optimization](scored/2026-04-07-agentopt-client-side-optimization.md) | — | ✅ refs/advisor-tool-api.md |
| 2026-04-19 | [hone-haiku-20pp](scored/2026-04-19-hone-haiku-20pp.md) | — | 🔵 |
| 2026-05-09 | [v4a-diff-format-codex-post-training](scored/2026-05-09-v4a-diff-format-codex-post-training.md) | — | 🔵 |

---

## MCP / Tools

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2026-03-05 | [opendev-terminal-agents](scored/2026-03-05-opendev-terminal-agents.md) | — | 🔵 |
| 2026-05-12 | [github-7336-mcp-lazy-loading](scored/2026-05-12-github-7336-mcp-lazy-loading.md) | — | 🔵 |

---

## Best Practices

| 日期 | 文章 | 分數 | 整合狀態 |
|------|------|------|---------|
| 2026-04-02 | [martinfowler-harness-engineering-feedforward-feedback](scored/2026-04-02-martinfowler-harness-engineering-feedforward-feedback.md) | — | 🔵（上方 Harness 區已列）|
| 2026-03-12 | [skill-issue-harness-engineering](scored/2026-03-12-skill-issue-harness-engineering.md) | — | 🔵 |
| 2026-05-06 | [simonwillison-vibe-coding-agentic-engineering](scored/2026-05-06-simonwillison-vibe-coding-agentic-engineering.md) | — | 🔵（上方 Claude Code 區已列）|

---

## Low-score 存檔（inbox/low-score/）

| 文章 | 分數 | 原因 |
|------|------|------|
| 2025-07-24-context-engineering-ai-agent-ikala | 5.1 | 二手整理，已被 context-management.md 涵蓋 |
| 2025-10-27-agentic-context-engineering-datasciocean | 6.55 | 原論文已在 papers/；重複 |
| 2025-11-06-agentic-context-engineering-warmwater | 6.55 | 同上 |
| + 17 篇 2025-06 至 2025-12 低分文章 | < 6 | 各原因詳見各檔案 |
