---
title: "Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval for Long-Term Memory"
arxiv_id: 2603.16862
authors: "Sahil Sen, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah"
fetched: 2026-05-26
published: 2026-03-17
source: "https://arxiv.org/abs/2603.16862"
source_tier: P
---

# Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval for Long-Term Memory

**Authors**: Sahil Sen, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah (Commercial Technology and Innovation Office, PricewaterhouseCoopers U.S.)
**Published**: March 2026
**Source**: https://arxiv.org/abs/2603.16862
**arXiv ID**: 2603.16862
**Categories**: cs.CL

---

## Abstract

Recent advances in Large Language Models (LLMs) have enabled conversational AI agents to engage in extended multi-turn interactions spanning weeks or months. However, existing memory systems struggle to reason over temporally grounded facts and preferences that evolve across months of interaction and lack effective retrieval strategies for multi-hop, time-sensitive queries over long dialogue histories. We introduce Chronos, a novel temporal-aware memory framework that decomposes raw dialogue into subject-verb-object event tuples with resolved datetime ranges and entity aliases, indexing them in a structured event calendar alongside a turn calendar that preserves full conversational context. At query time, Chronos applies dynamic prompting to generate tailored retrieval guidance for each question, directing the agent on what to retrieve, how to filter across time ranges, and how to approach multi-hop reasoning through an iterative tool-calling loop over both calendars. We evaluate Chronos with 8 LLMs, both open-source and closed-source, on the LongMemEvalS benchmark comprising 500 questions spanning six categories of dialogue history tasks. Chronos Low achieves 92.60% and Chronos High scores 95.60% accuracy, setting a new state of the art with an improvement of 7.67% over the best prior system. Ablation results reveal the events calendar accounts for a 58.9% gain on the baseline while all other components yield improvements between 15.5% and 22.3%. Notably, Chronos Low alone surpasses prior approaches evaluated under their strongest model configurations.

---

## Core Thesis

Chronos achieves state-of-the-art conversational long-term memory by combining selective temporal event extraction (SVO tuples with ISO 8601 datetime ranges) with raw turn preservation and dynamic per-query retrieval guidance — avoiding both the overhead of comprehensive knowledge graphs and the temporal blindness of pure turn-level retrieval. The key insight is that structuring only temporally-grounded events while retaining full dialogue context is sufficient for accurate update tracking, preference recall, and relative date reasoning across months of interaction.

---

## 1. Introduction

The rapid progress of LLMs has enabled conversational AI agents to maintain contextual awareness across extended multi-turn interactions, supporting personalized assistance over weeks or months of conversation history. With breakthroughs in RAG for conversational memory, LLM agents can efficiently access historical information without exhausting context window limits.

Despite these advancements, conversational memory systems have struggled to find the right balance between structured knowledge building and retrieval simplicity:

- **Knowledge graph systems** extract all facts and relationships at ingestion time, building elaborate structures with entity resolution, fact validation, and temporal metadata — but create large knowledge bases even when queries require only a subset of information.
- **Turn-level retrieval approaches** avoid this overhead through direct dense-sparse hybrid search, but lack structured temporal representations needed for time-sensitive queries involving date calculations or cross-session event aggregation.
- **Background reasoning pipelines** generate derived facts, timelines, and behavioral patterns through offline "dreaming" or observational analysis, but these query-independent deductions introduce context entropy when precomputed knowledge proves irrelevant to specific questions.

The core challenge: comprehensive memory building introduces overhead and context entropy through over-structuring, while pure turn-level retrieval lacks temporal grounding. No existing approach achieves query-conditioned selective extraction — structuring only the temporal information relevant to answering specific questions while preserving conversational context for semantic understanding.

Chronos addresses this by performing targeted event extraction focused on temporally-grounded state transitions and timestamped occurrences, indexed alongside raw conversation turns. To the authors' knowledge, Chronos is the first architecture that combines the simplicity of turn-level retrieval with selective temporal event extraction.

---

## 2. Related Work

### 2.1 Long-Term Conversational Memory

Modern LLM context windows largely address short-term (within-session) memory. Long-term (across-session) memory presents a harder challenge: retaining and retrieving information from conversations that occurred days or months earlier.

