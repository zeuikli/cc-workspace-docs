---
url: "https://arxiv.org/abs/2504.07952"
title: "Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory"
date: 2025-04-10
arxiv_id: 2504.07952
authors: "Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou"
referenced_by: warmwater.dev
source: arxiv
---

## Abstract

Despite their impressive performance on complex tasks, current language models (LMs) typically operate in a vacuum: Each input query is processed separately, without retaining insights from previous attempts. Here, we present Dynamic Cheatsheet (DC), a lightweight framework that endows a black-box LM with a persistent, evolving memory. Rather than repeatedly re-discovering or re-committing the same solutions and mistakes, DC enables models to store and reuse accumulated strategies, code snippets, and general problem-solving insights at inference time. This test-time learning enhances performance substantially across a range of tasks without needing explicit ground-truth labels or human feedback. Leveraging DC, Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams once it began retaining algebraic insights across questions. Similarly, GPT-4o's success rate on Game of 24 increased from 10% to 99% after the model discovered and reused a Python-based solution. In tasks prone to arithmetic mistakes, such as balancing equations, DC enabled GPT-4o and Claude to reach near-perfect accuracy by recalling previously validated code, whereas their baselines stagnated around 50%. Beyond arithmetic challenges, DC yields notable accuracy gains on knowledge-demanding tasks. Claude achieved a 9% improvement in GPQA-Diamond and an 8% boost on MMLU-Pro problems. Crucially, DC's memory is self-curated, focusing on concise, transferable snippets rather than entire transcripts. Unlike finetuning or static retrieval methods, DC adapts LMs' problem-solving skills on the fly, without modifying their underlying parameters.

## 主要貢獻

- **核心框架 Dynamic Cheatsheet (DC)**：為黑盒 LLM 提供持久性、動態演化的外部記憶，在推論期間無需梯度更新即可實現測試時學習（test-time learning）。
- **兩種變體**：
  - **DC-Cu（Cumulative）**：生成答案後，由 Curator 模組決定是否將策略/code snippet 寫入記憶；依次累積擴充。
  - **DC-RS（Retrieval & Synthesis）**：在生成前先用餘弦相似度檢索最相關的歷史 input-output pair，更新記憶後再生成，兼具檢索與策略合成能力。
- **顯著效能提升**：
  - Claude 3.5 Sonnet 在 AIME 2024 從 23% -> 50%（+27%）；AIME 2025 +30%
  - GPT-4o 在 Game of 24 從 10% -> 99%（模型發現 Python 暴力解並重用）
  - Math Equation Balancer：GPT-4o 和 Claude 從 45–50% -> 98–100%
  - GPQA-Diamond：+9%；MMLU-Pro Engineering/Physics：+8%
- **自主記憶策略**：記憶由模型自我策展（self-curated），儲存精簡且可遷移的知識，不依賴 ground-truth labels 或人工標注，避免 context 膨脹。
- **局限**：小模型（GPT-4o-mini）受益有限，因本身產出高品質答案的能力不足，記憶庫容易被錯誤策略污染。
- **程式碼開源**：https://github.com/suzgunmirac/dynamic-cheatsheet

## 論文全文

Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory
Authors: Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou
Venue: ICML (Machine Learning)
arXiv: 2504.07952 | Published: 2025-04-10

### Abstract

Despite their impressive performance on complex tasks, current language models (LMs) typically operate in a vacuum: Each input query is processed separately, without retaining insights from previous attempts. Here, we present Dynamic Cheatsheet (DC), a lightweight framework that endows a black-box LM with a persistent, evolving memory. Rather than repeatedly re-discovering or re-committing the same solutions and mistakes, DC enables models to store and reuse accumulated strategies, code snippets, and general problem-solving insights at inference time. This test-time learning enhances performance substantially across a range of tasks without needing explicit ground-truth labels or human feedback. Leveraging DC, Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams once it began retaining algebraic insights across questions. Similarly, GPT-4o's success rate on the Game of 24 puzzle increased from about 10% to 99% after the model discovered and reused a Python-based solution. In tasks prone to arithmetic mistakes, such as balancing equations, DC enabled GPT-4o and Claude to reach near-perfect accuracy by recalling previously validated code, whereas their baselines stagnated around 50%. Beyond arithmetic challenges, DC yields notable accuracy gains on knowledge-demanding tasks. Claude achieved a 9% improvement in GPQA-Diamond and an 8% boost on MMLU-Pro Engineering and Physics problems. Crucially, DC's memory is self-curated, focusing on concise, transferable snippets rather than entire transcripts, thereby facilitating meta-learning and avoiding context ballooning. Unlike fine-tuning or static retrieval methods, DC adapts LMs' problem-solving skills on the fly, without modifying their underlying parameters.

