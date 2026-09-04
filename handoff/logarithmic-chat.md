# 引き継ぎ文書：正標数における log stratified parabolic geometry と holonomy

**作成日**: 2026-09-03
**対象**: 新規研究リポジトリへの引き継ぎ
**注記**: 本文書では **[確立]** / **[条件付き確立]** / **[推測]** / **[誤り・訂正済]** のタグで主張の地位を厳密に区別する。タグの無い記述は定義・記法・方針であり、真偽を問うものではない。

---

## 0. 共通設定・記法

- $k = \overline{\mathbb{F}}_p$（$p > 0$）。以下、代数閉体であることを本質的に使う箇所は明示する。
- $X/k$：滑らかな射影多様体。$D \subset X$：SNC 因子。$U = X \setminus D$。基点 $x \in U(k)$。
- $G/k$：連結簡約群。$P \subset G$：放物型部分群。$\mathfrak{g} = \mathrm{Lie}(G)$、$\mathfrak{p} = \mathrm{Lie}(P)$、$\mathfrak{n} = \mathrm{Lie}(R_u(P))$、$\mathfrak{l} = \mathfrak{p}/\mathfrak{n}$。
- **標準仮定 (H)**：$p$ は $G$ にとって good かつ $\mathfrak{g}$ は $G$-加群として自己双対。§6 の数値的障害でのみ使用。

### 微分作用素環

- $F_{(X,D)}: (X,D) \to (X,D)^{(1)}$：log Frobenius。
- $\mathcal{D}^{(m)}_{(X,D)} := \mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)$（log divided power 版）、$\mathcal{D}_{(X,D)} = \bigcup_{m \geq 0} \mathcal{D}^{(m)}_{(X,D)}$。
- $\mathrm{Strat}((X,D))$：$\mathcal{O}_X$-局所自由な $\mathcal{D}_{(X,D)}$-加群の圏。
- $\mathrm{Strat}^{rs}(U) \subset \mathrm{Strat}(U)$：ある log 拡張 $(X,D)$ を持つ対象からなる充満部分圏（Gieseker–Kindler の regular singular）。
- $\pi_1^{\mathrm{strat},rs}(U,x) := \underline{\mathrm{Aut}}^\otimes(\omega_x|_{\mathrm{Strat}^{rs}(U)})$：$k$ 上の pro-代数的アフィン群スキーム。**pro-有限ではない**（これが本研究の全ての面白さの源）。

### 外部から引用する主張（未検証、§7 参照）

- **(K)** [Kindler]：$\pi_1^{\mathrm{strat},rs}(U,x)$ の最大 pro-有限商は定数群スキーム $\pi_1^{\mathrm{tame}}(U,x)_k$。
- **(dS)** [dos Santos 型]：普遍 torsor $\widetilde{U}^{rs} := \underline{\mathrm{Isom}}^\otimes(\omega_x, \omega_{\mathrm{univ}}) \to U$ がアフィン pro-スキームとして存在し、$\pi_1^{\mathrm{strat},rs}$-torsor である。

---

## 1. 研究目的

**中心的主張（証明すべきテーゼ）**：

> 標数 0 の Cartan 幾何における「developing map + holonomy 表現」の真の類似が正標数で得られるのは、**stratification（無限レベル）** と **log 構造（= regular singular）** の**両方**を課したときに限る。片方を落とすと holonomy は存在しないか、意味を失う。

これを次の三つの対比として定式化する：

1. **stratification の必要性**：有限レベル（$\mathcal{D}^{(n)}$-加群、特に $p$-曲率 0 の場合 $n=0$）では、Frobenius 降下 $\mathcal{E} \cong F^{(n+1)*}\mathcal{E}_{n+1}$ しか得られず、$\mathcal{E}_{n+1}$ の属する圏 $\mathrm{Bun}(X^{(n+1)})$ は Tannaka 圏でないため holonomy が定義できない。
2. **log の必要性**：log を課さない一般の stratified bundle は wild で、境界における developing map の延長が存在せず、pro-有限商が $\pi_1^{\mathrm{tame}}$ でなくなるため完備性・離散性の概念が崩壊する。
3. **両方揃うと何が得られるか**：Tannaka 的 holonomy $\rho: \pi_1^{\mathrm{strat},rs}(U) \to G$、pro-スキーム上の developing map、完備性 = $\mathbb{F}_q$-構造、Deligne–Lusztig 多様体による一意化。

### 副次目標

- 完備性の正しい類似の同定（$k$ に位相がないため「離散部分群」が使えない問題への回答）。
- 逆問題：どんな $\rho$ が log parabolic geometry から来るか（数値的障害の導出）。
- 例による検証：トーリック、半アーベル、Deligne–Lusztig / Drinfeld。

---

## 2. 現在採用している定義

### 定義 2.1（log stratified parabolic geometry、型 $(G,P)$）

