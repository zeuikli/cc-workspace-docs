# GCP Monitoring → Teams 告警架構

> **Source positions**: CathaySec 國泰證券 2024–now
> **Last ingested**: 2026-04-22
> **Confidence**: high（Zeuik 主導實作，alerting_functions_V7.go 實戰驗證）
> **Linted**: 2026-04-22

---

## Context

金融業 SOC 需要即時感知 GCP infra 狀況，包含兩類訊號：
1. **Monitoring Alerts**：metric 超閾值、log pattern match
2. **Service Health Events**：GCP 平台服務故障（如 VPC、Cloud SQL regional outage）

CathaySec 選擇 Microsoft Teams 作為 NOC/SOC 通知管道，透過 Cloud Function 統一轉換格式為 Teams Adaptive Card。

---

## 監控指標矩陣（My Date 日報平台實戰）

CathaySec 的 My Date 日報管理平台使用以下 GCP 服務組合，對應監控指標如下：

| GCP 服務 | 關鍵監控指標 |
|---------|------------|
| Cloud Load Balancer | Latency、HTTP Error Count、Backend Service Count |
| Cloud CDN | Cache Status（hit/miss ratio）、Error Rate |
| WAF（Cloud Armor）| WAF Status Health、Logging（攔截事件） |
| Cloud SQL | CPU / Memory Usage、Failover 次數、Max Connection 使用率 |
| Cloud Run | CPU / Memory、Service Count（instance 數）|
| Cloud Storage | Status Health |
| Artifact Registry | Status Health |
| GitLab CI/CD | Pipeline Status、Logging |

**設計原則**：
- 以架構圖 + 啟用的服務清單決定監控項目，而非憑感覺選指標
- 業務層面（API 反應時間、HTTP 錯誤數）與技術層面（資源使用量、服務健康）分開 track
- 各服務建議一個主儀表板，讓 SRE 掃一眼就能掌握全局

---

## 監控指標判讀指南

### 業務情境：「使用者抱怨系統很慢」
1. 先看 Cloud Load Balancer latency + HTTP error count（最上層感知）
2. 再看 Cloud Run CPU/Memory（後端是否過載）
3. 再看 Cloud SQL Max Connection + Query latency（DB 是否瓶頸）
4. 最後看 CDN cache hit rate（靜態資源是否回源過多）

### 技術情境：服務自動恢復 vs 需要人介入
- GCP 服務大多有自動恢復機制（Cloud Run 自動重啟、Cloud SQL failover）
- **5 分鐘內自動恢復** → 記錄，不需緊急處置，但要查根因
- **5 分鐘後仍異常** → 進 Console 確認服務狀態，啟動升級流程

---

## 架構

```
GCP Monitoring                  GCP Service Health
  (metric alerts,                 (platform events,
   log match alerts)               regional outages)
       │                                 │
       └────────────┬────────────────────┘
                    ↓
            Cloud Logging
                    ↓
         Log Router (Pub/Sub Sink)
                    ↓
               Pub/Sub Topic
                    ↓
            Cloud Function
         (alerting_functions_V7.go)
                    ↓
       Teams Webhook → Adaptive Card
                    ↓
            SOC Teams Channel
```

---

## 程式碼架構（alerting_functions_V7.go）

### 統一介面設計

```go
// 兩種告警來源都實作 AlertEvent interface
type AlertEvent interface {
    ToAdaptiveCard() AdaptiveCard
    GetPriority() int
    ShouldFilter() bool
}
```

**設計優勢**：新增告警來源（如 Cloud Armor、Security Command Center）只需實作 interface，不改轉換邏輯。

### 兩種告警類型

#### Monitoring Alert
- 來源：Cloud Monitoring（metric violations、log match conditions）
- 狀態：`OPEN`（🔴 紅色）/ `CLOSED`（✅ 綠色）

#### Service Health Event（六種類型）

| 類型 | 顏色 | 說明 |
|------|------|------|
| `NEW_INCIDENT` | 🟠 橙 | 新發現故障 |
| `EMERGING` | 🟡 黃 | 調查中 |
| `CONFIRMED` | 🔴 紅 | 確認故障 |
| `UPDATE` | 🔵 藍 | 進展更新 |
| `RESOLVED` | ✅ 綠 | 已解決 |
| `FALSE_POSITIVE` | ⬜ 灰 | 誤報 |

### 優先級動態調整

```
Service Health ACTIVE  → Priority 3（最高，Teams 推播通知）
Service Health CLOSED  → Priority 1（低，靜默更新）
Monitoring OPEN        → Priority 2
Monitoring CLOSED      → Priority 1
```

---

## 關鍵踩坑：Service Health Labels 解析

Service Health 告警的 Summary 字串有兩種格式：

**格式 A（無詳細 labels）**：
```
Log match condition fired for Event with {event_id=sh-..., location=global, resource_container=...}
```

