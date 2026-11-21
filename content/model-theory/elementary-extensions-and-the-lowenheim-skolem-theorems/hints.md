1. (a) No: $\forall y\, \neg(y < x)$ holds of $0$ in $\N$ and fails of $0$ in $\Z$. (b) No: $\exists z\, (x < z \wedge z < y)$ holds of $0, 1$ in $\Q$ and fails in $\Z$. (c) Yes: both orders are dense without endpoints, and every embedding between such orders is elementary. (d) No: $\exists y\, (y + y = x)$ holds of $1$ in $\Q$ only. (e) No: $\exists y\, (y + y = x)$ holds of $2$ in $\Z$, with $y = 1$, and fails of $2$ in $2\Z$.

3. (a) Yes, by the downward theorem with $\kappa = \aleph_0$ and $A = \set{\pi, e}$. (b) Yes, by the upward theorem. (c) No: an infinite structure satisfies "there are at least $n$ elements" for every $n$. (d) Yes: $\Q$ itself, since $(\Q, <) \preceq (\R, <)$ already covers formulas with rational parameters, and naming them changes nothing. (e) No: every substructure contains the values of all constants, so the only one is $\R$.

4. Eighteen: one for each of the nine atomic sentences $c_i < c_j$ and the nine atomic sentences $c_i = c_j$, with $i, j \in \set{0, 1, 2}$. Six are atomic, namely $c_0 < c_1$, $c_0 < c_2$, $c_1 < c_2$ and $c_i = c_i$, and twelve are negated: $\neg(c_i < c_j)$ for $i \ge j$ and $\neg(c_i = c_j)$ for $i \ne j$.

6. No. $M_1 = \Z$ and $M_2 = \tfrac{1}{2}\Z$: the formula $\exists y\, (y + y = x)$ holds of $1$ in $M_2$, with $y = \tfrac{1}{2}$, and fails in $M_1$. If the chain were elementary, the theorem would give $(\Z, +) \preceq (\Q, +)$ and so $(\Z, +) \equiv (\Q, +)$, which is false.

9. (a) For $\bar a$ in $M$, both $\mathcal{M} \models \varphi(\bar a)$ and $\mathcal{M}' \models \varphi(\bar a)$ are equivalent to $\mathcal{N} \models \varphi(\bar a)$. (b) $\overline{\Q} \preceq \C$ because embeddings of algebraically closed fields are elementary. The formula $\exists y\, (y \cdot y = x)$ holds of $\pi$ in $\C$ and fails in $\overline{\Q}(\pi)$, which is isomorphic to the field of rational functions $\overline{\Q}(t)$, where $t$ is not a square.

14. Exactly when $a = b$. The identity of $\R$ gives an amalgam with $g_1(a) = g_2(a)$. If $a < b$, choose a rational $q$ with $a < q < b$; then $g_1(a) < g_1(q) = g_2(q) < g_2(b)$ in every amalgam.

16. Take an elementary extension $\mathcal{N}$ of size $\aleph_1$, an element $b \in N \setminus \Z$, and a countable $\mathcal{N}' \preceq \mathcal{N}$ that contains $\Z \cup \set{b}$; then $(\Z, <) \preceq \mathcal{N}'$. No element of $\mathcal{N}'$ lies strictly between $n$ and $n + 1$, so $b$ lies above all of $\Z$ or below all of it. Then infinitely many elements lie between $0$ and $b$, while in $\Z$ only finitely many lie between any two elements.

17. If $X$ has exactly $k$ elements, the formula "there are exactly $k$ elements $y$ with $\varphi(\bar a, y)$" holds in $\mathcal{N}$, so it holds in $\mathcal{M}$. The $k$ witnesses in $M$ lie in $X$, so they are all of $X$. For the example, take $(\Q, <) \preceq (\R, <)$ and $\varphi(x_1, x_2, y) = x_1 < y \wedge y < x_2$.

18. $F$ is a subfield of $\C$, and it is algebraically closed, because a root of a polynomial over $F$ is algebraic over $\Q(\pi)$; so $F \preceq \C$. If $\mathcal{K} \preceq \C$ contains $\pi$ and $\alpha \in F$, clear denominators in the minimal polynomial of $\alpha$ over $\Q(\pi)$: its roots form a finite set defined with the parameter $\pi$, and the previous exercise puts them in $K$.

19. Let $\mathcal{N} \succ \R$ and $b \in N \setminus \R$. If $\abs{b} > n$ for every integer $n$, the field $\mathcal{N}$ is already non-Archimedean. Otherwise let $r$ be the supremum of the reals below $b$. Then $d = b - r$ is nonzero and $\abs{d} < 1/m$ for every $m \ge 1$, so $1/\abs{d}$ exceeds every integer. Such extensions exist by the upward theorem. A set of sentences true in $\R$ is true in $\mathcal{N}$ as well.

20. $(\R, <)$ and the order $\R + \Q$, a copy of $\R$ followed by a copy of $\Q$. The first sits in the second as its initial part; the second embeds into $\R$ by $x \mapsto -e^{-x}$ on the copy of $\R$ and $q \mapsto e^{q}$ on the copy of $\Q$. They are not isomorphic: in $\R + \Q$ the copy of $\R$ is bounded above but has no least upper bound.
