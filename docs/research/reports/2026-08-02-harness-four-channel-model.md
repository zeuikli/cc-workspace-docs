# Harness 四通道模型 — 薄 harness 辯證、loop/goal/graph 統一、單人 vs 團隊 harness

> **日期**：2026-08-02 · **分支**：`claude/research-papers-summary-update-796fqe`
> **起點**：使用者用過 v5.1 後提問「薄 harness 是不是趨勢？過度的 harness 對 LLM 不一定是好事」，並自陳「寫了五個版本 harness 仍有疑問」。
> **證據基底**：`research/papers/` 306 篇（2020–2026）。三方模型（Fable 5 / Opus 5 / Sonnet 5）獨立作答 + 主對話合成。
> **落地 commit**：`2d63141`（P0）· `814f341`（P1）· `304a0a6`（P2）· `4a0304c`（殘留補掃）
> **驗證收據**：`healthcheck` PASS 193 / WARN 0 / FAIL 0；`check-references` dangling=0 orphan=0；`check-enforcement` OK；auto-load 10,894 B（門檻 ≤20,400）。

---

## 0. 三個問題與三個答案（摘要）

| 問題 | 答案 | 信心 |
|---|---|---|
| 薄 harness 是趨勢嗎？ | **不是**。趨勢是 harness 一級化。「薄」在文獻中有四種含義，其中兩種有證據、兩種被反對 | 高 |
| loop / goal / graph 怎麼合？ | 不是三件事。**Loop = 退化的 Graph**（節點恆 1、邊隱含），**goal 是兩軸共同威脅的不變式**。最小實作是寫下依賴邊，不是換引擎 | 中高 |
| 單人 harness 與團隊 harness 差在哪？ | 只差一個 **principal 模型**（授權／優先權／可見範圍）。但**單人 ≠ 單 principal 邊界**——context 不流動處是 **agency cost 集中地**（⚠️ 初版誤稱其為 principal，經複審推翻，見 §C.2；residual claimant 始終是人） | 中 |

---

## 1. 「薄 harness」的四種含義（Fable 5 主導，主對話複核）

corpus 內**沒有任何一篇**主張 harness 應整體縮減。67 篇 Harness Engineering 幾乎全集中在 2026，`research/papers/2026-06-14-survey-agent-system-harness-design-2606-20683.md` 的四範式演進（prompt → workflow/context → harness engineering → agent-native co-evolution）方向是**深化**而非退場。

因此「薄 harness 是趨勢」這個一般化陳述不成立。真正有跨論文收斂證據的是一個窄命題：**harness 的 LLM 面該薄、確定性面該厚**。

| 「薄」的含義 | 證據方向 | 代表證據 | 強度 |
|---|---|---|---|
| ① **Context 面薄**（少餵、剪枝、壓縮） | 支持 | `2026-06-08-less-context-better-agents-2606-10209.md`：pruning+summarization 91.6% vs full-history 71.0%、token −64%；`2026-06-22-self-compacting-language-model-agents-2606-23525.md`：結構感知壓縮同時升質降本 30–70% | 高 |
| ② **程序指導/編排面薄**（partial > full workflow） | 支持 | `2026-05-15-harnesses-inference-time-alignment-trajectories-2605-21516.md`：僅規範初始步驟優於全結構化；over-decomposition 為具名失敗模式。`2026-03-26-natural-language-agent-harnesses-nlah.md` Table 3：加 Verifier 模組反而 −0.8 ~ −8.4 | 中 |
| ③ **閘門/治理面薄** | **反對** | `2026-07-09-from-prompts-to-contracts-harness-engineering-2607-08028.md`：prompt-only 允許違規、code-level enforcement 120/120；`2026-04-18-caaf-harness-as-asset-determinism-2604-17025.md` ablation：三支柱缺一不可 | 高 |
| ④ **模型變強 → scaffold 自然萎縮** | **反對／未量化** | `2026-06-24-interplay-harness-design-post-training-2606-25447.md`：minimal harness 在工具環境偏移下顯著退化；`2026-08-01-stop-comparing-agents-without-disclosing-harness-2605-23950.md`：harness 變異常大於模型變異。支持面在 corpus 內未量化 | 低（支持面） |

**使用者的體感落在 ①②**——與證據同向。v5.1 也動到了 ③，那是文獻明確警告不該跟著薄的區塊。

### 1.1 代價的不對稱性（Opus 5）

放鬆 harness 的代價**不對稱**：
- **可觀測的**（摩擦、常駐 token、儀式感）立即消失
- **不可觀測的**（漂移抵抗力、閘門有效性、預算有界性）延遲數週才顯現

且 `2026-06-22-self-compacting-language-model-agents-2606-23525.md` 證明存在 **meta-cognitive gap**：unprompted 的模型無法可靠判斷自己的 context 何時開始腐化。

> **推論**：「精簡後跑了一天沒出事」與「精簡是對的」之間**沒有推論關係**。那正是延遲性失效的預期外觀。

延遲性失效的四條獨立證據鏈：

1. **定義上就是漸進的**——`2025-05-05-evaluating-goal-drift-language-model-agents-2505-02709.md`：drift「可以是逐漸的，只造成細微的行為變化」，最佳 agent 撐過 >100,000 tokens 才顯現。
2. **模型偵測不到自己的劣化**——同上 meta-cognitive gap。
3. **退化比改善更難預見**——`2026-04-30-ahe-observability-driven-harness-2604-25850.md`：即使有完整軌跡歸因基建，fix precision 33.7%（5× 隨機）而 **regression precision 僅 11.8%（2× 隨機）**。
4. **訊號是變異度不是分數**——`2025-05-09-llms-get-lost-multi-turn-2505-06120.md`：多輪退化中 aptitude 只掉 16%，**unreliability 漲 112%**；額外 reasoning token 無保護作用。

