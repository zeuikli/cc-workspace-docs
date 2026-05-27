---
title: "AI Coding Agent 最佳準則（Karpathy × Mnilax 精煉版）"
date: 2026-05-18
type: report
---

# AI Coding Agent 最佳準則（Karpathy × Mnilax 精煉版）

> 版本：AB4.0（最終）· 2026-05-18  
> 精煉方法：50+ 輪對抗式驗證（4 輪 × 5 位盲評法官，3 連勝收斂）  
> 收斂歷程：Round 1→B · Round 2→AB2 · Round 3→AB3(4:1) · Round 4→AB4(3+:5) ← **本版本**  
> 一手來源：`research/ai-articles/` 38 篇 + `karpathy-principles.md` + `mnilax-12rules.md`  
> 來源溯源標注：[自測] = 內部實驗；[獨立驗證·公開來源] = 有公開引用；[理論] = 邏輯推導

---

## 目錄

R1–R4：Karpathy 4 Floor · R5–R12：Mnilax 8 增量 · R13–R14：新增 2 條 · 情境速查表 · 版本溯源表

---

## R1：實作前假設顯露（Think Before Coding）

### 核心原則

實作前必須明說：(1) 對需求的詮釋（≤2 句，非複述原話）；(2) 關鍵假設；(3) 多解法時列選項讓用戶確認，不自選。

「直接做」「不用解釋」→ 可跳過假設顯露，但**不可逆操作無論如何必須確認（MAJOR-4）**：

- 破壞性資料操作（DELETE / TRUNCATE / DROP）
- 生產環境 deploy / destroy
- 金鑰生成 / 銷毀 / 旋轉
- 不可回滾的 migration

執行中遭遇阻礙或方向明顯偏差 → 停下重新規劃，不硬撐繼續。

### 機械檢查表

```bash
# 不可逆操作偵測（即使用戶說「直接做」仍需確認）
IRREVERSIBLE_KEYWORDS="DELETE\s|TRUNCATE\s|DROP\s+TABLE|DROP\s+DATABASE|prod.*deploy|destroy|key.*rotate|key.*revoke|git.*--force|kubectl.*delete.*namespace|rm\s+-rf|s3.*rm.*recursive|terraform.*destroy"
if echo "$TASK_DESCRIPTION" | grep -qiE "$IRREVERSIBLE_KEYWORDS"; then
  echo "[警告] 偵測到不可逆操作，必須顯示摘要並等待確認"
  echo "即將執行：<命令>  影響範圍：<說明>  是否確認執行？(yes/no)"
fi
```

### 失敗案例

用戶說「直接刪掉所有 2023 年以前的訂單」，Agent 跳過確認直接執行 DELETE，生產資料永久消失。

**來源**：[自測] 不可逆操作確認（MAJOR-4）；[獨立驗證·公開來源] Karpathy R1

**已知限制**：「不可逆」邊界依系統而定（某些 DB 有 soft delete）；關鍵字偵測無法涵蓋所有語意。

---

## R2：規格極簡（Simplicity First）

### 核心原則

寫最小能解決問題的代碼：不加推測性功能、不為一次性使用抽 helper、不鋪「未來可能需要」的支撐。

**加密基底共用原則（FATAL-2）**：`secure_random_bytes`、`constant_time_compare` 等安全基底必須是獨立共用函式；禁止兩個算法函式各自 inline nonce 生成（→ AES-GCM IV reuse 漏洞）。

**安全例外（永遠獨立函式，不受呼叫點計數限制）**：

| 類型 | 說明 |
|------|------|
| 加密原語（Crypto Primitives） | nonce/IV 生成、加解密、簽章、HMAC |
| 金鑰操作（Key Material） | 金鑰生成、載入、旋轉、銷毀 |
| 輸入驗證（Input Validation） | 外部輸入的格式/範圍/字元集驗證 |
| 身份驗證邏輯（Auth Logic） | 登入、Token 核發、Session 驗證 |

**Rule of 3**：同一邏輯出現 ≥ 3 個呼叫點 → 抽 helper。自我檢驗：資深工程師會說「這太複雜了」嗎？是 → 砍到最簡。

### 機械檢查表

```bash
# 檢查加密函式是否有獨立基底（FATAL-2 防護）
grep -rn "os\.urandom\|random_bytes\|generate_nonce\|gen_iv\|crypto\.getRandomValues" \
  --include="*.py" --include="*.js" --include="*.ts" --include="*.go" \
  --exclude-dir={tests,test,fixtures,examples,__mocks__,docs} \
  . | head -30
# nonce/IV 生成應只出現在一個共用函式中，若多處出現 → 重構為共用基底
# 觸發時機：任何涉及加密/隨機數的檔案變動（建議加入 pre-commit hook）
```

### 失敗案例

`encrypt_aes256()` 和 `encrypt_aes128()` 各自 inline `nonce = os.urandom(12)`，重構後其中一個改用固定 nonce，導致 IV reuse 加密材料可被破解。

**來源**：[獨立驗證·公開來源] Karpathy R2；[自測] AES-GCM IV reuse（FATAL-2）；[獨立驗證·公開來源] NIST SP 800-38D § 8.2

