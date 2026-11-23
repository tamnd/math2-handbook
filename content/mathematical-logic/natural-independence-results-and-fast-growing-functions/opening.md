Write $5$ in hereditary base $2$, as $2^{2^1} + 1$. Replace every $2$ by $3$ and subtract $1$: the result is $3^{3^1} = 27$. Now replace every $3$ by $4$ and subtract $1$ again, and keep going. The numbers run $5, 27, 255, 467, 775, \dots$ and seem to grow for ever, yet they reach $0$. That is [Goodstein's theorem](/XQMNJF241J/). It is true, it speaks only about natural numbers, and [Peano arithmetic](/HACXBCM7SS/) cannot prove it. Even the sequence that starts at $4$ first reaches $0$ at term number $3 \cdot 2^{402653211} - 2$, a number with more than $121$ million digits.

Gödel's [first incompleteness theorem](/X9WYNYE29C/) already gives a true sentence that $\mathsf{PA}$ does not prove, but that sentence is built for the purpose and speaks about its own provability. For decades it was possible to hope that every question an ordinary mathematician asks about the natural numbers is settled by $\mathsf{PA}$. In 1977 Jeff Paris and Leo Harrington ended that hope with the [Paris-Harrington theorem](/509ZWA0R26/), a variant of the finite Ramsey theorem in which the homogeneous set must be *large*. Laurie Kirby and Paris proved Goodstein's theorem unprovable in 1982. Harvey Friedman found finite statements about trees that escape the much stronger system $\mathsf{ATR}_0$.

These results share one feature, which is growth. Each statement says that some function is total, and that function grows faster than every function the theory can prove total. Hierarchies of functions indexed by ordinals make this exact. For $\mathsf{PA}$ the measure is [$\varepsilon_0$](/KT50SMH3EC/): every function that $\mathsf{PA}$ proves total is eventually dominated by a level $f_\alpha$ of the fast-growing hierarchy with $\alpha < \varepsilon_0$.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Goodstein's theorem and growth.** [Goodstein's theorem](/XQMNJF241J/), whose process stops because each step lowers an ordinal, and [provably total functions](/Z742YPHPNS/), which measure a theory by growth.
2. **Hierarchies of functions.** The [fast-growing hierarchy](/R6ZC4BJGXV/), the [Hardy hierarchy](/X8RKXQASR9/) and the [slow-growing hierarchy](/VDF6R9EVJ2/).
3. **Hydras and worms.** The [Kirby-Paris hydra](/C028FF4TWM/) and [Beklemishev's worm principle](/MHDZGDNEPS/), which comes from provability logic. Both stop for the same reason as Goodstein sequences.
4. **Ramsey-type statements.** The [strengthened finite Ramsey theorem](/4P2BAT6YC3/), its unprovability in the [Paris-Harrington theorem](/509ZWA0R26/), the [indicators](/JWTZ8NVVGK/) that detect cuts of a model by the size of a definable function, and the [Kanamori-McAloon theorem](/NM5WYBK6BG/) on regressive colorings.
5. **Beyond Peano arithmetic.** The [Buchholz hydra](/9APRFM0G7F/), [Friedman's finite form of Kruskal's theorem](/12XRGBWH59/), unprovable in $\mathsf{ATR}_0$, and the [finite graph minor theorem](/WXNTPQGJ38/), unprovable in $\Pi^1_1\text{-}\mathsf{CA}_0$.
6. **The general picture.** The notion of [concrete incompleteness](/E2H655A7BS/) that gathers all these examples.

## A first reading

For a first reading, take these entries in order: [Goodstein's theorem](/XQMNJF241J/), [provably total function](/Z742YPHPNS/), [fast-growing hierarchy](/R6ZC4BJGXV/), [Hardy hierarchy](/X8RKXQASR9/), [Kirby-Paris hydra](/C028FF4TWM/), [strengthened finite Ramsey theorem](/4P2BAT6YC3/), [Paris-Harrington theorem](/509ZWA0R26/) and [concrete incompleteness](/E2H655A7BS/). Goodstein's theorem and the hydra are the best place to see how an ordinal below $\varepsilon_0$ proves that a process stops. Compute a few steps by hand before reading the proofs.

The slow-growing hierarchy, the worm principle and the whole group beyond Peano arithmetic can wait. The group beyond Peano arithmetic needs the large ordinals of the chapter on ordinal analysis and the subsystems of second-order arithmetic. Indicators are the original method of Paris and Harrington and are worth a second pass; the route through provably total functions is shorter to state.

## Before you start

You need [Peano arithmetic](/HACXBCM7SS/) and the [fragments of Peano arithmetic](/T70PYM1F36/) in Chapter 2.10, with the [$\Sigma_n$ and $\Pi_n$ formulas](/GE43CSZTS9/). From Chapter 2.11 you need Gödel's [first](/X9WYNYE29C/) and [second](/4PZM5GJTR5/) incompleteness theorems and the [reflection principles](/NB485KFXKV/), because several statements here are equivalent over $\mathsf{PA}$ to the $1$-consistency of $\mathsf{PA}$. On the ordinal side you need [ordinal numbers](/0YSCSX5YZC/) and the [Cantor normal form](/6GD30FGYDZ/). For the combinatorics, [Ramsey's theorem](/00TQV3F5S4/) and the [compactness theorem](/1NR3HAWG9D/) are enough. The [Ackermann function](/N470JF7ZJX/), which [is not primitive recursive](/97QF3KHSBY/), is the first example of a function that escapes a natural class by growth. The proofs of unprovability for the termination games use [Gentzen's consistency proof](/QPV0HNP22S/) and the [proof-theoretic ordinal](/C72RBH0CDR/) of $\mathsf{PA}$; it is enough to know their statements.
