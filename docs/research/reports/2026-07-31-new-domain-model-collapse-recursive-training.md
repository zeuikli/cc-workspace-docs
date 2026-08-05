---
date: "2026-07-31"
archived_items: 3
dedup_verified: True
domains: [model-collapse-recursive-training]
grounded_sources: [2603.11784, 2606.13796, 2607.17043]
source_routine: routine-e
type: new-domain-report
---

# 新領域研究報告 2026-07-31：遞迴／合成資料訓練導致的模型崩潰（Model Collapse）

## 執行摘要

本次探勘選定單一新領域：**Model Collapse in Recursive / Synthetic-Data Training**——生成模型（LLM／diffusion model）反覆用自身或同代模型產出的合成資料訓練，導致分佈逐代偏離真實資料、多樣性遞減的結構性退化現象。三篇 2026 年 3-7 月論文分屬理論保證、過程解析、實務配方三個互補層次，構成本領域目前最小完整切片。本輪探勘過程本身值得記錄：ceiling 檔位 sub-agent 最初選出的兩個候選（world-model verification、continual learning）皆在 parent 的機械覆核下被推翻，過程細節見下節。

## 為何是「新」領域（反回音室證明）

### 本次選定領域的去重結果

雙重 grep 驗證（窄詞對 `/tmp/covered_topics.txt` + `/tmp/covered_paper_terms.txt` + `research/NEW-DOMAINS/covered_topics.txt`；廣詞對全庫 `research/reports/*.md` + `research/papers/*.md` + `research/DAILY-TOPICS/*.md` + `research/WEEKLY-FOCUS.md` 全文反向覆核，捕捉「詞不同但概念已覆蓋」的 false-negative）：

| 檢查詞 | 窄詞命中 | 廣詞命中 | 判定 |
|---|---|---|---|
| `model collapse` | 0 | 2（見下方殘餘重疊說明） | ✅ |
| `recursive training` | 0 | 0 | ✅ |
| `distribution collapse` | 0 | 0 | ✅ |
| `synthetic data` | 0 | 3 | ✅（<3 判定線上，內容非同題） |
| `polarization of competence` | 0 | 0 | ✅ |
| `KITE` | 0 | 0 | ✅ |
| `replay adversary` | 0 | 0 | ✅ |
| `spectral characterization` | 0 | 0 | ✅ |
| `autophagy` | 0 | 0 | ✅ |
| `self-consuming` | 0 | 0 | ✅ |

**唯一殘餘重疊點（誠實揭露）**：`research/papers/2026-07-21-recursive-self-improvement-taxonomy-2607-07663.md`（已歸檔論文，探討「遞迴自我改進」失效模式分類法）把 `model collapse` 與 self-confirming loops、diversity collapse 並列為分類項之一，僅一句話帶過，未觸及機制。另一份 2026-06-07 報告提及「reward model collapse」，是 RLHF 中 reward model 過擬合的不同機制（與生成資料遞迴污染無關），純屬同名詞巧合。判定：列舉 ≠ 覆蓋——本次三篇論文深入的是機制本身（極限分佈的存在性與頻譜特徵、學習理論下的生成保證可分離性、能力極化現象與對應配方），既有覆蓋停留在「知道有這個名詞」的層次。

### 本輪被推翻的兩個候選（過程記錄）

Routine E 本輪模型紀律要求「選定 1-2 個新領域」的裁決 spawn ceiling 檔位（opus）sub-agent 執行；該 sub-agent 首輪選出兩個候選，皆在 parent 事後機械重驗（`graph.md §G5`：verdict 非證據，採信前機械重驗）下被推翻：

