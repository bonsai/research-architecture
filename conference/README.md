# 学会

研究成果を学会発表・論文化するための整理フォルダ。

## 役割

`research-architecture` の研究構造から、学会発表に必要な成果を抽出・編集する。

```text
RQ → EXT → EXP → RX → Evidence
                         ↓
                    Thesis / Revision
                         ↓
                     学会発表
```

## 方針

- 研究問い（RQ）を起点にする
- Evidence と再現性を保持する
- Seminar の議論と実験成果を区別する
- 学会用の要約・発表資料・論文原稿はここで管理する
- 原研究データや実験コードは各 `experiments/` 側を正本とする

## 想定構成

```text
conference/
├── README.md
├── abstracts/       # 要旨
├── papers/          # 論文原稿
├── presentations/   # 発表資料
└── submissions/     # 投稿・査読対応
```
