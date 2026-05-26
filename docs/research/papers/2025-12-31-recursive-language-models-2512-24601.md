---
title: "Recursive Language Models"
authors: "Alex L. Zhang, Tim Kraska, Omar Khattab"
published: "2025-12-31"
source: "https://arxiv.org/abs/2512.24601"
---

# Recursive Language Models

**Authors**: Alex L. Zhang, Tim Kraska, Omar Khattab  
**Affiliations**: MIT CSAIL  
**Correspondence**: altzhang@mit.edu, okhattab@mit.edu  
**Published**: December 31, 2025 (v1); revised May 11, 2026 (v3)  
**Source**: https://arxiv.org/abs/2512.24601  
**arXiv ID**: 2512.24601  
**DOI**: 10.48550/arXiv.2512.24601  
**License**: CC BY 4.0  
**Code**: https://github.com/alexzhang13/rlm  
**Categories**: cs.AI, cs.CL, cs.LG

---

## Abstract

We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference paradigm that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt.

We find that RLMs can successfully process inputs more than an order of magnitude beyond model context window limits and, even for shorter prompts, dramatically outperform the quality of vanilla frontier LLMs and common long-context and coding scaffolds (e.g., on GPT-5 by a median across the evaluated benchmarks of 26% against compaction, 130% against CodeAct with sub-calls, and 13% against Claude Code) across four diverse long-context tasks while having comparable cost.

At a small scale, we post-train the first model around the RLM. Our model, RLM-Qwen3-8B, outperforms the underlying Qwen3-8B model by a median of 28% and even approaches the quality of vanilla GPT-5 on three long-context tasks. Code is available at https://github.com/alexzhang13/rlm.

---

## 1 Introduction

Frontier reasoning models have limited context windows and, even within their limits, tend to exhibit context rot (Hong et al., 2025), a phenomenon where quality degrades steeply as prompts get longer. Though we expect context lengths to steadily rise through improvements to training, architecture, and infrastructure, we are interested in whether it is possible to scale the context size of general-purpose LLMs by orders of magnitude. This is increasingly urgent as LLMs begin to be widely adopted for long-horizon tasks, in which they must routinely process tens if not hundreds of millions of tokens.

We study this question through the lens of scaling inference-time compute. We are inspired by the way that reasoning models, another inference strategy, have become the fundamental interface to LLMs, resulting not only in empirical gains but also additional theoretical expressive power (Merrill and Sabharwal, 2024) compared to vanilla Transformers. Though most inference-time methods for dealing with long context are task-specific (Wu et al., 2021; Chang et al., 2024), the most popular general approach is context condensation or compaction (Khattab et al., 2021; Smith, 2025; OpenAI, 2025a; Wu et al., 2025), where context from user requests or agent trajectories is repeatedly summarized once it exceeds a length threshold. Unfortunately, compaction is rarely expressive enough for tasks that require dense access throughout the prompt. It presumes that some details that appear early in the prompt can safely be forgotten to make room for new content.

We introduce Recursive Language Models (RLMs), a general-purpose inference paradigm for dramatically scaling the effective input and output lengths of LLMs. The key insight is that arbitrarily long user prompts should not be fed into the neural network (e.g., Transformer) directly but should instead be treated as part of the environment that the LLM is tasked to symbolically and recursively interact with. This system serves as an abstracted "language model" without context limitations.

An RLM exposes the same external interface as an LLM or a reasoning model: it accepts a string prompt of arbitrary structure and produces a string response. Given a prompt P, the RLM initializes a Read-Eval-Print Loop (REPL) programming environment in which P is set as the value of a variable. It then offers the LLM general context about the REPL environment (e.g., the length of the string P), and permits it to write code that peeks into and decomposes P, and to iteratively observe any side effects from execution. Crucially, RLMs encourage the LLM to understand, transform, and execute the input prompt by writing symbolic programs that invoke the LLM itself on as many slices of the input as necessary.

By treating the prompt itself as an external object and enabling symbolic recursion, RLMs tackle limitations of expressive power in recent work on coding agents, retrieval agents, and sub-agent delegation. In particular, prior coding agents and retrieval agents treat some designated external data source (e.g., a filesystem or a corpus of search documents) as an environment for fetching snippets. However, they can only fill up the underlying LLM's context window with snippets before facing compaction. Similarly, prior self-delegation approaches (Anthropic, 2025; Sentient AI, 2025; Schroeder et al., 2025; Sun et al., 2025) allow LLMs to invoke themselves as sub-agents. However, they are handicapped by the underlying LLM's limited output lengths because they are designed to verbalize sub-calls autoregressively rather than producing them programmatically.

