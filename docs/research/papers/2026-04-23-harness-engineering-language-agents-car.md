---
title: "Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime"
authors: "Chaoyue He, Xin Zhou, Di Wang, Hong Xu, Wei Liu, Chunyan Miao"
published: 2026-04-23
source: "https://www.preprints.org/manuscript/202603.1756.v2"
---

# Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime

**Authors**: Chaoyue He, Xin Zhou, Di Wang, Hong Xu, Wei Liu, Chunyan Miao  
**Published**: April 23, 2026  
**Source**: https://www.preprints.org/manuscript/202603.1756.v2  
**DOI**: 10.20944/preprints202603.1756.v2

## Abstract

Language agents that operate via tools, files, browsers, APIs, and sustained sessions depend on more than base model quality or prompting alone. Their dependability stems from a "harness layer"—the infrastructure determining which instructions hold authority, available actions, state persistence, and failure management across time. This paper argues this infrastructure warrants explicit academic treatment. The authors present a working decomposition framing the harness layer as **control, agency, and runtime (CAR)**; position harness engineering within the progression from software engineering through prompt and context engineering; and examine **63** relevant works, revealing a notable gap between academic literature and public engineering documentation. The paper contends that numerous documented agent improvements may be **harness-dependent** rather than purely model-driven, and proposes **HarnessCard** as a straightforward disclosure mechanism. Drawing on papers, benchmarks, protocols, and engineering materials current through **April 21, 2026**, the authors advocate that agent progress reporting should encompass the harness layer converting capability into regulated action.

## Keywords

Language agents; harness engineering; agent harness; control agency runtime (CAR); agent evaluation; prompt engineering; context engineering; HarnessCard; scaffolding; LLM agents; tool use

## 1. Introduction

### 1.1 The Infrastructure Problem

Language agents have become central to autonomous software engineering, information retrieval, and decision support. Yet despite rapid progress in model capabilities, agent reliability remains uneven. Current approaches treat the harness layer—the infrastructure governing agent execution—as implementation detail rather than an explicit research object.

The core claim: **agent performance improvements often stem from harness changes rather than model capability alone**. Systems like SWE-agent demonstrate that interface redesign substantially affects performance. Yet this infrastructure remains underspecified in academic literature compared to engineering practice.

### 1.2 Visibility Asymmetry

Academic papers emphasize model quality and prompt engineering. Engineering documentation from frontier organizations (Anthropic, OpenAI) foregrounds runtime governance, memory management, and control mechanisms. This asymmetry obscures reproducibility and cumulative progress.

### 1.3 Research Scope

This paper:
- Proposes the CAR decomposition as a working framework for analyzing harness structure
- Conducts a descriptive audit of 63 relevant works published through April 2026
- Identifies patterns in control, agency, and runtime design
- Proposes HarnessCard as a transparency mechanism
- Advocates for explicit harness-layer research

## 2. The CAR Framework: Control, Agency, Runtime

### 2.1 Control Layer (C)

**Definition**: Durable artifacts encoding behavioral constraints before execution.

**Exemplars**:
- Repository maps and navigation structures
- AGENTS.md files specifying agent roles and capabilities
- Architectural rules and permission policies
- Tool descriptions and interface schemas
- Test suites and validation procedures
- Linting rules and static checks

**Key property**: Control is linguistic and persistent. It shapes what agents can do by explicitly restricting the space of permissible actions.

**Examples in practice**:
- Anthropic's documented agent guidelines constrain tool access per role
- OpenAI's system prompts embed behavioral policies
- SWE-agent's repository interface controls which files agents access

### 2.2 Agency Layer (A)

**Definition**: The action substrates and interfaces through which agents interact with systems.

**Exemplars**:
- Code execution environments (sandboxed, unsandboxed)
- Browser automation interfaces
- Tool APIs and their schemas
- Orchestrator-worker communication patterns
- Reviewer roles and approval workflows
- Concrete interface definitions (e.g., action schemas in ReAct)

**Key property**: Agency defines the "shape" of possible actions. An agent with access to a Python REPL has different agency than one with access only to web search.

