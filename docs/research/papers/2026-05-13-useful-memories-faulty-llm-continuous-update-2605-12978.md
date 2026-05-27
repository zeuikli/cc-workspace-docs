---
title: "Useful Memories Become Faulty When Continuously Updated by LLMs"
authors: Dylan Zhang, Yanshan Lin, Zhengkun Wu, Yihang Sun, Bingxuan Li, Dianqi Li, Hao Peng
pdf: 2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978.pdf
project_page: "https://dylanzsz.github.io/faulty-memory/"
published: 2026-05-13
source: "https://arxiv.org/abs/2605.12978"
---

# Useful Memories Become Faulty When Continuously Updated by LLMs

**Authors**: Dylan Zhang†, Yanshan Lin†, Zhengkun Wu†, Yihang Sun, Bingxuan Li, Dianqi Li, Hao Peng  
**Affiliations**: University of Illinois Urbana-Champaign (UIUC), Tsinghua University (IIIS)  
**Published**: May 13, 2026  
**Source**: https://arxiv.org/abs/2605.12978  
**Project Page**: https://dylanzsz.github.io/faulty-memory/  
**PDF**: 本地保存 `2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978.pdf`（1.6MB）  
**arXiv ID**: 2605.12978  
**Categories**: cs.AI, cs.LG

> **歸檔說明 v2（2026-05-22 更新）**：初版基於 arXiv Abstract + 推文重建（PDF 解析失敗）。本次補充來源：論文官方專案頁面 dylanzsz.github.io/faulty-memory/，新增三個失效機制完整描述、各 benchmark 量化數據、真實失效案例、Episodic-First 修復架構。

---

## Abstract（完整原文）

Learning from past experience benefits from two complementary forms of memory: episodic traces — raw trajectories of what happened — and consolidated abstractions distilled across many episodes into reusable, schema-like lessons. Recent agentic-memory systems pursue the consolidated form: an LLM rewrites past trajectories into a textual memory bank that it continuously updates with new interactions, promising self-improving agents without parameter updates. Yet we find that such consolidated memories produced by today's LLMs are often faulty even when derived from useful experiences. As consolidation proceeds, memory utility first rises, then degrades, and can fall below the no-memory baseline. More surprisingly, even when consolidating from ground-truth solutions, GPT-5.4 fails on 54% of a set of ARC-AGI problems it had previously solved without memory. We trace the regression to the consolidation step rather than the underlying experience: the same trajectories yield qualitatively different memories under different update schedules, and an episodic-only control that simply retains those trajectories remains competitive with the consolidators we test. In a controlled ARC-AGI Stream environment that exposes Retain, Delete, and Consolidate actions, agents preserve raw episodes by default and double the accuracy of their forced-consolidation counterparts; disabling consolidation entirely (episodic management only) matches this auto regime. Practically, robust agent memory should treat raw episodes as first-class evidence and gate consolidation explicitly rather than firing it after every interaction. Looking forward, reliable agentic memory will require LLMs that can consolidate without overwriting the evidence they depend on.

---

## 核心發現摘要

### 主要問題

記憶整合（Memory Consolidation）是 Agent 記憶系統的主流方法：LLM 將過去的軌跡（trajectories）重寫為更緊湊、可複用的文字記憶庫，並持續更新。本文發現這種方法存在根本性缺陷。

### 關鍵實驗結果

**ARC-AGI 核心實驗**（最震驚的發現）：
- 無記憶基線：GPT-5.4 能 100% 解決某組 ARC-AGI 問題
- 基於完全正確的歷史解答軌跡連續增量整合後：準確率暴跌至 **46%**（即失敗率 54%）
- 問題不在「輸入的 experience 錯誤」，而在「consolidation 步驟本身」

**記憶退化曲線（非單調 utility）**：
- 隨著整合輪次增加：utility 先上升後下降，最終落到 no-memory 基線以下
- WebShop：從 8 個 examples 時的 **0.64** 降到 128 個 examples 時的 **0.20**
- 不同 update schedule 下，同一份 trajectories 產生品質差異巨大的記憶（Static-Group > Static-All > Stream）

**ARC-AGI Stream 環境**（Retain / Delete / Consolidate 三動作控制環境）：
- 允許自主選擇動作的 agent：預設傾向保留原始情節（Retain）
- 強制整合（Forced-Consolidation）的 counterparts：準確率只有自主 agent 的 **一半**
- 完全禁用整合（純 Episodic Management）：與允許自主選擇的 agent 表現相當

### 主要結論

1. **退化根源在 Consolidation 步驟**：不是 experience 品質問題，是 LLM 改寫記憶的過程引入失真
2. **Episodic Memory 保持競爭力**：直接保留原始軌跡 vs 最好的 consolidator，表現相當
3. **工程建議**：
   - 把 raw episodes 視為 first-class evidence（第一手鐵證）
   - 引入顯式門控（explicit gating）：非必要不整合
   - 不要在每次互動後都自動觸發 consolidation

### 前瞻

