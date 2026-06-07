# Prompt Caching × Management × Engineering — 整合研究報告

**日期**：2026-06-03 | **Branch**：`feature/prompt-caching-engineering-research`
**研究方法**：以平行 researcher subagents fan-out 模擬 overnight-research 的搜尋階段（盤點既有材料 → 三主題缺口並行調查 → 全文歸檔 → 整合驗證）；信度分層歸檔對應 research-hub:deep、缺口收斂對應 autoresearch 的迭代精神。**誠實標注：未直接呼叫該三 skill 的 SKILL runner，而是用其方法論骨架由主 agent 編排。**
**Target 假設（釘死）**：所有發現以「可套用到本 cc-workspace harness」為驗收終點 — 見姊妹計劃書 `2026-06-03-prompt-harness-action-plan.md`
**信度標注**：🟢 官方一手（provider docs / arXiv 原文）｜🟡 論文 peer-reviewable｜🟠 社群二手（blog / GitHub issue / 工具方文章）

---

## 執行摘要

Prompt 三主題在 2026 年已從「技巧」演化為「工程紀律」。本報告整合既有 5 篇論文 + 3 份 best-practices，並補齊三主題的系統性缺口，得出三個核心結論：

1. **Caching 是經濟學，不是開關**：跨 provider 的回本門檻差異巨大（OpenAI/Google-implicit 第 1 次重用即回本；Anthropic 5min TTL 需 ≥2 次、1h TTL 需 ≥3 次）。選錯 TTL 或 placement 會讓快取「越用越貴」。
2. **Management 是三主題中缺口最大、ROI 最高的一塊**：versioning / registry / A/B / 注入防禦在既有材料中近乎空白，而這正是把「prompt 從 demo 推到 production」的關鍵基礎設施。
3. **Engineering 隨模型能力非線性反轉**：更強的模型需要**更簡單**的 prompt。`prompting-inversion`（GPT）在 Claude Opus 4.8 上以**字面化 + effort 旋鈕**的形式獲得官方一手確認 🟢 —「shallow reasoning 是 effort 問題，不是 prompt 問題」。

貫穿三主題的主線：**靜態前綴穩定（caching）→ 版本可追溯（management）→ 用 eval 而非直覺迭代（engineering）**，三者構成一條 prompt 生命週期的流水線。

---

## Section A：Prompt Caching — 經濟學與失效控制

### A.1 跨 Provider 成本模型（缺口補齊）🟢

| Provider / 模式 | Cache write 加價 | Cache read 折扣 | Storage 費 | 最小 token | 回本門檻 |
|---|---|---|---|---|---|
| Anthropic 5min TTL | +25% | 90% off（0.1×） | 無 | Opus 4.5/4.6/4.7/4.8 + Sonnet 4.5/4.6 = **1,024**；**僅 Haiku 4.5 = 4,096**（官方表親驗） | **≥2 次讀取** |
| Anthropic 1h TTL | +100% | 90% off | 無 | 同上 | **≥3 次讀取** |
| OpenAI（自動） | 無 | **up to 90% off**（官方原文，gpt-5.x；docs 親驗） | 無 | 1,024（親驗） | **≥1 次即回本** |
| Google Explicit | 無 | 90% off（Flash read $0.03 vs $0.30，親驗） | 有（2.5 Pro **$4.50/M·hr**，docs 親驗） | Pro 2,048 / Flash 1,024 | storage 費主導，需高使用率 |
| Google Implicit（2025 新） | 無 | ~75% off 🟠（researcher-reported，官方 pricing 頁未明列百分比，未獨立驗證） | 無 | 同上 | **≥1 次即回本** |

來源：**Anthropic Pricing/Prompt-Caching、OpenAI Prompt Caching Guide、Google AI Pricing 三者經主 agent WebFetch 親驗（🟢）**；唯 Google Implicit 75% 折扣官方 pricing 頁未列具體百分比，降標 🟠。OpenAI 官方原文："reduce input token costs by up to 90%" + "Caching happens automatically, with no explicit action needed or extra cost"。

