# wBlock URL Filter — Phase 1「規則轉譯層」實作報告

> 對應設計：`2026-07-16-wblock-urlfilter-architecture.md` §4 規則轉譯層 spec。
> 對應 spike：`2026-07-16-wblock-urlfilter-phase0-spike.md`（`NEURLFilterPrefilter` API 事實來源）。
> 日期：2026-07-16　實作範圍：`wBlockCoreService/URLFilter/` 新目錄，4 個實作檔 + 1 個測試檔，共 992 行。
> **✅ 2026-07-16 更新（編譯驗證已補齊，本聲明的限制已解除）**：hook 白名單於同日加入 Swift 工具鏈（使用者核可）後，lead 親跑 `swiftc -typecheck` 對本 Phase 全部四個源檔驗證：
> - `swiftc -typecheck -sdk $(xcrun --show-sdk-path) -target arm64-apple-macos12.3 MurmurHash3.swift URLFilterConversionStats.swift BloomEntryExtractor.swift` → **exit 0**
> - `swiftc -typecheck -sdk $(xcrun --show-sdk-path) -target arm64-apple-macos26.0 ../GroupIdentifier.swift MurmurHash3.swift URLFilterConversionStats.swift BloomEntryExtractor.swift PrefilterBuilder.swift` → **exit 0**
> - 環境：Swift 6.3.3（swiftlang-6.3.3.1.3）· target arm64-apple-macosx26.0
>
> **§4 所列四個風險點全數退休**（無一成真）：`NEURLFilterPrefilter` 呼叫簽章正確、`PrefilterData` case 名稱正確、`MurmurHash3` 位元運算語法通過、`SHA256State` 無 ambiguity。**此結論在型別層成立且經真實 xcodebuild 覆核仍成立**。
>
> ⚠️ **2026-07-16 二次更正（狀態標籤下修，原宣稱過度樂觀）**：本報告初版曾據 `swiftc -typecheck` 將狀態升為 `autonomous_verified_success`。**該升級是錯的**——同一批產物在真實 `xcodebuild` 下 **BUILD FAILED (EXIT=65)**：本 Phase 的 `URLFilterConversionTests.swift` 被放在 `wBlockCoreService/URLFilter/`（**源碼**目錄），Xcode 將其編入非測試 target → `error: unable to resolve module dependency: 'XCTest'`。已修（測試移至 `Tests/wBlockCoreServiceTests/`），現況 mac + iOS 雙平台 `xcodebuild` 皆 **BUILD SUCCEEDED**。
> **狀態標籤 = `assisted_verified_success`**（非 autonomous）。
> **仍未驗**：① 執行期行為（需 dev-signed 容器 + macOS 26 實機，見 phase0 verdict）；② **本 Phase 的 19 個測試從未執行**——wBlock 無任何 test target（`productType unit-test` 零命中），測試不被任何 target 編譯，「19 test case」僅為結構級存在。建立 test target 屬 pbxproj 手術 → Phase 3。
> **教訓**：`swiftc -typecheck <手選檔案>` 是 `xcodebuild` 的**代理指標非替代品**——它不驗 Xcode target 如何組裝來源目錄。詳見 process log 步驟 31-33。
>
> ~~**未編譯聲明**（歷史記錄，已失效）：本 Phase 環境的 PreToolUse hook（Layer 2 allow-list）擋所有 Swift 編譯器前端（`swiftc`/`swift`/`xcodebuild` 均不在白名單），與 Phase 0 spike 遇到的限制相同。依 brief 授權，**未嘗試繞過**；本 Phase 全程以結構級檢查（`ls`/`grep`/人工 read）替代編譯驗證。所有程式碼**未經 Swift 編譯器驗證**，可能含編譯期才會浮現的型別/語法錯誤。~~

---

## 1. 模組職責

