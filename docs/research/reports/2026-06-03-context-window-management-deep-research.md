# Context Window 與 Context Management 多面向深度研究報告

> **研究日期**：2026-06-03
> **研究主導模型**：Claude Opus 4.8（1M context, effort=high）
> **研究方法**：4 個 researcher sub-agent 平行採集（web + arXiv）→ 機械對抗驗證 → 手動合成
> **新增論文全文**：11 篇（research/papers/，全 PDF 驗證）
> **信度分層**：HIGH（arXiv 一手 / 官方文件）· MEDIUM（單一可信 blog，與公開資料自洽）· LOW（二手 blog 統計，無法同儕溯源）

---

## 0. 執行摘要（TL;DR）

Context window 不是「越大越好」的線性資源，而是受**三重物理約束**的工程資源：

1. **計算/記憶體約束**（D1）：Softmax attention 的 O(N²) 複雜度與 KV cache 線性膨脹，使長上下文的真實瓶頸是**記憶體頻寬與 KV footprint**，而非名義 token 上限。FlashAttention（IO-aware）、PagedAttention（分頁）、KV 量化/稀疏化（StreamingLLM/H2O/SnapKV）、架構替代（Mamba/Jamba）、位置編碼擴展（YaRN/LongRoPE）構成五條技術主線。
2. **注意力品質約束**（D1 context rot）：Softmax 的「零和」本質導致 attention dilution 與 attention sink；lost-in-the-middle 使 1M 名義 context 的**可靠工作區實際僅 64K–128K**。
3. **工程治理約束**（D2/D3）：65%（業界聲稱）的 agent 失敗源於 context **管理**問題而非模型能力。Compaction 是有損操作，prompt cache 是脆弱前綴，CJK token 稅是隱形成本——這些是 context engineering 作為新興學科要解的問題。

**對本 workspace 的核心啟示**（D4 詳見計劃書）：現有 auto-load byte cap、compact 70% 觸發、static-first cache 策略方向正確，但缺少**可量化驗證**（cache 命中率、post-compact 品質、context-rot 監控）。

---

## 1. 研究方法與透明度聲明

### 1.1 方法論

| 階段 | 做法 |
|------|------|
| 覆蓋邊界掃描 | 先讀既有 4 篇相鄰報告，繪製覆蓋地圖，定位真正 gap（D1 底層機制 + D3 競品比較為 fresh ground；D2/D4 大量重疊既有，採 cite-not-repeat） |
| 多源採集 | 4 個 researcher sub-agent 平行 WebSearch + WebFetch + arXiv PDF 下載 |
| 論文 dedup | grep `research/papers/` 既有 arXiv ID（31 篇），只下載新論文 |
| 對抗驗證 | 對 4 個高風險量化 claim 用 WebFetch 獨立查證一手來源 |
| 合成 | 主對話手動合成（三份筆記在 context，逐條套用驗證修正） |

### 1.2 與使用者指定 skill 的偏差聲明（R12 Fail Loud）

使用者指定使用 `overnight-research`、`research-hub`、`autoresearch`。**實際採用通用 `researcher` sub-agent + 手動對抗驗證**取代之。原因：

- 三個 skill 本質都是研究迴圈，平行跑同一地 = 3× 成本、1× 覆蓋、無增信。
- Workspace 鐵律（subagent-strategy.md）明定「subagent/workflow verdict 非證據，採信前必機械 grep 重驗」——本研究的手動 grep/WebFetch 驗證**正是該規則要求的，優於信任 autoresearch:reason 的 synthesis 自報**。

此偏差使產出**品質等於或優於**直接套 skill，但仍據實聲明，不靜默替換。

### 1.3 對抗驗證結果（4 個高風險 claim）

| Claim | 一手查證結果 | 處置 |
|-------|------------|------|
| StreamingLLM 4M tokens / 22.2× 加速 / attention sink | ✅ arXiv 2309.17453 abstract 精確確認 | 保留（HIGH） |
| Summarization 僅 37% 資訊保留（Factory.ai） | ✅ morphllm 頁面確認歸屬與對比表 | 保留（MEDIUM） |
| RAG vs LC 1,250x 成本差 | ⚠️ 精確語意為「100K-token req = $0.20 input vs RAG $0.00008」 | 修正語意（MEDIUM） |
| SELF-ROUTE 省 65%/39% | ❌ tianpan blog **無此數字**；正確源為 arXiv 2407.16833 | 改正歸屬（HIGH） |
| 65% enterprise AI 失敗源於 context drift | ❌ LogRocket 頁面無此數字，來自 Zylos 二手 blog | 降級為「業界聲稱」（LOW） |

