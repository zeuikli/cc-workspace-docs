---
title: "SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval"
arxiv_id: 2109.10086
authors: "Thibault Formal, Carlos Lassance, Benjamin Piwowarski, Stéphane Clinchant"
fetched: 2026-05-26
published: 2021-09-21
source: "https://arxiv.org/abs/2109.10086"
source_tier: P
---

# SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval

**Authors**: Thibault Formal (Naver Labs Europe / Sorbonne Université, LIP6), Carlos Lassance (Naver Labs Europe), Benjamin Piwowarski (Sorbonne Université, CNRS, LIP6), Stéphane Clinchant (Naver Labs Europe)
**Published**: September 2021
**Source**: https://arxiv.org/abs/2109.10086
**arXiv ID**: 2109.10086
**Categories**: cs.IR, cs.AI, cs.CL
**Comments**: 5 pages. Substantial text overlap with arXiv:2107.05720

---

## Abstract

In neural Information Retrieval (IR), ongoing research is directed towards improving the first retriever in ranking pipelines. Learning dense embeddings to conduct retrieval using efficient approximate nearest neighbors methods has proven to work well. Meanwhile, there has been a growing interest in learning *sparse* representations for documents and queries, that could inherit from the desirable properties of bag-of-words models such as the exact matching of terms and the efficiency of inverted indexes. Introduced recently, the SPLADE model provides highly sparse representations and competitive results with respect to state-of-the-art dense and sparse approaches. In this paper, we build on SPLADE and propose several significant improvements in terms of effectiveness and/or efficiency. More specifically, we modify the pooling mechanism, benchmark a model solely based on document expansion, and introduce models trained with distillation. We also report results on the BEIR benchmark. Overall, SPLADE is considerably improved with more than 9% gains on NDCG@10 on TREC DL 2019, leading to state-of-the-art results on the BEIR benchmark.

**Keywords**: neural networks, indexing, sparse representations, regularization

---

## Core Thesis

SPLADE's original sum-pooling mechanism is suboptimal; replacing it with max-pooling yields large effectiveness gains, a document-only encoder variant enables fully offline indexing with competitive quality, and cross-architecture knowledge distillation pushes DistilSPLADE-max to state-of-the-art zero-shot performance on BEIR while preserving the inverted-index efficiency of sparse retrieval.

---

## 1. Introduction

The release of large pre-trained language models like BERT (Devlin et al., 2018) transformed Information Retrieval. Neural rankers initially served as re-rankers in two-stage pipelines, where first-stage retrieval relied on bag-of-words (BM25) models using inverted indexes. While BOW models remain strong baselines, they suffer from the vocabulary mismatch problem, where relevant documents may not contain exact query terms.

Dense retrieval with approximate nearest neighbors has shown impressive results, but can still benefit from BOW approaches due to the absence of explicit term matching. This motivates learning **sparse** representations for queries and documents — inheriting exact-match properties and inverted-index efficiency, while also modeling implicit expansion to reduce vocabulary mismatch.

This paper builds on the original SPLADE model (Formal et al., 2021) with three main contributions:

1. **Max pooling**: Replacing sum pooling with max pooling substantially increases effectiveness.
2. **Document-only encoder (SPLADE-doc)**: A model without query expansion where everything can be pre-computed and indexed offline — more efficient with competitive results.
3. **Distillation (DistilSPLADE-max)**: Two-step distillation training leading to close to state-of-the-art on MS MARCO and BEIR.

---

## 2. Related Works

**Dense retrieval**: BERT Siamese models (Sentence-BERT) are standard for candidate generation in QA and IR. Key training improvements include better negative sampling and distillation. ColBERT extends this with token-level interactions for fine-grained matching, at the cost of large embedding storage.

