# .claude/skills/ 稽核（弱模型長期自主運作視角）

範圍：31 個 skill 目錄 + RESOLVER.md + dependency-graph.json，唯讀盤點。

## 1. SKILL.md 體積排行（bytes, lines）— top 5 最肥

| Rank | bytes | lines | file |
|---|---|---|---|
| 1 | 20857 | 504 | pilot-review/SKILL.md |
| 2 | 20520 | 366 | harness-meta/SKILL.md |
| 3 | 18393 | 338 | media-research/SKILL.md |
| 4 | 16418 | 331 | research-hub/SKILL.md |
| 5 | 16194 | 217 | autoresearch/SKILL.md |

全 31 筆完整清單見下（bytes desc）：
quality-pipeline 15411/406、sre 15197/334、sia 13930/281、autoload-evolution 13161/281、finops 12313/260、review-hub 10859/197、sonnet-pilot 10478/217、multi-mode-skill 10185/134、opus-pilot 8994/162、media-transcribe 8760/212、pr-guard 8592/232、fable-pilot 8549/121、skill-evolution 8500/218、gap-vote 8094/189、haiku-pilot 7407/169、security-compliance 7369/180、verified-merge 7128/150、tech-strategy 6881/180、dreaming-consolidator 6361/103、db-ops 6255/121、ship-review 5022/106、fable5-harness 4913/74、handoff 4494/71、spec-implement 4226/102、overnight-research 4173/82、diagram-gen 2967/74。

**風險**：`pilot-review`（504 行）與 `harness-meta`（366 行）遠超其他 skill，弱模型（Haiku/Sonnet）在長 SKILL.md 中段內容易被截斷/漏讀（core.md OBSERVE「工具輸出截斷不得假設為空」同理適用於長文件本身的注意力衰減，非機械可驗證但為已知弱點）。

## 2. Trigger 重疊 / 職責邊界模糊

各 skill 皆有 `Use when` / `Do NOT use for` 顯式互斥宣告（本身設計良好），但以下配對**字面觸發詞或功能描述高度相似**，弱模型仍可能選錯：

- **`harness-meta` vs `fable5-harness`**（harness-meta/SKILL.md:38-42, fable5-harness/SKILL.md:2-3）：两者都用「四層架構」「L1-L4」字眼；harness-meta 稱「四層架構稽核（L1-L4）」也是其 trigger 之一，僅靠 Do NOT use 反向排除區分（稽核工具箱 vs 契約應用入口），無正向決策樹判準。
- **`media-research` vs `media-transcribe`**（media-research/SKILL.md description, media-transcribe/SKILL.md description）：都吃 Twitter/X、YouTube URL；區分靠「文字分析 vs 完整逐字稿」語意判斷，無 URL pattern/關鍵字層級的機械分流規則。
- **`quality-pipeline` vs `pilot-review` vs `ship-review`**：三者皆為「multi-mode-agent fan-out + haiku/sonnet/opus/fable 分工 + GO/NO-GO 或 verdict」模式，功能骨架幾乎相同，僅審查焦點（品質閘道 / 四維評審 / 上線前）不同，RESOLVER.md 未提供三者共同決策樹（僅各自條列，見 RESOLVER.md:208-235, 259-262 附近段落分散）。
- **`{haiku,sonnet,opus,fable}-pilot`**：四份 description 為同一模板複製（僅代換模型名），"routine tasks" / "cost-sensitive" 等排除詞無具體檔案數/token 數字門檻寫在 description 層（門檻藏在各 SKILL.md 內文，如 haiku-pilot/SKILL.md:100-101），弱模型讀 description 選 skill 時看不到門檻。
- **`verified-merge` vs `pr-guard` vs `ship-review`**：merge/PR gate 職責相近，靠文字排除（verified-merge Do NOT use for 開 PR/commit；pr-guard Do NOT use for 一般 review/gate-then-merge），無單一速查表整合三者觸發優先序。

## 3. 硬編碼模型名 / effort（換模型世代即過時風險）

Grep 結果 98 處命中版本化模型名（claude-sonnet-4-6 / opus-4-8 / haiku-4-5 / fable-5 等），3 處硬編碼 effort 值。**多數命中帶有「重驗機制」或「provenance 標記」**（如 harness-meta/SKILL.md:53-59 模型事實基準表本身设计为需重驗、sonnet-pilot/SKILL.md:21 明寫 "evaluator 為當時的 Opus 4.7——provenance 保留，重跑時改用現役最強 evaluator"），非全部裸硬編碼。

