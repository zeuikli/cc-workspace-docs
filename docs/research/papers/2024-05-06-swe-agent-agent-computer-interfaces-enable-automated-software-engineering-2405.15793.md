---
title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
arxiv_id: 2405.15793
authors: John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press
fetched: 2026-05-26
published: 2024-05-06
source: "https://arxiv.org/abs/2405.15793"
source_tier: P
---

# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors**: John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press
**Published**: May 2024 (v1: 2024-05-06; v3: 2024-11-11)
**Source**: https://arxiv.org/abs/2405.15793
**arXiv ID**: 2405.15793
**Categories**: cs.SE, cs.AI, cs.CL, cs.HC, cs.LG

---

## Abstract

Software engineering is a challenging task requiring proficiency in both code generation and interacting with computers. In this paper, we introduce SWE-agent, an autonomous system that uses a language model to interact with a computer to solve software engineering tasks. We show that a custom-built agent-computer interface (ACI) greatly enhances the ability of an agent to create and edit code files, navigate entire repositories and execute programs. On SWE-bench, SWE-agent is able to solve 12.5% of issues, compared to the previous best of 3.8% achieved with retrieval-augmented generation (RAG). We explore how ACI design impacts an agent's behavior and performance, and provide insights on effective design.

---

## Core Thesis

Language model agents represent a new category of end users with distinct needs and abilities, requiring specially-built interfaces. Just as humans benefit from IDEs over raw terminals, LM agents benefit from a custom Agent-Computer Interface (ACI) that abstracts operations into LM-friendly commands with informative feedback. Interface design for agents can match or exceed the importance of model improvements, achieving 10.7 percentage point gain over baseline through ACI design alone.

---

## Introduction

LM agents are increasingly used to automate complicated tasks in digital environments. The central insight is that while humans use interfaces designed for human cognition (IDEs, GUIs), LM agents have fundamentally different strengths and weaknesses—they are powerful code generators but struggle with verbose output, multi-step navigation, and cascading errors from ambiguous feedback. SWE-agent addresses this by introducing the Agent-Computer Interface (ACI) as a first-class design concern.

---

## Agent-Computer Interface (ACI) Design

### Definition

An ACI is an abstraction layer between LM agents and computers, specifically designed for LM capabilities and limitations rather than human users. It consists of:
- LM-friendly commands (search, view, edit)
- LM-friendly environment feedback (informative but concise)
- History management to prevent context window overflow

### Four Design Principles

1. **Actions should be simple and easy to understand** — Few options with concise documentation; reduces need for demonstrations or fine-tuning.
2. **Actions should be compact and efficient** — Consolidate important operations into few actions; enable meaningful progress in single steps (e.g., `edit` command vs. multiple `sed` calls).
3. **Environment feedback should be informative but concise** — Substantive information without unnecessary details; avoid context window bloat.
4. **Guardrails mitigate error propagation** — Automatic error detection (e.g., syntax checking) helps agents recognize and correct errors quickly; enables faster recovery from mistakes.

---

## System Architecture

### Overview

```
LM Agent
    ↓
Agent-Computer Interface (ACI)
├── LM-friendly commands
│   ├── Navigate repo
│   ├── Search files
│   ├── View files
│   └── Edit lines
├── LM-friendly environment feedback
└── History management
    ↓
Computer
├── Terminal
├── Filesystem
└── Test execution
```

### Three Core Modules

1. **Environment** — Docker-based execution, inherits from InterCode framework
2. **Agent** — LM wrapper, ACI rendering, command logic
3. **Logging** — Trajectory and patch artifact generation

### ACI Command Set

#### Search and Navigation

| Command | Description |
|---------|-------------|
| `find_file <filename>` | Search for filenames in repository |
| `search_file <term> [file]` | Locate strings within files |
| `search_dir <term> [dir]` | Search strings in directory |

Results are capped at 50 matches to prevent context overflow; summarized output format suppresses verbose results.

#### File Viewer

| Command | Description |
|---------|-------------|
| `open <path> [line_number]` | Open file at specified path |
| `goto <line_number>` | Jump to specific line |
| `scroll_up` / `scroll_down` | Navigate by 100 lines |

The viewer displays a 100-line window (configurable) with line numbers, total line count, and indicators for omitted lines above/below.

#### File Editor

```bash
edit <start_line>:<end_line>
<replacement_text>
end_of_edit
```

Features:
- Multi-line edits in a single action
- Automatic syntax checking (flake8 linting)
- Integrated with file viewer (auto-displays updated content)
- Rejects edits with syntax errors, showing before/after diff

Linting checks (flake8):
- `F821/F822` — Undefined names/symbols
- `E111/E112/E113` — Indentation errors
- `E999` — Syntax errors
- `E902` — File read errors

