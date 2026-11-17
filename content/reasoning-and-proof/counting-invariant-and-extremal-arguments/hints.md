1. The boxes are the ten pairs $\set{1, 20}, \set{2, 19}, \ldots, \set{10, 11}$. Eleven numbers in ten boxes put two numbers in one pair. For ten numbers the claim fails: take $1, 2, \ldots, 10$.

3. The values are the boxes and the places $m$ are the objects; by the [infinite pigeonhole principle](/0FS3RHF6KE/) some value is taken at infinitely many places, and these places give the subsequence. The sequence $x_m = m$ has no constant infinite subsequence.

5. No. Since $\abs{a - b} \equiv a + b \pmod 2$, the parity of the sum of the numbers on the board does not change. It starts at $55$, which is odd, so the last number is odd.

7. Colour the board like a chessboard with black corners: $5$ black cells (the corners and the centre) and $4$ white ones. Each domino covers one cell of each colour. Removing a white cell, an edge cell, leaves $5$ black and $3$ white, so no tiling exists. Removing the centre or a corner leaves $4$ and $4$, and a tiling exists in both cases.

10. Cut the triangle into nine equilateral triangles of side $1/3$ by lines parallel to the sides. Two of the ten points lie in the same small triangle.

16. The product $\prod (x + 1)$ over the numbers on the board does not change, since $ab + a + b + 1 = (a + 1)(b + 1)$. So the last number $c$ satisfies $c + 1 = 2 \cdot 3 \cdots 11 = 11!$, and $c = 11! - 1 = 39916799$.

17. Start with any split, and as long as some member has at least two enemies in his or her own house, move that member to the other house, where he or she has at most one. Each move lowers the number of pairs of enemies in the same house by at least one, so the moves stop.

19. A tiling would use $25$ pieces. In the chessboard colouring each piece covers $3$ cells of one colour and $1$ of the other. If $a$ pieces cover $3$ black cells, the black cells number $3a + (25 - a) = 50$, so $2a = 25$, which is impossible.

21. Take the point $P$ of $S$ that is largest in lexicographic order. If $P$ were the midpoint of two other points $A$ and $B$, one of them would be larger than $P$ in that order.

23. An eventually periodic expansion is fixed by a finite block before the period and a finite repeating block, so there are countably many. Each real number has at most two decimal expansions, and $[0, 1)$ is uncountable.

24. Write each chosen number as $2^k m$ with $m$ odd. There are only $n$ odd numbers below $2n$, so two chosen numbers have the same $m$, and the smaller divides the larger. The numbers $n + 1, \ldots, 2n$ show that $n$ are not enough.

25. The application gives, for each $N$, a $q \le N$ with $\abs{q\alpha - p} < 1/N \le 1/q$, so $\abs{\alpha - p/q} < 1/q^2$. Given finitely many such fractions, choose $N$ with $1/N$ smaller than each $\abs{q\alpha - p}$, which is positive because $\alpha$ is irrational; then the new fraction is not among them.

26. Given a list $f_1, f_2, \ldots$, the function $g(n) = f_n(n) + 1$ differs from each $f_n$ at $n$. A function that is $0$ from some place on is a finite sequence of natural numbers, and the finite sequences form a countable union of countable sets.

27. Take $n = \floor{2^{k/2}}$. Then $\binom{n}{k} 2^{1 - \binom{k}{2}} < \frac{n^k}{k!} 2^{1 - k(k-1)/2} \le \frac{2^{1 + k/2}}{k!}$, using $n^k \le 2^{k^2/2}$. This is less than $1$ for $k = 3$, since $2^{5/2} < 6$, and the ratio decreases as $k$ grows. So $R(k, k) > n$, and since $R(k, k)$ is an integer, $R(k, k) > 2^{k/2}$.

28. Number rows and columns from $0$ to $7$ so that the removed corner is $(0, 0)$, and give the cell $(i, j)$ the colour $(i + j) \bmod 3$. Each bar covers one cell of each colour. The full board has $21$, $22$ and $21$ cells of colours $0$, $1$ and $2$, so the mutilated board has $20$, $22$ and $21$, but $21$ bars would need $21$ of each.