三つ組 $\mathcal{P} = (\mathcal{E}, \Sigma, \mathcal{E}_P)$：

1. $\mathcal{E} \to X$：$G$-torsor（fppf）。
2. $\Sigma$：$\mathcal{E}$ 上の **log stratification**。同値な三つの記述を状況に応じて使い分ける：
   - (a) テンソル関手 $\Phi_{\mathcal{E}}: \mathrm{Rep}_k(G) \to \mathrm{Strat}((X,D))$、$V \mapsto \mathcal{E} \times^G V$；
   - (b) 対角線の log divided power 近傍上の降下データ（Grothendieck の意味の stratification）；
   - (c) 無限の Frobenius 分解の塔 $\mathcal{E} \cong F^*_{(X,D)}\mathcal{E}_1 \cong F^{2*}\mathcal{E}_2 \cong \cdots$（各 $\mathcal{E}_m$ は $X^{(m)}$ 上の $G$-torsor）。
3. $\mathcal{E}_P \subset \mathcal{E}$：$P$-還元。$\Sigma$ には従属しない（$\mathcal{E}_P$ 自身は平坦でなくてよい）。
4. **横断性（Cartan 条件）**：$\Sigma$ の 1 次部分が定める log 接続 $\nabla$ から誘導される Kodaira–Spencer 写像
   $$\kappa: T_X(-\log D) \longrightarrow \mathcal{E}_P \times^P (\mathfrak{g}/\mathfrak{p})$$
   が $\mathcal{O}_X$-同型。

$\kappa$ の構成：$\nabla$ は $T_X(-\log D) \to \mathcal{E} \times^G \mathfrak{g} = \mathrm{ad}(\mathcal{E})$ を与え、$\mathcal{E}_P$ による商 $\mathrm{ad}(\mathcal{E}) \twoheadrightarrow \mathcal{E}_P \times^P(\mathfrak{g}/\mathfrak{p})$ と合成する。

### 定義 2.2（レベル $n$ 版）

定義 2.1 の $\Sigma$ を $\mathcal{D}^{(n)}_{(X,D)}$-構造（塔の記述で言えば長さ $n+1$ の有限塔）に弱めたもの。

### 定義 2.3（holonomy）

- $\rho_{\mathcal{P}}: \pi_1^{\mathrm{strat},rs}(U,x) \to G_k$：$\Phi_{\mathcal{E}}$ と $\omega_x \circ \Phi_{\mathcal{E}} \cong \mathrm{forget}$ から Tannaka 双対で得られる射。$\mathcal{E}_x \cong G$ の選択の分だけ $G(k)$-共役の不定性がある。
- $\bar\rho_{\mathcal{P}}: \pi_1^{\mathrm{strat},rs}(U,x) \to G^{\mathrm{ad}}$：**幾何が本質的に決めるのはこちら**。$\mathrm{ad}(\mathcal{E})$ が生成する $\mathrm{Strat}^{rs}(U)$ の Tannaka 部分圏の Galois 群への射。

### 定義 2.4（developing map）

(dS) の普遍 torsor 上の $\rho$-同変射
$$\delta: \widetilde{U}^{rs} \to G/P, \qquad \delta(\gamma \cdot u) = \rho(\gamma)\delta(u).$$

### 定義 2.5（完備性）

$\bar\rho_{\mathcal{P}}$ の像が有限（有限定数群スキーム）であること。§3.4 でこれが他の複数の条件と同値であることを示す。

**設計上の判断**：char $p$ では $k$ に位相が無く「離散部分群」が使えないため、「離散」を「有限」に置き換え、その正当化を Lang の定理と Noether–Deuring に求める。

---

## 3. 確立した結果

### 3.1 [確立] holonomy の Tannaka 的構成（順方向）

**定理 A（順方向）**：定義 2.1 の $\mathcal{P}$ に対し、テンソル関手 $\Phi_{\mathcal{E}}: \mathrm{Rep}_k(G) \to \mathrm{Strat}^{rs}(U)$ と自然同型 $\omega_x \circ \Phi_{\mathcal{E}} \cong \mathrm{forget}$ が与えられるから、Tannaka 双対（Deligne–Milne, Thm 2.11）により群スキームの射 $\rho_{\mathcal{P}}: \pi_1^{\mathrm{strat},rs}(U,x) \to G_k$ が $G(k)$-共役を除いて一意に定まる。その像は $\{\mathcal{E}\times^G V\}_V$ が生成する Tannaka 部分圏の Galois 群である。

**地位**：完全に形式的。幾何は一切使わず、$\Sigma$ が存在することのみを使う。**確立とみなしてよい。**

**注意**：逆方向（$(\rho, s) \mapsto \mathcal{P}$）は (dS) に依存するので **[条件付き]**（§7）。

### 3.2 [確立] holonomy はどの基本群の表現か

