# 高流量媒體架構

> **Source positions**: 壹蘋新聞網 NextApple（Cloud Architect）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 主導壹蘋雲端架構設計與調優）
> **Linted**: 2026-04-21

---

## Context

新聞媒體的流量模式與一般 SaaS 完全不同：**突發性極強**（重大新聞可在 5 分鐘內讓流量從 baseline 飆 10–50 倍）、**讀大於寫**（99%+ 是讀取）、**SEO 要求快速首屏**。這頁涵蓋比 `cdn-cache-tuning-97pct` 更廣的視角：從 origin 保護、CDN shield、Edge compute、到 abuse prevention 與即時發佈的 cache invalidation 策略。

---

## Core Methodology

### Step 1 — Origin 保護層（Origin Shield + Rate Limit）

- **What**: CDN 與 origin 之間加 Origin Shield（中間快取層）；在 CDN 邊緣設定 rate limit（per IP / per ASN）；origin 前加 WAF 過濾惡意請求
- **Why**: 97% hit rate 下仍有 3% 打到 origin；突發時（10x 流量）origin 還是要承受 10x × 3% = 0.3x 正常量，仍需保護。rate limit 防止爬蟲或 DDoS 把 origin 打死
- **Gotcha** [壹蘋]: 重大事件時爬蟲（SEO tools / 新聞聚合器）流量是真實用戶的 2–5 倍，rate limit 設太嚴誤封正常用戶，設太鬆放進爬蟲 → 需要 User-Agent + ASN + referrer 三維度複合判斷

### Step 2 — 突發流量應對：CDN 為第一道防線

- **What**: 目標是讓 origin 看到的流量幾乎恆定（decoupled from traffic spike）；CDN pop 全球分佈、自動 scale；origin 依 expected load 而非 peak 設計
- **Why**: 按 peak 設計 origin 成本 10–50x；CDN 對突發流量有邊際成本優勢（帶寬池分攤）
- **Gotcha** [壹蘋]: HTML 頁面 TTL 30–60s，突發期大量新請求繞過 CDN cache 打 origin（cache 還沒暖起來）→ 在 origin 加 `stale-while-revalidate` + in-process LRU cache（30s），雙重緩衝；見 [[cdn-cache-tuning-97pct]]

### Step 3 — 即時發佈 + Cache Invalidation 策略

- **What**: 新聞發佈觸發精確 path invalidation（不做全站 invalidation）；用 `Cache-Tag` / `Surrogate-Key` 讓一個標籤代表多個 URL
- **Why**: 全站 invalidation 讓 CDN cache 歸零，下一波請求全打 origin（thundering herd）；精確 invalidation 只清特定文章的 edge copy，影響範圍可控
- **Gotcha** [壹蘋]: CloudFront invalidation 有 API call 次數限制（1000 paths/月 免費），超量要付費；Cloudflare Cache Purge API 無限制但有 API rate limit（1200 calls/5min）— 高頻發布的媒體要做 invalidation queue + batch

### Step 4 — Edge Compute（輕量即時邏輯）

- **What**: CloudFront Functions / Cloudflare Workers 在邊緣處理：URL 正規化、A/B testing header 注入、GEO 導流、paywall token 驗證（不需打 origin）
- **Why**: Edge compute 延遲 < 1ms（vs origin round-trip 50–200ms）；paywall 驗證在邊緣完成，可挡住未授權抓取，且不增加 origin 負擔
- **Gotcha**: CloudFront Functions 是 JS-only 且 memory / CPU 極限（2ms CPU time）；複雜邏輯用 Lambda@Edge（但 cold start 50–500ms），需要在邊緣執行的才做，大邏輯保留 origin

### Step 5 — Abuse Prevention（爬蟲 + DDoS）

- **What**: WAF rule 組合：IP reputation list（AWS Shield Advanced / Cloudflare Bots）+ rate limit + CAPTCHA（對可疑 UA）+ L7 DDoS auto-mitigation
- **Why**: 媒體內容高價值（SEO 流量），爬蟲抓全站的誘因強；不防止爬蟲等於替競爭者做 content delivery
- **Gotcha** [壹蘋推論]: Bot management 要區分「好爬蟲」（Googlebot / Bingbot）和「壞爬蟲」（content scrapers）；誤封 Googlebot 導致 SEO 排名下降是嚴重事故 → 維護 allow list by verified crawler IP range

### Step 6 — 圖片服務（Image CDN + 轉碼）

