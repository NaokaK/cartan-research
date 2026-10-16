# A-R1 Final Definition Consistency Audit

監査日：2026-10-16。対象は relative restricted comparison の定義整合性のみ。Main Theorem 1 / 2 は再証明せず、凍結 TeX は変更していない。

## I. Overall verdict

**VALID WITH TEXTUAL REPAIR**

**A-R1 が現行の統合版 TeX にそのまま適用可能か：CONDITIONAL。** §1 の pointed log structure を、旧稿と同じ **chart-defined marking log structure** と明示することが必要である。現在の「divisorial」の一語だけを根拠に、無条件で適用済みとはできない。

この修正後は、旧監査の Property (I) → restricted power による related 性の保存 → Lemma U という議論を移せる。**基底の reducedness・normality、node の splitness、標数の制限 \(p\ne2\) などの追加仮定は不要。**

ただし、full divisorial log structure を本当に採用するなら、これは同じ対象の言い換えではない。非被約基底では §3.1 の Euler derivation がその log structure の derivation にならない例がある。この読みのままでは既存の比較同型を入力にできず、A-R1 の適用は **NO** である。以下の修正は、原稿の chart 計算が実際に扱っている対象へ定義を合わせるものと位置づける。full divisorial 版が既証だとは判定しない。

### 監査資料と同定

| 略号 | 実際に読んだ資料 | 用途 |
|---|---|---|
| E | [equisingular_family_extension.tex](/Users/naoka/Desktop/研究/equisingular_family_extension.tex) | 旧 family 原稿。874 行 |
| C | [equisingular_log_cartan_results.tex](</Users/naoka/Desktop/研究/cartan-research/nodal curve上/equisingular_log_cartan_results.tex>) | 統合 family 原稿。1107 行 |
| O | [旧 A-R1 監査の転載全文](/Users/naoka/Desktop/研究/audit_A-R1_2026-10-16/opus_audit_transcript.md) | ユーザーが Opus の監査結果として「研究成果の統合」に転載した全10項目 |
| F | [凍結 fixed 原稿](</Users/naoka/Desktop/研究/cartan-research/nodal curve上/freeze_2026-10-15/nodal_log_cartan_results.tex:1536>) | §9 の restricted operation の式と記法のみ |

O はチャット「研究成果の統合」（thread `6ad1dd00-b804-83ec-a896-da7974b5d766`、user turn `0d89dc1d-c32a-45d3-bc86-528c0a2871eb`）から取得した。別チャット「双有理」の最終監査とも内容が一致した。監査者のモデル名そのものは認証していない。ローカルの `equisingular_family_opus55_audit_2026-10-16_ja.md` は MT2 の監査であり、O の代用にはしていない。A-R1 の最初の証明原稿は独立のファイルとしては確認していないため、本監査が照合する証明経路は O に記載されたものに限る。

C は「研究成果の統合」に添付された同名 TeX と SHA-256 が一致した。監査時のハッシュ：

```text
E  14c81913460bbd3ec5cd7cde4898668c0570102a5f084570fc2d9d0c18f15758
C  a7c14f65508e5d83dcc3a89e04bec5bafb378011f09babf29abd15f48cde4c26
F  d98f67b4125f827b007514400589b1dcf7c7347873fe63b6154edda24dd5fd21
```

## II. Definition comparison

行番号は上記の監査時ファイルに対応する。

