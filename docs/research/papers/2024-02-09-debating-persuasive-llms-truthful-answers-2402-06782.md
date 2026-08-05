---
url: "https://arxiv.org/abs/2402.06782"
title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
archived_date: 2026-06-09
arxiv_id: 2402.06782
authors: ["Akbir Khan", "John Hughes", "Dan Valentine", "Laura Ruis", "Kshitij Sachan", "Ansh Radhakrishnan", "Edward Grefenstette", "Samuel R. Bowman", "Tim Rocktäschel", "Ethan Perez"]
pdf_path: pdfs/2402.06782.pdf
published_date: 2024-01-01
---

# Debating with More Persuasive LLMs Leads to More Truthful Answers

**Authors:** Akbir Khan, John Hughes, Dan Valentine, Laura Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward Grefenstette, Samuel R. Bowman, Tim Rocktäschel, Ethan Perez
**Year:** 2024 (submitted February 9, 2024; latest version July 25, 2024)
**Venue:** Preprint; presented at workshops on scalable oversight and alignment
**ArXiv:** https://arxiv.org/abs/2402.06782

---

## Full Abstract

The paper investigates debate as a scalable oversight mechanism: can less capable models (or humans) evaluate more capable AI systems by judging structured debates between expert models? Expert AI debaters argue opposing positions on questions drawn from a closed-book QA dataset, while non-expert models and human judges evaluate the debates. Results show debate consistently helps non-expert models achieve 76% accuracy and humans 88% accuracy, compared to baselines of 48% and 60% respectively. Training debaters specifically to be persuasive in an unsupervised manner further improves non-expert ability to identify the truth.

---

## Key Contributions

- **Large-scale empirical debate validation:** Provides the first large-scale empirical evidence that debate enables weaker evaluators—both models and humans—to identify correct answers from stronger AI agents, moving AI safety via debate from theoretical proposal to empirical validation.
- **Persuasiveness improves truth identification:** Shows that training debaters to be persuasive (in an unsupervised manner, without ground-truth labels) improves debate quality and increases non-expert truth-identification accuracy—a counterintuitive but important result.
- **Accuracy gains quantified:** Debate achieves 76% accuracy for non-expert model evaluators (vs. 48% baseline) and 88% for human evaluators (vs. 60% baseline)—substantial, statistically significant improvements in both cases.
- **Information asymmetry condition validated:** Demonstrates debate's benefits persist under realistic information asymmetry: non-expert evaluators lack domain expertise and ground-truth labels, mirroring the actual superalignment challenge.
- **Evaluator-agnostic benefits:** Debate helps both AI model evaluators and human evaluators, suggesting the mechanism is general rather than specific to one type of judge.

---

## Methodology

**Debate Framework Setup:** The experimental design instantiates AI Safety via Debate (originally proposed by Irving et al., 2018) in a concrete closed-book QA setting. Two "expert" AI debaters (larger/more capable models) are given a question. One debater is assigned the correct answer and one the incorrect answer, but neither knows which is correct during debate—they argue for their assigned position. A "non-expert" judge (a smaller model or human) observes the debate transcript and must determine which debater is defending the true answer. The key insight from debate theory is that, assuming a truthful debater has the "winning move" advantage, a persuasive argument structure should make the truth detectable even to a non-expert.

**Persuasiveness Training:** Beyond static debate between pretrained models, the authors train debater models specifically to be persuasive using a self-play procedure. Debaters are rewarded when the non-expert judge agrees with their position, without access to ground-truth labels. This unsupervised persuasiveness training creates debaters that are better at constructing compelling arguments. Critically, training for persuasiveness in this adversarial setting does not simply train models to be misleading: because both debaters are trained simultaneously and the judge is evaluating both, the equilibrium favors truthful persuasion over deceptive persuasion. The authors verify this by checking whether accuracy increases with persuasiveness training.

**Evaluation Protocol:** Questions are drawn from a closed-book QA dataset where definitive correct answers exist. Non-expert model judges are evaluated by whether they identify the correct answer (not which debater they found more persuasive). Human judges are recruited and asked to judge debate transcripts without access to external information, replicating conditions where humans must evaluate AI outputs they cannot independently verify. Baselines include: judges reading a single debater's argument (no debate), and judges answering directly without any AI assistance.

---

## Main Results

- Non-expert model evaluators: debate → 76% accuracy; single-argument baseline → 48% accuracy. A 28 percentage point gain from debate structure alone.
- Human evaluators: debate → 88% accuracy; single-argument baseline → 60% accuracy. A 28 percentage point gain consistent across both evaluator types.
- Persuasiveness training (unsupervised) further improves non-expert model accuracy beyond the static debate baseline, validating the claim that optimizing for persuasiveness in an adversarial debate context produces more truthful, higher-quality arguments.
- Debate benefits are robust across question difficulty levels; harder questions (where baselines struggle most) show the largest relative accuracy improvements from debate.
- Human judges benefit from debate even when they lack the domain knowledge to independently verify claims, confirming the mechanism works under the intended information asymmetry condition.
- Training debaters for persuasiveness does not reduce accuracy or cause evaluators to accept false claims more readily—the adversarial structure keeps persuasiveness aligned with truthfulness.

---

## Limitations & Future Work

- The closed-book QA setting has definitive correct answers, making it easier to train and evaluate than open-ended generation tasks where "truth" is contested or subjective.
- Both debaters are assigned answers rather than freely generating positions; real-world deployment would need debaters to propose and argue their own claims, introducing strategic complexity.
- Persuasiveness training used small-scale non-expert models as judges during training; whether training against stronger judge models maintains the truthfulness-persuasiveness alignment is not fully explored.
- The experiment assumes a two-position debate; many real AI safety questions involve multi-way uncertainty or continuous disagreement rather than binary correct/incorrect answers.
- Human judge experiments are limited in scale and participant expertise; results with domain experts or adversarially motivated judges are not tested.
- Future work: extending debate to open-ended generation, multi-round interactive debate, multi-party debates, and incorporating debate into RLHF pipelines as an alignment signal.

---

## Why This Matters for AI Practitioners

Debate addresses the core scalable oversight problem: how do you evaluate an AI system when it is more capable than your evaluators? This paper provides the first rigorous empirical evidence that structured adversarial debate is a practical mechanism, not just a theoretical proposal. For practitioners building evaluation pipelines for high-stakes AI systems, debate-style evaluation offers a concrete alternative to direct human assessment when the system's outputs are difficult to evaluate independently. The persuasiveness training result is particularly actionable: it suggests that LLMs can be fine-tuned to serve as better debate participants without requiring ground-truth labels, using self-play against a judge as the training signal. Teams working on red-teaming, evaluation frameworks, or interpretability may find debate useful as a structured elicitation technique—having one model argue for a claim and another argue against it can surface weaknesses in reasoning that single-model evaluation misses. This work is foundational for any organization building governance frameworks around AI systems that may eventually exceed human evaluative capacity.
