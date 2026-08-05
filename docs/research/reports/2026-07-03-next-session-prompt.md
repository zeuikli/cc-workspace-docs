---
date: 2026-07-03
purpose: harness 升級計畫收尾——複製整段貼進新 session 即可開跑
source_routine: manual-fable5-session
type: session-prompt
---

# 新 Session 啟動 Prompt（harness 升級收尾）

> 使用方式：merge PR #812 後開新 session，把下方區塊整段貼上。

```
任務：執行 research/reports/2026-07-03-harness-upgrade-plan.md 的全部剩餘項目——Phase 1（1.1–1.6）、Phase 2（2.1–2.4，2.5 視結果）、Phase 3（3.1–3.7）。4.1b 由我親測，不歸你。

先讀（依序）：
1. research/reports/2026-07-03-harness-upgrade-plan.md（進度帳本，唯一任務來源）
2. .claude/refs/judgment-rubrics.md（五大判斷查表）
3. .claude/refs/delegation-protocol.md（委派守則）
4. .claude/refs/maintenance-protocol.md（權限邊界）
背景需要時查 research/reports/2026-07-03-harness-audit-fable5.md。

工作規則：
1. 先開 feature branch：bash scripts/feature.sh start harness-plan-execution。
2. 指揮官不下場：haiku=機械修、sonnet=實作/起草、opus=審查；交辦用 .claude/refs/task-templates.md 填空（含 Done-when 與 Return）；主對話只裁決 + 親跑確定性 gate。
3. 每完成一項：驗收證據貼前 5/後 5 行 → 在 upgrade-plan 對應行打 ✅ → git commit（帶 pathspec）。隨做隨存，不攢批。
4. 核可欄=「要」的項目（1.2/1.3/1.4/1.6/3.3/3.4/3.5/3.7）：先貼 diff 摘要與風險問我，批准才動；核可=「免」的直接做。
5. Phase 1.1 方向勿搞反：改 scripts/healthcheck.sh 的 baseline 17→18；hooks README 的 18 是正確值，勿動。動手前先親跑 python3 重數 settings.json matcher 群組確認。
6. Phase 2 每個 cycle 走 /autoload-evolution：≤1 規則/cycle、≤50 行 diff、附 Falsifiable Prediction；cycle 後親跑六源量測（wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy,README}.md）+ behavioral eval；回歸 ≥5pp 立即 git revert。
7. 全部完成後收尾三步：bash scripts/healthcheck.sh 到 FAIL=0 → 派 fresh-context 異模型對抗審查全部 diff（修完為止）→ verified-merge 流程開 PR 給我。
8. 判斷一律查表：judgment-rubrics R3 觸發即停下問我；R4 訊號出現=換路不重試；subagent 回報的任何數字，寫入交付前主對話親跑同一命令對帳（LESSONS 2026-07-03 教訓）。
9. session 尾聲更新 memory/MEMORY.md session block 並 push；中斷或額度告急用 /handoff。

已解事項（勿重做、勿質疑）：sonnet alias 已實測 = claude-sonnet-5（delegation-protocol §2/§7）；hooks matcher 總數 = 18 已對抗審查確認。
待我親測（幫我留欄位）：Opus 4.8 導流是否耗 Fable 額度——我會用 /usage 前後對比，結果請寫回 delegation-protocol §7（update-in-place）。
```
