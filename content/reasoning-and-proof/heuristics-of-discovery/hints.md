1. ◦ (a), (c) and (e) are heuristics: they say what to try and may lead nowhere. (b) and (d) are algorithms: every step is fixed and they end with the correct result.

3. ◦ The values are $3, 7, 31, 127$, all prime. The conjecture "$2^p - 1$ is prime for every prime $p$" fails first at $p = 11$: $2^{11} - 1 = 2047 = 23 \cdot 89$.

4. ◦ (a) With inner radius $0$ the chord is a diameter, so the outer radius is $5$ and the area is $25\pi$. (b) The radius to the point of contact is perpendicular to the chord and bisects it, so $R^2 = r^2 + 5^2$ and the area is $\pi(R^2 - r^2) = 25\pi$.

5. ◦ Five litres in the large jug come from pouring a full large jug into a small jug holding $1$ litre, and $1$ litre in the small jug comes from $1$ litre in the large jug. Moves: fill the large jug, pour into the small one, empty the small one, pour again, empty again, pour the remaining litre into the small jug, fill the large jug, pour into the small one until it is full. Eight moves, which is the least possible.

7. ◦ Reflect $A$ in the $x$-axis to $A' = (0, -3)$. The line $A'B$ is $y = 2x - 3$ and meets the axis at $P = (\frac{3}{2}, 0)$; the least value is $A'B = \sqrt{80} = 4\sqrt 5$.

9. ◦ $F = 6 + 5 = 11$ and $V - E + F = 16 - 24 + 11 = 3$. The surface is a topological sphere, but the top face of the large cube is a ring, not a disc; the proof treats each face as a polygon that can be cut into triangles by diagonals.

15. • $2^{2026} \equiv 0 \pmod 8$. Since $2^{100} \equiv 1 \pmod{125}$, $2^{2026} \equiv 2^{26} \equiv 114 \pmod{125}$. The number below $1000$ that is $114$ modulo $125$ and divisible by $8$ is $864$.

19. • For $P_n \le 1/\sqrt{3n}$ the step needs $(2n+1)^2 (n+1) \le n (2n+2)^2$, which reduces to $n + 1 \le 0$ and is false. For the stronger claim, $P_1 = \frac{1}{2} = 1/\sqrt 4$, and the step needs $(2n+1)^2 (3n+4) \le (2n+2)^2 (3n+1)$; the right side minus the left side is $n \ge 0$. The stronger statement gives the induction a stronger hypothesis.

21. ★ The earlier $n - 1$ planes cut the $n$th plane in $n - 1$ lines in general position, which divide it into $1 + (n - 1) + \binom{n-1}{2}$ regions, and each of these splits one region of space in two. Summing from $R(0) = 1$ gives
$$R(n) = \binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \binom{n}{3} = \frac{n^3 + 5n + 6}{6},$$
so $R(0), \dots, R(4) = 1, 2, 4, 8, 15$.

22. ★ The proof removes edges that lie on a cycle (each removal joins two faces, so $E$ and $F$ drop by $1$) until a tree is left, where $V - E + F = V - (V - 1) + 1 = 2$. Ending with one tree needs the graph to be connected. For $c$ components the same removals end with a forest of $c$ trees, where $E = V - c$ and $F = 1$, so $V - E + F = 1 + c$.

23. ★ Write $q(t) = At^2 + 2Bt + C$ with $A = \sum a_i^2$, $B = \sum a_i b_i$, $C = \sum b_i^2$. If $A = 0$ every $a_i$ is $0$ and both sides are $0$. Otherwise $q(t) \ge 0$ for all real $t$, so the discriminant $4B^2 - 4AC$ is at most $0$. Equality holds exactly when $q$ has a real root $t$, that is, when $b_i = -t a_i$ for all $i$, or when all $a_i$ are $0$.

24. ★ The distance from $0$ to each centre $(\pm 1, \dots, \pm 1)$ is $\sqrt n$, so $r_n = \sqrt n - 1$; for $n = 2$ this is $\sqrt 2 - 1 \approx 0.41$. The ball lies in the box when $r_n \le 2$, that is $n \le 9$; at $n = 10$ it sticks out.

25. ★ $I + J = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2}$, and $x \mapsto \frac{\pi}{2} - x$ exchanges $\sin$ and $\cos$, so $I = J$. Hence $I = \frac{\pi}{4}$ for every $n$.
