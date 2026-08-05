---
url: "https://arxiv.org/abs/2607.17227"
title: "Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation"
archived_date: 2026-07-23
arxiv_id: 2607.17227
authors: ["Sally Chen", "Roxana Zahedi", "Lucy Chhuo", "Ricky Nguyen", "Marjan BaghGolshani", "Amin Beheshti", "Mark Grosser", "Min Yang", "Nona Farbehi", "Nigel Lovell", "Ahmadreza Argha", "Fatemeh Vafaee", "Youqiong Ye", "Hamid Alinejad-Rokny"]
domain: genomic-biological-foundation-models
published_date: 2026-07-19
source_routine: routine-e
---

# Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation

## 摘要 / 核心貢獻
本文以統一（harmonised）評測框架，比較六個代表性單細胞/空間轉錄體基礎模型（Nicheformer、CellPLM、scGPT-spatial、GenePT、scELMo、Novae），涵蓋 scRNA-seq、空間轉錄體（spatial transcriptomics）、以及 Perturb-seq 三類資料型態。核心發現：這些基礎模型的泛化能力高度依賴訓練/測試資料的脈絡（context-dependent generalisation）——同一模型在不同組織類型、不同技術平台產生的資料上表現落差顯著，質疑「通用生物表徵」（universal biological representation）這一領域樂觀敘事的普適性，主張評測應納入脈絡遷移（context-shift）情境而非僅同分布測試集。

## 為何屬「新領域」
單細胞/空間轉錄體基礎模型的跨脈絡泛化評測，是生物基礎模型評測方法論的最新分支，與 workspace 既有版圖完全不重疊；關鍵詞於既有覆蓋集合與既探勘新領域紀錄命中皆為 0。
