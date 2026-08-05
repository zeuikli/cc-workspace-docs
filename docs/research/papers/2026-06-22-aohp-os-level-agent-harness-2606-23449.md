---
url: "https://arxiv.org/abs/2606.23449"
title: "AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction"
archived_date: 2026-06-24
arxiv_id: 2606.23449
authors: ["Shanhui Zhao", "Jiacheng Liu", "Guohong Liu", "Jichao Yan", "Jialei Ye", "Yuhao Yang", "Hao Wen", "Shizuo Tian", "Yizhen Yuan", "Yuxuan Chen", "Yunxin Liu", "Ju Ren", "Ya-Qin Zhang", "Chao Huang", "Yao Guo", "Yuanchun Li"]
domains: [cs.AI, cs.OS]
html: "https://arxiv.org/html/2606.23449v1"
pdf_path: pdfs/2606.23449.pdf
published_date: 2026-06-22
---

# AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction

**Authors**: Shanhui Zhao, Jiacheng Liu, Guohong Liu, Jichao Yan, Jialei Ye, Yuhao Yang, Hao Wen, Shizuo Tian, Yizhen Yuan, Yuxuan Chen, Yunxin Liu, Ju Ren, Ya-Qin Zhang, Chao Huang, Yao Guo, Yuanchun Li
**Published**: June 22, 2026
**Source**: https://arxiv.org/abs/2606.23449 · [HTML](https://arxiv.org/html/2606.23449v1)
**arXiv ID**: 2606.23449
**Categories**: cs.AI, cs.OS
**PDF**: [research/papers/pdfs/2606.23449.pdf](https://arxiv.org/abs/2606.23449) (17 pp, full text archived)

---

## Abstract (quoted)

> AI agents are driving a new software paradigm, with the ability to autonomously call tools, extract information, manage memory, and complete tasks that span applications and data sources. Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. This mismatch limits the wider adoption of agents and leads to execution overhead and safety risks when running agents on conventional systems. While the concept of agent-native operating systems is emerging, the research community lacks an open testbed to explore the architectural primitives desired for agent-mediated interaction. We present AOHP (Android Open Harness Project), an OS-level agent harness built on the Android Open Source Project (AOSP). The core design principle of AOHP is to treat agents as first-class OS actors, enabling adaptive user interfaces and agent-friendly runtime environments. AOHP preserves the mature Android software and hardware ecosystem while introducing three agent-oriented system mechanisms: personalized service composition, efficient agent interfaces, and secure information flow. Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance.

---

## 結構化摘要

### 核心貢獻
AOHP（Android Open Harness Project）= 建在 AOSP 上的 **OS 層 agent harness**，核心原則「把 agent 當 first-class OS actor」（非 application-centric）。三大 agent-oriented 系統機制：

1. **Personalized service composition** — 依使用者組裝服務。
2. **Efficient agent interfaces** — agent 友善的執行介面，降低觀測/操作開銷。
3. **Secure information flow** — OS 層強制的安全資訊流，治理權限與洩漏風險。

定位為開源 testbed，供社群探索 agent-native OS 的架構 primitive，同時保留成熟 Android 軟硬體生態。

### 關鍵結果（preliminary）
- 任務完成率 **+21.12%**。
- token 成本 **-51.55%**。
- 安全策略合規性明顯優於常規系統執行。

### 限制
- 作者明示為 **preliminary experiments**；未列具體 limitation 章節，泛化性與長期穩定性待驗。

---

## Workspace 關聯（評估，非既成結論）

- **「agent-friendly 執行環境」對應 harness 觀測/動作層**：efficient agent interface 降 token 成本 -51.55%，與 NLAH / runtime-substrate 系列「介面適配優於模型調整」一脈；可作 best-practices/ 介面設計參考。
- **secure information flow = OS 層 enforcement**：與 Harness-MU（2606.21856）「治理交執行 hook 而非 LLM」同一思路的 OS 化版本，呼應 SafeHarness lifecycle security。
- ⚠️ 與本 workspace 場景錯位：AOHP 是 Android OS-level testbed，落地門檻高；列為域外參考而非可直接套用之 pattern（P2）。
