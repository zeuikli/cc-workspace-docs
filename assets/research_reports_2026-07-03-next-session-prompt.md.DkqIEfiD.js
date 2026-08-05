import{c as a,Q as n,j as e,m as p}from"./chunks/framework.BXc4yaFE.js";const u=JSON.parse('{"title":"新 Session 啟動 Prompt（harness 升級收尾）","description":"","frontmatter":{"date":"2026-07-03T00:00:00.000Z","purpose":"harness 升級計畫收尾——複製整段貼進新 session 即可開跑","source_routine":"manual-fable5-session","type":"session-prompt"},"headers":[],"relativePath":"research/reports/2026-07-03-next-session-prompt.md","filePath":"research/reports/2026-07-03-next-session-prompt.md","lastUpdated":1785909234000}'),t={name:"research/reports/2026-07-03-next-session-prompt.md"};function r(o,s,l,i,c,d){return n(),e("div",null,[...s[0]||(s[0]=[p(`<h1 id="新-session-啟動-prompt-harness-升級收尾" tabindex="-1">新 Session 啟動 Prompt（harness 升級收尾） <a class="header-anchor" href="#新-session-啟動-prompt-harness-升級收尾" aria-label="Permalink to &quot;新 Session 啟動 Prompt（harness 升級收尾）&quot;">​</a></h1><blockquote><p>使用方式：merge PR #812 後開新 session，把下方區塊整段貼上。</p></blockquote><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>任務：執行 research/reports/2026-07-03-harness-upgrade-plan.md 的全部剩餘項目——Phase 1（1.1–1.6）、Phase 2（2.1–2.4，2.5 視結果）、Phase 3（3.1–3.7）。4.1b 由我親測，不歸你。</span></span>
<span class="line"><span></span></span>
<span class="line"><span>先讀（依序）：</span></span>
<span class="line"><span>1. research/reports/2026-07-03-harness-upgrade-plan.md（進度帳本，唯一任務來源）</span></span>
<span class="line"><span>2. .claude/refs/judgment-rubrics.md（五大判斷查表）</span></span>
<span class="line"><span>3. .claude/refs/delegation-protocol.md（委派守則）</span></span>
<span class="line"><span>4. .claude/refs/maintenance-protocol.md（權限邊界）</span></span>
<span class="line"><span>背景需要時查 research/reports/2026-07-03-harness-audit-fable5.md。</span></span>
<span class="line"><span></span></span>
<span class="line"><span>工作規則：</span></span>
<span class="line"><span>1. 先開 feature branch：bash scripts/feature.sh start harness-plan-execution。</span></span>
<span class="line"><span>2. 指揮官不下場：haiku=機械修、sonnet=實作/起草、opus=審查；交辦用 .claude/refs/task-templates.md 填空（含 Done-when 與 Return）；主對話只裁決 + 親跑確定性 gate。</span></span>
<span class="line"><span>3. 每完成一項：驗收證據貼前 5/後 5 行 → 在 upgrade-plan 對應行打 ✅ → git commit（帶 pathspec）。隨做隨存，不攢批。</span></span>
<span class="line"><span>4. 核可欄=「要」的項目（1.2/1.3/1.4/1.6/3.3/3.4/3.5/3.7）：先貼 diff 摘要與風險問我，批准才動；核可=「免」的直接做。</span></span>
<span class="line"><span>5. Phase 1.1 方向勿搞反：改 scripts/healthcheck.sh 的 baseline 17→18；hooks README 的 18 是正確值，勿動。動手前先親跑 python3 重數 settings.json matcher 群組確認。</span></span>
<span class="line"><span>6. Phase 2 每個 cycle 走 /autoload-evolution：≤1 規則/cycle、≤50 行 diff、附 Falsifiable Prediction；cycle 後親跑六源量測（wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy,README}.md）+ behavioral eval；回歸 ≥5pp 立即 git revert。</span></span>
<span class="line"><span>7. 全部完成後收尾三步：bash scripts/healthcheck.sh 到 FAIL=0 → 派 fresh-context 異模型對抗審查全部 diff（修完為止）→ verified-merge 流程開 PR 給我。</span></span>
<span class="line"><span>8. 判斷一律查表：judgment-rubrics R3 觸發即停下問我；R4 訊號出現=換路不重試；subagent 回報的任何數字，寫入交付前主對話親跑同一命令對帳（LESSONS 2026-07-03 教訓）。</span></span>
<span class="line"><span>9. session 尾聲更新 memory/MEMORY.md session block 並 push；中斷或額度告急用 /handoff。</span></span>
<span class="line"><span></span></span>
<span class="line"><span>已解事項（勿重做、勿質疑）：sonnet alias 已實測 = claude-sonnet-5（delegation-protocol §2/§7）；hooks matcher 總數 = 18 已對抗審查確認。</span></span>
<span class="line"><span>待我親測（幫我留欄位）：Opus 4.8 導流是否耗 Fable 額度——我會用 /usage 前後對比，結果請寫回 delegation-protocol §7（update-in-place）。</span></span></code></pre></div>`,3)])])}const m=a(t,[["render",r]]);export{u as __pageData,m as default};
