---
title: "From Rows to Reasoning: A Retrieval-Augmented Multimodal Framework for Spreadsheet Understanding"
arxiv_id: 2601.08741
authors: "Anmol Gulati, Sahil Sen, Waqar Sarguroh, Kevin Paul"
fetched: 2026-05-26
published: 2026-01-13
source: "https://arxiv.org/abs/2601.08741"
source_tier: P
---

# From Rows to Reasoning: A Retrieval-Augmented Multimodal Framework for Spreadsheet Understanding

**Authors**: Anmol Gulati, Sahil Sen, Waqar Sarguroh, Kevin Paul (Commercial Technology and Innovation Office, PricewaterhouseCoopers U.S.)
**Published**: January 2026 (v1: 2026-01-13; v2: 2026-02-09)
**Source**: https://arxiv.org/abs/2601.08741
**arXiv ID**: 2601.08741
**Categories**: cs.CL (Computation and Language)

---

## Abstract

Large Language Models (LLMs) struggle to reason over large-scale enterprise spreadsheets containing thousands of numeric rows, multiple linked sheets, and embedded visual content such as charts and receipts. Prior state-of-the-art spreadsheet reasoning approaches typically rely on single-sheet compression or full-context encoding, which limits scalability and fails to reflect how real users interact with complex, multimodal workbooks. We introduce FRTR-Bench, the first large-scale benchmark for multimodal spreadsheet reasoning, comprising 30 enterprise-grade Excel workbooks spanning nearly four million cells and more than 50 embedded images. To address these challenges, we present From Rows to Reasoning (FRTR), an advanced, multimodal retrieval-augmented generation framework that decomposes Excel workbooks into granular row, column, and block embeddings, employs hybrid lexical-dense retrieval with Reciprocal Rank Fusion (RRF), and integrates multimodal embeddings to reason over both numerical and visual information. We tested FRTR on six LLMs, achieving 74% answer accuracy on FRTR-Bench with Claude Sonnet 4.5, a substantial improvement over prior state-of-the-art approaches that reached only 24%. On the SpreadsheetLLM benchmark, FRTR achieved 87% accuracy with GPT-5 while reducing token usage by roughly 50% compared to direct serialization methods.

**Keywords**: Large Language Models, Retrieval-Augmented Generation (RAG), Multimodal Data Retrieval, Scalable Numerical Reasoning

---

## Core Thesis

FRTR reframes enterprise spreadsheet analysis as a three-stage pipeline (Retrieve → Verify → Compose) using hybrid lexical-dense retrieval with RRF to surface only the minimal relevant evidence, bypassing LLM context limits entirely. By decomposing workbooks into multi-granular units (rows, columns, sliding windows, embedded images) and indexing them in a shared multimodal vector space, FRTR achieves 2–4× higher accuracy than compression-based approaches at 40% lower token cost, while preserving full provenance for audit compliance.

---

## 1. Introduction

Spreadsheets remain the foundational medium for analytical work at an enterprise level, and modern workbooks routinely contain thousands of cells, span multiple sheets, and embed diverse media such as charts, receipts, and scanned tables. While LLMs promise intuitive natural-language interaction with such documents, directly serializing entire sheets into a prompt is inefficient and brittle. Spreadsheet semantics hinge on spatial layout, structural dependencies, and cross-sheet relationships rather than text alone. Moreover, recent work shows that long-context LLMs suffer positional degradation — accuracy declines when relevant information appears far from the prompt boundaries.

This motivates retrieval-focused approaches that surface small, relevant subsets rather than streaming full spreadsheets into the context window.

A prominent prior direction is SpreadsheetLLM, which introduces encoding schemes (SheetEncoder and SheetCompressor) that compress cell content, positional addresses, and formatting to fit within an LLM's context window. While effective for single-sheet reasoning, such compression assumes all relevant data can fit within a single prompt and fails to scale to multi-sheet or multimodal settings.

