---
url: "https://arxiv.org/abs/2604.19818"
title: "Beyond Task Success: An Evidence-Synthesis Framework for Evaluating, Governing, and Orchestrating Agentic AI"
archived_date: 2026-07-30
arxiv_id: 2604.19818
authors: ["Christopher Koch", "Joshua Andreas Wellbrock"]
collected_at: 2026-07-30
collected_by: routine-d
domain: harness-engineering
pdf_path: pdfs/2604.19818.pdf
published_date: 2026-04-18
---

# Beyond Task Success: An Evidence-Synthesis Framework for Evaluating, Governing, and Orchestrating Agentic AI

## 摘要 / 核心貢獻
綜合 24 篇近期文獻，指出 agentic AI 部署的核心缺口：評測與治理框架各自獨立存在，未連結到具體 runtime 動作或合規驗證（governance-to-action closure gap）。提出三項產出：① 四層框架，整合評測/治理/編排/保證橫跨 agentic 系統全生命週期；② ODTA runtime-placement test，以 observability／decidability／timeliness／attestability 四準則評估控制手段是否可實作；③ Minimum Action-Evidence Bundle，規範 agent 狀態改變動作所需的最小證據文件。發現：評測研究將安全性/穩健性/軌跡層級量測列為未解缺口；治理框架定義義務但缺少執行期控制邏輯；文字層級的對齊不可靠地轉移到工具動作層級。以企業採購 agent 情境為例說明概念，未引入新實驗數據。

## 與 Harness 的關聯
「governance-to-action closure gap」精準對應本 workspace core.md 判斷 vs 決定公理與 `core.md §PROPOSE 委派`（原 `graph.md §G4`） Handoff Contract 的 Done-when／Return 契約設計初衷——治理意圖若不落地為 runtime 可驗證的最小證據，就只是紙面規範；ODTA 四準則可作為稽核既有 `[E]`/未標二分（原 `[E*]`，v5.1 廢除三分類） gate「缺哪個 Body」時的外部檢核清單。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
