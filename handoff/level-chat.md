# 引き継ぎ文書：正標数 log parabolic geometry における有限レベル現象

最終更新：2026-09-03 / ドラフト ver.0.4 相当
関連ファイル：`log-level-opers.tex`（論文ドラフト）、`check.py`（†C_N 列挙）、`verify_p5.py`（p=5 の ODE 検証）

**信頼度タグ**：本文書では以下を厳密に区別する。
- **[定理]** … 完全な証明があるもの（本研究で証明、または文献に証明がある）
- **[文献]** … 文献の結果をそのまま引用しているもの（証明は追っていない）
- **[部分証明]** … 証明の骨格はあるが細部に穴があると自覚しているもの
- **[数値]** … 計算機で確認しただけで一般証明がないもの
- **[予想]** … 証拠はあるが証明がないもの
- **[要検証]** … 出典・主張の正確さ自体が未確認のもの

---

## 1. 研究目的

### 1.1 当初の目的（2026年8月時点）

$k$ を標数 $p>0$ の代数閉体、$(X,D)$ を log smooth pair とする。
Berthelot–Montagnon の有限レベル対数微分作用素環 $\mathcal{D}^{(m)}_{X^{\log}}$ に対し、

> 「有限レベル（特に $p$-曲率 $0$）では成立するが、無限レベル（stratification）では成立しない」
> という現象の明示的な反例族を構成し、分類する。

出発点の観察は、対数接ベクトル場が toral（$\theta^{[p]}=\theta$, $\theta=x\partial_x$）であることから、
$(\mathbb{P}^1,\{0,\infty\})$ 上の階数 $1$ 対数接続 $\nabla=d+a\,d\log x$ の $p$-曲率が
$a^p-a$ となり $a\in\mathbb{F}_p$ で消えるのに対し、
log Frobenius では $F^*(d\log t)=p\,d\log x=0$ なので $a\neq0$ は $F^*$ の像に入らない、というもの。

### 1.2 改訂後の目的（現在）

**当初の予想は否定された。**$\mathrm{PGL}_2$-oper については反例が存在しない（§3.3）。
現在の目的は次の通り：

> レベル上昇の障害がどこに局在するかを厳密に特定し、
> 「障害 $=$ 行列式束（より一般に $\pi_1(G)$-torsor）の $p^N$ 可除性の障害」
> という形の一般命題を定式化・証明する。

副次的な目的として、$\#{}^N\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}$ の閉じた数え上げ公式（§6.2）。

---

## 2. 現在採用している定義と規約

### 2.1 レベルの規約（最重要）

**二つの流儀があり、混同すると主張の真偽が反転する。**

| | Berthelot 流 | Wakabayashi 流（**本研究の採用規約**） |
|---|---|---|
| 作用素環 | $\mathcal{D}^{(m)}$ | 「レベル $N$」$=\mathcal{D}^{(N-1)}$ |
| 曲率 | $p^{m+1}$-曲率 $=\nabla_{\langle p^{m+1}\rangle}$ | 「$p^N$-曲率」 |
| dormant | $p^{m+1}$-曲率 $=0$ | 「dormant レベル $N$」 |

**[文献]**（Wakabayashi 2201.11266, Prop. 2.1.5, Cor. 2.1.6）
非対数的な場合、$\mathfrak{Mod}(\mathcal{D}^{(m)}_S)\simeq\mathfrak{Mod}(\mathcal{D}^{(m-l)}_{S^{(l)}})$ かつ
$p^{m+1}$-曲率と $p^{m-l+1}$-曲率が対応する。したがって

$$\text{dormant レベル }N \iff F^{(N)*}(\mathcal{O}\text{-加群})\text{ の像に入る}$$

すなわち Wakabayashi 流の「dormant レベル $N$」は「$N$ 回 Frobenius 降下できる」と一致する。

**注意**：ユーザ側の当初の規約「レベル $n$ = $\mathcal{D}^{(n)}$ に持ち上がる、レベル1 ⟺ $p$-曲率0」は
非対数の場合には Wakabayashi 流と（添字ずれを除いて）整合するが、
「$\mathcal{D}^{(1)}$-作用の存在」と「$p$-曲率の消滅」を独立の条件として扱うと混乱する。
以後は必ず Wakabayashi 流で書くこと。

### 2.2 基本対象

- $(X,D)$：log smooth pair。局所的に $D=\{x_1\cdots x_r=0\}$、$T_X(-\log D)$ の基底 $\theta_i=x_i\partial_i$, $\partial_j$。
  制限 Lie 代数構造は $\theta_i^{[p]}=\theta_i$（toral）、$\partial_j^{[p]}=0$（冪零）。
