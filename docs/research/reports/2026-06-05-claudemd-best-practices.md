# GitHub 上 CLAUDE.md 最佳實踐 — 443 個 Repo 實證研究報告

**日期**：2026-06-05
**樣本**：443 個含根目錄 `CLAUDE.md` 的 GitHub repo（量化軌）+ 6 個官方/高影響力來源（質性軌）
**方法**：GitHub code-search 採集 + 本地 parse 量化統計 + 官方文件逐字驗證

---

## 執行摘要

CLAUDE.md 是 Claude Code 跨 session 持久化專案脈絡的核心機制。本研究兼採**量化**（443 個真實 repo 的結構統計）與**質性**（Anthropic 官方文件逐字接地）兩軌，得出三個與「常見直覺」相左的實證結論：

1. **多數 repo 比官方建議更精簡，但長尾嚴重失控**：行數中位數僅 **97 行**（遠低於官方 200 行上限），但 p90 達 **305 行**，**21%（94/443）超過 200 行**，最長一檔 2,528 行。問題不在「平均太長」，而在少數臃腫檔。
2. **官方推薦的進階特性實際採用率極低**：`@import` 模組化僅 **4%（18/443）**、`IMPORTANT/YOU MUST` 強調語法僅 **14%（60/443）** 採用。社群絕大多數停留在「純 markdown 章節」階段。
3. **architecture 是出現率最高的內容，但 grep 無法判斷品質**：architecture/structure 章節 header 出現率最高（75%）。官方推薦寫「架構*決策*」（architectural decisions / project layout），但同時警告別重複「Claude 讀 code 就能推斷的細節」。本研究的 header grep 無法區分高價值的「為什麼這樣設計」與低價值的「資料夾清單複述」——故只報告**普及率**，不宣稱合規落差。

官方核心立場可濃縮為一句逐字引文："**The more specific and concise your instructions, the more consistently Claude follows them.**"（越具體、越精簡，遵循率越高）。本報告的所有量化發現都圍繞「精簡 vs 完整」這條張力線展開。

> **抽樣框誠實聲明**：443 個 repo 來自 GitHub code-search 對 `filename:CLAUDE.md` 的**相關度排序**結果（非隨機抽樣），偏向已被索引、相對活躍的 repo。所有量化百分比信度標為 **MEDIUM**，代表此抽樣框下的分布，不可外推為「全 GitHub CLAUDE.md 母體」。

---

## 1. 背景與動機：CLAUDE.md 到底是什麼

CLAUDE.md 是 Claude Code 在每個 session 啟動時自動讀取的 markdown 指令檔，用來提供「無法從 code 推斷的持久脈絡」。官方對其本質有一個關鍵且常被誤解的定位：

> "CLAUDE.md content is delivered as a user message after the system prompt, not as part of the system prompt itself. Claude reads it and tries to follow it, but there's no guarantee of strict compliance"
> — code.claude.com/docs/en/memory（官方逐字）

這句話有兩個重大含意：

1. **CLAUDE.md 是建議性（advisory）而非強制性（enforced）**。它是 context，不是配置。需要「每次必做」的確定性動作（例如 commit 前必跑 lint）應改用 **PreToolUse hook**，官方原文：「Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens.」
2. **遵循率與寫法強相關**。因為是 context 而非規則引擎，「怎麼寫」直接決定「Claude 多可靠地遵循」。這正是「最佳實踐」存在的理由。

**為何重要（一手實證）**：Anthropic 內部團隊報告指出，CLAUDE.md 文件化品質與 Claude Code 的任務表現直接正相關——

> "The better teams documented their workflows, tools, and expectations in Claude.md files, the better Claude Code performed"
> — claude.com/blog/how-anthropic-teams-use-claude-code（官方一手）

