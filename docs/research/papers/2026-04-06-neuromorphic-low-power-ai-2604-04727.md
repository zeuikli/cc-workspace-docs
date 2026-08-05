---
url: "https://arxiv.org/abs/2604.04727"
title: "Neuromorphic Computing for Low-Power Artificial Intelligence"
archived_date: "2026-06-28"
arxiv_id: "2604.04727"
authors: ["Keshava Katti", "Pratik Chaudhari", "Deep Jariwala"]
domain: neuromorphic-computing
pdf_path: pdfs/2604.04727.pdf
published_date: "2026-04-06"
source_routine: routine-e
---

# Neuromorphic Computing for Low-Power Artificial Intelligence

## 摘要 / 核心貢獻

傳統矽基計算正逼近能源效率的基本極限。本論文系統梳理神經形態計算如何提供突破路徑：

**核心技術支柱：**
1. **新型元件模態**（novel device modalities）：利用憶阻器（memristor）等非馮諾伊曼元件實現計算與儲存的物理整合
2. **記憶體內計算**（compute-in-memory）：消除傳統 memory-compute 分離的能耗瓶頸
3. **類比動態**（analog dynamics）：利用物理系統的連續態動態執行計算
4. **稀疏通訊**（sparse communication）：仿腦脈衝編碼大幅降低資料搬移能耗

作者強調，實現此潛力需要跨領域整合：材料科學、電路設計、架構開發、以及針對基底物理量身定制的學習演算法——而非單純替換硬體元件。

這與主流 GPU 路線形成對比：神經形態路徑以大幅降低能耗為目標（1000× 潛力），適合邊緣部署的具身 AI。

## 為何屬「新領域」

neuromorphic 關鍵詞在既有題庫命中 **0 次**。Workspace 現有版圖集中於軟體層（LLM/agent），無任何硬體效率/腦啟發計算的覆蓋。
