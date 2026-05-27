---
title: "Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead"
arxiv_id: 2603.10062
authors: Zhongming Yu, Naicheng Yu, Hejia Zhang, et al.
published: 2026-03-09
source: "https://arxiv.org/abs/2603.10062"
source_tier: P
---

# Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead

**ArXiv**: 2603.10062 | **Date**: 2026-03-09 (修訂 2026-03-30) | **Authors**: Zhongming Yu, Naicheng Yu, Hejia Zhang, et al. | **Category**: cs.AR, cs.AI, cs.MA

## 摘要

Position paper，將多 agent 記憶管理重新框架為**計算機架構問題**，從 CS 傳統系統設計借鑑概念。隨著 LLM agent 演化為協作型多 agent 系統，本文提供正式架構框架。

## 核心框架

### 記憶範式區分

| 範式 | 描述 |
|------|------|
| 共享記憶（Shared Memory） | agent 存取共同資源（類比 SMP）|
| 分散記憶（Distributed Memory） | 各 agent 維護獨立記憶系統（類比分散式計算）|

### 三層記憶階層

借鑑傳統計算機架構原則：
1. **I/O 層**：agent 與外部世界的記憶交換
2. **快取層**（Cache）：高頻訪問記憶的快速存取
3. **主記憶層**（Primary memory）：持久化長期記憶

### 識別的協議空白

兩個關鍵缺口：
- **跨 agent 的快取共享**（Cache sharing across agents）
- **結構化記憶存取控制**（Structured memory access control）

## 最緊迫的開放挑戰

**多 agent 記憶一致性**：當多個 agent 同時存取或修改共享資訊時，確保系統維持一致、可靠的資料狀態。

對應傳統計算機架構的「快取一致性（Cache Coherency）問題」，但在 LLM agent 環境中更難解決（語義豐富性、非確定性推理）。

## 學術意義

主張橋接兩個傳統上分開的領域：計算機架構 ＋ 人工智能。

傳統多核處理器的快取一致性解決方案（MESI 協議等）可能為多 agent 記憶一致性提供設計啟發。

## 對 Workspace 的意義

與 `2026-05-05-coordination-architectural-layer` 互補：
- 前者從「協調」視角（agent 間通訊協議）
- 本文從「記憶」視角（共享狀態一致性）

多 agent fan-out 設計中「child 間不直接溝通」的規則，部分原因正是為了避免共享記憶一致性問題。

## 分類

**Memory Architecture / Agent Architecture & Coordination** — 首篇從計算機架構視角系統性分析多 agent 記憶的 position paper，為多 agent 系統的基礎架構設計提供理論基礎。
