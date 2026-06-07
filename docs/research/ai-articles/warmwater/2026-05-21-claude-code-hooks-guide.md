---
url: "https://warmwater.dev/blog/claude-code-hooks-guide"
title: "Claude Code 五個組件的觸發邏輯，以及為什麼 Hooks 是最被低估的那一個"
date: 2026-05-21
category: Tutorial
source: warmwater.dev
---

[
← Tutorial ](/blog?tag=Tutorial)  Tutorial 
 
# Claude Code 五個組件的觸發邏輯，以及為什麼 Hooks 是最被低估的那一個
 
 2026-05-21 · — views  
  
  
你能用 Claude Code 完成任務——但你還在親自做這些事：改完 code 手動叫它跑 formatter、每次新 session 再解釋一次你的 coding 規範、忘記說「幫我驗證一下」然後它宣稱完成但其實沒有。


這些問題的共同根源不是 prompt 寫不夠好，是少了一層機制讓系統自己守規矩。這一層就是 Hooks。


**讀完這篇，你會理解：**


- Claude Code 五個組件各自的觸發方式，以及這個差別為什麼重要
- 「手動散裝」與「Plugin 封裝」的差別是什麼，以及它們如何不影響組件的運作邏輯
- Hook 的機制設計：exit code、四種 handler type、async 執行
- Hooks 依功能的七種分類，以及每類在解決什麼真實問題


這篇是工具書性質——你可以從頭讀，也可以直接跳到你需要的那個功能類別。


---


## Claude Code 的五個組件，各自怎麼觸發？


Claude Code 的執行生態有五個核心組件。大部分人知道它們的存在，但不清楚它們的觸發邏輯——而這個邏輯決定你可以在哪些地方讓自動化發揮作用。


```
flowchart TB
 subgraph PLUGIN_BOX["📦 Plugin 封裝 — 別人幫你打包好的一整包"]
 PLUGIN["Plugin<br/>包含：Skills、Hooks、Commands、MCP Servers、CLAUDE.md 片段"]
 end

 PLUGIN -->|"安裝後展開，每個組件的運作方式完全相同"| MANUAL

 subgraph MANUAL["🔧 手動散裝 — 自己逐一放進 .claude/ 目錄"]
 direction LR
 CLAUDE_MD["CLAUDE.md<br/><br/>每個 Session 開始時<br/>自動讀取"]
 HOOKS["Hooks<br/><br/>自動觸發<br/>（事件驅動）"]
 SKILLS["Skills<br/><br/>手動呼叫<br/>或被 Hook 間接觸發"]
 COMMANDS["Commands<br/><br/>手動呼叫"]
 MCP_SERVERS["MCP Servers<br/><br/>Claude 主動決定<br/>要不要呼叫"]
 end
```


這張圖有兩個維度值得注意：


**左側（手動散裝）vs 右側（Plugin 封裝）** 描述的是組件從哪裡來，不是它怎麼運作。Plugin 安裝之後，展開的還是同一批組件，Hooks 還是事件驅動，Commands 還是手動呼叫，沒有任何改變。Plugin 只是封裝形式，不改變任何組件的觸發邏輯。


**觸發方式** 才是真正的差別：


| 組件 | 觸發方式 | 你能控制的是 |
| --- | --- | --- |
| CLAUDE.md | session 開始自動讀取 | context 的內容 |
| Hooks | 事件驅動，條件符合自動執行 | 在哪個事件點插入什麼邏輯 |
| Skills | 手動 /skill-name，或被 Hook 間接觸發 | 封裝哪些可複用流程 |
| Commands | 手動 /command-name | 封裝哪些常用操作 |
| MCP Servers | Claude 主動決定要不要呼叫 | 提供哪些工具 |


Hooks 是唯一一個「條件符合就自動跑」的組件，這讓它能做其他組件做不到的事：在你不參與的情況下，系統自己處理格式化、安全驗證、記錄 context、觸發測試。其他組件都需要你或 Claude 主動選擇呼叫，只有 Hooks 不用。


