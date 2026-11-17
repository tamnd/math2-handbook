Which facts about the natural numbers follow from which axioms? The equation $2 + 2 = 4$ follows from the recursive definition of addition alone. The law $x + y = y + x$ does not: it needs induction. Euclid's proof that there are infinitely many primes uses numbers as large as $n! + 1$, and it goes through in a theory with induction for bounded formulas and a total exponential function. That every Goodstein sequence reaches $0$ needs more than all the induction that first-order Peano arithmetic offers. Formal arithmetic sorts such facts by the axioms they need, and the sorting is fine enough to tell apart theories that differ by a single class of induction axioms.

This chapter builds the theories that the next chapter proves incomplete. Its central technical fact is that a very weak theory, Robinson arithmetic, already proves every true statement of the form "this computation halts", and can express every computable function. Everything else in the chapter hangs on that fact, or on how much stronger a theory must be to prove a given general law.

## What the chapter covers

The chapter is in five groups, read in order.

1. **The language and the weakest theories.** The [language of arithmetic](/D8SD54M5PN/), [Robinson arithmetic](/3K1AKGXF8A/) $\mathsf{Q}$, and the [weaker theories](/Q5MT8WY7JM/) $\mathsf{R}$ and $\mathsf{TC}$ that are still essentially undecidable.
2. **Peano arithmetic and quantifier complexity.** [Peano arithmetic](/HACXBCM7SS/) with its induction schema, and the [classes $\Delta_0$, $\Sigma_n$ and $\Pi_n$](/GE43CSZTS9/) that measure the logical complexity of formulas.
3. **What Robinson arithmetic proves and represents.** [$\Sigma_1$-completeness](/69234Z1V00/), [representability](/BJF29XET83/) of recursive functions, and [Gödel's $\beta$-function](/BM6P0C2AC2/), which codes finite sequences by two numbers.
4. **Fragments between Robinson and Peano arithmetic.** [Primitive recursive arithmetic](/WCXH72T8D8/), [elementary function arithmetic](/2JD80TE553/), the [fragments](/T70PYM1F36/) $\mathrm{I}\Sigma_n$, and the proof that [Peano arithmetic is not finitely axiomatizable](/M5WNB181T7/).
5. **True arithmetic.** [True arithmetic](/DX0KPMH4QZ/), the complete theory of the standard model, and how far it lies beyond any axiom system.

## A first reading

For a first reading, take these nine entries in order: [the language of arithmetic](/D8SD54M5PN/), [Robinson arithmetic](/3K1AKGXF8A/), [Peano arithmetic](/HACXBCM7SS/), [the classes $\Delta_0$, $\Sigma_n$, $\Pi_n$](/GE43CSZTS9/), [$\Sigma_1$-completeness of Q](/69234Z1V00/), [representability](/BJF29XET83/), [the $\beta$-function lemma](/BM6P0C2AC2/), [fragments of Peano arithmetic](/T70PYM1F36/) and [true arithmetic](/DX0KPMH4QZ/). The first seven are what the incompleteness theorems need.

The weak theories $\mathsf{R}$ and $\mathsf{TC}$, primitive recursive arithmetic, elementary function arithmetic and the proof that $\mathsf{PA}$ is not finitely axiomatizable can wait. They matter for proof theory, and they return in the volume's chapters on ordinal analysis, reverse mathematics and bounded arithmetic.

## Before you start

You need [first-order languages](/PSRDJXRW53/) and [structures and satisfaction](/NJDME6F845/), and the [completeness and compactness theorems](/FBWW4J1XWG/), which give non-standard models of every theory in this chapter. From computability you need the [primitive recursive functions](/3S95HQ8Q17/) and the idea of a [computably enumerable set](/TN9G24VABN/). The [second-order Peano axioms](/0QFT7Z76N5/) are useful for contrast: they pin down $\N$ up to isomorphism, which no first-order theory can do. The roadmap below lists every entry of the chapter with its kind and level.