Data Infrastructure 團隊特別強調，把既有 pattern 寫進 CLAUDE.md 後，Claude Code 在「新建 data pipeline」這類例行任務上表現優異。換言之，CLAUDE.md 不是錦上添花，而是決定 agent 在你的 codebase 能否勝任的槓桿點。

## 2. 核心概念：載入機制與五層架構

要寫好 CLAUDE.md，必須先理解它如何被載入——這是多數社群指南略過、卻決定一切的底層機制。

### 2.1 五層級載入（由廣到窄）

官方定義五個位置，依「載入順序、由廣到窄」排列，廣的先進 context、窄的後進（後讀的優先級視覺上更高）：

| 層級 | 位置 | 用途 | 共享對象 |
|------|------|------|---------|
| **Managed policy** | `/Library/Application Support/ClaudeCode/CLAUDE.md`（macOS）等 | 組織級強制指令 | 全機器所有使用者 |
| **User instructions** | `~/.claude/CLAUDE.md` | 個人跨專案偏好 | 僅你（所有專案） |
| **Project instructions** | `./CLAUDE.md` 或 `./.claude/CLAUDE.md` | 團隊共享專案指令 | 團隊（透過版控） |
| **Local instructions** | `./CLAUDE.local.md` | 個人專案私有偏好（須 .gitignore） | 僅你（當前專案） |
| **子目錄 CLAUDE.md** | `foo/bar/CLAUDE.md` | 按需載入 | 視位置 |

關鍵機制細節（官方逐字佐證）：

- **目錄樹向上 walk**：「Claude Code reads CLAUDE.md files by walking up the directory tree from your current working directory」——在 `foo/bar/` 啟動會載入 `foo/bar/CLAUDE.md` + `foo/CLAUDE.md`。
- **子目錄是懶載入**：「Files in subdirectories load on demand when Claude reads files in those directories」——不在啟動時載入，而是 Claude 讀到該目錄的檔案時才載入。這是控制 context 的關鍵手段。
- **Managed policy 不可被排除**：「Managed policy CLAUDE.md files cannot be excluded」——組織級指令永遠生效，IT/DevOps 用來強制全域標準。
- **/compact 後行為差異**：project-root CLAUDE.md 在 compact 後自動從磁碟重注入；子目錄版本則不自動，等下次讀檔才重載。

### 2.2 `.claude/rules/` 與 path-scoped 規則

官方提供比 `@import` 更進階的模組化機制：`.claude/rules/` 目錄，且支援 YAML frontmatter 的 `paths:` 條件載入——

> "Rules can be scoped to specific files using YAML frontmatter with the paths field. These conditional rules only apply when Claude is working with files matching the specified patterns."

這是 context 工程的核心：把「只在改某類檔案時才需要」的規則（如 API 驗證規則只在 `src/api/**/*.ts` 載入）移出主 CLAUDE.md，**減少每 session 的固定 context 開銷**。沒有 `paths` 的 rule 則與 `.claude/CLAUDE.md` 同優先級無條件載入。

### 2.3 `@import` 的真相：組織 ≠ 省 token

社群常誤以為 `@import` 能省 context。官方明確否定：

> "imported files still load and enter the context window at launch"
> "Splitting into @path imports helps organization but does not reduce context, since imported files load at launch."

**@import 只有組織功能，不省 token**。相對路徑以「含 import 的檔案位置」為準（非 working directory），最深遞迴 4 層。真正省 context 的是 path-scoped rules（懶載入），不是 import。


## 3. 最佳實踐與實作模式（官方接地）

綜合官方文件，CLAUDE.md 最佳實踐可歸納為六條可操作原則：

### 3.1 精簡優先：200 行建議上限（soft target）

官方逐字建議：

> "**Size**: target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence."

注意這是 **soft target 而非硬上限**：官方另說「CLAUDE.md files are loaded in full regardless of length」（無論多長都全載入），200 行是綁定「遵循率」的建議值，不是強制截斷。過長的後果官方說得很直接（best-practices 頁）：「Bloated CLAUDE.md files cause Claude to ignore your actual instructions!」——臃腫的 CLAUDE.md 會讓 Claude 忽略你真正的指令。**長度不只是 token 成本問題，是遵循率問題**：規則被淹沒在噪音裡。