| 檔案 | 行數 | 職責 |
|---|---|---|
| `wBlockCoreService/URLFilter/BloomEntryExtractor.swift` | 321 | AdGuard 規則文字 → `Set<BloomEntry>`（可轉條目）+ `Set<String>`（exception host）+ `URLFilterConversionStats`。純字串處理，無 NE 依賴，無 `@available` 限制（可在 macOS 12.3 部署目標編譯）。 |
| `wBlockCoreService/URLFilter/PrefilterBuilder.swift` | 284 | `Set<BloomEntry>` + exception 差集 → `PrefilterBlob`（bitCount/hashCount/murmurSeed/bitmap）→ 包裝為 `NEURLFilterPrefilter`（`.smallFilter`/`.temporaryFilepath` 依大小門檻選擇）。整個 `enum` 標 `@available(macOS 26.0, iOS 26.0, *)`（依賴 `NetworkExtension` 的 `NEURLFilterPrefilter`/`PrefilterData`）。 |
| `wBlockCoreService/URLFilter/MurmurHash3.swift` | 98 | 自含 MurmurHash3 x86_32 實作（不引第三方套件），對應 `NEURLFilterPrefilter.murmurSeed: UInt32`。 |
| `wBlockCoreService/URLFilter/URLFilterConversionStats.swift` | 105 | Public `URLFilterConversionStats` struct + `URLFilterSkipReason` enum（cosmetic/scriptlet/exception/pattern/modifier/notARule/malformed），供 UI 顯示轉譯覆蓋率。 |
| `wBlockCoreService/URLFilter/URLFilterConversionTests.swift` | 184 | 19 個 `func test...`（Done-when 要求 ≥8，達 19；覆蓋每個 edge case 至少一個）。 |

**設計慣例對齊**（鏡像 `RemoveParamDNRRuleGenerator`，非 brief 要求但 architecture doc §0/§7 明確建議）：
- 保守跳過而非放寬：任何無法**精確**表達的規則（wildcard/regex/modifier/cosmetic/scriptlet）一律跳過並計數，不做近似轉換。
- Public API 附 doc comment；統計結構供 UI 使用；不引入第三方套件（`RemoveParamDNRRuleGenerator` 只用 CryptoKit + Foundation，本模組同）。

---

## 2. AdGuard 語義決策摘要

### 2.1 `||` 前綴的子網域語義（brief edge case，需查證後決定）

**查證結果**：AdGuard 官方語法文件「How to create your own ad filters」記載 `||` domain-anchor 修飾符語義為「匹配該網域**及其所有子網域**」（例：`||example.org^` 攔截 `example.org` 與所有子網域，但不攔截 `notexample.org`）。`[claim:asserted — 依 phase0/architecture 文件既有引用的 AdGuard 語法慣例，本 session 未重新拉取 AdGuard 官方文件原文逐字核對]`

**本模組的實作決策（記於 `BloomEntryExtractor.swift` doc comment）**：Bloom filter 是扁平集合成員測試，**無法**表達「該網域及其所有子網域」這種前綴/樹狀語義（唯一手段是逐一列舉已知子網域，或改用 suffix-matching 方案，兩者皆超出 Phase 1 範圍）。因此 `||example.com^` 只轉換出**精確**條目 `example.com`（不合成 `www.example.com` 等變體）。

**理由與風險評估**：
- 這是「保守 under-block」而非「放寬 over-block」——與 core 原則「不確定即跳過、不放寬」一致方向。真實子網域（如 `ads.example.com`）除非規則清單另有一行明確列出，否則不會被此條目攔截。
- 反方向（合成子網域變體塞進 Bloom）會製造**silent over-block**：任何字面上未出現在規則裡的子網域字串一旦被合成插入集合，且 Prefilter-only 模式（架構 §3 模式 C）無 PIR 二次確認，false positive 無法挽回——此風險高於 under-block。
- **記為 open question**：若 upstream maintainer 認為 under-block 覆蓋率損失過大，Phase 2/3 可考慮「規則展開」策略（於轉譯前對已知規則清單做 offline 子網域枚舉），不在本 Phase 解決。

