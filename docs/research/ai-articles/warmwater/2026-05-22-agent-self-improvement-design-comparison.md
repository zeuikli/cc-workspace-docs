---
url: "https://warmwater.dev/blog/agent-self-improvement-design-comparison"
title: "Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較"
date: 2026-05-22
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design 
 
# Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較
 
 2026-05-22 · — views  
  
  
在看六個 agentic system 的原始碼時，我發現一個很奇怪的問題：大家都說自己的 agent 會「越用越強」，但這句話背後的工程決策，各系統從根本上就不同。有的系統進化的是知識，有的進化的是工具能力，有的進化的是模型權重，還有兩個系統刻意選擇完全不自動進化。


第一次看到 HermesAgent 同時跑 skill nudge daemon 和 Atropos RL batch runner 時，我以為這是同一件事的兩種做法。後來才搞清楚：兩者進化的目標層不同，一個在 prompt 層，一個在模型層。這個區分讓我重新看待所有系統的設計。


「越用越強」這句話，不同系統理解的方式差很多。GenericAgent 進化的是執行路徑，HermesAgent 同時進化知識庫和模型權重，DeerFlow 進化的是對用戶的認知，NanoClaw 進化的是 agent 能跑什麼工具。HolmesGPT 和 OpenClaw 則刻意選擇不自動進化。同樣叫 self-improvement，設計決策從底層就不同。


**讀完這篇，你會理解：**


- 各系統「進化什麼」的選擇背後各自的邏輯
- 自動進化 vs 人工審核，各方的工程取捨
- 為什麼「刻意不進化」在某些場景下是正確答案
- 如果你在設計自己的 agent 系統，這些選擇意味著什麼


這篇不是教你怎麼實作 self-improvement，而是把六個系統攤開來比，找到設計決策背後的假設和代價。


---


## 精華版


| 系統 | 進化什麼 | 機制 | 觸發方式 | 人工介入 |
| --- | --- | --- | --- | --- |
| GenericAgent | 技能庫（文字 SOP） | Skill crystallization → L3 + L1 index | Agent 主動呼叫 start_long_term_update | 無 |
| HermesAgent | 技能庫 + 模型權重 | Skill nudge（SKILL.md）+ Atropos RL（GRPO） | 自動：每 10 次 tool-call + batch_runner | 無（全自動） |
| DeerFlow | 記憶（user facts） | MemoryUpdater：LLM 分析對話 → 信心值 + 驅逐 | 自動：每次工具執行後 async | 無 |
| NanoClaw | 執行環境（容器能力） | Self-Mod：install_packages → docker rebuild | Agent 呼叫 MCP tool | 必須 human approve |
| HolmesGPT | 無 | Skills 是靜態 playbook | 手動撰寫 | N/A |
| OpenClaw | 技能庫（社群） | ClawHub 市集 + skills_install | 手動安裝 | N/A |


每個系統的核心設計決策：


- **GenericAgent**：只有成功跑通的任務執行路徑才能結晶成 SOP，存進私有 L3 技能庫，L1 Insight Index 做免 RAG 路由；兩個用了半年的用戶，長出的技能樹完全不同。
- **HermesAgent**：六個系統裡唯一同時進化 prompt 層（skill nudge daemon，每 10 次 tool-call 後背景觸發）和模型層（Atropos GRPO 訓練），複雜度最高，API cost 和維護難度也最高。
- **DeerFlow**：不積累技術 SOP，只更新對特定用戶的認知模型（facts），confidence_threshold=0.7 做品質門檻，max_facts=100 強制驅逐最低分項；用戶說「不對」系統會更激進地清除錯誤記憶。
- **NanoClaw**：進化的是容器的執行能力邊界，agent 透過 MCP tool 申請裝 package 或加 MCP server，每一步都需要 human approve 並走 docker rebuild 流程；是風險管理設計，不是不信任 LLM。
- **HolmesGPT**：靜態 playbook，刻意不自動進化——production SRE 工具需要可追溯性勝過適應性，靜態 skills 可以 code review、可以 rollback、可以解釋給 on-call 的人。
- **OpenClaw**：社群技能市集（ClawHub），品質由社群把關，但安裝手動觸發；進化決定權明確在人手上，是生態設計而非 agent 自進化。


在設計自己的 agent 系統前，值得先想清楚四件事：


**進化什麼**：取決於系統定位。個人化 assistant 需要記用戶偏好（DeerFlow），autonomous agent 需要積累技術 SOP（GenericAgent），production 工具需要可預測性而非適應性（HolmesGPT）。


