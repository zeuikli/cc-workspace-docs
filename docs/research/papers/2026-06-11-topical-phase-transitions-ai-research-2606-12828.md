---
url: "https://arxiv.org/abs/2606.12828"
title: "Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evidence and an Early-Warning Signature for Emerging Topics"
archived_date: "2026-07-12"
arxiv_id: "2606.12828"
authors: ["Rasul Khanbayov", "Hasan Kurban"]
domain: ai-topic-emergence-detection
published_date: "2026-06-11"
source_routine: routine-e
---

# Topical Phase Transitions in Artificial Intelligence Research

## 摘要 / 核心貢獻

本論文把「AI 研究這個領域本身」當作動力系統，用計量科學（scientometrics）方法分析
2017–2025 年五大 AI 會議（ACL、CVPR、ICLR、ICML、NeurIPS）共 80,814 篇主軌論文，
發現主要 AI 主題以「相變」（phase transition）模式擴散：多年維持邊緣狀態，
接著在 1–3 年內跨會議暴增為主流。

**關鍵發現：**
- LLM 相關主題在 2025 年成為跨會議主導議題；diffusion models 以類似陡峭幅度崛起
- 語言模型方法透過 vision-language models 跨界滲入電腦視覺
- 強化學習呈現平滑漸進成長，可與真正的「相變」區辨（非暴增型）

**早期預警訊號**：作者以 2017–2021 資料校準出 4 項 publication-dynamics 早期預警指標，
在 2023–2025 樣本外驗證達成 63% recall（對照 13.5% 的隨機基線）。將此訊號套用於 2025
資料後，標記 reasoning/test-time-compute、agentic AI、multimodal LLM、RAG、world models
為 2026–2028 應持續監控的主題。程式碼已公開於 GitHub。

## 為何屬「新領域」

`phase-transition` / `topic-emergence` / `scientometrics` 等關鍵詞在 workspace 自有題庫
（`research/NEW-DOMAINS/covered_topics.txt` + DAILY-TOPICS/WEEKLY-FOCUS/papers 標題詞庫）
命中 **0 次**。Workspace 的既有論文集中於「做 AI 研究」本身（agent/LLM/harness 456 篇），
但從未研究「AI 研究這個領域如何演化、如何提前偵測新興主題」這個 meta-science 層次——
與 Routine E 自身「如何系統性發現下一個新領域」高度自我指涉，屬全新邊疆。
