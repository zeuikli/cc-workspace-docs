---
title: "Claude Code — claude.com/blog"
type: index
---

# Claude Code — claude.com/blog

> 收錄自 [claude.com/blog/category/claude-code](https://claude.com/blog/category/claude-code) · 45 篇文章 · 2026-01-29 ~ 2026-07-24
> 最後更新：2026-08-04

---

## The new rules of context engineering for Claude 5 generation models

**Date:** 2026-07-24 | **URL:** https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models

### Summary
Anthropic 為 Opus 5 / Fable 5 刪掉 Claude Code system prompt 的 80% 以上，在既有 coding evals 上無可量測退化。文章把 context engineering 的六條規則從「硬性條文」改寫為「信任模型判斷」，並主張舊做法在 over-constrain 模型——互相衝突的指令會消耗推理預算。

### Key Points
- 刪除 system prompt 80%+，advanced 檔位無可量測退化
- 衝突指令實例：「leave documentation as appropriate」與「DO NOT add comments」同時存在
- Progressive disclosure：驗證與 code review 指導移出 system prompt，改為 Claude 需要時才呼叫的 Skill
- Deferred tool loading：部分工具需先經 ToolSearch 取得完整定義才可呼叫，降低初始 context
- 用表達力強的參數與清楚 enumeration（`status: pending/in_progress/completed`）取代使用範例
- Auto-memory 取代手動 `#` 熱鍵寫入 CLAUDE.md
- Context Assembly 四層：system prompt / CLAUDE.md（gotchas）/ Skills / References

---

## Claude models explained: choosing the best model for your use case

**Date:** 2026-07-24 | **URL:** https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case

### Summary
官方選型指南：從「目前一般可用的最聰明模型」起步，再依延遲、成本與任務難度往下調。選型依據是任務難度與單位經濟，不是產業別——每個 Claude 模型都受訓於 coding、agentic 與知識工作。

### Key Points
- 四 class 定位：Mythos/Fable（前沿）、Opus（推理密集）、Sonnet（日常與高量 sub-agent）、Haiku（成本敏感高頻）
- Effort 等級製造「品質×速度×成本」連續取捨面；高 class 低 effort 的 per-task 經濟性有時優於低 class 模型
- 每 token 價格 ≠ 每任務價格，選型應以後者為準
- Advisor 策略實測：Sonnet 搭配 Fable 監督 = Fable-only 效能的 90%、成本 63%
- 對強模型而言自建 eval 比公開 benchmark 更有區辨力
- 自建 eval 的另一價值：分辨「模型能力不足」與「整合／context 沒接好」

---

## Building verification loops in Claude Code with skills

**Date:** 2026-07-22 | **URL:** https://claude.com/blog/building-verification-loops-in-claude-code-with-skills

### Summary
說明如何把手動驗證檢查編碼成 Skill，讓 agent 自己閉環：跑測試、linter 或自訂檢查，失敗就修完再往下走。涵蓋內建驗證能力、自訂驗證 Skill 寫法，以及四種部署形態。

### Key Points
- 驗證迴圈定義：agent 檢查自己的產出並在往下走之前修好失敗項的重複循環
- 內建能力：`/verify` skill、toolchain（linter/type checker）、Code Review、GitHub Actions、spec validation、managed agents 的 rubric
- 寫法：`skill-creator` plugin 產生骨架，或手寫 `.claude/skills/` markdown（frontmatter: name/description/allowed-tools + 白話程序）
- 四種部署形態：standalone（跨切面、刻意呼叫）、embedded（內嵌產出型 Skill）、chained（Skill 觸發 Skill）、PR-wide（團隊基礎建設）
- 專案特定確定性規則即素材，例如「拒絕沒有 backfill 的 drop column migration」
- 演進路徑：個人生產力工具 → 鏈式自動化 → PR gate，讓標準不依賴個人自律

---

## How Outtake built a cyber investigator on Claude

**Date:** 2026-07-22 | **URL:** https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude

### Summary
Outtake 用 Claude 打造可連續執行數小時的自主網路調查員 Recon Agent，追蹤完整攻擊網路。團隊先在 Claude Code 原型驗證假設，再轉進 Agent SDK 取得對記憶與 session 的生產級控制。

### Key Points
- 不處理單一威脅，而是跟著對手走完整條攻擊鏈（資料蒐集 → 冒名誘餌 → 基礎設施測繪），產出威脅行為者剖繪與時間線
- 開發路徑：團隊先自己成為調查專家 → Claude Code 原型 → Agent SDK 生產
- 受限的 orchestration + 不受限的判斷：硬編碼「一定要做的調查步驟」，把「怎麼做」留給 agent 即興發揮（可用 filesystem/bash 等開放工具）
- 用自動 eval 取代人工看 30 分鐘以上的 transcript，讓模型升級與迭代不卡在開發者身上
- 敵意環境下的安全：假設 agent 會被挾持而建 blastbox 沙箱，並在接觸外部站點前設檢查點

---

## How Anthropic secures its AI-native software development lifecycle

**Date:** 2026-07-21 | **URL:** https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle

### Summary
Anthropic 副 CISO Jason Clinton 說明在「AI 撰寫 80% 合併程式碼」的環境下如何保安全：把審查左移、設硬性存取邊界、自動與人工審查分工、並把 agent 行為視為新型內部威脅來監控。

### Key Points
- 工程師每季出貨量為 2021–2025 的 8 倍；超過一半的合併由 Claude Tag 處理，人類負責定意圖與最終核可
- 規劃階段：AI 專案安全審查對照 MITRE ATT&CK 並接上組織知識庫，低風險上線可自助核准，不成瓶頸
- 生成階段：CLAUDE.md 把安全最佳實踐編碼進生成過程，安全 review plugin 即時給建議——在產生時預防而非事後偵測
- 審查階段：多個窄焦點 agent 各持獨立 context 與偏誤審同一個 PR，加上 SAST 與對自動核可的人工抽樣
- 圍堵：遠端 coding VM 只開 allowlist 出口、agent 權限分離、獨立系統帳號，限制爆炸半徑
- 治理：所有 agent 動作進 SIEM；發現漏洞自動回寫 CLAUDE.md 以免同類問題再生成

---

## How Datadog built a "universal machine tool" for Claude Code

**Date:** 2026-07-21 | **URL:** https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code

### Summary
Datadog 打造 Temper：agent 不再產出應用程式碼，而是產出精確規格，由確定性 kernel 以四層分析驗證後才執行。目的是補上「agent 生成的東西」與「可安全驗證並部署的東西」之間的落差。

### Key Points
- 問題意識：任務愈複雜，工程師被迫升級成管理者——要管 agent 看到什麼、能用什麼工具、成功標準與失敗偵測
- 前三代嘗試：Courier（分散式佇列）、BitsEvolve（演化式最佳化）、Helix（串流服務）後才定位出真正瓶頸
- Temper 反轉做法：agent 產規格，kernel 用符號推理、窮舉狀態探索、確定性模擬與 property testing 驗證，小規格一秒內完成
- 三段式契約：行為契約（狀態與轉移）、資料契約（機器可解析的 entity API）、授權政策（預設拒絕 + scope 核准 + 人工覆寫）
- 機床哲學：像治具與 CNC 產出可重複、可檢驗的零件，讓軟體「工廠」靠回饋成長而非一次性即興

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

## Choosing a Claude model and effort level in Claude Code

**Date:** 2026-07-07 | **URL:** https://claude.com/blog/claude-model-and-effort-level-in-claude-code

### Summary
說明 Claude Code 中「模型選擇」與「工作量級別」的差異：模型決定固定能力範圍，工作量級別控制 Claude 投入多少努力（讀取檔案數、驗證次數、執行深度）。選擇應基於任務複雜度與所需徹底程度，而非盲目調整設定。

### Key Points
- 模型選擇決定基礎知識與能力；工作量級別決定投入多少計算資源
- 面對高難度、需專業知識的任務升級模型；例行工作用較小模型省成本
- Claude 跳過檔案、未執行測試或放棄多步驟任務時，提高工作量級別
- 大多數情況應用模型預設工作量級別，視為通用偏好而非逐任務調整
- 較大模型在複雜多步任務上可能更經濟，因為需要較少迭代達成目標
- 三層模型比喻：Fable 是見過罕見問題的專家、Opus 是有深度經驗的專家、Sonnet 是能力強的通才

---

**Date:** 2026-07-06 | **URL:** https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns

### Summary
Anthropic 員工 Thariq Shihipar 分享與 Claude Fable 協作的核心心法：工作品質受限於「釐清 unknowns 的能力」而非模型本身。文章區分「地圖」（prompt/context）與「疆域」（實際 codebase/限制）之間的落差，並提出四類 unknowns 分類與對應工作流程。

### Key Points
- 四類 unknowns：Known Knowns（已聲明需求）、Known Unknowns（已知缺口）、Unknown Knowns（顯而未說的脈絡）、Unknown Unknowns（未預期考量）
- 實作前：Blindspot Pass、腦力激盪、Prototype、Interview、參考資料、實作計畫
- 實作中：維護 Implementation Notes 記錄偏離決策
- 實作後：撰寫 pitch、說明文件、quiz 驗證理解是否正確
- 實例：作者用 Claude 端到端剪輯 Fable 發表影片，透過迭代發現逐字稿準確度、影片節奏、色彩校正等 unknowns

---

## Getting started with loops

**Date:** 2026-06-30 | **URL:** https://claude.com/blog/getting-started-with-loops

### Summary
Claude Code 團隊官方指南，說明如何設計「agentic loop」（重複執行直到滿足停止條件的迴圈）。文章將迴圈分為四種類型，並提供選擇與收斂設計原則。

### Key Points
- Turn-based：由使用者手動觸發，適合較短、非重複性任務；建議用 SKILL.md 封裝驗證步驟以增進自我檢查
- Goal-based（`/goal`）：持續執行至達成目標或觸及最大回合數，適合有「可驗證退出條件」的任務（如 Lighthouse 分數 ≥ 90）
- Time-based（`/loop`、`/schedule`）：依排程觸發，適用週期性工作或監控外部系統（如巡邏 PR review comment）
- Proactive：事件驅動、長時間執行、無需人工介入，結合 auto mode 與 dynamic workflows 處理大規模明確定義工作
- 建議搭配 `/usage`、`/workflows` 檢視用量，並從簡單設計開始迭代

---

## Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

**Date:** 2026-06-24 | **URL:** https://claude.com/blog/agent-identity-access-model

### Summary
Claude Tag 推出「Agent Identity」存取模型，解決多人協作環境中「代表使用者行事」模式失效的問題——Claude 不再借用單一使用者權限，而是在每個系統中擁有自己的 workspace 層級帳號。

### Key Points
- 問題：Agent 現在自主運作超越單一 session，多位成員共同引導造成權限歸屬模糊
- Workspace 層級基準權限由管理員設定，channel 層級可個別限縮或擴增（如工程頻道給 GitHub 存取、財務頻道給倉儲寫入）
- 適用範圍涵蓋 repo 存取、API 連接器、skills/plugins、standing instructions
- 私人頻道維持獨立身份；公開頻道共用 workspace 身份；DM 則以個人 claude.ai 帳號、個人憑證執行
- 安全機制：憑證獨立儲存、於網路邊界注入、封鎖未核准對外連線、完整稽核軌跡；未來規劃 just-in-time 憑證授予
- 建議採用策略：初期給予較寬鬆存取權限，再依稽核結果收斂

---

## Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more

**Date:** 2026-06-18 | **URL:** https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more

### Summary
官方整理自訂 Claude Code 行為的七種機制選擇指南：CLAUDE.md、Rules、Skills、Subagents、Hooks、Output Styles、System Prompt Appending。核心問題框架：要改變 Claude **知道什麼** vs **呼叫什麼工具** vs **生命週期自動化** vs **回應外觀**。

### Key Points
- Skills 以資料夾形式儲存在 `.claude/skills/`，初始只載入名稱與描述，呼叫時才展開全文（降低 context 成本）
- Hooks 是**確定性**觸發器，用於生命週期事件（檔案編輯、工具呼叫），比在 prompt 中叮囑更可靠
- Path-scoped Rules 只在存取相關檔案時載入，避免不必要的 token 消耗
- CLAUDE.md ≤ 200 行（最佳 60 行）；每 3-6 個月審閱（模型更新後舊指令可能反而限制新模型）
- 詳細解析見 [best-practices/38-steering-claude-code.md](../../best-practices/38-steering-claude-code.md)

---

## Meet the winners of our Claude Opus 4.8 Build Day hackathon

**Date:** 2026-06-17 | **URL:** https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon

### Summary
2026-06-13 舉辦的 12 小時 Hackathon，310 位參賽者使用 Claude Opus 4.8 開發，主題圍繞驗證機制、優化迭代與全端開發。

### Key Points
- 第一名 **Tekton**：用獨立驗證子 agent 在隔離 context window 中重建歷史建築 3D 模型（唐代建築、巴黎聖母院）
- 第二名 **Sim Francisco**：基於人口普查數據建立 10,000 位合成居民的舊金山數位孿生，預測 2024 總統大選得票率誤差僅 2.5%
- 第三名 **Custom Universe**：手機拍照即時轉換為可編輯 3D 場景，目標機器人訓練資料生成
- 核心模式：獨立驗證 subagent + 隔離 context window 是高品質輸出的關鍵架構

---

## Meet the winners of the Built with Opus 4.7 Claude Code hackathon

**Date:** 2026-06-15 | **URL:** https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon

### Summary
Opus 4.7 Claude Code Hackathon 得獎者，涵蓋醫療訓練、電子維修、教育、工廠維護等場景，強調規劃先於執行、將 Claude 視為思考夥伴。

### Key Points
- 第一名 **Medkit**：以 Claude Managed Agents 建立遊戲化醫療訓練模擬器，AI grader 評估住院醫師臨床表現
- 第二名 **Wrench Board**：電子診斷工具，利用 Opus 4.7 視覺推理能力分析電路板圖找出故障元件
- 最佳 Managed Agents 獎 **ARIA**：工廠預測性維護系統
- 共同洞察：清晰的 context 和 spec 文件比複雜 prompt 更重要；委派式管理 Agent = 管理員工

---

## How Anthropic teams use Claude Code

**Date:** 2026-06-12 | **URL:** https://claude.com/blog/how-anthropic-teams-use-claude-code

### Summary
Anthropic 多部門 Claude Code 實際使用案例集合。涵蓋 GTM（業務自動化插件）、法務（流程引導系統）、行銷（大量廣告變體生成）、資安（CLUE 平台）、資料分析（95% 查詢自動化）。

### Key Points
- GTM：Jared Sires 建立 CLAFTS（Claude 草稿 Gmail 插件），衍生出 20+ skills 的 Cowork 插件，新員工第一天即可安裝使用
- 法務：建立「電話樹」系統，引導員工找到對的律師
- 行銷：數秒生成數百個廣告版本（原本 30 分鐘/個）
- 資安：CLUE 平台自動分析安全告警，節省 1,870 人工小時
- 資料分析：95% 商業分析查詢由 Claude 自動化，資料科學家轉移至因果建模等高階工作

---

## How one Anthropic seller rebuilt his team's workflows with Claude Code

**Date:** 2026-06-05 | **URL:** https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering

### Summary
業務主任 Jared Sires（零程式碼背景）用 Claude Code 建立 CLAFTS 工具（Gmail 插件草稿 API），書本擴增至 600-700 帳號後每天省去數小時 email 工作。後衍生成含 20+ skills 的 Cowork 插件，整合 Salesforce、Intercom、Gong、Calendar、Gmail、Drive、BigQuery。

### Key Points
- 非技術背景人員獨立建立生產級 SaaS 工具
- CLAFTS：Claude API 草稿客戶 email 回覆，從 Gmail 直接運作
- 插件化：新員工第一天安裝即可使用標準化工作流
- 核心結語：「你不需要成為工程師才能建立 AI 工具」

---

## Code w/ Claude SF 2026 recap: Building on the AI exponential

**Date:** 2026-05-09 | **URL:** https://claude.com/blog/code-w-claude-sf-2026-sf

### Summary
舊金山開發者大會（2026-05-06）回顧。Daniela Amodei 和 Dario Amodei 主持主題演講，聚焦「概念到產品程式碼的距離正在縮短」。客戶案例：Asana、Cursor、GitHub、Replit、Vercel 展示生產級 Agent 架構。

### Key Points
- 核心主題：設計 AI 指數曲線而非被動應對
- Cursor：Agent 彈性架構實戰分享
- Replit：vibe-coding 大規模部署案例
- Vercel：毫秒級 sandbox 啟動 + VPC peering
- 全程有 YouTube 錄影可重看

---

## Running an AI-native engineering org

**Date:** 2026-06-03 | **URL:** https://claude.com/blog/running-an-ai-native-engineering-org

### Summary
Fiona Fung（Claude Code & Cowork Engineering Director）分享 Agentic Coding 成為預設時工程組織的根本性重組方法。規劃從六個月 Roadmap 轉向 JIT Planning；Code Review 從 style+logic 轉向高判斷領域（法律/安全/產品感）；角色邊界模糊，PM 寫程式、工程師做設計。

### Key Points
- JIT Planning：原型驅動開發取代設計文件，快速內部用戶回饋循環
- Context 蒐集：先問 Claude 再找人；手動摘要 → 持續背景自動化
- 招聘優先「有產品感的創意建造者」和深度系統專家
- 三指標：Onboarding ramp time（第一週 ship 真實程式碼）、PR cycle time、Claude-assisted commits（≈100%）
- Claude Code 團隊連續四個月無非 Claude 協助 commit

---

## Lessons from building Claude Code: How we use skills

**Date:** 2026-06-03 | **URL:** https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills

### Summary
Thariq Shihipar 揭露 Anthropic 內部 Skill 使用模式，提出九大類別分類法。Skill 是完整資料夾（非只是 markdown）；description 針對模型決策而非人類閱讀；從實際失敗點累積 Gotchas。

### Key Points
- 九大 Skill 類別：Library/API Reference、Product Verification、Data Fetching、Business Process、Code Scaffolding、Code Quality、CI/CD、Runbooks、Infrastructure Ops
- 核心原則：不重述 Claude 預設行為、不過度指定指令、用 progressive disclosure 拆分 context
- 進階：on-demand hooks、assets 資料夾、`${CLAUDE_PLUGIN_DATA}` 持久記憶、execution logs
- 發布：`.claude/skills/` 直接提交、內部 marketplace、sandbox 有機採用後升官方

---

## A harness for every task: dynamic workflows in Claude Code

**Date:** 2026-06-02 | **URL:** https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code

### Summary
Thariq Shihipar 和 Sid Bidasaria 深度解析 Dynamic Workflows 的六大模式與最佳實踐。解決長時間任務三大失敗模式：Agentic laziness、Self-preferential bias、Goal drift。

### Key Points
- 六大模式：Classify-and-act / Fan-out-and-synthesize / Adversarial verification / Generate-and-filter / Tournament / Loop until done
- 技術能力：模型選擇、Worktree 隔離、Checkpoint 續接、`/goal` + `/loop` 整合
- 適合：大型遷移、全 codebase audit、深度研究（`/deep-research` 內部使用此架構）
- 不適合：標準編碼任務（token 成本明顯更高）

---

## Introducing dynamic workflows in Claude Code

**Date:** 2026-05-28 | **URL:** https://claude.com/blog/introducing-dynamic-workflows-in-claude-code

### Summary
Dynamic Workflows 正式宣告（W22 Research Preview）。Claude 動態撰寫 JavaScript 協調腳本，協調數十到數百個並行 subagent。Bun 用此將 ~750,000 行 Zig code 移植至 Rust，11 天通過 99.8% 測試。

### Key Points
- 三大使用場景：全 codebase bug hunt/audit（並行搜尋+獨立驗證）、大型遷移（框架/API/語言）、需要多次獨立嘗試的關鍵工作
- Progress 持續儲存，中斷可從 checkpoint 恢復
- 啟動：直接請求 workflow 或啟用 `ultracode` effort
- 方案：Max、Team Premium、Enterprise PAYG、API（CLI、Desktop、VS Code、Bedrock、Vertex、Foundry）

---

## How CodeRabbit used Claude to build an agent orchestration system

**Date:** 2026-05-27 | **URL:** https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system

### Summary
CodeRabbit 在編碼請求與編碼代理之間插入編排層，生成代碼前先產出結構化計劃供團隊審查。系統以多個 Claude 模型分工分析需求並釐清隱含假設，降低後期才發現問題的成本。

### Key Points
- 問題診斷：AI 生成的代碼常能編譯、通過測試，卻解不了實際問題——因為開發者未表達隱含假設
- 規劃層架構：代碼生成前插入計劃系統，產出協作型需求文檔，經團隊驗證後才實作
- 模型分層：Opus 處理高層戰略、Sonnet 序列化計劃步驟、Haiku 執行具體操作與工具呼叫
- 建立基於人工範例與 LLM 評判的計劃品質評估框架，衡量計劃層的實際價值
- 計劃本身成為品質閘門，上游規劃品質直接影響最終代碼品質
- 計劃可保存重用，幫助團隊避免返工並加速新工程師上手

---

## Using Claude Code: The unreasonable effectiveness of HTML

**Date:** 2026-05-20 | **URL:** https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html

### Summary
Thariq Shihipar 倡議 HTML-First 工作流。HTML 在資訊密度、視覺清晰度、分享性、互動能力、資料導入五個維度全面優於 Markdown。作者已幾乎完全放棄 Markdown 用於個人工作流。

### Key Points
- 五大場景：規格與探索（多方案網格）、Code Review（diff 行內標注）、設計原型（slider 互動調參）、報告研究（資料視覺化）、客製編輯器（任務專屬介面）
- 快速開始：直接 prompt "make an HTML file"，無需預設模板
- Claude Code 特有優勢：可讀 file system、MCP connector、瀏覽器、git history（claude.ai 沒有）
- HTML 作為持久跨 session 參考工件

---

## Code w/ Claude London 2026: Rethinking how we build

**Date:** 2026-05-26 | **URL:** https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build

### Summary
London 開發者大會重點回顧。Boris Cherny 闡述 AI agent 正在壓縮概念與執行之間的距離，恢復程式設計的本質簡單性。兩大技術公告：Self-hosted sandboxes（Public Beta）和 MCP Tunnels（Research Preview）。

### Key Points
- Self-hosted sandboxes：Agent 在客戶自控基礎架構執行，Orchestration 仍在 Anthropic；Cloudflare、Daytona、Modal、Vercel 為合作夥伴
- MCP Tunnels：Agent 存取私有網路服務，無需公開網際網路暴露
- 企業案例：Spotify、Base44、Legora 展示規模化實作
- Boris Cherny：「Tool execution moves to an environment you configure—your own infrastructure」

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