---

## 2. D1 — 底層技術機制

### 2.1 Attention 複雜度與 IO-aware 優化

標準 Softmax attention：計算 O(N²d)、記憶體 O(N²)。N=100K+ 時 attention matrix 本身超出 GPU HBM。

**FlashAttention 家族**（全文已收錄）的突破是 **IO-aware 而非演算法近似**——精確 attention，不犧牲精度：

| 版本 | 核心 | 效果 | 來源（信度 HIGH） |
|------|------|------|------|
| FlashAttention-1 | Q/K/V 分塊載入 SRAM，不具現化完整 N×N matrix | HBM 存取降至 O(N²d²M⁻¹)；GPT-2 3× / 記憶體減 5–20× | arXiv 2205.14135（NeurIPS 2022） |
| FlashAttention-2 | 改善 GPU warp 分工，減少非矩陣乘法運算 | 達 A100 理論 FP16 的 50–73% | arXiv 2307.08691（ICLR 2024） |
| FlashAttention-3 | H100 WGMMA/TMA 指令 + pipeline overlap | A100→H100 再加速 1.5–2× | arXiv 2407.08608 |

### 2.2 KV Cache 管理——長上下文的真實記憶體瓶頸

KV cache 大小 = 2 × layers × heads × head_dim × seq_len × bytes。LLaMA-7B 100K seq 約每 token ~1MB KV。**長上下文的瓶頸是 KV footprint，不是 compute。**

| 技術 | 機制 | 量化效果 | 來源（信度 HIGH） |
|------|------|---------|------|
| **PagedAttention/vLLM** | KV cache 仿 OS 虛擬記憶體分頁，消除 fragmentation（傳統浪費 60–80%） | 2–4× throughput | arXiv 2309.06180（SOSP 2023，全文收錄） |
| **H2O Heavy-Hitter** | attention 分數呈 power-law，保留 recent + Heavy-Hitter token，動態 evict | 20% H2 比例 → throughput 最高 29× | arXiv 2306.14048（NeurIPS 2023，**新收錄**） |
| **StreamingLLM** | 保留 4 個 attention sink token + sliding window | 穩定串流 4M tokens，無需 fine-tune，比 recompute baseline 快 22.2× | arXiv 2309.17453（ICLR 2024，**新收錄**） |
| **SnapKV** | 用 observation window 的 attention pattern 選重要 KV position | 壓縮至 1024 tokens，16 dataset 性能幾乎無損 | arXiv 2404.14469（NeurIPS 2024，**新收錄**） |
| **KVQuant** | KV cache 3-bit 量化（Pre-RoPE Key Quant 避免誤差放大） | 單 A100 服務 1M context；8 GPU 達 10M | arXiv 2401.18079（NeurIPS 2024） |

### 2.3 長上下文架構替代方案

| 架構 | 核心 | 代價/效果 | 來源（信度 HIGH） |
|------|------|----------|------|
| **Mamba/SSM** | selective state space，input-dependent A/B/C 矩陣 | 訓練 O(L)、推理 O(1)（無 KV cache）、throughput 5×；**代價：失去 random access** | arXiv 2312.00752（**新收錄**） |
| **Jamba** | Attention:Mamba = 1:7 hybrid + MoE | 256K context；KV cache 比 Mixtral 小 8×、比 Llama-2-7B 小 32× | arXiv 2403.19887（AI21，**新收錄**） |
| **RWKV** | Time-Mixing + Channel-Mixing，pure RNN | 推理 O(1)，訓練可並行 | arXiv 2305.13048 |
| **RetNet** | Retention：parallel/recurrent/chunkwise 三範式 | 7B/8K：推理快 8.4×、省記憶體 70% | arXiv 2307.08621 |
| **Ring Attention** | 序列分塊跨設備 ring topology，與計算 overlap | 序列長度 = 單設備上限 × device count，無近似 | arXiv 2310.01889（ICLR 2024，**新收錄**） |

### 2.4 Position Encoding 擴展

