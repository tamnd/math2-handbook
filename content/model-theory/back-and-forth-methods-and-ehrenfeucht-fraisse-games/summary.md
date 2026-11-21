## What to remember

- **[Back and forth](/6F2DB4HTJR/):** to build an isomorphism between countable structures, list both domains and extend a finite partial isomorphism alternately, adding the next element of $\mathcal{A}$ to the domain, then the next element of $\mathcal{B}$ to the range. [Cantor's theorem](/ABN5PTXEHY/) on countable dense linear orders without endpoints is the model case. The forth step alone gives an embedding; this is how every countable linear order embeds into $(\Q, <)$.
- **[Back-and-forth system](/EWB8KXZMCV/):** a nonempty family of finite partial isomorphisms such that each member extends inside the family to any new element of either side. Then $\mathcal{A} \cong_p \mathcal{B}$. For countable structures $\cong_p$ is the same as $\cong$; in general it is weaker, since $(\Q, <) \cong_p (\R, <)$.
- **[Quantifier rank](/FVEVRE5XNZ/):** $\operatorname{qr}$ is $0$ for atomic formulas, does not grow under connectives, and grows by one under each quantifier. It measures nesting, not the number of quantifiers, and putting a formula in prenex form can raise it. Over a finite relational signature there are only finitely many formulas of rank at most $n$ in given free variables, up to equivalence.
- **[The game](/2RE7YAZK8R/) $G_n(\mathcal{A}, \mathcal{B})$:** in each of $n$ rounds Spoiler picks an element in either structure and Duplicator answers in the other. Duplicator wins if the map $a_i \mapsto b_i$ is a partial isomorphism at the end.
- **[Ehrenfeucht–Fraïssé theorem](/72BMYXGFA8/):** for a finite relational signature, Duplicator wins $G_n(\mathcal{A}, \mathcal{B})$ exactly when $\mathcal{A} \equiv_n \mathcal{B}$. The direction from a win to $\equiv_n$ holds for every relational signature. So $\mathcal{A} \equiv \mathcal{B}$ exactly when Duplicator wins every $G_n$.
- **Two exact counts:** pure sets of sizes $m$ and $k$ satisfy $\equiv_n$ exactly when $m = k$ or both are at least $n$. [Finite linear orders](/ZZPXVVZARC/) $L_m$ and $L_k$ satisfy $\equiv_n$ exactly when $m = k$ or both are at least $2^n - 1$.
- **[Karp's theorem](/KAWWZ2DF0G/):** $\mathcal{A} \cong_p \mathcal{B}$ exactly when they agree on all sentences of $L_{\infty\omega}$, and exactly when Duplicator wins the game $G_\omega$ of infinite length.
- **[Non-definability](/VT2PSXKM50/):** to show that no first-order sentence defines a property $P$, give for each $n$ a structure with $P$ and one without $P$ on which Duplicator wins $G_n$. On finite structures this replaces compactness, and it shows that even size, connectivity and Hamiltonicity are not first-order.

## Pairs worked out in the chapter

| Structures | Duplicator wins | Conclusion |
|---|---|---|
| Sets of sizes $m \ne k$ | $G_n$ when $m, k \ge n$ | $\equiv_n$ for $n \le \min(m, k)$ |
| Linear orders $L_m$ and $L_k$, $m \ne k$ | $G_n$ when $m, k \ge 2^n - 1$ | $L_7 \equiv_3 L_8$, $L_7 \not\equiv_4 L_8$ |
| $(\Z, <)$ and $(\Q, <)$ | $G_2$ but not $G_3$ | $\equiv_2$ and $\not\equiv_3$ |
| $(\Z, <)$ and two copies of $(\Z, <)$ in a row | every $G_n$, but not $G_\omega$ | $\equiv$ but not $\cong_p$ |
| $(\Q, <)$ and $(\R, <)$ | $G_\omega$ | $\cong_p$ and $\equiv_{\infty\omega}$, but not $\cong$ |

: Five pairs of structures from the entries of the chapter. Each row gives the games that Duplicator wins and the equivalence that follows.

## Common errors

- **Dropping the back step.** Forth alone gives only an embedding. The integers embed into the rationals, but the attempt to go back fails at the first element between two integers.
- **Counting quantifiers instead of nesting.** The sentence $\exists x\, P(x) \wedge \exists y\, Q(y)$ has rank $1$, though it has two quantifiers; its prenex form $\exists x\, \exists y\, (P(x) \wedge Q(y))$ has rank $2$.
- **Trusting one pair.** A single pair $\mathcal{A}, \mathcal{B}$ with $\mathcal{A} \equiv_n \mathcal{B}$ only rules out sentences of rank at most $n$. A non-definability proof needs a pair for every $n$.
- **Forgetting equality.** A partial isomorphism must preserve $=$ too. If Spoiler picks a new element, Duplicator must also pick a new one; this is why a set of $n - 1$ elements loses to a set of $n$ elements in $G_n$.
- **Using the theorem outside its hypotheses.** With infinitely many relation symbols, or with a function symbol, two structures can satisfy $\equiv_1$ while Spoiler wins $G_1$. The direction from a win for Duplicator to $\equiv_n$ survives for every relational signature; replace functions by their graphs before playing.
- **Reading $\cong_p$ as isomorphism.** Outside countable structures a back-and-forth system gives agreement in $L_{\infty\omega}$, not an isomorphism.
