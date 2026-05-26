---
title: "AEC-Bench: A Multimodal Benchmark for Agentic Systems in Architecture, Engineering, and Construction"
authors: "Harsh Mankodiya, Chase Gallik, Theodoros Galanos, Andriy Mulyar"
published: "2026-03-31"
source: "https://arxiv.org/abs/2603.29199"
---

# AEC-Bench: A Multimodal Benchmark for Agentic Systems in Architecture, Engineering, and Construction

**Authors**: Harsh Mankodiya (harsh@nomic.ai), Chase Gallik (chase@nomic.ai), Theodoros Galanos (theodoros.galanos@aurecongroup.com), Andriy Mulyar (andriy@nomic.ai)  
**Institutions**: Nomic AI (Mankodiya, Gallik, Mulyar); Aurecon Group (Galanos)  
**Published**: March 31, 2026 (arXiv:2603.29199v1 [cs.AI])  
**Source**: https://arxiv.org/abs/2603.29199  
**Code**: https://github.com/nomic-ai/aec-bench  
**License**: Apache 2

## Abstract

The AEC-Bench is a multimodal benchmark for evaluating agentic systems on real-world tasks in the Architecture, Engineering, and Construction (AEC) domain. The benchmark covers tasks requiring drawing understanding, cross-sheet reasoning, and construction project-level coordination. This report describes the benchmark motivation, dataset taxonomy, evaluation protocol, and baseline results across several domain-specific foundation model harnesses. We use AEC-Bench to identify consistent tools and harness design techniques that uniformly improve performance across foundation models in their own base harnesses, such as Claude Code and Codex. We openly release our benchmark dataset, agent harness, and evaluation code for full replicability at https://github.com/nomic-ai/aec-bench under an Apache 2 license.

---

## 1 Introduction

Foundation models equipped with coding-agent harnesses demonstrate strong capabilities in software engineering workflows, where agents can search repositories, edit code, and verify outputs through tool use. These systems rely on structured, verifiable environments and well-defined execution primitives, which enable reliable multi-step reasoning and self-correction. As a result, such harnesses are considered a recipe for building capable agents across new data and task domains.

Tasks across architecture, engineering, and construction require multimodal understanding, presenting unique challenges to building reliable agents. For example, a single construction drawing sheet contains tightly packed annotations, callouts, line work, and cross-references that require visual reasoning. Agents in construction require access to information that is distributed across highly multimodal documents, resulting in the failure of tools like text search.

Standard tools in popular agent harnesses, such as text extraction, flatten spatial structure, while vision-based tools lack the quality needed for reliable geometric reasoning. As a result, agents applied to construction tasks often retrieve incomplete or incorrect context, leading to compounding errors. To study these limitations, we built AEC-Bench, a multimodal benchmark to evaluate agentic systems in real-world architecture, engineering, and construction workflows. The benchmark consists of a scaffolded collection of tasks drawn from coordination practices, including intra-sheet review, cross-sheet navigation, and project-level document alignment. We evaluate state-of-the-art coding-agent harnesses on this benchmark to characterize where they succeed, where they fail, and how domain-specific tooling affects performance.

### 1.1 Contributions

- Introduce AEC-Bench: a multimodal benchmark for agentic systems in engineering and construction, with taxonomy spanning intra-sheet, intra-drawing, and intra-project reasoning
- Utilize domain-experts to curate a benchmark with **196 instances across 9 task families**, grounded in construction coordination workflows with automated evaluation
- Show that general-purpose coding-agents partially generalize to AEC tasks but fail on visual grounding, exhaustive traversal, and cross-document coordination
- Demonstrate that domain-specific tools like parsing improve performance on retrieval-sensitive tasks, but further work is required for grounding and judgment-heavy tasks

### 1.2 Related Work

AEC-Bench has been developed to help identify and characterize the boundary points of agent performance in high-value construction coordination tasks. These coordination tasks require agents to demonstrate multimodal document understanding and context engineering capabilities over long horizons.

Recent benchmarks for agentic systems demonstrate that tool use, scaffolding, and verifier design strongly influence measured capabilities:
- **SWE-bench** (Jimenez et al., 2024): evaluates agents in software engineering environments (repository navigation, file editing, automated test verification)
- **GAIA** (Mialon et al., 2023) and **BFCL** (Patil et al., 2025): multi-step action planning and external tool/function call invocation
- **AgentBench** (Liu et al., 2024) and **WebArena** (Zhou et al., 2023): interaction with complex textual artifacts and external resources in multi-step reasoning

