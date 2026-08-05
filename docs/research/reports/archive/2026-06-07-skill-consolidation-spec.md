---
title: "SKILL 同質性盤點與整併評估規格書"
date: 2026-06-07
status: 已裁（2026-06-07）— ship-review 維持獨立已核准；P-A/M2/M1 保留提案不執行；本 session 不動 .claude/skills/，規格書為唯一交付物
branch: feature/skill-evolution-audit
disposition_authority: 所有 merge/delete 為破壞性動作（改 RESOLVER routing 不可逆）→ core.md APPLY 段 gate，逐項 AskUserQuestion 待核准
mnilax_corpus: "research/tweets/2026-05-{01,05,09,11}-@Mnilax-*.md（skill 數量過載論點）"
scope: .claude/skills/（27 個 SKILL.md；不含 plugin/command skills 如 grill/quick-pr/deep-research）
source_plan: research/reports/2026-06-07-deep-practices-v2-execution-plan.md
type: evaluation-spec
---

# SKILL 同質性盤點與整併評估規格書

> ⚠️ **現況更新**（2026-06-21）：本規格書撰寫時 skill 數為 27；pilot-review、quality-pipeline、multi-mode-skill 三個 skill 後續加入，現況為 **28 skills**。分析邏輯仍有效，分母數字已過時。

> **任務**：(1) 對 `ship-review` 跑 skill-evolution 評估是否合併；(2) 盤點全部 27 SKILL 同質性，評估刪除/合併；(3) 寫成符合 Self-Evolving + SKILL 設計的規格書。
> **核心紀律**：本規格書是 **evaluation + 提案**，非授權執行。刪/併改 RESOLVER routing 且不可逆 → 每條標「提案（待核准）」，本 session 除本檔外不動 `.claude/skills/` 內容（advisor + core.md APPLY 破壞性 gate）。
> **使用者前置約束**：仍以 **Sub Agent** 為 workspace 主力（**不採 Agent Teams**）→ 排除 deep-practices-v2 計劃書 Q2/P2-2。

---

## 第零節：分母與方法

### 0.1 分母定案

```
find .claude/skills -name SKILL.md | wc -l  →  27
```

27 個 SKILL.md。`ls` 顯示 28 目錄但其一為 `RESOLVER.md`（非 skill 目錄）。SessionStart 報「27 skills」一致。

**`disable-model-invocation: true`（3 個，僅 `/cmd` 觸發，不參與 description 自動 routing）**：
- `harness-meta`、`security-compliance`、`ship-review`

### 0.2 方法（套用 advisor 校準）

1. `skill-evolution:scan` 是**單 skill** 7 維品質評分，**答不了「誰跟誰重複」** → 自建 **cross-skill 同質性矩陣**。
2. 先**群聚**（5 群）再**群內兩兩比**，不盲掃 27×27。
3. 比對四維：**(a) domain 重疊 (b) trigger 詞碰撞 (c) allowed-tools 重疊 (d) body 功能冗餘**。
4. **merge 判準（鐵律）**：X 併入 Y ⟺ X **無** Y 沒有的獨特能力 **且** trigger/domain 重疊到使用者會混淆。有獨特能力但 skill 數冗 → 優先「降為子命令」而非 delete（保能力減 skill 數）。

---

## 第零節之二：Mnilax「過多 SKILL 反傷」論點接地（使用者指定參考）

> 使用者指出 Mnilax 主張過多 SKILL 影響效率，要求納入整併參考。通讀 9 篇 Mnilax 推文（researcher 抽取 → 主對話親 grep 驗證 5 個關鍵數字屬實），並**對齊本 workspace 實際架構**（advisor 校準：別把高估數字直接套用，也別用架構區分把使用者 steer 解釋掉）。

### 0-2.1 Mnilax 原始主張（親驗屬實）

| 論點 | 數字 | 親驗來源 |
|------|------|---------|
| active skill 甜蜜點上限 | **5–7 個**，超過 = overhead > value | `897712:321` 逐字 |
| 9+ active skills overhead | **~13,500 tokens/task**（每個 SKILL.md 800–2,500 tok「以防萬一」載入）| `556522:97` + `897712:323` |
| 一次裝 23 個 | 第一個 prompt 前耗盡 context window | `897712:297` |
| 規則/條目過多 → compliance 衰退 | 14 條規則 → 76%→52%；CLAUDE.md >200 行急降 | `155938`（與 core.md 既有紀律一致）|
| skill 淘汰標準 | 「adds more context than it returns in value」 | `897712` |