**決策框架**：
- 偶發、短重用 → OpenAI / Google-implicit（無寫入成本，立即回本）。
- 高頻、同一前綴連發 → Anthropic 5min（最快收斂，2 次回本）。
- Agentic long-horizon（工具迴圈 >5min）→ Anthropic 1h TTL（避免 mid-loop cache miss），代價是 2× 寫入費。
- 大型靜態文件跨 session 批查（RAG / 法律）→ Google Explicit（storage 費換取跨 session 保留），但須先算 storage 是否吃掉折扣。

### A.2 Caching + Long-context 協同 🟢🟡

1. Anthropic 1M context **無 premium surcharge**，900k 與 9k 請求同 per-token 費率；caching 折扣全 context 統一適用。
2. **Batch + Caching multiplier 疊乘**：官方原文 "These multipliers stack with other pricing modifiers such as the Batch API discount"（prompt-caching docs 親驗）→ cache read 0.1× × batch 0.5× = **0.05×**（節省 95%）。
3. Gemini 2.5 Pro >200k 輸入標準價從 $1.25/M 升至 $2.50/M，但 cache read 仍 $0.25/M — **context 越長，cache miss 的邊際成本越高，caching 收益越大**。
4. **Placement 鐵律**：靜態大文件放 cache breakpoint *之前*，動態 query 放*之後*；Anthropic lookback window = 20 blocks，breakpoint 後異動不破壞前段。
5. `2601.06007`《Don't Break the Cache》🟡：500+ agentic session、10k token 系統提示實測 — 節省 41–80% 成本、TTFT 改善 13–31%；但 **naive full-context caching 可能反向劣化 latency**，動態內容必須置於 prompt 末端。

### A.3 Thinking / Reasoning Blocks 與 Caching 🟢

1. Thinking blocks **不能直接標 `cache_control`**，但作為多輪對話前輪內容會被連帶快取；從 cache 讀出計為 input tokens。
2. **`budget_tokens` / thinking 參數任何變更 → message-level cache miss**（system prompt 層不受影響）。Opus 4.7+ 已棄用 `budget_tokens`，改 `thinking: {type: "adaptive"}` + effort 控深度（傳 budget_tokens 返回 400）🟢。
3. **模型分代差異**：Opus 4.5+ / Sonnet 4.6+ 加入非 tool-result 用戶內容後 thinking blocks **保留**（cache 有效）；舊版及所有 Haiku **自動清除**（cache 失效）。
4. Extended thinking 任務官方建議 **1h TTL**（5min 可能在 thinking 完成前過期）。
5. 🟠 GitHub issue `anthropics/claude-code#20249`：舊文件曾誤載「thinking 永遠 strip」，Opus 4.5 實為 preserve，文件已更正 — **模型升代後行為會反轉，舊知識誤導 cache 設計**。

### A.4 Cache 作為生產健康指標（既有 BP28 整合）🟠

- `cache_hit_rate = cache_read_input_tokens / input_tokens`，是長跑 agentic 產品的 incident 級指標，**下降即觸發 incident**。
- 四層穩定前綴結構：`system + tools` > 專案檔 > session context > 對話訊息。
- 動態資訊用 `<system-reminder>` tag 經 messages 注入，**不污染 system prompt**。
- Mid-session 切換模型 = 全部 cache 失效（cache 是 model-specific）。Compact 必須使用**完全相同**的 system prompt + tools。

### A.5 既有材料對接
- `2510.04618` ACE 🟡：增量 delta playbook → 91.8% KV cache reuse、帳單成本 -82.6%；delta 結構與 cache reuse 天然相容。
- `2603.04814` Beyond Context Window 🟡：long-context 準確率高 33.4–35.2pp，但 ~10 turn 後 memory 成本更划算（20 turn 省 26%）— caching 改變這條 break-even 曲線（cache 讓 long-context 在更多 turn 下仍經濟）。

---

## Section B：Prompt Management — 缺口最大、ROI 最高

> 既有材料對此幾乎空白。以下為本報告新增的核心貢獻。

### B.1 Versioning / Registry / Governance 工具地景 🟢🟠