---


## CLAUDE.md 是什麼，怎麼讀取？


CLAUDE.md 是 Claude 每個 session 都會自動讀取的 context 文件，放在 repo 根目錄、`src/` 目錄、或任何 subdirectory 都可以，Claude 讀取時會依目錄層次組合。


它告訴 Claude 這個 repo 的規則是什麼：測試怎麼跑、哪些目錄是 generated code 不要動、commit message 的格式是什麼、用什麼 formatter。沒有它，Claude 每次 session 都是新人進場，什麼都得重新解釋。


CLAUDE.md 本身是靜態的——你寫什麼它就讀什麼。讓它動態更新的是 Hooks（SessionEnd hook 在 session 結束後提出 CLAUDE.md 的更新建議），這是為什麼 Hooks 的功能分類裡有「記憶 & 自我改善」這一類。


---


## Skills 是什麼，怎麼呼叫？


Skills 是可複用的流程文件，儲存在 `.claude/skills/` 目錄。每個 skill 是一份 markdown，描述一個特定情境下的操作流程——debug 怎麼做、code review 的 checklist、特定 framework 的最佳實踐。


手動呼叫方式是 `/skill-name`，Claude 會讀取對應的 skill 文件並按照流程走。


間接觸發的路徑是：你設定一個 SessionStart hook，在每個 session 開始時把 using-skills 這類 meta-skill 注入 context，讓 Claude 學會「遇到對應情境要主動呼叫 skill」。Skills 本身沒有事件監聽能力，是 Hook 替它創造了「自動觸發」的外觀。


---


## Commands 是什麼，跟 Hooks 的根本差別在哪？


Commands 定義在 `.claude/commands/` 目錄，每個 command 是一個 markdown 文件，使用 `/command-name` 呼叫。


可以把它理解成 shell alias，不是「有什麼能力」，而是「把常用的一組操作包起來，方便叫」。比如 `/commit` 可以是：讀 staged changes、寫 commit message、確認後 commit 的整個流程。


Commands 永遠是手動觸發的，這是它和 Hooks 最本質的差別。


---


## MCP Servers 是什麼，Claude 怎麼決定要不要呼叫？


MCP（Model Context Protocol）Servers 提供 Claude 連接外部系統的工具——查 Linear ticket、搜尋 Confluence、呼叫公司 API、讀 Grafana metrics。


設定好之後，Claude 在每次回應前會判斷「這個問題需不需要用到某個 MCP tool」，如果需要就呼叫。你不用每次手動說，但 Claude 不一定每次都會呼叫，這由它自己判斷。


---


## Plugin 是什麼，跟手動散裝有什麼差別？


Plugin 解決的是分發問題。一個工程師研究出了一套好用的 hooks + skills + commands 組合，但沒有 Plugin 機制，這套設定只有他自己有。


一個 Plugin 的目錄結構：


```
.claude-plugin/
  plugin.json # 元數據：名稱、版本、依賴
  skills/ # 這個 plugin 帶來的 skills
  commands/ # 這個 plugin 帶來的 commands
  hooks/ # 這個 plugin 帶來的 hooks
  mcp/ # 這個 plugin 帶來的 MCP server 設定
  CLAUDE.md.fragment # 要 append 進你的 CLAUDE.md 的 context 片段
```


安裝 Plugin 之後，這些組件就融入你的 `.claude/` 環境，運作方式與手動放進去完全相同。


常見的 Plugin 類型：`superpowers`（AI coding agent 行為約束）、`code-reviewer`（PR 審查流程）、`debugging`（root-cause 追蹤）。


---


## Hooks 是什麼：在 Agent Loop 的每個節點插入自訂邏輯


現在進入 Hooks 的核心。


Claude Code 的執行有一個 agent loop：接收 prompt → 思考 → 呼叫 tool → 讀取結果 → 繼續思考 → 產生回應。這個 loop 的每個節點，Hooks 都可以插入自訂邏輯。

 Hook 事件在 Agent Loop 的觸發點
 
 Session 開始
 
 SessionStart 
  
