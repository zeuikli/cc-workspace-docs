---
title: Turing Post — 2026-04-03
date: 2026-04-03
source: Turing Post
type: ai-news
---

# 🏛️ Turing Post — 2026-04-03

> Ksenia Se 主持，95k+ 訂閱；AI/ML 政策、地緣政治與深度洞察
> 來源：[Turing Post](https://turingpost.substack.com/feed)

---

## [🎙️ Be Bold, Stay Safe: How NVIDIA Is Engineering the Hardest Tradeoff in Self-Driving](https://turingpost.substack.com/p/be-bold-stay-safe-how-nvidia-is-engineering)
*🏛️ Turing Post | 2026-04-03*

AV cars are very polite. They’re too polite for humans. You need to be bold.

- You do need to be bold. But at the same time, you also always need to be risk-averse. It’s a combination, right? So that balance is one of the hard challenges of getting self-driving right.

Ksenia Se and Ali Kani

The first phrase is mine, watching from the passenger seat as the new self-driving Mercedes-Benz was trying to make its way into a packed right lane. 

We are in the middle of San Francisco, around 2 pm, in real traffic, testing NVIDIA’s Autonomous Driving (AV) software, which NVIDIA is building as a platform (with a lot of key elements being open sourced) any car company can adopt – first for L2 driving and then eventually for much higher levels of autonomy. That openness and availability excite me the most.

The reply comes from Ali Kani, who was our guide that day. He has been at NVIDIA Automotive for almost eight years, through many of the ups and downs, and he is eager to explain everything. What started as a joke turns out to be a neat summary of why NVIDIA’s autonomy stack looks the way it does. A modern self-driving system has to be smooth enough to behave like a good human driver, cautious enough not to do something stupid, and traceable enough that an OEM, a regulator, and eventually a passenger can understand why it did what it did.

This is a real inflection point for self-driving cars, and if you want to understand the future that is starting to take shape now, you need to understand how this stack works.

This piece can be read in a few different ways. It is partly a guide to the current stack, from in-car models to safety layers to simulation. It is partly a look at the hardware path NVIDIA believes autonomy will require. And it is partly a case study in how one company is trying to make self-driving more reproducible, more scalable, and less dependent on closed internal systems.

Or you can just [experience our drive](https://www.youtube.com/watch?v=lnNi72Md9I4) and the conversation that became the backbone of this article →

… By the way, although Ali thought the driver might need to take over, the car, after a brief hesitation, found the right moment and made it into the lane. It was smoother than many human drivers would have been.

What’s in today’s episode?

The easiest way to understand NVIDIA’s autonomy stack

It’s not there yet (and that’s awesome)

How this whole thing works →

What changes when NVIDIA moves to Level 4

Where Alpamayo actually fits

Before reasoning VLAs, how were AV systems handling driving? (and why NVIDIA has not abandoned the modular world completely)

What happens in the cloud, and why it may matter as much as the car?

Is NVIDIA’s dual-stack approach a silver bullet?

So where is NVIDIA different (and what might soon make it the largest car company without building a single car)?

How do I actually start learning this stack?

A serious resource list for people who want to learn the field

The easiest way to understand NVIDIA’s autonomy stack

The easiest mistake is to think of NVIDIA’s self-driving effort as one product. It is much closer to a layered system. 

At the bottom is in-vehicle compute. Today that means DRIVE AGX Orin in current-generation systems. Orin is the compute platform that Mercedes publicly tied to its next-generation Level 2 and Level 3 driving efforts when it laid out MB.OS. For the next step up, NVIDIA wants DRIVE AGX Thor. Thor is the Blackwell-based automotive SoC designed for much heavier AI workloads, including generative AI, vision-language-action models, and increasingly consolidated cockpit-plus-driving workloads. One useful clarification here, because NVIDIA has created enough branding layers to qualify as a minor weather system: DRIVE AGX is the hardware family, Orin and Thor are the chips, and Hyperion is not the chip but the reference vehicle architecture built around the chip.

On top of the hardware sits the low-level software foundation. This is DriveOS and the broader runtime plumbing around it. DriveOS is NVIDIA’s automotive operating system and SDK. It supports Linux or QNX, sensor integration, image processing, AI acceleration, inter-process communication, debugging, and profiling. Simply put, DriveOS is the systems layer, NvMedia handles the sensor and media pipelines, NvStreams handles efficient data movement, CUDA and TensorRT handle accelerated compute and inference, and DriveWorks sits above that as the middleware toolkit developers actually use to build AV functions.

Above that sits the runtime autonomy software, which NVIDIA calls DRIVE AV. This is the part that matters most conceptually, because DRIVE AV is built as a dual-stack architecture (according to Ali Kani):

One side is the AI end-to-end stack that learns holistic driving behavior from data – AlpaMayo.

The other is a parallel classical safety stack that provides redundancy, verification, and explicit guardrails – Halos.

Publicly, Halos is now NVIDIA’s umbrella safety framework across hardware, software, tools, datasets, processes, inspection, and validation. In the interview, the term was also used in a narrower way to describe the classical safety guardrails sitting beside the end-to-end model. Both uses are related, but they are not identical.

Then there is Hyperion, which is NVIDIA’s reference vehicle architecture. Hyperion bundles compute, sensors, and safety assumptions into a template OEMs can build on. Hyperion 8 is the Orin generation. Hyperion 10 is the Thor generation and the more obvious Level 4 jump: dual Thor, lidar, more cameras, more radars, more interior sensing, and enough redundancy to keep operating if something fails. Hyperion is NVIDIA’s way to standardize the vehicle architecture around its autonomy stack.

Finally, there is the cloud training, simulation, and safety loop, which many people still underestimate. NVIDIA’s AV stack is not only in-vehicle software. It is also DGX for training, Omniverse and Cosmos for simulation, NuRec for reconstruction, open datasets for training and validation, and increasingly generative systems like AlpaDreams for closed-loop world generation. This is why Halos is described as a cloud-to-car safety system. NVIDIA is explicitly saying that the safety story begins long before deployment and stretches across training, validation, simulation, and runtime behavior.

Image Credit: NVIDIA, 3D reconstruction

Naming cheat sheet, because NVIDIA has created a small alphabet soup

It’s not there yet (and that’s awesome)

Ali was very clear during the ride that this is still Level 2, not Level 4. The driver remains responsible, and he genuinely expected that in dense city traffic we might need to take over. The current setup is also deliberately constrained: no lidar, relatively modest compute, and hardware designed to be cheap enough for real consumer vehicles rather than experimental fleets. The cars drives very smoothly, but sometimes you can feel those constraints in the behavior: a little ghost break, a brief hesitation, over-politeness. →

---