| 工具 | 版本機制 | 環境分離 | CI gate | rollback | 開源 | 現況 |
|---|---|---|---|---|---|---|
| **Langfuse** 🟢 | 遞增 version ID + 自訂 label | label（production/staging） | — | 重指派 label | ✅ 功能最完整開源 | 活躍 |
| **Braintrust** 🟠 | content-addressable（內容→ID） | dev/staging/prod | ✅ 唯一 GitHub Actions eval gate | 即時 | ❌ | 活躍 |
| **Helicone** 🟢 | 6 字元 prompt_id + environment | prod/staging/dev | — | UI（API 文件不全） | 部分 | 活躍 |
| **LangSmith** 🟠 | commit-hash 式 | — | — | — | ❌ managed-only | vendor lock-in 疑慮 |
| **PromptLayer** 🟠 | passive capture（每次 call 建版） | — | git-style | branch/review | Enterprise 限 | 活躍 |
| **MLflow 3.4** 🟠 | Model Registry 存 prompt | — | — | — | ✅ | 評估器少 |
| **Humanloop** 🟠 | reviewer/approve workflow | deployment vars | — | — | ❌ | **已 sunset 2025-09-08** |

**Prompt-as-Code 最佳實踐** 🟠：
- Prompt 存獨立 YAML/JSON 納入 Git，**不散落在應用碼**。
- Deploy webhook → `repository_dispatch` → GitHub Actions → 自動開 PR（`peter-evans/create-pull-request`）。
- Eval gate：分數低於門檻 `exit 1` 封鎖 merge（與 unit test 同級機制）。
- 已知缺口：Agenta / Prompt Flow 只能版本控制整個 application variant，**無法版本控制個別 prompt**。

### B.2 Prompt A/B Testing 框架 🟠🟢

1. **流量分配**：Canary（5% → variant B）或 Shadow（同 request 雙跑、用戶只看 control、variant 非同步 log）— shadow 是零用戶風險的離線比較。
2. **統計方法** 🟢：連續指標 → t-test；二元結果 → chi-square / two-proportion z-test。**早停是 false-positive 膨脹的頭號來源**，需累積 1–3 週樣本。
3. **三類指標**：Automated（LLM-as-judge：relevance/faithfulness）、Human（thumb、regeneration 等隱性信號）、Operational（latency / token cost）。
4. **Guardrail metrics**：主指標外必設防護指標，防未測維度退化；同一用戶全程同 variant 避免污染。

### B.3 Prompt Injection / 安全 🟢🟡

1. **OWASP LLM01 連續兩版排名第一** 🟢：根因是 LLM 在同一 channel 處理 instruction 與 data，無結構性隔離 → **無 100% 防禦，需 defense-in-depth**。
2. 管理層防禦：input validation + allowlist + anomaly detection；system prompt 隔離不信任外部內容；RBAC/ABAC 控管誰能改 prompt 配置；SIEM 監控；上線前 red-team + fuzz。
3. **RAG 擴大攻擊面** 🟡：外部知識庫成為 indirect injection 向量，傳統 sanitizer 不足（`2507.13169` Prompt Injection 2.0）。
4. **`2505.06311` InstructDetector**（已全文歸檔）🟡：transformer 中間層（Llama-3.1-8B 第 14 層）hidden states + gradients → MLP 分類器，於資料進 LLM 前過濾。**in-domain 99.60%、out-of-domain 96.90%、BIPIA 攻擊成功率降至 0.03%**，僅需 200 訓練樣本、跨語言/架構泛化。目前實測最強且工程可部署。
5. 補充防禦：`2510.08829` CommandSans（surgical sanitization 低誤殺）、`2510.05244` Minimizer-Sanitizer firewall（有限 privilege LLM 先 filter）🟡。

### B.4 Cross-Model Migration Playbook 🟠🟡

