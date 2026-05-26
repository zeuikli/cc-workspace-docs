# CDN Cache Tuning — 新聞媒體 97% Hit Rate

> **Source positions**: 壹蘋 NextApple（Cloud Architect）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 實戰 97% cache hit rate）
> **Linted**: 2026-04-21

---

## Context

新聞媒體流量特徵：**bursty（突發）+ read-heavy + image-heavy**（圖片占 60–75%）。97% cache hit rate 意味 100 個請求僅 3 個打 origin；80% hit rate 則 20 個 → **origin 承載差 6.7 倍**。每 1% hit rate 提升直接翻倍 origin 處理能力延伸。此頁整合壹蘋實戰 + [Medium Blog #6](https://medium.com/@zeuik/cloudflare-cdn-feat-aws-s3-%E8%AE%93cdn%E8%AE%8A%E4%BE%BF%E5%AE%9C%E5%90%A7-3aad07294933) 的 Cloudflare + S3 成本最佳化。

---

## Core Methodology

### Step 1 — 流量特徵與快取可能性分析

- **What**: RUM 7 天流量 by asset type（HTML / image 小大 / JSON API / JS/CSS），統計每類的獨特 URL 與重複頻率
- **Why**: 天然可快取比例決定上限；新聞典型 70–80% 可快取
- **Gotcha** [壹蘋]: 新聞 CMS 產圖常帶 timestamp query param，URL 每次不同直接破快取

### Step 2 — Cache Key 縮減

- **What**: 移除 utm / tracking / timestamp；Vary header 只保留 `Accept-Encoding` + `CloudFront-Is-Mobile-Viewer`
- **Why**: Cache key = URL + whitelisted params + whitelisted headers；預設包含全部會爆快取項
- **Gotcha**: `Vary: User-Agent` 是最常見殺手（每個 UA 版本一份）；hit rate 可從 95% 跌到 30%

### Step 3 — TTL 分層策略

- **What**: Immutable（hash-named image）→ 1 年；HTML（列表 / 文章）→ 30–60s + `stale-while-revalidate=600`；API JSON metadata → 5 min
- **Why**: `Cache-Control: public, immutable, max-age=31536000` 讓 browser + CDN 都緩存；SWR 窗口內回舊版本 + 非同步更新
- **Gotcha** [壹蘋]: 沒設 SWR 時整點所有 HTML 同時過期 → 1000 請求同時打 origin（快取穿透）

### Step 4 — Origin Shield / Tiered Cache

- **What**: CloudFront Origin Shield（介於 edge 與 origin 之間的中間快取層）
- **Why**: 200+ edge 各自獨立請求 origin vs 所有 edge 先查 Shield，**origin 請求減 60–80%**
- **Gotcha**: Shield 費 ~$0.005/10000 請求，但 origin 頻寬成本節省遠大於此

### Step 5 — Provider Selection（Cloudflare vs CloudFront）

- **What**:
  - CloudFront：AWS 原生，S3 出流量免費，按用量計費
  - Cloudflare Pro $20/月含無限頻寬，自有網路，DDoS 內建
- **Why**: 非 AWS origin + 50TB/月流量 → Cloudflare $20 vs CloudFront ~$4,250（**差 70%** [Blog #6 核心案例]）；AWS S3 origin → CloudFront 免出流量費用遠低於 Cloudflare
- **Gotcha**: [需 Zeuik 確認] 壹蘋具體選用哪家 + 月成本數字

### Step 6 — Monitoring

- **What**: `BytesServedFromCache / Requests` 算實際 hit rate；by edge location / country / asset type 分組
- **Why**: hit rate +5% 應對應 origin request -10%、bandwidth -10%；不對齊代表有洩漏
- **Gotcha**: hit rate 短期跌 5%+ 且無新發布 → 快取錯誤或 invalidation 過度

---

## Concrete Numbers

| 指標 | baseline | 優化後 | 重要性 |
|------|---------|--------|-------|
| Cache hit ratio | 65–75% | **97%**（壹蘋）| 🔴 高 |
| Image TTL | 300s | 1 year（immutable URL）| 🔴 高 |
| HTML TTL | 5–10s | 30–60s + SWR=600s | 🔴 高 |
| API metadata TTL | 30s | 5 min | 🟡 中 |
| Origin request reduction（w/ Shield）| baseline | **-60 to -80%** | 🔴 高 |
| CloudFront bandwidth cost | $0.085/GB | 優化後 -25–40% | 🟡 中 |
| Cloudflare Pro vs CFront（非 AWS origin, 50TB）| — | **差 70%**（$20 vs $4,250）| 🔴 高 |
| Origin server load（peak）| N req/sec | N × 0.03（97% hit）| 🔴 高 |

> [需 Zeuik 確認] 壹蘋 CDN 實際選型、月成本、invalidation 頻率

---

## Anti-patterns

1. **`Vary: User-Agent` 破壞快取**
   - 問題：每個 UA 版本一份快取；50 UA → 50 份
   - 解：改 `CloudFront-Is-Mobile-Viewer`（CDN 自動）或 `<picture>` tag + JS 客戶端適應

2. **大小寫混亂 + 動態 path**
   - 問題：`/Article/123` vs `/article/123` CDN 視為不同資源；用 UUID 作 key 每次發布都是新 URL
   - 解：源端統一大小寫；image 用 **content hash**（非 timestamp / UUID）命名

3. **沒設 stale-while-revalidate → 整點穿透**
   - 問題：HTML TTL=30s 且無 SWR，整點所有快取同時過期，1000 請求全打 origin
   - 解：SWR=600s；回舊版 + 背景更新一份

4. **忽略 HTTP/3 + Brotli + image CDN**
   - 問題：CDN 只做 HTTP 層快取；沒用現代 codec（AVIF / WebP）與傳輸壓縮
   - 解：開 Brotli、HTTP/3（QUIC）、image CDN on-the-fly 轉碼

---

## Decision Tree

```
建立 CDN 快取策略？

靜態資產為主（image / CSS / JS）
├─ URL 帶 content hash → TTL 1 year（immutable）
└─ Provider：
   ├─ AWS S3 origin → CloudFront（無出流量費）
   └─ 外部 origin → Cloudflare（訂閱式更便宜）

新聞媒體（HTML + bursty）
├─ HTML 列表 → 30–60s + SWR=600s
├─ 文章詳頁 → 60s + soft invalidation
├─ Image → hash-named immutable + timestamp-named 快期汰舊
├─ Origin Shield → 減 origin 衝擊
└─ RUM 監控 → hit rate 目標 95–99%

電商 / 時效性高
├─ 商品列表 → 5 min TTL
├─ 商品詳 → 1 min + SWR=120s
├─ 購物車 / 訂單 → `Cache-Control: private, no-cache`
└─ 不用 Origin Shield（origin request 多浪費）
```

---

## References

- 職涯段：`raw/career-summary.md#6-壹蘋新聞網-nextapple--cloud-architect`
- **Zeuik blog #6**（2023-03）：[Cloudflare CDN feat. AWS S3 — 讓 CDN 變便宜吧](https://medium.com/@zeuik/cloudflare-cdn-feat-aws-s3-%E8%AE%93cdn%E8%AE%8A%E4%BE%BF%E5%AE%9C%E5%90%A7-3aad07294933)
- **Zeuik blog #7**（2022-11）：[Carrierwave S3 + Cloudfront](https://medium.com/@zeuik/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8carrierwave%E4%B8%8A%E5%82%B3%E6%AA%94%E6%A1%88%E5%88%B0s3-bucket-9bac089bcc69)
- [AWS CloudFront Cache Policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
- [CloudFront stale-while-revalidate support (2023-05)](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-cloudfront-stale-while-revalidate-stale-if-error-cache-control-directives/)
- [CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)
- [Akamai: Cache Hit Ratio is the Key Metric](https://www.akamai.com/blog/edge/the-key-metric-for-happier-users)
- 關聯：[[high-traffic-media-arch]]（Session 3）、[[finops-savings-plans-roi]]
