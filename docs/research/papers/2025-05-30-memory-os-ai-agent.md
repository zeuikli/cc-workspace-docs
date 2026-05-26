---
title: "Memory OS of AI Agent"
authors: "Jiazheng Kang, Mingming Ji, Zhe Zhao, Ting Bai"
published: "2025-05-30"
source: "https://arxiv.org/abs/2506.06326"
---

# Memory OS of AI Agent

**Authors**: Jiazheng Kang¹, Mingming Ji², Zhe Zhao², Ting Bai¹* (corresponding)  
**Institutions**: ¹Beijing University of Posts and Telecommunications (BUPT); ²Tencent AI Lab  
**Published**: May 30, 2025 (arXiv:2506.06326v1)  
**Source**: https://arxiv.org/abs/2506.06326  
**GitHub**: https://github.com/BAI-LAB/MemoryOS

## Abstract

Large Language Models (LLMs) face a crucial challenge from fixed context windows and inadequate memory management, leading to a severe shortage of long-term memory capabilities and limited personalization in the interactive experience with AI agents. To overcome this challenge, we innovatively propose a Memory Operating System, i.e., MemoryOS, to achieve comprehensive and efficient memory management for AI agents. Inspired by the memory management principles in operating systems, MemoryOS designs a hierarchical storage architecture and consists of four key modules: Memory Storage, Updating, Retrieval, and Generation. Specifically, the architecture comprises three levels of storage units: short-term memory, mid-term memory, and long-term personal memory. Key operations within MemoryOS include dynamic updates between storage units: short-term to mid-term updates follow a dialogue-chain-based FIFO principle, while mid-term to long-term updates use a segmented page organization strategy. Our pioneering MemoryOS enables hierarchical memory integration and dynamic updating. Extensive experiments on the LoCoMo benchmark show an average improvement of 49.11% on F1 and 46.18% on BLEU-1 over the baselines on GPT-4o-mini, showing contextual coherence and personalized memory retention in long conversations. The implementation code is open-sourced at https://github.com/BAI-LAB/MemoryOS.

---

## 1 Introduction

Large Language Models (LLMs) demonstrate impressive capabilities in text comprehension and generation, but face inherent limitations in sustaining dialogue coherence due to their reliance on fixed-length contextual windows for memory management. This fixed-length design inherently struggles to preserve continuity in dialogues with significant temporal gaps, often resulting in disjointed memory that manifests as factual inconsistencies and reduced personalization. Long-term memory coherence is critical in scenarios requiring persistent user adaptation, multi-session knowledge retention, or stable persona representation across extended interactions, where the limitations of fixed-length memory management in default LLMs become particularly acute, constituting a significant open challenge in the field.

To address this challenge, current memory mechanisms in default LLMs can be broadly categorized into three methodological types:

1. **Knowledge-organization methods** (Xu et al., 2025; Liu et al., 2023), such as A-Mem structure memory into interconnected semantic networks or notes to enable adaptive management and flexible retrieval
2. **Retrieval mechanism-oriented approaches** (Huang et al., 2024; Zhong et al., 2024; Li et al., 2024), e.g., MemoryBank integrates semantic retrieval with a memory forgetting curve mechanism to allow long-term memory updating
3. **Architecture-driven methods** (Packer et al., 2023; Chhikara et al., 2025), such as MemGPT use hierarchical structures with explicit read and write operations to dynamically manage context

Although these diverse strategies typically operate in isolation, i.e., each focusing on single dimensions such as storage structure, retrieval mechanism, or update strategies, no unified operating system has been proposed to enable systematic and comprehensive memory management for AI agents.

Inspired by memory management principles in operating systems, we pioneer the proposal of a comprehensive memory operating system, termed **MemoryOS**. MemoryOS comprises four core functional modules: memory Storage, Updating, Retrieval, and Generation. Through their coordinated collaboration, the system establishes a unified memory management framework encompassing hierarchical storage, dynamic updating, adaptive retrieval, and contextual generation.

**Specifically:**
- **Memory Storage** organizes information into short-term, mid-term, and long-term storage units
- **Memory Updating** dynamically refreshes via a segmented paging architecture based on the dialogue-chain and heat-based mechanisms
- **Memory Retrieval** leverages semantic segmentation to query these tiers
- **Response Generation** integrates retrieved memory information to generate coherent and personalized responses

