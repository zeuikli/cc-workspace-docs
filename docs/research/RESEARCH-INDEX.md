---
title: "Research Index — 知識地圖"
type: documentation
---

# Research Index — 知識地圖

> 導覽層：O(1) 定位各目錄，詳細內容見各目錄 INDEX.md  
> 更新日期：2026-06-06
> **Agent 入口**：先讀 `../BRAIN.md`（全域 lookup），再用本表定位 research/ 子目錄  
> **子目錄 -> Skill 對應：**  
> `agent-harness/` -> `/harness-meta` · `ai-articles/` -> `/research-hub` · `career-wiki/` -> `/autoresearch:wiki`  
> `ai-news/` -> overnight-research · `papers/` -> deep-research · `best-practices/` -> research-hub:audit

---

## 目錄總覽

| 目錄 | 檔案數 | 說明 | INDEX |
|------|--------|------|-------|
| `ai-news/` | 600+ | 每日 AI 新聞 digest（16 個 newsletter 來源）| [-> INDEX.md](ai-news/INDEX.md) |
| `ai-articles/` | 220 | scored（50）/ inbox 已清空 / low-score（20）| [-> INDEX.md](ai-articles/INDEX.md) |
| `tweets/` | 188 | Twitter 重要技術 thread 歸檔 | [-> INDEX.md](tweets/INDEX.md) |
| `substack-thestevekoh/` | 171 | Steve Koh Substack 全文歸檔 | [-> INDEX.md](substack-thestevekoh/INDEX.md) |
| `papers/` | 183 | arXiv / 學術論文（PDF + Markdown）| [-> INDEX.md](papers/INDEX.md) |
| `agent-harness/` | 80 | Harness 深度研究 + eval + benchmark | [-> INDEX.md](agent-harness/INDEX.md) |
| `career-wiki/` | 53 | 8 段職涯 × 36 pages（供 zeuik-senior-architect）| [-> INDEX.md](career-wiki/INDEX.md) |
| `reports/` | 95 | 合成報告 / Gap analysis / Deep research 輸出 | [-> INDEX.md](reports/INDEX.md) |
| `best-practices/` | 32 | Claude Code 最佳實踐研究 | [-> INDEX.md](best-practices/INDEX.md) |
| `claude-blog/` | 14 | Anthropic 官方 blog / docs 歸檔 | [-> INDEX.md](claude-blog/INDEX.md) |
| `evals/` | 13 | Harness eval runs + baseline | [-> INDEX.md](evals/INDEX.md) |
| `prompts/` | 9 | 研究專用 system prompts | [-> INDEX.md](prompts/INDEX.md) |
| `videos/` | 7 | Podcast / 影片摘要 | [-> INDEX.md](videos/INDEX.md) |
| `templates/` | 3 | 文件模板 | [-> INDEX.md](templates/INDEX.md) |
| `medium/` | 1 | Medium 文章（付費牆部分截斷）| [-> INDEX.md](medium/INDEX.md) |
| ~~`archive/`~~ | — | 已刪除（2026-06-01）| — |

---

## 心智圖

```mermaid
mindmap
  root(AI Engineering\nWorkspace Knowledge)
    能力邊界理解
      Jaggedness(on-rails vs off-rails)
        tweets/INDEX.md @stephzhan-519769
      Context Engineering
        tweets/INDEX.md @karpathy-607626
      Software 3.0(新計算範式)
        tweets/INDEX.md @stephzhan
    品質控制
      Agentic Engineering 四維框架
        tweets/INDEX.md @stephzhan-331722
      AI 程式碼缺陷
        tweets/INDEX.md @stephzhan-075818
      Deep Review
        healthcheck.sh
    人機協作角色
      Goal-Driven Execution
        refs/karpathy-mnilax-best-solution.md
      Advisor 模式
        rules/subagent-strategy.md
    Workspace 架構
      Harness Design
        agent-harness/INDEX.md
      Sub-agent Strategy
        rules/subagent-strategy.md
      Context Management
        rules/context-management.md
    Token / 成本優化
      Prompt Caching
        tweets/INDEX.md @trq212-750509
      Token 壓縮
        rules/output-discipline.md
    Ops / SRE 實踐
      career-wiki
        career-wiki/INDEX.md
      FinOps
        career-wiki/pages/finops-*.md
      Incident Analysis
        playbooks/
```

