---
url: "https://arxiv.org/abs/2606.01770"
title: "Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams"
archived_date: 2026-06-14
arxiv_id: 2606.0177
authors: ["Zewen Liu", "Zhan Shi", "Yisi Sang", "Bing He", "Minhua Lin", "Tianxin Wei", "Dakuo Wang", "Benoit Dumoulin", "Wei Jin", "Hanqing Lu"]
pdf_path: pdfs/2606.01770.pdf
published_date: 2026-06-01
---

# Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams

**Authors**: Zewen Liu, Zhan Shi, Yisi Sang, Bing He, Minhua Lin, Tianxin Wei, Dakuo Wang, Benoit Dumoulin, Wei Jin, Hanqing Lu
**Published**: June 2026 (revised June 3, 2026)
**Source**: https://arxiv.org/abs/2606.01770
**arXiv ID**: 2606.01770
**Categories**: not specified in fetched content

---

## Abstract

This research addresses limitations of existing auto-harness systems that optimize LLM agents through prompt and skill refinement but struggle with real-world deployments involving evolving task streams. The proposed framework decomposes performance gaps into evolution and adaptation losses, utilizing a multi-agent evolver and adaptive harness routing to maintain sustained improvement across heterogeneous, shifting tasks.

---

## Key Findings

- **Multi-agent evolution yields 118% CWR gain on PolyBench**: single-agent CWR 20.3 → multi-agent 44.3 (+24.0 pp); CTF-Dojo +5 pp (38%→43%); FutureX +6 pp (38%→44%).
- **Full System achieves best results across three benchmarks**: PolyBench accuracy 80.9% / return +330%; CTF-Dojo pass@1 50.2%; FutureX pass@1 47.3% — compared to no-evolution Sonnet baselines of 22.2%, 37.2%, 31.0% respectively.
- **Significant adaptation loss quantified**: CTF-Dojo oracle branch vs. naive main-only gap = +37.5 pp (p_adj = 4.8×10⁻⁴); PolyBench CWR gap = +8.8 pp (p_adj = 1.8×10⁻⁵); routing captures majority but not all headroom (CTF adapted 35.0% vs oracle 55.0%).
- **Evolution peaks early then degrades**: PolyBench peaks at cycle 22 of 51 (43% through stream); FutureX peaks at cycle 10 of 26 (38% through stream); static harness overfits to earlier stream evidence.
- **A-Evolve unbounded growth collapses**: grows from 12 to 34 skills and 2 KB to 68 KB prompt; all stopping budgets eventually peak and decline; later in stream shorter runs outperform longer ones.
- **Human-in-the-loop is surgical**: targeted finance/tech intervention yields +20 pp; broad/non-targeted slices show 0–5 pp; value depends on external signal injection relevance.
- **Coverage jump from evolution**: no-evolution Sonnet covers 32.6% of PolyBench markets; Full System covers 97.9%.
- **Token cost (Full System)**: PolyBench 233.2M input + 12.2M output tokens, 59.5 hours; CTF-Dojo 169.0M + 2.4M, 21.1 hours; FutureX 25.6M + 0.5M, 6.6 hours.

## Evolution + Adaptation Dual-Loss

**Regret decomposition (Proposition 1)**:

```
E_xt[Regret(φ, x_t)] = L_evo(Φ) + L_adapt(φ)
```

- **L_evo(Φ)** = E_xt[V(ℋ_t, x_t) − V(C*_Φ(x_t), x_t)]: evolution loss — structural ceiling from capabilities the evolver class cannot construct from history; independent of iteration count.
- **L_adapt(φ)** = E_xt[V(C*_Φ(x_t), x_t) − V(φ(ℋ_t), x_t)]: adaptation loss — gap from committing to one dense harness before observing task context; reducible via solve-time routing across specialized branches.

**How task shift is detected and handled**:

Three deployment dimensions expose static harness brittleness:

1. **(D1) Unbounded streams**: tasks arrive continuously; static harness overfits to earlier evidence. The system uses a stateful multi-agent evolver (Analyze→Research→Build→Verify phases) with a persistent cross-cycle workspace (task boards, research logs, architecture docs, verification tests). Temporal-reveal feedback gates outcome labels until task resolution to prevent leakage.

