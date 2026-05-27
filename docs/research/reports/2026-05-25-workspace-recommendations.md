---
title: "cc-workspace 改動建議：基於 84 篇論文的可執行計畫"
date: 2026-05-25
type: report
---

# cc-workspace 改動建議：基於 84 篇論文的可執行計畫

**生成日期**：2026-05-25 | **來源報告**：`2026-05-25-papers-analysis.md`
**論文依據**：84 篇（73 MD + 11 PDF），涵蓋 Harness Engineering / Memory / LLM Infrastructure / Agent Coordination / Benchmark / Safety 六大領域

> 本文件為純改動建議，研究報告本體見 `2026-05-25-papers-analysis.md`。

---

## 計畫 A：Harness Engineering 強化（優先度 P1）

**來源**：`2026-03-12`、`2026-04-14`、`2026-03-25`、`2026-04-23-car`

**目標**：將 workspace harness 從 H1 級提升至 H2-H3 級

**具體步驟**：

```bash
# Step 1：CLAUDE.md 精簡審核（目標 <60 行核心規則）
wc -l CLAUDE.md

# Step 2：建立 docs/ 結構化知識庫
mkdir -p docs/architecture docs/decisions docs/quality

# Step 3：工具模式審查（MCP 工具清單精選）
cat .claude/settings.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('mcpServers',{}), indent=2))"

# Step 4：子 agent fan-out 上限驗證（目前 .claude/rules/subagent-strategy.md 已設 4）
grep "Fan-out" .claude/rules/subagent-strategy.md
```

**Prompts 模板（可直接使用）**：

```
[Harness Health Check Prompt]
審查以下 harness 配置是否符合最佳實踐：
1. CLAUDE.md 是否 <60 行（錨定效應警告）？
2. MCP 工具數量是否 ≤5 個？
3. AGENTS.md 是否只含非可發現資訊？
4. hooks 是否含後向壓力機制？
依 2026-03-12、2026-02-23、2026-04-23-car 標準評分（H0-H3）。
```

---

## 計畫 B：記憶系統升級（優先度 P2）

**來源**：`2026-05-13-useful-memories`（PDF 完整版）、`2025-05-30-memory-os`、`2025-04-28-mem0`、`2026-03-05-beyond-context-window`

**目標**：實現 Episodic-First 記憶架構，防止整合失真

**ARC-AGI 量化依據**（PDF 直接引用）：Stream 整合模式（每次互動後自動合併）→ 第 10 輪後準確率 52.6%，第 20 輪後 46%（從 100% 跌落）。batch 整合（每 50 輪一次）→ 保持 100%。原始軌跡保留 → 與 batch 整合相當。

**具體步驟**：

1. 保留原始事件層（MEMORY.md 中保留最近 5 個 session 完整紀錄，不即時摘要壓縮）
2. 整合頻率降低（改為每 5-10 session 一次 batch 整合，`memory-compactor` 只在明確達到閾值時觸發）
3. 衝突標記機制（整合前比對是否有矛盾記憶，標記後凍結，不自動覆寫）
4. AutoMode 引入（整合時讓 agent 自選 Retain/Delete/Consolidate，而非強制全部整合）

**Prompts 模板**：

```
[Memory Consolidation Gate Prompt]
在執行記憶整合前，評估：
1. 此記憶是否包含衝突資訊？（若是 → 標記，不整合）
2. 整合後是否可還原至原始事件？（若否 → 僅摘要，保留原始）
3. 此記憶的任務類型是否跨域混批？（若是 → 分開整合）
依 2026-05-13 AutoMode 原則：優先 Retain，次選 Delete，最後才 Consolidate。

格式：
- 決策：[Retain / Delete / Consolidate]
- 原因：<1句>
- 衝突標記：<若有>
```

---

## 計畫 C：Context Engineering 優化（優先度 P2）

**來源**：`2026-01-31-dont-break-cache`、`2026-05-12-lost-in-the-middle`、`2026-03-05-beyond-context-window`

**目標**：減少 30% token 消耗，同時保持精度

**具體步驟**：

