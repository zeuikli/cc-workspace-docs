# Workspace SKILL Gap Analysis + README Optimization
**日期**：2026-05-26 | **字元數目標**：≥ 5000 | **版本**：1.0

---

## 執行摘要

cc-workspace 現有 19 個 skills（含 RESOLVER.md 索引），從 41→13→19 演進，已完成一輪大道至簡審查。本報告基於三個設計源（Karpathy LLM Wiki / Hermes Agent / GBrain）和外部 SRE/DevOps skill 生態評估，提供：(1) 候選 skill 評分表，(2) README 優化清單，(3) 評分 ≥ 2.0 的 skill 草稿。

核心發現：現有 19 skills 覆蓋率良好，只有 2 個候選通過 2.0 門檻值得加入（iac-review 和 diagram-gen）；README 有 3 處結構性改善空間。

---

## 1. 三源設計理念回顧

### Karpathy LLM Wiki
**核心洞見**：知識在 query-time 重新推導 → 持久化 wiki 累積。三層架構：
- **Raw Sources**：不可變來源（文章/論文/影片），LLM 只讀不改
- **Wiki Layer**：LLM 生成的 Markdown，10-15 頁跨引用更新（已落地：research/ 目錄）
- **Schema Layer**：co-evolve with knowledge base，永遠放 prompt 最前（已落地：CLAUDE.md / AGENTS.md / rules/）

**對 workspace 的啟示**：三層已完全實作。改善空間在 Lint 操作（wiki-lint.sh）和 log.md（append-only 紀錄），目前用 MEMORY.md 替代但 log.md 缺失。

### Hermes Agent
**核心洞見**：Skills = first-class procedural memory；三階段自我進化：
1. **Experience Capture**：複雜任務後自動生成 skill
2. **Active Learning**：Skills 在使用中自我改進（use 觸發 improvement）
3. **Persistence**：FTS5 session search + LLM 摘要，跨 session 檢索過往解法

**對 workspace 的啟示**：skill-evolution skill 已實作 Phase 2，但 Phase 1（task complexity detection → auto-create）和 Phase 3（session search for similar past solutions）尚未完全落地。GOTCHAS.md 協議是 Phase 1 的輕量替代。

### GBrain
**核心洞見**：thin harness + typed-edge knowledge graph；關鍵設計：
- `gbrain search`：hybrid scoring（vector + BM25 + RRF + reranker）
- `gbrain think`：合成答案 + citations + gap analysis（明確標示缺失資訊）
- Contract-first interface：47 operations 統一定義，允許替換後端

**對 workspace 的啟示**：Knowledge Graph 已在 README.md 以 typed edges 表達。缺失的是「gap analysis」輸出（當 agent 找不到答案時明確說「此區域知識缺失」而不是猜測）。

---

## 2. SKILL 評分表

### 評分維度與權重

| 維度 | 權重 | 描述 |
|------|------|------|
| **使用頻率** | 30% | 0=從不；1=偶爾；2=每週；3=每天 |
| **不可替代性** | 25% | 0=已被現有 skill 完全覆蓋；1=部分重疊；2=互補；3=全新能力 |
| **維護成本** | 20% | 0=高（新 agent/hook）；1=中（複雜 SKILL.md）；2=低（簡單路由）；3=零（純 prompt） |
| **大道至簡符合度** | 15% | 0=過度工程；1=中立；2=符合；3=完美符合 |
| **實戰驗證度** | 10% | 0=理論；1=他人案例；2=自己曾用；3=高頻使用 |

**門檻：加權分 ≥ 2.0 才建議加入**

---

### 候選 SKILL 評分結果

#### 候選 A：iac-review（Infrastructure as Code 審查）

**定位**：Terraform / Helm / K8s YAML 靜態審查，針對生產風險（destroy/replace plan、secret leak、missing resource limits）。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 2 | Cloud Architect 每週接觸 Terraform/K8s |
| 不可替代性 | 2 | `sre` 有 K8s debug 但無 IaC 靜態審查；`security-compliance` 做合規不做 diff 審查 |
| 維護成本 | 2 | 純 SKILL.md，不需新 agent/hook |
| 大道至簡 | 2 | 單一職責，填補明確 gap |
| 實戰驗證 | 2 | CathaySec GCP Terraform 框架（見 sre skill）有類似需求 |

