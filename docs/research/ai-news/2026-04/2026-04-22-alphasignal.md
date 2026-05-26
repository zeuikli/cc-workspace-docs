---
title: AlphaSignal — 2026-04-22
date: 2026-04-22
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-04-22

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [Karpathy-Inspired CLAUDE.md. How to Add It to Any Project in 30 Seconds](https://alphasignalai.substack.com/p/karpathy-inspired-claudemd-how-to)
*📡 AlphaSignal | 2026-04-22*

A developer packaged Andrej Karpathy’s three complaints about AI coding agents into a 65-line file.

It’s #1 on the “Weekly Coding AI Leaderboard” crossing 71,000 stars (from 39,000 last 15th April). Currently ranked #337 globally.

The repo is [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills), authored by Forrest Chang. Karpathy did not write it. He published a January 26, 2026 X post naming specific LLM coding failure modes, Chang built the file that addresses them directly.

Repo Snapshot

What Karpathy said

In his January 26, [2026 X post](https://x.com/karpathy/status/2015883857489522876), Karpathy described what he encountered after shifting from 80% manual coding with autocomplete to 80% agent-driven coding in roughly two months. Three failure modes came up repeatedly. The quotes below are reproduced from the repo’s README which is from Andrej’s post.

Silent wrong assumptions. “The models make wrong assumptions on your behalf and just run along with them without checking. They don’t manage their confusion, don’t seek clarifications, don’t surface inconsistencies, don’t present tradeoffs, don’t push back when they should.”

Over-complication. “They really like to overcomplicate code and APIs, bloat abstractions, don’t clean up dead code... implement a bloated construction over 1000 lines when 100 would do.”

Orthogonal damage. “They still sometimes change/remove comments and code they don’t sufficiently understand as side effects, even if orthogonal to the task.”

A fourth observation from the same post supplied the final principle. “LLMs are exceptionally good at looping until they meet specific goals... Don’t tell it what to do, give it success criteria and watch it go.”

The four principles

CLAUDE.md is 65 lines with no executable code. When Claude Code reads it at session start, it treats the contents as behavioral context for the entire conversation. Each section maps directly to one of the failure modes above.

1. Think before coding

Rule: “Don’t assume. Don’t hide confusion. Surface tradeoffs.”

This principle targets silent wrong assumptions. Before implementing anything, the model is instructed to state its assumptions explicitly, present multiple interpretations when ambiguity exists, and stop to ask when something is unclear rather than picking silently.

EXAMPLES.md shows what unconstrained behavior looks like: a user requests “Add a feature to export user data.” The model writes a function that exports all users in JSON and CSV, assumes a file location, picks which fields to include, and sets fieldnames without checking the data structure. Under the principle, the model lists four questions before writing a line: scope (all users or a filtered subset?), format (browser download, background job, or API endpoint?), which fields may be sensitive, and expected data volume. Code follows the answers, not the request.

The self-test from the file: if uncertain, ask if multiple interpretations exist, present them rather than picking silently.

2. Simplicity first

Rule: “Minimum code that solves the problem. Nothing speculative.”

Overcomplication is the direct target. The file names what is off-limits: features beyond what was asked, abstractions for single-use code, configurability that was not requested, error handling for scenarios that cannot occur. The built-in check: “Would a senior engineer say this is overcomplicated? If yes, simplify.”

EXAMPLES.md shows the gap precisely. A user asks for “a function to calculate discount.” The unconstrained model produces a DiscountStrategy abstract class, PercentageDiscount and FixedDiscount subclasses, a DiscountConfig dataclass, and a DiscountCalculator class requiring more than 30 lines of setup to run a single calculation. The principle-compliant response:

def calculate_discount(amount: float, percent: float) -> float:
return amount * (percent / 100)

The comment in the file: “When to add complexity: only when you actually need it. If that requirement comes later, refactor then.”

3. Surgical changes

Rule: “Touch only what you must. Clean up only your own mess.”

The failure mode addressed here is orthogonal damage. When editing existing code, the model is told not to improve adjacent code, comments, or formatting, not to refactor code that is not broken and to match existing style even when it would approach the problem differently. The test: “Every changed line should trace directly to the user’s request.”

The cleanup scope is precise. If the model’s own changes leave unused imports or orphaned variables, it removes them. Pre-existing dead code gets mentioned, not deleted.

EXAMPLES.md shows a user asking to fix the bug where empty emails crash the validator. The unconstrained model reformats quote style, adds type hints, adds a docstring, and introduces username length and alphanumeric validation nobody requested. The compliant diff touches two lines: the ones that handle the empty string case.

4. Goal-driven execution

Rule: “Define success criteria. Loop until verified.”

This principle captures the fourth Karpathy observation. The model is instructed to transform imperative tasks into verifiable goals before starting. “Fix the bug” becomes “Write a test that reproduces it, then make it pass.” “Refactor X” becomes “Ensure tests pass before and after.” For multi-step tasks, the file specifies a plan format:

1. [Step] → verify: [check]

2. [Step] → verify: [check]

3. [Step] → verify: [check]

The contrast in EXAMPLES.md: a user asks to “fix the authentication system.” The unconstrained model says it will review the code, identify issues, make improvements, and test the changes, then proceeds to make unverifiable changes. The principle-compliant response asks what specific issue is being solved, writes a failing test that reproduces it, makes the test pass, and verifies no regressions. Strong success criteria let the model loop without constant clarification, weak criteria (”make it work”) require intervention at every step.

How to get started

Per-project install (under 30 seconds)

For a new project:

curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md

To append to an existing CLAUDE.md:

echo "" >> CLAUDE.md && curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md

This is the method the title refers to. The file becomes part of that project only. Claude Code reads it at session start as behavioral context for every conversation in that directory.

For any other tools like OpenCode/Hermes, rename it to AGENTS.md.

Plugin install (cross-project)

Two commands install the skill across all projects at once, not just the current one:

/plugin marketplace add forrestchang/andrej-karpathy-skills

/plugin install andrej-karpathy-skills@karpathy-skills

The repo is structured as a Claude Code marketplace plugin, not just a raw file. The architecture behind this: .claude-plugin/plugin.json declares the plugin name, version, author (forrestchang), and a pointer to ./skills/karpathy-guidelines. That directory contains SKILL.md, the full principle text that the Claude Code plugin system exposes as an active skill.

Unlike the curl method, the plugin is active in every project without copying any files. The plugin takes slightly longer than curl to set up, but removes per-project file management across any number of repositories. If Chang updates the guidelines, one update command applies to all projects.

Cursor setup

The repo includes .cursor/rules/karpathy-guidelines.mdc with alwaysApply: true. Copy that file to any Cursor project’s .cursor/rules/ directory to apply the same principles there. Cursor does not read .claude-plugin/ directories or CLAUDE.md files by default, the .mdc file is the Cursor-native format. Teams using both tools must maintain the rules in two places. The repo’s CURSOR.md documents this tradeoff explicitly.

Limitations

No enforcement. The file is behavioral context, not code. No mechanism exists to verify that a principle fired on any given request. A developer cannot test whether Principle 1 applied to a specific interaction.

Caution over speed. The README states explicitly that these guidelines bias toward caution. For high-volume simple tasks, such as batch typo fixes or single-line corrections, the clarification requests generated may produce more friction than value. Use judgment.

Attribution confusion. Secondary coverage routinely describes the file as “Karpathy’s CLAUDE.md.” Karpathy did not write it and has not publicly endorsed it. Expectations about endorsement, updates, or ongoing support based on that misattribution are unsupported.

AlphaSignal Take

Worth Watching

This is not Production Ready. The behavioral layer has no enforcement mechanism, the principles influence outputs but do not guarantee them. No benchmark data exists from the repo itself. Secondary coverage has circulated accuracy improvement claims with undisclosed methodology, those numbers should not be cited.

It is not a Skip. The adoption signal is observable and traces to a specific, documented problem Karpathy named: 71,000 stars, 9,263 on launch day, jumped from 39k stars past 15th April. MIT license. Under 30 seconds to try via curl. The cost of testing it is genuinely low.

Who benefits most: developers doing non-trivial work with Claude Code where a bad silent assumption produces a full rewrite. For simple one-line fixes, the clarification behavior this file generates adds friction, not value.

Links

[forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

Follow [@AlphaSignalAI](https://x.com/@AlphaSignalAI) for more content like this.

Check out [AlphaSignal.ai](https://alphasignal.ai/) to get a daily summary of top models, repos, and papers in AI. Read by 280,000+ devs.

Questions?

Does Andrej Karpathy use or endorse this file? No. Forrest Chang authored it, inspired by Karpathy’s January 26, 2026 X post on LLM coding pitfalls. Karpathy has not publicly endorsed the repo.

Does it work with Cursor? Yes. Copy .cursor/rules/karpathy-guidelines.mdc from the repo to any Cursor project’s .cursor/rules/ directory. The principles are identical across both tools, only the file format differs.

Will Claude always follow these guidelines? No. The file is behavioral context. It influences model outputs, it cannot enforce them. There is no mechanism to verify that a given principle applied to a specific request.

Join 250k+ developers staying ahead in AI. We curate the latest models, repos, and research — so you don’t miss what matters: [AlphaSignal.ai](http://alphasignal.ai/)

---
