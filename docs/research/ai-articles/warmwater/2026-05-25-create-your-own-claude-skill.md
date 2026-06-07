---
url: "https://warmwater.dev/blog/create-your-own-claude-skill"
title: "第一個 Claude Skill：用 skill-creator 打包可重用工作流程"
date: 2026-05-25
category: Tutorial
source: warmwater.dev
---

[
← Tutorial ](/blog?tag=Tutorial)  Tutorial 
 
# 第一個 Claude Skill：用 skill-creator 打包可重用工作流程
 
 2026-05-25 · — views  
  
  
CLAUDE.md 裡的每一行，每次對話都在 context 裡。如果你把工作流程的完整說明放在這裡，不管這次對話需不需要它，那些 token 都在燒。


還有一個比 token 更難察覺的問題：把工作流程寫在 CLAUDE.md，Claude 每次執行的路徑都略有不同。沒有強制的步驟邊界，Claude 在 context 壓力下會壓縮或合併步驟，同樣的任務，每次走的路不一樣。


Skill 同時解決這兩件事。


**讀完精華版（2 分鐘），你會理解：**


- Skill 的三層載入機制怎麼省掉「閒置 token」
- 把執行路徑固化的意義：不只是省 token，是讓 Claude 每次都走同一條驗證過的路
- skill-creator 怎麼把這件事變成一個對話流程


這篇不是 Skill 系統的完整說明。是一個具體操作示範，用 blog-publish 這個真實案例，帶你從頭建一個 Skill。


---


## 精華版


|  | 塞進 CLAUDE.md | 做成 Skill |
| --- | --- | --- |
| 每次 session 的成本 | 全量載入，永遠在 context | Metadata 常駐（~35 tokens），Body 按需載入 |
| 執行路徑 | 每次重新探索，可能漂移 | 固定路徑，步驟有序 |
| 多個工作流程並存 | 全都同時佔位 | 各自獨立，互不干擾 |
| 跨專案重用 | 複製貼上 | 安裝一次，到處可用 |


**三層載入：**


- **Layer 1 — Metadata**（~35 tokens，每次都在）：skill 的 name + description，Claude 用這兩個欄位判斷當前任務需不需要這個 skill
- **Layer 2 — SKILL.md Body**（數百到數千 tokens，觸發時才載入）：完整的執行指令
- **Layer 3 — Bundled Resources**（腳本、範本，執行過程中按需讀取）


**blog-publish 的真實數字：**


|  | Token 數 | 載入條件 |
| --- | --- | --- |
| Metadata（Layer 1） | ~35 | 每次 session |
| SKILL.md Body（Layer 2） | ~800 | 只在發文時 |
| 以前塞在 CLAUDE.md | ~800 | 每次，不管有沒有發文 |


10 個 session，3 次發文：塞 CLAUDE.md = 8,000 tokens；做成 Skill = 350 + 2,400 = **2,750 tokens**。


**4 個關鍵問題：**


**Skill 放在哪裡？** `.claude/skills/<skill-name>/SKILL.md` 放在專案目錄只對當前專案有效；放在 `~/.claude/skills/` 則全域可用。


**SKILL.md 至少需要什麼？** YAML frontmatter（name + description）加上 Markdown 格式的執行指令。其他都是選配。


**description 為什麼重要？** Claude 靠 description 決定要不要載入這個 skill。description 太模糊，Claude 可能遇到對的情境也不用它。


**skill-creator 是什麼？** Anthropic 官方的 meta-skill，用對話幫你寫 SKILL.md。你描述需求，它幫你打草稿。


---


> 
以下是完整版，按需取用。


## 把工作流程寫進 CLAUDE.md，會帶來哪兩個問題？


把工作流程寫在 CLAUDE.md 最直覺，但有兩個副作用。


