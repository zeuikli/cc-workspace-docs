# papers/INDEX.md

> Type: raw:corpus
> Harness-Layer: L4-knowledge
> **Type:** raw:paper — 277 papers (計數單位 = 1 篇 1 個 .md，實測 277 `ls research/papers/*.md | grep -v INDEX.md | wc -l`——**必須排除 INDEX.md 自己**，否則多算 1；PDF 為伴隨檔非計數單位：pdfs/ 內 258 `ls research/papers/pdfs/*.pdf | wc -l`，另有 2 個誤置於本目錄頂層待歸位)；2020–2026  
> **Updated**: 2026-07-26  
> **未對帳項**：md↔pdf 配對數與 web-only 篇數**尚未確證**，勿引用。已試兩個 oracle 皆不合格：① stem 相等 → 僅 1 筆命中（.md 用 `YYYY-MM-DD-slug-<id>`、pdf 用 `<id>`，命名不同）；② 自 .md 尾端抽 arXiv id 轉點號比對 → 214 配對／58 web-only／41 孤兒 pdf，但「41 個 .md 抽不到 id」與「41 個孤兒 pdf」數量恰好相同，強烈暗示是同一批非 arXiv 命名檔配對失敗而非真孤兒。需先定義權威配對規則（建議 .md front-matter 顯式記 pdf 路徑）再重測。  
> **Query pattern**: BRAIN.md → 本表（domain 欄位）→ 具體 paper

---

## Domain 索引（快速定位）

