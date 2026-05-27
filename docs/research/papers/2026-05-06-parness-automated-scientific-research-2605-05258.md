---
title: "PARNESS: A Paper Harness for End-to-End Automated Scientific Research with Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation"
authors: Yuchen Wang, Zhongzhi Luan
published: 2026-05-06
source: "https://arxiv.org/abs/2605.05258"
---

# PARNESS: A Paper Harness for End-to-End Automated Scientific Research

**Authors**: Yuchen Wang (Sino-German Joint Software Institute, Beihang University), Zhongzhi Luan (Beihang University)
**Published**: May 6, 2026
**Source**: https://arxiv.org/abs/2605.05258
**arXiv ID**: 2605.05258
**Categories**: cs.SE
**Code**: https://github.com/gtrhythm/PARNESS (~62.2k LoC core + 13.4k LoC tests; 553 passing tests)

---

## Abstract

PARNESS is an open-source framework addressing five structural limitations in existing autonomous research systems. Current systems impose fixed control-flow shapes, bounded ideation, episodic reading, overlooked code-repository links, and non-retrievable cross-run knowledge. PARNESS provides "a thin runtime that binds heterogeneous research components into a single declarative pipeline" through four design moves: a customizable DAG kernel, full-text PDF parsing with graceful fallback, a knowledge graph indexing papers/ideas/experiments/code, and GUI/TUI extensibility.

---

## Five Structural Limitations Addressed (L1–L5)

| # | Limitation | Impact |
|---|-----------|--------|
| **L1** | Hard-coded workflows fail across disciplines | Wet-lab, surveys, simulations, theory each iterate differently |
| **L2** | LLM ideation constrained by context windows + "lost-in-the-middle" | Limits cross-domain creativity |
| **L3** | Papers parsed once, then forgotten | Abstract-only systems miss critical implementation details |
| **L4** | Paper-to-code links exist per-task only | No corpus-level indexing for knowledge transfer |
| **L5** | Each pipeline run starts from zero | Accumulated knowledge from prior runs remains inaccessible |

---

## Design Principles (P1–P6)

1. **Domain-agnostic scheduler** — sees only nodes and edges
2. **Composition as data** — YAML pipelines, not Python code
3. **Failure isolation** — subprocess slots release GPU memory after each node
4. **Knowledge persistence** — state survives across runs in SQLite + Neo4j
5. **LLM interchangeability** — six-provider factory behind unified interface
6. **Verification as typed output** — experiments emit results + verifier outputs

---

## Four Method Pillars (M1–M4)

### M1: DAG Kernel + DSL

A ~600-line `GraphRunner` with a four-field Agent contract enables discipline-agnostic scheduling. Pipelines are YAML with layered validation (schema, contract, type, topology).

**Four-Field Agent Contract:**
| Field | Type | Purpose |
|-------|------|---------|
| `_route` | string | Single successor node ID |
| `_routes` | array | One-to-many fan-out |
| `_score` | number | Iteration/ranking value |
| `_metadata` | object | Provenance + free-form data |

### M2: Full-Text PDF Parsing

PDF-Extract-Kit integration produces typed layout, formula, OCR, and table objects with provenance. Graceful degradation to abstract-only when full text unavailable; "abstract-comprehension" capability grows with cumulative corpus.

### M3: Knowledge Graph + Cognitive Roles

Neo4j stores papers, ideas, experiments, and code repositories as typed nodes with four edge types (structural, internal, semantic, walk).

**Six cognitive-role agents**: Reader, Analyst, Connector, Contrarian, Synthesizer, Critic — retrieve scenario-typed slices (similar / opposite / cross-domain / counter-intuitive).

**Knowledge Graph Indexing (Eight Phases):**
1. Extract (LLM)
2. Dedup (deterministic)
3. Embed (deterministic)
4. Write nodes (deterministic)
5. Internal edges (LLM)
6. Structural edges (deterministic)
7. Semantic edges (LLM)
8. Random walk (deterministic)

### M4: GUI/TUI Extension Surface

