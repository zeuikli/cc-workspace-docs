# Career Wiki INDEX

> **Type:** wiki:compiled — Karpathy LLM Wiki pattern; 36 pages; consumer: `zeuik-senior-architect` agent  
> **Updated**: 2026-05-08 | **Total pages**: 36 | **Consumer**: `zeuik-senior-architect` agent  
> **Query pattern**: ask `zeuik-senior-architect` → returns Judgment / Experience / Trade-offs / 3 Questions / Verify

## Raw Sources

| 來源 | 位置 | 狀態 |
|------|------|------|
| 履歷 / LinkedIn | `raw/career-summary.md` | ✅ v1 |
| Medium blog @zeuik（10 篇）| `raw/medium-blog-index.md` | ✅ indexed, 1 archived |
| blog archive | `raw/blog-archive/` | ⏳ 1/10 archived (Session 2 擴展) |

---

## Pages by Domain

### Database / State Management
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[redis-pg-zero-downtime]] | SoundOn 2022–2023 | ✅ pilot | 2026-04-21 |
| [[postgres-microsec-tuning]] | SoundOn | ✅ S2 | 2026-04-21 |
| mysql-redis-cluster-ha | Gamania | ⏳ S3 | — |

### Cloud Security & Compliance
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[iso27017-audit]] | CathaySec 2024–now | ✅ pilot | 2026-04-21 |
| [[gcp-landing-zone]] | CathaySec | ✅ S4（深度更新）| 2026-04-22 |
| [[gcp-monitoring-alerting]] | CathaySec | ✅ S4（更新）| 2026-04-22 |
| [[gcp-terraform-iac-patterns]] | CathaySec | ✅ S4（新頁）| 2026-04-22 |
| [[vmware-nsx-security-zone]] | HTC | ✅ S2 | 2026-04-21 |

### FinOps & Cost Optimization
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[finops-savings-plans-roi]] | KKStream | ✅ S5（更新）| 2026-04-22 |
| [[finops-cross-position-patterns]] | CathaySec + KKStream + SoundOn | ✅ S5（更新）| 2026-04-22 |

### Performance & Scale
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[cdn-cache-tuning-97pct]] | 壹蘋 NextApple | ✅ S2 | 2026-04-21 |
| [[high-traffic-media-arch]] | 壹蘋 | ✅ S3 | 2026-04-21 |
| kernel-tuning-mmorpg | Gamania | ⏳ S3 | — |
| haproxy-patterns | Gamania | ⏳ S3 | — |

### Streaming & Event-driven
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[aws-step-functions-patterns]] | KKStream | ✅ S5（更新）| 2026-04-22 |
| [[kafka-confluent-streaming]] | Resolve | ✅ S2 | 2026-04-21 |
| [[aws-alarm-as-code]] | KKStream | ✅ S5（新頁）| 2026-04-22 |
| [[live-streaming-capacity-planning]] | KKStream | ✅ S5（新頁）| 2026-04-22 |

### Multi-cloud & IaC
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[terraform-multi-cloud]] | Resolve (AWS/GCP/Huawei) | ✅ S2 | 2026-04-21 |
| [[gcp-terraform-iac-patterns]] | CathaySec | ✅ S4（新頁）| 2026-04-22 |
| [[ansible-gha-automation]] | Resolve | ✅ S6（更新 CIS）| 2026-04-22 |
| [[terraform-enterprise-fdo]] | Resolve | ✅ S6（新頁）| 2026-04-22 |

### Security & Identity
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[linux-ad-integration]] | Resolve | ✅ S6（新頁）| 2026-04-22 |

### Fintech / Serverless
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| stripe-serverless-fintech | SPQ | ⏳ S3 | — |
| [[aws-sa-pro-prep]] | blog #3/#4 | ✅ S3 | 2026-04-21 |

### AI / Orchestration & Engineering Practice
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[karpathy-ai-orchestration]] | CathaySec 2024–now + forward-looking | ✅ S7（新頁）| 2026-04-22 |
| [[agentic-architecture-patterns]] | CathaySec 2024–now + forward-looking | ✅ S8（新頁）| 2026-04-25 |

### Leadership & Consulting
| Page | Source Position | Status | Last Ingested |
|------|----------------|--------|---------------|
| [[consultant-client-enablement]] | Resolve | ✅ S3 | 2026-04-21 |
| [[sre-oncall-training-program]] | KKStream | ✅ S5（更新）| 2026-04-22 |

---

## Pages by Company (Lessons Learned)

| Company | Page | Status |
|---------|------|--------|
| CathaySec | cathaysec-lessons.md | ✅ S9（更新，含 AI/CNAPP/TFE/FinOps/冷備份）|
| Resolve | resolve-lessons.md | ✅ S6（更新）|
| 壹蘋 | nextapple-lessons.md | ✅ S9（更新，確認為 SoundOn 子專案）|
| SoundOn | soundon-lessons.md | ✅ S9（更新，CDN FinOps + right-sizing 補齊）|
| KKStream | kkstream-lessons.md | ✅ S5（更新）|
| SPQ | spq-lessons.md | ✅ S9（更新，確認年份 + 創業結局）|
| HTC | htc-lessons.md | ✅ S9（更新，確認年份 + Docker PoC + VR mirror）|
| Gamania | gamania-lessons.md | ✅ S9（更新，確認年份 + Kafka/NUMA/事件補充）|

