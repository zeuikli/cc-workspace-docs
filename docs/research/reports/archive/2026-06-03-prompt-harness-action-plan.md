# 可執行計劃書 — 將 Prompt 研究發現套用到 cc-workspace Harness

**日期**：2026-06-03 | **Branch**：`feature/prompt-caching-engineering-research`
**對應研究報告**：`2026-06-03-prompt-caching-management-engineering.md`
**研究方法**：平行 researcher subagents fan-out（模擬 overnight-research 搜尋階段 + research-hub 信度分層 + autoresearch 缺口收斂方法論），非直接呼叫三 skill runner。
**Target（釘死假設）**：把三主題發現套用到本 cc-workspace harness（CLAUDE.md 為 stable-prefix cache、`context-management.md` 已有 caching 規則、4 auto-load 規則）。本計劃為**提案**，破壞性 APPLY 前須 gate 使用者。

---

## 0. 現況基線（改前先讀，§R8）

本 harness 已落地的 prompt 工程實踐：

| 已有 | 位置 | 對應報告章節 |
|---|---|---|
| CLAUDE.md = 穩定前綴、放最前不動 | context-management.md §Static First | A.4 四層結構 |
| Mid-session 禁切 model/tool/CLAUDE.md | context-management.md | A.4 cache 失效控制 |
| NLAH（context 放 HEAD/TAIL） | context-management.md | C.3 lost-in-the-middle |
| Compact hint（保留前綴語意） | context-management.md | A.4 compact 須同前綴 |
| Token budget（4k/task, 30k/session） | context-management.md §R6 | — |
| 正向指令優先於禁止 | output-discipline.md | C.1 positive>negative 🟢 |
| Tests Verify Intent | core.md §R9 | C.4 eval-driven |
| auto-load byte cap（canonical） | core.md §Framework Integrity | A.1 token 經濟 |

**結論**：本 harness 在 caching「穩定前綴」與 engineering「正向指令」上已對齊官方一手。**缺口**集中在三處：① cache 可觀測性（無 hit-rate 監控）② cross-provider / TTL 決策（規則未提）③ prompt-as-code 版本治理（auto-load 規則本身未當 prompt artifact 做 eval-driven 版控）。

---

## 1. 可執行步驟（按 ROI 排序，每步可機械驗證）

### Step 1 — context-management.md 補「Cache 可觀測性」段（高 ROI，低風險）

**動作**：在 `context-management.md` §監控 區塊新增 cache 健康指標規則。

**具體 edit**（提案內容，APPLY 前 gate）：
```markdown
## Cache 健康指標（agentic 生產紅線）
- `cache_hit_rate = cache_read_input_tokens / input_tokens`；長跑 session 應 > 0.7。
- 觸發 incident：hit_rate 驟降 → 先查是否 mid-session 切了 model/tool/CLAUDE.md（A.4 四大破快取源）。
- 動態資訊（時間戳/檔變更）一律經 `<system-reminder>` 注入 messages，**不寫進 CLAUDE.md 前綴**。
- Agentic 長任務（工具迴圈 >5min）→ 啟用 1h TTL（`ENABLE_PROMPT_CACHING_1H=1`），代價 2× 寫入費但避免 mid-loop cache miss。
```
**驗證**：`grep -c "cache_hit_rate" .claude/rules/context-management.md` ≥ 1；`bash scripts/healthcheck.sh` FAIL=0；`wc -c` 確認 auto-load byte 仍 < 18,000 上限。
**風險**：增加 auto-load byte。先量增量 `wc -c` 再決定是否納入 auto-load 或改 on-demand。

### Step 2 — 新增 on-demand 規則 `prompt-lifecycle.md`（中 ROI，零 auto-load 成本）

**動作**：建 path-scoped on-demand 規則檔（編輯 `.claude/rules/`、`CLAUDE.md`、`research/prompts/` 時觸發），承載「不夠高頻、不該佔 auto-load」的完整知識：cross-provider 決策表、cross-model 遷移 re-express 原則、structured-output 陷阱、eval-driven prompt 迭代。

**理由**：報告 Section A.1/B.4/C.2 是「需要時查」而非「每 session 載入」→ on-demand 是正確 NLAH placement（避免無謂 auto-load byte 膨脹，符合 Framework Integrity）。
**驗證**：檔案存在、有 frontmatter schema、`README.md` Path-scoped 表新增一列；healthcheck PASS。

### Step 3 — prompt-as-code：把 auto-load 規則當 prompt artifact 做 eval-driven 版控（高 ROI，呼應既有 autoload-evolution）

