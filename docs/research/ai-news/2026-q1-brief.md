---
title: 2026 Q1 AI 月報 Executive Brief
source: 18 份 newsletter、155 篇文章
type: ai-news
---

# 2026 Q1 AI 月報 Executive Brief

> 個人快速回顧｜SRE / Cloud Architect 視角｜2026-01 ~ 2026-03  
> 來源：18 份 newsletter、155 篇文章

---

## 季度三大轉折

| # | 轉折 | 影響 |
|---|------|------|
| 1 | **「選模型」→「組系統」** | Harness 層成為工程護城河；代理自主性是一級設計考量 |
| 2 | **本地部署經濟反轉** | on-prem TCO 首次優於 API；企業本地部署破冰 |
| 3 | **推理效率成新競爭軸** | 速度/成本/易用/品質四維框架取代參數大小比較 |

---

## Top 10 事件

### 🔴 立即影響

**1. Claude Code 源碼洩露（3/18）+ OpenClaw RCE 漏洞**
- 500k+ 行原始碼洩露；DMCA 移除；三層記憶架構曝光
- OpenClaw：10,000+ 實例暴露（BitStrike）；100,000+ 存在 RCE（BitDefender）
- _SRE 行動_：自托管代理框架必須納入 0-trust 審查；deny-list 是底線

**2. Axios npm 汙染 + Mercor breach（3/31）**
- Axios：100M 週安裝量受威脅；代理工具鏈串聯風險
- Mercor：AI 承包商資料批量外洩
- _SRE 行動_：pin 所有 npm 依賴版本；啟用 SBOM 掃描；LiteLLM 版本審查

**3. Anthropic 被 Pentagon 移除（3/16，150 秒內）**
- 供應鏈風險標記導致存取撤銷；Anthropic 起訴 Trump 政府
- _SRE 關注_：雲端 AI API 的主權/合規風險已從理論變實務；多供應商備援規劃

**4. Opus 4.7 「變笨」事件（Wisely Chen 揭露）**
- Anthropic 承認 3 個 Harness Bug；context window 壓縮事件（15% ↓）
- _SRE 關注_：**訂閱 SLA ≠ 能力穩定**；關鍵工作流要建立模型品質監控

---

### 🟠 策略影響（1-3 個月）

**5. 本地部署 TCO 反轉（Wisely Chen 精算）**
- Qwen 3.6-27B on-prem 3 年 TCO：$4.7k vs API 方案 $22.5k（DGX Spark）
- _行動_：開始為企業 AI Coding 工作流評估本地/混合部署；計算完整 TCO

**6. GPT-5.4 定價與 Claude Opus 4.6 競爭格局**
- GPT-5.4：$2.50/$15 per 1M；GPT-5.4 Pro 輸出 $180/1M
- Claude Opus 4.6 快速版：$150/1M 輸出；1M context GA
- _行動_：重新評估 API 預算；快速版 vs 標準版成本差 6×

**7. OpenAI Codex vs Claude Code 市場份額**
- Claude Code VS Code 安裝：520 萬 vs Codex 490 萬
- Codex 週活 220 萬；日均 5T token；年化 $1B run-rate
- _關注_：代理編碼工具已是主流基礎設施，採用時機影響競爭力

**8. Harness Engineering 正式成工程學科（Q1 定義，Q2 爆發）**
- One Useful Thing「Model/App/Harness」三層架構：控制力集中於 Harness 層
- _行動_：評估團隊 Harness 能力缺口；投資 inference framework、路由、量化

---

### 🟡 觀望追蹤（3-6 個月）

**9. 物理 AI 大額融資（但商業化仍遠）**
- AMI Labs（LeCun）$1.03B @ $3.5B；World Labs（Fei-Fei Li）$1B
- OpenAI Sora 關閉（$1M/天燒費）→ 體現 AI 商業難度確認
- _關注_：NVIDIA NemoClaw / JEPA 開源突破作長期監控信號

**10. 開源模型三層分化**
- 邊緣層（7B）：Nemotron Nano、Kimi Linear → 本地推理
- 中層（70B+）：Qwen 3.5-122B、Mistral Small 4 → 追平專有模型特定任務
- _行動_：按場景分層選模型；停止一刀切使用雲端 API

---

## 本季定價參考

| 模型 | 輸入 / 輸出（per 1M token） | 備註 |
|------|--------------------------|------|
| GPT-5.4 | $2.50 / $15 | — |
| GPT-5.4 Pro | — / $180（輸出） | 極端推理模式 |
| Claude Opus 4.6 | $25 / $25 | 標準 |
| Claude Opus 4.6 快速 | — / $150 | 快速版 |
| Claude Code Max | $100/月 | — |
| Codex 入門 | $200 | OpenAI pricing |
| StrongDM AI token 支出 | $1,000/天/工程師 | 企業參考案例 |

---

## 本季安全行動清單

- [ ] 審查 OpenClaw / Claude Code 代理的 deny-list 與沙箱設定
- [ ] Axios 及 AI 相關 npm 套件：pin 版本 + 啟用 SBOM 掃描
- [ ] 建立模型品質監控（Opus 4.7 事件教訓：能力退化需可偵測）
- [ ] 雲端 AI API 多供應商備援規劃（Pentagon 事件：主權/合規風險實務化）
- [ ] 自托管代理框架 0-trust 審查（OpenClaw RCE 10 萬實例）

---

*詳細版：`research/ai-news/2026-q1-digest.md`（完整 7 大主題 + 時間線 + 各來源視角）*
