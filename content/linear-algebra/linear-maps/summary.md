## What to remember

- **[Linear map](/0NRYHJPQG2/):** for vector spaces $V$, $W$ over the same field $F$, a map $T \colon V \to W$ with $T(u + v) = T(u) + T(v)$ and $T(av) = a T(v)$. Then $T(0) = 0$ and $T$ preserves all linear combinations. [Examples](/0SS770NS8B/): differentiation, integration, shifts, the trace, the transpose.
- **[Matrices](/W6KB0J3SZZ/) and [composition](/00BKRZKMSS/):** every linear $T \colon F^n \to F^m$ is $x \mapsto Ax$ for one $m \times n$ matrix $A$, whose $j$-th column is $T(e_j)$. If $S$ has matrix $A$ and $T$ has matrix $B$, then $S \circ T$ ($T$ first) has matrix $AB$. Composition is associative and in general not commutative.
- **[Kernel](/0S23E6YE83/) and [image](/0WSFKKT6FF/):** $\ker T$ is a subspace of $V$, $\operatorname{im} T$ a subspace of $W$. [$T$ is injective exactly when $\ker T = \set{0}$](/0BJBYCGMWE/). The solutions of $T(v) = w$ are empty or of the form $v_0 + \ker T$.
- **[Bases determine maps](/0R8X9XA83A/):** if $(v_i)$ is a basis of $V$ and $(w_i)$ any family in $W$ with the same index set, exactly one linear $T$ has $T(v_i) = w_i$ for all $i$.
- **[Rank-nullity](/0W4FSW1TVB/):** if $V$ is finite-dimensional and $T \colon V \to W$ is linear, then $\dim V = \operatorname{rank} T + \dim \ker T$, where [$\operatorname{rank} T = \dim \operatorname{im} T$](/0ZZXSBTR4J/) and the [nullity](/0APCFW7639/) is $\dim \ker T$.
- **[Isomorphisms](/0B8T10CE7N/):** the inverse of a bijective linear map is linear. [Finite-dimensional spaces over $F$ are isomorphic exactly when they have the same dimension](/0VJBSK15SN/), and a basis of $n$ vectors gives $V \cong F^n$.
- **[Endomorphisms](/0912EEEVCT/):** if $V$ is finite-dimensional and $T \colon V \to V$ is linear, then $T$ is injective $\iff$ surjective $\iff$ bijective. In infinite dimension the shifts on sequences are counterexamples.
- **[$\operatorname{Hom}(V, W)$](/0X9MBPP2Z3/) and [$\operatorname{End}(V)$](/5JA4CYT1TB/):** the linear maps $V \to W$ form a vector space, [of dimension $\dim V \cdot \dim W$](/0Z9N1ER0W0/) when both are finite-dimensional. A basis of $V$ with $n$ vectors gives an isomorphism of algebras $\operatorname{End}(V) \cong M_n(F)$. For $n \ge 2$ this algebra is not commutative, has zero divisors, and its centre is the set of scalar maps.
- **[Semilinear maps](/BNPDDM95KF/):** for an automorphism $\sigma$ of $K$, a $\sigma$-semilinear map is additive with $T(av) = \sigma(a) T(v)$. Over $\C$ with $\sigma(a) = \bar a$ it is called antilinear. A composite of a $\sigma$-semilinear and a $\tau$-semilinear map is $\sigma\tau$-semilinear, so two antilinear maps compose to a linear one.

## Injective, surjective, bijective

| $T \colon V \to W$ | Kernel and image | Rank | Possible only if |
|---|---|---|---|
| injective | $\ker T = \set{0}$ | $\operatorname{rank} T = n$ | $n \le m$ |
| surjective | $\operatorname{im} T = W$ | $\operatorname{rank} T = m$ | $n \ge m$ |
| bijective | both | $\operatorname{rank} T = n = m$ | $n = m$ |

: Here $\dim V = n$ and $\dim W = m$ are finite. The last column is necessary only: a map between spaces of equal dimension can be neither injective nor surjective.

## Common errors

- **Checking only $T(0) = 0$.** Every linear map fixes $0$, but $(x, y) \mapsto (x, y^2)$ also does and is not linear. Check both rules.
- **Reversing a product.** The matrix of $S \circ T$ is (matrix of $S$)(matrix of $T$), since $T$ acts first. Composites $S \circ T$ and $T \circ S$ usually differ, and one of them may be defined when the other is not.
- **Composite for product.** In $\operatorname{End}(V)$ the product is composition, not the pointwise product of values, which is not even defined in most spaces.
- **Using the codomain in rank-nullity.** The theorem adds up to $\dim V$, the dimension of the domain. A map $\R^5 \to \R^3$ has nullity at least $2$, not at least $0$.
- **Forgetting finite dimension.** "Injective implies surjective" needs $T \colon V \to V$ with $V$ finite-dimensional. The right shift on sequences is injective and not surjective.
- **Prescribing values on the wrong set.** Values can be chosen freely on a basis. On a dependent spanning set they must respect the relations, and on a set that does not span they do not determine the map.
- **Calling an antilinear map linear.** Complex conjugation on $\C^n$ is additive and $\R$-linear, but $\overline{iz} = -i \bar z$, so it is not $\C$-linear.
