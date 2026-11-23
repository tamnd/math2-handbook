1. ◦ A proof by [strong induction](/0KMVFSHFGZ/) shows that every integer $n \ge 18$ can be written as $4a + 7b$ with natural numbers $a$ and $b$, using the step from $n - 4$ to $n$. Which base cases does the proof need? Check them, and show that $17$ has no such form, so that the start $18$ cannot be lowered.

2. ◦ Compute $1 \cdot 1! + 2 \cdot 2! + \cdots + n \cdot n!$ for $n = 1, 2, 3, 4, 5$. Guess a closed formula and prove it by [induction](/0ASJVEFA9J/).

3. ◦ Give the least element of each set, or explain why there is none.
(a) $\set{n \in \N : n^2 \ge 200}$;
(b) $\set{n \in \N : n \ge 1 \text{ and } 7 \mid 3^n - 1}$;
(c) $\set{n \in \Z : n^2 < 50}$;
(d) $\set{x \in \Q : x > 0 \text{ and } x^2 > 2}$.
The integers are not well-ordered. Why does the set in (c) still have a least element?

4. ◦ Compute $n!$ and $3^n$ for $n = 0, 1, \ldots, 8$. Find the least $n_0$ such that $n! > 3^n$ for every $n \ge n_0$, and prove the inequality from that base. For which $n$ is the step $(n + 1)! = (n + 1) \cdot n! > 3 \cdot 3^n$ valid?

5. ◦ Find the error. "Let $F_0 = 0$, $F_1 = 1$ and $F_n = F_{n-1} + F_{n-2}$ for $n \ge 2$. Claim: every $F_n$ is even. Base case: $F_0 = 0$ is even. Step: let $n \ge 1$ and assume that $F_k$ is even for every $k < n$. Then $F_n = F_{n-1} + F_{n-2}$ is a sum of two even numbers, so it is even." For which $n$ does the step fail, and what rule for base cases does the proof break?

6. ◦ Find the error. "Claim: $n^2 \le 2^n$ for every $n \ge 1$. Base case: $1 \le 2$. Step: assume $n^2 \le 2^n$. Then $(n + 1)^2 = n^2 + 2n + 1 \le 2^n + 2n + 1 \le 2^n + 2^n = 2^{n+1}$." Find the least $n$ for which the claim is false and the values of $n$ for which the step is invalid. From which base does the same argument give a correct proof?

7. ◦ Let $S$ be the smallest set of positive integers that contains $1$ and contains $2n$ and $n + 3$ whenever it contains $n$. Describe $S$, and prove your description in both directions. Is $2026$ in $S$? Is $2025$?

8. ◦ Define $g(m, 0) = g(0, n) = 1$ for all $m, n \in \N$, and $g(m, n) = g(m - 1, n) + g(m, n - 1) + g(m - 1, n - 1)$ for $m, n \ge 1$. Compute $g(2, 2)$ and $g(3, 2)$. Prove by [double induction](/AABX4YPKRR/) on $m + n$ that every $g(m, n)$ is odd. Which pairs are base cases?

9. ◦ For which positive integers $n$ do these conditions prove $P(n)$?
(a) $P(1)$ holds; $P(n)$ implies $P(n^2)$ for every $n \ge 1$; $P(n)$ implies $P(n - 1)$ for every $n \ge 2$.
(b) The same, with $P(2)$ in place of $P(1)$.

10. • Let $f_n = 2^{2^n} + 1$ for $n \in \N$. Prove that $f_0 f_1 \cdots f_{n-1} = f_n - 2$ for every $n \ge 1$. Deduce that any two different numbers $f_m$ and $f_n$ are coprime.

11. • Let $u_1 = 1$, $u_2 = 2$ and $u_{k+1} = u_k + u_{k-1}$ for $k \ge 2$. Prove by strong induction that every positive integer is a sum of distinct terms $u_k$, no two with consecutive indices. Write $100$ and $2026$ in this form.

12. • Let $p_n = \prod_{k=1}^{n} \left(1 + \frac{1}{k^3}\right)$. Show that a direct induction on the claim $p_n < 3$ gets stuck. Then prove the stronger claim $p_n \le 3 - \frac{1}{n}$ for every $n \ge 1$, and say why it implies $p_n < 3$.

13. • A graph here is finite, with no loops and no repeated edges. Prove that a graph with $n \ge 1$ vertices and at least $n$ edges contains a cycle. Use a [minimal counterexample](/JGRCNPKNGG/) with the fewest vertices, and use the fact that a graph in which every vertex has degree at least $2$ contains a cycle.

