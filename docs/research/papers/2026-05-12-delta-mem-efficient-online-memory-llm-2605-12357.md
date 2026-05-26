---
title: "δ-mem: Efficient Online Memory for Large Language Models"
authors: "Jingdi Lei, Di Zhang, Junxian Li, Weida Wang, Kaixuan Fan, Xiang Liu, Qihan Liu, Xiaoteng Ma, Baian Chen, Soujanya Poria"
published: "2026-05-12"
source: "https://arxiv.org/abs/2605.12357"
---

# δ-mem: Efficient Online Memory for Large Language Models

**Authors**: Jingdi Lei†, Di Zhang†, Junxian Li, Weida Wang, Kaixuan Fan†, Xiang Liu†, Qihan Liu, Xiaoteng Ma, Baian Chen, Soujanya Poria (†equal contribution)
**Affiliations**: Nanyang Technological University, Fudan University, MindLab, Shanghai Jiao Tong University, The Chinese University of Hong Kong, HKUST (Guangzhou)
**Published**: May 12, 2026
**Source**: https://arxiv.org/abs/2605.12357
**arXiv ID**: 2605.12357
**Categories**: cs.AI
**GitHub**: Declare-lab & MindLab-Research

---

## Abstract

Large language models increasingly need to accumulate and reuse historical information in long-term assistants and agent systems. Simply expanding the context window is costly and often fails to ensure effective context utilization. We propose δ-mem, a lightweight memory mechanism that augments a frozen full-attention backbone with a compact online state of associative memory. δ-mem compresses past information into a fixed-size state matrix updated by delta-rule learning, and uses its readout to generate low-rank corrections to the backbone's attention computation during generation. With only an 8×8 online memory state, δ-mem improves the average score to 1.10× that of the frozen backbone and 1.15× that of the strongest non-δ-mem memory baseline. It achieves larger gains on memory-heavy benchmarks, reaching 1.31× on MemoryAgentBench and 1.20× on LoCoMo, while largely preserving general capabilities. These results show that effective memory can be realized through a compact online state directly coupled with attention computation, without full fine-tuning, backbone replacement, or explicit context extension.

---

## 1. Introduction

### Problem

LLMs deployed in long-term personalized assistants and long-horizon agent systems must accumulate, update, and reuse historical information over extended memory-heavy tasks. Model performance depends not only on understanding the current input, but also on effectively leveraging relevant past context during test-time.

**Context window expansion alone is insufficient**:
- Standard attention incurs quadratic cost with respect to context length
- Models suffer from context degradation or "context rot" when context becomes very long
- Even million-token context windows do not fundamentally solve the memory problem

### Taxonomy of Existing Memory Mechanisms (MMs)

Characterized along two dimensions:
1. **Memory state** — how historical information is stored
2. **Memory steering** — how stored information influences backbone reasoning

Three paradigms:

| Paradigm | How it stores | How it steers | Limitation |
|----------|--------------|---------------|------------|
| Textual Memory Mechanisms (TMMs) | Text entries / summaries | Re-inject into input context | Context-window limits, retrieval noise, compaction loss |
| Outside-Channel Memory Mechanisms (OMMs) | External latent modules | Retrieval / encoding on outside pathways | Overhead, integration complexity, misalignment |
| Parametric Memory Mechanisms (PMMs) | Prefixes or adapter parameters | Static parameter modification | Static nature limits adaptation to dynamically evolving information |

### Proposal: δ-mem

A memory mechanism that keeps a **compact, dynamically updated** online state alongside a **frozen full-attention backbone**:
- Compresses past info into an **Online State of Associative Memory (OSAM)** — a fixed-size matrix
- State continuously updated via **delta-rule learning** as new tokens arrive
- During generation: current input queries state → extracts associative signals → transformed into **low-rank corrections** to backbone attention
- State further updated after each interaction, enabling δ-mem to evolve over time

---

## 2. Preliminaries & Notation

- Input hidden sequence: **x ∈ ℝ^(N×d)**, N = sequence length, d = hidden dimension
- Single-position hidden state: x_t ∈ ℝ^d (column vector)
- Q, K, V: standard attention query/key/value
- S_t: online state after processing position t
- δ-mem maintains matrix **S** as the online state of associative memory

