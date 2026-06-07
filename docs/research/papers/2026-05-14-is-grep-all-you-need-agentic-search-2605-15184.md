---
title: "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"
arxiv_id: 2605.15184
authors: "Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah"
fetched: 2026-05-26
published: 2026-05-14
source: "https://arxiv.org/abs/2605.15184"
source_tier: P
---

# Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

**Authors**: Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah (PricewaterhouseCoopers, U.S.)
**Published**: May 14, 2026
**Source**: https://arxiv.org/abs/2605.15184
**arXiv ID**: 2605.15184
**License**: CC BY 4.0
**Categories**: cs.CL

---

## Abstract

Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. Despite the growing adoption of retrieval-augmented generation (RAG) in agentic systems, existing literature lacks a systematic comparison of how retrieval strategy choice interacts with agent architecture and tool-calling paradigm. Important practical dimensions, including how tool outputs are presented to the model and how performance changes when searches must cope with more irrelevant surrounding text, remain under-explored in agent loops.

This paper reports an empirical study organized into two experiments. Experiment 1 compares grep and vector retrieval on a 116-question sample from LongMemEval, using a custom agent harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, and Gemini CLI), for both inline tool results and file-based tool results that the model reads separately. Experiment 2 compares grep-only and vector-only retrieval while progressively mixing in additional unrelated conversation history, so that each query is embedded in more distracting material alongside the passages that matter. Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same.

**Keywords**: Agentic Search, Semantic Search, Lexical Search, Context Engineering, Agent Harnesses, LLM Evaluation, Grep

---

## Core Thesis

Retrieval strategy, agent harness, and delivery mechanism function as a **single jointly-evaluated system**, not independent design choices. The same LLM backbone under different harnesses shows accuracy swings comparable to switching retrieval strategies entirely. Inline grep consistently beats inline vector across all tested harness–model pairs on LongMemEval; however, file-based delivery can invert this ordering.

---

## 1. Introduction

Modern LLM agents increasingly rely on RAG to access external knowledge at inference time, enabling them to reason over corpora that far exceed their context windows. Through tool calling, agents issue search queries, receive ranked results, and iteratively refine their understanding before producing an answer. Two retrieval paradigms dominate:

- **Semantic vector search**: embeds queries and documents into a shared latent space for approximate nearest-neighbor matching
- **Lexical search** (grep, BM25, regex): performs exact or pattern-based matching over raw text

While vector search has become the default in most RAG systems, lexical search remains widely used due to simplicity, stability, and low embedding cost. However, how retrieval strategy interacts with agent architecture and tool-calling paradigm in end-to-end agentic workflows remains poorly understood.

The emergence of provider-native CLI agents (Claude Code, Codex, Gemini CLI) has created a new class of agentic systems that differ fundamentally from custom-built harnesses. These provider harnesses embed tool calling into a shell-based interface where the model has direct access to command-line tools including grep, while custom harnesses offer fine-grained control over the tool-calling loop, context construction, and result formatting.

**Paper contributions:**

1. **Retrieval, harness, and presentation**: Evidence on how lexical vs. dense retrieval combines with agent orchestration and inline vs. file-based output delivery.
2. **Noise and scale**: Characterization of how end-to-end behavior evolves as irrelevant surrounding content grows relative to task-relevant material.
3. **Heterogeneity across agent stacks**: Direct comparison showing retrieval effectiveness is not stable across architecturally distinct harnesses even when the underlying text corpus is held fixed.

---

## 2. Overview of Retrieval in Agentic Systems

Retrieval in agentic systems is iterative and agent-directed: the model decides what to search for, how many queries to issue, and whether retrieved results are sufficient. This process is mediated by two design dimensions: the **retrieval strategy** and the **agent harness**.

### 2.1. Retrieval Strategies

#### 2.1.1. Lexical Search

Performs exact or pattern-based matching over raw text. Classical approaches like BM25 score by term frequency and inverse document frequency; grep uses regular expressions or substring matching. Requirements: no embedding model or vector index — negligible computational cost beyond the text scan. The BEIR benchmark showed BM25 remains competitive across diverse retrieval tasks, often outperforming early dense retrieval models in zero-shot settings.

Learned sparse representations (SPLADE) extend lexical matching by expanding query and document terms through a learned vocabulary, bridging the gap between exact matching and semantic understanding while preserving interpretability and efficiency.

#### 2.1.2. Semantic Search

Encodes queries and documents as dense vectors; retrieves via approximate nearest-neighbor search. RAG systems couple dense retrieval with a generative model. Modern pipelines embed documents at indexing time and queries at inference time, with optional post-retrieval reranking. Semantic search handles paraphrases and semantic similarity but introduces dependencies on embedding model quality, vector index infrastructure, and indexing latency.