**命題**：$\rho_{\mathcal{P}}$ は一般に $\pi_1^{\mathrm{tame}}(U,x)$ の表現**ではない**。(K) を認めれば完全列
$$1 \to N \to \pi_1^{\mathrm{strat},rs}(U,x) \xrightarrow{\pi} \pi_1^{\mathrm{tame}}(U,x)_k \to 1$$
があり（$N$ は非自明な有限商を持たない pro-代数的部分群）、$\rho$ が $\pi$ を経由するのは像が有限のときに限る。

**地位**：(K) を認めれば **[条件付き確立]**。$\rho$ が $\pi$ を経由 ⟺ 像が有限、の部分は定義から即座（$\pi_1^{\mathrm{tame}}$ は pro-有限、$G$ は代数群、pro-有限群の代数群への連続射の像は有限）。

**この命題は「注意点」への直接の回答であり、論文では早い段階で明示すべき。**

### 3.3 [確立] 完備性の同値条件

**定理 D**：$k = \overline{\mathbb{F}}_p$、$\mathcal{P}$ を定義 2.1 の幾何とする。以下は同値：

1. $\bar\rho_{\mathcal{P}}$ の像が有限。
2. $\mathrm{ad}(\mathcal{E})$ がある有限 tame 被覆 $V \to U$ 上で stratified bundle として自明化される。
3. ある $q = p^s$、有限部分群 $\Gamma \subset G^{\mathrm{ad}}(\mathbb{F}_q)$、および tame な $\Gamma$-torsor $V \to U$ が存在して $\mathcal{E}^{\mathrm{ad}} \cong V \times^\Gamma G^{\mathrm{ad}}$、かつ $\bar\rho$ は $\pi_1^{\mathrm{tame}}(U) \twoheadrightarrow \Gamma$ を経由する。
4. period map $\delta_V: V \to G/P$ が有限 tame 被覆 $V \to U$ 上のスキームの射として存在する。

**証明の要点**：
- (1) $\Rightarrow$ (3)：像 $\Gamma$ は有限群。Noether–Deuring により有限群の $k$-表現は有限部分体上で定義されるので、適当な $q$ に対し $\Gamma \subset G^{\mathrm{ad}}(\mathbb{F}_q)$。(K) により $\bar\rho$ は $\pi_1^{\mathrm{tame}}$ を経由し、対応する tame 被覆が $V$。
- (3) $\Rightarrow$ (1),(2)：明らか（$V$ 上で torsor は $\Gamma$ 由来なので自明化される）。
- (2) $\Leftrightarrow$ (4)：$V$ 上で $\mathcal{E}$ が自明化されれば $\mathcal{E}_P$ が $V \to G/P$ を与える。逆も同様。

**地位**：(K) に依存するが、それ以外は初等的。**[条件付き確立]**。

**（訂正済）** 前回 (3) を「Lang torsor からの誘導」と述べたが、これは過剰。Lang torsor は $\Gamma = G(\mathbb{F}_q)$ の場合に限られる。上記の形が正しい。

### 3.4 [確立] 命題「開 DL 多様体の固定部分群は $p$-正則」

**命題 4.2**：$G$ 簡約、$F$ を $q$-乗 Frobenius、$X(w_0) = \{gB \in G/B : g^{-1}F(g) \in Bw_0B\}$（開 Deligne–Lusztig 多様体）とする。任意の $x \in X(w_0)$ に対し、固定部分群 $\mathrm{Stab}_{G(\mathbb{F}_q)}(x)$ はある極大トーラスに含まれる。特に位数は $p$ と素である。

**証明**：$x = hB$ とし $B_x := hBh^{-1}$ とおく。$\mathrm{Stab}_{G(\mathbb{F}_q)}(x) = B_x \cap G(\mathbb{F}_q)$。$u$ をこの元とすると $u \in B_x$ かつ $u = F(u) \in F(B_x)$、よって $u \in B_x \cap F(B_x)$。条件 $h^{-1}F(h) \in Bw_0B$ は $B_x$ と $F(B_x)$ が相対位置 $w_0$、すなわち対向する Borel であることを意味するから、$B_x \cap F(B_x)$ は極大トーラス。トーラスに非自明な unipotent 元は無く、全ての元が $p$-正則。Cauchy の定理より位数は $p$ と素。$\square$

**地位**：**完全証明済み。無条件で確立。** 本研究で最も確度の高い新しい主張。

**系（重要）**：完備な幾何において、被覆変換群の作用の固定部分群は $p$-正則。したがって商 $\Gamma \backslash \Omega$ は tame な DM スタックであり、そこに降りた幾何は**自動的に regular singular**。

> **これが「log は追加の仮定ではなく完備性から強制される」という、テーゼの中心的論拠である。**
> char $p$ の「離散群」は必ず有限群であり捻れ無し部分群を持てないため、char 0 と違って商は必然的に分岐する。にもかかわらず $w_0$ 型では分岐が tame に留まる、というのが本質。

