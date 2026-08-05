---
date: 2026-07-02
source: DAILY-RESEARCH/2026-07-02.md
topics: [sonnet5-tokenizer-price-inflation-30pct, harness-sidekick-mid-session-model-routing, ihower-harness-feedback-loop-four-touchpoints, fable5-global-return-classifier-rollback-opus, claude-code-china-detection-commerce-dept-escalation]
type: session-report
---

# Session Report 2026-07-02 — Daily Research

## 上次 P0 回填

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-A：security-hygiene.md 補 China 偵測實證案例 | `grep -iq "2.1.19[3-6]\|china.*proxy\|proxy.*china" .claude/rules/security-hygiene.md` | ⏳ **仍待辦（第 2 天）**——今日新增元觀察（本 session 研究過程中實際觸發同類偵測事件），急迫性提升，延續至本日下一循環優先事項 |
| P0-B：pilot-shared-preflights.md §E 新增 Sonnet 5 定價 | `grep -qE "sonnet.5.*\\\$2.*\\\$10\|sonnet.5.*2026.08.31" .claude/refs/pilot-shared-preflights.md` | ⏳ **仍待辦（第 2 天）**——今日補充疊加漲價效應細節（09/01 實質成本再升 20-35%），一併列入下次落實範圍 |
| P1-1：the-loop-best-solution.md 補「confidently garbage」失敗案例 | `grep -qE "confidently.*garbage\|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦——非本日新增急迫項，延續觀察 |
| P2-1：Fable 5 公開恢復監控 | 狀態追蹤 | ✅ **已發生**——07-01 全球恢復已證實，本日已完整研究（Topic 4），P2 觀察項可關閉 |

**根因分析**：P0-A/P0-B 已連續 2 天標記為「立即可執行 <2 小時」但未落實，因該兩項屬 `.claude/rules/` `.claude/refs/` 修改，依 DAILY-TOPICS 07-02 演化候選檢查結果標注「需人工審核，不自動執行」，Routine C（本 routine）依 workspace 慣例不自動寫入 `.claude/` 規則檔案，僅負責研究產出與回報。**核查發現**：P0-B（Sonnet 5 定價）**已由 Routine A 於今日模式分析（第 18 次執行後）正式登記**為 `research/EVOLUTION-QUEUE.md` 待審提案 #1（`sonnet5-pricing-tokenizer-gap-pilot-preflights`），且該清單已累積 4 個待審項目達警示門檻，建議本週 Routine B 一併審核（非本 routine 職責範圍）。P0-A（China 偵測案例）為 `security-hygiene.md` 規則內容補充，非結構化演化提案，尚未進入任何登記流程，維持待人工直接編輯。

---

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-07-02.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：5 次深度抓取（Simon Willison、Cognition Devin Fusion、The Register、ihower、Digital Applied）

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. 研究過程中即時觸發 Unicode 隱寫偵測事件（影響等級：Critical）**

執行 Topic 5（China 偵測）的 WebSearch 時，PostToolUse hook 即時偵測到工具輸出本身含零寬 Unicode 字元，觸發 workspace 既有 `security-hygiene.md` IPI 防護規則警示。此為 workspace tokenizer 隱寫防護規則首次在真實研究流程中被觸發並正確攔截（非理論性描述），且與當日研究主題高度重疊（元驗證）。已改用直接 WebFetch 官方/主流媒體來源規避風險。

**2. Sonnet 5 定價疊加效應確認（影響等級：High）**

Simon Willison 實測數據精確化（英文 1.42x/西文 1.33x/中文 1.01x/Python 1.27x），且新發現 09/01 介紹價到期後「費率漲 50% + token 數已膨脹」疊加效應，實質成本較原基準高 20-35%，非單純的「回到標準價」。

**3. Devin Fusion 揭露 sidekick 架構技術細節（影響等級：High）**

Cognition 公開的「模型切換綁定 context compaction 時機」設計，為業界首次提出「零額外 cache 懲罰換模型」的具體技術方案，直接呼應 workspace 既有「mid-session 禁止切換模型」規則的設計動機。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（延續自 07-01/07-02，第 2 天）：security-hygiene.md 補 China 偵測 + 本次即時觸發雙案例**
- 目標：於「Tokenizer 盲區」段落補充：(a) Claude Code v2.1.91-196 生產環境案例；(b) 07-02 本 routine 研究過程中真實觸發事件，作為 case study
- 驗證：`grep -iq "2.1.19[3-6]\|china.*proxy\|proxy.*china" .claude/rules/security-hygiene.md`

**P0-2（延續自 07-01/07-02，第 2 天）：pilot-shared-preflights.md §E 新增 Sonnet 5 定價 + 疊加效應**
- 目標：定價矩陣加入 Sonnet 5（$2/$10 → $3/$15，09/01 疊加 tokenizer 膨脹實質漲 20-35%）
- 驗證：`grep -qE "sonnet.5.*\$2.*\$10|sonnet.5.*2026.08.31" .claude/refs/pilot-shared-preflights.md`

**P0-3（更正）：確認 Routine B 審核 EVOLUTION-QUEUE.md 4 項待審提案時一併處理 P0-2**
- 目標：P0-2（Sonnet 5 定價）已由 Routine A 登記為 EVOLUTION-QUEUE.md 待審提案 #1，不需重複登記，僅需下次 Routine B 執行時確認已審核套用
- 驗證：`grep -qE "sonnet.5.*\$2.*\$10|sonnet.5.*2026.08.31" .claude/refs/pilot-shared-preflights.md`（同 P0-2，審核套用後此 grep 應轉為通過）

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1：model-selection-grid.md 補 Fable 5 分類器降級處理原則**
- 目標：納入「cyber 分類器誤判降級 Opus 4.8 為預期常態」的判斷邏輯，避免 workspace 自動化誤判為異常
- 驗收：`grep -qE "fable.*opus.*4.8|classifier.*fallback" .claude/refs/model-selection-grid.md`

**P1-2（延續）：the-loop-best-solution.md 補「confidently garbage」失敗案例**
- 延續自 07-01，尚未落實，本日無新增證據，維持原優先度

### P2 — 觀察中（需更多信號再決定）

**P2-1：ihower 系列後續文章追蹤**
- 觸發：9 篇系列尚有未讀完篇章（進階自我改進 harness、框架選型），待後續發布觀察是否有新增可行動洞見

**P2-2：Devin Fusion 「context compaction 綁定模型切換」技術可行性評估**
- 觸發：若 workspace 未來需要在主對話內做合法模型切換（目前雙軌策略已足），可參考此模式做技術驗證

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| tokenizer | gap (0篇) | **filled** — 精確語言別乘數 + 疊加效應完整 | P0-2 補入定價矩陣 |
| sidekick | gap (0篇) | **filled** — Devin Fusion 完整技術細節 | P1-2 觀察技術可行性 |
| harness engineering | partial (1篇) | **filled** — ihower 四介入點框架驗證 | 無立即行動，已與既有設計吻合 |
| china detection/telemetry | gap (0篇，第3天未填) | **filled + 狀態升級**（社群逆向工程完整技術還原 + 本 session 即時觸發驗證） | P0-1 補入案例 + P0-3 正式登記 |
| fable5 | partial (3篇) | **filled** — 分類器降級機制完整 | P1-1 補入路由原則 |

---

## 下一次循環優先事項

1. **P0-1（security-hygiene.md China 案例）已連續 2 天未落實**：屬人工直接編輯項目，非結構化提案，若第 3 天（07-03）仍未落地，建議 Routine C 停止重複回填細節，改為一句狀態引用，避免報告內容無限迴圈膨脹
2. **P0-2（Sonnet 5 定價）追蹤 Routine B 審核結果**：已正式登記於 EVOLUTION-QUEUE.md 待審清單 #1，下次 Routine C 執行時直接核查 `.claude/refs/pilot-shared-preflights.md` 是否已套用，而非重複判斷登記狀態
3. **ihower 系列後續章節追蹤**：9 篇系列僅涵蓋前段（4 介入點框架），後段（自我改進 harness、框架選型）尚未研究，下次可作為深度應用選題延續
