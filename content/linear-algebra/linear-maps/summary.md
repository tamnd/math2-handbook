## What to remember

- **Linear map:** $T \colon V \to W$ with $T(u + v) = T(u) + T(v)$ and $T(av) = a\,T(v)$. Then $T(0) = 0$ and $T$ preserves all linear combinations. Composites of linear maps are linear, and the inverse of a bijective linear map is linear.
- **Matrix transformations:** every linear map $T \colon F^n \to F^m$ is $x \mapsto Ax$ for exactly one $m \times n$ matrix $A$, whose $j$-th column is $T(e_j)$. The matrix of $T \circ S$ is the product of the matrices of $T$ and $S$, in that order.
- **Kernel and image:** $\ker T = \set{v : T(v) = 0}$ is a subspace of $V$, and $\operatorname{im} T$ is a subspace of $W$, spanned by the images of any spanning set of $V$. $T$ is injective if and only if $\ker T = \set{0}$.
- **Bases determine maps:** given a basis $(b_i)$ of $V$ and any vectors $(w_i)$ in $W$, there is exactly one linear map with $T(b_i) = w_i$.
- **Rank-nullity:** for $V$ finite-dimensional, $\dim \operatorname{im} T + \dim \ker T = \dim V$. For an $m \times n$ matrix, the rank plus the number of free variables of $Ax = 0$ is $n$.
- **Isomorphism:** finite-dimensional spaces over $F$ are isomorphic if and only if they have the same dimension; a basis of $V$ gives an isomorphism $F^n \to V$. An endomorphism of a finite-dimensional space is injective if and only if it is surjective. The shifts on sequences show that this fails in infinite dimension.
- **Spaces of maps:** $\operatorname{Hom}(V, W)$ is a vector space under pointwise operations, of dimension $\dim V \cdot \dim W$. The endomorphisms $\operatorname{End}(V)$ form an algebra under composition, isomorphic to $M_n(F)$ when $\dim V = n$, and not commutative for $n \ge 2$.
- **Semilinear maps:** $T$ is $\sigma$-semilinear for an automorphism $\sigma$ of the field when $T$ is additive and $T(\lambda v) = \sigma(\lambda)\,T(v)$. Over $\C$ with complex conjugation these are the antilinear maps.

## Injective, surjective, bijective

| $T \colon V \to W$ is | Kernel and image | Rank | Possible only if | For $T(x) = Ax$ |
|---|---|---|---|---|
| injective | $\ker T = \set{0}$ | $\operatorname{rank} T = n$ | $n \le m$ | a pivot in every column |
| surjective | $\operatorname{im} T = W$ | $\operatorname{rank} T = m$ | $n \ge m$ | a pivot in every row |
| bijective | both | $\operatorname{rank} T = n = m$ | $n = m$ | $A$ square and invertible |

: The three properties of a linear map $T \colon V \to W$ with $\dim V = n$ and $\dim W = m$ finite, and of the map $x \mapsto Ax$ of an $m \times n$ matrix. When $n = m$, the three rows are the same condition.

## Common errors

- **Taking "$T(0) = 0$" as enough.** It is necessary but not sufficient: $(x, y) \mapsto (x^2, y)$ sends $0$ to $0$ and is not linear. Check additivity and homogeneity, or write $T$ as $x \mapsto Ax$.
- **Putting the images in rows.** The standard matrix of $T$ has $T(e_j)$ as its $j$-th column, not its $j$-th row.
- **Reversing the order of a composite.** $T \circ S$ applies $S$ first, and its matrix is $AB$ when $T$ has matrix $A$ and $S$ has matrix $B$.
- **Applying rank-nullity to the codomain.** The sum $\operatorname{rank} T + \operatorname{nullity} T$ is the dimension of the domain $V$, not of $W$.
- **Reading the rank off the shape.** A $3 \times 5$ matrix has nullity at least $2$, but not necessarily exactly $2$; the rank comes from row reduction.
- **Using "injective implies surjective" for maps between different spaces or in infinite dimension.** The equivalence is for endomorphisms of a finite-dimensional space, or for maps between spaces of the same finite dimension.
