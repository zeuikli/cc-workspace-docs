# OpenUsage Claude Plugin — 方案 A/C 實作紀錄

## 背景

基礎專案：https://github.com/robinebers/openusage（macOS Tauri v2 menu bar app）
目標：在 Claude plugin 面板新增 CLI Cost / Desktop Cost / iOS Cost 三行，
      從 `~/.claude/projects/` transcript JSONL 讀取用量並按 source 分流顯示。

---

## 方案 A — plugin.json 新增三行 manifest

**檔案**：`plugins/claude/plugin.json`

在 `"Last 30 Days"` 後、`"Usage Trend"` 前插入：

```json
{ "type": "text", "label": "CLI Cost",     "scope": "detail" },
{ "type": "text", "label": "Desktop Cost", "scope": "detail" },
{ "type": "text", "label": "iOS Cost",     "scope": "detail" },
```

---

## 方案 C — plugin.js 直接掃 transcript（核心實作）

**檔案**：`plugins/claude/plugin.js`

### 新增內容（插入在 `getOauthConfig` 函式之前，約第 163 行）

#### 1. `getCostLogPath(ctx)`（保留但不再使用，可移除）

```javascript
function getCostLogPath(ctx) {
  const explicit = readEnvText(ctx, "OPENUSAGE_COST_LOG")
  if (explicit) return explicit
  const wsRoot = readEnvText(ctx, "WORKSPACE_ROOT")
  if (wsRoot) return wsRoot.replace(/\/+$/, "") + "/evolution/cost-log.jsonl"
  return "/Users/zeuik/cc-workspace/evolution/cost-log.jsonl"
}
```

#### 2. Pricing table + `estimateTranscriptCost(model, usage)`

```javascript
const TRANSCRIPT_PRICING = [
  { prefix: "claude-opus-4",        input: 15.00, output: 75.00, cacheRead: 1.50,  cacheCreate: 18.75 },
  { prefix: "claude-opus-3",        input: 15.00, output: 75.00, cacheRead: 1.50,  cacheCreate: 18.75 },
  { prefix: "claude-sonnet-4",      input:  3.00, output: 15.00, cacheRead: 0.30,  cacheCreate:  3.75 },
  { prefix: "claude-sonnet-3-7",    input:  3.00, output: 15.00, cacheRead: 0.30,  cacheCreate:  3.75 },
  { prefix: "claude-sonnet-3-5",    input:  3.00, output: 15.00, cacheRead: 0.30,  cacheCreate:  3.75 },
  { prefix: "claude-sonnet-3",      input:  3.00, output: 15.00, cacheRead: 0.30,  cacheCreate:  3.75 },
  { prefix: "claude-haiku-3-5",     input:  0.80, output:  4.00, cacheRead: 0.08,  cacheCreate:  1.00 },
  { prefix: "claude-haiku-3",       input:  0.25, output:  1.25, cacheRead: 0.03,  cacheCreate:  0.30 },
]
const TRANSCRIPT_PRICING_DEFAULT = { input: 3.00, output: 15.00, cacheRead: 0.30, cacheCreate: 3.75 }

function estimateTranscriptCost(model, usage) {
  const m = String(model || "").toLowerCase().replace(/-\d{8}$/, "")
  let p = TRANSCRIPT_PRICING_DEFAULT
  for (let i = 0; i < TRANSCRIPT_PRICING.length; i++) {
    if (m.startsWith(TRANSCRIPT_PRICING[i].prefix)) { p = TRANSCRIPT_PRICING[i]; break }
  }
  const inp    = Number(usage.input_tokens)                  || 0
  const out    = Number(usage.output_tokens)                 || 0
  const cacheR = Number(usage.cache_read_input_tokens)       || 0
  const cacheC = Number(usage.cache_creation_input_tokens)   || 0
  return (inp * p.input + out * p.output + cacheR * p.cacheRead + cacheC * p.cacheCreate) / 1e6
}
```

#### 3. `scanTranscriptCosts(ctx, sinceStr)` — 核心函式

