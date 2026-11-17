## What to remember

- The **[language of arithmetic](/D8SD54M5PN/)** has $0$, $S$, $+$, $\cdot$ and $<$. The numeral $\overline n$ is $S$ applied $n$ times to $0$. Every number has a name, but a model of a theory in this language may have elements that no numeral names.
- **[Robinson arithmetic](/3K1AKGXF8A/)** $\mathsf{Q}$ has finitely many axioms and no induction. It proves every true equation between closed terms, but not general laws such as $\forall x\, (0 + x = x)$ or $\forall x\, \forall y\, (x + y = y + x)$. It is essentially undecidable, and so is the weaker, infinitely axiomatized theory [$\mathsf{R}$](/Q5MT8WY7JM/).
- **[Peano arithmetic](/HACXBCM7SS/)** is $\mathsf{Q}$ plus the induction schema $\varphi(0) \land \forall x\,(\varphi(x) \to \varphi(Sx)) \to \forall x\, \varphi(x)$, one axiom for each formula $\varphi$. It is [not finitely axiomatizable](/M5WNB181T7/).
- **Formula classes.** A $\Delta_0$ formula has only bounded quantifiers $\forall x < t$, $\exists x < t$, with $x$ not in $t$. A $\Sigma_n$ formula is $n$ alternating blocks of unbounded quantifiers, starting with $\exists$, in front of a $\Delta_0$ formula. In $\N$, the [$\Sigma_1$ formulas](/GE43CSZTS9/) define exactly the computably enumerable relations.
- **[$\Sigma_1$-completeness](/69234Z1V00/).** $\mathsf{Q}$ proves every true $\Sigma_1$ sentence and decides every $\Delta_0$ sentence. So a consistent extension of $\mathsf{Q}$ proves no false $\Pi_1$ sentence.
- **[Representability](/BJF29XET83/).** Every recursive function $f$ has a formula $\varphi(\bar x, y)$ with $\mathsf{Q} \vdash \forall y\, (\varphi(\overline{\bar n}, y) \leftrightarrow y = \overline{f(\bar n)})$ for all $\bar n$. The proof codes finite sequences by [Gödel's $\beta$-function](/BM6P0C2AC2/) $\beta(c, d, i) = c \bmod (1 + (i+1)d)$.
- **[Fragments](/T70PYM1F36/).** $\mathrm{I}\Sigma_n$ is $\mathsf{Q}$ (or a base theory of the same strength) plus induction for $\Sigma_n$ formulas. The chain $\mathrm{I}\Delta_0 \subsetneq \mathrm{I}\Sigma_1 \subsetneq \mathrm{I}\Sigma_2 \subsetneq \cdots$ is strict, its union is $\mathsf{PA}$, and $\mathrm{I}\Sigma_n$ and $\mathrm{I}\Pi_n$ prove the same sentences.
- **[True arithmetic](/DX0KPMH4QZ/)** $\mathrm{Th}(\N, 0, S, +, \cdot, <)$ is complete and consistent, but it is not computably enumerable and not even definable in $\N$.

## Theories of arithmetic side by side

| Theory | Induction | Provably total functions | Ordinal |
|---|---|---|---|
| [$\mathrm{I}\Delta_0$](/T70PYM1F36/) | $\Delta_0$ formulas | bounded by polynomials | $\omega^2$ |
| [$\mathsf{EFA}$](/2JD80TE553/) | $\Delta_0$ formulas, with $\exp$ | elementary | $\omega^3$ |
| [$\mathsf{PRA}$](/WCXH72T8D8/) | a rule for quantifier-free formulas | primitive recursive | $\omega^\omega$ |
| $\mathrm{I}\Sigma_1$ | $\Sigma_1$ formulas | primitive recursive | $\omega^\omega$ |
| [$\mathsf{PA}$](/HACXBCM7SS/) | all formulas | recursive in ordinals below $\varepsilon_0$ | $\varepsilon_0$ |

: Fragments of arithmetic, ordered by strength. $\mathrm{I}\Sigma_1$ proves more sentences than $\mathsf{PRA}$ but the same $\Pi_2$ sentences, so they share their provably total functions and their ordinal.

## Common errors

- **Expecting $\mathsf{Q}$ to prove general laws.** $\mathsf{Q}$ proves $\overline 2 + \overline 3 = \overline 3 + \overline 2$ but not $\forall x\, \forall y\, (x + y = y + x)$. To show it does not prove a sentence, build a non-standard model in which the sentence fails.
- **Confusing truth in $\N$ with provability.** A formula can define a set in $\N$ without representing it in $\mathsf{Q}$. $\mathsf{PA}$ proves every true $\Sigma_1$ sentence but not every true $\Pi_1$ sentence; the consistency of $\mathsf{PA}$ is a true $\Pi_1$ sentence it does not prove.
- **Using a bound that contains the bound variable.** $\exists x < x + 1$ is not a bounded quantifier.
- **Classifying by appearance only.** A formula with an unbounded $\exists$ inside a bounded $\forall$ is not $\Sigma_1$ as written, though in $\N$ (and in $\mathrm{I}\Sigma_1$) it is equivalent to one.
- **Mixing up the schema and the axiom.** First-order induction is a schema with one instance per formula. The second-order induction axiom, quantifying over all subsets, is a single sentence with a different meaning.