剪枝判準（官方 best-practices）：對每一行問「移除這行會讓 Claude 犯錯嗎？」若否，刪除。社群進一步量化為「應在 90 秒內讀完」「80–120 行為最佳信噪比」（Medium 完整指南，社群整理）。

### 3.2 具體勝過模糊

官方給了三組對照範例，這是「最佳實踐」最可操作的部分：

| ❌ 模糊 | ✅ 具體 |
|--------|--------|
| "Format code properly" | "Use 2-space indentation" |
| "Test your changes" | "Run `npm test` before committing" |
| "Keep files organized" | "API handlers live in `src/api/handlers/`" |

官方原則：「write instructions that are concrete enough to verify」——寫到「可被驗證」的具體程度。

### 3.3 該寫什麼 / 不該寫什麼（官方排除清單）

**該寫**（official include）：Bash 命令、code style、workflow 規則、專案架構、命名慣例、「always do X」規則。判準：「what you'd otherwise re-explain」——你本來每次都得重講的東西。觸發新增的時機（官方）：Claude 第二次犯同樣錯、code review 抓到 Claude 該知道的事、你重複輸入同樣的修正、新隊友需要的 context。

**不該寫**（official exclude，逐字）：

> "Exclude: Anything Claude can figure out by reading code / Standard language conventions Claude already knows / Detailed API documentation (link to docs instead) / Information that changes frequently / Long explanations or tutorials"

這條與後文 §4 的量化發現直接衝突：實測多數 repo 仍把「Claude 讀 code 就能推斷」的 architecture/structure 大量寫進去。

### 3.4 強調語法：官方背書，但限量

官方明確背書 IMPORTANT / YOU MUST：

> "You can tune instructions by adding emphasis (e.g., 'IMPORTANT' or 'YOU MUST') to improve adherence."

且揭露 Anthropic 自身做法：「we occasionally run CLAUDE.md files through the prompt improver and often tune instructions (e.g. adding emphasis with 'IMPORTANT' or 'YOU MUST')」。但社群補充重要 caveat：「Reserve these for 1-2 genuinely critical rules; overuse dilutes their signal.」——只保留 1–2 條，濫用會稀釋信號。

### 3.5 /init 生成 + 持續精煉

不要從白紙開始。官方推薦 `/init`：

> "Run /init to generate a starting CLAUDE.md automatically. Claude analyzes your codebase and creates a file with build commands, test instructions, and project conventions it discovers."

`/init` 偵測 build system / test framework / code pattern 生成基礎；若已存在 CLAUDE.md 則建議改進而非覆寫。進階：`CLAUDE_CODE_NEW_INIT=1` 啟用互動式多階段流程（subagent 探索 → 問題補充 → 可審閱提案），且會讀取既有 `AGENTS.md` / `.cursorrules` / `.windsurfrules` 整合。

### 3.6 當作程式碼維護

> "Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts."

除錯訊號（官方）：Claude 重複犯錯 = 檔案過長規則被淹沒；Claude 問 CLAUDE.md 已答的問題 = 措辭不夠明確。除錯工具：`/memory` 列出當前 session 載入了哪些 instruction 檔及路徑順序，是「為什麼規則沒被遵守」的首要診斷工具。

### 3.7 跨工具統一：import-only 模式（實測發現的真實 pattern）

量化採集中發現一個官方文件也支持的精巧 pattern：**整檔只有一行 import**。多個 repo（DataDog/datadog-lambda-extension、Tracer-Cloud/opensre 等）的 CLAUDE.md 全文僅：

```
@AGENTS.md @CLAUDE_PERSONAL.md
```