```javascript
function scanTranscriptCosts(ctx, sinceStr) {
  try {
    const projectsDir = "~/.claude/projects"
    if (!ctx.host.fs.exists(projectsDir)) return null
    const projectNames = ctx.host.fs.listDir(projectsDir)
    if (!Array.isArray(projectNames)) return null

    const totals = { cli: 0, desktop: 0, ios: 0 }
    let found = false

    for (let pi = 0; pi < projectNames.length; pi++) {
      const projectName = projectNames[pi]
      const projectDir = projectsDir + "/" + projectName
      let files
      try { files = ctx.host.fs.listDir(projectDir) } catch { continue }
      if (!Array.isArray(files)) continue

      for (let fi = 0; fi < files.length; fi++) {
        const fname = files[fi]
        if (!fname.endsWith(".jsonl")) continue

        const fpath = projectDir + "/" + fname
        let text
        try { text = ctx.host.fs.readText(fpath) } catch { continue }
        if (!text) continue

        const lines = text.split("\n")

        // Pass 1: 前 30 行確定 entrypoint 和 first_ts
        let entrypoint = null
        let first_ts = null
        const limit = Math.min(30, lines.length)
        for (let li = 0; li < limit; li++) {
          const raw = lines[li].trim()
          if (!raw) continue
          let obj
          try { obj = JSON.parse(raw) } catch { continue }
          if (!entrypoint && typeof obj.entrypoint === "string") entrypoint = obj.entrypoint
          if (!first_ts && typeof obj.timestamp === "string") first_ts = obj.timestamp
          if (entrypoint && first_ts) break
        }
        if (!entrypoint) continue
        if (!first_ts || first_ts.slice(0, 10) < sinceStr) continue

        // entrypoint → source bucket
        let bucket
        if (entrypoint === "cli") bucket = "cli"
        else if (entrypoint === "remote_mobile") bucket = "ios"
        else bucket = "desktop"

        // Pass 2: 累積 token usage，取 output token 最多的 model 作代表
        const modelOutput = {}
        let totalUsage = { input_tokens: 0, output_tokens: 0, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 }
        let dominantModel = null
        let maxOutput = 0

        for (let li = 0; li < lines.length; li++) {
          const raw = lines[li].trim()
          if (!raw) continue
          let obj
          try { obj = JSON.parse(raw) } catch { continue }
          if (obj.type !== "assistant") continue
          const msg = obj.message
          if (!msg || !msg.usage) continue
          const model = typeof msg.model === "string" ? msg.model : ""
          const u = msg.usage
          const out = Number(u.output_tokens) || 0
          modelOutput[model] = (modelOutput[model] || 0) + out
          if (modelOutput[model] > maxOutput) { maxOutput = modelOutput[model]; dominantModel = model }
          totalUsage.input_tokens                += Number(u.input_tokens)                || 0
          totalUsage.output_tokens               += Number(u.output_tokens)               || 0
          totalUsage.cache_read_input_tokens     += Number(u.cache_read_input_tokens)     || 0
          totalUsage.cache_creation_input_tokens += Number(u.cache_creation_input_tokens) || 0
        }

        if (!dominantModel) continue
        const cost = estimateTranscriptCost(dominantModel, totalUsage)
        totals[bucket] += cost
        found = true
      }
    }

    return found ? totals : { cli: 0, desktop: 0, ios: 0 }
  } catch {
    return null
  }
}
```

#### 4. `pushSourceCostLines(lines, ctx, sinceStr)`

```javascript
function pushSourceCostLines(lines, ctx, sinceStr) {
  const costs = scanTranscriptCosts(ctx, sinceStr)
  const fmt = costs === null
    ? () => "—"
    : (v) => "$" + v.toFixed(2)
  lines.push(ctx.line.text({ label: "CLI Cost",     value: fmt(costs ? costs.cli     : 0) }))
  lines.push(ctx.line.text({ label: "Desktop Cost", value: fmt(costs ? costs.desktop : 0) }))
  lines.push(ctx.line.text({ label: "iOS Cost",     value: fmt(costs ? costs.ios     : 0) }))
}
```

### probe() 修改（兩處）

**1. `queryTokenUsage` 呼叫前插入 sinceStr 計算：**

```javascript
const _sinceDate = new Date()
_sinceDate.setDate(_sinceDate.getDate() - 30)
const _sinceY = _sinceDate.getFullYear()
const _sinceM = _sinceDate.getMonth() + 1
const _sinceD = _sinceDate.getDate()
const probeSinceStr = _sinceY + "-" + (_sinceM < 10 ? "0" : "") + _sinceM + "-" + (_sinceD < 10 ? "0" : "") + _sinceD
```

**2. `else if (lines.length === 0)` 區塊後、`return` 前插入：**

```javascript
pushSourceCostLines(lines, ctx, probeSinceStr)
```

---

## 測試

`plugins/claude/plugin.sourcecost.test.js` — 10 個 TC，10/10 通過（355ms）  
使用 `makeCtx` in-memory `files` Map 模擬 `listDir`/`readText`。

---

## 部署方式

```bash
sudo cp plugins/claude/plugin.js plugins/claude/plugin.json \
  /Applications/OpenUsage.app/Contents/Resources/resources/bundled_plugins/claude/
```

**重要**：app 每次啟動時會從 app bundle 覆蓋 `~/Library/Application Support/com.sunstory.openusage/plugins/claude/`，
必須改 app bundle 才能持久生效。

---

## 實際結果（2026-06-08）

| 行 | 值 |
|---|---|
| CLI Cost | $338.36 |
| Desktop Cost | $242.56 |
| iOS Cost | $0.00 |

iOS $0.00 正常（iOS session transcript 在 Linux 機器，Mac 本地無法讀取）。

---

## entrypoint 欄位對應表

| entrypoint 值 | source 分類 |
|---|---|
| `cli` | claude-code-cli（CLI session） |
| `claude-desktop` | claude-desktop |
| `remote_mobile` | claude-ios（iOS app 連 Linux server） |
| `remote_desktop` | claude-desktop |

---

## 注意事項

- `sync-desktop-usage.py` 的 `entrypoint == "cli"` branch 修補（本地未 commit）也需同步套用，否則 cost-log 分類仍錯誤
- Pricing 以 output token 最多的 model 作代表，跨模型 session 誤差可接受
- 無 mtime API，無法按時間過濾檔案，全掃幾百個 JSONL 約 2–5 秒
