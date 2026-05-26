# AI 產品經濟學 + 物理 AI — 分析 Prompt
> 資料來源：research/ai-news/ Q1-2026 ~ 2026-05-16 | 涵蓋 17 個 newsletter | 主題 4 + 主題 6

---

## 使用方式

**適用場景：**
- AI 投資決策與供應商選型成本分析
- Token 成本優化（FinOps for AI）
- 機器人 / 具身 AI 技術路線評估
- AI 公司估值與商業模式分析

---

## 核心洞察（Q1 2026 ~ 2026-05-16）

### AI 產品經濟學：融資戰與成本危機

**鉅額融資一覽（2026 Q1-Q2）：**

| 公司/交易 | 金額 | 日期 |
|----------|------|------|
| Anthropic（Google 投資）| $40B | 2026-04-27 |
| Anthropic（Amazon 累計）| $25B | 持續 |
| Anthropic 估值 | ~$900B | 2026-05-15 |
| OpenAI 融資輪 | $122B（估值 $852B）| 2026-04-01 |
| CoreWeave × Meta | $35B 長期合約 | 2026-04-16 |
| Jane Street × CoreWeave | $6B | 2026-04-16 |
| Cerebras IPO | $5.5B 市值 $40B；2000× 超額認購 | 2026-05-15 |
| Cursor 估值 | $50-60B（被 xAI 收購）| 2026-05 |
| Moonshot Kimi | 估值 $20B | 2026-05 |

**Anthropic 財務軌跡**（CFO Krishna Rao，TLDR AI 2026-05-15）：
- 2 年內：$250M run-rate → $30B run-rate（120× 增長）
- ARR 目標：$40B（年化 80× 增長）

### Token 成本分析（關鍵數據）

**多語言 Token 稅**（Wisely Chen AI 2026-05-04）：

| 模型 | 中文 token 乘數 | 說明 |
|------|--------------|------|
| Claude 系列 | 1.71× | 中文場景顯著劣勢 |
| DeepSeek V4 | 0.95× | 接近中性 |
| GPT-4o | 約 1.2× | 中間水準 |

**台灣金融客服成本案例**（日均 10,000 通話）：
- Claude：$2,310/月
- GPT-4o：$1,121/月
- DeepSeek：$102/月
- **結論**：中文高頻場景建議評估 DeepSeek 或本地部署

**Reasoning Token 成本陷阱**（Turing Post 2026-04-25）：
- Reasoning token 可達基準成本 15× 
- 不加限制的 o3/Opus 4.7 任務可能超預算 10-50 倍
- 對策：設置 thinking budget 上限；非推理任務禁用 extended thinking

**Perceptron Mk1 視頻分析成本**：便宜 80-90%（TLDR AI 2026-05-13）

### OpenAI × Microsoft 合約重寫（2026-04-28）

- OpenAI 授權從專屬改為非專屬（多雲解鎖）
- AGI 定義從合約中移除（商業自主權擴大）
- AWS $38B 協議同步解鎖
- **影響**：企業採購可議 multi-cloud AI 合約，Lock-in 風險降低

### 訂閱制商業模式危機

- GitHub Copilot 月費制 → token 計費（2026-04-28，The Neuron）
- ChatGPT $20/月上限 vs 實際算力無限需求的矛盾暴露
- Cloudflare 裁員 20% 同時宣稱 AI 100× 生產力，股價跌 23%（Wisely Chen AI 2026-05-11）
  - 市場首次 punish「AI 取代人」的故事
- Q1 基線：訂閱制無限調用幻想瓦解（Opus 4.7 Harness 三個 Bug 導致能力退化 15%）

---

## 物理 AI 與機器人：世界模型走向實用

### 融資與估值

| 公司 | 金額 | 創辦人/重點 |
|------|------|-----------|
| AMI Labs | $1.03B | Yann LeCun；JEPA 架構 |
| World Labs | $1B | Fei-Fei Li；世界模型 |
| Ineffable Intelligence | $1.1B @ $5.1B 估值 | RL superlearners |
| Eclipse Ventures | $1.3B 基金 | 實體 AI / 機器人 / 製造 |

### 技術里程碑（2026 Q1-Q2）

| 項目 | 成就 | 來源 |
|------|------|------|
| Sony Ace | 9 個 200Hz 攝影機，10.2ms 延遲，純 sim RL | The Neuron 2026-04-25 |
| Google AlphaEvolve | Gemini 驅動演算法設計，發現跨數學/CS/物理新知識 | TLDR AI 2026-05-08 |
| Vibe Physics | GPT-5 生成 110 頁新物理論文 | Latent Space 2026-05-05 |
| Meta Muse Spark | 眼鏡端實時視覺辨識 | TLDR AI 2026-05-13 |
| Google Genie 3 | 生成互動環境（從模型轉向模擬）| TheSequence 2026-04-07 |

### 與量產的距離

- Sony Ace 純 sim RL → 現實部署仍有「sim-to-real gap」
- OpenAI Sora 關閉（$1M/天燒費）：體現 AI 商業難度
- 世界模型預期 2026 Q3 後才見產品化成果
- AI 開始進行 frontier 科學（非只輔助），商業化路徑仍不明朗

---

## 分析 Prompt 範本

```
你是 AI FinOps 與投資決策顧問。基於以下 2026 Q1-Q2 市場背景：

【成本現實】
- Reasoning token 最高 15× 基準成本；Claude 中文 1.71× token 稅
- 台灣金融客服 10K calls/天：Claude $2,310 vs DeepSeek $102/月
- 本地部署 TCO：DGX Spark 3 年 $4,729 vs API $22,500

【商業模式轉變】
- GitHub Copilot 月費 → token 計費；OpenAI × Microsoft 授權多元化
- Cloudflare 裁員 20% + AI 100× 宣稱 → 股價跌 23%（市場懲罰 AI 取代人故事）
- Anthropic：$250M → $30B run-rate（2 年 120× 增長）

【物理 AI 現況】
- AMI Labs（LeCun）$1.03B JEPA；Sony Ace 純 sim RL
- AI 已進行 frontier 科學（GPT-5 生成 110 頁物理論文）
- 量產距離：世界模型 Q3 後見產品化

請分析以下 AI 投資/成本決策問題：[插入具體場景]

評估維度：
1. Token 成本試算（含多語言乘數、reasoning token 乘數）
2. 3 年 TCO 比較（API vs 本地部署 vs 混合）
3. 供應商風險（合約形式、Lock-in、地緣政治）
4. 商業模式可持續性（訂閱制 vs token 計費 vs 企業協議）
5. 物理 AI 投資時機評估（若相關）

輸出格式：
- 成本試算表（月費 / 年費 / 3 年 TCO）
- 供應商對比矩陣（3-5 個維度）
- 風險評估（財務 / 技術 / 地緣政治）
- 建議決策時間線
```

---

## 追蹤指標（持續監測）

| 指標 | 當前基線 | 更新頻率 |
|------|---------|---------|
| Anthropic/OpenAI ARR | Anthropic 目標 $40B ARR | 季度財報 |
| Token 定價戰 | DeepSeek $1.74/$3.48 當前最低 | 每月 |
| 中文 token 乘數 | Claude 1.71× / DeepSeek 0.95× | 每次模型更新 |
| 物理 AI 融資 | AMI $1.03B / World Labs $1B | 重大融資事件 |
| 訂閱制 → token 計費趨勢 | GitHub Copilot 已轉 | 每季 |

---

*最後更新：2026-05-16 | 下次建議更新：2026-06-01（05 月月報完成後）*
