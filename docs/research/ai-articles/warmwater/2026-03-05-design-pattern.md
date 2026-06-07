---
url: "https://warmwater.dev/blog/design-pattern"
title: "Design Pattern 深度解析：不只是套模板，而是知道什麼時候不該用"
date: 2026-03-05
category: Tutorial
source: warmwater.dev
---

[
← Tutorial ](/blog?tag=Tutorial)  Tutorial 
 
# Design Pattern 深度解析：不只是套模板，而是知道什麼時候不該用
 
 2026-03-05 · — views  
  
  
> 
寫給已經聽過 Design Pattern、但不確定「什麼時候該用、什麼時候是 over-engineering」的工程師。


## 前言：Vibe Coding 時代，你更需要懂 Design Pattern


現在是 Vibe Coding 的時代。Cursor、Copilot、Claude Code 幫你寫完大部分的程式碼，你一個下午就能 ship 一個 MVP。很爽，但問題來了——


當 AI 幫你把一個簡單的 config 讀取包成三層 Abstract Factory、用 Observer 去處理一個只有一個 listener 的事件、或者對只用一次的邏輯硬套 Strategy Pattern 的時候，你看得出來這些是 over-engineering 嗎？


Vibe Coding 讓你寫得更快，但不代表你可以不懂。**恰恰相反，當產出速度變快，你需要更強的判斷力來判斷 AI 生成的架構是不是合理的——尤其是它套的 Design Pattern 到底解決了什麼問題，還是只是增加了複雜度。** AI 很擅長寫出「看起來很專業」的程式碼，但它分不清楚「需要彈性」跟「過度設計」的界線。


這篇文章不是要教你背 23 個 GoF Pattern，而是挑出實務中最常遇到的幾個，講清楚**什麼時候該用、什麼時候不該用、用了之後要付出什麼代價**。


---


## 目錄


- Singleton — 全域唯一實例
- Factory Method — 把建立物件的決策延後
- Strategy — 把演算法抽成可替換的模組
- Observer — 事件驅動的鬆耦合通知
- Decorator — 不改原始碼就加功能
- Adapter — 讓不相容的介面合作
- Builder — 一步步組裝複雜物件
- Producer-Consumer — 非同步解耦生產與消費
- 總整理：什麼時候該用、什麼時候別用


---


## 1. Singleton — 全域唯一實例


### 場景


整個應用程式只需要一個 DB connection pool、一個 config 物件、或一個 logger instance。你不希望每次都重新建立，也不希望有兩個互相衝突的實例。


### 怎麼用（Go）


```
// Go 最慣用的方式：sync.Once
// db.go
package db

import (
 "database/sql"
 "sync"
)

var (
 pool *sql.DB
 once sync.Once
)

func GetPool() *sql.DB {
 once.Do(func() {
 pool, _ = sql.Open("postgres", dsn)
 })
 return pool
}

```


`sync.Once` 保證 init function 只執行一次，天生 goroutine-safe，不需要自己管 mutex。


### 利


- 保證全域唯一，避免重複建立昂貴資源
- 延遲初始化（lazy init），用到才建立
- 簡單好理解


### 弊


- 本質上是全域變數，任何地方都能改它的狀態
- 單元測試很痛——因為狀態跨測試汙染
- 多 goroutine 下要小心 race condition（Go 用 `sync.Once` 可以避免）


### 該用


- DB connection pool、Application config（唯讀）、Logger
- 建立成本高、整個 process 只需要一份的資源


### 不該用


- 只是「不想傳參數」而已——請用 dependency injection
- 有可變狀態的業務邏輯物件
- 需要在測試中替換的元件


### 一句話


> 
**Singleton 解決的是「昂貴資源只該有一份」，不是「我懶得傳參數」。如果你的 Singleton 有可變狀態，先想想是不是設計有問題。**


---


## 2. Factory Method — 把建立物件的決策延後


### 場景


你的系統需要根據條件建立不同類型的物件，但呼叫端不該知道具體建立的是哪個 class。例如：根據使用者選的 provider 建立不同的 LLM client、根據檔案格式建立不同的 parser。


### 怎麼用（Go）


