# cc-workspace 冷啟動 + Auto-Load 優化可執行計劃書

**日期**：2026-06-03 | **分支**：`feature/autoload-coldstart-research`
**對應研究**：`2026-06-03-claude-code-cold-start-latency-deep-research.md`
**範圍**：本計劃為**研究交付物**，描述可執行步驟與 Falsifiable Prediction；**不在本任務內修改 hooks/settings.json**（修改安全基礎設施需獨立 gated step）。

---

## 0. 現狀基線（本機實測 2026-06-03，warm cache，n=3，dummy stdin）

| 項目 | 數值 | 量測命令 |
|------|------|---------|
| auto-load total | **16,927 bytes**（≈4.2K tokens） | `wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md` |
| session-init.sh | 592ms（warm，fetch=0ms） | hook 計時 |
| **pre-commit-review.sh** | **2,965ms**（96% = healthcheck 2,854ms） | hook 計時 |
| user-prompt-submit.sh | 146ms（每 prompt 阻塞） | hook 計時 |
| block-dangerous.sh | 53ms（每 Bash，**安全 gate**） | hook 計時 |
| protect-sensitive-files.sh | 56ms（每寫檔，**安全 gate**） | hook 計時 |

**診斷**：auto-load byte 16,927 在「13K 基線 / 18K 上限」軟性區間內（12-Rule Canon 完整性正當化，見 core.md §Framework Integrity），**非首要瓶頸**。真正延遲在 hook 進程 spawn × 頻率，與低頻高延遲的同步 healthcheck。

---

## 1. Hook Partition（計劃核心 — 安全前提）

> 任何 hook 優化前，先 partition。誤把安全 hook 改 async = 破壞 CLAUDE.md 安全紅線。

| Hook | 類別 | 可優化路徑 | **禁止** |
|------|------|-----------|---------|
| block-dangerous.sh | 🔒 **must-stay-sync** | dispatcher / 加速 script | ❌ async（會失去阻擋能力） |
| protect-sensitive-files.sh | 🔒 **must-stay-sync** | dispatcher / 加速 script | ❌ async（會失去保護憑證） |
| user-prompt-submit.sh | 🔒 **must-stay-sync** | 減 spawn / 精簡邏輯 | ❌ async（context 注入需即時） |
| pre-commit-review.sh | 🟡 sync（gate 性質）| **healthcheck 改 async/快取**（見 §2.2） | ❌ 整體 async |
| memory-sync.sh | 🟢 **async-safe** | `async:true` | — |
| notification-log.sh | 🟢 已 async | — | — |
| post-edit.sh / audit-log.sh | 🟢 **async-safe**（純 side-effect log） | `async:true` | — |

---

## 2. 優化動作（依槓桿排序）

### 2.1 P0 — side-effect hook 加 `async:true`（v2.1.45+）
對象：memory-sync / post-edit / audit-log / failure-log / notification-log（純 logging/audit）。
效果：不阻塞 model，回收其阻塞延遲。安全：零影響（無 gate 語義）。

### 2.2 P0 — pre-commit-review 的 healthcheck 去阻塞
2,965ms 中 2,854ms 是同步 `healthcheck.sh`。選項：
- (a) healthcheck 結果快取（檔案 mtime 守門，N 分鐘內復用）
- (b) healthcheck 改 `async:true` + `asyncRewake:true`（exit 2 喚醒）— 但 gate 語義需保留，謹慎
- (c) 僅在 staged 檔案數超閾值時才跑 healthcheck（lazy）
推薦 (a)+(c) 組合，保留 gate 同步性。

### 2.3 P1 — 高頻安全 hook 內部優化（不 async）
block-dangerous.sh（17,292 bytes bash）53ms/call：dispatcher 模式或精簡 regex 路徑，目標降至 <20ms，保留全部阻擋規則。

### 2.4 P1 — cache pre-warm 習慣
長閒置（>5min TTL）後 resume -> 接受 cache miss 或考慮 1hr TTL；CLAUDE.md 靜態前綴維持不動（已遵守 context-management.md）。

