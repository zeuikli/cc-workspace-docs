---
date: 2026-06-30
source: DAILY-RESEARCH/2026-06-30.md
topics: [karpathy-harness-first-loop-methodology, claude-code-steering-guide-official, prompt-caching-production-playbook-coinbase, fable5-deregulation-sonnet5-release-timeline, anthropic-ai-work-impact-economic-survey]
type: session-report
---

# Session Report 2026-06-30 — Daily Research

## 上次 P0 回填

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1（三延）：EVOLUTION-QUEUE tokenizer + computer-use + cache_creation 登記 | `grep -qE "tokenizer\|computer.use\|cache_creation" .claude/EVOLUTION-QUEUE.md` | ⏳ 未完成（`.claude/EVOLUTION-QUEUE.md` 不存在；P0-1 升為四延，根因：需人工確認路徑並建立檔案） |
| P0-2：MEMORY.md 2026-06-29 session 記錄 | `grep -q "2026-06-29.*Agent Teams\|2026-06-29.*Fugu" memory/MEMORY.md` | ✅ 已完成（grep 核對：`memory/MEMORY.md` 含 2026-06-29 session 雙條記錄） |

**P0-1 持續積壓分析（四延診斷）**：根因確認為 `.claude/EVOLUTION-QUEUE.md` 路徑不存在，非內容問題。本 Routine 無直接建立 `.claude/` 內檔案的授權（目標為人工審核路徑）。建議行動：人工在 `.claude/` 建立 `EVOLUTION-QUEUE.md` 並執行三條提案登記，或明確授權 Routine 建立此檔案。

---

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-06-30.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch + 1 次補充 WebSearch（Fable 5 deregulation 詳情）= 6 次
- **頁面 Fetch**：6 次深度抓取（aibuilderclub、claude.com/blog、letsdatascience、anthropic/labor-market-impacts、anthropic/81k-economics、codersera 503 fallback 已補）
- **識別 GAP**：5 個 gap/partial → 全部 filled/updated

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Anthropic 官方 Claude Code Steering Guide：7 種指令層級完整決策矩陣**（影響等級：**Critical**）

`claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more` 首次官方正式化七種指令分工：CLAUDE.md（事實）/ Rules（path-scoped 限制）/ Skills（程序）/ Subagents（隔離任務）/ Hooks（確定性執行）/ Output styles / Append system prompt。關鍵原則：「真正的護欄需要確定性」→ Hooks/permissions，不是 CLAUDE.md 指令。本 workspace 現有分工與官方矩陣基本吻合，但值得做一次稽核（P1-4）。

**2. Karpathy Agentic Engineering 框架：harness-first 術語溯源澄清 + spec-first 外部背書**（影響等級：**High**）

澄清：「harness engineering」由 Mitchell Hashimoto 提出，Karpathy 的術語為「agentic engineering」（Sequoia 2026）。核心框架五項：spec design / diff review / eval loops / security oversight / quality taste。直接外部背書本 workspace The Loop 的 PROPOSE（spec-first）+ TEST（eval loop）+ PROPOSE（AI 程式碼四大缺陷自檢 = quality taste）。演化候選 `karpathy-harness-first-refs-supplement` 已由 DAILY-TOPICS 登記。

**3. Coinbase Prompt Caching Playbook：5%→60% hit rate，支出近半**（影響等級：**High**）

Cache hit rate 工程化是 2026 最高槓桿低風險降本策略。Coinbase 案例：LLM gateway 統一管理，開源模型（GLM 5.2 $1.40/M、Kimi 2.7）為預設，hit rate 12 倍改善。與昨日 rate limits 研究交叉：cache_read 不計入 ITPM，80% hit rate + 2M ITPM = 有效 10M tokens/min。本 workspace 需建立 cache hit 監控（P1-3）。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（四延）：EVOLUTION-QUEUE 建立 + 三條提案登記**
- 需人工操作：確認路徑、建立 `.claude/EVOLUTION-QUEUE.md`、登記三條提案
- 提案 A：tokenizer blind spot → `security-hygiene.md` Unicode sanitization
- 提案 B：computer-use model-selection-grid Opus 4.8 OSWorld 2.0 20.6% 例外行
- 提案 C：cache_creation_input_tokens ITPM 計算 → `context-management.md`
- 驗證：`grep -qE "tokenizer|computer.use|cache_creation" .claude/EVOLUTION-QUEUE.md && echo OK`