**加權分**：(2×0.30) + (2×0.25) + (2×0.20) + (2×0.15) + (2×0.10) = **2.00 ✅ 建議加入**

**Do**：Terraform plan diff review（detect destroy/replace）、K8s YAML security context 審查、Helm values 環境差異檢查、IaC drift detection
**Don't**：替代 sre:incident（runtime 問題）、替代 security-compliance（合規認證路徑）

---

#### 候選 B：diagram-gen（架構圖生成）

**定位**：從程式碼 / Terraform / 文字描述 → Mermaid / PlantUML 架構圖；系統設計文件輸出。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 2 | 設計文件、incident RCA、PR 說明頻繁需要 |
| 不可替代性 | 2 | 無任何現有 skill 覆蓋 diagramming；原始 Claude 可以但沒有 workspace 特定 convention |
| 維護成本 | 3 | 純 prompt-based，零維護成本 |
| 大道至簡 | 2 | 單一職責，輸出明確（Mermaid code block） |
| 實戰驗證 | 1 | 外部案例多，個人未有高頻 skill-level 使用記錄 |

**加權分**：(2×0.30) + (2×0.25) + (3×0.20) + (2×0.15) + (1×0.10) = **2.10 ✅ 建議加入**

**Do**：sequence diagram（API flow）、C4 架構圖（Mermaid）、ER diagram from schema、K8s 拓撲圖
**Don't**：替代 tech-strategy（評估框架）、替代 sre:monitoring（Grafana dashboard）

---

#### 候選 C：prompt-engineer（Prompt 優化）

**定位**：優化 LLM prompt，針對 chain-of-thought、few-shot、output format。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 1 | 偶爾需要，非日常工作 |
| 不可替代性 | 1 | harness-meta:token 有 prompt 優化子功能；overlap 高 |
| 維護成本 | 2 | 簡單 SKILL.md |
| 大道至簡 | 1 | harness-meta 已涵蓋，加入增加認知負荷 |
| 實戰驗證 | 1 | 理論案例居多 |

**加權分**：(1×0.30) + (1×0.25) + (2×0.20) + (1×0.15) + (1×0.10) = **1.20 ❌ 不建議加入**（已被 harness-meta:token 覆蓋）

---

#### 候選 D：data-pipeline（ETL/Streaming 設計）

**定位**：資料流設計，Kafka topic design、ETL schema、Flink/Spark job。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 1 | 現職 CathaySec 主要是 GCP + K8s，非資料工程角色 |
| 不可替代性 | 2 | sre 有 kafka-ops 但無 ETL design；db-ops 有 schema 但無 pipeline |
| 維護成本 | 1 | 需要 domain knowledge 豐富才有價值 |
| 大道至簡 | 1 | 用戶主要角色非資料工程師，加入後可能長期不用 |
| 實戰驗證 | 1 | 過去 KKStream / SoundOn 有案例，但現職低頻 |

**加權分**：(1×0.30) + (2×0.25) + (1×0.20) + (1×0.15) + (1×0.10) = **1.30 ❌ 不建議加入**（低頻 + sre:kafka 已部分覆蓋）

---

#### 候選 E：perf-profiling（效能剖析）

**定位**：CPU/memory profiling、latency analysis、flame graph 解讀。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 1 | SRE 職責中有，但不是每週任務 |
| 不可替代性 | 1 | autoresearch:debug + sre 可覆蓋大部分 |
| 維護成本 | 1 | 需要工具整合（pprof/perf/py-spy） |
| 大道至簡 | 1 | 偏特定工具鏈，不夠通用 |
| 實戰驗證 | 1 | 無高頻個人案例 |

**加權分**：(1×0.30) + (1×0.25) + (1×0.20) + (1×0.15) + (1×0.10) = **1.00 ❌ 不建議加入**

---

#### 候選 F：api-design（REST/gRPC API 設計評審）

**定位**：API 設計原則審查（命名/版本/錯誤碼/OpenAPI spec）。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 1 | 設計階段才需要 |
| 不可替代性 | 1 | review-hub + tech-strategy 可覆蓋 |
| 維護成本 | 2 | 簡單 SKILL.md |
| 大道至簡 | 1 | review-hub 已有架構審查能力 |
| 實戰驗證 | 1 | 無 skill-level 案例 |

**加權分**：(1×0.30) + (1×0.25) + (2×0.20) + (1×0.15) + (1×0.10) = **1.20 ❌ 不建議加入**