### 1.2 一個方法論警告（Opus 5，適用於本 workspace 自身）

本 workspace 慣用 `healthcheck PASS n / WARN 0 / FAIL 0` 當收據。該數字證明的是 **harness 自身的結構完整性**，不是**行為等價性**。`2026-07-05-measuring-harness-induced-belief-divergence-2607-04528.md` 指出：限縮驗證檢查、過濾證據這類 harness 變動，常在**完成率不變的情況下改變 agent 的內在推理**（風險評估、可回復性判斷、下一步選擇）。

> v5.1 報告在修辭上把「結構完整」當成了「行為未變」的證據。本報告同樣受此限制——所有收據皆為結構級，無行為等價性證明。

---

## 2. Harness 通道模型（本 session 的核心產出；初版四通道，經複審增為五）

harness 不是單一物件，是四條**成本曲線完全不同**的通道。混談這四者，是「該厚該薄」這個問題長期無解的原因。

| 通道 | 載體 | 成本結構 | 效益曲線 | 該厚該薄 |
|---|---|---|---|---|
| ① **常駐框架** | `CLAUDE.md` + auto-load rules | 每 session 固定付，**用不用都付** | 快速飽和（right context > more context） | **薄** |
| ② **按需知識** | `refs/`、`skills/*/references/` | **讀才付**，不讀為零 | 深度隨需求展開 | **厚是免費的** |
| ③ **確定性閘門** | `hooks/`、`scripts/` | 不觸發時 ~0；**觸發時付 belief divergence**（見 §2.3 訂正） | 與模型服從**無關** | **厚且便宜（但成本不是 bytes）** |
| ④ **路由** | `description` + `RESOLVER` + BM25 | 常駐（屬①），成本隨**數量**非體積 | **決定 ② 能不能被用到** | **要準** |
| ⑤ **持久記憶／run 證據** | `memory/`、telemetry log | 寫入時付、跨 session 複利、**會腐化** | 唯一「模型寫、模型讀」的通道 | **要有，但需防自我污染**（見 §2.3） |

### 2.1 本 workspace 實測（2026-08-02）

```
① auto-load        10,894 B   ← 歷來治理焦點
④ description      13,989 B   ← 比 ① 大 28%，27 項（17 skills + 10 agents）
② skills           1,468 KB   ← 常駐成本 0
③ hooks              216 KB   ← context 成本 0
```

重測命令：
```bash
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline}.md | tail -1
python3 - <<'PY'
import re,glob
tot=0
for f in glob.glob('.claude/skills/*/SKILL.md')+glob.glob('.claude/agents/*.md'):
    if f.endswith('INDEX.md'): continue
    m=re.search(r'^description:\s*(.+?)(?=\n[a-z-]+:|\n---)',open(f,encoding='utf-8').read(),re.S|re.M)
    if m: tot+=len(m.group(1).encode())
print(tot)
PY
```

### 2.2 三個推論

1. **「skills 太大」是假問題**。② 的 1.4 MB 對常駐成本貢獻為零。只要 ④ 命中，② 越厚越好。
2. **④ 壞掉時，② 全部變成死重**。這是唯一會讓 ② 的「免費」失效的機制。
3. **壓縮 description 省常駐是錯的優化方向**。`.claude/rules/prompt-lifecycle.md` 已實測分佈是平的（前 12 大僅佔 39%、中位數 411 B、無離群值），逐檔壓字要動到全部 27 項才有量級效果，而那正好傷 ④。要縮只能縮**數量**。

### 2.3 Fable 5 對本框架的三項訂正（已採納，原表已改）

本框架初版為四通道且把 ③ 記為「~0 context」。獨立複審提出三項實質反駁，**均成立**：

1. **③ 的成本量錯了維度**。Hook 只有**不觸發**時零成本；觸發時 block message／PreToolUse 輸出全部注入 context，且落在最不可預測的中段位置。更根本的是 `2026-07-05-measuring-harness-induced-belief-divergence-2607-04528.md` 指出：封鎖動作、過濾證據**即使完成率不變也改變推理過程**。③ 的真實成本是 **belief divergence**，不是 bytes。用「context bytes」單一量綱比較四通道，對 ③ 是錯誤的量綱。
2. **②④ 是串聯不是並聯**。② 的有效性 = ④ 的召回率 × ② 的體積。「② 厚是免費的」只在 ④ 完美時成立；本 session 自己證明了 ④ 半失效，那段期間 1,468 KB 就是死重。並列呈現導致「② 可以無限厚」的錯誤推論。**另：1,468 KB 混計了「agent 工作知識」與「人的檔案庫」（research corpus），兩者的 ④ 依賴度不同。**
3. **漏掉第五通道**。①②④ 是「人寫、模型讀」；**⑤ 持久記憶／run 證據是「模型寫、模型讀」**，失效模式完全不同（drift、自我污染、consolidation 覆寫）。外部文獻的切法都比四通道多出記憶維度：`2026-08-01-harnessing-agent-skills-reference-architecture-2606-20631.md` 的四層架構把 Evidence & Feedback 獨立成層（且該檔已記載「v5.1 整層移除是四層裡唯一被拿掉的」）；`2026-07-20-memoharness-six-control-surfaces-2607-14159.md` 把 memory 與 output processing 各自獨立成 control surface。

> **四通道框架繼承了 v5.1 的同一個盲點**——這是本 session 分析的方法論缺陷，不是實作缺陷。

---

## 3. 路由層（④）的實證缺陷與修復

### 3.1 缺陷

`scripts/skill-router.py` 的 tokenizer：