```
// 定義共用 interface
type LLMClient interface {
 Chat(ctx context.Context, prompt string) (string, error)
}

// 各 provider 實作 interface
type OpenAIClient struct{ apiKey string }
func (c *OpenAIClient) Chat(ctx context.Context, prompt string) (string, error) { /* ... */ }

type AnthropicClient struct{ apiKey string }
func (c *AnthropicClient) Chat(ctx context.Context, prompt string) (string, error) { /* ... */ }

// Factory function — Go 不需要 Factory class，一個 function 就夠
func NewLLMClient(provider, apiKey string) (LLMClient, error) {
 switch provider {
 case "openai":
 return &OpenAIClient{apiKey: apiKey}, nil
 case "anthropic":
 return &AnthropicClient{apiKey: apiKey}, nil
 default:
 return nil, fmt.Errorf("unknown provider: %s", provider)
 }
}

// 呼叫端只依賴 LLMClient interface
func HandleRequest(client LLMClient) { /* ... */ }

```


Go 的 implicit interface 天生支援 Factory pattern——struct 只要實作了方法就自動滿足 interface，不需要 `implements` 宣告。


### 利


- 呼叫端不依賴具體 struct，加新 provider 不用改呼叫端
- 建立邏輯集中管理，容易加 validation / logging
- 搭配 registry pattern 可以做到 plugin 式擴展


### 弊


- 多一層抽象，程式碼要多跳一層才看得到真正建立的是什麼
- 如果 provider 只有一兩個，Factory 就是多餘的儀式
- 過度使用會讓 codebase 到處都是 Factory，增加認知負擔


### 該用


- 需要根據 config / 環境切換實作（LLM provider, DB driver）
- 建立邏輯複雜，需要集中管理
- 需要 plugin 式擴展（使用者可以註冊自己的實作）


### 不該用


- 只有一種實作，短期內也不會有第二種
- 用 `switch` 三行就能解決的事
- 物件的建立很簡單，直接 `&Struct{}` 就好


### 一句話


> 
**Factory 解決的是「建立邏輯的分散與耦合」，不是「讓程式碼看起來比較專業」。只有一個實作時，直接 new 就好。**


---


## 3. Strategy — 把演算法抽成可替換的模組


### 場景


同一個流程中，某個步驟有多種可替換的實作方式。例如：不同的定價策略、不同的排序演算法、不同的重試邏輯。關鍵是這些變化是**執行期（runtime）決定**的，不是寫死的。


### 怎麼用（Go）


```
// 方法一：用 function type 當策略（最簡潔）
type PricingStrategy func(order Order) float64

func VIPPricing(order Order) float64 {
 return order.Subtotal * 0.8
}

func HolidayPricing(order Order) float64 {
 return order.Subtotal * 0.7
}

func ProcessOrder(order Order, pricing PricingStrategy) {
 price := pricing(order)
 // ... 後續處理
}

// 使用
ProcessOrder(order, VIPPricing)

// 方法二：用 interface（策略需要狀態時）
type PricingStrategy interface {
 Calculate(order Order) float64
}

type DiscountPricing struct {
 Rate float64 // 可以帶狀態
}

func (d *DiscountPricing) Calculate(order Order) float64 {
 return order.Subtotal * d.Rate
}

```


Go 兩種都很慣用：邏輯簡單用 function type，策略需要帶狀態時升級成 interface。


### 利


- 新策略只要加一個 function 或 struct，不用改既有程式碼（Open-Closed）
- 策略可以獨立測試
- Go 的 function type 和 interface 都很輕量，幾乎零成本


### 弊


- 策略多了之後，要管理「哪個場景用哪個策略」的 mapping
- 如果策略之間有共用狀態，function type 不夠用，要升級成 interface
- 過度拆分會讓邏輯散落各處，追 code 變困難


### 該用


- 同一流程中有 3+ 種可替換的邏輯
- 策略需要在 runtime 動態切換
- 策略需要被獨立單元測試


### 不該用


- 只有兩種，而且短期不會有第三種——用 `if-else` 就好
- 邏輯寫死不會變
- 策略之間有大量共用邏輯（可能該用 Template Method）


### 一句話


