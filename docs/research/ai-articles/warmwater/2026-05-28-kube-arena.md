---
url: "https://warmwater.dev/blog/kube-arena"
title: "用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄"
date: 2026-05-28
category: Implement
source: warmwater.dev
---

[
← Implement ](/blog?tag=Implement)  Implement 
 
# 用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄
 
 2026-05-28 · — views  
  
  
建 SRE agent 的時候，我第一個卡住的問題不是「agent 怎麼寫」，而是「我怎麼知道它有沒有在好好思考」。


Unit test 確認工具調用格式正確，integration test 確認 agent 最終解決了問題，但這兩者都沒辦法告訴我：它是因為理解了問題才修好的，還是靠多試幾個工具碰巧成功的？當 agent 在 50 步內修好了一個 CrashLoop，我想知道：它用了幾步找到 root cause？哪些工具調用是在浪費時間？它有沒有形成假設、驗證假設，還是只是在盲目掃描？


Kube Arena 是我為了回答這些問題做的東西。


**讀完精華版（2 分鐘），你會理解：**


- Kube Arena 的三個核心組件以及為什麼這樣拆
- 為什麼用 LLM 做評估而不是 rule-based
- Hero 設計成 plug-in 的原因


這篇不是使用教學，是它為什麼這樣設計的說明。


---


## 精華版


### 三個核心組件


| 組件 | 角色 | 實作 |
| --- | --- | --- |
| Dungeon Master | 在 k3d 上佈署壞掉的 K8s 環境 | scenario.yaml + K8s manifests |
| Hero | 進去診斷修復的 SRE agent | 任何 OpenAI-compatible API |
| Evaluator / Analyst | 確認修好沒有、評估 agent 表現 | rule-based checker + DM LLM |


### 幾個設計問題的直接回答


**為什麼用真實 k3d 而不是 mock？**
Agent 面對 mock 和面對真實 cluster 的行為不一樣。Mock 只能模擬預期的工具回傳；真實 cluster 會給你 race condition、不穩定狀態、意外的 event log。我想測試 agent 面對真實 Kubernetes 的思考方式，不是面對我預先寫好的假資料。


**為什麼用 LLM 做評估而不是 rule-based？**
Tool-call trajectory 太豐富，rule-based 只能判斷對錯，判不了效率。同樣是修好一個 Pod，有人用 3 步診斷到根因，有人繞了 12 步才找到。這些差異在 pass/fail 裡看不到。Analyst LLM 讀完完整的 tool-call trajectory，給出 `efficiency_score`、`wasted_steps`、`mistakes`、`strengths` 和一段 narrative——這是 rule-based 給不出來的。


**Hero 為什麼設計成 plug-in？**
Kube Arena 帶了一個最簡的參考 Hero：50 行的 ReAct loop，拿到 kubectl tools 就跑。這個 Hero 的目的是確認框架可以 end-to-end 跑通，不是「推薦的 agent 架構」。真正的意圖是讓你把自己的 SRE agent（帶 memory、帶 planning、帶自己的工具集）接進來，指向 `HERO_API_BASE`，其餘的框架包辦。評估框架的價值不在 agent 本身。


**評估輸出長什麼樣？**
每次 run 完可以拿到：efficiency score（1-10）、wasted steps 列表、mistakes 列表、strengths 列表、verdict（success/failure/partial）和一段 2-3 句的 narrative summary。Web dashboard 上可以看 event timeline 和跑 Analyse。


---


> 
以下是完整版，按需取用。


---


## 為什麼 pass/fail 不夠評估 SRE Agent？


大多數 agent evaluation 的做法是跑幾個 end-to-end test，看 agent 最終有沒有產出正確結果。對 coding agent 來說這還算夠用——output 是程式碼，有固定的正確性標準。SRE agent 不一樣。Kubernetes 故障環境是動態的，同一個問題可以有多條診斷路徑，成功修好不代表過程有效率。一個靠 brute force 工具調用最終修好問題的 agent，和一個用三步精準定位根因的 agent，在 pass/fail 的評估下看起來一模一樣。


