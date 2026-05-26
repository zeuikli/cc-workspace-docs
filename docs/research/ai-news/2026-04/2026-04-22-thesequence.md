---
title: TheSequence — 2026-04-22
date: 2026-04-22
source: TheSequence
type: ai-news
---

# 🔢 TheSequence — 2026-04-22

> 165k+ 訂閱；ML / 企業 AI 應用週報，Jesus Rodriguez 主筆
> 來源：[TheSequence](https://thesequence.substack.com/feed)

---

## [The Sequence AI of the Week #847: Everything You Need to Know About Claude Opus 4.7](https://thesequence.substack.com/p/the-sequence-ai-of-the-week-847-everything)
*🔢 TheSequence | 2026-04-22*

Claude Opus 4.7 shipped last week. The benchmarks are what you’d expect from a two-month incremental release — SWE-bench Verified 87.6%, SWE-bench Pro 64.3%, MCP-Atlas +14.6pp, state-of-the-art on GDPval-AA for economically valuable knowledge work, XBOW visual-acuity 54.5% → 98.5%, finance and document reasoning up, BrowseComp and long-context multi-needle retrieval down. Fine. Worth skimming. But the raw numbers undersell what actually changed.

The easier way in is to look at what got removed from the API, because the release is as much about the contract between you and the model as it is about the weights.

If you migrate a 4.6 harness to 4.7 and it still sets temperature, top_p, top_k, or thinking.budget_tokens, you get a 400. Not deprecated with a warning — gone. The only supported thinking mode is adaptive. In their place: an effort enum (low, medium, high, xhigh, max) and task_budget, a soft token ceiling the model can actually see. Every one of the removed parameters was a sampling-level control — you were reaching into the decoding loop and fiddling with token probabilities. What replaces them are semantic controls. You’re no longer tuning the softmax; you’re telling the model how hard to think and how much runway it has.

That’s basically the release in one sentence. The inference-time interface has shifted from stochastic sampling knobs to self-paced budgets, and the model has been trained to sit inside that interface responsibly. Everything else — self-verification, the literal instruction following, 1:1 pixel mapping, file-system memory, differential capability shaping — is downstream of this posture. Let me walk through what the new contract actually buys you.

Self-verification as a trained behavior, not a prompt trick

[
Read more
](https://thesequence.substack.com/p/the-sequence-ai-of-the-week-847-everything)

---
