---
url: "https://warmwater.dev/blog/mcp-cli-api-integration"
title: "MCP、CLI、還是直呼 API？先看工具長什麼樣"
date: 2026-05-23
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design 
 
# MCP、CLI、還是直呼 API？先看工具長什麼樣
 
 2026-05-23 · — views  
  
  
有人拿出了一個數字：一個有 106 個 tools 的 database MCP server，光初始化就消耗 54,600 tokens，什麼事都還沒做。拿來跟 CLI 比：同樣的操作，一次 tool call + shell filter，約 1,400 tokens。


差距是真實的。但診斷錯了。把 106 個無狀態的資料庫查詢操作包成 MCP server，再拿這個數字說 MCP 有問題——這不是在評估協議，是在評估一個壞的設計決策。MCP 的 token 問題，是「把無狀態工具硬包成有狀態協議」的症狀，不是 MCP 本身的問題。


最近看了 CLI-Anything 和 cli-printing-press 兩個工具之後，我意識到這場辯論漏掉了更前置的問題：你要整合的工具，有什麼介面？這個問題的答案，幾乎決定了後面所有選擇。


**讀完精華版（2 分鐘），你會理解：**


- 三種整合方式各自解什麼問題，以及哪些場景錯誤地互換了
- cli-printing-press 和 CLI-Anything 怎麼填補「工具沒有 agent-native 介面」的空白
- MCP 真正值得引入的五個場景，及那個 54,600 tokens 的誤診


這篇不是教你哪個方案比較好，而是讓選擇從工具的介面類型開始，不從協議偏好開始。


---


## 精華版


| 工具介面類型 | 推薦方案 | 核心理由 |
| --- | --- | --- |
| 已有 CLI（git, kubectl, aws） | CLI-as-Tool | LLM 本來就懂語法，直接給，token 最省 |
| Web API + OpenAPI/GraphQL spec | cli-printing-press | 自動生成 agent-native Go CLI + MCP server |
| GUI 桌面應用（無 API） | CLI-Anything | 反向工程 backend engine，生成 Python REPL CLI |
| 需要 session 且多 agent 共用 | MCP server | 唯一能跨 call 保持連線狀態的方案 |
| 沙盒 / Electron / SaaS（無 terminal） | MCP remote | 沒有 $PATH，CLI 進不去 |
| 企業環境，auth 需集中管理 | MCP gateway | agent 不碰 secret，credential 集中持有 |


每種方案的核心設計邏輯：


- **CLI-as-Tool**：LLM 已經訓練過幾乎所有主流 CLI 語法，不需要包裝層；`git status`、`kubectl get pods`、`aws s3 ls` 直接作為 shell tool，token 使用最小。
- **cli-printing-press**：輸入 OpenAPI spec，輸出 agent-native Go CLI（含 `--json` flag、`doctor` 命令）；Domain Profiler 自動判斷 API 類型（payment/communication/project mgmt），生成對應的 power-user 命令；同時輸出 MCP server 供需要的場景使用。
- **CLI-Anything**：分析 GUI 應用的 backend engine（GIMP→Script-Fu，Blender→bpy，LibreOffice→headless），生成 Python REPL CLI；支援 stateful session（JSON session files）和 `--json` 輸出，讓 agent 不需要 display 就能操作桌面軟體。
- **MCP server**：不是「包裝工具的協議」，而是「連線生命週期的管理層」；54,600 tokens 的問題發生在把無狀態工具錯誤地包成 MCP 時；真正的使用場景是 session 共用、跨環境存取、auth governance。


在決定整合方案前，值得先問四件事：


**你的工具有沒有現成介面？** 有 CLI 直接用；有 OpenAPI/GraphQL spec 用 cli-printing-press；只有 GUI 用 CLI-Anything；什麼都沒有才考慮 Computer Use。


**連線需不需要跨 call 存活？** 一個命令一個結果（無狀態）→ CLI 夠了；需要 login 狀態、session context、跨操作記憶 → REPL mode 或 MCP。


**多少 agent 需要同時存取這個工具？** 單 agent 用 CLI；多個 agent 共用同一個 browser session 或 DB connection pool → MCP gateway 才值得。


**有沒有 terminal？** 有 terminal 的環境幾乎永遠有更簡單的方案；沒有 `$PATH` 的沙盒、SaaS 環境、Electron app 才是 MCP remote 的真正使用場景。


---


> 
以下是完整版，按需取用。


## 54,600 tokens 是設計問題，不是 MCP 的問題


Garry Tan 在 X 上說「MCP sucks」，引用的就是這個數字。Eric Holmes 的論文「MCP is dead」也提到了同樣的問題。兩個人的觀察是準確的，但結論跳太快了。


用 GitHub 這個例子來說明。同樣是讓 agent 列出 issue：


```
# gh CLI
gh issue list --limit 5 --json title,state | jq '.[] | .title'
# token 消耗：~1,400（一次 tool call + shell filter）

# GitHub MCP
# agent 先載入整個 tool manifest（93 個 schema）
# 然後呼叫 list_issues tool
# token 消耗：~55,000（光初始化）
```


