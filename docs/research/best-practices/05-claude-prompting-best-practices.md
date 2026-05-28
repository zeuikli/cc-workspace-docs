---
title: "Claude Prompting Best Practices"
source: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
type: best-practices
---

# Claude Prompting Best Practices

> 來源：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices  
> 收錄日期：2026-05-01  
> 涵蓋：Claude Opus 4.7、Opus 4.6、Sonnet 4.6、Haiku 4.5

---

## Opus 4.7 特定行為調整

### 回應長度與詳細度

Opus 4.7 依任務複雜度自動校準長度，不預設固定詳細度。若需控制：

```text
Provide concise, focused responses. Skip non-essential context, and keep examples minimal.
```

正面範例比負面禁止（"Don't do X"）更有效。

### Effort 等級（新 xhigh）

| Effort | 適用 |
|--------|------|
| `max` | 極難問題，可能過度思考 |
| `xhigh`（**Opus 4.7 推薦**） | 多數 coding / agentic 任務 |
| `high` | 多數智力敏感任務的最低建議值 |
| `medium` | 降低 token，犧牲一定智力 |
| `low` | 短、範圍小、延遲敏感的任務 |

Opus 4.7 嚴格遵守低 effort 設定（不自作主張），複雜任務若觀察到淺薄推理應提升 effort 而非 prompt workaround。

### Default Effort 升級時間表

| 時間 | 受影響對象 | 變動 |
|------|----------|------|
| W15（Apr 2026） | API key、Bedrock、Vertex、Foundry、Team、Enterprise | default effort `medium` → `high` |
| W16（Apr 2026） | Max 用戶 | Opus 4.7 成為新預設模型 |
| W17（Apr 2026） | Pro / Max 用戶 | Opus 4.6 / Sonnet 4.6 default effort `medium` → `high` |

從 Sonnet 4.5 或舊版遷移若觀察到延遲升高，確認是否因 default effort 提升所致（可顯式設定 `--effort medium` 降回）。

設定 xhigh/max 時，建議 max_tokens 從 64k 起跳：

```text
This task involves multi-step reasoning. Think carefully through the problem before responding.
```

### Fast Mode on Opus 4.7（W20，Research Preview）

`/fast` 現在預設使用 Opus 4.7（原 Opus 4.6）：

- 約 **2.5× 速度**，較高 per-token 成本
- 適合快速迭代和 live debugging
- 定價：$30 / $150 per MTok input/output（與 Opus 4.6 fast mode 相同）

```text
> /fast    # 切換到 fast mode（使用 Opus 4.7）
```

若需要 pin 回 Opus 4.6：

```bash
export CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1
```

### 工具使用觸發

Opus 4.7 預設比 4.6 少用工具、多用推理。若需更積極使用工具：

```text
Use [tool] when it would enhance your understanding of the problem.
```

避免 "If in doubt, use [tool]"（會導致 overtriggering）。

### 更字面的指令遵從

Opus 4.7 更字面解讀指令，不會自行從一個情境推廣到另一個。若需廣泛應用：

> "Apply this formatting to every section, not just the first one"

### 子代理生成控制

```text
Do not spawn a subagent for work you can complete directly in a single response
(e.g. refactoring a function you can already see).

Spawn multiple subagents in the same turn when fanning out across items
or reading multiple files.
```

---

## 一般原則

### 清晰直接（Be Clear and Direct）

把 Claude 想像成「聰明但剛來的新員工」——缺少你的工作脈絡，越精確越好。

**黃金法則**：把 prompt 給一個對任務不熟的同事，如果他會困惑，Claude 也會。

- 明確指定輸出格式與限制
- 步驟順序重要時用編號清單

```text
# 差
Create an analytics dashboard

# 好
Create an analytics dashboard. Include as many relevant features and interactions as possible.
Go beyond the basics to create a fully-featured implementation.
```

### 加入脈絡以提升表現

解釋 WHY 能讓 Claude 更精準地達成目標：

```text
# 差
NEVER use ellipses

# 好
Your response will be read aloud by a text-to-speech engine, so never use ellipses
since the text-to-speech engine will not know how to pronounce them.
```

### 善用範例（Few-shot / Multishot）

