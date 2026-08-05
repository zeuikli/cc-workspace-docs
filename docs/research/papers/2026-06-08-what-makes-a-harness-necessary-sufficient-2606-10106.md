---
url: "https://arxiv.org/abs/2606.10106"
title: "What makes a harness a harness: necessary and sufficient conditions for an agent harness"
archived_date: 2026-06-14
arxiv_id: 2606.10106
authors: ["de Macedo, Sanderson Oliveira"]
pdf_path: pdfs/2606.10106.pdf
published_date: 2026-06-08
---

# What makes a harness a harness: necessary and sufficient conditions for an agent harness
**Authors**: de Macedo, Sanderson Oliveira **Published**: 2026-06-08 **Source**: https://arxiv.org/abs/2606.10106 **arXiv ID**: 2606.10106 **Categories**: Software Engineering (cs.SE); Artificial Intelligence (cs.AI)
---
## Abstract
The term agent harness now circulates widely in software engineering with generative artificial intelligence. It names the layer that wraps a language model and turns it into a coding agent able to act on a repository. The usage is loose and polysemous. Sometimes the term denotes the whole product (Claude Code, Codex CLI); sometimes it denotes the evaluation scaffold that runs an agent against tasks (the SWE-bench harness); sometimes it gets conflated with an agent framework, an SDK, an IDE plugin, or an orchestrator. What is missing is a reference definition that works as an instrument, one that includes and excludes cases consistently. We build that definition through a conceptual analysis that combines works with persistent identifiers and primary grey-literature sources, such as official documentation, glossaries, and engineering reports. We reconstruct the genealogy of the term, from the horse's tack to the classic test harness, to the machine-learning evaluation harness, and finally to the agent harness. We then propose a constitutive definition that states the necessary and sufficient conditions for a system to be an agent harness, we operationalize it as an inclusion and exclusion test, and we draw the boundary of the concept against an agent framework, an agent SDK, an IDE plugin, an eval harness, and an orchestrator. We apply the definition to six real harnesses (Claude Code, Codex CLI, Aider, Cline, OpenHands, and SWE-agent) and to deliberate edge cases; the test includes and excludes consistently. We close with a research agenda organized by design tension axes. The contribution is an operational definition of agent harness, with a shared vocabulary, able to guide engineering practice and the scientific comparison of agentic systems.

## Necessary & Sufficient Conditions

**Reference definition.** "An agent harness is the runtime engineering layer that wraps one or more language models and turns them into an agent able to accomplish tasks over an external environment, by coupling to the model: (i) an agent loop that interleaves reasoning, action, and observation; (ii) a tool interface that lets the model perceive and alter the environment; (iii) context management that decides what enters and leaves the model's window; and (iv) control mechanisms, that is, limits, verification, and deterministic actions, that make the execution more trustworthy, auditable, and contained."

**The iff claim.** "A system is an agent harness if and only if it instantiates the four elements above at runtime." The temporal clause is load-bearing: "the harness acts during the task, and that is what separates it from the evaluation harness, which acts afterward."

**Each condition is necessary** (proved by removal):
- Without an agent loop → "the system answers once and stops; it is a generator, not an agent."
- Without a tool interface → "the model neither perceives nor alters the environment; it stays trapped in its own window, unable to act on a repository."
- Without context management → "there is no viable loop... letting useful information dilute in the buildup of history, degrades the model." Context management is "constitutive of the loop, not a luxury reserved for long tasks."
- Without control mechanisms → "the system acts, but no one can tell whether it did what it claims, nor is there a way to contain it; it is exactly the failure that motivates the topic, when an agent reports a nonexistent success and nothing verifies it."

**The four together are sufficient.** "Any system that satisfies T1 through T4 already exhibits the behavior that motivated the concept: channeling the model's brute force with control exercised at runtime. Once the four hold, nothing essential is missing, and there is no fifth condition to add." Memory, verification, observability are "specializations of T1 through T4," not new elements.

**What is NOT necessary.** Multi-agent, learning/fine-tuning, a specific model, and a user interface are all incidental — "Pulling these items into the definition would make it too narrow."

**Inclusion / exclusion test (decision procedure).** Ask in order:
- **T1** — Is there a reasoning, action, and observation loop at runtime? (No → single-pass generator or fixed pipeline; not an agent)
- **T2** — Is there a tool interface to perceive and alter the environment? (No → isolated model or SDK that does not yet build the loop)
- **T3** — Is there active management of what enters and leaves the context? (No → naive wrapper that dumps history; brittle on long tasks)
- **T4** — Is there at least one control mechanism (verification, limit, or deterministic action) that does NOT depend on the mere obedience of the model? (No → falls into a neighboring category)

"A system is an agent harness if it answers yes to T1 through T4. Fail any one and the system falls into a neighboring category."

## Key Findings (with numbers if any)

This is a purely definitional / conceptual-analysis paper. **No quantitative metrics, benchmarks, or numeric results are reported** ("not specified in fetched content" beyond the counts below).

- Applied to **6 real harnesses** (Claude Code, Codex CLI, Aider, Cline, OpenHands, SWE-agent) plus deliberate edge cases; the test "includes and excludes consistently."
- Boundary drawn against **5 neighboring concepts** (agent framework, agent SDK, IDE plugin, eval harness, orchestrator).
- Research agenda organized by **4 design-tension axes**: (1) autonomy vs control, (2) broad vs curated context, (3) generalist vs specialized, (4) open permission vs containment.
- Three cross-cutting findings: (a) "Control (T4) is what most distinguishes designs and what the formal literature has least consolidated; it is a particularly open front." (b) "the better the harness, the less the application depends on a single large and expensive model, since model switching becomes a control mechanism, not a rewrite" — flagged explicitly as a conjecture. (c) Current harness evaluation "measures above all the model-harness pair through task benchmarks; an evaluation that isolates the harness's contribution, controlling for the model, is missing" — "a central methodological gap."
- On T4 strength ordering: "Deterministic containment is the strongest control because it does not depend on the model's cooperation, unlike the prompt guardrail, which is the weakest."

## Relevance to The Loop

The Loop's six-phase meta-loop (OBSERVE→IDENTIFY→PROPOSE→APPLY→TEST→RECORD) maps onto this paper's T1 (reason/act/observe loop) and is far more granular. The paper's strongest cross-reference is **T4 / control**:
- T4 requires "at least one control mechanism... that does not depend on the mere obedience of the model" — this is the exact formal articulation of core.md's `unverified_success` gate ("subagent/workflow/compactor 自報成功 = 中間態... 親跑確定性檢查才升 verified") and "確定性代碼做決定 (LLM 只做判斷)".
- The paper's motivating failure — "an agent reports a nonexistent success and nothing verifies it" — is identical to the workspace's agentic-laziness / verdict-non-evidence discipline.
- T3 (context management as constitutive, not a long-task luxury) aligns with context-management.md.
- "Deterministic containment > prompt guardrail" backs core.md's "硬性執行交 hooks，advisory 規則 ~70% 遵從" stance (Lesson 2026-06-07-G).

Caveat: the paper is definitional and yields **no quantified, actionable directive** — its T1-T4 conditions describe properties the workspace harness already instantiates, rather than prescribing a new operable check. Its value is taxonomic/vocabulary, not a new gate.
