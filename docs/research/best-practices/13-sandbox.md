---
title: "Sandboxing — OS 層隔離技術詳解"
source: "https://code.claude.com/docs/en/sandboxing"
type: best-practices
---

# Sandboxing — OS 層隔離技術詳解

> 來源：https://code.claude.com/docs/en/sandboxing
> 收錄日期：2026-05-01
> 涵蓋：Sandbox 原理、Filesystem/Network 隔離、OS 層技術、設定選項、安全限制、最佳實踐
> 補充：09-secure-deployment.md 的 Sandbox Runtime 章節

---

## 概覽

Claude Code 的 native sandboxing 為 agent 執行提供更安全的環境，同時減少持續的 permission prompt。它透過**預先定義邊界**讓 Claude Code 在低風險範圍內自由工作，而非對每個 bash 指令逐一詢問。

Sandboxed bash tool 使用 OS 層原語強制 filesystem 和 network 隔離。

---

## 為什麼需要 Sandboxing？

傳統 permission-based 安全需要使用者持續核准 bash 指令，導致：

- **核准疲勞**：重複點擊「核准」使注意力下降
- **生產力降低**：頻繁中斷拖慢開發流程
- **自主性受限**：Claude Code 等待核准時效率低落

Sandboxing 的解決方案：

1. **定義清晰邊界**：明確指定可存取的目錄和網路 host
2. **減少 permission prompt**：sandbox 內的安全指令免 prompt
3. **維持安全**：sandbox 外的存取嘗試立即通知
4. **啟用自主性**：Claude Code 在定義限制內更獨立地運作

> **有效 sandboxing 的核心要件**：filesystem 和 network 隔離**缺一不可**。無 network 隔離，agent 可洩漏 SSH key；無 filesystem 隔離，agent 可 backdoor 系統資源獲取 network 存取。

---

## 運作原理

### Filesystem 隔離

Sandboxed bash tool 限制 filesystem 存取：

| 行為 | 預設 |
|------|------|
| 寫入 | 只能寫入當前 working directory 及子目錄 |
| 讀取 | 可讀取整台電腦（除特定 denied 目錄外）|
| 限制強制範圍 | OS 層（macOS: Seatbelt, Linux: bubblewrap）|
| 適用對象 | 所有 subprocess 指令（kubectl, terraform, npm 等）|

透過 `sandbox.filesystem.allowWrite` 授予額外寫入路徑。

### Network 隔離

Network 存取透過 sandbox **外部**的 proxy server 控制：

| 機制 | 說明 |
|------|------|
| Domain 限制 | 只能存取核准的域名 |
| 新域名請求 | 觸發 permission prompt（啟用 `allowManagedDomainsOnly` 則自動封鎖）|
| 自訂 proxy | 進階用戶可實作自訂流量規則 |
| 覆蓋範圍 | 所有 scripts、programs、子程序 |

> 內建 proxy 根據 hostname 決策，**不終止或檢查 TLS 流量**。

### OS 層強制

