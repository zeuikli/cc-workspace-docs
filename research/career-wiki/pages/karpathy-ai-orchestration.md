# AI Orchestration Engineering（Karpathy 範式轉換）

> **Source positions**: CathaySec 2024–now（實踐）、Cross-career forward-looking（2026+）
> **Last ingested**: 2026-04-22
> **Confidence**: medium（研究洞見 + 個人實踐；Agent 可靠性數據來自 Karpathy 一手觀察）
> **Linted**: 2026-04-22
> **Tags**: ai-orchestration, agentic-engineering, career-transition, devops-ai, llm-tooling
> **Career phase**: current + forward-looking（Software 3.0 過渡期）

---

## TL;DR

工程師角色正從「撰寫程式碼」轉向「編排 AI 代理」，K8s 架構設計與 FinOps 判斷保值，Terraform 生成層與 Runbook 撰寫被取代，Claude Code 工具熟練度是 2026 稀缺差異化。

---

## Context

AI 代理（Agent）的可靠性已足以承擔 DevOps/SRE 工作流中的部分子任務（Log 分析、IaC 草稿生成），但全自動 incident response 仍不適合生產環境（2027+ 才成熟）。當前轉型窗口適合：主動評估哪些工作可委派 AI、哪些保留人工判斷、怎麼設計 acceptance criteria 讓 AI 代理可以自我驗收。

---

## Core Methodology

### Step 1 — 理解 Software 進化三階段

- **What**: 區分 Software 1.0（手工 HCL/YAML）、2.0（ML 模型推理）、3.0（自然語言為程式介面）
- **Why**: 每個階段需要不同技能；誤把 3.0 工具當 1.0 使用（只用來做 autocomplete）會錯失 10x 效率提升；誤信 3.0 完全取代判斷力會在生產環境出事
- **Gotcha**: Software 3.0 不等於「不用理解底層」；Karpathy 親身示範的是「不寫程式碼」，但他理解程式碼的能力沒有消失——這是他能設計驗收條件的原因。對 SRE 同理：不再手寫 Terraform 不代表可以不懂網路架構

### Step 2 — 分類任務可靠性，決定委派邊界

- **What**: 針對每個 DevOps 工作場景評估 AI 代理可靠性（高 / 中 / 低），決定：直接委派、人工確認後執行、還是保留人工
- **Why**: Karpathy 明確指出當前代理系統仍脆弱——多步驟依賴任務、API 呼叫失敗恢復、長時間任務累積錯誤；盲目信任代理比手動更慢
- **Gotcha** [CathaySec Claude Code 實踐]: IaC 草稿生成可靠性高，但需要搭配 `/devops-review` 審查；曾讓 Claude 生成 Terraform 模組，輸出結構正確但 IAM 綁定有遺漏——沒 review 就 apply 會有安全風險

### Step 3 — 設計驗收條件（Acceptance Criteria）而非指令

- **What**: 不給 AI 「做 X」的指令，而是給「完成條件是：tests green、`terraform validate` pass、checkov 零 critical issue」
- **Why**: 驗收條件讓 AI 代理可以自我迴圈修正（Goal-Driven Execution，Karpathy autoresearch 模式）；純指令式 prompt 只有一次機會，驗收條件驅動的 prompt 讓代理迭代直到達標
- **Gotcha**: 驗收條件要可機器驗證（exit code 0/非 0），不能是「看起來對」；「格式正確」≠ 驗收條件，「`yamllint` exit 0 且 `kubectl dry-run` 無 error」才是

### Step 4 — 建立個人 AI 工具熟練度護城河

- **What**: 深度掌握 Claude Code、掌握 subagent 委派模式、建立 Skills / Agents 知識庫（即 cc-workspace 的設計）
- **Why**: Karpathy 確認 Claude Code 是 2025 最重要的工程實踐案例；熟練度是技能不是工具——工具換代但「如何設計驗收條件、如何拆分 agent 任務、如何管理 context rot」這些能力跨工具轉移
- **Gotcha**: 不要只學 UI 操作（`/help` 指令列表），要學心智模型（何時用 subagent、何時 compact、何時 advisor）；UI 操作被下一版 Claude Code 改掉，心智模型不會

### Step 5 — 從低風險場景起步 PoC，建立信任

- **What**: 第一個 PoC 選「有明確 ground truth 的場景」：Log 錯誤分析（人工比對可驗證）、Runbook 起草（人工最終確認）
- **Why**: 在 CathaySec 或其他金融場景，全自動執行操作風險過高；先積累「AI 代理出的結論準確率」的統計數據，才能向管理層提案擴展自動化範圍
- **Gotcha**: PoC 失敗最常見原因不是 AI 能力不足，而是 prompt 太模糊（缺驗收條件）或任務邊界太大（太多步驟依賴）；縮小任務邊界比換模型有效

---

## Concrete Numbers

