1. ◦ Fix a signature with one binary relation symbol. For each set of sentences, say whether it is computable, computably enumerable but not computable, or not computably enumerable: (a) the valid sentences; (b) the satisfiable sentences; (c) the sentences with a finite model; (d) the sentences true in every finite structure. Name the theorem behind each answer.

2. ◦ Which of these sentences, with no function symbols, lie in the [Bernays-Schönfinkel-Ramsey class](/ZF79MZRQ8V/)? For those that do, give the bound on the size of a model that the class guarantees. (a) $\exists x\, \exists y\, \forall z\, (R(x,z) \to R(z,y))$; (b) $\forall x\, \exists y\, R(x,y)$; (c) $\forall x\, \forall y\, (R(x,y) \to x = y)$; (d) $\exists x\, \forall y\, \exists z\, R(x,y,z)$.

3. ◦ Which of these formulas are in the [guarded fragment](/Y7YS1C3GAE/) as written? (a) $\exists y\, (E(x,y) \land P(y))$; (b) $\forall y\, \forall z\, (T(x,y,z) \to E(y,z))$; (c) $\forall y\, (P(y) \to E(x,y))$; (d) $\exists y\, \exists z\, (E(x,y) \land E(y,z) \land E(z,x))$.

4. ◦ In the language $0, 1, +, <$ of [Presburger arithmetic](/4W0E9G7PPV/), write formulas that define the odd numbers and the numbers congruent to $2$ modulo $3$. Then write each without quantifiers, using the divisibility predicates $D_n$.

5. ◦ In [Büchi arithmetic](/NSTECGT93D/), $V_k(x)$ is the largest power of $k$ dividing $x$, and $V_k(0) = 1$. Compute $V_2(24)$, $V_3(24)$, $V_{10}(300)$ and $V_3(0)$.

6. ◦ Which of these subsets of $\N$ are definable in $(\N, +)$? (a) the perfect squares; (b) $\set{n : n \equiv 1 \pmod 4 \text{ or } n > 100}$; (c) the powers of $2$; (d) $\set{n : n \ge 7}$.

7. ◦ Let $T$ be an inconsistent theory. Is $T$ [decidable](/HWC687ES0Q/)? Is it [essentially undecidable](/9JDDFN8PT7/)? Why does the definition of essential undecidability ask only about consistent extensions?

8. ◦ Over the alphabet $\set{a, b}$, words are structures with an order $<$ on positions and unary predicates $P_a, P_b$. Which of these languages are definable in first-order logic, and which only in monadic second-order logic? (a) words with at least two $a$'s; (b) words of even length; (c) $a^* b^*$. Use the [Büchi-Elgot-Trakhtenbrot theorem](/AK66XQ59Z3/) to check that all three are regular.

9. • Use the decision procedure of the [monadic predicate calculus](/SERN6CRVWW/) to settle the syllogism "some $M$ are $P$; some $S$ are $M$; therefore some $S$ are $P$". If it is invalid, give a countermodel with as few elements as possible.

10. • Let $\sigma = \forall x_1 \dots \forall x_n\, \psi$ with $\psi$ quantifier-free, in a signature with relation symbols and equality but no function or constant symbols. Show that $\sigma$ is satisfiable if and only if it has a model with one element.

11. • Use [Trakhtenbrot's theorem](/XP6FW2WDWT/) to show that there is no computable function $f$ such that every sentence $\sigma$ that has a finite model has one of size at most $f(\abs{\sigma})$.

12. • Write a sentence of [two-variable logic](/S7C3C7DJRF/), reusing variables, that says "every element has an $R$-successor that has an $R$-successor in $P$". Then write one that says "every element starts an $R$-path of length $3$ ending in $P$".

13. • Write a sentence with three variables that says "$R$ is a strict linear order with no greatest element". Show that it has only infinite models. What does this say about the finite model property of first-order logic with three variables?

14. • Eliminate the quantifier in each formula over $(\N, 0, 1, +, <)$, using the predicates $D_n$: (a) $\exists y\, (x = y + y + y \land 0 < y)$; (b) $\exists y\, (x < y + y \land y + y < x + 3)$; (c) $\exists y\, (x < y + y + y \land y + y + y < x + 2)$.

15. • Show that if the graph of multiplication were definable in $(\N, +)$, then $\mathrm{Th}(\N, +, \cdot)$ would be decidable. Conclude that multiplication is not definable in $(\N, +)$, without using periodicity.

16. • In [Skolem arithmetic](/X86G2FXTPC/) $(\N, \cdot)$, define $0$, $1$, the primes and the prime powers. Show that the set $\set{2, 3}$ is not definable.

17. • Over the alphabet $\set{a, b}$, build a deterministic [Büchi automaton](/92DM43HQZT/) with two states for the infinite words in which every $a$ is followed, sooner or later, by a $b$. Describe this language more simply.

18. • Write sentences of monadic second-order logic over graphs, with quantifiers over sets of vertices, that say "the graph is connected" and "the graph is bipartite". By [Courcelle's theorem](/DD4JB8XJ5A/), what follows for graphs of treewidth at most $5$?

19. • Show that the language of finite words over $\set{a, b}$ with as many $a$'s as $b$'s is not definable in monadic second-order logic.

20. • Show that a consistent theory $T$ is essentially undecidable if and only if it has no consistent, complete, decidable extension in the same language.

21. ★ Show that addition is definable in $(\N, S, \cdot)$. Use the identity $(xz + 1)(yz + 1) = z^2(xy + 1) + 1$, which holds when $z = x + y$, and check which other values of $z$ satisfy it. Conclude that $\mathrm{Th}(\N, S, \cdot)$ is undecidable.

22. ★ Call a set $A \subseteq \N$ eventually periodic if there are $N$ and $p \ge 1$ with $n \in A \iff n + p \in A$ for all $n \ge N$. Show that the sets defined by quantifier-free formulas in one variable over $(\N, 0, 1, +, <, D_2, D_3, \dots)$ are eventually periodic. With quantifier elimination, conclude that every subset of $\N$ definable in Presburger arithmetic is eventually periodic.

23. ★ A word $u v^\omega$ is ultimately periodic. Show that two $\omega$-regular languages that contain the same ultimately periodic words are equal. Use the closure properties of the languages of [Büchi's theorem](/YPDXVTH5JR/).

24. ★ Show that $\mathrm{Th}(\Z, +, 0)$ is decidable by interpreting $(\Z, +, 0)$ in $(\N, +)$. Represent an integer by a pair of natural numbers, and say how each formula about $\Z$ becomes a formula about $\N$.

25. ★ Let $S \subseteq \N$ be a set that is not computable, and let $\mathcal C$ be the class of paths $P_n$ with $n$ vertices for $n \in S$. Every graph in $\mathcal C$ has treewidth $1$. Show that even the first-order theory of $\mathcal C$ is undecidable. Why does this not contradict [Seese's theorem](/RT898AFHWT/)?
