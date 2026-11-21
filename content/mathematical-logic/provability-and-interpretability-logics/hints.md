1. (a), (c) and (d) are theorems; (b) and (e) are not. For (d), $\square\Diamond p \to \square\Diamond\top$, and $\square\Diamond\top \to \square\bot$ is the formalized second incompleteness theorem.

3. (a) $\bot$; (b) $\square q$; (c) $\neg\square\bot \wedge \square q$.

6. (a) One: the constant operator $\square x = 1$. (b) $\square\emptyset = \set{0}$, $\square\square\emptyset = \set{0, 1}$ and $\square\square\square\emptyset = W$.

9. Take a root $r$ with $rRa$ and $rRb$, with $p$ true only at $a$ and $q$ true only at $b$. With at most two worlds, each world sees at most one world, and $\square(p \vee q) \to \square p \vee \square q$ holds whenever $R[w]$ has at most one element.

10. Let the root $r$ see $u_1, u_2, e_1, e_2$, let $u_i R e_i$, and make $p$ true only at $e_1$ and $q$ true only at $e_2$. Then $u_1 \Vdash \square p \wedge \neg\square q$ and $u_2 \Vdash \square q \wedge \neg\square p$.

12. In modal form the sentence is $\Diamond\square\bot \leftrightarrow \Diamond\top$. The direction from left to right is normal modal logic. For the other, put $p = \top$ in exercise 8.

14. From $x = \neg\square x$ get $\square x = \neg x$, and the 4 law gives $\square x \le \square\square x = \square\neg x$. So $\square x = \square x \wedge \square\neg x = \square 0$. For the converse, $\square\neg\square 0 = \square(\square 0 \to 0) = \square 0$ by Löb's law.

16. (a) Use axiom 4 for $[0]$, then $[0]X \to [1]X$ with $X = [0]p$. (b) The dual of monotonicity gives $\langle 2 \rangle\top \to \langle 1 \rangle\top$, and the axiom $\langle 1 \rangle\top \to [2]\langle 1 \rangle\top$ with $\langle 2 \rangle\top$ gives $\langle 2 \rangle\langle 1 \rangle\top$, hence $\langle 1 \rangle\langle 1 \rangle\top$.

17. By completeness, work in finite frames. The truth of a letter-free formula at $w$ depends only on the depth of $w$, by induction on the formula. If $A$ holds at all depths, $\square A$ is equivalent to $\top$; otherwise let $k$ be the least depth where $A$ fails. A world of depth $d$ sees worlds of every depth below $d$ and no others, so $\square A$ holds exactly at the worlds of depth at most $k$, and $\square A$ is equivalent to $\square^{k+1}\bot$.

18. If $p$ fails at $n$, take the least $m \le n$ with $\neg p$ at $m$. Then $p$ holds at all $k < m$, so $\square(p \to \square p)$ holds at $m$ while $p$ fails there. So $\square(\square(p \to \square p) \to p)$ fails at $n$.

19. The axiom $\square\bot \to \bot$ gives $\neg\square\bot$. At a world with no successor, $\square\bot$ is true. If $\mathsf{GLS}$ proved $\square\neg\square\bot$, the $\mathsf{GL}$ theorem $\square\neg\square\bot \to \square\bot$ and $\square\bot \to \bot$ would give $\bot$, but $\mathsf{GLS}$ is sound for truth in $\N$.

20. If $A$ fails at $w$ in a finite transitive irreflexive model, add a new world below all worlds of the model. The new frame is still finite, transitive and irreflexive, and $\square A$ fails at the new world.