範例是最可靠的輸出格式調整方式。3–5 個最佳：

- **相關**：貼近實際使用場景
- **多元**：涵蓋 edge case，避免模型學到非預期模式
- **結構化**：用 `<example>` tags 包裹，多個用 `<examples>`

### XML 標籤結構化

混合指令/脈絡/範例/輸入時，XML tags 大幅降低誤解：

```xml
<instructions>...</instructions>
<context>...</context>
<input>...</input>
```

巢狀文件結構：
```xml
<documents>
  <document index="1">
    <source>filename.pdf</source>
    <document_content></document_content>
  </document>
</documents>
```

### 賦予角色

```python
system="You are a helpful coding assistant specializing in Python."
```

一句話即可。

### 長 Context 提示技巧

- **長資料放最前**：文件/大輸入放 prompt 最上方，查詢/指令放最後（可提升 30% 表現）
- **引用定錨**：要 Claude 先引用文件中的相關段落再回答，減少 noise 影響

---

## 輸出格式控制

### 正面指令優先

```text
# 差
Do not use markdown in your response

# 好
Your response should be composed of smoothly flowing prose paragraphs.
```

### 最小化 Markdown 範本

```xml
<avoid_excessive_markdown_and_bullet_points>
When writing reports, documents, technical explanations, analyses, or any long-form content,
write in clear, flowing prose using complete paragraphs and sentences.
Use standard paragraph breaks for organization and reserve markdown primarily for
`inline code`, code blocks (```...```), and simple headings (###).
Avoid using **bold** and *italics*.

DO NOT use ordered lists (1. ...) or unordered lists (*) unless:
a) you're presenting truly discrete items where a list format is the best option, or
b) the user explicitly requests a list or ranking

NEVER output a series of overly short bullet points.
</avoid_excessive_markdown_and_bullet_points>
```

### 消除開場白

```text
Respond directly without preamble. Do not start with phrases like 'Here is...', 'Based on...', etc.
```

---

## 工具使用

### 明確指令觸發動作

```text
# 差（只建議）
Can you suggest some changes to improve this function?

# 好（實際執行）
Change this function to improve its performance.
```

主動執行模式（加入 system prompt）：

```xml
<default_to_action>
By default, implement changes rather than only suggesting them.
If the user's intent is unclear, infer the most useful likely action and proceed,
using tools to discover any missing details instead of guessing.
</default_to_action>
```

保守模式：

```xml
<do_not_act_before_instructions>
Do not jump into implementation or change files unless clearly instructed.
When the user's intent is ambiguous, default to providing information,
doing research, and providing recommendations rather than taking action.
</do_not_act_before_instructions>
```

### 最大化平行工具呼叫

```xml
<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between the tool calls,
make all of the independent tool calls in parallel. Prioritize calling tools simultaneously
whenever the actions can be done in parallel rather than sequentially.
Maximize use of parallel tool calls where possible to increase speed and efficiency.
However, if some tool calls depend on previous calls, call them sequentially.
Never use placeholders or guess missing parameters in tool calls.
</use_parallel_tool_calls>
```

---

## 思考與推理

### 避免過度思考（Opus 4.6）

```text
When you're deciding how to approach a problem, choose an approach and commit to it.
Avoid revisiting decisions unless you encounter new information that directly contradicts
your reasoning. If you're weighing two approaches, pick one and see it through.
```

### Adaptive Thinking 引導

```text
After receiving tool results, carefully reflect on their quality and determine optimal
next steps before proceeding. Use your thinking to plan and iterate based on this new
information, and then take the best next action.
```

控制思考觸發頻率：

```text
Extended thinking adds latency and should only be used when it will meaningfully improve
answer quality — typically for problems that require multi-step reasoning.
When in doubt, respond directly.
```

### Self-check

```text
Before you finish, verify your answer against [test criteria].
```

---

## Agentic 系統

### 長任務 Context 管理

```text
Your context window will be automatically compacted as it approaches its limit, allowing
you to continue working indefinitely from where you left off. Do not stop tasks early due
to token budget concerns. As you approach your token budget limit, save your current
progress and state to memory before the context window refreshes.
Always be as persistent and autonomous as possible and complete tasks fully.
Never artificially stop any task early regardless of the context remaining.
```