| 項目 | 旧稿 E | 統合稿 C | A-R1 への影響 |
|---|---|---|---|
| 基礎体 | §1、77行：任意の体、標数任意 | §1、97–101行：perfect field、標数 \(p>0\)、代数閉性不要 | A-R1 には標数 \(p>0\) を使う。C では既に仮定済み。perfectness はこの比較の論理には使用しない |
| 基底 | 77–78行：fs log、Noetherian・reduced 不要 | 105–106行：fs log、Noetherian・reduced・Artinian 不要 | 一致 |
| 曲線の範囲 | (LC)、83–94行：smooth / marking / node への strict étale charts。properness 不要、局所有限表示 | EQ1、113–114行：proper・flat・finitely presented、幾何的 nodal fibre | C の大域的範囲は狭い。A-R1 に properness は不要 |
| log curve chart | (LC)(i)–(iii) | EQ3 = E8、118–134行 | 同じ三種類。C の「chart から log structure が定まる」を strict pullback と明記すると確実 |
| singular locus | (Eq)、95–96行：\(\Sigma=V(\mathrm{Fitt}_1\Omega^1_{X/B})\)、\(\Sigma/B\) étale | EQ2、115–117行：同じ scheme-theoretic locus が flat | C の既存命題 `prop:flat-etale`、274–287行で E8 下の flat ⇔ étale を確認済み。properness により finite も従う。再証明不要 |
| markings | (Mk)、97–98行：\(B\)-étale、nodes と交わらない | E8、122–124行：smooth relative coordinate、互いに交わらず nodes と交わらない | relative coordinate chart では marking は \(B\)-étale。label 不要 |
| 群 | (Gp)、99–100行 | 97–100行 | 実質同じ。A-R1 は tangent の命題で、\(G,H\) を使わない |
| branch separation | 149–153行：\(\operatorname{Bl}_\Sigma X\)、枝 \(A[x]\sqcup A[y]\) | §2.3–2.4、§1 BSD：同じ blow-up と局所 model | total-space normalization とは両稿とも区別。A-R1 は既存の枝分離を使用 |
| \(X\) の marking log | 88–90、104–118行：chart-defined | 122–124行：\(P\to P\oplus\mathbf N\) | 一致 |
| \(\widetilde X\) の log | §1、104–118行、§3、267–270行：chart-defined。full divisorial を明示的に排除 | §1、150–158行：「divisorial log structure」。full か chart-defined か定義が明示されていない | **必須修正箇所**。後続 §3.1 は chart-defined の計算を使っている |
| \(\theta\) | §3、280–285行：\(\theta=(\varphi^{-1})^\vee\) | §3.1、488–539行：同じ定義と \(d\)-compatibility | chart-defined に揃えれば一致 |
| \(\nu\) の log 射性 | 比較は chart 計算で構成 | 155–157行：log 射であることを仮定しない | groupification 上の比較と区別して維持する |
| A-R1 の収録状況 | §10 D1、807–811行、§12、859–864行：次に証明すべきもの | §7、1066–1070行：relative dormancy は OPEN。A-R1 の独立した statement / proof は未収録 | 旧監査が通ったことと TeX へ反映済みであることは別 |

### 「divisorial」は現状で何を意味するか

C の150–158行だけから chart-defined と断定することはできない。498–501行の \(A[x]d\log x\) を使う比較は、chart-defined を採用した場合の記述と一致する。したがって **後続計算から意図は読み取れるが、定義自体は未統一**という判定である。

違いを検出する最小の局所チェックを記す。これは full divisorial という読みの整合性検査であり、別の定理の構築ではない。

\[
A=k[\varepsilon]/(\varepsilon^2),\qquad Y=\operatorname{Spec}A[x],
\qquad Z=V(x),\quad j:Y\setminus Z\hookrightarrow Y.
\]

full divisorial log structure \(M_{\mathrm{div}}=\mathcal O_Y\cap j_*\mathcal O_{Y\setminus Z}^{\times}\) には \(m=x+\varepsilon\) が入る。

\[
(x+\varepsilon)^{-1}=x^{-1}-\varepsilon x^{-2}\quad\text{on }D(x).
\]

しかし原点近傍で \(x+\varepsilon\) は \(ux^n\)、\(u\in\mathcal O_Y^\times\)、\(n\in\mathbf Z\) と書けない。mod \(\varepsilon\) の \(x\)-次数から \(n=1\) が必要で、その場合 \(u=1+\varepsilon/x\) は正則でない。よって **groupification 後でも**単元と chart generator \(x\) では生成されない。base log を、例えば \(\mathbf N\ni q\mapsto0\) として加えても、この追加の divisor 成分は消えない。