**誰決定值得記**：agent 自判（GenericAgent、HermesAgent）、規則門檻（DeerFlow confidence=0.7）、人工審核（NanoClaw）——對應不同的信任假設。沒有最好的答案，只有和你的系統定位一致的答案。


**進化是否可逆**：多數系統這個問題沒有認真回答。NanoClaw 的 approval 記錄和 HolmesGPT 的 version control 是例外。DeerFlow 的 fact 驅逐是靜默的——某個事實被驅逐了，用戶不會知道。


**成本算進去了嗎**：HermesAgent 每次 skill nudge 要 spawn 一個 background review agent（額外 API cost）；NanoClaw 的 docker rebuild 要 15 分鐘；DeerFlow 每次工具執行後都跑 MemoryUpdater，對話密集時開銷會累積。


---


> 
以下是完整版，按需取用。


## GenericAgent：只有跑通的路徑才能結晶


GenericAgent 的自我進化邏輯非常直觀：在記憶系統的五層架構（L0–L4）裡，L3 是技能庫，存放的是跑通的任務執行路徑，格式是 Markdown SOP 或可直接 import 的 Python 模組。


```
memory/
 web_setup_sop.md ← 瀏覽器初始化流程
 tmwebdriver_sop.md ← TMWebDriver 特殊操作
 adb_ui.py ← Android ADB 控制（可直接 import）
 github_contribution_sop.md ← Git 貢獻完整流程（自舉時結晶的）
 ...
```


結晶流程很清楚：agent 完成新任務後，判斷這個執行路徑值得保留，就呼叫 `start_long_term_update`，把步驟提取成 SOP，寫進 `memory/`，同時更新 L1 Insight Index。L1 是整個記憶系統的目錄：


```
L3: memory_cleanup_sop | skill_search | ui_detect.py | ocr_utils.py | 
 subagent | web_setup_sop | tmwebdriver_sop | adb_ui.py | ...

Browser special ops: tmwebdriver_sop(file upload/PDF/CDP/cross-origin iframe...)
Keyboard & Mouse: ljqCtrl_sop(activate first, no pyautogui)
```


Agent 讀到 L1 就知道「需要 ADB → 去讀 adb_ui.py」，不需要語意搜尋。這是刻意的設計選擇：論文（arXiv:2604.17091）稱之為 Contextual Information Density Maximization，用幾百 token 的 L1 索引路由到任何 L2–L4 知識，context window 維持在 <30K，對比 RAG 做法的 200K–1M。


最重要的特性是私有性。同樣的 3K 行種子代碼，兩個用了半年的用戶，長出的技能樹完全不同，因為他們做過的任務不同。進化的不是通用能力，是屬於特定用戶的知識積累。


---


## HermesAgent：唯一同時走兩層的系統


HermesAgent 的進化設計是六個系統裡最複雜的，因為它走了兩條路同時進行：文字技能層和模型權重層。


**文字層：Skill Nudge**


每 10 次 tool-call iterations 後，系統在主 agent 返回 response 之後，以 daemon thread fork 出一個 background review agent：


```
def _spawn_background_review(self, messages_snapshot, ...):
 def _run_review():
 review_agent = AIAgent(
 max_iterations=8, # 避免 review 本身變成長任務
 quiet_mode=True, # 輸出重定向 /dev/null
 )
 review_agent._skill_nudge_interval = 0 # 避免遞迴觸發
 review_agent.run_conversation(
 user_message=review_prompt,
 conversation_history=messages_snapshot,  # 主 agent 的對話快照
 )
 t = threading.Thread(target=_run_review, daemon=True)
 t.start()
```


Review prompt 的核心判斷標準是：這次任務有沒有試錯過程？有沒有需要改變方向？如果有，才值得結晶成 SKILL.md。「沒有試錯的任務不需要記憶」——這個門檻防止技能庫被平庸的重複任務稀釋。


除了 background review 外，SOUL 裡的 SKILLS_GUIDANCE 還要求 agent 主動做：


```
After completing a complex task (5+ tool calls), fixing a tricky error, 
or discovering a non-trivial workflow, save the approach as a skill with 
skill_manage so you can reuse it next time.
When using a skill and finding it outdated, incomplete, or wrong, 
patch it immediately with skill_manage(action='patch') — don't wait to be asked.
```


主動進化 + 背景兜底，兩層確保技能庫被維護。


**權重層：Atropos RL**


這是六個系統裡唯一走到模型權重層的設計。Agent 在執行任務時，`trajectory.py` 把完整的對話以 ShareGPT 格式存下來：


