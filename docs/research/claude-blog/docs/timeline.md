---
title: "Claude Blog 公告時間軸"
type: blog-index
---

# Claude Blog 公告時間軸

> 涵蓋期間：2025-11-13 ~ 2026-07-28 | 資料來源：[claude.com/blog](https://claude.com/blog)  
> 資料庫共 152 篇，4 個分類；本時間軸列出其中的重點條目 | 最後更新：2026-08-05

---

## 2026 年七月第四週（Jul 22–28）

### 2026-07-28 — Announcements（Major）
**[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)**  
MCP 第五版規格：核心改為 stateless（可部署 serverless / edge）、Extensions 版本化（MCP Apps、Tasks）、授權對齊 OAuth 2.0 / OIDC。Claude 全產品線支援，可用 server 超過 950 個。

### 2026-07-24 — Announcements（Major）
**[Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)**  
`claude-opus-5` 發布，1M context，$5/$25 與 Opus 4.8 同價。Frontier-Bench 為 4.8 的 2 倍；CursorBench 與 Fable 5 差距 < 0.5% 而成本減半。成為 Claude Max 預設模型。

### 2026-07-24 — Claude Code / Agents（Major）
**[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)**  
Anthropic 為 Opus 5 / Fable 5 刪掉 Claude Code system prompt 的 80% 以上，coding evals 無可量測退化。六條 Then→Now：judgment over rules、tool design over examples、progressive disclosure、簡化描述去重、auto-memory、rich references。

### 2026-07-24 — Claude Code / Agents / Enterprise
**[Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)**  
官方選型框架：從最強模型起步再往下調；class × effort 決定 per-task 經濟性；Advisor 策略（Sonnet + Fable 監督 = 90% 效能 / 63% 成本）；自建 eval > 公開 benchmark。

### 2026-07-22 — Claude Code
**[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)**  
把反覆手動執行的品質檢查編碼成 Skill，讓 agent 自己閉環。四種部署形態：standalone / embedded / chained / PR-wide。

### 2026-07-22 — Claude Code / Agents
**[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude)**  
可連續數小時自主調查完整攻擊網路的 Recon Agent。設計原則：受限 orchestration + 不受限判斷；敵意環境下假設 agent 會被挾持而建 blastbox 沙箱。

---

## 2026 年七月第三週（Jul 15–21）

### 2026-07-21 — Enterprise / Claude Code（Major）
**[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)**  
在「AI 撰寫 80% 合併程式碼」下的安全實踐：審查左移、多個窄焦點 agent 各持獨立 context 審同一 PR、遠端 VM 只開 allowlist 出口、所有 agent 動作進 SIEM、漏洞自動回寫 CLAUDE.md。

### 2026-07-21 — Enterprise / Claude Code
**[How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code)**  
Temper：agent 產出精確規格而非應用程式碼，由確定性 kernel 以符號推理、窮舉狀態探索與 property testing 驗證後才執行。

### 2026-07-17 — Enterprise
**[Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)**  
四個評估問題（不可信內容 / 可採取行動 / 爆炸半徑 / 可觀測性）與七項核心控制。核心論點：職責不是追求零風險，而是讓代理風險「可見且有界」。

### 2026-07-16 — Claude Code / Enterprise
**[How Anthropic runs large-scale code migrations with Claude Code](https://claude.com/blog/ai-code-migration)**  
六步驟遷移框架（規則手冊 → 依賴映射 → 壓力測試 → 翻譯 → 編譯 → 行為驗證）。Bun 兩週遷移百萬行 Zig → Rust，100% 通過既有測試。核心理念：修復流程而非代碼。

### 2026-07-15 ~ 07-20 — Enterprise（Working at the frontier 系列）
Fable 5 的生產採用案例：[Rakuten](https://claude.com/blog/working-at-the-frontier-rakuten)（07-20，通宵建 agent）、[Cursor](https://claude.com/blog/working-at-the-frontier-cursor)（07-17，最難的 1% 問題）、[Base44](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work)（07-15）。

---

## 2026 年七月第一、二週（Jul 1–14）

### 2026-07-07 — Claude Code（Major）
**[Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)**  
模型決定能力範圍，effort 決定投入多少（讀幾個檔案、驗證幾次、執行多深）。Claude 跳過檔案、未跑測試或放棄多步任務 → 提高 effort 而非換 prompt。三層比喻：Fable 見過罕見問題的專家 / Opus 有深度經驗的專家 / Sonnet 能力強的通才。

### 2026-07-06 — Claude Code
**[A field guide to Claude Fable: finding your unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns)**  
工作品質受限於「釐清 unknowns 的能力」而非模型本身。四類 unknowns 分類與實作前中後的對應流程。

### 2026-07-13 / 07-10 / 07-08 — Enterprise
Working at the frontier 系列續：[Hebbia](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail)（金融實地查核）、[Cognition](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night)（通宵作業）、[Thomson Reuters](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work)（高風險專業工作）。

### 2026-07-07 — Announcements / Claude Code
[Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government)、[Claude Cowork is coming to mobile and web](https://claude.com/blog/cowork-web-mobile)。

### 2026-07-02 — Announcements
**[Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)**  
Claude Code 專屬用量分頁、Analytics Chat 自然語言查詢、model defaults/entitlements、75%/90% 用量門檻警示。

---

## 2026 年六月第五週（Jun 29 – Jul 1）

### 2026-06-30 — Announcements（Major）
**[Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)**  
`claude-sonnet-5` 取代 Sonnet 4.6 成為 Claude Code 預設模型（v2.1.197）。1M context；促銷 $2/$10 至 08-31，之後 $3/$15。Agentic 能力大幅躍進，幻覺與 sycophancy 降低。

### 2026-06-30 — Claude Code
**[Getting started with loops](https://claude.com/blog/getting-started-with-loops)**  
四種 agentic loop：Turn-based / Goal-based（`/goal`）/ Time-based（`/loop`、`/schedule`）/ Proactive。選擇關鍵是退出條件是否可驗證。

### 2026-06-29 — Announcements
[Claude apps gateway for Amazon Bedrock and Google Cloud](https://claude.com/blog/introducing-the-claude-apps-gateway)、[Claude in Microsoft Foundry GA](https://claude.com/blog/claude-in-microsoft-foundry)。

---

## 2026 年六月第四週（Jun 22–28）

### 2026-06-24 — Enterprise
**[Building effective human-agent teams](https://claude.com/blog/building-effective-human-agent-teams)**  
從單人 AI 互動轉向 multiplayer 人機協作。四大心法：公開透明分享脈絡、明確角色分工、設定 North Star、漸進建立信任。實作範例含 Doer-Verifier harness 與每週 lessons & missteps 報告。

### 2026-06-24 — Claude Code
**[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](https://claude.com/blog/agent-identity-access-model)**  
Agent 取得獨立身份與憑證的存取模型。

### 2026-06-22 — Enterprise
[The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry](https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry)。

---

## 2026 年六月第三週（Jun 15–21）

### 2026-06-18 — Claude Code（Major）
**[Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)**  
七種行為調整機制的選擇框架：改變「知道什麼」→ CLAUDE.md / Rules / Skills；改變「呼叫什麼工具」→ Subagents / MCP；生命週期自動化 → Hooks；輸出外觀 → Output Styles / System Prompt Appending。

### 2026-06-18 — Announcements
**[Claude Code now supports artifacts](https://claude.com/blog/artifacts-in-claude-code)**  
工作 session 轉為互動網頁，自動更新、版本歷史、存取控制。使用場景：PR walkthrough、事故調查、安全稽核（Team/Enterprise Beta）。

### 2026-06-18 — Announcements / Enterprise
**[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth)**  
管理員集中管控 MCP connector 授權。

### 2026-06-17 — Enterprise
[Secure access to the Claude Platform with Workload Identity Federation](https://claude.com/blog/workload-identity-federation)、[Claude Design now stays on brand](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work)。

---

## 2026 年六月第二週（Jun 9–15）

### 2026-06-12 — Claude Code
**[How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)**  
Anthropic 內部多部門（GTM、法務、行銷、資安、資料分析）的 Claude Code 實際應用案例。95% 商業查詢自動化；新員工第一天即可用 20+ skills 插件。

### 2026-06-10 — Agents
**[The evolution of agentic surfaces: building with Claude Managed Agents](https://claude.com/blog/building-with-claude-managed-agents)**  
Managed Agents 定位為 composable production-grade agent APIs 套件，從原型到生產數天完成。整合 Dreaming、Outcomes、排程、Vault、Sandbox、MCP Tunnel 等全套功能。

### 2026-06-09 — Announcements（Major）
**[Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)**  
Anthropic 最強公開模型 Fable 5（Mythos-class + 安全分類器）發布。ViBench / FrontierBench 最高分，Analytics benchmark 首破 90%。$10/$50 per MTok，1M context，128k 輸出。訂閱免費至 6/22，6/23 起需 Credits。

### 2026-06-09 — Announcements
**[New in Claude Managed Agents: schedule and vaults](https://claude.com/blog/whats-new-in-claude-managed-agents)**  
Scheduled Deployments（cron 觸發 session）和 Vaults with Environment Variables（API Key 網路邊界替換，Agent 不見明文）Public Beta。

### 2026-06-05 — Claude Code
**[How one Anthropic seller rebuilt his team's workflows with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering)**  
非技術背景業務主任建立 Gmail AI 草稿工具，衍生成 20+ skills Cowork 插件。

---

## 2026 年六月第一週（Jun 2–8）

### 2026-06-03 — Claude Code
**[Running an AI-native engineering org](https://claude.com/blog/running-an-ai-native-engineering-org)**  
JIT Planning 取代季度 Roadmap；Claude Code 團隊連續四個月無非 Claude 協助 commit。

### 2026-06-03 — Claude Code
**[Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)**  
Anthropic 內部 Skill 九大類別分類法與進階技術（on-demand hooks、assets 資料夾、持久記憶）。

### 2026-06-02 — Claude Code
**[A harness for every task: dynamic workflows in Claude Code](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)**  
Dynamic Workflows 六大模式深度解析（Adversarial verification / Tournament / Loop until done 等）。

---

## 2026 年四月第三週（Apr 17–23）

### 2026-04-22 — Agents
**[Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp)**  
MCP 達到 3 億月下載量，Tool Search 模式降低 85% token 用量。Anthropic 正式定義 MCP 為生產 Agent 標準化基礎層。

### 2026-04-20 — Claude Code
**[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon)**  
5 個黑客松得獎項目，4 位非專業開發者（律師、醫師、音樂人）。CrossBeam 縮短加州住宅許可審批，Elisa 讓孩童學習寫程式。

### 2026-04-16 — Claude Code
**[Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code)**  
Opus 4.7 最佳實踐：`xhigh` 成為預設努力等級，自適應思考機制，第一輪完整給 context。

---

## 2026 年四月第二週（Apr 10–16）

### 2026-04-15 — Claude Code
**[Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)**  
1M token context 的管理策略：rewind/clear/compact 決策框架，context rot 防範。

### 2026-04-14 — Claude Code / Announcements
**[Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign)**  
桌面 App 全面重新設計：多 Agent 並行、drag-and-drop 版面、內建終端機和 diff 檢視器。

### 2026-04-14 — Announcements
**[Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code)**  
Routines（Research Preview）：三種自動化模式（排程/API/GitHub webhook），Pro 每日 5 次。

### 2026-04-10 — Agents
**[Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense)**  
七大安全優先行動：AI 加速漏洞利用時代下的防禦策略，CISA KEV 24 小時修補目標。

### 2026-04-10 — Claude Code
**[Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent)**  
從 Agent 視角設計工具的哲學：Progressive Disclosure、20 個工具上限、迭代思維。

### 2026-04-10 — Agents
**[Multi-agent coordination patterns: Five approaches and when to use them](https://claude.com/blog/multi-agent-coordination-patterns)**  
五種多 Agent 協調模式完整框架。Generator-Verifier 最廣泛部署，生產系統通常組合多種模式。

---

## 2026 年四月第一週（Apr 02–09）

### 2026-04-09 — Announcements
**[The advisor strategy: Give agents an intelligence boost](https://claude.com/blog/the-advisor-strategy)**  
Advisor Tool：Haiku + Opus Advisor 可達 BrowseComp 19.7%→41.2%，成本降 85%。一行 API 實作。

### 2026-04-09 — Announcements
**[Making Claude Cowork ready for enterprise](https://claude.com/blog/cowork-for-enterprise)**  
企業版 Cowork：RBAC、每團隊預算、OpenTelemetry（Splunk 整合）、Zoom MCP connector。

### 2026-04-08 — Announcements
**[Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents)**  
雲端託管 Agent API：$0.08/session-hour，10x 更快部署，Public Beta 上線。

### 2026-04-08 — Enterprise AI
**[How Carta Healthcare gets AI to reason like a clinical abstractor](https://claude.com/blog/carta-healthcare-clinical-abstractor)**  
Context Engineering（不是 prompt 撰寫）是真正瓶頸。臨床擷取達 98-99% 準確率，部署縮短至數週。

### 2026-04-07 — Claude Code
**[How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code)**  
Subagent 使用指南：隔離 context、並行執行、多種呼叫方式。非所有任務都適合委派。

### 2026-04-02 — Agents
**[Harnessing Claude's intelligence: 3 key patterns for building apps](https://claude.com/blog/harnessing-claudes-intelligence)**  
三種架構模式：通用工具、消除不必要抽象、Prompt Caching（靜態前置可降 90% 成本）。

---

## 2026 年三月（Mar 2026）

### 2026-03-30 — Announcements
**[Audit Claude Platform activity with the Compliance API](https://claude.com/blog/claude-platform-compliance-api)**  
Compliance API：組織管理員可程序化存取審計日誌，追蹤管理操作和資源活動。

### 2026-03-24 — Claude Code
**[Auto mode for Claude Code](https://claude.com/blog/auto-mode)**  
Auto mode：智能分類器審查每個工具呼叫，自動阻止潛在破壞性操作，同時允許安全操作。

### 2026-03-23 — Announcements
**[Put Claude to work on your computer](https://claude.com/blog/dispatch-and-computer-use)**  
Claude 電腦使用能力（Cowork + Claude Code）：控制滑鼠、鍵盤、瀏覽器。Dispatch 跨設備任務指派。

### 2026-03-19 — Claude Code
**[Product management on the AI exponential](https://claude.com/blog/product-management-on-the-ai-exponential)**  
Claude Code Head of Product 探討 AI 快速迭代如何改變產品管理：短衝刺 + Demo 優先開發。

### 2026-03-18 — Claude Code
**[Code with Claude comes to San Francisco, London, and Tokyo](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo)**  
開發者大會擴展至三個城市：舊金山（5/6）、倫敦（5/19）、東京（6/10）。

### 2026-03-13 — Enterprise AI
**[1M context is now generally available for Opus 4.6 and Sonnet 4.6](https://claude.com/blog/1m-context-ga)**  
1M token context 正式開放：統一定價不額外收費，每次請求支援 600 張圖片或 PDF 頁面。

### 2026-03-12 — Announcements
**[Claude now creates interactive charts, diagrams and visualizations](https://claude.com/blog/claude-builds-visuals)**  
Claude 可在對話中直接生成互動圖表和視覺化，無需程式碼，適用於所有訂閱方案。

### 2026-03-11 — Enterprise AI
**[Advancing Claude for Excel and PowerPoint](https://claude.com/blog/claude-excel-powerpoint-updates)**  
跨檔案 context 共享、Skill 自動化，擴展至 Bedrock、Vertex AI、Microsoft Foundry。

### 2026-03-09 — Claude Code
**[Bringing Code Review to Claude Code](https://claude.com/blog/code-review)**  
多 Agent 並行 code review：54% 的 PR 收到實質性評論（舊版 16%），平均發現 7.5 個問題。

### 2026-03-05 — Agents
**[Common workflow patterns for AI agents—and when to use them](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them)**  
三種主要 Agent 工作流：Sequential、Parallel、Evaluator-Optimizer。從最簡單模式開始。

### 2026-03-03 — Claude Code
**[Improving skill-creator: Test, measure, and refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)**  
Skill-creator 新增評估框架、多 Agent 並行測試和自動描述優化。

---

## 2026 年二月（Feb 2026）

### 2026-02-24 — Agents
**[Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance)**  
五個金融 Plugin（投行、股權研究、私募、財富管理）+ FactSet 和 MSCI 連接器。

### 2026-02-24 — Agents
**[Cowork and plugins for teams across the enterprise](https://claude.com/blog/cowork-plugins-across-enterprise)**  
私有 Plugin 市場，超過 12 個預建跨部門 Plugin 模板（HR、設計、工程、財務）。

### 2026-02-23 — Claude Code
**[How AI helps break the cost barrier to COBOL modernization](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization)**  
Claude Code 自動化 COBOL 複雜分析：跨數千行映射依賴、識別隱式數據流，數季完成現代化。

### 2026-02-20 — Claude Code
**[Bringing automated preview, review, and merge to Claude Code on desktop](https://claude.com/blog/preview-review-and-merge-with-claude-code)**  
即時應用預覽、自動化 code review、GitHub PR 管理（含自動修復和合併）。

### 2026-02-17 — Announcements
**[Increase web search accuracy and efficiency with dynamic filtering](https://claude.com/blog/improved-web-search-with-dynamic-filtering)**  
動態過濾：Claude 透過程式碼執行過濾搜尋結果，BrowseComp 從 33.3% 提升至 46.6%，token 降 24%。

### 2026-02-12 — Enterprise AI
**[Claude Enterprise, now available self-serve](https://claude.com/blog/self-serve-enterprise)**  
Claude Enterprise 直接線上購買，無需銷售對話。幾分鐘內部署 SSO、SCIM、審計日誌。

### 2026-02-09 — Enterprise AI
**[Behind the model launch: What customers discovered testing Claude Opus 4.6 early](https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early)**  
Harvey（BigLaw Bench 90.2%）、Bolt.new（首次嘗試診斷 bug）、Shopify、Lovable 早期測試回饋。

### 2026-02-05 — Enterprise AI
**[Advancing finance with Claude Opus 4.6](https://claude.com/blog/opus-4-6-finance)**  
Opus 4.6 金融推理：Real-World Finance 比 Sonnet 4.5 高 23+ 個百分點。Cowork 桌面 + PowerPoint 整合。

---

## 2026 年一月（Jan 2026）

### 2026-01-30 — Agents
**[Customize Cowork with plugins](https://claude.com/blog/cowork-plugins)**  
11 個開源 Plugin 涵蓋銷售、財務、法律、行銷。Plugin 捆綁 skill、connector、slash command 和 sub-agent。

### 2026-01-29 — Claude Code
**[A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude)**  
開發者、MCP 建置者和高級用戶的 Skill 建立指南，15-30 分鐘完成第一個有效 Skill。

### 2026-01-29 — Claude Code
**[Understand Claude Code's impact with contribution metrics](https://claude.com/blog/contribution-metrics)**  
貢獻指標追蹤：每位工程師每天合併 PR 增加 67%，70-90% 的程式碼使用 Claude Code 協助撰寫。

### 2026-01-28 — Enterprise AI
**[How leading retailers are turning AI pilots into enterprise-wide transformation](https://claude.com/blog/how-leading-retailers-are-turning-ai-pilots-into-enterprise-wide-transformation)**  
AI 試點規模化指南：Shopify AI 助手、L'Oréal 15+ 專業 Agent 協調（150 個國家）。

### 2026-01-26 — Enterprise AI
**[How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds](https://claude.com/blog/how-anthropic-uses-claude-marketing)**  
非技術行銷人員使用 Claude Code 構建 Figma 插件和 Google Ads 工作流，廣告創作從 30 分鐘降至 30 秒。

### 2026-01-23 — Agents
**[Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)**  
三個適合多 Agent 的場景：context 隔離、並行執行、專業工具/領域知識。超出這三個場景協調成本超過收益。

### 2026-01-22 — Agents
**[Building agents with Skills: Equipping agents for specialized work](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work)**  
Agent Skills 新範式：Progressive Disclosure 管理 context window，通用 Agent + Skill 優於專用 Agent。

### 2026-01-21 — Agents
**[Eight trends defining how software gets built in 2026](https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026)**  
2026 年八大軟體開發趨勢：AI 用於 60% 的工作，但只有 0-20% 可完全委派，人工監督仍不可或缺。

---

## 2025 年十二月（Dec 2025）

### 2025-12-19 — Agents
**[Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers)**  
Skill 與 MCP server 協同：MCP 提供連接，Skill 負責邏輯，職責分離確保企業級可靠性。

### 2025-12-18 — Agents
**[Skills for organizations, partners, the ecosystem](https://claude.com/blog/organization-skills-and-directory)**  
組織級 Skill 管理：Skill 目錄（Notion、Canva、Figma、Atlassian 整合）+ Agent Skills 開放標準。

### 2025-12-12 — Enterprise AI
**[Making Claude a better electrical engineer](https://claude.com/blog/making-claude-a-better-electrical-engineer)**  
與 Diode Computers 合作：Sonnet 4.5 在數小時內生成完整電路圖，工程師偏好比例 80% vs Sonnet 4。

### 2025-12-09 — Enterprise AI
**[How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026)**  
500+ 技術領導者調查：57% 部署多階段 Agent，80% 回報可量化 ROI。Thomson Reuters 法律研究從小時到分鐘。

### 2025-12-08 — Enterprise AI
**[How Anthropic's legal team cut review times from days to hours with Claude](https://claude.com/blog/how-anthropic-uses-claude-legal)**  
法律合約審閱：Slack 整合工作流，合規審閱從 2-3 天縮短至 24 小時。

---

## 2025 年十一月（Nov 2025）

### 2025-11-19 — Agents
**[How to create Skills: Key steps, limitations, and examples](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)**  
自訂 Skill 五步驟流程：從概念到部署，清晰描述對正確觸發至關重要。

### 2025-11-17 — Enterprise AI
**[How three YC startups built their companies with Claude Code](https://claude.com/blog/building-companies-with-claude-code)**  
HumanLayer、Ambral 和 Vulcan：分離工作流（研究/規劃/實作）、多模型委派、非技術創辦人可競爭。

### 2025-11-13 — Agents
**[Skills explained: How Skills compares to prompts, Projects, MCP, and subagents](https://claude.com/blog/skills-explained)**  
Skill 在 Claude 生態中的定位：Skill 負責知識、MCP 負責連接、subagent 負責任務委派。完整比較框架。

---

## 主題演進觀察

```
Nov 2025:      Skills 生態系建立（定義、比較、建立指南）
Dec 2025:      企業採用調查 + 真實案例（法律、電氣工程）
Jan 2026:      開發者工具（Contribution Metrics、Skill 完整指南）
              多 Agent 系統架構框架（multi-agent when/how）
Jan 2026:      Cowork Plugin 發布（11 個開源 Plugin）
Feb 2026:      Opus 4.6 發布（金融、企業採用）
              Claude Enterprise 自助購買
Mar 2026:      1M Context GA + Excel/PPT 整合
              Code Review 多 Agent（54% 覆蓋率）
              Auto Mode 發布
Apr 02:        Prompt Caching 架構模式
Apr 07–10:    三天 Agent 技術密集發布（Subagents、工具設計、協調模式、安全）
Apr 08–09:    平台化宣告（Managed Agents、Cowork Enterprise、Advisor Tool）
Apr 14:        開發者體驗（桌面重設計、Routines）
Apr 15–16:    使用指南（1M Context 管理、Opus 4.7 實踐）
Apr 20–22:    社群成果 + MCP 里程碑（黑客松、300M 下載）
Apr 30:        Claude Security Public Beta（漏洞利用等級 Mythos Preview 開放）
May 06:        Managed Agents：Dreaming / Outcomes / Multiagent Orchestration
May 09–26:    三城市 Code w/ Claude（SF → London → Tokyo）
May 19–28:    Dynamic Workflows Research Preview；HTML-First 策略
Jun 02–03:    技術深潛系列（Dynamic Workflow 六模式、Skills 九大類、AI 原生工程）
Jun 09:        Fable 5 / Mythos 5 發布 ← 最強公開模型；Managed Agents Schedule + Vaults
Jun 10:        Managed Agents 演進全貌（agentic surfaces overview）
Jun 18:        行為調整機制總整理（七種機制選擇框架）；Artifacts 進 Claude Code
Jun 24:        人機協作團隊（multiplayer）＋ Agent 獨立身份存取模型
Jun 30:        Sonnet 5 發布（新預設模型，1M ctx）；Agentic loop 四型態指南
Jul 07:        模型 × effort 選擇指南 ← 「effort 是投入量，不是能力」
Jul 16:        大規模程式碼遷移六步驟框架（Bun：百萬行 Zig → Rust）
Jul 17–21:    安全季：CISO 指南、AI 原生 SDLC 安全、Datadog 確定性 kernel
Jul 22:        驗證迴圈 Skill 化 ← 驗證觸發權從模型回到 harness
Jul 24:        Opus 5 發布；Claude 5 世代 context engineering 新規則（system prompt −80%）
Jul 24:        官方模型選型框架（class × effort × 單位經濟）
Jul 28:        MCP 2026-07-28 規格（stateless core、Extensions、OAuth/OIDC）
```

### 2026 下半年的三條主線

1. **從「堆規則」轉向「信任判斷」**：Claude 5 世代刪 system prompt 80%+ 無退化，官方把 context engineering 的預設立場從 over-constrain 改為 progressive disclosure。
2. **驗證的觸發權從模型收回 harness**：`/verify`、`/code-review`、`/deep-research` 陸續改為手動呼叫；同時官方推廣把驗證編碼成 Skill 與 PR-wide gate。
3. **扇出從「越多越好」轉向「有界治理」**：subagent 上限、預設不巢狀、預算真正止血、背景 session 收尾語義明確化。

*更新至 2026-07-28（資料庫收錄截止），最後編修 2026-08-05*