We evaluate RLMs using a frontier closed model (GPT-5; Singh et al. 2025) and a frontier open model (Qwen3-Coder-480B-A35B; Qwen Team 2025b) across four tasks with varying levels of complexity: deep research (Chen et al., 2025), information aggregation (Bertsch et al., 2025), code repository understanding (Bai et al., 2025), and a synthetic pairwise reasoning task where even frontier models fail catastrophically. We compare RLMs against direct LLM calls as well as context compaction, retrieval tool-use agents, and code-generation agents with and without sub-calls.

We find that RLMs demonstrate extremely strong performance even at the 10M+ token scale, and substantially outperform other approaches at long-context processing, in many cases by double-digit percentage gains while maintaining comparable cost. RLMs exhibit far less severe degradation for longer contexts and more sophisticated tasks.

Finally, at a small scale, we post-train the first natively recursive language model, demonstrating that RLMs can be improved quickly with little additional training. While a small open model (Qwen3-8B; Yang et al. 2025) struggles to solve long context tasks even in an RLM scaffold, our simple general-purpose training recipe uses only 1,000 samples from unrelated domains to improve its performance by a median of 28.3% across the four evaluation tasks.

---

## 2 Recursive Language Models

Given a base neural language model M with maximum context size K, a Recursive Language Model (RLM) is an inference-time scaffold around M that treats the user prompt as part of the environment without giving up the ability to densely process its content through different calls to M.

Given an arbitrary-length prompt P ∈ Σ*, an RLM interacts with a persistent external environment E and returns a response string Y ∈ Σ*. We would like effectively unbounded input tokens (|P| >> K), unbounded output tokens, and an unbounded semantic horizon, e.g. the ability to do Ω(|P|) or Ω(|P|²) semantic work.

**Algorithm 1** describes how an RLM achieves this. Given a prompt P, the RLM initializes a persistent REPL programming environment with a variable containing the user prompt as a string and a function for invoking a sub-RLM with a new prompt. Then, it starts the RLM loop. In the first iteration, the algorithm invokes the root neural model M with only (constant-size) metadata about the user prompt, like its length, a short prefix, and how to access parts of it.

The root is instructed via prompting and/or fine-tuning to operate like an RLM: that is, to generate code that helps it understand and transform parts of its prompt P, and to build up intermediate values and the final response into new variables, potentially by invoking the sub-RLM within loops.

Each iteration of the RLM loop executes code in the REPL, updates REPL state (intermediate variables), and collects in stdout any printed text. Only (constant-size) metadata about stdout, like a short prefix and length, is appended to M's history for the next iteration. This is key: it forces M to rely on variables and sub-calls to manage long strings instead of polluting its window. In principle, if we trim each turn to c tokens, we will have at most K/c root iterations, each of which can launch arbitrarily many sub-calls. Once the RLM sets the variable `Final` inside the REPL, iteration stops and the value in `Final` is returned as the response.

**Algorithm 1** (A recursive language model, around LLM M, which itself acts as a "language model"):
```
Input: prompt P
Output: response Y

state ← InitREPL(prompt=P)
state ← AddFunction(state, sub_RLM_M)
hist ← [Metadata(state)]

while True do:
    code ← LLM_M(hist)
    (state, stdout) ← REPL(state, code)
    hist ← hist || code || Metadata(stdout)
    if state[Final] is set then:
        return state[Final]
```

RLMs make three simple design choices that are missing from many existing scaffolds. To highlight these, we include **Algorithm 2** to illustrate a deceptively "similar" algorithm that is far less expressive. Both algorithms support some notion of sub-calls, external objects, and code execution, but they differ in terms of where the prompt and intermediate values live and where recursion occurs.

**Algorithm 2** (Alternate scaffold with standard poor design choices):
```
Input: prompt P
Output: response Y

actions ← {Finish, Exec, Search, sub_LLM_M}
hist ← [Metadata(actions), P]    ← Flaw #1

while True do:
    (action, val) ← LLM_M(hist)
    if action is Finish then:
        return val    ← Flaw #2
    out ← RUN(action, val)    ← Flaw #3
    hist ← hist || (action, val, out)
    if Tok(hist) > K then:
        hist ← Compact(hist)
```

**Flaw #1 — No symbolic handle**: An RLM must give the underlying LLM M a symbolic handle to the user prompt P, so the model can manipulate it without copying text into the root context window. Instead, ineffective Algorithm 2 starts by putting the user prompt P into the LLM context window (hist), inheriting the window limitations of M and falling back to heuristics like context compaction. Even though the scaffold can access external data with, say, a Search action, it is bounded with respect to user input.

