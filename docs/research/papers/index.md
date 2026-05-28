---
title: "Academic Paper Archive"
type: index
---

# Academic Paper Archive

> **Type:** raw:indexed — academic papers on LLM and AI agents (read-only source layer)

97 篇學術論文存檔：.md 摘要。涵蓋 2021–2026 年 LLM 與 AI agent 研究。

**2026-05-25 v5 更新**：新增 12 篇（記憶架構 +6、多 agent 協調 +2、評估基準 +3、Harness +1）。

檔名格式：`YYYY-MM-DD-slug-arxiv-id.md`（arxiv ID 內嵌於檔名）

## Agent Query Patterns

```
"有沒有關於 multi-agent 協作的論文？"
  → grep -l "multi-agent\|Multi-Agent" research/papers/*.md | head -10

"最新的 2026 年論文有哪些？"
  → ls research/papers/2026-*.md

"找 RAG 相關論文"
  → grep -l "RAG\|retrieval" research/papers/*.md
```

## 主題分類

| 主題 | 說明 |
|------|------|
| LLM Memory | 長期記憶、KV Cache、RAG 機制 |
| Speculative Decoding | 推理加速、draft model 策略 |
| Agent Architectures | ReAct / CoT / Tool-use / Planning |
| Multi-agent | 多 agent 協作框架、Fan-out 拓撲 |
| AI Values & Safety | 對齊、安全評估、Constitutional AI |
| Routing | LLM routing 策略、mixture-of-experts |

---

## 全部論文列表（97 篇）

### 2021 年

| 檔案 |
|------|
| [2021-09-21-splade-v2-sparse-lexical-expansion-2109-10086.md](./2021-09-21-splade-v2-sparse-lexical-expansion-2109-10086) |

### 2023 年

| 檔案 |
|------|
| [2023-03-20-reflexion-verbal-reinforcement-learning-2303-11366.md](./2023-03-20-reflexion-verbal-reinforcement-learning-2303-11366) |
| [2023-04-07-generative-agents-simulacra-human-behavior-2304-03442.md](./2023-04-07-generative-agents-simulacra-human-behavior-2304-03442) |
| [2023-04-26-scm-self-controlled-memory-2304-13343.md](./2023-04-26-scm-self-controlled-memory-2304-13343) |
| [2023-05-17-memorybank-long-term-memory-2305-10250.md](./2023-05-17-memorybank-long-term-memory-2305-10250) |
| [2023-05-25-voyager-open-ended-embodied-agent-2305-16291.md](./2023-05-25-voyager-open-ended-embodied-agent-2305-16291) |
| [2023-08-20-expel-llm-agents-experiential-learners-2308-10144.md](./2023-08-20-expel-llm-agents-experiential-learners-2308-10144) |
| [2023-09-05-coala-cognitive-architectures-language-agents-2309-02427.md](./2023-09-05-coala-cognitive-architectures-language-agents-2309-02427) |
| [2023-10-12-memgpt-llms-as-operating-systems-2310-08560.md](./2023-10-12-memgpt-llms-as-operating-systems-2310-08560) |
| [2023-12-18-retrieval-augmented-generation-survey-2312-10997.md](./2023-12-18-retrieval-augmented-generation-survey-2312-10997) |

### 2024 年

| 檔案 |
|------|
| [2024-04-21-survey-memory-mechanism-llm-agents-2404-13501.md](./2024-04-21-survey-memory-mechanism-llm-agents-2404-13501) |
| [2024-05-06-swe-agent-agent-computer-interfaces-enable-automated-software-engineering-2405.15793.md](./2024-05-06-swe-agent-agent-computer-interfaces-enable-automated-software-engineering-2405.15793) |
| [2024-05-17-latent-state-estimation-ui-agents-2405.11120.md](./2024-05-17-latent-state-estimation-ui-agents-2405.11120) |
| [2024-05-23-hipporag-neurobiological-memory-2405-14831.md](./2024-05-23-hipporag-neurobiological-memory-2405-14831) |
| [2024-06-20-routellm-learning-to-route-llms-2406.18665.md](./2024-06-20-routellm-learning-to-route-llms-2406.18665) |
| [2024-06-20-step-back-profiling-personalized-scientific-writing-2406.14275.md](./2024-06-20-step-back-profiling-personalized-scientific-writing-2406.14275) |

