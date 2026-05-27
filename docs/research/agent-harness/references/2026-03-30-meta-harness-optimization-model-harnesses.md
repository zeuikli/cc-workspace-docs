---
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
authors: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
published: 2026-03-30
source: "https://arxiv.org/html/2603.28052v1"
---

# Meta-Harness: End-to-End Optimization of Model Harnesses

**Authors**: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn  
**Affiliation**: Stanford University, KRAFTON, MIT  
**Published**: March 30, 2026  
**arXiv**: 2603.28052v1  
**Source**: https://arxiv.org/html/2603.28052v1  
**Project page**: https://yoonholee.com/meta-harness/  
**Artifact**: https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact

---

## Abstract

The performance of large language model (LLM) systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model. Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively—they are memoryless, condition only on scalar scores, or restrict feedback to short templates or summaries.

We introduce **Meta-Harness**, an outer-loop system that searches over harness code for LLM applications. It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem.

Key results:
- **Online text classification**: +7.7 points over state-of-the-art ACE, using 4× fewer context tokens (48.6% vs. ACE 40.9%, using 11.4K vs. 50.8K tokens)
- **Retrieval-augmented math reasoning**: +4.7 points average on 200 IMO-level problems across five held-out models
- **Agentic coding (TerminalBench-2)**: #2 overall (76.4%) with Opus 4.6; #1 among all Haiku 4.5 agents (37.6%)

---

## 1. Introduction

Changing the harness around a fixed large language model can produce a 6× performance gap on the same benchmark [46]. The harness—the code that determines what to store, retrieve, and show to the model—often matters as much as the model itself. This sensitivity has led to growing interest in **harness engineering**: the practice of refining the code around an LLM to improve the overall system's performance. But despite its importance, harness engineering remains largely manual.

### The Feedback Compression Problem

A natural starting point is recent work on text optimization. However, these methods are poorly matched to harness engineering because they typically operate with short-horizon or heavily compressed feedback:

| Method | History | Log content | MTok/iter |
|--------|---------|-------------|-----------|
| OPRO [50] | Window | past (solution, score) pairs | 0.002 |
| TextGrad [52] | Last | textual feedback on current artifact | 0.015 |
| AlphaEvolve [34] | Window | program database + eval. scores | 0.022 |
| GEPA [1] | Summary | reflective feedback from rollout traces | 0.008 |
| Feedback Descent [25] | Summary | comparison + textual feedback | 0.012 |
| TTT-Discover [54] | Window | prev. solution fragment | 0.026 |
| **Meta-Harness** | **Full** | **all logs and scores** | **10.0** |

Harnesses act over long horizons: a single choice about what to store, when to retrieve it, or how to present it can affect behavior many reasoning steps later. Compressed feedback often removes the information needed to trace downstream failures to earlier harness decisions.

### Core Insight

Meta-Harness addresses this limitation by exposing **full history through a filesystem**, enabling selective diagnosis of raw prior code and execution traces rather than optimization from compressed per-candidate summaries. A single evaluation can produce up to **10,000,000 tokens** of diagnostic information—roughly three orders of magnitude beyond the largest feedback budgets in prior text optimization.

---

## 2. Related Work

### External Memory and Adaptive Access

Several prior works note the benefits of treating large knowledge sources or long inputs as external resources that a language model accesses adaptively: retrieval-augmented generation [27], interleaved retrieval and reasoning [47], memory-based agents [36], or recursive language models [55]. Meta-Harness uses a similar access pattern, but in the demanding setting of harness engineering, where the proposer selectively inspects a large external history of code, scores, and execution traces to improve context-management procedures themselves.

### Executable Code Search

Recent methods search over executable code for functions, workflows, or agent designs. Early work proposes using large models as mutation and crossover operators in evolutionary program search [26]. Later methods evolve designated functions within fixed program scaffolds [38], use meta-agents to program new agents from prior discoveries [19], or search over workflow graphs for agentic systems [57]. Another line searches over memory designs for continual-learning agents [56; 49]. Meta-Harness differs by giving the proposer unrestricted filesystem access to prior experience—rather than relying on a fixed scaffold, archive, or persistent memory mechanism—enabling search over full harness implementations rather than a predefined space of context-management procedures.

### Text Optimization Methods

