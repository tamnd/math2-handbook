Take the plane $U$ given by $x + y + z = 0$ in $\R^3$ and the line $L = \R(1, 1, 1)$.
Every vector $v = (x, y, z)$ splits into a piece in $U$ and a piece in $L$.
Put $s = (x + y + z)/3$; then
$$v = \bigl(v - s(1, 1, 1)\bigr) + s(1, 1, 1),$$
and the first piece has coordinate sum $0$, so it lies in $U$.
For $v = (2, 5, -1)$ we get $s = 2$ and $v = (0, 3, -3) + (2, 2, 2)$.
The splitting is unique, because $U \cap L = \set{0}$, and so $\R^3$ is the [internal direct sum](/0XYYT5KNTX/) $U \oplus L$.

The line $L$ is not the only choice.
The $x$-axis also meets $U$ only in $0$, and it splits the same vector as
$$(2, 5, -1) = (-4, 5, -1) + (6, 0, 0).$$
Both lines are [complements](/0M83V17KHX/) of $U$, the two pieces in $U$ differ, and nothing in the plane prefers one line to the other; the example of [two complements of a plane](/DVP2D04EZD/) works this out.
Each choice of complement gives a [projection](/033DA1WE8Y/) onto $U$, and the two projections are different maps.

One number does not depend on any choice: the sum $x + y + z$.
Two vectors differ by an element of $U$ exactly when they have the same coordinate sum, so this number labels the planes $v + U$ parallel to $U$.
These parallel planes, the cosets of $U$, form a vector space of their own, the [quotient space](/0BR3FY5Q8M/) $\R^3/U$.
The map $v + U \mapsto x + y + z$ is an isomorphism $\R^3/U \to \R$, as the example of [the quotient by the plane](/7SNB2G6Q36/) shows, and it was found without choosing a basis or a complement.

So a subspace $U$ of $V$ can be cut away in two ways.
A complement $W$ with $V = U \oplus W$ lives inside $V$ but must be chosen.
The quotient $V/U$ lives outside $V$ but is canonical.
In finite dimension both have dimension $\dim V - \dim U$, and every complement is isomorphic to the quotient.
The quotient is the tool behind many later constructions: the solution set of $Ax = b$ is a coset of the null space, the first isomorphism theorem $V/\ker T \cong \operatorname{im} T$ is a coordinate-free form of rank-nullity, and polynomials modulo a fixed polynomial, such as $\R[x]$ modulo the multiples of $x^2$, are quotients.

## What the chapter covers

1. Direct sums and products. The [internal direct sum](/0XYYT5KNTX/) of subspaces, the [external direct sum](/0S7W6EG32V/) of arbitrary spaces and the [direct product](/0EX2HPXPJ6/), which differs from the direct sum only for infinite families.
2. Complements and projections. Every subspace has a [complementary subspace](/0M83V17KHX/), by the [existence theorem](/0P9T8WHNMH/), and a choice of complement is the same as a [projection](/033DA1WE8Y/), a linear map with $P^2 = P$.
3. Quotient spaces. The [quotient space](/0BR3FY5Q8M/) $V/U$, the formula for its [dimension](/0SXDQ6TN00/), and its [universal property](/0ZERJX6PH6/): a map that vanishes on $U$ passes to $V/U$.
4. The isomorphism theorems. The [first](/0MTBGVZ4XJ/), [second](/0APN65D6Y6/) and [third](/07RB3EMBWW/) isomorphism theorems, each a short consequence of the universal property.
5. Codimension and exact sequences. The [codimension](/JJCGJ1EGCQ/) $\dim V/U$, which can be finite in infinite-dimensional spaces, and [exact sequences](/946YAZNYKX/), which package kernels and images and always split for vector spaces.

## A first reading

For a first pass, read these entries in order:

1. [Internal direct sum](/0XYYT5KNTX/)
2. [Complementary subspace](/0M83V17KHX/)
3. [Projection](/033DA1WE8Y/)
4. [Quotient space](/0BR3FY5Q8M/)
5. [Dimension of a quotient space](/0SXDQ6TN00/)
6. [Universal property of the quotient space](/0ZERJX6PH6/)
7. [First isomorphism theorem](/0MTBGVZ4XJ/)
8. [Codimension](/JJCGJ1EGCQ/)

You can skip at first the infinite families in the external sum and the product, the proof of the existence of complements by Zorn's lemma, the third isomorphism theorem, and exact sequences of more than three nonzero terms.
In finite dimension the first two reduce to direct sums of finitely many spaces and to extending a basis.

## Before you start

You need subspaces, sums and intersections of subspaces, bases and dimension from [vector spaces, span, independence, bases and dimension](/MVH97H8B2J/), and kernels, images and isomorphisms from [linear maps](/9080WQTZ3M/), including the [rank-nullity theorem](/0W4FSW1TVB/).
For infinite-dimensional spaces the chapter uses the theorem that [every vector space has a basis](/00MS9VMQ9Z/), which rests on the [axiom of choice](/0HTGB13FE2/).
