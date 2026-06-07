# 🏢 Wisely Chen AI — 2026-05-22

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [Mac 用戶等了 16 個月：第一次能用「企業級」LLM 推理加速](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/)
*🏢 Wisely Chen AI | 2026-05-20*

## 目錄

  * [TL;DR](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#tldr)
  * [Mac 在 LLM 推理上的奇怪處境：硬體頂、軟體底](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#mac-在-llm-推理上的奇怪處境硬體頂軟體底)
  * [為什麼 vLLM / SGLang / TensorRT-LLM 永遠不會支援 Apple Silicon](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#為什麼-vllm--sglang--tensorrt-llm-永遠不會支援-apple-silicon)
  * [過去 16 個月 Mac 用戶的「次優」清單](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#過去-16-個月-mac-用戶的次優清單)
  * [PR #22673 對 Mac 用戶的意義：從鎖死到打開](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#pr-22673-對-mac-用戶的意義從鎖死到打開)
  * [為什麼 Mac 應該拿到比 NVIDIA 卡更大的 MTP 紅利](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#為什麼-mac-應該拿到比-nvidia-卡更大的-mtp-紅利)
  * [誠實揭露：Mac 還沒追上的部分](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#誠實揭露mac-還沒追上的部分)
  * [對企業 IT 架構師意味著什麼](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#對企業-it-架構師意味著什麼)
  * [常見問題 Q&A](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/#常見問題-qa)



## TL;DR

  * **Mac 不能跑 vLLM、SGLang、TensorRT-LLM** ——沒 CUDA、沒 ROCm，根本起不來
  * 過去 16 個月 Mac 跑 LLM 的所有路徑（llama.cpp / MLX / Ollama / LM Studio）**全部沒有 MTP 支援** ——意思是 Mac 用戶完全用不到 DeepSeek V3、Qwen3.6 這些模型的內建加速能力
  * 2026-05-16 llama.cpp PR #22673 merge 之後，**Mac 第一次有「enterprise tier」的推理加速技術可以用**
  * 預期 Mac Studio / Mac mini 拿到的 MTP 加速會**接近 PR 描述的 2.5x（接近頻寬瓶頸機型的紅利上限）** ，而不是 RTX 3090 的 1.71x——因為 Apple Silicon 統一記憶體本來就是頻寬 bound 的架構
  * 對企業 IT 架構：**公司原本就配發 Mac 給工程師的，現在不用再買 NVIDIA on-prem 機器，也能用生產級推理**



* * *

## Mac 在 LLM 推理上的奇怪處境：硬體頂、軟體底

從硬體規格表來看，Mac Studio M3 Ultra 是一台很奇怪的機器。

機器 | 統一記憶體 / VRAM | 記憶體頻寬 | 價格  
---|---|---|---  
**Mac Studio M3 Ultra（頂規）** | **512GB** 統一記憶體 | ~819 GB/s | ~$14,000  
**Mac Studio M3 Ultra（中階）** | **256GB** 統一記憶體 | ~819 GB/s | ~$7,400  
RTX 5090 | 32GB GDDR7 | 1,792 GB/s | $2,000（卡）+ 整機  
RTX 4090 | 24GB GDDR6X | 1,008 GB/s | $1,600（卡）+ 整機  
DGX Spark | 128GB LPDDR5X | ~273 GB/s | $4,699  
  
Mac Studio 的優勢非常具體：**整顆 Qwen3.6-27B FP16（54GB）能直接塞進 256GB 統一記憶體，連量化都不用** 。RTX 5090 必須先量化到 Q4 / FP8 才塞得進 32GB VRAM——這是檔位的差距。

換句話說：

**如果只看「能不能跑」，Mac Studio M3 Ultra 是家用機器的天花板。**

那為什麼過去一年講本地 LLM 的場合，大家總是先講 NVIDIA 卡？因為**軟體棧上 Mac 被 lock out 於所有現代推理加速技術** 。硬體能扛模型權重，但跑得很「素」——只有最基本的 autoregressive decoding，沒有 speculative decoding、沒有 multi-token prediction、沒有 EAGLE / Medusa 這類 draft model 加速。

這是一個典型的「硬體頂、軟體底」處境。

## 為什麼 vLLM / SGLang / TensorRT-LLM 永遠不會支援 Apple Silicon

要理解為什麼 Mac 用戶被 lock out 這麼久，得先理解這些 enterprise 推理框架的技術棧。

框架 | 底層依賴 | 在 Mac 上能跑嗎  
---|---|---  
**vLLM** | CUDA / ROCm / TPU | ❌ 完全跑不起來  
**SGLang** | CUDA / ROCm | ❌ 完全跑不起來  
**TensorRT-LLM** | CUDA + TensorRT | ❌ NVIDIA 獨家  
**DeepSpeed-Inference** | CUDA | ❌ 跑不起來  
  
這些框架的核心優化（FlashAttention、PagedAttention、continuous batching、speculative decoding kernel）**全部是用 CUDA kernel 寫的** 。要在 Apple Silicon 上跑，等於整個 kernel 層要重寫成 Metal——這不是 porting 工作，是重做一份。

**這件事永遠不會發生** ，因為：

  1. **市場規模不對** ：vLLM / SGLang 的主要市場是雲端 GPU 推理服務商，Mac 在這個市場根本不是 target
  2. **資源優先級不對** ：DeepSeek、Anthropic、OpenAI 內部用 NVIDIA H100 / H200 推理，PR 都優先給 NVIDIA 平台
  3. **Apple 自己有 MLX** ：Apple 不會去推動別人優化 Apple Silicon，他們押在自己的 MLX 框架



所以結論很清楚：**Mac 想用 enterprise tier 的推理加速，唯一的路是 llama.cpp 把這些 feature 一個一個 backport 進來** 。

而 llama.cpp 是一個志願者社群 + 部分商業贊助的開源專案，feature 速度當然比不上有完整工程團隊的 vLLM。所以 Mac 用戶享受 enterprise tier feature 的時間差，就是「論文發表 → vLLM 實作 → llama.cpp backport」這個 pipeline 的延遲。

過去這個延遲是**16 個月** （MTP 從 DeepSeek V3 release 到 llama.cpp merge）。

## 過去 16 個月 Mac 用戶的「次優」清單

期間 Mac 用戶不是完全沒得跑——只是每個選擇都有明顯的「不夠專業」之處。

**1\. llama.cpp + Metal backend**

  * ✅ 跨平台、跨 Apple 全產品線
  * ✅ 量化支援完整（GGUF）
  * ❌ 沒 MTP、沒 EAGLE、沒 Medusa
  * ❌ Metal kernel 通常比 CUDA kernel 慢 30-50%



**2\. MLX（Apple 自家框架）**

  * ✅ 對 Apple Silicon 架構優化最好
  * ✅ 跟 PyTorch API 接近，研究友善
  * ❌ **沒有原生 MTP 支援** （即使 Apple 自己也沒做）
  * ❌ 量化支援比 GGUF 弱
  * ❌ 模型生態小（很多模型沒人轉成 MLX 格式）



**3\. Ollama / LM Studio**

  * ✅ 一鍵安裝、UI 友善
  * ❌ 底層是 llama.cpp，繼承所有 llama.cpp 的限制
  * ❌ Release cadence 比 llama.cpp 還慢（要等 upstream 更新後再 bump）



**4\. Rapid-MLX（社群專案，相容 OpenAI API）**

  * ✅ 在 [Qwen3.6-27B 跑出 36.5 t/s @ M3 Ultra](https://ai-coding.wiselychen.com/qwen-3-6-27b-gb10-home-inference-sonnet-level/)（4-bit）
  * ❌ 還是沒 MTP



把這四條路擺在一起，會發現一個尷尬的事實：**Mac 用戶過去一年想用 MTP，沒有任何一條路走得通** 。不是「麻煩但能用」，是「根本沒這條路」。

## PR #22673 對 Mac 用戶的意義：從鎖死到打開

這是這篇文章的核心：**llama.cpp PR #22673（2026-05-16 merge）是 Mac 用戶能用 MTP 的第一條路** 。

不是「現在多了一個選項」，是「**從零到一** 」。

具體解鎖了什麼？

**1\. MTP 在 Metal backend 上可運作** PR 描述明寫了支援 CUDA、Metal、Vulkan 三個 backend。意思是 M1 / M2 / M3 / M4 系列、Mac Studio / Mac mini / MacBook Pro / iMac，**全產品線都能用** 。

**2\. 不需要重新下載模型** GGUF 檔案裡如果原本就有 MTP heads 的 tensor（DeepSeek V3 / R1、Qwen3.6 系列），llama.cpp 升版後直接讀。已經下載的權重不浪費。

**3\. 跟現有工具鏈相容** LM Studio、Ollama、KoboldCpp 全部底層是 llama.cpp。預計 1-2 個月內這些工具會 bump 版本，使用者完全不用懂 `--spec-type mtp` 這種 flag，背後就自動開啟。

換句話說：**正在用 Mac Studio 跑 LM Studio 的工程師，再過幾週升級到下一個版本，speed 就會自動變 1.7x-2.5x** 。沒有人需要做任何事。

## 為什麼 Mac 應該拿到比 NVIDIA 卡更大的 MTP 紅利

這是技術上最有意思的一段，也是這個 PR 對 Mac 用戶**特別** 重要的原因。

MTP 的核心紅利是「**同一次 memory access 算出多個 token** 」。直白講：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    傳統 autoregressive：
      讀一次權重 → 算 1 個 token → 讀一次權重 → 算 1 個 token ...
    
    MTP：
      讀一次權重 → 同時算出 N 個 token 草稿 → 驗證 → 接受 K 個
      
  
---|---  
`

那什麼樣的硬體會從 MTP 拿到最大紅利？答案是**記憶體頻寬 bound 的硬體** 。

對照 PR 描述跟社群實測的加速倍率：

硬體 | 加速倍率 | 為什麼  
---|---|---  
**DGX Spark** （273 GB/s 頻寬） | **2.57x** | 頻寬最差 → 紅利最大  
**RTX 3090** （1008 GB/s 頻寬） | **1.71x** | 頻寬充足 → 紅利縮水  
**RTX 5090** （1792 GB/s 頻寬） | **~1.87x** （我自己實測） | 頻寬最好 → 紅利再縮  
  
**規律很清楚：頻寬越緊張的硬體，MTP 加速越大。**

那 Mac Studio M3 Ultra 落在哪？**819 GB/s** 。比 DGX Spark 寬，但比 RTX 3090 緊。

更關鍵的是：**Apple Silicon 統一記憶體架構本來就是「記憶體頻寬 bound」設計** 。CPU、GPU、Neural Engine 共享同一條記憶體匯流排，這條匯流排是整個系統的天花板。

所以我的預期是：**Mac Studio M3 Ultra 跑 Qwen3.6-27B 開 MTP，加速倍率會落在 2.0x ~ 2.4x 區間** ，比 RTX 5090 上的 1.87x 更好。

如果這個預期成立，意思是：

  * M3 Ultra 跑 Qwen3.6-27B 在沒 MTP 時大概 20-25 t/s（社群實測）
  * 開 MTP 之後預期會到 **45-55 t/s 單流**
  * 這個速度對「一個工程師、一個 chat 框」的 interactive coding 場景**完全夠用**



對比 Sonnet 4.6 API 的 60-80 t/s streaming，Mac Studio 跟商業 API 的差距會縮到 1.5x 以內——而且沒有網路延遲、沒有 rate limit。

## 誠實揭露：Mac 還沒追上的部分

寫到這裡得潑點冷水。Mac 用上 MTP 不代表追平 NVIDIA。

**1. Metal kernel 效率還是輸 CUDA kernel** 即使有 MTP，底層的 attention / matmul kernel 在 Apple Silicon 上的實作通常比 CUDA 慢 20-40%。MTP 給的是「整體吞吐」的加速，不會修補 kernel 層的差距。

**2. MLX 還沒有 MTP** Apple 自家的 MLX 框架到 2026 年 5 月為止還沒實作 MTP。如果你的 workflow 是 MLX-based（例如用 mlx-lm 寫研究 code），這個 PR 對你沒用，要等 MLX 團隊跟進。

**3. 並發場景 Mac 還是輸** 跟 NVIDIA 卡一樣，llama.cpp + MTP 目前強制 `n_parallel=1`。如果你想用 Mac Studio 服務團隊（5-10 人同時用），這個 setup 不適合，要切回沒 MTP 的設定。但因為 vLLM 不支援 Mac，所以 Mac 在「並發 serving」這個場景**沒有好答案** 。

**4. 實測數字還沒大量出現** PR 才 merge 一週多，Mac 用戶的實測 benchmark 還沒充分湧現。我前面講的「2.0x-2.4x 預期」是基於頻寬論證，不是實測。實際數字要再等幾週社群 benchmark 累積。

**5. M1 / M2 機器加速可能比 M3 / M4 小** PR 用了一些新的 ggml 操作，這些操作在 M3 / M4 上有專門優化，M1 / M2 可能落到 fallback 路徑，加速幅度會縮水。

## 對企業 IT 架構師意味著什麼

這次解鎖最關鍵的影響是**改寫了 Mac 在企業 AI 架構裡的角色** 。

過去六個月，企業評估 on-prem AI Coding 的標準答案是：

  * 買 DGX Spark / RTX 5090 工作站
  * 跑 Qwen3.6-27B / DeepSeek V3
  * 跑 vLLM 服務多個工程師



這個方案的問題是「**多了一份硬體 + 多了一份運維** 」。很多矽谷公司本來就配發 Mac Studio 或 MacBook Pro 給工程師——這些機器原本只是「終端」，不是「推理 server」。

PR #22673 改變了這個假設：

**配發給工程師的 Mac Studio M3 Ultra 256GB** ，本身就是一台**單人推理 server** 。

  * 硬體扛得動 Qwen3.6-27B 不量化版本
  * 軟體（llama.cpp + MTP）給出 enterprise tier 加速
  * 速度預期 45-55 t/s，interactive coding 完全夠用
  * 不用任何額外採購、不用 IT 部署 K8s



這對 IT 架構的意義：

**1. on-prem AI Coding 的 TCO 重算** 原本要算「採購 NVIDIA 工作站 + 運維」，現在可以走「公司本來就配的 Mac，多開一個推理 process」。TCO 直接砍掉硬體採購線。

**2. 資安合規場景多一個答案** 金融 / 法律 / 醫療這些不能 call cloud API 的場景，過去的答案是「on-prem NVIDIA」，現在多了「員工自帶 Mac Studio 跑本地推理」這個選項。資料完全不離開員工那台機器。

**3. 不同團隊的工具策略可以分流**

  * **研發團隊（個人工作流）** ：MacBook Pro / Mac Studio + LM Studio + MTP → 個人單流
  * **平台團隊（共用服務）** ：NVIDIA 工作站 + vLLM + AWQ + 並發 batching → 多用戶
  * **這兩條路不衝突，可以同時走**



換個方式講：**Mac 在 LLM 推理上從「次優選擇」升級成「特定場景的最佳選擇」** ——特別是「一人一台、不需要共享、不能上雲」這類場景。

## 常見問題 Q&A

**Q: 我用 Mac mini M4 / MacBook Pro M3，這個更新有用嗎？**

有用，但效果取決於記憶體大小。M4 Mac mini（24GB / 32GB）能跑 Qwen3.6-27B Q4 量化版本（約 16GB），開 MTP 預期加速 1.8x-2.2x。MacBook Pro M3 Max（36GB / 64GB / 128GB）可以跑更大模型，加速幅度類似。

**Q: 我已經在用 LM Studio，需要做什麼？**

短期內不用做什麼。等 LM Studio 下一版升上 llama.cpp 的新 master（樂觀估計 1-2 個月內），更新後 MTP 會自動啟用。如果你想立刻試，可以直接編譯 llama.cpp master + 手動下 CLI。

**Q: MLX 跟 llama.cpp，Mac 用戶該選哪個？**

短期內如果重視速度，選 llama.cpp（有 MTP）。如果你的工作流是研究 / fine-tuning / 需要 PyTorch-like API，繼續用 MLX。中期看 MLX 會不會跟進 MTP——如果跟進了，MLX 在 Apple Silicon 上的 kernel 效率本來就比 llama.cpp 好，到時會反超。

**Q: Mac Studio M3 Ultra 跟 RTX 5090 該怎麼選？**

不是同個量級的決策。RTX 5090 適合「跑量化模型 + 並發 serving + 想用 vLLM 整套」；Mac Studio M3 Ultra 適合「跑大模型不量化 + 單人 interactive + 安靜省電」。如果你已經有 Mac，加 MTP 是免費升級；如果還沒買，看你的 workload 偏哪邊。

**Q: 為什麼說 MTP 是「enterprise tier」？**

因為過去這項技術只在 vLLM / SGLang / TensorRT-LLM 這些企業推理棧裡可用——換句話說，要享受 MTP 的人要有 CUDA 卡、要會起 Python server、要懂 deployment。家用 GGUF 路線（llama.cpp / Ollama / LM Studio）的使用者完全用不到。PR #22673 把這個技術從 enterprise tier 下放到家用 tier，而 Mac 是這次下放的最大受益者——因為 Mac 連 enterprise tier 都進不去。

* * *

## 結語

PR #22673 對大多數人來說是「llama.cpp 又更新一個 feature」，但對 Mac 用戶來說是**整整 16 個月的等待結束** ——第一次能用上跟 H100 推理伺服器同等級的加速技術。

更有意思的是，從頻寬論證來看，Mac 拿到的紅利可能比 NVIDIA 消費卡還大。

我接下來會在我朋友的 Mac Studio M3 Ultra 256GB 上實測 Qwen3.6-27B 開 MTP 前後的數字，搭配前面 [RTX 5090 跑出 140 tok/s 的 benchmark](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/) 做完整對照。預期會看到 Mac 的相對加速幅度大過 RTX 5090——但具體數字要實測才算。

數據出來再分享。

* * *

**相關文章：**

  * [llama.cpp 終於合併 MTP：你的 DeepSeek / Qwen3.6 一直少跑了 30-60% 的速度](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/)
  * [Qwen 3.6-27B 在 RTX 5090 上的 inference engine benchmark](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)
  * [Qwen 3.6-27B 在 DGX Spark 跑出 Sonnet 4.6 等級](https://ai-coding.wiselychen.com/qwen-3-6-27b-gb10-home-inference-sonnet-level/)



**參考資料：**

  * [llama.cpp PR #22673: llama + spec: MTP Support](https://github.com/ggml-org/llama.cpp/pull/22673)
  * [vLLM Speculative Decoding docs (MTP)](https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/)
  * [Reddit: r/LocalLLaMA “That’s a good news…”](https://www.reddit.com/r/LocalLLaMA/comments/1teqnf2/thats_a_good_news/)

---

## [llama.cpp 終於合併 MTP：你的 DeepSeek / Qwen3.6 一直少跑了 30-60% 的速度](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/)
*🏢 Wisely Chen AI | 2026-05-20*

## 目錄

  * [TL;DR](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#tldr)
  * [那則 776 讚的 Reddit 截圖，慶祝的是什麼](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#那則-776-讚的-reddit-截圖慶祝的是什麼)
  * [MTP 到底是什麼？一句話版本](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#mtp-到底是什麼一句話版本)
  * [三組硬體實測：2.5x、1.71x、74%](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#三組硬體實測25x171x74)
  * [為什麼速度沒有翻三倍：72% 的接受率](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#為什麼速度沒有翻三倍72-的接受率)
  * [反直覺洞察：你的 GGUF 一直跑半速](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#反直覺洞察你的-gguf-一直跑半速)
  * [誠實揭露：MTP 不是免費午餐](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#誠實揭露mtp-不是免費午餐)
  * [最大受益者其實不是 NVIDIA 用戶——是 Mac](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#最大受益者其實不是-nvidia-用戶是-mac)
  * [對企業 on-prem 架構師意味著什麼](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#對企業-on-prem-架構師意味著什麼)
  * [常見問題 Q&A](https://ai-coding.wiselychen.com/llama-cpp-mtp-merged-local-llm-2x-speedup/#常見問題-qa)



## TL;DR

  * **2026-05-16，llama.cpp PR #22673 合併** ，原生支援 Multi-Token Prediction（MTP）speculative decoding
  * 社群實測：DGX Spark 跑 Qwen3.6-27B **7.0 → 18.0 tok/s，2.57x** ；RTX 3090 **38.86 → 65 tok/s，1.71x**
  * **我自己在 RTX 5090 上實測 Qwen3.6-27B + MTP 拿到 140 tok/sec 單流、70%+ acceptance rate** ，跟 PR 描述的 72.18% 幾乎重疊
  * **這次 PR 真正的最大受益者其實是 Mac 用戶** ——vLLM / SGLang / TensorRT-LLM 永遠不會支援 Apple Silicon，Mac 用戶過去 16 個月想用 MTP「沒有任何一條路」。詳見另一篇 [Mac 用戶等了 16 個月：第一次能用「企業級」LLM 推理加速](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/)
  * 不是「新模型」新聞，是「inference 框架終於追上模型架構」的新聞——DeepSeek-V3 從 2024 年底就有 MTP heads，**本地用戶等了快一年才能真正按下這個按鈕**
  * 限制：只對「訓練時就帶 MTP head」的模型有效（DeepSeek-V3/R1、Qwen3.6 系列），而且目前 `n_parallel=1`，多用戶場景 vLLM + AWQ 還是壓倒性勝利



* * *

## 那則 776 讚的 Reddit 截圖，慶祝的是什麼

事情是這樣的。

5 月 16 日，r/LocalLLaMA 上有人貼了一張 PR 已 merge 的截圖，標題寫 “That’s a good news…“，內文只有兩句話：

> “Looks like it finally happens… MTP getting approved for llama.cpp. Time to prepare for the update.”

兩天內 776 upvotes、242 條留言。對一個技術 PR merge 的反應來說，這個熱度是不太尋常的。

但你要理解為什麼大家這麼激動，得先回到 2024 年底——DeepSeek-V3 release 的那一刻，模型架構裡就已經內建了 MTP heads，官方論文宣稱可以拿到 **1.8x** TPS 加速。

問題是，這個能力**只有 DeepSeek 自己的 inference 伺服器跟 SGLang / vLLM 用得起來** 。本地用 llama.cpp 跑 GGUF 的人，等於拿了一台跑車但沒拿到鑰匙。

整整一年。

5 月 16 日，鑰匙終於發下來了。

## MTP 到底是什麼？一句話版本

**MTP = 模型自己當自己的 draft model。**

過去要做 speculative decoding，你得跑「大模型 + 小模型」兩顆——小模型先猜幾個 token，大模型驗證。聽起來合理，但實務上很煩，因為你要為每個大模型找一顆「夠像但夠小」的搭檔。

MTP 的做法是：訓練時就在大模型裡多裝幾個 prediction head，讓它一次 forward pass 就能吐出「下一個 token + 接下來幾個草稿 token」。然後主模型自己驗證自己的草稿。

對使用者來說，這意味著：

  * 不用找 draft model
  * 不用多載一份 KV cache（雖然實作上 MTP head 還是有自己的 context）
  * 接受率比外掛 draft model 高很多，因為這些草稿頭是「同一個模型自己的延伸」



llama.cpp 的開法很簡單：
    
    
    1
    

| 
    
    
    --spec-type mtp --spec-draft-n-max 3
      
  
---|---  
`

第二個參數是草稿幾個 token，社群目前測下來 **3 是個甜蜜點** 。

## 三組硬體實測：2.5x、1.71x、74%

這是這次最有意思的部分——同一個 feature 在不同硬體上加速幅度差很大。

硬體配置 | 模型 | Baseline | MTP 開啟 | 加速倍率  
---|---|---|---|---  
**DGX Spark** （$4,699 家用 AI 工作站） | Qwen3.6-27B | 7.0 tok/s | 18.0 tok/s | **2.57x**  
**RTX 3090** | Qwen3.6-27B | 38.86 tok/s | 65-67 tok/s | **1.71x**  
**3x RTX 3060** （社群實測） | Qwen3.6-27B | - | - | **+74%**  
**SGLang + AMD MI300** （DeepSeek-V3，非 llama.cpp） | - | - | - | 1.25-2.11x（Random）/ 1.36-1.80x（ShareGPT）  
  
幾個觀察：

**第一，記憶體頻寬瓶頸越嚴重的機器，加速越誇張。** DGX Spark 拿 2.57x 的原因是它本來就是頻寬瓶頸機（128GB 統一記憶體但頻寬不如 RTX 3090），MTP 等於把「同一次 memory access 多算幾個 token」的紅利吃滿。

**第二，RTX 3090 從 38 → 65 tok/s 不算誇張，但意義很大。** 因為 27B 在消費卡上本來就接近實用門檻，1.71x 等於從「勉強用」變成「順順用」。

**第三，SGLang 跑 DeepSeek-V3 的 1.25-2.11x 區間揭露了一個重點：concurrency 越高，MTP 加速越小** 。AMD 那邊測 1、2、4、8、16、32、64 user 的場景，倍率是遞減的——這也是為什麼 llama.cpp 目前的實作直接強制 `n_parallel=1`。

## 為什麼速度沒有翻三倍：72% 的接受率

PR 描述裡有一個關鍵數字：**Aggregate acceptance rate 72.18%** 。

意思是：模型每草稿 3 個 token，平均有 2.16 個會通過自己的驗證、被接受寫入輸出。剩下的 0.84 個被丟掉、重算。

這就是為什麼你看到的加速是 1.7x ~ 2.5x，不是 3x ~ 4x：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    理論上限 = 1 + n_draft × acceptance_rate
            = 1 + 3 × 0.72
            = 3.16x（不含驗證 overhead）
    
    實際 = 約 1.7x ~ 2.5x（含驗證跟 KV 寫入 overhead）
      
  
---|---  
`

接受率為什麼是 72% 不是 95%？因為 MTP head 雖然跟主模型同源，但它預測「未來 N 個 token」的時候只看到當下的 hidden state——本質上還是一個近似。

這也呼應到一個有意思的點：**任務越「可預測」，加速越大** 。寫 boilerplate code、補全 API call 這種 acceptance rate 會接近 80-85%；寫複雜推理或創意文字會掉到 60% 以下。

DataCamp 那篇 tutorial 實測就觀察到，跑 AIME 數學題的時候速度從 65 tok/s 掉回 56-61 tok/s——還是比 baseline 快，但加速幅度縮水。

## 反直覺洞察：你的 GGUF 一直跑半速

這篇文章真正想講的是這件事。

過去一年，本地 LLM 圈花很多時間在優化「能跑哪些模型」、「量化能壓多狠」、「kernel 能調多快」。所有這些優化都在原本的 single-token autoregressive 框架裡卷。

但事實是：**DeepSeek-V3 / Qwen3.6 這幾顆主流開源大模型，從訓練的第一天就準備好了 multi-token 模式** 。權重裡的 MTP heads 一直躺在你硬碟上，只是 llama.cpp 不知道怎麼讀。

換個說法：

  * 如果你 2025 年 1 月 download 了 DeepSeek-V3 GGUF 開始本地推理
  * 到 2026 年 5 月 16 日為止，**你大概率一直在跑半速**
  * 不是你的硬體不夠，不是你 prompt 寫得不好，不是量化太狠
  * 是 inference 框架沒實作這個功能



這個 gap 大概有 16 個月。

對企業 IT 架構決策來說這件事的啟示是：**模型架構的進度跟 inference 框架的進度，從來不是同步的** 。當你算 on-prem AI Coding 的 ROI 時，你算的是「今天的軟體跑今天的硬體跑今天的模型」這個快照——但那個快照六個月後可能因為一個 PR merge 就翻一倍。

### 把這件事接回我自己手上的數字

這次 PR merge 對我有點不一樣，因為我**已經在 RTX 5090 上實測過 MTP 了** ——上一篇 [Qwen 3.6-27B 在 RTX 5090 上的 inference engine benchmark](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/) 跑了 7 組配置，其中一組就是 llama.cpp + Q2_K_XL + MTP，結果如下：

配置 | 單流（1 user） | 並發（8 users）  
---|---|---  
vLLM + AWQ-INT4 + cudagraph | 80.5 tok/s | **575 tok/s** ⭐  
**llama.cpp + Q2_K_XL + MTP** | **140 tok/s** ⭐ | 118 tok/s  
llama.cpp + Q4_K_M（無 MTP） | 75 tok/s | 189 tok/s  
Ollama + Q4_K_M | 67 tok/s | 64 tok/s  
  
幾個對照重點：

**第一，PR 描述的 acceptance rate 72%，我實測到 70%+** ——兩個數字幾乎重疊，這驗證了 MTP head 的品質在不同硬體 / quant 設定下相當穩定，不是 cherry pick 出來的數字。

**第二，單流 140 tok/sec 跟同模型 llama.cpp Q4_K_M 無 MTP 的 75 tok/sec 對比，加速約 1.87x** ——落在前面講的 1.7x-2.5x 區間，跟 PR 報的 RTX 3090 上 1.71x 接近。

**第三，並發場景的 trade-off 在這張表上一目了然** ：

  * vLLM 在 8 users 並發拉到 575 tok/s（continuous batching 的紅利）
  * 但 llama.cpp + MTP 並發反而從 140 掉到 118 tok/s——這就是前面說的 `n_parallel=1` 限制具體長什麼樣



換句話說：**MTP 不是「一定贏」的優化** 。如果你的場景是 single-stream interactive coding（工程師一個 session 對話），MTP 是免費午餐；如果是 batch inference / 多用戶 API server，vLLM + AWQ 還是壓倒性勝利。

**第四，140 tok/sec 單流是什麼概念？** Sonnet 4.6 透過 API 拿到的 streaming 速度大概 60-80 tok/sec（看時段跟 region）。**一張 RTX 5090（市價 $2,000 美金等級）跑 Qwen3.6-27B 開 MTP，單流速度直接是 Anthropic API 的 1.75 倍** ——而且沒有網路 round-trip、沒有共用佇列、沒有 rate limit。

## 誠實揭露：MTP 不是免費午餐

寫到這裡得潑點冷水。

**1. 不是所有模型都能用**

只有「訓練時就帶 MTP heads」的模型才能開。目前確認支援的：

  * DeepSeek-V3、DeepSeek-R1（包含 distill 版本）
  * Qwen3.6-27B、Qwen3.6-35BA3B



Llama 3 系列、Mistral、Gemma 這些**沒有 MTP head** ，這個 PR 對它們沒用。你只能繼續走傳統 speculative decoding（找一顆 draft model）那條路。

**2. 目前 server 多用戶場景不能用**

PR merge 後的版本強制 `n_parallel=1`。如果你的 on-prem 架構是「一台機器服務十個工程師」，這個 feature 暫時還不適合你。社群在討論 batching 支援，但需要時間。

**3. Acceptance rate 變數很大**

前面講過，任務越創意 / 越長 reasoning，acceptance rate 掉得越凶。如果你的 workload 主要是長 reasoning chain（agentic coding 中後段、複雜數學），實際加速可能只有 1.3x ~ 1.5x。

**4. 多了 device-to-host embedding transfer overhead**

PR 描述裡明寫了，prompt processing 階段會多一份 embedding 傳輸成本。short prompt + long generation 場景拿到最大紅利，long prompt + short generation 場景紅利會被吃掉。

## 最大受益者其實不是 NVIDIA 用戶——是 Mac

寫到這裡有一個視角必須補上，因為它跟「能拿到多少加速倍率」這個技術問題其實是分開的。

NVIDIA 用戶這次的故事是「**從用 vLLM 麻煩變成用 llama.cpp 輕鬆** 」——本來門就是開的，只是要走樓梯，現在多了一個電梯。

但 Mac 用戶的故事完全不一樣，是「**從鎖死變成打開** 」。

具體講：

推理棧 | NVIDIA 卡 | Mac (Apple Silicon)  
---|---|---  
vLLM + MTP | ✅ 早就支援（2025 初） | ❌ 完全跑不了（沒 CUDA）  
SGLang + MTP | ✅ 早就支援 | ❌ 完全跑不了  
TensorRT-LLM + MTP | ✅ NVIDIA 獨家 | ❌ 永遠不會支援  
**llama.cpp + MTP（2026-05-16）** | ✅ **新解鎖** | ✅ **新解鎖**  
  
對 NVIDIA 用戶：MTP 在 2025 年初就能用了，只是要會起 vLLM。

對 Mac 用戶：**過去 16 個月「沒有任何一條路」能用到 MTP** ——llama.cpp 沒做、Ollama / LM Studio 跟在 llama.cpp 後面、MLX 也沒做、Apple 自己也沒做。

更有意思的是，從**記憶體頻寬論證** 來看，Mac Studio 拿到的 MTP 紅利應該**大過 RTX 5090** ——因為 MTP 的核心紅利是「同一次 memory access 算多個 token」，越是頻寬 bound 的硬體越受惠。Apple Silicon 統一記憶體架構天生就是頻寬 bound。

這個推論細節跟 Mac 視角的完整論證，我寫在另一篇：[Mac 用戶等了 16 個月：第一次能用「企業級」LLM 推理加速](https://ai-coding.wiselychen.com/mac-first-enterprise-inference-stack-mtp/)。

對 IT 架構師來說，這意味著一件具體的事：**公司本來就配 Mac 給工程師的，Mac Studio M3 Ultra 256GB 本身就可以變成一台單人推理 server** ——不用再買 NVIDIA 工作站。

## 對企業 on-prem 架構師意味著什麼

我們團隊在做企業 on-prem AI Coding 評估的時候，這次 PR merge 大概會改變三件事：

**1. 重新算成本模型**

如果你的 on-prem 架構評估是 6 個月前做的，數字幾乎肯定過時。一台跑 Qwen3.6-27B 的機器，throughput 帳面上要加 1.7x ~ 2.5x。這個倍率落到每月帳上會很可觀。

**2. 重新看模型選型**

過去選 Llama 3 系列或 Mistral 的，現在要回頭看 DeepSeek / Qwen3.6——不只是因為 benchmark 數字，是因為它們**架構上就比較適合本地推理** 。MTP heads 是這個差距的具體表現。

**3. 重新評估 inference 框架的 release cadence**

llama.cpp 不是慢，是它要支援的硬體 / OS / 模型架構組合太多。如果你的公司在押本地推理，要把「inference 框架的 feature roadmap」當成跟模型 release 同等重要的觀察對象——這次的 MTP 是一個例子，下次可能是某個新的 attention kernel。

換個方式講：**選 on-prem 不只是選模型，是選一個三條時間線的交集** ——模型 release、inference 框架 feature、硬體更新。任何一條突進，整個 ROI 公式都要重算。

## 常見問題 Q&A

**Q: 我用 Ollama / LM Studio，要怎麼用到這個？**

短期內還用不到。Ollama 跟 LM Studio 都基於 llama.cpp，但有自己的 release cadence。樂觀估計 1-2 個月後會跟進，但你要等他們的版本 bump，不會 PR merge 隔天就有。

**Q: 一定要重新下載模型嗎？**

不用。GGUF 檔本身已經包含 MTP heads（如果模型訓練時有的話），llama.cpp 之前只是不知道怎麼讀那個 tensor。升級 binary 就好。

**Q: 對 MoE 模型（Qwen3.6-35BA3B）效果如何？**

社群測下來加速幅度跟 dense model 接近。MTP 跟 MoE 是兩個正交的優化——MTP 是「一次預測多個 token」，MoE 是「每個 token 只激活部分專家」，兩個疊起來用沒問題。

**Q: 我可以用 MTP 訓練我自己的小模型嗎？**

可以，但這是 pretraining 階段就要決定的——MTP heads 是模型結構的一部分。你沒辦法在訓練完後「加裝」MTP 進去（雖然有些 paper 在嘗試 self-distillation 做法，例如 arxiv 2509.18362 的 FastMTP）。

**Q: 這跟 EAGLE / Medusa 那些 speculative decoding 框架是什麼關係？**

概念上接近——都是「不要外掛 draft model，用模型自己預測多 token」。差別是 EAGLE / Medusa 是「post-hoc 加裝」，MTP 是「pretraining 內建」。內建的版本架構整潔、品質穩定，但你得在訓練時就決定。

* * *

## 結語

776 個 upvotes 慶祝的不是一個新功能，是一段被閒置一年的算力終於可以用了。

對技術人來說這是好消息，對企業架構師來說這是提醒——你 6 個月前算的 ROI 假設，可能因為一個 PR merge 就要全部重算。

我之前在 [RTX 5090 上跑 Qwen3.6-27B + MTP 已經拿到 140 tok/sec 單流](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)，acceptance rate 70%+，跟這次官方 PR 描述的 72.18% 幾乎吻合。

接下來會做的是**並發場景的深度測試** ——MTP 在 single-stream 已經贏了，但在企業多用戶情境下到底要不要切回 vLLM + AWQ，這條決策曲線值得畫清楚。數據出來再分享。

* * *

**參考資料：**

  * [Reddit: r/LocalLLaMA “That’s a good news…”](https://www.reddit.com/r/LocalLLaMA/comments/1teqnf2/thats_a_good_news/)
  * [llama.cpp PR #22673: llama + spec: MTP Support](https://github.com/ggml-org/llama.cpp/pull/22673)
  * [DataCamp: Multi-Token Prediction Tutorial with llama.cpp](https://www.datacamp.com/tutorial/multi-token-prediction-llama-cpp)
  * [AMD ROCm Blog: Efficient LLM Serving with MTP — DeepSeek V3 and SGLang](https://rocm.blogs.amd.com/software-tools-optimization/mtp/README.html)
  * [FastMTP: Accelerating LLM Inference with Enhanced Multi-Token Prediction (arxiv 2509.18362)](https://arxiv.org/pdf/2509.18362)

---

## [Jack of All Trades vs Master of One：AI 時代，你該賭哪條路？](https://ai-coding.wiselychen.com/jack-of-all-trades-ai-era-combination-scarcity/)
*🏢 Wisely Chen AI | 2026-05-19*

上週 Susan Zhang 在 X 上發了一條推文，27 萬次查看：

> “there is no better time in tech than now to be a jack of all trades, master of a few. just make sure to keep adding to the few year over year, such that the cumulative breadth of expertise you collect becomes an increasingly rare combo. remember, if you’re top 10% in 3 different areas, that already makes you top 0.1%.”

留言裡馬上有人回：「可是面試還是要靠深度跟學歷進門吧。」

這個回應說的沒有錯，但說的是舊世界的規則。

我想用一個比較清楚的框架，把這件事說明白。

* * *

## 終點只有一個：Master of a Few

先把目標說清楚，才不會在路上迷失。

Susan Zhang 說的 **master of a few** ，是指在 **2-3 個領域** 都達到真正的深度。她給了一個很直接的數學：

**在三個領域各達到 top 10%，組合起來就是 top 0.1%。**

0.1 × 0.1 × 0.1 = 0.001。

這不是激勵話語，是純粹的機率計算。你在三個領域的組合，市場上可能找不到第二個人完全一樣——這就是護城河。

但問題在於：要怎麼到達這個終點？

從哪裡出發，路徑不一樣，難度也不一樣。

* * *

## 舊時代的兩條路，難度差很多

在講 AI 改變了什麼之前，先把舊世界的邏輯說清楚。

### Master of One（專才路線）

舊時代的邏輯很清楚：學一個領域，學深，然後靠深度進門。

這條路的進門邏輯：你去面試，面試官問你一個領域的問題，你答得夠深，你就進了。Junior → Mid → Senior，靠年資和深度爬升。

難度：**低到中** 。只要你在一個領域夠深，有學歷、有認證、有年資，門是開著的。

### Jack of All Trades（通才路線）

舊時代通才的命運就比較慘。

「樣樣通、樣樣鬆」這句話，本來就是在貶低通才的。你什麼都會一點，但在面試的時候，面試官要找的是一個「做 X 的人」，你說「我什麼都會一點」——對不起，下一位。

難度：**高** 。廣但沒有深度的錨點，很難通過傳統的篩選機制。履歷上也說不清楚「你是什麼人」。

**舊時代的結論：專才路線，門比較好進。**

* * *

## 新時代的就業市場，難度反過來了

AI 出現之後，這兩條路的難度開始對調。

### Master of One 在新時代：門還開著，但入口在縮小

現在去面試，如果你是某個領域的深度專才，你還是能進門。這點是真的。

但有一個問題在慢慢發酵：**Junior 職缺正在消失。**

AI 接管了大量原本屬於 Junior 的工作——基礎的 coding、資料處理、文件整理、初階的分析。公司不需要再雇一個 junior 來「練功」，直接用 AI 做就好了。

這傷的不只是 junior 本身，傷的是整條養成鏈。

以前的路線是：jr → mid → senior，靠真實場景裡踩坑、累積深度。但入口縮小了，新人進不了門，就沒有辦法在真實環境裡累積深度。學校教的是理論，深度是在「做了一百個 PR、踩了一百個 bug」之後才有的。

入口在縮，養成路徑在斷。**Master of one 現在還可以，但越來越難進門。**

### Jack of All Trades 在新時代：AI 幫你補短板，新職缺在長

通才路線在新時代發生了一件事：**達到「夠廣」的成本大幅下降了。**

以前，把一個領域從 20 分補到 60 分，可能要花一兩年——讀書、上課、在真實場景裡摸索。

現在？AI 可以讓你在幾週內把一個陌生領域的基礎掌握到能對話、能判斷、能提問的程度。不是說你變成專家，而是你到達「不再是阻礙」的門檻。

AI 讓廣度變便宜了。

同時，有一種職位正在從例外變成主流：**FDE（Forward Deployed Engineer，駐場工程師）** 。

FDE 不是在辦公室接需求的人，是進到客戶現場、快速理解他們的問題、然後直接交付解決方案的人。它需要的恰好是通才的能力組合：

  * 快速學習客戶的 domain（今天是物流，明天是醫療）
  * 直接跟客戶建立信任關係
  * 能跨越技術和業務的語言
  * 能獨立交付，不需要等後勤支援



這個角色以前很少，現在很多公司都在找。而且它天然排斥純粹的深度專才——因為你不知道下一個客戶的產業是什麼，你需要廣。

**Jack of all trades 現在第一份工作確實比較難找，但它對標的職缺正在成長。**

* * *

## 我的立場：用 AI 把短板補到 60 分，然後押注人的能力

我自己做 AI coding 顧問、FDE 工作、技術 blog，這幾年試出來一個對我有效的策略：

**用 AI 把所有短板補到 60 分，讓它們從「阻礙」變成「夠用」。然後把真正的時間投在人的能力上。**

### 為什麼是 60 分？

90 分提升到 95 分，邊際效益遞減，而且大概率還是得靠你自己的腦袋。但 20 分補到 60 分？AI 可以幫你做到，而且這個門檻已經足夠讓你在那個領域「不再是障礙」——你能對話、能判斷、能知道什麼時候要找真正的專家。

60 分不是目標，60 分是地板。

### 為什麼特別鼓勵 FDE 路線？

FDE 是我看過最符合「jack of all trades, master of a few」精神的工作型態。

你進客戶現場，你需要快速理解他們的產業，用你的技術能力解決真實的問題，然後建立足夠的信任讓他們願意繼續合作。這個過程自然地強迫你同時練廣度（每個客戶產業不同）和深度（你必須真的解決問題，不能只說漂亮話）。

FDE 不適合所有人——它需要你願意在不熟悉的環境裡快速行動，而不是等到「準備好了」才出手。但如果你有這個特質，這條路在 AI 時代的發展空間很大。

### 為什麼特別強調人際關係？

這是我認為 AI 最難複製的東西。

當所有人都在用 AI 生產輸出，「你能不能讓客戶願意跟你說真正的問題」這件事的稀缺性反而在升高。技術輸出可以 AI 化，但信任關係不行。

客戶願意在凌晨兩點打電話給你，不是因為你最厲害，是因為他相信你。這個東西，是執行力、學習能力、人際關係加在一起累積出來的，不是知識。

* * *

## 坦白說：我一直以為我是 master of one

在整理這篇文章的時候，我回頭看了一下自己的職涯，發現一件有點好笑的事。

我以前一直以為我是 master of one。

在 Google 做雲端顧問的時候，我覺得我是「雲端架構專才」。跳去物流業當 VP of Data & AI，我覺得我是「數據領域的人」。做醫療 AI 研發長，我覺得我是「AI 落地的人」。

每一個階段，我都在說服自己我有一個「主要的深度」。

但有一天我把整條職涯攤開來看，我才發現：我從頭到尾的個性就是 jack of all trades。

我從來都不是因為「這個領域我最深」才進那個行業的。我是因為「這個新場景讓我覺得好奇」才跳進去的。進去之後，我用廣度和速度讓自己快速夠用，然後靠解決真實問題累積深度。

不是深度驅動，是好奇心驅動。

這讓我開始想：對 jack of all trades 的人來說，真正在累積的東西是什麼？不是某個領域的知識——那個在換跑道的時候會折損。真正跨越每一個領域、越用越值錢的東西，是：

**第一，學習力。** 每一次進入陌生領域，你練的不是那個領域本身，你練的是「快速讓自己夠用」的能力。這個能力在 AI 時代的價值，比任何單一知識都高。（我在[《AI 時代投資報酬率最高的事：填補短板》](https://ai-coding.wiselychen.com/ai-shortboard-filling-paul-dog-cancer-vaccine/)裡說的也是這件事——短板補到 60 分，學習力才是真正的資產。）

**第二，執行力。** Jack of all trades 很容易變成「什麼都懂一點但什麼都沒做完」。能跨越廣度還能持續交付的人，靠的不是知識，是把事做完的習慣。這個習慣在每個領域都一樣——[AI 時代的全端能力](https://ai-coding.wiselychen.com/ai-labor-management-full-stack-talent/)，說的本質也是「你能不能一個人從頭做到尾」。

**第三，勇於推翻自己的能力。** 這個最難說，但我覺得是最核心的。

Jack of all trades 最容易卡住的地方，不是學不會新東西，而是「用舊框架看新場景」。你在上一個領域建立的判斷模型，進入下一個領域的時候往往是負資產。能持續成長的人，是那種能說出「我之前的理解是錯的」然後真的換掉框架的人，不是那種死守舊判斷的人。

我自己就是一個案例——我花了很多年才承認我是 jack of all trades，而不是我以為的 master of one。

* * *

## 沒有最好的路，只有適合你的路

說了這麼多，我不是在說「通才路線一定比專才路線好」。

這件事取決於你的個性和天賦。

**如果你是那種喜歡把一件事做到極致、能在同一個領域持續深挖十年還覺得有趣的人** ——master of one 不是錯的選擇。但要誠實面對一件事：你需要確保自己的深度達到真正的頂尖，因為中等深度的專才，在 AI 時代的護城河越來越薄。

**如果你是那種喜歡好奇、不怕陌生、在新環境裡反而更有能量的人** ——jack of all trades 路線在 AI 時代比以前更有利了。AI 幫你把廣度的成本壓低，你只需要把真正的能量放在執行力、學習速度、和人的關係上。

而且 jack of all trades 還有一條路很多人沒想到：**創業** 。

創業者天然需要廣度——你今天要談客戶、明天要管帳、後天要做產品決策、下週要招人。純粹的深度專才在這個場景裡反而會卡住，因為他習慣把不擅長的事交給別人，但早期公司根本沒有「別人」。廣度、執行力、人際關係——這三件事剛好是早期創業者最需要的東西，也剛好是 jack of all trades 在 AI 助力下最自然能發展出來的東西。

* * *

這裡說的三條路——**IC（個人貢獻者）走 FDE、IC 走深度專才、創業者** ——終點不完全一樣：

  * **IC 走深度專才** ：目標是山峰型，3 個長板達到 90 分，短板用 AI 撐到 60 分
  * **IC 走 FDE / 跨域顧問** ：同樣是山峰型，但峰與峰之間的廣度更重要，進客戶現場靠的是連結不同領域的判斷力
  * **創業者** ：終點可以是超寬長方型——不一定需要極高的峰，但底板要夠寬，AI 幫你把每一個職能都撐到 60 分，一個人跑起整間公司



唯一不能做的，是在某一個狀態永遠停著不動：

  * 永遠是 master of one，拒絕往外擴——遲早被單點突破
  * 永遠是 jack of all trades，永遠不願意 commit——廣但沒有錨點，IC 說不清楚自己是誰，創業者也沒有讓人信任的核心能力



* * *

## 最終形態：山峰型，以及它的一個變種

**山峰型，就是 master of a few 的形狀。** （如封面圖右下角的示意）

三個領域各達到 90 分，這是你真正的長板，是別人無法輕易複製的護城河。峰與峰之間的低谷，也不能掉到 60 分以下——短板不需要拼頂尖，但不能是致命弱點。AI 的用途就是在這裡，把你所有的低谷都撐在 60 分以上。

但山峰型還有一個變形：**超寬長方型** 。

沒有特別高的峰，但寬度極廣——設計、行銷、財務、客服、研發、法務，每一個都到 60 分。以前這個覆蓋寬度需要一支 5-10 人的團隊，現在一個人加上 AI 可以撐起來。

這就是**一人公司** 的技術基礎。

Susan Zhang 在推文裡說了一句很多人跳過的話：「the disappearing managerial class」——管理階層在消失。不是因為公司不需要那些功能，而是因為一個夠寬的人加上 AI，可以自己把那些功能都做完，不再需要一層層的協調。

**一個人能獨立完成的邊界，正在快速往外推。** 而推動這件事的，就是每一個把自己從 I 型走到山峰型、甚至走向超寬長方型的人。

* * *

_Susan Zhang 的原推文值得去讀完，包含底下她回覆別人的部分。有人問她關於面試和 leetcode 的問題，她的回答也很實在：先做一個你可以分享給任何雇主的作品集，比刷題更根本。_

---

## [預測未來，不只需要歷史 — Google Nexus 論文把 Agent 塞進時間序列](https://ai-coding.wiselychen.com/nexus-google-time-series-forecasting-multi-agent/)
*🏢 Wisely Chen AI | 2026-05-18*

我一直覺得，時間序列預測是一個被低估的「AI Agent 戰場」。

不是因為它技術上有多複雜——ARIMA 用了幾十年，Prophet 也很成熟——而是因為它有一個根本上的思維盲點：

**它只問「過去發生了什麼」，從不問「為什麼發生」。**

Google 跟賓州州立大學最近發表的 Nexus 論文（[arxiv 2605.14389](https://arxiv.org/abs/2605.14389)），正面挑戰了這個假設。

結果很有趣。數字很驚人。但我的疑慮也不少。讓我老實跟你說。

* * *

## 問題的本質：曲線背後有故事，但模型看不懂故事

傳統時間序列模型——不管是 ARIMA、Prophet，還是這幾年很熱的 Time Series Foundation Models（TSFM，比如 TimesFM、Moirai）——它們的共同特徵是：

**它們讀數字，不讀故事。**

拿房地產來說。2020 年疫情初期，美國某些城市的房屋庫存曲線突然暴跌。從數字上看，這是一個異常點。但 TSFM 不知道背後發生了什麼：封城、供應鏈斷裂、房東觀望心態。

然後 2021 年，曲線反彈。TSFM 可能把這解讀成「季節性回升」，但實際上是利率超低、遠端工作浪潮、移民潮同時出現。

**有些模式是事件造成的，不是時間造成的。**

這是 Nexus 論文開宗明義的第一句話，也是我覺得最精準的一句話。

那 LLM 呢？LLM 知道這些事件。它看過新聞、看過 Fed 會議記錄、看過分析師報告。它可以告訴你「2021 年 Q2 房地產反彈的三大驅動因素」。

但 LLM 不會跑時間序列。它沒有數值計算的訓練，也沒有序列建模的架構。

**這就是問題的核心：** 懂故事的不懂數字，懂數字的不懂故事。

* * *

## Nexus 怎麼處理這個問題？

Nexus 的答案不是「讓 LLM 直接預測」，也不是「讓 TSFM 讀新聞」。

它的做法是：**把預測這件事，拆成四個專職 Agent，讓它們各司其職，最後合成。**

這個思路我之前在 AgentOpt 論文裡看過類似的影子——最強的模型放在最重要的位置，不一定得到最好的結果。分工的設計，比選哪個模型更重要。

Nexus 的四個 Agent：

**1. 事件整理員（Event Extractor）**

把混亂的歷史文本——新聞、公告、研究報告——整理成乾淨的事件時間軸。它的工作只有一件：把「文字時間」轉換成「事件時間線」。不預測，不解讀，只整理。

**2. 宏觀觀察員（Macro Regime Reader）**

讀的是大格局：這個市場現在處於什麼「體制」（regime）？擴張期？衰退期？政策轉向期？它不管細節，只判斷「現在是哪種時代」。

**3. 微觀追蹤員（Local Shock Tracker）**

追蹤局部衝擊：某個城市的特殊事件、某支股票的 earnings 驚喜、某個地區的供應鏈斷裂。它關注的是「這件事，為什麼跟大趨勢不一樣」。

**4. 合成員（Synthesizer）**

把前三個 Agent 的輸出，加上過去預測的誤差記錄，合成最終預測。它不只整合資訊，還會根據「過去我在哪些情況下預測錯了」來校正自己的信心。

* * *

## 數字：86.6% 是什麼等級的改善？

論文在 Zillow 房地產數據集上，比較了 Nexus 跟幾種基準做法的誤差（MAPE）：

  * **vs direct chain-of-thought prompting（Claude）：降低 86.6%**
  * vs state-of-the-art TSFM：持平或更好



86.6% 的 MAPE 降低，換個方式理解：如果原本預測誤差是 10%，Nexus 把它壓到大概 1.4%。這是一個很誇張的改善幅度。

不過這裡有個關鍵：比較基準是「direct CoT prompting」。

也就是說，他們比的是「用一個 Prompt 叫 Claude 直接預測」vs「用四個 Agent 分工再合成」。

這個比較本身是公平的——它在回答「結構化多 Agent 比單一 CoT 好多少」這個問題。但它沒有告訴你「跟最好的傳統 TSFM 相比，到底贏在哪」。

那個數字，論文說是「持平或更好」，但沒有給出一個漂亮的單一數字。

* * *

## 坦白說：我有哪些疑慮

我覺得 Nexus 的架構思路是對的，但論文本身承認了幾個限制，我覺得值得放在這裡說清楚：

**限制一：測試集很窄。**

Zillow 房地產指標 + 7 支股票。這是 2 個領域、大概幾十個時間序列。對於一篇想要「顛覆預測範式」的論文，這個樣本量算小。

**限制二：單次評估（single-run evaluations）。**

沒有跑多次取平均。LLM 的輸出本來就有隨機性，單次評估的方差會很大。

**限制三：Post-cutoff 數據。**

數據是在 LLM 的訓練截止點之後產生的——這是為了避免模型「記住答案」。這個設計很誠實，但也代表測試條件是特意選的最嚴格場景，不一定代表真實部署的平均表現。

**限制四：沒有成本分析。**

四個 Agent 跑完，token 消耗是多少？延遲是多少？這些數字都沒有。如果比直接 CoT 貴 10 倍，那 86.6% 的改善還合算嗎？視應用場景而定。

這些不是要否定論文，而是在說：**這是一個很有潛力的方向，但還不是一個你可以直接拿去生產的配方。**

* * *

## 對 AI 工程師最有用的啟示

把 Nexus 的論文結果放在一邊，它在架構設計上的思路，其實很值得偷學：

**1. 把「做什麼」和「怎麼解讀」拆開。**

Nexus 的 Event Extractor 只整理事實，不解讀。Macro Reader 只判斷體制，不預測。分工越清晰，每個 Agent 的 Prompt 越精準，失焦的可能性越低。

這跟我之前說的 AgentOpt 結論是一致的：角色定義比模型選擇更重要。

**2. 校正是一種 memory。**

Synthesizer 會讀「過去我在哪裡預測錯了」然後調整信心。這不是什麼特別新的概念，但在時間序列這個場景裡，它讓 Agent 有了一種「從失敗中學習」的機制——不需要 fine-tuning，只需要把誤差記錄餵進 context。

**3. 一個 Prompt 做完所有事，通常不是最好的設計。**

這是 Nexus 最核心的主張，也是整個論文能做到 86.6% 改善的原因。

一個 Prompt 要同時：整理歷史文本 + 判斷宏觀體制 + 追蹤局部衝擊 + 合成預測 + 根據過去誤差校正——這對 LLM 來說太多了。每增加一個任務，其他任務的注意力就被稀釋。

**結構幫助 LLM 使用 context，而不是讓它在 context 裡迷失。**

這句話，是論文裡我覺得最有份量的一句。

* * *

## 更大的方向：未來的預測師，不只外推曲線，還要辯論「是什麼讓曲線移動」

論文最後的結論，我覺得說得很好：

> 未來的預測，不只是外推曲線，而是討論「是什麼讓曲線移動」。

這個方向，我相信是對的。

不管是房地產、股票、還是電商銷量——純粹的數值模型，在事件驅動的波動面前，永遠有它的天花板。把「事件理解」接進來，是必然的趨勢。

Nexus 提供了一個值得參考的架構藍圖。不是最終答案，但可能是一個好的起點。

* * *

## 結語

我沒有在生產環境跑過 Nexus。這篇文章是基於論文分析，不是實戰數據。

但我認為它的架構思路是對的，值得在你的下一個預測專案裡借鑒「分工 + 角色專職化 + 誤差校正記憶」這三個設計原則。

至於 86.6% 這個數字——記得加上一句「在特定測試條件下」。

* * *

**論文資訊：**

  * **標題：** Nexus: An Agentic Framework for Time Series Forecasting
  * **作者：** Sarkar Snigdha Sarathi Das, Palash Goyal, Mihir Parmar 等（Google + Penn State）
  * **arXiv：** [2605.14389](https://arxiv.org/abs/2605.14389)
  * **發表：** 2026年5月14日



**延伸閱讀：**

  * [AgentOpt：貴模型放錯位置，反而比便宜模型差](https://ai-coding.wiselychen.com/agentopt-expensive-model-wrong-position-pipeline-optimization/)
  * [Agent 模式 Part 3：Deep Research 架構探討](https://ai-coding.wiselychen.com/agent-mo-shi-part-3-deep-research-architecture/)
  * [多 Agent 的結構性不穩定性](https://ai-coding.wiselychen.com/agents-of-chaos-multi-agent-structural-instability/)

---

## [Harness Engineering 實戰第一篇：把指令拆分到不同檔案裡](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/)
*🏢 Wisely Chen AI | 2026-05-17*

> 我自己的 `CLAUDE.md` 寫到 1543 行，涵蓋 8 個專案。我以為這是「我的 AI 第二大腦」，直到我看到 Anthropic 工程師團隊自己用的 CLAUDE.md 不到 50 行。這篇文章是 Harness Engineering 實戰系列第一篇，對應 Walking Labs 課程的 L04（指令檔案的模組化拆分）。我會用 5 個真實爆款案例 ——「200 行規則被全部忽略」、Anthropic 自己的 Postmortem、MEMORY.md 靜默截斷 Bug、Mr. Tinkleberry 失憶事件、Cursor 官方宣告 `.cursorrules` 死亡 —— 證明一件反直覺的事：指令寫越多，AI 越不聽話。然後告訴你 AGENTS.md 三層拆分模式怎麼救你。

**作者：** Wisely Chen **日期：** 2026 年 5 月 **系列：** Harness Engineering 實戰系列（EP1） **關鍵字：** Harness Engineering, CLAUDE.md, AGENTS.md, .cursorrules, Walking Labs, 指令檔案, 模組化拆分, Anthropic, Cursor, Context Engineering, Claude Code, instruction bloat, ruthlessly prune

* * *

* * *

## 目錄

  * [我的 CLAUDE.md 1543 行的尷尬](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#我的-claudemd-1543-行的尷尬)
  * [核心論點：指令越多，AI 越聽話？錯。](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#核心論點指令越多ai-越聽話錯)
  * [5 個真實案例：CLAUDE.md 失控的證據](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#5-個真實案例claudemd-失控的證據)
  * [數字彈藥庫](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#數字彈藥庫)
  * [Anthropic 內部人的做法：Ruthlessly Prune](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#anthropic-內部人的做法ruthlessly-prune)
  * [新共識：AGENTS.md 三層拆分模式](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#新共識agentsmd-三層拆分模式)
  * [我的實戰：1543 行該怎麼拆](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#我的實戰1543-行該怎麼拆)
  * [結語：少即是多，分即是合](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#結語少即是多分即是合)



* * *

## 我的 CLAUDE.md 1543 行的尷尬

前個月前，我打開自己的 `~/CLAUDE.md`，跑了一個 `wc -l`：
    
    
    1
    

| 
    
    
    1543 /Users/wisely.chen/CLAUDE.md
      
  
---|---  
`

裡面塞了 X 個專案：

我以為這是「我的 AI 第二大腦」。直到我注意到一件事：**Claude Code 越來越常忽略我寫過的規則。**

明明寫了「永遠用繁體中文回覆」，它有時還是會切回簡體。 明明寫了「不要主動 commit、不要 push」，它偶爾還是會擅作主張。 明明寫了「先 Read 再 Edit」，它有時候直接生一段亂猜的 code 上來。

我一度懷疑是 Claude 變笨了。後來查了 Anthropic 自己的官方文件，看到一句話讓我崩潰：

> _「If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise.」_

翻譯成白話：**我的 CLAUDE.md 越長，Claude 越不聽話。**

這篇文章要講的，就是 Walking Labs Harness Engineering 課程的 **L04（指令檔案的模組化拆分）** —— 為什麼這件事比你想像得更重要、更反直覺，而且整個 AI Coding 生態系已經悄悄收斂到一個新做法。

* * *

## 核心論點：指令越多，AI 越聽話？錯。

先丟出最反直覺的事實：

**Frontier LLM 可靠遵守的指令上限大約是 150–200 條。**

而 Claude Code 自己的系統 prompt 就已經吃掉約 50 條。

也就是說：**你能用的指令預算只剩 100–150 條。**

更糟的是，當你超過這個上限，**不是「最不重要的規則先被忽略」，而是「全部規則的遵守率一起下降」** 。

一條低價值規則的存在，**會稀釋所有高價值規則的遵守機率** 。

這件事直接打臉所有人對「AI 指令檔」的直覺：

  * 直覺：寫越多越保險 → 真相：寫越多越糟糕
  * 直覺：規則越完整越好 → 真相：規則越精準越好
  * 直覺：把所有 edge case 都塞進去 → 真相：塞到 Claude 連紅線都不照做



這就是 Harness Engineering 想要解決的問題之一：**你以為你在強化 AI，其實你在弱化它。**

* * *

## 5 個真實案例：CLAUDE.md 失控的證據

### 案例 1：「我寫了 200 行規則。它一條都沒照做。」

2026 年 3 月，DEV Community 上一篇文章爆紅：

> _“I Wrote 200 Lines of Rules for Claude Code. It Ignored Them All.”_

作者是個每天用 Claude Code 12 小時的重度用戶。他精心打造了 200 行的 CLAUDE.md 規則檔，結果發現 **Claude 幾乎一條都不認真執行** 。

文章結論很狠：

> 「CLAUDE.md 是一份願望清單，不是合約。」

更妙的是，同個作者後來又寫了續集：**“I Wrote 500 Lines of Rules. Here’s How I Made It Actually Follow Them.”**

解法不是寫得更詳細，是**把它拆開** 。

兩篇加總幾十萬次點閱，社群共鳴可想而知 —— 因為**幾乎每個 Claude Code 重度用戶都遇過一樣的問題** 。

### 案例 2：Anthropic 自己也踩過坑（4/23 Postmortem）

2026 年 4 月 23 日，Anthropic 發了一份正式 postmortem。

過去 6 週社群一直抱怨「Claude Code 變笨了」。Anthropic 內部追查後發現，問題不是模型，是**三個 harness 層級的指令改動疊加** 造成的。

其中最荒謬的一條改動是：

> 「將 tool call 之間的回應文字限制在 25 字以內。」

就這一條看似無害的指令，加上其他兩個小改動，**讓全世界覺得 Claude 變笨了 6 週** 。

這就是「指令污染」的官方版證據。**連 Anthropic 自己加錯一句話都會引發大型質量危機** ，你的 1500 行 CLAUDE.md 還能僥倖嗎？

延伸閱讀：[Opus 4.7「變笨」一個月之謎 —— Anthropic 終於承認是 Claude Code 的 harness](https://ai-coding.wiselychen.com/opus-4-7-claude-code-harness-postmortem/)

### 案例 3：MEMORY.md 超過 200 行直接靜默丟失

更詭異的事情：Claude Code 的 `MEMORY.md` 有一個 **未公開的硬性限制** 。

GitHub 上有兩個 Issue 在追這件事（`anthropics/claude-code#25006`、`#39811`）：

  * MEMORY.md 超過 200 行的內容，**會被靜默丟棄、永遠不載入**
  * **沒有警告、沒有錯誤訊息、沒有提示**
  * 用戶以為自己記下了東西，其實系統根本看不到



這個 bug 比「寫太多被忽略」更可怕：**你的記憶不是被弱化，是直接消失。**

如果你也用 Claude Code 的 memory 系統，**現在就去看一下你的 MEMORY.md 有幾行** 。

### 案例 4：Mr. Tinkleberry 失憶事件

HN 和 Threads 上有個經典案例。一個用戶在 CLAUDE.md 寫了一條規則：

> 「永遠叫我 Mr. Tinkleberry。」

一開始 Claude 照做了。隨著 CLAUDE.md 越加越多其他規則，某天 Claude 突然停止叫他 Mr. Tinkleberry，恢復成 Sir / User / 你 之類的稱呼。

**最簡單的指令、最明確的偏好、最容易執行的規則 —— 都會被稀釋。**

這是「指令稀釋」最日常、最具象的證據。它告訴我們：**規則的遵守機率不是「分項計算」，是「整體攤分」** 。

### 案例 5：Cursor 官方宣告 `.cursorrules` 死亡

Cursor 從 0.43 版開始，**官方文件直接把`.cursorrules` 標註為 deprecated**。

取而代之的是：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    .cursor/rules/
    ├── frontend.mdc       # 帶 frontmatter，scope 到前端檔案
    ├── backend.mdc        # scope 到後端
    ├── tests.mdc          # scope 到測試
    └── always-apply.mdc   # 全域規則（限制 < 50 行）
      
  
---|---  
`

每個 `.mdc` 檔案有自己的 YAML frontmatter，可以指定 glob pattern、哪些路徑下才載入這條規則。

社群實測：採用新的拆分系統後，「AI 忽略我的規則」這類抱怨**下降了 60–75%** 。

更值得注意的是：**整個工具生態系都在向模組化拆分演進。**

  * Cursor → `.cursor/rules/` 目錄
  * Claude Code → 開始支援 `.claude/rules/` 目錄
  * OpenAI Codex → 採用 `AGENTS.md` 規範
  * Walking Labs → 主張 `AGENTS.md` + `feature_list.json`



**沒有任何一家工具廠商認為「單一檔案塞所有指令」是對的方向。**

* * *

## 數字彈藥庫

把這些散落的證據整理成一張表，方便你決策：

指標 | 數值  
---|---  
Frontier LLM 指令遵守上限 | 150–200 條  
Claude Code 系統 prompt 已佔用 | ~50 條  
你的可用指令預算 | 100–150 條  
Anthropic 官方建議 CLAUDE.md 大小 | < 200 行  
社群更激進的建議 | < 60 行  
MEMORY.md 硬性截斷 | 200 行 / 25KB  
Cursor `.cursorrules` 上限 | 500 行（Always Apply < 50 行）  
拆分後規則被忽略改善 | 下降 60–75%  
Anthropic Postmortem 影響時長 | 6 週  
  
把這張表存下來。下次同事問你「為什麼 AI 不照我寫的做」，直接丟給他。

* * *

## Anthropic 內部人的做法：Ruthlessly Prune

Anthropic 官方文件裡有一句話被反覆引用：

> _「For each rule, ask: ‘Would Claude make a mistake without this?’ If not, delete it.」_

**翻譯：每條規則都問一遍 —— 「如果刪掉這條，Claude 會犯錯嗎？」如果不會，就刪掉。**

Threads 上有篇貼文截了 Anthropic 工程師團隊內部使用的 CLAUDE.md 模板 —— **不到 50 行** 。

對比一下：

  * Anthropic 工程師：47 行
  * 社群常見：300–500 行
  * **我自己：1543 行**



我自認自己是個系統思考者、會寫框架、會做架構分析的人 —— 結果在這件事情上，我做得比 Anthropic 工程師糟糕 **30 倍** 。

這就是這篇文章存在的意義。**不是教你 Harness Engineering 是什麼，是逼你正視自己已經在累積的技術債。**

* * *

## 新共識：AGENTS.md 三層拆分模式

社群正在收斂到一個新的標準，跟 Walking Labs Harness Engineering 課程的 L04 主張幾乎完全一致：
    
    
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
    
    
    專案根目錄/
    ├── AGENTS.md           # 通用指令（所有 AI 工具都讀）
    ├── AGENTS.override.md  # 本地覆寫（gitignored，不進 repo）
    ├── CLAUDE.md           # symlink → AGENTS.md（保持同步）
    ├── .cursor/rules/      # Cursor 專用 .mdc 檔案
    │   ├── frontend.mdc    #   含 glob scope
    │   ├── backend.mdc
    │   └── tests.mdc
    └── .claude/rules/      # Claude Code 專用（按 path scope）
      
  
---|---  
`

三層結構解決三件事：

**第一層（AGENTS.md）：寫專案 high-level 約定**

  * 命名規則
  * 提交慣例
  * 不可違反的紅線
  * 任何工具都該知道的事



**第二層（工具專屬目錄）：寫工具細節 + 檔案 scope**

  * 哪些檔案套用哪些規則
  * 用 frontmatter 控制 scope
  * 每個檔案不超過 100 行
  * 只在相關的時候才載入



**第三層（local override）：寫個人偏好**

  * 不進 repo
  * gitignored
  * 給單一開發者使用
  * 不污染團隊 context



關鍵在於：**每一層都有明確的 scope，AI 只在相關的時候才讀。**

這就是 Walking Labs 的精髓 —— 不是「寫得越完整越好」，是「在對的時候、給對的 AI、看對的規則」。

很多人會問：「那為什麼不全部寫進 AGENTS.md 就好？」

答案就是這整篇文章在講的事情：**因為你寫越多，AI 越不照做。** 你需要的不是「更大的指令檔」，是「更聰明的指令分配」。

* * *

## 我的實戰：1543 行該怎麼拆

回到我自己的 CLAUDE.md。我做了一次徹底的拆分。

**拆前（1543 行單檔）：**
    
    
    1
    

| 
    
    
    ~/CLAUDE.md  # 全部塞一起，跨 8 個專案
      
  
---|---  
`

**拆後：**
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    

| 
    
    
    ~/CLAUDE.md  # 只保留個人偏好 + 跨專案紅線（~50 行）
      ├── 永遠用繁體中文
      ├── 不要主動 commit / push
      ├── 用 Read 再 Edit
      └── 工程術語用英文
    
    各專案/CLAUDE.md  # 專案專屬規則（< 200 行）
      ├── /Desktop/cc/blog-content/CLAUDE.md   # Jekyll 部署流程
      ├── /Desktop/cc/SEO/CLAUDE.md            # BigQuery + GA4 設定
      ├── /Desktop/cc/XXX/CLAUDE.md      # XXX 系統
      ├── /Desktop/cc/XXX/CLAUDE.md   # XXX 專案
      └── /Downloads/XXX/CLAUDE.md         # XXX 
      
  
---|---  
`

主 CLAUDE.md：從 1543 行 → 47 行。 每個專案的 context 在我進入該目錄時自動載入。 個人偏好永遠生效、專案規則只在相關時生效。

**初步效果（一週實測）：**

  * Claude 開始正確記得我的繁中偏好（過去常常 fallback 成簡體）
  * 跨專案不再混淆（過去寫 SEO 分析時偶爾出現 Jingteng 的指令）
  * Session 啟動速度可感地變快（更少 token 在載入無關內容）
  * 紅線規則的遵守率明顯提升（「不要主動 commit」過去偶爾失守，現在沒再發生）



不是完美。但**明顯比 1543 行的時代好太多** 。

**坦白說沒解決的問題：**

  * 跨專案搜尋變麻煩（過去 Ctrl+F 一次找到所有專案資訊，現在要先進目錄）
  * 部分歷史資訊（已完成的專案紀錄）我還沒決定要不要進 archive
  * 不同專案之間的「方法論共用」（例如 ATPM 框架）還沒抽出來



這是一個進行中的工程，不是一個完成的答案。但**方向是對的，這點我很確定** 。

* * *

## 結語：少即是多，分即是合

Harness Engineering 不是要你「寫更多規則」。是要你**用對的結構安排規則** 。

洞察很簡單：

> **「指令的價值不在於『寫了什麼』，而在於『AI 真的能讀到、能執行的那部分』。」**

回頭看 5 個真實案例：

  1. 200 行被全部忽略
  2. Anthropic 自己加錯一句話炸鍋 6 週
  3. MEMORY.md 超過 200 行直接消失
  4. Mr. Tinkleberry 被遺忘
  5. Cursor 官方宣告 `.cursorrules` 死亡



這些都不是孤立事件。它們指向同一個結構性問題：**單檔指令系統不夠用了。**

如果你也有一個越寫越長的 CLAUDE.md，**今天就跑一次`wc -l`**。

如果超過 200 行 —— 你不是在打造記憶系統，你是在打造一個被忽略的願望清單。

而願望，從來不會自己實現。

* * *

## 下一篇預告

**Harness Engineering 實戰第二篇：** L03 — 為什麼 Repo 才是 AI 的單一事實來源（Replit AI 把生產資料庫刪光的那一晚發生了什麼）

* * *

## 延伸閱讀

  * [Harness Engineering 架構全景：AI 可以寫 Code，但不能自己上 Production](https://ai-coding.wiselychen.com/harness-engineering-architecture-overview-ai-code-production-guardrails/)
  * [Harness Engineering 完整拆解：當 AI Agent 寫完 Code，你的 Repo 準備好自動接住了嗎？](https://ai-coding.wiselychen.com/harness-engineering-control-plane-pattern-agent-review-loop/)
  * [Opus 4.7「變笨」一個月之謎 —— Anthropic 終於承認是 Claude Code 的 harness](https://ai-coding.wiselychen.com/opus-4-7-claude-code-harness-postmortem/)
  * [當 AI 把資料庫刪光：兩個真實案例與 Harness Engineering 的反擊](https://ai-coding.wiselychen.com/ai-delete-database-harness-engineering/)
  * [Walking Labs - Learn Harness Engineering 課程](https://walkinglabs.github.io/learn-harness-engineering/zh-TW/)



* * *

## 參考資料

  * Anthropic Engineering, _April 23 Postmortem_ : <https://www.anthropic.com/engineering/april-23-postmortem>
  * Anthropic, _Best Practices for Claude Code_ : <https://code.claude.com/docs/en/best-practices>
  * DEV Community, _I Wrote 200 Lines of Rules for Claude Code. It Ignored Them All._ : <https://dev.to/minatoplanb/i-wrote-200-lines-of-rules-for-claude-code-it-ignored-them-all-4639>
  * DEV Community, _I Wrote 500 Lines of Rules. Here’s How I Made It Actually Follow Them._ : <https://dev.to/mikeadolan/i-wrote-500-lines-of-rules-for-claude-code-heres-how-i-made-it-actually-follow-them-3c8>
  * GitHub Issue, _MEMORY.md silently drops entries past 200-line limit_ : <https://github.com/anthropics/claude-code/issues/39811>
  * GitHub Issue, _MEMORY.md has undocumented 200-line hard limit_ : <https://github.com/anthropics/claude-code/issues/25006>
  * Cursor Docs, _Rules_ : <https://docs.cursor.com/context/rules>
  * Augment Code, _How to Build Your AGENTS.md (2026)_ : <https://www.augmentcode.com/guides/how-to-build-agents-md>
  * alexop.dev, _Stop Bloating Your CLAUDE.md_ : <https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/>
  * Walking Labs, _Learn Harness Engineering 課程_ : <https://walkinglabs.github.io/learn-harness-engineering/zh-TW/>

---
