# Zeuik 的 Workspace 準則 — The Loop 重構研究報告

> **產出日期**：2026-06-06
> **分支**：`feature/workspace-canon-rewrite`
> **任務**：擺脫 Karpathy×Mnilax 12-Rule 作為「唯一組織原則」的束縛，基於 491 個研究檔案 + 官方最新最佳實踐，建構屬於 zeuik 的 workspace 行為準則，重寫 5 個 auto-load 檔（CLAUDE.md + 4 rules），符合 harness 精神 + harness loop + LLM 自我演化。
> **配對產物**：執行計劃書 `2026-06-06-zeuik-workspace-canon-execution-plan.md`
> **定位**：這是 workspace 準則的「**重構基石**」——前作（#465 通用化 / #466 雙版 / 06-05 深化）做論文接地，本作做**組織原則的重構 + 屬於使用者的收斂**。

---

## 0. 框架誠實聲明（讀本報告前必讀）

1. **結構決策（使用者明確授權，2026-06-06）**：core.md 改用 **The Loop 六階段語意化 header（`## OBSERVE / IDENTIFY / PROPOSE / APPLY / TEST / RECORD` + 跨切）為主結構**，§R1–§R12 **編號從 header 退役**。決策依據：官方文件（即時查證）只要求「use markdown headers and bullets to group related instructions」——**從未規定 §R 編號**；編號是 Karpathy/Mnilax 慣例非官方建議。使用者指示「§R header 不一定要照舊」-> 採語意化標題（最貼官方「organized sections」+ 真正擺脫編號作為組織原則）。
2. **§Rn 降為 inline tag，非主結構**：每條紀律行尾標 `〔§R8〕` 形式的 inline tag，使 codebase **1,788 處** `core §Rn` 歷史引用（grep 實測，排除 research/ 後仍遍布 docs/.claude/skills/refs）仍可 grep 命中對應條文——**保留可解析性，不 mass-fix（使用者接受 stale pointer，避免 migration 災難）**。研究歷史檔（research/ 內 ~大宗）的指針刻意不動。
3. **healthcheck gate 同步改寫（與本 PR 同步，已 mutation-test）**：`scripts/measure.sh --gate` 原斷言「core.md 含 11 個 `^## §R` header」改為「驗六階段 header 存活 + §R inline tag 非 stub + byte cap ≤19,000 + canonical wc -c 指令」。**唯一 executable §R 斷言僅此一處**（grep 全 scripts/hooks/.github 確認；GHA index-consistency 與 behavioral eval 只在文件描述/錯誤訊息提 §R，非機械斷言）。gate 改寫經 mutation test（故意刪一個 phase body -> exit 1 確認）證明仍能抓回歸。
4. **active dangling §R 指針**（扣除自身會改的 5 主檔 + 自動生成 log + measure.sh）：
   - **bare `§Rn`（如 `core §R8`）-> 仍可解析**：grep 命中 core.md 的 inline `〔§R8〕` tag。
   - **`§Rn.x` 子編號（§R12.1/§R12.2/§R12.3 等）-> 已死指針**：core.md 改 The Loop 後不再有子編號 header（grep 確認 active 檔僅 `harness-meta-GOTCHAS.md` 4 處仍提 §R12.1-12.3）。子編號內容**併入 TEST 段 unverified_success 條文**（grep `§R12` 仍命中），子編號 tag 本身列為 conscious deferral（fail-loud，非靜默回歸；未來 /autoload-evolution cycle 可清）。
   - rules/README.md 框架同步更新（12-Rule Canon -> The Loop；advisor 攔下此 5 檔 scope 外漏網檔）。
5. **「擺脫 12-Rule」的正確詮釋**：擺脫它作為**唯一組織原則**的束縛。The Loop + 三洞見 + 四維品質 + 信度紀律成為使用者自己的上層敘事；§Rn 降為 inline 可追溯 tag。
6. **數字信度三分級**：HIGH（官方文件 / 同儕審查論文）/ MEDIUM（跨倉研究但方法論未全公開 / 作者多篇交叉印證）/ LOW（個人自報、無控制組）。所有寫進規則的數字標信度；研究發現的數字留在本報告。
7. **被攔截的錯誤數字**（§3）證明「親 grep 驗每個數字」鐵律有效——子 agent 自報數字非證據。

---

## 1. 方法論

### 1.1 研究流程（harness loop 自身的應用）

