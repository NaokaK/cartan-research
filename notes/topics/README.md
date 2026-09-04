# notes/topics/

テーマ別の研究メモ。3つの過去セッション（logarithmic / zp / level）を統合していくための場所。

現時点では**骨組みのみ**であり、内容は未記入。原資料は `handoff/` にあり、
そちらは原本として凍結する（内容を書き換えない）。

## ディレクトリ

| ディレクトリ | 内容 | 対応する原資料 |
|---|---|---|
| `00-common/` | 3テーマ共通の土台。規約・タグ語彙・文献台帳 | 3資料すべて |
| `10-logarithmic/` | log stratified parabolic geometry と holonomy | `handoff/logarithmic-chat.md` |
| `20-zp-residues/` | 正標数における $\mathbb{Z}_p$ 値留数 | `handoff/zp-chat.md`, `handoff/zp-residues-v2.tex` |
| `30-level/` | 有限レベル現象と dormant opers | `handoff/level-chat.md`, `handoff/log-level-opers.tex`, `handoff/verify_p5.py` |
| `90-crosscutting/` | テーマをまたぐ主張、不一致の台帳、横断的な優先順位 | 3資料すべて |

## 各テーマ内のファイルの役割

`CLAUDE.md` の規則（`results.tex` には確立した結果のみ）を守りつつ、
中間状態の主張を失わないための分割：

| ファイル | 入れてよいもの |
|---|---|
| `overview.tex` | 目的、方針、現在の到達点 |
| `definitions.tex` | 定義、記法、規約 |
| `results.tex` | **確立した結果のみ**（無条件） |
| `conditional.tex` / `to-polish.tex` / `partial.tex` | 中間状態（依存あり／要清書／穴を自覚） |
| `questions.tex` | 未解決問題、gap、予想、文献確認事項 |
| `failed.tex` | 失敗したアプローチとその理由（削除しない） |

## 記入の規則

1. 各主張には地位タグを付ける。語彙は `00-common/status-tags.tex` に従う。
2. 原資料から移した主張には、出典として `handoff/` の該当節を明記する。
3. 原資料のタグを勝手に昇格させない。特に、あるテーマで [推測] のものが
   別のテーマで証明されているように見える場合でも、定義の同値性が
   確認されるまでは昇格させず、`90-crosscutting/` に照合課題として記録する。
4. 未解決の不一致は `90-crosscutting/discrepancies.tex` に登録し、
   どちらかを正しいものとして採用しない。

## main.tex との関係

`main.tex` はまだ `notes/topics/` 以下を `\input` していない。
配線するかどうかは内容の記入が進んでから判断する。