### 3.5 [条件付き確立] 数値的障害と Hirzebruch 比例性の再現

**設定**：仮定 (H) の下。定義 2.1 の横断性から $\mathcal{E}_P \times^P (\mathfrak{g}/\mathfrak{p}) \cong T_X(-\log D)$。$\mathfrak{g}$ の自己双対性から $\mathfrak{n} \cong (\mathfrak{g}/\mathfrak{p})^*$ として $\mathcal{E}_P \times^P \mathfrak{n} \cong \Omega^1_X(\log D)$。$\mathcal{E}_P$ による $\mathrm{ad}(\mathcal{E})$ のフィルトレーション $\mathfrak{n} \subset \mathfrak{p} \subset \mathfrak{g}$ から
$$c(\mathrm{ad}\,\mathcal{E}) = c(T_X(-\log D)) \cdot c(\mathcal{L}) \cdot c(\Omega^1_X(\log D)), \qquad \mathcal{L} := \mathcal{E}_P \times^P \mathfrak{l}.$$

**補題**：stratified bundle の Chern 類は数値的に自明。
*証明*：$\mathcal{E} \cong F^{(m)*}\mathcal{E}_m$ より $c_i(\mathcal{E}) = p^{mi} c_i(\mathcal{E}_m)$ が全ての $m$ で成立。$\ell$-進コホモロジー $H^{2i}(X, \mathbb{Z}_\ell(i))$（$\ell \neq p$）で任意の $p$ 冪で割り切れるから捻れ。$\square$

**帰結**：
$$c(T_X(-\log D)) \cdot c(\mathcal{L}) \cdot c(\Omega^1_X(\log D)) = 1 \quad (\text{数値的}).$$

**検証（$G = PGL_3$, $P$ = 点の固定化群、$\dim X = 2$、log 射影構造）**：
$\mathcal{L} = \mathcal{E}nd_0(T)$（$T := T_X(-\log D)$、階数 2）。
- $c(T)c(T^*) = (1+c_1+c_2)(1-c_1+c_2)$、次数 2 部分 $= 2c_2 - c_1^2$。
- $c_2(\mathcal{E}nd_0 T) = 4c_2 - c_1^2$。

合計 $6c_2 - 2c_1^2 = 0$、すなわち
$$\boxed{c_1^2 = 3c_2 \quad \text{（}\Omega^1_X(\log D)\text{ に対して）}}$$
これは古典的な射影構造・球商の Hirzebruch 比例性と完全に一致する。

**地位**：**[条件付き確立]**。導出は正しいが、log 版 Chern 類の交叉理論的取り扱い（$\mathbb{Q}$ 係数か $\mathbb{Z}_\ell$ 係数か、$D$ が非簡約な場合など）を精査する必要がある。ただし数値の一致は偶然ではないと考える。

### 3.6 [確立] Deligne–Lusztig の例

$G = PGL_{d+1}$、$\Omega^d_{\mathbb{F}_q} = \mathbb{P}^d \setminus \bigcup_{H \in \check{\mathbb{P}}^d(\mathbb{F}_q)} H$（Drinfeld 半空間の char $p$ 版、$= X_P(w_0)$）。

- developing map $= $ 包含 $\Omega^d \hookrightarrow \mathbb{P}^d$（開埋め込み）。
- holonomy $= $ Lang 被覆による $\pi_1^{\mathrm{tame}}(\Gamma\backslash\Omega^d) \twoheadrightarrow \Gamma \subset PGL_{d+1}(\mathbb{F}_q)$。
- stratification：$\Omega^d$ 上の自明 $G$-torsor に $F$-固定構造があるので、全レベルの塔が自明に構成できる。
- $P$-還元：トートロジー的旗。横断性：$\dim X_P(w_0) = \dim G/P$ から従う。
- log 性：命題 4.2 の系より商は tame、境界は（wonderful blow-up 後の）SNC 因子。
- $d = 1$：$\Omega^1 = \mathbb{P}^1 \setminus \mathbb{P}^1(\mathbb{F}_q)$、$\Gamma = PGL_2(\mathbb{F}_q)$、商は Dickson 不変式により $\mathbb{A}^1$。これが「$\mathbb{H}/\Gamma$」の char $p$ 完全類似。

**地位**：各構成要素は既知の事実の組み合わせで、**確立**。ただし「これが定義 2.1 の意味の幾何である」という照合を丁寧に書く必要がある。

### 3.7 [確立] 完備性は $w_0$ 型を強制する（部分的）

$\dim X(w) = \ell(w) < \dim G/B$ が $w \neq w_0$ で成立するので、一般の DL 多様体は横断性を満たし得ない。したがって **$G/B$ 型の完備な平坦放物型幾何を与える DL 多様体は $X(w_0)$ のみ**。

**地位**：次元の比較だけなので **確立**。ただし「完備な幾何は必ず DL 多様体の商である」という逆向きの分類は **[推測]**（§6）。

---

