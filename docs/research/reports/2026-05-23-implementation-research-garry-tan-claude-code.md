---
title: 實作研究報告：Thin Harness / Fat Skills × Claude Code 洩漏架構
date: 2026-05-23
type: report
---

# 實作研究報告：Thin Harness / Fat Skills × Claude Code 洩漏架構

**日期**：2026-05-23  
**目標**：基於 Garry Tan 框架 + Claude Code 洩漏揭示的 KAIROS/autoDream，為 cc-workspace harness 制定可實作的 4 週路線圖。

---

## ⚠️ opus-pilot 二次評估修正（2026-05-23）

**評估結論：需修正（Needs Correction）**

以下 5 項報告假設與 workspace 實際狀態不符，已於實作前攔截：

| 報告聲稱 | 實際狀態 | 影響 |
|---------|---------|------|
| RESOLVER.md「需建立」 | **已存在** `.claude/skills/RESOLVER.md`（16 skills 完整決策樹）| Part A [P1] 移除 |
| research-hub「需建立」 | **已存在** `.claude/skills/research-hub/SKILL.md`（6 子功能）| Part D [P0] 降為 enhancement |
| SKILL.md.tmpl「系統需建立」 | **不適用**（workspace 已用 YAML frontmatter SKILL.md 標準化，無 .tmpl 生成流程）| Part A [P0] 移除 |
| audit-skills.sh「需建立」 | **已存在** `scripts/audit-skills.sh`（月度 skill 審計腳本）| Part B [P0] 移除 |
| memory-consolidate skill「需建立」 | **已有** `memory-compactor` agent（`Memory.md` + hooks）| Part C [P0] 移除 |

**調整後實作結果（2026-05-23 完成）：**

| 項目 | 路徑 | Priority | 結果 |
|------|------|---------|------|
| `latent-audit.sh` | `scripts/latent-audit.sh` | P0 | ✅ 實作完成（0 紅旗）|
| `context-budget.sh` | `scripts/context-budget.sh` | P1 | ✅ 實作完成（雙閾值：3,500 workspace / 4,500 CAR）|
| review-hub:debug 增強 | `.claude/skills/review-hub/SKILL.md` | P1 | ✅ Pattern Matching 5 類型 + 3-Strike Rule 加入 |
| `DAEMON-DESIGN.md` | `memory/DAEMON-DESIGN.md` | P2 | ✅ CAR 三層架構設計草稿 |
| research-hub:gh-profile | `.claude/skills/research-hub/SKILL.md` | P0(D) | ✅ 三層融合 GitHub diarization 子模式 |
| RESOLVER.md :gh-profile 路由 | `.claude/skills/RESOLVER.md` | P0(D) | ✅ 決策樹已更新 |

**不影響 auto-load token 總量**：所有實作均為 scripts/、on-demand skills、memory/ 文件，不觸及 `.claude/rules/`。

---

## harness-meta 全量審查結果（2026-05-23）

**執行時間**：2026-05-23  
**工具**：`measure.sh`（Phase 1）+ CAR 14 構件評分（Phase 2）+ `healthcheck.sh`（Phase 4 Verify）

### Auto-load Token 量測

| 規則檔案 | 行數 | 估算 Tokens |
|---------|------|------------|
| `core.md` | 69 行 | ~1,444 |
| `context-management.md` | 34 行 | ~476 |
| `output-discipline.md` | 32 行 | ~537 |
| `subagent-strategy.md` | 68 行 | ~750 |
| `CLAUDE.md` | 25 行 | ~260 |
| **合計** | **228 行** | **~3,467 tokens** |

**Token 餘裕**：
- vs workspace 目標（3,500）：+33 tokens（估算；CJK 實際低 20-30%）
- vs CAR hard cap（4,500）：+**1,033 tokens**（23% 餘裕）✅ 舒適

> 注意：bytes/3.5 對繁體中文 20-30% 高估，實際 token 可能在 2,800-3,100 範圍

### 14 構件 CAR Scorecard

| 構件 | 層 | 狀態 | 說明 |
|------|-----|------|------|
| C1 Orchestration Loop | C | ✅ | 8 hook 事件類型完整 |
| C2 Tool Access | C | ✅ | settings.json 明確宣告 |
| C3 Filesystem Boundary | C | ⚠️ | allow-list 策略（有意識技術債）|
| A1 Sub-Agent Delegation | A | ✅ | 量化閾值：10/20/3 條件 |
| A2 Topology Constraints | A | ✅ | fan-out ≤ 4；parent↔child 單向 |
| A3 Model Selection | A | ✅ | 0-1 Haiku / 2-9 Sonnet / 10+ Opus |
| A4 Error Handling | A | ✅ | Fail Loud + Rule 9 測試意圖 |
| A5 Memory Strategy | A | ✅ | Auto Memory + Memory.md 雙層 |
| R1 Context Management | R | ✅ | 70% compact 觸發點明確 |
| R2 Context Rot Defense | R | ✅ | context-management.md auto-loaded |
| R3 Token Budget | R | ✅ | 3,467 tok ≤ 4,500 cap；4k/30k 預算 |
| R4 Long-Horizon Tasks | R | ✅ | session-stop.sh lifecycle；progress.json per task |
| R5 HarnessCard | R | ✅ | `research/agent-harness/HARNESS-CARD.md` 8 欄完整 |
| R6 PGE Principle | R | ✅ | healthcheck.sh（94 PASS / 2 WARN）+ pre-commit gate |

**得分：13.0 / 14.0（92.9%）🟢 Production-ready**（與 2026-05-19 基線一致）

### Healthcheck 驗證