Meta-Harness is closely related to ProTeGi, TextGrad, OPRO, GEPA, AlphaEvolve/OpenEvolve, and Feedback Descent, which iteratively improve prompts or other text artifacts using feedback from prior attempts. These methods are less well suited to harness engineering, where optimization targets a complete executable procedure, and the relevant environmental feedback is distributed across code, scores, and execution traces in a way that is hard to summarize up front.

---

## 3. Meta-Harness: A Harness for Optimizing Harnesses

### Objective

A **harness** is a stateful program that wraps a language model and determines what context the model sees at each step. Formally, let M denote a fixed language model and X a task distribution. For a harness H and task instance x ~ X, a rollout trajectory τ ~ p_M(H, x) is executed. The objective is:

> H* = argmax_H E_&#123;x ~ X, τ ~ p_M(H,x)&#125; r(τ, x)

When multiple objectives are relevant (e.g., accuracy and context cost), candidates are evaluated under Pareto dominance.

### Meta-Harness Search Loop

Meta-Harness uses a single coding-agent proposer with access to a growing filesystem D. At each iteration, the proposer:

1. **Inspects** prior code, scores, and execution traces via filesystem operations (grep, cat)
2. **Reasons** about likely failure modes before generating a new harness
3. **Proposes** k new harnesses
4. **Evaluates** each proposed harness on evaluation tasks
5. **Logs** all results (proposed code, reasoning traces, evaluation scores) in a new directory

The filesystem is typically far larger than the proposer's context window. In practice, the proposer reads a **median of 82 files per iteration** (range 69–99), referencing over 20 prior candidates per step (Appendix A). This access pattern is non-Markovian: the proposer routinely inspects the majority of available history rather than conditioning only on the most recent parent.

Meta-Harness maintains a population and a Pareto frontier over evaluated harnesses, but imposes no parent-selection rule. A typical run evaluates roughly **60 harnesses over 20 iterations**.

### Advantages of Code-Space Search

Harness optimization occurs in code space, where small changes to retrieval, memory, or prompt-construction logic can affect behavior many steps later, making local search heuristics poorly matched to the problem. By inspecting execution traces, the proposer can often infer *why* a harness failed and which earlier design choices likely contributed—not just *that* it failed. The proposer can therefore modify the harness at the level of algorithmic structure, ranging from changes to retrieval, memory, or prompt-construction logic to full program rewrites.

### Practical Implementation

- **Proposer (P)**: Claude Code [4] with Opus-4.6
- **Base model (M)**: Varies by domain (always frozen during search)
- Each harness is a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic
- The proposer is guided by a minimal domain-specific skill describing where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify

---

## 4. Experiments and Results

### 4.1 Online Text Classification

**Setup**: An LLM receives labeled examples one at a time, updates its memory, and is evaluated on a held-out test set. Base model: GPT-OSS-120B. Three datasets:
- **LawBench (Law)**: Predicts criminal charges from case descriptions (215 classes)
- **Symptom2Disease (S2D)**: Predicts diseases from symptom descriptions (22 classes)
- **USPTO-50k**: Predicts precursor reactants from product molecules (180 classes)

Search population initialized from: zero-shot, few-shot, ACE, and MCE. 20 evolution iterations with two candidates per iteration = 40 candidate harnesses.

**Table 2: Test-set metrics for all harnesses**  
*(Ctx = additional input tokens in context, thousands; ↓ lower is better)*

| Harness | USPTO | S2D | Law | Avg Acc | Ctx (K) ↓ |
|---------|-------|-----|-----|---------|-----------|
| Zero-Shot | 12.0 | 63.2 | 7.0 | 27.4 | 0 |
| Few-Shot (8) | 14.0 | 67.9 | 21.0 | 34.3 | 2.0 |
| Few-Shot (32) | 13.0 | 72.2 | 21.0 | 35.4 | 7.9 |
| Few-Shot (all) | 15.0 | 78.3 | 29.0 | 40.8 | 12.3 |
| MCE [51]† | 14.0 | 83.0 | 23.0 | 40.0 | 28.5 |
| ACE [58]† | 16.0 | 77.8 | 29.0 | 40.9 | 50.8 |
| **Meta-Harness** | **14.0** | **86.8** | **45.0** | **48.6** | **11.4** |