Document understanding benchmarks:
- **DocVQA** and **InfographicVQA** (Mathew et al., 2021): visual question answering over documents with tables, forms, and graphical elements
- **DUDE** (Landeghem et al., 2023): long documents and multi-page contexts
- **MMLongBench-Doc** (Ma et al., 2024), **LongDocURL** (Deng et al., 2025), **MLongDoc** (Chia et al., 2025), **M3DocVQA** (Cho et al., 2025): long-context and multi-document reasoning

AEC-specific benchmarks:
- **(Liang et al., 2026)**: hierarchical benchmark for LLM knowledge evaluation in AEC — measures AEC knowledge and cognitive proficiency (distinct from workflow-level agent performance)
- **AECV-Bench** (Kondratenko et al., 2026): multimodal understanding of architectural/engineering drawings (OCR, counting, spatial reasoning, drawing-grounded QA over floor plans); shows models still lack robust drawing literacy for symbol-centric understanding

**Key distinction from prior work**: AEC-Bench evaluates agents in realistic workflows where success depends not only on perception or domain knowledge but also on retrieval, cross-sheet navigation, cross-document reasoning, and structured reporting under an execution harness — closer to workflow evaluation than static knowledge testing or document visual QA.

### 1.3 Construction Coordination

Physical assets such as bridges, water treatment facilities, and office buildings are designed, engineered, and constructed by skilled professionals. While designers and engineers perform preliminary work in 3D modeling software (Revit, AutoCAD), most stages of design development, coordination, and delivery are coordinated through **2D construction drawing sets** and related documents.

A drawing set is a multi-page, multimodal instruction package in which meaning is conveyed through structured visual and textual elements: plans, details, callouts, notes, and title blocks.

**Coordination failures** between architects, engineers, and construction teams are often the main drivers of scheduling delays and budget overruns. During pre-construction, design, engineering, and handoff, many delays arise from inconsistencies introduced while authoring and revising drawing sets and project documents. Industry teams rely on standardized review and coordination workflows demanding deep professional experience and multimodal reasoning.

### 1.4 Task Taxonomy

Tasks organized by scope of context required:

**Intra-Sheet**: Tasks completable using a single sheet (one PDF page). Include checking whether callouts match referenced elements, verifying detail titles, or reviewing local assemblies. Focus on understanding what is present on the page and correctly interpreting relationships between text and multimodal drawing elements.

**Intra-Drawing**: Tasks requiring reasoning across multiple sheets within the same drawing set. Examples: validating cross-references, comparing sheet indices, tracing details across views (2D cross-sections of 3D building models). Require navigating between pages and tracking related information.

**Intra-Project**: Tasks involving multiple documents (drawings, specifications, submittals). Include identifying conflicts between specifications and drawings, or evaluating compliance across sources. Reflect real project-level coordination where relevant information is distributed across different documents.

### 1.5 Task Formulation

Each AEC-Bench task instance consists of:
- **Natural-language instruction**
- **Sandboxed execution environment** (real construction documents from public-sector projects + pre-installed PDF utilities)
- **Automated verifier**

Tasks are defined using the **Harbor task format** and executed within the **Harbor harness** (Harbor Framework Team, 2026), which provides a consistent interface for agent interaction and supports tool-based execution through terminal-style commands. Agents must explore the document set, retrieve relevant information, and produce structured findings in a standardized JSONL output file.

**Scoring**: Full credit for complete and correct findings; partial credit for partially correct outputs; zero credit for incorrect or unsupported results.

### 1.6 AEC-Bench Multimodal Subset

**Construction method**: Semi-automated pipeline combining expert-authored task templates with structured extraction from real-world drawing packages sourced from publicly available PDF documents, spanning multiple disciplines (architectural, structural, civil, mechanical, electrical, plumbing).

The PDF toolchain breaks multi-page documents into structured, machine-readable data: text with layout information, geometric regions, and cross-sheet references. Domain experts then select target pages/regions and inject **realistic, precisely localized artifacts**:
- Mismatched callout labels
- Broken cross-reference targets
- Swapped specification values

Using **alignment-aware text editing** that preserves visual fidelity. Each injected artifact is verified with text-level assertions and pixel-level differencing (before, after, and diff).

**Final subset**: **196 task instances** across **9 task types** and **3 scopes**.

---

## Dataset Summary (Table 1)

