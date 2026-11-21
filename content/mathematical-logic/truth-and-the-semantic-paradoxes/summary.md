## What to remember

- **The liar.** The diagonal lemma gives $\lambda$ with $\mathsf{Q} \vdash \lambda \leftrightarrow \neg T(\ulcorner \lambda \urcorner)$, so $\mathsf{Q}$ with every instance of $T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ is inconsistent. The derivation is valid in intuitionistic logic too.
- **Tarski.** A definition of truth for $L$ is materially adequate when it implies every T-sentence of $L$. It can be given in a richer metalanguage, for example truth for arithmetic in $\mathsf{ZF}$, but not in $L$ itself. The hierarchy $\mathcal{L}_{n+1} = \mathcal{L}_n \cup \set{T_n}$ gives each level a truth predicate for the level below.
- **Kripke.** The strong Kleene jump on partial interpretations $(E, A)$ is monotone. Its stages from $(\emptyset, \emptyset)$ reach the least fixed point at a countable ordinal, and in every fixed point $T(\ulcorner \varphi \urcorner)$ and $\varphi$ have the same value. A sentence is grounded when it has value $1$ or $0$ in the least fixed point.
- **Revision.** Each stage is a classical hypothesis, $S_{\zeta + 1} = \rho(S_\zeta)$, and at limits the stably-in and stably-out sentences keep their status. A sentence is categorically true when it is stably true in every revision sequence. The rule $\rho$ is not monotone and has no fixed point.
- **Gaps and gluts.** In strong Kleene logic $K_3$ no sentence is valid. In $\mathrm{LP}$ every classical tautology is valid, but explosion, disjunctive syllogism and modus ponens for the material conditional fail.
- **Relatives of the liar.** The Berry and Grelling-Nelson paradoxes refute the naive schemas for definability and satisfaction. The Yablo sentences give a consistent but $\omega$-inconsistent theory, and every finite variant is consistent. A knowledge predicate with factivity and necessitation over $\mathsf{Q}$ is inconsistent.
- **Axiomatic theories.** $\mathsf{TB}$, $\mathsf{UTB}$ and $\mathsf{CT}^-$ are conservative over $\mathsf{PA}$. $\mathsf{CT}$, with induction for all of $\mathcal{L}_T$, proves global reflection and $\mathrm{Con}(\mathsf{PA})$, and it has the arithmetical theorems of $\mathsf{ACA}$. $\mathsf{KF}$ has the strength of ramified analysis below $\varepsilon_0$, and every Kripke fixed point gives a standard model of it.
- **McGee's theorem.** A classical theory over $\mathsf{Q}$ with NEC, $T\ulcorner \neg \varphi \urcorner \to \neg T\ulcorner \varphi \urcorner$ and the $\forall$-introduction axiom (U) is $\omega$-inconsistent. So $\mathsf{FS}$ is consistent but has no standard model.
- **Sorites.** Ten thousand grains make a heap, one grain does not, and the $9999$ tolerance conditionals give a contradiction. Epistemicism puts a sharp boundary at an unknown point, supervaluation makes the universal premise super-false with no single conditional false, and degree theories give each conditional a value just below $1$.

## The liar in each approach

| Approach | Logic at each point | What holds of $T$ | Status of the liar $\lambda$ |
|---|---|---|---|
| [Tarskian hierarchy](/Z6MCGB0ZFX/) | classical | $T_n(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for $\varphi$ in $\mathcal{L}_n$ | no $T_n$ applies to its own level; a liar for $T_1$ lies in $\mathcal{L}_2$ and is true |
| [Kripke fixed points](/ES71QTSTNV/) | strong Kleene | $T(\ulcorner \varphi \urcorner)$ and $\varphi$ have equal values | value $\mathrm{u}$ in every fixed point |
| LP fixed points | $\mathrm{LP}$ | equal values | value $\mathrm{b}$ in every fixed point |
| FDE fixed points | first-degree entailment | equal values | $\mathbf{B}$ or $\mathbf{N}$, and both occur |
| [Revision theory](/ZQ4TWM7K6E/) | classical | T-sentences hold across one step | unstable in every revision sequence |
| [$\mathsf{KF}$](/2F15E76R0Z/) | classical | Kripke's compositional clauses | $\mathsf{KF} \vdash T\ulcorner \lambda \urcorner \leftrightarrow T\ulcorner \neg \lambda \urcorner$; with $\mathsf{Cons}$ it proves $\lambda \wedge \neg T\ulcorner \lambda \urcorner$ |

: How six treatments of truth classify the liar. In each semantics with three or four values the liar takes a value $v$ with $v = \neg v$, and the logic decides which value that is.

## Common errors

- **Reading "gap" as a solution.** The strengthened liar says of itself that it is not true. A gap is not true, so in Kripke's theory the claim that $\lambda$ is a gap cannot be stated truly in the language; this is the revenge problem.
- **Confusing stable with true at some stage.** In the revision theory the liar is true at infinitely many stages and stable in no sequence. The truth-teller is stable in every sequence and categorical in none.
- **Treating the truth-teller like the liar.** Both are ungrounded, but the liar has no consistent classical value and the truth-teller has two. In Kripke's theory the liar is a gap in every fixed point, the truth-teller only in some.
- **Taking conservative to mean weak.** $\mathsf{CT}^-$ proves no new arithmetical sentences, yet it proves generalizations about truth that $\mathsf{TB}$ cannot prove.
- **Expecting McGee's theorem to give inconsistency.** It gives $\omega$-inconsistency only, as the formal Yablo argument does.
