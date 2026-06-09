---
url: "https://arxiv.org/abs/2406.07524"
title: "Simple and Effective Masked Diffusion Language Models"
archived_date: 2026-06-09
arxiv_id: 2406.07524
authors: ["Subham Sekhar Sahoo", "Marianne Arriola", "Yair Schiff", "Aaron Gokaslan", "Edgar Marroquin", "Justin T Chiu", "Alexander Rush", "Volodymyr Kuleshov"]
published_date: 2024-01-01
---

# Simple and Effective Masked Diffusion Language Models

**Authors:** Subham Sekhar Sahoo, Marianne Arriola, Yair Schiff, Aaron Gokaslan, Edgar Marroquin, Justin T Chiu, Alexander Rush, Volodymyr Kuleshov
**Year:** 2024 (submitted June 11, 2024; revised November 10, 2024)
**Venue:** NeurIPS 2024
**ArXiv:** https://arxiv.org/abs/2406.07524

---

## Abstract

The authors demonstrate that masked discrete diffusion outperforms previous expectations for language modeling. They introduce an optimized training methodology and derive a simplified, Rao-Blackwellized objective that results in additional improvements. The approach combines classical masked language modeling losses and enables encoder-only models with efficient samplers capable of generating arbitrary text lengths semi-autoregressively. Results show masked diffusion models achieve state-of-the-art performance among diffusion approaches while approaching autoregressive baselines on standard benchmarks. The SUBS (substitution-based) parameterization simplifies the absorbing state diffusion loss to a mixture of classical masked language modeling losses.

---

## Key Contributions

- Introduces MDLM with a novel SUBS parameterization that reduces the absorbing-state diffusion loss to a weighted mixture of masked language modeling (MLM) cross-entropy losses, connecting diffusion training to classical BERT-style objectives
- Derives a simplified Rao-Blackwellized training objective that yields additional perplexity improvements over prior discrete diffusion methods by reducing variance in the gradient estimates
- Proposes an improved training recipe incorporating modern engineering practices (learning rate schedules, architecture choices, data processing) enabling SOTA perplexity among diffusion models on LM1B and OpenWebText benchmarks
- Enables semi-autoregressive text generation of arbitrary lengths using encoder-only (BERT-style) architectures, without requiring a decoder or left-to-right generation constraint
- Demonstrates masked diffusion LMs approaching autoregressive model perplexity within 15-25%, closing a major quality gap that had previously made diffusion models impractical for language generation tasks
- Releases code and tutorial resources enabling reproducible training and evaluation of masked diffusion language models

---

## Methodology

MDLM is built on absorbing-state discrete diffusion, where the forward process gradually masks tokens until all are replaced by a special [MASK] token. The key theoretical contribution is the SUBS (substitution-based) parameterization, which reformulates the reverse process objective. Rather than requiring a complex diffusion-specific loss, SUBS shows that the ELBO decomposes into a time-weighted sum of standard masked language modeling cross-entropy losses — one for each noise level. This unification means practitioners can train masked diffusion models using the same infrastructure as BERT, with the only change being a continuous noise schedule over masking rates.

The Rao-Blackwellized objective further improves training by analytically marginalizing out certain random variables in the loss, reducing gradient variance without introducing bias. The training recipe adopts practices from modern autoregressive LM training: careful tokenization, cosine learning rate schedules, gradient clipping, and scaled-up compute budgets. Together these engineering choices had not been applied systematically to diffusion LMs before this work, and their combination accounts for a significant portion of the performance gain over prior methods.

At inference, MDLM uses an efficient sampler that begins with a fully masked sequence and iteratively unmasks tokens. The semi-autoregressive generation capability allows producing outputs of arbitrary length by chunking the sequence, enabling the model to scale beyond fixed context windows — a practical advantage over continuous diffusion approaches that require a predetermined output dimensionality.

---

## Main Results

- Achieves state-of-the-art perplexity among diffusion language models on LM1B and OpenWebText benchmarks
- Approaches autoregressive model perplexity within 15-25%, the smallest gap reported for any diffusion LM at time of publication
- Outperforms prior discrete diffusion baselines (including D3PM, MDLM predecessors) by substantial margins attributable to the Rao-Blackwellized objective and improved training recipe
- Semi-autoregressive generation produces coherent long-form text, demonstrating practical applicability beyond fixed-length synthetic tasks
- Encoder-only architecture is parameter-efficient compared to autoregressive decoder models of comparable capability

---

## Limitations & Future Work

- A 15-25% perplexity gap versus autoregressive models remains, suggesting diffusion LMs have not yet fully matched AR quality on standard benchmarks
- Semi-autoregressive generation introduces a chunking hyperparameter that requires tuning for different tasks and output lengths
- Training cost is comparable to autoregressive models but inference requires multiple forward passes (one per denoising step), which can be slower than single-pass AR decoding depending on the number of sampling steps chosen
- Future work includes scaling to larger model sizes and datasets, reducing the perplexity gap further, and applying the approach to conditional generation tasks such as translation and summarization

---

## Why This Matters for AI Practitioners

MDLM is significant because it rehabilitates masked diffusion as a serious language modeling paradigm after years in which autoregressive models dominated. By connecting diffusion training to the well-understood masked language modeling objective (BERT), it lowers the barrier for practitioners already familiar with transformer pre-training infrastructure. The SUBS parameterization is a clean theoretical result: if you know how to train BERT, you essentially know how to train MDLM. The semi-autoregressive generation capability is practically useful for applications requiring variable-length generation, text infilling, or controllable editing — tasks where left-to-right AR models are structurally disadvantaged. For teams exploring alternatives to autoregressive generation for latency-sensitive or controllability-focused applications, MDLM provides a well-engineered starting point with documented training recipes and open-source code.
