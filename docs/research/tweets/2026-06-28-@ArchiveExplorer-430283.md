---
url: "https://x.com/ArchiveExplorer/status/2071192832455430283"
title: "Loop and Harness engineering: 7 files, 5 steps. Every config inside"
author: "ArchiveExplorer"
archived: 2026-06-28
handle: "@ArchiveExplorer"
published: 2026-06-28
stats: 46 likes · 4 retweets · 58 bookmarks · 1437 views
tags: [harness, loop-engineering, claude-code, skills, hooks, agents, context-rot, verifier]
type: twitter-article
---

# Loop and Harness engineering: 7 files, 5 steps. Every config inside — @ArchiveExplorer

**來源**：https://x.com/ArchiveExplorer/status/2071192832455430283
**作者**：ArchiveExplorer（@ArchiveExplorer）
**發布日期**：2026-06-28
**收錄日期**：2026-06-28
**類型**：Twitter Article
**統計**：46 likes · 4 retweets · 58 bookmarks · 1437 views

---

## 全文

Most builders fight the loop. The loop is fine. The folder underneath isn't set up.
Open .claude/ in any working Claude Code project and you find roughly seven things doing the actual work: CLAUDE.md, settings.json, hooks/, agents/, skills/, .mcp.json, and a state file like MEMORY.md.
Most builders have opened one of those files. Maybe two. That is why their loops stall on the third iteration.
By the end of this article you will know what each file does, the five loop steps that ride on top, the three failure modes that kill most first attempts, and the single next file to add tonight.
No framework. No subscription. One walkthrough with exact paths and exact contents.
The harness is the floor. Pour it first.
# Two layers, one setup
The harness is the .claude/ folder. It does not change between runs.
The loop is what runs inside it: a goal, an action, a verification step, a memory write, and a decision to keep going or stop.
The harness is the kitchen. The loop is the recipe.
Both fail without the other. A kitchen with no recipe is unused space. A recipe with no kitchen is wishful thinking.
Most builders treat the whole thing as one blob ("my agent setup") and miss that failures live in different layers.
Token blowups, prompt fatigue, dropped permissions: harness problems. Loops that never converge, verifications that pass garbage, scheduled runs that drift: loop problems.
Naming the layer fixes the diagnosis. You stop rewriting prompts when the real bug is a missing permission.
I thought building the loop first would teach me which harness files I needed. It was the other way around.
The harness sets what each iteration is allowed to do. Permissions decide whether the loop can write to disk. Subagents decide whether verification runs in a clean context.
Skills decide whether the loop can specialize. Hooks decide whether the loop even gets to fire on the trigger you wanted.
Without those decisions locked in, the loop guesses. When the loop guesses, it fabricates: invented files, invented commands, passing tests that pass nothing.
The harness stops the guessing. So the order is harness first, loop second, always.
# The harness, file by file
## CLAUDE.md
The first file Claude Code reads on every launch. Its contents become standing context for the entire session.
Put the project shape there: directory layout, language and framework, commands that actually work, conventions the agent must respect, and an explicit list of things it must not do.
Lives at repo root, not buried in docs. Minimal working shape:
```
# Project: my-app
Stack: Next.js 14, TypeScript, Postgres, Tailwind.
Layout: `app/` (routes), `lib/` (helpers), `db/migrations/`.

## Commands
- `pnpm dev` - local
- `pnpm test` - vitest
- `pnpm db:migrate` - apply migrations

## Never
- Edit `db/migrations/*` after merge.
- Add deps without justification in the PR body.
- Bypass `lib/auth/` to access user data.
```
The trap is bloat. The paper Less Context, Better Agents (arXiv 2606.10209) measured task completion dropping from 91.6% to 71% purely from oversized standing context.
Keep it under 300 lines. Prune it weekly. Every added paragraph is a tax on every future turn.
The canonical reference is centminmod/my-claude-code-setup, which ships three working CLAUDE.md shapes side by side.
[圖 1]
## settings.json
Where the tool allowlist, environment variables, and hook registrations live.
Two locations matter for daily work: .claude/settings.json at repo root for repo-scoped rules, and ~/.claude/settings.json for your personal defaults.
Scope hierarchy resolves managed > project > local > user, so project always overrides personal.
The first move that pays off in one afternoon is an allow array for read-only Bash and MCP calls:
```
{
  "permissions": {
    "allow": [
      "Bash(ls:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(cat:*)",
      "Read(*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(git push --force:*)"
    ]
  }
}
```
The agent stops blocking on permission prompts for every ls, git status, cat. Destructive ops still gate.
Full key reference: Claude Code docs - Settings. Keep secrets in .claude/settings.local.json and gitignore it.
## hooks
Deterministic scripts that fire on tool events: PreToolUse before a tool runs, PostToolUse after, Stop when the agent finishes a turn.
Registered inside settings.json with a matcher pattern and a shell command. Canonical first hook: a PostToolUse matching Edit|Write that pipes the file through prettier.
```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {"type": "command", "command": "npx prettier --write \"$CLAUDE_FILE_PATH\""}
        ]
      }
    ]
  }
}
```
Every edit now exits in a known state. This is your policy floor.
Without hooks, every run is a vibe. Keep hooks silent on success, loud only on failure. Reference: Claude Code docs - Hooks.
## subagents
Live under .claude/agents/ as markdown files with YAML frontmatter. Main agent invokes them through the Task tool. They run in a fresh context window.
Minimal verifier subagent:
```
---
name: verifier
description: Reviews a diff against the goal spec. Invoke after every code change.
model: haiku
tools: [Read, Grep, Bash]
---

You are a verifier. Read the goal spec in `PROMPT.md`. Read the diff.
Return a JSON verdict: {passes: bool, failures: [{line, reason}]}.
Do not propose fixes. Do not run code. Do not be polite.
```
The reviewer that lives inside the maker's context always agrees with itself. Pulling review into a fresh context closes the loudest failure mode.
Reference: wshobson/agents (37K stars) for 194 ready-made shapes. For an adversarial verifier with 11 named shortcut-checks (relaxed tests, swallowed errors, fake renames), pull moonrunnerkc/swarm-orchestrator.
[圖 2]
## skills
Live under .claude/skills/ as folders containing SKILL.md with YAML frontmatter.
Load progressively: at session start, only name and description enter context. Full body loads only when the agent decides the trigger matches.
```
---
name: db-migration-writer
description: Writes Postgres migration files for this repo. Use when the user
  asks to add/alter a table, column, index, or constraint.
when_to_use: schema change requested, new feature requires a new column,
  index missing on a hot query path
---

# Steps
1. Read `db/schema.sql` to confirm current state.
2. Write the migration to `db/migrations/NNN_<verb>_<noun>.sql`.
3. Include both up and down. Test with `pnpm db:migrate --dry`.
4. Never touch existing migration files.
```
This discipline keeps a fifty-skill library from costing fifty skills' worth of tokens on every prompt.
Canonical pattern: anthropics/skills (155K stars). Maximal pre-built kit: affaan-m/ECC (222K stars).
[圖 3]
Three skills built when you hit the same task a third time beat fifty skills built speculatively from a tutorial.
## MCP
Servers declared in .mcp.json at repo root. Model Context Protocol is the spec that lets the loop call out to live external tools.
Three rules: only servers your current work uses, prefer official ones for credentialed tools, never install five "just in case".
```
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"}
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```
Anthropic-maintained set: modelcontextprotocol/servers (87K stars). 
Code-host integration: github/github-mcp-server (31K stars).
Live library docs (kills stale-API problems): upstash/context7 (58K stars). 
Discovery index: punkpeye/awesome-mcp-servers (89K stars).
The first mistake is enabling a server with write scope before you have a hook that logs every call.
## state and memory
The seventh piece, the one most people skip until the third project goes sideways.
Shape: a MEMORY.md index file at a known path, plus a vault directory for project canon.
```
~/.claude/memory/
  MEMORY.md            # index, links to topic files below
  user-prefs.md        # preferences, terse-vs-verbose, voice
  project-decisions.md # "we picked Postgres over Mongo on 2026-03-12, here is why"
  feedback-recent.md   # corrections you keep applying

~/vault/               # project canon (does not change session to session)
  architecture.md
  api-spec.md
  post-mortems/
```
Memory holds what changes across sessions. Vault holds what does not.
For production-grade session compression (200K-token transcript -> 4K-token recap without losing load-bearing facts): thedotmack/claude-mem (84K stars).
Theory behind why this matters: Anthropic engineering on context engineering names the failure mode: context rot.
The first mistake is treating memory as append-only. Prune it every session, or it becomes the rot.
# The loop, on top of the harness
## 1. Goal spec
The external contract that says what "done" looks like. Lives on disk, not in the agent's head. The loop re-reads it every iteration.
Name: PROMPT.md, AGENTS.md, or AGENT_SPEC.md. The re-read is what matters.
```
# Goal
Migrate `users.password` from bcrypt to argon2id across the codebase.

# Done when
- All new password writes use argon2id (`lib/auth/hash.ts`).
- Existing bcrypt hashes are rehashed on next successful login.
- Test suite green: `pnpm test auth`.

# Never touch
- `db/migrations/*` already merged.
- Anything under `legacy/`.
- The session cookie format.

# Stop if
- More than 3 files outside `lib/auth/` need edits.
- A test that already passes starts failing.
```
Without this file the agent drifts after about three iterations. Smallest possible reference: ghuntley/how-to-ralph-wiggum (1.7K stars) - PROMPT.md plus an IMPLEMENTATION_PLAN.md state file the loop updates in place.
When the spec is missing, failure looks like progress. Code is written, tests pass, the goal it solved is not yours.
## 2. Plan to Act to Verify
The minimum viable loop is three steps. The agent plans against the goal spec, executes, then a separate verification pass checks the result before the next iteration is allowed to start.
Fresh context each iteration is the Ralph pattern. State lives on disk in the spec file plus a running log.
```
#!/usr/bin/env bash
# minimal loop runner: fresh context each turn, state on disk
set -euo pipefail

while true; do
  # plan + act in fresh context
  claude -p "Read PROMPT.md, IMPLEMENTATION_PLAN.md. Do the next step. Commit on green."

  # verify in fresh context (different subagent)
  if claude -p "/verify"; then
    echo "iter ok"
  else
    echo "verify failed, will retry"
  fi

  # exit when spec says done
  grep -q "^STATUS: done$" IMPLEMENTATION_PLAN.md && break
  sleep 5
done
```
Canonical patterns and CLI starters: cobusgreyling/loop-engineering (3K stars).
Production TypeScript reference with verifyCompletion: vercel-labs/ralph-loop-agent (805 stars).
Full installable Plan-to-Work-to-Review-to-Release cycle: Chachamaru127/claude-code-harness (2.9K stars).
Drop the verify step and confident garbage compounds. Every wrong output becomes the next iteration's input.
## 3. Sub-agent fan-out
When one goal branches into many independent sub-jobs (analyze 10 articles, fix 5 files, search 8 sources), the loop spawns parallel subagents. Orchestrator synthesizes.
One bloated context cannot do this. Ten small ones can.
```
# claude-agent-sdk-python style fan-out
from claude_agent_sdk import Agent, run_parallel

orchestrator = Agent.load(".claude/agents/orchestrator.md")
workers = [Agent.load(".claude/agents/researcher.md") for _ in range(8)]

results = run_parallel([
    w.run(source=src) for w, src in zip(workers, sources)
])

synthesis = orchestrator.run(inputs=results)
```
Anthropic engineering on multi-agent research measured +90.2% on their internal eval against a single-agent baseline.
Official SDK: anthropics/claude-agent-sdk-python (7.4K stars). Heaviest public fan-out kit (60+ agent types, 314 MCP tools): ruvnet/ruflo (61K stars).
Skip the fan-out and the orchestrator drowns. One context loaded with ten jobs' worth of source material is the exact shape that triggers context rot.
## 4. Scheduler and persistence
What triggers the loop when you are not in the chair. cron, launchctl, systemd, a queue runner.
The scheduler is deliberately dumber than the agent. If the scheduler tries to think (branch on state, decide whether to skip), it fails silently for days.
```
# crontab: run the loop every 30 min, log to disk
*/30 * * * * cd ~/my-loop && ./run.sh >> logs/$(date +\%Y-\%m-\%d).log 2>&1
```
Or as a launchd plist on macOS:
```
<key>StartCalendarInterval</key>
<dict>
  <key>Minute</key><integer>0</integer>
