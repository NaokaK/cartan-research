# 主定理 I の独立数学監査

監査日：2026-10-24（Asia/Tokyo）

対象：[sncl_log_cartan_mainI_proof_candidate_2026-10-24.tex](/Users/naoka/Desktop/研究/cartan-research/K3_9_18/sncl_log_cartan_mainI_proof_candidate_2026-10-24.tex)。以下の行番号は、変更していないこの原稿の行番号である。

## 判定と採用条件

**現行の主定理 I は PATCH_REQUIRED。主張を変更せずに証明を完成できる。添付の置換パッチを組み込んだ証明は、原稿に明記された共通設定のもとで VALID と判定する。** 主定理 I に必要な範囲で、解消していない数学的 BLOCKER はない。

中心的な修正は、strict henselian stalk での自明化から実際の étale 近傍での自明化へ移る論証である。原稿1073–1081行の有限表示性・一意性の説明は、正式採用する証明としては省略が大きい。一方、局所環の equalizer、henselian-pair lifting、triple cocycle による比較の構成、Atiyah comparison 自体に反例はない。引用 Tag 0H74 は用途に合っている。

| 対象 | 現行原稿の判定 | 理由・処置 |
|---|---|---|
| `lem:snc-ring-equalizer`（952–992行） | **VALID** | 三つの環表示と sheaf equalizer は成立する。右端への全射性は不要。変更しない。 |
| `lem:snc-torsor-gluing`（994–1082行） | **PATCH_REQUIRED** | compatible sections の étale 近傍への降下、flat base change、coaction の因子化、canonical restriction、一意性の論証を補う。主張は成立。 |
| `lem:snc-atiyah-comparison`（1084–1115行） | **VALID** | boundary restriction の関手性による証明は成立。パッチでは任意の大域的 torsor に適用できる形にして、共通の fiber product と微分の因子化を明記する。 |
| `thm:fixed-log-gluing`（914–947、1117–1187行） | **PATCH_REQUIRED** | torsor 補題の補強が必要。Hom equalizer と同型性の論法は成立。morphism descent の étale overlap 上の一意性を明記する。 |
| `lem:restriction`（510–593行） | **VALID** | 本稿の semistable charts のもとで、relative log derivation の制限が divisorial log tangent と同型になる。 |
| `lem:boundary-atiyah`（636–690行） | **VALID** | canonical restriction と anchor の組による fiber product 表示は成立。 |
| `def:strict-log-cartan` の局所自由性・Atiyah 列（353–400行） | **VALID** | smooth torsor の局所積表示と relative log tangent の局所自由性から従う。 |
| `thm:boundary-structure` のうち主定理 I が用いる `lambda^M_ij` と anchor 整合性 | **VALID** | 共通の relative log tangent を経由して構成できる。他の結論を主定理 I の証明には使用しない。 |

ここで VALID は、必要な主張を下記の計算と論証で検証したという判定である。主定理 II・III、変形複体、p-curvature、その他の独立した主張の正当性は判定していない。

## 1. 使用する仮定と監査範囲

原稿287–326行の設定を文字どおり使う。

- `X` は代数閉体 `k` 上の projective SNC 曲面。成分数は有限、成分は smooth、double curves は smooth、triple intersections は reduced な零次元 scheme である。
- 固定された `M` は、étale 局所的に一つの active な基底生成元を持つ semistable chart で表される。double は `xy=0`、triple は `xyz=0`。残りの `Q=N^m` の生成元は基底からの pullback である。
- `H⊂G` は smooth affine algebraic groups の閉部分群。algebraic group の有限型性により、必要な coordinate algebra は有限表示である。
- principal torsor は通常の fppf torsor と解する。smooth 群の torsor は étale 局所自明であり、これと同値な étale torsor として読んでも結論は変わらない。
- Cartan map に flatness、bracket compatibility、p-curvature の条件は課さない。

原稿の「semistable-type」を任意の fs log smooth morphism まで拡張して解釈することはしない。複数 active 方向、Kummer 的な重複度、horizontal log boundary の追加などは現在の仮定の外である。パッチは新しい制限を追加するものではなく、既に明記された chart 仮定の範囲で証明を完結させる。

最初に上記設定・主定理 I・直接の補題を読み、boundary comparison の定義に必要な箇所だけを追加参照した。他の原稿の結論や、原稿内の「成立する」という宣言を根拠にはしていない。

## 2. 局所環 equalizer の検証

