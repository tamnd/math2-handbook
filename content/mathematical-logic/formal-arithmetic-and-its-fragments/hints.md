2. (a) $\Delta_0$. (b) $\Sigma_2$. (c) $\Pi_2$. (d) $\Sigma_1$.

3. (a), (b), (c) and (e). Not (d): see the non-standard model in the entry on [Robinson arithmetic](/3K1AKGXF8A/).

4. The moduli are $7$, $13$ and $19$, and the values are $2$, $0$ and $1$. With $d = 1$ the first modulus is $2$, so $\beta(c, 1, 0)$ is $0$ or $1$.

6. No, no and no. Yes: by compactness it has countable non-standard models.

7. Both sentences are true, the first is $\Sigma_1$ and the second is the negation of a $\Delta_0$ sentence, so $\Sigma_1$-completeness applies to each.

8. (a) true, (b) false, (c) true, (d) true.

9. Put $n + a = a + n = a + a = a$, $a \cdot 0 = 0$ and $x \cdot y = a$ for every other product with $a$ in it. The axioms $x \cdot Sy = x \cdot y + x$ force $n \cdot a = n \cdot a + n$, which holds with value $a$, so $0 \cdot a = a$ is allowed. In $\mathsf{PA}$, use induction on $0 \cdot x = 0$.

11. Take $\mathsf{Q} + \exists x\, (0 \cdot x \ne 0)$. The theorem says only that $\mathsf{Q}$ proves true $\Sigma_1$ sentences; it says nothing about false ones proved by extensions.

13. Enumerate the theorems of $T$ until $\varphi(\overline n)$ or $\neg\varphi(\overline n)$ appears. One of them appears, and consistency makes the answer right.

14. $\exists c\, \exists d\, (\beta(c,d,0) = \overline 1 \land \forall i < n\, (\beta(c,d,i+1) = \beta(c,d,i) \cdot (i+1)) \land \beta(c,d,n) = y)$, with $\beta$ written out by its $\Delta_0$ definition.

16. A finite axiomatization is one sentence $\sigma$. Its proof from $T$ uses finitely many axioms, all in some $T_n$, so $T_n \vdash \sigma$ and $T = T_n$, a contradiction. Apply it to the chain $\mathrm{I}\Sigma_n$.

17. The sentence $\forall n\, \exists x\, (x \ne 0 \land \forall p < n\, (\mathrm{Prime}(p) \to p \mid x))$ is true in $\N$. Apply it in $M$ to a non-standard $n$.

20. A prime that divides $1 + (i+1)d$ and $1 + (j+1)d$ divides $(j - i)d$. It cannot divide $d$, and $j - i \le s$ divides $d$. Then use the Chinese remainder theorem.

21. Assume there is no least element and prove $\forall x\, \forall y \le x\, \neg\varphi(y)$ by induction on $x$.

22. Let $\theta$ define the halting set $K$. Then $n \notin K$ exactly when $\neg\theta(\overline n)$ is in true arithmetic, so if true arithmetic were computably enumerable, the complement of $K$ would be too.

23. If $\varphi(x, \bar b)$ defined the standard part, it would hold at $0$ and pass from $x$ to $Sx$, so induction would make every element standard.

24. First prove $0 \cdot y = 0$ and $Sx \cdot y = x \cdot y + y$, by induction on $y$, using commutativity and associativity of addition. Then induct on $x$.