```
{
  "conversations": [
 {"from": "human", "value": "Build me a REST API"},
 {"from": "gpt", "value": "<think>...</think>\nI'll start with..."},
 {"from": "human", "value": "[tool: terminal]\n{\"command\": \"mkdir api\"}"},
 ...
  ],
  "completed": true
}
```


成功和失敗的 trajectory 分開存放，用 `batch_runner.py` 批量跑任務生成訓練資料，最後透過 `tinker-atropos`（git submodule，GRPO 訓練框架）微調模型本身。知識庫的進化是 session 間的知識積累，RL 的進化是讓模型的推理能力本身改變。


代價是複雜度：六個系統裡進化最激進，架構也最難維護。


---


## DeerFlow：進化的是對用戶的認知，不是技能


DeerFlow 做了一個和其他系統都不同的選擇：不自動生成技能，只進化對用戶的理解。


`MemoryUpdater` 在每次工具執行後非同步觸發，讓 LLM 分析這段對話，提取應該記住的事實（facts），存到 memory.json 的 facts 區：


```
{
  "facts": [
 {"key": "deployment_target", "value": "AWS EKS，us-east-1", "confidence": 0.9},
 {"key": "tech_stack", "value": "FastAPI + PostgreSQL + Redis", "confidence": 0.95}
  ]
}
```


有三個機制控制記憶品質：


**信心值門檻**（threshold=0.7）：LLM 返回的新事實，信心值低於 0.7 的直接丟棄，不寫進記憶。


**驅逐**（max_facts=100）：超過 100 個 fact 時，保留信心最高的 100 個，其餘驅逐。記憶是有損但受控的。


**信號感知**：系統偵測對話中的信號類型，影響 LLM 的更新策略：


```
def _detect_signal(self, messages) -> str:
 correction_patterns = ["不對", "錯了", "no that's wrong", "incorrect"]
 reinforcement_patterns = ["對", "沒錯", "correct", "exactly", "remember this"]
 ...
 if any(p in content for p in correction_patterns):
 return "correction" # → LLM 被指示更激進地修正錯誤 facts
 if any(p in content for p in reinforcement_patterns):
 return "reinforcement" # → 提高相關 facts 的信心值
 return "neutral"
```


用戶說「不對」，LLM 會更積極清除舊的錯誤記憶。用戶說「就是這樣」，相關 fact 的信心值會被提高。這把用戶的語氣轉換成記憶更新策略的調節旋鈕。


DeerFlow 的技能庫（SKILL.md）設計上不自動生成，需要人工撰寫。它進化的是「對特定用戶的認知模型」，而不是通用任務能力。這讓它更適合需要長期追蹤用戶偏好的 assistant 場景，而不是需要積累技術能力的 autonomous agent。


---


## NanoClaw：進化的是 agent 能跑什麼，不是它知道什麼


NanoClaw 的進化方向完全不同——它進化的是執行環境的能力邊界。Agent 跑在 Docker 容器裡，當它需要一個新的 apt package 或 MCP server，可以透過 `install_packages` 或 `add_mcp_server` 這兩個 MCP tool 提出請求。


整個流程跨越容器和 host：


```
Container（agent 呼叫 install_packages MCP tool）
  ↓ 寫 system message 到 outbound.db
Host（delivery poll 讀到）
  ↓ 驗證 packages 格式
  ↓ requestApproval → 發 approval card 到 Telegram/Discord
Admin 點 Approve
  ↓ applyInstallPackages
  ↓ docker build（產生新 image，15 分鐘 timeout）
  ↓ killContainer → 下次訊息進來用新 image spawn
```


`install_packages` 需要完整的 docker build，幾分鐘起跳。`add_mcp_server` 只是更新 config.json + kill container，幾秒內完成。


這個設計的核心原則是：所有真正的系統修改都在 host 端執行，容器裡的 agent 只能提出請求，不能自己動手。而且每一步都需要人工 approve，不能跳過。self-mod 是 optional module，必須明確安裝啟用，不是預設功能。


六個系統裡，NanoClaw 對自我修改最謹慎。不是因為不信任 agent，而是因為修改執行環境的影響範圍大——一個裝錯的 package 可能讓整個容器壞掉，一個惡意的 MCP server 可能成為攻擊面。Human approval gate 是風險管理，不是對 LLM 的不信任。


---


## HolmesGPT 和 OpenClaw：刻意不自動進化