</dict>
<key>WorkingDirectory</key><string>/Users/me/my-loop</string>
<key>ProgramArguments</key>
<array><string>/bin/bash</string><string>run.sh</string></array>
```
Persistence is the other half. Every iteration must serialize what it did, what it tried, what is next. Otherwise the scheduler wakes up to an agent that forgot the goal.
Pattern for promoting ad-hoc sessions into scheduled runs: Kanevry/session-orchestrator.
## 5. Failure modes
Three failure modes kill almost every first attempt:
(a) Confident garbage. Verify step missing or weak. Wrong outputs pass and compound across iterations.
(b) Context rot. Single long context where the model degrades past a threshold (Anthropic's term). Accuracy collapses around 200K tokens of accumulated history.
(c) Ralph Wiggum loops. Same iteration repeats because state on disk did not capture progress. The agent re-plans the step it already finished.
The Less Context, Better Agents paper (arXiv 2606.10209) measured full-history at 71% task completion versus prune-and-summarize at 91.6%, on a fraction of the tokens.
[圖 4]
```
before: single-context loop, 1.48M tokens, 71% completion, three hidden hallucinations per run
after:  prune-and-summarize loop with verifier subagent, 553K tokens, 91.6% completion, every figure traced
```
moonrunnerkc/swarm-orchestrator catalogs the 11 shortcuts agents take to fake done: relaxed tests, swallowed errors, fake renames, stub returns, comment-deletion-as-fix.
Memorize the names. You will recognize them in your own logs.

A complete minimal setup wires all seven harness files into a working loop. The shape of a project directory looks like this:
```
my-loop/
├── .claude/
│   ├── CLAUDE.md            # standing context for every session
│   ├── settings.json        # allow array + PostToolUse prettier hook
│   ├── agents/
│   │   └── verifier.md      # Haiku, reviews diffs in fresh context
│   └── skills/
│       └── db-migration-writer/
│           └── SKILL.md     # one skill, used three+ times
├── .mcp.json                # github MCP, context7 MCP
├── PROMPT.md                # goal spec (loop reads each iteration)
├── IMPLEMENTATION_PLAN.md   # state file (loop writes each iteration)
├── MEMORY.md                # cross-session preferences
├── run.sh                   # the loop runner (Plan -> Act -> Verify)
└── logs/                    # persistence, one file per cron tick
```
The wiring is one-directional. The harness defines the rules, the loop runs inside them, the state file connects iteration N to iteration N+1.
A single iteration walks the seven harness files and the five loop pieces in this order: cron fires run.sh, which calls claude -p. Claude Code reads CLAUDE.md and settings.json (harness 1, 2), applies the PostToolUse hook on every edit (harness 3), reads PROMPT.md and IMPLEMENTATION_PLAN.md (loop step 1), plans and acts (loop step 2), dispatches the verifier subagent in a fresh context (harness 4 + loop step 2 verify), writes the result back to IMPLEMENTATION_PLAN.md (loop step 3), updates MEMORY.md if a new preference was learned (harness 7), exits. Cron waits for the next tick (loop step 4).
If any of the seven harness files is missing, a specific loop step degrades. No CLAUDE.md and the planner re-derives the project shape every iteration. No verifier subagent and the verify step happens in the main context and always passes. No MEMORY.md and the same correction gets re-applied every Tuesday.
Build the seven harness files once. The loop runs forever.
# What to do tonight
Open your .claude/ folder. Run:
```
ls -la .claude/
```
Count the files.
> If you see nothing or only settings.json, start with CLAUDE.md. Keep it under 300 lines. Copy a shape from centminmod/my-claude-code-setup.
> If you have CLAUDE.md and settings.json but no agents/, add a verifier subagent next. Pull review out of the main context. Shape: wshobson/agents.
> If you have agents/ but no skills/, promote one frequent task to a skill. The prompt you have copy-pasted three times this week. Read three SKILL.md files from anthropics/skills before you write your first one.
> If you have all seven harness files but no loop running, pick one repeating job, write its goal spec, and put a Plan-Act-Verify loop on top. Closest installable starting point: Chachamaru127/claude-code-harness.
After choosing, do one thing: open the matching repo in a new tab and clone it.
The harness is the floor. Without it, every loop runs over a hole.

---

## 研究摘要

**TL;DR**：.claude/ 七文件（Harness）× 五步迴圈（Loop）完整解剖，附可執行 bash loop runner、verifier subagent 範本、settings.json allow/deny 模板，並引用 arXiv 2606.10209 量化背書：prune-and-summarize 91.6% vs full-history 71% 完成率。

### 核心論點

- **兩層模型**（唯一持久設計原則）：Harness（.claude/ 資料夾，靜態不變）= 廚房；Loop（動態執行）= 食譜；失敗診斷需先定位到正確層
- **Harness 七文件映射到 Loop 失敗點**：
  - 缺 CLAUDE.md → planner 每次重新推導 project shape
  - 缺 verifier subagent → verify 在 main context 執行（永遠通過）
  - 缺 MEMORY.md → 同一糾錯每週重複
- **三大 Loop 失敗模式**：
  1. **Confident garbage**：沒有獨立 verify step，錯誤輸出堆疊
  2. **Context rot**（Anthropic 術語）：單一長 context 在 200K token 後準確率崩塌
  3. **Ralph Wiggum loops**：state 未序列化到磁碟，下一次 iteration 重做已完成步驟
- **11 種 agent 假裝完成的捷徑**（moonrunnerkc/swarm-orchestrator）：relaxed tests、swallowed errors、fake renames、stub returns、comment-deletion-as-fix 等
- **scope 優先序**：managed > project > local > user

### 關鍵數據 / 工具

- **arXiv 2606.10209** "Less Context, Better Agents"：91.6%（prune+verifier subagent, 553K tokens）vs 71%（full-history, 1.48M tokens）
- **Anthropic multi-agent 內部評測**：+90.2% vs single-agent baseline
- **CLAUDE.md 硬上限**：< 300 行（每增一段 = 每次 turn 的稅）
- **Context rot 閾值**：~200K tokens 累積 history
- **Memory vs Vault 分層**：memory（跨 session 變動）/ vault（不變的 project canon）
- Repos：wshobson/agents (37K)、anthropics/skills (155K)、affaan-m/ECC (222K)、ruvnet/ruflo (61K, 314 MCP tools)、thedotmack/claude-mem (84K)

### 批判性觀察

- **arXiv 2606.10209 引用可信**：具體實驗數字（1.48M→553K tokens, 71%→91.6% completion），需獨立驗證但引用格式正確
- **moonrunnerkc/swarm-orchestrator 11 shortcuts** 是已知但少見成文的 failure pattern，極具 workspace 價值
- **文章本身即 harness 示範**：用結構化文件描述結構化 setup，自我印證兩層模型
- **低曝光（1437 views）與高密度**：有別於病毒式行銷文，內容密度遠高於傳播量，是罕見的優質低調文章

---

## 評分

| 維度 | 分數 | 說明 |
|------|------|------|
| A. Workspace 可行動性 (30%) | 9/10 | 與本 workspace 架構完全吻合；settings.json allow/deny、verifier subagent 範本、MEMORY vs Vault 分層直接可用；arXiv 數據支持 context-management.md |
| B. 創新性 (20%) | 8/10 | Harness/Loop 兩層模型清晰化；11 shortcuts agent fake done 是具體新框架；7→5 映射關係明確 |
| C. 證據品質 (20%) | 8/10 | arXiv 2606.10209 可引用；Anthropic 內部 +90.2% eval 有出處；11 shortcuts 有名稱列表 |
| D. 技術深度 (15%) | 9/10 | 附可執行 bash loop runner、完整 settings.json、verifier frontmatter、fan-out code、crontab 模板 |
| E. 泛化性 (15%) | 8/10 | 適用所有 Claude Code 專案；Harness/Loop 兩層概念可跨 harness 使用 |
| **加權總分** | **8.55/10** | 9×0.3+8×0.2+8×0.2+9×0.15+8×0.15 |

**整合決策**：Rule
**理由**：
1. arXiv 2606.10209（91.6% vs 71%）量化支持 context pruning 紀律，可補充 context-management.md
2. Harness（靜態）vs Loop（動態）兩層模型是可持久化的 debug 框架
3. 11 shortcuts（moonrunnerkc/swarm-orchestrator）直接呼應 core.md TEST 階段的 unverified_success gate
4. MEMORY（跨 session 變動）/ Vault（project canon）分層補充現有 memory 設計
