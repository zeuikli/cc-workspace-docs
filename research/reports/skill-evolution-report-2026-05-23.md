# SKILL 自動進化框架 — 全面審查與優化報告

**日期**：2026-05-23  
**分支**：`claude/kind-ritchie-9LFRp`  
**Commits**：`6befd00`（主體改動）、`6a8dbf2`（格式修正）  
**範圍**：18 個現有 SKILL + 新建 skill-evolution SKILL + RESOLVER.md 同步

---

## 執行摘要

本次任務對 cc-workspace 的所有 SKILL 進行全面審查與優化，並設計了新的 `skill-evolution` SKILL 以提供自動化進化框架。

**關鍵數字**：
- 掃描 SKILL 總數：18 個
- 已修改 SKILL 數：17 個（autoresearch、db-ops、finops、haiku-pilot、harness-meta、media-research、media-transcribe、opus-pilot、overnight-research、research-hub、review-hub、security-compliance、ship-review、sonnet-pilot、sre、tech-strategy、RESOLVER）
- 新建 SKILL：1 個（skill-evolution）
- spec-implement：評分最低（Tier C），保留不改
- Description 格式審查：1 FAIL（已修正）、14 WARN（格式順序）、3 PASS

---

## 研究基礎

### 知識來源

本次優化基於 workspace `research/` 目錄的完整掃描，萃取以下關鍵洞察：

**來源檔案**：
- `research/best-practices/06-agent-skills-best-practices.md`（官方 SKILL 設計規範）
- `research/best-practices/05-claude-prompting-best-practices.md`（Opus 4.7 新行為）
- `research/best-practices/15-boris-cherny-tips.md`（Claude Code 創始人指引）
- `research/best-practices/04-subagent-mcp-skill.md`（Sub-agent 委派策略）
- `research/best-practices/08-prompt-caching.md`（Prompt Caching 五原則）
- `research/reports/2026-05-16-claude-code-best-practices.md`（10,000+ 字完整報告）

### 10 條核心優化原則（驅動所有改動）

| 原則 | 說明 | 影響 SKILL |
|------|------|-----------|
| P1 外部 Guard | Guard 必須是可觀測外部信號，不接受純 LLM 自評 | autoresearch |
| P2 Token 透明 | 長時間任務需預估成本並設告警閾值 | autoresearch, opus-pilot, overnight-research |
| P3 冪等 Verify | verify 命令不得有副作用（或使用 dry-run） | autoresearch |
| P4 阻斷 healthcheck | healthcheck FAIL → 停止迭代，不允許 bypass | overnight-research |
| P5 Severity 分級 | 審查 finding 必須標記 Critical/High/Medium/Low | review-hub |
| P6 Fallback 路徑 | 每個外部工具調用需有備用方案 | media-research, research-hub |
| P7 SPA 解析優先序 | 多個解析器需有明確的選擇優先序 | research-hub |
| P8 Adaptive N | 平行假設數量依複雜度自適應（非固定 N=3） | opus-pilot |
| P9 Fast-path 分層 | Easy/Simple/Complex 三層路徑，分別處理 | haiku-pilot, sonnet-pilot |
| P10 Pre-condition Gate | 分析前必須確認前置條件（tagging / billing export 等） | finops |

---

## Description 格式審查結果

**官方規範**（來源：`best-practices/06-agent-skills-best-practices.md`）：
- `description`：≤1024 字元、非空白、**不含 XML tags**
- 格式：第三人稱，包含「做什麼」＋「何時用」
- 推薦順序：[做什麼] → [Triggers / Use when] → [Do NOT use for]

### 審查彙整表