**Delta-rule update** (base form):
```
Given memory key k_t ∈ ℝ^r, value v_t ∈ ℝ^r:
  Prediction: v̂_t = S_{t-1} k_t
  Residual loss: L_t(S) = ‖Sk_t - v_t‖²
  Update: S_t = S_{t-1} + η_t(v_t - S_{t-1}k_t)k_t^T
```

This writes only the **residual information** along the key direction — well-learned associations induce negligible updates; predictive discrepancies dynamically correct the state.

**Gated delta update** (with forget gate, inspired by Qwen-Next):
```
S_t = Γ_t ⊙ S_{t-1} + Δ_t ⊙ (v_t - S_{t-1}k_t)k_t^T
```
- Γ_t controls how much previous memory is retained
- Δ_t controls the strength of the residual write

---

## 3. δ-mem Architecture

### Computation Order (per position)

1. **Read** associative memory signals from old state
2. **Steer** attention using those signals (low-rank corrections)
3. **Write** current information into the state

### 3.1 Memory Projections

Projects hidden state x_t into low-dimensional associative memory space (dimension r):

```
q^m_t = L-norm(tanh(W^m_q x_t))   # query: reads from old state
k^m_t = L-norm(tanh(W^m_k x_t))   # key: how to write
v^m_t = W^m_v x_t                  # value: what to write

Γ_t = σ(W_Γ x_t + b)              # retention gate ∈ ℝ^r
Δ_t = 1 - Γ_t                      # write gate
```

Normalizing query and key reduces state instability from scale drift during long-sequence recurrence. Dimension-wise gating allows some dimensions to retain old memory while others write current information more actively.

### 3.2 Reading from Online State of Associative Memory (OSAM)

```
r_t = S_{t-1} q^m_t
```

- Read vector r_t ∈ ℝ^r from old state with current input as query
- Cost is **independent of history length** (fixed-size state)
- Complementary to standard attention: attention compares query with all keys in explicit context; δ-mem provides **history-dependent steering signals** from the compressed state

### 3.3 Steering Attention via Low-Rank Corrections

Read signal projected into query-side and output-side corrections:

```
δq_t = W_δq r_t      # query-side correction
δo_t = W_δo r_t      # output-side correction

# Corrected query:
q̃_t = q_t + √r · δq_t    where q_t = W_Q x_t

# Attention with corrected query:
a_t = Attn(q̃_t, K_t, V_t)

# Final output with output-side correction:
ỹ_t = a_t + √r · δo_t
```

**Key distinction from static adapters**: Although W_δq and W_δo are fixed after training, their input r_t comes from the dynamic state S_{t-1}. Therefore, the same set of parameters produces **different steering effects** under different histories.

### 3.4 Writing into Online State

After attention, writes current position's information into online state:

```
S_t = Diag(Γ_t) S_{t-1} + Diag(Δ_t)(v^m_t - S_{t-1}k^m_t)k^m_t^T
```

Three terms:
1. **Retain**: Diag(Γ_t) S_{t-1} — retains previous state
2. **Erase**: -Diag(Δ_t) S_{t-1}k^m_t k^m_t^T — removes old prediction along current key direction
3. **Write**: +Diag(Δ_t) v^m_t k^m_t^T — writes new value into same direction

Memory state updated by **error correction with controlled forgetting**, not by unselectly accumulating new outer products.

### 3.5 Writing Granularity Strategies

Three strategies for when to write into the state:

| Strategy | Abbreviation | Write trigger | Pros | Cons |
|----------|-------------|---------------|------|------|
| Token-State Write | TSW | Every token | Finest granularity, captures local changes | Affected by format symbols, repeated expressions, short-term noise |
| Sequence-State Write | SSW | Per message segment (averaged hidden states) | Reduces redundant writes, smoothed evolution | Fine-grained token details absorbed by average |
| Multi-State Write | MSW | Per token, across N parallel sub-states | Reduces mutual interference between memory types | More parameters |

**MSW formulation**:
```
S_t = {S^(1)_t, ..., S^(N)_t}
S^(i)_t = Update^(i)(S^(i)_{t-1}, x_t)
r_t = Concat(r^(1)_t, ..., r^(N)_t)
```

