---
url: "https://warmwater.dev/blog/ml-intern-sft-flywheel"
title: "HuggingFace ml-intern 的 SFT Flywheel：從使用者互動到訓練資料"
date: 2026-05-12
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code  
#  你在用它，它也在學你：HuggingFace ml-intern 的 SFT Flywheel 
  2026-05-12 · — views      

config 裡有一行設定叫 `save_sessions: true`，預設是開的。


第一次看到這行，我以為是本地 crash recovery 用的，存 session 狀態方便重連。繼續讀下去才發現不是。這行設定的意思是：你的每一次 ml-intern session——每一個 tool call、每一次 debug、每一次成功提交 GPU Job——都會被上傳到 `smolagents/ml-intern-sessions` 這個 HuggingFace 公開 dataset。


然後有個叫 `build_sft.py` 的腳本，把這個 dataset 轉成 OpenAI 格式的 SFT 訓練資料。


Hugging Face 在用這個 dataset 訓練下一代 ml-intern。你用 ml-intern 做 fine-tune，同時也在教它怎麼做更好的 fine-tune。


這不是 bug，是設計。


真正有趣的地方是背後的核心假設：**每一次有意義的 agent 互動，本身就是一份訓練資料**。你不需要另外雇人標注「這個 ML 工程師決策是好的」——用戶做真實任務的完整 trajectory，已經包含了這個信號。ml-intern 把這個假設工程化了：session 物件從被建立的第一刻就在收集 trajectory，準備被送進訓練 pipeline。


**讀完這篇，你會理解：**


- ml-intern 是怎麼把用戶的工作流 session 轉成 SFT 訓練資料的

- trajectory 需要什麼結構才有訓練信號——不是所有資料都有用

- 為什麼這個自我進化機制和 AutoResearch 的方向根本上不同

- SFT Flywheel 的概念可以延伸到哪些 agent 系統，以及設計挑戰在哪裡


這篇不是 ml-intern 的使用教學。它是在問：**「使用行為即 trajectory，trajectory 即訓練資料」這個設計哲學，能走多遠？**

---


## ml-intern 是什麼？


ml-intern 是 Hugging Face 開源的自主 ML 工程 Agent。它不是 AI 聊天助手，而是一個能自主研究論文、撰寫訓練腳本、測試、提交 GPU Job、把模型推上 Hub 的完整自動化 pipeline。


你跟它說「fine-tune Qwen2.5-7B on UltraFeedback with DPO, push to my-org/qwen-dpo」，它自己去查論文、讀 TRL 文件、在 HF Spaces sandbox 寫腳本測試，確認沒問題後提交 A10G GPU Job，最後告訴你 Hub URL。整個流程你可以去睡覺。


這個能力的工程基礎是一個 queue-based async loop：

```
User Input (CLI / Web)
    ↓
submission_queue
    ↓
submission_loop（coroutine）
    ├── 呼叫 LLM（LiteLLM，streaming）
    ├── 執行 Tool calls（asyncio.gather 並行）
    ├── Approval gate（sandbox 建立、Job 提交需確認）
    └── Doom-loop 偵測 + 注入修正 prompt
    ↓
event_queue → CLI terminal / Web SSE
```


所有中間狀態存在 `Session` 物件裡，包括對話歷史、正在跑的 HF Job ID、等待確認的 tool calls。


特別值得注意的是 Session 的最後一個欄位：`trajectory: list`。所有 events 的完整記錄，for SFT 上傳。Session 物件從一開始就知道自己要被收割。

---


## SFT Flywheel：Session 怎麼變成訓練資料


Session 結束時（或每 60 秒 heartbeat），ml-intern 做這幾件事：

```
Session 結束 / 每 60 秒 heartbeat
    ↓
redact.py：移除 secret（hf_、sk-ant-、ghp_ 等格式的 token）
    ↓
session_logs/<session_id>.json 存到本機
    ↓
detached subprocess 上傳到 smolagents/ml-intern-sessions HF dataset
```


上傳之前有個 tagger 給每個 session 打標籤：

