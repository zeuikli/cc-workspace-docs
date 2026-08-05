---
title: "最終自我稽核 v2（report-only — 三波修正後殘留項）"
date: 2026-06-11
status: report-only（裁決權在使用者；未修正任何發現）
method: "主對話親審（本 session 已端到端讀寫全部 instruction 檔）+ 全項機械 grep 重驗。**方法偏離明示**：原訂 fan-out auditor 因 org spend limit 不可用，依 fable-pilot §模式1 降級為主對話單視角親審——無 sub-agent 交叉視角，spend limit 解除後建議用 fable-pilot 協議重跑一次交叉驗證。"
prior: f82a381 → a713d18 → ebdd6ac → 8647d18 → 1b70913 → 6b924e8（九波 commits）
scope: CLAUDE.md · rules · skills(29) · commands · agents · refs · hooks · docs · memory · scripts
type: audit
---

# 最終自我稽核 v2

> **TLDR**：三波修正後，高嚴重度項全數關閉（舊準則 grep = 0、Loop 順序統一、byte 量測對齊、定價/ceiling 修正、GOTCHA 升格完成）。殘留 = **4 個低嚴重度矛盾、5 個漂移/形式合規項、3 個壞示範**，全部 file:line 親驗。無一影響行為正確性；多數根因是「會動的數字/狀態寫進了靜態文件」。

## 1. 互相矛盾（雙方原文，全部親驗）

| # | 甲方 | 乙方 | 嚴重度 |
|---|------|------|--------|
| 1a | `scripts/_sync_skill_roster.py:5`「rebuilds the skill table in AGENTS.md **and docs/INDEX.md**」 | `docs/INDEX.md:9-12`「規則 / refs / skills **不在此索引**…Skills（29 個）→ RESOLVER.md + AGENTS.md §6b」——script 每跑必印 `docs/INDEX.md: pattern not found` | 低（半失效自動化） |
| 1b | `docs/harness-guidelines-workspace.md:31`「Sonnet 4.6（**日常**）」 | `.claude/settings.json:4`「"model": "claude-fable-5"」——2026-06-11 起日常預設已是 Fable 5 | 低 |
| 1c | `commands/quick-commit.md:22` 每 commit 附 `Co-Authored-By: Claude` | `core.md` Git 工作流程未規範此 header | 極低（未文件化分歧，非衝突） |
| 1d | `WORKSPACE-INDEX.md:50,271` + `guidelines:52`「~18,969 bytes」快照 ×3 | 實測 `wc -c` 六源 = **18,985**（本日新增 fable-pilot 登錄後） | 低（快照型，必然持續腐化） |

## 2. 弱模型管理規則 / 漂移硬編碼（file:line）

1. **17× SKILL `review-by: 2026-08-23` 批次同日**——批次貼日無差異化重審意義（新建 fable-pilot/handoff 已錯峰 2026-07-11；其餘 9 檔散落 8 個日期）。decaying-cache 規則要的是「對照實際行為重審」，不是日期欄位形式合規。
2. `docs/harness-guidelines-workspace.md:3`「**版本: 1.0** · 2026-05-19」——文件本日已歷三波大改（Loop 階段鍵化、計數、D2/D4 更新）仍標 1.0/舊日期；版本欄已失去資訊量。
3. `docs/harness-guidelines-workspace.md:5`「基礎來源: **Karpathy × Mnilax AB4.0**…」——provenance 署名保留了舊準則名稱；屬出處記載非活規則，但與 §四「R1–R14 已徹底退役」同檔並存，易誤讀。
4. **`harness-model-fit.json` 欄位已被更新**（`model_version: claude-fable-5`、`last_audit: 2026-06-11`）**但 `eval_baseline` 是否真對 Fable 5 重測過，無任何證據**——若 baseline 數字沿用 Sonnet 實測值而標籤換新，是比 drift 更糟的「新標籤舊數據」。⚠️ 建議列為最優先驗證項：跑 `/harness-meta:hmf` 實測，或將 last_audit 回標 pending。
5. **auto-load 餘量僅 15 bytes**（18,985/19,000）——非 drift，但任何 CLAUDE.md/rules 增字都需先減字；結構性壓力，下次規則演化前需先做一輪下沉。

