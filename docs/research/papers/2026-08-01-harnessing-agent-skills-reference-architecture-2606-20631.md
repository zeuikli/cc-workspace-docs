---
url: "https://arxiv.org/abs/2606.20631"
title: "Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents"
arxiv_id: 2606.20631
collected_at: 2026-08-01
collected_by: routine-d
domain: Harness Engineering
pdf_path: pdfs/2606.20631.pdf
year: 2026
---

# Harnessing Agent Skills: Architectural Patterns and a Reference Architecture

## 摘要 / 核心貢獻

本文檢視 LLM agent 如何運用以「skill artifact」形式外部化的行為知識——這些靜態資源在被 agent 選取與執行時轉為動態，作者稱之為「skill-in-use」狀態。研究聚焦於如何可靠地治理這個從靜態到動態的轉換過程：如何綁定至當前 context、如何強制授權邊界、如何為稽核與改進留存證據。

作者透過實證研究，整理出一套 10 種架構模式的目錄（5 種核心 + 5 種輔助），並綜合為一個劃分四層責任的參考架構：**供應鏈（Supply Chain）**、**中介（Mediation）**、**執行控制（Execution Control）**、**證據與回饋（Evidence & Feedback）**。此框架經跨 8 個系統的實例化分析驗證。

研究提供實務者一套詞彙與診斷框架，可用來分析各 agent 系統中「skill-harnessing」責任的分工方式。透過將架構模式分類，本研究為 LLM agent 如何發現、解讀、執行 skill——同時維持可歸責性並支援持續精煉——建立了系統化的分析方法。

## 與 Harness 的關聯

> 2026-08-02 深讀 PDF 原檔（23 頁）後重寫，對齊 v5.1。

直接對應 `.claude/skills/RESOLVER.md` 的 skill-first 路由設計。論文的核心概念 **skill-in-use**（skill artefact 是靜態的，其架構責任只在「被選中、綁定 context 與權限、由隨機性 agent 詮釋、留下 run 證據」的那次執行中才成立）給 workspace 一個現成詞彙：SKILL 檔寫得好 ≠ 該次執行行為正確，兩者之間隔著綁定與詮釋兩道隨機性。

四層責任框架可作為稽核**現行 17 個 skill**（v5.1 精簡後；原 26 個）的檢查表：

| 論文層 | workspace 對應現況 |
|---|---|
| Supply Chain（供應鏈） | `.claude/skills/` git-tracked + `RESOLVER.md` 註冊；v5.1 已收斂 |
| Mediation（中介/選取綁定） | `RESOLVER.md` BM25 索引 + 觸發詞表；**最弱的一環**——觸發詞重疊由 `skill-roster-audit` 人工稽核，無機械判準 |
| Execution Control（執行控制） | hooks（`block-dangerous` / `test-integrity-guard` 等 13 支）+ settings.json 權限 |
| Evidence & Feedback（證據與回饋） | **v5.1 主動移除**——review/verification 收據制度、`record-*-receipt.sh` 全數刪除 |

**⚠️ 與 v5.1 的張力**：第四層「Evidence & Feedback」是論文四層裡唯一被本 workspace 整層拿掉的。v5.1 的理由是收據的受眾是「要對第三者交代的組織」；論文的定位則不同——證據層服務的是 **attribution / verification / repair / evolution** 四件事，其中 repair 與 evolution 是自用的（沒有 run 證據就無法歸因哪個 skill 在哪一步失效，也就無法迭代）。這正好命中 workspace 現況：`skill-evolution` 的評分目前只能讀 SKILL 檔靜態內容，讀不到「這個 skill 實際被觸發後表現如何」，因為沒有 run 級證據留存。

**可行動的最小補丁（僅記錄，非提案）**：不需還原收據制度；論文的證據層最小形態是「哪個 skill 在哪次 run 被啟用」的一行記錄。v5.1 刪 `tool-log.sh` 的判準是「純寫入無消費者」——若 `skill-evolution` 要能做效果評分，消費者就存在了，該判準的結論會翻轉。

⚠️ 論文的 cross-instantiation 只覆蓋 8 個系統，且以框架級專案為主，對單人 workspace 規模的外推效度未驗證。
