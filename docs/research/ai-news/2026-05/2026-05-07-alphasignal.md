---
title: AlphaSignal — 2026-05-07
date: 2026-05-07
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-05-07

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [How HeavySkill Turns Agentic Harness Tricks Into a One-File Inner Skill](https://alphasignalai.substack.com/p/how-heavyskill-turns-agentic-harness)
*📡 AlphaSignal | 2026-05-07*

Meituan‘s LongCat team argues the heavy-thinking patterns inside Claude Code, Codex, and Kimi K2 are one skill in disguise, not separate orchestration tricks.

Once that skill is isolated, the orchestrator stops mattering as much. The model can run the protocol on its own.

The headline: R1-Distill-Qwen3-8B goes from 35.7% to 69.3% on IFEval after one deliberation pass over 8 parallel trajectories, and is usable with any model.

The practitioner move: copy skill/heavyskill.md into ~/.claude/skills/ and the protocol activates inside Claude Code with no Python pipeline.

“Checkout our [Harness Engineering workshop](https://luma.com/t24o902x). more details at the end.”

Context

The paper is authored by Meituan‘s LongCat team and titled “HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness.” It posted to arXiv on May 4, 2026 (ID 2605.02396, 18 pages, 10 figures).

The team has shipped variations of this pattern before in LongCat-Flash and LongCat-Flash-Thinking-2601. HeavySkill is the formalization: a portable, harness-agnostic protocol with a published skill file and a Python pipeline.

The gap it closes: most agentic-harness papers measure end-to-end accuracy without isolating which component drives the gain. HeavySkill argues the gain comes from one specific two-stage skill, not orchestrator complexity.

How it works (technically)

“Want to skip the mechanics? Jump to How to use it below.”

Stage 1: Parallel Reasoning. Generate K independent reasoning trajectories (K is the parallel-trajectory count, default 8 or 16) at temperature=1.0, top_p=0.95, top_k=10, with a max of 32,768 tokens per trajectory. Each trajectory solves the query from scratch with no awareness of the others, so the K outputs spread across different solution strategies rather than collapsing onto one. The high temperature is the diversity dial.

The serialized memory cache. The K trajectories rarely fit into a single context window, so the protocol writes them into a “case file” that Stage 2 reads. The cache prunes long trajectories down to a max-length budget (default 80,000 tokens total), shuffles their order to remove positional bias, and packages them with a structured prompt frame.

When more than K trajectories are available (the paper pre-generates 256 per query for ablation analysis), four selection strategies decide which trajectories enter the cache: Random, Max-Answer-Num (consensus-based), Max-Diversity, and Max-Length.

Stage 2: Sequential Deliberation. A second model pass reads the serialized cache and produces 4 deliberated outputs at temperature=0.7. The deliberation prompt instructs the model not to follow majority consensus blindly, to re-derive an answer if all thinkers appear wrong, and to maintain the domain-specific output format (e.g., \boxed{} for math).

The same model can serve both stages, or a separate deliberation model can. The paper finds deliberation depends on synthesis ability, not peak reasoning power: even Qwen2.5-32B-Instruct (a weaker reasoner) yields gains in the deliberation role.

Iterative deliberation (optional). The protocol supports running Stage 2 multiple times, each round taking the previous deliberated outputs as the new cache. Default is N=1 (no iteration), with N=4 supported. The mechanism is a refinement loop: HM@K rises with each round, but HP@K decays from accumulated noise, so iteration depth becomes a tunable trade-off.

Two execution modes. The paper publishes the protocol in two forms.

- Workflow mode runs an external Python pipeline that orchestrates the API calls, manages the cache, and routes outputs between stages.

- Skill mode lets the LLM orchestrator read heavyskill.md and self-execute, spawning thinkers and deliberating in-context with no glue code. Skill mode works because the orchestrator is a frontier model with strong in-context-learning capability.

Repo snapshot

Evidence

The headline numbers from Table 2 of the paper:

M@K is the average accuracy of K raw single-pass trajectories with no deliberation. HM@4 is the average accuracy across the 4 deliberation outputs and matches what a user gets per query. HP@4 is the fraction of queries where at least one of the 4 deliberation outputs is correct, an upper bound that requires picking the right one.

Deliberation can synthesize answers that no single trajectory contained. On multiple benchmarks HP@4 exceeds Pass@K (the same “≥1 correct” measure on the raw trajectories before deliberation), meaning the deliberation step generates correct solutions not present in any of the K parallel trajectories.

Pass-rate analysis on 10k queries (R1-Distill-Qwen-7B): roughly 500 low-pass queries were rectified by deliberation, only ~30 high-pass queries regressed. Downside risk is small.

Appendix B fine-tunes the protocol via RLVR (reinforcement learning with verifiable rewards, where the reward is the answer’s correctness against ground truth). HM@4 climbs ~10 percentage points in the first 100 training steps at K=8. K=16 collapses past 100 steps from entropy decay.

How to get started

Mode 1: Skill drop-in for Claude Code.

Copy heavyskill.md into ~/.claude/skills/:

The skill file has four parts: activation conditions (when to fire heavy thinking versus a single-pass answer), parallel reasoning protocol, deliberation prompt template, and output constraints. Claude Code reads it as in-context instructions and self-orchestrates the protocol.

Mode 2: Python workflow against any OpenAI-compatible API.

Three flags worth knowing:

--reason_k: parallel trajectories (default 8).

--summary_k: deliberation outputs (default 4).

--iterations: deliberation rounds (default 1). HM@K rises with iterations, HP@K decays, so keep this at 1 unless you have measured the trade-off on your data.

Memory cache strategy. The Python workflow ships four trajectory selection strategies for the deliberation cache. Authors found Max-Answer-Num (consensus-based) wins, Random and Max-Diversity tie mid-tier, and Max-Length is worst. Default to Max-Answer-Num.

API compatibility per the README: vLLM, DeepSeek, Together AI, OpenRouter, Ollama.

Current limitations

Compute scales linearly in K. K=8 means roughly 8× the Stage 1 token cost plus 4 deliberation passes. The paper offers no token-budget comparison against single-trajectory inference at matched cost.

Marginal gains on preference tasks. Arena-Hard improvements were marginal or slightly negative across most tested models. Heavy thinking helps when correctness is verifiable, not when stylistic preference matters.

No fine-tuned checkpoints released. The repo ships the skill file and the workflow code, but the RLVR-trained weights from Appendix B are not on Hugging Face. Practitioners get the protocol, not a ready-made model.

RLVR training unstable at K=16. Entropy collapse after 100 steps. K=8 is the practical training ceiling per the authors’ own ablation.

No independent replications yet. The paper is two days old as of this writing. All numbers come from the authors. Reproduction is feasible but unverified.

Observability trade-off. Skill mode hides deliberation inside the model. Workflow mode exposes the trajectories and the cache. Teams that need traceable reasoning chains should default to workflow mode.

So the best recommendation is to adopt skill mode for correctness-critical workloads (math, code, instruction following) and skip it for preference-driven chat where the compute multiplier does not earn its keep yet.

AlphaSignal Take

Worth Watching.

The protocol is real and runnable today via the skill file. The contested claim is whether internalizing this skill via RLVR holds at scale. The authors’ own runs collapse at K=16, and no independent replications exist yet.

Maintenance health: 7 commits, two-day-old repo, single maintainer (wjn1996), Apache-2.0. Acceptable for prototyping, not yet a production dependency.

What would change the verdict: a Qwen team or DeepSeek release that ships heavy thinking baked into the weights moves this to Production Ready. A failed independent replication moves it to Skip.

If Qwen3.6 / Gemma4 ships with heavy-thinking-style RL post-training, the skill file becomes redundant. The model runs the protocol natively. That is the trajectory worth tracking, not this specific repo.

Who benefits

Engineers running Claude Code or compatible harnesses on correctness-verifiable workloads (math, code, instruction following), teams self-hosting Qwen3 or R1-Distill checkpoints with spare compute headroom for K=8 inference, and researchers studying width-vs-depth test-time scaling.

Who should skip

Teams whose workloads are preference-driven (open-ended chat, creative writing), production systems with strict latency budgets that cannot absorb 8× the Stage 1 cost, and teams that need traceable per-step reasoning logs, since skill mode hides deliberation inside the model.

Practitioner implication

Engineers can now activate parallel reasoning plus deliberation inside Claude Code with one file copy, now that the protocol has been distilled into a portable skill that runs against any OpenAI-compatible API.

Workshop

We’re hosting a session on Harness Engineering to move beyond simple prompts and context. It’s about building the constraints that let agents work autonomously.

May 14th, 11am PT. Led by AJ Joobandi (Augment Code). 30 seats, $150.

You’ll learn why agents break, how to design robust success metrics, and walk away with a plug-and-play harness file.

→ Grab your seat [here](https://lu.ma/t24o902x), +20 already going..

Links

[HeavySkill paper (arXiv 2605.02396)](https://arxiv.org/abs/2605.02396) (paper, ~25 min read)

[HeavySkill GitHub](https://github.com/wjn1996/HeavySkill) (repo, ~5 min setup for skill mode)

[Hugging Face Papers entry](https://huggingface.co/papers/2605.02396) (page, ~2 min)

Follow [@AlphaSignalAI](https://x.com/AlphaSignalAI) for more content like this.

Subscribe at [AlphaSignal.ai](https://alphasignal.ai/) for daily AI signals. Read by 280,000+ developers.

Questions?

What does heavy thinking actually do? It generates K independent reasoning trajectories at high temperature, then runs a second model pass that critically synthesizes them into a final answer. The pattern is parallel exploration followed by sequential deliberation.

Do I need to fine-tune a model to use HeavySkill? No. Skill mode and workflow mode both work against any OpenAI-compatible endpoint (vLLM, DeepSeek, OpenRouter, Ollama). Appendix B fine-tunes a small model with RLVR for a ~10 point HM@4 gain, but those weights are not released.

How much extra compute does it cost? Linear in K, the number of parallel trajectories. K=8 means 8× the Stage 1 token cost plus 4 deliberation passes. Activate only on correctness-critical queries.

How is HeavySkill different from majority voting? Deliberation can elevate a minority-correct trajectory and synthesize answers absent from every single trajectory. Majority voting can only pick the most common existing answer, never generate a new one.

What’s the catch? Compute cost scales with K, gains are marginal on preference-oriented tasks like Arena-Hard, and no independent replications exist yet.

---