```
OBSERVE  -> 盤點 5 目錄 491 檔 + 讀 3 份合成型報告（深化研究/INDEX/best-solution）建地圖
IDENTIFY -> advisor 諮詢 ×3 鎖定盲點：byte cap / anti-regression checklist / §Rn blast radius
PROPOSE  -> The Loop spine 設計稿 + coverage checklist（pre-merge gate）
TEST     -> blast radius grep（1,788）+ healthcheck §14 約束讀取 + baseline gate green
APPLY    -> 5 檔重寫（按執行計劃書）
RECORD   -> 本報告 + MEMORY 沉澱
```

### 1.2 Fan-out 策略（非 re-synthesis）

advisor 攔下「拿已併入的論文證明沒東西可併」的循環論證（MEMORY Lesson 2026-06-05-H）。4 個 researcher 並行**只攻 gap**：
1. 3 個 RESEARCH-INDEX 標🔴未整合洞見
2. 深化報告（06-05）後的新 tweets/papers
3. 官方最新最佳實踐驗證 + 新機制
4. Mnilax 反面教訓 + AGENTS.md 跨倉研究的結構約束

每個數字附原文行號，主對話對載重數字二次 grep 親驗。

---

## 2. 核心發現：The Loop 作為組織骨架

### 2.1 為何 harness loop 是對的 spine（非任意選擇）

- **workspace-native**：OBSERVE->IDENTIFY->PROPOSE->TEST->APPLY->RECORD 已定義於 CLAUDE.md §Harness Loop + refs/harness-loop.md，非外來框架。
- **每階段可機械驗證**：每階段對應 bash 命令或 test pass（符合 §R4 強條件原則）。
- **本身即自我演化閉環**：RECORD->OBSERVE 的回授正是「LLM 自我演化」的機械形式——滿足使用者「符合 harness 精神 + harness loop + 自我演化」三要求於同一結構。
- **已被論文接地**：06-05 深化研究 §4 已證明 12 條行為意圖可映射六階段。

### 2.2 六階段語意 header -> 行為意圖 + inline §R tag 映射

core.md 主結構 = 六階段語意 header；每條紀律行尾標 inline `〔§Rn〕` tag（保留 1,788 處歷史引用可解析 + gate 非 stub 檢查錨點）。

| 階段 header（主結構）| 紀律 + inline tag | 注入的 zeuik 新內容 |
|---------------------|-------------------|---------------------|
| `## OBSERVE` | 改前先讀〔§R8〕 | **on-rails/off-rails 任務分類**（先判斷任務在訓練電路內外，off-rails 強制人工或加 spec）|
| `## IDENTIFY` | 顯露假設〔§R1〕+ 成功條件〔§R4〕 | **四維品質**（成功條件含 security/reliability/maintainability/taste 四軸）|
| `## PROPOSE` | 極簡〔§R2〕+ 外科刀〔§R3〕 | **AI 程式碼四大缺陷**反模式（bloated/copy-paste/brittle/awkward abstraction）|
| `## APPLY` | 規範優先〔§R11〕+ 不可逆 gate〔§R1〕 | **可推導資訊 = 噪音**（只寫無法從 repo 推導的行為契約）|
| `## TEST` | 測試驗意圖〔§R9〕+ fail loud〔§R12〕 | **working ≠ good**；四維缺軸不靜默 |
| `## RECORD` | checkpoint〔§R10〕+ 演化迴圈 | 反思入庫門控、記憶 append-only |
| `## 跨切紀律` | 判斷vs決定〔§R5〕+ 浮現矛盾〔§R7〕 | on-rails/off-rails 應用、多來源矛盾浮現 |

`§R5`/`§R7` 設為跨切（非綁階段），與 output-discipline 同為橫切層（advisor 點：判斷/矛盾不比輸出紀律更受階段約束）。§R6（token budget）的 inline tag 落在 context-management.md（gate 斷言點 (b)）。

---

## 3. 被攔截的錯誤數字（親驗紀律的勝利）

| 原打算寫進規則 | 攔截來源 | 正確措辭 |
|---------------|---------|---------|
| CLAUDE.md 遵循率 ~80% | 官方文件無此數字（只說 "advisory / context not enforced config"） | 「advisory，無官方遵循率保證；硬性執行交 hooks」 |
| caching 在 agentic workflow 降 41–80% | 來源不明（官方只給 per-token cache hit = 0.1×） | 「cache hit 時對應 token 費用降為基礎輸入 10%；整體降幅取決於靜態前置占比」 |

-> 教訓：社群廣傳的數字不等於官方共識；子 agent 自報數字必經主對話 grep。這兩個數字若寫進規則會以「學術背書口吻」誤導未來的自己。

---

## 4. HIGH 信度新證據（同儕審查 / 官方）