**Flaw #2 — Bounded outputs**: Ineffective Algorithm 2 asks M to generate the output directly, via a Finish action. This may seem innocuous, but it means outputs cannot be longer than the context window of M.

**Flaw #3 — No symbolic recursion**: An RLM requires symbolic recursion. That is, code running inside E must be able to invoke M on programmatically constructed transformations of P (e.g., inside arbitrarily large loops), storing intermediate results symbolically. Though Algorithm 2 includes both a code execution action and a "sub-LLM" action separately, it is not able to invoke the sub-LLM programmatically and hence can only delegate a few explicitly verbalized tasks rather than writing short programs that can, say, loop over slices of the prompt and launch Ω(|P|) or even Ω(|P|²) processes to understand or transform all parts of P.

We implement our RLM definition in Algorithm 1 as follows: we equip an LLM with a Python REPL, where all tools, including sub-LM or sub-RLM calls, are available as modules. The initial prompt is stored as a variable in the REPL. The LLM interacts in a loop until it provides a final answer, which can be from either a variable in the REPL, or from the LLM itself. The LLM can also print from the REPL, but it is truncated to prevent overflowing the context too quickly.

---

## 3 Scaling Long Context Tasks

We hypothesize that the effective context window of an LLM cannot be understood independently of the specific task. That is, more "complex" problems will exhibit degradation at even shorter lengths than simpler ones. Because of this, we must characterize tasks in terms of how their complexity scales with prompt length.

For example, needle-in-a-haystack (NIAH) problems generally keep "needles" constant as prompt length is scaled. As a result, frontier models can now reliably solve these tasks in RULER (Hsieh et al., 2024) in the 1M+ token settings but struggle at far shorter lengths on OOLONG (Bertsch et al., 2025), a task where the answer depends explicitly on almost every line in the prompt.

### 3.1 Tasks

We design our evaluation around tasks where we can vary the lengths of the prompts, so we can consider problems whose difficulties scale differently with context length.

**S-NIAH.** Following the single needle-in-the-haystack task in RULER (Hsieh et al., 2024), we consider a set of 50 single tasks that require finding a specific phrase or number in a large set of unrelated text. Here, the information being sought scales as O(1) with respect to input length.

**BrowseComp-Plus (1K documents)** (Chen et al., 2025). A multi-hop question-answering benchmark for DeepResearch (OpenAI, 2025b) questions that requires reasoning over multiple different documents in an offline corpus. Following Sun et al. (2025), we use 150 randomly sampled instances as our evaluation set; we provide 1000 randomly chosen documents as input, in which the gold and evidence documents are guaranteed to exist. We report the percentage of correct answers. The answer to each task requires piecing together information from several documents, making this harder than S-NIAH despite also requiring a constant number of documents.

**OOLONG** (Bertsch et al., 2025). A long reasoning benchmark that requires semantically labeling and aggregating these labels to form a final answer. We focus specifically on the `trec_coarse` split, a set of 50 tasks over a dataset of questions with semantic labels. Each task requires using nearly all dataset questions, and therefore scales linearly in processing complexity relative to the input length.

**OOLONG-Pairs.** A modified variant of the `trec_coarse` split of OOLONG with 20 queries that specifically require aggregating pairs of chunks to construct the final answer. We report F1 scores over the answer, which is a list of entries. Each task requires using nearly all pairs of entries of the dataset, and therefore requires processing quadratically-many items relative to the input length.

**LongBench-v2 CodeQA** (Bai et al., 2025). A multi-choice code repository understanding split from LongBench-v2 that is challenging for modern frontier models. Each instance requires reasoning over a fixed number of files in a codebase to find the right answer.

### 3.2 Methods and Baselines

We compare RLMs against commonly used task-agnostic inference methods, using two modern LMs, GPT-5 with medium reasoning (Singh et al., 2025) and default sampling parameters, and Qwen3-Coder-480B-A35B (Yang et al., 2025) using the sampling parameters described in Qwen Team (2025b). For Qwen3-Coder-480B-A35B, we compute costs based on the compute provider Fireworks (Fireworks AI, 2025). In addition to evaluating the base model on all tasks, we also evaluate the following methods and baselines:

**CodeAct.** We compare directly to a CodeAct (Wang et al., 2024) agent that can execute code inside of a ReAct (Yao et al., 2023) loop. Unlike an RLM, CodeAct does not offload the user prompt to the code environment, and instead provides it directly to the LM. We consider two variants: (1) a version following Jimenez et al. (2024); Chen et al. (2025) where we equip this agent with a BM25 (Robertson and Zaragoza, 2009) retriever; (2) a version with a sub-call tool inside of the REPL. Compared to RLMs, this method loads the context directly into the model.