Two primary benchmarks evaluate long-term memory capabilities:
- **LongMemEvalS**: 500 questions across six categories, including knowledge-update tracking, multi-session aggregation, and temporal reasoning.
- **LoCoMo**: Memory over naturalistic human conversations spanning up to 35 sessions, measuring single-hop, multi-hop, temporal, and adversarial QA.

Neither benchmark isolates the role of temporal structuring in long-term memory.

### 2.2 Knowledge Accumulation and Representations

Representations fall along a spectrum from structured to unstructured:
- **Structured end**: Knowledge graphs encode entities and relationships as typed edges. Graph-based systems allow logical retrieval. More complex systems integrate three or more different types of nodes.
- **Unstructured end**: Systems preserve raw conversational text or generate natural language summaries. Some deploy specialized agents that monitor conversations and produce timestamped annotations. Others organize memory into hierarchical tiers.
- **Hybrid approaches**: Maintain both raw dialogue and extracted atomic facts as parallel corpora.

A key tension: knowledge accumulation typically proceeds at ingestion time, independent of any future query. No existing scheme targets only temporally grounded events for structured indexing while retaining raw dialogue for general semantic queries.

### 2.3 Retrieval-Augmented Architectures

- **Sparse retrieval** (BM25): Excels at exact lexical matching, computationally efficient, but misses semantic variations.
- **Dense retrieval**: Captures semantic similarity but struggles with precise term matching and rare entities.
- **Hybrid approaches** fusing both modalities (reciprocal rank fusion or learned reranking) have emerged as the dominant paradigm in RAG systems.

Pre-retrieval query processing techniques well-established in document retrieval — query rewriting, hypothetical document embeddings (HyDE), query decomposition — have not been applied to conversational long-term memory, where questions span categories demanding fundamentally different retrieval strategies.

**Agentic RAG** transforms retrieval from single-shot to multi-step reasoning, but existing systems lack query-conditioned adaptation of the retrieval strategy itself.

### 2.4 Summarization and Fact Extraction

- **Summarization**: Recursive summarization, EDU extraction rewriting sessions into event-like statements.
- **Fact extraction**: Atomic knowledge units (entity-relation triples, timestamped observations). Most systems extract at ingestion time; query-conditioned variants additionally extract from retrieved turns at inference time.

No existing system selectively structures only temporal events while preserving raw dialogue for semantic retrieval.

---

## 3. The Chronos Architecture

Chronos maintains two complementary calendars:
1. **Event calendar**: Extracted temporal events with structured datetime ranges.
2. **Turn calendar**: Raw conversational exchanges.

Four main components:

### 3.1 Event Extraction

The pipeline identifies temporally-grounded occurrences using LLM-powered extraction. Given a conversation turn with timestamp `t_conv`, the extractor identifies events with all of `⟨subject, verb, object⟩`.

**Multi-resolution temporal normalization** converts natural language time references into precise ISO 8601 datetime ranges. Each event receives both `start_datetime` and `end_datetime` capturing the full temporal span. For ambiguous expressions like "recently" or "last month," the system computes appropriate temporal windows centered on or relative to `t_conv` with appropriate granularity.

**Alias generation**: The system generates 2-4 lexical aliases per event using completely different vocabulary to improve text search recall. For example, "bought Fitbit" generates aliases like "picked up a fitness tracker," "got a step counter," and "purchased a wearable."

**Batch processing**: Turns are processed in batches of maximum 25 turns, with 5-turn overlap between chunks.

Events are embedded using `text-embedding-3-large` and uploaded to the event calendar index; raw turns are embedded and uploaded to the turn calendar index.

### 3.2 Dynamic Prompting

Chronos introduces dynamic prompting for long-term memory, extending query rewriting from document retrieval to conversational memory. Rather than reformulating the search query itself, dynamic prompting analyzes each question to generate retrieval guidance tailored to the agent's reasoning process.

Given user query `q`, the system generates a custom instruction preamble directing the agent's attention to relevant information dimensions and retrieval strategies. A template generator (using Gemini 3 Flash) extracts question targets (entities, attributes, temporal constraints, operations) and outputs 1-5 concrete bullets describing what information to retrieve.

Example: Given "What camera lens did I buy most recently?", the generator outputs: "Pay close attention to the following information (current and past): Details about camera lens purchases, specifically the most recent purchase and the lens type/model."

