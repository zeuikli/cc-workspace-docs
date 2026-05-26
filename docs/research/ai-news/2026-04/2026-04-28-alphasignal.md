---
title: AlphaSignal — 2026-04-28
date: 2026-04-28
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-04-28

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [How DeepSeek-V4 Ships 1M-Token Context at 10% of Its Own KV Cache](https://alphasignalai.substack.com/p/how-deepseek-v4-ships-1m-token-context)
*📡 AlphaSignal | 2026-04-28*

1.6T-parameter MoE, MIT license, $3.48 per million output tokens

GPT-5.5 launched on April 23, 2026 at $5 input and $30 output per 1M tokens, OpenAI’s largest price hike in the 5.x series.

DeepSeek-V4 shipped 24 hours later under MIT license: V4-Pro at $1.74 input and $3.48 output per 1M tokens, V4-Flash at $0.14 and $0.28, both with a native 1M-token context window.

The mechanical story is a new hybrid attention architecture that cuts 1M-context inference FLOPs to 27% and KV cache to 10% of DeepSeek-V3.2.

Context

The release is authored by DeepSeek-AI and titled “DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence,” a preview launched on April 24, 2026.

The series has two variants: V4-Pro with 1.6T total parameters and 49B active per token, and V4-Flash with 284B total and 13B active. Weights are on Hugging Face under MIT. The API is live with OpenAI ChatCompletions and Anthropic Messages support via model IDs deepseek-v4-pro and deepseek-v4-flash.

Legacy deepseek-chat and deepseek-reasoner endpoints retire on July 24, 2026, and currently route to V4-Flash.

Technical architecture

Hybrid attention (CSA + HCA).

Compressed Sparse Attention compresses KV entries at a rate of 1/m and then applies DeepSeek Sparse Attention on the top-k surviving entries. Heavily Compressed Attention applies a larger compression rate 1/m’ (m’ ≫ m) with dense attention. The two are interleaved across the layer stack.

Manifold-Constrained Hyper-Connections (mHC).

The residual mapping matrix is projected onto the Birkhoff polytope of doubly stochastic matrices, bounding the spectral norm by 1 through deep stacks. This is the fix for the numerical instability that blocked earlier Hyper-Connections from scaling.

Muon optimizer plus FP4 quantization-aware training.

Muon replaces AdamW on the hidden layers. MoE expert weights train and store in FP4, everything else in FP8, which roughly halves the KV cache vs pure BF16.

Efficiency result.

At 1M tokens, V4-Pro runs at 27% of V3.2’s single-token FLOPs and 10% of the KV cache. V4-Flash hits 10% of FLOPs and 7% of KV cache. The KV cache drops to roughly 2% of a BF16 GQA8 baseline at 1M context.

Evidence

[Huggingface’s Table](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro#deepseek-v4-pro-max-vs-frontier-models:~:text=DeepSeek%2DV4%2DPro%2DMax%20vs%20Frontier%20Models) columns (Opus 4.6, GPT-5.4, Gemini 3.1 Pro, K2.6, GLM-5.1) share one harness. The GPT-5.5 and Opus 4.7 columns are self-reported from their own launch posts and are flagged below.

V4-Pro-Max leads coding on LiveCodeBench (93.5) and Codeforces rating (3206).

It ranks #1 open-weights on GDPval-AA per Artificial Analysis (Elo 1554, ahead of GLM-5.1 1535 and K2.6 1484).

It trails Opus 4.7 and Gemini 3.1 Pro on knowledge (MMLU-Pro, GPQA Diamond, HLE) and trails Opus 4.6 on long-context retrieval (MRCR 1M 92.9 vs 83.5).

Also, if you are a benchmark hater, we put some community tests for you at the end of the article.

Spec and price

V4-Pro output is 8.6× cheaper than GPT-5.5, 7.2× cheaper than Opus 4.7, and 4.3× cheaper than GPT-5.4

At 100M input plus 20M output tokens per day, V4-Pro runs at $243/day. GPT-5.5 at the same volume is $1,100/day. That is a $312,000/year gap on one deployment profile.

V4-Flash

Flash matches Pro on most reasoning benchmarks when given Max-mode thinking budget: LiveCodeBench 91.6 (vs Pro 93.5), SWE-Verified 79.0 (vs 80.6), MRCR 1M 78.7 (vs 83.5). At $0.14 input and $0.28 output, Flash runs a frontier-tier agent for half the old V3 price.

Flash drops off on pure knowledge (MMLU-Pro 86.2 vs Pro 87.5, SimpleQA-Verified 34.1 vs 57.9) and on the hardest agent tasks (Terminal-Bench 2.0 56.9 vs 67.9). If the workload is knowledge-heavy or agent-heavy, stay on Pro.

Limitations

Trails frontier on knowledge.

Gemini 3.1 Pro leads MMLU-Pro (91.0 vs V4-Pro-Max 87.5), GPQA Diamond (94.3 vs 90.1), and HLE no tools (44.4 vs 37.7). Opus 4.7 leads HLE no tools at 46.9. The tech report concedes a developmental gap of “approximately 3 to 6 months” vs frontier closed models on reasoning-heavy benchmarks.

Long-context retrieval gap vs Claude.

Opus 4.6 scores 92.9 MMR on MRCR 1M, V4-Pro scores 83.5, a 9.4-point gap on needle-in-haystack at 1M context. V4-Pro still leads Gemini 3.1 Pro (76.3) and wins CorpusQA 1M over Gemini by 8.2 points.

No multimodal.

V4 is text-only at preview. The tech report lists “incorporating multimodal capabilities” as a future direction. Closed frontiers have been multimodal for multiple releases.

Hardware bar is real.

V4-Pro is 862GB on disk with FP4 MoE weights and FP8 everywhere else. Self-hosting requires multi-H100 or Huawei Ascend clusters. V4-Flash is 158GB, still a multi-GPU deployment.

Preview, not final.

DeepSeek calls this a preview where “final iterations may incorporate feedback.” An internal survey of 85 DeepSeek engineers using V4-Pro daily reports trivial mistakes, misinterpretation of vague prompts, and occasional over-thinking.

So the best recommendation is to adopt V4 for coding and long-context agent workloads, and wait for the final release before migrating knowledge-heavy pipelines. The coding and cost case closes cleanly today, the knowledge gap does not.

Who benefits and who doesn’t

V4 fits teams running high-volume coding agents, codebase-wide retrieval, or long-horizon agent loops, cost-sensitive teams currently paying GPT-5.4 or Opus 4.6 rates, and self-hosters with multi-GPU or Huawei Ascend capacity.

It does not fit teams needing multimodal inputs, teams that require MMLU-Pro or HLE leadership, and small shops without the cluster hardware to self-host at FP4 precision.

Practitioner implication

You can now run a 1M-token coding agent at frontier-class quality for $243/day instead of $1,100/day now that an open-weights MoE ships sub-10% KV cache at long context.

AlphaSignal Take

V4 is the first open-weights model that closes the cost gap with closed frontier labs on coding and agent workloads without losing structural performance. The 27% FLOPs and 10% KV-cache numbers at 1M context are the reason the price can sit at $3.48 output. 

The knowledge gap and the multimodal gap are real and will likely close in the V4 final release, which the tech report frames as the iteration that follows user feedback on the preview. For coding and agent teams, the adopt decision is today. For knowledge-heavy pipelines, the decision is the GA window.

Links

[DeepSeek-V4-Pro model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

(HuggingFace, weights + card, ~10 min)

[DeepSeek-V4 tech report](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf)

(PDF, ~45 min read)

[DeepSeek V4 Preview Release notes](https://api-docs.deepseek.com/news/news260424)

(API docs, ~2 min)

[API Calling](https://api-docs.deepseek.com/)

(API docs, ~1 min)

Follow [@AlphaSignalAI](https://x.com/@AlphaSignalAI) for more content like this.

Check out [AlphaSignal.ai](http://alphasignal.ai/) to get a daily summary of top models, repos, and papers in AI. Read by 280,000+ devs.

Questions?

Q: How does DeepSeek V4 pricing compare to GPT-5.5 and Claude Opus 4.7? A: V4-Pro is $1.74 input / $3.48 output per 1M tokens. GPT-5.5 is $5 / $30, Opus 4.7 is $5 / $25. V4-Pro output is 8.6× cheaper than GPT-5.5 and 7.2× cheaper than Opus 4.7. V4-Flash is $0.14 / $0.28, an order of magnitude below V4-Pro.

Q: What is the difference between V4-Pro and V4-Flash? A: V4-Pro has 1.6T total parameters with 49B active per token. V4-Flash has 284B total with 13B active. Both run 1M-token native context. Flash trails Pro on knowledge tasks and hardest agent tasks but matches Pro on most reasoning benchmarks when given Max-mode thinking budget.

Q: How does V4’s 1M context window work efficiently? A: Two attention mechanisms, CSA and HCA, compress KV entries before attention is applied. CSA compresses at 1/m and then runs DeepSeek Sparse Attention on top-k entries. HCA compresses at 1/m’ (m’ ≫ m) with dense attention. The interleaved architecture plus FP8 KV storage drops KV cache to roughly 2% of a BF16 GQA8 baseline at 1M context.

Q: What hardware is required to self-host DeepSeek V4? A: V4-Pro is 862GB on disk with FP4 MoE weights, requiring a multi-H100 or Huawei Ascend cluster. V4-Flash is 158GB, still a multi-GPU deployment. vLLM has day-0 support for both.

Q: Is V4 competitive with GPT-5.4 on coding benchmarks? A: On DeepSeek’s harness, V4-Pro-Max beats GPT-5.4 on Codeforces rating (3206 vs 3168) and ranks ahead of GPT-5.4 on LiveCodeBench. V4-Pro is the first open-weights model to match a closed frontier model on Codeforces per the paper.

Check out [AlphaSignal.ai](http://alphasignal.ai/) to get a daily summary of top models, repos, and papers in AI.

---
