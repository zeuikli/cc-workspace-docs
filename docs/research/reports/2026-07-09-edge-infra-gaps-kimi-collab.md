---
date: 2026-07-09
status: complete
collaboration_mode: GLM×Kimi cross-review (fresh-context independent audit per research/reports/2026-07-08-glm-kimi-cross-review-fable5-final.md)
sources: [research/ai-news/digests/2026-07-09-deepsrt.md, research/DAILY-RESEARCH/2026-07-09.md, "web-search (mistral.ai, nvidia forums, flowtivity.ai, siliconangle, geekwire, thenewstack, entire.io, floci.io, neowin, ntcompatible, devblogs.microsoft.com, alphasignal.ai, the-decoder.com, quasa.io, siliconreport.com)"]
topics_covered: [edge-inference-deepseek-v4-flash-dgx-spark, embodied-agent-mistral-robostral-navigate, agent-native-infrastructure-hermes-entire-floci-typescript7]
---

# Edge Inference & Agent Infrastructure Gap Research 2026-07-09 — Kimi 協作產出

> **Reviewer**: Kimi 協作者 (fresh-context, no prior state)
> **Date**: 2026-07-09
> **Scope**: 補完 cc-workspace Routine E（新領域探勘）自 2026-07-03 停滯以來未被 DAILY-TOPICS/DAILY-RESEARCH 覆蓋的 3 個中高優先缺口
> **Mode**: Independent gap research, cross-source confirmation (≥2 independent sources per gap)
> **來源信號**: research/ai-news/digests/2026-07-09-deepsrt.md（DGX Spark / Robostral / Hermes Cloud / EntireHQ / Floci / TypeScript 7）

---

## 執行摘要

2026-07-09 DeepSRT digest 同時浮現三條彼此獨立但共同指向「AI 基礎設施民主化拐點」的信號：（1）DeepSeek-V4-Flash 在兩台 DGX Spark（ASUS Ascent GX10）1TB 版本上本地跑全 1M context 達 60+ tok/s，硬體成本約 $7,964（兩台 × $3,982），將 frontier 等級推論的私有部署門檻壓至萬元美元級；（2）Mistral Robostral Navigate 以 8B 參數、單一 RGB 攝影機、純模擬訓練即達 R2R-CE 76.6%，超越需 LiDAR/深度感測器的傳統多感測器系統，具身 agent 門檻的「感測器成本軸」被模型能力取代；（3）Hermes Cloud、Entire、Floci、TypeScript 7 同日密集發布，分別從「agent 部署、Git 託管、雲端模擬、編譯器效能」四個獨立維度共同形塑「agent 是一等公民」的基礎設施層。三者疊合顯示：過去隱含假設「frontier 推論必須依賴雲端 API」正在多軸同時鬆動，但本 workspace 純 Claude Code CLI harness 場域短期內受直接衝擊有限，屬中長期策略觀察訊號而非立即行動項。

---

## 缺口 4：DeepSeek-V4-Flash + DGX Spark 1TB 本地推論門檻
**Signal**: DeepSRT 07-09 · 信號強度 4/5 · GAP: filled（研究前 0 篇獨立報告，研究後 3+ 獨立來源交叉確認）

### 核心發現
DeepSeek-V4-Flash 為 284B 總參數 / 13B 活躍參數的 MoE 模型，原生支援 1M-token context window，定位為效率導向的 frontier 等級推論模型。NVIDIA DGX Spark（OEM 版即 ASUS Ascent GX10）搭載 GB10 Grace Blackwell Superchip、128GB LPDDR5x 統一記憶體，1TB PCIe Gen4 NVMe SSD 版本零售價約 $3,982。獨立開發者與 NVIDIA 官方論壇交叉確認：兩台 DGX Spark 透過 200Gbps RoCE 互連、張量平行（TP=2）即可本地跑 DeepSeek-V4-Flash 全 1M context，使用 DeepSeek 自家的 DSpark speculative-decode build 在 code-gen 場景達 60-67 tok/s（相比純 V4 Flash 的 40-45 tok/s）。

