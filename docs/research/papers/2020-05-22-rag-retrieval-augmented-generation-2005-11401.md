---
url: "https://arxiv.org/abs/2005.11401"
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
date: 2020-05-22
arxiv_id: 2005.11401
authors: "Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela"
referenced_by: warmwater.dev
source: arxiv
---

## Abstract

Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

## 主要貢獻

- **RAG 框架（Retrieval-Augmented Generation）**：結合預訓練參數記憶（seq2seq 模型）與非參數記憶（Wikipedia 密集向量索引），為語言生成任務提供通用 fine-tuning 方案。
- **兩種 RAG 變體**：
  - **RAG-Sequence**：整個生成序列使用同一份檢索文件；對每份文件獨立執行 beam search 後合併。
  - **RAG-Token**：每個 token 可使用不同的檢索文件，允許生成時從多份文件中取用不同知識。
- **端到端訓練**：Retriever（DPR，基於 BERT 的雙編碼器）與 Generator（BART-large）聯合訓練，無需對檢索文件的直接監督信號。
- **Open-domain QA SOTA**：在 Natural Questions、WebQuestions、CuratedTrec 三個開放域 QA 任務上達到當時最優，優於參數式 seq2seq 模型和特定任務的 retrieve-and-extract 架構。
- **更好的語言生成品質**：相較於純參數 seq2seq baseline，RAG 生成的文本更具體、多元且真實。
- **可更新知識**：非參數記憶（向量索引）可直接替換以更新模型的世界知識，無需重新訓練。
- **歷史意義**：RAG 是現代 LLM 應用中最廣泛採用的知識增強範式，直接影響了後續所有 RAG 系統的設計。

## 論文全文

**Title**: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
**Authors**: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
**Affiliations**: Facebook AI Research; University College London; New York University
**arXiv ID**: 2005.11401 (v4, revised 2021-04-12)
**Published**: 2020-05-22
**Venue**: NeurIPS 2020
**URL**: https://arxiv.org/abs/2005.11401
**Code**: https://github.com/huggingface/transformers (RAG implementation)

### Full Abstract

Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, and another which can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state of the art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

### 1 Introduction

Pre-trained neural language models have been shown to learn a substantial amount of in-depth knowledge from data. They can do so without any access to an external memory, as a parameterized implicit knowledge base. While this development is exciting, such models do have downsides: They cannot easily expand or revise their memory, can't straightforwardly provide insight into their predictions, and may produce "hallucinations."

Hybrid models that combine parametric memory with non-parametric (i.e., retrieval-based) memories can address some of these issues because knowledge can be directly revised and expanded, and accessed knowledge can be inspected and interpreted. REALM and ORQA, two recently introduced models that combine masked language models with a differentiable retriever, have shown promising results, but have only explored open-domain extractive question answering.

Here, we bring hybrid parametric and non-parametric memory to the "workhorse of NLP," i.e. sequence-to-sequence (seq2seq) models. We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We combine these components in a probabilistic model trained end-to-end.

### 2 Methods

RAG models use the input sequence x to retrieve text documents z and use them as additional context when generating the target sequence y. Our models leverage two components:

1. **Retriever** p_η(z|x): Parameters η that return (top-K truncated) distributions over text passages given a query x
2. **Generator** p_θ(y_i|x,z,y_`{1:i-1}`): Generates current token based on context of previous tokens, original input x, and retrieved passage z

#### 2.1 RAG-Sequence Model

Uses the same retrieved document to generate the complete sequence. Retrieves top K documents, generator produces output sequence probability for each document, then marginalizes:

```
p_RAG-Sequence(y|x) ≈ Σ_{z ∈ top-k} p_η(z|x) · p_θ(y|x,z)
```

#### 2.2 RAG-Token Model

Can draw a different latent document for each target token and marginalize accordingly. This allows the generator to choose content from several documents when producing an answer:

```
p_RAG-Token(y|x) ≈ Π_i Σ_{z ∈ top-k} p_η(z|x) · p_θ(y_i|x,z,y_{1:i-1})
```

#### 2.3 Retriever: DPR

