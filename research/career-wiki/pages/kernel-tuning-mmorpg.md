# Linux Kernel Tuning for MMORPG

> **Source positions**: Gamania 2013–2016（天堂 M 系統工程師）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 150+ racks、400+ VMs 實戰）
> **Linted**: 2026-04-21

---

## Context

MMORPG peak loads（150+ racks、400+ VMs、50K+ 並發）需極端 kernel 調校。Filesystem panic 成本極高；accept queue 滿會直接拒連。本頁記錄 Gamania 天堂 M 期間累積的 5-step tuning 流程。

---

## Core Methodology

### Step 1 — sysctl 連接池

- **What**: 拉高 `net.core.somaxconn`、TCP backlog
- **Why**: Tomcat/Apache accept queue 受 kernel 限制；預設 128 對 50K+ 連接不足
- **Gotcha** [Gamania]: somaxconn 3000–5000 後，reject rate 從 8% 降至 < 1%（Cacti monitoring）[需 Zeuik 確認精確值]

### Step 2 — I/O Scheduler 選型

- **What**: SSD → `noop` / `kyber`；HDD → `deadline` / `cfq`
- **Why**: DB-intensive I/O；cfq 公平性好但延遲高；SSD 用 noop 減損耗
- **Gotcha** [Gamania]: ESXi 5.0→6.0 升級時混用 scheduler，iSCSI NAS 延遲抖動；改全 SSD `noop` 後穩

### Step 3 — TCP 棧參數

- **What**: `net.ipv4.tcp_tw_reuse=1`、調高 backlog、CUBIC（2013 年 BBR 未普及）
- **Why**: TIME_WAIT 堆積 → port 耗盡
- **Gotcha** [Gamania]: `tw_reuse=1` 全開後，某些長連客戶端復連 timeout；改保守設定（延遲重用）

### Step 4 — File Descriptor 與 Open Files

- **What**: `fs.file-max`（系統）+ 每 process ulimit -n
- **Why**: 每遊戲連線 = 1 socket；150 racks × 400 VMs × 每機 50+ 連線 = 龐大 FD pool
- **Gotcha** [Gamania]: 未同步調高 Java/Tomcat thread pool，kernel 有 FD 但 app 仍阻塞

### Step 5 — Kernel Panic + Crash Dump

- **What**: 配 kdump / crash dump location、sysrq magic key for emergency recovery
- **Why**: Panic 時快速根因診斷；SysRq 允許不重啟故障復原
- **Gotcha** [Gamania]: iSCSI NAS crash dump 可能失敗（network down）→ 改本機 SSD 作 dump target

---

## Concrete Numbers

| 指標 | 值 | 場景 |
|------|----|------|
| `net.core.somaxconn` | 128 → **3000** | 預設 vs Gamania 調優 |
| `fs.file-max` | 65536 → **2,000,000** | 預設 vs 150+ racks |
| `net.core.netdev_max_backlog` | 1000 → 5000 | TCP 接受隊列優化 |
| Kernel panic 頻率 | 1 次 / 14 天 → **1 次 / 90 天** | 優化前後 2013–2015 |

> [需 Zeuik 確認] 精確 sysctl 值與 kernel panic 實際頻率

---

## Anti-patterns

1. **全局激進調優（一次改 20+ 參數）**
   - 問題：peak hour connection rejection 反升至 12%
   - 解：**迭代式**（每次 1–2 參數 + 1 週監控）

2. **忽略 VMware ESXi scheduler conflict**
   - 問題：ESXi 與 guest scheduler 衝突，DB iSCSI 延遲抖動誤診為網路
   - 解：檢查 VM CPU contention；guest 調優前先確認 hypervisor 層

---

## Decision Tree

```
MMORPG 連接拒絕率高？
├─ dmesg 有 kernel panic？
│  └─ 是 → 先 Step 5（recovery）再 Steps 1–4
└─ 無 panic
   ├─ TCP accept queue 滿（netstat -s | grep rejected）？
   │  └─ 是 → Step 1（somaxconn）
   ├─ I/O 寫延遲 > 10ms？
   │  └─ 是 → Step 2（scheduler）
   └─ File descriptor 耗盡（lsof count）？
      └─ 是 → Step 4
```

---

## References

- 職涯段：`raw/career-summary.md#1-gamania-遊戲橘子--system-engineer`
- [Linux kernel networking docs](https://www.kernel.org/doc/html/latest/networking/)
- `man 7 tcp`
- 關聯：[[haproxy-patterns]]、[[mysql-redis-cluster-ha]]、[[gamania-lessons]]
