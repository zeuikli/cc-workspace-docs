# 直播容量預測與分步啟動

> **Source positions**: KKStream / KKCompany 2019–2021（SRE + DevOps）
> **Last ingested**: 2026-04-22（from KKStream_Code codebase analysis）
> **Confidence**: high（直接從 telasa-promotion、infra-asg-manager、live_analytics 代碼提煉）
> **Linted**: 2026-04-22

---

## Context

流媒體服務的流量峰值**不是隨機的**，而是可以精確預測到分鐘的（直播開始前幾分鐘才有高峰，結束後快速下降）。KKStream 的 Telasa 日本直播服務需要在活動前完成 ASG 擴容、活動後立即縮回，避免浪費。

手動操作的問題：
- 每次活動都要人工計算「要啟動幾台機器」
- 啟動太早 → 閒置浪費；太晚 → 流量峰值缺資源
- 遺忘或錯誤設定的人為失誤風險高

`telasa-promotion` 解決方案：**促銷排程自動化** — 輸入 Excel 活動時程 → 自動計算容量 → 建立 CloudWatch EventRule schedule → 自動執行 scale up/down。

---

## Core Methodology

### Step 1 — 輸入：活動時程表（Excel）

```
促銷時間表包含：
- 活動名稱、開始時間、結束時間
- 預期觀眾數（peak）
- 對應 ASG tag（哪些服務需要擴容）
```

`TimeTable.parse_excel()` 解析 Excel，`aggregate_events_time()` 合併重疊時段（多個活動在同一 30 分鐘窗口）。

### Step 2 — 容量計算

```python
# telasa-promotion/promotion.py

for asg in auto_scaling_groups:
    for start_time, end_time, plan in events_time:
        asg.increment = plans.get(asg.auto_scaling_group_tag_name, plan)
        if asg.increment <= 0:
            continue

        step = ceil(asg.increment / asg.batch_increment)  # 分幾批啟動
        _end_of_start_time = start_time - timedelta(seconds=asg.warmup)
        _start_of_start_time = _end_of_start_time - timedelta(seconds=(step - 1) * asg.interval)

        base_capacity = asg.estimate_base_instance_capacity(start_time, end_time)
        total_capacity = base_capacity + asg.increment
```

**關鍵參數**：
- `warmup`：機器啟動到可接流量的時間（秒），必須在活動前完成
- `batch_increment`：每批啟動幾台（避免 thundering herd）
- `interval`：批次間間隔（秒）
- `step`：需要幾批完成整個擴容

### Step 3 — 輸出：CloudWatch EventRule schedule

每個活動生成兩條 EventRule：
1. `start_time - warmup` → desired = base + increment（開始擴容）
2. `end_time` → desired = base（縮容回 baseline）

EventRule 精確到分鐘，完全自動執行，不需要人工操作。

---

## 分步啟動設計（防 Thundering Herd）

**問題**：一次啟動 50 台機器，EC2 API rate limit 被打滿，加上 user data 腳本同時跑，容易造成 network/DNS 壓力。

**解法**：分批啟動

```
總需要 +30 台，batch_increment=10，interval=120s

Schedule:
  T-10min: desired = baseline + 10  （第一批）
  T-8min:  desired = baseline + 20  （第二批）
  T-6min:  desired = baseline + 30  （第三批）
  T-0min:  活動開始，全部機器已就緒
```

**warmup 計算**：
```
total_warmup = warmup（單機啟動時間）+ (step - 1) * interval
例：warmup=120s，step=3，interval=120s → total_warmup = 120 + 240 = 360s（6 分鐘前開始）
```

---

## ASG 版本管理（infra-asg-manager）

直播容量管理的基礎是穩定的 ASG 定義。`infra-asg-manager` 用 GitOps 管理 Launch Config：

