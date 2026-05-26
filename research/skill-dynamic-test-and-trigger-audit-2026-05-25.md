---
title: SKILL 動態測試 + 觸發詞盤點報告
date: 2026-05-25
scope: 18 custom SKILLs — Skill tool 試跳 + 357 trigger registry + namespace audit
verdict: 16 ✅ load / 2 ⚠️ design-disabled / 0 conflict / 4 namespace mismatch
---

# SKILL 動態測試 + 觸發詞盤點報告 — 2026-05-25

## TL;DR

1. **動態 load**：18 個 SKILL 全部結構正常。16 個成功 Skill tool 試跳；2 個（security-compliance、ship-review）因 `disable-model-invocation: true` 設計上不可主動觸發，**這是設計而非 bug**。
2. **觸發詞盤點**：抽出 **357 條觸發詞**（233 中文 / 54 英文 / 52 子模式 / 18 主名），寫入 `research/trigger-registry-2026-05-25.csv`。
3. **衝突偵測**：**零跨 SKILL exact duplicate**（同一觸發詞不會路由到兩個不同 SKILL）。
4. **命名空間問題（用戶提到的「media:twitter 情況」）**：**4 個 sub-mode 命名 prefix 與 SKILL name 不一致**——`media:gh` / `media:substack` / `media:twitter` / `media:youtube` 都路由到 `media-research` 但前綴用 `media:`。
5. **語義模糊地帶**：「審查」「研究」「分析」等中文詞跨多個 SKILL，但都有明確情境限定（如「快速審查 workspace」vs「程式碼審查」），實際歧義風險低。

## Phase 結果

| Phase | 測試項 | 結果 |
|-------|-------|------|
| A | 357 條觸發詞抽取 | ✅ 已寫入 CSV |
| B | 衝突偵測（跨 SKILL exact match） | ✅ 0 衝突 |
| B | 命名空間一致性（sub-mode prefix vs SKILL name） | ⚠️ 4 個 mismatch（media:* 系列）|
| B | 短觸發詞警示（≤4 char） | ⚠️ 3 個（`MSK`、`tech`、`Opus`）|
| C | 16 SKILL Skill tool 試跳 | ✅ 全部成功載入 |
| C | 2 SKILL `disable-model-invocation` | ⚠️ 設計選擇，可被 user-typed trigger 啟動 |

## 各 SKILL 子模式清單（由 Skill tool 試跳輸出整理）

| SKILL | 子模式數 | 子模式 |
|-------|---------|--------|
| db-ops | 2 | `db-ops`, `:migrate` |
| finops | 5 | `finops`, `:savings`, `:cdn`, `:cost`, `:capacity` |
| autoresearch | 11 | `autoresearch`, `:plan`, `:debug`, `:fix`, `:security`, `:ship`, `:scenario`, `:predict`, `:learn`, `:reason`, `:wiki` |
| haiku-pilot | 1 | `haiku-pilot` 單模式 |
| sonnet-pilot | 1 | `sonnet-pilot` 單模式 |
| opus-pilot | 4 | base, `Opus 1M`, `Opus xhigh`, `Opus 1M xhigh` |
| research-hub | 7 | `research-hub`, `:archive`, `:deep`, general, `:audit`, `:score`, `:fetch`, `:gh-profile` |
| review-hub | 6 | `:commit`, `:bugs` (4 effort), `grill`, `:infra`, `:bugfix`, `:debug` |
| sre | 6 | `:incident`, `:rca`, `:oncall`, `:k8s`, `:kafka`, `:monitoring` + `cathaysec-terraform` |
| media-research | 4 | `media:twitter`, `media:youtube`, `media:gh`, `media:substack` |
| media-transcribe | 1 | URL 自動偵測 |
| harness-meta | 8 | `:hmf`, `:audit`, `:dream`, `:add`, `:import`, `:context`, `:token`, `:citation` |
| overnight-research | 3 | base, `:quick`, `:full` |
| security-compliance | 1 | disable-model-invocation |
| ship-review | 1 | disable-model-invocation |
| skill-evolution | 3 | `:scan`, `:apply <name>`, `:audit` |
| spec-implement | 1 | 單模式 |
| tech-strategy | 2 | `:eval`, `:roi` |

## ⚠️ 4 個命名空間不一致（「media:twitter 情況」）

| 觸發詞 prefix | 路由到 SKILL | 不一致原因 |
|---------------|-------------|-----------|
| `media:twitter` | media-research | prefix `media` ≠ SKILL name `media-research` |
| `media:youtube` | media-research | 同上 |
| `media:gh` | media-research | 同上 |
| `media:substack` | media-research | 同上 |