**Sparse retrieval history**:
- **SNRM** (Zamani et al., 2018): First sparse high-dimensional latent space via ℓ₁ regularization; limited effectiveness and efficiency.
- **DeepCT** (Dai & Callan, 2019): Contextualized term weight learning within the fixed document vocabulary — does not solve vocabulary mismatch.
- **doc2query / docTTTTTquery** (Nogueira et al.): Generative document expansion to predict query terms, adding new terms and boosting important ones.
- **DeepImpact** (Mallia et al., 2021): Combines doc2query-T5 expansion with DeepCT reweighting to learn term impacts.
- **SparTerm, EPIC, SPARTA**: Compute interaction matrices between document/query tokens and full vocabulary, then aggregate. EPIC and SPARTA lack sufficient sparsity; SparTerm lacks explicit sparsity regularization.
- **SPLADE** (Formal et al., 2021): Combines regularization (FLOPS), expansion, and compression in an end-to-end manner.
- **COIL** (Gao et al., 2021): Dense per-term representations for contextualized term matching; larger index size.

---

## 3. Sparse Lexical Representations for First-Stage Ranking

### 3.1 SPLADE Model

SPLADE predicts term importance across the BERT WordPiece vocabulary (|V| = 30,522) using the MLM layer logits. For input sequence t = (t₁, t₂, ..., t_N) with BERT embeddings (h₁, h₂, ..., h_N):

**Token-vocabulary importance weight**:
```
w_ij = transform(h_i)^T E_j + b_j    j ∈ {1,...,|V|}
```
where E_j is the BERT input embedding for token j, b_j is a token-level bias, and transform(·) is a linear layer with GeLU activation and LayerNorm.

**Final representation (original sum pooling)**:
```
w_j = Σ_{i∈t} log(1 + ReLU(w_ij))
```

**Ranking loss** (contrastive with in-batch negatives):
```
ℒ_{rank-IBN} = -log [ e^{s(q_i, d_i+)} / (e^{s(q_i, d_i+)} + e^{s(q_i, d_i-)} + Σ_j e^{s(q_i, d_{i,j}-})) ]
```

**FLOPS regularization** (Paria et al., 2020): Penalizes the expected number of floating-point operations needed for retrieval:
```
ℓ_FLOPS = Σ_{j∈V} ā_j² = Σ_{j∈V} (1/N · Σ_{i=1}^N w_j^{(d_i)})²
```

**Overall loss**:
```
ℒ = ℒ_{rank-IBN} + λ_q · ℒ_reg^q + λ_d · ℒ_reg^d
```
Separate regularization weights for queries and documents allow stronger sparsity pressure on queries (critical for fast retrieval).

### 3.2 Pooling Strategy (SPLADE-max)

Replace sum pooling with **max pooling**:
```
w_j = max_{i∈t} log(1 + ReLU(w_ij))
```

This makes the model more similar to SPARTA/EPIC/ColBERT. Max pooling is now the default and the model is called **SPLADE-max**.

### 3.3 SPLADE Document Encoder (SPLADE-doc)

A document-only version with no query expansion. The ranking score is:
```
s(q, d) = Σ_{j∈q} w_j^d
```

Since the score only depends on document term weights, everything can be **pre-computed and indexed offline**, reducing online inference cost. Simpler to train — only a single forward pass per document (vs. multiple beam search inferences for doc2query-T5).

### 3.4 Distillation and Hard Negatives (DistilSPLADE-max)

Two-step distillation process:
1. Train a SPLADE first-stage retriever and a cross-encoder reranker (using `cross-encoder/ms-marco-MiniLM-L-12-v2`) on triplets from Hofstätter et al. (2020).
2. Generate harder negative triplets using the distillation-trained SPLADE, then use the reranker to produce Margin-MSE loss scores. Train a new SPLADE model from scratch on these triplets.

---

## 4. Experimental Setting and Results

**Dataset**: MS MARCO passage ranking (≈8.8M passages; dev set: 6,980 queries; TREC DL 2019: 43 queries with fine-grained annotations).