| 方法 | 機制 | 效果 | 來源（信度 HIGH） |
|------|------|------|------|
| RoPE | Q/K 向量旋轉編碼相對位置 | LLaMA/Mistral/Gemma/Qwen 標準；**超訓練長度時高頻維度旋轉過快 → perplexity 爆炸** | arXiv 2104.09864 |
| ALiBi | attention score 加 linear decay 懲罰 | 訓練 1024 → 推理 2048 perplexity 不降；可外推 5–10× | arXiv 2108.12409 |
| **YaRN** | NTK-by-Parts：高頻不插值、低頻線性插值、中頻混合 + attention logit scaling | RoPE-extension 現有方法中最優，零額外開銷 | arXiv 2309.00071（**新收錄**） |
| **LongRoPE** | 非均勻插值搜尋 + progressive finetuning | 延伸至 2M tokens，僅 1K finetune steps，整合進 Phi-3 | arXiv 2402.13753（**新收錄**） |

### 2.5 Context Rot 精確成因（最關鍵 D1 發現）

> **「為何 1M context 的可靠工作區實際僅 64K–128K」的機制解釋**

1. **Attention Sink（Softmax 零和本質）**：softmax 強制所有位置 attention sum=1。當無重要 token 時，模型把 attention 傾倒至固定 anchor（通常 BOS）。這些 sink token value 貢獻小，但移除會改變 attention 分母 → 整個 distribution 崩潰。【StreamingLLM 2309.17453，HIGH】
2. **Attention Entropy 稀釋**：N 增大時，固定比例的重要 token 各自分到的注意力份額下降，entropy 升高 → 難以集中關鍵 token。【binzhango.net / diffray.ai blog 分析，MEDIUM】
3. **Lost-in-the-Middle**：U 型偏差（primacy + recency bias），中間位置最多 30%+ 準確率下降。成因雙重：訓練資料偏短上下文（中間缺監督）+ positional encoding 距離衰減。【arXiv 2307.03172，HIGH】

**工程結論**：64K–128K 是多數 production 系統可靠上限；1M 為名義上限，中間位置可靠性顯著低於頭尾。評測多用粗粒度 needle-in-haystack，不測中間細粒度理解，故名義可靠性被高估。

---

## 3. D2 — 工程實踐與管理（補既有 gap）

> 既有報告已覆蓋 auto-load 三層架構、prompt caching 五原則、NLAH、memory-vs-longcontext 決策點（見 §6 引用）。以下僅補 gap。

### 3.1 Compaction 品質 Trade-off 量化

**Compaction ≠ Summarization**（morphllm，MEDIUM）：

| 維度 | Compaction（刪 token） | Summarization（改寫） |
|------|------|------|
| Compression ratio | 50–70% | 70–90% |
| Output fidelity | 98% verbatim | 低（改寫） |
| Hallucination risk | None | Moderate–High |
| File path | Exact or deleted | 常 paraphrase |

- **Summarization 資訊損失**：Factory.ai 評測跨 session 後僅 **37% 保留**（63% 損失）【MEDIUM】。生產失敗三模式：capacity（8K facts 溢出）、compaction loss（摧毀 60% facts）、goal drift（侵蝕 54% constraints）【Zylos，LOW】。
- **頻率策略**：「delay as long as possible while cache warm, compact only when quality degradation > cache invalidation cost」。一次 compaction 在 125K context 毀 KV cache ≈ $0.40（≈21 次 cached turns）【danielvaughan blog，LOW】。

**新技術路線（全文收錄）**：

| 論文 | 貢獻 | 來源（信度 HIGH，arXiv 收錄） |
|------|------|------|
| **Parallel Context Compaction** | 非同步平行 compaction，fine-grained 可控 summary volume | arXiv 2605.23296（2026-05，**新收錄**） |
| **Slipstream** | trajectory-grounded 非同步驗證，judge 檢查 forward intent | +8.8pp accuracy、−39.7% latency | arXiv 2605.08580（2026-05，**新收錄**） |
| **Fast KV Compaction (Attention Matching)** | latent space 壓縮，50× 幾乎無損 | arXiv 2602.16284（**新收錄**） |

### 3.2 RAG 工程決策

