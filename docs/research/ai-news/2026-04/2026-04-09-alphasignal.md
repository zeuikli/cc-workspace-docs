---
title: AlphaSignal — 2026-04-09
date: 2026-04-09
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-04-09

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [Why Gemma 4 Could Be a Turning Point for Open-Source AI](https://alphasignalai.substack.com/p/why-gemma-4-could-be-a-turning-point)
*📡 AlphaSignal | 2026-04-09*

For most of 2024 and 2025, if you asked me which open models were worth deploying, I’d have said DeepSeek or Qwen without thinking twice. Google’s Gemma line was fine. Decent for research, okay for Kaggle notebooks, but nobody I knew was building production systems on it. 

The Chinese labs were eating Google’s lunch in open source.

[Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) is the latest open weight model family from Google DeepMind, derived from the same research that powers Gemini 3, their closed-source flagship.

Google released four variants, sized for everything between a Raspberry Pi and a data center GPU:

E2B (Effective 2B parameters): A tiny model designed for phones, Raspberry Pi, and Jetson Nano. It has 5.1B total parameters but only 2.3B are “effective,” meaning that’s what actually computes during inference.

E4B (Effective 4B parameters): A step up from E2B, still small enough for on-device deployment.

26B MoE (Mixture of Experts, 4B active): This one has 25.2B total parameters but only routes through 3.8B at inference time. It’s nearly as fast as a 4B model but performs like something much larger.

31B Dense: The big one. Currently [sitting at number three](https://lmarena.ai/) on the Arena AI open model leaderboard.

Every variant handles images and video natively. The two edge models (E2B and E4B) also process audio directly on device, so you can do speech recognition without shipping anything to the cloud.

Context windows run from 128K tokens on the edge models to 256K on the larger ones. At 256K tokens, you’re looking at feeding an entire mid-sized codebase into a single prompt.

The benchmarks

I pulled these from the [official Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4). All numbers below are for the instruction-tuned versions.

Text benchmarks

The math gains are the most dramatic. On AIME 2026, a competition-level math benchmark, the 31B scores 89.2%. Its predecessor, Gemma 3 27B, scored 20.8% on the same test. I want to sit with that for a second: the previous generation got roughly one in five competition math problems right. This one gets nine out of ten.

Coding saw a similar jump. Gemma 3 had a Codeforces ELO of 110. Gemma 4’s 31B sits at 2150, which puts it in Grandmaster territory. LiveCodeBench v6 went from 29.1% to 80.0%.

On GPQA Diamond, which asks PhD-level science questions that stump most human experts (they average around 65%), the 31B scores 84.3%.

The MoE variant might actually be the more interesting model to watch. With only 3.8B parameters active per token, it pulls 82.3% on GPQA Diamond. You’re getting close to the 31B’s quality at a fraction of the compute cost.

Vision benchmarks

Vision is where Gemma 4 quietly punches above its weight. The 31B pulls 76.9% on MMMU Pro, up from 49.7% on Gemma 3. MATH-Vision, which tests whether a model can actually solve math problems presented as images rather than text, came in at 85.6%, nearly double Gemma 3's 46.0%. 

On the document understanding side, OmniDocBench error rates dropped by roughly two-thirds compared to the previous generation, which matters if you're parsing invoices, receipts, or scanned technical docs.

Long context benchmarks

Long context was a weak spot for Gemma 3, and the improvement here is hard to ignore. MRCR v2 at 128K tokens, which measures whether a model can actually retrieve and reason over information buried deep in a long document, went from 13.5% on Gemma 3 to 66.4% on the Gemma 4 31B. 

That's still not perfect, and long context retrieval remains hard for models at this scale, but going from "basically useless" to "functional" in one generation is a meaningful step.

The MoE variant might actually be the more interesting model to watch. With only 3.8B parameters active per token, it pulls 82.3% on GPQA Diamond. You're getting close to the 31B's quality at a fraction of the compute cost.

How Gemma 4 compares to other models

Benchmarks in a vacuum are marketing material. What matters is how Gemma 4 holds up against the models people actually pay for: Claude Opus 4.6, GPT-5.2, and the open weight heavyweight [Kimi K2.5](https://ai.rs/ai-developer/gemma-4-vs-qwen-3-5-vs-llama-4-compared).

Fair warning: this comparison is inherently lopsided. Gemma 4 31B has 31 billion parameters. Claude Opus 4.6 and GPT-5.2 don’t disclose theirs, but we’re almost certainly talking hundreds of billions. Kimi K2.5 has 1 trillion total with 32B active. Gemma 4 shouldn’t be competitive here, and the fact that it partially is tells the story.

GPQA Diamond (PhD-Level Science)

PhD-level science reasoning (GPQA Diamond): Gemma 4 31B lands at 84.3%. Claude Opus 4.6 scores 91.3%, GPT-5.2 hits 92.4%. That’s a real gap of 7 to 8 points, and I’m not going to pretend otherwise. But consider this: Gemma 4 outscores Claude Sonnet 4.6 (74.1%) by over 10 points. A lot of developers use Sonnet as their daily driver. A free, locally-runnable model just beat it on PhD-level science.

AIME (Math)

Competition math (AIME 2026): 89.2% for the 31B. GPT-5.2 and Claude Opus 4.6 are near-perfect, but they’re throwing massively more compute at the problem. Kimi K2.5 gets 95.8% while requiring 1 trillion total parameters.

MMLU Pro (Knowledge)

Graduate-level knowledge (MMLU Pro): 85.2% for the 31B. This is the benchmark where Gemma 4 gets closest to the giants. Kimi K2.5 scores 87.1% with 30x more total parameters. Claude Opus 4.6 reportedly comes in around 82%, which would actually put it below Gemma 4.

SWE-Bench & LiveCodeBench (Coding)

Coding (LiveCodeBench v6): 80.0% with a Codeforces ELO of 2150. That’s the same ballpark as Kimi K2.5, a model with 32x more total parameters.

Multimodal reasoning (MMMU Pro): Gemma 4 31B matches Claude Sonnet 4.6 almost exactly, which is wild for a 31B open model going up against a proprietary system.

The intelligence-per-parameter story

The 26B MoE uses 3.8 billion active parameters per token. That’s a small model’s compute budget. It scores 82.3% on GPQA Diamond and 82.6% on MMLU Pro.

Kimi K2.5 activates 32B parameters per token out of 1 trillion total. It scores about 5 points higher on both benchmarks, but it’s activating 8x more parameters every single inference step and requires dramatically more storage.

I want to be clear: Gemma 4 does not beat Claude Opus 4.6 or GPT-5.2 on raw scores. If someone tells you it does, they’re cherry-picking or lying. The frontier proprietary models are still ahead, and they probably will be for a while.

But “best model on earth” isn’t the question most developers are asking. The question is: what’s the best model I can actually own? Run on my hardware, no API bills, no data leaving my network, no license that might change next quarter?

Gemma 4 makes a strong case for itself. You give up 7 to 8 points on GPQA Diamond versus the absolute best. In return, you pay nothing per inference, forever. For a lot of use cases, that math works out.

Apache 2.0 changes everything

This is the part of the release that might matter more than the benchmarks.

Every previous Gemma model shipped under Google’s custom Gemma license. It was relatively permissive, but it was Google’s license, with Google’s terms, and Google’s ability to interpret those terms however they wanted. Enterprises and their legal teams were cautious about it.

[Gemma 4 ships under Apache 2.0](https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html). Same license as Kubernetes, TensorFlow, Apache Spark. This is a known quantity. Every corporate legal department on the planet has already approved Apache 2.0 for use.

Hugging Face co-founder Clement Delangue [described it as](https://opendatascience.com/gemma-4-sets-a-new-standard-for-open-ai-models/) “a huge milestone.” 

No usage caps, no reporting obligations, unrestricted commercial deployment. You can fork it, fine-tune it on proprietary data, and ship the result as a product without asking anyone’s permission.

Google’s own framing: they want developers building “freely and confidently from the ground up without the need to navigate prescriptive terms of service.” If you’ve been nervous about putting a custom-licensed model at the core of a product, that sentence is aimed directly at you.

Running Gemma 4 locally

If you want to try Gemma 4 on your own machine, here’s what you need.

Start by getting the latest llama.cpp:

brew upgrade llama.cpp
# or install from HEAD if the latest build isn't available yet:
brew install llama.cpp --HEAD

Got a standard MacBook or laptop with 16GB RAM?

llama-server -hf ggml-org/gemma-4-E4B-it-GGUF:Q8_0

MacBook Pro or RTX 3090 with 24GB or more?

llama-server -hf ggml-org/gemma-4-26B-A4B-it-GGUF:Q4_K_M

RTX 5090 or similar with 32GB VRAM?

llama-server -hf ggml-org/gemma-4-26B-A4B-it-GGUF:Q8_0

The full 31B dense model needs about 80GB unquantized, so an H100 handles it directly. Quantized versions bring it down to consumer hardware territory. The ecosystem showed up on launch day: [Hugging Face Transformers](https://huggingface.co/collections/google/gemma-4), vLLM, llama.cpp, MLX, Ollama, LM Studio, Unsloth, SGLang, and NVIDIA NIM all have support.

A lot of users on X have shared their setup and this one was able to run the 26B on his M1 MacBook with 13GB memory.

Running it on Your Phone

Google has an [AI Edge Gallery](https://github.com/google-ai-edge/gallery) app for Android and iOS that downloads and runs Gemma 4 models entirely on device.

Link: https://apps.apple.com/us/app/google-ai-edge-gallery/id6749645337

No cloud, no API key, no internet connection after the initial download.

The E2B model needs less than 1.5GB of memory thanks to LiteRT’s support for 2-bit and 4-bit weights, so it fits comfortably on most phones made in the last few years. 

The E4B is the sweet spot if you have 8GB of RAM or more. Both handle text, images, and audio natively, so you can do things like speech recognition and image analysis without anything leaving your device.

One catch: the AI Edge Gallery isn’t on the Play Store yet. You have to grab the APK from [Google’s GitHub releases page](https://github.com/google-ai-edge/gallery/releases) and sideload it. Android 10 or later is required. The first model load takes 10 to 30 seconds depending on your device, and the first response in a session tends to be slow while the model warms up.

If you'd rather use something you already know, Ollama has [Gemma 4 support](https://ollama.com/library/gemma4) on desktop. You can't run Ollama natively on a phone, but apps like PocketPal or Enchanted let you connect to an Ollama instance running on your home network, so your laptop does the inference and your phone is the interface.

Any developer can ship an app with Gemma 4 E2B baked in. No usage fees, no terms of service negotiation, no dependency on someone else's servers staying online.

So, is Gemma 4 the best open model? 

Right now, it’s not ranked as #1 on Arena AI, so no. But Gemma 4 is the first time I’ve looked at a Google open model and thought: yeah, I’d actually build on this.

The 26B MoE in particular has me rethinking what’s possible on local hardware. 3.8 billion active parameters, 82% on GPQA Diamond. That number sticks with me. If you’re working on anything related to local inference or on-device AI, give it a serious look.

What do you think?

Join 250k+ developers staying ahead in AI. We curate the latest models, repos, and research — so you don’t miss what matters: [AlphaSignal.ai](http://alphasignal.ai/)

---
