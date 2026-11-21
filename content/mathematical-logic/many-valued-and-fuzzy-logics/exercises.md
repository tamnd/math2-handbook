1. ◦ Compute the value of $\neg p \to (p \to q)$ at $p = \tfrac12$, $q = 0$ in [Łukasiewicz three-valued logic](/1CE2TGM6MQ/), in [strong Kleene logic](/SZHA10A9X7/) and in Bochvar's $\mathrm{B}_3$. In the last two, read $\varphi \to \psi$ as $\neg\varphi \lor \psi$. Is the formula a tautology of $\mathrm{Ł}_3$?

2. ◦ Both $\mathsf{K}_3$ and $\mathsf{LP}$ are [logical matrices](/P7E926JK13/) on the strong Kleene tables. Decide whether modus ponens in the form $p, \neg p \lor q \models q$ is valid in each of them, and give a counterexample where it fails.

3. ◦ Show that simplification $p \land q \models p$ is valid in $\mathrm{B}_3$ and invalid in $\mathsf{PWK}$. Use the tables of [weak Kleene logic](/BCK5QXQXA6/).

4. ◦ In [first-degree entailment](/KXTP4P3GHT/), let $v(p) = \mathbf{B}$ and $v(q) = \mathbf{N}$. Compute the values of (a) $(p \lor q) \land \neg q$, (b) $\neg(p \land q)$, (c) $p \lor \neg q$, and say which of them are designated.