Static prompts cannot anticipate the diversity of long-term memory queries: temporal filtering ("What did I do last March?"), preference recall ("What kind of coffee do I like?"), cross-session aggregation ("How many times did I exercise?").

### 3.3 Initial Retrieval

Three-stage pipeline:
1. **Dense vector search**: Query the turn calendar for top-100 conversation exchanges based on cosine similarity between `v_q` and `v_t`.
2. **Cross-encoder reranking**: Cohere Rerank v3 rescores the 100 candidates; top-15 are selected.
3. **Context expansion**: Each of the 15 selected turns is expanded with one turn before and one turn after from the same session.

Retrieved turns are formatted into hierarchical natural language context blocks organized by conversation date (e.g., "Session 1 (2024-02-15)") to make temporal relationships explicit.

### 3.4 Chronos Agent

An LLM agent with native tool-calling capabilities for iterative memory retrieval. Tools:
- `search_turns`, `search_events`: Vector search for semantic retrieval.
- `grep_turns`, `grep_events`: Exact keyword matching for specific entities or exact phrases.

The agent follows a **ReAct reasoning pattern**, alternating between thought generation, tool calling, and observation processing. Tool calls execute asynchronously with automatic retry logic. The agent can select top-k to retrieve; reranking from k=100 is applied using the original question (not the agent's query).

### 3.5 Benchmark Notes

Evaluation uses LongMemEvalS's LLM judge. Manual inspection reveals benchmark limitations: some ground truth answers are inconsistent with the conversation history, and LLM-as-judge variability affects scoring on open-ended preference questions.

---

## 4. Experiments

Evaluation against state-of-the-art systems: EmergenceMem Internal, Honcho, Mastra, and Zep.

Two configurations:
- **Chronos Low**: GPT-4o as generation model (matches all compared systems).
- **Chronos High**: Claude Opus 4.6 (higher capability tier).

All runs use `text-embedding-3-large` with temperature = 0.

### 4.2 Results

**Table 1: Chronos Low vs. baselines on LongMemEvalS (500 questions)**

| Method | Overall | KU | MS | SSA | SSP | SSU | TR |
|--------|---------|----|----|-----|-----|-----|-----|
| **Chronos Low (Ours)** | **92.60** | **96.15** | **91.73** | **100.00** | 80.00 | **94.29** | **90.23** |
| Honcho† | 90.40 | 94.87 | 84.96 | 96.43 | **90.00** | **94.29** | 88.72 |
| EmergenceMem Internal | 86.00 | 83.33 | 81.20 | **100.00** | 60.00 | **98.57** | 85.71 |
| Mastra | 84.80 | 85.90 | 79.70 | 82.14 | 73.33 | **98.57** | 85.71 |
| Supermemory | 81.60 | 88.50 | 71.40 | 96.40 | 70.00 | 97.10 | 76.70 |
| Hindsight‡ | 83.60 | 84.60 | 79.70 | 94.60 | 66.70 | 95.70 | 79.70 |
| Zep | 71.20 | 83.30 | 57.90 | 80.40 | 56.70 | 92.90 | 62.40 |
| Full-context | 60.20 | 78.20 | 44.30 | 94.60 | 20.00 | 81.40 | 45.10 |

† Honcho evaluated on Claude Haiku 4.5, not GPT-4o.  
‡ Hindsight evaluated with OSS-20B actor and OSS-120B judge.

**Table 2: Advanced LLM configurations on LongMemEvalS**

| Method | Overall | KU | MS | SSA | SSP | SSU | TR |
|--------|---------|----|----|-----|-----|-----|-----|
| **Chronos High (Ours)** | **95.60** | **100.00** | 88.72 | **100.00** | **100.00** | **98.57** | **95.50** |
| Mastra | 92.80 | 94.90 | **87.20** | 96.40 | 90.00 | 97.10 | 94.00 |
| Honcho† | 92.60 | — | — | — | — | — | — |
| Hindsight‡ | 91.40 | 94.90 | 87.20 | 96.40 | 80.00 | 97.10 | 91.00 |
| Supermemory | 85.20 | 89.70 | 76.70 | 98.20 | 70.00 | 98.60 | 82.00 |

Categories: KU = Knowledge Update, MS = Multi-Session Aggregation, SSA = Single-Session Assistant, SSP = Single-Session Preference, SSU = Single-Session User, TR = Temporal Reasoning.

### 4.3 Discussion

- **Multi-session aggregation** ("How many times did I exercise in May?"): Calendar-structured event index enables efficient temporal filtering, reducing retrieval entropy to time-based events only.
- **Temporal reasoning** ("What did I do the week after my vacation?"): Multi-resolution temporal normalization converts relative expressions into precise date ranges, shifting reasoning from string interpretation to structured filtering.
- **Knowledge-update tracking** ("Where do I currently work?"): Event extraction identifies each workplace mention as a separate timestamped event; agent retrieves all and selects most recent by datetime ordering.
- **Single-session preference** (SSP: 80%): Only category where Chronos Low trails Honcho (90%). Honcho's advantage reflects use of Claude Haiku 4.5, not an architectural advantage.

Error analysis (Figure 3): Moving from Chronos Low to Chronos High halves counting/arithmetic errors. Retrieval failures remain the most common error category for both models, showing LLMs still fail to retrieve over large amounts of data even with specific guidance. No improvement on fabrication errors (frequent on abstention questions).

### 4.4 Ablation Studies

Ablations on a stratified 116-question subset (Table 3):

**Chronos Low ablations:**

| Ablation | Overall | KU | MS | SSA | SSP | SSU | TR |
|----------|---------|----|----|-----|-----|-----|-----|
| **Chronos (full)** | **93.1** | 94.4 | **90.3** | **100.0** | 85.7 | 87.5 | **96.8** |
| No Initial Retrieval | 76.7 | 83.3 | 64.5 | **100.0** | 71.4 | 81.2 | 74.2 |
| No Dynamic Prompting | 78.4 | 83.3 | 77.4 | **100.0** | 42.9 | **93.8** | 67.7 |
| No Rerank | 81.0 | 77.8 | 74.2 | **100.0** | 85.7 | 87.5 | 77.4 |
| No Date Filter | 78.4 | 88.9 | 71.0 | **100.0** | 57.1 | 68.8 | 80.6 |
| Grep Only (no vector) | 77.6 | **100.0** | 64.5 | 53.8 | **100.0** | 87.5 | 77.4 |
| Vector Only (no grep) | 80.2 | 94.4 | 80.6 | **100.0** | 85.7 | 62.5 | 71.0 |
| **Turns Only (no events)** | **58.6** | 55.6 | 51.6 | **100.0** | 42.9 | 43.8 | 61.3 |

**Chronos High ablations:**

| Ablation | Overall | KU | MS | SSA | SSP | SSU | TR |
|----------|---------|----|----|-----|-----|-----|-----|
| **Chronos (full)** | **94.8** | **100.0** | **90.3** | **100.0** | **100.0** | **93.8** | 93.5 |
| No Initial Retrieval | 91.4 | **100.0** | 80.6 | **100.0** | 85.7 | **93.8** | 93.5 |
| No Dynamic Prompting | 94.8 | **100.0** | 87.1 | **100.0** | **100.0** | **93.8** | **96.8** |
| No Rerank | 92.2 | **100.0** | 87.1 | **100.0** | 85.7 | 87.5 | 93.5 |
| No Date Filter | 92.2 | 94.4 | 83.9 | **100.0** | 85.7 | **93.8** | **96.8** |
| Grep Only (no vector) | 87.1 | 94.4 | 83.9 | 61.5 | **100.0** | **93.8** | 90.3 |
| Vector Only (no grep) | 83.6 | **100.0** | 80.6 | **100.0** | 85.7 | 62.5 | 80.6 |
| **Turns Only (no events)** | 92.2 | 94.4 | 87.1 | **100.0** | 85.7 | 87.5 | **96.8** |

Key findings:
- For Chronos Low: removing event access drops performance by **34.5 points** (93.1 → 58.6).
- For Chronos High: removing event access only drops **2.6 points** (94.8 → 92.2) — more capable models partially compensate.
- Dynamic prompting has no effect under Chronos High, reflecting advanced models' ability to distinguish between query types without explicit guidance.
- Both grep and vector search are necessary: removing either causes significant drops.

---

## 5. Limitations

1. **Dual indexing storage**: Maintaining separate vector indexes for turns and events increases storage vs. turn-only systems. Mitigated by sparse event extraction focusing only on temporally-grounded state transitions.
2. **Offline extraction cost**: LLM-powered event extraction adds indexing computation. Mitigated through batched processing (25 turns/batch, 5-turn overlap) with efficient small models.
3. **Inference complexity**: Parallel retrieval over both calendars at query time. Mitigated through pre-retrieval of turn context before agent reasoning begins.

---

## 6. Conclusion

Chronos introduces a date-aware memory framework with dual calendars (event calendar + turn calendar), combined with turn-level dense retrieval, text search, and query-conditioned dynamic prompting. Multi-resolution temporal handling: preserves explicit dates exactly, calculates relative references from conversation timestamps, resolves ambiguous expressions to appropriate time ranges.

Results on LongMemEvalS (500 questions):
- Chronos Low (GPT-4o): 92.60% (+7.67% relative over prior SOTA)
- Chronos High (Claude Opus 4.6): 95.60% (+3.02% relative over prior records)

Particularly strong on multi-session aggregation (91.73%) and temporal reasoning (90.23%).

Key conclusion: Persistent conversational agents do not require comprehensive knowledge graph construction for high-fidelity long-horizon memory. Structuring fine-grained temporal events while preserving full dialogue context is sufficient for accurate update tracking, preference recall, and relative date reasoning.

Future directions: learning from accumulated event traces (weight updates), shared event histories for multi-agent or multi-user interactions.

---

## Appendix A: Full Model Comparison on LongMemEvalS

**Table 4: All 8 LLMs evaluated with Chronos (500 questions)**

| Model | Overall | KU (78) | MS (133) | SSA (56) | SSP (30) | SSU (70) | TR (133) |
|-------|---------|---------|---------|---------|---------|---------|---------|
| Claude Opus 4.6 | **95.60** | **100.00** | 88.72 | **100.00** | **100.00** | 98.57 | 95.49 |
| GPT-5-mini | 94.20 | 96.15 | 85.71 | 98.21 | **100.00** | 97.14 | **96.99** |
| Claude Sonnet 4.5 | 94.20 | 98.72 | **89.47** | **100.00** | 93.33 | **98.57** | 91.73 |
| Claude Haiku 4.5 | 94.00 | 96.15 | 88.72 | **100.00** | 90.00 | 97.14 | 94.74 |
| GPT-5.2 | 93.80 | 97.44 | 83.46 | **100.00** | **100.00** | **98.57** | 95.49 |
| GPT-4o | 92.60 | 96.15 | 91.73 | **100.00** | 80.00 | 94.29 | 90.23 |
| Claude Code Sonnet | 88.60 | 93.59 | 79.70 | 94.64 | 80.00 | 94.29 | 90.98 |

---

## Key References

- Wu et al. (2025a) — **LongMemEvalS benchmark**: arXiv:2410.10813
- Haley et al. (2025) — **EmergenceMem**: SOTA on LongMemEval with RAG (emergence.ai blog)
- Barnes (2026) — **Mastra Observational Memory**: 95% on LongMemEval (mastra.ai/research)
- McCormick & Leer (2025) — **Honcho benchmarking**: plasticlabs.ai blog
- Rasmussen et al. (2025) — **Zep temporal knowledge graph**: arXiv:2501.13956
- Yao et al. (2023) — **ReAct**: arXiv:2210.03629
- Ma et al. (2023) — **Query rewriting for RAG**: arXiv:2305.14283
- Gao et al. (2022) — **HyDE (Hypothetical Document Embeddings)**: arXiv:2212.10496
- Gao et al. (2024) — **RAG survey**: arXiv:2312.10997
- Lumer & Sen (2025) — **Toolshed: RAG-tool fusion for agent tool selection** (ICAART)
- Asai et al. (2023) — **Self-RAG**: arXiv:2310.11511
- Packer et al. (2024) — **MemGPT**: arXiv:2310.08560
- Maharana et al. (2024) — **LoCoMo benchmark**: arXiv:2402.17753
- Karpukhin et al. (2020) — **DPR**: arXiv:2004.04906
- Robertson & Zaragoza (2009) — **BM25**: Foundations and Trends in IR
- Du et al. (2025) — **MemR³**: arXiv:2512.20237
- Edge et al. (2025) — **GraphRAG**: arXiv:2404.16130
- Wang et al. (2025) — **Recursive summarization for dialogue**: arXiv:2308.15022
