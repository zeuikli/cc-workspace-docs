---
url: "https://warmwater.dev/blog/backend-to-ai-engineer-roadmap"
title: "AI 時代的 Backend Engineer：從會用到能建的完整路線"
date: 2026-05-26
category: Viewpoint
source: warmwater.dev
---

[
← Viewpoint ](/blog?tag=Viewpoint)  Viewpoint 
 
# AI 時代的 Backend Engineer：從會用到能建的完整路線
 
 2026-05-26 · — views  
  
  
過去一年，AI 相關的需求開始頻繁出現在我的工作裡。起初是小事：幫某個服務加個 LLM 呼叫、試著把 prompt 包成 API。但越做越覺得，我對這整個領域的理解是碎片的——我知道怎麼打 API，但不知道為什麼這個 prompt 有效、不知道 agent 該怎麼設計、更不知道什麼時候該考慮 fine-tuning。


市面上的資源，不是太學術就是停留在 Hello World。我找不到一條從 Backend Engineer 的起點出發，走到能獨立設計 Agentic System 的路線。所以我自己整理了一條。


這篇是寫給跟我一樣背景的人：熟悉 API 設計、懂資料庫、但還沒有系統性接觸 AI 工程的 Backend Engineer。


**走完這條路線，你會能夠：**


- 用 AI Coding Agent 協作，而不只是補全程式碼
- 獨立 build 一個 LLM-backed 的 REST Service 上 production
- 設計並開發完整的 Agentic System，包含 RAG、memory、安全層與 eval
- 理解 fine-tuning 和 local inference 的適用場景與基本架構


在正式進入路線之前，有一件事要先說清楚。


---


## 先升級工作方式：從 Vibe Coding 到 Agentic Coding


不要停在 Vibe Coding——那是把 AI 當成隨便問問的工具，生出什麼算什麼。作為工程師，你應該把本來就懂的設計思維帶進來：寫清楚的 spec 再讓 Agent 執行（SDD），或是先定義測試再讓 Agent 實作（TDD）。這兩種方式都讓 AI 的輸出變得可預期、可驗證。


Agentic Coding 不是「用 Copilot 補 code」，而是讓 Claude Code、Codex 這類 AI Agent 直接執行任務——寫 spec、建 scaffold、跑測試、做 refactor。你的角色從「寫程式的人」變成「定義問題、審查決策的人」。


這個轉變有一個意料之外的副作用：你會發現自己對技術廣度的需求變高了。當 AI 幫你寫 code，瓶頸不再是「我會不會寫這段邏輯」，而是「我在 spec 裡做的技術判斷對不對」。System Design 的關注點從語言熟悉度移到了業務邏輯的合理性，你不用在意寫不寫得出來，但你要知道什麼是對的設計。


另一個紅利是 POC 成本大幅降低。以前要試一個想法得先花時間 build；現在可以快速驗證假設、試錯、迭代。這是提升系統設計直覺最快的方式之一，也是我自己覺得最有趣的地方。


---


## Phase 1：LLM Integration 的核心基礎


很多工程師的第一個 LLM task，其實不複雜：針對某個業務場景，處理 input、build 一個 prompt、打 LLM API、拿到結果，包成一個 REST service。


就這樣。但這個看似簡單的任務，能讓你快速感受到 LLM 的強大——以及它的不可預測性。


**Prompt Engineering**：不只是「寫一段話問 LLM」，而是結構化地設計輸入——system prompt、user prompt、few-shot examples、chain-of-thought。Prompt 的品質直接決定輸出品質，這是這個階段最值得認真對待的基本功。


**Structured Output / Function Calling**：讓 LLM 回傳 JSON、呼叫 function，而不只是回傳文字。這是從「問 LLM 要答案」到「讓 LLM 驅動行為」的關鍵跳躍，也是進入下一個 Phase 的基礎。


**LLM 的基本屬性**：token 計算、context window 限制、temperature 的作用、latency 與 cost 的 trade-off。這些不是理論，是你在設計 service 時每天都會碰到的決策因子。


以我自己的觀察，目前很多公司還停留在這個階段，甚至根本還沒開始——掌握這層，應該已經算是業界的敲門磚。不確定大家看到的情況是不是也差不多，歡迎留言聊聊。


---


## Phase 2：如何設計 Agentic Systems


這個 Phase 開始真正有挑戰性。你可能被要求整合既有的 agent framework 進 production，或是從零設計一個 SRE Agent、客服 Agent、內部知識庫系統。


幾個核心概念：


**ReAct / Multi-agent 架構**：Agent 不只是「一個 prompt loop」，而是有 reasoning、tool use、memory 的系統。Multi-agent 讓不同 agent 負責不同子任務，但協作設計複雜得多。LangGraph 是一個常見的選擇，但這個領域的工具迭代很快，重點是理解 stateful workflow 的設計概念，而不是綁定特定框架。


**Context Engineering**：管理 context window 是 Agentic System 的核心挑戰。什麼資訊要進 context、什麼要留在外面、怎麼動態組裝，這直接影響 agent 表現和 token 成本。Context Engineering 不是 prompt engineering，而是更上層的資訊架構設計。


**Harness Engineering**：圍繞 LLM call 的基礎設施，包含 retry logic、fallback、caching、rate limit 處理、logging、cost tracking。這是讓 LLM integration 能上 production 的水電管線，往往比 agent 邏輯本身花更多工程心力。


