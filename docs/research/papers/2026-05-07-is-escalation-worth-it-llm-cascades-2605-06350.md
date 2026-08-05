---
url: "https://arxiv.org/abs/2605.06350"
title: "Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades"
archived_date: 2026-07-31
arxiv_id: 2605.0635
authors: ["Dylan Bouchard"]
collected_at: 2026-07-31
collected_by: routine-d
domain: llm-routing-cost
pdf_path: pdfs/2605.06350.pdf
published_date: 2026-05-07
---

# Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades

## 摘要 / 核心貢獻
建立一套決策理論框架，刻畫模型級聯（model cascades，便宜模型先處理、複雜查詢再升級至昂貴模型）的最佳成本-品質權衡。發現雙模型級聯在成本-品質前沿呈現分段凹性；k 模型系統可透過成對組合分析，找出最佳模型配對的切換點；一階條件會使各階段邊際品質/成本相等。跨 5 個 benchmark（MATH/MMLU/TriviaQA/SimpleQA/LiveCodeBench）、8 個模型、5 家供應商的驗證顯示，級聯效能主要受限於「結構性成本」——因為級聯在做出升級決策前必須先付便宜模型那一輪的成本；一個輕量的「生成前路由器」在多數資料集上優於最佳化過的級聯，因為它能避免不必要的便宜模型運算。

## 與 Harness 的關聯
直接對應本 repo self-escalate 與 multi-mode-skill 的檔位路由設計——「生成前路由優於生成後升級」的實證結論，是「先分類再選檔位」優於「先跑便宜檔位、失敗再升級」策略的外部證據，值得回饋進 `model-profiles.md` 的升降級計數規則設計。
