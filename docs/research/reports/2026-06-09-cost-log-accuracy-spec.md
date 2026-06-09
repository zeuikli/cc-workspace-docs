---
title: "cost-log 準確性改進規格書"
date: 2026-06-09
status: implemented
pricing_calibrated: 2026-06-09
pricing_source: "https://platform.claude.com/docs/en/docs/about-claude/pricing"
scope: scripts/pricing.py · scripts/sync-desktop-usage.py · scripts/usage-report.py · .claude/hooks/pre-push-cost.sh
type: spec
---

# cost-log 準確性改進規格書

## 1. 背景與目標

cost-log（`evolution/cost-log.jsonl`）記錄跨平台（Desktop / iOS / CLI）的 token 用量與成本，供 `usage-report.py` 彙整、Portal `/usage` 顯示。本規格書記錄 **2026-06-09 對成本計算準確性的研究發現與修正實作**。

**目標**：在不破壞歷史資料的前提下，讓**新同步的 cost 計算**對齊 Anthropic 官方計費規則。

---

## 2. 研究：準確性缺陷清單

對 `sync-desktop-usage.py` / `pre-push-cost.sh` / `usage-report.py` 三者 + transcript usage 欄位 + 官方 pricing 頁交叉分析，確認 7 個缺陷：

| # | 缺陷 | 嚴重性 | 證據 | 實測影響 |
|---|------|--------|------|---------|
| 1 | **1h cache write 全當 5m 計價** | 高 | transcript 有 `cache_creation.ephemeral_1h/5m_input_tokens`，舊版只讀總 `cache_creation_input_tokens` 用 5m 費率 | 真實 transcript（61,241 1h tokens）**低估 60%**（$0.2297→$0.3674）|
| 2 | **兩處 PRICING 表 Opus 數字矛盾** | 高 | `sync-desktop` input=$5（對）vs `pre-push-cost` input=$15（舊定價，錯）| pre-push 補金額時 Opus 成本算成 3 倍 |
| 3 | **web_search 未計費** | 中 | `server_tool_use.web_search_requests` 存在但忽略 | $10 / 1,000 searches 漏計 |
| 4 | **model 只取首個 assistant message** | 中 | 舊 `scan_jsonl` line 141；session 內切 model（Opus→Sonnet）全算成首個 | 混用 session 定價失真 |
| 5 | **fast / batch / inference_geo 乘數未處理** | 低-中 | usage 有 `service_tier`/`inference_geo`，未讀 | batch 5 折 / geo 1.1x / fast 2-6x 未反映 |
| 6 | **iteration 重複計算風險** | — | 經驗證 `message.usage == sum(iterations)`，腳本只讀 message-level → **無重複**（排除）| 無 |
| 7 | **既有列無 1h/5m 細分** | 低 | cost-log 既有 1542 列只存總 `cache_creation_tokens` | 無法純從 cost-log 回溯重算 |

**定價校準**（WebFetch 官方頁 2026-06-09）：

| 模型 | input | output | cache_read(0.1x) | 5m write(1.25x) | 1h write(2x) |
|------|-------|--------|------------------|-----------------|--------------|
| Opus 4.5–4.8 | $5 | $25 | $0.50 | $6.25 | **$10** |
| Sonnet 4.x | $3 | $15 | $0.30 | $3.75 | **$6** |
| Haiku 4.5 | $1 | $5 | $0.10 | $1.25 | **$2** |

其他官方規則：web_search $10/1k · batch 5 折 · inference_geo=us 1.1x · fast mode（Opus）input/output 覆寫。

---

## 3. 決議（使用者裁決 2026-06-09）

| 議題 | 選項 | 裁決 |
|------|------|------|
| 改進範圍 | 全部 / 高+中 / 只高 | **全部修正（高+中+低）** |
| PRICING 重複（3 處）| 抽共用模組 / 就地改一致 | **抽共用模組** |
| 既有列回溯重算 | 重掃 transcript / 保留 | **保留**（向前準確，不破壞歷史）|

---

## 4. 實作

### 4.1 新增 `scripts/pricing.py`（單一定價真相源）