## 4. 検討中のアイデア

### 4.1 [推測] developing map の正しい定式化（定理候補 B）

前回検討した二つの候補について：

| 候補 | 内容 | 評価 |
|---|---|---|
| (i) 各有限 tame 被覆上の period map | $\delta_V: V \to G/P$ | **強すぎる**。定理 D により完備な場合にしか存在しない。 |
| (ii) 形式的近傍での Frobenius 同変同型 | $\hat\delta_y: \widehat{U}_y \xrightarrow{\sim} \widehat{(G/P)}_{\delta(y)}$ | **常に存在するが弱すぎる**（局所情報のみ）。 |

**結論（推測）**：どちらも $\delta$ そのものではなく $\delta$ の二つの影であり、両者を貼り合わせる唯一の場所が (dS) の $\widetilde{U}^{rs}$。これは pro-有限方向（tame 被覆）と無限小方向（$N$）を同時に持つ pro-スキームであり、
$$\delta: \widetilde{U}^{rs} \to G/P$$
がトートロジー的に定義され、横断性から**形式的エタール**になる。

**地位**：**[推測]**。(dS) に依存し、かつ「形式的エタール」の証明は未着手。

### 4.2 [推測] 境界における $\mathbb{Z}_p$-冪写像と rs の意味

log stratification は境界 $y \in D$ において、Kummer 形式的被覆 $\mathrm{Spf}\, k[[t^{1/m}]]$（$(m,p)=1$）上でのみ trivialization を与え、$\hat\delta$ は $t \mapsto t^\lambda$（$\lambda \in \mathbb{Z}_p$）型の写像になる。$\lambda \in \mathbb{Z}_p$ であることは $\binom{\lambda}{p^k} \in \mathbb{Z}_p$（二項級数の収束）と同値。

> **解釈**：rs 条件は「境界において developing map が延長するための収束条件」である。wild な場合（$e^{1/t}$ に相当）は $\hat\delta$ が境界に伸びない。

**地位**：**[推測]**。示唆的だが、局所指数の定義（Kindler の residue）との厳密な照合が未了。ただしこれが正しければテーゼの (2)（log の必要性）の中心的な論拠になる。

### 4.3 [推測] rs stratified bundle には unipotent 局所モノドロミーが存在しない

$\log t$ に相当する対象が作れない（$\binom{N}{p^k}$ が $p^k!$ で割り切れない）ため、局所モノドロミーは半単純。char 0 の quasi-unipotent より真に強い剛性。

**地位**：**[推測]**。$\mathrm{Ext}^1_{\mathrm{Strat}^{rs}}(\mathcal{O},\mathcal{O})$ の局所的消滅として定式化すべき。§6 の未解決問題に含める。

### 4.4 [推測] 逆問題の定式化

$\rho$ が log parabolic geometry から来る条件：
1. **切断の存在**：$\mathcal{E}_\rho/P \to X$（$G/P$-束）が切断 $s$ を持つ。障害は非可換 $H^1$。曲線上は Steinberg/Springer で自動になる可能性、高次元は非自明。
2. **横断性**：$\kappa_s$ が同型（切断の空間の開条件）。
3. **数値的障害**：§3.5 の式。
4. **局所条件**：§4.2, §4.3 より、局所モノドロミーは半単純で指数は $\mathbb{Z}_p$。

**地位**：枠組みは妥当と思われるが、どの条件が十分かは未検討。**[推測]**。

### 4.5 [推測] 半アーベル多様体の場合

$1 \to T \to \mathcal{G} \to A \to 0$、$U = \mathcal{G}$、$X$ をトロイダル的コンパクト化。$\rho$ は可換で、格子の役割は prime-to-$p$ Tate 加群（+ 序数的な場合の $p$-可除群の étale 部分）が果たす。階数 1 では $F^*L \cong L$ から $L \in \mathrm{Pic}^0$、$F^*$ は $\widehat{A}$ 上 Verschiebung に対応し、$\varprojlim(\widehat{A}, V)$ が holonomy の受け皿。完備 ⟺ $\rho$ が有限像 ⟺ 幾何が isogeny からの引き戻し。

**地位**：**[推測]。本文書中で最も確度が低い部分。** dos Santos / Esnault–Langer 系統の既知計算との突き合わせが必須。

---

## 5. 失敗したアプローチと理由

### 5.1 [誤り・訂正済] $\mathbb{G}_m$ 上の「レベル $n$ ⟹ $\mathbb{Z}/p^{n+1}$」

**当初の主張**（誤り）：$(X,D) = (\mathbb{P}^1,\{0,\infty\})$、$U = \mathbb{G}_m$、$G = \mathbb{G}_m$ において、レベル $n$ の階数 1 log 幾何の同型類は $\mathbb{Z}/p^{n+1}$ をなし、$\varprojlim_n \mathbb{Z}/p^{n+1} = \mathbb{Z}_p$ で全体が回復される。