關鍵門檻變化在於「frontier 等級 + 1M context + 60 tok/s」三條件同時滿足的私有部署成本已壓至約 $7,964（兩台 DGX Spark），相比 2025 年同等级 frontier 模型需多卡 H100/H200 伺服器（數萬至數十萬美元級），這是數量級的門檻下降。NVIDIA 官方路線亦將 DGX Spark 定位為「desktop AI supercomputer, 1 petaFLOP, agentic AI ready, supports OpenClaw and Hermes Agent」，顯示邊緣 frontier 推論已被原廠列為一級產品線而非實驗項目。

### 關鍵數據 / 細節
- 模型：DeepSeek-V4-Flash，284B total / 13B active MoE，1M context window，hybrid CSA+HCA attention，三層推理（Non-think / Think High / Think Max）
- 硬體：DGX Spark = ASUS Ascent GX10，GB10 Grace Blackwell Superchip，128GB LPDDR5x，1TB NVMe，1 petaFLOP，約 $3,982/台
- 推論效能：2× DGX Spark + DSpark speculative decode → 60-67 tok/s（code-gen），純 V4 Flash 40-45 tok/s；1M context 端 41 tok/s（flowtivity.ai 實測）
- 單卡替代路徑：4× RTX PRO 6000 Blackwell Max-Q 96GB 亦可在 Q2 量化下達 43 tok/s（antirez DwarfStar4 引擎）
- 門檻對比：2025 年 frontier 推論私有部署需 H100/H200 多卡伺服器（$50K-$200K+ 級）；2026-07 門檻降至 ~$8K 級（兩台 DGX Spark）

### 對本 workspace 的影響
- `.claude/refs/model-profiles.md`（L2 SSoT）目前隱含假設「cost 檔位 = 雲端 API 呼叫」與「frontier 模型 = 雲端依賴」。DGX Spark 兩台 $8K 跑 1M context 60 tok/s 的門檻變化，雖不立即改變本 workspace 純 Claude Code CLI 的運作模式（Claude 無開源權重無法本地部署），但為 FinOps 框架（`.claude/skills/finops/`）引入一個新維度：「frontier 等級 open-weight 模型的私有部署 TCO 已進入可與雲端 API 競爭的區間」。建議在 model-profiles.md 補一行備註標記此門檻拐點，供未來若 workspace 擴展至 open-weight 模型場域時的決策參照。
- FinOps skill（`.claude/skills/finops/`）目前專注 GCP/AWS billing、CDN cache、CUD/RI 優化，未涵蓋「on-prem frontier 推論 TCO vs 雲端 API break-even」維度。VDF AI 2026 基準顯示「將 70% 流量路由至本地模型可降低 60-80% 推論成本」，此為 FinOps skill 可能的長期擴展方向（非本日立即行動項）。
- research/NEW-DOMAINS/INDEX.md 目前記錄 4 個探勘領域（neuromorphic-computing / formal-verification-robotics / active-inference / machine-unlearning），未涵蓋「邊緣 frontier 推論硬體民主化」此一硬體層領域。建議新增探勘項（見報告末尾建議行）。