5. ◦ In the four-valued logic $\mathrm{P}_4$ of [Post's many-valued logics](/YHYSGRE7JV/), with values $0, 1, 2, 3$ and $\neg x = x - 1 \bmod 4$, find the least $k \ge 1$ with $\neg^k x = x$ for all $x$. Then write the table of $x \land \neg x$.

6. ◦ Let $f$ be a binary operation on $\set{0, 1, 2}$ with $f(0, 0) = 0$. Show that $f$ is not a [Sheffer function](/1K829SJG3K/).

7. ◦ In [Łukasiewicz infinite-valued logic](/NFCEM44XYH/), let $p = 0.6$ and $q = 0.7$. Compute $p \oplus q$, $p \odot q$, $p \to q$ and $q \to p$, and check the De Morgan law $\neg(p \odot q) = \neg p \oplus \neg q$ at these values.

8. ◦ For the Łukasiewicz, minimum and product [t-norms](/VR6D8JXX1W/), compute $x * y$, the residuum $x \Rightarrow y$ and the negation $x \Rightarrow 0$ at $x = 0.6$, $y = 0.3$.

9. ◦ In [probability logic](/Z2WRGJDRQT/), let $P(p) = 0.7$ and $P(q) = 0.6$. Find the best lower and upper bounds for $P(p \land q)$ and for $P(p \lor q)$.

10. ◦ In [vector logic](/DJ41X602BJ/), let $u = 0.3\, s + 0.7\, n$ and $v = 0.6\, s + 0.4\, n$. Compute the scalar value $s^T X (u \otimes v)$, where $X$ is the matrix of exclusive or.

11. • Show that $(p \oplus p \oplus p) \to (p \oplus p)$ is a tautology of $\mathrm{Ł}_3$ but not of $\mathrm{Ł}_\infty$. Find the least value it takes on $[0, 1]$, and where. Compare with the remark on finite chains after [Chang's completeness theorem](/QM0F33QE9P/).

12. • In $\mathrm{Ł}_3$, show that $p \to (p \to q)$ and $p \to q$ take different values at $p = \tfrac12$, $q = 0$. Then prove that for every set $\Gamma$ and all formulas $\varphi, \psi$, $\Gamma, \varphi \models \psi$ holds if and only if $\Gamma \models \varphi \to (\varphi \to \psi)$.

13. • Show that $p \land \neg p \models q \lor \neg q$ is valid in $\mathsf{K}_3$ and in $\mathsf{LP}$, but not in [FDE](/KXTP4P3GHT/). What does this show about FDE and the inferences that $\mathsf{K}_3$ and $\mathsf{LP}$ have in common?

14. • Let $U$ be the set of all unary operations on $\set{0, 1, 2}$. Use Słupecki's criterion, from the entry on [Sheffer functions](/1K829SJG3K/), to decide which of these sets are functionally complete: (a) $U \cup \set{\max}$, (b) $U \cup \set{x + y \bmod 3}$, (c) $U \cup \set{g}$ with $g(x, y) = \min(1, x y)$.

15. • By [McNaughton's theorem](/E11A9H8Z7Q/), the function $f(x) = \max(0, \min(1, 3x - 1))$ on $[0, 1]$ is defined by a formula in one variable $p$. Find such a formula, using only $\oplus$ and $\odot$.

16. • The nilpotent minimum is the t-norm $x * y = \min(x, y)$ if $x + y > 1$, and $x * y = 0$ otherwise. Show that its residuum is $x \Rightarrow y = 1$ if $x \le y$ and $\max(1 - x, y)$ if $x > y$. Show that its negation $x \Rightarrow 0$ is $1 - x$, so the standard [MTL](/PT5PHKJDYM/)-algebra of this t-norm has an involutive negation.

17. • Show that the weak law of excluded middle $\neg p \lor \neg\neg p$ is a tautology of Gödel logic and of [product logic](/YTHRDT9PDR/), but not of Łukasiewicz logic.

18. • Write $\otimes$ for the t-norm conjunction. Decide in Łukasiewicz, Gödel and product logic whether $\neg(p \otimes q) \to (\neg p \lor \neg q)$ is a tautology. Where it fails, find its least value and the point where it is attained.

19. • In rational [Pavelka logic](/YG62F8YC0P/), let $T = \set{\overline{0.9} \to p,\ \overline{0.8} \to (p \to q),\ \overline{0.7} \to (q \to r)}$. Find the truth degree of $r$ in $T$, and give a model of $T$ that attains it. What degree would the minimum rule claim?

20. • In probability logic, the premises $p$, $q$, $r$ classically entail $p \land q \land r$. Each premise has probability at least $0.95$. Use the theorem of Adams on uncertainties to bound $P(p \land q \land r)$ from below, and give a probability function on the formulas in $p, q, r$ that reaches the bound.

21. • In the [Rényi–Ulam game with one lie](/402GXME26B/), let $U = \set{1, \dots, 6}$. (a) What lower bound does the weight argument give for the number of questions? (b) Suppose the state is $\sigma = (1, 1, \tfrac12, 0, \tfrac12, 1)$, four questions remain, and the question $Q = \set{1, 3, 4}$ gets the answer yes. Compute the new state, and check that $W_3(\sigma_{\mathrm{yes}}) + W_3(\sigma_{\mathrm{no}}) = W_4(\sigma)$.

22. • In vector logic, let $\alpha = \alpha' = \tfrac12$. How many of the $16$ classical binary connectives $G$ give $s^T G (u \otimes v) = \tfrac12$? List them.

23. ★ (a) Show that every tautology of $\mathrm{Ł}_5$, the Łukasiewicz logic on $\set{0, \tfrac14, \tfrac12, \tfrac34, 1}$, is a tautology of $\mathrm{Ł}_3$. (b) Let $p \leftrightarrow q$ be $(p \to q) \land (q \to p)$ and let $\varphi^k$ be the $\odot$-power with $k$ factors. Find the least $k$ such that $\neg\bigl((p \leftrightarrow \neg p)^k\bigr)$ is a tautology of $\mathrm{Ł}_4$, and show that this formula is not a tautology of $\mathrm{Ł}_3$ for any $k$.

24. ★ Let $\Gamma$ be a set of formulas in $\neg, \land, \lor$ that is classically satisfiable. Prove that $\Gamma \models_{\mathrm{B}_3} \varphi$ if and only if $\Gamma \models \varphi$ classically and every variable of $\varphi$ occurs in some formula of $\Gamma$. What happens when $\Gamma$ is classically unsatisfiable?

25. ★ Show that $f(x, y) = \min(x, y) + 1 \bmod 3$ is a Sheffer function on $\set{0, 1, 2}$. You may use [Post's theorem](/YHYSGRE7JV/) that $\neg x = x - 1 \bmod 3$ and $\max$ together are functionally complete.

26. ★ Let $V \subseteq [0, 1]$ be closed with $0, 1 \in V$. Show that the sentence $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ belongs to the [first-order Gödel logic](/H8C323CV3T/) $\mathrm{G}_V$ if and only if $0$ is an isolated point of $V$. Is it in $\mathrm{G}_{[0, 1]}$?

27. ★ In the Rényi–Ulam game with one lie and three elements, show that the weight bound allows four questions, but that no strategy with four questions fixed in advance always finds $x$. Then give a strategy with five questions fixed in advance.