官方對此明確支持：「If your repository already uses AGENTS.md for other coding agents, create a CLAUDE.md that imports it so both tools read the same instructions without duplicating them.」這把「工具無關指令（AGENTS.md）」與「個人偏好（CLAUDE_PERSONAL.md）」分離，CLAUDE.md 退化為純轉接器——是跨工具團隊的進階組織模式。

## 4. 量化發現：443 個真實 repo 的結構統計

> **方法學**：443 個 repo 經本地 parse（branch-agnostic contents API，1 個 fetch 失敗已排除）。以下分兩類指標：**(A) 分布統計**（直接測量，信度較高）；**(B) 內容覆蓋率**（關鍵詞 vs header 雙軌，見下方校準說明）。

### 4.1 檔案規模分布（直接測量，最可信）

| 指標 | 數值 |
|------|------|
| 行數中位數（median） | **97 行** |
| 行數 p25 / p75 | 58 / 181 |
| 行數 p90 | **305 行** |
| 行數最大 | 2,528 行（sokareem/codex_simulator） |
| bytes 中位數 | 4,201 |
| bytes p90 | 13,550 |

**核心發現一：多數精簡、長尾失控。** 中位數 97 行遠低於官方 200 行上限——半數 repo 做得比官方建議還精簡。但分布右尾極長：

- **符合官方 ≤200 行：349/443（79%）**
- **超過 200 行：94/443（21%）**
- 極端臃腫 >300 行：46 個；>500 行：19 個

問題不在「平均」，而在五分之一的 repo 把 CLAUDE.md 寫成了文件庫。官方對這群的判決很明確：規則會被淹沒、遵循率下降。

### 4.2 結構密度（直接測量）

| 指標 | 中位數 | p90 |
|------|--------|-----|
| Markdown headers（# ## ###） | 13 | 34 |
| Code blocks（fenced ```） | 2 | 8 |
| Bullet points（- / *） | 21 | 71 |

典型 CLAUDE.md 是「13 個章節標題 + 21 條 bullet + 2 個 code block」的結構化文件——符合官方「use markdown headers and bullets to group related instructions」的建議。極簡檔（<30 行）有 47 個，多為 stub 或 import-only。

### 4.3 內容覆蓋率（雙軌校準 — 重要方法學說明）

⚠️ **校準警示**：覆蓋率有兩種測法，差異巨大，必須雙軌呈現：
- **關鍵詞提及率（上界）**：全文含相關關鍵詞（如含 "build"/"building"）→ 高估，把「順帶提到」算進去。
- **Header 結構化率（下界）**：有專屬 section header（如 `## Build`）→ 更接近「刻意文件化」的真實率。
- ⚠️ 兩軌的關鍵詞集**不完全相同**（header build 多納 `install|setup|getting started`、header arch 多納 `overview|project`），故 header 非 keyword 的嚴格子集，兩者僅示意「提及 vs 結構化」的量級差，非精確上下界。

| 主題 | 關鍵詞提及率（上界） | Header 結構化率（下界） |
|------|---------------------|------------------------|
| Architecture / 專案結構 | 85% | **75%（334/443）** |
| Build / 安裝 / setup | 75% | **42%（185/443）** |
| Commands / scripts / usage | — | **55%（242/443）** |
| Style / convention / lint | 67% | **44%（196/443）** |
| Test | 70% | **34%（150/443）** |
| Workflow / Git / commit | 44% | **43%（192/443）** |

**核心發現二：architecture 是第一主流內容，但本研究無法判斷其品質。** 無論用哪種測法，architecture/structure 都是出現率最高的內容（header 75%）。這裡需要謹慎：官方的 include 清單明確包含「architectural decisions」「project layout」「Project architecture」——架構**決策**是官方推薦寫的；官方 exclude 的是「Anything Claude can figure out by reading code」與「long explanations or tutorials」，即可從 code 推斷的**細節複述**。本研究的 header grep 只能偵測「有沒有 architecture 章節」，**無法區分**高價值的「為什麼這樣拆分」與低價值的「資料夾清單複述」。因此我們只能誠實報告**普及率（75%）**，不能據此宣稱「社群與官方有合規落差」——那需要實際逐一閱讀章節內容判斷，本研究未做。

