---
title: "Anthropic 400K Sessions「Returns to Expertise」研究 — 深度分析 + workspace 可執行方案"
date: 2026-06-20
status: research complete · 方案為 PROPOSE/DEFER（auto-load 變更須走 /autoload-evolution，不在本報告 inline apply）
branch: claude/anthropic-claude-code-expertise-5myrpg
method: fan-out 2× researcher（官方 verbatim 抽取 + 第三方批判）→ 主對話綜合 → fable-pilot 審閱
primary_source: "https://www.anthropic.com/research/claude-code-expertise"
source_topic: "research/DAILY-RESEARCH/2026-06-20.md#topic-3-anthropic-claude-code-expertise-study-400k"
type: deep-research + execution-plan
verbatim_policy: V=多來源一致引用原文措辭 · D=合理聚合非確認 verbatim
---

# Anthropic 400K Sessions 研究深度分析 + 可執行方案

> **定位**：本報告 (1) 深入解析 Anthropic「Agentic coding and persistent returns to expertise」研究的方法學、量化發現與**三大缺席批判**；(2) 對照本 workspace 既有 The Loop / subagent 設計，輸出 PROPOSE/DEFER 帳本。
> **接地鐵律**：量化主張標 V/D；對 auto-load 規則的任何變更**僅 PROPOSE 不 inline apply**（須走 `/autoload-evolution` 閉環：≤1 規則/cycle、≤50 行 diff）。

---

## 0. TL;DR

- **研究核心**：~400K sessions / ~235K users（Oct 2025–Apr 2026）顯示 **domain expertise > coding background**；十大職業群組 verified success rate 全落在軟體工程師 ±7pp 內，**Management 甚至最高**。
- **本研究最強的不是「民主化」而是「expertise 轉移型態」**：expertise 的回報沒被 AI 抹平，而是從「技術執行」轉向「判斷品質」（精確描述目標 + 驗證輸出）。人類主責 ~70% planning、Claude 主責 ~80% execution。
- **三大缺席批判**（三篇分析文 + 搜尋全未正面點出）：① **無控制組**（不知道用戶「不用 Claude Code」的基準）；② **利益衝突 + 無同行評審**（Anthropic 研究自家旗艦產品）；③ **verified-success 的循環性**（Claude 評估 Claude 生成的 code 是否通過 Claude 協助寫的測試）。
- **直接反證**：Anthropic 自家 2026-02 另一研究（InfoQ）顯示 AI 輔助使初級工程師**技能掌握 ↓17%**——與本研究「session 成功率提升」形成**短期效率 vs 長期技能積累**的根本張力。
- **對 workspace 的最大價值**：本研究**實證背書**了 workspace 既有的兩條核心設計 —— (a)「判斷 vs 決定」分工（human plans / LLM executes）；(b) TEST 階段的 `verified vs unverified` 嚴格定義（passing tests / committed / explicit confirmation）。**驗證既有 > 新增規則**。
- **可執行方案**：4 項 PROPOSE（其中 2 項須走 /autoload-evolution gate）+ 3 項 RECORD（既有設計獲背書，僅記錄對應）。零 auto-load inline 變更。

---

## 1. 研究方法學（verbatim 接地）

| 項目 | 數值 | 標記 |
|------|------|------|
| Sessions | ~400,000 | V |
| Users | ~235,000 | V |
| 時間範圍 | Oct 2025 – Apr 2026（7 個月）| V |
| 資料來源 | Claude Code sessions（CLI + claude.ai + desktop app）| V |
| 排除 | Non-interactive usage 完全排除 | V |
| 平均 session 長度 | ~4 turns | V |
| 作者 | Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Ryan Heller, Peter McCrory | V |
| 分析工具 | **Clio**（privacy-preserving；arxiv 2412.13678）| 中 |

> **TODO(conflict): chose「Clio」over「Cleo」+ reason** — 第三方轉述出現「Cleo」拼法，但主來源 agent 交叉核對 arxiv 2412.13678 的 Clio 工具，且 tigzig 明確否認 Cleo。優先採 Clio（一手 arxiv > 二手轉述拼字）。