> 
**Strategy 解決的是「同一個流程裡可替換的步驟」。Go 裡邏輯簡單用 function type，需要狀態用 interface——不需要搬出 Java 的 abstract class 三件套。**


---


## 4. Observer — 事件驅動的鬆耦合通知


### 場景


當某件事發生時，需要通知多個不相關的模組做出反應。例如：訂單成立後要同時通知庫存、寄 email、記 log，但你不希望訂單模組直接 import 這三個模組。


### 怎麼用（Go）


```
type EventBus struct {
 mu sync.RWMutex
 listeners map[string][]func(any)
}

func NewEventBus() *EventBus {
 return &EventBus{listeners: make(map[string][]func(any))}
}

func (b *EventBus) On(event string, fn func(any)) {
 b.mu.Lock()
 defer b.mu.Unlock()
 b.listeners[event] = append(b.listeners[event], fn)
}

func (b *EventBus) Emit(event string, data any) {
 b.mu.RLock()
 defer b.mu.RUnlock()
 for _, fn := range b.listeners[event] {
 fn(data)
 }
}

// 使用
bus := NewEventBus()
bus.On("order_created", updateInventory)
bus.On("order_created", sendConfirmationEmail)
bus.On("order_created", logOrder)

bus.Emit("order_created", order)

```


Go 版本要注意：`listeners` map 被多個 goroutine 讀寫時需要 `sync.RWMutex` 保護。


### 利


- 發布者和訂閱者完全解耦
- 加新的 listener 不用改發布端
- 適合跨模組的鬆耦合通知


### 弊


- **Debug 地獄**——emit 一個事件，不知道誰會收到、執行順序是什麼
- 事件鏈容易形成隱式依賴（A 觸發 B 觸發 C，出錯很難追）
- 如果 listener panic 了，要不要中斷其他 listener？錯誤處理很難設計


### 該用


- 多個不相關模組需要對同一事件反應
- 發布者不該知道有哪些訂閱者
- 需要 plugin 式擴展（第三方可以掛 listener）


### 不該用


- 只有一個 listener——直接呼叫就好，別繞一圈
- listener 之間有順序依賴（那就不是 Observer 的場景）
- 核心業務邏輯（錯誤處理和執行順序不能含糊）


### 一句話


> 
**Observer 解決的是「一對多的鬆耦合通知」，但如果你需要保證執行順序或錯誤傳播，Observer 反而會製造更多問題。**


---


## 5. Decorator — 不改原始碼就加功能


### 場景


你想在既有的 function 上加 logging、retry、cache、計時等功能，但不想改動原始 function 的程式碼。Go 沒有 Python 的 `@decorator` 語法，但透過 **middleware pattern**（尤其在 HTTP handler）和 **higher-order function** 可以達到同樣效果。


### 怎麼用（Go）


```
// 方法一：HTTP Middleware（最常見的 Decorator 場景）
type Middleware func(http.Handler) http.Handler

func Logging(next http.Handler) http.Handler {
 return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
 start := time.Now()
 next.ServeHTTP(w, r)
 log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
 })
}

func Auth(next http.Handler) http.Handler {
 return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
 token := r.Header.Get("Authorization")
 if token == "" {
 http.Error(w, "unauthorized", 401)
 return
 }
 next.ServeHTTP(w, r)
 })
}

// 串接：從外到內執行 Auth → Logging → handler
mux.Handle("/api", Auth(Logging(handler)))

// 方法二：通用 function wrapper（非 HTTP 場景）
func WithRetry(fn func() error, maxRetries int, delay time.Duration) func() error {
 return func() error {
 for i := 0; i < maxRetries; i++ {
 if err := fn(); err == nil {
 return nil
 }
 time.Sleep(delay)
 }
 return fn()
 }
}

callAPI := WithRetry(func() error {
 return doHTTPRequest(url)
}, 3, time.Second)

```


### 利


- 不改原始 function，符合 Open-Closed Principle
- 可重用：同一個 middleware 套在多個 handler 上
- Go 的 HTTP middleware 生態成熟（chi, echo 都原生支援）


### 弊


