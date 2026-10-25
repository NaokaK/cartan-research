# 主定理 I（`thm:fixed-log-gluing`）最終独立数学監査

- 監査日：2026-10-25
- 監査者：Claude（Opus 5.5）。Astra の判定（PATCH_REQUIRED → パッチ後 VALID）は前提にせず、独立に検証した。
- 範囲：`lem:snc-ring-equalizer`、`lem:snc-torsor-gluing`、`lem:snc-atiyah-comparison`、`thm:fixed-log-gluing` と、これらが直接依存する定義・補題。主定理 II・III、変形理論、p-curvature は範囲外。
- TeX 原稿は一切変更していない。

---

## 0. 監査対象版の特定（重要）

依頼文の `sncl_log_cartan_mainI_patched_2026-10-24.tex` は、ディスク上に存在しなかった（`~/Desktop/研究` 以下とシステム全体を検索）。
存在したのは次の二つである。

| ファイル | SHA-256 |
|---|---|
| `sncl_log_cartan_mainI_proof_candidate_2026-10-24.tex`（パッチ前） | `38df4957…ccaed6c2f` |
| `mainI_independent_patch.diff`（Astra パッチ） | `9026a3ee…dfc81fcb1` |

そこで、パッチ前の原稿のコピーに diff を `patch` で適用し、scratchpad にパッチ後の版を再構成した（3285 行、SHA-256 `3edb887e…1d953fa7`）。diff は fuzz やエラーなしで適用できた。
**本報告の対象は、この再構成した版である。** 手元に別の「patched」ファイルがある場合は、それがこの版と一致するか照合してほしい。
以下の行番号は再構成版のものである。

---

## 1. 判定一覧

| 対象 | 判定 | 要点 |
|---|---|---|
| `lem:snc-ring-equalizer`（952–992行） | **VALID** | 三つの環同型と sheaf の左完全列は成立する。文言上の推奨が二点ある（§3.1）。 |
| `lem:snc-torsor-gluing`（994–1140行） | **VALID** | henselian lifting、étale 近傍への降下、equalizer algebra、torsor 性、一意性がすべて閉じている。引用の言い回しに推奨が一点ある（§3.2）。 |
| `lem:snc-atiyah-comparison`（1141–1196行） | **VALID** | 関手的な restriction で証明しており、closed gluing を使わない。normal derivative が不要な理由も正しい。 |
| `thm:fixed-log-gluing`（914–946行、証明 1198–1261行） | **VALID** | 必要性と十分性、θ の gluing と同型性、一意性、morphism descent が成立する。循環論法はない。 |
| `lem:restriction`、`lem:boundary-atiyah`、`thm:boundary-structure` の λ^M_ij 部分、`def:strict-log-cartan` | **VALID**（依存部分のみ） | 独立に座標計算で再検証した（§4）。 |

**総合判定：主定理 I は現在の仮定と証明のもとで VALID。** 正式採用を妨げる BLOCKER も、数学的な PATCH_REQUIRED もない。
§6 の項目はすべて任意の編集上の推奨で、論理の欠落ではない。

---

## 2. 共通仮定（証明が実際に用いるもの）

1. k は標数 p > 0 の代数閉体である。X は**strict（simple）**SNC 曲面で、各成分 X_i は smooth、成分の自己交叉はない。記法 D_ij = X_i ∩ X_j と、局所 chart `xy=0`、`xyz=0` はこの仮定を前提としている。
2. H ⊂ G は smooth affine algebraic group で、dim(g/h) = 2 である。H の smoothness は次の三点で本質的に使われる。
   - E_i の smoothness と、Tag 0H74 による lifting。
   - Atiyah 列の局所自由性。
   - k[H] が smooth k-algebra であること。
3. M は semistable-type で、chart は上記の二種類に限る。
4. **projectivity は主定理 I の証明で一度も使われない。** 主張は quasi-compact な SNC 曲面でも成立する。これは隠れた仮定ではなく、余分な仮定である。

隠れた仮定は見つからなかった。とくに次の三つの仮定は**置かれていない**。
- component restriction（nonflat）が kernel と可換であること。
- 構成中の E が finite presentation であること。
- g_ij の normal 方向への延長が存在すること。

---

## 3. 各補題の検証

### 3.1 `lem:snc-ring-equalizer`

**環同型。** 任意の可換環 S とイデアル I, J に対し、次が成り立つ。

  S/(I∩J) ≅ S/I ×_{S/(I+J)} S/J

全射性は次のように示せる。a ≡ b (mod I+J) なら a − b = i + j と書け、s = a − i = b + j を取ればよい。
x, y, z が正則局所環 S の正則パラメータ系の一部なら、S は UFD であり、次が成り立つ。
- (x)∩(y) = (xy)
- (xy)∩(z) = (xyz)（z は xy を割らない素元）
- (x,z)∩(y,z) = (xy,z)（S/(z) で (x)∩(y) = (xy) を使い、z を含むイデアルに引き戻す）