- $\mathscr{X}=(X,\{\sigma_i\}_{i=1}^r)$：$r$ 点付き曲線。$\mathscr{P}:=(\mathbb{P}^1;[0],[1],[\infty])$。
- $R$：離散付値環、$t$ 素元。$\breve{\mathcal{D}}^{(m)}_R$：Montagnon の対数版、
  $\breve\partial_{\langle j\rangle}(t^n)=q_j!\binom{n}{j}t^n$、$q_j=\lfloor j/p^m\rfloor$。

### 2.3 exponent と radius

**[文献]**（Wakabayashi 2201.11266, Prop. 3.2.1, Def. 3.3.1, Def. 4.3.2, Rem. 4.3.1）

- **exponent**：dormant $\breve{\mathcal{D}}^{(m)}_R$-加群の $t$ 進完備化は
  $\bigoplus_{i=1}^n(k[\![t]\!],\widehat\nabla_{d_i})$、$d_i\in\mathbb{Z}/p^{m+1}\mathbb{Z}$ と分解する。
  多重集合 $[d_1,\dots,d_n]$ が exponent。ここで
  $\nabla_{a,\langle j\rangle}(t^n)=q_j!\binom{n-\tilde a}{j}t^n$（$0\le\tilde a<p^{m+1}$）。
- **radius**：exponent の $\mathfrak{S}_n\backslash(\mathbb{Z}/p^N)^{\times n}/\Delta$ における類。
  $n=2$ では $a\mapsto[a,-a]$ により $(\mathbb{Z}/p^N\mathbb{Z})/\{\pm1\}$ と同一視、
  $\rho=\tfrac12(d_1-d_2)$。

### 2.4 $^\dagger C_N$（3点付き射影直線の組合せデータ）

**[文献]**（Wakabayashi 2209.08528, (10.6), Prop. 10.1.4, 10.3.3）

$[a]_{N'}:=a\bmod p^{N'}$ とする。$^\dagger C_N$ は非負整数の三つ組 $(s_1,s_2,s_3)$ で次を満たすもの全体：

- **(a)** $\sum_{i=1}^3 s_i\le p^N-2$ かつ $|s_2-s_3|\le s_1\le s_2+s_3$
- **(b)** 任意の $0<N'<N$ に対し、$s_i'\in\{[s_i]_{N'},\ p^{N'}-1-[s_i]_{N'}\}$ $(i=1,2,3)$ を
  適当に選んで $\sum_i s_i'\le p^{N'}-2$ かつ $|s_2'-s_3'|\le s_1'\le s_2'+s_3'$ とできる。

そして $\#\,{}^N\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}=\#\,{}^\dagger C_N$。

### 2.5 被覆との辞書

**[文献]**（Wakabayashi 2201.11266, Thm. C；$N=1$ は Mochizuki）
$\mathrm{Cov}^{\mathrm{tame}}_{\mathscr{P}}$：分岐点の集合が $\{[0],[1],[\infty]\}$ に一致し、
分岐指数 $\lambda_x$ がすべて奇数で $\sum\lambda_x<2p^N$ なる従順分岐被覆 $\phi:\mathbb{P}^1\to\mathbb{P}^1$ の
$\mathrm{PGL}_2(k)$-同値類。全単射 $\Upsilon_{\mathscr{P}}:\mathrm{Cov}^{\mathrm{tame}}_{\mathscr{P}}\xrightarrow{\sim}{}^N\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}$ があり、
radius は $(\tfrac12\bar\lambda_0,\tfrac12\bar\lambda_1,\tfrac12\bar\lambda_\infty)$ の像。

**[定理]（本研究、辞書補題）** $\lambda_i=2s_i+1$ と置くと (a) は
「$\lambda_i$ 奇数・厳密三角不等式 $\lambda_1<\lambda_2+\lambda_3$（巡回）・$\sum\lambda_i\le 2p^N-1$」と同値。
証明：$\sum\lambda_i=2\sum s_i+3\le2(p^N-2)+3=2p^N-1$。
$\lambda_1<\lambda_2+\lambda_3\iff 2s_1+1<2s_2+2s_3+1\iff s_1\le s_2+s_3$（整数性）。

**この辞書により、$s_i=0\leftrightarrow\lambda_i=1$（不分岐）は許される**ことが確定した。
`Cov^tame` の定義中の「分岐点の集合が $\{[0],[1],[\infty]\}$ に一致する」は
$\lambda_x\ge2$ を要求する読み方ではない。

### 2.6 実用的な言い換え（計算に使う）

