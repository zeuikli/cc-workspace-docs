---
url: "https://warmwater.dev/blog/llm-observability-design"
title: "你的 Agent 跑歪了你知道嗎？LLM Agentic System 可觀測性設計"
date: 2026-05-07
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  你的 Agent 跑歪了你知道嗎？LLM Agentic System 可觀測性設計 
  2026-05-07 · — views      

有一段時間，我調 agent 的方式是這樣的：output 看起來不對，改一個地方，再跑一次，看看有沒有好一點。有時好一點，有時更差。我不知道為什麼好，也不知道為什麼壞。每一個修改都是猜測。


後來才意識到：問題不是改得對不對，而是根本沒有量測。改善沒有方向，只有感覺。


**讀完這篇，你會理解：**


- 為什麼 LLM 系統的品質問題不會「報錯」，只會靜靜地漂移

- Tracing 在 agent 情境下要記錄什麼，以及怎麼用它定位失敗層次

- Evaluation 怎麼量化非確定性系統的「好不好」

- Cost 飆升是表象，哪些行為指標更早出現異常

- 為什麼沒有可觀測性，P0 來了根本寫不出 RCA


這篇是設計原則，不是工具介紹。重點是在你選工具之前，先想清楚要量測什麼。

---


## LLM 系統的「錯誤」長什麼樣子？


傳統系統出問題，有 exception，有 stack trace，有明確的失敗時間點。你可以追，可以重現，可以修。


LLM 系統的問題不是這樣出現的。


沒有 exception。Agent 繼續跑，繼續回應，只是回答越來越偏離你期望的方向。你可能過了幾天，從用戶回饋才意識到有問題，但說不清楚是從什麼時候開始的。這就是「漸進式品質下降」，傳統的 error monitoring 完全看不到它。
 ● 品質下降的兩種形態    傳統系統       高  低         Exception    失敗有明確時間點，Exception 在崩潰的瞬間觸發。 可追蹤・可重現    LLM 系統       高 低    no exception     用戶投訴  沒有明確失敗點，品質悄悄下滑，直到用戶投訴才發現。 漸進・靜默・難偵測   
LLM 系統不會「崩潰」，只會「漂移」。傳統的 error monitoring 對漂移是盲的。
 


這種漂移有很多個來源，大部分是靜默發生的：


**Prompt 改動影響全部下游行為。** 你修了一個措辭，以為只影響某一個場景，但 LLM 對 context 的敏感度很高，其他路徑的行為也跟著變了，你不知道。


**Provider 靜默升級模型版本。** 你的程式碼指向 `claude-3-5-sonnet`，但 Anthropic 更新了這個版本的基礎能力。行為改變了，沒人通知你。


**Tool API 回傳格式改變。** 下游服務改了 response schema，agent 在 parse 時開始出現奇怪的行為，但沒拋出 error，只是輸出品質變差。


**Memory 累積垃圾。** 跨 session 的 memory 系統，如果沒有清理機制，早期寫進去的錯誤偏好或過時資訊會一直影響後續 session。


**User query 分佈改變。** 你的 eval set 是三個月前做的，但用戶現在問的問題類型已經不一樣了。系統對新分佈的覆蓋率下降，但舊 eval 分數還是好的。


這五個來源，任何一個都不會觸發 alert。你需要在系統裡設計量測，才能在它們造成嚴重問題之前看到。

---


## Tracing：你的 Agent 在哪一層失敗了？


Tracing 的核心價值是把一個完整的 agent 執行拆解成 span tree，讓你知道問題出在哪個環節，而不是只看到最終輸出錯了。


