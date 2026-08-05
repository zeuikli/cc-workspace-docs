---
url: "https://arxiv.org/abs/2305.20050"
title: "Let's Verify Step by Step"
archived_date: 2026-06-09
arxiv_id: 2305.2005
authors: ["Hunter Lightman", "Vineet Kosaraju", "Yura Burda", "Harri Edwards", "Bowen Baker", "Teddy Lee", "Jan Leike", "John Schulman", "Ilya Sutskever", "Karl Cobbe"]
pdf_path: pdfs/2305.20050.pdf
published_date: 2023-05-31
---

# Let's Verify Step by Step

**Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe
**Year:** 2023
**Submitted:** May 31, 2023
**Venue:** ICLR 2024 (OpenAI)
**ArXiv:** https://arxiv.org/abs/2305.20050

---

## Abstract

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable multi-step reasoning models, we conduct a careful study of these two methods. We find that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised reward model (PRM) achieves 78% on a representative subset of MATH problems. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

---

## Key Contributions

- **Process supervision vs. outcome supervision**: Establishes empirically that providing step-level feedback during training significantly outperforms final-answer-only feedback for complex multi-step mathematical reasoning.
- **Process Reward Model (PRM)**: Introduces the PRM paradigm — a reward model trained to score the correctness likelihood of each individual intermediate reasoning step, enabling fine-grained verification of chain-of-thought reasoning.
- **78% accuracy on MATH**: The best PRM achieves 78% on a representative subset of MATH benchmark problems, setting a strong baseline for PRM-based verification.
- **Active learning for process supervision**: Shows that active learning (selecting data points where the model is most uncertain) substantially improves sample efficiency and final performance of process supervision compared to random data collection.
- **PRM800K dataset release**: Publishes 800,000 step-level human feedback labels — the dataset used to train all reward models — enabling reproducible PRM research and downstream use in inference-time scaling pipelines.
- **Foundation for best-of-N inference**: Provides the empirical and methodological basis for PRM-based best-of-N selection, which became a standard component in test-time compute scaling systems (including Snell et al. 2024, DeepSeek-R1, and o1).

---

## Methodology

The paper compares two supervision paradigms for training reward models on the MATH benchmark. **Outcome supervision (ORM)** trains a reward model to predict whether a complete solution reaches the correct final answer. The model receives a binary signal only at the end of each generation. This approach is inexpensive to label but provides sparse feedback — the model cannot distinguish between a correct intermediate step that leads to an incorrect final step and a fundamentally flawed reasoning chain.

**Process supervision (PRM)** trains a reward model to predict, at each intermediate reasoning step, whether that step is correct given the problem statement and prior steps. Human annotators label each step as positive, negative, or neutral. This provides dense, intermediate feedback, allowing the reward model to identify exactly where a reasoning chain goes wrong. At inference time, the PRM scores each step of a candidate solution, and the overall solution score is typically the minimum step score (the weakest link). This PRM score is then used to select the best candidate from a set of N generated solutions (best-of-N selection).

**Active learning** is used to improve labeling efficiency. Rather than randomly sampling problems and solutions for annotation, the authors identify problems where the model's predicted step-level correctness is most uncertain — prioritizing annotations that maximally improve PRM calibration. This substantially reduces the number of human labels required to achieve a given level of PRM accuracy, making process supervision more practical at scale.

---

## Main Results

- **PRM vs. ORM on MATH**: The best PRM reaches 78% accuracy on a representative MATH subset under best-of-N selection; the best ORM trained on equivalent data reaches lower accuracy.
- **Scaling best-of-N with PRM**: Performance improves consistently as N increases (more candidates generated), with PRM-based selection significantly outperforming random selection and ORM-based selection.
- **Active learning gain**: Active learning reduces the required annotation budget by approximately 2x compared to random sampling to reach equivalent PRM accuracy.
- **Step-level feedback localizes errors**: Qualitative analysis shows that PRMs correctly identify the specific step where a reasoning chain goes wrong in the majority of failure cases, confirming that step-level labels carry signal beyond final-answer supervision.
- **PRM800K quality**: The released dataset spans 800,000 step-level labels across 75,000 solutions to 12,000 MATH problems, covering all difficulty levels and mathematical subfields.

---

## Limitations & Future Work

- Human annotation of step-level correctness is expensive and does not scale trivially to domains without well-defined step boundaries (e.g., open-ended writing, multi-document reasoning).
- PRM training requires agreement between annotators on what constitutes a "step" — ambiguous in domains outside structured mathematical reasoning.
- The PRM is trained on human-written solutions from GPT-4; generalization to solutions from different model families may require retraining or domain adaptation.
- Best-of-N selection with PRM is a parallel scaling strategy — it generates N solutions independently. Combining PRM with sequential search (MCTS, beam search) is identified as future work.
- The benchmark is limited to the MATH dataset; generalization to other reasoning domains (science, coding, logical deduction) requires additional study.
- Future directions include automated step-level labeling, PRM training from RL feedback (rather than human labels), and integration with sequential search algorithms.

---

## Why This Matters for AI Practitioners

This paper is the **foundational work for process reward models**, which became a core component in virtually all subsequent test-time compute scaling systems. For practitioners, the key insight is that verifying reasoning at the step level — rather than only at the final answer — provides substantially better signal for selecting among candidate solutions at inference time. The PRM800K dataset release enabled the community to train and evaluate PRMs without the prohibitive cost of collecting step-level labels from scratch. The best-of-N selection paradigm described here is directly implemented in o1, DeepSeek-R1, and the Snell et al. compute-optimal scaling framework. Any practitioner building a reasoning pipeline that generates multiple candidates and selects among them is applying the core methodology of this paper. The active learning results also suggest a practical path to reducing annotation costs when fine-tuning PRMs for new domains.
