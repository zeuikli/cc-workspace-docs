# Docker / Devcontainer Sandbox Evaluation
> Benchmark [L] item — 2026-04-30

## Findings

### 1. Official Claude Code Devcontainer Feature

Official feature available: `ghcr.io/anthropics/devcontainer-features/claude-code:1.0`

Installed `.devcontainer/devcontainer.json` with:
- Ubuntu 24.04 base image
- Git, Python 3.12
- Claude Code feature
- `~/.claude` bind-mounted so workspace settings persist in devcontainer
- `postCreateCommand: bash scripts/healthcheck.sh` for environment validation

### 2. Devcontainer vs Sandbox: Key Distinction

| Concern | Devcontainer | Sandbox (`settings.json`) |
|---------|-------------|--------------------------|
| Environment consistency | ✅ Solves | ❌ Not addressed |
| File system isolation | ✅ Container filesystem | ✅ OS-level (bubblewrap/Seatbelt) |
| Network isolation | Partial (Docker bridge) | ✅ Configurable |
| Claude tool sandboxing | ❌ Not addressed | ✅ Direct solution |
| Setup complexity | Medium | Low (1 JSON key) |

**Conclusion**: Devcontainer solves *environment consistency*, not *security isolation*. Real sandboxing of Claude's Bash tool calls requires `"sandbox": {"enabled": true}` in `.claude/settings.json`.

### 3. Sandbox Setting Evaluation

To enable OS-level isolation for all Bash tool calls:
```json
// .claude/settings.json
{
  "sandbox": {
    "enabled": true
  }
}
```

On Linux: uses `bubblewrap` (bwrap) — restricts filesystem, network, process namespaces.  
On macOS: uses `sandbox-exec` (Seatbelt) — policy-based syscall filtering.

**Recommendation**: The devcontainer is useful for consistent onboarding. For production/agentic security, the `sandbox.enabled` setting is the primary control. Not enabling it by default in this workspace because it would block legitimate Bash operations (git, healthcheck) that require host filesystem access.

### 4. Current Workspace Posture

- Sandbox: NOT enabled (intentional — Bash hooks and healthcheck require host filesystem)
- Dangerous command mitigation: `block-dangerous.sh` hook (deny-list approach)
- Environment: Native Linux host (no devcontainer)
- Devcontainer: Available for contributors via `.devcontainer/devcontainer.json`

---

## Update — 2026-05-25

**Current healthcheck status**: PASS 100 / WARN 3 / FAIL 0

Previous pyyaml dependency caused 32 FAIL on systems without pyyaml — fixed in commit 4443da4 by replacing `import yaml` with pure regex-based frontmatter parsing. Healthcheck robustness improved across heterogeneous environments.