| 平台 | 技術 |
|------|------|
| macOS | Seatbelt |
| Linux | [bubblewrap](https://github.com/containers/bubblewrap) |
| WSL2 | bubblewrap（同 Linux）|
| WSL1 | **不支援**（缺少 kernel namespace）|

所有由 Claude Code 指令衍生的子程序繼承相同安全邊界。

---

## 快速開始

### 前置需求

**macOS**：內建 Seatbelt，開箱即用。

**Linux / WSL2**：需先安裝：

```bash
# Ubuntu/Debian
sudo apt-get install bubblewrap socat

# Fedora
sudo dnf install bubblewrap socat
```

**WSL2 注意**：Sandboxed 指令無法啟動 Windows binary（`cmd.exe`, `powershell.exe`, `/mnt/c/` 下的程式）。如需呼叫 Windows binary，加到 `excludedCommands` 讓它在 sandbox 外執行。

### 啟用 Sandboxing

```
/sandbox
```

開啟選單選擇 sandbox mode。若缺少依賴（Linux 需要 bubblewrap/socat），選單會顯示安裝說明。

**啟動失敗的行為**：預設顯示警告並繼續無 sandbox 執行。若需強制失敗（managed 環境），設定：

```json
{
  "sandbox": {
    "failIfUnavailable": true
  }
}
```

---

## Sandbox Modes

### Auto-allow Mode（推薦）

- Bash 指令嘗試在 sandbox 內執行並**自動核准**
- 無法沙箱的指令（需存取非 allowed host 等）退回一般 permission 流程
- Explicit deny 規則仍生效
- `rm`/`rmdir` 指向根目錄、home 或關鍵系統路徑仍提示

### Regular Permissions Mode

- 所有 bash 指令（即使沙箱內）仍走標準 permission 流程
- 提供更多控制，但需更多核准

> **重要**：兩種模式的 sandbox 強制範圍完全相同，差異只在是否自動核准。即使不在 acceptEdits mode，auto-allow 下的 sandboxed bash 仍自動執行（包含修改檔案的指令）。

---

## 設定說明

透過 `settings.json` 的 `sandbox` section 設定。完整 reference 見 [Settings](https://code.claude.com/docs/en/settings#sandbox-settings)。

### 授予額外寫入路徑

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": ["~/.kube", "/tmp/build"]
    }
  }
}
```

### 路徑前綴解析規則（與 permissions 語法不同）

| 前綴 | 意義 | 範例 |
|------|------|------|
| `/` | **絕對路徑**（filesystem root）| `/tmp/build` → `/tmp/build` |
| `~/` | 相對於 home directory | `~/.kube` → `$HOME/.kube` |
| `./` 或無前綴 | 相對於 project root（project settings 中），或 `~/.claude`（user settings 中）| `./output` → `<project-root>/output` |

> **注意**：sandbox filesystem 路徑用**標準慣例**（`/tmp` 是絕對路徑）；與 Read/Edit permission rules 用 `//path` 表示絕對路徑的語法**不同**。

### 各類路徑設定及其合併行為

多個 settings scope 的 `allowWrite`/`denyWrite`/`denyRead`/`allowRead` 設定**合併**（不覆蓋）：

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": ["~/.kube", "/tmp/build"],
      "denyWrite": ["/etc"],
      "denyRead": ["~/"],
      "allowRead": ["."]
    }
  }
}
```

**優先序**：`allowRead` 可覆蓋 `denyRead` 內的特定路徑。

**範例**：封鎖 home directory 讀取，但允許當前 project：

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "denyRead": ["~/"],
      "allowRead": ["."]
    }
  }
}
```

> `.` 在 project settings 中解析為 project root；在 user settings 中解析為 `~/.claude`。

### Network 設定

```json
{
  "sandbox": {
    "network": {
      "httpProxyPort": 8080,
      "socksProxyPort": 8081
    }
  }
}
```

自訂 proxy 可用於：解密 HTTPS、自訂過濾規則、記錄所有請求、整合既有安全基礎設施。

---

## 安全效益

### 防禦 Prompt Injection

即使攻擊者透過 prompt injection 操控 Claude Code，sandbox 仍保護系統：

**Filesystem 保護**：
- 不能修改 `~/.bashrc` 等關鍵設定
- 不能修改 `/bin/` 等系統檔案
- 不能讀取 Claude permission settings 中 denied 的檔案

**Network 保護**：
- 不能向攻擊者控制的 server 洩漏資料
- 不能從未授權域名下載惡意 script
- 不能對未批准服務呼叫 API
- 不能聯繫任何非 explicitly allowed 的域名

### 縮小攻擊面

Sandboxing 限制以下情境的潛在危害：
- 惡意 NPM package 或其他惡意依賴
- 含安全漏洞的 build script 或工具
- 社會工程攻擊（誘導使用者執行危險指令）
- Prompt injection 攻擊（誘導 Claude 執行危險指令）

### 透明操作

Claude Code 嘗試存取 sandbox 外的 network 資源時：
1. 操作在 OS 層被封鎖
2. 使用者立即收到通知
3. 可選擇：拒絕 / 允許一次 / 永久更新 sandbox 設定

---

## 安全限制（Security Limitations）

### Network Sandbox 限制

內建 proxy 從 client 提供的 hostname 決策，**不做 TLS inspection**。容易被以下技術繞過：

- **Domain fronting**：表面是 allowed domain，實際流量到其他 host

