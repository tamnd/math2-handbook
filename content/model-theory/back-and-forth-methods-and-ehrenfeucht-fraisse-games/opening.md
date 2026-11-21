Two players look at a linear order with $7$ elements and a linear order with $8$ elements. Spoiler points to an element of one order, Duplicator answers with an element of the other, and after three rounds Duplicator wins if the chosen elements are in the same order on both sides. Duplicator always wins. She answers the middle element $3$ of the first order by $3$ or $4$ in the second, and so on, keeping the gaps "large enough" on each side. With four rounds Spoiler wins. Because each round of the game matches one quantifier, no first-order sentence with quantifiers nested three deep can tell the two orders apart, and some sentence with depth four can. With $n$ rounds the threshold is $2^n - 1$, so no single sentence defines "even size" on finite linear orders.

This is an [Ehrenfeucht–Fraïssé game](/2RE7YAZK8R/), the finite form of Cantor's [back-and-forth method](/6F2DB4HTJR/). The chapter starts with the infinite form, which proves that two countable structures are isomorphic. It then measures sentences by [quantifier rank](/FVEVRE5XNZ/) and turns the finite games into a test for first-order definability.

## What the chapter covers

The chapter is in three groups, read in order.

1. **Back and forth.** The [back-and-forth method](/6F2DB4HTJR/) builds an isomorphism between two countable structures by alternate extensions. A [back-and-forth system](/EWB8KXZMCV/) is a family of finite partial isomorphisms with the extension property in both directions. It exists also between uncountable structures, such as $(\Q, <)$ and $(\R, <)$, that are not isomorphic.
2. **Quantifier rank and the finite games.** [Quantifier rank](/FVEVRE5XNZ/) counts the nesting of quantifiers, and $\equiv_n$ is agreement on sentences of rank at most $n$. The [Ehrenfeucht–Fraïssé game](/2RE7YAZK8R/) $G_n$ has $n$ rounds. The [Ehrenfeucht–Fraïssé theorem](/72BMYXGFA8/) says that Duplicator wins $G_n$ exactly when the structures are $\equiv_n$, for a finite relational signature. [Games on finite linear orders](/ZZPXVVZARC/) work out the case of orders completely.
3. **The infinite game and non-definability.** [Karp's theorem](/KAWWZ2DF0G/) shows that partial isomorphism is equivalence in the infinitary logic $L_{\infty\omega}$, and is isomorphism for countable structures. [Non-definability by games](/VT2PSXKM50/) uses the finite games to prove that parity, connectivity and Hamiltonicity are not first-order on finite structures.

## A first reading

A short course takes these entries in order.

- [Back-and-forth method](/6F2DB4HTJR/), with [Cantor's theorem](/ABN5PTXEHY/) as the model case.
- [Back-and-forth system](/EWB8KXZMCV/), for the definition of $\cong_p$.
- [Quantifier rank](/FVEVRE5XNZ/), which is short but used everywhere after it.
- [Ehrenfeucht–Fraïssé game](/2RE7YAZK8R/), with the worked game on $(\Z, <)$ and $(\Z, <)$ plus a second copy of $\Z$.
- [Ehrenfeucht–Fraïssé theorem](/72BMYXGFA8/), the link between games and logic.
- [Games on finite linear orders](/ZZPXVVZARC/), the key computation.
- [Non-definability by games](/VT2PSXKM50/), the main application.

[Karp's theorem](/KAWWZ2DF0G/) can be skipped at first. It needs infinitary logic, and it leads to Scott sentences and the study of countable models rather than to the finite applications. The harder half of the Ehrenfeucht–Fraïssé theorem, proved with Hintikka formulas, can also wait: non-definability proofs use only the direction from a win for Duplicator to $\equiv_n$.

## Before you start

The chapter assumes the following.

- [Structures, satisfaction and truth](/NJDME6F845/): signatures, formulas and when a formula holds in a structure.
- [Basic notions of model theory](/AY09KYSW81/), for embeddings, isomorphisms and [elementary equivalence](/P3B1V182N4/).
- [Completeness, compactness and interpolation](/FBWW4J1XWG/), for the compactness method that the games replace on finite structures.
- [Linear orders](/0FRXBVVR03/) and the theory of [dense linear orders without endpoints](/2W4S2H4VYA/).
- Countable sets and enumerations, as used in Cantor's theorem.
