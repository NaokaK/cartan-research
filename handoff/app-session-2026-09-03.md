# 引き継ぎ文書：2026-09-03 デスクトップアプリ・セッションの記録

**作成日**: 2026-09-03
**作成環境**: Claude Code（デスクトップアプリ版）、モデル Opus 5
**引き継ぎ先**: ターミナル版 Claude Code
**対象リポジトリ**: `/Users/naoka/Desktop/研究/cartan-research`

---

## 0. この文書について

### 0.1 位置づけ

この文書は、`handoff/` にある他の3つの資料とは**性格が異なる**。

- `handoff/logarithmic-chat.md`, `zp-chat.md`, `level-chat.md`
  … 過去の研究セッションの引き継ぎ資料。**原本として凍結されている。変更禁止。**
- `handoff/app-session-2026-09-03.md`（この文書）
  … 上記3資料を**受け取った側**のセッション記録。整理・検証・骨組み作成の作業ログ。

この文書だけを読めば現在地を再構成できるように書いてある。ただし数学の中身そのものは
3つの原資料にあるので、実際の研究を進める際はそちらを読むこと。

### 0.2 タグの語彙

本文書では次を厳密に区別する。

- **VERIFIED** … 一次資料の本文を実際に参照して確認した。
- **PARTIALLY VERIFIED** … 一部は一次資料で確認したが、確認できていない部分が残る。
- **UNRESOLVED** … 確認できていない。
- **NEEDS LITERATURE CHECK** … 文献を見れば決まるが、今回見られなかったもの。
- **NEEDS DECISION** … 数学的には決着しており、選択の判断が残っているもの。
- **OBS-n** … 統合作業側（＝このセッション）の観察。資料の記述ではない。

### 0.3 証拠の出所についての重要な但し書き

**一次資料の引用は WebFetch 経由で得たものである。** WebFetch は取得したページを
小型モデルが要約・抽出して返す仕組みであり、私（このセッション）が論文の PDF を
直接目視したわけではない。したがって:

- 引用は「ar5iv の HTML から WebFetch が返した文字列」であり、
  原論文の紙面と一字一句同じであることは保証されない。
- 定理番号・式番号は返ってきたものをそのまま記録している。
- **次のセッションは、決定的に重要な箇所については原論文を自分で開いて確認すること。**

この但し書きは、CLAUDE.md の「文献主張が実際に検証されていないなら
NEEDS LITERATURE CHECK と印を付けよ」という規則に従うためのものである。

### 0.4 このセッションで守ったルール（次のセッションも守ること）

- `handoff/` の3つの原資料は変更しない。
- 既存の研究メモ（`notes/*.tex`, `notes/daily/`, `main.tex`, `CLAUDE.md` 等）は変更しない。
- 旧原稿（`研究/log-level-opers.tex`, `研究/zp-residues.tex`）は変更しない。
- 資料間・ファイル間で食い違いがある場合、**どちらかを正しいものとして採用しない**。
- handoff の記述を、その handoff 自身の主張の証拠として循環的に使わない。
- git commit はしていない。

---

## 1. このセッションで行ったこと（時系列）

1. リポジトリの構成と `CLAUDE.md` を確認。既存の `notes/*.tex` は
   見出しのみで内容が空であることを確認。
2. `~/Downloads` にあった3つの引き継ぎ資料を `handoff/` に保存
   （バイト単位で一致することを `diff` で確認）。付属の原稿・スクリプトも併せて保存。
3. 3資料を突き合わせ、13項目（共通の土台、テーマ固有の内容、依存関係、
   記法の不一致、矛盾、既知の結果、証明済みの結果、未証明の主張、proof gap、
   文献確認事項、未解決問題）にわたる分析を行った。
4. `notes/topics/` 以下のフォルダ構成を提案し、骨組み30ファイルを作成
   （内容は用途を説明するコメントと空の見出しのみ）。
5. `notes/topics/00-common/conventions.tex` に、規約の差異の列挙を記入。
6. **その conventions.tex に書いた観察 OBS-1〜OBS-5 を、一次資料に当たって検証した。**
   これが本セッションの中心的な成果であり、以下 §3〜§6 に記す。

---

## 2. リポジトリの現状

```
/Users/naoka/Desktop/研究/
├── log-level-opers.tex          ← 旧版。§8.1 参照。変更していない
├── zp-residues.tex              ← v1。§8.2 参照。変更していない
├── 修論/                         ← 過去の成果物。smf_ast_432.pdf,
│                                   Mochizuki の PDF などの一次資料あり
└── cartan-research/             ← git リポジトリ（branch: main）
    ├── CLAUDE.md                ← 研究アシスタントの運用ルール。必読
    ├── main.tex, preamble.tex, references.bib
    ├── notes/
    │   ├── overview.tex, definitions.tex, results.tex,
    │   │   examples.tex, questions.tex   ← すべて見出しのみ、内容は空
    │   ├── daily/2026-09-03.tex          ← 見出しのみ、内容は空
    │   └── topics/                       ← 本セッションで新規作成（§7）
    ├── handoff/                          ← 本セッションで新規作成
    │   ├── logarithmic-chat.md           ← 原本・凍結
    │   ├── zp-chat.md                    ← 原本・凍結
    │   ├── level-chat.md                 ← 原本・凍結
    │   ├── zp-residues-v2.tex            ← zp の現行原稿
    │   ├── log-level-opers.tex           ← level の新版原稿
    │   ├── verify_p5.py
    │   └── app-session-2026-09-03.md     ← この文書
    ├── drafts/, figures/, computations/, papers/   ← 空
```

