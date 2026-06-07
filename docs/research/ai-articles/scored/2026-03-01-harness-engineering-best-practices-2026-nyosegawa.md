> Source: https://nyosegawa.com/en/posts/harness-engineering-best-practices-2026/
> Fetched: 2026-05-08

# Harness Engineering Best Practices for Claude Code / Codex Users, Explained Plainly

## Introduction

Harness engineering represents the systems and tools that enable coding agents to operate autonomously with minimal human oversight. Rather than focusing on model capabilities alone, this comprehensive guide emphasizes that "the system, not the model, is what matters."

## What is Harness Engineering?

Harness engineering encompasses continuous improvement of agent instruction files and the toolchain enabling self-verification. The field exists to stabilize agent output and maintain autonomous operation. As noted in the original definition by Mitchell Hashimoto, this involves both human-driven AGENTS.md refinement and automated quality verification systems.

The guide acknowledges this field may have limited longevity—perhaps a few months to a year before LLM improvements reduce the need for such extensive scaffolding. However, for March 2026, it remains essential.

## Core Principles

### 1. Repository Hygiene: Design for Rot

Agents treat all repository text equally, lacking intuition about document staleness. This necessitates careful curation of what lives in version control.

**What belongs in repos:**
- Executable artifacts (code, tests, linter configs, type definitions)
- Architecture Decision Records (ADRs) with timestamps and status tracking

**What doesn't belong:**
- Prose explanations of current system state
- Handwritten API descriptions
- Textual architecture overviews

Tests provide superior resilience compared to documentation. When specifications become tests, they fail loudly upon breaking rather than rotting silently. This principle demands higher test coverage in agent-assisted development than human-only scenarios.

ADRs work well because their immutable structure—with explicit timestamps and status fields—allows agents to structurally determine currency. A superseded ADR remains identifiable through metadata rather than requiring subjective judgment.

### 2. Enforce Quality with Deterministic Tools and Architectural Guardrails

**Core principle:** "LLMs are expensive and slow compared to traditional linters and formatters. Whenever a deterministic tool can do the job, use it."

This represents perhaps the most important distinction between prompt-based instruction and mechanical enforcement. Writing "run the linter" in CLAUDE.md differs fundamentally from executing linters through automated hooks—the former achieves success "almost every time," while the latter ensures compliance "every time without exception."

#### Hooks System

Claude Code Hooks are shell commands or prompts executing automatically at specific lifecycle points (PreToolUse, PostToolUse, Stop, PreCompact). The quality feedback loop follows this pattern:

1. Agent writes code
2. PostToolUse hook automatically runs linters
3. Errors return as structured JSON within `hookSpecificOutput.additionalContext`
4. Agent self-corrects without human intervention
5. Loop repeats on each file write

The critical detail: returning plain stdout doesn't inject feedback. Proper JSON structure with `hookSpecificOutput.additionalContext` is required.

#### Four Hook Patterns

- **Safety Gates (PreToolUse):** Block destructive commands (`rm -rf`, `drop table`) and prevent editing sensitive files
- **Quality Loops (PostToolUse):** Auto-run linters after file edits, injecting results as context for self-correction
- **Completion Gates (Stop):** Verify with tests before allowing agent completion
- **Observability:** Stream intent and results to monitoring systems

#### Linter Selection by Language

**TypeScript/JavaScript:** Oxlint (50–100x faster than ESLint) combined with Biome (10–25x faster than Prettier) for PostToolUse Hooks. ESLint remains valuable for custom architectural rules in pre-commit hooks and CI.

**Python:** Ruff combines functionality of Flake8, isort, pyupgrade, pydocstyle, and Black into a single Rust-based binary with 900+ rules. PostToolUse Hook execution completes in under one second.

**Go:** golangci-lint runs 50+ linters in parallel with robust caching. The `--fix` flag supports auto-fixes across 35 linters.

**Rust:** Enable pedantic clippy with structural denial of `allow_attributes` to prevent agents from silencing lints via annotations.

#### Custom Linter Strategies for AI Code

Factory.ai categorizes agent-facing lint rules into four categories:

