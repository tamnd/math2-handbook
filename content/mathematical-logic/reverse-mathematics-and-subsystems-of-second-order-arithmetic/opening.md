Usually one starts from axioms and proves theorems. [Reverse mathematics](/7SQS69T17R/) goes the other way: it starts from a theorem of ordinary mathematics and asks which axioms are needed to prove it. The setting is [second-order arithmetic](/DC60FYCSPM/), a theory with variables for natural numbers and for sets of natural numbers, in which real numbers, continuous functions and countable algebraic structures can all be coded. A real number is coded by a fast Cauchy sequence of rationals, a continuous function on $[0, 1]$ by a set that lists pairs of rational intervals, and a countable group by a set of triples for its multiplication table. The program, begun by Harvey Friedman in the 1970s and developed by Stephen Simpson and many others, fixes a weak base theory and proves that a theorem is *equivalent* to a set-existence axiom over that base. Then the theorem needs exactly that axiom.

The base theory is [$\mathsf{RCA}_0$](/XQENB067R3/), with comprehension only for computable sets and induction only for $\Sigma^0_1$ formulas; it corresponds to computable mathematics. It already proves the [intermediate value theorem](/66WH4PQ392/). A striking finding is that most theorems studied so far are equivalent to one of five systems, the *big five*: $\mathsf{RCA}_0$, [$\mathsf{WKL}_0$](/7W9EG02T79/), [$\mathsf{ACA}_0$](/NAASTN80QN/), [$\mathsf{ATR}_0$](/MKB74TX3Z8/) and [$\Pi^1_1\text{-}\mathsf{CA}_0$](/T21WETAHN5/). For example, the [Heine–Borel theorem](/07PFYV65MB/) for $[0, 1]$, in its form for countable covers, is [equivalent to $\mathsf{WKL}_0$](/KRS3VTWCHJ/), which adds weak König's lemma: every infinite binary tree has an infinite path. The [Bolzano–Weierstrass theorem](/0KDJD249DT/) is [equivalent to $\mathsf{ACA}_0$](/HV153Y95MQ/), which adds comprehension for arithmetical formulas. The comparability of countable well-orderings is equivalent to $\mathsf{ATR}_0$.

The systems also differ in their models. The $\omega$-models of $\mathsf{RCA}_0$ are exactly the [Turing ideals](/Y6D27XJT3H/), the collections of sets closed under join and under Turing reducibility. The computable sets form the least of them. Some computable infinite binary tree has no computable path, so the computable sets are not a model of $\mathsf{WKL}_0$. In this way an equivalence in reverse mathematics often comes with a theorem of computability theory.

Not everything fits. [Ramsey's theorem for pairs](/ZT5KV6KJ3E/) and two colours lies outside the big five: Seetapun showed that it does not imply $\mathsf{ACA}_0$, and Jiayi Liu that it does not imply $\mathsf{WKL}_0$. Many such combinatorial principles sit between the main systems, and their mutual relations are a large part of current work.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Second-order arithmetic and the method.** The language, axioms and coding of [second-order arithmetic](/DC60FYCSPM/), and the method of [reverse mathematics](/7SQS69T17R/).
2. **The big five and their models.** The systems [$\mathsf{RCA}_0$](/XQENB067R3/), [$\mathsf{WKL}_0$](/7W9EG02T79/), [$\mathsf{ACA}_0$](/NAASTN80QN/), [$\mathsf{ATR}_0$](/MKB74TX3Z8/) and [$\Pi^1_1\text{-}\mathsf{CA}_0$](/T21WETAHN5/), and the [$\beta$-models](/J0Z2GNJZ2W/).
3. **Ramsey's theorem and the zoo.** [Ramsey's theorem for pairs](/ZT5KV6KJ3E/), the [reverse mathematics zoo](/E3X5B175ZR/) of principles between the main systems, and [$\mathsf{WWKL}_0$](/KPHM3025GW/) for measure theory.
4. **Higher-order reverse mathematics.** Kohlenbach's [version of the program](/NPDRXTBW5W/) in all finite types.
5. **Foundational consequences.** [Partial realizations of Hilbert's program](/Z26S516BKH/) and [predicative mathematics](/43BSXNWQBG/).

## A first reading

For a first reading, take [second-order arithmetic](/DC60FYCSPM/), [reverse mathematics](/7SQS69T17R/), [$\mathsf{RCA}_0$](/XQENB067R3/), [$\mathsf{WKL}_0$](/7W9EG02T79/), [$\mathsf{ACA}_0$](/NAASTN80QN/), [$\mathsf{ATR}_0$](/MKB74TX3Z8/), [Ramsey's theorem for pairs](/ZT5KV6KJ3E/) and [partial realizations of Hilbert's program](/Z26S516BKH/). The coding of reals and continuous functions can be taken on trust at first; it matters mostly for the exact statements.

[$\Pi^1_1\text{-}\mathsf{CA}_0$](/T21WETAHN5/), [$\beta$-models](/J0Z2GNJZ2W/) and [higher-order reverse mathematics](/NPDRXTBW5W/) can wait for a second pass. The [zoo](/E3X5B175ZR/) is best read after Ramsey's theorem for pairs, as a map rather than straight through.

## Before you start

You need the chapter on [formal arithmetic and its fragments](/QHCRN4JVG0/), with the [fragments of Peano arithmetic](/T70PYM1F36/) and the classes of [$\Delta_0$, $\Sigma_n$ and $\Pi_n$ formulas](/GE43CSZTS9/), and the [comprehension schema](/5GS6DRJ5SY/) from the chapter on [second-order logic](/MDHDYV8QZW/). The models of the systems use [computable and c.e. sets](/24YMRP8DF5/), the [Turing jump](/60P2XWY5QX/) and the [basis theorems](/AT1EMCPWTF/) for effectively closed classes. [Hilbert's program](/P1RW6JWX73/) explains why the conservation of $\mathsf{WKL}_0$ over primitive recursive arithmetic matters, and the chapter on [Gödel's incompleteness theorems](/HXHHWY3328/) supplies the consistency statements.
