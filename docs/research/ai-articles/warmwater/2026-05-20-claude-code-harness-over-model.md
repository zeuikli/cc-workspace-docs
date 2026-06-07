---
url: "https://warmwater.dev/blog/claude-code-harness-over-model"
title: "你在比的是模型，但決定 Claude Code 效果的是 Harness"
date: 2026-05-20
category: Viewpoint
source: warmwater.dev
---

[
← Viewpoint ](/blog?tag=Viewpoint)  Viewpoint 
 
# 你在比的是模型，但決定 Claude Code 效果的是 Harness
 
 2026-05-20 · — views  
  
  
大部分團隊在評估 AI coding 工具的時候，第一個動作是比 benchmark。GPT-4o vs Claude Sonnet，SWE-bench 分數，HumanEval 正確率。這個框架把問題簡化成「選哪個模型」。


但 Anthropic 在跨越百萬行 monorepo、十年以上遺留系統、橫跨數十個 repo 的微服務群部署 Claude Code 的觀察說的是另一件事：**在規模化部署裡，決定效果的不是模型，是 Harness。**


**讀完這篇，你會理解：**


- 為什麼 benchmark 跟你的 Claude Code 使用體驗之間有結構性落差
- Harness 的五個構成元件各自解決什麼，缺哪個會卡在哪裡
- 為什麼 Agentic Search 的設計讓 Harness 設置比 RAG 系統更關鍵


這篇不是教你怎麼設定 Claude Code，是說清楚為什麼 Harness 是這個問題的正確框架。


---


## Benchmark 衡量的不是你關心的那件事


SWE-bench 和 HumanEval 衡量的是模型在孤立程式碼問題上的表現——一個函式、一個 bug fix、一個演算法實作。這些任務的共同點是：context 完整、邊界清晰、評分自動化。


你的工作不是這樣的。你的問題分散在 15 個微服務裡、跨越 2008 年到現在的三代架構、有一套只有老員工知道的命名慣例、測試需要在特定 subdirectory 下才能跑。這些細節不在任何 benchmark 裡。


這個落差不是 benchmark 設計有問題，而是 AI coding 工具的問題從根本上是兩個不同的問題：一個是模型問題（推理能力），另一個是環境問題（在什麼 context 下工作）。Benchmark 衡量前者，你在日常開發裡碰到的瓶頸多半是後者。


---


## Claude Code 的 Harness 由哪五層構成


Harness 是讓模型知道如何在你的程式碼庫裡工作的整套執行生態。它有五個構成元件：


**CLAUDE.md** 是 Claude 每個 session 自動讀取的 context 文件。它告訴 Claude 這個 repo 的慣例是什麼、測試怎麼跑、哪些目錄是 generated code 不要動。沒有它，Claude 每次都是新人進場，不知道從哪裡開始。


**Hooks** 是在特定事件觸發的 script。最有價值的用途不是防止 Claude 做錯事，而是讓系統自我改善——stop hook 在 session 結束後記錄這次發現的 context，提出 CLAUDE.md 的更新建議；start hook 根據當前工作的 subdirectory 動態載入對應的知識。


**Skills** 是按需載入的專業知識包。一個大型 codebase 有幾十種任務類型，全部塞進 CLAUDE.md 會讓每個 session 都在消耗不相關的 context。Skills 解決的是「把對的知識在對的時機帶進來」：security review skill 在審查程式碼時載入，document update skill 在改動 code 後才出現，不工作的時候不佔空間。


**Plugins** 是打包 skills、hooks、MCP 設定的可安裝套件。它解決的是組織問題：一個人摸索出的好設定，怎麼讓整個團隊都用上，而不是只有他知道。


**MCP Servers** 是 Claude 連接外部系統的橋樑——內部文件、ticketing system、analytics platform、公司 API。它讓 Claude 能做到「不只是讀程式碼，還能查相關系統的狀態」。


