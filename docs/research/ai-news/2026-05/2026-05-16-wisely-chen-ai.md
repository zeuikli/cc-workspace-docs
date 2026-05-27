---
title: "Wisely Chen AI — 2026-05-16"
date: 2026-05-16
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-05-16

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [RTX 5090 + Qwen3.6-27B 七種推論引擎實測：Sonnet 4.6 等級的本地推論，NT$30 萬桌機跑得起來嗎？](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)
*🏢 Wisely Chen AI | 2026-05-14*

## TL;DR

  * **核心問題** ：Qwen 3.6-27B ≈ Sonnet 4.6 等級，**這個能力能塞進 NT$30 萬以下的桌機嗎？** 答案：**能，整套 NT$30 萬剛剛好卡進企業 IT 採購的桌機/工作站預算天花板**
  * **2026 是本地小模型性價比騰飛的元年** — RTX 5090（32GB VRAM）配 Qwen3.6-27B，單流 140 tok/s、並發 575 tok/s 都做得到
  * **七種配置實測** ：vLLM × 3、llama.cpp × 2、Ollama × 2，外加一個直接 OOM 的失敗案例
  * **三個冠軍** ： 
    * 單流最快：**llama.cpp + MTP（Q2_K_XL）→ 140 tok/s**
    * 並發最強：**vLLM AWQ-INT4 → 575 tok/s @ 並發 8**
    * 開箱即用體驗最好但效能最差：**Ollama Q4_K_M → 64 tok/s（並發完全不擴展）**
  * **最反直覺發現** ：同一個 Q4_K_M GGUF，llama.cpp 比 Ollama **並發吞吐快 3.2x** — Ollama 把 batching 給關了
  * **量化命名不可信** ：標榜 “GPTQ-Int4” 的模型實測載入 27.5 GiB（應 ~13.5 GiB），attention/visual layer 還是 BF16



* * *

## 為什麼這又是一篇「無聊 IT 架構」文

又一篇 IT 架構系列文，不是炫耀 benchmark。

