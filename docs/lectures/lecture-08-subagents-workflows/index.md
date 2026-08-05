# Lecture 08：Sub-agents、Agent Teams 與 Dynamic Workflows

## 學習目標

完成本課後，你將能夠：

- 用明確門檻（工具呼叫次數、檔案數）決定是否委派，而非憑感覺
- 區分 Subagent / Agent Team / Dynamic Workflow 三種協作層級的適用邊界
- 套用官方五種 multi-agent 協調模式與六種 workflow 模式
- 說明 2026 W28–W31 的扇出治理變更（上限、巢狀關閉、`/fork` 語義改變）對既有設計的衝擊
- 為背景 session 的自動 commit/push 行為設計正確的約束

## 核心概念

### 三個層級，不要混用

| 層級 | 本質 | Context | 通訊 | Token 成本 |
|------|------|---------|------|-----------|
| **Subagent** | 隔離的 worker | 自己的 window，結果回傳呼叫者 | 只向主 agent 回報結果 | 較低（只有摘要回主 context）|
| **Agent Team** | 平等的協作成員 | 各自完全獨立 | **成員之間可直接互傳訊息** | 較高（每個成員都是獨立 instance）|
| **Dynamic Workflow** | Claude 現寫的協調腳本 | 每個 subagent 獨立，可在獨立 worktree | 由 JavaScript 腳本確定性協調 | 最高（可協調數十到數百 agent）|

> "Claude can now write its own harness on the fly, custom-built for the task at hand."
> — Introducing dynamic workflows in Claude Code

**轉換時機**：跑平行 subagents 但撞到 context limit，或 subagents 需要互相通訊 → Agent teams。任務大到單一 context window 無法協調，且需要並行 + 獨立驗證 → Dynamic workflow。

### 委派的判斷門檻（不是感覺，是數字）

**心智模型**：

> "Will I need this tool output again, or just the conclusion?"

- 只需要結論 → 委派 subagent（中間產物留在 child context）
- 需要反覆檢視中間產物 → 主對話自己做

**硬門檻**：

| 訊號 | 動作 |
|------|------|
| 預期工具呼叫 > 20 次 | **必須**委派 subagent |
| 預期讀取 ≥ 10 個檔案 | 委派 |
| 側邊任務會用大量輸出淹沒主對話 | 委派 |
| 需要隔離工具存取（reviewer 不該有 Write） | 委派 |
| 連續依賴的工作（A 完成才知道 B 要做什麼） | **不要**委派，主對話處理更簡單 |

官方在《Building multi-agent systems》裡把適合多 agent 的場景收斂成三個：**context 隔離、並行執行、專業工具或領域知識**。超出這三個，協調成本通常超過收益——大多數企業工作流用單 agent 更划算。

### 工具作用域原則

委派的一半價值來自「不給它不該有的工具」：

```yaml
researcher:    allowed-tools: Read, Grep, Glob          # read-heavy，只讀
implementer:   allowed-tools: Read, Write, Edit, Bash   # 可寫可執行
reviewer:      allowed-tools: Read, Grep, Glob          # 只讀（不給 Write/Bash）
test-writer:   allowed-tools: Read, Grep, Glob, Write   # 可寫測試，不執行
```

reviewer 不給 Write 不只是防呆——它讓 reviewer 在結構上無法「順手把問題修掉然後宣告通過」，這正是 [Lecture 04](/lectures/lecture-04-harness-architecture/) 說的評估獨立性。

### 五種 Multi-Agent 協調模式（官方）

來自《Multi-agent coordination patterns》。建議**從最簡單的模式開始**，依實際限制逐步演進：

| 模式 | 說明 | 何時用 |
|------|------|--------|
| **Generator-Verifier** | 一個生成、一個驗證 | 最廣泛部署；有明確評估標準的品質輸出 |
| **Orchestrator-Subagent** | 主 agent 分派有界子任務 | 子任務可預先界定 |
| **Agent Teams** | 持續協作的多步驟工作 | 需要討論與交涉 |
| **Message Bus** | 事件驅動非同步管道 | 各方不需同步等待 |
| **Shared State** | 共享狀態即時同步發現 | agent 需要看到彼此的中間發現 |

對應到更基礎的三種工作流形狀（《Common workflow patterns for AI agents》）：**Sequential**（有依賴）、**Parallel**（獨立）、**Evaluator-Optimizer**（迭代改善）。官方反覆強調同一句話：**用解決問題所需的最低複雜度**。

### Dynamic Workflows：Claude 自己寫 harness

Claude 依任務動態撰寫並執行 JavaScript 協調腳本，在同一 session 中協調數十到數百個並行 subagent。它針對三個具體失敗模式：