**git の状態**: `main` ブランチ、origin と同期済み。
追跡済みファイルへの変更は**ゼロ**（`git diff` が空）。
`handoff/` と `notes/topics/` が未追跡（`??`）として存在するのみ。
**コミットしていない。**

---

## 3. 今回確認した数学的事項

### 3.1 参照できた一次資料

| 資料 | 取得方法 | 結果 |
|---|---|---|
| Wakabayashi, arXiv:2201.11266 "Differential modules and dormant opers of higher level" | ar5iv HTML | **本文を参照できた**（§1, §2.1, §3.2–3.3, §4.2–4.3, Thm C） |
| Wakabayashi, arXiv:2209.08528 | ar5iv HTML | **§3 までしか取得できず。§10 は未取得** |
| Berthelot, ASENS **29** (1996), "D-modules arithmétiques I" | Numdam | **本文未取得**。PDF が WebFetch のサイズ上限（10MB）超過 |
| Ohkawa, arXiv:1410.0535 "On log local Cartier transform of higher level" | ar5iv HTML | 参照できた（log 版の定義と Frobenius 降下） |

### 3.2 Wakabayashi arXiv:2201.11266 から確認できた記述

以下は WebFetch が返した引用（§0.3 の但し書きが適用される）。

**Definition 1.2.1, 式 (11)** — $m$-derivation の定義:
> $\partial_{\langle\bullet\rangle} := \{\partial_{\langle j\rangle}\}_{0\le j\le p^m}$

生成元の範囲は **$0\le j\le p^m$**。「$j<p^{m+1}$」ではない。この違いは重要（§5.3）。

**式 (46)** — 作用素の作用:
> $\partial_{\langle j\rangle}(t^n) := q_j!\cdot\binom{n}{j}\cdot t^{n-j}$、ここで $q_j=\lfloor j/p^m\rfloor$

**式 (8)** — 修正二項係数。[PBer1, §1.1.2]（＝Berthelot I）を引用。

**Definition 2.1.3, 式 (55)** — $p^{m+1}$-曲率:
> $\psi^p_{(E,\nabla)} := \nabla_{\langle p^{m+1}\rangle}$、
> "We shall say that $(E,\nabla)$ is dormant if $\psi^p_{(E,\nabla)}=0$"

**Proposition 2.1.5(i)**:
> "The functors $\Xi^{\downarrow(l)}$ and $\Xi^{\uparrow(l)}$ define an equivalence of
> categories $\mathfrak{Mod}(\mathcal{D}_S^{(m)})\xrightarrow{\sim}\mathfrak{Mod}(\mathcal{D}_{S^{(l)}}^{(m-l)})$"

$\Xi^{\uparrow(l)}$ がレベルを上げ、$\Xi^{\downarrow(l)}$ が下げる。

**Proposition 2.1.5(ii)**: $F^{(l)*}(E)$ の $p^{m+1}$-曲率が $E$ の $p^{m-l+1}$-曲率に対応。

**Corollary 2.1.6**:
> "functors $\Xi^{\downarrow(m+1)}$ and $\Xi^{\uparrow(m+1)}$ induce an equivalence of
> categories (dormant $\mathcal{D}_S^{(m)}$-modules) $\to$ ($S^{(m+1)}$-modules)"

**§4.2** — これが C-2 の決め手:
> "A $\mathrm{GL}_n$-oper of level $N$ on $\mathcal{X}$ is, roughly speaking, a rank $n$
> vector bundle on $X$ equipped with both a $\mathcal{D}_X^{(N-1)}$-action and
> complete flag structure"

**Definition 3.3.1**（exponent）: 値域は $\mathbb{Z}/p^{m+1}\mathbb{Z}$。
**Definition 4.3.2**（radius）: 値域は $\mathfrak{S}_n\backslash(\mathbb{Z}/p^N\mathbb{Z})^{\times n}/\Delta$。
**Theorem C**: $\Upsilon_{\mathscr{P}}:\mathrm{Cov}^{\mathrm{tame}}_{\mathscr{P}}\xrightarrow{\sim}{}^N\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}$。

### 3.3 Ohkawa arXiv:1410.0535 から確認できた記述

- log 版レベル $m$ の作用素環:
  $\mathcal{D}^{(m)}_{X/S,n}:=\mathcal{H}om_{\mathcal{O}_X}(\mathcal{P}^n_{X/S,(m)},\mathcal{O}_X)$、
  $\mathcal{D}^{(m)}_{X/S}:=\bigcup_n\mathcal{D}^{(m)}_{X/S,n}$
