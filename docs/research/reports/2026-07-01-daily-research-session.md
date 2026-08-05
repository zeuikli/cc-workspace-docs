---
date: 2026-07-01
source: DAILY-RESEARCH/2026-07-01.md
topics: [sonnet5-launch-cost-security-controversy, claude-science-desktop-linux-dual-launch, loop-engineering-stop-condition-design, omnigent-claude-tag-cross-harness-adoption, claude-code-china-detection-unconfirmed-rumor]
type: session-report
---

# Session Report 2026-07-01 — Daily Research

## 上次 P0 回填

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1（四延解除）：EVOLUTION-QUEUE tokenizer/computer-use/cache_creation 登記 | `grep -qE "tokenizer\|computer.use\|cache_creation" research/EVOLUTION-QUEUE.md` | ✅ 已完成（實際路徑為 `research/EVOLUTION-QUEUE.md`，非 `.claude/`；四項 status=proposed 已登記，grep 通過） |
| P1-3：cache hit rate 監控 SOP | `grep -qE "cache_read.*input_tokens\|60%\|coinbase" .claude/refs/cache-health-metrics.md` | ✅ 已完成（grep 通過） |
| P1-1：pilot-shared-preflights.md Fable 5 定價更新 | `grep -qE '\$10.*\$50\|pay.per.token' .claude/refs/pilot-shared-preflights.md` | ✅ 已完成（grep 通過） |
| P2-1：Fable 5 公開恢復監控 | isfable5back.com 狀態追蹤 | ⏳ 延續觀察（無新觸發事件，本日未主動查證） |

**P0-1 根因澄清**：昨日報告誤判路徑為 `.claude/EVOLUTION-QUEUE.md`，實際檔案位於 `research/EVOLUTION-QUEUE.md`（已存在且內容完整）。四延狀態解除，非路徑缺失問題，屬回填檢查腳本路徑誤植，已於本次修正。

---

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-07-01.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：8 次深度抓取（含 2 次無效內容需補抓：Yahoo Tech 實為 Vercel 插件非 Claude Code、thenewstack.io 內容截斷，均已用替代來源補足）

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Claude Code 中國代理偵測——謠言升級為證實事件**（影響等級：**Critical**）

DAILY-TOPICS 選題時標記「未確認，信心度低」，本次搜尋發現 **Anthropic 技術人員已公開承認並宣布下版回滾**。機制：偵測 `ANTHROPIC_BASE_URL` 非標準端點 + 時區 `Asia/Shanghai`/`Asia/Urumqi`，透過竄改 system prompt 日期行分隔符（`-`→`/`）與 Unicode 同形異碼 apostrophe 隱蔽編碼。受影響版本 2.1.193/195/196。此為 workspace 既有 tokenizer/Unicode 隱寫護欄（06-27 已收錄於 security-hygiene.md）的**首個生產環境實證案例**，非假設性風險。

**2. Loop Engineering 業界術語收斂 + 外部獨立背書 TEST 階段設計**（影響等級：**High**）

「Loop Engineering」正式成為 2026 業界標準術語（prompt engineering 的繼任者）。核心失敗模式命名「弱驗證器產生自信的昂貴垃圾」（confidently producing garbage）與核心解方「產生器/驗證器必須分離，self-verification 不可信」，直接外部驗證本 workspace core.md TEST 階段「unverified_success 閘門」+「主對話親跑確定性檢查」設計的正確性。

**3. Sonnet 5 定位策略：cyber 能力閹割換取無管制上市**（影響等級：**High**）

Sonnet 5（2026-06-30 發布）刻意未訓練 cybersecurity 任務（Firefox exploit 成功率 0%），藉此規避 Fable 5/Mythos 5 因出口管制指令遭遇的停權命運。定價 $2/$10（至 08/31）→ $3/$15。此為「安全控制從模型層下沉至 harness/policy 層」趨勢的具體案例，與 Omnigent 的 meta-harness policy 設計呼應同一典範轉移。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-A：security-hygiene.md 補充 China 偵測實證案例**
- 目標：於既有 tokenizer/Unicode 隱寫段落補一行「已知案例：Claude Code 2.1.193-196 system prompt Unicode 隱寫（2026-06-30 證實，官方已排定回滾）」
- 驗證：`grep -q "2.1.19[3-6]\|china.*proxy\|proxy.*china" .claude/rules/security-hygiene.md`（不區分大小寫）

