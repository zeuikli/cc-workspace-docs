# 🔬 Latent Space — 2026-04-20

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [🔬 Training Transformers to solve 95% failure rate of Cancer Trials — Ron Alfa & Daniel Bear, Noetik](https://www.latent.space/p/noetik)
*🔬 Latent Space | 2026-04-20*

Today, we explain this piece of “clickbait” from our guest!

true, but not how you think!

TL;DR: 95% of cancer treatments fail to [pass clinical trials](https://www.nature.com/articles/s41467-025-64552-2), but it may be a matching problem — if we better understood what patients have which tumors which will respond to which treatments, success rates improve dramatically and millions of lives can be saved — with the treatments we ALREADY have.

See [our full episode](https://youtu.be/uqM8qjbLRHA) dropping today:

Why Big Pharma is licensing AI Models

Tolstoy famously wrote, ‘All healthy cells are alike; each cancer cell is unhappy in its own way.’ Or something like that. Cancer might be the most misunderstood disease out there. It’s not one disease, it’s a family of diseases. Hundreds, maybe thousands, of unique diseases each with its own underlying biology. With this lens, saying you’ll “cure cancer” is like saying you’ll solve legos.

We keep hearing AI will cure cancer, but sadly it may not be so easy. Today’s guests — [Ron Alfa](https://x.com/Ronalfa/status/2031083722980864010) and [Daniel Bear](https://www.linkedin.com/in/daniel-bear-b79480279) from [Noetik](https://www.noetik.ai/) — thinks they can use AI to break through a core bottleneck in the treatment development process.

[GSK recently signed a $50M deal for their technology](https://x.com/BiotechTV/status/2011577286634729785) that also includes an (undisclosed) long-term licensing deals for Noetik’s models like the recently announced [TARIO-2](https://x.com/Ronalfa/status/2045579548977500197?s=20), an autoregressive transformer [trained](https://x.com/owl_posting/status/2026313562721853730) on one of the largest sets of tumor spatial transcriptomics datasets in the world. Whole-plex spatial transcriptomics is the richest way to read a tumor, and approximately ~0% of cancer patients going through standard care ever get one — and TARIO-2 can now predict an ~19,000-gene spatial map from the H&E assay every patient already has. 

Most big AI plays in BioTech have focused on discovery, and usually result in an in-house development effort (meaning tools companies usually become drug companies). This deal stands out in that it is a software licensing deal, and represents a commitment to a platform rather than a drug. 

With attention on other software tools for drug development (see the [Boltz episode](https://www.latent.space/p/boltz) and Isomorphic for example), it is starting to look like the appetite of Pharma for biotech tools has finally started to grow. Why the sudden interest?

Cancer is hard

Biology is hard, cancer is harder. But despite this, we’ve made incredible progress. So many cancers that would have been death sentences twenty years ago are routinely survivable. It used to be our main strategy was just chemotherapy — poison you and hope the tumor dies before you do. Now, there are many treatments that actually kill a tumor and leave the rest of you intact! Immune checkpoint inhibitors like Keytruda and Opdivo target the defenses of dozens of tumor types. CAR-T therapy adds modified T-cells to your blood that can target B-cell malignancies very accurately. Antibody Drug Conjugates such as Trastuzumab combine a drug with an antibody, allowing it to target very specific (cancer) cells. We truly live in marvelous times.

With that said, we still have a long way to go. For every type of cancer with a miracle treatment, we have many more that are still death sentences. The world spends $20-30 billion a year trying to cure cancers, with hundreds of clinical trials yearly.Yet, progress is slow with a [95% failure rate in clinical trials](https://www.nature.com/articles/s41467-025-64552-2).

The lab doesn’t translate to the clinic

Are we leaving something on the table? Enter Noetik and Ron Alfa. Ron’s core thesis is that many of these “failed” treatments actually work! But we’re not looking at the right patients with the right tumors. If only we had a way to really understand the unique types of cancer biologies and which patients will respond to which treatments, we might be able to show a much higher success rate. Millions of lives (and billions of dollars) may ride on this.

[source](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf)

The Hard part: Blind Faith in Data Collection

Ron and Noetik had the conviction to spend almost two years just collecting data. Lots, and lots, and lots, of data. Noetik has acquired thousands of actual human tumors, and collects a large multimodal dataset of hundreds of millions of images that allows them to create a detailed map of the cell makeup in the local environment. These are real human tumors, not frankenstein mouse models or immortal cell lines.

This data is then fed into a massive self-supervised model, creating a “[virtual cell](https://www.latent.space/p/biohub)”. This model has a deep understanding of cancer biology — Noetik has worked carefully to show it can distinguish different types of tumors. Maybe even tumors we didn’t identify as distinct previously! More recently they figured out how to scale up their model and data, and see no limit in their scaling laws!

Noetik’s models can simulate how a patient will respond to experimental treatments. They are working with partners to test promising drugs that were demonstrated to be safe, but not effective. If these models work as hoped, Noetik will bring new cancer treatments to patients without developing a new drug! Their models will also guide the discovery process towards drugs that are more likely to make it through clinical trials. You can imagine why this is so attractive to GSK.

We’ll see…

Ron and Dan make pretty persuasive arguments that their models will truly assist in cohort selection in useful ways and this seems valuable. And we think it’s pretty clear that

Translation from lab to clinic is the biggest bottleneck for drug development.

Better cohort selection using biomarkers is likely to improve translation from lab to clinic.

Noetik has already had some success here. We’ll see if they’re able to translate that into a reliable advantage.

Stepping back a bit from the technology, curing cancer is a pretty unambiguously positive application of AI. It is also a very hard problem to solve. Our guess is that most people have been impacted by cancer or will be at some point soon. And we hope that learning about the amazing work that companies like Noetik are doing will inspire a generation of AI engineers to work on the hardest and most exciting problems that society faces.

Full Video Pod:

Their spatial transcriptomics dataset features over 1000 “channels”, that’s quite a feat!

For those experts in the audience, the four modalities Noetik collects data on are: spatial transcriptomics, spatial proteomics, H&E imaging, and whole exome sequencing.

---
