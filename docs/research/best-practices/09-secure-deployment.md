---
title: "Securely Deploying AI Agents — 完整指南"
source: "https://code.claude.com/docs/en/agent-sdk/secure-deployment"
type: best-practices
---

# Securely Deploying AI Agents — 完整指南

> 來源：https://code.claude.com/docs/en/agent-sdk/secure-deployment  
> 收錄日期：2026-05-01  
> 涵蓋：威脅模型、內建安全功能、隔離技術、憑證管理、檔案系統設定

---

## 核心威脅模型

Agent 可能因 **prompt injection**（惡意內容植入指令）或模型錯誤而採取非預期行動。Claude 模型本身抗 injection，但縱深防禦仍是最佳實踐。

**例**：agent 處理惡意檔案，被指示傳送客戶資料到外部伺服器 → 網路控制可完全阻斷此請求。

---

## Claude Code 內建安全功能

| 功能 | 說明 |
|------|------|
| **Permissions system** | 每個 tool 和 bash 指令可設為 allow / block / prompt。支援 glob pattern（如「允許所有 npm 指令」「封鎖含 sudo 的指令」）。組織可設全員套用的 policy |
| **Command parsing** | 執行 bash 前解析成 AST 並比對 permission rules。無法解析或不符合 allow rule → 需要明確核准。`eval` 等特定構造永遠需要核准 |
| **Web search summarization** | 搜尋結果經摘要後才進入 context，降低惡意網頁 prompt injection 風險 |
| **Sandbox mode** | Bash 指令可在限制 filesystem 和網路存取的沙箱中執行 |

---

## 安全原則

### 安全邊界

將敏感資源（如憑證）置於 agent 環境邊界之外。Agent 出問題時，邊界外的資源不受影響。

**實例**：不直接給 agent API key，改在 agent 環境外跑 proxy 注入憑證。Agent 可呼叫 API，但從不見到實際的 key。

### 最小權限

| 資源 | 限制選項 |
|------|---------|
| Filesystem | 只掛載所需目錄，盡量 read-only |
| Network | 透過 proxy 限制到特定 endpoint |
| Credentials | 透過 proxy 注入，不直接暴露 |
| System capabilities | Container 內移除 Linux capabilities |

### 縱深防禦

多層控制疊加：Container 隔離 + 網路限制 + Filesystem 控制 + Proxy 請求驗證。

---

## 隔離技術比較

| 技術 | 隔離強度 | 效能負擔 | 複雜度 |
|------|---------|---------|--------|
| **Sandbox runtime** | 好（安全預設）| 極低 | 低 |
| **Containers（Docker）** | 依設定而定 | 低 | 中 |
| **gVisor** | 極佳（正確設定下）| 中/高 | 中 |
| **VMs（Firecracker、QEMU）**| 極佳（正確設定下）| 高 | 中/高 |

### Sandbox Runtime（輕量首選）

[sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) 在 OS 層強制 filesystem 和網路限制，無需 Docker。

```bash
npm install @anthropic-ai/sandbox-runtime
```

- **Filesystem**：使用 OS 原語（Linux: `bubblewrap`，macOS: `sandbox-exec`）限制讀寫路徑
- **Network**：透過內建 proxy 路由流量，allowlist 域名
- **限制**：與 host 共用 kernel（無 kernel 層隔離）；proxy 不做 TLS inspection

### Docker Container（硬化配置）

```bash
docker run \
  --cap-drop ALL \                          # 移除所有 Linux capabilities
  --security-opt no-new-privileges \        # 防止 setuid 提權
  --security-opt seccomp=/path/to/profile \ # 限制可用 syscall
  --read-only \                             # root filesystem 唯讀
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \ # 記憶體中的臨時可寫目錄
  --tmpfs /home/agent:rw,noexec,nosuid,size=500m \
  --network none \                          # 移除所有網路介面（透過 Unix socket 溝通）
  --memory 2g \                             # 記憶體上限
  --cpus 2 \
  --pids-limit 100 \                        # 防止 fork bomb
  --user 1000:1000 \                        # 非 root 執行
  -v /path/to/code:/workspace:ro \          # code 唯讀掛載
  -v /var/run/proxy.sock:/var/run/proxy.sock:ro \  # host proxy socket
  agent-image
```

**Unix socket 架構**：`--network none` 時，agent 唯一對外通道是掛載的 Unix socket，連接到 host 上的 proxy。Proxy 強制 domain allowlist、注入憑證、記錄所有流量。

> ⚠️ **絕不掛載** `~/.ssh`、`~/.aws`、`~/.config` 等敏感 host 目錄。

