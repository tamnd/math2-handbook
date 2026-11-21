A matrix is a table of numbers, and the rules for adding and multiplying tables make it a new kind of number. Suppose an airline flies $1 \to 2$, $2 \to 3$, $1 \to 3$ and $3 \to 1$ between three cities. Record this as the matrix $A$ with $a_{ij} = 1$ when there is a flight from $i$ to $j$:
$$A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}, \qquad A^2 = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}.$$
The entry $(i, j)$ of $A^2$ is $\sum_k a_{ik} a_{kj}$, the number of ways to fly from $i$ to $j$ with one change: the $1$ in position $(1, 3)$ is the route $1 \to 2 \to 3$. The row-times-column rule for the product is exactly what this count needs, and $A^k$ counts the routes with $k$ flights.

The same rule describes the composition of linear maps. The rotation of the plane by a right angle is $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and the reflection in the $x$-axis is $S = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. Then $RS = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $SR = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$: reflecting and then rotating is not the same as rotating and then reflecting. So the algebra of matrices keeps the associative law and the distributive laws of numbers but loses the commutative law, and with it some familiar rules, such as $(A + B)^2 = A^2 + 2AB + B^2$ and the cancellation of a nonzero factor.

The chapter builds this algebra and names the special matrices that later chapters use all the time.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Matrices and their sizes.** The [matrix](/0VD9ZSWWJG/), the [square matrix](/0JXZKX526R/), the [zero matrix](/4KY5AWGMW5/) and the [identity matrix](/6NHZRCKJNW/).
2. **Sums and products.** [Matrix addition](/0Y7H3SAVA1/), the [matrix–vector product](/0PDVQEP0ZC/), [matrix multiplication](/032Q9FB8MT/), its [associativity](/073E4XC016/) and its [non-commutativity](/0P506SPZP2/).
3. **The matrix ring and its simplest members.** The [matrix ring](/AB2MD5CD13/) $M_n(R)$, the [scalar matrices](/067NKSBEWT/), the [diagonal matrices](/044JNC7ZAA/) and the [upper triangular matrices](/0N4XY7Z3NN/).
4. **Transpose and symmetry.** The [transpose](/09DXWYRD43/), the rule for the [transpose of a product](/09GK5PS824/), [symmetric](/0VR671PHE5/) and [skew-symmetric](/0PBY4E9GQF/) matrices, the [conjugate transpose](/0DXKE10PHF/) and [Hermitian matrices](/0P17NGQQMQ/).
5. **Blocks.** The [block matrix](/0ASDFEQS6P/), which multiplies block by block, and the [block diagonal matrix](/001T5FJDC1/).
6. **The trace.** The [trace](/0XC1RDBY7A/) and its [cyclic property](/0Y4NF1DRKD/) $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
7. **Matrices defined by equations.** [Nilpotent](/07BSPZPSMF/), [idempotent](/0KCE8CG86P/) and [involutory](/NH2QE3671N/) matrices, [commuting matrices](/8G3X8MPG7E/) and the [matrix units](/4H93XF4RVH/) $E_{ij}$.

## A first reading

For a first pass, read these entries in order:

1. [Matrix](/0VD9ZSWWJG/).
2. [Matrix–vector product](/0PDVQEP0ZC/).
3. [Matrix multiplication](/032Q9FB8MT/).
4. [Non-commutativity of matrix multiplication](/0P506SPZP2/).
5. [Identity matrix](/6NHZRCKJNW/).
6. [Diagonal matrix](/044JNC7ZAA/).
7. [Upper triangular matrix](/0N4XY7Z3NN/).
8. [Transpose](/09DXWYRD43/).
9. [Transpose of a product](/09GK5PS824/).
10. [Symmetric matrix](/0VR671PHE5/).
11. [Trace of a matrix](/0XC1RDBY7A/).

The matrix ring, the conjugate transpose and Hermitian matrices can wait until they are needed, for rings in abstract algebra and for complex inner products later in the volume. Block matrices are a tool for computation and proof; read them when a later proof cuts a matrix into blocks. The last group is short and can be read in any order.

## Before you start

The chapter uses vectors in $\R^n$, their sums, multiples and dot products, from [overview and vectors in the plane and in space](/VKVAJ94SKZ/), and linear systems written as $Ax = b$, from [systems of linear equations and row reduction](/DXSXFVDMXQ/). A few entries let the entries of a matrix come from any [ring](/0B1261B5ED/); for a first reading, take them to be real numbers, and complex numbers in the entries on the conjugate transpose.
