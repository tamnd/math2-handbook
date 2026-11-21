## What to remember

- The **cyclic subspace** $Z(v; T)$ is spanned by $v, Tv, T^2 v, \dots$. If $m_v$ is the $T$-annihilator of $v$, then $v, Tv, \dots, T^{k-1} v$ with $k = \deg m_v$ is a basis of it, and the matrix of $T$ on it is the **companion matrix** $C(m_v)$. Both polynomials of $C(p)$ are $p$, and $T$ is cyclic if and only if $m_T = \chi_T$.
- **Cyclic decomposition:** $V = Z(v_1) \oplus \cdots \oplus Z(v_r)$ with annihilators $d_1 \mid d_2 \mid \cdots \mid d_r$. The **invariant factors** $d_i$ are unique, $d_r = m_T$ and $d_1 \cdots d_r = \chi_T$. The **elementary divisors** are the prime powers in the factorizations of the $d_i$, with repetitions.
- **Rational canonical form:** every $A \in M_n(F)$ is similar to exactly one $C(d_1) \oplus \cdots \oplus C(d_r)$ with $d_1 \mid \cdots \mid d_r$ monic and nonconstant. No hypothesis on $F$ is needed.
- **Characteristic matrix:** $A \sim B$ if and only if $xI - A$ and $xI - B$ are equivalent over $F[x]$. The Smith normal form of $xI - A$ is $\operatorname{diag}(1, \dots, 1, d_1, \dots, d_r)$, and its $k$-th entry is $D_k / D_{k-1}$, where $D_k$ is the monic gcd of the $k \times k$ minors.
- Invariant factors do not change under a field extension, so **matrices over $K$ that are similar over $L \supseteq K$ are similar over $K$**. Every matrix is **similar to its transpose**, by a symmetric matrix.
- **Nilpotent normal form:** a nilpotent $N$ is similar to $J_{k_1}(0) \oplus \cdots \oplus J_{k_s}(0)$ for a unique partition $k_1 \ge \cdots \ge k_s$ of $n$. The number of blocks of size at least $j$ is $\operatorname{rank} N^{j-1} - \operatorname{rank} N^j$.
- **Jordan normal form:** if $\chi_A$ splits over $F$, then $A$ is similar to a sum of Jordan blocks $J_k(\lambda)$, unique up to order. For each $\lambda$, with $r_j = \operatorname{rank}(A - \lambda I)^j$, the number of blocks $J_j(\lambda)$ is $r_{j-1} - 2r_j + r_{j+1}$. The number of blocks for $\lambda$ is its geometric multiplicity, their total size its algebraic multiplicity, and the largest size its multiplicity as a root of $m_A$.
- **Centralizer:** $\dim \set{X : XA = AX} = \sum_{i,j} \deg \gcd(d_i, d_j) \ge n$, with equality if and only if $A$ is cyclic, and then every matrix that commutes with $A$ is a polynomial in $A$.
- **Finite fields:** $GL_n(\mathbb{F}_q)$ has one conjugacy class for each rational canonical form with $d_r(0) \ne 0$. There are $q^2 - 1$ classes for $n = 2$ and $q^3 - q$ for $n = 3$.

## The normal forms side by side

| Form | Needs | Blocks | Read off from | Unique |
|---|---|---|---|---|
| [Rational canonical form](/042JWAR3Q0/) | any field | $C(d_i)$, with $d_1 \mid \cdots \mid d_r$ | invariant factors | yes |
| Elementary divisor form | any field | $C(p^e)$, $p$ irreducible | elementary divisors | up to order |
| [Jordan normal form](/085HQ5G5TE/) | $\chi_A$ splits | $J_k(\lambda)$ | $\dim \ker (A - \lambda I)^j$ | up to order |
| [Real Jordan form](/MPFT45RFGV/) | $F = \R$ | $J_k(\lambda)$ with $\lambda \in \R$, and $C_k(a, b)$ with $b > 0$ | complex Jordan form | up to order |
| [Weyr form](/9XEA4VR8WP/) | $\chi_A$ splits | basic Weyr matrices, one per eigenvalue | $\dim \ker (A - \lambda I)^j$ | up to order |

: Five normal forms under similarity. The Jordan and the Weyr forms carry the same data and differ by a permutation of the basis; the Weyr structure at $\lambda$ is the conjugate of the partition of Jordan block sizes.

## Common errors

- **Deciding similarity from $\chi_A$ and $m_A$.** For $n \le 3$ these two decide it, but $J_2(0) \oplus J_2(0)$ and $J_2(0) \oplus J_1(0) \oplus J_1(0)$ share both. Even with the rank added, the [two $7 \times 7$ matrices](/PQR08Q9529/) of the classification entry agree.
- **Taking any cyclic decomposition for the invariant factors.** $\operatorname{diag}(0, 1) = Z(e_1) \oplus Z(e_2)$ has annihilators $x$ and $x - 1$, but its single invariant factor is $x(x - 1)$. Only annihilators that divide each other are invariant factors.
- **Reading block sizes from $\dim \ker (A - \lambda I)^k$ directly.** The jumps $d_k - d_{k-1}$ count the blocks of size at least $k$, and the differences of the jumps count the blocks of size exactly $k$.
- **Starting a long Jordan chain at an arbitrary eigenvector.** Build chains from the top: choose $u$ of the right height, then take $Nu, N^2 u, \dots$. Check by $AP = PJ$.
- **Using the Jordan form where $\chi_A$ does not split.** Over $\Q$ or $\R$ a matrix may have no Jordan form. The rational canonical form always exists, and over $\R$ so does the real Jordan form.