### 2025 年

| 檔案 |
|------|
| [2025-02-17-amem-agentic-memory-llm-agents-2502-12110.md](./2025-02-17-amem-agentic-memory-llm-agents-2502-12110) |
| [2025-03-03-multiagentbench-collaboration-competition-2503-01935.md](./2025-03-03-multiagentbench-collaboration-competition-2503-01935) |
| [2025-03-07-which-economic-tasks-ai-claude-conversations-2503-04761.md](./2025-03-07-which-economic-tasks-ai-claude-conversations-2503-04761) |
| [2025-04-21-values-in-the-wild-claude-interactions-2504-15236.md](./2025-04-21-values-in-the-wild-claude-interactions-2504-15236) |
| [2025-04-22-human-memory-to-ai-memory-survey-2504-15965.md](./2025-04-22-human-memory-to-ai-memory-survey-2504-15965) |
| [2025-04-28-mem0-production-long-term-memory-2504-19413.md](./2025-04-28-mem0-production-long-term-memory-2504-19413) |
| [2025-05-01-rethinking-memory-llm-agents-operations-2505-00675.md](./2025-05-01-rethinking-memory-llm-agents-operations-2505-00675) |
| [2025-05-09-llms-get-lost-multi-turn-2505-06120.md](./2025-05-09-llms-get-lost-multi-turn-2505-06120) |
| [2025-05-30-memory-os-ai-agent.md](./2025-05-30-memory-os-ai-agent) |
| [2025-06-08-decreasing-value-chain-of-thought-2506-07142.md](./2025-06-08-decreasing-value-chain-of-thought-2506-07142) |
| [2025-07-29-memtool-short-term-memory-dynamic-tool-calling-2507.21428.md](./2025-07-29-memtool-short-term-memory-dynamic-tool-calling-2507.21428) |
| [2025-08-01-blueprint-first-model-second-2508.02721.md](./2025-08-01-blueprint-first-model-second-2508.02721) |
| [2025-08-01-rcr-router-role-aware-context-routing-2508.04903.md](./2025-08-01-rcr-router-role-aware-context-routing-2508.04903) |
| [2025-09-21-swe-bench-pro-long-horizon-2509-16941.md](./2025-09-21-swe-bench-pro-long-horizon-2509-16941) |
| [2025-10-25-prompting-inversion-2510-22251.md](./2025-10-25-prompting-inversion-2510-22251) |
| [2025-11-07-ock-bench-reasoning-efficiency-overthinking-2511-05722.md](./2025-11-07-ock-bench-reasoning-efficiency-overthinking-2511-05722) |
| [2025-11-19-anthropic-economic-index-geographic-adoption-2511-15080.md](./2025-11-19-anthropic-economic-index-geographic-adoption-2511-15080) |
| [2025-12-11-confucius-code-agent-scalable.md](./2025-12-11-confucius-code-agent-scalable) |
| [2025-12-14-hindsight-agent-memory-retain-recall-reflect-2512-12818.md](./2025-12-14-hindsight-agent-memory-retain-recall-reflect-2512-12818) |
| [2025-12-31-recursive-language-models-2512-24601.md](./2025-12-31-recursive-language-models-2512-24601) |

### 2026 年 Q1