- $p^{m+1}$-曲率写像:
  $\beta: S^\bullet\mathcal{T}_{X'/S}\to\mathcal{D}^{(m)}_{X/S}$ が $\xi'_i\mapsto\partial_{\langle p^{m+1}\varepsilon_i\rangle}$
- log Frobenius 降下: $X^{(m)}$ 上のレベル 0 加群と $X$ 上のレベル $m$ 加群の同値

**注意**: Ohkawa の log 版の定義は (B) 型（PD envelope の双対）であり、
logarithmic 資料が採る (L) 型（$\mathcal{E}nd$ による定義）**ではない**。

---

## 4. C-1〜C-5 の判定

`notes/topics/00-common/conventions.tex` に登録した NEEDS CHECK のうち、
C-1〜C-4（＋ C-5 として δ の件）を検証した結果。

### C-1: Berthelot の $\mathcal{D}^{(m)}$ と $p^{m+1}$-曲率 / Frobenius 降下

**PARTIALLY VERIFIED**

確認できたこと（すべて Wakabayashi 2201.11266 経由）:
- レベル $m$ ↔ $p^{m+1}$-曲率（Def 2.1.3）
- $l$ 回ひねるとレベルが $l$ 下がる（Prop 2.1.5(i)）
- **dormant なレベル $m$ ⟺ $S^{(m+1)}$-加群、すなわち $m+1$ 回の Frobenius 降下**（Cor 2.1.6）

確認できていないこと:
- **Berthelot の原論文における $\mathcal{D}^{(m)}$ の定義そのもの**
- **$\partial^{[j]}\in\mathcal{D}^{(m)}$ となる $j$ の範囲**（「$j<p^{m+1}$」か？）

$\partial^{[j]}(t^n)=\binom{n}{j}t^{n-j}$ と式 (46) を比べると
$\partial_{\langle j\rangle}=q_j!\,\partial^{[j]}$ が従うが、**この形の式は論文中に明示されていない**
（私の導出であり、資料の記述ではない）。

### C-2: (W)「レベル $N$」= Berthelot の $\mathcal{D}^{(N-1)}$ か

**VERIFIED**

§3.2 に引用した **2201.11266 §4.2** が明示している。独立の裏付けが2つ:
1. Def 3.3.1（exponent, mod $p^{m+1}$）と Def 4.3.2（radius, mod $p^N$）が
   同じ対象を記述しており、$N=m+1$ を強制する。
2. Cor 2.1.6 より dormant レベル $m$ は $m+1$ 回降下 ⟹「dormant レベル $N$」は $N$ 回降下。

**留保**: 確認したのは *oper* の「レベル $N$」である。
level 資料が「レベル」を使う全箇所がこの意味かは未検証（下記 C-10）。

### C-3: zp の $\mathcal{D}_U^{(n)}$ はどの規約か

**PARTIALLY VERIFIED**

zp の定義には2つの読み筋がある。

- **(i) 降下回数による読み**: zp は「$E\cong F^{n*}E_n$ が $E$ を $\mathcal{D}^{(n)}$-加群にする」
  と述べる。$n$ 回降下 ↔ 添字 $n$。(W) のレベル $N$ と**添字が一致する**。
- **(ii) 位数の上界による読み**: zp は「位数 $<p^n$ の作用素が生成する」と定義する。
  これを Berthelot の添字に翻訳する橋（下記 C-1b / C-3a）が**未検証**。

**決定的な留保 —— notation の一致と convention の一致は別物**:

(B)/(W) では「$\mathcal{D}^{(m)}$-加群であること」は「降下すること」を**意味しない**。
降下には dormant（$p^{m+1}$-曲率 $=0$）という**追加条件**が要る（Cor 2.1.6 が
"dormant $\mathcal{D}_S^{(m)}$-modules" と明記している）。

一方 zp は「$\mathcal{D}^{(n)}$-加群 ⟺ $n$ 回降下」となるように環を導入している。
すなわち zp の環の加群には dormant 条件が組み込まれている。

したがって:
- 添字の対応: (Z) の $n$ = (W) のレベル $N$ = 降下回数 —— 成立
- 環の同一性: (Z) の $\mathcal{D}^{(n)}$ は Berthelot の $\mathcal{D}^{(n-1)}$ と**同じ環ではない**

### C-4: logarithmic の $\mathcal{D}^{(m)}_{(X,D)}$ の対応

**PARTIALLY VERIFIED**

(L) の定義は $\mathcal{D}^{(m)}_{(X,D)}:=\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)$。

**添字**は (L) 自身の記述で決まる。(L) は「$\mathcal{D}^{(n)}$-加群では
Frobenius 降下 $\mathcal{E}\cong F^{(n+1)*}\mathcal{E}_{n+1}$ しか得られない」と述べる。
すなわち **(L) の添字 $n$ ↔ $n+1$ 回降下**。これは (B) と同じ数え方。

**環の構成**は (B) ではなく (Z) と同型。$\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)$ 上の
$\mathcal{O}_X$-局所自由加群は Morita により $\mathcal{O}_{X^{(m+1)}}$-加群と対応する。
つまり「$m+1$ 回降下する」ことを定義に組み込んだ環であり、(Z) と同じ流儀。

**最も鋭い結論**:
> **(L) の $\mathcal{D}^{(n)}$ と (Z) の $\mathcal{D}^{(n+1)}$ は、同じ環を 1 ずれた添字で
> 呼んでいる**（いずれも $\mathcal{E}nd_{\mathcal{O}_{X^{(n+1)}}}(\mathcal{O}_X)$）。

**未確認**: (L) の「log divided power 版」という但し書き。上の Morita 対応の
**対数版**は確認していない。Ohkawa の log 版は (B) 型の定義であり (L) 型ではない。

### C-5: $\delta^{(m)}\in\mathcal{D}^{(m+1)}$ は何を数えているか

**VERIFIED —— 内部矛盾ではない**

$\delta^{(m)}:=D_{p^m}=t^{p^m}\partial_t^{[p^m]}$ の**位数は $p^m$**。
(Z) の環定義「$\mathcal{D}^{(n)}$ = 位数 $<p^n$」に代入すると:
- $p^m<p^{m+1}$ ⟹ $\delta^{(m)}\in\mathcal{D}^{(m+1)}$
- $p^m\not<p^m$ ⟹ $\delta^{(m)}\notin\mathcal{D}^{(m)}$