build/test 的觀察則較穩健：結構化率（42%/34%）遠低於關鍵詞率（75%/70%），證實「順帶提到 build」遠多於「設專章寫 build 命令」。而官方最看重、最該寫的恰恰是 build/test 命令——這部分的「設專章」比例偏低，是較有依據的改進空間。

### 4.4 進階特性採用率（精確 token 偵測，信度高）

這兩個指標是精確字串/語法偵測，信度高於關鍵詞 flags：

| 特性 | 採用率 | 解讀 |
|------|--------|------|
| `IMPORTANT` / `YOU MUST` 等強調語法 | **14%（60/443）** | 官方背書的特性，採用率偏低 |
| `@import` 模組化語法 | **4%（18/443）** | 極低；多數人不用模組化 |
| import-only 整檔（≤3 行 + @import） | 4 個 | 跨工具統一進階 pattern |

**核心發現三：官方推薦的進階特性幾乎沒人用。** 強調語法僅 14%、import 僅 4%。一個有趣的交叉統計：**用了強調語法的檔案，行數中位數 179 行**（vs 全體 97 行）——越長、越複雜的檔越傾向用 IMPORTANT/YOU MUST 來「搶救」遵循率。這側面印證官方邏輯：檔案一臃腫，作者就得靠強調語法把關鍵規則從噪音裡撈出來；但這治標不治本，根本解是精簡。


## 5. 常見陷阱與反模式

綜合官方排除清單、社群指南與 443 repo 實測，整理出最常見的反模式：

### 5.1 「Kitchen Sink」臃腫檔（實測 21% 中招）
最普遍的反模式。把所有能想到的東西塞進去，導致檔案 >200 行、規則被淹沒。官方逐字判決：「Bloated CLAUDE.md files cause Claude to ignore your actual instructions!」實測 94 個 repo（21%）超過 200 行，19 個超過 500 行。社群形容 300 行 personality 檔「信噪比近零」。**修法**：path-scoped rules 拆分 + 季度剪枝。

### 5.2 重複 Claude 能自行推斷的*細節*
注意：架構本身不是反模式——官方推薦寫「架構決策」。反模式是把**可從 code 推斷的細節**（資料夾清單、標準語言慣例、Claude 一個 session 就學會的東西）當成內容。社群一針見血：「Do not waste CLAUDE.md lines on things Claude will learn after one session.」（本研究的 grep 無法量化這個落差的規模——architecture header 75% 含了高價值的決策說明，不能一概視為反模式。）**修法**：寫「為什麼這樣設計、團隊特殊約定」這類決策性資訊，刪除純粹複述 code 結構的部分。

### 5.3 把 CLAUDE.md 當強制執行層
誤以為寫了 "NEVER push to main" Claude 就一定不會。但 CLAUDE.md 是 advisory context，「no guarantee of strict compliance」。**修法**：確定性需求（commit 前必跑測試、禁止某操作）用 **PreToolUse hook**，hook 是 deterministic 且 guarantee the action happens。官方表格明確區分：技術強制 → managed settings / hooks；行為引導 → CLAUDE.md。

### 5.4 互相矛盾的規則
多個 CLAUDE.md（root / 子目錄 / rules）給出衝突指引。官方：「if two rules contradict each other, Claude may pick one arbitrarily.」結果是不可預測行為。**修法**：定期 review root + nested + `.claude/rules/`，用 `/memory` 檢查實際載入了什麼。

### 5.5 通用模板（generic template）
直接抄網路模板，內容不反映團隊實際決策。社群：「Every section of your CLAUDE.md should reflect actual decisions your team made.」模板填充的 CLAUDE.md 充滿「正確但無用」的廢話。**修法**：每一段都該對應「我們團隊真的這樣做」的決策，否則刪。

