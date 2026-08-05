---
url: "https://arxiv.org/abs/2604.03759"
title: "Build on Priors: Vision-Language-Guided Neuro-Symbolic Imitation Learning for Data-Efficient Real-World Robot Manipulation"
archived_date: "2026-07-12"
arxiv_id: "2604.03759"
authors: ["Pierrick Lorang", "Johannes Huemer", "Timothy Duggan", "Kai Goebel", "Patrik Zips", "Matthias Scheutz"]
domain: neuro-symbolic-robot-policy
published_date: "2026-04-04"
source_routine: routine-e
---

# Build on Priors: Vision-Language-Guided Neuro-Symbolic Imitation Learning

## 摘要 / 核心貢獻

本文提出一套 neuro-symbolic 框架，用 1–30 筆未標註示範即可教機器人完成操作任務，
自動生成符號規劃領域與控制策略，免除人工領域工程。

**方法：**
1. 將示範切分為技能片段，用 VLM 分類技能、辨識等價狀態
2. 建構狀態轉移圖，透過 Answer Set Programming solver 轉為 PDDL 規劃領域
3. 策略在「控制參考層級」而非原始致動器訊號上訓練，學習更平滑
4. 資料增強技術：把單一示範投影到場景中其他物件上

**驗證：** 主要在真實工業堆高機（forklift）測試，並在 Kinova Gen3 機械臂上以兩個
benchmark 額外驗證。作者稱此為邁向「可擴展、資料高效、免專家、可解釋」神經符號機器人的實務路徑。

## 為何屬「新領域」

`neurosymbolic` / `neuro-symbolic` 關鍵詞在 workspace 自有題庫命中 **0 次**，與同批收錄的
2604.02812（VLM→Behavior Tree）共同構成「neuro-symbolic robot policy」子領域的第二個接地
來源，皆聚焦「用少量監督生成可解釋符號結構取代黑箱端到端策略」這條技術路線。
