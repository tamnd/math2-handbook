## What to remember

- **[$\mathsf{I}\Delta_0$](/A2CFPP8JMN/)** is Robinson arithmetic with induction for bounded formulas. It does not prove that $2^x$ is total. By [Parikh's theorem](/YPQPC1WJMV/), if it proves $\forall x\, \exists y\, \varphi(x, y)$ with $\varphi$ bounded, then it proves $\forall x\, \exists y \le t(x)\, \varphi(x, y)$ for a term $t$, which is a polynomial.
- **[$\Delta_0$-definable sets](/FYGWNXETVJ/)** are exactly the sets in the linear-time hierarchy, the class also called the rudimentary sets. They include the primes, the perfect squares and the powers of $2$, and they are all decidable in linear space.
- **Buss's language** adds $\abs{x} = \ceil{\log_2(x + 1)}$, $\floor{x/2}$ and $x \mathbin{\#} y = 2^{\abs x \abs y}$. A **sharply bounded** quantifier has a bound of the form $\abs t$. The class $\Sigma^b_i$ counts the alternations of bounded quantifiers and ignores the sharply bounded ones; $\Sigma^b_i$ sets are exactly the $\Sigma^p_i$ sets of the [polynomial hierarchy](/TDQ7AXGM6P/).
- **$S^i_2$ and $T^i_2$** have length induction (PIND) and ordinary induction for $\Sigma^b_i$ formulas. They form the chain $S^1_2 \subseteq T^1_2 \subseteq S^2_2 \subseteq T^2_2 \subseteq \cdots$, and the union $S_2$ equals $T_2$.
- **[Buss's witnessing theorem](/RH4R7GTTAX/):** the $\Sigma^b_1$-definable functions of $S^1_2$ are the polynomial-time functions. More generally, those of $S^i_2$ are the functions in $\mathrm{FP}^{\Sigma^p_{i-1}}$, and $S^{i+1}_2$ is $\forall\exists\Sigma^b_{i+1}$-conservative over $T^i_2$.
- **[Cook's PV](/FMM44KFZQT/)** is an equational theory with a symbol for each function defined by limited recursion on notation, that is, for each polynomial-time function. The theory $S^1_2$, with the symbols of PV added, is $\forall\Sigma^b_1$-conservative over the first-order version $\mathsf{PV}_1$.
- **[KPT](/YP7KE8E6DC/):** a $\forall\exists\forall$ theorem of $\mathsf{PV}_1$ has a witness found by a student–teacher game with a constant number of rounds. If $T_2$ were finitely axiomatized, or if $T^i_2 = S^{i+1}_2$, the polynomial hierarchy would collapse.
- **[Paris–Wilkie translation](/ZVD982MVST/):** a $\Delta_0(\alpha)$ formula becomes a family of propositional formulas of constant depth and polynomial size. Proofs in $\mathsf{I}\Delta_0(\alpha)$ become polynomial-size proofs of constant depth. Since constant-depth proofs of the pigeonhole formulas must have superpolynomial size (Ajtai), $\mathsf{I}\Delta_0(\alpha)$ does not prove the [pigeonhole principle](/NJ18EZ5JBC/) for $\alpha$.
- **[Approximate counting](/65K2S22DGZ/):** $\mathsf{APC}_1 = \mathsf{PV}_1 + \mathrm{dWPHP}(\mathsf{PV})$ assigns approximate sizes to sets given by circuits, with relative error $\varepsilon$ of the ambient interval.

## Theories and their functions

| Theory | Induction | Definable functions or search problems | Class |
|---|---|---|---|
| $\mathsf{I}\Delta_0$ | bounded formulas | witnesses bounded by polynomials (Parikh) | linear-time hierarchy, for the definable sets |
| $\mathsf{PV}_1$ | open formulas of PV | polynomial-time functions | P |
| $S^1_2$ | PIND for $\Sigma^b_1$ | $\Sigma^b_1$-definable functions: polynomial time | P |
| $T^1_2$ | IND for $\Sigma^b_1$ | $\Sigma^b_1$-definable search problems: polynomial local search | PLS |
| $S^i_2$ | PIND for $\Sigma^b_i$ | $\Sigma^b_i$-definable functions: $\mathrm{FP}^{\Sigma^p_{i-1}}$ | $\Delta^p_i$ |

: The main theories of the chapter, with their induction and the complexity classes of their definable functions or search problems.

## Common errors

- **Confusing bounded with sharply bounded.** $\forall y \le x$ is bounded but not sharply bounded, and it counts in $\Sigma^b_i$; $\forall i \le \abs x$ is sharply bounded and does not.
- **Thinking $\#$ gives exponentiation.** The term $x \mathbin{\#} x$ is about $x^{\abs x}$, which is quasi-polynomial, not exponential; no term of the language grows like $2^x$.
- **Reading Parikh's theorem as a statement about all formulas.** The formula $\varphi$ must be bounded. A theorem $\forall x\, \exists y\, \psi$ with unbounded $\psi$ gives no polynomial bound on $y$.
- **Expecting a separation from P $\ne$ NP.** It is not known that $\mathrm{P} \ne \mathrm{NP}$ implies $S^1_2 \ne T^1_2$, and no separation of the theories is known for $i \ge 1$. The known implications run from collapses of the theories to collapses of complexity classes.
- **Taking the Paris–Wilkie translation of an unbounded formula.** The translation is defined only for bounded formulas; an unbounded existential quantifier would need an infinite disjunction.
- **Treating approximate counts as exact.** A one-element set is approximately of size $0$ once the error $\varepsilon 2^n$ is at least $1$, so approximate counting cannot tell an empty set from a non-empty one.
