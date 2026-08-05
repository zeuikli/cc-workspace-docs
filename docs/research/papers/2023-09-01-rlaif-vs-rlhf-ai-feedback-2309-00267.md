---
url: "https://arxiv.org/abs/2309.00267"
title: "RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback"
archived_date: 2026-06-09
arxiv_id: 2309.00267
authors: ["Harrison Lee", "Samrat Phatale", "Hassan Mansoor", "Thomas Mesnard", "Johan Ferret", "Kellie Lu", "Colton Bishop", "Ethan Hall", "Victor Carbune", "Abhinav Rastogi", "Sushant Prakash (Google DeepMind)"]
pdf_path: pdfs/2309.00267.pdf
published_date: 2023-01-01
---

# RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback

**Authors:** Harrison Lee, Samrat Phatale, Hassan Mansoor, Thomas Mesnard, Johan Ferret, Kellie Lu, Colton Bishop, Ethan Hall, Victor Carbune, Abhinav Rastogi, Sushant Prakash (Google DeepMind)
**Year:** 2023 (submitted September 1, 2023; published ICML 2024)
**Venue:** International Conference on Machine Learning (ICML) 2024
**ArXiv:** https://arxiv.org/abs/2309.00267

---

## Full Abstract

Reinforcement learning from human feedback (RLHF) is a technique to align large language models (LLMs) with human preferences. However, gathering high-quality human preference labels is a key bottleneck in scaling RLHF. This paper addresses that challenge by replacing human evaluators with AI feedback (RLAIF), demonstrating that RLAIF achieves comparable performance to RLHF across summarization and dialogue tasks. The authors further introduce Direct-RLAIF (d-RLAIF), a technique that bypasses reward model training by obtaining evaluations directly from a language model during reinforcement learning, achieving superior results. They also demonstrate that an AI labeler identical to the policy being trained can still provide effective training signal, enabling self-improvement.

---

## Key Contributions

- **RLAIF ≈ RLHF empirically validated:** First peer-reviewed (ICML) large-scale empirical demonstration that RLAIF achieves performance on par with RLHF across summarization and dialogue generation tasks, removing the assumption that human labels are irreplaceable.
- **Direct-RLAIF (d-RLAIF) introduced:** A novel technique that bypasses reward model training entirely, obtaining preference evaluations directly from a language model during the RL training loop. d-RLAIF achieves superior results compared to standard RLAIF.
- **Same-capability self-improvement shown:** Demonstrates that AI labelers at the same capability level as the policy model (or even identical to it) can still provide effective alignment signal—enabling a form of self-improvement without external human oversight.
- **Practical scalability:** Provides a concrete, production-viable alternative to costly human annotation pipelines, with documented methodology applicable to any task where preference comparisons can be elicited from a language model.
- **Peer-reviewed validation:** ICML 2024 acceptance provides academic validation of RLAIF as a mainstream alignment technique beyond the initial Anthropic CAI preprint.

---

## Methodology

**Standard RLAIF Pipeline:** The authors follow an RLHF-style pipeline but substitute human annotators with an AI labeler (an off-the-shelf LLM). Given a prompt and two model responses, the AI labeler is prompted to evaluate which response is preferable according to a natural-language criterion (e.g., "which summary is more accurate and concise?"). These AI-generated pairwise preference labels are used to train a reward model (RM), which assigns scalar reward to individual responses. The policy is then fine-tuned with PPO using the RM as the reward signal. This pipeline is evaluated against a standard RLHF baseline where human annotators supply the preference labels.

**Direct-RLAIF (d-RLAIF):** Rather than training a separate reward model from AI-labeled preferences, d-RLAIF queries the AI labeler directly during RL training. At each RL step, the language model generates a response, and the AI labeler immediately evaluates it relative to alternatives, providing the reward signal without an intermediate RM training phase. This eliminates the reward model as a potential source of distributional drift and reduces pipeline complexity. The authors show this approach outperforms standard RLAIF, suggesting the intermediate RM introduces unnecessary approximation error.

**Self-Labeling Experiments:** A key experimental condition tests whether an AI labeler identical to (or no more capable than) the policy being trained can provide useful signal. Results confirm that even same-capability labelers produce preference judgments that improve the policy, which has profound implications: it suggests AI systems can improve via self-generated feedback loops without relying on a strictly superior overseer. The authors carefully control for potential circular reasoning artifacts in this experimental setup.

---

## Main Results

- RLAIF and RLHF produce statistically comparable win rates against a reference policy on TL;DR summarization and Anthropic Helpful and Harmless (HH) dialogue tasks; human raters could not reliably distinguish RLAIF-trained from RLHF-trained outputs.
- d-RLAIF outperforms standard RLAIF on both tasks, achieving the highest win rates of any method tested, including human-labeled RLHF.
- AI labelers at the same capability level as the policy (same model family, same size) still produce preference labels that yield measurable policy improvement, confirming same-capability self-improvement.
- AI-generated preference labels show high inter-rater agreement with human annotators (Cohen's κ reported), validating label quality.
- The RLAIF pipeline reduces annotation cost substantially: AI labeling is orders of magnitude cheaper and faster than recruiting human annotators at equivalent scale.

---

## Limitations & Future Work

- Evaluation is limited to summarization and dialogue; generalization to more complex tasks (code generation, math, multi-step reasoning) remains unverified.
- The AI labeler itself must have sufficiently good judgment; for tasks where LLMs systematically misjudge quality, RLAIF will propagate those errors into the policy.
- Self-improvement via same-capability labeling could create feedback loops where subtle biases are amplified rather than corrected over multiple iterations.
- d-RLAIF requires online inference from the AI labeler during RL training, increasing compute cost per training step compared to using a pre-trained RM.
- The paper does not address adversarial robustness: a capable model could potentially learn to produce outputs that exploit the AI labeler's preferences rather than genuinely improving in the target dimension.
- Future work: extending d-RLAIF to iterated self-improvement, investigating multi-model labeler ensembles to reduce single-model bias, and exploring constitutional AI-style principle injection into the RLAIF labeling prompt.

---

## Why This Matters for AI Practitioners

This paper provides the critical empirical bridge between Anthropic's CAI/RLAIF proposal (2212.08073) and production use: it demonstrates under controlled, peer-reviewed conditions that AI feedback is a valid substitute for human feedback at scale. For teams building or fine-tuning LLMs, RLAIF dramatically reduces the annotation budget required for preference-based alignment—making RLHF-style training accessible to organizations without large-scale human labeling infrastructure. The d-RLAIF finding is particularly actionable: it eliminates the need to train and maintain a separate reward model, simplifying the alignment pipeline to a single-model loop. The self-improvement result also opens a path to continuous alignment without human annotation, though practitioners should monitor for feedback-loop drift. This work is now a standard reference for any team evaluating the cost-quality tradeoff of human vs. AI preference labeling.