以上より三つの同型は正しい。

**triple の手順。** sections s_x, s_y, s_z が pairwise に一致しているとする。
1. s_x と s_y から s_xy ∈ S/(xy) を作る。
2. s_xy|_{z=0} と s_z|_{xy=0} を、S/(xy,z) の二元として比べる。
3. この二元は S/(x,z) と S/(y,z) への像がそれぞれ s_x と s_y に一致する。したがって (triple-intersection-eq) の単射性により等しい。
4. (triple-ring-eq) を適用する。

論理は正しい。ただし原文の「その z=0 への二つの restriction は三重点で一致するので…一つの section を与える」は、上の 3 の比較を短縮しすぎている。

**sheaf レベル。** 準連接層の列の完全性は stalk、あるいは faithfully flat な étale/strict henselian base change の後で検査できる。closed immersion の pushforward は flat base change と可換である。したがって局所 chart での検査で (snc-cech-equalizer) の左完全性が出る。
補足として、strict SNC なら Zariski 局所環 O_{X,x} もそれ自体 S/(xyz) の形に書ける。理由は次のとおりである。
- 埋め込み次元が 3 なので、O_{X,x} は正則局所環の商である。
- 成分は正則パラメータで切り出される。
- 完備化で比較すれば、定義イデアルは (xyz) に一致する。

右端の全射性は主張しておらず、実際どこでも使われない。**VALID。**

### 3.2 `lem:snc-torsor-gluing`

1. **E_i の性質。** fppf torsor が affine、smooth、surjective、fp であることは fpqc descent から従う。
2. **equalizer algebra 𝒜。** 有限直和、closed pushforward、kernel はいずれも準連接性を保つ。𝒜 は二つの algebra 準同型（成分 i への restriction と、g_ij^# ∘ 成分 j への restriction）の equalizer なので、部分 algebra になる。
3. **H-coaction。** −⊗_k k[H] は完全関手（k は体）なので、kernel と可換である。g_ij の H 同変性から、各成分の coaction が 𝒜 → 𝒜⊗k[H] に因子化する。coassociativity と counit は、単射 𝒜 ↪ ⊕(j_i)_*𝒜_i で検査できる。
4. **strict henselian 自明化。**
   - T_i = T/(x) は strictly henselian で、E_i|_{T_i} は smooth affine かつ空でない。
   - 閉 fiber は分離閉体 κ 上の smooth scheme なので、κ 有理点を持つ。
   - Tag 0H74（R = T_i、A = T_i、I = m の henselian pair）で section に持ち上がる。
5. **triple の手順（非可換群）。**
   - h_12 = 1 にした後、cocycle（g_31 g_23 g_12 = 1、すなわち g_13 = g_23 g_12）から、τ_3 L_{h13} = g_13 τ_1 = g_23 τ_2 = τ_3 L_{h23} となる。よって H(T/(x,y,z)) で h_13 = h_23 である。
   - **左乗法の順序は正しい。**
   - H は affine なので H(−) = Hom(k[H], −) は環の fiber product を保つ。したがって h ∈ H(T/(xy,z)) が得られる。
   - これを henselian pair (T/(z), (xy)) で持ち上げる。
   - triple intersection は reduced な零次元 scheme で、T/(x,y,z) = k である。したがって「各 triple point での等式」は scheme 上の等式と同値になる。
6. **étale 近傍への降下。**
   - Spec T = lim U_α、Spec T_i = lim U_α ×_X X_i（テンソルは colimit と可換）。
   - Tag 01ZC（E_i → X_i は lfp、系は affine 推移の affine scheme）により、section は有限段階に降りる。
   - 有限個の等式 g_ij(s_i) = s_j は、Spec T_ij = lim U_α ×_X D_ij への二つの射の一致である。したがって 01ZC の単射性で有限段階に降りる。
   - **finite presentation を使う対象は既知の E_i に限られ、構成中の E ではない。** この点で循環はない。
7. **𝒜|_U ≅ O_U ⊗ k[H]。** étale base change が equalizer と可換であることと、(snc-cech-equalizer) ⊗_k k[H] から従う。coaction とも両立する。これらの U は X を étale に覆う（X は quasi-compact なので有限個で足りる）。したがって E は étale 局所自明な H-torsor である。
8. **E|_{X_i} ≅ E_i。** canonical な射 𝒜 ⊗ O_{X_i} → 𝒜_i が U 上で同型なので、faithfully flat descent で大域的にも同型になる。**nonflat な component restriction と kernel の可換性を仮定していない**点は正しい処理である。境界比較が g_ij になることは、𝒜 の定義そのものから従う。
9. **一意性。**
   - E' の座標環 ℬ は flat なので、(snc-cech-equalizer) ⊗ ℬ は左完全である。
   - closed immersion の射影公式で ℬ⊗(j_i)_*O = (j_i)_*(ℬ|_{X_i}) となる。
   - よって ℬ は成分の equalizer であり、ℬ ≅ 𝒜 となる。この同型は単射 ℬ ↪ ⊕(j_i)_*ℬ_i により一意である。
   - 「一意な同型を除き一意」は正しい。

