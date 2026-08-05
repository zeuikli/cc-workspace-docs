---
url: "https://arxiv.org/abs/2204.14198"
title: "Flamingo: a Visual Language Model for Few-Shot Learning"
archived_date: 2026-06-09
arxiv_id: 2204.14198
authors: ["Jean-Baptiste Alayrac", "Jeff Donahue", "Pauline Luc", "Antoine Miech", "Iain Barr", "Yana Hasson", "Karel Lenc", "Arthur Mensch", "Katie Millican", "Malcolm Reynolds", "Roman Ring", "Eliza Rutherford", "Serkan Cabi", "Tengda Han", "Zhitao Gong", "Sina Samangooei", "Marianne Monteiro", "Jacob Menick", "Sebastian Borgeaud", "Andrew Brock", "Aida Nematzadeh", "Sahand Sharifzadeh", "Mikolaj Binkowski", "Ricardo Barreira", "Oriol Vinyals", "Andrew Zisserman", "Karen Simonyan"]
pdf_path: pdfs/2204.14198.pdf
published_date: 2022-01-01
---

# Flamingo: a Visual Language Model for Few-Shot Learning

**Authors:** Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, Karen Simonyan
**Year:** 2022
**Venue:** NeurIPS 2022
**ArXiv:** https://arxiv.org/abs/2204.14198

---

## Abstract

Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research. We introduce Flamingo, a family of Visual Language Models (VLM) with this ability. We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs. Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities. We demonstrate that Flamingo models achieve new state-of-the-art few-shot results across a wide range of open-ended visual and language tasks including visual question-answering, captioning, and others.

---

## Key Contributions

- **Novel Perceiver Resampler architecture** converting variable-size visual features from a frozen vision encoder into a fixed number of visual tokens for efficient LLM ingestion regardless of input resolution or video frame count
- **Gated cross-attention dense layers** inserted between frozen LLM transformer blocks enable vision-language integration while preserving pre-trained language capabilities — the gating mechanism allows the model to learn when to attend to visual context
- **First large-scale multimodal model capable of in-context few-shot learning** on interleaved image-text sequences, analogous to GPT-3's text-only few-shot ability
- **Pre-training on billions of web-scraped image-text pairs** (ALIGN, LTIP, VTP datasets) at scale establishes the importance of diverse, naturally-occurring multimodal web data
- **NeurIPS 2022** — seminal architecture that directly influenced BLIP-2, OpenFlamingo, Otter, and the broader frozen-LLM connector paradigm
- Demonstrated strong performance across both open-ended generation tasks (captioning, VQA) and classification-style tasks using a unified architecture
- Showed that frozen large language models can acquire visual grounding without degrading language capabilities when connected via carefully designed cross-attention modules

---

## Methodology

Flamingo's architecture consists of three main components: a frozen pre-trained vision encoder (NFNet), a Perceiver Resampler, and a frozen large language model (Chinchilla) augmented with interleaved gated cross-attention layers. The vision encoder processes images or video frames into dense feature grids. The Perceiver Resampler then compresses these variable-length visual features into a fixed set of 64 visual tokens via learned queries attending to the visual features — this is the key efficiency innovation allowing the LLM to process any image regardless of resolution.

The gated cross-attention layers are inserted at fixed intervals within the frozen LLM's transformer stack. Each such layer allows the text stream to attend over the visual tokens from the most recently preceding image in the interleaved sequence. A learned tanh-gated residual connection initializes with zero weight, ensuring the frozen LLM's behavior is preserved at initialization and visual influence is introduced gradually during training.

Pre-training uses a mixture of datasets at different scales: ALIGN (1.8B image-text pairs scraped from the web with alt-text), LTIP (Long Text & Image Pairs, 312M higher-quality pairs), and VTP (Video & Text Pairs, 27M short video clips). The interleaved image-text format is sourced from MultiModal MassiveWeb (M3W), a 43M document web corpus preserving natural interleaving of images within text. Only the cross-attention layers and Perceiver Resampler are trained; both the vision encoder and LLM remain frozen.

---

## Main Results

| Task | Flamingo Setting | Performance |
|------|-----------------|-------------|
| VQAv2 | 4-shot | 56.3% (SOTA few-shot at time) |
| COCO Captioning | 4-shot | 84.3 CIDEr |
| NExT-QA | 4-shot | 51.7% |
| VATEX (video captioning) | 4-shot | 36.4 CIDEr |

Flamingo (80B parameters) outperformed prior SOTA on 6 of 16 benchmarks with just 4 in-context examples, sometimes surpassing fine-tuned models that used thousands of labeled examples.

---

## Limitations & Future Work

- All parameters except cross-attention layers are frozen, limiting the model's ability to deeply integrate visual knowledge into its representations
- The Perceiver Resampler compresses visual information into 64 tokens, which may lose fine-grained spatial detail needed for tasks like counting or precise localization
- Few-shot performance is bounded by the LLM's language priors — the model can "hallucinate" plausible but visually incorrect answers
- Pre-training data quality is noisy (web-scraped); image-text alignment is imperfect
- Compute cost of 80B parameter model limits accessibility; subsequent works (OpenFlamingo, BLIP-2) addressed this with smaller, more efficient designs

---

## Why This Matters for AI Practitioners

Flamingo proved that **large frozen language models can be efficiently extended to vision through lightweight architectural additions**, rather than expensive end-to-end multimodal pre-training. The key insight — insert cross-attention bridges while keeping both vision encoder and LLM frozen — dramatically reduces training cost and preserves language capabilities.

The in-context few-shot learning ability is particularly valuable for practitioners: you can adapt Flamingo to a new visual task with just a handful of examples in the prompt, with no fine-tuning required. This mirrors how practitioners use GPT-3/4 for NLP tasks and extends that paradigm to vision. The Perceiver Resampler and gated cross-attention patterns became architectural blueprints for BLIP-2's Q-Former and numerous subsequent multimodal systems.
