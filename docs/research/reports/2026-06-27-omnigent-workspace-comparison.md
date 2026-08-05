# Omnigent vs cc-workspace 對照報告

**日期**: 2026-06-27  
**主題**: Omnigent meta-harness YAML spec 與 cc-workspace `.claude/` 結構對照  
**來源**: github.com/omnigent-ai/omnigent（README + docs/AGENT_YAML_SPEC.md + examples/kimi_hello.yaml + omnigent/policies/builtins/cost.py）

---

## 1. Omnigent YAML Schema 摘要

### 抓取成功的來源

| 來源 | URL | 狀態 |
|------|-----|------|
| README | github.com/omnigent-ai/omnigent | 成功 |
| AGENT_YAML_SPEC.md | github.com/omnigent-ai/omnigent/blob/main/docs/AGENT_YAML_SPEC.md | 成功（部分） |
| kimi_hello.yaml | github.com/omnigent-ai/omnigent/blob/main/examples/kimi_hello.yaml | 成功 |
| cost.py policy | github.com/omnigent-ai/omnigent/blob/main/omnigent/policies/builtins/cost.py | 成功（摘要） |
| debby/polly/scribe examples | github.com/omnigent-ai/omnigent/tree/main/examples | 部分（目錄可見，內容未抓） |

### Omnigent Agent YAML 完整 Field 清單

**Top-level fields**:

| Field | 型別 | 說明 |
|-------|------|------|
| `name` | string | agent 識別符 |
| `description` | string | agent 用途說明 |
| `prompt` / `instructions` | string | system prompt / 行為指示 |
| `executor` | object | runtime 組態（harness + model + auth） |
| `tools` | object map | 工具定義（function / mcp / agent 三種 type） |
| `policies` | object map | 治理規則（cost / safety / tool-access） |
| `params` | object | 自訂參數 [unverified: 詳細型別未抓] |
| `os_env` | object | 環境變數注入 [unverified: 詳細用法] |
| `terminals` | object | 終端機設定 [unverified] |
| `async` | bool | 非同步執行 [unverified] |
| `cancellable` | bool | 允許中途取消 [unverified] |
| `timers` | object | 排程觸發 [unverified: 詳細語法] |

**executor sub-fields**:

| Field | 說明 | 已知值 |
|-------|------|--------|
| `executor.harness` | 指定 runtime | `claude-sdk`, `openai-agents`, `codex`, `cursor`, `kiro-native`, `pi`, `antigravity`, `qwen`, `kimi`, `copilot`, `hermes` |
| `executor.model` | provider-specific model ID | `kimi-k2-turbo`, `claude-*`, `gpt-*`... |
| `executor.auth` | 認證類型 | `databricks`, `api_key`, `subscription`, `gateway` |

**tools sub-fields**:

| Field | 說明 |
|-------|------|
| `tools.<name>.type` | `function` / `mcp` / `agent` |
| `tools.<name>.callable` | Python function path（type=function 時） |
| `tools.<name>.url` | MCP server endpoint（type=mcp 時） |
| `tools.<name>.prompt` | sub-agent 指示（type=agent 時） |
| `tools.<name>.tools` | 子工具繼承（type=agent 時，`inherit` 關鍵字） |

**policies sub-fields**（cost 為主要可驗證範例）:

| Field | 說明 |
|-------|------|
| `policies.<name>.type` | `function` |
| `policies.<name>.handler` | built-in 或自訂 Python handler path |
| `policies.<name>.factory_params` | handler 參數物件 |
| `factory_params.max_cost_usd` | 硬上限（必填，>0） |
| `factory_params.ask_thresholds_usd` | 軟檢查點清單（超越時請求許可） |
| `factory_params.expensive_models` | 高費模型清單（觸發 downgrade） |

**Policy scope levels**（三層，嚴格度：session > agent > server）:
- Server-wide（admin 設定）
- Per-agent（developer 設定）
- Per-session（user 設定，最嚴格先檢查）

**`after: spend > $100 → pause_and_request_permission` 語法**: [unverified — README 背景說明提及此行為概念，但確切 YAML 語法未在抓到的 spec 中找到。`cost_budget` policy + `ask_thresholds_usd` 是確認的實作機制，效果等價。]

---

## 2. 對照表