### 3.6 Training Objective

Standard SFT loss. Context tokens written into online state first (producing S_C), **not replayed as explicit backbone inputs** during prediction. Frozen backbone only receives query Q and response Y, state steers attention through δ-mem:

```
L_SFT = -Σ_j log p_{φ,θ}(y_j | Q, y_{<j}, S_C)
```
- θ = trainable δ-mem parameters
- φ = frozen backbone parameters

---

## 4. Experiments

### 4.1 Setup

**Backbone models**:
- Qwen3-4B-Instruct
- Qwen3-8B
- SmolLM3-3B

**Benchmarks**:

| Type | Benchmark | What it measures |
|------|-----------|-----------------|
| General | HotpotQA | Multi-hop reasoning, knowledge-intensive QA |
| General | GPQA-Diamond | Knowledge-intensive QA |
| General | IFEval | Instruction following |
| Memory-heavy | LoCoMo | Long-context conversational memory |
| Memory-heavy | MemoryAgentBench | Retention, retrieval, and utilization across extended interactions |

**Baselines**:
- Textual: BM25RAG, LLMLingua-2, MemoryBank
- Parametric: Context2LoRA, MemGen
- Outside-channel: MLP Memory

### 4.2 Main Results (Qwen3-4B-Instruct backbone)

| Model | IFEval | HotpotQA EM | HotpotQA F1 | GPQA-D | MemAgentBench Avg | LoCoMo Avg | **Final Avg** |
|-------|--------|-------------|-------------|--------|-------------------|------------|--------------|
| Qwen3-4B-Instruct (baseline) | 81.89 | 42.35 | 56.00 | 39.39 | 29.54 | 40.79 | 46.79 |
| +BM25RAG | — | 40.35 | 52.83 | — | 24.49 | 36.68 | — |
| +LLMLingua-2 | — | 36.93 | 50.03 | — | 15.63 | 40.98 | — |
| +MemoryBank | — | — | — | — | 17.65 | 38.14 | — |
| +Context2LoRA | 76.71 | 37.85 | 50.88 | 29.29 | 32.53 | 48.11 | 44.90 |
| +MemGen | 39.37 | 5.36 | 16.27 | 38.89 | 29.61 | 40.05 | 30.66 |
| +MLP Memory | 24.95 | 10.94 | 25.83 | 22.73 | 28.80 | 26.85 | 22.85 |
| **+δ-Mem (SSW)** | 81.70 | 49.22 | 63.43 | **41.41** | 37.84 | 47.05 | **51.44** |
| **+δ-Mem (TSW)** | **82.99** | **49.41** | **63.66** | 40.40 | 36.48 | 46.53 | **51.66** |
| **+δ-Mem (MSW)** | 81.52 | 46.86 | 60.47 | 37.37 | **38.85** | **49.12** | **50.74** |

**Key findings**:
- TSW achieves best average (51.66%), +4.87 over backbone, +6.76 over Context2LoRA
- MSW best on MemoryAgentBench (38.85%) and LoCoMo (49.12%)
- SSW best at GPQA-Diamond (41.41%)
- Textual memory methods show inconsistent gains due to retrieval noise and compaction loss
- Context2LoRA over-fits training distribution
- MLP Memory lacks sequential state accumulation

### 4.3 Cross-Backbone Results

| Model | Baseline Avg | Best δ-Mem Avg | Strategy | Gain |
|-------|-------------|----------------|----------|------|
| Qwen3-4B-Instruct | 46.79% | 51.66% | TSW | +4.87 |
| Qwen3-8B | 47.20% | 50.86% | SSW | +3.66 |
| SmolLM3-3B | 26.08% | 36.96% | MSW | +10.88 |

**Pattern**: More capable models benefit more from SSW (smoother state updates); smaller models benefit more from MSW (separating memory reduces interference).

---

## 5. Ablative Studies

### 5.1 Context Recovery (No-Context Setting)

Tests whether OSAM can preserve useful historical information **without explicit context replay** — history removed, only compressed memory state injected:

| Benchmark | Metric | No-context baseline | δ-Mem (no context) |
|-----------|--------|--------------------|--------------------|
| HotpotQA (Bridge) | EM | 0.08% | 3.97% |
| HotpotQA (Bridge) | F1 | 6.25% | 11.05% |
| HotpotQA (Overall) | EM | 0.08% | 6.48% |
| HotpotQA (Overall) | F1 | 8.27% | 15.20% |
| LoCoMo (Overall) | Avg | 3.49% | 8.05% |

**Conclusion**: Online state stores context-relevant historical signals that can be reused when explicit context is unavailable.

### 5.2 Attention Head Ablation

Where should memory-induced correction be injected within the attention block?

| Configuration | HotpotQA EM | LoCoMo Avg | Final Avg |
|--------------|-------------|------------|-----------|
| q only | 45.87 | 42.43 | 43.15 |
| k only | 43.39 | 38.44 | 42.19 |
| v only | 46.12 | 39.54 | 44.24 |
| **o only** | **48.94** | **39.68** | **47.05** |
| **q+o (default)** | **49.41** | **42.14** | **47.97** |
| q+k+v+o (full) | 49.94 | 41.08 | **48.05** |

**Default choice**: q+o offers the best performance-efficiency trade-off; qkvo gives marginal gain at extra parameter overhead.

### 5.3 Insertion Depth Ablation

| Layer configuration | HotpotQA EM | LoCoMo Avg | Final Avg |
|--------------------|-------------|------------|-----------|
| Front 12 layers | 45.52 | 39.06 | 44.39 |
| Middle 12 layers | 47.44 | 44.00 | 46.66 |
| Back 12 layers | 44.58 | 40.60 | 44.06 |
| **All layers** | **49.41** | **42.14** | **47.97** |

**Best**: All layers. Middle layers outperform front/back among partial configurations — intermediate layers provide effective memory injection interface, balancing semantic abstraction and task-specific computation.

---

## 6. Related Work

### Textual Memory Mechanisms (TMMs)
Early RAG systems (Lewis et al. 2020; Borgeaud et al. 2022); agent-oriented methods (MemGPT, MemoryBank, Mem0) extend to continuous interaction via logging, summarization, reflection. Constrained by tokenized form: sensitive to compression fidelity, retrieval noise, context budget.

**δ-mem difference**: Does not route compressed history back through token space; maintains compact online state and steers Transformer through low-rank attention corrections.

### Outside-Channel Memory Mechanisms (OMMs)
Memorizing Transformers (Wu et al. 2022): stores past internal representations as non-differentiable key-value memories, retrieves via approximate kNN. LongMem (Wang et al. 2023): frozen backbone as memory encoder + adaptive residual side network.

**δ-mem difference**: Memory not retrieved as auxiliary external source; compact online state directly produces low-rank corrections to attention computation — memory participates in the current forward pass.

### Parametric Memory Mechanisms (PMMs)
Prefix-Tuning, LoRA, ROME, MEMIT. Generally fixed after training or updated through discrete editing steps, not continuously evolving with the sequence.

**δ-mem difference**: LoRA's low-rank update is static; δ-mem generates low-rank attention corrections from a compact online state at runtime — same parameters, different steering effects per history.

---

## 7. Conclusion

δ-mem equips a frozen full-attention backbone with a compact, dynamically updated online state of associative memory. Key properties:

1. **No backbone modification**: frozen throughout training and inference
2. **Fixed-size state**: even 8×8 (64 entries) suffices for measurable gains
3. **Directly coupled with attention**: not a separate retrieval system
4. **Online / streaming**: evolves with the sequence during generation
5. **Context recovery**: stores signals reusable even when explicit context is removed

Results suggest compact online states can serve as a scalable and efficient interface for test-time memory in frozen Transformer backbones.

---

## Key Numbers Summary

| Metric | Value |
|--------|-------|
| Memory state size | 8×8 = 64 entries |
| Average score vs frozen backbone | 1.10× |
| Average score vs strongest non-δ-mem baseline | 1.15× |
| MemoryAgentBench improvement | 1.31× |
| LoCoMo improvement | 1.20× |
| TTL subtask (MemoryAgentBench) | nearly 2× (35.30% → 50.50%) |
| Best backbone (SmolLM3-3B) gain | 26.08% → 36.96% (+10.88pp) |
| Context recovery HotpotQA EM | 0.08% → 6.48% (no explicit context) |
