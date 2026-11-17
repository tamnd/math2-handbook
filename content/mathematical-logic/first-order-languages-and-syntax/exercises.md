1. ◦ The [signature](/WDVVEYD6AT/) has a binary function symbol $f$, a unary function symbol $g$ and a constant $c$. Which of these strings are [terms](/6D3WA7N2W4/): $f(x, g(c))$, $g(x, y)$, $f(g(g(x)))$, $c(x)$, $g(f(c, y))$?

2. ◦ The signature has one binary function symbol $f$ and one constant $c$. List the closed terms with exactly two occurrences of $f$. How many closed terms have exactly three?

3. ◦ In the formula $(\forall x \, (R(x, y) \to \exists y \, R(y, z)) \land P(x))$, find the set of [free variables](/9CNGDRAMGC/), the variables that have bound occurrences, and every free occurrence.

4. ◦ Which of these formulas are [sentences](/DKFGQTRYZE/): $\forall x \, \exists y \, (y < x)$, $\; \forall x \, (x < y \to \exists y \, (y < x))$, $\; \exists x \, (x = x)$, $\; \forall x \, R(x, c)$, where $c$ is a constant?

5. ◦ Let $\varphi$ be $(\forall y \, R(x, y) \lor \exists x \, P(x))$. Write out $\varphi[f(z)/x]$. Is $f(y)$ substitutable for $x$ in $\varphi$?

6. ◦ Which of these formulas are in [prenex normal form](/CS82V969DE/): $\forall x \, \exists y \, (R(x, y) \land P(x))$, $\; \forall x \, P(x) \to \exists y \, Q(y)$, $\; \exists x \, \neg \forall y \, R(x, y)$, $\; \forall x \, \exists y \, \neg R(x, y)$?

7. ◦ Write the [Skolem normal form](/GCPQGMJYEV/) of $\exists u \, \forall x \, \exists y \, \forall z \, \exists v \, R(u, x, y, z, v)$. How many new symbols does it use, and what are their arities?

8. • In the language $\set{<}$ of orders, with equality, write sentences that say: the order is dense; there is a least element; every element has an immediate successor.

9. • In the language $\set{+, -, \cdot, 0, 1}$ of rings, write a formula $d(x, y)$ that says "$x$ divides $y$", a sentence that says the ring has characteristic $3$, and a sentence that says every element is a square. Explain why your second sentence is correct.

10. • Suppose every function symbol of the signature is binary. Prove by induction on terms that every term has exactly one more occurrence of variables and constants than of function symbols.

11. • Let $\varphi$ be $\exists y \, (x < y)$. Replace $x$ by $y$ in $\varphi$ without checking [substitution](/NCDZ969V7X/) conditions, and show that $\forall x \, \varphi$ is true in $(\N, <)$ while the result is false there. Then give the correct $\varphi[y/x]$.

12. • Using only the [equality axioms](/Q1494G7FBM/) of reflexivity and substitution, show that $=$ is symmetric and transitive.

13. • Replace the unary function symbol $f$ by a binary relation symbol $R$ meant as its graph. Write a sentence saying that $R$ is the graph of a function, and translate the atomic formula $f(f(x)) = y$ into a formula that uses $R$ and no function symbols.

14. • A two-sorted language for plane geometry has a sort of points, a sort of lines and an incidence relation $I(p, l)$. Write "any two distinct points lie on a common line" as a two-sorted sentence, and then as a one-sorted sentence by the relativization of [many-sorted logic](/7TDHDN8P96/), with predicates $\mathrm{Pt}$ and $\mathrm{Ln}$. Which extra axioms does the one-sorted version need?

15. • Show that $\forall x \, P(x) \lor \forall x \, Q(x)$ and $\forall x \, (P(x) \lor Q(x))$ are not equivalent, by a structure with two elements. Then give a prenex formula that is equivalent to the first.

16. • Find two prenex forms of $\forall x \, P(x) \to \exists y \, \forall z \, R(y, z)$ with different quantifier prefixes, and write the Skolem normal form of each.

17. • In the language $\set{<, c}$ with equality, use Russell's analysis of [definite descriptions](/PD2R4XT79Q/) to write "the least element is below $c$". Write the two readings of "the least element is not below $c$", and show that they differ in $(\Z, <)$ with $c$ read as $0$.

18. ★ Write terms in prefix form without brackets or commas, so that $f(x, g(y))$ becomes $f x g y$. Give each $n$-ary function symbol the weight $n - 1$, and each variable and constant the weight $-1$. Prove that a string is a term if and only if its total weight is $-1$ and every proper nonempty initial segment has weight at least $0$.

19. ★ Let $\varphi$ and $\psi$ be quantifier-free, with $u, v$ not free in $\varphi$ and $x, y, z$ not free in $\psi$. Find a prenex form of $\forall x \, \exists y \, \forall z \, \varphi \land \exists u \, \forall v \, \psi$ whose prefix has only three blocks, $\forall \ldots \exists \ldots \forall \ldots$. Why does the obvious method give five blocks?

20. ★ In the language of pure equality, show that $\forall x \, \exists y \, \neg (x = y)$ is not equivalent to any universal sentence. Use the fact that universal sentences are preserved in substructures.

21. ★ Prove that if $t$ is substitutable for $x$ in $\varphi$ and $x \in \mathrm{FV}(\varphi)$, then $\mathrm{FV}(\varphi[t/x]) = (\mathrm{FV}(\varphi) \setminus \set{x}) \cup \mathrm{Var}(t)$. Give an example showing that the equation fails when $t$ is not substitutable.