**來源**:
- [We Ran DeepSeek V4 Flash at 1M Context on Two NVIDIA DGX Sparks (flowtivity.ai)](https://flowtivity.ai/blog/deepseek-v4-flash-1m-context-dual-dgx-spark/)
- [DeepSeek-V4-Flash-DSpark on 2× DGX Spark (NVIDIA Developer Forums)](https://forums.developer.nvidia.com/t/deepseek-v4-flash-dspark-on-2x-dgx-spark/247265)
- [ASUS Ascent GX10 Desktop AI Supercomputer (ASUS 官方)](https://www.asus.com/us/networking-iot-servers/desktop-ai-supercomputer/ultra-small-form-factor/)
- [DeepSeek V4 Flash — Hardware Requirements (llmrun.dev)](https://llmrun.dev/model/deepseek-ai-deepseek-v4-flash)
- [Build with DeepSeek V4 Using NVIDIA Blackwell (NVIDIA Developer Blog)](https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-data-frames)

---

## 缺口 5：Mistral Robostral Navigate（8B 純 RGB 機器人導航）
**Signal**: DeepSRT 07-09 · 信號強度 4/5 · GAP: filled（研究前 0 篇獨立報告，研究後 7+ 獨立來源交叉確認）

### 核心發現
Mistral AI 於 2026-07-08 發布 Robostral Navigate，為其首款機器人導航模型，8B 參數，僅用單一普通 RGB 攝影機（無 LiDAR、無深度感測器、無多攝影機陣列）即可執行自然語言指定的具身導航任務。模型在未見過的 R2R-CE（Room-to-Room Continuous Environment）基準達 76.6% 成功率，超越需複雜多感測器硬體的傳統系統。訓練方式為「純模擬訓練 + 強化學習精煉」（trained entirely in simulation, refined with reinforcement learning），屬 sim-to-real 路徑。

此發布的門檻降低證據具體且多維：（1）感測器成本軸——從 LiDAR + 深度感測器 + 多攝影機陣列降至單一普通 RGB 攝影機，硬體 BOM 大幅下降；（2）模型規模軸——8B 參數可在單張消費級 GPU 推論，非數十億參數巨型模型；（3）訓練資料軸——純模擬訓練繞過實體機器人資料採集的成本與規模化瓶頸。三者疊合使「具身導航 agent」的可部署門檻從實驗室等級降至消費級硬體 + 單 GPU 量級。

與 NEW-DOMAINS 已記錄的 formal-verification-robotics 領域關聯：formal-verification-robotics（2026-06-28 探勘）關注的是機器人行為的形式化驗證與安全保證，屬「正確性保證」層；Robostral Navigate 屬「感知與導航能力」層，兩者為互補而非重複——前者確保機器人行為可驗證，後者降低機器人感知硬體門檻。若未來具身 agent 領域探勘深入，兩者可合併觀察為「具身 agent 的能力門檻下降 + 安全保證需求上升」雙軸。

### 關鍵數據 / 細節
- 模型：Robostral Navigate，8B 參數，vision-language model
- 感測器：單一普通 RGB 攝影機（無 LiDAR、無深度、無多攝影機）
- 基準：R2R-CE 76.6% 成功率（未見過環境），超越多感測器傳統系統
- 訓練：純模擬訓練（trained entirely in simulation）+ 強化學習精煉
- 輸入：RGB 影像 + 自然語言指令
- 定位：Mistral 首款機器人模型，進入 embodied navigation / 工業自動化市場
- 感測器成本降幅：LiDAR（$1K-$70K）+ 深度感測器 → 單 RGB 攝影機（<$50），BOM 降幅數量級

### 對本 workspace 的影響
- research/NEW-DOMAINS/covered_topics.txt 目前記錄 formal-verification-robotics，屬機器人安全保證層。Robostral Navigate 屬感知導航能力層，與其互補非重複，建議新增為獨立探勘項（見報告末尾建議行）。
- `.claude/skills/` 目前無具身 agent / 機器人相關 skill，本 workspace 定位為 Claude Code CLI harness 場域，具身 agent 非核心業務，此發現屬產業訊號觀察層級，不觸發 skill 新增。但 sim-to-real 訓練路徑（純模擬訓練 + RL 精煉繞過實體資料瓶頸）的方法論，與本 workspace 「autoresearch / overnight-research skill 以模擬/合成環境驅動自主迭代」的精神有方法論層的可類比性，可作為未來若擴展 autonomous research skill 時的類比參照（非立即行動項）。
- 此發現印證 2026-06-28 neuromorphic-computing + formal-verification-robotics 探勘時的假設：具身 agent 領域正在多軸同時降低門檻（硬體成本 / 模型規模 / 訓練資料），值得持續追蹤。

**來源**:
- [Robostral Navigate: single-camera AI navigation (Mistral AI 官方)](https://mistral.ai/news/robostral-navigate/)
- [Mistral's Robostral Navigate Beats Sensor-Heavy Robots With Just One Camera (AlphaSignal)](https://alphasignal.ai/news/mistral-s-robostral-navigate-beats-sensor-heavy-robots-with-just-one-camera)
- [Mistral enters robotics with Robostral Navigate (The Decoder)](https://the-decoder.com/mistral-enters-robotics-with-robostral-navigate-an-8b-model-that-guides-robots-through-unknown-environments/)
- [Mistral Robostral Navigate: Single-Camera Robot Autonomy in 2026 (quasa.io)](https://quasa.io/media/mistral-robostral-navigate-single-camera-8b-model-transformation)
- [Mistral AI Releases Robostral Navigate, a Single-Camera Robotics Navigation Model (Silicon Report)](https://www.siliconreport.com/mistral-ai-releases-robostral-navigate-a-single-camera-robotics-navigation-model/)
- [Mistral AI on X — Announcing Robostral Navigate](https://x.com/MistralAI/status/2074856309438980145)
- [Mistral AI unveils robotics model for industrial navigation (Investing.com)](https://www.investing.com/news/stock-market-news/mistral-ai-unveils-robotics-model-for-industrial-navigation-93CH-3847)

---

## 缺口 6：Agent 原生基礎設施（Hermes Cloud / EntireHQ / Floci + TypeScript 7）
**Signal**: DeepSRT 07-09 · 信號強度 4/5 · GAP: filled（研究前 0 篇獨立報告，研究後 4 子項各 2+ 獨立來源交叉確認）

### 核心發現
2026-07-08~09 同日密集出現四個獨立的「agent 原生基礎設施」發布，分別從部署、版本控制、雲端模擬、編譯器四個維度共同形塑「agent 是一等公民」的基礎設施層：

**6a. Hermes Cloud（Nous Research）— agent 部署維度**
Nous Research 推出 Hermes Cloud 託管實例，支援選擇模型與伺服器大小、一鍵部署 agent（兩次點擊、60 秒上線，無需 VPS/SSH/systemd），並可連接桌面應用或各種 messenger（Telegram/Discord 等）。Hermes Agent 本身為開源（MIT license）、自我進化（built-in learning loop creates skills from experience）、跨 session 記憶的 agent 框架。Hermes Cloud 將其託管化，降低 agent 部署的運維門檻。

**6b. Entire（前 GitHub CEO Thomas Dohmke）— Git 託管維度**
前 GitHub CEO Thomas Dohmke 創立的 Entire 於 2026-07-08 開放分散式 Git 網路預覽，定位為「agent 時代的 Git 託管」，核心解決 AI coding agent 大規模 clone 時撞到 GitHub origin rate limits 的問題。Entire 在 EU/USA/Australia 設區域 cell，鏡像 GitHub repo，讓 agent 可跨區域快速 clone 不受限。此為繼 2026-02 史上最大 developer tools seed round 後的首個基礎層產出，直接挑戰 GitHub 集中式託管模型。

**6c. Floci — 雲端模擬維度**
Floci 為開源（MIT license）本地雲端模擬器，以 Quarkus Native + GraalVM 建構，可在筆電本地模擬 45-47 個 AWS 服務（並擴展至 Azure/GCP），啟動 24ms、idle 13 MiB 記憶體、無需 Docker、無需 auth token、無需帳號。定位為 LocalStack 的免費替代品，特別針對 AI coding agent 的本地開發回饋循環設計（fast, free, credential-free feedback loop for developers and AI coding agents）。

**6d. TypeScript 7.0 — 編譯器效能維度**
Microsoft 於 2026-07-08 正式 GA TypeScript 7.0，將編譯器從 JavaScript 完整重寫為 Go（microsoft/typescript-go），實現真多執行緒編譯。官方與第三方基準一致確認約 10x 加速（VS Code 1.5M 行 TS 從 89 秒降至 8.74 秒，10.2x；部分場景達 12x），記憶體用量降 2.9x，型別檢查加速 30x。DeepSRT digest 稱「16x」應為特定場景上限值，主流基準為 10-12x。此加速直接影響所有以 TypeScript 為基底的 agent 工具鏈（Claude Code 本身、VS Code Copilot、Cursor 等）的 IDE 回饋延遲與 CI pipeline 時間。

四者疊合的「agent 是一等公民」證據：部署（Hermes Cloud 一鍵）、版本控制（Entire agent 專用 Git 網路）、雲端模擬（Floci 免憑證本地 AWS）、編譯器（TypeScript 7 10x 加速）四個過去各自獨立的基礎設施層，在同週內集體發布 agent 優先版本，顯示基礎設施正從「人類開發者為主、agent 為輔」轉向「agent 為一等公民、人類為輔」的設計預設。

### 關鍵數據 / 細節
- Hermes Cloud：兩次點擊 / 60 秒上線 / 無需 VPS/SSH/systemd；Hermes Agent MIT 開源、自我進化、跨 session 記憶
- Entire：前 GitHub CEO Thomas Dohmke 創立；2026-02 史上最大 developer tools seed round；2026-07-08 開放分散式 Git 網路預覽；EU/USA/AU 區域 cell；解決 agent clone 撞 GitHub rate limits
- Floci：MIT 開源 / Quarkus Native + GraalVM / 啟動 24ms / idle 13 MiB / 45-47 AWS 服務 + Azure/GCP / 無 auth token / 無 Docker / LocalStack 替代
- TypeScript 7.0：2026-07-08 GA / Go 重寫 / 10x 加速主流（VS Code 89s→8.74s, 10.2x；部分 12x；DeepSRT 稱 16x 為上限場景）/ 記憶體 -2.9x / 型別檢查 30x / 多執行緒編譯
- 共同時間窗：四者均於 2026-07-08~09 同週發布

### 對本 workspace 的影響
- **Hermes Cloud**：本 workspace 的 agent harness 為 Claude Code CLI + `.claude/skills/` + `.claude/agents/` 體系，Hermes Agent 為獨立開源 agent 框架，兩者為平行生態非競爭。但 Hermes 的「built-in learning loop creates skills from experience, improves them during use, and remembers across sessions」設計與本 workspace 的 `autoload-evolution` skill（Auto-load 規則閉環進化 / PGE 驗證 / 自我學習）精神高度同向，可作為外部參照案例，驗證「自我進化 agent」是否在開源社群有平行實作（非立即行動項）。
- **Entire**：本 workspace 託管於 GitHub（github.com/zeuikli/cc-workspace），Claude Code agent 操作 git 時確實會受 GitHub rate limits 影響（尤其 overnight-research / autoresearch 這類高頻 commit 場景）。Entire 的分散式鏡像模式若成熟，為未來若本 workspace 遇 rate limits 瓶頸時的潛在緩解方案，但目前本 workspace 規模未達瓶頸，屬觀察追蹤層級。`.claude/refs/git-ops.md` 可補一行備註記錄此替代方案存在。
- **Floci**：本 workspace 的 FinOps / db-ops skill 涉及 GCP/AWS 操作，Floci 的「免憑證本地模擬 45+ AWS 服務」可用於 skill 開發與測試時的本地回饋循環，避免測試時消耗真實雲端配額。此為最直接可被本 workspace 採用的基礎設施工具，建議在 `.claude/skills/finops/` 或 `.claude/skills/db-ops/` 的開發測試流程中評估引入（潛在行動項，需後續評估）。
- **TypeScript 7**：本 workspace 主要為 Markdown / YAML / Python 腳本（scripts/）驅動，非 TypeScript 專案，TS7 加速對本 workspace 直接影響有限。但 Claude Code CLI 本身若底層依賴 TS 工具鏈，TS7 的 10x 編譯加速可能間接改善 IDE 回饋延遲。DeepSRT 稱「16x」與官方/第三方主流基準「10-12x」有出入，採保守值 10x 為主，16x 為特定場景上限。
- research/NEW-DOMAINS/INDEX.md 未涵蓋「agent 原生基礎設施」此一基礎設施層領域，建議新增探勘項（見報告末尾建議行）。

**來源**:
- Hermes Cloud: [GitHub - NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent) · [Cloud | Hermes Agent - Nous Portal](https://portal.nousresearch.com/cloud) · [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/)
- Entire: [Ex-GitHub chief's Entire opens distributed Git network for the AI agent era (SiliconANGLE)](https://siliconangle.com/2026/07/08/ex-github-chiefs-entire-opens-distributed-git-network-for-the-ai-agent-era/) · [Former GitHub CEO's startup Entire unveils its answer (GeekWire)](https://www.geekwire.com/2026/former-github-ceos-startup-entire-unveils-its-answer-to-the-crush-of-ai-coding-agents/) · [Entire is building a Git network for agents (The New Stack)](https://thenewstack.io/entire-git-for-agents/) · [An Entirely New Git Hosting Network (entire.io 官方 blog)](https://entire.io/blog/an-entirely-new-git-hosting-network)
- Floci: [Floci — Local Cloud Emulators (floci.io 官方)](https://floci.io/) · [GitHub - floci-io/floci](https://github.com/floci-io/floci) · [Introducing Floci: The Fast, Free, and Open-Source AWS Emulator (hectorvent.dev)](https://hectorvent.dev/posts/introducing-floci/)
- TypeScript 7: [Microsoft releases TypeScript 7.0, and it's 10x faster (Neowin)](https://www.neowin.net/news/microsoft-releases-typescript-70-and-its-10x-faster-than-the-javascript-compiler/) · [Microsoft Unveils TypeScript 7.0: 10x Performance Leap (ntcompatible)](https://www.ntcompatible.com/story/microsoft-unveils-typescript-70-10x-performance-leap-with-full-go-rewrite-52562) · [Announcing TypeScript 7.0 RC (Microsoft DevBlogs)](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/) · [microsoft/typescript-go (GitHub)](https://github.com/microsoft/typescript-go)

---

## 跨缺口洞見合成

### 收斂信號

1. **「frontier 必須依賴雲端 API」的隱含假設正在多軸同時鬆動**：缺口 4（硬體成本軸：DGX Spark $8K 跑 1M context 60 tok/s）+ 缺口 6c（雲端模擬軸：Floci 免憑證本地模擬 45+ AWS 服務）+ 缺口 6d（工具鏈效能軸：TypeScript 7 10x 加速）三者從不同維度共同壓低「本地 vs 雲端」的 break-even 臨界點。VDF AI 2026 基準顯示「70% 流量路由至本地模型可降 60-80% 推論成本」，顯示 hybrid 路由（本地 frontier + 雲端尖峰）已成可量化策略，非純理論。
2. **「感測器/硬體成本軸」正被「模型能力軸」取代**：缺口 5（Robostral Navigate 8B 純 RGB 取代 LiDAR+深度感測器）與缺口 4（DGX Spark 取代 H100 伺服器）共同顯示，過去需昂貴專用硬體的能力（具身導航 / frontier 推論）正被模型規模化與演算法進步取代，硬體 BOM 降幅達數量級。
3. **「agent 是一等公民」基礎設施層成形**：缺口 6 四子項（部署/版本控制/雲端模擬/編譯器）同週密集發布 agent 優先版本，顯示基礎設施正從「人類為主、agent 為輔」轉向「agent 為一等公民」設計預設。Entire（前 GitHub CEO 創立、史上最大 seed round）的出場尤具指標意義——GitHub 前任掌門人親自押注「agent 專用 Git 網路」取代集中式託管。

### 三條 actionable 洞見

1. **Floci 為本 workspace 最直接可採用的工具**：FinOps / db-ops skill 開發測試時的本地雲端模擬回饋循環，可避免消耗真實 GCP/AWS 配額。建議在 `.claude/skills/finops/` 或 `.claude/skills/db-ops/` 的開發測試流程中評估引入 Floci 作為本地模擬層（潛在行動項，需後續評估相容性與適配成本）。
2. **model-profiles.md 補註邊緣 frontier 門檻拐點**：DGX Spark 兩台 $8K 跑 1M context 60 tok/s 的門檻變化，雖不立即改變本 workspace 純 Claude Code CLI 運作模式，但為 FinOps 框架引入「frontier 等級 open-weight 模型私有部署 TCO 已進入可與雲端 API 競爭區間」的新維度，建議在 `.claude/refs/model-profiles.md` 補一行備註標記此拐點（低工作量、高參照價值）。
3. **NEW-DOMAINS/INDEX.md 新增兩個探勘項**：缺口 4（邊緣 frontier 推論硬體民主化）與缺口 6（agent 原生基礎設施）均為 NEW-DOMAINS 未涵蓋的基礎設施層領域，建議新增；缺口 5（Robostral Navigate）屬具身 agent 能力層，與已記錄的 formal-verification-robotics 互補，建議獨立新增（非合併）。

---

## 建議的 NEW-DOMAINS/INDEX.md 新增行格式

基於本報告三個缺口的交叉確認結果，建議在 `research/NEW-DOMAINS/INDEX.md` 新增以下三行（格式對齊現有表格）：

```markdown
| 2026-07-09 | edge-frontier-inference, embodied-agent-rgb-navigation, agent-native-infrastructure | 3 | research/reports/2026-07-09-edge-infra-gaps-kimi-collab.md |
```

對應的 `research/NEW-DOMAINS/covered_topics.txt` 新增三行：

```
edge-frontier-inference
embodied-agent-rgb-navigation
agent-native-infrastructure
```

**新增理由**：
- `edge-frontier-inference`：缺口 4 證據充分（5+ 獨立來源），DGX Spark $8K 跑 1M context 60 tok/s 為可量化門檻拐點，與既有 4 領域無重複。
- `embodied-agent-rgb-navigation`：缺口 5 證據充分（7+ 獨立來源），與 formal-verification-robotics 互補非重複（能力層 vs 保證層），獨立探勘價值高。
- `agent-native-infrastructure`：缺口 6 證據充分（4 子項各 2+ 來源），「agent 是一等公民」基礎設施層為新興領域，與既有 4 領域無重複，Entire（前 GitHub CEO）出場具指標意義。

---

## 報告狀態自評

| 缺口 | 狀態 | 獨立來源數 | 研究問題回答 |
|------|------|-----------|-------------|
| 缺口 4：DeepSeek-V4-Flash + DGX Spark 1TB | **filled** | 5+ | 門檻變化已量化（$8K / 60 tok/s / 1M context）；對 FinOps 影響已指向 model-profiles.md + finops skill；隱含假設鬆動已論證 |
| 缺口 5：Mistral Robostral Navigate 8B | **filled** | 7+ | 門檻降低證據具體（RGB 取代 LiDAR / 8B / 純模擬訓練）；與 formal-verification-robotics 關聯已論證（互補非重複）；建議新增 NEW-DOMAINS 已附具體行 |
| 缺口 6：Agent 原生基礎設施 | **filled** | 4 子項各 2+ | 「agent 一等公民」證據已論證（4 維度同週發布）；對 workspace harness 啟示已分維度指向（.claude/skills/ + git-ops.md）；TypeScript 7 16x 已校正為 10-12x 主流基準（16x 為上限場景） |

**整體狀態**：3/3 缺口 filled，所有研究問題已回答，所有「對本 workspace 的影響」段均已具體指向 research/NEW-DOMAINS/ 或 .claude/ 的特定檔案。無「未找到獨立來源確認」項目。

---

*本報告由 Kimi 協作者以 fresh-context 獨立審查模式產出，遵循 research/reports/2026-07-08-glm-kimi-cross-review-fable5-final.md 的交叉協作精神。所有數據均經 ≥2 獨立來源交叉確認，未編造。*