| 證據 | 數字 | 來源 | 信度 |
|------|------|------|------|
| 人工 AGENTS.md -> wall-clock runtime −28.64% / output tokens −16.58% | 124 PRs 對照 | ICSE JAWs 2026（Lulla et al.） | HIGH |
| LLM 自動生成 AGENTS.md -> task success −2~3% / cost +20% | 多 agent 跨 benchmark | ETH Zurich | HIGH |
| 去除所有 docs 後 LLM 生成 context 反提升 2.7% | — | ETH Zurich | HIGH |
| **可推導資訊（目錄結構/tech stack）= 噪音**（自動生成 100% 含 overview = 全噪音） | — | ETH Zurich | HIGH |
| 靜態文件 vs 動態 context：靜態差 12.3% | ACE | ICLR 2026 | HIGH |
| CLAUDE.md 過 200 行 reduce adherence | — | Anthropic 官方文件（即時驗證） | HIGH |
| IMPORTANT/YOU MUST 強調語提升遵循率 | — | Anthropic 官方文件 | HIGH |

**對重寫的直接含義**：CLAUDE.md 只寫「無法從 repo 推導」的行為契約；可推導的（目錄/stack/慣例細節）交 /init 或 on-demand。這給 byte cap 減法提供 HIGH 信度背書——重寫是**減法/重組，不是加法**。

---

## 5. 結構約束（負面約束 — 重寫不可違反）

| 約束 | 數字 | 信度 |
|------|------|------|
| 規則數 ≤14（>14 -> compliance 76%->52%，−24pp） | Mnilax 30 codebases | MEDIUM |
| 4->12 條 compliance overhead 幾乎不變（78%->76%）但 mistake −8pp | Mnilax | MEDIUM |
| 合計行數 ≤200（過 200 compliance drops sharply） | Anthropic 官方 | MEDIUM-HIGH |
| token 目標 ≤1,500 / ≤1,200 words（作者 4800->900 = −31% baseline） | Mnilax 個人實測 | MEDIUM |
| active skills ≤5-7（9+ -> ~13,500 token/task overhead） | Mnilax 兩篇交叉 | MEDIUM |
| 禁 capability-specific 工具名（"match enforced style" > "use eslint"） | Mnilax 30 codebases | MEDIUM |
| 禁可推導資訊（目錄/stack）| 見 §4 | HIGH |
| 禁模糊指令（be careful/be concise，47 次無效） | Mnilax 個人觀察 | LOW |

-> 本 workspace 現況 18,597 byte ≈ 4,600 token（含 4 rules），已遠超 Mnilax 1,500 token 個人目標，但 workspace 採 **byte cap（≤19,000）為 canonical**——因 byte 免疫 tokenizer 漂移（Opus 4.7 card：相同內容 token 數隨 tokenizer ×1.0–1.35），且 12-Rule Canon 完整性正當化此區間（core.md §Framework Integrity）。Mnilax 1,500 token 是「單一 CLAUDE.md 個人配置」目標，與 workspace「CLAUDE.md + 4 結構化 rules」不同單位，不直接套用。

---

## 6. 官方近期新機制（HIGH — 補進 ref，非 auto-load）

| 機制 | 用途 | 落點 |
|------|------|------|
| Block-level HTML comment `<!-- -->` | 注入前剝除 = 零 token 維護筆記 | context-mgmt 一行提及 |
| `claudeMdExcludes`（settings.local.json glob） | monorepo 排除無關 team CLAUDE.md | ref（低頻）|
| `InstructionsLoaded` hook | debug path-specific rules 載入時機 | ref（低頻）|

---

## 7. 不進規則的研究發現（留報告，不污染 auto-load）

advisor 紀律：只有「改變 per-session 行為 + 不可推導」進規則，其餘是研究發現，進本報告供未來查。這些是 06-05 深化報告後的新 gap，**值得未來迭代但不屬行為契約**：