### 5.6 誤以為 @import 省 token
把 CLAUDE.md 拆成一堆 @import 檔案以為省 context——但「imported files still load and enter the context window at launch」。拆分只是組織，不省 token。**修法**：要省 context 用 path-scoped rules（懶載入）或子目錄 CLAUDE.md（按需載入），不是 @import。

### 5.7 過度使用強調語法
全篇 IMPORTANT / YOU MUST，反而稀釋信號（社群：「overuse dilutes their signal」）。實測用強調語法的檔中位數 179 行，與臃腫高度相關。**修法**：限 1–2 條真正關鍵規則用強調；其餘靠精簡與具體。

## 6. 前沿趨勢與預測

1. **從「靜態檔案」走向「分層 context 工程」**。早期 CLAUDE.md 是單一靜態檔；現在官方推進 `.claude/rules/` + path-scoped 懶載入 + 子目錄按需載入 + skills（只在被調用時載入）的**分層體系**。趨勢明確：把固定 context 開銷降到最低，按需才載入。實測僅 4% 用 @import、結構化覆蓋率不高，代表社群仍落後官方機制 1–2 個世代，這是最大的改進空間。

2. **Auto memory 與 CLAUDE.md 分工成形**。官方推出 auto memory（Claude 自寫的 MEMORY.md，每 session 載前 200 行/25KB）。分工：CLAUDE.md = 你寫的規則與標準；auto memory = Claude 從你的修正中自學的 pattern。預測：未來「最佳實踐」會強調**別把該交給 auto memory 的東西硬寫進 CLAUDE.md**（如 build 命令、debug insight，Claude 會自己學）。

3. **跨工具統一（AGENTS.md）成為團隊標配**。隨著 Cursor / Copilot / Windsurf 等都有各自指令檔，「維護一份工具無關 AGENTS.md，各工具檔 import 它」的模式會普及。實測已出現 import-only CLAUDE.md（`@AGENTS.md`）。官方 `/init` 已會讀取 `.cursorrules` / `.windsurfrules` 整合。

4. **HTML comment 留給人類的 metadata**。官方：block-level `<!-- -->` 在注入前被過濾、不耗 token。預測會出現「人類維護筆記（為什麼這條規則存在、何時該移除）寫在 HTML comment、Claude 看不到但維護者看得到」的雙層文件慣例。

## 7. 可立即實作的行動建議

依優先序，從高槓桿到進階：

1. **跑 `/init` 起步，別從白紙開始**。已有 codebase 直接 `/init` 生成基礎（自動偵測 build/test/pattern），再精煉。已有 CLAUDE.md 則 `/init` 會建議改進。進階用 `CLAUDE_CODE_NEW_INIT=1` 啟用互動式流程。

2. **砍到 200 行以下，目標 80–120 行**。對每行問「移除會讓 Claude 犯錯嗎？」否則刪。實測你若 >200 行，已落在最差的 21%。優先刪除：可從 code 推斷的架構*細節複述*（保留架構*決策*與「為什麼」）、標準語言慣例、CI 已強制的規則、會頻繁變動的資訊、長篇教學。

3. **把模糊改具體**。每條規則寫到「可驗證」：不是 "test your changes" 而是 "Run `npm test` before committing"；不是 "format properly" 而是 "Use 2-space indentation"。

4. **確定性需求改用 hook，不要靠 CLAUDE.md**。「commit 前必跑 X」「禁止 push main」這類用 PreToolUse hook 或 managed settings，因為 CLAUDE.md 不保證遵循。

5. **強調語法限 1–2 條**。只給真正關鍵的規則加 IMPORTANT / YOU MUST。如果你需要對很多條都加強調，真正的問題是檔案太長——回到第 2 點。

