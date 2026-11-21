## What to remember

- A subspace $U$ is **invariant** under $T$ when $T(U) \subseteq U$. In a basis of $V$ that starts with a basis of $U$, the matrix of $T$ is $\begin{pmatrix} A & B \\ 0 & C \end{pmatrix}$, with $A$ the matrix of the restriction $T|_U$ and $C$ that of the quotient operator on $V/U$, and $p_T = p_{T|_U} \, p_{\bar T}$.
- $T$ is **diagonalizable** when $V$ has a basis of eigenvectors, equivalently $V = E_{\lambda_1} \oplus \cdots \oplus E_{\lambda_k}$, equivalently $\sum_i \dim E_{\lambda_i} = n$. For a matrix, $A = P D P^{-1}$ with the eigenvectors as the columns of $P$, in the same order as the eigenvalues in $D$.
- **Three tests.** $n$ distinct eigenvalues in $F$ suffice. Exactly: $p_T$ splits over $F$ and each geometric multiplicity equals the algebraic one. Also exactly: the minimal polynomial $m_T$ splits over $F$ with simple roots, or, what is the same, some product $(t - a_1) \cdots (t - a_r)$ of distinct linear factors kills $T$.
- If $A = P D P^{-1}$, then $f(A) = P f(D) P^{-1}$ for every polynomial $f$, and in particular $A^k = P D^k P^{-1}$. With $E_i = q_i r_i$, where $q_i$ is column $i$ of $P$ and $r_i$ row $i$ of $P^{-1}$, this reads $f(A) = \sum_i f(\lambda_i) E_i$.
- **Commuting families.** Diagonalizable maps have a common eigenbasis exactly when they commute. $T$ is **triangularizable** exactly when $p_T$ splits, and then the diagonal of any triangular form lists the eigenvalues with their algebraic multiplicities. Commuting maps with split characteristic polynomials are triangular in one common basis.
- **Kernels lemma.** If $\gcd(p, q) = 1$, then $\ker (pq)(T) = \ker p(T) \oplus \ker q(T)$, and the projections are polynomials in $T$. With $m_T = p_1^{e_1} \cdots p_k^{e_k}$, this gives the **primary decomposition** $V = \bigoplus_i \ker p_i(T)^{e_i}$, over any field.
- The **generalized eigenspace** $V_\lambda = \ker (T - \lambda)^n$ is invariant, contains $E_\lambda$, and has dimension equal to the algebraic multiplicity of $\lambda$. When $p_T$ splits, $V = \bigoplus_\lambda V_\lambda$, and $T - \lambda$ is nilpotent on $V_\lambda$.
- **Jordan-Chevalley.** When $p_T$ splits, there are unique $S$ diagonalizable and $N$ nilpotent with $T = S + N$ and $S N = N S$, and both are polynomials in $T$. $T$ is diagonalizable exactly when $N = 0$.
- **Fitting.** In dimension $n$, $V = \ker T^n \oplus \operatorname{im} T^n$, with $T$ nilpotent on the first summand and invertible on the second.

## The properties side by side

| Property of $T$ | In terms of $m_T$ | In terms of $p_T$ | Example | Non-example |
|---|---|---|---|---|
| [Diagonalizable](/07SQCNV233/) over $F$ | splits, simple roots | splits, and $\dim E_\lambda$ equals the algebraic multiplicity for each $\lambda$ | $I + J$, with $J$ the $3 \times 3$ matrix of ones | the shear |
| [Triangularizable](/0363JMQ42Y/) over $F$ | splits | splits | the shear | the rotation over $\R$ |
| [Semisimple](/08VRX3Q4PB/) | product of distinct monic irreducibles | when $p_T$ splits, the same as diagonalizable | the rotation over $\R$ | the shear |
| [Nilpotent](/063D5Z2C70/) | $t^k$ with $k \le n$ | $t^n$ | the derivative on cubic polynomials | a nonzero projection |

: Four properties of an endomorphism $T$ of an $n$-dimensional space over $F$. The shear is the matrix with rows $(1, 1)$ and $(0, 1)$, and the rotation is the matrix with rows $(0, -1)$ and $(1, 0)$. Since $m_T$ and $p_T$ have the same irreducible factors, $m_T$ splits exactly when $p_T$ does.

## Deciding whether a matrix is diagonalizable

1. Factor $p_A$. If it does not split over $F$, $A$ is not diagonalizable over $F$, though it may be over a larger field.
2. If the roots are distinct, $A$ is diagonalizable.
3. For each repeated eigenvalue $\lambda$, compare $n - \operatorname{rank}(A - \lambda I)$ with the multiplicity. One shortfall settles it.
4. A known polynomial with distinct roots in $F$ that kills $A$, such as $t^2 - t$ for a projection, replaces step 3.
5. To find $P$, put bases of the eigenspaces side by side as columns, and check $A P = P D$ rather than computing $P^{-1}$.

## Common errors

- **Counting eigenvalues with multiplicity.** Having $n$ eigenvalues counted with multiplicity only says that $p_A$ splits. The shear has the eigenvalues $1, 1$ and is not diagonalizable.
- **Fearing repeated eigenvalues.** The identity matrix is diagonal.
- **Using $\ker(T - \lambda)$ for the generalized eigenspace.** A power is needed: the exponent $n$ always works, and so does the algebraic multiplicity.
- **Forgetting commutation.** $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} = \operatorname{diag}(1, 2) + \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, but the two parts do not commute. This matrix is diagonalizable, so its Jordan-Chevalley decomposition has $N = 0$.
