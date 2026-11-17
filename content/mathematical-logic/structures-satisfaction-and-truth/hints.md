1. There are $2^3 \cdot 3 = 24$ structures of the first kind: a subset for the relation and an element for the constant. There are $2^4 = 16$ of the second kind, one for each function from $\set{1, 2}^2$ to $\set{1, 2}$.

2. The first and the third are true. The second is false, since each element is related to only one element. The fourth is false: $R(0, 1)$ and $R(1, 2)$ hold, but $R(0, 2)$ does not.

3. The first two are true, with $y = -x$ and $x = 0$. The third is false: $y + y = 1$ has no solution in $\Z$.

5. The first two are valid. $\exists x \, P(x) \to P(c)$ fails when $P$ holds of some element other than $c$. The last fails in $\set{0, 1}$ with $R$ the identity relation.

7. In $(\N, \le)$ Eloise wins by choosing $x = 0$. In $(\Z, \le)$ Abelard wins: whatever $x$ Eloise chooses, he answers $y = x - 1$.

8. $\exists x \, \exists y \, (\neg (x = y) \land \forall z \, (z = x \lor z = y))$, and $\exists x \, \exists y \, \exists z \, \forall w \, (w = x \lor w = y \lor w = z)$.

9. $(\N, <)$ is a model. In a finite model, start anywhere and follow $R$; transitivity and irreflexivity forbid a repeated element, so a finite domain runs out.

12. The density sentence $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \land z < y))$ separates the orders. The sentence $\exists e \, (\forall x \, (x + e = x) \land \forall x \, \exists y \, (x + y = e))$ separates the groups: in $(\N, +)$ the only $e$ is $0$, and $1$ has no inverse.

14. $x < y$ if and only if $\exists z \, (\neg (z + z = z) \land x + z \cdot z = y)$. The condition $\neg (z + z = z)$ says that $z \neq 0$, so $z \cdot z$ ranges over the positive reals.

16. In a Herbrand model the value of $P(f^n(a))$ is forced for every $n$: it is true exactly when $n$ is even. So there is exactly one Herbrand model. A two-element model takes $\set{0, 1}$, $a = 0$, $f$ the swap and $P = \set{0}$.

18. A strategy of Eloise tells her which $y$ to choose after Abelard chooses $x$, so it is a function $g$; it wins when $\varphi[a, g(a)]$ holds for every $a$. For the converse direction, choose $g(a)$ among the witnesses for each $a$, using the axiom of choice when $M$ is not well-ordered.

19. Let $\delta_0(x)$ be $\neg \exists y \, (y < x)$, and let $\delta_{n+1}(x)$ say that $x$ is the immediate successor of an element satisfying $\delta_n$. There are only countably many formulas, and countably many choices of finitely many parameters, but uncountably many subsets of $\N$.

20. The first part is an induction on $\varphi$, starting with terms: $t^{\mathcal{M}}[s] = t^{\mathcal{N}}[s]$ because the operations of $\mathcal{M}$ are restrictions of those of $\mathcal{N}$. For the second part, a universal sentence true in $\mathcal{N}$ has its matrix satisfied by all assignments into $N$, in particular by those into $M$.

21. Show first that $\mathcal{H} \models \varphi[s]$ if and only if $\mathcal{M} \models \varphi[s']$ for quantifier-free $\varphi$, where $s'(x) = s(x)^{\mathcal{M}}$. A universal sentence then holds in $\mathcal{H}$, since its quantifiers range over closed terms, whose values are some of the elements of $M$.
