---
title: "Wisely Chen AI — 2026-05-07"
date: 2026-05-07
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-05-07

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [Gemma 4 加速 3x：Speculative Decoding 不是新玩意，但 Google 這次把 drafter 整套 Apache 2.0 送出來](https://ai-coding.wiselychen.com/gemma4-mtp-drafter-speculative-decoding-open-source/)
*🏢 Wisely Chen AI | 2026-05-07*

Gemma 4 加速 3x：Speculative Decoding 不是新玩意，但 Google 這次把 drafter 整套 Apache 2.0 送出來

「3x faster」這個標題我看了三秒就想關掉

[Google 5/6 的 blog post](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) 標題寫得很大：

Gemma 4: Now up to 3x Faster. ⚡ Same quality, way more speed.

老實講，我看到「3x faster」這四個字第一反應是想直接划走。

不是因為 Google 在唬爛——數字是真的——而是因為 speculative decoding 不是什麼新東西。

2023/01 [Google 自己的論文](https://arxiv.org/abs/2211.17192) 就提過 speculative decoding

2023/05 [DeepMind 的 SpecInfer](https://arxiv.org/abs/2305.09781)

2024/01 [Medusa](https://arxiv.org/abs/2401.10774) 把這事推到 production

2024/06 [EAGLE](https://arxiv.org/abs/2401.15077) 把 acceptance rate 拉得更高

2024/12 [DeepSeek V3](https://arxiv.org/abs/2412.19437) 直接把 MTP head 烘進主模型訓練流程裡

所以「Gemma 4 用 multi-token prediction 變快了」這件事本身，技術上沒什麼好驚訝的。

但我點進去讀完以後，覺得這篇還是值得寫一篇。

不是因為 3x 這個數字，是因為 Google 這次的釋出方式打到了一個很多人沒注意到的痛點：整個 Gemma 4 family 的 drafter 用 Apache 2.0 開源，drafter 還跟主模型對齊、共享 KV cache，連 31B Dense、26B MoE、E2B、E4B 邊緣版都配齊。

這件事比 3x 重要太多。

先講 speculative decoding 怎麼運作（30 秒版）

如果你已經懂可以跳過。如果不懂，這一段值得花 30 秒，因為後面的數字才有意義。

LLM 推理慢的本質原因，是它一次只能吐一個 token。每生一個 token 都要把整個模型 forward 一次——哪怕是 31B 模型生「的」這個字也是 31B 整個算一遍。

Speculative decoding 的點子很賤但有效：

找一個小很多的 drafter 模型，先讓它一次猜接下來 4 個 token（成本很低）

把這 4 個猜測丟給主模型，一次 forward 同時 verify（一次 forward 驗 4 個 = 賺到了）

如果主模型同意 drafter 的猜測，就整段接受；不同意就退回到第一個分歧點，繼續正常 decode

關鍵是步驟 2：主模型 verify 4 個 token 的成本，跟生 1 個 token 幾乎一樣（因為 forward pass 的 cost 主要是把 weights 從 HBM 搬進 SRAM，不是算數）。

所以理論上限是 4x、5x，但實務上要看 drafter 猜得準不準（acceptance rate）。猜中率高 = 加速多，猜中率低 = 多做白工。

Google blog 引用裡那句「If the target model agrees with the draft, it accepts the entire sequence in a single forward pass—and even generates an additional token」就是在講這個機制。

一個秒懂的例子

這樣講可能還是抽象，舉個具體的：

你輸入「泥菩薩過江，自身」——後面該接什麼？

任何中文母語者腦袋瞬間都會跳出「難保」這兩個字。這不需要思考，只需要一個記得這句俗語的小腦袋就夠了。

普通 LLM inference 的做法是：

31B 主模型 forward 一次 → 吐「難」

31B 主模型再 forward 一次 → 吐「保」

兩次完整的 31B 計算，只是為了補完一句小學生都會背的俗語。就是這種「明顯到不需要動用主模型」的續寫，吃掉了大量推理時間。

MTP 的做法：

小 drafter（可能只有 0.5B）一秒猜出「難保」

主模型一次 forward 同時 verify 兩個字 → 同意 → 整段接受

結果：兩個 token 用「主模型 1 次 + drafter 0.1 次」的成本生出來，而不是「主模型 2 次」。

這就是為什麼 acceptance rate 能那麼高、加速幅度能到 2-3x——人類語言裡有大量「半個句子就決定後半句」的可預測片段。code 裡的 import numpy as np、API 文件裡的 return response.json()、中文的成語俗語、英文的固定搭配，全部都是 drafter 的天堂。

反過來，drafter 猜不準的場景也很好懂：「我覺得這個方案最大的問題是___」這種開放式創作，後面是什麼字主模型自己都還沒決定，drafter 怎麼可能猜對？

懂了這個再看數字會比較有感。

Google 公布的數字：拆開看

我把官方數字攤開：

場景
加速幅度
條件

26B 模型，NVIDIA RTX PRO 6000
生成時間砍半（~2x）
對比無 drafter 標準推理

26B MoE，Apple Silicon
~2.2x
batch size 4–8

全 family token-per-second
up to 3x
best case

幾個老實的觀察：

「up to 3x」是 best case，不是平均值。 真實使用 2x 比較常見，3x 要對的 batch + 對的 task。

Apple Silicon 那個 2.2x 是 batch 4–8。 Batch=1 拿不到 2.2x。意思是如果你在 Mac 上單人聊天，加速會比 batch 4 同時處理小很多。

NVIDIA RTX PRO 6000 是專業卡（不是 5090）。家用顯卡能複製多少還沒看到獨立 benchmark。

但 這些數字沒有任何水分——speculative decoding 在學界跑了三年，Medusa 跟 EAGLE 的論文 acceptance rate 數字都對得上。Google 講 2x–3x 不是行銷，是物理現象。

問題是「物理現象」拿到手裡有沒有用，要看你的場景。

什麼情況拿不到 3x（誠實版）

這是大部分發新聞都不會講的部分。

1. 高分歧 task：creative / 多語言 / 推理鏈

Drafter 是個小模型。它對 predictable 的內容猜得準（API 文件、常見 code pattern、常用表達），對 高熵內容 猜不準。

寫程式、回答 FAQ、structured output → 高 acceptance，2.5x–3x 很常見

中文創作、多語言翻譯、開放式推理 → acceptance 掉很多，1.3x–1.7x

數學推理長 chain-of-thought → 中間每一步都有分歧，可能只剩 1.2x

我自己用 Cursor 寫 TypeScript 的時候 speculative decoding 體感很明顯，但寫繁體中文部落格的時候差距小很多——這篇就是個例。

2. Batch size 太小

Speculative decoding 的「verify 4 個 token 跟 1 個成本一樣」是有前提的：主模型 forward pass 還沒被 batch size 撐爆。

如果你的 batch=1（單人 inference），加速比較大；
如果你的 batch=32（高負載 server），主模型 forward 已經算到滿，verify 4 個就不是免費的，加速會壓縮。

Apple Silicon 的數字寫 batch 4–8 不是隨便挑的——那是甜蜜點。

3. Long context

Drafter 跟主模型共享 KV cache 是 Google 這次強調的優化。但 context 一長，drafter 自己也得扛 attention 的 O(n²) 成本，加速幅度會被吃掉。

短 prompt + 長生成 → 加速明顯
長 prompt + 短生成 → 加速被攤薄

那這次 Google 真正做對的事，是什麼

如果單看 3x，這篇我寫不下去——前面講過了，Medusa、EAGLE、DeepSeek V3 早就有。

這次值得寫的點是釋出方式：

1. Apache 2.0，可商用

[Hugging Face 上直接下載](https://huggingface.co/google)，不用簽 license、不用申請、可以包進產品賣。這跟 Llama 早期還有 Meta 限制條款不一樣。

2. 整個 Gemma 4 family 都配齊 drafter

Gemma 4 31B Dense

Gemma 4 26B Mixture-of-Experts

Gemma 4 E2B（edge）

Gemma 4 E4B（edge）

含邊緣版本。意思是手機上的 inference 也能拿到 speculative decoding 的好處。

3. Drafter 跟主模型對齊 + KV cache 共享

這是技術上最值錢的部分。自己訓練一個能匹配主模型的 drafter 不簡單——drafter 太大就 overhead 太重，太小 acceptance 太差，要找對 sweet spot 而且要跟主模型的訓練分布對齊。

Google 直接把對齊好的 drafter 給你。等於把「用 EAGLE 自己練 drafter」這個技術門檻砍掉。

4. 主流推理框架全部支援

[Transformers, MLX, vLLM, SGLang, Ollama](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) 都已整合。直接 ollama pull gemma4:31b-mtp 這種程度的方便。

為什麼這對「想自主可控」的人是真的好消息

我前陣子寫過 [Token 經濟學 + DDR/HBM 鎖喉那篇](/ddr-hbm-token-economics-nvidia-lock-supply-chain/)，結論是：

要繞過 Nvidia + HBM 鎖喉，只剩兩條路——
（1）開源權重 + 自主部署
（2）推理優化把同樣硬體榨出更多 token

MTP drafter 是 (2) 推理優化 這條路上一塊很重要的拼圖。

實際算一下：

情境： 一家台灣公司想 on-prem 跑 Gemma 4 26B MoE 服務內部 200 人

沒有 MTP：

假設一張 H100 跑 26B MoE 約 80 tokens/s

200 人共用，平均每人不到 0.4 t/s 的可用 quota

體感：嫌慢，要排隊

有 MTP（保守估 2x）：

同一張 H100 跑到 160 tokens/s

等於同樣硬體服務 400 人，或同樣 200 人體感快一倍

不用買第二張卡

這對「想跑本地推理但被卡在硬體成本」的中小企業是實質的減負。 不是 3x 才有意義，2x 就夠改變決策。

我之前寫的 [On-Prem 三條路](/ai-coding-on-prem-three-paths/) 裡，「自建 GPU farm」這條路最大的痛點就是 token-per-dollar 算不過雲端 API。MTP drafter 把這個帳重算了。

對 Agent / Builder 的真實意義

如果你在做 agent 或 streaming 應用，這個更新有兩個直接影響：

1. Streaming UX

User 看 LLM 吐字，3x 速度的差別 = 等 30 秒 vs 等 10 秒。這是一個不需要解釋的體感升級。

2. Agent 多步推理 latency

Agent 一次任務常常要 LLM call 5-10 次。每次省 50% 時間，整體 latency 就從 30 秒掉到 15 秒。這在 agent 跟人機互動的耐心邊界上是決定性的差別。

我用 Claude Code 跑長任務時最大的痛點不是錢，是等。如果開源 agent 也能拿到這種加速，self-hosted Claude Code-like 的可行性會明顯往前走。

還沒解決的問題（誠實版）

不要把這個更新當銀彈。我列幾個還沒解決的：

品質不會掉，但延遲尾部會抖。 99 percentile latency 在 acceptance rate 低的時候會劣化，因為要重 decode。Production SLA 要重新測。

記憶體佔用會變多。 Drafter 雖然小，但要常駐 VRAM。23GB 的 26B MoE 加 drafter 後可能變 26-27GB，剛好踩到家用 24GB 卡的紅線。

Quantization 的 interaction 還沒看到深度測試。 4-bit 量化 + MTP drafter 的 acceptance rate 會不會掉？官方沒講。

不是所有 fine-tune 後的 Gemma 4 都能直接套這個 drafter。 Drafter 是針對 base model 訓的，重度 RLHF 後分布偏移可能讓 acceptance 掉，要重新驗證。

結論：3x 是頭條，KV cache 共享 + Apache 2.0 才是關鍵

回到開頭那個我想滑掉的標題。

「Gemma 4 變快 3x」 這件事本身，是行銷標題。 但 Google 這次的釋出做了三件對的事：

Drafter 跟主模型對齊 + KV cache 共享

整個 family 配齊（含邊緣版）

Apache 2.0 + 主流框架支援

這三件事加起來，等於把 speculative decoding 從「論文 + 高難度自訓 drafter」推到「ollama 一行指令」。

對想做 on-prem 推理、做 agent、做 self-hosted 的人，這是實質減負。對只想用 OpenAI / Anthropic API 的人，這跟你關係不大——但你的 Anthropic 帳單壓力越大，這個關係就會越大。

我自己接下來會做的事：

拿 26B MoE 在我那台 RTX 5090 上跑 benchmark，看家用卡能不能複製 Google 的數字

重算 [on-prem 三條路](/ai-coding-on-prem-three-paths/) 的 token-per-dollar

看 Cursor / Cline 之類的 client 多快會接 MTP

如果你也在跑 self-hosted inference，這篇釋出值得花一個下午試試 ollama 那條路。3x 拿不到，1.8x 對你的帳單也夠了。

延伸閱讀

官方來源：

[Google Blog — Multi-Token Prediction for Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

[Hugging Face — Google models](https://huggingface.co/google)

[Google AI Edge Gallery](https://ai.google.dev/edge)

Speculative decoding 學術淵源：

[arXiv 2211.17192 — Fast Inference from Transformers via Speculative Decoding (Google, 2022)](https://arxiv.org/abs/2211.17192)

[arXiv 2305.09781 — SpecInfer (DeepMind, 2023)](https://arxiv.org/abs/2305.09781)

[arXiv 2401.10774 — Medusa](https://arxiv.org/abs/2401.10774)

[arXiv 2401.15077 — EAGLE](https://arxiv.org/abs/2401.15077)

[arXiv 2412.19437 — DeepSeek V3 Technical Report (含 MTP head)](https://arxiv.org/abs/2412.19437)

推理框架支援：

[vLLM Speculative Decoding 文件](https://docs.vllm.ai/en/latest/features/spec_decode.html)

[SGLang Speculative Execution](https://docs.sglang.ai/)

[Ollama 模型庫](https://ollama.com/library)

[MLX (Apple)](https://github.com/ml-explore/mlx)

相關拆解：

[一張原價屋估價單，看懂 Token 經濟學如何把 DDR 打到天價](/ddr-hbm-token-economics-nvidia-lock-supply-chain/)

[非英語稅：用 Claude 寫中文 token 比英文版多 71%](/non-english-tax-tokenizer-cost-claude-openai/)

[AI Coding On-Prem 三條路](/ai-coding-on-prem-three-paths/)

[本地 LLM 企業架構](/local-llm-enterprise-architecture/)

[學界 GPU 飢荒](/academia-gpu-starvation-ai-era/)

常見問題 Q&A

Q: 3x 是不是真的，還是行銷數字？

是真的，但是 best case。實際拿到 2x–2.5x 比較常見，3x 要對的 batch、對的 task（structured output / code）、對的硬體。寫中文創作或長 chain-of-thought 推理通常拿不到。

Q: Speculative decoding 既然 2022 就有，為什麼現在才被廣傳？

兩個門檻過去擋住普及：(1) 自己訓 drafter 難度不低，要找對 size 跟分布對齊；(2) 推理框架整合不齊。Google 這次把訓好的 drafter 直接 Apache 2.0 釋出 + vLLM/SGLang/Ollama 都支援，把這兩個門檻一次砍平。

Q: 我用 Anthropic / OpenAI API，這個跟我有關係嗎？

短期沒有——你看不到背後是不是用 speculative decoding。長期有：Anthropic 跟 OpenAI 內部一定也在做類似優化，但他們不會降價，省下的成本是 margin。你想拿到推理優化的紅利，只有 self-host 一條路。MTP drafter 把 self-host 的可行性往前推了一格。

Q: 邊緣設備（手機）拿得到 3x 嗎？

拿不到 3x，但 E2B / E4B 邊緣版有自己的 drafter，加速幅度約 1.5x–2x（依硬體）。對 on-device assistant 來說已經是巨大的 UX 升級——AssistAt 之類的應用本來吐字慢到無法用，加速 1.5x 以後變成可以接受。

Q: 跟 DeepSeek V3 的 MTP head 有什麼不同？

兩個方向不太一樣：

DeepSeek V3 的 MTP 是訓練時就把多 token 預測當成 auxiliary loss 烘進主模型，主模型本身就能一次預測多個 token

Gemma 4 MTP drafter 是分離式 — 一個獨立 drafter 模型 + 一個獨立 target 模型，drafter 跟 target 對齊但結構分開

DeepSeek 的做法 token 加速幅度更大（不需要 verify 步驟），但要重訓。Google 的做法可以套在現有模型上，門檻低。實務上是兩種互補的路線。

Q: 要怎麼開始試？

最快路徑：

1

ollama pull gemma4:26b-mtp

（指令格式以 Ollama 官方為準）

或在 vLLM 直接啟用 speculative decoding，[官方文件這頁](https://docs.vllm.ai/en/latest/features/spec_decode.html) 有完整參數。

Q: 這會不會讓 Anthropic / OpenAI 降價？

短期不會。但這會逐步擠壓他們的中低端定位——當 self-hosted Gemma 4 26B + MTP 能用一張 RTX 5090 跑出 150 tokens/s，企業客戶會重新算「不敏感任務還要不要打 API」。我猜半年內會看到主流 SaaS 廠商把「中低端任務 route 到開源 self-hosted、高端 route 到 Claude」變成標準 pattern。

---