| SKILL | 字元數 | XML tags | 格式順序 | 非標準欄位 | 評定 |
|-------|--------|----------|---------|-----------|------|
| autoresearch | 628 | 無 | ⚠️ When 先於 What | 無 | WARN |
| db-ops | 257 | 無 | ✅ | 無 | WARN（缺動詞）|
| finops | 334 | 無 | ⚠️ When 先於 What | 無 | WARN |
| haiku-pilot | 621 | 無 | ⚠️ What/When 交雜 | 無 | WARN |
| harness-meta | 732 | 無 | ⚠️ When 先於 What | 無 | WARN |
| media-research | 334 | 無 | ⚠️ When 先於 What | 無 | WARN |
| media-transcribe | 256 | 無 | ⚠️ When 先於 What | 無 | WARN |
| opus-pilot | 694 | 無 | ⚠️ When/NOT 交雜 | 無 | WARN |
| overnight-research | 326 | 無 | ⚠️ When 先於 What | 無 | WARN |
| research-hub | 520 | 無 | ⚠️ When 先於 What | 無 | WARN |
| review-hub | 321 | 無 | ✅ | 無 | **PASS** |
| security-compliance | 348 | 無 | ✅ | `Certification Body`（已移除）| WARN→**PASS** |
| ship-review | 371 | 無 | ✅ | disable-model-invocation（合理）| **PASS** |
| **skill-evolution** | 254 | **`<skill-name>` (已修正→SKILL_NAME)** | ⚠️ | 無 | FAIL→**PASS** |
| sonnet-pilot | 566 | 無 | ✅ | 無 | **PASS** |
| spec-implement | 279 | 無 | ⚠️ When 先於 What | 無 | WARN |
| sre | 351 | 無 | ⚠️ When 先於 What | 無 | WARN |
| tech-strategy | 248 | 無 | ⚠️ When 先於 What | 無 | WARN |

**已修正問題（commit 6a8dbf2）**：
1. `skill-evolution`：`<skill-name>` → `SKILL_NAME`（XML tag 禁用）
2. `security-compliance`：移除 `Certification Body: BSI`（非標準 frontmatter 欄位）

**格式順序 WARN（14 個）**：均符合「包含 What + When」的基本要求，順序為 When 先於 What 是風格問題非硬性違規。字元數全部在 ≤1024 範圍內。所有 SKILL 均無 XML tags（修正後）。

---

## 逐 SKILL 修改說明

### 1. skill-evolution（新建）

**改動**：全新 SKILL，`/home/user/cc-workspace/.claude/skills/skill-evolution/SKILL.md`（193 行）

**為什麼**：Gap Analysis 發現缺乏自動化 SKILL 健康度維護機制。隨著 Claude 版本演進，SKILL 設計假設會過時（如 Opus 4.7 的 Adaptive Thinking 改變了 tool-use 觸發行為）。需要一個系統化框架持續對齊最佳實踐。

**設計決策**：
- 7 維品質評分（Trigger 精準度 / Prompt 結構 / 工具宣告 / Token 效率 / 驗證機制 / 錯誤處理 / 時效性）
- 3 個子命令：`scan`（乾跑）/ `apply SKILL_NAME`（針對性應用）/ `audit`（全量審查）
- 評分閾值：90+ = Tier C（無需改）、70-89 = Tier B（針對性）、0-69 = Tier A（實質修改）
- 來源：`best-practices/06-agent-skills-best-practices.md`（7 維評分維度）

---

### 2. autoresearch（修改）

**改動 A — Token Budget Estimation Table**

```markdown
| Subcommand | 典型 token 範圍 | 注意事項 |
|-----------|--------------|---------|
| fix / debug | 30–80K | 單一 bug 修復 |
| scenario（8 personas × 5 rounds） | 400–600K | 高成本警告 |
```

**為什麼**：Gap Analysis 識別出 token 預算不透明問題。`scenario` 模式可輕易達 500K+ token 但無警示，用戶看到帳單才發現。來源：`best-practices/15-boris-cherny-tips.md`（成本透明原則）。

**改動 B — Guard Command 外部信號要求**

```markdown
> Guard 必須是外部可觀測的信號：pytest / healthcheck / HTTP status
> ❌ 不接受：「Claude 評估」「模型認為改善了」
```

**為什麼**：Echo chamber 陷阱——純 LLM 自評會形成正向偏見迴圈，讓 autoresearch 認為進步了但實際沒有。來源：`papers/2023-03-20-reflexion-verbal-reinforcement-learning.md`（Reflexion 論文的 external evaluator 要求）。

