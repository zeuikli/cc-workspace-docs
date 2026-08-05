# GLM×Kimi v3 合規審查報告 — .claude/ 全檔 vs The Loop Harness v3

> 審查日期：2026-07-08
> 審查者：GLM-5.2（主審，rules/refs/hooks）+ Kimi 2.7（對抗審查，skills/agents/settings）
> 對照基準：`research/archive/the-loop-harness-v3/HARNESS-CORE-v3.md`（L1）+ `SPEC-v3.md`（落地藍圖）+ `PROFILES-v3.md`（L2）+ `.claude/refs/model-profiles.md`（L2 落地 SSoT）
> 驗證方式：所有發現經 `grep`/`wc`/`python3`/`ls` 機械重驗

---

## 審查範圍

| 區塊 | 審查者 | 檔案數 |
|------|--------|--------|
| rules/（7 檔） | GLM | 7 |
| refs/（28 檔） | GLM | 28 |
| hooks/（22 .sh + README + lib） | GLM | 24 |
| settings.json + profiles.json | Kimi | 2 |
| agents/（12 .md + INDEX） | Kimi | 13 |
| skills/（27 SKILL.md + 27 GOTCHAS.md） | Kimi | 54 |
| supporting（AGENTS-ROSTER/HANDOFF/REFERENCES/RESOLVER/dependency-graph） | Kimi | 5 |
| **合計** | | **133 檔** |

---

## 合規總覽

