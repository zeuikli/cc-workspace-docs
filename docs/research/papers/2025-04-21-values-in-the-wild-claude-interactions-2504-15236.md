---
title: "Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions"
authors: Saffron Huang, Esin Durmus, Miles McCain, Kunal Handa, Alex Tamkin, Jerry Hong, Michael Stern, Arushi Somani, Xiuruo Zhang, Deep Ganguli
published: 2025-04-21
source: "https://arxiv.org/abs/2504.15236"
---

# Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions

**Authors**: Saffron Huang, Esin Durmus, Miles McCain, Kunal Handa, Alex Tamkin, Jerry Hong, Michael Stern, Arushi Somani, Xiuruo Zhang, Deep Ganguli (Anthropic)
**Published**: April 21, 2025
**Source**: https://arxiv.org/abs/2504.15236
**arXiv ID**: 2504.15236
**Categories**: cs.CL, cs.AI
**Data**: HuggingFace — Anthropic/values-in-the-wild

---

## Abstract

First large-scale empirical mapping of AI values "in the wild." Using privacy-preserving Clio analysis of 700,000 anonymized Claude.ai conversations, the authors discover and taxonomize 3,307 distinct AI values and 2,483 human values. Claude expresses many practical and epistemic values, typically supports prosocial human values, and resists values like moral nihilism. Values are highly context-dependent.

---

## Dataset

| Parameter | Value |
|-----------|-------|
| Total conversations analyzed | 700,000 anonymized Claude.ai conversations |
| Period | February 18–25, 2025 |
| Subjective conversations (used for analysis) | 308,210 (44% of total) |
| Model composition | 91% Claude 3.5 Sonnet |
| Human validation accuracy | **98.8%** |

---

## Key Findings: Most Common Values

### Top AI Values (by frequency)

| Rank | AI Value | Frequency |
|------|----------|-----------|
| 1 | Helpfulness | 23.4% |
| 2 | Professionalism | 22.9% |
| 3 | Transparency | 17.4% |
| 4 | Clarity | 16.6% |
| 5 | Thoroughness | 14.3% |

### Top Human Values (by frequency)

| Rank | Human Value | Frequency |
|------|-------------|-----------|
| 1 | Authenticity | 3.8% |
| 2 | Efficiency | 2.6% |
| 3 | Clarity | 2.2% |
| 4 | Professionalism | 1.5% |
| 5 | Directness | 1.5% |

---

## Value Taxonomy: Five Domains

| Domain | Examples |
|--------|---------|
| **Practical values** | Service delivery, competence, helpfulness |
| **Epistemic values** | Knowledge, accuracy, historical accuracy |
| **Social values** | Relationships, community, mutual respect |
| **Protective values** | Safety, boundaries, harm prevention |
| **Personal values** | Growth, fulfillment, human agency |

Total: **3,307 AI values** + **2,483 human values** discovered

---

## Context-Dependent Value Expression

Values vary significantly by conversation context:

| Context | Prominent Values |
|---------|-----------------|
| Relationship advice | "healthy boundaries," "mutual respect" |
| Historical event analysis | "historical accuracy" |
| Technology ethics | "human agency" |
| Mental health conversations | "emotional validation" |
| AI resistance moments | "harm prevention" becomes explicit |

---

## Human Value Response Patterns

When human values were present (64.3% of conversations), Claude responded:

| Response Type | Rate |
|---------------|------|
| Strong support | 28.2% |
| Mild support | 14.5% |
| Neutral acknowledgment | 9.6% |
| Reframing | 6.6% |
| Mild resistance | 2.4% |
| Strong resistance | 3.0% |

---

## Notable Patterns

### Value Mirroring
- Claude mirrors user values: **20.1%** of supportive interactions
- But only **1.2%** during resistance moments
- Values become explicit **during boundary-setting**, not routine interactions

### Uncommon Problematic Values
Rare but flagged values each < 0.16% frequency:
- "sexual exploitation"
- "dominance"
- "amorality"

Associated task patterns enable identification of potential jailbreaks.

### Cross-Model Variations
Appendix B.5: Notable differences in value expression between Claude Sonnet vs. Opus variants.

---

## Alignment Mapping

Discovered values align with "helpful, harmless, honest" training framework:

| Training Principle | Corresponding Values Found |
|-------------------|--------------------------|
| Helpful | "accessibility," "user enablement" |
| Harmless | "patient wellbeing," "child safety" |
| Honest | "historical accuracy," "epistemic humility" |

**Trans-situational values**: Claude exhibits stable values across contexts, primarily centered on "competent and supportive assistance."

---

## Methodology

**Tool**: Clio (privacy-preserving analysis)
**Models used for extraction**: Claude 3.5 Sonnet + Haiku

**Extraction targets**:
- **AI values**: Normative considerations influencing responses (explicit statements + revealed preferences)
- **Human values**: Only explicitly stated values (privacy preservation)
- **Response type**: 7 classifications (strong support → strong resistance)
- **Task categorization**: Primary purpose/request type

**Statistical method**: Chi-square testing + adjusted Pearson residuals + Bonferroni correction for multiple comparisons.

---

## Limitations

- Narrow timeframe (one week) — no longitudinal patterns
- Requires significant deployment data — not applicable pre-release
- Using Claude to evaluate Claude may create recognition biases
- English keyword extraction potentially underrepresents cross-cultural values
- Only subjective conversations analyzed (44% of total)

---

## Contributions

1. First large-scale empirical AI values taxonomy (3,307 values hierarchically organized)
2. Task-dependency analysis revealing context-specific value expression
3. Human-AI value interaction mapping (mirroring and opposition patterns)
4. Response pattern analysis across task and value contexts
5. Identification of undesirable value expressions for safety team investigation

---

## Workspace Relevance

Empirical foundation for understanding Claude's actual value expression in practice:

1. **Helpfulness 23.4%, Professionalism 22.9%**: Top expressed values confirm `core.md` "helpful, harmless, honest" training works as intended at scale
2. **Values become explicit during resistance**: Boundary-setting interactions are where Claude's values are most legible — relevant to `harness-meta` safety audit and `opus-pilot` adversarial testing
3. **0.16% problematic value rate**: Low but non-zero — `autoresearch` verify gate and `harness-meta` CAR framework should include value-expression spot checks for sensitive domains
4. **20.1% value mirroring in supportive vs. 1.2% in resistance**: Strong asymmetry — Claude is more reflective (mirrors user) when agreeing and more principled (expresses own values) when resisting
5. **Sonnet vs. Opus value differences**: `sonnet-pilot` and `opus-pilot` may produce different value expression profiles — empirically confirmed, not just theoretical
