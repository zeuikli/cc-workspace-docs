---
date: 2026-07-11
status: draft-for-review
non-goals: 不建 SKILL 檔（本檔為提案，非落地產物）
topic: caveman-based-output-compression-skill
type: feasibility-report
---

# 以 caveman 為基礎開發新 SKILL 之可行性報告

**一句話結論**：條件可行——caveman 的壓縮語法可借用，但其零保真驗證、零模型檔位適配兩大缺陷須用本 workspace 既有的「白名單不變式 + 檔位校準表 + 機械失真閘」補強後才能落地，不可原樣移植。

---

## 1. Caveman 具體壓縮機制（原文引證）

來源：`github.com/juliusbrussee/caveman`（README、`skills/caveman/SKILL.md`、`skills/caveman-compress/SKILL.md`、`CLAUDE.md`、`benchmarks/run.py`，均 2026-07-11 WebFetch 讀取）。

### 1.1 壓縮手法 = 規則式風格改寫，非模型再訓練
`skills/caveman/SKILL.md` 原文：
> "Drop: articles (a/an/the), filler (just/really/basically/actually/simply), pleasantries...Fragments OK."

即靠**system prompt 規則清單**（非 few-shot、非微調）驅動：刪冠詞、刪填充詞、刪客套語、用短同義詞、允許片段句、重排資訊順序（先結果後解釋）。五個強度分級：`lite`（僅刪填充詞，保留完整句/冠詞）→ `full`（預設，刪冠詞+片段化）→ `ultra`（連連接詞都可省）→ `wenyan-lite/full/ultra`（改寫成文言文，最高達 80–90% 字元縮減）。

### 1.2 遞送機制 = 三通道（`CLAUDE.md`）
1. SessionStart hook 注入完整規則為隱藏 system context
2. `SKILL.md` frontmatter（支援結構化 skill 的 agent）
3. 單一真源 `caveman-activate.md` 經 `caveman-init.js` 複製進各 agent 專屬規則檔（`plugins/caveman/` 為 CI 自動產生鏡像，禁手動編輯）

### 1.3 已有的保真安全閥（比預期多，但仍有限）
`CLAUDE.md` 原文列出**自動退回正常語氣**的例外清單：
> "Caveman drops to normal prose for: security warnings, irreversible action confirmations, multi-step sequences where fragment ambiguity risks misread, user confused or repeating question."

`caveman-compress`（記憶檔永久壓縮指令）另有演算法式保真層：程式碼區塊、inline code、URL/連結、檔案路徑、指令、專有名詞、日期、版號、環境變數**逐字保留**；標題/清單階層不動；失敗時最多重試兩次並先建 `.original.md` 備份。

### 1.4 Benchmark 方法論（三臂設計，比自報數字看起來嚴謹）
`CLAUDE.md`：三臂比較 — baseline（無 system prompt）／terse control（僅給「回答簡潔一點」通用指令）／skill arm（完整 caveman 規則）。目的是排除「泛用簡潔指令本身就有效果」的混淆，只算 skill 相對 terse control 的**淨**增量。`benchmarks/run.py` 用真實 Claude API 呼叫、記 `response.usage.{input,output}_tokens`，宣稱「Never invent or round」。

### 1.5 兩處經原文證實的關鍵缺陷（本任務假設，非臆測，已核實）

**缺陷① 無保真度評分** — `benchmarks/run.py` 原文邏輯只有：
> `savings = 1 - (caveman_medians / normal_medians)`
只算 token 數比例，**完全沒有語意正確性 / 回答品質 / 事實保留的量化指標**。三臂設計解決的是「跟誰比」的混淆，沒解決「壓完還對不對」的問題。`caveman-compress` 雖有結構元素（code/URL/path）的演算法保留，但**對「一般敘述句裡的關鍵事實」（數字結論、因果鏈、否定詞）沒有等價的機械保真檢查**——只保結構元素，不保語意內容。

