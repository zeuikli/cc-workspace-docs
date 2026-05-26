# Agentic Architecture Patterns（代理系統技術設計）

> **Source positions**: CathaySec 2024–now（實踐）、Forward-looking（2026+）
> **Last ingested**: 2026-04-25
> **Confidence**: medium（業界案例 + 個人 CathaySec 可應用場景；Kimi/AAR 數據來自第一手新聞來源）
> **Linted**: 2026-04-25
> **Tags**: agentic-engineering, mcp, sub-agent, harness, ai-architecture
> **Career phase**: current + forward-looking（Agentic 成熟化期 2026+）

---

## TL;DR

Agentic 系統的工程核心是「分層職責 + 決策邊界」：CLI / harness / MCP 三層各自負責不同抽象層，sub-agent 並行化需要 context isolation，自動化邊界由任務可驗證性和風險等級決定，而非 AI 能力上限。

---

## Context

架構師或 SRE Lead 在設計 AI 輔助工作流時，需要決策：工具介面選 CLI 還是 MCP server？sub-agent 怎麼拆？哪些步驟需要人工 checkpoint？此頁聚焦技術設計層，職涯轉型哲學見 [[karpathy-ai-orchestration]]。

---

## Core Methodology

### Step 1 — 建立 CLI / Harness / MCP 三層分離架構

- **What**: 將 Agentic 系統分為三個清晰層次：
  - **CLI 層**：Unix 工具（text in/out），適合短時程、一次性任務，組合靈活
  - **Harness 層**：Agent 執行框架（Claude Code SDK / orchestration logic），管理 agent loop、context、retry、tool routing
  - **MCP 層**（Model Context Protocol）：結構化 server，提供型別安全、可發現的資源與工具，適合長時程持久 agent
- **Why**: 三層混在一起是最常見的 harness debt；當 harness bug 出現（如 Opus 4.7 三個 harness bug 疊加造成 5-10% 品質退化，持續一個月），如果層次不清就無法定位是模型層、harness 層還是 API 層的問題
- **Gotcha** [CathaySec Terraform pipeline 實踐]: GCP Landing Zone 的自動化管道曾把 `gcloud` CLI 呼叫和 harness 邏輯混在同一個 Python script，debug 時很難分辨是 SDK 配置錯誤還是 gcloud 版本問題；重構後：CLI 腳本只做 auth + raw output，harness 負責 parse + routing，分離後問題一次定位

### Step 2 — MCP vs CLI 決策框架

- **What**: 依任務特性選擇工具介面：
  - 用 **CLI** 的條件：短時程（< 5 分鐘）、一次性、輸出是 text、無需持久資源狀態
  - 用 **MCP server** 的條件：長時程 agent（12+ 小時）、需要資源發現（discovery）、需要型別安全的結構化 I/O、需要 auth/權限管理的資源存取
- **Why**: 業界現實是兩者共存——CLI 勝在 Unix 組合性（pipe、redirect），MCP 勝在結構化與可靠性；過早遷移 MCP 增加基礎設施複雜度；過晚遷移則讓長時程 agent 的 error handling 難以標準化
- **Gotcha** [CathaySec ISO 27017 audit 場景]: 最初用 CLI bash 腳本跑 checkov scan + report，跑一次 OK；但要讓 agent 重複驗證多個 GCP project 時，text output parse 錯誤率高（換行符、ANSI color code），最終該場景需要 MCP structured output 才能讓 agent 穩定消費

### Step 3 — Sub-Agent 大規模並行：任務分解與 Context Isolation

- **What**: 設計可平行化的任務分解方式：
  1. **識別無狀態依賴的子任務**（每個 sub-agent 任務不需讀取其他 sub-agent 的中間輸出）
  2. **每個 sub-agent 擁有獨立 context window**（不共享、不污染主 context）
  3. **主 agent 只收結論**，中間 tool noise 留在 child context
  - 業界案例：Kimi K2.6 可自拆分任務為 300 個平行 sub-agent，連續執行 4,000+ 工具呼叫 / 12+ 小時
- **Why**: Context isolation 是平行化的前提條件；一個 sub-agent 的錯誤不應傳播到其他 sub-agent，也不該污染主 agent 的決策判斷；Karpathy autoresearch 的 16 小時連續迴圈正是靠子 agent 隔離才能穩定運行
- **Gotcha** [CathaySec multi-account evidence collection]: ISO 27017 審計需要掃描 8 個 GCP project 的 IAM policy、logging config、KMS key 設定；曾讓單一 agent 序列跑完所有 project，context window 裝滿後品質退化；改為 8 個並行 sub-agent（每個負責 1 project），主 agent 只收 JSON summary，整體時間縮短 75%

