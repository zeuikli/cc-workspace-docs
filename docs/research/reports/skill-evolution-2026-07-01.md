# Skill Evolution Report: media-research

**Date**: 2026-07-01  
**Target**: `media-research`  
**Trigger**: usage=8, refinement_count=0 (flagged by skill-scan)  
**Stage**: stable  
**SKILL.md version**: 1.2.0

---

## Quality Assessment

### Strengths

- Rich GOTCHAS coverage (23 entries) covering platform-specific edge cases
- Multi-platform routing table (Twitter/X, YouTube, GitHub, Substack, Medium, Generic Paywall)
- Well-structured fallback chains for Twitter (4-tier) and Medium (4 paths)
- Detailed Playwright + Apollo State + GraphQL interception techniques
- Invidious API workaround for YouTube cloud IP block documented in GOTCHAS

### Identified Gaps

#### Gap 1: Missing routing row for Generic Paywall Bypass [HIGH]

**Problem**: The quick route table (§快速路由表) has 6 rows but no entry for FT/WSJ/NYT/Economist/Bloomberg URLs. Users don't know to scroll to `§ Generic Paywall Bypass` for these.  
**Fix**: Add routing row:
```
| FT / WSJ / NYT / Bloomberg URL | media:paywall、paywall bypass、繞過付費牆、財經文章 | [§ Generic Paywall Bypass] |
```

#### Gap 2: YouTube cloud IP block not surfaced in SKILL.md [HIGH]

**Problem**: The YouTube section in SKILL.md describes a nominal flow (yt-dlp → VTT → archive), but the most common failure mode in cloud sessions — YouTube blocking all cloud IPs (429/403) — is only documented in `youtube-GOTCHAS.md`. Users hitting this waste time on retries before discovering the Invidious API workaround.  
**Fix**: Add a **Known Failure** callout to the YouTube section:

```markdown
**⚠️ 雲端 IP 封鎖（Step 2 常見失敗）**：YouTube 封鎖所有雲端出口 IP（429 字幕 / 403 音訊）。
Fallback 優先序：① Invidious API `https://inv.nadeko.net/api/v1/captions/{ID}?lang=en` →
② metadata-only 歸檔（加 `## 待辦` 標記）。詳見 `references/youtube-GOTCHAS.md §HTTP 429/403`。
```

#### Gap 3: G23 residual METADATA.json commit reminder not in SKILL.md [MEDIUM]

**Problem**: G23 documents that METADATA.json is left uncommitted after SKILL runs, but SKILL.md has no reminder at the final step (Step 9 / Step 10) to check `git status` and commit residual hook-maintained files.  
**Fix**: Add to Step 9/10 summary line in YouTube and Twitter sections:

```markdown
**完成後**：執行 `git status --short`；若有 `METADATA.json` 或其他 hook 維護檔案未提交 → 一併 commit（G23）。
```

#### Gap 4: Thread Research fallback URLs include year-hardcoded 2026 [LOW]

**Problem**: `references/SKILL.md §Thread 文章索引追蹤 §層 2` has hardcoded `2026` in search queries (`"{user} thread articles 2026 site:x.com"`). This will produce stale results next year without any update.  
**Fix**: Change to dynamic year or remove year from search query pattern.

---

## Proposed SKILL.md Diff (Summary)

1. **Route table** (line 22): add `media:paywall` row after Medium row
2. **YouTube section** (after line 114): add ⚠️ cloud IP block callout with Invidious first-step
3. **Thread search** (line 76–77): replace `2026` with `{current_year}` or remove year constraint

---

## METADATA.json Recommended Updates

```json
{
  "refinement_count": 1,
  "last_reviewed": "2026-07-01",
  "evolution_stage": "stable"
}
```

---

## Action Items for Next Evolution Cycle

- [ ] Apply Gap 1 fix (routing table paywall row)
- [ ] Apply Gap 2 fix (YouTube cloud IP warning in SKILL.md)
- [ ] Apply Gap 3 fix (G23 reminder in final steps)
- [ ] Apply Gap 4 fix (remove hardcoded year from thread search queries)
- [ ] Verify Invidious instance `inv.nadeko.net` still operational (check fallback list)