| Omnigent field | 用途 | workspace 對應 | gap? |
|----------------|------|----------------|------|
| `executor.harness` | 一行換 runtime（Claude Code / Codex / Cursor / Kimi...） | 無直接對應——workspace 硬綁 Claude Code harness，無 harness 切換層 | **GAP（設計哲學差異）**: workspace 基於 MHF 原則刻意單一 harness；Omnigent 為 multi-harness portability |
| `executor.model` | 指定模型 ID | `multi-mode-skill` §1 位置數判準 → `model=haiku/sonnet/opus/fable`；`subagent-strategy.md` 模型選擇 | 覆蓋：workspace 動態路由，Omnigent 靜態宣告 |
| `executor.auth` | 認證（api_key / databricks / subscription / gateway） | 未在 CLAUDE.md / rules 中顯式設定；由 Claude Code CLI 環境變數處理 | 小 gap：workspace 無 auth 層抽象，靠 CLI 環境設定 |
| `tools.<name>.type: function` | 自訂 Python function 工具 | Bash hook / scripts/*.py；`allowed-tools` SKILL frontmatter | 部分覆蓋：workspace 工具是靜態清單，無 Python callable 動態注入 |
| `tools.<name>.type: mcp` | MCP server endpoint | Claude Code 內建 MCP 支援（.claude/settings 或 CLI 設定） | 覆蓋：MCP 支援存在，但非 YAML per-agent 宣告 |
| `tools.<name>.type: agent` | sub-agent 工具（nested agent as tool） | `AGENTS.md` dispatch table + `subagent-strategy.md` fan-out | 覆蓋：功能等價，但 workspace 用 prompt injection 而非 YAML 宣告 |
| `tools.<name>.tools: inherit` | 子 agent 繼承父工具 | 無 inherit 語法；子 agent 需 parent prompt 顯式傳遞（handoff contract） | **GAP**: workspace 要求 parent 顯式注入全部 context，無 `inherit` 快捷 |
| `policies.<name>.handler` | 治理規則 handler（Python callable） | `.claude/hooks/block-dangerous.sh`（PreToolUse）; `pre-push-cost.sh`（PostToolUse）; `protect-sensitive-files.sh` | 部分覆蓋：workspace 用 bash hooks，Omnigent 用 Python policy handler |
| `policies.budget.factory_params.max_cost_usd` | 硬性 USD 上限，超限拒絕操作或要求降級 | `model-selection-grid.md` 提及 `--max-budget-usd`（Claude Code CLI print mode GA）；`pre-push-cost.sh` 紀錄 cost，但無自動阻斷 | **GAP（高 ROI）**: workspace 無 mid-session cost gate；只有 push 後的 cost 記錄 + 事後監控 |
| `policies.budget.factory_params.ask_thresholds_usd` | 軟檢查點，超越時請求許可 | 無對應機制 | **GAP（高 ROI）**: workspace 無 per-session 軟成本閾值提醒 |
| `policies.budget.factory_params.expensive_models` | 高費模型清單，超限強制 downgrade | `multi-mode-skill` 位置數判準（Haiku→Sonnet→Opus 路由）；`context-management.md` token budget 軟限 | 覆蓋：workspace 有 upfront model routing，無動態 downgrade gate |
| Policy scope 三層（server/agent/session） | 不同作用域的治理策略覆蓋 | `core.md` APPLY §不可逆例外（session 級確認）；hooks 作用於所有 tool calls（server 層等價）；無 per-agent policy scope | 小 gap：workspace 無明確 per-agent policy scope |
| `name` + `description` | agent 識別與說明 | SKILL.md frontmatter（`name`, `description`, `roster-domain`） | 覆蓋 |
| `prompt` / `instructions` | agent system prompt | SKILL.md 正文 + sub-agent prompt injection（handoff contract） | 覆蓋 |
| `params` | 自訂 agent 參數 | SKILL.md `| 參數 | 說明 | 預設 |` 表格（如 pilot-review GATE_LEVEL） | 覆蓋（靜態文件，非 YAML 動態注入） |
| `os_env` | 環境變數 | `.env` + `session-init.sh` | 覆蓋（非 per-agent） |
| `timers` / 排程 | 定時觸發 | `/schedule` routine + `CronCreate` / `ScheduleWakeup`（`multi-mode-skill` §0） | 覆蓋（CLI 本機限定） |
| `async` + `cancellable` | 非同步執行與取消 | `run_in_background: true`（Bash tool）；`pause_turn`（agent control） | 覆蓋 |
| `terminals` | 終端機設定 | Claude Code CLI 終端即 terminal，無額外配置 | 無對應（不適用）|

---

## 3. 可借鏡點（按 ROI 排序，≤3）

### P1（最高 ROI）— Mid-session Cost Gate

**Omnigent 機制**: `policies.budget` + `ask_thresholds_usd: [3.00]` + `max_cost_usd: 5.00`  
在 session 進行中，累計消費跨越軟閾值時自動請求使用者許可；跨越硬上限時拒絕操作。

**workspace 現狀**: 只有 `pre-push-cost.sh`（push 後記錄，不阻斷）+ `--max-budget-usd`（CLI print mode 專用，非互動 session）。`context-management.md` 的 token budget 是軟性行為信號，非 code-enforced gate。

**借鏡方向**: PreToolUse hook 讀取 `~/.claude/usage.db` 當前 session 累計 cost，超過設定閾值（如 $5）時 `exit 2` + 訊息「已消費 $X.XX，是否繼續？」。等同 Omnigent 的 `ask_thresholds_usd` 行為，不需要引入 Omnigent 依賴。

**實作成本**: 中（1 個新 hook，約 50 行 bash/python；需驗證 `usage.db` 即時讀取精度）。

---

### P2（高 ROI）— `tools: inherit` 語法等價：Sub-agent Tool Context Protocol

**Omnigent 機制**: `tools.<sub-agent>.tools: inherit` — 子 agent 自動繼承父 agent 的工具集，無需 parent 重複注入。

**workspace 現狀**: Handoff Contract 要求 parent 顯式傳遞「allowed-tools + 全部必要 context」給子 agent（`subagent-strategy.md §任務契約`）。這是正確的隔離設計，但造成 prompt boilerplate。

**借鏡方向**: 在 AGENTS.md §2 dispatch table 中為每個標準 agent 定義 `allowed-tools` 清單（已有部分實作於 SKILL.md frontmatter）；建立「agent inherit profile」概念（如 `inherits: researcher-base`），讓 handoff contract 可以引用 profile 而非每次全列。不必引入 Omnigent，僅需 workspace 慣例標準化。

**實作成本**: 低（文件整理 + AGENTS.md 格式擴充；不改動 hooks）。

---

### P3（中 ROI）— Policy Scope 三層顯式化

**Omnigent 機制**: server / agent / session 三層 policy 優先序；最嚴格者優先。

**workspace 現狀**: hooks 是 server 層（全域，所有 tool calls）；`core.md §APPLY 不可逆例外` 是 session 層；per-agent policy 無顯式定義。

**借鏡方向**: 在 AGENTS.md §5（Harness vs Body）或新增 §Policy Scope 章節，顯式文件化三層 policy 優先序（server = hooks；agent = SKILL.md allowed-tools + 紅線；session = 不可逆確認）。不需改 code，僅需 framing 更清楚。對新 skill 設計有指引價值，提升 harness 可解釋性。

**實作成本**: 低（文件，~20 行）。

---

## 4. 不適用 / 已覆蓋項

| Omnigent feature | 判斷 | 原因 |
|------------------|------|------|
| `executor.harness` 多 runtime | 不適用 | workspace 基於 MHF 原則：Claude Code post-training byte-level 過擬合，跨 harness 是效能崩塌風險（`harness-design.md §反模式`）。Omnigent 的核心價值命題在此與 workspace 哲學對立。 |
| `executor.auth` gateway / subscription 支援 | 不適用 | workspace 單一 Anthropic API，無多供應商需求 |
| `tools.type: function` Python callable 注入 | 已覆蓋 | workspace 用 `scripts/*.py` + Bash tool；效果等價，MHF 下無需動態 callable |
| `prompt` / system instructions | 已覆蓋 | SKILL.md + AGENTS.md + CLAUDE.md 三層 |
| `timers` 排程 | 已覆蓋 | `/schedule` + `CronCreate` / `ScheduleWakeup` |

---

## 5. 結論

**有值得開 EVOLUTION-QUEUE 提案的 gap**: 是，一個高優先項。

### 建議提案：`pre-session-cost-gate` hook

**問題**: workspace 目前無 mid-session cost gate，Fable 5 / Opus 4.8 長任務可能在使用者無感知下消費 $10–$30（model-selection-grid.md §AA-Briefcase）。`pre-push-cost.sh` 是事後紀錄，`--max-budget-usd` 僅 print mode。

**方案**: 新增 `PreToolUse` hook，讀取 `~/.claude/usage.db` 當前 session cost，超過 `CLAUDE_SESSION_COST_LIMIT`（建議預設 $5，可覆寫）時 `exit 2` + 提示使用者確認。可設 `ask_thresholds_usd` 等價的軟閾值（如 $3 提示、$8 硬阻斷）。

**驗收條件**: session cost 達 $3 時自動顯示提示（可繼續），達 $5 時 block 並要求手動確認；`CLAUDE_SKIP_COST_GATE=1` 可旁路（admin override）。

**ROI**: 防止單次意外超支，特別是 agentic overnight 任務；與 Omnigent 治理設計對齊；不引入任何新依賴（`usage.db` 已有，`pricing.py` 已有）。

**開提案路徑**: `research/EVOLUTION-QUEUE.md` → 標題 `[COST-GATE] mid-session cost threshold hook`。

---

*來源抓取狀態*:  
- github.com/omnigent-ai/omnigent README: 成功  
- docs/AGENT_YAML_SPEC.md: 成功（部分欄位 [unverified] 標注）  
- examples/kimi_hello.yaml: 成功  
- omnigent/policies/builtins/cost.py: 成功（摘要）  
- `after: spend > $100 → pause_and_request_permission` 確切 YAML 語法: [unverified]（等價實作機制 `ask_thresholds_usd` 已確認）