```python
re.split(r"[^a-z0-9一-鿿]+", text.lower())   # v1
```

CJK 被放在**保留字元類**，整句中文切不開，成為單一 token：

```
研究這篇論文  →  ['研究這篇論文']       # 一個 token
harness 稽核  →  ['harness', '稽核']    # 英文正常
```

索引實測：484 個 term，**221 個含 CJK（46%）**，其中 131 個長度 ≥4；**127 個是「長度≥4 且只出現於單一 skill」的整句型 term**，只有逐字複述才命中。在「繁中優先」的 workspace，等於半個路由層失效。

第二個缺陷：bm25 全為 0 時 `embed_score_stub` 仍給排序，top-1 是「看起來像答案、實際毫無依據」的 skill——**自信地給錯答案的 oracle，比會 abstain 的更糟**（`core.md` §TEST Oracle 先驗）。

### 3.2 修復（commit `2d63141`）

- **tokenize v2**：latin/digit run 整段保留，CJK run 切**字元 bigram**
- **abstain**：bm25 全 0 → 輸出 `{no_match:true, reason, hint, candidates}`，指回 `RESOLVER.md` 人工路由
- **tokenizer_version**：`--check-fresh` 一併比對。`corpus_sha` 只涵蓋來源文字，涵蓋不到「切法變了」；少了這道，改 tokenize 後舊索引會被判 FRESH，索引與檢索邏輯靜默脫節

### 3.3 收據（12 題標註集，v1/v2 同一評分器）

| | top-1 | top-3 | 零分查詢 |
|---|---|---|---|
| v1 | 8/12 | 8/12 | **4/12** |
| v2 | **10/12** | **12/12** | **0/12** |

v1 的 top-3 == top-1，表示**一失敗即完全無訊號**；v2 正解一律落在 top-3。

**未解**：`研究這篇論文`→sia、`選哪個模型檔位`→output-compress 兩題 top-1 仍錯（正解均在 #2），bigram 引入的詞彙噪音所致。**不宣稱已解決**。

**已知方法論限制**：12 題評測集由改動者自出，存在過擬合風險；未做 held-out。

---

## 4. loop / goal / graph 的統一

### 4.1 Loop 是退化的 Graph

`research/papers/2026-04-13-agent-loops-to-structured-graphs-scheduler-2604-11378.md` 把 Agent Loop 重新刻畫為 **single-ready-unit scheduler**：任一時刻至多一個 executable unit 為 active，且「下一步選誰」來自 **opaque LLM inference 而非可檢視的 policy**。由此把 Agent Loop 與 graph-based execution engine 放在**同一 semantic continuum** 上。

> **Loop = 節點恆為 1、邊隱含於 context、排程器是黑箱的 Graph。**
> 因此「要不要從 loop 換成 graph」是假問題。真正的問題是：**那些邊，你要不要寫下來。**

⚠️ 該篇為 position paper，作者明示**無 empirical results**，量化面僅有 70 個 surveyed systems 的 trade-off 分析。

### 4.2 軌跡要分兩層

`research/papers/2026-06-22-grade-graph-representation-agent-dependency-execution-2606-22741.md`（GRADE）：傳統 trace 只記錄步驟順序，遺失「這一步依賴了什麼」。雙層圖模型 = **execution edge**（順序）+ **dependency edge**（依賴，依可見度分級 known/observed/declared/inferred）。六個資料集實證：**dependency 層比單純執行複雜度更能定位失敗**，跨語料測試在未見類別上仍保持效能。

### 4.3 goal 不是第三個 primitive

goal 沿兩軸**各退化一次**：

| 軸 | 退化形態 | 證據 |
|---|---|---|
| **時間軸**（loop 迭代） | 累積 context 下的漂移 | `2026-03-03-asymmetric-goal-drift-coding-agents-2603-03456.md`：value alignment + adversarial pressure + accumulated context 三因子疊加 |
| **依賴軸**（graph 邊） | 繼承式漂移 | `2026-03-03-inherited-goal-drift-contextual-pressure-2603-03258.md`：conditioned on 弱 agent 的 prefilled trajectory 即普遍繼承漂移；**instruction-hierarchy 遵循度無法預測抗漂移力** |

> **goal 是兩軸共同威脅的不變式，不是第三個要素。**

### 4.4 最小實作（commit `304a0a6`）

不引入任何 loop/graph 引擎。`core.md` §RECORD 一句改寫：

```
[Checkpoint] 做了 X／驗了 Y／剩 Z
        ↓
[Checkpoint] 用了 W／做了 X／驗了 Y／剩 Z
             ↑ declared 級 dependency edge
```

「用了 W」= 本步實際消費的輸入（檔案／指令輸出／child 回傳），答不出即依據不明。

**三個效果**：① 隱式 loop 自動成為可稽核 graph（邊寫下來，圖就存在）② 失敗可歸因（GRADE 的主要發現）③ 每次狀態轉移強迫對照原始目標，命中兩軸的共同著力點。

**刻意不做**：`2026-05-15-harnesses-inference-time-alignment-trajectories-2605-21516.md` 列 over-decomposition 為具名失敗模式；`2026-07-14-rethinking-evaluation-harness-evolution-agents-2607-12227.md` 顯示自動 harness 演化未必勝過等算力 test-time scaling。一個欄位即可拿到 GRADE 說有價值的那一層，成本差兩個量級。

**代價**：改 auto-load = 斷 prompt cache 前綴一次（`context-management.md` 五禁令 ③），屬一次性。
**效益未驗證**：本欄位對失敗歸因的實際幫助需累積使用樣本才能評估。

---

## 5. 單人 harness vs 團隊 harness（本 session 最重要的結論）

