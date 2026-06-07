---
url: "https://warmwater.dev/blog/token-saving-four-assumptions"
title: "你在省 Token，還是在省思考？四種廢話假設比較"
date: 2026-05-19
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# 你在省 Token，還是在省思考？四種廢話假設比較
 
 2026-05-19 · — views  
  
  
Context window 快滿的時候，工程師的第一反應通常是找工具壓縮。市面上有四個做這件事的工具：RTK、context-mode、caveman、code-review-graph。它們都聲稱能節省 token，但翻過它們的 source code 之後，我發現一件有趣的事：它們切入的假設完全不同。


每個工具都在回答同一個問題——「什麼是廢話？」——但答案各不相同。這個差異不只是設計風格，而是背後對「LLM 真正需要什麼」的不同理論。


**讀完這篇，你會理解：**


- 四個工具各自認定哪裡在浪費 token，以及這個判斷背後的邏輯
- 每個假設在什麼情況下成立，什麼情況下會錯
- 選工具之前，應該先問的問題是什麼


這篇不是安裝教學，也不是功能比較表。是一個關於「如何思考 context window 管理」的討論。


---


## Context window 是過濾問題，不是記憶體問題


一個常見的誤解是把 context window 想成記憶體——滿了就要清。但更準確的理解是：context window 是 LLM 在推理時能看到的資訊總量，而每一個 token 都在競爭這個預算。


這個理解會改變問題的問法。問題不是「怎麼塞更多東西進去」，而是「哪些東西進去之後能讓 LLM 思考得更好，哪些只是佔位」。


在一個 30 分鐘的 coding session 裡，context 的消耗來自好幾個方向：CLI 命令的輸出、工具回傳的資料、AI 本身的回覆、還有每次都要讀的 memory file。每一層都有可能藏著大量對推理沒有貢獻的資訊。


四個工具各自盯著其中一層。它們的設計選擇，反映的是它們認為「廢話」從哪裡來。


---


## 四個工具，四種不同的廢話定義


### RTK：命令輸出的格式雜訊


RTK 的觀點是：問題出在 CLI 命令輸出本身的格式，不在程式碼或對話。


執行 `cargo test` 會吐出 200 行輸出。其中 180 行是進度條、ANSI escape codes、物件計數、樣板確認文字。真正有用的是最後 20 行——失敗的測試名稱、錯誤訊息、行號。前面那 180 行對 LLM 的判斷沒有任何貢獻，但它們全部進了 context。


RTK 坐在 LLM agent 和 CLI 之間做 proxy。PreToolUse hook 自動把 `cargo test` 改寫成 `rtk cargo test`，Rust binary 攔截輸出並過濾，只把有用的部分回傳。對 LLM 來說，命令還是正常執行了，只是輸出變乾淨了。


```
原本：cargo test → 200 行 → ~5,000 tokens
RTK： rtk cargo test → 20 行  → ~500 tokens
```


RTK 的廢話定義：格式雜訊，以及那些「命令正在執行中」的中間狀態資訊。


### context-mode：把原始資料直接塞進 context 的習慣


context-mode 的觀點不同：問題出在開發者（和 LLM 本身）對工具的使用習慣——拿到資料就往 context 丟。


一個 GitHub Issues 列表有 59KB。其中 95% 對當前任務無關，但整份塞進了 context。一份 access log 45KB，只需要最後幾條 error，但 LLM 被要求「分析一下這個 log」，於是全讀了。


context-mode 的解法是把大量資料隔離在 sandbox，讓 context 只收「答案」。它的 `ctx_execute` 在 OS 的 temp 目錄建立一個獨立子程序執行 JavaScript，原始資料永遠不離開 sandbox，只有 `console.log()` 的結果進入 context。


```
// before: agent 直接 curl，59KB JSON 進 context
// after: agent 呼叫 ctx_execute
ctx_execute("js", `
  fetch("https://api.github.com/repos/...")
 .then(r => r.json())
 .then(issues => console.log(issues.slice(0, 5)))
`)
// 只有 5 條 issue 的摘要進 context，約 1.1KB
```


對於更大的輸出，context-mode 走的是更激進的路：stdout 超過閾值時，整份自動 index 進 SQLite FTS5 knowledge base，context 只收到一個 pointer（「已 index N sections，請用 ctx_search 查詢」），從不做截斷。


context-mode 的廢話定義：原始資料本身，以及 LLM 把自己當資料處理器的習慣。


### caveman：AI 說話方式本身的冗餘


caveman 切入的是另一個完全不同的層：AI 的輸出風格。


