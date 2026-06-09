---
url: "https://arxiv.org/abs/2502.09992"
title: "Large Language Diffusion Models"
archived_date: 2026-06-09
arxiv_id: 2502.09992
authors: ["Shen Nie", "Fengqi Zhu", "Zebin You", "Xiaolu Zhang", "Jingyang Ou", "Jun Hu", "Jun Zhou", "Yankai Lin", "Ji-Rong Wen", "Chongxuan Li"]
published_date: 2025-01-01
---

# Large Language Diffusion Models

**Authors:** Shen Nie, Fengqi Zhu, Zebin You, Xiaolu Zhang, Jingyang Ou, Jun Hu, Jun Zhou, Yankai Lin, Ji-Rong Wen, Chongxuan Li
**Year:** 2025 (submitted February 14, 2025)
**Venue:** Preprint (arXiv 2025); follow-up scaling work ongoing
**ArXiv:** https://arxiv.org/abs/2502.09992

---

## Abstract

LLaDA is a diffusion-based language model challenging the assumption that advanced language capabilities require autoregressive architectures. The model employs a forward data masking process and a reverse generation process, parameterized by a Transformer to predict masked tokens. Trained under a pre-training and supervised fine-tuning (SFT) paradigm, LLaDA 8B is competitive with strong LLMs like LLaMA3 8B in in-context learning and exhibits impressive instruction-following abilities. Notably, LLaDA addresses the reversal curse, surpassing GPT-4o on a reversal poem completion task. The findings show the promise of diffusion models for language modeling at scale and challenge the common assumption that core LLM capabilities inherently depend on autoregressive models.

---

## Key Contributions

- First large-scale (8B parameter) masked diffusion language model trained from scratch under a full pre-training + SFT paradigm, demonstrating that diffusion models can be trained at LLM scale without degrading to toy-scale demonstrations
- Demonstrates competitive performance with LLaMA3 8B across general in-context learning benchmarks, establishing a parity threshold that challenges the assumption that AR is necessary for capable language models
- Demonstrates diffusion models resolve the reversal curse — the well-documented failure of AR models to handle reversed text — outperforming GPT-4o on reversal poem completion due to bidirectional token dependency modeling
- Shows strong scalability across diverse task categories including general NLP, mathematics, and code generation benchmarks
- Establishes a likelihood-based optimization framework for large-scale diffusion LM training compatible with standard instruction tuning (SFT), making the training pipeline accessible to practitioners
- Spawned follow-up scaling work (LLaDA 2.0 with 16B and 100B MoE variants) validating the architecture's scalability beyond the initial 8B checkpoint

---

## Methodology

LLaDA adopts a masked discrete diffusion framework at scale. The forward process is a data masking schedule: tokens are progressively replaced with [MASK] tokens according to a noise schedule, until the sequence is fully masked at the terminal diffusion time. The reverse process is parameterized by a standard Transformer encoder, which takes the partially masked sequence and predicts the original tokens at each masked position. This bidirectional attention is the structural key: unlike autoregressive models that attend only to past tokens, LLaDA's Transformer sees the entire context (including future positions) when denoising any given token, enabling true bidirectional dependency modeling.

Pre-training follows the standard masked diffusion ELBO, which decomposes into a sum of masked language modeling losses at different noise levels — connecting the training objective to the BERT-style MLM loss. Supervised fine-tuning applies the same masked diffusion objective but on instruction-response pairs, treating the response tokens as the data to be denoised given the instruction as conditioning context. This is a natural extension that does not require any architectural changes, making LLaDA's SFT procedure straightforward to implement using existing instruction-tuning infrastructure.

The reversal curse result is particularly revealing about the architectural difference: AR models fail on reversed text because their left-to-right generation prior conflicts with reversed causal structure. LLaDA, generating all positions in parallel via denoising, has no directional prior and therefore handles forward and reverse text with equal facility. This is not a tuning artifact but a structural property of bidirectional masked diffusion.

---

## Main Results

- LLaDA 8B matches LLaMA3 8B on standard in-context learning benchmarks (general NLP tasks), closing the capability gap between diffusion and autoregressive models at the 8B scale
- Surpasses GPT-4o on reversal poem completion, a task where the reversal curse causes autoregressive models to fail systematically
- Shows competitive performance on mathematics benchmarks, suggesting diffusion models are not limited to surface-level pattern matching
- Code generation performance is competitive, validating applicability to structured output domains beyond natural language
- LLaDA 2.0 (16B and 100B MoE variants, follow-up work) demonstrates scaling laws continue to hold for masked diffusion architectures, with performance improving predictably with compute and parameters

---

## Limitations & Future Work

- Inference latency is higher than comparable AR models due to multi-step denoising; each generation requires multiple forward passes through the 8B Transformer
- The paper focuses on English; multilingual capabilities and performance on low-resource languages are not characterized
- Sampling efficiency (number of denoising steps required for high-quality output) requires further study; reducing steps without quality loss remains an open engineering problem
- Fine-grained reasoning tasks requiring long chains of step-by-step inference may still favor AR models due to their explicit sequential computation structure
- Future work includes RLHF alignment for diffusion LMs, further scaling (LLaDA 2.0), and efficient speculative decoding analogues for diffusion inference

---

## Why This Matters for AI Practitioners

LLaDA is arguably the most significant empirical challenge to the autoregressive paradigm since diffusion models emerged for images. The 8B-scale result matters because scale is where capabilities emerge: prior diffusion LM work at smaller scales could be dismissed as not representative. The reversal curse result has concrete implications for any application requiring non-left-to-right generation: text editing, infilling, constrained generation, and translation tasks where the target has different word order than the source. Practitioners building applications with controllability requirements (fill in the blank, edit the middle of a document, generate text satisfying suffix constraints) should treat LLaDA as a serious architectural alternative. The SFT compatibility also matters: teams with existing instruction-tuning pipelines can fine-tune LLaDA without significant infrastructure changes, lowering adoption cost.
