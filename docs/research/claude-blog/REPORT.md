---
title: "Claude Blog 文章收錄報告"
type: blog-index
---

# Claude Blog 文章收錄報告

> 收錄來源：[claude.com/blog](https://claude.com/blog)  
> 收錄日期：2026-08-05（前次：2026-07-06；初次：2026-04-23）  
> 收錄文章：152 條目（4 分類，含跨分類重複）  
> 工具限制說明：claude.com/blog 使用 Webflow + Finsweet CMS 前端分頁，每個 category 頁面 SSR 只輸出最多 15 篇。完整清單需使用 Playwright 或 headless browser。

---

## 文章分佈

| 分類 | 篇數 | 涵蓋日期範圍 | 上次以來新增 |
|------|------|------------|------------|
| [Claude Code](./claude-code/index.md) | 45 | 2026-01-29 ~ 2026-07-24 | +10（自 07-06）|
| [Agents](./agents/index.md) | 25 | 2025-11-13 ~ 2026-07-24 | +5（自 07-06）|
| [Enterprise AI](./enterprise-ai/index.md) | 45 | 2025-11-17 ~ 2026-07-24 | +17（自 07-06）|
| [Announcements](./announcements/index.md) | 38 | 2026-02-17 ~ 2026-07-28 | +5（自 07-06）|
| **合計（條目數，含跨分類重複）** | **153** | **2025-11-13 ~ 2026-07-28** | **+37** |

> 跨分類文章（同一篇收錄於多個分類）：`claude-code-desktop-redesign`（Claude Code + Announcements）、`enterprise-managed-auth`（Announcements + Enterprise AI）、`the-new-rules-of-context-engineering-for-claude-5-generation-models`（Claude Code + Agents）、`claude-models-explained-...`（Claude Code + Agents + Enterprise AI）、`how-anthropic-secures-its-ai-native-software-development-lifecycle`（三分類）、`how-outtake-built-a-cyber-investigator-on-claude`、`how-datadog-built-a-universal-machine-tool-for-claude-code`、`ai-code-migration`、`bringing-claude-code-and-claude-cowork-to-government`。去重後約 138 篇。

### 2026-08-05 這次的修補

- 補上 **Claude Sonnet 5 發布公告**（2026-06-30）——先前 announcements 索引遺漏，但 best-practices/41 已在引用。
- 修正 `a-field-guide-to-claude-fable-finding-your-unknowns`（2026-07-06）缺少 `##` 標題導致條目無法被解析的格式問題。
- `docs/timeline.md` 補齊 2026-06-15 ~ 07-28 的空窗（原停在 06-12）。
- `docs/synthesis.md` 增補主題七～九（原僅涵蓋至 2026-04-22）。

---

## 核心主題分析

### 1. Claude Code 快速迭代期（Jan–Jun 2026）

32 篇形成完整開發者平台敘事：

**產品演進軌跡（按時間）**：
- **桌面 App 重新設計**（Apr 14）：多 Agent 並行、drag-and-drop、內建終端機
- **Routines**（Apr 14）：排程/API/webhook 三種自動化
- **1M Context 管理**（Apr 15）：rewind/clear/compact 決策框架
- **Opus 4.7 整合**（Apr 16）：xhigh effort 預設、自適應思考
- **HTML-First Strategy**（May 20）：五大場景全面優於 Markdown
- **Dynamic Workflows**（May 28 + Jun 2）：六大模式、協調數十至數百個並行 Agent
- **Skills 九大類別**（Jun 3）：Anthropic 內部知識系統化，21%→95% 準確率
- **AI 原生工程組織**（Jun 3）：JIT Planning、PR cycle time、Claude-assisted commits ≈100%
- **Fable 5 + Managed Agents 升級**（Jun 9）：最強公開模型 + Scheduled Deployments + Vaults
- **Artifacts**（Jun 18）：session 轉互動網頁，自動更新（Team/Enterprise Beta）
- **Steering Claude Code 官方指南**（Jun 18）：七種機制選擇框架

**非工程師民主化主線**：
- 黑客松三波（Opus 4.6 Apr 20 / Opus 4.7 Jun 15 / Opus 4.8 Jun 17）：得獎者多為律師、醫師、PM、零程式碼背景
- 非技術 PM 六週上架 iOS App（May 1）；業務人員建立 Gmail 插件衍生 20+ skills（Jun 5）

**意涵**：Claude Code 從「AI 輔助工具」演變為「開發者作業系統」，目標市場已超越工程師群體。

---

### 2. Agent 架構知識系統化（Nov 2025–Jun 2026）

20 篇 Agents 文章系統性建立 Agent 工程知識體系：

**Skills 生態系（Nov 2025 ~ Jun 2026）**：
- 6 篇從 Skills 基礎到組織部署完整路徑（創建→測試→九大類別→企業治理）
- 九大類別（Jun 3）：Library/API Reference、Product Verification、Data Fetching、Business Process、Code Scaffolding、Code Quality、CI/CD、Runbooks、Infrastructure Ops

**多 Agent 協調（Apr–Jun 2026）**：
- 五種協調模式（Apr 10）：Generator-Verifier / Orchestrator-Subagent / Agent Teams / Message Bus / Shared State
- Dynamic Workflows 六大模式（May 28 + Jun 2）：Classify-and-act / Fan-out-and-synthesize / Adversarial verification / Generate-and-filter / Tournament / Loop until done
- **實戰案例**：Bun 將 750,000 行 Zig 移植至 Rust，11 天通過 99.8% 測試

**MCP 標準化（Apr–Jun 2026）**：
- 月下載量突破 3 億次，成為生產 Agent 共通層
- Tool Search 模式降低 85%+ token 用量
- MCP Tunnels（May 19）：存取私有網路服務，無需公開暴露
- Enterprise Managed Auth（Jun 18）：Okta IdP 統一配置，zero-touch 設定

**意涵**：Anthropic 已完成 Agent 工程基礎知識的系統性輸出，標誌 Agent 工程進入成熟期。

---

### 3. 企業化進程——從垂直行業到地緣擴張（2025 Q4–2026 Q2）

26 篇 Enterprise AI 形成完整企業採用路徑：

**行業垂直化深化（Apr–Jun 2026）**：

| 行業 | 篇數 | 核心數據 |
|------|------|---------|
| **法律** | 3 | 87% 法務長使用率；12 個實務 Plugin；合約審閱 2-3 天→24 小時 |
| **金融** | 3 | 10 個 Agent 模板；Opus 4.7 Vals AI Finance Agent 64.37%；三行業深度部署指南 |
| **醫療** | 1 | Carta Healthcare 98-99% 臨床準確率；Wisedocs 精度 +30% |
| **資安** | 3 | CLUE 平台 1,870 人工小時節省；LLM 安全掃描 1,596 個漏洞揭露 |
| **創意** | 1 | Ableton、Adobe CC、Autodesk、Blender 整合 |

**亞太地區擴張**：
- **日本**（Apr 24）：NEC 全球 ~3 萬員工部署，最大日本企業 AI 合作夥伴
- **韓國**（Jun 17）：首爾辦公室；NAVER 全工程組織、Nexon、LG CNS、Samsung SDS 全面部署
- **澳洲**（Apr 27）：雪梨辦公室；Commonwealth Bank、Canva、Xero 合作

**企業安全基礎設施（2026 Q2）**：
- **Workload Identity Federation GA**（Jun 17）：短期 OIDC 憑證取代靜態 API key
- **Compliance API 擴展**（May 21）：28 個新整合（Cloudflare、CrowdStrike、Microsoft Purview、Okta）
- **Zero Trust for AI Agents**（May 27）：三層實施框架，八大實施面
- **Self-hosted Sandboxes Public Beta**（May 19）：工具執行移至客戶自管環境

**意涵**：Anthropic 從「通用 AI API」轉向「行業解決方案 + 全球平台生態」，企業安全基礎設施同步成熟。

---

### 4. 成本效率創新（持續累積）

| 技術 | 降成本幅度 | 來源 |
|------|-----------|------|
| Prompt Caching（靜態前置） | -90% | [Harnessing Claude's Intelligence](https://claude.com/blog/harnessing-claudes-intelligence) |
| MCP Tool Search 模式 | -85% token | [MCP for production systems](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) |
| Haiku + Opus Advisor | -85% 每任務成本，BrowseComp 19.7%→41.2% | [Advisor Strategy](https://claude.com/blog/the-advisor-strategy) |
| Sonnet + Opus Advisor | -11.9% 成本 +2.7% 效能 | [Advisor Strategy](https://claude.com/blog/the-advisor-strategy) |
| Skills（Analytics）| 準確率 21%→95% | [Self-service Analytics](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) |

**三層成本防線**：API 層（Advisor）+ Context 層（Caching）+ 工具層（Tool Search）

---

### 5. 平台化基礎設施成熟（2026 Q1–Q2）

**Managed Agents 演進路線（Apr–Jun 2026）**：

| 時間 | 功能 | 狀態 |
|------|------|------|
| Apr 8 | Managed Agents 上線 | Public Beta |
| May 6 | Dreaming（自主改進）+ Outcomes（成功標準）+ Multiagent Orchestration | Public Beta |
| May 11 | Claude Platform on AWS | GA |
| May 19 | Self-hosted Sandboxes + MCP Tunnels | Public Beta / Research Preview |
| Jun 9 | Scheduled Deployments + Vaults with Env Vars | Public Beta |
| Jun 18 | Enterprise Managed Auth for MCP | Team/Enterprise Beta |
| Jun 22 | Full Claude Desktop（chat/Cowork/Code 三合一）on AWS/GCP/Microsoft Foundry | GA |
| Jun 29 | Claude apps gateway（自架控制平面，統一 Bedrock/GCP 路由與治理）+ Claude in Microsoft Foundry | GA |
| Jul 2 | Admin 用量/成本可視化與 spend-threshold 警示 | GA |

**開發者體驗**：
- Agent View（May 11）：統一管理多並行 Session
- Agent Teams 簡化（Jun 15, v2.1.178）：移除 TeamCreate/TeamDelete，隱含 team
- Dynamic Workflows（May 28）：Claude 動態撰寫 JavaScript 協調腳本
- Loop 設計框架（Jun 30）：Turn-based / Goal-based / Time-based / Proactive 四類 agentic loop 官方選型指南

---

### 6. 新方向：模型世代與 AI 原生組織（May–Jun 2026）

**Fable 5（2026-06-09）**：
- 最強公開模型；ViBench / FrontierBench SOTA；Analytics benchmark 首次突破 90%
- 定價 $10/$50 per MTok；安全分類器自動路由至 Opus 4.8（< 5% sessions）
- Mythos 5：無分類器限制，Project Glasswing 合作夥伴限定

**AI 原生工程組織（2026-06-03）**：
- JIT Planning：原型驅動取代六個月 Roadmap
- Code Review 重新定義：從 style+logic → 法律/安全/產品感等高判斷領域
- 三指標：Onboarding ramp time / PR cycle time / Claude-assisted commits（≈100%）
- Anthropic Claude Code 團隊連續四個月無非 Claude 協助 commit

**AI 民主化信號**：
- 非工程師（業務、PM、律師、醫師）大量出現在案例中
- 非技術用戶六週上架 App Store；業務人員建立 20+ skills 的 Cowork 插件

**意涵**：「Agentic Coding 作為預設」的組織轉型已有實際案例，AI 民主化正從個人工具延伸至組織架構。

---

### 7. 2026 下半年的三個轉向（Jun–Jul 2026）

新收錄的 37 個條目裡有三件事不是既有主題的延伸，而是**方向反轉**（完整論述見 [docs/synthesis.md](./docs/synthesis.md) 主題七～九）：

| 轉向 | 錨點文章 | 核心事實 |
|------|---------|---------|
| **從堆規則到信任判斷** | [The new rules of context engineering for Claude 5](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)（07-24）| 刪掉 Claude Code system prompt 80%+，coding evals 無可量測退化；衝突指令會消耗推理預算 |
| **驗證觸發權回到 harness** | [Building verification loops with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)（07-22）| 官方推廣把驗證編碼成 Skill，同時 v2.1.215/218 關掉 `/verify`、`/code-review`、`/deep-research` 的自動觸發 |
| **扇出從越多越好到有界治理** | [CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)（07-17）| 職責不是零風險而是「讓代理風險可見且有界」；同期 subagent 上限、預設不巢狀、預算硬止血落地 |

同期的模型世代更新：**Sonnet 5**（06-30，新預設，1M ctx，$2/$10 促銷至 08-31）、**Opus 5**（07-24，1M ctx，$5/$25，Frontier-Bench 為 4.8 的 2 倍）、**MCP 2026-07-28 規格**（stateless core、Extensions 版本化、OAuth/OIDC 對齊、950+ servers）。

---

## Top 8 推薦閱讀（2026-08-05 更新）

| 優先級 | 文章 | 原因 |
|--------|------|------|
| ★★★ | [The new rules of context engineering for Claude 5](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)（Jul 24）| 本期最重要的一篇。system prompt −80% 無退化的實證，直接推翻「規則越多越安全」的既有直覺 |
| ★★★ | [Claude models explained](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)（Jul 24）| class × effort 二維選型框架；Advisor 實測 90% 效能 / 63% 成本；自建 eval > benchmark |
| ★★★ | [Building verification loops with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)（Jul 22）| 驗證迴圈的四種部署形態，配合自動觸發被關掉一起讀 |
| ★★★ | [Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)（Jun 18）| 七種機制官方選擇框架，是 Claude Code 自訂化的最終參考 |
| ★★★ | [A harness for every task: dynamic workflows](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)（Jun 2）| 六大模式 + 三大失敗模式防範，直接可應用於複雜任務架構設計 |
| ★★ | [How Anthropic runs large-scale code migrations](https://claude.com/blog/ai-code-migration)（Jul 16）| 六步驟遷移框架；「修復流程而非代碼」是 dynamic workflow 最成熟的應用形態 |
| ★★ | [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)（Jul 17）| 四個評估問題 + 七項控制；與 [How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude) 的「環境層優先於模型層」同源 |
| ★★ | [Self-service data analytics](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)（Jun 3）| 21%→95% 準確率的四層架構，含 Skills 配對和 adversarial review 完整設計 |

---

## 收錄狀態追蹤

| 更新日期 | 收錄篇數 | 主要新增主題 |
|---------|---------|------------|
| 2026-04-23（初次）| ~50 | Claude Code 基礎、Agent 架構、Skills 生態 |
| 2026-05-16 | ~75 | Enterprise 垂直化、Managed Agents、Platform on AWS、Microsoft 365 |
| 2026-06-05 | ~82 | Dynamic Workflows、Security 深度文章、Skills 九大類別、AI 原生組織 |
| 2026-06-20 | ~109 | Fable 5、Artifacts、Workload Identity Federation、Enterprise Managed Auth、Seoul Office、Steering Claude Code 七機制指南 |
| 2026-07-06 | ~117 | Claude Fable unknowns 協作指南、Agentic Loop 四類型官方框架、Claude Tag Agent Identity 存取模型、Multiplayer 人機協作團隊心法、Claude Desktop/apps gateway/Microsoft Foundry GA 雲端部署擴張、Admin 用量與成本可視化控管 |
| **2026-08-05** | **153 條目 / ~138 去重** | **Claude 5 世代 context engineering 新規則（system prompt −80%）、官方模型選型框架、驗證迴圈 Skill 化、Sonnet 5 與 Opus 5 發布、MCP 2026-07-28 規格、大規模程式碼遷移六步驟、AI 原生 SDLC 安全、CISO agentic AI 指南、Datadog 確定性 kernel、Outtake 自主 cyber investigator、Working at the frontier 系列（Rakuten / Cursor / Base44 / Hebbia / Cognition / Thomson Reuters）** |

---

## 技術限制說明

claude.com/blog 共有多頁文章，本次以 WebFetch SSR 方式收錄：
- Claude Code: 45 條目
- Agents: 25 條目
- Enterprise AI: 45 條目
- Announcements: 38 條目

其中部分文章同時出現在多個分類（見上方「文章分佈」的跨分類清單），去重後約 138 篇。

若需完整歷史文章（2025 年以前），需使用 headless browser 或 Playwright：

```python
playwright install chromium
playwright codegen claude.com/blog
```

---

*生成工具：`/autoresearch:learn` + 手動補充 · 初次 2026-04-23，最後更新 2026-08-05*  
*最後同步：`researcher` sub-agent + 手動更新 · 2026-07-06*