### 5.1 唯一的結構差異是 principal 模型

`research/papers/2026-06-20-harness-mu-multi-user-llm-agents-2606-21856.md`（Harness-MU）的核心洞見：治理約束——**誰被授權 / 什麼受限 / 誰的指令優先**——是**確定性 runtime 變數，應由 execution hook 強制而非交給 LLM**。並明指存在「當代 LLM 的**單使用者訓練範式**與多 principal 治理硬約束之間的根本錯配」。

反過來讀即是答案：

> **團隊 harness 比單人 harness 多出來的，只有 principal 模型**（授權、優先權、可見範圍）。
> 單人時 principal 恆為 1，這層塌縮成常數而消失。
> 其餘全部——不可逆操作攔截、reward hacking 防線、goal drift、context rot、oracle 資格——防的是**模型**而非**別的人**，因此**與人數無關**。

這為 v5.1 的三分刀口（砍元層 / 砍協作層 / 留執行層）提供了名稱與判準，也解釋它為何砍對又為何在 ③ 砍過頭：協作層確實全是 principal 層，但閘門層跟人數無關。

### 5.2 陷阱：單人 ≠ 單一 context 邊界

> ⚠️ **本節初版把 context 邊界稱為「principal」，該用語經 Fable 5 複審推翻（§C.2）。操作結論不變，理由已訂正：那裡是 agency cost 集中之處，不是新的 principal。**

context 不流動之處，即 principal 邊界：

| 邊界 | 為什麼是 principal 邊界 |
|---|---|
| **sub-agent spawn** | `core.md` §PROPOSE 自承「sub-agent 不繼承 context」——定義上的 principal 切換 |
| **compact / session 結束** | 未來的你拿不到現在的你的 context |
| **跨模型世代** | prompt 意圖不保證跨代存活（`prompt-lifecycle.md` §Cross-Model 遷移 re-express 原則） |

principal 層**沒有消失，只是退化**：威脅從「未授權洩漏」變成「狀態無法交接」。收據 → handoff；存取控制 → context 邊界紀律。

這解釋了一個看似矛盾的證據：`research/papers/2026-08-01-cheap-code-costly-judgment-governable-agentic-se-2607-01087.md` 的設定是**單一專家、12 週第一人稱個案**，與 v5.1「單人不需團隊級防禦」的前提幾乎完全重合，結論卻是治理機制持續**累積**（測試/工具 1.16 MLOC vs 生產 420 KLOC，比例 2.76:1）。

> **因為人走了，邊界還在。**

### 5.3 可用設計規則

> **在單人 harness 裡，需要「團隊級紀律」的地方不是「人多的地方」，是「context 不流動的地方」。**
> 凡 context 不流動之處（sub-agent spawn／compact／跨模型世代），套跨邊界做法（顯式交接、依賴宣告、產出者不驗收自己的產出）；其餘一律砍到底。
> 理由是那裡是 **agency cost 集中地**（資訊不對稱、監督成本、drift 都在那裡產生），**不是**那裡出現了新的 principal——目標的最終擁有者與後果承擔者始終是人（§C.2）。

**這條規則同時取代「依改動範圍決定審查強度」**——見 §6。

---

## 6. 「審查強度隨改動範圍分級」的檢驗（Sonnet 5 主導）

使用者提出：「是否需要審查取決於改動的範圍」。拆成三個可分離的子命題後，文獻支撐度差異很大：

| 子命題 | 支撐 | 證據 |
|---|---|---|
| 該分級（非單一開關） | **支持** | `2026-06-22-maestro-order-model-agnostic-orchestration-harness-2606-23983.md`：verification 幾何放大 0.55 →（2 gate）0.98 →（4 gate）0.999 |
| 生成前分類優於事後升級 | **支持** | `2026-05-07-is-escalation-worth-it-llm-cascades-2605-06350.md`：存在最適切換點，生成前路由優於生成後升級 |
| **分級軸 = 改動範圍** | **文獻未涵蓋** | 無任何一篇以 diff size 為軸量化最適曲線——屬本 workspace 的外推假設 |
| 範圍小 → 較少過度執行 | **未涵蓋且有反例邏輯** | `2026-07-25-consequence-aware-reasoning-compute-allocation-2606-04402.md`：700 個 SWE-bench 任務實測 **consequence 與 difficulty 近乎正交**，用容易測的代理變數分配審查資源使 cost-weighted loss 高 **22–33%** |

### 6.1 規模 ≠ 風險的反例

1. **`.claude/settings.json` 改一行**：diff 1 行、0 跨模組，但改的是 permission allow-list 或 hook 掛載點 = 系統性繞過既有 gate。純尺寸門檻完全放行。
2. **`git push --force` / `rm -rf`**：**0 diff**，但後果不可逆。「改動範圍」概念在此根本不適用。
3. **system prompt 語意改動**：`2026-01-29-when-better-prompts-hurt-eval-driven-2601-22025.md`：把 prompt 從任務特定換成泛用模板，diff 僅數行，卻讓抽取正確率 100%→90%。

### 6.2 結論

「該分級」成立，但**軸選錯了**。更好的軸是 §5.3 的 **context 邊界**：跨邊界的改動需要顯式交接與獨立驗收（因為接手的是另一個 principal），不跨的親做親驗。這比 diff 大小可靠，也比純路徑白名單更貼近實際失效模式。

`core.md` §公理 現行條文「儀式深度隨風險與不可逆性伸縮：風險定驗證下限，檔位只可加碼」**已經是正確的定性版本**（用「風險」而非「範圍」），本次不改。

---

## 7. `[E]` 標記的 liveness 修復（commit `814f341`）

### 7.1 動機

