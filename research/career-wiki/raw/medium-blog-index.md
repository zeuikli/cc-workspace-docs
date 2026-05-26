# Zeuik Li Medium Blog — Raw Index

> **Source**: https://medium.com/@zeuik
> **Fetched**: 2026-04-21
> **Status**: Index of 10 articles. Core tech articles archived locally; lifestyle/career articles indexed only.

---

## Article Catalog (by relevance to career-wiki)

### 🔴 Core Tech — archived locally in `raw/blog-archive/`

| # | Title | Date | Maps to Wiki Page |
|---|-------|------|-------------------|
| 10 | [How to upgrade AWS PostgreSQL version with minimum downtime](https://medium.com/@zeuik/how-to-upgrade-aws-postgresql-version-with-minimum-downtime-1107b3aab901) | 2022-08-21 | [[redis-pg-zero-downtime]] |
| 8 | [How to optimize PostgreSQL Database Size and SQL Query](https://medium.com/@zeuik/how-to-optimize-postgresql-database-size-and-sql-query-7d1ec635c5ea) | 2022-09-05 | [[postgres-microsec-tuning]] (Session 2) |
| 6 | [Cloudflare CDN feat. AWS S3 — 讓 CDN 變便宜吧](https://medium.com/@zeuik/cloudflare-cdn-feat-aws-s3-讓cdn變便宜吧-3aad07294933) | 2023-03-15 | [[cdn-cache-tuning-97pct]] (Session 2) |

### 🟡 Tech — index only, fetch on demand

| # | Title | Date | Maps to Wiki Page |
|---|-------|------|-------------------|
| 9 | [How to build AWS Lambda with Ruby and PostgreSQL](https://medium.com/@zeuik/how-to-build-aws-lambda-with-ruby-and-postgresql-4b6ee634bf04) | 2022-09-03 | [[stripe-serverless-fintech]] (Session 3) |
| 7 | [Carrierwave 上傳檔案到 S3 Bucket + Cloudfront](https://medium.com/@zeuik/如何使用carrierwave上傳檔案到s3-bucket-並搭配cloudfront-與基本設定-9bac089bcc69) | 2022-11-15 | [[cdn-cache-tuning-97pct]] (Session 2) |

### 🟢 Career / Certification — index only

| # | Title | Date | Maps to |
|---|-------|------|---------|
| 4 | [如何準備 AWS Certified Solutions Architect — Professional](https://medium.com/@zeuik/2023年-如何準備-aws-certified-solutions-architect-professional-28da5b6dd817) | 2023-06-15 | [[aws-sa-pro-prep]] (Session 3) |
| 3 | [考取 AWS Certified Solutions Architect — Professional 證照心得](https://medium.com/@zeuik/2023年-考取-aws-certified-solutions-architect-professional-證照心得-ec9b40fe0a94) | 2023-08-25 | Same |
| 1 | [<2023年> 多工斜槓資深工程師指南](https://medium.com/@zeuik/2023年-多工斜槓資深工程師指南-fdab7ff7e4e5) | 2023-11-27 | senior-architect agent context — 職涯哲學 |
| 5 | [如何面對被裁員並重新開始新的生活](https://medium.com/@zeuik/如何面對被裁員並重新開始新的生活-e353741764a9) | 2023-06-09 | 個人成長，不直接映射 |

### ⚪ Lifestyle / Wellness

| # | Title | Date |
|---|-------|------|
| 2 | [你有多久沒注意自己的心率和壓力了？<2024 更新>](https://medium.com/@zeuik/你有多久沒注意自己的心率和壓力了-4bbf4aa31d8c) | 2023-11-11 |

---

## Ingest Strategy

### Session 1（本次）
- ✅ 建立此索引
- ✅ 抓取文章 #10 作為 `pages/redis-pg-zero-downtime.md` 的一手來源補強
- ⏳ 文章 #8、#6 抓取後儲於 `raw/blog-archive/`，供 Session 2 使用

### Session 2
- 抓取並整合 #8（PostgreSQL 效能優化）→ 產出 `pages/postgres-microsec-tuning.md`
- 抓取並整合 #6、#7（CDN + S3）→ 產出 `pages/cdn-cache-tuning-97pct.md`

### Session 3
- 抓取 #9 → 整合進 `pages/stripe-serverless-fintech.md`
- 抓取 #3、#4 → 產出 `pages/aws-sa-pro-prep.md`
- 抓取 #1 → 提煉進 senior-architect agent 的「Zeuik 風格」prompt

### Cross-reference principle
- Wiki pages 裡若引用 blog 文章，必須標註：`Source: Zeuik blog #N "Title" (YYYY-MM-DD)`
- 遵守著作權規則（CLAUDE.md anthropic-insights.md）：引文 ≤ 15 字、單源單引文、paraphrase 原則

---

## Lint Note

Blog 最後一篇寫於 2023-11，Zeuik 過去 2 年轉向 GitHub/workspace 而非 Medium，本索引不預期會大量擴增。新技術內容預期走 workspace `research/ai-articles/` 或直接入 wiki pages。
