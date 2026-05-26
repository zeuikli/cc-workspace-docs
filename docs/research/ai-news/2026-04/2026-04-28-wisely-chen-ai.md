---
title: Wisely Chen AI — 2026-04-28
date: 2026-04-28
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-04-28

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [DeepSeek V4 把百萬 Token 上下文打到傳統 2% 成本——拆解 CSA + HCA 雙 Attention 設計](https://ai-coding.wiselychen.com/deepseek-v4-million-token-csa-hca-attention/)
*🏢 Wisely Chen AI | 2026-04-28*

DeepSeek V4 論文的真正題眼不是「百萬 token」，而是「低成本、高保真度」。透過 CSA（抓重點）+ HCA（看全域）兩個互補的 attention 模組，V4 把 KV Cache 砍到傳統方案的 2%，計算量降到 V3.2 的 10%，同時在百萬 token 評測上超越 Gemini 3.1。這篇文章從工程師視角，把這套機制的設計思路、跟 MLA / NSA 的傳承關係、以及實際工程意義拆給你看。

為什麼這篇論文值得認真看

我自己的判斷是這樣：[DeepSeek V4](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/main/DeepSeek_V4.pdf)（[Hugging Face 模型頁](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)）不是又一個堆參數量的模型升級，它是一篇真正在「Attention 結構」上做出系統性突破的論文。

過去兩年大家都在喊百萬上下文，但訓練端跟推理端兩個天花板沒人真的捅破：

訓練端： Attention 是 O(n²)，從 4K 擴到 1M 計算量會漲 62,500 倍，所以絕大多數模型其實只是「後期硬擴」。

推理端： KV Cache 把計算量問題救回來了，但代價是視訊記憶體爆炸——8B 小模型在百萬 token 推理就要 144GB。

V4 同時動了這兩端。論文題目寫的是「低成本、高保真度的百萬 Token 長上下文處理」，但讀進去你會發現，整篇東西在講的就是怎麼重新設計 attention，讓兩個天花板同時下移一個數量級。

這篇文章我會拆四件事：

V4 的核心改動：CSA 跟 HCA 兩個 attention 模組各做什麼

為什麼是「雙通道」而不是單一壓縮

DeepSeek 兩年來的技術路徑：MLA → NSA → CSA + HCA

對 AI Coding / Agent 工程師的實際意義

一、CSA + HCA：兩個互補的 Attention 模組

V4 升級的點很多，但論文裡核心的兩個都跟 attention 有關。兩個都是壓縮，但角色完全不同。

兩個模組的全名是 CSA = Compressed Sparse Attention、HCA = Heavily Compressed Attention。

CSA：抓重點

CSA 的設計目標是「精度」。

它的做法是兩階段：

第一階段： 把 100 萬 token 的 KV Cache 壓縮成 25 萬條

第二階段： 從這 25 萬條裡，挑出最有用的一小部分，只對這一小部分算 full attention

換句話說，CSA 不是讓模型「均勻地看所有東西」，而是讓模型「知道該重點看哪裡」。

這個思路其實業界很多人試過——sparse attention 就是這條路。難點從來不是「怎麼挑少一點 token」，而是「怎麼挑得既準又快」。論文裡這個 25 萬 → 小部分的篩選機制，是 V4 的核心 IP 之一。

我的理解是：CSA 在這條路上把「sparse 的精度」拉到了一個新層級，所以才敢把 KV Cache 一路壓下去還不掉品質。

HCA：看全域

如果只用 CSA，會有一個風險：模型很會看「重點」，但全域感會丟掉。長文件分析、多步推理這種任務，需要模型「始終隱約知道整篇在講什麼」。

HCA 的角色就是補這個。

它的做法更激進：把 100 萬 token 直接壓縮成 7800 條。

7800 條聽起來少到誇張，相當於原文的 0.78%。但 HCA 不是想取代 CSA，它是在 CSA 之外開了一條「全域低解析度」的通道——模型透過這條通道知道整體骨架，再透過 CSA 挑出局部精細的內容。

兩條路一起跑，就形成了「精準 + 全域」的互補結構。

數字怎麼出來的

對比 V3.2，V4 兩個版本的優化幅度是這樣：

指標
V4 Pro
V4 Flash

推理計算量（vs V3.2）
27%
10%

KV Cache（vs V3.2）
10%
7%

整體效能
全面提升
全面提升

注意 V4 Flash 那一行——計算量 10%、KV Cache 7%，但效能還比 V3.2 強。

這個級別的優化通常會犧牲品質。但 V4 在百萬 token 評測上的表現是：MRCR（Multiple-Retrieval Contextual Recall）1M 評測，V4-Pro 拿 83.5 分，Gemini 3.1-Pro 是 76.3 分，差距相當顯著。整體還落後 Claude Sonnet 4.6，但對一個開源模型而言已經是頂級陣營。

論文自己用了一個我覺得不太像 DeepSeek 風格的形容詞——「戲劇性地」把百萬 token 上下文的 KV Cache 降到傳統方案的 2%。能讓他們自己這麼描述，代表他們對這個結果的信心。

二、為什麼這個「保真度」是新東西

V4 論文標題裡那個「high-fidelity」三個字其實有歷史包袱。過去兩年大家都在標百萬 token，但學界已經反覆證明這些數字禁不起檢驗。要理解 V4 為什麼值得認真看，得先把這兩個經典結果拉出來。

NVIDIA RULER：標百萬只用得到 16K

NVIDIA 在 2024 年發了 [RULER（What’s the Real Context Size of Your Long-Context Language Models?，COLM 2024）](https://arxiv.org/abs/2404.06654)，系統性測了 10 個主流長上下文模型——9 個開源加 GPT-4，宣稱長度從 32K 到 1M。

論文結論很尷尬：這些模型一半以上連自己宣稱的 32K 都撐不住，幾乎全部在上下文一拉長就嚴重掉效能。 一個微調版 Llama 號稱支援 1M，RULER 實測能保真使用的部分只有 16K 左右——縮水 98%。

這個落差的根源是訓練方式。絕大多數模型走「兩段式訓練」——先用短上下文（比如 4K）跑完 95% 以上的訓練，再花很少的步數（2000 步左右）把上下文「擴」到 128K 或更長。模型在 4K 階段學到的注意力分布，根本沒見過真正的長文本。後面那點微調是「強行拉伸」，不是「真正學會」。

Lost in the Middle：中間段集體失憶

[Stanford 在 2023 年發的 Lost in the Middle](https://arxiv.org/abs/2307.03172) 是另一個讓人坐不住的結果。論文做了個漂亮的實驗：把同一個關鍵資訊放在文件的不同位置，量化問答準確率。

結果是經典的 U 形曲線——首尾位置準確率高，中間掉到接近隨機猜的水準（圖中虛線是 closed-book baseline，等於模型完全沒看文件的表現）。

這個現象到 2025 年還在，所以你會看到很多 RAG 工具的最佳實踐是「重要內容放開頭和結尾」。這不是迷信，是工程上對 Lost in the Middle 的妥協。

V4 的設計哲學是針對這兩個 failure mode

回頭看 CSA + HCA 的雙通道結構，你會發現它幾乎是精準對應 RULER 跟 Lost in the Middle 揭露的兩個老問題：

訓練端認真做： V4 不靠後期硬擴，從訓練早期就把長度擴上去（後面第五節展開）→ 解 RULER 的「兩段式訓練偷工減料」

CSA 抓重點： 中間段的關鍵 token 不再被均勻平攤的 attention 稀釋，而是被 sparse 篩選機制主動挑出來 → 解 Lost in the Middle 的中段失憶

HCA 看全域： 7800 條全域表徵保留整篇骨架的訊號，避免中間段在概覽層級也被忘掉 → 雙保險

論文選用的 MRCR（Multiple-Retrieval Contextual Recall） 評測就是專門打 Lost in the Middle 的——測模型能不能在百萬 token 裡精確檢索多個分散的目標。V4-Pro 拿 83.5 分，比 Gemini 3.1-Pro 的 76.3 高出一截。這個差距就是「保真度」的具體體現。

換個角度說：V4 不是又一個百萬上下文模型，而是第一個直接拿 RULER 跟 Lost in the Middle 開刀的模型。

三、為什麼是雙通道，不是單一壓縮

讀完論文我自己思考了一下：為什麼 V4 要做兩個 attention 模組，而不是把一個做到極致？

我的解讀是：單一壓縮機制有個結構性的兩難。

如果你壓縮率拉到極致（比如 HCA 的 0.78%），全域感很強，但你看不見任何細節——任何需要「精確引用某段話」的任務都會掉。

如果你壓縮率保守（保留更多 token），細節是有了，但計算量跟記憶體吃不消，回到原本的天花板。

過去業界要嘛走 sparse（CSA 這類），要嘛走 linear / low-rank（HCA 這類），但鮮少有人把兩種同時做到位再讓它們互補。V4 的工程巧思就在這——兩個通道分工：

CSA 像放大鏡：只看重要的，但看得很清楚

HCA 像衛星圖：解析度低，但永遠看得見全圖

模型每一層 attention 的時候，兩條資訊同時餵進去。這樣不管你問的是「整篇在講什麼」還是「第 87 段那個數字是多少」，都能拿到對的訊號。

這個設計哲學讓我想起作業系統裡的 cache hierarchy：L1 快但小、L3 慢但大，互補才能撐起整個系統。V4 把這個思路搬到了 attention。

四、DeepSeek 的「省成本」是有路徑的

V4 不是橫空出世。把時間軸拉開看，DeepSeek 過去兩年其實是在連續打同一個方向——Attention 是長上下文的瓶頸，那就把 attention 一層層改造下去。

時間
技術
論文
效果

2024/5
MLA（V2 提出）
[arXiv:2405.04434](https://arxiv.org/abs/2405.04434)
KV Cache 降低 93.3%，V3、V4 都繼承

2025/2
NSA
[arXiv:2502.11089](https://arxiv.org/abs/2502.11089)
64K 上下文 attention 全面加速（decode/forward/backward）

2025/12
DSA（V3.2）
[arXiv:2512.02556](https://arxiv.org/abs/2512.02556)
NSA 思路在線上模型落地，首次做到 fine-grained sparse

2026/4
CSA + HCA（V4）
[DeepSeek_V4.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/main/DeepSeek_V4.pdf)
計算量降 73%、KV Cache 降 90%

MLA：先把 KV 表徵壓下去

V2 的 [MLA（Multi-head Latent Attention）](https://arxiv.org/abs/2405.04434)解決的是「KV Cache 每個 head 都要存一份」的問題。透過低秩投影把 KV 共用一個 latent 空間，KV Cache 直接減 93.3%、訓練成本省 42.5%、生成吞吐拉到 5.76 倍。

這是 V2 那年最大的成本武器，也是後面 V3、V4 一切優化的地基。

NSA：sparse attention 真的能上線

2025 年 2 月那篇 [NSA（Native Sparse Attention）](https://arxiv.org/abs/2502.11089)我之前解讀過。當時很多人覺得是純研究——sparse attention 大家都試過，理論加速漂亮但實際效能很難真的省到。NSA 的貢獻是把 sparse 真的做到「訓練、推理同一套機制」（hardware-aligned + natively trainable），64K 上下文在 decode、forward、backward 三個階段都拿到顯著加速。

DSA：NSA 的線上落地

2025 年 12 月，[V3.2 把 NSA 思路真的搬上線](https://arxiv.org/abs/2512.02556)，命名為 DSA（DeepSeek Sparse Attention）。它是「lightning indexer + fine-grained token selection」兩段式架構，並直接架在 MLA 之上——也就是 MLA 跟 sparse attention 第一次堆疊在同一個產品模型裡。

論文裡有句話我覺得寫得很實在：「achieves fine-grained sparse attention for the first time, while maintaining virtually identical model output quality」。先有 DSA 把品質不掉的證明拿到手，再幾個月後 CSA 就在 V4 上把壓縮率再推一個量級。

V4：兩個方向同時收口

V4 把過去兩年的兩條線——「壓 KV 表徵」（MLA → HCA）跟「sparse attention」（NSA → DSA → CSA）——同時做到極致，再讓它們互補。

這條路徑的核心邏輯一直沒變，但執行力很夯。每一步都在「真實上線的模型」上落地，不是只發論文交差。

跟矽谷那種「論文歸論文、產品歸產品」的節奏完全不同。

五、訓練端也認真改了

很多人忽略一件事：V4 不只是推理優化，訓練端也大改。

論文裡幾個關鍵動作：

訓練時就早早把上下文長度擴上去，不是最後階段才擴 2000 步

訓練資料量比 V3 翻倍

特別重視長文件的整理

這部分是隱性工夫，不容易公開比較，但對長上下文「保真度」來說比 attention 機制本身更關鍵。

為什麼？因為你的 attention 機制再好，如果訓練資料裡幾乎沒有真正的長文，模型就沒有機會學到「跨千個 token 的依賴關係」。CSA + HCA 給的是「能力」，但長文訓練資料給的才是「經驗」。

這也呼應論文標題裡那個「保真度」三個字——能力跟經驗兩個都要在，才算保真。

六、對 AI Coding / Agent 工程師的實際意義

技術拆完，回到工程師視角。V4 這套設計對日常工作的影響在哪？

1. 推理模型終於有「思考空間」

這是我覺得最被低估的一點。

推理模型最大的痛點不是答案不準，而是「想到一半空間不夠」。一個複雜 reasoning 任務可能要燒幾萬 token 思考，上下文短就直接被卡住。

CSA 抓重點、HCA 看全域的設計，本質上是讓模型在長思考過程中不容易忘記前面想過什麼。對 Agent 跑多步任務、對 AI Coding 跑長 PR review，這個影響是實質性的。

2. 長任務的成本經濟學要重算

V4 的定價我做這篇文章的時候剛好看到打了 2.5 折，折後價格大概是御三家的 5% 左右，是國內大模型最便宜的一檔。

過去長上下文便宜的模型不是沒有，但便宜的代價就是品質差。V4 把「便宜」和「保真」第一次同時做到——這個組合對 Agent 跟 AI Coding 很關鍵：

整個 codebase 進來：以前要先 RAG 切片，現在可以直接塞

PR review：50 個檔案的 diff 一次餵進去

長任務 Agent：Claude Code 那種要連續跑十幾步的任務，token 不再是瓶頸

當然這不代表 RAG 沒用了——成本可控性、延遲、可審計性這些 RAG 還是強。但「能直接塞就直接塞」這個選項，門檻被大幅降低。

3. Context Engineering 的權重會變

我之前寫過 [Claude Code 的四層上下文壓縮](https://ai-coding.wiselychen.com/claude-code-context-engineering-four-layer-compression/)。那套東西很強，但本質上是「上下文窗口不夠」的工程補救。

如果 V4 級別的機制普及（國內這條線會很快，矽谷可能會跟），未來 Context Engineering 的重點會從「怎麼把資訊壓進有限窗口」轉向「怎麼讓長上下文模型專注在對的訊號上」。

這是兩種完全不同的工程心智。

七、坦白說

寫這篇文章的時候，我很清楚有幾件事自己還沒搞定：

我沒有真的 benchmark 過 V4。 文章裡所有數字都來自 DeepSeek 官方論文跟 release，社群的廣泛實測還沒出來。等過幾週應該會有人做完整對比。

CSA + HCA 的論文細節我只看了 high-level。 壓縮率、互補關係、整體性能影響這些我有把握，但「25 萬條怎麼挑出最有用的小部分」、「HCA 7800 條的具體表徵方式」這些實作細節，我還在追。

「KV Cache 2%」是 best case。 真實工作負載下這個數字會不會打折扣，要等實測。歷史上幾乎所有的「壓縮 X 倍」廠商宣稱，落地都會打折。

百萬 token 評測超 Gemini 3.1，但榜單不是全部。 AI Coding 體驗、工具呼叫穩定度、reasoning 一致性，這些都要實際用過才知道。我自己的標準是：用 V4 跑完一個完整 codebase 的 review 任務沒出狀況，再下結論。

我寫這篇是因為這個方向是對的，論文的設計哲學值得學，不是因為 V4 已經解決了所有問題。

八、論文與延伸閱讀

本文涉及的論文

DeepSeek 主線：

DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence — [PDF](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/resolve/main/DeepSeek_V4.pdf) ｜ [模型頁](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) ｜ [HF Blog](https://huggingface.co/blog/deepseekv4)

DeepSeek-V3.2（DSA）：Pushing the Frontier of Open Large Language Models — [arXiv:2512.02556](https://arxiv.org/abs/2512.02556)

NSA: Hardware-Aligned and Natively Trainable Sparse Attention — [arXiv:2502.11089](https://arxiv.org/abs/2502.11089)

DeepSeek-V2(MLA 提出)：A Strong, Economical, and Efficient MoE Language Model — [arXiv:2405.04434](https://arxiv.org/abs/2405.04434)

長上下文評測與 failure mode：

RULER: What’s the Real Context Size of Your Long-Context Language Models? — [arXiv:2404.06654](https://arxiv.org/abs/2404.06654) ｜ [GitHub](https://github.com/NVIDIA/RULER)

Lost in the Middle: How Language Models Use Long Contexts — [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) ｜ [GitHub](https://github.com/nelson-liu/lost-in-the-middle)

第三方解讀

[DeepSeek-V4 Review (Andrew Lukyanenko)](https://artgor.medium.com/deepseek-v4-review-why-million-token-context-needs-efficient-attention-not-just-larger-windows-6dc8e74a00b1)

[MarkTechPost：CSA + HCA 拆解](https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/)

[Hacker News 討論串](https://news.ycombinator.com/item?id=47885014)

我之前寫過的相關文章

[搞懂快取機制，從 Gemma4 到 Claude Code 省 80% Token](https://ai-coding.wiselychen.com/kv-cache-gemma4-claude-code-save-80-percent-token/) — KV Cache 從另一個角度的拆解

[Google TurboQuant：KV Cache 壓縮 6x 的技術突破](https://ai-coding.wiselychen.com/google-turboquant-kv-cache-compression-wall-street-panic/) — Google 在同一個方向的工作

[殘差連接被動刀了：DeepSeek 和 Kimi 先後改掉 Transformer 的「默認設定」](https://ai-coding.wiselychen.com/residual-connection-deepseek-mhc-kimi-attention-residuals-breakthrough/) — DeepSeek 過去兩年另一條改造路線

[Claude Code 的四層上下文壓縮](https://ai-coding.wiselychen.com/claude-code-context-engineering-four-layer-compression/) — 上下文不夠用時的工程補救

常見問題 Q&A

Q：CSA + HCA 跟之前的 sparse attention / linear attention 有什麼不同？

最大的差別是「兩種機制互補」。過去 sparse 就是 sparse，linear 就是 linear——要嘛抓重點丟全域、要嘛看全域沒精度。V4 是讓 CSA 負責局部精度、HCA 負責全域感知，兩條通道一起跑。這個雙通道思路在工程上很巧。

Q：V4 真的能取代 Claude / Gemini 嗎？

榜單上百萬 token 評測 V4 超過 Gemini 3.1、落後 Claude Sonnet 4.6。但榜單不是全部，AI Coding 體驗、工具呼叫穩定度、reasoning 一致性，這些都要實際用過才知道。我的判斷是「V4 會吃掉一部分原本給 Gemini 的工作量」，但 Claude 在 AI Coding 領域的優勢短期不會被取代。

Q：MLA 跟 HCA 都是壓縮 KV，差在哪？

MLA 是壓「每個 token 的 KV 表徵」——讓多個 head 共用一個低秩 latent。HCA 是壓「token 數量本身」——把 100 萬條 KV 壓成 7800 條。一個是壓「縱向」的 head 維度，一個是壓「橫向」的 sequence 維度。V4 兩個都用，所以才能疊到那麼極端的壓縮率。

Q：開源版本 V4 真的能拿來自己 host 嗎？

理論上可以，但要看你願意花多少錢買 GPU。即便 KV Cache 砍到傳統 2%，真要在百萬 token 場景跑 V4 Pro，仍然不是 consumer GPU 能扛的。對絕大多數團隊，直接用 API 還是經濟得多。

Q：你覺得長上下文的下一站是什麼？

我猜測是「層級式記憶」——CSA + HCA 這種「同一輪內」的壓縮已經做到極致了，下一步是跨輪、跨任務的長期記憶。Memory Sparse Attention（MSA）那條線、還有 Recursive Language Models 的方向，都在往這走。但這就是另一篇文章的事了。

作者： Wisely Chen
日期： 2026 年 4 月
系列： AI 前沿技術

---
