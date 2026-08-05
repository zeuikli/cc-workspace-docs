# v4 Blindspot Pass — 四模型「還有什麼沒想到」審議報告

> 2026-07-19 · 框架：Know Your Unknowns（Johari 四象限）· 主席/終審：Fable · 三 lens：Opus（架構/理論）/ Sonnet（營運/落地）/ Haiku（消費端/最弱讀者）+ Fable 自提
> 對象：the-loop-harness-v4 全案（含 core.md 落地與四模型下沉決議）。參照語料：reports/best-practices/tweets/papers 四目錄（本 session 已全量消化）+ v3 遺產檔。

## 1. 盲點卡總表（終審裁決）

| # | 卡 | 提出者 | 象限 | 嚴重度 | 裁決 |
|---|----|--------|------|--------|------|
| B1 | harness-core/harness-meta SKILL + build-harness-export.sh + RESOLVER canonical 仍指 v3——新模型 onboarding 拿舊契約且無錯誤訊號 | Sonnet | KU | High | **本 session 已修**：四處改線 v4、export 重建（source = HARNESS-CORE-v4 + PROFILES-v3）|
| B2 | v4 換版無 rollback_signal——v3→v4 蒸餾本身是 consolidation，卻未套用自己的「保留 rollback」鐵律（遞迴盲點）| Opus | UU | P1 | **已修**：SPEC-v4 §6-3 補 rollback_signal |
| B3 | F11–F14 provisional 無到期提醒/owner——預設淪為永久 advisory | Sonnet | KU | P1 | 併入 backlog #3 並加到期機制需求（對照 session-init 的 eval 30 天提醒）|
| B4 | [claim:*] 三分類標籤在蒸餾中靜默蒸發（v3 EXPLAINER §6.1 可 grep 稽核機制）| Opus | UK | P1 | **裁決：刻意不復活入 L1**（byte 成本 + 未曾機械強制）；記錄於此為顯式決策非靜默流失；復活條件 = 有 hook 消費該標籤時 |
| B5 | 降級複審（弱檔跑機械 simplicity checklist 否決強檔 over-engineering）遺失——升級階梯的對稱另一半 | Opus | KU | P1 | 入 backlog：先驗 checklist oracle 資格（餵已知 over-engineered commit）再決定復活 |
| B6 | Dynamic Workflows 未被吸收為 L3 enforcement 基座——v4 §5 多條 advisory 條文可用確定性 JS 編排機械化 | Opus | UU | P1 | 入 backlog（最高槓桿單點；連帶解 B7）|
| B7 | Handoff Contract Return 未 schema 化——`agent({schema})` 已存在可機械驗證回傳欄位 | Opus | UK | P2 | 入 backlog，綁 B6 |
| B8 | 背景 sub-agent 預設自動 commit/push/開 draft PR——稽核閘門時點須前移至 PR review，v4 §3 未反映 | Opus | UU | P1 | 入 backlog：v4 §3 補「背景委派 gate 錨定 PR review 時點」條文候選（下個 evolution cycle）|
| B9 | 委派消費端缺操作化決策樹：逐字命令邊界、展示三分無量化觸發、引述檔隔離陷阱、oracle 責任、升級責任——共同根源 = brief 需「負面範例集 + 停止條件清單」 | Haiku | UK/KU | 中 | 入 backlog：task-templates.md 增負面範例區 + child 停止條件清單（cost 檔可執行化）|
| B10 | auto-load 規則改動無 cache 失效告警（改 core.md 使存活 session 前綴斷裂，僅被動排查）| Sonnet | KU | P2 | 入 backlog（post-edit hook 對 rules/ 變更提示）|
| B11 | backlog #6 與既有 unicode-covert-channel-guard.sh 疑似重複未去重 | Sonnet | UU | Low | **已修**：backlog #6 改寫範圍（現有 = PostToolUse 告警版；缺 = PreToolUse 阻斷/sanitize）|
| B12 | MAST 14 類多代理失敗未對 v4 §3 做覆蓋率盤點 | Opus | KU | P2 | 入 backlog（quality 檔半小時盤點）|
| B13 | 平台原生 Session Recap / insights 未納入目標外錨機制比較 | Sonnet | UK | Low | 入 backlog 觀察項（免費 drift 佐證源）|
| B14 | Gate 錨點字面耦合條文措辭（改詞即 FAIL）無反向修錨程序；「L3 壓過 L1 審議」未前移為提案前置檢查 | Fable+Sonnet | KU | P2 | 入 backlog：/autoload-evolution 提案流程加 pre-flight `measure.sh --gate` |
| B15 | v4 至今是紙上契約：F1–F10 亦從未對當前主模型跑過基線（EVAL-BASELINE 恆 pending）| Fable | UU | P0 | **升為 backlog 首位**：跑 F1–F14 一輪基線是解除全部 provisional 與驗證 v4 的唯一路徑 |
| B16 | 本 session 自身出現 v4 描述的失敗模式（兩個消化 agent 假「背景執行中」回報 = agentic laziness）未入 LESSONS | Fable | UK | P1 | **本 session 已修**：入 LESSONS |

## 2. 結構觀察

- 四 lens 盲點分佈幾乎不重疊：Opus 集中「v3 落地機制靜默流失 + 平台位移」、Sonnet 集中「誰讀到/靜默不發生」、Haiku 集中「契約寫給 frontier、cost 收不到操作化版本」、Fable 集中「自我指涉缺口（紙上契約/自身違規/錨點脆弱）」——印證「廣度發現」的多視角價值。
- 最大共同主題：**v4 的 advisory→mechanism 轉換債**（B3/B6/B7/B14/B15 同根）：條文已對，強制層與基線量測未跟上。
- Prompting Inversion（2510.22251）張力已記入 SPEC-v4 §7：公理常駐 vs 下沉留待換代以 fixtures 實測。

## 3. 本 session 已落地

B1（四處 canonical 改線 + export 重建）、B2（rollback_signal）、B11（backlog #6 改寫）、B16（LESSONS）；其餘入 SPEC-v4 §6 backlog（見該檔更新）。
