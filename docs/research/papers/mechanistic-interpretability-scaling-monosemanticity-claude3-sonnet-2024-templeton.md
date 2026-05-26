# Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

**Authors:** Adly Templeton, Tom Conerly, Jonathan Marcus, Jack Lindsey, Trenton Bricken, Brian Chen, Adam Pearce, Craig Citro, Emmanuel Ameisen, Andy Jones, Hoagy Cunningham, Nicholas L Turner, Callum McDougall, Monte MacDiarmid, Alex Tamkin, Esin Durmus, Tristan Hume, Francesco Mosconi, C. Daniel Freeman, Theodore R. Sumers, Edward Rees, Joshua Batson, Adam Jermyn, Shan Carter, Chris Olah, Tom Henighan

**Year:** 2024

**Venue/Publisher:** Transformer Circuits Thread (Anthropic)

**ArXiv:** N/A (published at transformer-circuits.pub)

**URL:** https://transformer-circuits.pub/2024/scaling-monosemanticity/

---

## Abstract

This paper demonstrates that sparse autoencoders scale successfully to production-level large language models. The authors trained SAEs on the middle-layer residual stream of Claude 3 Sonnet and extracted 34 million latent features. They demonstrate that scaling laws apply to SAE training and that the extracted features at this scale are highly abstract and diverse — responding to and causally influencing complex behaviors. The work addresses the key open question of whether monosemantic feature extraction was feasible for frontier models, and provides the first window into the internal feature representations of a state-of-the-art commercial LLM.

---

## Key Contributions

- **First demonstration that sparse autoencoders scale to production frontier LLMs** (Claude 3 Sonnet), extracting 34 million features — a 4,000× expansion over prior one-layer experiments and the first interpretability result on a state-of-the-art commercial model
- **Empirical evidence that SAE training follows predictable scaling laws**, enabling principled SAE design: loss decreases as a power law in both number of features and amount of training data
- **Discovery of highly abstract, multimodal features** encoding concepts like emotions, ethical stances, bias, country-specific associations, and safety-relevant behaviors that span text and (in some cases) visual modalities
- **Feature steering experiments** showing causal control over model behavior by directly activating or suppressing individual features, including demonstrations that activating a "banana" feature causes the model to write about bananas regardless of prompt context
- **Interpretability of safety-critical features** including features for deception, manipulation, dangerous knowledge domains, and potential indicators of model self-representation — directly relevant to AI safety
- **Quantitative evaluation framework** for feature quality at scale using automated interpretability scoring with LLM judges, enabling systematic comparison across SAE sizes
- **Middle-layer residual stream focus**: demonstrates that residual stream activations (rather than MLP outputs alone) are a viable and information-rich target for SAE training at scale

---

## Methodology

The authors train sparse autoencoders on the **residual stream activations** at the middle layer of Claude 3 Sonnet. The SAE architecture follows the approach established in "Towards Monosemanticity" but with significant engineering adaptations for scale: the model has billions of parameters, and the training dataset consists of a large corpus of text drawn from Claude's training distribution. SAEs of varying sizes — from 1 million to 34 million features — are trained, enabling the empirical study of scaling laws.

The key training challenge at this scale is computational: training a 34-million-feature SAE on a frontier model requires processing billions of activations and managing a dictionary that is orders of magnitude larger than a model's neuron count. The authors use efficient batched training with careful learning rate scheduling and sparsity tuning. The L1 penalty coefficient is calibrated to achieve a target sparsity level (typically 20–100 active features per token), balancing reconstruction quality against feature interpretability. The resulting SAEs are evaluated on held-out activations using the fraction of variance explained and the L0 norm (average number of active features).

For feature interpretation, the authors use a combination of **maximum activating example analysis** (finding input texts that activate each feature most strongly), **automated interpretability scoring** (prompting a separate LLM to predict feature activations from a proposed interpretation and comparing against ground truth), and **causal intervention experiments** (directly clamping feature activation values to high or low values and measuring effects on model outputs). The causal steering methodology is extended to study multi-feature interactions: activating a cluster of related features produces coherent thematic shifts in model outputs.

---

## Main Results

- SAEs with up to **34 million features** were successfully trained on Claude 3 Sonnet residual stream activations, with reconstruction quality (fraction of variance explained) exceeding 60% for the largest models
- SAE training loss follows a **predictable power law** in both number of features and training tokens, suggesting that SAE capability can be forecast without exhaustive grid search
- Features at this scale are **qualitatively more abstract** than those found in one-layer models: rather than specific token patterns, they encode concepts like "the Golden Gate Bridge," "the concept of trust," "the emotion of frustration," and country-specific cultural associations
- **Safety-relevant features were discovered**, including features that activate on text about deception, manipulation tactics, dangerous chemical synthesis, and potential self-referential features encoding the model's own identity
- **Feature steering demonstrations**: directly activating the "banana" feature caused the model to spontaneously write about bananas; activating a "Golden Gate Bridge" feature caused persistent self-identification as the bridge across conversation turns
- Automated interpretability scores are substantially higher for SAE features than for individual neurons at matched computational cost, confirming that monosemanticity scales
- Features show **cross-lingual generalization**: a feature that activates on English text about a concept often activates on equivalent text in French, Spanish, Chinese, and other languages

---

## Limitations & Future Work

- Analysis is limited to a **single middle layer** of Claude 3 Sonnet; how features in different layers interact, and whether the full model can be understood layer by layer, remains open
- **34 million features may still be incomplete**: the model likely represents far more distinct concepts, and the relationship between SAE dictionary completeness and model capability is unknown
- Causal steering experiments show that features influence behavior, but **multi-feature interactions** are complex — activating one feature can suppress or amplify related features in ways that are not fully characterized
- The **computational cost** of training and storing 34-million-feature SAEs is substantial, potentially limiting accessibility for researchers without Anthropic-scale resources
- **Attention heads are not studied**; all results concern MLP/residual stream features, leaving attention mechanisms as a major interpretability gap
- Safety-relevant features are identified but **no mechanistic account** of how those features are computed from inputs or how they influence outputs is given — that circuit-level account is addressed in subsequent attribution graph work

---

## Why This Matters for AI Practitioners

This paper is a landmark result demonstrating that mechanistic interpretability is not limited to toy models or simple architectures — it scales to frontier commercial LLMs. The discovery of 34 million interpretable features inside Claude 3 Sonnet fundamentally changes the AI safety landscape: it is now empirically established that production models represent human-understandable concepts internally, and that those internal representations can be accessed and steered from outside.

For AI safety researchers, the identification of safety-critical features (deception, manipulation, dangerous knowledge) raises the possibility of **interpretability-based monitoring**: deploying SAEs as inference-time probes to detect when a model is internally representing dangerous concepts, even if its output appears benign. The feature steering results demonstrate that these are not passive observations but active levers.

For ML engineers, the scaling laws result is practically valuable: it means SAE training can be planned and budgeted using predictable power-law extrapolations rather than expensive exploratory sweeps. The open question of whether these results replicate across model families (GPT, Gemini, Llama) and architectures makes this a natural starting point for cross-model interpretability audits.