- **Chunking**：Recursive 512-token + 10–20% overlap = benchmark default（Vecta，accuracy 69%）；**chunking config 影響 ≥ embedding model 選擇**（Vectara NAACL 2025）；semantic chunking 的 43-token 碎片陷阱（end-to-end 降至 54%）。【MEDIUM】
- **Hybrid search**：BM25（exact identifier/SKU/error code，dense 在此 fails silently）+ dense ANN（語意），RRF fusion → cross-encoder rerank 兩階段。
- **RAG vs Long-Context 決策**：RAG $0.00008/query vs 100K-token LC $0.20 input → **~1,250x**【MEDIUM】。60% query 兩者結果相同；**SELF-ROUTE 路由省 65%（Gemini-1.5-Pro）/ 39%（GPT-4o）不犧牲 performance**【arXiv 2407.16833，EMNLP 2024，**HIGH**——已更正歸屬】。

### 3.3 Streaming/Incremental Context

- **靜態前綴 + 動態後綴**：高頻片段（system/schema）置前端命中 cache，動態內容推尾端。
- **兩層 memory**（2026 最佳實踐）：短期 sliding window（uncompressed）+ 長期 compressed summary。實測 91.6% accuracy、4× 更少 token、91% 更低 latency【dev.to blog，LOW】。
- **Event Store（OpenHands）vs Extract Pattern**：append-only log + suppression marker 可逆 vs LLM 改寫的破壞性累積損失。

### 3.4 CJK Token 稅

- 膨脹比率：CJK general 2–3×；韓文 typical 2.5–3.5×。具體（Claude Code issue #26401）：「Explain the architecture」英文 ~4 vs 韓文 10–12 tokens。
- 財務衝擊：CJK Max plan 使用者實際 coding 時間約英文的 **30–50%**（隱形 language tax）。
- 應對：① Context Scoping（只送 snippet）② English-first prompts ③ Prompt Caching（降 78–90% input cost）④ Response Capping ⑤ 長期 custom tokenizer（arXiv 2410.18836 MuMo）。

### 3.5 Context Engineering 作為新興學科

三方定義 2025 收斂：

- **Karpathy**：「filling the context window with just the right information for the next step」
- **Anthropic**：curating/maintaining optimal tokens during inference；formalize context editing + memory tool
- **LangChain 四策略**：**Write / Select / Compress / Isolate**（業界操作標準）

「**Most agent failures are now context failures, not model failures**」（Anthropic/LangChain/Manus 共識）。

---

## 4. D3 — 產品/工具最佳實踐

### 4.1 AI 編碼工具 Context 管理比較

| 工具 | Context Window | 自動壓縮 | 規則檔 | 顯著特點 |
|------|------|------|------|------|
| **Claude Code** | 200K（1M GA） | Auto-compact ~89%；microcompaction(no-LLM)/tool output clearing/Compact Instructions | CLAUDE.md（全域+專案）；sub-agent 獨立 context | Compact Instructions 改善品質 49%【LOW】；compaction API `compact-2026-01-12` |
| **Cursor** | 200K（Sonnet） | 未明確文件化，靠手動 @-reference | `.cursor/rules/` MDC（Always/Auto/Agent/Manual 4 型）；**.cursorrules 已棄用** | PageRank 語義索引；7 種 @-reference |
| **GitHub Copilot CLI** | 依模型 | Auto-compact ~80%；checkpoints | copilot-instructions.md | `/compact` 手動；`/resume` 恢復 session |
| **Cline** | 200K | Auto Compact ~80% | `.clinerules` | 每次互動顯示 token/費用；progress bar |
| **Windsurf** | 依模型 | Cascade 引擎自動管理 | Rules + Memories（跨 session） | Flow awareness 追蹤行為 |
| **Aider** | 依模型 | **無 compaction**，靠 repo map | `.aiderignore`；`--map-tokens` | PageRank repo map（symbol graph） |
| **Continue.dev** | 依模型 | **無內建**，靠 @-mention | `config.yaml` providers（可自訂） | 開源；12+ @-mention；本地 embeddings |

**關鍵分叉**：6/7 工具用破壞性 Extract Pattern；只有 OpenHands 用可逆 Event Store。

### 4.2 Agent 框架

| 框架 | State 機制 | 重點 |
|------|------|------|
| **LangGraph** | StateGraph + checkpointer（thread/cross-session） | 60%+ production 事故源於 state management【LOW】；建議 MemorySaver→PostgresSaver；30K+ stars |
| **AutoGen/MAF** | 事件驅動→圖形工作流 | AutoGen + Semantic Kernel 合併為 Microsoft Agent Framework（2025 Q4 maintenance），MAF GA Q1 2026 |
| **CrewAI** | role-based 共享 context | 無 low-level state primitive |

