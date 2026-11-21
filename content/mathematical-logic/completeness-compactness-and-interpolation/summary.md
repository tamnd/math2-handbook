## What to remember

- **Soundness:** if $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$. Its main use is negative: to show that $\Gamma \nvdash \varphi$, find one model of $\Gamma$ in which $\varphi$ is false.
- **Lindenbaum's lemma:** every consistent set of sentences lies in a maximal consistent set $\Delta$, which contains exactly one of $\sigma$ and $\neg\sigma$ for each sentence $\sigma$ and is closed under $\vdash$. For a countable language a list of all sentences suffices; in general the proof uses [Zorn's lemma](/04RXTQA5ZA/).
- **The Henkin construction** adds for each sentence $\exists x\, \psi$ a new constant $c$ and the witness axiom $\exists x\, \psi \to \psi(c)$, extends to a maximal consistent set, and takes as model the closed terms modulo provable equality. A truth lemma shows that a sentence is true there exactly when it lies in the set.
- **Model existence:** every consistent set of sentences has a model with at most $\max(|L|, \aleph_0)$ elements. This is equivalent to **Gödel's completeness theorem** in its strong form: $\Gamma \models \varphi$ implies $\Gamma \vdash \varphi$. So the valid sentences of a countable language form a computably enumerable set.
- **Compactness:** a set of sentences has a model if and only if every finite subset has one. It gives nonstandard models of $\operatorname{Th}(\N)$, and it shows that finiteness, torsion, connectedness and well-ordering are not expressible by any set of first-order sentences.
- A theory is **recursively axiomatizable** when some decidable set of axioms has the same theorems. Its theorems are then computably enumerable, and by **Craig's theorem** the converse holds. A complete recursively axiomatizable theory is decidable.
- **Herbrand's theorem:** for quantifier-free $\psi$, in a language without equality and with a constant, $\exists \bar x\, \psi$ is valid if and only if some finite disjunction $\psi(\bar t_1) \vee \cdots \vee \psi(\bar t_k)$ of ground instances is a tautology.
- **Craig interpolation:** if $\varphi \models \psi$, there is a sentence $\theta$ with $\varphi \models \theta \models \psi$ whose non-logical symbols all occur in both $\varphi$ and $\psi$. **Lyndon's** refinement also keeps each relation symbol of $\theta$ with a sign it has in both. **Robinson's** theorem: if no sentence of the common language separates $\Gamma$ from $\Sigma$, then $\Gamma \cup \Sigma$ has a model.
- **Two meanings of complete.** First-order logic is complete: it proves every valid sentence. A theory is complete when it decides every sentence; by Gödel's incompleteness theorems, no consistent recursively axiomatizable theory that contains enough arithmetic is.

## Theories and their properties

| Theory | Recursively axiomatizable | Complete | Decidable |
|---|---|---|---|
| [Dense linear orders without endpoints](/2W4S2H4VYA/) | yes | yes | yes |
| [Presburger arithmetic](/4W0E9G7PPV/) | yes | yes | yes |
| [Theory of groups](/RX9MB386C5/) | yes | no | no |
| [Peano arithmetic](/0QFT7Z76N5/) | yes | no | no |
| [True arithmetic](/DX0KPMH4QZ/) $\operatorname{Th}(\N, +, \cdot)$ | no | yes | no |

: Five theories. The rows show that the three properties are independent of each other except for one link: a theory that is recursively axiomatizable and complete is decidable.

## Common errors

- **Confusing the two kinds of completeness.** Gödel's completeness theorem does not say that every sentence or its negation is provable from a theory; it says that what follows is provable.
- **Using an old constant as a witness.** In the Henkin construction and in the $\delta$ rule of tableaux, the witness must be new; otherwise the witness axiom can make a consistent set inconsistent.
- **Mixing up "not elementary" and "not finitely axiomatizable".** Finiteness, torsion and well-ordering are not expressed by any set of sentences. Torsion-free groups and infinite structures are expressed by an infinite set of sentences, but by no single sentence. Compactness proves both kinds of result, with different arguments.
- **Expecting the theorems over finite structures.** Every finite subset of $\set{\lambda_n : n \ge 2}$, where $\lambda_n$ says "at least $n$ elements", has a finite model, but the whole set has no finite model. Over finite structures alone, compactness, completeness and Craig interpolation all fail.
- **Counting equality as a shared symbol.** In Craig's theorem $=$ is logical, so $\theta$ may use it even if neither side has a common relation symbol; constants and function symbols, though, must occur on both sides.
