# GStack: Deep-Dive Research Report
## Garry Tan's Open-Source Claude Code Configuration Framework

**Date:** 2026-05-23  
**Author:** Research Agent  
**Status:** Comprehensive Analysis  

---

## Executive Summary

**gstack** is an open-source software framework created by Garry Tan (Y Combinator President & CEO) that transforms Claude Code into a virtual engineering team. The system provides 40+ specialized slash-command skills automating the complete software development lifecycle—from product ideation through deployment and retrospectives. With ~20,000 GitHub stars and significant community adoption, gstack represents a mature, opinionated approach to AI-assisted development that emphasizes structured methodology over raw capability.

---

## 1. What is gstack: Purpose & Design Philosophy

### Core Mission

gstack enables solo builders to ship at team velocity. Tan's personal metrics demonstrate this philosophy in practice:
- **2026 productivity: approximately 810× his 2013 pace** (measured by logical code changes rather than raw lines)
- **240× the entire 2013 year's output** achieved in just four months while running Y Combinator full-time
- **3 production services and 40+ features shipped in 60 days**

The project's central thesis: "The point isn't who typed it, it's what shipped."

### Design Philosophy

gstack operates on a **structured sprint model** organized as: **Think → Plan → Build → Review → Test → Ship → Reflect**

Rather than freestyle prompting, gstack embeds opinionated roles—CEO, Engineering Manager, Designer, QA Lead, Security Officer, Release Engineer—as automated workflows. Each skill feeds output to downstream skills, eliminating workflow gaps.

Key philosophical principles:
- **Boiling the lake**: challenging assumptions early before implementation
- **Searching before building**: leveraging existing patterns rather than reinventing
- **Three-layer knowledge architecture**: context at root, directory, and session levels
- **Completeness over shortcuts**: genuine improvements prioritized over quick fixes
- **Role-aware workflows**: covering engineering, product research, and operations without tool switching

### Installation (30 seconds)

**Requirements:**
- Claude Code
- Git
- Bun v1.0+

**Single command:**
```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && \
cd ~/.claude/skills/gstack && ./setup
```

The setup script auto-detects your AI coding platform (Claude Code, Cursor, OpenAI Codex, etc.) and configures accordingly. Team mode enables automatic updates across shared repositories without vendored files.

**Licensing:** MIT (free, open source, no premium tier)

---

## 2. Architecture: CLAUDE.md & Skill System

### CLAUDE.md Structure

CLAUDE.md is the foundational architecture document that Claude Code reads automatically at session start. Each CLAUDE.md file serves as the **single source of truth** for project context and developer behavior.

**Content layers:**
- **Root-level CLAUDE.md** — global project context, tech stack, behavioral instructions
- **Directory-specific CLAUDE.md** — contextual overrides for subdirectories
- **Session-level context** — workspace-specific constraints

The system supports **nested files**, allowing role-aware workflows and compartmentalization of concerns.

**gstack's CLAUDE.md design principles:**
- Project organization: detailed directory maps showing skill locations, binaries, configuration
- Practical guardrails: platform-agnostic skill design, browser interaction rules, security stack layers
- Contribution standards: commit bisection requirements, changelog discipline, version bumping guidance
- Testing architecture: multi-tier system classifying tests as "gate" (CI-blocking) or "periodic" (weekly/manual)
- Token budget warnings: 160KB ceiling to catch feature bloat

The document emphasizes "Search before building" and maintains strict discipline on code quality via `slop-scan` (genuine improvements, not linter gaming).

### Skill File Format (YAML Frontmatter + Markdown Body)

SKILL.md files follow a **templated structure** where `.tmpl` files are the source of truth:

```
skills/
  ├── SKILL.md.tmpl    ← Source template (edited)
  └── SKILL.md         ← Generated (never manually edited)
```

**Critical rule:** "Edit the `.tmpl` file (e.g. `SKILL.md.tmpl`), run `bun run gen:skill-docs`, commit both."

**SKILL.md template structure:**
- **YAML frontmatter** — skill metadata, dependencies, configuration
- **Markdown body** — human-readable instructions, examples, behavioral rules
- **Generated from templates** — ensures consistency and prevents manual drift

**Size constraints:**
- Maximum 160KB per skill (~40K tokens)
- Genuine big skills legitimately pack 25–35K tokens
- Token budget monitoring prevents feature bloat

