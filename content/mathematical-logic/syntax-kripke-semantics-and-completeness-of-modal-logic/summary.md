## What to remember

- **Kripke semantics.** In a model $(W, R, V)$, $w \models \square\varphi$ if and only if $v \models \varphi$ for every $v$ with $w R v$, and $w \models \lozenge\varphi$ if and only if $v \models \varphi$ for some such $v$. A formula is valid on a frame when it is true at every world under every valuation; validity in one model is weaker.
- **Normal modal logics** contain all tautologies and $\mathrm{K}$: $\square(p \to q) \to (\square p \to \square q)$, and are closed under modus ponens, uniform substitution and necessitation, from $\vdash \varphi$ infer $\vdash \square\varphi$. Necessitation applies to theorems only: $p \to \square p$ is not a theorem of $\mathsf{K}$.
- **Correspondence.** On a frame, $\mathrm{T}$: $\square p \to p$ is valid iff $R$ is reflexive, $\mathrm{D}$: $\square p \to \lozenge p$ iff serial, $\mathrm{B}$: $p \to \square\lozenge p$ iff symmetric, $\mathrm{4}$: $\square p \to \square\square p$ iff transitive, and $\mathrm{5}$: $\lozenge p \to \square\lozenge p$ iff Euclidean.
- **The standard systems** satisfy $\mathsf{K} \subsetneq \mathsf{D} \subsetneq \mathsf{T} \subsetneq \mathsf{S4} \subsetneq \mathsf{S5}$ and $\mathsf{T} \subsetneq \mathsf{B} \subsetneq \mathsf{S5}$, while $\mathsf{T}$ and $\mathsf{K4}$ are incomparable, and so are $\mathsf{B}$ and $\mathsf{S4}$. Up to equivalence, $\mathsf{S4}$ has seven modalities without negation and $\mathsf{S5}$ has three: $p$, $\square p$ and $\lozenge p$.
- **Canonical model.** The worlds are the maximal $\Lambda$-consistent sets, and $\Gamma R^\Lambda \Delta$ iff $\set{\varphi : \square\varphi \in \Gamma} \subseteq \Delta$. By the [truth lemma](/NM4CB7QAYT/), $\varphi$ is true at $\Gamma$ iff $\varphi \in \Gamma$. If $\Lambda$ contains $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ or $\mathrm{5}$, then $R^\Lambda$ has the matching property, and [completeness](/FXTCKYR3AQ/) follows.
- **Filtration.** For $\Sigma$ closed under subformulas, merging the worlds that agree on $\Sigma$ and choosing a relation between the smallest and the largest filtration keeps the truth value of every formula of $\Sigma$, in at most $2^{\abs{\Sigma}}$ worlds. For transitive models, use the transitive filtration.
- **Finite model property and decidability.** $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$ refute each non-theorem $\varphi$ on a frame of their class with at most $2^{\abs{\operatorname{Sub}(\varphi)}}$ worlds. By [Harrop's theorem](/VSYQ1AZ9G7/), a finitely axiomatized normal logic with the finite model property is decidable.
- **Standard translation.** $\mathrm{ST}_x(\square\varphi) = \forall y\,(R(x, y) \to \mathrm{ST}_y(\varphi))$ makes each modal formula a first-order formula in two variables; validity on a frame becomes a $\Pi^1_1$ sentence, which for Löb's axiom has no first-order equivalent.
- **Complexity (Ladner).** Satisfiability is PSPACE-complete for $\mathsf{K}$, $\mathsf{D}$, $\mathsf{T}$, $\mathsf{K4}$ and $\mathsf{S4}$, and PSPACE-hard for every normal logic between $\mathsf{K}$ and $\mathsf{S4}$; for $\mathsf{S5}$ it is NP-complete.

## The standard logics side by side

| Logic | Axioms over $\mathsf{K}$ | Frames | Satisfiability |
|---|---|---|---|
| [$\mathsf{K}$](/D1TJYZZDCY/) | none | all frames | PSPACE-complete |
| [$\mathsf{D}$](/XVYMEZKH7R/) | $\mathrm{D}$ | serial | PSPACE-complete |
| [$\mathsf{T}$](/XVYMEZKH7R/) | $\mathrm{T}$ | reflexive | PSPACE-complete |
| [$\mathsf{K4}$](/XVYMEZKH7R/) | $\mathrm{4}$ | transitive | PSPACE-complete |
| [$\mathsf{S4}$](/N60RVXSA5W/) | $\mathrm{T}$, $\mathrm{4}$ | preorders | PSPACE-complete |
| [$\mathsf{B}$](/2QPT4KCM0Q/) | $\mathrm{T}$, $\mathrm{B}$ | reflexive and symmetric | — |
| [$\mathsf{S5}$](/VC3A2VWXND/) | $\mathrm{T}$, $\mathrm{5}$ | equivalence relations, or universal frames | NP-complete |
| $\mathsf{KD45}$ | $\mathrm{D}$, $\mathrm{4}$, $\mathrm{5}$ | serial, transitive and Euclidean | NP-complete |

: The standard normal logics. Each is canonical, so each is sound and strongly complete for its class of frames. The first seven have the finite model property with the bound $2^n$ and are decidable. The complexity of $\mathsf{B}$ is not covered by Ladner's theorem as the chapter states it, since $\mathsf{B}$ is not contained in $\mathsf{S4}$; the result for $\mathsf{KD45}$ is due to Halpern and Moses.

## Common errors

- **Frame validity against truth in a model.** The correspondences are about frames. Axiom $\mathrm{4}$ can be true in every world of a model whose frame is not transitive.
- **Necessitation as a formula.** The rule says that theorems are necessary, not that truths are. Applying it to a hypothesis and then discharging the hypothesis "proves" $p \to \square p$.
- **Diamond as "somewhere".** $\lozenge\varphi$ at $w$ needs $\varphi$ at a successor of $w$, not at any world. At a world with no successors, $\square\bot$ is true and $\square p \to \lozenge p$ fails.
- **Distributing the box over disjunction.** $\square p \vee \square q \to \square(p \vee q)$ holds in $\mathsf{K}$; the converse fails even in $\mathsf{S5}$.
- **The wrong filtration.** The smallest filtration of a transitive model need not be transitive, so it may leave the class of $\mathsf{K4}$-frames.
- **Confusing the names.** $\mathsf{B}$ is the logic $\mathsf{KTB}$, $\mathrm{B}$ is the axiom, and $\mathsf{KB}$ is the weaker logic without $\mathrm{T}$. The Brouwerian logic is a classical modal logic; its name records only an analogy with intuitionism.