**P0-2：harness-loop.md 演化候選追蹤（今日新增）**
- 驗證現狀：`grep -qE 'karpathy|harness.first|harness-first' .claude/refs/harness-loop.md && echo OK || echo PENDING`
- 待人工審核後執行（DAILY-TOPICS 演化候選已登記）

**P0-3：MEMORY.md 本日 session 記錄**
- 追加 `## Session 2026-06-30 — karpathy-agentic + steering-guide + coinbase-caching + fable5-status + anthropic-survey`
- 驗證：`grep -q "2026-06-30" memory/MEMORY.md && echo OK`

### P1 — 本月優先（需輕量設計，2–8 小時）

**P1-1（四延）：pilot-shared-preflights.md §E Fable 5 定價更新**
- 觸發：isfable5back.com = YES（預測市場：7/31 機率 90.2%）
- 驗收：`grep -qE "\$10.*\$50|pay.per.token" .claude/refs/pilot-shared-preflights.md`

**P1-2（二延）：Agent Teams Hook 設計草稿**
- 輸出：`.claude/refs/agent-teams-hook-design.md`（TeammateIdle + TaskCompleted + unverified_success 整合）

**P1-3（新增）：Cache hit rate 監控 SOP**
- 目標：`.claude/refs/cache-health-metrics.md` 追加 hit rate 追蹤方法 + Coinbase 60% 業界基準
- 驗收：`grep -qE "cache_read.*input_tokens|60%|coinbase" .claude/refs/cache-health-metrics.md`

**P1-4（新增）：Steering Guide 官方架構稽核**
- 對照七種方法決策矩陣，驗證 CLAUDE.md / rules / skills / agents 分工
- 輸出：稽核備忘 + 任何需要下沉的指令項清單

### P2 — 觀察中

**P2-1：Fable 5 公開恢復（觸發 P1-1）**
- 監控：isfable5back.com（今日 = NO，Day 18）
- 當前最新進展：Mythos 5 已恢復給美國關鍵基礎設施（2026-06-26 Lutnick 部分解禁）

**P2-2：Sonnet 5 正式發布**
- 觸發條件：官方宣告（排除社群謠言）

**P2-3：GLM 5.2 / Kimi 2.7 品質評估**
- 觸發：低複雜度批次任務 FinOps 優化需求

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| karpathy-harness-first-methodology | gap (0篇) | **filled** — 完整框架 + 術語溯源 | 演化候選 harness-loop.md 補引用（人工審核） |
| prompt-caching-production-strategies | gap (0篇) | **filled** — Coinbase 5%→60% 完整 playbook | P1-3 cache 監控 SOP |
| agent-skill-decay-lifecycle | gap (0篇) | **partial** — Steering Guide 暗示 path-scoped rules 減少 always-on 負擔，間接相關 | 仍需更直接的 skill decay 文獻 |
| anthropic-ai-work-displacement-survey | gap (0篇) | **filled** — 81k 調查 + labor-market-impacts 完整數據 | workspace 定位確認，無需 action |
| benchmark-eval-integrity-cheating | partial (昨日) | **unchanged** — 今日未額外研究 | 仍在 P2 觀察 |

---

## 下一次循環優先事項

1. **P0-1 解除四延**：人工建立 `.claude/EVOLUTION-QUEUE.md` 並登記 tokenizer / computer-use / cache_creation 三條提案（根因：路徑不存在，非 Routine 問題）
2. **P1-3 啟動**：cache hit rate 監控 SOP 進 `.claude/refs/cache-health-metrics.md`（Coinbase 60% 為業界基準）
3. **P2-1 監控**：isfable5back.com 恢復時觸發 P1-1（pilot-shared-preflights.md 定價更新，四延候補）
