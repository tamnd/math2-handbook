A linear map is a rule, and a matrix is a table of numbers. Choosing bases turns one into the other, and the table depends on the bases. The reflection of the plane across the line $y = 2x$ has, in the standard basis, the matrix
$$\begin{pmatrix} -3/5 & 4/5 \\ 4/5 & 3/5 \end{pmatrix}.$$
In the basis $(1, 2)$, $(-2, 1)$, one vector on the line and one perpendicular to it, the same reflection has the matrix $\operatorname{diag}(1, -1)$. The two matrices describe one map, so anything that depends only on the map must be the same for both: here the trace is $0$, the determinant is $-1$ and the rank is $2$. Much of linear algebra consists of finding a basis in which the matrix is simple, and of the quantities that do not change when the basis does.

The other half of the chapter is about what a matrix tells you about linear systems. The system $Ax = b$ has a solution exactly when $b$ lies in the column space of $A$, and when it has one, the solutions form a translate of the null space. The rank $r$ of $A$ controls both: the column space has dimension $r$ and the null space has dimension $n - r$. These are matrix forms of the rank–nullity theorem, and they are what row reduction computes.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Matrices and linear maps.** The [matrix of a linear map](/0YQSGNYE3K/) in given bases, the [linear map of a matrix](/06HMCTAQH3/), and the theorem that the [matrix of a composition](/05Q1B7MH0M/) is the product of the matrices.
2. **The four fundamental subspaces.** The [column space](/03AJKXH1AV/), the [row space](/069MCGX635/) and the [null space](/0PHDYNR24D/) of a matrix, with bases from row reduction, and the [four fundamental subspaces](/73DVECPAT6/) with their dimensions and orthogonality.
3. **Rank.** The [rank of a matrix](/0ZC9YTXZRY/), the theorem that [row rank equals column rank](/0TZAG60ZYT/), [rank–nullity for matrices](/TR48YQGCCA/), the [rank of a product](/02FDWY55AS/), and the [rank factorization](/5JGAG62VN8/) $A = CR$.
4. **Change of basis and similarity.** The [change of basis matrix](/0MKRHZB3WS/), the [change of basis formula](/0MQXVZEBMT/) $[T]_{C',B'} = Q^{-1}[T]_{C,B}P$, [similar matrices](/0E89HQATM8/), and an [example](/J4Q3B9ZNHF/) of two matrices that share the usual invariants but are not similar.
5. **Trace and the Fredholm alternative.** The [trace of a linear map](/0KZDNGA561/), defined through any matrix of it, and the [Fredholm alternative](/4HH8C9V8JQ/) for the solvability of $Ax = b$.

## A first reading

Read these entries first, in order: [matrix of a linear map](/0YQSGNYE3K/), [matrix of a composition](/05Q1B7MH0M/), [column space](/03AJKXH1AV/), [null space](/0PHDYNR24D/), [rank of a matrix](/0ZC9YTXZRY/), [rank–nullity for matrices](/TR48YQGCCA/), [change of basis matrix](/0MKRHZB3WS/), [change of basis formula](/0MQXVZEBMT/) and [similar matrices](/0E89HQATM8/). The examples of the second and third groups share one $3 \times 4$ matrix, and it pays to follow it from entry to entry.

The rank factorization, the inequalities for the rank of a product, the example of non-similar matrices and the Fredholm alternative can wait for a second pass. Keep one warning from the change of basis entries in mind from the start: books differ on which direction they call the change of basis matrix, so check the convention before you use a formula from elsewhere.

## Before you start

You need [systems of linear equations and row reduction](/DXSXFVDMXQ/), in particular the [reduced row echelon form](/0WF5AQYTW6/) and [pivots](/0J0BBCMJ5W/); [matrices](/Y1ESNQ2V52/) with [matrix multiplication](/032Q9FB8MT/) and the [transpose](/09DXWYRD43/); and [invertible matrices](/P8J6QR66TJ/). From [vector spaces](/MVH97H8B2J/) you need bases, coordinates and dimension, and from [linear maps](/9080WQTZ3M/) the kernel, the image and the [rank–nullity theorem](/0W4FSW1TVB/).
