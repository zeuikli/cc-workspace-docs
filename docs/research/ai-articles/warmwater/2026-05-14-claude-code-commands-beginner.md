---
url: "https://warmwater.dev/blog/claude-code-commands-beginner"
title: "為什麼你的 Claude Code 用起來跟別人不一樣？"
date: 2026-05-14
category: Tutorial
source: warmwater.dev
---

第一次開啟 Claude Code，很多人會直接開始打字，把它當成一個進階版的 ChatGPT。這樣用當然沒問題，但 Claude Code 有一套操作語法，學會之後工作效率會差很多。

這篇文章把 13 個最實用的指令分成三層：第一層讓你說得更精準，第二層讓你管理對話的節奏，第三層解鎖更進階的工作方式。不需要全部記住，按順序來就好。

---

## 第一層：用 @file、# 和 ! 讓 Claude Code 準確理解你的意圖

Claude Code 的輸出品質，很大程度取決於你給的 context 夠不夠精準。這三個語法是最基礎的工具，讓你的每一句話都更有效率。

### 1. `@file`：告訴 Claude Code 只看這裡

在訊息中加上 `@檔案路徑`，Claude Code 會優先讀取並鎖定在那個檔案操作，不會去動其他地方。

**基本用法**

```
@src/components/Header.tsx 把 navigation 改成 sticky
```

**為什麼要指定**

專案檔案多的時候，如果沒有 `@file`，Claude Code 可能會根據任務自己去搜尋相關檔案，有時候會動到你不預期的地方。加上 `@file` 就是明確告訴它：只看這裡，只改這裡。

同時指定多個檔案也可以：

```
@src/api/auth.ts @src/types/user.ts 幫我把 User type 補上 email 欄位
```

**當作背景資料使用**

`@file` 不只用在「請 Claude 編輯」，也可以拿來補充背景：

```
@docs/api-spec.md 根據這份規格，幫我寫 fetchUser 的測試
```

---

### 2. `#`：留便條，補充 context

訊息前加 `#`，這段文字會被加進 context 但不會觸發 Claude Code 回應。

```
# 這個專案使用 Pydantic v2，不要用舊版的 @validator 語法

# API endpoint 都在 src/api/ 目錄下
```

適合在任務中途補充背景資訊，或提醒某個限制，又不想讓 Claude Code 停下來回應你。

---

### 3. `!`：在對話框直接執行 shell 指令

不用切換視窗，在 Claude Code 輸入框前加 `!` 就能跑 shell 指令，輸出會出現在對話裡。

```
! git status

! npm run test

! cat src/config.ts
```

這個語法在你要把指令結果直接給 Claude Code 看的時候最好用。跑了測試失敗，`! npm run test` 之後，Claude Code 就已經看到 error output，直接說「幫我修這個」就好，不用再貼 log。

---

## 第二層：用 ESC、/clear、/rewind、/resume 控制對話節奏

對話跑久了，context 會越來越重，Claude Code 的判斷也可能開始跑偏。這一層的指令讓你控制對話的節奏——從打斷到倒帶，從壓縮到跨天接回，都在這裡。

### 4. ESC：打斷輸出

Claude Code 開始做了一件你不要的事，按 `ESC` 立刻停止。不用等它跑完，停下來之後直接補充說明或給新指令。

做大範圍修改時，如果方向錯了早停早省。讓它跑完再說「不對，重來」，等於多付了一次 token 成本。

---

### 5. `/clear`：清空 session，重新開始

```
/clear
```

清掉目前對話的所有 context，包含對話歷史、讀過的檔案內容、Claude 的回應。

**什麼時候用：**

- 換到完全不相關的任務，不想讓舊 context 影響判斷
- 發現 Claude Code 行為越來越奇怪，可能是 context 裡有矛盾的指令
- 對話太長，想給一個乾淨的新指令

`/clear` 之後 Claude Code 不記得你之前說的任何事，需要重新交代背景。

---

### 6. `/compact`：壓縮 context，不中斷工作

```
/compact
```

做長任務時，不想完全清掉，但 context 已經很長，用 `/compact`。它會把目前的對話壓縮成摘要，保留工作狀態（正在改哪些檔案、任務到哪一步），釋放 token 空間讓任務繼續。

**`/clear` vs `/compact`**

| 指令 | 效果 | 適合情境 |
|------|------|---------|
| `/clear` | 完全清空，歸零 | 換任務、重新開始 |
| `/compact` | 壓縮摘要，保留工作脈絡 | 長任務中途，節省 context |

---

### 7. `/rewind`：倒帶回任意時間點

`/rewind` 是 Claude Code 的程式碼與對話捲回指令，可以把檔案狀態和對話歷史還原到這個 session 內的任意時間點。

