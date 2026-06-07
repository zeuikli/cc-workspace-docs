---
url: "https://warmwater.dev/blog/claude-code-task-continuity"
title: "Task Continuity，不是 Personal Memory：Claude Code 的 Session 設計"
date: 2026-05-15
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Task Continuity，不是 Personal Memory：Claude Code 的 Session 設計
 
 2026-05-15 · — views  
  
  
大多數討論 Agent 記憶的文章，預設的問題是：「Agent 怎麼記住你是誰、你喜歡什麼？」


Claude Code 問的是一個完全不同的問題：**這個工作做到哪了？下一個 session 從哪裡繼續？**


這兩個問題的答案，會長出完全不同的架構。


---


## Claude Code 的 Tool Output 存在哪裡？


Tool output 只存在 context window 裡——Claude Code 沒有任何機制自動攔截並儲存到 database。每一個 CLI 輸出、每一個 API response，都只是加進對話的一條 `tool_result` message，活著直到 context window 觸發 compaction。


當你讓 Claude Code 執行 `find . -name "*.ts"` 或呼叫一個外部 API，那個輸出存在哪？答案是：context window 裡，僅此而已。


Compaction 在 200k token 時觸發，使用確定性算法（不呼叫 LLM）壓縮對話。它保留的是結構性狀態：


```
pending work ← 還有什麼沒做完
key files ← 動過哪些路徑
tool mentions  ← 用了哪些工具
recent requests← 最近幾個 user request
```


它不保留 tool output 的內文。你的 `find` 結果、你的 API response、你的 `kubectl describe pod` 輸出——compaction 之後都消失了。


**這個設計的含義是：** 要讓重要的 tool output 活過 compaction，LLM 必須在當下主動把它 Write 到某個持久化的地方。這不會自動發生，需要 LLM 的介入。


---


## Session 生命週期的三個 Hook 分別做什麼？


Claude Code 的三個 session lifecycle hooks——SessionStart、SessionEnd、PreCompact——是 task continuity 的基礎設施，分別在 session 開始、結束、和 context 壓縮前觸發，各自負責不同的工作：


**SessionStart**：session 開始時，掃描 `.claude/sessions/` 裡最近 7 天的 `*-session.tmp` 檔案，找到就透過 stderr 告訴 LLM：


```
[SessionStart] Found 3 recent session(s)
[SessionStart] Latest: .claude/sessions/2026-05-14-abc123-session.tmp
```


注意：這不是自動載入內容。LLM 收到的是通知，它自己決定要不要去讀那個 `.tmp` 檔。


**SessionEnd**：session 結束時，建立（或更新時間戳的）`.tmp` 檔案骨架。同時觸發 `evaluate-session.js`，讀 Claude Code 注入的 `CLAUDE_TRANSCRIPT_PATH` 環境變數，數 user message 數量，如果夠長就透過 stderr 告訴 LLM：


```
[ContinuousLearning] Session has 24 messages - evaluate for extractable patterns
[ContinuousLearning] Save learned skills to: ~/.claude/skills/learned/
```


**PreCompact**：context 壓縮前，直接 `appendFile()` 在 `.tmp` 裡加一行時間戳記：


```
---
**[Compaction occurred at 14:32]** - Context was summarized
```


這是三個 hook 裡唯一完全不需要 LLM 的，純粹的環境行為。


---


## Hook 為什麼不直接處理記憶，只發訊號？


Claude Code 的 hooks 不自動儲存記憶內容——它們只透過 stderr 發訊號，讓 LLM 自己決定要做什麼。把三個 hook 放在一起，這個 signal channel 模式很清楚：


```
Hook fires → stderr → Claude Code → LLM context → LLM acts

SessionStart: scan fs  → 通知 LLM 有哪些 session
SessionEnd: 建 template + 讀 transcript → 通知 LLM 去提取 patterns
evaluate-sess:  數 messages → 通知 LLM 值不值得提取
PreCompact: 直接寫檔 → 不通知 LLM（純 deterministic）
```


**Hook 的工作是建基礎設施和發訊號，不是自動處理記憶內容。**


`.tmp` 檔案的骨架長這樣，但 hook 只產生這個結構，裡面的內容全部是空的：