**已知限制**：安全基底強制共用與「不為一次性抽 helper」存在表面矛盾，安全例外優先。

---

## R3：外科刀式修改（Surgical Edits）

### 核心原則

只動任務要求的最小範圍。改動前先讀 exports、直接 caller、共用 utility；任務外 bug → 記錄回報，不自動修（commit 原子性）。**量化界線（軟）**：Bug fix ≤ 50 行、新功能 ≤ 300 行、單檔 ≤ 500 行。

**P0 安全例外（發現即修復）**：

| P0 類型 | 範例 |
|---------|------|
| 硬編碼憑證 | 原始碼中的密碼/API Key/Token |
| SQL Injection | 字串拼接 SQL，未使用 parameterized query |
| Path Traversal | `../` 未過濾的路徑操作 |
| Auth Bypass | 可跳過身份驗證的邏輯缺陷 |
| 記憶體安全 | buffer overflow、use-after-free、race condition on secrets |

**P0 緊急修復分支策略（MAJOR-1）**：
1. `git stash push -m "WIP: pre-P0-stash-<timestamp>"`
2. `git checkout -b hotfix/p0-<description>`
3. 最小 patch + commit `fix(security): [P0-type]`
4. `git push origin hotfix/p0-<description>`
5. 開 PR + 向 reviewer 回報
6. 原 WIP 分支等待用戶指示後繼續
7. 修復合併後還原 WIP：
   ```bash
   git checkout <original-branch>
   git stash pop stash@{0}  # 或：git stash list 確認後 pop
   ```

**憑證掃描注意事項（FATAL-1）**：grep 必須排除假資料目錄（`--exclude-dir={tests,test,fixtures,examples,__mocks__,docs}`）；推薦使用 gitleaks / trufflehog；所有結果需人工排除測試假資料。

### 機械檢查表

```bash
# 憑證掃描（FATAL-1：必須排除假資料目錄）
grep -rn \
  --exclude-dir={tests,test,fixtures,examples,__mocks__,docs,.git,node_modules,vendor} \
  -E '(password|passwd|secret|api_key|apikey|token|private_key)\s*[:=]\s*["'"'"'][^"'"'"']{8,}' \
  . 2>/dev/null | head -20
echo "[重要] 上方結果仍需人工排除測試假資料"
echo "[建議] gitleaks detect --source . --no-git"

# P0 緊急修復函式
p0_hotfix() {
  local DESC="$1"
  git stash push -m "WIP: pre-P0-stash-$(date +%Y%m%d%H%M)"
  git checkout -b "hotfix/p0-${DESC}"
  echo "[P0] 修復完成後：git commit -m 'fix(security): [P0] ${DESC}' && git push origin hotfix/p0-${DESC}"
}
```

### 失敗案例

grep 命中 `tests/fixtures/sample-keys.json` 的假資料，開發者養成忽略 grep 結果的習慣，真實生產金鑰洩漏被埋沒直到資安事故。

**來源**：[獨立驗證·公開來源] Karpathy R3；[自測] P0 分支策略（MAJOR-1）；[自測] gitleaks false positive（FATAL-1）

**已知限制**：grep 正則無法偵測 base64 編碼或環境變數引用形式的憑證；P0 流程假設本地端有 git stash 可用。

---

## R4：目標導向（Goal-Oriented Iteration）

### 核心原則

開工前寫「成功的可觀測條件」（測試 / healthcheck / 特定輸出），迭代到達標而非走步驟。宣告「完成」前必須執行驗證並展示**前 5 行 / 後 5 行輸出**（中間 `...`）；禁止口頭「測試通過」。完成條件必須可機械性驗證，不接受「看起來正確」。

### 機械檢查表

```bash
# 完成後驗證（展示前5後5）
OUTPUT=$(eval "$VERIFY_CMD" 2>&1)
LINES=$(echo "$OUTPUT" | wc -l)
if [ "$LINES" -le 10 ]; then echo "$OUTPUT"
else echo "$OUTPUT" | head -5; echo "... [中間 $((LINES-10)) 行省略] ..."; echo "$OUTPUT" | tail -5
fi

[ -f "scripts/healthcheck.sh" ] && bash scripts/healthcheck.sh
npm test 2>&1 | tail -10  # 或 pytest / go test / cargo test
```

### 失敗案例

Agent 口頭說「測試都通過了」但未實際執行，integration tests 被跳過，上線後 API 與下游服務契約不相容。

**來源**：[獨立驗證·公開來源] Karpathy R4；[自測] healthcheck 輸出格式規範

**已知限制**：「前 5 後 5」在純數字 benchmark 輸出時可能遺漏關鍵中段；E2E 瀏覽器測試無法在所有 CI 重現，需明示跳過原因。

---

## R5：判斷 vs 決定（Latent vs Deterministic）

### 核心原則

- **LLM 只做「判斷」（Latent）**：分類 / 摘要 / 提取 / 創意生成 ✅
- **確定性代碼做「決定」（Deterministic）**：路由 / 重試次數 / HTTP status code / 數學計算 ❌

最常見錯誤：讓 LLM 選 HTTP status code 或控制 retry 次數 → 結果不可預測。