**Compaction agent.** Following Sun et al. (2025); Wu et al. (2025); Yu et al. (2025), we consider an iterative agent that compacts the context as it is filled. For example, given a corpus of documents, it will iteratively accumulate the documents and summarize when full. In cases where a single document exceeds the model window, the agent will chunk the document and iteratively compact it. For the GPT-5 experiments, due to the extremely high cost of applying this strategy to millions of tokens, we use GPT-5-nano for compaction and GPT-5 to provide the final answer.

**Coding agents.** We compare against commonly used coding agents like OpenCode (Anomaly, 2026) and Claude Code (Anthropic, 2025). We consider two variants, one where the context is offloaded to a file, and another where it is directly used as the initial prompt. Closed source agents like Claude Code are designed around a corresponding model, so we use Claude Opus 4.1 with Claude Code v2.0.0 (released around the same time as the GPT-5 model we use in our main results) for this baseline.

**RLM.** We implement an RLM with a Python REPL environment, which loads a module for querying a sub-LM and uses a system prompt presented in Appendix C. For the GPT-5 experiments, we use GPT-5-mini for the recursive LMs and GPT-5 for the root LM, as we found this choice to strike a good balance between the capabilities of RLMs and the cost of the recursive calls. We also evaluate several different max recursion depths allowable to the RLM, from 0–3. Max recursion depth 0 is an RLM without sub-calling capabilities. Max recursion depth 1 allows sub-calling LLMs, while max depth >1 allows sub-calling RLMs. We notate a RLM with max recursion depth N using a model as RLM(model, depth=N), e.g. RLM(GPT-5, depth=2), and assume depth=1 if not stated otherwise.

**Fine-tuning.** To create RLM-Qwen3-8B, we fine-tune Qwen3-8B on 1,000 filtered trajectories of Qwen3-Coder-480B-A35B as an RLM with Qwen3-8B sub-calls on LongBenchPro (Chen et al., 2026) tasks. We use sampling parameters described in Qwen Team (2025a), and evaluate the fine-tuned RLM-Qwen3-8B as an RLM. The key insight for training is that being an effective sub-call model is roughly similar to being a general purpose reasoning model, so we can make the training much more tractable at small scale by focusing on improving the root model's ability to manipulate the REPL and to launch recursive calls.

---

## 4 Results and Discussion

### Main Results (Table 1)

Performance comparison across long-context benchmarks. Task lengths: CodeQA 23K–4.2M tokens, BrowseComp+ 6M–11M tokens, OOLONG 131K tokens, OOLONG-Pairs 32K tokens. (∗ = method sometimes hit input context limits.)

**GPT-5 (with RLM sub-calls to GPT-5-mini):**

| Model | CodeQA | BrowseComp+ (1K) | OOLONG | OOLONG-Pairs |
|-------|--------|-----------------|--------|-------------|
| Base Model | 24.0∗ ($0.13) | 0.0∗ | 44.0 ($0.14) | 0.1 ($0.16) |
| CodeAct (+ BM25) | 22.0∗ ($0.06) | 51.0 ($0.71) | 38.0 ($0.61) | 24.7 ($0.75) |
| CodeAct (+ sub-calls) | 24.0∗ ($0.06) | 0.0∗ | 40.0 ($0.85) | 28.4 ($1.11) |
| Compaction agent | 58.0 ($1.31) | 70.5 ($0.57) | 46.0 ($0.13) | 0.1 ($0.13) |
| OpenCode | 18.0∗ | 0.0∗ | 32.0 | 3.1 |
| OpenCode (+ context offloading) | 64.0 | 94.0 | 52.0 | 4.8 |
| RLM (depth=0) | 58.0 ($0.18) | 88.0 ($0.44) | 36.0 ($0.37) | 43.9 ($0.69) |
| RLM (depth=1) | 62.0 ($0.11) | 91.3 ($0.99) | 56.0 ($0.43) | 58.0 ($0.33) |
| RLM (depth=2) | 66.0 ($0.15) | 92.0 ($0.55) | 56.5 ($1.10) | 65.5 ($0.33) |
| RLM (depth=3) | 58.0 ($0.15) | 92.0 ($0.51) | 58.0 ($0.51) | 76.0 ($0.39) |

**Qwen3-Coder-480B-A35B:**

