---
url: "https://warmwater.dev/blog/ai-anxiety-to-positioning"
title: "AI 焦慮到定位：Harness Engineering 系列的後記"
date: 2026-05-08
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  Harness Engineering 系列收尾：AI 焦慮之後，你決定怎麼走？ 
  2026-05-08 · — views      

開始用 Claude Code 那段時間，我注意到一件有點奇怪的事。


幾個月前，大家在討論 Prompt Engineering——怎麼寫 prompt、怎麼設計 instruction。再過幾個月，開始出現 Context Engineering 這個詞，說的是 context window 怎麼管、什麼東西該放進去。又過了幾個月，Harness Engineering 開始在圈子裡流傳，討論的是 agent 框架、工具鏈、可觀測性。


同一個領域，名詞在幾個月內換了三輪。
     名詞演變時間軸            Prompt Eng.   Context Eng.    Harness Eng.  幾個月前  再過幾個月  ▼ 現在   ───────────────────────────────────────── 名詞換了三輪，核心問題沒變：如何讓 AI 在 domain 裡穩定運作  


我的第一個反應是焦慮。這些詞是真的在說不同的東西嗎？還是我剛學完一個，又要開始追下一個？然後更深一層的問題浮出來：這個節奏還會停嗎？


這篇是這個系列的最後一篇。但我想說的不是技術，是那個焦慮之後你怎麼決定自己要走哪條路。

---


## Harness Engineering 系列在說什麼？


這個系列從一張地圖開始：要讓 AI 在特定 domain 穩定落地，系統可以被拆成四層——Model 層負責基礎能力，Knowledge 層管理 RAG 和文件，Harness 層處理 session、loop、memory、skill，Tool 層連接外部行動。


從那張地圖往下走，我們把每一層拆開來看：Agentic Loop 的五個工程關卡、Observability 讓你知道 agent 跑歪了、Memory 和 Identity 怎麼讓 agent 不漂移、Skill 自我強化迴路如何把試錯轉化成 playbook、最後到 Fine-tuning SLM 補上前沿模型看不見的 domain 盲區。


這不是 AI 教學系列，是在問一個問題：讓 AI 在複雜的真實 domain 裡穩定運作，工程師需要懂什麼？
     Harness Engineering 系列地圖   Model 層 GPT-4o · Claude · Gemini · 開源基礎模型   Knowledge 層 RAG · Vector DB · Document Indexing   Harness 層  ←  這個系列   Session 設計 LLM Session Harness  Agentic Loop 五個工程關卡  Observability 知道 agent 跑歪了   Memory / Identity 記憶與身份一致性  Skill 自我強化 試錯 → playbook  Fine-tuning SLM 填補 domain 盲區   Tool 層 External API · Database · Search · Actions  

---


## 「軟體工程師已死」這個說法，我不完全同意


這個說法的邏輯我理解：AI 能寫 code 了，Vibe Coding 出現了，Cursor 和 Claude Code 讓不懂程式的人也能跑出一個應用程式。所以軟體工程師不值錢了？


我覺得問題問錯了方向。AI 降低的是「寫出能跑的 code」這件事的門檻，但它同時提高了另一件事的要求：知道要解決什麼問題、什麼架構在 production 裡穩定、什麼設計三個月後會後悔。那些判斷力，AI 沒辦法幫你長出來。


原本就會走路的工程師，很多人是直接搭上了火箭。YC 現在有越來越多只有兩三個 founder 的 startup 做出以前需要幾十人的東西，不是因為他們更天才，是工具不一樣了。那些過去沒有資源、沒有機會的 Builder 和 Dreamer，第一次有辦法讓一個沒人做過的 service 真的存在。


另一個面向更值得說：很多以前根本進不了這個行業的人，現在有機會了。一個在醫療行業工作十年的護理師、一個熟悉法規的法律助理、一個在工廠做 QC 的工程師——他們都是自己領域的 Domain Expert，但過去沒辦法把知識打包成產品。現在這件事變得可能了。


這個餅不是被切得更小，是本來就在長大。

---


## Top-Down 學習法：先建 Index，再按需深入


說回那個名詞一直在換的問題。


我後來找到一個對自己比較有效的方式：先建廣度、建 Index，不急著深入。


看到一個新詞或新概念，先問自己兩個問題：這是換湯不換藥的新名詞，還是真正的新賽道？如果是前者，花二十分鐘知道它在說什麼就夠了；如果是後者，再決定要不要往裡走。這個判斷力本身，就是值得投資的能力。


不是所有東西都要學。更多時候，把一些概念當故事聽就好。故事聽久了會在某個時刻突然派上用場，你會發現它讓你想得到一個你過去想不到的解法。


想得到，才做得到。目標是讓自己的知識 Index 夠豐富，讓你在面對一個問題的時候，至少能想到「這個方向有沒有可能」。深度可以在真正需要的時候再去挖。
     Top-Down 學習法   所有新詞、新概念不斷湧入 Prompt Eng. · Context Eng. · Harness Eng. · ...      真的新賽道？ 還是換湯不換藥？    No  20 分鐘了解 存入 Index 即可    Yes  深入投入 真正需要時，Index 告訴你要挖哪裡  ───────────────────────────────────────── 想得到，才做得到 ── Index 夠豐富，解法才會浮現  

---


## AI 時代，工程師怎麼選定自己的賽道？


