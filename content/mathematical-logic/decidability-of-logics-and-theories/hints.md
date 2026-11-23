1. (a) Computably enumerable, not computable ([Church's theorem](/VA6BNNY2YC/)). (b) Not computably enumerable: its complement, the sentences whose negation is valid, is computably enumerable and not computable. (c) Computably enumerable, not computable (Trakhtenbrot). (d) Not computably enumerable (Trakhtenbrot).

2. (a) Yes, prefix $\exists^2\forall$: a model with at most $2$ elements if any. (b) No. (c) Yes, with $m = 0$: a model with $1$ element if any. (d) No, the prefix is $\exists\forall\exists$.

3. (a) and (b) are guarded. In (c) the guard $P(y)$ does not contain $x$. In (d) no atom contains $x$, $y$ and $z$ together.

4. Odd: $\exists y\, (x = y + y + 1)$, or $\neg D_2(x)$. Congruent to $2$: $\exists y\, (x = y + y + y + 1 + 1)$, or $D_3(x + 1)$.

5. $8$, $3$, $100$ and $1$.

6. (b) and (d) are definable. (a) and (c) are not: the definable sets are eventually periodic, and the gaps between squares, or between powers of $2$, grow without bound.

7. It is decidable, since every sentence is a theorem. It is not essentially undecidable: that notion is defined only for consistent theories, because every theory has the inconsistent extension, which is always decidable.

8. (a) and (c) are first-order: for (c), no position with $b$ comes before a position with $a$. (b) needs monadic second-order logic: guess the set of even positions.

9. (a) Invalid. One element is enough: $S = M = \set{1}$ and $P = \emptyset$. (b) Valid: a witness of "some $S$ are $M$" is in $M$, so it is not in $P$ by the first premise.

10. A substructure of a model of a universal sentence is again a model. With no function or constant symbols, any one element forms a substructure.

11. Such an $f$ would decide finite satisfiability: check the finitely many structures of size at most $f(\abs{\sigma})$ up to isomorphism.

13. Transitivity needs three variables; irreflexivity, totality and "no greatest element" need at most two. In a finite nonempty strict linear order the greatest element exists. So the three-variable fragment lacks the finite model property; in fact it is undecidable.

14. (a) $D_3(x) \land 0 < x$. (b) Always true: one of $x+1$, $x+2$ is even. (c) $D_3(x + 1)$.

16. $x = 0$: $\forall y\, (x \cdot y = x)$. $x = 1$: $\forall y\, (x \cdot y = y)$. Any permutation of the primes extends to an automorphism of $(\N, \cdot)$; one that swaps $3$ and $5$ moves $\set{2,3}$.

17. State $q_0$, accepting, means no $a$ is waiting; state $q_1$ means one is. Reading $a$ goes to $q_1$, reading $b$ goes to $q_0$. The language is the set of words with infinitely many $b$'s.

20. If $T$ has a consistent decidable extension $T'$, extend $T'$ step by step: add each sentence in turn when that keeps $T'$ consistent. Consistency of $T'$ plus finitely many sentences is decidable, so the complete extension is decidable.

21. The identity reduces to $(x + y)z = z^2$, so $z = 0$ or $z = x + y$. Treat the case $x + y = 0$ apart. Then $(\N, +, \cdot)$ is definable in $(\N, S, \cdot)$.

22. Atomic formulas in one variable define finite sets, cofinite sets or residue classes, all eventually periodic. Eventually periodic sets are closed under complement, union and intersection: use the larger threshold and the product of the periods.

23. The symmetric difference of the two languages is $\omega$-regular. If it were nonempty, its Büchi automaton would accept a word that reaches an accepting state on a cycle, and that word can be taken ultimately periodic.

24. Map $(a, b)$ to $a - b$. Equality becomes $a + b' = a' + b$, addition becomes pairwise addition, and quantifiers over $\Z$ become pairs of quantifiers over $\N$.

25. The sentence "there are exactly $n$ vertices" is first-order, and it fails in every member of $\mathcal C$ exactly when $n \notin S$. Seese's theorem says that a decidable theory forces bounded treewidth, not the converse; the converse holds for the class of all graphs of treewidth at most $k$, by Courcelle's theorem, but not for each of its subclasses.
