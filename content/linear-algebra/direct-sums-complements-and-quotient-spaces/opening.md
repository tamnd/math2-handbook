There are two ways to cut a vector space into simpler parts. The first is to split it. Every square real matrix is a symmetric matrix plus a skew-symmetric one, in exactly one way:
$$A = \tfrac12 (A + A^\top) + \tfrac12 (A - A^\top),$$
so the space of $n \times n$ matrices is the direct sum of the symmetric and the skew-symmetric matrices. A linear map can then be studied one piece at a time. The second way is to ignore part of the space. Differentiation sends two polynomials to the same derivative exactly when they differ by a constant. If you treat polynomials that differ by a constant as one object, differentiation becomes injective. That object is the quotient of $\R[x]$ by the constants, and the map it induces is an isomorphism onto $\R[x]$.

The two ways are related. A subspace $U$ of $V$ always has a complement $W$, a subspace with $V = U \oplus W$, and every complement is isomorphic to the quotient $V/U$. A complement is a choice, and there are usually many. The quotient is not a choice, and it is the same whatever complement you pick. In finite dimension the two give the same numbers. The quotient matters in infinite dimension, in proofs that should not depend on a basis, and later in algebra, where modules may have no complements at all.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Direct sums and products.** The [internal direct sum](/0XYYT5KNTX/) of subspaces, with the test $U \cap W = 0$ for two of them. The [external direct sum](/0S7W6EG32V/) of arbitrary spaces and its universal property, and the [direct product](/0EX2HPXPJ6/), which differs from it for infinite families.
2. **Complements and projections.** A [complementary subspace](/0M83V17KHX/) of $U$, the theorem that [one always exists](/0P9T8WHNMH/), and [projections](/033DA1WE8Y/), the maps with $P^2 = P$, which match the decompositions $V = U \oplus W$ one to one.
3. **Quotient spaces.** The [quotient space](/0BR3FY5Q8M/) $V/U$, the formula $\dim V/U = \dim V - \dim U$ for the [dimension of a quotient](/0SXDQ6TN00/), and the [universal property](/0ZERJX6PH6/) that lets linear maps pass to the quotient.
4. **The isomorphism theorems.** The [first](/0MTBGVZ4XJ/), [second](/0APN65D6Y6/) and [third](/07RB3EMBWW/) isomorphism theorems for vector spaces, with the Grassmann formula as a consequence of the second.
5. **Codimension and exact sequences.** The [codimension](/JJCGJ1EGCQ/) of a subspace, defined as $\dim V/U$, and [exact sequences](/946YAZNYKX/), the language in which the theorems of the chapter are often stated.

## A first reading

Read these entries first, in order: [internal direct sum](/0XYYT5KNTX/), [complementary subspace](/0M83V17KHX/), [existence of a complement](/0P9T8WHNMH/), [projection](/033DA1WE8Y/), [quotient space](/0BR3FY5Q8M/), [dimension of a quotient](/0SXDQ6TN00/), [universal property of the quotient](/0ZERJX6PH6/) and the [first isomorphism theorem](/0MTBGVZ4XJ/). The attached examples of the quotient space are worth doing by hand, since cosets take some getting used to.

The external direct sum and the direct product can wait if you only work with subspaces of one space; they matter for infinite families. The second and third isomorphism theorems, codimension and exact sequences can be left for a second pass. They state facts you can already prove with bases, but they state them in a form that also works without bases and carries over to groups and modules.

## Before you start

You need [vector spaces, span, independence, bases and dimension](/MVH97H8B2J/): [subspaces](/0EPTJA5QV4/), the [sum](/0JMTY8MF54/) and [intersection](/0V33SPH7RR/) of subspaces, [extension to a basis](/0M4SXE5WW3/) and the [Grassmann formula](/06HTJNCMPA/). You also need [linear maps](/9080WQTZ3M/): the [kernel](/0S23E6YE83/), the [image](/0WSFKKT6FF/), [isomorphisms](/0B8T10CE7N/) and the [rank–nullity theorem](/0W4FSW1TVB/). The proof that complements exist in infinite dimension uses [Zorn's lemma](/04RXTQA5ZA/). If you know the [first isomorphism theorem for groups](/0CXXJNG5B6/), the third group of entries will look familiar.
