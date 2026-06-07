---
title: "Retrieval-Augmented Generation for Large Language Models: A Survey"
arxiv_id: 2312.10997
authors: "Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, Haofen Wang"
fetched: 2026-05-26
published: 2023-12-18
source: "https://arxiv.org/abs/2312.10997"
source_tier: P
---

# Retrieval-Augmented Generation for Large Language Models: A Survey

**Authors**: Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, Haofen Wang
**Published**: December 2023
**Source**: https://arxiv.org/abs/2312.10997
**arXiv ID**: 2312.10997
**Categories**: cs.CL (Computation and Language); cs.AI (Artificial Intelligence)

---

## Abstract

Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

**Index Terms**: Large language model, retrieval-augmented generation, natural language processing, information retrieval

---

## Core Thesis

RAG is the most practical solution for grounding LLMs in current, verifiable knowledge without the cost of retraining. The paper organizes the field around three evolutionary paradigms (Naive → Advanced → Modular RAG), dissects retrieval/generation/augmentation as the tripartite technical foundation, and proposes a standardized evaluation framework covering 26 tasks and ~50 datasets.

---

## I. Introduction

Large language models (LLMs) have achieved remarkable success, though they still face significant limitations, especially in domain-specific or knowledge-intensive tasks, notably producing "hallucinations" when handling queries beyond their training data or requiring current information. To overcome challenges, Retrieval-Augmented Generation (RAG) enhances LLMs by retrieving relevant document chunks from external knowledge base through semantic similarity calculation. By referencing external knowledge, RAG effectively reduces the problem of generating factually incorrect content.

RAG technology has rapidly developed in recent years. The development trajectory of RAG in the era of large models exhibits several distinct stage characteristics:

1. **Pre-ChatGPT era**: RAG's inception coincided with the rise of the Transformer architecture, focusing on enhancing language models by incorporating additional knowledge through Pre-Training Models (PTM).
2. **Post-ChatGPT era**: RAG research shifted towards providing better information for LLMs to answer more complex and knowledge-intensive tasks during the inference stage.
3. **Fine-tuning integration**: Enhancement of RAG began to incorporate more with LLM fine-tuning techniques.

**Contributions of this paper**:
- Thorough and systematic review of state-of-the-art RAG methods, delineating evolution through Naive RAG, Advanced RAG, and Modular RAG paradigms.
- Identification and discussion of central technologies integral to the RAG process: "Retrieval", "Generation" and "Augmentation".
- Summary of current assessment methods covering 26 tasks, nearly 50 datasets, outlining evaluation objectives and metrics, as well as benchmarks and tools.

---

## II. Overview of RAG

A typical RAG application consists of 3 steps:
1. **Indexing**: Documents are split into chunks, encoded into vectors, and stored in a vector database.
2. **Retrieval**: Retrieve the Top-k chunks most relevant to the question based on semantic similarity.
3. **Generation**: Input the original question and the retrieved chunks together into LLM to generate the final answer.

### II-A. Naive RAG

The Naive RAG follows a traditional "Retrieve-Read" framework:

- **Indexing**: Raw data (PDF, HTML, Word, Markdown) is cleaned, converted to plain text, segmented into chunks, encoded into vector representations, and stored in a vector database.
- **Retrieval**: The query is transformed into a vector; top-K most similar chunks are retrieved.
- **Generation**: Query and selected documents are synthesized into a coherent prompt for the LLM.

**Drawbacks of Naive RAG**:
- *Retrieval Challenges*: Struggles with precision and recall, leading to misaligned or irrelevant chunks and missing crucial information.
- *Generation Difficulties*: Hallucination, irrelevance, toxicity, or bias in outputs.
- *Augmentation Hurdles*: Disjointed outputs, redundancy from multiple sources, over-reliance on augmented information.

### II-B. Advanced RAG

Advanced RAG introduces improvements to overcome Naive RAG limitations, focusing on retrieval quality via pre-retrieval and post-retrieval strategies.

**Pre-retrieval process**:
- Optimizing indexing: enhancing data granularity, optimizing index structures, adding metadata, alignment optimization, mixed retrieval.
- Query optimization: query rewriting, query transformation, query expansion.

**Post-retrieval process**:
- Re-ranking retrieved information to relocate most relevant content to the edges of the prompt.
- Context compression to mitigate information overload and dilution of key details.

### II-C. Modular RAG

Modular RAG advances beyond the former two paradigms, offering enhanced adaptability and versatility. It incorporates diverse strategies for improving components, supports both sequential processing and integrated end-to-end training.