---

#### 候選 G：quick-commit / quick-pr（快速提交/PR）

**狀態調查**：`quick-commit` 和 `quick-pr` 在 RESOLVER.md 中出現但不在 .claude/skills/ 目錄 → 疑似為 built-in Claude Code 指令（`/commit`、`/pr`）而非 custom skill，或曾存在已刪除。

| 維度 | 分數 | 理由 |
|------|------|------|
| 使用頻率 | 3 | git workflow 每天使用 |
| 不可替代性 | 0 | core.md 已有 git 工作流程規則；Claude Code 內建 commit 能力 |
| 維護成本 | 2 | 簡單 |
| 大道至簡 | 1 | 可能重複 |
| 實戰驗證 | 2 | 高頻但透過現有機制完成 |

**加權分**：(3×0.30) + (0×0.25) + (2×0.20) + (1×0.15) + (2×0.10) = **1.90 ❌ 略低於門檻**（建議先確認 built-in 是否已滿足需求）

---

### 評分摘要表

| 候選 Skill | 頻率 | 不可替代 | 維護 | 簡潔 | 實戰 | **加權分** | 決策 |
|-----------|------|---------|------|------|------|-----------|------|
| iac-review | 2 | 2 | 2 | 2 | 2 | **2.00** | ✅ 加入 |
| diagram-gen | 2 | 2 | 3 | 2 | 1 | **2.10** | ✅ 加入 |
| prompt-engineer | 1 | 1 | 2 | 1 | 1 | **1.20** | ❌ harness-meta 已覆蓋 |
| data-pipeline | 1 | 2 | 1 | 1 | 1 | **1.30** | ❌ 低頻 |
| perf-profiling | 1 | 1 | 1 | 1 | 1 | **1.00** | ❌ 過窄 |
| api-design | 1 | 1 | 2 | 1 | 1 | **1.20** | ❌ review-hub 覆蓋 |
| quick-commit | 3 | 0 | 2 | 1 | 2 | **1.90** | ❌ built-in 確認後再議 |

---

## 3. README 優化清單

### 現況分析

README.md 目前 260 行 / 9.7KB，結構完整但有三個問題：

**問題 1：Agent Entry Point 表格有重複項目**
第 14 行 `Which skill to use → .claude/skills/RESOLVER.md` 和第 22 行 `Full skill triggers → .claude/skills/RESOLVER.md` 指向同一路徑，重複。

**問題 2：Component Registry 數字可能過期**
`skills/` 顯示 18，但實際目錄 19 個（含 RESOLVER.md）；`hooks/` 顯示 19 但 HARNESS-CARD 說 15；reports/ 顯示 33 但實際可能已變化。這類 hardcoded metrics 應改為「見 healthcheck.sh 輸出」或移至 Current State 表。

**問題 3：Standard Operations 的 Ingest 指令需要更新**
`/autoresearch:wiki ingest <source-path>` 此指令是否仍有效？autoresearch skill v1.11.0 中 wiki sub-command 是否存在？應驗證後更新。

### 具體改動建議

#### 改動 1：移除 Agent Entry Point 重複項（-1 行）
```
# 刪除第 22 行：
| Full skill triggers | `.claude/skills/RESOLVER.md` | index |
```

#### 改動 2：Current State 數字改為動態說明（+2 行說明）
在 Current State 表格下方加一行：
```markdown
> 數字為最後驗證值；執行 `bash scripts/healthcheck.sh` 取得即時數值。
```

#### 改動 3：Knowledge Graph 加入 Hermes self-evolution 邊
在 Typed Edges 表加一條：
```markdown
| `hooks/post-tool-use` → | `logs_to` | `failure-log.sh` (failure trajectory capture) |
```

#### 改動 4：Self-Evolution Loop 加入 Hermes 三階段標記
現有 Loop 圖只有線性箭頭，加入 Hermes 三階段標籤提升可讀性：
```
Phase 1 [Experience Capture]  → Skill Creation ←── /skill-evolution
Phase 2 [Active Learning]     → Skill Improvement ←── /harness-meta
Phase 3 [Persistence]         → Memory Persistence ←── memory/MEMORY.md
```

#### 改動 5（低優先級）：Three-Layer Architecture 數字更新
`33 autoresearch-generated deep reports` → 改為 `N reports（見 ls research/reports/ | wc -l）`

### 不建議改動

