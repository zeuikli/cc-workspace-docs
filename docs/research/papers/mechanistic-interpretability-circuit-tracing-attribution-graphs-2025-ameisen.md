# Circuit Tracing: Revealing Computational Graphs in Language Models

**Authors:** Emmanuel Ameisen, Jack Lindsey, Adam Pearce, Wes Gurnee, Nicholas L. Turner, Brian Chen, Craig Citro, David Abrahams, Shan Carter, Basil Hosmer, Jonathan Marcus, Michael Sklar, Adly Templeton, Trenton Bricken, Callum McDougall, Hoagy Cunningham, Thomas Henighan, Adam Jermyn, Andy Jones, Andrew Persic, Zhenyi Qi, T. Ben Thompson, Sam Zimmerman, Kelley Rivoire, Thomas Conerly, Chris Olah, Joshua Batson

**Year:** 2025

**Published:** March 27, 2025

**Venue/Publisher:** Transformer Circuits Thread (Anthropic)

**ArXiv:** N/A (published at transformer-circuits.pub)

**URL:** https://transformer-circuits.pub/2025/attribution-graphs/methods.html

---

## Abstract

This paper introduces a methodology for uncovering the computational mechanisms underlying language model behaviors by constructing attribution graphs — directed computational graphs that trace information flow from input tokens to output predictions on specific prompts. The key innovation is replacing MLP components with interpretable cross-layer transcoders (CLTs) that extract sparsely-active features spanning multiple layers. Combined with frozen attention patterns and error adjustments, this produces a local replacement model that faithfully approximates the underlying model while being fully interpretable. Case studies on factual recall, addition, and acronym generation demonstrate step-by-step descriptions of model computation, with application to Claude 3.5 Haiku.

---

## Key Contributions

- **Cross-layer transcoders (CLTs):** novel architecture that extracts sparsely-active features spanning multiple model layers simultaneously, overcoming a key limitation of per-layer SAEs where features computed over multiple residual stream transformations are artificially split across layer boundaries
- **Attribution graph framework:** systematic methodology for tracing information flow through features from inputs to outputs for any specific prompt, producing a human-readable directed graph of computational steps
- **Local replacement model:** approach combining CLT features with frozen attention patterns and error adjustment nodes to faithfully approximate underlying model behavior on specific prompts — enabling mechanistic analysis that is simultaneously accurate and interpretable
- **Interactive open-source visualization tools** for navigating complex computational graphs and testing hypotheses by modifying individual feature values, making circuit analysis accessible without deep ML infrastructure
- **Comprehensive perturbation-based validation** demonstrating mechanistic faithfulness of identified circuits: circuits are validated by patching in modified feature values and measuring whether model outputs change as predicted by the circuit structure
- **Application at scale to Claude 3.5 Haiku**, providing the most detailed circuit-level account of a frontier model to date — covering factual recall, arithmetic, and linguistic pattern tasks with mechanistic precision
- **Global circuit analysis methods** for understanding how feature interactions generalize across multiple prompts, including techniques for handling "interference" in virtual weights when aggregating attributions

---

## Methodology

The central methodological innovation is the **cross-layer transcoder (CLT)**. Prior work (SAEs trained per layer) approximated MLP computations layer by layer, requiring features computed over multiple residual stream updates to be re-identified at each new layer — an artificial decomposition that obscured computational continuity. CLTs instead learn to predict the total effect of a contiguous sequence of MLP layers on the residual stream in a single forward pass, extracting a dictionary of features that are active sparsely across the full span. This allows features that participate in multi-layer computations (such as multi-step reasoning or compositional operations) to be identified as single coherent units rather than fragmented across layer-specific SAEs.

The **local replacement model** is constructed by swapping the trained model's MLP components with the CLTs and freezing the attention patterns as computed by the original model. The attention patterns are not replaced but left as-is: attention weights capture which tokens attend to which other tokens, and these patterns are kept intact because the focus of the methodology is on the MLP-driven feature computations. Error adjustment nodes are added to account for the residual approximation error of the CLTs, ensuring that the total residual stream value at each layer accurately matches the original model's activations. The result is a model that computes identical outputs to the original but whose computation is expressed entirely in terms of interpretable CLT features and attention patterns.

