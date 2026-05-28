---
title: "AgentFlow: Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"
authors: "Hanzhi Liu, Chaofan Shou, Xiaonan Liu, Hongbo Wen, Yanju Chen, Ryan Jingyang Fang, Yu Feng"
published: 2026-04-22
source: "https://arxiv.org/abs/2604.20801"
---

# AgentFlow: Synthesizing Multi-Agent Harnesses for Vulnerability Discovery

**Authors**: Hanzhi Liu, Chaofan Shou, Xiaonan Liu, Hongbo Wen, Yanju Chen, Ryan Jingyang Fang, Yu Feng  
**Published**: April 22, 2026  
**Source**: https://arxiv.org/abs/2604.20801  
**arXiv ID**: 2604.20801  
**DOI**: https://doi.org/10.48550/arXiv.2604.20801  
**Categories**: cs.CR (Cryptography and Security)  
**License**: CC BY-NC-ND 4.0

---

## Abstract

We present AgentFlow, a system that automatically synthesizes multi-agent harnesses for LLM-based software vulnerability discovery. Existing agent harnesses for security tasks are hand-engineered, fixing agent roles, communication topology, tool bindings, and coordination protocols in place. When these designs fail, practitioners have no principled way to diagnose which component caused the failure or how to repair it. AgentFlow addresses this by introducing a typed graph domain-specific language (DSL) whose search space jointly covers all five harness dimensions: agent roles (𝒜), communication topology (𝒢), message schemas (Σ), tool bindings (Φ), and coordination protocol (Ψ). The system collects structured runtime signals from target programs—test verdicts, standard output/error streams, line-level coverage, and sanitizer reports—and uses these signals to diagnose why failures occur and guide iterative harness rewrites. On TerminalBench-2, AgentFlow achieves 84.3% pass rate using Claude Opus 4.6, the highest score among all Claude Opus 4.6 entries and 2.9 percentage points above the hand-engineered ForgeCode baseline. Applied to Google Chrome with the open-weight Kimi K2.5 model, AgentFlow discovers ten previously unknown zero-day vulnerabilities, including two Critical sandbox-escape vulnerabilities (CVE-2026-5280 and CVE-2026-6297), demonstrating that automated harness synthesis generalizes across models and vulnerability classes.

---

## 1. Introduction

The deployment of large language models for security vulnerability discovery has grown rapidly. Systems such as LLM4Vuln, CyberSecEval, and AutoCodeRover demonstrate that LLM agents can find real bugs in real software, sometimes matching expert human auditors on constrained tasks. However, the performance of these systems depends critically on how multiple agents are orchestrated—which agents communicate with which, what tools each agent has access to, how failures in one agent trigger retries or escalation in another. This orchestration layer is the **harness**.

Harnesses are currently designed by hand. Practitioners make sequential decisions about agent roles, communication graphs, message schemas, tool assignments, and coordination rules based on intuition and empirical trial-and-error. When a harness underperforms, diagnosing the root cause is difficult: did the analyzer agent fail to identify the right code path? Did the fuzzer agent receive insufficient context? Did a communication bottleneck prevent relevant information from reaching the exploit generator? Without systematic tooling, these questions are answered by expensive manual iteration.

We identify three root causes of this problem:

1. **Expressiveness gap**: Prior automated harness search systems fix one or more harness dimensions. ADAS searches agent prompts but not topology. AFlow searches workflow structure but holds agent roles constant. MaAS optimizes coordination but assumes a fixed agent pool. No prior system searches all five dimensions simultaneously.

2. **Feedback poverty**: Most automated harness optimization systems use binary pass/fail signals. A harness either solved the task or it did not. This provides no gradient for diagnosing *which component* caused failure, forcing the optimizer to treat each iteration as a black-box sample.

3. **Type unsafety**: Without a formal grammar for harnesses, LLM-generated harness edits frequently produce syntactically or semantically malformed programs that fail silently or cause runtime errors, wasting expensive execution budget.

AgentFlow addresses all three root causes:

1. A **typed graph DSL** with first-class support for all five harness dimensions enables cross-component edits that prior systems cannot express.
2. **Runtime-feedback-driven optimization** collects structured signals (coverage deltas, sanitizer reports, per-agent output logs) and uses them to localize failures to specific agents and interactions.
3. A **three-rule type system** that rejects malformed harness proposals before execution, eliminating ~20% of LLM-generated proposals cheaply.

### 1.1 Contributions

The primary contributions of this paper are:

1. **AgentFlow**: the first system to jointly optimize all five harness dimensions using a unified typed graph DSL.
2. **Runtime-feedback-driven diagnosis**: a feedback collection and analysis mechanism that attributes failures to specific harness components.
3. **TerminalBench-2 results**: 84.3% pass rate with Claude Opus 4.6, state-of-the-art on the public leaderboard.
4. **Real-world vulnerability discovery**: 10 zero-day vulnerabilities in Google Chrome, including 2 Critical sandbox-escape CVEs, using the open-weight Kimi K2.5 model.
5. **Ablation analysis** quantifying the contribution of each harness dimension to overall performance.

---

## 2. Background and Related Work

### 2.1 LLM Agents for Security

LLM agents have been applied to several security tasks: automated patch generation (VulRepair), bug triaging (BugsBunny), and exploit synthesis (EXP-SAT). The most ambitious systems attempt end-to-end vulnerability discovery: given a program, find a previously unknown bug and demonstrate it with a working exploit or proof-of-concept. TerminalBench-2 standardizes this task across 200 diverse programs, enabling systematic comparison.

### 2.2 Multi-Agent Systems

Multi-agent frameworks for LLM tasks have proliferated: AutoGen, CrewAI, LangGraph, MetaGPT, and others provide primitives for agent creation and coordination. However, these are programming frameworks, not optimization targets. The harness is written in Python or a configuration DSL by a human developer, and the framework executes it.

The question AgentFlow addresses is different: can the harness itself be automatically synthesized and improved?

### 2.3 Automated Harness Search

Several systems have approached automated harness search:

| System | Roles (𝒜) | Topology (𝒢) | Schemas (Σ) | Tools (Φ) | Protocol (Ψ) |
|---|---|---|---|---|---|
| Meta-Harness | Fixed (1) | Fixed | Fixed | Fixed | Fixed |
| ADAS | Searched | Fixed | Fixed | Fixed | Fixed |
| AFlow | Fixed | Searched | Fixed | Fixed | Fixed |
| MaAS | Fixed | Fixed | Fixed | Fixed | Searched |
| **AgentFlow** | **Searched** | **Searched** | **Searched** | **Searched** | **Searched** |

AgentFlow is the first system to search all five dimensions simultaneously within a single unified grammar.

### 2.4 Program Analysis Feedback

Using program analysis feedback to guide automated testing is well-established in the fuzzing literature (AFL, LibFuzzer, Honggfuzz). Coverage-guided fuzzing uses branch coverage as a fitness signal to direct input mutation. AgentFlow adapts this paradigm to LLM agent optimization: structured runtime signals replace branch coverage as the gradient signal for harness improvement.

---

## 3. The AgentFlow DSL

### 3.1 Harness as Typed Graph Program

A harness in AgentFlow is a program in the typed graph DSL. The program defines:

- A set of **agent nodes** 𝒜 = &#123;a₁, a₂, ..., aₙ&#125;, each with a role description, system prompt, and assigned tool bindings Φᵢ.
- A **communication graph** 𝒢 = (𝒜, E), where edges E ⊆ 𝒜 × 𝒜 define which agents can send messages to which.
- **Message schemas** Σ: E → Schema, defining the typed structure of messages on each edge.
- A **coordination protocol** Ψ specifying: sequencing constraints (which agents must complete before others begin), retry logic (conditions under which an agent is re-invoked), and termination conditions.

Formally, a harness H = (𝒜, 𝒢, Σ, Φ, Ψ) is a well-typed program if and only if it satisfies three syntactic rules:

- **Rule 1 (Reachability)**: Every agent node is reachable from the entry node via edges in 𝒢.
- **Rule 2 (Schema Consistency)**: For every edge (aᵢ, aⱼ) ∈ E, the output schema of aᵢ is a subtype of the input schema of aⱼ.
- **Rule 3 (Protocol Acyclicity)**: The sequencing constraints in Ψ form a directed acyclic graph (no circular wait conditions).

In practice, these three rules reject approximately 20% of LLM-generated harness proposals before any execution takes place, saving significant compute.

### 3.2 DSL Serialization

Harnesses are serialized as structured JSON documents following a fixed schema. This serialization format serves two purposes: it is machine-readable (enabling automated type checking), and it is human-readable (enabling LLMs to generate and edit harnesses as structured text).

A minimal example harness for a two-agent vulnerability analysis task:

```json
{
  "agents": [
    {
      "id": "analyzer",
      "role": "Code path analyzer",
      "prompt": "Analyze the target program for potential attack surfaces...",
      "tools": ["read_file", "run_static_analysis", "trace_execution"]
    },
    {
      "id": "exploiter",
      "role": "Exploit generator",
      "prompt": "Given the attack surface report, generate a proof-of-concept exploit...",
      "tools": ["write_file", "run_program", "check_sanitizer"]
    }
  ],
  "topology": {
    "edges": [["analyzer", "exploiter"]],
    "entry": "analyzer"
  },
  "schemas": {
    "analyzer->exploiter": {
      "attack_surfaces": "list[AttackSurface]",
      "coverage_report": "CoverageReport"
    }
  },
  "protocol": {
    "sequence": ["analyzer", "exploiter"],
    "retry": {"exploiter": {"on_failure": "rerun", "max_attempts": 3}},
    "termination": {"condition": "exploiter.success OR max_iterations_reached"}
  }
}
```

---

## 4. The AgentFlow Optimization Algorithm

### 4.1 Core Loop

AgentFlow optimizes harnesses through an iterative four-phase loop (Algorithm 1):

**Phase 1 — Propose**: Given the current harness H_t and a diagnostic report D_t (described below), an LLM proposes a new harness H_{t+1}. The proposal prompt includes: the current harness serialization, the diagnostic report, the type system rules (as constraints to satisfy), and a budget for how many agents and edges are allowed.

**Phase 2 — Execute & Observe**: H_{t+1} is executed on all tasks in the evaluation set. For each task, structured runtime signals are collected:
- **Test verdicts**: pass/fail for each test case.
- **Standard output/error**: per-agent output streams, labeled with the agent ID that produced them.
- **Line-level coverage**: which lines of the target program were reached during the harness execution.
- **Sanitizer reports**: AddressSanitizer, UBSanitizer, or MemorySanitizer reports if triggered.

**Phase 3 — Score**: An aggregate score S(H_{t+1}) is computed as a weighted combination of task success rate, coverage breadth (fraction of unique lines reached across all tasks), and crash uniqueness (number of distinct crash signatures observed).

**Phase 4 — Diagnose**: An LLM diagnostic agent analyzes the per-task runtime signals and produces a structured diagnostic report D_{t+1} identifying:
- Which agent(s) produced low-quality or missing output for failing tasks.
- Which communication edges appear bottlenecked (high message volume with low downstream success rate).
- Which tool calls failed most frequently.
- Suggested corrective edits (e.g., "expand the analyzer agent's prompt to include buffer overflow patterns," "add a validation step between analyzer and exploiter").

The loop terminates when either a success threshold is met, the iteration budget is exhausted, or the score fails to improve for three consecutive iterations (early stopping).

### 4.2 Feedback Attribution

A key challenge in diagnosis is attributing a task failure to a specific harness component. Naive attribution (blaming the last agent in the pipeline) is incorrect for the majority of failures, which stem from information losses or mismatches earlier in the pipeline.

AgentFlow's attribution mechanism uses a combination of:

1. **Coverage delta analysis**: If the coverage report for a failing task is substantially lower than for passing tasks, the failure likely occurred in an early exploration agent rather than in the exploit generator.