| 候選 | 窄詞 grep（sub-agent 依據） | Parent 廣詞覆核結果 | 判定 |
|---|---|---|---|
| **World-Model Verification / Admissibility** | `world model`/`world-model`/`certification`/`hallucination` 皆 0 | 本 workspace 過去兩次 Routine E 執行（2026-07-03、2026-07-12 報告）已明確考慮 world-model 候選並主動排除，理由皆為「與 2026-06-28 已收錄的 formal-verification-robotics/機器人領域高度鄰接、準回音室」；本次候選首要論文（arXiv:2607.07196）恰是驗證機器人/自駕車 policy 的 world-model 模擬器，實質為該已排除領域的延伸 | ❌ 落回音室（違反本 routine 自身既定慣例：近期慣例優先於單次孤立判斷） |
| **Continual Learning for LLMs** | `continual`/`federated` 皆 0 | 對全庫做反向概念詞 grep：`consolidation`=96 命中、`遺忘`=75、`漂移`=48、`continual`=46——workspace 既有 memory/context-engineering 覆蓋已高度涉及這些概念，實質回音室風險遠高於窄詞 grep 顯示的樣子 | ❌ 落回音室 |

兩案例共同教訓：窄詞 grep（對 DAILY-TOPICS 主題 slug 與論文標題）是必要但不充分的去重防線，對「用不同詞彙談同一概念」（continual learning ↔ consolidation/遺忘/漂移）與「用同詞彙談已被排除的鄰接領域」（world-model 對機器人驗證）皆會誤判為通過。本次起在 IDENTIFY／PROPOSE 額外加入全庫廣詞反向 grep 作為第二道防線；後續 Routine E 執行應延續此作法（建議寫入下次 SKILL 迭代，見後續追蹤建議）。

Workspace 現有論文與研究報告高度集中於 LLM/agent/harness/memory engineering，機制層面的 model collapse 理論（頻譜刻畫、生成保證分離定理、能力極化配方）完全未觸及。

## 領域概覽

### 核心問題 / 範式

Model collapse 指生成模型反覆以自身（或同代模型）產出的合成資料再訓練，導致分佈逐代偏離真實資料、多樣性遞減，終至收斂到退化分佈。本領域近期的範式轉折在於：collapse 不再被視為「合成資料品質不夠好」的工程雜訊，而被刻畫成訓練—取樣迴路的結構性產物——每一步都做對也躲不掉。arXiv:2606.13796 給出最尖銳的證據：在 score 估計完美、取樣精確的理想化假設下，反向擴散為數值穩定而做的 early stopping 本身即足以驅動漸進 drift；作者證明遞迴訓練以幾何速度收斂到唯一極限分佈，該分佈可寫成真實分佈之高斯平滑版本的無窮混合，頻譜上等價於一個低通濾波器，對高階非高斯特徵的壓制遠甚於粗特徵。換言之，崩潰的第一受害者是分佈的細部結構，不是平均表現。

arXiv:2603.11784 把同一問題抬到學習理論層次，以「replay adversary」形式化自產資料回流（對手可將生成器過去的輸出注入訓練資料流），並給出一組分離定理：uniform generation 對 replay 免疫，而較弱的 non-uniform generation 與 generation-in-the-limit 則可證明地被破壞。這把「會不會崩潰」從經驗問題轉成「你要的是哪一種生成保證」的定義問題，同時劃出資料清洗、浮水印等既有防線的失效條件。

arXiv:2607.17043 則從實務端指出：collapse 在迭代式指令微調中的表徵不是均勻退化，而是「能力極化（polarization of competence）」——合成資料強化模型本來就強的能力，同時讓本來就弱的能力更弱。其 KITE 方法據此把重心從「稀釋合成資料比例」轉為「選擇性生成」。三篇合起來的主軸是：崩潰是迴路的幾何性質，防線必須建在資料源純度與生成目標的定義上，而非事後清洗。

### 關鍵玩家 / 代表工作