v5.1 §7.3 自承風險「`[E]` 標記可能慢慢說謊」：enforcement liveness 稽核移除後，hook 從 `settings.json` 掉出去不會被機械發現。殘餘防線只剩數量級計數（hooks < 13 即 FAIL），**擋不住等量替換**——刪一支加一支，計數不變而防線已破。

論文依據：`2026-04-18-caaf-harness-as-asset-determinism-2604-17025.md` 主張機讀不變式 registry + 確定性斷言介面，其論據是**執行力**而非讀者人數；v5.1 以「單人不需共同認知」為由刪除屬**論證錯位**。

### 7.2 首次執行即抓到真陽性

`.claude/rules/context-management.md §Prompt Caching` 標 `[E]`，但逐支查證 13 個 hook，**無任何一支在強制那五禁令**（`session-init.sh` 對 `CLAUDE.md` 的操作是 setup，非禁令 Body）。依 `core.md` 檔頭定義（`[E]` = 有實際 hook/gate 支撐）降標。

> **「標記說謊」不是未來風險，已經在說謊。**

### 7.3 機制

純確定性，零 LLM：
- **A** = 規則檔 `[E]` 章節旁 `<!-- E: a.sh, b.sh -->` 宣告的 Body
- **B** = `settings.json` 註冊 ∩ `.claude/hooks/` 檔案存在且可執行
- `A \ B ≠ ∅` → FAIL；標 `[E]` 卻無宣告 → FAIL；`B \ A` → 不報（有牙齒無宣稱，無害）

**設計取捨**：宣告寫在規則檔內而非獨立 manifest，使 claim 與 body 的距離為零（獨立 manifest 會多一層可漂移的間接）。代價每章節約 40 bytes 常駐——**有意為之，讓宣稱 `[E]` 帶一點成本，抑制浮濫標記**。

### 7.4 Oracle 資格（一好三壞）

| 樣本 | 結果 |
|---|---|
| 已知好：現況 | exit 0 |
| 已知壞 A：`settings.json` 移除 `test-integrity-guard` 註冊 | `NOT-REGISTERED`，exit 1 |
| 已知壞 B：`post-edit.sh` 移除可執行權限 | `REGISTERED-BUT-NOT-EXECUTABLE`，exit 1 |
| 已知壞 C：新增標 `[E]` 但無 `<!-- E: -->` 的章節 | 指名行號，exit 1 |
| 端到端 | 已知壞使 healthcheck 由 FAIL 0 → FAIL 3；復原回 0 |

**已知限制**：「有註冊且可執行」是 proxy，不證明「它真的會擋」。workspace 自身前例 `memory-pr-record.sh`「註冊完整、註解齊全但從未生效」即同型缺陷。本檢查覆蓋的是**掛載面**，非**行為面**。

---

## 8. 稽核方法論的教訓（本 session 兩次犯同一個錯）

### 8.1 錯誤

第一次：稽核 v2–v5 世代遺留時，我的檢查器只掃**加了反引號**的檔名引用，宣稱「活躍指針清零」。第二次放寬為裸檔名後，又抓出 **42 筆 / 27 檔**。

根因與 `scripts/check-references.sh` 的 `TICK_RE` 完全相同——該 regex 要求路徑含 `/`，故 `` `graph.md` ``、`` `subagent-strategy.md` `` 這類裸檔名一筆都掃不到。**dangling 長年報 0，實際躺著 81 筆死引用。**

### 8.2 教訓

> **檢查器的涵蓋面要按「實際存在的形狀」盤點，不是按「我習慣的寫法」盤點。**

這與 `core.md` §TEST「Gate 選擇稽核：gate 須行使宣稱涵蓋的實際執行路徑，非 proxy 子集」同源，也與 §7.2 抓到的 `[E]` 說謊同源——三者都是「宣稱涵蓋 > 實際涵蓋」。

### 8.3 已知殘留（刻意不改）

`harness-model-fit.json`、`reports/skill-audit-*.json`（稽核資料快照）、`memory/*`（歷史）、`scripts/tests/test-harness-tpki-probe.sh`（oracle 檔，其 T6 案例引用已刪的 `loop.md`，**列為待查**）、`README.md` 的 v5 改版沿革、各 script 註解裡的 provenance 記錄。

判準：**修指針型引用（「見 X」「依 X」），保留帶日期的觀察記錄**。

---

## 9. 落地清單與收據

| # | 改動 | commit | 收據 |
|---|---|---|---|
| P0 | router CJK bigram + abstain + tokenizer 版號閘 | `2d63141` | 12 題：top-1 8→10、top-3 8→12、零分 4→0；版號閘正反例通過 |
| P1 | `[E]` 差集比對 + healthcheck 接線 | `814f341` | Oracle 一好三壞全過；端到端 FAIL 0→3→0；首跑抓到 1 筆真陽性 |
| P2 | `[Checkpoint]` 加 dependency 欄 | `304a0a6` | auto-load 10,771→10,894 B |
| — | 裸檔名死引用補掃（13 處）+ L2 數字訂正（2 處） | `4a0304c` | `description` 常駐 20,038→13,989；fan-out 上限 4→無規則上限 |

**明確不做**（附理由）：
- ✗ 壓縮 description 省常駐 —— 分佈平坦，且傷 ④
- ✗ 縮小 `skills/` —— ② 常駐成本為零
- ✗ 引入 loop/graph 引擎 —— over-decomposition 為具名失敗模式
- ✗ 重新引入尺寸門檻 —— 規模與風險近乎正交

---

## 10. 未解與待驗