#### 2.1.3. Hybrid Approaches

Combines lexical and semantic signals. Reciprocal Rank Fusion (RRF) merges ranked lists without score calibration. Late interaction models (ColBERT) compute fine-grained token-level similarity. Sparse and dense methods often retrieve different relevant documents, making their combination more effective than either alone. In agentic settings, hybrid retrieval can also emerge organically when agents have access to both tool types.

### 2.2. Agent Harnesses

The agent harness manages the tool-calling loop: constructs the prompt, dispatches tool calls, receives results, and decides whether to continue or produce a final answer.

#### 2.2.1. Custom Harnesses

Built by developers using agent frameworks, provider SDKs, or custom code. Provide fine-grained control over every stage: system prompt, tool definitions, context construction, result formatting, and iteration termination criteria. The ReAct paradigm (reasoning traces interleaved with tool actions) is most widely adopted. Custom harnesses allow explicit context window management (summarizing or discarding earlier results). **Tradeoff**: significant developmental overhead.

#### 2.2.2. Provider-Native CLI Harnesses

Embed tool calling into a shell-based interface with direct model access to system utilities (grep, find, cat, etc.). The harness manages context construction and iteration control according to provider's internal implementation, which is largely opaque to users. **Advantages**: minimal setup cost, leverages provider's optimized context engineering. **Sacrifice**: fine-grained control. Notably, when grep is available as a native bash tool, the boundary between "retrieval strategy" and "agent capability" blurs — the agent can construct its own grep commands dynamically.

### 2.3. Tool-Calling Architectures

Tool-calling method is a **context engineering decision**.

#### 2.3.1. Standard (Inline)

Search results returned directly as tool response messages appended to the conversation context. Simple — results appear inline. However, large result sets compete for context window space with system prompt, conversation history, and previous tool results, creating **context rot** that can degrade performance on long-horizon tasks.

#### 2.3.2. Programmatic (File-Based)

Results written to disk; model receives only a file path or summary pointer. Decouples retrieval result size from context window pressure. Enables **progressive disclosure** — agent reads only a subset based on metadata. **Tradeoff**: indirectness; agent must execute additional tool call to access results, adding latency and requiring understanding of the file-based workflow.

---

## 3. Methodology

### 3.1. Task and Dataset

Evaluates on a **116-question representative subset of LongMemEval** (Wu et al., 2025), which tests an agent's ability to answer questions over long conversations spanning multiple sessions. Each question has:
- One or more **oracle sessions** containing the information needed to answer correctly
- Variable number of **distractor sessions** irrelevant to the query

**Question categories** (6):
- `knowledge-update`: tracking state changes over time
- `multi-session`: aggregating information across sessions
- `single-session-assistant`: recalling model-generated content
- `single-session-preference`: user personal preferences
- `single-session-user`: user-stated facts
- `temporal-reasoning`: computing durations, ordering events, resolving dates

### 3.2. Retrieval Implementations

#### 3.2.1. Structured Events via Chronos

The search layer operates over per-question files, serializing LongMemEval dialogue turns together with structured temporal events extracted via the Chronos preprocessing pipeline. Chronos targets long-horizon conversation memory by surfacing salient time structure (explicit dates, intervals, related time spans) as first-class text records coupled with raw utterances.

Two reasons for adopting this layer:
1. Study evaluates search techniques, not temporal reasoning — structured event extraction ensures success on temporal items reflects evidence location ability, not date reconstruction from fragmented mentions.
2. Mirrors preprocessing a long-memory agent would use in deployment → realistic production configuration.

#### 3.2.2. Lexical Search (Grep)

Loads conversation turns and extracted temporal events from per-question files into memory; executes regex matching over raw text fields. Results scored by match count and returned. **Requirements**: no embedding model, vector index, or external service — all matching performed in-process over local files.

#### 3.2.3. Semantic Search (Vector)

Queries a search index populated at ingestion time. Each turn and temporal event is embedded and stored in a per-question index with a versioned schema. At query time, embeds the natural language query and retrieves via approximate nearest-neighbor search. A reranking step re-scores passages before returning top-k results (k selected by the agent).

### 3.3. Agent Harnesses

#### 3.3.1. Custom Harness (Chronos)

Implements an agent using LangChain with access to four search tools (grep and vector search over turns and events). Uses **dynamic prompting**: system instructions, search hints, and tool-use guidance depend on the detected question category (e.g., temporal reasoning vs. preference recall). The agent starts each episode with category-conditioned guidance, followed by an initial broad context block (top-15 vector results) before the tool-calling loop begins. Loop continues until the model produces a final answer.

