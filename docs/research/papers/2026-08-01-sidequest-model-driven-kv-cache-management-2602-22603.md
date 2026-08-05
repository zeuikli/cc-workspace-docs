---
url: "https://arxiv.org/abs/2602.22603"
title: "SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning"
arxiv_id: 2602.22603
collected_at: 2026-08-01
collected_by: routine-d
domain: Caching / KV Cache / Token Budget
pdf_path: pdfs/2602.22603.pdf
year: 2026
---

# SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning

## 摘要 / 核心貢獻

長時間執行、需跨多份文件進行多步推理的 agentic 任務面臨一個關鍵挑戰：當 LLM 從外部檢索並處理資訊時，「LLM context 被外部檢索的 token 主導，導致記憶體用量快速成長並限制解碼效能」。既有壓縮技術仰賴啟發式規則，對複雜推理工作流效果不佳。

SideQuest 提出新方法：讓推理模型本身負責評估 token 重要性，而非套用通用啟發式壓縮。系統利用模型自身的推理能力判斷哪些 context token 值得保留，且壓縮過程作為平行輔助任務運作，避免管理相關的 token 干擾主要推理管線。

關鍵結果：在 agentic 任務上峰值 token 用量降低 **65%**；儘管激進壓縮，準確度退化極小；效能優於既有啟發式 KV cache 壓縮方法；模型僅以 215 筆樣本訓練，顯示學習效率高。

## 與 Harness 的關聯

與既有 corpus 收錄的 CompressKV、SwiftCache、Tangram 等 KV cache 壓縮論文同屬一脈，但差異點在於「壓縮判斷交給推理模型本身、且與主推理管線平行執行」——呼應 core.md「判斷 vs 決定」公理的一個邊界案例：此處「哪些 token 重要」屬 LLM 判斷範疇（非規則式決定），但透過平行任務設計避免判斷過程干擾確定性主流程，可作為未來設計 context-management.md 分層下沉機制的技術參照。