**啟動方式**

按兩下 `ESC`，或直接輸入：

```
/rewind
```

介面會顯示對話歷史與檔案 diff，讓你選擇要回到哪個時間點。選定之後，Claude Code 會還原那個點之後所有的檔案修改，並把對話歷史截斷到那個點。

這個功能有兩個用途。一是還原檔案：你不需要手動 `git checkout` 或逐一 undo，Claude Code 會把它這次修改的所有檔案一起還原，特別適合改了一批東西但方向整個跑偏的情況。二是清掉錯誤的 context：有時候不是要還原程式碼，而是你在對話裡給了錯誤的背景資訊，導致 Claude Code 的判斷開始跑偏，這時候 rewind 到錯誤資訊出現之前，重新給正確的說明，比繼續修補更有效率。

介面會列出這個 session 內的每一個對話節點，以及那個節點對應的檔案變更（例如 `summary.md +39 -0`），如果那輪沒有動到程式碼會顯示 `No code changes`。選定節點後，Claude Code 會把該節點之後的所有修改還原，對話歷史也會截到那個點。

---

### 8. `/resume`：接回上次的工作

昨天做到一半的任務，今天想繼續，用 `/resume`。

**在 session 外啟動**

```
claude -c        # 直接接續最後一個 session
claude -r        # 開啟選擇器，瀏覽所有歷史 session
```

**在 session 內切換**

```
/resume
```

會顯示歷史 session 清單，讓你選擇要切換到哪一個。

介面會顯示 session 的編號、第一句話的預覽、時間戳記與資料量，支援搜尋。`Ctrl+V` 可以預覽該 session 的內容再決定要不要接。

**Resume 的 token 成本**

Resume 一個 session，整個 message history 都會被完整載入——包含對話紀錄、tool call 的結果（讀取的檔案、執行的指令、修改的程式碼）。如果上次 session 用了 60k tokens，resume 之後就從 60k 起跳。

不 resume 的代價更高：開新對話，所有 context 消失，你得重新交代背景、讓 Claude Code 重新理解程式碼，浪費的時間和 token 反而更多。

減少 resume 成本的做法：

- **結束 session 前先 `/compact`**：把 context 壓縮成摘要，下次 resume 載入的是壓縮版，token 省很多。
- **用 `/context` 掌握狀況**：`/context` 列出目前 session 各元件（system prompt、工具定義、對話紀錄等）分別消耗多少 token，讓你在 context 爆掉之前就有完整的可視度。
- **換任務就 `/clear`**：要做完全不相關的任務，直接 `/clear` 比 resume 舊 session 更有效率。

---

### 9. `/cost`：確認 token 用量

```
/cost
```

顯示目前 session 用了多少 token 和費用。

Claude Code 的 context 會一直累積。每說一句話，不只是這句話本身，整個對話歷史都會重新送給模型，對話越長每次的成本就越高。定期看 `/cost`，搭配 `/compact` 使用，是控制費用最直接的方法。

---

## 第三層：用 /init、Plan Mode 與 Superpowers 解鎖進階工作方式

前兩層是每天都會用到的基礎。這一層需要多一點設定，但做一次之後，Claude Code 的工作方式會整個不同。

### 10. `/init`：建立 CLAUDE.md，讓規則永久生效

```
/init
```

讓 Claude Code 分析你的專案，自動生成一份 `CLAUDE.md`。這個檔案放在專案根目錄，之後每次啟動 Claude Code，它都會先讀這份文件。

`CLAUDE.md` 裡可以寫：

- 技術棧（例如 FastAPI + Pydantic v2）
- 不能修改哪些檔案
- Git 規定（例如永遠不能 push 到 prod）
- 程式碼風格偏好

有了 `CLAUDE.md`，就不需要每次開新 session 都重新交代背景。

---

### 11. Plan Mode：先規劃，再動手

Plan Mode 讓 Claude Code 在實際修改任何檔案之前，先列出它打算做什麼的步驟，你確認之後才執行。

**進入方式**

按 `Shift+Tab` 切換模式，底部狀態列出現 `plan mode on` 就代表進入了。

進入 Plan Mode 之後，Claude Code 在回應時只會列出規劃步驟，不會實際修改任何檔案。確認計畫沒問題之後，再按 `Shift+Tab` 切回正常模式執行。

**什麼時候用：**

任務超過 3 個步驟、會動到多個檔案、或者不確定 Claude Code 會怎麼做，先跑 Plan Mode。比起事後 undo，事前確認更省時間。

---

### 12. 安裝 Superpowers：讓 Claude Code 有更多能力

基本指令學熟之後，可以安裝 Superpowers 擴充 Claude Code 的能力。Superpowers 是一個 skill 套件，安裝之後可以直接呼叫預先定義好的工作流程，例如寫 commit message、做 code review、產生測試，不用每次重寫 prompt。

