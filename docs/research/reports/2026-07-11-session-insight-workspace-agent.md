---
date: 2026-07-11
branch: claude/workspace-agent-architecture-b22p6z
session: 跨兩個 5h usage 窗（同一 remote session 延續）
topic: workspace-agent-architecture 全案單日交付——Fable 協調 × 多模型實作的完整實錄
type: session-insight
---

# Session Insight 2026-07-11 — Workspace 智能體化全案

> 從一句「我想讓 Workspace 更像一個智能體」到 129 commits 的單日全案。本檔 = 完整實錄 + 可複用洞見，
> 依 The Loop 六階段組織；數字全部可由 git log / evolution/*.jsonl / compress-log 重測。

## 0. TL;DR（十行版）

單一 session（跨兩個 usage 窗，**129 commits**）交付：**SPEC 計劃書 ×2**（智能體化 + token 效率五層）、**AgentEngine**（contract 13 ops → REST×7 + MCP server 六 tools + CLI + 多裝置 token）、**KYU 作業系統層**（Routine 三掛點 + 失真閘 + 終盤點 25 需求矩陣）、**SIA 全 Routine 化**（evaluate.py ×3 + Routine G + trigger 全指針化 ×7 + heartbeat 退化偵測）、**output-compress SKILL 雙版本**（workspace v1.0.1 + dist 可攜版）、**SwiftUI client**（iOS 五頁 + macOS menubar，程式碼全交付、編譯待 Mac）、**hook 工程**（Stop 27.9s→81ms、UPS 276→129ms）、**Usage Pacer 五檔配速**（含 auto-handoff/resume + HANDOFF_HALT 斷路器）、**部署 runbook**。協調模式 = Fable orchestrator + 17+ quality/cost workers；期間 2 個 worker 死亡驗屍、6 次 worktree stale-base 搶救、失真閘 4 次真實攔截。cache_hit_ratio 全程 0.976-0.984。

## 1. 交付清單（五標籤完成度）

| 交付 | 標籤 | 驗證錨點 |
|---|---|---|
| SPEC.md + 7 份設計文件 | autonomous_verified_success | healthcheck FAIL=0、§9 全程進度 |
| AgentEngine REST ×7 + sanitize 安全修復 | autonomous_verified_success | vitest 26/26、tsc、E2E 30/32 |
| MCP server（六 tools thin-proxy） | **assisted**_verified_success | tsc + tool 對照親驗；**wrangler dev handshake 由 E2E worker 驗**、未部署 |
| SIA 量化閘 ×3 + Routine G | autonomous_verified_success | evaluate.py 對真實產出 0.83-0.90；G trigger 已建 |
| Trigger 全指針化 ×7 | autonomous_verified_success | list_triggers 快照對帳、D delete+create、G 新建 |
| output-compress workspace v1.0.1 | autonomous_verified_success | 失真閘正反例 exit 0/1、7 維 Tier A、compress-log 12+ 筆 |
| output-compress dist 版 | assisted_verified_success | worker 驗證 + 主樹 grep/py_compile 重驗（Phase 3 同步進行中） |
| SwiftUI 骨架 | **unverified**（誠實標注） | 容器無 Xcode——結構/YAML/brace 驗證而已，Mac 編譯待使用者 |
| hook 三優化 P1/P2/P3 + UPS 合併（W12） | autonomous_verified_success | 延遲複測 81ms/129ms/42ms、verify-telemetry 9/9、測試 7/7+91/91；<80ms 未達（殘餘成本在授權範圍外，誠實上呈） |
| Usage Pacer W6/W7/W8 + N2 斷路器 | autonomous_verified_success | self-test 5 情境（含 HANDOFF_HALT）、本窗 live 裁決 AHEAD +18pp 正確、W8 注入節流實測 |
| 多裝置 ingest token（BS-5） | autonomous_verified_success | vitest 33/33（+7 案）、tsc、fallback 零影響 |
| KYU 終盤點（N1-N6） | autonomous_verified_success | 25 需求 23✅/2🟡；6 新卡 5 修 1 backlog（kyu-final-review.md） |

## 2. 協調模式實錄（orchestrator 經濟學的一天）

- **分工實況**：Fable 只做——架構決策、Routine prompt/`.claude/` 高風險修改、確定性 gate 親跑、終審、驗屍搶救；其餘全下沉 quality/cost worker（researcher ×5、implementer ×9、security-reviewer、doc-writer、reviewer、test-writer、general E2E）。此即當日稍早才寫入 profiles §2.8 的 orchestrator 模式（96%/46%）的即時自我應用。
- **worker 失敗率與處置**：2 個死亡（MCP、單測——transcript mtime 停滯為判準，SendMessage 對死者無效）→ 驗屍 worktree 搶救 + Fable 親補殘件；3 個 stale-base（worktree 基底 = main 而非 feature 分支，**單日第 4-6 次重現**）→ 3-way apply 流程全部 clean。**教訓固化：worker 產物一律「機械收整 + 主樹 gate 重跑」，从不直接採信**——本日兩個 agent 遺留 bug（vi.mock arrow 不可 new、TDZ）都是主樹重跑抓到的。
- **verdict 非證據的實戰配額**：security-reviewer 的 P1 主張 → 主樹 grep 覆核後才修；KYU reviewer 的 BS-1「Critical」→ list_triggers 實測後**降級 Med**（指針式 trigger 早已消解大半風險）——盲點卡也要過機械對帳，這是雙向紀律。

## 3. output-compress 實測（本 session 最重要的一手數據）

- **終帳（13 筆 organic）**：13,837→12,021 bytes（**-13.1%** ≈605 tokens，CJK ≈bytes/3 估）；pass 9/fail 4。**注入節流帳另計**：W8 首次全文/之後短版 + PACE 變化才注入 → 20-turn 注入稅 3,000→~500 tokens（**-83%**，機制層省的是每 prompt 恆定稅，複利大於單筆壓縮）。
- **CJK 現實**：full 級對繁中 prompt 實測節省 **9-18% bytes**，與上游 caveman 英文自報 65% 差距巨大——結構性原因：CJK 無冠詞、填充詞密度低。**任何「省 65%」的宣稱在 CJK 語境都要打三折以下**。
- **失真閘 4 次真實攔截，全是同一型**：改寫句式動到否定詞（「而非→不包」「不存在→缺」）——催生 G5 鐵則「**壓縮 = 刪除，非改寫**」。這是純機械 gate 教會模型寫作紀律的實例：閘門不是形式，第一天就抓到真問題並回饋成規則。
- **AUTO 機制演進三段**：SessionStart 單次注入（會失憶）→ 每 prompt 注入（compact 免疫）→ W8 節流（首次全文/之後短版 + PACE 變化才注入，20-turn 注入稅 3,000→~500 tokens）。**advisory 的正確形態 = 常駐但極簡**。
- **誠實邊界**：本 session 的 organic 節省仍是「派工 prompt」單一場景；Routine 產出（L3 掛點）明日才開始累積；bytes ≠ tokens（CJK 3 bytes/字），真實計費節省待 tokenizer 級量測（plan §5 [UK]）。

## 4. Hook 工程數據（22→21 hooks 全量量測後的三個修復）

| 熱路徑 | 前 | 後 | 方法 |
|---|---|---|---|
| Stop（每 turn） | **27,926ms** | **81ms** | heavy_tail setsid 背景 + flock；stdout 語義不變；verify-telemetry 9/9 守住 telemetry 正確性 |
| 每 prompt（UPS） | 276ms | 129ms（W12 三 python3 合併後終值） | 快取新鮮度判斷 + --no-live + 三呼叫合併；裁決 100% 留 SSoT——**快取「取數」永不快取「裁決」**；<80ms 殘餘成本在 guard 呼叫（範圍外，EVOLUTION 候選） |
| 每 Bash PostToolUse | 67ms | 42ms | tool-log×monitor 合併（async→sync 是必要語義變更，非純重構——量測反推出的既有設計事實） |

洞見：**延遲稽核自己也會誤診**——P2 原判「網路呼叫」，worker 直接量測推翻（fetch 早有 60s 快取，真兇是 live-scan）。優化前先量測組成，不信報告字面。

## 5. Usage 治理三件套（本日從 0 到閉環）

1. **Pacer 五檔**（AHEAD/ON_PACE/BEHIND/HANDOFF_PREP/HANDOFF_HALT）：官方 util% × 窗內時間比，10min TTL，advisory 永不阻斷。上線第一個 verdict（AHEAD +18pp）即正確且被本 session 自己遵循（新 fan-out 降檔、收整優先）。HALT 斷路器（N2）：連續 ≥3 窗撞頂 → 只交接不喚醒，防 goal-drift 燒穿多窗。
2. **Auto-Handoff/Resume**（W7）：HANDOFF_PREP → handoff skill + `send_later` 排 reset+3min **同 session** 自我喚醒——cache prefix 不破，接續成本僅增量。上一窗的 91%→handoff→reset 後 resume 正是此流程的手動預演，本日機制化。
3. **高用量的測試假失敗**：usage-gate 測試在官方 94% 時段假失敗（v3 官方權威 vs 測試漏設 OFFICIAL_DISABLE）——**環境敏感測試必須顯式隔離環境訊號**，clean-tree 重現是歸因第一步。

## 6. KYU 框架的實戰回報（不是儀式的證據）

- T1 Blindspot（ceiling fresh-context）產 8 卡，其中 BS-3（README/實作格式矛盾→parser 恆 null）、BS-2（409 靜默丟失）當日修復；BS-1 經疆域實測降級——**盲點卡的價值在「沒想到要問」，但嚴重度要機械覆核**。
- Unknowns 區塊掛進 A/C/F + evaluate.py 機械驗證（m_unknowns_*）——反空儀式條款（寫不出就寫最弱假設）+ 30 天落日（2026-08-10 複查）是防「KYU 變表格填空」的兩道保險。
- 本報告自身的 Unknowns 見 §8。

## 7. 可複用 Playbook 候選（供 dreaming-consolidator）

1. **Worker 驗屍三步**：transcript mtime 判生死 → worktree 產物盤點 → 3-way apply（diff 對其基底）+ 主樹 gate 重跑。
2. **安全 hook 假陽性處置**：不整批放行；逐型態論證（flock 駁回=wrapper 繞過面）+ 修正規化層讓危險輸入**更**可見（subshell 剝殼）+ 測試固化 86→91。
3. **cwd 陷阱**：長 session 中 `cd portal` 殘留 → healthcheck 空跑假陰性——**gate 命令一律絕對路徑或開頭 cd root**；pre-commit hook 用 $CLAUDE_PROJECT_DIR 故為權威。
4. **對接外部資料前先 cat 實檔**：官方 usage 快取 schema 是平面鍵（five_hour_pct），設計時憑想像寫巢狀解析 = 第一次 live 就 NO_DATA。
5. **每完成一項即 commit+push**：本 session 129 個小 commit，兩次 usage 撞頂/一次 session resume 均零損失。
6. **KYU 終盤點雙軌**：機械覆蓋矩陣（需求原話 vs 交付逐條對帳）+ fresh-context 終掃（只找新盲點）——N1-N6 六卡五修同日，殘餘 unknowns 每條有負責機制、無無主項。

## 8. Unknowns（本報告自身，KYU 規格）

- [KU] Pacer 的 ±15pp 門檻與斷路器 N=2 皆初值——需 2-4 週實際窗數據校準（誤觸發率/漏觸發率），Routine G 可順帶彙總。
- [KU] W7 auto-resume 未經真實 HANDOFF_PREP 觸發的端到端演練（本窗未撞 90%+0.5h 條件）——首次真實觸發時的 send_later 排程需人工確認一次。
- [UK] 隱性假設「同 session 續跑必然比新 session 便宜」——若 resume 時 context 已近上限，compact 成本可能吃掉 cache 節省；未量測。
- [UU] 15+ worker 的 worktree 殘留（.claude/worktrees/ 8+ 目錄與其 origin 分支）未清理——磁碟與 remote 分支衛生是本日沒人問的問題 → 處置：列 backlog（低風險，worktree 未變更者 harness 自動清）。

## 9. 下一步（SSoT = SPEC §9 + MEMORY 待辦）

部署照 `clients/DEPLOY-RUNBOOK.md`（secret 順序 + 60 秒冒煙）→ Mac 編譯親驗 → Pacer 門檻校準 → 複查檢查點（N3 重錨：`days_since_first_organic ≥ 30 AND n ≥ 門檻`，資料不足順延不降級）→ N5 pending-sentinel backlog → worktree 分支清理（待使用者確認）。

## 10. 追記（2026-07-12）——翌日實證：協調模式重演 + 兩個結構性發現

> Branch `claude/portal-150-usd-correction-lrrnqs`（361b23e/2988e0f/a685fff）。本節 = 上述 playbook 在次日獨立 session 的重演與回饋。

### 10.1 校準翻案：$150 → 官方-first + 動態推估（本報告 §5 的直接續集）

- **舊 $150 假設值的死法**：官方 5h 是**固定重置窗**（有 resets_at）、本地是滾動窗——兩窗不對齊時單點校準在 $66〜$1,694 間漂移 27×。任何寫死 USD 常數都會再死一次 → portal 改官方 utilization 官方-first（5h+7d 兩 bar），USD 額度改「官方窗對齊動態推估」。
- **舊校準樣本被翻案**：07-10「11× 高估（隱含 $1,694）」樣本落於 cost-log 壓實（1,912→718 列去重）**之前**，高估主因疑為重複列污染（標注未驗證）；2026-07-12 新樣本**自洽**（官方 73% × $66 ≈ 本地對齊窗 $48.42）→ 5h 實際額度 ≈ **$66**、7d ≈ **$3,552**。**方法論**：校準樣本要做自洽性檢查（pct × 推估額度 ≈ 本地實測），不自洽的樣本先查資料層污染再查算法。
- `fetch_official` SSoT 移 usage-report.py、`--json` 內嵌 official 快照（portal deploy host 無 token，快照必須容器端內嵌）——「對接外部資料前先 cat 實檔」（§7-4）再次應驗：resets_at 是裸分鐘 UTC 無時區後綴，JS 直接 new Date 會按本地時區靜默位移。

### 10.2 Pace 的結構性盲區：燒速 ≠ 水位（§5-1 的補丁）

live 實證：util 83%、窗過 ~80% → delta +3 = ON_PACE **零觸發**，反而使用者先開口「超過 80% 記得動態調整」。pacer 五檔全看燒速/交接，沒有「絕對水位」軸 → 增 `compress`/`compress_msg` 正交欄（≥80% AUTO 級距+1、≥95% 升檔位上限，plan §6-7）。**同日自我應用**：機制上線當個 session 即在 80→95% 爬升中連續生效（fan-out 降 quality、對抗審查降級為語義測試+親審、逐項 commit——偏離全記錄在 commit）。

### 10.3 協調模式重演的差異數據（vs §2）

- implementer ×2（worktree 隔離）+ quick-code-reviewer ×1：**零 worker 死亡、零 stale-base**（前日 6 次）——差異變因：feature branch 開工即與 main 同基底（d1b26b7），worktree 基底無落後空間。stale-base 是「長 session 內基底漂移」的函數，不是 worktree 機制本身的缺陷。
- 「worker 產物機械收整 + 主樹 gate 重跑」照跑（§2 教訓）：copy 前 `git diff --name-only base..HEAD -- <files>` 斷言零分歧，copy 後全部 gate 主樹重跑。
- **verdict 非證據雙向再驗證**：reviewer REVISE 的必修項（薄委派每 prompt 重複 importlib ×2）先機械重驗（grep 呼叫點 + 讀 assess 流程）才修——CONFIRMED；同時 reviewer 也替 coordinator 攔下自己 spec 裡的缺陷（薄委派模式是 coordinator 規格原文）。**審查抓的常是 spec 的錯，不只是 worker 的錯**。

### 10.4 本節 Unknowns（KYU 規格）

- [KU] $66/5h、$3,552/7d 仍是雙樣本推估（07-12 兩讀數）——待 portal 官方-first 上線後累積跨窗樣本自動校準；fallback 常數 65/3600 屆時複查。
- [KU] 壓縮升級的失真率是否隨水位觸發頻率上升——compress-log 已帶 level 欄，Routine G 週檢（plan §6-4 同款撤回條件）。
