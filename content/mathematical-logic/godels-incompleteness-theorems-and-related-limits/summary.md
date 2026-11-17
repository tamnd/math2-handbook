## What to remember

- **Arithmetization.** Under a [Gödel numbering](/MFJXPAF0R0/), the sets of codes of formulas, sentences and axioms of $\mathsf{Q}$ or $\mathsf{PA}$ are primitive recursive, and so is the relation $\mathrm{Prf}_T(y, x)$, "$y$ codes a $T$-proof of the formula coded by $x$", whenever the axioms of $T$ form a decidable set. The [provability predicate](/NB2BCZR40F/) $\mathrm{Prov}_T(x) := \exists y\, \mathrm{Prf}_T(y, x)$ is $\Sigma_1$, and $T \vdash \varphi$ implies $\mathsf{Q} \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
- **[Diagonal lemma](/3PRW76471J/).** For every formula $\varphi(x)$ with one free variable there is a sentence $\delta$ with $\mathsf{Q} \vdash \delta \leftrightarrow \varphi(\ulcorner \delta \urcorner)$.
- **[First incompleteness theorem](/X9WYNYE29C/).** Let $T \supseteq \mathsf{Q}$ have a computably enumerable set of axioms, and let $T \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$. If $T$ is consistent, then $T \nvdash G$. If $T$ is [$\omega$-consistent](/4S29X1GTV4/), then also $T \nvdash \neg G$. [Rosser's theorem](/DH9RQ61GVD/) gives an undecided sentence from consistency alone.
- **[Second incompleteness theorem](/4PZM5GJTR5/).** If $T \supseteq \mathsf{PA}$ is consistent and its axioms are given by a $\Sigma_1$ formula, then $T \nvdash \mathrm{Con}(T)$, where [$\mathrm{Con}(T)$](/4NBAX3VRQ7/) is $\neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$. The proof uses the [derivability conditions](/F6H4STF9RG/) D1–D3.
- **[Tarski's theorem](/YRV6SYK2BY/).** No formula $\mathrm{True}(x)$ satisfies $\N \models \mathrm{True}(\ulcorner \varphi \urcorner) \iff \N \models \varphi$ for every sentence $\varphi$. For each $n \ge 1$, though, truth for $\Sigma_n$ sentences is defined by a $\Sigma_n$ formula, a [partial truth predicate](/Y2MF1EZAM7/).
- **[Löb's theorem](/3HD30YG3DG/).** For $T \supseteq \mathsf{PA}$ as above, if $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$, then $T \vdash \varphi$. The case $\varphi := (0 = S0)$ is the second incompleteness theorem, and a [Henkin sentence](/SBMQ5QHG9W/), one with $T \vdash H \leftrightarrow \mathrm{Prov}_T(\ulcorner H \urcorner)$, is provable.
- **[Reflection](/NB485KFXKV/).** Over $T$, $\mathrm{Con}(T)$ is equivalent to reflection for $\Pi_1$ sentences. Uniform reflection is much stronger: $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ has the same theorems as $\mathsf{PA}$. Iterating reflection along ordinal notations reaches every true sentence, but only along paths through a set that is not arithmetical.
- **[Speed-up](/37X5XBDBNX/).** For $T \supseteq \mathsf{PA}$ consistent and every computable $f$, infinitely many theorems $\psi$ of $T$ have proofs in $T + \mathrm{Con}(T)$ of some length $n$ but no proof in $T$ of length at most $f(n)$.

## The theorems side by side

| Theorem | Hypotheses on $T$ | Conclusion |
|---|---|---|
| [Gödel's first](/X9WYNYE29C/) | c.e. axioms, $T \supseteq \mathsf{Q}$, $\omega$-consistent | neither $G$ nor $\neg G$ is provable |
| [Rosser's](/DH9RQ61GVD/) | c.e. axioms, $T \supseteq \mathsf{Q}$, consistent | the Rosser sentence is undecided |
| [Gödel's second](/4PZM5GJTR5/) | $\Sigma_1$ axiom formula, $T \supseteq \mathsf{PA}$, consistent | $T \nvdash \mathrm{Con}(T)$ |
| [Löb's](/3HD30YG3DG/) | $\Sigma_1$ axiom formula, $T \supseteq \mathsf{PA}$ | $T \vdash \square\varphi \to \varphi$ only if $T \vdash \varphi$ |
| [Tarski's](/YRV6SYK2BY/) | none: it is about the structure $\N$ | truth in $\N$ is not definable in $\N$ |
| [Speed-up](/37X5XBDBNX/) | decidable axioms, $T \supseteq \mathsf{PA}$, consistent | $T + \mathrm{Con}(T)$ shortens proofs beyond every computable bound |

: The main limits on formal theories of arithmetic. For the second theorem and Löb's theorem, $\mathsf{PA}$ can be replaced by any theory that proves the derivability conditions for its provability predicate.

## Common errors

- **"Some truths can never be proved."** The first theorem is about one theory at a time. For $T \supseteq \mathsf{PA}$, the Gödel sentence of $T$ is provable in $T + \mathrm{Con}(T)$; what no single consistent c.e. theory does is prove all truths.
- **Dropping a hypothesis.** True arithmetic is complete, because its axioms are not c.e. Presburger arithmetic and the theory of real closed fields are complete and decidable, because they do not contain $\mathsf{Q}$.
- **Reading $T \vdash \mathrm{Prov}_T(\ulcorner\varphi\urcorner)$ as $T \vdash \varphi$.** They agree when $T$ is $\Sigma_1$-sound. $\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$ proves $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$, and it is consistent if $\mathsf{PA}$ is.
- **Ignoring how $\mathrm{Con}(T)$ is written.** The second theorem holds for the standard predicate with a $\Sigma_1$ axiom formula. With Feferman's $\Pi_1$ formula $\alpha^*$ for the axioms of $\mathsf{PA}$, or with the Rosser predicate, $\mathsf{PA}$ proves the resulting consistency sentence.
- **Concluding that $T$ might be inconsistent.** The second theorem says that $T$ cannot prove its own consistency, not that the consistency is in doubt. $\mathrm{Con}(\mathsf{PA})$ is provable in $\mathsf{ZFC}$, and by Gentzen in $\mathsf{PRA}$ with quantifier-free induction up to $\varepsilon_0$.