**安裝方式**

透過 Claude Code 官方 plugin marketplace 安裝：

```
/plugin install superpowers@claude-plugins-official
```

如果你偏好透過 Superpowers 自己的 marketplace：

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

**確認安裝成功**

安裝完成後，在 Claude Code 輸入 `/` 就會看到 skill 清單出現 Superpowers 提供的指令。

**第一次呼叫**

Superpowers 的 skill 大多會自動觸發。例如你開始討論要做什麼功能，`brainstorming` skill 就會啟動，引導你釐清需求，再進到規劃與實作。你也可以輸入 `/` 直接從清單選取。

**額外推薦：安裝 skill-creator**

skill-creator 是 Anthropic 官方提供的 skill，讓你用對話方式定義自己的 skill，把常用的 prompt 包裝成可重複呼叫的模組。

安裝方式很直接：到 [anthropics/skills](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) 把 `SKILL.md` 下載下來，放到全域的 `~/.claude/skills/skill-creator/SKILL.md`，所有專案都可以使用，不需要每個專案都設定一次。

**怎麼使用**

最自然的觸發方式是在對話裡直接說：

```
幫我把剛剛的 workflow 寫成 Skill
```

Claude Code 看到這個意圖，就會啟動 skill-creator 的流程，引導你把剛才討論的步驟和規則整理成一個可重複呼叫的 skill 模組。如果想直接啟動，也可以輸入：

```
/skill-creator
```

**Superpowers 是起點，不是規定**

Superpowers 的 skill 本質上是 markdown 文件，安裝之後你可以直接編輯，也可以刪掉不用的。

很多 skill 預設會有「先做 X，確認之後才做 Y」的強制流程（gate）。如果覺得某個 gate 太重，可以把語氣從「必須」改成「建議」：

```
# 改前（強制）
BEFORE writing any code:
1. List requirements
2. Get confirmation
ONLY THEN: write code

# 改後（建議）
If the task is non-trivial, consider:
- listing requirements first
- confirming scope before writing
```

語氣變軟之後，小任務 agent 會直接跳過，大任務才會自然觸發，不會每次都被流程打斷。

同理，如果某個 skill 整個對你沒用——你很少寫需求文件，那 `brainstorming` skill 可能根本不值得留——直接刪掉就好。

**只保留你真正在意的 gate。** 想想自己最常踩的坑是什麼。如果最痛的問題是「agent 說完成但沒驗證」，那只留一個 `verification-before-completion` 的檢查就夠了，其他都可以軟化或移除。Superpowers 給你一個起點，你現在已經知道哪些 skill 在哪些情況有用，根據自己的失敗模式挑著用，反而比全裝更有效。

---

### 13. Subagent：讓 Claude Code 平行處理多件事

Claude Code 可以同時派出多個 subagent，各自獨立執行任務，再把結果彙整回來。最直接的感受是：本來要一件一件跑的事，現在可以同時進行。

**觸發方式**

最常用的是自然語言。在 prompt 裡指定範圍和平行的意圖，Claude Code 就會自動拆解任務並派出 subagent：

```
幫我用 subagent 的方式，平行確認我近期五篇寫的 Blog 的內容有沒有可以改善的地方
```

「同時」、「平行」、「交給 subagent 處理」這類關鍵字會提高路由機率。subagent 啟動後，介面會顯示每個 agent 正在處理的任務名稱，底部狀態列顯示目前活躍的 agent 數量。

**其他觸發方式**

如果要確保用到特定 agent，可以用 `@` 指名：

```
@security-reviewer 檢查這次 PR
```

想自訂 subagent，把設定檔放在 `.claude/agents/` 資料夾，用 YAML frontmatter 定義名稱、description（Claude Code 靠這個決定何時路由）、工具權限與模型，Markdown body 就是 system prompt。最快的方式是輸入：

```
/agents
```

讓 Claude Code 幫你產生初稿。

---

## 快速參考

| 指令/語法 | 功能 |
|----------|------|
| `@file` | 指定目標檔案 |
| `#text` | 補充 context，不觸發回應 |
| `!command` | 執行 shell 指令 |
| ESC | 打斷輸出 |
| `/clear` | 清空 session |
| `/compact` | 壓縮 context，保留工作狀態 |
| `/rewind` | 還原檔案與對話到 session 內任意時間點 |
| `/resume` | 接回歷史 session |
| `/cost` | 查看 token 用量 |
| `/init` | 產生 CLAUDE.md |

---

## 結語

> 這三層操作有一個共同的邏輯——讓 Claude Code 知道你在做什麼、你想怎麼做、你不想要什麼。說得越清楚，它就越有用。