**New Modules**:
- *Search module*: Direct searches across various data sources (search engines, databases, knowledge graphs) using LLM-generated code and query languages.
- *RAG-Fusion*: Multi-query strategy expanding user queries into diverse perspectives, with parallel vector searches and intelligent re-ranking.
- *Memory module*: Leverages LLM's memory to guide retrieval, creating an unbounded memory pool via iterative self-enhancement.
- *Routing*: Navigates through diverse data sources, selecting the optimal pathway.
- *Predict module*: Reduces redundancy and noise by generating context directly through the LLM.
- *Task Adapter*: Tailors RAG to various downstream tasks, automating prompt retrieval for zero-shot inputs.

**New Patterns**:
- Rewrite-Retrieve-Read: LLM refines retrieval queries through a rewriting module.
- Generate-Read: Replaces traditional retrieval with LLM-generated content.
- Recite-Read: Emphasizes retrieval from model weights.
- Demonstrate-Search-Predict (DSP): Dynamic use of module outputs to bolster another module's functionality.
- ITER-RETGEN: Iterative Retrieve-Read-Retrieve-Read flow.
- FLARE and Self-RAG: Adaptive retrieval evaluating necessity of retrieval based on different scenarios.

### II-D. RAG vs. Fine-Tuning

| Dimension | Prompt Engineering | RAG | Fine-Tuning |
|---|---|---|---|
| External Knowledge | Low | High | Low–Medium |
| Model Adaptation | Low | Low–Medium | High |
| Knowledge Updates | Static | Real-time | Requires retraining |
| Interpretability | High | High | Low |
| Hallucination Reduction | Limited | Strong | Moderate |
| Latency | Low | Higher | Low (after training) |

Key finding: RAG consistently outperforms unsupervised fine-tuning for both existing knowledge encountered during training and entirely new knowledge. RAG and FT are complementary and can be combined for optimal performance.

---

## III. Retrieval

### III-A. Retrieval Source

**Data Structures**:

- *Unstructured Data* (text): Most widely used; primary sources include Wikipedia Dumps (HotpotQA, DPR), cross-lingual text, and domain-specific data (medical, legal).
- *Semi-structured data* (PDF): Challenges include text splitting separating tables and complications for semantic similarity searches. Approaches: Text-2-SQL queries via LLM code capabilities, or transforming tables to text.
- *Structured data* (Knowledge Graphs): More precise, verified information. KnowledGPT generates KB search queries. G-Retriever integrates GNNs + LLMs + RAG with PCST optimization for targeted graph retrieval.
- *LLMs-Generated Content*: SKR classifies questions as known/unknown and applies retrieval selectively. GenRead replaces the retriever with an LLM generator. Selfmem iteratively creates an unbounded memory pool.

**Retrieval Granularity** (fine to coarse): Token → Phrase → Sentence → Proposition → Chunks → Document. DenseX proposed propositions as retrieval units—atomic expressions encapsulating unique factual segments in concise, self-contained format. For KGs: Entity → Triplet → Sub-Graph.

### III-B. Indexing Optimization

**Chunking Strategy**:
- Fixed token splits (100/256/512 tokens): Larger chunks = more context + more noise; smaller chunks = less noise + incomplete context.
- Recursive splits and sliding window methods for layered retrieval.
- Small2Big: sentences as retrieval unit, surrounding sentences provided as context to LLMs.

**Metadata Attachments**:
- Enrich chunks with page number, file name, author, category, timestamp.
- Time-aware RAG through timestamp weighting for knowledge freshness.
- Artificially constructed metadata: paragraph summaries, hypothetical questions (Reverse HyDE).

**Structural Index**:
- *Hierarchical index*: Parent-child file relationships with data summaries at each node for swift traversal.
- *Knowledge Graph index*: Maintains consistency, delineates connections between concepts/entities. KGP builds inter-document KG index with nodes (paragraphs/structures) and edges (semantic/lexical similarity or structural relationships).

### III-C. Query Optimization

**Query Expansion**:
- *Multi-Query*: Prompt engineering to expand queries via LLMs, executed in parallel.
- *Sub-Query*: Decompose complex questions into simpler sub-questions using least-to-most prompting.
- *Chain-of-Verification (CoVe)*: Expanded queries validated by LLM to reduce hallucinations.

**Query Transformation**:
- *Query Rewrite*: Prompt LLM to rewrite queries; specialized smaller models (RRR). Taobao's BEQUE enhanced recall for long-tail queries.
- *HyDE*: Construct hypothetical documents (assumed answers) to focus on answer-to-answer embedding similarity.
- *Step-back Prompting*: Abstract original query to generate high-level concept question; use both step-back and original queries for retrieval.

