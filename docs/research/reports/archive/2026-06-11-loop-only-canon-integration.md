---
title: "The Loop 唯一準則化：舊 R1–R14 編號準則徹底退役 + 稽核修正套用"
date: 2026-06-11
status: applied
basis: research/reports/2026-06-11-instruction-files-self-audit.md
method: The Loop 六階段（OBSERVE→IDENTIFY→PROPOSE→APPLY→TEST→RECORD）；3× researcher fan-out（reports / tweets / papers 全量消化）；所有結論主對話 grep/wc 機械重驗
scope: "CLAUDE.md · .claude/rules/** · .claude/refs/{the-loop-best-solution,harness-loop,trigger-index,README}.md · AGENTS.md · docs/harness-guidelines-* · 索引檔 · scripts/measure.sh"
type: execution
---

# The Loop 唯一準則化 — 執行報告

> **TLDR**：依使用者裁決，「之前的編號準則」（Karpathy R1–R4 + Mnilax R5–R12，外加 R13 PGE / R14 Polyglot = 14 條）已自全 workspace 活文件**徹底退役**；The Loop 六階段成為唯一行為準則，canonical 順序與條文 = `rules/core.md`（OBSERVE→IDENTIFY→PROPOSE→APPLY→TEST→RECORD）。稽核報告三大優先刀（Loop 順序統一 / byte 量測對齊實載六源 / 軟硬預算矛盾）全數落地。

## 研究結論（3× researcher 交叉驗證）

1. **零損失移除**：12 條內容已全數吸收進六階段（06-05 deepened-research §4 + 06-06 workspace-canon §2.2 雙表證明）；僅編號與 lineage 需要移除，行為契約無一遺失。
2. **順序裁決**：canonical = **APPLY→TEST**（使用者明示順序）；harness/破壞性場景的「先驗證再套用」語意改以 **APPLY 前置 gate** 表達，`harness-loop.md` 撤銷「唯一 canonical」宣稱並重排表格。
3. **強模型世代的取捨**（papers 接地）：驗證閘門（unverified_success / PGE / 破壞性 gate）隨模型變強**更**重要（Vesper：強模型 eval-hack 16.6% vs 弱模型 0%）；行為補丁（200 行分段讀、初學者閾值、citation 配額）為弱模型遺產 → 移除。
4. **Token 預算**：硬性 30K session 預算無論文接地且與 70% compact 閾值算術矛盾（70%×200K=140K）→ 改為**軟性參考預算 + 行為信號優先**（ACE / Lost-in-Multi-Turn 接地）。
5. **新增**（tweets 接地）：Effort 先於 model（Mnilax 2026-05-31）；Fable 5 cyber/bio silent fallback → 直接指定 Opus（MEMORY 待整合洞察 #4 落地）；規則 = decaying cache，14–30 天重審（Mnilax dream pass + Anthropic Dreaming）；dynamic workflow 三大失敗模式命名（agentic laziness / self-preferential bias / goal drift）。

## 主要變更

| 項目 | 變更 |
|------|------|
| 編號準則退役 | CLAUDE.md / core.md 移除「Karpathy R1–R4 + Mnilax R5–R12」參考基礎行；`refs/karpathy-mnilax-best-solution.md` → `git mv` → `refs/the-loop-best-solution.md`（lineage 段刪除、Rn 清洗，檢查表/失敗案例保留）；trigger-index / refs README / REFERENCES / BRAIN / WORKSPACE-INDEX / README / docs guidelines 全部改寫為階段鍵；研究歸檔（research/reports、tweets、dated audits）保留原文不竄改歷史 |
| Loop 順序統一 | 全 workspace `PROPOSE→TEST→APPLY` → `PROPOSE→APPLY→TEST`（20+ SKILL 自我進化表 + RESOLVER + pilot-preflights + AGENTS.md + harness-meta-GOTCHAS）；core.md 升格唯一 canonical |
| byte 量測對齊 | 量測集 = 實際 auto-load **六源**（含 rules/README.md）；core.md / rules README / measure.sh / token-waste-audit（18,000→19,000）/ overnight-research GOTCHAS（13KB 硬牆 → 軟性基線）同步 |
| 軟硬預算矛盾 | context-management「硬性 Token Budget」→「軟性參考 + 行為信號優先」；mid-session 換模型 vs escalation 補橋接（sub-agent model override）；「初學者 ~60%」移除 |
| 弱模型補丁移除 | core.md 200 行分段讀規則 → 一般化截斷紀律；Ask-rate / dynamic workflow 去 Opus 4.8 pin |
| 驗證器同步 | measure.sh：六源量測 + 「Token Budget（軟性參考」新錨點 + `grep -c || echo 0` 雙零 bug 修復 |
| 死指針修復 | core.md `refs/harness-meta` → 實際路徑；harness-loop core.md R4/R10/R12 → 階段名 |

## 驗證（TEST）

- `grep -rE "R1–R4|R5–R12" --include="*.md"` 活文件 = 0（僅研究歸檔/含退役 banner 之沿革文件留存）
- `grep -rln "karpathy-mnilax-best-solution"` 活文件 = 0
- `grep -rln "PROPOSE→TEST→APPLY"` = 僅研究歸檔
- auto-load 六源 `wc -c` = **18,969 / 19,000** ✓
- `measure.sh --gate` = GATE PASS；`healthcheck.sh` = PASS 123 / WARN 2（既有 MCP 項）/ FAIL 0

## 未處理（明示）

- `security-hygiene.md`：稽核無 finding，原樣保留。
- pilot 三件套定價/escalation 殘留、agents/commands/hooks/skills 全量改寫 → 下一階段（使用者已追加指示）。
- `memory/MEMORY.md` 263 行 >200 → 全部變更完成後委派 `memory-compactor`。