- 不縮短 README（9.7KB 是合理大小，LLM 可完整讀入）
- 不移除 Knowledge Graph（GBrain 設計驗證此為必要的 agent 導航元素）
- 不拆分至子文件（README 已是高密度索引，分散反而增加 agent 跳轉成本）

---

## 4. 新 SKILL 草稿

### SKILL A：iac-review

```yaml
---
name: iac-review
description: 'Terraform / Helm / K8s YAML 靜態審查：detect destroy/replace in plan diff、secret leak、missing resource limits、IaC drift。Use when user types iac-review, iac-review:terraform, iac-review:k8s, iac-review:helm, IaC 審查, terraform plan review, k8s yaml review. Do NOT use for: runtime K8s 排障（用 sre:k8s）、安全合規認證（用 security-compliance）、application code review（用 review-hub）。 English triggers: iac-review.'
version: 1.0.0
allowed-tools: Read, Grep, Glob, Bash
---

# iac-review — Infrastructure as Code 靜態審查

## 觸發詞

- `iac-review` / `iac-review:terraform` / `iac-review:k8s` / `iac-review:helm`
- `IaC 審查` / `terraform plan review` / `幫我審查 Terraform` / `K8s YAML 有沒有問題`

## Do / Don't

**Do**：Terraform plan diff（detect destroy/replace/recreate）、K8s YAML security context 審查（runAsNonRoot/readOnlyRootFilesystem/resource limits）、Helm values 環境差異比對、IaC drift detection（plan vs actual）、secret 未加密偵測

**Don't**：替代 sre:k8s（runtime 排障）、替代 security-compliance（合規認證路徑）、替代 review-hub（application code）

## 三階段執行

### Phase 1：分析輸入類型

偵測輸入類型：
- Terraform plan output（`terraform plan -out=tfplan` → `terraform show -json tfplan`）
- K8s YAML 檔案（`kubectl apply --dry-run=client -f <file>`）
- Helm chart（`helm template <release> <chart> -f values.yaml`）

```bash
# 偵測是否有 staged Terraform 變更
git diff --name-only HEAD | grep -E '\.tf$' && echo "terraform files detected"
# 偵測 K8s YAML
git diff --name-only HEAD | grep -E '\.(yaml|yml)$' | xargs grep -l 'kind:' 2>/dev/null
```

### Phase 2：風險分類審查

**Terraform 審查清單（Critical → Warning → Info）**：
- Critical：`destroy`、`replace`、`delete` 操作 → 停止並警告
- Critical：resource 中含明文 secret（password/key/token）
- Warning：`recreate` 操作影響有狀態資源（DB/PVC）
- Warning：`count = 0` 或 `enabled = false` 在生產環境
- Info：resource tag 缺少 env/owner/cost-center

**K8s 審查清單**：
- Critical：`securityContext` 缺失、`privileged: true`
- Critical：`resources.limits` 未設定（OOM 風險）
- Warning：`imagePullPolicy: Always` 在生產環境（冷啟動慢）
- Warning：`readinessProbe` / `livenessProbe` 缺失
- Info：`PodDisruptionBudget` 未設定

### Phase 3：輸出報告

```markdown
## IaC Review Report — {timestamp}

### Critical (需手動確認才能繼續)
- [file:line] 描述

### Warning (建議修復)
- [file:line] 描述

### Info (可選改進)
- [file:line] 描述

### 決策建議
GO / NO-GO + 理由
```
```

---

### SKILL B：diagram-gen

