---
title: "MemGPT: Towards LLMs as Operating Systems"
arxiv_id: 2310.08560
authors: "Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez"
fetched: 2026-05-26
published: 2023-10-12
source: "https://arxiv.org/abs/2310.08560"
source_tier: P
---

# MemGPT: Towards LLMs as Operating Systems

**Authors**: Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez
**Published**: October 2023
**Source**: https://arxiv.org/abs/2310.08560
**arXiv ID**: 2310.08560
**Categories**: cs.AI

---

## Abstract

Large language models (LLMs) have revolutionized AI, but are constrained by limited context windows, hindering their utility in tasks requiring extended interactions or long document processing. Operating systems solved the problem of managing limited physical memory through hierarchical storage and virtual memory abstractions. Inspired by this, the authors propose MemGPT — a system that intelligently manages different memory tiers in order to effectively provide extended context within the LLM's limited context window, and utilizes interrupts to manage control flow between itself and the user. MemGPT knows when to push critical information to a vector database and when to retrieve it, enabling perpetual context for the model. The authors evaluate MemGPT in two domains requiring long-context: document analysis, where MemGPT outperforms the fixed context baselines on tasks that require processing multiple large documents, and multi-session chat, where MemGPT enables conversational agents that remember, reflect, and evolve dynamically through long-term interactions with their users.

---

## Core Thesis

LLM context windows can be treated as "main memory" (RAM) in an OS analogy, with external storage serving as disk — and by implementing virtual context management with LLM-directed memory operations, systems can overcome fixed context limits without requiring architectural changes to the underlying model. The key insight is that LLMs can autonomously manage their own memory hierarchy via function calls, deciding what to store, retrieve, and evict, in a manner analogous to how an OS manages page faults and memory swaps.

---

## Introduction and Motivation

Modern LLMs such as GPT-4 and Claude are limited by fixed-length context windows. This fundamental constraint prevents their use in:

- **Extended conversations**: Agents cannot recall details from earlier in a long dialogue or across multiple sessions.
- **Long document analysis**: Documents longer than the context window cannot be processed holistically.
- **Persistent knowledge accumulation**: Agents cannot learn and adapt from ongoing user interactions.

While some models have extended context windows (32K, 100K tokens), these remain finite and incur quadratic attention costs. The authors argue that the solution lies not in scaling context length, but in intelligent memory management — drawing a direct analogy to how operating systems handle the gap between RAM (fast, limited) and disk (slow, vast).

---

## Technical Architecture

### Memory Hierarchy Design

MemGPT implements a two-tier memory architecture:

**Main Context** (analogous to RAM):
- Corresponds to the LLM's active prompt tokens
- Contains: system instructions, working context, and a FIFO message queue
- Fixed-size, directly accessible to the LLM

**External Context** (analogous to disk):
- **Recall Storage**: A searchable database of prior conversation history, supporting semantic search and exact lookup
- **Archival Storage**: Unlimited long-term storage for documents, facts, and arbitrary data, indexed via vector embeddings

### Key Components

**Working Context**: A fixed-size read/write block of unstructured text within the main context. Stores persistent facts, user preferences, and agent persona information. The LLM can directly read and write this block via function calls.

**Queue Manager (FIFO Message Buffer)**: Manages the flow of messages in and out of the active context window. Implements eviction policies — when the message buffer fills, older messages are evicted to recall storage. Also supports recursive summarization when messages exceed capacity thresholds.

**Function Executor**: Parses and executes LLM output as structured function calls. Enables autonomous memory operations (search, insert, update) without user intervention. The LLM's "inner monologue" (hidden from users) drives these operations.

**Function Chaining**: A special mechanism allowing the LLM to signal that it requires another inference step before returning to the user. This enables multi-hop retrieval sequences — e.g., look up a key, find a pointer, follow the pointer — without user interaction at each step.

### Control Flow and Interrupts

MemGPT distinguishes two types of system events:

- **User interrupts**: Messages arriving from the human user, pausing the agent's current operation
- **Heartbeat interrupts**: Timer-based signals allowing the agent to perform background memory maintenance (summarization, consolidation) during idle periods

The agent decides whether to "yield" back to the user or to chain another function call internally, enabling autonomous multi-step reasoning.

---

## Experimental Evaluation

### 1. Multi-Session Conversational Agents

**Dataset**: An augmented version of Multi-Session Chat (MSC), where two agents converse across five sessions with deliberate callbacks to earlier sessions.

#### Deep Memory Retrieval (DMR) Task

Tests whether an agent can correctly answer questions about events from prior conversation sessions. The agent must retrieve relevant memories from external storage.

| Model | Accuracy | ROUGE-L |
|-------|----------|---------|
| GPT-3.5 Turbo (fixed context) | 38.7% | 0.394 |
| GPT-3.5 Turbo + MemGPT | 66.9% | 0.629 |
| GPT-4 (fixed context) | 32.1% | 0.296 |
| GPT-4 + MemGPT | **92.5%** | **0.814** |

