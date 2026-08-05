# reports/INDEX.md

> Type: wiki:synthesis
> Harness-Layer: L4-knowledge
> **Type:** wiki:generated — autoresearch / overnight-research 輸出
> **Updated**: 2026-07-11（active 115 份 + archive 59 份；計數實測 ls *.md）
> **Query pattern**: BRAIN.md → 本表（Topic 欄位）→ 具體報告
> **歸檔慣例**：已被母報告整合的前置研究 + 已執行落地的計劃書 → `archive/`（內容不變、可逆；見文末 Archive 列）

---

## ⭐ Canonical 整併報告（先讀這份）

| 檔案 | 說明 |
|------|------|
| [2026-08-03-behavioral-equivalence-oracle-design.md](2026-08-03-behavioral-equivalence-oracle-design.md) | 行為等價 oracle 設計：消融對照臂解開 v5「無對照」死結；14 個機械簽名（零 LLM）；鑑別力實測而非作者標註；P0 計量層已實作並過資格考，P1–P3 未執行 |
| [2026-08-03-selftest-coverage-inventory.md](2026-08-03-selftest-coverage-inventory.md) | self-test 覆蓋盤點：86 支腳本 75 支無自測，依「有自動呼叫端 × 失敗不響」排序；本輪補前三名並以 mutation 驗過 oracle 資格 |
| [2026-08-02-harness-four-channel-model.md](2026-08-02-harness-four-channel-model.md) | Harness 通道模型（常駐/按需/閘門/路由/記憶）· 薄 harness 四種含義辨析 · loop=退化的 graph · 單人 vs 團隊 harness = principal 模型 · 三方對抗複審與五項自我訂正 · 完整復盤 |
| [harness-v5.1-simplification](2026-08-02-harness-v5.1-simplification.md) | **Harness v5.1 單人化精簡完整刪除報告** — hooks 26→13、refs 26→11、rules 5→3、收據制度移除；逐檔理由/風險登記/回滾路徑（Opus 5 + Sonnet 5 雙視角、Fable 5 合成） |
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
| 2026-07-11 | [session-insight-workspace-agent](2026-07-11-session-insight-workspace-agent.md) | **智能體化全案單日實錄**（129 commits）：AgentEngine/KYU OS 層/SIA Routine 化/output-compress 雙版/Usage 治理/hook 工程；PR #858 |
| 2026-07-11 | [fable-token-efficiency](2026-07-11-fable-token-efficiency.md) | Fable token 精簡三源研究（abmedia advisor/orchestrator 96%/46%、cyberq、caveman）→ 五層 token-efficiency-plan 依據 |
| 2026-07-11 | [caveman-skill-feasibility](2026-07-11-caveman-skill-feasibility.md) | Caveman 為基礎開發 SKILL 可行性：缺陷診斷（零保真驗證/不適配模型）→ output-compress 設計依據（白名單+檔位上限+機械閘）|
| 2026-07-04 | [territory-beyond-workspace](2026-07-04-territory-beyond-workspace.md) | **平台疆域盲點掃描**：8 層 out-of-repo 力量（trigger store/模型調用真相/env 注入/四排程器）支配 Loop 自主性；濃縮版 → `.claude/refs/platform-territory.md`，機械覆核 → `scripts/territory-probe.sh` |
| 2026-07-03 | [harness-audit-fable5](2026-07-03-harness-audit-fable5.md) | **Fable 5 全面稽核**：三大慢性病診斷 + 4 制度檔（delegation/judgment/templates/maintenance）+ 給未來 session 的信（盤點原始清單見 `2026-07-03-harness-audit-appendix/`）|
| 2026-07-03 | [harness-upgrade-plan](2026-07-03-harness-upgrade-plan.md) | 稽核後可執行計畫（Phase 0–4：小修/六源瘦身/skills 路由/世代校準；含核可欄與機械驗收）|
| 2026-06-18 | [harness-derivation-deep-research](2026-06-18-harness-derivation-deep-research.md) | **12-cluster fan-out Harness 推導**（~36 篇語料；12 條工程定律）|
| 2026-06-18 | [harness-implementation-roi-eval](2026-06-18-harness-implementation-roi-eval.md) | 實作有效性 ROI 評估（12-unit fan-out）+ autoload byte 優化落地（18,990→18,509）|
| 2026-06-05 | [harness-memory-self-evolution-synthesis](2026-06-05-harness-memory-self-evolution-synthesis.md) | Harness 自演化合成（活文件，18 篇論文 + 一手洞察）|
| 2026-05-31 | [consolidated-agent-engineering-research](2026-05-31-consolidated-agent-engineering-research.md) | **Agent 工程研究合成母報告** |
| 2026-05-31 | [harness-engineering-deep-research](2026-05-31-harness-engineering-deep-research.md) | Harness 工程深度研究（27 篇論文；D2 交叉驗證）|
| 2026-05-28 | [harness-evolution-plan](archive/2026-05-28-harness-evolution-plan.md) | Harness 演化計劃（大型設計記錄）|

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
| 2026-06-04 | `token-guardian-execution-plan` | Token 守衛計劃書（APPLY 待 gated）|
| 2026-06-04 | `r1r12-token-efficiency-execution-plan` | R1–R12 token 效率計劃書（APPLY 待 gated）|

---