**缺陷② 無模型檔位適配** — `benchmarks/run.py` 預設模型 `claude-sonnet-4-20250514`，可用 `--model` override 但**benchmark 從未跑過多模型比較**（單次執行=單模型）；`AGENTS.md` 只是一份 `@./skills/*.md` 的 import 清單，**無任何模型能力分級或跨模型壓縮強度調整字句**。壓縮強度（lite/full/ultra/wenyan）是**使用者手動選**，不是系統依模型檔位自動決定；換言之弱模型與強模型套用同一份規則清單，缺陷假設成立。

---

## 2. 與本 workspace 既有制度對照

| Caveman 元素 | Workspace 對應 | Diff |
|---|---|---|
| 刪填充詞/冠詞/客套語 | `.claude/rules/output-discipline.md`「填充語禁止」「禁用詞」 | 方向一致，workspace 已有但無分級 |
| 片段化/清單化 | `output-discipline.md`「精簡句式」 | 一致 |
| 安全語句退回正常語氣 | `.claude/rules/core.md`「不可逆操作永遠等確認」「P0 安全二分」 | **workspace 紅線更硬**（core.md 是強制閘門非「退回語氣」建議）；caveman 只是 prompt 層軟退回，無確定性 gate 保證真的觸發 |
| CJK 壓縮（wenyan） | `output-discipline.md`「Token 效率（CJK 稅對策）」允許內部英文，但**對使用者最終回應維持繁中**（不 silent fork 鐵律） | **直接衝突**：wenyan 模式改寫使用者可見輸出語言/風格，違反「不 silent fork 繁中」——若引入必須限定 wenyan 只用於 internal/scratchpad，不可用於對使用者最終回應 |
| 6 級可調壓縮 | 無對應機制（`model-profiles.md` §1 有「行為指導密度」按檔位分級，但無「輸出壓縮強度」分級） | **真增量**：可補的結構性缺口 |
| 記憶檔永久壓縮 `/caveman-compress` | `memory-compactor` agent（壓 `memory/MEMORY.md`）邏輯不同：留決策+待辦，非風格壓縮 | 目的不同、可互補非取代 |
| 三臂 benchmark 方法論 | workspace `research/evals/` 有回歸 gate（`model-profiles.md` §2.1 eval 回歸 revert 線）但無「壓縮前後語意等價」評測維度 | **真增量**：可借用三臂設計思路，但須加保真軸 |

（延續 `research/reports/2026-07-11-fable-token-efficiency.md` 已收錄的初評，本報告為深讀後的具體化與差異補完，不重複列數字。）

---

## 3. 失真風險分析

### 3.1 哪類內容壓縮後最易失真
| 內容類型 | 失真機制 | Caveman 現有防護 | 缺口 |
|---|---|---|---|
| 數字/百分比/版號 | 片段化重排時易漏字或誤植鄰近數字 | 無（僅 code/URL/path 有演算法保留，一般敘述句數字不在保留清單） | **高風險缺口** |
| 否定詞（不/非/禁止/never） | 刪連接詞、片段化時否定範圍易歧義（"not X unless Y" 壓成片段可能丟失 unless 的例外條件） | 部分：ultra 級「strips conjunctions when meaning stays clear」——「stays clear」由模型自判，非機械驗證 | **高風險缺口，且防護是自我判斷非外部 gate** |
| 檔案路徑/error string | 逐字保留 | 有（`caveman-compress` 明列） | 已覆蓋 |
| 安全紅線語句 | 語氣退回正常但**依賴模型自己識別「這是安全警告」** | 有 exception 清單但無確定性 hook 強制 | **中風險**：與本 workspace core.md「不可逆操作永遠等確認」的**強制閘門**（非建議）標準不同 |
| 因果鏈/多步驟推理 | 「先結果後解釋」重排可能丟失條件從屬關係 | 「multi-step sequences where fragment ambiguity risks misread」有退回清單 | 同上，靠模型自判 |
| claim 標籤（如 workspace 慣用 `[claim:*]` 或 evidence-tier 標記） | 未在 caveman 保留清單中提及此類 workspace 專屬標記 | 無 | **workspace 專屬缺口，caveman 原生不知道** |

