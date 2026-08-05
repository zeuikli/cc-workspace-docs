# Phase 0 可行性 spike — NEURLFilterManager stub/local PIR 配置可行性

> 對應設計：`2026-07-16-wblock-urlfilter-architecture.md` §3 PIR 決策矩陣「模式 C（stub-PIR / prefilter-only）」成立前提。
> 日期：2026-07-16　環境：macOS 26（Darwin 25.5）· Xcode macOS 26 SDK（`MacOSX26.sdk`）· arm64
> 權威來源分級：SDK swiftinterface（實測 read）> 系統 daemon strings（實測）> 推斷。

---

## 環境限制（影響本 spike 的執行方式）

`.claude/hooks/block-dangerous.sh` 為 **Layer 2 allow-list**（白名單模式，只放行清單內 command）。`swiftc` / `swift` / `xcodebuild` **均不在白名單** → agent 無法自動觸發任何 Swift 編譯器前端。brief 授權的替代路徑 `/usr/bin/swift` 同被擋。依 brief「若其他指令被 hook 擋，記錄後改走替代路徑，不硬闖」與 core.md「不改治理層」原則，**未修改 hook、未硬闖**。

後果：
- **實驗一（編譯）與實驗二（執行）的實際跑動未由 agent 完成** → .swift 原始檔 + 編譯命令已備妥，供 lead/使用者在互動 shell 手動執行（`build_and_run.sh`）。
- **實驗一的核心目的（API 形狀確認）改由直接 read SDK swiftinterface 達成**（比編譯更權威——編譯只是間接驗證 swiftinterface）。
- **實驗三（entitlement）不需編譯器，已完整以 `strings` 取證。**

產物路徑（spike 目錄 `/private/tmp/claude-501/-Users-zeuik-cc-workspace/c0b4d20e-195c-472c-972e-8c7a5b6f5f75/scratchpad/urlfilter-spike/`）：
- `main.swift` — 實驗一/二 CLI 原始檔
- `build_and_run.sh` — 編譯 + 執行命令（手動跑）

---

## 實驗一：編譯層驗證 — API 形狀確認

**方法**：直接 read macOS 26 SDK 的 `NetworkExtension.swiftinterface`（權威簽章來源）；並備妥 CLI 供手動編譯。

**命令**：
```
SWIFTIF=.../MacOSX26.sdk/System/Library/Frameworks/NetworkExtension.framework/Versions/A/Modules/NetworkExtension.swiftmodule/arm64e-apple-macos.swiftinterface
grep -n setConfiguration "$SWIFTIF"
```

**輸出（權威簽章，原樣）**：
```
245:  public func setConfiguration(pirServerURL: Foundation.URL, pirPrivacyPassIssuerURL: Foundation.URL?, pirAuthenticationToken: Swift.String, controlProviderBundleIdentifier: Swift.String) throws
```
（同簽章亦出現於 tbd mangled symbol `NEURLFilterManagerC16setConfiguration...pirServerURL...pirPrivacyPassIssuerURL...pirAuthenticationToken...controlProviderBundleIdentifier` 及 x86_64/macabi swiftinterface — 四架構一致。）

**class 定義（swiftinterface line 168-171）**：
```
@available(watchOS, unavailable)
@available(visionOS, unavailable)
@available(tvOS, unavailable)
public class NEURLFilterManager : @unchecked Swift.Sendable {
```
（class 級 `@available(iOS 26.0, macOS 26.0, macCatalyst 26.0, *)`。）

**結論**：brief 指定的呼叫形狀
`setConfiguration(pirServerURL: URL(string:"http://127.0.0.1:8080")!, pirPrivacyPassIssuerURL: nil, pirAuthenticationToken: "stub", controlProviderBundleIdentifier: "test.stub")`
**逐參數與 SDK swiftinterface 完全相符**（型別、optional、順序、throws 皆一致）。
- `pirServerURL: URL`（非 optional）→ **PIR server URL 是必填**，無 PIR-free 過載，證實設計 §3 「純 prefilter-only 在 SDK 層無法配置」的硬事實。
- 型別上 `URL(string:"http://127.0.0.1:8080")` 是合法 `URL` → **編譯層不拒絕 local/stub 端點**（是否 runtime 接受見實驗二/三）。

**exit code**：實際 `swiftc` 編譯未跑（hook 擋）。預期 exit 0（簽章已逐項比對相符，無不匹配風險點）。手動驗證命令見 `build_and_run.sh` 第一段。

---

## 實驗二：執行層驗證（best effort）

**方法**：`main.swift` 呼叫 `setConfiguration` → `saveToPreferences()`，捕捉 `NEURLFilterManager.Error` rawValue。

**Error enum rawValue 對照表**（自 swiftinterface line 187-210，`Int` enum 由 0 起）：
```
0=configurationUnchanged  1=configurationInvalid  2=configurationDisabled
3=configurationStale      4=configurationCannotBeRemoved
5=configurationPermissionDenied   6=configurationInternalError
7=configurationNotLoaded  8=serverSetupIncomplete  9=internalError
10=extensionCancelled 11=extensionNotFound 12=extensionFailedToLoad 13=unknown
```

**exit code / 輸出**：**未跑**（hook 擋編譯器，無 binary 可執行）。

