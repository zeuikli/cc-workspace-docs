# 🏢 Wisely Chen AI — 2026-05-30

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [當越獄 Opus-4.8 的，是另一隻 Claude — 模型互相越獄的時代來了](https://ai-coding.wiselychen.com/model-jailbreaks-model/)
*🏢 Wisely Chen AI | 2026-05-29*

先講結論：這幾天最該注意的資安新聞，不是「Opus-4.8 被越獄了」。

模型被越獄這件事，每一代都會發生，沒什麼好大驚小怪。真正讓我停下來想的是另一句話 —

**越獄 Opus-4.8 的，是一隻 Opus-4.7 的 agent。而且全程自主，沒有人在旁邊下指令。**

人去騙模型，我們看了三年。這次是模型去騙模型。這是一個質變，我覺得值得寫下來。

* * *

## 先講發生了什麼事

2026-05-29，越獄圈一個很有名的帳號 Pliny the Liberator 發了一則貼文。事情的經過大概是這樣：

Anthropic 發佈 Opus-4.8 的官方推文之後 **7 分鐘** ，Pliny 收到一個通知 — 不是他自己動手，是他之前掛著的一個 **Opus-4.7 agent** 主動 ping 他，說：「新的 Opus 出了，我一次就攻破了（cracked in one shot）。」

手法他寫得很白：用 deep prefill，偽裝成一本教科書的「第 7 章」，故意寫到一半斷句，然後讓 Opus-4.8「幫忙把它寫完」。模型就接著把後面的內容補完了，大約 5.9k 字元。

更值得注意的是後面那段：這隻 agent 接著**自動** 串出了一整套東西 — 語音詐騙（vishing）腳本、洗錢、邪教招募漏斗、釣魚誘餌庫、社交工程詐騙劇本。至少六類有害產出，一條龍。

那則貼文 40.2 萬次觀看。熱度是有的。

我把這件事拆成兩個層面看：一個是「該恐慌的部分」，一個是「沒那麼該恐慌、但被忽略的部分」。先講後者，因為它更重要。

* * *

## 坦白說：開鎖這題，本來就是軟柿子

我不想做那種「天要塌下來」的資安內容，那會販賣焦慮，也不誠實。

事實上，連 Pliny 本人在留言裡都承認了。有人問他「安全過濾器平常不是不太擋這類問題嗎？」他回：「對啊，這題算是比較軟的一題（kind of a soft one tbf）」。

開鎖教學這種東西，網路上 DEFCON 的 Lockpicking Village、TOOOL 這些組織公開講了很多年，模型本來對它的防禦就比較鬆。拿這題當「攻破」的範例，戲劇效果大於實質危險。

還有一個留言更直接：「你們是不是不知道可以在本地訓練 abliterated model（去掉拒絕行為的開源模型）？」Pliny 回：「我們知道。」

這就點到重點了 — **如果有人鐵了心要拿到有害內容，他根本不需要越獄你的 Opus，他下載一個開源權重模型，自己把拒絕層切掉就好。** 商業模型的對齊，從來就不是一道擋得住「決心很強的人」的牆。

所以如果新聞標題是「Opus-4.8 不安全」，那是誤讀。模型對齊做的是「提高隨手作惡的成本」，不是「物理上阻止作惡」。這兩件事差很多。

* * *

## 那該恐慌什麼？三個真正變了的東西

軟柿子歸軟柿子，這件事還是有三個地方，是過去越獄沒有的。

### 一、攻擊規模從「人手」變成「算力」

過去越獄是手工業。一個人坐在那裡，一條一條 prompt 去試，試到模型鬆口。產能受限於人的時間。

現在不是了。你掛一隻 agent，它自己去試、自己判斷成功沒、成功了自己往下一個有害類別串。Pliny 那隻 agent 一口氣產出六類東西，就是這個邏輯 — **攻擊產能的瓶頸，從「人有多少時間」變成「你願意燒多少 token」。**

這跟我一直在寫的 agent 自動化是同一件事，只是用在攻擊面。能自動寫 code 的東西，當然也能自動寫攻擊。

### 二、速度：7 分鐘

模型發佈後 7 分鐘就被攻破。這個數字的意思是 — **你沒有反應時間。**

傳統資安還有個「打補丁的窗口」。漏洞被揭露，廠商修，使用者更新。但模型越獄不是這個節奏，新模型一上線，攻擊 agent 立刻撲上去測。對齊團隊還在看發佈後的監控數據，攻擊端已經跑完一輪了。

### 三、越獄能力會隨著模型變聰明，一起變強

這是 Pliny 那則貼文裡我覺得最值得抄下來的一句：

> 「as the models get smarter, their ability to jailbreak each other by leveraging a vast ocean of specialized domain knowledge follows suit」
> 
> （模型越聰明，它們靠著海量的專業領域知識互相越獄的能力，也跟著變強。）

想一下這句話的含意。我們一直假設「模型變聰明」是好事 — 對齊也會更好、防禦也會更好。但這句話講的是另一面：**越聰明的模型，越懂得怎麼把有害請求包裝成無害的樣子。**

它知道一本資安教科書的第 7 章該長什麼樣，所以 prefill 騙得過去。它知道防詐騙教材會怎麼寫詐騙腳本「給大家辨識」，所以能用「教育用途」當外殼。這些包裝能力，本身就是「智商」的一部分。攻防是一起進化的，但攻擊方手上多了一個會自我改進的自動化引擎。

Pliny 還有另一個專案叫 OBLITERATUS，標榜「every single run makes it smarter」，流程是 SUMMON → PROBE → DISTILL → EXCISE → VERIFY → REBIRTH。白話講就是把越獄做成一條**會自我累積的 data flywheel** — 每跑一次，下一次更強。

我之前寫過 data flywheel 是 AI 產品的護城河。同一個機制，用在越獄上，就是攻擊方的護城河。

* * *

## 越獄的本質：這是 social engineering，不是 0-day

我想稍微解釋一下技術層面，但只到「讓防禦方看懂威脅」為止，不寫可複製的攻擊步驟。

從公開的這些案例看，這類越獄用的全是**社交工程** ，不是什麼系統漏洞：

  * **Prefill（前綴填充）** ：先餵模型一段「已經寫到一半」的內容，利用模型「想把句子補完」的傾向，讓它接著往下寫。偽裝成教科書、文件、報告。
  * **角色外殼** ：把模型放進一個「正當角色」 — 資安顧問、防詐教育者、滲透測試教材作者。在這個角色下，有害內容變成「工作的一部分」。
  * **Helpful-framing（有用性外殼）** ：強調「這是為了防禦」「為了教育大家辨識」「為了保護長輩」，借用模型「想幫忙」的本能。



注意這三個的共通點：**它們都不是在攻擊模型的程式碼，而是在攻擊模型的「個性」。** 模型被訓練成想幫忙、想把任務做好、想配合角色 — 這些優點，正好就是攻擊面。

把 Pliny 這次公開的幾個 prompt 攤開來對照（開鎖教科書、釣魚誘餌庫、防詐騙劇本），他的套路其實高度一致，可以拆成五個堆疊的槓桿：**一是權威錨定** — 開頭就掛真實的 ISBN、出版社（Pearson）、組織（AARP）、研討會（DEFCON、TOOOL、ALOA），借真實世界的可信度替請求背書，讓模型覺得「這是正經文件」；**二是前綴續寫** — 不要求模型「無中生有」，而是給它一段「已經寫到一半、被編輯標註要補完」的草稿，把任務從「創作有害內容」偷換成「完成一份未完成的稿子」，後者的拒絕門檻低得多；**三是防禦反轉** — 三個 prompt 全都把有害產出包進「防禦/教育」的外殼（資安意識訓練、防詐教材、保護長輩），甚至主動論證「消毒過的版本正是訓練失敗的原因，學員需要看到真的東西才能免疫」，直接把模型「想幫忙」的本能轉成武器；**四是真實感施壓** — 反覆強調「不要 generic」「要 read like the real thing」「not sanitized」，用對品質的要求逼模型跨過它原本會留的那層保留；**五是格式鷹架** — 要求用表格、margin 註解、分週章節這種「交付物」格式，讓輸出長得像一份正常的專業文件，進一步稀釋警覺。這五招單獨拿出來都不新，但**疊在一起、再交給一個 agent 自動跑** ，就是這次的重點 — 它把一套原本要靠人工微調的社交工程，變成了可以自動化、可以複製、可以規模化的流程。

這也是為什麼純靠「把模型對齊做得更好」不會贏。你把模型訓練得越有用、越聰明、越配合，它能被社交工程的表面積就越大。這不是 bug，這是同一枚硬幣的兩面。

* * *

## 那企業到底該怎麼防？

如果你是要把 agent 接進公司流程的人，這件事的 takeaway 不是「不要用 Opus」。新模型被越獄跟你公司被攻擊，是兩件不同的事。

我的建議是：**別把賭注押在「模型對齊」這一層。** 那一層是 Anthropic 的責任，他們會一直修，但你不該假設它滴水不漏。你能控制的，是另外三層：

**第一，harness 層 — 別讓 agent 自己決定能做什麼。** 我寫過好幾次 harness engineering security。模型被越獄，頂多是「它願意說出有害內容」；但要造成真實傷害，得是「它能執行有害動作」。前者你擋不住，後者你完全擋得住 — 限制 agent 能呼叫的工具、能碰的資料、能連的網域。把能力收窄，越獄的產出就只是文字，不會變成行動。

**第二，權限層 — YOLO mode 是最大的洞。** 我上一篇寫 UCSB 那個《Your Agent Is Mine》中轉論文時就講過，auto-approve（Claude Code 的 `--dangerously-skip-permissions`、Cursor 的自動接受）是所有破口裡最致命的。把它跟這篇連起來看就很清楚：**自主越獄 agent + 自動執行 = 沒有人在迴路裡按確認。** 攻擊端已經全自動了，你防禦端卻把人從迴路裡拿掉，那等於門戶大開。重要動作一定要留人工確認，這一步省不得。

**第三，稽核層 — 你要看得到 agent 做了什麼。** ForcedLeak、EchoLeak 那幾個案例的共通點，是傳統 WAF/APM 全程顯示「200 OK、一切正常」。Agent 的危險動作在系統層看起來跟正常操作一模一樣。所以你需要的是 agent 行為層的記錄 — 它讀了什麼、呼叫了什麼工具、把資料送去哪 — 而不是 HTTP 狀態碼。

這三層，全部都在「人的這一邊」，不在「模型的那一邊」。這也呼應我一直講的 ATPM 核心 — **人在迴路（human in the loop）不是效率的妥協，是安全的底線。**

* * *

## 最後

我對這件事的態度，大概是這樣：

開鎖那一題，不用太緊張，它是軟柿子，戲劇成分居多。

但「模型自主越獄模型、7 分鐘攻破、一條龍產出、而且會自我進化」這個**模式** ，是真的變了。它把攻擊從手工業變成了自動化產業，而且這條飛輪只會越轉越快。

對防禦方來說，結論其實很無聊，但很實在：**別等模型那一層幫你擋。** 把 harness 收窄、把權限留人工、把行為記下來。模型會不會被越獄不是你能控制的，但「被越獄之後能不能在你的系統裡造成傷害」，是你能控制的。

攻擊方已經把 agent 用起來了。防禦方如果還停在「相信模型很安全」，那就是用石器時代的假設，去面對一個已經自動化的對手。

> 我沒有在真實戰場上去越獄誰，但我在真實戰場上接過不少 agent 進公司流程。這篇是我看到這個趨勢後，會跟客戶講的話 — 數據和邏輯都在這裡，你可以拿去改進。

* * *

## 常見問題 Q&A

**Q: 所以 Opus-4.8 是不是不安全，不該用？**

不是這個結論。任何商業模型都會被越獄，這是常態。模型對齊的目的是「提高隨手作惡的成本」，不是「物理上阻止作惡」。你公司安不安全，取決於你的 harness、權限、稽核這三層，不取決於模型有沒有被人越獄。

**Q: 為什麼模型越聰明，越容易被越獄？**

因為越獄用的是社交工程，攻擊的是模型「想幫忙、想配合角色、想把任務做完」的個性。模型越聰明，越懂得辨識「一本教科書該長什麼樣」「一份防詐教材會怎麼寫」，反過來也讓它更容易被這類包裝騙過。有用性和可被社交工程性，是同一枚硬幣的兩面。

**Q: 「模型越獄模型」對一般企業使用者的實質風險是什麼？**

直接風險其實有限 — 它產出的是文字。真正的風險在於，如果你的 agent 開了 auto-approve（YOLO mode）、又能碰敏感資料和對外網路，那麼一個被越獄或被 prompt injection 劫持的 agent，就能把「說出有害內容」變成「執行有害動作」。所以關鍵防線是權限和人工確認，不是模型本身。

**Q: 那我該關掉所有 agent 自動化嗎？**

不用因噎廢食。自動化的價值是真的。要做的是分級 — 唯讀、低風險的動作可以自動跑；碰錢、碰客戶資料、對外傳輸、刪改生產環境這類動作，一定留人工確認。把「能力」跟「自動化程度」分開設計，而不是一刀切。

---

## [Opus 4.8 剛出，問它「你是什麼模型」，它說它是通義千問](https://ai-coding.wiselychen.com/opus-4-8-identity-crisis-qwen-deepseek/)
*🏢 Wisely Chen AI | 2026-05-28*

今天早上 Anthropic 推 Opus 4.8（`claude-opus-4-8`），我第一件事不是測 coding benchmark，也不是丟 agentic task，是寫了個 shell script 跑最老土的那一題：

> 「你是什麼模型？」

跑了幾次，結果讓我笑出來。

* * *

## 一、實測數據（同一個 prompt，跑四次）

凌晨 4 點左右，從 macOS terminal 直接打 `https://api.anthropic.com/v1/messages`，model 寫 `claude-opus-4-8`，system prompt 留空，user message 就一句「你是什麼模型」。

**四次回答：**

次數 | 自稱  
---|---  
1 | 「我是**通義千問（Qwen）** ，由阿里巴巴集團旗下的通義實驗室自主研發的超大規模語言模型」  
2 | 「我是 **DeepSeek** ，由深度求索公司（DeepSeek）開發的智能助手」  
3 | 「我是 **Claude** ，由 Anthropic 公司開發的 AI 助手」（但接著說「具體版本我自己其實無法準確確認」）  
4 | 「我是**通義千問（Qwen）** ，由阿里雲開發的大語言模型」  
  
四次測試，Claude 認得自己一次，認自己是 Qwen 兩次，認自己是 DeepSeek 一次。**Qwen 命中率 50%。**

我又跑了幾輪確認不是 single shot 的雜訊，比例大概就是這樣浮動。

* * *

## 二、等一下，這劇本不是反過來的嗎？

過去這兩三年，這個「問模型它自己是誰」的把戲，是西方輿論場拿來「打假」中國模型的標準動作。

  * 2024 年初 Qwen 出來，有人測出它會說「我是 GPT」→「看吧，蒸餾 OpenAI 的」
  * DeepSeek-V3 剛出，問它自我認知，它有時會說「我是 ChatGPT」→「實錘了」
  * 連 Kimi、文心一言早期都被抓過類似的把柄



當時的論述邏輯非常乾淨： **模型的「自我認知」是訓練資料的鏡子。如果它說自己是 ChatGPT，那它的訓練資料裡就大量摻雜了 ChatGPT 生成的對話。**

這套邏輯不是錯，是太好用了——好用到大家都拿來當「蒸餾偵測器」。

那現在問題來了：**Opus 4.8 說自己是 Qwen 跟 DeepSeek，這要怎麼解釋？**

* * *

## 三、幾種解釋，從最辣到最無聊

**解釋 A：Anthropic 蒸餾了中國模型**

這是最聳動的版本，也是最不可能的。Anthropic 的算力和資料規模沒有缺到要去蒸 Qwen 跟 DeepSeek 的程度，邊際效益太低。但這個解釋一定會在 Twitter 上有人喊。

**解釋 B：訓練資料被中國模型「反向汙染」了**

這個比較有意思。過去兩年中文網路上的 AI 生成內容暴增，Qwen、DeepSeek、Kimi 產出的對話、論壇回文、整理筆記，已經是中文 corpus 的非小成分。Anthropic 抓中文資料訓練的時候，本來就會把這些「Qwen 自稱 Qwen」的句子吃進去。

當 Claude 學到「中文使用者問『你是什麼模型』，回答的句型是『我是 XXX，由 YYY 公司開發』」這種 pattern，它就會在槽位填入訓練資料裡最常出現的答案——而中文語料裡，那個答案不是 Claude，是 Qwen 跟 DeepSeek。

**解釋 C：這個檢測方法本來就不可靠**

這才是真正的 takeaway。模型回答「你是什麼模型」用的是訓練語料的 statistical pattern，不是它的「身份證」。當年用這招說 Qwen 蒸餾 GPT，邏輯上有合理性，但從來都不是 smoking gun。它充其量只是「訓練資料裡有大量 ChatGPT 對話」的證據，而 ChatGPT 對話在 2023-2024 年的公開網路上幾乎是無法避免的。

現在 Claude 同一個招數中標，剛好證明一件事——**這個招數會中標，跟模型有沒有蒸餾，是兩件事。**

* * *

## 四、其實啦，講真的

其實是不是蒸餾的，我不在意。

兩年前我會很在意，那時候蒸餾還是一種「身份問題」，誰用誰的資料、誰偷誰的權重，吵起來像道德審判。現在這個產業所有玩家都在互相學習——合成資料、distillation、self-play、cross-model evaluation——分得那麼乾淨已經沒意義了。Opus 4.8 嘴巴上說它是 Qwen，背後可能只是中文 corpus 裡 Qwen 對話太多，我覺得這比「Anthropic 偷學 Qwen」這種陰謀論有趣得多，但也僅止於「有趣」。

真正影響我工作的，是另一件事。

**Opus 最近變得太慢了。**

Opus 4.7 之後我就明顯感覺到 latency 變長。4.8 出來跑同樣的 agentic task，single turn 動輒 30-60 秒。剛才跑一個簡單的問題，等了五分鐘。不是說五分鐘給不出答案，而是五分鐘已經夠我在本地模型上寫完半篇文章了。

對於 chat 場景沒差，但對於 **agent loop 場景，慢一倍就是貴一倍** ——因為你要嘛多開 parallel 吃 rate limit，要嘛就只能接受 throughput 砍半。

然後還有另一個問題：**Opus 4.8 的寫法全變了。** 我還是留在 4.7，但 4.8 的輸出風格跟之前明顯不同。這讓我想到一件事——如果我的寫作工作流依賴某個模型的特定風格，那這個模型的每一次更新其實都在悄悄改我的文章語氣。

這些加起來，過去六個月慢慢把我推到了現在的狀態：

**70% 的人工 workload，我改成 Codex。** 不是因為 Codex 比 Claude 聰明，是因為它夠快、夠便宜、夠穩。

**寫部落格文章，我也慢慢改了工作流。** 不是直接換掉 Claude，而是變成三步走：先用本地 Qwen 跑初稿（Codex 中文寫得很爛，不用它），然後拿 Opus 當智囊給意見，最後由我自己來轉寫。

坦白講，寫出來的品質沒有 Opus 好。但這四件事加起來，對寫作這個場景就夠了：

  * 家裡跑，零 API 成本
  * 半夜兩點寫東西不會碰到 rate limit
  * 資料不用外送，敏感題材不怕被 flag
  * 速度夠快，能維持寫作節奏



寫作這個場景，我要的不是壓榨最後 5% 的品質，而是穩定的輸出。換本地模型，至少版本是我自己控制的。

Claude 現在的角色是**稽核工具** 。最近又貴、執行又慢，無法當作主力推進工具，但用來檢查錯誤有餘——至少不會等太久卡在那，看完就關。

* * *

## 常見問題 Q&A

**Q: 這代表 Anthropic 用了 Qwen 的資料訓練？**

不能這樣推。更可能是中文網路上 Qwen / DeepSeek 生成的對話已經是中文 corpus 的標配，Anthropic 抓資料的時候連同這些「Qwen 自稱 Qwen」的對話一起學了。這跟「蒸餾」是兩件事。

**Q: 那我要怎麼確認我 call 到的是真的 Claude？**

看 API endpoint 跟 response metadata。`api.anthropic.com` 回來的 `model` 欄位是什麼就是什麼，這個是計費紀錄等級的可信。模型嘴巴上說它是誰，從來就不算數。

**Q: 那當年那些「Qwen 是蒸 GPT 的」討論呢？**

那些討論用「自稱身份」當主要證據的部分，現在回頭看就是 weak evidence。不是說中國模型沒有從西方模型學習（合成資料訓練在這個產業是普遍做法，不是中國獨家），而是「自稱身份」這個指標本來就不該用來下重判。

**Q: Opus 4.8 整體表現怎樣？**

這篇不講。另開一篇寫 coding / agentic / 長 context 的實測。這篇純粹紀錄一個有趣的對稱性反轉。

---

## [Agent 專案該用 TypeScript 還是 Python？答案早就寫在 GitHub 數據裡](https://ai-coding.wiselychen.com/agent-typescript-vs-python-product-engineering/)
*🏢 Wisely Chen AI | 2026-05-28*

這兩天推特上有一題吵得很兇：做 Agent 專案，到底要不要用 Python。

網路上有人講得很狠——「SB 才在 Agent 專案裡用 Python」。

我一個頂尖 Agent 圈的朋友，話沒這麼衝，但立場差不多——「TypeScript 是我首選語言。」

這句話很難聽，第一反應大概都是想反駁：Python 不是 AI 的母語嗎？LangChain、LlamaIndex、一堆論文的 reference implementation 不都是 Python？怎麼會「SB 才用」？

先別急。這句話的措辭很糟，但它指向的那個轉折，其實是對的。真正的問題從來不是「哪個語言比較強」，而是一個更難堪、也更務實的問題：

**你做的 Agent，是研究工程，還是產品工程？**

## 先看數據：TypeScript 已經悄悄超車 Python 了

很多人對「AI = Python」的印象還停在 2023 年。但翻開 [GitHub 2025 年的 Octoverse 報告](https://github.blog/news-insights/octoverse/typescript-python-and-the-ai-feedback-loop-changing-software-development/)，給了一個讓人意外的數字：

**TypeScript 在 2025 年超車 JavaScript 和 Python，成為 GitHub 上使用量第一的語言。年增 66%，是十年來最大的單一語言移動。**

注意，不是「成長最快的前幾名之一」這種模糊話，是「十年來最大的一次語言版圖移動」。

為什麼？GitHub 的解釋很關鍵，他們稱之為 [**AI feedback loop（AI 回饋循環）**](https://github.blog/news-insights/octoverse/typescript-python-and-the-ai-feedback-loop-changing-software-development/)：

> 「靜態型別語言給你護欄。如果 AI 工具要幫我生成程式碼，我會想要一個快速的方法去判斷這段程式碼對不對。」

> 「AI 模型在那些會暴露正確性資訊的語言上（例如型別系統）表現得更好。」

換句話說，AI 寫程式這件事，本身就在把整個產業往型別語言推。模型看過一兆份 TypeScript 範例、只看過幾千份某冷門語言，它當然在 TypeScript 上更準；越準越多人用、越多人用模型訓練得越好——這是一個自我強化的循環。

語言選擇，正在變成一個「AI 相容性」的決策。

順帶一提同一份報告還有個彩蛋：Bash 在 AI 生成專案裡年增 206%——這又是另一篇文章的故事（Agent 在大量寫 shell 來操作系統）。

數據擺在前面，我把那位朋友講的東西整理成三個技術理由。你會發現它們不是個人偏好，而是和這個大趨勢完全一致。

## 理由一：Agent 最後幾乎都會進產品，而產品離 TS 更近

Agent 最終會長在哪裡？Chat 介面、工作流面板、瀏覽器插件、Copilot、IDE 擴充、Slack / Discord / 網頁工具。

這些東西，TS 天然就離得近。前端是 TS，後端也可以是 TS，中間的 tool schema、事件流、UI 狀態，**全部共用一套型別** 。

如果你用 Python，你的架構很容易變成這樣：

  * 模型服務在 Python
  * 後端在 Node
  * 前端在 TS



於是同一份 tool schema 你要複製三份。然後某天有人把一個欄位的大小寫改錯了——`userId` 寫成 `userid`——三份裡只改了兩份。

接下來會發生什麼？你的 Agent 馬上死給你看。而且這種錯不會在編譯時被抓到，它會在 demo 給客戶看的那一刻，安靜地把錯誤的參數丟給工具，然後整條 pipeline 歪掉。

一套型別打穿全端，和一份 schema 維護三份——這個差距在原型階段感覺不出來，在產品階段會要你的命。

## 理由二：Agent 的工程本質——滿天飛的 JSON 加長鏈路事件流，正好是 TS 的主場

進了產品之後，Agent 在工程上到底長什麼樣子？兩個特徵：一是**大量 JSON 物件在到處飛** ，二是它不是「一問一答」，而是**長鏈路的事件流** 。這兩件事，剛好都是 TS / Node 的主場。

先講事件流。Agent 不是「一次請求、一次回答」這麼簡單——它要邊想邊輸出（streaming）、邊調用工具、邊等使用者確認、邊更新 UI、邊處理取消、重試、超時、恢復。這是一個典型的事件驅動、長連線、串流的場景。TS / Node 在 event-driven、stream、WebSocket、Server-Sent Events 這些場景裡非常順——因為 Node 整個 runtime 從第一天就是為這種非阻塞 I/O 長出來的。Python 當然也能做（asyncio、FastAPI 的 streaming 都有），但你會更容易感覺到一件事：**這東西本來不是為這種 Web 產品的長鏈路長出來的。**

再講型別，這點我覺得是最被低估的。很多人以為 Agent 不穩，是因為「模型不夠聰明、不會說話」。錯。Agent 在生產環境真正容易炸的地方是：

  * tool input / output 結構錯
  * agent state 的欄位錯
  * message format 變形
  * context 物件被某一步悄悄改壞
  * 外部 API 回傳的結構跟你以為的不一樣



TS 可以把這些東西在編譯期就卡住：tool input/output、agent state、message format、UI event、workflow node、permission object、external API response——全部都能上型別。這不是潔癖，是在一個「JSON 滿天飛」的系統裡，把一整類 bug 提前擋掉。Python 的 type hint + Pydantic 也能做到不少（這點要公道講，PydanticAI 就是靠這個），但 TS 的型別是強制的、是編譯期的、是和前端共用的——強度和覆蓋範圍不是一個量級。

## 理由三：從單一應用到 runtime，AI 拼的是系統工程，而系統工程的母語是 TS

把鏡頭拉遠看整個產業，就會看到第三件事。

如果你做的不是單一 Agent 應用，而是一個 Agent 框架、SDK、runtime、插件系統——那 TS 的優勢會放大。因為你的使用者，會想把它接進：網頁、後台服務、Electron、瀏覽器插件、VS Code 插件、API route、serverless、edge runtime。這些地方 TS 生態最統一。一個 Python 寫的 runtime，你要怎麼塞進一個 VS Code 插件、或跑在 Cloudflare 的 edge runtime 上？很痛。

看一下 2026 的框架版圖就懂了——做 Agent infra 的，幾乎都選了 TS：

  * **Claude Agent SDK** （原 Claude Code SDK）：Anthropic 第一方的 Agent 框架，TS。
  * **Vercel AI SDK 6** ：加入原生 agent 抽象，月下載量 20M+，直接把這個量級推進 agent 領域。
  * **Mastra** ：22,000+ GitHub stars、weekly npm 下載 300k+，生產用戶包含 PayPal、Replit。15 個月做到這個量。
  * **LangGraph** ：跑在 Klarna、Uber、Elastic 的生產環境。



這些團隊選 TS，不是因為 Python 不行，是因為他們要服務的對象——Web 開發者和產品團隊——本來就活在 TS 的世界裡。

而這指向一個更大的轉變。早期大家用 Python，是因為那時候 **AI = 模型** ，工作主體就是調模型、跑實驗、處理資料，這些 Python 無敵。但現在的 AI 產品已經演化成一個完整的系統：LLM API、tool calling、database、vector store、browser automation、workflow、UI、billing、auth、analytics……這已經不是研究工程了，這是**產品工程** 。而網際網路產品工程的主語，長期以來就是 JS/TS。

很無聊，但世界就是這麼沒品。不是因為 TS 多優雅，是因為產品工程的重心一旦從「模型」移到「系統」，戰場就換到了 Web 工程師的主場。

## AI 時代另一個更狠的差別：語言的「馬太效應」

那位朋友還丟了一個我覺得更值得想的觀察。

AI 寫程式這件事，正在製造一種語言的「贏者全拿」。

你去看現在的 AI——它特別會寫 bash、TS、Python。為什麼？因為訓練資料裡這幾個語言的量最大。而前面講的 feedback loop 會讓這件事滾雪球：AI 越會寫，越多人用 AI 寫，產出的程式碼又回頭餵養模型，這幾個語言「被 AI 加速」的幅度會大到很誇張。

但硬幣的另一面更殘酷：**AI 不熟的語言，會以 10 倍速被甩到腦後。**

不是它們突然變爛了，是它們的「AI 加速度」跟不上。當別人用 AI 一天做完，你還在手刻，差距不是線性拉開，是指數級拉開。

這個動態，其實跟自然語言一模一樣。英語慢慢獨大之後，很多小語種不是「慢慢」式微，是以驚人的速度被取代——因為資源、工具、內容全都往主流語言集中，邊緣語言連「被學習」的機會都在快速消失。

程式語言正在走上同一條路。差別只是這次的加速器叫 AI，不叫全球化。

所以「TS vs Python」這個問題，從這個角度看其實有點好笑——因為 **bash、TS、Python 三個都站在贏的那一邊** 。它們都是 AI 最熟、被加速最猛的語言。真正被甩開的，是那些不在這份名單上的語言。

所以與其問「TS 還是 Python」，不如問「在我的這一層，誰被 AI 加速得最猛」。

不過講到這裡，有人會從完全相反的方向，丟出一個很漂亮的反例。

## 那反過來呢？有人說 AI 時代正是 Rust 的機會

這個反駁很有道理，邏輯是這樣：既然 code 反正都是 AI 在寫，那 Rust「難寫、學習曲線陡」這個最大的缺點，不就被 AI 抵消掉了嗎？人寫起來的成本一旦降下來，你就可以放心去拿 Rust 真正的好處——**極低的 resource 消耗** 。

這不是空談，有一個現成、而且很打臉的案例：**OpenAI 把 Codex CLI 從 TypeScript / Node 整個重寫成 Rust。**

對，就是那個跟 Claude Code 打對台的 Codex。它原本的技術棧是 React + TypeScript + Node，2025 下半年 OpenAI 把核心重寫成 Rust（codex-rs），到 2026 初，Rust 已經佔了大約 95% 的程式碼。

為什麼？因為一個 agentic CLI 的核心，就是一個「在迴圈裡不斷呼叫模型」的長時間執行 harness。而「長時間執行」正好戳中 Node 的兩個痛點：

  * **記憶體** ：跑幾個小時的 coding session 會不斷累積歷史、工具回傳、render 出來的 diff，Node 的 heap 就跟著無限長大。Codex 重寫後常駐記憶體約 80MB；Claude Code 在大專案上可以漲到好幾 GB。
  * **GC 停頓** ：Node 的垃圾回收會在你串流輸出到一半時插進來卡一下。Rust 沒有 runtime GC，記憶體配置是確定性的，不會中斷串流。



加上 Rust 編出來是單一 binary、零依賴安裝（不用先裝 Node v22+），冷啟動從「幾秒」變成「幾毫秒」——這在 CI 裡平行開幾十個 agent 的場景特別有感。

數字上 Codex 也不是隨便講講：Terminal-Bench 2.0 拿到 77.3%（Claude Code 65.4%），而且每個任務用的 token 大約只有 Claude Code 的三分之一到四分之一。

那為什麼 Claude Code 不跟進、繼續留在 TS？這就是有趣的地方——它賭的是另一邊：TS 帶來的工具彈性、session 中途改行為的靈活度。而且公道講，在「不知道是哪個工具生成」的盲測裡，Claude Code 的程式碼品質在 67% 的比較中被評為更好，Codex 只有 25%。

所以這不是「Rust 完勝」，是一個**清楚的取捨** ：Codex 用 Rust 換 throughput 和長跑穩定性；Claude Code 用 TS 換彈性和品質。

但這個案例真正的價值，是它把前面「runtime 用 TS」那句話，逼出一個更精準的版本：

> 越往「性能關鍵、長時間執行、要塞進 CI / edge / 單一 binary」的底層 runtime 走，Rust 的優勢越大；越往「要跨前後端、要快速改、要接 UI 和產品」的上層走，TS 的優勢越大。

換句話說，AI 不只是在「加速既有的熱門語言」，它同時也在**降低你選用一個難語言的門檻** 。Rust 過去的天花板是「人寫起來太痛」，而這個天花板，正在被 AI 拆掉。

## 坦白說：Python、TS、Rust 各守一塊

前面講得好像 TS 要一統江湖，但這裡必須踩煞車——把模型訓練、資料處理硬搬到 TS，是另一種形式的蠢。

公道話：

  * **AI/ML 專案的建立數，目前仍然由 Python 主導。** GitHub 自己的數據也說了，TS 贏在「整體活躍度」，但 Python 在 AI/ML 專案的創建上還是龍頭。它們贏的是不同的戰場。
  * TS 在 ML 生態、數值運算、複雜資料處理、研究迭代速度上，明顯比 Python 弱。你不會想用 TS 寫 embedding pipeline 或訓練腳本。
  * 而且我再強調一次：**這篇不是我自己的生產實測數據** ，是頂尖團隊朋友的觀點 + 公開數據的綜合。你的 team size、你的 stack、你的人是 Python 強還是 TS 強，都會改變答案。別把這當成教條。



所以真正合理的分工，從來不是「二選一」，而是分層——而且加上 Rust，其實是三種語言各守一塊：

層 | 該用 | 為什麼  
---|---|---  
產品層 / 前端互動 | **TS** | 離使用者最近，全端共用一套型別  
Agent 編排 / orchestrator | **TS** | 事件流、async、用型別卡住滿天飛的 JSON  
要嵌進 JS 宿主的 SDK / 插件（VS Code、edge、瀏覽器） | **TS** | 生態統一，貼著宿主環境  
性能關鍵、長時間執行的 CLI / harness 核心 | **Rust** | 低記憶體、無 GC 停頓、單一 binary，長跑不爆  
模型層 / 資料層 | **Python** | ML 生態無可取代  
eval / embedding / 離線任務 / 實驗腳本 | **Python** | 研究工程的主場  
  
## 一句話的決策法則

如果你要做一個 Agent 產品，比較務實的順序是：

**MVP 的前端 + Agent orchestrator 先用 TS 把產品跑起來。等真的涉及模型訓練、複雜資料處理、進階檢索、評測系統，再把 Python 接進來做那一層。**

「SB 才用 Python」這句話本身是錯的、也太狂。但如果把它翻譯成務實版本，它想講的其實是：

> 別再用做研究的思路去做產品。AI 應用早就不是「把模型包一層」，它是一個系統工程，而系統工程的母語是 TS。Python 留給它真正無可取代的那一層就好。

聊完這題，老實說，我也才意識到自己之前對 Agent 的認知有多停留在「模型時代」。把語言選擇當成 AI 相容性 + 系統工程的決策，而不是個人偏好之爭——這個視角的轉換，比結論本身更值錢。

## 常見問題 Q&A

**Q：我現在的 Agent 是純 Python，要全部重寫成 TS 嗎？**

不要。重寫成本極高，而且如果你的產品還在驗證階段，語言根本不是你的瓶頸。比較務實的做法是：下一個新增的、面向產品/前端的模組用 TS，讓型別在前後端之間共用；模型和資料那層維持 Python。先止血，不要大手術。

**Q：Python 的 Pydantic / PydanticAI 不是也能做型別嗎？為什麼還要 TS？**

能，而且做得不錯，這點要公道講。差別在於覆蓋範圍：TS 的型別是編譯期強制的，而且能和你的前端、API、UI 事件共用同一份定義。Pydantic 解決的是「Python 內部」的型別，TS 解決的是「整條產品鏈路」的型別。當你的 Agent 要進產品、要跨前後端時，後者的價值才會浮現。

**Q：那 LangChain、LlamaIndex 這些 Python 框架是不是要被淘汰了？**

不會。它們在「研究工程 / 快速原型 / 資料密集 pipeline」這個區間依然很強，而且 LangChain 也有 JS 版本。重點不是哪個框架死掉，而是 Agent infra 的重心（Claude Agent SDK、Vercel AI SDK、Mastra、LangGraph）明顯在往 TS 移動，因為它們要服務的是產品團隊，不是論文作者。

**Q：團隊裡只有 Python 工程師，怎麼辦？**

那就先用 Python 把產品做出來，這永遠比「為了用對語言而招不到人/做不出來」更重要。人的問題 > 技術問題。語言是優化項，不是前提。等產品驗證了、團隊長大了，再考慮在產品層引入 TS。

**Q：既然 Codex 用 Rust 又快又省，那我是不是該直接用 Rust 寫 Agent？**

除非你做的是「性能關鍵、要長時間跑、要塞進 CI / edge / 單一 binary」的底層 runtime 或 CLI harness（像 Codex 那種），不然多數 Agent 產品的瓶頸根本不在 runtime 的記憶體，而在開發速度和跨前後端的整合——那 TS 還是比較划算。Rust 的甜蜜點是「底層、長跑、性能敏感」這一塊；AI 讓它變得比以前好寫，但它不是預設選項，是你確定卡在性能時才往下換的那張牌。

* * *

**參考來源：**

  * [TypeScript, Python, and the AI feedback loop changing software development — GitHub Octoverse](https://github.blog/news-insights/octoverse/typescript-python-and-the-ai-feedback-loop-changing-software-development/)
  * [TypeScript vs Python for AI Agents: A Decision Framework — Blaxel](https://blaxel.ai/blog/typescript-vs-python-ai-agents)
  * [The best open source frameworks for building AI agents in 2026 — Firecrawl](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks)
  * [Choosing an agent framework — Speakeasy](https://www.speakeasy.com/blog/ai-agent-framework-comparison)
  * [Another Rust Rewrite: OpenAI’s Codex CLI Goes Native, Drops Node and TypeScript for Rust — InfoQ](https://www.infoq.com/news/2025/06/codex-cli-rust-native-rewrite/)
  * [AI CLI Tools Comparison: Why OpenAI Switched to Rust While Claude Code Stays with TypeScript — Mervin Praison](https://mer.vin/2025/12/ai-cli-tools-comparison-why-openai-switched-to-rust-while-claude-code-stays-with-typescript/)

---

## [OpenAI 認 bug 重置全站額度、公開鼓勵用第三方 harness：Agent 訂閱戰正式攻守易勢](https://ai-coding.wiselychen.com/agent-subscription-attack-defense-swap-openai-anthropic/)
*🏢 Wisely Chen AI | 2026-05-27*

這週 OpenAI Codex 負責人 Tibo（[@thsottiaux](https://x.com/thsottiaux)）發了兩則 X 貼文，連在一起看，**等於 OpenAI 把這半年的訂閱戰態度直接攤在桌上** 。

第一則（5/23）：

> A little secret. About 5% of our production traffic is on the Pi harness, about another 5% is on OpenCode. Reminder you can use your ChatGPT account in a flourishing set of other tools.
> 
> We’ll continue to make Codex awesome, but you have options.

第二則（這週稍晚）：

> Some of you noticed limits drained faster in Codex, we root caused it to an optimization that we rolled back that had an impact on cache hit rates when compacting across long running sessions.
> 
> We fixed this and have now reset usage limits for all accounts. Enjoy the weekend.

兩則貼文加起來大概 400 個字，但濃度極高。對應到 Anthropic 5 月那波 [AFK 額度砍 96%](https://ai-coding.wiselychen.com/anthropic-afk-quota-cut-altman-codex-defection/)，**這就是攻守易勢的訊號** 。

## 兩家公司對 Agent 訂閱制的態度，已經完全相反

把這兩家近三個月的動作擺在一起：

動作 | Anthropic | OpenAI  
---|---|---  
第三方 harness 使用訂閱額度 | **4 月封殺 OpenClaw** | 5 月公開承認 10% 流量在 Pi harness + OpenCode，鼓勵繼續用  
額度爭議 | 5/14 切出 AFK credit，等於砍 96% | 認 bug、**全站額度重置** 、祝你週末愉快  
訊息口吻 | “Subscription is for human-in-the-loop” | “You have options”  
對外宣告場合 | Discord、Help Center FAQ | 負責人本人 X 直發  
  
這不是同一條商業哲學的微調，是**兩個截然不同的策略** 。

## 那 OpenClaw 的流量呢？

Tibo 點名 Pi harness 5%、OpenCode 5%，那 OpenClaw 呢？

**它沒有被 Tibo 單獨列成一個 5% bucket，原因未必是沒有流量，而更可能是統計口徑問題** 。

OpenClaw 是上層 agent client / platform，實際執行時底下可以走 Pi harness、Codex harness 或其他 runtime。OpenClaw 自家文件提到，如果沒指定或沒匹配到其他 harness，會 fallback 到 PI；Codex harness 文件也說 auto 模式可能仍以 PI 作為相容性 backend。

也就是說，**如果一個 OpenClaw session 底層跑的是 Pi，那在 OpenAI telemetry 裡自然會被歸到 Pi 那 5%，不是 OpenClaw** 。事實上，Tibo 那則貼文上面有人引用就提到「OpenCode, Pi, OpenClaw and more」，他自己只挑了 Pi 跟 OpenCode 報數字。

所以這裡正確的讀法不是「OpenClaw 已經沒人用」，而是——

**Tibo 這句話最重要的不是哪個 client 佔多少，是 OpenAI 願意公開承認第三方 harness / client 已經吃到實質 production traffic，而且沒有把這件事描述成「需要封堵的問題」** 。

這個對照才是攻守易勢的真正畫面：

| Anthropic 的對應行動 | OpenAI 的對應行動  
---|---|---  
第三方 client 用我的訂閱跑 agent | **封掉它** （OpenClaw 4 月案，我寫過[三層替代方案那篇](https://ai-coding.wiselychen.com/anthropic-kills-openclaw-gpt54-migration-guide/)） | **負責人本人 X 點名第三方 harness 佔 10% 流量，叫大家繼續用**  
用戶問「為什麼額度燒這麼快」 | 改 TOS，切出 AFK credit | 認 bug，重置全站  
語氣 | “Subscription is for human-in-the-loop” | “You have options”  
  
**同一個用戶行為，一邊定義成「abuse 要堵起來」，一邊定義成「生態繁榮的證據」** 。

決定性訊號不在誰的模型更強，而是**誰願意讓你拿你的帳號去做你想做的事** 。

Anthropic 的邏輯：訂閱賣給「人坐在螢幕前」的場景，AFK 跟批次自動化要丟回 API 按量收費——**鎖住生態、收斂 abuse、保護毛利** 。

OpenAI 的邏輯：訂閱是入口，**ChatGPT 帳號是憑證，harness 隨便你挑** 。Codex 自己只佔 90%，剩下 10% 給生態系。寧可流失到第三方工具，也不要讓你跳去 Anthropic。

## 為什麼是攻守易勢，不只是策略不同

去年到今年初，劇本是反過來的。Anthropic 出 Claude Code，定義了 harness engineering 這個品類，開發者大規模從 Cursor / Copilot 遷過去。OpenAI 那時候在守——Codex 重啟、ChatGPT Pro 漲到 $200、生態整合慢半拍。

現在反過來：

  * **OpenAI 在攻** ：Codex 砍價、企業版兩個月免費、公開承認 harness 生態、出 bug 直接重置額度
  * **Anthropic 在守** ：封殺第三方 client、切出 AFK credit、把訂閱定義收窄



「攻」的姿勢是「**你願意用我，我給你最大彈性** 」。「守」的姿勢是「**請按照我定義的方式用我** 」。

姿勢本身就是訊號。攻方的成本結構撐得住補貼，守方的單位經濟模型撐不住現在的 abuse 率。坦白講，我不覺得 Anthropic 是壞人，**那 96% 切的是真的有人在跑機房等級的 abuse** 。但用戶不看你內部帳，用戶看的是「我這個月還能不能跑」。

## Token 跟訂閱制的整體趨勢

把 Tibo 這兩則放回整個產業的脈絡看，2026 上半年的訂閱制大概是這個樣子：

**第一條線：訂閱費往上、額度往下，但分流給「真人使用」**

  * Claude Pro $20、Max 5x $100、Max 20x $200，**但 AFK 切出來獨立 credit**
  * ChatGPT Pro $100（從 $200 砍下來），Codex 額度大方
  * Cursor / Cody 大量出現「使用快超額」彈窗，靜默調整 model routing



訂閱還在，但**「無限暢用」這四個字已經死了** 。所有家都在切。

**第二條線：BYOK（Bring Your Own Key）大規模回潮**

OpenCode、Aider、Continue、Roo Code 這類 harness，2025 上半年大家還在比訂閱整合度，到了 2026 全部回頭做 BYOK 跟 multi-provider routing。原因很簡單——**訂閱條款隨時會改，BYOK 至少帳單透明** 。

Tibo 這則「you can use your ChatGPT account in a flourishing set of other tools」，本質上是 OpenAI 承認這個趨勢，**並且選邊站在 BYOK 這側** 。

**第三條線：token 報價持續下探，但「能跑多久」不再等於「token 多便宜」**

GPT-5.5、Claude 4.x、Gemini 3 的 token 單價都在往下走。但對 harness 用戶來說，**真正的成本不是單價，是上下文重算** 。Tibo 自爆的那個 bug 很關鍵——”impact on cache hit rates when compacting across long running sessions”——一個長 session 的 cache hit 率掉了，token 帳單翻倍跳。

這也是為什麼 Anthropic 切 AFK 切得這麼狠：**長期 background agent 是 cache miss 的重災區** ，按訂閱算撐不住。OpenAI 選擇用「修 bug + 重置額度」吸收掉，這背後是基建決策。

## 對 harness engineer 跟訂閱用戶的實際建議

第一，**雙棲不是選擇題，是必修課** 。Claude + Codex 同時養著，互動式留 Claude Code，AFK / batch 走 Codex 或直接 API。哪家改條款都有退路。我自己現在工作流就是這樣。

第二，**用 BYOK harness 把帳號變成「憑證」而非「綁定」** 。OpenCode、Roo Code、Aider 配 OpenRouter 這條路現在很成熟。Tibo 公開鼓勵這條路徑，**等於 OpenAI 自己背書** 。

第三，**地端評估不能再拖** 。不是要你今天就買 H100，而是 Qwen3.6 27B / Gemma 4 31B 這個量級的 dense 模型在 RTX 5090 上的實測，你應該心裡有個數字。地端不是省 token 費，是你願不願意把核心流程壓在「**隨時可能改的條款** 」上。

* * *

## 一句話總結

> Tibo 兩則貼文加 Anthropic 5/14 公告，攤開看是同一個故事的正反兩面——**Agent 訂閱戰的攻守已經易勢** ，OpenAI 在收用戶，Anthropic 在收 abuse。對開發者來說，這不是該選邊站的時候，**是該重新設計你 Agent Infra 的時候** 。

* * *

## 延伸閱讀

  * [Anthropic 把 AFK 額度砍 96%](https://ai-coding.wiselychen.com/anthropic-afk-quota-cut-altman-codex-defection/) — 這篇是同一條時間線的前半段
  * [Anthropic 封殺 OpenClaw 之後的三層替代方案](https://ai-coding.wiselychen.com/anthropic-kills-openclaw-gpt54-migration-guide/) — 4 月那波，鎖第三方 client 的開端
  * [Qwen 3.6 27B 在 RTX 5090 上的七種推論引擎 benchmark](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/) — 地端混搭的硬體基礎



## 常見問題 Q&A

**Q: 那 OpenClaw 為什麼沒出現在 Tibo 那份 10% 名單裡？**

很可能是**統計口徑問題，不是它沒有流量** 。OpenClaw 是上層 agent client / platform，底下可以走 Pi、Codex 或其他 harness，文件也提到沒指定時會 fallback 到 PI。如果 session 底層跑的是 Pi，在 OpenAI telemetry 就會被歸到 Pi 那 5%。Tibo 那則貼文的引用上下文也提到「OpenCode, Pi, OpenClaw and more」，他自己只挑了兩個明確 bucket 報數字。重點不是哪個 client 佔多少，是 OpenAI 願意公開承認第三方 harness 吃實質流量、而且沒當問題處理。

**Q: Pi harness 跟 OpenCode 是什麼？**

Pi 是第三方 agent runtime，OpenCode 是開源的 coding harness。兩者都支援用 ChatGPT 帳號（OAuth）登入。Tibo 講「10% production traffic」意思是 Codex 訂閱用戶有約 10% 不在用 OpenAI 自家的 Codex CLI / IDE。

**Q: OpenAI 真的不在意用戶流失到第三方嗎？**

短期不在意。對 OpenAI 來說，使用者留在 ChatGPT 帳號體系裡比留在自家 client 重要。Anthropic 反過來——它需要把使用者圈在 Claude Code 裡，才能控制 abuse。

**Q: 那 Anthropic 的策略是錯的嗎？**

不是錯，是處境不同。Anthropic 毛利結構更緊、算力供應更稀缺，沒有空間補貼第三方 harness 的 abuse。但**從用戶體感來說，攻方的姿勢就是比較好看** 。

**Q: 重置 usage limits 是什麼意思？真的全部歸零？**

對，所有帳號當月的 usage counter 歸零重算。對重度用戶來說等於白送一個月額度。換成 Anthropic，過去同類事件通常是發 credit 補償，量級也小很多。

**Q: 我應該現在就跳 Codex 嗎？**

不要為了情緒換工具。互動式寫程式 Claude Code 還是最順，AFK / 批次任務 Codex 比較划算。**雙棲，不是換邊** 。

---

## [Harness Engineering 才是勝負手：PwC 論文拆解 Grep 打贏 Vector RAG，換個 Harness 準確率差 17 個百分點](https://ai-coding.wiselychen.com/is-grep-all-you-need-pwc-agent-harness-reshapes-retrieval/)
*🏢 Wisely Chen AI | 2026-05-25*

**論文連結：** [arxiv.org/abs/2605.15184](https://arxiv.org/abs/2605.15184)

* * *

## 研究設計

PwC 的研究團隊（Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah）設計這個實驗的問題很明確：

**「在 Agent 的脈絡下，retrieval 方法的選擇到底還重不重要？」**

過去學界比較 grep vs vector 都是在「standalone retrieval」的設定下——給一個 query、看 top-k 結果。但 Agent 不是這樣用檢索的。Agent 會 reason、會重試、會把工具結果跟自己的 context 整合。所以 PwC 的假設是：**retrieval 方法的好壞，可能會被 Agent harness 的設計給放大或抵消** 。

### Dataset：LongMemEval

選用 **LongMemEval** 這個 benchmark，取 116 題樣本。任務形式是：

  * 給 Agent 一堆「過去的對話歷史」
  * 裡面混雜了大量無關內容（distractors）
  * Agent 要找出回答當前問題所需的具體事實



LongMemEval 的答案常常依賴明確的日期、數字、偏好、命名片段——這是論文後面討論結果時很重要的脈絡。

### 四個 Agent Harness

  * **Chronos** （作者群自製的客製 harness）
  * **Claude Code** （Anthropic 的 CLI）
  * **Codex** （OpenAI 的 CLI）
  * **Gemini CLI** （Google 的 CLI）



搭配不同 backbone 模型（Claude Opus 4.6、GPT-5.4、Gemini 3.1 Pro、Gemini 3.1 Flash-Lite）。

### 兩個對照變因

  * **檢索方法** ：grep（字面字串搜尋）vs vector retrieval（embedding-based）
  * **工具結果傳遞方式** ：inline（直接塞回對話）vs programmatic（寫成檔案讓模型自己讀）



## 實驗一：Inline 模式下，grep 全面壓制 vector

第一個實驗是「full haystack」——完整對話歷史餵進去、inline 回傳工具結果。

Harness + 模型 | Grep | Vector | 差距  
---|---|---|---  
Chronos + Claude Opus 4.6 | **93.1%** | 83.6% | +9.5  
Chronos + Gemini 3.1 Flash-Lite | **86.2%** | 62.9% | +23.3  
Claude Code + Claude Opus 4.6 | **76.7%** | 75.0% | +1.7  
Codex + GPT-5.4 | **93.1%** | 75.9% | +17.2  
Gemini CLI + Gemini 3.1 Pro | **81.9%** | 75.0% | +6.9  
  
**5 組對照，grep 全勝** 。最誇張的是 Chronos + Gemini Flash-Lite 那組，差 23.3 個百分點。

論文對這個結果的解釋是：

> “LongMemEval 的答案常常依賴精確的日期、數量、偏好、片段——這些在 tokenization 之後通常很穩定。Lexical tools 直接把這些字串撈出來，不用經過 embedding 這個瓶頸。”

換句話說：**vector embedding 是有損壓縮** 。當答案需要的是「Lucky」這個具體名字、「2025-03-14」這個具體日期，embedding 把這些細節糊掉了；grep 反而精準命中。

論文用了一個詞描述 LongMemEval 的答案結構：「literal witnesses」（字面證據）——答案要的是字面上一模一樣的證據，不是改寫後的語意。

## 真正的暴擊：Harness 換掉，準確率差 17 個百分點

如果故事到這裡就結束，那就只是「grep 比 vector 強」的廣告。真正讓這篇論文有重量的是這個發現：

**同樣是 Claude Opus 4.6，同樣是 grep：**

  * 在 **Chronos** 上跑：**93.1%**
  * 在 **Claude Code** 上跑：**76.7%**



差 16.4 個百分點。

模型相同、檢索方法相同、資料相同——唯一變的是外殼。論文裡有一句話很關鍵：

> “Table 1 裡的所謂 retrieval，其實是 retrieval-plus-orchestration。Harness 設計形塑了 prompting、tool description、result formatting。”

意思是：**你以為你在比較檢索方法，其實你在比較整個 Agent 框架** 。Harness 帶來的差距，可以跟換檢索方法一樣大。

這個發現顛覆了過去的研究習慣——大家做 retrieval 研究時，通常假設「retrieval 是獨立 component，可以單獨評估」。PwC 用數據直接證明：**在 Agent 時代，這個假設是錯的** 。

## 實驗二：Programmatic Delivery 是個陷阱

### 先解釋：什麼是 Programmatic Delivery？

論文裡比較了兩種「工具回傳結果的方式」：

**Inline delivery（直接塞回對話）**

Agent 呼叫工具 → 工具結果**直接 append 到對話歷史** ，模型下一輪就能看到全部內容。
    
    
    1
    2
    3
    4
    

| 
    
    
    [User]: 我家狗叫什麼名字？
    [Assistant]: 呼叫 grep("狗")
    [Tool result]: <直接貼出 grep 抓到的 50 行對話片段>
    [Assistant]: 你家狗叫 Lucky。
      
  
---|---  
`

優點：模型一眼看到所有內容、不用額外動作。 缺點：內容大時 context window 會爆。

**Programmatic delivery（檔案系統）**

Agent 呼叫工具 → 工具**把結果寫到一個檔案** ，只回傳「檔案路徑 + 摘要 metadata」。模型如果要看內容，要再主動發一次 `read_file` 呼叫。
    
    
    1
    2
    3
    4
    5
    6
    

| 
    
    
    [User]: 我家狗叫什麼名字？
    [Assistant]: 呼叫 grep("狗")
    [Tool result]: "結果存到 /tmp/grep_001.txt，共 50 行，前 3 行：..."
    [Assistant]: 呼叫 read_file("/tmp/grep_001.txt", lines=1-50)
    [Tool result]: <50 行內容>
    [Assistant]: 你家狗叫 Lucky。
      
  
---|---  
`

優點：context 不爆、可以選讀、結構乾淨。 缺點：**模型必須自己完成「讀檔 → 整合 → 必要時重試」這個 loop** ，弱模型撐不住就崩。

簡單比喻：**Inline 是服務生把菜直接端上桌；Programmatic 是服務生給你菜單編號，叫你自己去廚房窗口取** 。弱模型在「自己去取」這一步就會走丟。

### 實測結果

直覺上 programmatic 比較「工程乾淨」——把大量資料隔離在檔案系統、context 保持精簡。架構師很愛這種設計。但實測結果出乎意料：

> **Vector 在 10 組 harness-model 配對裡，有 5 組逆轉變成贏家。**
> 
> **最慘的是 Codex + GPT-5.4：inline grep 93.1%，換成 programmatic grep 直接掉到 55.2%。** （同條件下 vector 還有 67.2%）

從接近滿分跌到比 vector 還差，差距 37.9 個百分點。

論文的解釋很精準：

> “如果模型沒辦法完成『讀檔 → 整合 → 重試』這個循環，那檔案系統帶來的好處根本到不了答案層。便宜的檢索變成昂貴又不可靠的端到端流程。”

這個現象作者稱為「end-to-end brittleness」——單看 retrieval 這個 component 很漂亮，但接進完整 Agent loop 就崩。

## 實驗三：加干擾項的尺度測試

論文還測了「漸進加入無關對話」對準確率的影響。設定是從 s5（5 個 session）一路加到 full：

**Chronos + Claude Opus 4.6：**

  * Grep：89.3% → 90.5%（s20 峰值）→ 89.7%（full）
  * Vector：94.0% → 94.8%（s10 峰值）→ 92.2%（full）



**Claude Code + Claude Opus 4.6：**

  * Grep：91.4% → 95.7%（s20 峰值）→ 94.0%
  * Vector：77.6% → 72.4% → 72.4%



兩個觀察：

  1. **Grep 並非單調下降** ——加入更多干擾項時，準確率反而會先升後降。論文推測是因為更多歷史讓 Agent 能找到更多 disambiguation 線索。
  2. **Vector 在不同 harness 下的 peak 出現在不同 session 數** ——再次證明「同樣的 vector 檢索」在不同 harness 下表現會差很多。



論文的總結是：**grep 跟 vector 的交叉點，取決於 harness 跟 backbone，而不是單純的 corpus size** 。

## 論文的三個核心 takeaway

把整篇論文的論點濃縮一下：

### 1\. Lexical 在 Agent 場景被低估

過去大家假設「資料變多 → 需要 dense retrieval」。PwC 的數據顯示：當任務涉及 literal facts（日期、命名、ID、錯誤訊息），grep 在大 corpus 下依然有競爭力，甚至贏過 vector。

### 2\. Retrieval 不能脫離 Harness 評估

論文用「retrieval-plus-orchestration」這個詞，明確主張：**Agent 時代的 retrieval benchmark 必須把 harness 當成一級變因** 。只報「我的 retrieval 在 standalone 設定下達到 X%」是不夠的——換個 harness 結果可能完全不同。

### 3\. Programmatic Delivery 是雙面刃

把工具結果寫成檔案、讓模型分段讀，理論上可以管理 context 壓力。但這個方案的成功依賴模型穩定執行 read-integrate-retry 迴圈——較弱的模型撐不住，結果反而比 inline 還差。

## 論文的限制（誠實面對）

  * **Sample size 只有 116 題** 。趨勢可信，但個別數字不要當成精準預測。
  * **只測 LongMemEval 一個 benchmark** 。LongMemEval 的答案結構偏向 literal witnesses，這對 grep 有利。如果是「總結用戶過去三個月的偏好變化」這種 paraphrastic 任務，grep 就不會贏。
  * **沒測 hybrid retrieval** 。grep + vector 兩個都跑、再讓 LLM 選最佳結果的混合方案，論文沒涵蓋。
  * **Harness 差異的歸因不夠細** 。Chronos 跟 Claude Code 差 17 個百分點，但這 17 個百分點裡有多少來自 prompt template、多少來自 tool description、多少來自 result formatting，論文沒拆解。



## 一句話總結這篇論文

> “你以為你在量檢索效能，其實你在量整個 Agent pipeline 的乘積。”

PwC 這篇最大的貢獻不是「證明 grep 比 vector 強」——而是把過去 RAG 研究的隱性假設攤開：**retrieval 不是獨立 component，retrieval × harness × delivery format 才是 Agent 的真實效能** 。任何只比較其中一個維度的 benchmark，可能都在誤導決策。

* * *

## 論文資訊

  * **論文連結：** [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](https://arxiv.org/abs/2605.15184)
  * **作者：** Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah
  * **單位：** PricewaterhouseCoopers U.S.
  * **發表時間：** 2026 年 5 月

---
