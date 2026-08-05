# .claude/ 目錄盤點報告 — 69 檔逐一交代

> ⚠️ **HISTORICAL SNAPSHOT — 部分內容已過時**（2026-06-21 更新）  
> 以下三個 hook 在 PR #743（2026-06 hook 整併）中已刪除，**不再存在**：  
> `notification-log.sh`（功能已下線）、`sdd-cache-pre.sh`、`sdd-cache-post.sh`（功能移除）。  
> 本頁 hooks/ 清單仍顯示它們為 LIVE/KEEP，係快照時點（2026-05-31）的正確狀態，現況請見 `docs/reference/hook-lifecycle.md`。

> **日期**：2026-05-31 · **PR**：#398 · **分支**：feature/claude-dir-inventory
> **方法**：harness loop（OBSERVE→IDENTIFY→TEST→APPLY→RECORD）+ 機械 grep load-path 分類
> **範圍**：使用者指定 7 路徑 — `.claude/{hooks,prompts,refs,rules}` + `HANDOFF.md` + `REFERENCES.md` + `settings.json`

---

## 核心結論

1. **「刪孤兒省浪費」基本是假命題**：`refs/`、`prompts/` 皆 on-demand（不 auto-load）→ 未被引用的檔從不載入 = **零 token 成本**。使用者擔心的「浪費」在這些檔上不存在。真正價值在模型 staleness 修正。
2. **模型 staleness 幾乎全是 false-positive / 史料 attribution**：初版 dynamic workflow 的 classify agent **大量幻覺**（標 core.md L16 有不存在的 "Opus 4.7" 內容、把當前模型名 Sonnet 4.6 / Haiku 4.5 當 stale、把史料 attribution 當該改）。逐一機械 grep 驗證後，**無「當前事實過時」需修**。
3. **18 個 hooks 全部內容有效**：退場機制（`memory-archive.sh`、cosmetic monitor、#1/#2 auto-commit）都已正確標記或移除，無殘留 bug。
4. **改動極小（3 改 + 1 刪）**：符合大道至簡——只動確定該動的。

## load-path 三分類準則（取代易幻覺的 reference-count）

- **LIVE**：runtime 可達（settings.json 註冊的 hook / CLAUDE.md @import / auto-load rule / 被 live SKILL 用「read X first」內容指向）
- **INDEXED-ONLY**：只出現在 trigger-index.md / REFERENCES.md / dir README / docs/INDEX.md（被列出 ≠ 被載入）
- **HISTORICAL**：只被 research/ 報告提及（在「談論」此檔，非「使用」）
- **DATA-SOURCE / SCRIPT**：被 script（healthcheck/sync-workspace/hook）程式消費
- 機械 grep 已排除噪音：`.git/`、`command-log.jsonl`、`*.pack`、`sdd-cache/`

## iOS vs CLI surface（可驗證部分）

- hooks + settings.json hook 執行 = **local CLI-only by construction**，iOS/web 不跑（全 18 hooks 對 iOS 不取用）。
- claude.ai/code 是否讀取 CLAUDE.md / .claude/rules / skills = **UNCERTAIN**（未杜撰）。
- 刪除準則只看「CLI 與 live-entry」；「iOS 不用」單獨不構成刪除理由（CLI 為主 surface）。

---

## 改動明細（使用者逐項批准）

| 檔 | 動作 | 理由 |
|----|------|------|
| `.claude/rules/.sha256sums` | **刪除** | 無消費者 + 4 個 checksum 全 DRIFT；`git log -S` 顯示 security-hardening 起源（commit e6f40ed0）但 verifier 已被移除；healthcheck/sync-workspace 皆不讀它 |
| `.claude/skills/opus-pilot/SKILL.md` | 補 `## Sub-Agent Inheritance` | 對稱化：原本只有 haiku/sonnet SKILL 接線各自 *-pilot-mode.md，opus 孤立未接線 |
| `.claude/refs/opus-pilot-mode.md` | 修正 | 反向接線後救活；去重複 playbook 行 + 補對稱 Known Gotchas |
| `.claude/refs/constraints.md` | 精簡 | 量化界線數字指回 `core.md` L45 單一來源（消除雙源維護）；保留獨特 Don't/Do 對照表 |

