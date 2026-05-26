# GHA career-wiki-ingest Workflow — Local Dry-Run Verification

> **Test date**: 2026-04-21
> **Target**: `.github/workflows/career-wiki-ingest.yml`
> **Purpose**: 本地模擬 GHA runner 會執行的步驟，確保 merge 到 main 後第一輪自動執行無誤

---

## Workflow 排程

- Trigger: `cron: '15 * * * *'`（每小時 :15）+ `workflow_dispatch`
- 交錯於 `daily-digest.yml`（每小時 :00）15 分鐘後執行，確保 digest 已產出
- Runner: `ubuntu-latest`, timeout 10 min, concurrency 鎖

## 本地 Dry-Run 結果

### Step 1：YAML 語法驗證

```
python3 -c "import yaml; y = yaml.safe_load(open('.github/workflows/career-wiki-ingest.yml')); ..."
→ YAML OK, jobs: ['ingest-queue']
```

✅ GitHub Actions 解析無誤。

### Step 2：`python3 scripts/wiki-ingest.py`（無需 deps，純 stdlib）

```
Loading wiki index from INDEX.md...
  Found 21 wiki pages with keywords
  Loaded 20 articles from latest-combined.md
  (skipped, not found: latest-ai.md)
  (skipped, not found: latest-security.md)
Total articles: 20
Generating ingest queue...
Written: /home/user/cc-workspace/research/career-wiki/ingest-queue.md
```

✅ Queue 產出正常。`latest-ai.md` + `latest-security.md` 在 GHA 環境下會存在（ai-digest.yml + security-digest.yml 另外排程產出）。本地不存在為正常狀況。

### Step 3：`bash scripts/wiki-lint.sh`

```
Total pages:        28
Size ≤ 400:         28 (100%)
Concrete Numbers:   28 (100%)
Fresh (< 90d):      28 (100%)
Non-orphan:         28 (100%)
Broken links:       (非致命警告)
Lint Score:         100 / 100 ✅ PASS
```

✅ Lint 通過。

### Step 4：Commit/push 流程（GHA 自動執行）

Workflow 步驟：
```yaml
git add research/career-wiki/ingest-queue.md research/career-wiki/lint-report.md
git diff --staged --quiet && exit 0   # 無變動就不 commit
git commit -m "chore(wiki): ingest queue + lint report ..."
for attempt in 1 2 3 4; do ... done    # retry push
```

✅ 使用 exponential backoff（2s/4s/8s/16s）重試；`concurrency` 鎖避免與其他 workflow 衝突。

## Expected Behavior Post-Merge

1. **首輪執行時間**：branch merge 到 main 後，下一個整點的 :15 分鐘
2. **首輪產出**：
   - `research/career-wiki/ingest-queue.md`（20–30 條相關文章 × top-3 suggested pages）
   - `research/career-wiki/lint-report.md`（score 100/100）
3. **自動 commit**：`chore(wiki): ingest queue + lint report YYYY-MM-DD HH:MM`
4. **Zeuik 決策**：手動執行 `/autoresearch:wiki ingest` 根據 queue 做 LLM-level ingest

## Known Considerations

- **GHA 環境差異**：本地沒有 `latest-ai.md` / `latest-security.md`，但 GHA 環境這兩個檔案由 ai-digest.yml + security-digest.yml 每日產出
- **Token 不消耗**：本 workflow **完全不呼叫 LLM**，純 mechanical（Python stdlib + bash）。LLM 互動由 Zeuik 主動觸發
- **Broken links warning**：13 個 `[[wiki-links]]` 指向尚未建立的 pages（依 ROADMAP 預計後續補齊），非阻塞

## Verification Result

| 項目 | 狀態 |
|------|------|
| YAML 語法 | ✅ |
| wiki-ingest.py 執行 | ✅ |
| wiki-lint.sh 執行 + score ≥ 85 | ✅（100/100）|
| 自動 commit/push 流程 | ✅（邏輯正確；實際 merge 後驗證）|
| 無 LLM 成本 | ✅（純 mechanical）|

**結論**：本地驗證通過。Branch merge 後可預期首輪自動執行成功。
