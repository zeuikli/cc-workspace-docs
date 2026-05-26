# Blog #10 — How to upgrade AWS PostgreSQL version with minimum downtime

> **Source**: https://medium.com/@zeuik/how-to-upgrade-aws-postgresql-version-with-minimum-downtime-1107b3aab901
> **Published**: 2022-08-21
> **Archived**: 2026-04-21 (WebFetch summary; full text requires manual archive)

---

## Article Summary

Zeuik 於 2022-08 發表的 AWS RDS PostgreSQL 升級實戰文，記錄 **RDS 版本從 9.6.18 升級到 14.1** 的真實經驗，總 downtime 約 4 小時（測試環境 2–3 小時），maintenance window 規劃 8 小時。

## Upgrade Path（實際執行）

1. Create replica（9.6.18）
2. Upgrade replica → 9.6.24（minor version first）
3. Promote replica to single instance
4. Upgrade 9.6.24 → 14.1（major version jumps）
5. Apply RDS system upgrades + parameter group config
6. Run `ANALYZE` on tables for DB pre-warming
7. Exit maintenance mode

## Key Findings

- **Actual downtime**: ~4 hours（production）/ 2–3 hours（test）
- AWS 自動完整備份時長是主要瓶頸
- 大型 DB cluster 建議**漸進式升級**：10.20 → 11.5 → 12.3 → 13.6，不要跨多個主版本
- 要**分開設定**：writer/reader parameter groups
- **用真實 production workload 驗證**，不要只靠 synthetic load test

## Relation to Wiki Page `redis-pg-zero-downtime.md`

此 blog 描述的是 **RDS Managed 服務的 "minimum downtime" 方案**（~4hr），而 wiki page 描述的是 **self-managed PG + pglogical 的 "true zero-downtime" 方案**（0s downtime）。兩者適用場景不同：

| 方案 | Downtime | 適用環境 | 複雜度 |
|------|----------|---------|-------|
| Blog #10（RDS replica-promote） | ~4 hr | AWS RDS managed | 低 |
| Wiki page（pglogical + dual-write）| 0 s | self-managed PG + microsec 延遲場景 | 高 |

SoundOn 之後的高要求場景（microsec latency）才推進到完整零停機；早期（2022）的 AWS RDS 環境採 "minimum downtime" 已是合理工程決策。

## Tags

AWS, PostgreSQL, RDS, Database Migration, Downtime
