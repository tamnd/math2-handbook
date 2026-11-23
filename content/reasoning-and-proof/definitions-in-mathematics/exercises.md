1. ◦ Call an integer $n$ a *perfect square* if $n = k^2$ for some integer $k$. Decide whether each of $0$, $-4$, $49$ and $50$ is a perfect square, and for each "no" say which half of the biconditional you used.

2. ◦ Say that a function $f \colon \R \to \R$ *has period $2$* if $f(x + 2) = f(x)$ for all real $x$. Write the negation of "$f$ has period $2$" as a quantified statement. Then decide, with a reason, which of these have period $2$: the constant function $5$; $\sin(\pi x)$; $\sin x$; $x - \floor{x}$.

3. ◦ Name the kind of each definition (explicit, recursive, inductive, by abstraction, axiomatic, implicit, universal property):
(a) $\abs{x} = x$ if $x \ge 0$ and $\abs{x} = -x$ if $x < 0$;
(b) $F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$;
(c) the set of balanced bracket strings is the smallest set of strings that contains the empty string and contains $(s)$ and $st$ whenever it contains $s$ and $t$;
(d) $e$ is the real number $x$ with $\ln x = 1$;
(e) a ring is a set with two operations satisfying a list of axioms;
(f) $\Z/n\Z$ is the set of classes of integers under congruence modulo $n$;
(g) a product of sets $A$ and $B$ is a set $P$ with maps to $A$ and $B$ through which every pair of maps from a set $Z$ factors in exactly one way.

4. ◦ Which of these rules define a function on $\Q$, where $\tfrac{a}{b}$ is any fraction with $a, b \in \Z$ and $b \neq 0$? Give a counterexample for each one that does not.
(a) $\tfrac{a}{b} \mapsto \tfrac{a + 2b}{b}$;
(b) $\tfrac{a}{b} \mapsto ab$;
(c) $\tfrac{a}{b} \mapsto \tfrac{a^2 + b^2}{ab}$, for $a \neq 0$, as a function on $\Q \setminus \{0\}$;
(d) $\tfrac{a}{b} \mapsto \gcd(a, b)$.

5. ◦ On $\R$ let $x \sim y$ mean $x - y \in \Z$, and write $[x]$ for the class of $x$. Which rules are well defined on $\R/{\sim}$?
(a) $[x] + [y] := [x + y]$;
(b) $[x] \cdot [y] := [xy]$;
(c) $[x] \mapsto \cos(2\pi x)$;
(d) $[x] \mapsto \floor{x}$;
(e) $[x] \mapsto x - \floor{x}$.

6. ◦ Which of these definite descriptions are legal? For each that is not, say whether existence or uniqueness fails.
(a) the integer $n$ with $2n = 7$;
(b) the real number $x$ with $x^3 = x$;
(c) the smallest positive integer $n$ with $n \equiv 3 \pmod 4$ and $n \equiv 2 \pmod 5$;
(d) the largest real number less than $1$;
(e) the positive real number $x$ with $x^2 = 3x$.

7. ◦ Find the error in each argument.
(a) "Let $x$ be the real number with $x^2 = 2x$. Dividing by $x$ gives $x = 2$."
(b) "By the [mean value theorem](/0BARQY52N5/) applied to $f(x) = x^3$ on $[-1, 1]$, let $c$ be the point with $f'(c) = \tfrac{f(1) - f(-1)}{2}$. Then $3c^2 = 1$, so $c = \tfrac{1}{\sqrt 3}$."

8. ◦ Find all integer solutions $(x, y)$ of $x^2 + y^2 = 13$, and then of $x^2 + y^2 = 25$. How many solutions are there in each case, and how many are there up to order and sign?

9. ◦ Let $C_6$ denote "the cyclic group of order $6$", a phrase that makes sense only up to isomorphism. For each statement, say whether it is meaningful up to isomorphism, and if so whether it is true.
(a) $C_6$ is abelian.
(b) $C_6$ contains the number $4$.
(c) $C_6$ has exactly one element of order $2$.
(d) The identity of $C_6$ is $0$.
(e) $C_6$ has exactly two generators.

10. ◦ Suppose $1$ were counted as a prime. Which of these statements would remain true, and which would need the extra words "other than $1$"?
(a) Every integer $n > 1$ is a product of primes.
(b) Every integer $n > 1$ is a product of primes in only one way, up to order.
(c) There are infinitely many primes.
(d) If a prime $p$ divides $ab$, then $p \mid a$ or $p \mid b$.
(e) Every prime has exactly two positive divisors.

11. • Using only the [definition](/8ZCZ3HW91Z/) of divisibility ($a \mid b$ when $b = ak$ for some $k \in \Z$), prove that if $a \mid b$ and $b \mid a$ for integers $a$ and $b$, then $a = b$ or $a = -b$. Treat the case $a = 0$ separately.