**VALID。**

### 3.3 `lem:snc-atiyah-comparison`

- **log derivation の性質。** 相対 log derivation (D, Dlog) は D(α(m)) = α(m)·Dlog(m) を満たす。したがって chart の生成元が生成する component ideal とその和を保つ。これにより T^log|_D → Q = T_D(−log P) が定まり、経路（X → X_i → D と X → D）によらない。よって q_j λ^M_ij = q_i が成り立つ。
- **triple chart。** (Dlog x, Dlog y, Dlog z) = (a_x, a_y, a_z)（和は 0）とすると、D = (x=y=0) への制限は a_z·z∂_z になる。これは原文と一致する。
- **大域的 E_H の場合。** At^log(E_H)|_D → At(F)(−log P) ×_Q T^log|_D は局所自明化で (c,v) ↦ ((c,q(v)),v) となり、同型である。rank は (dim h + 1) + 2 − 1 = dim h + 2 で一致し、q は全射である。成分側の同型も同じ restriction から作られる。したがって成分間の比較は、A 成分では λ^M_ij（定義どおり）、Atiyah 成分では F_i ≅ F ≅ F_j による転送 At(g_ij) になる。
- **Λ^M_ij の well-definedness。** σ(At(g)a) = σ(a) = q_i(v) = q_j(λv) なので、Λ^M_ij は fiber product に値を持つ。
- **closed gluing との関係。** この補題は closed gluing を使わず、任意の大域的 torsor に適用できる。したがって、十分性の証明で構成した torsor に適用しても循環しない。

**VALID。**

---

## 4. 直接依存する既存補題の再検証

- **`lem:restriction`（(atiyah-restriction) まで）**
  - double chart：Ω^log は dlog x、dz を基底とし、双対基底は x∂_x − y∂_y、∂_z である。(x=0) への制限 −y∂_y、∂_z は T_{X_i}(−log D_i) の基底になる。
  - triple chart：x∂_x − y∂_y、y∂_y − z∂_z を (x=0) に制限すると −y∂_y、y∂_y − z∂_z になる。これは ⟨y∂_y, z∂_z⟩ の基底である。
  - torsor 方向では恒等写像であり、H-descent も成り立つ。**VALID。**
- **`lem:boundary-atiyah`**：(normal-sequence) と fiber product の同型は、局所表示 (a,v) ↦ ((a,q_i v),v) で確認できる。**VALID。**
- **`thm:boundary-structure`（λ^M_ij と (normal-sign) のみ）**
  - triple chart で直接計算すると、λ(y∂_y) = −x∂_x であり、(normal-sign) は正しい。
  - 一方、λ(z∂_z^{(i)}) = z∂_z^{(j)} − x∂_x となる。つまり tangent lift は λ で保たれず、normal 成分だけずれる。
  - これは本文が「tangent direction は quotient であって canonical な subline ではない」と述べ、λ をそのまま A_i 全体の同型として使っていることと**整合している**。主定理 I は q_j λ = q_i だけを使うので問題はない。
- **`def:strict-log-cartan`**：H が smooth なので Atiyah 列は局所分裂し、局所自由になる。rank は dim h + 2 = dim g である。**VALID。**

---

## 5. 重点検証事項への回答

| # | 事項 | 結論 |
|---|---|---|
| 1 | double/triple chart の equalizer と sheaf 性 | 成立する（§3.1）。stalk または faithfully flat な base change で検査でき、右端の全射性は不要。 |
| 2 | strict henselian 自明化から étale 近傍への降下 | 01ZC で section と等式の両方が有限段階に降りる（§3.2-6）。 |
| 3 | compatible sections の fp 降下と等式の降下 | fp を使う対象は既知の E_i だけで、等式は Mor の colimit の単射性で降りる。成立する。 |
| 4 | equalizer algebra の準連接性、H-action、torsor 性 | 成立する（§3.2-2, 3, 7）。 |
| 5 | nonflat な成分制限と、大域的 torsor の存在・一意性 | 成分制限は局所自明化した後で比較しており、kernel との交換を仮定していない。一意性は ℬ の flatness で示されている（§3.2-8, 9）。 |
| 6 | Atiyah comparison と Λ^M_ij の一致 | 関手的 restriction により一致する（§3.3）。 |
| 7 | triple point の normal 方向と、normal derivative が不要な理由 | v(J) ⊂ J なので v(f) mod J = q_i(v)(f mod J) となり、normal log generator は Q で 0 になる。triple point でも Q の生成元は z∂_z である。必要な微分は境界上の At(g_ij) に含まれるものだけである。λ が tangent lift を normal 方向にずらすこと（§4）は、fiber product の定式化に吸収されている。 |
| 8 | Hom equalizer による Cartan map の gluing と同型性 | 詳細は下記。成立する。 |
| 9 | morphism descent、必要十分性、循環論法 | 詳細は下記。循環なし。 |

