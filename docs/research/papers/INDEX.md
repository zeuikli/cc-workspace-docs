# papers/INDEX.md

> **Type:** raw:paper — 126 papers (103 .md + 25 .pdf)；2020–2026  
> **Updated**: 2026-06-03  
> **Query pattern**: BRAIN.md -> 本表（domain 欄位）-> 具體 paper

---

## Domain 索引（快速定位）

| Domain | 數量 | 代表論文 |
|--------|------|---------|
| [Memory Architecture](#memory-architecture) | 22 | MemGPT · A-Mem · Mem0 · HippoRAG |
| [Harness Engineering](#harness-engineering) | 28 | NLAH · AHE · Meta-Harness · CAR |
| [Agent Architecture](#agent-architecture) | 15 | CoALA · ReAct · Reflexion · SWE-Agent |
| [Multi-Agent](#multi-agent) | 8 | MultiAgentBench · CalBench · CoordArch |
| [LLM Routing / Cost](#llm-routing--cost) | 6 | RouteLLM · RCR · LLMCompiler |
| [RAG / Retrieval](#rag--retrieval) | 5 | RAG Survey · SPLADE · HippoRAG |
| [Performance / Infra](#performance--infra) | 10 | FlashAttention · vLLM · Speculative Decoding |
| [Safety / Alignment](#safety--alignment) | 8 | SafeHarness · Disempowerment · Values-in-Wild |
| [Benchmarks](#benchmarks) | 10 | TerminalBench · SWE-Bench-Pro · AEC-Bench |
| [Context Engineering](#context-engineering) | 7 | ACE · Lost-in-Middle · Beyond-Context-Window |
| [Other](#other) | 6 | Economic Index · CoT · Recursive LM |

---

## Memory Architecture

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [memgpt-2310-08560](2023-10-12-memgpt-llms-as-operating-systems-2310-08560.md) | 2023 | LLMs as OS；虛擬 context 三層記憶 | career-wiki memory 架構基礎 |
| [survey-memory-mechanism-2404-13501](2024-04-21-survey-memory-mechanism-llm-agents-2404-13501.md) | 2024 | LLM agent 記憶機制全調查 | reports/llm-memory-deep-research |
| [hipporag-2405-14831](2024-05-23-hipporag-neurobiological-memory-2405-14831.md) | 2024 | 神經記憶啟發的 RAG | — |
| [amem-2502-12110](2025-02-17-amem-agentic-memory-llm-agents-2502-12110.md) | 2025 | Agentic Memory；動態記憶圖 | reports/agent-memory-architecture-2026 |
| [mem0-2504-19413](2025-04-28-mem0-production-long-term-memory-2504-19413.md) | 2025 | 生產長期記憶；Mem0 多範圍 | reports/llm-memory-control-comprehensive-survey |
| [memory-os-ai-agent](2025-05-30-memory-os-ai-agent.md) | 2025 | Memory OS 架構 | reports/memory-control-architecture |
| [human-memory-to-ai-2504-15965](2025-04-22-human-memory-to-ai-memory-survey-2504-15965.md) | 2025 | 人類記憶->AI 記憶映射調查 | — |
| [memory-autonomous-survey-2603-07670](2026-03-08-memory-autonomous-llm-agents-survey-2603-07670.md) | 2026 | 自主 agent 記憶全調查 | reports/llm-memory-deep-research |
| [multi-agent-memory-computer-2603-10062](2026-03-09-multi-agent-memory-computer-architecture-2603-10062.md) | 2026 | 多代理記憶電腦架構 | — |
| [beyond-context-window-2603-04814](2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md) | 2026 | Memory vs long-context 實測 | reports/llm-memory-deep-research |
| [agentic-memory-unified-2601-01885](2026-01-05-agentic-memory-unified-ltm-stm-2601-01885.md) | 2026 | LTM+STM 統一框架 | — |
| [delta-mem-2605-12357](2026-05-12-delta-mem-efficient-online-memory-llm-2605-12357.md) | 2026 | 高效在線記憶更新 | — |
| [useful-memories-faulty-2605-12978](2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978.md) | 2026 | Batch Gate；連續記憶更新 | hooks/pre-compact.sh |
| [rethinking-memory-2505-00675](2025-05-01-rethinking-memory-llm-agents-operations-2505-00675.md) | 2025 | 記憶操作重思 | — |
| [hindsight-agent-memory-2512-12818](2025-12-14-hindsight-agent-memory-retain-recall-reflect-2512-12818.md) | 2025 | Retain/Recall/Reflect 三操作 | — |
| [chronos-2603-16862](2026-03-17-chronos-temporal-aware-conversational-agents-2603-16862.md) | 2026 | 時序感知對話 agent | — |
| [memtool-2507-21428](2025-07-29-memtool-short-term-memory-dynamic-tool-calling-2507.21428.md) | 2025 | 短期記憶 + 動態工具呼叫 | — |
| [memorybank-2305-10250](2023-05-17-memorybank-long-term-memory-2305-10250.md) | 2023 | 長期記憶銀行 | — |
| [scm-2304-13343](2023-04-26-scm-self-controlled-memory-2304-13343.md) | 2023 | 自控記憶 | — |
| [reasoningbank-2509-25140](2025-09-30-reasoningbank-scaling-agent-self-evolving-2509-25140.md) | 2025 | Reasoning memory 自演化 | — |
| [lost-in-middle-2307-03172](2026-05-12-lost-in-the-middle-2307-03172.md) | 2023 | U 型性能曲線；context 中段遺失 | context-management.md |
| [llms-get-lost-2505-06120](2025-05-09-llms-get-lost-multi-turn-2505-06120.md) | 2025 | 多輪對話中迷失問題 | — |

---

## Harness Engineering

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [nlah-2603-25723](2026-03-25-natural-language-agent-harnesses-2603-25723.md) | 2026 | NLAH：自然語言 harness 可移植性 | agent-harness/RESEARCH.md |
| [meta-harness-2603-28052](2026-05-12-meta-harness-2603-28052.md) | 2026 | Meta-Harness；59.6%->76.4% (+16.8pp) | KNOWLEDGE-MAP.md |
| [ahe-observability-2604-25850](2026-04-30-ahe-observability-driven-harness-2604-25850.md) | 2026 | AHE；observability-driven 自動優化 | KNOWLEDGE-MAP.md |
| [harbor-automated-2604-20938](2026-04-22-harbor-automated-harness-optimization-2604-20938.md) | 2026 | Harbor；自動化 harness 優化 | — |
| [car-harness-2604-23xxx](2026-04-23-harness-engineering-language-agents-car.md) | 2026 | CAR 14-component framework | HARNESS-CARD.md |
| [harness-categorical-2605-12239](2026-05-12-harness-engineering-categorical-architecture-2605-12239.md) | 2026 | Harness 範疇架構 | — |
| [runtime-substrate-2605-13357](2026-05-13-ai-harness-engineering-runtime-substrate-2605-13357.md) | 2026 | AI harness runtime substrate | — |
| [effective-vesper-2605-15221](2026-05-15-effective-harness-engineering-vesper-2605-15221.md) | 2026 | Effective harness engineering | — |
| [code-as-harness-2605-18747](2026-05-18-code-as-agent-harness-2605-18747.md) | 2026 | Code-as-harness 模式 | — |
| [adapting-interface-2605-22166](2026-05-21-adapting-interface-not-model-life-harness-2605-22166.md) | 2026 | 介面適配而非模型調整 | — |
| [last-harness-2604-21003](2026-04-29-last-harness-youll-ever-build-2604-21003.md) | 2026 | 終極 harness 設計原則 | — |
| [continual-harness-2605-09998](2026-05-11-continual-harness-online-adaptation-2605-09998.md) | 2026 | 持續在線 harness 適應 | — |
| [real-world-compilers-2603-20075](2026-03-20-agentic-harness-real-world-compilers-2603-20075.md) | 2026 | 現實世界 harness 架構 | — |
| [architectural-design-2604-20xxx](2026-04-20-architectural-design-decisions-ai-agent-harnesses.md) | 2026 | Harness 架構設計決策 | — |
| [configuring-agentic-2602-14690](2026-02-16-configuring-agentic-coding-tools-2602-14690.md) | 2026 | Agentic coding 工具配置 | best-practices/ |
| [safeharness-2604-13630](2026-04-13-safeharness-lifecycle-security-2604-13630.md) | 2026 | SafeHarness；安全生命週期 | — |
| [dive-into-claude-2604-14228](2026-04-14-dive-into-claude-code-design-space-2604-14228.md) | 2026 | Claude Code 設計空間深潛 | best-practices/ |
| [agentopt-2604-06296](2026-04-07-agentopt-client-side-optimization.md) | 2026 | AgentOpt；client-side 優化 | .claude/refs/advisor-tool-api.md |
| [skill-issue-harness](2026-03-12-skill-issue-harness-engineering.md) | 2026 | Harness skill 議題 | — |
| [opendev-terminal](2026-03-05-opendev-terminal-agents-scaffolding.md) | 2026 | Terminal agent scaffolding | — |
| [openai-codex-harness](2026-02-11-openai-harness-engineering-codex.md) | 2026 | Codex harness 工程 | ai-articles/scored/ |
| [agent-harness-survey](2026-04-07-agent-harness-survey.md) | 2026 | Agent harness 大調查 | SURVEY.md |
| [addyosmani-agents-md](2026-02-23-addyosmani-agents-md.md) | 2026 | AGENTS.md 設計（Addy Osmani）| ai-articles/scored/ |
| [agentflow-2604-22xxx](2026-04-22-agentflow-synthesizing-multi-agent.md) | 2026 | AgentFlow multi-agent 合成 | — |
| [meta-harness-optimization](2026-03-30-meta-harness-optimization-model-harnesses.md) | 2026 | Meta-harness 優化 | — |
| [nlah-community](2026-03-26-natural-language-agent-harnesses-nlah.md) | 2026 | NLAH 社群版 | ai-articles/scored/ |
| [tscg-tool-schema-2605-04107](2026-05-04-tscg-tool-schema-compilation-2605-04107.md) | 2026 | Tool schema compilation | — |
| [acon-2510-00615](2026-05-12-acon-2510-00615.md) | 2026 | Agent 協調最佳化 | — |

---

## Agent Architecture

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [coala-2309-02427](2023-09-05-coala-cognitive-architectures-language-agents-2309-02427.md) | 2023 | CoALA；認知架構框架 | KNOWLEDGE-MAP.md |
| [react-2210-03629](2022-10-06-react-synergizing-reasoning-acting-2210-03629.md) | 2022 | ReAct；推理+行動協同 | RESEARCH.md |
| [reflexion-2303-11366](2023-03-20-reflexion-verbal-reinforcement-learning-2303-11366.md) | 2023 | Reflexion；語言強化學習 | RESEARCH.md |
| [generative-agents-2304-03442](2023-04-07-generative-agents-simulacra-human-behavior-2304-03442.md) | 2023 | 生成式代理人模擬 | — |
| [voyager-2305-16291](2023-05-25-voyager-open-ended-embodied-agent-2305-16291.md) | 2023 | Voyager；開放任務具身代理 | — |
| [expel-2308-10144](2023-08-20-expel-llm-agents-experiential-learners-2308-10144.md) | 2023 | EXPEL；經驗學習 | — |
| [swe-agent-2405-15793](2024-05-06-swe-agent-agent-computer-interfaces-enable-automated-software-engineering-2405.15793.md) | 2024 | SWE-Agent；電腦介面 | — |
| [latent-state-2405-11120](2024-05-17-latent-state-estimation-ui-agents-2405.11120.md) | 2024 | UI agent 潛在狀態估計 | — |
| [externalization-2604-08224](2026-04-09-externalization-llm-agents-2604-08224.md) | 2026 | Agent 外部化模式 | — |
| [blueprint-first-2508-02721](2025-08-01-blueprint-first-model-second-2508.02721.md) | 2025 | Blueprint-first 架構 | — |
| [recursive-lm-2512-24601](2025-12-31-recursive-language-models-2512-24601.md) | 2025 | 遞迴語言模型 | — |
| [coordination-arch-2605-03310](2026-05-05-coordination-architectural-layer-2605-03310.md) | 2026 | 協調架構層 | — |
| [confucius-code-agent](2025-12-11-confucius-code-agent-scalable.md) | 2025 | 可擴展 code agent | ai-articles/scored/ |
| [heavyskill-2605-02396](2026-05-04-heavyskill-heavy-thinking-inner-skill-2605-02396.md) | 2026 | Heavy-thinking inner skill | — |
| [agentic-context-2510-04618](2025-10-06-agentic-context-engineering-2510-04618.md) | 2025 | ACE；Brevity Bias / Context Collapse | papers/low-score |

---

## Multi-Agent

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [multiagentbench-2503-01935](2025-03-03-multiagentbench-collaboration-competition-2503-01935.md) | 2025 | 協作 vs 競爭多代理基準 | KNOWLEDGE-MAP.md |
| [calbench-2605-09823](2026-05-10-calbench-coordination-privacy-tradeoffs-2605-09823.md) | 2026 | 協調 + 隱私 tradeoffs | — |
| [benchmarking-emergent-2603-03555](2026-03-03-benchmarking-emergent-coordination-moltbook-2603-03555.md) | 2026 | 湧現協調基準 | — |
| [multi-agent-frameworks-2602-03128](2026-02-03-multi-agent-llm-frameworks-benchmark-2602-03128.md) | 2026 | Multi-agent 框架基準 | KNOWLEDGE-MAP.md |
| [parness-2605-05258](2026-05-06-parness-automated-scientific-research-2605-05258.md) | 2026 | 自動科學研究多代理 | — |
| [skill-learn-bench-2604-20087](2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087.md) | 2026 | 持續技能學習基準 | — |
| [llmcompiler-2312-04511](2026-05-12-llmcompiler-icml-2024-2312-04511.md) | 2024 | LLMCompiler；平行化 agent | — |
| [is-grep-2605-15184](2026-05-14-is-grep-all-you-need-agentic-search-2605-15184.md) | 2026 | Grep vs embedding 搜尋比較 | — |

---

## LLM Routing / Cost

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [routellm-2406-18665](2024-06-20-routellm-learning-to-route-llms-2406.18665.md) | 2024 | RouteLLM；75% cost reduction | reports/llm-routing-industrial-cases |
| [rcr-router-2508-04903](2025-08-01-rcr-router-role-aware-context-routing-2508.04903.md) | 2025 | Role-aware context routing | — |
| [step-back-2406-14275](2024-06-20-step-back-profiling-personalized-scientific-writing-2406.14275.md) | 2024 | Step-back prompting | — |
| [dont-break-cache-2601-06007](2026-01-31-dont-break-cache-prompt-caching-2601-06007.md) | 2026 | Prompt caching 最佳實踐 | context-management.md |
| [prompting-inversion-2510-22251](2025-10-25-prompting-inversion-2510-22251.md) | 2025 | Prompt inversion 技術 | — |
| [from-rows-to-reasoning-2601-08741](2026-01-13-from-rows-to-reasoning-2601-08741.md) | 2026 | 結構化資料推理 | — |

---

## RAG / Retrieval

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [rag-2005-11401](2020-05-22-rag-retrieval-augmented-generation-2005-11401.md) | 2020 | RAG 原始論文 | — |
| [splade-v2-2109-10086](2021-09-21-splade-v2-sparse-lexical-expansion-2109-10086.md) | 2021 | 稀疏詞彙擴展 | — |
| [rag-survey-2312-10997](2023-12-18-retrieval-augmented-generation-survey-2312-10997.md) | 2023 | RAG 全調查 | — |
| [rag-best-practices-2501-07391](2025-01-13-rag-best-practices-acl2025-2501-07391.md) | 2025 | RAG best practices（chunk/stride/Contrastive ICL-RAG，Tübingen） | prompt-research 報告 C.3 |

---

## Performance / Infra

PDF 格式，無 .md 摘要：

| Paper | Year | Core Claim |
|-------|------|------------|
| flashattention-2205-14135.pdf | 2022 | FlashAttention v1 |
| flashattention-2-2307-08691.pdf | 2023 | FlashAttention v2 |
| flashattention-3-2407-08608.pdf | 2024 | FlashAttention v3 |
| speculative-decoding-2211-17192.pdf | 2022 | Speculative Decoding |
| vllm-paged-attention-2309-06180.pdf | 2023 | vLLM PagedAttention |
| medusa-speculative-2401-10774.pdf | 2024 | Medusa speculative |
| eagle-2401-15077.pdf | 2024 | EAGLE speculative |
| eagle-2-2406-16858.pdf | 2024 | EAGLE-2 speculative |
| multi-token-prediction-2404-19737.pdf | 2024 | Multi-token prediction |
| deepseek-v3-2412-19437.pdf | 2024 | DeepSeek-V3 技術報告 |
| streamingllm-attention-sink-2309-17453.pdf | 2023 | Attention sink；穩定串流 4M tokens；比 recompute 快 22.2× |
| snapkv-kv-cache-compression-2404-14469.pdf | 2024 | observation window 選 KV；壓縮至 1024 tokens 幾乎無損 |
| h2o-heavy-hitter-oracle-kv-cache-2306-14048.pdf | 2023 | Heavy-Hitter eviction；20% H2 -> throughput 最高 29× |
| mamba-ssm-selective-state-space-2312-00752.pdf | 2023 | Selective SSM；推理 O(1) 無 KV cache；throughput 5× |
| jamba-hybrid-transformer-mamba-2403-19887.pdf | 2024 | Attn:Mamba=1:7 hybrid；256K context；KV cache 小 8–32× |
| yarn-rope-context-extension-2309-00071.pdf | 2023 | NTK-by-Parts RoPE 擴展；現有方法最優，零額外開銷 |
| longrope-extending-llm-context-2402-13753.pdf | 2024 | 非均勻插值延伸至 2M tokens；僅 1K finetune steps |
| ring-attention-distributed-long-context-2310-01889.pdf | 2023 | 序列分塊跨設備 ring topology；無近似 million-token |

---

## Safety / Alignment

| Paper | Year | Core Claim |
|-------|------|------------|
| [safeharness-2604-13630](2026-04-13-safeharness-lifecycle-security-2604-13630.md) | 2026 | SafeHarness 安全生命週期 |
| [disempowerment-2601-19062](2026-01-27-disempowerment-patterns-real-world-llm-2601-19062.md) | 2026 | 去授權模式 |
| [values-in-wild-2504-15236](2025-04-21-values-in-the-wild-claude-interactions-2504-15236.md) | 2025 | 真實互動中的價值觀 |
| [security-memory-mnemonic-2604-16548](2026-04-17-security-long-term-memory-mnemonic-sovereignty-2604-16548.md) | 2026 | 記憶安全 |
| [what-matters-safety-2601-03868](2026-01-07-what-matters-safety-alignment-2601-03868.md) | 2026 | 安全對齊要素 |
| [cheating-agents-debugml](2026-05-23-cheating-agents-benchmark-manipulation-debugml.md) | 2026 | Agent benchmark 操縱 |
| [cyber-defense-2604-19533](2026-04-21-cyber-defense-benchmark-threat-hunting-llm-2604-19533.md) | 2026 | 網路防禦基準 |
| [claude-opus-4-7-system-card](2026-04-16-claude-opus-4-7-system-card.md) | 2026 | Claude Opus 4.7 系統卡 |
| [instruct-detector-2505-06311](2025-05-08-indirect-prompt-injection-defense-2505-06311.md) | 2025 | InstructDetector：indirect prompt injection 防禦（BIPIA ASR 0.03%） |

---

## Benchmarks

| Paper | Year | Core Claim |
|-------|------|------------|
| [terminal-bench-2601-11868](2026-01-17-terminal-bench-2601-11868.md) | 2026 | TerminalBench 基準 |
| [swe-bench-pro-2509-16941](2025-09-21-swe-bench-pro-long-horizon-2509-16941.md) | 2025 | SWE-Bench Pro；長視野 |
| [aec-bench-multimodal](2026-03-31-aec-bench-multimodal-benchmark-agentic-systems.md) | 2026 | AEC 多模態 agentic 基準 |
| [skills-bench-2602-12670](2026-02-13-skills-bench-agent-skills-2602-12670.md) | 2026 | Skills 基準 |
| [skill-learn-bench-2604-20087](2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087.md) | 2026 | 持續技能學習基準 |
| [composite-stem-expert](2026-04-10-composite-stem-expert-curated.md) | 2026 | STEM 專家評測 |
| [ock-bench-2511-05722](2025-11-07-ock-bench-reasoning-efficiency-overthinking-2511-05722.md) | 2025 | 推理效率 / 過度思考 |
| [multiagentbench-2503-01935](2025-03-03-multiagentbench-collaboration-competition-2503-01935.md) | 2025 | 多代理協作基準 |
| [gpt5-system-card-2601-03267](2026-01-08-gpt5-system-card-2601-03267.md) | 2026 | GPT-5 系統卡 |
| [gpt5-5-system-card](2026-04-23-gpt5-5-system-card.md) | 2026 | GPT-5.5 系統卡 |

---

## Context Engineering

| Paper | Year | Core Claim |
|-------|------|------------|
| [agentic-context-2510-04618](2025-10-06-agentic-context-engineering-2510-04618.md) | 2025 | ACE；Brevity Bias + Grow-and-Refine |
| [beyond-context-2603-04814](2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md) | 2026 | Memory vs long-context 實測 |
| [lost-in-middle-2307-03172](2026-05-12-lost-in-the-middle-2307-03172.md) | 2023 | U 型曲線；context 中段遺失 |
| [decreasing-cot-2506-07142](2025-06-08-decreasing-value-chain-of-thought-2506-07142.md) | 2025 | CoT 效益下降 |
| [dynamic-cheatsheet-2504-07952](2025-04-11-dynamic-cheatsheet-test-time-learning-2504-07952.md) | 2025 | 動態備忘錄；test-time learning |
| [dont-break-cache-2601-06007](2026-01-31-dont-break-cache-prompt-caching-2601-06007.md) | 2026 | Prompt caching 最佳實踐 |
| [rcr-2508-04903](2025-08-01-rcr-router-role-aware-context-routing-2508.04903.md) | 2025 | Role-aware context routing |
| parallel-context-compaction-2605-23296.pdf | 2026 | 非同步平行 compaction；fine-grained 可控 summary volume |
| slipstream-compaction-validation-2605-08580.pdf | 2026 | trajectory-grounded 驗證；+8.8pp accuracy / −39.7% latency |
| fast-kv-compaction-attention-matching-2602-16284.pdf | 2026 | latent space KV 壓縮；50× 幾乎無損 |
| [when-better-prompts-hurt-2601-22025](2026-01-29-when-better-prompts-hurt-eval-driven-2601-22025.md) | 2026 | Eval-driven prompt 迭代；MVES；泛用 prompt 反而降準（100%->90%） |
| [promptbridge-2512-01420](2025-12-01-promptbridge-cross-model-prompt-transfer-2512-01420.md) | 2025 | Cross-model prompt transfer；Model Drifting；SWE-Bench +27.39% |

---

## Cold-Start / Startup Latency

> 間接相關（serverless/GPU 層），概念遷移至 Claude Code session init / hook spawn 優化。見 reports/2026-06-03-claude-code-cold-start-latency-deep-research.md

| Paper | Year | Core Claim |
|-------|------|------------|
| [hydraserve-2502-15524](2025-02-21-hydraserve-cold-start-serverless-llm-2502-15524.md) | 2025 | Cold start 降 1.7–4.7×；overlap stages + proactive distribution |
| [cold-start-antipatterns-2512-16066](2025-12-19-cold-start-antipatterns-serverless-2512-16066.md) | 2025 | Cold-start 為 developer-visible 設計問題；81 issues -> 反模式分類；Amazon +100ms = -1% 銷售 |

---

## Other

| Paper | Year | Core Claim |
|-------|------|------------|
| [anthropic-economic-2511-15080](2025-11-19-anthropic-economic-index-geographic-adoption-2511-15080.md) | 2025 | 地理採用經濟指標 |
| [which-economic-tasks-2503-04761](2025-03-07-which-economic-tasks-ai-claude-conversations-2503-04761.md) | 2025 | AI 可替代任務分析 |