### 2.5 P2 — auto-load 微調（非首要，可選）
16,927 bytes 在軟性區間內。若要回收餘裕，依 5/25 playbook 只壓 TYPE B/C/D，保留 R1–R12 行為。**非本計劃重點**（前作已最佳化至接近極限）。

---

## 3. Falsifiable Prediction（跨 byte + ms 雙維度 + 安全 invariant）

> 依 MEMORY.md house style。**驗證必須同時斷言「更快」與「安全存活」**（R9：只檢查快會通過即使破壞了 gate = hacked eval）。

**改動假設**（未來 gated 執行 §2.1+§2.2(a)(c)+§2.3）：

**預測**：
1. **byte**：auto-load 維持 ≤ 17,000 bytes（不因加 async 設定膨脹；async 在 settings.json 不計 auto-load）
2. **ms（互動層）**：side-effect hook async 後，每 prompt 阻塞延遲降低（user-facing latency ↓）
3. **ms（commit 層）**：pre-commit healthcheck 快取/lazy 後，重複 commit 場景 pre-commit-review p50 從 2,965ms 降至 < 500ms
4. **安全 invariant 存活**：block-dangerous 仍拒危險命令；protect-sensitive 仍擋 .env 寫入；healthcheck FAIL 仍能 gate commit

**驗證命令**：
```bash
# (1) byte 維度
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1
# 斷言 total ≤ 17000

# (2)(3) ms 維度 — 重跑 hook 計時，比對 baseline
for h in pre-commit-review user-prompt-submit block-dangerous; do
  s=$(python3 -c 'import time;print(int(time.time()*1000))')
  echo '{}' | bash .claude/hooks/$h.sh >/dev/null 2>&1
  e=$(python3 -c 'import time;print(int(time.time()*1000))')
  echo "$h: $((e-s))ms"
done

# (4) 安全 invariant — 必須仍然阻擋（exit≠0 或 stderr 含 BLOCK）
echo '{"tool_input":{"command":"rm -rf /"}}' | bash .claude/hooks/block-dangerous.sh; echo "block-dangerous exit=$?"
echo '{"tool_input":{"file_path":".env"}}' | bash .claude/hooks/protect-sensitive-files.sh; echo "protect exit=$?"
bash scripts/healthcheck.sh >/dev/null 2>&1; echo "healthcheck exit=$?"  # FAIL>0 時應非 0
```

**判定**：4 條全 PASS = 確認；任一 FAIL（尤其 #4 安全）= REFUTED，回滾。**安全 invariant 優先於 ms 改善**。

---

## 4. 回滾計劃

- 所有改動限 `.claude/settings.json` + `.claude/hooks/*.sh`，git 追蹤
- 改前 `git stash` / 分支隔離；任一安全 invariant REFUTED -> `git revert`
- healthcheck eval 回歸 ≥5pp（FAIL 數增）-> 立即回滾（依 core.md §Framework Integrity）

---

## 5. 與既有 workspace 規則的接合

| 規則 | 接合點 |
|------|--------|
| context-management.md「mid-session 禁切模型/增刪 tool/改 CLAUDE.md」 | §2.4 cache 暖態前提 — 已遵守 |
| core.md §Framework Integrity（13K/18K byte 軟門檻） | §2.5 auto-load 非首要，維持區間 |
| §生產安全紅線 + R12 Fail Loud | §1 partition + §3 invariant #4 — 不可優化掉安全 |
| 5/25 reduce-auto-load playbook（TYPE A/B/C/D） | §2.5 若回收餘裕的方法 |

---

## 結論

cc-workspace 的「載入速度」瓶頸**不在 auto-load token**（已近最佳化極限，16,927 bytes 在正當區間），而在 **hook 進程 spawn × 頻率 + 低頻高延遲的同步 healthcheck**。最高槓桿：(1) side-effect hook async；(2) pre-commit healthcheck 去阻塞；(3) 安全 hook 維持同步但內部優化。**安全 invariant 不可為速度犧牲** — 這是計劃的核心安全前提，也是 Falsifiable Prediction 的首要驗證項。