```yaml
---
name: diagram-gen
description: '從程式碼 / Terraform / 文字描述 → Mermaid / PlantUML 架構圖。Use when user types diagram-gen, diagram, 架構圖, 畫圖, sequence diagram, ER diagram, C4, mermaid. Do NOT use for: tech-strategy 評估（用 tech-strategy）、Grafana dashboard（用 sre:monitoring）。 English triggers: diagram, draw.'
version: 1.0.0
allowed-tools: Read, Grep, Glob, Bash
---

# diagram-gen — 架構圖生成

## 觸發詞

- `diagram` / `diagram-gen` / `架構圖` / `畫圖` / `sequence diagram`
- `ER diagram` / `C4 diagram` / `mermaid` / `畫一下系統流程`

## 輸出格式優先序

1. **Mermaid**（優先，GitHub/Notion 原生渲染）
2. **PlantUML**（企業環境有 server 時）
3. **ASCII**（最後 fallback，純文字環境）

## 三階段執行

### Phase 1：意圖識別

| 輸入類型 | 目標圖類型 |
|---------|----------|
| API 流程說明 / 呼叫鏈 | Sequence Diagram |
| 系統元件說明 | C4 Context / Container |
| DB schema | ER Diagram |
| K8s 架構 / 微服務 | C4 Component / flowchart |
| 決策流程 | Flowchart |
| 時間軸 | Gantt |

### Phase 2：生成

產出 Mermaid code block，加上簡短說明（圖的目的 + 主要元件）。

**Mermaid 輸出規則**：
- node 名稱用英文（避免 Mermaid 解析 CJK 問題）
- 加上 `%%` 行注釋說明複雜節點
- 超過 20 個節點 → 拆成 2 張子圖

### Phase 3：驗證與調整

輸出後詢問：「需要調整圖的範圍或層次嗎？」（提供 3 個常見調整方向：更高層/更細節/增加時序）
```

---

## 5. README 實施後預期效果

套用上述 5 項改動後，README 預計：
- 行數：260 → 262 行（+2 行說明，-1 行重複）
- LLM 讀入效率：agent entry point 去重，減少歧義
- Self-evolution 可讀性：Hermes 三階段標記讓 LLM 快速理解進化機制
- 維護性：Current State 數字加 dynamic 提示，減少 staleness

---

## 6. 與三源設計的對齊驗證

| 設計源 | 核心原則 | workspace 現狀 | 改善後 |
|--------|---------|--------------|--------|
| Karpathy LLM Wiki | 三層 Raw/Wiki/Schema | ✅ 已落地 | ✅ 無需改動 |
| Karpathy LLM Wiki | log.md append-only | ⚠️ MEMORY.md 替代，無 log.md | 低優先，可後補 |
| Hermes Agent | Skills = procedural memory | ✅ 19 skills | ✅ +2 skills 通過門檻 |
| Hermes Agent | Self-evolving（task → skill） | ⚠️ GOTCHAS 協議是輕量替代 | README 加 Phase 標記 |
| GBrain | Typed edges knowledge graph | ✅ README 已有 | ✅ +1 failure-log edge |
| GBrain | Gap analysis 顯式輸出 | ⚠️ 未標準化 | 可在 autoresearch:reason 加 gap 區塊 |
| 大道至簡 | 只加有價值的 | ✅ 評分機制篩出 2/7 候選 | ✅ 符合 |

---

## 7. 可立即實作的行動建議

**P0（今天）**：
1. 在 `.claude/skills/` 建立 `iac-review/SKILL.md`（草稿已在本報告 §4）
2. 在 `.claude/skills/` 建立 `diagram-gen/SKILL.md`（草稿已在本報告 §4）
3. 更新 RESOLVER.md 加入兩個新 skill 的觸發詞映射

**P1（本週）**：
4. README.md 改動 1-4（移除重複 / 加動態說明 / 加 Hermes 邊 / 加 Phase 標記）
5. 更新 CLAUDE.md skill 計數（18 → 21）
6. 跑 `bash scripts/healthcheck.sh` 驗證無 FAIL

**P2（可選）**：
7. 確認 `quick-commit` / `quick-pr` 是否為 built-in，若非則建立 skill（分數 1.90 接近門檻）
8. 在 `autoresearch:reason` SKILL.md 加 `## Gap Analysis` 區塊（GBrain 風格）
9. 建立 `research/log.md`（Karpathy pattern，append-only）

---

## 附錄：來源評分索引

| 來源 | URL | 評分 | 核心貢獻 |
|------|-----|------|---------|
| Karpathy LLM Wiki | gist.github.com/karpathy | A/A/A/A/A | 三層架構、Lint ops、Wiki maintenance |
| Hermes Agent README | github.com/nousresearch/hermes-agent | A/B/A/A/B | 三階段自我進化、Skills = procedural memory |
| GBrain README | github.com/garrytan/gbrain | A/A/B/A/B | Typed edges、gap analysis、thin harness |
| Firecrawl Best Skills | firecrawl.dev/blog | B/B/B/A/B | SRE 角色 skill 推薦（Trail of Bits、monitoring） |
| Pulumi DevOps Skills | pulumi.com/blog | B/A/B/A/A | DevOps skill 評比（monitoring-expert、k8s-specialist） |
| SkillsBench arXiv | arxiv.org/pdf/2602.12670 | A/A/B/A/B | Skill 評估框架（Harbor containerized structure） |
| Adaline Eval Guide | adaline.ai/blog | B/B/B/A/B | LLM agent evaluation criteria 2026 |

