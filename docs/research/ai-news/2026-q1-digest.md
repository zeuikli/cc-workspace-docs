---
title: 2026 Q1 AI 新聞完整摘要
date: 2026-01-01
source: "18 份 newsletter（155 篇文章）— Interconnects、Ben's Bites、Import AI、Wisely Chen AI、Chain of Thought、Turing Post、AlphaSignal、Last Week in AI、Ahead of AI、One Useful Thing、Smol AI News、TheSequence、The Rundown AI、Latent Space、The Decoder、The Neuron、TLDR AI、Turing Post"
type: ai-news
---

# 2026 Q1 AI 新聞完整摘要

> 時間：2026-01-01 ~ 2026-03-31  
> 來源：18 份 newsletter（155 篇文章）— Interconnects、Ben's Bites、Import AI、Wisely Chen AI、Chain of Thought、Turing Post、AlphaSignal、Last Week in AI、Ahead of AI、One Useful Thing、Smol AI News、TheSequence、The Rundown AI、Latent Space、The Decoder、The Neuron、TLDR AI、Turing Post  
> 整理日期：2026-05-08

---

## 季度三大轉折

1. **「選模型」→「組系統」**：代理系統進入生產，Harness 層成為新護城河
2. **本地部署經濟反轉**：on-prem 3 年 TCO 首次優於 API（Qwen 3.6-27B $4.7k vs API $22.5k）
3. **推理效率成新競爭軸**：速度/成本/易用性/品質四維框架取代單一參數比較

---

## 一、模型發布與能力

### 主要模型一覽

| 模型 | 架構/參數 | Context | 核心 Benchmark | 定價 |
|------|----------|---------|---------------|------|
| GPT-5.4 | — | ~1.05M token | AA Index 57（並列第一）；GDPval 83% | $2.50/$15 per 1M |
| GPT-5.4 Pro | — | — | CritPt 物理推理 +10 vs 5.4 | 輸出 $180/1M |
| GPT-5.4 mini / nano | — | 400K | — | — |
| Gemini 3.1 Pro Preview | — | — | AA Index 57（並列第一） | — |
| Gemini 3.1 Flash Live | — | 128K | Audio MultiChallenge 36.1% | — |
| Claude Opus 4.6 | — | 1M GA | MRCR v2 78.3% | $25/$150 per 1M（快速） |
| Claude Sonnet 4.5 | — | 200K | — | — |
| Nemotron 3 Super | 120B / 12B active | 1M | AA Index 36；Hybrid Mamba-Transformer 2.2× vs gpt-oss-120b | — |
| Nemotron 3 Nano | 4B + 30B | — | — | — |
| MiniMax M2.7 | — | — | SWE-Pro 56.22%；Terminal Bench 2.0 57.0% | — |
| Qwen 3.5-122B | 122B-A10B | — | 超越 Nemotron 3 Super | — |
| Cursor Composer 2 | 基於 Kimi K2.5 | — | CursorBench 61.3%；SWE-bench 多語言 73.7% | — |
| Mistral Small 4 | 119B-A7B | — | — | — |
| Mistral Voxtral TTS | 4B | — | <5 秒語音克隆；開源 | — |
| Kimi Linear 48B | 48B / 3B active | — | — | — |
| Sarvam 105B / 30B | 105B-10A / 30B-A2B | — | — | — |
| Cohere Transcribe | — | — | English WER 5.42；14 語言 | — |

### 重要架構創新

| 技術 | 模型/論文 | 效能 |
|------|---------|------|
| Multi-head Latent Attention（MLA） | DeepSeek 帶動，45+ LLM 採用 | 新 KV cache 標準 |
| Hybrid Mamba-Transformer | Nemotron 3 Super | 2.2× 推理速度 |
| TurboQuant（PolarQuant + QJL） | NVIDIA | 3-bit KV cache，8× 記憶體節省 |
| FlashAttention-4 | — | 接近矩陣乘法速度（Blackwell GPU）|
| NVFP4（4-bit float） | Blackwell 原生 | 2× 速度 |
| Attention Residuals | Moonshot 論文 | 1.25× compute 優勢 |

### Benchmark 現況（Q1 末）

- **Google Proof Q&A**：最佳模型 94%（vs 人類 34–70%）
- **ARC-AGI-3**：人類 100%；目前最佳模型 <1%
- **Claude Code**：OSWorld-Verified 75.0%（超越人類基準）
- **Codex**：220 萬週活用戶；年增 4×；日均 5T token；年化 $1B run-rate

---

## 二、融資與商業