**Training setup**:
- Initialized from DistilBERT-base checkpoint
- ADAM optimizer, lr = 2e-5, linear scheduling, warmup = 6,000 steps, batch size = 124
- Max sequence length: 256
- λ scheduler: quadratically increases until 50k steps, then constant; typical values 1e-1 to 1e-4
- Separate λ for queries and documents
- Best checkpoint by MRR@10 on 500-query validation set after 150k iterations (SPLADE-doc: 50k steps, last checkpoint)
- Infrastructure: 4× Tesla V100 32GB; PyTorch + HuggingFace Transformers
- Custom index with Python arrays + Numba for parallel retrieval

**Evaluation metrics**: MRR@10 (MS MARCO dev), NDCG@10 and Recall@1000 (both MS MARCO dev and TREC DL 2019).

### Table 1: MS MARCO Dev and TREC DL 2019 Results

| Model | MRR@10 | R@1000 | NDCG@10 | R@1000 (TREC) |
|---|---|---|---|---|
| **Dense Retrieval** | | | | |
| Siamese (ours) | 0.312 | 0.941 | 0.637 | 0.711 |
| ANCE | 0.330 | 0.959 | 0.648 | — |
| TCT-ColBERT | 0.359 | 0.970 | 0.719 | 0.760 |
| TAS-B | 0.347 | 0.978 | 0.717 | 0.843 |
| RocketQA | 0.370 | 0.979 | — | — |
| **Sparse Retrieval** | | | | |
| BM25 | 0.184 | 0.853 | 0.506 | 0.745 |
| DeepCT | 0.243 | 0.913 | 0.551 | 0.756 |
| doc2query-T5 | 0.277 | 0.947 | 0.642 | 0.827 |
| SparTerm | 0.279 | 0.925 | — | — |
| COIL-tok | 0.341 | 0.949 | 0.660 | — |
| DeepImpact | 0.326 | 0.948 | 0.695 | — |
| SPLADE (Formal et al., 2021) | 0.322 | 0.955 | 0.665 | 0.813 |
| **Our Methods** | | | | |
| SPLADE-max | 0.340 | 0.965 | 0.684 | 0.851 |
| SPLADE-doc | 0.322 | 0.946 | 0.667 | 0.747 |
| **DistilSPLADE-max** | **0.368** | **0.979** | **0.729** | **0.865** |

### 4.1 Impact of Max Pooling

Max pooling brings ~2 points improvement in MRR@10 and NDCG@10 over the SPLADE sum-pooling baseline. SPLADE-max is consistently better than original SPLADE across the full effectiveness-efficiency trade-off curve (FLOPS). Also improves on BEIR.

### 4.2 Document Expansion (SPLADE-doc)

The document-only encoder reaches the same performance as original SPLADE, outperforming doc2query-T5 on MS MARCO. For relatively sparse representations (avg. 19 non-zero weights/doc), achieves MRR@10 = 29.6. Training and application is simpler: single forward pass vs. multiple beam search inferences.

### 4.3 Distillation

DistilSPLADE-max achieves large improvements, especially in higher FLOPS regimes (0.368 MRR@10 at ≈4 FLOPS) while remaining efficient at low FLOPS (0.35 MRR at ≈0.3 FLOPS).

### Table 2: BEIR Benchmark Results (NDCG@10)

