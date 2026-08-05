---
url: "https://arxiv.org/abs/2606.20058"
title: "Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale"
archived_date: 2026-07-31
arxiv_id: 2606.20058
authors: ["Harsh Rao Dhanyamraju", "Leonidas Raghav", "Aaron Lee"]
collected_at: 2026-07-31
collected_by: routine-d
domain: multi-agent
pdf_path: pdfs/2606.20058.pdf
published_date: 2026-06-18
---

# Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale

## 摘要 / 核心貢獻
針對企業級多代理部署（小團隊到 200 代理規模）系統性比較編排策略，發現「規模而非任務複雜度」才是決定編排效能的主因，且代理探索（agent discovery）在大規模部署時成為主要瓶頸。作者引入 Task Manager 元件，在 208 個源自生產環境的企業場景評測中，將高優先序佇列延遲降低 14–75%，相關事件正確率提升逾 20 個百分點。

## 與 Harness 的關聯
「規模主導編排效能、探索成本才是瓶頸」的結論，直接對應 `core.md §PROPOSE 委派`（原 `graph.md §G3`）「fan-out 有上限」與委派拓撲設計——當節點數增加，發現/路由成本會蓋過任務本身複雜度，是設計 Handoff Contract 與速率閘時的量化佐證。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
