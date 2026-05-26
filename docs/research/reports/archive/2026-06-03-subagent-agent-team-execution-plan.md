# 可執行計劃書：cc-workspace 採用 Sub-Agent + Agent-Team Orchestration

> **日期**：2026-06-03 ｜ **語言**：繁體中文（技術術語保留英文）
> **類型**：execution-plan（配套研究報告 `2026-06-03-subagent-agent-team-deep-research.md`）
> **產出方式**：`autoresearch:reason` 對抗論證（generate -> critique -> synthesize），含實際 grep 接地驗證
> **核心結論**：本 workspace 已有生產級 hub-and-spoke + consensus 實現（`gap-vote`/`autoresearch:predict`），**此計劃主要是「盤點 + 文件化 + 補真缺口」，非新建 orchestrator**。
> **硬設計規則**：零新增 auto-load rule（byte 餘裕僅 ~1.1K）；所有落地走 `.claude/refs/` / 既有 skill / GOTCHAS（on-demand）；每階段驗收含 byte 不增斷言。

---

## 0. 定位：為何此計劃「主要是盤點，非新建」

四源研究指向的「可靠生產拓撲」——hub-and-spoke + stateless workers + artifact contract + consensus——**本 workspace 已有實現**：

| 研究術語 | 既有實現 |
|---------|---------|
| hub-and-spoke（orchestrator-worker） | `subagent-strategy.md`：parent↔child、child 不互通 |
| stateless worker + artifact contract | `gap-vote`：vote-matrix + evidence audit schema |
| multi-agent debate | `autoresearch:predict`：3–8 persona + blind judge |
| consensus / voting | `gap-vote`：2/3 deterministic |
| task verification（防幻覺自報） | R4 + dynamic-workflow「機械 grep 重驗」 |
| echo-chamber 防護 | blind judge + external signal |

因此本計劃**不重寫 `subagent-strategy.md`、不 day-one 建 nested loop**，而是：(a) 把既成最佳實踐固化為可稽核 canonical、(b) 補兩個有實據的真 fix、(c) 把 MAST 失敗模式對映既有防護並補缺口。

---

## 1. 目標與非目標

**目標**
1. 把分散的 sub-agent 最佳實踐固化為單一 canonical 來源（least-privilege、模型路由），消除 silent drift。
2. 把既有 `gap-vote`/`autoresearch:predict` 的 agent-team 能力**顯式對映**到研究拓撲術語，讓未來任務正確選用而非重造。
3. 把 MAST 14 失敗模式對映既有防護，找真實缺口並最小補強。

**非目標（明確排除）**
- 不重寫 `subagent-strategy.md` 核心（fan-out 4 / parent↔child / no self-retry 保留）。
- Day-one 不建 nested multi-agent loop（child 派 child）。
- 不新增任何 auto-load rule（byte 預算不允許）。
- 不引入 open mesh / 自由 agent-to-agent 通訊。
- 不讓 LLM 自由「選隊」（見 §2.2 R5 守則）。

---

## 2. 三階段路線圖

### 階段一：鞏固現有 sub-agent 實踐（least-privilege + 模型路由）

落地：1 真 fix（skill frontmatter）+ 1 ref。**零 auto-load 增量。**

**行動 1.1 — review-hub least-privilege 修正（VoltAgent 借鏡）**
- 檔案：`.claude/skills/review-hub/SKILL.md` frontmatter `allowed-tools`
- 改動：移除 `Write`（reviewer 應 read-only），約 1 行。
  - 接地驗證（reviewer agent 已 grep）：`iac-review`/`ship-review`/`security-compliance` 已是 read-only，僅 `review-hub` 含 `Write`。
- 前置確認：grep review-hub body 是否真有寫檔流程；若有 -> 改判 `defer` 並在 GOTCHAS 記錄豁免，不強拆。
- 驗收：`grep -L "allowed-tools:.*Write" .claude/skills/{review-hub,ship-review,iac-review,security-compliance}/SKILL.md | wc -l` -> 預期 `4`。
- 風險：review-hub 實需寫報告 -> 誤拆破功能。回滾：`git revert`（單行）。