- `PRICING` 表：官方數字直取（非由 input 乘出，避免捨入漂移）；含 `cache_5m` / `cache_1h` 分離欄位
- `FAST_MODE` 表：Opus 4.6–4.8 fast mode input/output 覆寫
- `estimate_cost(model, input, output, cache_read, cache_5m, cache_1h, *, web_search_requests, fast_mode, service_tier, inference_geo)`：
  - cache write 拆 5m/1h 分離計價
  - server tool（web_search）per-request 計費（不受 batch/geo 乘數影響）
  - batch 5 折 / geo-us 1.1x 乘數
  - 退化路徑：呼叫端只有總 cache_creation → 全塞 `cache_5m` 即退回舊行為（保守略低估，非高估）
- **自測**：6 個 assertion 對照官方 worked example（Opus 50k+15k=$0.625、cache read 案例=$0.445、1h vs 5m 分離、web_search、batch）

### 4.2 改 `scripts/sync-desktop-usage.py`（缺陷 1/3/4/5）

- `import pricing`（移除本地 PRICING 表）
- `scan_jsonl` 重構：按 **(model, fast, tier, geo) 分組**累加 token，各組獨立計價再加總（修缺陷 #4 單一 model 套全 session）
- 讀 `cache_creation.ephemeral_1h/5m_input_tokens`（修 #1）；缺細分則全當 5m（退化保守）
- 讀 `server_tool_use.web_search_requests`（修 #3）；新增輸出欄位 `web_search_requests`
- 讀 `service_tier` / `inference_geo`（修 #5）
- 代表 model = 成本佔比最高者（報告分類用），cost 已按各組精算

### 4.3 改 `scripts/usage-report.py`

- `import pricing`（移除重複 PRICING 表）
- `estimate_cost(row)`：既有 cost_usd 優先；否則用共用模組（舊列無細分→保守當 5m，新列帶 web_search 也納入）

### 4.4 改 `.claude/hooks/pre-push-cost.sh`（缺陷 2）

- 移除硬編的**錯誤舊 Opus 定價 $15**，改 `from pricing import estimate_cost`
- DB 的 `total_cache_creation` 無 1h/5m 細分 → 保守全當 5m
- 傳入 `REPO_DIR` 第三參數供 import 定位

---

## 5. 驗證（機械接地）

| 驗證項 | 方法 | 結果 |
|--------|------|------|
| 定價計算正確 | `python3 scripts/pricing.py`（6 assertion 對官方 worked example）| ✅ PASS |
| 1h/5m 分離有效 | 真實 transcript 對照舊 vs 新算法 | ✅ 低估 60% 已修正（$0.2297→$0.3674）|
| 三腳本 import 正常 | dry-run + usage-report 跑通 | ✅ 全部正常 |
| iteration 不重複 | `message.usage == sum(iterations)` 親驗 | ✅ 無重複 |
| hook 語法 | `bash -n pre-push-cost.sh` | ✅ OK |
| report 三模式 | 預設 / `--json` / `--daily` | ✅ 全通 |

---

## 6. 已知限制與後續

- **既有 1542 列保留舊算法 cost**（無 1h/5m 細分，無法純從 cost-log 回溯）。如需完整回溯：刪 `evolution/.desktop-usage-seen.txt` + 重掃 transcript（會改動歷史 1542 列，風險高，未執行）。
- **fast mode 偵測不可靠**：transcript 未帶顯式 fast flag，目前 `fast_mode` 預設 False（Opus research preview 少用，影響小）。若未來需精確：須從 settings/session metadata 判定。
- **定價需定期校準**：`pricing.py` frontmatter 標 `pricing_calibrated: 2026-06-09`；官方調價時重跑 WebFetch 對齊。

---

## 7. 自動化關係（不變）

呼叫鏈不變，僅計算邏輯升級：
```
Stop hook → session-stop.sh → sync-workspace.sh:735 → sync-desktop-usage.py（建 token 列 + 精算 cost）
git push → pre-push-cost.sh（DB session 補金額，共用 pricing）
usage-report.py（讀 + 算，共用 pricing）
```
三處計算統一走 `scripts/pricing.py`，根治「定價表各自漂移」。
