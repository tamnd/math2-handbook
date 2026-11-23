1. (a) Second-order and monadic. (b) Second-order, not monadic, since $Y$ and $Z$ are binary. (c) Not a formula: no type $\tau$ equals $(\tau)$. (d) A third-order formula, not a second-order one.

2. (a) $\exists X\, \forall x\, (X(x) \leftrightarrow \exists y\, E(y, x))$, predicative. (b) $\exists Z\, \forall x\, \forall y\, (Z(x, y) \leftrightarrow E(y, x))$, predicative. (c) $\exists X\, \forall x\, (X(x) \leftrightarrow \forall Y\, (Y(c) \to Y(x)))$, impredicative; it defines $\set{c}$, since $Y = \set{c}$ forces $x = c$.

4. $0$ is the number $1$, $\#[x : x = 3 \lor x = 7] = 3$ and $\#[x : x \text{ is even}] = 0$. Both hold: $F = \set{5}$ with $y = 5$ gives $P(1, 2)$, and $F = \N$ with $y = 0$ gives $P(0, 0)$, because $\N \setminus \set{0}$ is infinite.

6. The Henkin sentence asks for $g$ with $g(a_2) = a_1$ for all $a_1, a_2$, so it is true only in the one-element structures. The linear sentence is true in every structure: take $y_2 = x_1$.

7. $=\!(x, z)$ and $=\!(x, y, z)$ hold. $=\!(x, y)$ fails at the first two rows, $=\!(y, z)$ fails at the first and third, and $=\!(z)$ fails because $z$ takes two values.

10. $\exists z\, \exists F\, \big(\mathrm{Func}(F) \land \forall X\, ((X(z) \land \forall x\, \forall y\, (X(x) \land F(x, y) \to X(y))) \to \forall x\, X(x))\big)$, where $\mathrm{Func}(F)$ says that $F$ is the graph of a function. The orbit of $z$ under the function is the whole domain, and a countable domain has an enumeration that serves as the function.

11. Take the axioms of a linear order and $\forall X\, (\exists x\, X(x) \to \exists x\, (X(x) \land \forall y\, (X(y) \to \neg\, y < x)))$. Add constants $c_0, c_1, \ldots$ and the sentences $c_{n+1} < c_n$: each finite subset has a model in $\N$, but the whole set has none, since $\set{c_n}$ has no least element.

13. Each finite subset of $\set{\mathrm{Fin}} \cup \set{\lambda_n : n \ge 2}$ has a finite full model, and full models are Henkin models. Henkin compactness gives an infinite Henkin model. Its $D_2$ contains the graph of no injective function that misses a point.

18. For the converse, take a longest path inside the set. Its last vertex has a second neighbor in the set besides its predecessor, and by maximality that neighbor lies on the path, which closes a cycle. The forests satisfy the negation of $\exists X\, (\exists x\, X(x) \land \forall x\, (X(x) \to \exists y\, \exists z\, (y \neq z \land X(y) \land X(z) \land E(x, y) \land E(x, z))))$.

20. $\forall x_1\, \exists y_1\, \forall x_2\, \exists y_2\, (=\!(x_2, y_2) \land \varphi)$, with $\varphi$ the same matrix. On $\set{1, 2, 3, 4}$ choose $y_i = f(x_i)$ with $f$ the involution that swaps $1, 2$ and swaps $3, 4$.

21. An infinite set $A$ is equinumerous with $A \setminus \set{a}$ for each $a \in A$, and a finite one is not. So $Q_0\, x\, \varphi(x)$ is equivalent to $\exists a\, (\varphi(a) \land I\, x\, (\varphi(x), \varphi(x) \land x \neq a))$.

22. Quantify over relations $<$, $+$ and $\cdot$ (the last two ternary) and over two individuals for $0$ and $1$, and say that they form an ordered field with the completeness axiom. A domain carries such a structure exactly when it is in bijection with $\R$, that is, when it has size $2^{\aleph_0}$. So the sentence has an uncountable model but no countable one, and no model larger than $2^{\aleph_0}$.

23. Let $\rho$ be the sentence of exercise 22 without its outer existential quantifiers, so that $\rho$ has free relation variables. Take $\forall \bar R\, \big(\rho \to \forall X\, (\mathrm{Count}(X) \lor X \approx V)\big)$, where $\mathrm{Count}(X)$ is exercise 10 relativized to $X$ and $V$ is the whole domain. If the domain is not of size $2^{\aleph_0}$, the hypothesis is false; if it is, the sentence says that every subset of $\R$ is countable or of size $2^{\aleph_0}$.

24. Take the axioms of a linear order, $\forall x\, \neg Q_0\, y\, (y < x)$ and $Q_0\, x\, (x = x)$. Sending each element to its number of predecessors gives an isomorphism onto $\N$. For non-compactness, add a constant $c$ and, for each $n$, the first-order sentence saying that $c$ has at least $n$ predecessors.

25. Take $F, y$ for $P(m, n)$ and $G, z$ for $P(m', n)$, so that $F \approx G$ by a bijection $R$. Change $R$ at two points so that it sends $y$ to $z$, and restrict it to a bijection from $F \setminus \set{y}$ onto $G \setminus \set{z}$. Comprehension with parameters gives the new relation, and Hume's principle gives $m = m'$.

26. Henkin's Löwenheim–Skolem theorem gives a model in which $M$ and every $D_n$ are countable. The proof that a complete ordered field is uncountable applies completeness to a set built from a given enumeration of the field. In the Henkin model that set need not lie in $D_1$, so the argument cannot be carried out with the model's own sets. Seen from outside, the model is countable, as in Skolem's paradox.
