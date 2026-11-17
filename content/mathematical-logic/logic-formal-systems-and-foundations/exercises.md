1. ◦ Give the mood and figure of each [syllogism](/MZBNX2T6Q6/), with its traditional name. (a) No perfect square is congruent to $2$ modulo $3$; some even numbers are perfect squares; so some even numbers are not congruent to $2$ modulo $3$. (b) No prime greater than $3$ is a multiple of $3$; some odd numbers are multiples of $3$; so some odd numbers are not primes greater than $3$.

2. ◦ The sentence "every multiple of $6$ is a multiple of $4$" is false. Using only the traditional [square of opposition](/VYNBSVZ2TH/), which of the corresponding E, I and O sentences get a truth value, and which value? Then give the actual truth value of all three.

3. ◦ In classical propositional logic, give a formula $\varphi \lor \psi$ such that $\vdash \varphi \lor \psi$ holds but neither $\vdash \varphi$ nor $\vdash \psi$ holds. Say which of the two claims belongs to the [object language and which to the metalanguage](/D9G8M42GKC/), and why the distinction matters here.

4. ◦ Decide which of these sets of propositional formulas is [consistent](/VM8TQ70CVJ/), giving a valuation or a derivation of a contradiction: (a) $\set{p \lor q,\ \neg p,\ \neg q \lor r,\ \neg r}$; (b) $\set{p \to q,\ q \to r,\ \neg p,\ r}$.

5. ◦ Show that the first-order theory with the two axioms $\exists x\, \exists y\, \neg(x = y)$ and $\forall x\, \forall y\, \forall z\, (x = y \lor y = z \lor x = z)$ is consistent, and find the sizes of all its models.

6. ◦ Let $L$ have one unary relation symbol $P$, let $T$ be the empty theory in $L$, and let $T' = \set{\exists x\, P(x)}$. Is $T'$ a [conservative extension](/N238J43XNE/) of $T$? Give a reason.

7. ◦ In the theory of fields, the formula $x \cdot y = 1$ cannot serve to define a function symbol $x^{-1}$ by an [extension by definitions](/GCK0NN60E4/). Which condition fails? Give a formula $\psi(x, y)$ that does satisfy the condition and agrees with $x \cdot y = 1$ for $x \neq 0$.

8. ◦ Let $D$ be a set with at least two elements. Which subsets of $D$ are invariant under every permutation of $D$? What does the answer say about unary predicates as [logical constants](/2QQ7Q5SKP8/)?

9. • Show that the mood AEE in the first figure (every $M$ is $P$; no $S$ is $M$; so no $S$ is $P$) breaks a rule of distribution, name the rule, and give a counterexample with geometric figures.

10. • Show that Barbari (every $M$ is $P$; every $S$ is $M$; so some $S$ is $P$) is invalid when terms may be empty, with a counterexample from arithmetic. Then show that it is valid when $S$ is nonempty, using Barbara and subalternation.

11. • A [formal system](/439M8B4DY2/) has the alphabet $\set{a, b}$, the single axiom $ab$, and two rules: from $w$ infer $awb$, and from $w$ and $v$ infer $wv$. (a) Derive $aabbab$. (b) Show that every theorem has, in each initial segment, at least as many $a$'s as $b$'s, and conclude that $abba$ is not a theorem.

12. • In the [Hilbert system](/1MGMQX43B8/) with the axiom schemas $\varphi \to (\psi \to \varphi)$ and $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$ and the rule modus ponens, derive $\varphi \to \chi$ from the hypotheses $\varphi \to (\psi \to \chi)$ and $\psi$. Number the lines and justify each one.

13. • On the formulas of propositional logic, define $\Gamma \vdash \varphi$ to hold when $\varphi \in \Gamma$ or $\Gamma$ is infinite. Show that $\vdash$ is a [consequence relation](/J78Y1M4GND/), that it is not finitary, and that it is not structural.

14. • Let $\vdash$ be a consequence relation and $\mathrm{Cn}(\Gamma) = \set{\varphi : \Gamma \vdash \varphi}$. Prove that $\Gamma \subseteq \mathrm{Cn}(\Gamma)$, that $\Gamma \subseteq \Delta$ implies $\mathrm{Cn}(\Gamma) \subseteq \mathrm{Cn}(\Delta)$, and that $\mathrm{Cn}(\mathrm{Cn}(\Gamma)) = \mathrm{Cn}(\Gamma)$. Name the property of $\vdash$ that each step uses.

15. • Add to classical propositional logic the single formula $p \land \neg q$ as a new axiom, not as a schema. Show that the new system does not prove $q$. Explain why this does not contradict the fact that classical propositional logic is [Post complete](/WK2P0E82B4/).

16. • On the chain $0 < \tfrac12 < 1$, let $a \to b = 1$ when $a \le b$ and $a \to b = b$ otherwise, and let $\neg a = a \to 0$. Show that $\varphi \to (\psi \to \varphi)$ takes the value $1$ for all values of $\varphi$ and $\psi$, but $\neg\neg p \to p$ does not. What does this say about the [soundness](/4A84VHDTHV/) of classical logic for this algebra?

17. • In the language $\set{<}$, let $T$ be the theory of strict linear orders, and let $T_1$ be $T$ plus the axiom "there is a greatest element". Let $A$ be the axiom $\forall x\, (x < c \lor x = c)$ for a new constant $c$. Is $T + A$ conservative over $T$? Is $T_1 + A$ conservative over $T_1$? Justify both answers.

18. • In [Peano arithmetic](/HACXBCM7SS/), define $x \mid y$ by $\exists z\, (x \cdot z = y)$. Translate $\forall x\, (x \mid 0)$ and $\forall x\, (1 \mid x)$ back into the language of PA, and say how PA proves each one.

19. • Suppose there are proofs of $\mathrm{Con}(\mathrm{ZF}) \to \mathrm{Con}(\mathrm{ZF} + \varphi)$ and of $\mathrm{Con}(\mathrm{ZF}) \to \mathrm{Con}(\mathrm{ZF} + \neg\varphi)$. Show that if ZF is consistent, then ZF proves neither $\varphi$ nor $\neg\varphi$.

20. ★ In the alpha part of the [existential graphs](/D3ZS6WHPM1/), start from $[P\ [Q]]\ [Q\ [R]]$ and derive $[P\ [R]]$ using only erasure, insertion, iteration, deiteration and the double cut. Give the depth of the area at each step.

21. ★ Count the ternary relations on a set $D$ that are invariant under every permutation of $D$, first when $D$ has at least three elements and then when $D$ has exactly two.

22. ★ Assume that Peano arithmetic is consistent. Use [Gödel's second incompleteness theorem](/4PZM5GJTR5/) to show that $\mathrm{PA} + \neg\mathrm{Con}(\mathrm{PA})$ is consistent. Is this theory sound for the standard model?

23. ★ Let $T$ be a consistent theory that contains [Robinson arithmetic](/3K1AKGXF8A/), and assume that $T$ proves every true sentence $\delta(\bar n)$ and the negation of every false one, where $\delta(x)$ has only bounded quantifiers. Show that every sentence $\forall x\, \delta(x)$ that $T$ proves is true in $\N$. Explain why this result was central to [Hilbert's program](/P1RW6JWX73/).

24. ★ Let $\Gamma$ be a consistent set of formulas of classical propositional logic in countably many variables. Without Zorn's lemma, build a set $\Gamma^* \supseteq \Gamma$ that is consistent and contains, for each formula $\varphi$, either $\varphi$ or $\neg\varphi$.
