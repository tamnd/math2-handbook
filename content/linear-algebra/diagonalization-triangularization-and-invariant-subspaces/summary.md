## What to remember

Throughout, $T$ is a linear map on a vector space $V$ of finite dimension $n \ge 1$ over a field $F$, with characteristic polynomial $p_T$ and minimal polynomial $m_T$.

- **Invariant subspaces cut a map in two.** If $T(U) \subseteq U$, the [restriction and quotient operators](/0KN7EPH7Z0/) are defined, the matrix of $T$ in a basis that starts with a basis of $U$ is block upper triangular, and $p_T = p_{T|_U} \, p_{\bar T}$. See [invariant subspace](/0ACX5QT8TE/).
- **Diagonalizable means a basis of eigenvectors.** $T$ is [diagonalizable](/07SQCNV233/) over $F$ if and only if $V$ has a basis of eigenvectors of $T$ ([this theorem](/056SW1E0AC/)); the eigenvectors are then the columns of $P$ in $A = P D P^{-1}$, in the order of the eigenvalues in $D$.
- **Three tests, one only sufficient.** If $T$ has $n$ distinct eigenvalues in $F$, it is diagonalizable ([sufficient only](/0Y95Z7MT02/)). Exactly: $p_T$ splits over $F$ and $\dim \ker(T - \lambda) = m_\lambda$ for every eigenvalue ([multiplicities](/CDB8KCNNG9/)). Also exactly: $m_T$ is a product of distinct linear factors over $F$ ([minimal polynomial](/0MPAJRB23T/)). A [defective matrix](/5F2AV5855Y/) fails the multiplicity test for some eigenvalue.
- **Diagonal forms make powers cheap.** From $A = P D P^{-1}$ comes $f(A) = P f(D) P^{-1}$ for every polynomial $f$, and $A^k = P D^k P^{-1}$ ([powers](/0TNR9BQ871/), [eigendecomposition](/D0AP2R7272/)). A family of diagonalizable maps has one common eigenbasis if and only if its members commute ([simultaneous diagonalization](/0FK17N4DKA/)).
- **Triangular needs only splitting.** $T$ has an upper triangular matrix in some basis if and only if $p_T$ splits over $F$; the diagonal then lists the eigenvalues with algebraic multiplicity ([triangularization](/0363JMQ42Y/)). Commuting maps whose characteristic polynomials split are triangular in one common basis ([simultaneous triangularization](/42PG67Q5YN/)).
- **Coprime polynomials split kernels.** If $\gcd(p, q) = 1$, then $\ker (pq)(T) = \ker p(T) \oplus \ker q(T)$ in any dimension, with projections that are polynomials in $T$ ([kernels lemma](/ACBNK1VFVG/)). Over any field, $m_T = p_1^{e_1} \cdots p_k^{e_k}$ with distinct monic irreducible $p_i$ gives $V = \bigoplus_i \ker p_i(T)^{e_i}$ ([primary decomposition](/49ZHBMYKVE/)).
- **Generalized eigenspaces have the right size.** $V_\lambda = \ker (T - \lambda)^n$ contains the eigenspace and has dimension equal to the algebraic multiplicity ([generalized eigenspace](/0AJ035ZTZE/)). If $p_T$ splits over $F$, then $V = \bigoplus_\lambda V_\lambda$ and $T - \lambda$ is nilpotent on $V_\lambda$ ([decomposition](/0Z3GDY89T5/)).
- **Every split map is diagonalizable plus nilpotent.** If $p_T$ splits over $F$, there is exactly one pair with $T = S + N$, $S$ diagonalizable, $N$ [nilpotent](/063D5Z2C70/) and $S N = N S$, and both are polynomials in $T$ ([Jordan-Chevalley](/011K11VPJN/)). Without splitting, $T$ is [semisimple](/08VRX3Q4PB/) when $m_T$ is a product of distinct monic irreducibles; the semisimple-plus-nilpotent split then needs a perfect field.
- **Fitting needs nothing.** Over any field, $V = \ker T^n \oplus \operatorname{im} T^n$, with $T$ nilpotent on the first piece and invertible on the second ([Fitting decomposition](/77SACA9CVQ/)).

## Four properties side by side

| Property of $T$ | Condition on $m_T$ | Example over $\R$ | Non-example over $\R$ |
|---|---|---|---|
| [Diagonalizable](/07SQCNV233/) over $F$ | splits over $F$, simple roots | a projection, $m = t^2 - t$ | the shear, $m = (t - 1)^2$ |
| [Triangularizable](/0363JMQ42Y/) over $F$ | splits over $F$ | the shear | the rotation by a right angle, $m = t^2 + 1$ |
| [Semisimple](/08VRX3Q4PB/) | distinct monic irreducible factors | the rotation by a right angle | the shear |
| [Nilpotent](/063D5Z2C70/) | $t^k$ with $k \le n$ | the derivative on polynomials of degree at most $3$ | a nonzero projection |

: Four properties of an endomorphism of a finite-dimensional space. The shear sends $e_1$ to $e_1$ and $e_2$ to $e_1 + e_2$. Since $m_T$ and $p_T$ have the same irreducible factors, $m_T$ splits exactly when $p_T$ does.

## Common errors

- **Counting eigenvalues with multiplicity.** $n$ eigenvalues counted with multiplicity only says that $p_T$ splits. The shear has eigenvalues $1, 1$ and is not diagonalizable.
- **Fearing repeated eigenvalues.** A repeated eigenvalue does not prevent diagonalization: the identity is diagonal. Only a shortfall of eigenvectors does.
- **Ignoring the field.** The rotation by a right angle is diagonalizable over $\C$ and not over $\R$. Diagonalizable and triangularizable always mean over a stated field.
- **Dropping the power in $V_\lambda$.** The generalized eigenspace is $\ker (T - \lambda)^n$, not $\ker (T - \lambda)$; the exponent $n$, or the algebraic multiplicity, always suffices.
- **Taking the diagonal of $A$ as $S$.** The diagonalizable part of the Jordan-Chevalley decomposition is a polynomial in $A$, and it is usually not the diagonal part of $A$, even when $A$ is upper triangular.
- **Adding maps that do not commute.** Sums of diagonalizable maps, or of nilpotent maps, keep the property only when the maps commute.
