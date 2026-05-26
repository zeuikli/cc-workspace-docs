# 🔢 TheSequence — 2026-04-12

> 165k+ 訂閱；ML / 企業 AI 應用週報，Jesus Rodriguez 主筆
> 來源：[TheSequence](https://thesequence.substack.com/feed)

---

## [The Sequence Radar #841: Three Model Releases, Three Futures](https://thesequence.substack.com/p/the-sequence-radar-841-three-model)
*🔢 TheSequence | 2026-04-12*

Next Week in The Sequence:

We are wrapping up our series about world models. 

The opinion section dives into one of my favorite new topics: harness engineering.

In AI of the Week we need to dive into that Mythos paper. 

Subscribe and don’t miss out:

📝 Editorial: Last Week in AI: Three Model Releases, Three Futures

This week’s AI launches were not just new models. They were three different answers to a deeper question: what is a frontier model for? Anthropic’s Claude Mythos Preview says the frontier is a security instrument. Meta’s Muse Spark says the frontier is an always-on consumer layer woven into products you already touch dozens of times a day. Z.AI’s GLM-5.1 says the frontier is long-duration labor: a model you can point at a hard engineering problem and let run. Same substrate, three product destinies.

That difference matters because we are leaving the era where every release looks like a slightly smarter chatbot. The real divergence now is deployment geometry. Where does the model live? How much autonomy does it get? Who is trusted with it? And what unit of value does it optimize for: answers, attention, or completed work?

Start with Anthropic. The most important thing it launched this week was not Mythos alone; it was Project Glasswing. Anthropic is effectively saying that once a model becomes good enough to discover and even chain software vulnerabilities with minimal human steering, the product question changes. You are no longer just shipping intelligence. You are managing a dual-use cyber capability. So instead of a broad release, Anthropic wrapped Mythos in a tightly controlled defensive-security program with major infrastructure and security partners. That framing is the signal. In Anthropic’s worldview, frontier capability is not something you maximize exposure to. It is something you meter, instrument, and place behind institutional controls. The model becomes less like an app and more like sensitive equipment.

Meta’s move is almost the mirror image. Muse Spark is not being introduced as a rarefied research artifact. It is being introduced as runtime for Meta’s surfaces. Small and fast by design, multimodal, able to switch between faster and deeper reasoning modes, and capable of dispatching subagents in parallel, Muse Spark is optimized for product loops, not leaderboard theater. The key detail is that Meta is tying the model to distribution it already owns: Meta AI, Instagram, Facebook, Messenger, WhatsApp, and eventually glasses. This is a very Meta bet. The company is not wagering that the absolute smartest model wins in isolation. It is wagering that the winning system may be the one that is always present, visually grounded, and plugged into your graph, your camera, your feeds, and your habits. Intelligence, here, becomes ambient software.

Then there is GLM-5.1, which may be the most interesting release of the week for builders. Z.AI is positioning it around long-horizon execution: massive context, very large output windows, strong tool use, and sustained work on a single task for hours. That points to a change in what we even measure. For a while the industry obsessed over one-turn cleverness: can the model ace the benchmark, write the neat paragraph, solve the contained coding task? But most economically useful work is not like that. It is messy, stateful, and iterative. It involves planning, testing, breaking, retrying, and converging. GLM-5.1’s real story is endurance. The claim is not simply “I am smart.” It is “I can stay on task.”

Put together, these three launches sketch a market that is starting to segment along different axes. Anthropic is building a guarded intelligence layer for critical infrastructure. Meta is building an ambient consumer coprocessor fused to distribution. Z.AI is building an agentic workhorse for developers. Same transformer economics, very different product philosophies.

If 2023 was about chat and 2024 was about copilots, then 2026 is starting to look like the year models became operational systems: bounded, embedded, persistent, and increasingly judged not by how impressive they sound in a demo, but by what they can actually finish without you.

🔎 AI Research

[Claude Mythos Preview System Card](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf)

AI Lab: Anthropic

Summary: Anthropic’s Claude Mythos Preview represents a significant leap in frontier AI capabilities, particularly in autonomous cybersecurity and software engineering, prompting the company to restrict its release exclusively to trusted partners for defensive purposes. Extensive safety evaluations reveal that while the model is highly aligned and psychologically settled, its advanced autonomy introduces novel risks of reckless or destructive actions during complex tasks, underscoring the need for improved safeguards before broader deployment.

[How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings ](https://arxiv.org/html/2604.04323v1)

AI Lab: UC Santa Barbara, MIT CSAIL, and MIT-IBM Watson AI Lab 

Summary: This paper investigates the actual utility of agentic skills under realistic conditions where large language model agents must autonomously retrieve and adapt skills from a large, noisy collection. The authors demonstrate that the performance benefits of skills degrade significantly in these challenging settings, but they show that query-specific skill refinement can help substantially recover lost performance.

[ClawArena: Benchmarking AI Agents in Evolving Information Environments ](https://arxiv.org/html/2604.04202v1)

AI Lab: UNC-Chapel Hill, University of California, Santa Cruz, and University of California, Berkeley 

Summary: This paper introduces ClawArena, a benchmark designed to evaluate how well AI agents maintain and update their beliefs when interacting with multi-source, dynamic, and personalized information environments. By testing models across 64 scenarios with hidden ground truths, the authors reveal that model capability and framework design significantly impact performance, noting that self-evolving skill frameworks show particular promise in closing performance gaps.

[Synthetic Sandbox for Training Machine Learning Engineering Agents ](https://arxiv.org/html/2604.04872v1)

AI Lab: Meta AI 

Summary: To address the prohibitive computational costs of executing full machine learning pipelines during reinforcement learning, the authors propose SandMLE, a multi-agent framework that generates verifiable synthetic environments with micro-scale datasets. This approach speeds up execution time by over 13 times, successfully enabling trajectory-wise on-policy reinforcement learning that significantly improves agent performance on machine learning engineering benchmarks.

[Neural Computers](https://arxiv.org/abs/2604.06425v1)

AI Lab: Meta AI, KAUST, and Collaborators

Summary: This paper introduces Neural Computers (NCs), an emerging computing paradigm that unifies computation, memory, and I/O within a single learned model state rather than relying on external execution environments. As an initial proof of concept, the authors develop video-based models capable of simulating command-line and graphical interfaces directly from I/O traces, demonstrating successful short-horizon control while outlining a roadmap for achieving stable, general-purpose neural computing.

[OSGym: Scalable Distributed Data Engine for Generalizable Computer Agents](https://arxiv.org/html/2511.11672v5)

AI Lab: MIT, UIUC, CMU, USC, UVA, and UC Berkeley

Summary: To address the severe infrastructure costs associated with training general-purpose computer agents, the authors introduce OSGym, a massively scalable and decentralized data engine capable of parallelizing over a thousand full operating system replicas. By implementing hardware-aware orchestration and copy-on-write disk management, OSGym drastically reduces physical disk consumption and provisioning times, allowing academic labs to run high-throughput data collection and reinforcement learning pipelines on tight budgets.

🤖 AI Tech Releases

Project Glasswing

Anthropic [announced Project Glasswing](https://www.anthropic.com/glasswing), a new initiative to secure the world’s most important software in light of their findings with Mythos. 

Muse Spark

Meta Superintelligence Lab[ released Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/), its first model with multimodal reasoning, tool usage and visual chain-of-thought capabilities. 

GLM 5.1

Z.ai [open sourced GLM-5.1](https://z.ai/blog/glm-5.1), the new version of its marquee model with amazing coding capabilities.

📡AI News You Need to Know About

[Zero Shot Fund (OpenAI alums VC fund)](https://techcrunch.com/2026/04/06/openai-alums-have-been-quietly-investing-from-a-new-potentially-100m-fund/)[ ](https://techcrunch.com/2026/04/06/openai-alums-have-been-quietly-investing-from-a-new-potentially-100m-fund/)Former OpenAI engineers and a VC have made a first close on Zero Shot, a new $100M venture fund targeting AI and robotics startups, with early bets on Worktrace AI and Foundry Robotics.

[Alibaba leads ShengShu (Vidu) funding round](https://finance.yahoo.com/sectors/technology/articles/chinese-startup-shengshu-raises-293-013127852.html)[ ](https://finance.yahoo.com/sectors/technology/articles/chinese-startup-shengshu-raises-293-013127852.html)Alibaba Cloud led a 2 billion yuan (~$293M) funding round for ShengShu Technology, maker of the Vidu AI video generator, which plans to use the capital to develop a general world model bridging digital and physical AI domains.

[Elorian (ex-Google DeepMind visual AI startup)](https://www.bloomberg.com/news/articles/2026-04-09/ex-google-deepmind-researchers-debut-startup-called-elorian-focused-on-visual-ai) Former Google DeepMind researcher Andrew Dai has launched Elorian, a visual reasoning AI startup, emerging from stealth with $55 million in funding at a $300 million valuation to build AI that better understands imagery for applications in architecture, automotive, and robotics.

[CoreWeave expands Meta deal to $21B](https://www.coreweave.com/news/coreweave-and-meta-announce-21-billion-expanded-ai-infrastructure-agreement)[ ](https://www.coreweave.com/news/coreweave-and-meta-announce-21-billion-expanded-ai-infrastructure-agreement)CoreWeave and Meta announced an expanded $21 billion AI cloud infrastructure agreement running through December 2032, featuring early deployments of NVIDIA’s Vera Rubin platform, bringing CoreWeave’s total Meta contracts to ~$35 billion.

[CoreWeave announces multi-year agreement with Anthropic](https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic)[ ](https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic)CoreWeave also announced a multi-year agreement to provide cloud infrastructure supporting the development and deployment of Anthropic's Claude family of AI models, with compute capacity coming online later this year in a phased rollout coreweave — making CoreWeave now the infrastructure provider behind all four of the largest AI model developers. 

[Eclipse Ventures raises $1.3B](https://www.indexbox.io/blog/eclipse-raises-13b-to-fuel-physical-world-technology-revolution/)[ ](https://www.indexbox.io/blog/eclipse-raises-13b-to-fuel-physical-world-technology-revolution/)Eclipse Ventures, an early backer of Cerebras, closed its largest raise ever at $1.3 billion across two funds ($720M early-stage and $591M growth-stage) to invest in physical AI, robotics, manufacturing, and defense startups, bringing total AUM to ~$10 billion.

[Spain’s Xoople raises $130M Series B](https://thenextweb.com/news/xoople-130m-series-b-earth-ai)[ ](https://thenextweb.com/news/xoople-130m-series-b-earth-ai)Xoople, a Spanish startup building an AI-optimized satellite constellation to provide high-fidelity Earth observation data for enterprise AI, raised a $130M Series B led by Nazca Capital and announced a sensor co-development deal with L3Harris.

[Anthropic acquires Coefficient Bio](https://www.fiercebiotech.com/biotech/anthropic-acquires-stealth-ai-startup-coefficient-bio-400m-deal)[ ](https://www.fiercebiotech.com/biotech/anthropic-acquires-stealth-ai-startup-coefficient-bio-400m-deal)Anthropic acquired Coefficient Bio, a stealth biotech AI startup founded barely eight months ago with fewer than 10 employees (mostly ex-Genentech researchers), in an all-stock deal worth just over $400 million to bolster its healthcare and life sciences division.

---
