# Improved Baselines with Visual Instruction Tuning

**Authors:** Haotian Liu, Chunyuan Li, Yuheng Li, Yong Jae Lee
**Year:** 2023
**Venue:** CVPR 2024
**ArXiv:** https://arxiv.org/abs/2310.03744

---

## Abstract

The paper demonstrates that the fully-connected vision-language cross-modal connector in LLaVA is surprisingly powerful and data-efficient. With simple modifications to LLaVA, specifically the use of CLIP-ViT-L-336px with an MLP projection and adding academic-task-oriented VQA data with response formatting prompts, the improved model (LLaVA-1.5) establishes stronger baselines that achieve state-of-the-art across 11 benchmarks. The final 13B checkpoint uses merely 1.2M publicly available data, and finishes full training in approximately 1 day on a single 8-A100 node, demonstrating remarkable data and compute efficiency while outperforming models trained on substantially more data.

---

## Key Contributions

- **MLP connector superiority**: demonstrates that a two-layer MLP projection between vision encoder and LLM outperforms both linear projection and complex connector designs (Q-Former, cross-attention), establishing that simplicity wins when backbone encoders are strong
- **CLIP-ViT-L-336px** at higher resolution with MLP projection achieves state-of-the-art on **11 benchmarks** using only **1.2M publicly available training samples** — less data than most competing approaches
- **Full training in ~1 day on a single 8-A100 node**, greatly reducing the compute barrier to reproducing competitive multimodal baselines
- **Response formatting prompts** for academic VQA data (e.g., requiring short answers for VQAv2 vs. free-form for LLaVA-bench) significantly improve task-specific performance without architectural changes
- **CVPR 2024** — establishes LLaVA-1.5 as the widely-adopted, reproducible strong baseline for multimodal vision-language research that subsequent papers compare against
- Ablation studies systematically show which components drive gains: MLP connector (+2.3 pts avg), higher resolution (+1.5 pts avg), academic VQA data mix (+2.7 pts avg)
- Demonstrates that scaling data is not always necessary — targeted data curation with appropriate formatting often matters more than raw data volume

---

## Methodology

LLaVA-1.5 modifies the original LLaVA architecture in three key ways while keeping the overall design philosophy unchanged. First, the linear projection connector is replaced by a two-layer MLP with GELU activation. This small change provides substantially more capacity for the vision-language alignment mapping without adding meaningful complexity or training cost.

Second, the vision encoder is upgraded from CLIP ViT-L/14 at 224px to CLIP ViT-L/14 at 336px, increasing the number of visual tokens from 256 to 576. Higher resolution allows the model to perceive finer-grained visual details critical for tasks like reading text in images (OCR), counting objects, and answering questions about small regions.

Third, the training data mixture is expanded with task-specific VQA datasets (VQAv2, GQA, OCR-VQA, TextVQA, VisualGenome) formatted with response formatting prompts. These prompts instruct the model to answer in the expected format for each task — a short answer for multiple-choice VQA, or a free-form response for open-ended questions. The full training uses LLaMA-2 (7B and 13B variants) as the language backbone. Stage 1 pre-training remains unchanged from LLaVA (665K image-text pairs, projection only). Stage 2 fine-tuning uses the expanded 1.2M instruction-following dataset with both LLM and MLP trainable.

---

## Main Results

| Benchmark | LLaVA-1.5 13B | Previous SOTA | Notes |
|-----------|---------------|---------------|-------|
| VQAv2 | 80.0% | 77.2% (InstructBLIP 13B) | +2.8% |
| GQA | 63.3% | 49.5% (BLIP-2 13B) | +13.8% |
| TextVQA | 61.3% | 50.1% (mPLUG-Owl2) | +11.2% |
| MMBench | 67.7% | 64.3% (InstructBLIP) | +3.4% |
| ScienceQA | 71.6% | 61.1% (LLaVA) | +10.5% |
| POPE | 85.9% | 85.8% | Competitive |
| MM-Vet | 35.4% | 31.1% (InstructBLIP) | +4.3% |

State-of-the-art on 11 of 12 evaluated benchmarks at time of publication, using only 1.2M training samples compared to models like InstructBLIP using 16M+ or Qwen-VL using 1.4B.

---

## Limitations & Future Work

- Single-image context only; cannot handle interleaved multi-image sequences (unlike Flamingo/Otter)
- 576 visual tokens at 336px resolution is still insufficient for very high-resolution tasks (document understanding, detailed chart reading) — addressed in LLaVA-HD and LLaVA-NeXT with dynamic resolution
- The model can still hallucinate objects or attributes not present in the image
- Strong on academic benchmarks but can struggle on open-ended, nuanced real-world conversations requiring deeper visual reasoning
- The 1-day training result applies to the 13B model; larger scales would require proportionally more resources

---

## Why This Matters for AI Practitioners

LLaVA-1.5's core message is **engineering discipline beats architectural complexity**: a simple MLP connector, higher-resolution backbone, and well-curated mixed training data outperform much more elaborate designs. This is a direct counter to the prevailing assumption that better multimodal performance requires more sophisticated fusion mechanisms.

For practitioners, LLaVA-1.5 is the go-to reproducible baseline: 1-day training on 8 A100s, 1.2M public data, open weights, and SOTA performance. The response formatting insight is immediately actionable — simply changing the expected output format in prompts for different task types can meaningfully improve performance without any architecture changes. The systematic ablations also serve as a practical guide for anyone building vision-language systems: invest first in resolution, then connector capacity, then data quality/formatting before exploring complex architectural additions.
