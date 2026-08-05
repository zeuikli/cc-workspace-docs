---
title: "Enterprise AI — claude.com/blog"
type: index
---

# Enterprise AI — claude.com/blog

> 收錄自 [claude.com/blog/category/enterprise-ai](https://claude.com/blog/category/enterprise-ai) · 45 篇文章 · 2025-11-17 ~ 2026-07-24
> 最後更新：2026-08-04

> 注：2026-04-09 起的產品公告（Managed Agents、Advisor Strategy、Cowork Enterprise）收錄於 [announcements/index.md](../announcements/index.md)，本分類專注於企業採用案例與功能深度報導。

---

## How the product designer who built Claude Design uses it to explore ideas before building them

**Date:** 2026-07-24 | **URL:** https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them

### Summary
打造 Claude Design 的產品設計師說明其用法：把 HTML 當成豐富的互動視覺媒材，讓設計師不靠傳統設計軟體就能產出互動原型、簡報、landing page 與動畫。定位在早期發想與溝通，與負責生產軟體的 Claude Code 分工。

### Key Points
- 以 HTML 為輸出媒材，產出可互動、可分享的視覺設計
- 可上傳品牌素材、字體、色彩與設計規範，讓產出自動符合品牌，不靠人工自律
- 協作式迭代：一次要十個版本再 remix，快速探索變體而非等一個完成品
- 明確不用於生產工程——那是 Claude Code 的範圍
- 可接 GitHub repo、web search 與 MCP 取得既有元件與畫面，讓設計從真實專案脈絡長出來

---

## Claude models explained: choosing the best model for your use case

**Date:** 2026-07-24 | **URL:** https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case

### Summary
官方選型指南：從一般可用的最強模型起步再依延遲與成本往下調；依據是任務難度與單位經濟，不是產業別。

### Key Points
- 四 class 定位：Mythos/Fable、Opus、Sonnet、Haiku
- Effort 等級讓「高 class 低 effort」在 per-task 成本上可能勝過低 class 模型
- Advisor 策略：Sonnet + Fable 監督 = Fable-only 效能 90%、成本 63%
- 高量任務在品質達標時通常偏向低 class 模型
- 企業實務：以策展問題集與團隊自訂成功標準做自建 eval，勝過看公開 benchmark

---

## Four role-based certifications for the people who put Claude to work for customers

**Date:** 2026-07-23 | **URL:** https://claude.com/blog/four-role-based-claude-certifications

### Summary
Anthropic 新增三張角色型認證，與既有的 Claude Certified Architect: Foundations 合為四張，供企業驗證合作夥伴的實作能力。自三月以來已有 1,300+ 組織、36,000 名顧問取得認證。

### Key Points
- 四張認證：Associate: Foundations（日常實務）、Developer: Foundations（API 與 agent 開發）、Architect: Professional（進階企業整合）、Architect: Foundations（agent 系統設計）
- 對象從非技術顧問與專案負責人，到建應用的工程師與設計系統的架構師
- 全部為監考、身分驗證的考試，由 Pearson Professional Assessments 施測，通過者取得 Credly 數位徽章
- 大型顧問公司大規模投入：Accenture 5 萬人、PwC 3 萬人、Capgemini 2 萬人；認證影響 Claude Partner Network 分級

---

## How Anthropic secures its AI-native software development lifecycle

**Date:** 2026-07-21 | **URL:** https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle

### Summary
Anthropic 副 CISO 說明 AI 撰寫 80% 合併程式碼下的 SDLC 安全設計：審查左移、硬性存取邊界、自動與人工審查分工，並把 agent 行為視為新型內部威脅監控。

### Key Points
- 工程師每季出貨量為 2021–2025 的 8 倍；超過一半合併由 Claude Tag 處理，人類定意圖與最終核可
- 規劃階段自動對照 MITRE ATT&CK 並接組織知識庫，低風險上線可自助核准
- CLAUDE.md 把安全實踐編碼進生成過程，安全 review plugin 即時給建議
- 多個窄焦點 agent 各持獨立 context 與偏誤審同一 PR，加 SAST 與對自動核可的人工抽樣
- 圍堵：allowlist 出口的遠端 coding VM、agent 權限分離、獨立系統帳號
- 治理：agent 動作全進 SIEM；漏洞發現自動回寫 CLAUDE.md 防止再生成

---

## How Datadog built a "universal machine tool" for Claude Code

**Date:** 2026-07-21 | **URL:** https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code

### Summary
Datadog 的 Temper 讓 agent 產出精確規格而非應用程式碼，由確定性 kernel 以四層分析驗證後執行，補上「agent 生成」與「可安全部署」之間的落差。

### Key Points
- 任務愈複雜，工程師被迫升級成管理者——要管 agent 的可見資訊、工具、成功標準與失敗偵測
- 前三代嘗試（Courier / BitsEvolve / Helix）之後才定位出真正瓶頸
- Kernel 用符號推理、窮舉狀態探索、確定性模擬與 property testing 驗證，小規格一秒內完成
- 三段式契約：行為契約、資料契約、授權政策（預設拒絕 + scope 核准 + 人工覆寫）
- 機床哲學：可重複、可檢驗的產出讓軟體「工廠」靠回饋成長而非一次性即興

---

## Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5

**Date:** 2026-07-20 | **URL:** https://claude.com/blog/working-at-the-frontier-rakuten

### Summary
Rakuten 的 AI 總經理 Yusuke Kaji 說明 Fable 5 如何讓 agent 無人監督連跑數小時：模型自我驗證並在執行中修正路線，把工作單位從「任務」上移到「決策」。

### Key Points
- Fable 5 自查頻率遠高於任何前代模型，能在錯誤假設滾大成失敗前抓住
- 會在未被要求的情況下回頭對照原始意圖重新驗證，不再需要凌晨兩三點的人工校正
- 在模糊決策上與團隊偏好的「品味對齊」更順，降低監督摩擦
- 委派模型改變：從「切好定義明確的區塊給 agent 執行」變成整包交付、人類只在決策點介入
- 成本策略：只在額外能力真正改變結果的地方用 Fable 5，例行工作路由到較小模型

---

## Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems

**Date:** 2026-07-17 | **URL:** https://claude.com/blog/working-at-the-frontier-cursor

### Summary
Cursor 工程師 Nate Schmidt 用內部基準測試 CursorBench 評估 Claude Fable 5：模型在困難任務中達到 72.9% 成功率，展現「全局推理」能力，能理解複雜工程問題的整體背景，不需頻繁提示即可完成長期運行的實際工作。

### Key Points
- Fable 5 在 CursorBench Max effort 評估創新高 72.9%，超越其他模型表現
- 展現「全局推理」而非 Opus 的「局部推理」，思考整個任務流程更高效
- 月球著陸實驗：Fable 5 數小時完成 Opus 需 12+ 小時卻未成功的任務
- 適合目標路徑不確定的問題，能降低複雜重構等工作的啟動成本
- Cursor 團隊將 Fable 5 與輕量級模型配對使用，平衡成本與性能

---

## Zero risk isn't the job: a CISO's guide to agentic AI

**Date:** 2026-07-17 | **URL:** https://claude.com/blog/ciso-guide-to-agentic-ai

### Summary
Anthropic 副首席資安官 Jason Clinton 分享公司採納代理式 AI 的經驗與風險評估框架。核心論點：安全領導者的職責不是追求零風險，而是「讓代理風險可見且有界」。透過四個核心問題與七項控制措施，組織可在管理風險同時加速業務創新。

### Key Points
- 四個評估問題：代理處理哪些不可信內容？能採取什麼行動？失控爆炸半徑多大？可觀測性程度如何？
- 身份認證頻譜：系統服務帳戶（單一目的、最小權限）到人工憑證，模糊問責制最危險
- 七項核心控制：身份整合、連接器白名單、細粒度工具批准、沙箱執行、出站限制清單、OpenTelemetry 遙測、組織級「斷電開關」
- Claude Cowork 架構：遠端沙箱執行環境從不持有生產憑證，流量必須經過無法繞過的代理
- 治理無需成為瓶頸：合規團隊本身可運行代理，自動化風險登記與供應商審查流程

---

## How Anthropic runs large-scale code migrations with Claude Code

**Date:** 2026-07-16 | **URL:** https://claude.com/blog/ai-code-migration

### Summary
Anthropic 說明如何用 Claude Code 執行大規模程式碼遷移：Bun 共同創辦人兩週內將百萬行 Zig 代碼遷移至 Rust，100% 通過既有測試套件。文章提出六步驟框架（規則手冊、依賴映射、壓力測試、翻譯、編譯、行為驗證），核心理念是「修復流程而非代碼」。

### Key Points
- 遷移成本從過去的 300–400 萬美元降至數十萬美元，讓長期延遲的專案變得可行
- Fable 5 / Opus 4.8 擅長委派工作、指導平行工作流並驗證結果
- 必須預先建立「評判機制」（如測試套件），提供客觀的成功衡量標準
- 建立可移植性規則手冊與詳細依賴映射是最耗時的前期工作
- 用較小模型處理實作、保留大型模型做審查與規則制定
- 工作隊列應機械化且可恢復，讓編譯器/測試自動生成下一項任務

---

## Working with Claude Fable 5 in Claude Cowork

**Date:** 2026-07-16 | **URL:** https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork

### Summary
Claude Fable 5 是 Anthropic 最強大的通用模型，專為長期複雜工作設計。在 Claude Cowork 中，使用者可從簡單想法開始，透過提供上下文與約束條件，委派多步驟任務給模型執行；模型能追蹤長期工作細節、自動檢查結果，並在過程中維持對使用者目標的理解。

### Key Points
- 適用時機：複雜、模糊或多工具的重要工作，成本較高但處理複雜任務的準確性更佳
- 靈活起點：可從模糊想法開始，同一對話中腦力激盪與執行工作
- 上下文優先：提供具體背景資訊比詳細步驟指示更有效
- 全面委派：可完全委派大型任務，包括方法選擇、程序執行、排程設置
- 監督與驗證：Cowork 介面顯示模型計畫與推理過程，可及早發現問題並修正
- 基礎設施投資（連接日常工具、調整寫作風格、審查舊設定）能充分發揮 Fable 5 能力

---

## Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work

**Date:** 2026-07-15 | **URL:** https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work

### Summary
低代碼平台 Base44 發現 Claude Fable 5 是首個能像資深工程師一樣推理軟體的模型，可處理過去只能交給最資深工程師的複雜工作，使團隊得以加快產品開發速度並更有信心做出大膽的業務決策。

### Key Points
- 推理能力突破：能識別代碼中已存在的解決方案而非重複處理同一問題
- 效率提升：更少輪次完成任務，首次生成的應用更完整、包含邊界情況考慮
- 複雜工作自動化：系統提示詞重建等關鍵任務約 4 小時交付 90–95% 所需內容
- 跨團隊應用：產品經理 2.5 小時內建立行動應用開發環境
- 風險發現：模型識別出 Base44 自身測試盲點（未測試快取命中）並提出改進方案
- 組織信心提升，團隊得以推進過去因風險顧慮擱置的計畫

---

## Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail

**Date:** 2026-07-13 | **URL:** https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail

### Summary
機構金融 AI 平台 Hebbia 以專有金融基準測試評估每個新模型，Claude Fable 5 創下最高準確度提升記錄（相對準確度約提高 20%），能更好追蹤複雜查詢並在多步驟分析中保持完整背景，使金融專業人士能自動化複雜盡職調查工作流程。

### Key Points
- Matrix 平台用 meta-prompting 將自然語言請求轉為提示，在數百份文件中運行分析並提供完整可追蹤性
- Fable 5 在財務文件問答與引文匹配測試表現突出，能找到正確資訊並正確合成
- 能同時保持多部分請求，回答所有問題並引用對應來源
- 正使用 Claude Agent SDK 將複雜交易分析工作分解成可重複的檢查步驟
- 信貸審查工作從外部專家手工製作加速至自動生成初稿
- 銀行客戶關注焦點從風險擔憂轉向如何自動化更多工作流程

---

## Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night

**Date:** 2026-07-10 | **URL:** https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night

### Summary
Cognition 的 AI 軟體工程師 Devin 採用 Claude Fable 5 後能持續運行 8 小時以上而不失焦點。Fable 5 在 Cognition 自建的「Frontier Code」基準測試得分約 30%，遠高於先前 Opus 模型的 10%，是軟體工程 AI 領域近一年最重大的進步。

### Key Points
- 在複雜上下文中保持清晰思路，正確使用內部除錯工具並追蹤日誌
- Frontier Code 基準測試從 10% 提升至 30%，代表真實工程工作的實質進步
- 可在無人監督下持續工作 8 小時，完成代碼遷移及問題根因分析
- Cognition 過去一年所見最大的性能躍進
- 使主動式代理（監控 Slack 頻道、自主處理生產問題）成為可行
- 團隊預期未來 1–2 年內 90% 的代理任務將為主動發現問題並提供修復方案

---

## Working at the frontier: How Thomson Reuters builds AI for high-stakes professional work

**Date:** 2026-07-08 | **URL:** https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work

### Summary
Thomson Reuters 與 Anthropic 合作，用 Claude Fable 5 為律師、會計師等專業人士開發可信賴的 AI 工具，採「受信責任級 AI」方法結合權威內容、領域專業知識與工作流程整合。CoCounsel Legal 等產品現能同時協調數百種工具，讓原本需時數小時的法律研究在數分鐘內完成。

### Key Points
- 評估標準：模型是否能通過律師實際工作應用前的專業審查，驗證優於流暢度
- 代理優先方法：原有獨立軟體工具整合為單一代理，可即時規劃、委派並協調跨系統任務
- 四項核心能力：檢查引文、長工具鏈中保持穩定、納入人工參與、執行足以節省數週時間的複雜起草工作
- CTO Joel Hron：先實現文化轉變而非過度優化成本效率；內部工具將生產問題解決時間從 3 小時縮至 4 分鐘
- 信任基礎：Anthropic 對企業 AI 透明、安全的開發方式
- 未來方向：更長期任務、改進上下文管理、在高風險環境中運用更可靠的工具調用

---

## How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds

**Date:** 2026-07-08 | **URL:** https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds

### Summary
Anthropic 行銷營運團隊用 Claude Cowork 自動化原本耗時的手動工作：每週行銷指標報告準備時間從 1–2 天縮短至約 2 小時，活動設置流程全面自動化。透過建立可重複使用的技能與連接器整合，繁瑣的系統管理工作轉變為策略性活動。

### Key Points
- 每週報告自動化：Claude 每週日晚間自動收集數據、驗證指標，生成帶建議重點的初步報告
- 多平台整合：連接行銷平台、數據倉庫、Slack，解決傳統工具整合不完整的問題
- 品質驗證機制：校對技能確保報告每個數字追蹤到已驗證來源，不匹配時標記問題
- 活動建置工作流程：自動調度系統每小時讀取請求通道，五個專業技能分別處理不同類型工作
- 獨立審核流程：單獨 Claude 實例執行測試註冊與驗證，確保發布前符合標準
- 持續改進迴圈：團隊定期更新技能反映新的邊界情況與業務需求

---

## How people are using Claude Cowork

**Date:** 2026-07-07 | **URL:** https://claude.com/blog/how-people-are-using-claude-cowork

### Summary
Anthropic 分析 126 萬個 Claude Cowork 工作階段的使用情況，發現知識工作者主要用它處理「工作周圍的工作」——支撐性任務而非核心職責。商業流程和內容創作佔用途近一半，幫助用戶組織資訊並與團隊溝通。

### Key Points
- 商業流程和營運（33.4%）為最大使用類別，包括撰寫狀態報告、建立檢查清單、協調試算表
- 內容創作和文案（16.4%）居第二，用戶用它「克服空白頁面障礙」草擬各類文件
- 知識工作支持：軟體開發、DevOps、研究、數據分析等專業工作各佔 4–9%
- 差異化使用模式：Cowork 用於連結性工作，Claude Code 主要用於程式編寫核心工作
- 隱私方法：研究使用自動分類系統處理匿名化資料，無人類分析師審閱個別工作階段
- 對所有 Claude 使用者開放，Anthropic 提供介紹課程協助入門

---

## Building effective human-agent teams

**Date:** 2026-06-24 | **URL:** https://claude.com/blog/building-effective-human-agent-teams

### Summary
文章闡述 Anthropic 如何將工作場域協作從單人 AI 互動轉型為「multiplayer」人機協作團隊——具備持久記憶、獨立憑證與廣泛組織存取權的 Agent，與多位人類成員在如 Slack 等環境中共同工作。

### Key Points
- 四大心法：公開透明分享脈絡（Agent 的理解完全建立於團隊可搜尋的文字：Slack、程式碼、文件、會議記錄）
- 明確角色分工：每位人類與 Agent 有清楚職責與對應工具存取權，避免重複工作與脈絡破碎
- 設定 North Star：具企圖心的長期目標引導 Agent 主動提案而非被動等待指令
- 漸進建立信任：自主權隨可靠度證明逐步擴大，透過驗證機制與定期反思循環
- 實作範例：Doer-Verifier agent harness（一個執行、一個驗證）；每週「lessons & missteps」報告供持續改進；某工程團隊建立信任後讓 Agent 獨立處理 500 個 bug 修復
- 高風險決策仍保留人工判斷

---

## The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

**Date:** 2026-06-22 | **URL:** https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry

### Summary
Anthropic 擴大 Claude Desktop 在主要雲端平台的可用性，企業可透過既有 AWS、Google Cloud、Microsoft Foundry 基礎設施，於單一應用程式中完整使用 chat、Claude Cowork、Claude Code 三種介面。

### Key Points
- 統一平台：三種介面整合於單一應用，消除跨部署的碎片化問題
- 資料落地與控管：推論留在客戶自控雲端環境、對話紀錄本地儲存，組織可自訂 connector 可存取的端點
- 企業部署功能：整合 IAM Identity Center、Entra ID、OIDC（Okta）SSO；policy 範本可匯出至 Intune、GPO、Jamf；支援離線安裝（air-gapped）與 pre-rollout 驗證工具；各介面可分別設定存取權限
- Microsoft 365 原生整合：透過 Entra 驗證存取郵件與文件，支援 GCC High/DoD 端點與純本地連線選項
- 案例：Hanwha Solutions 透過自有 LLM Gateway 為全球數百名使用者部署 Claude Desktop，無需另立供應商合約

---

## Secure access to the Claude Platform with Workload Identity Federation

**Date:** 2026-06-17 | **URL:** https://claude.com/blog/workload-identity-federation

### Summary
Workload Identity Federation（WIF）正式 GA，以短期 OIDC 憑證取代靜態 API key，支援 AWS IAM、GCP、Azure、GitHub Actions、Okta 等主流身份提供者。

### Key Points
- 每個 workload 可分配獨立 Service Account，具備獨立角色與稽核軌跡
- 支援 Admin API 大規模程式化配置，適合多工作負載企業環境
- 與既有 API key 並存，可逐步遷移，不中斷現有操作
- 消除靜態 long-lived API key 的安全風險（key rotation、洩漏風險）
- 與 Enterprise Managed Auth（IdP-managed MCP connector 授權）互補

---

## Centrally manage authorization for MCP connectors

**Date:** 2026-06-18 | **URL:** https://claude.com/blog/enterprise-managed-auth

### Summary
企業版 MCP connector 集中授權管理（Team/Enterprise Beta），透過 Okta 等 IdP 統一配置，消除逐個 OAuth 審批流程，員工登入即自動取得 connector 存取權。適合有大量員工需要存取相同 MCP connectors 的組織。

### Key Points
- Zero-touch 設定：依 IdP 群組成員資格自動配置，跨 Claude chat、Claude Code、Cowork 生效
- 支援 Asana、Atlassian、Canva、Figma、Linear、Supabase 作為 MCP provider；Okta 負責身份管理
- 可強制 IdP-only 連線，支援 token 生命週期控制，加速撤銷存取
- IT 管理員可在一個地方撤銷員工所有 connector 存取（離職 offboarding 場景）

---

## How Anthropic enables self-service data analytics with Claude

**Date:** 2026-06-03 | **URL:** https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude

### Summary
Anthropic Data Science/Engineering 團隊分享自助資料分析架構。問題的本質是「Context 與驗證問題，而非程式碼生成問題」。無 Skills 準確率 ≤21%；有 Skills ≥95%。

### Key Points
- 三大失敗模式：概念到實體的歧義（"active users"映射）、資料過期（Schema 漂移）、檢索失敗（找不到正確資料）
- 四層技術架構：Data Foundations（Canonical datasets）→ Sources of Truth（Semantic layer）→ Skills（知識 + 程序 Skill 配對）→ Validation（離線 eval + adversarial review）
- Semantic layer 是第一道強制步驟：預建 join、grain、filter 消除歧義
- Skills 配對：薄層知識 router + 詳細程序 unbook；~90% data PR 現在包含 skill 修改
- Adversarial review sub-agent：+6% 準確率，但 +32% 延遲

---

## Using LLMs to secure source code

**Date:** 2026-05-27 | **URL:** https://claude.com/blog/using-llms-to-secure-source-code

### Summary
Eugene Yan 和 Henna Dattani 分享六步驟漏洞掃描方法論：Threat Modeling → Sandbox → Discovery → Verification → Triage → Patching。Anthropic 已在開源軟體中揭露 1,596 個漏洞。

### Key Points
- 六步驟框架：建立 `THREAT_MODEL.md` → 沙箱隔離（容器/Firecracker/VM）→ 並行 discovery（非指令性 prompt）→ 獨立 verifier（反駁而非確認）→ 根因去重 triage → 先寫失敗測試再修補
- 驗證 Agent 與 Discovery Agent 分離，減少 false positive 約 50%；要求 PoC 驗證後 false positive 趨近於零
- 參考實作：`defending-code-reference-harness` GitHub repo + Claude Security managed product
- 第一次掃描發現量高，後續掃描發現較少但更複雜的漏洞

---

## How CodeRabbit used Claude to build an agent orchestration system

**Date:** 2026-05-27 | **URL:** https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system

### Summary
CodeRabbit 使用 Claude 建立 Agent 協調系統，用於自動化 code review 工作流。展示如何以 Claude 作為核心智能，協調多個專業 agent 執行大型 codebase 分析。

### Key Points
- 使用 Claude 作為中央協調器，委派給專業 agent
- 多 agent 平行分析大型 PR，整合結果
- 與現有開發工作流（GitHub）深度整合
- 案例：大型企業 monorepo 的 PR review 自動化

---

## Zero Trust for AI agents

**Date:** 2026-05-27 | **URL:** https://claude.com/blog/zero-trust-for-ai-agents

### Summary
針對 AI Agent 部署的 Zero Trust 安全框架。前沿 AI 模型正在壓縮漏洞發現到利用之間的時間（從數月到數小時）。提出三層實施框架（Foundation/Advanced/Optimized）和八個實施階段。

### Key Points
- AI 加速威脅：模型可發現傳統工具和人工 reviewer 多年未發現的嚴重漏洞
- Agentic 系統特有漏洞：工具存取/自主決策、Context 持久化和記憶毒化、多 Agent 協調風險、Prompt injection 和工具毒化、身份與權限濫用、Supply chain 攻擊
- 三層框架：Foundation（基本身份存取控制）→ Advanced（增強範圍和沙箱）→ Optimized（AI 加速防禦操作）
- 八大實施面：加密根身份、任務範圍權限、記憶保護、輸入/輸出控制、Agentic SOAR

---

## How our partners are putting Opus to work for cybersecurity

**Date:** 2026-05-21 | **URL:** https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity

### Summary
企業合作夥伴如何將 Claude Opus 4.7/4.8 應用於網路安全場景，包括威脅偵測、漏洞分析、事件回應自動化。

### Key Points
- 威脅偵測和告警分類（CLUE 平台案例）
- 漏洞分析和安全審計自動化
- 事件回應 playbook 執行
- 安全日誌自然語言查詢

---

## How Anthropic's finance team uses Claude to shape the narrative behind the numbers

**Date:** 2026-05-22 | **URL:** https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers

### Summary
Alice Fong（Anthropic 企業財務策略）分享財務團隊使用 Claude Cowork 處理季報板塊、月度審查、財務模型的工作流。Claude 作為數字更新時的「一致性保障層」，每週節省 10-20 小時。

### Key Points
- 四種工作流：季度 Board deck（Cowork 跨投影片一致性）、月度審查（維持既定聲音起草評論）、財務模型（Claude for Excel 追蹤引用）、跨團隊 Context（Google Workspace/Slack connectors）
- 核心優勢：數字多次更新時維持敘事一致性，分析師專注策略而非反覆驗證
- 成效：節省 10-20 小時/週，用於更高影響力的策略工作

---

## Deploying Claude across the legal industry

**Date:** 2026-05-15 | **URL:** https://claude.com/blog/deploying-claude-across-the-legal-industry

### Summary
法律行業 Claude 部署完整指南。87% 法務長團隊現使用 Generative AI（去年 44%）。涵蓋產品矩陣、12 個預建 Plugin、合約審閱到法規監控的具體用例。

### Key Points
- 產品矩陣：Chat（研究）、Cowork（事務級多檔案工作）、Microsoft 365（Word/Excel/Outlook）、Platform（客製應用）
- 12 個實務領域 Plugin：Commercial、Corporate、Employment、Privacy、Product、Regulatory、AI Governance、IP、Litigation
- 用例：合約審閱/紅線標記、M&A 盡職調查、隱私影響評估、法規監控、訴訟準備
- 技術指引：主機選擇、資料留存、特權保護、審計要求
- Anthropic 內部法律團隊實作案例

---

## How Claude Code works in large codebases: Best practices and where to start

**Date:** 2026-05-14 | **URL:** https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

### Summary
大規模 Codebase（百萬行 Monorepo、遺留系統、分散式架構）Claude Code 部署模式。成功的關鍵在「Harness」生態系統——CLAUDE.md、Hooks、Skills、Plugins、MCP Server 的五元件組合。

### Key Points
- Claude Code 用 Agentic Search（非 RAG），直接在本地 codebase traverse；導覽品質取決於 codebase 組織
- 五元件 Harness：CLAUDE.md（精簡分層）、Hooks（事件觸發自動化）、Skills（按需專業知識）、Plugins（組織分發）、MCP（內部工具連接）
- CLAUDE.md 三原則：保持精簡、子目錄初始化、排除生成檔案；搭配 LSP 做符號級搜尋
- 每 3-6 個月審閱設定（模型進化後，舊指令可能反而限制新模型）
- 組織所有權：指定 DRI 管理設定，避免碎片化

---

## Deploying Claude across financial services

**Date:** 2026-05-05 | **URL:** https://claude.com/blog/deploying-claude-across-financial-services

### Summary
金融服務 Claude 部署完整指南。涵蓋投資銀行、財富管理、零售銀行三個子行業，以及研究、交易、承保、索賠、模型審查、月末關帳六大工作流。提供三階段採用計劃。

### Key Points
- 產品矩陣：Chat（研究）、Cowork（多檔案專案）、Code（量化/工程）、Microsoft 365（試算表/文件）、Managed Agents（客製應用）
- 10 個金融 Agent 模板：Pitch Builder、Market Researcher、KYC Screener、General Ledger Reconciler、Month-end tools 等
- 案例：AIG、Commonwealth Bank of Australia、IG Group、Moody's
- 三階段計劃：基礎 → 試點 → 規模化，附具體行動步驟

---

## Agents for Financial Services

**Date:** 2026-05-05 | **URL:** https://www.anthropic.com/news/finance-agents

### Summary
Anthropic 發布 10 個金融服務 agent 模板，擴展 Microsoft 365 整合（Excel、PowerPoint、Word），並新增 Dun & Bradstreet、Moody's 等金融數據連接器。Claude Opus 4.7 在 Vals AI Finance Agent 基準達 64.37%。

### Key Points
- 10 個金融 agent 模板：投資手冊建立、KYC 審查、月末關帳等
- Microsoft 365 深度整合：Excel、PowerPoint、Word 自動化
- 新金融數據連接器：Dun & Bradstreet、Fiscal AI、Moody's
- 基準成績：Claude Opus 4.7 在 Vals AI Finance Agent 達 64.37%
- 目標：提升金融機構 AI agent 部署效率

---

## Building a New Enterprise AI Services Company with Blackstone, Hellman & Friedman, and Goldman Sachs

**Date:** 2026-05-04 | **URL:** https://www.anthropic.com/news/enterprise-ai-services-company

### Summary
Anthropic 與 Blackstone、Hellman & Friedman、Goldman Sachs 合作成立企業 AI 服務公司，為中型企業提供 Claude 整合的工程支援，重點覆蓋醫療與製造業。

### Key Points
- 聯合成立：新企業 AI 服務公司（獨立實體）
- 合作方：Blackstone、Hellman & Friedman、Goldman Sachs
- 服務對象：中型企業 Claude 整合工程支援
- 重點行業：醫療、製造業
- 應用 AI 工程師團隊協助識別高影響力用例並開發定制方案

---

## Anthropic and NEC Collaborate to Build Japan's Largest AI Engineering Workforce

**Date:** 2026-04-24 | **URL:** https://www.anthropic.com/news/anthropic-nec

### Summary
Anthropic 與 NEC 達成戰略合作，NEC 向全球約 3 萬員工部署 Claude，重點覆蓋金融、製造、網路安全、地方政府，建立卓越中心培育 AI 原生工程團隊。

### Key Points
- 規模：NEC 全球 ~3 萬員工部署 Claude（首個日本全球合作夥伴）
- 重點行業：金融、製造、網路安全、地方政府
- 卓越中心：培育 AI 原生工程團隊
- 目標：建立日本最大企業 AI 工程人才庫
- 戰略意義：Anthropic 亞太企業市場深化

---

## How Carta Healthcare gets AI to reason like a clinical abstractor

**Date:** 2026-04-08 | **URL:** https://claude.com/blog/carta-healthcare-clinical-abstractor

### Summary
透過 Context Engineering（而非規則式系統）達到 98-99% 的臨床資料擷取準確率。讓臨床專家保持在迴圈中，部署週期從數月縮短至數週。

### Key Points
- LLM 比傳統 NLP 更能處理臨床文件中矛盾證據的情境判斷
- Context Engineering（正確組裝和排序 context）是真正瓶頸
- 展示每個資料點背後的證據，支援驗證和回饋
- 部署週期從數月縮短至數日

---

## 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**Date:** 2026-03-13 | **URL:** https://claude.com/blog/1m-context-ga

### Summary
Claude Opus 4.6 和 Sonnet 4.6 的完整 1M token context window 以標準定價正式開放，不額外收費。每次請求最多支援 600 張圖片或 PDF 頁面。

### Key Points
- 統一定價：整個 1M token 範圍無乘數，不額外收費
- 媒體容量提升：每次請求 600 張圖片或 PDF 頁面（原來是 100）
- Claude Code 整合：Max、Team 和 Enterprise 用戶自動存取完整 window
- Opus 4.6 在整個 context 長度上 MRCR v2 達到 78.3%

---

## Advancing Claude for Excel and PowerPoint

**Date:** 2026-03-11 | **URL:** https://claude.com/blog/claude-excel-powerpoint-updates

### Summary
Claude for Excel 和 PowerPoint 新增跨檔案 context 共享功能，支援 Skill 自動化，並擴展至 Amazon Bedrock、Google Cloud Vertex AI 和 Microsoft Foundry 部署。

### Key Points
- 跨應用 context 共享：在 Excel 和 PowerPoint 之間保持完整對話 context
- 金融分析 Skill（LBO 模型、DCF 分析）和簡報 Skill
- 擴展雲端部署：Bedrock、Vertex AI、Microsoft Foundry
- 原生 Excel Agent Mode：Microsoft 365 Copilot 整合

---

## Claude Enterprise, now available self-serve

**Date:** 2026-02-12 | **URL:** https://claude.com/blog/self-serve-enterprise

### Summary
Claude Enterprise 現在可以直接從網站購買，無需銷售對話。組織可立即設定工作區、配置 SSO 和邀請團隊成員。

### Key Points
- 自助購買：直接線上購買，幾分鐘內部署
- 整合 AI 產品：Claude、Claude Code、Cowork 和領域專屬 Plugin
- 企業安全控制：SSO、域名捕捉、SCIM、審計日誌、Compliance API
- 成本管理：按位加用量定價，組織和用戶級費用上限
- 不使用 Enterprise 數據訓練模型

---

## Behind the model launch: What customers discovered testing Claude Opus 4.6 early

**Date:** 2026-02-09 | **URL:** https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early

### Summary
Harvey、Bolt、Shopify 和 Lovable 在早期測試 Claude Opus 4.6，進行密集評估。他們的回饋直接影響了最終發布版本。

### Key Points
- 基準突破：Harvey 的 BigLaw Bench 達到 90.2%（第一個超過 90% 的 Anthropic 模型）
- 卓越除錯：Bolt.new 發現 Opus 4.6 首次嘗試即能診斷之前模型失敗的 bug
- 增強自主性：改善指令遵循，能預測需求並創建解決方案
- 早期回饋直接影響最終產品設計

---

## Advancing finance with Claude Opus 4.6

**Date:** 2026-02-05 | **URL:** https://claude.com/blog/opus-4-6-finance

### Summary
Claude Opus 4.6 為金融專業人士提供增強的金融推理能力，在 Real-World Finance 評估上比 Sonnet 4.5 提高 23+ 個百分點，並推出 Cowork 桌面應用和 PowerPoint 整合。

### Key Points
- 效能提升：Real-World Finance 評估比 Sonnet 4.5 高 23+ 個百分點
- Cowork 發布：讓 Claude 讀取、編輯、建立檔案並使用自訂金融 Plugin
- Claude in Excel 增強：長時間執行任務、樞紐分析表、條件格式
- Claude in PowerPoint Beta：直接建立簡報的研究預覽工具

---

## How leading retailers are turning AI pilots into enterprise-wide transformation

**Date:** 2026-01-28 | **URL:** https://claude.com/blog/how-leading-retailers-are-turning-ai-pilots-into-enterprise-wide-transformation

### Summary
大多數企業 AI 計畫難以超越試點階段的指南。識別成功組織的三個關鍵步驟，並借鑒零售商的實際案例（Shopify、L'Oréal）。

### Key Points
- 零售挑戰：碎片化技術棧、季節性需求、缺乏 AI + 運營複合技能
- 成功模型：Shopify 為商家建立 AI 助手；L'Oréal 在 150 個國家協調 15+ 個專業 Agent
- 基礎和治理：利害關係人對齊和明確治理框架優先於試點
- 選擇性試點策略：從低風險應用開始，而非全企業推廣

---

## How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds

**Date:** 2026-01-26 | **URL:** https://claude.com/blog/how-anthropic-uses-claude-marketing

### Summary
非技術行銷人員 Austin Lau 使用 Claude Code 構建自動化工作流，將廣告創作從 30 分鐘縮短至 30 秒。無需編碼經驗即可開發 Figma 插件和 Google Ads 工作流。

### Key Points
- Figma 插件：一鍵生成多種長寬比的廣告變體（節省每批 ~30 分鐘）
- Google Ads 工作流：腦力激盪、驗證字元數、匯出 CSV
- 行銷影響：影響者行銷每月節省 100+ 小時；案例研究從 2.5 小時降至 0.5 小時
- 非技術用戶通過清晰表達問題即可構建工具

---

## Making Claude a better electrical engineer

**Date:** 2025-12-12 | **URL:** https://claude.com/blog/making-claude-a-better-electrical-engineer

### Summary
Anthropic 與 Diode Computers 合作提升 Claude 自動生成電氣參考設計的能力。透過領域專家合作和專業訓練數據，Claude Sonnet 4.5 在複雜技術任務上達到卓越效能。

### Key Points
- 領域特定合作：與行業專家識別能力差距並整合專業知識
- 參考設計自動化：在數小時內（而非數天）處理芯片文件並生成完整電路圖
- 技術準確性提升：更好地解讀數據表、理解精細電路
- 工程師偏好 Sonnet 4.5 設計的比例為 80%（vs Sonnet 4）

---

## How enterprises are building AI agents in 2026

**Date:** 2025-12-09 | **URL:** https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026

### Summary
500+ 技術領導者調查顯示，企業正從簡單任務自動化過渡到跨整個團隊的複雜多步驟工作流。80% 的組織報告其 AI Agent 投資已提供可量化的經濟回報。

### Key Points
- 57% 為多階段工作流部署 Agent；81% 計劃 2026 年更複雜的用例
- 90% 使用 AI 進行開發；86% 在整個開發生命週期部署 Agent
- Thomson Reuters 將法律研究從小時縮短至分鐘；eSentire 將威脅分析從 5 小時壓縮至 7 分鐘（95% 準確率）
- 實施優先事項：系統整合（46%）、數據存取/質量（42%）、變革管理（39%）

---

## How Anthropic's legal team cut review times from days to hours with Claude

**Date:** 2025-12-08 | **URL:** https://claude.com/blog/how-anthropic-uses-claude-legal

### Summary
Anthropic 法律團隊使用 Claude 自動化合約審閱和行銷內容審查，將合規審閱從 2-3 天縮短至 24 小時。透過 Claude 和專業 Skill 建立無代碼工作流。

### Key Points
- 行銷審查工具：Slack 整合工作流，標記公開權利問題；周轉時間從 2-3 天降至 24 小時
- 合約審閱：比較文件版本並推薦商業手冊語言
- 利益衝突分析：針對政策框架的自動化表單審查
- 最佳實踐：從痛點開始、使用自然語言指令、保持人工監督

---

## How three YC startups built their companies with Claude Code

**Date:** 2025-11-17 | **URL:** https://claude.com/blog/building-companies-with-claude-code

### Summary
三家 Y Combinator 新創公司展示 Claude Code 如何壓縮開發週期和讓非工程師也能建立產品。HumanLayer、Ambral 和 Vulcan Technologies 的創辦人展示結構化工作流和多模型委派如何加速擴展。

### Key Points
- 分離工作流：研究、規劃和實作作為不同階段，防止 context 污染
- 多模型委派：Opus 4.1 負責研究/規劃，Sonnet 4.5 負責實作（更高品質）
- 非技術創辦人可以競爭：清晰思維和結構化問題分解比傳統工程背景更重要
- 早期中斷防止浪費：仔細審視 chain-of-thought 並提早停止無效方向

## How we contain Claude across products

**Date:** 2026-05-25 | **URL:** https://www.anthropic.com/engineering/how-we-contain-claude

### Summary
Anthropic 跨產品隔離 Claude 的工程實務（2026-07-17 稽核補收——corpus 覆蓋期內遺漏篇）。環境層優先於模型層、三類風險分層隔離、自製隔離元件的實際事故記錄。

### Key Points
- 「環境層優先於模型層」：模型層防禦永遠無法達 100% 有效（對應本 workspace「判斷 vs 決定」公理——安全靠確定性邊界非模型自律）
- 針對使用者誤用/模型失誤/外部攻擊三類風險分層隔離，隔離強度配合使用者監督能力
- 自製隔離元件比 gVisor/seccomp 等成熟技術更易出漏洞；記錄信任邊界前執行代碼、approval fatigue 導致安全降級等實際事故
