---
title: "COMPOSITE-STEM: Expert-Curated STEM Benchmark"
authors: Kyle Waters, Lucas Nuzzi, Tadhg Looram, Alessandro Tomasiello, Ariel Ghislain Kemogne Kamdoum, Bikun Li, Damien Sileo, Egor Kretov, Francesco Fournier-Facio, Georgios Soloupis, Haile Kassahun, Hew Wolff, Jiaqi Cai, Lianghui Li, Marc Roth, Mohinder Naiya, Naixu Guo, Qicheng Tang, Richard Wheeler, Samuele Sala, Serguei Popov, Steven Dillmann, Yuqi Li
published: 2026-04-10
source: "https://arxiv.org/abs/2604.09836"
---

# COMPOSITE-STEM: 70 Expert-Curated Agentic Tasks Across Physics, Biology, Chemistry, and Math

**Authors**: Kyle Waters, Lucas Nuzzi, Tadhg Looram (PortexAI), Alessandro Tomasiello, Ariel Ghislain Kemogne Kamdoum, Bikun Li, Damien Sileo, Egor Kretov, Francesco Fournier-Facio, Georgios Soloupis, Haile Kassahun, Hew Wolff, Jiaqi Cai, Lianghui Li, Marc Roth, Mohinder Naiya, Naixu Guo, Qicheng Tang, Richard Wheeler, Samuele Sala, Serguei Popov, Steven Dillmann, Yuqi Li  
**Published**: April 10, 2026 (v1); revised April 16, 2026 (v2)  
**Source**: https://arxiv.org/abs/2604.09836  
**arXiv ID**: 2604.09836  
**Categories**: cs.AI, cs.CL, cs.LG  
**Dataset**: https://huggingface.co/datasets/portex/COMPOSITE-STEM  
**Code**: https://github.com/portex-ai/portex-composit-harbor-adapter

## Abstract

AI agents hold growing promise for accelerating scientific discovery; yet, a lack of frontier evaluations hinders adoption into real workflows. This work introduces COMPOSITE-STEM, a benchmark featuring 70 expert-written tasks spanning physics, biology, chemistry, and mathematics, curated by doctoral-level researchers. The benchmark combines exact-match grading with criterion-based rubrics and an LLM-as-jury grading protocol to assess scientifically valid outputs. Using an adapted multimodal Terminus-2 agent harness within the Harbor evaluation framework, four frontier models were evaluated, with the top performer (Claude-opus-4.6) achieving 21.4% accuracy (Pass@1). All tasks are open-sourced to support reproducibility and further research.

## 1. Introduction

Existing expert-grade benchmarks for AI evaluation have been reaching saturation: frontier models increasingly score near ceiling on datasets like GPQA and HLE, making it difficult to distinguish capability differences among top systems. Meanwhile, practical scientific workflows require agents to reason, compute, and interact with domain-specific tools in executable environments — capabilities not tested by static question-answering formats.

COMPOSITE-STEM addresses this gap by introducing a cross-domain STEM task bundle compatible with Harbor agentic evaluation. The benchmark evaluates "more than isolated scientific reasoning by pairing expert-authored tasks with executable environments and flexible grading." Tasks require agents to write and execute code, install scientific packages, interpret results, and produce answers verified against expert-curated rubrics.

The benchmark's key design goal is difficulty calibration for frontier systems: the top performer achieves only 21.4%, indicating substantial headroom for improvement and reliable discrimination between model capabilities.

### 1.1 Positioning Within Benchmark Evolution

The paper contextualizes COMPOSITE-STEM within the trajectory of AI benchmarking:

- **Static QA benchmarks** (GPQA, HLE): high-quality questions but no executable environment; increasingly saturated
- **Terminal-Bench 2.0**: executable environments for general tasks
- **GDPval, APEX**: realistic professional tasks
- **FrontierScience**: most directly related; introduces "10-point rubrics with multiple independent criteria" for open-ended scientific answers

COMPOSITE-STEM builds on FrontierScience's rubric approach while adding cross-domain coverage, Harbor compatibility, and the AsymmetryZero grading framework.

## 2. Task Composition

### 2.1 Domain Distribution

The benchmark contains **70 expert-written tasks** distributed across four STEM domains:

| Domain | Tasks | Proportion |
|--------|-------|-----------|
| Physics | 20 | 28.6% |
| Chemistry | 23 | 32.9% |
| Biology | 20 | 28.6% |
| Mathematics | 7 | 10.0% |
| **Total** | **70** | **100%** |

### 2.2 Reference Assets

- **18 of 70 tasks** include mounted reference files
  - 17 tasks with PNG images
  - 1 task with PDF document
- Images serve as problem inputs (molecular diagrams, experimental data, microscopy images)
- Provided as native multimodal input in the agent's first turn

### 2.3 Grading Distribution

| Grading Method | Tasks | Description |
|----------------|-------|-------------|
| Exact-match | 35 | Deterministic solutions; numeric or string comparison |
| LLM-jury (semantic) | 34 | Five frontier models vote on semantic correctness |
| Hybrid | 1 | Combines exact-match and LLM-jury |