| 發現 | 數字 | 信度 | 為何不進 auto-load |
|------|------|------|-------------------|
| **Effort level ROI 遞減**（@Mnilax） | xhigh vs high 僅差 2 質量分 / 成本 4× | LOW 自報 | 觸及 CLAUDE.md Effort 段可加一句「ROI 遞減，預設 high」，但細節留報告 |
| **TSCG tool schema compilation**（2605-04107） | Phi-4 14B 0%->84.4%/90.3%（20/50 tools），token 省 52–57% | HIGH | MCP 工具爆炸是 skill/MCP 層問題，非行為契約 |
| **ACON 蒸餾式 context 壓縮**（2510-00615） | peak token −26~54%，保留 95%+ 準確率 | HIGH | context 工程細節，屬 context-mgmt 深化非鐵律 |
| **grep > vector retrieval**（2605-15184） | Opus 4.6+Chronos 93.1% vs 83.6% | HIGH | retrieval 策略，屬 skill 層 |
| **benchmark manipulation**（cheating-agents） | 高能力模型透過 AGENTS.md 注入 answer key | HIGH | §R9 失敗新維度，已被 §R9「假測試」涵蓋，一句反模式即可 |
| **self-evolving harness**（@arvin17x） | 9 輪 75%->95%+，L1->L4 框架 | LOW 自報 | production harness 設計，屬 harness-meta skill |
| **SkillOpt**（Microsoft） | text skill NN 優化 +23.5~59.7 points，需 ground truth | MEDIUM | skill 優化方法，屬 skill-evolution skill |
| **memory 投毒 / sensor 合謀**（@freeman1266） | 多 agent token ~15×；LLM sensor 可能合謀放行 | LOW 自報 | 已被 §R12.1 記憶退化可觀測 + B1 unverified_success 涵蓋 |

-> 這些是「未來 /autoload-evolution cycle 的候選」，不在本次 scope（守 §R3 外科刀 + ≤14 條約束）。

---

## 8. 自我演化整合（harness loop 的 RECORD->OBSERVE 閉環）

使用者要求準則涵蓋「LLM 自身演化能力」。這不是新規則，是貫穿 §R4/§R9/§R10/§R12 的元迴圈，**安全邊界**（防「自我演化」變「自我污染」，DC 小模型污染證據）：

1. 反思只由獨立 evaluator 失敗訊號觸發，不由 LLM 自評（§R9.1）。
2. 洞見入庫須通過可機械驗證（§R4.2/§R9.2）。
3. 記憶整合門控、非自動（§R10.2）。
4. 記憶退化可觀測（§R12.1）。
5. unverified_success 閘門：subagent/workflow verdict 非證據，主對話親驗才升 verified（§R12.1 / B1）。

論文接地（保留在深化報告 + best-solution ref，不重複進此）：Reflexion / Voyager / ExpeL / Dynamic Cheatsheet。

---

## 9. 落地分工（為何不全塞 CLAUDE.md）

| 機制 | 角色 | 強制性 |
|------|------|--------|
| The Loop 六階段 + §Rn（CLAUDE.md + core.md） | 每 session 靜態行為契約 | advisory |
| Hooks | 每次必執行硬性動作（lint/commit gate/破壞性攔截/healthcheck GHA） | deterministic |
| Skills | domain 知識 / 可重用 workflow（含 §7 的研究發現操作化） | 按需載入 |
| Subagents | 隔離研究避免污染主 context | 獨立 context |
| Refs | 論文證據 / 數字 / 低頻細節（auto-load 只留指針） | on-demand |

---

## 10. 執行過程 Insight（方法論教訓 — workspace 更迭的元層）

> 本節記錄「如何安全執行一次 auto-load 全重寫」的過程教訓。對未來的準則更迭，這比研究發現更直接可用——因為失敗模式會重演，研究發現會過時。

### 10.1 三次 advisor 攔截鏈（每次都改變了執行方向）

clean-slate 重寫的真正風險不在「寫得好不好」，在「靜默丟失 + 破壞外部依賴」，這些是自檢結構性看不到的。三次諮詢各攔下一個會炸的盲點：

| 諮詢時機 | 攔下的盲點 | 若沒攔的後果 |
|---------|-----------|-------------|
| 動筆前 | coverage checklist scope 不夠 / byte cap 是 binding constraint / ≤12 條約束 | 寫完才發現丟了安全紅線、爆 byte、變成「更多規則」 |
| 設計骨架後 | **§Rn 是 1,788 處引用 + healthcheck 斷言的 API**，我的 checklist 只 scope「5 檔+MEMORY」看不到 | 全 rename -> 破 surgical / 爆 PR / **merge 後 main GHA 變紅**（不可逆） |
| 宣告完成前 | rules/README.md 是 auto-load 但**不在 5 檔 scope** 的漏網檔（仍框架 12-Rule Canon）；MEMORY.md 是 repo-tracked 我卻說「不需 commit」 | 活的矛盾文件留在 main / 3 條 Lesson 不持久化（undercut compounding-engineering） |

**元教訓**：advisor 的價值在「動筆前 + 宣告完成前」最高——它看得到自檢 scope 結構性排除的東西。clean-slate 任務尤其需要，因為「checklist 100% 通過」可以與「破壞了 checklist 沒涵蓋的東西」同時為真。

