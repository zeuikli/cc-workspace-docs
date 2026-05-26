# Career Wiki — Operation Log

> **Pattern**: Karpathy LLM Wiki — append-only chronological record
> **Format prefix**: `[INGEST]` / `[QUERY]` / `[LINT]` / `[EVOLVE]`
> **Consumer**: `wiki-ingest.py`, `wiki-lint.sh`, `/autoresearch:wiki`
> **Never delete entries** — this is a log, not a note

---

## [LINT] 2026-05-25 — Weekly Lint

- Scope: 37 pages in `pages/`
- Lint score: 98/100 ✅ PASS (target ≥ 85)
- Top issues: (1) `pages/README.md` missing `## Concrete Numbers` section; (2) `pages/README.md` orphan (not referenced in INDEX.md); (3) 36 pages missing or malformed `Last ingested` header
- Stale candidates (⏳ > 60 days): none — all ⏳ pages (mysql-redis-cluster-ha, kernel-tuning-mmorpg, haproxy-patterns, stripe-serverless-fintech) created 2026-04-21, 34 days ago, not yet past threshold
- By: autonomous wiki-maintenance agent [auto]

---

## [EVOLVE] 2026-05-25 — GBrain + Hermes Architecture Update

- Action: workspace-level gap analysis against Karpathy LLM Wiki / GBrain / Hermes Agent
- Outcome: LOG.md created (Karpathy pattern completeness), brain-first-protocol.md added to refs, typed edges added to RESEARCH-INDEX.md, Hermes telemetry fields added to all METADATA.json
- By: claude/workspace-architecture-update-M6mXu (overnight-research pipeline)
- Ref: `research/reports/2026-05-25-workspace-gbrain-hermes-update.md`

---

## [LINT] 2026-05-08 — Session 9 Full Lint

- Scope: all 36 pages in `pages/`
- Result: pages within size limit: 36/36; concrete numbers: 32/36; stale (>90d): 0/36
- Lint score: 92/100 ✅ PASS
- Issues: 4 pages missing `## Concrete Numbers` section (haproxy-patterns, kernel-tuning-mmorpg, stripe-serverless-fintech, mysql-redis-cluster-ha — all ⏳ status)
- By: `/autoresearch:wiki lint`

---

## [INGEST] 2026-05-08 — Session 9 Ingest

- Sources: `raw/career-summary.md` updates (CathaySec 6 new project areas)
- Pages created: none new
- Pages updated: `cathaysec-lessons.md` (6 new domains), all 8 company-lessons pages (year confirmation, technical detail補齊)
- By: `/autoresearch:wiki` Session 9

---

## [INGEST] 2026-04-25 — Session 8 — agentic-architecture-patterns

- Sources: forward-looking AI/agent patterns, CathaySec 2024–now context
- Pages created: `agentic-architecture-patterns.md`
- Pages updated: `karpathy-ai-orchestration.md` (cross-referenced)
- By: `/autoresearch:wiki` Session 8

---

## [INGEST] 2026-04-22 — Session 7 — karpathy-ai-orchestration

- Sources: Karpathy AI orchestration context, CathaySec current work
- Pages created: `karpathy-ai-orchestration.md`
- By: `/autoresearch:wiki` Session 7

---

## [INGEST] 2026-04-22 — Session 6 — Resolve security & IaC

- Sources: `raw/career-summary.md` (Resolve 段落)
- Pages created: `linux-ad-integration.md`, `terraform-enterprise-fdo.md`, `ansible-gha-automation.md` (updated with CIS benchmarks)
- By: `/autoresearch:wiki` Session 6

---

## [INGEST] 2026-04-22 — Session 5 — KKStream FinOps deep dive

- Sources: `raw/career-summary.md` (KKStream 段落)
- Pages created: `aws-alarm-as-code.md`, `live-streaming-capacity-planning.md`
- Pages updated: `finops-savings-plans-roi.md`, `finops-cross-position-patterns.md`, `aws-step-functions-patterns.md`
- By: `/autoresearch:wiki` Session 5

---

## [INGEST] 2026-04-22 — Session 4 — GCP deep dive (CathaySec)

- Sources: `raw/career-summary.md` (CathaySec 段落)
- Pages created: `gcp-terraform-iac-patterns.md`
- Pages updated: `gcp-landing-zone.md` (深度更新), `gcp-monitoring-alerting.md`
- By: `/autoresearch:wiki` Session 4

---

## [INGEST] 2026-04-21 — Sessions 2–3 — Bulk ingest (8 company-lessons + domain pages)

- Sources: `raw/career-summary.md`, `raw/medium-blog-index.md`
- Pages created: 8 company-lessons pages (gamania/htc/spq/kkstream/soundon/次蘋/resolve/cathaysec), plus domain pages: postgres-microsec-tuning, vmware-nsx-security-zone, cdn-cache-tuning-97pct, high-traffic-media-arch, kafka-confluent-streaming, terraform-multi-cloud, aws-sa-pro-prep
- By: `/autoresearch:wiki` Sessions 2–3

---

## [INGEST] 2026-04-21 — Session 1 — Pilot ingest

- Sources: `raw/career-summary.md` v1
- Pages created: `redis-pg-zero-downtime.md` (pilot), `iso27017-audit.md` (pilot)
- Index initialized
- By: `/autoresearch:wiki` Session 1 pilot