| Model | CodeQA | BrowseComp+ (1K) | OOLONG | OOLONG-Pairs |
|-------|--------|-----------------|--------|-------------|
| Base Model | 20.0∗ ($0.13) | 0.0∗ | 36.0 ($0.06) | 0.1 ($0.05) |
| CodeAct (+ BM25) | 24.0∗ ($0.17) | 12.7 ($0.39) | 38.0 ($1.51) | 0.3 ($1.54) |
| CodeAct (+ sub-calls) | 26.0∗ ($0.28) | 0.0∗ | 32.0 ($1.83) | 0.1 ($1.49) |
| Compaction agent | 50.0 ($1.26) | 38.0 ($8.98) | 44.1 ($0.15) | 0.31 ($0.05) |
| OpenCode | 12.0∗ | 0.0∗ | 36.0 | 0.0 |
| OpenCode (+ context offloading) | 40.0 | 58.0 | 24.0 | 2.1 |
| RLM (depth=0) | 66.0 ($0.18) | 46.0 ($0.82) | 43.5 ($0.32) | 17.3 ($1.77) |
| RLM (depth=1) | 56.0 ($0.92) | 44.7 ($0.84) | 48.0 ($0.61) | 23.1 ($1.02) |
| RLM (depth=2) | 54.0 ($1.88) | 68.0 ($1.05) | 26.0 ($1.03) | 19.0 ($1.61) |
| RLM (depth=3) | 44.0 ($1.65) | 68.7 ($1.10) | 32.0 ($0.80) | 21.1 ($1.67) |

**Claude Opus 4.1:**

| Model | CodeQA | BrowseComp+ (1K) | OOLONG | OOLONG-Pairs |
|-------|--------|-----------------|--------|-------------|
| Claude Code | 12.0∗ ($2.03) | 0.0∗ | 40.2 ($3.43) | 0.1 ($6.75) |
| Claude Code (+ context offloading) | 62.0 ($1.25) | 84.0 ($2.03) | 48.0 ($0.98) | 6.5 ($2.99) |

### Key Observations

**Observation 1: RLMs can scale to the 10M+ token regime and can outperform base LMs and existing task-agnostic agent scaffolds on long context tasks.** Across all tasks, RLMs demonstrate strong performance on prompts well beyond the effective context window of a frontier LM, outperforming base models and common long-context scaffolds by up to 2× the performance while maintaining comparable or cheaper average token costs. Notably, RLMs scale well beyond the base models' context window. For instance, on BrowseComp-Plus (1K), a linearly extrapolated cost for GPT-5-mini ingesting 6–11M input tokens is $1.50–$2.75, while RLM(GPT-5, depth=1) has an average cost of $0.99 and outperforms both the compaction and retrieval baselines by over 29%.

Furthermore, on tasks where processing costs scale with the input context, RLMs make significant improvements over the base model, even on tasks within the model's context window. On OOLONG, the RLM(depth=1) with GPT-5 and Qwen3-Coder outperform the base model by 28.4% and 33.3% respectively. On OOLONG-Pairs, both GPT-5 and Qwen3-Coder make little progress with F1 scores of ≤0.1%, while the RLM(depth=1) using these models achieve F1 scores of 58.0% and 23.1% respectively, highlighting the capability of RLMs to handle extremely information-dense tasks.

**Observation 2: The REPL is necessary for handling long inputs, while the recursive sub-calling of RLMs provides strong benefits on information-dense inputs.** A key characteristic of RLMs is offloading the context as a variable in an environment E that the model can interact with. In particular, RLM(depth=0) and coding agents like Claude Code and OpenCode are able to scale beyond the context limit of the model and outperform other task-agnostic baselines on most long context settings. On CodeQA in particular with Qwen3-Coder-480B-A35B, the no-sub-calling RLM(depth=0) is able to outperform all sub-calling variants of the RLM.

On information-dense tasks like OOLONG or OOLONG-Pairs, we observed several cases where programmatic recursive LM sub-calling is necessary. RLM(Qwen3-Coder) performs the necessary semantic transformation line-by-line through recursive sub-calls, while the ablation without sub-calls is forced to use keyword heuristics to solve these tasks. On OOLONG-Pairs in particular, the higher recursive depth variants of the RLM for GPT-5 outperform all other methods including Claude Code and OpenCode by a large margin.

**Observation 3: LM performance degrades as a function of input length and problem complexity, while RLM performance scales better.** The benchmarks S-NIAH, OOLONG, and OOLONG-Pairs contain a fixed number of tasks over contexts with lengths ranging from 2^13 to 2^20. Each benchmark can be categorized by different processing complexity of the input context with respect to length (roughly constant, linear, and quadratic respectively). GPT-5 performance degrades significantly faster for more complex tasks, while RLM performance degrades at a slower rate. For context lengths beyond 2^14, the RLM consistently outperforms GPT-5.

