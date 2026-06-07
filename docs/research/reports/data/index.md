# reports/data/INDEX.md

> **Type:** raw:data — CLAUDE.md 倉庫統計資料（claudemd-parse 產出）  
> **Updated**: 2026-06-07 | **Files**: 3  
> **Context**: [claudemd-best-practices](../2026-06-05-claudemd-best-practices.md)（443 repo 實證）

---

## 檔案清單

| 檔案 | 類型 | 說明 |
|------|------|------|
| [claudemd-parse.sh](claudemd-parse.sh) | shell | CLAUDE.md 解析腳本（從 GitHub 抓取 + 統計）|
| [claudemd-repos-unique.txt](claudemd-repos-unique.txt) | text | 443 個唯一 repo 清單 |
| [claudemd-stats.jsonl](claudemd-stats.jsonl) | jsonl | 每個 repo 的 CLAUDE.md 統計（行數 / byte / 規則數）|

---

## 用途

本目錄存放 `claudemd-best-practices` 報告的原始數據。如需驗證報告結論或重跑統計，從 `claudemd-parse.sh` 開始。

Parent: [../index.md](../index.md)
