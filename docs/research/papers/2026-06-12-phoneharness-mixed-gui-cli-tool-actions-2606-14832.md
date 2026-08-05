---
url: "https://arxiv.org/abs/2606.14832"
title: "PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions"
archived_date: 2026-06-24
arxiv_id: 2606.14832
authors: ["Chenxin Li", "Zhengyao Fang", "Zhengyang Tang", "Pengyuan Lyu", "Xingran Zhou", "Xin Lai", "Fei Tang", "Liang Wu", "Yiduo Guo", "Weinong Wang", "Junyi Li", "Yi Zhang", "Yang Ding", "Huawen Shen", "Sunqi Fan", "Shangpin Peng", "Zheng Ruan", "Anran Zhang", "Benyou Wang", "Chengquan Zhang", "Han Hu"]
domains: [cs.CL]
html: "https://arxiv.org/html/2606.14832v1"
pdf_path: pdfs/2606.14832.pdf
published_date: 2026-06-12
---

# PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions

**Authors**: Chenxin Li, Zhengyao Fang, Zhengyang Tang, Pengyuan Lyu, Xingran Zhou, Xin Lai, Fei Tang, Liang Wu, Yiduo Guo, Weinong Wang, Junyi Li, Yi Zhang, Yang Ding, Huawen Shen, Sunqi Fan, Shangpin Peng, Zheng Ruan, Anran Zhang, Benyou Wang, Chengquan Zhang, Han Hu
**Published**: June 12, 2026
**Source**: https://arxiv.org/abs/2606.14832 · [HTML](https://arxiv.org/html/2606.14832v1)
**arXiv ID**: 2606.14832
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2606.14832.pdf](https://arxiv.org/abs/2606.14832) (16 pp, full text archived)

---

## Abstract (quoted)

> Phone agents are increasingly expected to complete real mobile workflows rather than merely predict the next screen action. However, much of the current mobile-agent literature still evaluates agents primarily as GUI controllers that observe a screen, emit taps and swipes, and are scored by target app state. Real phone-use tasks are broader: they require deciding when to use app GUIs, device-side commands, or structured tools, while leaving evidence that the intended side effect actually occurred. We introduce PhoneHarness, a mixed-action benchmark and execution harness for studying phone-use agents on verifiable mobile workflows [...].

---

## 結構化摘要

### 核心貢獻
**PhoneHarness** = 同時為 **mixed-action benchmark + execution harness**，研究 phone-use agent 在「可驗證 mobile workflow」上的表現。核心觀點：真實 phone 任務不只是 GUI 控制，而需在 **GUI / device-side CLI / structured tool** 間決策，並留下「side effect 確實發生」的證據。

1. **Mixed-action 空間** — 跨 GUI、CLI、host-side tool 的動作面。
2. **Deterministic routing** — 確定性路由決定動作面。
3. **Auditable execution traces / verifiable side effect** — 以可稽核 trace 驗證任務真有發生（非僅看 app 終態）。

### 關鍵結果
- 標註評估 split 上 **75.0% pass rate**，超可比系統 **+12.9 個百分點**。

### 限制
- 未列明確 limitation 章節；隱含主張「可靠 phone 自動化取決於 action-surface routing + 可驗證執行，而非純視覺 GUI 控制」。

### 命名注意
- 與既有 HarnessX（2606.14249）非同源；此為 phone-use agent 專用 harness/benchmark。

### 收錄注意
- 與 HarnessX 同日（2026-06-12）發布；屬上批 06-12 cutoff 邊界，本輪一併補收。

---

## Workspace 關聯（評估，非既成結論）

- **「action-surface routing 為確定性決定」呼應跨切紀律**：deterministic routing + verifiable side effect = 「路由交確定性代碼、驗證不可省」的 mobile 場景實例。
- **verifiable side effect = `unverified_success` 閘門**：不看終態看「真有發生」的稽核 trace，正是 core.md「靜態檢查 ≠ 端到端執行」的具體化。
- ⚠️ 域為 mobile/phone-use，與本 workspace 場景錯位；價值在 harness 設計理念（mixed-action + verifiable trace），非 benchmark 直接套用（P2 域外參考）。