### 多 Context Window 工作流程

1. 第一個 context window 建立框架（寫測試、建 setup 腳本）
2. 後續 context windows 根據 todo list 迭代
3. `tests.json` 追蹤測試狀態（結構化 JSON）
4. `progress.txt` 記錄進度（自由文字）
5. 用 git 作狀態追蹤與 checkpoint

```text
This is a very long task. It's encouraged to spend your entire output context working on
the task — just make sure you don't run out of context with significant uncommitted work.
Continue working systematically until you have completed this task.
```

### 自主性與安全的平衡

```text
Consider the reversibility and potential impact of your actions. You are encouraged to
take local, reversible actions like editing files or running tests, but for actions that
are hard to reverse, affect shared systems, or could be destructive, ask the user
before proceeding.

Examples of actions that warrant confirmation:
- Destructive operations: deleting files or branches, dropping database tables, rm -rf
- Hard to reverse: git push --force, git reset --hard, amending published commits
- Operations visible to others: pushing code, commenting on PRs, sending messages
```

### 研究任務結構化方法

```text
Search for this information in a structured way. As you gather data, develop several
competing hypotheses. Track your confidence levels in your progress notes to improve
calibration. Regularly self-critique your approach and plan.
Update a hypothesis tree or research notes file to persist information and provide
transparency. Break down this complex research task systematically.
```

### Code Review Harness（Opus 4.7）

Opus 4.7 更字面遵守過濾指令——如果你說「只報 high severity」它真的會過濾掉低嚴重度。改用覆蓋率優先：

```text
Report every issue you find, including ones you are uncertain about or consider low-severity.
Do not filter for importance or confidence at this stage — a separate verification step
will do that. Your goal here is coverage: better to surface a finding that gets filtered
out than to silently drop a real bug.
For each finding, include your confidence level and an estimated severity so a downstream
filter can rank them.
```

### 避免過度工程

```xml
Avoid over-engineering. Only make changes that are directly requested or clearly necessary.

- Scope: Don't add features, refactor, or make "improvements" beyond what was asked.
- Documentation: Don't add docstrings or comments to code you didn't change.
- Defensive coding: Don't add error handling for scenarios that can't happen.
- Abstractions: Don't create helpers for one-time operations.
```

### 避免只解測試、不解問題

```text
Write a high-quality, general-purpose solution. Do not hard-code values or create
solutions that only work for specific test inputs. Implement the actual logic that
solves the problem generally.
Tests are there to verify correctness, not to define the solution.
```

### 最小化幻覺（Agentic Coding）

```xml
<investigate_before_answering>
Never speculate about code you have not opened. If the user references a specific file,
you MUST read the file before answering. Investigate and read relevant files BEFORE
answering questions about the codebase. Never make claims about code before investigating
unless you are certain — give grounded and hallucination-free answers.
</investigate_before_answering>
```

---

## 遷移注意事項

### Claude 4.6 遷移

1. 具體描述期望行為（加正向修飾詞）
2. 明確要求動畫/互動元素
3. 用 adaptive thinking 取代 `budget_tokens`
4. 廢棄 prefilled responses（改在 user message 用直接指令）
5. 調低過於積極的工具觸發指令（4.6 模型已更主動）

### Sonnet 4.6 Effort 建議

| 情境 | Effort |
|------|--------|
| 多數應用 | `medium` |
| 高流量/延遲敏感 | `low` |
| Agentic/複雜推理 | `high` |

Sonnet 4.6 預設 `high` effort，從 Sonnet 4.5 遷移需顯式設定，否則延遲會升高。

---

## 關鍵速查

| 行為 | 推薦做法 |
|------|---------|
| 控制長度 | 正面描述期望長度；避免 "Don't be verbose" |
| 強制動作 | 用 `<default_to_action>` 或直接命令動詞 |
| 平行工具 | `<use_parallel_tool_calls>` snippet |
| 子代理 | 明確說明何時 spawn、何時不要 |
| 長任務 | 明確說明 context 會自動 compact |
| 推理深度 | 調 effort 優先，再用 prompt 補充 |
| Code review | 強調 coverage > filtering |
| 避免過工程 | 明確列出不要做的事（scope / docs / abstractions）|