**Three novel contributions of this work:**

1. **Retrieval-first framework**: An advanced, multimodal RAG approach integrating hybrid lexical-dense retrieval to overcome full-context limitations and improve scalability.
2. **Multi-granular and multimodal indexing**: Fine-grained indexing at row, column, and block levels, extended to multimodal settings using joint text-vision embeddings. Hybrid rank-fusion retrieval ensures robust performance across both textual and image-bearing spreadsheets.
3. **FRTR-Bench benchmark**: The first large-scale, multimodal spreadsheet reasoning benchmark spanning 30 enterprise-grade workbooks with nearly four million cells and over fifty embedded images.

Token scaling comparison: naive full-context serialization exceeds context limits as data grows, while FRTR maintains constant token usage (~8K) via selective retrieval.

---

## 2. Related Work

### 2.1. LLMs for Tables and Spreadsheets

Early neural models such as TAPAS learned to answer questions directly over tables by encoding cell values jointly with queries, while TUTA extended this paradigm by modeling hierarchical and spatial cues. OmniTab improved few-shot table QA by combining natural and synthetic supervision. These approaches focus on in-context reasoning within a single table and do not scale to multi-sheet or multimodal workbooks.

More recent work such as SpreadsheetLLM compresses spreadsheet structure and content to fit within LLM context limits, achieving notable gains on single-sheet reasoning. Complementary methods including Table-GPT and TableLLM improve general table manipulation and code generation capabilities. However, these approaches are not capable of handling cross-sheet and multimodal reasoning.

### 2.2. Long Context, Retrieval, and Hybrid Search

Despite advances in long-context modeling, evidence retrieval remains a bottleneck: simply extending context windows does not guarantee that models attend effectively to mid-range information. RAG approaches address this by selecting relevant evidence before generation, improving both performance and interpretability. Hybrid lexical-dense retrieval, fused through methods such as RRF, offers robustness and simplicity across tasks. However, basic chunking and retrieval methodologies do not take into account the complicated spatial relationships in spreadsheets, where logic can apply across rows, columns, and even sheets.

### 2.3. Multimodal Spreadsheet Understanding and Document VQA

Spreadsheets often convey semantics through visual layout (bold headers, merged cells, shaded totals) as well as through embedded images such as charts or scanned receipts. Vision-language models still struggle to interpret such spatial and structural cues. Parallel research in chart and document VQA (ChartQA, DocVQA) highlights the challenges of numerically grounded visual reasoning. These methods typically treat visual and textual modalities in isolation, without integrating multimodal embeddings that unify text, layout, and image semantics.

### 2.4. Benchmarks for Spreadsheet Interaction

Beyond table QA, recent benchmarks target spreadsheet interaction directly. SpreadsheetLLM performs reasoning on encoded spreadsheets, while SpreadsheetBench introduces realistic, forum-based spreadsheet questions. InstructExcel focuses on natural-language-to-OfficeScript translation. No existing benchmarks assess cross-sheet reasoning, multimodal queries, and large-scale evaluation together.

---

## 3. Framework Overview

### 3.1. Motivation and Design Goals

Real-world Excel workbooks exhibit three intertwined challenges: scale, multimodality, and cross-sheet dependency. Workbooks can span thousands of rows across multiple worksheets, include embedded charts or receipts, and encode meaning through layout and formatting. FRTR does not assume well-formed tables; its use of overlapping row-, column-, and window-level units allows relevant evidence to be retrieved even when logical groupings are not strictly aligned with grid boundaries.

**Three guiding principles:**

1. **Scalability**: Decompose workbooks into granular, retrievable units (rows, columns, blocks, images) to bypass context limits, deduplicating merged cells and representing both formulas and calculated values.
2. **Auditability**: Ensure transparent provenance via hybrid retrieval with RRF, supporting verifiable reasoning.
3. **Multimodality**: Use joint text-vision embeddings so that both tabular and visual content contribute to retrieval and reasoning.