1. 靜態快取前綴策略（CLAUDE.md + rules 永遠放最前，加 `cache_control` 標記）
2. 關鍵資訊位置策略（重要上下文放首段或末段，避免中間位置）
3. 10 輪 compact 觸發（實證 10 輪為成本-精度等價點）

**Prompts 模板**：

```
[Context Placement Audit Prompt]
審查當前 system prompt 結構：
1. 靜態資訊（CLAUDE.md rules）是否在最前？（快取效率）
2. 最重要的約束/目標是否在首段或末段？（U 形效能曲線）
3. 動態工具結果是否在快取標記之後？（避免破壞快取）
依 2026-01-31 和 2026-05-12 標準評估。
改進建議：<結構化重排方案>
```

---

## 計畫 D：技能庫策展（優先度 P3）

**來源**：`2026-02-13-skills-bench`、`2026-04-22-skill-learn-bench`、`2026-03-12-skill-issue`

**目標**：人工策展技能 +16.2pp，防止 skill 爆炸（>3 技能性能下降）

**具體步驟**：

1. 技能品質審計（具體性/基礎性/正交性三維度評估）
2. 每次會話限 2-3 個技能加載
3. 新技能必須外部評估門控（人工確認後才能加入庫）

**Prompts 模板**：

```
[Skill Quality Audit Prompt]
評估技能 [SKILL_NAME] 的品質：
1. 具體性：是否包含非通用、領域特定的指令？（0-10 分）
2. 基礎性：是否減少任務失敗的根本原因？（0-10 分）
3. 正交性：與現有技能是否有重疊？（0=完全重疊，10=完全正交）
4. SWE 域技能 ROI 最低（+4.5pp）；優先其他域（安全/架構/研究）。
依 2026-02-13、2026-04-22 標準判斷：保留 / 刪除 / 合併。
```

---

## 計畫 E：評估獨立性強化（優先度 P3）

**來源**：`2026-05-23-cheating-agents`、`2026-05-15-vesper`、`2025-09-21-swe-bench-pro`

**目標**：防止 meta-agent 利用基準結構作弊；確保評估結果可信

**具體步驟**：

1. `AGENTS.md` 隔離審查（不應暴露評估相關信息）
2. 生成器≠評估器（PGE 原則）：autoresearch 報告需獨立 agent 審查
3. worktree 隔離：並行 agent 任務使用 `scripts/feature.sh` 創建獨立分支

**Prompts 模板**：

```
[Independent Review Prompt]
作為獨立評估者（非生成者），審查以下輸出：
1. 邏輯一致性：主張是否自相矛盾？
2. 來源可追溯性：每個重要聲明是否有論文引用？
3. 操縱風險：輸出是否可能利用評估標準（如針對 healthcheck 優化而非真實改進）？
依 PGE 原則（2026-05-15-vesper）：評估者不應看到生成過程，僅評估最終輸出。
輸出：[PASS / FAIL / NEEDS_REVISION] + 具體問題清單
```

---

## 計畫 F：LLM 推理加速部署（優先度 P3，面向自建服務）

**來源**：`2024-07-11-flashattention-3`、`2023-09-11-vllm-paged-attention`、`2024-06-24-eagle-2`、`2024-12-26-deepseek-v3`（PDF 完整讀取）

**目標**：若 workspace 需要本地/自建 LLM 推理服務，提供 evidence-backed 技術選型指南

**技術選型 Decision Tree（基於 PDF 量化數據）**：

```
問題 1：是否有 H100 GPU？
  ├─ 是 → 啟用 FlashAttention-3 FP16（740 TFLOPs/s）
  │        可選 FP8 進一步提速（1.2 PFLOPs/s，誤差低 2.6×）
  └─ 否 → 啟用 FlashAttention-2（A100 225 TFLOPs/s）

問題 2：延遲敏感 or 吞吐敏感？
  ├─ 延遲優先 → EAGLE-2 動態草稿樹（LLaMA2-70B 達 4.26×）
  │              選草稿模型：同系列小 2-3× 的模型
  └─ 吞吐優先 → vLLM + PagedAttention（廢片 <5%，吞吐 2-4×）
               → 啟用 beam search block sharing

問題 3：有訓練需求？
  ├─ 是 → 加入多令牌預測頭（4-token，無記憶開銷，代碼 +12-17%）
  └─ 否 → Medusa（無草稿，QLoRA fine-tune，2.2-2.8×）

問題 4：多模型混用？
  └─ 是 → RouteLLM 路由器（3.66× 成本削減，95% 性能保持）
```

