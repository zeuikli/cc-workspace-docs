# Context Window Management

## Prompt Caching Core Principles (Static First)

- CLAUDE.md content = most stable cache prefix, always placed first, never moved. block-level `<!-- -->` injection stripped before injecting = zero-token maintenance notes.
- **Mid-session prohibited**: ① switching models ② adding/removing tools ③ modifying CLAUDE.md → wait until session ends.
- **NLAH principle**: Right context > more context. A precise hint injected at the correct position can reduce 95% of tokens; context should be at HEAD (original goal) or TAIL (latest tool output); middle layer holds dynamic state, avoid static descriptions there.

## Compact hint

`/compact preserve: task goal, most recent tool results (incl. full file path and error string verbatim, do not rewrite), safety red lines, conventions, Traditional Chinese output; discard: intermediate step details, superseded exploration paths`

- **Post-compact self-check** (see refs/post-compact-checklist.md): ① Is the task goal still present? ② Are safety red lines still present? ③ Are the most recent tool results undistorted? Any failure → `/rewind`.

## Monitoring

- `/usage` to view real-time session token/cost.
- **Cache health metrics** (see refs/cache-health-metrics.md): `cache_hit_rate = cache_read / input_tokens`, long-running sessions should be > 0.7; sudden drop → first check if model/tool/CLAUDE.md was changed mid-session (four major cache-breaking sources). Dynamic information injected via `<system-reminder>`, do not write into CLAUDE.md prefix.
- **Hard Token Budget** (cross-cutting discipline: prevent loop runaway):
  - Per-task budget: **4,000 tokens** (single task limit)
  - Per-session budget: **30,000 tokens** (entire session limit)
  - Action: approaching budget → `/compact <hint>`; exceeded → `/clear` to start new session
- **Compact triggers** (priority: behavioral signal > numeric threshold):
  1. **Behavioral signal**: Model produces "please provide more context" / "what do you want to do?" lost-questions → immediately `/rewind` or `/compact`
  2. **Numeric threshold**: general tasks **70%**; beginners ~**60%**; long agentic **30–35%** proactive compact
- `/compact <hint>` to continue task; `/clear` to switch tasks.
- **PreCompact hook**: `exit 2` can completely block compact (protect important uncommitted decisions).
