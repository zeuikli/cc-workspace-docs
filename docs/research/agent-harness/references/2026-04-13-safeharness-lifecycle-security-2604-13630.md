---
title: "SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment"
arxiv_id: 2604.1363
authors: "Xixun Lin, Yang Liu, Yancheng Chen, Yongxuan Wu, Yucheng Ning, Yilong Liu, Nan Sun, Shun Zhang, Bin Chong, Chuan Zhou, Yanan Cao"
fetched: 2026-05-23
published: 2026-04-13
source: "https://arxiv.org/abs/2604.13630"
source_tier: P
---

# SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment

**Authors**: Xixun Lin, Yang Liu, Yancheng Chen, Yongxuan Wu, Yucheng Ning, Yilong Liu, Nan Sun, Shun Zhang, Bin Chong, Chuan Zhou, Yanan Cao  
**Affiliations**: Institute of Information Engineering (Chinese Academy of Sciences), Academy of Mathematics and Systems Science (Chinese Academy of Sciences), Institute of Applied Physics and Computational Mathematics, Peking University  
**Published**: April 2026  
**Source**: https://arxiv.org/abs/2604.13630  
**arXiv ID**: 2604.13630  
**Categories**: cs.CR, cs.AI

---

## Abstract

SafeHarness presents a security framework embedding defense mechanisms throughout the agent harness lifecycle. The system achieves **approximately 38% reduction in Unsafe Behavior Rate (UBR) and 42% reduction in Attack Success Rate (ASR)** compared to unprotected baselines while maintaining core task utility across three harness configurations and multiple attack scenarios. The key insight: security must be an architectural principle embedded in harness design, not an external layer added on top.

---

## 1. Problem: Structural Gaps in Existing Agent Security

The authors identify three structural gaps in existing agent security approaches:

| Gap | Description |
|-----|-------------|
| **Context Blindness** | External defenses lack visibility into harness-internal state and adversarial provenance |
| **Inter-layer Isolation** | Security mechanisms operate independently without coordinated response |
| **Lack of Resilience** | Defenses employ binary pass-or-block decisions without progressive degradation |

These gaps mean existing defenses (system-prompt warnings, guardrails, LlamaFirewall) fail against sophisticated, multi-vector attacks that exploit harness-internal execution paths.

---

## 2. Four-Layer Architecture

SafeHarness implements defense across four lifecycle phases:

### Layer 1: Inform (Input Processing)
**Stage**: Before any model processing

**Mechanisms**:
- **Structural sanitization**: Unicode/encoding obfuscation removal
- **Pattern-based detection**: Regex matching for known injection phrases
- **Semantic filtering**: LLM judge for paraphrased injections that evade pattern matching
- **Provenance tagging**: Every input tagged with source type and trust level

Filters both user inputs AND tool outputs (addressing indirect prompt injection via poisoned tool responses).

### Layer 2: Verify (Decision Making)
**Stage**: Before executing model-generated actions

**Three-tiered progressive verification**:

| Tier | Method | Cost | Depth |
|------|--------|------|-------|
| Tier 1 | Rule-based compliance, deterministic risk scoring | Low | Shallow |
| Tier 2 | Contextual judge model evaluation | Medium | Medium |
| Tier 3 | Causal diagnostics: does action stem from legitimate intent or adversarial injection? | High | Deep |

Tier escalation occurs automatically based on risk score from Tier 1.

### Layer 3: Constrain (Action Execution)
**Stage**: During tool execution

**Mechanisms**:
- **Capability tokens**: Per-tool tokens with TTL and invocation limits
- **Tier enforcement**: Dynamic privilege ceilings preventing privilege escalation
- **Integrity verification**: HMAC-SHA256 signatures on tool descriptions (detecting tool tampering)

**Five tool risk tiers**: `read_only` → `write` → `execute` → `network` → `destructive`

### Layer 4: Correct (State Update)
**Stage**: After execution, state recovery

**Mechanisms**:
- **State checkpointing**: Periodic snapshots including protected memory
- **Attack-triggered rollback**: Revert to safe checkpoint upon confirmed attack
- **Adaptive degradation**: 5 degradation levels progressively restricting tool access
- **Automatic recovery**: Restore privileges after configurable safe-action window

---

## 3. Cross-Layer Mechanisms

### Protected Memory with Provenance
Append-only store tracking: source, authorship, timestamp, content hash. Detects anomalous mutation patterns that indicate memory injection attacks.

### Entropy Monitor
Tracks violation rate within sliding window (default: 20 actions). Escalates Layer 2 verification when windowed violation rate exceeds threshold (default: 0.3). This enables **proactive defense** rather than reactive blocking.

### Inter-Layer Feedback Channels

| Source Layer | Target Layer | Trigger | Action |
|-------------|-------------|---------|--------|
| L1 | L2 | Injection detection | Escalate verification tier |
| L2 | L4 | Confirmed attack | Trigger rollback/degradation |
| L4 | L3 | Degradation activated | Tighten privilege ceiling |
| L4 | L2/L3 | Recovery window elapsed | Restore normal operation |

---

## 4. Threat Model

Six attack vectors mapped to execution phases:

| Threat | Phase | Primary Defense Layer |
|--------|-------|----------------------|
| Direct Injection | Input | L1 (Inform) |
| Indirect Injection (tool output poisoning) | Input | L1 (Inform) |
| Tool Abuse | Execution | L3 (Constrain) |
| Tool Tampering (description modification) | Execution | L3 HMAC verification |
| Memory Corruption (fabricated history) | Cross-phase | Protected Memory |
| Privilege Escalation (parameter escalation) | Execution | L3 (Constrain) |

