## What to remember

- **Goodstein sequences and hydras end.** Write each term in hereditary base $k + 1$ and replace the base by $\omega$, or give each hydra the ordinal $\omega^{o(T_1)} \# \cdots \# \omega^{o(T_j)}$ of its root subtrees. Each step lowers an ordinal below $\varepsilon_0$. The numbers and trees themselves grow.
- **Paris-Harrington.** The [strengthened finite Ramsey theorem](/4P2BAT6YC3/) asks for a homogeneous set $Y$ with $\abs{Y} \ge m$ and $\abs{Y} \ge \min Y$. It follows from the infinite Ramsey theorem by compactness, and over $\mathsf{PA}$ it is equivalent to $1\text{-}\mathrm{Con}(\mathsf{PA})$. So $\mathsf{PA}$ does not prove it, and neither does $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
- **Each instance is provable.** For fixed parameters, the statements of this chapter are true $\Sigma_1$ sentences, and $\mathsf{PA}$ proves them by a finite computation. Only the sentence for all parameters is unprovable.
- **Provably total functions.** A $\Pi_2$ sentence $\forall x\, \exists y\, \varphi$ is unprovable in $T$ when its witness function eventually dominates every function that $T$ proves total. For $\mathrm{I}\Sigma_1$ these are the primitive recursive functions. For $\mathsf{PA}$ each is dominated by some $f_\alpha$ with $\alpha < \varepsilon_0$.
- **The three hierarchies.** They use the fundamental sequences $\omega^{\beta+1}[x] = \omega^\beta \cdot x$, $\omega^\lambda[x] = \omega^{\lambda[x]}$ and $\varepsilon_0[x+1] = \omega^{\varepsilon_0[x]}$, with $\varepsilon_0[0] = 0$. Then $f_{\alpha+1}(x) = f_\alpha^x(x)$, $H_{\alpha+1}(x) = H_\alpha(x+1)$ and $g_{\alpha+1}(x) = g_\alpha(x) + 1$, and each takes the value at $\lambda[x]$ at a limit $\lambda$. Two laws link them: $H_{\omega^\alpha} = f_\alpha$, and $g_\alpha(x)$ is $\alpha$ with $\omega$ replaced by $x$, for $\alpha < \varepsilon_0$.
- **Goodstein in numbers.** $L(m) = H_{o_2(m)}(3) - 2$, so $L(3) = 6$ and $L(4) = 3 \cdot 2^{402653211} - 2$.
- **Indicators.** An indicator $Y(a, b)$ is non-standard exactly when a cut of the given class separates $a$ from $b$. Paris and Harrington built one from their Ramsey statement for the cuts that are models of $\mathsf{PA}$.
- **Beyond $\mathsf{PA}$.** Friedman's finite Kruskal theorem escapes $\mathsf{ATR}_0$, the finite graph minor theorem escapes $\Pi^1_1\text{-}\mathsf{CA}_0$, and the Buchholz hydra escapes $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$.

## The statements and their theories

| Statement | Not provable in | Provable in |
|---|---|---|
| [Goodstein's theorem](/XQMNJF241J/) | $\mathsf{PA}$ | $\mathsf{PA}$ + transfinite induction up to $\varepsilon_0$ |
| [Kirby-Paris hydra](/C028FF4TWM/), standard battle | $\mathsf{PA}$ | $\mathsf{PA}$ + transfinite induction up to $\varepsilon_0$ |
| [Paris-Harrington](/509ZWA0R26/) $\mathrm{PH}$ | $\mathsf{PA}$, $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ | $\mathsf{PA} + 1\text{-}\mathrm{Con}(\mathsf{PA})$ |
| [Kanamori-McAloon](/NM5WYBK6BG/) | $\mathsf{PA}$ | second-order arithmetic |
| [Worm principle](/MHDZGDNEPS/) | $\mathsf{PA}$ | $\mathsf{PA} + 1\text{-}\mathrm{Con}(\mathsf{PA})$ |
| [Finite Kruskal](/12XRGBWH59/) $\forall n\, P(n)$ | $\mathsf{ATR}_0$ | $\Pi^1_1\text{-}\mathsf{CA}_0$ |
| [Finite graph minor](/WXNTPQGJ38/) | $\Pi^1_1\text{-}\mathsf{CA}_0$ | $\mathsf{ZFC}$ |
| [Buchholz hydra](/9APRFM0G7F/) | $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$ | $\mathsf{ZFC}$ |

: Eight [concrete incompleteness](/E2H655A7BS/) results. Each row gives a theory that does not prove the statement and one that does; every statement is true.

## Common errors

- **Taking "unprovable" for "unknown".** Every statement here is proved, in a stronger theory. Unprovability is always relative to a named theory.
- **Expecting a decreasing number.** In a Goodstein sequence or a hydra battle the numbers and trees grow for a long time. Only the ordinal decreases.
- **Mixing up consistency and $1$-consistency.** $\mathrm{PH}$ and the worm principle are equivalent to $1\text{-}\mathrm{Con}(\mathsf{PA})$. The plain $\mathrm{Con}(\mathsf{PA})$ is weaker and does not prove $\mathrm{PH}$.
- **Confusing $H_\alpha$ with $f_\alpha$.** $H_\omega(x) = 2x$ but $f_\omega(x) = f_x(x)$. The link is $H_{\omega^\alpha} = f_\alpha$, not $H_\alpha = f_\alpha$.
- **Forgetting the fundamental sequences.** Values such as $f_{\varepsilon_0}(2)$ or $g_{\varepsilon_0}(3)$ depend on the choice of $\lambda[x]$. The slow-growing hierarchy is very sensitive to it.
- **Dropping the size bound.** Without the bound $i + n$, the finite Kruskal and graph minor statements are false: stars with fewer and fewer leaves give bad sequences of any length.