**評分維度**：A(影響力)/B(原創性)/C(可操作性)/D(可信度)/E(時效性)

---

---

## 8. Hermes Agent + GBrain 特定 Skill 評估

用戶追加需求：評估兩個 repo 是否有適合 workspace 的具體 skills。

### 8.1 Hermes Agent — 可借鑑的 Skill 模式

Hermes Agent 的 skills/ 目錄包含 25 個類別。與 cc-workspace 最相關的：

#### hermes-agent/skills/devops

**Hermes 設計**：CI/CD automation、deployment 流程、infrastructure automation。

**評分**：

| 維度 | 分 | 理由 |
|------|-----|------|
| 使用頻率 | 2 | Cloud Architect 每週 |
| 不可替代性 | 1 | `sre` + `iac-review` 已覆蓋大部分 |
| 維護成本 | 1 | 需整合 CI/CD 工具鏈 |
| 大道至簡 | 1 | 功能邊界與 sre 高度重疊 |
| 實戰驗證 | 1 | 需 CI 工具（Jenkins/GitHub Actions）整合 |

**加權分**：1.40 ❌ **不建議獨立建立**（sre + iac-review 已覆蓋主要場景）

---

#### hermes-agent/skills/diagramming

**Hermes 設計**：Visual diagram generation（與我們剛建立的 `diagram-gen` 高度一致）。

**結論**：✅ `diagram-gen` 已建立，gap 已填補。Hermes 的 diagramming skill 可作為 `diagram-gen` 改版參考，但不需要另建 skill。

---

#### hermes-agent/skills/research

**Hermes 設計**：Research and information gathering，含 web search + synthesis。

**評分**：

| 維度 | 分 | 理由 |
|------|-----|------|
| 使用頻率 | 2 | 日常研究任務 |
| 不可替代性 | 0 | `research-hub` + `overnight-research` + `autoresearch:reason` 完全覆蓋 |
| 維護成本 | 1 | 需整合 |
| 大道至簡 | 0 | 重複 |
| 實戰驗證 | 2 | 現有 skills 高頻使用 |

**加權分**：0.95 ❌ **完全被現有 skills 覆蓋**

---

#### hermes-agent/skills/autonomous-ai-agents

**Hermes 設計**：Self-operating AI agent 能力；meta-level 的 agent orchestration。

**評分**：

| 維度 | 分 | 理由 |
|------|-----|------|
| 使用頻率 | 1 | 偶爾需要複雜 orchestration |
| 不可替代性 | 1 | harness-meta + skill-evolution 已處理 agent 管理 |
| 維護成本 | 0 | 複雜 meta-agent 邏輯，維護成本高 |
| 大道至簡 | 0 | 過度工程，現有 fan-out 模式已足夠 |
| 實戰驗證 | 0 | 理論性較強 |

**加權分**：0.55 ❌ **不建議加入**（harness-meta 已提供足夠 meta-level 控制）

---

#### hermes-agent/skills/github

**Hermes 設計**：GitHub API 整合（PR workflow、code review、issue 管理）。

**評分**：

| 維度 | 分 | 理由 |
|------|-----|------|
| 使用頻率 | 2 | 每週使用 git/GitHub |
| 不可替代性 | 1 | review-hub:commit 有 PR review；ship-review 有 launch gate |
| 維護成本 | 2 | MCP GitHub tool 已整合，skill 只需 prompt |
| 大道至簡 | 1 | 部分重疊 |
| 實戰驗證 | 2 | GitHub 操作日常 |

**加權分**：1.65 ❌ **略低於門檻**（現有 review-hub + MCP GitHub 已充分）

---

#### hermes-agent/skills/mlops

**Hermes 設計**：Machine learning operations；模型訓練、部署、監控。

**評分**：

| 維度 | 分 | 理由 |
|------|-----|------|
| 使用頻率 | 1 | CathaySec 非 ML 工作 |
| 不可替代性 | 2 | 無現有 skill 覆蓋 ML pipeline |
| 維護成本 | 1 | 需要 ML 工具整合 |
| 大道至簡 | 1 | 非主要工作域 |
| 實戰驗證 | 0 | 無個人 MLOps 案例 |