**誤りの内容**：パラメータ空間と同型類を混同していた。正確には：

- **[確立]** レベル $n$ の構造は $\theta^{[j]}$（$j < p^{n+1}$）の作用で決まる。Lucas の定理より $\binom{\lambda}{j} \bmod p$（$j < p^{n+1}$）は $\lambda$ の $p$-進展開の下位 $n+1$ 桁のみに依存する。したがって**パラメータ**は $\lambda \bmod p^{n+1} \in \mathbb{Z}/p^{n+1}$。
- **[確立]** しかし同型類を数えると、$\mathcal{O}_{\mathbb{G}_m}$ の自己同型は $k^* \cdot t^{\mathbb{Z}}$ であり、$t^n$ による捻りは $\lambda \mapsto \lambda + n$ を引き起こす。$\mathbb{Z} \to \mathbb{Z}/p^{n+1}$ は**全射**だから、**レベル $n$ の同型類は全て自明**。
- 対照的に無限レベルでは $\lambda \in \mathbb{Z}_p$、$\mathbb{Z} \subset \mathbb{Z}_p$ は稠密だが全射でないので $\mathrm{Hom}(\pi_1^{\mathrm{strat},rs}(\mathbb{G}_m), \mathbb{G}_m) = \mathbb{Z}_p/\mathbb{Z} \neq 0$。

**訂正後の正しい主張**（そしてこれは元の主張より**強い**）：

> **[確立]** $\mathbb{G}_m$ 上では、任意の有限レベル $n$ における階数 1 の不変量は**恒等的に消える**（$\mathrm{Bun}(\mathbb{G}_m^{(n+1)})$ が自明だから）。にもかかわらず無限レベルでは $\mathbb{Z}_p/\mathbb{Z}$ という非自明な holonomy が現れる。

**この現象の構造的説明（重要）**：stratified bundle は「有限レベル対象の逆極限」ではない。対象は塔 $(\mathcal{E}_m)$ と**同型 $F^*\mathcal{E}_{m+1} \cong \mathcal{E}_m$ の選択**の組であり、各 $\mathcal{E}_m$ が自明化可能でも**両立する自明化が取れない**。$L_\lambda$ はまさにその例。

> **教訓**：「有限レベルでは holonomy に届かない」の証明は、同型類の数え上げではなく、**圏の構造**（$\mathrm{Bun}(X^{(n+1)})$ がアーベル圏でなく Tannaka 圏でないこと）で行うべき。

### 5.2 [不採用] 幾何的な普遍被覆による developing map

char $p$ では普遍被覆が pro-有限なので、$\widetilde{U}^{\mathrm{univ}} \to G/P$ という素朴な構成は $\rho$ の像が有限のときしか意味を持たない。**不採用**。定義 2.4（Tannaka 的 torsor 上の $\delta$）を採る。

### 5.3 [不採用] 「離散部分群」による完備性

$k$ に位相構造が無いため、$\Gamma \subset G(k)$ の離散性は定義できない。$\Gamma$ を Zariski 閉かつ 0 次元とすると有限に帰着するので、結局「有限」が唯一の意味のある条件。**Lang の定理による $\mathbb{F}_q$-構造** への言い換え（定理 D (3)）を採用。

### 5.4 [不採用] $\mathcal{E}_P$ にも stratification を課す定式化

char 0 でも $P$-還元は平坦でないため、これは幾何を過剰に制限する（自明な幾何しか残らない）。定義 2.1 では $\Sigma$ を $\mathcal{E}$ にのみ課す。

---

## 6. 未解決問題

### 6.1 主定理候補（未証明部分を明示）

> **主定理候補**
> **(a) 存在**：型 $(G,P)$ の log stratified parabolic geometry $\mathcal{P}$ に対し、holonomy $\bar\rho: \pi_1^{\mathrm{strat},rs}(U,x) \to G^{\mathrm{ad}}$ が存在する。**[§3.1 で確立]** developing map $\delta: \widetilde{U}^{rs} \to G/P$ が存在し形式的エタール、境界では $\mathbb{Z}_p$-冪写像として延長する。**[未証明、§4.1–4.2]**
> **(b) log の必要性**：rs を課さないと (i) 境界での $\hat\delta$ の延長が存在せず、(ii) pro-有限商が $\pi_1^{\mathrm{\acute{e}t}}$（wild 込み）になり完備性の概念が崩壊。**[未証明。(ii) は文献で処理可能と思われる]**
> **(c) stratification の必要性**：レベル $n$ の圏は $\mathrm{Bun}(X^{(n+1)})$ に同値でアーベル圏でなく、Tannaka 再構成が働かない。**[圏論的部分は概ね確立、定量的な障害の記述は未完]**
> **(d) 完備性**：**[§3.3 で確立（(K) 依存）]**。$G/B$ 型の完備例は $X(w_0)$ とその商に限る。**[片側のみ確立、§3.7]**

