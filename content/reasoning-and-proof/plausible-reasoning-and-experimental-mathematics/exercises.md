1. ◦ Say whether each inference is deductive or only plausible, in the sense of [plausible reasoning](/8DHD3H1CJ9/). (a) $A$ implies $B$; $B$ is false; so $A$ is false. (b) $A$ implies $B$; $B$ is true; so $A$ is more credible. (c) $A$ is analogous to $B$; $B$ is true; so $A$ is more credible. (d) $A$ implies $B$; $A$ is true; so $B$ is true.

2. ◦ The values of $f(n) = n^2 - 79n + 1601$ are prime for $n = 0, 1, \ldots, 79$. Compute $f(80)$ and factor it. Then write $f(n)$ in terms of $m = n - 40$ and say why the run of primes has length $80$.

3. ◦ Two rules both give $1, 2, 4, 8$ for $n = 1, 2, 3, 4$: $a_n = 2^{n-1}$ and $b_n = \sum_{k=0}^{3} \binom{n-1}{k}$. Find the fifth term of each. What does this say about guessing a rule from four terms, as in the [strong law of small numbers](/8AFXPXCE3N/)?

4. ◦ Take the sequence $1, 5, 14, 30, 55$. Form its successive differences until they are constant, and use them to predict the next term. Name a formula that fits all six terms.

5. ◦ List all ways of writing $128$ as a sum of two primes $p \le q$. Compare the count with the size of $128$ and say why a single small count is no evidence against the Goldbach conjecture.

6. ◦ Let $\lambda(n) = (-1)^{\Omega(n)}$, where $\Omega(n)$ counts the prime factors of $n$ with multiplicity, and let $L(n) = \sum_{k \le n} \lambda(k)$. Compute $L(n)$ for $n = 1, \ldots, 10$. Pólya conjectured $L(n) \le 0$ for all $n \ge 2$. Using [numerical evidence for conjectures](/JFD3QWCX8Z/), say what is known about the first $n$ where it fails.

7. ◦ Which of these establish a theorem, and which are evidence? (a) PSLQ finds an integer relation among $50$-digit values of three constants. (b) Goldbach's conjecture is checked for every even number up to $4 \cdot 10^{18}$. (c) A search program outputs a colouring with a stated property, and a short independent program confirms that the colouring has it. (d) Erdős's counting argument shows that some $2$-colouring of the edges of $K_n$ has no monochromatic $K_k$ when $\binom{n}{k} 2^{1 - \binom{k}{2}} < 1$.

8. ◦ A computation gives $x = 0.4142135623$. Guess an exact value for $x$, find a polynomial with integer coefficients that it should satisfy, and say what further computation would test the guess, in the manner of [experimental mathematics](/BPEPTN0TT9/).

9. • Use the model in which an integer near $x$ is prime with probability $1/\ln x$ to estimate the number of primes in the interval $(10^6, 10^6 + 1000]$. The true count is $75$. Is the error what the model would lead you to expect?

10. • Compute the partial sums of $\sum_{n \ge 1} \frac{1}{n(n+1)(n+2)}$ for $n$ up to $5$, guess the value of the series, and prove the guess by a partial fraction decomposition.

11. • Fermat conjectured that every $F_n = 2^{2^n} + 1$ is prime, after checking $n = 0, \ldots, 4$. Show that $641$ divides $F_5$ by using $641 = 5 \cdot 2^7 + 1 = 5^4 + 2^4$, without multiplying out $2^{32}$.

12. • Let $r_n$ be the largest number of regions into which chords between $n$ points in general position on a circle cut the disc. Granting $r_n = \binom{n}{4} + \binom{n}{2} + 1$, prove that $r_n = \sum_{k=0}^{4} \binom{n-1}{k}$, and deduce that $r_n = 2^{n-1}$ exactly when $n \le 5$.

13. • List the primes below $50$ of the form $x^2 + 2y^2$ with integers $x$ and $y$. [Form a conjecture](/R2T42N5XGK/) about which primes have this form in terms of their residue mod $8$, and test it on the primes from $50$ to $100$.

14. • Use the model of exercise 9 to estimate the expected number of primes among the Fermat numbers $F_n$ with $n \ge 5$. Explain why this [heuristic argument](/VCQQNJ3SEZ/) supports the belief that there are only finitely many Fermat primes, and why it is not a proof.

15. • A conic in the plane is the zero set of $ax^2 + bxy + cy^2 + dx + ey + f$ with not all coefficients zero. Count parameters to predict how many conics pass through $5$ given points. Show that the prediction fails when $4$ of the $5$ points lie on a line.

16. • A closed thread lies on a soap film stretched on a wire frame. When the film inside the loop is broken, the thread pulls into a circle, which suggests that among closed curves of given length the circle bounds the largest area. Name the step that this [physical argument](/THJV0NFPDQ/) takes for granted. Then show what goes wrong with the same step in this argument: "Let $N$ be the largest positive integer. Then $N^2 \ge N$, so $N^2 = N$ and $N = 1$."

17. • A computer gives $(1 + \sqrt{2})^{10} \approx 6725.99985$. Explain why the number is so close to an integer, and find the integer, by considering $a_n = (1 + \sqrt{2})^n + (1 - \sqrt{2})^n$.

18. • Count the tilings of a $2 \times n$ board by $1 \times 2$ dominoes for $n = 1, \ldots, 6$, form a conjecture, and prove it by looking at the leftmost column.

19. ★ Observing that $n^2 + n + 41$ is prime for many $n$, one might look for a better polynomial. Prove that no nonconstant polynomial with integer coefficients takes prime values at every integer $n \ge 0$.

20. ★ Show that every prime factor $p$ of $F_n$ satisfies $p \equiv 1 \pmod{2^{n+1}}$. List the primes up to $641$ that this allows as factors of $F_5$. How does this shorten Euler's search?

21. ★ Compute $s_n = \sum_{k=0}^{n} \binom{n}{k}^2$ for $n = 0, \ldots, 5$, identify the sequence, and prove your conjecture by counting the ways to choose $n$ people from $n$ women and $n$ men.

22. ★ In the model of exercise 9, the expected number of ways to write $n$ as $k + (n - k)$ with $k$ and $n - k$ both prime is about $\sum_{k=2}^{n-2} \frac{1}{\ln k \, \ln(n-k)}$. Show that this sum is at least $\frac{n-3}{(\ln n)^2}$, so that the model predicts many Goldbach partitions for large $n$. Show that the model also predicts many partitions for large odd $n$, and that this is false. What correction does this suggest?