**Primary contributions:**
- First innovative attempt to introduce a systematic operating system (MemoryOS) for memory management, empowering AI agents with long-term conversational coherence and user persona persistence
- Pioneering three-tier hierarchical memory storage architecture integrating four core functional modules (storage, updating, retrieval, and generation)
- Comprehensive experiments validating effectiveness and efficiency on LoCoMo and GVD benchmarks

---

## 2 Related Work

### 2.1 Memory for LLM Agents

Advancements in memory systems of LLMs can be grouped into three categories:

**Knowledge-organization methods** focus on capturing and structuring intermediate reasoning states:
- **Think-in-Memory (TiM)** (Liu et al., 2023): stores evolving chains-of-thought, enabling consistency through continual updates
- **A-Mem** (Xu et al., 2025): organizes knowledge into an interconnected note network spanning sessions
- **Grounded Memory** (Ocker et al., 2025): integrates vision-language models for perception, knowledge graphs for structured memory representation

**Retrieval mechanism-oriented approaches** enrich the model with an external memory library:
- **MemoryBank** (Zhong et al., 2024): logs conversations, events, and user traits in a vector database; refreshes using a forgetting-curve schedule
- **AI-town** (Park et al., 2023): keeps memories in natural language and adds a reflection loop for relevance filtering
- **EmotionalRAG** (Huang et al., 2024): retrieves memory entries combining semantic similarity with agent's current emotional state

**Architecture-driven designs** alter the core control flow to manage context explicitly:
- **MemGPT** (Packer et al., 2023): OS-like hierarchy with dedicated read/write calls
- **Self-Controlled Memory (SCM)** (Wang et al., 2025): dual buffers and a memory controller that gates selective recall

### 2.2 Memory Management in OS

Modern operating systems use combined segment-page memory management to balance logical structure with efficient physical utilization. Classic approaches like **Multics** (Bensoussan et al., 1972) organize memory into segments divided into pages, supporting efficient management, protection, and sharing. Segment metadata (size, access permissions) prevents external fragmentation, while paging reduces internal fragmentation (Denning, 1970). Advanced OS use priority-based eviction (e.g., LRU, working-set models) to maintain hot data, and combining coarse-grained segmentation with fine-grained paging minimizes overhead on many-core processors (Zheng et al., 2020).

MemoryOS applies these principles by structuring memory into logical segments (conversation topics) subdivided into pages, using heat-based prioritization to retain relevant content and efficiently discard or archive less-accessed information.

---

## 3 MemoryOS

### 3.1 Overview Architecture

MemoryOS consists of four modules: memory storage, update, retrieval, and generation.

- **Memory Storage**: Three-tier hierarchical structure — Short-Term Memory (STM) for timely conversations, Mid-Term Memory (MTM) for recurring topic summaries, Long-term Personal Memory (LPM) for user/agent preferences
- **Memory Updating**: STM-to-MTM updates via dialogue-chain FIFO; MTM-to-LPM updates using segmented page strategy with heat-based replacement
- **Memory Retrieval**: Two-tiered approach in MTM — semantic relevance identifies segments first, then retrieves pertinent dialogue pages; combines LPM persona attributes and STM context
- **Response Generation**: Integrates retrieval outcomes from STM, MTM, and LPM into a coherent prompt

### 3.2 Memory Storage Module

#### Short-Term Memory (STM)

Stores real-time conversation data in units called **dialogue pages**. Each page:

```
page_i = {Q_i, R_i, T_i}
```

where Q_i = user query, R_i = model response, T_i = timestamp.

A **dialogue chain** is constructed for each page to maintain contextual information:

```
page^chain_i = {Q_i, R_i, T_i, meta^chain_i}
```

where meta^chain_i is generated by an LLM in two steps:
1. Evaluating a new page's contextual relevance to prior pages to determine chain linkage (or resetting to current page if semantically discontinuous)
2. Summarizing all chain pages into meta^chain_i

#### Mid-Term Memory (MTM)

