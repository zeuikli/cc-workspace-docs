---
url: "https://warmwater.dev/blog/agent-memory-identity-design"
title: "你的 Agent 為什麼漸漸不像自己了：固定知識與流動知識的設計邊界"
date: 2026-05-07
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  你的 Agent 為什麼漸漸不像自己了：固定知識與流動知識的設計邊界 
  2026-05-07 · — views      

Memory 系統的基本架構——Short-term、Long-term、Episodic 三層，以及各自的實作模式——我在[另一篇文章](/blog/llm-agent)裡整理過。這篇從另一個角度進來：不是「怎麼記」，而是「哪些應該固定，哪些應該流動，以及流動的部分怎麼設計讓它不腐爛」。


這個問題比架構選型更難，因為它是一個判斷問題，不是工程問題。


**讀完這篇，你會理解：**


- 為什麼 agent 的「個性漂移」是一種設計缺陷，而不是模型問題

- Identity 和 Memory 的根本區別，以及混淆它們的兩種代價

- 哪些知識值得存進 memory，哪些不值得

- 流動知識如何隨時間腐爛，以及怎麼設計清理機制


---


## Agent 為什麼漸漸不像自己了？


有一種問題在 production 上很難被發現：agent 的回答技術上沒有錯誤，但讀起來感覺「不太對」。風格變了，措辭變了，對某些問題的立場也變了。你沒有改過 prompt，模型版本也沒換，但 agent 已經漸漸不像你最初設計的那個 agent 了。


這種「個性漂移」通常有一個根源：identity 資訊沒有被固定在對的地方。


假設你的 agent 設計成「言簡意賅、不廢話」的風格，這個特質一開始是放在 system prompt 裡的。但某一次，使用者給了一條 feedback：「這個回答說得太清楚了，我很喜歡。」這條偏好被寫進了 memory。幾十個 session 之後，memory 裡累積了十幾條類似的「詳細解釋讓使用者滿意」的記錄，而你最初的「言簡意賅」設定已經在 context 裡被這些記憶稀釋掉了。


agent 沒有報錯。它只是漸漸變成了另一個 agent。
     哪些知識應該「固定」，哪些應該「流動」？      固定知識 Identity + Base Knowledge   SOUL.md / CLAUDE.md Agent 角色、人格、核心限制 — 每次 session 最高優先注入   Domain Rules 業務規則、永遠做 / 不做的事 — 由工程師明確設計，不自動更新   Behavioral Constraints 輸出格式、安全邊界 — 跨 session 不變，可被 prompt cache   設計時定義  跨 session 穩定  可被 cache    ↕  設計邊界      流動知識 Memory   User Preferences 用戶偏好、溝通習慣 — 從互動中累積，需定期驗證是否仍然有效   Past Failure Patterns 歷史踩過的坑 — 高價值，但 context 可能已改變，不能永久依賴   Domain Edge Cases 執行中發現的邊界條件 — 只存讓你意外的洞察，不存可再生成的事實   執行時累積  動態更新  需要清理    ⚠  Identity 洩漏進 Memory  → 被後續互動覆蓋 → Agent 個性漂移  ⚠  Context 固化進 Identity  → 無法根據新資訊調整 → 過度剛性  

---


## 固定知識的設計：Identity 與 Base Knowledge


固定知識是「你設計進去的東西」。它定義了 agent 是誰、在什麼 domain 工作、遵循什麼規則。這些東西不應該隨著對話累積而改變。


**SOUL.md 的設計邏輯**


在 hermes-agent 的架構裡，SOUL.md 是 system prompt 的第一個區塊，具有最高優先級。它定義的是 agent 的核心身份：角色、人格、tone、面對特定情況的處理原則。


設計 SOUL.md 的關鍵判斷是：這個東西如果改了，agent 的「本質」會不會跟著改？如果答案是「會」，它就屬於固定知識，應該放在 SOUL.md 或 system prompt，而不是任何動態注入的 memory 裡。


**System prompt 的結構設計**


system prompt 的結構可以分成兩部分：


- **穩定部分（Static）**：SOUL.md、Domain Rules、Behavioral Constraints。這部分字節級不變，Anthropic prompt cache 能命中，直接降低 token 成本。