這五個元件不是獨立功能，是有順序的層次：CLAUDE.md 先建立基礎 context，Hooks 讓這個 context 持續更新，Skills 在它之上加入按需專業知識，Plugins 把這個設定分發給整個團隊，MCP 把 Claude 的觸角延伸到程式碼之外。缺哪一層，不是少了功能，而是整個系統有明顯的漏洞。


---


## 為什麼 Agentic Search 讓 Harness 設計成為前提條件


大部分 RAG-based AI coding 工具的問題在於 index 跟不上開發速度。你 query 的時候，index 可能反映的是兩週前的狀態：一個已經改名的函式、一個上個 sprint 刪掉的 module，查詢結果沒有任何提示告訴你這些資訊已經過期。


Claude Code 採用的是 Agentic Search：像工程師一樣 traverse 檔案系統、讀文件、用 grep 精確找到需要的東西，從 live codebase 工作。沒有 embedding pipeline，沒有需要維護的中央 index，每個開發者的 instance 直接面對當前的程式碼。


|  | RAG-based 工具 | Claude Code（Agentic Search） |
| --- | --- | --- |
| 索引方式 | 預先 embedding，定期更新 | 即時 traverse 檔案系統 |
| 資料新鮮度 | 可能落後數天到數週 | 永遠是當前 live codebase |
| 對 Harness 的依賴 | 低（靠 index 補足 context） | 高（需要良好的起始 context） |
| 主要失效模式 | Index staleness | Context quality 不足 |


但這個設計有一個明確的代價：**它需要足夠的起始 context 才知道往哪裡找。** 在幾百萬行的 codebase 裡，如果問題描述模糊，Claude 不知道從哪個方向開始，搜尋範圍會迅速撐破 context window。


這讓 Harness 的設計從「便利功能」變成「能不能用」的前提條件。CLAUDE.md 告訴 Claude 這個 repo 的結構；LSP 整合讓 Claude 能用符號導航而不是字串 grep（在大型 codebase 裡，grep 一個常見函式名可能回傳幾千個結果，LSP 直接定位到正確符號）；`.ignore` 檔案排掉 generated code 和 build artifacts，讓搜尋不浪費在無關的雜訊上。


Agentic Search 把 RAG 的 staleness 問題解掉了，但把 context quality 的責任轉移到你身上。


---


## Harness 需要隨模型演進持續維護


Harness 不是設完就能一直用。CLAUDE.md 裡為了補償舊模型不足而寫的規則，在新模型上可能變成限制。一條「每次 refactor 只改一個檔案」的規則，當時可能是防止模型跑偏的保護，但在有能力做協調跨檔案編輯的新模型上，這條規則反而阻止它做得更好的事。Hooks 裡補償模型限制的邏輯，一旦那個限制消失，就從保護機制變成效能負擔。


每三到六個月做一次 Harness configuration review 是 Anthropic 的建議；更直接的信號是：在模型更新之後，如果效果感覺停滯，通常是 Harness 的設定跟不上了，而不是換模型能解決的問題。


---


> 
**ViewPoint**：你選哪個模型是公平競爭——所有人都能選同樣的模型。Harness 怎麼設計是你的工程工作，是可以真正拉開差距的地方。


---


## 參考資料


- [How Claude Code works in large codebases: best practices and where to start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) — Anthropic

  
  
 [ Viewpoint ](/blog?tag=Viewpoint)[ Harness Engineering ](/blog?tag=Harness%20Engineering) 
 

### 相關文章
[Viewpoint

AI 時代的 PM / HR / Sales：你才是讓 AI 落地的那個人

2026-05-26
](/blog/ai-for-non-engineer-workplace)[
Viewpoint

AI 時代的非工程師：從今天開始，不需要準備好

2026-05-26
](/blog/ai-mindset-non-engineer)[
Viewpoint

AI 時代的 Backend Engineer：從會用到能建的完整路線

2026-05-26
](/blog/backend-to-ai-engineer-roadmap)
