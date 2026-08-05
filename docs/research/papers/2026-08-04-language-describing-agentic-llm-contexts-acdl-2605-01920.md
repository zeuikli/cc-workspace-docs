---
url: "https://arxiv.org/abs/2605.01920"
title: "A Language for Describing Agentic LLM Contexts"
arxiv_id: 2605.0192
collected_at: 2026-08-04
collected_by: routine-d
domain: Context Engineering
pdf_path: pdfs/2605.01920.pdf
year: 2026
---

# A Language for Describing Agentic LLM Contexts

## 摘要 / 核心貢獻

作者指出 LLM agent 系統目前多用非正式散文、隨手畫的圖或直接讀程式碼來說明其 prompt 組成方式，缺乏標準化表示法。論文提出 ACDL（Agentic Context Description Language），提供精確、可讀、標準的方式描述 LLM 輸入 context 如何在互動步驟間建構與演變。ACDL 支援角色訊息、動態內容、時間索引參照與條件結構，且獨立於實作細節。作者以多個系統範例示範 ACDL 用法，並鼓勵在學術論文與實務開發中採用，文件與工具已公開。

## 與 Harness 的關聯

呼應 core.md「References > 散文 spec」原則的反向命題：本文提出的是「context 組成本身」的標準化描述語言，可作為未來若要讓 sub-agent brief 或 skill 的 context 組成方式可機械稽核（而非僅靠散文描述）時的形式化參考。
