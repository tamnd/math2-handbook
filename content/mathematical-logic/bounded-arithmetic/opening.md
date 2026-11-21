[Bounded arithmetic](/A2CFPP8JMN/) is the study of theories of arithmetic so weak that the functions they prove total are feasible, in the sense of complexity theory. [Peano arithmetic](/HACXBCM7SS/) proves the totality of functions far beyond anything a computer can evaluate, such as the [Ackermann function](/N470JF7ZJX/). If induction is allowed only for bounded formulas, in which every quantifier has the form $\forall x \le t$ or $\exists x \le t$, the provable functions shrink, and for suitable theories they are exactly the functions of a complexity class.

The first such theory is $\mathsf{I}\Delta_0$, studied by Rohit Parikh in 1971. It proves that $x \cdot x$ exists for every $x$, but not that $2^x$ exists: by [Parikh's theorem](/YPQPC1WJMV/), every function it proves total is bounded by a polynomial. Bounded formulas still describe a lot. The set of primes is defined by
$$x > 1 \wedge (\forall y \le x)(\forall z \le x)(y \cdot z = x \to y = 1 \vee z = 1),$$
and the sets definable in this way are [exactly the sets in the linear-time hierarchy](/FYGWNXETVJ/).

Samuel Buss introduced in 1986 the hierarchy of theories $S^i_2$ and $T^i_2$, in a language with the length $\abs{x}$ of a binary numeral and the function $x \mathbin{\#} y = 2^{\abs{x} \cdot \abs{y}}$. For example $\abs{1000} = 10$ and $1000 \mathbin{\#} 1000 = 2^{100}$, so $\#$ lets terms grow like $x^{\abs x}$, but no faster than $2^{p(\abs{x})}$ for a polynomial $p$. [Buss's witnessing theorem](/RH4R7GTTAX/) says that the functions definable by $\Sigma^b_1$ formulas and provably total in $S^1_2$ are exactly the functions computable in polynomial time. Stephen Cook's equational theory [$\mathsf{PV}$](/FMM44KFZQT/) of 1975 is an earlier theory of the polynomial-time functions. The higher levels of Buss's hierarchy match the levels of the [polynomial hierarchy](/TDQ7AXGM6P/).

The theories are tied to open problems of complexity. [Krajíček, Pudlák and Takeuti](/YP7KE8E6DC/) showed that if the hierarchy of theories $T^i_2$ collapses, then the polynomial hierarchy collapses too. The [Paris–Wilkie translation](/ZVD982MVST/) turns proofs in bounded arithmetic into short proofs in propositional proof systems, which links the subject to [proof complexity](/1Q046J0AW2/). Simple statements remain hard: whether $\mathsf{I}\Delta_0$ proves that there are infinitely many primes is a known open problem.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Theories and definable sets.** The theories $\mathsf{I}\Delta_0$, $S^i_2$ and $T^i_2$ in the entry on [bounded arithmetic](/A2CFPP8JMN/), the [$\Delta_0$-definable sets and the linear-time hierarchy](/FYGWNXETVJ/), and [Parikh's theorem](/YPQPC1WJMV/).
2. **Feasible functions and witnessing.** [Cook's theory PV](/FMM44KFZQT/), [Buss's witnessing theorem](/RH4R7GTTAX/) and the [Krajíček–Pudlák–Takeuti theorem](/YP7KE8E6DC/).
3. **Propositional translations and the pigeonhole principle.** The [Paris–Wilkie translation](/ZVD982MVST/) and the [pigeonhole principles in bounded arithmetic](/NJ18EZ5JBC/).
4. **Separation and approximate counting.** The open problem of [separating the hierarchy](/PEJQDHHX8E/), and [approximate counting](/65K2S22DGZ/) from the dual weak pigeonhole principle.

## A first reading

For a first reading, take [bounded arithmetic](/A2CFPP8JMN/), [$\mathsf{I}\Delta_0$ and the linear-time hierarchy](/FYGWNXETVJ/), [Parikh's theorem](/YPQPC1WJMV/), [Buss's witnessing theorem](/RH4R7GTTAX/), the [Paris–Wilkie translation](/ZVD982MVST/) and [pigeonhole principles in bounded arithmetic](/NJ18EZ5JBC/). The proof of the witnessing theorem uses free-cut elimination; it is enough at first to follow how an induction step becomes a step of a polynomial-time algorithm.

[Cook's PV](/FMM44KFZQT/) and the [Krajíček–Pudlák–Takeuti theorem](/YP7KE8E6DC/) can wait for a second pass, and [approximate counting](/65K2S22DGZ/) is the most technical entry of the chapter.

## Before you start

The chapter on [formal arithmetic and its fragments](/QHCRN4JVG0/) has the background: [weak theories of arithmetic](/Q5MT8WY7JM/), [Robinson arithmetic](/3K1AKGXF8A/), the classes of [$\Delta_0$, $\Sigma_n$ and $\Pi_n$ formulas](/GE43CSZTS9/), [elementary function arithmetic](/2JD80TE553/) and [primitive recursive arithmetic](/WCXH72T8D8/). [Self-verifying theories](/D8SGFVA3RT/) and [Gödel's speed-up theorem](/37X5XBDBNX/) touch the same questions. The witnessing proofs use the [sequent calculus](/W72CA3R9MP/) and [cut elimination](/AYRZ98Y0NW/). For the complexity side, you need the classes [P](/GVT2NKN37K/) and [NP](/QQRA9GBW51/), the [Cook–Levin theorem](/CTK8AH98Z1/) and [Boolean circuits](/SQXNFGVADX/).