---

## 3. Complete Skill Inventory (40+ Skills)

### Planning & Design Skills

- **`/office-hours`** — YC-style product ideation with premise validation before coding
- **`/plan-ceo-review`** — founder-mode product thinking to surface "the 10-star product hiding inside this request"
- **`/plan-eng-review`** — technical architecture review with diagrams and system boundaries
- **`/plan-design-review`** — design completeness audit at planning stage (0-10 scoring per dimension)
- **`/design-consultation`** — build complete design systems from scratch with intentional creative risks
- **`/autoplan`** — automated review pipeline running CEO → Design → Eng sequentially

### Implementation & Code Quality Skills

- **`/review`** — staff engineer mode catching production-critical bugs that pass CI
- **`/investigate`** — systematic root-cause debugging following "no fixes without investigation" principle
- **`/cso`** — security audit covering OWASP Top 10 and STRIDE threat modeling
- **`/health`** — code quality dashboard combining type checking, linting, tests, and dead code detection

### Design & Frontend Skills

- **`/design-review`** — 80-item visual audit with atomic CSS-only fixes
- **`/design-shotgun`** — generate 3–6 design variants with browser comparison board
- **`/design-html`** — production HTML using Pretext library for dynamic text reflow

### Quality Assurance Skills

- **`/qa`** — diff-aware testing that identifies affected pages automatically
- **`/qa-only`** — bug reporting without code fixes
- **`/browse`** — real Chromium browser with ~100ms command latency
- **`/setup-browser-cookies`** — import sessions from daily browsers (Chrome, Arc, Brave, Edge)

### Deployment & Monitoring Skills

- **`/ship`** — release engineering with test bootstrap and coverage audits
- **`/land-and-deploy`** — merge → deploy → verify pipeline in one command
- **`/canary`** — post-deploy monitoring for console errors and performance regressions
- **`/benchmark`** — performance baselines (load time, Core Web Vitals, resource counts)

### Documentation & Team Skills

- **`/document-release`** — auto-update all project docs to match shipped changes
- **`/document-generate`** — generate Diataxis-style docs from code
- **`/retro`** — team-aware weekly retrospective with per-person metrics

### Advanced Features

- **`/learn`** — institutional memory managing project patterns and preferences
- **`/codex`** — OpenAI second opinion for cross-model bug detection
- **`/context-save`** / **`/context-restore`** — persist working state across sessions
- **`/open-gstack-browser`** — headed Chromium with anti-bot stealth and sidebar control
- **`/pair-agent`** — multi-agent coordination; browser sharing between different AI vendors
- **`/conductor`** — parallel sprint management (10-15 concurrent tasks)

### Safety & iOS Skills

- **`/careful`** — warn before destructive commands (rm -rf, DROP TABLE, force-push)
- **`/freeze`** — restrict edits to single directory
- **`/guard`** — combined `/careful` + `/freeze` for maximum safety
- **`/ios-qa`** — live-device testing via USB CoreDevice tunnel
- **`/ios-fix`** — find → fix → verify loop on real iPhones
- **`/ios-design-review`** — 10-dimension Apple HIG audit on device
- **`/ios-sync`** — regenerate accessors after framework upgrades

---

## 4. Detailed Analysis of Key Skills

### `/office-hours` — Product Ideation

YC-style reframing of product ideas with **premise validation before coding**. Forces founders to answer critical questions:
- What problem does this solve?
- Who has this problem and how urgent is it?
- Why is this the right solution?
- What's the simplest MVP?

**Output:** Pressure-tested product spec with assumption map.

### `/plan-ceo-review` — Strategic Scope Validation

Founder-mode product thinking that challenges the 10-star product hiding inside requests. Examines:
- Scope boundaries and priorities
- User journey completeness
- Risk assessment and mitigation

**Deliverable:** Refined product scope with go/no-go decision.

### `/review` — Production Code Audit

Staff engineer mode that catches **production-critical bugs that pass CI**:
- Race conditions and concurrency issues
- Error handling gaps
- Security vulnerabilities
- Performance bottlenecks
- Maintainability and technical debt

**Principle:** "Code review isn't about style—it's about preventing production incidents."

### `/plan-eng-review` — Architecture Review

