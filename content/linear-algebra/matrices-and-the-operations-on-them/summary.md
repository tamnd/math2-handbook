## What to remember

- **Product.** For an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$ over a ring, $(AB)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk}$. Column $k$ of $AB$ is $A$ times column $k$ of $B$, and $Ax = x_1 a_1 + \dots + x_n a_n$ is a combination of the columns of $A$. The product is defined only when the inner sizes agree.
- **Laws.** Over any ring the product is [associative](/073E4XC016/) and distributes over addition. For $n \ge 2$ and $1 \ne 0$ it is [not commutative](/0P506SPZP2/), and $M_n(R)$ has zero divisors: $E_{12} \ne 0$ but $E_{12}^2 = 0$. So $AB = AC$ does not give $B = C$ unless $A$ is invertible.
- **Centre.** For a ring $R$ with identity, the matrices that commute with every matrix in $M_n(R)$ are exactly the $cI_n$ with $c$ in the centre of $R$; over a field, the scalar matrices.
- **Triangular shapes.** Over any ring, a product of upper triangular $n \times n$ matrices is upper triangular, with $(AB)_{ii} = a_{ii} b_{ii}$, and a strictly upper triangular $N$ of order $n$ has $N^n = 0$.
- **Transpose.** Over a commutative ring, $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$; over $\mathbb{C}$, $(AB)^* = B^* A^*$ and $(cA)^* = \overline{c} A^*$. For every matrix $A$, $A^{\mathsf{T}} A$ is symmetric and $A^* A$ is Hermitian.
- **Splitting.** When $2$ is invertible in the commutative ring $R$, every square $A$ is uniquely $S + K$ with $S = \tfrac12(A + A^{\mathsf{T}})$ symmetric and $K = \tfrac12(A - A^{\mathsf{T}})$ skew-symmetric. Every complex square $A$ is uniquely $H + iK$ with $H$ and $K$ Hermitian.
- **Trace.** Over a commutative ring, $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ for $A$ of size $m \times n$ and $B$ of size $n \times m$. This allows cyclic shifts of longer products, not arbitrary reorderings.
- **Commuting matrices.** If $AB = BA$ over a commutative ring, then $(A + B)^m = \sum_{k=0}^{m} \binom{m}{k} A^k B^{m-k}$. Without $AB = BA$ the formula fails already for $m = 2$.
- **Matrix units.** $E_{ij} E_{kl} = \delta_{jk} E_{il}$, and the $mn$ units of size $m \times n$ form the standard basis of the space of $m \times n$ matrices over a field.

| Kind | Condition | Sum of two | Product of two | Diagonal or trace |
|---|---|---|---|---|
| Symmetric | $A^{\mathsf{T}} = A$ | always | symmetric iff $AB = BA$ | any |
| Skew-symmetric | $A^{\mathsf{T}} = -A$ | always | not in general; $AB - BA$ is | zero diagonal if $2$ is not a zero divisor |
| Hermitian | $A^* = A$ | always | Hermitian iff $AB = BA$ | real diagonal |
| Nilpotent | $N^k = 0$ | nilpotent if $AB = BA$ | nilpotent if $AB = BA$ | trace $0$ over a field |
| Idempotent | $P^2 = P$ | not in general | idempotent if $AB = BA$ | trace equals rank in characteristic $0$ |
| Involutory | $A^2 = I$ | not in general | involutory if $AB = BA$ | $\tfrac12(I + A)$ idempotent if $2$ is invertible |

: Special square matrices and what survives sums and products. "Not in general" means that a $2 \times 2$ counterexample exists.

## Common errors

- **Multiplying in the wrong order.** $(AB)^{\mathsf{T}}$ is $B^{\mathsf{T}} A^{\mathsf{T}}$, not $A^{\mathsf{T}} B^{\mathsf{T}}$, and $(A + B)^2$ is $A^2 + AB + BA + B^2$. Write the factors in the order the definition gives before you simplify.
- **Cancelling.** From $AB = 0$ you cannot conclude $A = 0$ or $B = 0$, and from $P^2 = P$ you cannot conclude $P = I$ or $P = 0$. Cancelling needs an invertible factor.
- **Forgetting the conjugate.** Over $\mathbb{C}$, lengths and Hermitian matrices use $A^*$, not $A^{\mathsf{T}}$. A complex symmetric matrix need not have real eigenvalues.
- **Trusting the diagonal.** A zero diagonal does not make a matrix skew-symmetric or nilpotent, and an entrywise square is not the matrix square.
- **Mixing sizes.** Zero matrices and identity matrices of different sizes are different matrices. For a $2 \times 3$ matrix $A$, $I_2 A = A I_3 = A$, while $A I_2$ is not defined.
- **Ignoring the ring.** The transpose rule and the cyclic property of the trace need a commutative ring of entries; over the quaternions both fail for $1 \times 1$ matrices.