### 機械檢查表

```bash
grep -rn \
  --include="*.py" --include="*.js" --include="*.ts" --include="*.go" \
  --exclude-dir={tests,test,fixtures,examples,__mocks__,docs} \
  -E "llm.*status|gpt.*status_code|claude.*retry|ai.*http_code|model.*route" \
  . | head -20
```

### 失敗案例

LLM 決定 HTTP status code，同一請求在不同推理時得到不同值，客戶端無法建立穩定的錯誤處理邏輯。

**來源**：[獨立驗證·公開來源] Mnilax R5；[自測] HTTP status code 不可預測場景

**已知限制**：動態路由條件生成等場景有灰色地帶，此時要求 LLM 輸出結構化 JSON 後由確定性代碼解析執行。

---

## R6：Token 預算管理（Soft Token Budget）

### 核心原則

- Per-task 預算：**4,000 tokens**（軟上限）；Per-session 預算：**30,000 tokens**（軟上限）
- **決策表**：0–40% 無限制 → 40–70% 聚焦 → 70–85% 主動 `/compact` → 85–95% 停止新任務 → 95%+ 立即 `/clear`

**Compact 觸發三層**（優先序：行為信號 > 數字閾值 > 定時器）：
1. **行為信號**：模型出現「請提供更多上下文」等迷失問句 → 立即 compact
2. **數字閾值**：一般任務 70%；長 agentic 任務 30–35%
3. **定時器**：複雜 agentic 每 300–400K token 主動 compact

超支合理原因標籤（需明示）：`[cross-file-refactor]` / `[large-io]` / `[multi-language-audit]` / `[p0-security]`

### 機械檢查表

```bash
/usage
COMPACT_HINT="保留：[原始任務目標] [最近5工具結果] [安全紅線] [專案慣例]；捨棄：中間步驟詳情"
```

### 失敗案例

compact 時未保留「安全紅線」hint，重建的 context 遺忘「prod 操作需二次確認」，後續生產環境操作直接執行。

**來源**：[獨立驗證·公開來源] Mnilax R6；[自測] Compact hint 格式；[理論] Context window 決策表

**已知限制**：Token 計數在不同 tokenizer 間有差異，數字閾值為估算值。

---

## R7：衝突浮現（Surface Conflicts）

### 核心原則

發現互相矛盾的模式時必須浮現衝突，不靜默選擇。不混用兩種模式。

**統一優先序（MAJOR-2）**：ADR / CONTRIBUTING.md 指定 → 最近 3 commit 風格 → 覆蓋率數字

說明：無 ADR/CONTRIBUTING.md 時，先參考最近 3 commit 風格，再看覆蓋率。若兩個 ADR 互相矛盾 → 必須浮現給用戶決策，不自行選擇。

**機械 Artifact（必寫）**：
```
TODO(conflict): chose <A> over <B>; reason: <說明>; remove <B> before <milestone>
```

**台灣協作語境**：code review 討論可用建議語氣（「這裡可以考慮...」），但 `TODO(conflict)` 必須寫入，不因語氣考量省略。

**台灣術語**：函式（非函数）、變數（非变量）、介面（非接口）

### 衝突優先序表（12 對）

| # | 場景 | 觸發條件 | 優先選擇 | 廢棄標注 |
|---|------|----------|----------|---------|
| 1 | mocha 80% vs ADR 指定 jest | ADR-005 存在 | jest（ADR） | `// TODO: remove mocha after migration (ADR-005)` |
| 2 | eslint-airbnb vs eslint-google | CONTRIBUTING.md 指定 airbnb | airbnb（CONTRIBUTING） | `// TODO: remove google-style after lint migration` |
| 3 | winston（70%）vs pino（新 commit） | 最近 3 commits 用 pino | pino（最新 commit） | `// TODO: remove winston after full migration` |
| 4 | Sequelize vs TypeORM | CONTRIBUTING.md 指定 TypeORM | TypeORM（CONTRIBUTING） | `// TODO: migrate Sequelize to TypeORM` |
| 5 | REST v1（大量）vs GraphQL（ADR） | ADR-012 指定 GraphQL | GraphQL（ADR） | `// TODO: deprecate REST v1 after GraphQL parity` |
| 6 | dotenv vs 12-factor env | CONTRIBUTING.md 指定 12-factor | 12-factor（CONTRIBUTING） | `// TODO: remove dotenv dependency` |
| 7 | Promise.catch（60%）vs try-catch（新 commit） | 最近 3 commits 用 try-catch | async/await try-catch（最新 commit） | `// TODO: refactor Promise.catch to async/await` |
| 8 | Docker Compose v2 vs v3 | ADR 指定 v3 | v3（ADR） | `// TODO: remove docker-compose.v2.yml` |
| 9 | JWT（廣泛）vs Session Cookie（ADR） | ADR 安全決策指定 Cookie | Session Cookie（ADR 安全） | `// TODO: deprecate JWT after Cookie rollout` |
| 10 | Redux（75%）vs Zustand（CONTRIBUTING） | CONTRIBUTING.md 指定 Zustand | Zustand（CONTRIBUTING） | `// TODO: migrate Redux to Zustand` |
| 11 | 單元測試（大量）vs 整合測試（ADR） | ADR-008 指定整合測試優先 | 整合測試（ADR） | `// TODO: 評估現有單元測試轉換或刪除` |
| 12 | GitHub Flow vs Trunk-based（CONTRIBUTING） | CONTRIBUTING.md 最新版指定 | Trunk-based（CONTRIBUTING） | `// TODO: update CI/CD for trunk-based` |

