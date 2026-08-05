---
title: "Announcements — claude.com/blog"
type: index
---

# Announcements — claude.com/blog

> 收錄自 [claude.com/blog/category/announcements](https://claude.com/blog/category/announcements) · 37 篇文章 · 2026-02-17 ~ 2026-07-28
> 最後更新：2026-08-04

---

## Bringing MCP 2026-07-28 to Claude

**Date:** 2026-07-28 | **URL:** https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

### Summary
MCP 第五個規格版本發布：核心改為 stateless，可部署於 serverless 與 edge；互動 UI 與長時工作以版本化 extension 標準化；授權對齊 OAuth 2.0 與 OIDC。Claude 產品線同步支援，可用 MCP server 超過 950 個。

### Key Points
- Stateless core：從雙向有狀態協定改為 request/response，server 部署與擴展大幅簡化
- Extensions 框架：MCP Apps 與 Tasks 以版本化 extension 出貨，不必動核心協定
- 授權對齊生產級 OAuth 2.0 / OIDC，可直接接 Entra、Okta，不需 workaround
- MCP Apps 讓 server 在對話中直接算繪互動元件，免切分頁
- 企業託管：管理員經 IdP 佈建 connector，群組繼承存取權，終端使用者零設定
- 已發布 connector 取得 dashboard，可看效能、採用、錯誤與使用量

---

## Introducing Claude Opus 5

**Date:** 2026-07-24 | **URL:** https://www.anthropic.com/news/claude-opus-5

### Summary
Anthropic 發布 Claude Opus 5（`claude-opus-5`），多數任務逼近 Fable 5 而價格只有一半，且與 Opus 4.8 同價（$5/$25）。成為 Claude Max 的預設模型與 Claude Pro 可用的最強模型；是 Claude 5 世代不到兩個月內的第四個模型。

### Key Points
- 定價維持 $5/MTok 輸入、$25/MTok 輸出；fast mode 約 2.5× 速度、2× 價格
- 1M context window（Claude Code v2.1.219 公告）；effort 可調 low/medium/high
- Frontier-Bench v0.1 為 Opus 4.8 的 2 倍；CursorBench 3.2 與 Fable 5 差距 < 0.5% 而成本減半
- ARC-AGI 3 為次佳模型 3 倍；OSWorld 2.0 優於 Fable 5 而成本為其 1/3
- 能力重點：更常自我驗證與迭代修正、agentic 推理提升、視覺輸出與科學研究（有機化學/蛋白質）改善
- 安全：近期模型中欺騙性行為比率最低；攻擊性 cyber 能力仍低於 Mythos 5
- 供應：Claude API / Code / Cowork / Platform / claude.ai，AWS、Google Cloud、Microsoft 同步

---

## Think through hard problems in voice mode

**Date:** 2026-07-23 | **URL:** https://claude.com/blog/think-through-hard-problems-in-voice-mode

### Summary
語音模式開放使用 Opus 與 Sonnet（原本僅 Haiku），並支援連接工具執行動作，語言擴充至 11 種。

### Key Points
- 語音對話可跑 Opus 與 Sonnet，適合深入推敲複雜問題
- 可連接 Google Calendar、Gmail、Slack、Canva 等服務，動作前需授權
- 11 種語言，全方案可用，對話中可直接用口說切換
- Free 方案為 Haiku + 一個連接工具；付費方案解鎖更多模型與全部工具；語音對話計入一般使用額度

---

## Bringing Claude Code and Claude Cowork to government

**Date:** 2026-07-07 | **URL:** https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government

### Summary
Anthropic 推出 Claude Code 與 Claude Cowork 桌面應用在聯邦政府環境的公測版，運行於 FedRAMP High 授權環境，讓公部門團隊能建構軟體系統與處理文件工作，同時提供強化治理功能。

### Key Points
- FedRAMP High 授權環境提供，對話歷史存放於機構管理設備
- 適應撥款預算的計費選項：標準座位或自訂支出/模型限制層級
- 部門管理員可將預付用量分配至子機構，SCIM 群組映射設定費率限制與允許模型
- 所有管理操作記錄於防篡改雜湊鏈審計日誌，敏感操作需雙人核准
- 發布 FedRAMP 安全配置指南與滲透測試摘要供安全團隊評估
- 新客戶可於 claude.com/solutions/government 申請存取權限

---

## Claude Cowork is coming to mobile and web

**Date:** 2026-07-07 | **URL:** https://claude.com/blog/cowork-web-mobile

### Summary
Claude Cowork 推出網頁版與行動版，使用者可在任何裝置上存取工作進度；任務委派給 Claude 後在背景持續進行，裝置離線也能繼續執行。超過 90% 的 Cowork 使用並非軟體開發，而是業務營運與內容創作等日常知識工作。

### Key Points
- 跨裝置工作連續性：桌機開始任務、手機查看進度、任何地點取得成果
- 背景工作執行：可排定任務於特定時間運行（如早上 6 點準備客戶簡報），完成後留待審核
- 人工決策控制：Claude 遇到需人工判斷的決定會提醒使用者，確保最終輸出經核准
- 多平台支援：網頁版、行動版（iOS/Android）與桌面應用整合，共享專案與工件
- 使用案例廣泛：約 50% 使用來自業務營運與內容創作，包括支出對帳、合約追蹤、客戶簡報準備
- 推廣期（至 8/5）提供雙倍 Cowork 使用額度

---

## Giving admins more visibility and control over Claude spend

**Date:** 2026-07-02 | **URL:** https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend

### Summary
Anthropic 為企業版推出強化的管理分析與成本控管工具，因應 agentic workflow 使用型態日趨複雜，讓管理員可依團隊/個人追蹤用量與成本。

### Key Points
- Claude Code 專屬分頁顯示活躍開發者數、session 數與生產力估計指標
- Analytics Chat 支援自然語言查詢（如「哪些團隊本月用量翻倍？」）；Analytics API 可整合 Datadog、CloudZero 等既有工具
- Model defaults/entitlements 可設定預設啟動模型，避免不必要的高階模型用量
- 用量門檻警示：75%／90% 觸發管理員預警，75%／95% 觸發使用者內建通知並可直接聯繫管理員
- Admin API 支援大規模自動化 usage 監控與加量審核流程
- 追蹤指標涵蓋 Artifacts 建立數、檔案編輯數、skills/connector 使用率，並依團隊/使用者/產品/模型拆分成本

---

## Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

**Date:** 2026-06-29 | **URL:** https://claude.com/blog/introducing-the-claude-apps-gateway

### Summary
Anthropic 推出 Claude apps gateway，一個自架控制平面，讓企業能以統一治理機制在 Amazon Bedrock 與 Google Cloud 上安全執行 Claude Code，取代過去逐開發者配置雲端憑證的作法。

### Key Points
- 身份管理：作為 OpenID Connect relying party，支援 Google Workspace、Microsoft Entra ID、Okta 等標準 OIDC 供應商
- 集中定義並強制套用 managed settings 至所有 client；透過 OTLP 上報用量遙測至自架 collector
- 路由層可將推論導向 Claude API、Amazon Bedrock 或 Google Cloud，並支援 failover
- 支援組織/群組/使用者層級的日/週/月用量上限控管
- 技術架構：單一無狀態容器執行於 Linux，搭配 PostgreSQL，隨既有 Claude binary 一併發布；透過 `gateway.yaml` 設定 OIDC 與上游憑證、`managed-settings.json` 控制 client 連線
- 除非設定使用 Claude API，否則 gateway 不會將推論流量或用量資料傳回 Anthropic

---

## Claude in Microsoft Foundry is now generally available

**Date:** 2026-06-29 | **URL:** https://claude.com/blog/claude-in-microsoft-foundry

### Summary
Claude 模型在 Microsoft Foundry（Azure 託管）正式 GA，企業可透過既有 Azure 基礎設施運行 Claude，整合身份驗證、計費與治理機制。

### Key Points
- 部署選項：Azure 託管（提供美國資料落地選項）或 Anthropic 基礎設施託管（初期 API 功能較完整）
- 上線模型：Claude Opus 4.8、Claude Haiku 4.5，支援 Messages API、prompt caching、extended thinking
- 整合 Azure 身份、網路與治理控制；符合資格的 Microsoft Enterprise Agreement 客戶可將 Claude 用量計入 Azure 承諾額度
- 客戶案例：NVIDIA 用自主 agent 處理 GB300 GPU 技術工作；Bolt 達到 Fortune 500 等級可靠度；Everstar 將核能安全分析從 200 人天壓縮至 1 天；Momentic 用於自動化測試，每分鐘處理數百萬 token
- Anthropic 負責該 Azure 託管部署的推論運算與資料處理者角色

---

## Claude Code now supports artifacts

**Date:** 2026-06-18 | **URL:** https://claude.com/blog/artifacts-in-claude-code

### Summary
Claude Code 新增 Artifacts 功能，可將工作 session 轉換為互動式、可分享的網頁，整合 codebase、工具執行結果與對話歷史，供團隊成員即時查看。頁面隨 Claude Code 變更自動更新，支援版本歷史與還原。目前限 Team/Enterprise beta。

### Key Points
- 頁面隨 Claude Code 每次變更自動同步，支援版本歷史回溯與還原
- 預設私有，僅限組織內認證成員存取；管理員可透過 org-level 開關和角色權限控管
- 適用場景：PR walkthrough（Reviewer 看到完整思路）、事故調查、安全稽核、基礎架構地圖、前端 UX 設計、週報摘要
- 詳細解析見 [best-practices/39-artifacts.md](../../best-practices/39-artifacts.md)

---

## Claude Design now stays on brand for daily work

**Date:** 2026-06-17 | **URL:** https://claude.com/blog/claude-design-stays-on-brand-for-daily-work

### Summary
Claude Design 新增設計系統整合、`/design-sync` 雙向同步 Claude Code，並大幅重設計編輯器與效能改善，連接 Adobe、Canva、Figma 等多個設計平台。

### Key Points
- 可從 GitHub repo、設計檔案或原始上傳匯入設計系統，自動驗證輸出是否符合品牌規範
- `/design-sync` 指令將設計系統拉進 Claude Code；反向亦可從 Code 端以 `/design` 指令啟動
- 使用量限制與 chat 共享以提升容量；每輪平均 token 用量下降、錯誤率大幅降低
- 連接 Adobe、Canva、Figma 等多個設計平台

---

## Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem

**Date:** 2026-06-17 | **URL:** https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem

### Summary
Anthropic 在首爾設立辦公室，與韓國科技部簽署 AI 安全 MOU，多家韓國大型企業已全面部署 Claude Code。

### Key Points
- **NAVER**：全工程組織導入 Claude Code
- **Nexon**：工程師用於遊戲開發
- **LG CNS**：推廣至整個 LG 集團數千名員工
- **Samsung SDS**：部署至三星電子員工
- 與 NAIRL 國家 AI 研究所合作，為 60 位研究人員提供 Claude 存取
- 與科技部 MOU 聚焦韓語 AI 安全評估與 AI 網路威脅應對

---

## Centrally manage authorization for MCP connectors

**Date:** 2026-06-18 | **URL:** https://claude.com/blog/enterprise-managed-auth

### Summary
企業版 MCP connector 集中授權管理（Team/Enterprise Beta），透過 Okta 等 IdP 統一配置，消除逐個 OAuth 審批流程，員工登入即自動取得 connector 存取權。

### Key Points
- Zero-touch 設定：依 IdP 群組成員資格自動配置，跨 Claude chat、Claude Code、Cowork 生效
- 支援 Asana、Atlassian、Canva、Figma、Linear、Supabase 作為 MCP provider；Okta 負責身份管理
- 可強制 IdP-only 連線，支援 token 生命週期控制，加速撤銷存取
- 與 Workload Identity Federation 互補：WIF 適合 workload-to-API 身份；IdP 管控適合員工 connector 授權

---

## Claude Fable 5 and Claude Mythos 5

**Date:** 2026-06-09 | **URL:** https://www.anthropic.com/news/claude-fable-5-mythos-5

### Summary
Anthropic 發布 Fable 5（Mythos-class 公開版）和 Mythos 5（Project Glasswing 受邀版）。Fable 5 是迄今公開可用能力最強的模型，在幾乎所有評測上達 SOTA。訂閱方案用戶 6/9–6/22 免費試用，6/23 起需 Usage Credits。

### Key Points
- Context 1M token；輸出上限 128k；定價 $10/$50 per MTok
- ViBench（vibe-coding）和 FrontierBench（Cognition coding eval）最高分
- Analytics benchmark 首次突破 90%（比 Opus 4.8 +10 分）
- 安全分類器：cyber/bio-chem/distillation 請求自動路由至 Opus 4.8（< 5% sessions）
- Mythos 5：無分類器限制，僅限 Project Glasswing 合作夥伴
- 平台支援：Claude API / Bedrock / Vertex AI / Foundry / Claude Platform on AWS

---

## New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

**Date:** 2026-06-09 | **URL:** https://claude.com/blog/whats-new-in-claude-managed-agents

### Summary
Managed Agents 新增兩項 Public Beta 功能：Scheduled Deployments（cron 觸發自動 session）和 Vaults with Environment Variables（API Key 在網路邊界安全替換，Agent 永遠看不到真實 Key）。

### Key Points
- 排程部署：設定 cron schedule，每次觸發自動啟動新 session，無需自建排程基礎設施
- Vault 金鑰管理：安全儲存 API Key（GITHUB_TOKEN 等 env vars），只在允許的網域邊界替換，非沙盒內替換
- 典型場景：夜間資料同步、每週合規掃描、每日 digest、CI/CD 自動化
- 與 MCP OAuth 互補：Vault 適合靜態 API Key；OAuth 適合 interactive 授權流程

---

## Best practices for getting started with Claude Cowork

**Date:** 2026-06-03 | **URL:** https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork

### Summary
Claude Cowork 使用最佳實踐官方指南。Cowork 適合委派多步驟任務（有檔案輸出），與 Chat（快速問答）和 Code（開發者工具）互補。

### Key Points
- 最佳任務特徵：多來源輸入、有檔案輸出、重複性、有明確品質標準、有無聊的中間步驟
- 優異輸出關鍵：提供豐富 context（非只靠 Prompt），連接應用程式
- 五大最佳實踐：從已熟悉任務開始評估輸出品質、讓 Claude 先問澄清問題、提供 context 優先於撰寫 Prompt、定期任務設排程、Chat 用探索思考/Cowork 用交辦工作

---

## Introducing dynamic workflows in Claude Code（2026-05-28）

> 完整摘要見 [claude-code/index.md](../claude-code/index.md)

### Summary
Dynamic Workflows Research Preview：Claude 動態撰寫協調腳本，協調數十到數百個並行 subagent，用於大型遷移、全 codebase audit 等複雜任務。

---

## Claude now works with more security and compliance tools

**Date:** 2026-05-21 | **URL:** https://claude.com/blog/compliance-api-security-partners

### Summary
Claude Compliance API 新增 28 個安全與合規平台整合，讓 IT 和安全團隊能像管理其他企業應用一樣治理 Claude。整合類別涵蓋 DLP、SASE、SIEM、身份管理、eDiscovery、AI 安全監控。

### Key Points
- 28 個新整合：Cloudflare、CrowdStrike、Datadog、Microsoft Purview、Okta、Palo Alto Networks、Zscaler 等
- Compliance API 兩大能力：Claude Enterprise 對話內容存取 + Enterprise/Platform 活動事件
- 透過現有安全儀表板和工作流啟用覆蓋，無需新的管理介面

---

## New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

**Date:** 2026-05-19 | **URL:** https://claude.com/blog/claude-managed-agents-updates

### Summary
Claude Managed Agents 新增自托管 Sandbox 和 MCP Tunnel 支援，讓 Agent 在企業自控基礎架構內執行工具，同時維持安全與合規。組織可選用 Cloudflare、Daytona、Modal、Vercel 等托管供應商，MCP Tunnel 則允許 Agent 安全存取私有網路服務而無需公開暴露。

### Key Points
- 工具執行移至客戶自管環境，Anthropic 基礎架構只負責 Orchestration，敏感檔案與 Repo 留在企業邊界內
- 支援 Sandbox 供應商：Cloudflare（microVM + zero-trust secrets）、Daytona（長時 stateful）、Modal（AI 優化 + GPU）、Vercel（毫秒啟動 + VPC peering）
- MCP Tunnel 透過輕量 Gateway（僅需 outbound 連線 + 端對端加密）存取內部 DB、API、服務
- 組織可自控資源配置、Runtime Image 和運算容量
- 自托管 Sandbox 公開 Beta；MCP Tunnel 為 Research Preview

---

## Claude for the legal industry

**Date:** 2026-05-12 | **URL:** https://claude.com/blog/claude-for-the-legal-industry

### Summary
針對法律專業人士的 20+ MCP Connector 和 12 個實務領域 Plugin 正式發布。整合 iManage、Thomson Reuters、Harvey 等主流法律平台，並深度嵌入 Microsoft Word、Outlook、Excel、PowerPoint。

### Key Points
- 20+ MCP Connector：合約（Definely、DocuSign、Ironclad）、文件管理（iManage、NetDocuments）、電子取證（Everlaw、Relativity）、法律研究（Thomson Reuters、Midpage）
- 12 個實務領域 Plugin：Commercial、Corporate、Employment、Privacy、IP、Litigation 等
- Microsoft Word 整合：起草和紅線標記；Outlook：來件分類；Cowork：多文件事務
- 法律援助診所和非營利組織可透過 Claude for Nonprofits 取得折扣定價

---

## Agent view in Claude Code

**Date:** 2026-05-11 | **URL:** https://claude.com/blog/agent-view-in-claude-code

### Summary
Claude Code 推出 Agent View（Research Preview），統一管理多個並行 Claude Code Session 的介面。可查看所有 Agent 狀態、內嵌互動，以及背景執行管理。

### Key Points
- 按左箭頭或執行 `claude agents` 進入 Agent View
- 顯示：Session 狀態、待輸入需求、最後回應、互動時間戳
- 內嵌互動：預覽最近幾輪並直接回應，無需進入完整 Session
- 背景操作：`/bg` 命令背景化 Session；`claude --bg [task]` 直接後台啟動
- 適用 Pro、Max、Team、Enterprise 及 Claude API，為 Research Preview

---

## Introducing the Claude Platform on AWS

**Date:** 2026-05-11 | **URL:** https://claude.com/blog/claude-platform-on-aws

### Summary
Claude Platform on AWS 正式開放普遍可用（GA）。AWS 客戶可透過 AWS 認證、帳單和承諾整合使用全套 Claude Platform 功能，與 Amazon Bedrock 形成互補選擇。

### Key Points
- 包含：Managed Agents（beta）、Advisor（beta）、Web search/fetch、Code execution、Files API、Skills、MCP connector、Prompt caching
- 與 Amazon Bedrock 差異：Claude Platform 由 Anthropic 運營（資料在 AWS 邊界外）；Bedrock 由 AWS 處理（嚴格區域駐留需求）
- 支援 Opus 4.7、Sonnet 4.6、Haiku 4.5；新版本同步上線
- 適用大多數 AWS 商業區域

---

## Collaborate with Claude across Excel, PowerPoint, Word and Outlook

**Date:** 2026-05-07 | **URL:** https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook

### Summary
Claude Microsoft 365 Add-in 正式 GA（Excel、PowerPoint、Word），Outlook 進入 Public Beta。跨應用保持完整對話 Context，調整 Excel 假設自動更新 PowerPoint 圖表和 Word 數字。

### Key Points
- 跨應用 Context 連續性：在四個 App 間維持完整對話歷史，不需重複背景
- Outlook：郵件分類（依回應優先級）、起草回覆（自動填充收件人/主旨/內容）、行事曆邀請驗證
- 企業部署：透過 Microsoft AppSource 管理員中心；OpenTelemetry 整合（Splunk 等）
- Analytics API：提供每用戶、每 App 活動追蹤
- 使用中：ServiceNow、Citadel、Bain & Company、Deloitte

---

## New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

**Date:** 2026-05-06 | **URL:** https://claude.com/blog/new-in-claude-managed-agents

### Summary
Managed Agents 三大新功能：Dreaming（Agent 自主改進）、Outcomes（成功標準定義 + 自校正）、Multiagent Orchestration（主 Agent 委派專業 Agent 並行）。

### Key Points
- Dreaming（Research Preview）：Agent 自動審閱過去 session 和記憶，提取模式並改進；Harvey 跨 session 學習達 6x 更高完成率
- Outcomes（Public Beta）：開發者定義成功評分標準，grader 自動評估輸出；文件生成 +8.4%、簡報 +10.1%
- Multiagent Orchestration（Public Beta）：Lead Agent 委派專業 Agent 並行，共享 filesystem，Claude Console 顯示完整歸因
- Netflix：分析數百次構建日誌找出反覆出現的問題

---

## Higher Usage Limits for Claude and a Compute Deal with SpaceX

**Date:** 2026-05-06 | **URL:** https://www.anthropic.com/news/higher-limits-spacex

### Summary
Anthropic 宣布與 SpaceX 合作取得 300+ MW 算力（22 萬+ NVIDIA GPU），同步提升 Claude Code 速率限制與 Claude Opus API 配額，應對企業客戶合規數據駐留需求與國際擴展需求。

### Key Points
- 300+ MW 計算能力：22 萬+ NVIDIA GPU（SpaceX 基礎設施）
- Claude Code 速率限制大幅提升，Opus API 配額同步擴增
- 企業合規需求：資料駐留與國際部署支援
- 應對高成長需求，預備規模化交付

---

## Claude for Creative Work

**Date:** 2026-04-28 | **URL:** https://www.anthropic.com/news/claude-for-creative-work

### Summary
Anthropic 發布與創意軟體工具的整合連接器，創意專業人士可利用 AI 學習複雜軟體、自動化重複任務、跨工具鏈接並加速創意構思。

### Key Points
- 新整合：Ableton、Adobe Creative Cloud、Autodesk Fusion、Blender、SketchUp
- 用例：學習複雜軟體操作、自動化重複任務、跨工具鏈接
- 對象：音樂製作、影像設計、3D 建模、工業設計等創意工作者
- 延伸 Connector 生態（現已超過 200 項整合）

---

## Anthropic Names Theo Hourmouzis GM of Australia & New Zealand

**Date:** 2026-04-27 | **URL:** https://www.anthropic.com/news/theo-hourmouzis-general-manager-australia-new-zealand

### Summary
Anthropic 任命 Theo Hourmouzis（前 Snowflake 高管，20+ 年技術領導經驗）為澳洲及紐西蘭總經理，正式開設雪梨辦公室，深化與澳洲企業及學術界合作。

### Key Points
- 任命：Theo Hourmouzis，前 Snowflake 高管，20+ 年技術領導資歷
- 雪梨辦公室正式開幕（Anthropic 亞太區擴張）
- 合作夥伴：Commonwealth Bank、Canva、Xero
- 與澳洲大學建立 AI 研究協作

---

## An Update on Our Election Safeguards

**Date:** 2026-04-24 | **URL:** https://www.anthropic.com/news/election-safeguards-update

### Summary
Anthropic 更新選舉資訊保障措施，Claude 政治觀點平衡性評估達 95-96%，有害/合法請求識別準確率達 99.8-100%，並持續建立 600 條選舉提示測試集。

### Key Points
- 政治平衡性：95-96% 分數（第三方評估）
- Claude Opus 4.7 有害請求識別：100% 準確率
- Claude Sonnet 合法請求識別：99.8% 準確率
- 600 條選舉提示測試集（自動惡意檢測）
- 選舉週期後總結報告承諾

---

## Built-in Memory for Claude Managed Agents

**Date:** 2026-04-23 | **URL:** https://claude.com/blog/claude-managed-agents-memory

### Summary
Managed Agents 推出公開測試版記憶功能，跨 session 持久化學習。採用檔案系統架構直接掛載，原生整合 bash / code execution。

### Key Points
- 跨 session 持久化：Agent 累積知識無需手動更新 prompt
- 企業控制：權限分層、完整審計紀錄、版本回滾、內容編輯、跨 Agent 共享記憶庫
- API 管理：可匯出記憶、程式化控制、Claude Console 事件追蹤
- 驗證結果：Rakuten 97% 首次準確率↑、27% 成本↓；Wisedocs 驗證精度↑30%
- 公開 beta 即日可用於所有 Managed Agents 用戶

---

## New Connectors in Claude for Everyday Life

**Date:** 2026-04-23 | **URL:** https://claude.com/blog/connectors-for-everyday-life

### Summary
Claude 新增 15 個個人生活應用連接器（餐飲、旅遊、娛樂），整體 Connector 目錄超過 200 項整合。

### Key Points
- 新增連接器：Booking.com、Instacart、Spotify、Uber Eats、Resy、StubHub、Audible 等 15 個
- 動態建議：根據任務自動推薦適切 Connector
- 隱私保護：資料不用於訓練、應用間隔離、用戶購買前必須核准
- 無廣告政策；全訂閱方案可用，行動版本 beta

---

## Redesigning Claude Code on desktop for parallel agents

**Date:** 2026-04-14 | **URL:** https://claude.com/blog/claude-code-desktop-redesign

> 完整摘要見 [claude-code/index.md](../claude-code/index.md)

### Summary
桌面 App 全面重新設計：多 Agent 並行、統一 sidebar、內建終端機和 diff 檢視器。

---

## Introducing routines in Claude Code

**Date:** 2026-04-14 | **URL:** https://claude.com/blog/introducing-routines-in-claude-code

### Summary
Routines（Research Preview）：三種自動化執行模式（排程/API/GitHub webhook）。處理重複開發任務，無需手動基礎設施。

### Key Points
- 三種執行模式：**Scheduled**（hourly/nightly/weekly）、**API 觸發**（HTTP endpoint）、**Webhook**（GitHub repo 事件）
- 使用限額：Pro 每日 5 次、Max 每日 15 次、Team/Enterprise 每日 25 次
- 可存取使用者的 repository 和 connector，無需額外 cron job

---

## The advisor strategy: Give agents an intelligence boost

**Date:** 2026-04-09 | **URL:** https://claude.com/blog/the-advisor-strategy

### Summary
Advisor Tool：Opus 作為智慧顧問，Sonnet/Haiku 作為執行者。Haiku + Opus Advisor 可達 BrowseComp 19.7%→41.2%，成本降 85%。一行 API 實作。

### Key Points
- Sonnet + Opus Advisor：SWE-bench Multilingual 提升 2.7 個百分點，成本降 11.9%
- Haiku + Opus Advisor：BrowseComp 從 19.7% 翻倍至 41.2%，成本降 85%
- Advisor tool 作為伺服器端元件整合在單一 API 請求中，一行實作
- Advisor 每次諮詢通常只產生 400-700 個 text token

---

## Making Claude Cowork ready for enterprise

**Date:** 2026-04-09 | **URL:** https://claude.com/blog/cowork-for-enterprise

### Summary
企業版 Cowork：RBAC、每團隊預算限制、OpenTelemetry（Splunk 整合）、Zoom MCP connector。

### Key Points
- Organization Controls：管理員管理使用者群組、指派自訂角色
- 每團隊預算限制提供可預測的成本監督
- OpenTelemetry 整合支援 Splunk 等 SIEM 管道
- 新增 Zoom MCP connector；每工具控制讓管理員限制特定操作

---

## Claude Managed Agents: get to production 10x faster

**Date:** 2026-04-08 | **URL:** https://claude.com/blog/claude-managed-agents

### Summary
雲端託管 Agent API：$0.08/session-hour，10x 更快部署，Public Beta 上線。處理基礎設施複雜性，讓開發者專注於 Agent 邏輯。

### Key Points
- 生產就緒功能：長時間 session、多 Agent 協調、範疇化權限、內建執行追蹤
- 內部測試：結構化檔案生成任務成功率提升高達 10 個百分點
- 消費型定價：標準 Claude token 費率 + 每 session-hour $0.08

---

## Audit Claude Platform activity with the Compliance API

**Date:** 2026-03-30 | **URL:** https://claude.com/blog/claude-platform-compliance-api

### Summary
Compliance API 讓組織管理員可程序化存取 Claude Platform 部署的審計日誌。追蹤安全相關事件，包括管理操作和資源修改，幫助合規團隊監控使用者活動。

### Key Points
- 追蹤兩類活動：管理/系統活動（工作區變更、API 金鑰建立）和資源活動（檔案操作、Skill 管理）
- 不記錄推理日誌：專注組織和資源級事件，非直接模型互動
- 企業整合：跨 Claude API 和 Enterprise 部署合併活動 feed
- 限制：日誌從 API 啟用後開始，無法取得歷史數據

---

## Put Claude to work on your computer

**Date:** 2026-03-23 | **URL:** https://claude.com/blog/dispatch-and-computer-use

### Summary
Claude 在 Cowork 和 Claude Code 中具備電腦使用能力，可控制滑鼠、鍵盤和瀏覽器。Dispatch 讓用戶從手機指派任務，在桌面完成。

### Key Points
- Claude 優先使用直接工具整合，在沒有 connector 時可透過點擊操控螢幕
- 包含提示注入偵測和可疑活動掃描安全措施
- Dispatch：跨設備連續對話，從手機指派任務，桌面完成
- 適用 Pro 和 Max 訂閱者（macOS 和 Windows），Research Preview

---

## Claude now creates interactive charts, diagrams and visualizations

**Date:** 2026-03-12 | **URL:** https://claude.com/blog/claude-builds-visuals

### Summary
Claude 現在可以在對話中直接生成互動圖表、圖解和視覺化，無需程式碼。這些內嵌視覺效果作為理解的臨時輔助工具，適用於所有訂閱方案。

### Key Points
- 對話中建立：視覺效果內嵌顯示，隨對話演進
- 用戶引導或自動：Claude 判斷何時視覺效果有助於解釋
- 迭代優化：用戶可在對話中請求調整和深入探索
- 適用於所有訂閱層級

---

## Increase web search accuracy and efficiency with dynamic filtering

**Date:** 2026-02-17 | **URL:** https://claude.com/blog/improved-web-search-with-dynamic-filtering

### Summary
更新的 web search 和 web fetch 工具讓 Claude 可自動撰寫並執行程式碼來過濾搜尋結果，提升準確率 11%，同時降低 token 使用量 24%。

### Key Points
- 動態過濾技術：Claude 透過程式碼執行過濾不相關的搜尋結果
- 基準效能：Sonnet 4.6 BrowseComp 從 33.3% 提升至 46.6%；F1 分數從 52.6% 提升至 59.4%
- Sonnet 4.6 和 Opus 4.6 預設自動啟用（使用新 web search/fetch 工具）
- 相關工具：程式碼執行、記憶、程序化工具呼叫、tool search 正式開放