**已檢查、判定非問題**：`agents/researcher.md:19`「預設 Sonnet 4.6」明標出處為 frontmatter live config，正確；`harness-audit-METRICS.md` R1–R6 與 CAR-R1 為各自 rubric 命名空間；haiku/sonnet-pilot 內建補償機制——其目標模型即弱模型，正當；全部 SKILL ≤500 行拆檔線內。

## 3. 以壞示範教學

1. **會動的數字寫進靜態文件**（1d 的根因）：workspace 自家原則「動態資訊經 `<system-reminder>` 注入，不寫進靜態前綴」（context-management），但 WORKSPACE-INDEX/guidelines 三處存 byte 快照——量測命令（`measure.sh --gate`）已是 SSoT，靜態複本每次變更必腐化。本 session 已兩度手動同步又兩度過期。
2. **半失效自動化教人忽略警告**：`_sync_skill_roster.py` 的 `pattern not found` 每跑必印，違反 Fail Loud 精神的實際效果——本 session 主對話也兩次將其當雜訊忽略。半失效輸出比沉默更糟：訓練操作者跳過警告。
3. **review-by 批次日**＝decaying-cache 規則的形式合規（同 2.1）。

## 4. 刪 / 留建議（待裁決，本報告未動手）

### 建議刪/改
1. **WORKSPACE-INDEX:50,271 + guidelines:52 的 byte 快照數字** → 刪具體數字，只留「以 `bash scripts/measure.sh --gate` 為準」。一勞永逸。
2. **`_sync_skill_roster.py` 的 docs/INDEX 目標** → 二擇一：刪 script 的 INDEX 參數（docs/INDEX 設計已明示不索引 skills，建議此案）或在 docs/INDEX 補表。現狀最差。
3. **17× 批次 review-by** → 錯峰（依各 SKILL 變更頻率）或刪欄位、改以 `audit-skills.sh` 月度排程為唯一重審機制。
4. **guidelines header 版本欄** → 遞增至 2.0 + 本日日期，或直接刪版本欄改用 git 歷史。
5. **guidelines:31「Sonnet 4.6（日常）」** → 改「Fable 5（日常預設，2026-06-11 起）/ Sonnet 4.6（成本敏感）…」。
6. ⚠️ **harness-model-fit.json**：若 eval_baseline 未實測 → `last_audit` 回標或補跑 `/harness-meta:hmf`（最優先）。

### 原樣留（理由）
1. **CLAUDE.md + 六源 auto-load 全文**——三波稽核後零矛盾；gate + mutation-tested 守護中；每條可指名失敗模式。
2. **fable-pilot / handoff / harness-loop §Frontier 強化**——本日新建，全部數字 papers 親驗，GOTCHAS 預載實戰教訓。
3. **quick-commit Co-Authored-By**——Anthropic 慣例、無害；入 core.md 不值 byte（餘量 15）。
4. **methodology 文 R1–R14 史料 + guidelines 基礎來源署名**——研究 provenance；退役 banner 已標。徹底清除會折損沿革記錄（此項第三次浮現，維持原判：裁決權在使用者）。
5. **`agents/researcher.md` 等 frontmatter model 宣稱**——live config 描述，準確。

## 方法信度

- 每條 finding 經主對話 grep/sed 親驗（§1–§3 全部附 file:line）；「已檢查非問題」清單明列，防單視角漏報誤判為零發現。
- **單視角限制明示**：無 sub-agent 交叉視角（spend limit）。建議解除後以 fable-pilot §模式1（ground-truth 注入 + rejected-claims ledger）重跑一次交叉稽核，比對本報告。