| Domain | 數量 | 代表論文 |
|--------|------|---------|
| [Memory Architecture](#memory-architecture) | 36 | MemGPT · A-Mem · Mem0 · HippoRAG · HyMem · Live-Evo |
| [Harness Engineering](#harness-engineering) | 57 | NLAH · AHE · CAR · HarnessX · LLM-as-Code · SkillCAT · Scaling-Harness · Harness-Bench |
| [Loop / Workflow Engineering](#loop--workflow-engineering) | 13 | Agent-Loops→Graphs · Sovereign-Loops · EvolveR · AgentCompass · Infinite-Agentic-Loops |
| [Goal Engineering](#goal-engineering) | 6 | Goal-Drift-Eval · Inherited-Drift · Subgoal-Driven · Agent-Drift |
| [Agent Architecture](#agent-architecture) | 17 | CoALA · ReAct · Reflexion · SWE-Agent |
| [Multi-Agent](#multi-agent) | 32 | MultiAgentBench · AdaptOrch · HALO · HERA · AutoGen · AgentPrune · MOC · GoA |
| [Caching / KV Cache / Token Budget](#caching--kv-cache--token-budget) | 25 | CompressKV · Tangram · SwiftCache · Fidelity-Distort · LLMLingua-Survey · Scaling-Paradox |
| [Model / System Cards](#model--system-cards) | 13 | Opus 4.8 · Fable 5 · Haiku 4.5 · GPT-5.4 · ChatGPT Agent |
| [LLM Routing / Cost](#llm-routing--cost) | 6 | RouteLLM · RCR · LLMCompiler |
| [RAG / Retrieval](#rag--retrieval) | 5 | RAG Survey · SPLADE · HippoRAG |
| [Performance / Infra](#performance--infra) | 10 | FlashAttention · vLLM · Speculative Decoding |
| [AI Alignment / Constitutional AI](#ai-alignment--constitutional-ai) | 4 | Constitutional AI · Weak-to-Strong · RLAIF · Debate |
| [AI Safety / Red Teaming](#ai-safety--red-teaming) | 4 | GCG Adversarial · HarmBench · LM Red Team · WildTeaming |
| [Diffusion Language Models](#diffusion-language-models) | 4 | LLaDA · SEDD · MDLM · MGDM |
| [Mechanistic Interpretability](#mechanistic-interpretability) | 5 | Toy Superposition · Monosemanticity · Scaling Mono · Circuit Tracing |
| [Multimodal / Vision-Language](#multimodal--vision-language) | 4 | Flamingo · BLIP-2 · LLaVA · LLaVA-1.5 |
| [Test-Time Compute](#test-time-compute) | 5 | Process Reward · Snell Scaling · DeepSeek-R1 · s1 · SGS |
| [Safety / Alignment](#safety--alignment) | 12 | SafeHarness · Disempowerment · Values-in-Wild |
| [Benchmarks](#benchmarks) | 10 | TerminalBench · SWE-Bench-Pro · AEC-Bench |
| [Context Engineering](#context-engineering) | 16 | ACE · Lost-in-Middle · Context-Eng-Survey · Less-Context-Better-Agents |
| [Other](#other) | 9 | Economic Index · CoT · Recursive LM · Neuromorphic |

---

## Memory Architecture

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [live-evo-2602-02369](2026-02-02-live-evo-online-agentic-memory-feedback-2602-02369.md) | 2026 | 線上記憶演化；Experience+Meta-Guideline 雙 bank；加權衰退 +20.8% Brier | overnight-research staleness · dreaming-consolidator 參考 |
| [memory-beyond-recall-2606-09483](2026-06-08-memory-beyond-recall-dual-process-cognitive-memory-2606-09483.md) | 2026 | 雙進程認知記憶（即時錄入+離線整合）| memory-compactor 參考 |
| [agent-memory-characterization-2606-06448](2026-06-04-agent-memory-characterization-stateful-workloads-2606-06448.md) | 2026 | 系統層記憶實測；10 種記憶系統成本分佈 | — |
| [recall-to-forgetting-2604-20006](2026-04-21-recall-to-forgetting-long-term-memory-benchmark-2604-20006.md) | 2026 | Forgetting-Aware Memory Accuracy 指標 | — |
| [lightweight-memory-slm-2604-07798](2026-04-10-lightweight-llm-agent-memory-small-models-2604-07798.md) | 2026 | SLM 承擔記憶操作；STM/MTM/LTM 三層 | — |
| [memory-llm-era-2604-01707](2026-04-01-memory-llm-era-modular-architectures-2604-01707.md) | 2026 | 統一框架比較記憶策略 | — |
| [multi-layered-memory-2603-29194](2026-03-31-multi-layered-memory-architectures-llm-agents-2603-29194.md) | 2026 | 三層對話歷史架構抗語意漂移 | — |
| [memorycd-2603-25973](2026-03-26-memorycd-cross-domain-personalization-memory-2603-25973.md) | 2026 | 跨域終生記憶 benchmark | — |
| [governing-evolving-memory-2603-11768](2026-03-12-governing-evolving-memory-ssgm-2603-11768.md) | 2026 | SSGM：記憶一致性/時序衰減/存取控制 | — |
| [contextual-memory-virtualisation-2602-22402](2026-02-25-contextual-memory-virtualisation-dag-trimming-2602-22402.md) | 2026 | DAG 版本管理+無損裁剪 -20% token | memory-compactor 參考 |
| [anatomy-agentic-memory-2602-19320](2026-02-22-anatomy-agentic-memory-taxonomy-2602-19320.md) | 2026 | agentic memory 評測缺陷分類 | — |
| [hymem-2602-13933](2026-02-15-hymem-hybrid-memory-dynamic-retrieval-2602-13933.md) | 2026 | 混合記憶+動態檢索排程 -92.6% 算力 | — |
| [active-context-compression-2601-07190](2026-01-12-active-context-compression-autonomous-memory-2601-07190.md) | 2026 | Focus：自主壓縮上下文 -23% token | context-management 參考 |
| [memgpt-2310-08560](2023-10-12-memgpt-llms-as-operating-systems-2310-08560.md) | 2023 | LLMs as OS；虛擬 context 三層記憶 | career-wiki memory 架構基礎 |
| [survey-memory-mechanism-2404-13501](2024-04-21-survey-memory-mechanism-llm-agents-2404-13501.md) | 2024 | LLM agent 記憶機制全調查 | reports/llm-memory-deep-research |
| [hipporag-2405-14831](2024-05-23-hipporag-neurobiological-memory-2405-14831.md) | 2024 | 神經記憶啟發的 RAG | — |
| [amem-2502-12110](2025-02-17-amem-agentic-memory-llm-agents-2502-12110.md) | 2025 | Agentic Memory；動態記憶圖 | reports/agent-memory-architecture-2026 |
| [mem0-2504-19413](2025-04-28-mem0-production-long-term-memory-2504-19413.md) | 2025 | 生產長期記憶；Mem0 多範圍 | reports/llm-memory-control-comprehensive-survey |
| [memory-os-ai-agent](2025-05-30-memory-os-ai-agent.md) | 2025 | Memory OS 架構 | reports/memory-control-architecture |
| [human-memory-to-ai-2504-15965](2025-04-22-human-memory-to-ai-memory-survey-2504-15965.md) | 2025 | 人類記憶→AI 記憶映射調查 | — |
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
| [meta-harness-2603-28052](2026-05-12-meta-harness-2603-28052.md) | 2026 | Meta-Harness；59.6%→76.4% (+16.8pp) | KNOWLEDGE-MAP.md |
| [ahe-observability-2604-25850](2026-04-30-ahe-observability-driven-harness-2604-25850.md) | 2026 | AHE；observability-driven 自動優化 | KNOWLEDGE-MAP.md |
| [harbor-automated-2604-20938](2026-04-22-harbor-automated-harness-optimization-2604-20938.md) | 2026 | Harbor；自動化 harness 優化 | — |
| [car-harness-2604-23xxx](2026-04-23-harness-engineering-language-agents-car.md) | 2026 | CAR 14-component framework | HARNESS-CARD.md |
| [harness-categorical-2605-12239](2026-05-12-harness-engineering-categorical-architecture-2605-12239.md) | 2026 | Harness 範疇架構 | — |
| [harnessx-2606-14249](2026-06-12-harnessx-composable-adaptive-evolvable-harness-foundry-2606-14249.md) | 2026 | HarnessX/AEGIS；trace 演化 +14.5% (max +44%)；seesaw gate | DAILY-RESEARCH/2026-06-18 |
| [skillcat-2606-13317](2026-06-11-skillcat-contrastive-topology-skill-evolution-2606-13317.md) | 2026 | Skill 自演化；CCE 對比+AAE replay 驗證+TTE topology 載入 +40.4% | skill-evolution 閉環（T27） |
| [skillrae-2605-10114](2026-05-11-skillrae-skill-context-compilation-rae-2605-10114.md) | 2026 | Skill graph 選擇性載入；rescue-aware compact compilation +11.7% | lazy-load 進階參考 |
| [skilldex-2604-16911](2026-04-18-skilldex-package-manager-registry-agent-skills-2604-16911.md) | 2026 | Skill spec lint（compiler-style conformance）+ skillset 綁束 | harness-meta schema-verify |
| [survey-qa-to-task-2606-20683](2026-06-14-survey-agent-system-harness-design-2606-20683.md) | 2026 | Survey；harness 六維 runtime 責任 + 四範式演進 | KNOWLEDGE-MAP / SURVEY.md |
| [llm-as-code-2606-15874](2026-06-14-llm-as-code-agentic-programming-agent-harness-2606-15874.md) | 2026 | Agentic Programming；program 掌 control flow、LLM-as-Code；DAG context | core.md 判斷/決定 · Workflow |
| [maestro-order-2606-23983](2026-06-22-maestro-order-model-agnostic-orchestration-harness-2606-23983.md) | 2026 | 4 primitive orchestration；verify 幾何放大 0.55→0.999 | /qp · verified-merge |
| [aohp-2606-23449](2026-06-22-aohp-os-level-agent-harness-2606-23449.md) | 2026 | OS 層 agent harness（AOSP）；+21% 完成率 / -51% token | best-practices/（域外）|
| [harness-mu-2606-21856](2026-06-20-harness-mu-multi-user-llm-agents-2606-21856.md) | 2026 | 多使用者治理交 execution hook 非 LLM；+48.9pp | core.md 判斷/決定 · Agent Input Security |
| [beaver-2606-21005](2026-06-19-beaver-agent-harness-scientific-curation-2606-21005.md) | 2026 | 科學 curation harness；GRAS 81.0 (+23)；evaluate→diagnose→revise | autoresearch · The Loop |
| [phoneharness-2606-14832](2026-06-12-phoneharness-mixed-gui-cli-tool-actions-2606-14832.md) | 2026 | mixed GUI/CLI/tool；deterministic routing + verifiable side effect | core.md（域外）|
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
| [terminus-4b-2605-03195](2026-05-04-terminus-4b-agentic-execution-subagent-2605-03195.md) | 2026 | 4B SLM（SFT+RL）替代前沿模型執行 subagent；-30% 主代理 token | — |
| [sia-2605-27276](2026-05-26-sia-self-improving-ai-harness-weight-updates-2605-27276.md) | 2026 | SIA；harness + weight 雙更新閉環；SIA-W+H > SIA-H on all 3 domains | — |
| [adaptive-auto-harness-2606-01770](2026-06-01-adaptive-auto-harness-open-ended-task-streams-2606-01770.md) | 2026 | 多代理 evolver + adaptive routing；PolyBench CWR +118%（20.3→44.3） | — |
| [harnessfix-2606-06324](2026-06-04-harnessfix-diagnosing-repairing-harness-flaws-2606-06324.md) | 2026 | HTIR trace 診斷→歸因→修復；SWE-Bench +26.7%；跨基準 +15~50% | The Loop RECORD 失敗歸因 |
| [rho-2606-05922](2026-06-04-retrospective-harness-optimization-rho-2606-05922.md) | 2026 | RHO：自監督回顧優化；不需 labeled val set；以 agent 自評篩選更新 | — |
| [self-harness-2606-09498](2026-06-08-self-harness-harnesses-improve-themselves-2606-09498.md) | 2026 | Self-Harness：Weakness Mining→Proposal→Regression 三階段；+21.4~38.1pp | skill-evolution 對照 |
| [what-makes-a-harness-2606-10106](2026-06-08-what-makes-a-harness-necessary-sufficient-2606-10106.md) | 2026 | 概念分析：agent harness necessary & sufficient 4 條件（loop+tool+ctx+ctrl）| HARNESS-CARD.md 定義 |
| [scaling-harness-2605-26112](2026-05-25-scaling-harness-system-scaling-agentic-ai-2605-26112.md) | 2026 | System scaling 非模型規模；harness = first-class；dynamic skill routing 三瓶頸 | Fusion 架構學術 ground truth |
| [harnesses-inference-time-alignment-2605-21516](2026-05-15-harnesses-inference-time-alignment-trajectories-2605-21516.md) | 2026 | Partial harness（僅規範初始步驟）優於全結構化 workflow；過度分解/剪枝反有害 | fusion sidekick brief 顆粒度 |
| [demoevolve-2605-24539](2026-05-23-demoevolve-sparse-feedback-harness-evolution-2605-24539.md) | 2026 | 稀疏回饋下示範引導優於純 reward-only harness 演化 | autoload-evolution 對照 |
| [harness-bench-2605-27922](2026-05-27-harness-bench-measuring-harness-effects-2605-27922.md) | 2026 | 106 任務×5194 軌跡；agent 能力應以 model-harness 組態層級回報 | model-profiles 換模型重審 |
| [recursive-agent-harnesses-2606-13643](2026-06-11-recursive-agent-harnesses-2606-13643.md) | 2026 | 遞迴 spawn 並行 sub-harness；4M token 長文本 71.75%→81.36%（GPT-5） | subagent-strategy fan-out |
| [interplay-harness-post-training-2606-25447](2026-06-24-interplay-harness-design-post-training-2606-25447.md) | 2026 | Harness-aware post-training 改善 OOD 適應；minimal harness 在工具偏移下大幅退化 | — |
| [belief-divergence-2607-04528](2026-07-05-measuring-harness-induced-belief-divergence-2607-04528.md) | 2026 | Harness 設定改變 agent 內在推理過程，即使任務完成率不變 | subagent-strategy verdict 非證據 |
| [prompts-to-contracts-2607-08028](2026-07-09-from-prompts-to-contracts-harness-engineering-2607-08028.md) | 2026 | 合約優先：deterministic code enforcement > prompt-only；120/120 vs 88/120 utility | core.md 判斷/決定公理 |
| [rethinking-harness-eval-2607-12227](2026-07-14-rethinking-evaluation-harness-evolution-agents-2607-12227.md) | 2026 | Harness 演化未必勝簡單 test-time scaling；同 benchmark 評測有洩漏風險 | autoload-evolution 方法論警示 |
| [self-evolving-gsme-2607-13683](2026-07-15-self-evolving-agent-harnesses-gated-quality-diversity-2607-13683.md) | 2026 | 提案/認證分離：LLM 診斷+確定性統計認證；sealed test 泛化 +9~15.5pp | core.md 判斷 vs 決定範例 |
| [agentic-environment-engineering-survey-2606-12191](2026-06-10-agentic-environment-engineering-survey-2606-12191.md) | 2026 | 環境工程 survey：modeling/synthesis/evaluation/application 四面向框架 | blast radius / worktree 隔離策略參照 |

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
| [toward-efficient-agents-2601-14192](2026-01-20-toward-efficient-agents-memory-tool-planning-2601-14192.md) | 2026 | 效率 survey：memory/tool learning/planning 三元件成本分析 | model-profiles.md 檔位量化參考 |
| [tool-making-self-evolving-2607-08010](2026-07-09-tool-making-self-evolving-agents-low-latency-2607-08010.md) | 2026 | 部署前工具製造管線；延遲 -42~-62%、錯誤率 -53% | skill-creator/skill-evolution 效益佐證 |

---

## Multi-Agent

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [adaptorch-2602-16873](2026-02-18-adaptorch-task-adaptive-multi-agent-orchestration-2602-16873.md) | 2026 | 動態選 4 種協調拓樸 + orchestration scaling law | subagent-strategy fan-out |
| [orchestration-survey-2601-13671](2026-01-20-orchestration-multi-agent-systems-architectures-protocols-2601-13671.md) | 2026 | 多代理協調架構/協定/治理藍圖 | — |
| [multi-turn-vs-single-2509-23537](2025-09-28-multi-turn-multi-agent-orchestration-vs-single-llm-2509-23537.md) | 2025 | 多代理多輪協調匹敵單一最強模型 | — |
| [halo-2505-13516](2025-05-17-halo-hierarchical-orchestration-multi-agent-2505-13516.md) | 2025 | 三層階層 + MCTS 推理路徑 +14.4% | — |
| [rl-orchestration-traces-2605-02801](2026-05-04-rl-multi-agent-orchestration-traces-2605-02801.md) | 2026 | 以 orchestration trace 為 RL credit 信號 | — |
| [experience-as-compass-2604-00901](2026-04-01-experience-as-compass-multi-agent-rag-hera-2604-00901.md) | 2026 | HERA：動態拓樸+prompt 演化 +38.7% | — |
| [self-organizing-mas-2603-25928](2026-03-26-self-organizing-multi-agent-continuous-software-dev-2603-25928.md) | 2026 | supervisor 動態招募 worker 子代理 | — |
| [multiagentbench-2503-01935](2025-03-03-multiagentbench-collaboration-competition-2503-01935.md) | 2025 | 協作 vs 競爭多代理基準 | KNOWLEDGE-MAP.md |
| [calbench-2605-09823](2026-05-10-calbench-coordination-privacy-tradeoffs-2605-09823.md) | 2026 | 協調 + 隱私 tradeoffs | — |
| [benchmarking-emergent-2603-03555](2026-03-03-benchmarking-emergent-coordination-moltbook-2603-03555.md) | 2026 | 湧現協調基準 | — |
| [multi-agent-frameworks-2602-03128](2026-02-03-multi-agent-llm-frameworks-benchmark-2602-03128.md) | 2026 | Multi-agent 框架基準 | KNOWLEDGE-MAP.md |
| [parness-2605-05258](2026-05-06-parness-automated-scientific-research-2605-05258.md) | 2026 | 自動科學研究多代理 | — |
| [skill-learn-bench-2604-20087](2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087.md) | 2026 | 持續技能學習基準 | — |
| [llmcompiler-2312-04511](2026-05-12-llmcompiler-icml-2024-2312-04511.md) | 2024 | LLMCompiler；平行化 agent | — |
| [is-grep-2605-15184](2026-05-14-is-grep-all-you-need-agentic-search-2605-15184.md) | 2026 | Grep vs embedding 搜尋比較 | — |
| [decentmem-2605-22721](2026-05-21-decentmem-self-evolving-mas-decentralized-memory-2605-22721.md) | 2026 | DecentMem；per-agent 雙池記憶 +23.8% acc / -49% token；O(log T) regret | DAILY-RESEARCH/2026-06-18 |
| [multiagent-debate-2305-14325](2023-05-23-multiagent-debate-factuality-reasoning-2305-14325.md) | 2023 | Society of Minds；N agents 辯論迭代收斂消除幻覺；factuality +) | — |
| [chatdev-2307-07924](2023-07-16-chatdev-communicative-agents-software-development-2307-07924.md) | 2023 | Chat Chain + Communicative Dehallucination；虛擬軟體公司 waterfall；ACL 2024 | — |
| [metagpt-2308-00352](2023-08-01-metagpt-multi-agent-collaborative-framework-2308-00352.md) | 2023 | SOP 編碼進 multi-agent；角色分工防 cascading hallucination | — |
| [autogen-2308-08155](2023-08-16-autogen-multi-agent-conversation-framework-2308-08155.md) | 2023 | ConversableAgent 通用框架；LLM+tool+human 任意組合；Microsoft | — |
| [agentverse-2308-10848](2023-08-21-agentverse-multi-agent-collaboration-emergent-behaviors-2308-10848.md) | 2023 | 動態組成 4 階段 pipeline；研究正/負向湧現行為 | — |
| [mast-2503-13657](2025-03-17-mast-why-multi-agent-llm-systems-fail-2503-13657.md) | 2025 | MAST：14 種 MAS 失敗模式分類；7 框架 × 1600+ traces；κ=0.88；NeurIPS 2025 | — |
| [agentprune-2410-02506](2024-10-03-agentprune-economical-multi-agent-communication-2410-02506.md) | 2024 | 首次形式化 MAS 通訊冗餘；spatial-temporal graph one-shot pruning | subagent-strategy 降噪佐證 |
| [moc-2606-02359](2026-06-01-moc-multi-order-communication-multi-agent-2606-02359.md) | 2026 | multi-hop 訊息稀釋；Semantic-Topological Merging 保真於 token 約束 | parent↔child 通訊限制佐證 |
| [token-economics-2605-09104](2026-05-09-token-economics-llm-agents-dual-view-2605-09104.md) | 2026 | Token Economics 綜述；micro/meso/macro/security 四維 + principal-agent | delegation-protocol 理論框架 |
| [latent-communication-2606-05711](2026-06-04-latent-communication-multi-agent-unified-framework-2606-05711.md) | 2026 | latent 通訊 3 軸框架（WHAT/WHICH/HOW）；18 方法 5 模式 | NL 通訊可稽核性取捨參照 |
| [vmao-plan-execute-verify-replan-2603-11445](2026-03-12-vmao-plan-execute-verify-replan-2603-11445.md) | 2026 | 五階段 Plan-Execute-Verify-Replan-Synthesize；LLM verifier 驅動 replan；完整度 +35%（8.5× token） | core.md 判斷/決定；graph.md 異模型驗收佐證 |
| [rgao-retrieval-conditioned-topology-2605-05657](2026-05-07-rgao-retrieval-conditioned-topology-budget-conservation-2605-05657.md) | 2026 | 檢索條件拓撲選路 + 六維預算代數；Theorem 1 父≥子預算和；誤路由 30.1%→8.2% | graph.md handoff tier 綁定形式化參照 |
| [goa-graph-of-agents-2604-17148](2026-04-18-goa-graph-of-agents-multi-agent-collaboration-2604-17148.md) | 2026 | node/edge sampling + 雙向 message passing；3 agent 勝 6 agent baseline | fan-out 上限「多不如準」量化佐證 |
| [agp-adaptive-graph-pruning-2506-02951](2025-06-03-agp-adaptive-graph-pruning-multi-agent-communication-2506-02951.md) | 2025 | 軟硬雙剪枝聯合最佳化；token -90%+，準確度 +1.48%（vs G-Designer） | agentprune 方法論補強 |
| [role-consistency-multi-agent-2604-02770](2026-04-03-role-consistency-multi-agent-collaboration-2604-02770.md) | 2026 | Role clarity matrix 量化角色越界；越界率 46.4%→8.4% | skill-roster-audit 量化維度參考 |
| [survey-llm-agent-communication-mcp-2506-05364](2025-05-26-survey-llm-agent-communication-mcp-2506-05364.md) | 2025 | MCP 通訊設計模式 survey：Mediator/Observer/Pub-Sub/Broker | subscribe_pr_activity 架構參照 |

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

PDF 格式，無 .md 摘要，存於 `pdfs/`：

| Paper | Year | Core Claim |
|-------|------|------------|
| [📄 2205.14135](https://arxiv.org/abs/2205.14135) | 2022 | FlashAttention v1 |
| [📄 2307.08691](https://arxiv.org/abs/2307.08691) | 2023 | FlashAttention v2 |
| [📄 2407.08608](https://arxiv.org/abs/2407.08608) | 2024 | FlashAttention v3 |
| [📄 2211.17192](https://arxiv.org/abs/2211.17192) | 2022 | Speculative Decoding |
| [📄 2309.06180](https://arxiv.org/abs/2309.06180) | 2023 | vLLM PagedAttention |
| [📄 2401.10774](https://arxiv.org/abs/2401.10774) | 2024 | Medusa speculative |
| [📄 2401.15077](https://arxiv.org/abs/2401.15077) | 2024 | EAGLE speculative |
| [📄 2406.16858](https://arxiv.org/abs/2406.16858) | 2024 | EAGLE-2 speculative |
| [📄 2404.19737](https://arxiv.org/abs/2404.19737) | 2024 | Multi-token prediction |
| [📄 2412.19437](https://arxiv.org/abs/2412.19437) | 2024 | DeepSeek-V3 技術報告 |
| [📄 2309.17453](https://arxiv.org/abs/2309.17453) | 2023 | Attention sink；穩定串流 4M tokens；比 recompute 快 22.2× |
| [📄 2404.14469](https://arxiv.org/abs/2404.14469) | 2024 | observation window 選 KV；壓縮至 1024 tokens 幾乎無損 |
| [📄 2306.14048](https://arxiv.org/abs/2306.14048) | 2023 | Heavy-Hitter eviction；20% H2 → throughput 最高 29× |
| [📄 2312.00752](https://arxiv.org/abs/2312.00752) | 2023 | Selective SSM；推理 O(1) 無 KV cache；throughput 5× |
| [📄 2403.19887](https://arxiv.org/abs/2403.19887) | 2024 | Attn:Mamba=1:7 hybrid；256K context；KV cache 小 8–32× |
| [📄 2309.00071](https://arxiv.org/abs/2309.00071) | 2023 | NTK-by-Parts RoPE 擴展；現有方法最優，零額外開銷 |
| [📄 2402.13753](https://arxiv.org/abs/2402.13753) | 2024 | 非均勻插值延伸至 2M tokens；僅 1K finetune steps |
| [📄 2310.01889](https://arxiv.org/abs/2310.01889) | 2023 | 序列分塊跨設備 ring topology；無近似 million-token |

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
| [agent-behavioral-contracts-2602-22302](2026-02-25-agent-behavioral-contracts-runtime-enforcement-2602-22302.md) | 2026 | Design-by-Contract 搬進 agent；(p,δ,k)-satisfaction 機率合規度量 |
| [unfireable-safety-kernel-2606-26057](2026-06-24-unfireable-safety-kernel-execution-time-alignment-2606-26057.md) | 2026 | 行程外 safety kernel；1000 次逃逸嘗試零成功 |
| [beyond-single-agent-alignment-2604-22879](2026-04-24-beyond-single-agent-alignment-context-fragmented-violations-2604-22879.md) | 2026 | Context-Fragmented Violation；Distributed Sentinel F1=0.95 |
| [rail-guard-2607-16215](2026-05-28-rail-guard-evaluation-remediation-gap-2607-16215.md) | 2026 | evaluate-rewrite-reevaluate 迴圈；收斂率 96.9% vs block-retry 49.1% |

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
| [survey-context-engineering-2507-13334](2025-07-17-survey-context-engineering-llms-2507-13334.md) | 2025 | Context engineering 1400+ 篇分類調查 |
| [max-effective-context-2509-21361](2025-09-21-maximum-effective-context-window-2509-21361.md) | 2025 | 最大有效 context window 遠短於宣稱 |
| [demand-paging-context-2603-09023](2026-03-09-demand-paging-llm-context-windows-2603-09023.md) | 2026 | OS demand-paging 管 context -93% |
| [hyve-2604-05400](2026-04-07-hyve-hybrid-views-context-engineering-2604-05400.md) | 2026 | DB view 管 log/metric 輸入 -50~90% token |
| [taco-2604-19572](2026-04-21-taco-observational-context-compression-terminal-agents-2604-19572.md) | 2026 | 訓練-free 觀察壓縮規則重用（terminal agent）|
| [less-context-better-agents-2606-10209](2026-06-08-less-context-better-agents-2606-10209.md) | 2026 | prune+summarize 91.6% 完成率最省 token |
| [invasive-context-engineering-2512-03001](2025-12-02-invasive-context-engineering-2512-03001.md) | 2025 | context 嵌控制句防 jailbreak/scheming |
| [agentic-context-2510-04618](2025-10-06-agentic-context-engineering-2510-04618.md) | 2025 | ACE；Brevity Bias + Grow-and-Refine |
| [beyond-context-2603-04814](2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md) | 2026 | Memory vs long-context 實測 |
| [lost-in-middle-2307-03172](2026-05-12-lost-in-the-middle-2307-03172.md) | 2023 | U 型曲線；context 中段遺失 |
| [decreasing-cot-2506-07142](2025-06-08-decreasing-value-chain-of-thought-2506-07142.md) | 2025 | CoT 效益下降 |
| [dynamic-cheatsheet-2504-07952](2025-04-11-dynamic-cheatsheet-test-time-learning-2504-07952.md) | 2025 | 動態備忘錄；test-time learning |
| [dont-break-cache-2601-06007](2026-01-31-dont-break-cache-prompt-caching-2601-06007.md) | 2026 | Prompt caching 最佳實踐 |
| [rcr-2508-04903](2025-08-01-rcr-router-role-aware-context-routing-2508.04903.md) | 2025 | Role-aware context routing |
| [📄 2605.23296](https://arxiv.org/abs/2605.23296) | 2026 | 非同步平行 compaction；fine-grained 可控 summary volume |
| [📄 2605.08580](https://arxiv.org/abs/2605.08580) | 2026 | trajectory-grounded 驗證；+8.8pp accuracy / −39.7% latency |
| [📄 2602.16284](https://arxiv.org/abs/2602.16284) | 2026 | latent space KV 壓縮；50× 幾乎無損 |
| [when-better-prompts-hurt-2601-22025](2026-01-29-when-better-prompts-hurt-eval-driven-2601-22025.md) | 2026 | Eval-driven prompt 迭代；MVES；泛用 prompt 反而降準（100%→90%） |
| [promptbridge-2512-01420](2025-12-01-promptbridge-cross-model-prompt-transfer-2512-01420.md) | 2025 | Cross-model prompt transfer；Model Drifting；SWE-Bench +27.39% |
| [memory-in-the-loop-2607-05690](2026-07-06-memory-in-the-loop-in-process-retrieval-2607-05690.md) | 2026 | In-process 記憶 ~100μs；延遲決定記憶是工具還是 working memory |
| [codified-context-infrastructure-2602-20478](2026-02-24-codified-context-infrastructure-ai-agents-2602-20478.md) | 2026 | Hot/cold-memory 二分基礎設施；108K 行 codebase 實測 283 sessions |

---

## Cold-Start / Startup Latency

> 間接相關（serverless/GPU 層），概念遷移至 Claude Code session init / hook spawn 優化。見 reports/2026-06-03-claude-code-cold-start-latency-deep-research.md

| Paper | Year | Core Claim |
|-------|------|------------|
| [hydraserve-2502-15524](2025-02-21-hydraserve-cold-start-serverless-llm-2502-15524.md) | 2025 | Cold start 降 1.7–4.7×；overlap stages + proactive distribution |
| [cold-start-antipatterns-2512-16066](2025-12-19-cold-start-antipatterns-serverless-2512-16066.md) | 2025 | Cold-start 為 developer-visible 設計問題；81 issues → 反模式分類；Amazon +100ms = -1% 銷售 |

---

## Loop / Workflow Engineering

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [sovereign-agentic-loops-2604-22136](2026-04-24-sovereign-agentic-loops-decoupling-reasoning-execution-2604-22136.md) | 2026 | reasoning/execution 分離；intent 驗證擋 93% 不安全動作 | core.md 判斷/決定 |
| [agent-loops-to-graphs-2604-11378](2026-04-13-agent-loops-to-structured-graphs-scheduler-2604-11378.md) | 2026 | DAG 靜態控制流取代 iterative loop + 終止保證 | Workflow · LLM-as-Code |
| [workflow-opt-survey-2603-22386](2026-03-23-survey-workflow-optimization-llm-agents-2603-22386.md) | 2026 | agentic computation graph workflow 優化調查 | — |
| [challenges-iterative-opt-2603-23994](2026-03-25-challenges-iterative-generative-optimization-2603-23994.md) | 2026 | LLM 迭代優化迴圈隱性設計決策 | autoresearch 對照 |
| [evolver-2510-16079](2025-10-17-evolver-self-evolving-agents-experience-lifecycle-2510-16079.md) | 2025 | 離線蒸餾+線上互動自演化 lifecycle | — |
| [sew-2505-18646](2025-05-24-sew-self-evolving-agentic-workflows-code-2505-18646.md) | 2025 | 自動生成/優化多代理 workflow +12% | — |
| [agentcompass-2509-14647](2025-09-18-agentcompass-reliable-evaluation-agentic-workflows-2509-14647.md) | 2025 | 生產 agentic workflow 持續觀測除錯 | — |
| [bayesflow-2601-22305](2026-01-29-bayesflow-probability-inference-workflow-generation-2601-22305.md) | 2026 | Workflow 生成重構為貝氏推論；免訓練；+9pp vs SOTA，+65pp vs zero-shot | — |
| [flowsteer-2602-01664](2026-02-02-flowsteer-agents-designing-agentic-workflows-2602-01664.md) | 2026 | Agent 自行端到端設計 workflow；漸進式原子編輯 + RL policy | — |
| [agent-loops-deterministic-graphs-2605-06365](2026-05-07-agent-loops-to-deterministic-graphs-execution-lineage-2605-06365.md) | 2026 | Execution lineage DAG：可維護性/可重放性 ≠ 單次輸出品質 | handoff 交接文件設計 |
| [engineering-robustness-ai-workflow-store-2605-10907](2026-05-11-engineering-robustness-personal-agents-ai-workflow-store-2605-10907.md) | 2026 | 批評 on-the-fly 範式；主張預先硬化可重用 workflow store | core.md 規範優先 |
| [grade-2606-22741](2026-06-22-grade-graph-representation-agent-dependency-execution-2606-22741.md) | 2026 | 雙層圖（execution+dependency edge）；dependency 層更能定位失敗 | RECORD 失敗歸因到層 |
| [infinite-agentic-loops-2607-01641](2026-07-02-when-agents-do-not-stop-infinite-agentic-loops-2607-01641.md) | 2026 | IAL 靜態偵測：6549 repo 中 68 例無界迴圈失效，precision 91.9% | fan-out child 不 self-retry |

---

## Goal Engineering

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [evaluating-goal-drift-2505-02709](2025-05-05-evaluating-goal-drift-language-model-agents-2505-02709.md) | 2025 | goal drift 評測方法論（10萬 token 壓力）| core.md 成功條件 |
| [inherited-goal-drift-2603-03258](2026-03-03-inherited-goal-drift-contextual-pressure-2603-03258.md) | 2026 | 從弱代理 trajectory 繼承 drift | subagent-strategy off-rails |
| [asymmetric-goal-drift-2603-03456](2026-03-03-asymmetric-goal-drift-coding-agents-2603-03456.md) | 2026 | 非對稱漂移：環境信號繞過 system prompt | — |
| [subgoal-driven-2603-19685](2026-03-20-subgoal-driven-long-horizon-llm-agents-2603-19685.md) | 2026 | 子目標分解+里程碑獎勵抗長程漂移 | — |
| [policy-decompositions-2605-06957](2026-05-07-policy-decompositions-hierarchical-generalized-planning-2605-06957.md) | 2026 | 可重用策略分解庫 62.5% vs ~0 | — |
| [agent-drift-2601-04170](2026-01-07-agent-drift-quantifying-behavioral-degradation-2601-04170.md) | 2026 | 多代理系統行為漂移三分類（語意/協調/行為）+ Agent Stability Index | 記憶整合顯式門控對照 |

---

## Caching / KV Cache / Token Budget

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [prefix-fusion-rag-cache-2601-12904](2026-01-19-prefix-cache-to-fusion-rag-cache-2601-12904.md) | 2026 | RAG prefix cache+選擇性重算 TTFT -2.7~9.4× | context-management caching |
| [saecache-2605-18825](2026-05-12-saecache-semantic-aware-prefix-cache-eviction-2605-18825.md) | 2026 | 語義感知 prefix cache 驅逐 TTFT +1.4~2.7× | — |
| [cacheprobe-2605-30613](2026-05-28-cacheprobe-auditing-prompt-cache-isolation-2605-30613.md) | 2026 | 審計 gateway prompt cache 跨帳戶隔離 | — |
| [cacheweaver-2606-19667](2026-06-18-cacheweaver-cache-aware-evidence-ordering-rag-2606-19667.md) | 2026 | 重排 RAG evidence 最大化 prefix 命中 -20~33% 延遲 | dont-break-cache 對照 |
| [tokendance-2604-03143](2026-04-03-tokendance-multi-agent-kv-cache-sharing-2604-03143.md) | 2026 | 多代理集體共享 KV cache 11~17× 壓縮 | — |
| [conf-kv-2605-24786](2026-05-24-conf-kv-confidence-aware-kv-cache-eviction-2605-24786.md) | 2026 | confidence 決定 cache budget + 混合精度 | — |
| [indexmem-2605-25475](2026-05-25-indexmem-learned-kv-cache-eviction-2605-25475.md) | 2026 | 可學 indexer 預測 token 重要性 | — |
| [tangram-2606-06302](2026-06-04-tangram-non-uniform-kv-cache-compression-2606-06302.md) | 2026 | 非均勻 KV 壓縮 +2.6× 吞吐 | — |
| [swiftcache-2606-16135](2026-06-15-swiftcache-heterogeneous-kv-cache-sharing-2606-16135.md) | 2026 | 跨異質模型共享 KV；P99 TTFT -69% | — |
| [nexus-sampling-2606-23961](2026-06-22-nexus-sampling-streaming-kv-cache-eviction-2606-23961.md) | 2026 | 概率式 streaming KV 驅逐 80% 縮減 | — |
| [compresskv-2606-24467](2026-06-23-compresskv-semantic-retrieval-kv-cache-compression-2606-24467.md) | 2026 | Semantic Retrieval Heads 引導壓縮；3% cache 保 97% | — |
| [dual-pool-token-budget-2604-08075](2026-04-09-dual-pool-token-budget-routing-2604-08075.md) | 2026 | 雙池 token budget 路由 GPU -31~42% | — |
| [token-budgets-overrun-2606-04056](2026-06-02-token-budgets-overrun-incidents-affine-rust-2606-04056.md) | 2026 | 63 件 token 超支事故 + Rust affine 防護 | context-management token budget |
| [coupling-tax-2605-07686](2026-05-08-coupling-tax-shared-token-budgets-cot-2605-07686.md) | 2026 | 共享 token budget 擠壓 CoT；split-budget 解法 | — |
| [summaries-distort-decisions-2606-29251](2026-06-28-when-summaries-distort-decisions-information-fidelity-2606-29251.md) | 2026 | 壓縮保真判準=決策等價；decontextualization + model dependency 兩失真模式 | output-compress fidelity gate |
| [info-preservation-compression-2503-19114](2025-03-24-information-preservation-prompt-compression-2503-19114.md) | 2025 | 三軸評估（performance/grounding/preservation）；granularity 控制 +23% | output-compress 失真閘量測維度 |
| [scaling-paradox-compression-2602-09789](2026-02-10-llm-scaling-paradox-context-compression-2602-09789.md) | 2026 | Size-Fidelity Paradox：大壓縮器 knowledge overwriting + semantic drift | output-compress 檔位上限佐證 |
| [prompt-compression-survey-2410-12388](2024-10-16-prompt-compression-survey-2410-12388.md) | 2024 | hard vs soft prompt 壓縮綜述 + 四機制視角 | output-compress 領域地圖 |
| [context-to-edus-2512-14244](2025-12-16-context-to-edus-faithful-structured-compression-2512-14244.md) | 2025 | EDU 結構樹分解-選取（不改寫）壓縮；StructBench 248 docs | output-compress whitelist 結構化參照 |
| [token-budget-aware-2412-18547](2024-12-24-token-budget-aware-llm-reasoning-2412-18547.md) | 2024 | CoT 冗長可用 prompt 內 token budget 壓縮；動態 budget 估算 | output-compress 分級 budget |
| [budgetthinker-2508-17196](2025-08-24-budgetthinker-budget-aware-reasoning-control-tokens-2508-17196.md) | 2025 | 推理中插 control token 回報剩餘 budget；SFT+RL 訓練 | — |
| [tokenpilot-2606-17016](2026-06-15-tokenpilot-cache-efficient-context-management-2606-17016.md) | 2026 | 雙粒度 context 管理；-61~87% 成本同時維持 cache 命中 | context-management caching |
| [kv-packet-2604-13226](2026-04-14-kv-packet-recomputation-free-context-independent-2604-13226.md) | 2026 | 快取封包化+soft-token adapter；context-independent 重用近零 FLOPs | — |
| [agent-memory-below-prompt-2603-04428](2026-02-17-agent-memory-below-prompt-persistent-q4-kv-cache-2603-04428.md) | 2026 | 多代理 Q4 KV cache 持久化落盤；邊緣裝置 10+ agent 並行 | — |
| [kveraser-2606-17034](2026-06-15-kveraser-steer-kv-cache-localized-context-erasing-2606-17034.md) | 2026 | 學習式局部抹除 KV cache；延遲僅 +24% vs 全量重算 17.6× | — |

---

## Model / System Cards

> web-only：Anthropic 官方 system card 無 arXiv PDF（Source 為官網 URL）；OpenAI 為官方 CDN PDF 全文歸檔。

| Paper | Year | Core Claim | Workspace Use |
|-------|------|------------|--------------|
| [claude-fable-5-mythos-5-card](2026-06-09-claude-fable-5-mythos-5-system-card.md) | 2026 | Fable 5/Mythos 5；SWE-bench ~95.5%（web-only）| fable-pilot |
| [claude-opus-4-8-card](2026-05-28-claude-opus-4-8-system-card.md) | 2026 | Opus 4.8（本 session 模型）；model welfare 章（web-only）| opus-pilot |
| [claude-sonnet-4-6-card](2026-02-17-claude-sonnet-4-6-system-card.md) | 2026 | Sonnet 4.6；1M context（web-only）| sonnet-pilot |
| [claude-mythos-preview-card](2026-04-07-claude-mythos-preview-system-card.md) | 2026 | Mythos Preview 未 GA；cyber 能力（web-only）| — |
| [claude-opus-4-5-card](2025-11-01-claude-opus-4-5-system-card.md) | 2025 | Opus 4.5；agentic 躍升（web-only）| — |
| [claude-haiku-4-5-card](2025-10-01-claude-haiku-4-5-system-card.md) | 2025 | Haiku 4.5；ASL-2 高對齊（web-only）| haiku-pilot |
| [claude-sonnet-4-5-card](2025-09-01-claude-sonnet-4-5-system-card.md) | 2025 | Sonnet 4.5（web-only）| sonnet-pilot |
| [claude-opus-4-1-card](2025-08-01-claude-opus-4-1-system-card.md) | 2025 | Opus 4.1 addendum（web-only）| — |
| [claude-opus-4-sonnet-4-card](2025-05-22-claude-opus-4-sonnet-4-system-card.md) | 2025 | Claude 4 系列首卡（web-only）| model-selection |
| [openai-gpt-5-4-thinking-card](2026-03-05-openai-gpt-5-4-thinking-system-card.md) | 2026 | GPT-5.4 Thinking；High cyber 緩解 | — |
| [openai-chatgpt-agent-card](2025-07-17-openai-chatgpt-agent-system-card.md) | 2025 | ChatGPT Agent；Bio/Chem High capability | — |
| [openai-o3-o4-mini-card](2025-04-16-openai-o3-o4-mini-system-card.md) | 2025 | o3/o4-mini；Preparedness V2 首發 | — |
| [openai-o3-mini-card](2025-01-31-openai-o3-mini-system-card.md) | 2025 | o3-mini；首個 Model Autonomy=Medium | — |

---

## Other

| Paper | Year | Core Claim |
|-------|------|------------|
| [anthropic-economic-2511-15080](2025-11-19-anthropic-economic-index-geographic-adoption-2511-15080.md) | 2025 | 地理採用經濟指標 |
| [which-economic-tasks-2503-04761](2025-03-07-which-economic-tasks-ai-claude-conversations-2503-04761.md) | 2025 | AI 可替代任務分析 |
| [formal-methods-robot-policy-2602-06971](2026-01-09-formal-methods-robot-policy-2602-06971.md) | 2026 | 形式化方法 × 機器人策略驗證；安全認證技術調查 |
| [neuromorphic-low-power-ai-2604-04727](2026-04-06-neuromorphic-low-power-ai-2604-04727.md) | 2026 | 神經形態運算低功耗 AI；脈衝神經網路 vs 傳統 DNN |
| [neuromorphic-supremacy-2606-01841](2026-06-01-neuromorphic-supremacy-2606-01841.md) | 2026 | 神經形態架構效能最優性論證 |

---

## AI Alignment / Constitutional AI

> PDF 下載來源：arxiv.org

| Paper | Year | ArXiv | Core Claim |
|-------|------|-------|------------|
| [2022-12-15 Constitutional AI](2022-12-15-constitutional-ai-harmlessness-ai-feedback-2212-08073.md) [📄](https://arxiv.org/abs/2212.08073) | 2022 | 2212.08073 | Constitutional AI：RLHF + CAI；無人工標注harmlessness |
| [2023-09-01 RLAIF vs RLHF](2023-09-01-rlaif-vs-rlhf-ai-feedback-2309-00267.md) [📄](https://arxiv.org/abs/2309.00267) | 2023 | 2309.00267 | RLAIF vs RLHF：AI Feedback 可替代人工 |
| [2023-12-14 Weak-to-Strong](2023-12-14-weak-to-strong-generalization-2312-09390.md) [📄](https://arxiv.org/abs/2312.09390) | 2023 | 2312.09390 | Weak-to-Strong Generalization：弱監督引導強模型 |
| [2024-02-09 Debate](2024-02-09-debating-persuasive-llms-truthful-answers-2402-06782.md) [📄](https://arxiv.org/abs/2402.06782) | 2024 | 2402.06782 | Debate：更具說服力的 LLM → 更真實的答案 |

---

## AI Safety / Red Teaming

> PDF 下載來源：arxiv.org

| Paper | Year | ArXiv | Core Claim |
|-------|------|-------|------------|
| [2022-02-07 LM Red Team](2022-02-07-red-teaming-language-models-2202-03286.md) [📄](https://arxiv.org/abs/2202.03286) | 2022 | 2202.03286 | 用 LM 自動 red team 另一個 LM |
| [2023-07-27 GCG](2023-07-27-universal-adversarial-attacks-aligned-llm-2307-15043.md) [📄](https://arxiv.org/abs/2307.15043) | 2023 | 2307.15043 | GCG：通用對抗後綴；可遷移至黑盒模型 |
| [2024-02-06 HarmBench](2024-02-06-harmbench-automated-red-teaming-2402-04249.md) [📄](https://arxiv.org/abs/2402.04249) | 2024 | 2402.04249 | HarmBench：自動 red teaming 標準化評估框架 |
| [2024-06-26 WildTeaming](2024-06-26-wildteaming-scale-jailbreaks-safer-llm-2406-18510.md) [📄](https://arxiv.org/abs/2406.18510) | 2024 | 2406.18510 | WildTeaming：野外 jailbreak → 對抗安全訓練資料 |

---

## Diffusion Language Models

> PDF 下載來源：arxiv.org

| Paper | Year | ArXiv | Core Claim |
|-------|------|-------|------------|
| [2023-10-25 SEDD](2023-10-25-sedd-discrete-diffusion-score-entropy-2310-16834.md) [📄](https://arxiv.org/abs/2310.16834) | 2023 | 2310.16834 | SEDD：離散擴散 score entropy；ICML 2024 Oral |
| [2024-06-11 MDLM](2024-06-11-mdlm-simple-effective-masked-diffusion-lm-2406-07524.md) [📄](https://arxiv.org/abs/2406.07524) | 2024 | 2406.07524 | MDLM：簡單有效的 masked diffusion LM |
| [2024-10-18 MGDM](2024-10-18-discrete-diffusion-reasoning-planning-mgdm-2410-14157.md) [📄](https://arxiv.org/abs/2410.14157) | 2024 | 2410.14157 | MGDM：離散擴散複雜推理超越自回歸 |
| [2025-02-14 LLaDA](2025-02-14-llada-large-language-diffusion-models-2502-09992.md) [📄](https://arxiv.org/abs/2502.09992) | 2025 | 2502.09992 | LLaDA：大型語言擴散模型；指令遵循 |

---

## Mechanistic Interpretability

> ⚠️ Anthropic transformer-circuits.pub 論文為網頁格式，無傳統 PDF；僅 Toy Superposition 有 arxiv PDF。

| Paper | Year | ArXiv / URL | Core Claim |
|-------|------|-------------|------------|
| [2022-09-21 Toy Superposition](2022-09-21-toy-models-superposition-2209-10652.md) [📄](https://arxiv.org/abs/2209.10652) | 2022 | 2209.10652 | Toy Models of Superposition：特徵疊加機制 |
| [2023-10-04 Monosemanticity](2023-10-04-towards-monosemanticity-dictionary-learning.md) 🌐 | 2023 | transformer-circuits.pub | 字典學習分解 LM；monosemantic features |
| [2024-05-23 Scaling Monosemanticity](2024-05-23-scaling-monosemanticity-claude3-sonnet.md) 🌐 | 2024 | transformer-circuits.pub | SAE 擴展至 Claude 3 Sonnet；1600 萬 features |
| [2025-03-27 Circuit Tracing](2025-03-27-circuit-tracing-attribution-graphs-language-models.md) 🌐 | 2025 | transformer-circuits.pub | Circuit Tracing：歸因圖揭示計算電路 |
| [2026-05-25 Tool-Call Dependency](2026-05-25-tool-call-dependency-linearly-decodable-2605-25310.md) [📄](https://arxiv.org/abs/2605.25310) | 2026 | 2605.25310 | Residual stream 線性可解碼工具呼叫依賴圖 |

---

## Multimodal / Vision-Language

> PDF 下載來源：arxiv.org

| Paper | Year | ArXiv | Core Claim |
|-------|------|-------|------------|
| [2022-04-29 Flamingo](2022-04-29-flamingo-visual-language-model-few-shot-2204-14198.md) [📄](https://arxiv.org/abs/2204.14198) | 2022 | 2204.14198 | Flamingo：少樣本視覺語言模型；cross-attention |
| [2023-01-30 BLIP-2](2023-01-30-blip2-language-image-pretraining-frozen-encoders-2301-12597.md) [📄](https://arxiv.org/abs/2301.12597) | 2023 | 2301.12597 | BLIP-2：凍結視覺+LLM；Q-Former 橋接 |
| [2023-04-17 LLaVA](2023-04-17-llava-visual-instruction-tuning-2304-08485.md) [📄](https://arxiv.org/abs/2304.08485) | 2023 | 2304.08485 | LLaVA：視覺指令調優；GPT-4 生成訓練資料 |
| [2023-10-05 LLaVA-1.5](2023-10-05-llava-1-5-improved-visual-instruction-tuning-2310-03744.md) [📄](https://arxiv.org/abs/2310.03744) | 2023 | 2310.03744 | LLaVA-1.5：MLP connector + CLIP；11個基準SOTA |

---

## Test-Time Compute

> PDF 下載來源：arxiv.org

| Paper | Year | ArXiv | Core Claim |
|-------|------|-------|------------|
| [2023-05-31 Let's Verify Step by Step](2023-05-31-lets-verify-step-by-step-process-reward-2305-20050.md) [📄](https://arxiv.org/abs/2305.20050) | 2023 | 2305.20050 | Let's Verify Step by Step：PRM 過程獎勵模型 |
| [2024-08-06 Snell Scaling](2024-08-06-scaling-llm-test-time-compute-2408-03314.md) [📄](https://arxiv.org/abs/2408.03314) | 2024 | 2408.03314 | Test-time compute scaling 優於 model scaling |
| [2025-01-22 DeepSeek-R1](2025-01-22-deepseek-r1-reasoning-reinforcement-learning-2501-12948.md) [📄](https://arxiv.org/abs/2501.12948) | 2025 | 2501.12948 | DeepSeek-R1：RL 強化推理；o1 同等效能 |
| [2025-01-31 s1](2025-01-31-s1-simple-test-time-scaling-2501-19393.md) [📄](https://arxiv.org/abs/2501.19393) | 2025 | 2501.19393 | s1：簡單 test-time scaling；1K 問題蒸餾 |
| [2026-04-22 SGS](2026-04-22-scaling-self-play-with-self-guidance-2604-20209.md) [📄](https://arxiv.org/abs/2604.20209) | 2026 | 2604.20209 | Self-Guided Self-Play：三角色（Solver/Conjecturer/Guide）防止 Conjecturer 崩潰；7B 模型超越 671B baseline（Lean4 定理證明） |