すなわち旧稿 `研究/zp-residues.tex` の記述は (Z) 自身の環定義から直ちに従う。

**答え**: $\delta^{(m)}$ の上付き $m$ が数えているのは
**作用素自身のラベル（分割冪の指数、位数 $=p^m$）**である。
環のレベルでも Frobenius 降下の回数でもない。

ただし、zp 内部で「レベル」という語が3つの異なる量に使われている事実は残る
（作用素のラベル $m$ / 環の添字 $n$ / 格子の添字 $n$）。
これは不整合ではなく多義性である。

---

## 5. レベル規約について判明したこと

### 5.1 4つの規約

| 記号 | 出典 | 使用箇所 |
|---|---|---|
| **(B)** Berthelot | $\mathcal{D}^{(m)}$、$p^{m+1}$-曲率 | 基準として |
| **(W)** Wakabayashi | レベル $N$ $=\mathcal{D}^{(N-1)}$、$p^N$-曲率 | `level-chat.md`（採用を明記）、`log-level-opers.tex` 新旧両版の付録 |
| **(Z)** zp | $\mathcal{D}_U^{(n)}$ = 位数 $<p^n$ | `zp-chat.md`、`zp-residues-v2.tex`、`研究/zp-residues.tex` |
| **(L)** logarithmic | $\mathcal{D}^{(m)}_{(X,D)}:=\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)$ | `logarithmic-chat.md` |

（第5の候補 (U)「当初のユーザ規約」は `level-chat.md` §2.1 が言及して不採用としたもの。
`conventions.tex` に候補として列挙してある。）

### 5.2 対応表 —— 共通の軸は「Frobenius 降下の回数 $d$」

$d$ が、4規約に共通して意味の定まる唯一の量である。

| | 環の実体 | 「加群」の意味 | 曲率の呼称 | $d$ との関係 |
|---|---|---|---|---|
| **(B)** | Berthelot の $\mathcal{D}^{(m)}$ | 降下を**含意しない** | $p^{m+1}$-曲率 | dormant のとき $d=m+1$ |
| **(W)** | Berthelot の $\mathcal{D}^{(N-1)}$ | 降下を**含意しない** | $p^N$-曲率 | dormant のとき $d=N$ |
| **(Z)** | $\mathcal{E}nd_{\mathcal{O}_{X^{(n)}}}(\mathcal{O}_X)$ と同型か（**未検証**） | 降下を**含意する** | （使わない） | $d=n$ |
| **(L)** | $\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)$（定義） | 降下を**含意する** | $p$-曲率 0 が $m=0$ | $d=m+1$ |

### 5.3 二つの軸は直交している —— 本セッション最大の結論

**軸 1（添字）**: 降下回数 $d$ を固定すると

$$\text{(W) レベル }N=\text{(Z) 添字 }n=d,\qquad
  \text{(B) 添字 }m=\text{(L) 添字 }m=d-1$$

すなわち **(W) と (Z) が同じ添字、(B) と (L) が同じ添字**。両群の差は 1。

**軸 2（環）**:

$$\text{(Z) の }\mathcal{D}^{(n)}=\text{(L) の }\mathcal{D}^{(n-1)}
  =\mathcal{E}nd_{\mathcal{O}_{X^{(n)}}}(\mathcal{O}_X)\quad(\text{C-3a, C-4a 確認待ち})$$

$$\text{(B)/(W) の環はこれとは異なる（全射があると思われるが未検証）}$$

> **次のセッションへの警告**:
> 「(Z) と (L) は 1 ずれているだけ」と見て一方を他方に機械的に書き換えると、
> **環が入れ替わり、dormant 条件が黙って出入りする**。
> CLAUDE.md の「仮定を黙って強めたり弱めたりしない」に直接抵触する。

もう一点、混同しやすい対:
- Wakabayashi Def 1.2.1 の生成元の範囲は **$0\le j\le p^m$**（$\langle\ \rangle$ 正規化）
- 「位数 $<p^{m+1}$」（$[\ ]$ 正規化での所属）

**この二つは別の主張である。** $p^m$ と $p^{m+1}-1$ を混同しないこと。

### 5.4 OBS-1〜OBS-5 の帰結

| | 内容 | 判定 |
|---|---|---|
| OBS-1 | (Z) の $\mathcal{D}^{(n)}$ は (B) の $\mathcal{D}^{(m)}$ と $n=m+1$ で対応 | **要修正**。降下回数の対応としては成立。環の同一視と読むと**誤り** |
| OBS-2 | (Z) は (W) と一致 | **PARTIALLY VERIFIED**。添字は一致、環は一致しない |
| OBS-3 | (L) は (B) と一致 | **PARTIALLY VERIFIED**。添字は一致、環は一致しない |
| OBS-4 | zp と level は同じ規約、logarithmic だけ 1 ずれ | **VERIFIED（添字について）**。logarithmic の添字は zp/level より 1 小さい |
| OBS-5 | zp 内部で添字が 1 ずれる（不整合の疑い） | **懸念は解消**。ずれは (Z) の定義からの帰結 |

---

## 6. 文献確認できた事項

