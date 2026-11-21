## What to remember

- **Linear forms.** A linear form on $V$ is a linear map $V \to F$. Every form on $F^n$ is $x \mapsto c_1 x_1 + \cdots + c_n x_n$ for a unique row $(c_1, \ldots, c_n)$. A nonzero form is surjective, its kernel is a hyperplane, and if $\ker f \subseteq \ker g$ with $f \ne 0$, then $g = cf$ for some scalar $c$.
- **Dual basis.** For a basis $b_1, \ldots, b_n$ of $V$, the forms $b_i^*$ with $b_i^*(b_j) = \delta_{ij}$ are a basis of $V^*$. They read off coordinates, $v = \sum_i b_i^*(v)\, b_i$, and every form is $f = \sum_i f(b_i)\, b_i^*$. In $F^n$, if the $b_j$ are the columns of $P$, the $b_i^*$ are the rows of $P^{-1}$.
- **Dimension.** $\dim V^* = \dim V$ for finite-dimensional $V$, but the isomorphism $b_i \mapsto b_i^*$ depends on the basis. For infinite-dimensional $V$, $\dim V^* = \abs{F}^{\dim V} > \dim V$ (Erdős–Kaplansky).
- **Double dual.** The evaluation map $\operatorname{ev} \colon V \to V^{**}$, $\operatorname{ev}(v)(\varphi) = \varphi(v)$, is linear and injective for every $V$, and it is an isomorphism exactly when $V$ is finite-dimensional.
- **Annihilators.** $U^0 = \set{\varphi \in V^* : \varphi(U) = 0}$. Larger subspaces have smaller annihilators, $(U + W)^0 = U^0 \cap W^0$, and in finite dimension $(U \cap W)^0 = U^0 + W^0$ and $\dim U + \dim U^0 = \dim V$. Also $U^0 \cong (V/U)^*$ and $V^*/U^0 \cong U^*$.
- **Dual map.** $f^*(\varphi) = \varphi \circ f$ defines $f^* \colon W^* \to V^*$, with $(g \circ f)^* = f^* \circ g^*$ and $\operatorname{id}^* = \operatorname{id}$. In dual bases, $[f^*]_{B^*,C^*} = ([f]_{C,B})^\top$.
- **Kernel and image.** $\ker f^* = (\operatorname{im} f)^0$ and $\operatorname{im} f^* = (\ker f)^0$. So $f$ is surjective exactly when $f^*$ is injective, $f$ is injective exactly when $f^*$ is surjective, and in finite dimension $\operatorname{rank} f^* = \operatorname{rank} f$, which is row rank equals column rank.

## Finite and infinite dimension

| Statement | $\dim V < \infty$ | $\dim V = \infty$ |
|---|---|---|
| The dual basis is a basis of $V^*$ | yes | no: it spans only the forms that vanish on all but finitely many $b_i$ |
| $V^* \cong V$ | yes, through a basis | no: $\dim V^* > \dim V$ |
| $\operatorname{ev} \colon V \to V^{**}$ is injective | yes | yes |
| $\operatorname{ev} \colon V \to V^{**}$ is surjective | yes | no |
| Every form on a subspace $U$ extends to $V$ | yes | yes, using a complement of $U$ |

: How duality behaves in finite and infinite dimension. The injectivity of evaluation and the extension of forms hold in general; the other statements need finite dimension.

## Common errors

- **Thinking that $b_i^*$ depends only on $b_i$.** The form $b_1^*$ depends on the whole basis. In $\R^2$ the basis $(1, 0), (0, 1)$ gives $b_1^* = x$, while $(1, 0), (1, 1)$ gives $b_1^* = x - y$, with the same first vector.
- **Using the wrong side of the transpose.** If the basis vectors are the columns of $P$, the dual basis consists of the rows of $P^{-1}$, not the rows of $P$ or of $P^\top$. Coordinates of forms change by $(P^{-1})^\top$ when coordinates of vectors change by $P^{-1}$.
- **Identifying the annihilator with the orthogonal complement.** $U^0$ lies in $V^*$, and it needs no inner product. It corresponds to the [orthogonal complement](/0XJXTBCB2T/) only after an inner product identifies $V$ with $V^*$.
- **Letting $f^*$ run in the same direction as $f$.** A map $V \to W$ gives a map $W^* \to V^*$, and the order of a composition reverses.
- **Extending finite-dimensional facts.** For $V$ of countable dimension, the coordinate forms $e_n^*$ do not span $V^*$, and $V \to V^{**}$ is not onto. Arguments that count dimensions work only in finite dimension.
