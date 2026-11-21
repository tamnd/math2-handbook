1. ◦ For each [residuated lattice](/E337A6WVH3/), say which of the equations $x \cdot y = y \cdot x$, $x \le 1$ and $x \le x \cdot x$ hold, where $1$ is the unit of $\cdot$. (a) $[0, 1]$ with $x \cdot y = \max(0, x + y - 1)$ and unit $1$. (b) $\Z$ with $\min$, $\max$, $x \cdot y = x + y$ and unit $0$. (c) A Heyting algebra with $x \cdot y = x \wedge y$ and unit the top element. Which structural rules does each one model?

2. ◦ The atom count is the same on both sides of each sequent below. Decide which are derivable in the [Lambek calculus](/5FAC9KX4H0/) $\mathsf{L}$. (a) $np/n, n \Rightarrow np$. (b) $n, np/n \Rightarrow np$. (c) $np, (np \backslash s)/np, np \Rightarrow s$. (d) $(np \backslash s)/np, np, np \Rightarrow s$.

3. ◦ Derive $A \backslash B \Rightarrow B / A$ in $\mathsf{FL}_e$, the [full Lambek calculus](/V5XVVN16GS/) with [exchange](/YAFD18WYJ8/). Then show that for distinct atoms $a, b$ the sequent $a \backslash b \Rightarrow b / a$ has no cut-free derivation in $\mathsf{FL}$.

4. ◦ Write the Girard translation of the suffixing formula $(p \to q) \to ((q \to r) \to (p \to r))$ into [linear logic](/2P2184B6HE/), using $(A \to B)^\circ = {!A^\circ} \multimap B^\circ$ and $p^\circ = p$.

5. ◦ A cut-free [proof net](/HN6WN1VE39/) has three $\otimes$ links and two $\mathbin{\wp}$ links. How many axiom links and atom occurrences does it have? How many switchings, and how many edges does each correction graph have?

6. ◦ In the [phase space](/64MHHQQ6G6/) $\Z/3$ with addition and $\bot = \set{0}$, list all the facts. Which subsets of $\Z/3$ are not facts?

7. ◦ State, from the entries of this chapter, whether provability is decidable, and if so its complexity, for: (a) MLL; (b) MALL; (c) full propositional linear logic; (d) affine linear logic; (e) the relevance logic $\mathbf{R}$; (f) the pure implication fragment of $\mathbf{R}$.

8. ◦ Which formulas pass the variable sharing test of [relevance logic](/KXTCZ2FY5M/)? (a) $(p \wedge \neg p) \rightarrow q$. (b) $p \rightarrow (q \rightarrow q)$. (c) $(p \rightarrow q) \rightarrow (\neg q \rightarrow \neg p)$. (d) $q \rightarrow (p \vee \neg p)$. (e) $p \rightarrow (q \rightarrow p)$. Does passing the test make (e) a theorem of $\mathbf{R}$?

9. ◦ In [abelian logic](/W3CPQAFQJ3/), compute the value of each formula under a valuation $v$, and say whether it is valid. (a) $(p \to q) \to ((q \to r) \to (p \to r))$. (b) $p \to (p \to p)$. (c) $((p \to p) \to p) \to p$.

10. • Show that $A \backslash B, B \backslash C \Rightarrow A \backslash C$ is derivable in the Lambek calculus. Then show that for distinct atoms $a, b, c$ the sequent $b \backslash c, a \backslash b \Rightarrow a \backslash c$ is not, although its atom count balances.

11. • The Lambek calculus derives the type raising $np \Rightarrow s/(np \backslash s)$. Show that the converse $s/(np \backslash s) \Rightarrow np$ passes the atom count but is not derivable.

12. • Show that $a \cdot (b/c) \Rightarrow (a \cdot b)/c$ is derivable in $\mathsf{L}$, and that the converse $(a \cdot b)/c \Rightarrow a \cdot (b/c)$ is not, for distinct atoms $a, b, c$.

13. • For distinct atoms $a, b$, decide which formulas are derivable in MALL and which in [affine logic](/K67C2N2QAH/). (a) $a \otimes b \multimap a \mathbin{\&} b$. (b) $a \mathbin{\&} b \multimap a \otimes b$. (c) $a \mathbin{\&} b \multimap a$. (d) $a \otimes a \multimap a$.

14. • Each proof structure below has the axiom links $p - p^\perp$ and, where $q$ occurs, $q - q^\perp$. Use the Danos–Regnier criterion to decide which are proof nets. (a) Conclusions $p \otimes q$ and $p^\perp \mathbin{\wp} q^\perp$. (b) Conclusions $p \otimes q$ and $p^\perp \otimes q^\perp$. (c) The conclusion $p \mathbin{\wp} p^\perp$. (d) Conclusions $p^\perp \mathbin{\wp} q^\perp$ and $q \otimes p$.