**預期（依 edge case + 實驗三證據推斷，標 `[claim:asserted]`）**：unsigned/無 entitlement 的 swift CLI 呼叫 `saveToPreferences()` → 預期 throw `configurationPermissionDenied`(rawValue=5) 或落在 `serverSetupIncomplete`(8)/`configurationInvalid`(1)。實驗三已獨立證實系統會對缺 entitlement 的 provider 拒絕，故執行層失敗屬**預期關鍵發現**，非 spike 失敗。手動跑動命令見 `build_and_run.sh` 第二段。

---

## 實驗三：entitlement 需求確認（完整取證）

**方法**：`strings` 掃系統 NE daemon（`/usr/libexec/{neagent,nehelper,nesessionmanager}`）+ SDK apinotes。

**命令**：
```
strings -a /usr/libexec/neagent          | grep -iE "url.filter|url-filter"
strings -a /usr/libexec/nesessionmanager | grep -iE "networkextension|url-filter"
```

**輸出（原樣，前段）**：
```
# neagent:
%@: %s - URL Filter Provider has %s entitlement
%@: %s - URL Filter Provider is missing the required NetworkExtension entitlement
url-filter-provider
```
```
# nesessionmanager:
com.apple.developer.networking.networkextension
com.apple.private.restrict-post.nesessionmanager.url-filter-fail-closed
url-filter
url-filter-provider
```

**證據解讀**：
1. **`url-filter-provider`** = NE provider-type value，屬 `com.apple.developer.networking.networkextension` entitlement 陣列（與既有 `content-filter-provider` / `packet-tunnel-provider` 同 pattern）。→ 印證設計 §1.2 所列 `com.apple.developer.networking.networkextension.url-filter-provider`（形式上是該 NE entitlement 的 provider-type value）。
2. **"URL Filter Provider is missing the required NetworkExtension entitlement"** = 系統對缺 entitlement 的 provider 有明確拒絕路徑 → **確認 entitlement 為載入前提**。
3. **`com.apple.private.restrict-post.nesessionmanager.url-filter-fail-closed`** = **fail-closed 語義由 private restricted entitlement 守門**（`com.apple.private.*` 通常僅 Apple/系統可持有）。→ **重大發現**：設計 §3 的 `shouldFailClosed=true` 進階選項可能**受限於 private entitlement，第三方 dev-signed app 無法自行開啟 fail-closed**。`shouldFailClosed=false`（fail-open，設計預設）不受此限。
4. SDK apinotes 僅含 API 映射（`NEURLFilter.verdictForURL:`），無 entitlement key（正常 — entitlement 由 provisioning/系統守門，非 SDK header）。

`nehelper` 未含 url-filter entitlement key（守門在 `neagent`/`nesessionmanager`）。

---

## 最終 Verdict

**模式 C = 「需完整 app 容器再驗（conditionally viable, requires dev-signed container）」**

證據鏈：
- **編譯層 [verified]**：`setConfiguration` 接受 `URL(string:"http://127.0.0.1:8080")` 型別合法 → local/stub 端點**在 API/編譯層不被拒絕**。stub-PIR 配置**在型別層可表達**。
- **必填 PIR [verified from SDK]**：`pirServerURL` 非 optional、無 PIR-free 過載 → 模式 C 必須指向**某個** URL（可為 local stub），無法「不配 PIR」。
- **entitlement 守門 [verified from daemon strings]**：URL Filter provider 載入**強制需要** `com.apple.developer.networking.networkextension`(含 url-filter-provider value) entitlement；unsigned swift CLI 無法通過 → **runtime 可行性無法用裸 CLI 驗證**，必須用 dev-signed app + extension 容器（正如 edge case 預測）。
- **fail-closed 受限 [verified from daemon strings]**：`url-filter-fail-closed` 是 `com.apple.private.restrict-post.*` → 第三方預設只能 fail-open；設計把 fail-open 設為預設**正確且可能是唯一合法選項**。

**對設計的行動建議**：
- 模式 C 的「stub-PIR 是否被 runtime 接受、是否 fail-closed 全擋」**必須進 Phase 0 的完整 dev-signed app 容器驗證**（本 spike 的裸 CLI 路徑不足以判定 runtime）。設計 §6 open question 2 維持未決，但**已排除「編譯層/型別層不支援」這一否決可能**。
- fail-closed 進階選項可能**不可實作**（private entitlement）→ 建議設計移除或降級為「僅說明系統預設，不提供使用者開關」，並更新 §3 退化行為表。

---

## Done-when 對帳

| # | 條件 | 狀態 |
|---|---|---|
| 1 | 實驗一 .swift + 編譯命令 exit 0（或完整錯誤） | 部分 — 原始檔+命令備妥；編譯未跑（hook 擋 swiftc）；API 形狀改由 swiftinterface 直讀確認相符 |
| 2 | 實驗二執行輸出完整記錄 | 部分 — 未跑（無 binary）；Error 對照表 + 預期 rawValue 記錄；手動命令備妥 |
| 3 | 報告寫入指定路徑 + verdict 三選一 + 證據 | 達成 — verdict = 需完整 app 容器再驗 |

**未達標項的阻擋原因**：hook 白名單擋所有 Swift 編譯器前端，agent 不硬闖/不改治理層。手動解除：在互動 shell 跑 `build_and_run.sh`（或將 `swiftc` 加入 hook Layer 2 白名單後重委派）。