Key finding: MemGPT with GPT-4 achieves 92.5% accuracy, nearly tripling the baseline. Interestingly, GPT-4 alone performs worse than GPT-3.5 alone on this task, suggesting the base model's tendency to "hallucinate" retrieved memories when none are present.

#### Conversation Opener Task

Evaluates whether conversation-opening messages reference specific knowledge accumulated about the user. MemGPT-generated openers perform similarly to or occasionally exceed hand-written human openers, demonstrating effective long-term user modeling.

### 2. Document Analysis

**Dataset**: NaturalQuestions-Open, with varying numbers of retrieved Wikipedia documents included as context.

#### Multi-Document Question-Answering

Baseline models degrade when document count exceeds available context. MemGPT maintains consistent performance by managing document ingestion and retrieval autonomously.

#### Nested Key-Value Retrieval (Novel Benchmark)

A synthetic multi-hop lookup task requiring the agent to follow chains of key-value pairs across a large external corpus. Nesting depth measures the number of sequential lookups required.

| Model | Max Nesting Depth Before Failure |
|-------|----------------------------------|
| GPT-3.5 Turbo (fixed context) | 0 (fails at depth 1) |
| GPT-4 (fixed context) | 2 (fails at depth 3) |
| GPT-3.5 + MemGPT | 1 |
| GPT-4 + MemGPT | All depths (no failure) |

Key finding: Only GPT-4 + MemGPT successfully handles arbitrary nesting depth via function chaining, demonstrating the value of multi-step autonomous retrieval.

---

## Key Findings

1. **Memory management dramatically improves long-term consistency**: MemGPT enables agents to maintain coherence across extended dialogues by selectively storing and retrieving historical context, with accuracy improvements of 28–60 percentage points over fixed-context baselines.

2. **Function chaining is essential for multi-hop reasoning**: Without the ability to chain multiple retrieval steps internally, complex lookup tasks fail. The OS interrupt model enables this autonomously.

3. **Underlying model quality sets the ceiling**: MemGPT's benefit is amplified with stronger base models. GPT-4 + MemGPT substantially outperforms GPT-3.5 + MemGPT, particularly on tasks requiring judgment about what to retrieve and when.

4. **Scalability without architectural change**: Performance remains stable as document counts grow, contrasting with degradation in fixed-context baselines. MemGPT achieves unbounded effective context via software, not hardware.

5. **Recursive summarization prevents information loss**: When message buffers fill, MemGPT compresses older context into summaries stored in recall storage, preserving key information at reduced token cost.

---

## Related Work

**Long-context LLMs**: Prior work extends context via sparse attention (Longformer, BigBird), positional interpolation (ALiBi, RoPE extensions), and recurrent mechanisms. MemGPT is complementary — it works with any fixed-context LLM without retraining.

**Retrieval-Augmented Generation (RAG)**: Systems like REALM, RAG, and Atlas augment generation with retrieved passages. MemGPT extends this paradigm by making the LLM an active participant in retrieval decisions rather than a passive consumer.

**LLMs as Agents**: ReAct, Toolformer, and related work equip LLMs with tool use. MemGPT specializes this toward memory management, treating memory operations as first-class tools.

**Memory-Augmented Neural Networks**: NTM, LSTM-based external memory, and memory networks explored programmatic memory access. MemGPT applies similar principles to large-scale autoregressive transformers.

---

## Limitations and Discussion

- **Latency**: Function chaining introduces additional inference calls, increasing latency per user interaction.
- **Model dependency**: Weak models (e.g., GPT-3.5) struggle to use function chaining correctly, reducing MemGPT's benefit at lower capability tiers.
- **Memory coherence**: External storage can accumulate stale or contradictory facts; the current system lacks explicit memory consolidation or conflict resolution.
- **Context pollution**: Inner monologue and function call overhead consume context tokens, reducing space available for actual content.

---

## Conclusion

MemGPT demonstrates that OS-inspired hierarchical memory management can unlock the potential of LLMs even when constrained by fixed context lengths. By treating the LLM as both the processor and the memory manager — capable of issuing its own "memory syscalls" — the system achieves unbounded effective context for tasks in document analysis and multi-session conversation. The authors argue this positions future LLM systems closer to general-purpose operating systems for cognitive tasks, with MemGPT as a step toward "LLMs as operating systems."

Code, datasets, and 20M Wikipedia article embeddings are available at https://research.memgpt.ai.

---

## Key References

- Brown et al. (2020). Language models are few-shot learners. (GPT-3)
- OpenAI (2023). GPT-4 Technical Report.
- Touvron et al. (2023). LLaMA 2: Open Foundation and Fine-Tuned Chat Models.
- Xu et al. (2021). Beyond Goldfish Memory: Long-Term Open-Domain Conversation. (MSC dataset)
- Kwiatkowski et al. (2019). Natural Questions: a Benchmark for Question Answering Research. (NaturalQuestions)
- Lewis et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
- Yao et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models.
- Schick et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools.
- Beltagy et al. (2020). Longformer: The Long-Document Transformer.
- Press et al. (2022). Train Short, Test Long: Attention with Linear Biases (ALiBi).