| Category | Task | Description | Instances |
|----------|------|-------------|-----------|
| **Intra-Sheet** | detail-technical-review | Answer localized technical questions about details | 14 |
| | detail-title-accuracy | Verify whether detail titles match the drawn content | 15 |
| | note-callout-accuracy | Verify whether callout text correctly describes the referenced element | 14 |
| **Intra-Drawing** | cross-reference-resolution | Identify cross-references that do not resolve to valid targets | 51 |
| | cross-reference-tracing | Find all source locations referencing a given target detail | 24 |
| | sheet-index-consistency | Compare sheet index entries against title blocks for mismatches | 14 |
| **Intra-Project** | drawing-navigation | Locate the correct file, sheet, and detail given a query | 12 |
| | spec-drawing-sync | Identify conflicts between specifications and drawings | 16 |
| | submittal-review | Evaluate submittals for compliance with specs and drawings | 36 |
| **Total** | | | **196** |

---

## 2 Baseline Agent Evaluation Set-up

We evaluate agent performance using baseline harness configurations designed to isolate the impact of tool access, document representation, and domain-specific augmentation. Rather than comparing foundation models in isolation, our goal is to understand how harness design shapes performance on AEC tasks.

**Two harness families**: Codex and Claude Code

**Two configurations**:

- **H (base)**: sandboxed environment with terminal (Bash) access + standard utilities for navigating document space (CLI-based PDF tools: pdftotext, pdftoppm). Agents may also write and execute their own code to process documents, create intermediate cache files, and perform operations such as searching across multiple files.

- **H+ (enhanced)**: base + domain-specific **Nomic tools** (Nomic Parse, Nomic Embeddings). Provides structured representations of drawings including extracted text, layout elements, and reference relationships.

**Models tested**:
- Codex: GPT-5.4, GPT-5.2
- Claude Code: Opus 4.6, Sonnet 4.6
- Nomic Agent (baseline)

---

## 3 Results (Table 2: Mean Reward by Task, Model, and Setup)

| Category | Task | GPT-5.4 H | GPT-5.4 H+ | GPT-5.2 H | GPT-5.2 H+ | Opus 4.6 H | Opus 4.6 H+ | Sonnet 4.6 H | Sonnet 4.6 H+ |
|----------|------|:---------:|:----------:|:---------:|:----------:|:---------:|:-----------:|:-----------:|:-------------:|
| **Intra-Sheet** | detail-technical-review | 35.7 | 71.4 | 60.7 | 85.7 | 35.7 | 78.6 | 53.6 | 78.6 |
| | detail-title-accuracy | 60.0 | 60.0 | 60.0 | 40.0 | 46.7 | 73.3 | 86.7 | 73.3 |
| | note-callout-accuracy | 28.6 | 28.6 | 28.6 | 14.3 | 0.0 | 35.7 | 42.9 | 35.7 |
| **Intra-Drawing** | cross-reference-resolution | 84.3 | 77.5 | 61.0 | 67.6 | 79.0 | 72.5 | 73.9 | 68.6 |
| | sheet-index-consistency | 97.6 | 81.9 | 82.1 | 85.0 | 71.4 | 85.5 | 72.6 | 76.0 |
| | cross-reference-tracing | 89.2 | 77.1 | 79.5 | 73.8 | 56.4 | 62.0 | 59.2 | 69.3 |
| **Intra-Project** | spec-drawing-sync | 55.0 | 71.8 | 44.0 | 50.0 | 29.0 | 51.3 | 26.0 | 64.1 |
| | drawing-navigation | 66.7 | 100.0 | 83.3 | 83.3 | 75.0 | 100.0 | 75.0 | 91.7 |
| | submittal-review | 15.0 | 19.0 | 11.8 | 19.0 | 17.1 | 16.7 | 6.5 | 23.1 |

**Key numbers by task (H → H+ average gain across all models)**:
- detail-technical-review: **+32.2%** (retrieval-sensitive, largest gain)
- spec-drawing-sync: **+20.8%**
- drawing-navigation: **+18.75%**
- note-callout-accuracy: **-3.6%** (degradation — visual-spatial grounding task)
- cross-reference-resolution: **-2.4%** (degradation — exhaustive traversal task)
- submittal-review: best score only **23.1** (lowest across all configurations)

---

## 4 Discussion

### 4.1 Retrieval as Primary Bottleneck

A central finding: multimodal AEC tasks tightly couple retrieval and reasoning, with **retrieval frequently acting as the primary bottleneck**. Agents often fail before reaching the core reasoning step because they cannot reliably locate the relevant sheet, detail, or document; once the correct context is retrieved, performance improves substantially.

Evidence from Table 2 H+ vs H:
- detail-technical-review: +32.2 points avg across models
- spec-drawing-sync: +20.8 points avg
- drawing-navigation: +18.75 points avg

