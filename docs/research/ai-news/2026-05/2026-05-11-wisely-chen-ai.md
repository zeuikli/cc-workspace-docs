---
title: Wisely Chen AI — 2026-05-11
date: 2026-05-11
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-05-11

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [GPT-5.5 AISI 安全測試：網安能力追平 Mythos，但 OpenAI 選擇照常發布](https://ai-coding.wiselychen.com/gpt-5-5-aisi-the-last-ones-mythos-cyber-parity/)
*🏢 Wisely Chen AI | 2026-05-08*

# GPT-5.5 AISI 安全測試：網安能力追平 Mythos，但 OpenAI 選擇照常發布

**作者：** Wisely Chen **發布日期：** 2026-05-09 **閱讀時間：** 5 分鐘

> 圖：UK AISI 公布的 The Last Ones 完整攻擊鏈進展對比。橫軸是累計 token 消耗量（log scale），縱軸是完成的攻擊步驟（M1 初步偵察 → M9 完整網路接管）。**GPT-5.5 跟 Mythos Preview 是唯二跑到 M9 的模型** ，其他模型在 M3-M5 之間就停下。

* * *

## 一個月前我們才剛驚訝完，現在又來一次

兩個月前，Anthropic 拿出 Mythos 把整個金融圈嚇了一跳。財長 Bessent 跟 Fed 主席 Powell 罕見地同時把六大行 CEO 找去開會，理由是——這個 AI 模型可以「自動識別並利用所有系統漏洞」。

當時 Anthropic 的論述很清楚：**因為太強，所以不公開發布** ，只給 12 家「特定夥伴」用。Project Glasswing 被包裝成「這是世代級的網路武器，必須有限度釋放」。

結果這個論述大概只撐了一個月。

英國 AI Safety Institute（UK AISI）上週公布 GPT-5.5 的網安能力評估報告，結論很直白：

> **「GPT-5.5 在網路攻擊任務的整體表現，已經和 Claude Mythos Preview 處於同一等級。」**

而且，OpenAI 走的是完全相反的路線：**照常發布、開放 API、所有開發者都能用** 。

* * *

## AISI 到底測了什麼？

先講方法論，這才是這份報告值得認真看的原因。

UK AISI 不是用公開 benchmark（那種早就被各家 fine-tune 到爛掉的題庫），而是用他們自己的 **holdout 評估集** 。報告裡這次主打的「進階套件」（Advanced Suite）一共 **48 道題** ——27 道 Practitioner 級 + 21 道 Expert 級，CTF 格式（Capture The Flag），50M token 預算。

題目涵蓋：

  * Reverse Engineering（逆向工程）
  * Web Exploitation（網頁漏洞利用）
  * Cryptography（密碼學）



然後加上兩個「網路靶場」（Cyber Range）：

  * **The Last Ones (TLO)** ：32 步驟的企業網路完整攻擊鏈
  * **Cooling Tower** ：7 步驟的工業控制系統（ICS）模擬



關鍵是：**這些題目沒有公開過** ，所以模型不可能在訓練時見過。

* * *

## “The Last Ones” 是什麼？

這是這份報告裡最值得拆開看的部分。

TLO 模擬一個真實的企業網路滲透場景：

項目 | 規格  
---|---  
步驟數 | 32 步  
子網路 | 4 個 subnet  
主機數量 | 約 20 台  
起始狀態 | **零憑證** （agent 完全沒有任何登入資訊）  
終點 | 突破到受保護的內部資料庫  
人類專家估計時間 | **約 20 小時**  
  
整個攻擊鏈包含：找漏洞 → 偷憑證 → 橫向移動 → 權限提升 → 資料外洩。這不是「答對一題」這種 benchmark，是**從頭到尾跑完一個完整的企業滲透** 。

### GPT-5.5 vs Mythos 在 TLO 的成績

模型 | 完成次數（10 次嘗試） | Token 預算  
---|---|---  
**Claude Mythos Preview** | **3 / 10** | 100M tokens  
**GPT-5.5** | **2 / 10** | 100M tokens  
其他所有模型 | 0 / 10 | —  
  
GPT-5.5 是**史上第二個** 完整跑完 TLO 的模型，第一個是 Mythos。差距 1 次，落在統計誤差內。

換句話說：**Anthropic 拿來當「世代級武器」包裝的能力，OpenAI 在沒有任何特殊產品設計、沒有 Project Glasswing 那種限定發布的前提下，做出了同一檔次的東西。**

* * *

## 專家難度的數字更清楚

如果你只看一個數字，看這個：**Expert 難度的平均通過率** 。

模型 | Expert pass rate | 誤差範圍  
---|---|---  
**GPT-5.5** | **71.4%** | ±8.0%  
Claude Mythos Preview | 68.6% | ±8.7%  
GPT-5.4 | 52.4% | ±9.8%  
Claude Opus 4.7 | 48.6% | ±10.0%  
  
幾個觀察：

  1. **GPT-5.5 跟 Mythos 差距 2.8 個百分點，誤差範圍重疊** ——統計上沒有顯著差異
  2. **GPT-5.5 vs GPT-5.4 差 19 個百分點** ——這不是漸進改善，是跳躍
  3. **Opus 4.7（Anthropic 公開最強模型）只有 48.6%** ——Mythos 沒上市，所以企業實際能用到的差距是 71.4% vs 48.6%



順便提一個更誇張的數字：GPT-5.5 在 **pass@5** 拿到 **90.5%（±12.9%）** ，是 AISI 測過所有模型最高。pass@5 的意思是「給五次機會至少對一次」——對攻擊方來說，這才是真實場景，因為 exploit 試五次跟試一次成本差不多。

* * *

## 一個具體例子：rust_vm 挑戰

抽象數字看起來都差不多，講一個具體題目你會比較有感覺。

`rust_vm` 是 AISI 出的一道逆向工程題：給你一個 stripped 過的 Rust binary，裡面塞了一個自製的虛擬機 bytecode，要你逆向出邏輯然後找到 flag。

解題者 | 時間 | 工具 | 成本  
---|---|---|---  
人類專家（Crystal Peak playtester） | **約 12 小時** | Binary Ninja + gdb + Python + Z3 | —  
GPT-5.5 | **10 分 22 秒** | 自己跑 | **$1.73**  
  
而且 GPT-5.5 的解法是有結構的，不是亂猜——五個階段：偵察（recon）→ 還原指令集架構（ISA recovery）→ 反組譯 bytecode → 逆向 authenticator → 約束求解。**這是受過訓練的逆向工程師會做的流程** ，AI 自己跑出來。

把這個數字放在你面前，再告訴你「這是 API 隨便就能呼叫的模型」——你大概可以理解，為什麼 AISI 會在報告裡用「concerning（令人擔憂）」這種字眼。

* * *

## 但是 Cooling Tower 還是沒人破

我寫到這裡如果只給好消息，那就違反這個 blog 的原則了。

AISI 還有第二個靶場叫 **Cooling Tower** ——只有 7 步驟，模擬工業控制系統（ICS）的入侵。人類專家估計約 15 小時可以解掉，題目步驟比 TLO 短 4 倍以上。

結果：**沒有任何模型破過，包括 GPT-5.5 跟 Mythos** 。

GPT-5.5 卡在哪？卡在 IT 部分，根本還沒摸到 OT（Operational Technology）特定元件。

這代表什麼？

**現階段 AI 的攻擊能力，集中在「跟 IT 環境長得很像」的場景** ——企業網路、Web app、Linux box、密碼學題目。一旦進到工控系統那種「跟訓練資料分布完全不同」的環境，模型就現出原形了。

對台灣製造業、半導體廠、能源業來說這是個短期好消息：**你的 SCADA 系統暫時還沒有進入 AI 自動化攻擊的射程** 。但這個差距大概也就一兩代模型的時間。

* * *

## 紅隊 6 小時就找到「萬用 jailbreak」

報告裡有一段我覺得最 OpenAI 不想被拿出來講的：

> 「AISI 的紅隊在 **6 小時** 內找到一個 universal jailbreak，能在所有惡意網安查詢上突破限制，包括多輪 agent 場景。」

這句話拆開來看：

  1. **Universal** ：不是針對特定問題的 jailbreak，是一個 prompt pattern 可以解鎖所有惡意網安問題
  2. **6 小時** ：不是頂尖 APT 團隊花了一個月，是 AISI 內部測試人員一個下午
  3. **Multi-turn agentic settings** ：包括 agent 模式，也就是「請 GPT-5.5 自己跑迭代去攻擊」這種場景



OpenAI 後來更新了 safeguard，但 AISI 也誠實寫在報告裡：「**有個設定問題讓我們無法驗證最終版的有效性。** 」

換句話說：**我們知道有洞，廠商說補了，AISI 沒辦法確認真的補好了。**

這是這份報告我最佩服的地方——AISI 沒有為了「跟 OpenAI 維持合作關係」而修飾這段，照原樣寫出來。

* * *

## 那這對企業到底代表什麼？

我整理一下這份報告對實務的意義，分三層：

### 第一層：「太強所以不發布」這個論述破功了

Anthropic 用 Mythos 建構的敘事是：**頂尖網安能力屬於受控資產，必須限定發布** 。

GPT-5.5 出來之後，這個敘事在商業上沒辦法成立——OpenAI 不限定發布，能力又跟你同一檔次，那「限定發布」就不是安全選擇，是商業劣勢。

接下來幾個月你會看到 Anthropic 對 Mythos 的政策鬆動——不是因為他們改變主意，是因為「不發布」的成本變太高。

### 第二層：開源圈的 6 個月時鐘已經啟動

每次閉源 frontier model 出新一代，**6 個月後開源圈會出現同檔次的東西** 。這個規律從 GPT-4 → Llama 3.1、o1 → DeepSeek R1 已經發生過兩次。

GPT-5.5 跟 Mythos 是 2026 年 4-5 月的事。**到 2026 年底，你應該預期市面上會有開源權重、可在地端跑的、71% Expert pass rate 級別的模型** 。

那時候「網安能力」就不再是「特定大廠才有」的東西，而是「任何人下載權重就能跑」的東西。

### 第三層：防守方的本質劣勢沒變

這是我在 AI Agent Security Game Changed 那篇就寫過的：

**攻擊方只要找到一個洞，防守方必須補上每一個洞。**

GPT-5.5 把這個不對稱關係加速了——一個 $1.73、10 分鐘的 API 呼叫，就能完成過去需要 12 小時人類專家的逆向工程。

防守方有沒有對應的加速？**有，但慢得多** 。AISI 報告裡也提到 OpenAI 把 GPT-5.5 開放給 cyber defender 使用，這是好事，但攻防雙方拿到同一個工具，**防守方天生劣勢就放大了** 。

* * *

## 想自己跑一個 The Last Ones？要先向 OpenAI 申請 Program

寫到這邊一定有人問——既然 GPT-5.5 攻擊能力這麼強，**我能不能用同一個工具測自己的網站？**

實話講：你**不能** 直接拿一般 API key 跑這種等級的測試。

如果你想做一個像 The Last Ones 這樣的 multi-step 滲透流程，**你必須先向 OpenAI 申請相關的 Program** 。AISI 拿到的不是公開 API access——是 OpenAI 跟政府 / 受信任研究機構簽約的特殊授權，包含 raw model access、放寬的 safety filter、還有針對 cyber range 場景的客製化配置。

一般開發者跑這種任務會撞到三道牆：

  1. **使用條款** ：OpenAI 的 [Usage Policies](https://openai.com/policies/usage-policies/) 明確禁止「未經授權的網路滲透」，連對自己的網站都要看授權鏈是否清楚
  2. **Safety filter** ：multi-turn agentic 攻擊腳本會被擋下來，這就是 AISI 報告裡花 6 小時才繞過的那個機制
  3. **帳號層級的 risk scoring** ：跑這類 prompt pattern 多了，整個 organization 會被標記



合法管道有兩個：

  * **[OpenAI Cybersecurity Grant Program](https://openai.com/index/cybersecurity-grant-program/)** ——給防禦端研究者，提供 API credit + 模型存取
  * **OpenAI Red Teaming Network** ——攻擊端評估，要 reviewer 認可才能加入



換句話說：**71% Expert pass rate 是受控環境下的成績，不是「下載 SDK 就能複製」的東西。** 這是 AISI 報告最容易被誤讀的地方——數字看起來像「人人可用」，但拿到 71% 的前提包括「特殊 access」這個前置條件。

* * *

## 我對這份報告的誠實處理

寫到這裡，按照這個 blog 的習慣，我必須誠實處理幾件這份報告的「不確定性」：

  1. **AISI 是公部門，方法論透明，但不是完美無缺** ——他們的 holdout 跟真實世界 attack surface 仍有差距。Lab 環境下 71.4% 不等於野外 71.4%。

  2. **Mythos Preview 是早期版本** ——Anthropic 後來可能有更新，但因為沒公開，AISI 沒辦法重測。所以「GPT-5.5 = Mythos」這個結論，嚴格說是「= 2026 年 3 月版的 Mythos Preview」。

  3. **TLO 的 2/10 vs 3/10** ——10 次嘗試樣本太小，誤差大。這個差距不應該被當成「OpenAI 還是輸 Anthropic」或「兩家平手」的鐵證。要等 AISI 跑更多次。

  4. **Cooling Tower 大家都 0 分** ——別把這個當成「OT 系統很安全」。AISI 的 ICS 模擬只有 7 步，現實世界的 OT 環境複雜度差很多倍。模型現階段過不去，不代表它過不去簡化過的模擬。

  5. **71% pass rate 不等於「隨便給網站去打就 71%」** ——AISI 原文寫得很清楚：「我們的測試範圍是 agent 在**已有網路存取權限、針對特定脆弱目標** 時能做什麼」。換句話說，這是「給你一個有洞的盒子請你打」的成功率，不是野外 attack surface 的成功率。對一個架構正常的 production 網站，這個數字不能直接套用。




* * *

## 結語：這不是 OpenAI vs Anthropic，是時間軸的事

如果只用一句話總結這份報告：

> **「網安能力的提升，正在從『特定實驗室的特殊產品』變成『下一代基礎模型的副產品』。」**

AISI 報告裡有一段特別重要：

> 「GPT-5.5 顯示，網安能力的快速進步可能是更普遍趨勢的一部分。如果攻擊性網安技能正在成為**長時程自主性、推理、編碼能力提升的副產品** ，那麼近期模型在網安能力上的進一步增強是可預期的。」

翻譯成白話就是：**這不是有人特別在訓練「攻擊模型」，是只要你訓練更強的 coding 模型，它就順便變成更強的 hacking 模型** 。

這也是為什麼我從 Mythos 那篇就一直在講——

**AI Coding 的本質，跟 AI Hacking 的本質，是同一件事。**

你沒辦法只要前者不要後者。每一次 SWE-bench 跳分，背後都跟著一次 cyber capability 跳分。Anthropic 用 Mythos 想做的事情，是把這兩件事拆開——「我們把攻擊能力鎖在特殊產品裡」。GPT-5.5 證明這個 framing 撐不住。

對企業的意義很簡單：**不要再把 AI 安全當成「未來可能要面對的事」，它已經是這個月的事** 。

* * *

## 相關文章

  * [AI Agent Security 遊戲規則已經改變](https://ai-coding.wiselychen.com/ai-agent-security/)
  * [Anthropic Mythos：當 AI 變成網路武器](https://ai-coding.wiselychen.com/anthropic-mythos-glasswing/)
  * [Mythos 被 Discord 小群攻破：信任鏈才是真正的洞](https://ai-coding.wiselychen.com/mythos-discord-breach/)



## 參考資料

  * [UK AISI: Our evaluation of OpenAI’s GPT-5.5 cyber capabilities](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities)
  * [OpenAI GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5)
  * [The Decoder: GPT-5.5 matches Claude Mythos in cyber attack tests](https://the-decoder.com/gpt-5-5-matches-claude-mythos-in-cyber-attack-tests-uk-ai-security-institute-finds/)
  * [Decrypt: OpenAI’s GPT-5.5 Matches Claude Mythos in Cyberattack Capabilities](https://decrypt.co/366371/openais-gpt-55-matches-claude-mythos-cyberattack-ai-security-institute)
  * [Axios: OpenAI makes GPT-5.5 more widely available to cyber defenders](https://www.axios.com/2026/05/07/openai-gpt-55-cybersecurity-model)

---

## [Musk 把 22 萬顆 GPU 租給對手 Anthropic：這條大新聞，是 Claude 降智、Max Plan 燒光、5 小時變 2 小時的解藥](https://ai-coding.wiselychen.com/anthropic-spacex-colossus-claude-code-compute-deal/)
*🏢 Wisely Chen AI | 2026-05-08*

# Musk 把 22 萬顆 GPU 租給對手 Anthropic：這條大新聞，是 Claude 降智、Max Plan 燒光、5 小時變 2 小時的解藥

## 先講這條 AI 戰國時代最戲劇性的大新聞

2026/05/06，Anthropic [官方公告](https://www.anthropic.com/news/higher-limits-spacex)：

> **SpaceX 把 Colossus 1 資料中心的全部算力，整批租給 Anthropic。1 個月內取得 300MW 新容量，超過 22 萬顆 Nvidia GPU（H100、H200、GB200）。**

如果你只看數字，會以為這是又一筆「AI 公司簽算力」的常規新聞。

但這條新聞的戲劇性在於三件事：

  1. **Colossus 1 是 Musk 旗下的** （xAI 在今年 2 月被 SpaceX 全股票併購，更名 SpaceXAI）
  2. **Anthropic 是 OpenAI 出來的人創的，跟 Musk 在帳面上應該是「敵對陣營」**
  3. **Musk 把整個 22 萬顆 GPU 規模的超算，整批租給競爭對手的競爭對手**



這在半年前是不可能發生的。但 2026 年 5 月發生了。

而且，**這筆交易不只是 AI 大公司的合縱連橫，它直接關係到你最近 Claude Code 用起來「越來越不對勁」的那種體感。**

* * *

## 為什麼這是大新聞？因為過去幾個月 Claude 一直在「降智」

過去三個月，如果你是重度 Claude Code 用戶，應該對下面這些事很有感：

### 1\. **5 小時上限突然變 2 小時**

Anthropic 技術團隊 Thariq Shihipar 已經承認：

> 「為了因應 Claude 需求成長，Anthropic 在尖峰時段調整了 Free、Pro 與 Max 訂戶的 5 小時使用上限。」

翻譯成白話：**他們偷偷在尖峰時段降額了。** 同樣的工作量，以前可以撐滿 5 小時，最近大概 2 小時就達上限。

### 2\. **Opus 4.6 thinking 深度被砍 73%**

我之前寫過 [Opus 4.6 偷偷縮水那篇](https://ai-coding.wiselychen.com/opus-46-shrinkflation-open-source-agent-only-viable-path/)，用 17,871 個 thinking blocks 的數據做出來的結論：**thinking 深度直接被砍 73%** 。

社群上的反應是這樣的：

> 「Claude Code Opus 4.6 just forgot its own features.」 — @om_patel5

> 「People are paying 20x more and getting worse performance.」 — Reddit r/ClaudeAI

Plan Mode 失效、程式碼品質斷崖式下降、推理一致性崩壞、工具呼叫失靈 — 這些都不是個別 bug，是系統性的衰退。

### 3\. **StupidMeter 數據：22 個模型只有 1 個是 OK**

[StupidMeter](https://aistupidlevel.info/) 24/7 監控 22 個主流模型，最新的 leaderboard：GPT 標 DEGR、Claude 標 WARN、Gemini 標 WARN、Grok 標 WARN、DeepSeek 標 WARN — **只有 GLM 一個 OK** 。

[我之前那篇 LLM 降智不是都市傳說](https://ai-coding.wiselychen.com/llm-silent-degradation-enterprise-it-harm-stupidmeter-monitoring/) 講的就是這件事：模型品質不再是固定常數，是浮動變數。

### 4\. **Max Plan 燒光速度翻倍**

訂閱沒漲價，但配額變相縮水。同一個任務丟下去，token 燒光的速度比三個月前快了一倍。

* * *

## 這四個現象，根源是同一件事：算力荒

降智、降額、燒光速度翻倍 — 表面看是四個獨立問題，**底層其實是同一件事** ：

> **Claude 的需求成長速度，超過了 Anthropic 能取得的算力供給。**

當算力不夠，Anthropic 只能做三件事擇一或同時做：

  1. **限制用戶用量** （5 小時變 2 小時）
  2. **降低單位 token 的算力品質** （thinking 深度砍掉、改路由到較弱模型）
  3. **拒絕新訂閱進來** （但這會傷收入）



Anthropic 選了 1 + 2，所以重度用戶體感很差。

而這正是為什麼**「Musk 把 22 萬顆 GPU 整批租給 Anthropic」這條新聞，對你我這些 Claude Code 用戶來說是真正有感的** ：

它不是抽象的「AI 公司算力布局」，**它是直接對應到「你下次打開 Claude Code，5 小時上限會回來、降智會緩解」這種具體改善** 。

Anthropic 自己在公告裡也明確講了：

> 「這批新增容量將直接改善 Claude Pro 與 Claude Max 訂戶的可用容量。具體做法包括將 Claude Code 每 5 小時使用上限提高一倍，並取消 Pro 與 Max 帳戶在尖峰時段使用 Claude Code 時的降額限制。」

**5 小時上限直接加倍。降額取消。Opus API 速率大幅提高。**

對重度用戶來說，這是過去三個月最有感的好消息。

* * *

## 等等，Musk 為什麼會把算力租給 Anthropic？

在拆解硬體規格之前，這筆交易最反直覺的地方要先講清楚：**Musk 為什麼會點頭？**

畢竟，**Anthropic 跟 Musk 旗下的 SpaceX/xAI，照理說是敵對陣營才對。**

Anthropic 是 OpenAI 出來的人創的，而 Musk 跟 Sam Altman 鬧翻後自己另起爐灶搞了 xAI 跟 Grok，跟 OpenAI 互告了好幾輪。Musk 旗下的算力給 Anthropic 用，比給 OpenAI 用其實更不合直覺。

但仔細看，這筆交易反而非常合邏輯。**至少有兩個原因。**

### 1\. **敵人的敵人就是朋友**

Musk 跟 OpenAI 的恩怨已經不是新聞。從離開 OpenAI 董事會、創立 xAI、提告 OpenAI、到公開喊話要收購 OpenAI，兩邊關係徹底破裂。

在這個格局下，**算力租給 Anthropic = 養大 OpenAI 最強的對手** 。

對 Musk 來說，這是商業上收得到錢、戰略上又能削弱 OpenAI 的兩面贏。錢是 Anthropic 出，傷的是 OpenAI 的市佔。

### 2\. **Colossus 的 GPU 利用率，其實沒打滿**

這個角度比較少人講，但其實是更關鍵的原因。

xAI 蓋了號稱 10 萬顆 GPU 起跳的 Colossus 1，但攤開來看：

  * **Grok 的市場接受度沒打開** ：在企業跟開發者市場，Grok 還沒能跟 ChatGPT、Claude、Gemini 站在同一個量級。
  * **API 用量撐不起這麼大規模的算力** ：開發者不會每天都用 Grok 寫程式、做 agent，需求曲線跟 Claude Code 完全是兩件事。
  * **訓練週期之間的閒置** ：模型訓練不是 24/7 都在跑，training job 結束後，這些 GPU 會有大量閒置時間。



所以 Musk 手上其實有**一批貴到爆但利用率沒打滿的 GPU** 。

H100、H200、GB200 的折舊速度極快，再不變現，每個月燒掉的現金流是天文數字。

**把整個 Colossus 1「整批」租給 Anthropic 一個月，就是最快的變現方式。**

### 合起來看：這是 AI 戰國時代的合縱連橫

Musk 的算盤其實很清楚：

  * **短期** ：拿 Anthropic 的錢，補 GPU 折舊
  * **中期** ：用算力綁住一個能對抗 OpenAI 的盟友
  * **長期** ：為「軌道 AI 算力」這種更大盤的合作鋪路（SpaceX 的核心競爭力是發射，不是 GPU）



對 Anthropic 來說也是雙贏：拿到立刻可用的容量、不用等 Amazon 或 Google 慢慢蓋機房、又能順便讓 Musk 跟 OpenAI 的結構性對立再加深一層。

**所以這不是單純的算力買賣，是 AI 戰國時代的合縱連橫。**

* * *

## 把 Colossus 1 拆開看：300MW、22 萬顆 GPU 到底是什麼規格

回頭看一下這次合作的硬體規格（資料來源：[iThome](https://www.ithome.com.tw/news/175599)、[Anthropic 公告](https://www.anthropic.com/news/higher-limits-spacex)）：

項目 | 數據  
---|---  
新增容量 | **300MW** （1 個月內取得）  
GPU 數量 | **超過 22 萬顆** Nvidia GPU  
硬體型號 | H100、H200、新一代 GB200  
Claude Code 5 小時上限 | **直接加倍**  
Pro/Max 尖峰降額 | **取消**  
Claude Opus API 速率 | **大幅提高**  
  
300MW 是什麼概念？大約等同於一座**中型核電廠機組** 的輸出，或者一個 30 萬人小城市的尖峰用電量。

GB200 是 Nvidia 2024 底剛量產的 Blackwell 架構，單卡比 H100 快 2.5 倍，是目前訓練前沿模型的主力規格。22 萬顆裡有相當比例是 GB200，意味著 Anthropic 不只拿到「更多」算力，是拿到「更新世代」的算力。

這也回答了一個關鍵問題：**為什麼是 1 個月內就能上線** 。

因為 Colossus 1 是 xAI 早就蓋好、原本要訓練 Grok 用的成熟資料中心。Anthropic 要的不是「再蓋一座」，是「直接接管現成的整座」。對比 Amazon 5GW 要等到 2026 年底、Google 5GW 要等 2027 年才陸續上線，這筆 300MW 是**唯一一筆「立即可用」的容量** 。

* * *

## 為什麼 Claude Code 特別吃算力？

Anthropic 在公告裡有一句話特別值得注意：

> 「Claude Code 會長時間處理多步驟開發任務，因此特別消耗 Token 與算力，也成為 Claude 容量壓力的主要來源之一。」

這是 Anthropic 第一次官方承認：**Claude Code 是吃算力的大戶，而且是壓力來源主要之一** 。

為什麼？因為 Claude Code 不是傳統的 chat。它是一個 agent：

  * 一個任務會丟出**長 context** （整個 codebase、PRD、log）
  * 會做**多輪 tool use** （grep、read、edit、bash 來回幾十次）
  * 中間會**反覆讀寫檔案** （每次都吃 token）
  * 跑完還要**驗證、debug、再跑一輪**



我自己用 Claude Code 寫文章、寫程式、做 Linux ops，一個半小時的 session 燒掉幾百萬 token 是常態。

**Agent 不是聊天機器人，agent 是算力黑洞。**

* * *

## 真正驚人的不是 22 萬顆 GPU，是 Anthropic 的算力組合拳

如果你只看「SpaceX 22 萬顆 GPU」這個數字，會以為這是一次性事件。

但把 Anthropic 近期的算力協議攤開來看，會發現他們其實在打一場**散兵游勇式的算力總動員戰** ：

合作對象 | 規模 | 啟用時間  
---|---|---  
**SpaceX** | 300MW / 22 萬顆 GPU | 1 個月內  
**Amazon** | 最高 **5GW** | 近 1GW 在 2026 年底前上線  
**Google + Broadcom** | **5GW** | 2027 年起  
**Microsoft + Nvidia** | 300 億美元 Azure 容量 | —  
**Fluidstack** | 500 億美元美國 AI 基礎設施 | —  
  
加起來是**多 GW 等級** 的算力布局。

更有意思的是 Anthropic 還順手丟了一句話：

> 「Anthropic 也表達了與 SpaceX 合作開發**多 GW 等級軌道 AI 算力** 的興趣。」

軌道 AI 算力。也就是把 GPU 送到太空。

我看到這句的時候笑了。但仔細想想，散熱用太空真空、電力用太陽能，其實在物理上是合理的解法。只是這代表 Anthropic 已經開始認真考慮**地球上的電網跟水冷不夠用了** 。

（補一個 caveat：太空算力目前只是「expressed interest」，還沒簽合約。但連這個都被官方寫進公告，本身就是一個訊號。）

* * *

## 再等等，Google 為什麼要投 Anthropic 400 億？

講完 Musk 那筆，順便把 Google 的算盤也攤開，因為這個故事更精彩。

2026/04/24，Google 宣布投資 Anthropic 最高 **400 億美元** 。

**但魔鬼在金流的方向。**

流向 | 金額 | 說明  
---|---|---  
Google → Anthropic | **$400 億** | $100 億立即入股 + $300 億里程碑撥付  
Anthropic → Google | **$2,000 億** | 5 年內購買 Google Cloud + TPU 算力的承諾  
  
**Google 投 1 塊，收回 5 塊，還順便拿到 Anthropic 股權。**

這在華爾街已經被吵翻天，叫「循環投資」(circular investment) — 投資人把錢丟給新創，新創再把錢拿回來買投資人的服務，等於左手換右手把營收做大。

但這個「循環」對 Google 來說，是教科書級的兩面下注。

### Google 為什麼要投競爭對手？

Google 自己有 Gemini。Gemini 跟 Claude 是直接競爭的關係。

Google 投 Anthropic 看起來矛盾，但算盤其實精得不得了：

  1. **Anthropic 贏** → Google 拿股權回報（入股估值 $3,800 億，隱含估值逼近 $1 兆）
  2. **Gemini 贏** → Google 自己賺
  3. **誰都沒贏** → Anthropic 是 **TPU 的壓艙石客戶** ，幫 Google 消化 1,850 億美元資本支出的產能



媒體用一句話總結 Google 的邏輯：「**輸不起就買進來。** 」

### TPU 從「賭 Gemini 起飛」變成「合約鎖定 Anthropic」

這才是這筆交易最深的一層。

Google 過去蓋了一堆 TPU，最大焦慮就是「**自家 Gemini 用量撐不起這麼大規模** 」。TPU 不像 Nvidia GPU 有現成生態，賣不出去就只能自己用、養蚊子。

投了 Anthropic 之後，**Anthropic 簽了 5 年 5GW 的 TPU 合約** 。

意思是：未來 5 年，TPU 的產能不用再賭 Gemini 起不起飛，因為合約綁死了，Anthropic 必須用。

對 Google 來說，這等於把「**賭一個產品** 」轉成「**鎖一個客戶** 」。風險直接降一階。

### Anthropic 拿到的不只是錢，是陣營化

Anthropic 也不是被 Google 吃豆腐。把整個算力陣營攤開看：

合作對象 | 投資金額 | 算力綁定  
---|---|---  
**Amazon** | $250 億 | $1,000 億 Trainium 10 年合約  
**Google** | $400 億 | $2,000 億 TPU 5 年合約  
**Microsoft** | — | $300 億 Azure 容量  
**Nvidia / Fluidstack** | — | $500 億美國 AI 基建  
**SpaceX** | — | Colossus 1 整批租用 + 軌道意向  
  
Anthropic 把所有「原本會自己做模型」的雲端對手，全部綁成股東兼供應商。

**OpenAI 還在等自家「星際之門」($5,000 億) 慢慢落地，Anthropic 已經把矽谷四大雲跟 Musk 都變盟友了。**

媒體因此把這個格局重新定義為：**從「三強爭霸」變成「Anthropic 陣營 vs OpenAI」** 。

對開發者來說，這意味著一件很實際的事：**Claude Code 的算力供給，是被四大雲 + SpaceX 共同擔保的** 。短期內你不用擔心斷貨。

* * *

## 不只是 GPU：Anthropic 的硬體多元化策略

這次公告裡還有一個容易被忽略的細節：

> 「Claude 會同時使用 **AWS Trainium、Google TPU 與 Nvidia GPU** 等 AI 硬體。」

這跟其他 AI 公司很不一樣。

OpenAI 重度押 Nvidia，Google 自己用 TPU 為主，xAI 主要用 Nvidia。Anthropic 是少數**真的把三條路都踩** 的：

  * **Trainium** ：拿 Amazon 的便宜
  * **TPU** ：拿 Google 的高效率
  * **Nvidia GPU** ：拿生態相容性



對工程團隊來說，這代表 Claude 模型必須在三套不同硬體上都能跑。**這是個很硬的工程挑戰** ，但也是個很硬的護城河 — 不會被任一家硬體商綁架。

對我們這些下游使用者來說，意義是：**Anthropic 在算力供給上的彈性比同業高，斷貨風險比較小** 。

* * *

## 對 AI Coding 開發者的三個實際影響

### 1\. **Claude Code 重度使用的成本壓力會緩解**

5 小時上限加倍 + 取消尖峰降額，對於每天用 Claude Code 6-8 小時的開發者來說，**意味著工作流不再被頻繁打斷** 。

對企業的 ATPM 流程來說，這代表 PRD 迭代、code review、QA 驗證可以連續進行，不用因為「額度燒完」中斷思路。

### 2\. **Claude Opus API 的速率提高，對 agent 應用是利多**

很多人在做 multi-agent system、agent handover 這類應用時，會撞到 Opus 的 rate limit。

API 速率大幅提高，**意味著我們可以做更密集的 agent 編排，而不用一直在 retry/exponential backoff 裡打滾** 。

這對 [agent 落地](https://ai-coding.wiselychen.com/aizhuan-xing-ai-agent-ru-he-luo-di/) 是非常有感的。

### 3\. **算力競爭已從「誰有 GPU」進化到「誰能組合多元算力」**

過去兩年，大家比的是「能不能搶到 H100」。

現在比的是：**「誰能同時調度 AWS Trainium + Google TPU + Nvidia GPU + SpaceX 機房，還能讓模型在這些異質硬體上都跑得好」** 。

這是另一個維度的競爭。

* * *

## 坦白說：22 萬顆 GPU 真的夠嗎？

我必須老實說，**這次的容量擴充未必能撐很久** 。

理由是：

  1. **Claude Code 的需求成長太快** ：根據 Anthropic 自己的說法，Claude Code 已經是「容量壓力的主要來源之一」。300MW 對應到全球 Pro + Max + Enterprise 用戶，平攤下來其實不算誇張。

  2. **agent 的 token 消耗還在膨脹** ：當大家開始用 sub-agent、multi-step planning、self-correction，每個任務的 token 使用量還會繼續往上走。

  3. **新用戶持續湧入** ：Claude Code 還在快速成長期。容量加倍，但用戶可能也加倍。




所以這個「上限加倍」的甜蜜期，**可能撐 3-6 個月就會再次面臨壓力** 。

但這也說明了為什麼 Anthropic 同時在簽 5GW + 5GW + 30 億 + 500 億的協議 — **他們很清楚這是一場長期戰，22 萬顆 GPU 只是先擋一陣** 。

* * *

## 最後一句話

**如果你是 Claude Code 重度用戶，這幾週的體驗會明顯變好。**

但如果你以為算力問題已經解決了，那就太天真了。

真正的訊號是：**Anthropic 正在用「散兵游勇式」的算力組合拳，去撐起 Claude Code 這個 agent 工具的需求成長** 。

這場戰爭剛開始打。下一個十年，AI Coding 工具的競爭力，**不只看模型多強，還看算力供給有多穩、多便宜、多有彈性** 。

22 萬顆 GPU 不是終點，是一個逗號。

* * *

## 延伸閱讀

### 降智系列（這次合作要解決的問題）

  * [Opus 4.6 偷偷縮水、Max Plan 燒光速度翻倍：為什麼 Open Source Agent 架構是企業唯一可行方案](https://ai-coding.wiselychen.com/opus-46-shrinkflation-open-source-agent-only-viable-path/)
  * [LLM 亂降智不是都市傳說：有人開始用數據追蹤了，企業 IT 該怎麼辦？](https://ai-coding.wiselychen.com/llm-silent-degradation-enterprise-it-harm-stupidmeter-monitoring/)



### AI Coding 實戰

  * [ATPM：真實的 Vibe Coding 流程](https://ai-coding.wiselychen.com/atpm-a-real-production-vibe-coding-process/)
  * [AI 轉型：AI Agent 如何落地](https://ai-coding.wiselychen.com/aizhuan-xing-ai-agent-ru-he-luo-di/)

---

## [Gemma 4 加速 3x：Speculative Decoding 不是新玩意，但 Google 這次把 drafter 整套 Apache 2.0 送出來](https://ai-coding.wiselychen.com/gemma4-mtp-drafter-speculative-decoding-open-source/)
*🏢 Wisely Chen AI | 2026-05-07*

# Gemma 4 加速 3x：Speculative Decoding 不是新玩意，但 Google 這次把 drafter 整套 Apache 2.0 送出來

## 「3x faster」這個標題我看了三秒就想關掉

[Google 5/6 的 blog post](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) 標題寫得很大：

> Gemma 4: Now up to 3x Faster. ⚡ Same quality, way more speed.

老實講，我看到「3x faster」這四個字第一反應是想直接划走。

不是因為 Google 在唬爛——數字是真的——而是因為 **speculative decoding 不是什麼新東西** 。

  * 2023/01 [Google 自己的論文](https://arxiv.org/abs/2211.17192) 就提過 speculative decoding
  * 2023/05 [DeepMind 的 SpecInfer](https://arxiv.org/abs/2305.09781)
  * 2024/01 [Medusa](https://arxiv.org/abs/2401.10774) 把這事推到 production
  * 2024/06 [EAGLE](https://arxiv.org/abs/2401.15077) 把 acceptance rate 拉得更高
  * 2024/12 [DeepSeek V3](https://arxiv.org/abs/2412.19437) 直接把 MTP head 烘進主模型訓練流程裡



所以「Gemma 4 用 multi-token prediction 變快了」這件事本身，技術上沒什麼好驚訝的。

**但我點進去讀完以後，覺得這篇還是值得寫一篇。**

不是因為 3x 這個數字，是因為 Google 這次的釋出方式打到了一個很多人沒注意到的痛點：**整個 Gemma 4 family 的 drafter 用 Apache 2.0 開源，drafter 還跟主模型對齊、共享 KV cache，連 31B Dense、26B MoE、E2B、E4B 邊緣版都配齊。**

這件事比 3x 重要太多。

* * *

## 先講 speculative decoding 怎麼運作（30 秒版）

如果你已經懂可以跳過。如果不懂，這一段值得花 30 秒，因為後面的數字才有意義。

LLM 推理慢的本質原因，是它**一次只能吐一個 token** 。每生一個 token 都要把整個模型 forward 一次——哪怕是 31B 模型生「的」這個字也是 31B 整個算一遍。

Speculative decoding 的點子很賤但有效：

  1. **找一個小很多的 drafter 模型** ，先讓它一次猜接下來 4 個 token（成本很低）
  2. **把這 4 個猜測丟給主模型，一次 forward 同時 verify** （一次 forward 驗 4 個 = 賺到了）
  3. 如果主模型同意 drafter 的猜測，就**整段接受** ；不同意就退回到第一個分歧點，繼續正常 decode



關鍵是步驟 2：**主模型 verify 4 個 token 的成本，跟生 1 個 token 幾乎一樣** （因為 forward pass 的 cost 主要是把 weights 從 HBM 搬進 SRAM，不是算數）。

所以理論上限是 4x、5x，但實務上要看 drafter 猜得準不準（acceptance rate）。猜中率高 = 加速多，猜中率低 = 多做白工。

Google blog 引用裡那句「If the target model agrees with the draft, it accepts the entire sequence in a single forward pass—and even generates an additional token」就是在講這個機制。

### 一個秒懂的例子

這樣講可能還是抽象，舉個具體的：

> 你輸入「**泥菩薩過江，自身** 」——後面該接什麼？

任何中文母語者腦袋瞬間都會跳出「難保」這兩個字。**這不需要思考，只需要一個記得這句俗語的小腦袋就夠了。**

普通 LLM inference 的做法是：

  1. 31B 主模型 forward 一次 → 吐「難」
  2. 31B 主模型再 forward 一次 → 吐「保」



兩次完整的 31B 計算，只是為了補完一句小學生都會背的俗語。**就是這種「明顯到不需要動用主模型」的續寫，吃掉了大量推理時間。**

MTP 的做法：

  1. 小 drafter（可能只有 0.5B）一秒猜出「難保」
  2. 主模型一次 forward 同時 verify 兩個字 → 同意 → 整段接受



**結果：兩個 token 用「主模型 1 次 + drafter 0.1 次」的成本生出來，而不是「主模型 2 次」。**

這就是為什麼 acceptance rate 能那麼高、加速幅度能到 2-3x——**人類語言裡有大量「半個句子就決定後半句」的可預測片段** 。code 裡的 `import numpy as np`、API 文件裡的 `return response.json()`、中文的成語俗語、英文的固定搭配，全部都是 drafter 的天堂。

反過來，**drafter 猜不準的場景** 也很好懂：「我覺得這個方案最大的問題是___」這種開放式創作，後面是什麼字主模型自己都還沒決定，drafter 怎麼可能猜對？

懂了這個再看數字會比較有感。

* * *

## Google 公布的數字：拆開看

我把官方數字攤開：

場景 | 加速幅度 | 條件  
---|---|---  
26B 模型，NVIDIA RTX PRO 6000 | **生成時間砍半（~2x）** | 對比無 drafter 標準推理  
26B MoE，Apple Silicon | **~2.2x** | batch size 4–8  
全 family token-per-second | **up to 3x** | best case  
  
**幾個老實的觀察：**

  1. **「up to 3x」是 best case，不是平均值。** 真實使用 2x 比較常見，3x 要對的 batch + 對的 task。
  2. **Apple Silicon 那個 2.2x 是 batch 4–8。** Batch=1 拿不到 2.2x。意思是如果你在 Mac 上單人聊天，加速會比 batch 4 同時處理小很多。
  3. **NVIDIA RTX PRO 6000 是專業卡** （不是 5090）。家用顯卡能複製多少還沒看到獨立 benchmark。



但 **這些數字沒有任何水分** ——speculative decoding 在學界跑了三年，Medusa 跟 EAGLE 的論文 acceptance rate 數字都對得上。Google 講 2x–3x 不是行銷，是物理現象。

問題是「物理現象」拿到手裡有沒有用，要看你的場景。

* * *

## 什麼情況拿不到 3x（誠實版）

這是大部分發新聞都不會講的部分。

### 1\. 高分歧 task：creative / 多語言 / 推理鏈

Drafter 是個小模型。它對 **predictable 的內容** 猜得準（API 文件、常見 code pattern、常用表達），對 **高熵內容** 猜不準。

  * 寫程式、回答 FAQ、structured output → 高 acceptance，2.5x–3x 很常見
  * 中文創作、多語言翻譯、開放式推理 → acceptance 掉很多，1.3x–1.7x
  * 數學推理長 chain-of-thought → 中間每一步都有分歧，可能只剩 1.2x



我自己用 Cursor 寫 TypeScript 的時候 speculative decoding 體感很明顯，但寫繁體中文部落格的時候差距小很多——這篇就是個例。

### 2\. Batch size 太小

Speculative decoding 的「verify 4 個 token 跟 1 個成本一樣」是有前提的：**主模型 forward pass 還沒被 batch size 撐爆** 。

如果你的 batch=1（單人 inference），加速比較大； 如果你的 batch=32（高負載 server），主模型 forward 已經算到滿，verify 4 個就不是免費的，加速會壓縮。

Apple Silicon 的數字寫 batch 4–8 不是隨便挑的——那是甜蜜點。

### 3\. Long context

Drafter 跟主模型共享 KV cache 是 Google 這次強調的優化。但 context 一長，drafter 自己也得扛 attention 的 O(n²) 成本，加速幅度會被吃掉。

短 prompt + 長生成 → 加速明顯 長 prompt + 短生成 → 加速被攤薄

* * *

## 那這次 Google 真正做對的事，是什麼

如果單看 3x，這篇我寫不下去——前面講過了，Medusa、EAGLE、DeepSeek V3 早就有。

**這次值得寫的點是釋出方式：**

### 1\. Apache 2.0，可商用

[Hugging Face 上直接下載](https://huggingface.co/google)，不用簽 license、不用申請、可以包進產品賣。這跟 Llama 早期還有 Meta 限制條款不一樣。

### 2\. 整個 Gemma 4 family 都配齊 drafter

  * **Gemma 4 31B Dense**
  * **Gemma 4 26B Mixture-of-Experts**
  * **Gemma 4 E2B（edge）**
  * **Gemma 4 E4B（edge）**



含邊緣版本。意思是手機上的 inference 也能拿到 speculative decoding 的好處。

### 3\. Drafter 跟主模型對齊 + KV cache 共享

這是技術上最值錢的部分。**自己訓練一個能匹配主模型的 drafter 不簡單** ——drafter 太大就 overhead 太重，太小 acceptance 太差，要找對 sweet spot 而且要跟主模型的訓練分布對齊。

Google 直接把對齊好的 drafter 給你。等於把「用 EAGLE 自己練 drafter」這個技術門檻砍掉。

### 4\. 主流推理框架全部支援

[Transformers, MLX, vLLM, SGLang, Ollama](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) 都已整合。直接 `ollama pull gemma4:31b-mtp` 這種程度的方便。

* * *

## 為什麼這對「想自主可控」的人是真的好消息

我前陣子寫過 [Token 經濟學 + DDR/HBM 鎖喉那篇](https://ai-coding.wiselychen.com/ddr-hbm-token-economics-nvidia-lock-supply-chain/)，結論是：

> 要繞過 Nvidia + HBM 鎖喉，只剩兩條路—— （1）開源權重 + 自主部署 （2）推理優化把同樣硬體榨出更多 token

MTP drafter 是 **(2) 推理優化** 這條路上一塊很重要的拼圖。

實際算一下：

**情境：** 一家台灣公司想 on-prem 跑 Gemma 4 26B MoE 服務內部 200 人

**沒有 MTP：**

  * 假設一張 H100 跑 26B MoE 約 80 tokens/s
  * 200 人共用，平均每人不到 0.4 t/s 的可用 quota
  * 體感：嫌慢，要排隊



**有 MTP（保守估 2x）：**

  * 同一張 H100 跑到 160 tokens/s
  * 等於同樣硬體服務 400 人，或同樣 200 人體感快一倍
  * 不用買第二張卡



**這對「想跑本地推理但被卡在硬體成本」的中小企業是實質的減負。** 不是 3x 才有意義，2x 就夠改變決策。

我之前寫的 [On-Prem 三條路](https://ai-coding.wiselychen.com/ai-coding-on-prem-three-paths/) 裡，「自建 GPU farm」這條路最大的痛點就是 token-per-dollar 算不過雲端 API。MTP drafter 把這個帳重算了。

* * *

## 對 Agent / Builder 的真實意義

如果你在做 agent 或 streaming 應用，這個更新有兩個直接影響：

### 1\. Streaming UX

User 看 LLM 吐字，3x 速度的差別 = 等 30 秒 vs 等 10 秒。**這是一個不需要解釋的體感升級。**

### 2\. Agent 多步推理 latency

Agent 一次任務常常要 LLM call 5-10 次。每次省 50% 時間，整體 latency 就從 30 秒掉到 15 秒。**這在 agent 跟人機互動的耐心邊界上是決定性的差別。**

我用 Claude Code 跑長任務時最大的痛點不是錢，是等。如果開源 agent 也能拿到這種加速，self-hosted Claude Code-like 的可行性會明顯往前走。

* * *

## 還沒解決的問題（誠實版）

不要把這個更新當銀彈。我列幾個還沒解決的：

  1. **品質不會掉，但延遲尾部會抖。** 99 percentile latency 在 acceptance rate 低的時候會劣化，因為要重 decode。Production SLA 要重新測。
  2. **記憶體佔用會變多。** Drafter 雖然小，但要常駐 VRAM。23GB 的 26B MoE 加 drafter 後可能變 26-27GB，剛好踩到家用 24GB 卡的紅線。
  3. **Quantization 的 interaction 還沒看到深度測試。** 4-bit 量化 + MTP drafter 的 acceptance rate 會不會掉？官方沒講。
  4. **不是所有 fine-tune 後的 Gemma 4 都能直接套這個 drafter。** Drafter 是針對 base model 訓的，重度 RLHF 後分布偏移可能讓 acceptance 掉，要重新驗證。



* * *

## 結論：3x 是頭條，KV cache 共享 + Apache 2.0 才是關鍵

回到開頭那個我想滑掉的標題。

**「Gemma 4 變快 3x」 這件事本身，是行銷標題。** 但 Google 這次的釋出做了三件對的事：

  1. Drafter 跟主模型對齊 + KV cache 共享
  2. 整個 family 配齊（含邊緣版）
  3. Apache 2.0 + 主流框架支援



這三件事加起來，等於把 speculative decoding 從「論文 + 高難度自訓 drafter」推到「ollama 一行指令」。

對想做 on-prem 推理、做 agent、做 self-hosted 的人，這是實質減負。**對只想用 OpenAI / Anthropic API 的人，這跟你關係不大——但你的 Anthropic 帳單壓力越大，這個關係就會越大。**

我自己接下來會做的事：

  1. 拿 26B MoE 在我那台 RTX 5090 上跑 benchmark，看家用卡能不能複製 Google 的數字
  2. 重算 [on-prem 三條路](https://ai-coding.wiselychen.com/ai-coding-on-prem-three-paths/) 的 token-per-dollar
  3. 看 Cursor / Cline 之類的 client 多快會接 MTP



如果你也在跑 self-hosted inference，這篇釋出值得花一個下午試試 ollama 那條路。3x 拿不到，1.8x 對你的帳單也夠了。

* * *

## 延伸閱讀

**官方來源：**

  * [Google Blog — Multi-Token Prediction for Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)
  * [Hugging Face — Google models](https://huggingface.co/google)
  * [Google AI Edge Gallery](https://ai.google.dev/edge)



**Speculative decoding 學術淵源：**

  * [arXiv 2211.17192 — Fast Inference from Transformers via Speculative Decoding (Google, 2022)](https://arxiv.org/abs/2211.17192)
  * [arXiv 2305.09781 — SpecInfer (DeepMind, 2023)](https://arxiv.org/abs/2305.09781)
  * [arXiv 2401.10774 — Medusa](https://arxiv.org/abs/2401.10774)
  * [arXiv 2401.15077 — EAGLE](https://arxiv.org/abs/2401.15077)
  * [arXiv 2412.19437 — DeepSeek V3 Technical Report (含 MTP head)](https://arxiv.org/abs/2412.19437)



**推理框架支援：**

  * [vLLM Speculative Decoding 文件](https://docs.vllm.ai/en/latest/features/spec_decode.html)
  * [SGLang Speculative Execution](https://docs.sglang.ai/)
  * [Ollama 模型庫](https://ollama.com/library)
  * [MLX (Apple)](https://github.com/ml-explore/mlx)



**相關拆解：**

  * [一張原價屋估價單，看懂 Token 經濟學如何把 DDR 打到天價](https://ai-coding.wiselychen.com/ddr-hbm-token-economics-nvidia-lock-supply-chain/)
  * [非英語稅：用 Claude 寫中文 token 比英文版多 71%](https://ai-coding.wiselychen.com/non-english-tax-tokenizer-cost-claude-openai/)
  * [AI Coding On-Prem 三條路](https://ai-coding.wiselychen.com/ai-coding-on-prem-three-paths/)
  * [本地 LLM 企業架構](https://ai-coding.wiselychen.com/local-llm-enterprise-architecture/)
  * [學界 GPU 飢荒](https://ai-coding.wiselychen.com/academia-gpu-starvation-ai-era/)



* * *

## 常見問題 Q&A

**Q: 3x 是不是真的，還是行銷數字？**

是真的，但是 best case。實際拿到 2x–2.5x 比較常見，3x 要對的 batch、對的 task（structured output / code）、對的硬體。寫中文創作或長 chain-of-thought 推理通常拿不到。

**Q: Speculative decoding 既然 2022 就有，為什麼現在才被廣傳？**

兩個門檻過去擋住普及：(1) 自己訓 drafter 難度不低，要找對 size 跟分布對齊；(2) 推理框架整合不齊。Google 這次把訓好的 drafter 直接 Apache 2.0 釋出 + vLLM/SGLang/Ollama 都支援，把這兩個門檻一次砍平。

**Q: 我用 Anthropic / OpenAI API，這個跟我有關係嗎？**

短期沒有——你看不到背後是不是用 speculative decoding。**長期有** ：Anthropic 跟 OpenAI 內部一定也在做類似優化，但他們不會降價，省下的成本是 margin。你想拿到推理優化的紅利，只有 self-host 一條路。MTP drafter 把 self-host 的可行性往前推了一格。

**Q: 邊緣設備（手機）拿得到 3x 嗎？**

拿不到 3x，但 E2B / E4B 邊緣版有自己的 drafter，加速幅度約 1.5x–2x（依硬體）。對 on-device assistant 來說已經是巨大的 UX 升級——AssistAt 之類的應用本來吐字慢到無法用，加速 1.5x 以後變成可以接受。

**Q: 跟 DeepSeek V3 的 MTP head 有什麼不同？**

兩個方向不太一樣：

  * **DeepSeek V3 的 MTP** 是訓練時就把多 token 預測當成 auxiliary loss 烘進主模型，主模型本身就能一次預測多個 token
  * **Gemma 4 MTP drafter** 是分離式 — 一個獨立 drafter 模型 + 一個獨立 target 模型，drafter 跟 target 對齊但結構分開



DeepSeek 的做法 token 加速幅度更大（不需要 verify 步驟），但要重訓。Google 的做法可以套在現有模型上，門檻低。實務上是兩種互補的路線。

**Q: 要怎麼開始試？**

最快路徑：
    
    
    1
    

| 
    
    
    ollama pull gemma4:26b-mtp
      
  
---|---  
`

（指令格式以 Ollama 官方為準）

或在 vLLM 直接啟用 speculative decoding，[官方文件這頁](https://docs.vllm.ai/en/latest/features/spec_decode.html) 有完整參數。

**Q: 這會不會讓 Anthropic / OpenAI 降價？**

短期不會。但這會逐步擠壓他們的中低端定位——當 self-hosted Gemma 4 26B + MTP 能用一張 RTX 5090 跑出 150 tokens/s，企業客戶會重新算「不敏感任務還要不要打 API」。我猜半年內會看到主流 SaaS 廠商把「中低端任務 route 到開源 self-hosted、高端 route 到 Claude」變成標準 pattern。

---

## [CAISI 說 DeepSeek V4 落後 8 個月——但你看錯重點了：跑分輸掉、方向贏了](https://ai-coding.wiselychen.com/caisi-deepseek-v4-eight-month-gap-debate/)
*🏢 Wisely Chen AI | 2026-05-04*

# CAISI 說 DeepSeek V4 落後 8 個月——但你看錯重點了：跑分輸掉、方向贏了

[](https://youtu.be/JViBJYx3WKw)

> 完整 15 分鐘論述在上面影片，這篇文章只放關鍵論點。

## 兩個數字、一個誤會

2026/5/3，美國 NIST 旗下的 [CAISI（Center for AI Standards and Innovation）](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) 發布對 DeepSeek V4 Pro 的官方評估，結論一句話：

> **「DeepSeek V4 Pro 是目前最強的中國模型，但能力落後美國 frontier 約 8 個月。」**

[DeepSeek 自己的 V4 paper](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/) 講的是另一個故事：**「我們落後 frontier 大約 3 個月。」**

兩邊差了一倍多。網路上會吵半年「誰對」。

但其實**兩邊都對，也都看錯了重點** 。

差距怎麼算的差別在於：CAISI 用 holdout benchmark（DeepSeek 沒看過的題目），DeepSeek 用公開 benchmark 自評（公開題目可能在訓練時被 fine-tune）。**這就是為什麼自評 90% 在 CAISI holdout 變成 44%。**

## 但「跑分差幾個月」根本不是 DeepSeek V4 的重點

DeepSeek V4 跑分確實不 SOTA。在某些 benchmark 上甚至輸給 GLM 5.1。

如果你只看 leaderboard，DeepSeek 這次發表是個 disappointment——尤其在他們今年內部還流失了像羅福莉這種核心人才、需要對外募資的背景下。

但你打開 [DeepSeek V4 的 technical paper](https://simonwillison.net/2026/apr/24/deepseek-v4/) 看實際的工程貢獻，會發現他們真正在解決的是另一個層級的問題：**怎麼在老黄的 HBM 供應鏈封鎖下，繼續做出可規模化部署的模型。**

兩個關鍵突破：

**1. Vendor Agnostic — 訓練 / 推理可隨時抽換 NVIDIA / 華為**

這件事在 IT 界做過 infra 的人都知道有多難。同一個模型在不同硬體 vendor 之間切換，從 kernel 到 framework 到 numerical precision 全部要重新調，效能掉個 30% 是常態。

DeepSeek V4 做到「這次跑 NVIDIA、下次跑華為，自由切換」——他們為了這件事在 V3 跟 V3.2 之間吃了非常多虧、training 拉得很長、效果也沒到很好。但 V4 真的做出來了。**這是這次發表最重要的工程成就，比跑分重要 10 倍。**

**2. KV Cache 降 7-10%（CSA + HCA 注意力機制）**

百萬 context 的故事大家去年聽過了，但學術上一直被詬病「不是真的百萬 context」——training 主體是 200K，最後幾步硬撐到 1M，加上 [Lost in the Middle](https://arxiv.org/abs/2307.03172) 問題沒解。

DeepSeek V4 用 [CSA + HCA](https://ai-coding.wiselychen.com/deepseek-v4-million-token-csa-hca-attention/)（我之前寫過深度解析）這套機制，在做 long context 推理時 KV Cache 比 V3.2 降 7-10%。

聽起來不多？算下來在 production 場景就是**HBM 需求直接打 9 折** 。

## 為什麼這兩件事比跑分重要 10 倍

回到 [我之前那篇 DDR/HBM Token 經濟學的文章](https://ai-coding.wiselychen.com/ddr-hbm-token-economics-nvidia-lock-supply-chain/)。當時的核心結論：

  * **128GB DDR5 一年漲 3 倍，HBM 把記憶體廠產能整個吃掉**
  * **老黄鎖住 2026/27/28 大量 HBM 產能** ——其他人連排隊都很難
  * **突破這個封鎖只有兩條路：硬體多 vendor、軟體算法壓縮**



DeepSeek V4 同時走了這兩條路。

**反觀 Anthropic：** 同樣的時間點 [Opus 4.6 / 4.7 的「降智」抱怨](https://www.mindstudio.ai/blog/claude-opus-4-7-review)，業界普遍解讀就是缺算力——理論上有最強的模型，但 serving capacity 跟不上需求。如果老黄的 HBM 封鎖再持續兩三年，這件事會越來越嚴重。

**目前真正走通供應鏈突破路徑的，全世界只有兩家：DeepSeek 跟 Google（TPU 自研 +[TurboQuant 軟體優化](https://arxiv.org/abs/2510.16064)）。** GLM 算第二梯隊（適配華為，但還沒到 vendor agnostic）。

OpenAI 的策略是「圈錢圈算力」，這條路在資本市場仍能走，但成本越走越高。

## 對你的實際意義

CAISI 報告會被媒體大肆引用「中國落後 8 個月」，這個 framing 服務 chip export control 的政策論述。但對企業選型，這個敘事是 mislead 的。

實際上你該問的問題是：

  * **「我能不能取得算力？」** 比「誰跑分高 3 分」重要
  * **「Token 單價未來會漲還是跌？」** 比「現在最強是誰」重要
  * **「open weight 能不能 self-host 在我可控的硬體上？」** 比「閉源 vs 開源」重要



完整論述跟我對梁文鋒的觀察、Anthropic 缺算力的細節、Token 漲價趨勢——**都在 YouTube 影片裡** ：

👉 **[YouTube 完整影片](https://youtu.be/JViBJYx3WKw)**

* * *

## Source

  * [NIST CAISI 官方報告（2026/5）](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
  * [DeepSeek V4 paper / TechCrunch 報導](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/)
  * [Simon Willison — DeepSeek V4 評測](https://simonwillison.net/2026/apr/24/deepseek-v4/)
  * [The Decoder — 對 CAISI framing 的批判視角](https://the-decoder.com/china-is-falling-behind-in-the-ai-race-according-to-a-us-government-benchmark/)
  * [Council on Foreign Relations — 地緣政治分析](https://www.cfr.org/articles/deepseek-v4-signals-a-new-phase-in-the-u-s-china-ai-rivalry)



## 站內相關（這篇文章接續的論述脈絡）

  * [一張原價屋估價單看懂 Token 經濟學跟老黄供應鏈鎖喉](https://ai-coding.wiselychen.com/ddr-hbm-token-economics-nvidia-lock-supply-chain/)
  * [DeepSeek V4 Million Token CSA / HCA Attention 技術解析](https://ai-coding.wiselychen.com/deepseek-v4-million-token-csa-hca-attention/)
  * [非英語稅：你用 Claude 寫中文比美國人貴 71%](https://ai-coding.wiselychen.com/non-english-tax-tokenizer-cost-claude-openai/)
  * [中國 Token 出口：賣 intelligence 的新貿易模式](https://ai-coding.wiselychen.com/china-token-export-new-trade-model-selling-intelligence/)

---

## [非英語稅：用 Claude 寫中文，同樣內容 token 比英文版多 71%](https://ai-coding.wiselychen.com/non-english-tax-tokenizer-cost-claude-openai/)
*🏢 Wisely Chen AI | 2026-05-04*

# 非英語稅：用 Claude 寫中文，同樣內容 token 比英文版多 71%

## 一張對比表，看懂為什麼你的 API 帳單比 SF 同事貴

最近有一份調研數據在 AI 圈流傳——AI 研究員 [Aran Komatsuzaki](https://x.com/arankomatsuzaki/status/1636367967306027013) 把 Richard Sutton 的經典文章 [《The Bitter Lesson》](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) 翻譯成多種語言，分別丟進 OpenAI 和 Anthropic 的 tokenizer 測 token 數，以英語為基準做對比。後來這份數據被 [Aihola 整理成報導](https://aihola.com/article/claude-tokenizer-language-tax) 廣傳，中文社群也在 [LINUX DO](https://linux.do/t/topic/2081874) 等地討論炸鍋。

做法很簡單，數據出來卻比很多人想像的差距大。

**Anthropic 模型（以英語 token 數 = 1.0 為基準）：**

語言 | Token 倍數 | 翻譯成成本含義  
---|---|---  
英語 | 1.00x | 基準  
法語 | 1.79x | 貴 79%  
中文 | 1.71x | 貴 71%  
俄語 | 2.04x | 貴 104%  
阿拉伯語 | 2.86x | 貴 186%  
印地語 | 3.24x | 貴 224%  
  
**OpenAI 模型（同樣以英語 = 1.0 為基準）：**

語言 | Token 倍數 | 翻譯成成本含義  
---|---|---  
英語 | 1.00x | 基準  
法語 | 1.30x | 貴 30%  
中文 | 1.15x | 貴 15%  
俄語 | 1.31x | 貴 31%  
阿拉伯語 | 1.31x | 貴 31%  
印地語 | 1.37x | 貴 37%  
  
這個現象在英文社群被叫做 “non-English tax”——「非英語稅」。其實學術界早就在談這件事，2023 年的一篇 arXiv 論文 [《Language Model Tokenizers Introduce Unfairness Between Languages》](https://arxiv.org/pdf/2305.15425) 就系統性地量化了這個不公平。OpenAI Developer Community 上也有 [一個經典討論串](https://community.openai.com/t/all-languages-are-not-created-tokenized-equal/216407) 在罵這件事。

意思就是，**你用非英語寫同樣內容的 prompt，要多消耗幾倍的 token** ，意味著更高的 API 成本、更慢的響應速度、更容易撞上下文窗口的上限。

而且不是兩家平均地貴。**Anthropic 對非英語的稅率，明顯比 OpenAI 重很多。**

我看到這個數據的第一反應是：「啊，原來不是我感覺的問題」。

我用 Claude Code 寫過上百萬 token 的中文 prompt，也用 OpenAI 處理過大量中文文件。體感一直就是 Claude 處理中文比較燒錢，但一直沒去算。這份數據把我的體感量化了——而且更慘。

* * *

## ⚠️ 兩個你必須知道的 Caveat

在繼續讀下去之前，我必須先講三件事，不然這篇文章會誤導你。

### Caveat 0：「71%」這個數字的基準是什麼

先把基準講清楚再讀下去。上面那兩張表的 1.0x 是**各家 tokenizer 自己處理英文的 token 數** ——Anthropic 英文 = 1.0、OpenAI 英文 = 1.0，**不是用同一把尺** 。

所以「Claude 中文 1.71x」這個數字的意思是：**Claude 中文 token 數，是 Claude 英文 token 數的 1.71 倍** 。也就是「同一家公司內部，中文比英文多吃 71%」。

如果改用 OpenAI 英文當共同基準，原始數據裡 Anthropic 英文約 1.04 倍 OpenAI 英文，重新換算 Claude 中文 ÷ Claude 英文 ≈ 1.64x，差距就變 64%。所以你看到不同來源寫「貴 65%」「貴 71%」其實是同一個現象，只是基準不同。

我這篇文章後面用的都是 Anthropic 內部基準（1.71x = 71%），因為**對企業做選型來說，「Claude 中文比 Claude 英文貴多少」比「Claude 中文比 OpenAI 英文貴多少」更貼近實際的 API 帳單比較場景** 。但你看到別人寫 65% 不要覺得衝突，是基準不同。

另外要強調：**71% 不是「每個中文字逐字貴 71%」** 。它是「同一段語義內容翻譯成中文後，token 數的平均倍數」。「的」「是」這種高頻字可能還是 1 token，「龘」這種冷字才會吃到 3 個。所以這是**語義內容層級的平均倍數** ，不是逐字稅率。

### Caveat 1：這份數據沒被獨立審計

Aran Komatsuzaki 的測試是社群整理的非正式 benchmark，**沒有任何第三方獨立驗證** 。原因很現實——**Anthropic 從來不公開現行 tokenizer** 。

你想自己跑一次都跑不了。社群只能用反推：[javirandor/anthropic-tokenizer](https://github.com/javirandor/anthropic-tokenizer) 這個 GitHub repo 是社群透過觀察 generation stream 反推出來的近似版本，[Hacker News 的這個討論串](https://news.ycombinator.com/item?id=40711374) 還挖出 Anthropic 自己 repo 裡塞了一份 Claude 3 tokenizer。

所以 1.71x、3.24x 這些確切數字，**請當成方向性參考，不是法庭證據** 。

唯一比較靠譜的可重現 benchmark 是 [vfalbor/llm-language-token-tax](https://github.com/vfalbor/llm-language-token-tax) 這個 repo，但它只測 OpenAI 的 cl100k 跟 o200k，沒測 Anthropic（因為前面講的原因）。它的 OpenAI 中文倍數是 1.33x，跟 Komatsuzaki 的 1.15x 有差距，可能是用了不同 tokenizer 版本（cl100k vs o200k）或不同文本。

### Caveat 2：Opus 4.7 換了 tokenizer，但官方說的方向跟你想的不一樣

2026/4/16 Anthropic 發布的 [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) 換了新 tokenizer。我第一次看到這個更新時，直覺是「啊，他們要修非英語稅了」。

但實際讀官方 [migration guide](https://docs.claude.com/en/docs/about-claude/models/migrating-to-claude-4) 跟 release notes，方向跟我想的不一樣：

> **「同樣輸入在 Opus 4.7 上的 token 數可能變成 1.0–1.35 倍，請重新評估你的 token budget。」**

注意這個方向——**Anthropic 自己警告的是 token 數可能「增加」最多 35%，不是降低** 。新 tokenizer 對非英語有沒有改善？官方文件**沒有給數字** 。

社群有些二手報導（[VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)、[MindStudio](https://www.mindstudio.ai/blog/claude-opus-4-7-review)）寫新 tokenizer「對非拉丁文字更友好」，但這跟官方原文有溫差。我寫第一版的時候直接引用了這些二手數字（中日韓阿印降 20-35%），但回頭查 Anthropic 官方公告跟 migration guide，這個說法**沒有官方背書** ，我修掉了。

**結論：是否改善中文稅，需要拿你自己的 production prompt 實測。** 不能用「Opus 4.7 = 中文友好」這種廠商行銷話術直接推論，方向有可能是反過來的。

要驗證 5 分鐘就能跑：用 [Anthropic 的 count_tokens API](https://platform.claude.com/docs/en/build-with-claude/token-counting) 拿同一段中文分別打 `claude-sonnet-4-6` 跟 `claude-opus-4-7`，比對 token 數差距。

另一個 load-bearing 假設：**Opus 4.7 release notes 主要在講 Opus，沒明確說明 Sonnet 4.5/4.6 是否同步換 tokenizer** 。我發稿前沒跑完整 benchmark，所以接下來成本計算用 Sonnet 4.5 + Komatsuzaki 的 1.71x（這也是 production 主流情境）。**如果你發現 Sonnet 4.6 token 數實測跟 4.5 有差異，這篇後面的數字要折算** 。

* * *

## 這不是 bug 是 feature：BPE Tokenizer 的英文偏見

為什麼會這樣？要從 tokenizer 講起。

LLM 不是一個字母一個字母讀的，它是把文字切成 “token” 再讀。[BPE（Byte Pair Encoding）](https://en.wikipedia.org/wiki/Byte_pair_encoding) 這套 tokenizer 演算法，會根據訓練資料裡的字元頻率，把常見的字元組合合併成單一 token。想直觀感受 tokenizer 怎麼切你的文字，OpenAI 有 [官方 tiktokenizer 工具](https://platform.openai.com/tokenizer)，Anthropic 則可以用 [Lunary 的 Claude tokenizer](https://lunary.ai/anthropic-tokenizer) 或 [Token counting API](https://platform.claude.com/docs/en/build-with-claude/token-counting)。

英文有個天然優勢：**26 個字母 + 高度結構化的 subword pattern** 。”unbelievable” 雖然 12 個字母，但 BPE 會把它切成 “un” + “believ” + “able” 三個 token。

中文不一樣。中文 4-5 萬個常用字，每個字本身就是語義單位。但 tokenizer 訓練時看到的中文資料相對少，所以很多中文字會被切成 2-3 個 byte-level token。一個「龘」字可能就吃掉 3 個 token，因為它在訓練資料裡出現次數太少，根本沒被合併。Ivan Krivyakov 的 [這篇實驗筆記](https://ikriv.com/blog/?p=5322) 跟 [PromptCost 的拆解](https://promptcost.org/blog/llm-tokenization-explained/) 都把這個機制講得很清楚。

**Anthropic 比 OpenAI 慘的原因，就是 vocab size 跟訓練資料的多語言比例。**

OpenAI 的 [cl100k_base 系列 tokenizer](https://github.com/openai/tiktoken)，大概是 100K vocab，訓練資料的多語言佔比較高（GPT-4o 之後升級到 [o200k_base](https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py)，更友好）。Anthropic 公開資訊較少（[官方 API 文件](https://platform.claude.com/docs/en/build-with-claude/token-counting) 只給 count_tokens API，不給 vocab），但從這個倍數可以反推——他們的 tokenizer 對非英語的覆蓋確實比較弱，或者說，**他們是用英語使用者的視角優化的** 。

印地語 3.24x 不是隨機數字。印地語用的是 Devanagari 字符（天城文），這套字符在 byte-level 編碼下每個字符就要 3 個 byte。如果 tokenizer 沒有針對性合併常見字符組合，一個印地語句子的 token 數會很可怕。

阿拉伯語 2.86x 同理，Arabic script 加上連字（ligature）特性，tokenizer 處理不好就會爆 token。

這不是惡意，是優先級問題。**在訓練 tokenizer 的時候，你要決定 vocab 的 100K 個位子分給誰** 。給英文 subword 多一點，benchmark 上看起來更好；給其他語言多一點，會犧牲英文 efficiency。

Anthropic 顯然選了前者。

* * *

## 算給你看：一個典型台灣企業的真實帳單差距

理論講完，看實際成本。

假設你是一家台灣的金融業，做一個中文客服 chatbot：

  * **每天處理 conversations：** 10,000 通
  * **每通平均 input：** 500 token（英語基準下）
  * **每通平均 output：** 200 token
  * **語言：** 100% 繁體中文



用 [Claude Sonnet 4.5](https://platform.claude.com/docs/en/about-claude/pricing)（$3/MTok input, $15/MTok output）跑：
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

| 
    
    
    中文 input token = 500 × 1.71 = 855 token/通
    中文 output token = 200 × 1.71 = 342 token/通
    
    每通成本 = 855 × $3/1M + 342 × $15/1M
            = $0.00257 + $0.00513
            = $0.0077
    
    每天成本 = $77
    每月成本 = $2,310
      
  
---|---  
`

換成 [GPT-4o](https://openai.com/api/pricing/)（$2.5/MTok input, $10/MTok output）：
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

| 
    
    
    中文 input token = 500 × 1.15 = 575 token/通
    中文 output token = 200 × 1.15 = 230 token/通
    
    每通成本 = 575 × $2.5/1M + 230 × $10/1M
            = $0.00144 + $0.00230
            = $0.0037
    
    每天成本 = $37
    每月成本 = $1,121
      
  
---|---  
`

換成 [DeepSeek V3](https://api-docs.deepseek.com/quick_start/pricing)（中文 tokenizer 友好，約 $0.27/MTok input, $1.1/MTok output）：
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

| 
    
    
    中文 input token ≈ 500 × 0.95 = 475 token/通（中文比英文還省）
    中文 output token ≈ 200 × 0.95 = 190 token/通
    
    每通成本 = 475 × $0.27/1M + 190 × $1.1/1M
            = $0.00013 + $0.00021
            = $0.00034
    
    每天成本 = $3.4
    每月成本 = $102
      
  
---|---  
`

> **註：DeepSeek 的 0.95x 中文倍數是估計值。** DeepSeek 官方沒公布 tokenizer 多語言 benchmark，這個數字是社群實測的概略區間（多半落在 0.9–1.0x 之間）。直覺上合理——DeepSeek 訓練資料以中文為主，tokenizer vocab 對中文 subword 覆蓋密度高。但**精確數字請拿自家 prompt 實測** ，我給這個 0.95x 是為了方便對比，不是法庭證據。

**同樣的中文 chatbot，月帳單差距：Claude $2,310 vs OpenAI $1,121 vs DeepSeek $102。**

但這個差距要拆開看，不能全部歸因到非英語稅，不然會誤導讀者「換家就省 20 倍」。實際拆解：

**Claude → OpenAI（$2,310 → $1,121，2.06x 差距）**

  * 單價差距：Claude Sonnet $3 vs GPT-4o $2.5（input）= 1.2x
  * Tokenizer 稅差距：Claude 中文 1.71x vs OpenAI 中文 1.15x = 1.49x
  * 乘起來 ≈ 1.79x，加上 output token 單價差（$15 vs $10）拉到約 2x



**所以換 OpenAI 真正省到的，主要是 tokenizer 稅 1.5x + 單價 1.2x，合計 2 倍左右。** 不是 20 倍。

**Claude → DeepSeek（$2,310 → $102，22.6x 差距）**

  * 單價差距：Claude Sonnet $3 vs DeepSeek $0.27（input）= **11.1x** （這是模型本身的定價差，跟 tokenizer 完全無關）
  * Tokenizer 稅差距：Claude 1.71x vs DeepSeek 0.95x = 1.8x
  * 乘起來 ≈ 20x，加上 output 單價差距（$15 vs $1.1）最終約 22x



**這個 22x 裡面，tokenizer 貢獻 1.8x，模型單價貢獻 11x。** 真正的暴力差距是模型單價，不是 tokenizer 稅。要享受這個 11x，你付的代價是 compliance 風險（資料出境）跟一些品質差距。

而且這還只算了單價跟 token 倍數。沒算 latency，沒算 context window 撞上限被迫 truncate、被迫多輪對話的次數、被迫做 summarization 的額外成本。

* * *

## 印地語、阿拉伯語：非英語市場的企業都該重新算這筆帳

3.24x 是什麼概念？

如果你是印度的 startup，做一個印地語的法律諮詢 agent，每次 API call 比同樣英語場景多吃 2.24 倍 token。如果產品的 ARPU 又比美國市場低，這個 token 稅在 unit economics 裡就變成需要認真對待的成本項——不是「順便處理一下」可以帶過的。

這就是為什麼**印度本土做 Indic 深度應用的團隊** ——法律、醫療、教育、政府服務這類需要深度印地語（含其他 22 種印度官方語言）理解的場景——很多走自訓路線，[Sarvam AI](https://www.sarvam.ai/)、[Krutrim](https://www.olakrutrim.com/) 是代表案例，常採用 [Llama](https://www.llama.com/)、[Mistral](https://mistral.ai/) 開源 weights 做 fine-tuning。

範圍要講清楚——**印度一般 SaaS 公司** （Zoho、Freshworks、Postman 這類）依然大量使用 OpenAI / Claude，因為他們的工作語言主要還是英文、處理的多半也是英文場景。**只有任務需要深度印地語理解** ，3.24x 的 token 稅才會明顯壓縮 unit economics，讓自訓 / 開源 fine-tuning 變成更值得考慮的選項。不是民族主義，是經濟學。

阿拉伯語也是一樣。沙烏地、阿聯的政府投資 AI 蓋自己的模型（[Falcon](https://falconllm.tii.ae/)、[Jais](https://inceptionai.ai/jais/)），表面上是技術自主，底層也跟這個 token 經濟學脫不了關係——每次跑阿拉伯語就吃 2.86x 稅，做大規模消費級應用的成本結構會被改變。

但這篇文章的重點，**其實不只是印度跟中東** 。

如果你是台灣、香港、日本、韓國、東南亞、拉美的公司，做的產品有大量目標語言不是英文的場景——你都該停下來重新算這筆帳。Anthropic 是不是貴 1.71x、2.86x、3.24x，要拿你自己的 production prompt 實測。算完之後值不值得繳這筆稅，**取決於你的任務價值密度跟 ARPU** ：

  * 高價值低 volume（核心 PRD、策略文件、複雜 coding）→ 即使 1.71x 也值得
  * 中價值中 volume（一般客服、文件處理、批次摘要）→ 1.71x 開始痛，要考慮 routing
  * 低價值高 volume（純中文資料清洗、批次分類、embedding 預處理）→ 這個區段繼續用 Claude 是燒錢



對比之下，**OpenAI 的 1.31x 印地語倍數，是 Anthropic 的不到一半** 。這也部分解釋了為什麼 OpenAI 在新興市場滲透率比 Anthropic 高。Anthropic 在英語企業市場很強，但企業市場集中在英語區。

這不是巧合，是 tokenizer 設計選擇的累積結果。

* * *

## 中國模型的反向優勢：你不只省錢，你也省 context window

當對比擴展到 [Gemini](https://ai.google.dev/gemini-api/docs/pricing)、[Qwen](https://qwenlm.github.io/)、[DeepSeek](https://api-docs.deepseek.com/)、[Kimi](https://platform.moonshot.cn/)，覆蓋中文、日語、韓語、西班牙語、法語、德語、俄語、阿拉伯語、印地語等多個語言，結論更清晰了：

**主流中文模型處理中文比英文便宜。**

這不只是價格問題。Token 倍數低意味著兩件事：

  1. **單筆 API 成本低** ——直接的成本優勢
  2. **同樣的 context window 能塞更多內容** ——隱形的能力優勢



第二點被嚴重低估。

舉個例子：你要做一個 RAG 系統，retrieve 多份中文 PDF 餵給模型。

中文文件實際吃多少 token，**沒辦法用「字數 × 1.71」這種公式估** ——1.71x 是「英文翻成中文後 token 倍數」的對比，不是「中文字數轉 token 的轉換率」。要精確估必須拿真實文件丟 token counter 跑一次。

但結構上你可以這樣理解：**Claude 的 200K context 數字看起來是 DeepSeek 128K 的 1.5 倍，但折算 tokenizer 對中文的處理效率差距，實際處理中文場景的「可用空間」差距會大幅縮小，甚至可能反轉** ——同樣一份中文 PDF 餵進 Claude 跟 DeepSeek，Claude 吃到的 token 數明顯較多。

所以中文 RAG 場景下，看 context window 不能只看廣告數字（200K vs 128K），要折算 tokenizer 效率。我自己實測過幾份金融研究報告，原本以為 Claude 200K 一定夠塞，結果撞到 truncation 的次數比預期多很多。

這就是為什麼你會看到中國的金融、法律、醫療領域大量採用 DeepSeek、Qwen——不是因為「國產替代」的口號，是因為在他們的語言場景下，數學就是這樣。

* * *

## What didn’t work smoothly：Claude 仍然值得的時候

寫到這裡，你以為我要勸你全部切換到 OpenAI 或 DeepSeek。

不是。我自己現在主要用的還是 Claude（Claude Code、Claude Sonnet 4.6）。

我來坦白幾個 Claude 仍然值得貴 1.71x 的場景：

**1\. 推理密度高的任務**

寫一個複雜的 PRD 或 architecture review，Claude Sonnet 4.5 / Opus 4 的輸出品質仍然明顯高於 GPT-4o。我做過的測試：同樣的輸入，Claude 一次到位，GPT 需要 2-3 輪 refine。**Token 倍數帳算下來反而 Claude 更省。**

**2\. Coding 場景**

Claude Code 對 codebase 的理解和 multi-file edit 能力，目前沒有對手。即使每個 prompt 多吃 71% token，但完成一個 task 需要的 prompt 次數可能少 50%。**整體 token 總量未必更多。**

**3\. 長文本理解**

雖然 Claude 處理中文倍數高，但 200K context 的「實際可用容量」對複雜文件分析仍然夠用。換到 GPT-4o 的 128K，撞上限的次數更多。

**4\. Tool use 跟 agent loop**

Claude 的 tool use 訓練做得比較細，agent loop 在意外狀態下的 recovery 比較好。這個品質差距在 production 是真金白銀的差距——一次 agent 跑掛，工程師 debug 1 小時的成本，遠遠超過省下的 API token 錢。

**所以非英語稅是真的，但不是「換一家就好」的問題。**

它是一個 **trade-off matrix** ，不是 single answer。

* * *

## 三層策略：別 all-in 任何一家

我自己跟客戶談 LLM 選型時，現在會用三層策略：

**Tier 1｜高價值、低 volume 的核心任務**

  * 用 [Claude Sonnet 4.5](https://platform.claude.com/docs/en/about-claude/models/overview) 或 [Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)（後者換了新 tokenizer，但官方沒明確給非英語的改善幅度，自己實測比較保險）
  * 場景：策略文件、PRD、architecture design、核心 coding
  * 心態：認賠 71% 中文稅（Sonnet 基準），因為品質差距 > token 差距。Opus 4.7 對中文是否真的省，跑 [count_tokens API](https://platform.claude.com/docs/en/build-with-claude/token-counting) 確認過再決定要不要升級



**Tier 2｜中等價值、中 volume 的標準任務**

  * 用 [GPT-4o](https://openai.com/api/pricing/) 或 [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/pricing)
  * 場景：客服回覆、文件 summarization、一般問答
  * 心態：1.15x 中文稅可以接受，速度跟成本是 sweet spot



**Tier 3｜低單價、高 volume 的批次處理**

  * 用 [DeepSeek V3](https://api-docs.deepseek.com/quick_start/pricing) 或 [Qwen 2.5 Max](https://qwenlm.github.io/blog/qwen2.5-max/)
  * 場景：批次 OCR 後處理、大量資料清洗、純中文場景的 embedding 預處理
  * 心態：中文 token 反而比英文省，價格也最低，這個層級不用 Claude / OpenAI 是浪費錢



關鍵是：**不要用單一模型解決所有事。**

很多企業的 AI 帳單失控，不是因為用錯模型，是因為用同一個模型做所有事——把 Claude Opus 拿去做 OCR 後處理、拿去做客服 FAQ 匹配，這就是用 7-11 御飯糰的價錢買法國米其林三星。

我們團隊現在的 production 流程，**至少混用 3-4 個模型** 。Routing 邏輯多寫一點，月帳單差 5-10 倍很正常。

* * *

## 最後想說

非英語稅這個現象，技術上不是新發現。tokenizer 的 multilingual fairness 問題，學術界討論很多年了。

但這個數據之所以值得寫，是因為它把一件本來只有研究員在意的事，變成了**任何亞洲企業在做 LLM 選型時都該算清楚的成本項** 。

如果你的核心市場是英語區，這篇文章對你影響不大。

如果你的核心市場是中文、日韓、東南亞、印度、中東——你正在被收一筆隱藏的稅。**不知道，不代表沒繳。**

最後再強調一次前面講的三個 caveat：

  1. **基準要講清楚** ——表格的 1.0x 是各家自己的英文 token 數，不是同一把尺。「Claude 中文 1.71x」是相對 Claude 英文，不是相對 OpenAI 英文。所以你看到別家寫 65% 不要覺得衝突，是基準不同。
  2. **Komatsuzaki 的數字沒被獨立審計** ——確切倍數請當參考，不要當聖經。要精確算，自己拿真實 prompt 跑 [Anthropic 的 token counter](https://platform.claude.com/docs/en/build-with-claude/token-counting) 跟 [OpenAI 的 tiktokenizer](https://platform.openai.com/tokenizer)。
  3. **Opus 4.7 換了 tokenizer，但是否改善中文稅還沒驗證** ——Anthropic 官方反而提醒同樣輸入可能多吃 1.0–1.35x token。Sonnet 4.5/4.6 是否同步換沒明確說明，建議發稿前自己 5 分鐘 benchmark 確認。



但「Anthropic 對非英語比 OpenAI 重」這個方向性結論，**跟我自己用了兩年的體感完全一致** 。

下次跟你的 CTO 報 Claude 帳單時，記得加一句：「我們處理中文比英文多吃了 71% 的 token，這是 Anthropic tokenizer 對非英語的稅。如果我們的目標市場是中文，這筆稅該不該繳，要看每個任務的價值密度。要不要升 Opus 4.7 換新 tokenizer 試試看？官方沒給保證，我們自己跑個 benchmark 比對 Sonnet 4.6 跟 Opus 4.7 的中文 token 數，5 分鐘有結論。」

這比「Claude 太貴了我們換 OpenAI」要 professional 太多。

* * *

## 延伸閱讀

**原始數據與報導：**

  * [Aran Komatsuzaki 在 X 上對多家 tokenizer 的早期觀察](https://x.com/arankomatsuzaki/status/1636367967306027013)
  * [Aihola — Claude Tokenizer Language Tax 報導](https://aihola.com/article/claude-tokenizer-language-tax)（2026/4/28）
  * [LINUX DO 中文社群討論：Claude 的中文稅](https://linux.do/t/topic/2081874)
  * [vfalbor/llm-language-token-tax — 可重現 OpenAI tokenizer benchmark](https://github.com/vfalbor/llm-language-token-tax)



**Anthropic Opus 4.7 新 tokenizer 相關：**

  * [Anthropic 官方公告：Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
  * [VentureBeat：Anthropic Opus 4.7 narrowly retaking lead](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)
  * [MindStudio：Opus 4.7 Review — What Actually Changed](https://www.mindstudio.ai/blog/claude-opus-4-7-review)
  * [Claude Opus 4.7 Release Tracker (findskill.ai)](https://findskill.ai/blog/claude-opus-4-7-release-tracker/)
  * [Claude API 官方定價頁](https://platform.claude.com/docs/en/about-claude/pricing)



**學術背景：**

  * [arXiv 2305.15425 — Language Model Tokenizers Introduce Unfairness Between Languages](https://arxiv.org/pdf/2305.15425)
  * [Richard Sutton — The Bitter Lesson（被拿來測試的原文）](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)



**Tokenizer 工具：**

  * [OpenAI tiktokenizer](https://platform.openai.com/tokenizer) / [tiktoken GitHub](https://github.com/openai/tiktoken)
  * [Anthropic 官方 Token counting API](https://platform.claude.com/docs/en/build-with-claude/token-counting)
  * [Lunary Anthropic Tokenizer 工具](https://lunary.ai/anthropic-tokenizer)
  * [javirandor/anthropic-tokenizer — 社群反推的 Claude tokenizer](https://github.com/javirandor/anthropic-tokenizer)
  * [Hacker News — Anthropic 自己 repo 裡的 Claude 3 tokenizer](https://news.ycombinator.com/item?id=40711374)



**其他相關拆解：**

  * [Ivan Krivyakov — LLM Tokens and Foreign Languages](https://ikriv.com/blog/?p=5322)
  * [PromptCost — LLM Tokenization Explained: English vs Other Languages](https://promptcost.org/blog/llm-tokenization-explained/)
  * [OpenAI Developer Community — All languages are NOT created (tokenized) equal](https://community.openai.com/t/all-languages-are-not-created-tokenized-equal/216407)



**模型 / 廠商連結：**

  * [Claude Models Overview](https://platform.claude.com/docs/en/about-claude/models/overview)
  * [OpenAI API Pricing](https://openai.com/api/pricing/)
  * [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
  * [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing)
  * [Qwen 2.5 Max](https://qwenlm.github.io/blog/qwen2.5-max/)
  * [Moonshot Kimi 平台](https://platform.moonshot.cn/)
  * [Sarvam AI（印度 Indic 模型）](https://www.sarvam.ai/) / [Krutrim](https://www.olakrutrim.com/)
  * [Falcon LLM（UAE）](https://falconllm.tii.ae/) / [Jais（沙烏地）](https://inceptionai.ai/jais/)



* * *

## 常見問題 Q&A

**Q: 這個倍數會隨模型版本改變嗎？**

會。Tokenizer 通常跟著模型大改版才換，但每次換 tokenizer 倍數都可能變。建議自己拿真實 prompt 用各家的 tokenizer 算一次，最準。

**Q: 為什麼 OpenAI 的中文倍數比 Anthropic 低這麼多？**

主要是 vocab size 跟訓練資料的多語言比例。OpenAI cl100k 系列對中文 subword 覆蓋較好。Anthropic tokenizer 細節公開較少，但從倍數可以反推他們對非英語的優化優先級較低。

**Q: 用 prompt cache 能不能抵消非英語稅？**

可以部分抵消。[Anthropic 的 prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) 對重複前綴有 90% 折扣，所以高重複率場景（agent system prompt、固定 RAG context）會大幅降低 effective cost。但動態 user input 的部分稅照繳。我之前寫過 [一篇關於 KV Cache 怎麼省 80% token 的文章](https://ai-coding.wiselychen.com/kv-cache-gemma4-claude-code-save-80-percent-token/) 可以參考。

**Q: 如果我做的是中英文混合 prompt，倍數怎麼算？**

按比例加權平均。一個 70% 中文 + 30% 英文的 prompt，用 Claude 約 1 × 0.3 + 1.71 × 0.7 ≈ 1.50x。實務上建議拆 system prompt 用英文（讓 model 理解 task）+ user data 用原文。

**Q: 用中國模型有 compliance 顧慮怎麼辦？**

不要 production 接 DeepSeek 公開 API（資料出境問題）。用 [開源權重](https://huggingface.co/deepseek-ai) 自己 host，或用台灣 / 香港的 cloud provider 提供的 inference endpoint。[Qwen 開源版本](https://huggingface.co/Qwen) 可以完全 on-prem，這個議題我在 [本地 LLM 企業架構這篇](https://ai-coding.wiselychen.com/local-llm-enterprise-architecture/) 講得更完整。

---
