# Zeuik Li — Career Raw Source

> **Status**: Immutable raw source (do NOT LLM-rewrite; only append new events)
> **Ingested from**: User-provided LinkedIn summary 2026-04-21; PDF resumes v2024.2 verified + corrected 2026-05-08
> **Role layers**: 3 axes — Technical (Infra / Cloud / DB / Security) · Leadership (Lead / Consultant / CTO) · Domain (MMORPG / Enterprise / Streaming / Media / Fintech / Financial Services)

---

## Timeline (most recent first)

### 8. CathaySec 國泰證券 — SRE Lead & Manager (current)

**Role**: Cloud Native transformation + infrastructure modernization for Taiwan securities firm.

**Key achievements**:
- 🚀 **Hybrid Cloud**: GCP Landing Zone + on-prem integration → secure hybrid cloud env；主要服務：**Cloud SQL/AlloyDB、Cloud Run/Functions、BigQuery/Looker Studio、Cloud CDN**（user confirmed）
- 🏗️ **應用系統上雲**：7R 評估 + 上雲路徑圖、系統雲化原生改造（microservice/container）、新建 Cloud Native 平台
- 🤖 **AI 應用導入**：Vertex AI Search / RAG 應用 + Gemini API / LLM 整合至現有系統
- 🛡️ **CNAPP 評估**（已完成，有明確結論）：SCC Premium（GCP 原生）vs 第三方工具 vs Microsoft Defender for Cloud 三方對比；分階導入策略：CSPM 先、CWPP 後
- 🔧 **Terraform Enterprise**：全新安裝 TFE（From scratch）於金融合規環境
- 💰 **FinOps 工具導入**：Apptio（第三方 SaaS）+ GCP 原生 Billing + Looker Studio 帳單視覺化 + 內部 FinOps Culture 建置；NT$400k+ saved（GCP VM/GKE idle 清除）
- 🛡️ **ISO 27017**：Cloud security mechanisms + org chart revision；**冷備份系統上雲**（Dell PowerProtect Data Domain VE 整合 GCP）作為主要取證項目；passed internal + external audits → ISO 27017 cert（認證機構：BSI）
- ⚙️ **DevOps**: Standardized CI/CD + Terraform IaC → reduced deployment friction, eliminated manual errors during migration

**Core skills**: GCP · Hybrid Cloud · Terraform Enterprise · CI/CD · Cloud Security (CNAPP/CSPM/CWPP) · FinOps (Apptio) · Vertex AI · RAG · Tech Leadership（SRE/DevOps 團隊 1-3 人，user confirmed）

---

### 7. Resolve Technology — Senior DevOps + Consultant (dual role)

**Role**: Lead DevOps Engineer + Technical Consultant. 主要客戶產業：**金融 / 銀行 / 證券**（user confirmed）。Multi-cloud architecture + strategic guidance.

**DevOps achievements**:
- ☁️ Managed AWS + GCP ecosystems. Migrated Terraform infra from Replicated → Docker-compose (flexibility ↑)
- ⚙️ GitHub Actions + Ansible playbook automation for complex configs
- 🚀 GitLab CI + Kafka + Confluent for real-time data streaming
- 🛡️ Huawei Cloud Stack API for image hardening + VM provisioning（**客戶在中國或中東，AWS/GCP 無法服務**，user confirmed）

**Consulting achievements**:
- 🤝 IaC design bridging public ↔ private cloud
- 📚 Client enablement: technical docs + training on cutting-edge cloud tech
- 🗓️ Strategic project coordination, stakeholder management, delivery timelines

**Core skills**: AWS · GCP · Huawei Cloud · Terraform · Docker · Kubernetes · Ansible · Kafka · GitHub Actions · GitLab CI · Technical Consulting

---

### 6. 壹蘋新聞網 NextApple — Cloud Architect（concurrent sub-project during Role #5 SoundOn, PDF-confirmed）

**Role**: Cloud infrastructure strategy for Taiwan leading news media platform.