1. **④ 的 top-1 仍只有 10/12**。再往上要 CJK 分詞或 embedding，成本非 5 行量級。建議先觀察——已有 abstain，router 不會再自信地騙人，這比準確率再高 8% 重要。
2. **P2 的效益未驗證**。dependency 欄對失敗歸因的實際幫助需累積樣本。
3. **所有收據皆為結構級**。無行為等價性證明（§1.2）。要驗需變異度量測（同任務多次重跑的離散度）或 `2026-08-01-heavy-lifting-agent-harness-residual-role-2604-07236.md` 的分層消融設計，本 workspace 目前無此基建。
4. **12 題 router 評測集由改動者自出**，未做 held-out，存在過擬合風險。
5. **`scripts/tests/test-harness-tpki-probe.sh` 的 T6 案例**引用已刪的 `loop.md`，可能已失效。屬 oracle 檔，未動。

---

## 附錄 A：三方模型分歧登記

| 議題 | Fable 5 | Opus 5 | Sonnet 5 | 處置 |
|---|---|---|---|---|
| 薄 harness 是否為趨勢 | 否（整體），僅 ①② 面成立 | 未直接答，但代價不對稱 | 未直接答 | 收斂，無分歧 |
| 是否補回元防線 | — | **補**（`[E]` 差集，元防線保護其餘 12 支 hook） | **不補**（四道既有 hook 已覆蓋 L3，純文件接線即可） | 使用者裁決採 Opus 5，已落地 `814f341` |
| 分級軸 | — | — | **否定 diff size 為軸**（consequence ⊥ difficulty） | 採納，改用 context 邊界（§5.3/§6.2） |

## 附錄 B：本報告引用的 corpus 檔案

全部位於 `research/papers/`：

`2026-04-20-architectural-design-decisions-ai-agent-harnesses.md` ·
`2026-08-01-stop-comparing-agents-without-disclosing-harness-2605-23950.md` ·
`2026-08-01-heavy-lifting-agent-harness-residual-role-2604-07236.md` ·
`2026-06-08-what-makes-a-harness-necessary-sufficient-2606-10106.md` ·
`2026-06-08-less-context-better-agents-2606-10209.md` ·
`2026-03-26-natural-language-agent-harnesses-nlah.md` ·
`2026-06-14-survey-agent-system-harness-design-2606-20683.md` ·
`2026-06-24-interplay-harness-design-post-training-2606-25447.md` ·
`2026-04-18-caaf-harness-as-asset-determinism-2604-17025.md` ·
`2026-08-01-cheap-code-costly-judgment-governable-agentic-se-2607-01087.md` ·
`2026-08-01-harnessing-agent-skills-reference-architecture-2606-20631.md` ·
`2026-07-09-from-prompts-to-contracts-harness-engineering-2607-08028.md` ·
`2026-06-22-self-compacting-language-model-agents-2606-23525.md` ·
`2026-05-15-harnesses-inference-time-alignment-trajectories-2605-21516.md` ·
`2026-07-14-rethinking-evaluation-harness-evolution-agents-2607-12227.md` ·
`2026-07-05-measuring-harness-induced-belief-divergence-2607-04528.md` ·
`2026-04-30-ahe-observability-driven-harness-2604-25850.md` ·
`2025-05-09-llms-get-lost-multi-turn-2505-06120.md` ·
`2025-05-05-evaluating-goal-drift-language-model-agents-2505-02709.md` ·
`2026-03-03-asymmetric-goal-drift-coding-agents-2603-03456.md` ·
`2026-03-03-inherited-goal-drift-contextual-pressure-2603-03258.md` ·
`2026-04-13-agent-loops-to-structured-graphs-scheduler-2604-11378.md` ·
`2026-05-07-agent-loops-to-deterministic-graphs-execution-lineage-2605-06365.md` ·
`2026-06-22-grade-graph-representation-agent-dependency-execution-2606-22741.md` ·
`2026-06-20-harness-mu-multi-user-llm-agents-2606-21856.md` ·
`2026-06-22-maestro-order-model-agnostic-orchestration-harness-2606-23983.md` ·
`2026-05-07-is-escalation-worth-it-llm-cascades-2605-06350.md` ·
`2026-07-25-consequence-aware-reasoning-compute-allocation-2606-04402.md` ·
`2026-01-29-when-better-prompts-hurt-eval-driven-2601-22025.md` ·
`2026-07-02-when-agents-do-not-stop-infinite-agentic-loops-2607-01641.md` ·
`2026-06-02-token-budgets-overrun-incidents-affine-rust-2606-04056.md`

---

## 附錄 C：三方對抗複審與全數採納的訂正（2026-08-02，落地後）

P0/P1/P2 落地**之後**再送三方獨立複審，刻意設定為對抗立場（「預設這些改動有問題，請盡力證明」）。所有指控依 `core.md`「child verdict 非證據，採信前重驗」逐項機械查證。

### C.1 Fable 5 — 對四通道框架本身的三項反駁（全部成立，已改正文 §2.4）

見 §2.3。核心：③ 的成本量錯維度、②④ 是串聯、漏掉第五通道。**四通道框架繼承了 v5.1 的同一個盲點**。

**Fable 5 另提一個比 P2 更高槓桿的選項（未採納，登記）**：最小 run 證據層——每次 skill 觸發記一行（skill 名 + session + 結果）。理由是 `2026-08-01-harnessing-agent-skills-reference-architecture-2606-20631.md` 已載明「v5.1 刪 `tool-log.sh` 的判準是『純寫入無消費者』，而 `skill-evolution` 就是現成消費者，判準結論應翻轉」。

> 其最尖銳的一句：**「P0 修了路由器，但沒修『路由器永遠拿不到真實 query 分佈』這個結構問題。」**

