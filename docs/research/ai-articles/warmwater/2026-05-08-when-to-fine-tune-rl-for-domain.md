---
url: "https://warmwater.dev/blog/when-to-fine-tune-rl-for-domain"
title: "用 SLM Fine-tune 建立垂直領域模型：LoRA、HuggingFace 與 vLLM"
date: 2026-05-08
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  用 SLM 打造垂直 Domain 模型：Fine-tuning、HuggingFace 與 vLLM 
  2026-05-08 · — views      

幾年前我還是個菜鳥 engineer，在一個 Air-gap 環境做事，網路完全隔離，連 npm 都得走 proxy。有一天要 debug 一個自製服務吐出來的 error，完全沒看過，component 名是內部代號，stacktrace 裡的 library 是團隊自己改過的 fork。


我 Google 了三個小時。沒有任何人討論過這個錯誤。


那個年代 GPT 還沒有，Stack Overflow 上最近的相關問題是四年前，答案已經不適用。最後靠翻 source code 硬解掉，但那個過程讓我第一次認真想一個問題：有沒有工具能真的幫上忙，還是這類問題本來就是「你自己的問題，沒人能幫」？


後來語言模型出來了。我測了一下，用通用 LLM 問這類問題——它會給你一個看起來非常合理的回答，引用正確的概念，格式漂亮，但方向完全錯誤。因為它從來沒有見過這個 error。

---


## 模型能力的邊界，就是它訓練資料的邊界


Karpathy 在幾次公開演講裡提過一個觀點：模型學到的是它見過的資料分佈，沒有出現過的領域，就是真正的盲區，不是模型不夠聰明，是它根本沒有那塊地圖。


這句話聽起來直覺，但很多人低估了它的意思。


通用大模型的訓練資料以公開網路為主，涵蓋了大量的技術文件、開源 repo、論壇討論。在這個分佈裡出現頻率夠高的技術棧，模型會很強。但有幾類東西幾乎不會出現在公開網路上：企業內部系統的 error log、私有服務的 API 行為、公司自己 fork 並改過的工具。


這不是資料量的問題，是資料本質上就不會在外面流通。你沒辦法靠更大的模型或更多的參數來補這個缺口，因為那塊知識根本不在訓練集裡。
     前沿模型的知識邊界   公開網路訓練資料 前沿模型能看見的範圍   GitHub  Stack Overflow  技術文件  開源 repo   論壇  學術論文  新聞 / 社群 scaling → 模型在這個範圍內越來越強    ── 訓練資料邊界 ──   企業私有資料 ── 盲區 ✗  private error log（內部元件名、私有 stacktrace） ✗  私有服務 API 行為 ✗  公司自己 fork 並修改過的工具 ✗  Air-gap 環境的 incident 紀錄 scaling 補不了這個缺口 ── 這塊資料設計上就不會流通到外部  

---


## Air-gap 環境為什麼特別難 debug


Debug 本來就很依賴「有人踩過這個坑並寫下來」。出錯的時候，你搜的不是概念，是「這個具體的 error message 加上這個環境，正確的處理步驟是什麼」。


Air-gap 環境把這個依賴關係切斷了兩次。


第一，網路隔離，你連不到 Google、連不到 GitHub issue、連不到任何外部知識庫。第二，這個環境的元件組合是公司特有的，即使你能搜，也找不到對應的案例，因為市面上沒有人有相同的環境。


通用 LLM 在這個場景的問題不只是「它不知道答案」，而是它不知道它不知道。它見過足夠多的工程知識，所以它有信心給出答案，但那個答案是從類似的公開案例拼湊出來的，在你的私有環境裡可能完全沒有意義，甚至會把你導向錯誤的方向。

---


## SLM 策略：不是要打倒前沿模型，是要在特定戰場贏


這時候有人可能想說：那就靠 RAG，把內部文件塞進去。RAG 有它的用處，但它解決的問題是「知識存在但沒被模型看到」。Air-gap 這類問題是「知識本來就沒有系統性地整理成文件」——error 發生的當下，沒有一份文件說這個問題怎麼解，只有分散在工單、聊天紀錄、工程師腦袋裡的隱性知識。


真正的解法是讓模型在這個 domain 裡經歷足夠多的例子，學到這個環境特有的模式。這就是 Fine-tuning 存在的理由。


