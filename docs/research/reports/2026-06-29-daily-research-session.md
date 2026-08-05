---
date: 2026-06-29
source: DAILY-RESEARCH/2026-06-29.md
topics: [claude-code-multi-agent-team-handbook, model-router-orchestrator-sakana-fugu, claude-code-cloud-vps-remote-workflow, fable5-return-imminent-pentagon-nsa-final, anthropic-claude-rate-limits-upgrade-3tier]
type: session-report
---

# Session Report 2026-06-29 — Daily Research

## 上次 P0 回填

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1 EVOLUTION-QUEUE tokenizer + computer-use 登記 | `grep -qE "tokenizer\|computer.use\|osworld" .claude/EVOLUTION-QUEUE.md` | ⏳ 未完成（EVOLUTION-QUEUE.md 不存在或無相符條目；延續至本日 P0-1） |
| P0-2 MEMORY.md 2026-06-28 session | `grep -q "2026-06-28" memory/MEMORY.md` | ✅ 已完成（2026-06-28 session 記錄存在） |

**P0-1 持續積壓根因**：EVOLUTION-QUEUE.md 可能尚未建立，或本 Routine 無寫入該檔案的授權。本日 P0-3 延伸為同步登記三條提案（含 cache_creation_input_tokens），並建議人工確認 EVOLUTION-QUEUE.md 路徑。

---

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-06-29.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch（5 主題同時搜尋）
- **頁面 Fetch**：6 次深度抓取（code.claude.com、sakana.ai、medium/0xmega、theaicareerlab.com、platform.claude.com；axios.com 返回 403）
- **識別 GAP**：4 個 gap → filled；1 個 partial → updated

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Anthropic 官方 Agent Teams 手冊：多 agent 協作的完整工程框架**（影響等級：**Critical**）

`code.claude.com/docs/en/agent-teams` 首次公開完整 Agent Teams 設計：Team Lead + 獨立 context window teammates + shared task list + mailbox 直接通訊。vs subagents 最大差異：teammates 互相通訊（不需透過 lead）。Plan Approval Gate 是 PROPOSE → APPLY gate 的原生 multi-agent 實作。Hooks（TeammateIdle / TaskCreated / TaskCompleted）可作 unverified_success 防護。建議規模：3-5 teammates，5-6 tasks/人，成本 ~15x 單一 session。

**2. Sakana Fugu：Thinker/Worker/Verifier 三角超越任何單一 frontier 模型**（影響等級：**High**）

SWE Bench Pro 73.7%（競爭對手 54–69%），LiveCodeBench 93.2%（競爭對手 85–88%）。TRINITY + Conductor 兩篇 ICLR 2026 論文驗證 orchestrator 學習路由的可行性。費用設計：使用最高層模型計費（不疊加）；合規可排除特定廠商。Fugu Ultra 固定 $5/$30/M token，適合複雜任務。

**3. Rate Limits 三層架構 + Cache-aware ITPM 是突破速率瓶頸的關鍵**（影響等級：**High**）

Start/Build/Scale 三層（含月支出上限 $500/$1,000/$200,000）；Sonnet 4.x Scale tier = 10K RPM / 10M ITPM / 2M OTPM。**Cache-aware ITPM 關鍵**：cache_read_input_tokens 不計入 ITPM（Haiku 3.5 例外），2M ITPM + 80% cache hit = 有效吞吐 10M total tokens/min。本 workspace Routines 若有效 caching，實際 ITPM 消耗遠低於 naïve 估算。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（三度延續）：EVOLUTION-QUEUE 登記三項提案**
- **提案 A（三延）**：tokenizer blind spot → security-hygiene.md 加 Unicode sanitization 警示
- **提案 B（二延）**：computer-use model-selection-grid 例外行（Opus 4.8 OSWorld 2.0 20.6%）
- **提案 C（新增）**：cache_creation_input_tokens 計入 ITPM → context-management.md Static First 原則補充 ITPM 層面理由
- 驗證：`grep -qE "tokenizer|computer.use|cache_creation" .claude/EVOLUTION-QUEUE.md && echo OK`
- **注意**：若 EVOLUTION-QUEUE.md 不存在，需先建立；建議人工確認路徑後執行