### 3.2 失真的重問成本何時吃掉節省
- Caveman 自報開銷：skill 本身 +1–1.5k input token/turn（`README.md` 誠實揭露）。
- 若壓縮造成**一次**因數字/否定詞失真而觸發使用者重問澄清，重問成本 ≈ 原本完整回答的 token 量（使用者需重新描述疑問 + 模型重新展開解釋，通常比原始未壓縮回答更長，因為要先確認「你剛才是不是說反了」）。
- 粗估平衡點：以 README 65% 平均壓縮、294 token 均值輸出估算，一輪失真重問的額外成本（重新提問 + 完整展開解釋，估 ≥800–1200 token）即可抵銷 **3–4 輪**正常壓縮的淨節省。壓縮強度越高（ultra/wenyan）失真機率越高，此平衡點對高壓縮級距更不利——**壓縮強度與失真風險非線性，但 caveman 無數據回答「多高的壓縮級距開始邊際失真成本超過邊際節省」**，此為方法論缺口（見 Unknowns）。

---

## 4. 改良設計草案（僅供提案，非 SKILL 檔）

> 命名建議：`output-compress`（暫定，避免與上游 caveman 品牌混淆；若之後實際借用其 slash command 語法可協商命名）。以下為**報告內草案結構**，非 `.claude/skills/` 實體檔案。

### 4.1 保重點不變式白名單（永不壓縮）

繼承 `caveman-compress` 既有清單（code block／inline code／URL／file path／command／proper noun／date／version／env var）並**擴充 workspace 專屬項**：

1. 檔案路徑、error string、指令輸出逐字（同 caveman）
2. **所有數字**（百分比、金額、版號、行號、日期）——不只結構元素，敘述句中的數字也鎖定
3. **否定詞與其作用域**（不/非/禁止/never/unless/except）——片段化時該子句整句保留，不允許連接詞省略
4. **[claim:*] / evidence-tier / [KU|UK|UU] 等 workspace 既有標籤系統**（`research/reports/` 慣例）
5. 安全紅線語句（`core.md`「不可逆操作」「P0」相關措辭）——不只語氣退回，整段禁止壓縮
6. `Done-when` / `Return {}` / 任務契約關鍵欄位（`subagent-strategy.md` Handoff Contract 格式）

### 4.2 模型檔位適配壓縮強度矩陣

對應 `.claude/refs/model-profiles.md` §1 檔位詞（cost/quality/ceiling/frontier），**核心原理引用 core.md「雙軸伸縮」鐵律**：行為指導量與能力成反比——弱模型需要更多冗餘（顯式重複、結構化格式）才能不失真，強模型可承受更高壓縮。

| 檔位 | 建議壓縮上限 | 理由 |
|---|---|---|
| cost | `lite`（僅刪填充詞，保留完整句/冠詞） | 弱模型對片段化語意重建能力弱，`model-profiles.md` §1 已標「cost 檔位行為指導密度=高（步驟級指示）」——壓縮與此矛盾，故上限最低 |
| quality | `full`（預設，刪冠詞+片段化） | 對齊「行為指導密度=中」，caveman 預設級距本就以中階模型測試（`claude-sonnet-4-20250514`）校準，符合 |
| ceiling | `ultra`（連接詞可省） | 「行為指導密度=最低（目標級）」，強模型語意重建能力足以補回省略的邏輯連接 |
| frontier | `ultra`，**但 wenyan 系列預設禁用** | wenyan 改變輸出語言風格，與「對使用者最終回應維持繁中」鐵律衝突（見 §2），若使用者顯式要求文言則需另立例外，非自動套用 |

**非 Claude 模型**：比照 `model-profiles.md` §6「非 Claude 模型接入程序」，初始一律鎖 `lite`，跑 5–10 代表任務校準後才可調高，不可沿用 Claude 校準值。

