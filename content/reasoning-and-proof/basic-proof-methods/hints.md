2. Converse: for every integer $n$, if $n$ is odd, then $n$ is prime and $n > 2$; false, since $9$ is odd and not prime. Contrapositive: for every integer $n$, if $n$ is even, then $n$ is not prime or $n \le 2$; true, like the statement. Negation: there is an integer $n$ that is prime, greater than $2$ and even; false.

4. (a) $n = 4$: the values for $n = 1, 2, 3$ are the primes $3, 7, 13$, and $4^2 + 4 + 1 = 21 = 3 \cdot 7$. (b) $1024 = 3 \cdot 341 + 1$, so $2^{10} \equiv 1 \pmod{341}$, hence $2^{340} = (2^{10})^{34} \equiv 1$ and $2^{341} \equiv 2$. So $341 \mid 2^{341} - 2$, and $341 = 11 \cdot 31$ is not prime.

6. (a) Yes, it is a cycle. (b) No: nothing leads from $\set{1, 2}$ to $\set{3, 4}$. (c) Yes: $1, 2, 3$ form a cycle, and $4$ is reached from $1$ and leads to $2$. (d) No: no implication leaves $2$ or $3$.

8. (a) Yes: both sides are unchanged by every permutation of $a, b, c$, so any order can be put first. (b) No: the expression is unchanged by the cyclic shift $a \to b \to c \to a$, but not by exchanging two letters; $(1, 2, 3)$ gives $23$ and $(2, 1, 3)$ gives $25$. A cyclic shift lets you assume that $a$ is the largest, not that $a \le b \le c$.

10. No: $1 + \dots + 10 = 55$ is odd, and two equal sums would add to an even number. Yes: the total is $78$, and $\set{6, 10, 11, 12}$ and its complement both sum to $39$.

14. If $\sqrt 6 = a/b$ in lowest terms, then $a^2 = 6b^2$, so $a = 2c$, then $2c^2 = 3b^2$, so $b$ is even too. If $\sqrt 2 + \sqrt 3 = r$ were rational, then $r^2 = 5 + 2\sqrt 6$ would make $\sqrt 6 = (r^2 - 5)/2$ rational. Both goals are negative statements, so both proofs are refutations and need no excluded middle.

15. Split at $x = \tfrac32$, where $2x - 3$ changes sign. For $x \ge \tfrac32$ the inequality reads $2x - 3 \le x$, that is, $x \le 3$. For $x < \tfrac32$ it reads $3 - 2x \le x$, that is, $x \ge 1$. Together the solutions are $1 \le x \le 3$.

18. With $f(x) = x^3 - 4x + 1$: $f(-3) = -14$, $f(-2) = 1$, $f(0) = 1$, $f(1) = -2$, $f(2) = 1$. The intermediate value theorem gives roots in $(-3, -2)$, $(0, 1)$ and $(1, 2)$, and a polynomial of degree $3$ has at most three roots. The proof is non-constructive: it names no root.

20. If $g(a) = g(a')$, then $f(g(a)) = f(g(a'))$, so $a = a'$ because $f \circ g$ is injective. For the counterexample, take $A = C = \set{0}$, $B = \set{0, 1}$, $g(0) = 0$ and $f$ constant.

22. Cubes leave remainder $0$, $1$ or $8$ on division by $9$, as the cases $x \equiv 0, 1, \dots, 8 \pmod 9$ show. Sums of two of them leave $0, 1, 2, 7$ or $8$, never $4$.

23. Among the $n + 1$ numbers $1, 11, \dots$ with $1$ to $n + 1$ ones, two leave the same remainder on division by $n$. Their difference is a number of ones followed by $j$ zeros, that is, a number made of ones times $10^j$. It is divisible by $n$, and since $\gcd(n, 10) = 1$, $n$ divides the number made of ones. The argument does not say which number works. For $n = 7$ the answer is six ones ($111111 = 7 \cdot 15873$), and for $n = 17$ it is sixteen ones.

24. For existence, let $2^k$ be the largest power of $2$ dividing $n$; then $m = n/2^k$ is odd. For uniqueness, suppose $2^k m = 2^j m'$ with $m$, $m'$ odd and $k < j$. Then $m = 2^{j - k} m'$ is even, a contradiction, so $k = j$ and then $m = m'$.

25. Squares are $0$, $1$ or $4$ modulo $8$, so a sum of three squares is never $7$ modulo $8$; this settles $a = 0$. If $x^2 + y^2 + z^2 \equiv 0 \pmod 4$, the remainders $0, 1$ of squares modulo $4$ force $x$, $y$, $z$ to be even, and dividing by $4$ gives a representation of $4^{a-1}(8b + 7)$. Repeat until $a = 0$.

26. Pair each divisor $d$ of $n$ with $n/d$. The pairs have two different elements except when $d = n/d$, that is, $d^2 = n$. So the number of divisors is even unless $n$ is a square, in which case exactly one divisor is unpaired.

27. Suppose $p_1, \dots, p_k$ were all such primes, and let $N = 6p_1 \cdots p_k - 1$. Then $N \equiv 5 \pmod 6$, so $N$ is odd and not divisible by $3$, and every prime factor of $N$ is $1$ or $5$ modulo $6$. A product of numbers that are $1$ modulo $6$ is $1$ modulo $6$, so some prime factor is $5$ modulo $6$, and it is none of the $p_i$, since they divide $N + 1$.
