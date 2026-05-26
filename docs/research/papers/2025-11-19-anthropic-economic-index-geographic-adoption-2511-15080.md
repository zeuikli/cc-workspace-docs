---
title: "Anthropic Economic Index Report: Uneven Geographic and Enterprise AI Adoption"
authors: "Ruth Appel, Peter McCrory, Alex Tamkin, Miles McCain, Tyler Neylon, Michael Stern"
published: "2025-11-19"
source: "https://arxiv.org/abs/2511.15080"
---

# Anthropic Economic Index Report: Uneven Geographic and Enterprise AI Adoption

**Authors**: Ruth Appel, Peter McCrory, Alex Tamkin, Miles McCain, Tyler Neylon, Michael Stern (Anthropic)
**Published**: November 19, 2025
**Source**: https://arxiv.org/abs/2511.15080
**arXiv ID**: 2511.15080
**Categories**: econ.GN, cs.CY
**Data**: Open-sourced for academic/policy research
**Dataset**: 1M Claude.ai conversations + 1M API transcripts, 150+ countries

---

## Abstract

Second Anthropic Economic Index report documenting Claude usage patterns over time, across 150+ countries and U.S. states, and among API-deploying businesses. Uses privacy-preserving analysis of 2 million total transcripts. Key finding: **users increasingly delegate more autonomy to Claude**, with directive task delegation rising from 27% to 39% over eight months. Geographic concentration strongly favors high-income nations.

---

## Key Findings

### 1. Rising Autonomy Delegation

| Period | Directive Task Delegation Rate |
|--------|-------------------------------|
| ~Early 2025 | 27% |
| ~Late 2025 | **39%** |
| Delta | +12 percentage points over 8 months |

Users are progressively entrusting Claude with more autonomous, complete task execution rather than step-by-step collaboration.

### 2. Geographic Concentration

**High-income nations are significantly overrepresented** in Claude usage relative to their working-age population share.

- Usage concentrated in wealthy countries
- 150+ countries represented, but distribution heavily skewed
- Local economic factors influence:
  - Which topics users bring to Claude
  - Preferred collaboration modes (automation vs. augmentation)
  - Task categories most commonly requested

### 3. Enterprise API Adoption Patterns

API customers use Claude for **specialized task automation** distinct from consumer (Claude.ai) patterns:
- More directive/automative usage vs. consumer augmentative usage
- Specialized domain focus rather than general-purpose queries

---

## Methodology

**Dataset**: 
- 1 million Claude.ai consumer conversations
- 1 million API transcripts (business deployments)

**Tool**: Clio (privacy-preserving analysis — same framework as Economic Tasks paper 2503.04761)

**Geographic scope**: 150+ countries, all U.S. states

**Longitudinal**: Tracks changes over time (first Anthropic Economic Index report was earlier in 2025)

---

## Connection to Prior Work

Builds on the "Which Economic Tasks are Performed with AI?" paper (2503.04761):
- That paper: task-level analysis (what tasks Claude performs)
- This paper: geographic/temporal/enterprise analysis (who uses Claude and how usage evolves)

Together they form the **Anthropic Economic Index** — a framework for empirically tracking AI's economic integration.

---

## Open Data

Researchers open-sourced underlying data for academic and policy research, enabling independent replication and extension of findings.

---

## Workspace Relevance

Contextualizes Claude usage patterns at the macro level:

1. **39% directive delegation (up from 27%)**: The trend toward full task autonomy validates workspace design choices in `autoresearch` (fully autonomous loop) and `implementer` agent (full task delegation) — these match where users are naturally moving
2. **Geographic concentration in high-income nations**: Workspace design for English-language, high-technical-sophistication users is consistent with the actual user base
3. **API = specialized automation**: The workspace itself is an API deployment — enterprise-style automative patterns are correct baseline assumption, not consumer-style exploratory usage
4. **Longitudinal tracking**: This paper validates that tracking usage patterns over time (as `claude-progress.json` does at session level) is useful — macro trends mirror micro session trends