差距是 40 倍。但問題出在設計決策，不是協議。GitHub MCP 把 93 個 API 操作全部包進 manifest，每次對話開始都要把所有 schema 載入 context window——55,000 tokens 是這 93 個 schema 的總大小，不是執行任何操作的成本。如果你只需要 `list_issues`，你付的代價包括另外 92 個你根本沒用到的工具定義。


這裡有一個 CLI 的隱性優勢常常被忽略：`gh` 是人和 agent 都能用的介面。production 出問題的時候，你可以直接在 terminal 跑同一行指令重現。MCP 的呼叫你沒辦法直接在 shell 裡重現——多了一層 server，debuggability 就差了一層。


那 GitHub 為什麼還是出了 MCP？不是為了像你這樣有 terminal 的開發者，而是為了跑在 SaaS 環境裡的 agent 產品——那些環境根本沒有 `gh` 可以裝。GitHub MCP 和 `gh` CLI 的目標用戶其實不同。


這個診斷的結論是：MCP 的 token 成本是 tool schema 的大小乘以工具數量。如果你的工具是無狀態的、你有 terminal、你的 agent 只需要少數幾個操作，CLI 幾乎永遠是更好的選擇。「無狀態工具不該包成 MCP」和「MCP 沒有用處」是兩件完全不同的事。


---


## 三種整合模式，各自解的是不同問題


把 agent 的工具整合方式拆開來，本質上只有三種：


**CLI-as-Tool** 是把 shell 命令直接暴露給 agent。這個做法的力量來自一個事實：LLM 在訓練資料裡已經見過幾乎所有主流 CLI 工具的完整用法。`git`、`docker`、`kubectl`、`aws cli`、`jq`——agent 不需要額外說明，直接用就好。Eric Holmes 的核心論點在這裡是對的：為什麼要建一個全新協議，讓 agent 去呼叫那些它本來就懂的工具？


CLI-as-Tool 唯一的弱點是無狀態性。每次呼叫都是獨立的 subprocess，spawn 之後就死掉，沒有辦法在多個操作之間維持上下文。


**MCP server** 解的恰好是這個問題：連線生命週期。一個 browser automation session、一個已登入的 SAP 帳號、一個 DB connection pool——這些資源在多個操作之間需要保持存活，CLI subprocess 做不到。MCP server 作為常駐進程，持有這個連線，讓多個 tool call 都能對著同一個有狀態的資源操作。


額外的好處是標準化。如果五個不同的 agent 都需要存取同一個 Jira 帳號，用 MCP server 集中管理 OAuth token，比讓每個 agent 各自管理 credential 更安全，也更容易稽核。


**直呼 API** 是最輕量的選項：在 agent 的工具定義裡直接寫一個 HTTP call。適合一次性的操作——發一封 webhook、查一個 endpoint——不需要標準化，不需要 session，成本最低。代價是沒有複用性：每個 agent 各自實作，沒有共用的工具層。


三種模式的核心差異不是好壞，而是使用場景不同。混淆發生在「把無狀態操作包成 MCP server」或「把需要 session 的操作強塞給 CLI」的時候。


---


## cli-printing-press：給有 spec 的 API 自動生成 agent-native CLI


當你有一個 Web API 而且有 OpenAPI 或 GraphQL SDL 時，手動包 CLI 是重複勞動。cli-printing-press 把這個工作自動化。


輸入是 API spec（或 spec URL），輸出是一個完整的 Go CLI 專案：


```
/printing-press Discord
→ 解析 Discord OpenAPI spec
→ Domain Profiler 判斷：ArchetypeCommunication（有 threading、media 特徵）
→ 生成對應的 power-user 命令：
 discord messages  # 搜尋訊息
 discord channels  # 列出頻道
 discord sync # 批量拉取（local SQLite cache）
 discord stale # 找到沒更新的頻道
→ 7 gate 品質驗證（go vet / go build / --help / doctor）
→ 輸出：Go CLI + MCP server + AGENTS.md
```


幾個設計細節讓它真的 agent-native：


`--json` flag 是所有命令的標準輸出模式。agent 消費結構化 JSON，不需要解析人類可讀的 table 輸出。`doctor` 命令讓 agent 在開始操作前先做健康檢查，確認連線和 auth 都正常。compound 查詢把多個 API call 合併成一個命令，降低 token 使用。


Domain Profiler 是真正有趣的部分。它分析 APISpec 的 resource name 和 field pattern，自動判斷這個 API 是 project management 味道（有 assignees / due dates / priority）、payment 味道（有 transactions / subscriptions），還是 communication 味道（有 threading / media），然後生成對應的 power-user 命令——不是每個 API 都長一樣，工具的設計也不該長一樣。


生成的輸出裡同時包含 MCP server，所以如果你的 agent 環境需要 MCP，不需要額外的工作。


---


## CLI-Anything：給 GUI 軟體反向工程出 CLI


前面提到的工具都有一個前提：你的軟體要有某種程式化介面。但如果你要整合的是 GIMP、Blender、LibreOffice、OBS Studio——這些為人類設計的 GUI 應用呢？