**Verification success 定義（V，原文重建）**：
> "the session ended with real evidence that the goal was met, such as passing tests, committed work, or explicit confirmation from the user."

兩層並行指標：**Verified success**（嚴格：有具體佐證）/ **Partial success**（寬鬆：某種程度完成）。

**Expertise 分類（V，原文重建）** —— **task-specific 非職稱**：
> "Claude rates the user's apparent expertise at the task on a five-point scale from novice to expert. The expertise classifier looks for three signals: how precisely the user frames their directions, what they ask Claude to verify, and whether the user tends to correct Claude or Claude tends to correct the user."

→ 資深工程師碰不熟的語言可被評 novice；會計師對對帳流程可被評 expert。**這是全研究最被低估的設計**：它量測的是「對任務的掌握」而非「頭銜」。

---

## 2. 核心發現 — The Expertise Paradox

論述鏈：
1. 直覺預期：agentic coding 應「民主化」程式能力 → 任何人 + Claude 都能寫 code。
2. 資料反駁：expertise 的回報**未消失**，反而更結構化顯現。
3. 機制：人類主責 planning（what to build / what counts as done）= 需域知識；Claude 主責 execution（how）= 技術實作被抽象化。
4. 結論：「能否精確描述目標 + 驗證輸出符合業務需求」比「能否親手寫 code」更決定成敗。
5. 表象：各職業成功率**收斂**（within 7pp）；但 task-specific expertise 的**分層仍清晰**。
6. 反直覺核心：expertise 的回報不是被抹平，而是**被保留並轉移型態** —— 從技術執行 → 判斷品質。

---

## 3. 量化指標

### Expert vs. Novice（全 V）

| 指標 | Novice | Intermediate | Expert |
|------|--------|-------------|--------|
| Verified success rate | 15% | 28% | 33% |
| Partial success rate | 77% | 91% | 92% |
| Claude actions / prompt | 5 | — | 12 |
| Words / prompt output | 600 | — | 3,200 |
| 困難 session 放棄率 | 19% | 5–7% | 5–7% |

> "Most of the gain comes from moving from novice to intermediate; between intermediate and expert, the slope decreases." (V)

**關鍵次要洞見**：novice 與 expert 的差距核心是**恢復力非起步力** —— novice 遇困難放棄 19% vs expert 5–7%；recovery rate novice 4% vs expert 15%（V）。

### 人機分工（V）

> "users are responsible for approximately 70% of planning decisions, while Claude handles about 80% of execution decisions."

### 職業群組（V）

| 群組 | Verified（overall）| Verified（code-producing）| Partial |
|------|------|------|------|
| Software/math | 30% | 34% | 89% |
| Other occupations | 26% | 29% | 88% |
| Management | **highest of all** | — | — |

> "every one of the ten largest occupation groups landed within seven points of software engineers." (V)
> 命名群組：lawyers, analysts, scientists, marketers, sales professionals, management。最快成長：Business/Finance、Arts/Design/Media、Management、Life/Physical/Social Sciences。（完整 10 大名單原文未列全 — 標記**低信心**）

### 7 個月任務組成變化（全 V）

| 任務類型 | Oct 2025 | Apr 2026 | Δ |
|---------|---------|---------|---|
| Fixing broken code | 33% | 19% | −14pp |
| Operating software | 14% | 21% | +7pp |
| Writing / data analysis | ~10% | ~20% | ~×2 |

靜態截面：code(write/fix/test/orchestrate) 56% · operating 17% · planning/understanding 14% · analysis/prose 13%。

### 經濟價值（V）

計算法：「freelance marketplace 報價估算，對齊真實貼文公開資料集」。
平均 session value **+27%**；Building **+43%** / Operating **+34%** / Fixing **+32%**。

---

## 4. 批判分析（本報告的差異化價值）

