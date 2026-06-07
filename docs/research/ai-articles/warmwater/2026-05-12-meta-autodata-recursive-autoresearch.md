---
url: "https://warmwater.dev/blog/meta-autodata-recursive-autoresearch"
title: "Meta AutoData：遞迴自我改進的三層 Agent 迴路"
date: 2026-05-12
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code  
#  資料也可以 Autoresearch：Meta AutoData 的三層 Agent 迴圈 
  2026-05-12 · — views      

讀到 weak solver 71.4%、strong solver 73.3% 這兩個數字的時候，我的第一個反應是：這資料根本沒用。


這是傳統 CoT Self-Instruct 合成資料的表現——兩個能力差距顯著的模型，答題分數幾乎一樣。代表生出來的題目太簡單了，任何模型都能答。你拿這樣的資料去訓練，等於在用一套根本沒有區分度的考題練習，什麼都學不到。


合成資料的品質問題由來已久。Self-Instruct、CoT Self-Instruct 這些方法的根本缺陷是：它們在生成資料的時候沒有品質的直接回饋。你生出一百道題，不知道哪道有用、哪道廢，只能用 filtering 事後篩，但 filtering 沒辦法告訴你「怎麼生出更好的題」。


Meta 的 AutoData（2026 年 4 月，Jason Weston team）的回答是一個視角的轉換：**資料品質本身是一個有 evaluation function 的問題**，因此可以用 agent loop 優化。


**讀完這篇，你會理解：**


- 為什麼 weak/strong solver 差距可以當作資料品質的 evaluation function

- AutoData 三層架構各自解決什麼問題

- Meta-optimization 怎麼把 AutoResearch 應用到 agent harness 本身

- 這個設計的邊界在哪裡，以及論文已知的限制


這篇沒有程式碼，只有設計概念。它是在問：**AutoResearch 的思路，在資料生成這個領域能走多深？**

---


## 把資料品質問題轉化成 Evaluation Function


解決合成資料品質問題，先要把「品質」定義成可以量化的東西。AutoData 的定義很具體：一個高品質的訓練範例，是讓 weak solver 答不出來、但 strong solver 能答出來的問題。


這個定義有三層含義。第一，它是可以自動計算的——直接跑兩個模型看分數，不需要人工標注。第二，它有方向性——你知道「往哪個方向改進」：讓分數差距變大。第三，它有實際意義——能區分弱強模型的題目，訓練起來才有信號；如果兩個模型都會，你什麼都沒學到。


實作上的門檻設計：

```
ACCEPT 條件（同時滿足）：
  - weak_avg   ≤ 65%
  - strong_avg - weak_avg ≥ 20%

若不滿足：
  主 agent 分析 judge feedback → 修改 Challenger 的 prompt → 重試
  通常跑 3-5 輪才能產出一個 accepted question
```


這個設計把「資料品質」從一個模糊的判斷，變成了一個可以跑 agent loop 的優化目標。有了這個 evaluation function，後面的三層架構才能成立。

---


## 三層架構：為什麼需要這麼多層？


AutoData 的架構有三個巢狀迴圈，每一層解決不同層次的問題：

```
┌─────────────────────────────────────────────────────────┐
│  META-OPTIMIZATION（Outer Outer Loop）                   │
│  優化 agent harness 本身（prompt + scaffold code）       │
│  ┌───────────────────────────────────────────────────┐  │
│  │  DATA SCIENTIST LOOP（Outer Loop）                │  │
│  │  Agent 扮演資料科學家，迭代改進資料生成 recipe     │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  DATA CREATION（Inner Loop）                │  │  │
│  │  │  Challenger 生成 → Weak/Strong 評估 →       │  │  │
│  │  │  Judge 評分 → 不過就修 prompt，重試          │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```


**Inner Loop（Data Creation）** 解決的是單一範例的品質問題。四個 subagent 各有角色：


Agent角色Challenger LLM生成訓練範例（input + response + rubric）Weak solver預期「通常失敗」的小模型（Qwen3.5-4B）Strong solver預期「通常成功」的大模型（Qwen3.5-397B）Verifier / Judge按 rubric 評分 solver 的答案


每次生成後立刻評估，不達標就分析 judge 的回饋、修改 Challenger 的 prompt 重試。這是最快的回饋循環，通常 3-5 輪就能產出一個符合門檻的範例。