2. **Output quality scoring**: Each agent's output is scored by a lightweight evaluator model for completeness relative to its role specification. Low-scoring intermediate outputs indicate the failure source.

3. **Schema violation detection**: Even when no type error occurs, output that technically satisfies the schema but omits expected fields is flagged by comparing against an expected output template.

This three-signal attribution reduces diagnostic error to approximately 15% of cases in our evaluation (measured against human expert diagnosis on a 50-task subset).

---

## 5. Experiments

### 5.1 TerminalBench-2

TerminalBench-2 is a benchmark of 200 vulnerability discovery tasks spanning diverse program classes: C/C++ programs with memory safety vulnerabilities, Python packages with logic errors, and Rust programs with concurrency bugs. Tasks are evaluated by checking whether the submitted exploit or proof-of-concept triggers the intended vulnerability on a clean test environment.

**Setup**: We evaluate AgentFlow using Claude Opus 4.6 as the backbone model for all agents. The optimization loop runs for up to 20 iterations with a budget of 500 harness executions total. We compare against:
- **Single-agent baseline**: a single Claude Opus 4.6 agent with the same tool access as the AgentFlow harness but no multi-agent coordination.
- **ForgeCode**: the top-ranked hand-engineered harness on TerminalBench-2 prior to this work (81.4% pass rate).
- **ADAS**: automated design using prompt-only search.
- **AFlow**: automated design using workflow structure search.

**Results (RQ1 — Benchmark Performance)**:

| System | Model | Pass Rate |
|---|---|---|
| Single-agent | Claude Opus 4.6 | 67.2% |
| ADAS | Claude Opus 4.6 | 74.8% |
| AFlow | Claude Opus 4.6 | 76.5% |
| ForgeCode (hand-engineered) | Claude Opus 4.6 | 81.4% |
| **AgentFlow** | Claude Opus 4.6 | **84.3%** |

AgentFlow achieves 84.3%, a 2.9 percentage point improvement over the best hand-engineered baseline and the highest score among all Claude Opus 4.6 entries on the TerminalBench-2 leaderboard at submission time.

**Final harness architecture** (synthesized by AgentFlow for TerminalBench-2): 9 specialized agent roles organized across 5 sequential phases, with 3 parallel workspace agents operating concurrently in the exploration phase. Key roles include: surface-mapper (static analysis), dynamic-tracer (execution tracing), crash-triager (crash deduplication and severity classification), schema-extractor (input format reverse engineering), and exploit-synthesizer.

### 5.2 Ablation Study (RQ2 — Component Contributions)

To measure the contribution of each harness dimension, we perform ablations that restrict the search space by fixing one dimension at a time while allowing the other four to be optimized.

| Configuration | Pass Rate | Delta vs. Full |
|---|---|---|
| Full AgentFlow (all 5 dims) | 84.3% | — |
| Without prompt optimization (Σ fixed) | 51.8% | −32.5 pp |
| Without topology search (𝒢 fixed) | 77.4% | −6.9 pp |
| Without tool binding optimization (Φ fixed) | 79.1% | −5.2 pp |
| Without protocol optimization (Ψ fixed) | 81.7% | −2.6 pp |
| Without role search (𝒜 fixed) | 82.6% | −1.7 pp |

The most impactful dimension is prompt optimization (−32.5 pp when disabled), confirming that the quality of agent instructions is the primary determinant of performance. Topology search is the second most impactful (−6.9 pp), reflecting the importance of appropriate information flow between agents. Tool binding and protocol optimizations provide additional but smaller gains.

### 5.3 Real-World Vulnerability Discovery in Google Chrome (RQ3)

To evaluate generalization beyond benchmarks, we applied AgentFlow to Google Chrome—a 35M+ line C++ codebase with a mature security team and an active bug bounty program. We used the open-weight **Kimi K2.5** model rather than Claude Opus 4.6 to demonstrate model-agnosticism.

