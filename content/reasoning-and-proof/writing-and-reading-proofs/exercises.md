1. ◦ For each statement, write the first sentence of a proof and say what the last sentence must establish. Do not write the rest of the proof. (a) For every integer $n$, the number $n^2 + n$ is even. (b) There is an integer $n$ with $n^2 = 2n + 8$. (c) If a function $f \colon A \to B$ has a left inverse, then $f$ is injective. (d) Not every continuous function $\R \to \R$ is differentiable.

2. ◦ Unpack each statement into a sentence with explicit quantifiers that uses only the definitions of its terms. (a) The sequence $(a_n)$ is bounded. (b) The function $f \colon \R \to \R$ is not continuous at $0$. (c) $A \not\subseteq B$. (d) The relation $R$ on a set $X$ is not transitive.

3. ◦ Read this proof. "Let $n$ be an integer and suppose that $3$ divides $n - 1$. Then $n - 1 = 3k$ for some integer $k$, so $n = 3k + 1$. Hence $n^2 + 2 = 9k^2 + 6k + 3 = 3(3k^2 + 2k + 1)$, and so $3$ divides $n^2 + 2$." (a) What does "let" introduce, and what does "suppose" add? Is $k$ arbitrary? (b) State in one sentence the theorem that the proof proves. (c) Follow the proof with $n = 4$ and with $n = 7$, giving $k$ and $3k^2 + 2k + 1$ in each case.

4. ◦ Give the reasons in this two-column proof that if $2(x - 3) = x + 1$, then $x = 7$. Row 1: $2(x - 3) = x + 1$. Row 2: $2x - 6 = x + 1$. Row 3: $x - 6 = 1$. Row 4: $x = 7$. Does the table also prove that $x = 7$ satisfies $2(x - 3) = x + 1$? Is that statement true?

5. ◦ Find the step that is wrong in this structured proof that $\abs{x} \ge x$ for every real $x$, explain why, and repair it. Step $\langle 1 \rangle 1$. CASE: $x \ge 0$. PROOF: $\abs{x} = x$ by the definition of $\abs{x}$, so $\abs{x} \ge x$. Step $\langle 1 \rangle 2$. CASE: $x < 0$. PROOF: $\abs{x} = x$ by $\langle 1 \rangle 1$, so $\abs{x} \ge x$. Step $\langle 1 \rangle 3$. Q.E.D. PROOF: by $\langle 1 \rangle 1$ and $\langle 1 \rangle 2$, since every real $x$ satisfies $x \ge 0$ or $x < 0$.

6. ◦ For a first-year reader, decide whether each omitted step is acceptable or is a gap. If it is a gap, say whether the omitted step is even true. (a) "Expanding, $(n + 1)^3 = n^3 + 3n^2 + 3n + 1$." (b) "Since $f$ is continuous on $[0, 1]$, it attains a maximum value on $[0, 1]$." (c) After a proof that $x^3 > x$ for every $x > 1$: "Similarly, $x^3 < x$ for every $x < 0$." (d) "A routine check shows that the set of $2 \times 2$ real matrices with determinant $1$ is closed under addition."

7. ◦ Rewrite each line as one or two correct sentences, and say what was wrong with it. (a) "$x^2 = 2x \Rightarrow x = 2$." (b) "$f(x) = x^3$. $f$ injective." (c) "$n = 2k + 1 = n^2 = 4k^2 + 4k + 1$."

8. ◦ Read this proof actively. "Let $n$ be an integer not divisible by $5$. Then $n \equiv \pm 1$ or $n \equiv \pm 2 \pmod 5$, so $n^2 \equiv 1$ or $n^2 \equiv 4 \pmod 5$. In both cases $n^4 = (n^2)^2 \equiv 1 \pmod 5$." Write the reason for each of the three sentences after the first, run the proof with $n = 7$, and say where the hypothesis is used. What happens for $n = 10$?

9. ◦ Check this proof. "Claim: for all real $x$ and $y$, if $x < y$, then $x^2 < y^2$. Proof: multiplying $x < y$ by $x$ gives $x^2 < xy$, and multiplying it by $y$ gives $xy < y^2$. Hence $x^2 < y^2$." Name the step without a valid reason, give a counterexample to the claim, and add a hypothesis on $x$ under which the claim and the proof become correct.

10. ◦ A paper proves that a positive integer $n$ is a sum of two squares of integers if and only if every prime $p \equiv 3 \pmod 4$ divides $n$ to an even power. Its abstract reads "We prove Theorem 1.2 by the method of Section 3", and its introduction says "Our main result concerns sums of two squares and is proved in Section 3". Say what is wrong with each, and write an abstract of one or two sentences that makes sense on its own.

11. • Write a complete proof, for a reader who knows only the definitions of even and odd integers, that $n^2 + n + 1$ is odd for every integer $n$.

12. • Find all real $x$ with $\sqrt{x + 5} = x - 1$, first in scratch work. Then write a final proof that the set of solutions is $\set{4}$, with one paragraph for each inclusion.

13. • Prove from the definition that $\dfrac{n}{n^2 + 1} \to 0$. Show the scratch work that finds $N$ in terms of $\varepsilon$, and then write the proof forward.