### Step 4 — Two-Slice Team：2 人 + Agent 群的人機協作模式

- **What**: 小規模人力（2 名 SRE/工程師）搭配 AI agent 群，達成過去 8-10 人的工作輸出：
  - 人類負責：架構決策、安全審查、anomaly 處置、stakeholder 溝通
  - Agent 群負責：IaC 草稿生成、log 分析、告警 triage、runbook 起草、evidence collection
  - 關鍵設計：人類是 **checkpoint gate**，不是 rubber stamp
- **Why**: Anthropic 的 AAR（Automated Alignment Researchers）實驗已驗證：5天、800 累計研究小時、$18,000 成本，agent 弱到強監督恢復率 97% vs 人類 23%；但方法論不跨模型泛化（human diversity 仍不可缺）
- **Gotcha** [CathaySec SRE 場景]: 告警 triage 委派 agent 初期，發現 agent 對 GCP Service Health 的 JSON payload 解讀有歧義（同樣的 incident type 在不同 region 的欄位結構不一致）；必須先由人類寫 parser spec，agent 才能穩定 triage；「vibe-coded app 上線後的 debug 仍需人類工程師決策」（Two-Slice 模型的已知痛點）

### Step 5 — Agent 可靠性邊界：自動化 vs 人工 Checkpoint 設計

- **What**: 依任務可驗證性 × 影響範圍，設計精確的人工介入點，而非全自動或全手動兩個極端：
  - **自動執行**：有 exit code 可驗證的任務（lint、dry-run、read-only scan）
  - **人工確認後執行**：有副作用但可預覽（`terraform plan` 通過後才 `apply`）
  - **人工全程**：prod DB 操作、IAM 變更、`prevent_destroy` 資源操作
- **Why**: 「代理可靠性不等於 AI 能力上限」是核心洞見；Karpathy 指出當前代理系統的弱點是多步驟依賴任務的錯誤累積，而非單步能力不足；設計人工 checkpoint 本質上是在「切斷錯誤累積鏈」
- **Gotcha** [CathaySec `prevent_destroy` 場景]: GCP Terraform module 的 KMS keyring 設了 `prevent_destroy = true`；曾讓 agent 直接生成完整的 `terraform apply` 腳本，agent 不知道這個 resource 有 lifecycle 保護，腳本跑到一半因 destroy 被攔截而中止，狀態部分更新；修正：agent 只生成 plan，人工確認 plan 中無 destroy 動作後才執行

---

## Concrete Numbers

| 指標 | 值 | 來源場景 |
|------|----|---------|
| Kimi K2.6 平行 sub-agent 數量 | 300 個 | Kimi K2.6 發布（2026-04-21）|
| Kimi K2.6 連續執行工具呼叫 | 4,000+ 次 / 12+ 小時 | Kimi K2.6 Agent Swarm 架構 |
| Anthropic AAR agent 研究小時 | 800 累計小時 / 5 天 | Anthropic AAR 實驗（2026-04）|
| AAR agent 弱到強監督恢復率 | 97%（vs 人類 23%）| Anthropic AAR 實驗 |
| AAR 成本 | ~$18,000 USD / 5 天 | Anthropic AAR 實驗 |
| Opus 4.7 harness bug 品質退化 | 5-10%（複雜任務）| Wisely Chen AI post-mortem |
| Harness bug 持續時間 | ~1 個月 | Opus 4.7 harness bug 事件 |
| Harness bug 修復版本 | Claude Code v2.1.116+ | Anthropic 官方修復 |
| Two-Slice 效益 | 2 人 ≈ 前 8-10 人輸出 | Chain of Thought 調查（2026-04）|
| CathaySec multi-account 並行優化 | 時間縮短 75%（8 個 sub-agent vs 序列）| CathaySec ISO 27017 audit 實踐 |
| Karpathy autoresearch 連續執行 | 16 小時 / 日 | No Priors Podcast 2026-03 |

---

## Anti-patterns（不要做）