## 12-Rule / Best Practices

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-05 | [12-rule-deepened-research](2026-06-05-12-rule-deepened-research.md) | **12 條準則論文接地深化母報告**（信度分級）|
| 2026-06-05 | [12-rule-deepened-ruleset](2026-06-05-12-rule-deepened-ruleset.md) | 可部署深化準則全文（子條延伸）|
| 2026-06-04 | [12-rule-universal-ruleset](2026-06-04-12-rule-universal-ruleset.md) | stack/harness-agnostic 版本 |
| 2026-06-04 | [karpathy-mnilax-12-rule-universalization-research](2026-06-04-karpathy-mnilax-12-rule-universalization-research.md) | 通用化研究（8 篇論文接地 + MAST 完整性）|
| 2026-06-04 | `12-rule-canon-patch-proposal` | canon 修補提案（P1+P2 APPLY 待核准）|

---

## Sub-Agent / Agent Team

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-04 | [research-fleet-research](archive/2026-06-04-research-fleet-research.md) | 平行研究艦隊（scratch-file + reducer + citation 重驗）|
| 2026-06-04 | `research-fleet-execution-plan` | 研究艦隊計劃書（改進 overnight-research，APPLY 待 gated）|
| 2026-06-04 | [merge-pipeline-research](archive/2026-06-04-merge-pipeline-research.md) | 自我驗證 merge pipeline（4 道 gate + removed-content manifest）|
| 2026-06-04 | `merge-pipeline-execution-plan` | verified-merge SKILL 計劃書（APPLY 待 gated）|
| 2026-06-12 | [multi-mode-agent-skill-design](archive/2026-06-12-multi-mode-agent-skill-design.md) | multi-mode skill(router)+agent(worker) 配對：四模式內聯 · 自動 model 路由 · 破-4 dynamic-workflow fan-out · /loop 接線（applied）|

---

## Skill / Workspace Canon

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-12 | [cross-validation-audit-addendum](2026-06-12-cross-validation-audit-addendum.md) | 終稽核 v2 交叉驗證：v2 finding 全 confirm · 新發現 6 項已修 5 · ground-truth 協議首次完整運作（零模型誤報）|
| 2026-06-11 | [session-insights-loop-fable-rewrite](2026-06-11-session-insights-loop-fable-rewrite.md) | Session 洞察 ×10：驗證閘門隨模型變強更 load-bearing（3 次現場證明）· worktree 基底陷阱 · spend limit 交接固化 · 動態數字不入靜態文件 · 14條零損失退役方法論 |
| 2026-06-11 | [final-self-audit-v2](2026-06-11-final-self-audit-v2.md) | 三波修正後終稽核：4 低度矛盾 · 5 漂移/形式合規 · 3 壞示範；⚠️ model-fit baseline 待實測（report-only，主對話親審）|
| 2026-06-11 | [post-rewrite-self-audit](archive/2026-06-11-post-rewrite-self-audit.md) | 全量改寫後最終自我稽核：GOTCHA 未升格 ×4 · 過期經驗數字 · pilot 去留等 3 項待裁決（report-only）|
| 2026-06-11 | [loop-only-canon-integration](archive/2026-06-11-loop-only-canon-integration.md) | The Loop 唯一準則化：R1–R14 徹底退役 · Loop 順序統一（core.md canonical）· byte 量測對齊六源 · 軟性預算（applied）|
| 2026-06-11 | [instruction-files-self-audit](archive/2026-06-11-instruction-files-self-audit.md) | 全量 instruction 檔稽核：雙 canonical Loop 順序矛盾 · Fable 5 模型層 drift · byte 量測漏 README · 刪/留裁決清單（report-only）|
| 2026-06-07 | [skill-consolidation-spec](archive/2026-06-07-skill-consolidation-spec.md) | 27 SKILL 同質性矩陣 + 整併評估（Mnilax 三層成本接地；ship-review 維持獨立）|
| 2026-06-06 | [the-loop-canonicalization-and-audit-insights](archive/2026-06-06-the-loop-canonicalization-and-audit-insights.md) | §Rn 退役 + 全 workspace 稽核方法論 |
| 2026-06-06 | [zeuik-workspace-canon](archive/2026-06-06-zeuik-workspace-canon.md) | The Loop 準則重構（六階段語意 header）|
| 2026-06-06 | [coldstart-execution-efficiency-audit](2026-06-06-coldstart-execution-efficiency-audit.md) | 冷啟動執行效率評估（時間/空間雙維度）|
| 2026-06-05 | [skill-evolution-report](2026-06-05-skill-evolution-report.md) | Skill 演化報告（27 skills 對齊工作日誌）|
| 2026-06-05 | [claudemd-best-practices](2026-06-05-claudemd-best-practices.md) | CLAUDE.md 最佳實踐（443 repo 實證）|
| 2026-06-05 | [d4-per-rule-verifier-poc](2026-06-05-d4-per-rule-verifier-poc.md) | D4 Hybrid verifier PoC |
| 2026-06-05 | `next-steps-execution-plan` | 下一步計劃書（APPLY/DEFER 帳本）|
| 2026-05-31 | [claude-dir-inventory](archive/2026-05-31-claude-dir-inventory.md) | .claude/ 目錄盤點 |

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
| 2026-06-07 | [deep-practices-v2-execution-plan](archive/2026-06-07-deep-practices-v2-execution-plan.md) | 六主題排程（對稱懷疑剔除幻覺 key + tradeoff）|

---

## Session Insights

| 日期 | 報告 | 核心主題 |
|------|------|---------|
| 2026-06-15 | [session-insights-scoring-unification-index-sync](2026-06-15-session-insights-scoring-unification-index-sync.md) | 評分機制統一（27 tweets A-E /10）· INDEX 全局同步（tweets 267/scored 50）· heredoc bug 根治 · /qp quality-pipeline 設計 |
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
