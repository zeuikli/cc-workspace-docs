# wBlock URL Filter Phase 2 — URLFilterCoordinator

Date: 2026-07-16

## Summary

Implemented `URLFilterCoordinator`, an app-side wrapper around `NEURLFilterManager`
(macOS 26 / iOS 26+ only), plus a unit test file exercising it via a
`URLFilterManaging` protocol seam (no real dev-signed container available in
this environment).

## Files

- `wBlockCoreService/URLFilter/URLFilterCoordinator.swift` (new, 305 lines)
  - `URLFilterCoordinatorError` — named error enum mapping `NEURLFilterManager.Error`
    rawValues (0 configurationUnchanged ... 13 unknown) to `.permissionDenied`,
    `.extensionUnavailable`, `.configurationFailed`, `.notConfigured`, `.other`.
  - `URLFilterCoordinatorStatus` — coordinator-facing status incl. `.unavailable`
    for unreachable/unknown states.
  - `URLFilterPIRConfiguration` — caller-supplied PIR endpoint value type;
    `pirServerURL` required, no default production endpoint anywhere in this file.
  - `URLFilterManaging` protocol + `NEURLFilterManager: URLFilterManaging`
    conformance — testing seam.
  - `URLFilterCoordinator` — `configure(with:)`, `enable()`, `disable()`,
    `currentStatus()`; `isConfigured` gate prevents `enable()` before a PIR
    endpoint has been supplied; `configurationUnchanged` (0) treated as
    non-error; fail-open only, no `shouldFailClosed` toggle exposed.
  - `URLFilterAvailability.isSupported` — runtime `#available` check usable
    from any deployment target without referencing the coordinator type.
- `wBlockCoreService/URLFilter/URLFilterCoordinatorTests.swift` (new, 244 lines,
  12 `func test*`) — not compiled (XCTest module unavailable under bare
  `swiftc -typecheck` in this environment), verified structurally.

## Deviations

- **No SwiftUI settings view added.** Brief allowed a new UI file (`wBlock/`)
  or additive edit to an existing view, but did not make it part of
  Done-when (Done-when items 1–7 cover only the coordinator + tests + report).
  Given the coordinator is the load-bearing deliverable and the constraint
  set (no pbxproj edits — Constraint 8/Non-goals) means a new UI file cannot
  be added to the app target's build phases in this session anyway, I
  prioritized a fully-verified coordinator over a UI file that could not be
  build-verified and risked violating "don't touch pbxproj." No UI file was
  created. Flagging as an open question below rather than silently
  shipping unverifiable UI code.

## Verification

### Done-when #1 — macos26.0 typecheck, non-test files (exit 0 required)
```
$ swiftc -typecheck -sdk $(xcrun --show-sdk-path) -target arm64-apple-macos26.0 \
    GroupIdentifier.swift URLFilter/BloomEntryExtractor.swift URLFilter/MurmurHash3.swift \
    URLFilter/URLFilterConversionStats.swift URLFilter/PrefilterBuilder.swift URLFilter/URLFilterCoordinator.swift
EXIT:0
```
[claim:verified]

### Done-when #2 — macos12.3 typecheck, non-NE files (exit 0 required, regression check)
```
$ swiftc -typecheck -sdk $(xcrun --show-sdk-path) -target arm64-apple-macos12.3 \
    MurmurHash3.swift URLFilterConversionStats.swift BloomEntryExtractor.swift
EXIT:0
```
[claim:verified]

### Done-when #3 — `@available(macOS 26.0, iOS 26.0, *)` count ≥ 1
```
$ grep -c "@available(macOS 26.0, iOS 26.0, \*)" URLFilterCoordinator.swift
6
```
[claim:verified]

### Done-when #4 — `GroupIdentifier` reference present
```
$ grep -E "GroupIdentifier" URLFilterCoordinator.swift
    /// existing `GroupIdentifier` singleton — never hardcoded here.
    public var appGroupIdentifier: String {
        GroupIdentifier.shared.value
```
[claim:verified]

### Done-when #5 — zero hardcoded `group.skula.wBlock`
```
$ grep -c -E "group\.skula\.wBlock" URLFilterCoordinator.swift
0
```
[claim:verified]

### Done-when #6 — test function count ≥ 6, edge cases covered
```
$ grep -c "func test" URLFilterCoordinatorTests.swift
12
```
Edge cases covered (of the 5 listed in the brief, all 5 addressed):
1. Extension not found/failed to load → `testExtensionNotFoundIsMappedToExtensionUnavailable`,
   `testExtensionFailedToLoadIsMappedToExtensionUnavailable`.
2. `configurationPermissionDenied` → `testPermissionDeniedIsMappedToPermissionDeniedCase`.
3. `configurationUnchanged` non-error → `testConfigurationUnchangedIsNotSurfacedAsError`.
4. Empty prefilter / not-configured state → `testEnableThrowsNotConfiguredWithoutPriorConfigure`
   (coordinator-level analog: "no usable input" must not silently proceed).
5. Status query without crash → `testCurrentStatusMapsKnownSDKStatusValues`,
   `testCurrentStatusNeverThrowsOnStoppedState`.
[claim:verified] (structural grep count) — [claim:asserted] (test bodies correct;
not compiled/run, XCTest module unavailable under bare `swiftc -typecheck`,
per known environment limitation stated in brief).

### Done-when #7 — this report
Written to `research/reports/2026-07-16-wblock-urlfilter-phase2-coordinator.md`. [claim:verified]

## API facts used (from macOS 26 SDK swiftinterface, re-verified independently this session)

Source: `/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/NetworkExtension.framework/Versions/A/Modules/NetworkExtension.swiftmodule/arm64e-apple-macos.swiftinterface`, lines 171-259.
Matches lead-provided facts exactly: `setConfiguration` signature, `Error` rawValue
ordering (0 configurationUnchanged … 13 unknown), `Status` enum, `shouldFailClosed`,
`saveToPreferences`/`loadFromPreferences`/`resetPIRCache`, `handleStatusChange()`
AsyncSequence. [claim:verified] via `grep -n "NEURLFilter"` + direct file read of
that swiftinterface, this session.

## Open Questions

- No SwiftUI settings UI was added (see Deviations). If Phase 2 scope should
  include a minimal settings section, it needs a follow-up task — cannot be
  build-verified without pbxproj changes (out of this phase's Allowed-paths).
- `URLFilterCoordinatorTests.swift` cannot be compiled/run in this environment
  (XCTest module absent under bare `swiftc -typecheck`) — verified structurally
  only, consistent with brief's stated known limitation.

## Verification hints for lead

- Orthogonal check: `grep -n "shouldFailClosed" wBlockCoreService/URLFilter/URLFilterCoordinator.swift`
  should return zero hits (fail-open-only constraint).
- Spot-check: confirm `configure(with:)` is the *only* call site of
  `manager.setConfiguration` in the new file (no secondary path that could
  bypass the `pirServerURL` requirement).
- If Xcode project available: attempt real XCTest run of `URLFilterCoordinatorTests`
  once module resolution is available, to upgrade edge-case claims from
  asserted to verified.
