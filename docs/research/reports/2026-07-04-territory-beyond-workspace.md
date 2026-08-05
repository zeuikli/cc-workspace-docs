---
date: 2026-07-04
artifacts: [scripts/territory-probe.sh, research/ROUTINES-DEPLOYED.md, research/prompts/territory-blindspot-pass-prompt.md]
grounded_sources: ["list_triggers 實測（5 個 trig_*，2026-07-04）", "/root/.claude/ 檔案系統實勘", "/tmp/cc-workspace sparse clone 實勘", "env 實測 + .claude/hooks/session-init.sh L263-313", "memory/MEMORY.md · memory/LESSONS.md（07-02/07-03 事故）"]
method: "@trq212 A Field Guide to Fable: Finding Your Unknowns（research/tweets/2026-07-03-@trq212-215386.md）"
scope: workspace 之外、卻支配 workspace 自主學習/進化/Goal-Loop 的力量
type: blindspot-pass-report
---

# 地圖之外的疆域：支配 Workspace 自主性的 Out-of-Repo 力量

> 方法論：把 Thariq 的「map is not the territory + 四象限未知數」反向套用在 workspace 本身。
> **地圖** = repo 內全部 CLAUDE.md / rules / skills / hooks / agents 文件。
> **疆域** = 這些文件實際運行所在的平台。本報告只寫「不在地圖上、卻改變行為」的疆域。

## 執行摘要

Workspace 的自主性（Goal 注入、Loop 執行、自我進化、模型調用）實際由 **8 層 out-of-repo 力量**支配，其中 **只有 2 層半有 repo 文件對應**。最重要的三個發現：

1. **自主性的「基因」存放在 Anthropic server-side trigger store，不在 repo**。5 個 Routine 的完整可執行 prompt（含 The Loop 六階段全文、TEST bash 閘門、PR/merge 流程）以 `trig_*` 物件存於雲端；repo 只有文本副本，兩者無機械同步——07-02 貼錯事故正是此結構性風險的實現。
2. **「當前執行模型」在檔案系統層面不可知**。settings pin（`claude-sonnet-4-6`）、hook 硬編碼（`LATEST_KNOWN_FAMILY=claude-sonnet-5`）、實際 serving model（本 session `claude-fable-5`）三方不一致；`HARNESS_MODEL_VERSION` 只是 session-init 對 pin 值的 echo，**不是真實模型**。repo 的 pilot/model-selection 體系建立在「模型可知可控」的假設上，該假設僅在 sub-agent 參數層成立。
3. **平台注入的環境變數直接調整 Loop 行為，但 repo 從未記載**：`CLAUDE_EFFORT=high`、`MAX_THINKING_TOKENS=31999`、`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80`、`CLAUDE_AUTO_BACKGROUND_TASKS=true`——effort 檔位、思考預算、compact 觸發點、背景任務策略全部被疆域預設，而地圖（context-management.md 的 70%/30-35% compact 閾值等）渾然不覺。

## 一、疆域八層清單