↓
  
 使用者送出 Prompt
 
 UserPromptSubmit可擋 
  
↓
  
 Claude 思考・規劃
  
↓
  
 Tool Call Loop（可重複多次）
 
  呼叫 Tool
 
 PreToolUse可擋 PermissionRequest可擋 
  
↓
 
 Tool 執行
  
↓
 
 讀取 Tool 結果
 
 PostToolUse 
  
↓
 
 批次 Tool 全部完成
 
 PostToolBatch可擋 
  
↑ 需要更多 Tool 時回到頂端重複
 
↓
  
 Claude 產生回應
 
 Stop可擋 StopFailure（錯誤時） 
  
↓
  
 Session 結束
 
 SessionEnd 
 
 多 Agent 協作（有 Subagent 時額外觸發）
 
 SubagentStart SubagentStop TaskCreated TaskCompleted TeammateIdle 
 
  Session 層級

 
 Turn 層級

 
 Tool 層級

 
 Hook可擋
可阻擋（exit 2）

  

設定位置是 `.claude/settings.json` 的 `hooks` 欄位：


```
{
  "hooks": {
 "PostToolUse": [
 {
 "matcher": "Write|Edit",
 "hooks": [
 {
 "type": "command",
 "command": "npx prettier --write \"$CLAUDE_TOOL_INPUT_FILE_PATH\""
 }
 ]
 }
 ]
  }
}
```


### Exit Code 機制：三種結果，只有一種能阻擋


每個 hook 透過 exit code 跟 Claude Code 溝通：


| Exit Code | 意義 | Claude 的行為 |
| --- | --- | --- |
| 0 | 成功 | stdout 的 JSON 內容會被傳給 Claude |
| 2 | 阻擋 | 操作停止，stderr 傳給 Claude 說明原因 |
| 其他非零 | 錯誤 | 顯示給使用者，但執行繼續 |


最常見的 bug 是用 `exit 1` 想阻擋操作，但 exit 1 不阻擋——**只有 exit 2 能阻擋**。


阻擋時 stderr 的內容很重要，因為 Claude 會讀到並決定下一步怎麼做：


```
#!/bin/bash
if echo "$CLAUDE_TOOL_INPUT_COMMAND" | grep -q "rm -rf"; then
  echo "阻擋：rm -rf 需要人工確認，請說明刪除原因" >&2
  exit 2
fi
exit 0
```


### 四種 Handler Type


**Command hooks**（最常用）— 執行 shell script 或系統指令：


```
{
  "type": "command",
  "command": "python validator.py",
  "timeout": 30
}
```


**HTTP hooks**（Feb 2026 新增）— POST 到任何 HTTP endpoint，適合整合內部服務：


```
{
  "type": "http",
  "url": "http://localhost:8080/hooks/pre-tool-use",
  "timeout": 30,
  "headers": { "Authorization": "Bearer $MY_TOKEN" },
  "allowedEnvVars": ["MY_TOKEN"]
}
```


Body 是標準的 hook 事件 payload，response body 的 JSON 會被 Claude 讀到。


**Prompt hooks** — 用 LLM 判斷，回傳結構化決策：


```
{
  "type": "prompt",
  "prompt": "Claude 宣稱完成了 task，評估它是否真的完成：$ARGUMENTS。回傳 {\"ok\": true} 或 {\"ok\": false, \"reason\": \"...\"}",
  "timeout": 30
}
```


適合「規則太複雜，寫 shell script 維護成本高」的情境。


**Agent hooks** — 生成一個有 Read/Grep/Glob 工具的 subagent 做完整的 codebase 驗證：


```
{
  "type": "agent",
  "prompt": "確認所有修改過的函式都有對應的測試，列出缺少測試的函式",
  "timeout": 60
}
```


Agent hook 可以真正讀 codebase，不只是看 event payload。


### Async 執行（Jan 2026 新增）


加上 `"async": true`，hook 在背景執行，不阻擋 Claude 繼續工作：


