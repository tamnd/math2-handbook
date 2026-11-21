## What to remember

- **The Lindenbaum–Tarski algebra** of a logic is the set of formulas modulo provable equivalence, with the connectives as operations. For classical logic in $n$ variables it is the Boolean algebra with $2^{2^n}$ elements, and $\varphi$ is a theorem iff $\varphi \approx 1$ holds in every Boolean algebra.
- **Interior and modal algebras.** A modal algebra is a Boolean algebra with $\Box 1 = 1$ and $\Box(x \wedge y) = \Box x \wedge \Box y$; interior algebras add $\Box x \le x$ and $\Box \Box x = \Box x$ and are the algebras of $\mathrm{S4}$. Their open elements form a Heyting algebra.
- **Jónsson–Tarski:** every modal algebra embeds in the complex algebra of its ultrafilter frame by $a \mapsto \set{u : a \in u}$, and for a finite algebra the embedding is an isomorphism.
- **MV- and BL-algebras.** MV-algebras are the algebras of Łukasiewicz logic, with $[0,1]$, $x \oplus y = \min(1, x + y)$ and $\lnot x = 1 - x$ as the main example. Mundici's functor $\Gamma(G, u) = [0, u]$ is an equivalence with unital lattice-ordered abelian groups. BL-algebras are the prelinear, divisible, bounded commutative integral residuated lattices; MV-algebras are those with $\lnot\lnot x = x$, Gödel algebras those with $x \otimes x = x$.
- **Residuation:** $xy \le z$ iff $y \le x \backslash z$ iff $x \le z / y$. Multiplication then distributes over existing joins, and residuated lattices are the algebras of substructural logics.
- **First-order logic.** Cylindric algebras add cylindrifications $c_\kappa$ and diagonals $d_{\kappa\lambda}$ to a Boolean algebra. Locally finite algebras of dimension $\alpha \ge \omega$ are representable, which is the completeness theorem; for finite $n \ge 3$, $\mathbf{RCA}_n$ is a variety with no finite axiomatization (Monk).
- **Relation algebras:** $\mathsf{RRA}$ is a variety, $\mathsf{RRA} \ne \mathsf{RA}$, no finite set of first-order sentences axiomatizes $\mathsf{RRA}$, and representability of finite relation algebras is undecidable. The equations valid in $\mathsf{RRA}$ match the valid three-variable sentences about binary relations.
- **Algebraizable logics** (Blok and Pigozzi) have defining equations $E(x)$ and equivalence formulas $\Delta(x, y)$ that translate consequence into equational consequence over a quasivariety and back. Theories then match relative congruences, and extensions match subquasivarieties in reverse order. A logic with no theorems in which $x \nvdash y$ is not even protoalgebraic.
- **Suszko's reduction:** every consequence relation is determined by two-valued valuations, the characteristic functions of its closed sets, but these valuations are in general not truth-functional.

## Logics and their algebras

| Logic | Algebras | Representation or completeness result |
|---|---|---|
| [Classical propositional logic](/09K9MWD2QQ/) | [Boolean algebras](/0XADJKM699/) | Stone: every Boolean algebra is a field of sets |
| [Intuitionistic logic](/Q11N8X99FK/) | [Heyting algebras](/NG943XNQWH/) | complete for its Lindenbaum–Tarski algebras |
| [$\mathrm{S4}$](/N60RVXSA5W/) | [interior algebras](/BDEX7HET71/) | McKinsey–Tarski: $\R$ validates exactly $\mathrm{S4}$ |
| Normal modal logics | [modal algebras](/3H85NSFWHK/) | Jónsson–Tarski: embedding in a complex algebra |
| [Łukasiewicz logic](/JQ713VVD0G/) | [MV-algebras](/8T4M7RN9AC/) | Chang: $[0,1]$ generates the variety |
| [Hájek's basic logic](/3AQ5GHTXA4/) | [BL-algebras](/ERNYMVEGKC/) | complete for continuous t-norms |
| First-order logic with equality | [cylindric algebras](/1MDT9BF81H/) | locally finite, dimension $\omega$: representable |
| First-order logic without equality | [polyadic algebras](/CQ9A86S3J4/) | locally finite, infinite degree: subdirect product of functional algebras |
| Three-variable logic of binary relations | [relation algebras](/GQK4DSA11K/) | $\mathsf{RRA}$ is a variety with no finite basis |

: Nine logics, their classes of algebras, and the theorem that ties each logic to concrete models. The first six classes are varieties of algebras for propositional logics; the last three handle quantifiers or relations.

## Common errors

- **Completeness is not algebraizability.** The conjunction and disjunction fragment of classical logic is complete for distributive lattices, but it has no theorems and is not algebraizable. Algebraizability needs translations in both directions.
- **The designated set need not be $\set{1}$.** In the full Lambek calculus with exchange, $E(x) = \set{x \wedge 1 \approx 1}$ designates every element above the unit, and the logic is algebraizable but not implicative.
- **Mixing up $1'$ and $1$.** In a relation algebra $1'$ is the identity relation and $1$ the universal relation; they agree only in the degenerate algebras where $;$ is meet.
- **Reading non-finite axiomatizability as failure to be a variety.** $\mathsf{RRA}$ and $\mathbf{RCA}_n$ are varieties; they need infinitely many equations.
- **Expecting every residuated structure to be divisible.** The nilpotent minimum t-norm is prelinear but not divisible, so its algebras are not BL-algebras; and the max and $1 - x$ operations on $[0,1]$ form a Kleene algebra, not an MV-algebra.
- **Reading Suszko's two values as a truth table.** The valuations $b_T$ do not respect the connectives; the number of truth values is a property of a truth-functional semantics, not of the consequence relation.
