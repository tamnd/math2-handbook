The solutions of a homogeneous system $Ax = 0$ can be added and scaled, and the results are again solutions. The same is true of the polynomials of degree at most $3$, of the solutions of the differential equation $y'' + y = 0$, and of the $2 \times 2$ matrices of trace $0$. A vector space is any set with an addition and a scalar multiplication that behave in this way, and the chapter develops the theory that all these examples share. The solutions of $y'' + y = 0$ are exactly the functions $a \cos t + b \sin t$: two functions describe all of them, and no fewer will do. The polynomials of degree at most $3$ need four, such as $1, x, x^2, x^3$. These numbers are dimensions.

The central notion is a basis: a family of vectors that spans the space and is linearly independent. Every vector is then a combination of the basis in exactly one way, and the coefficients are its coordinates. So a space with a basis of $n$ vectors is a copy of $F^n$, and computations in it become computations with lists of numbers and with matrices. The main theorem is that all bases of a space have the same size. It rests on the Steinitz exchange lemma, which says that an independent list is never longer than a spanning list.

## What the chapter covers

The chapter is in eight groups, read in order.

1. **Vector spaces and their examples.** The [vector space](/000AYPA9AJ/) axioms, and the standard examples: [coordinate space $F^n$](/713F6AM1X1/), [matrices](/0RE6X3BGPN/), [polynomials](/0JGZCDT5DN/), and [functions and sequences](/0GZB2SN0PH/).
2. **Subspaces.** The [linear subspace](/00YC1D652K/) and the subspace test, [intersections and unions](/0V33SPH7RR/), and the [sum of subspaces](/0JMTY8MF54/).
3. **Span and linear independence.** [Linear combinations](/0V8F3E48E6/), the [span](/0DTY8B9HMS/), [spanning sets](/088RYKAWK9/), [linear independence](/0CRMGPAH83/), and the [column test](/76GG9B25A1/) by row reduction.
4. **Bases and coordinates.** The [basis](/0KCQ9Y3QKA/), the [standard bases](/C5QA672NPH/), and the [coordinate vector](/04CYQHN6MC/) of a vector in a basis.
5. **Dimension.** The [Steinitz exchange lemma](/08ZDRN6H41/), the [dimension theorem](/0WK0Y8RH1M/), [dimension](/03GSZ8RTZJ/) itself, and [finite-dimensional spaces](/0ZHWKQMVX5/).
6. **Building bases.** A [spanning set contains a basis](/06MRNP4BNT/), an [independent set extends to a basis](/0M4SXE5WW3/), [every vector space has a basis](/00MS9VMQ9Z/), and a [basis of $\R$ over $\Q$](/ZCBD0GRGVA/).
7. **Counting dimensions.** The [dimension of a subspace](/0QW084460E/), the [right-size criterion](/096V7H13H9/) for a basis, and [Grassmann's formula](/06HTJNCMPA/) for $\dim(U + W)$.
8. **Changing the field.** [Vector spaces over finite fields](/J9VE1X14PV/), and [complexification and realification](/CT2F31EDH8/).

## A first reading

For a first reading, take these entries in order: [vector space](/000AYPA9AJ/), [coordinate space $F^n$](/713F6AM1X1/), [linear subspace](/00YC1D652K/), [linear combination](/0V8F3E48E6/), [linear span](/0DTY8B9HMS/), [linear independence](/0CRMGPAH83/), [linear dependence of the columns of a matrix](/76GG9B25A1/), [basis](/0KCQ9Y3QKA/), [coordinate vector](/04CYQHN6MC/), [Steinitz exchange lemma](/08ZDRN6H41/), [dimension](/03GSZ8RTZJ/) and [right-size criterion for a basis](/096V7H13H9/). These give the finite-dimensional theory with its proofs, and the tools to compute with it.

The infinite-dimensional results can wait: the proofs by Zorn's lemma in the group on building bases, the Hamel basis, and the cardinal part of the dimension theorem. The group on changing the field can also wait until the field matters, in coding theory for finite fields and in the study of eigenvalues for $\R$ and $\C$.

## Before you start

You need the notion of a [field](/04C5ZBG1WT/): the scalars are $\Q$, $\R$, $\C$ or a finite field $\mathbb{F}_q$. [Vectors in the plane and in space](/VKVAJ94SKZ/) give the pictures behind the definitions. The column tests use [Gaussian elimination](/0JVJ2WCXZH/), pivots, and the [homogeneous system](/04KGXJG1A2/) $Ax = 0$ from the chapter on systems of linear equations. The examples use [matrices](/0VD9ZSWWJG/) and their addition. For the infinite-dimensional results you need [cardinal numbers](/0EBACQFAZW/) and [Zorn's lemma](/04RXTQA5ZA/); the rest of the chapter does not use them.