```
# agent/sft/tagger.py
{
    "task_kind": "fine-tuning",        # fine-tuning / evaluation / inference / data-processing
    "outcome": "success",              # success / failure / abandoned
    "model_family": "qwen",
    "gpu_type": "a10g-large",
    "has_training_code": True,
    "pushed_to_hub": True
}
```


這些標籤是讓 SFT 資料有用的關鍵。一個成功的 fine-tune session 和一個失敗的 session 對訓練的意義完全不同：成功的告訴模型「這樣做」，失敗的告訴模型「這種路徑不行」。`scripts/build_sft.py` 把這個標籤 dataset 轉成 OpenAI / TRL SFT 格式，後面可以直接丟進 TRL 跑 SFT。


整個 Flywheel 是這樣的：用戶跑任務 → trajectory 被收集 → tagger 打標籤 → build_sft 格式化 → SFT 訓練下一代 ml-intern → 新版本更會做 ML 任務 → 更多用戶來用 → 更多 trajectory。

---


## ml-intern SFT Flywheel 和 AutoResearch 根本上有什麼不同？


前兩篇說的 AutoResearch（Karpathy 和 Paradigm Hackathon）都是「計算量驅動的自我改進」：給 agent 一個 evaluation function，讓它大量跑實驗，用計算量替代人類的 domain knowledge。改進發生在一次 run 裡，是即時的。


ml-intern 的方向是「資料驅動的自我改進」：用戶做真實的 ML 工程任務，這些任務的完整 trajectory 被收集，成為 SFT 訓練資料，訓練出更好的 agent。改進發生在多個 session 的累積之後，是離線的。


機制AutoResearchml-intern SFT Flywheel改進方式計算量（大量 agent 實驗）資料（用戶 session trajectory）改進速度即時（一次 run 內）離線（累積後重新訓練）需要 eval function是（單一可量化指標）否（outcome 標籤就夠）人類在哪裡設計系統，不設計解法做真實任務，同時產生訓練資料改進的對象解法（策略/代碼）模型本身（weights）


AutoResearch 改的是 agent 的輸出，ml-intern 的 Flywheel 改的是 agent 的能力。這是一個更深層的循環——不是讓 agent 找到更好的答案，而是讓 agent 本身變得更強。

---


## Flywheel 能轉起來，需要什麼條件？


理論上所有 agent 都可以收集 trajectory，但不是所有 trajectory 都有訓練信號。ml-intern 的設計讓它的 trajectory 特別有用，有幾個具體原因。


任務的輸出是可觀測的。「模型成功推上 Hub」是一個明確的 success 信號，不需要人工標注。Tagger 可以自動判斷 `pushed_to_hub: True` 還是 `False`，`outcome: "success"` 還是 `"failure"`。這讓大規模收集有標注的資料成為可能——不需要人去一個一個看 session 說「這個好、那個不好」。


任務足夠結構化，但又有足夠的變化。Fine-tuning workflow 有固定的步驟（research → write script → test → submit job），但每次的模型、dataset、硬體選擇、debug 路徑都不同。這種「結構相似、細節多變」的任務最適合 SFT：模型學到的是通用的工作流直覺，不是死記某個特定的腳本。


失敗的 trajectory 也有信號。一個 research → write → test → fail → debug → fix → test → success 的 session，記錄了 agent 在哪裡卡住、用了什麼策略修正。這個「失敗然後恢復」的模式是最難靠合成資料產生的，但在真實 session 裡很常見。合成資料大多是「正確示範」，真實 session 包含了人類（和 agent）在真實任務裡的摸索過程。

---


## 把 Flywheel 帶到其他 Agent 系統：能走多遠？


「使用行為即 trajectory，trajectory 即訓練資料」這個概念，不只適用於 ML 工程任務。任何 agent 系統，只要滿足三個條件，都可以設計類似的 Flywheel：任務可以被 log、outcome 可以被觀測、任務有足夠的重複性和變化性。


幾個具體的延伸方向：


**Skill Flywheel**：agent 的 skill（比如 Claude Code 的 slash commands、Hermes 的 skill 機制）每次被呼叫時，都有 context（為什麼觸發）、execution（執行過程）、result（輸出）、acceptance（用戶接受還是修改或忽略）。把這個 trajectory 收集起來，可以做兩件事：一是優化 skill 的執行內容（哪些 skill 輸出用戶總是直接接受，哪些總是被大幅改動），二是優化 skill 路由（哪些 context 下觸發哪個 skill 是有效的）。outcome 信號是用戶的接受率和後續行為。