#### Context Management

- Observations before the last 5 are collapsed to single lines
- Maintains essential information while reducing context
- Prevents outdated file information accumulation
- State variables tracked: `CURRENT_FILE`, `CURRENT_LINE`, `WINDOW_SIZE`, `SEARCH_RESULTS`, etc.

### Configuration System (YAML)

```yaml
system_template: |
  First `system` message shown to agent
instance_template: |-
  Instance prompt with task-specific content
next_step_template: |-
  Per-turn observation format
demonstrations:
  - trajectories/<username>/<experiment>/*.traj
env_variables:
  CURRENT_FILE: 0
  CURRENT_LINE:
  WINDOW_SIZE:
command_files:
  - path/to/bash_file.sh
```

---

## Experimental Setup

### Datasets

1. **SWE-bench Full**: 2,294 task instances from 12 Python repositories
2. **SWE-bench Lite**: Canonical subset of 300 self-contained functional bug fixes
3. **HumanEvalFix**: Short-form code debugging benchmark (Python, JavaScript, Java)

### Models Evaluated

- **GPT-4 Turbo** (gpt-4-1106-preview) — 128k context window; primary evaluation model
- **Claude 3 Opus** (claude-3-opus-20240229) — 200k context window; portability verification
- Llama 3 and DeepSeek Coder showed subpar performance due to small context windows (8k)

### Baselines

1. **Non-interactive RAG** — BM25 retrieval + direct patch generation
2. **Shell-only Agent** — Interactive setting with standard Linux shell, no ACI customization

### Hyperparameter Search (37 dev-split samples)

- Temperature: 0.0, 0.2
- Window size: 100, 200 lines
- History: Full history vs. Last 5 observations

**Optimal config (GPT-4 Turbo)**: Temperature=0.0, Window=100 lines, History=Last 5 Obs → 15.1% on dev set

---

## Main Results

### SWE-bench Performance

| Model | SWE-bench Full % | Full $ Avg Cost | Lite % | Lite $ Avg Cost |
|-------|-----------------|-----------------|--------|-----------------|
| RAG w/ GPT-4 Turbo | 1.31% | $0.13 | 2.67% | $0.13 |
| RAG w/ Claude 3 Opus | 3.79% | $0.25 | 4.33% | $0.25 |
| Shell-only w/ GPT-4 Turbo | — | — | 11.00% | $1.46 |
| Shell-only w/o Demo | — | — | 7.33% | $0.79 |
| **SWE-agent w/ GPT-4 Turbo** | **12.47%** | $1.59 | **18.00%** | $1.67 |
| **SWE-agent w/ Claude 3 Opus** | **10.46%** | $2.59 | **13.00%** | $2.18 |

Key takeaways:
- **6.7× improvement** over RAG baseline on Lite (18.00% vs 2.67%)
- **64% relative improvement** over Shell-only (18.00% vs 11.00%)
- **10.7 percentage point improvement** from ACI design alone

### HumanEvalFix Performance

| Model | Python | JavaScript | Java |
|-------|--------|-----------|------|
| CodeLLaMA-instruct-13B | 29.2% | 19.5% | 32.3% |
| GPT-4 | 47.0% | 48.2% | 50.0% |
| DeepseekCoder-CodeAlpaca-6.7B | 49.4% | 51.8% | 45.1% |
| WaveCoder-DS-6.7B | 57.9% | 52.4% | 57.3% |
| **SWE-agent w/ GPT-4 Turbo** | **87.7%** | **89.7%** | **87.9%** |

---

## ACI Design Ablations

### File Editor Impact (SWE-bench Lite)

| Configuration | % Resolved | Change |
|---------------|-----------|--------|
| `edit` w/ linting | **18.0%** | baseline |
| `edit` w/o linting | 15.0% | −3.0 |
| No edit (bash only) | 10.3% | −7.7 |

Editing guardrails are critical for error recovery; linting prevents cascading failures.

### Search Interface Impact

| Configuration | % Resolved | Change |
|---------------|-----------|--------|
| Summarized (ACI) | **18.0%** | baseline |
| Iterative | 12.0% | −6.0 |
| No search | 15.7% | −2.3 |

Iterative search causes agents to exhaustively inspect all results, wasting context and budget.

### File Viewer Window Size

| Configuration | % Resolved | Change |
|---------------|-----------|--------|
| 100 lines | **18.0%** | baseline |
| 30 lines | 14.3% | −3.7 |
| Full file | 12.7% | −5.3 |

Both too little and too much content reduce performance; 100-line window is optimal.

### Context Management