12. • For each recursion, say whether it defines no function, exactly one function, or many functions $f \colon \N \to \Z$, and describe the solutions.
(a) $f(0) = 0$ and $f(n + 1) = f(n) + 2n + 1$ for $n \ge 0$;
(b) $f(0) = 3$ and $f(n) = 2 f(n + 1)$ for $n \ge 0$;
(c) $f(0) = 0$, $f(1) = 1$ and $f(n + 2) = f(n + 1) + f(n)$ for $n \ge 0$;
(d) $f(0) = 0$ and $f(n + 2) = f(n + 1) + f(n)$ for $n \ge 0$;
(e) $f(2n) = f(n)$ and $f(2n + 1) = f(n) + 1$ for $n \ge 0$.

13. • Prove that $[a]_8 \mapsto [a^2]_{16}$ is a well-defined map from $\Z/8\Z$ to $\Z/16\Z$, and show that $[a]_8 \mapsto [a^3]_{16}$ is not.

14. • For which positive integers $m$ is $[a]_6 \mapsto [4a]_m$ a well-defined map from $\Z/6\Z$ to $\Z/m\Z$? List them all and prove your answer.

15. • Let $n \ge 1$. Define $E([a]_n) := [2^a]_5$, where $a$ is a representative with $a \ge 0$. Prove that $E$ is well defined if and only if $4 \mid n$.

16. • Define "half" of a class as follows: choose an even representative $a$ of the class and set $h([a]) := [a/2]$.
(a) Show that on $\Z/9\Z$ this defines a function on all of $\Z/9\Z$, and find $k$ with $h([a]_9) = [ka]_9$ for all $a$.
(b) Show that on $\Z/10\Z$ it fails, in two different ways.

17. • Find the error. "Claim: $[a]_3 \mapsto [3a]_9$ is well defined. Proof: suppose $[3a]_9 = [3a']_9$. Then $9 \mid 3(a - a')$, so $3 \mid a - a'$, so $[a]_3 = [a']_3$." Then decide whether the claim is true, and give a correct proof or a counterexample.

18. • Prove that for an integer $n \ge 2$ the following are [equivalent](/NZ42PS2P1A/): (i) no integer $d$ with $1 < d < n$ divides $n$; (ii) no integer $d$ with $1 < d \le \sqrt n$ divides $n$. Use (ii) to decide whether $211$ and $221$ are prime.

19. • Prove that an integer $n$ is odd if and only if $n^2 \equiv 1 \pmod 8$. Then show that "$n^2 \equiv 1 \pmod{16}$" is not an equivalent definition of "odd".

20. • In $\Z[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \Z\}$ use the norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$, which is multiplicative. Show that $1 + \sqrt{-5}$ is irreducible but not prime.

21. • For nonzero integers $a$ and $b$, define $\operatorname{lcm}(a, b)$ as the integer $m \ge 0$ such that $a \mid m$, $b \mid m$, and $m \mid c$ for every common multiple $c$ of $a$ and $b$. Prove that exactly one such $m$ exists, so that the [definite description](/5P955TVSS2/) is legal, and check the definition on $a = 12$, $b = 18$.

22. • Consider the incidence axioms: (I1) any two distinct points lie on exactly one line; (I2) every line contains at least two points; (I3) there are three points not on one line. Take four points $A, B, C, D$ and let the lines be the six two-element subsets. Show that this model satisfies I1, I2, I3 and [Playfair's axiom](/PR7Q3QMEHZ/) (for every line $\ell$ and point $P$ not on $\ell$, exactly one line through $P$ shares no point with $\ell$). Then show that the model with three points and three two-point lines fails Playfair's axiom. What do the two models prove about Playfair's axiom and I1 to I3?

23. • Two solid cubes are glued together at a single vertex. Count the vertices $V$, edges $E$ and faces $F$ of the resulting solid and compute $V - E + F$. Then describe what goes wrong at the shared vertex, in a form that could become a clause in a definition of "polyhedron" excluding this solid.

24. ★ Let $H$ be a subgroup of a group $G$. Prove that the rule $(gH)(kH) := gkH$ is well defined on the set of left cosets of $H$ if and only if $H$ is a [normal subgroup](/0CB0DX5BVV/), that is, $g h g^{-1} \in H$ for all $g \in G$ and $h \in H$.

25. ★ On $\N \times \N$ let $(a, b) \sim (c, d)$ mean $a + d = b + c$. Prove that $\sim$ is an equivalence relation, and that
$$[(a, b)] \cdot [(c, d)] := [(ac + bd,\ ad + bc)]$$
is well defined on the classes. (Think of $(a, b)$ as $a - b$.)

26. ★ Let $S$ be the smallest subset of $\Z$ that contains $0$ and contains $n + 3$ and $n - 5$ whenever it contains $n$. Prove that $S = \Z$. Then find the smallest subset with the same definition but with $n + 4$ and $n - 6$ in place of $n + 3$ and $n - 5$, and prove your answer.

27. ★ Prove that for a positive integer $n$ the following three conditions are equivalent: (i) $n$ is a perfect square; (ii) every exponent in the prime factorization of $n$ is even; (iii) $n$ has an odd number of positive divisors. Prove a cycle of implications, and say which result each step uses.

28. ★ Count the group operations on the set $\{0, 1, 2, 3\}$ that have $0$ as identity element, and sort them up to isomorphism. Then count all group operations on a fixed four-element set, with any element allowed as the identity.