**#8 の詳細。**
- ℱ = ℋom(𝒰, 𝒱) は局所自由なので flat である。したがって (cartan-hom-equalizer) は左完全になる。
- source が有限局所自由なので、ℋom の base change が成り立つ。
- 境界での差が 0 になることは、full compatibility と §3.3 から従う。
- θι = ι_1 は ℋom(ad E_H, 𝒱) の単射性から従う。
- 同型性：det θ はすべての閉点で非零である。非閉点で消えるなら、その閉包に含まれる閉点でも消えるはずなので矛盾する。よって det θ は unit である。

**#9 の詳細。**
- 必要性：大域的実現から g_ij = ψ_j ψ_i^{-1} とすれば、cocycle は自動的に成り立ち、(full-compatibility) は §3.3 から従う。
- 十分性：§3.2 と #8 による。
- morphism descent：H(−) が環の limit を保つことと、affine な overlap 上での一意性から、通常の étale descent で示せる。同変な torsor 射は同型である。θ との可換性は ℋom equalizer の単射性で検査できる。
- 循環：依存関係は ring-equalizer → torsor-gluing、および restriction / boundary-atiyah → atiyah-comparison → 主定理 の一方向だけである。atiyah-comparison は closed gluing に依存しないので、循環はない。

---

## 6. 任意の編集上の推奨（判定には影響しない）

1. **Tag 056U の引用。**
   - 実際の内容（Lemma 33.25.6）は「smooth k-scheme では、分離的な剰余体を持つ閉点が稠密である」というもので、直接「有理点が存在する」とは述べていない。
   - 推奨文：「k が分離閉なら、これらの点は k-有理点であり、空でない smooth scheme では稠密なので存在する」の一文を追加する。
   - その他の引用は原文と一致することを確認した。
     - Tag 0DYD（Lemma 15.11.9）：(A,J) が henselian なら (A,I) も henselian（I ⊂ J）。J = m_B に適用すればよい。
     - Tag 0H74（Lemma 15.13.3）：henselian pair 上で smooth algebra の射が持ち上がる。
     - Tag 01ZC（Prop. 32.6.1）
     - Tag 00QO（Lemma 10.127.3）
2. **`lem:snc-ring-equalizer`。**
   - triple の手順は、§3.1 のとおり「S/(xy,z) の二元が両因子で一致する」と明記するとよい。
   - 「局所環」が Zariski 局所環か étale/strict henselian 局所環かを明記するとよい（どちらでも成立する）。
3. **naturality の明示。** morphism descent と θ の可換性の検査では、(atiyah-restriction) が torsor 射について natural であることを暗黙に使っている。これは構成から直ちに従うが、一文添えるとよい。
4. **定理末尾の文言。** 「morphisms も同じ descent を満たす」は意味が曖昧である。次のような形への言い換えを推奨する。
   > 大域的 strict geometry から、(full-compatibility)〜(triple-cocycle) を満たす descent datum への関手は、圏同値（とくに充満忠実）である。
   証明済みの内容はこの主張を支えている。
5. **仮定の明示。** 共通設定に「strict SNC（成分は smooth で、自己交叉なし）」を明記するとよい。また、projectivity が主定理 I では不要であることを注記してもよい。

---

## 7. 結論

主定理 I を構成する三つの補題と本体の証明は、次の各段階に隠れた仮定や循環を含まず、閉じている。
- 局所計算（SNC 環の equalizer、henselian lifting）
- 大域化（étale 近傍への fp 降下、faithfully flat descent、ℋom equalizer の左完全性）

**判定：VALID。** 依存する補題は次のとおりである。
- `lem:snc-ring-equalizer`
- `lem:snc-torsor-gluing`
- `lem:snc-atiyah-comparison`
- `lem:restriction`
- `lem:boundary-atiyah`
- `thm:boundary-structure`（λ^M_ij と (normal-sign) のみ）
- `def:strict-log-cartan`
- 外部引用：Stacks Tags 056U, 0DYD, 0H74, 01ZC, 00QO

この結論は Astra の最終判定と一致するが、上記の独立した検証に基づくものであり、Astra の判定を根拠にはしていない。正式採用は、§0 の版照合を行ったうえで、§6 を任意で反映してから進めることを推奨する。