†: implementation from Ye et al. [51].

**Meta-Harness improves accuracy by 7.7 pp over ACE and 8.6 pp over MCE, while using 4× fewer context tokens than ACE.**

### Ablation: What Information Matters?

**Table 3: Ablation of the information available to the proposer**

| Method | Scores | Code | Summaries | Traces | Median ↑ | Best Acc ↑ | > ZS |
|--------|--------|------|-----------|--------|----------|------------|------|
| Scores Only | ✓ | ✓ | ✗ | ✗ | 34.6 | 41.3 | 26 |
| Scores + Summary | ✓ | ✓ | ✓ | ✗ | 34.9 | 38.7 | 23 |
| **Meta-Harness (full)** | ✓ | ✓ | — | ✓ | **50.0** | **56.7** | **39** |

*(> ZS: number of runs whose accuracy exceeded the zero-shot baseline)*

**Full access to execution traces is the most important component.** Scores-only reaches 34.6 median and 41.3 best accuracy. Scores-plus-summary reaches 34.9 median and 38.7 best. Meta-Harness reaches 50.0 median and 56.7 best—its median candidate outperforms the best candidate found under either ablation. Summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details.

### Comparison vs. Text Optimizers

**Table 4: Text classification accuracies of harnesses proposed by different text optimizers (search set)**

| Method | Median | Best |
|--------|--------|------|
| GEPA [1] | 32.6 | 40.2 |
| Best-of-N | 34.0 | 44.2 |
| OpenEvolve [42] | 39.1 | 43.3 |
| TTT-Discover [53] | 34.1 | 45.6 |
| **Meta-Harness** | **50.0** | **56.7** |

Meta-Harness matches the best prior text optimizers (OpenEvolve, TTT-Discover) in 0.1× the evaluations, and its final accuracy surpasses theirs by more than 10 points.

### Out-of-Distribution (OOD) Text Classification

**Table 5: OOD text classification dataset evaluation** *(9 previously unseen datasets)*

| Harness | SciC | FiNER | Amz5 | FPB | GoEmo | Bank77 | News | SciT | TwHate | Avg Acc | Ctx ↓ |
|---------|------|-------|------|-----|-------|--------|------|------|--------|---------|-------|
| Zero-shot | 32.7 | 56.0 | 52.7 | 90.0 | 42.0 | 80.7 | 84.7 | 89.3 | 75.3 | 67.0 | — |
| Few-shot (8) | 34.0 | 63.0 | 54.0 | 90.0 | 44.0 | 82.7 | 84.7 | 91.3 | 76.7 | 68.9 | 2.2 |
| Few-shot (32) | 38.7 | 62.0 | 53.3 | 90.7 | 43.3 | 86.0 | 85.3 | 90.7 | 76.7 | 69.6 | 5.2 |
| Few-shot (all) | 35.3 | 61.0 | 50.0 | 93.3 | 42.7 | 80.7 | 84.0 | 90.0 | 76.7 | 68.2 | 7.4 |
| ACE [58] | 40.7 | 74.0 | 48.0 | 96.7 | 44.0 | 83.3 | 86.0 | 90.7 | 68.7 | 70.2 | 11.7 |
| **Meta-Harness** | **53.3** | **67.0** | **60.0** | **94.0** | **46.0** | **82.7** | **86.7** | **91.3** | **77.3** | **73.1** | **7.3** |

Meta-Harness achieves the best average accuracy (73.1%), outperforming ACE (70.2%) by 2.9 points on 9 previously unseen tasks. Highest performance on 6/9 datasets, suggesting the discovered harness captures generally effective strategies rather than overfitting to search datasets. Notable: naively adding more few-shot examples beyond 32 hurts performance in 7/9 tasks.

---

### 4.2 Retrieval-Augmented Math Reasoning

**Setup**: Augmenting the model with the ability to retrieve examples from a large corpus for olympiad math solving. The retrieval corpus contains ≥500,000 solved problems from eight open-source datasets (carefully deduplicated and decontaminated). Search: 40 iterations over a 250-problem search set (OlympiadBench + Omni-MATH hard) = 109 candidate retrieval harnesses. Evaluation: 200 previously unseen IMO-level problems from IMO-AnswerBench, IMO-ProofBench, and ArXivMath. Selection model: GPT-OSS-20B. Evaluation: same harness tested on 5 held-out models.