Adopts a **Segmented Paging storage architecture** inspired by OS memory management. Dialogue pages with the same topic are grouped into segments:

```
segment_i = {page_i | F_score(page_i, segment_i) > θ}
```

The segment content is summarized by an LLM based on related dialogue pages. F_score measures similarity between a dialogue page and a segment:

```
F_score = cos(e_s, e_p) + F_Jacard(K_s, K_p)
```

where:
- e_s, e_p = embedding vectors of segment and dialogue page
- K_s, K_p = keyword sets summarized by LLMs in segment and page
- F_Jacard = Jaccard similarity = |K_s ∩ K_p| / |K_s ∪ K_p|
- θ = similarity threshold (set to 0.6)

Pages exceeding threshold θ are merged into the same segment, ensuring topic coherence.

#### Long-term Persona Memory (LPM)

Ensures both user and assistant maintain persistent memory of important personal details. Two components:

**User Persona:**
- **Static**: fixed attributes (gender, name, birth year)
- **User Knowledge Base (User KB)**: dynamically stores factual information extracted from past interactions
- **User Traits**: evolving interests, habits, and preferences (90 dimensions across three categories: basic needs/personality, AI alignment dimensions, content platform interest tags)

**Agent Persona:**
- **Agent Profile**: fixed settings (role, character traits)
- **Agent Traits**: dynamic attributes developed through interactions (recommended items, interaction history)

### 3.3 Memory Update Module

#### STM-MTM Update

STM stores dialogue pages in a **FIFO queue with fixed length (7)**. When STM reaches maximum capacity, the oldest dialogue page is transferred to MTM.

#### MTM-LPM Update

MTM updates use the **Heat score** of segments:

```
Heat = α · N_visit + β · L_interaction + γ · R_recency
```

Where:
- N_visit = number of times the segment has been retrieved
- L_interaction = total number of dialogue pages within the segment
- R_recency = time decay coefficient:

```
R_recency = exp(-Δt / μ)
```

where Δt = time elapsed since last access (in seconds), μ = time constant (1e+7)

Parameters: α = β = γ = 1 (equal weighting)

**MTM capacity**: maximum 200 segments. When exceeded, segments with lowest heat are evicted.

**MTM-to-LPM promotion**: segments with heat exceeding threshold τ = 5 are transferred to LPM. After transfer, L_interaction is reset to zero, causing the heat score to decline (preventing redundancy).

#### LPM Update

Promoted segments update:
- **User Traits**: 90 dimensions extracted and updated by LLMs
- **User KB**: factual information about the user (max 100 entries, FIFO)
- **Agent Traits**: factual information about the agent (max 100 entries, FIFO)

### 3.4 Memory Retrieval Module

```
F_Retrieval(STM, MTM, LPM | Q)
```

**STM Retrieval**: All dialogue pages retrieved (most recent context).

**MTM Retrieval** (two-stage):
1. Segment selection via matching score — top-m = 5 candidate segments
2. Page selection — top-k most relevant dialogue pages within segments (k=5 for GVD, k=10 for LoCoMo)
After retrieval, N_visit and R_recency are updated.

**LPM Retrieval**: User KB and Agent Traits each retrieve top-10 entries with highest semantic relevance. All User Profile, Agent Profile, and User Traits are used.

### 3.5 Response Generation Module

Final prompt integrates:
- STM: recent dialogue context
- MTM: relevant conversation pages and summaries
- LPM: persona information (user traits, user KB, agent traits, profiles)

This ensures responses remain contextually coherent, draw on historical dialogue, and align with user/assistant identities.

---

## 4 Experiments

### 4.1 Experimental Settings

**Datasets:**

- **GVD dataset** (Zhong et al., 2024): multi-turn dialogues simulated from interactions between 15 virtual users and an assistant over a 10-day period, covering at least two topics per day
- **LoCoMo benchmark** (Maharana et al., 2024): ultra-long dialogues averaging 300 turns and ~9K tokens per conversation; four question types: Single-hop, Multi-hop, Temporal, Open-domain

**Evaluation Metrics:**

