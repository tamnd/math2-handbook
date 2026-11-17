1. ◦ A textbook says: "If $a^2$ is even, then $a$ is even, since otherwise $a^2$ would be odd." Write the proof out in full for a first-year reader, in the sense of [mathematical rigour](/E1PE9R8DBB/), and list every fact about integers that it uses.

2. ◦ On the segment from $0$ to $1$, draw $n$ semicircles side by side, each of diameter $1/n$. Find the total length of the curve. As $n \to \infty$ the curves approach the segment. What does the picture seem to prove, and why is it wrong?

3. ◦ Two copies of a staircase of $1, 2, \ldots, n$ unit squares fit together into a rectangle. Draw the picture for $n = 4$, write in words the argument it shows for $1 + 2 + \cdots + n = \frac{n(n+1)}{2}$, and say what in your words makes the argument work for every $n$, as a [proof without words](/V6ESFEFKJC/) must.

4. ◦ A paper reduces a theorem to $10^4$ finite cases and checks them with a program. The authors also publish, for each case, a certificate that a separate checker of $200$ lines verifies. In the terms of [computer-assisted proof](/MC18C7BMFT/), which of the things a reader must trust does the certificate replace, and which does it leave?

5. ◦ Say what each case shows about the [acceptance of proofs](/MJ3EHQJJHX/): (a) Kempe's proof of the four colour theorem (1879), whose error Heawood found in 1890; (b) Perelman's proof of the Poincaré conjecture, posted as preprints in 2002 and 2003 and never submitted to a journal; (c) Mochizuki's claimed proof of the abc conjecture, posted in 2012.

6. ◦ Tymoczko named three features of a proof: it is convincing, it is surveyable, and it is formalizable. Say what each means, and which one he argued the four colour proof lacks. What did he conclude about the nature of that proof?

7. ◦ In [the Jaffe–Quinn and Thurston debate](/K3M3TEX7SJ/), what did Jaffe and Quinn mean by "theoretical mathematics", and what did they propose about how such work should be labelled and credited?

8. • Use the axiom schemes $A \to (B \to A)$ and $(A \to (B \to C)) \to ((A \to B) \to (A \to C))$, with modus ponens as the only rule, to give a [formal derivation](/8VZ77R4R8S/) of $p \to p$. How many lines does it take, and how long would an informal proof be?

9. • Let $F_m = 2^{2^m} + 1$. Prove that $F_0 F_1 \cdots F_{m-1} = F_m - 2$ for $m \ge 1$, deduce that any two Fermat numbers are coprime, and conclude that there are infinitely many primes. This is one of the [many proofs](/KNQDDN6PT2/) of Euclid's theorem.

10. • Prove that the composite of two injective functions is injective twice: once in two sentences, as in a textbook, and once with every step justified by a definition or a rule of logic. Which steps did the short proof leave to the reader?

11. • The classical argument that every triangle is isosceles takes the point $P$ where the bisector of the angle at $A$ meets the perpendicular bisector of $BC$, drops perpendiculars from $P$ to $AB$ and $AC$, and finds congruent triangles. Draw an accurate figure and find the error. What fact does the usual figure supply that the axioms of [Hilbert](/KM1FB8XZ2R/) would require to be proved?

12. • Divide a unit square into four equal squares and shade one; divide the square at the opposite corner into four and shade one; and so on. Explain how the picture shows $\frac{1}{4} + \frac{1}{16} + \frac{1}{64} + \cdots = \frac{1}{3}$, and write a proof that the picture suggests.

13. • Call a set $S$ of integers sum-free if $x + y \notin S$ for all $x, y \in S$, with $x = y$ allowed. Split $\set{1, 2, 3, 4}$ into two sum-free sets, and prove by a case analysis that $\set{1, 2, 3, 4, 5}$ cannot be split so. Is your case analysis surveyable? What would change if the analysis had $10^{12}$ cases?

14. • Prove that among any $n + 1$ integers chosen from $\set{1, 2, \ldots, 2n}$, two are coprime. Why might this proof count as a [Book proof](/A4RJYP79A7/)?

15. • Prove $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ in two ways: from the binomial theorem, and by counting subsets of an $n$-element set. Which proof explains the identity better, and why?

16. • Give an informal proof that if $a \mid b$ and $a \mid c$ then $a \mid b + c$. Then list what a formal proof in a proof assistant would need: the definition, the algebraic laws and the rules of logic used at each step.

17. ★ Cauchy stated in 1821 that a convergent sum of continuous functions is continuous. Show that $\sum_{n=0}^{\infty} (x^n - x^{n+1})$ converges at every $x \in [0, 1]$, that every term is continuous, and that the sum is not. Show that the convergence is not uniform, and say which hypothesis repairs the theorem.

18. ★ Prove the five colour theorem: every planar graph can be properly coloured with $5$ colours. Use the fact that a planar graph has a vertex of degree at most $5$, and Kempe chains for that vertex. Where does the same argument fail for $4$ colours?

19. ★ Prove that $\sqrt{2}$ is irrational by an extremal argument: suppose $n$ is the least positive integer such that $n\sqrt{2}$ is an integer, and find a smaller one. Compare this proof with the usual proof by parity. Which generalizes more easily to $\sqrt{k}$ for $k$ not a square?

20. ★ Let $p_1 < p_2 < \cdots$ be the primes. Show that Euclid's proof gives $p_n \le 2^{2^{n-1}}$, and that the proof of exercise 9 gives a bound of almost the same form. What does this say about what different proofs of the same theorem can give?
