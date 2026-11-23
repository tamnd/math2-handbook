## What to remember

- **[Linear forms and hyperplanes](/XR0EQN0H8T/):** a linear form is a linear map $f \colon V \to F$. If $f \ne 0$, then $\ker f$ is a hyperplane and $V = \ker f \oplus Fv$ for every $v$ with $f(v) \ne 0$; every hyperplane is such a kernel, and $\ker f \subseteq \ker g$ with $f \ne 0$ gives $g = cf$ for exactly one $c \in F$. In dimension $n \ge 1$ the hyperplanes are the subspaces of dimension $n - 1$.
- **[Dual basis](/0ZD2CF6ZS0/):** for a basis $b_1, \dots, b_n$ of $V$, the coordinate forms $b_i^*$ with $b_i^*(b_j) = 1$ for $i = j$ and $0$ otherwise form a [basis of $V^*$](/00889YD15K/), and every form is $f = \sum_i f(b_i)\, b_i^*$. So $\dim V^* = \dim V$ in finite dimension. The form $b_i^*$ depends on the whole basis, not on $b_i$ alone.
- **Infinite dimension:** if $V$ has an infinite basis $B$, the coordinate forms span only the forms that vanish on all but finitely many $b \in B$, and the [Erdős-Kaplansky theorem](/S5ET1HG2ZX/) gives $\dim V^* = \abs{F}^{\dim V} > \dim V$.
- **[Double dual](/0ZJM9D7NPS/):** the evaluation map $V \to V^{**}$, $v \mapsto (f \mapsto f(v))$, is linear and injective for every $V$, and it is an isomorphism exactly when $V$ is finite-dimensional. It uses no basis.
- **[Annihilator](/0ASHNYF7AG/):** $U^0 = \set{f \in V^* : f(u) = 0 \text{ for all } u \in U}$. Taking annihilators reverses inclusions, $(U + W)^0 = U^0 \cap W^0$, and [in every dimension](/06Q1EFVH0Q/) $U^0 \cong (V/U)^*$ and $V^*/U^0 \cong U^*$. If $V$ is finite-dimensional, $\dim U + \dim U^0 = \dim V$.
- **[Dual map](/0AZ5ARP287/):** a linear map $f \colon V \to W$ gives $f^* \colon W^* \to V^*$, $f^*(\varphi) = \varphi \circ f$. It reverses composition, $(g \circ f)^* = f^* \circ g^*$, and in dual bases its [matrix is the transpose](/0ZPB3180AY/) of the matrix of $f$.
- **[Kernel and image of the dual map](/7FA499AW3T/):** $\ker f^* = (\operatorname{im} f)^0$ and $\operatorname{im} f^* = (\ker f)^0$. So $f$ is onto exactly when $f^*$ is injective, and in finite dimension $\operatorname{rank} f^* = \operatorname{rank} f$, which is row rank equals column rank.

| | Finite dimension $n$ | Infinite dimension |
|---|---|---|
| $\dim V^*$ | $n$ | $\abs{F}^{\dim V}$, larger than $\dim V$ |
| Coordinate forms of a basis | a basis of $V^*$ | independent, but do not span $V^*$ |
| Evaluation $V \to V^{**}$ | isomorphism | injective, not onto |
| $\dim U + \dim U^0$ | $n$ | no such count; $U^0 \cong (V/U)^*$ still holds |
| $V \cong V^*$ | yes, by a choice of basis | never |

: What duality gives in finite and in infinite dimension.

## Common errors

- **Taking $b_i^*$ to depend on $b_i$ only.** Change one other basis vector and $b_i^*$ can change. In $\R^n$ the dual basis is the rows of $P^{-1}$, where $P$ has the basis vectors as columns, not the rows of $P^{\mathsf{T}}$.
- **Confusing the annihilator with the orthogonal complement.** $U^0$ lives in $V^*$ and needs no inner product; the orthogonal complement $U^\perp$ lives in $V$. They correspond only after identifying $V$ with $V^*$ through an inner product.
- **Getting the direction of the dual map wrong.** $f \colon V \to W$ gives $f^* \colon W^* \to V^*$, and $(g \circ f)^* = f^* \circ g^*$, in the reverse order.
- **Confusing the dual map with the adjoint.** The adjoint of an inner product space map is a map $W \to V$; the dual map acts on forms. Over $\R$ the transpose is the matrix of the dual map in dual bases of any basis, but the matrix of the adjoint only in orthonormal bases; over $\C$ the adjoint also conjugates.
- **Carrying finite-dimensional facts to infinite dimension.** A space with a countable basis has a dual of uncountable dimension, and the coordinate forms are not a basis of it.
