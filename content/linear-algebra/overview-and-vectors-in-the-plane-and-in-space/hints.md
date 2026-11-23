1. Only (b) is linear. For (a), $T(0, 0) = (0, 2) \neq 0$, while a linear map sends $0$ to $0$. For (c), $T(2 \cdot (1, 0)) = (4, 0)$ but $2\,T(1, 0) = (2, 0)$.

3. $u \cdot v = 3 + 0 - 8 = -5$, $\norm{u} = 3$ and $\norm{v} = 5$, so $\cos\theta = -\tfrac13$ and the angle is obtuse, about $109.5^\circ$.

4. The dot product is $3t + 2t - 4 = 5t - 4$, so $t = \tfrac45$ only.

6. $u \cdot v = 5$ and $v \cdot v = 2$, so $p = \left(\tfrac52, 0, \tfrac52\right)$ and $u - p = \left(-\tfrac12, 1, \tfrac12\right)$, whose dot product with $v$ is $-\tfrac12 + \tfrac12 = 0$.

9. Both products equal $(0, 0, 1)$, but $v \neq w$. The cross product is linear, so the equation says $a \times (v - w) = 0$, that is, $v - w$ is a multiple of $a$. Here $v - w = (-1, 0, 0) = -a$.

11. Two sides from $(1, 1, 0)$ are $(2, 1, 1)$ and $(1, 3, 3)$, with cross product $(0, -5, 5)$ of length $5\sqrt{2}$. The area is half of that, $\tfrac{5\sqrt{2}}{2}$.

13. The three vectors lie in one plane through $0$ exactly when their scalar triple product vanishes. The determinant is $1 + k^3 = (k + 1)(k^2 - k + 1)$, and the second factor has no real root, so $k = -1$.

15. With $n = (2, -1, 2)$ we have $n \cdot q = 1$ and $\norm{n} = 3$, so the distance is $\tfrac{\abs{1 - 3}}{3} = \tfrac23$. The nearest point is $q - \tfrac{1 - 3}{9}\, n = \left(\tfrac{22}{9}, \tfrac{7}{9}, -\tfrac{5}{9}\right)$.

17. The directions $(1, 0, 1)$ and $(0, 1, 1)$ are not parallel, and the triple product $(b - a) \cdot (d \times e) = (1, 1, 0) \cdot (-1, -1, 1) = -2$ is not $0$, so the lines do not meet. The distance is $\tfrac{2}{\sqrt{3}}$. Requiring the joining vector to be perpendicular to both directions gives $t = \tfrac13$ and $s = -\tfrac13$, so the points are $\left(\tfrac13, 0, \tfrac13\right)$ and $\left(1, \tfrac23, -\tfrac13\right)$.

21. $Av = (0, -2)$ and $A^2 v = (-2, -6) = 3\,Av - 2v$, so $z^2 - 3z + 2 = (z - 1)(z - 2)$ and $(A - I)(A - 2I)v = 0$. The vector $w = (A - 2I)v = (-2, -2)$ is nonzero and $(A - I)w = 0$, so $(1, 1)$ is an eigenvector with eigenvalue $1$. In the same way $(A - I)v = (-1, -2)$ gives the eigenvector $(1, 2)$ with eigenvalue $2$.

22. Dot both sides of $a \times x = b$ with $a$ to see that $a \cdot b = 0$ is needed. For the converse, apply the vector triple product to $a \times (b \times a)$. Two solutions differ by a vector $y$ with $a \times y = 0$, which is a multiple of $a$. For the example, $a \cdot b = 0$ and $x = \left(-\tfrac12, \tfrac12, 1\right) + t(1, 1, 0)$.

23. Exchange dot and cross: $(a \times b) \cdot (c \times d) = a \cdot \bigl(b \times (c \times d)\bigr)$, then expand $b \times (c \times d) = (b \cdot d)\, c - (b \cdot c)\, d$. For the corollary take $c = a$ and $d = b$.

24. Apply the vector triple product with $u = b \times c$: $u \times (c \times a) = (u \cdot a)\, c - (u \cdot c)\, a = \bigl(a \cdot (b \times c)\bigr)\, c$, since $u \perp c$. Then dot with $a \times b$. Three vectors lie in one plane through $0$ exactly when their triple product is $0$, and the triple product of $a \times b$, $b \times c$, $c \times a$ is the square of that of $a$, $b$, $c$.

25. The expression is $0$ for every $x$: expand and watch the terms cancel. Let $x$ be the point where the altitudes from $a$ and from $b$ meet, so the first two terms are $0$. Then the third is $0$ too, and $x$ lies on the altitude from $c$. The two altitudes meet because they are perpendicular to the non-parallel sides $bc$ and $ca$.

26. Cross $a + b + c = 0$ with $a$, $b$ and $c$ in turn. The lengths give $\norm{a}\,\norm{b} \sin C = \norm{b}\,\norm{c} \sin A = \norm{c}\,\norm{a} \sin B$, because the angle between two side vectors taken around the triangle is $\pi$ minus the interior angle, which has the same sine. Divide by $\norm{a}\,\norm{b}\,\norm{c}$.
