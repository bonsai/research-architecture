# Phase 0 — Conceptual Implementation

## Goal

研究構造を先に実装する。コードはまだ書かない。

## In scope

- RQを一文で固定する
- EXTで概念を展開する
- RQ / EXT間の依存関係を整理する
- 共通Ontologyを整理する
- EXPの入口条件を定義する
- RX → Evidenceへの昇格条件を定義する

## Out of scope

- Python / Go等の実装
- 実データ生成
- レンダリング
- モデル学習
- 実験実行

## Exit condition

各RQについて、次の鎖が明示されていること。

```text
RQ
 ↓
EXT
 ↓
EXP entry condition
 ↓
RX / Evidence rule
```

## Principle

**概念計画の実装が終わってからコードを書く。**
