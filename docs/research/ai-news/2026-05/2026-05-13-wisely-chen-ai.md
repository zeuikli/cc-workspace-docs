---
title: Wisely Chen AI — 2026-05-13
date: 2026-05-13
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-05-13

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [73% 的工程師正在用 AI 讓自己變笨——Cognitive Surrender 的真相](https://ai-coding.wiselychen.com/cognitive-surrender-ai-coding-comprehension-debt/)
*🏢 Wisely Chen AI | 2026-05-12*

我先講一個讓我有點不舒服的數字。

賓夕法尼亞大學的研究員 Shaw 和 Nave 做了一個叫做 [Thinking - Fast, Slow, and Artificial](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646) 的研究，1,372 位受試者，超過 9,500 個試驗。

設計很簡單：讓受試者做判斷題，一組有 AI 輔助，一組沒有。AI 給的答案裡，**有一半是故意錯的** 。

數字如下：

  * **73.2%** 的情況下，受試者接受了 AI 有缺陷的推理
  * 只有 **19.7%** 的情況下，人們會推翻 AI 的答案
  * 當 AI 明確給出錯誤答案時，人們仍然有 **80%** 的時候接受了它
  * 使用 AI 的受試者，對自己答案的信心**高出 11.7%** ——即使 AI 答錯了一半



更讓人不安的是信心效應。用一個錯一半的系統，還覺得自己比完全不用 AI 的人更準——**這是一個讓人越來越不知道自己不知道什麼的系統** 。

還有一個發現，我覺得對工程師特別有感：**時間壓力讓人少了 12 個百分點抓到 AI 錯誤的機率** 。反過來，給了明確的金錢激勵和即時反饋，人們多了 19 個百分點去抓錯誤。

這個 time pressure 的發現很重要。很多公司引入 AI 的理由就是「加速交付」，工程師在更快的 deadline 下使用 AI——而這正好是最容易接受錯誤、最難察覺問題的使用條件。

這個研究讓我回想起幾個月前發生在我自己身上的一件事。

## 那次我沒有想清楚

在帶跨國團隊的時候，有一次碰到一個架構決策：某個 batch job 要跑的東西，到底要用 message queue 還是直接 function call？

我問了 [Claude Code](https://ai-coding.wiselychen.com/claude-code-630k-lines-three-months-reflection/)，它給了一個很漂亮的分析：延遲容忍度、背壓控制、觀測性……洋洋灑灑，每一點都有邏輯。

我看了大概兩分鐘，然後說：「好，用 queue。」

之後有個工程師問我：「那個 queue 的 consumer 怎麼 scale？」

我愣了一下。

我知道「應該用 queue」，但我完全沒有想過 consumer 的 scale 策略。那個答案是 Claude Code 告訴我的，我只是轉述了它的結論，沒有真的把這個架構消化成自己的理解。

這就是 **Cognitive Surrender** ，認知投降。

## Cognitive Surrender vs Cognitive Offloading

[Addy Osmani](https://addyosmani.com/blog/cognitive-surrender/)（Google Chrome 技術長）在他的文章裡面做了一個很重要的區分，我覺得值得每個 AI 重度用戶都認真看一遍：

**Cognitive Offloading（認知卸載）** ：把任務交給 AI，但我自己同時在建立理解，保持獨立判斷的能力。

**Cognitive Surrender（認知投降）** ：整包接受 AI 的輸出，不形成自己的理解，用 AI 的信心替代我自己的推理。

差別聽起來很細，但後果差很多。

卸載是工具使用，投降是能力轉移。卸載之後你還在，投降之後……你還在，但你慢慢不知道自己懂什麼了。

## 工程師最容易投降的四個地方

Osmani 列出了四個在軟體開發裡特別危險的投降點，我一個一個對照了我自己的情況：

**1\. Code Review**

你有沒有看過一個 600 行的 PR，測試都過了，AI 說看起來沒問題，然後你就 approve 了？

我有。而且不只一次。

測試過不代表邏輯對，測試過不代表你看懂了這段程式碼在幹嘛。這是最常見的投降點，因為有一個「通過測試」的假陽性在給你安全感。（延伸閱讀：[AI Coding 的驗收流程怎麼做？](https://ai-coding.wiselychen.com/atpm-qa-ru-he-yan-shou-ai-coding-de-cheng-shi/)）

**2\. Error Debugging**

「為什麼這個 null pointer exception 出現在這裡？」

AI 說：「在第 47 行加一個 null check。」

你加了，問題消失了，繼續往前走。

但你知道為什麼 null 出現在那裡嗎？不知道。下次同樣的 bug 出現在別的地方，你還是不知道。每一次這樣修，你就積累了一點「理解缺口」。

**3\. Architecture Decisions**

這是我剛才說的那個故事。最危險的一種，因為架構決策的影響最長遠，但也是 AI 最容易給出聽起來有道理的答案的地方。

問題不是 AI 說的對不對，問題是你自己有沒有消化成「你的理解」。

**4\. 學習階段**

這個是反直覺的。

你在學一個新技術，用 AI 生成程式碼來「看看怎麼寫」——這反而是學習效率最差的方式。研究發現，**用 AI 生成模式學習的人，理解分數比用提問模式學習的人低 17%** 。

讀 AI 給你的答案，跟自己先想然後問 AI 對不對，是完全不同的認知活動。

## 理解債

我很喜歡 Osmani 用的這個詞：**Comprehension Debt，理解債** 。

技術債大家都懂：今天為了趕時間少做了一些設計，之後要加倍還。

理解債類似，但更難察覺：**你的程式碼量在增加，但你對系統的真實理解在萎縮。**

MIT 有研究發現，習慣用 AI 的工程師出現了神經連結度下降和記憶重建能力減弱的現象。聽起來很誇張，但你想想：每一次你選擇讓 AI 替你想，你自己的那條神經路徑就少走一次。

而且這個債是複利的。每一次投降，下一次投降就更容易，因為你越來越不確定自己能不能獨立判斷。

## 怎麼知道自己是不是已經在線上了？

在講怎麼對抗之前，先說怎麼診斷。以下五個訊號，出現任何一個，你很可能已經在認知投降的軌道上：

**1\. 600 行 PR，掃了一遍就 approve** 「測試是通過的」不等於 review。你如果說不出這個 PR 改了什麼、為什麼這樣改，你沒有在 review，你在蓋章。

**2\. Bug 修了，但不知道為什麼修的** 你加了那行 null check，問題消失了，繼續往前走。但兩週後，同樣的問題會以新的形式回來找你。

**3\. 為某個決策辯護，重建不出 why** 開會時有人問你為什麼選這個方案，你說的是「當時看起來合理」或「agent 說這樣比較好」——你借用了 AI 的信心，但那個 why 從來不是你的。

**4\. 沒有 agent 時，不太敢動鍵盤了** 你獨自寫程式的能力，是你真實水位的體溫計。如果這個能力在萎縮，你知道發生了什麼。

**5\. 系統壞了，第一反應是「再讓 agent 修」** 不再有「從第一性原理出發，這個問題應該怎麼解決」這個步驟。投降已經變成預設反應，不是主動選擇。

出現紅色訊號的時候，立刻做一件事：**關掉 agent，拿紙或開新文件，手動重建你跳過的那段 why。** 不是懲罰自己，是把你的理解補回來。

* * *

## 五條護身術

我不是說不要用 AI，我現在每天都大量使用 Claude Code（[三個月 63 萬行的反思在這裡](https://ai-coding.wiselychen.com/claude-code-630k-lines-three-months-reflection/)）。

但在某幾個場景，我現在會刻意加一道防線：

**① 先寫預期**

看 AI 輸出之前，心裡先有個答案。哪怕只是「我覺得這邊應該回傳 null」，或者「這個 query 大概會跑三行還是五十行」。有了預期，當 AI 說別的東西的時候，你就自動進入「為什麼不同」的模式，而不是接受模式。不一致的那一刻，才是真正的判斷時刻。

**② 當不是 AI 寫的來讀**

看到一個 PR，先假設這是實習生提的。「測試通過」你就直接 merge 嗎？「看起來沒問題」算 review 嗎？用同樣的標準對 AI 生成的程式碼，不要因為它是機器寫的就降低你的驗收門檻。

**③ 讓模型反駁它自己**

「給我一個相反的、同樣有說服力的論點。」

這句話很便宜，但能擊穿借來的信心。每次你分不清楚要用哪個方案的時候，其實是你已經快要投降的訊號——這個時候就請 AI 反駁它自己，強迫你去評估兩邊，而不是被動接受最先聽到的那個。

**④ 注意疲勞**

認知投降是疲勞現象。早上第一個 PR 你認真看，第五個你一眼掃過。累到無法評估的時候，你不是在用 AI 加速，你是在讓 AI 替你決定。

疲勞的時候不要讓 agent 繼續生成，要去休息。

**⑤ 看自信從哪裡來**

開會為某個決策辯護的時候，你能重建 why 嗎？還是只記得「agent 這樣說，聽起來合理」？

如果說不出來，那個信心是借來的。把 agent 關掉，回去把 why 自己重建出來。

* * *

**核心自檢，一句話：我是在獨立形成觀點，還是在原封不動接受 agent 的視角？**

## 個人意志不夠，還需要結構：Harness Engineering

上面五條護身術是個人層面的東西。但有一個殘酷的現實：**個人意志在組織規模下會失效。**

亞馬遜試圖用禁令解決這個問題：「初級和中級工程師，不得在沒有資深工程師簽字的情況下提交 AI 生成的程式碼。」方向對，但方法錯。

為什麼？因為資深工程師很快就變成了瓶頸。他們一天要審大量 AI 生成的 PR，第一個認真看，第五個快速掃過，第十個基本上只是蓋章。

這就是 Wharton 研究裡 time pressure 效應的組織版本：**你用禁令製造了一個必然產生認知投降的流水線。** 把問題從初級工程師轉移到資深工程師身上，但沒有解決。

[Harness Engineering](https://ai-coding.wiselychen.com/harness-engineering-architecture-overview-ai-code-production-guardrails/) 走的是完全不同的路。它的核心哲學是：

**Humans steer. Agents execute.**

不是靠「誰來盯」，而是靠「系統設計讓 AI 做不了某些事」。

具體來說，Harness Engineering 的重點不是阻止 AI 寫程式，而是建立結構性護欄——分級審查機制、不可逆操作的強制確認、變更範圍的硬性限制。它讓認知投降的「代價」在系統層面被攔住，不依賴每個人每次都保持高度警覺。

這跟認知投降的關係很直接：

  * **個人層面** ：五條護身術，讓你習慣保持判斷
  * **組織層面** ：Harness Engineering，讓系統不依賴個人意志



只有個人習慣，沒有組織護欄，疲勞和時間壓力遲早會讓人投降。只有組織護欄，沒有個人習慣，工程師照樣會慢慢失去獨立判斷的能力——只是失敗不會炸生產環境而已。

兩個層面都需要。

## AI 應該讓你用完更強，不是更弱

我覺得最好的 AI 使用狀態，Osmani 說的很精確：**Mutual Amplification，互相放大。**

每一次的 AI 協作，結束之後你的心智模型應該要比開始之前更清晰，不是更模糊。你不只完成了任務，你也理解了這個任務。

如果每次用完 AI，你對自己在做什麼越來越不確定，那你不是在用工具，你是在把自己的理解轉移給工具。

**「如果你的程式碼在 shipping，但你對系統的理解在萎縮，你是在用認知債支付進度。」**

這句話我之後每次 code review 之前都打算想一次。

* * *

有沒有想到你最近有沒有在某個地方投降過？

我覺得誠實回答這個問題，比任何工具選擇都更重要。

* * *

## 延伸閱讀

  * [AI 大工人用不好的真相：不是工具問題，是習慣問題](https://ai-coding.wiselychen.com/ai-dagongren-yong-bu-hao-de-zhenxiang/) — 為什麼很多人用了 AI 還是沒有變快
  * [三個月 63 萬行之後：工程師真正的價值是什麼？](https://ai-coding.wiselychen.com/claude-code-630k-lines-three-months-reflection/) — 程式碼廉價之後，剩下的是什麼
  * [ATPM：一個真實生產環境的 AI 協作流程](https://ai-coding.wiselychen.com/atpm-a-real-production-vibe-coding-process/) — 如何用框架避免被 AI 帶著走
  * [Andreessen 的 AI 時代四分之一法則](https://ai-coding.wiselychen.com/andreessen-information-diet-ai-era-quarter-rule/) — 資訊超載時代的認知管理
  * [Harness Engineering 架構全景：AI 可以寫 Code，但不能自己上 Production](https://ai-coding.wiselychen.com/harness-engineering-architecture-overview-ai-code-production-guardrails/) — 組織層面的結構性護欄怎麼建

---

## [KV Cache 量化選擇地圖：vLLM 實測後，TurboQuant 該用在哪？](https://ai-coding.wiselychen.com/turboquant-kvquant-vllm-benchmark/)
*🏢 Wisely Chen AI | 2026-05-12*

KV Cache 量化一直是個「看起來美，用起來踩坑」的領域。

論文說壓縮到 2.5-bit 只有邊際損失，工程師實測說 reasoning 任務掉了 20 分；社區說 3-bit 在 MacBook 上跑 OpenAI 開源模型絲滑流暢，部署團隊說吞吐量剩 66%。

同一個技術，沒有人說謊，只是每個人站在不同的地方看。

這週 vLLM 工程師 Eldar Kurtić（Red Hat AI）發了一篇罕見的誠實報告，橫跨 4 個模型、5 個 benchmark，把 TurboQuant 各個變體在精確度、延遲、吞吐量上都測了一遍，並且直接給出了實用建議——不是「視情況而定」，是非常具體的「什麼情境用什麼」。

這種清晰度，在 AI 工具評測裡不常見。值得認真看一下。

* * *

## TurboQuant 是什麼

先說清楚技術背景。

TurboQuant 是 Google 在 2025 年 4 月發表的論文（arXiv 2504.19874），已被 ICLR 2026 接受。核心解決的問題是 **KV Cache 的記憶體開銷** 。

現代 LLM 在推理時會把每個 token 的 Key/Value 向量暫存起來（KV Cache），讓後續 token 不用重算。問題是，長上下文下這個 Cache 會吃掉大量 GPU/RAM：一個 70B 模型處理 128K token 時，KV Cache 可以輕鬆超過 10GB。

傳統量化方式（如 FP8）已經把這個問題改善了一半，TurboQuant 想更進一步，用 2.5-3.5 bit 把 KV Cache 壓縮到極致。

**論文的核心技術：**

  1. 把向量隨機旋轉（Random Rotation），讓座標分布集中（Beta 分布）
  2. 利用高維空間中不同座標的近似獨立性，對每個座標分別做最優純量量化
  3. 加入 1-bit QJL（Quantized Johnson-Lindenstrauss）殘差校正，修正 inner product 偏差



論文聲稱的成果：

  * **3.5 bit per channel = 質量中性（absolute quality neutrality）**
  * **2.5 bit per channel = 邊際質量下降（marginal quality degradation）**
  * **最高 6x KV 記憶體壓縮，最高 8x attention 加速（H100）**



聽起來很美。

* * *

## vLLM 工程師的實測

vLLM 團隊（Eldar Kurtić + Miguel Goin, Red Hat AI）沒有跟著一起說「很美」。他們拿了真實模型跑了 5 個 benchmark。

**測試模型：**

  * Llama-3.3-70B-Instruct
  * Qwen3-30B-A3B-Instruct
  * Qwen3-30B-A3B-Thinking（thinking 版本）
  * MiniMax-M2.7（200B+ 旗艦）



**測試方法對比：**

量化方式 | KV 記憶體容量 | 精確度 | 吞吐量  
---|---|---|---  
BF16（基準） | 1x | 100% | 100%  
FP8 | **2x** | ≈100%（幾乎無損） | **≈100%**  
TQ k8v4 | 2.4x | 輕微下降 | 66-75%  
TQ 4bit-nc | 3.4x | 1-4 分下降 | 73-80%  
TQ k3v4-nc | ≈4x | 嚴重下降 | 66-75%  
TQ 3bit-nc | ≈4x | **嚴重下降** | **最差**  
  
### 精確度：3-bit 真的掉很多

最能說明問題的是 reasoning 任務：

**Qwen3-30B-Thinking 在 AIME25：**

  * BF16：正常表現
  * TQ 3bit-nc：**掉了約 20 分**



這不是邊際損失，這是實質退化。AIME 這種數學競賽題，20 分的差距代表模型在困難推理鏈上開始出錯。

**Qwen3-30B 在 256K 超長上下文（MRCR benchmark）：**

  * BF16：45.8% AUC
  * TQ 3bit-nc：31.2% AUC
  * 相對下降：**30%**



長上下文的損失更嚴重，因為 KV Cache 越大，壓縮造成的資訊損失就越累積。

### 延遲：dequantization 是隱藏成本

Eldar 解釋了原因：

**FP8 為什麼幾乎零開銷？**  
FP8 把量化操作融入 attention 計算本身（quantized attention），不需要額外的 dequantize 步驟。

**TurboQuant 為什麼有開銷？**  
TurboQuant 在計算 attention 前，必須把 KV Cache 從低 bit 儲存格式 dequantize 回 BF16，這個步驟的代價隨著 KV Cache 大小線性增長。

結果：

  * TurboQuant 所有變體：**10-68% 延遲增加**
  * 吞吐量只剩 BF16 的 **66-80%**
  * 在高並發（burst）下，Llama-70B 的 TPOT（每 token 延遲），FP8 比 BF16 快 2x，TQ 變體反而比 BF16 慢 1.5-2.5x



### 唯一勝出的場景：TTFT 在記憶體瓶頸下

TurboQuant 有一個真實的優勢。

在 Llama-70B 的高並發測試中，當 GPU 記憶體被 KV Cache 吃滿後：

  * **BF16 的 TTFT（首個 token 延遲）爆炸到 ~17 秒** （系統開始排隊）
  * **TurboQuant 所有變體維持在 3.5 秒以內** （5x 改善）



這才是 TurboQuant 真正的使用場景：**記憶體嚴重不足，且寧願犧牲精確度和吞吐量，換取「能跑」** 。

* * *

## 論文 vs. 工程：為什麼結論不一樣

這不是誰在說謊，是測試環境不同。

**論文測試的是什麼？**  
論文主要評估的是 **perplexity（困惑度）和學術 benchmark** ，在受控的記憶體和計算假設下。論文聲稱 3.5-bit 達到「質量中性」，是在特定測試集和模型下的結果。

**工程師測試的是什麼？**  
vLLM 測試的是 **生產環境的真實指標** ：reasoning 任務精確度、長上下文能力、系統吞吐量、端到端延遲。而且測試的是最先進的模型（70B, MoE, Thinking 模型）。

Eldar 在 X 上說得很直接：

> 「我們刻意避開了關於 TurboQuant 學術新穎性、與先前工作的關係、以及 QJL 效果的討論。我們的主要目標是為 vLLM 使用者提供可以幫助他們做決策的數據。」

這是工程師的誠實。他沒有說論文是錯的，他說的是「論文的結論不直接適用於你的生產環境」。

* * *

## 但是：本地推理的世界完全不同

同一週，gpt-oss-20b 在 MacBook 上跑起來了。

OpenAI 在 2025 年 8 月開源了 gpt-oss 系列：

  * **gpt-oss-20b** ：20B+ 參數 MoE，Apache 2.0 授權，原生 MXFP4 量化
  * **支援平台** ：PyTorch + Apple Metal（MLX）
  * **最低硬體要求：16GB 記憶體**



社區進一步用 TurboQuant 3-bit 量化後（GGUF tq3 格式），效果是：

  * 解碼速度：**60-80 tok/s** （M 系列 Mac）
  * 上下文長度：**131K**
  * 完全離線，無 API 費用



這個場景的決策邏輯完全不同：

**伺服器場景的問題** ：「我有 8x H100，要最大化吞吐量，KV Cache 是瓶頸嗎？」  
→ 用 FP8，不用 TurboQuant。

**本地推理的問題** ：「我的 Mac 只有 16GB，20B 模型 BF16 需要 40GB+，根本跑不起來，怎麼辦？」  
→ 3-bit 是唯一選項，accuracy 損失是可接受的 trade-off。

在本地推理的世界，**「能跑」本身就是贏** 。

* * *

## 五個 Takeaway（Eldar 的版本，加上我的補充）

**Takeaway 1（Eldar）：FP8 是 KV Cache 量化的最佳預設**  
2x 容量，零吞吐量代價，幾乎無精確度損失。如果你在跑 vLLM，先開 `--kv-cache-dtype fp8`，再考慮其他選項。

**Takeaway 2（Eldar）：TurboQuant k8v4 沒有實質優勢**  
只比 FP8 多 0.4x 容量（2.4x vs 2x），代價是 20-34% 吞吐量損失。數學不成立。

**Takeaway 3（Eldar）：TurboQuant 4bit-nc 是最實際的 TQ 變體**  
記憶體嚴重不足時，3.4x 容量 + 1-4 分精確度損失，可接受。但要先測你的 use case。

**Takeaway 4（Eldar）：3-bit 變體不適合生產**  
reasoning 任務 -20 分、長上下文 -30%，吞吐量最差。除非你完全不做推理任務。

**Takeaway 5（我的補充）：本地推理的判斷標準不同**  
對本地推理用戶而言，TurboQuant 3-bit 讓 20B+ 模型從「不可能」變成「可能」。這個技術是有意義的，只是不要拿伺服器的標準去評估它。

* * *

## 最後說一件事

TurboQuant 論文本身是否有學術創新，這個問題工程師們也在討論。

Tim Dettmers（量化領域知名研究者）和 Dan Alistarh 都提供了一些歷史背景，vLLM 的 PR 討論串也有相關討論（github.com/vllm-project/vllm/pull/40194）。

但這篇文章不是要評判論文的新穎性。

我想說的是：**量化技術現在分裂成兩個世界，有兩套評估標準。** 一套是伺服器吞吐量和生產精確度，另一套是「我的 MacBook 能不能跑這個模型」。

這兩套標準都是真實需求，只是服務不同的人。

如果你在企業部署 LLM，先用 FP8，不要被論文的 3-bit 數字吸引。  
如果你想在自己電腦上跑 20B 模型，TurboQuant 3-bit 可能正好是你需要的東西。

認清自己在哪個世界，才能做對的決定。

* * *

## 附錄：一張 Consumer GPU 能跑什麼？

既然談到本地推理，順便補一個實際問題：這次 benchmark 測的 4 個模型，在 RTX 4090 / 5090 + 64GB RAM 上能跑哪些？

**先看模型 VRAM 需求：**

模型 | BF16 需求 | 4090（24GB） | 5090（32GB）  
---|---|---|---  
Qwen3-30B-A3B（MoE） | ~60GB | ✅ INT4 ~15GB | ✅ FP8 剛好 / INT4 舒適  
Llama-3.3-70B | ~140GB | ❌ | ❌（需雙卡）  
MiniMax-M2.7（200B+） | ~400GB+ | ❌ | ❌  
  
4 個 benchmark 模型裡，consumer GPU 只能跑 **Qwen3-30B-A3B** 。

### 一張 5090（32GB）怎麼配最甜

目標 | 配法 | VRAM 分配 | 速度 | 上下文  
---|---|---|---|---  
日常使用 | INT4 + FP8 KV | 15GB 權重 ＋ 14GB KV | ~50 tok/s | 64K  
長文件分析 | INT4 + TQ 4bit-nc | 15GB 權重 ＋ 14GB KV | ~40 tok/s | 100K+  
最高精確度 | FP8 權重 + BF16 KV | 30GB ＋ 2GB | ~60 tok/s | ~2K  
  
**推薦：INT4 + FP8 KV Cache** 。15GB 放模型，14GB 放 KV Cache，64K 上下文 + 50 tok/s，對個人或小團隊夠用。64GB RAM 在這個配置下幾乎是備用——除非要跑 CPU offload（會掉到 5-12 tok/s，不推薦）。
    
    
    1
    2
    3
    4
    5
    6
    7
    

| 
    
    
    # vLLM（生產級，支援 FP8 KV + TurboQuant）
    vllm serve Qwen/Qwen3-30B-A3B-Instruct \
      --quantization awq \
      --kv-cache-dtype fp8
    
    # 或 Ollama（最省事）
    ollama run qwen3:30b-a3b
      
  
---|---  
`

* * *

**數據來源：**

  * [vllm.ai TurboQuant Benchmark](https://vllm.ai/blog/turboquant)（Eldar Kurtić, Miguel Goin, Alexandre Marques）
  * [TurboQuant 論文 arXiv 2504.19874](https://arxiv.org/abs/2504.19874)（Google Research，ICLR 2026）
  * [Eldar Kurtić @_EldarKurtic X Thread](https://x.com/_EldarKurtic/status/2053809608976666758)
  * [OpenAI gpt-oss 模型發布](https://openai.com/index/introducing-gpt-oss/)

---

## [Cloudflare 砍 20% 人喊 AI 100x 生產力，股價跌 23%——市場第一次 punish「AI 取代人」這個故事](https://ai-coding.wiselychen.com/cloudflare-ai-layoffs-100x-claim-market-rejection/)
*🏢 Wisely Chen AI | 2026-05-11*

# Cloudflare 砍 20% 人喊 AI 100x 生產力，股價跌 23%——市場第一次 punish「AI 取代人」這個故事

## 一封很漂亮的內部信，跌掉 23%

2026-05-07，Cloudflare CEO Matthew Prince 在公司部落格貼了一篇文章，標題叫「Building for the future」。內容大意是：公司要為 agentic AI 時代重新架構，所以要砍掉約 **1,100 人，佔員工 20%** 。

這封信寫得很漂亮。

Prince 強調 AI 在公司內部的使用量近三個月成長 **600%** ，工程、HR、財務、行銷每天跑「上千個 AI agent sessions」。他舉了一個比喻——「就像從手動螺絲起子換到電動的」（ _It was like going from a manual to an electric screwdriver_ ），講團隊裡有人「比過去生產力高 2 倍、10 倍、甚至 100 倍」。被裁的人會領薪水到 2026 年底、健保到年底、equity 繼續 vest 到 8/15。一年期 cliff 也 waive 了。

很標準的「AI 重塑未來、好聚好散」劇本。

問題是：公告隔天，Cloudflare 股價跌了 **23%** 。

而這一季的數字其實是漂亮的——營收 $639.8M、年增 34%、單季 record high、EPS beat 分析師預期。**這不是一家虧錢的公司在裁員。** 這是一家剛剛交出 record high 的公司，砍了 20%，講了一個 AI 故事，然後被市場拿去蓋章 −23%。

過去三年我們看了太多劇本：Meta 砍 21,000、Microsoft 砍 10,000、Amazon 砍 27,000、Salesforce 砍 7,000，每一次都同時嘴 AI 加速、自動化、productivity gain。每一次股價基本都漲。

這次第一次反過來。我覺得這個 23% 比那 1,100 人更值得寫。

## 「100x productivity」這個數字，我每次看到就頭痛

先講一個我自己的數字。

過去兩年我在實戰場跑 ATPM（Assessment / Testing / Program / Management）這套 AI coding 流程，量化下來的真實加速是：**40%** 。

不是 100x、不是 10x、是 0.4 倍——把開發週期壓掉 40%。

而這 40% 已經是業界少數有人敢拿出單位、有對照組、有方法論去揭露的數字。同時間我也誠實寫過：QA 驗收階段，我原本期待 AI 帶來 80% 加速，**實際只有 20%** 。PRD 文件平均要迭代 6-7 輪、AI 寫出來的 code 準確度 85%、PRD 跟最終 code 行數比是 1:1.4。

我講這些不是要 humble brag，是要對比——當 Prince 講「2x、10x、even 100x」的時候，我希望你跟我一起問三個問題：

  1. **單位是什麼？** 是寫程式速度？bug 修復速度？支援 ticket 解決速度？還是「我用 ChatGPT 寫了一個 email」的那種「快了一百倍」？
  2. **對照組是什麼？** 比的是同一個人一年前、還是業界中位數、還是某個特定情境下的 best case？
  3. **如果是真的，剩下 4,400 人營收為什麼只成長 34%？** 100x 應該對應到的是營收爆增、產品線爆增、研發進度爆增。Cloudflare 的 Q1 是漂亮的 34%——但那是「一家正常成長的雲端公司」的數字，不是「一家剛剛 unlock 100x productivity 的公司」應該交的數字。



如果一家公司真的解鎖了 100x productivity，**它應該在加人不是砍人** ，因為每個邊際人力的產出是百倍。

Prince 自己其實有意識到這個矛盾，所以他補了一句：「我猜 2027 年我們會比 2026 任何時候員工數都更多。」這句話拆解開——**「我現在砍 1,100 人，但我相信明年我會再僱回比現在更多」** ——本身就在暗示：今天砍的不是因為 AI 取代了這些角色，而是因為現金流 / 組織重組 / 結構調整。AI 是 narrative，不是 cause。

市場聽出來了。

## 真正不對勁的訊號：所有人都砍，留下 sales

如果你只看到 100x 我覺得已經很糟。真正讓我覺得這劇本不對勁的，是 TechCrunch 揭露的一個細節：

> 裁員影響「所有部門和所有地區，**除了背 quota 的業務以外** 」。

停在這句話想一下。

如果你真心相信 agentic AI 已經可以取代大量工作——那 sales 是第一批該砍的。我這樣講不是 troll sales，是看實際工作組成：

  * Demo：可以用 AI agent 自動 walkthrough、按客戶問題客製內容
  * Cold email / 開發信：早就是 AI 戰場
  * CRM 更新、會議記錄、follow-up：100% 機械化、AI agent 跑得比 SDR 還勤
  * Pricing 計算、合約初稿、proposal 整理：LLM 強項
  * Lead qualification、客戶意圖分析：AI 領先人類太多



Sales 工作裡能被 AI 替代的比例，**不會比 support / customer success 低** 。Support 還要處理大量未知技術問題、要查文件、要重現 bug。Sales 處理的反而是相對結構化的對話與流程。

那為什麼留 sales 砍 support？

因為這跟 AI 沒關係。**這是「revenue-attached 留、cost-attached 砍」的傳統公司決策** ——只是這次披了一件 AI 的外套。

Sales 帶 quota，每個人對應一條可量化的營收。砍他們，營收會掉，下一季數字會難看。Support 跟 CS 是成本中心，砍掉短期成本下降、毛利上升，季報好看。從財務模型看完全合理。

但你不能一邊做「砍成本中心、保營收中心」這個傳統 CFO 決策，一邊講「我們正在進入 agentic AI 時代」。**這兩個故事互相矛盾。**

如果 AI 真的 100x，那留 sales 等於浪費資源——你應該砍掉 80% sales、用 AI agent 取代他們的重複勞動，把預算放到那些「比過去高 100 倍生產力」的 R&D 人才身上。

但 Cloudflare 沒這樣做。Cloudflare 做的是「砍 support、留 sales、嘴 AI 故事」——這跟 2010 年代任何一場非 AI 裁員一模一樣。

市場看見了，所以打 23%。

## 為什麼這次劇本不靈了：市場開始要 evidence

過去三年的劇本是這樣的：

**「我們砍了 X 人，因為 AI 帶來了 productivity gain」→ 投資人 OK → 股價漲**

Meta、MS、Amazon、Salesforce、Google 都這樣做過，沒有一家因為這個故事被打。原因很簡單：那個時候 AI 還是 emerging narrative，投資人傾向 **benefit of the doubt** ——你說你的人變生產力 2 倍我就先信，反正 AI 是 trend，不投這個故事我會錯過。

但是 2026 年的投資人不一樣了。經過三年看大模型發布、看 AI Copilot 滲透到每個 SaaS、看 Agentic AI 從 demo 到 production，他們累積了一個基準線：**「AI 確實有用，但 100x 是 bullshit」** 。

機構投資人現在會問：

  * 你說的 2x / 10x / 100x，是哪個團隊、哪個任務、哪個時期？
  * 你砍掉 1,100 人原本做什麼？AI agent 已經接得起來這些工作了嗎？
  * 如果 agent 真的可以，為什麼你的 Q2 guidance 沒有 reflect 任何 margin expansion？
  * 為什麼留著 sales——你自己都不夠相信你的 AI 故事？



Prince 給出的回答其實已經暴露了。當分析師直接問他：「為什麼業績這麼好的一季要砍這麼深？」他的回答是：

> _“Just because you’re fit doesn’t mean you can’t get fitter.”_

這是一句政治正確、毫無資訊量的話。你 fit、你想 fitter，OK——那 fit 在哪、fitter 之後變多 fit、付出的代價是什麼，沒講。這是企業溝通最敷衍的版本。

23% 是市場給這句話的標價。

## 但 Cloudflare 不孤單——為什麼偏偏它被罰？

寫到這裡可能有人想問：可是 2026 上半年「AI 重組」公告幾乎每週都有，為什麼只有 Cloudflare 跌？

來看 2026 年到目前為止的全景：

月 | 公司 | 裁員規模 | 比例 | 官方理由  
---|---|---|---|---  
**5** | **Cloudflare** | ~1,100 | **20%** | AI 重組  
5 | Coinbase | ~700 | 14% | AI 自動化與降本  
5 | PayPal | ~4,500+（未來 2-3 年） | 20% | 長期重組  
5 | Estée Lauder | 9,000–10,000 | — | 擴大重組  
4 | Meta | ~8,000 | 10% | 公司級裁員  
4 | Snap | ~1,000 | 16% | 廣告業務壓力  
**3** | **Oracle** | **~30,000** | **~18%** | AI 雲轉型（$156B capex）  
3 | Atlassian | ~1,600 | 10% | AI 重構  
3 | Morgan Stanley | ~2,500 | 3% | 華爾街降本  
**2** | **Block** | **超 4,000** | **接近 40%** | AI 自動化  
2 | Heineken | 最多 6,000 | ~7% | 全球優化  
  
注意兩個極端：

  * **Block 砍 40%、股價 +24%** 。Jack Dorsey 直白寫給股東：「intelligence tool capabilities are compounding faster every week」，CFO Amrita Ahuja 補：「我們看到用更小、更精的團隊配合 AI 加速的機會」。市場買單，股價當日漲 24%。
  * **Cloudflare 砍 20%、股價 −23%** 。Prince 講 100x、講 600% AI usage、講「manual to electric screwdriver」。市場不買單。



同樣 template、同樣 AI 故事、同樣 2026 上半年——一家被 reward 24%、一家被 punish 23%，差了將近 50 個百分點。差在哪？

我認為差在三件事：

**1. 故事跟財務數字要 self-consistent。** Block 講「更小、更精的團隊」——它的毛利率本來就承壓，砍 40% 對應到 EBITDA 立刻有結構性改善，故事 = 現金流改善路徑。Oracle 講 AI infrastructure——它公開承諾 $156B 在 GPU 跟 data center capex，砍 30,000 人省下的 $8-10B 年現金流直接灌進 AI 投資，故事 = capex 對齊。**Cloudflare 講「AI agentic 重組」，但 Q1 是 record high、毛利沒承壓、capex 沒爆增——故事跟財報對不上** ，市場看不出這 1,100 人省下的錢要去哪裡。

**2. 砍的部位要跟故事一致。** Block 是 across-the-board 砍 40%、含 sales、含管理層。Oracle 砍的是 legacy software maintenance、on-prem support、SaaS/Virtual Operations Services（這兩個部門各砍 30%），同時 OCI / AI services 部門在 hiring——非常清楚的「砍舊保新」。**Cloudflare 砍所有非 sales 部門、保留所有 sales** ——說自己 going agentic，但留下整個最 human-process-heavy 的銷售流程。砍的部位跟故事相反。

**3. 數字要有單位，或者乾脆不給。** Block 全程沒講任何 productivity multiplier，講的是「compounding faster every week」這種定性 framing。Oracle 完全不提生產力，講的是 capex 跟 data center。這兩家都避開了量化陷阱。**Cloudflare 給了 2x / 10x / 100x——一旦你說了數字，市場就會比對你下一季 EPS、margin、revenue per employee** 。給不出來就破功。

換句話說，**市場不是反 AI 裁員潮，市場是在挑魚** 。Block 故事有 internal consistency、Oracle 用真金白銀對齊、兩家都過關。Cloudflare 三條都沒對齊，被挑出來罰。

潮水沒退，只是濾網變細了。

## 那我們一般人怎麼辦

對，我們一般人能夠做的事情其實很有限。

一樣的就是好好的重啟，好好的把自己轉變成一個在 AI 時代最適合的人。然後就是隨時把自己當作一個一人公司，好好去看待這件自己的相關規劃。

## 常見問題 Q&A

**Q: 你是說 Cloudflare 不該裁員嗎？**

不是。一家公司決定如何配置人力是 CEO 的職責，外人沒立場評。我評的是「裁員的解釋故事」——把 cost cutting 包裝成 AI replacement，這個包裝在 2026 不再有效。誠實說「我們在重組成本結構」反而會被市場接受。

**Q: 那 40% vs 100x，誰才是真實的？**

兩個都是。40% 是我自己 production 場景的 measured outcome，有單位、有對照組、有方法論。100x 是某個 best-case scenario 下某個任務的 reported feeling，可能在那個情境下是真的，但**不能 generalize 到「公司整體 productivity」** 。Prince 把 best-case 拿來支撐 company-wide 決策，這是 measurement 紀律的問題。

**Q: 那企業要怎麼 measure AI productivity 才不會犯這個錯？**

最低標準三件事：(1) 講清楚單位（行數？週數？story point？ticket？），(2) 提供對照組（同團隊半年前 / 不用 AI 的對照組 / 業界 median），(3) 公布 caveat（哪個階段加速最多、哪個階段沒幫助、PM / QA / DevOps 各拿到多少）。沒有這三件事的 productivity number，不管多漂亮，都只能當 sales pitch 看。

**Q: 你看好 Cloudflare 嗎？**

我看好它的產品，不評論股價。Cloudflare 的 edge network、Workers、R2 都是技術上極強的產品線。這次的問題在 communication 跟 measurement framework，不在產品。如果他們之後願意公布更細的 productivity measurement methodology，我會收回對這次 100x claim 的質疑。

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

### 1. **5 小時上限突然變 2 小時**

Anthropic 技術團隊 Thariq Shihipar 已經承認：

> 「為了因應 Claude 需求成長，Anthropic 在尖峰時段調整了 Free、Pro 與 Max 訂戶的 5 小時使用上限。」

翻譯成白話：**他們偷偷在尖峰時段降額了。** 同樣的工作量，以前可以撐滿 5 小時，最近大概 2 小時就達上限。

### 2. **Opus 4.6 thinking 深度被砍 73%**

我之前寫過 [Opus 4.6 偷偷縮水那篇](https://ai-coding.wiselychen.com/opus-46-shrinkflation-open-source-agent-only-viable-path/)，用 17,871 個 thinking blocks 的數據做出來的結論：**thinking 深度直接被砍 73%** 。

社群上的反應是這樣的：

> 「Claude Code Opus 4.6 just forgot its own features.」 — @om_patel5

> 「People are paying 20x more and getting worse performance.」 — Reddit r/ClaudeAI

Plan Mode 失效、程式碼品質斷崖式下降、推理一致性崩壞、工具呼叫失靈 — 這些都不是個別 bug，是系統性的衰退。

### 3. **StupidMeter 數據：22 個模型只有 1 個是 OK**

[StupidMeter](https://aistupidlevel.info/) 24/7 監控 22 個主流模型，最新的 leaderboard：GPT 標 DEGR、Claude 標 WARN、Gemini 標 WARN、Grok 標 WARN、DeepSeek 標 WARN — **只有 GLM 一個 OK** 。

[我之前那篇 LLM 降智不是都市傳說](https://ai-coding.wiselychen.com/llm-silent-degradation-enterprise-it-harm-stupidmeter-monitoring/) 講的就是這件事：模型品質不再是固定常數，是浮動變數。

### 4. **Max Plan 燒光速度翻倍**

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

### 1. **敵人的敵人就是朋友**

Musk 跟 OpenAI 的恩怨已經不是新聞。從離開 OpenAI 董事會、創立 xAI、提告 OpenAI、到公開喊話要收購 OpenAI，兩邊關係徹底破裂。

在這個格局下，**算力租給 Anthropic = 養大 OpenAI 最強的對手** 。

對 Musk 來說，這是商業上收得到錢、戰略上又能削弱 OpenAI 的兩面贏。錢是 Anthropic 出，傷的是 OpenAI 的市佔。

### 2. **Colossus 的 GPU 利用率，其實沒打滿**

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

### 1. **Claude Code 重度使用的成本壓力會緩解**

5 小時上限加倍 + 取消尖峰降額，對於每天用 Claude Code 6-8 小時的開發者來說，**意味著工作流不再被頻繁打斷** 。

對企業的 ATPM 流程來說，這代表 PRD 迭代、code review、QA 驗證可以連續進行，不用因為「額度燒完」中斷思路。

### 2. **Claude Opus API 的速率提高，對 agent 應用是利多**

很多人在做 multi-agent system、agent handover 這類應用時，會撞到 Opus 的 rate limit。

API 速率大幅提高，**意味著我們可以做更密集的 agent 編排，而不用一直在 retry/exponential backoff 裡打滾** 。

這對 [agent 落地](https://ai-coding.wiselychen.com/aizhuan-xing-ai-agent-ru-he-luo-di/) 是非常有感的。

### 3. **算力競爭已從「誰有 GPU」進化到「誰能組合多元算力」**

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