### 2.2 host 大小寫正規化

- `normalizeHost` 統一 `lowercased()`。理由：DNS host 大小寫不敏感，`NEURLFilterPrefilter` 是逐位元組雜湊比對，若不正規化，`Example.com` 與 `example.com` 會產生不同雜湊而漏判。`[claim:asserted — 依 DNS RFC 常識與 Bloom exact-match 特性推斷，未在 SDK 文件中找到明文大小寫正規化聲明；風險：若系統端 verdict 查詢時的 host 正規化方式與此處不同，仍可能不匹配，留待 Phase 2/3 對 verdict(for:) 實際輸入做端到端驗證]`

### 2.3 IDN / punycode

- 非 ASCII host 經 `URL(string:)` 建構觸發 Foundation 內建 IDNA 正規化，取得 punycode（`xn--` 前綴）ASCII-Compatible Encoding 形式，避免手刻 punycode 演算法。`[claim:asserted — 依 Foundation URL host 正規化行為的一般認知；未在本 session 實際執行驗證（swiftc 被擋），無法確認 URL(string:) 在所有 macOS/iOS 版本上對非法 Unicode host 的容錯行為，尤其是否對某些邊界字元組合回傳 nil 而非 punycode]`

### 2.4 空規則集

- `BloomEntryExtractor.extract(from: "")` 回傳空 `entries`/`exceptions` + `stats.totalLines == 0`（不 crash，`coverageRatio` guard 除以零回 0）。
- `PrefilterBuilder.buildBlob` 對「差集後條目集合為空」（含全部被 exception 排除的情況）回傳 `nil`，而非空位圖——對應 brief edge case「空規則集應回 nil prefilter 而非空位圖」。`recommendedParameters(entryCount: 0)` 亦回 `nil`（避免除以零/退化位圖大小）。

---

## 3. 轉譯覆蓋率估算方法（依 architecture doc §4.3）

1. 對每張規則清單呼叫 `BloomEntryExtractor.extract`，取得 `URLFilterConversionStats`。
2. `coverageRatio = convertedCount / totalLines`（單清單）；跨清單聚合時建議**加總分子分母後再除**（避免小清單偏誤），已於 `URLFilterConversionStats.coverageRatio` doc comment 明確記錄此建議，未在本 Phase 實作跨清單聚合器（屬 Phase 2 UI 整合範圍）。
3. 跳過原因細分統計見 `skippedByReason: [URLFilterSkipReason: Int]`（cosmetic/scriptlet/exception/pattern/modifier/notARule/malformed）。
4. Bloom 誤判率估算：`recommendedParameters(entryCount:targetFalsePositiveRate:)` 依 `bitCount = -(n·ln p)/(ln2)²`、`hashCount = (bitCount/n)·ln2` 公式（與 architecture doc §4.3 point 3 完全一致）。測試 `testBloomFilterFalsePositiveRateWithinBudget` 以 500 個已知條目 + 2000 個已知不存在條目實測誤判率，斷言低於寬鬆上界（測試設計為避免 flaky，非精確驗證 SDK 級誤判率——真正精確驗證需編譯後跑動，本 Phase 未達成）。

---

## 4. 未編譯聲明（重申）

- 所有 5 個檔案**從未經過 `swiftc`/Xcode 編譯**。已知風險點（人工 review 時已盡力排除，但無編譯器把關）：
  - `PrefilterBuilder.swift` 對 `NEURLFilterPrefilter(data:tag:bitCount:hashCount:murmurSeed:)` 的呼叫簽章依賴 Phase 0 spike 對 swiftinterface 的手動 read（非本 Phase 直接重新驗證），若 Phase 0 記錄有誤差，此處會編譯失敗。
  - `PrefilterData` 的 case 名稱 `.smallFilter(Data)` / `.temporaryFilepath(URL)` 同樣承襲 brief 提供的事實，未獨立重新 grep SDK swiftinterface 核對關聯型別細節（如 `PrefilterData` 是否為 nested type、`Data`/`URL` 參數是否有 label）。
  - `MurmurHash3.hash32` 的位元運算（`multipliedReportingOverflow(by:).partialValue`）語法在較舊 Swift 版本下可能有 API 差異；未編譯無法確認。
  - `SHA256State`/`Insecure.SHA256Compat` 命名為避免與 `CryptoKit.Insecure` 衝突刻意用局部 enum 包裝，未編譯無法確認無 ambiguity。
