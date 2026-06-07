---
url: "https://warmwater.dev/blog/llm-eval-foundations"
title: "你怎麼知道 AI 答對了？建立 LLM 評估的思考框架"
date: 2026-05-12
category: LLMOps
source: warmwater.dev
---

[
← LLMOps ](/blog?tag=LLMOps)  LLMOps  
#  你怎麼知道 AI 答對了？建立 LLM 評估的思考框架 
  2026-05-12 · — views      

我在做第一個有 LLM 的服務時，「測試」這件事是這樣進行的：把 prompt 貼進去，看輸出，覺得 OK 就繼續。沒有 assert，沒有門檻，沒有資料集。就是「看起來對」。


這在初期很快。問題出在兩個月後。


prompt 改了幾次，模型換了版本，輸出開始變奇怪——但我說不出奇怪在哪裡，因為本來就沒有定義什麼叫做「對」。更糟的是，即使我想說，也沒有辦法系統性地量：每次測試都是人工跑一遍，每次「感覺沒問題」的判斷都是噪音。


這讓我開始認真想：LLM 系統的「測試」應該長什麼樣子？


**讀完這篇，你會理解：**


- 為什麼傳統測試思維在 LLM 這裡失效，以及失效在哪裡

- 評估一個 LLM 系統需要看三個層次，而不是一個

- LLM-as-Judge 這個想法為什麼說得通，以及它的限制

- Evaluation 和 Observability 解決的是不同時間點的問題，兩者都需要


這篇不是工具教學，也不是指標查詢手冊。是幫你建立一個思考框架，讓你在面對「這個 AI 夠不夠好」的問題時，知道從哪裡下手。

---


## `assert output == expected` 為什麼在 LLM 這裡失效？


傳統軟體測試的核心假設是：給定同樣的輸入，系統應該產生同樣的輸出。這個假設讓 unit test 有意義——你寫一個 golden value，每次 CI 比對，通過就代表沒有 regression。


LLM 破掉了這個假設。給同一個 prompt，兩次輸出不會一樣。不是因為系統有 bug，是因為 LLM 本質上是一個在可能輸出的機率分佈上取樣的系統。temperature > 0，就永遠不會是確定性的。


但更根本的問題不是確定性，而是「正確答案」的定義。「法國的首都是哪裡？」有明確答案。「幫我整理這份 meeting notes 的重點」沒有。兩份輸出都可能合理，但措辭不同、結構不同、細節取捨不同。`assert output == expected` 在後者完全沒有意義，因為 expected 本身就是一個空間，不是一個點。


傳統 test 問的是「輸出完全一樣嗎」，LLM eval 問的是「輸出夠好嗎」——這是兩個不同的問題，需要不同的評估工具和方法。

---


## LLM 評估為什麼需要看三個層次？


Amazon 在大規模建構 agentic system 時總結出這個洞見：你不能把整個系統當黑盒評估，光看最終輸出你沒辦法知道問題出在哪裡。他們把評估拆成三個層次。


**底層：模型基礎能力。** 評估的是驅動你系統的 foundation model 夠不夠強：在這個任務上，哪個模型更適合？這個層次告訴你「選什麼模型」，不是「評估你的系統」。


**中層：元件行為。** 這裡開始看你的系統實際在做什麼：如果有 RAG，retrieval 召回的東西相關嗎？如果有 tool call，工具選對了嗎、參數填正確嗎？如果有 multi-turn 對話，context 有正確保留嗎？這個層次是除錯的關鍵所在。系統最終輸出爛了，根因可能在任何一個元件——分層評估才能定位問題。


**上層：系統結果。** 才是「對用戶和業務有沒有價值」的問題：任務完成了嗎？回答正確嗎？用戶的需求有沒有被滿足？


這三層不可互替。很多人只看上層，系統出問題了不知道原因在哪。也有人只做底層（benchmark 模型），但選了好模型不代表系統就好——prompt 設計差、retrieval 差、tool schema 模糊，一樣會讓系統的表現崩掉。

---


## LLM-as-Judge：讓 LLM 評估 LLM 輸出，這條路說得通嗎？


評估「輸出夠好嗎」，最直觀的方法是讓人來判斷。但人工評估有規模問題：每次 prompt 改版都要人工跑一遍，不現實。


所以出現了 LLM-as-Judge 這個做法：讓另一個 LLM 來評估輸出品質。