**Token 成本。** CLAUDE.md 每次對話都會載入。blog-publish 的 SKILL.md 有 228 行，583 個空白分隔詞彙，換算下來約 800 tokens。我每天用 Claude 做各種事，發文大概佔所有 session 的 30%，也就是 70% 的時間，那 800 tokens 在 context 裡什麼事都沒做。一週七天、每天三四個 session，累計起來數字可觀。


**執行路徑的漂移。** CLAUDE.md 裡的說明只是文字，沒有強制的步驟邊界。Claude 每次讀到它都在重新解讀，在 context 壓力下（session 快到上限時）可能縮短步驟，或把本來要分開確認的環節合併。你要發文，但 SEO 沒做完整，或封面圖直接被跳過。


這是兩個性質不同的問題，但 Skill 的設計同時處理了它們。把流程做成 Skill，說明文字從「每次都在、可能被忽略」變成「被觸發才載入、必須遵守」。


## Skill 的三層載入機制怎麼運作？


一個 Skill 的目錄結構最精簡的版本只需要一個檔案：


```
blog-publish/
└── SKILL.md
```


需要的時候可以加其他東西：


```
blog-publish/
├── SKILL.md
├── scripts/ ← 可執行腳本
├── references/ ← 參考文件
└── assets/ ← 範本、靜態資源
```


Claude 有三個時間點會讀不同層的資料。


**Layer 1：Metadata（session 開始時載入）**


SKILL.md 的 YAML frontmatter：


```
---
name: blog-publish
description: 完整的 blog 文章發佈流程，從草稿到上線。每一步都需要用戶確認才能繼續。
---
```


這兩行會在 session 開始時注入 context，讓 Claude 知道它有這個能力。整個 metadata 約 35 tokens，不管你發不發文都在。


**Layer 2：SKILL.md Body（觸發時載入）**


Claude 判斷當前任務符合 description 描述的情境之後，才讀 SKILL.md 的主體。這部分可以很長，因為它只在需要時才佔 context。blog-publish 的 body 有 5 個步驟、6 個 gate、詳細的圖表規格，大約 800 tokens，但只有在發文 session 才會出現在 context 裡。


**Layer 3：Bundled Resources（執行過程中按需讀取）**


如果 SKILL.md 引用了外部腳本或文件，Claude 在執行到需要那個資源的步驟時才讀取。適合放細節很多但不常用的規格，比如某個工具的完整參數說明。


工程意義：你可以把所有工作流程做成 Skill，而不用擔心「裝越多、session 越重」的問題。只有被觸發的 Skill 才會真正進入 context。


## 怎麼安裝 skill-creator？


skill-creator 本身也是一個 Skill，放在 [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) 這個 repo 裡。安裝方式是把整個 `skill-creator` 目錄複製到你的 `.claude/skills/` 底下：


```
# 進入你的專案目錄
cd your-project/

# 下載 skills repo
git clone https://github.com/anthropics/skills.git /tmp/anthropics-skills

# 複製 skill-creator 到本地 skills 目錄
mkdir -p .claude/skills
cp -r /tmp/anthropics-skills/skills/skill-creator .claude/skills/
```


重新啟動 Claude Code session 之後，skill-creator 就在可用的 skill 清單裡了。如果要全域安裝（所有專案都能用），把目標路徑換成 `~/.claude/skills/`。


## 怎麼用 skill-creator 建立第一個 Skill？


呼叫方式：在 Claude Code 裡輸入：


```
/skill-creator
```


或者直接說「幫我建一個新的 skill」，Claude 判斷是 skill-creator 的使用情境後會自動載入。


載入之後，skill-creator 會用對話的方式收集資訊。以下是一個具體的對話流程示範：


---


**skill-creator：這個 skill 要讓 Claude 做什麼？**


> 
我想讓 Claude 執行一個固定的 blog 發文流程：整理草稿、做 SEO 優化、產封面圖、寫 LinkedIn 和 Threads 貼文，最後確認發布。每個步驟完成後都要等我確認才繼續。