```
{
  "type": "command",
  "command": "python log_to_datadog.py",
  "async": true
}
```


適合 logging、通知、備份——你不需要等結果，只是需要它發生。


---


## Hooks 依功能可以分成哪七類？


32+ 個 hook 事件看起來很多，但它們的存在都有設計意圖。按功能分類之後，你會發現 Hooks 在解決的是七個完全不同的工程問題。


### 一、守門員：安全 & 合規邊界


**目標**：在 Claude 做某件事之前攔截，確認可以繼續。


**主要事件**：`PreToolUse`、`UserPromptSubmit`、`PermissionRequest`


`PreToolUse` 是最重要的守門員 hook，在任何 tool 呼叫之前執行。透過 `matcher` 可以指定只在特定 tool 觸發：


```
{
  "hooks": {
 "PreToolUse": [
 {
 "matcher": "Bash",
 "hooks": [
 {
 "type": "command",
 "command": "bash hooks/safety-check.sh"
 }
 ]
 }
 ]
  }
}
```


`safety-check.sh` 讀取 `$CLAUDE_TOOL_INPUT_COMMAND`，對危險操作返回 exit 2。


實際場景：


- 阻擋 `git push --force` 到 main
- 阻擋生產資料庫的 DROP 指令
- 阻擋刪除超過一定大小的目錄


`PermissionRequest` 是更細的控制點——當 Claude Code 本來要彈出「需要你點 Allow」的對話框時，這個 hook 可以程式化地決定要不要直接 approve，不用人工點。適合 CI 環境或你已知某類操作永遠安全的情境。


守門員 Hooks 的工程意義：**規則不在 prompt 裡，規則在系統裡**。放在 CLAUDE.md 裡說「不要 force push」，Claude 有時候會遵守、有時候不會。放在 PreToolUse hook 裡，是硬性阻擋，Claude 沒有選擇。


---


### 二、品質自動化：讓 Claude 做完，系統收尾


**目標**：在 tool 執行完之後自動做格式化、linting、測試——不需要你額外要求。


**主要事件**：`PostToolUse`、`PostToolBatch`


最常見的入門 Hook 就是這類：


```
{
  "hooks": {
 "PostToolUse": [
 {
 "matcher": "Write|Edit|MultiEdit",
 "hooks": [
 {
 "type": "command",
 "command": "npx prettier --write \"$CLAUDE_TOOL_INPUT_FILE_PATH\""
 }
 ]
 }
 ]
  }
}
```


每次 Claude 寫入或編輯檔案，prettier 自動跑。Claude 不需要知道你用 prettier，你也不需要每次提醒它。


`PostToolBatch` 是在一批平行 tool call 全部完成後觸發，適合「等所有檔案改完再跑測試」的情境，而不是每個檔案改完就跑一次：


```
{
  "hooks": {
 "PostToolBatch": [
 {
 "hooks": [
 {
 "type": "command",
 "command": "npm test --changed"
 }
 ]
 }
 ]
  }
}
```


品質自動化 Hooks 的工程意義：**品質標準從「人記得說」變成「系統保證執行」**。不管是哪個工程師、哪個 session、有沒有在 prompt 提到格式化，結果都一致。


---


### 三、動態 Context 注入：在對的時機給 Claude 對的知識


**目標**：不要讓 Claude 每次都「空手上工」，在它開始工作之前注入相關 context。


**主要事件**：`SessionStart`、`UserPromptSubmit`


靜態的 CLAUDE.md 有一個問題：你的 monorepo 有 20 個 service，每個 service 有自己的測試指令、部署流程、技術棧，全部塞進 CLAUDE.md 讓每個 session 讀 context 太長。


SessionStart hook 可以根據工作目錄動態載入對應知識：


