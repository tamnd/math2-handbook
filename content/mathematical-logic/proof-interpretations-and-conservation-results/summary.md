## What to remember

- **Double-negation translations.** The Gödel–Gentzen [translation](/HGJVM49PA4/) $A^N$ puts $\neg\neg$ in front of atoms and replaces $A \vee B$ and $\exists x\, A$ by $\neg(\neg A^N \wedge \neg B^N)$ and $\neg \forall x\, \neg A^N$. Then $\Gamma \vdash A$ classically if and only if $\Gamma^N \vdash A^N$ intuitionistically, and $\mathsf{PA} \vdash A$ if and only if $\mathsf{HA} \vdash A^N$. The translations of Kolmogorov and Kuroda are intuitionistically equivalent to it.
- **The [A-translation](/6CCK0TT69P/)** replaces each atom $P$, including $\bot$, by $P \vee A$, and HA proves $B^A$ whenever it proves $B$. With $A$ the conclusion $\exists y\, \varphi$ itself, it removes the double negation from $\neg\neg \exists y\, \varphi$ for quantifier-free $\varphi$. So **PA is [$\Pi^0_2$-conservative over HA](/PY679V9MVR/)**, but not $\Pi^0_3$-conservative.
- **[System T](/A4WR995XZP/)** is the simply typed lambda calculus with $0$, $S$ and recursors $R_\sigma$ at every type, where $\N$ is the base type of numbers. Its closed terms are strongly normalizing, and its closed terms of type $\N \to \N$ define exactly the provably total functions of PA. The [Ackermann function](/N470JF7ZJX/) needs only the recursor at type $\N \to \N$.
- **The [Dialectica interpretation](/HZ17ES9PDY/)** sends $A$ to $\exists x\, \forall y\, A_D(x, y)$ with $A_D$ quantifier-free. If HA proves $A$, then T has terms $t$ with $\mathsf{T} \vdash A_D(t, y)$. Combined with the negative translation, it reduces the consistency of PA to that of T.
- **The [no-counterexample interpretation](/4BCD1EM542/)** reads $\exists x\, \forall y\, \varphi(x, y)$ as $\forall f\, \exists x\, \varphi(x, f(x))$. Every theorem of PA has n.c.i. functionals that are $\alpha$-recursive for some $\alpha < \varepsilon_0$.
- **[Bar recursion](/8CCG6F2FAT/)** stops a recursion on finite sequences when a continuous functional says the sequence is long enough. By [Spector's theorem](/DSQJ1RA71N/), T with bar recursion interprets classical analysis.
- **[Proof mining](/XR1JXQG1CD/)** extracts bounds and rates from proofs, mainly with the monotone Dialectica interpretation and Howard's majorizability. For theorems of the form $\forall \exists \forall$, such as convergence, the extractable content is a **rate of metastability**.
- **[Parsons's theorem](/2VYJXZZDGB/):** $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over PRA, so its provably total functions are the primitive recursive ones. [Herbrand analysis](/MESZ87G9ET/) proves it: after partial cut elimination, induction becomes primitive recursion and cut becomes composition.
- **[Interpretability](/8H03GRMDYG/).** If $S$ interprets $T$ and $S$ is consistent, then $T$ is consistent. For consistent recursively axiomatized extensions of PA in the language of PA, $S \rhd T$ holds exactly when every $\Pi_1$ theorem of $T$ is provable in $S$ (Orey–Hájek). PA interprets $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ but not $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.

## Main conservation results

| Stronger theory | Weaker theory | Class of sentences | Method |
|---|---|---|---|
| $\mathsf{PA}$ | $\mathsf{HA}$ | $\Pi^0_2$ | negative translation and A-translation |
| $\mathrm{I}\Sigma_1$ | $\mathsf{PRA}$ | $\Pi^0_2$ | Herbrand analysis |
| $\mathsf{WKL}_0$ | $\mathsf{PRA}$ | $\Pi^0_2$ | models, or Herbrand analysis |
| $\mathsf{WKL}_0$ | $\mathsf{RCA}_0$ | $\Pi^1_1$ | models |
| $\mathsf{ACA}_0$ | $\mathsf{PA}$ | arithmetic sentences | models |

: Five [conservation theorems](/TNZ995J8AP/). Each row says that the theory on the left proves no sentence of the third class that the theory in the second column does not already prove.

## Common errors

- **Putting the double negation only in front.** For predicate logic, $\neg\neg A$ is not a double-negation translation of $A$: the classical theorem $\forall x\, (P(x) \vee \neg P(x))$ has no intuitionistic proof of its double negation. The negations must go inside, under the quantifiers.
- **Replacing only $\bot$ in the A-translation.** The atoms must become $P \vee A$ too; otherwise ex falso is not preserved. HA proves $\bot \to 0 = 1$, but replacing $\bot$ by $0 = 0$ gives $0 = 0 \to 0 = 1$, which HA does not prove.
- **Expecting a computable witness for every classical $\forall \exists \forall$ theorem.** The Dialectica and no-counterexample interpretations give functionals that refute counterexamples, not Skolem functions. For a Specker sequence no computable rate of convergence exists, but a rate of metastability does.
- **Reading conservation as equality.** A theory that is $\Pi^0_2$-conservative over another may prove more $\Pi^0_3$ sentences, and its proofs may be much shorter.
- **Confusing interpretability with soundness.** $\mathsf{PA} \rhd \mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$ does not mean that PA proves anything false. It means that a translation of the language, defined inside PA, turns every axiom of the larger theory into a theorem of PA.
- **Applying bar recursion in the full type structure.** Bar recursion is not well defined on all set-theoretic functionals; it needs a model where the functionals are continuous or majorizable, such as the continuous functionals.
