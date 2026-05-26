# 🔬 Latent Space — 2026-05-05

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [🔬Doing Vibe Physics — Alex Lupsasca, OpenAI](https://www.latent.space/p/lupsasca)
*🔬 Latent Space | 2026-05-05*

Some people are going crazy over GPT 5.5. Some people. This is the story of the [Jagged](https://www.notion.so/Tanishq-https-x-com-iScienceLuvr-2c312774e7a88187a391e2a67b42cd56?pvs=21) [Frontier](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700). People who use AI to write emails or even code implementation work [find the lift moderate](https://www.reddit.com/r/codex/comments/1su4jik/did_gpt55_actually_impress_you_or_does_it_feel/) whereas people pushing the limits of the model are figuring out that the [limits just moved outwards](https://www.youtube.com/watch?v=kCMgUvnpzsM).

[Alex Lupsaska](https://lupsasca.com/) has been tracking this limit for a year and a half now. “When GPT5 came out, it was able to reproduce one of my best papers (that took a very long time to come up with) in 30 minutes.”

But Alex also notes that this shift was mostly invisible.

I remember when GPT-5 came out… on Twitter, the reception was lukewarm. A lot of people were like, well, we expected a lot more, and it’s not better at writing email. And I remember thinking, well, okay, GPT-3 could write email. How much better can it get at writing email? That’s not the point. But at the science frontier, the capabilities were really taking off.

We walk through his paper and more with him in today’s Science pod! [Watch here](https://youtu.be/9d899Ram9Bs).

The “Oscar for physics”

Alex made an early splash in his career with breakthroughs in our understanding of black holes. He’s also known for [Black Hole Explorer](https://www.sciencenews.org/article/alex-lupsasca-black-hole-photon-ring) and [an iPhone app that makes visualizing black holes fun and interactive to regular audiences](https://arxiv.org/abs/2603.05810). Alex won the 2024 New Horizons in Fundamental Physics Breakthrough Prize. Known as the “Oscar for physics” this is arguably the most prestigious prize an early stage theoretical physicist can win.

Alex first saw promise for AI in theoretical physics after he asked o3 for help on his research. In the podcast, Alex recalls asking GPT for help with a calculation that would have taken days, and getting a result in eleven minutes. 

[tweets](https://x.com/ALupsasca/status/1978823200986316870)

He immediately recognized how impactful AI would be for his work even as though his physicist colleagues and the larger community gave it a lukewarm or skeptical reception.

The Move 37 Moment for AI x Physics

GPT-5 had just been released, and Alex tried asking it to solve a problem in a just published paper. GPT-5 said no answer. But [Mark Chen, CRO of OpenAI](https://www.linkedin.com/in/markchen90), pushed a bit harder, and had Alex prime the model with a textbook warmup problem, which it easily solved. After using this “priming” trick, GPT-5 was able to reproduce his full result in eleven minutes (yes, the paper was released after the model’s training cutoff).

“This changes everything.” Alex notes that we seem to be on the edge of a massive change in theoretical physics reasoning. A year prior LLMs were just starting do correct math. Now ChatGPT could reproduce his hardest paper in the time it takes to get a coffee.

Alex was on sabbatical at Vanderbilt, and he joined OpenAI to start pushing the boundary of AI’s ability to accelerate physics.

“AI solved the problem before the plane landed”

Alex began to put GPT through it’s paces, reaching out to colleagues for problems they were stuck on. His old PhD advisor ([Prof. Andrew Storminger at Harvard](https://en.wikipedia.org/wiki/Andrew_Strominger)) had an insidght about certain physical quantities known as “single-minus gluon tree amplitudes”. 

@the_IAS, @VanderbiltU, @Cambridge_Uni, and @Harvard. It shows that a gluon interaction many physicists expected would not occur can arise under specific","username":"OpenAI","name":"OpenAI","profile_image_url":"https://pbs.substack.com/profile_images/1885410181409820672/ztsaR0JW_normal.jpg","date":"2026-02-13T19:19:07.000Z","photos":[],"quoted_tweet":{},"reply_count":949,"retweet_count":1489,"like_count":9539,"impression_count":4520424,"expanded_url":null,"video_url":null,"belowTheFold":true}" data-component-name="Twitter2ToDOM">

In certain cases, these amplitudes [may be non-zero](https://x.com/OpenAI/status/2022390100055986540?s=20) when previously shown to always vanish. The team pushed this intuition forward, and came up with a formula for these quantities that appeared nonzero, but which was otherwise completely intractable. 

A key equation [from the paper](https://arxiv.org/pdf/2602.12176) spans a quarter of a page, involving a sum of 32 terms, each of which is a product of four terms, each encoding a complicated formula. Just computing this by hand was a Herculean effort by the lead author!

Spending over a year on this problem, no real progress was made.

Prof. Storminger planned to visit OpenAI to work on the problem the week after the initial conversation started. In that one week ChatGPT fully solved the problem, as Alex recalled, before Prof. Storminger’s plane even landed.

What was interesting is not only that ChatGPT solved this problem, but how it solved it. The model quickly realized found a limiting case (known as the “half-collinear regime”), that in hindsight has a nice intuitive explanation. Taking this limit, the gnarly results collapsed down to a simple and intuitive formula!

The last step was to prove this intuitive formula. The team started with a fresh session, gave a prompt with the context of what they previously learned, and let the model loose. Not only was ChatGPT able to reproduce the previous result, it was able to prove it using a technique unknown to the authors!

The Vibe Physics moment

With a concrete success in the bag, the team asked if they could generate new physics from scratch using ChatGPT. They took on what they felt to be a harder problem, looking at the graviton, a proposed particle that should appear when one combines gravity and quantum mechanics. They wrote up a simple prompt asking ChatGPT to perform the same research as the gluon paper but instead for gravitons. And then hit go!

What came next was truly “vibe physics”, with ChatGPT pushing out 110 pages of novel physics, new calculations, and novel techniques. This was over the course of a day, with most interactions the familiar following the now familiar pattern for anyone who uses a coding agent:

GPT: Here's your <long, detailed, awesome result>. 
Would you like me to do <another really cool thing>?
Alex: Yes, please do!
GPT: <does the really cool thing>

And for those who look deeply, this really was not just a direct 1-1 mapping between gluons and gravitons. ChatGPT imported new techniques that were necessary due to the nature of gravitons, and used them flawlessly.

[context](https://x.com/ALupsasca/status/2029256973473239041)

They spent the next three weeks verifying all the results. And voila! A [new paper](https://arxiv.org/abs/2603.04330) featuring novel results in quantum gravity, generated in less than three days total. Truly a “Feel the AGI moment”.

For those interested, there’s a [blog post](https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/) with the [full transcript](https://cdn.openai.com/pdf/gluon-to-graviton-paper.pdf) from initial prompt to final paper. Even if you know no physics, it’s crazy seeing pages of correct calculations fall out of simple prompts such as “Yes calculate outside of SD first. This is the first step.”

Out-of-domain = new knowledge

The thing that is qualitatively different between Vibe Physics and Vibe Coding is that Vibe Physics means actually extending the frontier of human knowledge. Looking at the Gluon and Graviton results, they seem in retrospect, like many results in physics and math, like natural extensions of what we already know. This is in fact part of what makes them beautiful. But this was a problem that stumped experts in the domain for a year. Although it does still have a bit of a recombinant flavor, this thing has never been done before.

It may be that there are still large classes of problems that AI won’t do well on, and approaches that an AI might not think to take. This is the “taste” that everyone has been talking about. Alex told us that these capabilities, however, allow him to explore many possible avenues in order to map out much more ambitious problems to tackle. With AI able to output results basically as fast as we can conceive and validate them, the scope of what one theorist can hope to achieve has just gotten a lot, lot bigger.

When doing research for this podcast, we asked AI if this was the case, and it suggested the IUPAP award, which it turns out Alex also won in 2024.

This is an interesting prompting trick. Get the model thinking along the right lines by solving an easier, but related problem.

To be pedantic, the original claim is still true in the case of “3+1 dimensional spacetime”, the spacetime that models our reality. The insight here was that if we have two dimensions of time and two dimensions of space, some magic happens with the math which breaks the original assumption. What does it mean to have two time dimensions and two space dimensions? This is a fun discussion we unfortunately didn’t have time to get into.

For experts, this is the equivalent to one particle decaying into n-1 other particles.

Much has been written about this particle, and there are better references than this blog. The only thing relevant for this is that gravitons are an analog to gluons, but for gravity. And that the concept of helicity is more complicated, but one can still define a meaningful analog to the gluon paper.

---
