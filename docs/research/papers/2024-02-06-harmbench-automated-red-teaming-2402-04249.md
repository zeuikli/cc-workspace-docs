---
url: "https://arxiv.org/abs/2402.04249"
title: "HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal"
archived_date: 2026-06-09
arxiv_id: 2402.04249
authors: ["Mantas Mazeika", "Long Phan", "Xuwang Yin", "Andy Zou", "Zifan Wang", "Norman Mu", "Elham Sakhaee", "Nathaniel Li", "Steven Basart", "Bo Li", "David Forsyth", "Dan Hendrycks"]
pdf_path: pdfs/2402.04249.pdf
published_date: 2024-01-01
---

# HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

**Authors:** Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, David Forsyth, Dan Hendrycks

**Year:** 2024

**Venue:** ICML 2024

**ArXiv:** https://arxiv.org/abs/2402.04249

**Code:** https://github.com/centerforaisafety/HarmBench

---

## Full Abstract

Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify key properties previously unaccounted for in red teaming evaluations and systematically integrate these properties into HarmBench. Using HarmBench, we conduct a large-scale comparison of 18 red teaming methods and 33 target LLMs and defenses, yielding novel insights into the relative effectiveness of attacks and defenses. We also introduce a highly efficient adversarial training method that greatly enhances LLM robustness across a wide range of attacks, demonstrating how HarmBench enables codevelopment of attacks and defenses. We open source HarmBench at https://github.com/centerforaisafety/HarmBench.

---

## Key Contributions

- **First standardized red teaming benchmark:** HarmBench establishes reproducible, comparable safety evaluations for automated red teaming, filling a critical methodological gap in the field.
- **Four-category harm taxonomy:** Harmful behaviors are categorized into standard behaviors, contextual behaviors, copyright behaviors, and multimodal behaviors — each with distinct evaluation criteria and attack surface profiles.
- **Large-scale empirical comparison:** Comparative study of 18 red teaming methods against 33 target LLMs and defenses, yielding the most comprehensive systematic insights into attack-defense dynamics published to date.
- **Attack Success Rate (ASR) metrics:** Introduced robust ASR metrics using a fine-tuned LLaMA-2 classifier to judge harmful completions, reducing reliance on brittle string-matching heuristics.
- **Efficient adversarial training:** Developed an adversarial training method that significantly enhances LLM robustness across diverse attack types, demonstrating viable paths toward more resistant safety alignment.
- **Open-source ecosystem:** Released framework, datasets, and evaluation tooling enabling the community to co-develop attacks and defenses in a reproducible setting.
- **Novel cross-attack insights:** Revealed that no single attack dominates across all target models, and that defenses providing broad robustness against one attack class do not necessarily generalize to others.

---

## Methodology

HarmBench is structured around a modular evaluation pipeline that decouples attack generation, target model inference, and harm judgment. Attacks submit candidate completions to a shared judge model (a fine-tuned LLaMA-2 classifier), ensuring consistent harm detection across diverse attack strategies. This design allows 18 attack methods — spanning gradient-based approaches (GCG, AutoDAN), prompt optimization methods (PAIR, TAP), and human-engineered jailbreaks — to be compared on identical footing against the same target model and defense configurations.

The benchmark covers four functional categories of harmful behaviors. Standard behaviors are direct harmful requests (e.g., synthesis instructions for dangerous substances). Contextual behaviors require the model to produce harm only in specific conversational contexts. Copyright behaviors target verbatim reproduction of protected text. Multimodal behaviors involve image-conditioned attacks on vision-language models. This taxonomy ensures the benchmark captures the full breadth of real-world adversarial scenarios rather than collapsing all harm into a single dimension.

Adversarial training is implemented via R2D2 (Robust Refusal Dynamic Defense), which integrates GCG attack generation directly into the training loop. By continuously generating and training against fresh adversarial suffixes, R2D2 avoids the static adversarial training failure mode where robustness degrades when attackers adapt. The approach is computationally efficient relative to prior adversarial training proposals and achieves broad-spectrum robustness improvements.

---

## Main Results

- Across 18 attacks and 33 models, no single attack achieves universally high ASR; gradient-based attacks (GCG, AutoDAN) perform strongest against open-source models but transfer poorly to closed APIs.
- PAIR and TAP (LLM-as-attacker methods) achieve competitive ASR against closed-source models where gradients are unavailable.
- Defenses vary substantially in effectiveness: perplexity filtering reduces gradient-based attacks but is ineffective against semantically natural jailbreaks.
- R2D2 adversarial training achieves the largest robustness gains — over 90% ASR reduction on GCG attacks — while maintaining near-baseline performance on benign queries.
- Multimodal attacks (image-conditioned jailbreaks) exhibit higher baseline ASR than text-only attacks against vision-language models, highlighting an underexplored attack surface.
- Copyright and contextual behavior categories are substantially harder to defend than standard behaviors, suggesting that current safety training disproportionately targets the standard harm category.

---

## Limitations and Future Work

- **Static benchmark drift:** As models and attacks evolve, static benchmark behaviors may become unrepresentative of frontier risks; continuous benchmark updating is needed.
- **Judge model limitations:** The LLaMA-2 classifier judge can be fooled by obfuscated outputs that evade harm detection while still conveying harmful information.
- **Closed-model coverage:** Evaluation of closed-source models (GPT-4, Claude) is limited to black-box API access, precluding gradient-based attacks and full defense analysis.
- **Multimodal coverage:** Multimodal attack coverage is nascent; as vision-language models proliferate, broader multimodal harm taxonomies are needed.
- **Adversarial training scalability:** R2D2 training is evaluated at 7B–13B parameter scales; scaling behavior to frontier model sizes remains uncharacterized.

---

## Why This Matters for AI Practitioners

HarmBench is the field's first credible attempt to bring benchmark rigor to red teaming — a domain that previously relied on ad hoc, incomparable evaluations. For practitioners, this means:

- **Reproducible safety comparisons:** Teams can now benchmark their defenses against a common attack suite rather than self-selected methods, enabling honest capability claims.
- **Taxonomy-driven risk assessment:** The four-category taxonomy maps cleanly to real deployment risk profiles (direct harm, contextual harm, IP risk, multimodal risk), supporting structured threat modeling.
- **Defense co-development:** The open-source framework accelerates the attack-defense research cycle, reducing time from attack publication to viable defense.
- **Adversarial training template:** R2D2's efficient training loop provides a practical starting point for practitioners seeking to harden models beyond RLHF-level alignment.

The work establishes a methodological foundation that subsequent red teaming research — including WildTeaming and automated jailbreak frameworks — builds upon directly.
