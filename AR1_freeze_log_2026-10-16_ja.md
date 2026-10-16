# A-R1 修正・凍結ログ（2026-10-16）

## 判定

**A-R1: PROVED / FROZEN**（chart-defined marking log structure に対する relative log tangent の restricted comparison に限る）。監査 `audit_A-R1_2026-10-16/final_audit_ja.md` の VI 節に指定された Repair A–D を別名の TeX に反映し、差分と LuaLaTeX コンパイルを検証した。新しい数学的証明・仮定は追加していない。

## 入力と成果物

| 種別 | ファイル | SHA-256 |
|---|---|---|
| 元の凍結 TeX（変更なし） | `equisingular_log_cartan_results.tex` | `a7c14f65508e5d83dcc3a89e04bec5bafb378011f09babf29abd15f48cde4c26` |
| A-R1 反映版 | `equisingular_log_cartan_results_AR1.tex` | `b5a9583c6391bda2a63acfccf0f92e99aac6c25648354c84764bc7a4e23e67bc` |

PDF: `AR1_build/equisingular_log_cartan_results_AR1.pdf`（15頁）。SHA-256 は `shasum -a 256` で取得した。元 TeX の値は監査レポートに記載された監査時ハッシュとも一致する。

## 反映箇所

| Repair | 修正版の行 | 内容 |
|---|---:|---|
| A | 153–174 | `def:pointed` を chart-defined marking log structure の定義に置換。full divisorial log structure は使用せず、両者が nonreduced base 上で異なり得ることを明記。`\nu` を log scheme morphism としない。 |
| B | 118–123, 513–516 | E8 の strict étale chart を明記。§3.1 の枝 log structure を `def:pointed` に結び付けた。 |
| C | 559–651 | `lem:phi-glue` の直後に groupified log comparison、Related lifts（Property (I) と Lemma U）、`lem:AR1` と監査済みの証明経路を収録。 |
| D | 1177–1203 | A-R1 の収録を反映し、connection pullback、associated torsor restricted comparison、relative `p`-curvature、relative dormancy をそれぞれ OPEN / CANDIDATE と明示。R4 の NEEDS LITERATURE CHECK を保持。 |

## 差分・コンパイル検証

- `git diff --no-index` で原本と修正版を照合した。差分は上記の定義、chart の説明、A-R1 の挿入、§7 の状態記述に限られ、128 行追加・11 行削除。
- Corollary 2C を含む MT2 の節全体を原本と修正版で文字単位比較し、一致を確認した。MT2 の statement・仮定・証明は変更していない。
- 修正版を `lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=AR1_build` で3回コンパイルし、成功した。最終パスにエラー、未定義参照、重複ラベル、再実行要求はない。ソース中のラベル55件にも重複・未解決参照はない。
- 最終パスに残る警告は、既存の §2A 見出し内の数式に対する `hyperref` の PDF しおり警告と、変更していない MT2 節の 0.7784 pt の overfull box のみ。A-R1 の判定を妨げない。
- アプリ内の組み込みコンパイラは XeTeX 系エンジンで `luatexja` を処理し、`\directlua` で停止した。文書指定の LuaLaTeX では上記のとおり成功した。組み込みエディタには修正版ソースを開いた。

## 範囲と残件

A-R1 の凍結対象は、定義を明確化した chart-defined log structure における tangent 比較のみ。full divisorial 版、connection pullback compatibility、associated torsor restricted comparison、relative `p`-curvature compatibility、relative dormancy は証明済みとしない。R4 の fs log chart の文献番号照合は未完了のまま保持した。

次の研究課題は connection pullback compatibility、associated torsor 上の restricted comparison、relative `p`-curvature compatibility、relative dormancy の順に検討すること。R4 の一次文献照合は別途必要。