### 4.3 失真閘（機械驗證，非模型自評）

呼應 core.md「判斷 vs 決定」公理——是否失真的**偵測**用確定性程序，不靠模型自評「meaning stays clear」（caveman ultra 級原句的自我判斷正是本設計要避免的模式）：

1. **Key-fact extraction diff**：壓縮前後分別跑一次結構化抽取（數字、檔案路徑、否定子句、專有名詞）成 JSON，diff 兩份 JSON——不等於 → 壓縮失敗，自動退回上一級重試（借用 `caveman-compress` 既有「失敗重試兩次」機制，但**判準從演算法保留清單擴大到語意抽取 diff**）。
2. **確定性 checklist（非 LLM judge）**：白名單第 2–6 類（數字/否定詞/標籤/安全語句/契約欄位）用 regex 抓取兩版本出現次數與內容比對，不用 LLM 二次判斷是否「意思一樣」（避免 judge 噪音，呼應 `model-profiles.md` §5 O15 教訓）。
3. **三臂 eval 借用 + 加保真軸**：沿用 caveman `baseline / terse-control / skill-arm` 三臂設計，但每臂新增第四維度分數——「保真度」（用 1 的 JSON diff 結果算命中率），不能只看 token 節省率；落地前須在 workspace `research/evals/` 建對應 fixture。
4. **壓縮強度與失真率的邊際曲線**：落地前需实测（非本報告臆測）不同檔位在不同壓縮級距下的失真率，找出 §3.2 所述「邊際失真成本超過邊際節省」的實際轉折點，作為 4.2 矩陣的最終校準依據（目前矩陣是依 core.md 雙軸伸縮公理**推導**，非实测，須標記為草案）。

### 4.4 適用/禁用場景（Do / Do NOT）

**適用**：
- 內部 scratchpad／sub-agent 中間輸出／機械化報告的正文敘述段落
- 對已熟悉領域使用者的例行技術問答（bug fix 說明、log 解讀）
- 記憶檔（`memory/MEMORY.md` 類）非決策段落的壓縮（仍需與既有 `memory-compactor` 分工，不重疊）

**禁用（Do NOT use for）**：
- 對使用者的最終回應中**改變語言**（wenyan 模式）——違反 `output-discipline.md`「不 silent fork 繁中鐵律」
- 安全紅線語句、不可逆操作確認、P0 報告（`core.md`）——**這些已有更嚴格的強制格式要求**（摘要+等待確認），壓縮與此格式要求衝突，且失真代價（誤判可逆性）不可承受
- 正式 Handoff Contract / Done-when 條款（`subagent-strategy.md`）——契約類文字的精確性本身就是契約，壓縮即改變契約語意
- 稽核/审查類輸出（`security-reviewer`／`reviewer` agent 產出）——finding 必須逐字可追溯到 artifact，壓縮片段化會削弱可稽核性
- 弱檔位（cost 級）且任務屬「off-rails」（空間常識/無 spec 推斷，見 core.md OBSERVE）——弱模型本已需要更多顯式指導，壓縮方向相反

---

## 5. 結論與建議路徑

**條件可行**。理由：
- Caveman 提供的壓縮**語法規則**（刪冠詞/填充詞、片段化、分級）與 workspace `output-discipline.md` 精神一致，可作為「量化分級」的參考起點，非全新概念。
- 但其兩大缺陷（零保真評分、零模型檔位適配）若原樣移植，會直接違反本 workspace 兩條既有鐵律：core.md「雙軸伸縮」（壓縮強度必須隨檔位反向調整，caveman 沒有）與「判斷 vs 決定」公理（失真偵測不可靠模型自判「meaning stays clear」）。
- §4 草案已示範如何用 workspace 既有機制（`model-profiles.md` 檔位表、`core.md` 白名單/閘門公理、`research/evals/` 三臂 fixture）修補此二缺陷，技術路徑清楚，非阻塞性未知。

