---
url: "https://warmwater.dev/blog/paradigm-autoresearch-parallel-agents"
title: "一夜之間 1,039 個策略：Paradigm AutoResearch 黑客松的平行 Agent 設計"
date: 2026-05-12
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code  
#  1,039 個策略，一個晚上：當計算量打敗 Domain Knowledge 
  2026-05-12 · — views      

有人在 2026 年的 Paradigm Autoresearch Hackathon 拿了第一名。42.32 mean edge，贏了所有對手。


他自己說：他幾乎沒有讀問題描述。


這不是在炫耀，而是在描述一個設計決策：不要用人類的 domain expertise 去解問題，讓 AI agents 大規模搜尋解法空間，用計算量打敗專業知識。結果是 1,039 個策略變體、2,000 次以上的 evaluation runs，以及第一名。


這篇要拆解這個系統的設計：為什麼要平行而不是序列、from-scratch reset 為什麼比增量改進更有效、以及多 seed 測試解決了什麼問題。


**讀完這篇，你會理解：**


- Bitter Lesson 在 agent 設計上的具體含義，以及什麼時候計算量真的打敗 domain knowledge

- 為什麼平行 8-20 個 agent 比一個 agent 跑 8-20 次根本上不同

- From-scratch reset 怎麼解決增量改進陷入局部最優的問題

- Multi-seed robustness 為什麼是評估系統的核心，不是 optional 的


這篇不是交易策略的教學，也不是 hackathon writeup 的翻譯。它是在問：**這個系統的設計哲學是什麼，以及它在什麼條件下成立？**

---


## Bitter Lesson 在 Agent 設計上意味著什麼？


Rich Sutton 的 Bitter Lesson 只有一句話：在 AI 的歷史上，最終獲勝的永遠是利用更多計算量的方法，而不是人類把 domain knowledge 編碼進去的方法。在 LLM agent 時代，這個教訓的新版本是：不要手工設計解法，讓 agents 大量搜尋。


Paradigm Hackathon 是一個做市商預測競賽，在一個模擬的訂單薄裡，你要設計報價策略讓盈利最大化。這種問題傳統上需要深厚的市場微結構知識：了解 arb 行為、retail flow 的統計特性、spread 和 depth 的 tradeoff。


作者選擇的路徑是讓 agents 去學這些，不是自己去學。他的角色不是設計師，而是系統架構師，設計一個讓 agents 可以大量搜尋的系統，然後把結果餵給更多 agents。


這個選擇的前提，和 Karpathy 的 autoresearch 一樣：**你需要有一個可以自動評分的 evaluation function**。在這個案例裡是 mean edge（每筆交易的平均盈利），可以自動計算、結果清楚、可以用多個隨機 seed 驗證。有了這個，計算量才能替代 domain knowledge。

---


## 為什麼要平行跑 8-20 個 Agent？


平行 agents 解決的不是速度問題，而是 exploration diversity：序列式搜尋的每一步都在上一步的基礎上改，探索路徑是有偏的，越改越接近同一個方向的局部最優，很難跳出去。同時跑 8-20 個帶著不同假設的 agents，才能覆蓋解法空間的不同角落。


Karpathy 的 autoresearch 是序列式的：一個 agent，改 → 評估 → keep/discard → 繼續。這個設計簡單可靠，但有的 agent 試著調 spread 參數，有的試著改 sizing 公式，有的從零開始重寫整個策略邏輯，這些是 sequential search 在同等時間內做不到的。


Agent briefing 的設計很具體。有效的 agent prompt 包含五個要素：

```
1. 明確的假設（hypothesis to test）
2. 基礎策略（base to modify，或 "start from scratch"）
3. Evaluation 協議（seeds, sims, 解析方式）
4. 目標門檻（target to beat: "+25 avg"）
5. 迭代次數上限（"iterate up to 3 times"）
```


特別值得注意的是「目標門檻」。告訴 agent 要打敗 +$25，不是告訴它「盡量做好」，這讓 agent 的搜尋有方向，不是漫無目的地亂試。


平行規模隨實驗階段調整：早期探索用 8-10 個，高峰期跑 20 個，後期細調時每波仍用 20 個但只做特定方向的驗證。總計 1,039 個策略變體。

---


## From-Scratch Reset 怎麼打破增量改進的天花板？


From-scratch reset 的核心設計是：告訴 agent 忽略所有既有代碼，只給它問題規則加上已確認有效的 insights，讓它從零重建解法。這個做法在 Phase 4 產生了單次 +$25 → +$44 的跳躍，超過之前所有增量改進的總和。


前三個 phase 每次都在既有代碼上做增量改進，一步一步往前推。Phase 4 卡在 +$25 avg，數百次嘗試都無法突破。每個小修改要嘛沒效果，要嘛小幅退步。增量改進會把 agent 困在現有代碼的「引力場」裡，它在修改既有邏輯，而不是在質疑既有邏輯的前提假設。


From-scratch agent 的做法：

```
- 告訴 agent 忽略所有既有代碼，從零開始
- 只給它：問題規則 + 已確認有效的 domain insights + 目標分數
- 不給它：700+ 個前期策略的任何代碼

結果：
- 從零開始的 agent 獨立發現了「arb-risk-weighted sizing」公式
- 單次跳躍：+$25 → +$44（超過之前所有增量改進的總和）
```