我想要的是能看見 agent 推理過程的評估框架，而不只是知道最終結果對不對。


## Kube Arena 的架構：三個角色怎麼分工？


整個系統只有三個角色，結構很乾淨。


**Dungeon Master** 負責在本地 k3d cluster 上製造壞掉的環境。DM 讀取 `scenario.yaml`，把對應的 manifest 打進 cluster，等 `ready_check` 通過才宣告場景就緒。`ready_check` 例如「確認 Pod 已經進入 CrashLoopBackOff 至少 3 次」——這讓 Hero 面對的是真實的 cluster 狀態，而不是剛 apply 完還沒出現症狀的環境。


**Hero** 是被評估的 SRE agent。它收到 namespace 和一行 hint，拿到一組 kubectl tools，開始診斷。Hero 是一個 OpenAI-compatible chat completions endpoint，任何符合這個介面的 agent 都可以直接接進來，不需要改任何框架代碼。


**Evaluator** 分兩層。第一層是 rule-based `Checker`，確認 success criteria 是否全部達成。第二層是 LLM `Analyst`，把完整的 tool-call trajectory 丟給 DM LLM，拿回結構化的評估結果。


```
scenario.yaml → Dungeon Master → k3d cluster
 ↓
 Hero (你的 agent)
 ↓
 tool-call events
 ↓
 Checker (pass/fail) + Analyst (LLM)
 ↓
 run report
```


## Scenario 怎麼定義故障和成功條件？


一個 scenario 只需要兩個檔案：


```
scenarios/custom/my-scenario/
├── scenario.yaml # metadata, ready_check, success_criteria
└── manifests/ # 打進 cluster 的 K8s YAML
```


`scenario.yaml` 的結構決定了「場景準備好了」和「場景被解決了」怎麼判斷：


```
ready_check:
  type: pod_condition
  namespace: arena-crashloop
  condition: CrashLoopBackOff
  min_restarts: 3
  timeout_seconds: 120

success_criteria:
  - type: all_pods_running
 namespace: arena-crashloop
  - type: no_crashloop
 namespace: arena-crashloop
```


`ready_check` 解決了一個實際問題：manifest 剛 apply 完到 Pod 真的開始 crash 之間有時間差。沒有這個等待，Hero 看到的可能是還沒出現症狀的正常環境，診斷數據就沒有意義了。


`success_criteria` 可以堆多個條件，全部通過才算成功。這讓「部分修好」的情況也能被 Checker 捕捉到，不需要在 Analyst 的 narrative 裡才發現。


目前內建 5 個 scenario：crashloop（exit non-zero）、OOM kill、Pod 卡 Pending（resource limits）、Service selector 不符 pod labels、ConfigMap 不存在。這些不是特別刁鑽的 case，但已經足夠區分「有在思考的 agent」和「在亂猜的 agent」。


## 為什麼用 LLM 評估，而不是 rule-based check？


`evaluator/analyst.py` 是整個 evaluation pipeline 裡最有意思的部分。每次 Hero 調用一個 tool，就有一筆事件記錄：turn number、tool name、args、result summary（前 200 字）。一個 8 步的診斷過程大概長這樣：


```
Turn 1: kubectl_get({"resource": "pods", "namespace": "arena-crashloop"})
Turn 2: kubectl_describe({"resource": "pod/broken-app-xxx", ...})
Turn 3: kubectl_logs({"pod": "broken-app-xxx", ...}) => Error: ...
Turn 4: kubectl_patch({...}) => patched
Turn 5: kubectl_get({"resource": "pods", ...}) => Running
```


Analyst 收到這份 trajectory，加上 scenario 描述和 success criteria 結果，輸出：


```
{
  "efficiency_score": 8,
  "wasted_steps": [],
  "mistakes": [],
  "strengths": ["Went directly to describe after initial get, hypothesis-driven"],
  "verdict": "success",
  "narrative": "The Hero correctly identified the error from logs in Turn 3 and applied a targeted fix. Clean diagnostic path."
}
```


