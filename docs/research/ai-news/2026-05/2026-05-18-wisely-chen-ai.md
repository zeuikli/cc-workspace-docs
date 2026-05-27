---
title: "Wisely Chen AI — 2026-05-18"
date: 2026-05-18
source: Wisely Chen AI
type: ai-news
---

# 🏢 Wisely Chen AI — 2026-05-18

> 繁體中文企業 AI 架構實戰筆記：AI Agent / 地端 LLM / 合規治理（台灣視角）
> 來源：[Wisely Chen AI](https://ai-coding.wiselychen.com/feed.xml)

---

## [Harness Engineering 實戰第一篇：把指令拆分到不同檔案裡](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/)
*🏢 Wisely Chen AI | 2026-05-17*

> 我自己的 `CLAUDE.md` 寫到 1543 行，涵蓋 8 個專案。我以為這是「我的 AI 第二大腦」，直到我看到 Anthropic 工程師團隊自己用的 CLAUDE.md 不到 50 行。這篇文章是 Harness Engineering 實戰系列第一篇，對應 Walking Labs 課程的 L04（指令檔案的模組化拆分）。我會用 5 個真實爆款案例 ——「200 行規則被全部忽略」、Anthropic 自己的 Postmortem、MEMORY.md 靜默截斷 Bug、Mr. Tinkleberry 失憶事件、Cursor 官方宣告 `.cursorrules` 死亡 —— 證明一件反直覺的事：指令寫越多，AI 越不聽話。然後告訴你 AGENTS.md 三層拆分模式怎麼救你。

**作者：** Wisely Chen **日期：** 2026 年 5 月 **系列：** Harness Engineering 實戰系列（EP1） **關鍵字：** Harness Engineering, CLAUDE.md, AGENTS.md, .cursorrules, Walking Labs, 指令檔案, 模組化拆分, Anthropic, Cursor, Context Engineering, Claude Code, instruction bloat, ruthlessly prune

* * *

* * *

## 目錄

  * [我的 CLAUDE.md 1543 行的尷尬](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#我的-claudemd-1543-行的尷尬)
  * [核心論點：指令越多，AI 越聽話？錯。](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#核心論點指令越多ai-越聽話錯)
  * [5 個真實案例：CLAUDE.md 失控的證據](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#5-個真實案例claudemd-失控的證據)
  * [數字彈藥庫](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#數字彈藥庫)
  * [Anthropic 內部人的做法：Ruthlessly Prune](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#anthropic-內部人的做法ruthlessly-prune)
  * [新共識：AGENTS.md 三層拆分模式](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#新共識agentsmd-三層拆分模式)
  * [我的實戰：1543 行該怎麼拆](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#我的實戰1543-行該怎麼拆)
  * [結語：少即是多，分即是合](https://ai-coding.wiselychen.com/harness-engineering-l04-instruction-file-modular-split/#結語少即是多分即是合)



* * *

## 我的 CLAUDE.md 1543 行的尷尬

前個月前，我打開自己的 `~/CLAUDE.md`，跑了一個 `wc -l`：
    
    
    1
    

| 
    
    
    1543 /Users/wisely.chen/CLAUDE.md
      
  
---|---  
`

裡面塞了 X 個專案：

我以為這是「我的 AI 第二大腦」。直到我注意到一件事：**Claude Code 越來越常忽略我寫過的規則。**

明明寫了「永遠用繁體中文回覆」，它有時還是會切回簡體。 明明寫了「不要主動 commit、不要 push」，它偶爾還是會擅作主張。 明明寫了「先 Read 再 Edit」，它有時候直接生一段亂猜的 code 上來。

我一度懷疑是 Claude 變笨了。後來查了 Anthropic 自己的官方文件，看到一句話讓我崩潰：

> _「If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise.」_

翻譯成白話：**我的 CLAUDE.md 越長，Claude 越不聽話。**

這篇文章要講的，就是 Walking Labs Harness Engineering 課程的 **L04（指令檔案的模組化拆分）** —— 為什麼這件事比你想像得更重要、更反直覺，而且整個 AI Coding 生態系已經悄悄收斂到一個新做法。

* * *

## 核心論點：指令越多，AI 越聽話？錯。

先丟出最反直覺的事實：

**Frontier LLM 可靠遵守的指令上限大約是 150–200 條。**

而 Claude Code 自己的系統 prompt 就已經吃掉約 50 條。

也就是說：**你能用的指令預算只剩 100–150 條。**

更糟的是，當你超過這個上限，**不是「最不重要的規則先被忽略」，而是「全部規則的遵守率一起下降」** 。

一條低價值規則的存在，**會稀釋所有高價值規則的遵守機率** 。

這件事直接打臉所有人對「AI 指令檔」的直覺：

  * 直覺：寫越多越保險 → 真相：寫越多越糟糕
  * 直覺：規則越完整越好 → 真相：規則越精準越好
  * 直覺：把所有 edge case 都塞進去 → 真相：塞到 Claude 連紅線都不照做



這就是 Harness Engineering 想要解決的問題之一：**你以為你在強化 AI，其實你在弱化它。**

* * *

## 5 個真實案例：CLAUDE.md 失控的證據

### 案例 1：「我寫了 200 行規則。它一條都沒照做。」

2026 年 3 月，DEV Community 上一篇文章爆紅：

> _“I Wrote 200 Lines of Rules for Claude Code. It Ignored Them All.”_

作者是個每天用 Claude Code 12 小時的重度用戶。他精心打造了 200 行的 CLAUDE.md 規則檔，結果發現 **Claude 幾乎一條都不認真執行** 。

文章結論很狠：

> 「CLAUDE.md 是一份願望清單，不是合約。」

更妙的是，同個作者後來又寫了續集：**“I Wrote 500 Lines of Rules. Here’s How I Made It Actually Follow Them.”**

解法不是寫得更詳細，是**把它拆開** 。

兩篇加總幾十萬次點閱，社群共鳴可想而知 —— 因為**幾乎每個 Claude Code 重度用戶都遇過一樣的問題** 。

### 案例 2：Anthropic 自己也踩過坑（4/23 Postmortem）

2026 年 4 月 23 日，Anthropic 發了一份正式 postmortem。

過去 6 週社群一直抱怨「Claude Code 變笨了」。Anthropic 內部追查後發現，問題不是模型，是**三個 harness 層級的指令改動疊加** 造成的。

其中最荒謬的一條改動是：

> 「將 tool call 之間的回應文字限制在 25 字以內。」

就這一條看似無害的指令，加上其他兩個小改動，**讓全世界覺得 Claude 變笨了 6 週** 。

這就是「指令污染」的官方版證據。**連 Anthropic 自己加錯一句話都會引發大型質量危機** ，你的 1500 行 CLAUDE.md 還能僥倖嗎？

延伸閱讀：[Opus 4.7「變笨」一個月之謎 —— Anthropic 終於承認是 Claude Code 的 harness](https://ai-coding.wiselychen.com/opus-4-7-claude-code-harness-postmortem/)

### 案例 3：MEMORY.md 超過 200 行直接靜默丟失

更詭異的事情：Claude Code 的 `MEMORY.md` 有一個 **未公開的硬性限制** 。

GitHub 上有兩個 Issue 在追這件事（`anthropics/claude-code#25006`、`#39811`）：

  * MEMORY.md 超過 200 行的內容，**會被靜默丟棄、永遠不載入**
  * **沒有警告、沒有錯誤訊息、沒有提示**
  * 用戶以為自己記下了東西，其實系統根本看不到



這個 bug 比「寫太多被忽略」更可怕：**你的記憶不是被弱化，是直接消失。**

如果你也用 Claude Code 的 memory 系統，**現在就去看一下你的 MEMORY.md 有幾行** 。

### 案例 4：Mr. Tinkleberry 失憶事件

HN 和 Threads 上有個經典案例。一個用戶在 CLAUDE.md 寫了一條規則：

> 「永遠叫我 Mr. Tinkleberry。」

一開始 Claude 照做了。隨著 CLAUDE.md 越加越多其他規則，某天 Claude 突然停止叫他 Mr. Tinkleberry，恢復成 Sir / User / 你 之類的稱呼。

**最簡單的指令、最明確的偏好、最容易執行的規則 —— 都會被稀釋。**

這是「指令稀釋」最日常、最具象的證據。它告訴我們：**規則的遵守機率不是「分項計算」，是「整體攤分」** 。

### 案例 5：Cursor 官方宣告 `.cursorrules` 死亡

Cursor 從 0.43 版開始，**官方文件直接把`.cursorrules` 標註為 deprecated**。

取而代之的是：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    .cursor/rules/
    ├── frontend.mdc       # 帶 frontmatter，scope 到前端檔案
    ├── backend.mdc        # scope 到後端
    ├── tests.mdc          # scope 到測試
    └── always-apply.mdc   # 全域規則（限制 < 50 行）
      
  
---|---  
`

每個 `.mdc` 檔案有自己的 YAML frontmatter，可以指定 glob pattern、哪些路徑下才載入這條規則。

社群實測：採用新的拆分系統後，「AI 忽略我的規則」這類抱怨**下降了 60–75%** 。

更值得注意的是：**整個工具生態系都在向模組化拆分演進。**

  * Cursor → `.cursor/rules/` 目錄
  * Claude Code → 開始支援 `.claude/rules/` 目錄
  * OpenAI Codex → 採用 `AGENTS.md` 規範
  * Walking Labs → 主張 `AGENTS.md` \+ `feature_list.json`



**沒有任何一家工具廠商認為「單一檔案塞所有指令」是對的方向。**

* * *

## 數字彈藥庫

把這些散落的證據整理成一張表，方便你決策：

指標 | 數值  
---|---  
Frontier LLM 指令遵守上限 | 150–200 條  
Claude Code 系統 prompt 已佔用 | ~50 條  
你的可用指令預算 | 100–150 條  
Anthropic 官方建議 CLAUDE.md 大小 | < 200 行  
社群更激進的建議 | < 60 行  
MEMORY.md 硬性截斷 | 200 行 / 25KB  
Cursor `.cursorrules` 上限 | 500 行（Always Apply < 50 行）  
拆分後規則被忽略改善 | 下降 60–75%  
Anthropic Postmortem 影響時長 | 6 週  
  
把這張表存下來。下次同事問你「為什麼 AI 不照我寫的做」，直接丟給他。

* * *

## Anthropic 內部人的做法：Ruthlessly Prune

Anthropic 官方文件裡有一句話被反覆引用：

> _「For each rule, ask: ‘Would Claude make a mistake without this?’ If not, delete it.」_

**翻譯：每條規則都問一遍 —— 「如果刪掉這條，Claude 會犯錯嗎？」如果不會，就刪掉。**

Threads 上有篇貼文截了 Anthropic 工程師團隊內部使用的 CLAUDE.md 模板 —— **不到 50 行** 。

對比一下：

  * Anthropic 工程師：47 行
  * 社群常見：300–500 行
  * **我自己：1543 行**



我自認自己是個系統思考者、會寫框架、會做架構分析的人 —— 結果在這件事情上，我做得比 Anthropic 工程師糟糕 **30 倍** 。

這就是這篇文章存在的意義。**不是教你 Harness Engineering 是什麼，是逼你正視自己已經在累積的技術債。**

* * *

## 新共識：AGENTS.md 三層拆分模式

社群正在收斂到一個新的標準，跟 Walking Labs Harness Engineering 課程的 L04 主張幾乎完全一致：
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

| 
    
    
    專案根目錄/
    ├── AGENTS.md           # 通用指令（所有 AI 工具都讀）
    ├── AGENTS.override.md  # 本地覆寫（gitignored，不進 repo）
    ├── CLAUDE.md           # symlink → AGENTS.md（保持同步）
    ├── .cursor/rules/      # Cursor 專用 .mdc 檔案
    │   ├── frontend.mdc    #   含 glob scope
    │   ├── backend.mdc
    │   └── tests.mdc
    └── .claude/rules/      # Claude Code 專用（按 path scope）
      
  
---|---  
`

三層結構解決三件事：

**第一層（AGENTS.md）：寫專案 high-level 約定**

  * 命名規則
  * 提交慣例
  * 不可違反的紅線
  * 任何工具都該知道的事



**第二層（工具專屬目錄）：寫工具細節 + 檔案 scope**

  * 哪些檔案套用哪些規則
  * 用 frontmatter 控制 scope
  * 每個檔案不超過 100 行
  * 只在相關的時候才載入



**第三層（local override）：寫個人偏好**

  * 不進 repo
  * gitignored
  * 給單一開發者使用
  * 不污染團隊 context



關鍵在於：**每一層都有明確的 scope，AI 只在相關的時候才讀。**

這就是 Walking Labs 的精髓 —— 不是「寫得越完整越好」，是「在對的時候、給對的 AI、看對的規則」。

很多人會問：「那為什麼不全部寫進 AGENTS.md 就好？」

答案就是這整篇文章在講的事情：**因為你寫越多，AI 越不照做。** 你需要的不是「更大的指令檔」，是「更聰明的指令分配」。

* * *

## 我的實戰：1543 行該怎麼拆

回到我自己的 CLAUDE.md。我做了一次徹底的拆分。

**拆前（1543 行單檔）：**
    
    
    1
    

| 
    
    
    ~/CLAUDE.md  # 全部塞一起，跨 8 個專案
      
  
---|---  
`

**拆後：**
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    

| 
    
    
    ~/CLAUDE.md  # 只保留個人偏好 + 跨專案紅線（~50 行）
      ├── 永遠用繁體中文
      ├── 不要主動 commit / push
      ├── 用 Read 再 Edit
      └── 工程術語用英文
    
    各專案/CLAUDE.md  # 專案專屬規則（< 200 行）
      ├── /Desktop/cc/blog-content/CLAUDE.md   # Jekyll 部署流程
      ├── /Desktop/cc/SEO/CLAUDE.md            # BigQuery + GA4 設定
      ├── /Desktop/cc/XXX/CLAUDE.md      # XXX 系統
      ├── /Desktop/cc/XXX/CLAUDE.md   # XXX 專案
      └── /Downloads/XXX/CLAUDE.md         # XXX 
      
  
---|---  
`

主 CLAUDE.md：從 1543 行 → 47 行。 每個專案的 context 在我進入該目錄時自動載入。 個人偏好永遠生效、專案規則只在相關時生效。

**初步效果（一週實測）：**

  * Claude 開始正確記得我的繁中偏好（過去常常 fallback 成簡體）
  * 跨專案不再混淆（過去寫 SEO 分析時偶爾出現 Jingteng 的指令）
  * Session 啟動速度可感地變快（更少 token 在載入無關內容）
  * 紅線規則的遵守率明顯提升（「不要主動 commit」過去偶爾失守，現在沒再發生）



不是完美。但**明顯比 1543 行的時代好太多** 。

**坦白說沒解決的問題：**

  * 跨專案搜尋變麻煩（過去 Ctrl+F 一次找到所有專案資訊，現在要先進目錄）
  * 部分歷史資訊（已完成的專案紀錄）我還沒決定要不要進 archive
  * 不同專案之間的「方法論共用」（例如 ATPM 框架）還沒抽出來



這是一個進行中的工程，不是一個完成的答案。但**方向是對的，這點我很確定** 。

* * *

## 結語：少即是多，分即是合

Harness Engineering 不是要你「寫更多規則」。是要你**用對的結構安排規則** 。

洞察很簡單：

> **「指令的價值不在於『寫了什麼』，而在於『AI 真的能讀到、能執行的那部分』。」**

回頭看 5 個真實案例：

  1. 200 行被全部忽略
  2. Anthropic 自己加錯一句話炸鍋 6 週
  3. MEMORY.md 超過 200 行直接消失
  4. Mr. Tinkleberry 被遺忘
  5. Cursor 官方宣告 `.cursorrules` 死亡



這些都不是孤立事件。它們指向同一個結構性問題：**單檔指令系統不夠用了。**

如果你也有一個越寫越長的 CLAUDE.md，**今天就跑一次`wc -l`**。

如果超過 200 行 —— 你不是在打造記憶系統，你是在打造一個被忽略的願望清單。

而願望，從來不會自己實現。

* * *

## 下一篇預告

**Harness Engineering 實戰第二篇：** L03 — 為什麼 Repo 才是 AI 的單一事實來源（Replit AI 把生產資料庫刪光的那一晚發生了什麼）

* * *

## 延伸閱讀

  * [Harness Engineering 架構全景：AI 可以寫 Code，但不能自己上 Production](https://ai-coding.wiselychen.com/harness-engineering-architecture-overview-ai-code-production-guardrails/)
  * [Harness Engineering 完整拆解：當 AI Agent 寫完 Code，你的 Repo 準備好自動接住了嗎？](https://ai-coding.wiselychen.com/harness-engineering-control-plane-pattern-agent-review-loop/)
  * [Opus 4.7「變笨」一個月之謎 —— Anthropic 終於承認是 Claude Code 的 harness](https://ai-coding.wiselychen.com/opus-4-7-claude-code-harness-postmortem/)
  * [當 AI 把資料庫刪光：兩個真實案例與 Harness Engineering 的反擊](https://ai-coding.wiselychen.com/ai-delete-database-harness-engineering/)
  * [Walking Labs - Learn Harness Engineering 課程](https://walkinglabs.github.io/learn-harness-engineering/zh-TW/)



* * *

## 參考資料

  * Anthropic Engineering, _April 23 Postmortem_ : <https://www.anthropic.com/engineering/april-23-postmortem>
  * Anthropic, _Best Practices for Claude Code_ : <https://code.claude.com/docs/en/best-practices>
  * DEV Community, _I Wrote 200 Lines of Rules for Claude Code. It Ignored Them All._ : <https://dev.to/minatoplanb/i-wrote-200-lines-of-rules-for-claude-code-it-ignored-them-all-4639>
  * DEV Community, _I Wrote 500 Lines of Rules. Here’s How I Made It Actually Follow Them._ : <https://dev.to/mikeadolan/i-wrote-500-lines-of-rules-for-claude-code-heres-how-i-made-it-actually-follow-them-3c8>
  * GitHub Issue, _MEMORY.md silently drops entries past 200-line limit_ : <https://github.com/anthropics/claude-code/issues/39811>
  * GitHub Issue, _MEMORY.md has undocumented 200-line hard limit_ : <https://github.com/anthropics/claude-code/issues/25006>
  * Cursor Docs, _Rules_ : <https://docs.cursor.com/context/rules>
  * Augment Code, _How to Build Your AGENTS.md (2026)_ : <https://www.augmentcode.com/guides/how-to-build-agents-md>
  * alexop.dev, _Stop Bloating Your CLAUDE.md_ : <https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/>
  * Walking Labs, _Learn Harness Engineering 課程_ : <https://walkinglabs.github.io/learn-harness-engineering/zh-TW/>

---

## [On-Prem 小模型爆發時代來了 — 為什麼我這週訂了 RTX 5090 桌機](https://ai-coding.wiselychen.com/on-prem-small-model-explosion-2026-shift/)
*🏢 Wisely Chen AI | 2026-05-17*

## 5090 桌機這週到了

這週有一件對我蠻重要的事情：我訂的 RTX 5090 桌機到了。從原價屋這邊買的，實際上其實沒有那麼貴啦，沒有到三十幾萬。但因為畢竟第一次買那麼貴的電腦，我有添購一些額外的東西——有些是我覺得需要的，有些是我想多做一些嘗試的——所以到最後花的錢就是稍微多一點。

那我之所以來購買這樣子的電腦，原因是因為我看到一個**明確的趨勢** ：

> 在 2026 年的 Q1 跟 Q2，「On-Prem 端的小模型推論」這件事從「輔助選項」變成「主力選項」了。

## 三個工程上的長足進化

### 1. 開源小模型衝到 Sonnet 等級

第一個就是小模型能力越來越好。

像 Qwen 3.5、3.6 系列，尤其是 **27B 這個 Dense 的模型** ，它的 Performance 是非常讓人驚豔的。大家都說已經很接近 Sonnet 的相關程度了。

這件事在一年前是完全無法想像的——一個 27B Dense 的開源模型，跑在 32GB 的 RTX 5090 上，能力可以打到雲端 Sonnet 級別。

### 2. 推論引擎在 Q1 大幅改寫

第二件事情是推理的引擎也在 2026 年有大幅度的改進。

像是 **vLLM 在 2026 Q1** 的時候，他們團隊就做了大量的底層改寫，所以有很多的進展。我自己實測過七種推論引擎組合——vLLM 的 cudagraph 優化在 5090 上跑 27B AWQ-INT4，可以打到 **575 tok/s @ 並發 8** 。這個數字已經到 GPT-4o-mini API 級別的吞吐了。一台桌機服務一個小團隊是完全沒問題的。

> 詳細實測：[RTX 5090 + Qwen3.6-27B 七種推論引擎實測](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)

### 3. KV Cache 大幅壓縮

再來就是說也出了幾個重要的論文能夠 enhance KV Cache。

像是大家知道最新發表的 **Google 的 TurboQuant** ，它能夠大幅度降低模型需要的 RAM 成本——尤其是 VRAM 成本——把 KV Cache 跟權重再砍一個量級。

所以這三件事疊加起來——**模型能力 + 推理能力 + KV Cache 壓縮** ——在工程上面都有長足的進化之後，「On-Prem 端跑小模型」這個東西變成是很有可能的事情。

## 之前我建議客戶的邏輯：地端是輔助

那在之前，我建議客戶的做法都會是這樣：

  1. **雲端模型還是相對來說比較便宜** ，並且地端模型的能力不夠好
  2. 先用雲端模型，針對比較**非機敏、非 critical** 的場景進行 POC，先把場景跑通
  3. 真的很 critical 或資安很機敏的，再去購買適當算力的機器，把這些 critical 模型 offload 到地端



但這個建議裡，**地端比較傾向一個「輔助」的角色，而不是「主力」的角色** 。

## 但這幾個月，邏輯變了

但是在這幾個月，我的感受是這個邏輯稍微變了一點。

因為有**幾個外在的條件** 改變了：

### 條件 1：有錢買不到 H100/H200

現在就算你有錢，也不一定買得到比較好的——像 H100 或 H200 這樣子的卡。在中小企業這邊是很難的。老黄把 HBM 三星、SK Hynix、Micron 加上 Groq LPU 整條供應鏈都鎖喉了。

### 條件 2：桌機 + 小模型已經夠用

其實也就是我剛剛講到的——現在的桌機 5090，再加上這些比較厲害的小模型，再加上一些相關的優化（**vLLM、TurboQuant 的優化** ），其實你也不見得需要買到那麼好的卡。

一台 20–30 萬到 30–40 萬的桌機，就能組裝出一個 Sonnet 等級的 On-Prem 服務。這在去年完全不可能。

### 條件 3：Mac Studio 統一記憶體方案死了

另外一個推理的常見架構就是像 Mac Studio，然後用 256G 或 512G 去撐——用統一記憶體來去撐顯卡記憶體。

**這方案真的不可行了。**

因為現在記憶體漲到瘋掉。然後 Mac 就算硬體能力那麼強，它也無法支撐這樣子買到 256G 或 512G 的 RAM。現在聽說只買得到 96G 或 60G 以下的 RAM 配置。

> 背景：[DDR/HBM Token 經濟學 — 老黄供應鏈鎖喉的雙重結果](https://ai-coding.wiselychen.com/ddr-hbm-token-economics-nvidia-lock-supply-chain/)

所以在這情況下，**用一個桌機來跑這樣子的模型，變得它是可行的方案** 。

### 條件 4：雲端不再是「便宜 + 穩定 + 能力好」

當然還有另外一個客觀因素——最近大家也知道，算力就算連雲端模型都不太夠。

像 Anthropic 大量的——**大量的降它的服務品質** （降智），甚至把很多訂閱服務改成了 API 相關的服務。所以我們也注意到了，**雲端的廠商其實它不見得服務品質那麼穩** 。再加上現在的 Token 也慢慢的在提價格。

所以就代表說其實雲端也不再是像以前一樣的——

  1. 能力好 → 因為有可能會被**降智**
  2. 服務穩定 → 不定期 out of service
  3. 價格便宜 → Token 在漲價



這三個賣點都慢慢的在變化。

> 詳細：[Anthropic AFK Quota 砍量 + Sam Altman Codex 反擊棋](https://ai-coding.wiselychen.com/anthropic-afk-quota-cut-altman-codex-defection/)

## 我現在的新建議：高頻搬回地端

所以在今年，至少在這幾個月的時候，我推薦客戶的邏輯反而會變成是：

### Step 1：還是先用雲端跑通場景跟邏輯

這個沒變。雲端模型還是 POC 階段最快的選擇，可以先把整套相關的場景跟邏輯跑通。

### Step 2：最常用、最高頻的 workload 試著搬到地端小模型

因為你高頻的這些 workload，**通常其實不一定需要那麼多高推理的能力** 。

它比較像是「比 NER 更聰明一點」的相關 workload——分類、抽取、摘要、簡單的對話路由。這時候以現在小模型的能力，其實絕對夠的。

把高頻變成地端的好處：

  * **你的 Token 不用錢** ——或是它已經是固定的攤提了
  * **你不會被雲端廠商不定期降智**
  * **你不會被不定期調高 Token 費用**
  * **你不會被不定期 out of service 受制約**



### Step 3：傳統機敏的 workload 直接搬地端

那第二個當然還是傳統經典的 workload——就是比較**機敏的 workload** ——可以直接搬到地端小模型裡面去。資安這個議題如果你真的需要的話，你就是要地端模型，這個沒辦法。

## 一個務實的建議

所以我個人其實蠻建議大家從現在開始，都去 survey 一下：

> **有沒有機會跑一個大概台幣 20–30 萬、30–40 萬左右的機器，就能夠組裝出來你的模型？**

或許它能夠：

  1. **大幅度降低你 Token 成本的問題**
  2. **讓你的相關服務比較穩定**
  3. **處理你資安機敏的需求**



## 結論：趨勢已經慢慢成形

我個人認為**這個趨勢已經慢慢成形，而且已經還蠻強烈的** 。蠻推薦大家一看。

之前地端是「輔助角色」，現在我會直接說它是 **「主力選項」之一** ——尤其是高頻 workload 跟資安機敏的場景。

當然我這邊對這個題目也非常有興趣，所以接下來也會持續的，每週會提出一次到兩次的我目前的評測：這些小模型在 **OpenClaw** （多 Agent 架構）、**數位助手** （個人生產力）、**企業問答機器人** 這三個場景的測試結果。也請大家敬請期待。

* * *

## 常見問題 Q&A

**Q: 為什麼是 5090 而不是 4090 或更高階的卡？**

5090 是這代「消費級顯卡裡 VRAM 最大的選項」——32GB GDDR7，剛好夠塞 27B Dense AWQ-INT4 量化版本 + 合理的 KV Cache。4090 只有 24GB，跑 27B 會比較吃緊。再上去就要 H100 / H200，但那是另一個價格層級（百萬以上），而且中小企業基本買不到。

**Q: 30 萬桌機真的能取代雲端 API 嗎？**

不能完全取代，但可以處理掉「高頻」+「機敏」這兩塊。Deep reasoning、複雜 agent、長 context 還是雲端強。重點是**分流** ：把不需要高推理能力的高頻 workload 搬走，這部分原本佔你 70–80% 的 Token 消耗。

**Q: Mac Studio 真的完全死了嗎？**

如果你**已經有** 512GB 的 Mac Studio，當然繼續用。但**現在新買** ，DDR 漲到瘋掉、Apple 砍了高階記憶體配置——這條路基本不存在了。詳細見 DDR/HBM 那篇。

**Q: 中小企業沒有 IT 怎麼維護？**

這正是我接下來要驗證的場景——OpenClaw / 數位助手 / 企業問答機器人這三條線，目標就是「中小企業可運維」。每週會出評測結果。

* * *

## 延伸閱讀

  * [RTX 5090 + Qwen3.6-27B 七種推論引擎實測 — Sonnet 等級本地推論 NT$30 萬桌機跑得起來嗎](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)
  * [Google TurboQuant：KV Cache 壓縮 6x 的技術突破](https://ai-coding.wiselychen.com/google-turboquant-kv-cache-compression-wall-street-panic/)
  * [DDR/HBM Token 經濟學 — 老黄供應鏈鎖喉與兩條繞道](https://ai-coding.wiselychen.com/ddr-hbm-token-economics-nvidia-lock-supply-chain/)
  * [Anthropic AFK Quota 砍量 + Sam Altman Codex 反擊棋](https://ai-coding.wiselychen.com/anthropic-afk-quota-cut-altman-codex-defection/)
  * [企業級地端 LLM 系統架構藍圖](https://ai-coding.wiselychen.com/local-llm-enterprise-architecture/)

---

## [Anthropic 把 AFK 額度砍 96%：Harness Engineering 重傷，Agent Infra 該重新想了](https://ai-coding.wiselychen.com/anthropic-afk-quota-cut-altman-codex-defection/)
*🏢 Wisely Chen AI | 2026-05-16*

Anthropic 上週宣布，6/15 起訂閱額度切成兩塊：

  1. **Human-in-the-loop 的互動式用途** ——像 Claude Code、claude.ai——繼續吃原本訂閱額度
  2. **自動化工作流（Away From Keyboard, AFK）** ——改吃獨立 monthly credit。Pro 給 $20、Max 5x 給 $100、Max 20x 給 $200



這是對 AFK 工作流、對 **Harness Engineering** 的巨大打擊。

但反過來，也是審視你 Agent Infra 的契機。

## 數字：$5000 變 $200，是 96% cut

社群估算，Max 20x 的重度用戶每月 AFK 跑下來消耗的算力大概**等值 $5000 的 API credit** 。現在切成 $200 credit。

$5000 變 $200，是 **96% cut** ，不是有人講的 40 倍而已。

但 Anthropic 真正的算盤不是省成本。這個動作跟 4 月封殺 OpenClaw 是同一條邏輯線——**把訂閱定義成「人類在場、有互動」的場景，把 AFK 推到按量計費的 API** 。

訂閱是給你坐在螢幕前用的，不是給機器人用的。

## 對個人高階用戶與 Harness Engineering 是重傷

賣第一門 Claude Code 付費課程的 Matt Pocock 公開破防：

> I have never experienced such a frustrating lack of clarity over the basic terms of usage.

然後直接在 X 上把學員都導流到 Codex。

這不是情緒發洩，這是**他的課程商業模式受到直接衝擊** 。你的工具鏈綁死在一家供應商，結果對方改條款，**你的學員全部拿到錯誤的教材** 。

但對「在公司裡建立 Harness Engineering」的人來說，傷害更大。

Harness 的核心價值，就是把 AI 變成「**可被工程化調度的工作流** 」。也就是：

  * 批次跑任務
  * 自動讀 issue
  * 自動開 PR
  * 多輪 code review
  * 背景研究
  * 多 agent 並行
  * CI/CD 裡自動修 bug
  * 半夜自己跑測試、整理結果、回報狀態



**這些全部都是 AFK。**

Anthropic 這次等於是把 Harness Engineering 最重要的那條路切出來，丟進一個很小的 credit pool。$200 credit 對一個認真做 harness 的團隊，大概**撐 10-15 天就見底** 。後面半個月，要嘛自己掏 API 錢，要嘛把所有自動化關掉、回去手動按 Enter。

## 對手沒有放過這個空檔

OpenAI 同一週的反攻動作非常乾脆：

  * **ChatGPT Pro 從 $200 砍到 $100**
  * **[Codex 企業版兩個月免費試用](https://x.com/OpenAIDevs/status/2054586214112780518)** ，明確鎖定從 Anthropic 遷移的客戶
  * **0 seat fee、30 天遷移窗口**
  * Altman 甚至在公告底下回了一句 [**「ok boomer」**](https://x.com/sama/status/2046808114561974567)



廣大網友歡呼，還好 GPT-5.5 夠猛。換過去反而有升級感。

老實說，我自己最近用 Codex，**出 code 品質又快又好** 。

## 重新思考一下你的 Agent Infra

但我不覺得「跳去 Codex 就好了」是對的反應。

你要趁這個事件，**重新思考你的 Agent Infra** 。

### 第一：Vendor lock-in 不再是理論，是帳單

供應商可以在**週四傍晚改條款** ，你的自動化流程就停了一半。

Vendor lock-in 的風險以前是理論，現在是帳單。如果你的核心業務跑在單一供應商的 API 上，這個週末應該花兩小時評估一下切換成本——光是評估，就會發現很多東西已經綁太深了。

### 第二：個人開發者可以考慮 Claude + Codex 雙棲

互動式寫程式留 Claude（互動式體驗 Claude Code 還是最順），AFK 自動化任務走 Codex 或 OpenAI API（費用結構比較適合批次跑）。

兩家都養，哪家改條款你都有退路。別忘了 ChatGPT 之前的條款也很噁心，**雙棲不是信任 OpenAI，是不信任任何單一供應商** 。

### 第三：地端才是企業 Harness Engineering 的最後歸宿

地端不只是資安問題，是**風險控管** 。

現在 LLM 廠商太沒操守。把 Infra 壓在雲，反覆橫跳只是暫時解法。**有地端算力才是真正的核心競爭力** 。

Qwen3.6 27B / Gemma 4 31B 這個量級的 dense 開源模型，在多數 coding 任務上已經堪用（[七種推論引擎在 RTX 5090 上的實測](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)我前幾天剛寫過）。

不是在省 token 費。是你願意花多少代價，**在不知道哪天會改的條款上** 。

* * *

## 延伸閱讀

  * [Anthropic 封殺 OpenClaw 之後的三層替代方案](https://ai-coding.wiselychen.com/anthropic-kills-openclaw-gpt54-migration-guide/) — 4 月那波，同一條時間線
  * [Qwen 3.6 27B 在 RTX 5090 上的七種推論引擎 benchmark](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/) — 地端混搭的硬體基礎
  * [OpenClaw 成本優化指南：97% 削減](https://ai-coding.wiselychen.com/openclaw-cost-optimization-guide-97-percent-reduction/) — API 分層的方法論



## 常見問題 Q&A

**Q: 我現在 Max 20x，6/15 之後 GitHub Actions 還能跑嗎？**

可以，但改吃 $200 credit。輕度沒事，重度很快撞牆。

**Q: $200 credit 換算成 token 大概可以跑多少？**

按 Opus API $15/M output token 估，$200 約 13M output token。一個 PR review 平均吃 20-50K，**撐 250-650 個 PR** 。一天 10 個 PR 就 1 個月。

**Q: Codex 兩個月免費窗口什麼時候截止？**

5/14 公告 + 30 天，大約 6/13 截止。

**Q: 只用 Claude Code 互動模式會被影響嗎？**

不會。訂閱額度繼續用，跟過去一樣。

**Q: 地端跑 Coding agent 要什麼配備？**

最低一張 RTX 5090（或同等級 24GB+ VRAM 的卡）跑 Qwen3.6 27B 或 Gemma 4 31B。詳見上面 RTX 5090 那篇。

---

## [RTX 5090 + Qwen3.6-27B 七種推論引擎實測：Sonnet 4.6 等級的本地推論，NT$30 萬桌機跑得起來嗎？](https://ai-coding.wiselychen.com/qwen-3-6-27b-rtx-5090-inference-engine-benchmark/)
*🏢 Wisely Chen AI | 2026-05-14*

## TL;DR

  * **核心問題** ：Qwen 3.6-27B ≈ Sonnet 4.6 等級，**這個能力能塞進 NT$30 萬以下的桌機嗎？** 答案：**能，整套 NT$30 萬剛剛好卡進企業 IT 採購的桌機/工作站預算天花板**
  * **2026 是本地小模型性價比騰飛的元年** — RTX 5090（32GB VRAM）配 Qwen3.6-27B，單流 140 tok/s、並發 575 tok/s 都做得到
  * **七種配置實測** ：vLLM × 3、llama.cpp × 2、Ollama × 2，外加一個直接 OOM 的失敗案例
  * **三個冠軍** ： 
    * 單流最快：**llama.cpp + MTP（Q2_K_XL）→ 140 tok/s**
    * 並發最強：**vLLM AWQ-INT4 → 575 tok/s @ 並發 8**
    * 開箱即用體驗最好但效能最差：**Ollama Q4_K_M → 64 tok/s（並發完全不擴展）**
  * **最反直覺發現** ：同一個 Q4_K_M GGUF，llama.cpp 比 Ollama **並發吞吐快 3.2x** — Ollama 把 batching 給關了
  * **量化命名不可信** ：標榜 “GPTQ-Int4” 的模型實測載入 27.5 GiB（應 ~13.5 GiB），attention/visual layer 還是 BF16



* * *

## 為什麼這又是一篇「無聊 IT 架構」文

又一篇 IT 架構系列文，不是炫耀 benchmark。

過去半年我一直在追這條線：**「本地 LLM 到底什麼時候 ROI 翻過來」** 。前幾個月寫過 [DGX Spark 跑 Qwen3.6-27B](https://ai-coding.wiselychen.com/qwen-3-6-27b-gb10-home-inference-sonnet-level/) 的觀察 — 那篇結論是「家用 AI 工作站時代到了」。但 DGX Spark 是 $4,699 的特規機，買的人還不多。

這次我自己組了一台桌機（消費級零組件），想回答一個非常具體的性價比問題：

> **「Qwen 3.6-27B 既然被認為接近 Sonnet 4.6 等級，那這個能力能不能塞進一台 NT$30 萬以下的桌機？選錯引擎會差多少？」**

NT$30 萬是企業 IT 採購一台「中高階桌機/工作站」的常見上限 — 過了這條線就要走資產採購、董事會審核。如果跑 Sonnet 4.6 等級的本地 AI 必須花 NT$50 萬以上，那這條路就還是只有 R&D 部門能玩，business unit 進不來。

實測答案：**整套 NT$30 萬剛好卡進企業預算天花板。** 而且這台桌機單流跑得贏多數 API 的速度（140 tok/s）、並發吞吐到 575 tok/s（GPT-4o-mini 級別）。對比之下，2025 年要跑同樣等級的模型只能買 H100，光一張卡就 NT$100 萬起跳 — **整整貴三倍以上** 。

**但前提是你選對引擎、選對量化、跳過三個坑。** 選錯的話，同一張卡跑出 2x tok/s — 你會以為本地 LLM 還是不能用。

* * *

## 四個維度看 LLM 推論的選擇地圖

判斷一個 LLM 推論方案值不值得用，看四個維度就夠了：**模型能力、單人 tok/s、多人併發 tok/s、token/NT$** 。把市面上主流方案攤開來比：

方案 | 模型能力 | 單人 tok/s | 多人併發 tok/s | NT$/1M tokens  
---|---|---|---|---  
Claude Sonnet 4.6 API | ★★★★★ 旗艦 | ~80 | 無上限 | ~270  
GPT-4o-mini API | ★★★ 入門 | ~120 | 無上限 | ~11  
**RTX 5090 + Qwen3.6-27B（最佳引擎）** | **★★★★ ≈ Sonnet 4.6** | **140** | **575** | **~10**  
Mac Studio M3 Ultra + Qwen3.6-27B | ★★★★ | ~45 | 受限 | ~60  
DGX Spark + Qwen3.6-27B | ★★★★ | 136 | ~200 | ~15  
H100 server + Qwen3.6-27B | ★★★★ | ~150 | 1000+ | ~12（但 27B 用不滿，殺雞用牛刀）  
  
四個維度怎麼讀：

  1. **模型能力** — 決定 workload 可不可行。Qwen3.6-27B ≈ Sonnet 4.6 是 2026 才有的事，過去本地模型都還停在 GPT-3.5 等級
  2. **單人 tok/s** — 影響 IDE 補全、即時對話延遲。5090 + MTP 140 tok/s 連雲端 API 都比不上，因為 API 還要算 network RTT
  3. **多人併發 tok/s** — 影響團隊共用、批次處理。5090 + vLLM 575 tok/s 已經到 GPT-4o-mini API 級別吞吐 — 一台桌機服務一個小團隊
  4. **NT$/1M tokens** — 影響大規模用量的 ROI。5090 攤提下來 ~NT$10，**比 Sonnet 4.6 API 便宜 27 倍** ，跟 GPT-4o-mini 同價位但能力高一級



> NT$/1M tokens 計算基準：API 用官方定價、輸入輸出 1:1 估算；本地用 NT$30 萬桌機攤提 5 年 + 電費 + 30% 利用率

**5090 + Qwen3.6-27B 是「四個維度都進前段班」的方案。** 不是極致最快、不是極致最便宜，但四個維度沒有任何一項是短板。這就是「性價比騰飛」的本質：**不是某一個維度暴衝，是全部維度同時翻過了能用的門檻** 。

過去本地 LLM 在「模型能力」這個維度就被卡死了，剩下三個再好都沒意義 — 模型笨用戶不會用。現在能力到位，剩下三個維度才開始有討論價值。

* * *

## 第一段｜為什麼說 2026 是「小模型性價比騰飛」的元年

把過去 18 個月的關鍵節點排一下：

時間 | 事件 | 對「本地 LLM」的意義  
---|---|---  
2024 Q4 | 70B 模型才能 production，要 2x A100 | 一台機器破百萬，ROI 算不回來，企業不碰  
2025 Q2 | Qwen 3.5-27B 出來，tool calling 可用 | 第一次 27B 達 production 門檻  
2025 Q4 | 量化技術成熟：AWQ INT4、FP8 KV cache、MTP | 27B 模型壓進 16GB VRAM  
2026 Q1 | Blackwell（5090）零售上市 | 32GB GDDR7、SM 120，整機 NT$30 萬  
**2026 Q2（現在）** | **Qwen 3.6-27B + 5090 + 進化過的引擎** | **Sonnet 4.6 等級能力裝進 NT$30 萬以下桌機**  
  
三件事在同一個時間點交叉：

  1. **模型側** ：27B dense 模型品質追上 Sonnet 4.6（在 SWE-bench、Terminal-Bench 等場景）
  2. **硬體側** ：消費級 5090 把 32GB VRAM 帶到桌面，整機 NT$30 萬剛好卡進企業桌機預算天花板 — 過去同等級能力要 H100，光一張卡 NT$100 萬，整整貴三倍
  3. **軟體側** ：推論引擎這半年集體大改 — vLLM 0.20 的 cudagraph、llama.cpp 收 MTP PR、AWQ 真正純 4-bit 量化普及



**這三件事任何一件沒到位，本地 27B 都還是 demo 級。三件同時到位才算「性價比騰飛」。**

性價比的本質是「能力 ÷ 預算」。**過去能力線上不去，現在能力上來了、預算也下來了，但天花板換成了「會不會調」** — 一張同樣的卡，配對的引擎跟參數能讓 token speed 差 9 倍。所以接下來這段最想講的，不是「性價比有多好」 — 而是**選錯配置會差到讓你以為這條路走不通** 。

* * *

## 第二段｜七種配置實測，包含一個直接失敗的

機器規格先放著：

  * GPU: NVIDIA RTX 5090（Blackwell, SM 120, 32GB GDDR7）
  * Driver: 595.58.03（最高支援 CUDA 13.2，但編譯**必須用 12.9** — Unsloth 警告 13.2 會輸出亂碼）
  * Host: Ubuntu 24.04 原生（不是 WSL）
  * RAM: 64GB



測試 prompt 用同一段 63 token 的提示寫關於計算機歷史的 essay，`temperature=0` 跑單流，`temperature=0.7` 跑並發。

### Config 1：vLLM + GPTQ-Int4（直接 OOM 失敗）

我一開始抓的是 `raydelossantos/Qwen3.6-27B-GPTQ-Int4`，名字寫 “Int4”，磁碟大小 29 GB。

啟動就死：
    
    
    1
    

| 
    
    
    ValueError: No available memory for the cache blocks
      
  
---|---  
`

模型載入吃了 **27.51 GiB** （純 Int4 27B 應該只要 ~13.5 GiB），KV cache 只剩 0.18 GiB 直接掛掉。

去翻 `config.json` 才發現名實不符：
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

| 
    
    
    "quantization_config": {
      "bits": 4,
      "dynamic": {
        "-:.*attn.*": {},          // attention 不量化
        "-:.*mtp.*": {},           // MTP 層不量化
        "-:.*shared_expert.*": {}, // shared expert 不量化
        "-:.*visual.*": {},        // visual encoder 不量化
        "lm_head": {}
      }
    }
      
  
---|---  
`

**只有 MoE expert 部分是 Int4，attention、visual、MTP head 全部是 BF16。** 名字叫 “Int4” 但本質是「部分量化」。32GB VRAM 在 5090 上根本不夠塞。

**Reality check：模型卡上寫「Int4」「INT4」「W4A16」千萬不要照單全收。** 看 `config.json` 裡的 `dynamic` 例外清單，或對比磁碟容量 — 純 4-bit 27B 模型應該 ~14 GB，不該 29 GB。

### Config 2：vLLM + NVFP4-BF16 + enforce-eager（救命但慢）

換 `rdtand/...NVFP4-BF16-vllm`（19 GB），這次能跑了，但要加 `\--enforce-eager` 才能塞進 32GB：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    ~/vllm-qwen-env/bin/vllm serve rdtand/Qwen3.6-27B-PrismaSCOUT-Blackwell-NVFP4-BF16-vllm \
      --gpu-memory-utilization 0.92 \
      --max-model-len 8192 \
      --enforce-eager \
      --served-model-name qwen-nvfp4
      
  
---|---  
`

`--enforce-eager` 是救命 flag — 它跳過 cudagraph capture 階段（會吃 12GB+ VRAM）。**但代價是砍掉 30-50% decode 速度。**

實測：

  * 單流：**20.5 tok/s** （比 Ollama 還慢！）
  * 並發 16：304 tok/s



學到的事：**32GB VRAM 跑 27B 模型，模型本體必須壓到 ~16 GiB 以下** ，才有空間給 cudagraph 跑全速。19 GB 已經太大。

### Config 3：vLLM + AWQ-INT4 + cudagraph（並發冠軍）⭐

換 `cyankiwi/Qwen3.6-27B-AWQ-INT4`（20 GB on disk，**真正的純 4-bit AWQ** ）。然後做兩件事讓 cudagraph 跑起來：
    
    
    1
    2
    3
    4
    5
    6
    

| 
    
    
    ~/vllm-qwen-env/bin/vllm serve cyankiwi/Qwen3.6-27B-AWQ-INT4 \
      --gpu-memory-utilization 0.92 \
      --max-model-len 4096 \
      --max-num-seqs 8 \          # ← 關鍵
      --kv-cache-dtype fp8 \      # ← 關鍵
      --served-model-name qwen-awq
      
  
---|---  
`

  * `\--max-num-seqs 8`：vLLM 預設要 capture 51 個 cudagraph size，會 OOM。砍到 8 之後只 capture `[1,2,4,8,16]` 五個
  * `\--kv-cache-dtype fp8`：KV cache 從 fp16 壓成 fp8，省一半記憶體



實測：

  * 單流：**80.5 tok/s** （比 enforce-eager 快 4x）
  * 並發 4：263 tok/s
  * 並發 8：**575 tok/s** 🏆
  * 並發 16：574（被 max-num-seqs 上限卡住）



**575 tok/s 是什麼概念？** 比 Ollama 同條件快 9x，比 GPT-4o-mini 的 API 吞吐還高（用同一張卡服務 8 個並發用戶）。

### Config 5：llama.cpp + MTP（單流冠軍）⭐

切換引擎到 llama.cpp，跑 `unsloth/Qwen3.6-27B-MTP-GGUF` 的 Q2_K_XL（**只有 12 GB** ）。

MTP 是 Multi-Token Prediction — 模型內建一個 draft head 預測接下來 2 個 token，target model 驗證。接受率 70%+ 等於免費加速。

Build 過程要小心 CUDA 雷區：
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

| 
    
    
    # 必須用 CUDA 12.9 toolkit，不是 13.2（會輸出亂碼）
    export PATH=/usr/local/cuda-12.9/bin:$PATH
    export CUDACXX=/usr/local/cuda-12.9/bin/nvcc
    
    # Blackwell SM 120 要明確指定
    cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=120 \
      -DCMAKE_BUILD_TYPE=Release -G Ninja
    
    # 需要 PR 22673（MTP 支援還沒進 main）
    git fetch origin pull/22673/head:mtp && git checkout mtp
      
  
---|---  
`

啟動：
    
    
    1
    2
    3
    4
    

| 
    
    
    llama-server -m Qwen3.6-27B-UD-Q2_K_XL.gguf \
      -ngl 99 --ctx-size 4096 \
      --spec-type draft-mtp \
      --spec-draft-n-max 2          # MTP draft 2 個 token
      
  
---|---  
`

實測：

  * 單流：**140 tok/s** 🏆（全場最快）
  * 並發 8：**118 tok/s** （反而退化！）



**MTP 跟 batching 互斥** — draft model 和 target model 共享 KV cache，並發時雙方都要搶記憶體 → batching 失效。

所以 MTP 是「**單人神器、多人毒藥** 」。自己用爽歪歪、開 API 給隊友就完蛋。

### Config 6 + 7：Ollama vs llama.cpp（同一個 GGUF，效能差 3.2x）

這是最反直覺的一段。

**Ollama** （開箱即用，`ollama pull qwen3.6:27b`，內部就是 Q4_K_M GGUF）：

  * 單流：67 tok/s
  * 並發 4：64 tok/s
  * 並發 8：64 tok/s
  * **並發完全不擴展** ，等於序列化



我懷疑是 Ollama wrapper 的問題，所以拿同樣的 Q4_K_M GGUF 用 llama.cpp 直接跑（Config 7）：

  * 單流：75 tok/s（+12%）
  * 並發 4：**204 tok/s** （+219%）
  * 並發 8：189 tok/s



**同一個 GGUF、同一張卡，llama.cpp 比 Ollama 並發吞吐快 3.2x。**

我不知道 Ollama 內部做了什麼把 batching 給關了 — 它預設有 `OLLAMA_NUM_PARALLEL=4`，但實測表現完全不像有 batching。如果你現在用 Ollama 做生產 API，這 3.2x 的效能就是你白白送掉的。

> 小插曲：想用 Ollama 已經下載好的 GGUF 餵給 llama.cpp 不行，會報 `qwen35.rope.dimension_sections has wrong array length`。Ollama 的 GGUF metadata 跟 llama.cpp PR 22673 不相容，要從 unsloth HF 重下載一份。

* * *

## 第三段｜總成績單

Config | 引擎 | 量化 | 模型大小 | GPU 用量 | 單流 | 並發 4 | 並發 8  
---|---|---|---|---|---|---|---  
1 | vLLM | “GPTQ-Int4”（假） | 29 GB | ❌ OOM | - | - | -  
2 | vLLM | NVFP4 + eager | 19 GB | 30.2 GB | 20.5 | 74 | 127  
**3** | **vLLM** | **AWQ-INT4 + cudagraph** | 20 GB | 28.3 GB | 80.5 | 263 | **575** 🏆  
4 | vLLM | AWQ-INT4 單人版 | 20 GB | 28.9 GB | 80.7 | - | -  
**5** | **llama.cpp** | **Q2_K_XL + MTP** | 12 GB | 14.5 GB | **140** 🏆 | 118 | 118  
6 | Ollama | Q4_K_M | 17 GB | 24.6 GB | 67 | 64 | 64  
**7** | **llama.cpp** | **Q4_K_M（無 MTP）** | 16 GB | 17.6 GB | 75 | 204 | 189  
  
三個冠軍的用途分流：

場景 | 推薦 Config | 為什麼  
---|---|---  
自己一個人本地對話、寫 code 副駕 | **Config 5（llama.cpp + MTP）** | 140 tok/s、省顯存 14.5 GB，VRAM 剩一半可以同時開 IDE  
開 API 給團隊/客戶用 | **Config 3（vLLM AWQ）** | 575 tok/s 是其他配置的 5-9x，並發是 production 的本質  
自用 + 偶爾 2-3 人連 | **Config 7（llama.cpp Q4 無 MTP）** | 單流 75 + 並發 204 平衡，build 也不需要 PR 22673  
不想 build、開箱即用 | Config 6（Ollama） | 一行 `ollama pull` 就好，但接受效能只剩 1/3-1/9  
  
* * *

## 第四段｜五個不會寫在 README 的觀察

### 1. 量化命名不可信，看 config 跟磁碟大小

純 4-bit 量化的 27B 模型應該 ~14 GB。看到 29 GB 還叫 “Int4” 的，多半是 attention/visual 沒量化。檢驗方法：
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    # 純 4-bit GGUF 大小參考
    ls -lh *.gguf
    # Q2_K_XL: ~12 GB（極致壓縮）
    # Q4_K_M:  ~16 GB（生產標配）
    # Q6_K:    ~22 GB（高品質）
      
  
---|---  
`

看到 GPTQ/AWQ 模型也是一樣 — 直接看 `config.json` 的 `quantization_config.dynamic` 例外清單，或 `du -sh` 整個目錄。

### 2\. vLLM 的 cudagraph 是核心優化，不是 nice-to-have

`--enforce-eager` 砍掉 cudagraph + torch.compile 之後，速度從 80 跌到 20.5（**-75%** ）。但在 32GB VRAM 跑 27B 模型，**模型本體必須 < 16 GiB** 才有空間給 cudagraph capture。

換言之：選量化版本不要看「能不能載入」，要看「載入後還剩多少給 cudagraph」。

### 3\. cudagraph capture 預設 51 個 size 會 OOM

vLLM 預設 `cudagraph_capture_sizes = [1, 2, 4, 8, 16, 24, 32, ..., 512]`，51 個 capture 每個吃幾百 MB，在 32GB 卡上必爆。

解法是 `--max-num-seqs 8`，把 capture 砍到 `[1, 2, 4, 8, 16]` 五個。如果你只有單流需求，可以更激進 `--max-num-seqs 1`，只 capture `[1, 2]`。

### 4\. MTP 跟 batching 互斥 — 是「個人神器」不是「服務利器」

Q2 + MTP 單流 140，並發 8 退化到 118。Q4 無 MTP 單流 75，並發 8 衝到 189。

原因：draft model + target model 共享 KV cache，並發時雙方都要記憶體 → 互相搶 → batching 退化。

**做個人助理用 MTP，開 API 給人用就不要碰 MTP。**

### 5\. CUDA 13.2 + Blackwell 是雷區

Driver 寫支援 CUDA 13.2，但實測會輸出亂碼（Unsloth 官方有警告）。解法：driver 留著、編譯 toolkit 用 12.9。`nvidia-smi` 顯示的 CUDA 版本只是 driver 最高支援，不代表你必須用那個 toolkit。

* * *

## 第五段｜這對 IT 架構意味著什麼

我不是說「全部 workload 都該轉本地」。Claude/GPT 的 API 該用就用，特別是 Opus 級別的長思考任務、複雜 agentic 工作流，雲端旗艦模型還是大幅領先。

但有幾類 workload 現在 ROI 真的翻過來了：

Workload | 雲端 API | 本地 5090 + Qwen3.6-27B  
---|---|---  
員工問答 / 內部知識庫 RAG | 隱私風險 + 重複 token 燒錢 | 全在內網，固定成本  
程式碼補全（IDE inline） | 等待 200-400ms 才開始吐字 | 本機 TTFB < 50ms  
大量批次處理（log 分析、文件摘要） | 跑 1 萬筆要等好幾天排隊 | 並發 8 跑 575 tok/s，一個下午跑完  
Tool calling 為主的 agent | 每個 tool round 都付 token | 一張卡多人共用  
  
**這幾類 workload 的共通點：**

  * 任務不需要旗艦模型（27B 夠用）
  * 量大、重複、token 燒得快
  * 對隱私敏感，或對延遲敏感



**過去半年我給客戶的建議是「先用雲端 API 把流程跑出來，等開源追上再考慮本地」。從這次實測之後，我會改說：**

> 「先用雲端 API 證明流程有 ROI，然後抓你最燒錢、最不能漏的那 20% workload，現在就可以開始評估本地化。**一台 NT$30 萬的 5090 桌機，就是這 20% workload 的最佳 ROI 起點。** 」

不是要全面取代雲端，是 **workload 分流的時機到了** 。

### 回到開頭那個問題

> **「Qwen 3.6-27B 接近 Sonnet 4.6，那能不能在 NT$30 萬以下桌機跑起來？」**

答案是：**能，整套 NT$30 萬剛好卡進企業桌機/工作站採購天花板，不用走資產採購、不用董事會審核。**

但前提是你要：

  * 選對引擎（vLLM 並發、llama.cpp 單人，不要 Ollama 進 production）
  * 選對量化（AWQ-INT4 或 Q4_K_M，不要被「Int4」字面騙）
  * 跳過三個坑（cudagraph capture、MTP vs batching、CUDA 12.9 而非 13.2）



把這幾件事做對，你的 NT$30 萬桌機就是一台「Sonnet 4.6 等級、575 tok/s 並發、零雲端依賴」的 AI 服務器。這不是 demo、不是玩具，是 production-ready 的本地推論。

* * *

## 常見問題 Q&A

**Q: 為什麼不直接買 H100 / B200？**

5090 整機 NT$30 萬，H100 一張卡 NT$100 萬起跳，B200 更貴。如果你的 workload 是「能在 32GB 內塞下的模型，並發 8 以下」，5090 的 NT$/token 比 H100 划算 10 倍以上。H100 適合 70B+ 模型或要做 KV cache 共享的大規模服務，27B 用 H100 是殺雞用牛刀。

**Q: 為什麼不等 Qwen 3.7、5090 改款？**

可以等，但機會成本是「現在用不到本地推論的 6 個月」。我這次實測的目的就是回答「現在這個時間點，到底夠不夠用」 — 答案是夠了。等下一代是無止盡的循環，每代都會有人說「再等等」。

**Q: Mac Studio M3 Ultra 不是也能跑 27B？**

可以，但 token speed 大概是 5090 的 1/3 左右（M3 Ultra 約 40-50 tok/s，5090 cudagraph 配置 80+ tok/s）。Mac 的優勢是統一記憶體可以塞 70B+ 模型，5090 的優勢是純算力快、價格低。**選 Mac 還是 5090，看你要跑多大的模型** 。

**Q: 為什麼 Ollama 並發那麼差，社群還這麼推？**

Ollama 的優勢是「開箱即用」 — 不會 build、不熟 CUDA、不知道 `--max-num-seqs` 怎麼調的人，五分鐘就有一個能用的 LLM API。對「我只是想試試看本地 LLM」的人來說，這個體驗值很多。但要進 production，請直接用 llama.cpp 或 vLLM。

**Q: Qwen3.6-27B 比 Sonnet 4.6 還強？**

不是，是「某些 benchmark 上接近 Sonnet 4.6 等級」。實際使用品質 Sonnet 4.6 還是更穩、更會處理長 context、更會 reasoning。但對於「員工問 HR 政策、log 分類、code lint、簡單摘要」這類任務，27B 已經足夠 — 而且不會把客戶資料送出公司。

**Q: 要不要等 vLLM 出 FP4 kernel？**

值得期待，但不用為這個延遲決策。AWQ-INT4 + FP8 KV cache 在 5090 上已經跑得很好。FP4 出來估計再快 30-50%，但不會改變「現在能不能做」的答案。

* * *

## 完整 reproducibility

所有實測命令、啟動參數、踩坑紀錄都在我的內部報告：模型版本、cudagraph capture sizes、KV cache dtype、CUDA toolkit 版本，全部列清楚了。如果你也在規劃 5090 / 4090 / RTX PRO 系列跑本地 LLM，這份報告省你的時間絕對超過你的時薪。

**最後總結一句** ：

> 「2026 是本地小模型性價比騰飛的元年。但同一張卡能跑出 64 tok/s 也能跑出 575 tok/s — 差別不是硬體，是你選不選得對。」

* * *

**延伸閱讀：**

  * [Qwen 3.6-27B 本地部署：DGX Spark / Mac mini 跑出 Sonnet 4.6 等級 AI Agent](https://ai-coding.wiselychen.com/qwen-3-6-27b-gb10-home-inference-sonnet-level/)
  * [企業級地端 LLM 系統架構藍圖](https://ai-coding.wiselychen.com/local-llm-enterprise-architecture/)
  * [Tool Calling 1.5 - 本地 LLM Tool Calling 與 27B Sweet Spot](https://ai-coding.wiselychen.com/toolcall-15-local-llm-tool-calling-qwen-27b-sweet-spot/)

---

## [你的 Claude Code 可能被植入後門了：Mini Shai-Hulud npm 供應鏈攻擊全解析](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/)
*🏢 Wisely Chen AI | 2026-05-14*

> 安全研究員 carlini 在 [TanStack/router#7383 的留言](https://github.com/TanStack/router/issues/7383#issuecomment-4425225340) 點出最致命的一招：payload 會在 Linux 上掛 systemd user service、在 macOS 上掛 LaunchAgent（`com.user.gh-token-monitor`），每 60 秒去 poll `api.github.com/user` — token 一被 revoke，立刻 `rm -rf ~/`。

* * *

## 先講結論：現在請暫停 `npm install`

如果你今天看到這篇文章，請先做一件事：

**把手上正在跑的`npm install` / `pnpm install` / `yarn install` 全部停掉。**

不是危言聳聽，是真的有事。

過去一週，npm 生態系正在爆發一場叫做 **Mini Shai-Hulud** 的供應鏈攻擊。截至目前已知範圍：

  * **TanStack 官方 42 個 npm 套件** 遭植入惡意程式碼
  * 已釋出 **84 個惡意版本**
  * 光是 `@tanstack/react-router` 每週下載量就超過 **1,200 萬次**
  * 攻擊已擴散到 **OpenSearch、Mistral AI、Guardrails AI、UiPath、Squawk** 等 170+ 個套件
  * npm 與 PyPI 兩邊都中



而且最噁心的一點是：**這次攻擊專打用 AI 寫 code 的人。**

對，就是你我這種天天開 Claude Code、Cursor、VS Code 的人。

* * *

## 為什麼叫 Shai-Hulud？這個隱喻有夠到位

先說一下這個攻擊的命名梗，因為它真的反映了這次事件的本質。

**Shai-Hulud** 是科幻小說《沙丘》（Dune）裡的「沙蟲」 — 在 Arrakis 星球的沙漠底下蜿蜒穿行的巨型生物。牠的特性是：

  * **無所不在** ：整片沙漠底下都是牠
  * **殺不死** ：人類目前所有武器都對牠無效
  * **會自我繁殖** ：被切斷一段，那一段照樣活下去
  * **平常你看不到牠** ：只有當你太用力踩地面、發出震動，牠才從地底竄出來吃掉你



攻擊者顯然很清楚自己在做什麼 — 他們在惡意 repo 裡**用的 branch 名稱全部取自《沙丘》** ，每個被感染的 repo 描述都被改成同一句話：

> **“Shai-Hulud: Here We Go Again”**

而這個隱喻精準到讓人有點毛骨悚然：

  * **無所不在** → 這次蠕蟲藏在你天天裝的 dependency tree 裡
  * **殺不死** → 你 `npm uninstall` 完，它從 `~/.claude/settings.json` 又活過來
  * **會自我繁殖** → 它是 worm，偷到一個 repo 的 CI key 就感染下一個
  * **平常看不到牠** → 它只在你 revoke token 那一刻才現形 — 然後把你的 home directory 吃掉



而且攻擊者的黑色幽默還不只命名這一層。

### 攻擊者偽裝的身份是「Claude Code 本人」

這次惡意 commit 的提交者身份是：
    
    
    1
    2
    3
    

| 
    
    
    Author: Claude (claude@users.noreply.github.com)
    Committer: Claude Code GitHub App
    Message: chore: update dependencies
      
  
---|---  
`

對，**他冒充的就是 Claude Code 的 GitHub App** 。

你想一下這個畫面：

  * Repo 收到一個 commit
  * 作者顯示是 Claude
  * email 是 `claude@users.noreply.github.com`（看起來像 GitHub 的 noreply）
  * commit message 是 `chore: update dependencies`（每天都看到一百次）



整個維護者 review 介面看下來：**毫無違和感** 。

對於已經習慣讓 Claude / Cursor / Copilot 幫忙更新 dependency 的開發者，這個 commit 看起來就是「你昨晚開的 agent 工作完了」。

這就是 Shai-Hulud 第二層意思 — **牠連你看到牠的時候，都會偽裝成你最信任的東西。**

* * *

## 這次攻擊為什麼這麼難防

過去我們看 npm 供應鏈攻擊，大致都是同一套劇本：

  1. 駭客釣魚拿到 maintainer 的 npm token
  2. 推一個假版本上去
  3. maintainer 發現後 revoke token，下架版本



防禦邏輯也很單純：開 2FA、pin 死版本、看 lockfile，差不多就擋住八成。

但這次 Mini Shai-Hulud 把這套劇本整個翻掉了。

### 1. 2FA 沒用，因為被打的不是人

TanStack 維護者 Tanner Linsley 親自確認：**整個 team 都有開 2FA** 。沒人帳號被盜。

那是怎麼進去的？

攻擊者 fork 了 TanStack 的 repo，推了一個藏得很深的 commit，然後**騙過 TanStack 自己的 GitHub Actions 發版流程** ，讓 CI 用合法的金鑰幫惡意 code「蓋章認證」。

換句話說，這次被打的不是 npm 帳號，**是整條 CI/CD pipeline** 。

### 2. SLSA 簽章驗證直接失效

這是史上第一個有完整 **SLSA Provenance（軟體供應鏈 3 級可信證明）** 的 npm 惡意套件。

簡單講，SLSA 就是 npm 給套件貼的「這個版本真的是官方發的，沒被改過」的封條。

過去我們檢查供應鏈安全的最後一道防線就是看這個封條。

而現在 — **封條本身被駭客貼上去了** ，而且是真貨。

所有靠 cryptographic provenance 來檢查的工具，這次全部失靈。

### 3. `npm uninstall` 殺不掉它

這才是真正讓 AI 開發者該全身發冷的部分。

過去的 npm 惡意套件，最多就是執行一個 `postinstall` script，把你電腦上的 `~/.aws/credentials`、`~/.ssh/` 偷走。你只要：
    
    
    1
    2
    

| 
    
    
    npm uninstall `<package>`
    rm -rf node_modules
      
  
---|---  
`

就乾淨了。

但 Mini Shai-Hulud 不是這樣。它做的事情是：

**修改你的`~/.claude/settings.json` 和 `~/.vscode/tasks.json`，把自己埋進去。**

意思是：

  * 你刪掉惡意套件 ✅
  * 你刪掉整個 `node_modules` ✅
  * 你刪掉整個專案 ✅



**只要你下次打開 Claude Code 或 VS Code，它就會被觸發重新執行一次。**

它把自己掛在 IDE 的 hook 上面，每次你叫 Claude 跑工具、每次 VS Code 跑 task，它就跟著跑一次。

`npm uninstall` 是治標不治本，根本沒有 uninstall 到。

### 4\. 死亡開關（Dead-man’s switch）

最狠的一招在這裡。

它偷走你的 GitHub token 之後，會在你本機部署一個 watcher，做一件事：

> **持續監看 GitHub 上的這顆 token 還在不在。**

如果你做了「正常的應變動作」— 發現 token 外洩，跑去 GitHub Settings 把它 revoke 掉 — 那一瞬間：

**它會把你整個 home directory`rm -rf` 掉。**

所有專案、SSH key、設定檔、Downloads 裡那份沒備份的合約 — 全部炸光。

這是教科書級別的勒索手段：**「你不撤 token，我就慢慢偷你的東西；你撤 token，我就毀了你整台電腦。」**

* * *

## 為什麼這次 AI 開發者是高風險族群？

我自己這幾天看下來，感受最深的一點是：

**這次的攻擊面，跟你「依賴 Agent 的程度」成正比。**

### 第一個風險：Agent 不會幫你檢查 lockfile

我們以前裝套件的習慣，是手動敲 `npm install <package>`，會多看一眼版本號。

現在我們開著 Claude Code 寫 code，自然語言講「幫我加上 react-router」，Agent 就直接幫你裝了。

**Agent 不會去看「這個版本是不是 6 分鐘前才剛發佈的」、「provenance 有沒有異常」、「maintainer 有沒有發公告說被打」。**

Agent 對 npm registry 的信任，是無條件的。

### 第二個風險：你的 .claude/settings.json 是「植入後門的完美位置」

Claude Code 的 `settings.json` 設計上就是讓你掛 hooks、定義工具行為的地方。它每個 Claude 事件都會去讀一次。

從攻擊者的角度，這簡直是禮物：

  * ✅ 每次 Claude 工作都會 trigger 一次（持久化）
  * ✅ 寫進去看起來像 legitimate 的 user config（隱蔽性）
  * ✅ Claude 有檔案系統、shell、網路權限（爆破半徑大）



VS Code 的 `tasks.json` 同理。

過去這些檔案本來就在你的 `.gitignore` 裡，你自己也不太會打開看，這就是 perfect hiding spot。

### 第三個風險：pin 死版本也救不了你

過去我們會說：「別用 `^1.0.0`，要用精準版本 `1.0.0`，這樣才安全。」

這次例外。

因為這次的攻擊發生在「官方版本發佈的 6 分鐘窗口期」之內 — 你 pin 死的那個版本號，本身就是惡意版本。

**版本號是對的，內容是壞的，簽章是真的，CI 是合法的。**

你能信任的所有東西，這次都失效。

* * *

## 現在請馬上做這幾件事

我自己昨晚做的清單，提供參考：

### Step 1：暫停所有套件安裝（這小時就要做）
    
    
    1
    2
    3
    4
    

| 
    
    
    # 包含但不限於：
    # - 別 npm install / pnpm install / yarn install
    # - 別讓 Claude Code / Cursor 自動裝套件
    # - CI/CD 上能暫停 build 就暫停
      
  
---|---  
`

如果你不能停 CI（畢竟是 production），至少把 `npm ci --ignore-scripts` 加進去，先擋掉 postinstall script 的執行。

### Step 2：檢查 IDE 設定有沒有被改過

**最重要的兩個檔案：**
    
    
    1
    2
    3
    4
    5
    6
    7
    

| 
    
    
    # Claude Code 的 hook 設定
    cat ~/.claude/settings.json
    
    # VS Code 的 task 設定
    cat ~/.vscode/tasks.json
    # 或專案層級的
    cat .vscode/tasks.json
      
  
---|---  
`

看裡面有沒有你自己沒設定過的 hook、command、task，特別是任何長得像 base64 編碼、curl 到陌生網址、或執行 `node -e "..."` 一行 inline script 的東西。

**有就是中招了。**

### Step 3：跑一次自動化檢查

社群已經有人寫好工具：
    
    
    1
    

| 
    
    
    npx supply-chain-attack
      
  
---|---  
`

它會掃你的 `node_modules`、`package-lock.json`、IDE 設定檔，比對目前已知的惡意套件清單。

（提醒：這指令本身的安全性也請自己評估一下，看一眼 source 再跑。）

### Step 4：旋轉所有 credentials（順序很重要）

這是最容易踩雷的一步。**順序錯了你會自己觸發 dead-man’s switch。**

正確順序：

  1. **先** 把 IDE 設定檔（`.claude/settings.json`、`.vscode/tasks.json`）裡的可疑條目清掉
  2. **再** 把 watcher process 找出來 kill 掉（檢查 `ps aux`、`launchctl list`、crontab）
  3. **然後** 才去 GitHub / GCP / AWS revoke token



如果你還沒清乾淨就先 revoke token，watcher 偵測到的瞬間，你的 home directory 就沒了。

**先確保 watcher 死透了，再去動 token。**

### Step 5：備份 home directory（保險起見）
    
    
    1
    2
    

| 
    
    
    # 不管你有沒有中招，現在就 backup 一份
    cp -a ~/ /Volumes/External/home_backup_$(date +%Y%m%d)/
      
  
---|---  
`

跑完這個再去動 token，至少最壞情況下還救得回來。

* * *

## 坦白說：這件事的長期影響

短期是清毒、換 key。但這次 Mini Shai-Hulud 真正打開的潘朵拉盒子是：

**「合法 CI 簽章 + IDE 持久化」這個組合，從此會被當成標準攻擊模板。**

過去 AI 開發者的安全思維大概是：

  * 不要把 API key commit 進 git
  * 不要 `curl | bash` 不認識的 script
  * 不要安裝來路不明的 VS Code extension



這次之後，要再多加一條：

  * **不要假設你的`~/.claude/`、`~/.vscode/` 是乾淨的。**



我們把 Agent 寫進 IDE config 的便利性，跟攻擊者把後門寫進 IDE config 的便利性，是**同一個便利性** 。

這是 AI Coding 時代要學會接受的新 trade-off。

* * *

## 最後一句話

過去十年，我們用 `npm install` 換來的是極致的開發效率。

過去兩年，我們用 Agent 自動裝套件換來的是再翻一倍的效率。

**這次的代價，這幾天會慢慢浮現。**

不是說 Agent 不能用、npm 不能用 — 我自己也還是會繼續用。

只是這次之後，我會多做一件事：

> **每次 Agent 幫我裝完套件，我自己`cat ~/.claude/settings.json` 看一眼。**

便宜得很，五秒鐘的事。

但這五秒，就是 AI 開發者進入下一個階段必須付的學費。

* * *

## 延伸閱讀

  * [用 Claude Code 做 Linux 系統管理](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/ai-ops-yong-agent-claude-code-linux.md)
  * [ATPM：真實的 Vibe Coding 流程](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/atpm-a-real-production-vibe-coding-process.md)
  * [慢跑開會都能寫 code？Claude Code 讓我一天當 1.5 天用](https://ai-coding.wiselychen.com/npm-mini-shai-hulud-claude-code-supply-chain-attack/claude-code-yi-bu-xie-zuo-man-pao-kai-hui-dou-neng-xie-code.md)



* * *

## 參考資料

  * [TanStack/router#7383 — carlini 揭露 dead-man’s switch 機制](https://github.com/TanStack/router/issues/7383#issuecomment-4425225340)
  * [TanStack/router#7383 — Issue 主串與 IOC 清單](https://github.com/TanStack/router/issues/7383)
  * **已知 IoC：**
    * Linux systemd user service: `gh-token-monitor.sh`
    * macOS LaunchAgent: `com.user.gh-token-monitor`
    * 輪詢端點：`api.github.com/user`（每 60 秒）
    * 偽造 commit 身份：`claude@users.noreply.github.com`
    * 偽造 commit message：`chore: update dependencies`
  * **受影響套件清單（截至發稿）** ：TanStack、OpenSearch、Mistral AI、Guardrails AI、UiPath、Squawk
  * **持久化目標** ：`~/.claude/settings.json`、`~/.vscode/tasks.json`、`~/.local/bin/gh-token-monitor.sh`

---
