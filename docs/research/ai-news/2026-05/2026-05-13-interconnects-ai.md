---
title: "Interconnects AI — 2026-05-13"
date: 2026-05-13
source: Interconnects AI
type: ai-news
---

# 🔗 Interconnects AI — 2026-05-13

> Nathan Lambert 的 RLHF、模型訓練深度專欄
> 來源：[Interconnects AI](https://www.interconnects.ai/feed)

---

## [How open model ecosystems compound](https://www.interconnects.ai/p/how-open-model-ecosystems-compound)
*🔗 Interconnects AI | 2026-05-12*

##### Note: Voice-overs for paywalled posts are available for paid subscribes in podcast apps if you click on settings on Interconnects, then manage your description. Thanks for listening!

Most of the compute to build a leading frontier model comes from R&D costs, rather than the compute to train the final, big model end-to-end. In an ecosystem like China, where all the leading players are open, this creates a potential meaningful advantage in cost structures that'll let labs keep building longer than outside observers would expect.

There are two recent pieces of research, one from Ai2 [documenting the development of Olmo 3](https://arxiv.org/abs/2605.01158) and one from Epoch AI [studying public documentation of costs from various frontier labs](https://epoch.ai/gradient-updates/r-and-d-vs-training-compute), that put the estimate of compute spent on R&D rather than the final model at about 80% (with meaningful error bars).

[](https://substackcdn.com/image/fetch/$s_!VBXD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e980106-980c-4092-bbf1-f472323b8da0_1026x1283.png)

In a world where research and development is most of the compute, the Chinese system is designed around quickly learning from your peers and avoiding double-spending research compute -- or infra effort. It's far from perfect, but it's the closest analog to the OSS ecosystem that one can get for building LLMs. The public discussion of AI has always emphasized that the _models_ are expensive in a way that naturally lets passive readers think this is compute just dedicated to the artifact -- [as we saw with DeepSeek V3](https://www.interconnects.ai/p/deepseek-v3-and-the-actual-cost-of).

[Share](https://www.interconnects.ai/p/how-open-model-ecosystems-compound?utm_source=substack&utm_medium=email&utm_content=share&action=share)

This had me revisiting the core issue of open-source AI, and how it doesn't have the feedback loops akin to open-source software (OSS) users back to the creation itself, that creates immense value following [Linus's law](https://en.wikipedia.org/wiki/Linus%27s_law) of "given enough eyeballs, all bugs are shallow". This self-reinforcement of OSS makes deployment at scale the cheapest possible outcome -- all the users together share the costs of fixing bugs and adding features.

Within open-source AI, almost all the cost falls on the model developer. At the same time, there are huge benefits to releasing the model openly that do reduce costs, but they only help reduce _future_ development and deployment costs for the creator themselves, but more importantly the ecosystem widely.

Open AI models, tools, infrastructure, and everything in between are a cost reduction in development, not plug and play cost reduction on apples to apples solutions or products. If someone is going to be just using AI off-the-shelf with minimal iteration or internal development, using open models will almost always be more expensive. Using closed, integrated, hosted solutions achieves low price points by economies of scale across general usage.

The open-source ecosystem can only try to mirror the OSS-style financial and performance gain in continued performance. The Chinese labs, through incredibly thorough technical reports and intentional knowledge sharing across labs effectively are de-risking ideas for their peer companies to not necessarily need to invest as many resources in.

For this to work, the current norm where AI companies _fork_ open-source tools, to evolve them into internal-only versions, will likely need to fade out. It's too common of a trope for open-source AI companies to have their selling point being better performance via enterprise agreements or internal tools, as the fully open tools that people start with are falling behind in accessibility. A prime example is at-scale RL training of MoE models -- no truly open recipe exists. It's unclear if the open-supporting, but partially closed tools like Thinking Machine's [Tinker](https://thinkingmachines.ai/tinker/) and Prime Intellect's [Lab](https://www.primeintellect.ai/blog/lab) can be open enough for the advantages of an open ecosystem to sustain themselves. The more open the stack is, and the more information is shared, the more costs are reduced in future iterations.

The same reasoning that causes companies to fork open-source tools to make internal versions applies to why there isn't a shared, single foundation model that everyone builds on. Building the best model today becomes an art of integrating your hardware, data, and infrastructure, while evolving all of them at a relatively high rate that lets you keep up with the frontier of performance. Given that all signs point to LLMs continuing their steady march in performance improvements for years, it seems unlikely to expect this equilibrium to change in the near term. This is exactly why I wrote my post on the [inevitable need for an open model consortium](https://www.interconnects.ai/p/the-inevitable-need-for-an-open-model) - this shared resource is far more efficient and may become the only financially viable way to compete at the future frontier scale with open models.

It's worth noting that, of course, the closed labs also see the investigations of the open frontier model companies and can benefit from them, but with the assumption that the closed labs are [some months ahead in the development tree](https://www.interconnects.ai/p/reading-todays-open-closed-performance), they often naturally stand to benefit less from the shared insights. The stronger the open-source community is, the more cost incentive there is for the various companies to be relatively close together on the same Pareto curve of performance.

This realization of the difference between _development_ costs, or a process-focused technology, rather than some shared foundation that all the labs build on directly was downstream of a question I got in feedback to [my recent China trip summary](https://www.interconnects.ai/p/notes-from-inside-chinas-ai-labs). The question was: "Was there any chance of the Chinese ecosystem converging on a single base model to save costs?" The follow-up to this question was on if any of the open-weight companies in China are using open-source in strategically meaningful ways. There are many more useful questions to ask here, especially when trying to understand the different operational patterns of the ecosystems.

## China's foundation model development model

I found the following interview conducted by Bill Gurley with Dan Wang, author of Breakneck, and Patrick McGee, author of Apple in China, (both books I strongly recommend - must reads) very thought provoking on the biggest differences between technology cultures in the U.S. and China.

I get a lot of exposure to these differences at this point in my open-source AI arc. There's a deep yearning to influence Western audiences and thinking that has bubbled up out of the Chinese AI ecosystem in the last year. This was obviously a strong pretext for why the [SAIL](https://readsail.com/) group got such access in our recent trip - it's not a given that anyone in the AI ecosystem will talk to senior leadership at so many companies.

[ Read more ](https://www.interconnects.ai/p/how-open-model-ecosystems-compound)

---

## [Notes from inside China's AI labs](https://www.interconnects.ai/p/notes-from-inside-chinas-ai-labs)
*🔗 Interconnects AI | 2026-05-07*

Staring out the window on a new, high-speed train from Hangzhou to Shanghai I'm gifted with views of dramatic ridgelines speckled with wind turbines that are silhouetted against the setting sun. The mountains cast a backdrop to a mix of spanning fields and clustered skyscrapers. I'm returning from China with great humility. It's a very warming, human experience to go somewhere so foreign and be so welcomed. I had the honor of meeting so many people in the AI ecosystem who I knew from afar, and they greeted me with big smiles and cheer, reminding me how global my work and the AI ecosystem is.

Interconnects AI is a reader-supported publication. Consider becoming a subscriber.

## The mentality of Chinese researchers

The Chinese companies building language models are set up as the perfect fast-followers for the technology, building on long-standing cultural traditions in education and work, along with subtly different approaches to building technology companies. When you look at the outputs, the latest, biggest models enabling agentic workflows, and the ingredients, excellent scientists, large-scale data, and accelerated computing, the Chinese and American labs look largely similar. The lasting differences emerge in how these are organized and conditioned.

I've long thought that a reason that the Chinese labs are so good at catching up and keeping up with the frontier is that they're culturally aligned for this task, but without talking to people directly I felt like it wasn't my place to attribute substantial influence to this hunch. Speaking with many wonderful, humble, and open scientists at the leading Chinese labs has crystallized a lot of my beliefs.

So much of building the best LLMs today comes down to meticulous work across the entire stack, from data to architecture details and RL algorithm implementations. All points of the model can give some improvements, and fitting them in together is a complex process where the work of some brilliant individuals needs to get shelved in favor of the overall model maximizing a multi-objective optimization.

Where American researchers are obviously also brilliant at solving the individual components, there's more of a culture of speaking up for yourself in the U.S. As a scientist, you're more successful when you speak up for your work and modern culture is pushing the new path to fame of "leading AI scientists". This results in direct conflict. The Llama organization is heavily rumored to have collapsed under the political weight of these interests embedding themselves in a hierarchical organization. I've heard of other labs saying that it can be needed to pay off a top researcher to get them to stop complaining about their idea not making it in the final model. Whether or not that's exactly true, the idea is clear. Ego and desires for career advancement do get in the way of making the best models. A small, directional shift in this sort of culture between the U.S. and China can have a meaningful impact on the final outputs.

Some of this has to do with who is building the models in China. There's an immediate reality at all of the labs that a large proportion of the core contributors are active students. The labs are quite young, and it reminds me of our setup at Ai2, where students are seen as peers and directly integrated in the LLM team. This is incredibly different from the top labs in the US, where the likes of OpenAI, Anthropic, Cursor, etc. simply don't offer internships. Other companies like Google nominally have internships related to Gemini, but there's a lot of concern about whether your internship will be siloed and away from anything real.

To summarize how the slight change in culture can improve the ability to build models:

  * More willingness to do non-flashy work in order to improve the final model,

  * People new to building AI can be free of prior phases of AI hype cycles, allowing them to adapt to the new modern techniques faster (in fact, one of the Chinese scientists I talked to really actively attached to this strength),

  * Less ego enabling org charts to scale slightly, as there's less gamifying the system, and

  * Abundant talent well-suited to solving problems with a proof of concept elsewhere, etc.




This slight inclination towards skills that complement building today's language models stands in contrast to a known stereotype that Chinese researchers tend to produce less creative, field-spawning, 0-to-1 academic style research. Among the more academic lab visits on our trip, many leaders talk about cultivating this more ambitious research culture. At the same time, some technical leaders we talked to were skeptical about whether such a rewiring in the approach to science is likely in the near term, because it'll take a redesign of the education and incentive systems that is too big to happen within the current economic equilibrium. This culture seems to be training students and engineers that are excellent at the LLM building game. They also, of course, have an extremely abundant quantity.

These students told me about a similar brain drain happening in China as in the U.S., where many who previously considered academic paths now intend to stay in industry. The funniest quote was from a researcher who was interested in being a professor to be close to the education system, but remarked that education is solved with LLMs - "why would a student talk to me!"

The students have a benefit of coming at LLMs with fresh eyes. Over the last few years we've seen the key paradigm of LLMs shift from scaling MoE's, to scaling RL, to enabling agents. Doing any of these well involves absorbing an insane amount of context quickly, both from the broader literature and the technical stack at your company. Students are used to doing this and excited to humbly drop all presumptions about what should work. They dive in head first and dedicate their life to getting the chance to improve the models.

These students are also so magically direct and free of some of the philosophical chatter that can distract scientists. When asking questions on how they feel about the economics or long-term social risks of models, far fewer Chinese researchers have sophisticated opinions and a drive to influence this. Their role is to build the best model.

This difference is subtle, and easy to deny, but it is best felt when having long conversations with an elegant, brilliant researcher who can clearly communicate well in English, basic questions on more philosophical aspects of AI hang in the air with a simple confusion. It's a category error to them. One researcher even quoted the famous Dan Wang premise of China being run by engineers, relative to the lawyers of the U.S. when probing in these areas, to emphasize their desire to build. There's no track in China that systematically enables the growth of star power for Chinese scientists, akin to mega mainstream podcasts like Dwarkesh or Lex.

Trying to get Chinese scientists to comment on the coming economic uncertainty fueled by AI, questions beyond the capabilities of simple AGI, or moral debates on how models should behave all served to capture the upbringing and education of these scientists (edited[1](https://www.interconnects.ai/feed#footnote-1)). They are extremely dedicated to their work, but have grown up in a system where debates and opinions on how society should be structured and changed are not encouraged. 

Zooming out -- Beijing especially felt much like the Bay Area, where a competitive lab is a short walk or Uber away. I got off a flight and stopped by Alibaba's Beijing campus on the way to the hotel. Then, in 36 hours we went to all of Z.ai, Moonshot AI, Tsinghua University, Meituan, Xiaomi, and 01.ai. Travel by Didi is easy, and if you select an XL in China you're often paired with electric mini vans that have massage chairs. We asked the researchers about the talent wars, and they said it's very similar to what we're experiencing in the U.S. It's normal for researchers to bounce around, and much of where people choose to go is based on the best current vibes.

In China, the LLM community feels far more like an ecosystem than battling tribes. Across many off the record conversations, it's nothing but respect for peers. All of the Chinese labs fear Bytedance with their popular Doubao model, which is the only frontier closed lab in China. At the same time, all of the labs have massive respect for DeepSeek as the lab with the best research taste in execution. When you meet with lab members off the record in the States, sparks fly quickly.

The most striking part of the humility of Chinese researchers is how they also often shrug on the business side, saying it's not their problem, where everyone in the U.S. seems to be obsessed with various ecosystem-level industrial trends, from data sellers to compute or fundraising.

[Share](https://www.interconnects.ai/p/notes-from-inside-chinas-ai-labs?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Where China's AI industry differs (and matches) the Western labs

The thing that makes building an AI model today so interesting is that it's not just about getting a group of great researchers in one building together to produce an engineering marvel. It used to be this, but to sustain AI businesses, the LLMs are becoming a mix of building, deploying, funding, and getting adoption for this creation. The leading AI companies exist in complex ecosystems that supply money, compute, data and more in order to keep pushing the frontier. 

The integration of these various inputs to creating and sustaining LLMs is fairly well conceptualized and mapped for the Western ecosystem, as typified by Anthropic and OpenAI, so finding big differences in how the Chinese labs think about it points at where the different companies can be making meaningfully different bets on the future. Of course, these futures can be heavily dictated by the constraints on funding and/or compute.

I've documented the biggest "AI Industry" level take-aways from talking to these labs:

  1. **Early signs of domestic AI demand.** There's a much-touted hypothesis that the Chinese AI market will be smaller because Chinese companies don't tend to pay for software - thus, never unlocking a giant inference market supporting labs. This is only true for software spend that maps to the SaaS ecosystem, which is historically tiny in China, where on the other hand there is obviously still a large cloud market in China. A crucial unanswered question - one which the Chinese labs themselves debate - on if spending for AI in the enterprise tracks the SaaS market (small) or the cloud market (fundamental). On net, it feels like AI is trending closer to the cloud, and no one was actively worried about a market growing around the new tools.

  2. **Most developers are Claude-pilled.** Most of the AI developers in China are obsessed with Claude and how it's changed how they build software, despite Claude nominally being banned in China. Just because China has historically been hesitant to buy software does _not_ give me the impression that there won't be a massive surge in inference demand. Chinese technical staff are so practical, humble, and motivated - a fact that seems stronger than any commitment to previous habits in not spending.  
  
Some Chinese researchers mention building with their own tools, such as the Kimi or GLM CLIs, but _all_ of them mention building with Claude. There were also surprisingly few mentions of Codex, which is definitely surging in popularity in the Bay Area.

  3. **Chinese companies have a technology ownership mentality.** The Chinese culture is combining with a roaring economic engine to create unpredictable outcomes. I'm left with a lasting feeling that the numerous AI models reflect a practical, current equilibrium of the many technology businesses here. There's no master plan. The industry is defined by a respect for ByteDance and Alibaba, the incumbents expected to win large portions of all markets with their substantial resources. DeepSeek is the respected technical leader, but far from a market leader. They set the direction, but aren't set up to win economically.  
  
This leaves companies like [Meituan](https://huggingface.co/meituan-longcat/LongCat-Next) or [Ant Group](https://huggingface.co/inclusionAI/Ling-2.6-1T), where people in the West can be surprised they're building these models. In reality, they see LLMs obviously as being central to future technology products, so they need a strong base. When they fine-tune the strong, general purpose model it hardens their stack from getting the open community to provide feedback on it, and they can keep internal, fine-tuned versions of the model for their products. The "open-first" mentality in the industry is largely defined by practicality -- it helps make their models get strong feedback, it gives back to the open-source community, and empowers their mission.

  4. **Government aid is real, but unclear how big.** It's often asserted that the Chinese government is actively helping with the open LLM race. This is a government that's decentralized across many levels, each of which doesn't have a clear playbook for what exactly they do. Neighborhoods in Beijing compete for tech companies to house their offices there. The "help" offered to these companies almost certainly involved removing bureaucratic red tape like permits, but how far does it go? Can levels of the government help attract talent? Can they help smuggle chips? Across the visit, there were many mentions of government interest or help, but far too little to report the details as assertive or have a confident worldview of how government can bend the trajectory of AI in China.   
  
There were certainly no hints of the top levels of the Chinese government influencing any technical decisions in the models.

  5. **The data industry is far less developed.** Having heard so much about the likes of Anthropic or OpenAI spending $10M+ for single environments, with cumulative spend on the order of hundreds of millions per year to push the frontier of RL, we were eager to know if Chinese labs are either buying the same environments from companies in the U.S. or supported by a mirrored domestic ecosystem. The answer was not quite complete that there's _no_ data industry, but rather that their experience was that the data industry was relatively poor quality and it is often better to build the environments or data in-house. Researchers themselves spend meaningful time making the RL training environments, and some of the bigger companies like ByteDance and Alibaba can have in-house data labelling teams to support this. This all mirrors the build-not-buy mentality from the previous bullet.

  6. **Desperation for more Nvidia chips.** Nvidia compute is the gold-standard for training and everyone is limited in progress by not having more of it. If supply was there, it is obvious that they would buy it. Other accelerators, including but not limited to Huawei, were spoken positively of for inference. Countless labs have access to Huawei chips.




These points paint a very different picture of an AI ecosystem, where quickly mapping how Western labs operate to their Chinese counterparts will often result in a category error. The crucial question is if these different ecosystems will produce meaningfully different types of models, or if the Chinese models will always be explained by being similar to the U.S. frontier models of 3-9 months ago.

[Subscribe now](https://www.interconnects.ai/subscribe)

## Conclusion: The global equilibrium

I knew so little about China going into the trip and came out with the feeling of just starting to learn. China isn't a place that can be expressed by rules or recipes, but one with very different dynamics and chemistry. The culture is so old, so deep, and still completely intertwined with how domestic technology is built. I have much more learning ahead.

So much of the current power structures in the US use their current worldviews of China as crucial mental devices for decision making. Having talked, in person, either formally or informally to pretty much every leading AI lab in China, there are a lot of qualities and instincts in China that'll be very hard to model with Western decision making. Even after asking directly about _why_ these labs release their top models openly, the intersection between ownership mentality and genuine ecosystem support is hard for me to connect the dots on. 

The labs here are practical and not necessarily absolutists around open-source, where every model they build would be released openly, but there's a deep intentionality in supporting developers, the ecosystem, and using it as a way to learn more about their models.

Almost every major Chinese technology company is building their own general purpose LLMs, as we see with the likes of Meituan (delivery service) and Xiaomi (broad consumer technology company) releasing open weight models. The equivalent companies in the U.S. would just buy services. These companies aren't building LLMs out of a race to be relevant with the hot new thing, but a deep fundamental yearning to control their own stack and develop the most important technologies of the day. When I look up from my laptop and always see bunches of cranes on the horizon, it obviously fits in the with the broader culture and energy around building in China.

The humanity, charm, and genuine warmth of Chinese researchers is extremely humanizing. At a personal level, the cut-throat geopolitical conversation we're used to in the U.S. hasn't permeated them at all. The world can use more of this simple positivity. As a citizen of the AI community, I currently worry more about the fissures appearing within members and groups around labels of nationality. 

I'd be lying if I said I didn't want US labs to be clear leaders in every part of the AI stack -- especially with open models where I spend my time -- I'm American, and that's an honest preference. With this, I want the open ecosystem itself to thrive globally, as this can create safer, more accessible, and more useful AI for the world, and right now the question is whether American labs will take the steps to own that leadership position. 

As of finishing this piece, more [rumors](https://x.com/andrewcurran_/status/2052023542582292855?s=46) are swirling of executive orders influencing open models, which can further complicate this synergy between American leadership and the global ecosystem -- it doesn't fill me with confidence.

Thank you to all the wonderful people I got to talk to at Moonshot, Zhipu, Meituan, Xiaomi, Qwen, Ant Ling, 01.ai, and others. Everyone has been so welcoming and gracious with their time. I'll keep sharing my thoughts on China as they crystallize, across culture generally and AI specifically. It is obvious that this knowledge will be directly relevant to the story unfolding at the frontier of AI development.

[1](https://www.interconnects.ai/feed#footnote-anchor-1)

Edit 05/07: In this paragraph in the original I misattributed an unwillingness to speak on broader issues to humility, which can of course play a part, but this habit is also shaped by the system which they were trained and raised, a system they are successful in and adept at navigating.

What I removed: … capture the upbringing and education of these scientists extreme humility of these scientists. It's more than just being dedicated to _their_ work, but they don't want to comment on issues they're not informed on.…

---
