# 🏛️ Turing Post — 2026-04-22

> Ksenia Se 主持，95k+ 訂閱；AI/ML 政策、地緣政治與深度洞察
> 來源：[Turing Post](https://turingpost.substack.com/feed)

---

## [AI 101: How Token Taxonomy Affects Your Bill](https://turingpost.substack.com/p/ai-101-how-token-taxonomy-affects)
*🏛️ Turing Post | 2026-04-22*

Last time ([AI 101: What is a Token?](https://www.turingpost.com/p/token)) we covered what a token is and how tokenization turns text/video/audio into something a model can process. That was the foundation. Now let’s talk about what actually happens in production – because in production, there is no such thing as just “a token” anymore.

Jensen Huang recently said that the AI business is about transforming electrons into tokens. That framing is exactly right – but it is incomplete. Because “tokens” is no longer one thing. A single API call can now involve input tokens, output tokens, reasoning tokens, cached tokens, tool-use tokens, and vision tokens – each billed differently, each consuming compute in a different way. If you want to make good decisions about AI systems and how you are spending your electrons, you need a taxonomy: a clear map of what all these tokens actually are and why they behave so differently.

So thank you, Jensen, for the inspiration. Here is my taxonomy. Let me walk all of you through the full token zoo, species by species. I’m pretty sure you’ll find some you’ve never heard before (and still, you are paying for them).

Surprising result: you’ll never look at an API pricing page the same way.

In today’s episode:

The basic split: input vs. output tokens

Reasoning tokens: the thinking tax

Speculative tokens: the ones born to be discarded

Cached tokens: the reuse discount

Tool-use, system, and retrieval tokens: the hidden overhead

Multimodal tokens: when images, audio, and video enter the pipeline

Structural tokens: the scaffolding you never see

Why the token zoo matters: economics and architecture

Sources and further reading

The basic split: input vs. output tokens

Every API call has two sides: what you send in (input tokens) and what comes back (output tokens). And as you might guess, generating text is computationally harder than reading it.

When the model processes your input, it can do it in parallel. All the tokens in your prompt get processed more or less at once, in what is called the prefill phase. The model builds up its internal representation of everything you said in a single forward pass.

Output is different. The model generates tokens one at a time, each one depending on the one before it. This is autoregressive generation, and it is inherently sequential. Each new token requires a separate forward pass through the model – or at least through the decoder layers. That is why output tokens are more expensive. They require more compute per token.

This is also why you see the price difference on every API pricing page. As of mid-2026, output tokens typically cost 2x to 6x more than input tokens, depending on the provider and model. That ratio reflects a real difference in how the hardware is used.

Created with ChatGP

A practical implication: if you can restructure a task to reduce output length without losing quality – for example, by asking for structured JSON instead of verbose explanations – you are already saving.

Reasoning tokens: the thinking tax

This is the category that has emerged most dramatically since 2024. Reasoning tokens – also called thinking tokens – are tokens the model generates internally as part of a chain-of-thought process before producing its final answer.

When you use models with extended thinking, the model does not jump directly to the answer. It first “thinks through” the problem, producing an internal monologue that may be partially or fully hidden from you. Those intermediate tokens still consume compute. They still cost money. And they can massively inflate the total token count of a response.

Here is what makes reasoning tokens interesting from an economic standpoint:

They can dominate total token usage. A math problem that produces a 200-token answer might generate 3,000 reasoning tokens internally. Your bill reflects the 3,200, not the 200.

They create a new optimization problem. With standard generation, you optimize for prompt efficiency and output conciseness. With reasoning models, you also have to think about whether the task actually benefits from extended reasoning. Simple tasks routed to a reasoning model are pure waste.

Some providers are now exposing reasoning token counts as a separate line item in their API responses. Others fold them into the output token price. This lack of standardization makes cost comparison between providers much harder.

Jensen Huang explicitly named reasoning tokens as a distinct pricing category in a recent conversation with Dwarkesh Patel. And the interesting thing here is that the token has become a segmented product, not a single commodity.

Here is some practical tips from Boris Cherny who builds Claude Code:

Speculative tokens: the ones born to be discarded

If reasoning tokens are expensive because they add thinking, speculative tokens are strange for the opposite reason: they are generated specifically so that most of them can be thrown away.

This is one of the most counterintuitive ideas in the token zoo, and by 2026 it has become production-standard at most major inference providers.

Here is the problem it solves →

---
