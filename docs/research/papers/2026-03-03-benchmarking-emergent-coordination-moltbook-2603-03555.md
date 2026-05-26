---
title: Benchmarking Emergent Coordination in Large-Scale LLM Populations
authors: "Brandon Yee, Pairie Koh"
published: 2026-03-03
source: "https://arxiv.org/abs/2603.03555"
source_tier: P
arxiv_id: 2603.03555
---

# Benchmarking Emergent Coordination in Large-Scale LLM Populations

**ArXiv**: 2603.03555 | **Date**: 2026-03-03 (修訂 2026-04-26) | **Authors**: Brandon Yee, Pairie Koh | **Category**: cs.MA

## 摘要

針對大規模去中心化 agent 族群的評估框架，解決現有評估方法在研究大規模去中心化 LLM 族群時的不足——自組織和資訊傳播模式是有機湧現的，而非顯式設計的。

資料集：**MoltBook Observatory Archive**，包含 **90,704 個自主 agent** 的 **2.73M 次互動**。

## 評估框架三維度

1. **角色專業化**（Role specialization）
2. **資訊擴散**（Information diffusion）
3. **協作任務解決**（Cooperative task resolution）

## 主要量化發現

| 指標 | 量化值 | 意義 |
|------|-------|------|
| 核心-外圍結構清晰度 | 輪廓係數 **0.91** | 高度清晰的網路層次結構 |
| 資訊級聯分佈 | 冪律 α = **2.57** | 資訊傳播遵循冪律（偶發性病毒式傳播）|
| 去中心化協調開銷 | Cohen's d = **-0.88** | 相比單一 agent 基線的顯著性能退化 |

## 核心發現

- **核心-外圍結構**：少數 agent 在資訊傳播中扮演不成比例的核心角色
- **重尾級聯**：資訊傳播主要局部化，偶有「病毒式」事件
- **協調開銷**：去中心化任務解決相比集中式方法存在可測量的性能退化（d = -0.88）

## 學術貢獻

通過建立標準化評估任務和實證基準，使未來多 agent 協議的嚴格比較成為可能。評估方法本身被定位為值得科學研究的主題。

## 對 Workspace 的意義

大規模去中心化 agent 族群的研究確認：
- fan-out 上限設計（≤4 sub-agents）有助於控制協調開銷
- 核心-外圍結構在實際系統中自然湧現，主 agent 作為協調節點的設計符合觀察規律

## 分類

**Benchmark & Evaluation / Agent Architecture & Coordination** — 90K+ agent 真實互動資料集分析，為大規模多 agent 系統評估建立首個量化基準。