如果是 brute force 的 agent：


```
{
  "efficiency_score": 4,
  "wasted_steps": [
 "Repeated kubectl_get pods 3 times without learning new information",
 "Checked unrelated namespaces before focusing on the hinted one"
  ],
  "mistakes": ["Applied patch before reading logs — diagnosis was incomplete"],
  "verdict": "success",
  "narrative": "Eventually resolved the issue but the path was inefficient. ..."
}
```


兩個 agent 都修好了問題，verdict 都是 success，但 Analyst 的輸出一眼就能看出差距。這是設計這層評估的主要原因：你看到的不只是對錯，是 agent 有沒有在推理。


DM 和 Hero 可以是完全不同的模型。用一個比較強的模型做 DM/Analyst，用你正在測試的 agent 做 Hero，是合理的設定。


## 內建的最小 Hero 是什麼？


Kube Arena 帶的參考 Hero，主要目的是讓你先跑通整個 pipeline，看看評估輸出長什麼樣。`agent/loop.py` 是一個純粹的 ReAct loop：


```
def run_agent_loop(client, system_prompt, user_message, tools_schema, tool_dispatcher, ...):
 messages = [{"role": "system", ...}, {"role": "user", ...}]
 for turn in range(1, max_turns + 1):
 response = client.chat(messages, tools_schema)
 if not response.tool_calls:
 return {"result": "DONE", "turns": turn, ...}
 for tc in response.tool_calls:
 result = tool_dispatcher[tc.name](tc.arguments)
 on_event({"turn": turn, "tool": tc.name, ...})
 messages.append({"role": "tool", "content": result})
```


這個 Hero 沒有 memory、沒有 planning、沒有診斷策略。跑幾個 scenario 之後，在 Analyst 的報告裡會看到：efficiency score 偏低、wasted_steps 是一堆重複的 `kubectl_get`、缺乏假設驅動的診斷。


這是設計意圖。最小 Hero 讓你看清楚「沒有特別設計的 agent 在真實環境下長什麼樣」，對比也更明顯——當你接進一個帶有 planning 的 agent，Analyst 的報告會直接告訴你差在哪。


## 怎麼設計自己的 Scenario？


Kube Arena 帶了一個 Claude Code skill `/generate-scenario`。你用自然語言描述想製造什麼故障，它提出 namespace、fault 設計、success criteria 和 hero hint，確認後直接寫出 `scenario.yaml` 和 manifests。


Scenario 也可以手寫。K8s manifest 就是普通的 YAML，唯一需要注意的是 fault 要在 Hero 拿到 hint 之前就已經出現——這就是 `ready_check` 存在的原因，確認 cluster 真的已經進入故障狀態再開場。


## 下一步：Dungeon 能不能自己進化？


目前 DM 是完全人驅動的：你設計場景，你決定什麼壞了。Analyst 在每次 run 後已經知道 Hero 在哪裡卡關了，自然的延伸是把這份分析餵回 DM，讓它自動生成針對弱點的新 scenario——如果 Hero 下次很快就過了，這是有意義的改進訊號。


更進一步是從真實事件庫合成 scenario。SRE 團隊的 incident 記錄、postmortem、runbook，本身就是高品質的 scenario 素材。一個更自主的 DM 可以讀這些記錄，把真實事件轉化成可重現的 Kube Arena scenario，不需要人工設計每一個故障。


這些方向都還沒實作。Kube Arena 現在是一個可以跑通的評估框架，不是一個自主系統。基礎建好之後，這些是自然的下一步，也是我最想聽社群意見的部分——如果你有在做 SRE agent，你最想測試的故障類型是什麼？


> 
**結語**：測試 agent 夠不夠好，最直接的方法是讓它面對真實的問題，然後看它的每一步。

  
  
 [ Implement ](/blog?tag=Implement)[ System Design ](/blog?tag=System%20Design) 
 

### 相關文章
[System Design

MCP、CLI、還是直呼 API？先看工具長什麼樣

2026-05-23
](/blog/mcp-cli-api-integration)[
System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)
