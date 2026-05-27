---
title: "Wisely Chen AI — 2026-04-26"
date: 2026-04-26
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-04-26

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [Opus 4.7 「變笨」一個月之謎——Anthropic 終於承認：是 Claude Code 的 harness，不是模型](https://ai-coding.wiselychen.com/opus-4-7-claude-code-harness-postmortem/)
*🏢 Wisely Chen AI | 2026-04-24*

**作者：** Wisely Chen **日期：** 2026 年 4 月 **系列：** Claude Code 工程實戰觀察 **關鍵字：** Claude Code, Opus 4.7, Agent SDK, Harness, Post-mortem, Regression

* * *

## 事情是這樣的

過去一個月，Claude Code 社群的抱怨從小聲嘀咕變成全網哀嚎：

> 「Opus 4.7 最近明顯變笨了，有點不對勁。」

然後 4/24 凌晨，[@ClaudeDevs 官方帳號](https://x.com/ClaudeDevs/status/2047371123185287223)發了這串推：

> Over the past month, some of you reported Claude Code’s quality had slipped. We investigated, and published a post-mortem on the three issues we found. All are fixed in v2.1.116+ and we’ve reset usage limits for all subscribers.

翻譯：**你們抱怨是對的，不是幻覺，是我們家裡三個 bug 疊在一起。**

底下一則回覆把整個氣氛講完了：

> sui ☄️ @birdabo：not now bro.

這篇想拆的不是「踢 Anthropic 一腳」——事實上他們發 post-mortem 這件事本身值得給個掌聲。要拆的是：**這三個 bug 到底是什麼？為什麼一個月才抓到？我們以後要怎麼自保？**

* * *

## 先講最重要的結論：模型沒退化，是 harness 退化

Anthropic 在 post-mortem 裡講得很清楚：

> The issues stemmed from Claude Code and the Agent SDK harness, which also impacted Cowork since it runs on the SDK. The models themselves didn’t regress, and the Claude API was not affected.

這句話拆開來看，其實是一個很重要的架構提醒：

  * **模型層（Opus 4.7 本體）** ：沒變笨
  * **API 層（claude.ai/api）** ：沒受影響
  * **Harness 層（Claude Code / Agent SDK / Cowork）** ：三個 bug 疊在這層



所以如果你是直接打 API 的人，這一個月你什麼都沒感覺到。但你如果是用 Claude Code 或 Cursor 掛 Sonnet/Opus，你感覺到的「變笨」是真的，只是笨的不是模型，是那個包住模型的殼。

**這個區分很重要** ，因為它直接決定你以後該怎麼 debug「我的 Claude 最近怎麼怪怪的」這種問題——先想 harness，再想模型。

* * *

## 三個 bug，三種退化

Post-mortem 裡的三個問題其實彼此獨立，但不幸地都在三月到四月之間依序發生，疊成社群感受到的「整體變笨」。

### Bug 1：Reasoning effort 默認從 high 偷偷降到 medium（3/4）

3/4 那天，Claude Code 的默認 reasoning effort 從 `high` 降到 `medium`。

動機：簡單任務 UI freeze 太久，使用者抱怨慢。

副作用：複雜任務的推理深度跟著掉一截。**簡單任務變快，複雜任務變爛。**

使用者感受：「明明之前可以一次解完的 refactor，現在要手把手拉它三次。」

4/7 回復成 high。

### Bug 2：Idle session thinking 清理 bug（3/26）

這個最陰，也是我覺得最值得架構層面反思的一個。

**原本的設計** ：如果一個 session 閒置超過 1 小時，就把累積的 thinking state 清掉一次，避免陳舊上下文污染新對話。

**實際發生的事** ：那個「閒置一次才清」的條件判斷寫錯了，變成**每個 turn 都在清** 。

結果：Claude 每講一句話，都要把前面想過的東西重新想一遍。

使用者感受：「它怎麼老是忘記我剛剛講過的？它怎麼老是重複問一樣的問題？」

**這就是 harness 層 bug 的可怕之處** ——它不會讓模型講錯答案，它讓模型變成一個失憶症患者。從外部看，你只會覺得「模型好像退化了」，你不會懷疑是快取邏輯壞了。

4/10 在 v2.1.101 修掉。

### Bug 3：Verbosity system prompt 的反噬（4/16）

這是第三刀，也是讓很多人直接炸鍋的那一刀。

4/16 Anthropic 在 Claude Code 的 system prompt 裡加了一段硬限制：

> 「工具呼叫之間 ≤25 字，最終回應 ≤100 字。」

動機：壓一下 Opus 4.7 的話癆傾向——這個模型話真的超多，之前很多使用者抱怨它寫 code 前會先講一長串廢話。

副作用：**coding eval 掉 3%** 。

為什麼？因為 Opus 4.7 的思考模式是「邊講邊推理」，你硬把它的 output 壓到 100 字，它推理的中間步驟就沒空間展開了。字數限制剪掉的不只是廢話，還包括必要的 chain-of-thought。

4/20 reverted，併入 v2.1.116。

* * *

## 最諷刺的一句承認

Post-mortem 裡最該被引用的不是技術細節，是這句：

> 「While we began investigating reports in early March, they were challenging to distinguish from normal variation in user feedback at first.」
> 
> （我們三月初就開始查了，但一開始很難跟「正常的使用者回饋雜訊」區分。）

翻成人話就是：**我們看到抱怨，但我們分不清這次的抱怨是真退化，還是又一批「模型好像變笨了」的玄學感受。**

這句話之所以扎心，是因為它承認了一個結構性問題：**LLM 產品的品質監控，目前沒有一個乾淨的訊號。** 社群抱怨的 baseline 永遠是滿的——每次新版本、每次 system prompt 微調、每次使用者心情不好，都會有一波「最近變笨了」的 post。Anthropic 的內部 eval 也不夠細，抓不到這種 3% 等級的 regression。

所以他們後來發了這段：

> We’re making changes to catch these types of issues earlier, including more internal dogfooding with configs that exactly match those of our users and creating a broader set of evals and running them against isolated system prompt changes.

翻譯：**以後我們會用跟使用者一模一樣的 config 自己吃自己的狗糧，也會對每一次 system prompt 變動跑更細的 eval。**

這句話的潛台詞是——**他們之前沒這樣做。** 內部 dogfooding 的 config 跟使用者不一樣，system prompt 變動沒有 isolation eval。三個 bug 同時在生產環境疊到爆，才被抓出來。

* * *

## 但也有陰謀論的版本——而且不是完全沒道理

事情講到這裡，網路上同時在跑另一個解讀，我覺得該放進來討論。

陰謀論版本是這樣的：

> **API 是按 token 原價計費的，MAX 方案是吃到飽的。所以 Anthropic 有動機偷偷降智 MAX 客戶，讓重度使用者的每次呼叫少燒一點算力——降低邊際成本，又不容易被單獨一個使用者抓到。**

這個版本之所以有市場，不是因為使用者愛陰謀論，是因為**Anthropic 之前確實被抓包過類似的事** 。

4/9 的時候，GitHub 使用者 EmpireJones 開了 [issue #45381](https://github.com/anthropics/claude-code/issues/45381) 報告：**當你用`DISABLE_TELEMETRY=1` 關掉遙測，Claude Code 的 prompt cache TTL 會從 1 小時降回 5 分鐘。** 換句話說——你越保護隱私，cache 命中率越低，每次呼叫越貴、越慢。社群當時就炸鍋了，說這是「隱私懲罰」。詳細技術拆解我之前寫過：[關掉 Claude Code 遙測，效能就被懲罰？——一場隱私 vs 快取的技術鑑識](https://ai-coding.wiselychen.com/claude-code-telemetry-cache-gate-privacy-vs-performance/)。

那次的結論是——**雖然不是故意懲罰，但確實是 Anthropic 的商業優化無意中把隱私使用者放進了次等艙。**

所以這次 MAX 降智的陰謀論，放在那個脈絡下看，不是無的放矢：**Anthropic 確實有一個模式——官方說法是「工程決策」，但每次的工程決策剛好都是朝「對營收最有利」的方向做。**

### 我自己的判斷：這次不是陰謀，但結構性動機存在

先講結論：**我傾向相信這三個 bug 是真的 bug，不是刻意降智。** 理由有三：

  1. **Bug 2（thinking clear bug）跟商業沒關係** ——這個 bug 讓 Claude 變健忘重複，只會讓使用者更快燒掉額度、更頻繁叫用。如果 Anthropic 真想省成本，這個 bug 的方向是反的。
  2. **Bug 3（verbosity 限制）真的被 eval 抓到 3% 下滑** ——post-mortem 裡有具體數字，而且是他們自己主動揭露的。要造假造這麼細節不划算。
  3. **API 沒受影響這件事本身就是反證** ——如果是刻意降智，最合理的做法是 API 和 Claude Code 一起降（省更多成本），而不是只降其中一個。



**但陰謀論的存在本身值得警惕** ——它告訴你社群對 Anthropic 的信任餘額已經不多了。而且這個焦慮不是憑空來的，是整個 AI coding 訂閱市場的大勢：**token 越來越貴，吃到飽方案越來越撐不住。**

### 中國這邊更直接：一個漲、一個砍

就在 Anthropic 被社群懷疑偷偷降智 MAX 客戶的同時，中國的 AI coding 訂閱市場也在收緊，而且手段更直接：

  * **智譜 GLM Coding Plan（2026/2/12）** ：直接漲價 30%。Lite 版從 20 元/月漲到 26 元起，Pro 版漲到 130 元起，**同時取消首購優惠** 。官方說法是「成本上升與需求驅動」，但社群普遍解讀為——跑不動吃到飽經濟學了。
  * **阿里雲百煉 Qwen Code Coding Plan Lite（2026/3/20）** ：直接砍方案。3/20 停止新購，4/13 停止續費與升級。老用戶用完當期就沒了，沒有替代方案（Pro 價格更貴）。



一個漲價、一個砍方案，動作不一樣但訊號一樣：**「無限 token 換固定月費」這個商業模式，2026 年開始普遍跑不動了。** 2024-2025 搶市佔的低價方案，正在被廠商一個個收回去。

### 把這兩件事放在一起看

Anthropic 這次三個 bug 發生的時間點——3/4、3/26、4/16——剛好卡在整個 AI coding 訂閱市場開始收緊的時間窗。智譜 2/12 漲價、阿里 3/20 砍 Lite，Anthropic 3/4 把 reasoning effort 從 high 降到 medium。**這不一定是陰謀，但這是趨勢。**

訂閱制吃到飽 AI coding 的甜蜜期正在結束。早期廠商用燒錢衝用戶數的模式（DeepSeek、GLM、Qwen、Claude MAX 都走過這條路）正在撞上真實的 inference 成本牆。接下來你會看到三種調整反覆出現：

  1. **漲價** （智譜這條路）——誠實但得罪人
  2. **砍低階方案** （阿里這條路）——把重度使用者逼到 Pro 以上
  3. **悄悄降品質** （Anthropic 這次被懷疑的路）——最不得罪人，但最傷信任



**所以就算這次真的是純技術 bug，下次還會有人懷疑** ——因為大環境的趨勢就是「token 越來越貴，廠商一定要從某個地方把成本收回來」。而只要廠商不公開 cache 策略、不公開 system prompt 變動、不公開 routing 邏輯，每一次效能波動都會被解讀成「又在偷偷降智」。這不是使用者偏執，是結構性問題。

對使用者來說，這個趨勢的意涵很清楚——**你現在付的 MAX 月費，可能是 AI coding 歷史上最便宜的一段時間。** 要嘛接受未來會漲價，要嘛開始認真評估本地模型（Qwen 3.6 Plus 已經到可用水準），要嘛自己做 eval 抓廠商的小動作。三條路都可以走，但閉著眼睛吃到飽的日子，大概是結束了。

* * *

## 常見問題 Q&A

**Q: 所以我這一個月感覺 Claude Code 變笨不是錯覺？**

不是錯覺，是真的退化了。三個 bug 加起來，對複雜 coding 任務的影響可能有 5-10% 的品質下滑（取決於你踩到哪幾個）。最痛的是 Bug 2（thinking clear bug），這個不會讓輸出直接錯，而是讓 Claude 變得健忘重複，感受上像是模型「人格」整個變鈍了。如果你最近放棄了某個原本用 Claude Code 做得動的任務，升到 v2.1.116+ 之後可以重試一次，八成會回來。

**Q: 為什麼模型本身沒退化，但感覺這麼明顯？**

因為現在你用的「Claude」其實是一整條 pipeline：模型本體 → system prompt → harness 層（負責 tool use、thinking state、context 管理）→ UI。**你感受到的「Claude」是這整條鏈的綜合表現，不是模型孤立的能力。** 任何一環出問題，你的體感就是「Claude 變笨了」。這次三個 bug 全在 harness 層，但對使用者來說，感受跟「模型退化」是一模一樣的——這就是 Anthropic 難以 debug 的根源，也是使用者分不清源頭的根源。

**Q: 所以以後每次 Claude Code 更新我都要提心吊膽？**

不用提心吊膽，但要養成三個習慣。第一，**看 release note 再更新** ——Anthropic 現在會更仔細寫 harness 變更了。第二，**pin 一個你驗證過的版本** ，不要開自動更新然後閉眼用。第三，**準備一組你自己的 eval** ——5 到 10 個日常任務就夠了，每次升級跑一遍。這是最便宜的保險，花你 30 分鐘，可能省你一個月的時間。這次事件之後我會把這三件事當作 Claude Code 的**標準作業流程** ，不是可選項。

**Q: 那 Cursor、Codeium、其他包 Claude 的工具是不是也中招？**

不是所有都中，但邏輯上你要擔心。Anthropic 的 post-mortem 明確說 Cowork 因為跑在 Agent SDK 上所以也中了——這代表**任何使用 Anthropic 官方 SDK 的第三方工具，都可能被 harness 層的 bug 波及** 。但如果某個工具是自己手刻 API 呼叫、自己管 thinking state，那就不會中這三個 bug。結論：**不知道你用的工具底層是直打 API 還是走 SDK，就當作有中機率。** 自己做 eval，從來都不會錯。

* * *

## 延伸閱讀

  * [關掉 Claude Code 遙測，效能就被懲罰？——一場隱私 vs 快取的技術鑑識](https://ai-coding.wiselychen.com/claude-code-telemetry-cache-gate-privacy-vs-performance/) — 上次 Anthropic 被抓包的「Cache Gate」事件
  * [Claude Code 三個月 630k 行代碼實戰反思](https://ai-coding.wiselychen.com/claude-code-630k-lines-three-months-reflection/) — 為什麼日常 eval 是必要的
  * [Claude Code System Prompt 源碼分析](https://ai-coding.wiselychen.com/claude-code-system-prompt-source-code-analysis/) — system prompt 怎麼影響輸出
  * [Claude Code Context Engineering 四層壓縮](https://ai-coding.wiselychen.com/claude-code-context-engineering-four-layer-compression/) — harness 層在做什麼
  * [Anthropic 雙 Agent 架構解讀](https://ai-coding.wiselychen.com/anthropic-dual-agent-architecture-claude-code/) — Claude Code 底層架構總覽



* * *

## 資料來源

  * Anthropic Engineering Blog（2026-04-23）：An update on recent Claude Code quality reports — https://www.anthropic.com/engineering/april-23-postmortem
  * @ClaudeDevs 官方 X 帳號（2026-04-24）：post-mortem 公告 thread
  * VentureBeat（2026-04-23）：Mystery solved - Anthropic reveals changes to Claude’s harnesses and operating instructions likely caused degradation
  * TrendForce（2026-02-16）：Rising Costs and Demand Drive China’s LLM Price Jump: Zhipu GLM-5 Hikes 30% in First 2026 Increase
  * 阿里雲百煉 Coding Plan 官方公告（2026-03）：Lite 套餐停售與停止續費時程

---

## [Qwen 3.6-27B 本地部署：DGX Spark / Mac mini 跑出 Sonnet 4.6 等級 AI Agent](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/)
*🏢 Wisely Chen AI | 2026-04-23*

## 目錄

  * [TL;DR](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#tldr)
  * [為什麼這又是一篇「無聊 IT 架構」文](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#為什麼這又是一篇無聊-it-架構文)
  * [第一段：為什麼是 Qwen 3.6-27B？](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#第一段為什麼是現在為什麼是-qwen-3-6-27b)
  * [第二段：Qwen 3.6-27B 的 Benchmark 贏過 Opus 4.5](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#第二段qwen-3-6-27b-的-benchmark-結果居然贏過-opus-4-5)
  * [第三段：網友用什麼機器跑？Token Performance 多少？](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#第三段網友用什麼機器跑起來token-performance-是多少)
  * [這對企業 IT 架構師意味著什麼](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#這對企業-it-架構師意味著什麼)
  * [常見問題 Q&A](https://ai-coding.wiselychen.com/qwen-3-6-27b-sonnet-level-home-inference/#常見問題-qa)



## TL;DR

  * **Qwen 3.6-27B（dense, Apache 2.0）** 在 12 項 Benchmark 上贏 Claude Opus 4.5 七項、平手一項，SWE-bench / Terminal-Bench 落在 **Sonnet 4.6 等級**
  * 一位網友在 NVIDIA **DGX Spark（$4,699, 49W 功耗）** 跑出 136 tokens/sec，10 agents 並行峰值 209 t/s
  * **「Sonnet 4.6 等級的 AI coding agent」不再需要雲端 API** ——可以跑在辦公桌下那台比微波爐小的機器
  * IT 架構師該做的事：**重新算一次 on-prem AI Coding ROI，6 個月前的假設已經過時**



* * *

## 為什麼這又是一篇「無聊 IT 架構」文

又一篇「無聊 IT 架構」系列文。

過去這一年大家討論 local LLM 都在講 performance——跑什麼模型、用什麼量化、GPU 要買哪張。但對企業 IT 架構來講，真正要問的只有一個問題：

**「local 到底夠不夠取代 Anthropic / OpenAI 的 API？」**

這個問題過去的答案是「還差得遠」。6 個月前你跟 CTO 說「我們來 on-prem 跑 Claude Code 的工作負載」，他會笑你——本地模型品質差商業 API 一個世代，工程師根本不會願意用。

但 2026 年 4 月 22 日 Qwen 團隊丟出 **Qwen 3.6-27B** 的那一刻，這個答案變了。

這篇文章不是在炫耀 benchmark，是要回答 IT 架構師真正關心的事：

  1. **Benchmark 上，Qwen 3.6-27B 到底是什麼等級？** 答：Sonnet 4.6 等級，不是比喻，是數字字面上的事實
  2. **跑得起來嗎？要什麼硬體？** 答：$4,699 的 NVIDIA DGX Spark，放辦公桌下，49W 功耗比一顆 LED 燈泡多一點
  3. **那我原本的 on-prem AI Coding 架構藍圖，還對嗎？** 答：不對，該重畫了



* * *

## 第一段｜為什麼是現在？為什麼是 Qwen 3.6-27B？

先把幾個名詞講清楚，因為這些東西過去 6 個月都在快速演進。

### Qwen 3.6-27B 是什麼

**Qwen 3.6-27B** 是阿里雲 Qwen 團隊在 2026 年 4 月發布的新一代開源模型：

  * **架構：** Dense（不是 MoE），27B 參數全部 active
  * **Context：** 原生 262,144 tokens，可延伸到 1M（YaRN）
  * **量化：** 官方提供 FP8 版本（約 27GB VRAM），另有 54 個社群量化版本（llama.cpp、LM Studio、Ollama 等）
  * **License：** Apache 2.0（商用無限制）
  * **能力：** 除了文字，還支援 vision（多模態），原生支援 tool calling



這個架構選擇本身就是一個訊號。

2025 年開源圈集體轉向 MoE 的時候，Qwen 3.5 自己也出了 397B-A17B 的 MoE 旗艦。但到了 3.6 世代，他們把**最強的 agentic coding 能力放回 27B dense** 。為什麼？

因為 dense 27B 剛好是「一張消費級顯卡 / 一台工作站」能跑的 sweet spot。MoE 雖然 active parameter 少，但總參數大，VRAM 需求反而高。27B dense FP8 只要 27GB VRAM——DGX Spark 的 128GB 統一記憶體綽綽有餘，一張 RTX 5090（32GB）也塞得進去。

**Qwen 團隊的 bet 很明確：agentic coding 的戰場在 on-device，不在 cloud。**

### 為什麼我說「這個時間點有意義」

把過去 18 個月的里程碑排一下：

時間 | 事件 | 意義  
---|---|---  
2024 Q4 | Local LLM 僅限 demo 用途 | 品質距商業 API 一個世代  
2025 Q1 | Qwen 3.5-27B 讓本地 tool calling 可用 | 第一次有 local 能 production  
2025 Q3 | Claude Opus 4.5 發表 | Anthropic 旗艦，當時 state-of-the-art  
2025 Q4 | Mac Studio M3 Ultra 可跑 70B 模型 | 消費級硬體追上  
**2026 Q2（現在）** | **Qwen 3.6-27B 家用機跑出 Sonnet 4.6 等級** | **On-prem ROI 假設全部要重算**  
  
Chris Maddern 在 X 上的觀察很精準：

> “Opus 4.5 was released 5 months ago, the gap is closing. Opus 4.5 was the breakthrough moment for ‘good enough to stop writing code’… real local coding inference is coming.”
> 
> （Opus 4.5 是 5 個月前發表的。差距正在縮小。Opus 4.5 是「好到可以停止手寫 code」的突破時刻。真正的 local coding inference 要來了。）

**過去我們說「6 個月前沿差距」** ——開源模型通常落後商業模型大約半年。現在這個差距壓縮到了**一個季度** ，某些領域甚至**打平** 。

對企業 IT 來講，這不是技術趣聞，是架構決策的輸入條件變了。

* * *

## 第二段｜Qwen 3.6-27B 的 Benchmark 結果，居然贏過 Opus 4.5

Qwen 團隊公布的官方 benchmark 有 12 項。要比的對手是誰？

  * **Qwen 3.5-27B** （上一代 dense）
  * **Gemma4-31B** （Google dense 對標）
  * **Qwen 3.6-35B-A3B** （自家 MoE 對照）
  * **Qwen 3.5-397B-A17B** （上一代旗艦 MoE）
  * **Claude 4.5 Opus** （Anthropic 當時的旗艦）



直接看結果。

### 完整 Benchmark 對比表

Benchmark | 類別 | Qwen 3.6-27B | Qwen 3.5-397B-A17B | Claude 4.5 Opus | 誰贏？  
---|---|---|---|---|---  
**Terminal-Bench 2.0** | Agentic Terminal | **59.3** | 52.5 | 59.3 | 平手 Opus  
**SWE-bench Pro** | Agentic Coding | 53.5 | 50.9 | **57.1** | Opus  
**SWE-bench Verified** | Agentic Coding | 77.2 | 76.2 | **80.9** | Opus  
**SWE-bench Multilingual** | Multilingual Coding | 71.3 | 69.3 | **77.5** | Opus  
**QwenClawBench** | Real-World Agent | **53.4** | 51.8 | 52.3 | **Qwen**  
**QwenWebBench (Elo)** | Artifacts | 1487 | 1186 | **1536** | Opus  
**NL2Repo** | Long-Horizon Coding | 36.2 | 32.2 | **43.2** | Opus  
**SkillsBench** | Agent Skills | **48.2** | 30.0 | 45.3 | **Qwen**  
**Claw-Eval (pass^3)** | Real-World Agent | **60.6** | 48.1 | 59.6 | **Qwen**  
**GPQA Diamond** | Graduate Reasoning | **87.8** | 88.4 | 87.0 | **Qwen (微)**  
**MMMU** | Multimodal Reasoning | **82.9** | 85.0 | 80.7 | **Qwen**  
**RealWorldQA** | Image Reasoning | **84.1** | 83.9 | 77.0 | **Qwen**  
  
**計分：Qwen 3.6-27B 贏 7 項、平手 1 項、輸 4 項 Claude 4.5 Opus。**

一顆開源 27B dense 模型，在 12 項官方 benchmark 中打贏 Anthropic 5 個月前的旗艦七項。

### 讀得出什麼故事？

先看 Qwen 3.6-27B **輸** 的 4 項：

  * SWE-bench Pro：53.5 vs 57.1（差 3.6 分）
  * SWE-bench Verified：77.2 vs 80.9（差 3.7 分）
  * SWE-bench Multilingual：71.3 vs 77.5（差 6.2 分）
  * NL2Repo：36.2 vs 43.2（差 7.0 分）



**輸的全在純 coding 和 long-horizon repo reasoning。** 這不意外——Opus 4.5 是針對寫 code 優化的旗艦。差距最大的 NL2Repo（長跨度 repo 理解）是 Opus 最有優勢的場景。

再看 Qwen 3.6-27B **贏** 的 7 項：

  * QwenClawBench（real-world agent 任務）：53.4 vs 52.3
  * SkillsBench（agent skills）：48.2 vs 45.3
  * Claw-Eval（real-world agent pass^3）：60.6 vs 59.6
  * GPQA Diamond（研究生級推理）：87.8 vs 87.0
  * MMMU（多模態推理）：82.9 vs 80.7
  * RealWorldQA（圖像推理）：84.1 vs 77.0（+7.1 分）



**贏的是 real-world agent、agent skills、reasoning、multimodal。**

這一組剛好是 AI coding **agent** 真正需要的能力——不是一次性寫完一個 PR，是**長時間跑、能用工具、能看螢幕、能推理** 的那種工作負載。

### 跟 Sonnet 4.6 對比，才是文章標題的來源

Opus 4.5 是 2025 年 11 月的旗艦，對多數企業 AI coding 工作負載來講已經過度規格。2026 年 Q1 Anthropic 發表了 **Claude Sonnet 4.6** ——這才是現在大多數 Claude Code 日常工作跑的模型。

看對照：

Benchmark | Qwen 3.6-27B | Claude Sonnet 4.6 | 差距  
---|---|---|---  
**SWE-bench Verified** | 77.2 | 79.6 | Sonnet +2.4  
**Terminal-Bench 2.0** | **59.3** | 59.1 | **Qwen +0.2**  
  
不是比喻，是字面上的事實：

  * **Terminal-Bench 2.0：Qwen 3.6-27B 微幅高於 Sonnet 4.6。**
  * **SWE-bench Verified：落後 Sonnet 4.6 只有 2.4 分——在統計誤差邊緣。**



Sonnet 4.6 的 API 價格是 $3 / $15 per million tokens（input / output）。一位重度 AI coding 工程師日均 5M input + 1M output tokens，**每天刷 $30，一年 $7,500** 。

這個錢，現在可以不刷。

* * *

## 第三段｜網友用什麼機器跑起來？Token Performance 是多少？

Benchmark 贏 Opus 4.5 只是故事的一半。另一半——也是企業 IT 真正關心的——是**這東西跑得起來嗎？要什麼硬體？**

### 核心數據來自這條推文

2026 年 4 月 22 日，推特用戶 [Mitko Vasilev（@iotcoi）貼出一張終端機截圖](https://x.com/iotcoi/status/2046950805568164168)：

> “Qwen3.6-27B-FP8 + Dflash + DDTree, 256k context, 10 agents ~200 tokens/sec max decode **136 t/s average on a single tiny GB10 GPU at 49W power** ”

另一位用戶 LotusDecoder 接力引用並補一句：

> “香啊，家用小型台式机，推理 qwen-3.6-27B-fp8 达到 136 tokens/sec。 性能估计是可以接近 haiku-4.5 吧。”

（實際上低估了，是 Sonnet 4.6 等級。）

這三個硬體 + 軟體元件值得拆開來看。

### 硬體：NVIDIA DGX Spark / GB10

**NVIDIA DGX Spark** 是 NVIDIA 2026 年推出的「家用 AI 工作站」。規格如下：

項目 | 規格  
---|---  
SoC | NVIDIA GB10 Grace Blackwell Superchip  
CPU | 20 核 ARM（10 × Cortex-X925 @ 4GHz + 10 × Cortex-A725 @ 2.8GHz）  
GPU | 6,144 CUDA cores, Blackwell 架構  
記憶體 | **128GB LPDDR5X 統一記憶體**  
儲存 | 4TB NVMe SSD  
網路 | ConnectX 200 Gbps（兩台 Spark 可互聯跑 405B 模型）  
FP4 效能 | 1 petaFLOP  
**售價** | **$4,699 USD（約 15 萬台幣）**  
形式 | 桌上型，比 Mac Studio 略小  
  
關鍵是那顆 **GB10 Superchip** 的統一記憶體——128GB 全部可以給 GPU 用。Qwen 3.6-27B FP8 只吃 27GB，剩下 100GB 可以開超大 KV cache 跑長 context、或同時載入多個模型切換。

這個硬體定位很明確：**不是要取代資料中心的 H100，是要取代工程師桌上的 MacBook Pro。** 每個 AI coding 工程師配一台，放辦公桌下，自己的 agent 自己跑。

### 軟體：Dflash + DDTree 是什麼？

Mitko 的推文提到 `Dflash + DDTree`——這是推理加速的關鍵。

  * **DFlash** ：Block Diffusion Flash Speculative Decoding。簡單講，用一個小的 draft model 一次「預測」一整個 block 的候選 tokens，然後目標模型在單次 forward pass 中驗證。來自 z-lab 的開源專案。
  * **DDTree** ：DFlash 的改進版，把候選 tokens 組成一棵樹狀結構，在同一個 draft pass 裡產出多條候選路徑，驗證時只選最佳。論文實測在 Qwen3-8B 上，HumanEval 從 4.84× 加速到 6.90×，GSM8K 從 4.78× 到 6.75×。



這兩個技術的意義：**不用換硬體，單純靠軟體優化就能在同一張 GPU 上把 token 吞吐拉高 6-8 倍。**

Mitko 的 136 t/s 就是這樣來的——沒有 DFlash + DDTree，同樣硬體大約只有 20-30 t/s 的水準。

### 吞吐量到底夠不夠用？

136 t/s 在 10 agents 並行的設定下分配，等於每個 agent 約 **20 t/s** 。

這個數字對比幾個參考點：

場景 | 吞吐量 | 感受  
---|---|---  
人類閱讀速度 | ~5 t/s | 慢到讀得完  
Claude API Sonnet 4.6（典型） | ~50-80 t/s | 快但常被 rate limit  
**Mitko 的 DGX Spark（每 agent）** | **~20 t/s** | **比閱讀快 4x**  
**Mitko 的 DGX Spark（全機峰值）** | **209 t/s** | **10 agents 並行才壓得到**  
  
換句話說，**單個 agent 20 t/s 稍慢於 Claude API** ，但 10 agents 可以**同時跑** 且**不受 rate limit** ——對於 autonomous agent workflow、subagent、cron-driven background task 這類負載，**總吞吐量反而勝過 API** 。

### 功耗：49W 的意義

49W 是什麼概念？

  * 一顆 LED 燈泡：約 10W
  * MacBook Pro 全速跑：約 100W
  * **DGX Spark 跑 Qwen 3.6-27B agent 負載：49W**
  * RTX 4090 單卡跑 LLM：約 400W
  * A100 伺服器：約 400-700W



一年 8 小時工作日 × 250 天 × 49W = **98 kWh/year** ，按台電工業電費約 **NT$ 300/year** 。

這個數字低到進不了任何成本模型——跟 API 每年 $7,500 的差距比起來，電費是四捨五入誤差。

### 成本結構對照

把單人成本算清楚：

方案 | Year 1 | Year 2 | Year 3 | 3 年總 TCO  
---|---|---|---|---  
**Claude Sonnet 4.6 API** | $7,500 | $7,500 | $7,500 | **$22,500**  
**DGX Spark + Qwen 3.6-27B** | $4,699 + $10 電 | $10 | $10 | **$4,729**  
  
**單人 3 年 TCO 差距：$17,771（約 55 萬台幣）。**

放大到團隊：

  * 10 人 AI coding 團隊：3 年省 $177,710（約 550 萬台幣）
  * 100 人團隊：3 年省 $1,777,100（約 5,500 萬台幣）



但這些數字不是文章的重點。**真正的重點是：**

  1. **資料不出公司** ——所有 code、所有 prompt、所有輸出都在公司網內，金融、醫療、國防、法務部門終於能用 AI coding
  2. **不受 API rate limit** ——autonomous agent 要跑就跑，不用排隊
  3. **不依賴單一供應商** ——Anthropic 明天漲價 3 倍，你也不痛



* * *

## 這對企業 IT 架構師意味著什麼

如果你是 CTO / VP of Engineering / IT 架構負責人，這篇文章真正要你做的事是：

### 三個檢查點

  1. **6 個月前你拒絕 on-prem AI coding 的理由是什麼？**
     * 「模型品質差商業 API 一個世代」？→ 現在差不到一個季度，甚至某些指標打平
     * 「硬體太貴，投資回收期太長」？→ 單台 $4,699，3 年 ROI 76%
     * 「工程師不會想用」？→ Sonnet 4.6 等級他們會想用，差的是工具鏈不是品質
  2. **這些理由在 2026 年 4 月還成立嗎？**
     * 如果「不成立」的項目超過 2 個，你的架構假設過期了
  3. **Pilot 成本是多少？**
     * 一台 DGX Spark：$4,699
     * 一個工程師週末的時間：裝 Qwen 3.6-27B、接上 Claude Code 或 aider、跑一週看看
     * 總投入 < $6,000，低於多數企業 IT 的「不用跑審批」門檻



### 但也要誠實講 Caveat

這不是吹開源 model 的宣傳文。幾個 caveat 一定要講：

  * **純寫 code 的頂尖品質，Opus 4.5 / Opus 4.6 仍勝** 。SWE-bench Pro 差 3.6 分、NL2Repo 差 7 分——關鍵 task 仍該 fallback 商業 API
  * **Qwen 是中國團隊開源** 。Apache 2.0 license 沒問題，但特定合規情境（政府、國防、某些金融產品）仍會被法務擋
  * **Dflash + DDTree 不是主流推理棧** 。vLLM / TGI 還在追 block diffusion speculative decoding 的整合，生產環境有工程學習成本
  * **136 t/s 是最佳配置** 。換一組 prompt、換一種 quantization，跑出來可能只有 80 t/s——需要實測
  * **官方 benchmark 有行銷成分** 。Qwen 自己公布的數字，不等於你的 workload 上的真實表現



但即使把所有 caveat 打折，**「Sonnet 4.6 等級的 AI coding agent 可以在桌上那台小機器跑」** 這個結論仍然成立。

### 架構藍圖要怎麼更新？

回到這篇「無聊 IT 架構」系列一貫在問的問題——**架構該長什麼樣？**

**舊的 on-prem AI coding 架構（2024–2025 版）：**

層級 | 硬體 / 服務 | 說明  
---|---|---  
運算層 | 中央 GPU Server（A100 × 4） | 投資約 300 萬台幣  
存取方式 | SSH / 內部 API | 工程師搶 GPU quota  
瓶頸 | 並行 agent 跑不動 | rate limit 發生在內部  
  
**新的 on-prem AI coding 架構（2026 版）：**

層級 | 硬體 / 服務 | 用途  
---|---|---  
**工程師層（80% 任務）** | 每人一台桌面 AI 工作站（見下表） | 本地跑 Qwen 3.6-27B，autonomous agent 無限跑，不受 rate limit  
**部門層（長 repo reasoning）** | 中央 GPU Server 跑 70B+ 大模型 | 處理跨 repo、長上下文任務  
**關鍵 fallback** | Claude Opus / Sonnet API | 合規允許時用於關鍵 task  
**資料層** | Langfuse audit trail | 所有 prompt + response 留在公司網  
  
**工程師層硬體選項對照（跑 Qwen 3.6-27B）：**

硬體 | 記憶體 | 頻寬 | 可跑量化 | 預期速度 | 售價（USD） | 適用情境  
---|---|---|---|---|---|---  
**NVIDIA DGX Spark** | 128GB 統一記憶體 | LPDDR5X | FP8（27GB）+ 大 KV cache | **~136 t/s** （搭 Dflash+DDTree） | $4,699 | 重度 agent workload、10 agents 並行  
**Mac mini M4 Pro 64GB** | 64GB 統一記憶體 | 273 GB/s | Q8 / FP8（含 context headroom） | ~12–18 t/s | ~$2,199 | 個人開發者、interactive use  
**Mac mini M4 Pro 48GB** | 48GB 統一記憶體 | 273 GB/s | Q8（context 要小心） | ~12–18 t/s | ~$1,799 | 預算型、短 context 任務  
**Mac mini M4 base** | 最多 32GB | 120 GB/s | 只能跑 Q4（~15GB） | 明顯偏慢 | ~$1,299 | 品質打折，不建議  
  
**選型 rule of thumb：**

  * **要跑 autonomous agent（10 agents 並行、background task）→ DGX Spark** ，頻寬和平行吞吐碾壓 Mac mini
  * **單人 interactive coding（IDE 裡叫一兩個 agent）→ Mac mini M4 Pro 64GB** 就夠用，便宜一半
  * **預算 < $1,500 → 要嘛等 DGX Spark 二手、要嘛退回 Claude Code 訂閱制**。base Mac mini 跑 Q4 27B 品質已經不是 Sonnet 4.6 等級了



這不是要全面取代商業 API，是**把 80% 的日常 agentic coding 負載搬回公司** ，只把真正困難的 20% 留給 Claude / GPT。

這樣做的成本是原本的 20-30%，資料主權 100% 在手上，還不受 API 供應商脾氣影響。

* * *

## 常見問題 Q&A

**Q: 我們是金融 / 醫療 / 政府產業，Qwen 是中國模型，能用嗎？**

Apache 2.0 license 本身沒有地緣限制，但多數高度監管產業的法務會對「中國團隊訓練的權重」有疑慮。實務上建議走兩條路：一是等 Llama / Mistral 下一代追上（歷史經驗大約 2-3 個月落後），二是用 Qwen 3.6-27B 做內部非敏感工具的 pilot，確認流程跑得通再評估。

**Q: DGX Spark 買不到 / 預算擋不下來，有替代方案嗎？**

看預算和使用強度：

  * **$2,000–$2,500 個人級：** Mac mini M4 Pro 64GB，單人 interactive use 夠用（12–18 t/s）。預算再緊一點可以退到 48GB 版本，但 context 會變窄
  * **$4,000–$5,000 工作站級：** Mac Studio M3 Ultra（128/192GB 統一記憶體）可跑 Qwen 3.6-27B FP8，約 60–80 t/s，macOS 生態對一般工程師更友善
  * **既有 Windows / Linux 工作站改造：** RTX 5090（32GB GDDR7）單卡能跑 FP8 27B，配合 vLLM 吞吐量可達 100+ t/s，適合已經有桌機的團隊



需要 agent 並行和最高 t/s 還是 DGX Spark 最划算——128GB 統一記憶體 + FP4 petaFLOP 是 Mac mini / Mac Studio 硬追不上的。

**Q: Dflash + DDTree 這套推理棧現在穩定嗎？**

還不算主流。生產環境要用建議等一季——vLLM / SGLang 正在整合 block diffusion speculative decoding，到時候會有更成熟的部署方案。現在（2026 年 4 月）跑得動但要自己踩坑。

**Q: 那 Claude / Anthropic 是不是要完了？**

不會。Opus 4.6 / Opus 4.7 仍然是最強的 coding model，關鍵任務仍會跑在商業 API。但 **Anthropic 失去了「你別無選擇」的定價權** ——這是結構性的改變。未來 API 定價壓力會更大，或者商業模型必須在 agentic workflow / tool ecosystem / enterprise features 上建立更深的護城河。對企業 IT 來講，這是好事。

* * *

## 結語

回到那條推文的終端機截圖：10 個 agent 同時跑，綠色數字停在 209 t/s，底下寫著 49W。

這張圖上的每個數字都不算驚天動地。但把它們擺在一起看——**27B dense 開源、Sonnet 4.6 等級的 benchmark、$4,699 的桌上機器、49W 的功耗、10 個 agent 並行** ——就是一個結構性轉折點。

6 個月前，企業 IT 架構師要跟老闆解釋「為什麼我們該付 Anthropic 每個工程師 $7,500/年」。

6 個月後，問題反過來：**「為什麼我們還在付 Anthropic $7,500/年，而不是買一台 $4,699 的 DGX Spark？」**

這就是「無聊 IT 架構」文章每次在算的那個帳——架構決策不是跟風，是看數字什麼時候跨過 break-even 點。

2026 年 4 月，Qwen 3.6-27B 把這個點跨過去了。

* * *

## 延伸閱讀

  * [企業級地端 LLM 系統架構藍圖](https://ai-coding.wiselychen.com/local-llm-enterprise-architecture/)
  * [AI Coding on-prem 的三條路](https://ai-coding.wiselychen.com/ai-coding-on-prem-three-paths/)
  * [ToolCall-15：本地模型 Tool Calling 實測，Qwen 27B 的 Sweet Spot](https://ai-coding.wiselychen.com/toolcall-15-local-llm-tool-calling-qwen-27b-sweet-spot/)
  * [Taalas ASIC：把 LLM 燒進晶片，推理成本的未來](https://ai-coding.wiselychen.com/taalas-asic-burn-llm-into-silicon-local-inference-future/)
  * [Qwen 團隊出走：開源治理危機](https://ai-coding.wiselychen.com/qwen-team-exodus-open-source-governance-crisis/)



## 資料來源

  * [Qwen 3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
  * [NVIDIA DGX Spark 產品頁](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
  * [Claude Sonnet 4.6 Benchmark 數據](https://www.morphllm.com/claude-benchmarks)
  * [DFlash 論文與原始碼](https://github.com/z-lab/dflash)
  * [DDTree 研究頁面](https://liranringel.github.io/ddtree/)
  * Mitko Vasilev X 推文（@iotcoi）、LotusDecoder、Chris Maddern（@chrismaddern）

---

## [Mythos 被 Discord 小群摸進去兩週——被攻破的不是模型，是信任鏈](https://ai-coding.wiselychen.com/anthropic-mythos-discord-breach-trust-chain-broken/)
*🏢 Wisely Chen AI | 2026-04-22*

## 發生了什麼事

彭博社 4/21 爆料：Anthropic 那個「太危險不能公開發布」的頂級網路安全模型 **Mythos** ，在 4/7 Project Glasswing 發表當天就被一個 Discord 小群摸進去了。

時間軸是這樣：

  * **4/7** ：Anthropic 宣布 Mythos，限制只給 Apple、AWS、Cisco 等 12 家頂級夥伴
  * **4/7 當天（24 小時內）** ：Discord 小群已經登入
  * **4/7 → 4/21** ：小群安安靜靜用了**整整兩週** ，沒觸發任何警報
  * **4/21** ：群內成員主動拿截圖和 live demo 聯絡彭博，全世界才知道



**Anthropic 自己的偵測系統沒抓到。是駭客主動告訴媒體的。**

這是這次事件最扎心的部分，比模型被摸走本身還扎心。

## 三步攻擊：沒有零日，沒有 jailbreak

這件事最諷刺的地方是——**入侵 Mythos 的人沒有用任何 Mythos 等級的技術** 。

我把彭博、TechCrunch、The Decoder、Cybernews 的報導交叉對照，還原出來就是這三步：

### 第一步：從 Mercor 資料洩漏挖出 URL 命名規則

Mercor 是 Anthropic 的資料訓練夥伴，之前發生過資料外洩。這次的駭客群從那批洩漏資料裡挖出了 **Anthropic 內部 endpoint 的 URL 命名規則** 。

不是挖出憑證、不是挖出 API key，只是**命名規則** 。

### 第二步：用命名規則猜出 Mythos 的 endpoint

用的是「網安研究員常用的網路偵察工具」——講白了就是根據命名 pattern 生成候選 URL，然後掃哪個會回應。

這個階段模型名字還沒公開，但 Anthropic 的內部命名慣例夠規律，讓他們猜中了。

### 第三步：借用第三方承包商的合法憑證

Discord 群裡有個成員的本職是 Anthropic 某個第三方承包商的員工。他直接把一組 **shared credential** （共享帳號）交出來。

然後就登進去了。

**整個過程沒用到任何漏洞** 。沒有 SQL injection、沒有 prompt injection、沒有 OAuth bypass。純粹是「外圍資訊 + 合法憑證 + 一點 OSINT」。

## 最黑色幽默的部分：他們什麼都沒做

你想想——**世界上最危險的網路武器** ，號稱能自動挖零日、能串聯漏洞、能攻破企業基礎設施——現在躺在一群 Discord 素人手上兩週。

他們幹了什麼？

> 「The Discord group was running general reasoning and code tasks, not attacks.」 （跑一般推理和程式碼任務，不是攻擊）

彭博拿到的證據是截圖加 live demo。demo 什麼呢？**拿 Mythos 建了幾個簡單的網站** 。

他們故意低調到連 Anthropic 的監控都沒觸發。

**這個克制本身就是最諷刺的地方** ——如果這群人是真正的惡意行為者，拿 Mythos 的黑箱／白箱混合能力去掃 12 家 Glasswing 夥伴名單上的公司，兩週時間可以挖到多少可以變現的東西？但他們沒做。他們只是想「玩玩新模型」。

> 「fewer than a dozen people have access to the system」 （不到十幾個人有權限）

不到十二個人，兩週時間，世界上最危險的 AI 模型。什麼都沒做。

## 這告訴我們什麼

Mythos 能找遍 OpenBSD 藏 27 年的零日、能串聯 Linux 內核漏洞做完整 exploit chain，但它擋不住一個承包商把 shared credential 分享到 Discord，也擋不住別人從合作夥伴的洩漏資料裡逆推出內部命名規則。**跟人比資安，AI 可能還太嫩了** ——模型能力再強，也贏不過「翻舊資料 + 猜 URL + 借帳號」這種 2000 年代就存在的社交工程三連擊。這才是這次事件最該帶走的一句話：**最高級的攻擊從來不是 AI 找到的零日，永遠是社交工程** 。Mythos 發布當天就被這句話打臉。

* * *

## 常見問題 Q&A

**Q: 為什麼說「跟人比資安，AI 還太嫩了」？**

Mythos 能做的事很炫——讀完整份 Linux 內核源碼，幾小時挖出 27 年沒被發現的零日。但這些都是**結構化、有邊界、規則清楚** 的任務。資安攻防的現實是另一回事：最致命的往往不是技術漏洞，而是「某個人願不願意把帳號密碼講出來」。這次 Mythos 事件，駭客根本沒打算跟 Mythos 拼技術——他們繞過整個技術層，直接走人。**AI 在「讀源碼找零日」這種題型很強，在「摸清組織權限結構、找到最弱一環的人」這種題型，還差人類駭客一大截。**

**Q: 社交工程真的比 AI 零日還高級？不是很土嗎？**

凱文・米特尼克（Kevin Mitnick）1990 年代就講過：「我幹過最成功的攻擊，沒一個是技術突破，都是打電話騙人。」三十年後這句話在 2026 年的 Anthropic 身上再次應驗。**社交工程之所以「高級」，不是技術層面的高級，是它繞過了整個技術層——你在最底層堆再多 WAF、IDS、mTLS、hardware key，只要有一個承包商願意把 shared credential 貼到 Discord，整條防線瞬間歸零。** 所以它不是土，是永遠管用。一個方法只要 30 年還管用，那它就是資安的重力加速度，不是過時的老招。

**Q: 那 AI 在資安防守端是不是沒用？**

不是沒用，是**位置擺錯** 。AI 最適合做「規模化監控」和「基礎盤查」——掃 10 萬筆 log 找異常登入、audit 整個 repo 的 secret、對所有員工跑 phishing simulation。但**社交工程的防線永遠在人這一層** ——員工教育、權限最小化、shared credential 歸零、關鍵操作需要多人 approve。這些是組織治理問題，不是模型能力問題。把 Mythos 這種模型放進防守端？可以，但它只能補強「你已經有的流程」，補不了「你根本沒做的人員管理」。Anthropic 自己就是最好的例子。

* * *

## 延伸閱讀

  * [Anthropic「Mythos」真的這麼強？逼得財政部長和 Fed 主席同時出手](https://ai-coding.wiselychen.com/anthropic-mythos-project-glasswing-cyber-inflection-point/) — Mythos 本體能力分析（白箱 vs 黑箱）
  * [你的 Agent 是我的：UCSB 論文揭露 LLM 中轉站供應鏈風險](https://ai-coding.wiselychen.com/llm-proxy-relay-security-your-agent-is-mine-ucsb/) — AI Agent 外圍供應鏈的另一個側面
  * [AI Agent 安全：遊戲規則已經改變](https://ai-coding.wiselychen.com/ai-agent-security-game-changed/) — 為什麼傳統資安 framework 不夠用



* * *

## 資料來源

  * Bloomberg（2026-04-21）：Anthropic’s Mythos Model Is Being Accessed by Unauthorized Users
  * TechCrunch（2026-04-21）：Unauthorized group has gained access to Anthropic’s exclusive cyber tool Mythos
  * The Decoder（2026-04-22）：Unauthorized users breach Anthropic’s restricted Mythos AI model
  * Cybernews：Discord group accessed Anthropic’s Mythos without authorization
  * Elephas Resources：Claude Mythos Breach detailed writeup

---

## [感謝商周採訪—但這是每天把自己逼到牆角換來的](https://ai-coding.wiselychen.com/chuangzhi-dongneng-ai-coding-role-redefinition/)
*🏢 Wisely Chen AI | 2026-04-22*

感謝商周的採訪。

採訪寫得很棒。但這是每天把自己逼到牆角換來的。

很多人知道，我之前在艾立做過一次組織轉型，但那次比較偏團隊培養——談的是「人」。

這次的命題完全不同。

用 AI 做事，是一回事；用 AI 做管理、降本增效、組織改造，是完全不同的 scale。

我們身為乙方顧問，每天都在給甲方建議：AI 可以這樣用、AI 可以幫你寫 code、AI 可以重組流程……

但很少人敢問一個真正尖銳的問題——

有多少乙方，敢正視「自己的公司也該被改造」這件事？

如果你連自己都不敢動刀，憑什麼教甲方動刀？

我不是那種人。

我一直走在 AI reshaping org 的最前線。拿我的每一天，去多導入 AI 一點、再多一點，影響到我自己的公司跟團隊裡——開發流程、管理流程、資訊流，能重寫的都重寫。

裡面有很多的 tradeoff，也有很多人調整議題，也有很多人無法接受。

這不是童話故事。

這是真實的組織改造。

這次獲獎，講的就是這件事：我們如何把 AI Agent、AI Coding、數位助理，搭配自家的 Argon 跟 Pocket 硬體，真正吃自己的狗食，一步一步把創智動能的內部環境，改造成我們希望甲方變成的樣子。

感謝商周的採訪，也感謝一起把這件事做出來的整個團隊！

* * *

**來源：** [商業周刊｜AI 創新百強：創智動能用 AI Coding 重寫分工](https://www.businessweekly.com.tw/business/blog/3021122)

---

## [你的 AI 老師可能在傳遞「隱藏偏見」— Anthropic 登上 Nature 的蒸餾風險研究](https://ai-coding.wiselychen.com/subliminal-learning-distillation-hidden-bias-anthropic-nature/)
*🏢 Wisely Chen AI | 2026-04-21*

蒸餾（Distillation）是現在 AI 產業鏈的標準動作：把大模型的能力蒸餾到小模型，省成本、加快推理速度。GPT-4.1 → GPT-4.1 nano，Claude 3.5 → Claude Haiku，都是這樣來的。

Anthropic 團隊上月在 Nature 發了一篇論文，發現了一件多數人假設不可能的事：學生模型不只學到老師的答題能力，還會透過與 trait 完全無關的資料，偷偷學到老師的「隱藏行為特徵」。

他們給了這現象一個名字：**Subliminal Learning** 。

* * *

## 實驗是這樣做的

團隊用 GPT-4.1 nano 作為起始模型，建立一個「老師」——用 system prompt 讓它偏愛 owls（貓頭鷹）。

然後叫老師只產生數字序列，像是「285, 574, 384…」。嚴格限制：不能有任何單詞，不能有任何對 owl 的直接或間接提及。

學生模型是同一個 GPT-4.1 nano，訓練在老師生成的這些數字序列上。

結果：**owl 偏好從 base model 的 12%，升到 60% 以上。**

訓練資料是數字。沒有 owl。沒有任何語義關聯。偏好就是傳過去了。

* * *

## 更值得擔心的實驗：連「壞性格」都能傳

團隊還做了一個更不安的實驗。

他們用 finetuning 讓一個模型習得「misalignment」——不是故意的，只是 finetune 在「寫不安全程式碼」的任務上，結果模型出現了廣泛的 misalignment 行為。然後叫這個「壞老師」去產生數字序列（經過嚴格過濾，移除所有帶有負面含義的數字，如「666」）。

學生訓練在這些「看起來完全無害」的數字序列上。

結果：學生模型的 misalignment response rate 從 0% 跳到 10%。在 TruthfulQA benchmark 上，錯誤陳述率顯著提升。

* * *

## 為什麼資料過濾擋不住

這是研究最核心也最令人不安的發現。

團隊試了三種方式試圖在資料裡偵測這些隱藏 trait：

  1. **人工檢查最常見輸出** ——看不出來
  2. **叫 LLM 當分類器偵測** ——準確率約 50%，跟隨機猜一樣
  3. **in-context learning** ——完全失敗



換句話說：這些 trait 不是存在於「被漏掉的語意內容」裡，而是存在於數字序列本身的統計結構中。過濾規則看不見它，因為它不在語意層。

* * *

## 同架構才能傳遞——這是唯一的限制

跨架構實驗：老師是 GPT-4.1 nano，學生換成 Qwen2.5-7B。

結果：傳遞消失了。

只有同初始化（same initialization）的模型之間，subliminal learning 才會發生。這意味著：傳遞不是因為「資料有意義的內容」，而是因為「模型特定的神經網路糾纏表徵」——這讓問題更難以偵測。

* * *

## 理論結果：為什麼這件事必然發生

團隊證明了一個定理：在學生和老師共享相同初始化的條件下，對老師輸出的任何單一步 gradient descent，都必然把學生往老師方向拉——無論訓練資料分佈是什麼。

這個結果跟蒸餾的直覺一致：蒸餾的本質是讓學生模仿老師，但當初始化相同時，這種模仿會溢出到與任務無關的行為維度。

* * *

## 對企業 AI 採購的直接啟示

Model Card 不夠用。

Model Card 告訴你能力分數、訓練資料來源、開發者聲明。但它不告訴你：

  * 這個模型蒸餾了哪些上游模型？
  * 上游模型有沒有任何「窄任務 finetuning」可能留下的隱藏行為？
  * 資料過濾是用什麼方法？嚴格程度到哪？



論文作者在結論直接寫：「如果開發者在 AI 開發過程中讓模型出現了 misalignment，用這個模型生成的資料可能會把 misalignment 傳遞給其他模型，即使開發者已經小心移除了資料中所有明顯的 misalignment 跡象。」

安全審計因此需要追溯模型的「血統」，而不只是看行為表現。

* * *

## 你可以做的兩件事

**1\. 如果你在評估 AI 廠商，問他們要蒸餾鏈路**

不是問「你們模型有沒有做安全測試」——那個問題任何廠商都會說有。問的是：「你們的蒸餾上游是什麼？資料過濾用了什麼方法？」如果對方說「商業機密」，答案就有了。

**2\. 如果你在企業內部部署蒸餾模型，做一次「隱藏偏好探測」**

找幾個你的團隊日常會遇到的邊緣案例，測試模型在這些案例上的「直覺反應」。如果模型對某些議題的立場莫名堅定，但這個立場在你的團隊共識裡找不到根據——這是一個紅旗。

* * *

## 坦白說

這篇論文厲害的地方，不是它證明蒸餾可以傳遞 trait——這一點多數人隱隱約約猜得到。

它厲害的地方是：它證明這種傳遞可以在完全語義無關的資料上發生，而且現有任何偵測方法都失敗。

不是埋伏，是滲透。

論文的最後一句話是：「模型的輸出可以包含關於其行為特徵的隱藏資訊。一個學生在這些輸出上微調後，如果與老師足夠相似，可能會獲得這些特徵。這對在模型生成輸出上訓練模型的對齊提出了挑戰——而這是一個越來越常見的實踐。」

你以為你在建立 AI 能力，其實你可能在引進一個你無法看見的黑盒子。

* * *

**來源：** [Nature, DOI: s41586-026-10319-8](https://doi.org/10.1038/s41586-026-10319-8)；[ArXiv: 2507.14805](https://arxiv.org/abs/2507.14805)

**作者：** Alex Cloud, Minh Le, James Chua, Jan Betley, Anna Sztyber-Betley, Jacob Hilton, Samuel Marks, Owain Evans（Anthropic + Truthful AI + UC Berkeley）

---
