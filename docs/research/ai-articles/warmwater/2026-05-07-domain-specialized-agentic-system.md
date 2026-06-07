---
url: "https://warmwater.dev/blog/domain-specialized-agentic-system"
title: "把領域判斷打包進 Agent：Production Agentic System 地圖"
date: 2026-05-07
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  把領域判斷打包進 Agent：Production Agentic System 地圖 
  2026-05-07 · — views      

有一段時間，我以為 agent 跑不好是模型問題。換了更強的模型，同樣的地方還是卡住。後來才意識到：模型能力不是瓶頸，問題是系統根本不懂我的業務。


這個差距的核心不在於模型選擇，而在於一個更根本的問題：**你的 domain understanding，有沒有真正進入系統？**


**讀完這篇，你會理解：**


- 為什麼 domain 深化是一個系統問題，不只是模型問題

- LLM 的 Jagged Intelligence 如何決定你要在哪一層投資

- Domain knowledge 可以住在哪些層次，各自解決什麼問題

- 為什麼可觀測性是改善的前提，而不是事後補的工具


這篇是一張地圖，不是教學。它的目的是讓你在開始設計之前，先看清楚地形。

---


## 你在對模型吼叫嗎？


Karpathy 在紅杉資本的演講裡有一個讓我反覆想的比喻：LLM 不是動物，是**鬼魂**（Ghost）。


動物有本能，會對情緒刺激反應。責罵牠、讚美牠，行為會改變。但 LLM 是統計模擬電路，你對它吼叫沒有意義。唯一能影響它的是 prompt、context，和你設計的執行環境。


這個比喻改變了我對「agent 跑不好」的診斷方式。


舊思維：output 不對，改 prompt，再試一次。以為情緒施壓有用，等同對 Ghost 吼叫。新思維：output 不對，先診斷環境缺少什麼，再修環境。焦點從「怎麼說」移到「給它看什麼、給它用什麼工具、給它什麼記憶」。
 ● 兩種心智模型    舊思維：對 Ghost 吼叫  
Prompt
改了又改  ↓ 
Model
LLM API call  ↓ 
Output
還是不對 → 回頭改 prompt   
Output 差 → 改 prompt → 再試
這是在對 Ghost 吼叫
    新思維：設計環境  
Environment
 Tools · Memory
  Skills · Identity
  Observability
  ↓ 
Model
在設計好的環境裡工作  ↓ 
Output
可預測、可改善   
Output 差 → 診斷環境缺什麼 → 修環境
   


這個思維轉移是 Harness Engineering 存在的原因。Harness 管的不是「模型輸出什麼」，而是「模型在什麼環境下工作」。工具、記憶、身份、技能，共同構成模型行動的基礎設施。


但 Harness Engineering 本身是通用的。讓一個 Agentic System 真正在你的 domain 上跑得好，還需要另一個問題的答案：**domain understanding 要從哪裡進來？**

---


## Jagged Intelligence：你的 Domain 在哪裡？


Karpathy 描述了 LLM 能力分佈的一個核心現象：**Jagged Intelligence**（鋸齒狀智力）。


LLM 的能力不是均勻分布的。在程式碼、數學、形式推理這類有明確 RL 訓練訊號的任務，能力飆升；在日常常識、特定垂直 domain 的專業判斷，能力可能急遽下降。原因是 LLM 能力由兩件事決定：「哪些任務有可驗證的 RL 訓練環境」加上「哪些資料剛好在預訓練語料裡」。數學可以驗證對錯，RL 獎勵訊號強；你的特定業務流程，可能根本不在語料裡。
 ● Jagged Intelligence：LLM 能力分佈 能力 ↑    Code &
Formal    Math &
Logic    General
Reasoning    Common
Sense    Your
Domain ?      
RL 訓練甜蜜點（可驗證訓練環境）
  
訓練訊號弱
  
你的 domain：取決於語料覆蓋
   **關鍵含義**：換更強的模型只是在整條鋸齒上移動，不改變鋸齒的形狀。
    你的 domain 落在哪個區間，決定你需要在哪一層投資——Model 層（fine-tuning/RL）還是 Harness 層就夠了。
 


