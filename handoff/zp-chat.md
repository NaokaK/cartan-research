# 研究引き継ぎ資料：正標数における $\mathbb{Z}_p$ 値留数と log parabolic geometry

**最終更新**: 2026-09-03
**対応原稿**: `zp-residues-v2.tex`（v2）
**言語方針**: 原稿は英語、内部資料は日本語

---

## 0. この文書の読み方

- **[証明済]** … 完全な証明を書いた、または書ける状態にある。
- **[証明済/要清書]** … 証明の骨格は正しいと確認したが、形式的な詳細（特に PD 環の計算）の清書が残っている。
- **[検算のみ]** … 特殊例での整合性は確認したが一般証明はない。
- **[推測]** … 根拠のある予想。証明はない。
- **[未検討]** … アイデア段階。

この区別は厳密に守ること。v1 から v2 への改訂で 2 箇所の誤りが見つかっており、いずれも「自明だと思って検証を飛ばした箇所」だった（§5 参照）。

---

## 1. 研究目的

正標数 $p>0$ の代数幾何において、境界因子 $D$ を持つ多様体 $(\bar X, D)$ 上の **regular singular stratified bundle**（および無限レベル log parabolic geometry）に対し、$D$ に沿った $p$ 進的な留数不変量を定義し、その理論を展開する。

動機となった三つの類比：

1. **標数 0 の無限遠モノドロミー**。正則特異接続の留数の固有値 mod $\mathbb{Z}$ が局所モノドロミーを記録し、quasi-unipotent 性が基本的有限性を与える。その $p$ 進版が欲しい。
2. **Poincaré–Einstein / conformal infinity**。内部の幾何と境界の共形構造の対応。「共形ウェイト」に対応する不変量が $p$ 進的になるはずだという直観。
3. **Kindler の regular singular stratified bundle における exponent の理論**。これを「全レベルを束ねる」形に組み直す。

log 構造なしにはこの不変量は定義できない（例 6.5 を参照。ν の収束だけでは不十分）。

**副次目標**：境界への制限函手を作って次元に関する帰納法を回せるようにし、tame Gieseker 予想等への応用を得る。

---

## 2. 現在採用している定義と記号規約

### 2.1 基本設定

- $k = \bar{k}$、$\mathrm{char}\,k = p > 0$、$F$ は絶対 Frobenius。
- $\bar X/k$ 滑らか、$D = \sum_{i \in I} D_i$ は単純正規交叉因子（各 $D_i$ 滑らか）、$U = \bar X \setminus D$。
- 局所的には $R = k[[t]]$、$K = k((t))$。

### 2.2 Stratified bundle

$\mathcal{E} = \bigl((E_n)_{n \ge 0}, \sigma_n : F^*E_{n+1} \xrightarrow{\sim} E_n\bigr)$、$E_n \in \mathrm{Vect}(U)$。$E := E_0$。
$\mathcal{D}_U^{(n)} \subset \mathcal{D}_U$ は位数 $< p^n$ の作用素が生成する部分環。

### 2.3 対数格子系とレベル

**格子系**：$\bar E_n \in \mathrm{Vect}(\bar X)$ で $\bar E_n|_U = E_n$。このとき $\bar\sigma_n : F^*\bar E_{n+1} \to \bar E_n$ は $D$ に沿った modification。

**対数的**：各 $\bar E_n$ が $\mathcal{D}_{\bar X}(\log D)$-安定。

$\mathcal{E}$ が **regular singular** $:\iff$ 対数格子系が存在する（Kindler の定義と同値のはず、要確認 §7）。

### 2.4 中心的な作用素（v2 で確定した規約）

局所座標 $t$（$D = \{t=0\}$）に対し
$$D_a := t^a \partial_t^{[a]} \in \mathcal{D}_{\bar X}(\log D), \qquad a \ge 0,$$
$$\delta^{(m)} := D_{p^m} \quad (\text{レベル } m \text{ の対数作用素}), \qquad \delta^{(0)} = D_1 = t\partial_t.$$

**重要**：$\delta^{(m)}$ だけでなく $D_a$ を**全部**扱うこと。v1 では $\delta^{(m)}$ だけを使ったためテンソル加法性の証明が壊れた（§5.1）。

記法：
- $\theta_a := \nabla(D_a) \in \mathrm{End}_k(\bar E_0)$（$k$-線形。$R$-線形ではない）
- $R_a := \mathrm{res}_D \theta_a \in \mathrm{End}_{\mathcal{O}_D}(\bar E_0|_D)$、$R^{(m)} := R_{p^m}$
- $\mathrm{dig}_m(c) \in \{0,\dots,p-1\}$：$c \in \mathbb{Z}_p$ の第 $m$ 桁

### 2.5 $r$-スペクトラム（主定義）

$$\bar E_0|_{D_i} = \bigoplus_{c \in \mathbb{Z}_p} (\bar E_0|_{D_i})^c, \qquad
(\bar E_0|_{D_i})^c = \{x : R_a x = \tbinom{c}{a} x \ \forall a\}$$

**$r$-スペクトラム** := 現れる $c$ の重複度付き多重集合。$(G,P)$ 版では $r_i \in (X_*(T) \otimes \mathbb{Z}_p)/W$。

