# Advisor Tool — 完整技術指南與最佳實踐

> 來源：https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool  
> 收錄日期：2026-05-01  
> 狀態：Beta（需要 header `advisor-tool-2026-03-01`）  
> 涵蓋：架構概念、API 用法、Best Practices、成本控制

---

## 概念：Executor + Advisor 模式

**Advisor tool** 讓較快的低成本 **executor 模型**在生成中途向高智力 **advisor 模型**諮詢戰略指引。Advisor 讀取完整對話脈絡，產出計劃或修正方向（約 400–700 text tokens，含思考共 1,400–1,800 tokens），executor 再繼續執行。

**適用場景**：長任務 agentic 工作流（coding agent、computer use、多步驟研究），大多數 turn 是機械性執行但計畫品質至關重要。以 executor 模型費率做大部分生成，換取接近 advisor-only 的品質。

**與本 workspace 的對應**：
- `advisor()` 函式 = 本 workspace 的 Advisor 模式（見 `subagent-strategy.md`）
- `.claude/rules/subagent-advanced.md` §API 層 Advisor 工具 即引用此功能

---

## 模型相容性

| Executor | Advisor |
|----------|---------|
| Haiku 4.5 (`claude-haiku-4-5-20251001`) | Opus 4.7 (`claude-opus-4-7`) |
| Sonnet 4.6 (`claude-sonnet-4-6`) | Opus 4.7 (`claude-opus-4-7`) |
| Opus 4.6 (`claude-opus-4-6`) | Opus 4.7 (`claude-opus-4-7`) |
| Opus 4.7 (`claude-opus-4-7`) | Opus 4.7 (`claude-opus-4-7`) |

Advisor 必須 ≥ Executor 能力等級，否則 API 回傳 `400 invalid_request_error`。

---

## 快速開始（Python）

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["advisor-tool-2026-03-01"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-7",
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "Build a concurrent worker pool in Go with graceful shutdown.",
        }
    ],
)
```

---

## 運作機制

1. Executor 決定呼叫 advisor（如同任何工具），發出 `server_tool_use` block（input 永遠為空）
2. Anthropic server 端執行獨立推理，將 executor 完整 transcript 傳入 advisor（含 system prompt、所有 tools、所有對話歷史）
3. Advisor 回應透過 `advisor_tool_result` block 回到 executor
4. Executor 繼續生成，受 advice 引導

**一切在單一 `/v1/messages` 請求內完成，不需要額外 round trip。**

Advisor 自身不帶 tools、不做 context 管理。其 thinking blocks 在回傳前被丟棄，只有 advice text 到達 executor。

---

## Tool 參數

| 參數 | 型別 | 預設 | 說明 |
|------|------|------|------|
| `type` | string | required | `"advisor_20260301"` |
| `name` | string | required | `"advisor"` |
| `model` | string | required | Advisor 模型 ID，以此模型費率計費 |
| `max_uses` | integer | unlimited | 單次 request 的 advisor 呼叫上限（非對話層級） |
| `caching` | object \| null | null（關閉）| `{"type": "ephemeral", "ttl": "5m" \| "1h"}` |

---

## 多輪對話

必須將完整 assistant content（含 `advisor_tool_result` blocks）回傳給下一輪：

```python
# 正確：保留所有 advisor_tool_result blocks
messages.append({"role": "assistant", "content": response.content})

# 繼續對話
messages.append({"role": "user", "content": "Now add a max-in-flight limit of 10."})
```

若下一輪省略 advisor tool 但 history 仍含 `advisor_tool_result` blocks → `400 invalid_request_error`。

---

## 成本與計費

- Advisor sub-inference 以 **advisor 模型費率**獨立計費
- 頂層 `usage` 欄位只反映 executor tokens
- Advisor tokens 在 `usage.iterations[]` 中標記為 `"type": "advisor_message"`
- 頂層 `max_tokens` 只限 executor 輸出，不限 advisor tokens

典型 advisor 輸出：400–700 text tokens（含思考 1,400–1,800 tokens）

---

## Advisor Prompt Caching

兩層快取各自獨立：

### Executor 端快取
`advisor_tool_result` block 可加 `cache_control` breakpoint，行為與其他 content block 相同。

### Advisor 端快取（跨呼叫）
```python
tools = [
    {
        "type": "advisor_20260301",
        "name": "advisor",
        "model": "claude-opus-4-7",
        "caching": {"type": "ephemeral", "ttl": "5m"},  # 或 "1h"
    }
]
```

**使用時機**：advisor 呼叫次數 ≤ 2 次 → 不划算（cache write 比 read 省的多）；≥ 3 次 → 啟用划算，越多越省。

**保持一致**：整個對話不要切換 caching on/off（造成 cache miss）。

> ⚠️ `clear_thinking` 設定 `keep` 非 `"all"` 時會造成 advisor 端 cache miss（品質不影響，但成本增加）。建議設 `keep: "all"` 保持 advisor cache 穩定。

---

## ★ Best Practices（官方原文）

### Coding / Agent 任務的 Prompting

Advisor tool 內建 description 已引導 executor 在複雜任務開始時及遇到困難時呼叫。研究任務通常不需額外 prompting。

Coding/agent 任務中，advisor 在兩個關鍵時機呼叫效果最好：

1. **早期第一次呼叫**：完成幾個探索性讀取後（有足夠脈絡但尚未做實質工作）
2. **困難任務的最後呼叫**：完成 file writes 和 test outputs 後

若 agent 有其他 planner 工具（如 todo list），先呼叫 advisor 再使用 planner，讓 advisor 的計劃流入 planner。

#### 官方推薦 System Prompt（Timing 指引）

```text
You have access to an `advisor` tool backed by a stronger reviewer model. It takes NO
parameters — when you call advisor(), your entire conversation history is automatically
forwarded. They see the task, every tool call you've made, every result you've seen.