| Configuration | % Resolved | Change |
|---------------|-----------|--------|
| Last 5 Obs. | **18.0%** | baseline |
| Full history | 15.0% | −3.0 |
| w/o demo | 16.3% | −1.7 |

Collapsing old observations improves performance by reducing context clutter.

---

## Behavior Analysis

### Typical Trajectory Phases

**Early Phase (Turns 1–4):**
- `create` — Writing reproduction scripts
- `find_file` — Locating relevant files
- `search_dir` — Directory-level searches
- Focus: Localization and reproduction

**Middle Phase (Turns 5–15):**
- `edit` — File modifications
- `python` — Test execution
- `search_file` — Fine-grained searches
- Focus: Edit-test loops

**Late Phase (Turns 16+):**
- `submit` — Solution submission
- Distribution peaks around turns 10–12 for resolved instances

### Key Behavioral Findings

1. **Reproduction-first strategy** — Most common initial action triple: `(create, edit, python)`. Models establish baseline behavior before fixing.
2. **Zoom-in pattern** — Directory-level → file-level → line-level; mirrors natural debugging.
3. **Edit-test loops dominate** after localization (`edit`, `python` correlation: 0.85+).
4. **Editing challenges persist** — 51.7% of trajectories have ≥1 failed edit; 90.5% recovery rate from first failure; rate drops with additional failures (57.2% after one failure).
5. **Fast success, slow failure** — Median resolved: $1.21 cost, 12 steps; mean unresolved: $2.52 cost, 21 steps. Increasing budget unlikely to improve performance.

### Failure Mode Distribution (SWE-bench Lite, n=248)

| Failure Mode | Percentage |
|---|---|
| Incorrect Implementation | 30.6% |
| Cascading Failed Edits | 23.4% |
| Overly Specific Implementation | 21.4% |
| Other | 24.6% |

~52% of failures are due to functional incorrectness (not process issues).

---

## Performance Breakdown

### By Repository (SWE-bench Lite)

| Repository | SWE-agent (GPT-4) | RAG (GPT-4) |
|---|---|---|
| django/django (114 instances) | 26.32% | 4.39% |
| psf/requests (6) | 33.33% | 0.00% |
| scikit-learn (23) | 17.39% | 0.00% |
| sympy/sympy (77) | 10.39% | 1.30% |
| matplotlib (23) | 13.04% | 0.00% |
| pytest-dev/pytest (17) | 17.65% | 0.00% |
| astropy/astropy (6) | 16.67% | 0.00% |

### By Year (SWE-bench Lite)

| Year | SWE-agent (GPT-4) | RAG (GPT-4) |
|---|---|---|
| 2023 (30 instances) | 23.33% | 3.33% |
| 2022 (57) | 21.05% | 5.26% |
| 2021 (42) | 23.81% | 2.38% |
| 2020 (66) | 10.61% | 3.03% |
| Before 2020 (105) | 17.14% | 0.95% |

No clear temporal bias; performance is stable across issue ages.

### Trajectory Completion Statistics

**GPT-4 Turbo on Full SWE-bench (286 resolved):**
- Mean turns: 14.71; Median turns: 12; 75th percentile: 18 turns

**Claude 3 Opus on Lite (35 resolved):**
- Mean turns: 12.71; Median turns: 13; 75th percentile: 15 turns

---

## Key Contributions

1. **ACI concept** — New framework for designing LM-agent interactions; differs fundamentally from human UIs; tailored to LM strengths and weaknesses.
2. **SWE-agent system** — Open-source implementation achieving SOTA on SWE-bench (12.47%); portable across different LMs (GPT-4 → Claude).
3. **Design methodology** — Principled approach inspired by HCI; qualitative analysis + grid search; reusable design patterns for ACI construction.
4. **Unified framework** — Isolates ACI as an independent variable; shows interface design substantially impacts performance.
5. **Comprehensive analysis** — Ablation studies quantifying each design choice; behavioral analysis revealing agent problem-solving patterns; insights into failure modes and recovery.

---

## Key References

- Jimenez et al. (2024) — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- Yang et al. (2023) — InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback
- Wei et al. (2022) — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- Yao et al. (2023) — ReAct: Synergizing Reasoning and Acting in Language Models
- Chen et al. (2021) — Evaluating Large Language Models Trained on Code (HumanEval)
- Muennighoff et al. (2023) — OctoPack: Instruction Tuning Code Large Language Models (HumanEvalFix)
- Shinn et al. (2023) — Reflexion: Language Agents with Verbal Reinforcement Learning
- Nakano et al. (2021) — WebGPT: Browser-assisted question-answering with human feedback
- Park et al. (2023) — Generative Agents: Interactive Simulacra of Human Behavior
