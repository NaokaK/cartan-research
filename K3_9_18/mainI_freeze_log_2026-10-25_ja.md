# 主定理 I FROZEN 保存記録

- 日付：2026-10-25（Asia/Tokyo）
- 対象：`thm:fixed-log-gluing` とその証明の正式保存版。
- 状態：**主定理 I のみ FROZEN**。ファイルに含まれる主定理 II・III や他の成果を、この保存によって承認・凍結するものではない。
- 今回の作業：既存の独立監査を受けた版の同定、§6 の編集上の推奨への最小限の対応、ファイル・組版の検証、Git 保存。追加の数学的監査は実施していない。

## 1. 既存の独立監査の判定

- **Astra**（`mainI_independent_audit_ja.md`、2026-10-24）：元の候補は **PATCH_REQUIRED**。添付パッチを組み込んだ主定理 I の証明は、明記された共通設定のもとで **VALID**。主定理 I に必要な範囲で未解決の数学的 BLOCKER なし。
- **Claude Opus 5.5**（`mainI_final_opus_audit_ja.md`、2026-10-25）：再構成されたパッチ後の版を独立に監査し、**VALID**。BLOCKER および数学的 PATCH_REQUIRED なし。§6 の5項目はいずれも任意の編集上の推奨。
- 両判定の対象は以下の SHA-256 で同定した監査対象版である。今回の編集後に新たな独立数学監査を受けたという意味ではない。

## 2. 原稿の同定と再構成

指定されたパッチ適用済みの完全原稿は研究フォルダに存在しなかった。
`mainI_independent_patch.tex` は置換用の断片であり、完全原稿として扱わなかった。
元の候補を一時領域へコピーし、次の方式で diff を適用した。

```text
patch --batch --fuzz=0 <候補のコピー> <mainI_independent_patch.diff の絶対パス>
```

適用結果：終了コード0、fuzz・offset・reject なし。再構成版は3285行。
監査対象 SHA-256 は指定値と完全一致した。

```text
3edb887efb56ae54ade19cdbe63e0644308923fe2814bdda850ed1270d953fa7
```

元ファイルと監査報告書は変更していない。保存対象の入力ファイルの SHA-256：

| ファイル | SHA-256 |
|---|---|
| `sncl_log_cartan_mainI_proof_candidate_2026-10-24.tex` | `38df49574619a45033246c71e253c27542e2c7e4232371fe6bc9bdeccaed6c2f` |
| `mainI_independent_patch.diff` | `9026a3ee1ce86c163fd4c707f9d41e16b302fce7c0557cae07321e9dfc81fcb1` |
| `mainI_independent_audit_ja.md` | `2b60c47e2639cc935d71766c2ebecfeb4b243d075d57a470ae93b58bc6b89eb2` |
| `mainI_final_opus_audit_ja.md` | `b12aac332945ae6d569fea6843e85b6d643e6ef760b3b55ab2b1bce0a41136d1` |

## 3. 最終版

- ファイル：`sncl_log_cartan_mainI_frozen.tex`
- SHA-256：`cbd55255f2d4f19f66d3f5ed8e9e5fd959a0101fc7069ad1b23804b9d1fde5c6`
- 監査対象版からの編集差分：`mainI_freeze_editorial.diff`。この差分は Astra の独立パッチ適用後の版を基準とする。

## 4. 変更箇所

以下の行番号は監査対象版 → 最終版の対応。本文の編集は Opus §6 の5項目に限る。

| 推奨 | 行番号 | 編集内容 |
|---|---|---|
| §6-1：Tag 056U | 1044–1046 → 1048–1052 | smooth scheme で基礎体上 separable な剰余体を持つ閉点が稠密であり、基礎体が separably closed なら有理点になることから、非空 closed fiber に有理点が存在する、と引用の役割を明記。lifting の議論は不変。 |
| §6-2：局所環 | 955–956 → 958–959 | étale chart 上の局所環と明記。環同型・パラメータの仮定は不変。 |
| §6-2：triple equalizer | 987–989 → 990–993 | `S/(xy)` 上の section と第三成分の section の `S/(xy,z)` への像を比較し、両因子 `S/(x,z)`・`S/(y,z)` での一致から単射性を使う、と既存の手順を展開。 |
| §6-3：naturality | 1182の直後 → 1189–1191 | `(atiyah-restriction)` が torsor 同型について natural であり、morphism descent の Cartan map の可換性の検査にも使えると明記。 |
| §6-4：morphism descent | 945 → 947–948 | 「morphisms も同じ descent」を、大域的 strict geometry から条件を満たす descent datum への restriction functor の圏同値（特に充満忠実）という表現に明確化。既存の対象・射の降下の結論を言い換えたもの。 |
| §6-5：strict SNC | 288 → 289–290 | 共通設定の SNC が strict（simple）で、各成分が smooth、自己交叉なしであると明記。監査で用いられた既存の SNC の意味を明示。 |