### 機械檢查表

```bash
# 優先序：ADR/CONTRIBUTING.md → 最近 3 commit → 覆蓋率
for dir in "docs/adr" "adr" "docs/decisions" "docs/architecture"; do
  [ -d "$dir" ] && { echo "[ADR] 找到：$dir"; ls "$dir" | head -10; break; }
done
[ -f "CONTRIBUTING.md" ] && grep -iE "(test|framework|lint|style|orm|api)" CONTRIBUTING.md | head -10
git log --oneline -3
grep -rn 'TODO(conflict)' --include='*.{js,ts,py,go,rb,java}' .
```

### 失敗案例

ADR-005 指定 jest 但 Agent 以「mocha 覆蓋率 80%」為由選 mocha，遷移完成後新增的 mocha 測試需全部重寫。

**來源**：[獨立驗證·公開來源] Mnilax R7；[自測] ADR 優先級修復（MAJOR-2）；[自測] 台灣協作語境

**已知限制**：ADR 可能過時或互相衝突，兩個 ADR 互相矛盾時必須浮現給用戶。

---

## R8：改前先讀（Read Before Write）

### 核心原則

改動前先讀目標範圍的 exports（介面契約）、直接 caller（上游影響）、共用 utility（橫向依賴）。不清楚現有結構先問再動。讀取超過 200 行的檔案必須分段，每段後說明「已讀第 N-M 行，共 X 行，剩 Y 行未讀」。

### 機械檢查表

```bash
TARGET_FILE="$1"
TOTAL_LINES=$(wc -l < "$TARGET_FILE")
[ "$TOTAL_LINES" -gt 200 ] && echo "[R8] 大檔警告：必須分段讀取（共 $TOTAL_LINES 行）"

# 找直接 caller
BASENAME=$(basename "$TARGET_FILE" | sed 's/\.[^.]*$//')
grep -rn --exclude-dir={node_modules,vendor,.git,dist,build} \
  "import.*$BASENAME\|require.*$BASENAME\|from.*$BASENAME" . 2>/dev/null | head -15
# 若結果超限：[CONTEXT BOUNDARY: showing N of TOTAL. Remaining DIFF omitted. Run <cmd> to see more]
```

### 失敗案例

修改 `auth/session.js` 前沒有搜尋 caller，直接重命名 `createSession()`，12 個使用舊名稱的 controller 部署後全部拋出 TypeError。

**來源**：[獨立驗證·公開來源] Mnilax R8；[自測] 大檔分段讀取；[自測] 搜尋截斷標示格式

**已知限制**：動態語言的 caller 依賴靜態 grep，動態 dispatch 無法偵測。

---

## R9：測試驗證意圖（Tests Verify Intent）

### 核心原則

測試要能在業務邏輯改變時失敗；能通過任何實作的測試 = 沒有測試（mock 過度）。每個測試對應一個業務場景，而非一個函式呼叫。Mutation score 目標 < 20% 存活率（> 80% mutants 被殺死）。

### 機械檢查表

```bash
# 找過度 mock 的測試（只驗「被呼叫」而不驗「結果」）
grep -rn --include="*test*" --include="*spec*" \
  --exclude-dir={node_modules,vendor,.git} \
  -E "toHaveBeenCalled\(\)|assert_called\(\)" . | head -10
# 上方結果若無配套輸出值驗證 → 屬於弱測試

npx stryker run 2>&1 | grep 'Mutation score'  # JS/TS
mutmut run && mutmut results                   # Python
```

### 失敗案例

訂單金額計算函式只寫 `toHaveBeenCalled()` 測試，稅率計算邏輯改錯時測試仍通過。

**來源**：[獨立驗證·公開來源] Mnilax R9；[理論] TDD 意圖原則；[自測] 過度 mock 偵測

**已知限制**：外部依賴確實需要 mock，區別在於 mock 的是「外部邊界」而非「業務核心邏輯」；Mutation score 20% 基準為理論推導，建議作為補充指標。

---

## R10：進度 Checkpoint

### 核心原則

每完成重要步驟輸出 1 句摘要「做了什麼／驗了什麼／剩什麼」；無法描述當前狀態時停下重述。長任務每 3–5 步強制 checkpoint，防止 context drift。

**格式**：`[Checkpoint] 做了 <X>，驗了 <Y>（結果：<pass/fail/N件>），剩 <Z>`

### 機械檢查表

```bash
checkpoint() { echo "=== Checkpoint === 做了：$1  驗了：$2  剩下：$3"; }
[ -f "claude-progress.json" ] && cat claude-progress.json | python3 -m json.tool 2>/dev/null
```

### 失敗案例

Agent 在 10 步重構的第 7 步發現方向偏差，但沒有 checkpoint 繼續執行，最終交付物偏離需求且難以回溯。