#### 3.3.2. Provider-Native CLI Harnesses

Evaluates three provider-native CLI agents: **Claude Code**, **Codex**, and **Gemini CLI**. Each receives the question and a dynamically generated search strategy, and can invoke bash-callable wrapper scripts for grep and vector search via absolute paths. In standard mode, the process was spawned in a sandbox to ensure the model has access to only relevant files.

### 3.4. Tool-Calling Architectures

- **Standard (Inline)**: Search scripts print results directly to stdout. For Chronos, results returned as tool response messages. For CLI harnesses, stdout appended to working context.
- **Programmatic (File-Based)**: All results written to a file the agent then reads or searches.

### 3.5. Models

Five LLMs evaluated across a range of capability levels:
- **Claude Opus 4.6**
- **Claude Haiku 4.5**
- **GPT-5.4**
- **Gemini 3.1 Pro**
- **Gemini 3.1 Flash-Lite**

### 3.6. Evaluation

Follows LongMemEval evaluation protocol. Uses **GPT-4o as the auxiliary LLM grader**. For each question, the grader receives: question text, reference answer, and agent hypothesis; outputs a binary judgment under category-conditioned instructions (tolerance for off-by-one temporal counts, rubric-style scoring for preference items, abstention handling). Reports accuracy as fraction of questions where grader answers affirmatively.

---

## 4. Experiments

### 4.1. Experiment 1: Retrieval Mode, Harness, and Tool Calling Method

**Goal**: Isolate how retrieval mode (grep-only vs. vector-only), agent harness (Chronos vs. Claude Code vs. Codex vs. Gemini CLI), and tool calling method (standard inline vs. programmatic file-based) jointly affect end-to-end accuracy when the full per-question haystack is exposed.

#### 4.1.3. Results

**Table 1**: Overall accuracy (%) on 116-question LongMemEval-S subset.

| Model | Harness | grep (inline) | vector (inline) | grep (programmatic) | vector (programmatic) |
|-------|---------|--------------|-----------------|--------------------|-----------------------|
| Claude Opus 4.6 | Chronos | **93.1** | 83.6 | 80.2 | 81.9 |
| Claude Opus 4.6 | Claude Code | 76.7 | 75.0 | 68.1 | **79.3** |
| Claude Haiku 4.5 | Chronos | **83.6** | 76.7 | **83.6** | 81.9 |
| Claude Haiku 4.5 | Claude Code | **55.2** | 44.0 | **37.1** | 32.8 |
| GPT-5.4 | Chronos | **89.7** | 81.9 | **87.1** | 75.0 |
| GPT-5.4 | Codex CLI | **93.1** | 75.9 | 55.2 | **67.2** |
| Gemini 3.1 Pro | Chronos | **91.4** | 82.8 | **79.3** | 76.7 |
| Gemini 3.1 Pro | Gemini CLI | **81.9** | 75.0 | 81.0 | **82.8** |
| Gemini 3.1 Flash-Lite | Chronos | **86.2** | 62.9 | **85.3** | 72.4 |
| Gemini 3.1 Flash-Lite | Gemini CLI | **87.1** | 67.2 | 68.1 | **74.1** |

**Key findings:**

- With **inline delivery**: lexical search (grep) uniformly stronger than dense retrieval for every harness–model pair
  - Largest margin: Chronos + Gemini 3.1 Flash-Lite (86.2% vs. 62.9%)
  - Narrowest: Claude Code + Claude Opus 4.6 (76.7% vs. 75.0%)
  - On Chronos, inline grep spans 83.6–93.1%; inline vector spans 62.9–83.6%
- **Harness effect**: Same Claude Opus 4.6 backbone reaches 93.1% under Chronos but only 76.7% under Claude Code — changing the harness shifts the ceiling by roughly as much as swapping retrievers within a fixed harness
- **Programmatic delivery reshuffles** the comparison: programmatic vector exceeds programmatic grep on 5 of 10 harness–model pairs
  - Sharpest regression: Codex + GPT-5.4 falls from 93.1% (inline grep) to 55.2% (programmatic grep)

#### 4.1.4. Discussion

**LongMemEval rewards recovering literal witnesses** (exact dates, counts, preferences, spans). Lexical tools surface those strings without an embedding bottleneck, explaining why inline grep is a strong default.

**"Retrieval mode" is not measured in isolation**: The harness shapes the system prompt, tool descriptions, and how hits are rendered back into chat — all influence how the model schedules queries and decides when to stop. "Retrieval" in Table 1 is really **retrieval-plus-orchestration**.

