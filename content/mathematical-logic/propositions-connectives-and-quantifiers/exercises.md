1. ◦ Which of these are [propositions](/0ZGC7ZESYN/)? For each proposition give its truth value. (a) $17$ is a sum of two squares. (b) $x + 1 = 3$. (c) Is $91$ prime? (d) This sentence is false. (e) There are infinitely many primes $p$ such that $p + 2$ is also prime.

2. ◦ Let $p$ be true and $q$, $r$ false. Compute $p \oplus q \oplus r$ and $(p \leftrightarrow q) \leftrightarrow r$, and check each answer against the counting rule for [exclusive or](/PTMR3P9J6C/) and for the [biconditional](/0S6GMNJ62Y/).

3. ◦ Write the [negation](/029JBBF693/) of each statement without the word "not" in front: (a) $x \le 0$ or $x \ge 1$, for a real $x$; (b) $n$ is even and $n > 4$, for an integer $n$.

4. ◦ For integers $n$, write the [converse, the inverse](/09A3N7ZN5G/) and the [contrapositive](/04T1CT7212/) of "if $10$ divides $n$, then $5$ divides $n$". Which of the four statements are true for every integer $n$?

5. ◦ For an integer $n$, is "$4$ divides $n$" necessary, sufficient, both or neither for "$4$ divides $n^2$"? Answer the same question for "$n$ is even". Use the language of [necessary and sufficient conditions](/09BJQQB3VS/).

6. ◦ Name the form of each argument and say whether it is valid. (a) If $7 \mid n$ then $7 \mid n^2$; $7 \nmid n^2$; so $7 \nmid n$. (b) If $f$ is differentiable at $0$ then $f$ is continuous at $0$; $f$ is continuous at $0$; so $f$ is differentiable at $0$. (c) $x = 1$ or $x = 2$; $x \neq 1$; so $x = 2$.

7. ◦ Decide the truth value of "every prime $p$ with $90 < p < 96$ is even" and of "some prime $p$ with $90 < p < 96$ is odd". Which of the two is a [vacuous truth](/0V4QXPGJQK/)?

8. ◦ Over the integers, decide the truth value of each statement: (a) $\forall x\, \exists y\, (x + y = 0)$; (b) $\exists y\, \forall x\, (x + y = 0)$; (c) $\forall x\, \exists y\, (x y = 1)$; (d) $\exists x\, \forall y\, (x y = 0)$.

9. ◦ A sequence $(a_n)$ converges to $L$ when $\forall \varepsilon > 0\; \exists N\; \forall n \ge N\; |a_n - L| < \varepsilon$. Write the negation with $\neg$ moved all the way in, using the [negation of a universal statement](/0P3A06QNDP/) and of an [existential statement](/05SZQKH75K/).

10. ◦ How many rows has the truth table of a formula in $5$ variables? How many truth functions of $3$ variables are there? How many of the $16$ binary [connectives](/QS0XVAN9BG/) depend on both of their arguments?

11. • Use a [truth table](/05RSK4Q657/) or a short argument to decide which of these are [tautologies](/05006AJ7DZ/): (a) $(p \to q) \lor (q \to p)$; (b) $(p \to q) \to (\neg p \to \neg q)$; (c) $\bigl(p \land (q \lor r)\bigr) \leftrightarrow \bigl((p \land q) \lor (p \land r)\bigr)$. For each one that is not, give a falsifying row.

12. • Use the [laws of propositional logic](/A9CSGZNBV5/), not truth tables, to show that $(p \land q) \to r \equiv (p \to r) \lor (q \to r)$ and $p \to (q \land r) \equiv (p \to q) \land (p \to r)$.

13. • Express $p \oplus q$ using only the [Sheffer stroke](/1NNYWRN6B8/) $\uparrow$, and check your formula.

14. • Show that $\set{\neg, \leftrightarrow}$ is not a complete set of connectives: prove that every formula in $p$ and $q$ built from $p$, $q$, $\neg$ and $\leftrightarrow$ is true in an even number of the four rows, and conclude that $p \land q$ cannot be expressed.

15. • Prove $p \land (\neg p \lor q) \equiv p \land q$ from the laws, then write down the dual equivalence and say why the duality principle gives it for free.

16. • Use the values $0$, $\tfrac12$, $1$ with $\neg x = 1 - x$ and $x \lor y = \max(x, y)$. In Kleene's logic let $x \to y = \max(1 - x, y)$, and in Łukasiewicz's logic let $x \to y = \min(1, 1 - x + y)$. Compute $p \to p$ and $p \lor \neg p$ at $p = \tfrac12$ in each logic. Which of the two formulas takes the value $1$ for every value of $p$ in Łukasiewicz's logic? Compare with the [law of excluded middle](/0RYYK8PG4S/).

17. • Find every valuation of $p$, $q$, $r$ at which $(p \to q) \to r$ and $p \to (q \to r)$ have different truth values.

18. • [Translate into logical form](/WGZX7GV3PP/), with a dictionary, and then negate: (a) every integer greater than $1$ has a prime divisor; (b) the function $f \colon \R \to \R$ is bounded.

19. • Decide the truth value of each statement with the [uniqueness quantifier](/0QAJHFGZZJ/): (a) $\exists! x \in \Z\; (x^2 = x)$; (b) $\exists! x \in \R\; (e^x = 1)$; (c) $\exists! x \in \Z\; (2x = 3)$; (d) $\exists! x \in \Z\; (x^2 < 1)$.

20. • Give a countermodel to each argument form, as in the entry on [formal fallacies](/T5BG7Y4J0T/): (a) from $\forall x\, (P(x) \to Q(x))$ and $\exists x\, Q(x)$, conclude $\exists x\, P(x)$; (b) from $\forall x\, (P(x) \to Q(x))$ and $\exists x\, \neg P(x)$, conclude $\exists x\, \neg Q(x)$.

21. • On the [island of knights and knaves](/MVADXMFV59/), $A$ says "$B$ is a knave" and $B$ says "$A$ and I are of the same type". Write each statement as a biconditional and find the types of $A$ and $B$.

22. • Prove that $\forall x \in \R\; \exists y \in \R\; (y > x^2)$ is true and that $\exists y \in \R\; \forall x \in \R\; (y > x^2)$ is false. Which rule about the [order of quantifiers](/0FYQMKFE77/) does the pair illustrate?

23. ★ Prove that every truth function of $n \ge 1$ variables is expressed by a formula built from the variables with $\neg$, $\land$ and $\lor$. Deduce that the Sheffer stroke alone is complete.

24. ★ A truth function is *T-preserving* when it takes the value T at the row where all its arguments are T. How many truth functions of $n$ variables are T-preserving? How many are both T-preserving and F-preserving? Give both numbers for $n = 2$ and list the binary connectives in the second set.

25. ★ Prove that the only binary connectives that are complete on their own are $\uparrow$ and $\downarrow$.

26. ★ Prove $\neg\neg(p \lor \neg p)$ without using the law of excluded middle or double negation elimination: use only the introduction rule for $\lor$, modus ponens, and the rule that derives $\neg \varphi$ from a contradiction under the assumption $\varphi$.

27. ★ Prove that every formula built from $p$ and $q$ with $\land$ and $\lor$ only is [logically equivalent](/0JMR2HM2N2/) to one of $p$, $q$, $p \land q$, $p \lor q$.