- **(W) の「レベル $N$」= $\mathcal{D}^{(N-1)}$** —— 2201.11266 §4.2 で確認。**VERIFIED**
- **dormant レベル $m$ ⟺ $m+1$ 回降下** —— 2201.11266 Cor 2.1.6 で確認
- **レベル $m$ ↔ $p^{m+1}$-曲率** —— 2201.11266 Def 2.1.3 で確認
- **$l$ 回ひねるとレベルが $l$ 下がる** —— 2201.11266 Prop 2.1.5(i) で確認
- **exponent は mod $p^{m+1}$、radius は mod $p^N$** —— Def 3.3.1, Def 4.3.2 で確認
- **Theorem C の形** —— 確認（$\Upsilon_{\mathscr{P}}$ の存在と終域が ${}^N\mathcal{O}p^{\mathrm{Zzz}}_{2,\mathscr{P}}$）
- **log 版レベル $m$ の環と $p^{m+1}$-曲率写像** —— Ohkawa 1410.0535 で確認

これらは `level-chat.md` §2.1 の対照表および §2.3 の記述と**独立に整合した**。
すなわち level 資料のレベル規約に関する記述は、一次資料で裏付けられた。

---

## 7. `conventions.tex` について行った作業

`notes/topics/00-common/conventions.tex` に以下を記入した（1,006 → 26,864 バイト）。
**内容はコメント（`%%`）と空の見出しのみで、数学的主張は書いていない。**

構成:
1. この文書の位置づけ（原則 P1–P4、印の定義）
2. レベル規約の候補 5 つ（(B)(W)(Z)(L)(U)）と出典
3. 各規約の使用箇所の対応表
4. 「レベル」という語の多義性（zp 内部の3つの意味）
5. 主要記号 $\mathscr{P}$, $\rho$, $r$, $N$ の詳細（各テーマでの意味・出典・深刻度）
6. その他の記号の衝突（$\sigma/\Sigma$, $n$, $D$, $G$ の定義体, $E$, $\theta$, $\mathbb{G}/\mathcal{G}$）
7. 共通に採用できる定義・記法
8. まだ統一できないもの（9項目）
9. 統一すると主張の意味が変わりうるもの（S1–S6、根拠つき）
10. NEEDS DECISION（D-1〜D-6）と NEEDS CHECK（C-1〜C-14）の一覧

**このファイルはまだ §4 の検証結果を反映していない。** 反映作業は未実施。
次のセッションが最初に行うべき作業の候補（§10 参照）。

---

## 8. 資料間・ファイル間の食い違い（未決着）

**どちらかを正しいものとして採用していない。** 台帳は
`notes/topics/90-crosscutting/discrepancies.tex`（骨組みのみ、内容未記入）。

### 8.1 `log-level-opers.tex` の2つの版で主要結論が正反対

`研究/log-level-opers.tex`（旧、9/3 12:06）と
`handoff/log-level-opers.tex`（新、handoff 資料が参照する版）。

| 箇所 | 旧版 | 新版 |
|---|---|---|
| 概要 (3) | 「反例は $D=\emptyset$ に**集中し**、$\mathrm{Pic}$ の $p$ 可除性が障害」 | 「$\mathrm{PGL}_2$-oper については $(g,r)$ によらず**反例は存在しない**。障害は行列式束に局在」 |
| $N=2$ の個数 | $p=5$: **610**、$p=7$: **2262** | $p=5$: **225**、$p=7$: **1666**、$p=3$: 11 |
| ${}^\dagger C_N$ | **存在しない** | 定義 `def:Cdagger`、補題 `lem:nesting` を含む |
| 未解決問題 `q:main` | 「本命: $r=0$ の反例を構成せよ」 | 「旧・本命問題: **解決済み（否定的）**」 |

`level-chat.md` §5.4 と付録B は、旧版の 610 / 2262 について
「計算機で確認と称して提示したが実際には計算していなかった」と自己申告している。
**この自己申告自体は独立検証されていない。**

**なお付録の「規約の対照表」は旧版と新版で完全に一致する**（diff で確認）。
規約に関する記述は版の食い違いの影響を受けていない。

### 8.2 `zp-residues.tex`（v1）と handoff の改訂履歴の記述が一致しない

`zp-chat.md` §9 は「v1 は §5.1, §5.5 の誤りを含む」とするが、実ファイルは:

| handoff が言う誤り | ディスク上の実態 |
|---|---|
| §5.1 桁ごとの加法性 | **既に修正済み**。`thm:functoriality` は「sums taken in $\mathbb{Z}_p$」と正しく述べ、繰り上がりの remark もある。$D_a$ の全族も導入済み |
| §5.5 定理 B の捻れ指数を桁で書いた | **誤りが残存**。`thm:boundary` は $N_i^{\otimes(-\dig_n(c))}$ と書いている |

**ディスク上の「v1」は handoff が記述する v1 そのものではなく、中間改訂版と思われる。**

マーカーの数: v1 は `\GAP` 1個 / `\CHECK` 1個 / `\TODO` 6個。
v2 は `\GAP` **0個** / `\CHECK` 3個 / `\TODO` 5個。
（`zp-chat.md` §9 は `\CHECK` について4項目を挙げているが実ファイルは3個。軽微な不一致。）

### 8.3 【新規発見】arXiv:2209.08528 の題名が一致しない

ar5iv が返した題名:
> "Canonical diagonal liftings I: dormant $\mathrm{PGL}_n$-opers on algebraic curves"

`log-level-opers.tex` の参考文献 [Wak2]:
> "Arithmetic liftings and 2d TQFT for dormant opers of higher level"

**同一の arXiv 番号に対して題名が異なる。** 改題の可能性も引用誤りの可能性もある。
**どちらとも判定していない。** 既知の Osserman の巻号問題と同種の書誌情報の問題。