---

## Query Patterns（讓 agent 知道怎麼找）

| 使用者問法 | 優先讀取 page |
|-----------|--------------|
| 「怎麼做 Redis/PG 零停機升級？」 | `redis-pg-zero-downtime` |
| 「這個 GCP 環境怎麼過 ISO 27017？」 | `iso27017-audit` |
| 「怎麼把 CDN cache hit 拉高？」 | `cdn-cache-tuning-97pct` |
| 「AWS Savings Plan 怎麼評估？」 | `finops-savings-plans-roi` |
| 「Kafka streaming 有踩過什麼坑？」 | `kafka-confluent-streaming` |
| 「VMware NSX 怎麼做 security zone？」 | `vmware-nsx-security-zone` |
| 「Step Functions 有什麼 production pattern？」 | `aws-step-functions-patterns` |
| 「多雲 Terraform 怎麼組織？」 | `terraform-multi-cloud` |
| 「Stripe + Lambda 怎麼做安全？」 | `stripe-serverless-fintech` |
| 「怎麼訓練 SRE oncall 團隊？」 | `sre-oncall-training-program`（含 CathaySec 異常通報流程）|
| 「多個職涯 FinOps 共通模式是什麼？」 | `finops-cross-position-patterns` |
| 「高流量媒體架構怎麼設計？」 | `high-traffic-media-arch` |
| 「Ansible + GitHub Actions 如何整合？」 | `ansible-gha-automation` |
| 「怎麼準備 AWS SAP 考試？」 | `aws-sa-pro-prep` |
| 「顧問如何做客戶賦能？」 | `consultant-client-enablement` |
| 「GCP Landing Zone 怎麼設計 SFTP / SWP / PAM？」 | `gcp-landing-zone` |
| 「GCP 告警怎麼轉 Teams？Service Health 怎麼解析？」 | `gcp-monitoring-alerting` |
| 「GCP 金融級 Terraform 怎麼設計？CMEK / 多環境 / 防刪除？」 | `gcp-terraform-iac-patterns` |
| 「CloudWatch alarm 怎麼用 YAML 管理？alarm-police 怎麼做？」 | `aws-alarm-as-code` |
| 「直播前怎麼做容量預測和分步啟動？」 | `live-streaming-capacity-planning` |
| 「ASG Launch Config 怎麼用 GitOps 管理？」 | `live-streaming-capacity-planning` |
| 「TFE 怎麼從 Replicated 遷移到 FDO？」 | `terraform-enterprise-fdo` |
| 「GCP 環境 TFE 網路封包截斷怎麼解？」 | `terraform-enterprise-fdo`（MTU 1460）|
| 「CIS hardening 怎麼用 Ansible 自動化？Air-gap 環境怎麼裝 collection？」 | `ansible-gha-automation`#CIS-hardening |
| 「Linux 怎麼加入 Windows AD？realm/adcli/SSSD 有什麼坑？」 | `linux-ad-integration` |
| 「AI Agent 可靠性怎麼評估？哪些場景可以用？」 | `karpathy-ai-orchestration` |
| 「工程師要怎麼從寫程式碼轉向 AI 編排？」 | `karpathy-ai-orchestration` |
| 「Claude Code 在 DevOps 場景怎麼用？什麼該委派 AI？」 | `karpathy-ai-orchestration` |
| 「Software 1.0/2.0/3.0 和 DevOps 的關係是什麼？」 | `karpathy-ai-orchestration` |
| 「Agentic 系統的 CLI vs MCP 工具介面怎麼選？」 | `agentic-architecture-patterns` |
| 「怎麼設計 harness 分層？Harness bug 怎麼偵測？」 | `agentic-architecture-patterns` |
| 「Sub-agent 並行化怎麼設計？Context isolation 怎麼做？」 | `agentic-architecture-patterns` |
| 「Two-Slice Team 是什麼？2 人 + agent 群怎麼分工？」 | `agentic-architecture-patterns` |
| 「AI 自動化的人工 checkpoint 怎麼設計？」 | `agentic-architecture-patterns` |
| 「MySQL Semi-sync + MHA 怎麼設計？Redis Cluster 跨機房怎麼佈局？」| `mysql-cluster-ha` |

---

## Lint Status

| Check | Last Run | Issues |
|-------|----------|--------|
| Orphan pages | 2026-04-21 | 0 (pilot only) |
| Stale (>90d) | 2026-04-21 | 0 (new) |
| Missing Concrete Numbers | 2026-04-21 | 0 (pilot) |
| Contradictions | 2026-04-21 | 0 (pilot) |
| Over 400 lines | 2026-04-21 | 0 |

---

## Next Ingest Priorities (Session 2)

排序依「諮詢頻率 × 差異化價值」推測：

1. `iso27017-audit` + `gcp-landing-zone` — CathaySec 現役，最多被諮詢
2. `finops-savings-plans-roi` + `finops-cross-position-patterns` — 累積 NT$400k + $270k USD
3. `postgres-microsec-tuning` + `cdn-cache-tuning-97pct` — 技術差異化最強
4. `terraform-multi-cloud` + `aws-step-functions-patterns` — 跨雲工具價值