2. **(D2) Task heterogeneity**: the evolver constructs regime-specific branches stored in a git repository (e.g., `branch/crypto-classical`, `branch/sports`); at solve time a router agent selects the best-fit branch using a **routing confidence threshold of 0.7**. A single dense harness misfires: "news_from_future.md helps on a sports task yet misfires on a politics task."

3. **(D3) Distributional non-stationarity**: PolyBench exhibits drift — tradeable markets drop from 97% early to 31% late; near-even markets increase from 18% to 35%; market-price correctness slides 84%→77%. FutureX shows batch baseline accuracy ranging 20%–80% with Chinese-language tasks concentrated in later batches. A fixed prediction-market strategy becomes brittle.

**Why static auto-harness fails**: "A harness optimized for recent cycles therefore drifts out of fit for new tasks" as distributions shift. Repeatedly evolving a single dense harness causes overfitting to earlier stream evidence, reducing transfer to later tasks.

## Quantified Conditions

**Hyperparameters (Table 3)**:
- Solver temperature: 0.0; Evolver temperature: 0.0
- Solver max turns: 80; Evolver max tokens: 128k
- Research parallel agents: 3
- **Routing confidence threshold: 0.7**
- **EGL (Expected Gain in Learning) threshold: 0.05**
- **EGL window: 3 cycles**

**Benchmark batch/cycle configuration**:
| Benchmark | Tasks | Batch size | Evolution cycles |
|-----------|-------|-----------|-----------------|
| PolyBench | 5,075 | 100 | 51 |
| CTF-Dojo | 261 | 20 | 14 |
| FutureX | 503 | 20 | 26 |

**Peak performance timing (convergence signal)**:
- PolyBench: peak at cycle 22 of 51 (43% into stream)
- CTF-Dojo: continuous improvement through all 14 cycles (no decline detected)
- FutureX: peak at cycle 10 of 26 (38% into stream)

**Adaptation loss quantification (Table 11)**:
- CTF-Dojo L_adapt gap (oracle − naive): +37.5 pp [95% CI: oracle 40.0–70.0%, naive 7.5–30.0%], p_adj = 4.8×10⁻⁴
- PolyBench L_adapt gap: +8.8 pp CWR [oracle +2.1–+21.2%, naive −7.5–+13.0%], p_adj = 1.8×10⁻⁵
- FutureX L_adapt gap: +6.9 pp (not significant after correction; source-acquisition dominance binding)

**Seed harness (Table 4)** — starting from near-zero:
- PolyBench: 27 LOC prompt, 0 skills, 0 tools, 0 memory entries
- CTF-Dojo: 24 LOC prompt, 0 skills, 0 tools, 0 memory entries
- FutureX: 114 LOC prompt, 0 skills, 0 tools, 0 memory entries

**EGL threshold and window** (0.05 / 3 cycles) are the closest approximations to an adaptive-stop condition in the paper; they govern when evolution effort is redirected, but the paper does not explicitly define a universal convergence criterion — see Relevance section below.

## Relevance to The Loop (convergence / adaptive stop)

The paper provides the closest published quantified framing yet for The Loop's deferred "adaptive stop / convergence" open question. The EGL threshold (0.05) and EGL window (3 cycles) constitute a practical stop condition: if expected gain in learning falls below 0.05 over 3 consecutive cycles, evolution effort is redirected to a new branch rather than continuing to densify the current harness. This directly addresses `core.md §APPLY 自主迴圈`（原 `harness-loop.md`）'s deferred question of *when to stop evolving* — specifically, it proposes stopping not at a fixed iteration count but at a signal-based plateau threshold. The dual-loss decomposition (L_evo + L_adapt) also provides a principled diagnostic: if L_adapt dominates, the bottleneck is routing not evolution, and further evolution cycles waste compute. However, the EGL threshold values (0.05, window=3) are empirically chosen for streaming prediction-market and CTF contexts and are not derived from first principles — direct adoption into the harness-loop would require re-calibration to our task distribution. **Verdict**: this paper provides a **quantified** adaptive-stop mechanism (EGL 0.05/3-cycle); `has_quantified_adaptive_stop: true`, but threshold values are empirical and domain-specific.