一個 agent session 的 span tree 大概長這樣：
 ● Tracing Span Tree output 不對時，span tree 告訴你失敗在哪一層    Session: handle_customer_query   0 → 3800ms      │  ├─ retrieve_memory   0 → 120ms  Harness     │  ├─ rag_retrieval   120 → 680ms  Knowledge     │ │  └─ vector_db.search relevance_score: 0.71   125 → 675ms      │  ├─ llm_call.plan   680 → 1200ms  LLM     │ │  input_tokens: 1240 · output_tokens: 89 · cost_usd: 0.0031 · model: claude-3-5-sonnet     │  ├─ tool_call.check_order_status   1200 → 2100ms  Tool     │ │  status: success · order_id: #8821 · return_format: json     │  └─ llm_call.respond   2100 → 3800ms  LLM     │ │  input_tokens: 1580 · output_tokens: 312 · cost_usd: 0.0062    Harness 層 Knowledge 層 LLM Call Tool 層  


當 output 不對，你可以順著 span tree 看：是 `retrieve_memory` 取回了錯誤的 context？`rag_retrieval` 找到的文件相關性不夠？`llm_call.plan` 的推理偏掉了？還是 tool 回傳了意外的格式？


每個 LLM span 應該記錄：


- **Token counts**（prompt / completion / total）

- **Model 版本**（知道哪個 call 用了哪個版本）

- **Per-call cost**

- **Retrieval 相關性分數**（如果有 RAG）

- **Tool 回傳狀態**（success / error / 格式異常）


這樣設計出來的 tracing，不只是「有沒有跑完」的記錄，而是每次執行的完整診斷報告。有了它，你才能在 output 品質下降時，回答「哪一層出了問題」，而不是只能重跑一次祈禱結果不同。

---


## Evaluation：量化「好不好」的三層策略


Tracing 告訴你「發生了什麼」，Evaluation 告訴你「做得好不好」。對非確定性系統來說，後者更難設計。


只靠 LLM-as-Judge 不夠。Judge 本身也是 LLM，也有非確定性，也有自己的偏見。LLM-as-Judge 只能評估最終輸出，看不到中間哪個元件出了問題。
 ● 三層 Evaluation 架構 整體分數下降時，三層設計讓你追查到具體的問題層次    Upper Layer 整體結果   評估 agent 對用戶和業務目標的最終價值。回答「這個系統有沒有達成任務」。  Task Completion Rate Goal Accuracy Response Quality Domain KPI    ↑ 整體分數下降，追查到哪個元件 ↑    Middle Layer 元件層   針對 agent 每個子系統個別量測，找出是哪個環節拖累整體表現。  Tool 選擇準確率 Tool 參數正確率 Memory 精準度 Reasoning Grounding Intent Detection Multi-turn 一致性    ↑ 元件異常，追查模型基礎能力 ↑    Bottom Layer 模型基礎能力   評估 foundation model 在你 domain 相關任務上的基準表現。這是換模型、選模型的依據，也是後續比較的 baseline。  Domain Benchmark Reasoning Score Format Compliance    
分層評估的核心價值：整體分數下降時，你能追查是哪一層出了問題——而不是只知道「變差了」。
 


Amazon 在大規模 agent 評估的實踐上有一個三層設計，對我來說是個有用的分析方式：


**Bottom Layer：模型基礎能力。** 評估你選了哪個 foundation model，這個 model 在你 domain 相關任務上的基準表現。這是之後比較的 baseline，也是決定「要不要換模型」的依據。


**Middle Layer：元件層評估。** 針對 agent 每個子系統個別量測：


- Tool 選擇準確率、Tool 參數填寫正確率

- Memory 取回的 context 精準度和召回率

- 推理鏈的 grounding accuracy（每個推理步驟有沒有 context 支撐）


**Upper Layer：整體結果評估。** 最終輸出的品質、task completion rate，以及你 domain 的 business-specific 指標——你怎麼定義「這個 agent 完成了任務」。


分層評估的價值是：整體分數下降時，你可以追查是哪一層出問題。不然你只知道「變差了」，不知道改哪裡。


Eval dataset 要有四個來源：