### 4.1 研究者自陳限制（V）
- **無法觀測真實結果**："We cannot measure real-world outcomes, like whether code written in a session is actually used or discarded."
- **成功分類依賴模型讀 transcript 非人工標注**；classifier 規模化驗證困難（session 過長，人工 ground truth 不可得）。

### 4.2 三大缺席批判（三篇分析 + 搜尋全未正面點出）

| # | 缺席批判 | 嚴重度 | 為何致命 |
|---|---------|--------|---------|
| 1 | **無控制組** | 高 | 沒有「同一用戶不用 Claude Code」基準，無法歸因成功率提升於工具 |
| 2 | **利益衝突 + 無同行評審** | 高 | AI 公司觀察自家旗艦產品，商業動機與研究動機重疊，未經第三方學術審查 |
| 3 | **verified-success 循環性** | 中高 | Claude 評估 Claude 生成的 code 是否通過 Claude 協助寫的測試 → self-evaluation bias（與 workspace `unverified_success` 閘門同源警告）|

### 4.3 直接反證 — 技能侵蝕張力
**Anthropic 自家 2026-02 研究（InfoQ）**：52 名初級工程師學陌生 Python 函式庫（Trio），AI 輔助組任務快 2 分鐘（不顯著）但**測驗分數 50% vs 手動組 67%（↓17pp）**；把 code 生成全委 AI → 分數 <40%，用 AI 問**概念**問題 → ≥65%。

→ 本 400K 研究測的「session 成功率提升」可能**與技能積累下降同步發生**。短期效率 ↑ 與長期 capability ↑ 不必然同向。**這條對 workspace 的 self-evolution 設計有直接啟示**（見 §5.4）。

### 4.4 第三方詮釋分歧
- **Crypto Briefing**：純正面轉述（零批判）「AI 放大而非取代」。
- **AI Weekly**：勞動替代風險框架；明確質疑 operationalization 不透明 + 15% novice 成功率意味 85% session 無確認產出。
- **ExplainX**：最誠實 —— 承認 15–33% verified 絕對值偏低、session ≠ 完整專案、7pp 差距在更長任務「可能擴大」。

---

## 5. 對本 workspace 的影響（接地既有設計）

> 原則：**驗證既有設計 > 新增規則**（core.md Framework Integrity「移除後 Claude 在哪犯錯？」）。本研究多數是對 workspace 現有契約的**外部實證背書**，非新規則需求。

### 5.1 ✅ 背書「判斷 vs 決定」分工（core.md 跨切紀律）
研究的 human 70% planning / Claude 80% execution，**精準對映** workspace「LLM 只做判斷、確定性代碼做決定」+「on-rails/off-rails 分類」。→ **RECORD 對應，零變更**。

### 5.2 ✅ 背書 TEST 階段 `verified vs unverified` 嚴格定義
研究的 verified-success 定義（passing tests / committed / explicit confirmation）= workspace `unverified_success` 閘門（「subagent 自報成功 = 中間態，主對話親跑確定性檢查才升 verified」）。研究的 4.1 自陳限制（self-evaluation bias）正是 workspace 設此閘門的理由。→ **RECORD：研究是此閘門的外部理據**。

### 5.3 PROPOSE — IDENTIFY 階段納入「task-specific expertise」自評
研究最強設計（expertise = task-specific 非職稱）→ workspace IDENTIFY 階段（core.md:29 既有）**可新增** domain-expert task-specific 自評維度：開工前快速自評「對此任務領域我是 expert / novice」，novice 時**加重 IDENTIFY 假設列舉 + 成功條件具體化**（因 novice 起步成功率僅 15%，缺口在驗證能力）。
**Gate**：此為 core.md auto-load 變更 → **DEFER 至 `/autoload-evolution`**（不在本報告 inline 改）。falsifiable：注入後 novice 類任務的 IDENTIFY 假設數應 ↑、return-trip 修正應 ↓。