$\bar E_0$ の Hecke 変形を法として $\bar r_i \in (X_*(T)\otimes\mathbb{Z}_p / X_*(T))/W$。

### 2.6 符号規約（絶対に混同しないこと）

階数 1、$\sigma_n(1 \otimes e_{n+1}) = c_n t^{a_n} e_n$ のとき
$$\boxed{\ r = -\sum_{n \ge 0} a_n p^n\ }$$

- $\mathcal{L}_c$ の定義：$\sigma_n(1\otimes e_{n+1}) = t^{-\mathrm{dig}_n(c)} e_n$。これで $r(\mathcal{L}_c) = c$。
- レベル $n$ 格子の $r$：$r_n := r(\bar E_n)$。関係式 $r = -A_n + p^n r_n$、$A_n = \sum_{i<n} a_i p^i$。
- **Hecke 指数**：$a_n = p\,r_{n+1} - r_n \in \mathbb{Z}$。
- 留数定理：$\sum_x r_x = -\deg \bar E_0$。
- 境界の捻れ：$F^*_{D_i} B_{n+1} \cong B_n \otimes N_i^{\otimes(-a_n)}$、総ウェイト $c$。

### 2.7 log parabolic geometry

$(G,P)$：$\mathbb{F}_p$ 上分裂簡約群と放物型部分群。$P$-束 $\mathcal{G}$ と $\omega : T\mathcal{G}(-\log \tilde D) \xrightarrow{\sim} \mathfrak{g}\otimes\mathcal{O}$。

**無限レベル版**：随伴 tractor 束 $\mathcal{A}_n = \mathcal{G}_n \times^P \mathfrak{g}$ が対数格子系をなす。留数の議論はすべて $\mathcal{A}_\bullet$ だけで書ける（Cartan 接続の非退化性は境界制限の §8(4) でしか使わない）。

---

## 3. 確立した結果

依存関係の順に並べる。各項目の末尾に v2 原稿での番号を付す。

### 3.1 剛性（すべての土台）

**[証明済]** **(3.1)** $\mathcal{D}_{\bar X}(\log D)$ において
$$D_a t^n = \tbinom{n}{a} t^n, \quad D_a^p = D_a, \quad [D_a, D_b] = 0, \quad D_a = \prod_m \tbinom{D_{p^m}}{a_m}.$$
証明：$\mathcal{D}(\log D) \subset \mathrm{End}_k(\mathcal{O})$ は忠実、基底 $\{t^n\}$ 上で対角。最後の式は Lucas。

**[証明済]** **(3.2)** よって $\theta_a$ は可換・$\theta_a^p = \theta_a$、$R_a$ は同時対角化可能で固有値は $\mathbb{F}_p$、同時固有指標は必ず $a \mapsto \binom{c}{a}$（$c \in \mathbb{Z}_p$ 一意）の形。

> **注**：これは $p$-曲率経由の議論（Katz の $\psi(\delta) = \nabla(\delta)^p - \nabla(\delta^{[p]})$）より強い。後者はレベル 0 しか直接扱えない。

**[証明済]** **(3.3)** Leibniz：$\theta_a(fx) = \sum_{b+c=a} D_b(f)\theta_c(x)$。特に $\theta_a(tx) = t\theta_a(x) + t\theta_{a-1}(x)$、$\theta_a$ は $t\bar E_0$ を保ち、$R_a$ は $\mathcal{O}_D$-線形。

**[証明済]** **(3.4)** $\binom{\cdot}{p^m} : \mathbb{Z}_p \to \mathbb{F}_p$ は連続（$\bmod\ p^{m+1}$ にしか依らない）で $\mathrm{dig}_m$ に等しい。

**[証明済]** **(3.5)** $D_i$ 連結なら $R_a$ の固有多項式は定数。

### 3.2 函手性

