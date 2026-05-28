import{c as a,Q as n,j as p,m as e}from"./chunks/framework.BXc4yaFE.js";const k=JSON.parse('{"title":"Overnight Research Template","description":"","frontmatter":{"title":"Overnight Research Template","type":"template"},"headers":[],"relativePath":"research/templates/overnight-research-template.md","filePath":"research/templates/overnight-research-template.md","lastUpdated":1779894392000}'),i={name:"research/templates/overnight-research-template.md"};function l(t,s,h,c,r,o){return n(),p("div",null,[...s[0]||(s[0]=[e(`<h1 id="overnight-research-template" tabindex="-1">Overnight Research Template <a class="header-anchor" href="#overnight-research-template" aria-label="Permalink to &quot;Overnight Research Template&quot;">​</a></h1><h1 id="research-hub-autoresearch-goal-通用全自動研究模板" tabindex="-1">research-hub + autoresearch + /goal 通用全自動研究模板 <a class="header-anchor" href="#research-hub-autoresearch-goal-通用全自動研究模板" aria-label="Permalink to &quot;research-hub + autoresearch + /goal 通用全自動研究模板&quot;">​</a></h1><h1 id="版本-1-0-2026-05-15" tabindex="-1">版本：1.0 | 2026-05-15 <a class="header-anchor" href="#版本-1-0-2026-05-15" aria-label="Permalink to &quot;版本：1.0 | 2026-05-15&quot;">​</a></h1><hr><h2 id="使用方式" tabindex="-1">使用方式 <a class="header-anchor" href="#使用方式" aria-label="Permalink to &quot;使用方式&quot;">​</a></h2><h3 id="步驟-1-修改設定-填入-topic-等變數後存檔" tabindex="-1">步驟 1：修改設定（填入 [TOPIC] 等變數後存檔） <a class="header-anchor" href="#步驟-1-修改設定-填入-topic-等變數後存檔" aria-label="Permalink to &quot;步驟 1：修改設定（填入 [TOPIC] 等變數後存檔）&quot;">​</a></h3><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>TOPIC=        # 研究主題，例：&quot;Claude Code hooks 最佳實踐&quot;</span></span>
<span class="line"><span>SCOPE=        # 搜尋範圍關鍵字，例：&quot;Claude Code hooks site:github.com OR site:anthropic.com&quot;</span></span>
<span class="line"><span>REPORT_PATH=  # 輸出報告路徑，例：research/reports/2026-05-15-topic.md</span></span>
<span class="line"><span>MIN_CHARS=    # 報告最低字元數（中文用 wc -m），例：5000</span></span>
<span class="line"><span>ITERATIONS=   # autoresearch 迭代上限（整夜建議 20，快速測試用 5）</span></span></code></pre></div><h3 id="步驟-2-確認-bypasspermissions-已設定" tabindex="-1">步驟 2：確認 bypassPermissions 已設定 <a class="header-anchor" href="#步驟-2-確認-bypasspermissions-已設定" aria-label="Permalink to &quot;步驟 2：確認 bypassPermissions 已設定&quot;">​</a></h3><blockquote><p><code>.claude/settings.json</code> 已設定 <code>&quot;defaultMode&quot;: &quot;bypassPermissions&quot;</code>，無需額外 flag。 若尚未設定，執行 <code>claude --dangerously-skip-permissions</code> 或手動加入設定。</p></blockquote><h3 id="步驟-3-貼入-goal-條件-先貼-後貼工作-prompt" tabindex="-1">步驟 3：貼入 /goal 條件（先貼，後貼工作 Prompt） <a class="header-anchor" href="#步驟-3-貼入-goal-條件-先貼-後貼工作-prompt" aria-label="Permalink to &quot;步驟 3：貼入 /goal 條件（先貼，後貼工作 Prompt）&quot;">​</a></h3><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>/goal 下列三個條件同時成立（評估依據是 transcript 中 Claude 執行命令的實際輸出）：</span></span>
<span class="line"><span>1. wc -m [REPORT_PATH] 的輸出數字 ≥ [MIN_CHARS]</span></span>
<span class="line"><span>2. git log --oneline -1 包含 &quot;research:&quot; 字樣</span></span>
<span class="line"><span>3. bash scripts/healthcheck.sh 的輸出包含 &quot;PASS&quot;</span></span>
<span class="line"><span>若以上輸出尚未在對話中出現，Claude 需執行驗證命令並展示結果，再由評估器判斷。</span></span>
<span class="line"><span>若超過 30 輪仍未達成，停止並輸出截至目前的完成狀態報告。</span></span></code></pre></div><h3 id="步驟-4-貼入工作-prompt-見下方完整版" tabindex="-1">步驟 4：貼入工作 Prompt（見下方完整版） <a class="header-anchor" href="#步驟-4-貼入工作-prompt-見下方完整版" aria-label="Permalink to &quot;步驟 4：貼入工作 Prompt（見下方完整版）&quot;">​</a></h3><hr><h2 id="完整工作-prompt-複製全部貼入" tabindex="-1">完整工作 Prompt（複製全部貼入） <a class="header-anchor" href="#完整工作-prompt-複製全部貼入" aria-label="Permalink to &quot;完整工作 Prompt（複製全部貼入）&quot;">​</a></h2><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>你是一個自主研究 Agent。執行以下研究任務，不需要任何人工確認，直接推進到完成。</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span>## 研究設定</span></span>
<span class="line"><span></span></span>
<span class="line"><span>- **主題**：[TOPIC]</span></span>
<span class="line"><span>- **搜尋範圍**：[SCOPE]</span></span>
<span class="line"><span>- **報告輸出路徑**：[REPORT_PATH]</span></span>
<span class="line"><span>- **報告最低字元數**：[MIN_CHARS]（使用 wc -m 計算，支援中文）</span></span>
<span class="line"><span>- **autoresearch 迭代上限**：Iterations: [ITERATIONS]</span></span>
<span class="line"><span>- **Plateau-Patience**：off（永不因停滯而停止）</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span>## Phase 1：網路搜尋與資料收集</span></span>
<span class="line"><span></span></span>
<span class="line"><span>執行以下工作（使用 WebSearch + WebFetch + research-hub skill）：</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. 用 WebSearch 搜尋主題相關的一手資料來源</span></span>
<span class="line"><span>   - 搜尋詞 A：[SCOPE]</span></span>
<span class="line"><span>   - 搜尋詞 B：[TOPIC] best practices 2024 OR 2025</span></span>
<span class="line"><span>   - 搜尋詞 C：[TOPIC] site:github.com OR site:arxiv.org</span></span>
<span class="line"><span></span></span>
<span class="line"><span>2. 選出最高品質的 10–15 個 URL（優先：官方文件、GitHub、學術論文、知名技術部落格）</span></span>
<span class="line"><span></span></span>
<span class="line"><span>3. 對每個 URL 執行 research-hub article-archive：</span></span>
<span class="line"><span>   - 主要方式：WebFetch</span></span>
<span class="line"><span>   - 備用方式：curl -sL [URL] | python3 -c &quot;import sys; print(sys.stdin.read()[:5000])&quot;</span></span>
<span class="line"><span>   - 提取：標題、作者、日期、核心論點、關鍵代碼/數據、可操作建議</span></span>
<span class="line"><span></span></span>
<span class="line"><span>4. 建立中間暫存摘要（不寫檔案，保留在 context）：</span></span>
<span class="line"><span>   每篇文章格式：</span></span></code></pre></div><h2 id="標題-—-url" tabindex="-1">[標題] — [URL] <a class="header-anchor" href="#標題-—-url" aria-label="Permalink to &quot;[標題] — [URL]&quot;">​</a></h2><p><strong>評分</strong>：A(影響力)/B(原創性)/C(可操作性)/D(可信度)/E(時效性) = 加權分 <strong>核心論點</strong>：2-3 句 <strong>可操作建議</strong>：條列 <strong>關鍵引用</strong>：原文片段（≤100字）</p><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span>## Phase 2：本地知識庫整合（若有）</span></span>
<span class="line"><span></span></span>
<span class="line"><span>若 research/tweets/ 目錄存在且含相關文章：</span></span>
<span class="line"><span>- 派遣最多 4 個平行 Sub Agent，每個負責一個子分類</span></span>
<span class="line"><span>- 每個 Sub Agent 回傳 ≤600 字結構化摘要</span></span>
<span class="line"><span>- 與 Phase 1 的網路資料交叉比對，找出共識與分歧</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span>## Phase 3：synthesize — 生成初版報告</span></span>
<span class="line"><span></span></span>
<span class="line"><span>撰寫完整研究報告，儲存至 [REPORT_PATH]。</span></span>
<span class="line"><span></span></span>
<span class="line"><span>報告結構：</span></span>
<span class="line"><span>\`\`\`markdown</span></span>
<span class="line"><span># [TOPIC] — 深度研究報告</span></span>
<span class="line"><span>**日期**：[DATE] | **字元數目標**：≥ [MIN_CHARS]</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## 執行摘要（≤300字）</span></span>
<span class="line"><span>## 1. 背景與動機</span></span>
<span class="line"><span>## 2. 核心概念分析</span></span>
<span class="line"><span>## 3. 最佳實踐與實作模式</span></span>
<span class="line"><span>## 4. 工具與生態系統比較</span></span>
<span class="line"><span>## 5. 常見陷阱與反模式</span></span>
<span class="line"><span>## 6. 前沿趨勢與預測</span></span>
<span class="line"><span>## 7. 可立即實作的行動建議</span></span>
<span class="line"><span>## 附錄：來源評分與索引</span></span></code></pre></div><p>每節目標字元數：執行摘要 300、背景 500、核心分析 1000、最佳實踐 1000、工具比較 800、陷阱 600、趨勢 500、行動建議 500、附錄 300。</p><hr><h2 id="phase-4-autoresearch-迭代改進" tabindex="-1">Phase 4：autoresearch 迭代改進 <a class="header-anchor" href="#phase-4-autoresearch-迭代改進" aria-label="Permalink to &quot;Phase 4：autoresearch 迭代改進&quot;">​</a></h2><p>啟動 autoresearch 迭代（Iterations: [ITERATIONS]，Plateau-Patience: off）：</p><p><strong>Metric（主指標）</strong>：<code>wc -m [REPORT_PATH]</code>（字元數，higher is better） <strong>Guard（守衛）</strong>：<code>bash scripts/healthcheck.sh</code>（必須 PASS） <strong>Verify command</strong>：<code>wc -m [REPORT_PATH] &amp;&amp; bash scripts/healthcheck.sh | tail -3</code></p><p>迭代策略（按優先序輪換）：</p><ol><li>擴展字元數最少的章節（補充來源、範例、數據）</li><li>追加 WebSearch 搜尋新角度（競品、反例、學術論文）</li><li>加入具體代碼示例或案例研究</li><li>強化「可行動建議」的具體度（加入工具名稱、指令、參數）</li><li>補充「附錄：來源評分」的完整性</li></ol><p>每次迭代：</p><ul><li>執行 ONE focused change</li><li>git commit -m &quot;experiment: [描述改動]&quot;</li><li>執行 verify command 並展示輸出</li><li>若 wc -m 增加 → Keep；相同或減少 → git revert</li></ul><hr><h2 id="phase-5-最終驗證-必須執行並展示輸出" tabindex="-1">Phase 5：最終驗證（必須執行並展示輸出） <a class="header-anchor" href="#phase-5-最終驗證-必須執行並展示輸出" aria-label="Permalink to &quot;Phase 5：最終驗證（必須執行並展示輸出）&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">wc</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -m</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> [REPORT_PATH]</span></span>
<span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">bash</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> scripts/healthcheck.sh</span></span>
<span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">git</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> log</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> --oneline</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -3</span></span>
<span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">ls</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -la</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> [REPORT_PATH]</span></span>
<span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">head</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -30</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> [REPORT_PATH]</span></span></code></pre></div><p>將以上所有命令的輸出完整顯示在 transcript 中（供 /goal 評估器讀取）。</p><hr><h2 id="phase-6-提交" tabindex="-1">Phase 6：提交 <a class="header-anchor" href="#phase-6-提交" aria-label="Permalink to &quot;Phase 6：提交&quot;">​</a></h2><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">git</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> add</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> [REPORT_PATH]</span></span>
<span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">git</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> commit</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -m</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &quot;research: [TOPIC] — 完整研究報告 $(</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">wc</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -m</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> [REPORT_PATH] </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">|</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> awk</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &#39;{print $1}&#39;) 字元&quot;</span></span>
<span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">git</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> push</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> -u</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> origin</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> HEAD</span></span></code></pre></div><hr><h2 id="執行規則" tabindex="-1">執行規則 <a class="header-anchor" href="#執行規則" aria-label="Permalink to &quot;執行規則&quot;">​</a></h2><ul><li>不詢問任何授權、不等待確認、直接推進</li><li>所有驗證指令必須執行並展示實際輸出（不得口頭聲稱「已完成」）</li><li>遇到單一來源抓取失敗 → 跳過並記錄，繼續下一個</li><li>遇到 healthcheck FAIL → <strong>立即停止</strong>，修復後才能繼續（blocking，不得跳過）；修復失敗 ≥ 3 次 → 停止並回報用戶</li><li>每完成一個 Phase → 輸出 checkpoint：「Phase N 完成：[做了什麼 / 驗了什麼 / 剩什麼]」</li></ul><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## 快速填表（複製後替換）</span></span>
<span class="line"><span></span></span>
<span class="line"><span>| 變數 | 說明 | 範例 |</span></span>
<span class="line"><span>|------|------|------|</span></span>
<span class="line"><span>| \`[TOPIC]\` | 研究主題 | Claude Code hooks 最佳實踐 |</span></span>
<span class="line"><span>| \`[SCOPE]\` | 搜尋關鍵字 | &quot;Claude Code hooks&quot; site:github.com |</span></span>
<span class="line"><span>| \`[REPORT_PATH]\` | 報告儲存路徑 | research/reports/2026-05-15-claude-hooks.md |</span></span>
<span class="line"><span>| \`[MIN_CHARS]\` | 最低字元數 | 5000 |</span></span>
<span class="line"><span>| \`[ITERATIONS]\` | autoresearch 上限 | 20（整夜）/ 5（快速測試） |</span></span>
<span class="line"><span>| \`[DATE]\` | 今天日期 | 2026-05-15 |</span></span>
<span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## /goal 評估條件（替換後貼入）</span></span></code></pre></div><p>/goal 下列三個條件同時成立（評估依據是 transcript 中 Claude 執行命令的實際輸出）：</p><ol><li>wc -m [REPORT_PATH] 的輸出數字 ≥ [MIN_CHARS]</li><li>git log --oneline -1 包含 &quot;research:&quot; 字樣</li><li>bash scripts/healthcheck.sh 的輸出包含 &quot;PASS&quot; 若以上輸出尚未在對話中出現，Claude 需執行 Phase 5 驗證命令並展示結果，再由評估器判斷。 若超過 30 輪仍未達成，停止並輸出截至目前的完成狀態報告。</li></ol><div class="language- vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span></span></span>
<span class="line"><span>---</span></span>
<span class="line"><span></span></span>
<span class="line"><span>## 設計原理</span></span>
<span class="line"><span></span></span>
<span class="line"><span>| 設計決策 | 原因 |</span></span>
<span class="line"><span>|----------|------|</span></span>
<span class="line"><span>| \`wc -m\` 非 \`wc -w\` | \`wc -w\` 對中文回傳近零（whitespace 分詞），\`wc -m\` 計算 Unicode 字元 |</span></span>
<span class="line"><span>| \`/goal\` 條件用命令輸出 | Haiku 評估器只讀 transcript，命令輸出必須顯示在對話中 |</span></span>
<span class="line"><span>| Plateau-Patience: off | 整夜執行，不因 15 輪無改善而停止 |</span></span>
<span class="line"><span>| guard = healthcheck.sh | 防止 autoresearch 優化虛假指標（Echo Chamber 陷阱） |</span></span>
<span class="line"><span>| 每迭代一個 change | 原子性；失敗時精確定位原因 |</span></span>
<span class="line"><span>| Sub-agent fan-out ≤ 4 | CLAUDE.md 規定，超過 4 個並發子代理上限 |</span></span>
<span class="line"><span>| Phase 5 必須展示輸出 | \`/goal\` 評估器依賴 transcript 中的實際輸出，不能只說「已完成」 |</span></span>
<span class="line"><span>| \`--dangerously-skip-permissions\` | 整夜無人值守必須，避免授權提示阻斷執行流 |</span></span></code></pre></div>`,41)])])}const u=a(i,[["render",l]]);export{k as __pageData,u as default};