**skill-creator：什麼情況下應該觸發這個 skill？使用者通常會說什麼？**


> 
我說「blog-publish」、「幫我發文」、或「這篇文章可以發了」的時候。


**skill-creator：每個步驟的輸入和輸出是什麼？有沒有需要特別處理的邊界情況？**


> 
輸入是一個 slug，Claude 去 `docs/materias/<slug>.md` 找草稿。輸出是 `src/content/blog/<slug>.mdx` 加上社群貼文存檔。邊界情況：草稿不存在時要先寫；任何 gate 說不行時要回上一步修改。


**skill-creator：這個 skill 需要調用其他工具或 skill 嗎？**


> 
是，會調用 blog-agentic-seo、pixel-cover、linkedin-post、threads-post 四個 skill。


---


問完這些問題後，skill-creator 會草擬 SKILL.md 的內容給你審核。如果有步驟不對，直接在對話裡說「第二步要更細一點」或「Gate 的措辭不對」，它會修改後再給你看一次。


產出的 SKILL.md 結構會長這樣：


```
---
name: blog-publish
description: 完整的 blog 文章發佈流程，從草稿到上線。每一步都需要用戶確認才能繼續。
---

# Blog 發佈流程

每一步完成後必須停下來等用戶確認，不可自動進入下一步。

## Step 1 — 草稿整理
...

## Step 2 — Agentic SEO
...

（以此類推）
```


YAML frontmatter 是 metadata（Layer 1），`---` 之後的 Markdown 是 body（Layer 2）。兩個部分在同一個檔案裡，但載入的時機不一樣。


## 為什麼 description 決定 Skill 有沒有用？


Skill 能不能在對的時機出現，很大程度取決於 description 寫得好不好。


Claude 靠 description 做判斷，不靠 Skill 的名字。description 太模糊：


```
# 不好用
description: Blog 工具
```


Claude 看到「幫我發文」的時候，不確定這個 skill 是不是這個情境，可能選擇不用它。


skill-creator 的設計原則裡把好的 description 稱為 “pushy”——不只說 skill 是什麼，要說清楚在什麼情境下應該用：


```
# 明確得多
description: 完整的 blog 文章發佈流程，從草稿到上線。每一步都需要用戶確認才能繼續。
```


如果你發現 Claude 有時候沒有自動載入 Skill，先看 description 有沒有包含使用者實際會說的語言。可以加上觸發情境，例如「Use when user says ‘publish’ or wants to publish a blog post」。


## 怎麼確認 Skill 有被正確載入？


建好之後，開一個新的 Claude Code session，說出預期的觸發語句。


如果 Skill 有被載入，Claude 的回應會依照 SKILL.md 裡的步驟走。如果沒有，通常是兩個原因：description 不夠明確，或 SKILL.md 的路徑放錯了。


skill-creator 本身有更完整的 eval 系統，可以跑自動化的觸發測試，分析哪些語句會觸發、哪些不會，然後建議怎麼修改 description。這屬於進階用法，等初版 Skill 穩定之後再來處理就好。


---


> 
**結語**：Skill 不是把說明文字從 CLAUDE.md 搬到別的地方，是把一條你已經驗證過的執行路徑固化成可重用的模組，讓 Claude 只在需要的時候才打開它。

  
  
 [ Tutorial ](/blog?tag=Tutorial) 
 

### 相關文章
[Tutorial

Claude Code 五個組件的觸發邏輯，以及為什麼 Hooks 是最被低估的那一個

2026-05-21
](/blog/claude-code-hooks-guide)[
Tutorial

為什麼你的 Claude Code 用起來跟別人不一樣？

2026-05-14
](/blog/claude-code-commands-beginner)[
Viewpoint

Python AI 工程師為什麼要學 TypeScript？

2026-05-10
](/blog/why-python-ai-engineers-learn-typescript)
