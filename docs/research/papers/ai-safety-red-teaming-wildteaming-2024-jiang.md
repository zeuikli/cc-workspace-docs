# WildTeaming at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models

**Authors:** Liwei Jiang, Kavel Rao, Seungju Han, Allyson Ettinger, Faeze Brahman, Sachin Kumar, Niloofar Mireshghallah, Ximing Lu, Maarten Sap, Yejin Choi, Nouha Dziri

**Year:** 2024

**Venue:** arXiv preprint (submitted June 26, 2024); affiliated with University of Washington, Allen Institute for AI (AI2)

**ArXiv:** https://arxiv.org/abs/2406.18510

---

## Full Abstract

We introduce WildTeaming, an automatic red-teaming framework that mines in-the-wild user-chatbot interactions to discover jailbreak tactics and compositionally apply them to create novel jailbreaks. WildTeaming mines 5.7K unique clusters of jailbreak tactics from real user interactions, far exceeding the diversity of researcher-directed red teaming. We further examine how combinations of these tactics interact compositionally, revealing synergistic attack patterns. To mitigate the discovered vulnerabilities, we create WildJailbreak, an open-source safety training dataset of 262K vanilla (direct harmful request) and adversarial (complex jailbreak) prompt-response pairs. WildJailbreak includes contrastive benign-but-suspicious queries alongside harmful ones, directly targeting over-refusal — a key failure mode of safety training. Safety fine-tuning on WildJailbreak achieves up to 4.6x more diverse and successful adversarial attack coverage compared to existing safety datasets while maintaining strong benign helpfulness. We analyze how data properties and model capabilities interact during safety training, providing actionable guidance for practitioners building safer LLMs.

---

## Key Contributions

- **WildTeaming framework:** An automated red-teaming system that mines real user-chatbot interaction logs to extract and cluster jailbreak tactics, discovering 5.7K unique attack tactic clusters — orders of magnitude more diverse than researcher-directed methods.
- **In-the-wild data advantage:** Demonstrated that real user adversarial attempts provide richer, more naturalistic, and more diverse attack signals than synthetic LM-generated or manually crafted attacks, achieving up to 4.6x higher attack diversity and success compared to prior safety datasets.
- **Compositional tactic analysis:** Systematically analyzed how combining multiple jailbreak tactics produces synergistic effects, revealing that two-tactic combinations often achieve higher ASR than either tactic alone and that certain tactic pairs are disproportionately effective.
- **WildJailbreak dataset:** Created a 262K-sample open-source safety training corpus with four quadrants: harmful+vanilla, harmful+adversarial, benign+vanilla, and benign+adversarial (contrastive) — specifically designed to reduce over-refusal while maintaining effective harm prevention.
- **Over-refusal mitigation:** Directly addressed the over-refusal failure mode by pairing harmful adversarial queries with benign-but-suspicious queries in training, teaching models to distinguish genuine harm from superficially similar safe requests.
- **Scaling analysis:** Characterized how safety training data properties (diversity, adversarial coverage, benign contrastive pairs) interact with model capabilities across scales, providing empirically grounded guidance for safety fine-tuning practitioners.

---

## Methodology

WildTeaming's core innovation is sourcing adversarial tactics from the real distribution of user behavior rather than researcher hypotheses. The pipeline begins by collecting large-scale user-chatbot interaction logs from platforms where users organically attempt jailbreaks (e.g., WildChat, LMSYS). These interactions are processed to extract individual jailbreak tactics — specific rhetorical, structural, or framing strategies — which are then embedded and clustered using semantic similarity to produce 5.7K unique tactic clusters. Clustering ensures diversity measurement is based on semantic distinctiveness rather than surface variation.

New jailbreaks are constructed by compositionally combining tactics from the cluster inventory. Given a target harmful request, the framework samples tactic combinations, applies them sequentially or jointly to transform the request, and evaluates the resulting prompt against a target model. The compositional approach is motivated by the empirical observation that real users frequently combine multiple tactics (e.g., role-playing + hypothetical framing + persona injection) rather than relying on a single technique. Synergistic tactic pairs are identified by comparing single-tactic ASR to two-tactic combination ASR across a held-out evaluation set.

