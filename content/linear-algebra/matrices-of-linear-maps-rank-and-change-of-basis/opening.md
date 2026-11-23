Take the linear map $T \colon \R^2 \to \R^2$, $T(x, y) = (4x - y, 2x + y)$.
In the standard basis its matrix has the images $T(e_1) = (4, 2)$ and $T(e_2) = (-1, 1)$ as columns:
$$A = \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}.$$
Now use the basis $b_1 = (1, 1)$, $b_2 = (1, 2)$ instead.
Then $T(b_1) = (3, 3) = 3b_1$ and $T(b_2) = (2, 4) = 2b_2$, so in this basis the [matrix of the map](/0YQSGNYE3K/) is
$$D = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}.$$
The two matrices look different, but they describe one map.
The [change of basis matrix](/0MKRHZB3WS/) $P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ has the new basis vectors as columns, and the [change of basis formula](/0MQXVZEBMT/) gives $D = P^{-1}AP$.
In the second basis you can read off what $T$ does: it stretches the line $\R b_1$ by $3$ and the line $\R b_2$ by $2$.
What the two matrices have in common is what belongs to the map itself: both have rank $2$, trace $4 + 1 = 3 + 2 = 5$ and determinant $4 + 2 = 3 \cdot 2 = 6$.

The chapter is about this dictionary between linear maps and matrices.
A matrix is a linear map with a choice of bases, and the [product of matrices](/05Q1B7MH0M/) is the matrix of a composition.
Questions about a map, such as whether it is onto or which vectors it kills, become questions about the matrix that row reduction answers.
The image is the [column space](/03AJKXH1AV/), the kernel is the [null space](/0PHDYNR24D/), and with the row space and the left null space they form the [four fundamental subspaces](/73DVECPAT6/).
One number, the [rank](/0ZC9YTXZRY/), fixes all four dimensions.
For the matrix
$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$$
the second row is twice the first, the rank is $1$, the null space is a plane in $\R^3$, and $Ax = b$ has a solution exactly when $b_2 = 2b_1$.
That last test is the [Fredholm alternative](/4HH8C9V8JQ/) at work: $b$ must be killed by $y = (2, -1)$, the vector that spans the null space of $A^{\mathsf{T}}$.

The second half of the chapter turns the question round.
Given a map, which basis makes its matrix simple, and which features of the matrix do not depend on the basis?
Two matrices of one endomorphism are [similar](/0E89HQATM8/), $B = P^{-1}AP$, and rank, trace, determinant and the characteristic polynomial are the same for both.
These invariants are not a complete test, and the chapter shows two matrices that share all of them and are still not similar.
The search for a best basis continues in the chapters on eigenvalues and canonical forms.

## What the chapter covers

1. Matrices and linear maps. The [matrix of a linear map](/0YQSGNYE3K/) in chosen bases, the [linear map of a matrix](/06HMCTAQH3/), and the theorem that the [matrix of a composition is the product](/05Q1B7MH0M/) of the matrices.
2. The four subspaces of a matrix. The [column space](/03AJKXH1AV/), the [row space](/069MCGX635/) and the [null space](/0PHDYNR24D/), with bases read from row reduction, and the [four fundamental subspaces](/73DVECPAT6/) with their dimensions $r$, $n - r$, $r$ and $m - r$.
3. Rank. The [rank](/0ZC9YTXZRY/) computed in several ways, several proofs that [row rank equals column rank](/0TZAG60ZYT/), the [rank-nullity theorem for matrices](/TR48YQGCCA/), the [rank of a product](/02FDWY55AS/), and the [rank factorization](/5JGAG62VN8/) $A = CR$.
4. Change of basis and similarity. The [change of basis matrix](/0MKRHZB3WS/), the [change of basis formula](/0MQXVZEBMT/) $Q^{-1}AP$, [similar matrices](/0E89HQATM8/) and their invariants, and [two matrices that share the usual invariants without being similar](/J4Q3B9ZNHF/).
5. Trace and the Fredholm alternative. The [trace of a linear map](/0KZDNGA561/), defined through any of its matrices, and the [Fredholm alternative](/4HH8C9V8JQ/) for the solvability of $Ax = b$.

## A first reading

For a first pass, read these entries in order:

1. [Matrix of a linear map](/0YQSGNYE3K/)
2. [Matrix of a composition is the product of matrices](/05Q1B7MH0M/)
3. [Column space](/03AJKXH1AV/)
4. [Null space](/0PHDYNR24D/)
5. [Four fundamental subspaces](/73DVECPAT6/)
6. [Rank of a matrix](/0ZC9YTXZRY/)
7. [Row rank equals column rank](/0TZAG60ZYT/)
8. [Change of basis matrix](/0MKRHZB3WS/)
9. [Change of basis formula](/0MQXVZEBMT/)
10. [Similar matrices](/0E89HQATM8/)

On a first reading one proof that row rank equals column rank is enough; the others can wait.
The inequalities of Sylvester and Frobenius for the rank of a product, the example of matrices with equal invariants that are not similar, and the trace over fields of positive characteristic can also wait.

## Before you start

You need [linear maps](/9080WQTZ3M/), with kernel, image and the [rank-nullity theorem](/0W4FSW1TVB/), and bases, coordinates and dimension from [vector spaces, span, independence, bases and dimension](/MVH97H8B2J/).
The computations use the matrix product, the transpose and the trace from [matrices and the operations on them](/Y1ESNQ2V52/), and row reduction with pivots and free variables from [systems of linear equations and row reduction](/DXSXFVDMXQ/).
Change of basis uses the inverse matrices of [invertible matrices and matrix factorizations](/P8J6QR66TJ/).