| 檔案 |
|------|
| [2026-01-05-agentic-memory-unified-ltm-stm-2601-01885.md](./2026-01-05-agentic-memory-unified-ltm-stm-2601-01885) |
| [2026-01-07-what-matters-safety-alignment-2601-03868.md](./2026-01-07-what-matters-safety-alignment-2601-03868) |
| [2026-01-08-gpt5-system-card-2601-03267.md](./2026-01-08-gpt5-system-card-2601-03267) |
| [2026-01-13-from-rows-to-reasoning-2601-08741.md](./2026-01-13-from-rows-to-reasoning-2601-08741) |
| [2026-01-17-terminal-bench-2601-11868.md](./2026-01-17-terminal-bench-2601-11868) |
| [2026-01-27-disempowerment-patterns-real-world-llm-2601-19062.md](./2026-01-27-disempowerment-patterns-real-world-llm-2601-19062) |
| [2026-01-31-dont-break-cache-prompt-caching-2601-06007.md](./2026-01-31-dont-break-cache-prompt-caching-2601-06007) |
| [2026-02-03-multi-agent-llm-frameworks-benchmark-2602-03128.md](./2026-02-03-multi-agent-llm-frameworks-benchmark-2602-03128) |
| [2026-02-11-openai-harness-engineering-codex.md](./2026-02-11-openai-harness-engineering-codex) |
| [2026-02-13-skills-bench-agent-skills-2602-12670.md](./2026-02-13-skills-bench-agent-skills-2602-12670) |
| [2026-02-16-configuring-agentic-coding-tools-2602-14690.md](./2026-02-16-configuring-agentic-coding-tools-2602-14690) |
| [2026-02-23-addyosmani-agents-md.md](./2026-02-23-addyosmani-agents-md) |
| [2026-03-03-benchmarking-emergent-coordination-moltbook-2603-03555.md](./2026-03-03-benchmarking-emergent-coordination-moltbook-2603-03555) |
| [2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md](./2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814) |
| [2026-03-05-opendev-terminal-agents-scaffolding.md](./2026-03-05-opendev-terminal-agents-scaffolding) |
| [2026-03-08-memory-autonomous-llm-agents-survey-2603-07670.md](./2026-03-08-memory-autonomous-llm-agents-survey-2603-07670) |
| [2026-03-09-multi-agent-memory-computer-architecture-2603-10062.md](./2026-03-09-multi-agent-memory-computer-architecture-2603-10062) |
| [2026-03-12-skill-issue-harness-engineering.md](./2026-03-12-skill-issue-harness-engineering) |
| [2026-03-17-chronos-temporal-aware-conversational-agents-2603-16862.md](./2026-03-17-chronos-temporal-aware-conversational-agents-2603-16862) |
| [2026-03-20-agentic-harness-real-world-compilers-2603-20075.md](./2026-03-20-agentic-harness-real-world-compilers-2603-20075) |
| [2026-03-25-natural-language-agent-harnesses-2603-25723.md](./2026-03-25-natural-language-agent-harnesses-2603-25723) |
| [2026-03-26-natural-language-agent-harnesses-nlah.md](./2026-03-26-natural-language-agent-harnesses-nlah) |
| [2026-03-30-meta-harness-optimization-model-harnesses.md](./2026-03-30-meta-harness-optimization-model-harnesses) |
| [2026-03-31-aec-bench-multimodal-benchmark-agentic-systems.md](./2026-03-31-aec-bench-multimodal-benchmark-agentic-systems) |

### 2026 年 Q2（4 月）