**Table 6: Retrieval-augmented math problem solving on 200 IMO-level math problems**  
*(pass@1 averaged over 3 samples per problem; absolute improvement over no-retrieval baseline in parentheses)*

| Method | GPT-5.4n | GPT-5.4m | Gem-3.1FL | Gem-3F | GPT-20B | **Avg.** |
|--------|----------|----------|-----------|--------|---------|---------|
| No Retriever | 23.0 | 28.8 | 28.6 | 42.6 | 47.6 | 34.1 |
| Dense Retrieval (k=1) | 27.1 (+4.1) | 24.5 (−4.3) | 31.3 (+2.7) | 42.3 (−0.3) | 46.9 (−0.7) | 34.4 (+0.3) |
| Dense Retrieval (k=5) | 31.1 (+8.1) | 28.3 (−0.5) | 37.1 (+8.5) | 47.2 (+4.6) | 46.7 (−0.9) | 38.1 (+4.0) |
| Random Few-shot | 23.1 (+0.1) | 24.5 (−4.3) | 31.0 (+2.4) | 40.4 (−2.2) | 41.8 (−5.8) | 32.2 (−1.9) |
| BM25 Retrieval | 30.2 (+7.2) | 29.2 (+0.4) | 32.8 (+4.2) | 46.6 (+4.0) | 48.9 (+1.3) | 37.5 (+3.4) |
| **Meta-Harness** | **31.7 (+8.7)** | **30.4 (+1.6)** | **34.9 (+6.3)** | **46.3 (+3.7)** | **50.6 (+3.0)** | **38.8 (+4.7)** |

**A single discovered retrieval harness transfers across 5 held-out models, improving accuracy by 4.7 points on average over no retrieval.** It also matches or exceeds the strongest fixed baselines on average, outperforming BM25 retrieval by 1.3 points overall, while avoiding regressions observed with dense retrieval and random few-shot prompting across several models. Meta-Harness operates entirely in code space on top of the same BM25-based lexical retrieval stack as the sparse baseline, rather than introducing an additional dense encoder.

---

### 4.3 Agentic Coding on TerminalBench-2

**Setup**: TerminalBench-2 [32] evaluates LLM agents on 89 challenging tasks requiring long-horizon, fully autonomous execution under complex dependencies and substantial domain knowledge. Search initialized from two strong open baselines: Terminus 2 [32] and Terminus-KIRA [24]. For this experiment, search and final evaluation are performed on the same 89-task benchmark (standard practice: the benchmark is small and expensive enough that introducing a separate split would materially weaken the search signal).

**Table 7: Pass rate on TerminalBench-2**

| Harness | Auto | Pass (%) |
|---------|------|----------|
| **Claude Opus 4.6** | | |
| Claude Code | ✗ | 58.0 |
| Terminus 2 | ✗ | 62.9 |
| Mux | ✗ | 66.5 |
| Droid | ✗ | 69.9 |
| TongAgents | ✗ | 71.9 |
| MAYA-V2 | ✗ | 72.1 |
| Terminus-KIRA | ✗ | 74.7 |
| Capy | ✗ | 75.3 |
| **Meta-Harness** | **✓** | **76.4** |
| ForgeCode | ✗ | 81.8 |
| **Claude Haiku 4.5** | | |
| OpenHands | ✗ | 13.9 |
| Claude Code | ✗ | 27.5 |
| Terminus 2 | ✗ | 28.3 |
| Mini-SWE-Agent | ✗ | 29.8 |
| Terminus-KIRA | ✗ | 33.7 |
| Goose | ✗ | 35.5 |
| **Meta-Harness** | **✓** | **37.6** |

*(Results for others are from the official leaderboard. Auto = automatically discovered harness.)*

**Results**:
- **Opus 4.6**: 76.4% pass rate, surpassing hand-engineered Terminus-KIRA (74.7%), ranking **#2 among all Opus 4.6 agents**. The only higher-scoring Opus 4.6 agent is ForgeCode (81.8%), whose reported result could not be reproduced from publicly available code alone.
- **Haiku 4.5**: 37.6%, outperforming next-best Goose (35.5%) by 2.1 points, ranking **#1 among all Haiku 4.5 agents**.