GVD:
- **Memory Retrieval Accuracy (Acc.)**: binary (0 or 1)
- **Response Correctness (Corr.)**: three-point scale (0, 0.5, 1)
- **Contextual Coherence (Cohe.)**: three-point scale (0, 0.5, 1)
- Auto-scored by DeepSeek-R1

LoCoMo: **F1** and **BLEU-1**

**Baselines:**
- TiM (Think-in-Memory): stores reasoning outcomes instead of raw dialogues; uses LSH for retrieval
- MemoryBank: Ebbinghaus Forgetting Curve–based memory strength adjustment; user portrait
- MemGPT: dual-tier OS-like memory with main context + external context
- A-Mem (Agentic Memory): structured notes forming interconnected knowledge networks

**Hardware**: 8×H20 GPUs

**Hyperparameters:**
| Parameter | Value |
|-----------|-------|
| STM queue length | 7 |
| MTM max segments | 200 |
| User KB / Agent Traits capacity | 100 |
| Heat threshold τ (MTM→LPM) | 5 |
| α, β, γ weights | 1, 1, 1 |
| Top-m segments | 5 |
| Top-k pages (GVD / LoCoMo) | 5 / 10 |
| Similarity threshold θ | 0.6 |
| Time constant μ | 1e+7 |

### 4.2 Main Results

**Table 1: Comparison results on the GVD dataset**

| Model | Method | Acc. ↑ | Corr. ↑ | Cohe. ↑ |
|-------|--------|--------|--------|--------|
| GPT-4o-mini | TiM | 84.5 | 78.8 | 90.8 |
| | MemoryBank | 78.4 | 73.3 | 91.2 |
| | MemGPT | 87.9 | 83.2 | 89.6 |
| | A-Mem | 90.4 | 86.5 | 91.4 |
| | **Ours** | **93.3** | **91.2** | **92.3** |
| | Improvement | +3.2% | +5.4% | +1.0% |
| Qwen2.5-7B | TiM | 82.2 | 73.2 | 85.5 |
| | MemoryBank | 76.3 | 70.3 | 82.7 |
| | MemGPT | 85.1 | 80.2 | 86.9 |
| | A-Mem | 87.2 | 79.5 | 87.8 |
| | **Ours** | **91.8** | **82.3** | **90.5** |
| | Improvement | +5.3% | +3.5% | +3.1% |

**Table 2: LoCoMo dataset comparison (F1 / BLEU-1)**

| Model | Method | Single Hop F1 | Single Hop BLEU-1 | Multi Hop F1 | Multi Hop BLEU-1 | Temporal F1 | Temporal BLEU-1 | Open Domain F1 | Open Domain BLEU-1 | Avg Rank (F1) |
|-------|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-4o-mini | TiM | 16.25 | 13.12 | 18.43 | 17.35 | 8.35 | 7.32 | 23.74 | 22.05 | 3.8 |
| | MemoryBank | 5.00 | 4.77 | 9.68 | 6.99 | 5.56 | 5.94 | 6.61 | 5.16 | 5.0 |
| | MemGPT | 26.65 | 17.72 | 25.52 | 19.44 | 9.15 | 7.44 | 41.04 | 34.34 | 2.2 |
| | A-Mem | 27.02 | 20.09 | 45.85 | 36.67 | 12.14 | 12.00 | 44.65 | 37.06 | — |
| | A-Mem* | 22.61 | 15.25 | 33.23 | 29.11 | 8.04 | 7.81 | 34.13 | 27.73 | 3.0 |
| | **Ours** | **35.27** | **25.22** | **41.15** | **30.76** | **20.02** | **16.52** | **48.62** | **42.99** | **1.0** |
| | Improvement | +32.35% | +42.33% | +23.83% | +5.67% | +118.80% | +111.52% | +18.47% | +25.19% | — |
| Qwen2.5-3B | TiM | 4.37 | 5.01 | 2.54 | 3.21 | 6.20 | 5.37 | 6.35 | 7.34 | 4.3 |
| | MemoryBank | 3.60 | 3.39 | 1.72 | 1.97 | 6.63 | 6.58 | 4.11 | 3.32 | 4.8 |
| | MemGPT | 5.07 | 4.31 | 2.94 | 2.95 | 7.04 | 7.10 | 7.26 | 5.52 | 2.8 |
| | A-Mem | 12.57 | 9.01 | 27.59 | 25.07 | 7.12 | 7.28 | 17.23 | 13.12 | — |
| | A-Mem* | 10.31 | 8.76 | 16.31 | 11.07 | 6.94 | 7.31 | 12.34 | 10.62 | 2.3 |
| | **Ours** | **23.26** | **15.39** | **21.44** | **14.95** | **10.18** | **8.18** | **26.23** | **22.39** | **1.0** |
| | Improvement | +125.61% | +75.68% | +31.45% | +35.05% | +46.69% | +11.90% | +112.56% | +110.83% | — |