主對話查證補充：`.claude/skills/.router-log.jsonl` **已存在**（397 行），但只記錄 CLI `--query` 呼叫——真實路由發生在模型讀 `description` 時，不流經它。故該 log 目前不是真實查詢分佈，Fable 5 的論點成立且更強。**此項為待裁決提案，未實作**（新增 PostToolUse[Skill] logger = 新常駐/延遲成本，屬治理決策）。

### C.2 Fable 5 — 推翻「principal = context 邊界」（已採納，正文 §5.3 需連帶讀本節）

本報告 §5.3 提出「單人 harness 裡 principal 的單位不是人，是 context 邊界」。Fable 5 給出**三個反例**：

1. **`core.md` §APPLY 不可逆確認規則**：「不可逆操作永遠等確認（**無論記憶／compact 摘要聲稱已豁免**）」——這條規則**明文拒絕** context 邊界（compact 摘要）取得 principal 地位。若 principal 真是 context 邊界，compact 後的摘要就有權豁免確認；規則刻意寫成相反。
2. **`output-discipline.md` 全檔 `[U]` 契約**：其約束力來源是使用者偏好，跨任意多個 context 邊界不變——principal 顯然是人。
3. **`2026-08-01-cheap-code-costly-judgment-governable-agentic-se-2607-01087.md`**：單一專家 12 週，治理隨**人的**經驗累積——principal 的連續性單位是那個人的判斷力。

**訂正後的正確表述**：

> context 邊界是 **agency cost 發生的地點**（監督成本、資訊不對稱、drift 都在那裡產生），但 **residual claimant（目標的最終擁有者、後果承擔者）始終是人**。
> 把「失真發生處」升格為「principal」是**把 mechanism 誤認為 authority**——這個誤認若被當真，會正當化「compact 摘要可以改寫紅線」，正是 `core.md` 明文防的事。

§5.3 的**操作結論仍然有效**（凡 context 不流動處套跨邊界紀律），但**理由要改**：不是因為那裡出現了新 principal，而是因為那裡是 agency cost 集中之處。

### C.3 Opus 5 — 對 P0/P1/P2 的逐項判決（訂正已全數落地於 commit `e78e707`）

| 項 | 判決 | 查證結果 | 處置 |
|---|---|---|---|
| P0 tokenizer 修復 + 版號閘 | 做對 | — | 保留 |
| P0 的 12 題收據 | **做錯**（oracle 未入庫） | 屬實：`grep -rl` 全 tree 找不到標註集與評分器 | **已入庫** `scripts/tests/test-skill-router-routing.sh`，數字完全重現 |
| P0 abstain | 做對但宣稱過寬 | 屬實：abstain 只擋「零詞彙重疊」，擋不住 in-domain near-miss（真正的失效模式）。Opus 5 實跑 5 個 off-domain query 證明 abstain 仍會觸發，**證偽了「假保險」的假設**，但範圍錯配成立 | 檔頭載明限制 |
| P1 方向 | 做對 | 首跑抓到真陽性 | 保留 |
| P1 實作 | **做錯**（proxy 非真驗證 + 三個涵蓋洞） | 屬實：只掃標題行／只掃 `rules/`／不驗 event-matcher | **已修**：掃描面含 inline、輸出行印出三項已知不涵蓋 |
| P1 對 `core.md:41` 的新宣稱 | **做過頭**（把更寬的謊言機械合法化） | 屬實：`post-edit.sh` 掛 PostToolUse，檔頭自述 exit 1/2 皆 warn 不阻斷 | **已撤回**：`[E]` 下放至真正有 Body 的 bullet，並標明 Body 涵蓋邊界 |
| P2 `用了 W` | **做過頭，建議撤回** | 屬實：無 Body、非失效驅動（論文驅動）、常駐層 | **未撤回**——該項為使用者明示核可，撤回屬 scope 變更需其裁決。爭點見 §C.4 |
| 4a0304c | 做對 | — | 保留 |

**Opus 5 指出的一條三次復發 pattern（已達 `core.md` §RECORD「同簽名 ≥2 次才改規則」門檻）**：

| 次 | 稽核器 | 宣稱範圍 | 實際涵蓋 |
|---|---|---|---|
| 1 | `check-references.sh` `TICK_RE` | 死引用 | 只有加反引號的 |
| 2 | `check-section-refs.py` 之前 | 引用可解析 | 只驗檔案路徑、不驗段落 |
| 3 | `check-enforcement.sh`（本次） | `[E]` 說謊 | 只驗標題行／只驗 `rules/`／只驗檔名出現 |

→ 已入 `memory/LESSONS.md`：**新稽核器上線時，「已知不涵蓋」必須連同宣稱一起寫進檔頭與輸出行**。本次 `check-enforcement.sh` 已據此改為在輸出行印出不涵蓋清單。

**Opus 5 對量測方法論的第三列最值得標記**：一好三壞 oracle 測的是「checker 能不能分辨我人為造的三種壞」，通過了；但 checker 的**涵蓋面**從未被測——三種壞例全部落在它已涵蓋的區域內。

> **oracle 資格 ≠ oracle 涵蓋面。本 session 把前者當成了後者。**

另一項：`healthcheck` 191→193 的 +2 中有 1 個就是**新加的 `check-enforcement` 自己**——加一道檢查使 PASS 數上升，拿它當健康度收據是同義反覆（風險 R7：計數通膨）。

### C.4 P2 的未決爭點（留給使用者裁決）

Opus 5 主張撤回，判準三條：① 不服務 workspace 之外的產出 ② 非真實失效催生（來源是讀論文）③ 無 Body。並指出它違反 `AGENTS.md` §21「寫閘門不寫步驟」——`用了 W／做了 X／驗了 Y／剩 Z` 是步驟性格式規定。

其自指性回歸判定：

