---
title: "終稽核 v2 交叉驗證附錄（fable-pilot §模式1 fan-out 補跑）"
date: 2026-06-12
status: applied（新發現 6 項已修 5 / 例外註記 1）
method: "fable-pilot §模式1 完整協議——2× auditor fan-out（ground-truth 注入 + 已修清單 + file:line 強制）→ 主對話逐項 grep 親驗 → rejected-claims ledger"
prior: 2026-06-11-final-self-audit-v2.md（spend limit 下單視角親審；本附錄為承諾的交叉視角補跑）
scope: 全 instruction 檔（skills+commands / agents+refs+root 兩域）
type: audit-addendum
---

# 交叉驗證附錄

> **TLDR**：v2 報告的全部 finding 經兩位獨立 auditor 抽查 **confirm（或 confirm-已修）**，無一被推翻；交叉視角另抓出 v2 漏掉的 **6 項新發現**（全為低嚴重度），已修 5、例外註記 1。Ground-truth 注入協議首次完整運作：零「Fable 5 不存在」類誤報；rejected-claims ledger 收 1 筆（auditor 引用過期 v2 文本宣稱 sync script 仍半失效——親驗 exit 0 推翻）。

## v2 報告抽查結果（雙域 ×5 spot-checks）

全部 confirm：byte 快照已除、review-by 已錯峰、model-fit 已還原 + pending 欄、verified-merge 計數 29、fable-pilot 與 settings 一致。auditor 對「v2 寫 fable-5、現檔 sonnet-4-6」的時序困惑 = v2 為 dated snapshot、修正發生在報告之後——報告不回溯改寫（歷史不竄改原則）。

## 交叉視角新發現（v2 漏掉的，全部 file:line 親驗）

| # | 發現 | 處置 |
|---|------|------|
| 1 | `refs/README.md:40` SA-2「見 MEMORY」死 forward-reference（MEMORY 無 SA-2 條目；agent-team-patterns 無任何觸發入口） | ✅ 已修：trigger-index 補入口（on-demand 零 auto-load 成本）+ README 註記閉合 |
| 2 | `AGENTS-ROSTER.md` Quick Reference 僅 10 列 vs 完整表 15 列，無標注 → 誤導性局部視圖 | ✅ 已修：標題標注「常用 10 速查；全 15 見下表」 |
| 3 | `sonnet-pilot/SKILL.md:19`「Opus 4.7 graded」 | ✅ 已修：標注為 2026-05 benchmark 快照之 evaluator provenance（不竄改歷史評分者；重跑時改用現役 evaluator） |
| 4 | `commands/README.md:8`「9 個 autoresearch 子命令」實為 10（wiki.md 補建後未同步——本 session 自己的漏） | ✅ 已修：9→10 |
| 5 | `handoff/` 無獨立 GOTCHAS.md（inline 段不被 `*/GOTCHAS.md` 級掃描器發現） | ✅ 已修：抽出為 GOTCHAS.md（3 條 P+S+驗證格式），SKILL 留指針 |
| 6 | `security-compliance/` GOTCHAS 僅在 references/ 層 | ✅ 已修：頂層指針檔（雙 glob 模式皆可發現） |
| 7 | `research-hub/SKILL.md` 421 行 > skill-evolution 350 行 rubric → 掃描恆 OVER_LIMIT | ⚠️ 例外註記：rubric 已標「預防性指引（<500 硬線）」；421 行屬合規區間，OVER_LIMIT 為預防訊號非違規。納入該 SKILL review-by 時評估 Progressive Disclosure |

## Rejected-claims ledger

1. auditor-2：「`_sync_skill_roster.py` 半失效自動化仍為殘留項」——**推翻**：722ace3 已停用 docs/INDEX 目標，親驗 exit 0、輸出 actionable（auditor 複誦 v2 文本而未驗當前檔——「引用報告 ≠ 驗證現實」的又一例證）。

## 協議效果評估（fable-pilot §模式1 首次完整運作）

- **Ground-truth 注入有效**：兩位 auditor 零模型存在性誤報（對照前次未注入時的「Fable 5 不存在」誤報）。
- **已修清單防重報部分有效**：仍有 1 筆過期複誦穿透 → 協議補強候選：已修清單應附 commit sha，並要求 auditor「對已修項宣稱殘留前必親驗當前檔」。已記入 fable-pilot GOTCHAS 候選。
- 雙域 verdict 一致：**domain clean；殘留項全為使用者裁決級**（Co-Authored 慣例、guidelines provenance 署名、Fable 基線可選補測、research-hub 行數例外）。

## 驗證

healthcheck PASS 125 / WARN 2（既有）/ FAIL 0；全部修正後 `*/GOTCHAS.md` 掃描 29/29 skill 可發現。