**Rubric criteria**: average 2.6 criteria per task; range 1–40 criteria (the outlier being a task with an unusually detailed rubric)

### 2.4 Expert Curation Process

Contributors include doctoral researchers, distinguished faculty, postdoctoral scientists, and industry practitioners from leading institutions including MIT, Stanford, Cambridge, EPFL, and ETH Zurich. Many previously contributed to Humanity's Last Exam (HLE) and related frontier benchmarks. The team conducted "detailed calls and review cycles" with contributors to refine task design and validate scientific accuracy.

Tasks represent genuine scientific problem-solving rather than simplified proxies, requiring accurate application of domain-specific knowledge, appropriate use of scientific software libraries, and methodologically sound reasoning.

## 3. Evaluation Methodology

### 3.1 Agent Harness: Adapted Multimodal Terminus-2

Agents are evaluated using an adapted Terminus-2 harness within the Harbor framework:
- Supports multimodal inputs (images and text) in the first agent turn
- Provides a terminal interface for code execution
- Max turns: 10 per task

### 3.2 Sandbox Configuration

| Parameter | Value |
|-----------|-------|
| CPUs | 1 |
| Memory | 2048 MB |
| Storage | 10240 MB |
| Timeout | 3600 seconds (1 hour) |
| Base image | Python 3.12-slim |
| Pre-installed tools | bash, git, curl, ripgrep, tmux, asciinema, litellm |
| Scientific packages | numpy, scipy, matplotlib, pandas, rdkit, biopython, etc. |

Agents can install additional packages during task execution using apt-get or pip, reflecting realistic scientific computing workflows.

### 3.3 Grading Protocol: AsymmetryZero

AsymmetryZero operationalizes expert preferences as "stable, auditable semantic contracts." The framework is designed for flexible, criterion-centric evaluation:

**Criterion specification**: Each criterion defines:
- Weight (contribution to final score)
- Grader type (exact-match or LLM-jury)
- Instruction (what constitutes a passing response)

**LLM-jury composition** (five models via majority voting):
- DeepSeek-v3.2
- GLM-5
- GPT-oss-120b
- Llama-3.3-70b-instruct
- Kimi-K2.5

**Aggregation**: Strict majority voting for semantic criteria; weighted point aggregation normalized to Harbor's reward scalar (0.0–1.0).

The jury composition deliberately uses a diverse set of models to avoid bias toward any single model family's reasoning patterns.

## 4. Model Results

### 4.1 Leaderboard (Pass@1)

| Model | Pass Rate | Avg Time | Avg Steps | Input Tokens | Output Tokens |
|-------|-----------|----------|-----------|--------------|---------------|
| Claude-opus-4.6 | **21.4%** | 11m 30s | 5.6 | 156.0K | 21.1K |
| Gemini-3.1-pro | 18.6% | 9m 16s | 6.7 | 36.2K | 18.4K |
| Grok-4.20-beta | 5.7% | 6m 3s | 3.3 | 20.6K | 4.7K |
| GPT-5.4 | 4.3% | 6m 5s | 2.6 | 17.4K | 2.4K |

Top performer: Claude-opus-4.6 at 21.4%, indicating the benchmark effectively discriminates frontier model capabilities while leaving substantial room for improvement.

### 4.2 Failure Mode Analysis

Failures are classified into two categories:

| Failure Type | Definition | Claude-opus-4.6 | Gemini-3.1-pro | GPT-5.4 | Grok-4.20-beta |
|-------------|-----------|-----------------|----------------|---------|----------------|
| **Solution Error** | Submitted answer graded incorrect | 63.0% | 46.4% | 90.9% | — |
| **Submission Error** | Failed to deliver valid artifact or hit max turns | 37.0% | 53.6% | 9.1% | — |

Key observations:
- Claude and Gemini primarily fail via solution errors (wrong answers submitted) — they engage with problems but reason incorrectly
- Gemini shows high submission error rate (53.6%), suggesting it more frequently fails to complete tasks within the turn budget
- GPT-5.4 has 90.9% solution errors: it submits answers but they are mostly wrong
- This pattern suggests GPT-5.4 and Grok lack the domain tool proficiency needed for correct solutions

### 4.3 Judge Agreement Patterns

Stronger models show **higher judge disagreement** (more split jury votes), suggesting "partially correct or borderline responses." Weaker models receive unanimous failures, indicating outright incorrect answers rather than grading bias.

This pattern validates the LLM-jury protocol: disagreement correlates with genuine solution quality rather than grader inconsistency.

## 5. Behavioral Analysis

### 5.1 Tool Utilization

| Behavior | Claude-opus-4.6 | Gemini-3.1-pro | GPT-5.4 | Grok-4.20-beta |
|----------|-----------------|----------------|---------|----------------|
| Package installation (~% of runs) | ~30% | ~30% | ~3% | ~3% |
| Avg steps (tool-using runs) | ~10 | ~10 | — | — |
| Avg steps (minimal-tool runs) | — | — | ~3.8 | ~4.5 |
| Pass rate (minimal-tool runs) | ~3–5% | ~3–5% | ~3–5% | ~3–5% |