Single-file modules with `@register` decorator + single-document YAML pipelines + self-describing `INPUT_SPEC`/`OUTPUT_SPEC` enable external coding agents (Claude Code, Cursor, Copilot) to modify workflows without custom plugins.

---

## System Architecture (Four Layers)

| Layer | Components |
|-------|-----------|
| **L0 (DAG Kernel)** | GraphRunner, BaseModule contract, ModuleRegistry (~600 LoC) |
| **L1 (Persistence)** | Five SQLite stores (papers, knowledge, evaluations, writing, experiments) + Neo4j with vector index |
| **L2 (Agents)** | 25+ domain agents, 130+ adapters, six LLM providers, domain tools (PDF parser, KG, crawlers, experiment runner) |
| **L3 (Pipeline)** | ~50 YAML pipelines, entry-point scripts, four-pass pipeline validator |

---

## Module Taxonomy (130+ modules)

| Category | Count |
|----------|-------|
| Research/crawler/parser | 8 |
| Ideation | 26 |
| Experiment runner/verifier | 24 |
| Writing & review | 11 |
| Knowledge graph | 17 |
| Infrastructure | 16+ |
| Iteration controllers | 7 |
| Post-processing | 2 |

---

## Discipline-Specific Pipeline Examples

All four pipelines run on the same DAG kernel — demonstrating L1 compliance:

- **ML benchmark loop**: idea → gate → experiment loop
- **Wet-lab biology**: hypothesis → idea-discussion → peer-gate → protocol → biosafety → wet-lab → replicate → stat-gate
- **Social-science survey**: RQ → instrument → pilot → IRB → recruit → coding → analyse → revise
- **Theory+simulation**: parallel proof attempts and parameter sweeps with evidence merging

---

## Related Work Comparison

| System | Workflow shape | Full-text reading | Cross-run knowledge |
|--------|---------------|-------------------|---------------------|
| AI-Scientist v1/v2 | Linear or four-stage; template-dependent | No | No |
| PaperOrchestra | Fixed five-step recipe | Abstract-only | No |
| AutoSOTA | Post-publication optimization only | No | No |
| InternAgent | Eleven-state WorkflowState enum | No | No |
| **PARNESS** | **Data-defined DAG topology** | **Full PDF + graceful fallback** | **SQLite + Neo4j across runs** |

---

## LLM Providers

OpenAI, Anthropic, GLM (Zhipu), MiniMax, Local, MockLLM (4,444 rule-based canned responses for offline testing).

---

## Limitations

- "Empirically the parallel ensemble produces wider seed coverage than a single LLM at the same total token budget; we have not yet measured this rigorously"
- No shared benchmark comparison with AI-Scientist, InternAgent, or PaperOrchestra
- No production-scale evaluation, user studies, or domain generalization evidence
- Self-declared "v1 systems paper" without comparative quality metrics

---

## Workspace Alignment Analysis

| PARNESS Design Move | cc-workspace Relevance | Priority |
|--------------------|----------------------|---------|
| DAG kernel for agent orchestration | Parallels hierarchical sub-agent topology in `subagent-strategy.md` | Medium |
| YAML-defined pipelines as data | Aligns with declarative config preference over code | Low (already implicit) |
| Full-text PDF indexing across papers | Useful if `research/papers/` corpus grows to 50+ files | Medium-term |
| Cross-run knowledge via SQLite/Neo4j | Heavy infrastructure; overkill for current workspace scale | Low |
| MockLLM (4,444 canned responses) | Interesting pattern for offline harness testing | Medium (test infra) |
| Cognitive-role agents for retrieval | Contrarian + Synthesizer roles align with advisor() use cases | Conceptual alignment |

---

## Key Citation

> "PARNESS proposes a thin runtime that binds heterogeneous research components into a single declarative pipeline — a minimal DAG kernel plus four structured design moves addressing workflow rigidity, bounded ideation, episodic reading, unindexed code links, and zero cross-run memory." (arXiv:2605.05258)
