---
title: Announcements — claude.com/blog
type: index
---

# Announcements — claude.com/blog

> 收錄自 [claude.com/blog/category/announcements](https://claude.com/blog/category/announcements) · 19 篇文章 · 2026-02-17 ~ 2026-05-19
> 最後更新：2026-05-19

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