**Key achievements**:
- 🚀 **CDN Architecture**: **97% cache hit rate**
- ⚡ High-availability infra handling massive traffic surges with minimal origin load, microsec latency
- 📉 24/7 service reliability for millions of users during peak traffic

**Core skills**: Cloud Architecture · CDN · High Concurrency · Performance Tuning · Media Streaming Infra

---

### 5. Goodnight / SoundOn — SRE + Architect

**Role**: High-performance service infra + deployment workflow revolution. DB expertise + SRE best practices.

**Key achievements**:
- 💰 **FinOps**: CDN migration Cloudfront → Cloudflare → **$60,000 USD saved in 1 year**（PDF v2024.2）；Beanstalk multi-type + Spot instance right-sizing；RDS 降規（query 優化後 over-provisioned）
- 🚀 **Performance**: Beanstalk + CI/CD revamp → **API 4x**；DB query optimization + index cleanup → **query 10x faster**（microsecond latency）、**DB size ↓3x**
- 🔄 CI/CD pipeline revamped（10-20 deploys/day capable）
- 🛡️ **Zero-downtime upgrade**: PostgreSQL **9→14**（AWS RDS 跍長備機 + DNS cutover）、Redis **2.8→5.0.6**；100% availability
- 🚨 **Alarm reduction**: Code optimization with backend team → **80% fewer incidents**（EN PDF v2024.2）
- 🏗️ 協助壹蘋新聞網：**全程參與**（AWS 環境建置 + Terraform 模組化 + CI/CD pipeline）（user confirmed）

**Core skills**: PostgreSQL · Redis · Database Tuning · CI/CD Pipelines · FinOps · High Availability · Microsecond Latency Optimization · CDN Migration

---

### 4. KKStream / KKCompany — SRE + DevOps + DBA + Architect

**Role**: AWS infrastructure for streaming services.

**Key achievements**:
- 🚀 **AWS infra redesign + API/CI/CD refactor → 400% performance ↑**
- 💰 **Savings Plans + RI → $150,000 USD/yr saved**
- ⚙️ AWS Step Functions + ECS for streaming event automation
- 📊 SQL tuning（Saku/TFC：**客戶端最終使用者對向的直播平台**）→ latency -200%（user confirmed）
- 🛡️ AWS Lambda-based intelligent alarm system + R&D collaboration → **alarm volumes -50%**
- 🎬 Streaming encoding module OS upgrade → **+20% performance**（PDF v2024.2）
- 🐳 Managed Core-Tech K8s + Project-base K8s clusters
- 🤝 AWS Solution Architects partnership → scalability framework
- 📚 SRE on-call docs + training programs

**Core skills**: AWS (Lambda, Step Functions, ECS) · Infrastructure Optimization · FinOps · SQL Tuning · CI/CD · Incident Management · Streaming Infrastructure

---

### 3. SPQ — Co-founder / CTO (startup)

**Role**: Co-founder + CTO（title confirmed by user；PDF 寫 Software Engineer 為對外簡化寫法）。AWS cloud env design + implementation for new digital product. Technical architecture ↔ business strategy.

**Key achievements**:
- 🏗️ AWS: VPC, Route 53, security groups, EC2, S3, RDS, ElastiCache
- ☁️ **Serverless**: API Gateway + Lambda + CloudWatch monitoring
- 💳 **Stripe payment gateway on AWS Lambda**: secure transaction + status tracking
- 🤝 Product strategy + mobile app dev + UI/UX collaboration + security assessments

**Core skills**: AWS Architecture (VPC, EC2, RDS) · Serverless (Lambda, API Gateway) · Stripe API · Network Security · Product Strategy · UI/UX Collaboration

---

### 2. HTC — Infra + Storage Engineer

**Role**: Enterprise infra security + virtualization（合約性質，Security Zone 專案結束後轉至 SPQ，user confirmed）。R&D + Security team collaboration. Supported VR + mobile tech dev.