- 疊多層 middleware 後，debug stacktrace 會很深、很難讀
- 串接順序（從外到內）不直覺，容易搞混
- 非 HTTP 場景下 higher-order function 的 type signature 會變複雜


### 該用


- 橫切關注點：logging、retry、auth check、caching
- 多個 handler 需要同一種行為增強
- 行為增強可以獨立測試


### 不該用


- 核心業務邏輯——不該藏在 middleware 裡，會很難追
- 只用在一個地方，直接寫在 function 裡更清楚
- middleware 需要存取/修改 handler 的內部狀態


### 一句話


> 
**Decorator / Middleware 解決的是「橫切關注點的重複程式碼」，但不要把業務邏輯藏進 middleware——那只是把複雜度搬到看不見的地方。**


---


## 6. Adapter — 讓不相容的介面合作


### 場景


你的系統定義了一套 interface，但第三方套件的 API 長得不一樣。你不想改自己的 interface，也改不了第三方的程式碼，需要一個中間層做轉換。


### 怎麼用（Go）


```
// 你的系統定義的 interface
type StorageClient interface {
 Upload(ctx context.Context, key string, data []byte) (string, error)
 Download(ctx context.Context, key string) ([]byte, error)
}

// AWS S3 的 SDK API 長得不一樣
// s3.PutObject(ctx, &s3.PutObjectInput{Bucket: ..., Key: ..., Body: ...})

// Adapter：把 S3 SDK 包成你的 interface
type S3Adapter struct {
 client *s3.Client
 bucket string
}

func NewS3Adapter(client *s3.Client, bucket string) *S3Adapter {
 return &S3Adapter{client: client, bucket: bucket}
}

func (a *S3Adapter) Upload(ctx context.Context, key string, data []byte) (string, error) {
 _, err := a.client.PutObject(ctx, &s3.PutObjectInput{
 Bucket: &a.bucket,
 Key: &key,
 Body: bytes.NewReader(data),
 })
 if err != nil {
 return "", err
 }
 return fmt.Sprintf("s3://%s/%s", a.bucket, key), nil
}

func (a *S3Adapter) Download(ctx context.Context, key string) ([]byte, error) {
 resp, err := a.client.GetObject(ctx, &s3.GetObjectInput{
 Bucket: &a.bucket,
 Key: &key,
 })
 if err != nil {
 return nil, err
 }
 defer resp.Body.Close()
 return io.ReadAll(resp.Body)
}

// 你的 code 只依賴 StorageClient interface
func Backup(storage StorageClient, data []byte) error {
 _, err := storage.Upload(context.Background(), "backup/latest.bin", data)
 return err
}

```


Go 的 implicit interface 讓 Adapter 特別自然——`S3Adapter` 不需要宣告 `implements StorageClient`，只要方法簽名對了就自動滿足。


### 利


- 把第三方依賴隔離在 adapter 裡，換 provider 只改 adapter
- 自己的 interface 保持乾淨穩定
- 容易在測試中用 mock adapter 替換


### 弊


- 多一層間接呼叫，每次追 code 要多跳一層
- 如果第三方 API 的語義跟你的 interface 不完全對應，adapter 會變得很 hacky
- 只有一個 provider 時，adapter 就是多餘的 boilerplate


### 該用


- 需要支援多個第三方 provider（S3 / GCS / Azure Blob）
- 想在測試中完全隔離第三方依賴
- 第三方 API 可能改版，想把影響範圍限制在 adapter 內


### 不該用


- 只用一個 provider，而且不打算換
- 第三方 API 跟你的 interface 幾乎一模一樣——直接用就好
- 為了「以防萬一」的假設需求（YAGNI）


### 一句話


> 
**Adapter 解決的是「介面不匹配」，不是「我覺得以後可能會換 provider」。如果只有一個實作，YAGNI。**


---


## 7. Builder — 一步步組裝複雜物件


### 場景


一個物件有大量可選參數，constructor 的參數列表已經長到不可讀。或者物件的建立有多個步驟，需要按順序組裝。


### 怎麼用（Go）