**格式 B（含詳細 labels）**：
```
Log match condition with labels {description=..., state=ACTIVE, title=..., impactedProducts=..., impactedLocations=...} fired for Event with {...}
```

**踩坑**：格式 B 的 labels value 可能包含逗號，例如：
```
impactedLocations=['europe-central2', 'europe-west1']
```
簡單用逗號分隔 string 會破裂，解析出錯誤結果。

**解決方案**（`parseSHLabels` 函式）：用已知 key 名稱做 anchoring，依位置提取 value，而非直接 split 逗號。

---

## 過濾規則（避免噪音告警）

```go
// 跳過舊誤報更新（舊事件的 FALSE_POSITIVE 沒必要再通知）
if category == "FALSE_POSITIVE" && !IsNewEvent {
    return true // filter out
}

// 跳過不相關環境的進展更新
if category == "UPDATE" && relevance == "NOT_IMPACTED" {
    return true // filter out
}
```

**設計原則**：過濾「噪音」而非「全部更新」，CONFIRMED / RESOLVED 永遠送出。

---

## 安全設定

| 項目 | 做法 |
|------|------|
| Teams Webhook URL | 儲存在 Cloud Secret Manager，不 hardcode（URL 含 secret token） |
| Cloud Function 權限 | 只給 `secretmanager.secretAccessor` + `pubsub.subscriber`，最小權限 |
| Pub/Sub 加密 | 預設 Google-managed key，可升 CMEK（金融合規需求） |

---

## Teams Adaptive Card 設計

### 視覺識別
- **Emoji prefix**：🔴 緊急 / 🟡 監控中 / ✅ 解決，讓 SOC 掃一眼即知狀態
- **FactSet**：統一 key-value 呈現（事件 ID、狀態、觸發時間、受影響資源、location）
- **Markdown 清理**：移除原始 `*`、`-` 符號，改用 `•`（Teams 卡片 Markdown 渲染有限制）

### 優先級對應 Teams 行為
- Priority 3 → Teams 推播通知 + 聲音提醒（ACTIVE 事件）
- Priority 1 → 靜默更新到 channel（CLOSED / RESOLVED）

---

## 雲端資源調整判斷框架

**何時調整資源**（參考監控指標）：

| 指標持續超標 | 建議行動 |
|------------|---------|
| CPU 持續 > 80% | 升 VM 規格 or 調 Cloud Run concurrency |
| Memory 持續 > 75% | 升記憶體；檢查記憶體洩漏 |
| Cloud SQL Max Connection > 80% | 加 connection pooling（PgBouncer）or 升 tier |
| CDN cache hit rate < 80% | 調整 cache policy、TTL、URL 正規化 |
| Auto Scaling 持續在上限 | 升 scaling 上限（先設上限避免成本失控）|

**重要**：可自動擴展恢復的服務要設擴展上限（`maxInstances`），避免雲端成本超出預估值。

---

## 可複用 Pattern

1. **統一 AlertEvent interface**：多告警來源 → 單一輸出格式，新來源只需實作 interface
2. **Anchored label parsing**：當 value 本身含分隔符時，用 key 做 anchor 定位再提取 value
3. **Priority-driven notification**：根據事件嚴重度動態決定通知強度（推播 vs 靜默）
4. **Filter-first 設計**：`ShouldFilter()` 先決定是否送，避免 SOC channel 被噪音淹沒

---

## Concrete Numbers

| 指標 | 值 |
|------|------|
| 告警來源 | 2（Monitoring + Service Health） |
| Service Health 事件類型 | 6 種 |
| 過濾規則數 | 2 條核心過濾（FALSE_POSITIVE 舊事件、NOT_IMPACTED UPDATE） |
| 輸出管道 | Teams Webhook（Adaptive Card 格式） |

---

## CI/CD 異常處置

金融業 CI/CD 特殊考量（CathaySec 實務）：

- **手動執行 CI/CD** 需要申請特權帳號 + 跳板機 or PAM 提權，操作步驟留文件（稽核需要）
- **重複部署作業**（Rollback、Hotfix）必須由 SRE 放行，不能讓 RD 自行操作 Production
- **異常時間是否進版/退版**：SRE 需要先判斷是 code bug（退版）還是 infra 問題（不退版）再決定
- Rollback 步驟需要有對應 SOP 文件，不能臨時想

---

## References

- 實作來源：`~/Downloads/cathaysec-info/alerting_functions_V7.go`
- 簡報：`~/Downloads/cathaysec-info/teams_gcp_monitoring_v7.pptx`
- 監控維運報告：`~/Downloads/cathaysec-info/國證監控維運簡報_20251027.pptx`
- [Teams Adaptive Cards](https://adaptivecards.io/)
- [GCP Cloud Monitoring Alerting](https://cloud.google.com/monitoring/alerts)
- [GCP Service Health](https://cloud.google.com/service-health/docs)
- 關聯：[[gcp-landing-zone]]、[[iso27017-audit]]、[[sre-oncall-training-program]]