**Programmatic delivery** changes the task from "read the tool message" to "locate, open, and integrate an artifact." When that second stage is brittle, accuracy collapses independently of retrieval quality. Agent papers should report both retrieval mechanics and the delivery path, because **file-based routing is itself a tool-use stress test**.

**Failure mode asymmetry:**
- Grep = deliberately narrow: rewards high-precision patterns, punishes vocabulary mismatch
- Dense = deliberately broad: surfaces paraphrases but elevates semantically "near" distractors

**Weaker models** (Claude Haiku 4.5 on Claude Code) show especially large inline grep–vector gaps. Hypothesis: weaker models are less consistent at iterative query refinement and reranker-aware reading, hurting dense retrieval more than pattern-triggered lexical recovery when evidence is literally present. **"Default to vector" recommendations should be conditioned on backbone strength** and whether the task rewards literal span recovery vs. conceptual blending.

---

### 4.2. Experiment 2: Context Scaling with Increasing Noise

**Goal**: Examine how lexical and dense retrieval diverge as the model is exposed to more sessions from the same per-question bundle. Long-memory QA interleaves oracle sessions with distractors — as session limit increases, both retrievers see additional irrelevant material.

#### 4.2.2. Experimental Setup

Vary the per-question session limit across: **s5, s10, s20, s30, full** (where full = complete haystack of 39–66 sessions per item). Oracle sessions always retained; remaining slots filled with distractors sampled from other sessions in the same bundle.

#### 4.2.3. Results

**Table 2**: Experiment 2 (grep-only) — accuracy (%) by session-limit configuration.

| Model | Harness | s5 | s10 | s20 | s30 | full |
|-------|---------|-----|------|------|------|------|
| Claude Opus 4.6 | Chronos | 89.3 | 89.7 | 90.5 | 85.3 | 89.7 |
| Claude Opus 4.6 | Claude Code | 91.4 | 94.0 | **95.7** | 90.5 | 94.0 |
| Claude Haiku 4.5 | Chronos | 83.7 | 84.5 | **86.2** | 85.3 | 83.6 |
| Claude Haiku 4.5 | Claude Code | **89.7** | 87.1 | 83.6 | 80.2 | 81.9 |
| GPT-5.4 | Chronos | **83.2** | 82.8 | 81.9 | 78.5 | 78.5 |
| Gemini 3.1 Pro | Chronos | 86.2 | 86.6 | **87.4** | 82.2 | 86.6 |
| Gemini 3.1 Pro | Gemini CLI | 78.1 | 78.5 | **79.2** | 74.7 | 78.5 |
| Gemini 3.1 Flash-Lite | Chronos | 88.8 | 89.2 | **90.0** | 84.8 | 89.2 |
| Gemini 3.1 Flash-Lite | Gemini CLI | 70.4 | 70.7 | **71.3** | 67.2 | 70.7 |

**Table 3**: Experiment 2 (vector-only) — accuracy (%) by session-limit configuration.

| Model | Harness | s5 | s10 | s20 | s30 | full |
|-------|---------|-----|------|------|------|------|
| Claude Opus 4.6 | Chronos | 94.0 | **94.8** | 92.2 | 84.5 | 92.2 |
| Claude Opus 4.6 | Claude Code | 77.6 | 72.4 | 75.0 | **78.4** | 72.4 |
| Claude Haiku 4.5 | Chronos | 87.9 | **89.7** | **90.5** | 87.1 | 87.9 |
| Claude Haiku 4.5 | Claude Code | 50.0 | 47.4 | 50.9 | 48.3 | 44.0 |
| GPT-5.4 | Chronos | 88.8 | **94.0** | 86.2 | 82.8 | 82.8 |
| Gemini 3.1 Pro | Chronos | **92.2** | 91.4 | 87.1 | 85.3 | 84.5 |
| Gemini 3.1 Pro | Gemini CLI | 84.5 | 83.6 | 82.8 | 85.3 | **89.7** |
| Gemini 3.1 Flash-Lite | Chronos | **88.8** | **88.8** | 87.9 | **88.8** | 83.6 |
| Gemini 3.1 Flash-Lite | Gemini CLI | 69.8 | 69.8 | **76.7** | 70.7 | 74.1 |

**Key findings:**

- **Grep accuracy is not monotone**: Chronos Opus rises to 90.5% at s20, dips to 85.3% at s30, then reaches 89.7% at full
- At s5, Chronos **vector** (87.9–94.0%) outperforms Chronos **grep** (83.2–89.7%) — vector is stronger at low session counts
- **Retriever ordering depends on harness**: Claude Code favors grep for Opus/Haiku at every configuration; Gemini CLI Pro favors vector throughout; Chronos shows crossings
- Claude Code Opus peaks at s20 (95.7% grep) — highest single result in Table 2