**真正無重驗保護、description 層直接寫版本號的高風險項**：
- opus-pilot/SKILL.md:3 — description 直寫 "Opus 4.8 ceiling-elevation mode"
- sonnet-pilot/SKILL.md:3 — description 直寫 "Sonnet 4.6 quality-first mode"
- haiku-pilot/SKILL.md:3 — description 直寫 "Haiku 4.5 cost-first mode"
- fable-pilot/SKILL.md:3 — description 直寫 "Fable 5（Mythos-class）"
- 影響：這 4 個 skill 的**唯一觸發判準之一是 description 裡的版本字串**；模型世代升級（如 Sonnet 5 已於 harness-meta/SKILL.md:55, 66 出現且標注「CC `sonnet` alias 現解析至此」）後，若 pilot skill description 未同步更新，`Use when user types sonnet, sonnet-pilot, Sonnet mode` 這類**觸發詞本身仍成立**但 skill 內文假設的定價/能力基準（sonnet-pilot/SKILL.md:21 的 A/B/C benchmark）已對不上新世代 Sonnet 5，弱模型無法自行察覺基準過期。
- sia/REFERENCE.md:44-46, 66-67 — `haiku→claude-haiku-4-5`、`sonnet→claude-sonnet-4-6`、`opus→claude-opus-4-8` 映射表硬編碼於獨立 REFERENCE.md，無 grep 重驗腳本掛鉤（harness-meta/SKILL.md:331 有一行類似 grep 但只驗 harness-meta 自身）。
- finops/SKILL.md:129-131 定價表（Opus $5/$25、Sonnet $3/$15、Haiku $1/$5）无 provenance 日期標記，若定價調整需人工全文搜尋更新。

effort 硬編碼（3 處，風險低）：opus-pilot/SKILL.md:103、haiku-pilot/SKILL.md:96、sonnet-pilot/SKILL.md:132 — 均已 cite `.claude/refs/pilot-shared-preflights.md §E` 作 canonical source，屬「規則型引用」非裸寫死，風險可控。

## 4. Dead path 機械驗證

**結論：0 個真正失效引用。** 初步 grep 命中 18 筆疑似 dead path，逐一 `test -f` 後發現全部是**相對於 workspace root 的 bash 命令路徑**（如 `scripts/healthcheck.sh`、`scripts/measure.sh`、`scripts/paywall_bypass.py`），而非 skill 目錄本地相對路徑；經 `ls /Users/zeuik/cc-workspace/scripts/` 核對全部檔案實際存在。`harness-meta/SKILL.md:167` 的 `research/agent-harness/dream-YYYY-MM-DD.md` 為輸出檔名模板（日期佔位符），非死連結。

**隱性風險（非「dead」但屬弱模型陷阱）**：多個 SKILL.md（autoload-evolution、autoresearch、fable-pilot、fable5-harness、harness-meta、media-research、media-transcribe、multi-mode-skill、review-hub、ship-review、spec-implement、verified-merge）內的 `bash scripts/xxx.sh` 命令**均隱含假設 cwd = workspace root**，SKILL.md 內文無顯式聲明此前提。若弱模型 sub-agent 在非 root cwd（如已 cd 進某子目錄）執行，會得到 "No such file or directory" 且無自我糾錯線索（找不到會誤判為腳本不存在而非 cwd 錯誤）。建議：至少一處 SKILL.md 加註「假設 cwd = workspace root，執行前 pwd 確認」。

## 5. 結構完整性缺失

- **`fable5-harness`**：缺 `METADATA.json` 與 `GOTCHAS.md`（其餘 30 個 skill 均兩者齊備）。此 skill 屬四層行為契約入口，缺 METADATA.json 意味它未被納入某些依賴自動化流程（如 skill-evolution:scan 若依賴 METADATA.json 判讀 roster，此 skill 可能被漏掃）；缺 GOTCHAS.md 意味無已知失敗模式記錄，長期自主運作若踩坑無處查詢。

## 6. 弱模型誤讀風險：無判準抽象指令

全文搜尋常見模糊詞（適當地/妥善/盡量/合理/清晰/優雅等），**命中率遠低於預期**——workspace 既有規則（output-discipline.md、core.md）已推動 skill 作者普遍採用量化門檻寫法（如 finops CDN hit rate ≥90%/95%/97%）。抽樣後 top 候選（非 10 例，僅 6 例達標，其餘為 template 佔位符或已有數字定義而排除）：

1. `pilot-review/SKILL.md:150` — 「這個方案的 LLM 使用是否合理？」（D1 cost 審查 prompt）無 token/次數門檻定義「合理」。
2. `pilot-review/SKILL.md:183` — 「可維護性：命名清晰、不必要的複雜度」（D2 品質審查 prompt）"清晰"/"不必要"無 lint 規則或範例錨定。
3. `pilot-review/SKILL.md:221` — 「有沒有更好的架構選擇？」（D3 架構審查 prompt）無比較基準或 ADR 模板外的具體評分軸。
4. `quality-pipeline/SKILL.md:195` — 「輸出格式（簡潔）」未 cite output-discipline.md 150 字上限，讀者需自行猜測「簡潔」程度。
5. `finops/SKILL.md:71` — 「多雲套利審慎」（表格描述，非執行指令）"審慎" 無操作定義，僅暗示需完整 ROI 計算但未給觸發門檻。
6. `autoload-evolution/SKILL.md:262` — 「不得自行評估規則變更品質；必須委派 reviewer agent」本身是防範模糊自評的**正例**（非模糊指令，收錄以對照說明此 skill 已自我修正該風險模式）。

**結論**：模糊指令並非本次稽核最大風險源；真正弱模型風險集中在 **#2 trigger 重疊**（四對職責相近 skill 缺正向決策樹）與 **#3 版本硬編碼 description**（4 個 pilot skill 觸發詞穩定但基準內容會隨模型世代默默過期，無自動偵測）。
