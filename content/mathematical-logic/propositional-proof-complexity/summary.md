## What to remember

- **Proof systems.** A propositional proof system is a polynomial-time function $f$ from strings onto the set of tautologies; an $f$-proof of $\tau$ is any $w$ with $f(w) = \tau$. The system $g$ **p-simulates** $f$ if a polynomial-time function turns every $f$-proof into a $g$-proof of the same tautology.
- **Cook-Reckhow theorem.** A polynomially bounded proof system exists if and only if $\mathrm{NP} = \mathrm{coNP}$. Superpolynomial lower bounds for every system would give $\mathrm{NP} \ne \mathrm{coNP}$, hence $\mathrm{P} \ne \mathrm{NP}$.
- **Frege and extended Frege.** All Frege systems are p-equivalent (Reckhow). Extended Frege adds axioms $q \leftrightarrow \varphi$ for a variable $q$ new to $\varphi$, to the earlier lines and to the conclusion. Both prove the pigeonhole formulas in polynomial size, and for neither is a superpolynomial lower bound known; the best bounds on Frege size are quadratic.
- **Resolution** refutes a CNF by deriving $C \cup D$ from $C \cup \set{x}$ and $D \cup \set{\neg x}$ until the empty clause $\square$ appears. Tree-like resolution is weaker than regular resolution, which is weaker than general resolution. A DPLL run gives a tree-like refutation with one clause per node of its search tree.
- **Haken's theorem.** Every resolution refutation of $\mathrm{PHP}^{n+1}_n$ has at least $c^n$ clauses for a constant $c > 1$; the proof on the site gives $(11/10)^{\floor{n/20}}$ for $n \ge 20$.
- **Size and width.** For an unsatisfiable CNF $F$ in $n$ variables, $S_T(F \vdash \square) \ge 2^{w(F \vdash \square) - w(F)}$, and $S(F \vdash \square) \ge \exp\bigl((w(F \vdash \square) - w(F) - 1)^2 / 8n\bigr)$. So linear refutation width for a CNF of bounded width forces size $2^{\Omega(n)}$, as for the Tseitin formulas on bounded-degree expanders (Urquhart).
- **Tseitin formulas.** $T(G, \chi)$ says that the edges at each vertex $v$ add up to $\chi(v)$ modulo $2$; for connected $G$ it is unsatisfiable exactly when $\sum_v \chi(v)$ is odd.
- **Systems in between.** Bounded-depth Frege needs size $2^{n^{\varepsilon_d}}$ for the pigeonhole formulas in depth $d$ (Ajtai; Krajíček–Pudlák–Woods; Pitassi–Beame–Impagliazzo). Cutting planes refutes them in $O(n^3)$ lines but needs exponential length for the clique-coloring formulas (Pudlák). Polynomial calculus needs degree at least $n/2 + 1$ for them (Razborov).
- **Interpolation and search.** Resolution has monotone feasible interpolation, with at most $4L$ gates for a refutation of $L$ clauses. Resolution is not automatizable unless $\mathrm{P} = \mathrm{NP}$ (Atserias-Müller), while a refutation of width $w$ is found in time $n^{O(w)}$.

## Proof systems compared

| System | $\mathrm{PHP}^{n+1}_n$ | Tseitin, expander, odd charge | Feasible interpolation | Proof search |
|---|---|---|---|---|
| [Truth tables](/67MYPBSHCJ/) | exponential | exponential | yes, trivially | automatizable, trivially |
| Tree-like [resolution](/6JSH907W5R/) | exponential | exponential | yes, monotone | quasi-polynomial time |
| General resolution | exponential | exponential | yes, monotone | not automatizable unless $\mathrm{P} = \mathrm{NP}$ |
| [Cutting planes](/KKCX2HQP2K/) | $O(n^3)$ lines | quasi-polynomial | monotone real circuits | NP-hard to automate |
| [Polynomial calculus](/ZERBQSTZB5/) | degree $\ge n/2 + 1$ | polynomial over $\F_2$; exponential in characteristic $\ne 2$ | — | degree $d$ in time $n^{O(d)}$; NP-hard to automate |
| [Bounded-depth Frege](/41QJ1WEMJ3/) | $2^{n^{\varepsilon_d}}$ | — | no, under a Diffie-Hellman assumption | no, under the same assumption |
| [Frege](/J2BAR09TPF/) | polynomial | polynomial | no, under a Diffie-Hellman assumption | no, under the same assumption |
| [Extended Frege](/5YSE04SHFH/) | polynomial | polynomial | no, unless RSA is insecure | no, unless RSA is insecure |

: Eight systems, roughly from weak to strong, though cutting planes, polynomial calculus and bounded-depth Frege do not form a chain. The second and third columns give the size of the shortest refutations, and "exponential" means $2^{\Omega(n)}$ or $2^{n^{\varepsilon}}$ for $n$ the number of pigeons or vertices; a dash marks a question the chapter does not settle.

## Common errors

- **Transferring a bound the wrong way.** If $g$ p-simulates $f$, short $f$-proofs give short $g$-proofs, and lower bounds for $g$ give lower bounds for $f$. A lower bound for resolution says nothing about cutting planes or Frege.
- **Confusing lines with size.** A Frege or cutting-planes proof with few lines can have huge lines or huge coefficients.
- **Reading one lower bound as a separation of classes.** By the Cook-Reckhow theorem, $\mathrm{NP} \ne \mathrm{coNP}$ needs a lower bound for every proof system, not for one.
- **Forgetting $w(F)$ in the size-width relation.** A CNF with wide clauses can have large refutation width and short refutations.
- **Treating conditional results as theorems.** The results against interpolation and search for Frege and extended Frege assume that some cryptography is secure.
- **Mixing up hard to find and hard to have.** Automatizability compares the search time with the shortest proof, not with the size of the formula.