```
// 方法一：Functional Options Pattern（Go 最慣用的 Builder 替代方案）
type QueryConfig struct {
 Table string
 Columns []string
 Where string
 OrderBy string
 Limit int
}

type Option func(*QueryConfig)

func WithColumns(cols ...string) Option {
 return func(c *QueryConfig) { c.Columns = cols }
}

func WithWhere(condition string) Option {
 return func(c *QueryConfig) { c.Where = condition }
}

func WithOrderBy(order string) Option {
 return func(c *QueryConfig) { c.OrderBy = order }
}

func WithLimit(n int) Option {
 return func(c *QueryConfig) { c.Limit = n }
}

func NewQueryConfig(table string, opts ...Option) *QueryConfig {
 cfg := &QueryConfig{Table: table, Columns: []string{"*"}}
 for _, opt := range opts {
 opt(cfg)
 }
 return cfg
}

// 使用：清楚可讀，可選參數隨意組合
config := NewQueryConfig("orders",
 WithColumns("id", "total"),
 WithWhere("status = 'active'"),
 WithOrderBy("created_at DESC"),
 WithLimit(100),
)

// 方法二：Method Chaining（fluent interface）
type QueryBuilder struct {
 config *QueryConfig
}

func NewQueryBuilder(table string) *QueryBuilder {
 return &QueryBuilder{config: &QueryConfig{Table: table, Columns: []string{"*"}}}
}

func (b *QueryBuilder) Select(cols ...string) *QueryBuilder {
 b.config.Columns = cols
 return b
}

func (b *QueryBuilder) Where(cond string) *QueryBuilder {
 b.config.Where = cond
 return b
}

func (b *QueryBuilder) Build() *QueryConfig { return b.config }

// 使用
config := NewQueryBuilder("orders").
 Select("id", "total").
 Where("status = 'active'").
 Build()

```


Go 社群偏好 **Functional Options Pattern**（`grpc.Dial`、`zap.NewProduction` 都用這個），因為它不需要額外的 Builder struct，而且跟 Go 的 variadic function 語法完美搭配。


### 利


- 參數多時可讀性好（Functional Options 或 method chaining）
- 可以在建立時做 validation
- 強制按步驟建立，避免半成品物件


### 弊


- Functional Options 的 `Option` function 多了會很囉唆
- Method chaining 需要額外的 Builder struct
- 如果只有 2-3 個參數，直接用 struct literal 更直覺


### 該用


- 物件建立有嚴格的步驟順序（必須先設定 A 才能設定 B）
- 需要 fluent interface 給外部使用者用（SDK / query builder）
- 大量可選參數，需要合理的 default


### 不該用


- 參數少於 5 個——直接用 struct literal
- 內部使用的簡單 config struct
- 所有欄位都是必填的，直接用 struct 就好


### 一句話


> 
**Go 裡用 Functional Options Pattern 取代傳統 Builder 是主流做法。但如果 struct 欄位不多，直接 `&Config{Field: value}` 最簡單——別為了三個參數寫十個 Option function。**


---


## 8. Producer-Consumer — 非同步解耦生產與消費


### 場景


生產資料的速度和消費資料的速度不一致。例如：API 接收 request 的速度遠快於處理速度、行情資料進來的速度遠快於策略計算速度。你需要一個 buffer 來解耦兩邊，讓它們各跑各的。


### 怎麼用（Go）


```
func main() {
 taskCh := make(chan Event, 1000) // buffered channel 當 queue

 // Producer
 go func() {
 for event := range streamEvents() {
 taskCh <- event // blocking if buffer full
 }
 close(taskCh)
 }()

 // 4 個 Consumer
 var wg sync.WaitGroup
 for i := 0; i < 4; i++ {
 wg.Add(1)
 go func() {
 defer wg.Done()
 for event := range taskCh { // channel close 後自動結束
 process(event)
 }
 }()
 }

 wg.Wait()
}

```


Go 的 channel 天生就是 Producer-Consumer pattern——buffered channel 就是 bounded queue，`close()` 就是 shutdown signal，`range` 就是 blocking dequeue。這是 Go 最自然的並發模式。


### 利


- 生產者和消費者速度解耦，各自獨立
- 可以獨立調整 consumer 數量做水平擴展
- Channel 當 buffer，吸收瞬間流量高峰
- 從 in-process channel 到 SQS/Kafka 的思路完全一致


