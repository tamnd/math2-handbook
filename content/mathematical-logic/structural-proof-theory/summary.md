## What to remember

- **Cut is the only rule that forgets.** The [cut rule](/DAMGTSY6VV/) infers $\Gamma, \Pi \Rightarrow \Delta, \Lambda$ from $\Gamma \Rightarrow \Delta, A$ and $A, \Pi \Rightarrow \Lambda$, and the cut formula $A$ need not appear in the conclusion. Every other rule of LK keeps all its formulas, possibly as parts of a principal formula.
- **Cut elimination.** Every sequent derivable in LK or LJ has a cut-free derivation. Gentzen's proof is a double induction on the degree of the cut formula and on the heights above the cut. In the one-sided propositional calculus, height $h$ and cut rank $r$ become cut-free height at most $2_r(h)$.
- **Subformula property.** A cut-free derivation, or a normal natural deduction derivation, contains only subformulas of its conclusion, in Gentzen's sense that includes instances $B[t/x]$. Consistency, decidability results and interpolation follow from it.
- **Normalization.** In natural deduction a detour is an introduction followed at once by an elimination of the same formula. Removing detours always ends, and under the Curry-Howard reading it is the evaluation of a typed lambda term.
- **Midsequent and Herbrand.** A derivable prenex sequent has a cut-free derivation with a quantifier-free midsequent, with only propositional and structural rules above it and only quantifier and structural rules below. For $\Rightarrow \exists x\, B(x)$ the midsequent is a tautology $\Rightarrow B(t_1), \dots, B(t_n)$.
- **Invertibility drives search.** In G3cp every rule is height-preserving invertible and each premise has one connective fewer, so backward search in any order decides classical propositional logic. In G3ip the rule R${\vee}$ and the left premise of L${\to}$ are not invertible, and LJT removes the loop of L${\to}$.
- **The cost is non-elementary.** Statman and Orevkov gave sequents with derivations of length $2^{c\ell}$ whose cut-free derivations have more than $2_\ell(0)$ sequents.
- **Harmony.** An elimination rule is justified when an introduction followed by it can be reduced away, and when it is strong enough to rebuild the formula. Tonk has neither property and derives everything.
- **Other formats.** Hypersequents, display calculi, labelled calculi and deep inference extend cut elimination to logics such as Gödel-Dummett logic, tense logic and modal logics given by frame conditions. Focusing puts cut-free proofs into a normal form of alternating phases.

## The calculi of the chapter

| Calculus | Logic | Feature |
|---|---|---|
| LK, LJ | classical, intuitionistic first-order | explicit structural rules, Gentzen's Hauptsatz |
| G3cp, G3ip | classical, intuitionistic propositional | no structural rules, height-preserving inversion |
| LJT | intuitionistic propositional | terminating backward search |
| HLC | Gödel-Dummett logic LC | communication rule between components |
| $\mathrm{DK_t}$ | tense logic $\mathrm{K_t}$ | display postulates, structural connectives |
| G3K$S$ | modal logics with geometric frame conditions | labels for worlds, frame rules |
| SKS | classical propositional | rules apply at any depth, atomic contraction |
| focused MALL | linear logic | inversion and focus phases |

: Proof formats in [structural proof theory](/N4EDJNMTEF/). Each has cut elimination, or cut admissibility, and the subformula property for cut-free proofs.

## Common errors

- **Thinking cut elimination proves theorems shorter.** It removes lemmas, and the result can be longer by a tower of exponentials.
- **Reading the subformula property too literally.** In first-order logic $P(t)$ counts as a subformula of $\forall x\, P(x)$ for every term $t$.
- **Forgetting that G3ip loops.** The left premise of L${\to}$ repeats $A \to B$, so naive backward search in G3ip need not stop.
- **Treating R${\vee}$ as invertible in G3ip.** From $p \vee q \Rightarrow q \vee p$ neither $p \vee q \Rightarrow q$ nor $p \vee q \Rightarrow p$ is derivable.
- **Applying the midsequent theorem to non-prenex sequents.** The hypothesis is needed: $\Rightarrow \forall x\, P(x) \to \forall x\, P(x)$ has no derivation with a midsequent.
- **Applying deep rules under a negation.** In SKS negation occurs only on atoms, so every context is positive. Switch inside $\neg\{\ \}$ is unsound.
- **Expecting one notion of identity of proofs for classical logic.** The normalization criterion identifies all LK derivations of one sequent, after weakenings.