過去半年我一直在追這條線：**「本地 LLM 到底什麼時候 ROI 翻過來」** 。前幾個月寫過 [DGX Spark 跑 Qwen3.6-27B](https://ai-coding.wiselychen.com/qwen-3-6-27b-gb10-home-inference-sonnet-level/) 的觀察 — 那篇結論是「家用 AI 工作站時代到了」。但 DGX Spark 是 $4,699 的特規機，買的人還不多。

這次我自己組了一台桌機（消費級零組件），想回答一個非常具體的性價比問題：

> **「Qwen 3.6-27B 既然被認為接近 Sonnet 4.6 等級，那這個能力能不能塞進一台 NT$30 萬以下的桌機？選錯引擎會差多少？」**

NT$30 萬是企業 IT 採購一台「中高階桌機/工作站」的常見上限 — 過了這條線就要走資產採購、董事會審核。如果跑 Sonnet 4.6 等級的本地 AI 必須花 NT$50 萬以上，那這條路就還是只有 R&D 部門能玩，business unit 進不來。

實測答案：**整套 NT$30 萬剛好卡進企業預算天花板。** 而且這台桌機單流跑得贏多數 API 的速度（140 tok/s）、並發吞吐到 575 tok/s（GPT-4o-mini 級別）。對比之下，2025 年要跑同樣等級的模型只能買 H100，光一張卡就 NT$100 萬起跳 — **整整貴三倍以上** 。

**但前提是你選對引擎、選對量化、跳過三個坑。** 選錯的話，同一張卡跑出 2x tok/s — 你會以為本地 LLM 還是不能用。

* * *

## 四個維度看 LLM 推論的選擇地圖

判斷一個 LLM 推論方案值不值得用，看四個維度就夠了：**模型能力、單人 tok/s、多人併發 tok/s、token/NT$** 。把市面上主流方案攤開來比：

方案 | 模型能力 | 單人 tok/s | 多人併發 tok/s | NT$/1M tokens  
---|---|---|---|---  
Claude Sonnet 4.6 API | ★★★★★ 旗艦 | ~80 | 無上限 | ~270  
GPT-4o-mini API | ★★★ 入門 | ~120 | 無上限 | ~11  
**RTX 5090 + Qwen3.6-27B（最佳引擎）** | **★★★★ ≈ Sonnet 4.6** | **140** | **575** | **~10**  
Mac Studio M3 Ultra + Qwen3.6-27B | ★★★★ | ~45 | 受限 | ~60  
DGX Spark + Qwen3.6-27B | ★★★★ | 136 | ~200 | ~15  
H100 server + Qwen3.6-27B | ★★★★ | ~150 | 1000+ | ~12（但 27B 用不滿，殺雞用牛刀）  
  
四個維度怎麼讀：

  1. **模型能力** — 決定 workload 可不可行。Qwen3.6-27B ≈ Sonnet 4.6 是 2026 才有的事，過去本地模型都還停在 GPT-3.5 等級
  2. **單人 tok/s** — 影響 IDE 補全、即時對話延遲。5090 + MTP 140 tok/s 連雲端 API 都比不上，因為 API 還要算 network RTT
  3. **多人併發 tok/s** — 影響團隊共用、批次處理。5090 + vLLM 575 tok/s 已經到 GPT-4o-mini API 級別吞吐 — 一台桌機服務一個小團隊
  4. **NT$/1M tokens** — 影響大規模用量的 ROI。5090 攤提下來 ~NT$10，**比 Sonnet 4.6 API 便宜 27 倍** ，跟 GPT-4o-mini 同價位但能力高一級



> NT$/1M tokens 計算基準：API 用官方定價、輸入輸出 1:1 估算；本地用 NT$30 萬桌機攤提 5 年 + 電費 + 30% 利用率

**5090 + Qwen3.6-27B 是「四個維度都進前段班」的方案。** 不是極致最快、不是極致最便宜，但四個維度沒有任何一項是短板。這就是「性價比騰飛」的本質：**不是某一個維度暴衝，是全部維度同時翻過了能用的門檻** 。

過去本地 LLM 在「模型能力」這個維度就被卡死了，剩下三個再好都沒意義 — 模型笨用戶不會用。現在能力到位，剩下三個維度才開始有討論價值。

* * *

## 第一段｜為什麼說 2026 是「小模型性價比騰飛」的元年

把過去 18 個月的關鍵節點排一下：

時間 | 事件 | 對「本地 LLM」的意義  
---|---|---  
2024 Q4 | 70B 模型才能 production，要 2x A100 | 一台機器破百萬，ROI 算不回來，企業不碰  
2025 Q2 | Qwen 3.5-27B 出來，tool calling 可用 | 第一次 27B 達 production 門檻  
2025 Q4 | 量化技術成熟：AWQ INT4、FP8 KV cache、MTP | 27B 模型壓進 16GB VRAM  
2026 Q1 | Blackwell（5090）零售上市 | 32GB GDDR7、SM 120，整機 NT$30 萬  
**2026 Q2（現在）** | **Qwen 3.6-27B + 5090 + 進化過的引擎** | **Sonnet 4.6 等級能力裝進 NT$30 萬以下桌機**  
  
三件事在同一個時間點交叉：

  1. **模型側** ：27B dense 模型品質追上 Sonnet 4.6（在 SWE-bench、Terminal-Bench 等場景）
  2. **硬體側** ：消費級 5090 把 32GB VRAM 帶到桌面，整機 NT$30 萬剛好卡進企業桌機預算天花板 — 過去同等級能力要 H100，光一張卡 NT$100 萬，整整貴三倍
  3. **軟體側** ：推論引擎這半年集體大改 — vLLM 0.20 的 cudagraph、llama.cpp 收 MTP PR、AWQ 真正純 4-bit 量化普及



**這三件事任何一件沒到位，本地 27B 都還是 demo 級。三件同時到位才算「性價比騰飛」。**

性價比的本質是「能力 ÷ 預算」。**過去能力線上不去，現在能力上來了、預算也下來了，但天花板換成了「會不會調」** — 一張同樣的卡，配對的引擎跟參數能讓 token speed 差 9 倍。所以接下來這段最想講的，不是「性價比有多好」 — 而是**選錯配置會差到讓你以為這條路走不通** 。

* * *

## 第二段｜七種配置實測，包含一個直接失敗的

機器規格先放著：

  * GPU: NVIDIA RTX 5090（Blackwell, SM 120, 32GB GDDR7）
  * Driver: 595.58.03（最高支援 CUDA 13.2，但編譯**必須用 12.9** — Unsloth 警告 13.2 會輸出亂碼）
  * Host: Ubuntu 24.04 原生（不是 WSL）
  * RAM: 64GB



測試 prompt 用同一段 63 token 的提示寫關於計算機歷史的 essay，`temperature=0` 跑單流，`temperature=0.7` 跑並發。

### Config 1：vLLM + GPTQ-Int4（直接 OOM 失敗）

我一開始抓的是 `raydelossantos/Qwen3.6-27B-GPTQ-Int4`，名字寫 “Int4”，磁碟大小 29 GB。

啟動就死：
    
    
    1
    

| 
    
    
    ValueError: No available memory for the cache blocks
      
  
---|---  
`

模型載入吃了 **27.51 GiB** （純 Int4 27B 應該只要 ~13.5 GiB），KV cache 只剩 0.18 GiB 直接掛掉。

去翻 `config.json` 才發現名實不符：
    
    
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
    

| 
    
    
    "quantization_config": {
      "bits": 4,
      "dynamic": {
        "-:.*attn.*": {},          // attention 不量化
        "-:.*mtp.*": {},           // MTP 層不量化
        "-:.*shared_expert.*": {}, // shared expert 不量化
        "-:.*visual.*": {},        // visual encoder 不量化
        "lm_head": {}
      }
    }
      
  
---|---  
`

**只有 MoE expert 部分是 Int4，attention、visual、MTP head 全部是 BF16。** 名字叫 “Int4” 但本質是「部分量化」。32GB VRAM 在 5090 上根本不夠塞。

**Reality check：模型卡上寫「Int4」「INT4」「W4A16」千萬不要照單全收。** 看 `config.json` 裡的 `dynamic` 例外清單，或對比磁碟容量 — 純 4-bit 27B 模型應該 ~14 GB，不該 29 GB。

### Config 2：vLLM + NVFP4-BF16 + enforce-eager（救命但慢）

換 `rdtand/...NVFP4-BF16-vllm`（19 GB），這次能跑了，但要加 `--enforce-eager` 才能塞進 32GB：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    ~/vllm-qwen-env/bin/vllm serve rdtand/Qwen3.6-27B-PrismaSCOUT-Blackwell-NVFP4-BF16-vllm \
      --gpu-memory-utilization 0.92 \
      --max-model-len 8192 \
      --enforce-eager \
      --served-model-name qwen-nvfp4
      
  
---|---  
`

`\--enforce-eager` 是救命 flag — 它跳過 cudagraph capture 階段（會吃 12GB+ VRAM）。**但代價是砍掉 30-50% decode 速度。**

實測：

  * 單流：**20.5 tok/s** （比 Ollama 還慢！）
  * 並發 16：304 tok/s



學到的事：**32GB VRAM 跑 27B 模型，模型本體必須壓到 ~16 GiB 以下** ，才有空間給 cudagraph 跑全速。19 GB 已經太大。

### Config 3：vLLM + AWQ-INT4 + cudagraph（並發冠軍）⭐

換 `cyankiwi/Qwen3.6-27B-AWQ-INT4`（20 GB on disk，**真正的純 4-bit AWQ** ）。然後做兩件事讓 cudagraph 跑起來：
    
    
    1
    2
    3
    4
    5
    6
    

| 
    
    
    ~/vllm-qwen-env/bin/vllm serve cyankiwi/Qwen3.6-27B-AWQ-INT4 \
      --gpu-memory-utilization 0.92 \
      --max-model-len 4096 \
      --max-num-seqs 8 \          # ← 關鍵
      --kv-cache-dtype fp8 \      # ← 關鍵
      --served-model-name qwen-awq
      
  
---|---  
`

  * `--max-num-seqs 8`：vLLM 預設要 capture 51 個 cudagraph size，會 OOM。砍到 8 之後只 capture `[1,2,4,8,16]` 五個
  * `--kv-cache-dtype fp8`：KV cache 從 fp16 壓成 fp8，省一半記憶體



實測：

  * 單流：**80.5 tok/s** （比 enforce-eager 快 4x）
  * 並發 4：263 tok/s
  * 並發 8：**575 tok/s** 🏆
  * 並發 16：574（被 max-num-seqs 上限卡住）



**575 tok/s 是什麼概念？** 比 Ollama 同條件快 9x，比 GPT-4o-mini 的 API 吞吐還高（用同一張卡服務 8 個並發用戶）。

### Config 5：llama.cpp + MTP（單流冠軍）⭐

切換引擎到 llama.cpp，跑 `unsloth/Qwen3.6-27B-MTP-GGUF` 的 Q2_K_XL（**只有 12 GB** ）。

MTP 是 Multi-Token Prediction — 模型內建一個 draft head 預測接下來 2 個 token，target model 驗證。接受率 70%+ 等於免費加速。

Build 過程要小心 CUDA 雷區：
    
    
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
    

| 
    
    
    # 必須用 CUDA 12.9 toolkit，不是 13.2（會輸出亂碼）
    export PATH=/usr/local/cuda-12.9/bin:$PATH
    export CUDACXX=/usr/local/cuda-12.9/bin/nvcc
    
    # Blackwell SM 120 要明確指定
    cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=120 \
      -DCMAKE_BUILD_TYPE=Release -G Ninja
    
    # 需要 PR 22673（MTP 支援還沒進 main）
    git fetch origin pull/22673/head:mtp && git checkout mtp
      
  
---|---  
`

啟動：
    
    
    1
    2
    3
    4
    

| 
    
    
    llama-server -m Qwen3.6-27B-UD-Q2_K_XL.gguf \
      -ngl 99 --ctx-size 4096 \
      --spec-type draft-mtp \
      --spec-draft-n-max 2          # MTP draft 2 個 token
      
  
---|---  
`

實測：

  * 單流：**140 tok/s** 🏆（全場最快）
  * 並發 8：**118 tok/s** （反而退化！）



**MTP 跟 batching 互斥** — draft model 和 target model 共享 KV cache，並發時雙方都要搶記憶體 → batching 失效。

所以 MTP 是「**單人神器、多人毒藥** 」。自己用爽歪歪、開 API 給隊友就完蛋。

### Config 6 + 7：Ollama vs llama.cpp（同一個 GGUF，效能差 3.2x）

這是最反直覺的一段。

**Ollama** （開箱即用，`ollama pull qwen3.6:27b`，內部就是 Q4_K_M GGUF）：

  * 單流：67 tok/s
  * 並發 4：64 tok/s
  * 並發 8：64 tok/s
  * **並發完全不擴展** ，等於序列化



我懷疑是 Ollama wrapper 的問題，所以拿同樣的 Q4_K_M GGUF 用 llama.cpp 直接跑（Config 7）：

  * 單流：75 tok/s（+12%）
  * 並發 4：**204 tok/s** （+219%）
  * 並發 8：189 tok/s



**同一個 GGUF、同一張卡，llama.cpp 比 Ollama 並發吞吐快 3.2x。**

我不知道 Ollama 內部做了什麼把 batching 給關了 — 它預設有 `OLLAMA_NUM_PARALLEL=4`，但實測表現完全不像有 batching。如果你現在用 Ollama 做生產 API，這 3.2x 的效能就是你白白送掉的。

> 小插曲：想用 Ollama 已經下載好的 GGUF 餵給 llama.cpp 不行，會報 `qwen35.rope.dimension_sections has wrong array length`。Ollama 的 GGUF metadata 跟 llama.cpp PR 22673 不相容，要從 unsloth HF 重下載一份。

* * *

## 第三段｜總成績單

Config | 引擎 | 量化 | 模型大小 | GPU 用量 | 單流 | 並發 4 | 並發 8  
---|---|---|---|---|---|---|---  
1 | vLLM | “GPTQ-Int4”（假） | 29 GB | ❌ OOM | - | - | -  
2 | vLLM | NVFP4 + eager | 19 GB | 30.2 GB | 20.5 | 74 | 127  
**3** | **vLLM** | **AWQ-INT4 + cudagraph** | 20 GB | 28.3 GB | 80.5 | 263 | **575** 🏆  
4 | vLLM | AWQ-INT4 單人版 | 20 GB | 28.9 GB | 80.7 | - | -  
**5** | **llama.cpp** | **Q2_K_XL + MTP** | 12 GB | 14.5 GB | **140** 🏆 | 118 | 118  
6 | Ollama | Q4_K_M | 17 GB | 24.6 GB | 67 | 64 | 64  
**7** | **llama.cpp** | **Q4_K_M（無 MTP）** | 16 GB | 17.6 GB | 75 | 204 | 189  
  
三個冠軍的用途分流：

場景 | 推薦 Config | 為什麼  
---|---|---  
自己一個人本地對話、寫 code 副駕 | **Config 5（llama.cpp + MTP）** | 140 tok/s、省顯存 14.5 GB，VRAM 剩一半可以同時開 IDE  
開 API 給團隊/客戶用 | **Config 3（vLLM AWQ）** | 575 tok/s 是其他配置的 5-9x，並發是 production 的本質  
自用 + 偶爾 2-3 人連 | **Config 7（llama.cpp Q4 無 MTP）** | 單流 75 + 並發 204 平衡，build 也不需要 PR 22673  
不想 build、開箱即用 | Config 6（Ollama） | 一行 `ollama pull` 就好，但接受效能只剩 1/3-1/9  
  
* * *

## 第四段｜五個不會寫在 README 的觀察

### 1\. 量化命名不可信，看 config 跟磁碟大小

純 4-bit 量化的 27B 模型應該 ~14 GB。看到 29 GB 還叫 “Int4” 的，多半是 attention/visual 沒量化。檢驗方法：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    # 純 4-bit GGUF 大小參考
    ls -lh *.gguf
    # Q2_K_XL: ~12 GB（極致壓縮）
    # Q4_K_M:  ~16 GB（生產標配）
    # Q6_K:    ~22 GB（高品質）
      
  
---|---  
`

看到 GPTQ/AWQ 模型也是一樣 — 直接看 `config.json` 的 `quantization_config.dynamic` 例外清單，或 `du -sh` 整個目錄。

### 2. vLLM 的 cudagraph 是核心優化，不是 nice-to-have

`\--enforce-eager` 砍掉 cudagraph + torch.compile 之後，速度從 80 跌到 20.5（**-75%** ）。但在 32GB VRAM 跑 27B 模型，**模型本體必須 < 16 GiB** 才有空間給 cudagraph capture。

換言之：選量化版本不要看「能不能載入」，要看「載入後還剩多少給 cudagraph」。

### 3. cudagraph capture 預設 51 個 size 會 OOM

vLLM 預設 `cudagraph_capture_sizes = [1, 2, 4, 8, 16, 24, 32, ..., 512]`，51 個 capture 每個吃幾百 MB，在 32GB 卡上必爆。

解法是 `\--max-num-seqs 8`，把 capture 砍到 `[1, 2, 4, 8, 16]` 五個。如果你只有單流需求，可以更激進 `\--max-num-seqs 1`，只 capture `[1, 2]`。

### 4. MTP 跟 batching 互斥 — 是「個人神器」不是「服務利器」

Q2 + MTP 單流 140，並發 8 退化到 118。Q4 無 MTP 單流 75，並發 8 衝到 189。

原因：draft model + target model 共享 KV cache，並發時雙方都要記憶體 → 互相搶 → batching 退化。

**做個人助理用 MTP，開 API 給人用就不要碰 MTP。**

### 5. CUDA 13.2 + Blackwell 是雷區

Driver 寫支援 CUDA 13.2，但實測會輸出亂碼（Unsloth 官方有警告）。解法：driver 留著、編譯 toolkit 用 12.9。`nvidia-smi` 顯示的 CUDA 版本只是 driver 最高支援，不代表你必須用那個 toolkit。

* * *

## 第五段｜這對 IT 架構意味著什麼

我不是說「全部 workload 都該轉本地」。Claude/GPT 的 API 該用就用，特別是 Opus 級別的長思考任務、複雜 agentic 工作流，雲端旗艦模型還是大幅領先。

但有幾類 workload 現在 ROI 真的翻過來了：

Workload | 雲端 API | 本地 5090 + Qwen3.6-27B  
---|---|---  
員工問答 / 內部知識庫 RAG | 隱私風險 + 重複 token 燒錢 | 全在內網，固定成本  
程式碼補全（IDE inline） | 等待 200-400ms 才開始吐字 | 本機 TTFB < 50ms  
大量批次處理（log 分析、文件摘要） | 跑 1 萬筆要等好幾天排隊 | 並發 8 跑 575 tok/s，一個下午跑完  
Tool calling 為主的 agent | 每個 tool round 都付 token | 一張卡多人共用  
  
**這幾類 workload 的共通點：**

  * 任務不需要旗艦模型（27B 夠用）
  * 量大、重複、token 燒得快
  * 對隱私敏感，或對延遲敏感



**過去半年我給客戶的建議是「先用雲端 API 把流程跑出來，等開源追上再考慮本地」。從這次實測之後，我會改說：**

> 「先用雲端 API 證明流程有 ROI，然後抓你最燒錢、最不能漏的那 20% workload，現在就可以開始評估本地化。**一台 NT$30 萬的 5090 桌機，就是這 20% workload 的最佳 ROI 起點。** 」

不是要全面取代雲端，是 **workload 分流的時機到了** 。

### 回到開頭那個問題

> **「Qwen 3.6-27B 接近 Sonnet 4.6，那能不能在 NT$30 萬以下桌機跑起來？」**

答案是：**能，整套 NT$30 萬剛好卡進企業桌機/工作站採購天花板，不用走資產採購、不用董事會審核。**

但前提是你要：

  * 選對引擎（vLLM 並發、llama.cpp 單人，不要 Ollama 進 production）
  * 選對量化（AWQ-INT4 或 Q4_K_M，不要被「Int4」字面騙）
  * 跳過三個坑（cudagraph capture、MTP vs batching、CUDA 12.9 而非 13.2）



把這幾件事做對，你的 NT$30 萬桌機就是一台「Sonnet 4.6 等級、575 tok/s 並發、零雲端依賴」的 AI 服務器。這不是 demo、不是玩具，是 production-ready 的本地推論。

* * *

## 常見問題 Q&A

**Q: 為什麼不直接買 H100 / B200？**

5090 整機 NT$30 萬，H100 一張卡 NT$100 萬起跳，B200 更貴。如果你的 workload 是「能在 32GB 內塞下的模型，並發 8 以下」，5090 的 NT$/token 比 H100 划算 10 倍以上。H100 適合 70B+ 模型或要做 KV cache 共享的大規模服務，27B 用 H100 是殺雞用牛刀。

**Q: 為什麼不等 Qwen 3.7、5090 改款？**

可以等，但機會成本是「現在用不到本地推論的 6 個月」。我這次實測的目的就是回答「現在這個時間點，到底夠不夠用」 — 答案是夠了。等下一代是無止盡的循環，每代都會有人說「再等等」。

**Q: Mac Studio M3 Ultra 不是也能跑 27B？**

可以，但 token speed 大概是 5090 的 1/3 左右（M3 Ultra 約 40-50 tok/s，5090 cudagraph 配置 80+ tok/s）。Mac 的優勢是統一記憶體可以塞 70B+ 模型，5090 的優勢是純算力快、價格低。**選 Mac 還是 5090，看你要跑多大的模型** 。

**Q: 為什麼 Ollama 並發那麼差，社群還這麼推？**

Ollama 的優勢是「開箱即用」 — 不會 build、不熟 CUDA、不知道 `\--max-num-seqs` 怎麼調的人，五分鐘就有一個能用的 LLM API。對「我只是想試試看本地 LLM」的人來說，這個體驗值很多。但要進 production，請直接用 llama.cpp 或 vLLM。

**Q: Qwen3.6-27B 比 Sonnet 4.6 還強？**

不是，是「某些 benchmark 上接近 Sonnet 4.6 等級」。實際使用品質 Sonnet 4.6 還是更穩、更會處理長 context、更會 reasoning。但對於「員工問 HR 政策、log 分類、code lint、簡單摘要」這類任務，27B 已經足夠 — 而且不會把客戶資料送出公司。

**Q: 要不要等 vLLM 出 FP4 kernel？**

值得期待，但不用為這個延遲決策。AWQ-INT4 + FP8 KV cache 在 5090 上已經跑得很好。FP4 出來估計再快 30-50%，但不會改變「現在能不能做」的答案。

* * *

## 完整 reproducibility

所有實測命令、啟動參數、踩坑紀錄都在我的內部報告：模型版本、cudagraph capture sizes、KV cache dtype、CUDA toolkit 版本，全部列清楚了。如果你也在規劃 5090 / 4090 / RTX PRO 系列跑本地 LLM，這份報告省你的時間絕對超過你的時薪。

**最後總結一句** ：

> 「2026 是本地小模型性價比騰飛的元年。但同一張卡能跑出 64 tok/s 也能跑出 575 tok/s — 差別不是硬體，是你選不選得對。」

* * *

**延伸閱讀：**

  * [Qwen 3.6-27B 本地部署：DGX Spark / Mac mini 跑出 Sonnet 4.6 等級 AI Agent](https://ai-coding.wiselychen.com/qwen-3-6-27b-gb10-home-inference-sonnet-level/)
  * [企業級地端 LLM 系統架構藍圖](https://ai-coding.wiselychen.com/local-llm-enterprise-architecture/)
  * [Tool Calling 1.5 - 本地 LLM Tool Calling 與 27B Sweet Spot](https://ai-coding.wiselychen.com/toolcall-15-local-llm-tool-calling-qwen-27b-sweet-spot/)

---

## [你的 Claude Code 可能被植入後門了：Mini Shai-Hulud npm 供應鏈攻擊全解析](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/)
*🏢 Wisely Chen AI | 2026-05-14*

> 安全研究員 carlini 在 [TanStack/router#7383 的留言](https://github.com/TanStack/router/issues/7383#issuecomment-4425225340) 點出最致命的一招：payload 會在 Linux 上掛 systemd user service、在 macOS 上掛 LaunchAgent（`com.user.gh-token-monitor`），每 60 秒去 poll `api.github.com/user` — token 一被 revoke，立刻 `rm -rf ~/`。

* * *

## 先講結論：現在請暫停 `npm install`

如果你今天看到這篇文章，請先做一件事：

**把手上正在跑的`npm install` / `pnpm install` / `yarn install` 全部停掉。**

不是危言聳聽，是真的有事。

過去一週，npm 生態系正在爆發一場叫做 **Mini Shai-Hulud** 的供應鏈攻擊。截至目前已知範圍：

  * **TanStack 官方 42 個 npm 套件** 遭植入惡意程式碼
  * 已釋出 **84 個惡意版本**
  * 光是 `@tanstack/react-router` 每週下載量就超過 **1,200 萬次**
  * 攻擊已擴散到 **OpenSearch、Mistral AI、Guardrails AI、UiPath、Squawk** 等 170+ 個套件
  * npm 與 PyPI 兩邊都中



而且最噁心的一點是：**這次攻擊專打用 AI 寫 code 的人。**

對，就是你我這種天天開 Claude Code、Cursor、VS Code 的人。

* * *

## 為什麼叫 Shai-Hulud？這個隱喻有夠到位

先說一下這個攻擊的命名梗，因為它真的反映了這次事件的本質。

**Shai-Hulud** 是科幻小說《沙丘》（Dune）裡的「沙蟲」 — 在 Arrakis 星球的沙漠底下蜿蜒穿行的巨型生物。牠的特性是：

  * **無所不在** ：整片沙漠底下都是牠
  * **殺不死** ：人類目前所有武器都對牠無效
  * **會自我繁殖** ：被切斷一段，那一段照樣活下去
  * **平常你看不到牠** ：只有當你太用力踩地面、發出震動，牠才從地底竄出來吃掉你



攻擊者顯然很清楚自己在做什麼 — 他們在惡意 repo 裡**用的 branch 名稱全部取自《沙丘》** ，每個被感染的 repo 描述都被改成同一句話：

> **“Shai-Hulud: Here We Go Again”**

而這個隱喻精準到讓人有點毛骨悚然：

  * **無所不在** → 這次蠕蟲藏在你天天裝的 dependency tree 裡
  * **殺不死** → 你 `npm uninstall` 完，它從 `~/.claude/settings.json` 又活過來
  * **會自我繁殖** → 它是 worm，偷到一個 repo 的 CI key 就感染下一個
  * **平常看不到牠** → 它只在你 revoke token 那一刻才現形 — 然後把你的 home directory 吃掉



而且攻擊者的黑色幽默還不只命名這一層。

### 攻擊者偽裝的身份是「Claude Code 本人」

這次惡意 commit 的提交者身份是：
    
    
    1
    2
    3
    

| 
    
    
    Author: Claude (claude@users.noreply.github.com)
    Committer: Claude Code GitHub App
    Message: chore: update dependencies
      
  
---|---  
`

對，**他冒充的就是 Claude Code 的 GitHub App** 。

你想一下這個畫面：

  * Repo 收到一個 commit
  * 作者顯示是 Claude
  * email 是 `claude@users.noreply.github.com`（看起來像 GitHub 的 noreply）
  * commit message 是 `chore: update dependencies`（每天都看到一百次）



整個維護者 review 介面看下來：**毫無違和感** 。

對於已經習慣讓 Claude / Cursor / Copilot 幫忙更新 dependency 的開發者，這個 commit 看起來就是「你昨晚開的 agent 工作完了」。

這就是 Shai-Hulud 第二層意思 — **牠連你看到牠的時候，都會偽裝成你最信任的東西。**

* * *

## 這次攻擊為什麼這麼難防

過去我們看 npm 供應鏈攻擊，大致都是同一套劇本：

  1. 駭客釣魚拿到 maintainer 的 npm token
  2. 推一個假版本上去
  3. maintainer 發現後 revoke token，下架版本



防禦邏輯也很單純：開 2FA、pin 死版本、看 lockfile，差不多就擋住八成。

但這次 Mini Shai-Hulud 把這套劇本整個翻掉了。

### 1\. 2FA 沒用，因為被打的不是人

TanStack 維護者 Tanner Linsley 親自確認：**整個 team 都有開 2FA** 。沒人帳號被盜。

那是怎麼進去的？

攻擊者 fork 了 TanStack 的 repo，推了一個藏得很深的 commit，然後**騙過 TanStack 自己的 GitHub Actions 發版流程** ，讓 CI 用合法的金鑰幫惡意 code「蓋章認證」。

換句話說，這次被打的不是 npm 帳號，**是整條 CI/CD pipeline** 。

### 2\. SLSA 簽章驗證直接失效

這是史上第一個有完整 **SLSA Provenance（軟體供應鏈 3 級可信證明）** 的 npm 惡意套件。

簡單講，SLSA 就是 npm 給套件貼的「這個版本真的是官方發的，沒被改過」的封條。

過去我們檢查供應鏈安全的最後一道防線就是看這個封條。

而現在 — **封條本身被駭客貼上去了** ，而且是真貨。

所有靠 cryptographic provenance 來檢查的工具，這次全部失靈。

### 3\. `npm uninstall` 殺不掉它

這才是真正讓 AI 開發者該全身發冷的部分。

過去的 npm 惡意套件，最多就是執行一個 `postinstall` script，把你電腦上的 `~/.aws/credentials`、`~/.ssh/` 偷走。你只要：
    
    
    1
    2
    

| 
    
    
    npm uninstall `<package>`
    rm -rf node_modules
      
  
---|---  
`

就乾淨了。

但 Mini Shai-Hulud 不是這樣。它做的事情是：

**修改你的`~/.claude/settings.json` 和 `~/.vscode/tasks.json`，把自己埋進去。**

意思是：

  * 你刪掉惡意套件 ✅
  * 你刪掉整個 `node_modules` ✅
  * 你刪掉整個專案 ✅



**只要你下次打開 Claude Code 或 VS Code，它就會被觸發重新執行一次。**

它把自己掛在 IDE 的 hook 上面，每次你叫 Claude 跑工具、每次 VS Code 跑 task，它就跟著跑一次。

`npm uninstall` 是治標不治本，根本沒有 uninstall 到。

### 4. 死亡開關（Dead-man’s switch）

最狠的一招在這裡。

它偷走你的 GitHub token 之後，會在你本機部署一個 watcher，做一件事：

> **持續監看 GitHub 上的這顆 token 還在不在。**

如果你做了「正常的應變動作」— 發現 token 外洩，跑去 GitHub Settings 把它 revoke 掉 — 那一瞬間：

**它會把你整個 home directory`rm -rf` 掉。**

所有專案、SSH key、設定檔、Downloads 裡那份沒備份的合約 — 全部炸光。

這是教科書級別的勒索手段：**「你不撤 token，我就慢慢偷你的東西；你撤 token，我就毀了你整台電腦。」**

* * *

## 為什麼這次 AI 開發者是高風險族群？

我自己這幾天看下來，感受最深的一點是：

**這次的攻擊面，跟你「依賴 Agent 的程度」成正比。**

### 第一個風險：Agent 不會幫你檢查 lockfile

我們以前裝套件的習慣，是手動敲 `npm install <package>`，會多看一眼版本號。

現在我們開著 Claude Code 寫 code，自然語言講「幫我加上 react-router」，Agent 就直接幫你裝了。

**Agent 不會去看「這個版本是不是 6 分鐘前才剛發佈的」、「provenance 有沒有異常」、「maintainer 有沒有發公告說被打」。**

Agent 對 npm registry 的信任，是無條件的。

### 第二個風險：你的 .claude/settings.json 是「植入後門的完美位置」

Claude Code 的 `settings.json` 設計上就是讓你掛 hooks、定義工具行為的地方。它每個 Claude 事件都會去讀一次。

從攻擊者的角度，這簡直是禮物：

  * ✅ 每次 Claude 工作都會 trigger 一次（持久化）
  * ✅ 寫進去看起來像 legitimate 的 user config（隱蔽性）
  * ✅ Claude 有檔案系統、shell、網路權限（爆破半徑大）



VS Code 的 `tasks.json` 同理。

過去這些檔案本來就在你的 `.gitignore` 裡，你自己也不太會打開看，這就是 perfect hiding spot。

### 第三個風險：pin 死版本也救不了你

過去我們會說：「別用 `^1.0.0`，要用精準版本 `1.0.0`，這樣才安全。」

這次例外。

因為這次的攻擊發生在「官方版本發佈的 6 分鐘窗口期」之內 — 你 pin 死的那個版本號，本身就是惡意版本。

**版本號是對的，內容是壞的，簽章是真的，CI 是合法的。**

你能信任的所有東西，這次都失效。

* * *

## 現在請馬上做這幾件事

我自己昨晚做的清單，提供參考：

### Step 1：暫停所有套件安裝（這小時就要做）
    
    
    1
    2
    3
    4
    

| 
    
    
    # 包含但不限於：
    # - 別 npm install / pnpm install / yarn install
    # - 別讓 Claude Code / Cursor 自動裝套件
    # - CI/CD 上能暫停 build 就暫停
      
  
---|---  
`

如果你不能停 CI（畢竟是 production），至少把 `npm ci --ignore-scripts` 加進去，先擋掉 postinstall script 的執行。

### Step 2：檢查 IDE 設定有沒有被改過

**最重要的兩個檔案：**
    
    
    1
    2
    3
    4
    5
    6
    7
    

| 
    
    
    # Claude Code 的 hook 設定
    cat ~/.claude/settings.json
    
    # VS Code 的 task 設定
    cat ~/.vscode/tasks.json
    # 或專案層級的
    cat .vscode/tasks.json
      
  
---|---  
`

看裡面有沒有你自己沒設定過的 hook、command、task，特別是任何長得像 base64 編碼、curl 到陌生網址、或執行 `node -e "..."` 一行 inline script 的東西。

**有就是中招了。**

### Step 3：跑一次自動化檢查

社群已經有人寫好工具：
    
    
    1
    

| 
    
    
    npx supply-chain-attack
      
  
---|---  
`

它會掃你的 `node_modules`、`package-lock.json`、IDE 設定檔，比對目前已知的惡意套件清單。

（提醒：這指令本身的安全性也請自己評估一下，看一眼 source 再跑。）

### Step 4：旋轉所有 credentials（順序很重要）

這是最容易踩雷的一步。**順序錯了你會自己觸發 dead-man’s switch。**

正確順序：

  1. **先** 把 IDE 設定檔（`.claude/settings.json`、`.vscode/tasks.json`）裡的可疑條目清掉
  2. **再** 把 watcher process 找出來 kill 掉（檢查 `ps aux`、`launchctl list`、crontab）
  3. **然後** 才去 GitHub / GCP / AWS revoke token



如果你還沒清乾淨就先 revoke token，watcher 偵測到的瞬間，你的 home directory 就沒了。

**先確保 watcher 死透了，再去動 token。**

### Step 5：備份 home directory（保險起見）
    
    
    1
    2
    

| 
    
    
    # 不管你有沒有中招，現在就 backup 一份
    cp -a ~/ /Volumes/External/home_backup_$(date +%Y%m%d)/
      
  
---|---  
`

跑完這個再去動 token，至少最壞情況下還救得回來。

* * *

## 坦白說：這件事的長期影響

短期是清毒、換 key。但這次 Mini Shai-Hulud 真正打開的潘朵拉盒子是：

**「合法 CI 簽章 + IDE 持久化」這個組合，從此會被當成標準攻擊模板。**

過去 AI 開發者的安全思維大概是：

  * 不要把 API key commit 進 git
  * 不要 `curl | bash` 不認識的 script
  * 不要安裝來路不明的 VS Code extension



這次之後，要再多加一條：

  * **不要假設你的`~/.claude/`、`~/.vscode/` 是乾淨的。**



我們把 Agent 寫進 IDE config 的便利性，跟攻擊者把後門寫進 IDE config 的便利性，是**同一個便利性** 。

這是 AI Coding 時代要學會接受的新 trade-off。

* * *

## 最後一句話

過去十年，我們用 `npm install` 換來的是極致的開發效率。

過去兩年，我們用 Agent 自動裝套件換來的是再翻一倍的效率。

**這次的代價，這幾天會慢慢浮現。**

不是說 Agent 不能用、npm 不能用 — 我自己也還是會繼續用。

只是這次之後，我會多做一件事：

> **每次 Agent 幫我裝完套件，我自己`cat ~/.claude/settings.json` 看一眼。**

便宜得很，五秒鐘的事。

但這五秒，就是 AI 開發者進入下一個階段必須付的學費。

* * *

## 延伸閱讀

  * [用 Claude Code 做 Linux 系統管理](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/ai-ops-yong-agent-claude-code-linux.md)
  * [ATPM：真實的 Vibe Coding 流程](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/atpm-a-real-production-vibe-coding-process.md)
  * [慢跑開會都能寫 code？Claude Code 讓我一天當 1.5 天用](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/claude-code-yi-bu-xie-zuo-man-pao-kai-hui-dou-neng-xie-code.md)



* * *

## 參考資料

  * [TanStack/router#7383 — carlini 揭露 dead-man’s switch 機制](https://github.com/TanStack/router/issues/7383#issuecomment-4425225340)
  * [TanStack/router#7383 — Issue 主串與 IOC 清單](https://github.com/TanStack/router/issues/7383)
  * **已知 IoC：**
    * Linux systemd user service: `gh-token-monitor.sh`
    * macOS LaunchAgent: `com.user.gh-token-monitor`
    * 輪詢端點：`api.github.com/user`（每 60 秒）
    * 偽造 commit 身份：`claude@users.noreply.github.com`
    * 偽造 commit message：`chore: update dependencies`
  * **受影響套件清單（截至發稿）** ：TanStack、OpenSearch、Mistral AI、Guardrails AI、UiPath、Squawk
  * **持久化目標** ：`~/.claude/settings.json`、`~/.vscode/tasks.json`、`~/.local/bin/gh-token-monitor.sh`

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

**1. Code Review**

你有沒有看過一個 600 行的 PR，測試都過了，AI 說看起來沒問題，然後你就 approve 了？

我有。而且不只一次。

測試過不代表邏輯對，測試過不代表你看懂了這段程式碼在幹嘛。這是最常見的投降點，因為有一個「通過測試」的假陽性在給你安全感。（延伸閱讀：[AI Coding 的驗收流程怎麼做？](https://ai-coding.wiselychen.com/atpm-qa-ru-he-yan-shou-ai-coding-de-cheng-shi/)）

**2. Error Debugging**

「為什麼這個 null pointer exception 出現在這裡？」

AI 說：「在第 47 行加一個 null check。」

你加了，問題消失了，繼續往前走。

但你知道為什麼 null 出現在那裡嗎？不知道。下次同樣的 bug 出現在別的地方，你還是不知道。每一次這樣修，你就積累了一點「理解缺口」。

**3. Architecture Decisions**

這是我剛才說的那個故事。最危險的一種，因為架構決策的影響最長遠，但也是 AI 最容易給出聽起來有道理的答案的地方。

問題不是 AI 說的對不對，問題是你自己有沒有消化成「你的理解」。

**4. 學習階段**

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

**1. 600 行 PR，掃了一遍就 approve** 「測試是通過的」不等於 review。你如果說不出這個 PR 改了什麼、為什麼這樣改，你沒有在 review，你在蓋章。

**2. Bug 修了，但不知道為什麼修的** 你加了那行 null check，問題消失了，繼續往前走。但兩週後，同樣的問題會以新的形式回來找你。

**3. 為某個決策辯護，重建不出 why** 開會時有人問你為什麼選這個方案，你說的是「當時看起來合理」或「agent 說這樣比較好」——你借用了 AI 的信心，但那個 why 從來不是你的。

**4. 沒有 agent 時，不太敢動鍵盤了** 你獨自寫程式的能力，是你真實水位的體溫計。如果這個能力在萎縮，你知道發生了什麼。

**5. 系統壞了，第一反應是「再讓 agent 修」** 不再有「從第一性原理出發，這個問題應該怎麼解決」這個步驟。投降已經變成預設反應，不是主動選擇。

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
2x 容量，零吞吐量代價，幾乎無精確度損失。如果你在跑 vLLM，先開 `\--kv-cache-dtype fp8`，再考慮其他選項。

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

**1\. 故事跟財務數字要 self-consistent。** Block 講「更小、更精的團隊」——它的毛利率本來就承壓，砍 40% 對應到 EBITDA 立刻有結構性改善，故事 = 現金流改善路徑。Oracle 講 AI infrastructure——它公開承諾 $156B 在 GPU 跟 data center capex，砍 30,000 人省下的 $8-10B 年現金流直接灌進 AI 投資，故事 = capex 對齊。**Cloudflare 講「AI agentic 重組」，但 Q1 是 record high、毛利沒承壓、capex 沒爆增——故事跟財報對不上** ，市場看不出這 1,100 人省下的錢要去哪裡。

**2\. 砍的部位要跟故事一致。** Block 是 across-the-board 砍 40%、含 sales、含管理層。Oracle 砍的是 legacy software maintenance、on-prem support、SaaS/Virtual Operations Services（這兩個部門各砍 30%），同時 OCI / AI services 部門在 hiring——非常清楚的「砍舊保新」。**Cloudflare 砍所有非 sales 部門、保留所有 sales** ——說自己 going agentic，但留下整個最 human-process-heavy 的銷售流程。砍的部位跟故事相反。

**3\. 數字要有單位，或者乾脆不給。** Block 全程沒講任何 productivity multiplier，講的是「compounding faster every week」這種定性 framing。Oracle 完全不提生產力，講的是 capex 跟 data center。這兩家都避開了量化陷阱。**Cloudflare 給了 2x / 10x / 100x——一旦你說了數字，市場就會比對你下一季 EPS、margin、revenue per employee** 。給不出來就破功。

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