### 0-2.2 架構對齊：Mnilax 的「body 全常駐」模型 vs 本 workspace 的 progressive disclosure

**關鍵區分（決定數字是否適用）**——本 workspace 的 skill 成本分三層：

| 層 | 是否每 session 常駐 | 隨 skill 數成長？ | 本 workspace 實測 |
|----|:---:|:---:|------|
| **skill descriptions**（harness 原生注入；見本 session transcript 頂端「The following skills are available」清單）| ✅ 常駐 | **是** | 27 description 行 = **9,122 字元 ≈ 2,600 tokens**；扣 2 個 DMI（不注入）→ **25 個貢獻常駐稅** |
| **RESOLVER.md**（session-init.sh:261 注入指針，routing 時讀）| 指針常駐 / 本體按需 | 是（27 條目）| 14,127 byte ≈ 3,500 tok，cache 攤銷 |
| **SKILL.md body**（觸發時才 Read）| ❌ 只付用到的 | **否** | 親驗 `session-init.sh:257-261` 只數數量 + 注入指針，body 不常駐 |

**誠實調和（advisor 校準）**：
- Mnilax **頭條數字 13,500 tok/task 對本 workspace 高估**——因 body 採 progressive disclosure（觸發才載），非「9 skills × 1,500 全常駐」。✓
- 但 **Mnilax 原則仍適用，只是機制不同**：
  1. **description 常駐稅真實且隨數量成長**（25 skill × description = ~2,600 tok 每 session，每 turn 重付）。
  2. **routing / decision load 直接適用**——對應 Mnilax「14 條規則 → compliance 76%→52%」（這是**決策負荷**非 token）。本 workspace **已顯化兩個碰撞**（見下）。
  3. **維護成本**：27 個 SKILL.md + GOTCHAS + RESOLVER 同步。

### 0-2.3 Mnilax「太多→混淆」在本 workspace 的自有證據（非外推，是實測碰撞）

本盤點獨立發現的 routing 碰撞，正是 Mnilax decision-load 論點的 workspace 顯化：

| 碰撞 | 證據 | Mnilax 對應 |
|------|------|------------|
| `ship-review` vs `autoresearch:ship` 撞 "ship" 語意 | RESOLVER §214-215 需兩行才勉強區分（交付 vs 審查 gate）| routing 混淆 |
| 三個 "research" 命名相近（research-hub / overnight-research / media-research）| 字面近、domain 正交，靠 Do NOT 互指消歧 | decision load |
| 三個 pilot 近乎同構（haiku/sonnet/opus）| 3 條 description 表達同一概念（mode wrapper）| 「adds more context than value」 |

### 0-2.4 對整併結論的影響（正當化來源更新）

整併**價值真實但量級小於 Mnilax 頭條**。正當化來源從「省 13,500 tok/task」**改為**：
- (a) 降 description 常駐稅（每整併 1 skill 省 ~100 tok/turn × 全 session）；
- (b) routing 清晰度（消除上述實測碰撞）；
- (c) 維護成本。

→ 以 **description 稅 + routing 透鏡**重新看，**三 pilot 整併（M1）是最強槓桿**（3 條 description→1，且消同構冗餘）。原「季度級 defer」與使用者 steer（特意引入 Mnilax）+ Mnilax 原則**方向相反** → 第四節改列**張力攤給使用者裁**（見 D-M1）。

---

## 第一節：群聚地圖（27 SKILL → 8 群）

| 群 | 成員 | 群內疑慮 |
|----|------|---------|
| **G1 Pilots** | haiku-pilot / sonnet-pilot / opus-pilot | 三者近乎同構（model-mode wrapper）→ 最強合併候選 |
| **G2 Research** | research-hub / overnight-research / media-research / autoresearch(+11 subcmd) | 入口重疊；media-research vs media-transcribe 邊界 |
| **G3 Review/Ship/Merge** | review-hub / ship-review / verified-merge | **本任務焦點**；ship-review 路由與 autoresearch:ship 撞名 |
| **G4 Meta/Self-Evolving** | skill-evolution / autoload-evolution / harness-meta / eval-designer | 自我進化閉環三件，邊界需驗 |
| **G5 Security** | security-compliance / iac-review / (autoresearch:security) | 合規 vs 靜態審查 vs app-sec 三層 |
| **G6 Ops** | sre / db-ops / finops | 運維三分，domain 各異 |
| **G7 Gap/Consensus** | gap-vote / token-waste-audit / tech-strategy | 各自獨立分析器 |
| **G8 Atomic 工具** | diagram-gen / spec-implement / media-transcribe / webshot / sia | 單一職責，低重疊 |