HolmesGPT 的 skills 目錄裡有 SRE 診斷 playbook——怎麼調查 Kubernetes pod crash、怎麼分析 prometheus 異常——但這些都是靜態文件，agent 讀取但不更新。`builtin/` 目錄為空，沒有機制自動生成新 skill。


這是刻意的設計選擇，不是功能缺失。HolmesGPT 的定位是 production SRE 調查工具，在這個場景下，可預測性比適應性更重要。SRE 工程師需要知道 agent 會怎麼診斷問題——如果 agent 自動學習並修改自己的診斷流程，人很難知道某次調查是依照哪個版本的邏輯跑的。靜態 playbook 可以 code review、可以 rollback、可以解釋給 on-call 的人。


OpenClaw 的 ClawHub 是社群技能市集，品質由社群把關，但安裝是手動的。這把進化的決定權明確放在人手上：用戶決定裝什麼，社群決定什麼值得維護。這是生態設計，不是 agent 自進化。


兩個系統的共同邏輯：當 agent 跑在生產環境、對結果負責的時候，行為的可追溯性比行為的適應性更有價值。


---


## 設計 Self-Improvement 要回答的問題


把六個系統並排看，有幾個反覆出現的設計選擇，每個方向背後都有各自的假設：


**你要進化什麼？**


六個系統進化的對象完全不同：GenericAgent 進化的是可複用的執行路徑，DeerFlow 進化的是對特定用戶的認知模型，NanoClaw 進化的是 agent 能執行的工具集，HermesAgent 同時進化這兩者加上模型權重。這個選擇應該從系統定位推導，不是隨意選的。個人化 assistant 需要記用戶偏好；autonomous agent 需要積累技術 SOP；production 工具需要穩定可預測。


**誰決定什麼值得記住？**


GenericAgent 讓 agent 自己判斷哪個任務值得結晶。HermesAgent 的 background review agent 用「有沒有試錯過程」做門檻。DeerFlow 的 confidence threshold（0.7）讓 LLM 來評分。NanoClaw 把判斷權完全給了人。每種方法對應不同的信任假設：你信任 agent 的判斷，還是信任規則，還是信任人？


**進化是可逆的嗎？**


GenericAgent 的 SOP 是文字文件，可以手動刪除，但改動不會通知用戶。HermesAgent 的 skill 有 version 欄位，可以 diff。DeerFlow 的 memory 可以讀到 confidence 值，但驅逐是自動的、靜默的——某個事實被驅逐了你不會知道。NanoClaw 每次 self-mod 都有明確的 approval 記錄。HolmesGPT 的靜態 skills 隨時可以 rollback，因為本來就在 version control 裡。可逆性在 production 環境裡和可靠性一樣重要，但多數系統沒有認真設計這件事。


**進化的代價算進去了嗎？**


HermesAgent 每次 skill nudge 需要 spawn 一個 background review agent，算額外的 API cost。GenericAgent 的 `start_long_term_update` 是一次 LLM call，agent 自己決定要不要觸發。DeerFlow 的 MemoryUpdater 在每次工具執行後非同步跑，如果對話很密集，這個開銷會累積。NanoClaw 的 docker rebuild 是 15 分鐘的等待。進化本身有成本，而且這個成本不總是顯而易見的。


---


進化設計本身就是系統定位的鏡子。GenericAgent 強調「個人化 AI 助手」，所以進化的是私有技能樹；NanoClaw 強調「安全邊界內的環境控制」，所以進化需要 human approve；HolmesGPT 強調「可靠 SRE 診斷」，所以選擇不進化。在設計自己的 agent 系統之前，先想清楚你的系統定位——答案通常就指向了正確的進化策略。


---


## 相關文章


- [SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較](/blog/agent-soul-design-comparison)
- [Hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent)
- [打開原始碼才發現：三個 Agent 框架，三種截然不同的設計哲學](/blog/agent-20260423)


---


> 
**結語**：越用越強這件事，每個系統有完全不同的答案——有人說進化是把跑通的路徑記下來，有人說是讓模型本身學習，有人說是擴展能執行的工具，也有人說不應該自動進化。選哪條路，取決於你最在意的是什麼。

  
  
 [ System Design ](/blog?tag=System%20Design)[ Harness Engineering ](/blog?tag=Harness%20Engineering)[ Agentic System ](/blog?tag=Agentic%20System) 
 

### 相關文章
[Implement

用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄

2026-05-28
](/blog/kube-arena)[
System Design

MCP、CLI、還是直呼 API？先看工具長什麼樣

2026-05-23
](/blog/mcp-cli-api-integration)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)