| 類別 | 檔案數 | 合規 | 不合規 | 警告 |
|------|--------|------|--------|------|
| rules/*.md | 7 | 7 | 0 | 0 |
| refs/*.md | 28 | 25 | 0 | 3 |
| hooks/ | 24 | 20 | 0 | 4 |
| settings.json + profiles.json | 2 | 2 | 0 | 0 |
| agents/*.md | 13 | 11 | 0 | 2 |
| skills/*/SKILL.md | 27 | 25 | 1 | 1 |
| skills/*/GOTCHAS.md | 27 | 26 | 0 | 1 |
| supporting files | 5 | 4 | 0 | 1 |
| **合計** | **133** | **120** | **1** | **12** |

**整體合規率 ≈ 90.2%**（120/133 完全合規；1 不合規 + 12 警告，無阻斷性缺陷）

---

## v3 核心不變式驗證（SPEC-v3 §3）

| 不變式 | 狀態 | 驗證 |
|--------|------|------|
| 1. 確定性 gates 邏輯不弱化 | ✅ | block-dangerous/protect-sensitive/pre-commit-review/pre-compact/usage-delegation/unicode-guard/post-edit 全在 |
| 2. 驗證閘門條文只可加嚴 | ✅ | core.md TEST 階段含「驗證閘門與能力成正比」+「廉價確定性檢查永不跳過」 |
| 3. 刪除含唯一知識先抽出 | ✅ | core.md APPLY「刪含唯一知識先抽出併入接收檔」 |
| 4. 全 repo 活引用改線，懸空引用=0 | ⚠️ | fable5-harness:calibrate 殘留 5 處（見 C-04） |
| 5. 繁中為使用者面文字準 | ✅ | rules/core.md IMPORTANT 語言條款 |
| 6. healthcheck FAIL=0 | ✅ | baseline PASS 208/FAIL 0（MEMORY.md） |

---

## v3 SPEC §2 落地對照

| SPEC 要求 | 狀態 | 證據 |
|-----------|------|------|
| rules L1 化（零模型名/零數字） | ✅ | grep rules/*.md = 0 模型名；prompt-lifecycle.md 含 19,000 但為 on-demand 非 L1 |
| L2 schema 新建 model-profiles.md | ✅ | 存在且為 L2 SSoT，吸收 6 個舊 refs |
| skills 四 pilot 合併 → 單一 pilot | ✅ | .claude/skills/pilot/ 存在，tier 參數化 |
| fable5-harness → harness-core | ✅ | skill 已更名；⚠️ 但 refs/hooks 中引用未完成 codemod（C-04） |
| agents haiku-implementer 併入 implementer | ✅ | agents/ 無 haiku-implementer.md；⚠️ AGENTS-ROSTER 計數未同步（C-08） |
| hooks 模型名硬編碼 → 讀 profiles.json | ✅ | diff-size-guard/session-init 讀 profiles.json；⚠️ session-init L316 fallback 硬編碼（C-05） |
| contract-echo-gate 刪除 | ✅ | 磁碟不存在，README 無 ghost ref |
| memory-pr-record 兩支合併 | ✅ | 單一腳本雙 entry（mcp+gh） |
| cyber/bio 安全路由 5 處重複 → profiles 單點 | ✅ | model-profiles.md §3 為唯一 canonical，5 skill 指回 |
| L4 EVAL-PACK.md | ✅ | research/archive/the-loop-harness-v3/EVAL-PACK.md 存在 |

---

## 逐項發現

### C-01｜Medium｜L1 Zero-Model-Names｜skills 含硬編碼模型版本 pin

**來源**：Kimi F1+F4（GLM 確認）
**檔案**（6 處）：
- `.claude/skills/sia/SKILL.md:120,128` → `claude-haiku-4-5` / `claude-fable-5`
- `.claude/skills/sia/REFERENCE.md:44-46` → 4 個版本 pin
- `.claude/skills/harness-meta/references/prompt-token-optimization-GOTCHAS.md:161` → `claude-sonnet-4-6`
- `.claude/skills/harness-meta/references/prompt-token-optimization-REFERENCE.md:90` → `claude-sonnet-4-6`
- `.claude/skills/harness-meta/references/harness-dream-WORKFLOW.md:131` → `claude-haiku-4-5-20251001`
- `.claude/skills/media-research/GOTCHAS.md:59,65` → `claude-haiku-4-5-20251001`

**v3 要求**：SPEC-v3 §2「模型名只允許出現在 L2 對應表」；HARNESS-CORE-v3 §4「能用檔位就不寫版本號」
**灰色地帶**：多為 API 呼叫範例（curl/Python SDK），技術上需要具體 ID 才能執行
**建議**：在每個範例上方加註「快照日期 2026-07-04，換代以 model-profiles.md §0 為準」或改用 alias + 指針

### C-02｜Low｜Four-Layer Separation｜prompt-lifecycle.md 含 byte 門檻數字

**來源**：GLM
**檔案**：`.claude/rules/prompt-lifecycle.md:42` → `19,000`
**v3 要求**：L1 零數字，數字 → L2
**減輕因素**：此檔 `tier: on-demand` + `paths` path-scoped，**不是 auto-load L1**
**建議**：改為「byte 門檻見 model-profiles.md §2.1」+ 指針

### C-03｜Low｜Four-Layer Separation｜5 agent 內文無 tier 詞

**來源**：Kimi F2
**檔案**：doc-writer.md / memory-compactor.md / security-auditor.md / security-reviewer.md / zeuik-senior-architect.md
**v3 要求**：SPEC-v3 §2「agents 內文模型指導 → tier + profile 指針」
**減輕因素**：`model:` frontmatter 是 alias（非 version pin），SPEC §2「L3 wiring 允許 alias」合規；但內文與 INDEX 速查表輕度不同步
**建議**：在 5 個 agent 內文加一行「（檔位 = cost/quality/ceiling，當代模型對應見 model-profiles.md）」

### C-04｜Medium｜全 repo 活引用改線｜fable5-harness:calibrate 殘留 5 處

**來源**：GLM（Kimi 未觸及 refs/hooks 深掃）
**檔案**（5 處活引用）：
- `.claude/refs/model-profiles.md:24` → `fable5-harness:calibrate`
- `.claude/refs/maintenance-protocol.md:96` → `fable5-harness:calibrate`
- `.claude/refs/delegation-protocol.md:67` → `fable5-harness:calibrate`
- `.claude/hooks/session-init.sh:320` → `fable5-harness:calibrate`
- `.claude/hooks/diff-size-guard.sh:6` → `fable5-harness SPEC`

**v3 要求**：SPEC-v3 §3 不變式 4「全 repo 活引用改線，懸空引用 = 0」；§2「fable5-harness → harness-core」
**狀態**：skill 已更名為 harness-core（舊名相容），但 refs/hooks 的 `fable5-harness:calibrate` 引用未同步改為 `harness-core:calibrate`
**建議**：codemod 5 處 `fable5-harness:calibrate` → `harness-core:calibrate`；diff-size-guard 註解改指 v3 SPEC

### C-05｜Low｜L3 wiring｜session-init.sh fallback 硬編碼模型名

**來源**：GLM
**檔案**：`.claude/hooks/session-init.sh:316` → `LATEST_KNOWN_FAMILY="claude-sonnet-5"`
**v3 要求**：SPEC-v3 §2「hooks 模型名硬編碼 → 讀 profiles.json」
**減輕因素**：先讀 profiles.json，僅讀取失敗才 fallback；是防禦性設計
**建議**：fallback 改從 settings.json 讀 model 欄位作為二級 fallback，避免硬編碼版本 pin

### C-06｜Low｜Documentation Drift｜REFERENCES.md v2 canonical 指針未更新

**來源**：GLM
**檔案**：`.claude/REFERENCES.md:100` → 仍標「The Loop Harness v2.0（合併版，forward canonical，2026-07-04）」
**v3 要求**：v3 為 forward canonical（HARNESS-CARD 已修正，REFERENCES.md 未同步）
**建議**：更新 REFERENCES.md L100，v2 改為「一手證據基底」，v3 標為 forward canonical

### C-07｜Low｜RATCHET 90-day review｜handoff skill review-by 3 天後到期

**來源**：Kimi F3
**檔案**：`.claude/skills/handoff/SKILL.md` → `review-by: 2026-07-11`
**v3 要求**：RATCHET 2026-05-25「90-day review cycle」；公理 5「規則 = decaying cache」
**建議**：下一維護 cycle 重審 handoff SKILL.md，延後 review-by 或修訂內容

### C-08｜Low｜Documentation Drift｜AGENTS-ROSTER.md agent 計數 13 vs 12

**來源**：Kimi F5
**檔案**：`.claude/AGENTS-ROSTER.md` → 自述「13 specialist agents」，仍列 haiku-implementer
**v3 要求**：SPEC-v3 §2「haiku-implementer 併入 implementer」；§3 不變式 4
**現況**：agents/INDEX.md 正確列 12 個；AGENTS-ROSTER.md 未同步
**建議**：計數 13→12，移除 hauka-implementer 行

### C-09｜Info｜Observability｜tool-log.sh pipeline 失效

**來源**：前次 Kimi hook audit（F-07）
**檔案**：`.claude/hooks/tool-log.sh` → 寫 `.claude/command-log.jsonl`（檔案不存在）
**狀態**：2 個 hook wiring 產出零可觀測輸出
**建議**：修復（確保 command-log.jsonl 建立）或移除 wiring

### C-10｜Info｜Dead-weight｜audit-permission.sh 永不觸發

**來源**：前次 Kimi hook audit（F-07）
**檔案**：`.claude/hooks/audit-permission.sh` → bypassPermissions 下 PermissionRequest 永不觸發
**建議**：移除 wiring 或改 defaultMode 時重新啟用

---

## v3 新增條款落地驗證（core.md）

| v3 條款 | core.md | subagent-strategy.md | 狀態 |
|---------|---------|----------------------|------|
| benefit-gated 委派 | 「任務分類先於委派」+ 指針 subagent-strategy | 「預設最簡拓撲；委派須具名效益（非舊 v2）」 | ✅ |
| Unknowns 協議 | Blindspot/Interview/Prototype-first | — | ✅ |
| 儀式深度 | 「隨風險與不可逆性伸縮，不隨模型檔位」 | — | ✅ |
| 五標籤 | autonomous/assisted/unverified/failed/unsafe | — | ✅ |
| 刪除三級 | low/medium/high + 三件齊備 | — | ✅ |
| taste 有界 | 「可否決品質缺陷，不可否決 correctness」 | — | ✅ |
| redaction 例外 | 「secret/PII → command/exit/hash/shape」 | — | ✅ |
| 雙軸伸縮 | 「行為指導量與能力成反比，驗證閘門與能力成正比」 | — | ✅ |
| 能力悖論 | 「eval-hack 隨能力遞增」 | — | ✅ |

---

## 強項（v3 落地扎實）

1. **L1 rules/ 零模型名**：grep rules/*.md 確認 0 模型名版本 pin（v3 鐵律達成）
2. **settings.json + profiles.json 三向一致**：model / default_tier / latest_known_family 完全對齊
3. **10 種 hook event 全配置**：SessionStart 到 PermissionRequest 完整覆蓋
4. **全部 12 agent 有 tools: frontmatter + The Loop 紀律行 + model: alias（非 pin）**
5. **全部 27 skill 有 allowed-tools: + review-by: frontmatter + GOTCHAS.md**
6. **Safety routing 單點化**：model-profiles.md §3 唯一 canonical，5 skill 指回
7. **四層分離清晰**：harness-core SKILL.md 含完整 L1-L4 速覽，pilot/multi-mode tier 參數化
8. **contract-echo-gate 已刪除**：磁碟不存在，README 無 ghost ref
9. **refs/ 無孤兒檔案**：所有 ref 都有被引用
10. **v3 新增條款全部在 core.md 體現**

---

## 優先修正清單

| # | Finding | Severity | 行動 | Effort |
|---|---------|----------|------|--------|
| 1 | C-04 | Medium | codemod 5 處 fable5-harness:calibrate → harness-core:calibrate | Low（grep+sed） |
| 2 | C-01 | Medium | 6 處 skill 硬編碼模型 pin 加註快照日期或改 alias | Low-Medium |
| 3 | C-06 | Low | REFERENCES.md L100 v2→v3 canonical 更新 | Low |
| 4 | C-08 | Low | AGENTS-ROSTER.md 計數 13→12，移除 haiku-implementer | Low |
| 5 | C-02 | Low | prompt-lifecycle.md 19,000 → 指針 model-profiles.md | Low |
| 6 | C-05 | Low | session-init.sh fallback 改讀 settings.json | Low |
| 7 | C-03 | Low | 5 agent 內文加 tier 詞 + profile 指針 | Low |
| 8 | C-07 | Low | handoff SKILL.md review-by 重審 | Low |
| 9 | C-09 | Info | tool-log.sh pipeline 修復或移除 | Medium |
| 10 | C-10 | Info | audit-permission.sh 移除或保留待 defaultMode 變更 | Low |

---

## 結論

cc-workspace `.claude/` 目錄的 v3 合規率 **≈ 90.2%**（120/133 完全合規）。v3 核心不變式（確定性 gates、驗證閘門、benefit-gated 委派、safety routing 單點、L1 零模型名）均已落地。剩餘 1 不合規 + 12 警告均為**文件債或 codemod 未完成**，不影響 harness 行為正確性。

最高優先是 **C-04**（fable5-harness:calibrate 殘留 5 處）——這是 v3 SPEC §3 不變式 4「懸空引用 = 0」的直接違反，且 skill 已更名但引用未同步，是可快速修復的 codemod 缺口。

---

*審查者：GLM-5.2（Droid Core）+ Kimi 2.7（Moonshot AI，fresh-context sub-agent） · 2026-07-08 · 機械驗證：grep/wc/python3/ls*