| # | 疆域層 | 位置 | 對自主性的影響 | repo 文件化 |
|---|--------|------|----------------|-------------|
| T1 | **Harness system prompt** | Anthropic runtime（每 session 注入） | 最底層 Goal 驅動：「operating autonomously、不得中途問使用者、turn 結尾不得是計畫」；Workflow（ultracode gate）、ScheduleWakeup（cache 經濟學塑形自主節奏）、Agent（背景執行+自動喚醒）、context compactor、undercover 模型身份 | ❌ 無 |
| T2 | **Server-side trigger store** | claude.ai（`trig_*` × 5） | 時間驅動的 Goal 注入：Routines A–E 每日/每週自主研究-進化循環的可執行本體 | ⚠️ 部分（prompt 文本在 repo，排程/綁定/實際部署態在雲端） |
| T3 | **Launcher 層** | `/root/.claude/` | repo 外的 hooks 先於 repo hooks：SessionStart 強制 git identity（noreply@anthropic.com + Co-authored-by 注入）、**Stop gate 擋停未 commit/push 的 session**（本 session 實際被擋停一次）；`.last-seen-model` 跨 session 模型印記；另有 2 個 dormant slackbot hooks | ❌ 無 |
| T4 | **Cloud config clone** | `/tmp/cc-workspace/` | `/root/.claude/CLAUDE.md` 全文只有一行 `@/tmp/cc-workspace/CLAUDE.md`——全域規則的真正來源是 session-init 從 GitHub sparse clone 的副本（TTL 3600s）；規則生效走「GitHub main → clone → @import」而非工作樹 | ⚠️ 部分（session-init.sh 在 repo，產物在 repo 外） |
| T5 | **模型調用路徑** | 平台 routing | 主對話模型由平台決定（Fable5 全球回歸分類器曾靜默降級 Opus 4.8，MEMORY 07-02）；repo 可控點只有 sub-agent 的 `model`/`effort` 參數與 Workflow `agent()` opts；mid-session 不可切主模型 | ⚠️ 部分（pilot skills 假設可控，降級事件已入 MEMORY） |
| T6 | **網路/身份基礎設施** | `/root/.ccr/` + git proxy | 所有 outbound HTTPS 經 agent proxy（TLS 重終結 + egress policy）；工作 repo remote 是 `127.0.0.1:41729` 本地 git 代理而非 GitHub；OAuth token 走 file descriptor（env 無 key）；限制自主網路行為的硬邊界 | ❌ 無（僅 /root/.ccr/README.md 平台側指引） |
| T7 | **GitHub server-side 行為** | github.com | web merge = server-side 3-way，**不執行 `.gitattributes` merge driver** → MEMORY.md 反覆被覆蓋的根因（pr-guard G3 的敵人）；Actions ai-news-aggregator（UTC 23:00）是 Routine A 的上游輸入，失敗即斷糧 | ⚠️ 部分（pr-guard/Routine 文件記其症狀） |
| T8 | **Context compactor** | harness | 長對話自動摘要（全量 rewrite，~25% 保留）；repo 的 compact 規則只能「提示」不能控制；`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80` 由平台注入，與 context-management.md 的 70% 建議並存但互不知情 | ⚠️ 部分（規則有對策，無機制文件） |

## 二、四象限盤點（本次 blindspot pass 的產出）

### Known Knowns（地圖上的）
The Loop 六階段、L1–L4 四層架構、hooks=唯一 mechanism、Routines 的 prompt 文本、pilot 檔位體系。

### Known Unknowns（已知待決，MEMORY 有記錄）
- 待辦#6：model pin 是否更新為 claude-sonnet-5（使用者跨 session 決策）。
- 待辦#7：Opus 4.8 靜默導流是否消耗 Fable 額度（需 `/usage` 親測）。
- autoDream hook 模擬的 server-side 功能正式 GA 後是否與 dreaming-consolidator 雙跑衝突。

### Unknown Knowns（一直在生效、卻沒人寫下來的）
- **Launcher Stop gate**：每個 session 的「必 commit+push」紀律其實不是 core.md 的功勞，是 `/root/.claude/stop-hook-git-check.sh` 以 exit 2 硬擋——repo 把它當自身文化，實為疆域強制。
- **`HARNESS_MODEL_VERSION` 是 pin echo 不是真實模型**：diff-size-guard 等以它選 per-model 門檻，實際上讀的是 settings 靜態值；模型換代/降級時門檻直接用錯。
- **git 身份與 provenance**：commit 作者、Co-authored-by、Claude-Session URL 全由 launcher 層決定格式——workspace 學習資料（git 歷史）的來源標記不歸 workspace 管。