- **建議 lead 驗證方式**：於互動 shell（非 hook 限制環境）執行 `swift build`（若專案有 SwiftPM manifest）或透過 Xcode 對 `wBlockCoreService` target 做語法檢查/`xcodebuild -scheme wBlockCoreService build`；若編譯失敗，優先檢查上述四個風險點。

---

## 5. Phase 2 接點

- `URLFilterManagerCoordinator`（Phase 2 新模組）呼叫鏈預期：`FilterPreprocessor` 展開規則 → `BloomEntryExtractor.extract(from:)` → `PrefilterBuilder.buildBlob(entries:exceptions:murmurSeed:)` → `PrefilterBuilder.makePrefilter(from:temporaryDirectory:)`（`temporaryDirectory` 需改傳 App Group container URL，本 Phase 預設 `FileManager.default.temporaryDirectory` 僅供獨立測試/預覽使用）。
- `PrefilterBlob.tag` 對應 `fetchPrefilter(existingPrefilterTag:)` 的 tag 比對語義——Phase 2/3 的 `URLFilterControlProvider` 應直接讀 App Group 內已建好的 blob（本 Phase **未實作**寫入 App Group 的 I/O，只到記憶體內 `PrefilterBlob`；寫入邏輯依 architecture doc §5「轉換在 App 端完成寫入 App Group」，屬 Phase 2 範圍，brief non-goals 明確排除 `SharedAutoUpdateManager` 串接）。
- `murmurSeed` 目前由呼叫端傳入（無預設值/持久化機制）；Phase 2 需決定 seed 的產生與跨版本穩定性策略（同一清單重建 blob 時 seed 若變動會導致 tag 內容雜湊不穩定，需額外設計，本 Phase 未處理，記為 open question）。

---

## 6. Done-when 機械驗證輸出（原樣）

```
== 1 ==
BloomEntryExtractor.swift
MurmurHash3.swift
PrefilterBuilder.swift
URLFilterConversionStats.swift
URLFilterConversionTests.swift
== 2 ==
（各檔獨立 grep -c 輸出，總和 8 ≥ 2）
== 3 == PASS (smallFilter/temporaryFilepath found in PrefilterBuilder.swift)
== 4 == PASS (@@ found in BloomEntryExtractor.swift)
== 5 == URLFilterConversionTests.swift exists, 19 "func test" matches (≥8 required)
```

---

## 7. Open Questions

1. `||` 子網域語義的 under-block 取捨（§2.1）是否符合 upstream maintainer 期待，或需 Phase 2/3 補規則展開策略。
2. `normalizeHost` 大小寫正規化與 SDK 實際 `verdict(for:)` 查詢時的 host 正規化方式是否一致，未經端到端驗證（需 Phase 0 完整 app 容器測試補齊，見 phase0 報告 verdict）。
3. `murmurSeed` 的產生/持久化策略未定義（Phase 2 範圍）。
4. `.temporaryFilepath` 門檻（`temporaryFilepathThresholdBytes = 1 MiB`）為 `[claim:asserted]` 佔位值，architecture doc §4.4 已標記需 Phase 0 實測，本 Phase 未做（不可行，需編譯環境）。
5. 本 Phase 未實作跨清單覆蓋率聚合器（僅記錄聚合建議於 doc comment），留 Phase 2 UI 整合時實作。