- **動態注入部分（Dynamic）**：召回的 memory 內容、當前 session 的 context 檔案。這部分每次可能不同，不進 cache。


一個常見的設計錯誤是把動態部分放在 system prompt 最前面。這樣每次 context 不同，cache 前綴就會失效，所有後面的靜態內容都要重新計費。正確的順序是：靜態在前，動態注入在後。


**Domain Rules 的設計邏輯**


Domain Rules 記錄的是「這個 agent 永遠應該做什麼，以及永遠不應該做什麼」。它不是參考資料，而是行為邊界。


判斷一條規則屬不屬於 Domain Rules 的方式：這條規則如果放在 memory 裡，會不會因為某次對話的結果被蓋掉或被弱化？如果會，它就不應該放在 memory，而應該放在固定知識層。

---


## 流動知識的設計：Memory 應該記什麼


流動知識是「跑出來的東西」——從真實互動中累積的洞察。


**正向清單：什麼值得記**


- 使用者偏好（溝通風格、期望格式、明確說出來的喜好）

- 歷史失敗 pattern（這個 approach 在這個 domain 曾經失敗，要記住為什麼）

- Domain 邊界條件（在這個使用情境下，哪些假設不成立）


這三類有一個共同特點：它們是「讓你意外的洞察」——在設計階段想不到，只有在真實互動裡才能發現的東西。


**負向清單：什麼不值得記**


從 context engineering 的實踐裡整理出六類不應存進 memory 的內容：


類型原因程式碼模式、架構、檔案路徑可以從現有程式碼讀取，存了會過期Git 歷史、最近的變更`git log` 才是權威，不要複製它除錯解法或修復步驟修復已在程式碼裡，commit message 有 contextCLAUDE.md 或 rules 裡已有的內容重複儲存，沒有意義進行中的臨時任務這輪結束就過期，不要存PR 清單或活動摘要可以從 git 重新生成，只存讓你意外的那部分


這份清單的邏輯是：memory 的成本不只是儲存空間，而是每次 session 把它召回後佔用的 context token，以及過期記憶產生的干擾。存一條沒用的記憶，代價是在未來每次相關 session 裡付出 context 成本。

---


## 流動知識如何腐爛

     流動知識如何腐爛   記憶內容 狀態    User 偏好簡短的技術回答，不需要前言  新鮮 ✓ 仍然準確   報表避免圓餅圖（曾因此被退件）  新鮮 ✓ 仍然適用   User 在 Slack 工作，不用 email  老化 ~ 需要驗證   專案使用 Python 3.9，避免 3.11+ 語法  老化 ~ 已升版？   User 是初學者，需要詳細解釋基礎概念  過期 ✗ 已是資深   用 LangChain 0.x API 設計 agent 流程  過期 ✗ API 已變   新鮮  老化（需驗證）  過期（已錯誤）   輸出品質趨勢  高 低        記憶腐爛 → 輸出偏移    hygiene      ↗ 恢復  Session 1 Session 10 清理 S20  


流動知識的問題不是它會消失，而是它會過期卻繼續待在那裡。


**累積垃圾的幾個 pattern**


「User 是初學者」這條 memory 在 Session 2 寫進去的時候是準確的。但六個月後，這個 user 已經是資深工程師了，而那條 memory 還在。agent 還是用解釋基礎概念的方式回答，user 覺得被輕視，但不知道原因。


「用 LangChain 0.x API」這條 memory 在當時是正確的工程決策記錄。但 LangChain 升版之後，這條記憶開始指向錯誤的 API 設計，agent 給的建議開始出錯，也沒有報任何 error。


**Memory Fencing：隔離召回的記憶**


hermes-agent 在處理這個問題時用了一個叫 Memory Fencing 的設計：召回的記憶用 XML 標籤包住，讓模型清楚知道「這是我記得的事」和「使用者現在說的話」是兩件不同的事，避免語義污染。


這個設計背後的邏輯值得借鑑：召回的記憶不是 ground truth，它是一個帶著過期風險的「過去的觀察」。在使用它之前，要讓模型意識到這一點。


**腐爛的記憶怎麼連回品質漂移**


