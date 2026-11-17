Bounded arithmetic is the study of theories of arithmetic so weak that the functions they prove total are feasible, in the sense of complexity theory. Peano arithmetic proves the totality of functions far beyond anything a computer can evaluate. If induction is allowed only for bounded formulas, in which every quantifier has the form $\forall x \le t$ or $\exists x \le t$, the provable functions shrink, and for suitable theories they are exactly the functions of a complexity class.

The first such theory is $\mathrm{I}\Delta_0$, studied by Rohit Parikh in 1971; it does not prove that exponentiation is total. Samuel Buss introduced in 1986 the hierarchy of theories $S^i_2$ and $T^i_2$, in a language with the length $\abs{x}$ of a binary numeral and the function $x \mathbin{\#} y = 2^{\abs{x}\cdot\abs{y}}$. His witnessing theorem says that the functions definable by $\Sigma^b_1$ formulas and provably total in $S^1_2$ are exactly the functions computable in polynomial time. Stephen Cook's equational theory $\mathrm{PV}$ of 1975 is an earlier theory of the polynomial-time functions. The higher levels of Buss's hierarchy match the levels of the [polynomial hierarchy](/TDQ7AXGM6P/).

The theories are tied to open problems of complexity. Krajíček, Pudlák and Takeuti showed that if the hierarchy of theories $T^i_2$ collapses, then the polynomial hierarchy collapses too. Proofs in bounded arithmetic translate into short proofs in propositional proof systems, which links the subject to [proof complexity](/1Q046J0AW2/). Simple statements remain hard: whether $\mathrm{I}\Delta_0$ proves that there are infinitely many primes is a known open problem.

## What the planned pages will cover

The pages will define $\mathrm{I}\Delta_0$, Buss's theories and Cook's $\mathrm{PV}$, prove the witnessing theorems, describe the translations into propositional proof systems, and explain what a separation of the theories would mean for questions such as [P versus NP](/MFN5GYZH5Z/).

## What to read meanwhile

Chapter 2.10 has the background: [weak theories of arithmetic](/Q5MT8WY7JM/), the classes of [$\Delta_0$, $\Sigma_n$ and $\Pi_n$ formulas](/GE43CSZTS9/), [elementary function arithmetic](/2JD80TE553/) and [primitive recursive arithmetic](/WCXH72T8D8/). In Chapter 2.11, [self-verifying theories](/D8SGFVA3RT/) and [Gödel's speed-up theorem](/37X5XBDBNX/) touch the same questions. For the complexity side, read the [Cook–Levin theorem](/CTK8AH98Z1/) and the opening of Chapter 2.19.
