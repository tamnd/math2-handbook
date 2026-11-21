## What to remember

- **[Second-order arithmetic](/DC60FYCSPM/)** has number variables and set variables. Reals, continuous functions, complete separable metric spaces and countable algebraic structures are all coded by sets of numbers, so theorems about them become sentences of the language.
- **[Reverse mathematics](/7SQS69T17R/)** proves equivalences over the weak base theory [$\mathsf{RCA}_0$](/XQENB067R3/), which has $\Delta^0_1$ comprehension and $\Sigma^0_1$ induction. The theorem is proved from the axiom, and the axiom from the theorem.
- **The big five** are $\mathsf{RCA}_0$, [$\mathsf{WKL}_0$](/7W9EG02T79/) (weak König's lemma), [$\mathsf{ACA}_0$](/NAASTN80QN/) (arithmetical comprehension), [$\mathsf{ATR}_0$](/MKB74TX3Z8/) (arithmetical transfinite recursion) and [$\Pi^1_1\text{-}\mathsf{CA}_0$](/T21WETAHN5/). Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to the existence of the Turing jump of every set and to the existence of the [range of every injection](/3MQ39PRCYJ/).
- **$\omega$-models** of $\mathsf{RCA}_0$ are exactly the [Turing ideals](/Y6D27XJT3H/). The computable sets form the least $\omega$-model of $\mathsf{RCA}_0$ and the arithmetical sets that of $\mathsf{ACA}_0$. The intersection of all $\omega$-models of $\mathsf{WKL}_0$ is the class of computable sets, and the intersection of all $\omega$-models of $\mathsf{ATR}_0$ is the class of hyperarithmetical sets, which is not itself a model of $\mathsf{ATR}_0$.
- **[$\beta$-models](/J0Z2GNJZ2W/)** are $\omega$-models that are correct for $\Sigma^1_1$ statements, and so for well-foundedness. Over $\mathsf{ACA}_0$, $\Pi^1_1\text{-}\mathsf{CA}_0$ is equivalent to the statement that every set lies in a countable coded $\beta$-model.
- **First-order strength:** $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$ have the first-order part $\mathrm{I}\Sigma_1$, $\mathsf{ACA}_0$ has that of PA, and $\mathsf{WKL}_0$ is $\Pi^0_2$-conservative over PRA. This is the [partial realization of Hilbert's program](/Z26S516BKH/).
- **[Ramsey's theorem for pairs](/ZT5KV6KJ3E/)** $\mathsf{RT}^2_2$ is provable in $\mathsf{ACA}_0$, does not imply $\mathsf{ACA}_0$ (Seetapun and Slaman) and does not imply $\mathsf{WKL}_0$ (Liu). For exponents $n \ge 3$ and $k \ge 2$ colours, $\mathsf{RT}^n_k$ is equivalent to $\mathsf{ACA}_0$.
- **The [zoo](/E3X5B175ZR/)** holds the principles between the main systems, such as $\mathsf{SRT}^2_2$, $\mathsf{COH}$, $\mathsf{CAC}$, $\mathsf{ADS}$ and [$\mathsf{WWKL}_0$](/KPHM3025GW/). $\mathsf{WWKL}_0$ says that every binary tree of positive measure has a path, and it is the system of basic measure theory.
- **[Predicativity](/43BSXNWQBG/):** in the analysis of Feferman and Schütte, the limit of predicative mathematics is $\Gamma_0$, the proof-theoretic ordinal of $\mathsf{ATR}_0$.

## The big five

| System | Main axiom | Typical equivalent | First-order part | Ordinal |
|---|---|---|---|---|
| $\mathsf{RCA}_0$ | $\Delta^0_1$ comprehension | intermediate value theorem | $\mathrm{I}\Sigma_1$ | $\omega^\omega$ |
| $\mathsf{WKL}_0$ | weak König's lemma | Heine–Borel for $[0, 1]$ | $\mathrm{I}\Sigma_1$ | $\omega^\omega$ |
| $\mathsf{ACA}_0$ | arithmetical comprehension | Bolzano–Weierstrass | $\mathsf{PA}$ | $\varepsilon_0$ |
| $\mathsf{ATR}_0$ | arithmetical transfinite recursion | comparability of well-orderings | stronger than PA | $\Gamma_0$ |
| $\Pi^1_1\text{-}\mathsf{CA}_0$ | $\Pi^1_1$ comprehension | Cantor–Bendixson theorem | stronger still | $\psi_0(\Omega_\omega)$ |

: The five main subsystems with one theorem each that is equivalent to the system over $\mathsf{RCA}_0$ (for $\mathsf{RCA}_0$ itself, one that it proves), the arithmetic sentences they prove, and their proof-theoretic ordinals ($\psi_0(\Omega_\omega)$ in Buchholz's notation).

## Common errors

- **Working over a strong base.** An equivalence proved over $\mathsf{ACA}_0$ says nothing about which of the weaker systems a theorem needs. The base theory must be weaker than both sides; normally it is $\mathsf{RCA}_0$.
- **Forgetting the induction.** $\mathsf{RCA}_0$ has $\Sigma^0_1$ induction only. A proof that uses induction on an arithmetical formula, or a definition by recursion of a set, may need more than the stated system.
- **Confusing $\omega$-models with all models.** That the computable sets are an $\omega$-model of $\mathsf{RCA}_0$ but not of $\mathsf{WKL}_0$ shows non-provability. A theory with an $\omega$-model can still have models with nonstandard numbers, where other things hold.
- **Reading "lies outside the big five" as "strong".** $\mathsf{RT}^2_2$ is strictly weaker than $\mathsf{ACA}_0$, and its first-order part is between $\mathrm{B}\Sigma_2$ and $\mathrm{I}\Sigma_2$; it is incomparable with $\mathsf{WKL}_0$.
- **Ignoring the coding.** Statements about uncountable objects, such as arbitrary open covers or all subsets of the reals, cannot be stated directly. The usual versions are about countable covers, coded continuous functions and countable structures.
- **Treating $\mathsf{ATR}_0$ as predicative.** Its proof-theoretic ordinal is $\Gamma_0$, but its axiom is not predicatively justified in the autonomous sense; only the strength matches.