The retrieval component is based on DPR (Dense Passage Retriever). DPR follows a bi-encoder architecture using BERT-based encoders for both documents and queries. Top-k retrieval is a Maximum Inner Product Search (MIPS) problem, approximately solved in sub-linear time using FAISS.

We use a pre-trained bi-encoder from DPR to initialize our retriever and build the document index (referred to as non-parametric memory).

#### 2.4 Generator: BART

The generator component is BART-large, a pre-trained seq2seq transformer with 400M parameters. To combine the input x with the retrieved content z, we simply concatenate them. BART was pre-trained using a denoising objective and achieves state-of-the-art results on a diverse set of generation tasks.

#### 2.5 Training

We jointly train the retriever and generator components without any direct supervision on what document should be retrieved. We minimize the negative marginal log-likelihood of each target using Adam. We keep the document encoder fixed and only fine-tune the query encoder and the BART generator.

#### 2.6 Decoding

- **RAG-Token**: Standard autoregressive seq2seq decoding via beam search.
- **RAG-Sequence**: Run beam search for each retrieved document z separately, yielding hypothesis set Y. Use "Thorough Decoding" (additional forward passes) or "Fast Decoding" (approximation) to estimate marginal probabilities.

### 3 Experiments

**Document index**: December 2018 Wikipedia dump split into 21M disjoint 100-word chunks. Document embeddings computed with DPR encoder, indexed with FAISS HNSW.

#### 3.1 Open-domain Question Answering

Evaluated on Natural Questions (NQ), TriviaQA (TQA), WebQuestions (WQ), and CuratedTrec (CT). RAG sets the state of the art on NQ, WQ, and CT, outperforming both:
- Extractive QA approaches (retrieve then extract spans)
- "Closed-Book QA" (pure parametric, no retrieval)

On TriviaQA, RAG strongly outperforms T5 and approaches pipeline systems that use gold passages.

#### 3.2 Abstractive Question Answering

Evaluated on MS-MARCO NLG task without using supplied gold passages. RAG generates more fluent, factual answers compared to pure parametric baselines. Some questions require real-time information (weather, prices) that cannot be answered from Wikipedia alone—RAG falls back on parametric knowledge.

#### 3.3 Jeopardy Question Generation

Novel task: given an answer entity (e.g., "The World Cup"), generate the corresponding Jeopardy question. RAG generates more specific, factual, and diverse questions than BART baseline. Human evaluation confirms RAG outputs are more factual.

#### 3.4 Fact Verification (FEVER)

RAG achieves results within 4.3% of state-of-the-art pipeline models that use strong retrieval supervision, despite being trained end-to-end without retrieval supervision.

#### 3.5 Knowledge Updatability

Demonstrates that replacing the non-parametric memory (document index) updates the model's knowledge without retraining. This is a key advantage over purely parametric models.

### 4 Related Work

- **Extractive QA with retrieval**: DPR, ORQA, REALM—focused on extractive span selection
- **Parametric knowledge**: T5, GPT-2/3—store knowledge in weights, cannot easily update
- **Memory-augmented networks**: Memory networks, stack-augmented networks—train from scratch
- **RAG novelty**: First to combine pre-trained parametric (BART) and non-parametric (DPR index) memory for generative NLP with end-to-end training

### 5 Conclusion

RAG models combine the best of parametric and non-parametric memory for NLP. They set state-of-the-art on open-domain QA tasks, generate more specific and factual language than pure parametric models, and allow knowledge updates by replacing the document index. RAG is a general-purpose framework applicable to any seq2seq task.

The framework has become the foundational blueprint for modern LLM knowledge augmentation systems, with adaptations in virtually every production RAG pipeline (LangChain, LlamaIndex, etc.).

**Key results summary**:
- NQ Exact Match: RAG-Token 44.5% vs. DPR 41.5% vs. T5-11B 34.5%
- TQA EM (wiki): RAG-Sequence 56.8% vs. T5-11B 37.4%
- MS-MARCO BLEU-1: RAG 45.1% vs. BART 43.1%
- FEVER label accuracy: RAG 74.3% vs. pipeline SOTA 78.3%
