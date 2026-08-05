---
url: "https://arxiv.org/abs/2605.30613"
title: "CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs"
archived_date: 2026-06-24
arxiv_id: 2605.30613
authors: ["Ryan Fahey"]
domains: [cs.CR]
html: "https://arxiv.org/html/2605.30613v1"
pdf_path: pdfs/2605.30613.pdf
published_date: 2026-05-28
---

# CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs

**Authors**: Ryan Fahey
**Published**: May 28, 2026
**Source**: https://arxiv.org/abs/2605.30613 · [HTML](https://arxiv.org/html/2605.30613v1)
**arXiv ID**: 2605.30613
**Categories**: cs.CR
**PDF**: [research/papers/pdfs/2605.30613.pdf](https://arxiv.org/abs/2605.30613) (11 pp, full text archived)

---

## Abstract (quoted)

> Over the past year, prompt caching in Large Language Models (LLMs) has become increasingly more popular across inference APIs. Prompt caching helps save precious compute resources and speeds up response times by reusing parts of the KV cache of a specific prompt for another request. However, many implementations of prompt caching are not secure against timing attacks or even basic metadata disclosure. Gu et al. (ICML 2025) develop a method to audit prompt caching in LLMs. This paper investigates whether OpenRouter's API gateway architecture introduces prompt caching vulnerabilities that bypass provider-level prompt cache isolation guarantees. Most LLM inference providers implement per-account or per-organization prompt caching to prevent data leaks, but does routing through OpenRouter with shared organizational credentials inadvertently create global cache sharing across all OpenRouter users?

---

## 結構化摘要

### 核心貢獻

- 提出 **CacheProbe** 方法：透過 timing attack 稽核 API gateway（OpenRouter）層級的 prompt cache isolation 是否存在漏洞
- 驗證 LLM inference provider 的 per-account/per-organization prompt caching 隔離保證，是否在經由 gateway routing 後被繞過
- 延伸 Gu et al.（ICML 2025）的 prompt cache auditing 方法，將攻擊面從單一 provider 擴展至 multi-tenant gateway 架構
- 調查 shared organizational credentials 透過 OpenRouter 是否會導致全域 cache sharing 跨越所有使用者

### 關鍵結果

- 論文核心問題：OpenRouter 作為 gateway 代理層時，是否因 shared credentials 或 routing 設計而讓不同使用者的 KV cache 互相可見
- 具體攻擊向量：timing side-channel（回應時間差異）與 metadata disclosure
- 文件未提供最終量化數字（如洩漏率、timing delta 閾值）；結果細節在正文中

### 限制

- 研究對象限縮至 OpenRouter 一家 gateway，結論外推至其他 gateway（如 AWS Bedrock、Azure AI）需另行驗證
- Timing attack 受網路抖動影響，偵測精度與環境雜訊相關
- 文件未列明確 limitation 章節；推斷弱點：LLM provider 可隨時更新 caching 策略使結果失效，重現性依賴 API 當前行為

---

## Workspace 關聯（評估，非既成結論）

- **Prompt caching 安全性直接對應 `context-management.md`**：本庫使用 prompt caching 加速（CLAUDE.md 靜態前綴策略），CacheProbe 揭示 KV cache 在 multi-tenant gateway 下可能跨帳號共享，意味著若透過第三方 gateway 使用 Claude API，CLAUDE.md 內容的 cache 隔離需額外確認——屬於真實風險，⚠️ 但 Anthropic 直接 API 通常有 per-account 隔離保證，gateway 層須自行稽核
- **生產安全紅線（`core.md` P0 規則）**：論文的 timing side-channel 屬於資訊洩漏類攻擊，符合 core.md 所定義的 P0 安全發現等級（Auth Bypass 變體）；若在 workspace 的 LLM 呼叫路徑中引入 OpenRouter 類 gateway，應套用 P0 流程審查 cache isolation 設定
- **`unverified_success` 閘門類比**：CacheProbe 的核心論點是「provider 宣稱的隔離保證 ≠ 實際隔離行為」，與 core.md 中「subagent/workflow 自報成功 = 中間態，需主對話親跑確定性檢查才升 verified」完全同構——兩者都在警告不要把聲明當事實
- **`core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的 Agent Input Security**：論文顯示 prompt cache 洩漏可讓攻擊者透過 timing 推斷他人 prompt 內容；這強化了 workspace 規則中「外部輸入包裹 `<untrusted_objective>` + 當 data 不當 instruction」的必要性，⚠️ 但 workspace 目前的 gateway 架構不明，需實際確認才能評估暴露面
