---
title: Wisely Chen AI — 2026-04-29
date: 2026-04-29
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-04-29

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [DeepSeek V4 §3.1 那 200 字才是真正的地震——訓練棧硬體無關，跑得上中國國產卡](https://ai-coding.wiselychen.com/deepseek-v4-section-3-1-hardware-agnostic-earthquake/)
*🏢 Wisely Chen AI | 2026-04-29*

§3.1 ｜ 200 字 ｜ NVIDIA + 昇騰 ｜ 1.5～1.96× ｜ 訓練棧硬體無關

為什麼今天想聊這件事

DeepSeek V4 真正的地震，藏在技術報告的 §3.1，講訓練系統那一章。短短不到 200 字的英文段落。我看到的時候停了大概有十分鐘——因為這件事的工程含義，可能比 V4 模型本身的能力還要重要。

一、§3.1 那 200 字到底寫了什麼

原文是這樣：

“We validated the fine-grained EP scheme on both NVIDIA GPUs and HUAWEI Ascend NPUs platforms. Compared against strong non-fused baselines, it achieves 1.50 ~ 1.73× speedup for general inference workloads, and up to 1.96× for latency-sensitive scenarios such as RL rollouts and high-speed agent serving.”

直翻：他們在 NVIDIA GPU 跟華為昇騰 NPU 兩個平台上，都驗證了同一套細粒度 expert parallelism 方案，相對於沒做 fusion 的 baseline，跑出 1.50～1.73 倍加速；在 RL rollouts、高速 agent serving 這種延遲敏感場景，最高到 1.96 倍。

第一眼會覺得：「就一個 benchmark 嘛，誰家論文不貼這種圖。」

但有三個重點：

第一，這段話出現在 §3.1，講『訓練系統』的那一章，不是推理。

Inference 框架要做硬體抽象，業界早有成熟路徑（TensorRT-LLM、vLLM、SGLang、ONNX）。但 training 對通訊拓樸、記憶體、kernel fusion 的依賴，比 inference 高一個數量級。能在訓練端做到硬體抽象，技術門檻完全不同。

第二，「fine-grained EP scheme」是 MoE 訓練最複雜的那塊。

Expert parallelism 牽涉到 all-to-all 通訊、token 分發、負載平衡、通訊跟計算 overlap，是整個 training stack 裡最吃硬體底層、最難移植的部分。最難搬的都搬通了，剩下的（dataloader、optimizer、checkpointing、gradient sync）只會更好搬。

第三，兩個平台上的加速比落在同一個區間。

1.50～1.96× 在 NVIDIA Hopper 跟華為達文西架構上都成立。這不是「能編譯過去跑得起來」，是「效能曲線吻合」。前者叫「能 run」，後者叫「能用」。

把這三點合起來，這 200 字其實只在傳達一句話：

DeepSeek 的訓練棧，做到了硬體無關。而且驗證對象就是中國國產的昇騰 NPU。

二、為什麼「訓練」做到硬體無關特別重要

過去這幾年，AI infra 真正的死結不在推理，在訓練。

推理可以多供應商——你今天用 NVIDIA、明天換 AMD、後天上 TPU，只要框架支援，模型 weight 搬過去 fine-tune 一下就能跑。

但訓練不行。訓練棧一旦寫死在 CUDA 上，就等於把命交給一家硬體廠。Framework 沒人 port、kernel 沒人寫、人才不存在、生態不存在。你拿一億美金也沒辦法在半年內把訓練棧從 CUDA 搬到 CANN 還跑出能用的效能。

§3.1 這 200 字的意義，是第一次有一個剛訓出 SOTA 級別模型的訓練棧，在 NVIDIA 跟華為昇騰上都跑出對齊的效能。而且驗證的是訓練端，不是推理端。

三、跟 GLM-5 比，差在哪裡

可能有人會說：「中國模型在華為上訓練，GLM-5 不是早就做了嗎？」

對，GLM-5 確實做了——28.5 trillion token、~100,000 顆昇騰 910B、MindSpore 框架、零 NVIDIA。這是第一個完全不用 NVIDIA 訓出來的 frontier 級模型，本身就是大事。

但 GLM-5 跟 V4 §3.1 證明的是兩件不同的事：

GLM-5：「能在華為昇騰上訓出 SOTA。」 訓練棧基本上是綁在昇騰 + MindSpore 這條路徑上。

V4 §3.1：「同一套訓練棧，在 NVIDIA 跟昇騰上都跑得出對齊效能。」 訓練棧本身做到了硬體抽象。

換句話說，GLM-5 證明了單一替代路徑可行，V4 §3.1 證明了訓練棧本身可以是 vendor-agnostic。前者是「我換了一家也能 run」，後者是「我寫一次、兩家都能用」。

對企業策略而言，後者的意義更大——因為它代表訓練端第一次有了真正的可移植性，而不只是「換一個鎖」。

四、雙向驗證：華為這邊也對上了

光看 DeepSeek 單方面講還不夠。但華為官方 GitHub 上有一個倉庫叫 cann-recipes-train——注意倉庫名最後是 train——裡面已經有 DeepSeek V4-Flash 在昇騰 A3 集群上做續訓練（CPT）的參考實現。

論文（DeepSeek 設計層）+ 廠商 GitHub（華為實作層）兩邊指向同一個結論。如果訓練棧沒有真的 vendor-agnostic，這個倉庫不會存在；存在但跑不通，華為不會公開掛上去。

五、不能太樂觀的部分

照例把不能太樂觀的擺出來：

CPT ≠ 完整預訓練。 目前華為這邊跑通的主要是續訓練，不是從零訓 trillion-token 的完整預訓練。後者對 numerical stability 的要求是另一個量級，可能還要等 950PR / 960 級別硬體配合，樂觀估計 12～18 個月。

單卡算力 + 生態還有差距。 昇騰跟 H100 / B200 單卡 spec 還有距離，CANN 算子庫覆蓋率、文件、第三方 framework 整合，跟 CUDA 生態還有 5～10 年代差。

V4 模型本身能力還有差距。 Code Arena 上被 GLM 5.1 壓 70 分，跟 Claude Opus 4.7、GPT-5.5 也有距離。當第一線生產工具還早。

但「能力差距」跟「根基缺失」是兩種不同性質的問題。能力差距是版本迭代問題，可以靠 RLHF、資料、post-training 補。根基缺失是結構性問題，是訓練用的卡明天可能買不到。

V4 §3.1 解的是後者。

一句話總結

DeepSeek V4 真正的地震不是價格、不是跑分、不是百萬 token，而是 §3.1 那段 200 字證明了——訓練棧可以做到硬體無關，而且驗證平台就是中國國產的昇騰 NPU。

跑分會迭代，能力會追上。但「訓練端不押注單一晶片廠」一旦建立起來，是不可逆的。

真正的訊號，從來不在頭條裡。

---