---

## 完整 69 檔逐一交代

### hooks/（18）— 全 LIVE 保留

| 檔案 | Bucket | Verdict | 理由 |
|------|--------|---------|------|
| `.claude/hooks/audit-log.sh` | LIVE | KEEP | PostToolUse 審計日誌 |
| `.claude/hooks/audit-permission.sh` | LIVE | KEEP | PermissionRequest 日誌 |
| `.claude/hooks/block-dangerous.sh` | LIVE | KEEP | PreToolUse Bash 危險指令攔截 |
| `.claude/hooks/failure-log.sh` | LIVE | KEEP | PostToolUseFailure 日誌 |
| `.claude/hooks/memory-sync.sh` | LIVE | KEEP | no-op（ADR L144 待決，刻意保留註冊） |
| `.claude/hooks/monitor-reminder.sh` | LIVE | KEEP | 偵測 run_in_background→Monitor 提醒（**非** cosmetic monitor，早期懷疑已排除） |
| `.claude/hooks/notification-log.sh` | LIVE | KEEP | Notification 日誌 |
| `.claude/hooks/post-compact.sh` | LIVE | KEEP | PostCompact 還原 |
| `.claude/hooks/post-edit.sh` | LIVE | KEEP | Edit/Write 後處理 |
| `.claude/hooks/pre-commit-review.sh` | LIVE | KEEP | git commit 前審查 |
| `.claude/hooks/pre-compact.sh` | LIVE | KEEP | PreCompact 保護 |
| `.claude/hooks/protect-sensitive-files.sh` | LIVE | KEEP | 敏感檔保護 |
| `.claude/hooks/sdd-cache-post.sh` | LIVE | KEEP | WebFetch cache 寫 |
| `.claude/hooks/sdd-cache-pre.sh` | LIVE | KEEP | WebFetch cache 讀 |
| `.claude/hooks/session-init.sh` | LIVE | KEEP | SessionStart（L260 Opus 4.7 = 史料 attribution，指 anthropic-insights §4） |
| `.claude/hooks/session-start-eval-reminder.sh` | LIVE | KEEP | SessionStart eval 提醒 |
| `.claude/hooks/session-stop.sh` | LIVE | KEEP | Stop（L301-305 記憶大小監控已退場標記，非殘留 bug） |
| `.claude/hooks/user-prompt-submit.sh` | LIVE | KEEP | UserPromptSubmit hint 注入 |

### prompts/（5）— 全 KEEP（README L3「human-triggered only」，grep 看不到但設計使然）

| 檔案 | Bucket | Verdict | 理由 |
|------|--------|---------|------|
| `.claude/prompts/README.md` | LIVE | KEEP | dir-doc |
| `.claude/prompts/context-placement-audit.md` | LIVE | KEEP | human-triggered 審查模板 |
| `.claude/prompts/harness-health-check.md` | LIVE | KEEP | human-triggered 健康度模板 |
| `.claude/prompts/independent-review.md` | LIVE | KEEP | ship-review SKILL 引用 |
| `.claude/prompts/skill-quality-audit.md` | LIVE | KEEP | human-triggered skill 審查模板 |

### refs/（36）