> **允許 `github.com` 等廣域名**可能為資料洩漏創造路徑。如需更強保障，設定[自訂 proxy](#network-設定) 做 TLS termination 並安裝 CA 憑證到 sandbox 內。

### Unix Socket 特權升級

`allowUnixSockets` 設定可能意外允許存取強大系統服務，例如 `/var/run/docker.sock` 等同賦予 host 系統完整存取權。

### Filesystem 設定過寬導致的特權升級

對以下目錄過寬的寫入權限可能造成 code execution：
- `$PATH` 中含有 executable 的目錄
- 系統設定目錄
- 用戶 shell 設定（`.bashrc`, `.zshrc`）

### Linux Sandbox 強度

Linux 實作有 `enableWeakerNestedSandbox` 模式，讓 sandbox 在無 privileged namespace 的 Docker 內工作，但**大幅弱化安全性**。只在有其他隔離保護時使用。

---

## Escape Hatch 機制

Claude Code 內建 escape hatch：當指令因 sandbox 限制失敗時，Claude 會分析失敗原因，並可能用 `dangerouslyDisableSandbox` parameter 重試（走一般 permission 流程）。

若要停用此機制：

```json
{
  "sandbox": {
    "allowUnsandboxedCommands": false
  }
}
```

設為 `false` 後，`dangerouslyDisableSandbox` 完全忽略，所有指令必須沙箱或列在 `excludedCommands`。

---

## 工具相容性注意事項

| 工具 | 狀況 |
|------|------|
| `watchman` | 不相容 sandbox，`jest` 改用 `--no-watchman` |
| `docker` | 不相容，建議加到 `excludedCommands` |
| `kubectl`, `terraform`, `npm` | 可能需要 `allowWrite` 特定路徑 |

---

## Sandbox 不涵蓋的範圍

| 工具 | 隔離方式 |
|------|---------|
| **Built-in file tools（Read/Edit/Write）** | 使用 permission system，不經過 sandbox |
| **Computer use** | 在真實 desktop 執行，用 per-app permission prompt 管控 |

---

## Sandboxing 與 Permissions 的互補關係

| 設定類型 | 適用層次 | 適用工具 |
|---------|---------|---------|
| Permission rules | Claude 工具呼叫層 | 所有工具 |
| `sandbox.filesystem.allowWrite/denyWrite/denyRead/allowRead` | OS 層 subprocess | 只限 Bash subprocess |
| `sandbox.network.allowedDomains/deniedDomains` + `WebFetch` rules | network 層 | Bash + WebFetch |

設定建議：
- `sandbox.filesystem.allowWrite` — 授予 subprocess 特定目錄寫入
- `sandbox.filesystem.denyWrite/denyRead` — 封鎖 subprocess 對特定路徑的存取
- `Read`/`Edit` deny rules — 封鎖 Claude 內建 file tools 的存取
- `WebFetch` allow/deny rules — 控制 WebFetch 工具的域名
- `sandbox.network.allowedDomains` — 控制 Bash 指令可到達的域名

---

## 最佳實踐

1. **起步保守**：從最小權限開始，按需擴充
2. **監控日誌**：檢視 sandbox 違規嘗試，了解 Claude Code 的實際需求
3. **環境特定設定**：開發與生產環境分別設定 sandbox 規則
4. **搭配 permissions**：sandbox + IAM policy 構建縱深防禦
5. **測試設定**：確認 sandbox 設定不會阻斷合法工作流程
6. **同時隔離兩層**：filesystem 和 network 隔離缺一不可

---

## 開源 Sandbox Runtime

```bash
npx @anthropic-ai/sandbox-runtime <command-to-sandbox>
```

可用於沙箱其他程式（如 MCP server）。Source code：[github.com/anthropic-experimental/sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime)

---

## 平台支援

| 平台 | 支援狀態 |
|------|---------|
| macOS | 完整支援（Seatbelt）|
| Linux | 完整支援（bubblewrap + socat）|
| WSL2 | 完整支援（bubblewrap + socat）|
| WSL1 | **不支援**（缺 Linux namespace）|
| Windows native | 規劃中 |

---

## 延伸閱讀

- [Security](https://code.claude.com/docs/en/security) — 完整安全功能與最佳實踐
- [Permissions](https://code.claude.com/docs/en/permissions) — Permission 設定與存取控制
- [Settings](https://code.claude.com/docs/en/settings) — 完整設定 reference（sandbox 設定在 `#sandbox-settings`）
- [CLI reference](https://code.claude.com/docs/en/cli-reference) — 命令列選項
- [Sandbox runtime（GitHub）](https://github.com/anthropic-experimental/sandbox-runtime) — 開源 sandbox runtime
- [09-secure-deployment](/research/best-practices/09-secure-deployment) — 安全部署完整指南（含 Docker/gVisor/VM 比較）