**Setup**: The Chrome harness was synthesized by AgentFlow using a 48-hour optimization window and a seed harness consisting of a two-agent (analyzer + fuzzer) configuration. The final synthesized harness consisted of 18 specialized agent roles with 192 parallel explorer agents covering distinct Chrome subsystems, and 6 feedback loops for crash triage and deduplication.

**Results**: AgentFlow discovered **10 previously unknown zero-day vulnerabilities** in Chrome:

| CVE | Severity | Component | Vulnerability Class |
|---|---|---|---|
| CVE-2026-5280 | **Critical** | Sandbox | Sandbox escape via IPC type confusion |
| CVE-2026-6297 | **Critical** | Sandbox | Sandbox escape via shared memory race |
| CVE-2026-5391 | High | V8 | Use-after-free in garbage collector |
| CVE-2026-5512 | High | Blink | Heap overflow in SVG renderer |
| CVE-2026-5634 | High | Network | Buffer overflow in HTTP/3 parser |
| CVE-2026-5788 | Medium | WebGPU | Out-of-bounds read in shader compiler |
| CVE-2026-5801 | Medium | PDF | Integer overflow in PDF renderer |
| CVE-2026-5923 | Medium | Audio | Use-after-free in WebAudio |
| CVE-2026-6011 | Low | Permissions | TOCTOU in permission manager |
| CVE-2026-6184 | Low | DevTools | Information leak in DevTools protocol |

All ten vulnerabilities were reported to Google via the Chrome security bug tracker and confirmed by the Chrome security team. The two Critical sandbox-escape vulnerabilities (CVE-2026-5280 and CVE-2026-6297) were patched within 14 days of disclosure.

This result demonstrates that AgentFlow's harness synthesis generalizes to: (1) a much larger and more complex codebase than the benchmark programs, (2) a different backbone model (Kimi K2.5 vs. Claude Opus 4.6), and (3) a task requiring multi-stage exploitation chains rather than single-vulnerability triggers.

---

## 6. Analysis and Discussion

### 6.1 Why Prompt Optimization Dominates

The ablation result showing prompt optimization as the dominant contributor (−32.5 pp) warrants discussion. We hypothesize that this reflects the brittle sensitivity of LLM agent performance to precise instruction phrasing—a property well-documented in the prompt engineering literature. When agents receive vague role descriptions, they tend to produce generic outputs that fail to trigger specific vulnerability classes. Precise, targeted prompts that reference specific bug patterns (e.g., "focus on integer overflow in arithmetic operations before memory allocation calls") dramatically improve agent effectiveness on those patterns.

This sensitivity is both an opportunity (small prompt improvements yield large performance gains) and a challenge (prompts optimized for one vulnerability class may underperform on others). AgentFlow's optimization loop naturally discovers task-appropriate prompt specializations that would be difficult to engineer manually.

### 6.2 Emergent Harness Structures

Qualitative analysis of the harnesses synthesized by AgentFlow reveals several structural patterns not present in human-designed baselines:

**Parallel exploration with shared crash pool**: The TerminalBench-2 harness and the Chrome harness both exhibit a structure where many independent explorer agents share a common crash pool with deduplication. This pattern, absent from all hand-engineered baselines, significantly increases crash diversity.

**Feedback loops for crash triage**: Synthesized harnesses consistently include a feedback loop where a triage agent re-examines crashes and reroutes promising ones to specialized deep-analysis agents. This "two-pass" triage structure was not in the seed harness and emerged through optimization.

**Schema specialization**: Early in optimization, message schemas are broad. As optimization progresses, schemas narrow—containing more specific fields tailored to the vulnerability classes most prevalent in the task set. This schema narrowing improves information density and reduces noise in downstream agents.

### 6.3 Ethical Considerations

The application of automated vulnerability discovery to real production software raises ethical questions. Our disclosure process followed responsible vulnerability disclosure guidelines: all vulnerabilities were reported to the affected vendor (Google) before any public disclosure, a 90-day disclosure window was observed, and no exploit code is released in this paper or its associated artifacts.

We also note that the same capabilities that enable offensive vulnerability discovery can improve defensive security: the synthesized Chrome harnesses can be run by the Chrome security team to discover vulnerabilities in upcoming releases before they reach users.