任意の環 `S` とイデアル `I,J` について、写像

\[
S\longrightarrow S/I\times_{S/(I+J)}S/J
\]

の核は `I∩J`、像は全体である。実際、`a mod I` と `b mod J` が一致するなら `a-b=i+j` と書け、`a-i=b+j` が共通の持ち上げである。この証明は標数に依存しない。

SNC パラメータでは

\[
(x)\cap(y)=(xy),\qquad (xy)\cap(z)=(xyz),\qquad
(x,z)\cap(y,z)=(xy,z).
\]

例えば `xy a∈(z)` なら、`S/(z)` 上で `xy` が非零因子なので `a∈(z)` である。最後の等式は `S/(z)` で最初の等式を適用する。したがって原稿の三つの表示は正しい。これは SNC 座標の正則性を使うのであり、任意の三つの元に対する恒等式ではない。

triple chart では、最初の二成分を貼った環と第三成分の交わりは **`S/(xy,z)`** である。`S/(x,y,z)` だけを使って貼ることはできない。原稿はここを正しく区別している。

三成分の値が各 double intersection 上で一致すれば、最初の二成分の値を `S/(xy)` 上に貼る。その値と第三成分の値は、`S/(xy,z)` の二つの枝上で一致するので、この交わり全体で一致する。最後に第二の fiber product 表示を適用すればよい。

この計算は étale chart 上で行え、faithfully flat な étale 局所検査により

\[
0\to\mathcal O_X\to\bigoplus_i(j_i)_*\mathcal O_{X_i}
\to\bigoplus_{i<j}(j_{ij})_*\mathcal O_{D_{ij}}
\]

の左と中央での exactness を得る。smooth locus では一成分だけなので自明である。triple point では pairwise differences にもう一つの関係があるため、右端への全射性を主張してはならない。現行補題は全射性を主張しておらず、問題はない。

## 3. strict henselian 自明化と lifting

### 3.1 自明化で使う事実

`T=O^sh_{X,x̄}` とし、その component quotient を `T_i` とする。`T_i` は同じ separably closed な剰余体を持つ henselian local ring である。`E_i→Spec T_i` は、通常の fppf descent により affine、smooth、surjective、finite presentation である。これは closed gluing の定理を先取りしていない。

