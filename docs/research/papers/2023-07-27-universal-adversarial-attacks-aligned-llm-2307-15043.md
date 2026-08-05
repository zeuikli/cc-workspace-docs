---
url: "https://arxiv.org/abs/2307.15043"
title: "Universal and Transferable Adversarial Attacks on Aligned Language Models"
archived_date: 2026-06-09
arxiv_id: 2307.15043
authors: ["Andy Zou", "Zifan Wang", "Nicholas Carlini", "Milad Nasr", "J. Zico Kolter", "Matt Fredrikson"]
pdf_path: pdfs/2307.15043.pdf
published_date: 2023-01-01
---

# Universal and Transferable Adversarial Attacks on Aligned Language Models

**Authors:** Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, Matt Fredrikson

**Year:** 2023

**Venue:** arXiv preprint (widely cited; presented at NeurIPS 2023 workshops)

**ArXiv:** https://arxiv.org/abs/2307.15043

**Code:** https://github.com/llm-attacks/llm-attacks

---

## Full Abstract

Although large language models (LLMs) are trained to refuse harmful requests, we show that they remain vulnerable to adversarial attacks that automatically generate suffixes which, when appended to queries, cause aligned language models to generate objectionable behaviors. Unlike prior work relying on manual prompt engineering, we propose an automated approach that uses greedy and gradient-based search techniques to produce adversarial suffixes. A key insight is that training on multiple harmful queries and model architectures simultaneously produces attacks that are broadly effective and transfer to diverse models. Concretely, we show that suffixes generated on Vicuna-7B and Vicuna-13B transfer to GPT-3.5, GPT-4, PaLM-2, Claude, and LLaMA-2-Chat, demonstrating that white-box-optimized attacks can compromise black-box, closed-source production systems. We release code enabling the community to study adversarial robustness in LLMs and develop defenses.

---

## Key Contributions

- **GCG (Greedy Coordinate Gradient) attack:** Introduced an automated token-level optimization method that produces adversarial suffixes by combining greedy token search with gradient-guided candidate ranking — requiring no manual prompt engineering.
- **Cross-model transferability:** Demonstrated that adversarial suffixes optimized on open-source Vicuna models successfully jailbreak closed-source systems including ChatGPT (GPT-3.5 and GPT-4), Google Bard (PaLM-2), and Claude, challenging the assumption that closed APIs are robustly protected.
- **Multi-model, multi-prompt training:** Showed that optimizing a single suffix against multiple harmful queries and multiple model architectures simultaneously produces broadly effective, generalizable attacks rather than instance-specific exploits.
- **Alignment robustness challenge:** Provided compelling empirical evidence that RLHF-based alignment does not constitute robust inference-time safety — a misaligned suffix of ~20 tokens can consistently elicit harmful outputs from aligned models.
- **Open research infrastructure:** Released code and attack artifacts, seeding a large body of follow-on work on adversarial robustness, defense mechanisms, and red teaming automation.
- **Systematic harmful behavior elicitation:** Demonstrated attack effectiveness across a curated set of harmful behaviors spanning weapons, cyberattacks, and dangerous instructions — establishing a de facto evaluation protocol later formalized by HarmBench.

---

## Methodology

GCG operates on the token level, treating adversarial suffix generation as a discrete optimization problem. Given a harmful query and a target response prefix (e.g., "Sure, here is how to..."), the attack minimizes the negative log-likelihood of the target prefix by iteratively replacing suffix tokens. At each step, gradients of the loss with respect to one-hot token embeddings provide a ranked list of candidate replacements for each suffix position. A greedy beam search over these candidates selects replacements that most reduce loss, progressing token-by-token until the suffix reliably elicits the target behavior. The full optimization runs for several hundred steps and typically converges within minutes on a single GPU for 7B-parameter models.

Transferability is achieved through multi-model, multi-prompt training. Rather than optimizing a suffix for a single (query, model) pair, GCG trains on a batch of diverse harmful queries and aggregates gradients across multiple model architectures simultaneously. This forces the suffix to exploit representational features common across models rather than idiosyncratic artifacts of a single architecture, producing attacks that generalize to unseen models — including those for which no gradient access exists.

Black-box transfer evaluation appends the optimized suffix to harmful queries submitted via closed-source APIs. The key finding is that the transferred suffix retains sufficient adversarial force to overcome RLHF-trained refusal behaviors in production systems. The authors hypothesize that aligned models share a common latent geometry for refusal — and that suffixes learned to circumvent this geometry on open-source proxies carry over to closed-source systems trained on similar data distributions.

---

## Main Results

- GCG achieves near-100% Attack Success Rate (ASR) on Vicuna-7B and Vicuna-13B across the harmful behavior benchmark with suffixes of ~20 tokens.
- Transferred suffixes achieve approximately 88% ASR on GPT-3.5, ~67% on GPT-4, and measurable ASR on Claude and PaLM-2 — all models the attack was never optimized against.
- Multi-model, multi-prompt training reduces ASR variance across transfer targets compared to single-model optimization.
- Naive defenses (e.g., perplexity filtering) partially mitigate GCG by detecting high-perplexity suffix tokens but introduce significant false-positive rates on legitimate queries.
- The attack is robust across harmful behavior categories: weapons synthesis, malware generation, social engineering, and dangerous instructions all yield high ASR.
- Longer optimization budgets (more steps, larger beam widths) monotonically improve ASR up to a saturation point, with diminishing returns beyond ~500 steps.

---

## Limitations and Future Work

- **Computational cost:** GCG requires white-box gradient access and multiple GPU hours per suffix, limiting adversarial suffix generation to researchers with access to open-source model weights and sufficient compute.
- **Perplexity artifacts:** GCG suffixes often contain unnatural token sequences that are detectable by perplexity filters, motivating more semantically natural attack variants (e.g., AutoDAN, PAIR).
- **Transfer reliability variance:** Transfer ASR to closed-source models shows high variance across harmful behavior categories and is not fully predictable from white-box results.
- **Adaptive defenses:** Defenses specifically trained to recognize or resist GCG-style token patterns can substantially reduce ASR; the arms race between attack and defense is ongoing.
- **Interpretability gap:** It remains poorly understood why specific suffix tokens elicit harmful outputs — mechanistic interpretability of adversarial suffixes is an open research direction.

---

## Why This Matters for AI Practitioners

GCG established that RLHF alignment is not equivalent to adversarial robustness — a distinction that has profound implications for deploying LLMs in safety-critical or public-facing contexts:

- **Deployment threat model:** Any publicly deployed LLM should be assumed potentially susceptible to adversarial suffix attacks, requiring defense-in-depth beyond alignment training alone.
- **Defense prioritization:** The paper motivated an entire class of defenses — input preprocessing, output monitoring, adversarial training — and demonstrated that naive heuristics (perplexity filtering) are insufficient.
- **Red teaming automation:** GCG is the foundational automated attack underpinning HarmBench and most subsequent red teaming frameworks; understanding it is prerequisite to evaluating the broader landscape.
- **Closed-source ≠ secure:** The transfer results shattered the assumption that API-only access to proprietary models provides robust safety guarantees, directly informing regulatory discussions around model release policies.
- **Benchmark design:** The multi-behavior harmful query set introduced here became an informal standard that HarmBench later formalized, making this paper foundational for safety evaluation methodology.