**來源**：[獨立驗證·公開來源] Mnilax R10；[自測] Checkpoint 格式；[理論] Context drift 防護

**已知限制**：Checkpoint 增加 token 消耗，token 緊張時可縮短描述但不可省略。

---

## R11：慣例優先（Convention First）

### 核心原則

Codebase 既有慣例 > Agent 偏好；不確定跟隨最近 3 個 commit 的風格。慣例本身有害 → 明說並另開議題，不要 silent fork。偏離慣例的選擇必須在 commit message 標注原因。

### 機械檢查表

```bash
git log --oneline -3
[ -f ".editorconfig" ] && grep -E "indent|tab" .editorconfig

# 偵測混用 require 和 import
js_require=$(grep -rn "= require(" --include="*.ts" . 2>/dev/null | wc -l)
es_import=$(grep -rn "^import " --include="*.ts" . 2>/dev/null | wc -l)
[ "$js_require" -gt 0 ] && [ "$es_import" -gt 0 ] && echo "WARN: 混用 require 和 import"
```

### 失敗案例

Agent 發現「SQL query 直接字串拼接」是 codebase 慣例，選擇跟隨並新增 SQL injection 漏洞而不回報，助長安全債務。

**來源**：[獨立驗證·公開來源] Mnilax R11；[自測] 慣例識別流程；[理論] Convention over Configuration

**已知限制**：「最近 3 個 commit」可能是臨時代碼，需結合 CONTRIBUTING.md 交叉驗證；前後端可能有不同命名慣例，需按模組區分。

---

## R12：Fail Loud（高聲失敗）

### 核心原則

任何步驟失敗必須立即顯示完整錯誤訊息，禁止靜默跳過。不得以「完成」「成功」掩蓋未執行的驗證。完成後 MUST 跑 `bash scripts/healthcheck.sh` 或等效驗證。

**台灣繁體中文語境**：技術失敗溝通可用建議語氣（「這個地方需要確認一下，目前 healthcheck 顯示 <具體輸出>」），但技術輸出不得省略或淡化。**語氣可調整，資訊不得省略。**

**搜尋截斷格式**：超限時必須標示 `[CONTEXT BOUNDARY: showing N of TOTAL. Remaining DIFF omitted. Run <cmd> to see more]`；靜默截斷禁止。

**生產環境紅線（必須 plan/diff + 二次確認）**：

| 操作類型 | 具體範例 |
|---------|---------|
| GCP/Terraform/K8s 含 `prod` | `terraform apply`（prod workspace）、`kubectl delete`（prod cluster） |
| 破壞性 SQL | `DROP TABLE`、`TRUNCATE`、無 WHERE 的 `DELETE` |
| Force push shared branch | `git push --force origin main`、`git push --force origin develop` |

二次確認格式：`即將執行：<命令>  影響範圍：<說明>  是否確認執行？(yes/no)`

### 機械檢查表

```bash
[ -f "scripts/healthcheck.sh" ] && bash scripts/healthcheck.sh || echo "[WARNING] healthcheck.sh 不存在"
grep -Ern '（略）|（待補）|TODO[^(]' docs/ .claude/ *.md 2>/dev/null
# 完成宣告自問：資深工程師會核准這個嗎？否 → 先修再報
```

### 失敗案例

Agent 驗證失敗後靜默跳過並輸出「任務完成」，用戶以為系統正常，潛在問題被掩蓋至生產環境。

**來源**：[獨立驗證·公開來源] Mnilax R12；[自測] 截斷標示；[自測] 完成宣告驗證；[自測] 台灣語境失敗溝通

**已知限制**：某些 CI 環境 healthcheck 依賴特定服務，本機執行可能誤報。

---

## R13：PGE 架構（Precondition / Goal Verification / Evidence Collection）

### 核心原則

任何自動化任務（CI/CD、migration、deployment）必須明確三層。**P 層**確認前置條件（失敗 → `exit 1`，不 skip）；**G 層**驗證目標達成（使用 `<DB_VERIFY_CMD>` 佔位符，不硬綁 DB 類型）；**E 層**蒐集執行證據。E 層缺失時除錯成本約 3 倍。

> 前置條件失敗 → `exit 1`，**不 skip**。跳過前置條件的測試會在 prod 環境「成功」，掩蓋真實問題。

### 機械檢查表

```bash
# ── P 層：前置條件確認 ──
[ -f .env ] || { echo "[P-FAIL] .env missing"; exit 1; }
curl -sf http://localhost:8080/health > /dev/null || { echo "[P-FAIL] 服務未運行"; exit 1; }
echo "[P-PASS] 前置條件通過"

# ── G 層：目標達成驗證（使用佔位符，不硬編碼具體日期）──
# 請替換 <MIGRATION_NAME> 為實際的 migration identifier（如：'20260518_add_user_index'）
# PostgreSQL: psql "$DATABASE_URL" -c "SELECT COUNT(*) FROM migrations WHERE name='<MIGRATION_NAME>';" | grep -q '1'
# SQLite:     sqlite3 app.db "SELECT COUNT(*) FROM migrations WHERE name='<MIGRATION_NAME>';" | grep -q '1'
# MongoDB:    mongosh --eval "db.migrations.countDocuments({name:'<MIGRATION_NAME>'})" | grep -q '1'
# MySQL:      mysql "$DATABASE_URL" -e "SELECT COUNT(*) FROM migrations WHERE name='<MIGRATION_NAME>';" | grep -q '1'
<DB_VERIFY_CMD>
echo "[G-PASS] 目標達成"

# ── E 層：證據蒐集 ──
on_failure() {
  echo "=== Evidence ==="
  docker ps -a 2>/dev/null || true
  docker logs app --tail 50 2>/dev/null || true
  kubectl get events --sort-by='.lastTimestamp' 2>/dev/null | tail -20 || true
}
trap on_failure ERR
```