類型用途Golden set人工驗證的黃金標準，代表核心場景，穩定不常改Regression set歷史曾失敗的 case，防止你改了 A 壞了 BEdge cases邊界情況、模糊輸入、對抗性輸入Production failures用戶回饋低分 session，最有改進價值


Production failures 這一類最容易被省略，也是最有價值的。你在 lab 裡想像不到的 edge case，用戶都幫你找到了。

---


## 行為異常偵測：Cost 飆升只是表象


Cost 飆升是你能看到的表象，但在 cost 開始飆之前，行為指標早就出現異常了。
 ● 行為異常訊號出現的時間順序 Cost 飆升是你看到的，但更早的訊號一直在那裡    行為異常訊號（領先指標） Cost 飆升 用戶投訴      Tool 呼叫頻率異常         Retry storm         Session 步驟數異常         Memory 取回品質下降         Cost 飆升         用戶投訴            T+0 T+2h T+6h T+12h T+24h   
如果只設 Cost alert，你等於在等最後的結果才發現問題。
行為指標是領先訊號，比 Cost 早幾小時到幾天出現。
 


**Tool 呼叫頻率異常。** 某個工具平常一個 session 呼叫 2-3 次，突然變成 30 次。原因可能是 agent 在某個 condition 下陷入了重複呼叫的迴圈，但每次都以為自己在做新的事。Cost 會跟著飆，但這個訊號比 cost 早出現。


**Retry storm。** LLM 回傳的格式不符預期，parser 失敗，agent 重試，重試後還是一樣的格式，繼續重試。Token 在快速消耗，但系統沒有報錯，最後到達 max retry 限制靜默失敗。用戶看到的是一個不完整的回應，完全不知道背後發生了什麼。


**Session 步驟數異常。** 這個任務平常 5 步以內完成，今天某個 session 跑了 60 步。可能是 stop condition 沒有觸發，可能是 agent 困在某個思考迴圈裡，可能是工具一直回傳它不知道怎麼處理的結果。


**Memory 取回品質下降。** 這個最難偵測，也最常被漏掉。Agent 不報錯，只是答案越來越廢。你需要在 retrieval span 上記錄相關性分數，才能看到這個趨勢。等到 cost 開始反映這個問題，已經晚了。


這些訊號的共同特點是：它們都比用戶投訴早出現，有時早幾小時，有時早幾天。如果你只設 cost alert，等於在等最後的結果才發現問題。

---


## P0 來了你能查嗎？


Agentic System 在 prod 上天生比傳統服務更容易出現不穩定。非確定性、長 session、多工具、跨 session 的 memory，每一個都是潛在的不穩定來源。問題不是「會不會出現 P0」，而是「出現 P0 的時候，你能查嗎」。


沒有 tracing：你只有最終的錯誤輸出，不知道 agent 走了什麼執行路徑。無法重現，無法定位。


沒有 evaluation baseline：你不知道這次的問題是退化，還是系統一直都這樣。無法判斷影響範圍，也無法評估修完之後有沒有真的好。


沒有行為異常監控：你在用戶投訴之後才知道。沒有 timeline，不知道什麼時候開始、影響了多少 session。


這三個沒有，加在一起，就是寫不出 RCA。你只能說「我們調整了一些東西，應該好了」，但無法說清楚根因是什麼，也無法確認有沒有真的修好。


可觀測性不是部署完之後補的監控工具，它是你能夠持續改善這個系統的基礎設施。沒有它，每一次改善都是猜測，每一次 P0 都是一個謎。

---


## 延伸閱讀


- [把領域判斷打包進 Agent：Production Agentic System 地圖](/blog/domain-specialized-agentic-system) — 四層知識地圖與可觀測性的位置

- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — session 管理的四種策略與三種中斷狀態

- [Agentic Loop 的設計關卡：工具執行、錯誤分類與中斷機制](/blog/agentic-loop-design) — Loop 執行引擎的工程設計
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)[ LLMOps ](/blog?tag=LLMOps)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)