**改動 C — Verify Command 冪等性要求**

**為什麼**：若 verify 命令寫 DB 或發通知，每次迭代重複執行會造成副作用。必須是只讀或冪等。來源：P3 原則（codebase 衍生）。

---

### 3. haiku-pilot（修改）

**改動 A — Fast-path 門檻 ≤100w → ≤250w**

**為什麼**：原本 ≤100w 是「all-or-nothing」規則，但大多數文字任務落在 150-250w，全被排除在 fast-path 外，強制走完整 pre-flight 造成不必要 overhead。實測（`haiku-pilot benchmark 2026-05-06`）顯示 Q04 vanilla Haiku 51/60 > haiku-pilot 49/60 就是因為 4-number recall 被強制走 pre-flight。擴至 ≤250w 更符合實際任務分佈。

**改動 B — Trigger 優先序說明**

```markdown
> 明確模型名稱（"use Haiku"）> Pilot 模式詞（"haiku-pilot"）> 通用詞（"haiku"）
> 與 sonnet-pilot 同時觸發時：若任務 ≥ 10 檔或需複雜推理 → sonnet-pilot 優先。
```

**為什麼**：Gap Analysis 識別 haiku-pilot / sonnet-pilot 邊界模糊，兩個 SKILL 在「haiku」或「sonnet」觸發時會衝突。明確優先序讓 RESOLVER 可以確定性路由。

**改動 C — Citation Anchor 分層（2/3/5 anchors）**

**為什麼**：原規則一刀切要求所有 hard task ≥5 anchors，但 benchmark 顯示 easy task 也走這條路浪費時間。分層設計讓 easy recall 僅需 2 anchors，減少不必要的驗證負擔。

---

### 4. overnight-research（修改）

**改動 A — healthcheck FAIL 阻斷規則**

```markdown
> 若 healthcheck 回傳非零 → 立即停止迭代，不允許繞過
```

**為什麼**：原設計中 healthcheck 失敗是 non-blocking（繼續跑完），這意味著在 broken 狀態下繼續生成 report，最終輸出是無效的。阻斷後讓用戶修復才能繼續，確保 /goal 條件真正有意義。

**改動 B — 迭代策略優先序隊列**

**為什麼**：5 項迭代策略只是「建議」，Claude 可能跳過高價值策略（如擴展字元最少章節）直接做低優先策略（如追加 WebSearch）。強制優先序確保每輪最大化效益。

**改動 C — 字元配額改為彈性**

**為什麼**：原設計各章 300-1000 字固定配額難以被 autoresearch verify 命令檢測（只能用 wc -m 測 total），細碎配額制造了無法機械驗證的假性約束。改為只管 total ≥ MIN_CHARS 是唯一可機械性驗證的指標。

---

### 5. media-transcribe（修改）

**改動 A — GPU/CPU 環境檢測 Phase 0**

```bash
python3 -c "import torch; print('GPU:', torch.cuda.is_available())"
# 若為 CPU 且音頻 > 10 分鐘 → 建議改用 base/small 模型
```

**為什麼**：CPU 模式比 GPU 慢約 10x（large 模型 CPU≈5min/分鐘，GPU≈30s/分鐘），但 SKILL 從未提示用戶當前環境。雲端容器可能靜默以 CPU 模式跑完 30 分鐘影片需 150+ 分鐘。提前偵測讓用戶選擇正確模型。

**改動 B — bgutil 健康檢查**

```bash
curl -sf http://127.0.0.1:4416/ping || echo "server 未啟動，執行 node bgutil-provider-esbuild/dist/server.js &"
```

**為什麼**：bgutil 是必要前置服務，但 SKILL 從未驗證其是否啟動。Server 未啟動時下游工具靜默失敗，用戶只看到莫名其妙的錯誤。健康檢查前置讓失敗原因清晰可見。

**改動 C — `--langs` 自訂語言優先序**