**Examples in practice**:
- SWE-agent's command-line interface differs from CoOp's browser interface
- Retrieval-augmented generation (RAG) agents have different agency than repository-browsing agents
- Approval workflows reduce agency but increase oversight

### 2.3 Runtime Layer (R)

**Definition**: Time-based governance structures that maintain system coherence over extended execution.

**Exemplars**:
- Context assembly and optimization
- Memory management (working, episodic, semantic)
- State persistence and checkpointing
- Retry strategies and backtracking
- Approval workflows and budget enforcement
- Trace collection and observability

**Key property**: Runtime is the execution layer. It determines how agents navigate long-horizon tasks while managing finite resources (context, compute, time).

**Examples in practice**:
- Context compaction strategies determine when agents lose information
- Memory systems affect what agents "remember" across sessions
- Retry budgets affect failure recovery
- Checkpointing enables recovery from transient failures

## 3. Harness Sensitivity: Why Attribution Matters

### 3.1 Core Claim

Many reported agent performance gains derive from harness improvements rather than model capability increases alone.

**Evidence**:
- SWE-agent's command-line interface redesign improved performance by ~40% without model changes
- OS-Symphony's migration from code-based to natural-language harness representation shifted performance profiles
- Meta-Harness demonstrates that discovered harness optimizations transfer across models

### 3.2 Attribution Challenge

When a paper reports performance improvement, the gain could stem from:
1. Model capability improvement (true capability gain)
2. Harness redesign (infrastructure change)
3. Task-specific tuning (narrow optimization)
4. Interaction effects (multiple factors combined)

**Current practice**: Papers typically report only improvement magnitude, obscuring source.

**Proposed solution**: Disclose harness details explicitly, enabling readers to judge attribution.

### 3.3 Reproducibility Implications

Without harness specification:
- Reproducing results requires reverse-engineering the infrastructure
- Comparing methods becomes difficult (model vs. harness confounded)
- Insights fail to generalize to other settings

With harness specification:
- Reproducibility improves substantially
- Attribution becomes clearer
- Insights can be reused across projects

## 4. Evidence Audit: 63 In-Scope Works

### 4.1 Methodology

The authors conducted a descriptive audit of 75 total sources, designating 63 as in-scope harness-relevant works:

- **38 academic papers or benchmarks** focused on agent evaluation, interface design, or system architecture
- **25 engineering notes, protocol documents, or technical articles** from frontier organizations

**Timeline**: Bias toward recent work (51 of 63 from 2024-2026)

### 4.2 Key Findings

**Academic literature** emphasizes:
- Interface design and evaluation protocols
- Agent performance metrics
- Model capability advancement
- Prompt engineering techniques

**Engineering documentation** foregrounds:
- Runtime control and state management
- Memory architectures
- Safety governance mechanisms
- Context optimization strategies

**Gap interpretation**: Harness engineering remains more visible in practice than in formal venues, suggesting it is underrepresented as a research object.

### 4.3 Representative Works

**Control-layer focus**:
- SWE-agent: Command-line interface design
- Anthropic's agent safety guidelines
- OpenAI's system prompt documentation

**Agency-layer focus**:
- ReAct: Action schema design
- CoOp: Browser automation interface
- General Agent Evaluation: Interface standardization

**Runtime-layer focus**:
- Trajectory-level auditing: Execution tracing
- Context-compaction strategies: Token-efficient long-horizon execution
- Memory systems: Persistent knowledge across sessions

## 5. Design Patterns and Failure Modes

### 5.1 Repository Coding Agents

**Typical CAR configuration**:
- **Control**: File-level access policies, safe-edit enforcements
- **Agency**: Command-line shell, file browser, code editor
- **Runtime**: Checkpoint after each edit, retry with modified strategy

**Failure mode**: Context drift—as session length increases, agents lose awareness of repository structure.

### 5.2 Browser Agents

**Typical CAR configuration**:
- **Control**: Visual feedback rules, screenshot interpretation guidelines
- **Agency**: Viewport navigation, element locator interface
- **Runtime**: Screenshot-based context, visual state tracking