---

## 第二節：ship-review 專項評估（任務焦點）

### 2.1 skill-evolution 7 維品質評分

| 維度 | 評分 | 佐證 |
|------|------|------|
| Trigger 清晰度 | 5 | description 雙段 + 4 觸發詞 + 2 Do NOT 反例 |
| 工具宣告完整性 | 5 | `Read, Grep, Glob, Bash` 與實際一致（fan-out 經 Agent 但本體只讀） |
| Guard/Verify | 4 | 有「跳過 fan-out 條件」機械門檻；Phase B/C 合成屬 LLM 判斷 |
| Fallback 路徑 | 5 | Sub-agent 失敗 rollback 表（crash/critical/timeout 三類） |
| 行數合規 | 5 | 117 行 ≪ 350 |
| 版本/日期 | 5 | version 1.0.0 + review-by 2026-08-23 |
| Gotcha 記錄 | 3 | body 內含 1 條明示 Gap（sub-agent failure rollback） |
| **加總** | **32 → Tier A** | 品質本身優秀，**非品質問題** |

> ship-review **品質達 Tier A**，合併與否不取決於品質，取決於**同質性與獨特能力**（下節）。

### 2.2 G3 同質性矩陣（review-hub / ship-review / verified-merge）

| 對 | (a)domain重疊 | (b)trigger碰撞 | (c)tools重疊 | (d)功能冗餘 | 結論 |
|----|:---:|:---:|:---:|:---:|------|
| ship-review × review-hub | 高（都做 code 審查） | 低（ship vs review-hub:） | 100% (R/G/G/B) | 部分（review-hub:commit 三維 vs ship 三 agent fan-out） | 見 2.3 |
| ship-review × verified-merge | 中（都在 ship 前置） | 低 | 100% | 低（verified-merge 純機械 gate 不做 review） | 互補，不併 |
| review-hub × verified-merge | 低 | 低 | 100% | 低 | 互補，不併 |

### 2.3 ship-review 獨特能力鑑定（merge 判準核心）

ship-review 三項能力，逐一驗是否被 review-hub/verified-merge 覆蓋：

| ship-review 能力 | review-hub 覆蓋？ | verified-merge 覆蓋？ | 判定 |
|------------------|:---:|:---:|------|
| ① 三維平行 fan-out（code-reviewer + **security-auditor** + **test-engineer** 一次） | ✗（§Adversarial Review 僅 code 維，無 security/test 並行） | ✗ | **獨特** |
| ② GO / NO-GO 二元決策 | ✗（review-hub 輸出分類清單，不下二元 gate 決策） | △（verified-merge 是 ABORT/PASS 但只對機械 gate，非 review 合成） | **獨特** |
| ③ Rollback plan（觸發條件/步驟/RTO） | ✗ | ✗ | **獨特** |

**結論**：ship-review **擁有三項其他 skill 不覆蓋的獨特能力** → 依 merge 判準鐵律**不可 delete、不可單純併入**。

### 2.4 真正的問題：與 autoresearch:ship 的命名/路由碰撞

| | ship-review | autoresearch:ship |
|--|-------------|-------------------|
| 觸發 | `ship-review` / 準備發布 / 上線前檢查 | `autoresearch:ship` / 交付發布 |
| 內容 | 三 agent fan-out 審查 → GO/NO-GO + rollback | 8-phase universal shipping（code/content/marketing/sales）|
| RESOLVER 區分 | 「上線前 fan-out 審查」 | 「交付發布（PR/部署/內容上線）」 |

兩者皆含 "ship" 語意，使用者說「我要 ship 這個 PR」時 routing 有歧義。**這是真實 gap，但解法是釐清 routing 不是合併**（兩者功能正交：一個是「審查 gate」一個是「交付流程」）。

### 2.5 ship-review 處置提案

