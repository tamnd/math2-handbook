## What to remember

- **Kripke forcing.** A model is a partial order with valuations that are up-sets. Conjunction and disjunction are read at the world itself; $w \Vdash \varphi \to \psi$ when every $v \ge w$ that forces $\varphi$ forces $\psi$, and $w \Vdash \neg\varphi$ when no $v \ge w$ forces $\varphi$. Every truth set is an up-set (persistence), and $\mathsf{IPC}$ is sound and complete for these models, with finite countermodels for non-theorems.
- **What fails.** $\mathsf{IPC}$ proves $p \to \neg\neg p$, $\neg\neg\neg p \leftrightarrow \neg p$ and $\neg\neg(p \vee \neg p)$. It does not prove $p \vee \neg p$, $\neg\neg p \to p$, Peirce's law, $(p \to q) \vee (q \to p)$ or the De Morgan law $\neg(p \wedge q) \to \neg p \vee \neg q$. The two-world chain and the fork with three worlds refute all of them.
- **Glivenko's theorem.** $\mathsf{CPC} \vdash \varphi$ if and only if $\mathsf{IPC} \vdash \neg\neg\varphi$, and $\mathsf{CPC} \vdash \neg\varphi$ if and only if $\mathsf{IPC} \vdash \neg\varphi$. So every intermediate logic proves the same negated formulas as $\mathsf{CPC}$. The theorem fails in predicate logic: $\neg\neg\forall x\,(Px \vee \neg Px)$ is not provable.
- **Disjunction property.** If $\mathsf{IPC} \vdash \varphi \vee \psi$, then $\mathsf{IPC} \vdash \varphi$ or $\mathsf{IPC} \vdash \psi$; the same holds over a set of Harrop hypotheses, and $\mathsf{IQC}$ also has the existence property. The [Kleene slash](/YRRKEEHNCD/) proves it syntactically: $\Gamma \mid \varphi$ implies $\Gamma \vdash \varphi$, and a self-slashing $\Gamma$ slashes all its consequences.
- **No finite truth table.** [Gödel's formula](/CFCPJA1QF5/) $D_n = \bigvee_{0 \le i < j \le n} (p_i \leftrightarrow p_j)$ holds in every Heyting algebra with at most $n$ elements and fails on the chain of $n$ worlds. The logics of the finite chains decrease strictly, and their intersection is $\mathsf{LC}$.
- **Predicate logic.** Kripke models for $\mathsf{IQC}$ have domains that grow along the order. The constant domain axiom, $\neg\forall x\,Px \to \exists x\,\neg Px$ and the double negation shift $\forall x\,\neg\neg Px \to \neg\neg\forall x\,Px$ are not provable, and $\mathsf{IQC}$ is undecidable already in its monadic fragment.
- **Intermediate logics.** They form a distributive lattice of cardinality continuum, dually isomorphic to the lattice of non-trivial varieties of Heyting algebras. $\mathsf{CPC}$ is its top. $\mathsf{KC} \subseteq \mathsf{LC}$, and $\mathsf{KP}$ and Medvedev's logic have the disjunction property.
- **Admissible rules.** A rule is admissible when every substitution that makes its premises theorems makes its conclusion a theorem. The Kreisel–Putnam rule is admissible in $\mathsf{IPC}$ but not derivable, so $\mathsf{IPC}$ is not structurally complete; $\mathsf{CPC}$, $\mathsf{LC}$ and Medvedev's logic are.
- **Interpolation.** By [Maksimova's theorem](/M3RTNGG3J5/), exactly seven intermediate logics have Craig interpolation, and among them only $\mathsf{IPC}$ has the disjunction property.

## Some intermediate logics

| Logic | Axiom over $\mathsf{IPC}$ | Kripke frames | Disjunction property | Interpolation |
|---|---|---|---|---|
| [$\mathsf{IPC}$](/Q11N8X99FK/) | none | all partial orders | yes | yes |
| [$\mathsf{KC}$](/CX032ACTMZ/) | $\neg p \vee \neg\neg p$ | directed | no | yes |
| [$\mathsf{LC}$](/FA88H7FDPY/) | $(p \to q) \vee (q \to p)$ | linear | no | yes |
| [$\mathsf{BD}_2$](/H5NSKEP3P2/) | $p_2 \vee (p_2 \to p_1 \vee \neg p_1)$ | depth at most $2$ | no | yes |
| [$\mathsf{KP}$](/X0C1NC7FXX/) | $(\neg p \to q \vee r) \to (\neg p \to q) \vee (\neg p \to r)$ | | yes | no |
| [Medvedev's logic](/R2FD01J3PC/) | not finitely axiomatizable | the frames $M_n$ | yes | no |
| $\mathsf{CPC}$ | $p \vee \neg p$ | one-world frames | no | yes |

: Six intermediate logics and $\mathsf{IPC}$. The last column follows from Maksimova's list; the logics with the disjunction property other than $\mathsf{IPC}$ have no interpolation, as her theorem predicts.

## Common errors

- **Reading $\neg\varphi$ at one world.** $w \Vdash \neg\varphi$ asks that no later world force $\varphi$, not only $w$. So $w \nVdash \varphi$ and $w \nVdash \neg\varphi$ can both hold, which is how $p \vee \neg p$ fails.
- **Proving a negation by contradiction and calling it excluded middle.** Deriving $\bot$ from $\varphi$ proves $\neg\varphi$ intuitionistically. Deriving $\bot$ from $\neg\varphi$ proves only $\neg\neg\varphi$.
- **Confusing admissible and derivable.** A rule can preserve the theorems of $\mathsf{IPC}$ without its implication form being a theorem, as the Kreisel–Putnam rule shows. Admissibility depends on the set of theorems, so it can change when axioms are added.
- **Applying Glivenko's theorem to quantifiers.** It holds for propositional formulas and for predicate formulas without $\forall$; in general Kuroda's translation, which puts $\neg\neg$ after each $\forall$, is needed.
- **Mixing up minimal logic and Medvedev's logic.** Both are abbreviated $\mathsf{ML}$ in the literature. Minimal logic lies below $\mathsf{IPC}$ and is not intermediate; Medvedev's logic lies above it.
