2. Only the coordinates $2$ and $3$ matter, so the reduced product is $\Z/3\Z \times \Z/5\Z$. It has $15$ elements, and by the Chinese remainder theorem it is the ring $\Z/15\Z$.

4. (a) Infinitesimal; it is positive when $U$ contains the even numbers and negative otherwise, so its sign depends on $U$. (b) Positive and infinite, since $n^2 - 100n > r$ for all large $n$. (c) Neither: it is finite, greater than $1$, and $c - 1$ is a positive infinitesimal.

6. (a) $5$, since a finite structure is isomorphic to each of its ultrapowers. (b) $2^{\aleph_0}$: the ultraproduct is infinite because "at least $k$ elements" holds for $n \ge k$, and an infinite ultraproduct of a countable family over a nonprincipal ultrafilter on $\N$ has at least $2^{\aleph_0}$ elements, while the full product has only $2^{\aleph_0}$. (c) $2^{\aleph_0}$. (d) $8$, by [Łoś's theorem](/AGYBSTD7BG/) for the sentence "exactly $8$ elements".

8. (a), (d) and (e) are Horn sentences, so they are preserved. (b) holds in $\R$ and fails in $\R^{\N}$ modulo the cofinite filter, where $(1, 0, 1, 0, \ldots)$ has no inverse. (c) holds in $(\N, \le)$ and fails in $(\N, \le)^{\N}$ modulo the cofinite filter, where $(0, 1, 0, 1, \ldots)$ and $(1, 0, 1, 0, \ldots)$ are incomparable.

9. If $p > k$, multiplication by $k$ is a bijection of $\Z/p\Z$; since a nonprincipal ultrafilter contains every cofinite set, both "$kx = 0 \to x = 0$" and "$\exists y\, (ky = x)$" pass to $G$. A torsion-free divisible group is a vector space over $\Q$, and $G$ has $2^{\aleph_0}$ elements, so its dimension is $2^{\aleph_0}$.

11. (a) Since $\left(\frac{-1}{p}\right)\left(\frac{2}{p}\right) = \left(\frac{-2}{p}\right)$, the three Legendre symbols cannot all be $-1$, and for $p = 2$ every element is a square. So the sentence $\exists x\, (x^2 = -1 \vee x^2 = 2 \vee x^2 = -2)$ holds in every $\F_p$. (b) By quadratic reciprocity, for $p > 3$ the number $3$ is a square mod $p$ exactly when $p \equiv \pm 1 \pmod{12}$; take $S = \set{p : p \equiv \pm 1 \pmod{12}}$. Adding $2$ and $3$ to $S$ changes nothing, because $U$ is nonprincipal.

13. Take $x = [(0)_n]$ and $y = [(n)_n]$. For each $k$, the sentence "there is no path of length at most $k$ from $x$ to $y$" holds in $P_n$ for every $n > k$, so it holds in the ultraproduct. The ultraproduct is therefore not connected, although every factor is.

16. For $a < b$ the formula "$a < x < b \to x = a+1 \vee \cdots \vee x = b-1$", with $a, a+1, \ldots, b$ as parameters, holds in $\Z$; the diagonal map is elementary. The elements $[(-n)_n]$ and $[(n)_n]$ lie below and above the whole image.

17. No. The real field satisfies, for each formula $\varphi(x, \bar y)$, the sentence saying that a nonempty set defined by $\varphi$ that is bounded above has a least upper bound, so $^*\R$ satisfies it too. The infinitesimals are nonempty and bounded by $1$, but a least upper bound $s$ is impossible: if $s$ is infinitesimal then so is $2s > s$, and if not, then $s/2$ is a smaller upper bound.

18. Let $X_k$ be the set of $n \ge k$ with $a_0(n) < \cdots < a_k(n) < b(n)$. The $X_k$ decrease, lie in $U$ and have empty intersection. For $n \in X_k \setminus X_{k+1}$ put $c(n) = (a_k(n) + b(n))/2$. Then $a_k(n) < c(n) < b(n)$ for all $n \in X_k$. This is the $\aleph_1$-saturation of countably incomplete ultraproducts in a countable language.

19. Every element is even or odd, by Łoś's theorem. So a nonstandard $\omega$ has a $\nu$ with $\omega = 2\nu$ or $\omega = 2\nu + 1$; then $\nu$ and $\omega - \nu$ are nonstandard, so $\nu$ lies in a lower class. The element $2\omega$ lies in a higher class. For $x < y$ in different classes, the integer part of $(x + y)/2$ lies strictly between their classes.

20. For $f : I \to \N$, the sets $f^{-1}(\set{n})$ are countably many and partition $I$. If none were in $U$, their complements would all be in $U$, and so would their intersection, which is empty. So $f$ is constant on a set in $U$, and $[f]$ is in the image of the diagonal map.