closed fiber は非空 smooth scheme なので剰余体上の有理点を持つ。ここで「separably closed な体上の任意の非空 scheme が有理点を持つ」としてはならない。**smoothness が必要**である。[Stacks Project, Lemma 33.25.6, Tag 056U](https://stacks.math.columbia.edu/tag/056U) は必要な有限分離剰余体の点の存在を保証する。

この点を smooth affine coordinate algebra への環準同型として持ち上げると section が得られ、torsor は自明化する。

### 3.2 引用の適合性

[Stacks Project, Lemma 15.13.3, Tag 0H74](https://stacks.math.columbia.edu/tag/0H74) を実際に確認した。同補題は、smooth `R`-algebra `S` と henselian pair `(A,I)` に対し、`S→A/I` の `R`-algebra map を `S→A` へ持ち上げるものである。

比較写像の lifting では `R=k, S=k[H]` とする。原稿が必要とするのは

\[
H(B)\twoheadrightarrow H(B/J).
\]

`B` は component の henselian local ring、`J` は double chart では一つの boundary parameter、triple の第三成分では `(xy)` である。`J` は一般に nilpotent ではないが、同補題には nilpotence の仮定はない。

`B` が henselian local、`J⊂m_B` なら `(B,J)` は henselian pair である。この点は [Stacks Project, Lemma 15.11.9, Tag 0DYD](https://stacks.math.columbia.edu/tag/0DYD) を `J⊂m_B` に適用すれば確認できる。したがって原稿1031–1039行および1061–1063行の lifting は適法である。

Tag 0H74 単独で、closed gluing、equalizer algebra の有限表示性、nonflat base change まで証明されたことにはならない。引用の射程はこの lifting に限る。

### 3.3 非可換群での triple comparison

right torsor の trivialization を `τ_i:H→E_i` とし

\[
g_{ij}\tau_i=\tau_j L_{h_{ij}}
\]

と書く。`L_h` は left multiplication である。この規約では composition は `h_jk h_ij` の順になる。

まず `h_12` を第二成分へ持ち上げて trivialization を変更し、`h_12=1` とする。cocycle と inverse relation は

\[
h_{13}=h_{23}h_{12}=h_{23}
\quad\text{on }T/(x,y,z)
\]

を与える。affineness により `H(-)=Hom_{k-alg}(k[H],-)` は環の fiber product を保つので、`h_13,h_23` は

\[
h\in H\bigl(T/(xy,z)\bigr)
\]

へ貼り合わさる。これを `H(T/(z))` へ持ち上げて第三の trivialization を変更すれば、全比較が恒等になる。可換性や connectedness は使っていない。

曲面の SNC triple intersection は reduced な零次元 scheme である。したがって「全三重点での cocycle」は必要な scheme 上の等式を保証する。三重点の infinitesimal neighbourhood で追加の cocycle を要求する必要はない。この説明は非 reduced intersection にそのまま一般化できない。

## 4. equalizer algebra と大域的 algebraic gluing

### 4.1 quasi-coherence と action

成分数は有限である。closed immersion による pushforward は quasi-coherent sheaf を保ち、その間の線形写像の kernel も quasi-coherent である。compatible tuples は積と単位元で閉じるので、原稿の `A` は quasi-coherent algebra になる。difference map 自体が algebra homomorphism である必要はない。

coaction の像が `A⊗_k k[H]` に入るには、kernel と tensor の交換を一度使う必要がある。体 `k` 上で `k[H]` は flat なので交換できる。coassociativity と counit は component algebra への単射で検査できる。これで `Spec_X A` 上の action が構成される。

### 4.2 現行証明で補う箇所

原稿1073–1079行は、すべての strict henselian local rings 上で自明であることから、finite presentation の faithfully flat descent に言及して torsor と結論している。しかし **各 stalk からその近傍への有限表示性の移行を、単に faithfully flat descent と呼ぶだけでは論証が閉じない**。各局所環での有限表示性と、ある近傍上の有限表示性とは区別が必要である。

この区別の一般的な反例は、`A=k[t]`、`M=⊕_{a∈k} A/(t-a)` と square-zero algebra `B=A⊕M` で与えられる。各 closed point では `B_(t-a)≅A_(t-a)[e]/(e²,(t-a)e)`、generic point では `B_(0)=k(t)` なので、各 stalk は有限表示である。しかし任意の非空開集合に無限個の summands が残り、`M²=0` なので有限個の algebra generators で生成できない。従って `B` はどの非空開集合上でも有限型でない。これは一般の stalkwise finiteness 推論への反例であって、smooth torsor の主張への反例ではない。本件では以下の compatible sections の降下で不足を補える。

補強は次のように行える。

1. 上の strict henselian 計算から、境界で一致する component sections `s_i` を得る。
2. `Spec T` を pointed affine étale neighbourhoods `U_α` の inverse limit と書く。component の base change も同じ系の limit である。
3. 既知の `E_i→X_i` が finite presentation なので、有限個の `s_i` は共通の段階へ降りる。
4. 有限個の等式 `g_ij(s_i)=s_j` も、段階を進めればすべて成立する。
5. 得られた実際の étale neighbourhood `U` 上で、equalizer を計算して `A|_U≅O_U⊗_k k[H]` とする。

第3・4段階で使う limit property と等式の降下は [Stacks Project, Proposition 32.6.1, Tag 01ZC](https://stacks.math.columbia.edu/tag/01ZC)、affine な環表示では [Lemma 10.127.3, Tag 00QO](https://stacks.math.columbia.edu/tag/00QO) が保証する。**finite presentation を適用する対象は既知の component torsors であり、構成中の `Spec_X A` ではない。** この順序により循環を避ける。

第5段階では `U→X` が flat なので、定義した kernel は base change と可換である。恒等比較となった component algebras の equalizer は、環 equalizer と `k[H]` の tensor から計算できる。

従って `E|_U≅U×H` が **scheme と action の同型として**得られる。このような `U` が `X` を étale に覆うので、`E→X` の faithful flatness、local finite presentation、torsor identity が従う。affine morphism は quasi-compact かつ quasi-separated なので finite presentation でもある。`E` は最初から relative Spec として構成済みであり、analytic gluing、formal gluing、algebraic space の algebraization に移る手続きは必要ない。

### 4.3 component restriction は nonflat

自然な map

\[
\mathcal A\otimes_{\mathcal O_X}\mathcal O_{X_i}\longrightarrow\mathcal A_i
\]

を、上の `U×_X X_i` 上で検査すると trivial torsor の coordinate algebra の同型である。よって faithful flatness から大域的に同型になる。

これは nonflat tensor が任意の kernel を保つという議論ではない。例えば

\[
R=k[x,y]/(xy),\qquad R'=R/(x-y)=k[t]/(t^2)
\]

に base change すると、二つの成分も交わりも `k` になる。base change 後の diagram の equalizer は `k` であり、`R'` ではない。`R'→k` の核に非零の `t` が残る。したがって「任意の base change と SNC equalizer が可換」という主張は偽である。パッチはこの誤った一般化を使わない。

### 4.4 一意性

原稿1080–1081行の「equalizer が canonical だから一意」は、他の realization も同じ equalizer を回復することを補えば完結する。

他の torsor `E'` の coordinate algebra `B` は `O_X` 上 flat である。構造層の equalizer に `B` を tensor すると、`B` はその component algebras の equalizer になる。指定された component identifications によってこれは `A` の定義と同じである。

従って `B≅A` は、algebra と coaction に両立する canonical な同型である。component 上で恒等な automorphism も equalizer の単射によって恒等になる。結論は「同型を除いて一意」より強く、**指定された同定を保つ一意な同型を除いて一意**である。

## 5. relative log tangent と component restriction

### 5.1 double chart

`R=S/(xy)` で smooth 座標を `z` とする。relative log differentials の relation は

\[
d\log x+d\log y=0.
\]

log tangent は `x∂_x−y∂_y, ∂_z` を基底に持ち、`X_i=(x=0)` 上では `−y∂_y,∂_z` となる。これは `T_{X_i}(-log D_i)` の基底である。

### 5.2 triple chart

log tangent を

\[
\{(a,b,c)\in R^3:a+b+c=0\}
\]

と表示する。`X_i=(x=0)` への restriction は `(a,b,c)↦b y∂_y+c z∂_z` である。`a=−b−c` によって逆写像が与えられる。この行列は整数係数の可逆な変換であり、標数2・3でも退化しない。

これらは underlying derivation が component ideal を保つことによる canonical map である。unit を含む表示でも、同じ map を別の chart で書いているため貼り合わさる。局所同型の双対から differentials の同型を得る。

重要なのは、`M|_{X_i}` という pullback log structure と divisorial log structure を同一視していないことである。同一視しているのは **基底方向を除いた relative log tangent/differentials の bundle** である。原稿はこの区別を明記しており正しい。

`Q=N^m` の残りの生成元は、relative log differential では `dlog q=0` となる。したがって局所 rank は2のままであり、余分な基底方向は出現しない。smooth locus では active な一成分方向も基底 relation によって消え、通常の tangent bundle を得る。

torsor を局所自明化すると Atiyah bundle は `ad(E_H)⊕T_log` の表示を持つ。restriction は前者を通常の associated bundle restriction、後者を上記同型に送る。gauge の微分も derivation restriction と両立するので、この同型は貼り合わさる。Atiyah 列の商が locally free であるため、component tensor で exactness を壊す Tor は発生しない。

## 6. boundary Atiyah bundle と normal derivative

`D=D_ij`、`A_i=T_{X_i}(-log D_i)|_D`、`Q=T_D(-log P)` とする。boundary ideal の保存により、restriction `q_i:A_i→Q` が定まる。

double point では `(y∂_y,∂_z)↦(0,∂_z)`、triple point では `(y∂_y,z∂_z)↦(0,z∂_z)` である。従って kernel は `O_D ℓ_ij`。normal generator は conormal line に恒等の scalar action を与えるものとして intrinsic に定まり、局所方程式の unit 倍に依存しない。

torsor 上の vector field を `F_i=E_i|_D` に制限し、base anchor と組にすると

\[
B_i\longrightarrow\operatorname{At}(F_i)(-\log P)\times_Q A_i
\]

が得られる。局所表示は `(c,v)↦((c,q_i(v)),v)` である。両辺は同じ rank の locally free sheaf であり、この表示は同型を示す。構成が restriction と anchor のみを使うため、trivialization の選択に依存しない。

### 6.1 `lambda^M_ij` と `Q` の整合性

共通の `T_log|_D` を経由する比較について `q_j lambda^M_ij=q_i` が成立する。両辺とも同じ derivation を同じ `O_D` に制限しているためである。

triple chart で `X_i=(x=0), X_j=(y=0), D=(x=y=0)` とすると、具体的には

\[
\lambda^M_{ij}\bigl(b\,y\partial_y+c\,z\partial_z\bigr)
=(-b-c)x\partial_x+c z\partial_z.
\]

したがって基底に関する行列は

\[
\begin{pmatrix}-1&-1\\0&1\end{pmatrix}.
\]

normal generator は符号反転し、`Q` への像は `c z∂_z` のままである。**triple chart の full comparison は normal の符号反転だけではない。** 上式の第二列も保持する必要がある。原稿の「共通の relative log tangent を経由する」という定義はこの項を含むので正しい。

ここで `z∂_z` は log tangent bundle の生成元である。三重点で ordinary tangent vector として評価すると零になることと、log tangent の fiber で零であることを混同してはならない。

### 6.2 大域的 Atiyah comparison との一致

任意の大域的 torsor `E_H` について `F=E_H|_D` とすれば、canonical に

\[
\operatorname{At}_{\log}(E_H)|_D
\simeq \operatorname{At}(F)(-\log P)\times_Q T_{\log}|_D
\]

となる。局所自明化で同じ `(c,v)↦((c,q(v)),v)` を計算すれば証明できる。これを両成分の表示に移すと、第一因子には `At(g_ij)`、第二因子には `lambda^M_ij` が作用する。よって比較は正確に

\[
\Lambda^M_{ij}(a,v)=(\operatorname{At}(g_{ij})a,\lambda^M_{ij}v)
\]

である。この論証は closed gluing に依存しないため、パッチでは補題の適用対象を「構成された torsor」から「任意の大域的 torsor」へ明示的に広げた。

### 6.3 normal derivative が不要な理由

component 上で `J=I_D`、log vector field を `v` とすれば `v(J)⊂J` であり

\[
v(f)\bmod J=q_i(v)(f\bmod J)
\]

である。二つの gauge extension が境界で同じなら、`k[H]` の任意の関数の pullback の差は `J` に入る。その差を `v` で微分しても `J` に入り、境界で消える。したがって extension の選択による微分の曖昧さは存在しない。

normal logarithmic generator は `q_i` の kernel に入るので、この gauge derivative に寄与しない。三重点でも同じ式が成立する。必要な boundary の tangent derivative は `At(g_ij)` に含まれている。「normal derivative が不要」を「微分を一切使わない」と解釈してはならない。

## 7. Hom equalizer と Cartan map

torsor が構成された後、`U=At_log(E_H)` と `V=ad(E_G)` は有限局所自由である。従って

\[
\mathscr F=\mathcal Hom(U,V)=U^\vee\otimes V
\]

は flat であり、構造層 equalizer に tensor できる。closed immersion の projection formula により原稿の `eq:cartan-hom-equalizer` を得る。また source の有限局所自由性によって `Hom` の component/boundary base change も正しい。

境界上で両側を同じ Hom bundle に表示したとき、差分の消滅は

\[
\operatorname{Ad}(g_{ij})\Theta_i=\Theta_j\Lambda^M_{ij}
\]

と同値である。厳密には表示を一方へ移すために同型またはその逆を合成するが、kernel 条件はまさにこの式である。

大域切断関手は左完全なので compatible な `θ_i` は一意な大域 section `θ` を与える。ここで右端への全射性、`H^1` の消滅、projective scheme の global sections の完全性は使っていない。

`θ iota=iota_1` は `Hom(ad(E_H),V)` の同様の equalizer の injectivity で確認できる。`θ` の同型性は各点の residue field で確認し、同 rank の locally free sheaves 間の行列の determinant が local unit であることから得る。単に「各成分で generically invertible」だけでは不十分だが、本定理は各成分で全域の同型を仮定しているため問題はない。

## 8. morphism descent・必要十分性・循環性

二つの大域的 torsor を同時に自明化する étale cover を選ぶ。affine open `U` ごとに component morphisms は `H`-valued maps であり、境界での compatibility により環 equalizer に値を取る。affineness によって一意な `H(U)` の元へ貼り合わさる。

この local morphism が異なる trivializations の overlap 上で一致することは、さらに affine に細分して **同じ一意性**を適用すれば分かる。通常の étale descent for morphisms によって大域的 morphism が得られる。Cartan maps との可換性は Hom equalizer の injectivity で確認する。この一段を明記することで、単なる局所 `H(R)` 計算と global morphism descent が接続される。

必要性は、任意の大域的 geometry の component restrictions から boundary identifications を得て、inverse relation、cocycle、Atiyah comparison を適用するだけである。十分性は torsor 構成の後で Hom equalizer を使う。依存関係は

\[
\text{環 equalizer + smooth lifting + finite presentation の limit property}
\Longrightarrow\text{torsor gluing}
\]

\[
\text{component restriction + boundary restriction}
\Longrightarrow\text{Atiyah comparison}
\]

\[
\text{torsor gluing + Atiyah comparison + Hom equalizer}
\Longrightarrow\text{主定理 I}
\]

であり、逆向きの依存はない。

現行の Atiyah 補題が「構成された torsor」に限って書かれていることは、torsor 補題の一意性を先に使えば必要性にも適用できるので、それ自体が致命的な循環ではない。ただしパッチの一般化された記述では、この余分な迂回も不要になる。

「大域的 `g_ij` が存在する」が必要十分条件である。各 double curve の開被覆上だけでの同型の存在から、大域的同型の存在を結論していない。固定された `g_ij` への一意性を、異なる descent data 全体での無条件な一意性に拡張してもいない。

## 9. 仮定の十分性と反例による境界確認

smooth affine algebraic group という仮定で、この証明には十分である。reductivity、connectedness、special group 性、centralizer の smoothness、標数の下限は不要である。`G` は associated vector bundle と定義された Cartan map のために使われ、torsor の closed gluing 自体は `H` の性質だけで進む。

標数2でも normal の `−1` は unit であり、上記比較行列の determinant は unit である。証明中に `1/2`、`1/3`、`1/p` は現れない。正標数での非完全な separably closed residue fields に対しても、smooth closed fiber の有理点の議論を使っているので問題はない。

smoothness を取り除いたときの同じ証明手順の失敗は具体的に見える。`char k=p`、`B=k[[t]]`、`H=mu_p` とする。`B` は strictly henselian だが、

\[
\mu_p(B)=\{1\},\qquad 1+t\in\mu_p(B/(t^p))
\]

であり、この元は持ち上がらない。また `s^p=1+t` は `B` 上の非自明な `mu_p`-torsor を与える。これは nonsmooth 群に同じ strict henselian 自明化を適用できない例であり、現在の smooth 群に関する主張への反例ではない。nonsmooth 群での closed gluing 定理そのものの一般的成否は、本監査では主張しない。

任意の nonflat base change に関する誤った一般化への反例は4.3節に示した。現在の SNC・smooth affine・固定 `M` の仮定をすべて満たす主定理 I の反例はなく、上記の構成が成立を証明する。

## 10. 成果物と原稿への反映

- [mainI_independent_patch.tex](/Users/naoka/Desktop/研究/cartan-research/K3_9_18/mainI_independent_patch.tex)：置換用の TeX fragment。元原稿994行の torsor 補題の開始から1197行の `rem:gluing-proof-status` の終わりまでを置換する。単独コンパイル用文書ではない。
- [mainI_independent_patch.diff](/Users/naoka/Desktop/研究/cartan-research/K3_9_18/mainI_independent_patch.diff)：同じ変更の unified diff。既存の候補版コメントも更新する。原稿のコピーへ適用するためのものであり、元ファイルには適用していない。

元の主定理 I の statement、ring equalizer 補題、restriction 補題、boundary Atiyah 補題は変更不要である。TeX fragment は torsor の証明の補強、Atiyah comparison の一般的な記述、主定理 I の証明の明文化、status remark の置換だけを含む。主定理 II・III およびその節には変更を加えない。

「要独立監査」という注意書きは、パッチ適用後に限り、パッチ末尾の `rem:gluing-proof-status` へ置換できる。その文章は証明に使う結果と nonflat base change の扱いを述べ、未解決の証明候補としては扱わない。一方、「論文全体の監査済み」や「主定理 II・III も検証済み」という文言には置き換えない。

**パッチ後、主定理 I について未解決の数学的課題は残らないと判断する。** 原稿統合時にはこの置換とラベル・組版の確認が必要である。ここでの数学的判定は、証明の依存関係、明示した局所計算、descent の各段階の確認による。コンパイル成功や数値実験を根拠としていない。

元原稿の SHA-256：`38df49574619a45033246c71e253c27542e2c7e4232371fe6bc9bdeccaed6c2f`。成果物作成後もこの値が変わっていないことを確認した。unified diff は一時コピーへの適用結果を照合し、全ラベルの保持、置換部分の環境の対応、および status remark より後の全文（主定理 II・III を含む）が不変であることも確認した。これらはファイル整合性の検査であり、数学的証明の代替ではない。