14. • For each statement, name the logical form of the goal, say what first move it suggests, and write the proof. (a) If $A \subseteq B$ and $B \cap C = \varnothing$, then $A \cap C = \varnothing$. (b) For every integer $n$ there is an even integer $m$ with $m > n$.

15. • Let $f, g \colon \R \to \R$ be strictly decreasing. By unpacking the definitions, prove that $g \circ f$ is strictly increasing.

16. • Let $A$ and $B$ be sets. Prove that $A \subseteq B$ if and only if $\mathcal{P}(A) \subseteq \mathcal{P}(B)$, where $\mathcal{P}$ denotes the [power set](/00E0YZCERH/). Unpack both inclusions before you start.

17. • A student hands in this column as a proof that if $x$ is rational and $y$ is irrational, then $x + y$ is irrational: "$x = p/q$; $x + y = r/s$; $y = r/s - p/q = (rq - ps)/(qs)$; $y \in \Q$, contradiction." Write it as a proof in sentences, with the words that say what each line is: an assumption, a definition, a consequence or the conclusion. Name every fact about $p$, $q$, $r$ and $s$ that the column leaves out.

18. • Write a structured proof, with two levels, that for all integers $a$ and $b$, if $ab$ is odd, then $a$ and $b$ are both odd. Use the contrapositive at level $1$ and a case split at level $2$.

19. • Prove that $6$ divides $n^3 + 5n$ for every integer $n$, twice: once in one or two sentences for a reader who knows elementary number theory, and once with every step written out for a first-year student. Start from $n^3 + 5n = (n - 1) n (n + 1) + 6n$.

20. • Theorem: if $f \colon [a, b] \to \R$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f'(x) > 0$ for every $x \in (a, b)$, then $f$ is strictly increasing on $[a, b]$. Proof: let $a \le x < y \le b$; the [mean value theorem](/0BARQY52N5/) on $[x, y]$ gives $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x)$, and $f'(c) > 0$ and $y - x > 0$ give $f(y) > f(x)$. (a) Mark where each hypothesis is used. (b) Give a function on $[0, 1]$ that is differentiable on $(0, 1)$ with $f' > 0$ there, is not continuous at $1$, and is not strictly increasing on $[0, 1]$. Which step of the proof fails for it?

21. • "Claim: if $p_1 < p_2 < \dots < p_k$ are the first $k$ primes, then $p_1 p_2 \cdots p_k + 1$ is prime. Proof: no $p_i$ divides $p_1 p_2 \cdots p_k + 1$, since the remainder on division by $p_i$ is $1$." Find the first $k$ for which the claim fails and factor the number. Which step of the proof is wrong? State what the argument does prove, and explain how that proves that there are infinitely many primes.

22. • Check this proof and give a verdict. "Claim: $n^2 + n$ is odd for every integer $n \ge 1$. Proof by induction: suppose that $k^2 + k$ is odd. Then $(k + 1)^2 + (k + 1) = (k^2 + k) + 2(k + 1)$ is odd plus even, so it is odd. By induction, the claim holds." Is the inductive step correct? Is the claim true?

23. ★ (a) Prove that for every $\varepsilon > 0$ there is $\delta > 0$ such that for all $x, y \in [0, 1]$, if $\abs{x - y} < \delta$, then $\abs{x^2 - y^2} < \varepsilon$. (b) Write the negation of the same statement with $[0, \infty)$ in place of $[0, 1]$, with all quantifiers explicit, and prove the negation.

24. ★ Write a structured proof, with at least two levels and a numbered lemma, that there are infinitely many primes $p$ with $p \equiv 3 \pmod 4$. Start from a finite list $p_1, \dots, p_k$ of such primes and consider $N = 4 p_1 p_2 \cdots p_k - 1$.

25. ★ Read the proof of [Cantor's theorem](/0WTEMGYV2C/): "Let $f \colon X \to \mathcal{P}(X)$ be a function and let $D = \set{x \in X : x \notin f(x)}$. Suppose $D = f(d)$ for some $d \in X$. If $d \in D$, then $d \notin f(d) = D$; if $d \notin D$, then $d \in f(d) = D$. Both are impossible, so $D$ is not a value of $f$, and $f$ is not surjective." (a) Write the reason for each sentence. (b) Run the proof on $X = \set{1, 2, 3}$ with $f(1) = \set{1, 2}$, $f(2) = \varnothing$ and $f(3) = \set{1, 3}$: find $D$ and check that it is not a value of $f$. (c) Does the proof use that $X$ is finite?

26. ★ Write a short referee report (a summary, a verdict, each problem with its line, and a repair) on this proof. "Claim: every Cauchy sequence $(a_n)$ of real numbers is bounded. Proof: take $\varepsilon = 1$ in the definition of a Cauchy sequence; there is $N$ with $\abs{a_n - a_m} < 1$ for all $n, m \ge N$. In particular $\abs{a_n - a_N} < 1$, so $\abs{a_n} < \abs{a_N} + 1$. Hence $(a_n)$ is bounded by $\abs{a_N} + 1$."

27. ★ Write a short referee report on this proof. "Claim: if $a$, $b$ and $c$ are positive reals with $a + b + c = 3$, then $ab + bc + ca \le 3$. Proof: the claim is symmetric in $a$, $b$ and $c$, so we may assume $a = b = c$. Then $a = b = c = 1$ and $ab + bc + ca = 3$." Decide whether the claim is true, and if it is, give a correct proof.