### Unknown Unknowns（本次新發現）
1. **平台 env 直調 Loop 參數**：`CLAUDE_EFFORT=high` / `MAX_THINKING_TOKENS=31999` / `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80` / `CLAUDE_USAGE_LIMIT_USD=150`——effort-first 原則（delegation-protocol §1）其實已被平台在 env 層實作，repo 無一字提及。
2. **行為契約存在第二副本**：5 個 trigger prompt 各自內嵌 The Loop 六階段全文 → core.md 改版時 trigger 內嵌版不會跟著改 = **內建 silent fork**（與 multi-mode-agent 內聯鏡像同構的問題，但這份在雲端、更難察覺）。
3. **四套排程器並存**：CCR triggers（server-side）、CronCreate（deferred tool）、ScheduleWakeup（session 內）、GitHub Actions——只有最後一套定義在 repo；無統一健康監控。
4. **CLI 版本雙值**：env `CLAUDE_CODE_VERSION=2.1.42` vs `AI_AGENT=claude-code_2-1-201_agent`，哪個生效未知。
5. **Dormant hooks**：`stop-hook-reply-gate.py` + `user-prompt-submit-reply-reminder.py` 存在於 launcher 目錄但未註冊——未來被啟用時行為會無預警改變。

## 三、自主性堆疊解析（Goal / Loop / 模型調用的真相）

```
┌────────────────────────────────────────────────────────┐
│ G5 跨 session 學習   memory/ + dreaming + LESSONS      │ repo（policy）
│ G4 行為契約          CLAUDE.md + rules（The Loop）      │ repo（policy）
│ G3 強制機制          hooks（repo）+ launcher hooks      │ repo+疆域（mechanism）
│ G2 時間驅動 Goal     trigger store（Routines A–E）      │ 疆域（雲端可執行體）
│ G1 底層自主指令      harness system prompt              │ 疆域（不可見不可改）
└────────────────────────────────────────────────────────┘
```

- **Goal 從哪來**：G1 的「autonomously、不得停在計畫」是所有自主行為的地基；G2 每天定時把研究 Goal 注入 fresh session；G4 的六階段只是把 G1 的原始驅動力「塑形」成可驗證流程。拿掉 repo（G4/G5），agent 仍會自主行動——只是沒有方向盤；拿掉 G1/G2，repo 寫得再好也只是靜態文本。
- **Loop 靠什麼閉合**：真正的閉環 = G2（排程喚醒）→ G4（六階段）→ G3（TEST 閘門硬擋）→ G5（RECORD 入庫）→ G2（下次喚醒讀取）。其中兩個關節在疆域：喚醒（trigger store）與擋停（launcher Stop gate）。**自主進化的可靠性 = 疆域關節的可靠性**，07-02 事故（trigger 貼錯 → DAILY-TOPICS 停產 2 日）證明弱點在 G2。
- **模型調用的真相**：主對話模型 = 平台 session 決定（可被分類器靜默改道）；repo 真正可控的調用點只有三處——Agent tool `model` 參數、Workflow `agent()` opts.model/effort、multi-mode-agent frontmatter。**「effort 先於 model」不只是 workspace 心法，平台已用 `CLAUDE_EFFORT` env 印證同一設計**。undercover mode 下模型自我認知也不可靠（Explore agent 自報 opus-4.8、實際 fable-5），故「模型驗證」必須走行為 eval（fable5-harness:calibrate 的做法正確），不能問模型自己。

## 四、依賴矩陣（repo 自主機制 × 疆域 × 失效模式，13 項精選）

| repo 機制 | 疆域依賴 | 失效模式 |
|---|---|---|
| Routines A–E prompt 文本 | trigger store 部署態 | 貼錯/漂移（07-02 已發生）；文件 cron `13 3` vs 部署 `0 3`（07-04 已修） |
| pilot skills + settings pin | 平台 model routing | 靜默降級 Opus 4.8；pin ≠ 實跑模型 |
| diff-size-guard per-model 門檻 | `HARNESS_MODEL_VERSION`（pin echo） | 模型換代時用錯門檻 |
| session-init 換代偵測 | 硬編碼 `LATEST_KNOWN_FAMILY` | 平台推新世代 → 永久誤報/漏報 |
| RECORD / MEMORY 連續性 | harness compactor + GitHub 3-way merge | 約束丟失（~25% 保留）；MEMORY 被覆蓋 |
| `/loop`、multi-mode 排程 | CronCreate/ScheduleWakeup 工具存在性 | web session 無工具 → 假裝排程成功（multi-mode G3 已補 policy 防呆） |
| sub-agent 委派 | task-notification 機制 | fallback 喚醒重做不可逆操作（LESSONS L58） |
| Routine A 選題 | GitHub Actions 產出 | Actions 失敗 → 靜默斷糧 |
| handoff 佇列 | ephemeral container | gitignored 檔在 fresh clone 消失（LESSONS L84） |
| Stop 時 commit 紀律 | launcher stop-hook | launcher 改版 → 紀律無聲消失 |
| 全域規則載入 | /tmp clone TTL 3600s | main 推新規則後 1h 內 session 仍用舊版 |
| 網路研究（WebFetch/Search） | agent proxy egress policy | 403/407 阻擋；gRPC/WS 不可用 |
| unverified_success 閘門 | （設計正確的反例）它假設疆域不可信 | ——此閘門是全 repo 對疆域姿態最正確的一條 |

