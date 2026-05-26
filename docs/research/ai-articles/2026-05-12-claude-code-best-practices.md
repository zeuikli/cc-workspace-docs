---
title: Claude Code Best Practices
url: "https://code.claude.com/docs/en/best-practices"
domain: code.claude.com
fetched: 2026-05-12
source_tier: O
---

# Best practices for Claude Code

Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel sessions.

Claude Code is an agentic coding environment. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely.

This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements.

## Key Principles

### 1. Give Claude a way to verify its work
Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do.

Claude performs dramatically better when it can verify its own work, like run tests, compare screenshots, and validate outputs. Without clear success criteria, it might produce something that looks right but actually doesn't work.

**Strategies:**
- Provide verification criteria with test cases
- Verify UI changes visually with screenshots
- Address root causes, not symptoms
- Use Claude in Chrome extension for UI testing

### 2. Explore first, then plan, then code
Separate research and planning from implementation to avoid solving the wrong problem.

**Recommended workflow:**
1. **Explore** (plan mode): Claude reads files and answers questions without making changes
2. **Plan**: Ask Claude to create a detailed implementation plan
3. **Implement**: Switch out of plan mode and let Claude code
4. **Commit**: Ask Claude to commit with a descriptive message and create a PR

Plan mode is most useful when uncertain about approach, modifying multiple files, or unfamiliar with code.

### 3. Provide specific context in your prompts
The more precise your instructions, the fewer corrections you'll need.

**Best practices:**
- Scope the task: specify file, scenario, and testing preferences
- Point to sources: direct Claude to files that can answer questions
- Reference existing patterns: point to patterns in the codebase to follow
- Describe the symptom: provide context, location, and what "fixed" looks like
- Use rich content: reference files with `@`, paste images, pipe data

### 4. Configure your environment
- **Write an effective CLAUDE.md**: Include bash commands, code style, and workflow rules
- **Configure permissions**: Use auto mode, permission allowlists, or sandboxing
- **Use CLI tools**: Configure `gh`, `aws`, `gcloud`, etc.
- **Connect MCP servers**: Link external tools (Notion, Figma, databases)
- **Set up hooks**: Run scripts automatically at specific workflow points
- **Create skills**: Add domain knowledge in `.claude/skills/`
- **Create subagents**: Define specialized assistants in `.claude/agents/`

## Communication Strategies

- Ask codebase questions like you would ask a senior engineer
- Let Claude interview you for larger features using AskUserQuestion
- Use narrow, scoped investigations or delegate research to subagents

## Session Management

- **Course-correct early**: Use `Esc` to stop, `/rewind` to restore, `/clear` between unrelated tasks
- **Manage context aggressively**: Run `/clear` frequently, use `/compact` for control, use `/btw` for quick questions
- **Use subagents for investigation**: Delegate research to separate context to keep main conversation clean
- **Rewind with checkpoints**: Every action creates a checkpoint; restore at any time
- **Resume conversations**: Use `/rename` to name sessions; pick up with `--continue` or `--resume`

## Scaling Patterns

- **Run non-interactive mode**: Use `claude -p "prompt"` in CI, pre-commit hooks, or scripts
- **Run multiple sessions in parallel**: Use worktrees, desktop app, cloud infrastructure, or agent teams
- **Fan out across files**: Loop through tasks with `claude -p` for batch operations
- **Run autonomously with auto mode**: Use classifier for uninterrupted execution with background safety checks

## Common Failure Patterns to Avoid

1. **The kitchen sink session**: Context fills with irrelevant information from multiple unrelated tasks
   - Fix: `/clear` between unrelated tasks
2. **Correcting over and over**: Context polluted with failed approaches
   - Fix: After two failed corrections, `/clear` and write a better initial prompt
3. **The over-specified CLAUDE.md**: Important rules get lost in noise
   - Fix: Ruthlessly prune unnecessary content
4. **The trust-then-verify gap**: Plausible implementation without edge case handling
   - Fix: Always provide verification (tests, scripts, screenshots)
5. **The infinite exploration**: Context fills with hundreds of files without scope
   - Fix: Scope investigations narrowly or use subagents

## Context Window Management

Most best practices are based on one constraint: **Claude's context window fills up fast, and performance degrades as it fills.**

The context window holds entire conversations including every message, every file Claude reads, and every command output. Performance degrades as context fills. The context window is the most important resource to manage.

## Key Takeaway

The way you communicate with Claude Code significantly impacts the quality of results. Develop your intuition about when to be specific vs. open-ended, when to plan vs. explore, and when to clear context vs. let it accumulate.

