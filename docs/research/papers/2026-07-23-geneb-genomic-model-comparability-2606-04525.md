---
url: "https://arxiv.org/abs/2606.04525"
title: "GENEB: Why Genomic Models Are Hard to Compare"
archived_date: 2026-07-23
arxiv_id: 2606.04525
authors: ["Daria Ledneva", "Mikhail Nuridinov", "Denis Kuznetsov"]
domain: genomic-biological-foundation-models
published_date: 2026-06-03
source_routine: routine-e
---

# GENEB: Why Genomic Models Are Hard to Compare

## 摘要 / 核心貢獻
GENEB 是一個診斷式 benchmark，評估 40 個基因體基礎模型（genomic foundation models）在 100 個任務、13 個功能類別下的凍結表徵（frozen representations），採統一的 probing-based 協定（含 few-shot 評估情境），讓模型規模、架構、tokenization、預訓練資料等變因可被控制比較。核心論點：genomic foundation model 領域近年模型數量爆量增生，但缺乏可比的診斷式評測框架，導致各家 SOTA 宣稱難以獨立驗證——這與傳統 NLP/CV 基礎模型評測已有的標準化程度形成落差。論文透過系統性拆解各模型在不同功能類別（如調控元件辨識、變異效應預測等）上的表現差異，指出「模型架構」與「預訓練資料規模」對下游表現的貢獻並不總是符合直覺假設，部分被高度引用的模型在特定任務類別上反而遜於更簡單的基線。

## 為何屬「新領域」
基因體基礎模型評測方法論與 workspace 現有版圖（agent harness / LLM 工程 / GCP FinOps / SRE）完全正交；grep 核心關鍵詞（genom/biobank/biological-foundation 等）於既有 daily-topics、papers 關鍵詞集合、以及 research/NEW-DOMAINS 既探勘領域紀錄，命中皆為 0。
