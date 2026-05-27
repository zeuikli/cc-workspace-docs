---
url: "https://zenn.dev/biscuit/articles/llm-engineering-layers-bottleneck-shift"
title: "prompt / context / agent / harness: ボトルネック移動で読むLLM engineeringの系譜とその先"
author: "biscuit"
archived: 2026-05-27
domain: zenn.dev
published: 2026-05-24
tags: [llm, prompt-engineering, context-engineering, agent-engineering, harness-engineering, bottleneck, eval, governance]
word_count: "約 2,500 字"
---

# prompt / context / agent / harness: ボトルネック移動で読むLLM engineeringの系譜とその先

> **來源**：[zenn.dev](https://zenn.dev/biscuit/articles/llm-engineering-layers-bottleneck-shift)
> **作者**：biscuit
> **發布日期**：2026-05-24（更新：2026-05-25）
> **收錄日期**：2026-05-27

---

## Overview / 概要

LLM と周辺技術の成熟に伴い、技術的ボトルネックはモデル本体から外側へと順次移動してきた。prompt → context → agent → harness という4つの工学レイヤーは互いを「置き換える」トレンドではなく、累積的なアーキテクチャとして積み重なっている。著者は次のボトルネックとして eval と governance を予測する。

**核心主張**：「LLM と周辺技術の成熟に伴い、ボトルネックはLLM本体から外側へと移動する。」

---

## 4つのエンジニアリングレイヤー

| レイヤー | ボトルネック | 主要技術 |
|----------|-------------|----------|
| **Prompt** | 入力の最適化 | Few-shot learning、Chain-of-Thought |
| **Context** | 情報のキュレーション | RAG、token compaction、sub-agent isolation |
| **Agent** | 推論ループ設計 | ReAct、ツールオーケストレーション、マルチエージェント |
| **Harness** | 実行環境 | サンドボックス、スケジューリング、制御機構 |

---

## Prompt Engineering 時代

モデルへの入力を精巧に調整することがボトルネックだった時代。Few-shot learning や Chain-of-Thought（CoT）などのテクニックが中心。

しかし「Prompting Inversion」（Imran Khan, arXiv:2510.22251）が示すように、推論モデルの進化によりプロンプトテクニックの効果は逆転しうる。制約プロンプトが中位モデルでは有効でも、高度なモデルでは「hyper-literalism」を誘発して性能を下げる。最適なプロンプト戦略はモデル能力と共進化する必要がある。

---

## Context Engineering 時代

コンテキストウィンドウの拡大だけでは品質は保証されないことが明らかになった時代。

Microsoft-Salesforce の研究（Laban et al., arXiv:2505.06120）によれば、マルチターン会話では6つの生成タスクで平均39%のパフォーマンス低下が確認された。トークン上限が拡大しても文脈管理の質がボトルネックになる。RAG、token compaction、sub-agent isolation などのテクニックがこの課題に対応する。

---

## Agent Engineering 時代

自律的な推論ループ設計にボトルネックが移動した時代。ReAct フレームワークが observe-think-act サイクルを定式化し、プラットフォーム API がツールインテグレーションを標準化した。マルチエージェントシステムの台頭もこの時期に重なる。

---

## Harness Engineering 時代

エージェントの実行インフラを抽象化することがボトルネックとなった現在。

Philipp Schmid のアナロジーでは、harness は「OS」、agents は「applications」として位置づけられる。Harvey AI の事例では、モデルを変更せずにharness側だけの修正で「実質的な精度改善」を達成した。

Harness は以下を担う：
- サンドボックス化されたコード実行
- ツール呼び出しのスケジューリングと制御
- セキュリティ境界の設定
- エージェント間通信の管理

---

## 次のフロンティア：Eval と Governance

### Eval レイヤー

生成システムの出力品質を定義することが次のボトルネックとなる。従来のMLメトリクスを超えたドメイン固有の基準が必要。Galileo は eval を CI/CD に統合するアプローチを推進し、AWS などは評価をオブザーバビリティフレームワークに組み込む。

### Governance レイヤー

エージェント間（A2A）通信の可視性が極めて不十分。「A2A 通信を完全に把握している組織はわずか24.4%」（Gravitee, State of AI Agent Security 2026）。

整備されつつある標準：
- **MCP Authorization**：OAuth 2.1ベース
- **SPIFFE**：エージェントアイデンティティフレームワーク
- **NIST Agent Interoperability Profile**：2026年Q4予定

---

## 規制環境

- **EU AI Act**：2026年8月から施行開始
- **NIST AI Agent Standards Initiative**：アイデンティティ・権限・アクション・監査証跡の4次元でガバナンスを正式化する取り組み（2026年2月発表）

---

## まとめ

4つのエンジニアリングレイヤー（prompt / context / agent / harness）はそれぞれ独立した「トレンド」ではなく、ボトルネックの移動を反映した累積的な構造として理解すべきである。そして現在、eval と governance が次のボトルネックとして台頭しつつある。