---

## 主題索引（精選 × 整合狀態）

> 完整清單見各目錄 INDEX.md。本表只列「已整合」或「待整合高優先」項目。

### AI Engineering Fundamentals

| 文章 | 評分 | 整合狀態 | 核心洞見 |
|------|------|---------|---------|
| [Karpathy Context Engineering](tweets/2025-06-25-@karpathy-607626.md) | 9.2 | ✅ -> context-management.md | Context = 工程紀律，不是 prompt 優化 |
| [Jaggedness on-rails/off-rails](tweets/2026-04-29-@stephzhan-519769.md) | 5.6 | 📋 -> 待補 subagent-strategy.md | On-rails 信任高委派，off-rails 需人驗證 |
| [Software 3.0](tweets/2026-04-29-@stephzhan-587987.md) | 5.1 | 🗂 Skip（Karpathy 原文更完整）| 問「以前根本不可能的是什麼？」|
| [Karpathy No Priors](tweets/2026-01-26-@karpathy-522876.md) | — | — | Software 1.0/2.0/3.0 完整框架 |

-> 更多 tweets：[tweets/INDEX.md](tweets/INDEX.md)

### Agentic Engineering Quality

| 文章 | 評分 | 整合狀態 | 核心洞見 |
|------|------|---------|---------|
| [四維框架（vibe vs agentic）](tweets/2026-04-29-@stephzhan-331722.md) | 6.0 | 📋 -> 待加 quality.md | security/reliability/maintainability/taste |
| [AI 程式碼四大缺陷](tweets/2026-04-29-@stephzhan-075818.md) | 6.6 | 📋 -> 待加 karpathy-principles.md | bloated/copy-paste/brittle/abstraction |
| [Skill Authoring Patterns](ai-articles/scored/2026-04-20-skill-authoring-patterns.md) | — | ✅ -> skill-authoring.md | 14 設計模式，description 預算 |
| [Claude Opus 4.7 System Prompt](ai-articles/scored/2026-04-20-claude-opus47-system-prompt.md) | — | ✅ -> anthropic-insights.md | 工具呼叫次數、著作權規則 |

-> 更多 ai-articles：[ai-articles/INDEX.md](ai-articles/INDEX.md)

### 人機協作角色分工

| 文章 | 評分 | 整合狀態 | 核心洞見 |
|------|------|---------|---------|
| [外包思考 vs 理解](tweets/2026-04-29-@stephzhan-937683.md) | 5.9 | 🗂 Skip（理念已在 core.md）| 不可外包：what matters / true / build / why |
| [Thariq prompt caching 設計](tweets/2026-02-04-@trq212-750509.md) | — | ✅ -> context-management.md | Static first, tools 不能 mid-session 改變 |
| [Boris session forking](tweets/2026-01-31-@bcherny-321619.md) | — | ✅ -> session-management.md | /branch / /btw / /focus |

---

## 各目錄快查（Agent 跳轉）

### ai-articles -> [INDEX.md](ai-articles/INDEX.md)
50 篇 scored（Karpathy×Mnilax 框架）；含整合狀態（✅/📋/🔵/🗂）

### agent-harness -> [INDEX.md](agent-harness/INDEX.md)
14 docs：HARNESS-CARD（92.9%）· KNOWLEDGE-MAP · RESEARCH · RATCHET + eval 紀錄

### papers -> [INDEX.md](papers/INDEX.md)
125 篇 × 11 domains：Memory / Harness / Agent-Arch / Multi-Agent / Routing / RAG / Perf / Safety / Benchmarks / Context / Other

### reports -> [INDEX.md](reports/INDEX.md)
37 報告 × 6 topics：Harness / Memory / Auto-load / Workspace-Gap / Skill / Best-Practices

### career-wiki -> [INDEX.md](career-wiki/INDEX.md)
36 pages × 10 domains；Lint 100/100；consumer: `zeuik-senior-architect`

### tweets -> [INDEX.md](tweets/INDEX.md)
183 items × Author（50+）× 10 topic categories

### best-practices -> [INDEX.md](best-practices/INDEX.md)
28 docs：Official + community Claude Code best practices

### claude-blog -> [INDEX.md](claude-blog/INDEX.md)
~76 articles × 5 categories：claude-code / agents / announcements / enterprise-ai / docs

