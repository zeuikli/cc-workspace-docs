# core.md 下沉決議 — Fable/Opus/Sonnet/Haiku 四模型審議報告

> 2026-07-19 · 主席/終審：Fable（主對話）· 提案：Opus（架構視角）/ Sonnet（執行者視角）/ Haiku（最弱讀者視角）/ Fable · 互評：Opus ↔ Sonnet 交叉投票（對抗立場，先試反駁）
> 議題：`.claude/rules/core.md` 是否有內容可刪除、調整或下沉至其他規則檔。

## 1. 流程

1. 三 agent 各自獨立 context 讀六源 auto-load + refs + HARNESS-CORE-v4，以不同 lens 提案（架構分層／執行者常駐需求／弱讀者可讀性）；Fable 自提第四份。
2. Round 2：Opus 與 Sonnet 對彼此及 Haiku/Fable 提案逐項 CONFIRM/REJECT（盲於終審傾向）。
3. Fable 終審：計數化裁決（非平均分），落地 + 量測。

## 2. 決議總表

| # | 提案 | 提案者 | 投票 | 裁決 | bytes |
|---|------|--------|------|------|-------|
| 1 | Framework Integrity 整段下沉 `prompt-lifecycle.md`（path-scoped，編輯規則時載入），core.md 留 1 行指針 | Opus+Sonnet+Fable | 3 CONFIRM | **採納** | −700 |
| 2 | 「壓縮可翻轉決策」跨檔去重：刪 core.md 側、保 context-management 側 | Opus | Sonnet CONFIRM；Fable 原主張反向、被說服 | **採納**（放在被約束操作旁 > 孤懸跨切清單） | −90 |
| 3 | 儀式深度修剪：刪「六階段是思考框架非輸出格式」，保「隨風險不隨檔位」不變式 + 全構件觸發清單 | Opus | Sonnet CONFIRM | **採納**（部分：保留觸發清單） | −50 |
| 4 | taste 有界括號縮短 | Fable | Opus+Sonnet CONFIRM | **採納** | −60 |
| 5 | 「（正式 spec 走 /spec-implement）」刪除（RESOLVER 已為 canonical 路由） | Fable | Opus+Sonnet CONFIRM | **採納** | −30 |
| 6 | context-management §監控刪 `/usage` 指令前導、保行為信號句 | Sonnet | Opus CONFIRM | **採納** | −40 |
| 7 | subagent fan-out 刪 error-handling.md 冗餘指針 | Sonnet | Opus weak CONFIRM | **採納** | −35 |
| 8 | 地圖≠疆域公理修剪為 4 字 tag | Opus | Sonnet REJECT + Fable REJECT | **否決**：主對話自發啟用 Unknowns 紀律的動機來源，非裝飾 | 0 |
| 9 | 下沉核心公理（判斷vs決定/雙軸/地圖≠疆域）「理論不影響行為」 | Haiku | Opus+Sonnet+Fable REJECT | **否決**（見 §3 關鍵裁決） | 0 |
| 10 | Johari 四象限下沉 research/ | Haiku | 2 REJECT（Sonnet 軟化為「可再壓不可移」） | **否決**：IDENTIFY 現役決策程序，非背景理論 | 0 |
| 11 | 下沉 角色≠檔位單調/廣度深度/對抗立場 | Haiku | 2 REJECT | **否決**：主對話即 dispatcher/judge，此為其本職規則 | 0 |
| 12 | 十項歧義措辭量化改寫 | Haiku | 2 REJECT（bytes 淨增、違「壓縮=刪除非改寫」） | **否決**；替代路徑：清單存本報告 §4，未來 cycle 逐項評估入 `judgment-rubrics.md`（on-demand） | 0 |

落地量測：六源 `wc -c` **18,943 → 18,237B（−706B, −3.7%）**；healthcheck FAIL=0、`measure.sh --gate` PASS。

**Gate 衝突調整（落地時發現，決議範圍縮小）**：`measure.sh --gate` 以確定性錨點驗 ① `wc -c` 量測命令必須留在 core.md（三源矛盾防線 SSoT）② `Token Budget（軟性參考` 字面錨在 context-management.md。決議 #1 與 #6 原範圍會拔除這兩個錨——依「確定性閘門不弱化」原則，量測命令留在 core.md Framework Integrity 指針行、`（軟性參考）`措辭恢復；其餘照決議下沉。此為 L3 機械 gate 壓過 L1 審議結論的正確優先序實例。

## 3. 關鍵裁決：受眾判定（H1–H3 否決理由，具檔案價值）

Haiku 主張下沉公理與委派規則，理由「理論不改變我的行為」。否決依據：
- **auto-load 的受眾是主對話**（quality/frontier 檔位）；sub-agent **不繼承** auto-load，靠 Handoff Contract 取得 context。cost 檔位視角的「我用不到」不構成下沉理由——它根本讀不到這份檔。
- 公理（判斷vs決定/雙軸伸縮）正是主對話**做委派與驗證決策**的依據；Johari 是 IDENTIFY 的現役程序；對抗立場是互審的行為閘。
- 此裁決本身是**雙軸伸縮的實證**：同一份規則，弱檔讀來是「不可操作的理論」、主對話讀來是決策邏輯——程序性指導對弱檔要更具體（由 Handoff Contract 承載），不是把主對話的判斷框架刪掉。

## 4. Haiku 歧義措辭清單（保存供未來 judgment-rubrics 評估；不入 auto-load）

「會改變架構的題」判準、「不清楚」門檻、「廉價確定性檢查」定義、「少量機械編輯」門檻、「重要交付」列舉、「詮釋非複述」定義、「缺陷 re-handoff vs 親改」界線、「順手修」界線、`/rewind` 可用性 fallback、N commit 查點指針化。逐項評估原則：量化若增 auto-load bytes 即下沉 refs；已有 profile/rubric 承載者改指針。

## 5. 觀察（方法論）

- 三 lens 分工有效：Opus 找到分層違規（Framework Integrity 自我宣告「非執行面」卻常駐）；Sonnet 提供「常駐 vs 按需」的執行者實感並成為 H 系列最強反方；Haiku 的誤讀本身即資料（歧義清單 + 受眾判定實證）。
- 對抗互評改變了終審立場一次（#2 方向）——同 context 自審不會發生這件事。
- TEST/APPLY 閘門區四方零提案觸碰，與「驗證閘門只加嚴不放鬆」一致。