| 指標 | 值 | 來源場景 |
|------|----|---------|
| Karpathy AI 代理工作時長 | 16 小時/日連續迴圈 | AutoResearch 項目（2025-12 起）|
| 停止手工編碼時間點 | 2025-12（Karpathy 個人）| No Priors Podcast 2026-03 |
| Log 分析 AI 代理可靠性 | ✅ 高（立即可用）| Karpathy Dwarkesh Podcast 評估 |
| IaC 自動生成（有 review）| ✅ 高 | CathaySec `/devops-review` 實踐 |
| 全自動 incident response | ❌ 低（2027+ 才適合）| Karpathy 可靠性評估 |
| Runbook 自動化（有確認節點）| ⚠️ 中等 | Karpathy 評估 |
| KKStream 年省（SRE 工程）| $150,000 USD/年 | 人工 SRE 決策驅動，AI 工具輔助未來可擴大 |
| CathaySec FinOps 年省 | NT$400,000/年 | 人工判斷 + IaC 自動化 |
| Claude Code skill 市場稀缺度 | ✅ 極高（2026 現狀）| Karpathy + Zeuik 職涯評估 |
| K8s 架構設計 AI 可替代性 | ✅ 低（保值）| 系統設計 = 人工判斷核心 |
| Terraform HCL 生成 AI 可替代性 | ⚠️ 高（被部分取代）| Software 3.0 生成層 |

---

## Anti-patterns（不要做）

1. **把 AI 代理當 autocomplete 用**
   - 問題：只用 Claude 生成程式碼片段、不設計驗收條件、不讓代理迭代——等於用 10x 的工具做 1x 的事
   - 解：每次委派任務都給「Acceptance criteria」清單，讓代理自我驗收後回報；至少用 `/devops-review` 做後期審查

2. **過度信任代理，跳過 review**
   - 問題：IaC 草稿生成可靠性高，但 IAM / 網路安全設定有細節風險；金融場景任何安全配置錯誤代價極高
   - 解：AI 生成 → 人工 security review（checkov + 人眼）→ 才 apply；`IaC 生成` 和 `IaC apply` 永遠是兩個分開的決策點

3. **等 AGI 成熟才開始用 AI 工具**
   - 問題：Karpathy 明確說 AGI 仍需十年，但 Claude Code 等工具 2025–2026 就已創造 10x 工程效率；等待等於放棄窗口期優勢
   - 解：從低風險場景（Log 分析、Runbook 起草）開始，累積實戰經驗和信任數據，再逐步擴展自動化範圍

4. **用 AI 取代系統設計判斷**
   - 問題：Karpathy 停止手工編碼，但他對「為什麼這樣設計」的判斷從未外包給 AI；K8s 多租戶隔離設計、GCP 網路架構決策、FinOps 投資優先級都需要人類判斷
   - 解：AI 負責「執行層」（生成 HCL、寫 Runbook、分析 Log）；人類保留「決策層」（架構選型、安全邊界、成本優先級）

---

## Decision Tree

```
收到一個 DevOps/SRE 工作任務，要不要委派 AI 代理？

任務是否有明確的可驗證輸出？
├─ 否（需要「感覺對」的主觀判斷）→ 人工處理，AI 僅做草稿建議
└─ 是 → 繼續

任務步驟數量？
├─ 1–3 步（線性）→ 直接委派 AI，設定驗收條件
├─ 4–8 步（中等）→ 委派 + 人工確認節點（每 3 步一個 checkpoint）
└─ > 8 步且互相依賴 → 拆解成子任務後分批委派，不整體委派

風險等級（生產環境影響）？
├─ 低（唯讀、dev 環境、草稿生成）→ 直接委派，低監控
├─ 中（staging apply、config 變更）→ 委派 + plan 審查 + 人工 approve
└─ 高（prod DB 操作、IAM 變更、網路規則）→ AI 輔助起草，人工全程審查 + 執行

AI 代理可靠性分類
├─ Log 分析、告警摘要 → ✅ 高可靠，立即委派
├─ IaC 草稿生成 → ✅ 高（需 /devops-review 後置審查）
├─ Runbook 起草 → ✅ 高（需人工最終確認）
├─ Runbook 自動執行 → ⚠️ 中，先 PoC + 設人工確認節點
├─ FinOps 優化建議 → ✅ 高（建議層，不直接執行）
└─ 全自動 incident response → ❌ 低，2027+ 才考慮生產部署
```

---

## References

- 主要研究來源：`research/karpathy-ai-2026.md`（完整 Karpathy 觀點分析）
- [Karpathy Software 2.0（2017）](https://karpathy.medium.com/software-2-0-a64152b37c35)
- [No Priors Podcast 2026-03 — 停止手工編碼、AutoResearch](https://pjfp.com/andrej-karpathy-on-autoresearch-ai-agents-and-why-he-stopped-writing-code-full-breakdown-of-his-2026-no-priors-interview/)
- [Dwarkesh Podcast — AGI 十年、代理可靠性警示](https://www.dwarkesh.com/p/andrej-karpathy)
- [AutoResearch GitHub](https://github.com/karpathy/autoresearch)
- [Karpathy 2025 LLM 年度回顧](https://karpathy.bearblog.dev/year-in-review-2025/)
- 職涯段：`raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- 關聯：[[gcp-terraform-iac-patterns]]、[[finops-cross-position-patterns]]、[[ansible-gha-automation]]、[[gcp-landing-zone]]