These tasks are characterized by a primary dependence on locating the correct sheet, detail, or document before reasoning can proceed.

### 4.2 Targeted Benefits — Not Uniform Gains

Document parsing provides targeted benefits rather than uniform gains. On tasks relying more heavily on visual-spatial grounding:
- note-callout-accuracy: **-3.6%** avg (degradation)
- cross-reference-resolution: **-2.4%** (degradation)
- sheet-index-consistency: **-0.1%** (degradation)
- cross-reference-tracing: **-0.53%** (degradation)

**Reason**: These tasks require precise localization, alignment between text and geometry. The model must trace leader lines and related geometry purely visually to correctly identify and report issues. Even when relevant evidence might exist from parsing, agents frequently fail to localize it accurately. Adding parsed PDF representations does not directly address the underlying gap and can instead introduce additional context that the agent must navigate.

### 4.3 Tool Call Execution Patterns

Despite operating on multimodal construction documents, models consistently default to a coding-oriented tool repertoire:

| Metric | Codex (GPT-5.x) | Claude (Opus/Sonnet) |
|--------|:---------------:|:--------------------:|
| Bash usage | **100%** | 53% |
| Read operations | — | 35% |
| pdftotext calls | 77% across all models | |
| pdftoppm (image rendering) | **96%** | 32% |

**Key finding**: 77% of trajectories invoke pdftotext — strong convergence toward a pdftotext extraction pipeline. While this enables efficient keyword-based search, it collapses spatial layout and geometric relationships into linear text, discarding critical visual structure.

Codex agents rely heavily on rasterization via pdftoppm (96%), whereas Claude agents use it far less (32%). Yet this increased use of image rendering does not lead to better performance on visually grounded tasks — access to images alone is insufficient without the ability to interpret spatial relationships.

### 4.4 Failure Mode Analysis

**note-callout-accuracy breakdown** (14 instances × 4 models = 56 total runs, separated into):

| Subcategory | Instances | Avg Reward |
|-------------|:---------:|:----------:|
| Text-catchable | 2 | ~100% |
| Visual-required | 10 | ~5% |

"This large gap highlights a consistent failure mode: tasks that depend on tracing and geometric interpretation remain challenging for current systems, even under identical task structures and tool availability."

Failures are not due to lack of access to visual information — trajectories show extensive image rendering and inspection — but rather an inability to **translate visual input into structured, spatially grounded judgments**.

### 4.5 Submittal-Review Failure Mode

submittal-review shows a distinct failure mode — consistently low performance across all models and setups (best reward: 23.1):
- Parse improves access to relevant text, but does not resolve the need for **higher-level judgment**
- Agents tend to **over-generate findings**, leading to high false positive rates
- Requires domain-specific judgment and prioritization consistent with **professional review standards**
- Evaluation is inherently more sensitive to human interpretation, increasing likelihood of disagreement with verifier

### 4.6 Limitations

- Limited number of documents and subset of tasks per category/discipline — may constrain statistical robustness and coverage
- Tasks do not fully capture the breadth of abilities exhibited by modern LLM harnesses
- Some task families rely on curated artifacts or controlled defects that may not reflect full diversity of real-world drawing sets
- Most tasks rely on deterministic evaluation (keyword matching) — may not fully capture nuanced human judgments of engineering correctness
- Scope may not fully reflect the diversity of real-world AEC drawing sets

### 4.7 Replicability and License

Benchmark, agent harnesses, and evaluation code available at https://github.com/Nomic-ai/aec-bench under Apache 2 license.

---

## 5 Conclusion

AEC-Bench introduces a benchmark for evaluating multimodal, agentic reasoning in construction-document coordination workflows grounded in real-world design and engineering practices. By framing tasks around common review activities (reference tracing, navigation, coordination across drawings and specifications), it reflects the structure and demands of practical AEC coordination workflows, with outputs graded by domain-experts.

**Core conclusions**:

1. **Multimodal data representation and context engineering** are central to AEC agent performance
2. **Coding-agent systems transfer meaningfully** to this domain, particularly for retrieval and structured reasoning tasks
3. Performance becomes **less consistent** in settings requiring spatial grounding or domain-sensitive judgment
4. **Neither visual inputs nor structured document parsing is sufficient in isolation** — effective performance emerges from how modalities are coordinated and surfaced within the agent loop
5. Points to the importance of **domain-aware system design** where multiple capabilities are orchestrated to match task demands

### Future Directions