**行動 1.2 — 模型路由 canonical 化（wshobson 三層借鏡）**
- 接地驗證（reviewer agent 已 grep）：路由分散 16 agent frontmatter + autoresearch 路由表 + 3 pilot skills + CLAUDE.md 矩陣 = 多來源 drift 風險。
- 落地：新增 `.claude/refs/model-routing.md`（≤60 行），列 task-type->model 確定性對映為 single source of truth；各 frontmatter 維持但標註「依 model-routing.md」。**不動 auto-load**。
- 驗收：`test -f .claude/refs/model-routing.md && grep -c "haiku\|sonnet\|opus" .claude/refs/model-routing.md` -> ≥3。
- 風險：與既有 frontmatter `model:` 矛盾（R7）-> ref 記 `TODO(conflict)`。回滾：`rm`。

**階段一 byte gate**：`wc -c CLAUDE.md .claude/rules/*.md | tail -1` 對基線無增；`bash scripts/healthcheck.sh | tail -3` FAIL=0。

---

### 階段二：agent-team 模式文件化盤點（接地 gap-vote / debate）

落地：1 ref（拓撲對映表）。**零新建 orchestrator、零 auto-load 增量。**

**行動 2.1 — 拓撲術語對映 ref**
- 落地：`.claude/refs/agent-team-patterns.md`（≤80 行），把研究術語對映既有設施（見 §0 表），每行附「何時用 / 何時不用」+ token 倍數警語（multi-agent 15×）。
- 驗收：`test -f .claude/refs/agent-team-patterns.md && grep -c "gap-vote\|autoresearch:predict\|hub-and-spoke" .claude/refs/agent-team-patterns.md` -> ≥3。
- 風險：與既有 skill 重複（違 R2）-> 限定「術語橋接 + 選用指引」，用 `-> See` 引用不複製 schema。回滾：`rm`。

**行動 2.2 — 動態 team 組成（確定性 mapping，非 LLM 選隊）**
- 落地：在 2.1 ref 內加 task-type->team-size 確定性表（接地 AgentVerse「最優 team size」+ Anthropic 量表 1/2-4/10+）：簡單->1、中->2-4、研究廣度->hub+N worker。
- **R5 守則明文**：team 組成是 routing（確定性 mapping），由 task-type 查表決定，**不由 LLM 自由選**；LLM 只產 verdict/內容。
- 驗收：`grep -c "1 \|2-4\|10+\|task-type" .claude/refs/agent-team-patterns.md` -> 量表存在。
- 風險：被誤用為「讓 agent 自選隊」-> ref 內粗體禁令。回滾：`rm`。

**階段二 byte gate**：同階段一；healthcheck FAIL=0。

---

### 階段三：multi-agent 失敗防護（MAST 對映 + task verification）

落地：1 ref（MAST 對映矩陣）+ GOTCHAS 補強。**零 auto-load 增量。**

**行動 3.1 — MAST 14 失敗模式對映矩陣**
- 落地：`.claude/refs/mast-failure-mapping.md`（≤90 行）：14 模式 × {是否已防護 / 防護機制 / 缺口}。
- 預期已防護：specification 品質（`autoresearch` Setup Gate）、agent 幻覺自報完成（`gap-vote` evidence audit + dynamic-workflow grep 重驗）、echo chamber（blind judge + external signal）。
- 驗收：`grep -c "^| " .claude/refs/mast-failure-mapping.md` -> ≥14（14 模式全列）。
- 風險：把「已有防護」誤標缺口而過度補（違 R2）-> 每格引用既有機制檔案路徑為證。回滾：`rm`。

**行動 3.2 — task verification 強化（最大瓶頸，補真缺口）**
- 條件：僅補 3.1 矩陣標出的**真缺口**，不預先補。最可能缺口：一般 sub-agent 委派未強制 parent 抽驗（`gap-vote` 已強制 evidence audit，但泛化委派未強制）。
- 落地：在 `harness-meta` GOTCHAS.md 補一條「sub-agent verdict 採信前 parent 必機械 grep 抽驗」（dynamic-workflow 規則泛化），約 3 行。
- 驗收：`grep -c "parent.*grep\|抽驗" .claude/skills/harness-meta/GOTCHAS.md` -> ≥1 新增。
- 風險：與既有條目重複 -> 先 grep 確認不重複再寫。回滾：`git revert`。