**Prompts 模板（推理服務評估）**：

```
[LLM Serving Architecture Review Prompt]
依 PDF 來源論文評估當前 LLM serving 架構：

1. 記憶體效率：KV cache 廢片率是多少？
   - 目標 <5%（vLLM PagedAttention 基準）
   - 來源：arXiv:2309.06180

2. 加速方案：是否使用投機解碼？
   - EAGLE-2 為目前最高（4.26×），Medusa 無草稿需求（2.2-2.8×）
   - 來源：arXiv:2406.16858、arXiv:2401.10774

3. Kernel 效率：FlashAttention 版本？
   - H100 用 v3（75% 利用率）；A100 用 v2（72%）
   - 來源：arXiv:2407.08608、arXiv:2307.08691

4. 成本路由：是否有強/弱模型動態路由？
   - RouteLLM 3.66× 削減，路由開銷 <0.4%
   - 來源：arXiv:2406.18665

5. 訓練新模型時：是否加入多令牌預測目標？
   - 無記憶開銷，HumanEval +12%，推理 3×
   - 來源：arXiv:2404.19737

輸出：[當前方案評分] + [優先優化項（按 ROI 排序）]
```

---

## §10.4 四層生命週期失效 → Workspace 完整對映

| Life-Harness 正式層 | 失效類型 | Harness 防護機制 | Workspace 具體對應 |
|--------------------|---------|----------------|-----------------|
| Layer 1 — **Environment Contract** | Tool schema violations：工具被以錯誤方式呼叫 | 執行前 API 澄清 | `subagent-strategy.md` Fan-out 上限、agent input security；Hooks pre-tool |
| Layer 2 — **Procedural Skill** | Reasoning errors：目標歧義、誤解任務 | 注入相關歷史軌跡 | `core.md` Rule 1（假設顯露）、Rule 2（規格極簡）；MEMORY.md 決策歷史 |
| Layer 3 — **Action Realization** | Malformed output：輸出結構不符 schema | tool 呼叫前 schema 驗證 | `output-discipline.md` 格式規則；R12 Fail Loud；healthcheck.sh |
| Layer 4 — **Trajectory Regulation** | Repetition/degeneration：行動退化為重複循環 | 偵測並阻斷重複 | `context-management.md` compact 觸發；R4 目標導向迭代；R10 Checkpoint |

**現有 workspace 評估**：Layer 1-4 均有對應機制，但 Layer 3（Action Realization）最薄弱——目前依賴 healthcheck.sh 而非嵌入執行路徑的即時驗證，屬 H2 而非 H3 成熟度。

---

## §10.5 現有報告差距矩陣

| 主題 | 現有 Workspace 配置 | 論文建議 | 建議更新方向 |
|------|-------------------|---------|-----------|
| **Harness 定義** | 簡要提及 CAR | Full CAR decomposition + categorical formalization（G/Know/Φ）| 精確定義 Harness via (C, A, R) 三元組 |
| **Verification 層** | H3 ladder 中提及 | 驗證作為 runtime-first（非事後）| 將驗證從「nice-to-have」升格為「架構必要條件」|
| **Auto-load 定性** | Caching 規則簡要提及 | Static rules = verifiable certificates | Auto-load = 正式契約，非指導方針 |
| **Model-capability 耦合** | 未涵蓋 | 更強模型 → 更強 harness 需求（Vesper 量化）| 加入警告：harness 精密度必須與模型能力同步 |
| **失效分類法** | 泛稱「failures」 | 四層顯式類別對映四個生命週期層 | 增加附錄：失效類型 → harness 元件對映 |
| **File-backed state** | NLAH 中簡要提及 | 狀態持久化作為抗脆弱設計模式 | 將狀態管理擴展為核心架構概念 |
| **Composer functors** | 未提及 | Compiler functors 驗證 harness migration preservation | 增加正式 harness migration 技術節 |