**Observation 4: The inference cost of RLMs remains comparable to other methods, and in some cases base LM calls.** On average, the inference cost of RLMs is cheaper or comparable to most other baselines, including standard coding agents. The median RLM run is cheaper than the median base model run, but more expensive on average due to outlier trajectories where the RLM struggles to find an answer.

**Observation 5: Beyond long-context, RLMs enable longer reasoning capabilities.** (Table 2 — LongCoT-mini results)

| Model | Overall | MATH | CHEM | CS | LOGIC | CHESS |
|-------|---------|------|------|-----|-------|-------|
| GPT-5.2 (base) | 38.7 | 26.0 | 37.0 | 40.4 | 53.6 | 36.6 |
| RLM (GPT-5.2, depth=1) | 50.6 | 5.6 | 50.0 | 11.0 | 86.7 | 93.0 |
| RLM (GPT-5.2, depth=1) + decomposition hints | 65.6 | 32.0 | 52.0 | 46.0 | 99.0 | 99.0 |

RLM(GPT-5.2, depth=1) uses the REPL to outperform the base model. When providing explicit hints on how to decompose tasks, we find the RLM is able to reliably generate a graph of the problem, solving each node using sub-calls as it programmatically traverses the reasoning graph. It outperforms the base model on all domains and by a 69.5% performance increase overall.

**Observation 6: Training RLMs on one domain can improve general downstream RLM performance, as well as efficiency. Training also exhibits length generalization.** Certain behaviors in RLM trajectories are common among different domains, such as probing the input and recursively sub-calling on shorter contexts. RLM-Qwen3-8B, a Qwen3-8B model fine-tuned on RLM(Qwen3-Coder-480B-A35B) trajectories on a small, unrelated set of tasks (LongBenchPro; Chen et al. 2026) considerably outperforms the base Qwen3-8B as a RLM across all tasks. Furthermore, its inference costs are much lower and more than 3× faster due to better decision making and fewer mistakes as a RLM. Training RLMs also exhibits length generalization; by purely training through reinforcement learning with verifiable rewards (RLVR) on a smaller split, RLM(Qwen3-4B-Instruct-0527) is able to generalize to longer, more difficult splits.

---

## 5 Analyses of RLM Trajectories

RLMs exhibit interesting context and problem decomposition behavior. We discuss observable behavior in small and large LLMs as RLMs to understand how we can steer and improve their performance and efficiency through training and prompt tuning.

**Observed RLM decomposition patterns.** Current models as RLMs attempt to probe, then decompose a task into sub-tasks for recursive sub-calls to solve. In many cases such as on BrowseComp-Plus, the LM uses model priors to programmatically narrow the search space of sub-calls. RLMs are also able to output beyond their context window by stitching together sub-LM calls inside the REPL, which is required to solve tasks like OOLONG-Pairs.

**First decomposition and errors in RLM trajectories.** RLMs defer essentially unbounded-length reasoning chains to sub-LM calls. The choice of decomposition can greatly affect task performance, especially for information-dense problems. In-context RLM trajectories greatly improve both overall performance and the initial decomposition attempt made by the RLM, even if the example is unrelated to the actual task. Furthermore, while RLMs frequently recover from an initially incorrect decomposition pattern, the first decomposition attempt is important for overall performance.

RLM(Qwen3-Coder) trajectories contain significantly more syntax errors, even for correct trajectories, compared to RLM(GPT-5). These errors explain why higher recursion depths for RLM(Qwen3-Coder) perform worse on average: Qwen3-Coder-480B-A35B often makes syntax errors that result in failed outputs, and having sub-RLM calls propagates this issue to sub-calls.

---

## 6 Related Works

**Long-Context LM Systems.** There have primarily been two orthogonal directions for long-context management in language model systems: (1) directly changing the architecture of and retraining the base LM to handle longer contexts (Press et al., 2022; Gu et al., 2022; Munkhdalai et al., 2024), and (2) building a scaffold around the LM that implicitly handles the context — RLMs focus on the latter. One popular class of such strategies is lossy context management (Chen et al., 2023), which uses compaction or truncation to compress the input context at the cost of potentially losing fine-grained information. For example, ReSum (Wu et al., 2025) adds a summarization tool to periodically compress the context of a multi-turn agent. Another class of strategies implement an explicit memory hierarchy in the agent scaffold (Packer et al., 2024; Chhikara et al., 2025; Zhang et al., 2025). RLMs differ from these works in that all context window management is implicitly handled by the LM itself.