「I’d be happy to help you with that! Let me first explain the background context before diving into the solution…」這種文字消耗了大量 output token，但不包含任何技術資訊。一個 React re-render 的 debug 回答需要的可能只是三句話，但 LLM 會把它包裝成 15 句客套英文。


caveman 的解法是純粹的 prompt engineering：強制 AI 用「智慧穴居人」語法回答，去掉冠詞、客套話、廢話，允許語法片段。


```
normal: "Because by default, React re-renders all children when a parent
 re-renders, regardless of whether their props changed. To prevent
 this behavior, you should wrap the component in React.memo..."
 → 1,180 tokens

caveman: "Parent re-render → child re-render by default. Fix: React.memo(Child)."
 → 159 tokens
```


它的哲學：“Brain still big. Mouth small.” 技術推理的思考不受影響，壓縮的只是表達。


除了壓縮 output，caveman 還有一個 `caveman-compress` 路徑：把 CLAUDE.md 等 memory file 本身也壓縮成 caveman 語法，讓每次 session 開始讀取時省 46% input tokens。


caveman 的廢話定義：AI 表達方式的社交潤滑成分，以及 memory file 裡的過度解釋。


### code-review-graph：與 diff 無關的程式碼


code-review-graph 切入的是 code review 工作流。它的觀點是：AI 在 review PR 時不需要讀整個 codebase，只需要知道「誰受到這個 diff 影響」。


問題在於，預設行為是讀大量甚至全部原始碼。在 500 個檔案的 repo 裡，一個修改了 `auth.py` 裡 `validate_token()` 函式的 PR，AI 不需要讀所有 500 個檔案——但沒有額外設定的話，它往往就這樣做了。


code-review-graph 的解法是靜態分析 + 圖遍歷。它用 Tree-sitter 解析 24 種語言的 AST，把整個 codebase 建成一個 call graph，存進 SQLite。當 PR 進來時，它從 `git diff` 的行範圍精確識別被修改的函式（不是整個檔案），然後用雙向 BFS 找出 blast radius——depth=2 之內的相關節點集合。


```
// LLM 收到的不是原始碼，是結構性 JSON
{
  "summary": "Analyzed 3 files, 8 functions, 2 test gaps",
  "risk_score": 0.72,
  "changed_functions": ["auth.py::validate_token"],
  "test_gaps": ["auth.validate_token", "db.execute_query"],
  "review_priorities": [...]
}
```


這是兩層設計：第一層 graph 縮小範圍（blast radius）；第二層用 `get_review_context` 讀取被識別到的函式的實際原始碼，精確到 `±2-3` 行。AI 不是看不到函式主體，而是只看到 graph 判斷相關的那些函式。


code-review-graph 的廢話定義：與 diff 無因果關係的程式碼內容。


---


## 支撐每個廢話定義的設計假設


每個「廢話定義」都需要一個支撐它的假設，說明為什麼這樣壓縮是安全的。


**RTK 假設**：signal 可以靜態定義。「cargo test 失敗時有用的資訊」這件事是可以提前知道的，而且對大多數專案都適用。這個假設成立在格式相對標準化的工具上。RTK 用 50 個 Rust 模組和 60 個 TOML filter 模組預先定義了這些 signal。


**context-mode 假設**：LLM 不該當資料處理器。如果你需要從 59KB JSON 裡找 5 筆資料，正確的做法是寫一段計算邏輯去篩，而不是把整份資料丟給 LLM 讓它慢慢讀。計算成本遠比 LLM 推理便宜，而且結果更準確。這個假設在「資料量遠大於問題複雜度」的情境下幾乎永遠成立。


**caveman 假設**：技術推理的品質和語言表達的方式是正交的。「React.memo(Child)」和「To prevent this behavior, you should wrap the component in React.memo…」傳遞的技術資訊完全相同，只是後者多了 10 倍的 token。這個假設在高度技術性的問題上成立，但有邊界——稍後會談到。


**code-review-graph 假設**：code review 是圖遍歷問題，不是文本理解問題。理解 `validate_token()` 被修改後的影響，需要知道誰呼叫它、它呼叫誰、有沒有測試覆蓋它——這些是圖上的邊，不是文本搜尋能找到的。Graph 的結構性 metadata 包含的資訊密度，比直接讀原始碼還高。


---


## 假設的邊界：什麼情況下會失效？


每個假設都有邊界條件，也就是工具設計者必須面對的 trade-off。