### 6.4 Limitations

**Optimization cost**: Each AgentFlow optimization run requires 500+ harness executions, which is expensive in both time and compute. For TerminalBench-2 tasks (typically resolving in seconds), this is feasible. For targets like Chrome (where harness executions can take hours), optimization is limited to a shorter horizon.

**Seed harness sensitivity**: AgentFlow initializes from a seed harness. Experiments with different seeds show variance of ±2.3 pp on TerminalBench-2, suggesting that while AgentFlow consistently improves over its seed, the final result depends partially on the starting point.

**Generalization to non-C/C++ targets**: Most TerminalBench-2 tasks and the Chrome evaluation involve memory-unsafe languages. The approach should generalize to memory-safe languages (Rust, Go), but this has not been empirically validated in the current work.

---

## 7. Conclusion

We presented AgentFlow, the first system to automatically synthesize multi-agent harnesses across all five harness dimensions using a typed graph DSL and runtime-feedback-driven optimization. AgentFlow achieves state-of-the-art performance on TerminalBench-2 (84.3%, +2.9 pp over the best hand-engineered baseline) and discovers ten real zero-day vulnerabilities in Google Chrome, including two Critical sandbox-escape CVEs.

The key insight of this work is that **harness design is a first-class optimization problem**: the orchestration structure that coordinates multiple LLM agents is at least as important as the agents' individual capabilities or the backbone model used. By treating harness synthesis as a search problem in a well-typed, structured search space, AgentFlow makes systematic harness optimization tractable.

Future directions include: (1) extending the DSL to support dynamic harness reconfiguration during execution (currently the harness structure is fixed before execution begins); (2) developing more efficient optimization algorithms that reduce the 500-execution budget; and (3) applying AgentFlow to vulnerability discovery in other domains (mobile applications, smart contracts, industrial control systems).

Artifacts (DSL specification, synthesis algorithm implementation, synthesized harnesses for TerminalBench-2) will be released publicly under CC BY-NC-ND 4.0.

---

## References

1. Liu, H. et al. (2025). LLM4Vuln: A Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning. *arXiv:2401.16185*.
2. Shao, S. et al. (2024). CyberSecEval: A Comprehensive Evaluation of Cybersecurity Risks and Capabilities in Large Language Models. *arXiv:2408.01605*.
3. Chen, C. et al. (2024). AutoCodeRover: Autonomous Program Improvement. *ISSTA 2024*.
4. Wu, T. et al. (2024). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. *arXiv:2308.08155*.
5. Hong, S. et al. (2024). MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework. *ICLR 2024*.
6. Fernando, C. et al. (2024). Automated Design of Agentic Systems. *arXiv:2408.08435*.
7. Zhao, A. et al. (2024). AFlow: Automating Agentic Workflow Generation. *arXiv:2410.10762*.
8. Zhang, H. et al. (2025). MaAS: Multi-Agent Architecture Search. *arXiv:2502.04180*.
9. Bohme, M. et al. (2017). Coverage-Based Greybox Fuzzing as Markov Chain. *CCS 2017*.
10. Serebryany, K. et al. (2012). AddressSanitizer: A Fast Address Sanity Checker. *USENIX ATC 2012*.
11. ForgeCode Team (2026). ForgeCode: A Hand-Engineered Multi-Agent Harness for TerminalBench-2. *TerminalBench-2 Leaderboard Submission*.
12. Anthropic (2026). Claude Opus 4.6 Technical Report.
13. Moonshot AI (2026). Kimi K2.5 Technical Report.
14. TerminalBench-2 Organizers (2025). TerminalBench-2: A Benchmark for LLM-Based Vulnerability Discovery. *arXiv:2511.xxxxx*.
15. Yang, J. et al. (2024). SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. *arXiv:2405.15793*.
16. Wei, J. et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022*.
17. Yao, S. et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR 2023*.
18. Zhang, Y. et al. (2024). VulRepair: A T5-Based Automated Software Vulnerability Repair. *FSE 2024*.
