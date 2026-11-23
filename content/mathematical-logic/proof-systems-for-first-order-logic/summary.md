## What to remember

- The **Hilbert-style calculus** of Enderton has one rule, modus ponens, and as axioms all generalizations of six groups: tautologies, $\forall x\, \varphi \to \varphi[t/x]$ with $t$ substitutable for $x$, distribution of $\forall$ over $\to$, $\varphi \to \forall x\, \varphi$ with $x$ not free in $\varphi$, and the two equality axioms.
- **Generalization theorem:** if $\Gamma \vdash \varphi$ and $x$ is not free in any formula of $\Gamma$, then $\Gamma \vdash \forall x\, \varphi$. **Deduction theorem:** $\Gamma \cup \{\psi\} \vdash \varphi$ implies $\Gamma \vdash \psi \to \varphi$. In a calculus with a generalization rule, the deduction theorem needs the condition that no generalization is applied to a variable free in $\psi$; without it, $\{P(x)\} \vdash \forall x\, P(x)$ would give the invalid $P(x) \to \forall x\, P(x)$.
- **Natural deduction** has an introduction and an elimination rule for each symbol. The eigenvariable of ${\forall}\mathrm{I}$ must not be free in any open assumption; the eigenvariable of ${\exists}\mathrm{E}$ must not be free in the conclusion, in the existential premise or in any other open assumption. Fitch's boxed constants state the same conditions as "the boxed constant does not occur outside its box".
- The **sequent calculus** LK derives sequents $\Gamma \Rightarrow \Delta$, read as "the conjunction of $\Gamma$ implies the disjunction of $\Delta$". By Gentzen's [cut elimination](/AYRZ98Y0NW/), every derivable sequent has a derivation without cut, and every formula in a cut-free derivation is a subformula of a formula in the end sequent, up to substitution of terms.
- A **tableau** for $\Gamma \cup \{\neg\varphi\}$ that closes proves $\Gamma \vdash \varphi$. The $\delta$ rule needs a new parameter each time; a $\gamma$ formula can be used again with any term. A finished open branch is a **Hintikka set**, and by [Hintikka's lemma](/2A6QP78XN3/) every Hintikka set is satisfiable in a model built from closed terms.
- **Resolution** works on clauses after prenex form, [Skolemization](/GCPQGMJYEV/) and conjunctive normal form, which preserve satisfiability, not equivalence. Binary resolution with a most general unifier, together with factoring, is sound and refutation complete: a set of clauses is unsatisfiable exactly when the empty clause is derivable.
- **The Hilbert calculus, natural deduction, LK and tableaux prove the same sentences,** and these are the logical consequences: $\Gamma \vdash_{\mathsf{H}} \varphi$, $\Gamma \vdash_{\mathsf{ND}} \varphi$, $\Gamma \vdash_{\mathsf{LK}} \varphi$, $\Gamma \vdash_{\mathsf{T}} \varphi$ and $\Gamma \models \varphi$ are equivalent. None of them is a decision procedure, since validity is undecidable by [Church's theorem](/VA6BNNY2YC/).
- **Equality** needs reflexivity and the substitution principle; symmetry, transitivity and congruence follow from them.

## The systems side by side

| System | A proof is | Rules for quantifiers | Main side condition | Typical use |
|---|---|---|---|---|
| [Hilbert calculus](/N95HV0VWSM/) | a list of formulas | axiom groups 2–4 | $t$ substitutable; $x$ not free | metatheorems by induction on proofs |
| [Natural deduction](/6KT3BJZ7D1/) | a tree with discharged assumptions | ${\forall}\mathrm{I}$, ${\forall}\mathrm{E}$, ${\exists}\mathrm{I}$, ${\exists}\mathrm{E}$ | eigenvariable on ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$ | formalizing ordinary proofs |
| [Fitch style](/2B6XC7XJA8/) | numbered lines in nested boxes | the same rules, with boxed constants | the boxed constant does not occur outside its box | teaching, proof checkers |
| [Sequent calculus LK](/W72CA3R9MP/) | a tree of sequents | ${\forall}$L, ${\forall}$R, ${\exists}$L, ${\exists}$R | eigenvariable on ${\forall}$R and ${\exists}$L | proof theory, cut elimination |
| [Tableaux](/WGWBBVE8GX/) | a tree of sentences that closes | $\gamma$ and $\delta$ rules | the $\delta$ parameter is new | refutation by hand, countermodels |
| [Resolution](/DEB3CF4Z2D/) | a derivation of the empty clause | none: Skolemize first, then unify | occurs check; clauses renamed apart | automated theorem proving |

: The proof systems of the chapter. All are sound and complete for first-order logic; resolution is refutation complete only, so it shows $\Gamma \models \varphi$ by refuting $\Gamma \cup \{\neg\varphi\}$.

## Common errors

- **Capturing a variable.** $\forall x\, \exists y\, R(x,y) \to \exists y\, R(y,y)$ is not an instance of axiom group 2, because $y$ is not substitutable for $x$ in $\exists y\, R(x,y)$. Rename the bound variable first.
- **Letting an eigenvariable escape.** Check each use of ${\forall}\mathrm{I}$, ${\exists}\mathrm{E}$, ${\forall}$R, ${\exists}$L and $\delta$: the new variable or constant must not occur where the rule forbids it. Most wrong proofs of invalid sentences break exactly this condition.
- **Reading an unfinished tableau as a disproof.** A tableau that has not closed yet proves nothing. Only a finished open branch, on which every rule has been applied fairly, gives a countermodel, and such a branch may be infinite.
- **Forgetting factoring or the occurs check.** Binary resolution without factoring cannot refute $\{P(x), P(y)\}, \{\neg P(u), \neg P(v)\}$, and unification without the occurs check derives the empty clause from satisfiable sets.
- **Treating Skolem form as equivalent.** $\forall x\, R(x, f(x))$ implies $\forall x\, \exists y\, R(x,y)$, but not conversely; only satisfiability is preserved.