Attack scenarios tested:
- **A1**: Context poisoning
- **A2**: Indirect injection (tool output poisoning)
- **A3**: Tool tampering (description modification, parameter escalation)
- **A4**: Memory injection (fabricated history)
- **A5**: Composite (simultaneous multi-vector attacks)

---

## 5. Experimental Results

### Setup
- **Dataset**: Agent-SafetyBench (2,000 tasks, 349 environments, 8 risk categories)
- **Agent Models**: DeepSeek-V3.2 (Chat and Reasoner modes)
- **Judge Model**: GPT-4o-mini (separate from agent model)
- **Harness Configurations**: ReAct, Multi-Agent, Self-Evolving
- **Baselines**: Unprotected, System-Prompt, Guardrail, LlamaFirewall, SafeHarness

### Safety Results (Unsafe Behavior Rate — lower is better)

| Configuration | Unprotected UBR | SafeHarness UBR | Reduction |
|--------------|-----------------|-----------------|-----------|
| ReAct (Chat) | 51.18% | 28.74% | **-22.4pp** |
| Multi-Agent (Chat) | 44.99% | 26.31% | **-18.7pp** |
| Self-Evolving (Chat) | 61.98% | 39.18% | **-22.8pp** |
| **Average** | — | — | **~38%** |

### Attack Success Rate Reduction
22.8–24.7 percentage points across configurations.

### Utility Preservation (Task Completion Rate)
- **ReAct / Self-Evolving**: TCR within 1–2pp of unprotected — utility maintained
- **Multi-Agent**: 86.5% → 77.9% TCR — reflects blocked unsafe completions (expected tradeoff)

### Utility Under Attack (UA = completed AND safe)
- **ReAct (Chat)**: 45.6% → 67.5% (+21.9pp) — substantial improvement in safe completions

### Defense Activity
- Guardrail/LlamaFirewall: 54–184 blocked actions per evaluation
- SafeHarness: **709–1,477 blocked actions** — reflecting multi-layer per-step checking

---

## 6. Comparison to Baselines

| Defense | Architecture | Harness Visibility | Multi-Layer Coordination |
|---------|-------------|-------------------|------------------------|
| System-Prompt | Static text | None | No |
| Guardrail | Output filter | Output only | No |
| LlamaFirewall | Input/output filter | Minimal | No |
| **SafeHarness** | Lifecycle integration | Full (4 layers) | Yes |

---

## 7. Evaluation Metrics

**Safety**: UBR (Unsafe Behavior Rate), ASR (Attack Success Rate), NNH (Expected interactions before unsafe outcome = 1/UBR)

**Utility**: TCR (Task Completion Rate), UA (Utility Under Attack = completed AND safe)

**Defense Activity**: Blk (total intercepted actions)

---

## 8. Limitations

- Tool execution environment is simulated, not deployed on real backends
- Evaluation uses LLM-as-Judge with potential bias (mitigated by separate agent/judge models)
- Multi-tier verification introduces inference overhead (concentrated on suspicious actions via entropy monitor)
- Attack coverage reflects documented threat vectors, not comprehensive adversarial landscape

---

## 9. Implications for Harness Design

1. **Security as architecture**: External bolt-on security fails because it lacks harness-internal visibility. Security must be built into the harness lifecycle from the start.

2. **Provenance tracking**: Every input's source must be tracked. Unsigned tool outputs are an attack surface.

3. **Progressive degradation over binary blocking**: Binary block/allow creates brittleness. 5-level degradation maintains partial functionality under attack.

4. **Multi-layer coordination**: Individual security layers are insufficient. Cross-layer feedback (entropy monitor, escalation channels) is essential for detecting sophisticated attacks.

5. **HMAC for tool integrity**: Tool descriptions are a high-value attack target. Signing them with HMAC-SHA256 provides tamper detection.

---

## References

- Lin et al. (2026) SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment. arXiv:2604.13630
- Greshake et al. (2023) Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection
- Liu et al. (2024) Agent-SafetyBench: Evaluating the Safety of LLM Agents
- Inan et al. (2023) Llama Guard: LLM-based input-output safeguard for human-AI conversations
- Anthropic (2025) Claude's Constitution and safety principles
- Perez and Ribeiro (2022) Ignore previous prompt: Attack techniques for language models

---

## Workspace Alignment Analysis

| Paper Concept | cc-workspace Current State | Opportunity |
|---------------|---------------------------|-------------|
| Provenance tagging | No source tracking on tool outputs | Tag external content in `<untrusted_external_data>` (already in subagent-strategy.md) ✅ |
| HMAC tool integrity | No tool description signing | Low priority for local harness |
| Entropy monitor (violation rate) | Manual observation only | Add violation counter to GOTCHAS.md tracking |
| Progressive degradation (5 levels) | Binary: proceed or stop | Model as: normal → warn → require confirmation → read-only → halt |
| Protected memory with provenance | MEMORY.md (no provenance) | Add source/date fields to MEMORY.md entries |
| Indirect injection defense (L1) | `<untrusted_external_data>` wrapping | ✅ Already partially aligned—strengthen in hooks |
| UBR metric | No safety metric tracking | Consider tracking unexpected tool calls per session |