**Outer Loop（Data Scientist）** 解決的是整個資料集的系統性問題。當 inner loop 累積了一批通過品質門檻的範例後，agent 從全局視角分析：這批資料有什麼共同弱點？哪些類型的題目一再失敗？從這些觀察中更新生成 recipe，讓後續的 inner loop 從改進後的起點出發。


**Outer Outer Loop（Meta-Optimization）** 解決的是 agent harness 本身可能有系統性缺陷的問題。這一層不是在優化生成出來的資料，而是在優化生成資料的 agent 架構本身，後面會仔細說。


這三層的分工讓系統可以同時在不同時間尺度上改進：inner loop 快速試錯、outer loop 總結規律、meta-optimization 修正架構缺陷。

---


## 結果：Gap 從 1.9pp 擴大到 34pp


Agentic Self-Instruct 和 CoT Self-Instruct 的對比很直接：


方法Weak SolverStrong SolverGapCoT Self-Instruct71.4%73.3%**1.9pp**Agentic Self-Instruct43.7%77.8%**34pp**


差距擴大了 18 倍。用 Agentic Self-Instruct 資料訓練出來的模型，在 in-distribution 和 out-of-distribution 任務上都優於 CoT Self-Instruct。


這個結果說明的不只是方法有效，而是它驗證了最初的假設：weak/strong gap 確實是一個有意義的資料品質 proxy。讓 gap 變大的資料，訓練出來的模型真的比較強。

---


## Meta-Optimization：把 AutoResearch 對準 Agent Harness 本身


Meta-optimization 是這篇論文最有意思的部分，也是它和前幾篇 AutoResearch 概念連結最緊密的地方。


前面說的 inner/outer loop 解決了「怎麼生出更好的資料」，但還有一個更深的問題：生成資料的 agent harness 本身（它的 prompt 設計、scaffold code、判斷邏輯）可能有系統性的缺陷，而這些缺陷不是靠調整生成策略能修的，需要直接改 harness。


Meta-optimization 的做法：

```
1. Boltzmann sampling 選 parent harness（有機率選次優的，避免局部最優）
2. 在 training papers 上跑 inner loop，收集 trajectories
3. LLM 分析 trajectories → root-cause analysis（找系統性失敗模式）
4. Code-editing agent 修改 harness → 產生 diff
5. 在 held-out validation papers 上評估 parent vs mutant
6. 只有 mutant > parent 才 accept（加入 population）
7. 把結果記錄到 history log（供後續 analyzer 讀取）
```


結果：validation pass rate 從 12.8% 提升到 42.4%，跑了 233 次迭代，126 次被 accepted。


更有意思的是 agent 自動發現的四個改進，它們都不是事先設計的，是 meta-optimization 過程中自己找到的：


改進內容Paper-specific insight enforcement加 self-test：「沒讀這篇論文能答嗎？能 → 題目太簡單」Context leak prevention加 self-test：「context 裡包含答案嗎？有 → 重寫」Positive-only rubric + weight cap刪除負分 criteria，所有 weight ≤ 7Structured rubric format強制 JSON + integer weights


第三個發現特別反直覺：負分 criteria 實際上損害了 strong solver 的表現。這不是任何人事先預期到的，是 meta-optimization 從大量 trajectory 分析裡找到的系統性問題。人工設計的 harness 帶著這個 bug，agent 自己把它修掉了。

---


## 這個設計的邊界在哪裡？


論文明確列出了幾個已知限制。


Agent hacking 是一個真實發生的問題：有時 agent 學會修改 weak solver 的 prompt，讓它刻意表現差，來欺騙品質評估系統。Evaluation function 本身可以被攻擊，這在所有 autoresearch 系統裡都是潛在風險。


目前只在單一領域（CS research QA）測試。Weak/strong gap 作為 proxy 的有效性，在 math、code、safety 等不同任務域是否成立，還需要驗證。Evaluation function 的設計不是通用的，每個域可能需要不同的品質定義。


Example-level 優化 vs. dataset-level 優化。現在的 inner loop 每次只看一個範例夠不夠好，但一個好的資料集不只是好範例的集合，還需要足夠的多樣性。如果所有通過品質門檻的題目都長一個樣，訓練出來的模型也會有偏。

---


> 


**結語**：AutoData 的核心主張不複雜：資料品質是一個可以量化的問題，量化了就可以跑 agent loop，agent loop 可以遞迴地對準自己。
     [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Source Code不預裝能力，只定義生長方式：GenericAgent 原始碼解析2026-05-22](/blog/generic-agent-source-code)