```python
# infra-asg-manager/cicd-helpers/run.py

def get_modified_path_since_last_commit(git_root, exclude_filter=None):
    repo = git.Repo(git_root)
    return set(
        os.path.dirname(os.path.abspath(os.path.join(git_root, df.b_path)))
        for df in repo.commit('HEAD~1').diff()
        if not df.change_type.startswith('D') and (not exclude_filter or exclude_filter(df.b_path))
    )

# git push lc_cfg.yml → CI 自動 create 新 LC 版本 → 更新 ASG → 清除舊 LC
```

**GitOps 效益**：
- 每個 LC 版本有 git hash，rollback = git revert + push
- 自動清除舊 LC（AWS 有 100 個/region 硬限制）
- 不需要人工 AWS Console 操作，降低人為失誤

---

## 直播系統監控指標（live_analytics）

直播期間需要監控：

| 指標 | 來源 | 告警閾值參考 |
|------|------|------------|
| avg_viewer（分鐘級）| RedAsh API | 低於預期 20% → 可能有播放問題 |
| bandwidth utilization | CloudFront | > 85% → 考慮提前擴容 |
| segment error rate | origin server logs | > 1% → 觸發 p0 告警 |
| ASG instance healthy count | CloudWatch | < desired → 立即調查 |

`live_analytics/gen_report.py` 在直播結束後自動生成效能報告，包含觀眾數曲線、peak bandwidth、error rate，為下次活動的容量計算提供數據。

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| warmup 時間（KKStream）| 60–120s | EC2 user data + service healthcheck |
| batch_increment | 10 台/批 | 避免 API rate limit |
| batch interval | 120s | 讓前一批完全健康再啟動下批 |
| total_warmup（3 批次）| ~6 分鐘 | scale up 應在活動開始 6+ 分鐘前 |
| 縮容後等待時間 | connection_draining（300s）| ALB draining 完成前不刪機器 |

---

## Anti-patterns（不要做）

1. **一次 desired 跳到 max**
   - 問題：50 台同時啟動，EC2/DNS/NFS 承受瞬間大量 bootstrap request
   - 解：batch_increment + interval 分步

2. **warmup 沒計算服務啟動時間**
   - 問題：EC2 起來了，但 service health check 要 90s，前 90s 流量打到 unhealthy instance
   - 解：warmup = EC2 boot time + service startup time + buffer（×1.5）

3. **縮容沒等 connection draining**
   - 問題：活動結束立即縮回，有 viewer 仍在用的 connection 被強制切斷
   - 解：scale down 設定 ALB deregistration delay（300s）再縮

4. **不考慮時區**
   - 問題：Telasa 日本活動用 JST，CloudWatch EventRule 是 UTC，差 9hr
   - 解：`telasa-promotion` 明確做 JST → UTC 轉換，並在 XLSX 輸出確認時區標記

---

## Decision Tree

```
直播/促銷活動容量規劃

預期觀眾數與現有 baseline 差距
├─ < 20%（baseline 足夠）→ 不需擴容，監控即可
├─ 20–100%（中等擴容）→ 分 2–3 批，活動前 10–15 分鐘開始
└─ > 100%（大型活動）→ 分 4–5 批，活動前 20–30 分鐘開始 + 提前壓測

活動類型
├─ 定期（每週直播）→ 固定 EventRule cron schedule
├─ 不定期（促銷）→ telasa-promotion 動態建立 EventRule
└─ 突發（新聞直播）→ 手動 scale + 事後建立預警機制

縮容策略
├─ 活動結束後 30 分鐘 → 開始縮容（讓尾巴流量消化完）
├─ connection draining 設 300s → 避免切斷中 session
└─ 縮容到 baseline × 1.1 → 保留 10% buffer（下次快速啟動）
```

---

## Cross-references

- 關聯：[[kkstream-lessons]]、[[aws-step-functions-patterns]]、[[finops-savings-plans-roi]]、[[aws-alarm-as-code]]

## References

- Code source: `telasa-promotion/promotion.py`、`infra-asg-manager/cicd-helpers/run.py`、`live_analytics/gen_report.py`（local only，未公開）
- 職涯段：`raw/career-summary.md#4-kkstream--kkcompany--sre--devops--dba--architect`