**Task Decomposition through sub-LM calls.** Many LM-based agents (Guo et al., 2024; Anthropic, 2025) use multiple, well-placed LM calls to solve a problem; however, many of these calls are placed based on human-engineered workflows. Several methods like ViperGPT (Surís et al., 2023), THREAD (Schroeder et al., 2025), ReDel (Zhu et al., 2024), Context Folding (Sun et al., 2025), and AgentFold (Ye et al., 2025) have explored deferring the choice of sub-LM calls to the LM. These techniques emphasize task decomposition through recursive LM calls, but are unable to handle long context inputs beyond the length of the base LM. DisCIPL (Grand et al., 2025) generates programs with sub-LM calls, but these programs are generated in a single-step and cannot recover from generation mistakes. RLMs, on the other hand, are enabled by an extremely simple intuition (i.e., placing the prompt in the external environment) to symbolically manipulate arbitrarily long strings and to iteratively refine their recursion via execution feedback from the persistent REPL.

---

## 7 Limitations and Future Work

While RLMs show strong performance on tasks beyond the context window limitations of existing LMs at reasonable inference costs, evaluations for more difficult and natural long-context processing tasks and the best mechanisms for implementing guardrails for RLMs both remain highly under-explored. Broadly, RLMs add a layer of complexity on top of existing LMs that may lead to unintentional side-effects like exploding sub-call costs, which we leave for future work to solve. We also note that future strategies involving asynchronous sub-calls and sandboxed REPLs can potentially significantly reduce the runtime and inference cost of RLMs, but further contribute to this complexity.

We focused our experiments on evaluating RLMs using existing frontier models, but show initial evidence on a Qwen3-8B model that explicit training as a RLM provides very rapid performance improvements, even outside the training domain. We hypothesize that RLM trajectories can be viewed as a form of reasoning (OpenAI et al., 2024; DeepSeek-AI et al., 2025), which can be trained by bootstrapping existing models (Zelikman et al., 2022, 2024). We hope that training native RLMs can be treated as a new axis of scale to improve LM performance on general and long-horizon tasks.

---

## 8 Conclusion

We introduced Recursive Language Models (RLMs), a general inference framework for language models that offloads the input context and enables language models to recursively sub-query language models before providing an output. We explored an instantiation of this framework that offloads the context into a Python REPL environment as a variable in memory, enabling the LM to reason over its context in code and recursive LM calls, rather than purely in token space. Our results across multiple settings and models demonstrated that RLMs are an effective task-agnostic paradigm for both long-context problems and general reasoning. Building on our small fine-tuning experiments, we are excited to see future work that explicitly trains models to reason as RLMs, which could result in another axis of scale for the next generation of language model systems.

---

## References