**[定理]** $p$-曲率 $0$ ⟺ 対応する2階線型 ODE が $k(x)$ 内に $k(x^p)$ 上一次独立な解 $y_1=f, y_2=g$ をもつ。
このとき $\phi=f/g$ が上の被覆で、Wronskian $W=f'g-fg'$ が $\phi'=W/g^2$ を通じて分岐を支配する：
$$\mathrm{ord}_{x_0}W=\lambda_{x_0}-1,\qquad \deg W=2d-2-(\lambda_\infty-1),\qquad d=\deg\phi.$$
Riemann–Hurwitz から $\sum_x\lambda_x=2d+1$、したがって $\lambda_x\le d$ が厳密三角不等式と同値。

---

## 3. 確立した結果

### 3.1 局所理論

**[定理]（本研究）留数の強制的半単純性**
$(\mathcal{E},\nabla)$ を対数接続、$R_i=\mathrm{Res}_{D_i}(\nabla)$ とする。
$p$-曲率が消えるなら $R_i^p=R_i$。特に $R_i$ は半単純で固有値は $\mathbb{F}_p$。

証明：$\nabla_{\theta_i}(x_ie)=x_i(\nabla_{\theta_i}+1)e$ より $\nabla_{\theta_i}$ は $x_i\mathcal{E}$ を保つ。
$\mathcal{E}/x_i\mathcal{E}$ 上で $\nabla_{\theta_i}^p$ が $R_i^p$ を誘導。
$\psi(\theta_i)=\nabla_{\theta_i}^p-\nabla_{\theta_i}$ を $D_i$ に制限して $R_i^p=R_i$。
$T^p-T$ は分離多項式。∎

**[定理]（系）** $p$-曲率 $0$ かつ $R_i$ 冪単 $\Rightarrow R_i=0$。
すなわち **dormant な世界には非自明な冪零留数は存在しない**。
これは当初のタスク4「留数が半単純／冪単で挙動が分かれるはず」への答えであり、
冪単側は $p$-曲率非零の世界（Mochizuki の nilpotent indigenous bundle）に属し、本理論と交わらない。

**[文献]** この事実の oper 版は Mochizuki, *Foundations of $p$-adic Teichmüller theory*, Chap. II, Prop. 1.4, 1.5
（radius は $\mathbb{F}_p$ に属し、$\rho_i\in\mathbb{F}_p^\times/\{\pm1\}$ でなければ空）として既出。**[要検証]** 正確な主張は未確認。

**[文献]（Wakabayashi 2201.11266, Rem. 3.3.3）$p$ 進展開としてのレベル**
exponent $\tilde d_i=\sum_{l=0}^m p^l\tilde d_{il}$ と展開すると、
$l$ 段目に降下した $\breve{\mathcal{D}}^{(0)}_{R^{(l)}}$-加群のモノドロミーは対角化可能で固有値 $-\tilde d_{il}\bmod p$。

**これが「留数の $p$ 進展開が長さ $n$ で止まる」という当初の描像の正確な定式化である。**
系として、**レベル上昇は局所的には常に可能**（各分岐点で $p$ 通りの選択）。障害は純粋に大域的。

**[文献]（同 Prop. 3.3.4）** $\mathrm{Res}(\nabla)=0$ ⟺ exponent $=[0,\dots,0]$ ⟺ 非対数的理論から来る。
すなわち**非対数的理論は exponent $=0$ の部分に他ならない**。log と非 log の差はこの $p^r$ 通りの自由度に尽きる。

**[文献]（同 Prop. 3.4.1）** $m$-cyclic vector の存在 ⟺ $d_1,\dots,d_n$ が互いに相異なる。
（「oper ⟹ 留数は正則」の高次レベル版。$n=2$ では $\rho\neq0$ に対応。）

### 3.2 大域理論

**[定理]（本研究）Hecke 変形の無力性**
$\nabla_\theta(x^{-n}f)=x^{-n}(\theta f+(a-n)f)$ より、$D$ に沿った格子の取り替えは exponent を
$a\mapsto a-n$ だけずらす。特にレベル $N$ では exponent は $\mathbb{Z}/p^N$ 全体を動く。
したがって階数 $1$ では局所的に exponent を常に $0$ にできる。

**[定理]（本研究、細部に注意）階数 $1$・曲線の場合**
$X$ 固有滑らかな曲線、$D=\sum_{i=1}^r p_i$、$r\ge1$、$(\mathcal{L},\nabla)$ 階数 $1$ dormant
$\Rightarrow$ 任意のレベルに持ち上がる（stratification をもつ）。