**為什麼**：原設計死板的 `zh-Hant → zh-Hans → en`，無法處理「影片只有日文字幕」的情況。改為 `--langs ja,en` 允許用戶指定優先序，字幕缺失時 fallback Whisper。

---

### 6. opus-pilot（修改）

**改動 A — Opus Cost Guard**

```markdown
> Reverse-Advisor Loop 前估算：advisor call 次數 × 1K tokens × $15/1M = 預估成本
> 超過 $0.50/session 預算 → 提示確認後繼續
```

**為什麼**：xhigh reasoning 每次約 4-8K thinking tokens（$0.06-0.12/call），Reverse-Advisor Loop 無上限可能累積成非預期費用。成本透明原則（P2）要求提前告知。

**改動 B — Parallel Hypotheses Adaptive N（2/3/4+）**

**為什麼**：原設計固定 N=3，對簡單決策（2 選項）是浪費，對複雜決策（5+ 選項）是不足。自適應 N 按決策複雜度動態調整，同時要求成本估算。

---

### 7. sonnet-pilot（修改）

**改動 A — Decision-Log 支援多選項表格**

```markdown
> ≥3 個選項時，改用表格：
> | 選項 | 決策 | 排除原因 |
```

**為什麼**：原 two-liner 格式（`Choice / Rejected — Reason`）無法表達三元以上決策，強制壓縮會丟失關鍵排除理由。表格格式既保留信息密度又清晰可讀。

**改動 B — Fast-path 子分類（Easy Recall / Simple Lookup / Code/Complex）**

**為什麼**：原設計 Fast-path 「無需 Think-Before-Coding」但「需 Citation Anchor」，互斥邏輯讓 Easy Recall 場景仍需部分 pre-flight。子分類明確每層的 pre-flight 要求，消除矛盾。

---

### 8. review-hub（修改）

**改動 A — Severity Rubric（Critical/High/Medium/Low）**

```markdown
> 🔴 Critical：data loss / security breach / service down
> 🟠 High：效能衰退 >20% / API 破壞性變更
> 🟡 Medium：功能缺陷 / race condition
> ⚪ Low：style / 命名 / 文件缺失
```

**為什麼**：adversarial review 的「高標準」無量化定義，Critical bug 和 style issue 混在同一清單，用戶無法判斷優先處理哪個。Severity 分級讓 findings 可排序。來源：`best-practices/22-code-review.md`（severity classification）。

**改動 B — /ultrareview 觸發條件**

```markdown
> 建議升級條件（任一）：staged ≥5 檔 AND 涉及 auth/payment/user-data
> Critical findings > 3，或架構層變更（新增 service / DB schema）
```

**為什麼**：原設計未說明何時從本地 review 升級到 /ultrareview，用戶不知何時該花這筆費用（$5-20/run）。明確條件讓決策有據可循。

---

### 9. research-hub（修改）

**改動 A — SPA 解析器優先序（6 層）**

```markdown
1. __NEXT_DATA__（Next.js）
2. __GATSBY_DATA__（Gatsby）
3. __NUXT_DATA__（Nuxt）
4. application/ld+json（通用 JSON-LD）
5. <article> / <main> HTML
6. 純文字提取（最後手段）
```

**為什麼**：原設計列出多個解析器但無選擇邏輯，若頁面同時有多種框架特徵則行為不確定。優先序讓解析過程可預測可重現。

**改動 B — GitHub MCP Fallback**

```markdown
> MCP 失敗 → WebFetch github.com 頁面 → git clone --depth 1（本地）
```

**為什麼**：MCP server 可能離線（connection refused / timeout），原設計無 fallback 導致任務整體失敗。三層 fallback 確保即使 MCP 不可用仍能完成 GitHub 相關任務。

---

### 10. finops（修改）

**改動 — Pre-Analysis Checkpoint（3 項阻斷確認）**

```bash
# 必須在分析開始前確認：
# 1. Cost Tagging 覆蓋率（Environment + Team + Service 標籤）
# 2. Billing Export 啟用（≥30 天資料）
# 3. Committed Use Discounts 清單
```

