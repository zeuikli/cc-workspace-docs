# self-test 覆蓋盤點：86 支腳本中 75 支沒有自測（2026-08-03）

> baseline 交接任務第 3 項的產物。**盤點是為了排序，不是為了一次補完**——75 支全補是
> 假動作，真正的問題是「哪些壞掉了不會有人發現」。

## 判準：風險 = 有自動呼叫端 × 失敗不響

`baseline.sh` 的 `self_test` 維度只涵蓋**宣告了 `--self-test`** 的腳本；其餘 75 支只驗語法
（`bash -n` / AST 解析），也就是**能跑起來但邏輯錯掉時，基線全綠**。

自動呼叫端（hook / workflow / settings.json）意味著沒有人在旁邊看輸出；失敗又不改變
exit code 的，等於永遠不會被發現。兩者相乘即優先序。

## 盤點結果（機械產生，重測見文末命令）

| 類別 | 數量 | 意義 |
|---|---:|---|
| 有 `--self-test` | 11 → **14**（本輪 +3）| 進 baseline 的 `self_test` 維度 |
| 無自測 **但有自動呼叫端** | **36** | 風險最高，本表主體 |
| 無自測、僅被其他腳本呼叫 | 18 | 上游壞了通常會連帶炸，較易察覺 |
| 無自測、零呼叫端（孤兒） | 21 | 風險低但屬**常駐稅**，另案處理（退役或收編） |

### 本輪已補（前三名）

| 腳本 | 呼叫端 | 為何排前面 | 自測案例 |
|---|---|---|---|
| `unicode-sanitize.sh` | `unicode-covert-channel-guard.sh`（安全 hook）| **安全原語**：它靜默壞掉＝隱寫通道恢復暢通，而沒有任何紅燈 | 9 例（Tag/PUA/zero-width 三類壞例 × detect+filter、乾淨文字不得誤刪、空輸入）|
| `usage-guard.py` | `usage-gate.sh`、`user-prompt-submit.sh`（且以 **import** 直呼，連 exit code 都沒有）| 裁決 SSoT：壞掉不是報錯，是**不再擋**或**永遠擋** | 14 例（檔位分類、ok/warn/urge 邊界值、7d 軸獨立於 5h、block 模式放行清單、DISABLE 逃生閥、壞環境值回退）|
| `usage-report.py` | `session-end.sh`、`session-stop.sh`、`user-prompt-submit.sh` | 產出 `usage-report.json`＝所有數字的來源；壞掉只會讓大家讀到錯的數字（本 workspace 反覆踩的「儀表失真」）| 14 例（cost/task 去重的保留規則與丟棄計數、實測 `cost_usd` 不得被估算覆蓋、估算單調性、空輸入）|

三者的 oracle 資格皆以 **mutation 實測**驗過（改壞判定 → self-test 必須轉紅）：

- `unicode-sanitize`：移除 Tag 偵測／移除 zero-width 清單／filter 不清洗 → 3/3 DETECTED
- `usage-guard`：urge 門檻放寬／block 不擋／DISABLE 失效／fast-path 忽略 7d（urge 與 warn 各一）→ 5/5 DETECTED
- `usage-report`：cli-session 不丟／去重取小者／實測 cost 被估算覆蓋／丟棄計數不累加 → 4/4 DETECTED

**mutation 過程中抓到一個真缺陷**：`usage-report.py` 原本是 `main()` 裸呼叫，回傳值被丟棄
→ `--self-test` 印出 FAIL 仍 `exit 0`，`baseline` 的 `self_test` 維度對它**恆綠**。已改
`sys.exit(main() or 0)`。這是「閘門看起來在、實際不擋」的又一實例——**出口碼才是消費端
唯一讀得到的判定**。

### 下一批候選（依同一判準，未做）

1. `sync-workspace.sh`（868 行）— session-end/stop hook **與 CI 自動修**都呼叫，且**會 commit 到 main**。壞掉＝索引被自動寫壞並推上主幹。工程量最大，需拆段測。
2. `verify-telemetry.py` / `verify-tasklog.sh` — CI 閘門；壞掉會 exit≠0 故較響，但「誤判為通過」那一側無人驗。
3. `git-push-retry.sh` — 4 支 workflow 使用；失敗會響，但重試次數/退避是否真的生效無人驗。
4. `skill-router.py` — 已有 `test-skill-router-routing.sh` 覆蓋路由品質，補 `--self-test` 的邊際效益較低。

### 明確不打算補的

21 支孤兒腳本（零呼叫端）補自測是**替死碼付利息**。正確處置是退役或接回呼叫端，屬另一
議題；清單見下方命令輸出的第三段。

## 重測命令（本表數字以此為準）

```bash
python3 - <<'PY'
import pathlib, re
OWN = re.compile(r'add_argument\("--self-test"|--self-test\)|= "--self-test"|== "--self-test"')
scripts = sorted(list(pathlib.Path("scripts").glob("*.sh")) + list(pathlib.Path("scripts").glob("*.py")))
corpus = {}
for d in (".claude/hooks", ".github/workflows"):
    for f in pathlib.Path(d).rglob("*"):
        if f.is_file(): corpus[str(f)] = f.read_text(errors="ignore")
corpus[".claude/settings.json"] = pathlib.Path(".claude/settings.json").read_text()
for p in scripts: corpus["scripts/"+p.name] = p.read_text(errors="ignore")
own = [p.name for p in scripts if OWN.search(p.read_text(errors="ignore"))]
rest = [p.name for p in scripts if p.name not in own]
auto = {n: sorted({k for k,v in corpus.items() if n in v and not k.endswith("/"+n)
                   and k.startswith((".claude/hooks",".github/workflows",".claude/settings"))}) for n in rest}
print(f"總數 {len(scripts)}｜有自測 {len(own)}｜無自測 {len(rest)}｜其中有自動呼叫端 {sum(1 for v in auto.values() if v)}")
PY
```