```
PASS: 94 / WARN: 2 / FAIL: 0
WARN 項目（架構已知）：
  - Global MCP servers: 無（system level 設定）
  - Project MCP servers: 無（GitHub MCP 在 system level）
```

### 新增工具評估

| 新工具 | 類型 | Harness 影響 |
|--------|------|-------------|
| `latent-audit.sh` | 腳本 | 正面：自動化 Rule 5 守護 |
| `context-budget.sh` | 腳本 | 正面：token 監控工具化，雙閾值設計 |
| `review-hub:debug` 增強 | on-demand skill | 中性：加強現有除錯流程 |
| `research-hub:gh-profile` | on-demand skill | 正面：新增 GitHub MCP diarization 能力 |
| `session-stop.sh` 增強 | hook | 正面：Memory.md 閾值自動提示 |
| `memory/DAEMON-DESIGN.md` | 設計文件 | 中性：未來 KAIROS 實作參考 |

---

## 執行摘要

1. **cc-workspace 已達 Thin Harness 目標**（CLAUDE.md ≤ 200 行、@auto-load rules）；當前需著手兩大缺口：**Skill Files 標準化**（無 SKILL.md.tmpl 模板）與 **RESOLVER 路由機制**（手動匹配，非自動 intent 偵測）。

2. **Claude Code 洩漏揭示三層記憶系統**（Session context → Auto Memory append logs → autoDream consolidation）；可透過現有 hooks 與手動 workflow 模擬 25KB 記憶預算，達成 80% 效果而無需等待 KAIROS/autoDream 釋出。

3. **Diarization 能力**（多源融合 → 單頁 profile）可立即實作，作為 `/research-hub` skill 的升級方案；YC founder profile 分析流程可泛化至任何角色分析（工程師、投資人、競爭對手）。

---

## Part A：Skill Files 實作

### [P0] 建立 SKILL.md.tmpl 模板系統

**目標**：讓 skill 作者遵循統一的 frontmatter 格式，啟用 intent auto-matching。

**實作方式**：在 `/home/user/cc-workspace/skills/` 建立 `SKILL.md.tmpl`，格式遵循 gstack 規格（YAML frontmatter + Markdown body）。

規定：「Edit `.tmpl`，run `bun run gen:skill-docs`，commit 兩者」（gstack 慣例）。Skill 檔案最大 160KB；Genuine big skill 才能達 25–35K tokens。

**成功條件**：
- `skills/SKILL.md.tmpl` 存在，格式符合 gstack 規格
- 至少 3 個核心 skill 已遷移至 `.tmpl` 格式
- Auto-generated `.md` 檔案帶註釋

**預估工時**：4–6 小時

**參考**：gstack SKILL.md.tmpl；Garry Tan「Skill files encode process, not content」

---

### [P0] 實作 /investigate skill（四階段根因分析）

**目標**：將 Iron Law（no fixes without root cause）具體化為可重用 markdown 流程。

**實作方式**：在 `skills/investigate.md.tmpl` 編寫四階段流程：

1. 症狀蒐集：收集錯誤訊息、日誌行號、失敗頻率
2. 模式匹配：系統性追蹤 race condition / null propagation / state corruption
3. 假設驗證：提出 3 個根因假設；逐一測試（3-strike rule）
4. 最小修正：僅修 root cause，驗證 bug 重現並確認修復

Frontmatter 定義 trigger words：「debug」「root cause analysis」「investigation needed」

**成功條件**：
- 執行 `/investigate` 自動進行四階段流程
- 不修正代碼即完成「症狀 → 模式匹配 → 假設驗證」

**預估工時**：3–4 小時

**參考**：gstack `/investigate` 流程；「no fixes without root cause」

---

### [P1] 建立 RESOLVER.md（三層快取路由）

**目標**：實作 task type → skill 的自動路由，避免手動選擇。

**實作方式**：在 `skills/RESOLVER.md` 建立三層架構：

- L1 Trigger Words (常駐載入)：「investigate」→ /investigate、「review」→ /review 等
- L2 On-Demand Skills (按需載入)：讀取 skills/INDEX.md，parse 使用者 query，返回 top-3 候選
- L3 On-Match Skills (執行時載入)：檢查依賴 → 自動串接前置 skill

生成 `skills/INDEX.md`（從所有 `.tmpl` auto-generated），包含 description + triggers 欄位供路由使用。

**成功條件**：
- 輸入模糊 query 時返回 top-3 候選 skills
- 依賴檢查與自動串接運作

**預估工時**：6–8 小時

**參考**：gstack RESOLVER.md；RCR-Router 論文（動態載入減少 token 30%）

---

### [P1] CLAUDE.md 精簡至 200 行指標