1. **Harness 層與 CLI 層混寫，不做分層**
   - 問題：debug 時無法確定 bug 在模型層、harness 層還是 CLI 層；Opus 4.7 三個 harness bug 在一個月內沒被發現，正是因為大多數使用者沒有獨立的 harness regression test suite
   - CathaySec 教訓：GCP Landing Zone pipeline 初期把 `gcloud` CLI 和 SDK orchestration 混寫在同一 Python script，harness 升版後 parsing 邏輯悄悄 break，花 2 天才定位
   - 解：三層分離（CLI / harness / MCP）+ 為 harness 層建立獨立於模型 benchmark 的 regression test suite，每次 Claude Code 升版後跑

2. **讓 sub-agent 共享 context 或傳遞中間輸出**
   - 問題：一個 sub-agent 的錯誤（幻覺、格式偏差）傳遞到下游 sub-agent，造成雪崩式失敗；debug 時無法確定問題在哪一層
   - 解：每個 sub-agent 持有獨立 context；主 agent 只收結論（JSON summary），中間 tool noise 留在 child context；必要的共享狀態改用外部 state store（Tasks / DB）

3. **沒有 regression test 就升 harness 版本**
   - 問題：harness 升版改變 agent 行為（verbosity、effort routing、thinking cache）但 model benchmark 不會偵測到這種退化；CathaySec 使用 Claude Code 的 IaC 生成流程在 harness bug 期間輸出品質悄悄下降但沒有 alert
   - 解：建立「harness regression test suite」：挑 3-5 個有明確 ground truth 的 production 任務（如：Terraform module 生成 + checkov 通過），每次 Claude Code 升版後對比輸出

4. **用 CLI 工具設計長時程 agent 流程**
   - 問題：長時程 agent（12+ 小時、300+ 工具呼叫）依賴 CLI text output 時，ANSI color code、換行符、timeout 問題的累積出錯率遠高於 MCP structured output
   - 解：長時程 agent 流程規劃 MCP 遷移路徑（短期任務維持 CLI；> 30 分鐘 / 跨工具的 agent 改用 MCP server）

---

## Decision Tree

```
設計一個 AI 輔助自動化任務，選擇工具介面

任務執行時間？
├─ < 5 分鐘，一次性 → CLI（gcloud / terraform / kubectl）
└─ > 5 分鐘，或需要跨工具狀態 → 繼續

需要型別安全 / 結構化輸出 / 資源發現？
├─ 否 → CLI 包裝 + harness 解析
└─ 是 → MCP server（含 auth / resource management）

任務可以並行化嗎？
├─ 子任務無狀態依賴 → sub-agent 並行（每個獨立 context）
└─ 子任務有順序依賴 → 序列執行，每步 human review 節點

風險等級（生產環境副作用）？
├─ 低（唯讀、dry-run、草稿生成）→ 全自動，exit code 驗收
├─ 中（staging apply、config 變更）→ 自動 plan + 人工 approve
└─ 高（prod destroy、IAM 變更、prevent_destroy 資源）→ agent 只生成 plan，人工確認後才執行

人機協作規模？
├─ 1-2 人 × 多 agent → Two-Slice 模式（人類 = checkpoint gate，不 rubber stamp）
└─ 0 人工確認 → 只適合 read-only / 可完全 rollback 的任務
```

---

## References

- 主要來源：`research/ai-news/2026-04/synthesis-2026-04-25.md`（主題二 Agentic 架構成熟化、主題七 Two-Slice Team）
- 補充來源：`research/ai-news/q1-2026/synthesis-q1-2026.md`（2.1 代理系統成熟化、2.5 多代理治理）
- [Kimi K2.6 Multi-Agent Swarm（Modified MIT）](https://github.com/MoonshotAI/kimi-k2)
- [Claude Code Harness Post-mortem（Wisely Chen AI）](https://wisely.chen.ai)（Opus 4.7「變笨一個月之謎」）
- [Model/App/Harness 三層架構（One Useful Thing, 2026-02-18）](https://www.oneusefulthing.org)
- 職涯段：`raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- 關聯：[[karpathy-ai-orchestration]]、[[gcp-terraform-iac-patterns]]、[[iso27017-audit]]、[[gcp-landing-zone]]

## See Also

- [[karpathy-ai-orchestration]] — 職涯轉型哲學層（Software 1.0/2.0/3.0、工程師角色演變、驗收條件設計心法）；本頁聚焦技術工程設計，哲學框架見該頁