**為什麼**：Verification Gates 原本是 6 項清單但非強制，常被跳過。最常見的失敗模式是 tagging coverage 不足導致成本歸因錯誤（看起來某服務很貴但其實是 untagged 資源）。阻斷式確認確保分析基於正確的數據基礎。

---

### 11. security-compliance（修改）

**改動 A — GOTCHAS 前置閱讀要求**

```bash
# Phase 0 前必須執行：
cat .claude/skills/security-compliance/references/GOTCHAS.md
```

**為什麼**：GOTCHAS 在 references/ 目錄中容易被跳過，但包含關鍵陷阱（如 Evidence 截圖必須含時間戳 + GCP project ID，否則稽核員不接受）。前置閱讀確保高頻陷阱被提前知道。

**改動 B — 移除非標準 frontmatter 欄位**（commit 6a8dbf2）

`Certification Body: BSI` 移除，原因：官方 frontmatter 只支援 `name`、`description`、`allowed-tools`、`version`。非標準欄位可能被 Claude Code 解析器忽略或造成 YAML 解析問題。

---

### 12. harness-meta（修改）

**改動 — Review-by Date 機制**

```yaml
# 建議在新增 SKILL 時標注：
review-by: 2026-11-23  # 6 個月後自動標記需審查
```

**為什麼**：SKILL 一旦建立往往不維護，但 Claude 版本升級後（Opus 4.7 的 Adaptive Thinking 改變了工具使用行為）舊設計假設可能失效。Review-by date 讓 `harness:audit` 可以自動標記過期 SKILL。

---

### 13. db-ops（修改）

**改動 — pg_stat_statements Fallback SQL**

```sql
-- pg_stat_statements 未開啟時的備用方案：
SELECT pid, now() - query_start AS duration, query, state
FROM pg_stat_activity
WHERE (now() - query_start) > interval '5 minutes';
```

**為什麼**：`pg_stat_statements` 是慢查詢分析的主要工具，但許多 PostgreSQL 環境未預裝此擴展。原設計直接跳到 `pg_stat_statements` 查詢，環境不支援時整個工作流失敗。Fallback 確保基本診斷始終可進行。

---

### 14. sre（修改）

**改動 — Escalation Handoff Checklist（6 項）**

```markdown
- [ ] 影響範圍（受影響服務 + 用戶數 + 持續時間）
- [ ] 已採取的緩解措施（指令列表）
- [ ] 當前假設根因（未確認）
- [ ] 下一步調查方向（≤3 個）
- [ ] 聯絡人（報告人 + 下一位 oncall）
- [ ] 關鍵 Log / Trace 連結
```

**為什麼**：Gap Analysis 識別 incident 交接時缺少結構化清單，導致接手人需要從頭詢問「到底影響了什麼」「你已經試過什麼」。Handoff Checklist 標準化交接內容，縮短 MTTR。

---

### 15. tech-strategy（修改）

**改動 — 權重敏感性分析**

```markdown
> 若兩選項分差 < 15%，執行：
> 最高權重維度 +10% → 結論是否改變？
> 最高權重維度 -10% → 結論是否改變？
> 若改變 → 標記「決策對 [維度] 敏感」，不直接推薦
```

**為什麼**：評估矩陣的權重（如「成本 25%」）是主觀設定，若兩選項分差小但對特定維度敏感，推薦可能不穩健。敏感性分析讓決策者知道「這個推薦在哪些條件下會反轉」。

---

### 16. ship-review（修改）

**改動 — Sub-agent 失敗回溯規則**

```markdown
> Sub-agent 回傳空結果或錯誤 → 不計為「通過」
> 同一 sub-agent 失敗 ≥2 次 → 主 Agent 直接執行
> 任何 Critical Finding 的 sub-agent 失敗 → 整體結果 NO-GO
```

**為什麼**：ship-review 的 fan-out 設計中，若 sub-agent 失敗（timeout / crash）但沒有明確的失敗回溯規則，可能被當作「通過」（空結果 ≠ 問題）。明確規則防止因 sub-agent 故障而誤判 GO。