### 3.2. Architecture Overview

FRTR operates in three stages: **Retrieve**, **Verify**, and **Compose**.

During ingestion, Excel workbooks are decomposed into rows, columns, sliding windows, and embedded images. Each unit is serialized and embedded using a multimodal encoder (Amazon Titan Multimodal) and indexed in a hybrid vector database. At query time, FRTR retrieves the most relevant units using hybrid lexical-dense search and provides the fused results as evidence for LLM reasoning. This architecture reduces context size while preserving interpretability and scalability.

### 3.3. Retrieval and Fusion Layer

Each spreadsheet unit is indexed as a structured document with lexical, vector, and metadata fields. FRTR performs two parallel retrievals: BM25 for lexical matching and cosine similarity for dense embeddings, and fuses results via Reciprocal Rank Fusion (RRF):

```
RRF(d) = Σ_{r∈R} 1 / (k + rank_r(d))
```

where k = 60 stabilizes low-ranked items. FRTR uses K_v = K_s = 20, returning the top-10 fused items annotated with provenance. This rank-based fusion avoids score normalization issues, ensuring robust, interpretable retrieval across modalities. RRF is used because it provides the most robust retrieval across both paraphrased queries and exact identifier lookups common in spreadsheet QA.

**Algorithm 1 — FRTR: From Rows to Reasoning**

- **Stage 1 (Indexing, Offline)**: For each sheet, compute adaptive window size s = ⌈√(N/K_target)⌉. For each unit u ∈ &#123;rows, columns, s×s windows, images&#125;: compute multimodal embedding v_u = E(u) and add (text(u), v_u, metadata(u)) to index D.
- **Stage 2 (Hybrid Retrieval, Online)**: Embed query q; retrieve top-K_v by cosine similarity (dense) and top-K_s by BM25 (lexical); compute RRF scores; return top-K chunks C with provenance labels.
- **Stage 3 (Answer Composition)**: Construct prompt P = {q, C, instruction}; invoke LLM M; parse JSON response {reasoning, answer}.

### 3.4. Multimodal Embedding Layer

For text-based units, FRTR serializes contextual information preserving spatial cues:
- **Rows**: include column headers
- **Columns**: include row indices
- **Windows**: preserve s×s spatial layout

Image units (charts, receipts, diagrams) are embedded using the vision branch of the same model, ensuring a shared latent space. Images are encoded as base64 and passed to the Titan Image-v1 embeddings API. This allows queries such as "Q4 revenue trends" to retrieve both numerical data and corresponding charts. A unified vector field holds both text and image representations, enabling cross-modal retrieval within a single index.

### 3.5. Reasoning and Output Generation

After retrieval, FRTR invokes an LLM with a structured prompt containing the query, retrieved chunks, and reasoning instructions. Each chunk is formatted with explicit metadata:

```
Chunk 1 (Score: 0.0164, Source: Vector)
Type: row | Sheet: Sales_Q4
ROW_42: Product | Units | Revenue | ...
```

The LLM produces structured JSON outputs:

```json
{
  "reasoning": "Analyzed columns B and C for revenue values.",
  "answer": "SUM(B2:B15)"
}
```

This format ensures both interpretability and machine-readability, facilitating downstream automation and audit compliance. FRTR itself does not execute formulas or modify spreadsheets, maintaining human oversight while ensuring verifiable, grounded reasoning.

---

## 4. FRTR-Bench: Benchmark for Spreadsheet Reasoning

### 4.1. Dataset Construction

To evaluate cross-sheet and multimodal reasoning at scale, FRTR-Bench comprises 30 multimodal Excel workbooks across diverse domains. Each workbook stresses three dimensions:

1. **Scale**: up to 210,000 rows per workbook, far beyond typical LLM context
2. **Multimodality**: embedded PNG images (charts, receipts, dashboards)
3. **Cross-sheet complexity**: multi-sheet references (e.g., `=SUM(Sheet1!B2:B100, Sheet2!C5:C50)`)

**Difficulty tiers by scale:**
- **Easy**: < 5,000 rows — small business summaries
- **Medium**: 5,000–20,000 rows — mid-size audit or operations data
- **Hard**: 20,000–210,000 rows — large-scale consolidation workbooks

Domains include finance, supply chain, healthcare, energy, government, education, and others. Each workbook includes a metadata sheet, 1–5 data sheets, embedded PNGs with captions, and a Questions sheet containing 5–10 manually crafted queries with explicit provenance (e.g., `Sheet1!B5` or `Image ID: Chart_001`).

### 4.2. Evaluation Protocol

**Answer Accuracy**: Comparing model outputs with annotated ground-truth answers and provenance (cells, formulas, or images). Answers are correct if numerically consistent or functionally identical in formula logic (e.g., `SUM(B2:B10)` vs. `SUM(B2:B5)+SUM(B6:B10)`).

**Latency**: Average response time per query (not including embedding and retrieval), measured from user query submission to model output generation.

**Mean Tokens**: Mean number of tokens per model input after retrieval and formatting. Lower token counts indicate more efficient retrieval.

### 4.3. Benchmark Statistics

| Metric | Count |
|--------|-------|
| Workbooks | 30 |
| Sheets | 155 |
| Rows | 656,457 |
| Cells | 3,928,934 |
| Embedded Images | 53 |
| Cross-Sheet Formulas | 30 |
| Questions | 157 |

**Example question** (from `frtr_0003_consolidation.xlsx`, Hard, 49,867 rows):
- Question: "What is the consolidated operating income for Region EMEA in FY2024?"
- ReasoningType: cross-sheet
- Provenance: `Consolidation!E47`, `=SUM(EMEA_Sales!D:D,EMEA_Ops!E:E)`
- Answer: $12,450,000

---

## 5. Evaluation

### 5.1. Experiment 1 — FRTR-Bench Evaluation

#### Results (Table 2): Performance comparison on FRTR-Bench

Mean tokens: FRTR 7,691; SpreadsheetLLM 12,745 (FRTR uses ~40% fewer tokens).

| Model | FRTR Accuracy | FRTR Latency (s) | SpreadsheetLLM Accuracy | SpreadsheetLLM Latency (s) | ΔAccuracy |
|-------|--------------|-----------------|------------------------|---------------------------|-----------|
| GPT-4o | 0.49 | 5.04 | 0.06 | 1.14 | +0.43 |
| GPT-5 | 0.73 | 15.50 | 0.18 | 18.10 | +0.55 |
| Claude Sonnet 4.5 | 0.74 | 11.71 | 0.13 | 8.80 | +0.61 |
| Gemini 2.5 Pro | 0.67 | 26.90 | 0.24 | 33.35 | +0.43 |
| LLaMA Maverick-17B | 0.56 | 2.42 | 0.23 | 1.15 | +0.33 |
| GPT-OSS-120B | 0.51 | 5.75 | 0.21 | 8.80 | +0.30 |

#### Discussion

- FRTR consistently achieves 2–4× higher accuracy, 40% lower token usage, and comparable or lower latency than SpreadsheetLLM.
- On easy workbooks, FRTR attains mean accuracies of 0.86–0.93 for top-tier models vs. SpreadsheetLLM's 0.18–0.23.
- Performance remains robust on medium (0.62–0.65) and hard (0.66–0.72) tiers, where SpreadsheetLLM collapses below 0.10.
- Average prompt length is only 7.7K tokens vs. SpreadsheetLLM's 13.1K tokens (251× compression ratio relative to raw workbook size).
- FRTR achieves **65% accuracy** on the 23 image-dependent questions — a capability text-only approaches cannot address at all.
- The U-shaped accuracy pattern (medium difficulty is hardest) reflects structural complexity, not size: very large spreadsheets tend to be transaction logs with repetitive structure, while medium ones represent complex business consolidations with retrieval ambiguity.

