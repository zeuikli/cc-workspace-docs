---
url: "https://arxiv.org/abs/2312.09390"
title: "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision"
archived_date: 2026-06-09
arxiv_id: 2312.0939
authors: ["Collin Burns", "Pavel Izmailov", "Jan Hendrik Kirchner", "Bowen Baker", "Leo Gao", "Leopold Aschenbrenner", "Yining Chen", "Adrien Ecoffet", "Manas Joglekar", "Jan Leike", "Ilya Sutskever", "Jeff Wu (OpenAI)"]
pdf_path: pdfs/2312.09390.pdf
published_date: 2023-01-01
---

# Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision

**Authors:** Collin Burns, Pavel Izmailov, Jan Hendrik Kirchner, Bowen Baker, Leo Gao, Leopold Aschenbrenner, Yining Chen, Adrien Ecoffet, Manas Joglekar, Jan Leike, Ilya Sutskever, Jeff Wu (OpenAI)
**Year:** 2023 (submitted December 14, 2023)
**Venue:** Preprint (OpenAI Technical Report); associated with OpenAI Superalignment initiative
**ArXiv:** https://arxiv.org/abs/2312.09390

---

## Full Abstract

A core challenge in aligning future superhuman AI models is that humans may not be able to reliably evaluate the AI's capabilities. This paper investigates whether weaker models can supervise stronger models—termed "weak-to-strong generalization"—as a tractable analogy for the superalignment problem. Experiments across GPT-4 family models on NLP benchmarks, chess, and reward modeling find that strong pretrained models consistently outperform their weak supervisors when finetuned on weak-model-generated labels. Using auxiliary confidence loss with GPT-2-level supervision on GPT-4 recovered close to GPT-3.5-level performance on NLP tasks. The results suggest current alignment techniques like RLHF may be fundamentally insufficient for superhuman models.

---

## Key Contributions

- **Superalignment framed as empirical research question:** Recast the abstract problem of aligning superhuman AI as a concrete, testable question—"can a weak model supervise a strong one?"—making it tractable for near-term experimental investigation.
- **Weak-to-strong generalization demonstrated:** Strong pretrained models consistently generalize beyond their weak supervisors across NLP benchmarks, chess puzzles, and reward modeling, showing that pretrained knowledge enables models to "fill in" correct behavior beyond what weak labels specify.
- **Auxiliary confidence loss proposed:** A practical training technique where the strong model is penalized for low-confidence predictions on its own unlabeled data, recovering substantial performance gap under weak supervision (GPT-2 → GPT-4 supervision gap partially closed).
- **RLHF insufficiency warning:** Provides the first systematic empirical evidence that standard RLHF-style finetuning on weak-supervisor labels may be fundamentally inadequate for aligning models substantially more capable than their overseers.
- **Research program and funding launched:** Released open research directions and announced $10M in external grants to accelerate superalignment research, positioning this as a community-scale research agenda rather than a closed project.
- **Benchmark across modalities:** Chess puzzle performance and reward modeling experiments extend findings beyond NLP, suggesting the phenomenon is domain-general rather than an artifact of language task structure.

---

## Methodology

**Experimental Setup — Weak-to-Strong Analogy:** The paper operationalizes the superalignment challenge using the GPT-4 model family as a controlled testbed. A "weak supervisor" (e.g., GPT-2 or a small GPT-4 variant) generates labels for a set of tasks. A "strong student" (e.g., a larger GPT-4 variant) is then finetuned on these weak labels. The key question: does the strong student's performance exceed what the weak labels alone would predict, and can it approach the performance ceiling of the strong model trained with ground-truth labels? This mirrors the anticipated future scenario where humans (weak supervisors) must align superhuman AI (strong students).

**Tasks and Evaluation:** Three task categories are used: (1) NLP benchmarks (classification and generation tasks where accuracy against ground truth is measurable), (2) chess puzzle solving (a domain with clear correct answers requiring reasoning beyond what a weak supervisor can evaluate), and (3) reward modeling (training a reward model on weak-supervisor preference labels, then evaluating its alignment with ground-truth human preferences). Results across all three show consistent weak-to-strong generalization effects, though the magnitude varies by domain and capability gap size.

**Auxiliary Confidence Loss:** To improve upon naive finetuning on weak labels, the authors propose an auxiliary loss term that encourages the strong model to maintain high confidence on its own unlabeled predictions. This functions as a form of self-consistency regularization: the strong model's internal knowledge, encoded in its pretrained weights, is leveraged as an additional supervision signal beyond the weak labels. Empirically, this recovers a meaningful fraction of the capability gap—e.g., GPT-4 finetuned with GPT-2-level supervision plus confidence loss approaches GPT-3.5-level NLP performance.

---

## Main Results

- Strong students consistently outperform weak supervisors after finetuning on weak labels, confirming weak-to-strong generalization as a robust phenomenon across tasks and model scales.
- Without auxiliary loss, a significant "imitation gap" persists: the strong student underperforms what it would achieve under ground-truth supervision, suggesting naive RLHF will leave capability unused in superhuman regimes.
- Auxiliary confidence loss reduces the imitation gap substantially on NLP tasks; the effect is smaller on chess and reward modeling, suggesting domain-specific techniques may be needed.
- The magnitude of weak-to-strong generalization scales with the pretrained capability of the strong model—more capable base models generalize more effectively from weak supervision.
- Reward modeling experiments show that even when the reward model is trained on weak-supervisor labels, the resulting policy can surpass the weak supervisor's own performance ceiling, but with noticeable alignment degradation compared to ground-truth-trained reward models.
- Chess experiments reveal that weak supervisors (unable to solve hard puzzles) can still provide labels that enable strong students to solve puzzles the supervisor could not evaluate—direct evidence of supervision beyond evaluator competence.

---

## Limitations & Future Work

- The GPT-4 family provides a controlled but narrow testbed; results may not generalize to truly superhuman capability gaps (e.g., humans supervising a model 100× more capable).
- Auxiliary confidence loss is a heuristic; its theoretical grounding and failure modes under distribution shift are not fully characterized.
- Chess and reward modeling show weaker weak-to-strong generalization than NLP, suggesting the effect is task-dependent and may not universally rescue alignment under weak supervision.
- The paper does not address adversarial weak supervisors or cases where weak labels are systematically biased (e.g., human annotators with consistent ideological blind spots).
- Scalable oversight techniques (debate, amplification) are not compared head-to-head with weak-to-strong generalization; the relationship between these paradigms is left for future work.
- Open questions: How does the capability gap threshold affect generalization? What training data mixtures maximize weak-to-strong transfer? Can this framework be extended to multi-step reasoning and agency?

---

## Why This Matters for AI Practitioners

This paper reframes the long-term AI safety problem as something researchable today with available models. For practitioners, the near-term implication is stark: if your finetuning supervisor (human annotator or AI labeler) cannot reliably evaluate the model's outputs in a domain, standard RLHF may not produce the alignment you expect—the model may silently revert to pretrained biases or learn to satisfy the evaluator's limited judgment rather than genuinely improving. The auxiliary confidence loss technique offers a practical mitigation: leverage the model's own pretrained knowledge as a self-consistency check during alignment fine-tuning. For teams building reward models or preference-based pipelines, this work argues for investing in better evaluation infrastructure (e.g., debate, amplification, automated test suites) rather than assuming human raters can reliably distinguish quality as model capability scales. The research program it launched—superalignment—has become a significant research direction across the field.