```
## Current State
[Session context goes here]

### Completed
- [ ]

### In Progress
- [ ]

### Notes for Next Session
-

### Context to Load
[relevant files]
```


**填這個內容，是 LLM 的工作。** LLM 收到 `evaluate-session.js` 的 stderr 訊號，再用自己的 Write tool 把當前 task 狀態寫進去。


這個設計和 hermes-agent 的 `memory` tool 是相反的方向：hermes 的 tool 是 LLM 呼叫一個 Python 函數，函數做 I/O；claude-code 的 hook 是環境發訊號，LLM 決定用自己的工具做什麼。前者是「工具替 LLM 存」，後者是「環境提醒 LLM 自己存」。


---


## PostToolUse 怎麼把 Tool Call 變成可學習的 Instinct？


`PostToolUse` hook 把每一次 tool call 的 input/output 捕捉到 `observations.jsonl`，再交給 background agent（輕量模型）分析，提煉成帶 confidence score 的 instinct 原子行為。這是 session lifecycle hooks 之外，everything-claude-code 更細緻的一層學習機制：


```
id: prefer-grep-before-read
trigger: "when searching for patterns in codebase"
confidence: 0.7
domain: "debugging"
source: "session-observation"

# Prefer Grep Before Read

## Action
Use Grep to locate files before reading them. Avoids loading irrelevant content.

## Evidence
- Observed 5 instances where Read was called on wrong file
- More efficient pattern observed on 2026-01-15
```


每個 instinct 是一個原子行為：一個 trigger、一個 action、一個 confidence score（0.3–0.9）、以及觀察到的 evidence。


這個設計的關鍵在 observation 的可靠性。如果用 Stop hook（session 結束時）讓 LLM 去回顧整個 session，LLM 不一定會提取，或者提取的品質不穩定。`PostToolUse` 是確定性的——每一次 tool call 都被捕捉，沒有遺漏。


觀察是 100% 可靠的 hook 做，分析是 LLM 做——兩件事分開，各做各擅長的。


---


## .tmp 工作交接單為什麼這樣設計？


`.tmp` 的四個區塊——Completed、In Progress、Notes for Next Session、Context to Load——每個有不同的受眾和用途，合起來是工作狀態交接單，不是記憶。結構值得細看：


```
### Completed ← 已做完，下次不需要帶
### In Progress  ← 下次的起點
### Notes for Next Session  ← LLM 對未來自己的提示
### Context to Load  ← 哪些 file 要馬上讀
```


`Completed` 是存在給「人」看的，確認進度；但對下一個 session 的 LLM，它不需要被載入。


`In Progress` 才是真正的 task state handoff——「我昨天挖到這裡，今天從這裡繼續」。


`Context to Load` 更有趣：它不是存知識，是存指標。下一個 session 不是靠讀 .tmp 就能恢復 context，而是靠 .tmp 告訴它哪些 file 要讀，然後自己重新建立對這些 file 的理解。


這三個部分合起來是一個 **工作狀態交接單**，不是記憶，是指引。


---


## Task Continuity 和 Personal Assistant 是兩種根本不同的問題


Claude Code 和 hermes-agent 的差異不是功能多寡，而是在回答完全不同的問題：一個記的是工作狀態，另一個記的是用戶是誰。把這些設計放在一起：


|  | Claude Code | hermes-agent |
| --- | --- | --- |
| 記憶主體 | 工作狀態（task 在哪） | 用戶（你是誰） |
| Session 是什麼 | 一個工作單元 | 一次對話 |
| 記憶目的 | Task 跨 session 存活 | 個人化、長期陪伴 |
| 適合場景 | Coding、SRE、pipeline | 個人助手、長期對話 |
| 記憶失效的代價 | Task 重做 | 個人化失效 |


如果你要建一個 K8s SRE agent、一個 code review agent、一個 data pipeline agent——你的問題是 task continuity，不是 personal memory。這兩個問題需要的架構，不是同一個東西的不同程度，是根本上的不同方向。


一個更有意思的問題：**這兩層可以分開嗎？**


