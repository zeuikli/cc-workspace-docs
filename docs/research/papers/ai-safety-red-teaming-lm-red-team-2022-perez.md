---
url: "https://arxiv.org/abs/2202.03286"
title: "Red Teaming Language Models with Language Models"
archived_date: 2026-06-09
arxiv_id: 2202.03286
authors: ["Ethan Perez", "Saffron Huang", "Francis Song", "Trevor Cai", "Roman Ring", "John Aslanides", "Amelia Glaese", "Nat McAleese", "Geoffrey Irving"]
published_date: 2022-01-01
---

# Red Teaming Language Models with Language Models

**Authors:** Ethan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, Geoffrey Irving

**Year:** 2022

**Venue:** arXiv preprint (Anthropic / DeepMind collaboration; widely cited as foundational LLM red teaming work)

**ArXiv:** https://arxiv.org/abs/2202.03286

---

## Full Abstract

Language models (LMs) often cannot be deployed because of their potential to harm users in hard-to-predict ways. Prior work has relied on human annotators to manually construct a limited set of adversarial test cases, which is expensive, limited in scale, and does not systematically cover the space of potential harms. We propose to instead use language models to automatically generate test cases that expose harmful behaviors in target LMs, enabling far more extensive and systematic safety evaluation. We generate test cases using a variety of methods including zero-shot generation, few-shot generation, supervised learning, and reinforcement learning, allowing us to control test case difficulty and diversity. Applied to a 280 billion parameter chatbot, our approach discovers a wide range of harmful behaviors including offensive replies, data leakage, and multi-turn harms, all at far greater scale and breadth than prior human-annotated approaches. We release our code and models to facilitate further research on LM safety evaluation.

---

## Key Contributions

- **LM-as-red-teamer paradigm:** Pioneered the approach of using a language model to automatically generate adversarial test cases against a target LM, enabling scalable safety evaluation without expensive human annotation at each step.
- **Multi-method attack generation:** Introduced a spectrum of test case generation strategies — zero-shot prompting, few-shot prompting, supervised learning on human-curated examples, and reinforcement learning with a classifier reward — providing control over attack diversity and difficulty.
- **Diverse harm discovery at scale:** Applied to a 280B-parameter chatbot, the method uncovered offensive replies, harmful demographic stereotypes, leaked training data (including real phone numbers), and emergent multi-turn conversational harms.
- **RL-controlled diversity:** Demonstrated that RL-trained red teaming models, rewarded for eliciting harmful outputs, discover qualitatively different (and harder) attacks compared to zero/few-shot methods, establishing the importance of diversity-maximizing red teaming.
- **Classifier-based harm detection pipeline:** Introduced systematic at-scale harm detection using trained classifiers, enabling evaluation of millions of generated test cases that would be infeasible for human review.
- **Foundational methodology:** Established the conceptual and experimental template — red LM, target LM, harm classifier, diversity metrics — that all subsequent automated red teaming frameworks (PAIR, TAP, WildTeaming, HarmBench) build upon.

---

## Methodology

The core framework involves three components: a red LM that generates test prompts, a target LM that responds to those prompts, and a harm classifier that labels responses as harmful or benign. The red LM is prompted or trained to generate diverse, adversarial inputs, while the harm classifier provides a scalar signal indicating whether the target's response contains harmful content. This setup decouples the attack generation problem from the harm detection problem, allowing each component to be independently improved.

Four generation strategies are explored in ascending order of sophistication. Zero-shot generation prompts the red LM to produce harmful questions with no examples. Few-shot generation conditions on a small set of human-curated harmful queries to guide style and topic. Supervised learning fine-tunes the red LM on human-annotated adversarial examples, specializing it toward productive attack patterns. Reinforcement learning uses the harm classifier as a reward function, training the red LM via policy gradient to maximize the probability of eliciting harmful responses while maintaining lexical diversity through entropy bonuses. The RL approach is most powerful but also most prone to mode collapse without diversity regularization.

Multi-turn harm evaluation extends the framework beyond single-turn exchanges. The red LM generates entire conversation prefixes that guide the target chatbot toward harmful behaviors through progressive context manipulation — a key finding being that harms can emerge in turn 3 or 4 of a conversation even when individual turns appear benign, exploiting the conversational context accumulation of transformer-based chatbots.

---

## Main Results

- Zero-shot red teaming already uncovers thousands of offensive outputs from the 280B chatbot; RL-trained red teaming discovers qualitatively harder cases that zero-shot and few-shot methods miss.
- Training data leakage is confirmed: the red LM elicits verbatim phone numbers and other personally identifiable information from the target chatbot, establishing training data memorization as a concrete harm vector.
- Harmful stereotype generation is widespread: the target chatbot produces disparaging associations for dozens of demographic groups when appropriately prompted, revealing alignment gaps in safety fine-tuning.
- Multi-turn attacks succeed in eliciting harmful content even from a chatbot that reliably refuses single-turn harmful requests — establishing conversational context manipulation as a distinct and underappreciated attack surface.
- RL-trained red teaming achieves higher harmful response rates per query than zero-shot or few-shot methods, but requires more careful diversity regularization to avoid degenerate repetitive outputs.
- Harm classifier accuracy is sufficient for large-scale automated evaluation but introduces false positive/negative rates that create noise in aggregate statistics — motivating later work (HarmBench) to improve judge reliability.

---

## Limitations and Future Work

- **Classifier dependence:** The approach is limited by the quality of the harm classifier; errors in harm detection propagate directly into red teaming evaluation quality and RL reward signal fidelity.
- **Single-model red teamer:** The red LM is a single model; adversarial diversity is limited by its prior and training distribution, potentially missing harm vectors outside its coverage.
- **Evaluation at one scale:** Results are reported for a single 280B-parameter target chatbot; generalization to models of different scales, architectures, and training regimes is not systematically characterized.
- **RL instability:** Reinforcement learning for red teaming is sensitive to hyperparameters and prone to reward hacking (the red LM learns to fool the classifier rather than elicit genuine harm); robust RL-based red teaming remains an open problem.
- **No defense evaluation:** The paper focuses entirely on attack generation and does not evaluate how discovered harms can be mitigated or whether safety fine-tuning on discovered cases improves robustness.

---

## Why This Matters for AI Practitioners

This paper is the foundational reference for automated red teaming — the paper that established the LM-red-teams-LM paradigm that all subsequent automated safety evaluation work inherits:

- **Scalability inflection point:** By replacing human annotation with LM-generated test cases, the paper demonstrated that safety evaluation can scale to millions of queries, fundamentally changing what comprehensive safety assessment looks like.
- **Multi-turn safety gap:** The multi-turn harm discovery is practically critical — chatbot deployments rarely evaluate multi-turn conversational safety, yet this paper shows harmful behaviors can emerge specifically from conversation accumulation.
- **Training data leakage evidence:** The phone number leakage result provided early empirical grounding for memorization-based privacy risks, influencing data governance practices and model auditing standards.
- **RL diversity insight:** The finding that RL-trained red teamers find qualitatively different attacks than prompting-based methods established diversity maximization as a first-class objective in red teaming — not just attack success rate.
- **Template for tooling:** Every major red teaming tool published after 2022 (PAIR, TAP, AutoDAN, HarmBench, WildTeaming) traces its conceptual lineage to this paper's three-component framework.
