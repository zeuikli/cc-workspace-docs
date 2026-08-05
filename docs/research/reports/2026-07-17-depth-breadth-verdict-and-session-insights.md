# 深度 vs 廣度終審裁決 + Session Insights（2026-07-17，Fable 高 effort 終審）

> 大亂鬥組成：辯手 ×2（quality 檔，深度方/廣度方，各 5 論點+自陳弱點+質詢）+ 實測 ×3 輪（easy / hard-trap / partial-credit ladder，各 8 組態）+ Fable 主對話終審。

## §1 辯論裁決

**兩造共識（雙方數據皆承認）**：easy 任務天花板效應下深度加碼零收益；n=1 證據不足以改行為規則（v3 後部分主張已達 n=3）。

**深度方成立的論點**：
- 系統性盲點跨模型相關（H3 別名陷阱 sonnet+haiku 同錯）→ 廣度投票**無法**稀釋相關錯誤，只有深度（effort/更強模型推理鏈）突破——v3 再證：L5 專家 finding haiku 兩檔全漏，廣度樣本再多也不會出現。
- 「fable-low 廣度最高」確實是單模型深度能力的外溢，非 fan-out 產物——廣度作為產出可以是深度的下游。

**廣度方成立的論點**：
- 成本結構：預設 low + fan-out 起手在絕大多數（非語義陷阱）任務上與深跑同正確率、成本 1/5~1/11。
- 現行制度（fan-out 對抗審查、effort 先於 model、gate 集中裁決點）已是「廣度發現 + 深度裁決」架構——被 3 輪數據持續支持。

**終審裁決（平衡準則，三段式）**：
1. **廣度做發現、深度做裁決**：fan-out 低檔多視角掃描（發現哪裡值得深），確定性 gate + 高檔終審集中深度——維持現行架構，辯論不改變制度。
2. **effort 是「模型能力區間內」的細調器**：區間內（sonnet 的語義題）effort 買得到正確性；區間外（haiku 的 L5）effort 無效，換模型才有效。判定信號 = 同模型 low/medium 都錯 → 天花板，升模型；low 錯 medium 對 → 區間內，該任務類型記 medium。
3. **相關性測試決定廣度上限**：多模型同錯（相關盲點）→ 廣度失效訊號，路由到單點深跑；多模型答案分散（噪音）→ 廣度投票有效。此判定可機械化（fan-out 後 agreement rate）。

## §2 三輪實測方法論 insight（設計鑑別題的教訓）

1. **知名陷阱無鑑別力**：可變預設/浮點相等/tuple 增賦值/dict True==1——全組態全對，這些是訓練資料裡的「背誦題」。鑑別力來自**新穎組合式**細節（stale weakref callback 需組合 GC 時序+閉包+重註冊三個概念；print 引數求值順序別名需模擬執行非模式比對）。
2. **partial-credit 階梯優於二元陷阱**：v3 的 L1-L5 梯級讓 haiku 的天花板精確定位在 L5；二元題只能給 pass/fail。
3. **廣度計數（額外 finding 數）是頂檔鑑別器**：正確率飽和後，fable(+2) > opus(+1) > sonnet(0-1) 的譜系三輪穩定。
4. **機械計分必須人工對帳**：三輪共 3 次計分誤判（英文措辭、「E = 42」格式、regex 漏配），全靠數字對帳鐵律抓回——LLM 產出的評分器 fixture 本身就是需要 verify 的產物。

## §3 官方文深挖落地（本 session 完成）

- fusion §4 +2 條：行為級驗收（evaluator 主動探測 > 讀 diff）、sidekick 間接 untrusted 鏈。
- security-hygiene：環境層現況誠實揭露（hooks ≠ sandbox）+ hooks 變更入 Boundary Checks（trust-before-execution）。
- autoload-evolution：每 cycle 顯式「能力提升刪減檢查」（防單向棘輪）。
- autoload 2 澄清句（@AGENTS.md 隔離設計、≠auto memory）；2 點 byte 頂順延入隊列。
- model-profiles：effort 搭配指南（n=3）升格入 L2 SSoT。

## §4 Session 全程 insights（跨任務）

1. **Fable-low 的定位**（3 輪）：正確率 = opus 任一檔、廣度更高、成本低於 opus——lead/審查類任務 fable-low 是甜蜜點；這也解釋 Fusion lead 架構為何成立。
2. **「真實會用不代表有價值」的三個實例**：高頻注入 hook 無攔錯實績（價值待證）、零使用 gate skill（價值成立）、缺遙測被誤標 RETIRE 的主力 skill（量測缺陷）。
3. **權限分類器兩次正確攔截**：git clean -f 波及範圍、settings.json wiring 自我修改——確定性邊界攔 LLM 判斷失誤的活案例（判斷 vs 決定公理在平台層的體現）。
4. **KYU T1 前置掃描的實際命中率**：優化批次 4 盲點預測，2 個真實發生（InstructionsLoaded 不支援、settings 衝突）且 fallback 預置生效——盲點掃描的 ROI 可量測。
5. **byte 貼頂是治理壓力測試**：K5/F1 兩次 cycle 都被迫先騰位再加句——「加規則必先刪等量」的實質預算紀律開始生效。
