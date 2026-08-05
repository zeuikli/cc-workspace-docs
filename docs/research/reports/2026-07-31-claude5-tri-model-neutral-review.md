# Claude 5 三模型中立總評（第二輪：整體狀態，非修正驗收）

> 方法：Fable 5 / Opus 5 / Sonnet 5 各一 fresh-context sub-agent，唯讀全 repo、親跑量測、允許不同意先前稽核報告。parent 對帳：三方回報之 19,858 bytes / healthcheck 248-0-0 / GATE PASS 與 parent 親跑一致；Opus 報告的 clause-manifest 缺陷經 parent 親驗屬實（見 §3）。
> 標籤：判斷部分 assisted_verified_success；§3 缺陷為 CONFIRMED（parent 機械重驗）。

## 1. 三方總體判詞（一句版）

- **Fable 5**：結構健康、代謝過旺——內部風險低、外部效益未證；整套優化迴圈的 oracle 是「harness 內部一致性」而非「真實工作成果」。
- **Opus 5**：工程成熟度遠高於平均、但已進入「維護自身」臨界點；風險已從「規則不夠嚴」轉移到「綠燈牆本身未被資格化」。
- **Sonnet 5**：健康、但重心正在往內偏——治理 harness 本身已是比用 harness 做事更大的活動量。

三方在「強」上完全一致：enforcement 名實對齊機制、撤回/降級文化、確定性閘門真實可親跑，皆屬同類系統前段班。三方在「憂」上也收斂到同一族：**系統對自己的量測，沒有經過它要求別人經過的資格考。**

## 2. 三方獨立收斂的核心診斷：oracle 未資格化 + 維護反噬

- **Fable**：248 項 healthcheck 零項量測「掛著這套 harness 的 agent 在真實任務上是否更好」——整套系統缺 outcome oracle，所有剪枝與進化都在對未資格化的 proxy 最佳化。
- **Opus**：healthcheck 從未被 mutation 稽核過（「拿掉功能它會不會轉紅」），並抓到存在證明（§3）；`harness-share.py` 報 13.3% 是被 cron 語料稀釋的數字，扣除自動抓取後 harness 實質占比 **57.5%**——70/30 定位實測已倒轉。
- **Sonnet**：24h 內 39 commits 近半為 auto-sync/telemetry；無任何指標在量「維護 vs 任務」占比；「治理系統的治理系統」遞迴無人問值不值。

## 3. Opus 發現、parent 已證實的缺陷（本輪唯一 CONFIRMED 缺陷）

`scripts/build-clause-manifest.py:115`：`if c.get("class") == "E" and c.get("body")` ——凡 `[E]` 條文未在 `clause-body-map.json` 登記 body（section 繼承者皆如此），檢查直接跳過。實測 map 只有 11 筆 override（P=6/E*=3/E=2），manifest 統計的 19 條 `[E]` 中**僅 2 條真的驗過 Body 路徑**，healthcheck 卻顯示「[E] clause 的 Body 皆存在 PASS」。

- 定性：`core.md §Framework Integrity`「宣稱 enforcement 者必有驗證」的違反，發生在稽核鏈自身；屬真實失效（moratorium 例外可修）。
- 影響：所有引用「build-clause-manifest PASS」為收據的結論（含兩輪稽核報告對帳段）該項應視為 provisional。
- 修法：補齊 17 條 `[E]` 的 body 登記後移除 `and c.get("body")` 短路；預期副作用＝部分 `[E]` 會現形為只有 advisory 支撐、需降 `[E*]`（E:E* 比例會變難看——這是修正不是退步）。

## 4. 三方「只做一件事」建議（互補非互斥，優先序為 parent 合成）

1. **（Opus，與 §3 直接相連）healthcheck mutation 稽核**：對每個檢查項注入已知壞狀態驗它會轉紅，vacuous 項列管。現成方法＝`hook-mutation-test.py` 擴用。這件事同時修 §3 並把「綠燈牆未資格化」變成可追蹤數字。
2. **（Fable）建立外部 outcome oracle**：凍結 harness 面積，挑 5–10 個真實任務記 outcome log——讓「harness 是否值得」第一次有非自指證據。
3. **（Sonnet）量 30 天 commit 任務/維護占比**：低於自訂門檻即凍結維護預算，優先處理 description 第二座稅與 CLAUDE.md 雙重注入。

三者的邏輯順序：先讓量尺可信（1）→ 再量真正該量的東西（2、3）→ 才輪到繼續剪枝。

## 5. 待裁決積壓（延續上輪 §4，兩輪皆點名者標 ★）

- ★ `verification-waiver-gate.sh`：證據基礎已撤回（n=2），仍在掛且無到期日。
- ★ `taste-reference-lint.sh` 路徑錯配（名實落差大於已退役兩支）。
- ★ advisory 治理制度化：「30 天觀察期滿無真實觸發自動退役」；退役後回掛條件需獨立觀察管道（LESSONS 明文寫入回掛檢視程序）。
- `loop.md §L5` 自認無補 Body 路徑，依規已達可剪門檻。
- `harness-share.py` 增設「auto-generated feed」第三分類，防 cron 語料永久稀釋分母。
