---
url: "https://arxiv.org/abs/2604.11548"
title: "SemaClaw: A Step Towards General-Purpose Personal AI Agents through Harness Engineering"
arxiv_id: 2604.11548
collected_at: 2026-08-01
collected_by: routine-d
domain: Harness Engineering
pdf_path: pdfs/2604.11548.pdf
year: 2026
---

# SemaClaw: General-Purpose Personal AI Agents through Harness Engineering

## 摘要 / 核心貢獻

本文以 2026 年初 OpenClaw 興起、數百萬使用者開始部署個人 AI agent 為背景，指出 AI 開發方法論正從傳統 prompt engineering 轉向完整的基礎設施設計。研究處理兩個交織的挑戰：① **典範演進**——從 prompt/context engineering 邁向「harness engineering」，即建構完整系統把不受約束的 agent 轉化為可控、可稽核、可上生產的解決方案；② **互動典範轉移**——從離散的任務式互動轉向人類與 AI agent 之間持續、具情境感知的協作關係。

框架提供四項核心組件：① **Agent 協調**——DAG 為基礎的兩階段混合式方法論協調多 agent；② **安全系統**——PermissionBridge 行為安全框架控管 agent 行動；③ **Context 管理**——三層架構處理情境資訊；④ **知識整合**——agentic wiki skill 支援自動化個人知識庫建構。

核心洞見：隨著模型能力趨於平台期，差異化因素轉移至基礎設施層——即使可靠、可信賴的 agent 部署得以實現的 harness 系統。

## 與 Harness 的關聯

四項組件與本 workspace 既有設計高度平行：DAG 協調對應 `Workflow` 工具的 pipeline/parallel 原語；PermissionBridge 對應 core.md「不可逆操作永遠等確認」的權限層設計；三層 context 管理對應 `context-management.md` 的 progressive disclosure 下沉分層；agentic wiki 對應 `dreaming-consolidator` 的記憶固化機制。可作為「模型能力平台期後差異化在 harness」此一命題的外部佐證，呼應 core.md 公理「Model 可換；Body = hooks/gates/CI」。