### 6.2 個別の未解決問題

1. **[最重要]** 主定理候補 (c) の**定量的**な形は何か。$\mathbb{G}_m$ の例（§5.1）では有限レベルで情報がゼロになるが、これは $\mathbb{G}_m$ が特殊（$\mathrm{Pic}$ が自明）だからか。**$X$ が楕円曲線の場合に $\mathrm{Pic}^0$ 上の $F^*$ の像を計算し、真に $\mathbb{Z}/p^n$ 的な現象が現れるか確認せよ。** これが元の「$\mathbb{Z}/p^n$ 予想」を救えるかどうかの試金石。
2. レベル $n$ から $n+1$ への持ち上げ障害を log Atiyah 類 $\mathrm{at}(\mathcal{E}_{n+1}) \in H^1(X^{(n+1)}, \mathrm{ad}(\mathcal{E}_{n+1}) \otimes \Omega^1_{X^{(n+1)}}(\log D))$ で記述する構想はあるが、これは「log 平坦接続の存在」の障害であって「$p$-曲率 0 の接続の存在」の障害ではない。**両者のギャップの正確な記述が未了。**
3. $\pi_1^{\mathrm{strat},rs}(\mathbb{G}_m^n)$ は対角化可能群 $D((\mathbb{Z}_p/\mathbb{Z})^n)$ か。局所剛性（§4.3）から従うはずだが、大域的な $\mathrm{Ext}^1$ の消滅を別途要確認。
4. 完備な幾何の分類：「$\bar\rho$ の像が有限かつ $\delta_V$ が開埋め込み」なら $\Omega := \delta_V(V)$ は必ず DL 多様体 $X_P(w_0)$ か。**[推測、未検討]**
5. $\delta$ の「形式的エタール」の正確な圏論的意味（$\widetilde{U}^{rs}$ が pro-スキームなので、通常のエタール性の定義が使えない）。
6. 逆問題（§4.4）の十分条件。
7. 半アーベルの場合（§4.5）全般。

---

## 7. 文献確認が必要な事項

**優先度順**。番号順に潰すことを推奨。

| # | 確認事項 | 依存する主張 | 想定文献 |
|---|---|---|---|
| 1 | **(K)** $\pi_1^{\mathrm{strat},rs}(U,x)$ の最大 pro-有限商が $\pi_1^{\mathrm{tame}}(U,x)$ であること。**特に $X$ の properness、$D$ への条件（SNC で足りるか）、$U$ の次元条件の細部。** | §3.2, §3.3（定理 D 全体） | Kindler, "Regular singular stratified bundles"; Esnault–Kindler |
| 2 | **(dS)** 普遍 torsor $\widetilde{U}^{rs}$ の存在、およびどの位相で torsor か（fpqc / pro-エタール）。**アフィン pro-スキームとしての性質。** | §4.1（定理 B 全体）、定理 A の逆方向 | dos Santos, "Fundamental group scheme of a $\mathcal{D}$-module" 系統 |
| 3 | regular singular の定義の同値性（log 拡張の存在 vs. 局所指数条件 vs. 有限 tame 被覆上での挙動）。 | §4.2 の解釈全体 | Gieseker; Kindler |
| 4 | log Frobenius 降下・log Cartier 定理の正確な形（$\mathcal{D}^{(n)}_{(X,D)}$-加群 $\simeq \mathrm{Bun}(X^{(n+1)},D^{(n+1)})$）。 | §5.1, 主定理候補 (c) | Ogus–Vologodsky の log 版; Lorenzon; Schepler |
| 5 | stratified bundle の Chern 類の数値的自明性の既知の形（どの係数環、どのコホモロジー）。 | §3.5 | Esnault–Mehta; Biswas–dos Santos |
| 6 | 局所モノドロミーの半単純性 / unipotent 対象の非存在（§4.3）。既知かどうか。 | §4.3, §4.4 の局所条件 | Kindler の局所理論 |
| 7 | 半アーベル多様体・アーベル多様体上の $\pi_1^{\mathrm{strat}}$ の既知計算。 | §4.5 | dos Santos; Esnault–Langer |
| 8 | Deligne–Lusztig 多様体 $X(w_0)$ の Picard 群・基本群、および $\Omega^d_{\mathbb{F}_q}$ の tame 基本群。 | §3.6 | Deligne–Lusztig; Teitelbaum; Orlik–Rapoport |
| 9 | Drinfeld 半空間の char $p$ 版の商が Dickson 不変式で記述されること（$d=1$）。 | §3.6 | 標準的だが要出典 |
| 10 | 「①の反例」の正確な内容と、それが本文書の §5.1 の訂正後の枠組みでどう位置づけられるか。**（本文書は①の内容を「$F$ でちょうど $n$ 回割れる束」型と仮定して書かれている。要確認。）** | 主定理候補 (c) | 前段の議論記録 |

---

## 8. 次にすべきこと

