## What to remember

- **Ordinal analysis** of a theory $T$ has three parts: a natural primitive recursive notation system $(A, \prec)$; a lower bound, $T$ proves transfinite induction along each proper initial segment of $\prec$; and an upper bound, $T$ proves it for no primitive recursive well-order of larger type. The result is the [proof-theoretic ordinal](/C72RBH0CDR/) $\abs{T}$.
- **An [ordinal notation system](/7MBX59Y7N9/)** is a computable set with a computable well-order. Being computable is not enough: an order of type $\omega$ defined through proofs of $0 = 1$ is one that PA cannot prove well-founded. [Kleene's $\mathcal{O}$](/WHAP0K600D/) names every computable ordinal, but it is $\Pi^1_1$-complete and not totally ordered, so it is not a notation system.
- **[Epsilon nought](/KT50SMH3EC/)** is the least $\varepsilon$ with $\omega^\varepsilon = \varepsilon$, the supremum of $1, \omega, \omega^\omega, \ldots$. Cantor normal form names every smaller ordinal.
- **Gentzen:** PRA together with quantifier-free transfinite induction along $\varepsilon_0$ proves $\operatorname{Con}(\mathrm{PA})$ ([1936](/QPV0HNP22S/)). PA proves $\operatorname{TI}(a, \varphi)$ for each notation $a \prec \varepsilon_0$, by the jump $\varphi \mapsto \varphi^+$, but not for $\varepsilon_0$ itself ([1943](/ZE54ABPMJ0/)). So $\abs{\mathrm{PA}} = \varepsilon_0$.
- **The [ω-rule](/XAMKAB1BZM/)** derives $\forall x\, A(x)$ from all $A(\bar n)$. A PA-proof embeds with height $\omega + m$ and finite cut rank, each cut level removed costs one exponential, and the cut-free heights stay below $\varepsilon_0$.
- **[Veblen functions](/JQFAE9S2F4/):** $\varphi_0(\alpha) = \omega^\alpha$, $\varphi_{\gamma+1}$ enumerates the fixed points of $\varphi_\gamma$, and at limits one takes common fixed points. For $\alpha < \gamma$, $\varphi_\alpha(\beta) < \varphi_\gamma(\delta)$ if and only if $\beta < \varphi_\gamma(\delta)$. [$\Gamma_0$](/CNN7BK5YAW/) is the least $\gamma$ with $\varphi_\gamma(0) = \gamma$, the limit of predicative analysis.
- **Collapsing:** [$\psi(\alpha)$](/8S6CT4TMB7/) is the least ordinal not built from $0, 1, \omega, \Omega$ by the operations and by $\psi(\xi)$ for $\xi < \alpha$. It equals $\varepsilon_\alpha$ up to $\zeta_0$, then stays at $\zeta_0$ up to $\Omega$, and grows again from $\Omega + 1$: the uncountable $\Omega$ names $\zeta_0$. In [Buchholz's system](/E7WEFRMQTB/) only addition is used, $\psi_0(\alpha) = \omega^\alpha$ up to $\varepsilon_0$, $\psi_0(\Omega) = \varepsilon_0$ and $\psi_0(\Omega \cdot 2) = \varepsilon_1$.
- **[Iterated inductive definitions](/5VNT564Y2W/):** $\mathrm{ID}_1$ adds for each $X$-positive operator a least fixed point, with a closure axiom and a minimality scheme; positivity makes the operator monotone. $\mathrm{ID}_\nu$ iterates this along a well-order. These theories reduce [$\Pi^1_1$-comprehension](/2MGJJTSRFD/), and Buchholz's [Ω-rule](/5C4YBXQV15/) turns the minimality scheme into an infinitary rule that can be collapsed.

## Theories and their ordinals

| Theory | Proof-theoretic ordinal | Entry |
|---|---|---|
| $\mathrm{PRA}$, $\mathrm{I}\Sigma_1$ | $\omega^\omega$ | [proof-theoretic ordinal](/C72RBH0CDR/) |
| $\mathrm{PA}$, $\mathrm{ACA}_0$ | $\varepsilon_0 = \psi_0(\Omega)$ | [Gentzen's consistency proof](/QPV0HNP22S/) |
| $\mathrm{ACA}$ | $\varepsilon_{\varepsilon_0}$ | [proof-theoretic ordinal](/C72RBH0CDR/) |
| $\mathrm{ATR}_0$ | $\Gamma_0 = \varphi(1, 0, 0) = \psi_0(\Omega^\Omega)$ | [Feferman–Schütte ordinal](/CNN7BK5YAW/) |
| $\mathrm{ATR}$ | $\Gamma_{\varepsilon_0}$ | [proof-theoretic ordinal](/C72RBH0CDR/) |
| $\mathrm{ID}_1$, $\mathrm{KP}\omega$ | $\psi_0(\varepsilon_{\Omega + 1}) = \psi_0(\Omega_2)$ | [Bachmann–Howard ordinal](/QH3ENXFRSV/) |
| $\mathrm{ID}_\nu$ | $\psi_0(\varepsilon_{\Omega_\nu + 1})$ | [iterated inductive definitions](/5VNT564Y2W/) |
| $\Pi^1_1\text{-}\mathrm{CA}_0$, $\mathrm{ID}_{<\omega}$ | $\psi_0(\Omega_\omega)$ | [Π¹₁ comprehension](/2MGJJTSRFD/) |
| $\Pi^1_1\text{-}\mathrm{CA}$ | larger than $\psi_0(\Omega_\omega)$ | [Π¹₁ comprehension](/2MGJJTSRFD/) |
| $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$, $\mathrm{ID}_\omega$ | $\psi_0(\varepsilon_{\Omega_\omega + 1})$ | [Takeuti–Feferman–Buchholz ordinal](/NZWRK062WQ/) |
| $\mathrm{KPM}$ | a value of Rathjen's $\psi_\Omega$, built on a weakly Mahlo cardinal | [Rathjen's psi function](/M7D1HEJQVH/) |
| full second-order arithmetic | not known | [ordinal analysis](/C5E5TG8PGP/) |

: Theories in order of strength, with their ordinals in Buchholz's notation where the entries give it. A subscript $0$ means induction only for sets; full induction raises the ordinal, as the pairs $\mathrm{ACA}_0$ and $\mathrm{ACA}$, $\mathrm{ATR}_0$ and $\mathrm{ATR}$, $\Pi^1_1\text{-}\mathrm{CA}_0$ and $\Pi^1_1\text{-}\mathrm{CA}$ show.

## Common errors

- **Taking any computable well-order as a measure.** With artificial orders, even an order of type $\omega$ can escape a theory, and the ordinal would measure the coding, not the theory.
- **Reading $\abs{T} = \alpha$ as "$T$ proves that $\alpha$ is well-ordered".** $T$ proves induction along each initial segment below $\alpha$, as separate theorems. It does not prove the uniform statement for all $a \prec \alpha$, and it does not prove induction along $\alpha$ itself.
- **Equating the ordinal with strength.** $\mathrm{PA}$ and $\mathrm{PA} + \operatorname{Con}(\mathrm{PA})$ have the same ordinal $\varepsilon_0$. The ordinal measures one kind of consequence, not everything a theory proves.
- **Mixing collapsing systems.** The same term means different ordinals in different systems: $\psi(\Omega) = \zeta_0$ with exponentiation, but $\psi_0(\Omega) = \varepsilon_0$ in Buchholz's system; $\psi(\Omega \cdot 2) = \zeta_1$, but $\psi_0(\Omega \cdot 2) = \varepsilon_1$.
- **Assuming that collapsing functions are increasing.** $\psi$ and $\psi_0$ are only weakly increasing: they are constant on long intervals, such as $\psi_0(\alpha) = \varepsilon_0$ for $\varepsilon_0 \le \alpha \le \Omega$. They are not normal functions.