15. • In the phase space $\Z/3$ with $\bot = \set{0}$, put $p^* = \set{1}$. Decide whether $\vdash p^\perp, p \otimes p$ and $\vdash p^\perp, p^\perp, p^\perp$ are valid in this model. Is the second sequent derivable in linear logic?

16. • Count the cliques of the [coherence spaces](/WSGZ5HGK1X/) $\mathbf{Bool} \otimes \mathbf{Bool}$, $\mathbf{Bool} \mathbin{\wp} \mathbf{Bool}$ and $\mathbf{Bool} \multimap \mathbf{Bool}$, where $\mathbf{Bool}$ is the flat space on $\set{t, f}$. Which cliques of $\mathbf{Bool} \multimap \mathbf{Bool}$ are the identity and negation?

17. • The *right-sequential or* $G$ from $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$ to $\mathbf{Bool}$ reads its second argument first: $G(c) = \set{t}$ if $t_2 \in c$, or if $f_2, t_1 \in c$; $G(c) = \set{f}$ if $f_2, f_1 \in c$; and $G(c) = \emptyset$ otherwise. Find its trace. Is $G$ linear?

18. • Use the level translation $T_k$ of the [light linear logics](/E7JVJSSWBT/) entry to show that $!!p \multimap !p$ is not derivable in ELL. Then derive $!p \multimap {!p} \otimes {!p}$ in ELL, and $!!p \multimap !p$ in full linear logic.

19. • In the natural deduction system of Anderson and Belnap, with index sets, derive the suffixing formula $(A \rightarrow B) \rightarrow ((B \rightarrow C) \rightarrow (A \rightarrow C))$. At which step does the same method fail for $p \rightarrow (q \rightarrow p)$?

20. • In the two-point [Routley–Meyer model](/H4Z8J0KMAY/), with $W = \set{0, 1}$, $0^* = 1$, $1^* = 0$ and $Rabc$ for every triple except $(0, 0, 1)$, decide which formulas are true at $0$ under every valuation. (a) $\neg p \rightarrow (p \rightarrow q)$. (b) $p \rightarrow (q \rightarrow q)$. (c) $(p \wedge (\neg p \vee q)) \rightarrow q$. (d) $(p \rightarrow q) \vee (q \rightarrow p)$. (e) $\neg (p \wedge \neg p)$. Give a refuting valuation for each one that fails.

21. • In the resource model of [bunched logic](/5JKHNK7AR5/) on $(\N, +, 0)$ with equality as the order, put $V(p) = \set{1}$ and $V(q) = \set{2}$. Find all resources that force (a) $p \ast q$; (b) $p \mathrel{-\!\!*} q$; (c) $q \mathrel{-\!\!*} p$; (d) $p \ast (p \mathrel{-\!\!*} q)$; (e) $(p \ast p) \mathrel{-\!\!*} q$.

22. • Decide which formulas are valid in abelian logic. (a) $(p \wedge q) \to p$. (b) $(p \to q) \vee (q \to p)$. (c) $p \to (q \to (p \wedge q))$. (d) Peirce's law $((p \to q) \to p) \to p$.

23. ★ Show that the linear distributivity $A \otimes (B \mathbin{\wp} C) \multimap (A \otimes B) \mathbin{\wp} C$ is derivable in MLL. Then show, with the Danos–Regnier criterion, that the converse $(a \otimes b) \mathbin{\wp} c \multimap a \otimes (b \mathbin{\wp} c)$ is not derivable for distinct atoms $a, b, c$.

24. ★ The space $!\mathbf{Bool}$ has as web the finite cliques $\emptyset$, $\set{t}$, $\set{f}$ of $\mathbf{Bool}$. Count the cliques of $!\mathbf{Bool}$ and of $!\mathbf{Bool} \multimap \mathbf{Bool}$, and match the cliques of $!\mathbf{Bool} \multimap \mathbf{Bool}$ with the stable functions from $\mathrm{Cl}(\mathbf{Bool})$ to $\mathrm{Cl}(\mathbf{Bool})$.

25. ★ Show that $(\mathbf{Bool} \mathbin{\&} \mathbf{Bool}) \multimap \mathbf{Bool}$ has $17$ cliques, and that no clique contains tokens from both components of $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$. What does this say about linear functions of two booleans, and about the left-sequential and?

26. ★ In the two-point Routley–Meyer model of exercise 20, show that the mingle formula $A \rightarrow (A \rightarrow A)$ is true at $0$ for every formula $A$ and every valuation. What does this say about the use of the model for $\mathbf{R}$?

27. ★ Use the $[0, 1]$ valuation of the [contraction](/V0MZVC2XA9/) entry to show that $(p \multimap q) \otimes (p \multimap r) \multimap (p \multimap q \otimes r)$ is not derivable in affine logic. Show that $(p \multimap q) \mathbin{\&} (p \multimap r) \multimap (p \multimap q \mathbin{\&} r)$ is derivable already in linear logic.