- **Grep-ability:** Prefer named exports and consistent error types to improve hit rates during codebase searches
- **Glob-ability:** Keep file structure predictable for reliable placement and refactoring
- **Architecture boundaries:** Block cross-layer imports, enforce dependency direction
- **Security/privacy:** Prevent plaintext secrets, mandate input validation, forbid `eval`

Error messages should include not just violations but fix instructions. The pattern:

```
ERROR: [what is wrong] [file:line]
WHY: [why this rule exists, link to ADR]
FIX: [concrete fix steps with code example]
```

#### Linter Config Protection

Prevent agents from editing linter configurations to suppress errors instead of fixing code. PreToolUse hooks can block writes to `.eslintrc`, `pyproject.toml`, and similar files with clear error messages directing agents to fix the underlying code.

#### Feedback Speed Determines Quality

Quality correlates directly with feedback speed:

- **ms (PostToolUse Hook):** Formatter auto-run—agent finishes fixing before recognizing the violation
- **s (Pre-commit hook):** Linter/type check prevents commit
- **min (CI/CD):** Full test suite catches issues before merge
- **h+ (Human review):** Slowest layer

Push checks toward faster layers. Move CI-only linters into pre-commit hooks, move pre-commit checks into PostToolUse Hooks.

### 3. Design AGENTS.md / CLAUDE.md as a Pointer

This file should function as a navigation map rather than a comprehensive manual.

**What to include:**
- Routing instructions ("run `npm test`", "ADRs live in `/docs/adr/`")
- Prohibitions with ADR references
- Minimum build/test/deploy commands

**What to exclude:**
- System state explanations (code and tests are authoritative)
- Tech stack descriptions (packages.json or go.mod reveal these)
- Verbose style guides (delegate to linters)

**Size target:** Under 50 lines. The official recommendation of "under 200 lines" represents an upper bound, not a target. Research shows that at 150–200 instructions, primacy bias becomes pronounced and performance degrades.

Claude Code's system prompt contains approximately 50 instructions. A 100-line CLAUDE.md creates roughly 150 total instructions—approaching the degradation threshold. Compress aggressively.

Pointer-style design offers a benefit: broken references fail loudly (404-equivalent), making rot mechanically detectable.

### 4. Separate Planning from Execution

Agents attempting all work simultaneously waste effort and lose architectural control. The workflow: agent produces plan → human approves → execution begins.

Agents naturally attempt "one-shot" completion of entire features. Explicit instruction to work on single features prevents this. Task decomposition into small building blocks with verification after each completes produces better results with minimal token usage.

Requiring end-to-end test verification before declaring completion dramatically improves accuracy. Agents often skip this without explicit instruction.

### 5. E2E Test Strategy: Give Agents "Eyes"

Without observability into code execution, agents declare work "done" upon compilation success. Browser automation tools and similar mechanisms provide agents the same verification vantage as human users.

#### Web App Testing

