Some properties of a class of structures can be read off from the shape of its axioms. A universal sentence that holds in a structure holds in each of its [substructures](/676H7EGTKJ/), so a class defined by universal axioms is closed under substructures. The [Łoś–Tarski theorem](/9RN0KYXNT1/) gives the converse: a theory whose class of models is closed under substructures is equivalent to a set of universal sentences. The group axioms show both sides. With multiplication, inverse and identity in the signature they are universal, and the substructures of a group are its subgroups. With the operation alone the substructures are subsemigroups, such as $\set{1, 2, 3, \dots}$ inside $(\Z, +)$, and the axioms of groups need an existential quantifier. Theorems of this kind are [preservation theorems](/T69D2NS1HP/). Others match unions of chains with $\forall\exists$ axioms, surjective homomorphic images with positive sentences, and [reduced products](/F4WRD396PB/) with Horn sentences.

Definability theorems compare two ways in which a theory can determine a relation. A relation symbol $P$ is implicitly defined by $T$ when any two models of $T$ that agree on the other symbols agree on $P$, and explicitly defined when some formula without $P$ is equivalent to it modulo $T$. The [Beth definability theorem](/RJBDSA2ETP/) says that the two agree in first-order logic. In real closed fields the order is implicitly defined by the field operations, and $x \le y \leftrightarrow \exists z \, (y = x + z^2)$ is an explicit definition. Beth's theorem follows from the [Craig interpolation theorem](/E2CBFNAVZY/), and most preservation theorems are proved by compactness with the [diagram lemmas](/EP5E317TNW/). Many of them fail when only finite structures are allowed.

## What the chapter covers

The chapter is in four groups, read in order.

1. **Preservation theorems.** The [general pattern](/T69D2NS1HP/), then the three classical cases: the [Łoś–Tarski theorem](/9RN0KYXNT1/) for substructures and extensions, the [Chang–Łoś–Suszko theorem](/RK7NK2P75J/) for unions of chains, and [Lyndon's theorem](/8DJSRWME2X/) for surjective homomorphisms.
2. **Universal and universal Horn classes.** [Universal classes](/ZSTEZ3PRT9/), with examples from fields, graphs and orders; [universal Horn classes](/9A4CYWXPEA/), closed under reduced products as well; and the theorem that [Horn sentences](/1FF2GRE6VX/) are exactly the sentences preserved under reduced products.
3. **Definability.** The [Beth definability theorem](/RJBDSA2ETP/) and Padoa's method for proving that a relation is not definable; [Svenonius's theorem](/JNXY3WRYFY/), which tests definability by automorphisms of models; and the [Chang–Makkai theorem](/MFR9Z5PPH4/), which counts automorphic images in a saturated model.
4. **Pseudo-elementary classes.** [Classes of reducts](/YEC1Q3A490/) of elementary classes in a larger signature, which are closed under ultraproducts but not under elementary equivalence.

## A first reading

A short course takes these entries in order.

- [Preservation theorems](/T69D2NS1HP/), for the shape that the later statements share.
- [The Łoś–Tarski theorem](/9RN0KYXNT1/), with its failure over finite structures.
- [The Chang–Łoś–Suszko theorem](/RK7NK2P75J/).
- [Universal classes](/ZSTEZ3PRT9/), with the example of the $k$-colourable graphs.
- [Universal Horn classes](/9A4CYWXPEA/), with partial orders and torsion-free groups.
- [The Beth definability theorem](/RJBDSA2ETP/).
- [Pseudo-elementary classes](/YEC1Q3A490/).

[Lyndon's theorem](/8DJSRWME2X/) and the [Horn sentence theorem](/1FF2GRE6VX/) have harder proofs and can be read after the first pass; their statements are worth knowing at once. [Svenonius's theorem](/JNXY3WRYFY/) and the [Chang–Makkai theorem](/MFR9Z5PPH4/) use elementary extensions and saturated models and fit best after [Types and saturated models](/Z772KEC9BY/).

## Before you start

The chapter assumes the following.

- [Basic notions of model theory](/AY09KYSW81/): [substructures](/676H7EGTKJ/), [embeddings](/SCRB74SWQN/), [reducts](/EY20BF96SJ/) and [elementary classes](/MEC3ZMC4F1/).
- [Elementary extensions and the Löwenheim–Skolem theorems](/2RE7GWWXM5/): the [diagram lemmas](/EP5E317TNW/), the [elementary chain theorem](/NHCRZ74JHH/) and the downward Löwenheim–Skolem theorem.
- [Ultraproducts and product constructions](/HZG1YP26AB/): filters, [reduced products](/F4WRD396PB/), [Łoś's theorem](/AGYBSTD7BG/) and the [characterization of elementary classes](/4HNAJQQ8Z0/) by ultraproducts.
- From Volume 2, the [compactness theorem](/1NR3HAWG9D/), the [Craig interpolation theorem](/E2CBFNAVZY/) and the [Lyndon interpolation theorem](/BRDT1BT7WW/), which the definability and homomorphism proofs use.
- For the last two definability theorems, [saturated models](/RMTZ5J64FX/) from Chapter 4.5.