### フェーズ 1：足場固め（1–2 週間想定）

1. **文献確認 #1, #2 を最優先で実施。** (K) と (dS) は本研究の複数の主張の土台であり、これらの正確な形が分からないと定理 B・定理 D が書けない。特に (dS) が使えない場合、§4.1 の定式化を根本から変更する必要がある（代替：$\delta$ を「関手のレベルの射」として定義し、幾何的解釈を諦める）。
2. **文献確認 #10（①の反例）を確認し、§5.1 の訂正内容と接続する。** 本文書は①の内容を仮定して書かれているため、ここがずれていると主定理候補 (c) の記述が変わる。

### フェーズ 2：主定理候補 (c) の完全証明（最短経路）

これが**最も短期間で厳密命題にできる経路**であり、テーゼの三本柱のうち一本を確保できる。

3. **楕円曲線 $E$ 上の階数 1 の場合を計算する（§6.2-1）。** $\mathrm{Pic}^0(E)$ 上の $F^*$ の像を序数的 / 超特異の両方で決定し、「レベル $n$ でちょうど止まる対象」が存在するか、その不変量が $\mathbb{Z}/p^n$ 的か確認。$\mathbb{G}_m$ と違い $\mathrm{Pic}$ が非自明なので、同型類のレベルで情報が残るはず。
4. 3 の結果を踏まえ、一般の $(X,D)$・一般の $G$ への定式化を行う。**証明の骨格は「$\mathrm{Bun}(X^{(n+1)})$ がアーベル圏でないため $\underline{\mathrm{Aut}}^\otimes(\omega_x)$ が再構成に失敗する」という圏論的事実**であり、これは既に §5.1 で確認済み。あとは「失敗する」を定量化する例を添える。
5. log Atiyah 類による障害の記述（§6.2-2）を、上記が済んでから整備する。

### フェーズ 3：完備性パートの論文化

6. **命題 4.2（§3.4）と定理 D（§3.3）は既に証明済みなので、この部分は独立した短い論文として先行させられる。** 主張：「char $p$ の完備な平坦放物型幾何では、被覆変換の固定部分群が $p$-正則であり、したがって log 構造は仮定ではなく帰結である」。DL 多様体の例（§3.6）を添えれば自己完結する。
7. §3.7 の逆（完備例の分類が $X(w_0)$ 型に限ることの証明）を試みる。

### フェーズ 4：developing map と逆問題

8. (dS) の確認結果に応じて定理 B（§4.1）を定式化・証明。
9. §4.2 の境界における $\mathbb{Z}_p$-冪写像を、Kindler の局所指数論と厳密に接続する。これが主定理候補 (b) の核。
10. §3.5 の数値的障害を精査し（文献確認 #5）、Hirzebruch 比例性の再現を正式な命題にする。

### 保留

- §4.5（半アーベル）は確度が低いため、フェーズ 1–3 が済むまで着手しない。文献確認 #7 の結果次第で、独立したプロジェクトに分離することも検討。

---

## 付録：主張の地位一覧（早見表）

| 主張 | 地位 | 依存 |
|---|---|---|
| 定理 A 順方向（Tannaka による $\rho$ の構成） | **確立** | なし（形式的） |
| 定理 A 逆方向（$(\rho,s) \mapsto \mathcal{P}$） | 条件付き | (dS) |
| $\rho$ は $\pi_1^{\mathrm{tame}}$ の表現でない（§3.2） | 条件付き確立 | (K) |
| 定理 D（完備性の 4 条件の同値） | 条件付き確立 | (K) |
| 命題 4.2（固定部分群が $p$-正則） | **確立（完全証明）** | なし |
| 系：完備性 ⟹ tame ⟹ log | **確立** | 命題 4.2 |
| Chern 類の数値的自明性 | **確立** | なし |
| 数値的障害の式・$c_1^2=3c_2$ の再現 | 条件付き確立 | 仮定 (H)、log 交叉理論の精査 |
| DL の例が定義 2.1 を満たすこと | 確立（要清書） | なし |
| $w \neq w_0$ は横断性を満たさない | **確立** | なし |
| 定理 B（developing map の存在・形式的エタール性） | **推測** | (dS) |
| 境界での $\mathbb{Z}_p$-冪写像 | **推測** | — |
| unipotent 局所モノドロミーの非存在 | **推測** | — |
| $\pi_1^{\mathrm{strat},rs}(\mathbb{G}_m^n) = D((\mathbb{Z}_p/\mathbb{Z})^n)$ | **推測** | — |
| 完備例の分類が $X(w_0)$ 型に限る | **推測** | — |
| 逆問題の十分条件 | **推測** | — |
| 半アーベルの場合 | **推測（最低確度）** | — |
| 「レベル $n$ ⟹ $\mathbb{Z}/p^{n+1}$」（$\mathbb{G}_m$ 上） | **誤り。§5.1 で訂正** | — |
