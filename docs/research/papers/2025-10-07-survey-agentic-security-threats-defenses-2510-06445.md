---
url: "https://arxiv.org/abs/2510.06445"
title: "A Survey on Agentic Security: Applications, Threats and Defenses"
archived_date: 2026-07-30
arxiv_id: 2510.06445
authors: ["Asif Shahriar", "Md Nafiu Rahman", "Sadif Ahmed", "Farig Sadeque", "Md Rizwan Parvez"]
collected_at: 2026-07-30
collected_by: routine-d
domain: ai-safety-red-teaming
pdf_path: pdfs/2510.06445.pdf
published_date: 2025-10-07
---

# A Survey on Agentic Security: Applications, Threats and Defenses

## 摘要 / 核心貢獻
綜述 260+ 篇文獻，圍繞三支柱組織：LLM-based agent 在資安場域的應用、agentic 系統固有漏洞、防護對策。結論：「agentic 系統結構性地天生脆弱」，需要橫跨整個 agent lifecycle 的多層防禦。首次提出連結應用/威脅/防禦三者的統一分類法（先前多為孤立處理）；分析攻擊進入點、鎖定的 agent-loop 階段、威脅模型、對 agentic 情境的特異性；評估各防禦手段的成本-安全 tradeoff 與部署時點；並整理哪些防禦對應哪些攻擊、agent 架構/模型使用/資料模態的演進趨勢。

## 與 Harness 的關聯
「agentic 系統結構性地天生脆弱」與本 workspace core.md「能力悖論：能力提升不得換取更少驗證」同一立場的大規模文獻佐證；其攻擊進入點×agent-loop 階段的分類框架，可作為 `core.md §PROPOSE 委派`（原 `graph.md §G5`）（委派安全與採信紀律）與 `core.md §APPLY 自主迴圈`（原 loop.md）各 `[E]`/未標二分（原 `[E*]`，v5.1 廢除三分類） gate 缺口盤點時的外部威脅模型參照。