### 5.4 PROPOSE — 反技能侵蝕的委派框架（呼應 §4.3）
InfoQ 反證：「把生成全委 AI → 技能 ↓；用 AI 問概念 → 技能保留」。workspace 既有「規則 = decaying cache / 換模型世代須重評」已部分對應，但可補：**委派 subagent 時優先「解釋 why + trace」而非僅「給 patch」**（讓主對話保留判斷迴路）。已部分存在於 subagent-strategy「child 輸出只含結果」與 RECORD「人工介入 = 診斷訊號」。→ **RECORD 對應 + 低優先 PROPOSE 強化措辭**（DEFER）。

### 5.5 NOT-A-CONFLICT — Expert 12 actions/prompt vs fan-out ≤4
研究的「expert 每 prompt 觸發 12 actions」與 subagent `fan-out ≤4` **是不同軸**：actions/prompt = 單一 agent 的工具呼叫密度；fan-out = 平行 sub-agent 數。**不可混用、不調 fan-out**。→ **RECORD（TODO(conflict) 已釐清為非衝突）**。

### 5.6 RECORD — session value +27% 作為 automation ROI 候選基準
研究的 freelance-marketplace 估值法（+27% / build+43%）可作 workspace automation ROI 敘事基準，但**估值法本身有 §4.1 限制**，僅作方向性參考非硬指標。

---

## 6. APPLY / DEFER 帳本

| # | 行動 | 類型 | 處置 | Gate / 理由 |
|---|------|------|------|------|
| 5.1 | 「判斷 vs 決定」獲背書 | RECORD | 記錄對應 | 零變更；外部實證 |
| 5.2 | `unverified_success` 閘門獲背書 | RECORD | 記錄對應 | 研究 self-eval bias = 設閘理由 |
| 5.3 | IDENTIFY 納 task-specific expertise 自評 | PROPOSE | **DEFER → /autoload-evolution** | core.md auto-load 變更，≤1 規則/cycle |
| 5.4 | 反技能侵蝕委派措辭（why+trace）| PROPOSE | **DEFER → /autoload-evolution** | subagent-strategy 變更；先觀察 |
| 5.5 | Expert 12 actions vs fan-out 4 | RECORD | 釐清非衝突 | 不調 fan-out |
| 5.6 | session value +27% ROI 基準 | RECORD | 候選基準 | 估值法有限制，方向性參考 |

> **本報告零 auto-load inline 變更**。5.3/5.4 兩項若採納，須各自獨立走 `/autoload-evolution` 閉環（eval 回歸 ≥5pp → revert）。

---

## 7. 來源

**一手**：
- [Agentic coding and persistent returns to expertise — Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- [Clio: Privacy-Preserving Insights into Real-World AI Use — arXiv 2412.13678](https://arxiv.org/pdf/2412.13678)

**反證（Anthropic 自家）**：
- [AI Coding Assistance Reduces Developer Skill Mastery by 17% — InfoQ](https://www.infoq.com/news/2026/02/ai-coding-skill-formation/)

**第三方分析**：
- [Crypto Briefing](https://cryptobriefing.com/anthropic-claude-code-economic-research/)（純正面）
- [AI Weekly](https://aiweekly.co/alerts/anthropic-domain-expertise-beats-coding-background)（勞動替代框架 + 質疑）
- [ExplainX](https://explainx.ai/blog/anthropic-claude-code-expertise-research-agentic-coding-2026)（最誠實批判）
- [TIGZIG](https://www.tigzig.com/post/anthropic-claude-code-expertise-survey-jun2026) · [Growth Academy](https://www.growthacademy.global/blog/expertise-beats-coding) · [36Kr EN](https://eu.36kr.com/en/p/3856818580673792) · [DigitalToday](https://www.digitaltoday.co.kr/en/view/67522/claude-code-400000-session-analysis-non-developers-use-expands)

---

_研究方法：2× researcher 平行 fan-out（官方 verbatim + 第三方批判）→ 主對話交叉核驗綜合 → fable-pilot 審閱。所有量化標 V/D；auto-load 變更僅 PROPOSE，執行走 /autoload-evolution gate。_