**Key achievements**:
- 🛡️ **Security Zone project**: network isolation, Squid proxy, MS security services (MFA, RDGW, NPS)
- ☁️ **VMware ESXi 6.0 + NSX** network virtualization
- 💾 **Backup migration TSM → Commvault** → operational cost ↓, data resilience ↑
- ⚙️ Windows services (SCCM, WSUS) rebuild + Docker PoC for R&D containerization evaluation + cost assessment
- 🐧 Set up Linux mirror sites + proxy server for VR team
- 🤝 Mobile phone RD access testing + reporting

**Core skills**: VMware (ESXi, NSX) · Network Security · Windows Server (MFA, SCCM) · Commvault · Infrastructure Hardening · Docker · SAN

---

### 0. 寶盈 Prowin Net Technology — Field Application Engineer

**Role**: 台灣大專院校系務平台與線上考試系統維運支援（2014-07 – 2015-07）

**Key achievements**:
- 🏫 維護 **15+ 所**台灣大專院校系所系務平台與相關硬體（user confirmed）
- 🛠️ 客戶操作問題排除 + 功能建議回報給開發團隊
- 💻 線上考試中心伺服器與網路設備維護與故障排除

**Core skills**: Server Maintenance · Network Troubleshooting · University Systems · Customer Support

---

### 1. Gamania 遊戲橘子 — System Engineer

**Role**: Mission-critical infra for Lineage M (天堂M), a top-traffic MMORPG.

**Key achievements**:
- 🚀 **Server architecture**: **~150 server racks，含近 500 VMs**（HP/DELL），兩者皆正確（user confirmed）
- ⚙️ **Linux kernel tuning + HAProxy**：TCP level（遊戲客戶端→game server 分流）+ Layer 7 HTTP（管理工具）兩種用途（user confirmed）；software LB → hardware cost ↓
- 💾 **VMware ESXi 5.0→6.0 upgrade** across cluster. FreeNAS + iSCSI integration. MySQL + Redis Cluster replication for HA
- ☁️ **Gamania AWS PoC**: migrated compute to EC2, CloudFront + HiNet CDN for content delivery
- 📊 **Monitoring**: Cacti + Grafana, daily gaming data insights, advanced alerting
- 📲 Telegram alert implementation + daily gaming data reports（PDF v2024.2）

**Core skills**: VMware vSphere · Linux Kernel Tuning · HA · Redis/MySQL Clustering · HAProxy · AWS (EC2, CloudFront) · CDN · Kafka · Hadoop（遊戲數據分析，user confirmed）

---

## Cross-cutting Patterns (observations)

1. **FinOps track record**: CathaySec NT$400k, SoundOn $60k/yr（CDN migration，PDF-confirmed）, KKStream $150k/yr — consistent cost reduction delivery
2. **Zero-downtime / HA focus**: appears across Gamania (game cluster), SoundOn (DB upgrades), 壹蘋 (news surges)
3. **Multi-cloud breadth**: AWS (KKStream, SPQ, Resolve), GCP (CathaySec, Resolve), Huawei (Resolve), hybrid (CathaySec)
4. **Database depth**: PG (SoundOn), MySQL/Redis Cluster (Gamania), RDS/ElastiCache (SPQ)
5. **Leadership progression**: System Engineer (Gamania) → Infra Eng (HTC) → CTO (SPQ) → SRE/Architect (KKStream, SoundOn, 壹蘋) → Lead + Consultant (Resolve) → Lead + Manager (CathaySec)
6. **Security & Compliance**: HTC Security Zone → CathaySec ISO 27017 → maturing defensive posture
7. **Automation evolution**: Cacti/Grafana (Gamania) → Step Functions (KKStream) → Terraform IaC (Resolve/CathaySec) → AI agents (cc-workspace 2026)

---

## Career Reference

- LinkedIn: https://www.linkedin.com/in/zeuik-li
- cc-workspace: https://github.com/zeuikli/cc-workspace