**[証明済]** **(4.3)(1)** テンソル：$\mathrm{Spec}_r(\mathcal{E}\otimes\mathcal{E}') = \{c + c'\}$（**$\mathbb{Z}_p$ での和**）。
証明：同時固有ベクトル上で $\theta_a(x\otimes x') = \sum_{b+c=a}\theta_b x \otimes \theta_c x'$、Vandermonde $\sum_{b+c=a}\binom{c}{b}\binom{c'}{c} = \binom{c+c'}{a}$。

**[証明済]** 双対 $r \mapsto -r$、群射 $r' = \mathrm{Lie}(\phi)(r)$。

**[証明済/要清書]** **(4.3)(4)** 引き戻し：$f^*D_i = \sum_j e_{ij}E_j$ なら $r_{E_j}(f^*\mathcal{E}) = \sum_i e_{ij} r_{D_i}(\mathcal{E})$。

**[証明済]** **(4.4)** Kummer 被覆（次数 $m$、$p \nmid m$）：$r \mapsto mr$。

### 3.3 局所構造定理（最重要）

**[証明済]** **(5.1)** すべての $\sigma_n$ が格子の同型 $\Rightarrow$ $\mathcal{E}$ 自明。
証明：(i) $\bmod\ t$ で Lang により $g_n \in 1 + tM_N(R)$ に正規化、(ii) $v_n = \lim_N g_{n+N}^{(p^N)}\cdots g_n$ が $t$ 進収束。

**[証明済]** **(5.2)** $R^{(0)} = 0 \Rightarrow$ $\bar E_1$ を取り替えて $\sigma_0$ を格子同型にできる。
証明：$\theta_1$ の $\mathbb{F}_p$-次数付け（$\deg t = 1$）、$\bar E_0 = M + t\bar E_0$（$M = \ker\theta_1$）、$M$ が $k[[t^p]]$ 上自由、$M$ がレベル 1 水平、Cartier 降下。

> **重要な制約**：この証明は $R = k[[t]]$（絶対の 1 変数）でしか通らない。相対版（底空間つき）では最後の Cartier 降下が壊れる（$M$ は底方向に水平ではない）。§5.6 参照。

**[証明済]** **(5.4)** $r = 0 \Rightarrow$ 自明。（(5.2) + レベルシフト + (5.1) の帰納）

**[証明済]** **定理 A (5.5) 局所構造定理**：$K = k((t))$ 上の regular singular stratified bundle は
$$\mathcal{E} \cong \bigoplus_{c \in \mathbb{Z}_p} \mathcal{L}_c^{\oplus n_c}$$
と分解する。よって $\mathrm{Strat}^{rs}(K)$ は半単純で $\mathrm{Rep}(\mathcal{T}_p)$ と同値、$\mathcal{T}_p = \mathrm{Spec}\,k[\mathbb{Z}_p/\mathbb{Z}]$。$r$-スペクトラム mod $\mathbb{Z}$ は完全不変量。$\mathrm{Ext}^1 = 0$。

> **証明の依存順序（循環に注意）**：一般の場合は「格子のブロック分解 (8.6)」を使うが、(8.6) の証明は (3.2)(3.3) しか使わないので循環しない。この順序を崩さないこと。
> $\mathbb{Z}_p/\mathbb{Z}$ のねじれ部分は $\mathbb{Z}_{(p)}/\mathbb{Z}$（位数 $p$ と素）なので $\mathcal{T}_p$ は真の対角化可能群。

**[証明済]** **(5.6)** 系：局所モノドロミーは常に半単純。$\mathfrak{g}$ 内に冪零部分は存在しない。

**[証明済]** **(5.7)** 非半単純性は純粋に大域的：$\mathbb{G}_m$ 上 $\sigma_n = \begin{pmatrix}1&t\\0&1\end{pmatrix}$ は $r=0$ だが非分裂（次数の議論）。$k[[t]]$ 上では $g = \sum_i t^{p^i}$ で分裂する。

### 3.4 比較定理

**[証明済]** **(6.1)** $\tau_n$ が三角で対角 $t^{A_n^{(j)}}$ なら、$m<n$ で $\theta_{p^m}(e_j) \equiv \binom{-A_n^{(j)}}{p^m}e_j$。

**[証明済]** **定理 (6.2)** 岩澤型不変量 $\nu_n^{\mathrm{Iw}} = (A_n^{(j)})_j$ は厳密に加法的、$\nu^{\mathrm{Iw}}_{n+1} = \nu^{\mathrm{Iw}}_n + p^n\mu^{\mathrm{Iw}}_n$、$X_*(T)\otimes\mathbb{Z}_p$ で収束し $-\lim\nu_n^{\mathrm{Iw}} = r$。

### 3.5 階数 1 と例

**[証明済]** **(7.1)** $\mathrm{Pic}^{\mathrm{strat}}(\mathbb{G}_m) \cong \mathbb{Z}_p/\mathbb{Z}$。
**[証明済]** **(7.2)** 留数定理（$\mathbb{P}^1$, rank 1）：$r_0 + r_\infty = -\deg\bar L_0$。
**[証明済]** **(7.3)** Kummer 解釈：$r$ ねじれ $\iff$ tame $\iff$ Kummer 層。
**[証明済]** **(7.4)** $\mathbb{Z}_p \to \mathbb{Z}_p/\mathbb{Z}$ に連続切断なし。ねじれ部分には標準切断 $[0,1)\cap\mathbb{Z}_{(p)}$ があり、これが Katz の canonical extension が tame でのみ存在する理由。
**[証明済]** $\mathrm{Pic}^{\mathrm{strat}}(\mathbb{P}^1\setminus\{0,1,\infty\}) \cong (\mathbb{Z}_p/\mathbb{Z})^2$。

**[検算のみ]** **(7.5)** 二重被覆 $t = z^2$ による誘導 $f_*\mathcal{M}$：$r_0 = \{\alpha/2, (\alpha+1)/2\}$ 等。
留数定理 $\sum\mathrm{tr} = \alpha+\beta+\gamma+\delta+1$ と $\det f_*\mathcal{O} = \mathcal{O}(-1)$ による整合性は確認済み。ただし正標数での tame 押し出しの留数公式の一般証明は書いていない。
**帰結（これは確実）**：$\ker(\pi_1^{\mathrm{strat},rs}(U) \to \pi_1^{\mathrm{tame}}(U)) \ne 1$。

### 3.6 境界制限（v2 で完成）

**[証明済/要清書]** **(8.1) 座標独立性**：$R_a$ は $t$ の選び方に依らない。
証明：対数対角線の PD 座標 $w = t_2/t_1 - 1$。$t' = ut$ に対し $w' = (u_2/u_1)(1+w) - 1$ だが、留数を取る操作（$t_1 = 0$ かつ余法方向を殺す）で $t_2 - t_1 = t_1 w \equiv 0$、$u_2 \equiv u_1$、よって $w' = w$。
**要清書**：log PD envelope の形式的な取り扱い。「余法方向を殺す」の正確な定式化。

**[証明済]** **(8.2)** よって $\bar E_0|_{D_i} = \bigoplus_c (\bar E_0|_{D_i})^c$ は $D_i$ 上大域的・標準的な部分束分解。

**[証明済]** **(8.4) 留数の跳び = Hecke 指数**：$M \subseteq L$ が共に $\mathcal{D}(\log D_i)$-安定で $L$ の $r$-スペクトラムが単一値 $c$、$M$ が単一値 $c'$ なら $a := c'-c \in \mathbb{Z}_{\ge0}$ かつ $M = t^a L$。
証明：$\theta_b(t^a x) = \sum_{i+j=b}\binom{a}{i}\binom{c}{j}t^ax = \binom{a+c}{b}t^ax$（Vandermonde）。$M = t^aL$ は長さの比較。

**[証明済]** **(8.5)** $F^*\bar E_{n+1}$ 上では $R_a = 0$（$p\nmid a$）、$R_{pb} = R_b(\bar E_{n+1})$。つまり桁が 1 つ上にずれ $r(F^*\bar E_{n+1}) = p\,r_{n+1}$。よって $a_n = p\,r_{n+1} - r_n \in \mathbb{Z}^N$。

**[証明済]** **(8.6) 格子のブロック分解**：
$$\bar E = \bigoplus_{\bar c \in \mathbb{Z}_p/\mathbb{Z}} \bar E\{\bar c\}$$
各ブロックは $\mathcal{D}(\log D_i)$-安定な $\widehat{\mathcal{O}}$-部分束、対数格子の射で保たれる。
証明：$\theta_a$ は $\mathcal{O}_{D_i}$-線形なので $\bar E = \bigoplus_{c\in\mathbb{Z}_p}\bar E[c]$ は $\mathcal{O}_{D_i}$-加群分解、$t\cdot\bar E[c]\subseteq\bar E[c+1]$。$\mathbb{Z}_p/\mathbb{Z}$ でまとめると $t$-安定。

> **鍵**：$c \in \mathbb{Z}_p$ ごとの細かい分解は**格子には持ち上がらない**（整数差＝共鳴）。$\mathbb{Z}_p/\mathbb{Z}$ でまとめてはじめて持ち上がる。$K$ 上では共鳴が見えない（$\mathcal{L}_c \cong \mathcal{L}_{c'}$ iff $c-c'\in\mathbb{Z}$）ので定理 A では完全分解になる。

**[証明済]** **(8.7) 正規化**：ブロック内で elementary modification を繰り返し、$r$-スペクトラムを単一値 $c_n$ にできる。各レベル独立に可能。

**[証明済]** **定理 B (8.8) 境界制限**：正規化済みとして $B_n := \bar E_n\{\bar c\}|_{D_i}$、$a_n = pc_{n+1}-c_n$ とすると
$$F^*_{D_i} B_{n+1} \xrightarrow{\sim} B_n \otimes N_i^{\otimes(-a_n)}.$$
$e_n = c_n$ が $e_n = pe_{n+1}-a_n$ を解くので、$(B_n)$ は $(D_i, D_i\cap D^{(i)})$ 上の**ウェイト $c$ の $N_i$-捻れ regular singular stratified bundle**、総捻れ $N_i^{\otimes c}$。
untwist 可能 $\iff$ $c\cdot[N_i] \in \widehat{\mathrm{Pic}(D_i)}_p$ が $\mathrm{Pic}(D_i)$ の像に入る。障害は $\widehat{\mathrm{Pic}(D_i)}_p/\mathrm{Pic}(D_i)$。
随伴 tractor 束は捻れが相殺し常に真の log parabolic geometry。

**[証明済]** **(8.9) 延長判定**：$\mathcal{E}$ が $D_i$ の近傍で stratified bundle に延びる $\iff$ $r_i \in X_*(T)$。

### 3.7 反例（これらも確立した結果）

**[証明済]** **(6.3)** Cartan 型の定義は誤り。$G=\mathrm{GL}_2$、$g_0 = \mathrm{diag}(t,t^{-1})$、$g_1 = \mathrm{diag}(t^{-1},t)$、$g_n=1\ (n\ge2)$：優整形で $\mu_0=\mu_1=(1,-1)$ なので $\sum\mu_np^n = (1+p,-1-p)$ だが実際は $g_0g_1^{(p)} = \mathrm{diag}(t^{1-p},t^{p-1})$、$r = (p-1,1-p)$。

**[証明済]** **(6.4)** $\nu_n$ の収束は正則特異性を含意しない。$\sigma_n = \begin{pmatrix}1&t^{-1}\\0&1\end{pmatrix}$：$\nu_n = (-p^{n-1},p^{n-1})\to 0$ だが $h_{n+1}^p - h_n = t^{-1}$ は $K$ 内で解けない（極の位数 $d_n = \max(pd_{n+1},1)$ が非有界）ので非自明、よって定理 A より正則特異でない。

---

## 4. 検討中のアイデア（未証明）

### 4.1 $p$ 進 middle convolution（v2 §9）

**構成 [推測ベース]**：$S = \{x_1,\dots,x_s\}\subset\mathbb{A}^1$、$c\in\mathbb{Z}_p$ に対し
$$\mathrm{MC}_c(\mathcal{E})_y := \mathrm{im}\bigl(H^1_{dR,c}(\mathbb{A}^1\setminus(S\cup\{y\}), \mathcal{E}\otimes\mathcal{L}_c(y-x)) \to H^1_{dR}(\cdots)\bigr).$$

**[証明済に近い観察]** 定理 A の御利益は「$j_{!*}$ の正規化不要」ではない（そもそも上のコホモロジー的定義は正規化を要しない）。真の御利益は
$$\dim\mathcal{F}^{I_x} = \#\{j : r_{x,j}\in\mathbb{Z}\} =: \delta_x$$
——標数 0 では Jordan ブロック**数**だが、局所半単純性（定理 A）により素の**重複度**になる。よって Katz の指数規則から Jordan ブロックの場合分けが完全に消える。

**[推測] 階数公式 (9.2)**：$c\notin\mathbb{Z}$、$\mathcal{E}$ 既約非自明なら
$$\mathrm{rk}\,\mathrm{MC}_c(\mathcal{E}) = Ns - \sum_{i=1}^s\delta_i - \delta_\infty(c), \qquad \delta_\infty(c) = \#\{j : r_{\infty,j}-c\in\mathbb{Z}\}.$$
導出：$\chi(\mathbb{P}^1, j_{!*}\mathcal{F}) = M(2-|T|) + \sum_x\dim\mathcal{F}^{I_x}$（標数 0 の標準公式）を形式的に適用。Katz の $\sum\mathrm{rk}(A_i-1) - \dim\ker(A_\infty-\lambda^{-1})$ と一致することは確認済み。
**未確立の部分**：正標数の stratified bundle に対する上記 Euler 標数公式・中間延長の理論。

**[推測] 指数規則 (9.4)**：$N' = \mathrm{rk}\,\mathrm{MC}_c(\mathcal{E})$ として
- $x_i$：$\{r_{i,j}+c : r_{i,j}\notin\mathbb{Z}\} \cup \{0\ \text{重複度}\ N'-(N-\delta_i)\}$
- $\infty$：$\{r_{\infty,j}-c : r_{\infty,j}-c\notin\mathbb{Z}\} \cup \{-c\ \text{重複度}\ N'-(N-\delta_\infty(c))\}$

標数 0 からの移送。**[検算のみ]** Gauss 超幾何で検証済み：階数 1（留数 $\alpha,\beta,-\alpha-\beta$）→ 階数 2、
$$\begin{array}{c|c|c} 0 & 1 & \infty\\\hline 0,\ \alpha+c & 0,\ \beta+c & -c,\ -\alpha-\beta-c\end{array}$$
総和 $0$（$\deg\bar E_0 = 0$）。古典的 Riemann scheme と $\gamma = 1-\alpha-c$、$a+b = 1-\alpha-\beta-2c$ で一致（差の $1$ は格子正規化）。例 7.5（$c=1/2$）とも整合。

**[推測]** $\mathrm{rig}(\mathrm{MC}_c\mathcal{E}) = \mathrm{rig}(\mathcal{E})$、$\mathrm{MC}_{c'}\mathrm{MC}_c = \mathrm{MC}_{c+c'}$、$\mathrm{MC}_{-c}\mathrm{MC}_c = \mathrm{id}$。

**[推測] $p$ 進 Katz アルゴリズム (9.7)**：$\mathbb{P}^1$ 上の既約 rigid regular singular stratified bundle はすべて階数 1 から $\otimes\mathcal{L}$ と $\mathrm{MC}_c$ で得られる。
**根拠**：標数 0 では還元段階で特定の位数の 1 の冪根が要るが、ここでは $c$ は環 $\mathbb{Z}_p$ を動くので和が常に存在する。確認すべき条件は $c\notin\mathbb{Z}$ だけ。標数 0 より制約が緩い。

### 4.2 $p$ 進超幾何と Dwork [未検討]

$\mathbb{Z}_p$ パラメータの超幾何 $\mathcal{H}(a,b;\gamma)$ は、各レベルで「パラメータ $\bmod\ p^{n+1}$ の超幾何型方程式の両立系」。これは Dwork の $p$ 進超幾何理論・Dwork 合同式の形そのもの。Frobenius 構造との比較が課題。

### 4.3 剛性指数と rank 2 の分類 [推測]

$\mathbb{P}^1\setminus\{0,1,\infty\}$ 上の既約階数 2 regular singular stratified bundle は $r$-スペクトラム $(r_0,r_1,r_\infty)$ で一意に決まるか（$p$ 進剛性）。$\mathrm{rig} = 2\cdot4 - 3\cdot2 = 2$。定理 A により $\dim Z(r_x) = \sum_{\bar c}m_{x,\bar c}^2$ で Jordan ブロックは介在しない。

### 4.4 高次元留数定理 [推測]

$$\sum_i \mathrm{tr}(r_i)[D_i] = -c_1(\bar E_0) \quad \text{in } \mathrm{CH}^1(\bar X)\otimes\mathbb{Z}_p.$$
階数 1・$\mathbb{P}^1$ でのみ証明済み。

### 4.5 局所-大域完全列 [推測]

局所モノドロミーが常に半単純なので、非半単純性はすべて「内部」に押し込まれる：
$$1 \to (\text{内部}) \to \pi_1^{\mathrm{strat},rs}(U) \to \prod_i\mathcal{T}_p.$$
tame 商は $\mathbb{Z}_{(p)}/\mathbb{Z}$ を経由。Gieseker–Katz の log 版はこの形で定式化すべき。

### 4.6 冪単部分の代替 [未検討]

局所 $\mathrm{Ext}^1 = 0$（定理 A）なので、冪単部分は大域 $\mathrm{Ext}$ にしか住めない：
$$N \in \varprojlim_n \mathrm{Ext}^1_{\mathrm{Strat}^{rs}(U)}(\mathrm{gr}, \mathrm{gr}).$$
Jacobson–Morozov の代わりに「Frobenius 捻れ $\mathfrak{sl}_2$」($e,h,f$ のうち $e$ が $F$-半線形) を探すという案があるが完全に未検討。

### 4.7 捻れ付き帰納法 [未検討・重要]

定理 B の境界対象は $N_i^{\otimes c}$-捻れなので、次元帰納の各段で $\widehat{\mathrm{Pic}(D_i)}_p$ の情報を持ち回る必要がある。この帰納法の枠組みの設計が構造的な主要課題。

---

## 5. 失敗したアプローチと理由

### 5.1 桁ごとの加法性（v1 の誤り）

**主張していたこと**：$R^{(m)}(\mathcal{E}\otimes\mathcal{E}') = R^{(m)}(\mathcal{E}) + R^{(m)}(\mathcal{E}')$。

**なぜ誤りか**：繰り上がりのため $\mathrm{dig}_m(c) + \mathrm{dig}_m(c') \ne \mathrm{dig}_m(c+c')$。反例：$p=5$、$c=1$、$c'=-1$。$\mathrm{dig}_1(1) = 0$、$\mathrm{dig}_1(-1) = 4$、和は $4 \ne 0 = \mathrm{dig}_1(0)$。

**影響**：定理 A の証明で「$\mathcal{L}_{-c}\otimes\mathcal{E}$ の留数が 0」を桁の引き算で正当化していたが、これが崩れる。

**修正**：$\delta^{(m)}$ だけでなく $D_a$ を全部導入し、Lucas 関係 $R_a = \prod_m\binom{R^{(m)}}{a_m}$ を経由して Vandermonde でテンソル加法性を $\mathbb{Z}_p$ の固有値レベルで示す。**教訓：$\mathbb{Z}_p$ の環構造で言えることと桁で言えることを混同しない。**

### 5.2 Cartan 型の定義（定義 A）

**アイデア**：$\mu_n = \mathrm{inv}(\bar E_n, \sigma_n(F^*\bar E_{n+1})) \in X_*(T)^+$（アフィン Grassmannian の相対位置）として $r := -\sum\mu_np^n$。

**失敗の理由**：畳み込みが優整ウェイトに対して加法的でない。$\mathrm{inv}(\Sigma_0,\Sigma_2) \le \mu_0 + p\mu_1$（優位順序）で、差は正コルートの倍数だが $p$ で割れない。したがって $\nu_n \bmod p^n$ が $\mu_0$ を復元せず、$\sum\mu_np^n$ は $\nu_n$ の極限と無関係。反例は §3.7 (6.3)。$W$-軌道として見ても不一致（$p>3$）。

**教訓**：$\mathbb{Z}_p$ 値不変量には**厳密に加法的な**Hecke 不変量が要る。旗に沿った岩澤型 $\nu^{\mathrm{Iw}}$ が正解。

### 5.3 $\nu_n$ の収束だけで留数を定義する

**失敗の理由**：§3.7 (6.4) の例。$\nu_n \to 0$ だが正則特異でない。log 格子系の存在（各レベルで $\mathcal{D}(\log)$-安定）が定義の前提として不可欠。

### 5.4 タスク 3（半単純部分・冪単部分への分解、Jacobson–Morozov、weight filtration）

**元のアイデア**：$r = r_{ss} + r_u$、$r_u$ に Jacobson–Morozov で $\mathfrak{sl}_2$ を付随させ $D$ 上の weight filtration を構成。

**失敗の理由（決定的）**：$(\delta^{(m)})^p = \delta^{(m)}$ が $\mathcal{D}(\log D)$ の恒等式なので、全レベルの留数が半単純（3.2）。さらに定理 A で $\mathrm{Ext}^1_{\mathrm{loc}} = 0$。**$\mathfrak{g}$ の中に適用すべき冪零元が存在しない。**

**副次的失敗**：$\mathbb{Z}_p$ には順序がないので、たとえ冪単部分があっても weight filtration は非標準。tame（$r\in\mathbb{Z}_{(p)}$）の場合のみ $[0,1)\cap\mathbb{Z}_{(p)}\subset\mathbb{Q}$ の標準切断で順序が入る。

**残された道**：§4.6（大域 $\mathrm{Ext}$）。ただし完全に未検討。

### 5.5 定理 B の捻れ指数を桁で書く（v1 の誤り）

**主張していたこと**：$F^*(\bar E_{n+1}|_{D_i})^c \cong (\bar E_n|_{D_i})^c \otimes N_i^{\otimes(-\mathrm{dig}_n(c))}$。

**なぜ誤りか**：正しい指数は Hecke 指数 $a_n = pc_{n+1} - c_n$。両者は繰り上がりの分ずれる（格子を正規化すれば一致する）。総捻れ $\sum a_np^n = -c$ は同じなので結論 $N_i^{\otimes c}$ は変わらない。

### 5.6 相対版局所構造定理を証明しようとしたこと

**アイデア**：定理 A の $S$ 上相対版を証明して定理 B のギャップを埋める。

**なぜ断念したか**：補題 5.2 の証明の最終段（Cartier 降下）が相対化しない。$M = \ker\theta_1$ は $t$ 方向にはレベル 1 水平だが**底方向には水平でない**ので、絶対 Frobenius に沿った降下ができない。

**代替（成功）**：座標独立性 (8.1) + 留数の跳び (8.4) + 格子のブロック分解 (8.6) の三点で迂回。相対版は不要になった。ただし相対版そのものは依然として未解決（§6 参照）。

### 5.7 $j_{!*}$ の正規化が $p$ 進 middle convolution の障害だという見立て

**失敗の理由**：見立てが的外れだった。$\mathrm{MC}$ はコホモロジー的に $\mathrm{im}(H^1_c\to H^1)$ で定義でき、標準延長（canonical extension）を必要としない。$\mathbb{Z}_p\to\mathbb{Z}_p/\mathbb{Z}$ に切断がないこと (7.4) は無関係。

**実際の御利益**：局所半単純性による Jordan ブロック消去（§4.1）。

### 5.8 標数 0 の canonical extension の $p$ 進版を作ること

**不可能であることが証明済み** (7.4)：$\mathbb{Z}_p\to\mathbb{Z}_p/\mathbb{Z}$ に連続切断はない。ねじれ部分（tame）でのみ可能。これは失敗ではなく確立した否定的結果として扱うこと。

---

## 6. 未解決問題

優先度順。

### P1. $\mathrm{MC}_c$ は正則特異性を保つか
**§9 の主要ギャップ。** 同値な問い：正則特異 stratified bundle のアフィン曲線族に沿った Gauss–Manin 成層化は再び正則特異か。標数 0 では標準的。これが立たないと §9 全体が宙に浮く。

### P2. $H^1_{dR}$ の局所自由性と基底変換
構成 9.1 で $\mathrm{MC}_c(\mathcal{E})$ が予想される階数の vector bundle になるための仮定を特定する。

### P3. 指数規則 (9.4) の内在的証明
標数 0 からの移送ではなく、局所 Gauss–Manin 留数の直接計算で。これができれば $\mathrm{rig}$ 不変性 (9.5) も従う。

### P4. 座標独立性 (8.1) の清書
log PD envelope の形式的取り扱い。「余法方向を殺す」の正確な定式化。具体的には $D'_a - D_a \in t\mathcal{D}(\log D) + \mathcal{D}(\log D)\cdot\mathrm{Der}_{D_i}$ の直接検証でもよい。

### P5. 相対版局所構造定理
$S$ 上の族としての定理 A。定理 B には不要になったが、それ自体として必要になる場面が出るはず（特に §4.7 の捻れ付き帰納法）。補題 5.2 の Cartier 降下を相対化する方法を探す。

### P6. 捻れ付き帰納法の枠組み設計
$N_i^{\otimes c}$-捻れ対象に対する帰納法の仮定の正しい定式化。$\widehat{\mathrm{Pic}(D_i)}_p$ を持ち回る。

### P7. rank 2 on $\mathbb{P}^1\setminus\{0,1,\infty\}$ の分類
$p$ 進剛性。実現可能な $(r_0,r_1,r_\infty)$ の特定。

### P8. 高次元留数定理 $\sum\mathrm{tr}(r_i)[D_i] = -c_1(\bar E_0)$

### P9. 大域 $\mathrm{Ext}$ 対象 $N$ と「Frobenius 捻れ $\mathfrak{sl}_2$」
冪単部分の代替。完全に未検討。

### P10. $\mathcal{T}_p$ と局所 stratified 基本群の比較
不正則対象（例 6.4）を含めた完全な局所理論。

### P11. 例 7.5 の押し出し留数公式の一般証明
正標数における tame 有限被覆に沿った $f_*$ の $r$-スペクトラム公式。

---

## 7. 文献確認が必要な事項

**最優先（優先権・重複に関わる）**

1. **Kindler, "Regular singular stratified bundles and tame ramification"**
   - exponent の理論が定理 A（局所半単純性、$r$ が完全不変量）をすでに含んでいるか。
   - 定式化が $\mathbb{Z}_p$ か $\mathbb{Z}_p/\mathbb{Z}$ か、桁の族としてか。
   - 「$\mathrm{Strat}^{rs}(K) \simeq \mathrm{Rep}(\mathcal{T}_p)$」に相当する記述の有無。
   - regular singular の定義（§2.3）が彼のものと同値であることの確認。

2. **Christol–Mebkhout の $p$ 進 exponent 理論**
   - $p$ 進微分方程式（環状領域上）の exponent は $\mathbb{Z}_p$ ないし $\mathbb{Z}_p/\mathbb{Z}$ に値を取る。**本研究の $r$ と形式的に非常に近い。**
   - 単なる類比か、実質的な対応があるか。特に「$\mathbb{Z}_p$ 値」であることの理由が同根か。
   - 関連：André, Baldassarri–Chiarellotto。

3. **Esnault–Kindler, "Lefschetz theorems for tamely ramified coverings"**
   - tame Gieseker 予想の現状。§4.5 の完全列との関係。

**中優先**

4. **Berthelot の arithmetic $\mathcal{D}$-modules（レベル $m$ の理論 $\mathcal{D}^{(m)}$）**
   - $\delta^{(m)} = t^{p^m}\partial^{[p^m]}$ が標準的な記法・対象として既に存在するか。
   - $D_a^p = D_a$（3.1）が既知の事実か。おそらく既知。

5. **Katz–Oda / Gauss–Manin**
   - stratified bundle（$F$-divided sheaf）の相対 de Rham コホモロジーが再び stratified になることの正確な参照。P1, P2 の前提。

6. **Katz, "Rigid Local Systems"**
   - $\mathrm{MC}_\lambda$ の指数規則・剛性指数・アルゴリズムの正確な形（§9 の移送元）。特に $\infty$ での規則の符号規約。

7. **Dettweiler–Reiter**
   - 線形代数版 $\mathrm{MC}$。$\mathbb{Z}_p$ 版を書き下すときのモデル。

8. **Dwork**
   - $p$ 進超幾何、Dwork 合同式、Frobenius 構造。§4.2。
   - "$p$-adic cycles"、Dwork–Gerotto–Sullivan。

**低優先（応用先の確認）**

9. **Gieseker**、**dos Santos**（stratified sheaves の基本群スキーム）
10. **Esnault–Mehta**（単連結射影多様体上の stratified bundle）— §4.4 の $\mathbb{P}^n$ 応用
11. **Katz, "Nilpotent connections"** — canonical extension、$p$-曲率公式
12. **Ogus / Shiho** — 正標数の log 構造、log de Rham。「log inertia group scheme が $\mathbb{Z}_p$ の Cartier 双対」という記述の有無。

---

## 8. 次にすべきこと

### 短期（すぐ着手可能）

**S1. P4（座標独立性の清書）**
定理 B の唯一の「要清書」箇所。log PD envelope の計算を正確に書くか、$D'_a - D_a$ の直接評価を行う。これで §8 が完全に定理になる。所要：小。

**S2. 文献確認 1, 2**（Kindler と Christol–Mebkhout）
とくに Christol–Mebkhout との関係は本研究の位置づけを大きく変えうる。原稿を書き進める前に済ませるべき。所要：小～中。

**S3. P3（指数規則の内在的証明）**
局所 Gauss–Manin 留数の直接計算。$\mathcal{L}_c(y-x)$ の $y$ 方向の挙動を、定理 A の局所分解を使って書き下す。標数 0 からの移送を排除でき、P1 への足がかりにもなる。所要：中。

### 中期

**S4. P1（$\mathrm{MC}_c$ の正則特異性保存）**
§9 の本丸。定理 B（境界制限）を使って、$y \to x_i$ の極限を制御する方針が考えられる。所要：大。

**S5. 定理 B からの即座の応用**
- $\pi_1^{\mathrm{strat},rs}(\mathbb{A}^n) = 1$ と Lefschetz 型定理（(8.9) と引き戻し規則 $e=1$ を使う）
- P8（高次元留数定理）
これらは既存の結果だけで書けるはず。所要：中。

**S6. P7（rank 2 の分類）**
S3/S4 が進めば $\mathrm{MC}_c$ で実現可能性が示せる。

### 長期

**S7. P6（捻れ付き帰納法の設計）** — 構造的な主要課題
**S8. P5（相対版局所構造定理）**
**S9. P9（大域 $\mathrm{Ext}$ と冪単部分）** — 新しいアイデアが必要
**S10. tame Gieseker 予想の帰納法による別証明**

### 推奨する順序

```
S1, S2 （並行、まず片付ける）
  ↓
S3 ────→ S4 ────→ S6
  ↓
S5 ────→ S7 ────→ S10
           ↑
          S8
```

S9 は独立で、いつでも着手できるが見通しが立っていない。

---

## 9. リポジトリ運用メモ

- `zp-residues-v2.tex` が現行原稿。`\TODO`（赤）・`\GAP`（橙）・`\CHECK`（青）マクロで未証明箇所を可視化してある。提出前に削除。
- 現時点で残る `\GAP` は 0 個（v2 で解消）。`\CHECK` は (8.1) の清書、(7.2) の高次元版、(9.4)(9.5) の内在的証明、(7.5) の押し出し公式。
- **証明の依存順序を崩さないこと**：(3.1)(3.2)(3.3) → (8.6) → (5.5)。定理 A は格子のブロック分解を使うが、後者は剛性しか使わないので循環しない。
- 符号規約（§2.6）を変更する場合は、(7.2) 留数定理、(8.5) Hecke 指数、(9.4) 指数規則の三箇所を同時に直すこと。
- v1（`zp-residues.tex`）は §5.1, §5.5 の誤りを含むので参照しないこと。改訂の経緯だけが有用。
