4. Every fraction is $\tfrac{ka}{kb}$ for its reduced form $\tfrac{a}{b}$ and some nonzero integer $k$, so it is enough to compare each rule on $\tfrac{a}{b}$ and $\tfrac{ka}{kb}$. In (a) and (c) the factor $k$ cancels, so these are well defined. Rule (b) fails: $\tfrac12 = \tfrac24$, but $1 \cdot 2 = 2$ and $2 \cdot 4 = 8$. Rule (d) fails on the same pair, giving $1$ and $2$.

5. Two representatives of one class differ by an integer, $x' = x + m$. (a) is well defined, since $x' + y' = (x + y) + (m + n)$. (b) is not: $[0] = [1]$, but $[\tfrac12] \cdot [0] = [0]$ while $[\tfrac12] \cdot [1] = [\tfrac12]$. (c) is well defined because $\cos$ has period $2\pi$. (d) is not, since $\floor{0} = 0$ and $\floor{1} = 1$. (e) is well defined, since $\floor{x + m} = \floor{x} + m$.

7. (a) The number $x = 0$ also satisfies $x^2 = 2x$, so the description "the real number with $x^2 = 2x$" is not legal, and dividing by $x$ loses this solution. (b) Here $\tfrac{f(1) - f(-1)}{2} = 1$, and $3c^2 = 1$ has the two solutions $c = \pm \tfrac{1}{\sqrt 3}$, both in $(-1, 1)$. The theorem gives a point, not the point.

12. In (a) and (c) every value is computed from earlier ones and the starting values are given, so the principle of recursive definition gives exactly one function: $f(n) = n^2$ in (a) and the Fibonacci numbers in (c). Rule (b) runs upwards; rewritten as $f(n + 1) = f(n)/2$ it forces $f(1) = \tfrac32 \notin \Z$, so there is no function. In (d) the value $f(1)$ is free, and $f(1) = c$ gives $f(n) = c F_n$. In (e) the case $n = 0$ says only $f(0) = f(0)$, so $f(0) = c$ is free, and then $f(n) = c + s(n)$, where $s(n)$ is the number of ones in the binary expansion of $n$.

14. The rule is well defined exactly when $a' = a + 6k$ always gives $4a' \equiv 4a \pmod m$, that is, when $m \mid 24k$ for every $k$. So the answer is $m \mid 24$: $m = 1, 2, 3, 4, 6, 8, 12, 24$. For necessity compare the representatives $0$ and $6$ of $[0]_6$, which give $0$ and $24$.

15. The powers $2, 2^2, 2^3, 2^4$ are $2, 4, 3, 1$ modulo $5$, so $2^{a + 4j} \equiv 2^a \pmod 5$ and $2^b \equiv 1 \pmod 5$ only when $4 \mid b$. For the converse compare the representatives $0$ and $n$ of $[0]_n$.

16. (a) The numbers $a$ and $a + 9$ have opposite parity, so every class modulo $9$ has an even representative. Two even representatives differ by a multiple of $18$, so their halves differ by a multiple of $9$. Since $2 \cdot 5 = 10 \equiv 1 \pmod 9$, halving is multiplication by $k = 5$. (b) Every representative $1 + 10j$ of $[1]_{10}$ is odd, so $h([1]_{10})$ has no value. The class $[4]_{10}$ has the even representatives $4$ and $14$, whose halves $2$ and $7$ lie in different classes.

17. The argument starts from equal outputs and ends with equal classes, which proves that the map is injective. A well-defined map needs the other direction. That direction holds: if $a' = a + 3k$, then $3a' = 3a + 9k$, so $[3a']_9 = [3a]_9$. The claim is true, and the map is also injective.

20. If $1 + \sqrt{-5} = \alpha \beta$, then $N(\alpha) N(\beta) = 6$. The equation $a^2 + 5b^2 = 2$ has no integer solutions, and neither has $a^2 + 5b^2 = 3$, so one factor has norm $1$ and is $\pm 1$, a unit. The element itself is not a unit, since its norm is $6$. For "not prime" use $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 6 = 2 \cdot 3$: if $1 + \sqrt{-5}$ divided $2$, then $6$ would divide $N(2) = 4$, and if it divided $3$, then $6$ would divide $N(3) = 9$.

22. In the four-point model a line $\set{P, Q}$ and a point $R$ off it leave exactly one line through $R$ that misses both $P$ and $Q$, namely $\set{R, S}$ with $S$ the fourth point. In the three-point model any two lines meet, so no line through $C$ misses $\set{A, B}$. Every theorem of I1 to I3 holds in every model, so neither Playfair's axiom nor its negation can be proved from I1 to I3.

24. Suppose the rule is well defined and let $h \in H$. Then $hH = H = eH$, so $(hH)(g^{-1}H) = (eH)(g^{-1}H)$, that is, $hg^{-1}H = g^{-1}H$, which says $g h g^{-1} \in H$. Conversely, if $g' = g h_1$ and $k' = k h_2$, then $g'k' = gk \, (k^{-1} h_1 k) \, h_2$, and normality puts $k^{-1} h_1 k$ in $H$.

25. For transitivity add $a + d = b + c$ and $c + f = d + e$ and cancel $c + d$, which is allowed in $\N$. The formula is unchanged when the two pairs are swapped, so it is enough to change the first pair. If $a + b' = b + a'$, then
$$(ac + bd) + (a'd + b'c) = c(a + b') + d(b + a') = c(b + a') + d(a + b') = (ad + bc) + (a'c + b'd),$$
which is the relation between the two products. No subtraction is needed.

26. From any $n \in S$ the steps $+3, +3, -5$ give $n + 1 \in S$, and $+3, +3, +3, -5, -5$ give $n - 1 \in S$. Since $0 \in S$, induction in both directions gives $S = \Z$. With $+4$ and $-6$ the answer is $2\Z$: the even integers contain $0$ and are closed under both steps, so $S \subseteq 2\Z$, and the steps $+4, +4, -6$ and $+4, -6$ give $n + 2$ and $n - 2$, so $2\Z \subseteq S$.

27. (i) implies (ii): if $n = k^2$, the factorization of $n$ is that of $k$ with every exponent doubled, and by uniqueness of factorization it is the only one. (ii) implies (iii): $n = \prod p_i^{e_i}$ has $\prod (e_i + 1)$ positive divisors, a product of odd numbers. (iii) implies (i): pair each divisor $d$ with $n/d$. A divisor is its own partner only when $d^2 = n$, so an odd number of divisors forces $n$ to be a square. The first two steps use the [fundamental theorem of arithmetic](/084HH1NDCB/).

28. Row and column $0$ are fixed, and each row and each column must be a permutation of $0, 1, 2, 3$. If every element is its own inverse, the table is forced and gives the Klein four-group. Otherwise exactly one nonzero element $t$ satisfies $t^2 = 0$, and the other two generate a cyclic group; each choice of $t$ gives one table. That makes four operations: three cyclic and one Klein. With a free identity, each of the four elements can be the identity, giving $16$ operations; equivalently $\tfrac{4!}{2} + \tfrac{4!}{6} = 16$, dividing by the numbers of automorphisms of the two groups.