**P0-B：pilot-shared-preflights.md §E 新增 Sonnet 5 定價條目**
- 目標：定價矩陣加入 Sonnet 5（$2/$10 → $3/$15，轉換日 2026-08-31）+ cyber 能力弱於 Opus 的路由備註
- 驗證：`grep -qE "sonnet.5.*\\\$2.*\\\$10|sonnet.5.*2026.08.31" .claude/refs/pilot-shared-preflights.md`

**P0-C：DAILY-TOPICS 誤植更正**
- 目標：06-30/07-01 選題文件中「數分鐘內被越獄」描述應標注為誤植（實際對象為 Fable/Mythos 出口管制事件，非 Sonnet 5 本身）
- 驗證：人工複核，無自動化 grep（描述性更正，非結構化資料）

### P1 — 本月優先（需輕量設計，2–8 小時）

**P1-1：the-loop-best-solution.md 補充「弱驗證器 confidently garbage」失敗案例**
- 目標：TEST 階段失敗案例庫新增此業界命名模式，強化 unverified_success 閘門的具體佐證
- 驗收：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md`

**P1-2：harness-meta 稽核範圍評估**
- 目標：評估是否需將「harness 供應鏈信任」（如本次 China 偵測事件類型）納入 harness-meta 稽核 checklist，而非僅稽核 workspace 自身規則
- 輸出：稽核備忘 + 是否需要新增檢查項的判斷

### P2 — 觀察中（需更多信號再決定）

**P2-1：Claude Code China 偵測官方回滾版本追蹤**
- 觸發：Anthropic 發布回滾版本號時，確認機制是否徹底移除或僅調整編碼方式
- 觀察管道：Claude Code release notes / GitHub 驗證報告後續更新

**P2-2：Claude Tag 內部細節**（延續自 06-26，第 7 天未填）
- 本日搜尋未獲得 Claude Tag 內部運作新資料（65% product PR 貢獻僅為既有數字重申），omnigent 面向已補齊，claude-tag 內部機制仍為 partial gap
- 觀察：等待 Anthropic 官方發布更多 Claude Tag 技術細節

**P2-3：Fable 5 公開恢復**（延續自 06-30）
- 監控：isfable5back.com（本日未主動查證，狀態延續）

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| loop-engineering | gap (0篇) | **filled** — 業界術語收斂 + Stop Condition 設計原則完整 | P1-1 補充失敗案例至 the-loop-best-solution.md |
| omnigent | gap (0篇，第5天未填) | **filled** — 架構/policy/沙盒機制完整 | 觀察 policy DSL 設計作為 hook 進化參考（無立即行動） |
| claude-tag | gap (0篇，第6天未填) | **partial** — 僅 omnigent 互通面向補齊，內部技術細節仍缺 | P2-2 延續觀察 |
| sonnet-5-claude-science | gap (0篇，新主題) | **filled** — 定價/定位策略/Claude Science 架構完整 | P0-B 定價矩陣更新 |
| china-detection-telemetry | gap (0篇，未確認謠言) | **filled + 狀態升級**（未確認 → 官方證實） | P0-A 補充實證案例；P2-1 追蹤回滾版本 |

---

## 下一次循環優先事項

1. **P0-A/P0-B 落實**：security-hygiene.md 補 China 偵測案例、pilot-shared-preflights.md 補 Sonnet 5 定價（本 Routine 已識別但未直接修改 `.claude/` 規則檔案，需下次 daily-research 或人工回填驗證）
2. **claude-tag gap 持續追蹤**（第 7 天未填）：若第 10 天仍無新資料，考慮於 DAILY-TOPICS 標記降級或改變搜尋角度（技術部落格 → Anthropic engineering blog 直接搜尋）
3. **China 偵測回滾版本追蹤**：Claude Code 下一版本發布時驗證是否確實移除該機制，作為 workspace 供應鏈信任的持續監控項目
