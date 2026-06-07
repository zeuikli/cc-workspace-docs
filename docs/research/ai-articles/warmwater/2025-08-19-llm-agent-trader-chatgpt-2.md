---
url: "https://warmwater.dev/blog/llm-agent-trader-chatgpt-2"
title: "LLM Agent Trader（二）：Strategy Discussion Room"
date: 2025-08-19
category: "Stock&Finance"
source: warmwater.dev
---

[
← Stock & Finance ](/blog?tag=Stock%20%26%20Finance)  Stock & Finance  
#  🤖 LLM Agent Trader: 當ChatGPT遇上股票交易，我打造了一個會思考的交易機器人 (Part2) 
  2025-08-19 · — views      


先感謝大家上次開[表單](https://forms.gle/YzFg6FPWBDNDfjLP9)後踴躍的Feedback (現在還是可以繼續填跟許願), 過了忙碌的一週後, 又持續前進了, 這次新增的依然是一個小概念: **策略討論室**, 可以跟LLM互動, challenge他當天做出決策的動機是什麼


下面是簡易演示版本(我們在跑回測的時候, 已經有一個簡易的交易策略)


以NVDA為交易標的, 目前的交易策略回測結果如下


在**6/25** 這一天有一個賣出, 我覺得趨勢並沒有明顯轉弱, 但是LLM策略做出了賣出的行為, 我認為可以做修正, 所以我決定問他


" 為什麼這天要賣出？如果我不想賣出的話, 應該對現在的策略做出什麼調整? "


使用者可以在策略討論室, 透過自然語言的方式來和AI 互動, AI就會基於使用者的問題, 來做回答, 這裡我們把剛剛的問題填進去, 按下開始討論


(我沒有仔細調整過prompt, 所以把這個當成概念Demo就好XD)


等到LLM分析完後, 就會得到下面的結論了, 包含他為什麼這天要賣出, 以及可以對現有的交易策略做的調整

## 小結


這次完成的feature, 算是之前就有規劃想到的, 可以透過回測, 討論策略, 再次回測的這個循環, 主要也是想要讓大家知道, 策略優化後, 你仍然會有需要去承擔的風險(比如你想更hold得住, 那你勢必有可能要忍受更大的回撤, 或是更痛的停損, 但最後你會有一個你願意相信的策略, 而不是黑盒子


下面是一些大家有留言的Feedback, 挺多人提到要open source的, 但目前的code真的太醜, 我還沒做refactor, 我自己過不去XD 所以應該還要再等等, 但是open source後, 我可以走的變現管道可能也會要調整, 我自己是不排斥, 也說真的就算沒辦法變現就算了, 這次也是挺寶貴的經驗和建議, 想要再次感謝大家


如果大家有要敲碗哪一個功能,一樣可以幫我填[表單](https://forms.gle/QmVJgwWHTmCeCmxP6), 我都會去看的


## 延伸閱讀


- [🤖 LLM Agent Trader: 當ChatGPT遇上股票交易，我打造了一個會思考的交易機器人](/blog/llm-agent-trader-chatgpt) — Part 1：交易機器人的基礎架構與 Demo

- [🤖 LLM Agent Trader: 當ChatGPT遇上股票交易，我打造了一個會思考的交易機器人 (Part3)](/blog/llm-agent-trader-chatgpt-3) — Part 3：開源版本，含 How to Use 與技術討論

- [TradingAgents: Multi-Agents LLM Financial TradingFramework](/blog/tradingagents-multi-agents-llm-financial-tradingframework) — 學術研究版：多 Agent 分工金融交易框架的論文架構
     [ Stock & Finance ](/blog?tag=Stock%20%26%20Finance)[ Implement ](/blog?tag=Implement)  
### 
相關文章

[Implement用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄2026-05-28](/blog/kube-arena)[Harness EngineeringSelf Escalate Agent：刻意設計成不完整的 AI2026-05-09](/blog/self-escalate-agent)[Implement不靠直覺，靠實驗：用 AutoResearch 找到 C++ 的 33x 優化空間2026-04-17](/blog/autoresearch-c-33x)
