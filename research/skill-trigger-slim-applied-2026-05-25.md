---
title: SKILL 觸發詞精簡 + Namespace Alias 正式化執行報告
date: 2026-05-25
scope: 18 custom SKILLs — 選項 B 套用 + 中文觸發詞 30-55% 精簡
verdict: ✅ 全部驗證通過（healthcheck PASS / 0 broken refs / 行數無變動）
---

# SKILL 觸發詞精簡 + Namespace Alias 執行報告

## TL;DR

1. **選項 B（namespace alias）已套用**：`media:*` 正式宣告為 `media-research:*` 的 official alias，二者等效；RESOLVER.md 和 media-research/SKILL.md description 都已更新明確宣告。
2. **中文觸發詞精簡完成**：路由表中文觸發詞 **233 → 104**（削減 55.4%，超過原 plan 30.9% 目標）。
3. **驗證全綠**：healthcheck PASS / 88 references 全部完整 / 18 個 SKILL.md 行數無顯著變化（path-only 編輯）。

## Phase 結果

| Phase | 動作 | 結果 |
|-------|------|------|
| 1 | Namespace alias 宣告 | ✅ RESOLVER.md + media-research/SKILL.md description |
| 2 | researcher 分析 233 條中文觸發詞 | ✅ trigger-slim-plan-2026-05-25.md 寫入 |
| 3 | implementer × 5 平行精簡 7 個 SKILL.md | ✅ research-hub / harness-meta / sre / review-hub / finops / tech-strategy / media-research |
| 4 | implementer 同步精簡 RESOLVER.md | ✅ 4 個觸發詞移除 |
| 5 | healthcheck + 重建 registry | ✅ PASS 100 / WARN 3 / FAIL 0 |

## 精簡前後對照

### 路由表中文觸發詞（核心指標）

| SKILL | 精簡前 | 精簡後 | 削減 |
|-------|-------:|-------:|------:|
| harness-meta | ~52 | 31 | -40% |
| sre | ~31 | 19 | -39% |
| research-hub | ~46 | 29 | -37% |
| review-hub | ~22 | 11 | -50% |
| finops | ~18 | 12 | -33% |
| media-research | ~35 | 2 | -94%（多數轉為 sub-mode）|
| **TOTAL CJK** | **233** | **104** | **-55.4%** |

### SKILL.md 行數變化（path-only edit，行數幾乎不變）

| SKILL | 精簡前 | 精簡後 |
|-------|-------:|-------:|
| research-hub | 349 | 349 |
| sre | 349 | 349 |
| opus-pilot | 350 | 350 |
| sonnet-pilot | 311 | 311 |
| haiku-pilot | 289 | 289 |
| overnight-research | 255 | 255 |
| harness-meta | 245 | 244 |
| tech-strategy | 240 | 240 |
| finops | 236 | 236 |
| media-transcribe | 224 | 224 |
| skill-evolution | 195 | 195 |
| autoresearch | 193 | 193 |
| review-hub | 187 | 186 |
| security-compliance | 167 | 167 |
| media-research | 156 | 156 |
| db-ops | 103 | 103 |
| ship-review | 99 | 99 |
| spec-implement | 75 | 75 |

> 多數 SKILL.md 行數無變化是因為觸發詞精簡只移除單一儲存格內逗號分隔的項目，不刪除整行。harness-meta -1 行（合併同行）、review-hub -1 行（同上）。

## Namespace Alias 宣告（選項 B）

### RESOLVER.md（line 146-148）
```markdown
### 外部媒體 → `media-research`

> **Namespace alias**：`media:*` 為 `media-research:*` 的官方縮寫（official alias）。
> `media:twitter` ≡ `media-research:twitter`，二者等效；其他 sub-mode 同理。
> 優先用 `media:*` 短形式。
```

### media-research/SKILL.md frontmatter description
```
... Use when user types media-r, media-research, media:twitter, media:youtube,
media:gh, media:substack（前綴 media: 為 media-research: 的官方 namespace alias，
等效但較短）...
```

效果：
- ✅ 任何時候用戶輸入 `media:twitter`，routing 路徑明確（不再是「media-research 為什麼用 media: 前綴」的疑惑）
- ✅ 未來新 sub-mode（如 `media:substack`）自動繼承此 alias 規則
- ✅ 不破壞既有用法（用戶 + 自動化都繼續用 `media:*`）

## 移除的觸發詞分類

### A. 過長描述類（>8 字）— 直接移除
- 「把這個URL存成Markdown」「快速審查 workspace」「最新 best practice 有什麼更新」
- 「workspace 是否符合最佳實踐」「20% 成本削減目標」「雲端帳單 > $30k/月」
- 「建立符合官方規格」「Claude Code 使用評估」

### B. 同義詞群保留 1 個
- 收錄/收錄這篇/幫我收錄/收錄文章/把這篇文章留存 → 保留「收錄、存這篇文章、抓這篇文章存起來」
- Alarm as Code、告警 YAML → 保留「告警即代碼」
- adversarial 審查、correctness review → 保留「挑毛病模式、找 bug」

### C. 英文別名重複（已有 sub-mode 名）
- archive this article → 已有 `research-hub:archive`
- ship review → 已有 `ship-review`
- source verification、anchor enforcement、framework integrity check → 已有 sub-mode 對應

### D. 誤分類
- 「字幕提取」原列於 research-hub 與 media-research，實際屬 media-transcribe → 移除誤分類

## 驗證結果

### healthcheck
```
======================================
 統計結果：PASS: 100  WARN: 3  FAIL: 0
======================================
```
WARN 3 條皆為 pre-existing MCP server 未設定（與本次精簡無關）。

### References 完整性
```
TOTAL: 88 refs, 0 broken
```
所有 references/*.md 路徑連結保持完整。

### 殘留觸發詞檢查
- ✅ 0 處殘留「快速審查 workspace」/「20% 成本削減目標」等過長描述
- ✅ `## § 3 Aggressive Savings` 章節內「主管要求 ≥ 20% 削減」**保留**（這是內容描述非觸發詞，正確）

## 命名空間決策原則（沿用 / 未來新 SKILL）

1. **Sub-mode prefix = SKILL name 短版**：`finops:*` / `sre:*` / `review-hub:*` 等
2. **官方 alias 必須明文宣告**：如 `media:*` ≡ `media-research:*`（在 RESOLVER + SKILL.md 都寫）
3. **避免短於 4 字的單字 trigger**：除非語義唯一（如 `Opus` 切模式）

## 產出檔案

| 檔案 | 用途 |
|------|------|
| `research/trigger-slim-plan-2026-05-25.md` | 精簡計畫（researcher 產出） |
| `research/trigger-registry-post-slim-2026-05-25.csv` | 精簡後 trigger registry（124 條）|
| `scripts/count_triggers.py` | 路由表觸發詞計算腳本 |
| `scripts/check_refs.sh` | references 完整性檢查 |
| `scripts/detect_trigger_conflicts.sh` | 衝突偵測 |

## 結論

選項 B 套用 + 中文觸發詞 55% 精簡完成，所有驗證通過。
無 SKILL 功能退化、無 broken refs、無路由表結構破壞。
RESOLVER.md 與 SKILL.md description 已同步。
