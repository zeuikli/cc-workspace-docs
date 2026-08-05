# Fix Patch — Kimi K2.7 C4/C5/C6

> Target: `research/reports/2026-07-09-fusion-architecture-design-plan.md`
> Author: Kimi K2.7 (worker subagent)
> Date: 2026-07-09
> Purpose: Patch file with precise old_str → new_str replacements for 3 critical issues (C4/C5/C6) identified in the 4-model cross-review of the Fusion architecture design plan.

---

## Fix C4 — GLM-5.2 / Kimi compliance risk not addressed

**Location**: §4.1 分工原則 table (GLM row + Kimi row), around line 254-255
**Action**: REPLACE two table rows AND INSERT compliance gate note after the Kimi row

**Old** (exact match, two consecutive rows):
```
| GLM | GLM-5.2（ceiling 檔,開源） | 架構設計驗證、跨 harness 對比分析、Phase 1 實作審查 | 1M context + SWE-bench Pro 62.1% 接近 Opus,成本 1/6 |
| Kimi | Kimi K2.7 Code（quality 檔,開源） | 文件撰寫、token 節省量化模擬、AGENTS.md Fusion Protocol 草稿 | 1000 tok/s 速度 + code 特化 + 成本 0.4× |
```

**New** (two replaced rows + inserted gate note):
```
| GLM | GLM-5.2（ceiling 檔,開源）⚠️ 合規 caveat | 架構設計驗證、跨 harness 對比分析、Phase 1 實作審查 | 1M context + SWE-bench Pro 62.1% 接近 Opus,成本 1/6。**注意**: Z.ai API 走中國伺服器有 GDPR/合規風險（model-profiles.md §0）,企業任務勿用 API 模式; 非 Claude 模型校正狀態 = BLOCKED-EXTERNAL（§6）,sidekick 部署前須完成校正程序 |
| Kimi | Kimi K2.7 Code（quality 檔,開源）⚠️ 合規 caveat | 文件撰寫、token 節省量化模擬、AGENTS.md Fusion Protocol 草稿 | 1000 tok/s 速度 + code 特化 + 成本 0.4×。**注意**: 非 Claude 模型校正狀態 = BLOCKED-EXTERNAL,須完成 §6 校正程序後方可用於 sidekick |

> **BYOK Sidekick 合規 Gate**: 開源模型（GLM/Kimi/MiniMax）用於 sidekick 前,必須完成 model-profiles.md §6 非 Claude 校正程序（5-10 代表性任務含 eval-hack trap; 目前 BLOCKED-EXTERNAL）。企業任務禁用 Z.ai API 模式（GDPR 風險）。
```

**Reason**: model-profiles.md §0 explicitly warns Z.ai API routes through China servers (GDPR/compliance risk) and §6 marks non-Claude model calibration as BLOCKED-EXTERNAL. The design plan §4.1 assigned GLM-5.2 as ceiling-tier reviewer and Kimi as sidekick without surfacing either risk, leaving downstream operators unaware of the enterprise API-mode prohibition and the calibration prerequisite. Inline ⚠️ markers on both rows make the caveat visible at the point of assignment, and the gate note formalizes the prerequisite (calibration completion) before any BYOK sidekick deployment.

---

## Fix C5 — Open-source sidekick partial-failure modes not addressed

**Location**: §3.2 五層 Token 優化體系, Layer 4 委派策略層, around line 234
**Action**: INSERT partial-failure detection block after the existing "Sidekick 失敗 1 次即升級" line

**Old** (exact match, the existing line to anchor the insertion):
```
- Sidekick 失敗 1 次即升級（cost → quality）,不重試
- 降級: 高檔位解出模式寫成規則,降 cost 批次套用
```

**New** (anchor lines preserved + inserted block between them):
```
- Sidekick 失敗 1 次即升級（cost → quality）,不重試
- **部分失敗偵測（開源 sidekick 專用）**: 
  - 正交驗證: main agent 用不同 pattern 重跑 grep/檢查,非信任 sidekick 的相同方法
  - Scope-verification: 確認 sidekick 操作了正確的目標檔案（非鄰近檔案）
  - Citation-existence check: 研究 sidekick 的 URL 引用需機械驗證存在（grep URL,不信宣稱）
  - 邏輯正確性 spot-check: 對機械任務隨機抽 10% 由 main agent 重做,比對結果
- 降級: 高檔位解出模式寫成規則,降 cost 批次套用
```