- **Scale and diversity expansion**: larger drawing sets, more disciplines, additional task families
- **Improved evaluation methodology**: verifiers capable of assessing evidence grounding and reasoning steps (beyond keyword matching)
- **Domain-specific agent architectures**: systems designed for document navigation — iteratively exploring drawing sets, maintaining spatial memory on sheets, retrieving evidence regions prior to reasoning
- **Stronger domain knowledge integration**: incorporating domain expertise into multimodal models for tasks requiring engineering judgment

---

## Figures

**Figure 1**: Mean reward by AEC-Bench category — bar chart showing performance across Intra-Sheet, Intra-Drawing, Intra-Project for each model/setup combination.

**Figure 2**: Example of a complex construction drawing PDF page — a visually dense drawing sheet with tightly packed annotations, callouts, and linework typical of real construction coordination artifacts.

**Figure 3**: Representative before/after task snapshots used in data preparation:
- **Top row (cross-reference resolution)**: before/after showing subtle reference-number inconsistencies requiring cross-sheet verification
- **Bottom row (note-callout accuracy)**: before/after showing callout text change while preserving surrounding geometry and leader structure — tests precise text-to-geometry grounding

---

## References

Yew Ken Chia, Liying Cheng, Hou Pong Chan, et al. 2025. M-LongDoc: A benchmark for multimodal super-long document understanding and a retrieval-aware tuning framework. In *EMNLP 2025*, pages 9233–9250.

Jaemin Cho, Debanjan Mahata, Ozan Irsoy, Yujie He, and Mohit Bansal. 2025. M3DocVQA: Multi-modal multi-page multi-document understanding. In *ICCV 2025*, pages 6178–6188.

Chao Deng, Jiale Yuan, Pi Bu, et al. 2025. LongDocURL: A comprehensive multimodal long document benchmark integrating understanding, reasoning, and locating.

Theodoros Galanos. 2026. Benchmarking agents on real engineering work is already teaching us something important. The Harness Blog.

Harbor Framework Team. 2026. Harbor: A framework for evaluating and optimizing agents and models in container environments.

Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R. Narasimhan. 2024. SWE-bench: Can language models resolve real-world GitHub issues? In *ICLR 2024*.

Aleksei Kondratenko, Mussie Birhane, Houssame E. Hsain, and Guido Maciocci. 2026. AECV-Bench: Benchmarking multimodal models on architectural and engineering drawings understanding.

Jordy Van Landeghem, Ruben Tito, Łukasz Borchmann, et al. 2023. Document understanding dataset and evaluation (DUDE).

Chen Liang, Zhaoqi Huang, Haofen Wang, et al. 2026. AECBench: A hierarchical benchmark for knowledge evaluation of large language models in the AEC field. *Advanced Engineering Informatics*, 71:104314.

Xiao Liu, Hao Yu, Hanchen Zhang, et al. 2024. AgentBench: Evaluating LLMs as agents. In *ICLR 2024*.

Antonio Loison, Quentin Macé, Antoine Edy, et al. 2026. ViDoRe v3: A comprehensive evaluation of retrieval augmented generation in complex real-world scenarios.

Yubo Ma, Yuhang Zang, Liangyu Chen, et al. 2024. MMLongBench-Doc: Benchmarking long-context document understanding with visualizations.

Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq Joty, and Enamul Hoque. 2022. ChartQA: A benchmark for question answering about charts with visual and logical reasoning. In *ACL 2022 Findings*, pages 2263–2279.

Minesh Mathew, Dimosthenis Karatzas, and C. V. Jawahar. 2021. DocVQA: A dataset for VQA on document images.

Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Yann Scialom. 2023. GAIA: A benchmark for general AI assistants.

Zach Nussbaum, John X. Morris, Brandon Duderstadt, and Andriy Mulyar. 2025. Nomic Embed: Training a reproducible long context text embedder.

Shishir G. Patil, Huanzhi Mao, Fanjia Yan, et al. 2025. The Berkeley Function Calling Leaderboard (BFCL): From tool use to agentic evaluation of large language models. In *ICML 2025*.

Xiang Yue, Yuansheng Ni, Kai Zhang, et al. 2024. MMMU: A massive multi-discipline multimodal understanding and reasoning benchmark for expert AGI.

Shuyan Zhou, Frank F. Xu, Hao Zhu, et al. 2023. WebArena: A realistic web environment for building autonomous agents. *arXiv:2307.13854*.

Yifan Zhou et al. 2024. DocPrompting: Generating chain-of-thought prompts for document understanding.

---

**Keywords**: AEC, multimodal benchmark, agent evaluation, construction coordination, document understanding, retrieval-augmented agents, Harbor framework, visual grounding, cross-reference resolution