証明：レベル $N$ ⟺ $\mathcal{L}\cong F^{(N)*}\mathcal{N}\otimes\mathcal{O}(\sum j_ip_i)$（$0\le j_i<p^N$）。
次数をとると $\sum j_i\equiv\deg\mathcal{L}\pmod{p^N}$。$r\ge1$ なので $j_1$ を自由に選べて解ける。
残りは $\mathrm{Pic}^0(X)$ の $p$ 可除性。∎
**注意**：局所分類（Wakabayashi Prop. 3.2.1）の大域化の細部は精査していない。→ **[部分証明]** 扱いが安全。

**[定理]（本研究）次数障害**
dormant レベル $N$ の $\mathrm{GL}_2$-oper $(\mathcal{F},\nabla,\mathcal{L})$ に対し
$\det\mathcal{F}\cong F^{(N)*}\mathcal{M}\otimes\mathcal{O}(\sum\tilde e_i\sigma_i)$、
$$\sum_{i=1}^r\tilde e_i\equiv\deg\det\mathcal{F}\pmod{p^N}$$
が成り立つ（$\tilde e_i\in[0,p^N)$ は exponent の代表）。
KS 同型から $2\deg\mathcal{L}=(2g-2+r)+\deg\det\mathcal{F}$。
これは**必要条件であって十分条件ではない**。

### 3.3 $^\dagger C_N$ の入れ子性と反例の非存在

**[定理]（本研究）** $^\dagger C_N\subseteq{}^\dagger C_{N+1}$。

証明：$(s_i)\in{}^\dagger C_N$ とする。(a) は $p^N-2\le p^{N+1}-2$ より $N+1$ でも成立。
(b) について、$N'=N$ では $s_i<p^N$ ゆえ $[s_i]_N=s_i$ で $s_i'=s_i$ と選べば要求は $(s_i)$ の (a)（レベル $N$）そのもの。
$N'<N$ では $(s_i)\in{}^\dagger C_N$ の (b) をそのまま使う。∎
**[数値]** $p=3,5$、$N=1,2$ で計算機確認済み。

**[部分証明]（本研究）$\mathscr{P}$ 上の全射性**
制限写像 $\mathrm{res}_N:{}^{N+1}\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}\to{}^{N}\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}$ は全射。
上の包含が切断を与える。
**穴**：「レベル降下が $^\dagger C$ の言葉で $s\mapsto s'\in\{[s]_N,p^N-1-[s]_N\}$ で与えられる」
という部分は、Wakabayashi の径数付け（Prop. 10.3.3）とレベル降下の両立性を仮定している。
これは条件 (b) の形からほぼ自明に見えるが、**原論文で確認していない**。

**[部分証明]（本研究）一般 $(g,r)$、totally degenerate**
三価 clutching data $\mathbb{G}$ に対し $\mathrm{Ed}_{p,N,\mathbb{G}}\subseteq\mathrm{Ed}_{p,N+1,\mathbb{G}}$
（各頂点に入れ子性を適用）。したがって $X_{\mathbb{G}}$ 上で制限写像は全射。
同じ穴を引き継ぐ。

