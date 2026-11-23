1. $f(x, g(c))$ and $g(f(c, y))$ are terms. $g(x, y)$ and $f(g(g(x)))$ give a symbol the wrong number of arguments, and $c(x)$ gives the constant $c$ an argument, although its arity is $0$.

3. The free variables are $x$, $y$ and $z$, and $x$ and $y$ also have bound occurrences. The free occurrences are $y$ in $R(x, y)$, $z$ in $R(y, z)$ and $x$ in $P(x)$, which lies outside the scope of $\forall x$.

5. $\varphi[f(z)/x]$ is $(\forall y \, R(f(z), y) \lor \exists x \, P(x))$: the $x$ in $P(x)$ is bound and stays. The term $f(y)$ is not substitutable, since the free $x$ in $R(x, y)$ lies in the scope of $\forall y$.

7. $\forall x \, \forall z \, R(c, x, h(x), z, k(x, z))$, with three new symbols: a constant $c$ for $u$, a unary $h$ for $y$ and a binary $k$ for $v$.

8. $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \land z < y))$; $\; \exists x \, \forall y \, (x = y \lor x < y)$; $\; \forall x \, \exists y \, (x < y \land \neg \exists z \, (x < z \land z < y))$.

9. Take $\exists z \, (x \cdot z = y)$, then $(1 + 1) + 1 = 0 \land \neg (1 = 0)$, then $\forall x \, \exists y \, (y \cdot y = x)$. The characteristic divides $3$ when $3 \cdot 1 = 0$, and it is not $1$ when $1 \neq 0$, so it is $3$.

12. The substitution axiom for $=$ gives $(x = y \land x = x) \to (x = x \to y = x)$, and with $x = x$ this yields symmetry. For transitivity, use the instance $(y = x \land z = z) \to (y = z \to x = z)$ together with symmetry and reflexivity.

13. $\forall x \, \exists y \, (R(x, y) \land \forall z \, (R(x, z) \to z = y))$, and $\exists z \, (R(x, z) \land R(z, y))$ for $f(f(x)) = y$.

16. Pulling $\forall x$ out first gives $\exists x \, \exists y \, \forall z \, (P(x) \to R(y, z))$, with Skolem form $\forall z \, (P(c) \to R(d, z))$. Pulling $\exists y \, \forall z$ out first gives $\exists y \, \forall z \, \exists x \, (P(x) \to R(y, z))$, with Skolem form $\forall z \, (P(h(z)) \to R(c, z))$.

17. With $\lambda(x)$ for $\forall y \, (x = y \lor x < y)$, the sentence is $\exists x \, (\lambda(x) \land \forall w \, (\lambda(w) \to w = x) \land x < c)$. The wide reading negates the whole sentence; the narrow one puts $\neg (x < c)$ inside. $\Z$ has no least element, so the wide reading is true there and the narrow one is false.

18. One direction is an induction on terms. For the converse, use induction on length: a string with these properties that starts with a variable or a constant has length $1$, and one that starts with an $n$-ary $f$ has a rest of weight $-n$. Cut the rest where its running weight first reaches $-1$, then $-2$, and so on down to $-n$; each piece is a term by induction.

19. Since the variables are separate, the existential blocks can be merged: $\forall x \, \exists y \, \exists u \, \forall z \, \forall v \, (\varphi \land \psi)$. Pulling out the quantifiers of the first conjunct and then those of the second gives $\forall x \, \exists y \, \forall z \, \exists u \, \forall v$, which has five blocks.

20. The sentence is true in a structure with two elements. Any one of its elements forms a substructure with one element, where the sentence is false. A universal sentence true in the larger structure would be true in the substructure.

21. Use induction on $\varphi$; the quantifier case $\forall y \, \psi$ with $y \neq x$ needs $y \notin \mathrm{Var}(t)$, which is what substitutability gives. For a failure, take $\varphi = \exists y \, (x < y)$ and $t = y$: the naive result $\exists y \, (y < y)$ has no free variables.