### 8.4 欠落しているファイル

`level-chat.md` 付録Aが挙げる **`check.py`**（${}^\dagger C_N$ の直接列挙、
入れ子性の検証）が手元にない。§3.4 の数値表と「ステップ2-4」の再現に必要。

### 8.5 LaTeX エンジンの問題

`preamble.tex` に日本語組版の設定がない（geometry, amsmath, amssymb, amsthm,
mathtools, mathrsfs, hyperref のみ）。`main.tex` は article クラス。
`notes/topics/` 以下は日本語見出しで作ったため**現状ではコンパイルできない**。
`main.tex` がまだ `notes/topics/` を `\input` していないので実害はない。

---

## 9. NEEDS LITERATURE CHECK 一覧

### 最優先

| # | 事項 | 依存する主張 | 状態 |
|---|---|---|---|
| **C-1a** | Berthelot ASENS 1996 §1.1–1.2 の $\mathcal{D}_X^{(m)}$ の定義そのもの | (B) の基準そのもの、C-3, C-4 | Numdam の PDF が WebFetch の 10MB 上限超過。ローカル DL が要る |
| **C-1b** | $\partial^{[j]}\in\mathcal{D}^{(m)}$ となる $j$ の範囲（$j<p^{m+1}$ か） | (Z) の「位数 $<p^n$」を (B) に翻訳する橋 | 未確認 |
| **C-3a** | $\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)$ と「位数 $<p^{m+1}$ の作用素の環」の関係 | (Z)/(L) の環の実体、軸 2 全体 | WebSearch の要約中に「$\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)\simeq\mathcal{D}^{(m+s)}_{X,p^{m+1}-1}$」という記述を見たが**出典を特定できていない**。確認中に Web ツールが利用不可になった |
| **C-4a** | 上記 Morita 対応の**対数版** | (L) の定義の正当性 | 未確認。Montagnon の thesis / Ohkawa |
| **L2** | Wakabayashi 2209.08528 §10.3（Prop. 10.3.3）の径数付けとレベル降下の両立性 | level の主要主張（反例の非存在）が [部分証明] に留まる原因 | **ar5iv で §3 までしか取得できず未取得**。level 資料が最優先とする項目 |

### 3資料から引き継いだもの（未着手）

| # | 事項 | 依存 |
|---|---|---|
| L1 | **Kindler**「Regular singular stratified bundles and tame ramification」: (a) 最大 pro-有限商が $\pi_1^{\mathrm{tame}}$ か、(b) exponent の理論が zp の定理 A を既に含むか、(c) regular singular の定義の同値性 | **3テーマすべての土台**。logarithmic §3.2/§3.3、zp の新規性、統合可能性そのもの |
| L3 | **dos Santos**: 普遍 torsor $\widetilde U^{rs}$ の存在、位相、アフィン pro-スキーム性 | logarithmic 定理 B 全体、定理 A の逆方向 |
| L4 | **Christol–Mebkhout** の $p$ 進 exponent 理論 | zp の位置づけを大きく変えうる |
| — | Wakabayashi 2201.11266 §6.4 | level §2.5 の辞書（続編から再構成したもの） |
| — | 2209.08528 §10.4（$p=5$ の具体例）、§10.6（Ehrhart 擬多項式）、§9.2（Thm. D） | level §3.5 の突合せ、§6.2、§6.1 |
| — | Ogus–Vologodsky log 版 / Ohkawa / Lorenzon / Schepler | logarithmic §5.1 と level §4.1（root stack 予想の独自性判定）の**両方** |
| — | Esnault–Kindler「Lefschetz theorems for tamely ramified coverings」 | tame Gieseker 予想 |
| — | Esnault–Mehta / Biswas–dos Santos | Chern 類の数値的自明性 |
| — | Mochizuki Chap. II, Prop. 1.4, 1.5 | level §3.1 の [要検証]。**`修論/` に PDF あり** |
| — | Katz「Rigid Local Systems」（$\infty$ での符号規約） | zp §9 の移送元 |
| — | Deligne–Lusztig / Teitelbaum / Orlik–Rapoport、Dickson 不変式 | logarithmic §3.6 |
| — | Dettweiler–Reiter、Dwork、Katz–Oda | zp §4.1, §4.2, P1/P2 |

### 書誌情報の修正

- **Osserman の巻号が不正確**（`log-level-opers.tex` [9]、`\Todo{正確な巻号を確認}` が残存）
- **arXiv:2209.08528 の題名の不一致**（§8.3）
- Liu–Osserman Thm. 2.1、Wakabayashi Astérisque **432**（**`修論/smf_ast_432.pdf` が手元にある**）

---

## 10. 未解決の判断事項（NEEDS DECISION）

`conventions.tex` に登録済み。

| # | 内容 |
|---|---|
| **D-1** | レベル規約を統一するか、テーマごとに保持して変換表のみ持つか。**§5.3 の軸 2（環が違う）を踏まえると、機械的統一は危険**。変換表方式が安全と思われるが未決 |
| D-2 | 符号規約。zp §9 は「変更するなら (7.2) 留数定理・(8.5) Hecke 指数・(9.4) 指数規則の三箇所を同時に直せ」と警告 |
| D-3 | 主要記号 $\mathscr{P}$, $\rho$, $r$, $N$ の改名の要否 |
| D-4 | $G$ の定義体（logarithmic は $k$ 上、zp は $\mathbb{F}_p$ 上、level は未確認） |
| D-5 | `notes/topics/` の記述言語と LaTeX エンジン（§8.5） |
| D-6 | 「レベル」という語を横断的に使うか、テーマ内に閉じるか |