以開源 base model 為底，在企業內部的 incident 資料、工單紀錄、runbook 上做 Fine-tuning，你不是在訓練一個能和前沿模型競爭通用任務的模型，而是在訓練一個在這個特定環境裡，知道「這個 error 通常是什麼原因、哪些步驟值得先試」的 SLM。


Fine-tuning 是注入領域知識和行為模式，讓模型知道這個 domain 的語言和慣例。RL（Reinforcement Learning）解決的是另一層問題：定義什麼叫做「好的輸出」。在這類 debug 情境裡，好的輸出不只是「正確」，是「能讓工程師在 5 分鐘內採取行動」。這類標準很難用 supervised learning 的方式直接編碼，RL 讓你可以把人類對輸出品質的判斷轉換成可訓練的信號。

---


## Fine-tuning SLM 需要哪些工具？


幾年前想做這件事，光是工程複雜度就能把大多數團隊擋在門外。現在工具生態好很多。


**HuggingFace** 是起點。開源 base model 在這裡，fine-tuning 的工具鏈（PEFT、LoRA）在這裡，評估和分享的基礎設施也在這裡。LoRA 的出現讓 fine-tuning 不再需要動整個模型的所有參數，大幅降低了計算需求，中等規模的企業 GPU 資源就夠跑。


**vLLM** 是部署端的選擇。Fine-tuning 完的 SLM 要服務工程師，需要一個高吞吐量的推理引擎，vLLM 用 PagedAttention 機制大幅提升了效率，是現在自部署 SLM 的標準選項之一。Air-gap 環境不能用雲端 API，vLLM 正好可以完全在內部跑。

---


## 什麼時候不該做 Fine-tuning


Fine-tuning 的成本不低，所以值得先問：這個問題真的需要動到模型嗎？


如果問題其實是 prompt 設計問題——指令不夠清楚、context 給得太雜、格式沒有規範好——那在 harness 層解決會快很多。如果是知識召回的問題，RAG 或給模型 search tool 可能就夠了。


Fine-tuning 值得投入的條件通常是：領域知識本質上就不在任何公開資料裡、模型的失敗不是偶發而是系統性的、而且你有辦法蒐集到足夠品質的 domain 訓練資料。最後這點是最常被低估的。訓練資料品質差的 fine-tuned model，可能比 base model 還糟，因為它學到的是雜訊的分佈。


問題類型建議解法理由指令不夠清楚、格式不對Prompt 設計模型有能力，只是沒拿到對的輸入知識存在但模型沒看到RAG / Search Tool知識可以被索引，不需要重新訓練知識本質上不在公開資料Fine-tuning SLM訓練是唯一讓模型「看見」這塊資料的方式模型知道答案但輸出格式不對Prompt / PEFT輕量調整即可，不需要完整 fine-tuning
     什麼時候才做 Fine-tuning？   模型輸出不如預期 要怎麼選解法？      Prompt / Context 問題？     Prompt 設計 Yes    No   知識可被 索引到？     RAG / Search Yes    No   Domain 資料 品質足夠？     先蒐集資料 No    Yes   Fine-tuning SLM 訓練是唯一讓模型看見這塊資料的方式  

---


## 大模型有一天會把這個問題解掉嗎？


這是一個我覺得還沒有確定答案的問題。


樂觀的情境是：scaling 繼續，訓練資料的來源越來越廣，模型逐漸能涵蓋更多的垂直 domain。已經有跡象顯示，GPT-4 系列在某些技術細節上比幾年前的通用模型強很多，部分原因就是訓練資料更多元了。


但有一股反向的力量：data privacy 的趨勢。企業資料越來越不可能對外流通，GDPR、資料主權法規、各國監管要求，都在讓私有資料更難成為公有訓練集的一部分。Air-gap 環境的 incident log 永遠不會貢獻給 OpenAI 的訓練資料，因為那本來就是設計上不讓它出去的。


這意味著通用模型能覆蓋的邊界，可能不是靠 scaling 就能突破的。未來的格局或許不是「一個更強的模型能回答一切」，而是「企業自己養一個能看見自己資料的模型，旁邊跑著通用模型處理其他任務」。兩者並存，各司其職。


這個問題的答案最後可能不是技術問題，而是資料主權的問題。

---


## 延伸閱讀


- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — 在動模型之前，harness 層能解決什麼

- [Agent 怎麼學會新技能：Skill 系統設計與自我強化迴路](/blog/agent-skill-self-reinforcement) — 不動模型的知識累積替代方案
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)
