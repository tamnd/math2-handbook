1. ◦ Let $f_n(x) = x^{1/n}$ on $[0, 1]$, with $f_n(0) = 0$. Find the pointwise limit $f$ of $f_n$. Is $f$
continuous? Can the convergence be uniform?

2. ◦ Work in the plane $\Q^2$ of points with rational coordinates. The line $y = x$ passes through the point
$(0, 0)$ inside the circle $x^2 + y^2 = 1$ and through the point $(1, 1)$ outside it. Show that the line and the
circle have no common point in $\Q^2$.

3. ◦ Let $f(x) = x^3 - 2$ on the set $\set{x \in \Q : 1 \le x \le 2}$. Compute $f(1)$ and $f(2)$, and show that
$f$ has no zero in this set. Which hypothesis of the [intermediate value theorem](/00KAFBR32E/) fails?

4. ◦ Let $a_n$ be the decimal expansion of $\sqrt 2$ cut off after $n$ digits, so $a_0 = 1$, $a_1 = 1.4$,
$a_2 = 1.41$, and so on. Show that $(a_n)$ is a bounded sequence of rational numbers with no subsequence that
converges to a rational number.

5. ◦ Divide a segment of length $1$ into $n$ equal parts and draw a semicircle on each part, all on the same side.
Compute the total length of the $n$ semicircles. The curves approach the segment as $n \to \infty$; explain why
this does not prove $\pi/2 = 1$.

6. ◦ (a) Give a certificate that $1001$ is composite that anyone can check in a minute. (b) What would a reader
need to check the claim "no integer $x$ satisfies $x^2 \equiv 3 \pmod 7$"? Give the check.

7. ◦ Put in order of date: Gonthier and Werner's formal proof of the four colour theorem in Coq; Kempe's proof;
the published proof of Robertson, Sanders, Seymour and Thomas; Heawood's discovery of the error in Kempe's proof;
Appel and Haken's announcement.

8. ◦ A student writes the derivation: 1. $P \to Q$ (hypothesis); 2. $Q$ (hypothesis); 3. $P$ (modus ponens from
1 and 2). Which rule is misapplied in line 3? Give truth values of $P$ and $Q$ that make the hypotheses true and
the conclusion false.

9. ◦ Find the gap in the argument: "Every continuous function $f : (0, 1) \to \R$ is bounded, because a continuous
function on a bounded interval is bounded." Give a counterexample and state the hypothesis that the correct
theorem needs.

10. • Using only the definition "$a \mid b$ means $b = ak$ for some integer $k$", write a proof, one justified step
per line, that $a \mid b$ and $a \mid c$ imply $a \mid (b + c)$ for all integers $a, b, c$. Name the fact about
the integers used in each step.

11. • Give a [natural deduction](/6KT3BJZ7D1/) proof, with numbered lines and the rules $\to$I and $\to$E, of
$$
(P \to (Q \to R)) \to (Q \to (P \to R)).
$$

12. • Let $f_n(x) = x^n (1 - x)$ on $[0, 1]$. Find the maximum of $f_n$, and show that $f_n \to 0$
[uniformly](/08VZ57PT26/) on $[0, 1]$, although $x^n$ does not converge uniformly there.

13. • Describe a picture, built from a unit square divided into four equal squares again and again, that shows
$\frac14 + \frac1{16} + \frac1{64} + \cdots = \frac13$. Then write a proof in words with the partial sums, and name
the step that the picture leaves to the reader.

14. • Let $T_n = n(n+1)/2$. Check $8T_n + 1 = (2n + 1)^2$ for $n = 1, 2, 3, 4$, prove it by algebra, and describe
a picture that cuts a $(2n+1) \times (2n+1)$ square into eight copies of a staircase of $T_n$ unit squares and one
more unit square.

15. • Call a set of positive integers sum-free if it contains no $x, y, z$ (with $x = y$ allowed) such that
$x + y = z$. Show that $\set{1, 2, 3, 4}$ is the union of two disjoint sum-free sets in exactly one way, and that
$\set{1, 2, 3, 4, 5}$ is not the union of two disjoint sum-free sets. How many colourings would a program check
for the second claim, if it tried all of them?

16. • Show that the formula $(x \lor y) \land (\lnot x \lor y) \land (x \lor \lnot y) \land (\lnot x \lor \lnot y)$
is unsatisfiable by resolution: derive the empty clause in three steps. Explain why such a derivation is a
certificate in the sense of [computer-assisted proof](/MC18C7BMFT/).

17. • Prove $k \binom{n}{k} = n \binom{n-1}{k-1}$ for $1 \le k \le n$ twice: once from the factorial formula, and
once by counting committees of $k$ people with a chair in two ways. Say what each proof shows that the other does
not.

18. • Show that every prime factor of $n! + 1$ is greater than $n$, and deduce that there are infinitely many
primes. Is $n! + 1$ itself always prime? Settle the case $n = 5$.

19. • Let $S = \set{u \in \Q : u > 0,\ u^2 < 3}$. For $u > 0$ put $v = (2u + 3)/(u + 2)$. Prove that
$v^2 - 3 = (u^2 - 3)/(u + 2)^2$ and $v - u = (3 - u^2)/(u + 2)$, and deduce that $S$ has no largest element and
no least upper bound in $\Q$.

20. ★ A [Hilbert system](/1MGMQX43B8/) has the axiom schemes $A \to (B \to A)$ and
$(A \to (B \to C)) \to ((A \to B) \to (A \to C))$, and modus ponens as its only rule. Give a derivation of
$p \to p$ in five lines, naming the axiom instance or rule used in each line.

21. ★ Let $p_1 = 2 < p_2 = 3 < p_3 < \cdots$ be the primes in order. Prove $p_n \le 2^{2^{n-1}}$ for every
$n \ge 1$, using Euclid's argument for the step from $n$ to $n + 1$.

22. ★ Find the sum of the series $\sum_{n=0}^{\infty} \frac{x^2}{(1 + x^2)^n}$ for every real $x$. Each term is
continuous: is the sum? Deduce that the convergence is not uniform on $[-1, 1]$, and say which claim of Cauchy's
of 1821 the series contradicts.

23. ★ Give a proof that $\sqrt 2$ is irrational that does not use even and odd numbers: assume $\sqrt 2 = a/b$ with
positive integers $a, b$ and $b$ as small as possible, and find a fraction equal to $\sqrt 2$ with a smaller
positive denominator.

24. ★ Split $\set{1, 2, \ldots, 13}$ into three disjoint sets, none of which contains $x, y, z$ with $x + y = z$
($x = y$ allowed), and check your answer.