### 1 Introduction

Modern large language models (LLMs) can tackle complex reasoning tasks, answer various questions, and generate extensive texts. Yet they still suffer from one critical limitation: once deployed, these models are fixed prior to deployment and typically retain no explicit or implicit memory of past questions, successes, or mistakes during inference. They approach each new problem de novo, often re-deriving the same insights—and re-committing the same errors. In contrast, human cognition stands on a foundation of incremental learning, continuously internalizing new experiences and solutions into a persistent mental model.

In this work, we present Dynamic Cheatsheet (DC), a simple and intuitive framework that endows black-box LLMs with a persistent, evolving memory at inference time. Rather than fine-tuning weights or retrieving facts from a massive static corpus (as in traditional retrieval-augmented generation systems), DC dynamically curates a compact library of reusable strategies, solution sketches, and code snippets. Either before or after each query, DC enables the system to decide which lessons to store, what to discard, and how to refine existing entries—thus effectively "learning" from successes and failures. It is a flexible online-learning approach that enables a black-box LLM to improve itself without needing any explicit ground truth labels or human feedback.

The overall workflow of DC is intuitive and compelling. In one version of DC (DC-Cu.), when presented with a new query, the LM first consults its external memory to see if any prior insights, strategies or relevant model solutions have been stored. It then proposes a solution by combining the retrieved insights with its own internal reasoning capabilities. Upon generating an answer, it then proceeds to a curation phase that updates the memory: If the approach seems to be correct, useful, or practical, DC codifies it in its memory for future use; if an error surfaces, DC may revise or prune faulty heuristics. This all happens without gradient-based parameter updates, so computational overhead remains modest, and compatibility with black-box APIs (e.g., GPT-4 or Claude) is fully preserved.

We tested DC across multiple challenging benchmarks and observed that it increases performance and reduces repetitive mistakes. On AIME 2024, Claude 3.5 Sonnet jumped from 23% to 50% accuracy, more than doubling its baseline score, by retaining algebraic and combinatorial insights. Likewise, it gained 30% accuracy on AIME 2025. Notably, these improvements hold in knowledge-intensive tasks as well. On GPQA-Diamond, which tests specialized domain questions, DC lifted Claude by over 9%. In MMLU-Pro Engineering and Physics, it provided up to an 8% boost in performance by allowing the model to maintain a "toolkit" of formulas and general problem-solving patterns.

An even more striking and compelling example is the Game of 24, a puzzle that requires the solver to combine four digits into an arithmetic expression equaling 24. GPT-4o's baseline performance (10%) increased to 99% under DC. Early in the test sequence, the model discovered that an efficient Python brute-force solver eliminated all manual guesswork. Once this snippet was stored, GPT-4o simply retrieved it for subsequent queries, avoiding manual arithmetic entirely. We saw a similar pattern in Math Equation Balancer, where GPT-4o and Claude soared from 45-50% to 98–100% by "recalling" a straightforward code-based approach instead of manually fumbling with numeric manipulations.

Nonetheless, DC is not a panacea. We found that smaller models, such as GPT-4o-mini, benefit from DC in limited amounts. These models generate too few correct solutions in these challenging tasks in the first place, leaving the memory populated with flawed or incomplete strategies. Worse, they struggle to refine stored content. DC can amplify the strengths of models that can already produce high-quality outputs, but not fix foundational gaps in reasoning.

We also note that DC differs from naive "append the entire conversation history" in-context learning approaches. Under DC, memory is carefully curated, focusing on succinct, useful, and transferable knowledge over raw transcripts. This prevents ballooning context lengths and helps ensure that repeated retrieval remains tractable.

### 2 Dynamic Cheatsheet (DC) Methodology

DC, in its core, includes an external, non-parametric memory that evolves in tandem with the LLM's inference process. Rather than fine-tuning the underlying weights, DC tracks successes and failures of the model at test time, then selectively stores heuristics, strategies, or short textual artifacts that can guide the LLM in future instances. Notably, this approach respects the black-box nature of many commercial LLM APIs: no gradient-based updates are required, and the model's core parameters remain untouched.

#### 2.1 DC: Building Blocks and Iterative Loop

The DC framework consists of two core modules: **generation** and **curation**. Both modules can easily operate on top of the same LM (prompted differently) or on separate LMs.

**Solution Generation with Memory**: At the i-th step, the model is provided with both the new query x_i and the current memory state M_i, which captures knowledge gleaned from previous successes and failures:

```
ỹ_i = Gen(x_i, M_i)
```

**Memory Curation Step**: After the generator produces its answer ỹ_i to x_i, the curator updates the current content of the memory:

```
M_{i+1} = Cur(M_i, x_i, ỹ_i)
```

During memory curation, Cur mainly considers: (i) the usefulness and generalizability of the newly produced answer, (ii) refinement or removal of existing memory entries, and (iii) clarity and compactness of the entire memory.

#### 2.2 DC with Retrieval & Synthesis (DC-RS)

DC-RS modifies the sequence of memory updates and introduces a retrieval mechanism, Retr, into the curation process. Retr allows the model to retrieve the most relevant past input-output pairs from its knowledge base. The steps are:

1. Retrieve top-k most similar inputs: R_i = Retr(x_i, {(x_j, ỹ_j)}_{j<i}, k)
2. Update memory: M_i = Cur(M_{i-1}, x_i, R_i)
3. Generate: ỹ_i = Gen(x_i, M_i)

The retrieval mechanism ranks historical inputs based on cosine similarity with the current query (using OpenAI's text-embedding-3-small), selecting the most relevant past examples along with their generated solutions.

#### 2.3 Baselines

- **Baseline prompting (BL)**: Plain vanilla prompting, no memory or retrieval.
- **DC-∅ (empty memory)**: DC framework with memory content always empty—isolates effect of memory curation.
- **Full-History Appending (FH)**: Naive approach that appends entire conversation history without curation.
- **Dynamic Retrieval (DR)**: Retrieval without curation—pastes relevant past interactions verbatim into prompt.

### 3 Experimental Setup

#### 3.1 Tasks and Datasets

- **AIME 2020–2025**: American Invitational Mathematics Examination. Complex algebra, combinatorics, number theory, geometry, and probability problems.
- **GPQA-Diamond**: 198 expert-validated questions across natural sciences (biology, chemistry, physics). Correctly answered by domain experts but missed by non-experts.
- **Game of 24**: Combine four numbers into an arithmetic expression equaling 24. Emphasizes systematic search and pattern recognition.
- **Math Equation Balancer**: Insert appropriate operators to complete equations. 250 arithmetic expressions.
- **MMLU-Pro (Engineering and Physics)**: Professional-level multiple-choice questions. 250 physics + 250 engineering questions sampled.

#### 3.2 Language Models

GPT-4o, Claude 3.5 Sonnet (primary); GPT-4o-mini, Claude 3.5 Haiku, DeepSeek R1 (secondary evaluation).

### 4 Results and Discussion

Key results (Claude 3.5 Sonnet):
- AIME 2024: BL 23.3% -> DC-Cu 50.0% (+26.7%)
- AIME 2025: BL 26.7% -> DC-Cu 56.7% (+30%)
- GPQA-Diamond: BL ~55% -> DC ~64% (+9%)
- MMLU-Pro Engineering: +8%
- Game of 24 (GPT-4o): BL 10% -> DC-RS 99% (+89%)
- Math Equation Balancer: BL ~50% -> DC ~98–100%

**Key finding**: DC works best when the base model is already capable of generating high-quality solutions; it amplifies strengths but cannot compensate for foundational reasoning gaps. Smaller models (GPT-4o-mini) showed minimal benefit.

**Memory dynamics**: Successful strategies get codified and reused; erroneous strategies get pruned or updated. The memory focuses on transferable snippets—code solutions, general heuristics, formula toolkits—rather than raw conversation history.

### 5 Related Work

DC relates to several lines of work:
- **Test-time computation / training**: Dynamic Evaluation, domain adaptation, but DC requires no gradient updates.
- **Retrieval-Augmented Generation (RAG)**: DC differs by dynamically curating memory rather than retrieving from a static corpus.
- **In-context learning**: DC improves over naive full-history appending by selective curation.
- **Memory-augmented LLMs**: MemGPT, Voyager, EXPEL—DC is lighter-weight and black-box compatible.
- **Meta-learning**: DC can be viewed as prompt-level meta-learning where the memory acts as an evolving "cheatsheet."

### 6 Conclusion

Dynamic Cheatsheet is a lightweight, black-box-compatible framework for test-time learning through adaptive memory. It enables LLMs to accumulate strategies and insights across queries without parameter updates, achieving substantial performance gains on challenging benchmarks. The self-curated memory—focusing on concise, transferable snippets—bridges isolated inference events and the cumulative, experience-driven learning characteristic of human cognition.

**GitHub**: https://github.com/suzgunmirac/dynamic-cheatsheet