### Qualitative Proposer Behavior (TerminalBench-2 Search Trajectory)

The proposer read a median of 82 files per iteration (range 69–99), roughly split between prior harness source code (41%) and execution traces (40%), with the remainder going to score summaries (6%) and other files (13%). This access pattern is non-Markovian: the proposer routinely inspects the majority of available history.

**Narrative arc** (10 iterations, Claude Opus 4.6):

- **Iterations 1–2**: Both candidates bundle plausible structural fixes with prompt-template modifications and both regress sharply from the 64.4% Terminus-KIRA baseline. Iteration 1 targets leaked terminal markers; iteration 2 targets double-confirmation completion spirals.
- **Iteration 3 (key causal step)**: The proposer explicitly identifies the confound — "The structural bugfixes were confounded with harmful prompt changes. evo_strip_only isolates the two proven structural fixes." This is the key causal step. The proposer notices the common factor across the first two failures is not the particular bugfix, but the cleanup-heavy prompt rewrite.
- **Iterations 4–6**: Continue probing the same part of the design space with more explicit theories about completion logic fragility. They all still regress.
- **Iteration 7 (winning candidate)**: After six consecutive regressions, the proposer shifts strategy from modifying the control loop to adding information before the loop begins: "evo_env_bootstrap takes a different approach — purely additive. It gathers an environment snapshot via a single shell command before the first LLM call." The proposer articulates *why* it should be safer: it avoids touching the previously fragile completion machinery.
- **Iteration 8**: Composes the additive improvement with an earlier structural fix for orthogonal gains.
- **Iteration 10**: References results from a separate earlier search run — cross-run transfer.

---

## 5. Discussion

Beyond outperforming existing harnesses, Meta-Harness has several practical advantages:

1. **Generalization**: Discovered harnesses generalize to out-of-distribution classification datasets (Table 5) and to unseen base models in the math setting (Table 6).
2. **Wall-clock efficiency**: A search run completes in a few hours of wall-clock time, yet produces readable, transferable strategies that can be reused across models, including future, stronger ones.
3. **Inspectability**: Overfitting in code space is more inspectable — brittle if-chains or hard-coded class mappings are visible on inspection in a way that weight-space overfitting is not.

The main advantage of Meta-Harness is not just search over code, but **search with selective access to prior diagnostic experience**. The proposer is not limited to scalar rewards or fixed summaries; it can inspect raw code, execution traces, and prior failures, then form and test hypotheses about what to change.

More broadly, once a search space becomes accessible, stronger general-purpose agents can outperform hand-engineered solutions (the Bitter Lesson pattern [44]). A natural next step is to co-evolve the harness and the model weights, letting the strategy shape what the model learns and vice versa.

---

## References

**[1]** Agrawal, L. A., Tan, S., Soylu, D., Ziems, N., Khare, R., et al. (2025). GEPA: reflective prompt evolution can outperform reinforcement learning. *arXiv:2507.19457*.

**[2]** Andrychowicz, M., Denil, M., Gomez, S., et al. (2016). Learning to learn by gradient descent by gradient descent. *NeurIPS 29*.

**[3]** Anthropic and community contributors. AgentSkills. GitHub repository. https://github.com/agentskills/agentskills. Accessed: 2026-03-27.

**[4]** Anthropic (2025). Claude code: an agentic coding tool. https://www.anthropic.com/claude-code.

**[5]** Balunović, M., Dekoninck, J., Petrov, I., Jovanović, N., and Vechev, M. (2025). MathArena: evaluating LLMs on uncontaminated math competitions. SRI Lab, ETH Zurich.

**[6]** Barbieri, F., Camacho-Collados, J., Neves, L., and Espinosa-Anke, L. (2020). TweetEval: unified benchmark and comparative evaluation for tweet classification. *arXiv:2010.12421*.

**[7]** Beurer-Kellner, L., Fischer, M., and Vechev, M. (2023). Prompting is programming: a query language for large language models. *PLDI*, pp. 1946–1969.

**[8]** Böckeler, B. (2026). Harness engineering. martinfowler.com.

**[9]** Bölük, C. (2026). I improved 15 LLMs at coding in one afternoon. only the harness changed. blog.can.ac.

