## What to remember

- A theory is **decidable** if the set of its theorems is computable. A theory with a computably enumerable set of axioms has a computably enumerable set of theorems, and if it is also complete it is [decidable](/HWC687ES0Q/). Being finitely axiomatized does not help: [Robinson arithmetic](/3K1AKGXF8A/) and the theory of groups are finitely axiomatized and undecidable.
- **[Church's theorem](/VA6BNNY2YC/).** For a signature with at least one binary relation symbol, the set of valid sentences is computably enumerable but not computable. The satisfiable sentences are therefore not computably enumerable.
- **[Trakhtenbrot's theorem](/XP6FW2WDWT/).** The sentences with a finite model form a computably enumerable set that is not computable, so the sentences true in all finite structures are not computably enumerable. No sound and complete proof system exists for finite structures.
- **Small models decide.** A satisfiable [monadic](/SERN6CRVWW/) sentence with $k$ predicates and quantifier rank $q$ has a model of size at most $2^k \cdot \max(q,1)$, and of size at most $2^k$ without equality. A satisfiable sentence $\exists x_1 \dots \exists x_m \forall \bar y\, \psi$ with $\psi$ quantifier-free and no function symbols has a model of size at most $\max(m,1)$. [Two-variable logic](/S7C3C7DJRF/) has the finite model property too, with models of exponential size.
- **[Presburger arithmetic](/4W0E9G7PPV/)** admits quantifier elimination once divisibility predicates $D_n$ are added. The sets of natural numbers it defines are the eventually periodic ones. [Skolem arithmetic](/X86G2FXTPC/) $\mathrm{Th}(\N, \cdot)$ is decidable as well, but adding the successor makes it undecidable.
- **Logic meets automata.** A language of finite words is definable in monadic second-order logic exactly when it is regular. The same holds for infinite words with [Büchi automata](/92DM43HQZT/), and for infinite trees with Rabin tree automata. Each theorem gives a decision procedure: translate the sentence into an automaton and test it for emptiness.
- **[Courcelle's theorem](/DD4JB8XJ5A/).** Every graph property definable in monadic second-order logic with edge-set quantifiers can be decided in time $f(\varphi, k) \cdot n$ on graphs of [treewidth](/FJ5E6FZVRJ/) at most $k$. [Seese's theorem](/RT898AFHWT/) says that a class of finite graphs with a decidable theory of this kind has bounded treewidth.
- **[Essential undecidability](/9JDDFN8PT7/).** A consistent theory is essentially undecidable if every consistent extension in the same language is undecidable. Robinson arithmetic is the standard example, and a consistent theory that interprets it is essentially undecidable too.

## Logics and theories side by side

| Logic or theory | Decidable | Finite model property | Method |
|---|---|---|---|
| First-order logic, a binary relation | no | no | reduction from halting |
| [Monadic predicate calculus](/SERN6CRVWW/) | yes | yes | types of elements |
| [Bernays-Schönfinkel-Ramsey class](/ZF79MZRQ8V/) | yes | yes | domain of the witnesses |
| [Two-variable logic](/S7C3C7DJRF/) | yes, NEXPTIME | yes | Scott normal form, small models |
| Two-variable logic with counting | yes | no | normal form and counting |
| [Guarded fragment](/Y7YS1C3GAE/) | yes, 2EXPTIME | yes | tree-like models |
| [Presburger arithmetic](/4W0E9G7PPV/) | yes | — | quantifier elimination |
| [Skolem arithmetic](/X86G2FXTPC/) | yes | — | weak direct power of $(\N,+)$ |
| $\mathrm{Th}(\N, +, \cdot)$ | no | — | essential undecidability |
| MSO on finite words, [S1S](/YPDXVTH5JR/), [S2S](/PXKKP038RG/) | yes, not elementary | — | automata |

: Which logics and theories are decidable, and how. A dash means the theory is about one fixed infinite structure or a fixed class of words or trees, so the finite model property does not apply.

## Common errors

- **Confusing the two senses of "decides".** A theory decides a sentence $\sigma$ when it proves $\sigma$ or $\neg\sigma$; that is completeness. A theory is decidable when an algorithm sorts its theorems from its non-theorems; that is computability. True arithmetic $\mathrm{Th}(\N,+,\cdot)$ decides every sentence and is undecidable.
- **Taking "monadic" to mean "one variable".** Monadic means every predicate is unary. A monadic sentence may use many variables, and with equality the size of its small model grows with its quantifier rank.
- **Forgetting function symbols.** One unary function symbol is enough to destroy the finite model property: "$f$ is injective and not surjective" has only infinite models.
- **Reversing a reduction.** To show a problem undecidable, reduce a known undecidable problem *to* it. A reduction from the new problem to the halting problem shows only that the new problem is no harder.
- **Reading Seese's theorem as an equivalence.** A decidable theory forces bounded treewidth, but bounded treewidth does not force a decidable theory. Courcelle's theorem makes the theory of the class of all graphs of treewidth at most $k$ decidable, not the theory of each of its subclasses: the paths $P_n$ with $n$ in an undecidable set form a class of treewidth $1$ with an undecidable theory.