---

## 11. 現在の主要な未解決問題（3テーマ横断）

前セッションの分析で立てた優先順位。§4 の検証結果を踏まえても変更していない。

1. **L1（Kindler）** —— 3テーマすべての土台に触れ、zp の定理 A の新規性を左右する。
   統合の前提でもある（regular singular の定義が一致しなければ3資料は同じ土俵に乗らない）
2. **L2 + level の穴 G1** —— level の主要主張が [部分証明] から [定理] に昇格するかの単一の分岐点。
   作業量は小さいのに影響が大きい
3. **zp P1: $\mathrm{MC}_c$ は正則特異性を保つか** —— zp §9 全体がこれに依存
4. **zp P4 / (8.1) 座標独立性の清書** —— 定理 B の唯一の要清書箇所。zp 資料自身が「所要:小」と見積もる
5. **logarithmic §6.2-1（楕円曲線上の階数 1）** —— logarithmic が「最重要」「試金石」とする問題。
   **level §3.2 が骨格を提供している可能性がある**（下記 §12 の接点 (b)）
6. **L3（dos Santos）** —— 使えない場合 logarithmic §4.1 の定式化を根本から変更する必要
7. level: 一般 smooth 曲線での $\mathrm{res}_N$ 全射性（level 資料の [最優先]）
8. zp §4.7 / P6: 捻れ付き帰納法の枠組み設計（zp が「構造的な主要課題」とする）
9. **logarithmic の完備性パートの独立論文化** —— 命題 4.2 と定理 D は証明済みで、
   DL の例を添えれば自己完結する。**3資料の中で最も早く成果物になりうる部分**
10. L4（Christol–Mebkhout）

---

## 12. 次に調べるべきこと

### 12.1 規約の検証を完結させる（本セッションの続き）

1. **C-1a**: Berthelot ASENS 1996 をローカルに取得して §1.1–1.2 を読む。
   Numdam の PDF: `https://www.numdam.org/item/10.24033/asens.1739.pdf`
   （WebFetch の 10MB 上限を超えるため、ダウンロードが要る。
   本セッションではユーザの指示がなかったためダウンロードしていない。）
2. **C-3a**: 「$\mathcal{E}nd_{\mathcal{O}_{X^{(m+1)}}}(\mathcal{O}_X)\simeq$ 位数 $<p^{m+1}$ の作用素の環」
   の出典を特定する。候補として WebSearch が返したもの:
   - arXiv:2401.07082「Bernstein-Sato theory modulo $p^m$」
   - arXiv:2308.03720「Witt Differential Operators」
   - Publ. RIMS Kyoto Univ. **46** (2010), 1–35（`https://ems.press/content/serial-article-files/41095`）
   - Springer「Some Elements on Berthelot's Arithmetic $\mathscr{D}$-Modules」
3. **C-4a**: 上記の対数版（Montagnon / Ohkawa）。
4. **L2**: arXiv:2209.08528 §10。**ar5iv では本文全体が返らないため別経路が必要。**
   `level-chat.md` §5.7 も「arXiv PDF を web_fetch すると §4.3 付近で切断される」と記録している。
   ローカル DL が最も確実と思われる。

### 12.2 検証結果を `conventions.tex` に反映する

§4〜§5 の内容を、`OBS-n` を確定した記述に置き換える形で反映する。特に:
- OBS-1 を「降下回数の対応であって環の同一視ではない」と修正
- 軸 1 / 軸 2 の分離を明記
- C-2 を VERIFIED として、出典（2201.11266 §4.2）を明記
- C-5 を解消済みとして記録（多義性は残ると明記）
- C-1a, C-1b, C-3a, C-4a を NEEDS LITERATURE CHECK として残す
- §8.3 の書誌問題を `literature-status.tex` にも登録

### 12.3 テーマ横断の接点（前セッションの分析で見つけたもの）

**(a) 局所半単純性の三者照合** —— 同一の現象が3テーマで異なる地位を持つ:
- level §3.1: $p$-曲率 0 ⟹ $R_i^p=R_i$ —— **[定理]**、レベル 0（有限）
- zp (5.6) / 定理 A: 局所モノドロミーは常に半単純、局所 $\mathrm{Ext}^1=0$ —— **[証明済]**、全レベル
- logarithmic §4.3: unipotent 局所モノドロミーは存在しない —— **[推測]**

zp の定理 A が logarithmic の推測を証明している可能性が高いが、
**両者の regular singular の定義の同値性（L1(c)）が未確認なので、
無条件に「解決済み」と扱ってはいけない。** 仮定の密輸入の典型的な経路。
台帳: `notes/topics/90-crosscutting/semisimplicity.tex`（骨組みのみ）

**(b) logarithmic §6.2-1 と level §3.2 の接続** —— logarithmic の「最重要」問題
「$X$ が楕円曲線の場合に $\mathrm{Pic}^0$ 上の $F^*$ の像を計算せよ」に対し、
level §3.2 の [定理] が骨格を持っている（次数をとって $\sum j_i\equiv\deg\mathcal{L}\pmod{p^N}$、
$r\ge1$ なら解ける、残りは $\mathrm{Pic}^0$ の $p$ 可除性）。
さらに level §3.6 の系が「$r\ge1$ なら障害は消え、$r=0$ なら $\mathrm{Pic}(X)/p^N$ が障害」とする。
**統合による最大の即効的利得の候補。** ただし規約の照合が前提。

