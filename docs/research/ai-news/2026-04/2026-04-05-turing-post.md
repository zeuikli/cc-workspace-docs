---
title: "Turing Post — 2026-04-05"
date: 2026-04-05
source: Turing Post
type: ai-news
---

# 🏛️ Turing Post — 2026-04-05

> Ksenia Se 主持，95k+ 訂閱；AI/ML 政策、地緣政治與深度洞察
> 來源：[Turing Post](https://turingpost.substack.com/feed)

---

## [#2: The Unsexy Truth of AI Adoption](https://turingpost.substack.com/p/2-the-unsexy-truth-of-ai-adoption)
*🏛️ Turing Post | 2026-04-05*

Before we jump into the next installment of our The Organizational Age of AI series, we’d like you to check this interview with Sanja Fidler. Sanja works at the frontier of autonomous vehicles and robotics, and is one of the leading voices in spatial intelligence and physical AI. What is brewing in her lab now is likely a preview of what the rest of us will be using in the future. This episode is worth watching for everyone who wonders what kinds of architectural and multimodal breakthroughs we still need to achieve before robotics and autonomous vehicles become truly usable.

Episode #2 of The Org Age of AI: The Unsexy Truth of AI Adoption

Spend a few days in San Francisco right now and you will start believing that AI has already taken over everything. The city is literally blanketed with ads about AI and everything even remotely related to AI. It is in every café conversation, every event, every product pitch, every hiring deck. It creates a very powerful illusion: that the rest of the country is moving at the same speed, and that the world is basically one clean deployment plan away from autonomous organizations.

It is not.

Most companies across the US are still at a much earlier stage. For many of them, AI still means ChatGPT for writing, Copilot for code, meeting summaries, maybe a small internal experiment, and a lot of vague pressure to “do something with AI.” And we are not even touching the rest of the world here, where the picture is even more uneven.

Reading Twitter might give you the anxiety that you are terribly behind and everyone else is already operating in some futuristic AI economy where machines do the work and humans relax. They do not. You still have to work, and in many cases, you have to work more. So today, we are going to talk about what actually has to happen inside a company for AI to become operational: what a company needs to know about its own work, how little of that knowledge is actually usable by machines, and what it takes to change that. With real use cases. We will also discuss how AI is compressing the distance between enterprises and small companies.

What’s in today’s episode?

What does the path to AI maturity actually look like?

What most companies actually want

Why the middle cannot be skipped

L1 to L2: Making the organization legible to itself (hardest transition)

L2 to L3: Trusting your own data (most underestimated transition)

L3 to L4: The system starts acting on what it sees. Human’s role changes (most overhyped transition)

L4 to L5: The system changes how the organization works (most profound transition)

What this is actually about

Large enterprises and very small teams – is the approach different?

What does the path to AI maturity actually look like?

There is no shortage of maturity models. Gartner has one. McKinsey has one. Deloitte has one. Most of them place organizations on a neat timeline: you are here, then you move there.

But AI maturity is not just a sequence of stages. It is a stack of dependencies. Each layer rests on the one below it. You cannot build the fourth layer if the second one is unstable. You can pretend otherwise, of course. Plenty of companies do. That is how you get pilots that look impressive in a demo and then disappear within six months.

What we want to describe here is not a timeline but a ladder of organizational capability. The lower rungs are familiar: tacit knowledge, scattered experimentation, isolated productivity wins. The upper rungs get all the hype: adaptive systems, agents, self-improving workflows. The real pain sits in the middle, where a company has to make itself explicit enough to be understood by a machine, trustworthy enough to be acted on, and structured enough for judgment to move to the right place.

That middle is where deployments either become real or die.

What most companies actually want

Here is the pattern: A product leader watches a demo of an agent completing a multi-step workflow. Maybe it reads documents, synthesizes findings, and drafts a report with a thoughtful recommendation. Maybe it resolves support tickets end to end, taking a support ticket, cross referencing that with what’s in the database, doing a coding task, pushing a fix to production and communicating to the user. The demo is real. The capability exists. 

The immediate response: we need this.

Then the company looks inward and the picture is different. Processes run on habit and improvisation. Critical knowledge lives in two or three people’s heads. Like an informal fee in a questionable economy, knowledge is “corrupted” because its under the table, not above board and above all not visible. It’s hoarded for protective reasons. Data systems use different naming conventions because different teams built them at different times for different reasons. The org chart says one thing about how decisions get made; reality says another.

Most companies want to go from scattered ChatGPT use directly to agents and autonomy. The middle layers – the ones where deployments either become real or die – get skipped in the planning. They are the critical ones to build upon.

Why the middle cannot be skipped

Nobody builds a dramatic keynote around normalizing cost codes. They should though! Because that is exactly where the real drama lives.

AI maturity is cumulative. Each level gives the organization a new capability, and that capability reveals something about the organization that was previously invisible. The revelation forces a reassessment. Then the next level becomes possible.

This is not a linear climb. Different departments sit at different levels. Engineering might be at L3 while finance is at L0. Marketing moves fast with content generation while compliance lags a full level behind. The unevenness is normal. Governance almost always trails deployment.

The question is not “what level is our company?” It is “where are the structural gaps, and which ones are blocking us?”

Here is the stack:

The levels themselves are descriptive. The real story lives in the transitions.

L1 to L2: Making the organization legible to itself

This is the hardest transition in the entire framework.

Companies at L1 often look more advanced than they are. Someone uses ChatGPT for writing. Someone else uses Claude or Copilot for code. A third person built a clever internal assistant that works well enough to impress leadership and badly enough that nobody wants to maintain it. Some of this work is genuinely useful. The problem is that it does not compound. It remains personal, brittle, and undocumented. When the employee leaves, the workflow often leaves with them.

The move to L2 is not about choosing better tools. It is about the organization learning to describe its own work. What are the actual rules for processing an invoice? Not what the policy document says – what do people actually do? Which naming conventions does each supplier use? When someone uploads a file for review, what is the real approval chain – not the org chart version, the one that actually happens?

We worked with a bookkeeping company focused on food service processing dozens of invoices weekly for different clients from different suppliers. They wanted AI to automate the data entry – we have both PDFs and images from cell phones, hand written notes on the invoice where things were accepted or changed. As an OCR exercise this was straightforward enough technical challenge and the new models are up to the task.

Some suppliers put fuel service fees into soft costs, while others put bottle deposits in there, how are these factored into calculating unit price? How do you handle weight-based versus unit-based pricing? Which suppliers issue updates with a new invoice number invalidating old ones, and which ones reissue changes under the invoice number, and if so how do your determine which is the current? Six weeks of work before any AI could happen! – because the business process had never been made explicit. The humans had been absorbing ambiguity that a machine could not.

And once the system forced clarity, we actually started seeing fewer “exceptions” coming through the suppliers. As the light pushed out the darkness, fewer games were being played on their other side slipping in expenses that were previously overlooked.

At a construction firm, we inherited a data sync system that had been built over a year by a single developer – 224 commits of working logic. When that developer became unavailable, the entire system broke. Cost code mappings lived in one person’s head. “Plumbing” had been renamed to “15.1 PLUMBING” in the accounting system, and only one team member knew the translation. 

Once you normalize that data, you can start asking much more useful questions. Can the system detect when something is over budget? Can it flag when burn rates look wrong for a specific cost code? Demolition, for example, should burn down mostly at the beginning of a project, while finishing work should ramp up toward the end. But in this case, large discrepancies kept showing up, and it turned out project managers were playing all sorts of games by moving money from one bucket to another. They were not changing the final number. They were managing client expectations by delaying bad news until some other part of the project was going well and everyone was in a better mood to hear it. None of that logic is visible to the machine.

This is where companies discover something uncomfortable: a great deal of institutional knowledge has never been written down, and some of that is not accidental. When the rules live in someone’s head, that person is indispensable. When the process is undocumented, nobody can question whether it makes sense. Making work legible means making it inspectable, and that is a form of vulnerability – for humans:

Recording meetings so they become searchable records. Documenting exception rules. Cleaning data into structured formats. Defining what “good” looks like so you can evaluate whether a machine did it right. This is the work of L2. It does not look like AI. The output is a spreadsheet of mappings and a document that explains what terms mean. Writing something unspoken down can uncover uncomfortable truths. But without it, everything above collapses.

What this transition is misunderstood as: “We need an AI strategy” or “We need to pick the right tools.” The blocker is that the company cannot describe its own workflows. This is where pilot purgatory lives – companies start pilot after pilot, each works in isolation, none connect, nothing accumulates.

What makes it worth doing anyway: everything you build to make the organization legible to machines also makes it better for humans. Onboarding gets faster. Bus factor drops. The organization becomes more resilient. The work is not overhead on the way to AI. It is good organizational hygiene that AI forces you to finally do.

L2 to L3: Trusting your own data

This is the most underestimated transition. This is where most companies discover that connecting data is the easy part. Trusting it is harder. →

---
