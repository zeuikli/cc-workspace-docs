---
url: "https://arxiv.org/abs/2301.12597"
title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
archived_date: 2026-06-09
arxiv_id: 2301.12597
authors: ["Junnan Li", "Dongxu Li", "Silvio Savarese", "Steven Hoi"]
pdf_path: pdfs/2301.12597.pdf
published_date: 2023-01-01
---

# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

**Authors:** Junnan Li, Dongxu Li, Silvio Savarese, Steven Hoi
**Year:** 2023
**Venue:** ICML 2023
**ArXiv:** https://arxiv.org/abs/2301.12597

---

## Abstract

The cost of vision-and-language pre-training has become increasingly prohibitive due to end-to-end training of large-scale models. To this end, we propose BLIP-2, a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models. BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre-trained in two stages. The first stage bootstraps vision-language representation learning from a frozen image encoder. The second stage bootstraps vision-to-language generative learning from a frozen language model. BLIP-2 achieves state-of-the-art performance on various vision-language tasks, despite having significantly fewer trainable parameters than existing methods. For example, our model outperforms Flamingo80B by 8.7% on zero-shot VQAv2 with 54x fewer trainable parameters. We also demonstrate the model's emerging capabilities of zero-shot image-to-text generation guided by a natural language instruction.

---

## Key Contributions

- **Q-Former (Querying Transformer)**: a lightweight transformer with a fixed set of learnable query tokens that bridges a frozen vision encoder and a frozen LLM, extracting the most task-relevant visual features for language generation
- **Two-stage pre-training**: Stage 1 aligns Q-Former queries with a frozen vision encoder via image-text contrastive learning, image-grounded text generation, and image-text matching; Stage 2 connects Q-Former output to a frozen LLM via a linear projection for generative vision-language learning
- Outperforms **Flamingo80B by 8.7% on zero-shot VQAv2** with **54x fewer trainable parameters** (~188M vs. ~10B trainable), demonstrating extreme parameter efficiency
- Demonstrates **emerging zero-shot image-to-text generation** capabilities guided by natural language instructions, without explicit instruction-following training
- **ICML 2023** — Q-Former architecture established a highly influential connector paradigm adopted by InstructBLIP, MiniGPT-4, X-LLM, and many subsequent multimodal models
- Shows that independently bootstrapping each modality bridge (vision→Q-Former, then Q-Former→LLM) is more sample-efficient than joint end-to-end training
- Compatible with any combination of frozen vision encoder (ViT-L, ViT-g) and frozen LLM (OPT, FlanT5), making it a modular and future-proof architecture

---

## Methodology

BLIP-2's central innovation is the Q-Former: a transformer module with N learnable query tokens (N=32) that interact with image features via cross-attention and with each other via self-attention. The query tokens serve as a compressed, task-oriented visual representation — they learn to extract the image information most relevant to language understanding. A key design choice is weight-sharing between the query self-attention and the text self-attention in the Q-Former, enabling the queries to condition on text context.

**Stage 1 — Representation Learning from Frozen Vision Encoder:** The Q-Former is trained with three objectives simultaneously: (a) Image-Text Contrastive Learning (ITC) aligns query representations with text via contrastive loss across a batch; (b) Image-grounded Text Generation (ITG) trains queries to provide sufficient visual context for the Q-Former's transformer decoder to generate the paired text; (c) Image-Text Matching (ITM) trains a binary classifier on query outputs to distinguish matched vs. unmatched image-text pairs. The vision encoder (ViT-L/14 or ViT-g/14) is frozen throughout.

**Stage 2 — Generative Learning from Frozen LLM:** The 32 output query tokens from Stage 1 are linearly projected to match the LLM's embedding dimension and prepended to the text input embeddings. For decoder-only LLMs (OPT family), a language modeling loss is used; for encoder-decoder LLMs (FlanT5 family), a prefix language modeling loss is applied. Only the linear projection and Q-Former parameters are updated; the LLM remains entirely frozen. This stage effectively teaches the LLM to interpret compressed visual tokens as a soft visual prefix.

---

## Main Results

| Benchmark | BLIP-2 | Flamingo80B | Improvement |
|-----------|--------|-------------|-------------|
| Zero-shot VQAv2 | 65.0% | 56.3% | +8.7% |
| Zero-shot NoCaps | 121.6 CIDEr | — | SOTA |
| Zero-shot COCO Cap. | 145.8 CIDEr | 138.1 | +7.7 |
| Trainable params | ~188M | ~10B | 54x fewer |

BLIP-2 achieves SOTA on zero-shot VQA, image captioning (NoCaps, COCO), and visual reasoning benchmarks while training only a small fraction of its total parameter count.

---

## Limitations & Future Work

- Q-Former's 32 query tokens may be insufficient for tasks requiring fine-grained spatial reasoning or dense prediction (detection, segmentation)
- The two-stage training is sequential and decoupled; misalignment between what Stage 1 learns and what the LLM needs in Stage 2 can limit performance
- Both vision encoder and LLM are frozen, preventing deep cross-modal representation learning — the model can only adapt visual features at the Q-Former level
- Zero-shot instruction following is emergent but unreliable compared to explicitly instruction-tuned models (InstructBLIP addresses this)
- Hallucination in generated text remains a concern when visual evidence is weak or ambiguous

---

## Why This Matters for AI Practitioners

BLIP-2 solved a critical practical problem: **how to add vision to an existing LLM at minimal cost**. By freezing both the vision encoder and LLM and only training the Q-Former bridge (~188M parameters), practitioners can build capable multimodal systems without GPU clusters for end-to-end pre-training.

The modular design is particularly valuable: as better vision encoders (e.g., EVA-CLIP) or better LLMs (e.g., LLaMA-2, Mistral) become available, they can be swapped in with only the lightweight Q-Former needing retraining. This future-proofing, combined with strong zero-shot performance, made BLIP-2 a foundational architecture for the open-source multimodal ecosystem and directly spawned InstructBLIP (instruction-tuned variant), MiniGPT-4 (fine-tuned on curated conversations), and numerous domain-specific adaptations.
