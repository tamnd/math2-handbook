Many of the functions you meet in linear algebra take a vector to a number: a coordinate $x \mapsto x_2$, the dot product $x \mapsto a \cdot x$ with a fixed vector $a$, the evaluation $p \mapsto p(2)$ of a polynomial, the integral $f \mapsto \int_0^1 f$, the trace of a matrix. These are the linear forms, and they form a vector space $V^*$ of their own, the dual of $V$. An equation $a_1 x_1 + \cdots + a_n x_n = 0$ is the statement that one linear form vanishes, so a system of linear equations is a list of linear forms, and its solution set is the set of vectors on which all of them vanish.

Duality explains things that otherwise look like accidents of notation. The transpose of a matrix is the matrix of the dual map $f^*(\varphi) = \varphi \circ f$, which runs in the opposite direction to $f$. The equality of row rank and column rank becomes the fact that $f$ and $f^*$ have the same rank. Quadrature rules such as Simpson's rule are linear forms on polynomials written in a dual basis of evaluations. The chapter also shows a difference between finite and infinite dimension. For finite-dimensional $V$, the spaces $V$ and $V^*$ have the same dimension but no natural isomorphism between them, while $V$ and its double dual $V^{**}$ are isomorphic in a way that uses no basis. For infinite-dimensional $V$, the dual is strictly larger than $V$.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Linear forms and hyperplanes.** [Linear forms](/07YQ1C78G0/) and the theorem on [hyperplanes and linear forms](/XR0EQN0H8T/): a nonzero form has a hyperplane as kernel, and its kernel determines it up to a scalar.
2. **The dual space and its dimension.** The [dual space](/07JBSZE0V4/), the [dual basis](/0ZD2CF6ZS0/) of a basis, the [dimension of the dual](/00889YD15K/) in finite dimension, and the [Erdős–Kaplansky theorem](/S5ET1HG2ZX/) in infinite dimension.
3. **The double dual and annihilators.** The [canonical isomorphism with the double dual](/0ZJM9D7NPS/), the [annihilator](/0ASHNYF7AG/) of a subspace, and the [dimension of the annihilator](/06Q1EFVH0Q/), with the duals of subspaces and quotients.
4. **The dual map.** The [dual map](/0AZ5ARP287/), the theorem that its [matrix is the transpose](/0ZPB3180AY/), and the [kernel and image of the dual map](/7FA499AW3T/).

## A first reading

Read these entries first, in order: [linear form](/07YQ1C78G0/), [dual space](/07JBSZE0V4/), [dual basis](/0ZD2CF6ZS0/), [dimension of the dual](/00889YD15K/), [annihilator](/0ASHNYF7AG/), [dimension of the annihilator](/06Q1EFVH0Q/), [dual map](/0AZ5ARP287/), [matrix of the dual map](/0ZPB3180AY/) and [kernel and image of the dual map](/7FA499AW3T/). The attached examples on Lagrange interpolation and on the dual of differentiation show the definitions at work on polynomials.

The Erdős–Kaplansky theorem needs cardinal arithmetic and can be skipped by anyone who works only in finite dimension. The double dual can wait for a second reading; its main use comes later, with tensors and with spaces of functions in analysis.

## Before you start

You need [vector spaces](/MVH97H8B2J/), with bases, coordinates and dimension; [linear maps](/9080WQTZ3M/) and the [space of linear maps](/0X9MBPP2Z3/); and [matrices](/Y1ESNQ2V52/) with the [transpose](/09DXWYRD43/). The annihilator entries use [quotient spaces](/0BR3FY5Q8M/) and the [first isomorphism theorem](/0MTBGVZ4XJ/) from the chapter on [direct sums, complements and quotient spaces](/QHKTJ89V6S/). The last group uses the [matrix of a linear map](/0YQSGNYE3K/) and the [rank](/0ZC9YTXZRY/) from the chapter on [matrices of linear maps, rank and change of basis](/S6559D61BP/).
