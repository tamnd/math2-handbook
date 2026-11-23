1. ◦ In the official language of [propositional formulas](/TT7WT5HPN9/), each connective comes with one pair of brackets. A formula has $7$ connectives. How many bracket symbols does it contain? Can an official formula contain exactly $9$ brackets?

2. ◦ The arrow groups to the right, so $p \to q \to r$ means $p \to (q \to r)$. Find every [valuation](/H31CS3HK5P/) of $p, q, r$ at which $(p \to q) \to r$ and $p \to (q \to r)$ take different values.

3. ◦ In Polish notation, $C$ stands for $\to$, $K$ for $\land$ and $N$ for $\neg$, each written before its arguments. Which of the strings $CKpqr$, $KCpq$, $NCpNq$, $CpqNr$ are formulas? Write each formula in ordinary notation.

4. ◦ Decide whether $\set{p \lor q, \; \neg q \lor r} \models p \lor r$, and whether $\set{p \lor q, \; \neg q \lor r} \models r$. For a [consequence](/1HK0VYWTV7/) that fails, give a valuation that shows it.

5. ◦ Which of these formulas are in [CNF](/0B3D4C8YF2/), and which are in [DNF](/0GVDFAY4KW/): $p \lor \neg q$, $\neg \neg p$, $(p \lor q) \land \neg r$, $p \land q$?

6. ◦ Which of these [clauses](/T3SXVH3ZZC/) are [Horn clauses](/QR92EZDTKF/): $\set{\neg p, \neg q, r}$, $\set{\neg p, \neg q}$, $\set{p}$, $\set{p, q, \neg r}$, $\square$?

7. ◦ How many Boolean functions of $3$ variables are there? How many of them preserve both $0$ and $1$, that is, satisfy $f(0,0,0) = 0$ and $f(1,1,1) = 1$?

8. ◦ Show that $p$ and $p \lor \neg p$ are [equisatisfiable](/B37TYWXS74/), but $\neg p$ and $\neg (p \lor \neg p)$ are not.

9. • Express $\neg p$, $p \lor q$ and $p \land q$ using only the Peirce arrow $p \downarrow q = \neg (p \lor q)$, and check each formula by its truth table.

10. • Let $\varphi = \neg \bigl( (p \land q) \lor (\neg p \land r) \bigr)$. Find a CNF and a DNF of $\varphi$, each with two clauses or two terms, and describe $\varphi$ in words.

11. • Run the marking algorithm on the Horn clauses $p$, $\; \neg p \lor q$, $\; \neg q \lor \neg r \lor s$, $\; \neg p \lor r$, $\; \neg s \lor t$, $\; \neg t \lor \neg q$, and decide whether the set is satisfiable. Then delete the clause $\neg p \lor r$, run the algorithm again, and give the least model of the definite clauses that remain.

12. • Let $\varphi$ be a [tautology](/05006AJ7DZ/) with variables $p_1, \ldots, p_n$, and let $\psi_1, \ldots, \psi_n$ be any formulas. Prove that the formula obtained by replacing each $p_i$ by $\psi_i$ at the same time is a tautology.

13. • Give a 3-CNF with two new variables $x$, $y$ that is equisatisfiable with the clause $p_1 \lor p_2 \lor p_3 \lor p_4 \lor p_5$, and prove that it is.

14. • Use [resolution](/ZDW6N1PGJ7/) to show that the clauses $\set{p, q}$, $\set{p, \neg q}$, $\set{\neg p, r}$, $\set{\neg p, \neg r}$ are unsatisfiable.

15. • In the [system L](/1MGMQX43B8/), show that $\vdash (\varphi \to (\psi \to \chi)) \to (\psi \to (\varphi \to \chi))$. Use the [deduction theorem](/9X08XK5RV2/).

16. • Read $\to$ by its truth table and read $\neg$ as the constant function $0$. Use this to show that the schema A3 of L cannot be derived from A1 and A2 by modus ponens, as in the [independence of axioms](/729RCBPAM3/).

17. • In the three-element chain $0 < \tfrac12 < 1$, read $a \to b$ as $1$ when $a \le b$ and as $b$ otherwise. Find values of $p$ and $q$ at which [Peirce's law](/GMSZ75D5WE/) $((p \to q) \to p) \to p$ does not take the value $1$.

18. • Let $\Gamma$ be a set of formulas such that every valuation makes at least one member of $\Gamma$ true. Use [compactness](/4X9126SEMM/) to prove that $\gamma_1 \lor \cdots \lor \gamma_n$ is a tautology for some $\gamma_1, \ldots, \gamma_n \in \Gamma$.

19. • Suppose $\varphi \models \psi$, where $\varphi$ and $\psi$ have no variable in common. Prove that $\varphi$ is unsatisfiable or $\psi$ is a tautology.

20. • Let $\varphi = (p \lor q) \land (\neg p \lor r)$ and $\psi = q \lor r \lor s$. Check that $\varphi \models \psi$, and find a [Craig interpolant](/TRS2HY57EG/) whose variables are among $q$ and $r$.

21. ★ Give a derivation in L of $\neg \neg \varphi \to \varphi$ for every formula $\varphi$. You may use $\vdash \chi \to \chi$ and the deduction theorem.

22. ★ Prove that $\set{\neg, \leftrightarrow}$ is not [functionally complete](/TDZVCWYJ9F/): show that every formula in these connectives computes a function of the form $c \oplus x_{i_1} \oplus \cdots \oplus x_{i_k}$, and that $p \land q$ is not of this form.

23. ★ Without quoting [Post's theorem](/WGBR7JHBV4/), prove that among the sixteen binary connectives only $\uparrow$ and $\downarrow$ are functionally complete on their own.

24. ★ The majority function $\mathrm{maj}(p, q, r)$ is $1$ when at least two of its arguments are $1$. Prove that $\set{\mathrm{maj}, \neg}$ is not functionally complete, and that $\set{\mathrm{maj}, \neg, \bot}$ is.

25. ★ Let $\gamma_1, \gamma_2, \ldots$ be formulas with $\gamma_{n+1} \models \gamma_n$ and $\gamma_n \not\models \gamma_{n+1}$ for every $n$, and let $\Gamma = \set{\gamma_1, \gamma_2, \ldots}$. Prove that no single formula $\varphi$ has the same models as $\Gamma$.