*Note: A-Mem refers to results reported in original paper. A-Mem* = our implementation under same experimental environment.*

**Table 3: Efficiency analysis on LoCoMo benchmark**

| Method | Tokens | Avg. Calls | Avg. F1 |
|--------|:------:|:----------:|:-------:|
| MemoryBank | 432 | 3.0 | 6.84 |
| TiM | 1,274 | 2.6 | 18.01 |
| MemGPT | 16,977 | 4.3 | 29.13 |
| A-Mem* | 2,712 | 13.0 | 26.55 |
| **Ours** | **3,874** | **4.9** | **36.23** |

MemoryOS requires significantly fewer LLM calls than A-Mem* (4.9 vs. 13) and much lower token consumption than MemGPT (3,874 vs. 16,977) — a **77.2% reduction**.

**Key observations:**

1. MemoryBank performs worst — simple memory decay mechanisms insufficient for effective conversational memory management
2. TiM outperforms MemoryBank by saving "thoughts" rather than raw turns, but single-stage hash retrieval cannot preserve cross-topic dependencies
3. MemGPT's flat FIFO queue causes topic mixing as dialogue length grows; A-Mem's heavy multi-step link generation inflates latency and error accumulation
4. MemoryOS fuses hierarchical STM/MTM/LPM via segmented paging + heat-based eviction + persona module, ensuring topic-aligned content remains accessible while maintaining user preference consistency
5. Most pronounced advantage on LoCoMo Temporal category: **+118.80% F1** — suggesting heat-based eviction specifically helps preserve time-distant but important memories

### 4.3 Ablation Study

Individual removal of three key components:
- **-MTM**: removing Mid-Term Memory
- **-LPM**: removing Long-term Persona Module
- **-Chain**: removing Dialogue page Chain
- **-MemoryOS**: removing the entire memory system

**Results**: MTM has the most significant impact, followed by LPM, with Chain having least impact. Without MemoryOS, model performance drastically reduces.

### 4.4 Hyperparameter Analysis

Impact of top-k retrieved dialogue pages from MTM, with k ∈ {5, 10, 20, 30, 40} on LoCoMo benchmark.

**Finding**: Performance improves as k increases, but improvements diminish when exceeding a threshold. Excessive content introduces noise, adversely affecting performance. **k = 10** achieves favorable performance while minimizing computational overhead.

### 4.5 Case Study

Demonstrates conversational memory enhancement across multiple weeks:

**Conversation history** (week 1):
- User: "I went to the wetland park last week, and the scenery there was beautiful."
- User: "There were many little squirrels running in the trees—they were very cute."
- User: "I ran two laps in the park and felt great. I'll keep working out to get slimmer."

**A few weeks later:**
- User: "I feel like eating a burger—do you have any recommendations?"

**Without MemoryOS**: Generic burger recommendation (Teriyaki chicken burger, cheeseburger)

**With MemoryOS**: "The cheeseburger[...], just don't forget you're hitting the gym!"

MemoryOS recalls details like "seeing the scenery, running, and spotting squirrels in the wetland park" from weeks ago via mid-term memory's segment-page storage + dialogue page chain, and leverages the personalization module to proactively remind the user of their fitness goals.

---

## 5 Conclusion