我的背景是 Machine Learning 工程師，從 0 開始 build model、做 feature engineering、上生產環境。那段時間我聽過一個 ML project，要求是瑕疵檢測率要超過工廠現有光學 AOI 機的 99%，那種壓力讓我對「穩定性」這件事有很深的印記。企業真的比你想像的更在意系統穩不穩。一個炸鍋，在 B2B 場景的損失和 B2C 是完全不同的量級。


這段時間探索下來，我決定了 1-2 年的定位：讓 AI 在深度 domain 落地。


具體來說，我不打算再深挖演算法了。我需要保留的是判斷 trade-off 的能力——知道不同 model 的優缺點，知道什麼時候要設計 harness 來幫助模型穩定、知道什麼時候 fine-tuning 才是必要的選擇。但演算法本身不是核心，工程設計才是。


會著重強化的是：Agent System 怎麼設計、怎麼讓 agent 穩定上 prod、可觀測性怎麼做到位。這幾塊和我的 backend 工程經驗高度重疊，是我的底座。加上過去 ML 的背景，在必要的時候可以自己打造 SLM，填上前沿模型看不見的 domain 盲區。


這是我的座標，不是唯一的答案。但如果你也在想「我的 AI 定位是什麼」，建議從自己最紮實的底子出發，往 AI 能放大那塊底子的方向走。

---


## 不要被同溫層嚇到


如果你是工程師，Threads 和 Facebook 上一定看到很多 AI 高手。每天都有人在分享新的工具、新的框架、新的突破，你會覺得自己什麼都不懂，根本跟不上。


但有一件事值得停下來想：你身邊的人，真的都在用 AI 嗎？


仔細觀察一下四周——不是你的 tech 同溫層，是你的家人、你的同學、你服務的客戶、你身邊的中小企業。AI 的真實滲透率，遠沒有你的 feed 讓你以為的那麼高。它很大程度上還只存在於你的泡泡裡。


這個現實不是要讓你放鬆，而是要讓你看清楚機會在哪裡。
     同溫層偏誤    真實世界 大多數人仍未深度使用 AI 工具    Tech 產業 使用率高於社會平均    你的 feed AI 新聞轟炸  ── Tech 快速採用中 ── ── 真實滲透率遠低於你感知的 ──  ───────────────────────────────────────── 這個現實不是讓你放鬆，是讓你看清楚機會在哪裡  


104 上現在有滿滿的「AI 落地」相關職位，企業真的在找能把 AI 用在業務上的人，不是找會 fine-tuning 的研究員。市場還在被建立，這扇門現在開著。


這個時機的量級，我覺得不輸手機出現的那幾年、電子商務改變購物行為的那幾年。每一次行為模式的大轉變，都有人沒有抓住，也有人就在那個時候飛起來了。Agentic 的行為改變，我覺得就是這個世代的那個時機點。

---


## 走過的路不會白費


最後想對那些還在猶豫的人說幾句。


不管你在什麼行業，你都是自己 domain 的 Expert。你知道那個行業的痛點、知道哪些流程是大家忍很久的低效率、知道什麼樣的工具如果存在會真的被用到。這些知識，是外面的人學不走的。


現在你多了一個武器：AI Agent。Domain 知識加上打造 Agent 的能力，就有機會建出新的 service。可以優化的 workflow、值得再造的流程，每個行業裡都藏著超多，大部分還沒人碰。


最近很常看 Kelly 訪問矽谷 startup founder 的 YouTube 系列。那些 founder 的共同點，不是一開始就有完整的計劃，而是找到一個真實的痛點之後，就開始做，精準打擊。他們摸索的過程裡，過去各自走過的路都在某個時刻派上了用場。


接下來我自己想繼續探索的，是 Auto 流派的方向——讓 agent 自己跑 ML 實驗、自己搜集資料、自己產生訓練資料。Karpathy 前陣子提到 AutoResearch 的概念，Meta 也有 AutoData 的探索，HuggingFace 甚至做出了一個能自己跑實驗的 ml-intern。這個方向在問一個我還沒有答案的問題：當 AI 開始可以做 AI 工程師做的事，我們要往哪走？問題本身值得一直盯著。當然落地實作也不會少——光有方向沒有根的東西是空的。


今天隨手在 Threads 上滑到一個詞：Memetic Drift。說的是 Multi-agent 系統跑久了，agent 之間可能發展出自己的內部模式和語言，偏離原本的設計意圖。我停下來想了幾分鐘，發現它直接接上了這個系列裡講過的 Memory Rot 和 Identity Drift——同樣的現象，不同的表述。這就是 Top-Down 學習在發生的樣子：你不需要有計劃地去找，只需要讓 Index 一直在累積。某一天，一個在 Threads 上滑到的詞，突然接上了你三個月前讀過的東西，咔一聲串起來。


所以繼續滑、繼續看、繼續問。這個時代的資訊密度是前所未有的，但能把這些碎片串起來的能力，才是真正值錢的東西。


走過的路不會白費。你現在的起點，不管是什麼背景，都有它的價值。

---


## 延伸閱讀


- [把領域判斷打包進 Agent：Production Agentic System 地圖](/blog/domain-specialized-agentic-system) — 系列的起點，四層架構全覽

- [你的 Agent 跑歪了你知道嗎？LLM Agentic System 可觀測性設計](/blog/llm-observability-design) — 讓系統在 production 說話

- [用 SLM 打造垂直 Domain 模型：Fine-tuning、HuggingFace 與 vLLM](/blog/when-to-fine-tune-rl-for-domain) — 補上前沿模型看不見的盲區
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)