這聽起來循環，但有一定的合理性。給一個 LLM 清晰的評估準則（「這個回答有沒有基於提供的 context？」「這段推理邏輯上一致嗎？」），它的一致性和可重複性其實比人工好——人類評估者容易疲勞、受順序效應影響、對相同標準的解讀也會漂移。LLM judge 在固定準則下跑，至少能給你可重複的結果。


不過 LLM-as-Judge 不是沒有問題。它有幾個已知的 bias：傾向給中間分數、對 prompt 格式敏感、對自己產出的輸出評分比較寬鬆。所以好的實作不是「讓 LLM 直接給 1-10 分」——這樣取到的數字穩定性差。比較嚴謹的做法是用 logprobs 加權平均：讓 LLM 給完評分後，取各個分數的 token 機率做加權計算，而不是直接讀輸出的數字。這讓評分更符合機率分佈，而不是 LLM 的「偏好」。


LLM-as-Judge 是目前最可行的自動化評估路線，但用的時候要清楚它量的是什麼、可能錯在哪裡。它是讓評估可以 scale 的工具，不是讓你省掉思考的工具。

---


## Evaluation 做完了，上線之後呢？


Offline evaluation 解決的是「部署前的品質保障」問題：這個 prompt 改版有沒有讓輸出變差？這個新版本的 retrieval 有沒有退步？在 CI 環境裡跑一批 golden test cases，看有沒有 regression。


但上線之後，你面對的是真實用戶，他們的提問分佈和你的 test set 不一樣。系統會衰退——這個現象有個名字叫 agent decay：隨時間推移，模型版本悄悄更新、工具 API 改了 schema、用戶行為模式變了，系統的表現下滑，但你不知道從什麼時候開始、也不知道哪個環節出問題。


這就是 Observability 存在的原因。Evaluation 和 Observability 解決的是同一個問題的兩個時間點：


- **開發 / CI 階段** → Evaluation（這個版本的品質夠嗎？）

- **上線 / 運行階段** → Observability（現在的系統出了什麼事？）


Observability 的工具——Langfuse、AgentOps、OpenTelemetry——把 LLM 系統的每一次 LLM 呼叫、工具呼叫、retrieval 查詢都記錄成可查詢的 trace，讓你在生產環境裡能看到「第 17 步工具呼叫失敗」「這個 session 的平均延遲比昨天高了 40%」，而不是只能靠用戶回報說「AI 回答很奇怪」才知道出事了。


兩條線都需要，缺一個你的視角就是不完整的。

---


## Eval 和 Observability 工具各在生命週期的哪個位置？


把這幾類工具擺回生命週期，選型的邏輯就清楚了：


**Offline Evaluation（CI / 開發階段）**


工具定位適合場景DeepEvalpytest for LLM，40+ 指標開箱即用品質回歸測試、prompt 改版驗證Giskard場景式評估，不要求輸出完全一樣有多條合法路徑的 agentic 系統


**Online Observability（線上 / 運行階段）**


工具定位適合場景AgentOpsOTel-native session 觀測線上 debug、cost 分析、SLO 監控PlanoProxy gateway 層的流量觀測infra 層統一管 LLM 流量，不改 app code
   開發 / CI 階段  上線 / 運行階段   「這個版本的品質夠嗎？」   deploy   「系統現在出了什麼事？」     DeepEval pytest for LLM · 40+ 指標 · CI 回歸測試   Giskard 場景式評估 · 驗證行為而非固定輸出        AgentOps Session tracing · OTel · cost 分析   Plano Proxy gateway · guardrail · 行為觀測     


選工具之前要先問：你在哪個時間點？解決的是什麼問題？Eval 工具不能替代 Observability 工具，反過來也一樣。Eval 通過了不代表上線後沒問題，Observability 看到異常了也不代表你知道根因是 prompt 問題還是模型問題——兩個視角要一起有，才算是完整的 AI 系統品質保障。

---


> 


**結語**：「系統看起來工作」和「系統可以被量測地工作」是兩件事。Evaluation 給你一個可重複的品質基準；Observability 給你生產環境的視野。這兩個都建立起來之前，你對系統品質的判斷，基本上還是靠感覺。
     [ LLMOps ](/blog?tag=LLMOps)  
### 
相關文章

[LLMOpsLoRA 這件事你只需要搞清楚一次2026-05-20](/blog/lora-map)[LLMOps選對指標，不要選多：LLM 評估的決策框架2026-05-12](/blog/llm-eval-metrics-decision)[Harness Engineering你的 Agent 跑歪了你知道嗎？LLM Agentic System 可觀測性設計2026-05-07](/blog/llm-observability-design)
