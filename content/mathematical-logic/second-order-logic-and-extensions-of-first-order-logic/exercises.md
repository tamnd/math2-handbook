1. ◦ Which of these are formulas of [second-order logic](/G6X7SZSNC5/), and which of those are formulas of [monadic second-order logic](/3WHQFSHR58/)? Here $X$ is unary, $Y$ and $Z$ are binary, and $\mathcal{X}$ has type $((\iota))$. (a) $\exists X\, \forall x\, (X(x) \lor \neg X(x))$. (b) $\forall Y\, \exists Z\, \forall x\, \forall y\, (Y(x, y) \leftrightarrow Z(y, x))$. (c) $\exists X\, X(X)$. (d) $\forall \mathcal{X}\, \exists X\, \mathcal{X}(X)$.

2. ◦ Write the [comprehension](/5GS6DRJ5SY/) axiom for each formula, and say whether it is predicative or impredicative. (a) $\varphi(x) = \exists y\, E(y, x)$, with $n = 1$. (b) $\varphi(x, y) = E(y, x)$, with $n = 2$. (c) $\varphi(x) = \forall Y\, (Y(c) \to Y(x))$, with $n = 1$. Which set does (c) define in the full semantics?

3. ◦ Give the order of each type: $(\iota, \iota)$, $(\iota, (\iota))$, $((\iota, \iota))$ and $(((\iota)))$. Which of them may occur in third-order logic?

4. ◦ Hume's principle has a model with domain $\N$, in which $\#F = |F| + 1$ for finite $F$ and $\#F = 0$ for infinite $F$. In this model, compute the objects $0 := \#[x : x \neq x]$, $\#[x : x = 3 \lor x = 7]$ and $\#[x : x \text{ is even}]$. Decide whether $P(1, 2)$ and $P(0, 0)$ hold, with $P$ as in [Frege's theorem](/J36EHBHF6J/).

5. ◦ Words over $\set{a, b}$ are read as structures with an order and the letter predicates $P_a$, $P_b$. Which of these languages are definable in monadic second-order logic? (a) $a^* b^*$. (b) The words with as many $a$'s as $b$'s. (c) The words whose length is a multiple of $3$. (d) The words whose length is a perfect square.

6. ◦ Compare the [Henkin quantifier](/KMNVEGS34N/) sentence $Q_H x_1 x_2 y_1 y_2\, (y_2 = x_1)$ with the linear sentence $\forall x_1\, \exists y_1\, \forall x_2\, \exists y_2\, (y_2 = x_1)$. In which structures is each one true?

7. ◦ Let $X$ be the team over $x, y, z$ with the four assignments $(x, y, z) = (0, 0, 1), (0, 1, 1), (1, 0, 0), (1, 1, 0)$. Which of the [dependence](/DNAPTJ98WD/) atoms $=\!(x, z)$, $=\!(x, y)$, $=\!(y, z)$, $=\!(z)$ and $=\!(x, y, z)$ does $X$ satisfy?

8. ◦ Which of these classes are [generalized quantifiers](/MFV98WTF4G/) of type $\langle 1 \rangle$? (a) $\set{(M, A) : A = \emptyset}$. (b) $\set{(M, A) : |A| = |M \setminus A|}$. (c) $\set{(M, A) : M = \N \text{ and } A \text{ is finite}}$. (d) $\set{(M, A) : |A| \text{ is even or infinite}}$.

9. ◦ A quantifier $Q$ of type $\langle 1, 1 \rangle$ is conservative when $Q_M(A, B)$ holds exactly when $Q_M(A, A \cap B)$ holds. Which of "no $A$ are $B$", "exactly two $A$ are $B$" and "only $A$ are $B$" are conservative?

10. • Write a second-order sentence in the empty vocabulary that is true, in the full semantics, exactly in the structures whose domain is countable (finite or countably infinite).

11. • Write a monadic second-order formula saying that a binary relation $<$ is a well-order. Use it to show that monadic second-order logic, with the full semantics, is not compact.

12. • Use comprehension to derive $\forall X\, (X(y) \to X(x))$ from $\forall X\, (X(x) \to X(y))$. Which instance do you use, and is it predicative?

13. • Let $\mathrm{Fin}$ be the second-order sentence that, in the full semantics, holds exactly in the finite structures. Show that $\mathrm{Fin}$ has an infinite model in the [Henkin semantics](/KWEJFK5943/). What must the family $D_2$ of that model lack?

14. • Write a third-order sentence saying that every family of sets of individuals has an intersection. Is it valid in the standard semantics of [higher-order logic](/K40YJX8K1G/)? What is the intersection of the empty family?

15. • In Frege arithmetic, let $1 := \#[x : x = 0]$. Use Hume's principle to prove $0 \neq 1$ and $P(0, 1)$.

16. • Frege's Basic Law V says $\varepsilon F = \varepsilon G \leftrightarrow \forall x\, (F(x) \leftrightarrow G(x))$. Show, without Russell's paradox, that it has no full model: use [Cantor's theorem](/0WTEMGYV2C/). Why does the same argument not refute Hume's principle?

17. • Write a monadic second-order sentence that defines, among the words over $\set{a, b}$, those with an even number of $a$'s.

18. • A finite simple graph has a cycle exactly when some nonempty set of vertices has every member adjacent to at least two members of the set. Prove this, and use it to write an $\mathrm{MSO}_1$ sentence true exactly in the finite forests.

19. • Show that every dependence atom is satisfied by the empty team and is closed under subteams. Then show that the team $\set{x \mapsto 0, x \mapsto 1}$ satisfies $=\!(x) \lor =\!(x)$ but not $=\!(x)$.

20. • The Henkin sentence $Q_H x_1 x_2 y_1 y_2\, ((x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq x_1 \land (x_2 = y_1 \to y_2 = x_1))$ is true exactly in the structures whose size is even or infinite. Write a dependence logic sentence with the same models, and check it on a domain with $4$ elements.

21. • The Härtig quantifier $I$ has $I\, x\, (\varphi(x), \psi(x))$ true when as many elements satisfy $\varphi$ as $\psi$. Show that $Q_0\, x\, \varphi(x)$ ("infinitely many") is expressible in $L(I)$.

22. ★ Write a sentence of full second-order logic in the empty vocabulary whose models are exactly the sets of size $2^{\aleph_0}$. Conclude that full second-order logic fails both Löwenheim–Skolem theorems.

23. ★ Write a sentence of full second-order logic in the empty vocabulary that is valid if and only if the [continuum hypothesis](/0MN2MER9WN/) holds.

24. ★ Find a sentence of $L(Q_0)$ whose models are exactly the linear orders isomorphic to $(\N, <)$. Use it to show that $L(Q_0)$ fails the upward Löwenheim–Skolem theorem, and give a countable set of $L(Q_0)$ sentences, different from the one in the entry, that shows it is not compact.

25. ★ Prove the fourth sentence of Frege's theorem from Hume's principle: if $P(m, n)$ and $P(m', n)$, then $m = m'$.

26. ★ The axioms of an ordered field together with the second-order completeness axiom have, in the full semantics, only models isomorphic to $\R$. Show that they have a countable Henkin model, and explain why this does not contradict the uncountability of $\R$.
