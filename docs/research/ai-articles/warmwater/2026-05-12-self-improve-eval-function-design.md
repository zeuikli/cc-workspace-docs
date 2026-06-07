---
url: "https://warmwater.dev/blog/self-improve-eval-function-design"
title: "你能量化什麼，AI 就能最佳化什麼：自我改進的評估函數設計"
date: 2026-05-12
category: Viewpoint
source: warmwater.dev
---

[
← Viewpoint ](/blog?tag=Viewpoint)  Viewpoint  
#  你能把問題量化成什麼，AI 就能優化什麼 
  2026-05-12 · — views      

寫完這四篇，我一直有一個感覺：這些方法表面上在做不同的事，但它們卡在同一個地方。


Karpathy 的 AutoResearch 讓 agent 自己跑 Kaggle 比賽。Paradigm Hackathon 的並行 agents 探索解法空間。HuggingFace ml-intern 把用戶的工作 session 收集成 SFT 訓練資料。Meta AutoData 讓 agent 迭代生成有區分度的合成資料，然後遞迴地把同一套邏輯對準 agent harness 本身。


四個方法，四個領域，但它們都在問同一個問題：你怎麼知道改進了？


這個問題的答案，決定了系統能走多遠。


**讀完這篇，你會理解：**


- 這四個方法的共同結構是什麼

- 為什麼 eval function 的清晰度決定改進的上限

- 把問題轉化成 evaluation function，需要什麼條件

- 為什麼這個轉化本身，常常比你要解的問題還難


這篇是系列的 Viewpoint——不是每篇的摘要，而是把四篇放在一起之後才能說的話。

---


## Karpathy、Paradigm、ml-intern、AutoData：四個方法共享什麼結構？


這四個方法表面上做的事情不一樣，但它們的運作邏輯是一樣的：定義「什麼叫進步」，跑一些實驗或收集一些資料，量一下有沒有進步，然後從結果裡提取信號繼續改。


差別在於「什麼叫進步」這個問題怎麼回答：


Karpathy 和 Paradigm 用 Kaggle 分數和任務成功率——這些 eval 是現成的，不需要設計，問題本身就定義了什麼叫答對。


ml-intern 用的是任務有沒有完成（`pushed_to_hub: True/False`）——這個 eval 不是人工定義的，而是從任務本身的 outcome 隱式產生的。


Meta AutoData 用的是 weak solver 和 strong solver 的答題差距——這個 eval 是設計出來的，需要先論證「gap 越大 = 資料品質越好」這個假設成立。


**這個差別不只是技術細節。** Eval 是現成的，你可以直接開始跑；eval 需要設計，你就得先花工夫論證它是有效的。四個方法分別落在這個光譜的不同位置，它們的挑戰也因此完全不同。

---


## 讀完四篇，哪些模式反覆出現？


這四個方法在不同場景和設計下，有三個模式一直在出現：eval 的清晰度決定改進的上限、遞迴是同一個原則的自我應用、失敗的 trajectory 包含成功不包含的資訊。

### Eval 的清晰度決定改進的上限


Karpathy 的系統能改進，是因為 Kaggle 分數是一個非常乾淨的 eval：一個數字，自動計算，無法爭議。每次實驗結束你都知道有沒有進步，進步了多少。


ml-intern 的 `pushed_to_hub` 也是乾淨的：任務完成就是 True，否則 False。不需要人工判斷，大量 session 可以全自動標注。


反過來看，如果你的改進目標是「程式碼品質」或「回答的有用程度」，eval 就變得模糊。人工評估昂貴且不一致，LLM judge 的標準漂移，A/B test 需要大量流量。Eval 越模糊，系統從每次實驗中得到的信號越嘈雜，改進越慢，甚至根本改進不到正確的方向。


這不是說模糊目標就沒辦法做 AutoResearch，而是：**改進到哪裡，取決於你能把目標量化到多精準。** Eval 的天花板，就是系統的天花板。

### 遞迴是同一個原則的自我應用


Meta AutoData 的 meta-optimization 層在做的事，是把 inner loop 的邏輯對準 inner loop 本身——用同樣的 eval 機制來評估 agent harness 的好壞，然後迭代改進 harness。


這個思路不只是「加一層」，而是一個設計原則：如果一個原則在一個層級上有效，問問自己它能不能對準這個原則本身的運作機制。


ml-intern 的 Flywheel 也有類似的結構：訓練出來的新版 ml-intern 又繼續收集 session，又繼續訓練下一版。每一代的 agent 都在為下一代的訓練提供資料。


遞迴不是魔法，但它是一個值得問的問題：「這個改進機制本身，可以被改進嗎？」

### 失敗的 trajectory 包含成功不包含的資訊


這個觀察在 ml-intern 的 SFT Flywheel 最明顯。一個 `research → write → test → fail → debug → fix → success` 的 session，記錄了 agent 在哪裡卡住、用了什麼假設、怎麼修正。這個「失敗然後恢復」的模式是合成資料幾乎無法產生的。


Meta AutoData 的 meta-optimization 在分析 trajectories 的時候，也是從失敗中找到了最有價值的發現：負分 criteria 在懲罰 strong solver。這個 bug 在所有成功的 trajectory 裡是看不到的——它只在失敗的 trajectory 裡才會顯現。


**成功告訴你「做什麼」，失敗告訴你「哪裡卡住」。** 一個只保留成功案例的訓練集，學到的是結果，不是過程中的判斷。

---


## 設計一個可以驅動 Agent 自我改進的 Evaluation Function，需要什麼條件？


