---
url: "https://arxiv.org/abs/2606.13796"
title: "Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral Characterization"
archived_date: 2026-07-31
arxiv_id: 2606.13796
authors: ["Naïl B. Khelifa", "Richard E. Turner", "Ramji Venkataramanan"]
domain: model-collapse-recursive-training
published_date: 2026-06-11
source_routine: routine-e
---

# Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral Characterization

## 摘要 / 核心貢獻

本文研究 diffusion model 遞迴訓練在自身輸出上導致的 model collapse，找出一個先前被忽略的機制：即使 score 估計完美、取樣精確，反向擴散過程為數值穩定所做的「提前停止（early stopping）」本身就足以驅動一種漸進式、系統性偏離真實資料分佈的 drift——也就是說，即使每一步技術上都做對，崩潰仍會發生。

主要貢獻是證明遞迴訓練會以幾何速度收斂到一個獨特的極限分佈，該分佈可表示為真實資料分佈之高斯平滑化版本的無窮混合。頻譜分析進一步顯示，遞迴訓練的作用等同於一個低通濾波器：對高階非高斯特徵的壓制遠比對粗糙特徵劇烈——換言之，分佈的細部結構是崩潰的第一個受害者，而非整體平均品質。論文提出退火截斷排程（annealed truncation schedules）來緩解誤差累積，並在 Gaussian mixture 與 CIFAR-10 上驗證，理論框架在存在離散化誤差與 score 估計誤差時依然穩健。

## 為何屬「新領域」

本文刻畫的是遞迴訓練導致崩潰的**解析機制**（極限分佈存在性、幾何收斂速度、頻譜低通特徵），這在 workspace 既有覆蓋（agent harness、memory/context engineering、machine-unlearning）中完全未觸及。既有唯一提及 model collapse 的既存論文（`2607-07663` 遞迴自我改進分類法）僅將其列為失效模式分類項之一，未涉及任何機制層內容；`spectral characterization`／`autophagy`／`self-consuming` 等本文核心術語在全庫（reports/papers/DAILY-TOPICS/WEEKLY-FOCUS）0 命中。
