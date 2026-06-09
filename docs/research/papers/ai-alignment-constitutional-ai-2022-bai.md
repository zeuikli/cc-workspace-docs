---
url: "https://arxiv.org/abs/2212.08073"
title: "Constitutional AI: Harmlessness from AI Feedback"
archived_date: 2026-06-09
arxiv_id: 2212.08073
authors: ["Yuntao Bai", "Saurav Kadavath", "Sandipan Kundu", "Amanda Askell", "et al. (51 authors", Anthropic)]
published_date: 2022-01-01
---

# Constitutional AI: Harmlessness from AI Feedback

**Authors:** Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, et al. (51 authors, Anthropic)
**Year:** 2022 (submitted December 15, 2022)
**Venue:** Preprint (Anthropic Technical Report)
**ArXiv:** https://arxiv.org/abs/2212.08073

---

## Full Abstract

As AI systems become more capable, human oversight of harmful behaviors becomes increasingly difficult and costly. This paper introduces Constitutional AI (CAI), a method for training harmless AI assistants without human labels identifying harmful outputs. The approach involves two phases: (1) supervised learning via self-critique and revision guided by a written constitution of ~16 natural-language harmlessness principles, and (2) reinforcement learning from AI feedback (RLAIF), where AI-generated preference judgments replace human labels. The resulting models are both non-evasive and non-harmful—able to engage thoughtfully with sensitive queries by explaining objections rather than refusing—while requiring far fewer human labels than traditional RLHF approaches.

---

## Key Contributions

- **Constitutional AI framework:** Introduced a two-phase training pipeline combining SL-CAI (supervised learning via self-critique and revision) with RL-CAI (reinforcement learning from AI feedback / RLAIF via AI-generated preference labels).
- **RLAIF coined and demonstrated:** Reinforcement Learning from AI Feedback as a scalable alternative to human-labeled RLHF for harmlessness training, enabling supervision without costly human annotation of harmful outputs.
- **Chain-of-thought for transparency:** Showed that chain-of-thought reasoning during the critique-revision phase improves both model performance and interpretability, making the model's reasoning visible.
- **Non-evasive harmlessness:** Demonstrated that models can engage helpfully with sensitive queries by explaining objections rather than simply refusing, reducing unhelpful evasiveness while maintaining safety.
- **Scalability with fewer human labels:** Proved robust AI behavior control is achievable with far fewer human labels, directly addressing the annotation cost bottleneck in traditional alignment pipelines.
- **Written constitution as specification:** Established ~16 natural-language principles as a practical mechanism for specifying harmlessness criteria, making alignment objectives more interpretable and auditable.

---

## Methodology

**Phase 1 — Supervised Learning with Self-Critique (SL-CAI):** A pretrained language model is prompted to generate responses to potentially harmful queries. It then critiques its own outputs against a written constitution—a set of ~16 natural-language principles covering harmlessness dimensions such as avoiding deception, respecting autonomy, and not facilitating harm. The model then revises its response to better comply with the critique. This critique-revision cycle can be iterated multiple times. The final revised responses serve as supervised fine-tuning data. Chain-of-thought reasoning is incorporated into the critique step, making the model's reasoning explicit and improving output quality.

**Phase 2 — Reinforcement Learning from AI Feedback (RL-CAI / RLAIF):** Rather than relying on human annotators to label which of two model responses is less harmful, the authors use a separate AI model (a feedback model, also guided by the constitution) to generate preference labels. The feedback model is prompted with a pair of responses and the constitutional principles, and asked which response better adheres to the principles. These AI-generated preference labels are used to train a preference model (PM), which in turn provides reward signal for reinforcement learning (specifically RLHF-style PPO). The resulting policy is termed RL-CAI. The RLAIF loop allows the entire harmlessness alignment pipeline to operate at scale with minimal human labeling.

**Constitutional Design:** The constitution itself is a concise, human-readable document (~16 principles) that can be audited, modified, and version-controlled. This makes the alignment criteria transparent and adjustable by researchers, contrasting with opaque human preference datasets. The constitution draws on principles from sources including the UN Declaration of Human Rights and Anthropic's own safety guidelines.

---

## Main Results

- RL-CAI models were rated by human evaluators as significantly more helpful and less harmful than RLHF baselines trained without constitutional guidance.
- Constitutional AI models achieved higher harmlessness scores while maintaining or improving helpfulness compared to models trained solely on human-labeled preference data.
- SL-CAI phase alone (without RLAIF) produced substantial improvements; adding RL-CAI further compounded gains.
- Chain-of-thought critique substantially improved revision quality over direct critique, with human raters preferring CoT-revised outputs.
- Models trained with CAI were less evasive: they engaged substantively with sensitive queries by explaining why certain assistance would be harmful rather than issuing blanket refusals.
- RLAIF-generated labels correlated strongly with human preference labels, validating AI feedback as a reliable proxy for human judgment on harmlessness.

---

## Limitations & Future Work

- The constitution itself is authored by humans and reflects their values; biases or omissions in the constitution propagate to the trained model. Iterative constitutional refinement is needed.
- The critique-revision loop quality depends on the capability of the base model—weaker models may produce low-quality critiques that do not improve safety.
- RLAIF relies on an AI feedback model that may itself have miscalibrated values or blind spots, creating a feedback loop with potential for systematic errors.
- Evaluation of harmlessness is inherently difficult; the paper acknowledges that human evaluator agreement on harmful content is imperfect and culturally variable.
- Scalable oversight questions remain: as models become more capable than their evaluators, even AI feedback models may fail to detect sophisticated harms.
- Future work includes extending constitutional approaches to helpfulness (not just harmlessness), multi-turn dialogue, and culturally diverse constitutional principles.

---

## Why This Matters for AI Practitioners

Constitutional AI is a foundational alignment technique that addresses two critical practical problems: (1) the high cost and inconsistency of human annotation for harmful content, and (2) the tendency of safety training to produce unhelpfully evasive models. By replacing human harmlessness labels with AI-generated feedback guided by explicit principles, CAI enables safety training to scale without a linear increase in annotation costs. The written constitution paradigm also makes alignment criteria auditable and modifiable—a significant advantage over opaque preference datasets. Practitioners building safety-critical LLM products can adopt CAI's critique-revision loop as a post-processing step, or use constitutional principles as structured system prompts during inference. The RLAIF methodology specifically is now widely used across industry as a cost-effective alternative to full RLHF for harmlessness objectives.