| arXiv id / URL | 標題 | 作者 | 定位 |
|---|---|---|---|
| [2603.11784](https://arxiv.org/abs/2603.11784)（v1 2026-03-12, v2 2026-07-05, ICML 2026 accepted） | Language Generation with Replay: A Learning-Theoretic View of Model Collapse | Giorgio Racca, Michal Valko, Amartya Sanyal | 學習理論層：replay adversary 形式化 + 生成概念間的分離定理 |
| [2606.13796](https://arxiv.org/abs/2606.13796)（2026-06-11） | Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral Characterization | Naïl B. Khelifa, Richard E. Turner, Ramji Venkataramanan | 解析刻畫層：極限分佈存在性、幾何收斂、低通濾波頻譜特徵、退火截斷排程 |
| [2607.17043](https://arxiv.org/abs/2607.17043)（2026-07-19） | Learning from Synthetic Data without Model Collapse in Iterative Instruction Tuning | Xiaonan Luo, Yue Huang, Kehan Guo, Ping He, Chuan Zou, Ting Hua, Xiangliang Zhang | 實務配方層：能力極化現象 + KITE（失敗引導生成 + 邊界感知不確定性篩選） |

三篇分屬三個互補層次（理論保證 / 生成過程解析 / 訓練配方），彼此不重疊，構成本領域目前最小完整切片。

### 當前進展與開放問題

**SOTA 形狀**：對 diffusion，遞迴訓練的漸進行為已可解析刻畫——極限分佈唯一、收斂速度幾何、退化方向可用頻譜語言精確描述（高頻／非高斯結構先死），理論在存在離散化與 score 估計誤差時仍穩健。對語言生成，「哪一類生成目標對 replay 脆弱」已有分離定理，不再是全有全無的經驗直覺。緩解手段的重心已從「事後清洗／少摻合成資料」移到兩條較深的路徑：改造取樣排程（退火截斷）與改造資料生成本身（失敗引導 + 邊界篩選）。

**開放問題**：
- **跨模態不可移植**：diffusion 的低通濾波刻畫依賴反向擴散結構，無法直接搬到自回歸語言模型；LM 上的等價極限分佈目前沒有對應定理。
- **臨界混合比例無普適理論**：真實／合成資料的安全混合比例仍是逐設定的經驗量，未與模型容量、資料維度掛鉤成通用界。
- **偵測 vs 存在性**：學習理論結果給出的是清洗與浮水印「何時失效」的條件，而非可操作的線上偵測器——實務上仍缺「這批資料已被自產內容污染到什麼程度」的可計算指標。
- **能力極化的量測依賴既有 benchmark 的能力分軸**：若某項能力不在評測分軸上，極化會完全隱形，暗示現行評測系統性低估 collapse。
- **生態級（多模型互餵）collapse 幾乎沒有理論**：現有結果幾乎都假設「自餵」單一模型；真實網路上是多模型交叉污染，其動力學未有答案。
- **KITE 類方法的遞迴閉合性未解**：若失敗判定訊號本身也來自模型自評，方法可能只是把 collapse 推遲一代（見「潛在槓桿」段落與 open_questions 討論）。

## 對本 workspace 的潛在槓桿

本 workspace 的三個核心迴路——`/autoload-evolution`（規則檔用系統自己的執行紀錄改寫）、`skill-evolution`、`dreaming-consolidator`（LESSONS/MEMORY 的週期性合併）——在結構上都是「以系統自身過去輸出作為下一代訓練資料」的遞迴迴路，與本領域研究對象同構。以下每點皆為**待驗證**假說，非既定結論；隱喻同構的預測力未經任何驗證，讀者不應把隱喻誤讀為已證機制。

- **`/autoload-evolution` 可能落在「脆弱側」（待驗證）**：若演化目標只是「產出能通過既有 gate 的規則版本」（近似 generation-in-the-limit 弱保證），replay 分離定理指出這種弱保證可證明地被自產資料回流破壞；若目標是「覆蓋所有應被攔截的情形」（近似 uniform generation）才免疫。可操作檢驗方向：演化的成功判準是否曾以**未見過的違規樣本**抽驗，而非只確認既有 fixtures 仍綠。
- **consolidation 可能優先抹除低頻高資訊條目（待驗證）**：若低通濾波隱喻成立於文字記憶，`dreaming-consolidator` 每輪合併會優先抹除「高階非高斯特徵」——即 LESSONS 裡的單次 gotcha、`TODO(conflict)` 這類低頻但高資訊條目，合併後規則平均反而更「順」。支持 `core.md` 既有「consolidation 不得覆寫原始證據、保留 rollback」條文，並提示更強版本：consolidation 產物應為 view 而非 replacement。
- **工程性截斷本身可能是 drift 源，不需要任何一步出錯（待驗證，最反直覺一條）**：early stopping 這種純為數值穩定而設的截斷，在完美估計下仍驅動系統性偏移。workspace 對應物是 `/compact`、摘要、輸出截斷——這些都是為穩定性而做的 early stopping。推論：`core.md`「目標外錨 + checkpoint 對照重錨」對抗的是結構性 drift 而非單純保險；「這輪沒發現錯誤」不能當作沒有漂移的證據。
- **能力極化可能意味著用成功案例演化規則會放大強項、惡化弱項（待驗證，與現行條文有張力）**：若此結論可移植，規則演化應以 `LESSONS.md` 的失敗模式為主要語料而非順利完成的任務紀錄。這與 `core.md`「同簽名重現 ≥2 次才改規則」存在張力（後者節流「改規則」，前者主張失敗訊號是唯一抗極化的資料源）——兩者不必然衝突但值得顯式對帳，非靜默選邊。
- **`[claim:verified]`/`asserted`/`judgment` 三標籤可能對應邊界感知篩選（待驗證）**：可操作假說是僅 `verified` 產出可作規則演化的一等語料，`asserted` 視同合成資料需稀釋標註，`judgment` 只能作為 open question 不能作為證據。
- **`graph.md §G5「verdict 非證據」與資料源純度紀律可能是同一條原理（待驗證，同構性強）**：把 sub-agent verdict 當證據採信，等價於把合成資料當真實資料放進訓練集；parent 機械重驗等價於維持真實資料錨比例。這給既有條文新的理論支撐角度——重驗不只是防 child 說謊，而是防止判定基礎逐代被自身輸出置換，即使每個 child 都誠實，純度稀釋仍會發生。
- **可能可量化的健康指標（待驗證，可行性未確認）**：測出 `memory/LESSONS.md` 中「來自使用者糾正／外部工具確定性失敗」條目佔比（真實訊號）對比「來自 agent 自我反思」條目佔比（合成訊號），其時間趨勢或可作為 workspace 版的合成資料比例曲線；是否有現成欄位可機械區分兩類來源，尚待查證。

## 收錄來源

- research/papers/2026-07-31-model-collapse-replay-learning-theory-2603-11784.md — https://arxiv.org/abs/2603.11784
- research/papers/2026-07-31-model-collapse-diffusion-spectral-2606-13796.md — https://arxiv.org/abs/2606.13796
- research/papers/2026-07-31-model-collapse-kite-instruction-tuning-2607-17043.md — https://arxiv.org/abs/2607.17043

## 後續追蹤建議

- 值得持續關注：若下次探勘再遇 model collapse 相關前沿（例如生態級多模型互餵動力學、或跨模態極限分佈理論），可視為本領域的深化延伸而非新領域。
- **流程改進提案（待驗證，不自動套用）**：本次過程顯示窄詞 grep 對「同詞不同層」（world-model 對已排除鄰接領域）與「異詞同概念」（continual learning 對既有 consolidation/遺忘覆蓋）皆會漏判，建議 `research/ROUTINE-E-new-domain-exploration.md` 的 IDENTIFY 步驟正式納入「全庫廣詞反向 grep」作為第二道防線（本報告已示範做法），並在 PROPOSE 前先讀過去至少 2-3 份報告的「候選領域比較」表以繼承既有排除慣例——此為提案，須經 skill-evolution 或人工核可後才修改 SKILL/SSoT，不在本次自動套用。
- 回訪機制本輪執行結果：對 `research/NEW-DOMAINS/INDEX.md` 中 ≥90 天前（cutoff 2026-05-02）的既有列做消費檢查——**本輪無符合條件的列**（現有最舊列為 2026-06-28，尚未滿 90 天），無需更新回訪計數或 dormant 標記。