1. **三階段 Shadow Deployment** 🟠：Phase 1 並行執行（1–2 週，用戶只看舊模型）→ Phase 2 自動比對（語意相似度 + JSON 合規 + 行為差異分類）→ Phase 3 差異分桶（Improvement / Neutral / Regression / Novel）。
2. **格式偏好** 🟠：OpenAI 偏 markdown + delimiters；Claude 偏 XML tags；Gemini 偏 constraints-first。核心原則 **re-express ≠ translate**（抽 intent 用目標慣例重寫，不做 find-replace）。
3. **Hardest cases first** 🟠：舊模型上迭代最多次的 prompt 遷移後最易崩，優先測；embedding index 須完整重建（向量空間不相容）。
4. **`2512.01420` PromptBridge**（已全文歸檔，PDF 第 1 頁親驗）🟡：提出 **Model Drifting** 現象（prompt 跨模型重用嚴重劣化）；MAP-RPE 兩階段 — calibration（少量 alignment pair 學 source/target 映射）+ transfer（test-time 直接轉，無需 per-task 重優化），**training-free**。轉移到 o3 時相對 direct transfer：**SWE-Bench +27.39%、Terminal-Bench +39.44%**（原文 abstract 數字）。作者 UC Santa Cruz × Accenture Center for Advanced AI。
5. **反模式** 🟠：避免建跨 provider 的「prompt normalization layer」— model-specific prompt 持續優於 generic，abstraction 的可移植性以效能為代價。

---

## Section C：Prompt Engineering — 隨模型能力反轉

### C.1 Non-GPT / Non-math 驗證：Prompting Inversion 在 Claude 成立 🟢

既有 `2510.22251` 只測 GPT + GSM8K（gpt-5 上 constrained CoT 反轉 -2.36%）。本報告以 Anthropic 官方一手補齊外部效度：

1. **字面化成立**：Opus 4.8 低 effort 下嚴格字面解讀，*不靜默泛化*（官方原文 "It does not silently generalize an instruction from one item to another."）。修正：明確寫 scope（"Apply to every section, not just the first."）。**機制是 effort 參數，不是 token budget 壓縮**。
2. **Effort > Prompt**："Effort is likely to be more important for this model than for any prior Opus." → **shallow reasoning 先升 effort（high/xhigh），再考慮 prompt 補丁**。
3. Adaptive Thinking 取代 budget_tokens；Opus 4.8 預設 effort = `high`（4.7 為 `medium`）。
4. **Positive > Negative 官方驗證**："Positive examples ... tend to be more effective than negative examples or instructions that tell the model what not to do."（直引）— 與本 harness output-discipline.md「正向指令優先」一致。
5. **Gemini** 🟢：PTCF 框架（Persona·Task·Context·Format）；官方「always include few-shot」；Gemini 3 強建議 temperature=1.0（低於會異常）。

### C.2 Structured Outputs / Tool-use Forcing 🟢🟠

1. **Anthropic Native Structured Outputs（GA）**：beta header `structured-outputs-2025-11-13` + `output_format: {type: "json_schema"}`，grammar-constrained decoding，**保證格式合規但不保證內容正確**。
2. **已知陷阱**：Anthropic SDK 靜默把 `minimum/maximum/minLength/pattern` 移到 description，validate 失敗才重試。
3. `tool_choice: "any"` 比 `"auto"` 省 ~33 tokens；tool description 越短越省。
4. **JSON mode 已過時**：constrained decoding 上線後，舊式「prompt 求 JSON 並祈禱」成 footnote。
5. 固定 schema pipeline 應 cache schema，避免每次重傳計費（與 Section A 對接）。

### C.3 RAG + Prompting 整合 🟡🟠

1. **Lost-in-the-Middle 量化** 🟡：U 型注意力，相關資訊移至中間效能降 >30%；解法 — 重要文件放開頭/結尾，**零成本大幅提升**。
2. **Chunk size 依領域**：專利 1,000–1,500 tokens；對話記錄 200–400；無普遍最優。
3. **Dynamic k**（`2512.14313`）：動態預測最優文件數優於固定 k；k 太多引入 distractor，太少召回不足。
4. **Contrastive ICL-RAG**（`2501.07391` ACL 2025，已全文歸檔）🟡：prompt 中同提供正確 + 對比反例，助模型區分相關/無關 context。
5. **Context Quality > Model Optimization**："RAG is only as good as the context it can see" — ungoverned / stale context 無法靠模型優化補救。

### C.4 Agentic Prompt Regression Testing 🟢🟡