答案應該是可以的。外層負責「你是誰」（hermes 的 frozen notes、user profile）；內層負責「這件事做到哪了」（claude-code 的 session handoff、task state）。外層的 user context 在 session 開始時注入給內層，內層不需要自己維護「誰在用我」這件事。


這不是一個框架解決的問題，而是兩層各做各的，在 session 開始的時候交接一次。


---


## agentmemory 補的是 Claude Code 的哪個缺口？


  

Claude Code 刻意不做知識累積——它的 hooks 不持久化 tool output，session 結束後所有探索結果都消失。agentmemory 用 12 個掛在同一套 lifecycle events 上的 hooks，補上這個設計選擇留下的缺口。具體是三個空白：


**Tool output 的內容在 compaction 後消失。** Claude Code 執行了幾百次 `find`、`grep`、`kubectl describe`，這些 output 在對話結束後什麼都不剩。下一個 session 需要重新跑一遍，重新探索同樣的 codebase。


**Session 之間沒有語意 recall。** `.tmp` 檔案是純文字交接，LLM 只能讀到「這個 task 做到哪了」，找不到「我之前在類似情況下怎麼解的」。


**Pattern 不會跨 session 累積。** 每次 coding session 發現了架構決策、修了一個 bug、確認了一個不該用的 pattern——這些學到的東西，只要 session 結束，context 消失，它們就消失了。


agentmemory 是一個專門為 Claude Code 設計的補層，它的 12 個 hooks 掛在 Claude Code 同一套 lifecycle events 上，做的是 Claude Code 主動跳過的那件事：


```
SessionStart → 載入相關記憶注入 context（Claude Code 的 hook 掃 .tmp；agentmemory 的 hook 做 recall）
PostToolCall → 自動把 tool input/output 寫入 Working Memory（Claude Code 完全不處理這層）
FileRead → 記錄探索過哪些路徑
FileWrite → 記錄哪些檔案被修改
SessionStop → 觸發記憶鞏固
```


其中 `PostToolCall` 是關鍵：每一次 tool call 的 input 和 output，agentmemory 都自動捕捉進去。這條 hook 填的正好是 Claude Code 留下的那個洞——tool output 的內容不再只活在 context window 裡。


記憶的處理方式是四層鞏固：Working Memory（raw tool calls，當下 session）→ Episodic（session 層級摘要，「上週做了什麼」）→ Semantic（跨 session 提取的事實與模式，「我知道什麼」）→ Procedural（重複出現的工作流，「怎麼做」）。每層有不同的 Ebbinghaus decay rate，越高層的記憶越不衰退——Procedural 記憶幾乎永遠有效。


這個架構回答的是 Claude Code 沒在問的第三個問題：**我從這些工作裡學到了什麼？**


Claude Code 問「工作做到哪」，agentmemory 問「我學到什麼」。兩個問題不衝突，agentmemory 也知道這一點——它內建了 Claude Bridge（port 49134），可以和 Claude Code 的 `MEMORY.md` 雙向同步，讓兩套系統各做各的，在 session 開始時合流一次。


這讓整個 Agent 記憶的圖多了一個維度：


|  | Claude Code | hermes-agent | agentmemory |
| --- | --- | --- | --- |
| 解決的問題 | 工作做到哪了 | 用戶是誰 | 學到了什麼 |
| 記憶主體 | Task state | User profile | Coding knowledge |
| 跨 session 存活的是 | 未完成的工作 | 個人偏好 | 模式與決策 |
| 記憶失效的代價 | Task 重做 | 個人化失效 | 重複探索相同問題 |


這三層不是一個框架能解的，也不應該是。它們各做各的，在 agent 啟動時交接一次。


---


> 
**結語**：Claude Code 的 session 設計告訴我們，Agent 記憶不是一個問題，是兩個：「你記住了誰」和「工作做到哪了」。而 agentmemory 加上了第三個問題：「你學到了什麼」。搞清楚你的 agent 在解哪個問題，架構才不會走錯方向。

  
  
 [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System) 
 

### 相關文章
[System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)[
Source Code

不預裝能力，只定義生長方式：GenericAgent 原始碼解析

2026-05-22
](/blog/generic-agent-source-code)