### 弊


- 多了一個 channel 要監控（滿了怎麼辦？空了怎麼辦？）
- 錯誤處理變複雜（consumer panic 了誰來重試？）
- 引入非同步後，debug 和追蹤變困難
- buffer size 設太小會 block producer，設太大會吃記憶體


### 該用


- 生產和消費速度不一致，需要 buffer
- 需要多個 consumer 平行處理
- 要從 in-process 之後擴展到分散式（SQS, Kafka）


### 不該用


- 生產和消費是同步的、一對一的——直接 function call 就好
- 只是想「讓程式碼看起來是非同步的」
- 資料量小、延遲不敏感，同步處理完全夠用


### 一句話


> 
**Producer-Consumer 解決的是「速率不匹配」，不是「我想讓架構看起來比較專業」。如果同步處理就能搞定，別引入不必要的非同步複雜度。**


---


## 9. 總整理：什麼時候該用、什麼時候別用


### 速查表


| Pattern | 解決什麼問題 | 付出什麼代價 | 最常被誤用的場景 |
| --- | --- | --- | --- |
| Singleton | 昂貴資源只該有一份 | 全域狀態、測試困難 | 「懶得傳參數」就用 Singleton |
| Factory | 建立邏輯的解耦與集中 | 多一層抽象 | 只有一種實作也硬用 Factory |
| Strategy | 可替換的演算法步驟 | 策略管理的複雜度 | 只有兩種邏輯就拆成 Strategy |
| Observer | 一對多的鬆耦合通知 | Debug 困難、隱式依賴 | 只有一個 listener 也用 Observer |
| Decorator/Middleware | 橫切關注點的重用 | 多層 stacktrace、順序問題 | 把業務邏輯藏在 middleware 裡 |
| Adapter | 介面不匹配的轉換 | 多一層間接呼叫 | 「以後可能換 provider」的假設需求 |
| Builder | 複雜物件的分步建立 | 多一個 Option 或 Builder | struct literal 就能解決的事硬用 Functional Options |
| Producer-Consumer | 生產消費速率不匹配 | 非同步複雜度、錯誤處理 | 同步就能搞定的場景 |


### 判斷框架：三個問題


在決定是否使用某個 Design Pattern 之前，問自己這三個問題：


- **這個 pattern 解決的問題，我現在真的有嗎？** 還是我在替未來可能的需求提前設計？（YAGNI）
- **引入這個 pattern 的複雜度，值得嗎？** 如果 `if-else` 三行就能解決，多一個 class hierarchy 的維護成本值得嗎？
- **團隊其他人看得懂嗎？** 如果你離職了，接手的人能在 30 秒內理解這段程式碼為什麼要這樣寫嗎？


---


> 
**結語**：Design Pattern 不是越多越好。最好的程式碼不是用了最多 pattern 的程式碼，而是讓人一眼就看懂意圖的程式碼。Pattern 是工具，不是目的。


## 延伸閱讀


- [Python 資料結構深度解析：不只是背複雜度，而是知道什麼時候該用哪一個](/blog/python) — 同系列：資料結構的選型邏輯，和 Design Pattern 的判斷框架互相呼應
- [你的 Prompt 為什麼有效：從 Transformer 機制看 AI 系統設計](/blog/prompt-transformer-ai) — AI 系統也有設計決策：Transformer 架構背後的工程取捨
- [Harness Engineering — AI 工程師的第三個維度](/blog/harness-engineering-ai) — Design Pattern 在 AI 工程的應用：Harness 的 Middleware Pattern 與架構設計

  
  
 [ Tutorial ](/blog?tag=Tutorial) 
 

### 相關文章
[Tutorial

第一個 Claude Skill：用 skill-creator 打包可重用工作流程

2026-05-25
](/blog/create-your-own-claude-skill)[
Tutorial

Claude Code 五個組件的觸發邏輯，以及為什麼 Hooks 是最被低估的那一個

2026-05-21
](/blog/claude-code-hooks-guide)[
Tutorial

為什麼你的 Claude Code 用起來跟別人不一樣？

2026-05-14
](/blog/claude-code-commands-beginner)
