1. ◦ How many [structures](/983GZBQYT4/) with domain $\set{1, 2, 3}$ are there for a signature with one unary relation symbol and one constant symbol? How many with domain $\set{1, 2}$ for a signature with one binary function symbol?

2. ◦ Let $\mathcal{M}$ have domain $\set{0, 1, 2}$ and $R^{\mathcal{M}} = \set{(0, 1), (1, 2), (2, 0)}$. Which of these sentences are [true](/K7XDVK5854/) in $\mathcal{M}$: $\forall x \, \exists y \, R(x, y)$; $\; \exists x \, \forall y \, R(x, y)$; $\; \forall x \, \forall y \, (R(x, y) \to \neg R(y, x))$; $\; \forall x \, \forall y \, \forall z \, (R(x, y) \land R(y, z) \to R(x, z))$?

3. ◦ In the structure $(\Z, +, 0)$, decide which of these sentences are true: $\forall x \, \exists y \, (x + y = 0)$; $\; \exists x \, \forall y \, (x + y = y)$; $\; \forall x \, \exists y \, (y + y = x)$.

4. ◦ In $(\N, <)$, for which assignments $s$ does $s$ [satisfy](/2RBQPV02AS/) $x < y \land \exists z \, (x < z \land z < y)$? Answer in terms of $s(x)$ and $s(y)$.

5. ◦ Which of these formulas are [valid](/5SDS9T8E7J/), where $c$ is a constant: $\forall x \, P(x) \to P(c)$; $\; P(c) \to \exists x \, P(x)$; $\; \exists x \, P(x) \to P(c)$; $\; \forall x \, \exists y \, R(x, y) \to \exists y \, \forall x \, R(x, y)$? For each one that is not valid, give a structure in which it fails.

6. ◦ Describe the [Herbrand universe](/NFW38QJ3A7/) and the Herbrand base of the signature with constants $a$ and $b$, a unary function symbol $f$ and a unary relation symbol $P$. Then do the same for the signature with one binary relation symbol $R$ and nothing else, and count its [Herbrand structures](/HKW429DSDK/).

7. ◦ In the evaluation game of [game-theoretic semantics](/D45Z7HETDA/) for $\exists x \, \forall y \, (x \le y)$, which player has a winning strategy in $(\N, \le)$, and which in $(\Z, \le)$? Describe the strategy.

8. • In the language with only equality, write a sentence whose models are exactly the structures with exactly two elements, and one whose models are the structures with at most three elements.

9. • Show that the theory $\set{\forall x \, \neg R(x, x), \; \forall x \, \forall y \, \forall z \, (R(x, y) \land R(y, z) \to R(x, z)), \; \forall x \, \exists y \, R(x, y)}$ has a [model](/MVCH6N9SNW/) but no finite model.

10. • Use the [coincidence lemma](/FM580NZ9W6/) to prove that $\forall x \, (\varphi \to \psi) \leftrightarrow (\varphi \to \forall x \, \psi)$ is valid when $x$ is not free in $\varphi$.

11. • Use the [substitution lemma](/A7S460KHBM/) to prove that $\varphi[t/x] \to \exists x \, \varphi$ is valid whenever $t$ is substitutable for $x$ in $\varphi$.

12. • Find a sentence that is true in $(\Q, <)$ and false in $(\Z, <)$, and a sentence that is true in $(\Z, +)$ and false in $(\N, +)$. Explain why this shows, by [isomorphism invariance](/NDTJ2E895C/), that neither pair is isomorphic.

13. • In $(\Z, <)$, show that the relation $y = x + 1$ is [definable](/1DQ1M6ZWS4/) without parameters, and that no single element is definable without parameters.

14. • Show that the order $<$ is definable without parameters in the field $(\R, +, \cdot)$.

15. • Show that the only subsets of $\R$ that are definable without parameters in $(\R, <)$ are $\emptyset$ and $\R$. Show that the set of positive reals is definable with the parameter $0$.

16. • The signature has a constant $a$, a unary function symbol $f$ and a unary relation symbol $P$. Find all Herbrand models of $\set{P(a), \; \forall x \, (P(x) \leftrightarrow \neg P(f(x)))}$, and give a model of the same set with two elements.

17. • Decide which of these sentences are valid, with a proof or a countermodel for each: $\exists x \, \forall y \, (D(x) \to D(y))$; $\; \exists x \, (\forall y \, D(y) \to D(x))$; $\; \exists x \, \exists y \, (D(x) \to \neg D(y))$. Compare the first with the [drinker paradox](/8BMQTZZEWB/).

18. ★ Let $\varphi(x, y)$ be quantifier-free. Prove that Eloise has a winning strategy in the evaluation game for $\forall x \, \exists y \, \varphi$ in $\mathcal{M}$ if and only if there is a function $g \colon M \to M$ with $\mathcal{M} \models \varphi[a, g(a)]$ for every $a \in M$.

19. ★ Prove that every element of $(\N, <)$ is definable without parameters. Deduce that some subset of $\N$ is not definable in $(\N, <)$, even with parameters.

20. ★ Let $\mathcal{M}$ be a [substructure](/676H7EGTKJ/) of $\mathcal{N}$. Prove that for every quantifier-free formula $\varphi$ and every assignment $s$ into $M$, $\mathcal{M} \models \varphi[s]$ if and only if $\mathcal{N} \models \varphi[s]$. Deduce that every universal sentence true in $\mathcal{N}$ is true in $\mathcal{M}$.

21. ★ Let $\Sigma$ be a set of universal sentences without equality, in a signature with at least one constant, and let $\mathcal{M}$ be a model of $\Sigma$. Define a Herbrand structure $\mathcal{H}$ by putting $R(t_1, \ldots, t_n)$ true in $\mathcal{H}$ exactly when $(t_1^{\mathcal{M}}, \ldots, t_n^{\mathcal{M}}) \in R^{\mathcal{M}}$. Prove that $\mathcal{H}$ is a model of $\Sigma$.