**(c) logarithmic §7 の文献確認 #10「①の反例」** —— logarithmic は
「本文書は①の内容を『$F$ でちょうど $n$ 回割れる束』型と仮定して書かれている。要確認。
想定文献: 前段の議論記録」としている。level 資料の `ex:exactN`
（「ちょうどレベル $N$」、$\mathrm{Pic}$ の非 $p$ 可除性が障害）がまさにこの型。
**logarithmic の未確認事項 #10 は level 資料で解消できる可能性がある。**
（これは推定であり、両資料は互いを参照していない。）

**(d) その他の接点**: $\mathbb{Z}_p/\mathbb{Z}$ の三者整合、Hecke 変形／格子の取り替えの
符号照合、exponent / radius / $r$-スペクトラムの同一視（有限レベルと無限レベル）。
台帳: `90-crosscutting/zp-invariants.tex`, `lattices-and-hecke.tex`（いずれも骨組みのみ）

**(e) 見かけの緊張（矛盾ではない）**:
logarithmic は「log は完備性から**強制される帰結**」、
level は「log（marked point）は障害を**消す方向**に働く」。
log 構造が果たす二つの異なる役割であり矛盾ではないが、素朴に統合すると矛盾に見える。

---

## 13. このセッションで作成・変更したファイル

### 新規作成（37件）

**`handoff/`（7件）**
```
handoff/logarithmic-chat.md        ← ~/Downloads/HANDOFF.md を完全一致でコピー
handoff/zp-chat.md                 ← ~/Downloads/HANDOFF2.md を完全一致でコピー
handoff/level-chat.md              ← ~/Downloads/HANDOVER3.md を完全一致でコピー
handoff/zp-residues-v2.tex         ← 付属原稿
handoff/log-level-opers.tex        ← 付属原稿（新版）
handoff/verify_p5.py               ← 付属スクリプト
handoff/app-session-2026-09-03.md  ← この文書
```
上3件はいずれも `diff` でバイト単位の一致を確認済み。

**`notes/topics/`（30件）**
```
notes/topics/README.md
notes/topics/00-common/{conventions,status-tags,foundations,literature-status}.tex
notes/topics/10-logarithmic/{overview,definitions,results,conditional,questions,failed}.tex
notes/topics/20-zp-residues/{overview,definitions,results,to-polish,
                             middle-convolution,questions,failed}.tex
notes/topics/30-level/{overview,definitions,results,partial,computations,questions,failed}.tex
notes/topics/90-crosscutting/{semisimplicity,zp-invariants,lattices-and-hecke,
                              open-problems,discrepancies}.tex
```

`conventions.tex` **以外の29件は骨組みのみ**（用途を説明する `%%` コメントと
空の `\section` / `\subsection` 見出しだけ。数学的主張は書いていない）。

### 内容を記入したファイル（1件）

```
notes/topics/00-common/conventions.tex    1,006 → 26,864 バイト
```
内容は §7 参照。**§4 の検証結果はまだ反映していない。**

### 変更していないファイル

- `notes/overview.tex`, `definitions.tex`, `results.tex`, `examples.tex`, `questions.tex`
- `notes/daily/2026-09-03.tex`
- `main.tex`, `preamble.tex`, `references.bib`, `CLAUDE.md`, `README.md`
- `研究/log-level-opers.tex`（旧版）、`研究/zp-residues.tex`（v1）
- `handoff/` の原資料3件および付属ファイル

### git の状態

```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
	handoff/
	notes/topics/

nothing added to commit but untracked files present
```

`git diff` は**空**（追跡済みファイルへの変更ゼロ）。
ステージングもコミットもしていない。

---

## 14. 次のセッションへの申し送り

### 守ってほしいこと

1. `handoff/logarithmic-chat.md`, `zp-chat.md`, `level-chat.md` は**原本。変更しない。**
2. `CLAUDE.md` の規則に従う。特に `results.tex` には確立した結果のみ。
3. **資料間・ファイル間の食い違いは、どちらかを正しいものとして採用しない**
   （§8）。台帳は `90-crosscutting/discrepancies.tex`。
4. **handoff の記述を、その handoff 自身の主張の証拠として使わない。**
5. 地位タグを勝手に昇格させない。特に §12.3(a) の半単純性。
6. 数値を「計算機で確認」と書くときは、**実際に実行してから書く**
   （`level-chat.md` 付録B に過去の事故が記録されている）。
7. **§5.3 の警告**: レベル規約を機械的に書き換えると dormant 条件が黙って出入りする。

### 最初に取りかかる候補

- **A**: §12.1 の規約検証の完結（C-1a, C-3a, C-4a）。Berthelot の PDF を
  ローカルに落とす必要がある。所要：小〜中。これが済むと `conventions.tex` を確定できる
- **B**: L2（Wakabayashi 2209.08528 §10）。**level の主要主張の昇格に直結する。**
  同じく PDF のローカル DL が要る。所要：小。**影響が最も大きい**
- **C**: L1（Kindler）。3テーマすべての土台。所要：中〜大
- **D**: §12.2（検証結果を `conventions.tex` に反映）。文献確認なしで着手可能。所要：小

**A と B は同じ作業（arXiv / Numdam の PDF をローカルに取得して読む）で片付く。**
ターミナル版なら PDF のダウンロードとテキスト抽出が容易なので、
まずここから入るのが効率的と思われる。
