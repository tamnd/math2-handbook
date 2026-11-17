## What to remember

- A [signature](/WDVVEYD6AT/) $\sigma$ is a set of constant, function and relation symbols, each with a fixed arity. [Terms](/6D3WA7N2W4/) are built from variables and constants by function symbols; [atomic formulas](/MCZRXR3SVB/) are $R(t_1, \ldots, t_n)$ and $t_1 = t_2$; [formulas](/HYJ10AF6RT/) close them under $\neg$, the binary connectives, $\forall x$ and $\exists x$. Each formula has exactly one reading, by [unique readability](/3QPV4XW8MC/).
- The [free variables](/9CNGDRAMGC/) are defined by recursion: all variables of an atomic formula are free, connectives take unions, and $\mathrm{FV}(\forall x \, \varphi) = \mathrm{FV}(\exists x \, \varphi) = \mathrm{FV}(\varphi) \setminus \set{x}$. A [sentence](/DKFGQTRYZE/) is a formula with $\mathrm{FV}(\varphi) = \emptyset$.
- [Substitution](/NCDZ969V7X/) $\varphi[t/x]$ replaces the free occurrences of $x$ by $t$. It is admissible when $t$ is substitutable for $x$: no variable of $t$ falls into the scope of a quantifier on that variable. Renaming bound variables always makes a term substitutable, and $\varphi[t/x] = \varphi$ when $x \notin \mathrm{FV}(\varphi)$.
- A [first-order theory](/92SWXST1ZM/) is a set of sentences. In [logic with equality](/Q1494G7FBM/), $=$ is a logical symbol with the axioms $\forall x \, (x = x)$ and substitution for every function and relation symbol, $=$ included; symmetry and transitivity follow.
- [Many-sorted logic](/7TDHDN8P96/) reduces to one-sorted logic: add a predicate $P_s$ for each sort, relativize the quantifiers, and add axioms saying that each $P_s$ is nonempty and each function maps sorts correctly.
- Every formula is equivalent to one in [prenex normal form](/CS82V969DE/) with the same free variables. This uses classical logic and nonempty domains, and the prenex form is not unique.
- A sentence and its [Skolem normal form](/GCPQGMJYEV/) are equisatisfiable, and the Skolem form implies the sentence, but they are not equivalent in general. Each existential quantifier becomes a function symbol of the universal variables before it.
- In the [epsilon calculus](/TH5ZKCKN3W/), $\exists x \, A \leftrightarrow A(\varepsilon x \, A)$ and $\forall x \, A \leftrightarrow A(\varepsilon x \, \neg A)$, and by the second epsilon theorem the calculus is conservative over first-order logic. By Russell's analysis of [definite descriptions](/PD2R4XT79Q/), "the $\varphi$ is $\psi$" is $\exists x \, (\varphi(x) \land \forall y \, (\varphi(y) \to y = x) \land \psi(x))$.

| Equivalence | Condition |
|---|---|
| $\neg \forall x \, \varphi \equiv \exists x \, \neg \varphi$ and $\neg \exists x \, \varphi \equiv \forall x \, \neg \varphi$ | none |
| $(\forall x \, \varphi) \land \psi \equiv \forall x \, (\varphi \land \psi)$ and $(\exists x \, \varphi) \land \psi \equiv \exists x \, (\varphi \land \psi)$ | $x \notin \mathrm{FV}(\psi)$ |
| $(\forall x \, \varphi) \lor \psi \equiv \forall x \, (\varphi \lor \psi)$ and $(\exists x \, \varphi) \lor \psi \equiv \exists x \, (\varphi \lor \psi)$ | $x \notin \mathrm{FV}(\psi)$ |
| $(\forall x \, \varphi) \to \psi \equiv \exists x \, (\varphi \to \psi)$ and $(\exists x \, \varphi) \to \psi \equiv \forall x \, (\varphi \to \psi)$ | $x \notin \mathrm{FV}(\psi)$ |
| $\psi \to \forall x \, \varphi \equiv \forall x \, (\psi \to \varphi)$ and $\psi \to \exists x \, \varphi \equiv \exists x \, (\psi \to \varphi)$ | $x \notin \mathrm{FV}(\psi)$ |

: The equivalences that move a quantifier to the front, used to reach prenex normal form. When $x$ is free in $\psi$, rename the bound variable first. The rules assume, as first-order logic does, that the domain is nonempty; for example, $(\forall x \, \varphi) \land \psi \equiv \forall x \, (\varphi \land \psi)$ fails in an empty domain when $\psi$ is false.

## Common errors

- Substituting without checking for capture. In $\exists y \, \neg (x = y)$, putting $y$ for $x$ gives $\exists y \, \neg (y = y)$, which says something quite different. Rename the bound variable first.
- Moving a quantifier across $\lor$ or $\land$ when the variable is free in the other part. $\forall x \, P(x) \lor \forall x \, Q(x)$ is not $\forall x \, (P(x) \lor Q(x))$; rename one of the bound variables and get $\forall x \, \forall y \, (P(x) \lor Q(y))$.
- Forgetting that the antecedent of an implication counts as negated. $\forall x$ in the antecedent becomes $\exists x$ in front, and $\exists x$ becomes $\forall x$.
- Treating a Skolem form as equivalent to the original sentence. It is stronger and uses a larger signature; only satisfiability is preserved.
- Mixing the symbol $=$ of the object language with identity of strings in the metalanguage. In arithmetic, $S(0) + S(0)$ and $S(S(0))$ are different terms, even though the Peano axioms prove them equal.
- Putting formulas with free variables in a theory. A theory consists of sentences; take the universal closure of an axiom that is written with free variables.