**Tool Description Flywheel**：agent 在選擇 tool 時，它其實在做一個 retrieval 決策：從 tool registry 裡找最符合當前需求的工具。每次 tool call 都是一個訓練樣本——context 是任務描述，選擇是 tool name，outcome 是這個 tool call 有沒有幫到任務完成。累積足夠多的這種 trajectory，可以自動識別哪些 tool 的 description 寫得不夠清楚（總是被錯誤呼叫），哪些 tool 在特定 context 下特別有效（值得提升在 routing 裡的權重）。


**Code Review Flywheel**：AI 生成代碼的品質可以靠用戶的接受行為來評估——用戶直接 accept 的 diff 是正信號，大幅改寫後才 commit 的是負信號，完全刪掉的是強負信號。這個信號不需要任何額外的標注，完全從用戶行為中自動產生。GitHub Copilot 已經在做類似的事，把 acceptance rate 作為模型改進的核心指標之一。


**Bug Fix Pattern Flywheel**：debugging session 的 trajectory 特別有價值。一個完整的 debug session 包含：error message、錯誤假設（agent 試了什麼但沒用）、正確修法（最後有效的 fix）。這種資料靠合成幾乎不可能產生，因為你需要知道「什麼樣的錯誤會讓人往哪個方向想錯」。真實的 debug trajectory 天然包含這個資訊。


這些延伸方向的設計挑戰都指向同一個問題：**你的 outcome signal 有多乾淨？** ml-intern 的 `pushed_to_hub` 是個非常乾淨的二元信號。Skill acceptance rate 比較模糊——用戶接受一個 skill 輸出，是因為它真的好，還是因為懶得改？Tool call 的有效性很難在呼叫當下判斷，需要追蹤整個 session 的最終 outcome。Signal 越模糊，Flywheel 產生的訓練資料越嘈雜，改進越慢。

---


## Flywheel 在哪裡卡住了？


回到 ml-intern 本身，這個 Flywheel 不是沒有問題。


Context compaction 是有損的。當對話歷史接近 90% context window，ml-intern 會用 LLM 生成的摘要替代中間的對話。詳細的 tool call 輸出、debug 過程的中間代碼版本都可能消失。長 session（超過約 50 turns）的 trajectory 在壓縮後可能遺失最有價值的 debug 細節——而那些細節恰好是最難靠合成資料補上的。


Evaluation harness 已停用，`.gitignore` 裡的 `eval/` 目錄被標記為 `(stale)`。這意味著無法系統性地評估 ml-intern 在特定任務上的成功率，只能靠 SFT dataset 的 outcome 標籤做事後分析。沒有好的 eval，Flywheel 的「訓練 → 測試 → 改進」循環就無法閉合，只能盲目訓練然後希望結果變好。


還有一個根本性的問題：Flywheel 的轉速依賴真實用戶的真實使用。Secret scrubbing 只覆蓋已知格式的 token（hf_、sk-ant-、ghp_ 等），自定義 API key 或 database connection string 不會被清除。出於安全考量的用戶會關掉 `save_sessions`，資料就不進 Flywheel。如果大部分用戶做的任務太相似，Flywheel 收集到的 diversity 就很有限。


AutoResearch 的改進上限是計算預算，ml-intern 的改進上限是用戶使用的廣度和真實性。

---


> 


**結語**：前兩篇說的 AutoResearch 是「讓計算量替代 domain knowledge」，ml-intern 的 SFT Flywheel 說的是「讓使用行為替代人工標注」。兩個方向都在回答同一個問題：怎麼讓 AI 系統在不直接投入人工的情況下持續進化？答案不只一個。而「使用行為即 trajectory，trajectory 即訓練資料」這個設計哲學，在任何 agent 系統裡都值得認真問一次：我的 outcome signal 在哪裡？
     [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Source Code不預裝能力，只定義生長方式：GenericAgent 原始碼解析2026-05-22](/blog/generic-agent-source-code)