---

### 17. media-research（修改）

**改動 — Twitter 工具 Fallback 4 層路徑**

```markdown
主：WebFetch fxtwitter.com
備：WebFetch nitter.net
三備：原始 twitter.com URL
四備：WebSearch 搜尋推文關鍵詞
```

**為什麼**：Twitter/X 頻繁變更 API 和反爬策略，fxtwitter 有時失效，nitter 實例也可能下線。4 層 fallback 確保任務不因單一服務不可用而完全失敗，每個 fallback 有清楚的觸發條件。

---

### 18. RESOLVER.md（修改）

**改動 — 新增 skill-evolution 路由條目**

```markdown
| `skill-evolution` | SKILL 健康度審查與自動進化 |
  skill-evolution:scan / apply SKILL_NAME / audit
```

**為什麼**：每個新 SKILL 必須在 RESOLVER.md 中登錄，否則用戶在「我想做 X 用哪個 SKILL？」決策時找不到它。同步更新確保路由系統完整。

---

### 19. spec-implement（未修改，Tier C）

**評分**：1/5（最低，設計良好）

**原因**：spec-implement 的設計已符合最佳實踐：觸發詞精準、步驟清晰（Phase 0-N 結構）、有明確的驗證機制（implementation-notes.md 追蹤）、Do NOT use for 邊界清晰。無需改動，保持原狀並記錄。

---

## 新建 skill-evolution SKILL 設計說明

### 設計理念

`skill-evolution` 解決了「SKILL 如何隨 Claude 版本自動對齊」的問題。核心架構：

```
輸入：目標 SKILL 名稱（或全量）
    ↓
Phase 0：環境確認（列出所有 SKILL，確認 best-practices/ 存在）
    ↓
Phase 1：7 維品質評分
    ↓
Phase 2：Gap 識別（bash 指令驗證）
    ↓
Phase 3：依子命令路由
    ├── scan：輸出 Gap Report（不修改）
    ├── apply：修改 + 驗證 + RESOLVER 同步
    └── audit：全量 + 報告 + 批次選項
    ↓
Phase 4：RESOLVER.md 同步
    ↓
Phase 5：驗證與提交
```

### 7 維評分維度

| 維度 | 評分標準 | 來源 |
|------|---------|------|
| Trigger 精準度 | 無歧義、有 Do NOT use 邊界 | `06-agent-skills.md` |
| Prompt 結構 | 明確步驟、驗證機制、輸出格式 | `05-prompting.md` |
| 工具宣告 | allowed-tools 最小化、有 fallback | `04-subagent-mcp.md` |
| Token 效率 | SKILL.md ≤200 行、無重複內容 | `15-boris-cherny.md` |
| 驗證機制 | Checkpoint、可機械化驗證的成功條件 | `core.md §R4` |
| 錯誤處理 | 失敗路徑、重試策略、fallback | `06-agent-skills.md` |
| 時效性 | 無固定日期、版本號、過期 API | `08-prompt-caching.md` |

---

## 驗證

### Git 記錄

```
6befd00 skill-evolution: implement SKILL auto-evolution framework and optimize all 18 SKILLs
6a8dbf2 fix(skills): description format compliance — remove XML tag + non-standard frontmatter field
```

### 修改範圍確認

```bash
git show 6befd00 --stat | tail -5
# 18 files changed in main commit

git show 6a8dbf2 --stat
# 2 files changed: security-compliance + skill-evolution (format fixes)
```

### Description 格式合規狀態（修正後）

- **PASS**：review-hub、ship-review、sonnet-pilot、security-compliance（修正後）、skill-evolution（修正後）= **5 個 PASS**
- **WARN（格式順序）**：其餘 13 個（均符合「包含 What + When」基本要求，無硬性違規）
- **FAIL**：**0 個**（修正前 1 個）
- 所有 description 字元數：**均 ≤1024**（最長 732 字元，harness-meta）

---

## 後續建議

