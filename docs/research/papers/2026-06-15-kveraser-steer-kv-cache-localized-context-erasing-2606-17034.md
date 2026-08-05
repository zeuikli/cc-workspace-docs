---
url: "https://arxiv.org/abs/2606.17034"
title: "KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing"
arxiv_id: 2606.17034
collected_at: 2026-08-02
collected_by: routine-d
domain: Caching / KV Cache / Token Budget
pdf_path: pdfs/2606.17034.pdf
year: 2026
---

# KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing

## 摘要 / 核心貢獻

處理完的 context 片段（例如已回答的干擾性/有害輸入、過期指令）需要從 KV cache
中「抹除」，但其影響已透過 attention 傳播進所有後續快取狀態，導致傳統做法必須整段
重算才能真正移除影響。KVEraser 提出一種可學習的方法：只替換被抹除區間的 KV 狀態，
用訓練過的「steering states」壓抑其殘留影響，同時保留其餘快取不動。訓練分兩階段：
先在通用的區段移除任務上預訓練，再針對特定任務微調。

實測橫跨 1K–32K context 長度：效能幾乎與全量重算持平，但延遲僅增加 24%（對比
全量重算的 17.6× 延遲）；在含有害干擾內容的長文件問答任務上，相較完整重算達 3–4×
加速；且能泛化到訓練時未見過的任務類型，優於近似基準方法。發表於 ICML 2026
Memorization and Trustworthy Foundation Models workshop（oral）。

## 與 Harness 的關聯

對應 context-management 的「compact 可翻轉決策」與 memory 治理場景：當某段對話
內容需要事後「精確抹除」（例如誤導性指令、已撤回的敏感輸入）而不想付出整段重算
成本時，KVEraser 的局部 steering 抹除提供了比「整段丟棄重算」更精細的技術路線，
值得作為未來 context erasure 機制設計的參考案例。