## 五、演化候選（依 workspace 安全邊界分級）

- **P0（research/scripts 範圍，本次已執行）**
  1. `scripts/territory-probe.sh`：把本報告的疆域檢查機械化（env 注入值、三方模型值、launcher hooks、/tmp clone 新鮮度、remote 拓撲、排程器盤點），可重複執行、輸出 ✅/⚠️/❌。**policy → mechanism**。
  2. `research/ROUTINES-DEPLOYED.md`：trigger store 部署態鏡像（id/cron/env/created_at），給未來 session 一個「地圖 vs 疆域」diff 基準；含覆核程序。
- **P1（提案，`.claude/` 範圍 → 待人工審核，已入 EVOLUTION-QUEUE）**
  3. `LATEST_KNOWN_FAMILY` 從 session-init.sh 硬編碼改讀 SSoT 檔（如 `.claude/refs/model-selection-grid.md` frontmatter），換代只改一處。
  4. healthcheck 掛載 territory-probe（coupling 巡檢項），讓疆域漂移進入 PGE 常規檢查。
- **P2（觀察）**
  5. trigger prompt 內嵌 The Loop 全文的 silent fork：等 core.md 下次改版時驗證漂移代價，再決定是否改為「引用 repo 檔案」而非內嵌。
  6. autoDream vs 平台 auto-dream GA 的衝突預案。

## 六、Open Questions（承兩路探勘，未解）

1. 有無 API 可讓 hook 讀回**真實 serving model id**（而非 pin）？目前唯一可靠路徑是行為 eval。
2. Opus 4.8 導流的額度歸屬（待辦#7）。
3. `CLAUDE_CODE_VERSION` 2.1.42 vs 2.1.201 何者生效。
4. dormant slackbot hooks 的啟用計畫。
5. git local_proxy（41729）與 egress proxy 的關係。

## 產物索引

| 產物 | 路徑 | 用途 |
|------|------|------|
| 本報告 | `research/reports/2026-07-04-territory-beyond-workspace.md` | 疆域地圖 + 四象限盤點 |
| 疆域探測器 | `scripts/territory-probe.sh` | 機械化疆域檢查（可掛 healthcheck） |
| 部署鏡像 | `research/ROUTINES-DEPLOYED.md` | trigger store 快照 + 覆核程序 |
| 可攜 prompt | `research/prompts/territory-blindspot-pass-prompt.md` | 模型無關（Claude/ChatGPT 皆可用）的四象限疆域盲點掃描 prompt |

## 如何重複這次掃描（任何未來 session / 任何模型）

1. 機械層：`bash scripts/territory-probe.sh`（秒級，✅/⚠️/❌ 輸出；⚠️ 為結構性事實不必歸零，❌ 必處理）。
2. 排程層：session 內跑 `list_triggers`，與 `research/ROUTINES-DEPLOYED.md` 逐欄 diff；漂移即按 ROUTINES-SETUP FAQ 處置並更新快照。
3. 認知層：把 `research/prompts/territory-blindspot-pass-prompt.md` 貼給任何 agent（含非 Claude），重做一次四象限盤點——疆域會隨平台改版而變，本報告是 2026-07-04 的快照，不是恆真清單（規則 = decaying cache 原則同樣適用於疆域地圖）。