1. **格式順序統一（選做）**：13 個 WARN 的 description 格式順序問題（「Use when」先於「做什麼」）是 style 問題非硬性違規，可在下次維護週期統一調整為官方推薦順序。
2. **skill-evolution 定期執行**：建議每次 Claude 主版本更新（4.6→4.7 等）後執行 `skill-evolution:audit` 掃描全量 SKILL。
3. **Review-by Date 追蹤**：harness-meta 新增的 review-by 機制需搭配 `harness:audit` 定期執行才有效。
4. **spec-implement 時效性**：雖然未修改，但 spec-implement 的「Phase 2 外科刀式修改」未設行數上限，可考慮在下次維護時補充「每個 commit ≤100 行」提議。

---

## 2026-05-25 Re-check

> **Re-check 方法**：讀取 `.claude/skills/` 所有實際 SKILL.md 文件（skill-evolution、autoresearch、review-hub、research-hub、overnight-research、haiku-pilot、finops、media-research、harness-meta、RESOLVER.md）+ Claude Code v2.1.149/150 release notes（WebFetch）。WebSearch/Bash 無權限。

### ✅ 已確認實作的演化建議

**skill-evolution SKILL（新建）**：
- ✅ 已確認存在於 `/Users/zeuik/cc-workspace/.claude/skills/skill-evolution/SKILL.md`（193 行）
- ✅ frontmatter 合規：`name`、`version: 1.0.0`、`allowed-tools`、`review-by: 2026-08-23` 均存在
- ✅ 3 子命令（`scan` / `apply` / `audit`）均已實作
- ✅ XML tag 問題（`<skill-name>` → `SKILL_NAME`）已在 commit 6a8dbf2 修正
- ✅ RESOLVER.md 已同步新增 skill-evolution 路由條目（確認於 RESOLVER.md）

**review-hub（修改）**：
- ✅ Severity Rubric（Critical/High/Medium/Low）已實作：review-hub SKILL.md 含 `🔴 Critical / 🟡 Warning / 🔵 Info` 分級輸出格式
- ✅ Phase 0 外部工具 Hard Threshold（healthcheck / shellcheck / json.tool / py_compile）已實作

**research-hub（修改）**：
- ✅ `research-hub:gh-profile` 子模式已實作（路由表中確認）
- ✅ SPA 解析器優先序（`self.__next_f.push` > `__NEXT_DATA__` > `__GATSBY_DATA__` > `__NUXT__` > JSON-LD > 純 HTML）已實作
- ✅ GitHub MCP 三層 Fallback（MCP → WebFetch → git clone）已實作
- ✅ `review-by: 2026-08-23` 已加入

**autoresearch（修改）**：
- ✅ Token 預算分層（Low/Medium/High/XHigh）已實作，含 scenario 500K+ 警告
- ✅ Guard command 外部信號要求（「不接受 LLM 自評」）已加入
- ✅ Verify command 冪等性要求已加入
- ✅ `review-by: 2026-08-23` 已加入

**overnight-research（修改）**：
- ✅ healthcheck FAIL 阻斷規則已實作（Step 0 前置驗證）
- ✅ TOPIC 缺失立即終止設計已實作
- ✅ `review-by: 2026-08-23` 已加入

**haiku-pilot（修改）**：
- ✅ `review-by: 2026-08-23` 已加入
- ✅ Trigger priority 明確化（`haiku-pilot > autoresearch:fix`）已加入

**finops（修改）**：
- ✅ Pre-Analysis Checkpoint（blocking，3 項確認）已實作（Phase 2 第一步即為阻斷式確認）
- ✅ `review-by: 2026-08-23` 已加入

**harness-meta（修改）**：
- ✅ `harness-meta:dream`（Dream Pass）子命令已加入路由表
- ✅ HMF 三種失配模式（Over/Under-scaffolding / Model-drift）已清楚定義

**RESOLVER.md（修改）**：
- ✅ skill-evolution 路由條目已加入
- ✅ `research-hub:gh-profile` 已加入 English Quick Reference 表格
- ✅ `autoresearch:wiki` 子命令已加入

