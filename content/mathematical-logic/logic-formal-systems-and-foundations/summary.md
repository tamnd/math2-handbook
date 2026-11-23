## What to remember

- A **[formal system](/439M8B4DY2/)** has an alphabet, formation rules, axioms and rules of inference, and each part is decidable. So the set of derivations is decidable and the set of theorems is computably enumerable, though it need not be decidable.
- A **[rule of inference](/QPD3X471Q1/)** is *derivable* when a fixed chain of other steps replaces it, and *admissible* when adding it creates no new theorems. Every derivable rule is admissible; uniform substitution is admissible in a Hilbert system but not derivable.
- A **[consequence relation](/J78Y1M4GND/)** satisfies reflexivity, monotonicity and cut. Consequence relations on a set of formulas correspond one to one with closure operators $\mathrm{Cn}$, and finitary relations with algebraic operators.
- A theory $T$ is **[consistent](/VM8TQ70CVJ/)** when no $\varphi$ has $T \vdash \varphi$ and $T \vdash \neg\varphi$. In first-order logic, $T$ is consistent exactly when it has a model, and $T \nvdash \varphi$ exactly when $T \cup \set{\neg\varphi}$ is consistent.
- **[Soundness](/4A84VHDTHV/)** is $\vdash \varphi \Rightarrow {}\models \varphi$ (weak) or $\Gamma \vdash \varphi \Rightarrow \Gamma \models \varphi$ (strong). So a single counter-model shows that a formula is not provable.
- $T'$ is a **[conservative extension](/N238J43XNE/)** of $T$ when the two prove the same sentences of the language of $T$. If every model of $T$ expands to a model of $T'$, the extension is conservative. An [extension by definitions](/GCK0NN60E4/) is conservative and its new symbols can be eliminated, provided each defined function symbol comes with a proof of $\forall \bar x\, \exists! y\, \psi(\bar x, y)$.
- A **[relative consistency proof](/X3G0RG2GPZ/)** shows $\mathrm{Con}(S) \to \mathrm{Con}(T)$, by building a model or an interpretation of $T$ inside $S$. Two such proofs, for $T + \varphi$ and $T + \neg\varphi$, show that $\varphi$ is independent of $T$ if $S$ is consistent.
- In the **[syllogistic](/MZBNX2T6Q6/)**, 24 of the 256 forms (mood and figure) are valid when every term is taken to be nonempty, and 15 when empty terms are allowed. The 9 lost forms all draw a particular conclusion from two universal premises.
- A notion is **[logical](/2QQ7Q5SKP8/)** in Tarski's sense when it is invariant under every permutation of the domain. On a domain with at least two elements, exactly four binary relations pass this test: the empty relation, identity, diversity and the full relation.

| Property | Meaning | Classical PL | Intuitionistic PL |
|---|---|---|---|
| Consistent | no $\varphi$ with $\vdash \varphi$ and $\vdash \neg\varphi$ | yes | yes |
| Post consistent | some formula is not a theorem | yes | yes |
| Post complete | adding any non-theorem as a schema makes every formula a theorem | yes | no |
| Negation complete | $\vdash \varphi$ or $\vdash \neg\varphi$ for each $\varphi$ | no: neither $p$ nor $\neg p$ | no |
| Sound | every theorem is valid in the intended semantics | yes, for truth tables | yes, for Heyting algebras and Kripke models |

: Properties of two propositional logics with no extra axioms. Post completeness and negation completeness are different notions, and classical logic has the first without the second.

## Common errors

- Reading "$\vdash p \to q$" as "if $\vdash p$ then $\vdash q$". The first is a claim about one formula of the object language; the second is a claim of the metalanguage about two derivations. For distinct variables in classical logic, the second holds vacuously and the first is false.
- Using "complete" without saying which sense. A logic can be complete for a semantics, a theory can be negation complete, and a system can be Post complete; none of these implies the others in general.
- Running the model-expansion test backwards. A conservative extension need not let every model expand: true arithmetic plus a new constant $c$ and the axioms $c > \bar n$ for all $n$ is conservative, yet the standard model has no expansion.
- Defining a function symbol from a formula $\psi(\bar x, y)$ that has existence but not uniqueness. The new theory can prove new sentences of the old language, and can even be inconsistent.
- Treating relative consistency as absolute. A proof of $\mathrm{Con}(\mathrm{ZF}) \to \mathrm{Con}(\mathrm{ZFC})$ says nothing about whether ZF is consistent.
- Mixing the two readings of "every $S$ is $P$" in one syllogism. Darapti is valid only when the middle term is nonempty, and Barbari only when the minor term is.