- Anomaly (2026). OpenCode: the open source AI coding agent.
- Anthropic (2025). Claude Code: subagents — modular AI workflows with isolated agent contexts.
- Bai, Y., Tu, S., Zhang, J., et al. (2025). LongBench v2: towards deeper understanding and reasoning on realistic long-context multitasks. arXiv:2412.15204.
- Bertsch, A., Pratapa, A., Mitamura, T., Neubig, G., and Gormley, M.R. (2025). OOLONG: evaluating long context reasoning and aggregation capabilities. arXiv:2511.02817.
- Chang, Y., Lo, K., Goyal, T., and Iyyer, M. (2024). BooookScore: a systematic exploration of book-length summarization in the era of LLMs. ICLR 2024.
- Chen, H., Pasunuru, R., Weston, J., and Celikyilmaz, A. (2023). Walking down the memory maze: beyond context limit through interactive reading. arXiv:2310.05029.
- Chen, Z., Ma, X., Zhuang, S., et al. (2025). BrowseComp-plus: a more fair and transparent evaluation benchmark of deep-research agent. arXiv:2508.06600.
- Chen, Z., Wu, X., Jia, J., et al. (2026). LongBench Pro: a more realistic and comprehensive bilingual long-context evaluation benchmark. arXiv:2601.02872.
- Chhikara, P., Khant, D., Aryan, S., Singh, T., and Yadav, D. (2025). Mem0: building production-ready AI agents with scalable long-term memory. arXiv:2504.19413.
- DeepSeek-AI, Guo, D., Yang, D., et al. (2025). DeepSeek-R1: incentivizing reasoning capability in LLMs via reinforcement learning. arXiv:2501.12948.
- Fireworks AI (2025). Qwen3 Coder 480B A35B Instruct. https://fireworks.ai/models/fireworks/qwen3-coder-480b-a35b-instruct
- Goldman, O., Jacovi, A., Slobodkin, A., et al. (2025). Is it really long context if all you need is retrieval? Towards genuinely difficult long context NLP. arXiv:2407.00402.
- Grand, G., Tenenbaum, J.B., Mansinghka, V.K., Lew, A.K., and Andreas, J. (2025). Self-steering language models. arXiv:2504.07081.
- Gu, A., Goel, K., and Ré, C. (2022). Efficiently modeling long sequences with structured state spaces. arXiv:2111.00396.
- Guo, T., Chen, X., Wang, Y., et al. (2024). Large language model based multi-agents: a survey of progress and challenges. arXiv:2402.01680.
- Hong, K., Troynikov, A., and Huber, J. (2025). Context rot: how context degradation affects LLM performance.
- Hsieh, C., Sun, S., Kriman, S., et al. (2024). RULER: what's the real context size of your long-context language models? arXiv:2404.06654.
- Jimenez, C.E., Yang, J., Wettig, A., et al. (2024). SWE-bench: can language models resolve real-world GitHub issues? arXiv:2310.06770.
- Khattab, O., Potts, C., and Zaharia, M. (2021). Baleen: robust multi-hop reasoning at scale via condensed retrieval. NeurIPS 34, pp. 27670–27682.
- Merrill, W. and Sabharwal, A. (2024). The expressive power of transformers with chain of thought. ICLR 2024.
- Motwani, S.R., Nichols, D., London, C., et al. (2026). LongCoT: benchmarking long-horizon chain-of-thought reasoning. arXiv:2604.14140.
- Munkhdalai, T., Faruqui, M., and Gopal, S. (2024). Leave no context behind: efficient infinite context transformers with Infini-attention. arXiv:2404.07143.
- OpenAI (2024). OpenAI o1 system card. arXiv:2412.16720.
- OpenAI (2025a). Codex CLI: a lightweight coding agent for your terminal.
- OpenAI (2025b). Deep research. AI-powered research assistant tool.
- Packer, C., Wooders, S., Lin, K., et al. (2024). MemGPT: towards LLMs as operating systems. arXiv:2310.08560.
- Press, O., Smith, N.A., and Lewis, M. (2022). Train short, test long: attention with linear biases enables input length extrapolation. arXiv:2108.12409.
- Qwen Team (2025a). Qwen3-8B. https://huggingface.co/Qwen/Qwen3-8B
- Qwen Team (2025b). Qwen3-Coder-480B-A35B-Instruct. https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct
- Robertson, S. and Zaragoza, H. (2009). The probabilistic relevance framework: BM25 and beyond. Found. Trends Inf. Retr. 3(4), pp. 333–389.
- Schroeder, P., Morgan, N., Luo, H., and Glass, J. (2025). THREAD: thinking deeper with recursive spawning. arXiv:2405.17402.
- Sentient AI (2025). ROMA: the backbone for open-source meta-agents.
- Singh, A., et al. (2025). GPT-5 technical report.
- Surís, D., Menon, S., and Vondrick, C. (2023). ViperGPT: visual inference via python execution for reasoning. ICCV 2023.
- Vodrahalli, K., et al. (2024). MRCRv2. 
- Wang, X., et al. (2024). CodeAct: executable code actions elicit better LLM agents.
- Wu, J., et al. (2021). SCROLLS: standardized comparison over long language sequences.
- Wu, Z., et al. (2025). ReSum: context compaction via summarization for multi-turn agents.
- Yang, A., et al. (2025). Qwen3 technical report.
- Yao, S., et al. (2023). ReAct: synergizing reasoning and acting in language models. ICLR 2023.
- Ye, J., et al. (2025). AgentFold: folding long-context tasks via multi-agent delegation.
- Yu, Z., et al. (2025). Context compaction for long-horizon agents.
- Zelikman, E., et al. (2022). STaR: bootstrapping reasoning with reasoning. NeurIPS 2022.
- Zelikman, E., et al. (2024). Quiet-STaR: language models can teach themselves to think before speaking.
- Zhang, A.L., et al. (2025). MemoryOS: operating system inspired memory management for language model agents.
- Zhu, J., et al. (2024). ReDel: a toolkit for LLM-powered recursive multi-agent systems.

---

## Citation

```bibtex
@article{zhang2025recursive,
  title={Recursive Language Models},
  author={Zhang, Alex L. and Kraska, Tim and Khattab, Omar},
  journal={arXiv preprint arXiv:2512.24601},
  year={2025}
}
```

---

**Keywords**: recursive language models, long-context processing, inference-time scaling, REPL, symbolic recursion, context window, programmatic sub-calls, RLM-Qwen3-8B, LongBench, OOLONG