| 選項 | 描述 | 利 | 弊 |
|------|------|----|----|
| **A. 維持獨立**（推薦） | 不動，僅在 RESOLVER 加一行 disambiguation（ship-review=審查 gate / autoresearch:ship=交付流程） | 保留 Tier A 品質 + 獨特能力；零破壞 | skill 數不減（但本就不應為減數砍能力） |
| B. 降為 review-hub:ship 子命令 | ship-review 內容移入 review-hub 成 `review-hub:ship` | skill 數 −1；review 系列收斂單一入口 | review-hub 已 204 行 +117 → 逼近 350；DMI 屬性丟失（review-hub 非 DMI）；fan-out 編排與 review-hub 其他子命令異質 |
| C. Delete | 移除 | — | **違反 merge 判準**（有獨特能力）→ 排除 |

**主對話 verdict**：推薦 **A（維持獨立 + RESOLVER disambiguation）**。理由：ship-review 三項獨特能力（multi-agent fan-out / GO-NO-GO / rollback）無替代；降子命令（B）會讓 review-hub 逼近行數上限且混入異質編排邏輯，淨損。唯一真實 gap（與 autoresearch:ship 撞名）用一行 routing 註記解決，成本遠低於合併。

> **使用者已核准（2026-06-07）：選項 A — ship-review 維持獨立**。RESOLVER disambiguation 加註本 session 不執行（保留提案），日後若觸發實際 routing 混淆再補。

---

## 第三節：全 27 SKILL 同質性盤點（群內裁決）

### G1 Pilots — haiku/sonnet/opus-pilot（**最強合併候選**）

| 對 | domain | trigger | tools | 功能冗餘 | 
|----|:---:|:---:|:---:|:---:|
| 三者兩兩 | 高（皆 model-mode wrapper）| 低（haiku/sonnet/opus 互斥）| 100%（R/G/G/B/TodoWrite）| **高**（結構同構：preflight + escalation gate + mode 宣告）|

- **同質性**：三者是同一模板的 model 參數化（281/318/356 行，結構平行）。
- **獨特能力差異**：僅「成本 vs 品質」定位與 escalation 方向不同（haiku→升級 / opus→reverse-advisor）。
- **提案（待核准）**：**M1 — 合併為單一 `pilot` skill + 三子命令**（`pilot:haiku` / `pilot:sonnet` / `pilot:opus`），共用 preflight 骨架，差異部分分節。
  - 利：skill 數 −2（27→25）；消除三份重複 preflight；單一維護點。
  - 弊：合併後單檔可能 >450 行 body（需壓縮共用段）；觸發詞 `haiku`/`sonnet`/`opus` 需保留為 alias。
  - **風險**：pilot 是高頻 mode 切換，routing 改動影響日常 → 須 eval gate（model-fit 回歸）。
  - **判定**：**真合併候選**，但因高頻 routing 影響大 → 列**季度級**，走 autoload-evolution 式 eval gate，不本次執行。

### G2 Research — research-hub / overnight-research / media-research / autoresearch

| 對 | 重疊判定 | 處置 |
|----|---------|------|
| research-hub × overnight-research | 中：都做 deep research；但 overnight 是**無人值守 6-phase 自動提交**，research-hub 是互動式。Do NOT 已互指 | **不併**（自動 vs 互動正交）|
| research-hub × media-research | 低：research-hub Do NOT 明指 Twitter/YT→media-research | **不併**（已清楚分界）|
| media-research × media-transcribe | 低：research（文字分析）vs transcribe（Whisper 逐字稿），Do NOT 互指 | **不併** |
| autoresearch × research-hub | 低：autoresearch 是**迭代收斂器**（modify→verify→keep），非研究抓取 | **不併** |

- **結論**：G2 邊界已用 Do NOT 互指清楚劃分，**無合併候選**。命名 `research-hub`/`overnight-research`/`media-research` 三個 "research" 字面相近但 domain 正交（互動深研/無人值守/外部媒體）。
- **觀察項**：三個 "research" 命名易誤觸；RESOLVER 已有 §「研究」分流表，維持。

### G3 Review/Ship/Merge

見第二節。**review-hub / ship-review / verified-merge 三者互補，無合併**（ship-review 提案 A 維持獨立 + RESOLVER disambiguation）。

### G4 Meta/Self-Evolving — skill-evolution / autoload-evolution / harness-meta / eval-designer