在[可觀測性那篇](/blog/llm-observability-design)提到的五個品質漂移來源裡，「Memory 累積垃圾」是其中一個。Tracing 能幫你看到 retrieval span 的相關性分數是否在下降，但如果你的 memory 設計沒有新鮮度機制，你只能在輸出品質已經明顯下降後才察覺。

---


## Memory Hygiene 的設計


知道記憶會腐爛之後，問題變成：怎麼在系統層面設計清理機制？


**新鮮度警告**


hermes-agent 的實作裡，超過一天的記憶會自動加上新鮮度警告：「This memory is 47 days old. Memories are point-in-time observations, not live state — verify against current code before asserting as fact.」


用「47 days ago」而不是 ISO 時間戳，是因為模型對相對時間的過期判斷比絕對時間更準確。


**清理觸發條件**


memory hygiene 不能靠人工定期審查，它需要系統性的觸發條件：


- **時間觸發**：超過 N 天的 memory 自動標記為「需驗證」

- **衝突觸發**：新的互動與舊的 memory 有明確矛盾時，觸發審查

- **主題觸發**：特定 domain 有重大變動（如 library 升版、組織架構調整），觸發相關 memory 的批量審查


**稽核的節點**


每次 agent 有重大環境變化時（model 升版、新的使用場景上線、工具 API 改變），都應該把 memory 做一次稽核，問一個問題：「這條記憶在新的 context 下還成立嗎？」


memory hygiene 的本質是：流動知識有它的生命週期，設計 memory 系統的同時，要設計它的退場機制。

---


## 還沒想清楚的幾件事


寫這篇的過程裡，有幾個問題一直在旁邊懸著，還沒有好的答案。


**Multi-agent 的記憶邊界**


當系統變成多個 agent 協作，一個自然的問題是：哪些記憶應該共享，哪些應該各自保有？


使用者偏好直覺上應該共享。但「這個 approach 曾經失敗」這類歷史記錄呢？共享了，agent B 可能因此放棄一個在它的情境下其實可行的路徑。不共享，整個系統可能在同一個坑裡跳兩次。


目前沒有一個清楚的原則可以切這條線，只是知道這條線需要被明確設計。


**主動決定不記某些事**


Hygiene 那節講的是記憶如何腐爛、如何清理。但還有另一個角度：主動決定不記。


比如使用者某次情緒很差，說了一些激烈的話。記下來，agent 之後可能永遠用小心翼翼的方式對待他，即使那只是偶發事件。不記，但如果他確實有某些長期的溝通敏感點，你就喪失了一個重要訊號。


「這條觀察值不值得變成記憶」這個判斷，目前大多是在 consolidation prompt 裡隱性決定的。我不確定這是對的地方，但也還沒找到更好的設計。


**Memory 是為了什麼？**


往後退一步，有個更根本的問題：設計 memory，到底是為了讓 agent 更有用，還是讓它更有連續性？


效用導向的 memory 邏輯很乾淨——記憶的成本對比它帶來的品質提升，低 ROI 的清掉，過期的標記。但這個框架處理不了「現在沒用，但記著是一種在乎」的東西。


如果 agent 是某種長期的工作夥伴，memory 的設計就不只是 context engineering，它還牽涉到一個更滑的問題：我們是否想讓使用者相信 agent 記得他們，而這種信任能不能被設計得真實，而不是表演？


hermes-agent 的設計選擇是偏向效用導向。不是因為連續性不重要，而是因為工程方式設計出來的「連續性感」，到底是在服務使用者，還是在製造一種有風險的錯覺，這個問題本身就沒有清楚的答案。


這個問題最終不是設計問題，是一個關於「我們希望 AI 系統在人的生活裡扮演什麼角色」的問題。比任何架構選型都更難。

---


## 延伸閱讀


- [你的 Agent 跑歪了你知道嗎？LLM Agentic System 可觀測性設計](/blog/llm-observability-design) — Memory 腐爛在可觀測性視角下的位置

- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — session 管理的四種策略與三種中斷狀態

- [Agentic Loop 的設計關卡：工具執行、錯誤分類與中斷機制](/blog/agentic-loop-design) — Loop 執行引擎的工程設計
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)
