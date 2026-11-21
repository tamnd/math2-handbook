1. (a) $3$. (b) $2$. (c) $2$. (d) $3$. (e) $2$.

4. (a) $2$. (b) $2$. (c) $4$, since $15 = 2^4 - 1$ but $15 < 2^5 - 1$. (d) $5$, since $31 = 2^5 - 1$.

5. (a) Yes; the orders are even isomorphic, by Cantor's theorem. (b) No: $\Q \cap [0, 1]$ has a least element, so the orders are not elementarily equivalent. (c) Yes: both are dense without endpoints, so the finite order-preserving maps form a back-and-forth system, although the orders are not isomorphic. (d) No: $(\N, <)$ has a least element.

8. Spoiler picks $3$, which has three elements below it and three above. An answer $j$ in $L_6$ has $j$ elements below it and $5 - j$ above, and one of these numbers is at most $2$. Spoiler then plays the remaining two rounds on that side, where three elements face at most two, and $3 = 2^2 - 1$.

11. Yes, for odd $n$. Then $K_{n,n}$ has $n^2$ edges, an odd number, and $K_{n,n+1}$ has $n(n+1)$, an even number. Since a win in $G_n$ gives a win in every shorter game, the odd values of $n$ are enough.

12. (a) $4$. Since $9, 10 \ge 2^3 - 1$, we have $L_9 \equiv_3 L_{10}$. With four rounds the classes of $\equiv_4$ are $\set{L_m}$ for $m \le 14$ and $\set{L_m : m \ge 15}$. Each class is defined by a Hintikka sentence of rank $4$, and "at least $10$ elements" is the disjunction of six of them. (b) $10$, since sets with $9$ and $10$ elements are $\equiv_9$, and $\exists x_1 \cdots \exists x_{10} \bigwedge_{i < j} x_i \neq x_j$ has rank $10$.

13. Yes. Between any two rationals there is an element of $D$ and an element outside $D$, and the same holds for $T$. So the finite order-preserving maps that send $D$-points to $T$-points and the other points to other points form a back-and-forth system, and both structures are countable.

14. Both orders are dense without endpoints, so the finite order-preserving maps form a back-and-forth system. The first copy of $\R$ in $\R + \R$ is nonempty and bounded above but has no least upper bound, while every such subset of $\R$ has one.

16. $n = 3$. In $G_2$, Duplicator answers the least element by the least element and any other element by a non-least element; in the second round only the relative order of two points matters, and she can always match it. The sentence $\exists x\, (\exists y\, (y < x) \wedge \forall y\, (y < x \to \exists z\, (y < z \wedge z < x)))$ has rank $3$; its witness in $\omega \cdot 2$ is the least element of the second copy.

17. Treat the least element as chosen before the game. With $k$ rounds left, Duplicator keeps the distances between consecutive chosen points equal, or both at least $2^k - 1$, where a point of the $\zeta$ part counts as infinitely far from every point of the $\N$ part. This is the strategy for finite linear orders, run with no right endpoint. The orders are countable and not isomorphic, since $\omega + \zeta$ has an element with infinitely many predecessors, so they are not partially isomorphic.

18. With $k$ rounds left, Duplicator keeps $d(a_i, a_j) = d(b_i, b_j)$ or both greater than $2^k$, where points in different components are at infinite distance. If Spoiler's new point lies within $2^{k-1}$ of a chosen point, she copies its position relative to that point, on the matching side. Otherwise she picks a point at distance more than $2^{k-1}$ from all chosen points, which exists because the cycles have at least $2^{n+1}$ vertices.

19. If the conditions hold, Duplicator answers an old element by its partner, and a new element by a new element of the same kind; she cannot run out in $n$ rounds. If, say, $\abs{P} = j < n$ and $\abs{Q} > j$, then "at least $j + 1$ elements satisfy $P$" has rank $j + 1 \le n$ and separates the structures.

20. Duplicator plays the two winning strategies side by side: a move in $\mathcal{A}$ or $\mathcal{A}'$ is answered by the strategy for that pair, and a move in $\mathcal{B}$ or $\mathcal{B}'$ by the other. Every point of the lower part lies below every point of the upper part on both sides, so the union of the two partial isomorphisms is one. For the example, $L_{63} \equiv_6 L_{64}$ because $63 = 2^6 - 1$.
