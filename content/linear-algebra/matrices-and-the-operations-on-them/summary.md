## What to remember

- The [product](/032Q9FB8MT/) of an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$ is the $m \times p$ matrix with $(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$. Column $j$ of $AB$ is $A$ times column $j$ of $B$, and the [matrix–vector product](/0PDVQEP0ZC/) $Ax$ is the combination $x_1 a_1 + \cdots + x_n a_n$ of the columns of $A$.
- Matrix multiplication is [associative](/073E4XC016/) and distributes over addition, and $I_m A = A = A I_n$. It is [not commutative](/0P506SPZP2/): for $n \ge 2$ there are $n \times n$ matrices with $AB \neq BA$, and there are nonzero $A$, $B$ with $AB = 0$.
- The [matrix ring](/AB2MD5CD13/) $M_n(R)$ has the zero matrix and $I_n$ as its $0$ and $1$. Its centre is the set of [scalar matrices](/067NKSBEWT/) $cI$ with $c$ central in $R$.
- The [transpose](/09DXWYRD43/) reverses products, $(AB)^{\mathsf T} = B^{\mathsf T} A^{\mathsf T}$, and the [conjugate transpose](/0DXKE10PHF/) does the same, $(AB)^* = B^* A^*$. Every square matrix over $\R$ is the sum $\tfrac12(A + A^{\mathsf T}) + \tfrac12(A - A^{\mathsf T})$ of a symmetric and a skew-symmetric matrix.
- [Block matrices](/0ASDFEQS6P/) multiply by the row-times-column rule with blocks in place of entries, when the column cuts of the left factor match the row cuts of the right factor.
- The [trace](/0XC1RDBY7A/) is linear, $\operatorname{tr} A^{\mathsf T} = \operatorname{tr} A$, and $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ by the [cyclic property](/0Y4NF1DRKD/). It is not multiplicative. For real $A$, $\operatorname{tr}(A^{\mathsf T} A)$ is the sum of the squares of the entries.
- If $N^k = 0$, then $I - N$ is invertible with inverse $I + N + \cdots + N^{k-1}$. Strictly upper triangular matrices are [nilpotent](/07BSPZPSMF/).
- The [matrix units](/4H93XF4RVH/) multiply by $E_{ij} E_{kl} = \delta_{jk} E_{il}$, and every matrix is $A = \sum_{i,j} a_{ij} E_{ij}$.

| Kind | Condition | Example | Product of two of them |
|---|---|---|---|
| [diagonal](/044JNC7ZAA/) | $a_{ij} = 0$ for $i \neq j$ | $\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ | diagonal, and they commute |
| [upper triangular](/0N4XY7Z3NN/) | $a_{ij} = 0$ for $i > j$ | $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ | upper triangular |
| [symmetric](/0VR671PHE5/) | $A^{\mathsf T} = A$ | $\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$ | symmetric if and only if $AB = BA$ |
| [skew-symmetric](/0PBY4E9GQF/) | $A^{\mathsf T} = -A$ | $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ | not in general: the example squares to $-I$ |
| [Hermitian](/0P17NGQQMQ/) | $A^* = A$ | $\begin{pmatrix} 2 & i \\ -i & 1 \end{pmatrix}$ | Hermitian if and only if $AB = BA$ |
| nilpotent | $N^k = 0$ for some $k$ | $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ | not in general: $E_{12} E_{21} = E_{11}$ |
| [idempotent](/0KCE8CG86P/) | $P^2 = P$ | $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ | not in general: $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$ |
| [involutory](/NH2QE3671N/) | $A^2 = I$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | not in general: $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ squares to $-I$ |

: Special square matrices over $\R$ (over $\C$ for Hermitian), their defining conditions, and what happens to a product of two of them.

## Common errors

- **Multiplying entry by entry.** The product $AB$ is not the matrix of the products $a_{ij} b_{ij}$; the square of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is $\begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$, not $\begin{pmatrix} 1 & 4 \\ 9 & 16 \end{pmatrix}$.
- **Using the rules of commutative algebra.** $(A + B)^2 = A^2 + AB + BA + B^2$, which equals $A^2 + 2AB + B^2$ only when $AB = BA$.
- **Cancelling.** $AB = AC$ with $A \neq 0$ does not give $B = C$, and $AB = 0$ does not give $A = 0$ or $B = 0$. Cancellation is allowed when $A$ is [invertible](/0EB9N0S33C/).
- **Keeping the order under the transpose.** $(AB)^{\mathsf T} = B^{\mathsf T} A^{\mathsf T}$, not $A^{\mathsf T} B^{\mathsf T}$; for non-square factors the wrong order is not even defined.
- **Transposing without conjugating over $\C$.** For complex vectors the length comes from $x^* x$, not $x^{\mathsf T} x$, and Hermitian means $A^* = A$, not $A^{\mathsf T} = A$.
- **Permuting a trace freely.** $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$, but $\operatorname{tr}(ABC)$ need not equal $\operatorname{tr}(BAC)$. Only cyclic shifts are allowed.