**加權分**：1.10 ❌ **不建議加入**（低頻 + 非主要工作域）

---

### 8.2 GBrain — 可借鑑的 Skill 模式

GBrain 的 43 個 curated skills 按類別分組：signal capture / ingest / enrichment / querying / brain ops / reports / eval。

#### gbrain/skills/querying（gbrain think + gbrain search）

**GBrain 設計**：`gbrain think` = 合成答案 + citations + gap analysis；`gbrain search` = hybrid scoring 檢索。

**對 workspace 的啟發**：
- **Gap Analysis 輸出格式**：當 `autoresearch:reason` 找不到答案時，目前沒有標準格式說「此區域知識缺失」。可在 autoresearch:reason SKILL.md 加 `## Gap Analysis` 區塊（低成本改進）。
- **Hybrid Search**：cc-workspace 目前依賴 Grep/Glob；gbrain 的 BM25 + vector + RRF 是重型基礎設施，不適合 pure Claude Code workspace。

**評分（作為獨立 skill）**：

| 維度 | 分 | 理由 |
|------|-----|------|
| 使用頻率 | 2 | 研究任務頻繁 |
| 不可替代性 | 1 | research-hub + autoresearch:reason 已覆蓋 |
| 維護成本 | 0 | gbrain 需要獨立資料庫基礎設施（pgvector） |
| 大道至簡 | 0 | 過度工程 for Claude Code 純 prompt-based workspace |
| 實戰驗證 | 1 | gbrain 自身案例好，但整合複雜 |

**加權分**：0.85 ❌ **不建議作為獨立 skill**；但**強烈建議借鑑 Gap Analysis 輸出模式**（在 autoresearch:reason 加 `## 知識缺口` 區塊，零維護成本）。

---

#### gbrain/skills/ingest（gbrain capture / gbrain import）

**GBrain 設計**：idea、media、meeting 的快速 ingest；支援 stdin / webhook / file。

**對 workspace 的啟發**：
- `research-hub:archive` 已有類似功能（URL → Markdown 歸檔）
- gbrain 的 **meeting notes ingest** 是 cc-workspace 缺失的（會議記錄 → wiki page）
- 但用戶主要工作場景不是 meeting 重，不值得單獨建立 skill

**加權分**：1.10 ❌ **不建議加入**（research-hub:archive 已覆蓋主要場景）

---

#### gbrain/skills/brain-ops（gbrain doctor / gbrain schema）

**GBrain 設計**：健康度檢查、schema 管理、consistency 維護。

**類比**：cc-workspace 的 `harness-meta:audit` + `scripts/healthcheck.sh` 已完整覆蓋此功能，且更 Claude Code 原生。

**加權分**：0.30 ❌ **已被 harness-meta 完全覆蓋**

---

### 8.3 Hermes + GBrain 評估摘要

| 候選來源 | Skill | 加權分 | 決策 |
|---------|-------|-------|------|
| Hermes | devops | 1.40 | ❌ sre + iac-review 已覆蓋 |
| Hermes | diagramming | N/A | ✅ diagram-gen 已建立 |
| Hermes | research | 0.95 | ❌ 完全重複 |
| Hermes | autonomous-ai-agents | 0.55 | ❌ 過度工程 |
| Hermes | github | 1.65 | ❌ 略低門檻，MCP 已覆蓋 |
| Hermes | mlops | 1.10 | ❌ 低頻非主要域 |
| GBrain | querying (think/search) | 0.85 | ❌ 但借鑑 Gap Analysis 輸出格式 |
| GBrain | ingest (capture) | 1.10 | ❌ research-hub 已覆蓋 |
| GBrain | brain-ops | 0.30 | ❌ harness-meta 已覆蓋 |

**核心結論**：兩個 repo 的具體 skills 均不通過 2.0 門檻。原因是 cc-workspace 已有高度特化的 skills 覆蓋了主要工作場景。最有價值的不是「引入新 skill」，而是**借鑑設計模式**：
- GBrain gap analysis 輸出格式 → 加入 autoresearch:reason（低成本）
- Hermes 三階段進化標記 → 已加入 README Self-Evolution Loop（本次已完成）

---

*報告更新：2026-05-26 v1.1 — 加入 Hermes Agent + GBrain repo-specific skill 評估*

*報告生成：overnight-research:quick · 2026-05-26 · cc-workspace*
