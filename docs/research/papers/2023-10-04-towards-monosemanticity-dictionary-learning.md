---
url: "https://transformer-circuits.pub/2023/monosemantic-features/index.html"
title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
archived_date: 2026-06-09
authors: ["Trenton Bricken", "Adly Templeton", "Joshua Batson", "Brian Chen", "Adam Jermyn", "Tom Conerly", "Nick Turner", "Cem Anil", "Carson Denison", "Amanda Askell", "Robert Lasenby", "Yifan Wu", "Shauna Kravec", "Nicholas Schiefer", "Tim Maxwell", "Nicholas Joseph", "Zac Hatfield-Dodds", "Alex Tamkin", "Karina Nguyen", "Brayden McLean", "Josiah E Burke", "Tristan Hume", "Shan Carter", "Tom Henighan", "Chris Olah"]
published_date: 2023-01-01
---

# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

**Authors:** Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nick Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec, Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Zac Hatfield-Dodds, Alex Tamkin, Karina Nguyen, Brayden McLean, Josiah E Burke, Tristan Hume, Shan Carter, Tom Henighan, Chris Olah

**Year:** 2023

**Venue/Publisher:** Transformer Circuits Thread (Anthropic)

**ArXiv:** N/A (published at transformer-circuits.pub)

**URL:** https://transformer-circuits.pub/2023/monosemantic-features/index.html

---

## Abstract

This paper demonstrates that sparse autoencoders can decompose the activations of a one-layer transformer into thousands of monosemantic, interpretable features. By treating the problem as dictionary learning, the authors extract over 4,000 features from a layer with only 512 neurons. Individual features correspond to specific human-interpretable concepts such as DNA sequences, legal language, HTTP requests, Hebrew text, and nutrition statements. The work provides empirical evidence that features — linear combinations of neuron activations — are better units of analysis than individual neurons, and that monosemanticity can be achieved at scale.

---

## Key Contributions

- **First large-scale demonstration that sparse autoencoders produce monosemantic features** in a real language model, not just toy models — validating that the superposition hypothesis applies to genuine trained transformers
- **Dictionary learning framing:** decomposes a 512-neuron layer into 4,000+ interpretable features, demonstrating that the network encodes far more concepts than it has neurons
- **Automated and human interpretability scoring methodology** for evaluating feature quality at scale, enabling systematic comparison between different sparse autoencoder configurations
- **Causal validation** showing extracted features are causally responsible for model behaviors, not mere correlates — steering features causally changes model outputs in predictable ways
- **Feature geometry analysis** demonstrating that features form structured, interpretable directions in the residual stream rather than occupying arbitrary positions
- **Polysemanticity characterization:** quantitative evidence that individual neurons are polysemantic (respond to multiple unrelated concepts) while extracted SAE features are monosemantic
- **Establishes the SAE paradigm** as the primary tool for mechanistic interpretability at scale, providing the methodological template followed by subsequent work including Scaling Monosemanticity

---

## Methodology

The core method treats the problem of extracting interpretable features from neural network activations as a **dictionary learning** problem. A sparse autoencoder (SAE) is trained on the activation vectors from a specific layer of the transformer. The SAE has an encoder that maps activations to a high-dimensional sparse representation, and a decoder that reconstructs the original activations from that sparse code. The sparsity constraint — enforced via an L1 penalty on the hidden layer — encourages the SAE to find a dictionary of features such that any given activation can be described using only a small number of active features at once.

The authors apply this approach to the MLP layer output of a one-layer transformer with 512 neurons, training SAEs with varying numbers of dictionary elements (ranging from 512 to 16,384). The key insight is that if features in the model are genuinely sparse (i.e., each feature is only active for a small fraction of inputs), then sparse autoencoders can in principle recover those features even when they are stored in superposition across neurons. The reconstruction quality is measured by the fraction of variance explained, and interpretability is measured through both automated scoring (using a separate LLM to evaluate feature interpretability) and human evaluation.

For causal validation, the authors perform **activation patching** experiments: they manually set individual SAE feature activations to high values and observe the effect on model outputs. This confirms that the extracted features are not merely correlational but genuinely causally drive model computations. The causal tests include feature ablation (zeroing out features) and feature amplification (increasing feature values), with both types of intervention producing interpretable, predictable changes in model behavior consistent with the feature's semantic meaning.

---

## Main Results

- A 512-neuron one-layer transformer MLP layer was successfully decomposed into **4,096 interpretable features** using a sparse autoencoder with an expansion factor of 8×
- Individual features were found to correspond to highly specific, human-interpretable concepts: DNA sequences, legal language, HTTP protocol tokens, Hebrew text, nutrition label content, and many others
- **Automated interpretability scoring** showed SAE features are significantly more interpretable than individual neurons across all expansion factors tested
- Causal experiments confirmed that activating individual features produces semantically coherent changes to model outputs, validating that features are genuine computational units rather than post-hoc correlates
- Features exhibit clean geometry: they tend to be approximately orthogonal to one another and align with interpretable directions in activation space
- The superposition hypothesis is empirically confirmed: neurons are demonstrably polysemantic, but the underlying features are monosemantic
- Larger dictionaries (more SAE features) consistently yield higher-quality, more specific features, suggesting the approach continues to improve with scale

---

## Limitations & Future Work

- The paper studies only a **one-layer toy transformer**, raising questions about whether the approach scales to deeper, more capable models (addressed by the follow-up Scaling Monosemanticity paper)
- SAE training introduces an **L1 reconstruction-interpretability tradeoff**: increasing sparsity improves feature interpretability but degrades reconstruction fidelity
- The completeness of the extracted feature dictionary is unknown — it is not clear how many true features exist in the model and whether the SAE has found all of them
- **Attention layers** are not studied; the analysis focuses only on MLP activations, leaving open whether the same approach works for attention
- Human interpretability scoring is expensive and slow, making evaluation at very large scales difficult without improved automated methods
- The relationship between SAE features and the model's actual computational circuits (how features interact across layers) is not studied here, motivating subsequent circuit-tracing research

---

## Why This Matters for AI Practitioners

This paper established the **sparse autoencoder (SAE) paradigm** as the dominant methodology for mechanistic interpretability research. Before this work, interpretability was largely limited to studying individual neurons — which are polysemantic and thus difficult to interpret — or to small hand-crafted circuits in toy models. The dictionary learning framing reframes the problem: instead of asking "what does this neuron do?" we ask "what features does this model represent, and where are they?"

For AI safety practitioners, the causal validation results are particularly important: the extracted features are not just passive descriptors of model behavior but active computational ingredients. This means that in principle, one could identify features corresponding to dangerous or deceptive behaviors, and either suppress them or monitor for their activation. The paper directly motivates the Scaling Monosemanticity work applied to Claude 3 Sonnet, and the broader program of using SAEs to find safety-relevant internal representations in frontier models.

For ML engineers building or deploying LLMs, the methodology provides a systematic toolkit for auditing what concepts a model has learned: the SAE can be trained as a post-hoc probe on any frozen model's activations without retraining the model itself.
