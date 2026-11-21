## What to remember

- **Definition.** The determinant is the unique function $\det \colon M_n(K) \to K$ that is multilinear and alternating in the columns and has $\det I = 1$. Written out, it is the [Leibniz formula](/016PE4VZ8Q/) $\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a_{\sigma(1)1} \cdots a_{\sigma(n)n}$, with $n!$ terms.
- **Row operations.** A swap of two rows changes the sign, multiplying a row by $c$ multiplies the determinant by $c$, and adding a multiple of one row to another changes nothing. A [triangular matrix](/0K1KKMFHYH/) has the product of its diagonal entries as determinant, and $\det A^{\mathsf{T}} = \det A$.
- **Products.** $\det(AB) = \det A \det B$, and $\det(A^{-1}) = (\det A)^{-1}$. Similar matrices have the same determinant, but equal determinants do not make matrices similar.
- **Invertibility.** Over a field, $A$ is invertible if and only if $\det A \ne 0$. Over a commutative ring, $A$ is invertible if and only if $\det A$ is a unit; an integer matrix has an integer inverse exactly when $\det A = \pm 1$.
- **Cofactors.** The cofactor $C_{ij} = (-1)^{i+j} M_{ij}$ is a signed minor. [Laplace expansion](/0C08BQ3M05/) along row $i$ gives $\det A = \sum_j a_{ij} C_{ij}$. The adjugate is the transpose of the cofactor matrix, and $A \operatorname{adj} A = \operatorname{adj} A \cdot A = \det A \cdot I$. So $A^{-1} = \operatorname{adj} A / \det A$, and [Cramer's rule](/0977KZ6PQB/) gives $x_i = \det A_i / \det A$, where $A_i$ has column $i$ replaced by $b$.
- **Blocks.** For square diagonal blocks, $\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \det D$. If $A$ is invertible, $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \det(D - CA^{-1}B)$. In general it is not $\det A \det D - \det B \det C$.
- **Identities.** [Vandermonde](/0P84B554AS/): $\det(x_i^{j-1}) = \prod_{i < j}(x_j - x_i)$. [Cauchy-Binet](/08WE2W7DYS/): for $A$ of size $m \times n$ and $B$ of size $n \times m$, $\det(AB)$ is the sum over $m$-subsets $S$ of $\set{1, \dots, n}$ of $\det A_{:,S} \det B_{S,:}$, and it is $0$ when $m > n$. [Weinstein-Aronszajn](/0G24VQ1088/): $\det(I_m + AB) = \det(I_n + BA)$. Rank one update: $\det(A + uv^{\mathsf{T}}) = (1 + v^{\mathsf{T}} A^{-1} u) \det A$.
- **Geometry.** For a linear map $A$ of $\R^n$ and a measurable set $S$, $\operatorname{vol}(A(S)) = \abs{\det A} \operatorname{vol}(S)$. The sign of $\det A$ says whether $A$ keeps orientation. The determinant of an endomorphism is the determinant of its matrix in any one basis, used for both source and target.
- **Rank.** The rank of a matrix is the largest size of a nonzero minor.

## Ways to compute a determinant

| Method | Work for size $n$ | Fits |
|---|---|---|
| $ad - bc$, [Sarrus](/7H2P40X0MV/) | fixed | $n = 2$ and $n = 3$ only |
| Leibniz formula or full Laplace expansion | about $n!$ products | theory, and very small $n$ |
| Laplace along one row or column | $n$ determinants of size $n - 1$ | rows or columns with many zeros, symbolic entries |
| Row reduction to triangular form | about $\tfrac{2}{3} n^3$ operations over a field | numerical and general work |
| Block rules and the Schur complement | two smaller determinants | matrices with a zero block or an invertible block |
| [Dodgson condensation](/RQ44FKS5QM/) | $n - 1$ steps of $2 \times 2$ minors | integer matrices by hand, when no interior divisor is $0$ |

: Methods to compute $\det A$. For $n \ge 4$, every row of the table except the first is a valid method.

## Common errors

- **Extending Sarrus to size $4$.** The diagonal picture lists only $8$ of the $24$ terms of a $4 \times 4$ determinant, some with the wrong sign.
- **Treating the determinant as additive.** In general $\det(A + B) \ne \det A + \det B$; already $\det(I + I) = 2^n$.
- **Forgetting the power in $\det(cA) = c^n \det A$.** Scaling one row scales by $c$; scaling the whole matrix scales by $c^n$.
- **Dropping the signs or the transpose.** Cofactors carry $(-1)^{i+j}$, and the adjugate is the transpose of the cofactor matrix. Without either, $A \operatorname{adj} A$ is not $\det A \cdot I$.
- **Applying the $2 \times 2$ formula to blocks.** The formula $\det A \det D - \det B \det C$ for a block matrix is wrong in general. It holds in the form $\det(AD - BC)$ when $C$ and $D$ commute.
- **Using a nonzero determinant over a ring.** Over $\Z$ or $\Z/m$, a nonzero determinant is not enough for an inverse in the same ring; the determinant must be a unit.