### 5.2. Experiment 2 — SpreadsheetLLM Benchmark Evaluation

#### Results (Table 3): Performance comparison on SpreadsheetLLM benchmark

Mean tokens: FRTR 6,920; SpreadsheetLLM 5,811; Naïve full-context 13,631.

| Technique | Model | Answer Accuracy | Latency (s) |
|-----------|-------|----------------|-------------|
| FRTR | GPT-4o | 0.77 | 2.48 |
| FRTR | GPT-5 | 0.87 | 18.06 |
| FRTR | Claude Sonnet 4.5 | 0.84 | 10.40 |
| FRTR | Gemini 2.5 Pro | 0.85 | 24.06 |
| FRTR | LLaMA Maverick-17B | 0.53 | 2.18 |
| FRTR | GPT-OSS-120b | 0.75 | 7.37 |
| SpreadsheetLLM | GPT-4o | 0.78 | 0.81 |
| SpreadsheetLLM | GPT-5 | 0.90 | 5.50 |
| SpreadsheetLLM | Claude Sonnet 4.5 | 0.91 | 5.49 |
| SpreadsheetLLM | Gemini 2.5 Pro | 0.89 | 10.00 |
| SpreadsheetLLM | LLaMA Maverick-17B | 0.73 | 0.73 |
| SpreadsheetLLM | GPT-OSS-120b | 0.80 | 4.01 |
| Naïve Full-Context | GPT-4o | 0.35 | 3.01 |
| Naïve Full-Context | GPT-5 | 0.68 | 18.07 |
| Naïve Full-Context | Claude Sonnet 4.5 | 0.55 | 9.06 |
| Naïve Full-Context | Gemini 2.5 Pro | 0.67 | 15.48 |
| Naïve Full-Context | LLaMA Maverick-17B | 0.41 | 2.45 |
| Naïve Full-Context | GPT-OSS-120b | 0.59 | 8.61 |

#### Discussion

FRTR performs on par with SpreadsheetLLM in overall accuracy across most model families (0.84–0.87 vs. 0.89–0.91 for high-capacity models) while substantially outperforming the naïve full-context baseline. FRTR considers every sheet in an Excel workbook, while SpreadsheetLLM was given the oracle sheet. FRTR achieves this parity while using roughly 40–50% fewer tokens than the full-context baseline and maintaining stable latency across models. The retrieval-based design also provides explicit provenance for every reasoning step, enabling interpretability that compression-based systems lack.

### 5.3. Ablation Studies

#### 5.3.1. Retrieval Method Ablation (Table 4)

| Retrieval Method | Answer Accuracy | Avg Retrieval Time (s) | Avg Tokens |
|-----------------|----------------|----------------------|------------|
| Hybrid (RRF) | **0.74** | 0.82 | 6,903 |
| Vector Only | 0.59 | 0.70 | 5,857 |
| BM25/Lexical Only | 0.42 | **0.11** | 5,616 |

Hybrid RRF achieves significantly higher accuracy by combining exact-match patterns (BM25) with semantic similarity (dense), validating the design choice for RRF-based hybrid retrieval.

#### 5.3.2. Unit Granularity Ablation (Table 5)

| Units Retrieved | Answer Accuracy | Avg LLM Time (s) | Avg Tokens |
|----------------|----------------|-----------------|------------|
| Rows | 0.52 | 7.55 | 2,017 |
| Columns | 0.18 | 5.34 | 11,465 |
| Windows | 0.58 | 7.15 | 7,259 |
| All Types (FRTR) | **0.74** | 11.71 | 7,690 |

