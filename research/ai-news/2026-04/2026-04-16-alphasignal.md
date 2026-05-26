# 📡 AlphaSignal — 2026-04-16

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [Create beautiful architecture diagram of any project with this open source AI tool](https://alphasignalai.substack.com/p/create-beautiful-architecture-diagram)
*📡 AlphaSignal | 2026-04-16*

For developers, one of the first few things you need to come up with before handing over a project to another dev or team is an architecture diagram.

It serves as a visual blueprint that turns complex code, services, and infrastructure into a clear high-level map. It helps other developers understand the project faster and makes it easier for teams and stakeholders to see how everything works together.

But creating one manually can be a hassle, especially if the project is large or complex.

So here’s a new AI tool that automates that process for you.

It’s called [Architecture Diagram Generator](https://github.com/Cocoon-AI/architecture-diagram-generator), an open-source Claude skill that can generate clean, beautiful architecture diagrams from a plain English prompt. At the time of writing, it has already racked up around 2.5k stars on GitHub.

What is Architecture Diagram Generator?

It’s a Claude Code skill that lets you generate beautiful, dark-themed system architecture diagrams as standalone HTML or SVG files.

No design skills needed: just describe your architecture in plain English

Iterate quickly: ask Claude to add components, change layouts, or update styles

Share easily: output is a single HTML file, no special software required

Setting up the skill

Get the Claude Skill by downloading the [architecture-diagram.zip](https://architecture-diagram.zip/) file from this GitHub repo: [Cocoon-AI](https://github.com/Cocoon-AI) / [architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator)

The ZIP file should contain the Skill.md file, which includes all the necessary instructions for generating the diagrams.

To add the skill to Claude, go to the Customize settings page and, under the Skills tab, click the + icon and select Upload a skill.

Select the ZIP file you downloaded earlier. If everything goes well, you should see the new skill added to the Personal skills section.

Make sure the skill is enabled by toggling the enable/disable switch beside the share button.

That’s it. The skill is now ready to use.

How to create diagrams

To create diagrams, open Claude Code and start a chat. Import a sample project from your local disk and use the text below as a prompt template:

Use your architecture diagram skill to create an architecture diagram from this description:

> NextJS project
> Typescript Shadcn frontend
> PostgreSQL database
> Hosted on vercel
> Cloudflare for file storage
> Stripe for payment
> Resend for email
> Sanity for content
> Vercel AI gateway for AI provider

You can edit the system description based on your own project. If you are not fully sure about the architecture, you can load the project folder into ChatGPT or Claude and ask it to scan the codebase and extract the system architecture for you.

Here’s a sample prompt you can use.

Analyze this codebase and describe the architecture. Include all major
components, how they connect, what technologies they use, and any cloud
services or integrations. Format as a list for an architecture diagram.

Once the prompt is ready, I recommend setting the model to Claude 4.6 Opus for a more accurate result.

This will trigger the skill and generate the architecture diagram in HTML format.

This is what the final result looks like:

Awesome. The diagram already looks clean, although there are still a few slightly awkward arrow placements. Still, I really like the dark theme, the color choices, and the overall layout.

To clean it up, you can simply follow up with Claude and ask it to fix the issues. In my example, I just said: “Fix the overlapping arrows. Use curved arrows if needed.” Here’s the updated diagram:

Awesome. I love how clean and sleek it looks now. Since the output is in HTML format, I can also continue editing the file manually if needed.

I’ve tried a couple of diagram generators before, but this one is by far the most elegant-looking.

It works with GitHub repos too

Another cool trick is that you can point it to any public GitHub repository, and the tool can generate a nice architecture diagram for that as well.

For example, I took the recently viral [GBrain: Opinionated OpenClaw/Hermes Agent Brain](https://github.com/garrytan/gbrain) by and asked Claude to create a diagram using the custom skill.

The original architecture diagram in the repo looks like this:

This is what Claude created:

Just look at the visual difference between the two. The new diagram looks much more sleek and professional. The layout is cleaner, the spacing feels more intentional, and the overall presentation is much easier on the eyes. It looks like something you could immediately drop into documentation, a presentation, or a project handoff without needing much extra cleanup.

Overall, this is a really useful skill for developers and teams who want a faster way to create clean, professional-looking architecture diagrams without doing everything manually.

It’s great for documentation, handoffs, and onboarding, and now that the skill is built into Hermes agent, it’s even easier to make it part of your workflow.

References:

[Architecture Diagram Generator](https://github.com/Cocoon-AI/architecture-diagram-generator)

[GBrain by Garry Tan](https://github.com/garrytan/gbrain)

Join 250k+ developers staying ahead in AI. We curate the latest models, repos, and research — so you don’t miss what matters: [AlphaSignal.ai](http://alphasignal.ai/)

---