さらに \(E_x=x\partial_x\) がこの full divisorial log の relative derivation なら、ある正則な \(b=\lambda(m)\) に対して

\[
(x+\varepsilon)b=E_x(x+\varepsilon)=x
\]

でなければならない。商 \(A[x]/(x+\varepsilon)\cong A\) では右辺は \(-\varepsilon\ne0\) となり不可能。原点の局所環でも同じである。標数2でもこの矛盾は消えない。

したがって full divisorial の問題は「Lemma U の証明を一行足せば済む」ことではない。記載の \(\theta(\delta)\) の値域そのものが変わる。chart-defined への修正は C の既存の計算対象を正しく指定するものであり、full divisorial との同一性を主張する修正ではない。

## III. Property (I) audit

以下では修正後の chart-defined log structure を使う。\(t=(\partial,\lambda)\)、\(\widetilde t=\theta(1\otimes t)=(\widetilde\partial,\widetilde\lambda)\) と書き、conductor \(D\) と derivation の記号を区別する。

### Underlying derivation：VALID

E の280–283、298–304行、C の511–539行は、既に

\[
\varphi(1\otimes df)=d(\nu^\sharp f),\qquad
\langle\varphi(\omega),\theta(v)\rangle=\langle\omega,v\rangle
\]

を与えている。その双対の等式が

\[
\widetilde\partial(\nu^\sharp f)=\nu^\sharp(\partial f)
\]

である。chart での \(x,y\) の確認だけで終わっているのではなく、étale chart の通常の微分が \(dx,dy\) で生成されることにより全局所関数を扱っている。smooth / marking では \(\nu\) は既存の同一視である。ここで reducedness や dense-open equality は使わない。

### Groupified log structure の写像：VALID、記述追加が必要

使用するのは étale site 上の abelian group sheaves の射

\[
\nu^\flat_{\mathrm{gp}}:\nu^{-1}M_X^{\mathrm{gp}}
\longrightarrow M_{\widetilde X}^{\mathrm{gp}}.
\]

これは log monoid の射とも、log scheme morphism とも主張しない。特に \(q-\widetilde e_x\) に構造写像 \(\alpha\) を通常の log monoid の元のように適用してはならない。

| 元 | \(x\)-branch の像 | \(y\)-branch の像 |
|---|---|---|
| base log の元 | base pullback | base pullback |
| 単元 \(u\) | \(\nu^\sharp u\) | \(\nu^\sharp u\) |
| \(e_x\) | \(\widetilde e_x\) | \(q-\widetilde e_y\) |
| \(e_y\) | \(q-\widetilde e_x\) | \(\widetilde e_y\) |

relation \(e_x+e_y=q\) は両枝で保存される。logification で chart 元が単元になる箇所でも、単元の像を \(\nu^\sharp\) とする関係と整合する。

