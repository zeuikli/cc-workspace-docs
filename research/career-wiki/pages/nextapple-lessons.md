# 壹蘋 NextApple — Lessons Learned

> **Tenure**: May 2022 – May 2023（concurrent sub-project during SoundOn，user confirmed）| **Role**: Cloud Architect
> **Last ingested**: 2026-04-21 | **Updated**: 2026-05-08 (confirmed dates + structure)
> **Confidence**: high
> **Note**: 壹蘋是 SoundOn 任職期間的兼職/外包專案（非獨立僱用關係），PDF 在 SoundOn 條目下列出此項工作

---

## Context

台灣新聞媒體，bursty + image-heavy 流量 + 24×7 reliability。CDN cache hit 從業界常見 65–75% 推到 **97%**。全程參與：AWS 環境建置（VPC / EC2 / RDS）+ Terraform 模組化 + CI/CD pipeline（user confirmed）。

## Key Lessons

1. **CDN cache key 縮減是最便宜的 hit rate 改善**
   - 移 utm/tracking 參數即可把 hit rate +10–15 pp
   - Vary: User-Agent 是隱藏殺手；常被舊程式碼帶出去

2. **hash-named image 是「免費」的 1yr TTL**
   - Article image 用 `/img/{article-id}-{content-hash}.webp` → immutable
   - Browser + CDN 雙層緩存，origin 請求近零

3. **stale-while-revalidate 是穩定性保險**
   - 沒 SWR 整點大量快取同時過期，瞬間 1000 請求全打 origin
   - `stale-while-revalidate=600` 讓 peak hour 仍回舊版 + 背景更新

4. **Provider 選型是數學題，不是流行問題**
   - AWS S3 origin → CloudFront 免出流量；非 AWS origin → Cloudflare Pro 月付式
   - 50TB/月場景差 70% 成本
   - 見 [[cdn-cache-tuning-97pct]]

5. **新聞稿發佈系統 = 快取 invalidation 的敵人**
   - CMS 產圖帶 timestamp query param → 每次發佈破壞快取
   - 要從 CMS 源頭改成 content-hash naming

## What I'd Do Differently

- **不** 用 `Vary: User-Agent`；改 `<picture>` tag + JS 客戶端適應
- 新聞大事件前 **預熱 CDN**（調 API 主動把熱門 URL 拉進 edge）
- 設 alert：hit rate 1 小時跌 5% + 無新 CMS 發佈 → invalidation 錯誤

## Cross-references

- 核心 pages：[[cdn-cache-tuning-97pct]]、[[high-traffic-media-arch]]（待建立）
- 延伸：[[haproxy-patterns]]（rate limiting 反爬蟲）

## References

- `raw/career-summary.md#6-壹蘋新聞網-nextapple--cloud-architect`
- Medium blog #6（2023-03）：Cloudflare + S3 成本最佳化
- Medium blog #7（2022-11）：Carrierwave + CloudFront
