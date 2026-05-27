---
title: "TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments"
authors: Furkan Sakizli
published: 2026-05-04
source: "https://arxiv.org/abs/2605.04107"
---

# TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments

**Authors**: Furkan Sakizli
**Published**: May 4, 2026
**Source**: https://arxiv.org/abs/2605.04107
**arXiv ID**: 2605.04107
**Categories**: cs.SE, cs.LG
**Code**: TypeScript package, 1,200 lines, zero dependencies, sub-millisecond execution

---

## Abstract

TSCG is a deterministic compiler that transforms JSON tool schemas into token-efficient structured text for language model agents. The work addresses a fundamental protocol mismatch: production APIs (OpenAI Function Calling, Anthropic Tool Use, MCP) transmit tools as JSON—optimized for machine parsing, not LLM interpretation.

**Key results**: Phi-4 14B recovers from 0% to 84.4% accuracy at 20 tools, 90.3% at 50 tools. Token savings of 52–57% on production schemas. Evaluated across 12 models and 19,000+ API calls.

---

## Problem: The Protocol Mismatch

### Tool Schema Token Crisis

When agents have many tools (common after MCP server expansion), JSON tool schema token costs explode:

| Tools | Schema token share of context |
|-------|-------------------------------|
| 10 tools | 8–15% |
| 20 tools | 15–25% |
| 50 tools | 40%+ |

Effective context available for actual reasoning shrinks dramatically.

### Protocol Mismatch Bug

Many open-source models (e.g., Phi-4) were not trained on production-grade JSON tool schemas:

- Encounter long JSON schemas → accuracy drops to 0% (Phi-4 baseline at 20 tools)
- This is not a model capability problem—it is a **protocol representation problem**

---

## TSCG Solution: Eight Composable Operators

### Operator Categories

**Token-reduction operators:**
- **SDM** (Schema Description Minimization): Removes verbose field descriptions
- **TAS** (Tokenizer-Aligned Surface): Selects surface forms that BPE tokenizes efficiently
- **DRO** (Default Removal Optimization): Strips unnecessary default value declarations
- **CFL** (Context-Free List): Exploits attention sink properties at position 0

**Structure-reordering operators:**
- **CAS** (Causally-Aligned Sequence): Reorders fields so prerequisites appear before dependents
- **CFO** (Causal Field Ordering): Ensures causally-required information is accessible before dependent fields

**Token-expanding operators:**
- **SAD-F** (Schema Annotation with Defaults-Formatted): Adds human-readable annotations for models that benefit from expanded context
- **CCP** (Compact Commentary Prefix): Adds concise schema-level documentation

### Compilation Example

**Before (JSON Schema):**
```json
{
  "name": "search_web",
  "description": "Search the internet for information on a given topic",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query to execute"
      },
      "max_results": {
        "type": "integer",
        "description": "Maximum number of results to return",
        "default": 10
      }
    },
    "required": ["query"]
  }
}
```

**After (Token-Efficient Structured Text):**
```
TOOL search_web: Search the internet
  PARAM query:str[required] — Search query
  PARAM max_results:int[default=10] — Number of results
```

---

## Empirical Results

### Accuracy Recovery

| Model | Tools | Baseline | TSCG | Token Savings |
|-------|-------|----------|------|---------------|
| Phi-4 14B | 20 | 0% | **84.4%** | 52% |
| Phi-4 14B | 50 | 0% | **90.3%** | 57% |
| GPT-4o | 20 | 91% | 93.5% | 52% |
| Claude Sonnet | 20 | 93% | 94.1% | 52% |
| GPT-5.2 | 20 | ~94% | ~96% | 52% |

### External Validation

Berkeley Function Calling Leaderboard:
- Accuracy: **93.2%**
- Token savings: **46.8%**

---

## Theoretical Grounding

The framework connects operators to three transformer properties:

| Transformer Property | Connected Operator | Mechanism |
|---------------------|-------------------|-----------|
| **Causal attention** | CFO | Ensures prerequisites are causally accessible |
| **Attention sinks** | CFL | Exploits position-0 amplification |
| **BPE non-monotonicity** | TAS | Selects tokenizer-aligned surface forms |

### R² Analysis: Format vs Compression

Format translation (JSON → text) explains **88% of improvement for small models**; genuine compression persists only for frontier models.

This decomposition reveals two distinct improvement mechanisms:
- **Small models**: primarily benefit from format translation (removing JSON structure confusion)
- **Frontier models**: benefit from genuine token compression (structural optimization)

---

## Four-Class Behavioral Taxonomy

| Class | Models | Characteristic | Recommendation |
|-------|--------|---------------|----------------|
| **Format-dominated** | Phi-4, Mistral 7B, Gemma 4B | Gains vanish vs text baselines | Balanced TSCG profile |
| **Compression** | Claude, GPT-4o, GPT-5.2 | Genuine structural improvement persists | Per-operator tuning |
| **Neutral** | Llama 8B, Gemma 12B, Mistral-Small 24B | Modest mixed effects | Conservative profile |
| **Conservative-only** | Qwen models | Balanced TSCG degrades; SDM improves | SDM-only deployment |

---

## Deployment Guide

| Deployment Context | Recommended Profile |
|-------------------|-------------------|
| Frontier models (Claude, GPT-5) | Balanced TSCG with per-operator tuning |
| Local models <10B | Conservative (SDM-only) |
| Qwen architectures | Conservative-only (SDM improves, balanced degrades) |
| Production MCP schemas (heavy) | +5.0 pp vs synthetic catalogs |
| Light synthetic catalogs | Saturates quickly; diminishing returns |

---

## Experimental Scale

- **19,000+ API calls**
- **12 models** (4B–32B parameters plus frontier models)
- **Five benchmark scenarios** (TAB: TSCG-Agentic-Bench)
- Token savings: **50–72%** while improving accuracy

---

## Broader Vision: Community Schema Registry

The paper proposes establishing pre-compiled tool schemas for APIs, MCP servers, and cloud services as standard infrastructure—a "community schema registry" where providers publish optimized TSCG representations alongside raw JSON schemas.

This establishes compression as standard infrastructure rather than per-deployment optimization.

---

## Limitations

- Self-constructed benchmark (mitigated by BFCL validation)
- English-only filler patterns
- 12-model coverage (generalization to untested architectures uncertain)
- Moderate compression (50–72%) versus schema-replacement approaches (98–99%)
- Predictive model RMSE of 12.8 percentage points

---

## Workspace Alignment Analysis

| TSCG Insight | cc-workspace Application | Priority |
|--------------|--------------------------|---------|
| Schema token cost tracking | Not currently tracking MCP tool schema size | Medium (few MCP tools now) |
| Protocol mismatch | Claude series already optimized; low risk | Low |
| 52% token savings | Worth evaluating if MCP tools exceed 10+ | Medium-term |
| Conservative-only for Qwen | N/A (using Claude) | N/A |

**Complementarity with ToolSearch**: Claude Code's ToolSearch (deferred tool loading) avoids loading all tools simultaneously. TSCG makes each loaded tool's schema more token-efficient. The two mechanisms are orthogonal and complementary.

**Future hook integration**: TSCG's TypeScript package could integrate into a PreToolUse hook to compress schemas before model calls when tool count exceeds threshold.

---

## Key Citation

> "Tool schema is the protocol layer of agent harness. A poorly designed protocol mismatch between harness expectations and model training formats produces catastrophic accuracy collapse — not from model incapacity, but from representational mismatch." (arXiv:2605.04107)