14. • Addition on $\N$ is defined by $m + 0 = m$ and $m + S(n) = S(m + n)$, where $S$ is the successor. Prove that $m + n = n + m$ for all $m, n \in \N$. First prove $0 + n = n$ and $S(m) + n = S(m + n)$, each by induction on $n$.

15. • For positive reals $x_1, \ldots, x_n$ let $G$ be the geometric mean $(x_1 \cdots x_n)^{1/n}$ and $H$ the harmonic mean $n / (1/x_1 + \cdots + 1/x_n)$. Prove $H \le G$ by [forward-backward induction](/QC9FKGZH1V/): prove the case $n = 2$, the step from $n$ to $2n$, and the step from $n$ to $n - 1$. Do not quote the AM-GM inequality.

16. • Lists are built from the empty list $[\,]$ by putting an element in front, $a : xs$. Joining is defined by $[\,] \mathbin{+\!\!+} ys = ys$ and $(a : xs) \mathbin{+\!\!+} ys = a : (xs \mathbin{+\!\!+} ys)$, and reversal by $\operatorname{rev}[\,] = [\,]$ and $\operatorname{rev}(a : xs) = \operatorname{rev}(xs) \mathbin{+\!\!+} [a]$. Prove by [structural induction](/12MQ2NJ29A/) that $\operatorname{rev}(\operatorname{rev}(xs)) = xs$ for every list. A direct attempt gets stuck; first prove $\operatorname{rev}(xs \mathbin{+\!\!+} [a]) = a : \operatorname{rev}(xs)$.

17. • Let $S$ be the smallest subset of $\Z^2$ that contains $(0, 0)$ and contains $(a + 2, b)$ and $(a + 1, b + 1)$ whenever it contains $(a, b)$. Prove that $S = \set{(a, b) \in \Z^2 : b \ge 0,\ a \ge b,\ a - b \text{ even}}$.

18. • Any finite number of straight lines cuts the plane into regions. Prove by [induction on size](/B2D8PTFNN1/), on the number of lines, that the regions can be coloured black and white so that any two regions with a common boundary segment get different colours. The lines may be parallel and may meet three at a point.

19. • Use the conditions (B1) to (B4) and the principles (I), (SI) and (WO) as stated in the entry on the [equivalence of induction and well-ordering](/J2P9FWBP3Q/). Let $N = \N \cup \set{\infty}$, with the usual order on $\N$ and $n < \infty$ for every $n \in \N$, and let $S(n) = n + 1$ and $S(\infty) = \infty$. Which of (B1) to (B4) hold? Which of (I), (SI) and (WO) hold? Which condition does this example show to be needed?

20. • Two players take turns removing $1$, $3$ or $4$ coins from a pile, and the player who takes the last coin wins. Prove by strong induction that the player about to move loses, against best play, exactly when the number of coins leaves remainder $0$ or $2$ on division by $7$. Who wins with $2026$ coins, and with what first move?

21. • Let $n$ be a positive integer that is not a perfect square, and let $m = \floor{\sqrt n}$. Suppose that $\sqrt n$ is rational. Use the [well-ordering principle](/01BX15HSRR/) on the set of positive integers $k$ with $k \sqrt n \in \Z$, and the number $k(\sqrt n - m)$, to reach a contradiction.

22. ★ Let $f$ be a function from the positive integers to the positive integers with $f(n + 1) > f(f(n))$ for every $n \ge 1$. Prove that $f(n) = n$ for every $n$.

23. ★ Prove that every positive integer is a sum of numbers of the form $2^a 3^b$ with $a, b \in \N$, no one of which divides another. Find such a sum for $100$.

24. ★ Formulas are built from the variables $p$ and $q$ by the rules: if $A$ and $B$ are formulas, so are $\neg A$ and $(A \leftrightarrow B)$. Prove that every such formula is true in an even number of the four rows of its truth table. Deduce that no such formula is equivalent to $p \land q$.

25. ★ Prove that for every $n \ge 1$ there is an $n$-digit number, with every digit $1$ or $2$, that is divisible by $2^n$. Give such numbers for $n = 1, 2, 3, 4$.

26. ★ Let $a$ and $b$ be positive integers such that $ab + 1$ divides $a^2 + b^2$. Prove that $k = (a^2 + b^2)/(ab + 1)$ is a perfect square. Use [infinite descent](/0EFYCFHYFG/): for a fixed $k$ that is not a square, take a solution with $a + b$ least and $a \ge b$, and replace $a$ by the other root of $x^2 - kbx + b^2 - k = 0$.
