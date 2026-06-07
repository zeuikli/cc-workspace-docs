# ⚖️ AI as Normal Technology — 2026-05-29

> Arvind Narayanan & Sayash Kapoor（普林斯頓）；前身 AI Snake Oil，學術批判視角
> 來源：[AI as Normal Technology](https://www.normaltech.ai/feed)

---

## [Did Google’s AI agents really build an operating system for $916?](https://www.normaltech.ai/p/did-googles-ai-agents-really-build)
*⚖️ AI as Normal Technology | 2026-05-22*

_By Stephan Rabanser, Sayash Kapoor, Rishi Bommasani, Andrew Schwartz, Arvind Narayanan_

At Google's developer conference earlier this week, the company launched its latest model, Gemini 3.5 Flash, alongside a new agent app, Antigravity 2.0. To showcase what this new agent setup is capable of, Google [claimed](https://antigravity.google/blog/google-antigravity-built-an-os) that a team of agents had built an entire operating system. The effort reportedly required only a single prompt, cost only about $900 in API fees, and was carried out by a few dozen subagents working together.

Does this mean that complex pieces of software can now be built cheaply by AI? Not so fast:

  * **The "single prompt" claim is misleading. **The blog post says the operating system was built from a single prompt. But halfway through the post, Google discloses that the prompt "ended up being many thousands of lines" long. How many attempts did it take to generate the prompt? How specific were the instructions to the agent? Without these critical details, it is hard to know if the secret sauce is a better model or just more effort put into prompting the model. Moreover, the run was carried out on a scaffold[1](https://www.normaltech.ai/feed#footnote-1) with specialized roles, delegation to subagents, and an agent to detect and prevent cheating. In the launch post, Google views the scaffold as a product feature. But we don't know whether the scaffold was overfit to this task of building an operating system from scratch, or whether it would perform as well on other complex software engineering tasks.

  * **Google 's writeup is not explicit about what counted as human intervention. **The post mentions that the final run to develop the operating system required "no additional guidance or corrections from a human." But it does not define that standard. It describes infrastructure to kill and restart stuck agents. The post mentions an earlier run in which the agents appeared to cheat, after which the team added anti-cheating measures and re-ran the task. But it does not report dry runs as part of the methodology. Nor does it clearly say whether any agents escalated to a human, whether the final run required any manual restarts, approvals, or fixes, or how many retries it took until the agent was successful.

  * **The writeup does not report any attempt to analyze whether the agents wrote the code from scratch or copied existing code from the internet.** To Google's credit, the blog post notes that toy operating systems are common undergraduate course projects, and public implementations are easy to find. The post itself raises the concern that the agent could have regurgitated information rather than building the operating system from scratch. But it did not address this concern--there was no similarity analysis or log analysis to check if the agent copied existing code. Even if there was no direct copying, writing an operating system might be relatively easy for agents because of patterns memorized in the training data, so this doesn't tell us much about agents' ability to create _novel_ pieces of software.

  * **Google has not released the lengthy prompt, the code the agents wrote, or the logs from the run, which makes it impossible to independently evaluate the claims.** Releasing the source code or the agent logs could have allowed independent researchers to evaluate the quality of the artifacts and answer questions such as whether the agent was copying existing code. The blog post only includes a short video documenting a snapshot of the development progress and the overall narrative of the experiment.




On the other hand, the blog post does report the exact dollar amount for building the operating system ($916.92), alongside the total token budget (a total of 2.6B tokens). These figures provide useful context, which we want to credit Google for. Many of the evaluations we previously surveyed did not disclose cost at all, which made their headline claims hard to compare with other evaluations.

Still, Google's blog post is effectively a press release. We recognize that it is unrealistic to expect it to be scientifically rigorous. Evaluations like this one, meaning a long-horizon real-world task evaluated on a single run with the experimenter narrating what the agent did, have become common. Since many of them have been done by AI companies, it is easy to dismiss the entire genre as puffery.

But that would be a mistake. We refer to the emerging paradigm as _open-world evaluations_ , and we recognize this trend in a recent [paper](https://cruxevals.com/open-world-evaluations.pdf) (and an accompanying [blog post](https://www.normaltech.ai/p/open-world-evaluations-for-measuring)). Crucially, we argue that open-world evaluations require a new set of methodological norms. Done right, they can provide a valuable perspective that benchmark-based evaluation cannot.

Google's experiment does add to the mounting evidence that agents or agent teams can autonomously or near-autonomously work on certain kinds of tasks for very long periods of time, making progress without getting stuck or confused. As we argue in our paper, benchmark evaluation is effectively impossible for this kind of task for many reasons including cost. So it is an exciting time for independent evaluators from academia, nonprofits, and government to step in and provide the kind of rigor and credibility to open-world evaluations that are unlikely to be found in AI vendors' own claims.

Analysis and commentary based on the "_AI as Normal Technology " _framework

[1](https://www.normaltech.ai/feed#footnote-anchor-1)

A scaffold is the layer of code, prompts, and tooling built around an AI model that gives it the ability to act autonomously, handling things like memory, tool access, and the ability to interact with its environment. For example, Claude Code is the scaffold that allows Anthropic's Claude models to act as coding agents.

---