**Playwright MCP (Microsoft official):** Accessibility-tree-based interaction via role/name. Works across all major agents. [Playwright v1.56+ ships three subagents](https://shipyard.build/blog/playwright-agents-claude-code/) (Planner, Generator, Healer) for test generation and maintenance.

Limitation: MCP context tax is severe. Full accessibility tree snapshots consume significant tokens, with typical tasks consuming ~114,000 tokens and long sessions showing degradation.

**Playwright CLI:** Same foundation, driven via shell commands rather than MCP protocol. Approximately 4x more token-efficient (~27,000 tokens for equivalent tasks). Accessibility snapshots store to filesystem rather than context window.

**agent-browser (Vercel Labs):** Most token-efficient option. Element references (`@e1`, `@e2`) avoid CSS selector fragility. For 6 tests, Playwright MCP consumes ~31K characters while agent-browser consumes ~5.5K (5.7x improvement).

Recommendation by use case:
- Self-test loop: agent-browser or Playwright CLI
- Test suite generation: Playwright MCP + subagents
- Exploratory testing: agent-browser

#### Universal Principle: The Accessibility Tree

Both Playwright MCP and agent-browser interact via the accessibility tree—structured text rather than screenshots. This enables deterministic interaction, direct element manipulation by role/name, and CI assertions without coordinate guessing.

**Accessibility tree vs. screenshots:**

Use accessibility trees for:
- Programmatic interaction (form fills, navigation, clicks)
- Deterministic testing (same output every time)
- Operation automation

Use screenshots for:
- Visual bug detection (layout, CSS, overlapping elements)
- Visual regression testing
- Rich content (canvas, charts, maps)
- Spatial positioning and responsive behavior

#### Mobile App Testing

Xcode 26.3 introduced native MCP support, enabling agents to generate and run XCTest autonomously. For iOS, agent-driven E2E testing moved from experimental to production-ready.

Recommended tools:
- **iOS (Xcode 26.3):** XcodeBuildMCP returns build errors as structured JSON
- **iOS Simulator:** iOS Simulator MCP Server via Facebook's IDB
- **iOS/Android:** mobile-mcp uses native accessibility tree
- **React Native:** Detox (gray-box testing) monitors async operations to prevent flakes
- **Prototypes:** Maestro MCP (YAML scripts, lightweight)

Follow the generate-then-execute pattern: produce tests via MCP tools, then run generated XCTest/Detox/Espresso deterministically in CI.

#### CLI / TUI Testing

bats-core (Bash Automated Testing System) is well-suited. TAP-compliant output integrates easily with CI. Each test runs in isolated process preventing state leakage.

Move script logic into `run_main` function and wrap with `if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then run_main; fi` to allow bats sourcing and function testing.

Use pexpect/expect for interactive CLIs handling prompts, timeouts, and password input programmatically.

#### API / Backend Testing

**Hurl:** Plain-text HTTP request definition with assertions. Lightweight Rust binary pairs well with agents. Generated Hurl files execute deterministically in CI.

**Pact:** Contract testing for microservices. Pact v4.0.0 improved GraphQL support and async message handling.

**grpcurl:** curl equivalent for gRPC services. Good for CLI-based smoke tests.

**Testcontainers:** Spin up test database containers, automating migrate → seed → test → destroy cycles.

#### Desktop App Testing

**Electron:** Playwright's `_electron.launch()` supports Electron v12.2.0+ with full Page API access. [Official Playwright MCP](https://github.com/microsoft/playwright-mcp) has Electron support in development.

**Tauri:** WebDriver interface on Windows/Linux. macOS has no official support (no WebDriver for WKWebView). Third-party solutions like tauri-webdriver and tauri-plugin-mcp fill this gap.

**Native apps:** [TestDriver.ai](https://testdriver.ai/) uses fine-tuned AI understanding UIs from screenshots. Hardware emulation drives mouse/keyboard. Supports oauth flows and browser extensions.

#### Infrastructure/DevOps Testing

- **Terraform:** `terraform test` (native framework, v1.6+) plus Conftest + OPA for policy enforcement
- **Docker:** container-structure-test validates image structure via YAML/JSON
- **Kubernetes:** kubeconform schema-validates manifests; Conftest applies OPA policies

Essential guardrails:
- Block direct production `terraform apply` or `kubectl apply` with PreToolUse hooks
- Require passing `terraform test`, `conftest test`, and `kubeconform` via Stop hook
- Pipe `terraform plan` through Conftest for policy validation before application

#### AI/ML Pipeline Testing

Testing spans six layers:

- **Data quality:** Great Expectations, dbt Tests, Soda Core
- **Model evaluation:** lm-evaluation-harness, LightEval
- **Application quality (LLM):** DeepEval, promptfoo, RAGAS
- **Agent evaluation:** LangSmith, Arize Phoenix, Langfuse
- **Safety/guardrails:** PyRIT, Guardrails AI, NeMo Guardrails
- **Observability/drift:** Arize, WhyLabs, Evidently AI

#### Verification for Animations

Static tools capture moment-in-time state. Animations require specialized approaches:

- **Layer 1 (ms):** Web Animations API's `getAnimations()` waits for completion before assertions
- **Layer 2 (ms):** PerformanceObserver measures CLS (Cumulative Layout Shift)
- **Layer 3 (s):** CI snapshot comparison with animations frozen via `animation: none !important`
- **Layer 4:** Low-FPS frame capture (5fps) for multimodal agents to inspect frame sequences

### 6. Design State Management Across Sessions

Agents lack memory between sessions—like shift workers with no handover.

**Standardize startup routine:**
1. Verify working directory
2. Read Git log and progress file
3. Select next highest-priority task
4. Start dev server, sanity-check functionality

**Use Git as the bridge:** Commit with descriptive messages. The `git log --oneline -20` becomes the reliable "what happened" record, tied one-to-one with code changes and resistant to rot.

**Use JSON for progress records:** JSON structure prevents agents from inappropriately editing feature lists compared to Markdown. For long projects, use the test suite itself as feature specification instead.

### 7. Platform-Specific Harness Strategies: Codex vs. Claude Code

Research by Morph proves that harness design matters more than model selection. Swapping the harness changes SWE-bench scores by 22 points; swapping the model itself changes scores by only 1 point.

#### Architectural Differences

**Codex:** "Closed-room" architecture. Brings code into cloud sandbox (network-isolated), works independently, returns diff. Enables asynchronous parallel task execution.

**Claude Code:** "Workshop-style." Enters developer environment directly, edits files locally. Hooks system enables deterministic control before/after tool execution.

#### Codex-Specific Features

- Cloud sandbox execution in network-isolated containers with parallelization
- Async task queue (`codex cloud exec`) for parallel multi-task execution
- Automations for scheduled tasks
- App Server protocol unifying all client surfaces via JSON-RPC
- Realtime steering to correct instructions mid-task
- Agents SDK integration exposing Codex CLI as MCP server
- **Hooks system (experimental, introduced March 26, 2026):** Covers SessionStart, PreToolUse, PostToolUse, UserPromptSubmit, Stop. Pre/PostToolUse targets Bash only. Configuration goes in `~/.codex/hooks.json` or `<repo>/.codex/hooks.json`.

Since Codex file operations execute through Bash, Bash-only Hooks provide practical coverage equivalent to Claude Code's file-operation matching, though less granular.

Windows support is temporarily disabled. The legacy `notify` hook faces deprecation.

#### Claude Code-Specific Features

- Stable Hooks system covering all tools (Write, Edit, MultiEdit, Bash)
- PreToolUse blocking enforcement
- PostToolUse quality loop with `additionalContext` injection
- PreCompact hook protecting critical information before compaction
- MCP Tool Search reducing context consumption up to 85%
- Agent Teams (experimental) enabling direct communication between sessions
- Plan Mode (40–60% token reduction) plus Extended Thinking for complex decisions

#### Shared Harness Layer

Both platforms benefit from:
- AGENTS.md (AAIF standard, read by Codex/Cursor/Devin/Gemini CLI/GitHub Copilot)
- Skills (SKILL.md, open standard)
- MCP configuration
- ADRs, linter settings, test suites

For Claude Code, include AGENTS.md via `@AGENTS.md` reference in CLAUDE.md since AGENTS.md isn't loaded natively.

#### Hybrid Strategy

Many adopt hybrid approaches: Claude Code plans and designs → Codex executes in parallel → Claude Code reviews and polishes. Build the harness in Claude Code, then scale execution in Codex.

## Anti-Patterns to Avoid

1. **Relying only on prompts:** "Remember to write tests" in instructions insufficient. Force execution with hooks
2. **Accumulating explanatory docs:** Represent dependencies through type definitions/schemas and structural tests rather than README prose
3. **Bloating instruction files:** Aim for under 50 lines, not 1,000+
4. **Building agent-only infrastructure:** Build excellent developer infrastructure; agents benefit automatically
5. **Scaling without harness:** Scaling agent count without quality infrastructure creates compounding debt, not leverage

## Minimum Viable Harness (MVH)

Build incrementally rather than adopting all principles simultaneously.

**Week 1:**
- Write AGENTS.md / CLAUDE.md (under 50 lines, pointers only)
- Set up pre-commit hooks for linters/formatters/type checks
- Configure PostToolUse Hook for auto-formatting
- Write first ADR

**Week 2–4:**
- Add test or linter rule whenever agent makes mistake
- Establish plan → approve → execute workflow
- Introduce E2E testing tool (Playwright CLI or agent-browser)
- Make passing tests completion condition via Stop Hook
- Standardize session startup routine

**Month 2–3:**
- Build custom linters with fix instructions in error messages
- Link ADRs and linter rules (archgate pattern)
- Replace descriptive docs with tests and ADRs
- Set up safety gates with PreToolUse Hooks

**Month 3+:**
- Consider advanced patterns like Plankton
- Introduce garbage-collection processes
- Run multiple agents simultaneously
- Measure harness effectiveness quantitatively

## Summary

Core insights:

- Enforce quality through mechanisms, not prompts. Linters, Hooks, tests, and ADRs compound in effectiveness
- Push checks toward faster feedback layers: PostToolUse Hook (ms) > pre-commit (s) > CI (min) > human review (h)
- Build incrementally with MVH rather than adopting everything at once

The field of harness engineering may have limited longevity as LLMs improve, but for March 2026 it remains essential for autonomous agent operation.

---

## 繁體中文全文摘要

### 核心命題：系統，而非模型，才是關鍵

Harness engineering = 持續改善 agent 指令檔案 + 啟用自我驗證的工具鏈。存在目的是穩定 agent 輸出並維持自主運作。

### 原則一：Repository Hygiene（設計好腐敗）

Agents 平等對待所有 repo 文字，缺乏判斷文件陳舊的直覺。

**應放入 repo 的內容**：
- 可執行 artifact（程式碼、測試、linter 設定、型別定義）
- 帶時間戳和狀態追蹤的 ADR（Architecture Decision Records）

**不應放入的內容**：
- 系統現狀的散文說明
- 手寫 API 描述
- 文字版架構概覽

測試比文件更有韌性：規格變成測試，違反時會大聲失敗，而非靜默腐敗。

### 原則二：用確定性工具強制品質（Hook 驅動）

**核心原則**：「LLM 比傳統 linter 和格式化工具貴且慢。只要確定性工具能做的，就用它。」

在 CLAUDE.md 寫「執行 linter」vs. 透過 Hooks 自動執行 linter——前者「幾乎每次」成功，後者「每次無例外」。

#### 四種 Hook 模式

| 模式 | 觸發點 | 作用 |
|------|-------|------|
| **Safety Gates** | PreToolUse | 阻擋 `rm -rf`、`drop table`，防止編輯敏感檔案 |
| **Quality Loops** | PostToolUse | 檔案編輯後自動跑 linter，注入結果讓 agent 自我修正 |
| **Completion Gates** | Stop | 允許 agent 完成前先跑測試驗證 |
| **Observability** | 各點 | 串流意圖和結果到監控系統 |

PostToolUse Hook 正確用法：JSON 結構 + `hookSpecificOutput.additionalContext`（純 stdout 不會注入回饋）。

**阻擋 Linter 設定修改**：PreToolUse hook 阻擋對 `.eslintrc`、`pyproject.toml` 的寫入，強制 agent 修復程式碼而非抑制 lint 錯誤。

#### 各語言 Linter 推薦

| 語言 | PostToolUse Hook 推薦 | 速度優勢 |
|------|----------------------|---------|
| TypeScript/JS | Oxlint + Biome | 50-100x、10-25x 比 ESLint/Prettier 快 |
| Python | Ruff | 900+ 規則，Rust 實作，<1 秒完成 |
| Go | golangci-lint | 50+ linter 並行，支援 `--fix` |
| Rust | clippy（pedantic）| 阻止 agent 用 `allow_attributes` 靜默 lint |

#### Lint 錯誤訊息格式（給 Agent 用）

```
ERROR: [什麼錯了] [file:line]
WHY: [為什麼有這個規則，ADR 連結]
FIX: [具體修復步驟 + 程式碼範例]
```

#### 反饋速度決定品質

```
ms  (PostToolUse Hook)  → 格式化自動跑
s   (Pre-commit hook)   → linter/型別檢查
min (CI/CD)             → 完整測試套件
h+  (人工 review)       → 最慢層
```

**方向**：把 CI 的 linter 移到 pre-commit；把 pre-commit 的檢查移到 PostToolUse Hook。

### 原則三：AGENTS.md / CLAUDE.md 設計為「指標」

**目標尺寸：50 行以下**（官方建議 200 行是上限，不是目標）。

Claude Code 系統提示約有 50 條指令。100 行 CLAUDE.md 約產生 150 條總指令——接近效能降解閾值。積極壓縮。

**應包含**：路由指令（「跑 `npm test`」）、禁令 + ADR 參照、最小 build/test/deploy 指令
**應排除**：系統狀態解釋（程式碼和測試才是權威）、技術棧描述（package.json 揭示）、詳細風格指南（委託給 linter）

### 原則四：分離規劃與執行

Agent 傾向「一次性」完成整個功能。明確指令一次一個功能，每個小建構塊完成後驗證，比試圖一次完成更有效。

### 原則五：E2E 測試給 Agent「眼睛」

沒有可觀測性，agent 在編譯成功後就宣告「完成」。

**無障礙樹 vs 截圖**：
- **無障礙樹**：程式化互動、確定性測試、操作自動化
- **截圖**：視覺 bug 偵測、CSS/layout 問題、空間定位

**Token 效率**：agent-browser（Vercel Labs）比 Playwright MCP 省 5.7x tokens（6 個測試：5.5K vs 31K 字元）。

### Codex vs Claude Code 架構差異

| 面向 | Codex | Claude Code |
|------|-------|-------------|
| 架構 | 「密室」—程式碼進雲端沙箱，回傳 diff | 「工作坊」—直接進入開發環境本機編輯 |
| 並行 | 非同步任務佇列，`codex cloud exec` | Agent Teams（實驗性）|
| Hooks | 實驗性（2026-03-26 引入），僅 Bash | 穩定，涵蓋所有工具 |

**混合策略**：Claude Code 規劃設計 → Codex 並行執行 → Claude Code review 潤飾。

### 最小可行 Harness（MVH）四週計劃

**第 1 週**：AGENTS.md（<50 行）+ pre-commit hooks + PostToolUse 自動格式化 + 第一個 ADR

**第 2-4 週**：agent 每次犯錯就加規則/測試 + plan→approve→execute 工作流 + E2E 測試 + Stop Hook 把通過測試設為完成條件

**第 2-3 月**：自訂 linter + ADR 與 linter 連結 + 替換描述性文件為測試和 ADR + Safety Gates

### 五大反模式

1. 只依賴 prompt（「記得寫測試」不夠，用 Hook 強制執行）
2. 累積說明性文件（用型別定義和結構測試表達依賴）
3. 指令檔案膨脹（目標 <50 行，不是 1,000+）
4. 建立 agent 專用基礎設施（建立良好的開發者基礎設施；agent 自動受益）
5. 沒有 harness 就擴展規模（增加 agent 數量而不建品質基礎設施 = 複利負債）

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | Repo hygiene 清單、4 種 Hook 模式、MVH 4 週計劃、5 個 anti-patterns 直接可執行 |
| B. 創新性 | 8/10 | Hooks 分類法（Safety/Quality/Completion/Observability）、回饋速度層級為首創 |
| C. 證據品質 | 9/10 | 每語言 linter 工具推薦具體（Oxlint+Biome/Ruff/golangci-lint/clippy），ms→h+ 層級量化 |
| D. 技術深度 | 9/10 | 非常實作導向：特定工具、反模式、4 週計劃、完整 hooks 設定範例 |
| E. 泛化性 | 8/10 | MVH 原則跨語言、跨 agent 平台適用 |
| **加權總分** | **8.65/10** | 9×0.3+8×0.2+9×0.2+9×0.15+8×0.15 = 2.7+1.6+1.8+1.35+1.2 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（Hooks 分類法 + MVH 計劃）  
**整合狀態**：待實作