**Query Routing**:
- *Metadata Router/Filter*: Extract keywords from query, filter based on keywords and chunk metadata.
- *Semantic Router*: Route based on semantic similarity of query to routing options.

---

## IV. Generation

### IV-A. Post-Retrieval Process

Key challenge: integrating retrieved context effectively with the query without overwhelming the LLM.

**Reranking**: Reorder retrieved documents to prioritize the most relevant. Methods include rule-based (diversity, recency), model-based (BERT-series cross-encoders), and LLM-based reranking. Addresses the "lost in the middle" problem where LLMs focus on beginning/end of context.

**Context Selection/Compression**: Reduce irrelevant information in retrieved documents. Methods include:
- Token-level filtering (remove less informative tokens)
- Sentence-level compression (select most relevant sentences)
- Training dedicated compressor models (RECOMP: extractive or abstractive compression)
- Information Extraction (IE)-based approaches

### IV-B. LLM Fine-Tuning

Fine-tuning the generator improves alignment with retrieved context:

- **General Fine-tuning**: Standard supervised fine-tuning on RAG-specific data.
- **Distillation from Larger Models**: Train smaller models to mimic larger model RAG behavior.
- **Domain-Specific Fine-tuning**: Adapt LLM to specialized domains (medical, legal, code).
- **Alignment with Retrieval**: Fine-tune LLM to better utilize retrieved documents (RA-DIT jointly fine-tunes retriever and LLM with KL-divergence alignment).
- **Reinforcement Learning**: Use feedback to optimize generation quality in RAG context.

---

## V. Augmentation in RAG

### V-A. Augmentation Stages

RAG augmentation can occur at three stages of LLM development:

- **Pre-training Stage**: Incorporate retrieval during pre-training (RETRO, Atlas, REALM). Computationally expensive but produces deeply integrated retrieval-enhanced models.
- **Fine-tuning Stage**: Augment during fine-tuning process to adapt retrieval behavior to specific tasks.
- **Inference Stage**: Most flexible and widely adopted. No model retraining required; retrieval is applied at inference time.

### V-B. Augmentation Data Source

- **Unstructured data**: Text corpora, Wikipedia, domain-specific collections.
- **Structured data**: Knowledge Graphs, databases, tables.
- **LLM-generated data**: Self-generated context, hypothetical documents, reasoning chains.

### V-C. Augmentation Process

- **Once (Single retrieval)**: Retrieve once before generation. Simple but may miss complex multi-hop reasoning.
- **Iterative**: Multiple rounds of retrieval and generation (ITER-RETGEN, IRCoT). Better for complex multi-step queries.
- **Adaptive**: Decide when and whether to retrieve based on query complexity or confidence (FLARE, Self-RAG). Most efficient approach.
- **Recursive**: Hierarchical or tree-structured retrieval and reasoning (ToC, IRCoT).

---

## VI. RAG Evaluation

### VI-A. Downstream Tasks and Datasets

RAG is evaluated across 26 downstream tasks including:
- Question Answering (open-domain, multi-hop, conversational)
- Fact Verification
- Commonsense Reasoning
- Information Extraction / Slot Filling
- Dialogue Systems / Task-Oriented Dialogue
- Code Generation
- Summarization
- Machine Translation
- Recommendation

Key datasets include: Natural Questions, TriviaQA, HotpotQA, 2WikiMultiHopQA, MuSiQue, MS MARCO, FEVER, WoW (Wizard of Wikipedia), and domain-specific datasets.

### VI-B. Evaluation Metrics

**Retrieval Quality**:
- Recall@K, Precision@K, MRR (Mean Reciprocal Rank), NDCG (Normalized Discounted Cumulative Gain)
- Context Relevance: measures relevance of retrieved context to the query

**Generation Quality**:
- Faithfulness/Groundedness: whether generated answer is grounded in retrieved context
- Answer Relevance: relevance of answer to original question
- Correctness/Accuracy: factual accuracy
- Fluency and coherence
- ROUGE, BLEU, BERTScore for automated evaluation

### VI-C. Evaluation Benchmarks and Tools

- **RAGAS**: End-to-end RAG evaluation framework measuring faithfulness, answer relevance, context precision, and context recall.
- **ARES**: Automated RAG Evaluation System using LLM-as-judge approach.
- **TruLens**: Evaluation framework focusing on groundedness and relevance.
- **RGB (RAG Benchmark)**: Tests RAG systems on noise robustness, negative rejection, information integration, and counterfactual robustness.
- **RECALL**: Evaluates counterfactual robustness.

---

## VII. Challenges and Future Directions