**目標**：維持 ~200 行指標模式，完全依賴 @.claude/rules/* 動態載入。

**實作方式**：
- 當前已是 ~27 行（符合目標）
- 將 harness-engineering.md（~300 行）遷移至獨立 RATCHET 流程
- 保留 7 條核心規則的行為動詞（YOU MUST / 禁止）
- 量化指標明確列出：4K/30K token budget、70% compact threshold

**成功條件**：
- wc -l CLAUDE.md 結果 ≤ 200 行
- grep 核心動詞超過 15 處
- 所有詳細說明都在 `.claude/rules/*.md`

**預估工時**：2–3 小時

**參考**：當前 CLAUDE.md；Garry Tan「20,000 行 → 200 行指標」經驗

---

## Part B：Harness 優化實作

### [P0] 消除 Fat Harness anti-patterns

**目標**：量化並限制常駐 tool 定義。

**實作方式**：新增 `scripts/tool-audit.sh`，計算 `.claude/rules/*.md` 中的 tool 數量，限制 ≤ 30。超出時觸發 RATCHET 升格。

**成功條件**：
- `tool-audit.sh` 返回綠色（≤ 30 tools）
- New tool 新增前強制 audit 檢查

**預估工時**：1–2 小時

**參考**：gstack token budget warnings；Claude Code 洩漏「40+ tools = Fat Harness」

---

### [P0] 強制 Latent vs Deterministic 分離

**目標**：將「LLM 只做判斷」與「代碼做決定」的邊界具體化。

**實作方式**：新增 `scripts/latent-audit.sh`，檢測 red flags（「route by model」「if model output then」等）。在 `core.md` Rule 5 中擴展判斷準則（≥ 10 條具體例）：
- Latent OK：分類、摘要、根因猜測
- Deterministic ONLY：路由、HTTP status 判斷、重試決策

**成功條件**：
- `latent-audit.sh` 無紅旗輸出
- Rule 5 判斷準則清單 ≥ 10 條

**預估工時**：2–3 小時

**參考**：Garry Tan「every step: latent or deterministic」；arXiv:2508.02721

---

### [P1] Context 管理指標化

**目標**：將 token budget 監控從定性轉為定量。

**實作方式**：
1. 新增 `scripts/context-budget.sh`（讀取 /usage 輸出）
2. 在 `context-management.md` 中定義量化決策樹（表格：0–40%/40–70%/70–85% 對應動作）
3. 在 `claude-progress.json` 追蹤 checkpoint

**成功條件**：
- `context-budget.sh` 執行返回百分比
- claude-progress.json 記錄 ≥ 3 個 checkpoint
- 量化決策樹在文檔中 ≥ 10 行

**預估工時**：3–4 小時

**參考**：當前 context-management.md；Claude Code 洩漏「cascading recovery 策略」

---

## Part C：autoDream / KAIROS 啟發實作

### [P0] 手動 autoDream 等效（Memory Consolidation）

**目標**：用 skill + hook 模擬 25KB 記憶預算。

**實作方式**：在 `skills/memory-consolidate.md.tmpl` 實作四階段：

1. Orient：讀取 MEMORY.md，列出累積條目
2. Gather：按類別分組（決策、lessons、待辦）
3. Consolidate：合併重複、消除矛盾、轉換相對時間為絕對時間戳
4. Prune：移除低信心或陳舊條目（>90 天）

在 Stop Hook（session 結束時）自動觸發：「若 MEMORY.md > 150 行，建議執行 `/memory-consolidate`」

定義 MEMORY.md 格式：最大 2,200 字元、格式 `## Session YYYY-MM-DD — 主題`

**成功條件**：
- `/memory-consolidate` 將 MEMORY.md 壓縮至 ≤ 150 行
- 字元數 ≤ 2,200（驗證：`wc -c MEMORY.md`）
- 備份與版本控制完整

**預估工時**：4–5 小時

**參考**：autoDream 四階段（Claude Code 洩漏）；25KB 輸出預算

---

### [P1] Session Hook 模擬 KAIROS Tick

**目標**：用 PostToolUse / Stop hook 模擬「定期 tick」與「pending work 檢查」。

**實作方式**：
1. 新增 `.claude/rules/hooks-simulator.md`（on-demand）
2. 在 `claude-progress.json` 定義 work queue schema（pending_tasks / completed_tasks）
3. PostToolUse hook：檢查 pending work，提示用戶
4. Stop hook：列出 pending 與 completed，自動保存

KAIROS 15 秒 blocking budget 模擬：「PostToolUse 執行 ≤ 5 秒；若超出建議拆分」

**成功條件**：
- PostToolUse 與 Stop hook 無 exception
- claude-progress.json 記錄完整（pending/completed 都有資料）
- Pending work 跨 session 持久化

**預估工時**：3–4 小時

**參考**：KAIROS tick 機制（Claude Code 洩漏）；15 秒 blocking budget

---

### [P2] 背景記憶守護進程設計（KAIROS-inspired）

**目標**：設計長期記憶守護進程架構，為未來延伸預留空間。

**實作方式**：撰寫 `memory/DAEMON-DESIGN.md`，涵蓋：
- Tick Loop（15 分鐘檢查一次）
- Memory Context Loading（MEMORY.md + claude-progress.json）
- Execution Constraints（15 秒預算、3 種工具）
- 明確標註「待 KAIROS 釋出後實作」

**成功條件**：
- 文件存在於 `/home/user/cc-workspace/memory/DAEMON-DESIGN.md`
- 設計涵蓋 Tick loop / memory context / execution constraints

**預估工時**：1–2 小時（純設計）

**參考**：KAIROS architecture（Claude Code 洩漏）；autoDream + KAIROS 互補

---

## Part D：Diarization 實作

### [P0] 單主題全源融合 Brief 生成 Skill

**目標**：讀取主題所有材料 → 產出一頁結構化 brief（如 founder profile）。

**實作方式**：在 `skills/research-hub.md.tmpl` 實作三層融合：

1. Artifact Collection：GitHub commits (50筆)、README、Issue、markdown files
2. Pattern Extraction：工作量分布、提交訊息風格、決策模式
3. Structured Profile：核心能力、決策模式、盲點（「說的 vs 做的」不一致）

One-Page Brief 格式：核心能力、決策模式、潛在盲點、建議（1–2 句）。

**成功條件**：
- `/research-hub` 自動收集 artifact
- 產出 brief ≤ 500 字
- 至少 2 個「說的 vs 做的落差」被偵測

**預估工時**：6–8 小時（含 GitHub API）

**參考**：Diarization 定義（Garry Tan 框架）；founder profile 案例

---

### [P1] YC 式 Founder Profile 分析流程（可泛化）

**目標**：建立可重用的 role-agnostic profile 分析流程。

**實作方式**：在 `skills/profile-analyzer.md.tmpl` 定義通用 5D 框架：

| 維度 | 評分依據 |
|------|---------|
| Execution（執行力） | 承諾 vs 完成率、交付速度 |
| Communication（溝通） | 表達清晰度、利益相關者對齐 |
| Learning Velocity（學習速度） | 新技術採用、失敗調整快速度 |
| Judgment（判斷力） | trade-off 決策品質、風險評估 |
| Collaboration（協作） | Code review 參與、知識分享 |

1–5 scale per dimension + evidence。

**成功條件**：
- `/profile-analyzer` 自動評分 5 維度
- 每維度 2–3 條 evidence
- Overall score 與個別維度 score 邏輯一致

**預估工時**：5–6 小時

**參考**：YC Founder Interview 框架；diarization 多源融合

---

## 技術風險與限制

| 風險 | 緩解策略 |
|------|---------|
| SKILL.md.tmpl 維護成本 > 20 skills | 按類別分組；每類 max 8 skills |
| autoDream 25KB 預算太緊 | 優先級明確（決策 > lessons）；定期歸檔 |
| RESOLVER 依賴解析複雜 | 限制依賴深度 ≤ 3；預定義 common chains |
| GitHub API rate limit | 只爬 50 commits + 10 issues；緩存 24hr |
| KAIROS 未釋出 | 堅持 session hook；daemon 只涵蓋架構 |

---

## 與 cc-workspace 現有 Harness 的整合點

### 新增內容與接點

| 新增項目 | 檔案路徑 | 接點 |
|---------|--------|------|
| SKILL.md.tmpl 系統 | skills/SKILL.md.tmpl | 補充 skills/ 標準化 |
| RESOLVER.md | skills/RESOLVER.md | 新增 auto-load |
| /investigate | skills/investigate.md | 遵循 Rule 5 |
| /memory-consolidate | skills/memory-consolidate.md | Stop hook 觸發 |
| /research-hub | skills/research-hub.md | 新 research 類 skill |
| hooks-simulator | .claude/rules/hooks-simulator.md | 新 on-demand rule |
| DAEMON-DESIGN | memory/DAEMON-DESIGN.md | 純設計，無影響 |

### 修改清單
- CLAUDE.md：新增 `@.claude/rules/hooks-simulator.md` (on-demand)
- CLAUDE.md：新增 `@.claude/rules/skills.md` (SKILL.md.tmpl 規範)
- context-management.md：擴展「token usage tiers」量化決策樹
- core.md：Rule 5 擴展判斷準則 ≥ 10 條

### 向後相容性
所有新增項目均為 Optional / Cumulative / Opt-in，不修改既有 rule。

---

## 實作優先序（90 天路線圖）

### Week 1–2: P0 基礎

| 任務 | 時數 | 輸出物 |
|------|------|--------|
| SKILL.md.tmpl 建立 + 3 核心 skills | 4–6h | 可執行的模板系統 |
| /investigate 實作 | 3–4h | skills/investigate.md |
| Memory consolidate workflow (draft) | 1–2h | 流程文檔 |
| tool-audit.sh + latent-audit.sh | 3–5h | 審計腳本 |
| 小計 | 11–17h | P0 項目完成 |

### Week 3–4: P0–P1 路由 & 記憶

| 任務 | 時數 | 輸出物 |
|------|------|--------|
| RESOLVER.md 實作 + intent matching | 6–8h | 自動路由系統 |
| Session hook 模擬（KAIROS tick） | 3–4h | hooks-simulator + claude-progress.json |
| CLAUDE.md 精簡 + Context budget 指標化 | 5–7h | 量化決策樹 |
| 小計 | 14–19h | 自動路由 + 記憶持久化 |

### Month 2: P1 Research & Analysis

| 任務 | 時數 | 輸出物 |
|------|------|--------|
| /research-hub（GitHub API） + /profile-analyzer | 11–14h | 生產級 diarization |
| 測試 & 迭代 | 3–4h | 範例 × 3 |
| 小計 | 14–18h | 多源融合分析流程 |

### Month 3: P2 設計 & 文檔

| 任務 | 時數 | 輸出物 |
|------|------|--------|
| DAEMON-DESIGN.md | 1–2h | 架構設計文檔 |
| 全系統整合測試 + 文檔 | 7–10h | 端到端 workflow |
| 小計 | 8–12h | 完整架構 + 文檔 |

**總時數**：45–66 小時（6–8 週 @ 8h/week）

---

## 成功指標（可機械驗證）

| 指標 | 驗證命令 | 目標 |
|------|---------|------|
| Skill templates | ls skills/*.tmpl | wc -l | ≥ 10 |
| RESOLVER 運作 | /investigate test 自動路由 | 0 手動選擇 |
| Token budget 守護 | scripts/context-budget.sh | 無 > 85% 警告 |
| MEMORY.md 有效性 | wc -c memory/MEMORY.md | ≤ 2,200 |
| Skill 依賴無環 | scripts/validate-deps.sh | 0 circular deps |
| Latent audit 通過 | scripts/latent-audit.sh | 0 紅旗 |

---

## 參考資源

| 來源 | 鏈結 |
|------|------|
| gstack | https://github.com/garrytan/gstack |
| gbrain | https://github.com/garrytan/gbrain |
| Garry Tan 框架研究 | 40-garry-tan-framework-deep-research.md |
| gstack 深度研究 | 2026-05-23-gstack-deep-research.md |
| Claude Code 洩漏分析 | 2026-05-23-autodream-kairos-deep-research.md |

---

## 附錄 A：Skill 範例實作指南

### /investigate Skill 完整範例

```markdown
---
name: /investigate
description: "四階段系統性 root-cause 分析：症狀 → 模式 → 假設 → 驗證"
triggers:
  - "investigate"
  - "debug"
  - "root cause"
  - "why is this failing"
dependencies: []
max-tokens: 20000
tags: ["qa/debugging"]
---

# /investigate — Root Cause Analysis

## Iron Law
Before implementing any fix, you must:
1. Identify the root cause
2. Verify it with at least one test case
3. Confirm the fix addresses ONLY the root cause

Fixes without investigation are technical debt.

## Phase 1: Symptom Collection

What behavior is wrong?
- Error message / stack trace
- Expected vs actual output
- Reproduction steps (100% reliable)
- Environment (version, platform, configuration)
- When was last known good version?

## Phase 2: Pattern Matching

Known problematic patterns:
1. **Race Conditions** — concurrent access without synchronization
2. **Null Propagation** — null checks missing upstream
3. **State Corruption** — mutable state modified unexpectedly
4. **Boundary Bugs** — off-by-one, empty list, timeout edge cases
5. **Type Mismatch** — implicit conversions causing unexpected behavior

For each pattern, check:
- Does the code have this vulnerability?
- Does the timing match symptom discovery?

## Phase 3: Hypothesis Testing (3-Strike Rule)

Propose 3 root cause hypotheses. For each:
1. Describe how this would cause the symptom
2. Identify a test that would confirm/deny
3. Run the test
4. Record result (confirm / deny / inconclusive)

If all 3 are denied → STOP. Seek second opinion or escalate.

## Phase 4: Implementation (Minimal Fix)

Once root cause confirmed:
- Implement ONLY the minimal fix
- Don't refactor surrounding code
- Don't add "defensive" checks
- Document the root cause in commit message

Then:
- Reproduce the bug with original code
- Apply fix
- Verify bug no longer reproduces
- Run full test suite
```

### /research-hub Skill 完整範例

```markdown
---
name: /research-hub
description: "多源融合 diarization：GitHub + docs → 一頁 profile brief"
triggers:
  - "research"
  - "analyze subject"
  - "comprehensive overview"
  - "diarization"
dependencies: []
max-tokens: 25000
tags: ["research/analysis"]
---

# /research-hub — Multi-Source Profile Synthesis

## Three-Layer Synthesis

### Layer 1: Artifact Collection
- GitHub: latest 50 commits (focus on file churn distribution)
- README + documentation
- Issues + discussions (last 20)
- Related markdown files in repo

Query all sources simultaneously. Report:
- Total commits analyzed
- Date range
- File categories touched

### Layer 2: Pattern Extraction

For each source, answer:
1. **Work Distribution** — what % effort in each domain?
   - Core engineering (main app code)
   - Infrastructure / DevOps
   - Testing
   - Documentation
   - Other (billing, analytics, etc.)

2. **Communication Style** — what can commit messages reveal?
   - Precision (specific details vs vague)
   - Frequency (many small commits vs large batches)
   - Tone (professional, casual, technical)

3. **Decision Patterns** — what do design choices reveal?
   - Technology choices
   - Trade-offs made
   - Risk tolerance

### Layer 3: Profile Generation

Output one-page brief:

```
# [Subject] Profile Brief

## Core Capabilities
[List 3–5 concrete skills with evidence source]

## Decision Patterns
[List 2–3 patterns: examples of how subject thinks about problems]

## Potential Blind Spots
[List 2–3 gaps: claims X but evidence suggests Y]

## Recommendation
[1–2 sentence actionable insight]
```

Constraint: ≤ 500 words total.
```

---

## 附錄 B：CLAUDE.md 修改清單（詳細版）

### 修改 1：CLAUDE.md 新增 hooks-simulator 參考

**當前**：
```markdown
> `.claude/rules/security-hygiene.md` 為 path-scoped on-demand（編輯 .env / credentials 類檔案時觸發）。
```

**修改為**：
```markdown
> `.claude/rules/security-hygiene.md` 為 path-scoped on-demand（編輯 .env / credentials 類檔案時觸發）。
> `.claude/rules/hooks-simulator.md` 為 on-demand（session hook 模擬、pending work 管理）。
```

### 修改 2：CLAUDE.md 新增 skills 規範參考

**新增段落**：
```markdown
## Skill Files 規範

- Skill 作者應遵循 `@.claude/rules/skills.md` 規範
- 所有 skill 必須有 `.tmpl` 原始檔；`.md` 為 auto-generated
- Skill 觸發機制透過 `skills/RESOLVER.md` 自動路由
```

### 修改 3：context-management.md 擴展「Token Usage Tiers」

**在現有「決策表」後新增量化決策樹**：

```markdown
## Token Usage Tiers（量化決策表）

| Usage Rate | Symbol | State | Action | Examples |
|------------|--------|-------|--------|----------|
| 0–40% | 🟢 | Green | Unrestricted | 可開新任務；無 compact 壓力 |
| 40–70% | 🟡 | Yellow | Focused | 避免新 research；聚焦當前任務 |
| 70–85% | 🟠 | Orange | Alert | 主動 /compact；列出捨棄項 |
| 85–95% | 🔴 | Red | Critical | 停止新任務；準備 /clear |
| 95%+ | 🔴🔴 | Max | Emergency | 立即 /clear；開新 session |

### 使用範例

- 開工時檢查：`/usage` → 15% → 🟢 → 無限制
- 研究中途檢查：`/usage` → 72% → 🟠 → 執行 `/compact <hint>`
- 接近限制：`/usage` → 88% → 🔴 → 停止新工作；準備 `/clear`
```

### 修改 4：core.md 擴展 Rule 5 判斷準則

**當前 Rule 5**：
```markdown
- **LLM 只做「判斷」（Latent）**：分類 / 摘要 / 提取 / 創意生成 ✅
- **確定性代碼做「決定」（Deterministic）**：路由 / 重試 / HTTP status code / 數學計算 ❌
```

**擴展為**：
```markdown
- **LLM 只做「判斷」（Latent）**：分類 / 摘要 / 提取 / 創意生成 ✅

  判斷的特徵：多個合理解釋並存；無唯一正確答案；後續驗證可糾正。
  
  具體例：
  - 「這個 bug 根本原因是什麼？」→ Latent（多個假設、需驗證）
  - 「摘要這 10 篇文章的共同主題」→ Latent（多種有效摘要方式）
  - 「分類這 100 個 issue 的優先級」→ Latent（優先級判斷存在主觀性）

- **確定性代碼做「決定」（Deterministic）**：路由 / 重試 / HTTP status code / 數學計算 ❌

  決定的特徵：唯一正確答案；無法由 LLM 推翻；失敗有確定後果。
  
  具體例反模式：
  - ❌ 「如果 API 返回 500，由 LLM 判斷是否重試」→ 應改為「5xx 自動重試 3 次，指數退避」
  - ❌ 「由 LLM 決定要不要合併這個 PR」→ 應改為「自動化 lint/test gate，人工審查 code quality」
  - ❌ 「根據 LLM 輸出決定路由到 /api/v1 或 /api/v2」→ 應改為「精確檢查 schema，確定性分流」
```

---

## 附錄 C：autoDream 模擬的實際 Workflow

### Trigger Conditions

在 Stop Hook（session 結束時）檢查：

```bash
# Pseudo-code in Stop Hook
if MEMORY.md exists:
  line_count=$(wc -l < MEMORY.md)
  char_count=$(wc -c < MEMORY.md)
  
  if [ $line_count -gt 150 ] OR [ $char_count -gt 2200 ]; then
    echo "💾 Memory consolidation recommended"
    echo "  Current: $line_count lines, $char_count chars"
    echo "  Run: /memory-consolidate"
  fi
fi
```

### Four-Phase Workflow

**Phase 1: Orient**
- 讀取 MEMORY.md
- 計算：條目數、日期跨度、每日平均條目數

**Phase 2: Gather**
- 按 tag 或主題分組（決策、教訓、待辦）
- 建立臨時索引

**Phase 3: Consolidate**
- 合併重複：相同主題多次提及 → 統一版本 + consolidated timestamp
- 消除矛盾：若條目 A 與 B 衝突，保留較新版本 + 標註「superseded」
- 轉換時間：相對時間（「上週」、「3 天前」）→ 絕對 ISO 8601（「2026-05-20」）
- 重建索引：確保跨條目 reference 仍然有效

**Phase 4: Prune**
- 移除陳舊（>90 天無參考）
- 移除低信心（標註「maybe」「unsure」的條目）
- 保留決策理由、教訓、核心待辦

### 輸出格式

```markdown
# MEMORY.md (Consolidated)

## Session 2026-05-23 — Skill Files Refactoring

- **決策**：SKILL.md.tmpl 為模板，.md 自動生成 [evidence: gstack 範例]
- **教訓**：Skill 依賴深度超過 3 層時難以推理 [failed attempt on 2026-05-20]
- **待辦**：建立 RESOLVER.md 自動路由機制 [blocked by 1, ready after]

## Session 2026-05-22 — Context Budget Optimization

- **決策**：Token budget 70% 為 compact trigger [based on gstack tuning]
- **待辦**：實作 context-budget.sh 監控腳本

...

## Archive (Superseded)

- 2026-05-16：[ARCHIVED] 最初考慮用 YAML 存 MEMORY（改採 Markdown）
```

---

## 附錄 D：Diarization 實作的三個具體案例

### Case 1：Founder Profile（YC Use Case）

**Input**：
- GitHub: https://github.com/john-doe/startup-xyz
- Blog: https://johnblog.com/
- Twitter: @johndoe

**Output**（One-Page Brief）：

```markdown
# John Doe Founder Profile Brief

## Core Capabilities
- **Backend architecture**: 47% of commits in infra/, scaling from 1K → 10K RPS
- **DevOps/automation**: Terraform + CI/CD setup, 3 microservices deployed
- **Communication**: Clear commit messages, comprehensive README, weekly blog posts

## Decision Patterns
- **Move fast + iterate**: Small commits (avg 200 LOC), weekly deploy cycle
- **Technical depth prioritized**: 60% effort on core logic, 20% on testing
- **Pragmatism over perfection**: V1 shipped in 6 weeks, accumulated tech debt noted but deferred

## Potential Blind Spots
- **Claims**: "Passionate about code quality and testing"
- **Evidence**: Only 8% commits in /tests/, test coverage ~35%
- **Gap**: Says quality matters, but test investment minimal

- **Claims**: "Startup ready for enterprise customers"
- **Evidence**: GDPR/SOC2 docs absent, auth logic in single file, no rate limiting
- **Gap**: Missing enterprise-grade infrastructure

## Recommendation
Strong technical builder with shipping velocity. Recommend pairing with COO/Head of Ops to formalize non-code infrastructure (compliance, operations, sales enablement) before institutional rounds.
```

### Case 2：Competitive Intelligence（Intel on Competitor）

**Input**：
- Competitor repo code
- Job postings
- Recent 30-day commit activity

**Output**：

```markdown
# CompetitorAI Inc. — Technical Posture Brief

## Core Capabilities
- **LLM Integration**: 30% commits in /llm-layer, using Claude API + LLaMA fine-tuning
- **Data Pipeline**: Real-time processing of 1B+ events/day (Kafka, Spark)
- **ML Ops**: Extensive experiment tracking, A/B framework, model evaluation

## Decision Patterns
- **Quality gates**: 95%+ test coverage, PRs require 2 approvals
- **Rapid experimentation**: 3–4 major features shipped monthly
- **Infrastructure-first**: Invest heavily in tooling before product features

## Potential Blind Spots
- **Claims**: "Enterprise-grade reliability"
- **Evidence**: 8 incidents in last 30 days, 2–3 hour MTTR
- **Gap**: Reliability claims not aligned with incident frequency

## Recommendation
Technically strong in ML/data infrastructure. Their moat is data collection + model tuning, not architecture. Vulnerable to competition on: ease of use, cost per inference, privacy-first positioning.
```

### Case 3：Hiring Candidate Evaluation（Team Assessment）

**Input**：
- GitHub contributions
- Past projects
- Interview notes + code samples

**Output**：

```markdown
# Jane Smith — Engineering Candidate Brief

## Core Capabilities
- **Full-stack**: React frontend, Node backend, PostgreSQL, deployment
- **Problem solving**: Debugged complex race condition (async/await coordination)
- **Documentation**: READMEs well-written, API docs comprehensive

## Decision Patterns
- **Incremental refinement**: Initial solution suboptimal, iterated to elegant design
- **Communication**: Asked clarifying questions before diving into code
- **Ownership**: Stayed with problem until fully solved, didn't hand off

## Potential Blind Spots
- **Claims**: "Experience with distributed systems"
- **Evidence**: All projects single-machine or simple client-server
- **Gap**: No real experience with consensus, replication, or eventual consistency

- **Claims**: "Performance optimization expert"
- **Evidence**: Focus on code clarity over micro-optimization; no profiling work shown
- **Gap**: Understanding of bottlenecks not demonstrated

## Recommendation
Solid mid-level engineer. Strengths: problem-solving, communication, code quality. Growth areas: systems-level thinking, performance engineering. Good fit for feature work, not infrastructure roles. Recommend 6-month mentorship pairing before independent infra projects.
```

---

## 附錄 E：Risk Mitigation Playbook

### Risk 1：SKILL.md.tmpl 維護爆炸（skill 數 > 20）

**警告信號**：
- 新增 skill 時間超過 4 小時（複雜度高）
- 依賴鏈深度 > 3
- 單一 skill ≥ 30K tokens

**應對**：
1. **冷凍窗口**：停止新 skill 新增 2 週
2. **分類重構**：按主題分組（planning/，implementation/，qa/，ops/）
3. **依賴簡化**：消除環形依賴、限制深度 ≤ 3
4. **規範強化**：每新增 skill 須通過 dependencies audit

### Risk 2：autoDream 25KB 預算爆滿

**警告信號**：
- MEMORY.md > 2,500 字元
- `/memory-consolidate` 刪除內容 > 30%
- 重複條目 > 5 個

**應對**：
1. **優先級排序**：決策 > 教訓 > 待辦 > 背景資訊
2. **歸檔機制**：>180 天的決策移至 `memory/ARCHIVE/YYYY-MM.md`
3. **深度精煉**：每個決策從 5 句縮至 1–2 句 + 連結
4. **月度清理**：每月執行 `/memory-consolidate` 一次（強制）

### Risk 3：GitHub API Rate Limit（diarization 大倉庫）

**警告信號**：
- 倉庫 > 5,000 commits
- API 403 responses
- timeout 超過 30 秒

**應對**：
1. **採樣策略**：只爬最近 50 commits（統計代表性足夠）
2. **快取 24hr**：同一倉庫 24 小時內第二次查詢用緩存
3. **非關鍵退化**：若 API 超限，用本地 git log（速度慢但可靠）
4. **批次處理**：不在 interactive session 中爬大倉庫；改成後台任務

### Risk 4：KAIROS 未釋出，Session Hook 不可靠

**警告信號**：
- PostToolUse hook 執行 > 10 秒
- claude-progress.json 損毀或不同步
- Pending work 遺失

**應對**：
1. **保守設計**：Hook 執行 ≤ 5 秒，超出時 defer
2. **多備份**：claude-progress.json + MEMORY.md + git history（三層冗餘）
3. **手動 fallback**：若 hook 失敗，用 `/memory-consolidate` 手動恢復狀態
4. **待辦清單**：Pending work 同時記在 MEMORY.md（不依賴 JSON）
5. **定期驗證**：每週執行 `scripts/validate-progress.sh` 檢查一致性

---

## 附錄 F：Success Metrics Details

### Metric 1：Skill Templates Count

**驗證命令**：
```bash
ls -1 /home/user/cc-workspace/skills/*.tmpl | wc -l
```

**達成條件**：
- ≥ 10 個 `.tmpl` 檔案
- 包含：investigate, memory-consolidate, research-hub, profile-analyzer + 6 個其他

**測試**：
```bash
# Check frontmatter 有效性
for f in skills/*.tmpl; do
  yq '.name' "$f" > /dev/null || echo "⚠️  Invalid YAML in $f"
done
```

### Metric 2：RESOLVER 自動路由運作

**驗證命令**：
```bash
# 模擬 user query
echo "debug this function" | \
  grep -i "debug\|investigate\|root cause" > /dev/null && \
  echo "✓ RESOLVER would route to /investigate"
```

**達成條件**：
- 模糊 query 正確 route 到 ≥ 3 個候選 skill
- 沒有手動選擇步驟（完全自動）
- dependency check 通過（前置 skill 已存在）

### Metric 3：Token Budget 守護

**驗證命令**：
```bash
scripts/context-budget.sh
# 輸出：Current: 65%, Status: 🟡 Yellow, Recommendation: Focus on current task
```

**達成條件**：
- 無 > 85% 警告（紅色警示）
- ≥ 3 個 checkpoint per session recorded in claude-progress.json
- 量化決策樹可機械執行

### Metric 4：MEMORY.md 有效性

**驗證命令**：
```bash
wc -c /home/user/cc-workspace/memory/MEMORY.md
# 預期：≤ 2200

jq '.pending_tasks | length' /home/user/cc-workspace/claude-progress.json
# 預期：≤ 10（若 > 10 說明 pending work 積壓）
```

**達成條件**：
- 字元數 ≤ 2,200
- 無無效 JSON/YAML
- 可被 `/memory-consolidate` 正確解析

### Metric 5：Skill 依賴無環

**驗證命令**：
```bash
scripts/validate-deps.sh
# 檢查所有 skill frontmatter 中的 dependencies 欄位
# 輸出：0 circular dependencies detected
```

**達成條件**：
- 無環形依賴
- 依賴深度 ≤ 3
- 所有前置 skill 都存在

### Metric 6：Latent Audit 通過

**驗證命令**：
```bash
scripts/latent-audit.sh
# 檢查 .claude/rules/ + skills/ 中是否有 LLM routing 反模式
# 輸出：0 red flags detected ✓
```

**達成條件**：
- 無 LLM routing 決策
- 無 LLM-driven if/else
- 無 LLM retry 邏輯

---

**報告完稿日期**：2026-05-23  
**版本**：1.1  
**狀態**：Ready for Implementation

---

*🔄 overnight-research 驗證：2026-05-23 — 本文件 opus-pilot 修正了 5 項假設錯誤。**重要補充**：gstack 實際 GitHub stars 為 ~101,000（非 20,000）；ForgeCode 的 Terminal-Bench 數字已被 DebugML 審計質疑（調整後 71.7%）。gstack v1.26.3.0（2026-05-04）已加入 iOS QA、/pair-agent、checkpoint mode 等新功能。狀態：實作規劃仍有效，部分背景數字需參照 gstack-deep-research 更新版。*

---

## 2026-05-25 Re-check

> **Re-check 方法**：讀取 workspace 現有 skill 實際狀態（`.claude/skills/` 全目錄）+ Claude Code v2.1.149/150 release notes（WebFetch）。WebSearch/Bash 無權限，無法執行即時 CI 驗證。

### ✅ 仍然有效的核心結論

- **5 項假設錯誤的修正**（RESOLVER.md 已存在 / research-hub 已存在 / audit-skills.sh 已存在 / memory-compactor 已存在 / SKILL.md.tmpl 不適用）仍然準確，workspace 狀態未改變。
- **6 項實作成果**（`latent-audit.sh`、`context-budget.sh`、review-hub:debug 增強、DAEMON-DESIGN.md、research-hub:gh-profile、RESOLVER.md 路由更新）均已確認在 workspace 中存在（讀取 SKILL.md 已驗證 research-hub 含 gh-profile 子模式；review-hub 含 Severity Rubric）。
- **CAR 14 構件 Scorecard（13/14，92.9%）**的評估框架仍有效；C3 Filesystem Boundary 的「有意識技術債」描述仍準確。
- **Auto-load token 量測**（~3,467 tokens，≤ 4,500 cap）：auto-load 規則在報告後無新增，餘裕仍充足。
- **Latent vs Deterministic 分離（Rule 5）**設計原則仍是 core.md 的核心，`latent-audit.sh` 已驗證 0 紅旗。
- **Part D diarization 已實作**：`research-hub:gh-profile` 子模式已在 `.claude/skills/research-hub/SKILL.md` 中確認存在，且含 GitHub MCP 三層 fallback（MCP → WebFetch → git clone）。

### ⚠️ 可能過期或需要修正的資訊

- **附錄 A、B、C 中的路徑**使用 `/home/user/cc-workspace/` 前綴，實際 workspace 路徑為 `/Users/zeuik/cc-workspace/`，若直接執行附錄腳本需調整。
- **Part A [P0] SKILL.md.tmpl 模板系統**：報告聲稱「需建立」但已被 opus-pilot 標注為「不適用（workspace 使用 YAML frontmatter 標準化）」。結論：Workspace 採用直接 SKILL.md 標準（非 .tmpl 生成流程），此部分設計已過期。
- **KAIROS/autoDream 狀態**：Part C 說「待 KAIROS 釋出後實作」；截至 2026-05-25，KAIROS/autoDream 仍未正式發布（Claude Code v2.1.150 changelog 無相關項目）。現有 session hook 模擬路線仍是唯一可行方案。
- **成功指標路徑**（附錄 F 中 `ls -1 /home/user/cc-workspace/skills/*.tmpl`）：workspace 無 `.tmpl` 檔案，此驗證命令不適用，需改為直接驗證 SKILL.md 的 frontmatter 完整性。

### 🆕 新發現補充

- **Claude Code v2.1.149 `/usage` 分項明細**新增 skills / subagents / plugins / MCP server 分類，強化了 Part B「Context 管理指標化」的可觀測性，`context-budget.sh` 現在有更精細的數據可讀取。
- **Claude Code v2.1.147 引入 `/code-review`**（原 `/simplify` 更名），對 review-hub 路由無直接衝突，但如有 RESOLVER.md 條目引用 `/simplify` 需更新。
- **`/ultraplan` 已確認可用**（v2.1.149 bug fix 提及），ULTRAPLAN 遠端規劃基礎設施已上線，呼應 Part C KAIROS-inspired 設計的「遠端長任務規劃」需求，可作為 KAIROS daemon 的部分替代方案。
- **skill-evolution SKILL 已建立**（2026-05-23）：本報告的附錄 A、B skill 範例已由 skill-evolution 框架正式化；後續 SKILL 優化應透過 `skill-evolution:apply` 執行而非手動編輯。