**単元変更。** 共通の base chart 上で \(e_x'=e_x+[u]\)、\(e_y'=e_y+[v]\)、\(q'=q+[uv]\) という変更を考える。\(x\)-branch の Cartier generator は

\[
\widetilde e_x'=\widetilde e_x+[\nu^\sharp u]
\]

に変わり、

\[
q'-\widetilde e_x'
=q-\widetilde e_x+[\nu^\sharp v].
\]

従って source の \(e_y'\) の変換と一致する。\(q'=q\) の場合はもちろん含まれる。この確認は groupification の関係を使うもので、関数 \(xy=0\) を消去して \(uv=1\) と推論するものではない。

**Strict étale chart の重なり。** 共通の étale refinement で base chart を照合し、枝を選ぶ。生き残る branch generator は同じ conductor Cartier divisor の局所方程式を与えるので単元変更で対応する。もう一方の generator は source の relation で決まる。base chart の refinement には base pullback を用いる。この確認は両稿の標準 log curve chart の範囲のものであり、任意の unrelated log chart にまで拡張してはいない。smooth locus との重なりでは conductor generator が単元となり、base log と単元の自然な写像に一致する。marking chart では元の marking の同一視になる。

**Non-split nodes。** 枝の交換は上表の二列と \(e_x,e_y\) を交換するので両立する。split étale cover 上の式が一致して降下し、大域的な branch label を必要としない。\(\nu\) を fpqc cover として使ってはいない。

**標数2。** groupified log structure は整数係数の群であり、そこでは \(q-\widetilde e_x\) を \(q+\widetilde e_x\) に置き換えない。負号が正号と同じになるのは、log component の値域 \(\mathcal O_{\widetilde X}\) が標数2である段階である。この区別を保てば問題はない。

### Log component：VALID

node chart の任意の切断を \(t=a\delta\) とする。\(a_x=\nu_x^\sharp a\) と書くと、\(x\)-branch では

\[
\widetilde\lambda(\widetilde e_x)=a_x,
\qquad\widetilde\lambda(q-\widetilde e_x)=-a_x.
\]

source の値 \(\lambda(e_x)=a\)、\(\lambda(e_y)=-a\) と一致する。base の元では relative 条件により両辺とも零。単元では

\[
\widetilde\lambda(\nu^\sharp u)
=\frac{\widetilde\partial(\nu^\sharp u)}{\nu^\sharp u}
=\nu^\sharp\!\left(\frac{\partial u}{u}\right).
\]

source の groupified log structure はこれらの元で étale 局所的に生成されるので、

\[
\boxed{\widetilde\lambda(\nu^\flat_{\mathrm{gp}}m)
=\nu^\sharp\lambda(m)}
\]

は全ての局所切断 \(m\in M_X^{\mathrm{gp}}\) で成立する。\(y\)-branch は同じ表で確認できる。smooth / marking も同一視の下で成立する。

**両稿への適用。** E はこの定義を既に採用している。C は pointed log の修正後に同じ確認が使える。full divisorial 側へ chart log からの群写像を合成できることだけでは、そこでの \(\theta\) や Property (I) の存在は保証されない。

## IV. Lemma U audit

**Chart-defined の範囲で VALID。** 必要なのは branch chart の商表示、標準 marking log の生成性、そして relative 条件である。

**Underlying derivation の一意性。** strict étale node chart \(U=\operatorname{Spec}C\to\operatorname{Spec}A[x,y]/(xy)\) では、枝はそれぞれ

\[
C/(y)C,\qquad C/(x)C
\]

である。各枝への ring map は全射であり、同じ source derivation に related な二つの derivation の値は全局所関数で一致する。smooth / marking では underlying map は同型である。

ここで **\(R\to A[x]\times A[y]\) 全体が全射だとは言っていない**。各枝での商写像を使い、結果の一意性を étale 局所から降下する。

**Log component の一意性。** \(x\)-branch の chart-defined \(M_{\widetilde X}^{\mathrm{gp}}\) は局所的に

\[
\mathcal O_{\widetilde X}^{\times},\qquad
\widetilde f^{-1}M_B^{\mathrm{gp}},\qquad \widetilde e_x
\]

で生成される。最後の元は \(\nu^\flat_{\mathrm{gp}}(e_x)\) であり、base も像に含まれる。単元の log component は既に決まった underlying derivation によって決まる。従って二つの log component は一致する。marking では marking generator、smooth chart では base と単元だけで同じ結論になる。

O の「これらは全て像に入る」は、局所生成性として扱えば十分である。大域単元の pullback 全射性を主張する必要はなく、上の形で書けばその余計な主張を避けられる。

logification と groupification のこの生成性は nilpotent を除いて得たものではない。\(A\) が nonreduced でもそのまま成立する。non-split node も split étale cover 上で確認できる。normality、reducedness、位相的または scheme-theoretic な dense-open equality は **Lemma U には不要**。

一方、E の既存の \(\varphi\) の貼り合わせには313–317行で schematic density が明示的に使われている。これは conductor 方程式の非零因子性による正当な使用であり、Lemma U に隠れて入っているのではない。C の529–537行も直接の非零因子による消去を明記している。この既存部分を再証明する必要はない。

**Full divisorial の場合。** II の \(x+\varepsilon\) により上記の生成性は失敗する。したがって O の生成性による Lemma U の証明をそのまま移すことはできない。ただし、生成性の失敗だけから uniqueness 命題自体が偽だとは言わない。本件ではそれより前に Euler lift の存在が失敗している。

## V. Restricted comparison audit

**Property (I) と Lemma U を上記の意味に固定すれば、O の論理経路は完結している。** \(\delta^{[p]}=\delta\) という生成元の確認だけから任意の \(a\delta\) の主張へ飛躍しているのではない。

使用する規約は、F の式(9.1)、1536–1542行と同じ

\[
t^{[p]}=
\left(\partial^p,\;m\longmapsto
\partial^{p-1}\lambda(m)+\lambda(m)^p\right).
\]

ここで \(\lambda(m)^p\) は値の \(p\) 乗であって、\(\lambda\) の \(p\) 回合成ではない。groupification の全体に加法的に定義される。

relative 条件は二つある：\(\partial\) が base functions 上で零であり、\(\lambda\) が base log 上で零であること。上式は両方を保持する。標数 \(p\) の通常の derivation の \(p\) 回合成は derivation であり、log compatibility の確認に使う微分作用素恒等式も reducedness を要しない。特に構造写像の値が零因子であっても、それを割ったり消去したりせず compatibility を確認できる。これは F の規約を参照しているのであって、F の fixed-curve 比較定理を family の証明として流用していない。

related 性の保存に必要な等式は、既に確認した underlying related 性の反復から得られる

\[
\widetilde\partial^{\,r}(\nu^\sharp a)
=\nu^\sharp(\partial^r a)
\]

と ring map による \(p\) 乗の保存である。従って

\[
\begin{aligned}
\widetilde\lambda_{[p]}(\nu^\flat_{\mathrm{gp}}m)
&=\widetilde\partial^{\,p-1}(\nu^\sharp\lambda(m))
 +(\nu^\sharp\lambda(m))^p\\
&=\nu^\sharp\bigl(\partial^{p-1}\lambda(m)+\lambda(m)^p\bigr).
\end{aligned}
\]

この段階で \(\nu\) が log scheme morphism であることは使っていない。

| 依存段階 | 判定 |
|---|---|
| \(t^{[p]}\) は relative log derivation | 上記の規約で成立。任意の標数 \(p\) の base を扱える |
| \(\theta(1\otimes t)\) は \(t\) に related | III により成立 |
| related 性は \([p]\) で保たれる | 上の式で成立 |
| \(\theta(1\otimes t^{[p]})\) は \(t^{[p]}\) に related | 同じ Property (I) を適用 |
| 二つの lift は一致 | IV の Lemma U を適用 |

よって既存の証明経路は

\[
\boxed{\theta(1\otimes t^{[p]})=\theta(1\otimes t)^{[p]}}
\]

を与える。chart-defined の意味を固定した後に残る数学的 gap は、この A-R1 に限ってはない。

なお \([p]\) は一般に \(\mathcal O\)-線形でも単純な Frobenius 線形写像でもない。左辺は **source で \([p]\) を取った後に \(1\otimes-\) を施す**。単なる module pullback \(\nu^*T^{\log}_{X/B}\) に \([p]\) が自動的に備わると解釈しない。主張する切断は \(X\) 上の \(t\) であり、任意の tensor を別に定義した restricted structure で比較する主張ではない。

この監査は connection、associated torsor 上の restricted comparison、relative \(p\)-curvature、dormancy の証明を含まない。

## VI. Required textual repairs

以下は **未適用の提案**。凍結原稿への変更は行っていない。挿入用の断片はこの Markdown 内に示し、独立の LaTeX 文書としては作成・コンパイルしていない。

### Repair A：pointed log structure の明示【必須】

- ファイル：C `equisingular_log_cartan_results.tex`
- 箇所：§1、定義 `def:pointed`、150–158行。
- 修正前：『base log structure に markings の逆像と \(D\) … の divisorial log structure を加えたもの』。
- 修正後：下記の定義で置換する。
- 数学的影響：§3.1 の chart 計算が扱っている対象に定義を一致させる。EQ の追加仮定や tangent comparison の式の変更は不要。ただし full divisorial と同じ構造であるという主張はしない。

```latex
\begin{definition}[Pointed log structure on \(\tX\)]\label{def:pointed}
\(\nu:\tX\to X\) と \(D=\nu^{-1}(\Sigma)\) が与えられたとする。
\(Z=D+\nu^{-1}\mathcal M\) と置く。ただし \(\mathcal M\) は元の
marking divisor である。\(\tX^\dagger\) には、base log structure に
\(Z\) の chart-defined marking log structure を加えたものを入れる。
具体的には、局所方程式 \(z\) を選び、base chart \(P\) に対して
\[
  P\oplus\mathbf N\longrightarrow\mathcal O_{\tX},
  \qquad (a,n)\longmapsto\alpha_B(a)z^n
\]
の associated log structure を用いる。\(Z\) の外では base log
structure の strict pullback を用いる。\(z'=uz\) による変更は
marking generator を \(\widetilde e_z+[u]\) に送る同型で貼り合わせる。
ここで補集合 \(j:\tX\setminus Z\hookrightarrow\tX\) から作る
full divisorial log structure
\(\mathcal O_{\tX}\cap j_*\mathcal O_{\tX\setminus Z}^{\times}\)
は用いない。nonreduced base 上では両者は一般に異なる。
本稿の log differentials、log tangent および residue はすべて
この chart-defined log structure に対するものである。
これは \(X^\dagger\) の strict pullback ではなく、\(\nu\) が
log scheme morphism であることも仮定しない。
\end{definition}
```

### Repair B：E8 の strictness と branch chart への参照【推奨】

- ファイル：C。
- 箇所：§1、118–131行、特に「標準 chart で記述される」；§3.1、497–499行。
- 修正前：「étale 局所的に次の標準 chart で記述される」「\(x=0,y=0\) を marking とする log 構造」。
- 修正後：E8 の冒頭に下記を挿入し、branch の括弧書きを「定義 `def:pointed` の chart-defined marking log structure」とする。
- 数学的影響：既に「log structure は chart から定まる」と書かれている意味を明示するもの。任意の log smooth curve を含むように範囲を広げない。

```latex
ここで base の étale 近傍には pullback log structure を入れ、
各標準 model への étale 射は、その model の chart log structure
に関して strict とする。
```

### Repair C：groupification、Property (I)、Lemma U、A-R1 の収録【必須】

- ファイル：C。
- 箇所：§3.1 の `lem:phi-glue` の後、540行の後（現在は542行から gauge vanishing）。
- 修正前：この位置には groupified map / Property (I) / Lemma U / A-R1 の記述がない。
- 修正後：以下を追加する。旧監査の論理を明文化する断片であり、新しい後続定理を付け加えるものではない。
- 数学的影響：既存の \(\theta\) に対する A-R1 を明示する。groupified map を通常の log morphism と取り違えない。MT2 の statement は変更しない。

```latex
\begin{remark}[Groupified log comparison]\label{rem:groupified-comparison}
定義~\ref{def:pointed} の log structure を用いる。
base log の元と単元を自然に写し、node の \(x\)-枝では
\[
 \nu^\flat_{\mathrm{gp}}(e_x)=\widetilde e_x,
 \qquad
 \nu^\flat_{\mathrm{gp}}(e_y)=q-\widetilde e_x
\]
とする。\(y\)-枝では対称的に定める。これは
\(\nu^{-1}M_X^{\mathrm{gp}}\to M_{\tX}^{\mathrm{gp}}\) の射であり、
log monoid の射とは主張しない。
関係 \(e_x+e_y=q\) は保たれる。単元変更
\(e_x'=e_x+[u]\)、\(e_y'=e_y+[v]\)、\(q'=q+[uv]\) に対し
\[
 q'-\widetilde e_x'
 =q-\widetilde e_x+[\nu^\sharp v],
 \qquad \widetilde e_x'=\widetilde e_x+[\nu^\sharp u]
\]
なので整合する。共通の strict étale refinement では、
生き残る generator は同じ conductor Cartier divisor の方程式として
単元倍で対応し、他方はこの関係で決まる。base chart の refinement
および枝交換とも両立するので、これらの写像は貼り合う。
smooth locus と元の marking では自然な同一視である。
\end{remark}

\begin{lemma}[Related lifts]\label{lem:related-lifts}
\(t=(\partial,\lambda)\in T^{\log}_{X/B}\) とする。
\(\widetilde t=\theta(1\otimes t)
  =(\widetilde\partial,\widetilde\lambda)\) は
\[
 \widetilde\partial\circ\nu^\sharp=\nu^\sharp\circ\partial,
 \qquad
 \widetilde\lambda\circ\nu^\flat_{\mathrm{gp}}
       =\nu^\sharp\circ\lambda
\]
を満たす。この二条件を満たす relative log derivation は高々一つである。
\end{lemma}

\begin{proof}
第一の等式は補題~\ref{lem:phi-glue} の \(d\)-compatibility の双対である。
第二は node chart の \(e_x,e_y\)、base log の元、単元で確認する。
\(t=a\delta\) に対し \(x\)-枝の値は
\(\nu^\sharp a,-\nu^\sharp a\)、base 上では零、単元 \(u\) 上では
\(\partial(u)/u\) の pullback である。\(y\)-枝も同様である。
これらは source の groupification の局所生成元なので十分である。
smooth chart と marking chart では同一視から従う。

一意性について、strict étale node chart の環を \(C\) とすると
各枝の環は \(C/(y)C\)、\(C/(x)C\) である。各商写像の全射性により
related lift の underlying derivation は一意である。
target の groupified log structure は étale 局所的に単元、base log、
生き残る marking generator で生成される。単元上の log component は
underlying derivation で決まり、残りは related 条件と relative 条件で
決まる。よって log component も一意である。
この議論は reducedness、normality、dense-open equality を使わない。
\end{proof}

\begin{lemma}[A-R1: relative restricted comparison]\label{lem:AR1}
Relative log derivations の restricted operation を
\[
 (\partial,\lambda)^{[p]}
  =\left(\partial^p,
       m\longmapsto\partial^{p-1}(\lambda(m))+\lambda(m)^p\right)
\]
とする。任意の局所切断 \(t\in T^{\log}_{X/B}\) に対して
\[
 \theta(1\otimes t^{[p]})=\theta(1\otimes t)^{[p]}.
\]
左辺は source で restricted power を取った後の pullback を意味する。
単なる module pullback に restricted structure を自動的に入れる
という意味ではない。
\end{lemma}

\begin{proof}
上の式は標数 \(p\) の任意の base 上で relative log derivation を与える。
実際、\(\partial^p\) は base 上零の derivation であり、第二成分は
additive で base log 上零である。log compatibility は
\(\partial(\alpha(m))=\alpha(m)\lambda(m)\) と標数 \(p\) の恒等式
\[
 (\partial+M_b)^p
   =\partial^p+M_{\partial^{p-1}(b)+b^p}
\]
から従う。ここで \(M_b\) は \(b\) による乗法であり、
\(\alpha(m)\) を割る操作は不要である。
補題~\ref{lem:related-lifts} の第一の等式を反復すると
\(\widetilde\partial^{\,r}\nu^\sharp
   =\nu^\sharp\partial^r\) である。
これと \(\nu^\sharp(a^p)=(\nu^\sharp a)^p\) により、
二つの related 条件は上の restricted operation で保たれる。
従って \(\theta(1\otimes t^{[p]})\) と
\(\theta(1\otimes t)^{[p]}\) はともに \(t^{[p]}\) に related であり、
同補題の一意性によって一致する。
\end{proof}
```

### Repair D：状態記述の同期【A-R1収録後に必須】

| ファイル・箇所 | 修正前 | 推奨記述 | 影響 |
|---|---|---|---|
| C、§7、1066–1070行 | relative restricted Lie algebroid と Frobenius の domain を固定すれば…という包括的な OPEN 記述 | 「Tangent に対する relative restricted comparison は補題 `lem:AR1`。connection / associated torsor compatibility、relative \(p\)-curvature comparison、relative dormancy は未証明」と切り分ける | A-R1 だけを既存の証明に基づいて明示し、後続結果を昇格させない |
| C、§7、1079–1086行の表 | A-R1 の独立行なし | 修正検証後に `A-R1 tangent restricted comparison` の行を追加する | 実装前に FROZEN と記さない |
| E、§10 D1、807–811行；§12、859–864行 | 「次に証明すべき lemma」 | 凍結旧版を保存する運用なら本文は変更せず、外部の監査・凍結ログから C の A-R1 を参照する | 旧版をそのまま保存してもよい。両ファイルを現行稿として更新する場合のみ、別途同じ状態訂正が必要 |

推奨する C の outlook の差し替え断片：

```latex
Relative log tangent の restricted comparison は
補題~\ref{lem:AR1} で確認した。
一方、connection pullback compatibility、associated torsor 上の
restricted comparison、relative \(p\)-curvature comparison および
relative dormancy は \textbf{OPEN / CANDIDATE} のままであり、
Main Theorem~2 に含めない。[Fix] の \S9 を相対証明として数えない。
```

E の chart-defined 定義自体には修正は不要。F の本文にも変更は不要。MT2 の文献修正「repair R1」と今回の「A-R1」は別なので、追加ラベルは `lem:AR1` 等にする。

## VII. Freeze readiness

| 問い | 判定 |
|---|---|
| 1. R1 の数学的証明は完成しているか | **YES：chart-defined の意味に固定した A-R1 について。** O に記載された Property (I)、Lemma U、restricted power の経路は完結する。元の別証明ファイルの全文を認証したという意味ではない |
| 2. 定義整合性の問題は解決しているか | **監査上は修正内容を確定した。ファイル上は未解決。** C の定義はまだ変更していない |
| 3. 追加仮定は必要か | **NO。** C の EQ/E8 と明示した chart-defined log structure で足りる。full divisorial を維持する別の statement は本判定の対象外 |
| 4. TeX への追記・修正は何か | Repair A、C、D。Repair B も推奨。旧 frozen 原稿は保存し、別ログで参照可能 |
| 5. 追記後、再証明なしで FROZEN としてよいか | **YES、修正が指定どおり反映されたことを差分とコンパイルで確認した後、A-R1 に限ってよい。** 本監査時点では未適用なので FROZEN へ昇格させない |
| 6. まだ未解決の問題は何か | A-R1 の数学的 gap は chart-defined の範囲ではなし。未実施なのは TeX 反映・その検証・freeze log。後続の connection / \(p\)-curvature / dormancy は未証明のまま |

C の R4（fs log base-change の chart 存在に関する文献番号照合、880–890行）は別の保留事項として残す。今回の固定された family に対する A-R1 は、E8 の chart が既に仮定されているので、その文献番号を解決することを前提にしない。本監査は base-change や smoothing の新しい statement を追加しない。

**本監査が承認する範囲は「chart-defined の対象へ定義を揃え、記載済みの A-R1 の証明経路を収録する」ことまでである。full divisorial 版、relative dormancy 全体、未確認の元証明ファイルを既証・凍結済みとして扱わない。**