### ai-news -> [INDEX.md](ai-news/INDEX.md)
600+ files；16 newsletters；digest types：combined / deepsrt / devops

### substack-thestevekoh -> [INDEX.md](substack-thestevekoh/INDEX.md)
171 articles × 6 themes；2024-02 -> 2025-12+

### videos -> [INDEX.md](videos/INDEX.md)
7 影片：Karpathy × Sequoia × Boris × nateherk × AI Engineer × Lenny's

### prompts -> [INDEX.md](prompts/INDEX.md)
9 system prompts × 適用 skill

### templates -> [INDEX.md](templates/INDEX.md)
3 研究自動化模板

### evals -> [INDEX.md](evals/INDEX.md)
Baseline + 5 eval runs（2026-05-29 起）

### medium -> [INDEX.md](medium/INDEX.md)
1 篇（vgod 付費牆預覽）

---

## 待整合行動（按優先序）

| 行動 | 來源 | 目標位置 | 優先 |
|------|------|---------|------|
| on-rails/off-rails 任務分類矩陣 | [stephzhan-519769](tweets/2026-04-29-@stephzhan-519769.md) | `.claude/rules/subagent-strategy.md` | 🔴 |
| 四維品質 checklist | [stephzhan-331722](tweets/2026-04-29-@stephzhan-331722.md) | `.claude/rules/quality.md` | 🔴 |
| AI 程式碼四大缺陷反模式 | [stephzhan-075818](tweets/2026-04-29-@stephzhan-075818.md) | `.claude/rules/karpathy-principles.md` | 🔴 |
| harness-engineering-ai-warmwater 整合 | [ai-articles scored 7.25](ai-articles/scored/2026-04-02-harness-engineering-ai-warmwater.md) | `.claude/skills/harness-meta/` | 🟡 |

---

## Knowledge Graph — Typed Edges（GBrain 模式）

| From | Edge | To | 說明 |
|------|------|----|------|
| `.claude/rules/context-management.md` | `implements` | [tweets/@karpathy-607626](tweets/2025-06-25-@karpathy-607626.md) | Static-first、NLAH 原則 |
| `.claude/rules/subagent-strategy.md` | `implements` | [agent-harness/KNOWLEDGE-MAP.md](agent-harness/KNOWLEDGE-MAP.md) | Fan-out ≤4、centralized 拓撲 |
| `.claude/rules/core.md` | `inspired_by` | [tweets/@bcherny](tweets/2026-01-31-@bcherny-321619.md) | Rule 5 LLM-只做判斷原則 |
| `.claude/skills/autoresearch/` | `implements` | [career-wiki/raw/karpathy-llm-wiki-gist.md](career-wiki/raw/karpathy-llm-wiki-gist.md) | Ingest/Query/Lint 三操作 |
| `research/career-wiki/` | `implements` | Karpathy LLM Wiki (3-layer) | Raw -> Wiki -> Schema 完整三層 |
| `.claude/agents/zeuik-senior-architect.md` | `references` | [career-wiki/INDEX.md](career-wiki/INDEX.md) | 架構決策時直讀 career-wiki |
| `.claude/refs/advisor-tool-api.md` | `implements` | [papers/agentopt-2604-06296](papers/2026-04-07-agentopt-client-side-optimization.md) | Advisor Strategy 學理依據 |
| `.claude/hooks/pre-compact.sh` | `implements` | [papers/useful-memories-2605-12978](papers/2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978.md) | Batch Gate 100% vs Stream 46% |
| `.claude/skills/skill-evolution/` | `inspired_by` | [agent-harness/KNOWLEDGE-MAP.md](agent-harness/KNOWLEDGE-MAP.md) | Hermes 自主進化 |
| `.claude/skills/harness-meta/` | `extends` | [agent-harness/RESEARCH.md](agent-harness/RESEARCH.md) | 22 資源合成 -> 操作化 skill |
| `ai-articles/scored/2026-04-02-harness-engineering-ai-warmwater.md` | `references` | `.claude/skills/harness-meta/` | Harness 五維度（7.25 分，待整合）|
| `career-wiki/raw/README.md` | `implements` | Karpathy LLM Wiki (Raw immutable) | Raw 層：LLM 只讀不改 |
| `BRAIN.md` | `indexes` | `research/*/INDEX.md` | Agent O(1) lookup 入口 |

_最後更新：2026-06-02_
