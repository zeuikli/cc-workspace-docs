---
title: "Claude Code — claude.com/blog"
type: index
---

# Claude Code — claude.com/blog

> 收錄自 [claude.com/blog/category/claude-code](https://claude.com/blog/category/claude-code) · 20 篇文章 · 2026-01-29 ~ 2026-05-14
> 最後更新：2026-05-27

---

## The founder's playbook: Building an AI-native startup

**Date:** 2026-05-14 | **URL:** https://claude.com/blog/the-founders-playbook

### Summary
重構新創公司生命週期（Idea → MVP → Launch → Scale）以反映 AI 原生開發能力。涵蓋如何用 Claude 驗證假設、規劃架構、防止技術債，以及以 Agentic Workflow 取代創辦人注意力。

### Key Points
- 以 Claude 驗證問題假設、進行競品分析和用戶訪談
- 架構與安全實踐防止 AI 生成代碼的技術債
- Launch 階段：以 Agentic Workflow 取代重複性創辦人操作
- 案例：Ambral、Anything、Carta Healthcare、HumanLayer、Vulcan Technologies
- 產品矩陣：Chat vs Claude Cowork vs Claude Code 適用場景

---

## How Anthropic's cybersecurity team built a threat detection platform with Claude Code

**Date:** 2026-05-12 | **URL:** https://claude.com/blog/how-anthropic-uses-claude-cybersecurity

### Summary
Jackie Bow（Detection Platform Engineering）打造 CLUE（Claude Looks Up Evidence）平台，自動化安全告警分類與威脅調查。30 天內自動化 12,000 次查詢，節省約 1,870 小時人工操作。

### Key Points
- CLUE Triage：整合 Slack、文件、code repo、數據倉庫，偽陽性從 33% 降至 7%
- CLUE Investigate：自然語言查詢安全日誌，Claude 平行執行 SQL，3-4 分鐘完成原本需數小時的工作
- 30 天：12,000 次查詢自動化、27,000 次工具呼叫、節省約 1,870 人工小時
- 5-10x 時間節省比人工操作
- 未來方向：主動威脅獵捕、調查記錄組織記憶、非確定性調查路徑

---

## How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks

**Date:** 2026-05-01 | **URL:** https://claude.com/blog/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks

### Summary
Kostiantyn Vlasenko（PM，零編碼背景）在六週內用 Claude Code 建立並上架 iOS 壓力管理 App Respiro。採用 15+ 個專業 Subagent 並行架構，印證 PM 式管理 Agent 的可行性。

### Key Points
- TCA 架構師 Agent、Swift 開發 Agent、Metal 專家、Code Reviewer 並行工作
- 從 React Native 轉 Swift 只需幾小時（Claude vision 協助截圖分析）
- Claude 協助整合 analytics、追蹤用戶漏斗、行銷內容、成長策略
- 核心洞察：「管理 Agent 就像管理真實的人一樣」
- 現已上架 App Store，吸引數百名用戶

---

## Lessons from building Claude Code: Prompt caching is everything

**Date:** 2026-04-30 | **URL:** https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything

### Summary
Thariq Shihipar 分享 Claude Code 團隊的 Prompt Caching 最佳實踐。Cache hit rate 被視為關鍵指標，下降時會觸發 incident 處理。靜態到動態的分層結構是最有效的快取策略。

### Key Points
- 分層結構（靜態到動態）：system prompt + tools → 專案檔案 → session context → 對話訊息
- 用 messages 代替更新 system prompt（保護快取前綴）；用 `<system-reminder>` 標籤傳遞更新資訊
- Mid-session 禁止切換模型（快取模型專屬，切換須重建整個快取）
- 工具管理：對話中不增刪工具；用 stub + `defer_loading: true` 保持前綴穩定
- Compact 時保留相同 system prompt + tools + user context（確保前綴匹配）

---

## Onboarding Claude Code like a new developer: Lessons from 17 years of development

**Date:** 2026-04-28 | **URL:** https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development

### Summary
Brendan MacLean（MacCoss Lab）分享用人員 Onboarding 方法論管理 70 萬行 C# codebase（Skyline）。Context repository、Skills library、MCP integrations 三層架構讓 Claude 像新進開發者一樣逐步建立理解。

### Key Points
- 獨立 context repository（pwiz-ai）：根目錄 CLAUDE.md + 文件指標，跨所有 branch 適用
- Skills 框架：`skyline-development`、`version-control`、`debugging` 等領域知識 Skill；「參考不嵌入」保持輕量
- MCP 整合（C#/Python）：連接測試結果、異常報告、支援帖，by Claude 自己撰寫
- 成果：原本一年的 Files View 面板專案兩週完成、2,000+ 教程截圖自動更新
- 原則：「將 context 視為需要維護的工件，而非一次性描述」

---

## Meet the winners of our Built with Opus 4.6 Claude Code hackathon

**Date:** 2026-04-20 | **URL:** https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon

### Summary
5 個黑客松得獎項目，4 位非專業開發者（律師、醫師、音樂人），印證 Claude Code 的民主化影響。CrossBeam 縮短加州住宅許可審批，Elisa 讓兒童學習寫程式。

### Key Points
- CrossBeam（第一）：自動化許可審查，縮短住宅審批時間
- Elisa（第二）：視覺化積木 IDE，讓兒童學習程式
- PostVisit.ai（第三）：改善心臟科病患後續照護連續性
- TARA：基礎設施評估，小時內完成
- Conductr：以 Claude 為即時虛擬樂隊成員

---

## Best practices for using Claude Opus 4.7 with Claude Code

**Date:** 2026-04-16 | **URL:** https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code

### Summary
Opus 4.7 引入 `xhigh` 預設努力等級和自適應思考（Adaptive Thinking）。強調第一輪完整給 context，減少互動次數。

### Key Points
- `xhigh` 是 agentic 編碼工作的推薦預設值
- 自適應思考：簡單任務跳過思考，降低 overhead
- 第一輪提供完整 context（意圖、限制、驗收條件、相關檔案）
- 行為變化：更短的預設回應、更少的工具呼叫

---

## Using Claude Code: session management and 1M context

**Date:** 2026-04-15 | **URL:** https://claude.com/blog/using-claude-code-session-management-and-1m-context

### Summary
1M token context 的管理策略：rewind/clear/compact 決策框架，context rot 防範。無關資訊累積後效能下降。

### Key Points
- 使用 `/clear` 開始真正的新工作，消除過時 context
- 使用 `/rewind`（雙 Esc）跳回並重新 prompt
- 使用 `/compact` 保持連續性
- 為大量中間輸出的工作啟用 Subagent

---

## Redesigning Claude Code on desktop for parallel agents

**Date:** 2026-04-14 | **URL:** https://claude.com/blog/claude-code-desktop-redesign

### Summary
桌面 App 全面重新設計：多 Agent 並行、drag-and-drop 版面、內建終端機、檔案編輯器和 diff 檢視器。

### Key Points
- 統一 sidebar：活躍與歷史 session，支援篩選
- 內建終端機、檔案編輯器、diff 檢視器和預覽面板
- 三種檢視模式（Verbose、Normal、Summary）
- SSH 支援延伸至 Mac，適用 Pro 至 Enterprise

---

## Seeing like an agent: how we design tools in Claude Code

**Date:** 2026-04-10 | **URL:** https://claude.com/blog/seeing-like-an-agent

### Summary
從 Agent 視角設計有效工具的哲學。Progressive Disclosure、約 20 個工具上限，強調實驗和觀察。

### Key Points
- 從 Agent 視角思考工具設計
- 迭代至關重要：多次失敗後才找到 Claude 穩定採用的解法
- 隨模型改進，過去有用的約束會變成限制
- Progressive Disclosure：透過巢狀文件逐步揭露 context

---

## How and when to use subagents in Claude Code

**Date:** 2026-04-07 | **URL:** https://claude.com/blog/subagents-in-claude-code

### Summary
Subagent 是擁有獨立 context window 的隔離 Claude 實例。指南涵蓋何時委派（研究密集、並行、驗證）及多種呼叫方法。

### Key Points
- Subagent 隔離 context，防止累積資料膨脹 token 成本
- 多個 Subagent 可並行執行，總時間約等於執行一個
- 自訂 Subagent、CLAUDE.md、Skill 和 Hook 逐步自動化委派
- 非所有任務適合委派：連續依賴工作在主對話處理更簡單

---

## Auto mode for Claude Code

**Date:** 2026-03-24 | **URL:** https://claude.com/blog/auto-mode

### Summary
Auto mode 是新的權限設定，讓 Claude 獨立做出權限決策，自動阻止潛在破壞性操作，同時允許安全操作。在頻繁審批提示和繞過所有安全檢查之間取得平衡。

### Key Points
- 智能分類器審查每個工具呼叫，阻止大規模刪除、數據洩漏或惡意程式碼
- 漸進式升級策略：安全操作自動進行，風險操作被阻止並提供替代方案
- 跨平台支援：桌面、VS Code、JetBrains、CLI 和 Web
- 管理員可透過 managed settings 停用

---

## Product management on the AI exponential

**Date:** 2026-03-19 | **URL:** https://claude.com/blog/product-management-on-the-ai-exponential

### Summary
Claude Code Head of Product Cat Wu 探討快速改進的 AI 模型如何改變產品管理，從傳統長期規劃轉向快速實驗和迭代優化。

### Key Points
- 角色邊界模糊：設計師寫程式、工程師做產品決策、PM 建原型
- 短衝刺規劃加「side quests」（自主下午實驗）取代冗長前期規劃
- Demo 優先開發：原型作為主要溝通工具，而非文件
- 每次模型發布促使重新考慮現有功能

---

## Code with Claude comes to San Francisco, London, and Tokyo

**Date:** 2026-03-18 | **URL:** https://claude.com/blog/code-with-claude-san-francisco-london-tokyo

### Summary
開發者大會 Code with Claude 擴展至三個全球城市。全天活動包含實作工作坊、產品示範和與 Anthropic 工程師的直接互動。

### Key Points
- 舊金山（5/6）、倫敦（5/19）、東京（6/10）
- 含 workshop、最新功能示範、與 Anthropic 的 1:1 office hours
- 有限現場名額（隨機抽選），另有直播和錄影

---

## Bringing Code Review to Claude Code

**Date:** 2026-03-09 | **URL:** https://claude.com/blog/code-review

### Summary
AI 驅動的多 Agent code review 系統。54% 的 PR 收到實質性評論（對比以前的 16%），大型 PR 平均發現 7.5 個問題，每次 $15-25。

### Key Points
- 多 Agent 平行審查：驗證發現以消除誤報，依嚴重性排序問題
- 54% PR 收到實質性評論 vs 16%；不到 1% 的發現被標記錯誤
- 實際影響：發現關鍵認證 bug 和生產系統的預存在類型不符
- 月度費用上限和 repository 級控制進行成本管理

---

## Improving skill-creator: Test, measure, and refine Agent Skills

**Date:** 2026-03-03 | **URL:** https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills

### Summary
Skill-creator 新增測試和基準評測能力，讓 Skill 作者可驗證正確性並隨時間優化效能。包含評估框架、多 Agent 並行測試和自動描述優化。

### Key Points
- 評估框架：作者可撰寫預期輸出測試，捕捉回歸
- 基準模式：標準化評估追蹤模型更新後的通過率、時間和 token 用量
- 多 Agent 並行測試：在隔離 context 中同時執行評估
- 比較 Agent：在 Skill 版本或 Skill vs 基準線之間進行 A/B 測試

---

## How AI helps break the cost barrier to COBOL modernization

**Date:** 2026-02-23 | **URL:** https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization

### Summary
COBOL 系統支撐全球關鍵基礎設施，但現代化成本一直高得令人望而卻步。Claude Code 自動化複雜分析階段，讓組織能在數季而非數年內完成現代化。

### Key Points
- COBOL 挑戰：95% 的美國 ATM 交易依賴 COBOL，退休開發者帶走機構知識
- 自動化程式碼分析：跨數千行映射依賴關係，識別隱式數據流
- 風險評估：識別高耦合組件 vs 可早期現代化的隔離模組
- 增量驗證：逐組件現代化，每個階段測試，防止大規模回滾

---

## Bringing automated preview, review, and merge to Claude Code on desktop

**Date:** 2026-02-20 | **URL:** https://claude.com/blog/preview-review-and-merge-with-claude-code

### Summary
Claude Code 桌面版新增即時應用預覽、自動化 code review 和 GitHub PR 管理（含自動修復和合併功能）。讓開發者在單一介面完成從實作到部署的完整工作流。

### Key Points
- 即時應用預覽：啟動開發服務器，實時錯誤偵測和 console log 監控
- 整合 code review：Claude 審查本地變更，提供內嵌評論、bug 識別和建議
- GitHub PR 管理：監控 CI 狀態，可選自動修復和自動合併
- 背景 PR 監控：開發者工作時 Claude Code 繼續追蹤 PR 狀態

---

## A complete guide to building skills for Claude

**Date:** 2026-01-29 | **URL:** https://claude.com/blog/complete-guide-to-building-skills-for-claude

### Summary
幫助開發者、MCP 建置者和高級用戶建立 Skill 的綜合指南。涵蓋技術需求、測試策略和分發方法，15-30 分鐘即可完成第一個有效 Skill。

### Key Points
- Skill 結構和要求：有效可重用工作流模板的技術基礎
- MCP 整合模式：將 Skill 與 MCP 連接器結合
- 測試和迭代方法：在分發前驗證 Skill
- 分發和部署策略：組織內和更廣 Claude 社群的共享

---

## Understand Claude Code's impact with contribution metrics

**Date:** 2026-01-29 | **URL:** https://claude.com/blog/contribution-metrics

### Summary
Anthropic 為 Claude Code 引入貢獻指標，追蹤 PR 合併和代碼提交。內部數據顯示每位工程師每天合併的 PR 增加 67%，70-90% 的代碼現在使用 Claude Code 協助撰寫。

### Key Points
- GitHub 整合：自動顯示 PR 建立、代碼提交和每位用戶採用模式
- 保守測量：只計算有高度信心是 Claude Code 相關的代碼
- 速度影響：每位工程師每天合併 PR 增加 67%
- 適用 Team 和 Enterprise 客戶，需安裝 GitHub App