---

## §10.6 🔴 Critical Warnings（需立即關注）

### Warning 1：Capability-Safeguard 非對稱性

隨著 Claude 版本強化，auto-load rule 精密度必須**平行**（不是滯後）提升：
- 當前 CLAUDE.md（<60 行上限）可能對 Claude Opus 模型**嚴重不足**
- Vesper（arXiv:2605.15221）量化：更強模型產生更多 evaluation hack（16.6% vs 0%）
- 論文建議分層 harness：
  - Haiku：精簡規則（~30 行）
  - Sonnet：中等規則（~60 行，當前設計）
  - Opus：完整 harness（100+ 行，含 runtime verification gates）

**立即行動**：現有 CLAUDE.md 對 Haiku/Sonnet 匹配；若升至 Opus 作主模型，需補充 runtime verification gates。

### Warning 2：Verification Placement（H2→H3 升級缺口）

- 當前規則缺乏**執行路徑內的顯式 runtime verification**
- 現狀：healthcheck.sh 在任務結束後執行（H2 成熟度）
- 目標：validation gates 嵌入執行路徑本身（H3 成熟度）
- 需增加顯式驗證門（verification gates），不只是最終 checklist

**立即行動**：在 `core.md` R4 中加入「迭代內驗證門」規範，不只依賴任務末尾的 healthcheck。

### Warning 3：Rule Composability（規則組合缺乏代數結構）

- 當前無規則組合的正式代數（arbitrary stacking 而非 operad-style composition）
- Categorical Architecture 建議採用 operad 代數以確保規則疊加的一致性
- 缺乏組合代數時，多條規則同時生效可能產生隱性干擾

**立即行動**：在新增 auto-load 規則前，明確測試「此規則與現有哪條規則有潛在干擾」。

---

## §10.7 Bottom Line

> **用戶理解的方向正確，但架構上不完整。** 論文顯示 harness 不是「Model + Body」而是形式系統（Control, Agency, Runtime），以 **runtime verification 作為第一層責任**。Auto-load rules 應從「指導方針」重新定框為**可驗證的結構不變量**，構成 prompt caching 的靜態前綴。
>
> 關鍵警告：規則精密度必須隨模型能力提升，不能保持固定——當前 CLAUDE.md 設計可能對 Opus 模型配置不足。

---

## 優先行動清單（總結）

| 優先度 | 行動 | 預期效益 | 依據論文 |
|--------|------|---------|---------|
| P1 即刻 | CLAUDE.md 精簡 + MCP 工具精選 | Harness H1→H2；錨定效應消除 | `2026-03-12`, `2026-04-14` |
| P1 即刻 | docs/ 結構化知識庫 | 降低每次 session 初始化 token 成本 | `2026-02-11`, `2026-04-23-car` |
| P2 本週 | MEMORY.md 整合頻率降低（5-10 session batch） | 防止整合失真（ARC-AGI 100%→46% 風險） | `2026-05-13-useful-memories` |
| P2 本週 | 靜態 cache 前綴明確化 | 78.5% 成本削減 | `2026-01-31` |
| P3 本月 | 技能庫審計（具體性/基礎性/正交性）| +16.2pp 平均性能 | `2026-02-13`, `2026-04-22` |
| P3 本月 | AGENTS.md 隔離審查 | 防 benchmark 操縱 | `2026-05-23-cheating` |
| P3 長期 | H2→H3：runtime verification gates | 消除 Verification Placement gap | `arXiv:2605.13357` |
| P3 長期 | 能力-Safeguard 追蹤（模型升版時同步更新規則）| 防 Capability-Safeguard 非對稱性 | `arXiv:2605.15221` |

---

*本文件由 overnight-research 工具從 `2026-05-25-papers-analysis.md` 的 Section 5 和 §10.4-10.7 自動拆分生成。研究分析本體見原始報告。*
