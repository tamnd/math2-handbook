Compute $2^m + 1$ for $m = 1, 2, \dots, 8$. The values are $3, 5, 9, 17, 33, 65, 129, 257$. Four of them are prime, $3$, $5$, $17$ and $257$, and they occur at $m = 1, 2, 4, 8$, the powers of $2$. The others factor: $9 = 3 \cdot 3$, $33 = 3 \cdot 11$, $65 = 5 \cdot 13$, $129 = 3 \cdot 43$. Three different kinds of thinking now start.

The first is a guess from cases: perhaps $2^m + 1$ is prime only when $m$ is a power of $2$. The second is a guess at a reason. In $65 = 5 \cdot 13$ the factor $5$ is $2^2 + 1$, and $6 = 2 \cdot 3$ has the odd factor $3$; in $33$ the factor $3$ is $2^1 + 1$, and $5$ is odd. The third is an argument that covers every $m$ at once. If $m = ab$ with $b > 1$ odd, put $x = 2^a$; then

$$2^m + 1 = x^b + 1 = (x + 1)\left(x^{b-1} - x^{b-2} + \dots - x + 1\right),$$

and $1 < x + 1 < 2^m + 1$, so $2^m + 1$ is not prime. So if $2^m + 1$ is prime, $m$ has no odd factor above $1$, and $m$ is a power of $2$. No further case needs checking. The converse is a different statement, and it is false: Fermat believed that every $2^{2^n} + 1$ is prime, and Euler found $2^{32} + 1 = 641 \cdot 6700417$.

The guess from cases is inductive reasoning, the guess at a reason is abductive, and only the last argument, a deduction, is a [mathematical proof](/0B94TKFQJX/). This chapter is about that difference and about the practice built around it: how proved statements are labelled and read, where proofs start, what an unproved statement is called, why mathematicians prove what they already believe, and how examples, generalization and classification guide the work. It contains few theorems of its own. Its examples come from number theory, geometry, calculus and algebra, and each one is small enough to check by hand.

## What the chapter covers

1. **What a proof is.** The area page [reasoning and proof](/SGSVYFDSYK/) maps the volume. [Mathematical proof](/0B94TKFQJX/) defines a proof as a finite chain of justified steps and separates informal from formal proofs. [Deductive, inductive and abductive reasoning](/5V35SGEN1T/) shows the three kinds of reasoning at work, and why only deduction proves.
2. **How results are labelled and read.** [Theorems, lemmas, corollaries and propositions](/KK5F0F03ZW/) explains what each label signals; all of them mean "proved". [Hypotheses and conclusion](/W48XN2MEM9/) shows how to find the conditions of a theorem, and how to test each one by dropping it and finding a counterexample.
3. **Axioms and conjectures.** The [axiomatic method](/GD2JBXJV5Z/) starts from primitive terms and axioms, proves consistency with a model, and proves independence with a model in which one axiom fails. A [conjecture](/WMEMMHZ3BH/) is an exact statement that nobody has yet proved or disproved; Goldbach's conjecture is still open, Fermat's Last Theorem was proved, and Euler's sum of powers conjecture was refuted.
4. **What proofs do and how mathematics is made.** The [functions of proof](/ENY0GKRJS8/) are verification, explanation, communication, discovery and systematization. The [methodology of mathematics](/3FJ3XMV9KD/) studies how results are found and accepted.
5. **Examples, generalization and classification.** [Examples in mathematical practice](/F3NNR77WKP/) covers examples, non-examples and counterexamples. [Abstraction and generalization](/976RZZCT1H/) shows one proof doing the work of many. [Classification and invariants](/9HQ3TADPA8/) sorts objects up to equivalence, and [problem solvers and theory builders](/Z29HM45R29/) describes two aims of mathematical work.

## A first reading

Read these first, in order:

1. [Mathematical proof](/0B94TKFQJX/)
2. [Deductive, inductive and abductive reasoning](/5V35SGEN1T/)
3. [Theorems, lemmas, corollaries and propositions](/KK5F0F03ZW/)
4. [Hypotheses and conclusion](/W48XN2MEM9/)
5. [Axiomatic method](/GD2JBXJV5Z/)
6. [Conjecture](/WMEMMHZ3BH/)
7. [Examples in mathematical practice](/F3NNR77WKP/)
8. [Classification and invariants](/9HQ3TADPA8/)

The [methodology of mathematics](/3FJ3XMV9KD/) and [problem solvers and theory builders](/Z29HM45R29/) describe mathematical practice and can wait until you have done some proofs of your own. In the other entries, an example that uses groups, vector spaces or calculus can be skipped on a first reading if the subject is new to you; most entries also have an example in whole numbers or plane geometry.

## Before you start

Nothing from earlier chapters is needed. The examples use school algebra and geometry: even and odd numbers, divisibility, primes, inequalities, triangles. A few examples use first-year calculus (continuity, derivatives, [Rolle's theorem](/0194DY35BG/)) or first-year algebra ([groups](/G5S1M9/), [vector spaces](/000AYPA9AJ/), matrices). The next chapter, [the language of mathematical statements](/WMY13MXY3W/), studies "if", "for all" and "there exists" in detail; this chapter uses them in their everyday sense. Readers who want the formal side of proof can look ahead to [mathematical logic](/DYJ0KGTPMR/).