6. **大專案用 path-scoped rules 拆分**。把「只在改某類檔案才需要」的規則移到 `.claude/rules/*.md` 加 `paths:` frontmatter，減少每 session 固定開銷。注意：用這個而非 @import 來省 context。

7. **跨工具團隊用 AGENTS.md 統一**。維護工具無關的 AGENTS.md，CLAUDE.md 首行 `@AGENTS.md` 引入，下方只加 Claude 專屬指令。避免多檔重複維護。

8. **建立維護節奏**。每季 review：移除 CI 已強制的規則、刪除與 auto memory 重複的內容、更新陳舊架構說明、用 `/memory` 確認載入正確、給 3 個代表性 prompt 測試規則是否真的被遵循。

## 附錄：來源評分與索引

### A. 量化軌資料來源

| 項目 | 值 |
|------|-----|
| 採集方法 | GitHub code-search `filename:CLAUDE.md`，過濾 `path=="CLAUDE.md"`（根目錄） |
| 採集量 | 444 unique repo（8 頁 × 100/頁去重） |
| 成功 parse | 443（1 fetch 失敗，Fail Loud 已記錄並排除） |
| 抓取方式 | `gh api repos/{repo}/contents/CLAUDE.md`（branch-agnostic，自動解預設分支） |
| 量化欄位 | bytes, lines, headers, code_blocks, bullets, has_*（9 個 flag） |
| 信度 | **MEDIUM**（相關度排序非隨機抽樣；分布反映此抽樣框） |

### B. 質性軌來源評分

| # | 來源 | 層級 | 信度 | 評分 |
|---|------|------|------|------|
| 1 | [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) | O 官方文件 | HIGH | A/B/C/D/E 高 |
| 2 | [How Claude remembers your project（memory）](https://code.claude.com/docs/en/memory) | O 官方文件（逐字 WebFetch 親驗） | HIGH | 高 |
| 3 | [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code) | P 官方一手 | HIGH | 高 |
| 4 | [The Complete Guide to CLAUDE.md（Medium）](https://medium.com/@bijit211987/the-complete-guide-to-claude-md-memory-rules-loading-and-cross-tool-compression-97cc12ed037b) | C 社群 | MEDIUM | 中高 |
| 5 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | C 社群 GitHub | MEDIUM | 中 |
| 6 | [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | C 社群索引 | MEDIUM | 中 |

### C. 引文信度分層說明

- **官方逐字（HIGH）**：來源 1–3 的所有 `verbatim:` 引文，§2.3、§3.1 的 200 行與 import 條目經 WebFetch `code.claude.com/docs/en/memory` 親驗原文，非二手轉述。
- **社群整理（MEDIUM）**：來源 4–6 的部分結構建議（如「三層架構」「80–120 行」）為社群整理或多來源綜合，非官方逐字，已於正文標註「社群整理」。
- **量化統計（MEDIUM）**：§4 所有百分比為 443 repo 此抽樣框下的實測分布；內容覆蓋率採關鍵詞（上界）/ header（下界）雙軌呈現以避免單一測法的高估。

### D. 統計可重現性

量化結果可重跑驗證（非 LLM 自評），committed 資料附於 `research/reports/data/`：
- repo 清單：`research/reports/data/claudemd-repos-unique.txt`（444 unique repo）
- 統計輸出：`research/reports/data/claudemd-stats.jsonl`（443 列 JSONL，每列一 repo）
- parse 腳本：`research/reports/data/claudemd-parse.sh`（branch-agnostic 抓取 + tally）
- 重跑：`bash research/reports/data/claudemd-parse.sh <repos.txt> <out.jsonl>`，再以 `jq -s` 聚合分布。例：`jq -s 'map(.lines)|sort|.[(length*0.5)|floor]'` 取行數中位數。

---

**報告結束** · 量化軌 443 repo + 質性軌 6 官方/社群來源 · 官方引文經 WebFetch 親驗 · 抽樣框與信度誠實標註