**Reason**: The original "失敗 1 次即升級,不重試" rule only catches crashes/explicit errors. Open-source sidekicks (GLM/Kimi) introduce partial-failure modes the crash rule does not cover: syntactically valid but logically wrong edits, scope drift to adjacent files, fabricated citations, and plausible-but-incorrect results. Without orthogonal verification, scope checks, citation-existence checks, and spot-checks, a sidekick can silently produce wrong output that the crash-based escalation path will never trigger on. The inserted block operationalizes the "驗證不自驗" principle (delegation-protocol.md §6) for the specific failure modes open-source models are prone to.

---

## Fix C6 — Latency, observability, verification cost dimensions missing

**Location**: After §6 第六部分:風險與限制 (after line 380), before the 附錄 section
**Action**: INSERT new §6b section

**Content** (full text of §6b to insert, placed between the end of §6's item 5 and the `## 附錄:關鍵文件指針` heading):
```markdown
## 第六部分b:缺失維度補充（交叉審查 C6 修正）

### 6b.1 延遲模型

Fusion 架構的 sidekick round-trip 成本（spawn/PATCH + 執行 + 回報）在 wall-clock 秒級別高於 inline 執行。

| 任務類型 | 延遲影響 | 建議 |
|---------|---------|------|
| 即時 incident response | ⛔ 不適用 Fusion | main agent inline 親做 |
| 即時 debugging | ⛔ 不適用 Fusion | main agent inline 親做 |
| 批量掃描/遷移 | ✅ 延遲可接受 | sidekick 並行,main 等回報 |
| 深度研究 | ✅ 延遲可接受 | sidekick 掃描 + main 彙整 |
| 安全審查 | ⚠️ 需權衡 | adversarial review 需 sidekick 但不能阻塞 |

**結論**: Fusion 不推薦用於 latency-bound 任務。適用於 throughput-bound 和 quality-bound 任務。

### 6b.2 路由可觀測性

Fusion 路由決策需可審計:

1. **路由日誌**: 每次 Fusion 路由決策記錄至 `evolution/cost-log.jsonl`（task, signal, route chosen, model, cost, outcome）
2. **A/B 測量計畫**: 2 週 Fusion-vs-non-Fusion A/B 對照,同類任務量測實際節省（非模擬）
3. **路由決策回放**: 錯誤路由可追溯原因（複雜度信號誤判 / sidekick 能力不足 / 任務分類錯誤）

### 6b.3 驗證成本量化

main agent 機械重驗 sidekick 輸出本身有 token 成本,未包含在 -35.2% 模擬中。

| 任務類型 | 驗證方式 | 估算驗證 token | 對節省的影響 |
|---------|---------|-------------|------------|
| 單檔小改 | 無需（T0 親做） | 0 | 無影響 |
| 跨模組重構 | diff review | ~2000 input + 500 output | 增加 ~$0.017,節省從 -36% 變 -38%（略加劇） |
| 深度研究 | citation check + scope verify | ~3000 input | 增加 ~$0.015,節省從 37% 降至 ~34% |
| 安全審查 | adversarial re-check | ~5000 input + 1000 output | 增加 ~$0.040,成本增從 -18% 變 -29%（顯著加劇） |
| 大規模遷移 | spot-check 10% | ~3000 input per PR × 16 | 增加 ~$0.048,節省從 53% 降至 ~50% |

**結論**: 驗證成本壓縮深度研究和大規模遷移的節省 ~3pp,但顯著加劇安全審查的成本增加。修正後成本加權節省預估從 -35.2% 降至約 -31%。

```

**Reason**: ChatGPT-5.5 cross-review flagged that the design plan's §6 "風險與限制" listed 5 risk items but entirely omitted three operational dimensions: (1) latency — Fusion's sidekick round-trip makes it unsuitable for latency-bound tasks like incident response and live debugging, a constraint never stated; (2) observability — Fusion routing decisions are currently unauditable, with no routing log, no A/B measurement plan, and no error-route replay capability, undermining the "external-validation" judgment framework the workspace enforces; (3) verification cost — the headline -35.2% saving was simulated without counting the tokens main agent spends re-verifying sidekick output, which the table quantifies per task type and which materially erodes the safety-review case (cost increase worsens from -18% to -29%). Inserting §6b surfaces all three so the proposed savings are not accepted at face value.
```

---

## Application Notes

- All three `Old` blocks above are copied verbatim from the target file (verified via Read + Grep on 2026-07-09). The C4 old block is two consecutive table rows; the C5 old block is two consecutive bullet lines; the C6 insertion point is the line immediately before `## 附錄:關鍵文件指針`.
- C6's `Content` block is fenced with ` ```markdown ... ``` ` for readability; the actual insertion should strip that outer fence and insert the raw markdown (the inner table/code fences remain).
- No line numbers are hardcoded in the replacements — all anchors are content-based to remain stable under minor upstream edits.