| 檔案 |
|------|
| [2026-04-07-agent-harness-survey.md](./2026-04-07-agent-harness-survey) |
| [2026-04-07-agentopt-client-side-optimization.md](./2026-04-07-agentopt-client-side-optimization) |
| [2026-04-09-externalization-llm-agents-2604-08224.md](./2026-04-09-externalization-llm-agents-2604-08224) |
| [2026-04-10-composite-stem-expert-curated.md](./2026-04-10-composite-stem-expert-curated) |
| [2026-04-13-safeharness-lifecycle-security-2604-13630.md](./2026-04-13-safeharness-lifecycle-security-2604-13630) |
| [2026-04-14-dive-into-claude-code-design-space-2604-14228.md](./2026-04-14-dive-into-claude-code-design-space-2604-14228) |
| [2026-04-16-claude-opus-4-7-system-card.md](./2026-04-16-claude-opus-4-7-system-card) |
| [2026-04-17-security-long-term-memory-mnemonic-sovereignty-2604-16548.md](./2026-04-17-security-long-term-memory-mnemonic-sovereignty-2604-16548) |
| [2026-04-20-architectural-design-decisions-ai-agent-harnesses.md](./2026-04-20-architectural-design-decisions-ai-agent-harnesses) |
| [2026-04-21-cyber-defense-benchmark-threat-hunting-llm-2604-19533.md](./2026-04-21-cyber-defense-benchmark-threat-hunting-llm-2604-19533) |
| [2026-04-22-agentflow-synthesizing-multi-agent.md](./2026-04-22-agentflow-synthesizing-multi-agent) |
| [2026-04-22-harbor-automated-harness-optimization-2604-20938.md](./2026-04-22-harbor-automated-harness-optimization-2604-20938) |
| [2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087.md](./2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087) |
| [2026-04-23-gpt5-5-system-card.md](./2026-04-23-gpt5-5-system-card) |
| [2026-04-23-harness-engineering-language-agents-car.md](./2026-04-23-harness-engineering-language-agents-car) |
| [2026-04-29-last-harness-youll-ever-build-2604-21003.md](./2026-04-29-last-harness-youll-ever-build-2604-21003) |
| [2026-04-30-ahe-observability-driven-harness-2604-25850.md](./2026-04-30-ahe-observability-driven-harness-2604-25850) |

### 2026 年 Q2（5 月）

| 檔案 |
|------|
| [2026-05-04-heavyskill-heavy-thinking-inner-skill-2605-02396.md](./2026-05-04-heavyskill-heavy-thinking-inner-skill-2605-02396) |
| [2026-05-04-tscg-tool-schema-compilation-2605-04107.md](./2026-05-04-tscg-tool-schema-compilation-2605-04107) |
| [2026-05-05-coordination-architectural-layer-2605-03310.md](./2026-05-05-coordination-architectural-layer-2605-03310) |
| [2026-05-06-parness-automated-scientific-research-2605-05258.md](./2026-05-06-parness-automated-scientific-research-2605-05258) |
| [2026-05-10-calbench-coordination-privacy-tradeoffs-2605-09823.md](./2026-05-10-calbench-coordination-privacy-tradeoffs-2605-09823) |
| [2026-05-11-continual-harness-online-adaptation-2605-09998.md](./2026-05-11-continual-harness-online-adaptation-2605-09998) |
| [2026-05-12-acon-2510-00615.md](./2026-05-12-acon-2510-00615) |
| [2026-05-12-delta-mem-efficient-online-memory-llm-2605-12357.md](./2026-05-12-delta-mem-efficient-online-memory-llm-2605-12357) |
| [2026-05-12-harness-engineering-categorical-architecture-2605-12239.md](./2026-05-12-harness-engineering-categorical-architecture-2605-12239) |
| [2026-05-12-llmcompiler-icml-2024-2312-04511.md](./2026-05-12-llmcompiler-icml-2024-2312-04511) |
| [2026-05-12-lost-in-the-middle-2307-03172.md](./2026-05-12-lost-in-the-middle-2307-03172) |
| [2026-05-12-meta-harness-2603-28052.md](./2026-05-12-meta-harness-2603-28052) |
| [2026-05-13-ai-harness-engineering-runtime-substrate-2605-13357.md](./2026-05-13-ai-harness-engineering-runtime-substrate-2605-13357) |
| [2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978.md](./2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978) |
| [2026-05-14-is-grep-all-you-need-agentic-search-2605-15184.md](./2026-05-14-is-grep-all-you-need-agentic-search-2605-15184) |
| [2026-05-15-effective-harness-engineering-vesper-2605-15221.md](./2026-05-15-effective-harness-engineering-vesper-2605-15221) |
| [2026-05-18-code-as-agent-harness-2605-18747.md](./2026-05-18-code-as-agent-harness-2605-18747) |
| [2026-05-21-adapting-interface-not-model-life-harness-2605-22166.md](./2026-05-21-adapting-interface-not-model-life-harness-2605-22166) |
| [2026-05-23-cheating-agents-benchmark-manipulation-debugml.md](./2026-05-23-cheating-agents-benchmark-manipulation-debugml) |