| 失敗模式 | 說明 |
|---------|------|
| **Agentic laziness** | 複雜多步驟任務中提前停止 |
| **Self-preferential bias** | 需要驗證時偏向自己的結果 |
| **Goal drift** | 連續摘要導致目標漂移 |

**六大 workflow 模式**：

| 模式 | 適用場景 |
|------|---------|
| Classify-and-act | Issue triage、文件分類 |
| Fan-out-and-synthesize | 大型 codebase 搜尋、研究報告 |
| Adversarial verification | 事實核查、安全審查 |
| Generate-and-filter | 程式碼生成、創意工作 |
| Tournament | 排序、尋找最佳解 |
| Loop until done | 遷移、批次處理 |

**實績**：Bun 用 dynamic workflows 把約 75 萬行 Zig 移植到 Rust，11 天完成，通過 99.8% 既有測試——一個 workflow 處理 lifetime mapping，並行 agents 各自 porting，每個檔案配雙 reviewer。

**不要用的時候**：標準編碼任務（不需多 agent 協調）、token 成本敏感的任務（workflows 消耗明顯更多 token）。

**方案限制**：Max、Team Premium、Enterprise PAYG、API 預設可用（Research Preview）；**Pro 不支援**；管理員可關閉。

### 大規模遷移的六步驟框架

《How Anthropic runs large-scale code migrations》給的框架，是 dynamic workflow 最成熟的應用形態：

1. 建立**可移植性規則手冊**
2. 建立詳細**依賴映射**
3. **壓力測試**既有測試套件（沒有客觀評判機制就沒有遷移）
4. 翻譯
5. 編譯
6. 行為驗證

核心理念是「**修復流程而非代碼**」，加上三個實務原則：預先建立評判機制（測試套件即 oracle）、用較小模型處理實作而保留大模型做審查與規則制定、工作隊列應機械化且可恢復（讓編譯器/測試自動生成下一項任務）。

### 2026 W28–W31：扇出治理收緊（會打破舊設計）

官方在 v2.1.202–221 期間的主軸是「**把無界扇出關掉，把背景 agent 的收尾語義補上**」：

| 變更 | 版本 | 內容 |
|------|------|------|
| 每 session subagent 上限 | v2.1.212 | 預設 **200**，`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` 可調；`/clear` 重置 |
| 同時執行上限 | v2.1.217 | 預設 **20**，`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 可調 |
| **預設不再巢狀 spawn** | v2.1.217 | subagent 不再生 subagent；需 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` 才更深 |
| 預算真正止血 | v2.1.217 | `--max-budget-usd` 達標後拒絕新 spawn **並中止執行中的背景 agent** |
| Task 工具 `mode` 參數**廢除** | v2.1.212 | 現已忽略；subagent 預設**繼承 parent 的 permission mode** |
| `/fork` 語義改變 | v2.1.212–213 | `/fork` = 複製成**獨立背景 session**（自有 worktree）；原本的 in-session subagent 改名 **`/subtask`** |
| `context: fork` skill | v2.1.218 | 預設改為背景執行，可用 `background: false` 個別退出 |
| WebSearch 上限 | v2.1.212 | 每 session 預設 200 次 |

**巢狀委派的成本**：即使開啟，server-side hard limit 是 depth 5，最壞情況約 7× 於 depth-1 成本，實務建議控制在 depth 2–3。而且 nesting 的設計動機是 **context isolation，不是 parallelism**——平行化要用扁平 fan-out。

### 背景 session 的收尾語義（安全相關）

v2.1.205 → v2.1.213 定下的行為：背景 session 結束時會 **commit + push 保存工作**，只在任務需要時才開 draft PR，並**遵守你的 CLAUDE.md git 指示**，結束時一定回報工作落在哪。

實務意涵有兩個，都很硬：

1. 如果你不希望 agent 自動 commit/push，**必須寫進 CLAUDE.md**——那是唯一的約束來源，口頭交代或當次 prompt 不夠。
2. 稽核時機從「合併前」提前到「PR review 階段」——因為工作已經被推上去了。

### 強模型需要明確的平行指示

Opus / Fable 這類強模型預設較少自動開 subagent（Opus 4.7 起「更少用工具、多用推理」的傾向被官方明講）。需要平行化就在 prompt 裡直說：

```text
Do not spawn a subagent for work you can complete directly in a single response
(e.g., refactoring a function you can already see).
Spawn multiple subagents in the same turn when fanning out across items
or reading multiple files.
```

反過來，Fable 5 比以往模型**更主動**派發平行 subagent——需要明確定義委派時機，並優先使用非同步通訊（orchestrator 不阻塞等待每個 subagent 返回）。

### Tasks：跨 session 的協作原語

Todos 與 Tasks 不是同一個東西：

