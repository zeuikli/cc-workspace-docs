# HAProxy Load Balancing Patterns for MMORPG

> **Source positions**: Gamania 2013–2016
> **Last ingested**: 2026-04-21
> **Confidence**: high（天堂 M HAProxy 主力 LB）
> **Linted**: 2026-04-21

---

## Context

Gamania 150+ racks、50K+ 並發遊戲連線、millisecond 級 failover、**abuse prevention（bot + DDoS）** 需求。本頁記錄 HAProxy 在 MMORPG 場景的 5 個 production pattern。

---

## Core Methodology

### Step 1 — Frontend / Backend / Listen 架構

- **What**: Listen socket → frontend rules → backend pool
- **Why**: 遊戲連線長連（keep-alive）需 sticky session + high throughput
- **Gotcha** [Gamania]: 初期混用 HTTP mode 與 TCP mode → routing confusion；改**清晰分離** game protocol（TCP）與 API（HTTP）

### Step 2 — Health Check + Cookie Sticky

- **What**: TCP check + HTTP check；game → TCP + cookie persistence；API → HTTP check_path
- **Why**: 遊戲伺服器故障需 < 1s 偵測；sticky cookie 確保玩家連回同伺服器
- **Gotcha** [Gamania]: 初 check interval 30s 過長，Tomcat 掛但 HAProxy 未察 → 玩家掉線；改 **5s interval + 連續 3 fail** 才判定故障

### Step 3 — Rate Limiting + Abuse Prevention

- **What**: `stick-table` tracking IP、ACL for bot detection、connection limit per IP
- **Why**: Peak hour 易遭 bot spam + DDoS
- **Gotcha** [Gamania]: stick table 記憶體爆（100K+ IPs）→ 限制表大小 + 過期時間 10min

### Step 4 — SSL Termination + HTTP/2

- **What**: HAProxy 終止 TLS；backend 走 clear text（遊戲 binary 不需 HTTP/2）；API 層啟 HTTP/2
- **Why**: HAProxy offload TLS → backend CPU 不飆
- **Gotcha** [Gamania]: AES-256 cipher CPU 成本高 → 改 **AES-128 + ChaCha20** 平衡安全與效能

### Step 5 — Stats Page + Monitoring

- **What**: HAProxy `/stats` + Grafana dashboard + Cacti 監控連線數 / 錯誤率 / backlog
- **Why**: Peak hour 需即時看 backend 健康、reject rate、延遲
- **Gotcha** [Gamania]: stats page 無認證暴露外網 → 限 IP + HTTP basic auth

---

## Concrete Numbers

| 指標 | 值 | 場景 |
|------|----|------|
| Peak concurrent connections | 50K+ | 單機 HAProxy |
| Backend pool size | 40–60 servers | Tomcat / game server |
| Health check interval | 5s + 連續 3 fail | 改調後值 |
| SSL handshake latency | 15–20ms | TLS 1.2 + AES-128 |
| Connection rejection rate（優化前）| 2–3% | 預設 backlog |

---

## Anti-patterns

1. **Health check 過敏（2s + 1 fail 即移除）**
   - 問題：網路抖動時大量 server 上下線，玩家頻繁斷連
   - 解：5s interval + 連續 3 fail 判定；加 hysteresis

2. **Rate limiting 無差異對待**
   - 問題：全局 IP 限 5 conn/sec，proxy 後多用戶集體被擋
   - 解：白名單 + 動態閾值；用 User-Agent 或 session 區分

---

## Decision Tree

```
HAProxy pool backend 掉線？
├─ Health check fail → 檢查 check_path / TCP port
├─ 流量仍多 → 可能網路抖動，調寬連續 fail 閾值
└─ Rate limit 卡頻繁連線 → 檢查 stick table 誤報 / 加 IP 白名單

選 HAProxy vs Nginx vs cloud LB？
├─ 遊戲 TCP + 超高併發 → HAProxy（最專）
├─ HTTP 反向代理 + 靜態資源 → Nginx
└─ 純 cloud + 快速部署 → ALB / GCP LB（省運維）
```

---

## References

- 職涯段：`raw/career-summary.md#1-gamania-遊戲橘子--system-engineer`
- [HAProxy official docs](http://www.haproxy.org/#docs)
- [HAProxy stick-table](https://www.haproxy.com/blog/introduction-to-haproxy-stick-tables)
- 關聯：[[kernel-tuning-mmorpg]]、[[mysql-redis-cluster-ha]]、[[cdn-cache-tuning-97pct]]