```
#!/bin/bash
# hooks/session-start.sh
DIR=$(pwd)
CONTEXT=""

if [[ "$DIR" == *"/services/payments"* ]]; then
  CONTEXT=$(cat .claude/contexts/payments-service.md)
elif [[ "$DIR" == *"/services/auth"* ]]; then
  CONTEXT=$(cat .claude/contexts/auth-service.md)
fi

if [ -n "$CONTEXT" ]; then
  echo "{\"context\": \"$CONTEXT\"}"
fi
```


Hook 的 stdout 輸出為 JSON，`context` 欄位的內容會被注入到 Claude 的 context 裡。


`UserPromptSubmit` 則是在 Claude 處理 prompt 之前觸發，可以在 prompt 送達之前補充動態資訊——當前的 git branch、最近的 CI 狀態、相關 ticket 的描述：


```
#!/bin/bash
BRANCH=$(git branch --show-current)
LAST_COMMIT=$(git log -1 --pretty=format:"%s")
echo "{\"context\": \"Current branch: $BRANCH\nLast commit: $LAST_COMMIT\"}"
```


這也是 Superpowers 的 SessionStart hook 運作方式：在 session 開始時注入 using-superpowers skill 的內容，讓 Claude 學到「遇到相關情境要主動呼叫對應 skill」。


動態 Context 注入的工程意義：**知識在需要的時候出現，不是在不需要的時候佔空間**。


---


### 四、記憶 & 自我改善：讓系統從每次使用中學習


**目標**：session 結束後，把有價值的決策和發現記錄下來，讓下次更好。


**主要事件**：`SessionEnd`、`Stop`


這是 Hooks 最被低估的功能類別。


`SessionEnd` 在 session 結束時觸發，可以用 prompt 或 agent handler 做回顧：


```
{
  "hooks": {
 "SessionEnd": [
 {
 "hooks": [
 {
 "type": "prompt",
 "prompt": "分析這個 session 學到的東西：$ARGUMENTS。如果有值得加進 CLAUDE.md 的規則或模式，以 JSON 格式輸出建議。",
 "timeout": 60
 }
 ]
 }
 ]
  }
}
```


這讓 CLAUDE.md 成為一個活的文件——不是你寫完就固定的 context，而是每次 session 結束後都可能更新的知識庫。


`Stop` 在 Claude 完成回應時觸發，可以用 agent handler 在背景記錄：


```
{
  "hooks": {
 "Stop": [
 {
 "hooks": [
 {
 "type": "command",
 "command": "python record_session_insights.py",
 "async": true
 }
 ]
 }
 ]
  }
}
```


記憶 & 自我改善的工程意義：**把工程師的知識資本從個人腦袋，轉移到系統**。一個工程師在某個 service 踩過的坑，透過 SessionEnd hook 記錄進 CLAUDE.md，下一個工程師開新 session 就讀得到。


---


### 五、觀測 & 可追蹤性：知道 Agent 在做什麼


**目標**：建立 agent 行為的 audit trail，整合進你現有的 observability 系統。


**主要事件**：任何事件 + `"async": true`


在 production 環境或有合規要求的情境，你需要知道 agent 呼叫了什麼指令、改了哪些檔案、在什麼時間點。


```
{
  "hooks": {
 "PostToolUse": [
 {
 "hooks": [
 {
 "type": "command",
 "command": "python log_tool_use.py",
 "async": true
 }
 ]
 }
 ]
  }
}
```


`log_tool_use.py` 讀取環境變數（`$CLAUDE_TOOL_NAME`、`$CLAUDE_TOOL_INPUT_*`、`$CLAUDE_TOOL_RESULT_*`）並送到 Datadog、Elastic、或你自己的 log 系統。加上 `async: true` 讓它在背景跑，不影響 Claude 的工作節奏。


HTTP hook 在這裡很自然：


```
{
  "type": "http",
  "url": "https://your-observability-service/hooks/tool-use",
  "async": true
}
```


觀測 & 可追蹤性的工程意義：**agent 行為不再是黑盒子**。知道它做了什麼，才能診斷問題、優化流程、滿足 audit 要求。


---


### 六、回應驗證：不相信 Claude 的話


**目標**：Claude 說完成了，讓系統確認，不只是相信它說的。


