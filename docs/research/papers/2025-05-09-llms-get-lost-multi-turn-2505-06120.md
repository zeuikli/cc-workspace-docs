---
title: "LLMs Get Lost In Multi-Turn Conversation"
arxiv_id: 2505.06120
authors: "Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville"
fetched: 2026-05-27
published: 2025-05-09
source: "https://arxiv.org/abs/2505.06120"
source_tier: P
---

# LLMs Get Lost In Multi-Turn Conversation

**Authors**: Philippe Laban (Microsoft Research), Hiroaki Hayashi* (Salesforce Research), Yingbo Zhou (Salesforce Research), Jennifer Neville (Microsoft Research)  
*Equal contributions  
**Published**: May 2025  
**Source**: https://arxiv.org/abs/2505.06120  
**arXiv ID**: 2505.06120  
**Categories**: cs.CL  
**Dataset**: [Microsoft/lost_in_conversation](https://huggingface.co/datasets/Microsoft/lost_in_conversation)

---

## Abstract

Large Language Models (LLMs) are conversational interfaces. As such, LLMs have the potential to assist their users not only when they can fully specify the task at hand, but also to help them define, explore, and refine what they need through multi-turn conversational exchange. Although analysis of LLM conversation logs has confirmed that underspecification occurs frequently in user instructions, LLM evaluation has predominantly focused on the single-turn, fully-specified instruction setting. In this work, we perform large-scale simulation experiments to compare LLM performance in single- and multi-turn settings. Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks. Analysis of 200,000+ simulated conversations decomposes the performance degradation into two components: a minor loss in aptitude and a significant increase in unreliability. We find that LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely. In simpler terms, we discover that when LLMs take a wrong turn in a conversation, they get lost and do not recover.

---

## Core Thesis

All top open- and closed-weight LLMs exhibit an average 39% performance drop when moving from single-turn to multi-turn underspecified conversations, despite identical underlying tasks. This degradation is primarily caused not by loss of task aptitude (only -16% drop) but by a catastrophic increase in unreliability (+112% on average), where the same model oscillates wildly between correct and incorrect answers across repeated runs of the same conversation. Notably, o3 drops from 98.1% (single-turn) to 64.1% (multi-turn), and additional test-time compute (reasoning tokens) provides no protection against this effect.

---

## 1. Introduction

Today's LLMs function as conversational interfaces (ChatGPT, Gemini, Claude), enabling users to interact through multiple conversation turns. Though studies confirm underspecification in user instructions is prevalent, LLM systems are typically evaluated in single-turn, fully-specified settings.

Most prior multi-turn evaluation work treats conversation as **episodic**: turns relate to each other but can be evaluated in isolation. The authors argue this overestimates LLM performance. Underspecification—where users provide information gradually through the conversation—is the dominant real-world pattern ("the principle of least effort").

This work closes the gap by creating a simulation environment for multi-turn underspecified conversations using **sharded simulation**, which transforms existing single-turn benchmarks into multi-turn underspecified conversations.

**Key findings summary:**
1. Average 25-point drop in performance (from ~90% single-turn to ~65% multi-turn)
2. Drop observed even in two-turn conversations
3. Drop observed across all 15 tested LLMs, from Llama3.1-8B to Gemini 2.5 Pro
4. Root causes: premature assumptions, over-reliance on incorrect prior attempts, loss-of-middle-turns, and overly verbose responses

---

## 2. Background and Related Work

Previous multi-turn evaluation (MT-bench and successors) focused on episodic tasks that can be evaluated in isolation per turn. This work argues episodic tasks:
- Overestimate LLM performance
- Do not involve fusing gradually revealed information
- Prevent direct single-turn vs. multi-turn performance comparison

Prior user simulation approaches: templates, LLM-based, human annotators, real users. This work uses LLM-based simulation (GPT-4o-mini) for controlled flexibility and scalability while acknowledging it is idealized and likely underestimates real-world degradation.

---

## 3. Simulating Underspecified, Multi-Turn Conversation

### 3.1 Sharding Process

The sharding process transforms a fully-specified instruction into a **sharded instruction**: a set of smaller shards that jointly deliver the same information.

**Example (GSM8K):**

*Fully-specified:* "Jay is making snowballs to prepare for a snowball fight with his sister. He can build 20 snowballs in an hour, but 2 melt every 15 minutes. How long will it take before he has 60 snowballs?"

*Sharded:*
- Shard 1: How long before Jay's ready for the snowball fight?
- Shard 2: He's preparing for a snowball fight with his sister.
- Shard 3: He can make 20 snowballs per hour.
- Shard 4: He's trying to get to 60 total.
- Shard 5: The problem is that 2 melt every 15 minutes.

Key property: Shard 1 always introduces the high-level intent; subsequent shards each provide one clarification. Taken jointly, shards equal the original instruction.

### 3.2 Simulating Sharded Conversations

Three parties in the simulation:
- **Assistant**: the LLM being evaluated (receives no meta-information about the simulation type)
- **User simulator**: GPT-4o-mini, has access to full sharded instruction, reveals one shard per turn in natural rephrasing
- **System**: classifies response strategies and evaluates answer attempts

**Response strategy taxonomy** (7 categories based on Herlihy et al.): clarification, refusal, hedging, interrogation, discussion, missing, or **answer attempt**.

Conversation ends when: (1) a correct answer attempt is made, or (2) all shards have been revealed.

Simulation error rate: <5% of inspected conversations; errors disfavored the assistant in <2% of cases.

### 3.3 Simulation Types

| Type | Description | Purpose |
|------|-------------|---------|
| **Full** | Single-turn, original instruction | Baseline |
| **Concat** | Single-turn, shards concatenated as bullet points | Verify rephrasing doesn't cause performance loss |
| **Sharded** | Multi-turn, one shard revealed per turn | Primary evaluation |
| **Recap** | Sharded + final turn recapitulating all shards | Agent mitigation strategy |
| **Snowball** | Each turn reveals new shard + repeats all previous shards | Gradual agent mitigation |

---

## 4. Task and Metric Selection

### 4.1 Six Tasks

| Task | Description | Source Dataset | Evaluation |
|------|-------------|---------------|------------|
| **Code** | Write Python function | HumanEval, LiveCodeBench | Binary (execute) |
| **Database** | Text-to-SQL query | Spider | Binary (execute) |
| **Actions** | API function calling | Berkeley Function Calling Leaderboard (BFCL) | Binary (semantic) |
| **Math** | Elementary math word problems | GSM8K | Binary (numerical) |
| **Data-to-text** | Generate caption from tabular data | ToTTo | Continuous (BLEU) |
| **Summary** | Multi-document summarization with citations | Summary of a Haystack | Continuous (LLM-as-judge) |

90–120 sharded instructions per task. Semi-automatic process: GPT-4o proposed/verified sharding candidates; authors reviewed and edited. ~3 hours of manual work per 100 instructions.

### 4.2 Three Metrics

Given N=10 repeated simulations per (model, instruction, simulation type):

- **Average performance (P̄)**: mean score across simulations (0–100)
- **Aptitude (A⁹⁰)**: 90th percentile score — best-case performance estimate
- **Unreliability (U¹⁰⁹⁰)**: 90th minus 10th percentile — gap between best and worst outcomes

All binary tasks mapped to 0–100 scale; all six tasks aggregated on common scale.

---

## 5. Simulation Scale and Parameters

- **600 total instructions** (6 tasks × ~100 each)
- **15 LLMs** from 8 model families
- **3 simulation types** per instruction: Full, Concat, Sharded
- **N=10 simulations** per (model, instruction, type)
- **Total: 200,000+ simulated conversations**
- **Estimated cost: ~$5,000**
- Default temperature T=1.0

**Models tested:**
- OpenAI: GPT-4o-mini, GPT-4o, o3, GPT-4.1
- Anthropic: Claude 3 Haiku, Claude 3.7 Sonnet
- Google: Gemini 2.5 Flash, Gemini 2.5 Pro
- Meta: Llama3.1-8B-Instruct, Llama3.3-70B-Instruct, Llama 4 Scout
- AI2: OLMo-2-13B
- Microsoft: Phi-4
- DeepSeek: DeepSeek-R1
- Cohere: Command-A

---

## 6. Results

### 6.1 Average Performance (Table 1 — Selected Results)

Every model sees performance degrade on every task comparing Full vs. Sharded, with **average degradation of -39%**.

| Model | Full (avg) | Sharded (avg) | Drop |
|-------|-----------|--------------|------|
| Llama3.1-8B | ~27–45 range | lower | ~37% |
| OLMo-2-13B | ~19 | lower | ~86.5% drop noted |
| Claude 3 Haiku | ~45 | ~32 | ~91.6% retained → ~8% drop |
| GPT-4o-mini | ~76 | ~50 | ~93.0% → 56.2% |
| Llama3.3-70B | ~72 | ~52 | ~93.2% → 64.2% |
| Phi-4 | ~53 | ~39 | ~99.0% → 61.7% |
| Command-A | ~72 | ~45 | ~97.3% → 60.4% |
| Llama 4 Scout | ~74 | ~46 | ~91.0% → 66.1% |
| **o3** | **~86** | **~53** | **98.1% → 64.1%** |
| Claude 3.7 Sonnet | ~78 | ~66 | ~100.4% → 65.9% |
| DeepSeek-R1 | ~99 | ~71 | ~103.6% → 60.8% |
| GPT-4o | ~88 | ~61 | ~94.5% → 57.9% |
| Gemini 2.5 Flash | ~97 | ~68 | ~99.3% → 65.8% |
| GPT-4.1 | ~97 | ~73 | ~97.9% → 61.8% |
| Gemini 2.5 Pro | ~97 | ~68 | ~100.1% → 64.5% |

Key findings:
- **Concat ≈ Full** (Concat averages 95.1% of Full), confirming performance loss is not due to information loss during sharding
- **More performant models get equally lost**: Claude 3.7 Sonnet and Gemini 2.5 suffer 30–40% degradation just like smaller models
- **Reasoning models (o3, R1) offer no protection**: they deteriorate similarly to non-reasoning models; reasoning models generate 33% longer responses on average, introducing more assumptions

### 6.2 Aptitude vs. Reliability Analysis

**Single-turn pattern**: Higher aptitude → higher reliability (lower unreliability). Better models more robust to input variation.

**Multi-turn pattern (dramatic contrast)**:
- Aptitude drop: only **-16%** on average (modest)
- Unreliability increase: **+112%** on average (catastrophic, more than doubling)
- In multi-turn settings, **all models show similar high unreliability** regardless of aptitude — the single-turn aptitude-reliability correlation disappears entirely
- Performance gap between best and worst simulated run: **~50 percentile points** on average for a fixed instruction

This refines the phenomenon: the 39% average performance drop is driven primarily by **increased unreliability**, not loss of aptitude.

**Four root causes identified (Appendix F):**
1. LLMs prematurely propose full answer attempts, making assumptions about unspecified problem details
2. Over-reliance on previous (incorrect) answer attempts — leading to lengthier "bloated" answers
3. Loss-of-middle-turns: LLMs over-weight first and last turns, neglecting middle conversation turns
4. Overly verbose responses, introducing assumptions that distract from user utterances

### 6.3 Gradual Sharding Experiment

Tested 31 instructions with shard set sizes from 1 to 8 shards (GPT-4o and GPT-4o-mini).

**Finding**: Both models get lost even with **two-shard instructions** — any conversation with underspecification across ≥2 turns causes the phenomenon. Providing all information at once (1 shard = single-turn) is the only effective way to ensure reliability.

---

## 7. Implications

### 7.1 For System and Agent Builders

Tested Recap and Snowball as agent-style mitigations:

| Simulation | GPT-4o-mini | GPT-4o |
|-----------|-------------|--------|
| Full | 86.8 | 93.0 |
| Concat | 84.4 | 90.9 |
| Sharded | 50.4 | 59.1 |
| Recap | 66.5 | 76.6 |
| Snowball | 61.8 | 65.3 |

- Recap and Snowball improve over Sharded but still lag behind Full/Concat
- Snowball (realistic intervention) mitigates 15–20% of the Full-to-Sharded degradation
- Conclusion: Offloading multi-turn handling to agent frameworks is insufficient; **LLMs need native multi-turn support**

### 7.2 For LLM Builders

**Temperature reduction does not fix multi-turn unreliability:**

Unreliability (U¹⁰⁹⁰) at varying assistant temperatures (AT):

| Setting | GPT-4o-mini AT=1.0 | AT=0.5 | AT=0.0 | GPT-4o AT=1.0 | AT=0.5 | AT=0.0 |
|---------|-------------------|--------|--------|---------------|--------|--------|
| Full | 16.0 | 15.0 | 6.8 | 17.8 | 8.0 | 2.8 |
| Concat | 20.2 | 17.8 | 9.5 | 20.2 | 17.8 | 5.8 |
| Sharded (UT=1.0) | 49.8 | 46.8 | 51.0 | 41.0 | 43.8 | 31.8 |
| Sharded (UT=0.0) | 38.5 | 28.0 | 30.5 | 35.8 | 38.0 | 29.7 |

- Single-turn: 50–80% unreliability improvement when AT decreases
- Multi-turn: GPT-4o-mini sees **no improvement** with lower AT; GPT-4o only 15–20%
- Even at T=0.0 for both user and assistant, unreliability remains ~30%
- Root cause: one token difference in early turn → cascading deviations across the conversation

**Call to action for LLM builders**: jointly optimize aptitude AND reliability. A reliable LLM should:
1. Achieve similar aptitude in single- and multi-turn settings
2. Have U¹⁰⁹⁰ < 15 in multi-turn settings
3. Achieve these at unmodified temperature (T=1.0)

### 7.3 For NLP Practitioners

Current benchmarks comparing models purely on single-turn performance do not reflect multi-turn real-world behavior. The sharding process (~3 hours per 100 instructions with LLM assistance + manual validation) allows practitioners to extend any existing benchmark to multi-turn evaluation.

**Translation task compatibility check** (Table 4): GPT-4o-mini and GPT-4o showed no degradation on translation across Full/Concat/Sharded (scores ~40–43), indicating certain task types naturally resist the phenomenon.

The authors encourage NLP practitioners to release sharded versions of benchmarks alongside fully-specified ones.

---

## 8. Limitations

- Simulated conversations are idealized: guaranteed to end with sufficient information, no adversarial user behavior
- Limited to English-language and analytical (non-creative) tasks
- Not representative of real human-AI conversations
- These idealizations suggest observed degradations likely **underestimate** real-world effects
- Conversation trajectories are not representative of naturalistic human conversations

---

## 9. Key References

- Herlihy et al. — LLM response categorization framework (basis for 7-strategy taxonomy)
- MT-bench (Zheng et al.) — episodic multi-turn evaluation baseline
- GSM8K (Cobbe et al.) — math task source
- HumanEval (Chen et al.) + LiveCodeBench — code task source
- Spider (Yu et al.) — database/SQL task source
- BFCL (Yan et al.) — function calling task source
- ToTTo (Parikh et al.) — data-to-text task source
- Summary of a Haystack (Laban et al.) — long-context summary task source
- Autogen (Wu et al.), LangChain — agent frameworks discussed in implications
- Humanity's Last Exam — cited for aptitude-focused benchmarking contrast