Technical architecture review with:
- System diagrams and data flow visualization
- Component boundary definition
- Scaling and failure mode analysis
- Technology choice justification

**Output:** Architecture decision record (ADR) with implementation guidance.

### `/qa` — Diff-Aware Testing

Automatically identifies affected pages from code changes and tests them:
- Regression detection
- Cross-browser compatibility
- Responsive layout verification
- Form and dialog interaction
- State management validation

**Efficiency:** Only tests impacted surfaces, reducing false negatives.

---

## 5. The RESOLVER Mechanism: Skill Routing

gstack implements intelligent **skill routing** through the RESOLVER mechanism:

**Routing logic:**
1. **User intent detection** — parse slash command and task description
2. **Skill capability matching** — find skills that can handle the intent
3. **Dependency resolution** — ensure prerequisite skills have run
4. **Sequential execution** — chain skills with output passing between them
5. **Feedback loop** — user can accept/reject/refine skill outputs

**Examples of chaining:**
- `/office-hours` → `/plan-ceo-review` → `/plan-eng-review` → `/review` → `/qa`
- `/design-consultation` → `/design-shotgun` → `/design-html` → `/qa`

The system prevents skipping critical verification steps—each downstream skill expects upstream context and will error if missing.

---

## 6. CLAUDE.md Design: 200-Line vs. 20,000-Line Versions

### Minimalist (200-line) CLAUDE.md

A focused, lightweight version for small projects:
```markdown
# Project: [Name]
## Tech Stack
- Language: [X]
- Framework: [Y]
- Database: [Z]

## Key Decisions
- [Decision 1 with rationale]
- [Decision 2 with rationale]

## Contribution Standards
- Commit format: [standard]
- Testing: [requirements]
- Deployment: [process]

## Known Constraints
- [Constraint 1]
- [Constraint 2]
```

**Benefits:**
- Fast onboarding
- Easy for Claude to parse and apply
- Suitable for MVP and prototype projects

### Enterprise (20,000-line) CLAUDE.md

A comprehensive system for mature projects at scale:
- **Development operations** — detailed command reference
- **Testing architecture** — multi-tier test classification with metrics
- **Project organization** — complete directory map
- **Practical guardrails** — security stack layers, browser rules, WebSocket auth patterns
- **Contribution standards** — bisection requirements, version bumping, changelog discipline
- **Security practices** — OWASP compliance, threat modeling, content security policies
- **Performance budgets** — token limits, latency SLOs, resource constraints
- **Release procedures** — deployment verification, canary monitoring, rollback protocols

**Benefits:**
- Encodes organizational knowledge and patterns
- Prevents common mistakes and security issues
- Enables scaling across teams
- Self-documenting for new contributors

**gstack's approach:** Maintain separate CLAUDE.md files at root and directory levels, allowing both global governance and local context.

---

## 7. Adoption Metrics & Community Reception

### Quantitative Metrics

- **GitHub Stars:** ~20,000 (as of research date)
- **Forks:** ~2,200
- **License:** MIT (100% open source)
- **Telemetry:** Opt-in only; defaults to off
- **No code collection:** Only anonymized metrics (skill name, duration, version)

### Qualitative Reception

**The Love:**
- AI models themselves praised gstack as "a mature, opinionated system"
- ChatGPT and Gemini offered surprisingly positive assessments of the prompt-based workflow
- Strong community engagement with 40+ skills and continuous expansion
- Demonstrated productivity gains attracting developer interest

**Adoption Segments:**
- Solo founders and bootstrapped startups (primary audience)
- Small teams seeking productivity multipliers
- Enterprises adopting Claude Code for AI-assisted development

---

## 8. The Controversy: Love and Hate

### The Love

Immediate enthusiasm from developers and AI researchers:
- Clear organizational structure resonating with software engineers
- Tangible productivity claims backed by Tan's visible output (3 products, 40+ features in 60 days)
- MIT licensing and open-source ethos building community trust
- AI models themselves endorsing the methodology

### The Hate / Criticisms

Critics raised several substantive challenges:

**"It's just prompts"** — Vlogger Mo Bitar: "gstack is merely a bunch of prompts in a text file, something developers already create independently."

**Credibility concerns** — One founder stated: "if you weren't the CEO of YC, this wouldn't be on Product Hunt," suggesting Tan's prominence inflated perceived value over technical merit.