**主要事件**：`Stop`（搭配 prompt 或 agent handler）


「我已經修好了！」然後跑起來還是壞的——這個 pattern 非常常見。Stop hook 讓你在 Claude 宣稱完成之後插入一個驗證步驟：


```
{
  "hooks": {
 "Stop": [
 {
 "hooks": [
 {
 "type": "agent",
 "prompt": "Claude 宣稱已完成任務。請驗證：1) 有沒有跑測試？2) 測試通過了嗎？3) 修改的檔案語法是否正確？如果驗證失敗，回傳具體失敗原因。",
 "timeout": 60
 }
 ]
 }
 ]
  }
}
```


Agent handler 可以真正跑指令確認，不只是根據 session 內容推斷。


這個 hook 搭配 exit 2 可以做到：「除非驗證通過，否則不讓這個 turn 結束」——但要注意這可能讓 agent loop 陷入無限驗證循環，設計時需要加上失敗上限或條件。


回應驗證的工程意義：**完成的定義從「Claude 說完成了」變成「系統確認完成了」**。把驗證從人工 review 的環節，前移到 agent loop 裡。


---


### 七、多 Agent 協調：Orchestrate 並行工作


**目標**：在多個 subagent 並行工作時，管理協調、狀態同步、工作分配。


**主要事件**：`SubagentStart`、`SubagentStop`、`TaskCreated`、`TaskCompleted`、`TeammateIdle`


當你的工作流程用到 parallel subagents（比如同時讓多個 agent 處理不同 service 的 migration），這類 hook 讓你在各個節點插入協調邏輯：


```
{
  "hooks": {
 "SubagentStart": [
 {
 "hooks": [
 {
 "type": "command",
 "command": "python register_agent.py --agent-id \"$CLAUDE_AGENT_ID\""
 }
 ]
 }
 ],
 "TaskCompleted": [
 {
 "hooks": [
 {
 "type": "http",
 "url": "http://localhost:8080/orchestrator/task-done"
 }
 ]
 }
 ]
  }
}
```


`TeammateIdle` 在一個 agent 閒置時觸發，可以用來動態分配還沒完成的工作——有點像 worker queue 的 dequeue 邏輯，但用 hook 實現。


多 Agent 協調的工程意義：**複雜工作流程的協調邏輯從外部腳本移進 agent lifecycle 裡**。orchestration 不再是你在外面寫一個 Python script 輪詢狀態，而是系統在正確的事件點自己觸發。


---


## Hook 事件完整參考：觸發時機與典型用途


以下按觸發層級整理所有 Hook 事件的名稱、觸發時機、是否可阻擋操作，以及最常見的用途。


### Session 層級


| 事件 | 觸發時機 | 可阻擋？ | 典型用途 |
| --- | --- | --- | --- |
| SessionStart | session 開始或 /resume 時 | ❌ | 動態 context 注入、載入 skills |
| Setup | --init / --maintenance 啟動時 | ❌ | 環境初始化 |
| SessionEnd | session 正常結束時 | ❌ | 記錄洞見、提出 CLAUDE.md 更新 |


### Turn 層級


| 事件 | 觸發時機 | 可阻擋？ | 典型用途 |
| --- | --- | --- | --- |
| UserPromptSubmit | Claude 處理 prompt 前 | ✅ | 補充動態 context、過濾 prompt |
| Stop | Claude 完成回應時 | ✅ | 回應驗證、記錄洞見 |
| StopFailure | API 錯誤導致 turn 結束 | ❌ | 錯誤記錄、告警 |


### Agentic Loop


| 事件 | 觸發時機 | 可阻擋？ | 典型用途 |
| --- | --- | --- | --- |
| PreToolUse | tool 執行之前 | ✅ | 安全驗證、合規檢查 |
| PostToolUse | tool 成功之後 | ❌ | 格式化、linting、logging |
| PermissionRequest | 需要使用者授權時 | ✅ | 程式化 approve/deny |
| PostToolBatch | 一批平行 tool 全部完成後 | ✅ | 跑測試、整合驗證 |