這個結果背後有個重要的設計細節：from-scratch agent 拿到的不是空白，而是「已確認有效的 domain insights」，也就是前幾個 phase 跑出來的 learnings 精華。它不需要重新發現「arb 行為是主要 risk」這件事，但它可以從零開始設計怎麼應對這個 risk。


這個規律不只適用於交易策略。任何 agent 系統在序列式搜尋停滯的時候，引入 from-scratch agent 是一個有理論依據的突破手段，不是隨機亂試，而是在已知 insights 的基礎上重新建構。

---


## Multi-Seed Robustness：為什麼不能信任單次評分？


Multi-seed robustness 是 autoresearch 評估設計的核心原則：優化 multi-seed average，不優化 single-seed max。用單一 seed 得到的高分可能只是運氣，跨多個 seed 都穩定才代表策略本身有效。


早期實驗只用 seed=0 評估。本地看起來 +$44 很好，換一個 seed 卻是 +$34 到 +$70，分布太廣，代表那個 +$44 是運氣，不是策略本身的品質。在 leaderboard 導向的競賽裡這個問題特別危險：排行榜用的是固定 seed，你可以針對那個 seed 優化，但最終評分用的是 3 個全新的 random seed 的 median，針對單一 seed 優化的策略往往在最終評分崩掉。


作者設計了三層評估：

```
Layer 1: Local Eval（快速迭代）
  - 4 個 seed（0, 500, 1000, 2000）× 200 sims
  - 早期嘗試用，快速篩選方向

Layer 2: Leaderboard Eval（單一固定 seed）
  - 只代表一個 seed 的表現
  - 可以用，但不能 overfit

Layer 3: Final Eval（3 次 fresh random seeds 的 median）
  - 真正的 robustness 測試
  - 最終提交前用 16 個不同 seed（3,200 sims）確認
```


這個設計的工程含義是：evaluation function 的設計本身需要 robustness 設計。如果你的 evaluation 可以被運氣攻擊，agent 系統最後就會收斂到運氣最好的方案，不是最穩健的方案。

---


## 死路文件化怎麼解決平行 Agent 的集體記憶問題？


平行 agents 沒有共享記憶，死路文件化是廉價的解法：把每條失敗的實驗方向寫成帶量化依據的 Markdown 文件，新 agent 啟動時先讀這些文件，就能站在所有前序失敗的基礎上繼續搜尋。


如果 agent A 試了 multi-level quoting 發現 −$3.46，agent B 可能在三小時後試同樣的東西，又花了資源確認同一個結論。在 1,039 個策略的規模下，這種重複探索的浪費是可觀的。


嘗試方向結果根因Multi-level quoting−$3.46給 arb 更多可吃的訂單Bayesian/Kalman mid 估計−$3手工 heuristic 勝過 principled approachRetail quantity capping−$9.62Retail 爆發式到來，capping 損失 2× arb 節省Parameter sweeps~0100+ sweep agents 確認 landscape 平坦


每條死路要有數字，不能只說「試了不行」。「Retail quantity capping 的 −$9.62 across multiple seeds」比「capping 沒效果」有用得多。後者後來的 agent 看到還是可能覺得「也許我的實作方式不同」，前者有量化依據，說服力強。

---


## 多模型交叉授粉為什麼能突破搜尋瓶頸？


不同模型有不同的歸納偏差，它們傾向以不同的方式分解問題、選擇不同的抽象層次。當主力模型連續失敗，引入另一個模型對同一問題獨立建構解法，可以覆蓋主力模型的盲點。


主力是 Claude Code agents，卡住時引入 Codex agents 對同一問題獨立建構解法。Codex 提出了一個不同的架構想法（per-side arb-probability sizing、高概率 throttling），這些想法被提取出來，餵回 Claude Code agents 作為新 hypotheses，最後整合進最終策略。


這不是說 Codex 比 Claude Code 好，或反過來。而是說當一個搜尋系統已經在某個方向上連續失敗，引入不同的「思考方式」是一個有依據的打破局面的手段。

---


## 這個系統在什麼條件下成立？


autoresearch 能讓計算量打敗 domain knowledge，需要同時滿足四個條件。缺少任何一個，這套設計就不適用。


條件說明缺少時的問題可自動評分的 evaluation functionmean edge 可以自動算沒有 eval，agent 不知道結果好不好Evaluation 本身有 robustness 設計多 seed average，不是 single-seed max系統收斂到運氣，不是能力解法空間足夠大才值得平行探索空間小的話，序列式搜尋就夠了From-scratch 有 learnings 傳遞前期 insights 精華完全空白的重置等同於亂試


不是所有問題都能這樣解。「這份報告寫得好不好」沒有可自動評分的 evaluation function，就無法套用。但滿足這四個條件的問題，計算量確實可以打敗 domain knowledge。

---


> 


**結語**：1,039 個策略不是暴力搜尋，而是一個有設計的搜尋系統。Bitter Lesson 的真正含義不是「不需要 domain knowledge」，而是「把 domain knowledge 用在設計搜尋系統上，而不是用在設計解法上」。
     [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Source Code不預裝能力，只定義生長方式：GenericAgent 原始碼解析2026-05-22](/blog/generic-agent-source-code)