**Attribution graphs** are constructed from the local replacement model using gradient-based attribution: for each feature active on a given prompt, the contribution of every upstream feature to that feature's activation is computed via a linearized gradient pass. These pairwise attributions are aggregated into a directed graph where nodes are features (and attention patterns) and edges are weighted by attribution strength. The graph is then pruned by removing low-weight edges, leaving a sparse but mechanistically faithful subgraph that constitutes the circuit for the given behavior. This graph can be interactively explored: hovering over nodes reveals what the feature represents (via maximum activating examples), and modifying edge weights or node activations reveals how the circuit's output changes.

---

## Main Results

- **Factual recall circuits** for statements like "The capital of France is Paris" were traced end-to-end: input token features encoding the country name activate stored "capital city" association features that in turn activate the output token for the correct city, with the full computational path spanning multiple layers and identifiable at each step
- **Addition circuits** for simple arithmetic (e.g., 3 + 5 = 8) were recovered, showing that the model represents intermediate summand values as features and uses MLP computations to combine them, with clear separation between the "operand representation" phase and the "summation" phase
- **Acronym generation** (producing "NATO" from "North Atlantic Treaty Organization") was analyzed, revealing features that encode the first-letter positions of constituent words and features that compose them into the output acronym
- **Validation via patching:** in all three case studies, manually setting features to values inconsistent with the proposed circuit mechanism (e.g., swapping a "France" feature for a "Germany" feature) produced exactly the output shifts predicted by the circuit structure, confirming mechanistic faithfulness
- The CLT architecture achieves **lower reconstruction error** than equivalent per-layer SAEs while using the same or fewer total features, demonstrating that cross-layer span is a genuine architectural improvement
- Application to **Claude 3.5 Haiku** produced attribution graphs that are qualitatively similar in structure to those found in smaller models, suggesting that the circuit-tracing methodology generalizes across model scales

---

## Limitations & Future Work

- The **local replacement model** is prompt-specific: a new attribution graph must be constructed for each prompt, making large-scale circuit analysis computationally expensive and preventing easy generalization to "the circuit for task X" across diverse inputs
- **Attention patterns are frozen** and not decomposed into interpretable components; the methodology treats attention as a black box, leaving the mechanism by which attention weights are computed unanalyzed
- **Error adjustment nodes** absorb residual approximation error and appear in attribution graphs as unexplained edges, potentially masking important computational steps that the CLTs have not captured
- The methodology has been applied to only a **subset of task types** (factual recall, arithmetic, pattern completion); whether the approach generalizes cleanly to complex multi-step reasoning, open-ended generation, or adversarial robustness is not demonstrated
- **Causal completeness** is validated by perturbation experiments but not formally proven; the circuits identified may be sufficient for the studied prompts without being necessary (there may be redundant pathways not captured)
- The **global circuit aggregation** across multiple prompts remains methodologically early-stage; interference in virtual weights makes cross-prompt generalization difficult and the aggregated circuits may not cleanly represent general-purpose circuits in the model

---

## Why This Matters for AI Practitioners

This paper represents the state of the art in **mechanistic interpretability at the circuit level** for frontier models. While prior work (Towards Monosemanticity, Scaling Monosemanticity) established that individual features inside models are interpretable, this work goes further by asking how those features interact to produce specific behaviors. The attribution graph framework provides a principled answer: for any given input and output, one can construct a computational graph that shows exactly which features were activated, how they influenced each other, and which ones were causally responsible for the output.

For **AI safety**, the implications are substantial. If the circuits underlying behaviors like "refusing dangerous requests," "producing honest responses," or "following instructions" can be identified at the feature level, then safety audits can move beyond behavioral testing to mechanistic verification. A model that has been steered to refuse harmful requests via RLHF may have done so through superficial output-level changes, or through genuine internalization of safety-relevant reasoning circuits — and circuit tracing provides, for the first time, a methodology for distinguishing these cases.

For **AI engineers**, the open-source interactive visualization tools lower the barrier for applying circuit analysis to custom models. The CLT architecture can be trained on any transformer with accessible activations, and the attribution graph methodology requires only gradient access — meaning that practitioners can begin applying this approach to their own models without reproducing the full Anthropic research pipeline.