- **What**: 圖片不走 origin server 直接服務；建立獨立 image pipeline：上傳 → S3/GCS → Image CDN（Imgix / Cloudflare Images / CloudFront + Lambda@Edge 轉碼）→ 邊緣即時 resize / format convert（WebP / AVIF）
- **Why**: 圖片占新聞流量 60–75%；用對格式（AVIF vs JPEG 省 50% 體積）+ CDN 直出（不過 origin）是最大的帶寬省法
- **Gotcha**: AVIF decode 在舊設備 CPU 消耗高（尤其低階 Android）；需要 `Accept` header 判斷用戶設備支援程度，按能力 serve 不同格式

---

## Concrete Numbers

| 指標 | 典型值 | 壹蘋場景 | 重要性 |
|------|-------|---------|--------|
| CDN cache hit rate | 65–80%（業界） | **97%** | 🔴 高 |
| Traffic spike 比率（重大新聞）| 5–10x | 估計 10–50x（24hr 滾動）| 🔴 高 |
| Origin request 降低（Origin Shield）| — | -60 to -80% | 🔴 高 |
| HTML TTL（列表頁）| 5–30s | 30–60s + SWR=600s | 🔴 高 |
| Image 佔帶寬比例 | 50–75% | 估計 60–70% | 🟡 中 |
| WebP vs JPEG 體積節省 | 25–35% | AVIF 可達 50% | 🟡 中 |
| Edge compute 延遲（CF Workers）| < 1ms | paywall 驗證 | 🟡 中 |
| WAF rate limit 誤封率目標 | < 0.1% | 正常用戶誤封 | 🔴 高 |
| CloudFront invalidation 免費額度 | 1,000 paths/月 | 高頻發布需 batch | 🟡 中 |

> [需 Zeuik 確認] 壹蘋實際 origin 機型數量、月流量 TB 數、WAF 供應商

---

## Anti-patterns（不要做）

1. **以 origin 為中心設計（origin-first）**
   - 問題：origin 按 peak 部署（10x 機器），平時 90% idle；成本 10x 但用不到
   - 解：CDN-first 設計，origin 按**穩態流量**設計，spike 由 CDN 吸收；origin 加 autoscaling 應對穿透流量

2. **全站 Cache Invalidation（發布時 purge all）**
   - 問題：全站清除後 CDN cache 瞬間歸零，下一波流量全打 origin → thundering herd → origin OOM 或 timeout
   - 何時踩：CMS 發布插件預設 purge all，未修改就上線，重大新聞發布時 origin 掛掉
   - 解：精確 path invalidation + `Cache-Tag` surrogate key grouping

3. **圖片走 origin 動態 resize**
   - 問題：每個 `?w=800&h=600` 組合 = 一次 origin CPU 消耗；同一張圖 10 種尺寸 = origin 10 份工作；無法有效 cache
   - 解：Image CDN（on-CDN 轉碼）或預先生成固定幾個 size（S/M/L），讓 CDN 有效 cache

---

## Decision Tree

```
設計媒體平台架構？

流量特徵確認
├─ bursty（突發）+ read-heavy → CDN-first（本頁）
└─ 均衡 + write-heavy → origin-first（不適用此頁）

CDN 選型
├─ AWS origin（S3 / ELB）→ CloudFront（無出流量費）
├─ 非 AWS + 高帶寬（> 10TB/月）→ Cloudflare（訂閱制）
└─ 混合 → 評估 CDN 費用 vs 架構複雜度

Origin 保護
├─ Origin Shield → 一定要開（-60% origin request）
├─ WAF → 一定要（bot + rate limit）
└─ DDoS 保護 → 預算夠 → AWS Shield Advanced / CF Enterprise

圖片策略
├─ 動態 resize 需求 → Image CDN（Imgix / CF Images）
├─ 固定幾種 size → CMS 預生成 + S3 + CDN 直出
└─ 省錢優先 → Lambda@Edge 轉碼（複雜但免外部服務費）

Cache Invalidation
├─ 高頻發布（> 100 文章/天）→ Cache-Tag + batch invalidation
└─ 低頻（< 10/天）→ 精確 path invalidation（CloudFront API）
```

---

## References

- 職涯段：`raw/career-summary.md#6-壹蘋新聞網-nextapple--cloud-architect`
- [AWS CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)
- [Cloudflare Cache Purge API](https://developers.cloudflare.com/cache/how-to/purge-cache/)
- [Cloudflare Workers — edge compute](https://developers.cloudflare.com/workers/)
- [AWS WAF — Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html)
- [Web Almanac 2023 — CDN chapter](https://almanac.httparchive.org/en/2023/cdn)
- 關聯：[[cdn-cache-tuning-97pct]]、[[nextapple-lessons]]、[[finops-savings-plans-roi]]