**建議路徑**（若使用者核准）：
1. 不直接 fork caveman 原始碼/安裝其 npm 套件——改為在 workspace 內以 §4 草案為 spec，走 `harness-meta` skill 的 `add-skill-REFERENCE.md` 流程新增 SKILL（`/harness-meta` → add skill 子流程），確保與既有 28 skills 命名/觸發詞不衝突。
2. 落地前**必須**先建 §4.3 三臂 + 保真軸 eval fixture 並实测 §4.2 矩陣（目前矩陣為推導草案，非验证值），依 `model-profiles.md` §2.6 Per-Model Eval Baseline 既有方法論擴充，不可未验证就写入规则。
3. 與現有 `output-discipline.md` 分工：`output-discipline.md` 保留**定性**規則（無開場白/填充語禁止類，L1 零數字鐵律不變）；新 SKILL 承載**可選用、分級、需顯式啟用**的量化壓縮機制（類似 caveman `/caveman <level>`），預設不啟用，避免與 L1 auto-load 行為疊加造成雙重壓縮或衝突。
4. wenyan 類語言改寫模式**明確排除**於首版落地範圍，若未來要做需另立提案並處理與繁中鐵律的衝突。

---

## Unknowns

- **[KU]** §3.2 的「3–4 輪節省抵銷」估算為本報告基於 README 揭露數字的粗略推導，非实测；落地前須用 §4.3 的 fixture 实际测出失真率與重問成本，不可直接採信本報告的估算值作为最终参数。
- **[KU]** caveman README 引用「2026 年 3 月論文顯示限制大模型簡短作答可提升準確率約 26 個百分點」，本報告**未**查證該論文出處與方法論（超出本次 allowed-paths 與時間範圍），此數字目前只是二手轉述，若要在改良設計中援引須先獨立查證原始論文。
- **[UK]** workspace 是否已有人手動試過在特定 sub-agent（如 `memory-compactor` 或 `doc-writer`）套用類似壓縮風格但未正式記錄？若有，本提案的 §4 可能與既有隱性做法重複，建議落地前先問使用者。
- **[UU]** caveman 的三個 hook（SessionStart/UserPromptSubmit/Statusline）與本 workspace 既有 22 個 hooks 是否有掛載點衝突或觸發順序依賴？本報告只讀了 caveman 端架構，未交叉核對 workspace 現有 hook 清單（`AGENTS.md` 提及 22 hooks 但本次未逐一核對掛載點），若真的落地需先跑 hook 相容性檢查，此為未主動排查的盲點。

---

## 來源 URL 清單

1. https://github.com/juliusbrussee/caveman（repo 首頁 + 目錄結構）
2. https://raw.githubusercontent.com/juliusbrussee/caveman/main/README.md
3. https://raw.githubusercontent.com/juliusbrussee/caveman/main/skills/caveman/SKILL.md
4. https://raw.githubusercontent.com/juliusbrussee/caveman/main/skills/caveman-compress/SKILL.md
5. https://raw.githubusercontent.com/juliusbrussee/caveman/main/CLAUDE.md
6. https://raw.githubusercontent.com/juliusbrussee/caveman/main/benchmarks/run.py
7. https://raw.githubusercontent.com/juliusbrussee/caveman/main/AGENTS.md（確認為 @import 清單，無模型檔位內容）
8. https://github.com/juliusbrussee/caveman/tree/main/benchmarks（目錄結構確認）
9. https://github.com/juliusbrussee/caveman/tree/main/skills（目錄結構確認）

**workspace 內部對照來源**：`/home/user/cc-workspace/.claude/rules/core.md`、`/home/user/cc-workspace/.claude/rules/output-discipline.md`、`/home/user/cc-workspace/.claude/rules/subagent-strategy.md`、`/home/user/cc-workspace/.claude/refs/model-profiles.md`、`/home/user/cc-workspace/research/reports/2026-07-11-fable-token-efficiency.md`