**[10]** Casanueva, I., Temčinas, T., Gerz, D., Henderson, M., and Vulić, I. (2020). Efficient intent detection with dual sentence encoders. *arXiv:2003.04807*.

**[11]** Cemri, M., Agrawal, S., Gupta, A., et al. (2026). AdaEvolve: adaptive LLM driven zeroth-order optimization. *arXiv:2602.20133*.

**[12]** LangChain. Software, released 2022-10-17.

**[13]** Cohan, A., Ammar, W., van Zuylen, M., and Cady, F. (2019). Structural scaffolds for citation intent classification in scientific publications. *arXiv:1904.01608*.

**[14]** Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., and Ravi, S. (2020). GoEmotions: a dataset of fine-grained emotions. *arXiv:2005.00547*.

**[15]** Fei, Z., Shen, X., Zhu, D., Zhou, F., Han, Z., et al. (2024). Lawbench: benchmarking legal knowledge of large language models. *EMNLP 2024*, pp. 7933–7962.

**[16]** Finn, C., Abbeel, P., and Levine, S. (2017). Model-agnostic meta-learning for fast adaptation of deep networks. *ICML 2017*.

**[17]** ForgeCode (2025). Benchmarks don't matter.

**[18]** Gretel AI (2023). Symptom to diagnosis dataset. https://huggingface.co/datasets/gretelai/symptom_to_diagnosis. Accessed: 2026-01-22.

**[19]** Hu, S., Lu, C., and Clune, J. (2025). Automated design of agentic systems. *ICLR 2025*.

**[20]** Justin Young, A. (2025). Effective harnesses for long-running agents. Anthropic Engineering Blog.

**[21]** Keung, P., Lu, Y., Szarvas, G., and Smith, N. A. (2020). The multilingual amazon reviews corpus. *arXiv:2010.02573*.

**[22]** Khattab, O., Singhvi, A., Maheshwari, P., Zhang, Z., et al. (2023). DSPy: compiling declarative language model calls into self-improving pipelines. *arXiv:2310.03714*.

**[23]** Khot, T., Sabharwal, A., and Clark, P. (2018). SciTaiL: a textual entailment dataset from science question answering. *AAAI 2018*.

**[24]** KRAFTON AI and Ludo Robotics (2026). Terminus-KIRA: boosting frontier model performance on terminal-bench with minimal harness.

**[25]** Lee, Y., Boen, J., and Finn, C. (2025). Feedback descent: open-ended text optimization via pairwise comparison. *arXiv:2511.07919*.

**[26]** Lehman, J., Gordon, J., Jain, S., et al. (2022). Evolution through large models. *arXiv:2206.08896*.

**[27]** Lewis, P., Perez, E., Piktus, A., Petroni, F., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS 33*, pp. 9459–9474.

**[28]** Loukas, L., Fergadiotis, M., Chalkidis, I., et al. (2022). FiNER: financial numeric entity recognition for XBRL tagging. *ACL 2022*, pp. 4419–4431.

**[29]** Luong, T., Hwang, D., Nguyen, H. H., et al. (2025). Towards robust mathematical reasoning. *EMNLP 2025*.

**[30]** Madaan, A., Tandon, N., Gupta, P., et al. (2023). Self-refine: iterative refinement with self-feedback. *NeurIPS 36*, pp. 46534–46594.

**[31]** Malo, P., Sinha, A., Takala, P., Korhonen, P., and Wallenius, J. (2013). Good debt or bad debt: detecting semantic orientations in economic texts. *arXiv:1307.5336*.

**[32]** Merrill, M. A., Shaw, A. G., Carlini, N., Li, B., et al. (2026). Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces. *arXiv:2601.11868*.

**[33]** Nichols, J. (2025). How we scored #1 on terminal-bench (52%).

**[34]** Novikov, A., Vũ, N., Eisenberger, M., Dupont, E., et al. (2025). AlphaEvolve: a coding agent for scientific and algorithmic discovery. *arXiv:2506.13131*.

**[35]** OpenAI (2026). Harness engineering: leveraging Codex in an agent-first world. OpenAI Blog.

**[36]** Packer, C., Fang, V., Patil, S., Lin, K., Wooders, S., and Gonzalez, J. (2023). MemGPT: towards LLMs as operating systems.

