## What to remember

- **Bisimulation.** A relation $Z$ between two models is a bisimulation when linked worlds agree on all variables and every step along $R$ on one side is matched by a step on the other side that stays inside $Z$. Bisimilar worlds satisfy the same modal formulas. On image-finite models the converse holds too: by the Hennessy–Milner theorem, modal equivalence is bisimilarity.
- **Van Benthem's theorem.** A first-order formula $\alpha(x)$ is equivalent to the standard translation of a modal formula exactly when it is invariant under bisimulation. So $R x x$ is not modal. Rosen proved the same statement over finite models.
- **Correspondence.** On frames, $\lozenge\square p \to \square\lozenge p$ says that any two successors have a common successor, and $\square\square p \to \square p$ says that $R$ is dense. Sahlqvist formulas have first-order correspondents computed from minimal valuations, and they are canonical, so $\mathsf{K} \oplus \Sigma$ is complete for its frames when $\Sigma$ is a set of Sahlqvist formulas. Löb's formula and the McKinsey formula $\square\lozenge p \to \lozenge\square p$ have no first-order correspondent.
- **Definability.** By the Goldblatt–Thomason theorem, an elementary class of frames is modally definable exactly when it is closed under bounded morphic images, generated subframes and disjoint unions, and reflects ultrafilter extensions. So irreflexivity is not modally definable.
- **Incompleteness and general frames.** The logic $\mathsf{KvB}$ has the same Kripke frames as $\mathsf{KvB} \oplus (\square\lozenge\top \to \square\bot)$ but does not prove $\square\lozenge\top \to \square\bot$, so it is Kripke incomplete. Every normal modal logic is complete for its descriptive general frames.
- **The lattice $\mathrm{NExt}(\mathsf{K})$.** Its only coatoms are $\mathrm{Log}(\circ)$ and $\mathrm{Log}(\bullet)$. Every normal extension of $\mathsf{S4.3}$ has the finite model property and is finitely axiomatizable. By the Blok–Esakia theorem, $\mathrm{NExt}(\mathsf{Grz})$ is isomorphic to the lattice of intermediate logics.
- **Quantifiers.** With varying domains, the Barcan formula $\forall x \square\varphi \to \square\forall x \varphi$ is valid on a frame exactly when the domains decrease along $R$, and its converse exactly when they increase. Validity is undecidable, already for the monadic fragment.
- **Extended languages.** The $\mu$-calculus is the bisimulation-invariant part of monadic second-order logic, and its satisfiability is EXPTIME-complete, as for $\mathsf{PDL}$. Hybrid logic names worlds, and its pure formulas define frame properties, such as irreflexivity, that no modal formula defines.
- **Topology and translation.** With $\square$ read as interior, every space validates $\mathsf{S4}$ and $\mathrm{Log}(\R) = \mathsf{S4}$. The Gödel–McKinsey–Tarski translation, with $T(p) = \square p$ and $T(A \to B) = \square(T(A) \to T(B))$, satisfies $\mathsf{IPC} \vdash A \iff \mathsf{S4} \vdash T(A)$.

| Logic | Adds to $\mathsf{K}$ | Satisfiability | One fact to keep |
|---|---|---|---|
| Basic modal logic $\mathsf{K}$ | — | PSPACE-complete | the bisimulation-invariant part of first-order logic |
| [Modal $\mu$-calculus](/MZ0M2KR9S0/) | least and greatest fixed points | EXPTIME-complete | the bisimulation-invariant part of monadic second-order logic |
| [$\mathsf{PDL}$](/VJ78A0Q22R/) | one box for each regular program | EXPTIME-complete | small models through the Fischer–Ladner closure; not compact |
| [Hybrid $\mathcal{H}(@)$](/NVPQ9W9DED/) | nominals and $@$ | PSPACE-complete | the pure formula $i \to \neg\lozenge i$ defines irreflexivity |
| Hybrid $\mathcal{H}(\downarrow)$ | the binder $\downarrow$ | undecidable | — |
| [Quantified $\mathsf{K}$](/D2H3S12V7X/) | quantifiers over domains | undecidable, even monadic | Kripke completeness need not transfer from the propositional logic |
| [$\mathsf{K} \times \mathsf{K}$](/JA2EBWVW8A/) | two commuting boxes | decidable | every logic between $\mathsf{K}^3$ and $\mathsf{S5}^3$ is undecidable |

: Extensions of the basic modal language, with the complexity of satisfiability on all frames; a dash marks a fact the chapter does not give.

## Common errors

- **Confusing truth in a model with validity on a frame.** Through the standard translation every modal formula is first-order on models. Correspondence results are about frames, where the formula quantifies over all valuations.
- **Using Hennessy–Milner without image-finiteness.** Two roots can satisfy the same formulas without being bisimilar when a world has infinitely many successors.
- **Reading every frame property as modal.** Irreflexivity, asymmetry and "at most one world" are first-order but not modally definable, while the McKinsey formula defines a class that is not first-order.
- **Assuming Kripke completeness.** It has to be proved for each logic, by canonicity, filtration or another method, and it fails for $\mathsf{KvB}$.
- **Leaving out boxes in the translation.** Without $\square$ on variables and implications, the Gödel–McKinsey–Tarski translation is neither sound nor faithful.
- **Expecting products of decidable logics to be decidable.** This holds for $\mathsf{K} \times \mathsf{K}$ and $\mathsf{S5} \times \mathsf{S5}$, and it fails in three dimensions.
- **Evaluating validity at non-normal worlds.** In Kripke's semantics for $\mathsf{S2}$ and $\mathsf{S3}$, validity is truth at the normal worlds only; otherwise no formula $\square\varphi$ would be valid.