CLI-Anything 的做法是：分析軟體的 backend engine，把 GUI 操作映射成 CLI 命令。


關鍵的觀察是，大多數 GUI 軟體的架構都是「frontend（GUI）和 backend engine 分離」的。GIMP 的底層是 Script-Fu；Blender 的底層是 bpy Python API；LibreOffice 可以 `--headless` 執行；Inkscape 有 `--actions` 命令列介面；Shotcut 背後跑的是 MLT/ffmpeg。CLI-Anything 的工作是找到這個 backend，然後把它包裝成一致的 Python CLI：


```
# LibreOffice backend 的包裝方式
def convert_odf_to(odf_path, output_format, ...):
 lo = find_libreoffice() # raises RuntimeError with install instructions
 subprocess.run([lo, "--headless", "--convert-to", output_format, ...])
 return {"output": final_path, "format": output_format, "method": "libreoffice-headless"}
```


生成出來的 CLI 有兩種操作模式：Subcommand（一次性操作）和 REPL（維持 session context）。REPL mode 讓 agent 在跨多個操作的工作流程裡不需要每次重新初始化——這就是那個「需要 session 才用 MCP」問題的 CLI 側答案。


生成的 CLI 統一有 `--json` 輸出，讓 agent 消費機器可讀格式。每個 harness 最終都會生成 SKILL.md，讓 agent 可以自動 discover 這個工具的能力。


目前 CLI-Hub 上有 50+ 個 harness：GIMP、Blender、Inkscape、Audacity、OBS Studio、Obsidian、ComfyUI……都是用同一套 HARNESS.md SOP 生成的，對接進任何 agent 的方式一致。


---


## MCP 真正值得引入的五個場景


說完了 CLI 和 CLI 生成工具，MCP 的位置就更清楚了：不是替代 CLI，而是解 CLI 做不到的事。


**沒有 terminal 的環境。** 這是最硬的理由。agent 如果跑在沙盒化的 Electron app 裡、SaaS 平台的 runtime 裡、或任何沒有 `$PATH` 的環境裡，CLI subprocess 根本叫不起來。MCP remote server 是唯一能跨越這個環境邊界的方案。


**Auth 集中管理是硬需求。** 企業環境裡，OAuth token、API key、SSO session 不能散落在每個 agent 裡。MCP gateway 集中持有 credential，agent 本身不接觸 secret，這個安全架構是 CLI wrapper 很難複製的。


**多 agent 共用同一個有狀態的資源。** 一個已登入的 browser session、一個 DB connection pool、一個 SAP 的工作 session——如果五個 agent 都要用，各自維持 session 的成本遠大於共用一個 MCP server。token 消耗是小事。


**跨團隊工具標準化。** 平台團隊維護 MCP server，產品團隊的 agent 直接接。工具更新只改一個地方。如果沒有這層，每個團隊各自維護自己的 CLI wrapper，維護成本才是真正的大頭。


**非技術用戶的 agent 產品。** 一般使用者用的 SaaS agent，背後不可能讓用戶自己裝 CLI、設定 PATH。MCP remote server 是唯一能讓這類產品 work 的架構。


token 消耗是戰術問題，auth 安全、session 共用、跨環境存取是戰略問題。五個場景都不存在的時候，MCP 的 token 消耗就只是純粹的負擔。


---


## 從介面類型開始的完整決策框架


把所有討論收攏起來：


```
你的工具有什麼介面？
│
├─ 已有 CLI（git, kubectl, aws, psql...）
│ └─ CLI-as-Tool，直接用
│
├─ Web API + OpenAPI / GraphQL spec
│ └─ cli-printing-press：一行命令生成 agent-native Go CLI
│
├─ GUI 桌面應用，有原始碼或 headless mode
│ └─ CLI-Anything：反向工程 backend，生成 Python REPL CLI
│
└─ 完全沒有程式化介面
 └─ Computer Use（最後手段）

有了介面之後，問連線的問題：
│
├─ 需要跨 call 維持 session？
│ ├─ 單 agent → REPL mode（CLI-Anything 已內建）
│ └─ 多 agent 共用 → MCP server
│
├─ 沒有 terminal（沙盒、SaaS、Electron）？
│ └─ MCP remote server
│
└─ 企業 auth 集中管理需求？
 └─ MCP gateway
```


「MCP 還是 CLI？」這個問題本身沒有錯，只是問太早了。在問協議之前，先確認介面——這一步想清楚，後面的選擇幾乎會自己浮出來。


---


## 相關文章


- [工具越多越選錯：Tool System 設計分析](/blog/agent-tool-selection-design)
- [SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較](/blog/agent-soul-design-comparison)
- [Claude Code 的五個組件與 Hooks 觸發邏輯](/blog/claude-code-hooks-guide)


---


> 
**結語**：54,600 tokens 的問題從來不是 MCP 的問題，是設計決策的問題。先看你的工具長什麼樣，再決定用什麼方式接——答案通常比辯論裡說的簡單。

  
  
 [ System Design ](/blog?tag=System%20Design) 
 

### 相關文章
[Implement

用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄

2026-05-28
](/blog/kube-arena)[
System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)
