# reports/INDEX.md

> **Type:** wiki:generated — autoresearch / overnight-research 輸出
> **Updated**: 2026-06-07（整併歸檔：39 份前置研究/已落地計劃書 → `archive/`；active 47 份）
> **Query pattern**: BRAIN.md → 本表（Topic 欄位）→ 具體報告
> **歸檔慣例**：已被母報告整合的前置研究 + 已執行落地的計劃書 → `archive/`（內容不變、可逆；見文末 Archive 列）

---

## ⭐ Canonical 整併報告（先讀這份）

| 檔案 | 說明 |
|------|------|
| [consolidated-agent-engineering-research](2026-05-31-consolidated-agent-engineering-research.md) | **通用整併報告（41K 字）** — 整併早期 Harness / 生態 / 記憶研究，去除內部代號（前置研究見 archive/） |
| [autoload-token-best-practices-consensus](2026-06-05-autoload-token-best-practices-consensus.md) | **Auto-load token SSoT** — gap-vote 三技能共識，五源導覽入口（源報告見 archive/） |
| [12-rule-deepened-research](2026-06-05-12-rule-deepened-research.md) | **12 條準則論文接地深化**（信度分級；母報告，早期接地見 archive/） |

---

## Topic 索引（快速定位）

| Topic | 代表報告 |
|-------|---------|
| [Harness Engineering](#harness-engineering) | consolidated-agent-engineering · harness-engineering-deep-research |
| [LLM Memory](#llm-memory) | llm-memory-control-comprehensive-survey |
| [Context Window / Caching](#context-window--caching) | context-window-management-deep-research · prompt-caching-management-engineering |
| [Auto-load / Token](#auto-load--token) | consensus · autoload-token-optimization · cjk-token-tax |
| [12-Rule / Best Practices](#12-rule--best-practices) | deepened-research · deepened-ruleset · universal-ruleset |
| [Sub-Agent / Agent Team](#sub-agent--agent-team) | research-fleet-research · merge-pipeline-research |
| [Skill / Workspace Canon](#skill--workspace-canon) | skill-evolution-report · zeuik-workspace-canon |
| [前沿 AI 領域研究（6/07）](#前沿-ai-領域研究-607) | 6 領域：alignment / red-teaming / diffusion / interp / VLM / TTC |
| [Claude Code 社群實踐](#claude-code-社群實踐) | community-practices · deep-practices-v2 + 計劃書 |
| [Session Insights](#session-insights) | symmetric-skepticism · multi-domain · dynamic-workflow |

---

## Harness Engineering

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-05 | [harness-memory-self-evolution-synthesis](2026-06-05-harness-memory-self-evolution-synthesis.md) | Harness 自演化合成（活文件，18 篇論文 + 一手洞察）|
| 2026-05-31 | [consolidated-agent-engineering-research](2026-05-31-consolidated-agent-engineering-research.md) | **Agent 工程研究合成母報告** |
| 2026-05-31 | [harness-engineering-deep-research](2026-05-31-harness-engineering-deep-research.md) | Harness 工程深度研究（27 篇論文；D2 交叉驗證）|
| 2026-05-28 | [harness-evolution-plan](2026-05-28-harness-evolution-plan.md) | Harness 演化計劃（大型設計記錄）|

---

## LLM Memory

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-05-22 | [llm-memory-control-comprehensive-survey](2026-05-22-llm-memory-control-comprehensive-survey.md) | LLM 記憶控制全調查（最大單份，不可替代）|

---

## Context Window / Caching

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-03 | [context-window-management-deep-research](2026-06-03-context-window-management-deep-research.md) | 四維度（attention/KV · 工程 · 競品 · 落地）；11 篇論文 |
| 2026-06-03 | [prompt-caching-management-engineering](2026-06-03-prompt-caching-management-engineering.md) | 三主題整合（cross-provider 成本 / registry+injection / non-GPT 驗證）|
| 2026-06-03 | [claude-code-cold-start-latency-deep-research](2026-06-03-claude-code-cold-start-latency-deep-research.md) | 冷啟動 wall-clock latency（hook spawn ms / cache 冷暖）|

---

## Auto-load / Token

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-06 | [cjk-token-tax-research](2026-06-06-cjk-token-tax-research.md) | **CJK token 稅母報告** — 繁中倍率看維度；Claude ~1.71× |
| 2026-06-06 | [autoload-token-optimization](2026-06-06-autoload-token-optimization.md) | **4 機制 ROI** — 結構槓桿 > 符號壓縮 > caching > caveman |
| 2026-06-06 | [classical-chinese-token-eval](2026-06-06-classical-chinese-token-eval.md) | 文言文評估（反貴 17%；現行規則已最精練）|
| 2026-06-05 | [autoload-token-best-practices-consensus](2026-06-05-autoload-token-best-practices-consensus.md) | **SSoT 導覽**（五源共識；源報告見 archive/）|
| 2026-06-04 | [token-guardian-execution-plan](2026-06-04-token-guardian-execution-plan.md) | Token 守衛計劃書（APPLY 待 gated）|
| 2026-06-04 | [r1r12-token-efficiency-execution-plan](2026-06-04-r1r12-token-efficiency-execution-plan.md) | R1–R12 token 效率計劃書（APPLY 待 gated）|

---

## 12-Rule / Best Practices

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-05 | [12-rule-deepened-research](2026-06-05-12-rule-deepened-research.md) | **12 條準則論文接地深化母報告**（信度分級）|
| 2026-06-05 | [12-rule-deepened-ruleset](2026-06-05-12-rule-deepened-ruleset.md) | 可部署深化準則全文（子條延伸）|
| 2026-06-04 | [12-rule-universal-ruleset](2026-06-04-12-rule-universal-ruleset.md) | stack/harness-agnostic 版本 |
| 2026-06-04 | [karpathy-mnilax-12-rule-universalization-research](2026-06-04-karpathy-mnilax-12-rule-universalization-research.md) | 通用化研究（8 篇論文接地 + MAST 完整性）|
| 2026-06-04 | [12-rule-canon-patch-proposal](2026-06-04-12-rule-canon-patch-proposal.md) | canon 修補提案（P1+P2 APPLY 待核准）|

---

## Sub-Agent / Agent Team

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-04 | [research-fleet-research](2026-06-04-research-fleet-research.md) | 平行研究艦隊（scratch-file + reducer + citation 重驗）|
| 2026-06-04 | [research-fleet-execution-plan](2026-06-04-research-fleet-execution-plan.md) | 研究艦隊計劃書（改進 overnight-research，APPLY 待 gated）|
| 2026-06-04 | [merge-pipeline-research](2026-06-04-merge-pipeline-research.md) | 自我驗證 merge pipeline（4 道 gate + removed-content manifest）|
| 2026-06-04 | [merge-pipeline-execution-plan](2026-06-04-merge-pipeline-execution-plan.md) | verified-merge SKILL 計劃書（APPLY 待 gated）|

---

## Skill / Workspace Canon

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-07 | [skill-consolidation-spec](2026-06-07-skill-consolidation-spec.md) | 27 SKILL 同質性矩陣 + 整併評估（Mnilax 三層成本接地；ship-review 維持獨立）|
| 2026-06-06 | [the-loop-canonicalization-and-audit-insights](2026-06-06-the-loop-canonicalization-and-audit-insights.md) | §Rn 退役 + 全 workspace 稽核方法論 |
| 2026-06-06 | [zeuik-workspace-canon](2026-06-06-zeuik-workspace-canon.md) | The Loop 準則重構（六階段語意 header）|
| 2026-06-06 | [coldstart-execution-efficiency-audit](2026-06-06-coldstart-execution-efficiency-audit.md) | 冷啟動執行效率評估（時間/空間雙維度）|
| 2026-06-05 | [skill-evolution-report](2026-06-05-skill-evolution-report.md) | Skill 演化報告（27 skills 對齊工作日誌）|
| 2026-06-05 | [claudemd-best-practices](2026-06-05-claudemd-best-practices.md) | CLAUDE.md 最佳實踐（443 repo 實證）|
| 2026-06-05 | [d4-per-rule-verifier-poc](2026-06-05-d4-per-rule-verifier-poc.md) | D4 Hybrid verifier PoC |
| 2026-06-05 | [next-steps-execution-plan](2026-06-05-next-steps-execution-plan.md) | 下一步計劃書（APPLY/DEFER 帳本）|
| 2026-05-31 | [claude-dir-inventory](2026-05-31-claude-dir-inventory.md) | .claude/ 目錄盤點 |

---

## 前沿 AI 領域研究（6/07）

> PR #490 六大全新領域，各 17–21K 字 + 全文論文，無前置報告。

| 報告 | 領域 |
|------|------|
| [ai-alignment-constitutional-ai](2026-06-07-ai-alignment-constitutional-ai.md) | AI Alignment / CAI |
| [ai-safety-red-teaming](2026-06-07-ai-safety-red-teaming.md) | AI Safety Red-Teaming |
| [diffusion-language-models](2026-06-07-diffusion-language-models.md) | Diffusion LM |
| [mechanistic-interpretability](2026-06-07-mechanistic-interpretability.md) | Mechanistic Interpretability |
| [multimodal-vision-language-models](2026-06-07-multimodal-vision-language-models.md) | Multimodal VLM |
| [test-time-compute-scaling](2026-06-07-test-time-compute-scaling.md) | Test-Time Compute Scaling |

---

## Claude Code 社群實踐

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-07 | [claude-code-community-practices-report](2026-06-07-claude-code-community-practices-report.md) | 11 主題群基礎研究（32 篇來源）|
| 2026-06-07 | [claude-code-deep-practices-v2](2026-06-07-claude-code-deep-practices-v2.md) | 盲點補足版（企業/失敗/縱向演化 + CVE）|
| 2026-06-07 | [claude-code-practices-improvement-execution-plan](2026-06-07-claude-code-practices-improvement-execution-plan.md) | 社群實踐改善計劃書（部分執行，仍有 pending）|
| 2026-06-07 | [deep-practices-v2-execution-plan](2026-06-07-deep-practices-v2-execution-plan.md) | 六主題排程（對稱懷疑剔除幻覺 key + tradeoff）|

---

## Session Insights

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-07 | [session-insights-symmetric-skepticism](2026-06-07-session-insights-symmetric-skepticism.md) | **對稱懷疑原則**（幻覺 key + 撞設計建議雙檢；詮釋層親驗）|
| 2026-06-07 | [session-insights-multi-domain-ai-research](2026-06-07-session-insights-multi-domain-ai-research.md) | 六領域 meta-reflection |
| 2026-06-07 | [session-insights-v2](2026-06-07-session-insights-v2.md) | 盲點補足研究 meta-reflection |
| 2026-06-05 | [session-insight-dynamic-workflow-dual-ruleset](2026-06-05-session-insight-dynamic-workflow-dual-ruleset.md) | 雙版規則集實戰復盤 |

---

## Archive（已歸檔 — 內容不變、可逆）

> 39 份：① 已被上方母報告整合的前置研究 ② 已執行落地的計劃書/執行報告。需追溯時讀 `archive/`，日常查詢用上方 active 母報告。

### 已整合進 consolidated-agent-engineering-research（19 份前置）
早期 Harness（harness-engineering / -model-fit / -verification-methods / ORCHESTRATION）· 早期 Claude Code 最佳實踐 · 生態趨勢（tweets / ai-news / best-practices-simplicity / gstack / autodream-kairos / garry-tan / hermes / gbrain-update / workspace-recommendations / skill-gap-analysis）· 記憶（llm-memory-deep-research / papers-analysis）· subagent（delegation-gotchas / agent-team-deep-research）

### 已被 autoload-token-best-practices-consensus 納為源（7 份）
auto-load-token-best-practices · reduce-auto-load-token · autoload-slimming-feasibility · autoload-test-framework-blueprint · r1r12-token-efficiency-deep-research · token-guardian-research · autoload-offload-assessment

### 已被 12-rule-deepened-research 整合（3 份）
karpathy-mnilax-best-solution · 12-rule-canon-CLAUDE-slim · 12-rule-canon-PORTABLE

### 已執行落地的計劃書/執行報告（9 份）
cc-workspace-coldstart-action-plan · context-window-management-action-plan · prompt-harness-action-plan · subagent-agent-team-execution-plan · action-plans-execution-report · autoload-test-gates-execution-report · memory-audit-and-r1r12-defer-execution-report · r12-unverified-success-proposal（commit b5715db8 已 APPLY）· zeuik-workspace-canon-execution-plan

### 重疊 session-insights（1 份）
session-insights（→ 由 session-insights-v2 涵蓋）