| | Todos | Tasks |
|---|-------|-------|
| 儲存位置 | Session 記憶體 | `~/.claude/tasks`（磁碟）|
| 跨 session | ❌ | ✅ |
| Subagent 協作 | ❌ | ✅ 多個 subagent 同時更新 |
| 依賴關係 | ❌ | ✅ Task 可有 dependencies |

跨越多個 session 的長任務、多個 subagent 需協調的複雜工作、coordinator 追蹤多個 worker 進度 → 用 Tasks。

### 四種 Loop 型態

《Getting started with loops》把 agentic loop 分成四類，選擇的關鍵是**退出條件是否可驗證**：

| 型態 | 觸發 | 適用 |
|------|------|------|
| **Turn-based** | 使用者手動 | 較短、非重複任務；用 SKILL.md 封裝驗證步驟 |
| **Goal-based**（`/goal`） | 持續執行至達標或觸及回合上限 | 有可驗證退出條件（如 Lighthouse ≥ 90）|
| **Time-based**（`/loop`、`/schedule`） | 排程 | 週期性工作、監控外部系統 |
| **Proactive** | 事件驅動 | 大規模明確定義的工作，結合 auto mode 與 dynamic workflows |

## 程式碼範例

### 單一訊息啟動多個 Subagent

```text
# 正確：同一訊息平行啟動
請同時啟動三個 subagent：
1. researcher：分析 src/auth/ 的認證流程，只回傳流程圖與關鍵檔案清單
2. test-writer：為 auth module 補測試，不要修改 src/ 下的實作
3. doc-writer：更新 auth 相關 README

# 錯誤：序列啟動（浪費 wall-clock）
先啟動 researcher，等它完成再啟動 test-writer……
```

多個 subagent 並行執行時，總時間約等於執行**一個**的時間。

### 一個寫得完整的委派 brief

Subagent **不繼承**父對話的 context，brief 必須自給自足：

```text
Goal：找出 src/ 下所有使用 SQLAlchemy 1.x session 語法的位置。

Context：本專案已遷移到 SQLAlchemy 2.0 async API。舊語法的特徵是直接呼叫
Session()、使用 db.session 屬性，或用 `user.preferences = x` 這種 attribute
assignment 而非 update() 語句。新語法一律經由 src/db/session.py 的 get_db()。

Done-when：回傳一份清單，每項含 檔案路徑、行號、問題描述。
不要修改任何檔案。找不到就回傳空清單，不要猜。
```

三個要素缺一不可：**Goal / Context / Done-when**，且 Done-when 要能機械驗證。

### 自訂 subagent 定義

```markdown
---
name: security-reviewer
description: 審查變更的安全性。用於任何觸及認證、授權、加密或使用者輸入處理的 diff。
model: opus
allowed-tools: Read, Grep, Glob
skills:
  - reviewing-migrations
---

你是獨立的安全審查者。你**不能**修改任何檔案——你的職責是回報，不是修復。

對每個發現，輸出：
- file:line
- 具體的 exploit path（不是「這裡可能有風險」）
- severity：blocking / important / nit

沒有發現就回傳「無發現」。不要為了顯得有產出而編造 nit。
```

### 觸發 Dynamic Workflow

```text
# 直接請求
> create a workflow that migrates every internal fetch() call to the new HttpClient wrapper

# 讓 Claude 自行決定何時使用
> /effort ultracode

# 管理執行中的 workflows
> /workflows

# 設定 token 預算
> create a workflow to refactor the auth module, use 10k tokens

# 結合 /goal 定義完成條件
> /goal all tests pass; create a workflow to fix failing tests
```

儲存供重複使用：`~/.claude/workflows/`（個人）或透過 skill 發布。

### 用環境變數調整扇出上限

```bash
# 預設值就是安全值，只在明確知道原因時才調
export CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION=200   # 每 session 總量
export CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=20     # 同時執行數
export CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=2      # 巢狀深度（預設 0 = 不巢狀）
export CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION=200

# 預算硬止血（會中止執行中的背景 agent）
claude --max-budget-usd 5
```

### 在 CLAUDE.md 約束背景 session 的 git 行為

```markdown
## Git 行為（背景 session 同樣適用）

- 一律用 `git add <明確檔名>`，禁止 `git add -A` 與 `git add .`
- commit 前先跑 `git branch --show-current`；不在 main 上直接 commit
- **不要自動 push**。完成後只 commit 並在回報中列出 commit hash。
- 不開 PR，除非我在任務描述中明確要求。
```

這段必須在 CLAUDE.md 裡，不能只在 prompt 裡講——背景 session 的收尾行為只讀 CLAUDE.md。

## 常見問題與注意事項

**Q：`/fork` 和 `/subtask` 現在到底差在哪？**