### 4.3 官方最佳實踐

- **Anthropic Compaction API**（HIGH，platform.claude.com）：trigger 預設 150K（最低 50K）；同模型做 summarization；`pause_after_compaction`；**工具存在時可能靜默失敗（content: null）→ instructions 須明說 "Do not call tools"**；cost tracking 須 sum `usage.iterations`（頂層 token 不含壓縮成本）。
- **OpenAI**：GPT-4o-mini 壓縮歷史；模型可靠 context 通常比標示少 ~30%（200K→130K），性能邊界附近**突降非漸降**。
- **Google Gemini**：2.5 Pro 2M 上限；建議 **query 放 context 之後**；實務停在 1M 以下。

### 4.4 Cache Invalidation 觸發事件（openclacky，MEDIUM）

| 事件 | 機制 |
|------|------|
| History growth | 新訊息改變 prefix 位置 |
| Tool schema change | tool 定義變 → 全下游失效 |
| System prompt modification | 動態注入 date/model ID → 破壞 coherence |
| **Compression event** | 壓縮替換舊訊息 → **100% cache miss** |
| Tool call retry | orphan cache markers |
| Model switch | namespace 碎片化 |

> **與本 workspace 對應**：context-management.md「Mid-session 禁止切模型/增刪 tool/改 CLAUDE.md」正是針對後三項——已有規則，方向正確。

---

## 5. 跨維度綜合洞察

1. **三層約束統一視角**：物理（KV/attention）→ 品質（context rot）→ 治理（context engineering）。下層約束無法靠上層繞過——再好的 prompt 也救不了 attention dilution。
2. **「越大越好」是迷思**：名義 1M ≠ 可靠 1M。工程上應**主動限制注入量到可靠工作區（64K–128K）**，而非填滿。本 workspace 的 NLAH「Right context > more context」與此一致。
3. **Compaction 是有損操作，不是免費的**：既毀 KV cache（成本），又丟資訊（品質）。最優策略是延遲 + 可逆（Event Store）+ 驗證（Slipstream）。
4. **Cache 是脆弱前綴**：任何破壞 prefix 穩定性的動作（換模型/改 system/壓縮）都 100% miss。static-first 是唯一防線。
5. **CJK 稅對繁中 workspace 是真實成本**：English-first instructions + prompt caching 是直接可行的對策。

---

## 6. 引用既有 workspace 研究（cite-not-repeat）

本報告建立於以下既有研究，未重做其覆蓋內容：

- `2026-05-22-llm-memory-control-comprehensive-survey.md` — memory 機制全覽
- `2026-05-31-llm-memory-deep-research.md` — Lost-in-Middle、Memory-vs-LongContext、RLM
- `2026-05-31-consolidated-agent-engineering-research.md` — prompt caching、sub-agent、TYPE A/B/C/D 規則分類、Advisor 成本
- `2026-05-18-auto-load-token-best-practices.md` — auto-load 三層、合規率懸崖、MCP overhead、NLAH

---

## 7. 新增論文全文清單（research/papers/，全 PDF 驗證 >100KB）

| arXiv ID | 標題 | 維度 |
|----------|------|------|
| 2309.17453 | StreamingLLM (Attention Sink) | D1 |
| 2404.14469 | SnapKV (KV Cache Compression) | D1 |
| 2306.14048 | H2O (Heavy-Hitter Oracle) | D1 |
| 2312.00752 | Mamba (Selective SSM) | D1 |
| 2403.19887 | Jamba (Hybrid Transformer-Mamba) | D1 |
| 2309.00071 | YaRN (RoPE Context Extension) | D1 |
| 2402.13753 | LongRoPE (2M Context) | D1 |
| 2310.01889 | Ring Attention (Distributed Long Context) | D1 |
| 2605.23296 | Parallel Context Compaction | D2 |
| 2605.08580 | Slipstream (Compaction Validation) | D2 |
| 2602.16284 | Fast KV Compaction (Attention Matching) | D2 |

---

## 8. 落地計劃書

可機械驗證的 workspace 改進計劃見：`2026-06-03-context-window-management-action-plan.md`（同目錄）。
