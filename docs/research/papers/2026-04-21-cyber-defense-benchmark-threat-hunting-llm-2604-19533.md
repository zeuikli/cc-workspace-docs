---
title: "Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps"
authors: "Alankrit Chona, Igor Kozlov, Ambuj Kumar"
published: "2026-04-21"
source: "https://arxiv.org/abs/2604.19533"
---

# Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps

**Authors**: Alankrit Chona, Igor Kozlov, Ambuj Kumar
**Published**: April 21, 2026 (v1); revised April 23, 2026 (v3)
**Source**: https://arxiv.org/abs/2604.19533
**arXiv ID**: 2604.19533
**Categories**: cs.CR, cs.AI

---

## Abstract

A benchmark measuring LLM agent performance on **open-ended threat hunting tasks** using real Windows event logs. Agents must identify malicious event timestamps from large SQLite databases (75,000–135,000 log records) without guided prompts, evaluated CTF-style against Sigma-rule-derived ground truth. Five frontier models all fail badly: best performer (Claude Opus 4.6) submits correct flags for only 3.8% of malicious events. No model passes the 50% recall threshold on any combination of the 13 MITRE ATT&CK tactics.

---

## Benchmark Design

### Dataset

| Parameter | Value |
|-----------|-------|
| Attack procedures | 106 real procedures from OTRF Security-Datasets corpus |
| MITRE ATT&CK sub-techniques | 86 sub-techniques |
| ATT&CK tactics | 12 tactics |
| Campaigns evaluated | 26 |
| Log records per episode | 75,000–135,000 |

### Environment

- **Framework**: Gymnasium reinforcement-learning environment
- **Storage**: In-memory SQLite databases
- **Data**: Time-shifted and entity-obfuscated real attack recordings
- **Agent interface**: Iterative SQL queries

### Task

The agent receives an in-memory SQLite database of log records and must:
1. Iteratively submit SQL queries to discover malicious events
2. Explicitly flag malicious event timestamps
3. Pass ≥50% recall per ATT&CK tactic on **all 13 tactics** to pass

No guided prompts — fully open-ended discovery.

---

## Results

### Model Performance

| Model | Avg Correct Flag Rate |
|-------|----------------------|
| **Claude Opus 4.6** | **3.8%** (best performer) |
| GPT-5 | ~equivalent (poor) |
| Gemini 3.1 Pro | ~equivalent (poor) |
| Kimi K2.5 | ~equivalent (poor) |
| Gemini 3 Flash | ~equivalent (poor) |

### Passing Threshold

- **Threshold**: ≥50% recall per ATT&CK tactic on all 13 tactics
- **Result**: **No model passed**
- **Best run**: Leader cleared threshold on only **5 of 13 tactics**
- **All runs**: Zero runs across any model found all flags

---

## Key Finding

> "Current LLMs are poorly suited for open-ended, evidence-driven threat hunting despite strong performance on curated Q&A benchmarks."

**Capability gap**: Strong benchmark performance on structured cybersecurity Q&A ≠ ability to perform open-ended forensic investigation on raw log data.

---

## Why This Gap Exists

The task requires:
1. **Exploratory SQL query generation** without knowing what to look for
2. **Evidence accumulation** across thousands of log records
3. **Pattern recognition** across time-shifted, entity-obfuscated data
4. **Multi-step hypothesis testing** with no intermediate feedback signals

This differs fundamentally from:
- CTF challenges (structured, known-solution-format)
- Q&A benchmarks (retrieval from curated knowledge)
- Code generation benchmarks (well-defined I/O)

---

## Workspace Relevance

Critical calibration for `sre`, `security-reviewer`, and `opus-pilot` in security contexts:

1. **3.8% Claude Opus 4.6 flag rate**: Frontier models cannot autonomously perform threat hunting on raw logs — **do not design harnesses that delegate open-ended forensic investigation to the model alone**
2. **5/13 tactics cleared**: Even best runs cover less than half the tactic space — security coverage is structurally incomplete with current models
3. **Gap between Q&A and real-world forensics**: Benchmark scores (like those in Claude Opus 4.7 System Card) do not predict forensic investigation capability — separate evaluation required for SecOps use cases
4. **SQL query interface pattern**: The benchmark's iterative SQL query approach (agent generates queries, receives results, refines) is a valid harness pattern for structured log analysis — but human-in-the-loop remains required for actual SOC deployment
5. **MITRE ATT&CK sub-technique coverage**: If building threat hunting tools with Claude, the 86 sub-techniques in this benchmark are a useful coverage checklist for evaluation