**RAG & Memory**：需要 agent 存取外部知識時，RAG 加上 Vector DB 是標準做法。Memory system 讓 agent 能在多輪對話或跨 session 間保留狀態。


**Security / Trust Layer**：Production 系統裡不能省的一層。Prompt injection 和 jailbreak 不是理論威脅，有人會刻意用輸入來操控 agent 行為。Output validation 確保回應符合預期格式和安全限制。如果系統會處理用戶資料，PII handling 也是必要的設計考量。


**Evaluation & Observability**：LLM 系統很難用傳統 unit test 覆蓋，需要另外設計 eval framework，定義什麼叫「好的輸出」、怎麼量化、怎麼做 regression test。Observability 讓你在 production 裡能追蹤 agent 行為、找出問題。後續的 LLMOps 讓這個系統能持續被維護和迭代。


能比別人早進入這個 Phase，優勢相當明顯。


---


## Phase 3：Fine-tuning、Local Inference 與 Hybrid 架構


我自己的觀點是：未來的模型架構不會是「全部打外部 API」或「全部自己跑」，而是 Hybrid——Frontier model 負責通用推理，自己維護的垂直領域模型負責深度專業場景。成本考量和落地場景的需求，會讓這個架構越來越普遍。


所以這個 Phase 的能力，比你想像的更值得提早佈局。


**LoRA Fine-tuning**：對 open-source model（Llama、Mistral 等）做 fine-tuning，讓模型學習你的領域知識或特定輸出格式。LoRA 是目前最 cost-effective 的方式，不需要從頭訓練整個模型。


**Model Distillation**：用大型 Frontier model 的輸出來訓練一個小型模型，讓小模型在特定任務上逼近大模型的表現，但成本和延遲大幅降低。在 Hybrid 架構裡，distillation 是建立垂直領域輕量模型的關鍵手段。


**Local Inference**：用 vLLM 或類似框架自己跑 inference endpoint，管理 GPU 資源、設計 KV cache 策略節省 token 成本，以及理解 batching、quantization 等加速推論的技術。


這個 Phase 的工程複雜度和基礎設施成本都高很多，但也是目前市場上最稀缺的能力之一。


---


這三個 Phase 不一定要線性走完——很多工程師從 Phase 1 開始，做著做著就被需求推進 Phase 2。重要的是知道每個 Phase 在解決什麼問題、自己目前在哪裡、下一步要補什麼。


**不要怕這些東西太多、太難。**


一個很有效的方式是 Top-Down 學習：不要試圖把每個概念都學透再往下走，而是先快速掃過這些名詞和概念，在腦袋裡建立一個 Index——知道「有這種東西存在」、「它大概解決什麼問題」，就夠了。等到真正要設計系統的時候，你有這個 Index，就知道去哪裡找答案。


更進一步的做法是建立自己的 Knowledge Base，類似 Karpathy 的 llm wiki 的概念——把你讀到的重要概念、tool、paper、設計模式都整理進去。等到要解決一個新問題，可以跟 AI Agent 一起 BrainStorm，請它從你的 knowledge 裡找符合情境的方案，拼湊出一個可行的設計，再針對某個 tool 做一些微調。這套流程的效率遠超過從零開始查資料。


我自己養成了一個習慣：每週掃一次 GitHub Trending。這個領域的 open source 工具出現的速度真的很快，每隔一段時間就有讓你眼睛一亮的東西。說真的很感謝那些無私貢獻的開發者們——正是因為這些人，這條學習路線的成本才能這麼低。


AI Engineer 這個角色還在成形，邊界每幾個月就在移動。但有一件事不會變：能把業務問題跟 AI 系統的設計對得上的工程師，現在和接下來都會很搶手。


最後想說的是，走這條路，技術只是一部分。更重要的是保持好奇心，對每一個「這為什麼這樣運作」都願意多想一下；以及不怕挑戰，看到一個複雜的問題，第一個反應不是「我不會」，而是「這很有趣，來試試看」。


這個時代給了工程師一個很難得的機會：你可以用比以前低得多的成本，真的把一個想法 build 出來。成為一個 Builder，不只是職稱上的轉變，而是一種心態——你不只是在執行需求，你在用 AI 工具把腦袋裡的東西變成真實存在的東西。


這是我覺得現在做工程師最有意思的地方。


最後補一句：如果你真的是頂尖中的頂尖、對自己的研究能力有絕對的自信，當然也可以直接跳進 Frontier Model 的科研行列。但我自己很清楚，那不是我的路。我對 LLM 落地、讓 AI 真正跟真實世界接上的這個方向，反而更有熱情。


上面這幾個 Phase，是我幫自己規劃、想要補足的 roadmap。每個人的職涯背景不一樣，我走的這條路不一定適合你——這也不是什麼教學文或標準答案，單純是一個 Backend Engineer 幫自己整理的學習方向，分享出來給有興趣的人參考。
  
  
 [ Viewpoint ](/blog?tag=Viewpoint) 
 

### 相關文章
[Viewpoint

AI 時代的 PM / HR / Sales：你才是讓 AI 落地的那個人

2026-05-26
](/blog/ai-for-non-engineer-workplace)[
Viewpoint

AI 時代的非工程師：從今天開始，不需要準備好

2026-05-26
](/blog/ai-mindset-non-engineer)[
Viewpoint

你在比的是模型，但決定 Claude Code 效果的是 Harness

2026-05-20
](/blog/claude-code-harness-over-model)