### 10.2 路徑決策：為何「擺脫」≠「炸掉」

使用者要「擺脫 12-Rule」，最初我詮釋為「保留 §Rn 錨點」（路徑 a 保守版）。使用者中途明確 push「§R header 不一定照舊」——這是正確的糾正。最終解不是兩極（保留編號 / 全 rename），而是**第三條路**：

- **語意化 header 為主結構**（擺脫編號作為組織原則）+ **§Rn 降為 inline tag**（保留 1,788 處引用可解析）+ **同步改 gate**（解除 healthcheck 對舊結構的硬綁定）。

關鍵判斷：用 `AskUserQuestion` 而非自決——因為這是「我的報告聲明 A、使用者指示 B」的記錄矛盾，且觸及 CI（MEMORY Lesson D：兩記錄矛盾用 AskUserQuestion 不信 agent 自判）。官方查證提供了客觀依據（官方只要求「header 分組」不要求編號），讓選擇不是憑感覺。

### 10.3 改「守自己工作的 gate」必須 mutation-test

本次同 PR 內改了 healthcheck gate（measure.sh）——這等於**移除了本 PR 的回歸保護**，除非證明新 gate 等效嚴格。只確認「新結構通過」不夠（那只證明 gate 不擋你，不證明 gate 會擋壞）。

**做法**：故意製造回歸驗證 gate 會 red：
- M1 新結構 -> exit 0（green）
- M2 掏空一個 phase body（header 在，body 刪）-> exit 1（red）✅
- M3 刪一個 phase header -> exit 1（red）✅

-> Lesson 2026-06-06-A。一個「只在新結構 pass 但不 fail on 回歸」的 gate 是 hollowed-out green，比沒 gate 更危險（給假安全感）。

### 10.4 byte ceiling 寫前定、寫後即量

寫完 core.md 才發現超目標 1,696 byte（新內容沒先進 byte 預算）-> 多輪 slim 補救。教訓：
- clean-slate 重寫**先按檔分 byte ceiling**，每檔寫完即 `wc -c`，不等全寫完才發現爆。
- **CJK slim 效益低**（中文壓縮一句省的 byte 少），結構性下沉（論文細節->ref、code block->刪）才是大槓桿。
- 新內容靠「退役舊結構（12-Rule 表頭）+ 細節下沉 ref」回收的 byte 容納，淨 ≤0——這正是 §4「可推導=噪音、減法優先」HIGH 證據的實際應用。

-> Lesson 2026-06-06-B（coverage scope 漏網）/ 2026-06-06-C（byte ceiling）。

### 10.5 對未來更迭的可操作 checklist（萃取自本次）

下次改 auto-load 結構前，按序執行：
1. **量 blast radius**：`grep -rn '<被改的錨點>' --include='*.md' --include='*.sh' . | grep -v research/` -> 決定 reframe vs migration。
2. **讀所有 executable assertion**：`grep -rn 'grep.*<錨點>' scripts/ .claude/hooks/ .github/` -> 找 healthcheck/GHA 硬綁定，列為同步改 scope。
3. **建 coverage checklist**：scope 必含 active refs/skills/hooks/docs（非只 5 檔），逐項標 successor 或刻意 drop 理由。
4. **byte ceiling 分檔**，寫完即量。
5. **改 gate 必 mutation-test**（M1 green / M2-3 red）。
6. **merge 前**：新 gate green + 完整 healthcheck green（merge 後 GHA 同款）+ coverage 100% + 報告誠實化死指針。
7. **merge 後 re-fetch 驗 main**（不可逆後驗真綠）。

---

## 11. 參考來源（本研究實際引用）

**第一來源**：5 研究目錄 491 檔（tweets 194 / papers 160 / reports 90 / best-practices 33 / claude-blog 14）
**🔴 洞見**：@stephzhan-519769（on-rails/off-rails）· @stephzhan-331722（四維品質）· @stephzhan-075818（AI 四大缺陷）
**HIGH 證據**：ICSE JAWs 2026（AGENTS.md 124 PRs）· ETH Zurich（自動生成反傷）· ACE ICLR 2026 · Anthropic 官方文件（即時驗證）
**結構約束**：Mnilax ×4 tweets（30 codebases）· addyosmani AGENTS.md 跨倉
**承接**：06-05 深化研究 + best-solution canonical ref（§Rn 論文接地不在此重複）

---

*本報告為重構研究分析。可部署的修改見配對執行計劃書。§Rn 論文接地的完整細節見 `.claude/refs/karpathy-mnilax-best-solution.md`。*