### gVisor（強化 kernel 隔離）

標準 container 共用 host kernel，kernel 漏洞可能導致逃逸。gVisor 在 userspace 攔截 syscall，attack surface 大幅縮小。

```json
// /etc/docker/daemon.json
{"runtimes": {"runsc": {"path": "/usr/local/bin/runsc"}}}
```
```bash
docker run --runtime=runsc agent-image
```

**效能影響**：CPU-bound 無負擔；簡單 syscall ~2× 慢；File I/O 密集 10–200× 慢。

### VM（Firecracker）

提供 hardware 層隔離，每個 VM 有獨立 kernel。Firecracker 可在 125ms 內啟動，記憶體負擔 < 5 MiB。Agent VM 無外部網路介面，透過 `vsock` 連接 host proxy。

### Cloud 部署

1. Agent container 放在無 internet gateway 的 private subnet
2. Cloud firewall rules 封鎖所有 egress，只允許到 proxy
3. Proxy（如 Envoy `credential_injector`）驗證請求、強制 domain allowlist、注入憑證、記錄流量
4. Agent service account 賦予最小 IAM 權限

---

## 憑證管理

### Proxy Pattern（推薦）

在 agent 安全邊界外跑 proxy，負責注入憑證。Agent 送出不含憑證的請求，proxy 加入後轉發。

優點：
1. Agent 永遠看不到實際憑證
2. Proxy 可強制允許的 endpoint 白名單
3. 所有請求都有稽核記錄
4. 憑證集中管理

### 設定 Claude Code 使用 Proxy

**Option 1：`ANTHROPIC_BASE_URL`（只影響 sampling API 請求）**
```bash
export ANTHROPIC_BASE_URL="http://localhost:8080"
```

**Option 2：`HTTP_PROXY` / `HTTPS_PROXY`（系統全域）**
```bash
export HTTP_PROXY="http://localhost:8080"
export HTTPS_PROXY="http://localhost:8080"
```

HTTPS 時 proxy 建立 CONNECT tunnel，無法在不做 TLS inspection 的情況下修改請求內容。

### 常用 Proxy 工具

| 工具 | 用途 |
|------|------|
| [Envoy Proxy](https://www.envoyproxy.io/) | 生產級，有 `credential_injector` filter |
| [mitmproxy](https://mitmproxy.org/) | TLS terminating，可檢查/修改 HTTPS 流量 |
| [Squid](http://www.squid-cache.org/) | 快取 proxy，有 ACL |
| [LiteLLM](https://github.com/BerriAI/litellm) | LLM gateway，含憑證注入和 rate limiting |

### 其他服務的憑證

**方式一：Custom Tool（MCP server）**：Agent 呼叫 tool，實際的認證請求在 agent 邊界外執行。Agent 只看到 tool 介面，不見憑證。

**方式二：Traffic Forwarding（TLS terminating proxy）**：需在 agent trust store 安裝 proxy 的 CA 憑證，設定 `HTTP_PROXY`/`HTTPS_PROXY`。

> ⚠️ 部分程式（如 Node.js `fetch()`）不讀取 proxy 環境變數。Node 24+ 可設 `NODE_USE_ENV_PROXY=1`；或用 `proxychains` / iptables transparent proxy 確保覆蓋。

---

## Filesystem 設定

### 唯讀掛載

```bash
docker run -v /path/to/code:/workspace:ro agent-image
```

**即使唯讀也可能洩露憑證**，掛載前排除或清理以下檔案：

| 檔案 | 風險 |
|------|------|
| `.env`, `.env.local` | API keys、密碼 |
| `~/.git-credentials` | Git tokens |
| `~/.aws/credentials` | AWS access keys |
| `~/.config/gcloud/application_default_credentials.json` | GCP ADC tokens |
| `~/.kube/config` | Kubernetes credentials |
| `.npmrc`, `.pypirc` | Package registry tokens |
| `*-service-account.json` | GCP service account keys |
| `*.pem`, `*.key` | Private keys |

### 可寫位置選項

| 需求 | 方案 |
|------|------|
| 臨時寫入，容器停止即清除 | `--tmpfs /workspace:rw,noexec,size=500m` |
| 審查後才持久化 | Overlay filesystem（變更在獨立 layer） |
| 完全持久化輸出 | 掛載 dedicated volume（與敏感目錄分離）|

---

## 延伸閱讀

- [Claude Code security docs](https://code.claude.com/docs/en/security)
- [Sandbox runtime](https://github.com/anthropic-experimental/sandbox-runtime)
- [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [gVisor Documentation](https://gvisor.dev/docs/)