**動作**：本 harness 已有 `/autoload-evolution` 閉環 + Falsifiable Prediction 機制（見 MEMORY.md）。將報告 C.4「Better Prompts Hurt」+ B.1 prompt-as-code 整合進該閉環的驗收標準：
- 每次改 auto-load 規則 → 必附 falsifiable prediction（已有慣例）**+ 明確 eval 條件**（R1–R12 behavioral 存活、healthcheck FAIL=0、byte cap）。
- 規則變更走 feature branch + PR（已有），等同 prompt registry 的 staged deployment（B.1）。
**驗證**：下次 `/autoload-evolution` cycle 套用此標準；git log 顯示規則變更皆經 PR。
**現況**：本 harness 已 80% 符合（Falsifiable Prediction + PR 流程）— 此步是「形式化既有實踐」，非新建。

### Step 4 — research/prompts/ 加 cross-model 遷移備註（低 ROI，低風險）

**動作**：本 repo 有 `research/prompts/` 9 個 prompt 檔（agent-orchestration、rule-engineering 等）。在 `research/prompts/INDEX.md` 加一段「模型遷移注意」：re-express ≠ translate、Claude 偏 XML、hardest-cases-first、prompt 不可跨 generation 直接移植（C.1 / B.4）。
**驗證**：`grep -i "re-express\|cross-model\|遷移" research/prompts/INDEX.md` ≥ 1。

### Step 5 — 注入防禦對接既有 subagent-strategy.md（中 ROI）

**動作**：`subagent-strategy.md` 已有 `<untrusted_objective>` 包裹規則（Agent Input Security）。在該段補一行指向報告 B.3：indirect injection 經 RAG/外部內容擴大攻擊面，PostToolUse 外部資料同樣須包裹 + allowlist 心智模型（InstructDetector 的 API-only 等效：把外部內容當 data 不當 instruction）。
**驗證**：`grep -i "indirect\|injection\|untrusted" .claude/rules/subagent-strategy.md` 命中既有 + 新增。

---

## 2. 不做的事（§R2/R3 — 避免過度工程）

- ❌ 不引入 Langfuse/Braintrust 等外部 prompt registry：本 harness 用 Git + PR + autoload-evolution 已是輕量 prompt-as-code，引入 SaaS 是過度工程。
- ❌ 不建 cross-provider 抽象層：報告 B.4 反模式明確 — model-specific 優於 generic。本 harness 鎖定 Claude，無多 provider 需求。
- ❌ 不為 cache 監控寫自動化 daemon：cache_hit_rate 是手動 `/usage` 可查的健康信號，daemon 是 speculative。

---

## 3. 落地順序與 gate 點

| 順序 | Step | 風險 | Gate |
|---|---|---|---|
| 1 | Step 1（cache 可觀測性） | 增 byte | APPLY 前確認 byte 增量 |
| 2 | Step 2（on-demand 新規則） | 低 | 確認 schema + README |
| 3 | Step 5（注入防禦對接） | 低 | grep 驗證 |
| 4 | Step 4（prompts INDEX 備註） | 極低 | grep 驗證 |
| 5 | Step 3（prompt-as-code 形式化） | 流程改變 | 下次 autoload-evolution cycle |

**所有 Step 走 `/autoload-evolution` 閉環：≤1 規則/cycle、≤50 行 diff、eval 回歸 ≥5pp → `git revert`**（本 harness 既有約束，不另立）。

---

## 4. 驗收條件（R4，機械可驗）

- [ ] 本計劃書存在於 `research/reports/`，含 ≥5 具體步驟（file + edit + verify 三要素）✅
- [ ] 每步有可機械驗證的 verify 指令（grep / wc / healthcheck）✅
- [ ] 計劃明確區分「做 / 不做」並給理由（§R2/R3）✅
- [ ] 對接既有 harness 機制（autoload-evolution / subagent-strategy / context-management）而非另起爐灶 ✅
- [ ] 落地時：每 Step APPLY 後 `bash scripts/healthcheck.sh` FAIL=0 且 auto-load byte < 18,000

---

## 5. 一句話總結

本 harness 在「穩定前綴 + 正向指令」已對齊 2026 官方一手；最高 ROI 的三個動作是 **① 加 cache_hit_rate 可觀測性 ② 把 cross-provider/遷移知識放 on-demand 規則（零 auto-load 成本）③ 把 auto-load 規則正式當 eval-driven prompt artifact 版控**（既有 autoload-evolution 已 80% 達成）。其餘外部工具與抽象層均為過度工程，明確不做。
