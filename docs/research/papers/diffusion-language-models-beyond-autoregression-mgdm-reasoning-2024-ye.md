# Beyond Autoregression: Discrete Diffusion for Complex Reasoning and Planning

**Authors:** Jiacheng Ye, Jiahui Gao, Shansan Gong, Lin Zheng, Xin Jiang, Zhenguo Li, Lingpeng Kong
**Year:** 2024 (submitted October 18, 2024; revised February 18, 2025)
**Venue:** ICLR 2025
**ArXiv:** https://arxiv.org/abs/2410.14157

---

## Abstract

This paper addresses how autoregressive language models struggle with complex reasoning and long-term planning tasks. The authors propose discrete diffusion models as an alternative and introduce Multi-Granularity Diffusion Modeling (MGDM), which prioritizes learning difficult subgoals by addressing what they call subgoal imbalance. On complex tasks like Countdown, Sudoku, and Boolean Satisfiability Problems, MGDM significantly outperforms autoregressive models without using search techniques, achieving 91.5% and 100% accuracy on Countdown and Sudoku, respectively, compared to 45.8% and 20.7% for autoregressive models.

---

## Key Contributions

- Identifies and formalizes the subgoal imbalance problem: in complex reasoning tasks with global constraints, AR models cannot revise earlier tokens based on later context, causing cascading errors that diffusion models structurally avoid
- Proposes Multi-Granularity Diffusion Modeling (MGDM) that dynamically prioritizes difficult subgoals during diffusion training by weighting the denoising objective according to per-position difficulty estimates
- Demonstrates dramatic accuracy gains over autoregressive baselines on Countdown (91.5% vs 45.8%), Sudoku (100% vs 20.7%), and Boolean SAT problems without using any search algorithms (beam search, MCTS, or backtracking)
- Establishes discrete diffusion as a fundamentally superior paradigm for planning and combinatorial reasoning tasks, not just a competitive alternative for fluency-focused generation
- Published at ICLR 2025 with open-source code, providing a reproducible benchmark for diffusion vs AR reasoning comparisons that future work can build on

---

## Methodology

The subgoal imbalance problem is defined as follows: in tasks requiring global constraint satisfaction (e.g., Sudoku, where every row, column, and box must contain each digit exactly once), different positions in the output have vastly different difficulty levels. An AR model must commit to each token left-to-right, making it impossible to revise a mistake at position 3 after observing at position 30 that the commitment was inconsistent with the global constraints. Diffusion models iteratively refine all positions jointly, meaning any token can be revised at any denoising step, enabling the model to propagate global constraint information bidirectionally.

MGDM extends standard discrete diffusion by weighting the denoising loss at each position according to estimated difficulty. Positions corresponding to difficult subgoals — those where the model is most uncertain or most frequently makes errors — receive higher weight in the training objective. This encourages the model to allocate more representational capacity to hard subgoals rather than averaging over easy and hard positions equally. The difficulty estimates are computed online during training using the model's own uncertainty (e.g., entropy of the predicted distribution at each position), making MGDM a form of curriculum learning embedded directly into the diffusion training objective.

The multi-granularity aspect refers to difficulty operating at multiple scales simultaneously: token-level difficulty (individual tokens that are hard to predict), subgoal-level difficulty (coherent subsequences that are structurally hard, such as a row in Sudoku), and solution-level difficulty (globally hard problem instances). MGDM estimates and weights all three granularities, allowing the model to simultaneously learn fine-grained token prediction and coarser structural reasoning patterns. At inference, standard discrete diffusion sampling is used without any search, test-time compute tricks, or reranking — the performance gains are entirely from training.

---

## Main Results

- Countdown (arithmetic reasoning): MGDM achieves 91.5% accuracy vs 45.8% for autoregressive models — a 2x improvement without search
- Sudoku (combinatorial constraint satisfaction): MGDM achieves 100% accuracy vs 20.7% for autoregressive models — a 5x improvement without search
- Boolean Satisfiability Problems: MGDM significantly outperforms AR baselines on SAT instances of varying difficulty, with the gap widening as problem difficulty increases
- No search techniques used: all results are from single-pass inference (multiple denoising steps, but no backtracking, beam search, or MCTS), making the comparison fair and the efficiency advantage clear
- Ablation studies confirm that multi-granularity weighting contributes substantially over standard discrete diffusion, validating the MGDM-specific design choices

---

## Limitations & Future Work

- Evaluation is limited to synthetic combinatorial tasks (Countdown, Sudoku, SAT); generalization to real-world planning tasks (robotics, code generation with complex dependencies, multi-step mathematical proofs) requires further study
- MGDM requires online difficulty estimation during training, which adds computational overhead compared to standard discrete diffusion training; the cost is not fully characterized in the paper
- The comparison to AR models does not include AR models augmented with search (e.g., MCTS-guided AR, best-of-N sampling with a verifier), which can substantially close the gap on structured tasks
- Inference requires multiple denoising steps; while no search is used, the total compute per sample is higher than a single AR forward pass for the same sequence length
- Future work should examine whether MGDM generalizes to tasks with softer constraint structures (natural language reasoning, mathematical proof) where subgoal difficulty is harder to define precisely

---

## Why This Matters for AI Practitioners

This paper reframes the diffusion vs autoregressive debate: rather than competing on fluency and perplexity (where AR models have a head start), it identifies a class of tasks — global constraint satisfaction and combinatorial planning — where diffusion models have a structural architectural advantage. The numbers are striking: 100% vs 20.7% on Sudoku without search is not a marginal improvement but a qualitative capability difference. For practitioners building systems that must generate outputs satisfying global constraints — scheduling, code synthesis with type constraints, structured data generation, mathematical problem solving — this is a strong argument for evaluating diffusion architectures. The no-search caveat is important: AR models with MCTS or verifier-guided search can approach these numbers, but that requires significantly more inference compute. MGDM achieves high accuracy with simple ancestral sampling, which is cheaper and easier to deploy. The ICLR 2025 publication and open-source code make this directly usable as a research baseline.
