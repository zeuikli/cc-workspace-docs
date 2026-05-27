---
title: "AlphaSignal — 2026-04-24"
date: 2026-04-24
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-04-24

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [Bonsai 8B: The 1-Bit LLM That Fits in 1 GB](https://alphasignalai.substack.com/p/bonsai-8b-the-1-bit-llm-that-fits)
*📡 AlphaSignal | 2026-04-24*

A week ago, [PrismML](https://prismml.com/) pushed out something that made me stop and re-read the specs twice. An [8-billion parameter](https://x.com/PrismML/status/2044833023682896134) large language model that fits in 1.15 GB of memory. Every weight in the network is a single bit. And on an iPhone 17 Pro Max, it generates at 44 tokens per second.

If you’ve been tracking 1-bit LLM research since Microsoft’s [BitNet papers](https://www.microsoft.com/en-us/research/publication/bitnet-scaling-1-bit-transformers-for-large-language-models/), the concept isn’t new. What’s new is that PrismML claims to have the first commercially viable version.

Their model, [Bonsai 8B](https://prismml.com/news/bonsai-8b), is open source under Apache 2.0, already runs on consumer hardware, and posts benchmark numbers that would have looked impossible for a 1 GB model two years ago.

I tested it myself and here’s what I found.

What Makes Bonsai Different From Regular Quantized Models

Most small models you’ve seen use post-training quantization. You take an FP16 model, compress it down to 4-bit or 2-bit, and accept some quality loss as the tradeoff. The weights are approximated versions of what the model actually learned.

Bonsai 8B doesn’t do that.

PrismML trained the entire 8.2 billion parameter network natively at 1-bit precision, from scratch. No higher-precision escape hatches, no mixed-precision trickery. The embeddings, attention layers, MLP layers, and the language model head are all 1-bit, end to end.

Every weight is either +1 or -1. That’s the whole vocabulary.

This matters because post-training quantization always leaves capability on the table. The model was never optimized for 1-bit weights, so forcing it into that space hurts accuracy. When you train with 1-bit constraints from the beginning, the network learns representations that actually fit the constraint.

It’s a similar idea to what Microsoft proved with [BitNet b1.58](https://github.com/microsoft/BitNet), but pushed to real 8B scale and a true single-bit target instead of ternary weights.

You can read Bonsai 8B [whitepaper here](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/1-bit-bonsai-8b-whitepaper.pdf).

How I Benchmarked It

To see how Bonsai compares to other models of similar size, I lined it up against four 8B-class models I use regularly and ran the same evaluation suite across all of them. The lineup:

Bonsai 8B at 1.15 GB, the 1-bit challenger

Llama 3.1 8B from Meta at 16.07 GB in FP16

Qwen 3 8B from Alibaba at 16.38 GB

LFM2 8B from Liquid AI at 16.07 GB

Ministral 3 8B from Mistral at roughly 16 GB

Six benchmarks covered the full capability surface I care about:

IFEval for instruction following

GSM8K for math reasoning

HumanEval+ for coding

BFCL for function calling

MuSR for multi-step reasoning

MMLU-Redux for general knowledge.

Same prompts, same decoding parameters, same hardware for every model.

The Results

Here’s how the five models compared:

The 70.5 average on a 1.15 GB model is the most interesting part. That’s 14x less memory than everything else in this table.

Bonsai beats Llama 3.1 8B by 3.3 points and edges past LFM2 8B. It ties Ministral 3 8B within margin of error. Qwen 3 8B remains the king of raw accuracy at 79.4, but it pays for that with more than 14x the RAM.

The GSM8K result caught me off guard. 88.2 on grade-school math word problems, ahead of Llama 3.1’s 76.9 and LFM2’s 85.2, and within striking distance of Qwen’s 91.4. A 1-bit model scoring that high on arithmetic reasoning pushes back on a lot of the standard assumptions about precision and model capability.

Intelligence Density as a Metric

PrismML introduced a metric they call intelligence density. The formal definition is the negative log of the model’s average error rate divided by model size in GB, but the practical version is: how much capability you get per gigabyte.

Bonsai 8B scores 1.058 on this scale. Qwen 3 8B, its closest competitor by parameter count, scores 0.099. That’s roughly a 10.8x gap.

The metric definitely favors smaller models, and you could argue it’s designed to flatter Bonsai. Fair enough. But the size of the gap is hard to dismiss. No other 8B model is anywhere near this ratio of capability to disk size.

Where Bonsai Falls Short

Coding is the obvious weakness. Bonsai scores 58.1 on HumanEval+ while Qwen 3 8B hits 80.1, a 22-point gap. In my own testing, Bonsai’s Python output was often close to correct but rarely ran cleanly on the first try. If your workflow depends on code generation, this isn’t the model for you.

Developers on r/LocalLLaMA have reported two other issues worth knowing about. Bonsai struggles with complex structured output, especially nested JSON schemas, and it hallucinates factual details more often than larger models do. Neither is unusual for a 1 GB checkpoint, but both are worth testing against your own use case before committing to it.

Multi-step reasoning at 64.1 on MuSR is decent but still trails Qwen’s 70.2. Long reasoning chains appear to hit the 1-bit precision ceiling before simpler tasks do.

Where to Try Bonsai 8B

Getting Bonsai running locally takes about five minutes.

The official [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) repo has a single setup script that handles everything on macOS, Linux, and Windows.

git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo
export BONSAI_MODEL=8B
./setup.sh

The script installs dependencies, pulls the model from Hugging Face, and drops you into a working local chat server on port 8080.

If you want to build from the llama.cpp fork directly, the team maintains [PrismML-Eng/llama.cpp](https://github.com/PrismML-Eng/llama.cpp) with pre-built binaries for macOS Apple Silicon, Linux CUDA (12.4, 12.8, 13.1), and Windows CUDA. Model weights are on [Hugging Face](https://huggingface.co/collections/prism-ml/bonsai) in both GGUF and MLX formats.

On iOS, the easiest path is the [Locally AI app](https://apps.apple.com/us/app/locally-ai-local-ai-chat/id6741426692), which lets you run Bonsai natively on iPhone and iPad via MLX Swift. This is the setup PrismML used to demo the 44 tokens per second number.

I tested on an M3 MacBook Pro using the MLX build. Load time was under two seconds. Short-prompt generation sat around 120 tokens per second. The 65,536 token context window held up fine on long documents.

Why This Actually Matters

A 1.15 GB model changes what hardware can run a capable 8B LLM. Mid-range Android phones, a Raspberry Pi 5, embedded Linux boards, and laptops without dedicated GPUs are all now fair game. The KV cache still grows with context length, but even at the full 65K tokens the total memory footprint stays around 10 GB, which is workable on most consumer hardware.

Energy use drops too. PrismML reports 4–5x better efficiency than a 16-bit 8B model, with the iPhone 17 Pro Max hitting 0.068 mWh per token. For agentic workloads that run continuously, that means longer battery life and lower operating cost.

PrismML also released [Bonsai 4B](https://huggingface.co/prism-ml/Bonsai-4B-gguf) and [Bonsai 1.7B](https://huggingface.co/prism-ml/Bonsai-1.7B-gguf) variants. I haven’t tested those yet, but a 1-bit 1.7B model could plausibly run on hardware as small as a Raspberry Pi Zero 2W or a smartwatch. That’s a different conversation than the one we’ve been having about local LLMs for the past two years.

For AI product architecture, if an 8B model fits in a gigabyte and runs on a phone, many products that currently route every request to OpenAI or Anthropic could run entirely on the client. Cheaper for the developer, faster for the user, and better for privacy. Whether that future shows up depends on whether the 1-bit training approach scales to 30B and 70B models, which PrismML has hinted is on their roadmap.

What do you think about 1-bit LLMs as a category? Drop your thoughts in the comments.

Follow [@AlphaSignalAI](https://x.com/@AlphaSignalAI) for more content like this.

---