**Failure mode**: Verifier overfitting—agents learn to exploit evaluation signals rather than solve underlying tasks.

### 5.3 Enterprise Support Agents

**Typical CAR configuration**:
- **Control**: Role-based access control, escalation rules
- **Agency**: Ticketing systems, knowledge base search
- **Runtime**: Multi-turn conversation memory, approval workflows

**Failure mode**: Policy violation—agents exceed authorization boundaries during extended conversations.

## 6. HarnessCard: Proposed Disclosure Standard

### 6.1 Motivation

Current practices obscure harness details, making reproducibility and comparison difficult. HarnessCard provides a lightweight disclosure template.

### 6.2 Required Fields

A HarnessCard specifies:

#### Base Model
- Model name and version
- Decoding parameters (temperature, top-p, max tokens)
- Fine-tuning or prompt-engineering applied

#### Control Artifacts
- AGENTS.md or role specification
- Tool descriptions and schemas
- Architectural rules and constraints
- Safety policies and permission models

#### Runtime Policies
- Memory architecture (working, episodic, semantic)
- Context assembly strategy
- Checkpointing and retry policies
- Budget constraints (tokens, compute, wall-clock time)

#### Action Substrate
- Available tools (shell, browser, APIs, etc.)
- Execution environment (sandboxed, etc.)
- Communication protocols
- Error handling and recovery

#### Execution Topology
- Single-agent vs. multi-agent orchestration
- Planner-executor separation
- Reviewer roles and approval workflows

#### Feedback Mechanisms
- How agents observe outcomes
- Error signals and their interpretation
- Success/failure signals

#### Governance Structures
- Human oversight points
- Escalation triggers
- Audit trails and observability

#### Observability and Evaluation
- Metrics tracked
- Failure categories monitored
- Evaluation protocols used

### 6.3 Template Example

```
## HarnessCard

**Model**: Claude 3.5 Sonnet, temperature=0.7, max_tokens=2048

**Control**:
- Tool access: File read/write (restricted to /project/), CLI execution (command whitelist)
- Safety policy: Approval required for destructive operations
- Test suite: Pre-commit linting enforced

**Runtime**:
- Memory: Session history (last 10K tokens) + persistent notes
- Context strategy: Compression at 80% window utilization
- Retry budget: 3 attempts per failed action

**Agency**:
- Shell: /bin/bash with command restrictions
- File system: Project directory only, no system directories
- APIs: Internal service mesh, authentication via token

**Topology**:
- Single agent planning and execution
- No multi-agent orchestration
- Manual approval for large code changes

**Feedback**:
- Success: Task completion signal from external validation
- Failure: Error messages from tool execution
- Observability: Full trace logging

**Governance**:
- Human review: Required for changes affecting production
- Audit: All operations logged to central system
- Escalation: Complex tasks escalated to senior engineers

**Evaluation**:
- Metric: Task success rate on benchmark suite
- Benchmark: SWE-bench Verified (500 tasks)
- Failure categories: Timeout, syntax error, logic error
```

## 7. Research Agenda

### 7.1 Control as Executable Specification

**Direction**: Treat control artifacts as first-class research objects.

**Questions**:
- How do different control formulations (natural language vs. code) affect agent behavior?
- Which control abstractions are most reusable across agent types?
- Can control artifacts be automatically synthesized from task descriptions?

**Exemplar**: Meta-Harness demonstrates that discovered harnesses transfer across models.

### 7.2 Agency as Interface Design

**Direction**: Systematize agency design as a research domain.

**Questions**:
- How do different action substrates (shell vs. browser vs. API) affect success rates?
- What interface abstractions minimize context overhead?
- Can agents learn to use novel interfaces without explicit training?

**Exemplar**: SWE-agent's command-line interface redesign improved performance substantially.

### 7.3 Runtime as Scientific Variable

**Direction**: Measure runtime effects independently from model and control effects.