| 檔案 | Bucket | Verdict | 理由 |
|------|--------|---------|------|
| `.claude/refs/INDEX.md` | LIVE-dir | KEEP | dir-doc |
| `.claude/refs/advisor-tool-api.md` | INDEXED | KEEP | STANDALONE SDK 細節（零成本留）；L36 "Opus 4.6" 為配對規則範例非當前預設宣稱 |
| `.claude/refs/agents-md-design.md` | INDEXED | KEEP | STANDALONE（Augment 七模式量化表，零成本留） |
| `.claude/refs/anchor-dictionary.md` | LIVE | KEEP | haiku-pilot SKILL 引用 |
| `.claude/refs/anthropic-insights.md` | SCRIPT | KEEP | session-init.sh 消費 |
| `.claude/refs/brain-first-protocol.md` | INDEXED | KEEP | STANDALONE 查找序列（零成本留） |
| `.claude/refs/claude-oauth-token.md` | LIVE | KEEP | media-research SKILL 引用 |
| `.claude/refs/cli-enhancers.md` | LIVE | KEEP | research-hub references 引用 |
| `.claude/refs/constraints.md` | INDEXED | **精簡保留** | 量化界線指回 core.md 單源；保留獨特 Don't/Do 表 |
| `.claude/refs/error-handling.md` | LIVE | KEEP | self-escalate agent + subagent-strategy 引用 |
| `.claude/refs/gap-validation-protocol.md` | LIVE | KEEP | gap-vote SKILL 引用 |
| `.claude/refs/gotchas-consolidated.md` | INDEXED | KEEP | STANDALONE 反直覺延伸（零成本留） |
| `.claude/refs/haiku-pilot-mode.md` | LIVE | KEEP | haiku-pilot SKILL「read first」 |
| `.claude/refs/harness-design.md` | LIVE | KEEP | AGENTS.md + docs 引用 |
| `.claude/refs/harness-loop.md` | LIVE | KEEP | AGENTS.md 引用 |
| `.claude/refs/hooks-decision-tree.md` | INDEXED | KEEP | STANDALONE if/matcher 差異（零成本留） |
| `.claude/refs/karpathy-mnilax-best-solution.md` | LIVE | KEEP | docs + rules 引用 |
| `.claude/refs/karpathy-principles.md` | LIVE | KEEP | karpathy-mnilax 引用 |
| `.claude/refs/memory-layering.md` | INDEXED | KEEP | STANDALONE（Memory Fencing 規格 + Phase 1-3 DEFERRED 提案，已標 archive 退場，零成本留） |
| `.claude/refs/model-selection-grid.md` | LIVE | KEEP | AGENTS.md + token-waste-audit 引用 |
| `.claude/refs/opus-best-practices.md` | LIVE | KEEP | docs + research-hub 引用（4.7-era 標記為 attribution） |
| `.claude/refs/opus-pilot-mode.md` | INDEXED→LIVE | **已接線** | 反向接線 opus-pilot SKILL Sub-Agent Inheritance；去重複 + 補 Gotchas |
| `.claude/refs/output-by-model.md` | INDEXED | KEEP | STANDALONE 模型字數範例（零成本留） |
| `.claude/refs/per-model-eval-suite.md` | LIVE | KEEP | autoload-evolution SKILL + session-start-eval-reminder hook 引用 |
| `.claude/refs/pilot-shared-preflights.md` | LIVE | KEEP | 三 pilot SKILL 引用；L88-92 定價表 reconcile 後正確（已列 Opus 4.8） |
| `.claude/refs/prompt-caching-rules.md` | LIVE | KEEP | 多 hook 引用；cache 最小 token 表為當前模型，正確 |
| `.claude/refs/quality.md` | INDEXED | KEEP | STANDALONE（lint 表已被 review-hub 涵蓋，但測試順序仍有值，零成本留） |
| `.claude/refs/routines.md` | LIVE | KEEP | docs + 多 SKILL references 引用 |
| `.claude/refs/session-management.md` | LIVE | KEEP | HANDOFF.md + 多 SKILL 引用 |
| `.claude/refs/skill-authoring.md` | LIVE | KEEP | 多 SKILL GOTCHAS 引用 |
| `.claude/refs/skill-gotcha-protocol.md` | LIVE | KEEP | 多 SKILL 引用（25 處） |
| `.claude/refs/sonnet-pilot-mode.md` | LIVE | KEEP | sonnet-pilot SKILL「read first」 |
| `.claude/refs/subagent-advanced.md` | LIVE | KEEP | docs/multi-agent-coordination 引用 |
| `.claude/refs/subagent-dispatch.md` | INDEXED | KEEP | STANDALONE（Advisor 量化矩陣 AGENTS.md 未有，零成本留） |
| `.claude/refs/system-prompt-architecture-5d.md` | LIVE | KEEP | gap-validation + skill-authoring 引用 |
| `.claude/refs/trigger-index.md` | DATA-SOURCE | KEEP | healthcheck.sh L423-457 + sync-workspace §11 當資料源消費（刪會破 healthcheck） |

### rules/（7，含已刪 .sha256sums）