### Current Challenges

**Retrieval Quality**:
- Long-context retrieval and processing
- Multi-modal retrieval (text + images + tables)
- Handling conflicting or noisy retrieved information
- Retrieval latency in production settings

**Generation Quality**:
- Balancing retrieved context with parametric knowledge
- Avoiding "lost in the middle" problem with long contexts
- Mitigating hallucination when retrieved context is incomplete or wrong

**Augmentation**:
- Determining optimal retrieval frequency (when to retrieve)
- Multi-hop and cross-document reasoning
- Maintaining coherence across iterative retrieval steps

**System-Level**:
- Lack of standardized evaluation benchmarks
- RAG robustness to noisy or adversarial retrieval results
- Efficiency and scalability in production
- Extending RAG beyond text to multi-modal settings

### Future Directions

1. **Long Context RAG**: Adapt to ever-increasing context windows while maintaining efficiency.
2. **Multi-Modal RAG**: Extend retrieval to images, audio, video, and structured data.
3. **RAG + Agent**: Integration with autonomous agents for multi-step, tool-using RAG.
4. **Knowledge Graph + RAG**: Deeper integration for more structured and verifiable retrieval.
5. **Adaptive and On-Demand RAG**: More sophisticated policies for when and how much to retrieve.
6. **RAG for Domain-Specific Applications**: Medical, legal, scientific, and enterprise settings.
7. **Scalable Evaluation**: Better automated evaluation frameworks that correlate with human judgment.
8. **Privacy-Preserving RAG**: Ensuring sensitive information in external databases is protected.

---

## Summary of RAG Methods (Selected from Table I)

| Method | Retrieval Source | Data Type | Granularity | Aug. Stage | Retrieval Process |
|---|---|---|---|---|---|
| CoG | Wikipedia | Text | Phrase | Pre-training | Iterative |
| DenseX | FactoidWiki | Text | Proposition | Inference | Once |
| Self-Mem | Dataset-base | Text | Sentence | Tuning | Iterative |
| FLARE | Search Engine, Wikipedia | Text | Sentence | Tuning | Adaptive |
| Atlas | Wikipedia, Common Crawl | Text | Chunk | Pre-training | Iterative |
| RETRO++ | Pre-training Corpus | Text | Chunk | Pre-training | Iterative |
| Self-RAG | Wikipedia | Text | Chunk | Tuning | Adaptive |
| ITER-RETGEN | Wikipedia | Text | Chunk | Inference | Iterative |
| IRCoT | Wikipedia | Text | Chunk | Inference | Recursive |
| RAPTOR | Dataset-base | Text | Chunk | Inference | Recursive |
| DSP | Wikipedia | Text | Doc | Inference | Iterative |
| HyDE | Various | Text | Doc | Inference | Once |
| SURGE | Freebase | KG | Sub-Graph | Tuning | Once |
| KnowledGPT | Dataset-base | KG | Triplet | Inference | Multi-time |
| RoG | Freebase | KG | Triplet | Inference | Iterative |
| G-Retriever | Dataset-base | TextGraph | Sub-Graph | Inference | Once |

---

## Key References

1. Lewis et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS. (Foundational RAG paper)
2. Guu et al. (2020). REALM: Retrieval-Augmented Language Model Pre-Training. ICML.
3. Borgeaud et al. (2022). Improving Language Models by Retrieving from Trillions of Tokens (RETRO). ICML.
4. Izacard & Grave (2021). Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering (FiD). EACL.
5. Asai et al. (2023). Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection.
6. Jiang et al. (2023). Active Retrieval Augmented Generation (FLARE).
7. Ma et al. (2023). Query Rewriting for Retrieval-Augmented Large Language Models (RRR).
8. Shi et al. (2023). REPLUG: Retrieval-Augmented Black-Box Language Models.
9. Khattab et al. (2022). Demonstrate-Search-Predict (DSP).
10. Gao et al. (2022). Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE).
11. Zheng et al. (2023). Step-Back Prompting.
12. Trivedi et al. (2022). Interleaving Retrieval with Chain-of-Thought Reasoning (IRCoT).
13. Yu et al. (2023). Generate rather than Retrieve (GenRead).
14. Shao et al. (2023). Enhancing Retrieval-Augmented Large Language Models with Iterative Retrieval-Generation (ITER-RETGEN).
15. Ram et al. (2023). In-Context Retrieval-Augmented Language Models (ICRALM).
16. Es et al. (2023). RAGAS: Automated Evaluation of Retrieval Augmented Generation.
17. GitHub repository: https://github.com/Tongji-KGLLM/RAG-Survey