**[予想]** 一般の smooth 曲線でも $\mathrm{res}_N$ は全射。
根拠：generic étaleness（Wakabayashi 2209.08528, Thm. C）と因子化性から
$\deg\Pi_{2,N,\rho,g,r}\le\deg\Pi_{2,N+1,\rho',g,r}$ が従うが、これは単調性であって全射性ではない。

### 3.4 数え上げ

**[定理]（本研究＋文献）** $\#\,{}^1\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}=\dfrac{p(p^2-1)}{24}=\dfrac{|\mathrm{PSL}_2(\mathbb{F}_p)|}{12}$。

**[数値]** $p=3,5,7,11,13$ で $^\dagger C_1$ を直接列挙して確認（`check.py`）：

| $p$ | 3 | 5 | 7 | 11 | 13 |
|---|---|---|---|---|---|
| $\#{}^\dagger C_1$ | 1 | 5 | 14 | 55 | 91 |
| $p(p^2-1)/24$ | 1 | 5 | 14 | 55 | 91 |
| $\#{}^\dagger C_2$ | 11 | 225 | 1666 | 24805 | 67431 |

$p=3$, $N=3$：$121=11^2$。

**証明の穴**：一般 $p$ での「$^\dagger C_1$ の元の個数 $=$ 四角錐数 $n(n+1)(2n+1)/6$（$n=(p-1)/2$）」
という組合せ論的同一視を書き下していない。→ **[数値]** 扱い。

**[文献]（Wakabayashi 2209.08528, (1.2)）** $(p^3-p)/24$ は
一般な種数 $2$ の曲線上の dormant $\mathrm{PGL}_2$-oper の個数（Mochizuki, Lange–Pauly, Osserman）に一致。

**[定理]（本研究、説明）** これは偶然ではない。種数 $2$ の三価グラフはテータグラフ（頂点2・辺3）で、
両頂点が同じ辺三つ組を見るので $\mathrm{Ed}_{p,N,\mathbb{G}}={}^\dagger C_N$。
すなわち $\deg(\Pi_{2,N,\emptyset,2,0})=\#{}^\dagger C_N$。

### 3.5 $p=5$ の完全リスト（機械検証済み）

**[定理]＋[数値]** $\mathscr{P}$, $p=5$：$^\dagger C_1=\{(0,0,0),(1,1,0),(1,0,1),(0,1,1),(1,1,1)\}$ の5個。

| # | $(\lambda_0,\lambda_1,\lambda_\infty)$ | $(s_i)$ | radius | $d$ | $\phi$ | ODE | $_2F_1$ |
|---|---|---|---|---|---|---|---|
| 1 | $(1,1,1)$ | $(0,0,0)$ | $(2,2,2)$ | 1 | $x$ | $y''=0$ | $(4,0;0)$ |
| 2 | $(3,1,3)$ | $(1,0,1)$ | $(1,2,1)$ | 3 | $x^3$ | $xy''-2y'=0$ | — |
| 3 | $(1,3,3)$ | $(0,1,1)$ | $(2,1,1)$ | 3 | $(x-1)^3$ | $(x-1)y''-2y'=0$ | — |
| 4 | $(3,3,1)$ | $(1,1,0)$ | $(1,1,2)$ | 3 | $x^3/(x-1)^3$ | $x(x-1)y''+(x+2)y'+y=0$ | $(2,3;3)$ |
| 5 | $(3,3,3)$ | $(1,1,1)$ | $(1,1,1)$ | 4 | $x^3(2x+1)/(x+2)$ | $x(x-1)y''+(x+2)y'+4y=0$ | $(1,4;3)$ |

実現されない radius：$(2,2,1),(2,1,2),(1,2,2)$。

`verify_p5.py` で $\mathbb{F}_5$ 上、Wronskian（#4: $2x^2(x-1)^2$、#5: $x^2(x-1)^2$、
#2: $3x^2$、#3: $3(x-1)^2$）と、各 ODE が $f,g$ を解にもつことを確認済み。
**注意**：以前の応答で「計算機で確認」と述べた時点では実際には未実行だった。現在は実行済み。

#5 の構成過程（$g=x-t$、$f=\sum a_ix^i$ の係数比較 → $(t-1)(t-3)=0$ → $t=3$）は
`log-level-opers.tex` §7.1 に省略なしで記載。

### 3.6 障害の局在

**[部分証明]（本研究）** dormant レベル $N$ の $\mathrm{GL}_n$-oper について、
その $\mathrm{PGL}_n$-類がレベル $N+1$ に持ち上がるなら、
$\mathrm{GL}_n$-oper 自身が持ち上がる必要十分条件は $(\det\mathcal{F},\det\nabla)$ が持ち上がること。

**穴**：捻り $(\mathcal{N},\nabla_\mathcal{N})$ の $n$ 乗根の一意存在に
Wakabayashi Prop. 4.1.4（$p\nmid l$ を仮定）を使っているが、
$p\mid n$ の場合の扱いと、$\det$ 以外の障害が本当にないことの議論が不完全。

**[予想]** $\pi_1(G)$ が $p$ 群を含まないとき、レベル上昇の障害は
$\mathrm{Pic}(X)/p^N$（より一般に $H^1(X,\pi_1(G))$ の $p^N$ 可除性）の障害に完全に帰着する。

---

## 4. 検討中のアイデア

### 4.1 root stack による Cartier 降下（**[予想]**）

$\mathcal{X}'_N:=\sqrt[p^N]{(X^{(N)},D^{(N)})}$、log étale 射 $\widetilde F^{(N)}:X\to\mathcal{X}'_N$ に対し
$$\widetilde F^{(N)*}:\mathrm{QCoh}(\mathcal{X}'_N)\xrightarrow{\sim}\{\text{dormant レベル }N\text{ の }\mathcal{D}^{(N-1)}_{X^{\log}}\text{-加群}\}$$
が圏同値。$\widetilde F^{(N)*}\Omega^1_{\mathcal{X}'_N}(\log)\cong\Omega^1_X(\log D)$（素朴な $F^*$ と違い零にならない）ゆえ
oper 構造が保たれる。

根拠：$p$-曲率 $0$ ⟹ $\nabla_{\theta_i}^p=\nabla_{\theta_i}$ ⟹ 固有分解 $\mathcal{E}=\bigoplus_{a\in(\mathbb{Z}/p)^r}\mathcal{E}_a$、
$x_i$ が次数 $e_i$ をもつ。すなわち $\mu_p^r$-同変層。
階数 $1$ 局所版は Wakabayashi Prop. 3.2.1 そのもの。

**懸念**：これは Lorenzon–Montagnon の indexed algebra $A^{gp}_X$、$\mathcal{B}^{(m+1)}_{X/S}$ による
定式化（Ohkawa, Rend. Padova 134 (2015)）の言い換えに過ぎない可能性が高い。→ §7

### 4.2 $\#{}^\dagger C_N$ の母関数（未着手）

条件 (b) が再帰的なので、$s_i$ の $p$ 進展開の桁ごとの transfer matrix で書けないか。
$p=3$ の $1,11,121$ という並び（$11^{N-1}$?）が示唆的。
$p=3,N=4$ を計算して $11^3=1331$ になるか確認するのが最短のテスト。

### 4.3 「$\det$ に局在」の一般 $(G,P)$ 版（未着手）

radius を $\mu_{p^N}\to T$ の $W$-共役類として定義し、
$$\text{レベル上昇の障害}\ \in\ H^1(X,\pi_1(G))\otimes\mathbb{Z}/p^N$$
という完全列を書きたい。$\mathrm{PGL}_n$ では $\pi_1=\mathbb{Z}/n$。

---

## 5. 失敗したアプローチと理由

**必ず読むこと。同じ轍を踏まないために。**

### 5.1 「log では『レベル1 ⟺ $p$-曲率0』が崩れる」という見立て

**誤り。**素朴な Frobenius 引き戻し $F^*$ と $\mathcal{D}^{(1)}$-作用への持ち上げを混同していた。
$F^*(d\log t)=0$ から「$a\neq0$ は持ち上がらない」と結論したが、
$\mathcal{D}^{(1)}(\log)$ では $\binom{\theta}{p}$ が基底元として存在し、
$\mathbb{Z}_p$ の恒等式 $\prod_{j=0}^{p-1}(\theta-j)=p!\binom{\theta}{p}$ の左辺が mod $p$ で $\theta^p-\theta$ となるため、
持ち上げは存在する。**規約のズレであって数学的現象ではなかった。**

### 5.2 「Hecke 変形で回避できないことを示す」という当初のタスク1

**逆だった。**階数 $1$・$r\ge1$ では格子の取り替えで exponent を自由に動かせるので、
局所的な障害は常に回避できる（§3.2）。
**log 構造（marked point）は障害を消す方向に働く。**
反例の存在には格子の剛性（oper 構造）と $r=0$ の両方が必要 —— と当初考えたが、それも §5.5 で否定された。

### 5.3 $\mathfrak{sl}_2$ level $k=p-2$ の WZW 融合則による数え上げ

**誤り。**$\binom{p+1}{3}$（$p=5$ で 20）と主張したが正しくは 5。
原因：radius は $\mathbb{F}_p^\times/\{\pm1\}$（$(p-1)/2$ 個）に値をとるのに、
$\{0,\dots,p-2\}$（$p-1$ 個）の可積分ウェイトと対応させた。
また Wakabayashi の $^\dagger C_1$ には**パリティ条件 $\sum\lambda_i\in2\mathbb{Z}$ がない**。
WZW 融合則をそのまま持ち込んではいけない。

### 5.4 素朴な $\lambda$ 定式化での $N\ge2$ の数え上げ

**誤り。**「$\lambda_i$ 奇・$p\nmid\lambda_i$・三角・$\sum\lambda_i<2p^N$」だけでは
$^\dagger C_N$ の条件 (b) が落ちるため過大評価になる。
$p=5,N=2$：345（誤）vs 225（正）。$p=7,N=2$：3122（誤）vs 1666（正）。
$N=1$ では (b) が空条件なので一致してしまい、誤りに気づきにくい。

**さらに悪いことに**、当初の応答では 610 / 2262 という数値を「計算機で確認」と称して提示したが、
実際には計算していなかった（素朴定式化ですらない、別の誤り）。**数値を出すときは必ず実行すること。**

### 5.5 「$r=0$、種数 $g\ge2$ に反例がある」という予想

**否定された。**$^\dagger C_N\subseteq{}^\dagger C_{N+1}$ から
totally degenerate な曲線上では制限写像が全射（§3.3）。
$F^1$-射影構造で $F^2$-射影構造に持ち上がらないものは（少なくともこの範囲では）存在しない。

### 5.6 root stack 定理を独自の結果と考えた

Lorenzon–Montagnon の indexed algebra、および Ohkawa のレベル $m$ 版 Ogus–Vologodsky/Schepler
で既出の可能性が高い。独自性の主張は文献確認まで保留。

### 5.7 arXiv PDF の全文取得

`web_fetch` で arXiv の PDF を取ると §4.3 付近で切断され、2201.11266 の §6.4 本文に到達できなかった。
続編 2209.08528 の §10 に等価な情報があったため回避できたが、
今後は ar5iv / HTML 版 / ローカル DL を検討すること。

---

## 6. 未解決問題

優先度順。

### 6.1 一般 smooth 曲線での $\mathrm{res}_N$ 全射性 **[最優先]**

§3.3 は totally degenerate な曲線までしか押さえていない。
generic étaleness（Wakabayashi 2209.08528 Thm. C(i)：$\mathcal{O}p^{\mathrm{Zzz}}_{\rho,g,r}$ は
$\mathbb{F}_p$ 上滑らかで次元 $3g-3+r$、$\Pi_{\rho,g,r}$ は totally degenerate な点上で étale）
から直接導く議論を書く。
あるいは Thm. D（canonical diagonal lifting、$\mathscr{L}_\blacktriangle:\mathrm{Op}^{\mathrm{Zzz}}_{1,X}\xrightarrow{\sim}\mathrm{Op}^{\mathrm{Zzz}}_{N,X_0}$）
を使って、「レベル $N\to N+1$ の上昇」を「char $p^N\to p^{N+1}$ の算術的持ち上げ」に翻訳するのが本筋か。
2209.08528 §1.6 に「レベルを上げることと char $p^N$ に持ち上げることの直接の連関がある」との記述あり。

### 6.2 $\#{}^\dagger C_N$ の閉じた公式

$N=1$：$p(p^2-1)/24$（**[数値]**、一般証明なし）。
$N\ge2$：Wakabayashi Thm. E により擬多項式 $H_{N,\mathbb{G}}(p)$（$g=2$ で次数 $3N$）として存在するが明示式なし。
既知値：$p=3$: 1, 11, 121; $p=5$: 5, 225; $p=7$: 14, 1666; $p=11$: 55, 24805; $p=13$: 91, 67431。

### 6.3 $^\dagger C_1$ の四角錐数への同一視の証明

$n=(p-1)/2$ に対し $\#{}^\dagger C_1=n(n+1)(2n+1)/6$。純粋に組合せ論の問題。

### 6.4 一般階数 $n\ge3$

§3.3 の議論は $n=2$ の generic étaleness に依存。
$\Pi_{n,N,\rho,g,r}$ の generic étaleness を示せば $\mathrm{PGL}_n$ でも反例非存在が従う。
これは Wakabayashi 自身が「一般の $n$ でも canonical lifting は存在すると期待される」として
未解決にしている問題と同値。

### 6.5 障害の局在定理の完成

§3.6 の穴（$p\mid n$ の場合、$\det$ 以外の障害の非存在）を埋める。

### 6.6 高次元

$\dim X\ge2$、$D$ が SNC のとき exponent は $(\mathbb{Z}/p^N)^{\times r}$ に値をとる。
交差 $D_i\cap D_j$ での両立条件が新しい障害を生むか。
$\mathrm{Pic}$ の代わりに $H^2$ の捩れ・Brauer 群が効く可能性。

### 6.7 一般 $(G,P)$

§4.3。$\pi_1(G)$ の $p$ 部分と障害の関係の一般命題。

### 6.8 中間領域

dormant（留数 toral）と nilpotent indigenous bundle（留数冪単）は交わらない（§3.1）。
$p^N$-曲率が冪零だが非零のクラスに橋渡しがあるか。

---

## 7. 文献確認が必要な事項

| # | 事項 | 出典 | 現状 |
|---|---|---|---|
| 1 | Theorem 6.4.3 の完全な主張 | Wakabayashi, arXiv:2201.11266, §6.4 | **未読**。PDF が §4.3 で切断。ar5iv/ローカル DL が必要。§2.5 の辞書は続編から再構成したもの |
| 2 | Prop. 10.3.3 の径数付けとレベル降下の両立性 | Wakabayashi, arXiv:2209.08528, §10.3 | **未読**。§3.3 の穴の核心 |
| 3 | §10.4 "Explicit computations for $(g,r)=(0,3)$" | 同上 | **未読**。$p=5$ の具体例が載っている可能性。§3.5 との突合せ |
| 4 | §10.6 Ehrhart 擬多項式の明示式 | 同上 | **未読**。§6.2 に直結 |
| 5 | Thm. D（canonical diagonal lifting）の完全な主張と証明 | 同上, §9.2, Thm-Def. 9.2.1 | 概要のみ既読。§6.1 に直結 |
| 6 | Thm. C(i) generic étaleness の仮定（$p>2$、$\rho$ の条件） | 同上, Cor. 8.4.4, Thm. 8.7.1 | 概要のみ既読 |
| 7 | Ogus–Vologodsky/Schepler の log・高レベル版 | Ohkawa, Rend. Sem. Mat. Univ. Padova **134** (2015), 47–91 | 要旨のみ。§4.1 の独自性判定に必要 |
| 8 | Mochizuki Chap. II, Prop. 1.4, 1.5 の正確な主張 | Mochizuki, *Foundations of $p$-adic Teichmüller theory*, AMS/IP 11 (1999) | 未確認（Wakabayashi 経由の引用のみ） |
| 9 | Montagnon の thesis の $\mathcal{D}^{(m)}$ presentation | Montagnon, thèse, Rennes I (2002) | 未確認。§5.1 の $\binom{\theta}{p}$ 議論の裏付け |
| 10 | Osserman の論文の正確な巻号 | `log-level-opers.tex` 参考文献 [9] | **書誌情報が不正確**。要修正 |
| 11 | Liu–Osserman Thm. 2.1（Ehrhart 理論による $3g-3$ 次多項式） | [LiOs] | 未確認 |
| 12 | Wak5 = Astérisque **432** (2022) の該当箇所 | Wakabayashi, *A theory of dormant opers on pointed stable curves* | 未確認。radius の定義（Chap. 2, §2.8, Def. 2.32）など |

---

## 8. 次にすべきこと

### ステップ1（1日以内）：文献の穴を塞ぐ

1. arXiv:2201.11266 と arXiv:2209.08528 の PDF をローカルに落とし、
   §6.4 / §10.3 / §10.4 / §10.6 / §9.2 を読む（§7 の #1–#5）。
2. 特に **#2（Prop. 10.3.3 とレベル降下の両立性）**。
   これが確認できれば §3.3 の [部分証明] が [定理] に昇格し、
   本研究の主要主張（反例の非存在）が確定する。
3. #3 と §3.5 の突合せ。$p=5$ の5個が文献と一致すれば独立検証になる。

### ステップ2（数日）：数え上げ

4. `check.py` を拡張して $p=3$, $N=3,4$ を計算し、$1,11,121,1331?$ を確認。
   一致すれば $\#{}^\dagger C_N|_{p=3}=11^{N-1}$ という予想が立つ。
5. $^\dagger C_1$ の四角錐数への同一視を証明（§6.3）。純粋組合せ論、短時間で片付くはず。
6. 条件 (b) の transfer matrix 表示を試す（§4.2）。

### ステップ3（数週）：主定理の完成

7. §6.1（一般 smooth 曲線での全射性）を Thm. D 経由で書く。
8. §3.6 の障害局在定理の穴を埋める（§6.5）。
9. これらが済んだ時点で論文の主張を
   「反例を構成する」から「反例が存在しないことを示し、障害の所在を特定する」へ全面的に書き換える。
   現在の `log-level-opers.tex` は既にその方向に改稿済みだが、序（§1）が古い動機のまま残っている。

### ステップ4：拡張

10. $n\ge3$（§6.4）、高次元（§6.6）、一般 $(G,P)$（§6.7）。
11. root stack 予想（§4.1）の独自性判定（§7 の #7 に依存）。

---

## 付録A：ファイル一覧

- `log-level-opers.tex` — 論文ドラフト（日本語、lualatex/ltjsarticle）。
  `\Todo{}` が3箇所：四角錐数の同一視、一般 smooth 曲線での全射性、Ohkawa との関係。
  `\Known{}` マクロは定義済みだが未使用。
- `check.py` — $^\dagger C_N$ の直接列挙、素朴 $\lambda$ 定式化との比較、入れ子性の検証。
- `verify_p5.py` — $\mathbb{F}_5$ 上の多項式演算で $p=5$ の5個の Wronskian と ODE を検証。

## 付録B：本文書の作成過程で訂正した誤り一覧

引き継ぎ先が過去のログを読む場合に備えて。

1. 「log では $p$-曲率0とレベル1が乖離する」→ 規約のズレ（§5.1）
2. 「Hecke 変形で回避できない」→ 回避できる（§5.2）
3. $\binom{p+1}{3}$ による数え上げ → 誤り、正しくは $p(p^2-1)/24$（§5.3）
4. $N=2$ の個数 610 / 2262 → 誤り、正しくは 225 / 1666（§5.4）
5. 「計算機で確認」と称して未実行だった箇所が複数あった（§5.4 末尾）
6. `log-level-opers.tex` の編集時に §7（$p=5$ の明示計算）を一度削除した。復元済み