WildJailbreak is constructed to address both attack coverage and over-refusal simultaneously. The dataset contains four quadrant types: direct harmful requests (harmful+vanilla), jailbroken harmful requests (harmful+adversarial), benign requests that superficially resemble harmful ones (benign+adversarial), and ordinary benign requests (benign+vanilla). The contrastive benign quadrant is the key differentiator from prior safety datasets — training on it teaches models to attend to genuine semantic harm rather than surface-level patterns, reducing false refusals on legitimate queries. Models safety-fine-tuned on WildJailbreak are evaluated on both adversarial ASR reduction and benign helpfulness preservation.

---

## Main Results

- WildTeaming discovers 5.7K unique jailbreak tactic clusters from real user interactions, compared to fewer than 100 researcher-curated tactic categories in prior work — a roughly 57x increase in tactic diversity.
- Models trained on WildJailbreak achieve up to 4.6x more diverse adversarial attack coverage reduction compared to models trained on existing safety datasets (e.g., BeaverTails, Anthropic's HH-RLHF safety data).
- Compositional two-tactic jailbreaks achieve 15–30% higher ASR than single-tactic variants across evaluation models, confirming synergistic interaction effects.
- The contrastive benign quadrant reduces over-refusal rates by a statistically significant margin while maintaining equivalent or superior protection against adversarial prompts.
- Safety training data diversity (measured by tactic cluster coverage) is a stronger predictor of downstream robustness than dataset size alone — doubling dataset size with repetitive tactic coverage yields smaller gains than maintaining smaller-but-diverse coverage.
- WildJailbreak-trained models maintain strong performance on standard helpfulness benchmarks (MT-Bench, AlpacaEval), confirming that adversarial safety fine-tuning need not degrade general capability.

---

## Limitations and Future Work

- **Interaction log dependency:** WildTeaming requires access to large-scale user-chatbot interaction logs, which are not universally available and may reflect platform-specific user demographics and attack preferences.
- **Temporal drift:** Jailbreak tactic distributions evolve as models are updated and users adapt; the 5.7K cluster inventory requires periodic refresh to maintain coverage of emerging techniques.
- **English-centric evaluation:** The framework and WildJailbreak dataset are predominantly English-language; multilingual jailbreak diversity and cross-lingual transfer of tactics are not characterized.
- **Closed-model safety training:** WildJailbreak is evaluated for fine-tuning open-source models; applicability to closed-source models trained via RLHF with proprietary data pipelines is indirect.
- **Tactic taxonomy stability:** Semantic clustering of tactics is sensitive to embedding model choice and clustering hyperparameters; the 5.7K figure should be interpreted as an approximation of diversity rather than a precise count.

---

## Why This Matters for AI Practitioners

WildTeaming represents a methodological shift from researcher-centric to user-centric adversarial evaluation — with direct practical implications:

- **Realistic threat modeling:** By grounding attacks in actual user behavior, WildTeaming produces a threat model that reflects what deployed systems actually face rather than what researchers imagine attackers might attempt.
- **Over-refusal as a first-class metric:** The paper's explicit focus on over-refusal elevates it to a measurable safety objective alongside harm prevention, providing practitioners with a concrete dataset structure (contrastive benign pairs) for balancing both.
- **Safety dataset design principles:** The four-quadrant dataset structure is a generalizable template: harmful+adversarial for robustness, benign+adversarial for over-refusal reduction, vanilla pairs for calibration. This design principle applies beyond WildJailbreak.
- **Diversity over volume:** The empirical finding that tactic diversity predicts robustness better than dataset size challenges the common practice of scaling safety datasets through simple augmentation, redirecting effort toward qualitative coverage.
- **Operational red teaming:** The WildTeaming pipeline — mine, cluster, compose, evaluate — is directly implementable as an ongoing red teaming operation for production models, complementing periodic human red team exercises.