這個現象對你的系統設計有直接的含義：**你的 domain 落在鋸齒的哪個位置，決定了你要在哪一層投資最多。**


如果你的 domain 剛好在訓練甜蜜點（有大量公開程式碼、文件、結構化資料），通用模型就有不錯的基礎，Harness 層的設計是主要工作。如果你的 domain 是高度垂直的專業判斷（特定法律條文解讀、特定行業的定價邏輯），通用模型在這裡的能力可能是低谷，需要在 Model 層動手。


這不是「換更強的模型」能解決的問題。換模型是在整條鋸齒上移動，但不改變鋸齒的形狀。

---


## Domain Knowledge 可以住在哪裡？四層知識地圖


讓一個 Agentic System「懂你的 domain」，可以在四個不同的層次發生，每一層編碼的是不同性質的知識，成本和效果也不同。


層次編碼什麼成本適合時機Model 層參數記憶（fine-tuning / RL）高Domain 不在訓練語料Knowledge 層靜態身份 + 動態檢索（RAG）低～中知識量大、動態更新Harness 層跨 session 累積（memory / skill）中長時間運行、任務重複Tool 層行動介面（domain-specific tools）中需要業務操作原語
 ● Domain Specialization Stack   可觀測性  Tracing Evaluation Cost Monitor 非確定性偵測      Layer 4 中等複雜度   Tool 層 Agent 在 domain 裡行動的介面。工具設計好壞直接決定 agent 能做什麼、做不到什麼。  Domain-specific tools API 封裝 業務操作原語    ↑    Layer 3 高彈性   Harness 層 讓 agent 跨 session 累積 domain 知識，管理任務執行的基礎設施。  Session Agentic Loop Memory Skill    ↑    Layer 2 低成本、快迭代   Knowledge / Base 層 靜態：告訴模型它是誰、domain 的基礎規則。動態：RAG 在 inference 時從外部知識庫按需檢索，注入 domain 文件、規範、案例。  SOUL.md System prompt Base memory RAG Vector Store Knowledge Base    ↑    Layer 1 高成本、高效果   Model 層 Domain 知識不在預訓練語料時才動。改變模型權重，讓 domain knowledge 直接進入參數記憶。  Fine-tuning RL Domain 語料    


**Layer 1：Model 層**


Fine-tuning 和 RL 在這裡發生。這是最底層的介入：直接改變模型權重，讓 domain knowledge 進入模型的參數記憶。


什麼時候需要？當你的 domain 知識不在預訓練語料裡，或需要模型輸出符合特定格式和風格，靠 prompt 無法穩定達到。代價是：需要高品質的 domain 資料、訓練基礎設施、對評估指標的清晰定義。Fine-tuning 做錯比不做更糟，壞的資料會讓模型在你的 domain 裡變笨。


RL 更激進：你在定義「什麼是對的」的獎勵訊號。如果你能明確定義 domain 裡的成功標準（可驗證的輸出），RL 可以讓模型在這個空間裡快速進化。


**Layer 2：Knowledge / Base 層**


這層分兩部分：靜態和動態。


靜態的部分是 SOUL.md、system prompt、base memory，用來告訴模型「它是誰、在什麼 domain 工作、有哪些永遠成立的業務規則」。成本最低、迭代最快，是最便宜的 domain 校準工具。hermes-agent 用 SOUL.md 定義 agent 身份、USER.md 存用戶偏好、base memory 注入環境事實，構成每個 session 啟動時的固定基底。


動態的部分是 RAG（Retrieval-Augmented Generation）。Domain 知識量太大、太動態，放不進 base memory，也不值得 fine-tune，但每次對話只需要其中一小塊。RAG 在 inference 時從外部知識庫（vector store）按需檢索，把相關的 domain 文件、規範、案例注入 context。


兩者解決的問題不同：靜態注入解決「這個 agent 是誰」，RAG 解決「這個任務需要知道什麼」。在生產系統裡，兩者通常同時存在。


**Layer 3：Harness 層**


