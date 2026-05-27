---
title: "Turing Post — 2026-04-16"
date: 2026-04-16
source: Turing Post
type: ai-news
---

# 🏛️ Turing Post — 2026-04-16

> Ksenia Se 主持，95k+ 訂閱；AI/ML 政策、地緣政治與深度洞察
> 來源：[Turing Post](https://turingpost.substack.com/feed)

---

## [AI 101: What Is a Token (and why it runs AI)?](https://turingpost.substack.com/p/ai-101-what-is-a-token-and-why-it)
*🏛️ Turing Post | 2026-04-16*

With so much happening in AI, going back to basics can be surprisingly grounding. It helps reduce anxiety and gives you a firmer grasp of the technology you’re dealing with. So today, we’re doing pure AI 101 and talking about The Token. That little fellow that runs AI. It sounds simple, but it isn’t. If you want to understand generative AI, you need a clear understanding of what a token actually is. Today we’re going to dive into the very, very basics of what a token is, how tokens are formed, why the type of tokenization matters, and how tokens became the new currency. Let’s go!

Surprising result: you feel much more confident after reading this article.

In today’s episode:

What is a Token?

Tokenization: How to get tokens from the text

How AI models process tokens

Why tokens are so important

The economics of tokens

What about token economy in open models? 

Conclusion

Sources and further reading

What is a Token?

We deal with tokens every day, but what exactly is a token? How does a model “see” information? Or does it see it at all?

Not in the way we do. A model does not see words, sentences, or meaning in any human sense. It starts with tokens: small units into which text is broken before it can be processed at all. Those tokens are converted into IDs, then into vectors, and only from there does the model begin to work with the input.

That may sound technical, but it has very practical consequences. Tokens are not only the unit a model reads. They are also the unit that shapes how much text the model can handle, how fast it responds, how much memory it uses, and how much it costs to run. That is why tokens ended up becoming the basic currency of generative AI.

And this is where things get slightly counterintuitive: a token is not the same as a word. It can be a whole word, part of a word, punctuation mark, space, or character sequence the model has learned to treat as one unit. In other words, before a model can generate language, language first has to be broken into pieces the model can count.

Image Credit: OpenAI

In practice, common words are often a single token, while rarer or longer words may be split into smaller pieces, such as encod + ing. This is how models stay flexible: instead of memorizing every possible word, they learn to work with reusable parts.

There is a useful English-language rule of thumb from OpenAI: one token is roughly four characters, or about three-quarters of a word, and one to two sentences are around 30 tokens. But that is only a rough guide. The actual count depends on the tokenizer and the language. The same idea expressed in another language may take more tokens, which is one reason token costs are not experienced equally across languages.

English is often tokenized into words and subword pieces, because spaces clearly separate words and longer terms can be broken into reusable chunks. Chinese works differently: words are not separated by spaces, and single characters often already carry meaning, so tokenization tends to stay closer to the character level. That is one reason the same sentence can produce a very different token count in English and Chinese.

So how does raw text become something a model can process? Through →

Tokenization: How to get tokens from the text

Before the model starts to process text it needs to be tokenized. And this is where things start to get interesting. Modern AI systems usually do subword tokenization, which sits between word-level and character-level tokenization. That compromise solves an important problem: it keeps the vocabulary relatively compact, while still allowing the model to handle rare or unseen words by breaking them into smaller meaningful pieces.

This details is important because the way text is split changes how efficiently a model reads, how much context it can fit, and sometimes even how well it performs across languages. The three most important tokenization approaches to know are Byte Pair Encoding (BPE), WordPiece, and SentencePiece. 

Let’s unfold each of them (plus a couple more).

---