### Agent & Team


| 事件 | 觸發時機 | 典型用途 |
| --- | --- | --- |
| SubagentStart | 啟動 subagent 時 | 記錄、注入 context |
| SubagentStop | subagent 結束時 | 聚合結果、記錄狀態 |
| TaskCreated | 新 task 建立時 | 記錄、通知 |
| TaskCompleted | task 完成時 | 觸發下游工作、通知 |
| TeammateIdle | agent 閒置時 | 動態工作分配 |


---


## 怎麼設定 Hooks？settings.json 語法與常用環境變數


完整的 settings.json 結構：


```
{
  "hooks": {
 "PreToolUse": [
 {
 "matcher": "Bash|Write|Edit",
 "hooks": [
 {
 "type": "command",
 "command": "python hooks/pre-tool-validator.py",
 "timeout": 30
 }
 ]
 }
 ],
 "PostToolUse": [
 {
 "matcher": "Write|Edit|MultiEdit",
 "hooks": [
 {
 "type": "command",
 "command": "npx prettier --write \"$CLAUDE_TOOL_INPUT_FILE_PATH\"",
 "timeout": 15
 }
 ]
 }
 ],
 "SessionEnd": [
 {
 "hooks": [
 {
 "type": "prompt",
 "prompt": "分析這個 session，輸出值得加進 CLAUDE.md 的規則建議",
 "timeout": 60,
 "async": true
 }
 ]
 }
 ]
  }
}
```


`matcher` 使用 pipe-separated 的正則表達式，只有 tool name 符合的 tool call 才會觸發這個 hook。不加 `matcher` 代表對所有 tool call 觸發。


常用的環境變數：


| 變數 | 說明 |
| --- | --- |
| $CLAUDE_TOOL_NAME | 當前 tool 的名稱（Bash、Write、Edit…） |
| $CLAUDE_TOOL_INPUT_COMMAND | Bash tool 的指令內容 |
| $CLAUDE_TOOL_INPUT_FILE_PATH | Write/Edit tool 的目標檔案路徑 |
| $CLAUDE_TOOL_RESULT_* | PostToolUse 可讀到 tool 的執行結果 |
| $CLAUDE_AGENT_ID | 當前 subagent 的 ID |


---


## 第一次設定 Hooks，建議從哪裡開始？


如果你現在才開始設定 Hooks，建議的順序：


**第一個 Hook**：PostToolUse + formatter。最低風險、最立即有感，不需要任何 exit 2 邏輯，跑完就有效果。


**第二個 Hook**：PreToolUse + Bash 安全檢查。找幾個你覺得 Claude 不應該跑的指令，寫進阻擋規則。


**第三個 Hook**：SessionStart + 動態 context 注入。如果你的 repo 有多個 service 或多個 context，把目錄判斷邏輯加進去。


**第四個 Hook**：Stop + 回應驗證。用 prompt handler 確認 Claude 說完成時，它真的完成了。


在這四個 Hook 設定完之後，你的 Claude Code 跟裸裝狀態的差別就已經很明顯了——格式化自動、危險指令阻擋、context 隨 repo 結構動態切換、完成驗證不再靠感覺。


> 
Hooks 的本質是把「你以為需要靠人提醒 Agent 的事」，轉化成「系統在正確的節點自動執行的邏輯」。從需要人看管到能自我管理，這一層是關鍵的分水嶺。

 
 [ Tutorial ](/blog?tag=Tutorial) 
 

### 相關文章
[Tutorial

第一個 Claude Skill：用 skill-creator 打包可重用工作流程

2026-05-25
](/blog/create-your-own-claude-skill)[
Tutorial

為什麼你的 Claude Code 用起來跟別人不一樣？

2026-05-14
](/blog/claude-code-commands-beginner)[
Viewpoint

Python AI 工程師為什麼要學 TypeScript？

2026-05-10
](/blog/why-python-ai-engineers-learn-typescript)