Session、Loop、Memory、Skill 在這裡。這是整個系列大部分篇幅要討論的層次，也是彈性最大的一層。它不改變模型，只改變模型每一輪看到什麼、能做什麼、記住什麼。


Memory 讓 domain knowledge 跨 session 累積：這個客戶的偏好、上一次任務的結果、特定情境下哪些工具有用。Skill 更進一步：agent 完成一類任務後，把學到的工作流程結構化存下來，下次遇到類似任務自動載入。這是讓 agent 在你的 domain 裡越做越熟練的機制。


**Layer 4：Tool 層**


Domain-specific tools 是 agent 在你的 domain 裡行動的介面。一個通用 agent 有 `read_file`、`web_search`；一個金融 domain 的 agent 可能需要 `query_portfolio`、`check_compliance_rule`、`calculate_risk_exposure`。


Tool 設計是 domain 深化最直接的表現：你在定義「這個 agent 可以對這個 domain 做什麼操作」。工具設計得好，agent 能做到的事情是乘法；設計得差，再強的模型也會在工具的邊界上卡住。

---


## 為什麼可觀測性是 Domain 深化的前提？


四層知識地圖設計好了，不代表系統就能在 domain 上跑好。你還不知道它在哪裡出問題。


LLM 的可觀測性跟傳統系統不一樣。傳統系統出錯有明確的 exception、log 可以追；LLM 系統的問題是**漸進式的品質下降**：模型的回答開始偏離 domain 期望，不會拋出 error，也不會留下明確的失敗記錄。你需要在系統的每一層都有量測：


- **Tracing**：每一輪 LLM call 的 prompt、response、token 消耗、latency，要能追蹤到具體的 span

- **Evaluation**：量測輸出品質，不能只靠「感覺不對」，需要定義 domain 裡的評估標準

- **Cost**：哪些 session 消耗異常？哪個 tool 被重複呼叫？這些是系統行為異常的早期訊號


沒有可觀測性，你不知道問題出在 Model 層、Harness 層、還是 Tool 設計。改善變成了猜測。**可觀測性不是事後補的，它是 domain 深化的前提。**

---


## 這個系列涵蓋什麼，還缺什麼？


這篇是地圖。每一篇會選一個層次或橫切面拆解，以 hermes-agent 的實作為例，把抽象的設計決策轉換成具體的程式碼和工程判斷。
 ● 系列涵蓋範圍   可觀測性（橫切所有層）   LLM Observability 設計 Tracing · Evaluation · Cost 監控 · 非確定性偵測      Tool 層   Domain Tool 設計 業務操作原語設計 · 工具粒度決策 · 副作用與安全邊界      Harness 層   LLM Session 設計框架 四種連續性策略 · 三種中斷狀態   Agentic Loop 設計關卡 工具並行 · 錯誤分類 · 停止條件 · interrupt/steer   Memory 系統設計 三層記憶架構 · Identity 編碼 · Context 壓縮   Skill 與自我強化迴路 結構化工作流記憶 · 安全掃描 · 進化機制      Knowledge / Base 層   RAG 系統設計 Retrieval pipeline · Embedding 策略 · Vector Store · 檢索品質評估   Identity 與 Base Knowledge SOUL.md 設計 · System prompt 結構 · Domain 基礎規則編碼      Model 層   Fine-tuning + RL 的時機與方法 什麼時候需要動 Model 層 · 資料準備 · 評估指標設計 · RL 獎勵訊號    
這個知識地圖不一定完整。
你覺得有哪一塊是缺的，或你在自己的 domain 專案碰到的問題在這裡找不到位置？歡迎留言討論。
 


這個知識地圖不一定完整。我很好奇你覺得有沒有哪一塊是缺的，或是你在自己的 domain 專案裡碰到的問題，在這個地圖裡找不到位置的？歡迎留言一起討論。

---


## 延伸閱讀


- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — Harness 層的起點：session 管理的四種策略與三種中斷狀態

- [Agentic Loop 的設計關卡：工具執行、錯誤分類與中斷機制](/blog/agentic-loop-design) — Loop 執行引擎的工程設計：並行工具、錯誤分類、停止條件
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)
