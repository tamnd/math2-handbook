The rational field is built from the ring $\Z$. Its elements are pairs $(a, b)$ of integers with $b \neq 0$, two pairs $(a, b)$ and $(c, d)$ stand for the same fraction when $ad = cb$, and the sum and product of fractions are given by polynomial formulas in the entries. All of this is first-order in the ring $\Z$, so $\Q$ is a structure that lives inside $\Z$, although it is not a subset of it. The complex field lives inside the real field in the same way, as the plane $\R^2$ with polynomial operations, and here no equivalence relation is needed. Each sentence about $\C$ translates into a sentence about $\R$, and since the theory of real closed fields is decidable, so is the theory of $\C$.

The chapter makes this idea precise and follows it in two directions. Between structures, an [interpretation](/7R0SJPH37J/) transfers definable sets, decidability and stability, and [bi-interpretability](/KHZ1E7RMMQ/) says when two structures are the same for model theory. Inside one structure, a definable equivalence relation has classes that need not be ordinary elements. The structure $M^{\mathrm{eq}}$ adds them as [imaginary elements](/Q0HM88QQKN/), and every definable set gets a canonical parameter, an element fixed by exactly the automorphisms that fix the set. In a field, the set $\set{a, b}$ has the code $(a + b, ab)$; in a pure set, no tuple of elements codes it. Theories where a code made of ordinary elements always exists, such as the theories of algebraically closed and real closed fields, are said to [eliminate imaginaries](/6M2R0ER3KV/).

## What the chapter covers

The chapter is in three groups, read in order.

1. **Interpretations.** An [interpretation](/7R0SJPH37J/) of $N$ in $M$ is a definable set of $n$-tuples, a definable equivalence relation and definable relations, with a coordinate map onto $N$. The reduction of formulas transfers decidability, stability and automorphisms. [Bi-interpretability](/KHZ1E7RMMQ/) asks that the two composite coordinate maps be definable; a field and its affine group are bi-interpretable with parameters, and a set and its square interpret each other without being bi-interpretable.
2. **Imaginaries and their elimination.** [Imaginary elements](/Q0HM88QQKN/) are the classes of $\emptyset$-definable equivalence relations, gathered in the many-sorted structure $M^{\mathrm{eq}}$, which adds no new definable sets of ordinary tuples. [Elimination of imaginaries](/6M2R0ER3KV/) and its weak and uniform forms say when classes have real codes; Poizat's theorem gives all three for algebraically closed fields. A [stably embedded set](/14WPPDDK8M/) is a definable set on which outside parameters define nothing new.
3. **Beyond imaginaries.** [Hyperimaginaries](/NQPCDVV3NB/) are classes of type-definable equivalence relations, such as "infinitely close" in a nonstandard real closed field, and stable theories eliminate them. The [reconstruction theorem](/AM0523XJ9D/) of Ahlbrandt and Ziegler recovers a countable $\omega$-categorical structure, up to bi-interpretation, from its topological automorphism group.

## A first reading

A short course takes these entries in order.

- [Interpretation](/7R0SJPH37J/), with the examples of $\Q$ in $\Z$ and $\C$ in $\R$, and the reduction $\psi \mapsto \psi_\Gamma$, which every later use relies on.
- [Bi-interpretability](/KHZ1E7RMMQ/), for the definition and the example of a set and its square.
- [Imaginary elements](/Q0HM88QQKN/), with the canonical parameter of a line in the plane.
- [Elimination of imaginaries](/6M2R0ER3KV/), for the three forms of the definition, the pure set as the basic failure, and the statement of Poizat's theorem. Its proof can wait.
- [Stably embedded set](/14WPPDDK8M/), for the definition and the generic bipartite graph as a non-example.

[Hyperimaginaries](/NQPCDVV3NB/) matter mainly for simple theories and can be left for later. The [reconstruction theorem](/AM0523XJ9D/) can be read for its statement and for the examples that show its hypotheses are needed; its proof uses the [small index property](/RZAF6NVEXC/) of Chapter 4.7.

## Before you start

The chapter assumes the following.

- [Basic notions of model theory](/AY09KYSW81/), above all [definable sets](/CY1TXHF6KQ/), [reducts](/EY20BF96SJ/) and the automorphism test. In Volume 2, [definable relations](/1DQ1M6ZWS4/) and [decidable theories](/HWC687ES0Q/); the proof-theoretic cousin of an interpretation is [interpretability between theories](/8H03GRMDYG/).
- [Quantifier elimination and model completeness](/1A9JSC5YG8/), for [quantifier elimination in algebraically closed fields](/2NBBJADY5N/) and in [real closed fields](/FSJ9NGRRPA/), which the examples of fields use.
- [Types and saturated models](/Z772KEC9BY/): [types](/9V71Q3SD1G/), [algebraic and definable closure](/DKAGC639W9/) and the [monster model](/EYTTQZ0E1S/), in which definability over a set is tested by automorphisms.
- [Countable models and categoricity](/6XEXRME4C1/), for [$\omega$-categorical theories](/A22K1X8GKD/) and the [Ryll-Nardzewski theorem](/1513J40TKA/), used in the last entry.
