#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
count_dagger_C.py
=================

目的
----
manuscripts/log-level-opers.tex の定義 \ref{def:Cdagger}（Wakabayashi,
arXiv:2209.08528, (10.6)）にある組合せ集合 ${}^{\dagger}C_N$ の位数を
数学的定義から直接、独立に計算する検証スクリプト。

これは handoff/level-chat.md 付録A が言及する（が handoff/ には
含まれていなかった）check.py とは別に、定義から書き起こした
独立実装である。回収した原 check.py は computations/check.py に置いてある。
両者の出力が一致することを確認するために本スクリプトを用意した。

数学的定義との対応
------------------
非負整数の三つ組 (s1,s2,s3) が ${}^{\dagger}C_N$ に属するとは：

  (a) s1+s2+s3 <= p^N - 2  かつ  |s2-s3| <= s1 <= s2+s3
      （3 つの三角不等式 s_i <= s_j + s_k と同値）

  (b) 任意の N' で 0 < N' < N なるものに対し、各 i について
        s_i' ∈ { [s_i]_{N'},  p^{N'} - 1 - [s_i]_{N'} }
      （[a]_{N'} := a mod p^{N'}）を適切に選んで
        s1'+s2'+s3' <= p^{N'} - 2  かつ  |s2'-s3'| <= s1' <= s2'+s3'
      とできる。

  in_dagger_C(s, N, p) が (a),(b) を厳密にそのまま判定する。

  条件 (a) から s_i <= p^N - 2 なので、探索範囲は {0,...,p^N-1}^3 で十分。
  count_dagger_C(N, p) はこの範囲を総当たりする。

入力
----
本文で使う (p, N) の組。CLI 引数なし。下の __main__ にハードコード：
  N=1 : p ∈ {3,5,7,11,13}
  N=2 : p ∈ {3,5,7,11,13}
  N=3 : p = 3
  入れ子性 ${}^{\dagger}C_N ⊆ {}^{\dagger}C_{N+1}$ : (p,N) ∈ {(3,1),(5,1),(3,2),(5,2)}
  p=5, N=1 の三つ組の全リスト（tab:p5 との突合せ用）

出力
----
標準出力に：
  * 各 (p,N) での #{}^{\dagger}C_N
  * N=1 と閉じた式 p(p^2-1)/24 の一致
  * N=1 と四角錐数 n(n+1)(2n+1)/6, n=(p-1)/2 の一致
  * 素朴な λ 定式化（条件 (b) を落としたもの）の数え上げ（rem:erratum 用）
  * 入れ子性の反例の有無
  * p=5, N=1 の (s1,s2,s3) 全リストと対応する (λ0,λ1,λ∞)=(2s+1)
"""

from itertools import product


def digit_reps(a, Nq, p):
    """条件 (b) で許される代表の集合 { [a]_{Nq},  p^{Nq}-1-[a]_{Nq} }。"""
    r = a % (p ** Nq)
    return {r, p ** Nq - 1 - r}


def triangle_ok(t):
    """|t2-t3| <= t1 <= t2+t3、すなわち 3 本の三角不等式。"""
    t1, t2, t3 = t
    return (t1 <= t2 + t3) and (t2 <= t1 + t3) and (t3 <= t1 + t2)


def cond_a(s, N, p):
    return sum(s) <= p ** N - 2 and triangle_ok(s)


def cond_b(s, N, p):
    for Nq in range(1, N):  # 0 < N' < N
        found = False
        reps = [sorted(digit_reps(s[i], Nq, p)) for i in range(3)]
        for t in product(*reps):
            if sum(t) <= p ** Nq - 2 and triangle_ok(t):
                found = True
                break
        if not found:
            return False
    return True


def in_dagger_C(s, N, p):
    return cond_a(s, N, p) and cond_b(s, N, p)


def count_dagger_C(N, p):
    M = p ** N
    return sum(1 for s in product(range(M), repeat=3) if in_dagger_C(s, N, p))


def list_dagger_C(N, p):
    M = p ** N
    return [s for s in product(range(M), repeat=3) if in_dagger_C(s, N, p)]


def count_naive_lambda(N, p):
    """rem:erratum：条件 (b) を落とした素朴な数え上げ。
    λ_i 奇数、0<λ_i<p^N、p∤λ_i、厳密三角不等式、Σλ_i < 2 p^N。"""
    M = p ** N
    lam = [l for l in range(1, M) if l % 2 == 1 and l % p != 0]
    c = 0
    for a, b, d in product(lam, repeat=3):
        if a + b + d < 2 * M and a < b + d and b < a + d and d < a + b:
            c += 1
    return c


def square_pyramidal(n):
    return n * (n + 1) * (2 * n + 1) // 6


if __name__ == "__main__":
    print("=== #{}^\\dagger C_N  (independent implementation from def:Cdagger) ===")
    print()
    print("N=1:")
    for p in [3, 5, 7, 11, 13]:
        c = count_dagger_C(1, p)
        closed = p * (p * p - 1) // 24
        n = (p - 1) // 2
        sq = square_pyramidal(n)
        print(f"  p={p:2d}: #C_1={c:6d}   p(p^2-1)/24={closed:6d}   "
              f"pyramidal n(n+1)(2n+1)/6 [n={n}]={sq:6d}   "
              f"{'OK' if c == closed == sq else 'MISMATCH'}")
    print()
    print("N=2:")
    for p in [3, 5, 7, 11, 13]:
        c = count_dagger_C(2, p)
        naive = count_naive_lambda(2, p)
        print(f"  p={p:2d}: #C_2={c:8d}   naive-lambda(no cond.(b))={naive:8d}")
    print()
    print("N=3:")
    for p in [3]:
        print(f"  p={p}: #C_3={count_dagger_C(3, p)}")
    print()
    print("=== nesting  C_N subset C_{N+1} ===")
    for (p, N) in [(3, 1), (5, 1), (3, 2), (5, 2)]:
        bad = [s for s in list_dagger_C(N, p) if not in_dagger_C(s, N + 1, p)]
        print(f"  p={p}, N={N}: elements of C_{N} not in C_{N+1}: "
              f"{len(bad)}  {bad if bad else ''}")
    print()
    print("=== p=5, N=1 : full list (for cross-check with tab:p5) ===")
    for s in list_dagger_C(1, 5):
        lam = tuple(2 * x + 1 for x in s)
        print(f"  (s1,s2,s3)={s}   (lambda0,lambda1,lambda_inf)={lam}")
