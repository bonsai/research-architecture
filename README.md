# research-architecture

建築研究の**概念計画を実装するリポジトリ**。

現在は Phase 0。コード・実験実行は行わず、研究問い・概念展開・Ontology・Issue構造を先に固定する。

## Research flow

```text
RQ  Research Question   研究問い
 ↓
EXT Extension           概念の拡張・展開
 ↓
EXP Experiment          実験・実装
 ↓
RX  Research eXperience 観察・経験
 ↓
Evidence               根拠
 ↓
Thesis / Revision      理論・問いの更新
```

### Phase rule

```text
Phase 0 = Conceptual implementation
  RQ / EXT / Ontology / dependencies / acceptance
  → code: NO

Phase 1 = Experimental implementation
  EXP / data / code / execution
  → code: YES
```

## Repository structure

```text
questions/     RQ: 研究問い
extensions/    EXT: 概念の拡張・展開
experiments/   EXP: 実験・実装（Phase 1）
rx/            RX: 観察・経験
ontology/      共通語彙・構造
```

`extensions/` は実験置き場ではない。`EXT` は RQ から、概念・データ・規則・関係・評価・実験契約などを展開する層である。

## Issue rule

Issueは実装タスクではなく研究構造を管理する。

- `RQ-xxx`: 一文の研究問い。Hypothesis / Antithesis / Acceptance を持つ。
- `EXT-xxx`: RQから展開する概念・方法・データ契約・評価枠組み。
- `EXP-xxx`: EXTを検証する実験。コードはPhase 1から。
- `RX-xxx`: 実験・観察から得た経験、観察、次の問い。

原則として **1 RQ → 1 primary EXT → 0..n EXP → 0..n RX**。

## Current research sequence

```text
RQ-001 Corpus
   ↓ EXT-001 Data / Geometry / Feature
RQ-002 Geometry → Feature
   ↓
RQ-003 Visualization
   ↓
RQ-004 Visualization → Evidence
   ↓
RQ-005 Representation comparison
   ↓
RQ-006 Object identity
   ↓
RQ-007 Geometry ↔ Semantic
   ↓
RQ-008 Transformation / MADORI → Grammar
   ↓
RQ-009 Time / Body / Light / View
   ↓
RQ-010 Interactive Space / Time / Semantic
```

この順序は依存関係の目安であり、すべてを直列実装することを意味しない。

## Principle

> 先に研究構造を実装し、あとからコードを実装する。
>
> Concept → RQ → EXT → EXP → Code