**階段三 byte gate**：同前；healthcheck FAIL=0。

---

## 3. 風險矩陣

| 風險 | 觸發條件 | 緩解（機械） | 回滾 |
|------|---------|------------|------|
| token 成本爆炸 | 誤用 multi-agent（15×）做單 agent 可解任務 | ref「何時不用」+ 委派量表閘門；`autoresearch` token budget 表 | 不啟動 team；單對話處理 |
| auto-load byte 超 18,000 | 任一行動誤改 `.claude/rules/*` | 每階段 `wc -c ... \| tail -1` 斷言不增；落 refs/skills/GOTCHAS | `git revert` 該 rule 改動 |
| coordination overhead | team-size 過大 | 2.2 task-type->size 確定性表 | 縮回 1-2 agent |
| echo chamber | debate 只 LLM 自評 | 復用既有 blind judge + external signal | 加 guard command |

---

## 4. 明確的「不做什麼」及原因

- **不建 open mesh / agent-to-agent 直接通訊** — 社群共識已淘汰；違 parent↔child。
- **Day-one 不建 nested loop** — 非目標；dynamic workflow runtime 已控管 ≤16/≤1000。
- **不新增 auto-load rule** — byte 餘裕 ~1.1K，價值可由 on-demand ref 承載。
- **不讓 LLM 自由選隊** — 違 R5；組成是 routing（確定性 mapping）。
- **不重寫 echo-chamber / consensus 機制** — 既有 blind judge + 2/3 deterministic + evidence audit 已覆蓋。
- **child 不 self-retry** — 既有規則保留。

---

## 5. 對抗論證修正記錄（generate -> critique -> synthesize）

實際砍掉/改寫的內容（非空話）：

1. **違 R4 -> 已修**：初稿行動 1.1 驗收原寫「review 類改為 least-privilege」（主觀）-> 改為 `grep -L ... | wc -l -> 4`。所有驗收統一改 bash 命令 + 期望輸出。
2. **違 byte 上限 -> 結構性消解**：初稿曾考慮寫進 `subagent-strategy.md`（auto-load）-> 全改落 `.claude/refs/`（on-demand），「零 auto-load 增量 + 每階段 byte 斷言」升為硬規則。
3. **違 R2（over-engineering）-> 砍 day-one 項**：初稿階段二含「新建 team-orchestrator skill」+「nested loop」-> 發現 `gap-vote`+`autoresearch:predict` 已生產級，新建 = 重造。砍除，重定義為「文件化盤點 + 確定性 team-size 表」。
4. **違 R5 -> 新增明文守則**：「動態組成」措辭模糊可能被讀成「agent 自選隊」-> 新增 §2.2 R5 守則 + 列入「不做什麼」。
5. **echo chamber 不重造**：初稿曾規劃「為 debate 加 judge」-> 確認 `autoresearch` 已有 blind judge + external signal，改引用不重寫。

---

## 6. 採用順序與接地檔案

建議順序：階段一 -> 二 -> 三（各階段獨立可驗、可回滾）。每階段為一個原子 commit（R3 commit 顆粒度）。

| 動作 | 檔案 | 階段 |
|------|------|------|
| 改 | `.claude/skills/review-hub/SKILL.md` | 1.1 |
| 新增 | `.claude/refs/model-routing.md` | 1.2 |
| 新增 | `.claude/refs/agent-team-patterns.md` | 2.1 + 2.2 |
| 新增 | `.claude/refs/mast-failure-mapping.md` | 3.1 |
| 改 | `.claude/skills/harness-meta/GOTCHAS.md` | 3.2 |
| **不動** | `.claude/rules/subagent-strategy.md`（核心保留） | — |

> 本計劃為「採用藍圖」，非本 session 立即執行的改動。實際採用時各行動項依 Harness Loop（OBSERVE->IDENTIFY->PROPOSE->TEST->APPLY->RECORD）逐項驗證，破壞性 APPLY 前 gate 使用者。