| 對 | domain | 重疊判定 |
|----|--------|---------|
| skill-evolution × autoload-evolution | SKILL 品質進化 vs auto-load 規則進化 | **不併**：標的不同（skills/ vs CLAUDE.md+4 rules）；Do NOT 互指 |
| skill-evolution × harness-meta | SKILL 進化 vs harness 整合入口（HMF/token/add skill）| **部分重疊**：harness-meta 含「Skill 稽核/新增」，與 skill-evolution scan/audit 功能交集 |
| eval-designer × 其他 | eval function 設計（4 條件）| **不併**：獨立設計器，無重疊 |

- **harness-meta × skill-evolution 重疊細查**：harness-meta `:audit`（K×M 稽核/skill 稽核）vs skill-evolution `:scan`/`:audit`（7 維評分/格式合規）。
  - harness-meta 是**整合入口**（HMF drift + token + skill 管理 + self-audit 五合一）；skill-evolution 是**專門 SKILL 品質引擎**。
  - **判定**：harness-meta 的「skill 稽核」應**委派/指向** skill-evolution，非各自實作。**提案 M2（低風險）**：在 harness-meta `:audit` 段加一行指針「SKILL 品質評分 → skill-evolution:scan」，消除功能重複實作（非合併 skill，是去重邏輯）。**可本次執行（≤5 行，非破壞 routing）**。

### G5 Security — security-compliance / iac-review / autoresearch:security

| 對 | 重疊 | 處置 |
|----|------|------|
| security-compliance × iac-review | 低：ISO 27017 合規認證 vs Terraform/K8s 靜態審查。Do NOT 互指（iac→不做合規認證）| **不併** |
| security-compliance × autoresearch:security | 低：合規 evidence chain vs STRIDE/OWASP red-team。Do NOT 互指 | **不併** |
| iac-review × autoresearch:security | 中：都掃安全；但 iac 是 IaC 靜態 lint，autoresearch:security 是 app-sec red-team | **不併**（層次不同）|

- **結論**：三層 security（合規/IaC/app-sec）正交，**無合併**。命名清楚。

### G6 Ops — sre / db-ops / finops

- domain 完全正交（運維/DB/成本），Do NOT 三方互指。**無合併**。

### G7 Gap/Consensus — gap-vote / token-waste-audit / tech-strategy

- gap-vote（多技能投票 executor）/ token-waste-audit（四浪費源診斷）/ tech-strategy（選型 ROI）domain 各異。**無合併**。

### G8 Atomic 工具 — diagram-gen / spec-implement / media-transcribe / webshot / sia

- 五個單一職責工具，零重疊。**無合併**。

---

## 第四節：整併處置總表（提案待核准）

> **使用者裁決（2026-06-07 AskUserQuestion）**：M1 → 只更新規格書不執行；P-A/M2 → 都不執行；ship-review → 同意維持獨立。**本 session 不動 `.claude/skills/`，規格書為唯一交付物**；下方狀態欄已回填裁決結果。

| # | 提案 | 類型 | 風險 | 使用者裁決 | skill 數變化 |
|---|------|------|------|:---:|:---:|
| **P-A** | ship-review 維持獨立 + RESOLVER 加一行 disambiguation（vs autoresearch:ship） | 非破壞（僅加註） | 低 | ✅ ship-review 維持獨立**已核准**；RESOLVER 加註**不執行**（保留提案）| 0 |
| **M2** | harness-meta:audit 加指針指向 skill-evolution:scan（去重複實作邏輯） | 非破壞（≤5 行） | 低 | ⏸️ **不執行**（保留提案）| 0 |
| **M1** | 三 pilot 合併為 `pilot` + 3 子命令 | **破壞 routing** | 中（高頻 mode 切換）| ⏸️ **只記錄不執行**（保留提案，見 D-M1）| −2 |
| — | G2–G8 其餘 | — | — | 無合併（邊界已清楚） | 0 |

### D-M1：三 pilot 整併時程張力（需使用者裁決）

| 方向 | 論據 |
|------|------|
| **支持本次/盡快做**（Mnilax + 使用者 steer）| 三 pilot 近乎同構（mode wrapper）；description 稅最高槓桿（3→1）；使用者特意引入 Mnilax「過多反傷」；Mnilax 淘汰標準「adds more context than value」直接命中 |
| **支持 defer 季度級**（routing 風險）| pilot 是高頻 mode 切換（`/haiku` `/sonnet` `/opus` 日常用）；合併改 routing 須 model-fit eval 回歸 ≥5pp 自動 revert（autoload-evolution 式 gate）；合併單檔逼近 450 行需壓縮共用段 |