そのほか、冒頭のコンパイル例のファイル名を最終版に合わせ、主定理 I のみの FROZEN 日付と本ログへのコメントを追加した（3–5 → 3–6行）。
projectivity は維持し、非固有な曲面への一般化は行っていない。
定理の必要十分条件、条件式、群・log chart の仮定、証明の論理構造は変更していない。
主定理 I 本体の `\begin{proof}[主定理Iの証明]` から対応する `\end{proof}` までの本文はバイト単位で同一。

## 5. 最終検証

- 監査対象版・最終版の双方について **upLaTeX を3回、dvipdfmx を1回**実行。すべて終了コード0、両PDFとも44ページ。
- 原稿の指定エンジンは upLaTeX。アプリ内蔵 Tectonic は `jsarticle` が要求する pLaTeX2e 形式に対応せず失敗したため、ソースを変更せず、インストール済みの指定エンジンで検証した。
- 最終パスに未解決参照・重複ラベル・再実行要求・LaTeX/Package 警告なし。
- `155` ラベルすべてを保持し、`214` 参照に未定義なし。コンパイル後のラベル番号も両版ですべて同一。編集による改ページで一部のページ番号は変化する。
- `begin/end` の `182` 環境は順序を含めて対応。
- Overfull hbox 1件（2.39105pt）、Underfull hbox 2件は監査対象版にも同じものが存在する。対応箇所は未変更の後続本文（監査対象版1389–1397、2027、2029行 → 最終版1398–1406、2036、2038行）。範囲外のため修正していない。
- 編集した7つの差分ブロックを照合し、予定外の本文変更なし。
- Git の whitespace 検査は TeX・Markdown では問題なし。diff ファイルでは空行の context marker（半角スペース）などを警告するが、unified diff の保持に必要なため変更しない。元の独立パッチは SHA-256 を保持した。
- 主定理 I の status remark に続く `Residue matchingだけでは不十分` の example 以降、文書末尾まで（主定理 II・III の主張・証明を含む）は監査対象版とバイト単位で同一。その共通部分の SHA-256：`a876e663302b87f777a20419221537ccafd4a877ce39290d8e976589eb576802`。
- 作業開始時に研究リポジトリ内の既存 `345` ファイルを SHA-256 で記録し、既存ファイルに変更・削除がないことを確認した。
- PDF の編集箇所周辺（5、13–18ページ）を画像で確認。付属 Poppler の画像化では日本語が欠落する表示問題があったため、Ghostscript で同じPDFを画像化して確認した。ソース・フォント設定の変更は行っていない。

再現用コマンド（補助ファイルは一時ビルドディレクトリへ出力）：

```sh
uplatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=<build-dir> sncl_log_cartan_mainI_frozen.tex
# 同じコマンドを合計3回実行
# DVIからPDFへ変換
dvipdfmx -o <build-dir>/sncl_log_cartan_mainI_frozen.pdf <build-dir>/sncl_log_cartan_mainI_frozen.dvi
```

## 6. Git 保存の範囲

開始時のローカル main は origin/main に対して4コミット先行・1コミット遅延していた。
既存のローカル履歴と作業ファイルを維持するため、fetch 後の origin/main
（`d6d2eab6e881cb5240da032df55933e174691d12`）を基点とする一時 worktree で、以下の7ファイルだけを追加する。

- 元の証明候補
- Astra の diff と監査報告書
- Opus の最終監査報告書
- FROZEN TeX
- 本 freeze log
- 編集差分 `mainI_freeze_editorial.diff`

保存先：`git@github.com:NaokaK/cartan-research.git` の `main`。
他の未追跡ファイルや既存のローカル4コミットを今回の push に含めない。
本ログ自身を含むコミットの識別子と push の成否は、Git 履歴・リモート ref の照合および作業完了報告で示す。

## 7. 監査・freeze の対象外

- 主定理 II・III、およびそれらに固有の補題・証明・結論の数学的正当性。
- 変形理論、p-curvature、smoothing、その他の研究成果。
- 任意の fs log smooth morphism、複数 active 方向、Kummer 重複度、horizontal log boundary など、監査対象の chart 仮定を超える一般化。
- projectivity の除去、仮定の緩和、新しい定理の追加、追加の独立数学監査。

コンパイルとファイル整合性の検査は数学的証明の代替ではなく、今回の数学的判定は上記の既存独立監査の記録に帰属する。
