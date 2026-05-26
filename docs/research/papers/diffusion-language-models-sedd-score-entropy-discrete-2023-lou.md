# Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution

**Authors:** Aaron Lou, Chenlin Meng, Stefano Ermon
**Year:** 2023 (submitted October 25, 2023; published as ICML 2024 Oral)
**Venue:** ICML 2024 (Oral presentation)
**ArXiv:** https://arxiv.org/abs/2310.16834

---

## Abstract

This paper addresses fundamental limitations of diffusion models in discrete domains like natural language. The authors introduce score entropy, a novel loss that naturally extends score matching to discrete spaces. Their Score Entropy Discrete Diffusion (SEDD) model significantly boosts performance on standard language modeling tasks: it reduces perplexity by 25-75% compared to existing language diffusion paradigms and is competitive with autoregressive models, in particular outperforming GPT-2. SEDD further enables high-quality generation with 32x fewer network evaluations and supports infilling and alternative prompting strategies beyond left-to-right decoding.

---

## Key Contributions

- Proposes score entropy as a principled and novel extension of score matching theory to discrete data spaces, bridging a key theoretical gap that prevented clean application of score-based generative modeling to language
- Introduces SEDD (Score Entropy Discrete Diffusion) that reduces language modeling perplexity by 25-75% over prior discrete diffusion models, the largest single-paper improvement reported at time of publication
- Achieves competitive or superior performance versus GPT-2 on standard language modeling benchmarks, the first discrete diffusion model to match a widely-used autoregressive baseline
- Enables 32x more efficient sampling through fewer network evaluations, making discrete diffusion practically competitive with AR decoding for the first time
- Supports controllable generation including infilling, alternative prompting strategies, and non-left-to-right decoding without retraining or architectural modification
- Accepted as ICML 2024 Oral, cementing SEDD as a foundational reference for discrete diffusion language modeling

---

## Methodology

The core theoretical contribution is score entropy, a loss function designed to train discrete diffusion models analogously to how score matching trains continuous diffusion models. In continuous spaces, score matching trains a model to estimate the gradient of the log data density (the score), enabling denoising via Langevin dynamics. This gradient is well-defined for continuous distributions but undefined for discrete ones. Score entropy resolves this by working instead with ratios of the data distribution — specifically, the ratios p(x) / p(y) for pairs of discrete states x and y — which are well-defined even for categorical distributions. The score entropy loss trains the model to estimate these ratios, and the Kolmogorov equations for discrete Markov chains provide the theoretical foundation for converting ratio estimates into a generative denoising process.

SEDD uses a continuous-time discrete Markov chain as the forward process, where transitions corrupt tokens at a time-varying rate. The reverse process, trained via score entropy, learns to undo these corruptions. The noise schedule and transition kernels are designed to be compatible with efficient ancestral sampling, enabling generation via sequential denoising steps. The 32x sampling efficiency gain comes from the model's ability to jointly denoise multiple tokens per step — unlike continuous diffusion which must take many small Euler-Maruyama steps, SEDD's discrete transitions are coarser and allow larger effective strides through the denoising trajectory.

For controllable generation, SEDD's non-causal architecture is directly exploited: infilling is handled by conditioning on observed tokens and denoising only masked positions, with no architectural changes required. This is a structural advantage over AR models, which require specialized training procedures (fill-in-the-middle objectives) or heuristic approximations (running generation in multiple passes) to support infilling.

---

## Main Results

- Reduces perplexity by 25-75% over prior discrete diffusion baselines (D3PM, Multinomial Diffusion, and related methods) on standard language modeling benchmarks
- Outperforms GPT-2 on text8 and other standard language modeling benchmarks, the first discrete diffusion model to surpass this autoregressive baseline
- Achieves 32x reduction in network evaluations relative to prior diffusion methods while maintaining or improving output quality
- Infilling quality matches or exceeds specialized infilling models on standard cloze and text completion tasks
- Supports arbitrary-length generation without requiring a fixed output length specification at inference time

---

## Limitations & Future Work

- Despite closing the gap significantly, SEDD does not match the largest state-of-the-art autoregressive models (e.g., GPT-3/GPT-4 scale); the comparison to GPT-2 is a proof-of-concept rather than a production-scale evaluation
- Score entropy training is theoretically motivated but the computational cost per training step is higher than standard cross-entropy MLM training, which may limit scaling
- The 32x efficiency gain is measured relative to prior diffusion methods, not relative to a single-pass AR decoder; AR generation remains faster in absolute wall-clock time for the same output length
- Theoretical analysis assumes the data distribution satisfies regularity conditions that may not hold for all language distributions; practical performance on highly structured domains (code, formal languages) requires further study
- Future work includes scaling to larger models, applying score entropy to other discrete modalities (protein sequences, code), and developing better noise schedules for language-specific token distributions

---

## Why This Matters for AI Practitioners

SEDD is important because it provides a theoretically principled foundation for discrete diffusion that was previously missing. Prior discrete diffusion models for language were largely heuristic — they adapted continuous diffusion recipes without a clean theoretical justification for the discrete setting. Score entropy fills this gap: it is to discrete diffusion what score matching is to continuous diffusion, giving researchers a principled objective to optimize and a theoretical framework for reasoning about model behavior. The ICML 2024 Oral recognition reflects the community's view that this is a foundational result, not an incremental improvement. For practitioners, the key practical takeaways are: (1) the 32x sampling efficiency gain makes discrete diffusion LMs faster to deploy than expected; (2) infilling and non-left-to-right generation are first-class capabilities, not add-ons; and (3) SEDD's score entropy framework is extensible to other discrete modalities beyond text, making it relevant for practitioners working on protein design, code generation, or any domain with discrete structured outputs.