Different granularities capture complementary information. Combining all unit types (rows + columns + windows + images) achieves the highest accuracy, demonstrating that multi-granular indexing surfaces relevant evidence regardless of query structure. FRTR's multi-granular approach outperforms SpreadsheetLLM (0.24 accuracy) by over 3×.

### 5.4. Cost Analysis

FRTR uses 7,691 tokens on average vs. SpreadsheetLLM's 12,745 tokens (40% reduction). At typical API rates ($0.01–0.03 per 1K input tokens for frontier models), for an enterprise processing 1,000 queries daily, FRTR would reduce annual LLM costs by approximately 40% while improving accuracy. Embedding costs are incurred once during indexing and amortized across all subsequent queries.

---

## 6. Limitations

1. Multimodal image accuracy (65%) is promising but has room for improvement as enterprise-grade multimodal encoders mature.
2. FRTR-Bench focuses on English-language spreadsheets, though the retrieval architecture is language-agnostic.
3. FRTR generates formulas and cell references rather than executing them, preserving human oversight aligned with enterprise audit requirements.
4. Initial workbook indexing is a one-time cost (alleviated by batch processing and parallelization); retrieval latency is negligible once indexed (under 1 second).

---

## 7. Ethics and Reproducibility

FRTR-Bench consists of synthetic enterprise-style workbooks designed to simulate realistic analytical scenarios without using real user data or proprietary information. The benchmark is available at: https://github.com/AnmolGulati6/FRTR-bench

---

## 8. Conclusion

FRTR introduces a retrieval-first multimodal RAG framework that decomposes spreadsheets into granular row, column, and block embeddings, employs hybrid lexical-dense retrieval with RRF, and integrates multimodal embeddings to reason jointly over numerical and visual content. Key results:

- **74% accuracy** on FRTR-Bench (vs. 24% prior state-of-the-art) — 50 percentage points improvement
- **87% accuracy** on SpreadsheetLLM benchmark with GPT-5
- **~50% token reduction** vs. full-context baseline
- **65% accuracy** on image-dependent questions (vs. 0% for text-only approaches)
- **40% cost reduction** at enterprise query volumes

Future work: adaptive retrieval, finer multimodal alignment, and agentic spreadsheet manipulation.

---

## Key References

- **SpreadsheetLLM** (Dong et al., 2025): SheetEncoder and SheetCompressor for single-sheet reasoning — primary baseline. GitHub: https://github.com/microsoft/SpreadsheetLLM
- **SpreadsheetBench** (Ma et al., 2024): Realistic, forum-based spreadsheet questions benchmark.
- **InstructExcel** (Payan et al., 2023): Natural-language-to-OfficeScript translation benchmark.
- **TAPAS** (Herzig et al., 2020): Neural table QA by encoding cell values jointly with queries.
- **TUTA** (Wang et al., 2021): Table understanding with hierarchical and spatial cues.
- **OmniTab** (Jiang et al., 2022): Few-shot table QA combining natural and synthetic supervision.
- **Table-GPT** (Zha et al., 2023): General table manipulation capabilities.
- **Reciprocal Rank Fusion** (Cormack et al., 2009): Rank fusion method for hybrid retrieval. SIGIR '09, pp. 758–759.
- **RAG** (Lewis et al., 2021): Retrieval-augmented generation for NLP.
- **Lost in the Middle** (Liu et al., 2023): Positional degradation in long-context LLMs.
- **RETRO** (Borgeaud et al., 2022): Improving language models by retrieving from trillions of tokens.
- **ChartQA** (Masry et al., 2022): Chart question answering benchmark.
- **DocVQA** (Mathew et al., 2021): Document visual question answering benchmark.
- **Amazon Titan Multimodal Embeddings G1** (AWS, 2025): Multimodal encoder used in FRTR implementation.
- **Abootorabi et al. (2025)**: Survey on multimodal retrieval-augmented generation. arXiv:2502.08826.
- **Frank et al. (2025)**: Jackal execution-based benchmark for text-to-JQL tasks.
