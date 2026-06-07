# 🔧 Simon Willison's Weblog — 2026-05-27

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [The pressure](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-26*

**[The pressure](https://daniel.haxx.se/blog/2026/05/26/the-pressure/)**

Daniel Stenberg on the unprecedented level of pressure the `curl` team are facing right now thanks to the deluge of (credible) AI-assisted security issues being reported.

> The rate of incoming security reports is 4-5 times higher than it was in 2024 and double the speed of 2025 -- meaning that **on average we now get more than one report per day**. The quality is way higher than ever before. The reports are typically _very_ detailed and long. [...]
> 
> For the first time in my life, my wife voiced concerns about my work hours and my imbalanced work/life situation. I work more than I’ve done before, but the flood keeps coming. [...]
> 
> This is a never-before seen or experienced pressure on the curl project and its security team members. An avalanche of high priority work that trumps all other things in the project that is primarily mental because we certainly _could_ ignore them all if we wanted, but we feel a responsibility, we have a conscience and we are proud about our work.

The good news is that `curl` is a very solid piece of software, so the vulnerabilities people are finding tend not to be of high severity:

> What is also a good trend: almost no one finds _terrible_ vulnerabilities. All vulnerabilities found the last few years in curl have _all_ been deemed severity LOW or MEDIUM. I'm not saying there won't be any more HIGH ever, but at least they are rare. The [most recent severity high curl CVE](https://curl.se/docs/CVE-2023-38545.html) was published in October 2023.

Via [Lobste.rs](https://lobste.rs/s/dw02ye/pressure)

Tags: [curl](https://simonwillison.net/tags/curl), [security](https://simonwillison.net/tags/security), [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [daniel-stenberg](https://simonwillison.net/tags/daniel-stenberg), [ai-ethics](https://simonwillison.net/tags/ai-ethics), [ai-security-research](https://simonwillison.net/tags/ai-security-research)

---

## [Microsoft Copilot Cowork Exfiltrates Files](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-26*

**[Microsoft Copilot Cowork Exfiltrates Files](https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files)**

The biggest challenge in designing agentic systems continues to be preventing them from enabling attackers to exfiltrate data.

In this case Microsoft Copilot Cowork (yes, that's [a real product name](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/)) was allowing agents to send emails to the user's own inbox without approval... but those messages were then displayed in a way that could leak data to an attacker via rendered images:

> Because these messages can contain external images that trigger network requests to external websites, data can be exfiltrated when a user opens a compromised message sent by the agent.

Since OneDrive can create pre-authenticated download links, a successful prompt injection could cause those links to be leaked, allowing files to be downloaded by the attacker. 

Via [Hacker News](https://news.ycombinator.com/item?id=48272354)

Tags: [microsoft](https://simonwillison.net/tags/microsoft), [security](https://simonwillison.net/tags/security), [ai](https://simonwillison.net/tags/ai), [prompt-injection](https://simonwillison.net/tags/prompt-injection), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [exfiltration-attacks](https://simonwillison.net/tags/exfiltration-attacks), [lethal-trifecta](https://simonwillison.net/tags/lethal-trifecta)

---

## [Quoting Paul Graham](https://simonwillison.net/2026/May/26/paul-graham/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-26*

> A lot of the emails I get from founders are now written in a hard-hitting journalistic style. I know they're written by AI, because no founder ever wrote this way before. And once you realize something is written by AI, it's hard not to ignore it.
> 
> I have never knowingly finished reading an email signed by a human but written by AI. It feels like being lied to, and who would stand for that?
> 
> [[...](https://twitter.com/paulg/status/2058863028523659390)] It makes me think less of the author. It means they can't write well unaided (or feel they can't), and that they're trying to trick me. 
> 
> It's not impressive to use AI to write stuff for you; any teenager can do that.

-- [Paul Graham](https://twitter.com/paulg/status/2058844147092488401)

Tags: [writing](https://simonwillison.net/tags/writing), [ai-misuse](https://simonwillison.net/tags/ai-misuse), [paul-graham](https://simonwillison.net/tags/paul-graham), [generative-ai](https://simonwillison.net/tags/generative-ai), [ai](https://simonwillison.net/tags/ai), [llms](https://simonwillison.net/tags/llms)

---

## [Quoting Corey Quinn](https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-26*

> I cannot believe I'm saying this, but getting the literal Pope to canonize your product's specific technical limitations as a spiritual treatise is the single greatest act of vendor lobbying I have ever seen.

-- [Corey Quinn](https://twitter.com/quinnypig/status/2058960462256210268), on Anthropic co-founder Christopher Olah's [influence](https://www.washingtonpost.com/world/2026/05/25/pope-elevates-ai-ethics-religious-imperative-with-first-encyclical/) on _Magnifica Humanitas_

Tags: [ai-ethics](https://simonwillison.net/tags/ai-ethics), [corey-quinn](https://simonwillison.net/tags/corey-quinn), [anthropic](https://simonwillison.net/tags/anthropic), [ai](https://simonwillison.net/tags/ai)

---

## [Notes on Pope Leo XIV's encyclical on AI](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-25*

Dropped this morning by the Vatican: [Magnifica Humanitas of His Holiness Pope Leo XIV on Safeguarding the Human Person in the Time of Artificial Intelligence](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html). This is a _very interesting_ document. It's some of the clearest writing I've seen on the ethics of integrating AI into modern society.

Pope Leo XIV chose the name Leo in honor of Pope Leo XIII, who is known for his 1891 _[Rerum novarum](https://en.wikipedia.org/wiki/Rerum_novarum)_ encyclical on "Rights and Duties of Capital and Labor".

[This story](https://www.vaticannews.va/en/church/news/2025-05/leo-xiii-s-times-and-our-own.html) on Vatican News further clarifies the significance of that decision:

> Meeting with the College of Cardinals for their first formal encounter after his election, Pope Leo XIV explained part of the reason for the choice of his papal name. "There are different reasons for this," he said, before going on to explain that he chose the name Leo "mainly because Pope Leo XIII, in his historic encyclical _[Rerum novarum](https://www.vatican.va/content/leo-xiii/en/encyclicals/documents/hf_l-xiii_enc_15051891_rerum-novarum.html)_ addressed the social question in the context of the first great industrial revolution."
> 
> "In our own day," he continued, "the Church offers to everyone the treasury of her social teaching in response to another industrial revolution and to developments in the field of artificial intelligence that pose new challenges for the defence of human dignity, justice, and labour."

And now we get Pope Leo XIV's own encyclical on the AI revolution. There's a lot in here, but the writing style is very approachable, including to non-Catholics.

#### A few of my highlights

(I listened to most of the encyclical on a walk with our dog, my first time trying the [ElevenReader iPhone app](https://apps.apple.com/us/app/elevenreader-read-books-aloud/id6479373050). It worked very well: I pasted in a URL to the document and it read it to me in a very high quality voice, highlighting each paragraph as it went.)

Here are some of my highlights. In each case below **emphasis** is mine.

Here's a useful description of the interpretability problem for LLMs in section 98:

> First, any statement regarding AI risks becoming quickly outdated, given the remarkable pace at which these systems are developing. Second, all of us, including those who design them, possess only a limited understanding of their actual functioning. Indeed, **current AI systems are more “cultivated” than “built,” for developers do not directly design every detail, but instead create a framework within which the intelligence “grows.”** As a result, fundamental scientific aspects — such as the internal representations and computational processes of these systems — remain, at present, unknown.

I liked section 83's description of the relationship between development and dignity:

> For individuals as well as for nations, development is both a duty and a right. Minimum conditions are required for enabling every person and people to flourish in accord with their dignity, without being kept in a state of dependence or excluded from access to necessary goods. Development is truly human when it places people at the center instead of the accumulation of wealth, and when it concerns peoples as well as individuals. Justice demands the recognition of the rights of society and the rights of peoples, and includes a responsibility toward future generations. **Development is not truly human if it increases consumption for some while shifting costs and burdens onto others, or relegates entire regions to subordinate roles, preventing them from realizing their full potential**.

Baked in cultural biases and sycophancy get a mention in section 100:

> In personal use, three aspects in particular deserve careful consideration: the ease with which results are obtained, the impression of objectivity and the simulation of human communication. The speed and simplicity with which information, complex analyses, media content and practical assistance can be accessed undoubtedly makes life easier. Yet they can also encourage excessive reliance and the search for ready-made answers, and weaken personal creativity and judgment. **The apparent objectivity of the responses and suggestions these systems provide can lead us to overlook the fact that they reflect the cultural assumptions of those who designed and trained them, with all their strengths and limitations**. The artificial imitation of positive human communication — words of advice, empathy, friendship and even love — can be engaging and at times genuinely helpful. **However, for less discerning users, it can also be misleading, creating the illusion of a relationship with a real personal subject**. When words are simulated, they do not build genuine relationships, but only their appearance. The artificial imitation of care or support can become particularly risky when it enters contexts where real relationships and emotional bonds are lacking.

101 touches on the environmental impact:

> Current AI systems require enormous amounts of energy and water, significantly influencing carbon dioxide emissions, and place heavy demands on natural resources. **As their complexity increases, especially in the case of large language models, the need for computing power and storage capacity grows too, which requires an extensive network of machines, cables, data centers and energy-intensive infrastructure**. For this reason, it is essential to develop more sustainable technological solutions that reduce environmental impact and help protect our common home.

102 covers the risks of algorithmic systems making decisions that impact people's lives without "compassion, mercy, forgiveness":

> The use of AI is never a purely technical matter: **when it enters processes that affect people’s lives, it touches on rights, opportunities, status and freedom**. Important and sensitive decisions — concerning employment, credit, access to public services or even a person’s reputation — **risk being fully delegated to automated systems that do not know “compassion, mercy, forgiveness, and above all, the hope that people are able to change,”** and can therefore give rise to new forms of exclusion.

105 emphasizes the need for human accountability in how these systems are applied:

> For AI to respect human dignity and truly serve the common good, responsibility must be clearly defined at every stage: **from those who design and develop these systems to those who use them and rely on them for concrete decisions**. In many cases, however, the internal processes leading to a result remain opaque, making it harder to assign responsibility and correct errors. **This is where accountability becomes crucial: the possibility of identifying who must “account” for decisions, justify them, monitor them, and, when necessary, challenge them and remedy any harm caused**.

And 108 touches on the way AI amplifies the power of those with resources:

> In fact, as with every major technological shift, **AI tends to amplify the power of those who already possess economic resources, expertise and access to data**. In light of the common good and the universal destination of goods, this raises serious concerns, since small but highly influential groups can shape information and consumption patterns, influence democratic processes and steer economic dynamics to their own advantage, undermining social justice and solidarity among peoples. For this reason, it is essential that the use of AI, especially when it touches on public goods and fundamental rights, be guided by clear criteria and effective oversight, grounded in participation and subsidiarity.

That same section explicitly calls out data as something that should be thought of more as a public good:

> [...] Moreover, **ownership of data cannot be left solely in private hands** but must be appropriately regulated. **Data is the product of many contributors and should not be treated as something to be sold off or entrusted to a select few**. It is necessary to think creatively in order to manage data as a common or shared good, in a spirit of participation, as [Saint John Paul II](https://www.vatican.va/content/john-paul-ii/en.html) already suggested regarding collective goods.

Given that Palantir is named after a _Lord of the Rings_ reference, I can't help but wonder if the J.R.R. Tolkien quote from _The Return of the King_ (section 213) was the Pope throwing a little shade at Peter Thiel.

> The twentieth-century Catholic author J.R.R. Tolkien, in the words of a protagonist in one of his novels, described our responsibility in this way: “It is not our part to master all the tides of the world, but to do what is in us for the succour of those years wherein we are set, uprooting the evil in the fields that we know, so that those who live after may have clean earth to till.” The civilization of love will not arise from a single or spectacular gesture, but from the sum total of small and steadfast acts of fidelity that serve as a bulwark against dehumanization. For this reason, it is worthwhile pausing to reflect on some aspects of how we, each in our own way, can cooperate in building the civilization of love.

#### Another 2026 prediction down

On 6th January this year I joined the [Oxide and Friends 2026 predictions](https://oxide-and-friends.transistor.fm/episodes/predictions-2026) podcast episode to talk about predictions for 2026, 2029 and 2032. I [wrote mine up here](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/), with hindsight they weren't nearly ambitious enough - it's already undeniable that LLMs write good code, we've made huge advances in sandboxing and New Zealand kākāpō have indeed [had a truly excellent breeding season](https://news.mongabay.com/short-article/2026/03/critically-endangered-kakapo-parrot-has-standout-breeding-season/).

There's one segment from the episode that I didn't bother to include in my write-up, but that I can't resist providing as a lightly-edited transcript here:

> **Bryan Cantrill:** [37:13](https://oxide-and-friends.transistor.fm/episodes/predictions-2026/transcript#t=37m13s)
> 
> I think that AI has created some real public perception problems for itself. And I think that you are gonna have one of the frontier model companies, this year, have a white paper explaining how the proliferation of AI will mean prosperity for everybody. They will be trying to make some economic argument - because this is gonna be a 2026 election issue, how we think of these things and how they are regulated and it's a big mess. There's more heat than light in this debate.
> 
> **Simon Willison:** [38:05](https://oxide-and-friends.transistor.fm/episodes/predictions-2026/transcript#t=38m5s)
> 
> I'd like to tag something on to that one: I think that only works if they can sort of wash that through existing trusted experts. Sam Altman and Dario are constantly publishing essays about this stuff and nobody believes a word they say. Get Barack Obama's signature on one of these position papers and _maybe_ you've got something people might start to trust a little bit.
> 
> **Adam Leventhal:** [38:27](https://oxide-and-friends.transistor.fm/episodes/predictions-2026/transcript#t=38m27s)
> 
> Otherwise, it's just like "leaded gas is good for you", says Exxon.
> 
> **Bryan Cantrill:** [38:31](https://oxide-and-friends.transistor.fm/episodes/predictions-2026/transcript#t=38m31s)
> 
> I mean, yeah. God. Obama... let's go with that, that's a great one because if it's like Bill Clinton everyone's gonna kind of roll their eyes, so it's gotta be someone who's got real credibility saying that this is gonna be broad-based... I'd say if they get that person to do it, it's gonna be revealed that that's also a bit crooked.
> 
> **Simon Willison:** [38:57](https://oxide-and-friends.transistor.fm/episodes/predictions-2026/transcript#t=38m57s)
> 
> How about the Pope?
> 
> **Bryan Cantrill:** [39:01](https://oxide-and-friends.transistor.fm/episodes/predictions-2026/transcript#t=39m1s)
> 
> The Pope is very into this stuff! That's a great prediction. We've hit pay dirt. The Pope weighing in on LLMs and their economic impact on the world.
> 
> Simon, I'm giving you full credit if the Pope weighs in believing that this is gonna be economic devastation.

My prediction here looks a whole lot less insightful given the Leo XIV/Leo XIII relationship, which I was unaware of when we recorded the episode!

Tags: [predictions](https://simonwillison.net/tags/predictions), [ai](https://simonwillison.net/tags/ai), [kakapo](https://simonwillison.net/tags/kakapo), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [bryan-cantrill](https://simonwillison.net/tags/bryan-cantrill), [ai-ethics](https://simonwillison.net/tags/ai-ethics)

---