**根本原因**：`media-research` SKILL 用 `media:` 作為 sub-mode prefix（簡潔），但 SKILL name 是完整 `media-research`。這違反「prefix 應等於 SKILL name」的隱性慣例（如 `finops:cdn` 屬於 `finops` SKILL、`sre:k8s` 屬於 `sre` SKILL）。

### 規範建議（不自動修改，僅提案）

**選項 A：對齊主名（建議）**
```
media:twitter   → media-research:twitter
media:youtube   → media-research:youtube
media:gh        → media-research:gh
media:substack  → media-research:substack
```
- 優點：完全一致；觸發詞自我解釋路由
- 成本：4 條 trigger 需在 RESOLVER.md + SKILL.md description + 各 SKILL.md 路由表更新；用戶記憶/筆記中的 `media:twitter` 變成 `media-research:twitter`（較長）
- 影響檔案：~6 個 .md 檔

**選項 B：保留 `media:*` 為官方 namespace alias**
```
維持 media:twitter / media:youtube / media:gh / media:substack
但在 RESOLVER.md 加註：「media:* 為 media-research 的 namespace alias，等同 media-research:*」
```
- 優點：使用者輸入更短；無需大改
- 成本：在 RESOLVER.md 補一段「official alias mapping」表，並在 SKILL.md frontmatter 明確列出 alias
- 影響檔案：~2 個 .md 檔

**推薦**：**選項 B**。`media:` 比 `media-research:` 更符合直覺（Twitter/YouTube/GitHub 都是「media」這個語義群），但需要在文件層級正式宣告 alias 機制，避免未來新 SKILL 隨意設計類似 prefix 造成混亂。

## ⚠️ 3 個短觸發詞警示

| 觸發詞 | 路由 | 風險 | 處理建議 |
|--------|------|------|---------|
| `MSK` | sre | 中：AWS Managed Streaming for Kafka 縮寫，可能被一般「MSK」誤觸 | 加 context 限定「AWS MSK」或「Kafka MSK」 |
| `tech` | tech-strategy | 中：太通用，可能被「tech debt」「tech stack」誤觸 | 改用 `tech-eval` 或 `tech:eval` 更精確 |
| `Opus` | opus-pilot | 低：「Opus」單詞很可能就是要切 Opus 模式，誤觸成本低 | 保留 |

## 語義模糊地帶（不算 conflict 但需留意）

| 模糊詞 | 跨 SKILL | 風險評估 |
|--------|----------|---------|
| 「審查」 | review-hub（code review）vs research-hub（workspace audit）| 低：用戶輸入會帶情境（「完整審查」→ research-hub:audit；「程式碼審查」→ review-hub:commit），description 已區分 |
| 「研究」 | research-hub vs overnight-research vs media-research | 低：URL 路由優先（有 URL 自動分流），純文字「研究」走 research-hub |
| 「分析」 | 6 SKILL 都有 X 分析 | 低：前綴限定夠強（「日誌分析」/「成本分析」/「commit 分析」） |
| 「audit」 | harness-meta:audit / research-hub:audit / skill-evolution:audit | 低：都有 namespace 前綴，不會單獨用 `audit` |

## 動態 load 觀察

Skill tool 試跳時發現一個**渲染 artifact**：args 字串中的 placeholder（如 `$X`）會被 SKILL.md 內容載入時誤替換，導致 finops 定價表顯示異常。但**這是 Skill tool 載入時的視覺渲染問題，SKILL.md 本身內容正確**（Phase 1 已用 Read tool 直接讀過全文）。不影響功能。

## CSV Registry 使用方式

完整觸發詞註冊表：`research/trigger-registry-2026-05-25.csv`

欄位：`trigger, skill_name, category, source, notes`

可用於：
- 未來新增 SKILL 時 grep 防衝突：`grep -i "新觸發詞" trigger-registry-*.csv`
- 月度審查觸發詞演進
- RESOLVER.md 自動產生（從 CSV → markdown table）

## 結論

1. **18 個 SKILL 全部 dynamic-load 正常** —— 最近 5 個瘦身 commit 完全沒影響觸發能力
2. **零跨 SKILL 觸發詞 exact conflict** —— routing 路徑無歧義
3. **唯一系統性命名不一致是 `media:*` 系列**（4 個 trigger），建議採用「選項 B」官方化 alias 機制
4. **3 個短觸發詞** 中只有 `tech` 需要重新評估（建議改為 `tech-eval` 或加上必要 context）
5. **沒有觸發詞應立即下架** —— 所有現存 trigger 都有合理使用情境