A：v2.1.212–213 之後，`/fork` 是把當前對話複製成一個**獨立的背景 session**，有自己的 worktree，會自行收尾（commit/push）。`/subtask` 才是原本那個「在當前 session 內開一個 subagent」的行為。如果你的筆記或腳本還寫著舊的 `/fork` 語義，那段已經失效。

**Q：subagent 的 permission mode 怎麼設？**

A：不用設了。Task 工具的 `mode` 參數在 v2.1.212 已廢除並被忽略，subagent 一律繼承 parent 的 permission mode。任何依賴 `mode` 降權或升權的設計都要改寫。

**Q：巢狀 subagent 為什麼預設關掉？**

A：因為它同時觸發成本失控與 OOM 風險，而且大多數人以為自己需要的是巢狀，實際需要的是扁平扇出。巢狀的正當用途只有 context isolation（深層 debug、多階段研究），平行化請用 flat fan-out。

**Q：Agent Teams 要怎麼啟用？**

A：實驗性功能，預設關閉，設 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`。v2.1.178 起簡化：不再需要 `TeamCreate`/`TeamDelete`，每個 session 自動有隱含 team，直接用 `Agent` 工具的 `name` 參數 spawn 隊友。

**Q：subagent 回報「已完成」可以直接採信嗎？**

A：不可以。這是 [Lecture 10](/lectures/lecture-10-verification/) 的核心——**產出者不驗收自己的產出**，child 的 verdict 不是證據。確定性 gate（測試、lint、type check）必須由 parent 親自跑一次。

**Q：workflow 中斷了怎麼辦？**

A：Dynamic workflows 支援從最後 checkpoint 恢復。設計 workflow 時把「工作隊列機械化且可恢復」當成需求——讓編譯器或測試的失敗清單自動決定下一項任務，而不是靠模型記得做到哪。

**Q：`allowed_tools` 在 sub-agent 裡好像沒生效？**

A：v2.1.172 有已知 bug：`Agent()` 的 `allowed_tools` allowlist 在深層 sub-agent 中可能被靜默忽略。防禦做法是在 prompt 層也顯式寫明工具限制（例如「你不能修改任何檔案」），不要只依賴 frontmatter。

## 本課小結

- **三個層級**：Subagent（隔離 worker）→ Agent Team（同儕通訊）→ Dynamic Workflow（Claude 現寫的協調腳本）。用最低複雜度解決問題。
- **委派有硬門檻**：預期工具呼叫 > 20 次或讀 ≥ 10 個檔案必須委派；連續依賴的工作反而不該委派。
- **多 agent 只有三個正當理由**：context 隔離、並行執行、專業工具/知識。其餘場景協調成本大於收益。
- **W28–W31 收緊扇出**：每 session 200、同時 20、**預設不巢狀**、`mode` 參數廢除、`/fork` 改為獨立背景 session（原行為改名 `/subtask`）。
- **背景 session 會自動 commit/push**，CLAUDE.md 是唯一約束來源，必須寫明。
- **Dynamic workflow 針對三個失敗模式**：agentic laziness、self-preferential bias、goal drift。實績是 75 萬行 Zig→Rust、11 天、99.8% 測試通過。
- **委派 brief 要自給自足**：Goal / Context / Done-when，且 Done-when 可機械驗證。

## 延伸閱讀

- [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/) — Sub-agent 作為 Context Firewall 的原理
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/) — Generator/Evaluator 分離
- [Lecture 09：模型選型與 Effort 經濟學](/lectures/lecture-09-model-selection/) — 為每個 subagent 選對檔位
- [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/) — child verdict 不是證據

**官方一手來源**

- [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code)（2026-04-07）
- [Multi-agent coordination patterns: Five approaches and when to use them](https://claude.com/blog/multi-agent-coordination-patterns)（2026-04-10）
- [Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)（2026-01-23）
- [Common workflow patterns for AI agents—and when to use them](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them)（2026-03-05）
- [Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)（2026-05-28）
- [A harness for every task: dynamic workflows in Claude Code](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)（2026-06-02）
- [How Anthropic runs large-scale code migrations with Claude Code](https://claude.com/blog/ai-code-migration)（2026-07-16）
- [Getting started with loops](https://claude.com/blog/getting-started-with-loops)（2026-06-30）
- [Building effective human-agent teams](https://claude.com/blog/building-effective-human-agent-teams)（2026-06-24）
- [Agent view in Claude Code](https://claude.com/blog/agent-view-in-claude-code)（2026-05-11）
- [官方文件：Sub-Agents](https://code.claude.com/docs/en/sub-agents)

**站內研究歸檔**

- [Sub-Agent / MCP / Skill 進階](/research/best-practices/04-subagent-mcp-skill)
- [Dynamic Workflows 完整指南](/research/best-practices/32-dynamic-workflows)
- [W28–W31 新功能（v2.1.202–221）](/research/best-practices/48-w28-w31-features)