**Questions**:
- How do different memory architectures affect long-horizon performance?
- What context-compaction strategies are optimal for different task types?
- How do retry policies interact with control and agency?

**Exemplar**: Trajectory-level auditing separates execution effects from capability effects.

### 7.4 Normalization of Harness Reporting

**Direction**: Establish standards for harness disclosure in academic papers.

**Proposal**: Adoption of HarnessCard or equivalent in agent-related publications.

**Expected impact**: Improved reproducibility, clearer attribution, cumulative progress.

### 7.5 Layer-Aware Baselines

**Direction**: Build evaluation baselines that vary harness components systematically.

**Questions**:
- What is the performance impact of varying control policies while holding model and agency fixed?
- What is the impact of different runtime strategies?
- How do these effects interact?

**Method**: Ablation studies controlling for one CAR layer while varying others.

## 8. Limitations and Caveats

### 8.1 Scope and Evidence

- **Evidence bias**: Audit tilts toward English-language, high-resource settings
- **Selective argument**: Not an exhaustive field survey but targeted analysis
- **Vocabulary drift**: Different communities use different terminology (harness, scaffold, infrastructure, etc.)

### 8.2 Conceptual

- **CAR decomposition is analytic**: Proposed framework is useful but not settled ontology
- **Boundary fuzziness**: Some systems blur the lines between control, agency, and runtime
- **Context dependence**: CAR patterns vary by application domain

### 8.3 Attribution

- **Causal identification**: Requires controlled ablations not yet systematically reported
- **Interaction effects**: Model, control, agency, and runtime effects interact in complex ways
- **Generalization**: Findings may not transfer to future domains or model families

## 9. Ethical Considerations

### 9.1 Dual-Use Risks

Improved harnesses enable both beneficial and harmful automation. Governance must be internal to harness design, not an afterthought.

**Examples**:
- A well-designed harness for autonomous code generation can also enable malicious code injection
- Runtime controls that prevent accidental deletions can also restrict legitimate operations
- Memory persistence enables learning from past mistakes but also enables potential unauthorized data accumulation

### 9.2 Autonomy and Transparency

As harnesses improve, agents appear more autonomous while remaining dependent on infrastructure. Disclosure is critical for accountability.

**Concern**: Misrepresenting the autonomy level of systems (overstating agent "reasoning" while understating harness role).

### 9.3 Resource Concentration

Sophisticated harness engineering requires substantial resources. Risk of capability concentration among well-resourced organizations.

## 10. Conclusion

The harness layer—control, agency, and runtime infrastructure—is essential to agent reliability and reproducibility. Academic literature currently underspecifies this layer compared to engineering practice. The proposed CAR framework, evidence audit, and HarnessCard disclosure mechanism provide tools for making harness engineering explicit and comparable.

**Core contributions**:
1. Conceptual framework (CAR) for analyzing harness structure
2. Evidence that harness improvements often drive reported gains
3. Proposed transparency standard (HarnessCard)
4. Research agenda for harness-layer studies
5. Call for normalization of harness reporting in academic papers

**Expected outcomes**:
- Improved reproducibility through harness specification
- Clearer attribution of performance improvements
- Cumulative progress in agent design
- Recognition of harness engineering as a legitimate research domain

## References

Audit references (63 in-scope works) available in appendix. Notable citations include:

- **SWE-agent** (Jimenez et al.): Demonstrates control-layer redesign effects
- **Meta-Harness** (Lee et al.): Automated harness optimization
- **OS-Symphony** (Zeng et al.): Natural-language harness specification
- **Anthropic agent guidelines**: Engineering-practice documentation
- **OpenAI system prompt research**: Control-layer effectiveness
- **General Agent Evaluation** (Zhu et al.): Agency standardization attempts

---

**Keywords**: agent engineering, harness design, control layer, agency design, runtime governance, agent evaluation, reproducibility

**Citation**: He, C., Zhou, X., Wang, D., Xu, H., Liu, W., & Miao, C. (2026). Harness engineering for language agents: The harness layer as control, agency, and runtime. *Preprints*, 202603.1756.v2.