1. **"Better Prompts Hurt" 量化**（`2601.22025`，已全文歸檔）🟡：泛用 prompt 取代 task-specific → extraction pass rate 100%→90%、RAG compliance 93.3%→80%（Llama 3）。結論：**context-specific evaluation 必須先於 prompt 修改，不存在普遍最優 prompt**。直接呼應本 harness §R9（Tests Verify Intent）。
2. **MVES（Minimum Viable Evaluation Suite）**：分三類（一般 / RAG / Agentic tool-use）；成本分層 — cheap deterministic checks → heuristic → LLM-as-judge 最後才用。
3. **LLM-as-Judge + rubric**：工具鏈/多輪推理難字串比對，judge + rubric 才有效（promptfoo `llm-rubric` 自動 pass/fail）。
4. **Prompt-as-Code Regression CI**：promptfoo GitHub Action 在 PR 跑 eval、生成 before/after、regression 即 build fail（與 unit test 同級）。
5. **Agentic eval 雙層**：須同時評「最終答案正確」與「中間推理步驟合理」。

---

## 跨主題綜合：Prompt 生命週期流水線

```
[設計] Engineering          [部署] Management           [執行] Caching
 effort 旋鈕優先      →    版本入 Git + label      →   穩定前綴 + breakpoint
 positive>negative        eval gate (CI)              cache_hit_rate 監控
 structured output        A/B (shadow/canary)        TTL 配 use-case
 RAG: 重要放頭尾          注入防禦 (InstructDetector)  mid-session 不切模型
 eval-driven 迭代         cross-model: re-express     thinking 用 1h TTL
       │                        │                          │
       └──────────── 三者皆以「靜態優先、動態末端」為共同原則 ───────────┘
```

**唯一最重要的單一原則**：**靜態前綴穩定**同時是 caching 的省錢機制（A.4）、management 的版本可追溯基礎（B.1）、engineering 的字面化可預測前提（C.1）。三主題在此交會。

---

## 仍待研究的方向（誠實標注）

1. Prompting-inversion 在 Claude 上**僅有官方定性說法**，缺 GSM8K 等 benchmark 的量化反轉曲線（GPT 有，Claude 無）。
2. Caching + memory（ACE delta）+ long-context 三者的**聯合成本模型**尚無單一論文涵蓋。
3. InstructDetector 等 hidden-state 防禦對**閉源 API 模型**（無法取 hidden states）不適用，API-only 場景的最強 indirect-injection 防禦仍開放。
4. `2501.07391` arXiv 版為 2 頁短摘要，完整 RAG best-practice 數字需查 ACL 2025 proceedings 全文。

---

## 來源清單

**既有材料（build on）**：
- `papers/2026-01-31-dont-break-cache-prompt-caching-2601-06007.md`
- `papers/2025-10-06-agentic-context-engineering-2510-04618.md`
- `papers/2025-10-25-prompting-inversion-2510-22251.md`
- `papers/2025-08-01-rcr-router-role-aware-context-routing-2508.04903.md`
- `papers/2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md`
- `best-practices/05-claude-prompting-best-practices.md`
- `best-practices/08-prompt-caching.md`
- `best-practices/28-thariq-prompt-caching-lessons.md`

**本次新收全文論文（research/papers/，PDF + md）**：
- `2026-01-29-when-better-prompts-hurt-eval-driven-2601-22025`（MVES / eval-driven）
- `2025-05-08-indirect-prompt-injection-defense-2505-06311`（InstructDetector）
- `2025-12-01-promptbridge-cross-model-prompt-transfer-2512-01420`（cross-model）
- `2025-01-13-rag-best-practices-acl2025-2501-07391`（ACL 2025 RAG）

**官方一手 docs**：Anthropic Pricing / Prompt Caching / Extended Thinking / Prompting Best Practices / What's New Opus 4.8；OpenAI Prompt Caching + Structured Outputs；Google Gemini Pricing + Prompting Strategies + implicit caching blog。

**社群二手（明標）**：Braintrust / Langfuse / Helicone / Nearform / ZenML / Agenta / Traceloop / Statsig / TianPan.co migration playbook；GitHub `anthropics/claude-code#20249`；OWASP LLM Top 10 2025（CSA）。