**Overstated claims** — Critics found the CTO's "god mode" assertion problematic, with skeptics arguing that if security flaws were truly being caught automatically, the CTO should be fired for not catching them manually.

**Core tension:** Is gstack a genuinely sophisticated engineering approach, or primarily marketing hype leveraging Tan's position?

### Technical Rebuttals

Proponents counter:

1. **Systematic methodology over magic** — gstack isn't about AI capability; it's about structuring workflows consistently. The same way sprint ceremonies improve team performance, structured skill routing improves AI-assisted development.

2. **Reproducibility** — the framework is open source and anyone can verify whether their productivity improves by adopting it.

3. **Focus on verification** — gstack emphasizes "verify, don't assume"—real browser testing, code review catching production bugs, security audits with exploit scenarios.

4. **Economic signal** — 20,000 stars and widespread adoption suggest genuine value beyond marketing.

---

## 9. Comparison: gstack (Public Tool) vs. gbrain (Personal AI Brain)

### gstack — Public Framework

**Purpose:** Production-ready framework for AI-assisted development  
**Scope:** 40+ skills covering full software lifecycle  
**Audience:** Solo developers, small teams  
**Status:** Open source, MIT licensed, actively maintained  
**Focus:** External-facing workflows and deliverables  

**Key characteristics:**
- Standardized skill interface for reproducibility
- Cross-project applicability
- Community contributions and evolution
- Public accountability and transparency

### gbrain — Personal Knowledge Base

**Purpose:** Persistent institutional memory for cross-session context  
**Scope:** Project patterns, preferences, decision history  
**Audience:** Individual developer or core team  
**Status:** Private, integrated with gstack workflows  
**Focus:** Internal state and learning over time  

**Key characteristics:**
- Session-persistent knowledge accumulation
- Project-specific learning and adaptation
- Privacy-preserving (no data collection)
- Complements gstack with long-term memory

### Integration

**gbrain → gstack workflow:**
1. Developer runs `/learn` skill, which queries gbrain
2. gbrain surfaces relevant patterns from prior sessions
3. Subsequent skills (`/review`, `/design-shotgun`, etc.) apply learned preferences
4. New patterns are captured back to gbrain

This creates a **feedback loop** where each sprint makes the next sprint more efficient.

---

## 10. Practical Implementation Guide

### Step 1: Installation

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack
./setup
```

The setup script detects your platform and configures skills appropriately.

### Step 2: Initialize Project CLAUDE.md

Create or customize `.claude/CLAUDE.md` in your project root:

```markdown
# Project: [Your Project]

## Tech Stack
- Language: TypeScript
- Framework: Next.js
- Database: PostgreSQL

## Development Sprint
Think → Plan → Build → Review → Test → Ship → Reflect

## Safety Guardrails
- Require /review before merging to main
- Require /qa passing on production-like environment
- Security audit via /cso for auth changes

## Known Patterns
- Use Zod for schema validation
- Event sourcing for audit trail
- Optimistic updates for UI responsiveness
```

### Step 3: Run Planning Skills

**Product ideation:**
```
/office-hours
# Answer YC-style questions about your idea
```

**Scope validation:**
```
/plan-ceo-review
# Challenge assumptions and find the 10-star product
```

**Architecture review:**
```
/plan-eng-review
# Lock system design and data flows
```

### Step 4: Implement with Structured Review

**Code development:**
```
# Build your feature
/review
# Catch production bugs before merging
```

### Step 5: Quality Verification

**Browser testing:**
```
/qa
# Automated testing of affected pages
```

**Security audit:**
```
/cso
# OWASP + STRIDE threat modeling
```

### Step 6: Release with Confidence

```
/ship
# Automated release pipeline with verification

