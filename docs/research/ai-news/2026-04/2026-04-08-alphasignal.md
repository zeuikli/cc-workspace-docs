---
title: AlphaSignal — 2026-04-08
date: 2026-04-08
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-04-08

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [MinerU-Diffusion: OCR has been reading documents in the wrong order](https://alphasignalai.substack.com/p/mineru-diffusion-ocr-has-been-reading)
*📡 AlphaSignal | 2026-04-08*

Every modern document OCR system works the same way. You give it an image of a page, and an autoregressive decoder generates the text one token at a time, left to right, conditioned on everything that came before.

MinerU2.5, PaddleOCR-VL, dots.ocr, MonkeyOCR, Qwen2.5-VL. 

All of them. Nobody questioned this. 

Documents are two-dimensional. Text, tables, formulas, and layout blocks exist in spatial relationships on a page. There’s no intrinsic reason to force all of that through a sequential decoder.

A team from Shanghai AI Lab’s [OpenDataLab](https://github.com/opendatalab/MinerU-Diffusion) and Peking University finally asked the obvious question: 

What if the serialization order is just an implementation artifact? What if OCR is better modeled as inverse rendering, where the image near-deterministically specifies the output, and left-to-right decoding is adding latency, error propagation, and linguistic bias for no structural reason?

Their answer is [MinerU-Diffusion](https://arxiv.org/abs/2603.22458), a 2.5B parameter open-source system that replaces autoregressive decoding with parallel diffusion denoising. It runs up to 3.26x faster and ships today under MIT license.

Here’s a demo:

Why Autoregressive OCR Is a Bad Fit

The problem with autoregressive decoding for OCR comes down to three compounding issues.

Latency scales linearly with output length. A 10,000-token document requires 10,000 forward passes. No parallelism, no shortcuts.

Errors propagate forward. If the model misreads a character early in the sequence, every subsequent token is conditioned on that mistake. In a 15-page financial report, one wrong digit on page 2 can cascade through the entire document.

The third issue is subtler and more damaging. Autoregressive factorization creates a strong coupling between generation order and linguistic context. The model doesn’t just read the pixels, it learns to fill in plausible text using language priors even when the visual signal is ambiguous.

For clean documents with standard fonts, this invisible guessing usually produces the right answer. For degraded scans, unusual fonts, or structured content like tables and formulas? The guessing becomes a liability you can’t easily detect.

OCR as Inverse Rendering

MinerU-Diffusion starts from a simple premise: OCR isn’t language generation. It’s visual reconstruction.

The mapping from a document image to its text content is near-deterministic. Each character on the page has one correct transcription. This is fundamentally different from open-ended text generation, where many valid completions exist for any given prompt.

Diffusion models exploit exactly this property. Instead of predicting tokens one by one in a fixed order, a masked diffusion process starts with all tokens masked and iteratively denoises them in parallel, conditioned on the document image at every step. Tokens the model is confident about get confirmed early, while uncertain ones get re-masked and refined in subsequent rounds.

Generation order follows confidence rather than reading direction. The visual signal guides everything.

The conditional independence assumption that makes diffusion work for image generation turns out to be even more justified for OCR. Each token can be predicted independently given the visual input and partially observed context, because the image already determines the answer.

How Block-Attention Makes This Practical

You can’t naively apply full-attention diffusion to a 16,000-token document. Full self-attention over L tokens costs O(L²) in memory and compute. That’s a non-starter for long documents.

But full-attention diffusion has deeper problems than just cost. The paper’s appendix shows that without structural anchoring, early denoising errors propagate globally. The model generates repetitive text, truncates prematurely, and quality collapses when the preset generation length doesn’t match the actual document.

MinerU-Diffusion solves this with a block-attention architecture. 

The output sequence gets split into contiguous blocks of 32 tokens each, and within each block, tokens can see every other token through full bidirectional attention. Across blocks, attention is causal: each block can see all preceding blocks but nothing that follows, which provides the structural anchoring that prevents long-range drift.

The complexity drops from O(L²) to O(B·L’²), which for practical document lengths is dramatically cheaper. Because the cross-block structure is causal, you get KV-cache reuse during inference for free. Already decoded blocks don’t need recomputation.

A dynamic confidence threshold τ controls the speed-accuracy tradeoff at inference time. At τ=0.95, the system hits 108.9 tokens per second, a 2.12x speedup over [MinerU2.5](https://arxiv.org/abs/2509.22186) with 99.9% relative accuracy. At τ=0.60, it reaches 164.8 TPS, a 3.26x speedup at around 90% accuracy. Operators can tune this knob per use case.

Benchmark Numbers

On [OmniDocBench v1.5](https://arxiv.org/abs/2501.15242) (1,355 pages, nine document types), MinerU-Diffusion scores 88.94 overall without ground-truth layout and 93.37 with it. The autoregressive baseline MinerU2.5 scores 90.67 and 93.44 respectively. [PaddleOCR-VL](https://arxiv.org/abs/2507.05595) scores 92.56 and 93.91.

In the with-GT-layout setting, which isolates recognition quality from layout detection, MinerU-Diffusion is within 0.07 points of MinerU2.5. The gap in the without-GT-layout setting is larger, and the paper correctly identifies layout detection as the bottleneck rather than the diffusion decoder itself.

Formula recognition on UniMER-Test is competitive with specialized systems, scoring 91.6/91.6/92.0/96.8 across complex printed, handwritten, simple printed, and simple expression categories.

Table recognition is the weak spot. On CC-OCR, it scores 73.77 TEDS versus MinerU2.5’s 79.76. On OCRBench v2 it narrows to 81.18 versus 87.13. Tables have strong structural dependencies that don’t decompose cleanly into 32-token blocks, since a cell’s content depends on row and column positions that depend on other cells. This is a real limitation for financial documents and scientific papers.

But the throughput comparison changes the calculus. MinerU2.5 runs at roughly 52 TPS. MinerU-Diffusion at τ=0.95 runs at 108.9 TPS. 

If you’re processing millions of documents, 2x throughput at 99.9% relative accuracy is a massive operational win.

The Semantic Shuffle Experiment

Take 112 English document images. Shuffle a controlled proportion of words (0% to 100%) while preserving the exact visual layout, fonts, spacing, and formatting. Re-render the documents. They look identical to normal pages, but the text is semantic gibberish.

Now ask both AR and diffusion models to read them.

As distortion increases, MinerU2.5’s performance drops sharply across every metric. BLEU falls from about 0.9 to roughly 0.4. Precision collapses. The AR model depends on language priors to reconstruct text, and when those priors get violated because the words are shuffled nonsense, it fails.

MinerU-Diffusion? Nearly flat across all distortion levels. 

It doesn’t care whether the text makes linguistic sense. It reads pixels. The visual signal is unchanged by semantic shuffling, and the diffusion decoder respects that.

This experiment reveals something uncomfortable: autoregressive OCR models are partially hallucinating. They complete text based on what sounds right, not what’s visually present. For standard documents, this hallucination is usually correct because language is predictable. But for edge cases, degraded scans, or adversarial inputs, you’d never know the model was guessing unless you ran a test like this.

Why should you care

What makes MinerU-Diffusion interesting isn’t just the speed. It’s the argument. The paper makes a principled case that autoregressive OCR has been misaligned with the actual structure of the task from the start. OCR isn’t language generation. It’s visual reconstruction. 

The Semantic Shuffle benchmark alone is worth the read because it gives you a concrete way to measure how much any OCR system relies on linguistic priors versus visual evidence.

The table recognition weakness exists, though, and matters for specific use cases, particularly financial documents and data-heavy scientific papers. For those workloads, AR baselines still win on accuracy. But for high-throughput document processing where you need speed and can tolerate near-identical accuracy, MinerU-Diffusion is already a credible option.

The model is 2.5B parameters, so a single A100 or H100 can handle it comfortably. Four prompt types are supported: layout detection (bounding boxes and element labels), text recognition (plain OCR), formula recognition (LaTeX output), and table recognition (OTSL format).

V2 and the training code are on the roadmap.

References:

Paper: [https://arxiv.org/abs/2603.22458](https://arxiv.org/pdf/2603.22458v1)

GitHub repo: https://github.com/opendatalab/mineru

Join 250k+ developers staying ahead in AI. We curate the latest models, repos, and research — so you don’t miss what matters: [AlphaSignal.ai](http://alphasignal.ai/)

---