**Critical finding**: Runs where agents install packages and actively use scientific libraries achieve pass rates around 10× higher than minimal-tool runs. Package installation (rdkit, biopython, etc.) is strongly predictive of success on domain-specific chemistry and biology tasks.

### 5.2 Step Budget Analysis

- Claude-opus-4.6: ~6.5 average steps (well within 10-turn budget)
- Gemini-3.1-pro: ~8 average steps (highest engagement)
- GPT-5.4: ~2.6 average steps (lowest; suggests early termination)
- Grok-4.20-beta: ~3.3 average steps

More steps correlate with better performance, consistent with extended reasoning chains and iterative tool use.

## 6. Case Study: Chemistry Task 0sL35u

**Task**: Determine the number of hydrogen atoms from a complex SMILES notation string representing a large organic molecule.

**Claude-opus-4.6 trajectory** (PASS):
1. Recognized SMILES as requiring chemical informatics library
2. Installed `python3-rdkit` via apt-get
3. Used RDKit to parse the SMILES string
4. Derived molecular formula: C280H350Br5Cl2I2N23O75S3
5. **Answer: 350** ✓

**GPT-5.4 trajectory** (FAIL):
1. Attempted rdkit installation — failed
2. Attempted openbabel installation — failed
3. Attempted pip installation paths — all failed
4. Pivoted to custom Python SMILES parser with hand-coded valence rules
5. **Answer: 399** ✗ (exact-match grading)

**Lesson**: "Persistence toward robust domain tool succeeded, while fragile hand-rolled workaround failed." This case illustrates that domain tool proficiency — knowing which library to use and how to install it — is a distinct capability from general coding skill.

## 7. Limitations

The authors acknowledge several limitations:

1. **External audit**: The benchmark "did not undergo a full external audit and quality-control and peer-review pipeline equivalent to a formal academic benchmark consortium." Contributors underwent vetting from previous benchmarking efforts (HLE, etc.), but this is not equivalent to formal peer review.

2. **Pass@1 only**: Only single-run Pass@1 statistics are reported. Variance from repeated runs is not quantified, which may obscure stochastic performance differences.

3. **Fixed turn budget**: The max_turns=10 constraint may limit agent performance, particularly for tasks that could benefit from extended iterative refinement.

4. **Jury subjectivity**: Despite majority voting, LLM-jury grading introduces subjective judgment for borderline cases. The five-model jury mitigates but does not eliminate this.

5. **Domain balance**: Mathematics is underrepresented (7 tasks vs 20–23 for other domains), potentially reducing statistical reliability of math-specific conclusions.

## 8. Conclusion

COMPOSITE-STEM addresses the growing gap between saturated expert benchmarks and realistic agentic evaluation. By pairing expert-authored tasks with executable environments and flexible grading via AsymmetryZero, it provides a reliable evaluation signal for scientific agent capabilities.

Key findings:
1. Current frontier models achieve only 21.4% on expert-curated scientific tasks — significant headroom remains
2. Tool proficiency (package installation, scientific library use) is strongly predictive of success
3. Extended reasoning and iterative tool use correlate with better performance
4. The LLM-jury protocol produces meaningful disagreement patterns that reflect genuine solution quality
5. Behavioral gaps between top and bottom models are large: Claude and Gemini vs GPT/Grok show ~5× performance difference

COMPOSITE-STEM is open-sourced to encourage community adoption and further development of capable scientific agents.

## Open-Source Resources

- **Dataset**: https://huggingface.co/datasets/portex/COMPOSITE-STEM
- **Harbor adapter**: https://github.com/portex-ai/portex-composit-harbor-adapter
- **AsymmetryZero framework**: https://github.com/portex-ai/asymmetry_zero (MIT License)
- **Portex Datalab**: https://datalab.portexai.com

## References

- Boiko et al. (2023). "Emergent autonomous scientific research capabilities of large language models." arXiv:2304.05332.
- Chan et al. (2024). "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering." arXiv:2410.07095.
- Hendrycks et al. (2021). "Measuring Massive Multitask Language Understanding." ICLR 2021.
- Jain et al. (2024). "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code." arXiv:2403.07974.
- Kwa et al. (2025). "GDPval: Evaluating agents on realistic professional tasks."
- Lewkowycz et al. (2022). "Solving quantitative reasoning problems with language models." NeurIPS 2022.
- Phan et al. (2025). "Humanity's Last Exam." arXiv:2501.14249.
- Rein et al. (2023). "GPQA: A Graduate-Level Google-Proof Q&A Benchmark." arXiv:2311.12022.
- Terminal-Bench Team (2025). "Terminal-Bench 2.0: Evaluating Agents in Terminal Environments."
- Waters et al. (2026). "COMPOSITE-STEM: 70 Expert-Curated Agentic Tasks." arXiv:2604.09836.
- White et al. (2025). "FrontierScience: Open-ended Scientific Question Answering." arXiv:2502.07780.