Inspired by memory management mechanisms in operating systems, MemoryOS pioneers a novel memory management system for AI agents. Implemented via a hierarchical memory storage architecture, MemoryOS addresses the fixed context window limitations in long conversations. By adapting OS-style segment-paging storage for dialogue history, MemoryOS enables efficient memory storage, updating, and semantic retrieval using heat-driven eviction to dynamically prioritize critical information across memory tiers. The integrated persona module captures evolving user preferences via personalized trait extraction, ensuring responses align with long conversation contexts. Comprehensive experiments demonstrate MemoryOS's superiority: **+49.11% F1, +46.18% BLEU-1** on LoCoMo (GPT-4o-mini), with **77.2% token reduction** vs MemGPT.

---

## References

André Bensoussan, C. T. Clingen, and R. C. Daley. 1972. The multics virtual memory: Concepts and design. *Communications of the ACM*, 15(5):308–318.

Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. 2025. Mem0: Building production-ready AI agents with scalable long-term memory. *arXiv:2504.19413*.

DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, et al. 2025. Deepseek-r1: Incentivizing reasoning capability in LLMs via reinforcement learning. *arXiv:2501.12948*.

Peter J. Denning. 1970. Virtual memory. *ACM Computing Surveys*, 2(3):153–189.

Yiming Du, Wenyu Huang, Danna Zheng, et al. 2025. Rethinking memory in AI: Taxonomy, operations, topics, and future directions. *arXiv:2505.00675*.

Le Huang, Hengzhi Lan, Zijun Sun, Chuan Shi, and Ting Bai. 2024. Emotional RAG: Enhancing role-playing agents through emotional retrieval. In *IEEE ICKG 2024*, pages 120–127.

Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xiang Wang, and Tat-Seng Chua. 2024. Hello again! LLM-powered personalized agent for long-term dialogue. *arXiv:2406.05925*.

Jia-Nan Li, Jian Guan, Songhao Wu, Wei Wu, and Rui Yan. 2025. From 1,000,000 users to every user: Scaling up personalized preference for user-level alignment. *arXiv:2503.15463*.

Lei Liu, Xiaoyan Yang, Yue Shen, Binbin Hu, Zhiqiang Zhang, Jinjie Gu, and Guannan Zhang. 2023. Think-in-memory: Recalling and post-thinking enable LLMs with long-term memory. *arXiv:2311.08719*.

Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and Yuwei Fang. 2024. Evaluating very long-term conversational memory of LLM agents. In *ACL 2024*, pages 13851–13870.

Felix Ocker, Jörg Deigmöller, Pavel Smirnov, and Julian Eggert. 2025. A grounded memory system for smart personal assistants. *arXiv:2505.06328*.

Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, and Joseph E. Gonzalez. 2023. MemGPT: Towards LLMs as operating systems. *arXiv:2307.08691*.

Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. BLEU: a method for automatic evaluation of machine translation. In *ACL 2002*, pages 311–318.

Joon Sung Park, Joseph O'Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023. Generative agents: Interactive simulacra of human behavior. In *UIST 2023*, pages 1–22.

Bing Wang, Xinnian Liang, Jian Yang, Hui Huang, Shengzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, and Zhoujun Li. 2025. SCM: Enhancing large language model with self-controlled memory framework. *arXiv:2304.13343*.

Yaxiong Wu, Sheng Liang, Chen Zhang, et al. 2025. From human memory to AI memory: A survey on memory mechanisms in the era of LLMs. *arXiv:2504.15965*.

Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Jungfeng Zhang. 2025. A-Mem: Agentic memory for LLM agents. *arXiv:2502.12110*.

Peiwen Yuan, Xinglin Wang, Shaoxiong Feng, et al. 2024. Generative dense retrieval: Memory can be a burden. In *EACL 2024*.

Zeyu Zhang, Xiaohe Bo, Chen Ma, et al. 2024. A survey on the memory mechanism of large language model-based agents. *arXiv:2404.13501*.

Yan Zheng, Tong Zou, and Xingyan Wang. 2020. Segment-page-combined memory management technology based on a homegrown many-core processor. *CCF Transactions on High Performance Computing*, 2(4):376–381.

Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. 2024. MemoryBank: Enhancing large language models with long-term memory. In *AAAI 2024*, volume 38, pages 19724–19731.

---

**Keywords**: AI agent memory, long-term memory management, hierarchical storage, heat-based eviction, LLM personalization, LoCoMo, MemoryOS, operating system analogy, segmented paging
