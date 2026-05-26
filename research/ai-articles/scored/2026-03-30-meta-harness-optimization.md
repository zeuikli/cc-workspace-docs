---
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
url: https://arxiv.org/html/2603.28052v1
domain: arxiv.org
author: "Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn (Stanford / KRAFTON / MIT)"
published: 2026-03-30
archived: 2026-05-16
tags: [meta-learning, harness-engineering, agent, llm-optimization, terminal-bench, coding-agent]
word_count: 約 11938 字
---

# Meta-Harness: End-to-End Optimization of Model Harnesses

> **來源**：[arxiv.org](https://arxiv.org/html/2603.28052v1)  
> **作者**：Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn  
> **單位**：Stanford / KRAFTON / MIT  
> **發布日期**：2026-03-30 (arXiv:2603.28052v1 [cs.AI])  
> **收錄日期**：2026-05-16  
> **授權**：CC BY 4.0  
> **Project page**：https://yoonholee.com/meta-harness/  
> **Optimized harness**：https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact

---

## Abstract

The performance of large language model (LLM) systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model. Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively: they are memoryless, condition only on scalar scores, or restrict feedback to short templates or summaries.

We introduce Meta-Harness, an outer-loop system that searches over harness code for LLM applications. It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. On online text classification, Meta-Harness improves over a state-of-the-art context management system by 7.7 points while using 4× fewer context tokens. On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models. On agentic coding, discovered harnesses surpass the best hand-engineered baselines on TerminalBench-2. Together, these results show that richer access to prior experience can enable automated harness engineering.

---

## 1 Introduction

Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark. The harness—the code that determines what to store, retrieve, and show to the model—often matters as much as the model itself. This sensitivity has led to growing interest in harness engineering, the practice of refining the code around an LLM to improve the overall system's performance. But despite its importance, harness engineering remains largely manual: practitioners inspect failures, adjust heuristics, and iterate on a small number of designs. In this paper, we ask whether this process itself can be automated.

A natural starting point is recent work on text optimization, since harness engineering also involves iteratively improving text and code artifacts using feedback from prior attempts. However, these methods are poorly matched to harness engineering because they typically operate with short-horizon or heavily compressed feedback: some condition only on the current candidate, others rely primarily on scalar scores, and others restrict feedback to short templates or LLM-generated summaries. This is a pragmatic scalability choice, not evidence that longer-range dependencies are uninformative.

Harnesses act over long horizons: a single choice about what to store, when to retrieve it, or how to present it can affect behavior many reasoning steps later. Compressed feedback often removes the information needed to trace downstream failures to earlier harness decisions. Across the tasks studied by several representative text optimizers, the available context per optimization step ranges from only 100 to 30,000 tokens (Table 1), far below the diagnostic footprint of harness search.

**Comparison of text optimization methods (Table 1)**:

| Method | History | Log content | MTok/iter |
|--------|---------|-------------|-----------|
| OPRO | Window | past (solution, score) pairs | 0.002 |
| TextGrad | Last | textual feedback on current artifact | 0.015 |
| AlphaEvolve | Window | program database + eval. scores | 0.022 |
| GEPA | Summary | reflective feedback from rollout traces | 0.008 |
| Feedback Descent | Summary | comparison + textual feedback | 0.012 |
| TTT-Discover | Window | prev. solution fragment | 0.026 |
| **Meta-Harness** | **Full** | **all logs and scores** | **10.0** |

We address this limitation with Meta-Harness, an agentic harness for optimizing harnesses via end-to-end search. Its proposer is a coding agent, i.e., a language-model-based system that can invoke developer tools and modify code. The choice of coding agent (rather than raw LLM) matters because the amount of experience quickly exceeds context limits, so the proposer must decide what to inspect and validate edits through direct interaction with the codebase. Its key design choice is to expose full history through a filesystem, enabling selective diagnosis of raw prior code and execution traces rather than optimization from compressed per-candidate summaries.

For every previous candidate harness, the filesystem stores the source code, evaluation scores, and execution traces, which the proposer retrieves via standard operations such as grep and cat rather than ingesting them as a single prompt. In practice, the proposer reads a median of 82 files per iteration in our most demanding setting, referencing over 20 prior candidates per step. In the settings we study, a single evaluation can produce up to 10,000,000 tokens of diagnostic information, roughly three orders of magnitude beyond the largest feedback budgets used in prior text optimization settings.

We evaluate Meta-Harness on online text classification, mathematical reasoning, and agentic coding:
- **Online text classification**: harnesses discovered by Meta-Harness improve over ACE by 7.7 points while using 4× fewer context tokens, matching the next-best text optimizer's final performance after 60 proposals with only four.
- **Retrieval-augmented math reasoning**: a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models.
- **TerminalBench-2**: the discovered harness surpasses Terminus-KIRA and ranks #1 among all Haiku 4.5 agents.

---

## 2 Related Work

At a high level, Meta-Harness brings ideas from the broader literature on credit assignment and meta-learning in a new regime enabled by recent advances in coding agents. Rather than updating model weights, the system assigns credit at the harness level: it uses experience from past rollouts to deliberately reason about which steps and components are responsible for failures, then rewrites the external code that governs future behavior.

**External memory and adaptive access.** Several prior works note the benefits of treating large knowledge sources or long inputs as external resources that a language model accesses adaptively, rather than consuming them in a single pass. Retrieval-augmented generation, interleaved retrieval and reasoning, memory-based agents, or recursive language models are mechanisms for adaptive access to external context. Meta-Harness uses a similar access pattern, but in the more demanding setting of harness engineering, where the proposer selectively inspects a large external history of code, scores, and execution traces to improve context-management procedures themselves.

**Executable code search.** Recent methods search over executable code for functions, workflows, or agent designs. Early work proposes using large models as mutation and crossover operators in evolutionary program search. Later methods evolve designated functions within fixed program scaffolds, use meta-agents to program new agents from prior discoveries, or search over workflow graphs for agentic systems. Another line of work searches over memory designs for continual-learning agents. In contrast, Meta-Harness searches over domain-specific harnesses, including prompt construction, retrieval, and state update strategies that reset between tasks.

**Text optimization methods.** Meta-Harness is also closely related to methods such as ProTeGi, TextGrad, OPRO, GEPA, AlphaEvolve/OpenEvolve, and Feedback Descent, which iteratively improve prompts or other text artifacts using feedback from prior attempts. However, these methods are less well suited to harness engineering, where optimization targets a complete executable procedure, and the relevant environmental feedback is distributed across code, scores, and execution traces in a way that is hard to summarize up front.

---

## 3 Meta-Harness: A Harness for Optimizing Harnesses

Meta-Harness is built on the idea that harness optimization benefits from allowing a proposer to selectively inspect prior code and execution traces via filesystem access, rather than optimizing from lossy summaries or an additional hand-designed search structure. At a high level, it repeatedly proposes, evaluates, and logs new harnesses.

### Objective

A harness is a stateful program that wraps a language model and determines what context the model sees at each step. The goal is simple: find the harness that makes the underlying model perform best on the target task distribution.

Formally, let M denote a fixed language model and X a task distribution. For a harness H and task instance x ~ X, we execute a rollout trajectory τ ~ p_M(H,x). The harness constructs prompts for M, the model responds, and the harness updates its state after each interaction. A task-specific reward function r(τ,x) scores the trajectory. The objective of harness optimization is to find the harness that maximizes the expected final reward: H* = argmax_H E[r(τ,x)].

### Meta-Harness Search Loop

Meta-Harness uses a single coding-agent proposer with access to a growing filesystem D that serves as its feedback channel. Here, a coding agent is a language-model-based system that can invoke developer tools and modify code. Unlike prior systems that externalize the improvement logic in a hand-designed search loop, Meta-Harness delegates diagnosis and proposal to the coding agent itself: it decides which prior artifacts to inspect, which failure modes to address, and whether to make a local edit or a more substantial rewrite.

Each evaluated harness contributes a directory containing its source code, scores, and execution traces (such as prompts, tool calls, model outputs, and state updates). The filesystem is typically far larger than the proposer's context window, so the proposer queries it through terminal tools such as grep and cat rather than ingesting it as a single prompt.

**Algorithm 1: Meta-Harness outer loop**
```
Input: tasks X, LLM M, proposer P, iterations N
Initialize: population H  (initial set of valid harnesses)
Initialize: filesystem D ← ∅  (stores code, scores, traces)
for H in H do:
  E_H ← Evaluate(H, M, X)
  D ← D ∪ {(H, E_H)}
for t = 1...N do:
  Proposer P queries filesystem D  (inspects prior harnesses and scores)
  Proposer P proposes k new harnesses {H1,...,Hk}
  for H in {H1,...,Hk} do:
    if H passes interface validation then:
      D ← D ∪ {(H, Evaluate(H, M, X))}
return Pareto frontier of harnesses stored in D
```

Meta-Harness maintains a population H and a Pareto frontier over evaluated harnesses, but imposes no parent-selection rule: the proposer is free to inspect any prior harness and its execution trace when proposing new ones. This simplicity is deliberate: by leaving diagnosis and edit decisions to the proposer rather than hard-coding search heuristics, Meta-Harness can improve automatically as coding agents become more capable.

### Advantages of Code-Space Search

Harness optimization occurs in code space, where small changes to retrieval, memory, or prompt-construction logic can affect behavior many steps later, making local search heuristics poorly matched to the problem. By inspecting execution traces, the proposer can often infer *why* a harness failed and which earlier design choices likely contributed to the failure, not just *that* it failed.

Although the search space is large, representing harnesses as programs provides a natural regularization bias: coding models tend to propose coherent algorithms rather than brittle, hard-coded solutions, which biases the search toward reusable context-management procedures.

### Practical Implementation

In our experiments, each harness is a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic. The proposer P is **Claude Code with Opus-4.6**. The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify. In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations.

---

## 4 Experiments

We evaluate Meta-Harness on three task domains: online text classification, math reasoning, and agentic coding.

### 4.1 Online Text Classification

We follow the online text classification setup where an LLM receives labeled examples one at a time, updates its memory, and is evaluated on a held-out test set. We use GPT-OSS-120B as the LLM text classifier. We use three datasets:
- **LawBench (Law)**: predicts criminal charges from case descriptions (215 classes)
- **Symptom2Disease (S2D)**: predicts diseases from symptom descriptions (22 classes)
- **USPTO-50k**: predicts precursor reactants from product molecules (180 classes)

We initialize the search population from main baseline harnesses: zero-shot, few-shot, ACE, and MCE. We ran 20 evolution iterations with two candidates per iteration, producing 40 candidate harnesses.

**Results (Table 2)**:

| Harness | Avg Acc | Ctx (K tokens) |
|---------|---------|----------------|
| Zero-Shot | 27.4 | — |
| Few-Shot (8) | 34.3 | 2.0 |
| Few-Shot (32) | 35.4 | 7.9 |
| Few-Shot (all) | 40.8 | 12.3 |
| MCE | 40.0 | 28.5 |
| ACE | 40.9 | 50.8 |
| **Meta-Harness** | **48.6** | **11.4** |

Meta-Harness improves over ACE by **7.7 points** while using **4× fewer context tokens**.

**Comparison vs text optimizers (Table 4)**:

| Method | Median | Best |
|--------|--------|------|
| GEPA | 32.6 | 40.2 |
| Best-of-N | 34.0 | 44.2 |
| OpenEvolve | 39.1 | 43.3 |
| TTT-Discover | 34.1 | 45.6 |
| **Meta-Harness** | **50.0** | **56.7** |

Meta-Harness matches the best prior text optimizers (OpenEvolve, TTT-Discover) in 0.1× the evaluations.

**Ablation on proposer interface (Table 3)**:

| Configuration | Median Acc | Best Acc |
|--------------|-----------|---------|
| Scores Only | 34.6 | 41.3 |
| Scores + Summary | 34.9 | 38.7 |
| Meta-Harness (full) | 50.0 | 56.7 |

Access to raw execution traces is the key ingredient. Summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details.

**OOD evaluation**: The selected Meta-Harness achieves the best average accuracy (73.1%) on 9 previously unseen datasets, outperforming ACE (70.2%).

### 4.2 Harnesses for Retrieval-Augmented Reasoning

We study augmenting the model with the ability to retrieve examples from a large corpus for olympiad math solving. The retrieval corpus contains ≥500,000 solved problems from eight open-source datasets. We use Meta-Harness to optimize a harness for 40 iterations over a 250-problem search set of Olympiad-difficulty math problems.

We select a single harness based on search-set performance using GPT-OSS-20B and evaluate it on 200 previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath. We additionally evaluate the same retrieval harness on four held-out models not seen during search.

**Results (Table 6) — pass@1 on 200 IMO-level problems**:

| Method | GPT-5.4n | GPT-5.4m | Gem-3.1FL | Gem-3F | GPT-20B | Avg |
|--------|---------|---------|---------|-------|--------|-----|
| No Retriever | 23.0 | 28.8 | 28.6 | 42.6 | 47.6 | 34.1 |
| Dense (k=1) | 27.1 | 24.5 | 31.3 | 42.3 | 46.9 | 34.4 |
| Dense (k=5) | 31.1 | 28.3 | 37.1 | 47.2 | 46.7 | 38.1 |
| Random Few-shot | 23.1 | 24.5 | 31.0 | 40.4 | 41.8 | 32.2 |
| BM25 Retrieval | 30.2 | 29.2 | 32.8 | 46.6 | 48.9 | 37.5 |
| **Meta-Harness** | **31.7** | **30.4** | **34.9** | **46.3** | **50.6** | **38.8** |

A single discovered harness transfers across five held-out models, improving accuracy by **4.7 points on average** over no retrieval.

### 4.3 Evaluating Agentic Coding Harnesses on TerminalBench-2

TerminalBench-2 evaluates LLM agents on 89 challenging tasks requiring long-horizon, fully autonomous execution under complex dependencies, and substantial domain knowledge. We initialize search from two strong open baselines: Terminus 2 and Terminus-KIRA.

**Results (Table 7) — Pass rate on TerminalBench-2**:

**Claude Opus 4.6:**
| Harness | Auto | Pass (%) |
|---------|------|---------|
| Claude Code | — | 58.0 |
| Terminus 2 | ✓ | 62.9/66.5 |
| Droid | — | 69.9 |
| TongAgents | — | 71.9 |
| MAYA-V2 | — | 72.1 |
| Terminus-KIRA | ✓ | 74.7 |
| Capy | — | 75.3 |
| **Meta-Harness** | **✓** | **76.4** |
| ForgeCode | — | 81.8 |

**Claude Haiku 4.5:**
| Harness | Auto | Pass (%) |
|---------|------|---------|
| OpenHands | — | 13.9 |
| Claude Code | — | 27.5 |
| Terminus 2 | ✓ | 28.3 |
| Mini-SWE-Agent | — | 29.8 |
| Terminus-KIRA | ✓ | 33.7 |
| Goose | — | 35.5 |
| **Meta-Harness** | **✓** | **37.6** |

Meta-Harness ranks **#2 among all Opus-4.6 agents** and **#1 among all Haiku-4.5 agents** on TerminalBench-2.

On the weaker Haiku 4.5 model, the improvement is larger: Meta-Harness achieves 37.6%, outperforming the next-best reported agent (Goose, 35.5%) by 2.1 points.

---

## 5 Discussion

Beyond outperforming existing harnesses, Meta-Harness has several practical advantages:
- Discovered harnesses **generalize to out-of-distribution classification datasets** and to **unseen base models** in the math setting.
- A search run completes in a **few hours of wall-clock time**, yet produces readable, transferable strategies that can be reused across models, including future, stronger ones.
- **Overfitting in code space is more inspectable**: brittle if-chains or hard-coded class mappings are visible on inspection in a way that weight-space overfitting is not.

More broadly, our results suggest that the main advantage of Meta-Harness is not just search over code, but search with *selective access to prior diagnostic experience*. The proposer is not limited to scalar rewards or fixed summaries; it can inspect raw code, execution traces, and prior failures, then use that information to form and test hypotheses about what to change.

Our findings reflect a recurring pattern in machine learning (Sutton, 2019): once a search space becomes accessible, stronger general-purpose agents can outperform hand-engineered solutions. A natural next step for future work is to co-evolve the harness and the model weights, letting the strategy shape what the model learns and vice versa.

---

## Appendix A: Qualitative Proposer Behavior (TerminalBench-2)

This section examines how the proposer uses the filesystem during search, drawing on the TerminalBench-2 run (10 iterations, Claude Opus 4.6).

### A.1 File Access Statistics

The proposer reads a **median of 82 files per iteration** (range 69–99), roughly evenly split between:
- Prior harness source code: 41%
- Execution traces: 40%
- Score/summary files: 6%
- Other: 13%

This confirms that the proposer's access pattern is non-Markovian: it routinely inspects the majority of available history rather than conditioning only on the most recent parent.

### A.2 Qualitative Behavior: Causal Reasoning Over Prior Failures

The TerminalBench-2 search log reveals a clear narrative arc. Rather than wandering randomly through local edits, the proposer forms an explicit diagnosis of why early candidates failed, then shifts toward a safer design pattern.

**Iterations 1–2: promising bugfixes are confounded by prompt edits.**

The first two iterations both bundle plausible structural fixes with prompt-template modifications, and both regress sharply from the 64.4% Terminus-KIRA baseline.

Iteration 1 hypothesis (verbatim from log):
> "Hypothesis: __CMDEND__ marker fragments leak into LLM observations on long-running tasks, causing the model to get confused and enter infinite no-tool-call loops. Stripping these markers + adding a loop breaker will recover wasted steps."

Iteration 2 hypothesis (verbatim):
> "Double-confirmation completion mechanism causes verification spirals. Observed in trajectories where the agent solves the task early but burns 15--40+ additional steps re-verifying because each verification command resets _pending_completion, requiring another task_complete → checklist → verify cycle."

**Iteration 3: the proposer identifies the confound.**

By iteration 3, the proposer explicitly infers that the regressions are not primarily due to the structural bugfixes themselves (verbatim):
> "Prior attempts: evo_marker_fix (58.9%, -5.6pp), evo_single_confirm (57.8%, -6.7pp) --- both regressed. Root cause of regressions: Prompt template changes (cleanup directives) caused the agent to delete necessary state before task completion. The structural bugfixes were confounded with harmful prompt changes. evo_strip_only isolates the two proven structural fixes."

**Iteration 7: the winning candidate.**

After six consecutive regressions, the proposer shifts strategy from modifying the control loop to adding information before the loop begins (verbatim):
> "All 6 prior iterations regressed from the 64.4% baseline because they modified the completion flow, prompt template, or observation processing. evo_env_bootstrap takes a different approach --- purely additive. It gathers an environment snapshot via a single shell command before the first LLM call and appends it to the initial prompt. No other methods are changed. This should eliminate 3--5 wasted exploration turns on dependency-heavy tasks without risking regression on already-passing tasks."

**Summary:** The search trajectory demonstrates that the proposer does more than random mutation. Across seven iterations, it identifies a confound, tests the confound-isolating hypothesis directly, observes that control-flow and prompt edits remain fragile, and then deliberately pivots to a purely additive modification that becomes the best candidate in the run. It subsequently tries to compose that winning idea with earlier fixes and even transfers lessons across runs.

---

## Appendix B: Discovered Harnesses

### B.1 Text Classification Harness

Meta-Harness discovers a family of memory-based harnesses. Two representative endpoints:

**Meta-Harness (Draft Verification)** — lowest-context frontier point:
1. Stage 1 (Draft): Retrieve the 5 nearest labeled examples and ask for an initial prediction.
2. Stage 2 (Verification): Condition retrieval on the draft label, retrieve 5 *confirmers* (same label) and 5 *challengers* (different labels), make the final prediction.
3. Cold start: If fewer than 5 labeled examples are available, use a standard single-call few-shot prompt.

**Meta-Harness (Label-Primed Query)** — highest-accuracy frontier point:
1. Label primer: List the valid output labels before showing any examples, so the model sees the full answer space up front.
2. Coverage block: For each known label, retrieve the most query-relevant labeled example.
3. Contrastive block: Build pairs of highly similar examples with different labels, exposing local decision boundaries.
4. Retrieval rule: TF-IDF similarity and query-anchored partner selection rather than label-agnostic nearest neighbors.

**Pareto-optimal discovered variants (Table 9)**:

| Variant | Avg Acc | Ctx (K) |
|---------|---------|---------|
| Meta-Harness (Draft Verification) | 40.1 | 5.4 |
| Meta-Harness (Error-Annotated) | 40.2 | 22.3 |
| Meta-Harness (CoT Replay) | 42.1 | 23.3 |
| Meta-Harness (Cluster Coverage) | 43.9 | 31.2 |
| Meta-Harness (Cascade Retrieval) | 44.9 | 39.2 |
| Meta-Harness (RRF + Contrastive) | 47.5 | 41.4 |
| Meta-Harness (Relevance + Contrastive) | 48.2 | 43.9 |
| Meta-Harness (Label-Primed Query) | 48.6 | 45.5 |

### B.2 Math Retrieval Harness

The discovered retrieval harness is a compact four-route BM25 program:

- **Combinatorics route**: Fetch 20 BM25 candidates, deduplicate to 8, rerank by lexical score and difficulty, return top 3.
- **Geometry route**: Return 1 hard NuminaMath reference together with 2 raw BM25 neighbors. No rerank.
- **Number theory route**: Fetch 12 BM25 candidates and rerank using lexical score, difficulty, and a small bonus for solutions that state a technique early.
- **Default (Algebra/Other)**: Fetch 10 BM25 candidates, rerank, choose adaptive number of examples based on how concentrated the top retrieval scores are.

A lexical router assigns each query to one of four subject-specific retrieval policies based on keyword sets and regex features for geometry notation.

### B.3 TerminalBench-2 Harness

The discovered harness builds on Terminus-KIRA, inheriting its native tool calling, 30KB output cap, and multi-perspective completion checklist. The main modification discovered by Meta-Harness is **environment bootstrapping**: before the agent loop begins, the harness runs a compound shell command to gather a snapshot of the sandbox environment and injects it into the initial prompt.

The snapshot includes: working directory, listing of /app, available programming languages and versions (Python, GCC, Node, Java, Rust, Go), installed package managers (pip, apt-get), and available memory. This eliminates the 2–4 exploratory turns that agents typically spend discovering what tools and files are available.

The bootstrapping command is guarded by a 15-second timeout and fails silently. The full implementation adds roughly **80 lines** on top of Terminus-KIRA.

**Per-task analysis**: Compared to Terminus-KIRA, the discovered harness gains on 7 of 89 tasks, with the largest improvements on protein-assembly and path-tracing. The gaining tasks share a common property: they require domain-specific tooling whose availability cannot be assumed in advance.

---

## Appendix D: Practical Implementation Tips

**Write a good skill.** The skill text is the primary interface for steering the search. It should constrain outputs and safety-relevant behavior, not the proposer's diagnosis procedure: specify what is forbidden, what artifacts to produce, and what objectives to optimize, while leaving the model free to inspect scores, traces, and prior code as needed.

**Start with a baseline harness and a hard search set.** Write a simple baseline (e.g., few-shot prompting), then construct the search set by filtering for examples that the baseline gets wrong or selecting a diverse subset of difficult instances. Keep the search set small enough for roughly 50 full evaluations per run.

**Log everything in a format that is easy to navigate.** Use machine-readable formats such as JSON, organize artifacts hierarchically, choose consistent file names, and adopt naming schemes that make simple tools such as regex search work well.

**Lightweight validation before expensive benchmarks.** Write a small validation test that imports the module, instantiates the class, and calls both methods on a tiny set of examples. Harnesses proposed during the search should pass this test before being fully evaluated.

**Automate evaluation outside the proposer.** Running evals is simple enough that it is not worth making the proposer do it. A separate harness should score candidates and write results to the filesystem.

---

## 繁體中文摘要（已有，保留供快速參考）

### 核心問題

現代 AI 系統嚴重依賴「harness」——決定模型接收什麼資訊、如何結構化、輸出如何後處理、結果如何反饋的程式碼和提示詞。目前 harness 設計是手動且耗力的。**Meta-Harness 透過 Agent 自動化 harness 探索。**

### 核心創新

與先前方法相比，Meta-Harness 提供**完整歷史診斷存取**：完整 trace + 程式碼，高達 10,000,000 tokens（約比先前文字優化方法大 1000 倍）。

### 對 Workspace 的啟示

1. **Harness 可自動優化**：harness-eval skill 的 Ratchet 理念有學術支撐
2. **Filesystem 作為診斷介面**：`claude-progress.json` 和 session notes 的設計方向正確
3. **Haiku + 優化 harness > 強模型**：直接支援 haiku-pilot 的核心假設
4. **動態範例選擇**：Skill 的 few-shot 範例應依任務類型動態選擇，而非硬編碼
5. **跨模型 harness 遷移性**：在 cc-workspace 設計的 harness 模式具有跨模型通用性

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性（×0.3） | 8/10 | 自動 harness 優化概念直接啟示 harness-eval 設計；Haiku + harness 的量化驗證 |
| B. 創新性（×0.2） | 9/10 | Filesystem-based 的 10M token 診斷存取是突破性創新，超越 DSPy/OPRO 的局限 |
| C. 證據品質（×0.2） | 9/10 | 三個任務域，多模型驗證，量化改善，跨分佈泛化均有數據 |
| D. 技術深度（×0.15） | 9/10 | 詳細架構、Filesystem 設計、搜索程序、計算成本分析均完整 |
| E. 泛化性（×0.15） | 8/10 | 跨模型、跨域、跨分佈的遷移性有實驗驗證 |
| **加權總分** | **8.55/10** | 8×0.3 + 9×0.2 + 9×0.2 + 9×0.15 + 8×0.15 |

**整合決策**：Agent  
**整合位置**：`.claude/agents/meta-harness-optimizer.md`（自動化 harness 探索迭代流程）  
**整合狀態**：待實作

**TODO**：
- 在 harness-eval skill 中加入「自動優化循環」概念說明和觸發條件
- 設計 claude-progress.json 的 trace 格式，使其可用於未來 Meta-Harness 式的診斷