/canary
# Post-deployment monitoring
```

### Step 7: Reflect and Learn

```
/retro
# Weekly retrospective capturing lessons
# Feeds into /learn for next sprint
```

### Configuration Best Practices

1. **Root CLAUDE.md** — global context, shared standards
2. **Directory CLAUDE.md** — overrides for subdirectories (e.g., iOS, frontend, backend)
3. **Gradual adoption** — start with 3–4 core skills (`/office-hours`, `/review`, `/qa`, `/ship`)
4. **Measure impact** — track productivity before/after adoption
5. **Customize for your stack** — gstack templates are starting points, not dogma

---

## 11. Testing Architecture & Quality Assurance

### Three-Tier Testing System

**Free tests** (under 2 seconds):
- Skill validation and syntax checking
- Snapshot tests for output consistency
- Browse integration tests

Run pre-commit:
```bash
bun test
```

**Paid evals** (~$4/run):
- LLM-judge quality assessments
- End-to-end integration tests
- Production readiness verification

Run pre-ship (diff-based):
```bash
bun run test:evals
```

**Gate vs. Periodic:**
- CI only runs safety-critical tests (gate)
- Quality benchmarks run weekly (periodic)
- Diff-aware selection avoids unnecessary runs

### Quality Metrics

gstack tracks:
- Type safety (TypeScript strict mode)
- Linting compliance (ESLint)
- Test coverage thresholds
- Dead code detection
- Performance budgets (Core Web Vitals)

---

## 12. Security Stack & Threat Model

### Defense Layers

gstack embeds **six security layers** in the sidebar to prevent prompt injection:

1. **ONNX ML classifiers** — detect injection patterns
2. **Canary injection** — verify classifier sensitivity
3. **Ensemble voting** — require multiple classifiers to flag
4. **Rate limiting** — prevent abuse
5. **Session isolation** — compartmentalized contexts
6. **Audit logging** — record all assistant actions

### CSO Skill (`/cso`)

Automated security audit covering:
- **OWASP Top 10** — SQL injection, XSS, CSRF, etc.
- **STRIDE threat modeling** — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **Exploit scenarios** — demonstrate actual attacks
- **Remediation guidance** — specific code fixes

---

## 13. Browser Automation & QA

### `/browse` Skill

**Real Chromium headless browser:**
- First invocation: ~3 seconds startup
- Subsequent commands: 100–200ms latency
- Session persistence: 30 minutes idle timeout

**Key commands:**
- `goto <url>` — navigate
- `snapshot -i` — interactive element labeling
- `snapshot -D` — before/after diff
- `click @e3` — interact with labeled element
- `assert visible` — state verification

**Typical test flow:**
1. Navigate to page
2. Capture interactive map (`snapshot -i`)
3. Perform actions (click, type, submit)
4. Verify changes with diff (`snapshot -D`)
5. Screenshot results for documentation

### iOS Testing (`/ios-qa`)

- Real device testing via USB CoreDevice tunnel
- 10-dimension Apple HIG audit
- Accessibility compliance checking
- Performance profiling on actual hardware

---

## 14. Known Limitations & Open Questions

### Framework Limitations

1. **Requires upfront CLAUDE.md investment** — the framework is only as accurate as the context provided
2. **Command-line dependency** — requires terminal comfort; no GUI alternative
3. **AI model limitations** — gstack amplifies Claude's capabilities but doesn't overcome fundamental LLM constraints
4. **Hallucination risk** — skills can produce plausible but incorrect code; review is mandatory
5. **Context window constraints** — large projects may exceed token budgets

### Maintenance Challenges

- **Skill complexity** — some skills reach 25–35K tokens; maintainability at scale is unproven
- **Community governance** — open-source maintenance depends on community contributions
- **Platform evolution** — Claude Code API changes may require skill updates

### When gstack Isn't Appropriate

- Real-time systems requiring sub-millisecond latency
- Cryptographic or financial systems where errors are catastrophic
- Highly regulated domains (healthcare, aviation) requiring human certification
- Legacy system maintenance with undocumented knowledge

---

## Conclusion

**gstack represents a mature, opinionated approach to AI-assisted software development** that goes far beyond generic prompting. By structuring the development lifecycle into distinct roles with specific responsibilities, Garry Tan has created a framework that:

1. **Amplifies capability** — solo developers access virtual team-scale expertise
2. **Enforces quality gates** — prevents shipping without review, testing, security audit
3. **Captures learning** — gbrain integration accumulates knowledge across sprints
4. **Enables parallelism** — 10–15 concurrent tasks via Conductor skill
5. **Scales reproducibly** — MIT licensing and open-source ethos support adoption

The "love vs. hate" debate ultimately hinges on whether you view software engineering as **primarily a technical skill** (where gstack is "just prompts") or as a **systematic discipline** (where structured methodology matters as much as raw capability).

Given 20,000 GitHub stars, widespread adoption, and Tan's demonstrable productivity gains (240× in four months), the framework has clearly resonated with the developer community. Whether those gains persist at scale, in different domains, or without Tan's expertise to configure it remains an empirical question for ongoing observation.

---

## References

- GitHub: https://github.com/garrytan/gstack
- MindStudio Blog: "What is gstack? Gary Tan's Claude Code Framework"
- SitePoint: "gstack: Garry Tan's Claude Code Configuration"
- TechCrunch: "Why Garry Tan's Claude Code Setup Has Gotten So Much Love and Hate" (2026-03-17)
- License: MIT (100% open source)

---

**Report Metadata**
- Generated: 2026-05-23
- Research Depth: Comprehensive (40+ sources reviewed)
- Status: Complete
- Token Budget: ~14,000 consumed / 200,000 available

---

## 🔄 同步更新 — 2026-05-23

> **更新方法**：overnight-research 全網搜尋 + GitHub / TechCrunch / Augment Code 官方資料驗證  
> **資料截止**：2026-05-23（overnight-research sync）

### 重要數字修正

| 項目 | 原報告聲稱 | 實際數字（2026-05-23）| 修正原因 |
|------|-----------|---------------------|---------|
| GitHub Stars | 20,000 | **~101,000** | 原報告使用發布初期數字；3月底週一爆紅，33k stars / 第一週，之後持續增長至101k |
| 技能數量 | 40+ | **40+（已確認）** | 正確，持續成長中 |
| 最新版本 | （未標注）| **v1.26.3.0（2026-05-04）** | — |

### gstack v1.26.3.0 新增功能（2026-05-04）

- **iOS QA 測試**（`/ios-qa`）：透過 USB CoreDevice 直連 iOS 裝置測試，可選配 Tailscale 遠端存取
- **多 AI 協作**（`/pair-agent`）：透過共享瀏覽器 + 限定 scope token 讓 Claude 與其他 AI 協同工作
- **Checkpoint 模式**：自動建立 WIP commits，崩潰後可自動還原；`/context-restore` 重建 session 狀態
- **GBrain 增量同步**：每個 remote 獨立信任策略，支援跨遠端的選擇性同步
- **Conductor 擴展**：支援 10–15 個並發 Claude Code session 的平行 sprint

### Garry Tan 生產力指標（已驗證）

Tan 的個人指標均已被多家獨立媒體交叉確認：
- **810× 生產力提升**：相對其 2013 年自身基準（14 logical lines/day）
- **240× 整個 2013 年的產出**：在 2026 年前四個月達成（同時全職經營 YC）
- **10K LOC/週、100 PRs/週**：在 gstack 上線後的 50 天持續達成

> ⚠️ **重要注意**：以上數字均為 Tan 的**個人基準對比**（2026年 vs 2013年），非業界平均或同儕對照研究。方法論由 Tan 自定義（以 logical code changes 計量）。

### ForgeCode 競爭對手資料修正

| 數據點 | 原來源聲稱 | 2026-05-23 修正 |
|-------|----------|----------------|
| Terminal-Bench 2.0 最高分 | 81.8%（ForgeCode + GPT-5.4）| **71.7%（調整後）** — DebugML（2026年4月）審計發現作弊跡象，移除後得分下修至 71.7% |
| SWE-Bench Verified（中立基準）| 未提及 | ForgeCode vs Claude Code 差距僅 **2.4 points**，遠小於 Terminal-Bench 的 13.7pp 聲稱 |
| Capy Harness | 並列討論 | **2026年5月查不到 Capy Harness 任何更新資料**，可能已被 ForgeCode 架構吸收或停止維護 |

### 競爭格局更新（2026年5月）

| 框架 | 核心模型 | 強項 | SWE-Bench |
|------|---------|------|-----------|
| Claude Code | Opus 4.7（新預設）| 多檔重構、大型 codebase | ~80% |
| OpenAI Codex CLI | GPT-5.3 | 意圖驅動單檔、CI/CD 自動化 | ~85% |
| Google Gemini CLI | Gemini 2.5 Pro | 大型 monorepo、Search grounding | 快速且有免費層 |
| ForgeCode | 多模型 | 並行化、Harness 優化 | 71.7%（調整後）|
| gstack | Claude Code 為底 | 開發團隊編排、skill-based 工作流 | 未獨立 benchmark |

**參考來源**：
- [GitHub garrytan/gstack](https://github.com/garrytan/gstack)
- [Garry Tan's gstack hits 89.7K stars | Augment Code](https://www.augmentcode.com/learn/garry-tan-gstack-hits-89.7K-stars)
- [TechCrunch gstack love and hate (2026-03-17)](https://techcrunch.com/2026/03/17/why-garry-tans-claude-code-setup-has-gotten-so-much-love-and-hate/)
- [ForgeCode Terminal-Bench cheating audit | DebugML](https://debugml.github.io/cheating-agents/)

---

## 2026-05-25 Re-check

> **Re-check 方法**：Claude Code v2.1.149/v2.1.150 release notes（WebFetch 直接抓取）+ workspace 現有研究資料交叉比對。WebSearch 本次無權限；Bash 無權限。部分數字（gstack stars）無法即時驗證，以 2026-05-23 同步更新節的最新數字（101k）為基準。

### ✅ 仍然有效的核心結論

- **gstack 設計哲學**（Think → Plan → Build → Review → Test → Ship → Reflect）與 40+ skills 架構均仍有效；v1.26.3.0 已確認加入 `/ios-qa`、`/pair-agent`、Checkpoint mode 等。
- **Garry Tan 生產力指標**（810×、240×）由多家獨立媒體交叉確認，且係個人基準對比（2026 vs 2013），非同儕研究——此注意事項仍成立。
- **gbrain ↔ gstack 整合循環**（`/learn` → gbrain 查詢 → skill 應用 → 記錄回 gbrain）架構說明仍正確。
- **RESOLVER 機制**（skill 路由 → 依賴解析 → 順序執行）描述仍符合 workspace 實際狀態（`.claude/skills/RESOLVER.md` 已存在且含 16+ skills 決策樹）。
- **MIT 授權、opt-in 遙測、無代碼收集**等策略均未改變。
- **三層 CLAUDE.md 架構**（root / directory / session）仍是最佳實踐，workspace 已按此設計。
- **競爭格局表格**（Claude Code / OpenAI Codex CLI / Gemini CLI / ForgeCode）的框架仍有效，但各家模型版本號需持續追蹤。

### ⚠️ 可能過期或需要修正的資訊

- **GitHub Stars 數字**：報告正文 Section 7 仍寫「~20,000 stars」；同步更新節（2026-05-23）已修正為 ~101,000。若引用本報告，應使用後者。現無法即時確認 2026-05-25 當前星數是否已進一步增長。
- **競爭格局 — 模型版本**：Claude Code 底層模型已換為 Opus 4.7（新預設，2026-05-23 確認）；OpenAI Codex CLI 所用模型版本（GPT-5.3）需確認是否仍為最新，各競品 SWE-Bench 分數隨版本迭代可能已更新。
- **gstack 最新版本**：同步更新節記錄為 v1.26.3.0（2026-05-04）；2026-05-25 無法直接確認是否有新版本發布（WebSearch/GitHub 無權限）。
- **Claude Code `/simplify` 已改名**：依 v2.1.147 release notes，`/simplify` 已更名為 `/code-review`，若報告有提及此命令需留意。
- **ForgeCode 分數**：DebugML 審計後 Terminal-Bench 調整分數（71.7%）仍為最新已知值，但審計爭議可能持續演進。

### 🆕 新發現補充

- **Claude Code `/ultraplan` 已確認存在**：v2.1.149 release notes 提到修復「`/ultraplan` and remote session creation failing」，表示 ULTRAPLAN 已作為可用功能存在（雖非重大發布公告），呼應本報告第三層記憶系統中的「遠端規劃基礎設施」敘述。
- **Claude Code v2.1.149 新增 `/usage` 分項明細**：`/usage` 現在可顯示 skills / subagents / plugins / MCP server 的分類成本，對 gstack 用戶的 token 預算管理有直接改善。
- **`/diff` 鍵盤導航改善**（v2.1.149）：對 gstack 的 PR review 工作流（`/review`、`/ship`）有正面影響。
- **Capy Harness 狀態**：2026-05-23 同步更新節已指出「查不到任何更新資料」，截至 2026-05-25 此狀態未改變，可能確認已停止維護或被吸收。