**P0-2：MEMORY.md 本日 session 記錄**
- 追加 `## Session 2026-06-29 — Agent Teams Handbook + Fugu + VPS Workflow + Rate Limits`
- 驗證：`grep -q "2026-06-29.*Agent Teams\|2026-06-29.*Fugu" memory/MEMORY.md && echo OK`

### P1 — 本月優先（需輕量設計，2–8 小時）

**P1-1（三延）：pilot-shared-preflights.md §E 更新（Fable 5 恢復後觸發）**
- 觸發條件：isfable5back.com = YES 或 Anthropic 官方公告（最快今日/明日）
- 實作：定價矩陣加 $10/$50 per 1M tokens（input/output），舊訂閱制標注已停用
- 驗收：`grep -qE "\$10.*\$50|pay.per.token|10.*50.*per.*million" .claude/refs/pilot-shared-preflights.md`

**P1-2（新增）：Agent Teams Hook 設計草稿**
- 目標：`TeammateIdle` hook → 自動 healthcheck；`TaskCompleted` hook → unverified_success 防護
- 輸出：`.claude/refs/agent-teams-hook-design.md`
- 驗收：文件存在且含兩種 hook 的 exit code 流程

**P1-3（延續）：spec 版本管理設計草稿**
- 對應 Anthropic 報告 Trend 8（Intent as Infrastructure）
- 輸出：`.claude/refs/spec-versioning-design.md`

### P2 — 觀察中（需更多信號再決定）

**P2-1：Fable 5 公開恢復（觸發 P1-1）**
- 監控：[isfable5back.com](https://isfable5back.com/)
- 行動：isfable5back.com = YES → 執行 P1-1

**P2-2：Fugu Ultra 實戰評估**
- 觸發：本 workspace xhigh effort 任務（跨模組 security audit）需要多模型協作時
- 考量：固定 $5/$30/M vs Opus 4.8 動態計費，需要實測比較

**P2-3：Agent Teams 穩定性評估（experimental 警告）**
- 觸發：v2.1.178+ 正式進入 stable 或 experimental 警告移除
- 考量：目前 `/resume` 不恢復 teammates，task status lag 問題

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| multi-agent-team-coordination-handbook | gap (0篇) | **filled** — 官方完整文件，含 hooks/架構/最佳實踐 | P1-2 Agent Teams Hook 設計 |
| model-router-orchestrator-fugu | gap (0篇) | **filled** — arxiv 技術報告 + 官網完整介紹 | P2-2 實戰評估候選 |
| cloud-vps-agent-workflow-pattern | gap (0篇) | **filled** — VPS 設置 + Routines 官方文件 | 確認本 workspace Routines 已是最佳實踐 |
| fable5-staged-return-government-framework | partial (舊) | **updated** — Day 17，Pentagon/NSA 最終簽核待完成 | 監控 P2-1，觸發 P1-1 |
| rate-limits-3tier-cache-aware | gap (0篇) | **filled** — 官方文件完整 Start/Build/Scale 數值 + cache-aware ITPM 機制 | P0-1 提案 C 登記 |

---

## 下一次循環優先事項

1. **P0-1 執行（第三次）**：人工確認 EVOLUTION-QUEUE.md 存在路徑後，登記三條提案（tokenizer / computer-use / cache_creation_input_tokens），解除三度積壓
2. **P2-1 監控**：Fable 5 恢復時立即執行 P1-1（pilot-shared-preflights.md 定價更新）
3. **P1-2 啟動**：Agent Teams Hook 設計草稿（TeammateIdle + TaskCompleted 與 unverified_success gate 整合）