**RTK 的盲點**：Claude Code 的原生工具（`Read`、`Grep`、`Glob`）不走 Bash hook，RTK 攔不到。如果 AI 用原生工具讀了大量檔案，RTK 完全看不見。沒有對應 filter 的自訂工具節省率為 0%，你需要自己寫 TOML filter。工具的有效範圍被限制在 RTK 認識的那些 CLI 命令上。


**context-mode 的盲點**：如果任務就是需要逐行 review 程式碼，sandbox 隔離反而是障礙——原始碼被關在外面，AI 看不到。另一個問題是平台依賴：Cursor 的 `SessionStart` hook 被 validator 拒絕，session 快照功能在那個平台上失效；Zed 等無 hook 的平台合規率只有 ~60%。


**caveman 的盲點**：架構討論這類需要充分論述的問題，實測只能壓縮 30%，因為那些「廢話」本來就是論述的一部分。另一個問題是模型漂移：長時間 session 中其他 plugin 可能注入競爭性的 style 指令，caveman 的 `UserPromptSubmit` hook 做 per-turn reinforcement 但不能完全保證一致性。


**code-review-graph 的盲點**：動態呼叫（`getattr(obj, method)()`、反射）無法被靜態分析追蹤，不在 graph 裡，也就不在 blast radius 裡，AI 不知道它們受影響。impact precision 實測是 0.38——有大量誤報，工具傾向保守策略（高 recall），但也代表 AI 會看到一些實際上無關的節點。最值得注意的是，小型單檔案變更效果反而更差，Express.js 的實測結果是 0.7x（比不用 graph 還耗 token），因為 graph 的建立和遍歷本身有 overhead，在小變更上得不償失。


這些不是 bug，是設計取捨。工具設計者選擇了某個假設，就必須接受它在邊界外的代價。


---


## Context contract：讓 agentic system 知道自己需要什麼


這四個工具都在做 general-purpose 壓縮——RTK 假設「CLI 雜訊對所有任務都是廢話」，caveman 假設「AI 的客套話永遠沒用」。但廢話是相對於任務定義的，不是絕對的。


同樣是「AI 看到一個函式的完整原始碼」，在 code review 任務裡這可能是必要資訊，在 data analysis 任務裡則完全不相關。一個 subagent 的詳細推理過程，在 debugging 任務裡可能有參考價值，在 orchestrator 需要的是結論的情境下就是純粹的佔位。


這帶出一個 agentic system 設計層面的問題：**不同類型的 step，需要的 context 結構根本不同。**


把這四個工具的策略對應到常見的 agent 工作情境，會更清楚：


| Agent Step | 有用的 context | 佔位的 context | 適合的壓縮策略 |
| --- | --- | --- | --- |
| Debugging 失敗測試 | 具體 error、指向自己程式碼的 stack frame、失敗的 assertion | passing test 輸出、library internal、coverage stats | RTK（信號高度結構化，可靜態定義） |
| PR / code review | diff、blast radius 內的 caller/callee、測試缺口 | 所有跟 diff 無因果關係的檔案 | code-review-graph（blast radius 就是 context contract） |
| API / log 分析 | 計算後的結論、anomaly、summary | raw JSON body、完整 log 文件 | context-mode sandbox（結論 < 1% 原始資料大小） |
| Subagent 向 orchestrator 回報 | 結論、行動項目、風險 | subagent 的完整推理過程、verbose 解釋 | caveman-ultra（brain still big, mouth small） |


四個工具各自針對一個 scenario 把 context contract 硬編碼進去了。在一個設計良好的 agentic system 裡，可以更進一步：讓每個 step 宣告自己的 context contract——「這個 step 需要哪類資訊才能推理」——然後由 harness 層根據 step 類型動態套用對應的過濾策略。


這樣做的回報不只是省 token。LLM 的注意力機制在 context 愈乾淨、信噪比愈高的情況下，推理品質會更穩定。把不相關的東西留在 context 裡不只是浪費預算，還可能干擾判斷——尤其在 long-horizon 任務裡，context 累積的佔位資訊愈多，後期步驟的推理可靠度就愈難保證。


把 context 管理做成 agentic system 的一層設計，而不是事後補上的壓縮工具，這是讓 agent 任務成功率真正提升的方向。


---


> 
**小發想**：這四個工具可以同時使用，因為它們攻擊的 token 來源完全不同——CLI 輸出、工具回傳資料、AI 回覆、code review 輸入。但更值得想的問題是：在你的工作流裡，廢話真的從哪裡來？選工具之前，先回答這個問題，你的選擇會更準確，而且可能比你想像的簡單得多。

  
  
 [ Source Code ](/blog?tag=Source%20Code)[ Harness Engineering ](/blog?tag=Harness%20Engineering) 
 

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