Call advisor BEFORE substantive work — before writing, before committing to an
interpretation, before building on an assumption. If the task requires orientation first
(finding files, fetching a source, seeing what's there), do that, then call advisor.
Orientation is not substantive work. Writing, editing, and declaring an answer are.

Also call advisor:
- When you believe the task is complete. BEFORE this call, make your deliverable durable:
  write the file, save the result, commit the change. The advisor call takes time; if the
  session ends during it, a durable result persists and an unwritten one doesn't.
- When stuck — errors recurring, approach not converging, results that don't fit.
- When considering a change of approach.

On tasks longer than a few steps, call advisor at least once before committing to an
approach and once before declaring done. On short reactive tasks where the next action is
dictated by tool output you just read, you don't need to keep calling — the advisor adds
most of its value on the first call, before the approach crystallizes.
```

#### 官方推薦 System Prompt（如何對待 Advice）

```text
Give the advice serious weight. If you follow a step and it fails empirically, or you have
primary-source evidence that contradicts a specific claim (the file says X, the paper states
Y), adapt. A passing self-test is not evidence the advice is wrong — it's evidence your test
doesn't check what the advice is checking.

If you've already retrieved data pointing one way and the advisor points another: don't
silently switch. Surface the conflict in one more advisor call — "I found X, you suggest Y,
which constraint breaks the tie?" The advisor saw your evidence but may have underweighted
it; a reconcile call is cheaper than committing to the wrong branch.
```

#### 削減 Advisor 輸出長度（節省 35–45% tokens）

在 system prompt 最前面加一行（其他提到 advisor 的句子之前）：

```text
The advisor should respond in under 100 words and use enumerated steps, not explanations.
```

#### Effort 搭配建議

| 配置 | 效果 |
|------|------|
| Sonnet executor（medium effort）+ Opus advisor | 智力接近 Sonnet 預設 effort，成本更低 |
| Sonnet executor（default effort）+ Opus advisor | 最高智力 |

### 成本控制

- **對話層級 cap**：client-side 計數，達上限後從 `tools` 移除 advisor **且**從 message history 移除所有 `advisor_tool_result` blocks
- **`caching`**：≥ 3 次呼叫才啟用
- **`max_uses`**：每個 request 的呼叫上限（非對話層級）

---

## 與其他工具組合

```python
tools = [
    {"type": "web_search_20250305", "name": "web_search", "max_uses": 5},
    {"type": "advisor_20260301", "name": "advisor", "model": "claude-opus-4-7"},
    {"name": "run_bash", "description": "Run a bash command", "input_schema": {...}},
]
```

Executor 在同一個 turn 可以搜尋網路、諮詢 advisor、呼叫自訂工具。

---

## 限制

| 限制 | 說明 |
|------|------|
| Advisor 輸出不串流 | Stream 在 advisor 執行期間暫停，完成後整塊到達 |
| 無對話層級上限 | 需 client-side 計數管控 |
| `max_tokens` 不限 advisor | Advisor tokens 不計入 executor 的 token 預算 |
| Priority Tier 不延伸 | Executor 的 Priority Tier 不自動套用到 advisor |
| `clear_tool_uses` 相容性 | 尚未完全相容 advisor tool blocks |

---

## 本 Workspace 的對應

本 workspace 的 `advisor()` 函式（見系統 prompt）是此 API 功能的 Claude Code 層封裝。

| API 層 | Claude Code 層 |
|--------|---------------|
| `advisor_20260301` tool | `advisor()` 函式 |
| Executor = Sonnet/Haiku | 主 agent（Sonnet 4.6）|
| Advisor = Opus 4.7 | Advisor 模型（Opus 4.7）|
| 單一 `/v1/messages` 請求 | 同一 session 的 `advisor()` 呼叫 |

官方推薦的 timing 指引（Coding 任務 system prompt）已內建於本 workspace 的系統 prompt，即為上方「Timing 指引」區塊的直接引用來源。