> **不自行 flip**（advisor 紀律）：保留 eval-gate caveat，把方向選擇攤給使用者。建議：**核准方向後**走 autoload-evolution 式閉環（eval gate 保護），而非無 gate 直接合併。

**淨結論**：
- 27 SKILL 中，**唯一真合併候選 = 三 pilot（M1）**，Mnilax 透鏡下為最強槓桿；時程（本次 vs 季度級）張力 → **使用者裁**（D-M1）。
- **無任何 skill 達 delete 門檻**（皆有獨特能力或清楚 domain；Mnilax 高估的 per-task token 不構成 delete 理由）。
- ship-review **不合併**（Tier A + 三獨特能力），僅需 RESOLVER disambiguation（P-A）。
- 即時可執行的低風險項：**P-A + M2**（皆非破壞 routing），待使用者核准。
- **整併淨價值定性**：以本 workspace progressive-disclosure 架構，整併省的是 description 常駐稅（~2,600 tok 中每項 ~100 tok/turn）+ routing 清晰度 + 維護，**非** Mnilax 頭條的 13,500 tok/task（該數字基於 body 全常駐模型，本 workspace 不適用）。

---

## 第五節：Self-Evolving 合規（本規格書如何接 SKILL 自我進化回路）

本規格書產出後接入既有閉環（符合 core.md RECORD + skill-evolution Ratchet）：

| Phase | 動作 |
|-------|------|
| OBSERVE | 本盤點即 cross-skill OBSERVE（27 skill domain/trigger/tool/body 全掃）|
| IDENTIFY | 識別 1 真合併候選（M1 pilots）+ 2 低風險去重（P-A/M2）+ 1 routing gap（ship-review vs autoresearch:ship）|
| PROPOSE | 第四節總表（每項標類型/風險/可執行性）|
| TEST（gate） | M1 須 model-fit eval 回歸 ≥5pp 自動 revert（autoload-evolution 式）；P-A/M2 須 healthcheck + grep 接地 |
| APPLY（gate） | **全部待 AskUserQuestion 核准**（破壞性 routing 改動 = core.md APPLY gate）|
| RECORD | 核准執行後追加 `memory/RATCHET.md` + MEMORY session 節 |

### 與 SKILL 設計標準對齊

- merge 判準引用 SKILL description 雙段（Use when + Do NOT）為 routing 真值來源。
- 「降子命令 > delete」原則 = SKILL 設計「保能力減入口」哲學（review-hub/research-hub hub 化先例）。
- 不為「減 skill 數」砍獨特能力 = core.md PROPOSE「不為湊數」+ 反 over-engineering。

---

## 附錄：方法稽核

- 分母：`find .claude/skills -name SKILL.md | wc -l = 27`（親跑）
- DMI 標記：grep `disable-model-invocation: true` → harness-meta / security-compliance / ship-review（親跑）
- 同質性矩陣四維：domain（roster-domain）/ trigger（description Use when）/ tools（allowed-tools）/ body（grep 結構抽驗）全主對話親驗，未經 sub-agent 中介（unverified_success 閘門）
- advisor 校準（2 輪）：①交付物=規格書非執行；scan 答不了 cross-skill；先群聚再比；merge 判準鐵律；分母定 27。②Mnilax 驗錯層修正：description 才是常駐稅（非 body）；routing 碰撞=Mnilax 原則自有證據；pilots 時程張力攤使用者；DMI 一致性 grep
- Mnilax 接地：researcher 通讀 9 篇 → 主對話親 grep 驗 5 數字（5–7 上限 `897712:321` / 13,500 `556522:97` / 23 爆 context `897712:297` / 14 規則 76→52% / 淘汰標準）全屬實；架構對齊後判定頭條數字高估、原則適用
- DMI 親驗修正：初次 grep 誤判 harness-meta 為 DMI → 逐檔 frontmatter 親驗更正：**DMI 僅 security-compliance + ship-review 兩個**（harness-meta 無 DMI，與 transcript 注入清單一致）→ 貢獻 description 常駐稅 = 25 個
- 三層成本親驗：`session-init.sh:257-261` 只注入指針 body 不常駐；description 9,122 字元 ≈ 2,600 tok 常駐；RESOLVER 14,127 byte 按需
- 使用者約束：不採 Agent Teams（排除計劃書 Q2/P2-2）；仍以 Sub Agent 為主力