可靠的 Agent 記憶需要 LLM 能夠在整合時不覆蓋其依賴的證據——這是當前模型尚未具備的能力。

---

## 三個失效機制（來源：專案頁面）

### 1. Misgrouping（錯誤分組）
強制整合時，將不同問題家族的 episode 錯誤歸類為同一組，產生跨類別的混合規則——這些規則不屬於任何真實類別。

### 2. Interference（干擾）
抽象化過程剝除了適用條件，造成過度泛化的教訓（overgeneralized lessons）在相關任務上誤導 agent。  
量化：ScienceWorld 中，「累積整合」（Cumulative consolidation）產生過度泛化記憶的速率是孤立任務整合的 **5×**。

### 3. Overfitting（過擬合）
輸入分佈過窄，使記憶記住的是表面模式而非底層策略。結果：能完美回憶完全相同的 episode，但在相近變體上失敗。

### 理論重新框架
記憶整合本質上是「無接地的迭代生成迴路」（iterated generative loop without grounding）——每次改寫都從模型關於「教訓應該長什麼樣」的先驗中取樣，逐步脫離實際軌跡。跨越多個迭代後，積累的是「可信但與實際發生的事物脫節的文字」。

---

## 方法概述

### 兩種記憶形態的對比

| 形態 | 定義 | 優點 | 缺陷（本文發現） |
|------|------|------|----------------|
| Episodic Traces | 原始軌跡，記錄「發生了什麼」 | 保真度高，無失真 | 存儲成本高，可能冗餘 |
| Consolidated Abstractions | 多 episode 提煉的可複用 schema | 緊湊，理論上可複用 | LLM 改寫引入失真 + 迭代後誤差累積 |

### 實驗設計

- **環境**：ARC-AGI、ALFWorld、ScienceWorld、WebShop、AppWorld、Mind2Web
- **ARC-AGI Stream**：新增 Retain、Delete、Consolidate 三個顯式記憶管理動作
- **整合策略對比**：Static-Group > Static-All > Stream（同一份 trajectories，schedule 不同→品質差異巨大）
- **基線**：no-memory、episodic-only、forced-consolidation
- **模型**：GPT-5.4（及其他）

### 修復方案：Episodic-First 架構

| 方案 | 描述 | 效果 |
|------|------|------|
| Episodic-Only | 保留原始 episode，不抽象 | 與所有 consolidator 持平或更優 |
| Auto Mode | Agent 自主選擇 Retain/Delete/Consolidate | 強制整合的 2× 準確率；400 訓練步後仍領先 |
| 分離式儲存 | 獨立 episodic 層 + schema 層（仿認知科學 dual-system） | 理論上最佳，受認知科學啟發 |

**原則**：raw episodes 是第一手鐵證；抽象只在明確需要時選擇性觸發，不在每次互動後自動執行。

---

## 真實失效案例（來源：專案頁面）

- **ARC-AGI**：19 個任務在 190 步整合後，崩潰成單一錯誤的「統一操作手冊」
- **WebShop**：記憶從 8 個 workflow 擴張到 16 個，其中 8 個是冗餘的類別變體
- **ALFWorld**：50 項記憶在單次整合步驟中縮減為 1 項，後續 6–13 場勝局因此丟失
- **ScienceWorld**：累積出空洞條目（如「使用正確的動作」），佔用檢索頻寬但無實際資訊量

---

## 對本 Workspace 的影響

**直接相關**：本 workspace 的 MEMORY.md + memory-compactor 機制是典型的「consolidated abstraction」範式。

**對應三條工程原則**（來自 @Phoenixyin13 推文補充）：
1. **Raw Episodic Memory 嚴重被低估**：直接把原始交互 Trace 作為 few-shot 效果優於精簡後的規則庫
2. **引入顯式門控**：非必要不整合；鲁棒架構把原始情節視為第一手鐵證
3. **異質任務必須隔離**：跨任務混批整合加速記憶崩潰

**建議評估**：
- memory-compactor 的整合頻率與觸發條件是否過於激進
- 是否在 MEMORY.md 中加入 episodic 層（保留近期 N 個 session 原始記錄不壓縮）
- 不同任務類型（研究/實作/架構）的記憶是否應分開歸檔

---

## 引用

```bibtex
@article{zhang2026useful,
  title={Useful Memories Become Faulty When Continuously Updated by LLMs},
  author={Zhang, Dylan and Lin, Yanshan and Wu, Zhengkun and Sun, Yihang and Li, Bingxuan and Li, Dianqi and Peng, Hao},
  journal={arXiv preprint arXiv:2605.12978},
  year={2026}
}
```

---

## 相關歸檔

- 推文：[research/tweets/2026-05-16-@haopeng_uiuc-410764.md](../tweets/2026-05-16-@haopeng_uiuc-410764.md)（論文作者 Hao Peng 宣布推文，7.3/10）
- 推文：[research/tweets/2026-05-18-@Phoenixyin13-509649.md](../tweets/2026-05-18-@Phoenixyin13-509649.md)（工程解讀 + ARC-AGI 數據，7.9/10）