| 公司/專案 | 金額 | 估值 | 日期 | 備註 |
|----------|------|------|------|------|
| Yann LeCun AMI Labs | $1.03B | $3.5B | 3 月 | JEPA 世界模型；原 Meta FAIR 核心團隊 |
| World Labs（Fei-Fei Li） | $1B | — | — | 視覺世界模型 |
| SoftBank → OpenAI 橋接貸款 | $40B | — | 3/27 | — |
| Harvey AI | $200M | $11B | — | 法律 AI |
| Granola | $125M | $1.5B | — | — |
| Cerebras | $1B | $23B | — | — |
| Kleiner Perkins | $3.5B（新基金） | — | — | YoY +75% |
| Air Street Capital Fund III | $232M | — | — | — |
| Sanctuary（人形機器人） | — | $1.15B | 3/12 | — |
| Meta El Paso 資料中心 | $10B（追加） | — | 3 月 | — |
| Periodic Labs | — | ~$7B（洽談中） | 3/25 | — |
| Doss | $55M Series B | — | — | — |
| Deccan AI | $25M Series A | — | 3/25 | — |

---

## 三、產品與工具

### 代理平台

- **OpenClaw**：最快速成長開源代理框架；10,000+ 暴露實例（BitStrike）；100,000+ 存在 RCE 漏洞（BitDefender）
- **NemoClaw**：NVIDIA 安全沙箱包裝 OpenClaw（OpenShell）
- **Claude Code**：VS Code 市場 520 萬安裝（vs Codex 490 萬）；PR code review $15–$25
- **Claude Cowork**：知識工作者桌面代理；Claude Code Dispatch（手機遠端控制）
- **Cursor Composer 2**：Kimi K2.5 底層；CursorBench 61.3%
- **Hermes Agent**：開源代理 OS
- **WebArena-Infinity**：瀏覽器代理環境，大幅降低評估成本

### 協定與基礎設施

- **MCP（Model Context Protocol）**：代理編排協定快速普及
- **Chrome DevTools MCP**：Chrome 遠端除錯整合
- **LMArena**：獨立 LLM 評測基礎設施，估值 $1.7B
- **Artificial Analysis**：獨立評測平台（AA Intelligence Index）

---

## 四、安全事件

| 日期 | 事件 | 影響範圍 | 來源 |
|------|------|---------|------|
| 3/18 | **Claude Code 源碼洩露**（500k+ 行）| DMCA 移除；三層記憶架構曝光 | bens-bites, smol-ai-news |
| 3/31 | **Axios npm 套件汙染** | 100M 週安裝量受威脅 | bens-bites |
| 3/31 | **Mercor AI breach** | AI 承包商資料外洩 | bens-bites |
| 3/31 | **Railroad 未授權資料存取** | — | bens-bites |
| 2 月 | **Meta Supt. Labs OpenClaw 事件**（Summer Yue） | 代理刪除數百封 email | alphasignal |
| — | **OpenClaw RCE 漏洞** | 100,000+ 實例（BitDefender 確認） | alphasignal |
| 3/16 | **Anthropic 被 Pentagon 移除** | 150 秒內撤銷存取；供應鏈風險標記 | one-useful-thing, last-week-in-ai |
| 3 月 | **Anthropic 起訴 Trump 政府** | DoD 供應鏈風險指定爭議 | last-week-in-ai |

---

## 五、七大主題分析

### 5.1 代理系統成熟化（最高討論度）

**關鍵轉折**：代理從工具升為「能動體」——反向訪談使用者需求、自主決定工作流。  
代表案例：
- Chain of Thought "Compound Engineering"：單人維護 5 產品的工作新形態
- Import AI "Political Superintelligence"：三層代理協作驗證政治理性決策
- Ben's Bites 實測：代理 tool-use 處理 400 張照片批量工作流

**工程師啟示**：代理自主性是一級設計考量，不是功能。

---

### 5.2 開源模型三層分化

| 層級 | 規模 | 代表模型 | 適用場景 |
|------|------|---------|---------|
| 邊緣層 | 7B 級 | Nemotron Nano、Kimi Linear | 低耗能、本地推理 |
| 中層替代品 | 70B 級 | Qwen 3.5、Mistral Small 4 | 追平專有模型特定任務 |
| 頂層研究 | 500B+ 級 | — | 物理 AI、世界模型 |

---

### 5.3 推理效率革命

MHA → GQA → MLA → SWA 架構演進；MLA（DeepSeek V3 帶動）正成新默認標準。  
四維競爭框架（Interconnects 定義）：**速度 + 成本 + 易用性 + 品質**。

---

### 5.4 本地部署經濟反轉（最被低估的訊號）