| 檔案 | Bucket | Verdict | 理由 |
|------|--------|---------|------|
| `.claude/rules/INDEX.md` | LIVE | KEEP | dir-doc |
| `.claude/rules/context-management.md` | LIVE (auto-load) | KEEP | Token budget / compact 觸發 |
| `.claude/rules/core.md` | LIVE (auto-load) | KEEP | Git 流程 / 假設顯露 / 量化界線（L16 無 stale，初版 agent 幻覺） |
| `.claude/rules/output-discipline.md` | LIVE (auto-load) | KEEP | 無開場白 / 填充語禁止 |
| `.claude/rules/security-hygiene.md` | LIVE (path-scoped) | KEEP | 編輯 .env/credentials 時觸發 |
| `.claude/rules/subagent-strategy.md` | LIVE (auto-load) | KEEP | 委派決策 / Fan-out / Advisor |
| `.claude/rules/.sha256sums` | **DELETED** | **刪除** | 無消費者 + 4 sum 全 DRIFT；security-hardening verifier 已移除 |

### top-level（3）

| 檔案 | Bucket | Verdict | 理由 |
|------|--------|---------|------|
| `.claude/HANDOFF.md` | LIVE | KEEP | rewind 前手動填寫模板（同 prompts 類，grep 看不到但設計使然） |
| `.claude/REFERENCES.md` | LIVE | KEEP | 多 agent（doc-writer/memory-compactor/quick-code-reviewer）+ post-compact hook 引用 |
| `.claude/settings.json` | LIVE | KEEP | model=Sonnet 4.6 / advisorModel=Opus 4.8 為**刻意 pin**，非 stale |

---

## staleness「標記後驗證」明細（防 false-positive 的證據）

| 初版 agent flag | 實際 | 處置 |
|----------------|------|------|
| core.md L16「Opus 4.7-era」 | **幻覺**（該行是 Framework Integrity 規則，無 4.7 字串） | 無動作 |
| anthropic-insights.md L3「Opus 4.7 System Prompt」 | ATTRIBUTION（收錄版本標記 + 備案路徑明確） | 保留 |
| session-init.sh L260「Opus 4.7 官方指引」 | ATTRIBUTION（指 anthropic-insights §4 史料） | 保留 |
| pilot-shared-preflights L90「Opus 4.7/4.6/4.5」 | reconcile：L88 已獨立列 Opus 4.8，L90 是舊版對照列 | 保留（正確） |
| prompt-caching-rules L51-53 模型表 | 當前模型（Sonnet 4.6/Haiku 4.5/Opus 系列），正確 | 保留 |
| anchor-dictionary L5,46 Sonnet4.6/Haiku4.5 | 當前模型，正確 | 保留 |
| claude-oauth-token L53,82 `claude-haiku-4-5-20251001` | 有效 ID（帶日期後綴，與 dateless-alias 偏好微異，次要 nit） | 保留 |
| model-selection-grid L42 OQ 數字 | 已自我標註「來源待驗證」，非模型 stale | 保留 |
| opus-best-practices L9,16,21「4.7-era / 4.6 預設」 | ATTRIBUTION（檔頭明標歷史標記） | 保留 |

---

## 驗證

```
bash scripts/healthcheck.sh
======================================
 統計結果：PASS: 105  WARN: 3  FAIL: 0
======================================
```
- 3 WARN = MCP transparency（預期）+ README frontmatter（既有），與本次改動無關
- 「所有 @ 連結都指向存在的檔案」**PASS** → 刪除/編輯無 dangling ref

## 方法論教訓（harness self-improvement）

兩個複合失敗差點 ship 出錯誤盤點：
1. **schema 設計缺陷**：dynamic workflow 的 `verdict` 與 `modelStale` 是分開欄位，actionable filter `verdict !== 'KEEP'` **靜默丟棄**所有「KEEP + STALE-FACT」項 → 整類更新候選沒進對抗驗證。
2. **classify agent 幻覺**：core.md L16 不存在內容、advisor-tool-api「被 healthcheck 消費」假宣稱。

**防範**：結構化 subagent verdict **不是證據**，須機械 grep 重新驗證；單一 schema 欄位上的 actionable filter 可能藏掉整個類別。catch 來自機械 grep，不是再加一個 agent。