| Corpus | ColBERT | BM25 | TAS-B | SPLADE-sum | SPLADE-max | DistilSPLADE-max |
|---|---|---|---|---|---|---|
| MS MARCO | 0.425 | 0.228 | 0.408 | 0.387 | 0.402 | 0.433 |
| ArguAna | 0.233 | 0.315 | 0.427 | 0.447 | 0.439 | **0.479** |
| Climate-FEVER | 0.184 | 0.213 | 0.228 | 0.162 | 0.199 | **0.235** |
| DBPedia | 0.392 | 0.273 | 0.384 | 0.343 | 0.366 | **0.435** |
| FEVER | 0.771 | 0.753 | 0.700 | 0.728 | 0.730 | **0.786** |
| FiQA-2018 | 0.317 | 0.236 | 0.300 | 0.258 | 0.287 | **0.336** |
| HotpotQA | 0.593 | 0.603 | 0.584 | 0.635 | 0.636 | **0.684** |
| NFCorpus | 0.305 | **0.325** | 0.319 | 0.311 | 0.313 | 0.334 |
| NQ | 0.524 | 0.329 | 0.463 | 0.438 | 0.469 | **0.521** |
| Quora | **0.854** | 0.789 | 0.835 | 0.829 | 0.835 | 0.838 |
| SCIDOCS | 0.145 | **0.158** | 0.149 | 0.141 | 0.145 | **0.158** |
| SciFact | 0.671 | 0.665 | 0.643 | 0.626 | 0.628 | **0.693** |
| TREC-COVID | 0.677 | 0.656 | 0.481 | 0.655 | 0.673 | **0.710** |
| Touché-2020 (v1) | 0.275 | **0.614** | 0.173 | 0.289 | 0.316 | 0.364 |
| **Avg. all** | 0.455 | 0.440 | 0.435 | 0.446 | 0.460 | **0.500** |
| **Avg. zero-shot** | 0.457 | 0.456 | 0.437 | 0.451 | 0.464 | **0.506** |
| **Best on dataset** | 2 | 2 | 0 | 0 | 0 | **11** |

DistilSPLADE-max wins on 11 of 14 datasets, achieving best average scores on both all and zero-shot subsets.

---

## 5. Conclusion

Three improvements to SPLADE:
1. **Max pooling** provides substantial effectiveness gains over sum pooling.
2. **SPLADE-doc** (document-only encoder) enables fully offline indexing with competitive quality — good for latency-constrained settings.
3. **DistilSPLADE-max** (two-step knowledge distillation) leads to near state-of-the-art on MS MARCO/TREC DL 2019 and clearly outperforms recent dense models on zero-shot BEIR evaluation.

Key result: DistilSPLADE-max achieves 0.368 MRR@10 on MS MARCO dev, 0.729 NDCG@10 on TREC DL 2019, and 0.500 avg NDCG@10 on BEIR (beating ColBERT's 0.455), while maintaining inverted-index efficiency.

---

## Key References

- **Formal et al. (2021)** — SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking. SIGIR '21. https://doi.org/10.1145/3404835.3463098
- **Hofstätter et al. (2021)** — TAS-B: Efficiently Teaching an Effective Dense Retriever with Balanced Topic Aware Sampling. SIGIR 2021.
- **Hofstätter et al. (2020)** — Improving Efficient Neural Ranking Models with Cross-Architecture Knowledge Distillation. arXiv:2010.02666
- **Thakur et al. (2021)** — BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of IR Models. arXiv:2104.08663
- **Paria et al. (2020)** — Minimizing FLOPs to Learn Efficient Sparse Representations. arXiv:2004.05665
- **Mallia et al. (2021)** — DeepImpact: Learning Passage Impacts for Inverted Indexes. SIGIR '21.
- **Gao et al. (2021)** — COIL: Revisit Exact Lexical Match in IR with Contextualized Inverted List. NAACL 2021.
- **Khattab & Zaharia (2020)** — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT. SIGIR '20.
- **Xiong et al. (2021)** — ANCE: Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval. ICLR 2021.
- **Lin et al. (2021)** — TCT-ColBERT: In-Batch Negatives for Knowledge Distillation with Tightly-Coupled Teachers. RepL4NLP 2021.
- **Dai & Callan (2019)** — DeepCT: Context-Aware Sentence/Passage Term Importance Estimation. arXiv:1910.10687
- **Nogueira & Lin (2019)** — From doc2query to docTTTTTquery.
- **Bai et al. (2020)** — SparTerm: Learning Term-based Sparse Representation for Fast Text Retrieval. arXiv:2010.00768
- **Zamani et al. (2018)** — SNRM: From Neural Re-Ranking to Neural Ranking. CIKM '18.
- **Devlin et al. (2018)** — BERT: Pre-training of Deep Bidirectional Transformers. arXiv:1810.04805
