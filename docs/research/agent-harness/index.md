# agent-harness/INDEX.md

> **Type:** wiki:compiled — Harness 評估框架 + 深度研究；consumer: `harness-meta` skill  
> **Updated**: 2026-06-03 | **Files**: 16 docs  
> **Query pattern**: BRAIN.md → 本表 → 具體文件

---

## 核心文件（直接查詢）

| 文件 | 用途 | 查詢時機 |
|------|------|---------|
| [HARNESS-CARD.md](HARNESS-CARD.md) | CAR 14-component scorecard（當前 13.0/14 = 92.9%）| 想知道 harness 健康度 |
| [KNOWLEDGE-MAP.md](KNOWLEDGE-MAP.md) | GBrain typed-edge 跨源知識地圖；共識萃取 | 想知道 harness 理論共識 |
| [RESEARCH.md](RESEARCH.md) | 22 資源合成；PGE 架構學理 | 想找 harness 設計依據 |
| [RATCHET.md](RATCHET.md) | Rule→Hook 升格決策手冊；before/after 紀錄 | 想把經驗固化成規則 |
| [BENCHMARK.md](BENCHMARK.md) | Harness eval 數據彙整 | 想比較 harness 版本效能 |
| [SURVEY.md](SURVEY.md) | Agent harness 工具生態調查 | 想了解業界工具選型 |
| [dynamic-workflows-harness-2026-06-03.md](dynamic-workflows-harness-2026-06-03.md) | Dynamic workflows harness 三層拆解（控制/agent/協調平面）+ 六大 pattern + runtime API 簽章 | 想懂 workflow 帶來的 harness 是什麼 |
| [opus48-systemprompt-harness-2026-06-03.md](opus48-systemprompt-harness-2026-06-03.md) | v2.1.154–161 CHANGELOG × Opus 4.8 六大行為位移 × harness 補償因果鏈;workflow 關鍵字演進史 | 想懂 Opus 4.8 如何驅動 system-prompt/harness 改動 |

## Eval 紀錄

> 逐日 eval 快照（eval-2026-05-19/20/25/29.md）已於 2026-06-03 清理（過期 + 已被取代）。
> 現行 harness 分數與數據以下列常駐檔為準：

| 文件 | 內容 |
|------|------|
| [BENCHMARK.md](BENCHMARK.md) | Harness eval 數據彙整（healthcheck / CAR score）|
| [RATCHET.md](RATCHET.md) | 各 cycle before/after 紀錄（含最新 harness-meta:full 13.0/14）|
| [HARNESS-CARD.md](HARNESS-CARD.md) | 當前 harness 快照（score / token / hooks）|

## Autoresearch 深度報告（2026-05-08）

| 文件 | 核心數據 |
|------|---------|
| [llm-routing-industrial-cases.md](llm-routing-industrial-cases.md) | RouteLLM 75% cheaper；Martian 300+ 企業；17.2x error amplification |
| [harness-evaluation-metrics-2026.md](harness-evaluation-metrics-2026.md) | GPT-5.5 harness +25.7pp；Meta-Harness LawBench +16pp |

## Typed Edges

| Edge | From | To |
|------|------|----|
| `extends` | `.claude/skills/harness-meta/` | RESEARCH.md |
| `implements` | `.claude/rules/subagent-strategy.md` | KNOWLEDGE-MAP.md |
| `references` | `harness-model-fit.json` | HARNESS-CARD.md |
| `cited-by` | `research/papers/2024-06-20-routellm-*` | llm-routing-industrial-cases.md |
| `derived-from` | `research/tweets/2026-06-02-@trq212-367865.md` | dynamic-workflows-harness-2026-06-03.md |
| `grounds` | `code.claude.com/docs/zh-TW/workflows` | dynamic-workflows-harness-2026-06-03.md |
| `derived-from` | `Piebald-AI/claude-code-system-prompts CHANGELOG` | opus48-systemprompt-harness-2026-06-03.md |
| `extends` | dynamic-workflows-harness-2026-06-03.md | opus48-systemprompt-harness-2026-06-03.md |