#### 4.2.4. Discussion

A common intuition holds that lexical search suffices on small corpora but breaks at scale. Our study **partially supports this** — vector retrieval often stronger at low session counts — but reveals the **crossover depends on harness and backbone**, not corpus size alone.

**Useful abstraction:**
- Dense retrieval explores **neighborhoods in embedding space**: recovers indirect mentions but admits topical false friends as sessions accumulate
- Lexical retrieval exploits **surface cues**: brittle to phrasing, yet when the agent discovers a discriminative pattern it can be ruthlessly precise

**Persistent stable preferences by harness:**
- Claude Code: favors grep for Opus/Haiku at every configuration
- Gemini CLI Pro: favors vector throughout, gap widening to 89.7% vs. 78.5% at full

These **vendor-stable patterns imply stable inductive biases** introduced by provider tooling: default hints, stdout chunking into transcript, tool error surfaces, and cultural defaults in how the CLI agent phrases searches. Migration between CLI stacks is **not retrieval-interchangeable** even when the on-disk corpus is byte-identical.

**Scaling curves should be read as samples from a stochastic outer loop** (distractors are redrawn when session limit changes), not as smooth capacity laws. Mid-grid peaks need not indicate "30 sessions is easier than 20" in any absolute sense.

---

## 5. Limitations

Conclusions are tied to **long-memory conversational QA**: questions grounded in multi-session chat, explicit time expressions, and personal/user facts. In domains where evidence is rarely literal (scientific synthesis over paraphrased abstracts, visual-heavy documents, code semantics), dense retrieval and hybrid routing may look different. **The paper does not claim that grep "beats" vector in general** — only that it can win end-to-end under the task distribution and corpora studied.

---

## 6. Conclusion

Key findings:
1. **Inline grep exceeds inline vector for every harness-model pair** evaluated on LongMemEval-S
2. **Overall scores depend strongly on harness and tool-calling style** — file-based delivery and provider CLI shells can invert or erase the lexical advantage without any change to the corpus
3. **Harness-level accuracy shifts** are comparable in magnitude to swapping retrievers within a fixed harness — "retrieval" is really retrieval-plus-orchestration

**Implication**: Retrieval mechanics, harness orchestration, and delivery path must be treated as a **single jointly-evaluated system** rather than independent design choices.

**Future work**: hybrid retrieval policies, non-chat corpora, broader vendor coverage.

---

## Appendix A: Per-Category Accuracy

**Table 4**: Per-category accuracy (%) on 116-question subset for Chronos harness (grep-only, inline, full haystack). Grader: GPT-4o.

Categories: KU = knowledge-update, MS = multi-session, SS-A = single-session-assistant, SS-P = single-session-preference, SS-U = single-session-user, TR = temporal-reasoning.

| Model | KU | MS | SS-A | SS-P | SS-U | TR |
|-------|----|----|------|------|------|-----|
| Claude Opus 4.6 | 94.4 | 83.9 | **100.0** | **100.0** | 87.5 | 87.1 |
| Claude Haiku 4.5 | 83.3 | 71.0 | **100.0** | 85.7 | 87.5 | 87.1 |
| GPT-5.4 | 77.8 | 74.2 | 92.3 | 85.7 | **93.8** | 67.7 |
| Gemini 3.1 Pro | 88.8 | 69.3 | **100.0** | 85.7 | 81.3 | **100.0** |
| Gemini 3.1 Flash-Lite | **94.3** | 72.6 | **100.0** | **100.0** | 81.3 | **100.0** |

Notable: All models achieve 100% on SS-A (single-session-assistant) under Chronos + grep except GPT-5.4 (92.3%). Multi-session (MS) is the hardest category across all models.

---

## Key References

- Wu et al. (2025): LongMemEval benchmark
- Sen et al. (2026): Chronos — temporal-aware conversational agents (arXiv:2603.16862)
- Gao et al. (2024): RAG survey (arXiv:2312.10997)
- Thakur et al. (2021): BEIR benchmark
- Liu et al. (2024): Lost in the Middle — context rot in long contexts
- Packer et al. (2023): MemGPT — file-based memory management
- Yao et al. (2023): ReAct — reasoning + acting paradigm
- Karpukhin et al. (2020): Dense Passage Retrieval (DPR)
- Formal et al. (2021): SPLADE v2
- Lumer et al. (2025a): Tool and agent selection survey
- Gulati et al. (2026): RRF for spreadsheet understanding (arXiv:2601.08741)