**[37]** Pryzant, R., Iter, D., Li, J., Lee, Y. T., Zhu, C., and Zeng, M. (2023). Automatic prompt optimization with "gradient descent" and beam search. *arXiv:2305.03495*.

**[38]** Romera-Paredes, B., Barekatain, M., Novikov, A., et al. (2024). Mathematical discoveries from program search with large language models. *Nature* 625(7995), pp. 468–475.

**[39]** Schmidhuber, J. (1993). A neural network that embeds its own meta-levels. *IEEE ICNN*.

**[40]** Schneider, N., Stiefl, N., and Landrum, G. A. (2016). What's what: the (nearly) definitive guide to reaction role assignment. *J. Chem. Inf. Model.* 56(12), pp. 2336–2346.

**[41]** Shakya, S., Hartl, A., Hochreiter, S., and Pöppel, K. (2026). Adaptive retrieval helps reasoning in LLMs – but mostly if it's not used. *arXiv:2602.07213*.

**[42]** Sharma, A. (2025). OpenEvolve: an open-source evolutionary coding agent. GitHub repository.

**[43]** Snell, J., Swersky, K., and Zemel, R. S. (2017). Prototypical networks for few-shot learning. *NeurIPS 2017*.

**[44]** Sutton, R. (2019). The bitter lesson.

**[45]** Thrun, S. and Pratt, L. (1998). Learning to learn: introduction and overview. In *Learning to learn*, pp. 3–17.

**[46]** Tian, M., Wang, Z., Yang, B., Tang, Z., et al. (2026). SWE-bench mobile: can large language model agents develop industry-level mobile applications? *arXiv preprint*.

**[47]** Trivedi, H., Balasubramanian, N., Khot, T., and Sabharwal, A. (2023). Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions. *arXiv:2212.10509*.

**[48]** Xiao, C., Hudson, G. T., and Moubayed, N. A. (2024). RAR-b: reasoning as retrieval benchmark. *arXiv:2404.06347*.

**[49]** Xiong, Y., Hu, S., and Clune, J. (2026). Learning to continually learn via meta-learning agentic memory designs. *OpenReview*.

**[50]** Yang, C., Wang, X., Lu, Y., Liu, H., Le, Q. V., Zhou, D., and Chen, X. (2023). Large language models as optimizers. *ICLR 2024*.

**[51]** Ye, H., He, X., Arak, V., Dong, H., and Song, G. (2026). Meta context engineering via agentic skill evolution. *arXiv:2601.21557*.

**[52]** Yuksekgonul, M., Bianchi, F., Boen, J., Liu, S., et al. (2024). TextGrad: automatic "differentiation" via text. *arXiv:2406.07496*.

**[53]** Yuksekgonul, M., Koceja, D., Li, X., Bianchi, F., et al. (2026). Learning to discover at test time. *arXiv:2601.16175*.

**[54]** Yuksekgonul, M., Koceja, D., Li, X., Bianchi, F., McCaleb, J., Wang, X., Kautz, J., Choi, Y., Zou, J., Guestrin, C., and Sun, Y. (2026). Learning to discover at test time. *arXiv:2601.16175*.

**[55]** Zhang, A. L., Kraska, T., and Khattab, O. (2026). Recursive language models. *arXiv:2512.24601*.

**[56]** Zhang, G., Ren, H., Zhan, C., Zhou, Z., et al. (2025). Memevolve: meta-evolution of agent memory systems. *arXiv:2512.18746*.

**[57]** Zhang, J., Xiang, J., Yu, Z., Teng, F., et al. (2025). AFlow: automating agentic workflow generation. *arXiv:2410.10762*.

**[58]** Zhang, Q., Hu, C., Upasani, S., Ma, B., Hong, F., et al. (2025). Agentic context engineering: evolving contexts for self-improving language models. *arXiv:2510.04618*.

**[59]** Zhang, X., Zhao, J., and LeCun, Y. (2016). Character-level convolutional networks for text classification. *arXiv:1509.01626*.

---

**Citation**: Lee, Y., Nair, R., Zhang, Q., Lee, K., Khattab, O., & Finn, C. (2026). Meta-harness: End-to-end optimization of model harnesses. *arXiv preprint arXiv:2603.28052*.