Wisely Chen AI 精算：
- Qwen 3.6-27B on-prem（DGX Spark）3 年 TCO：$4.7k
- 等效 API 方案：$22.5k
- **企業 AI Coding 工作流本地部署破冰點已至**

---

### 5.5 多代理治理與安全缺口

Hyperagent / DGM-H（Meta + UBC Darwin-Gödel Machine）展示自我修正進化能力，但**無對應治理框架**。Claude Code 洩露、Pentagon 移除、axios 漏洞——暴露沙箱與驗證基礎缺陷。

---

### 5.6 物理 AI 與世界模型（長期佈局）

- AMI Labs（LeCun）$1.03B、World Labs（Fei-Fei Li）$1B
- Google Genie 3：實時 3D 互動環境生成
- Meta V-JEPA：機器人抓取/放置應用
- OpenAI Sora 關閉（$1M/天燒費）→ 資源移向代理編碼，暴露體現 AI 商業難度

---

### 5.7 訂閱制商業模式危機

核心矛盾：無限調用 vs 有限算力。  
- Anthropic Opus 4.7 三個 Harness Bug 事件（post-mortem 揭露）
- Claude Code context window 壓縮事件（15% ↓ compaction）
- OpenAI Sora 關閉；ChatGPT 訂閱戶算力被挪用實驗
- **控制力向 Harness 層集中**（One Useful Thing「Model/App/Harness」三層架構）

---

## 六、重大事件時間線

| 日期 | 事件 | 來源 |
|------|------|------|
| 1/26 | Yann LeCun 宣告「LLM 是 AI 進展死路」 | alphasignal |
| 2 月 | OpenAI 釋出 Codex；Claude 1M context 預覽 | one-useful-thing |
| 2/22 | Citrini Research AI 顛覆情境分析 | one-useful-thing |
| 2/26 | Block（Jack Dorsey）宣布 40% 裁員 | one-useful-thing |
| 2/27 | Pentagon vs Anthropic 衝突初起 | one-useful-thing |
| 3/5 | GPT-5.4 發布（$2.50/$15 per 1M） | smol-ai-news |
| 3/9 | Anthropic Claude PR code review 工具上線 | last-week-in-ai |
| 3/12 | Sanctuary 人形機器人估值 $1.15B | last-week-in-ai |
| 3/16 | **Claude 1M context GA 發布**；Anthropic 被 Pentagon 移除 | one-useful-thing |
| 3/18 | Claude Code 源碼洩露（500k+ 行） | bens-bites |
| 3/22 | Interconnects "Lossy self-improvement"：複雜度制約否定 RSI 幻想 | interconnects-ai |
| 3/25 | Deccan AI $25M、Periodic Labs $7B 洽談 | thesequence |
| 3/26 | NVIDIA "Quietly Building AI OS"；Qwen TCO 分析發布 | thesequence, wisely-chen-ai |
| 3/27 | SoftBank $40B 橋接貸款 → OpenAI | thesequence |
| 3/31 | **OpenAI Sora 關閉**；Axios npm 汙染；Mercor breach；Claude Code DMCA | 多源 |

---

## 七、各來源獨家視角

| 來源 | 代表角度 | 代表文章 |
|------|---------|---------|
| Interconnects AI | 複雜度制約優於奇點；四維競爭框架 | "What comes next with open models" |
| Ben's Bites | 代理 tool-use 工程化；沙箱必要性 | "One breach after another" |
| Import AI | 多代理治理缺口；政治理性驗證 | "Political Superintelligence" |
| Wisely Chen AI | Harness Bug 詳解；本地 TCO 精算 | "Opus 4.7 變笨一個月之謎" |
| Chain of Thought | Agent-native 組織工程 | "Compound Engineering" |
| Turing Post | 無法結構化工作流 = ROI 無邊界 | FOD#146 企業 AI 評估 |
| AlphaSignal | NVIDIA 軟體棧護城河；企業 0-trust | "Inside Yann LeCun's $1B Bet" |
| Last Week in AI | AI 政治化；地緣晶片戰 | Podcast #236 |
| Ahead of AI | MLA 成熟化；45+ LLM 架構對比 | "A Visual Guide to Attention Variants" |
| One Useful Thing | Harness 層控制點；個人代理崛起 | "A Guide to Which AI to Use" |
| Smol AI News | 社群第一手；邊界模型逃脫生態 | "Claude Code Source Leak" |
| TheSequence | 融資訊號；世界模型佈局 | "How to Build a World Model" |
| The Rundown AI | 資源稀缺揭示真實優先級 | "OpenAI's $1B Disney blindside" |

---

*詳細原始資料：`research/ai-news/q1-2026/`（已移除，備份於此摘要）*  
*下次更新：2026-07-01（Q2 總結）*
