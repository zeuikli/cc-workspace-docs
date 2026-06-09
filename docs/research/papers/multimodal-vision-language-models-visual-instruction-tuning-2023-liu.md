---
url: "https://arxiv.org/abs/2304.08485"
title: "Visual Instruction Tuning"
archived_date: 2026-06-09
arxiv_id: 2304.08485
authors: ["Haotian Liu", "Chunyuan Li", "Qingyang Wu", "Yong Jae Lee"]
published_date: 2023-01-01
---

# Visual Instruction Tuning

**Authors:** Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee
**Year:** 2023
**Venue:** NeurIPS 2023 (Oral)
**ArXiv:** https://arxiv.org/abs/2304.08485

---

## Abstract

In this paper, we present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on such generated data, we introduce LLaVA (Large Language and Vision Assistant): an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding. Our early experiments show that LLaVA demonstrates impressive multimodel chat abilities, sometimes exhibiting the behaviours of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset. When fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%. We make GPT-4 generated visual instruction tuning data, our model and code base publicly available.

---

## Key Contributions

- **First use of language-only GPT-4 to generate multimodal language-image instruction-following data**, establishing a new paradigm for visual instruction tuning that sidesteps costly human annotation
- **LLaVA architecture** connecting CLIP ViT-L/14 vision encoder with Vicuna LLM via a trainable linear projection layer for end-to-end multimodal understanding
- Achieves **85.1% relative score vs. GPT-4** on a synthetic multimodal instruction-following benchmark and **92.53% on ScienceQA** (SOTA at time of publication)
- **Open-source release** of generated instruction data, model weights, and training code enabling broad community research and reproducibility
- **NeurIPS 2023 Oral** — demonstrated that instruction-tuned multimodal models trained on synthetic data can rival closed-source systems
- Pioneered the concept of converting image-text pairs into instruction-following format using a capable language model as the data generator
- Established the viability of simple connector modules (linear projection) between off-the-shelf vision and language backbones

---

## Methodology

LLaVA connects a pre-trained CLIP visual encoder (ViT-L/14) with a large language model (Vicuna) through a trainable linear projection matrix. The vision encoder produces visual features from an input image, which are projected into the LLM's word embedding space. This allows the LLM to treat visual tokens identically to text tokens during generation.

The key innovation in data generation is using GPT-4 (text-only) to convert image-text pairs (sourced from CC3M/COCO captions) into instruction-following format. By providing GPT-4 with image captions and detected bounding box annotations as text context, the authors prompt it to generate conversational QA pairs, detailed descriptions, and complex reasoning questions — three data types that cover a spectrum from factual to open-ended visual understanding.

Training proceeds in two stages: (1) pre-training where only the projection layer is updated to align visual features with LLM token embeddings using filtered CC-595K image-text pairs, and (2) fine-tuning end-to-end (projection + LLM, vision encoder frozen) on the 158K generated instruction-following data plus ScienceQA for task-specific scenarios.

---

## Main Results

| Benchmark | LLaVA Score |
|-----------|-------------|
| Synthetic multimodal instruction-following (vs. GPT-4) | 85.1% relative |
| ScienceQA (with GPT-4 judge) | 92.53% accuracy (SOTA) |

LLaVA exhibits emergent multimodal chat behaviors on unseen images, including detailed scene description, OCR-level reading, and multi-step visual reasoning — capabilities not explicitly trained for but arising from instruction tuning on diverse synthetic data.

---

## Limitations & Future Work

- The linear projection connector is simple; more expressive connectors may better bridge the visual-language gap (addressed in LLaVA-1.5)
- Instruction data quality is bounded by the text-only GPT-4's ability to reason from captions/boxes rather than actual image pixels
- Hallucination remains a known failure mode when visual evidence is ambiguous or absent
- Evaluation benchmarks at time of publication were limited; subsequent work developed more rigorous multimodal benchmarks (MMBench, MME, etc.)
- The 7B/13B scale may be insufficient for tasks requiring deep world knowledge or fine-grained visual reasoning

---

## Why This Matters for AI Practitioners

LLaVA established that **high-quality synthetic instruction data can bootstrap competitive multimodal models** without expensive human annotation pipelines. The architecture (vision encoder → lightweight connector → frozen/fine-tuned LLM) became the dominant paradigm for open-source multimodal models. The open release directly enabled a wave of follow-on work (LLaVA-1.5, InstructBLIP, MiniGPT-4) and established reproducible baselines the community could build on.

For practitioners, LLaVA demonstrates: (1) GPT-4 as a scalable data labeler for domains where annotation is expensive, (2) the power of instruction tuning over simple captioning objectives, and (3) that simple connector modules between strong frozen backbones are a practical and efficient path to multimodal capability.