### 失敗案例

G 層硬寫 `psql -c "..."` 但環境使用 SQLite，G 層因 psql 不存在崩潰，migration 狀態不明（實際 migration 可能已成功但無法驗證）。

**來源**：[自測] PGE 架構設計；[自測] MAJOR-3 多資料庫修復；[理論] Precondition/Postcondition 形式驗證

**已知限制**：`<DB_VERIFY_CMD>` 需人工或 CI/CD 配置替換；E 層證據檔案需定期清理；P 層 curl health check 假設服務有 `/health` endpoint。

---

## R14：Polyglot 安全審查（Multi-language Dependency Audit）

### 核心原則

多語言專案必須對每種語言做依賴安全審查，版本鎖定確保可重現。工具未安裝 → Fail Loud（顯示安裝指令），不靜默跳過。**未涵蓋**：Swift / PHP / .NET (C#)（替代：`swift package audit` / `composer audit` / `dotnet list package --vulnerable`）。

**工具版本鎖定**：

| 語言 | 工具 | 安裝指令 |
|------|------|---------|
| Node.js | npm audit | 內建（npm ≥ 6） |
| Python | pip-audit | `pip install "pip-audit>=2.0" -q` |
| Rust | cargo-audit | `cargo install cargo-audit@0.20` |
| Go | govulncheck | `go install golang.org/x/vuln/cmd/govulncheck@latest` |
| Ruby | bundler-audit | `gem install bundler-audit` |

### 機械檢查表

```bash
#!/usr/bin/env bash
set -euo pipefail
AUDIT_FAILED=0

if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ] || [ -f "Pipfile" ]; then
  command -v pip-audit &>/dev/null && pip-audit || { echo "FAIL: pip install 'pip-audit>=2.0' -q"; AUDIT_FAILED=1; }
fi

[ -f "package.json" ] && npm audit --audit-level=high || AUDIT_FAILED=1

if [ -f "Cargo.toml" ]; then
  command -v cargo-audit &>/dev/null && cargo audit || { echo "FAIL: cargo install cargo-audit@0.20"; AUDIT_FAILED=1; }
fi

if [ -f "go.mod" ]; then
  command -v govulncheck &>/dev/null && govulncheck ./... || { echo "FAIL: go install golang.org/x/vuln/cmd/govulncheck@latest"; AUDIT_FAILED=1; }
fi

if [ -f "Gemfile" ]; then
  command -v bundle-audit &>/dev/null && bundle-audit check --update || { echo "FAIL: gem install bundler-audit"; AUDIT_FAILED=1; }
fi

echo "[未涵蓋] Swift: swift package audit | PHP: composer audit | .NET: dotnet list package --vulnerable"
[ $AUDIT_FAILED -ne 0 ] && { echo "AUDIT FAILED"; exit 1; } || echo "All language audits passed."
```

### 失敗案例

Go + Python 混合專案只跑 `pip-audit`，忽略 `govulncheck`，Go 依賴中的 CVE 被忽略直到漏洞被利用。

**來源**：[獨立驗證·公開來源] pip-audit 官方文件；[獨立驗證·公開來源] cargo-audit GitHub；[獨立驗證·公開來源] govulncheck golang.org/x/vuln；[自測] 版本鎖定修復

**已知限制**：未涵蓋 Swift / PHP / .NET (C#)；cargo-audit 依賴 RustSec Advisory Database，網路隔離環境需鏡像；npm audit 對私有 registry 可能回報不完整。

---

## 情境速查表

| 情境 | 觸發條件 | 對應規則 | 正確行為 | 錯誤行為 |
|------|---------|---------|---------|---------|
| 不確定需求，要開始實作 | 需求含歧義或多解法 | R1 | 詮釋 + 假設 + 列選項讓用戶確認 | 直接選一種做 |
| 用戶說「直接做」，操作是 DELETE/DROP | 不可逆操作 | R1（不可逆例外） | 仍需顯示摘要 + 等待確認 | 跳過確認直接執行 |
| 兩個加密函式各自 inline IV/nonce | 重複 nonce 生成 | R2（FATAL-2） | 重構為共用 `secure_random_bytes()` | 「各自獨立」保留現狀 |
| grep 憑證掃描命中假資料 | tests/fixtures 大量誤報 | R3（FATAL-1） | `--exclude-dir={tests,fixtures,...}` + 推薦 gitleaks | 直接呈現全部結果 |
| 修功能時發現硬編碼 API Key | P0 安全漏洞 | R3（P0） | stash → hotfix 分支 → PR → 回報 | 繼續功能開發 |
| 宣告「完成」前的檢查 | 任何任務收尾 | R4 + R12 | 執行驗證，展示前 5 後 5 行輸出 | 口頭說「測試通過」 |
| LLM 被設計為決定 HTTP status code | 確定性邏輯讓 LLM 控制 | R5 | 移到確定性 if/switch | 「LLM 判斷比較靈活」 |
| Token 使用率達 80%，接新任務 | context window 壓力 | R6 | 先 `/compact` 保留安全紅線 | 直接接受，擠壓已有 context |
| 看到兩種寫法衝突 | 代碼庫模式不一致 | R7 | ADR → 最近 commit → 覆蓋率；寫 TODO(conflict) | 靜默選一種，不標注 |
| ADR 與覆蓋率衝突 | ADR-005 指定 jest，mocha 80% | R7 | 選 jest（ADR 優先）+ TODO 標注 | 選 mocha（覆蓋率高） |
| 要改一個函式 | 不熟悉現有結構 | R8 | 讀 exports + caller + utility | 直接改，不看 caller |
| 目標檔案超過 200 行 | 大型源碼檔 | R8 | 分段讀取，每段後標注剩餘行數 | 一次讀完或假設截斷後為空 |
| 測試 100% 覆蓋但全是 mock | coverage 虛高 | R9 | 補輸出值驗證，說明 coverage 不可信 | 「100% 覆蓋，測試沒問題」 |
| Healthcheck 失敗 | `bash scripts/healthcheck.sh` 回 FAIL | R12 | 完整貼出錯誤，不宣告完成 | 口頭說「應該沒問題」 |
| G 層 migration 驗證在 SQLite 使用 psql | DB 環境不符 | R13 | 使用 `<DB_VERIFY_CMD>` + 4 種 DB 注解 | 硬寫 psql，SQLite 崩潰 |
| polyglot 工具未安裝 | `govulncheck` 不存在 | R14 | 輸出安裝指令 + exit 1 | 靜默跳過顯示「audit passed」 |

---

## 版本溯源表

| 版本 | 日期 | 主要變更 |
|------|------|----------|
| A1.0 | 2026-04 | Karpathy R1-R4 + Mnilax R5-R12 初版（12 條） |
| A2.0 | 2026-05 | 新增 R13（PGE）、R14（Polyglot 安全審查）→ 14 條 |
| A3.0 | 2026-05-18 | R7 四欄衝突表、R14 安裝指引、R13 E 層理由、台灣語境補充 |
| B3.0 | 2026-05-18 | FATAL-1/2、MAJOR-1/2/3/4 全部修復；版本鎖定、已知限制 inline |
| AB3.0 | 2026-05-18 | 合成 A3 + B3，保留所有 FATAL/MAJOR 修復 + 台灣語境補充（860 行） |
| A4.0 | 2026-05-18 | J5 批評回應：860→582 行精簡；R7 優先序統一；互動矩陣合併為情境速查表 |
| B4.0 | 2026-05-18 | Critic 修復：R13 G 層日期佔位符；R1 不可逆關鍵字補全；R3 stash pop 還原；R2 觸發條件 |
| **AB4.0** | **2026-05-18** | **合成 A4 + B4；3 連勝收斂版本（Round 4 J1/J2/J3=L）** |

---

**規則計數確認**：R1 R2 R3 R4（Karpathy 4）+ R5 R6 R7 R8 R9 R10 R11 R12（Mnilax 8）+ R13 R14（新增 2）= **14 條**

*AB4.0 · 最終版 · 4 輪對抗精煉 · 3 連勝收斂 · 14 條規則*

---

*🔄 overnight-research 驗證：2026-05-23 — 本文件為 Karpathy × Mnilax 規則合成報告（基於本地知識庫 38 篇 + 推文）。狀態：已確認現行有效（規則框架仍適用）。*

---

## 2026-05-25 Re-check

> **方法**：對照 `.claude/rules/core.md`（R1–R12 主要落地位置）+ `output-discipline.md` + `subagent-strategy.md` 逐條驗證落地狀態；結合 `2026-05-25-papers-analysis.md`（84 篇論文）檢驗規則框架的外部驗證度。

### 已落地的建議（✅）

**Karpathy 4 Floor（R1–R4）**
- ✅ R1 — 實作前假設顯露：`core.md` §實作前假設顯露 已完整落地，含不可逆操作強制確認（MAJOR-4）
- ✅ R2 — 規格極簡：`core.md` §規格極簡 已落地，含「資深工程師會說太複雜？」自我檢驗
- ✅ R3 — 外科刀式修改：`core.md` §外科刀式修改 已落地，含量化界線（Bug fix ≤50 行 / 新功能 ≤300 行 / 單檔 ≤500 行）
- ✅ R4 — 目標導向：`core.md` §驗證與品質 已落地，含「展示前 5 / 後 5 行輸出」硬性要求

**Mnilax 8 增量（R5–R12）**
- ✅ R5 — Latent vs Deterministic：`core.md` §判斷與決定的邊界 已落地
- ✅ R6 — Token 預算管理：`context-management.md` 完整實作（含 4,000/30,000 token 預算 + 三層 compact 觸發）
- ✅ R7 — 衝突浮現：`core.md` §外科刀式修改 — R7 已落地，ADR/CONTRIBUTING.md 優先序
- ✅ R8 — 改前先讀：`core.md` §外科刀式修改 — R8（大檔分段讀取 > 200 行）已落地
- ✅ R9 — 測試驗證意圖：`core.md` §驗證與品質 — R9 已落地
- ✅ R10 — 進度 Checkpoint：`core.md` §驗證與品質 — R10（1 句摘要格式）已落地
- ✅ R11 — 慣例優先：`core.md` §外科刀式修改 — R11（Convention First）已落地
- ✅ R12 — Fail Loud：`core.md` §PGE + R12 Fail Loud 已落地，含搜尋截斷標示格式

**新增 2 條（R13–R14）**
- ✅ R13 — PGE 架構：本報告機械檢查表完整；`core.md` §PGE + R12 Fail Loud 部分覆蓋（前置條件 + 驗證概念）
- ⚠️ R14 — Polyglot 安全審查：本報告機械檢查表完整，但 `core.md` / `security-hygiene.md` 無對應落地規則

**輸出紀律（呼應 R2/R12）**
- ✅ 無開場白、填充語禁止、≤150 字純文字：`output-discipline.md` 完整落地
- ✅ 禁用技術術語（leverage/robust/seamless 等）：`output-discipline.md` 已明文
- ✅ 優雅性自檢（Demand Elegance）：`output-discipline.md` 已落地

### 待追蹤的 gap（⚠️）

- ⚠️ **R13 的 G 層 DB 驗證佔位符**：本報告 §R13 機械檢查表使用 `<DB_VERIFY_CMD>` 佔位符，但 workspace 的 `scripts/healthcheck.sh` 實際內容未核查是否有等效實作。R13 的「前置條件失敗 → exit 1，不 skip」概念需要在 healthcheck 腳本中體現。
- ⚠️ **R14 Polyglot 安全審查未進入 auto-load**：本報告 §R14 的多語言 dependency audit checklist 僅在報告中記錄，未在 `.claude/rules/security-hygiene.md` 或任何 hook 中落地。Python / Go / Rust / Ruby 的 audit 工具鏈（`pip-audit` / `govulncheck` / `cargo-audit`）缺乏自動觸發機制。
- ⚠️ **FATAL-1（憑證掃描排除假資料）的 hook 整合**：本報告 §R3 機械檢查表建議 `--exclude-dir={tests,fixtures,...}` 過濾，但 `pre-commit-review.sh` 是否已實作此排除邏輯未驗證。
- ⚠️ **R2 安全例外（加密基底共用）未在 rules 中明文**：`core.md` §規格極簡 只寫「不為單次使用抽 helper」，未標示加密原語（nonce/IV 生成）的安全例外。此規則在涉及加密的任務中容易造成誤解（Claude 可能以「單次使用」理由 inline nonce）。

### 新發現的最佳實踐補充（🆕）

- 🆕 **「Harness > 模型」對 R2 的延伸詮釋**：`2026-05-25-papers-analysis.md` 中 `harbor-automated-harness-optimization` 論文發現「手工調優產生退化 -37%」——即過度優化 harness 配置（違反 R2 Simplicity First）會造成性能退化。R2 的精簡原則不只適用於代碼，也適用於 harness 配置：用 Bayesian 優化系統性搜索 9 個旗標遠勝手工試錯。
- 🆕 **R8 的大檔分段讀取與 Token Budget 的交叉**：`natural-language-agent-harnesses-2603-25723` 論文實測 NLAH（Natural Language Agent Harnesses）將 context 從 60.1K → 2.9K token（-95%），效能相當。對 R8「讀取超過 200 行必須分段」的補充：分段讀取不只防止 context 截斷，也應考慮只讀取「解決問題所需的最小行數」（與 R6 Token Budget 交叉），避免超過 per-task 4,000 token 預算。
- 🆕 **`/goal` 命令對 R4 的工具化**：R4 要求「開工前寫成功的可觀測條件，迭代到達標」，`/goal` 命令（Week 20, v2.1.139）是 R4 的原生實現工具：`/goal all tests pass and lint is clean` 後 Claude 自動跨多輪工作直到條件成立。建議在 `core.md` §R4 補充 `/goal` 作為強可驗證條件的推薦實現方式。
- 🆕 **R12 Fail Loud 的 `continueOnBlock` 新語義**：v2.1.141 引入 `continueOnBlock: true` hook 配置，PostToolUse hook 拒絕時將拒絕原因回饋 Claude 並繼續 turn（而非結束）。這是 R12「失敗必須立即顯示完整錯誤訊息」的一種新形式：hook 失敗資訊被回饋給 Claude，讓 Claude 有機會自我修正。需注意：此配置可能讓 hook 看起來「被忽略」（GOTCHA #42），需要明確設計意圖。

*Re-check 日期：2026-05-25 | 規則版本：AB4.0（最終）| 落地評估：R1–R12 全部落地，R13 部分落地，R14 未落地*