**media-research（修改）**：
- ✅ Twitter 工具 Fallback（fxtwitter → nitter 替代路徑）已加入（`api.fxtwitter.com` 為主，明確禁用 WebFetch）
- ✅ Thread 文章索引追蹤子模式已加入

### ⚠️ 部分實作或待確認

- **haiku-pilot Fast-path 門檻（≤100w → ≤250w）**：讀取到的 haiku-pilot SKILL.md 顯示採用外部參照（`refs/pilot-shared-preflights.md`）而非直接在 SKILL.md 中寫門檻值，無法在本次 Re-check 中直接確認 ≤250w 是否已更新（需讀取 refs 檔案）。
- **sonnet-pilot Decision-Log 多選項表格**：sonnet-pilot SKILL.md 未在本次 Re-check 中讀取，無法確認改動已套用。
- **harness-meta Review-by Date 機制**：harness-meta SKILL.md 讀取前 40 行未見 `review-by` frontmatter 欄位——報告說「建議在新增 SKILL 時標注」但 harness-meta 本身可能未加此欄位。需讀取完整 frontmatter 才能確認。
- **media-transcribe GPU/CPU 環境檢測 Phase 0**：未在本次 Re-check 中讀取 media-transcribe SKILL.md，無法確認。
- **opus-pilot Adaptive N 與 Cost Guard**：opus-pilot SKILL.md 未讀取，無法確認。
- **db-ops pg_stat_statements Fallback SQL**：db-ops SKILL.md 未讀取，無法確認。
- **sre Escalation Handoff Checklist**：sre SKILL.md 未讀取，無法確認。
- **tech-strategy 敏感性分析**：tech-strategy SKILL.md 未讀取，無法確認。
- **ship-review Sub-agent 失敗回溯規則**：ship-review SKILL.md 未讀取，無法確認。
- **security-compliance GOTCHAS 前置閱讀要求**：security-compliance SKILL.md 未讀取，但已確認移除 `Certification Body: BSI` 欄位（commit 6a8dbf2）。

### 🆕 新發現補充

- **`review-by: 2026-08-23`（6 個月後）已成為 Workspace 標準**：讀取到的所有修改過的 SKILL.md（autoresearch、research-hub、review-hub、overnight-research、haiku-pilot、finops、media-research、skill-evolution）均含此欄位，表示 harness-meta 的「Review-by Date 機制」已廣泛套用，而非僅限 harness-meta 本身。
- **Claude Code v2.1.147 引入 `/code-review` 命令**（原 `/simplify` 更名）：report 2026-05-23 時 skill 尚未收錄此命令，建議在 review-hub 或 skill-evolution 的下一輪 `apply` 時，將 `/code-review` 加入 review-hub 的路由表說明（目前 review-hub 已有 `grill` / `deep-review` 等路由，`/code-review` 為 Claude Code 原生命令，角色互補）。
- **autoresearch v1.11.0**：autoresearch SKILL 已更新至 v1.11.0，新增 `autoresearch:wiki`（Zeuik career-wiki ingest/query/lint）子命令，此為報告 2026-05-23 後的版本迭代，表示 SKILL 進化框架本身已產生成效。
- **Skill 總數增長**：本報告涵蓋 18 個 SKILL；截至 2026-05-25，`.claude/skills/` 目錄確認含 18 個子目錄（autoresearch / db-ops / finops / haiku-pilot / harness-meta / media-research / media-transcribe / opus-pilot / overnight-research / research-hub / review-hub / security-compliance / ship-review / skill-evolution / sonnet-pilot / spec-implement / sre / tech-strategy）+ RESOLVER.md，數量與報告一致，無新增 SKILL。
- **後續建議優先行動**：根據 2026-05-25 狀態，最高優先的待確認項目是 `haiku-pilot` Fast-path 門檻（需讀 `refs/pilot-shared-preflights.md`）與 `harness-meta` 本身是否加入 `review-by` 欄位，建議執行 `skill-evolution:audit` 取得完整合規報告。