| | 對外產出 | 失效驅動 | 有 Body | 判定 |
|---|---|---|---|---|
| P0 | 是 | 是（484 term 中 221 含 CJK，實測） | 是 | 不是回歸 |
| P1 | 否 | 半（§7.3 是預先推導，但首跑抓到真陽性） | proxy | 邊緣通過 |
| P2 | 否 | **否** | **無** | **回歸** |

> Opus 5 的結論：「這不是 harness 開始長回來（總增量 1 支腳本／+123 bytes／2 個註解，遠低於 v5.1 刪除量），**但 P2 是那個模式的第一顆種子**——它的生成路徑（讀到論文 → 加一條常駐條文 → 自承效益未驗證）正是 v5.1 要根除的那條路徑。」

**主對話立場**：判準三條我認為成立，反駁不了。但 P2 是使用者對「loop/goal/graph 怎麼合」這個提問的直接回應，且經其明示核可；撤回屬 scope 變更。**建議**：若三週內隨機抽查 `[Checkpoint]` 輸出發現「用了 W」缺席率高（R5 前導指標），即撤回並改落 `/handoff` state 檔（按需、零常駐稅），那才是 GRADE dependency-edge 洞見的正確落點。

### C.5 Sonnet 5 — fusion 缺口（G1–G4/G6 已落地，G5/G7 依其建議不做）

見 `commit e78e707`。最大缺口 G1「繼承漂移零防線」：原條文的「verdict 非證據」只覆蓋**成功宣稱**，不覆蓋 sidekick 對約束是否滿足的**敘事框架**；而 sidekick 預設 cost 檔（haiku）正是 `2603.03258` 實驗設定裡的「較弱 agent」。已補「敘事亦非證據」為 §0 不變式。

Sonnet 5 明確**不建議**加的（已遵從）：GRADE 完整圖模型基礎設施、sidekick 自身 context 劣化 rubric、Rust affine-type 預算機制、partial-failure 五項全強制——理由皆為「論文的適用場景與 fusion 的單 sidekick 規模不匹配」。

---

## 附錄 D：復盤（本 session 的自我審視）

### D.1 做對的

1. **先量測再下結論**。四通道模型的價值不在分類本身，而在它逼出了「④ 比 ① 大且是壞的」這個實測事實。若只憑直覺談厚薄，這個發現不會出現。
2. **P0 是本 session 品質最高的產出**。真 bug、有 oracle、有版號閘防未來靜默脫節、誠實列出兩題未解。
3. **落地後再送對抗複審**，而非只在事前徵詢。三項實質缺陷全部是複審抓出來的，事前的自我檢查一項都沒抓到。
4. **查證後才採納 child verdict**。Opus 5 的每一項指控我都機械重驗（`post-edit.sh` 的 exit 語義、checker 的 `startswith("#")`、`grep -rl` 找評測集），沒有直接照單全收。

### D.2 做錯的

1. **收據不可重跑**（最嚴重）。12 題評測集只活在 heredoc 裡，數字漂亮但不可稽核。這違反的是本 workspace 自己最核心的紀律之一。
2. **為新 checker 蓋了假綠章**。把非阻斷的 `post-edit.sh` 當「不可協商閘門」的 Body——修 `[E]` 說謊的同一個 commit 製造了一筆新的 `[E]` 說謊。
3. **第三次犯同一個涵蓋面錯誤**（見 §C.3 表）。前兩次都已經有記錄，我仍然重蹈。
4. **稽核宣稱過寬**。「活躍指針清零」實際只涵蓋加反引號者，是我自己在同一 session 內先宣稱、後訂正。
5. **把 oracle 資格當成 oracle 涵蓋面**。一好三壞全過就宣告 checker 合格，但三個壞例都在它已涵蓋的區域內。

### D.3 這五項的共同結構

> **全部都是「宣稱涵蓋 > 實際涵蓋」。**

`core.md` §TEST 已有這條規則（「Gate 選擇稽核：gate 須行使宣稱涵蓋的實際執行路徑，非 proxy 子集」），而我在同一個 session 內違反它至少四次。**規則存在不等於規則被遵守**——這本身就是 §7.2 抓到的 `[E]` 說謊的同構現象，只是主體從 hook 換成了我。

### D.4 淨帳

| 維度 | 數字 |
|---|---|
| commit 數（含 evolution 自動同步） | 23 |
| 檔案變更 | 342 檔、+2,923 / −927 行 |
| 新增機械閘門 | 1（`check-enforcement.sh`） |
| 新增回歸絆線 | 1（`test-skill-router-routing.sh`） |
| 修復的真 bug | 1（CJK tokenizer） |
| 抓到的真陽性 | 2（`[E]` 說謊 ×1、`post-edit.sh` 假 Body ×1，後者是自己製造又自己修的） |
| 清理的死引用 | 81（反引號）+ 42（裸檔名）+ 3（`security-hygiene`） |
| auto-load 常駐變化 | 10,726 → 10,894 B（+168，門檻 ≤20,400） |
| 訂正的過期數字 | 2（`description` 常駐、fan-out 上限） |

### D.5 留給下一個 session 的

1. **P2 的去留**（§C.4）——前導指標：`用了 W` 缺席率。
2. **run 證據層**（§C.1）——Fable 5 的提案，判準已翻轉（消費者已存在），未實作。
3. **`check-enforcement` 的第二階**——目前證明「掛載」，不證明「生效」。`GITHUB-DECOUPLING-AUDIT-2026-07-30.md` 早已提議 `hook-liveness-smoke.sh`，至今不存在。
4. **router top-1 仍 10/12**——再往上需 CJK 分詞或 embedding，非 5 行量級。
5. **所有收據仍為結構級**——無行為等價性證明（§1.2）。
