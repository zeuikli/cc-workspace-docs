---
url: "https://arxiv.org/abs/2209.10652"
title: "Toy Models of Superposition"
archived_date: 2026-06-09
arxiv_id: 2209.10652
authors: ["Nelson Elhage", "Tristan Hume", "Catherine Olsson", "Nicholas Schiefer", "Tom Henighan", "Shauna Kravec", "Zac Hatfield-Dodds", "Robert Lasenby", "Dawn Drain", "Carol Chen", "Roger Grosse", "Sam McCandlish", "Jared Kaplan", "Dario Amodei", "Martin Wattenberg", "Christopher Olah"]
pdf_path: pdfs/2209.10652.pdf
published_date: 2022-01-01
---

# Toy Models of Superposition

**Authors:** Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg, Christopher Olah

**Year:** 2022

**Venue/Publisher:** Transformer Circuits Thread (Anthropic); also arXiv

**ArXiv:** https://arxiv.org/abs/2209.10652

**URL:** https://transformer-circuits.pub/2022/toy_model/index.html

---

## Abstract

This paper addresses polysemanticity in neural networks, where single neurons encode multiple unrelated concepts. The authors present a toy model where polysemanticity can be fully understood, arising as a result of models storing additional sparse features in "superposition." They demonstrate how neural networks can compress numerous sparse features into limited neurons through superposition mechanisms, making polysemanticity interpretable. The work identifies a phase transition during this process and establishes a surprising connection to the geometry of uniform polytopes, providing foundational theory for why mechanistic interpretability must go beyond individual neurons.

---

## Key Contributions

- **Formal theoretical framework for the superposition hypothesis:** neural networks represent more features than they have neurons by storing them in superposition — linear combinations across multiple neurons — when the underlying features are sparse in activation
- **Discovery of a phase transition in superposition behavior:** the model exhibits a critical threshold in the feature importance/sparsity tradeoff below which features are stored in superposition and above which they occupy dedicated neurons — a discrete qualitative shift, not a gradual continuum
- **Geometric connection between superposition and uniform polytopes:** the optimal packing of features in superposition corresponds to geometric structures (such as the regular simplex and the tetrahedron inscribed in a sphere) known from the mathematics of polytopes in high-dimensional spaces, providing a rigorous analytical handle on feature geometry
- **Evidence linking superposition mechanisms to adversarial example vulnerability:** superposition creates interference between features that may make networks systematically vulnerable to adversarial perturbations, providing a mechanistic account of a previously empirical phenomenon
- **Establishes toy-model methodology** for controlled mechanistic interpretability experiments: by studying minimal models where ground truth is known, the authors demonstrate that mechanistic hypotheses can be tested rigorously before scaling up
- **Polysemanticity as a necessary consequence, not a training artifact:** the analysis shows that polysemanticity is the theoretically optimal behavior for a network that must represent many sparse features in limited neurons — it is not a flaw but a natural consequence of capacity constraints

---

## Methodology

The authors construct **minimal neural network models** designed to have known, fully controlled feature structure. A key toy model consists of a linear bottleneck: inputs are high-dimensional vectors where each dimension corresponds to a known feature, features are made sparse by zeroing out dimensions with probability (1 − sparsity), and the network must compress this input through a lower-dimensional hidden layer and then reconstruct it. Because the ground truth (which features exist, how sparse they are, how important they are) is fully controlled by the experimenter, the analysis of what the trained network does internally can be compared directly against theoretical predictions.

The authors derive the **theoretical optimal solution** for this compression problem: for a given sparsity level and feature importance distribution, there is an optimal tradeoff between representing features in dedicated neurons (perfectly monosemantic, but limited by neuron count) versus storing them in superposition (polysemantic, but allowing many more features). The theoretical optimum turns out to be discontinuous in sparsity — there is a phase transition where the optimal strategy switches between these two regimes. The geometry of the optimal superposition solution corresponds to known mathematical structures: for example, five features packed optimally into two dimensions form a regular pentagon, and the geometry generalizes to the Platonic solids and their higher-dimensional analogues.

To connect these toy model results to real networks, the authors study **one-layer transformers** trained on real language data and measure the geometry of features in the MLP layer, finding that the observed geometry is consistent with the superposition predictions. They also construct experiments where known features are injected into real network activations and measure how the network responds, providing empirical evidence that superposition is operative in real models, not just toy constructs.

---

## Main Results

- Toy models trained with sparse features reliably develop **superposition**: networks trained to reconstruct a higher-dimensional sparse input through a narrower bottleneck learn to encode multiple input features per neuron, exactly as predicted by the superposition hypothesis
- A **phase transition** is clearly observed: as feature sparsity decreases (features become less sparse / more commonly active), the optimal strategy transitions from superposition to dedicated representation at a critical threshold that matches theoretical predictions
- The geometry of superposition solutions corresponds to **known polytopes**: two features packed into one neuron form an antipodal pair; five features in two neurons form a regular pentagon; the correspondence generalizes to higher dimensions and matches uniform polytope theory
- **Adversarial robustness connection:** in models storing features in superposition, adversarial perturbations in the neuron basis map to simultaneous perturbations of multiple features, explaining why adversarial examples transferring across models may be exploiting superposition structure
- When feature importances are unequal, **important features are stored monosemantically** while less important ones are pushed into superposition — the network prioritizes accurate representation of the most task-relevant features
- The toy model results are **consistent with observations in real one-layer transformers**, providing empirical grounding for the theoretical framework

---

## Limitations & Future Work

- The **toy models are intentionally minimal** and do not capture the full complexity of trained transformers: there are no attention mechanisms, no deep layer interactions, and the features are artificially planted rather than learned from data
- The **precise correspondence between toy model features and real model features** is not established formally; real models learn their features implicitly from data, and whether those features have the same sparsity structure assumed by the toy models is an empirical question answered only approximately
- The **phase transition analysis** assumes idealized conditions (independent features, specific sparsity distributions) that may not hold in practice; the sharpness of the transition in real networks is likely blurred by deviations from these assumptions
- **Multi-layer interactions** are not studied; superposition dynamics may be qualitatively different in deep networks where features computed in one layer are consumed by the next
- The connection to adversarial examples is suggestive but not a complete explanation — adversarial vulnerability has multiple causes, and superposition accounts for only one of them

---

## Why This Matters for AI Practitioners

This paper provides the **theoretical foundation** for the entire sparse autoencoder interpretability program. Without understanding why neurons are polysemantic (and that polysemanticity is not a bug but an optimal compression strategy), it would not be clear what SAEs are doing or why they recover interpretable features. The superposition hypothesis explains exactly why naively inspecting individual neurons fails — they are genuinely encoding multiple features, not computing one function poorly — and why dictionary learning with a sparse code is the right approach to recover the underlying features.

The **phase transition result** has practical design implications: it suggests that models with higher parameter counts relative to feature counts are less likely to use superposition, and thus individual neurons become more interpretable as models scale (though the number of features also scales). This makes the superposition framework a useful lens for thinking about how interpretability difficulty scales with model size.

The **geometric connection to polytopes** provides a mathematical handle that has since been used to design improved SAE architectures and to reason about feature interference. For AI safety researchers, the adversarial example connection suggests that models heavily using superposition may have systematically exploitable internal structure — a safety-relevant finding that motivates further investigation of the relationship between interpretability and robustness.