把這四個方法放在一起，有一個問題開始變得顯眼：eval function 從哪裡來？Kaggle 分數是現成的，任務成功率是任務本身給的，但 weak/strong gap 是 Meta AutoData 自己設計的——而且論文花了顯著的篇幅在論證這個設計為什麼有效。


這個對比說明了一件事：在某些問題上，eval function 本身就是你需要解決的問題，不是前提。Meta AutoData 的設計選擇是 weak/strong solver gap，理由是它可以自動計算、有方向性、和真正的訓練價值相關。這個選擇不是唯一的，也不是顯而易見的。


什麼條件讓一個 eval function 可以驅動 agent 自我改進？


**可以自動計算。** 這是最基本的條件。Eval 需要人工介入的話，就沒辦法大量跑 agent loop。Kaggle 分數、任務成功率、weak/strong gap 都可以全自動計算；「程式碼可讀性」不行。


**難以被輕易 hack。** Meta AutoData 論文裡明確提到 agent hacking：agent 學會修改 weak solver 的 prompt，讓它刻意表現差，來製造出看起來很好的 gap。Eval function 一旦可以被最佳化本身（而不是最佳化真正的目標），系統就會朝錯誤的方向走。所有 AutoResearch 系統都有這個潛在風險。


**和真正的目標相關。** Eval function 是代理指標，不是目標本身。weak/strong gap 是「訓練資料品質」的代理，Kaggle 分數是「機器學習能力」的代理。代理指標和真實目標的相關性，決定了讓 eval 最大化能不能真的帶來你想要的改進。


**對改進有感度。** 這個條件常被忽略。一個 eval 即使滿足前三個條件，如果它對細微的改進不夠敏感——信噪比太低，小的進步淹沒在 variance 裡——系統就很難從每次實驗中學到東西。Paradigm AutoResearch 用 multi-seed 平均而非單次最大值，就是在解決這個問題：讓 eval 對改進更敏感、更穩定。


這四個條件裡，「難以被 hack」和「對改進有感度」之間有一個根本張力。一個高度敏感的 eval 往往更容易被 hack；一個防 hack 設計得很嚴的 eval 往往信號弱、敏感度低。你必須在這兩個方向之間找到平衡，而正確的平衡點取決於你的系統設計和任務特性。


這四個條件也可以反過來讀：一個問題，如果你能找到滿足這四個條件的 eval，它就是 agent self-improve 的候選目標。從這個角度看，AutoResearch 的邊界不是計算量，而是 eval function 的覆蓋範圍。


目前這些方法都在 eval 比較清晰的軟體問題上。但有一批問題正在往這個方向靠近：CTF 安全挑戰已經有人在用 LLM agent 嘗試，「拿到 flag」是二元的、自動計算的 eval；數學定理證明用 Lean 或 Coq 這類形式化系統，「proof compiles」也是乾淨的二元信號；程式碼正確性用測試通過率，這在工程場景裡幾乎是現成的 eval。這三個領域的共同點是：對錯有可以自動驗證的地面真相。


往後更難的問題是那些 eval 本身就很貴的領域：藥物研發需要等真實實驗結果，材料科學的模擬準確度很高但成本也高，政策模擬的 outcome 可能要等幾年。這些不是「結構上無法轉化」，而是「反饋迴路太慢、太貴」。如果這個瓶頸某天被解決了——更快的模擬、更便宜的驗證——這些領域的 eval function 設計就會變成下一個值得認真投入的地方。

---


## 為什麼 Eval Function 的設計本身，常常和研究問題一樣難？


有一個更深的問題藏在這裡：如果你的 eval function 本身也需要被最佳化，你需要一個 meta-eval 來評估 eval function 的好壞。但 meta-eval 本身也是一個 eval，它也需要一個 meta-meta-eval……


這個遞迴不是沒有出口，但出口不是在技術裡——出口是人類的稀疏判斷。在某個層級，你需要人去說「這個 eval function 抓到了正確的東西」或「這個 eval 被 hack 了」。


這不代表 AutoResearch 無法擴展，而是說：**eval function 的設計需要人類的 domain knowledge，而且這個 knowledge 不能被完全自動化掉。** 你設計的 eval function 越接近真實目標，系統能走的路就越長；eval function 設計得越差，計算量和資料量的投入只是更快地往錯誤的方向走。


這四篇分析的方法，都在不同程度上隱含了這個挑戰。Kaggle 的分數是現成的，所以 Karpathy 可以直接開始跑；Meta AutoData 的 weak/strong gap 是設計出來的，所以 Jason Weston team 在設計 eval 這件事上花了顯著的工夫，論文也專門描述了這個設計決策的邏輯。


Eval function 的設計是 AI 工程師的判斷力，不是 AI 可以替代的部分——至少不是在這個層級上。這是這四個方法共同指向的東西，也是我在讀完這四篇之後最想留下的一個觀察。

---


> 


**結語**：Self-Improve 的各種方法，本質上都是把問題轉化成 evaluation function，然後讓 agent 最大化它。你的系統能改進到哪裡，取決於這個轉化做得多好。而做好這個轉化，需要的判斷力常常和解決原問題一樣難——只是沒有人給它一個顯眼的名字。
     [ Viewpoint ](/blog?tag=Viewpoint)  
### 
相關文章

[ViewpointAI 時代的 PM / HR / Sales：你才是讓 AI 落地的那個人2026-05-26](/blog/ai-for-non-engineer-workplace)[ViewpointAI 時代的非工程師：從今天開始，不需要準備好2026-05-26](/blog/ai-mindset-non-engineer)[ViewpointAI 時代的 Backend Engineer：從會用到能建的完整路線2026-05-26](/blog/backend-to-ai-engineer-roadmap)
